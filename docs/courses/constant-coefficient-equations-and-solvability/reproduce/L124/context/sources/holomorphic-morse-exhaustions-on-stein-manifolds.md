# Holomorphic Morse exhaustions on Stein manifolds

A Stein manifold has enough holomorphic functions to control its geometry at infinity and near each point. We construct a proper strictly plurisubharmonic function from those two properties, then perturb it so that its differential meets a prescribed cotangent set only at regular transverse points. At such a point, positivity of the Levi form bounds the Morse index. This gives the two local degree estimates needed for ordinary and compactly supported sheaf cohomology.

*Programme exposition by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026; mathematical revision by GPT-6 Astra (OpenAI), Ultra, 7 October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

The finite-parameter argument uses the independent proof of smooth regular values. The analytic application uses [global components and their regular carriers](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/weierstrass-parametrization-and-connected-regular-loci.md#the-global-component-theorem), Cartan's coherent reduced ideal, and local analytic dimension; their precise roles in the bad locus are proved below. The [conormal coefficient calculation and type convention](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/microlocal-composition-and-pure-sheaves/src/pure-and-simple-sheaves-from-directional-tests.md#conormal-sheaves-give-the-normalization-explicitly) supply the normalization in (17). [Complex middle perversity](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/complex-middle-perversity-and-exterior-products.md#the-even-values-determine-the-complex-cuts) explains the interpretation of that normalization, but is not an input to the exhaustion, transversality or local degree calculations. These are links to other programme courses; their proof bodies are not included in the AN-02 reproduction archive. See the [standalone-download prerequisite links](../scope.html#stein-exhaustion-prerequisites) for accessible source readings outside a complete repository checkout.

## Holomorphic convexity controls an exhaustion

Let \(X\) be a complex manifold of dimension \(n\), Hausdorff and countable at infinity. Write \(\mathcal O(X)\) for its global holomorphic functions. For a compact subset \(K\subset X\), define its holomorphic hull by

\[
\widehat K=\{x\in X:|f(x)|\leq\sup_K|f|
                 \text{ for every }f\in\mathcal O(X)\}.
\tag{1}
\]

We use the Stein definition consisting of holomorphic convexity, meaning that every \(\widehat K\) is compact, and local separation: every \(x\) has a neighborhood \(V\) such that for each \(y\in V\setminus\{x\}\) some global holomorphic function has different values at \(x,y\). No global holomorphic coordinate system is assumed.

Choose compact sets \(K_j\) exhausting \(X\), with

\[
K_j=\widehat K_j,\qquad K_j\subset\operatorname{Int}K_{j+1}.
\tag{2}
\]

Here is the construction. Start with any compact exhaustion by neighborhoods, available from a countable relatively compact atlas. At each step choose a compact neighborhood containing the preceding hull and the next set of that exhaustion, and take its hull. The new hull is compact and contains that neighborhood. Also \(\widehat{\widehat K}=\widehat K\): for every \(f\), the supremum on \(\widehat K\) equals the supremum on \(K\), directly from (1). This proves (2).

For \(j\geq2\), let \(S_j=K_{j+1}\setminus\operatorname{Int}K_j\). Every point of this compact shell lies outside \(K_{j-1}=\widehat K_{j-1}\). Hence there is a holomorphic function with value strictly larger there than its supremum on \(K_{j-1}\). Continuity and a finite covering of \(S_j\) give finitely many such functions. After shrinking their covering neighborhoods, each strict ratio has a positive margin. Powers and positive scalar multiples therefore give a finite block \(g_{j,1},\ldots,g_{j,N_j}\) satisfying

\[
\sum_{\nu=1}^{N_j}|g_{j,\nu}|^2\leq 2^{-j}
       \quad\text{on }K_{j-1},\qquad
\sum_{\nu=1}^{N_j}|g_{j,\nu}|^2\geq j^2
       \quad\text{on }S_j.
\tag{3}
\]

More explicitly, normalize a separating function by its nonzero supremum on \(K_{j-1}\). On its chosen shell neighborhood its modulus is at least \(1+\delta\). A high power, multiplied by a scalar at most \((2^{-j}/N_j)^{1/2}\), is as small as required on \(K_{j-1}\) and at least \(j\) on that neighborhood. If the supremum is zero, scalar multiplication alone supplies the large value while retaining zero on \(K_{j-1}\). Empty shells require no functions.

Set

\[
\psi=\sum_{j\geq2}\sum_{\nu=1}^{N_j}|g_{j,\nu}|^2.
\tag{4}
\]

The sum converges with all derivatives on every compact set. To check this assertion, take a coordinate polydisc whose slightly larger closure lies in \(\operatorname{Int}K_m\). For \(j>m+1\), (3) bounds the sum of squared moduli on that larger polydisc by \(2^{-j}\). Cauchy's integral formula in each variable bounds the sum of squared derivatives of any fixed order on the smaller polydisc by a constant times \(2^{-j}\). The product rule and Cauchy–Schwarz give the same summable bound for derivatives of the squared moduli. Finitely many earlier blocks cause no issue. A finite polydisc covering proves the assertion on a compact set.

In particular \(\psi\) is smooth, nonnegative and plurisubharmonic. The Levi form of every summand is \(|dg_{j,\nu}(v)|^2\geq0\), and convergence with two derivatives permits summation. It is proper. Indeed, a point outside \(K_m\) first belongs to some \(K_{j+1}\), with \(j\geq m\); it lies in \(S_j\), so \(\psi\geq j^2\geq m^2\). Thus each closed sublevel of \(\psi\) lies in a compact \(K_m\), and is closed there.

Holomorphic convexity alone supplied this nonnegative plurisubharmonic exhaustion. Strict positivity is a separate local step.

## Local separation supplies strict Levi positivity

Fix \(x_0\). Choose a holomorphic coordinate ball with closed unit ball \(B\) contained in a neighborhood on which global functions separate \(x_0\) from every other point. For each point of \(\partial B\), subtract a function's value at \(x_0\) and rescale it so that its modulus is greater than one there. A finite boundary covering gives global holomorphic functions \(f_1,\ldots,f_N\), and

\[
v=\sum_{\nu=1}^N|f_\nu|^2,\qquad
v(x_0)=0,\qquad v\geq1\text{ on }\partial B.
\tag{5}
\]

In these coordinates let \(q(z)=(1+|z|^2)/3\). It is strictly plurisubharmonic, equals \(1/3\) at the center, and equals \(2/3\) on the boundary.

We need a smooth maximum that preserves plurisubharmonicity. Let \(\kappa_\epsilon\) be an even, nonnegative smooth kernel of integral one supported in \((-\epsilon,\epsilon)\), and let \(\chi_\epsilon=|\cdot|*\kappa_\epsilon\). Then \(\chi_\epsilon\) is smooth, convex, has \(|\chi_\epsilon'|\leq1\), and equals \(|t|\) for \(|t|\geq\epsilon\). Define

\[
M_\epsilon(s,t)=\tfrac12
        (s+t+\chi_\epsilon(s-t)).
\tag{6}
\]

Both first partial derivatives are nonnegative and its real Hessian is positive semidefinite. The chain rule shows that \(M_\epsilon(u,w)\) is plurisubharmonic whenever \(u,w\) are: its Levi form is a nonnegative linear combination of their Levi forms plus the nonnegative quadratic form of that Hessian on their complex first derivatives. Jensen's inequality gives \(\chi_\epsilon\geq|\cdot|\), so \(M_\epsilon\geq\max(s,t)\).

Choose \(\epsilon<1/12\). On \(B\) use \(M_\epsilon(v,q)\), and outside \(B\) use \(v\). By (5) and continuity, \(v-q>\epsilon\) on a collar of the boundary, so the two formulas agree there. Near \(x_0\), \(q-v>\epsilon\), and the formula equals \(q\). We have constructed a global smooth nonnegative plurisubharmonic function \(u_{x_0}\) that is strictly plurisubharmonic near \(x_0\).

Choose a countable covering by these strict-positivity neighborhoods and denote the corresponding functions by \(u_i\). Choose positive constants \(b_i\) so small that, in finitely many fixed coordinate charts covering \(K_i\), all derivatives of \(b_i u_i\) of order at most \(i\) have modulus at most \(2^{-i}\). Then

\[
u=\sum_i b_i u_i,\qquad \rho=\psi+u
\tag{7}
\]

converge smoothly on compact sets. Every summand has nonnegative Levi form, and at each point at least one summand has positive definite Levi form. Thus \(\rho\) is strictly plurisubharmonic. Since \(u\geq0\), its closed sublevels lie in the compact sublevels of \(\psi\). This proves:

**Exhaustion theorem.** Every Stein manifold in the preceding sense has a smooth nonnegative proper strictly plurisubharmonic exhaustion.

This proof includes the local strict-positivity and global convergence arguments. It does not require a finite-dimensional closed holomorphic embedding.

## Small global perturbations can retain all three properties

First dispose of dimension zero, where a smallest Levi eigenvalue would be undefined. A Hausdorff complex zero-manifold is discrete; countability at infinity makes it countable, since every compact subset of a discrete space is finite. If it is infinite, enumerate its points \(x_j\) and put \(\rho(x_j)=j\); for a finite space choose any nonnegative function. This is a smooth nonnegative proper exhaustion, with strictly positive Levi form in the vacuous sense on the zero tangent spaces. Set \(\varphi_a=\rho+1\) for every parameter \(a\) in the unit ball. Here \(T^*X=X\); a bad set decomposed into pieces of dimension less than zero is empty. Every intersection with a zero-dimensional \(\Lambda_0\) is transverse, and every proper sublevel contains only finitely many intersection points. Thus both exhaustion theorems hold in dimension zero, including for the empty manifold. The metric, eigenvalue and spanning-parameter construction that follows is for \(n>0\).

Fix a smooth Hermitian metric. Denote by \(\lambda(x)>0\) the smallest eigenvalue of the Levi form of \(\rho\), relative to that metric. A countable collection of relatively compact real coordinate charts admits compactly supported smooth real functions \(w_i\) whose differentials span \(T_x^*X\) at every \(x\). To construct them, choose a bump function equal to one on a smaller chart, multiply it by each of the real coordinate functions, and take these functions for a countable covering.

Choose positive numbers \(\epsilon_i\) so small that

\[
|\epsilon_i w_i|\leq2^{-i-2},\qquad
\|\mathcal L(\epsilon_iw_i)\|\leq2^{-i-2}\lambda(x)
        \quad\text{on }X,
\tag{8}
\]

and the \(C^i\) norm of \(\epsilon_iw_i\) on each of the first \(i\) compact chart sets is at most \(2^{-i}\). Each choice is possible: \(w_i\) has compact support, \(\lambda\) has a positive minimum there, and the listed norms are finite.

For a real parameter \(a=(a_i)\in\ell^2\), with \(\|a\|<1\), set

\[
\varphi_a=\rho+1+\sum_i a_i\epsilon_iw_i.
\tag{9}
\]

The series and its derivatives converge on compact sets, by Cauchy–Schwarz and the summable bounds. It defines a smooth family in the Hilbert parameter. Formula (8) gives a uniform absolute perturbation less than \(1/2\) and a Levi perturbation of operator norm less than \(\lambda(x)/2\). Consequently every \(\varphi_a\) is nonnegative, proper and strictly plurisubharmonic.

At a fixed base point, varying finitely many \(a_i\) changes \(d\varphi_a\) in every cotangent direction. Positive scaling by \(\epsilon_i\) preserves the spanning property. On any compact base set one finite collection of parameters suffices, by a finite chart covering.

## A generic differential misses the bad cotangent locus

Let \(\Lambda\subset T^*X\) be closed, and let \(\Lambda_0\) be a relatively open smooth submanifold of real dimension \(2n\). Assume the closed complement \(B=\Lambda\setminus\Lambda_0\) has a countable decomposition into smooth pieces of dimension less than \(2n\).

**Analytic bad-locus lemma.** If \(\Lambda\) is a closed complex analytic Lagrangian, its regular locus on which the cotangent projection has locally constant rank can be chosen as \(\Lambda_0\) in this hypothesis. For \(n>0\), its complement is closed analytic and has complex dimension at most \(n-1\) at every point.

Identify the holomorphic cotangent bundle with the real cotangent bundle by taking the real part of a covector. Its complex dimension is \(2n\), and \(\Lambda\) is pure of complex dimension \(n\). Write \(\pi:T^*X\to X\). The [global component theorem and finite-branch proof](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/SH-03/src/weierstrass-parametrization-and-connected-regular-loci.md#a-finite-branch-calculation-controls-global-continuation) give an ambient locally finite family of closed irreducible components \(C\), each with connected dense intrinsic regular locus \(P=C_{\mathrm{reg}}\). Distinct components do not contain each other. On \(P\), let \(r_C\) be the maximum rank of \(d\pi|_{TP}\). This maximum is attained because rank takes values in the finite set \(\{0,\ldots,n\}\). Its rank-drop set \(Z_C\) is a proper analytic subset of the connected manifold \(P\), cut out there by rank minors; for \(r_C=0\) it is empty. The intersections of \(P\) with the other components form another proper analytic subset, by ambient local finiteness and the component theorem. Their union has empty interior in \(P\), so
\[
U_C=P\setminus\left(Z_C\cup\bigcup_{D\ne C}D\right)
\]
is dense in \(P\). Every point of \(U_C\) is regular for the entire \(\Lambda\), with projection rank \(r_C\). A regular point with locally constant projection rank must have this maximal rank: otherwise an open subset of the connected \(P\) would lie in its proper analytic rank-drop set. Thus \(\Lambda_0=\bigcup_C U_C\) is exactly the stated regular locally constant-rank locus.

We must still prove that its complement stays analytic across the singular points. Work in an ambient cotangent coordinate neighborhood \(V\). Cartan's coherence theorem, Theorem 1.1, applied to the **reduced** ideal sheaf \(\mathcal I_C\), supplies holomorphic functions \(f_1,\ldots,f_N\) that generate that sheaf throughout a smaller \(V\). Generators at just one stalk would not give this neighborhood statement. Put \(J=(\partial f_i/\partial z_j)\), with \(2n\) ambient coordinate columns. At every regular \(y\in C\cap V\), the germs of local submanifold equations belong to \(\mathcal I_{C,y}\), hence are combinations of the \(f_i\); differentiating at their common zero gives
\[
\operatorname{rank}J_y=n,\qquad
\ker J_y=T_yC,\qquad
\operatorname{rank}\begin{pmatrix}J_y\\ D\pi_y\end{pmatrix}
 =n+\operatorname{rank}(d\pi_y|_{T_yC}).
\]
The last equality is linear algebra: restriction of the row space of \(D\pi_y\) to \(\ker J_y\) has kernel its intersection with the row space of \(J_y\). Use of the reduced ideal is essential; replacing its generators by their squares would destroy the tangent-space calculation.

Let \(V_C\subset C\cap V\) be the common zero set of all \((n+r_C)\)-minors of the stacked matrix. On the regular part, it is exactly \(Z_C\cap V\). For \(r_C=0\) these are the \(n\)-minors, so their common zero set has no regular points, as required. The singular locus of \(C\) is analytic by the Jacobian proof of Theorem 2.1. Therefore
\[
(C_{\mathrm{sing}}\cap V)\ \cup\ V_C\
 \cup\left(C\cap V\cap\bigcup_{D\ne C}D\right)
\]
is analytic and equals \((C\setminus U_C)\cap V\). On overlapping coordinate neighborhoods these sets agree: at a singular point membership is automatic, and at a regular point it is the intrinsic rank or component-intersection condition. Hence \(C\setminus U_C\) is closed analytic in the ambient manifold. The locally finite union \(B=\bigcup_C(C\setminus U_C)\) is also closed analytic. This establishes analyticity by actual equations, rather than by an assertion about the closure of \(Z_C\).

For the dimension bound, properness must hold on **every local branch**, even if a globally irreducible \(C\) has several branches at a point \(y\). The finite-branch construction cited above supplies, on each such branch, a dense open smooth part lying in \(P\). It meets every sufficiently small neighborhood of \(y\) in a nonempty open subset of \(P\). Since \(P\setminus U_C\) is a proper analytic subset of the connected \(P\), no such open subset is contained in it. Thus each local branch has good points arbitrarily near \(y\), and the germ of \(C\setminus U_C\) is proper on that branch. Proper-subgerm dimension drop, Proposition 5.5, gives dimension at most \(n-1\) there. Only finitely many components meet a neighborhood of \(y\), so the same bound holds for \(B\).

Finally this analytic bound gives the required countable smooth decomposition without a Whitney stratification theorem. For a closed analytic set of maximum dimension \(e\), take the regular part of each irreducible component after removing its intersections with all other components. These are disjoint locally closed complex submanifolds. The remainder is the locally finite union of component singular loci and intersections; the same branchwise properness and dimension-drop argument gives maximum dimension at most \(e-1\). Repeat. After at most \(n\) rounds starting with \(B\), the remainder is empty. Ambient second countability makes the locally finite component families, and any needed manifold charts, countable. Every resulting piece has real dimension at most \(2n-2<2n\).

If \(n=0\), a closed analytic subset of \(T^*X=X\) is discrete and regular, its projection has rank zero, and \(B=\varnothing\). This proves the lemma in all dimensions. Its analytic inputs are the neighborhood form of Cartan coherence, the finite local-branch and connected regular-carrier theorem, and proper-subgerm dimension drop, with the exact proof links above.

**Generic exhaustion theorem.** There is a dense set of parameters in the open unit ball of \(\ell^2\) for which

\[
\Gamma_{d\varphi_a}\cap\Lambda\subset\Lambda_0,
\qquad \Gamma_{d\varphi_a}\pitchfork\Lambda_0.
\tag{10}
\]

The full intersection is closed and discrete, and each closed sublevel contains only finitely many of its base points.

**Proof.** Take compact neighborhoods \(C_m\) exhausting \(X\). Let \(O_m\) be the parameters for which the section avoids \(B\) over \(C_m\) and is transverse to \(\Lambda_0\) at every intersection there.

These sets are open in the parameter ball. On \(C_m\), the differentials of a sufficiently small parameter neighborhood are uniformly bounded, so their graphs lie in a compact cotangent set. Avoidance of the closed \(B\) persists. Any hypothetical sequence of nontransverse intersections for converging parameters has a convergent cotangent subsequence. Its limit belongs to \(\Lambda_0\), by avoidance of \(B\), and transversality there persists in a smooth chart, a contradiction.

To prove density near an arbitrary parameter \(a\), choose a finite parameter space \(E\) whose differentials span all fibres near \(C_m\). The map

\[
H:U\times E\longrightarrow T^*U,\qquad
(x,e)\longmapsto(x;d\varphi_{a+e}(x))
\tag{11}
\]

is a submersion: the \(x\)-variables supply the base tangent space and the \(e\)-variables supply the entire vertical cotangent space. If \(M=\dim_{\mathbb R}E\), the inverse image of a smooth bad piece of dimension \(b<2n\) is a manifold of dimension \(M+b-2n<M\). Its projection to \(E\) has measure zero. One can see this directly on compact coordinate pieces: a bounded \(C^1\) map from a \(d\)-dimensional cube to \(\mathbb R^M\), \(d<M\), covers its image by \(O(\delta^{-d})\) cubes of diameter \(O(\delta)\), whose total \(M\)-volume tends to zero. Countably many charts and pieces suffice.

The inverse image \(H^{-1}\Lambda_0\) is a smooth \(M\)-manifold. The smooth critical-value theorem, applied to its projection to \(E\), says that its critical values have measure zero. That proof covers arbitrary smooth maps between finite-dimensional countable-at-infinity manifolds, without properness; its independent coordinate argument does not use the Stein cohomology theorem elsewhere in that lesson. All the inverse images here have countable atlases as submanifolds of \(U\times E\). A value \(e\) is regular exactly when the section \(x\mapsto H(x,e)\) is transverse to \(\Lambda_0\). For the linear-algebra verification, quotient the differential of (11) by \(T\Lambda_0\). Its total map is onto. Surjectivity of the projection from the kernel of that quotient to \(E\) is equivalent to surjectivity of the quotient map restricted to the \(x\)-tangent space. The latter is precisely section transversality.

Thus arbitrarily small \(e\) avoid all bad-piece images and all critical values, proving density of \(O_m\). The argument is finite-dimensional; it invokes no infinite-dimensional Sard theorem.

The intersection of the countably many open dense \(O_m\) is dense in the Hilbert parameter ball. Here is the required Baire argument. Inside any parameter ball, choose nested closed balls with radii tending to zero, the \(m\)-th ball lying in \(O_m\) and in the interior of its predecessor. Completeness of \(\ell^2\) gives their common limit, and containment in those interiors keeps it in each \(O_m\) and in the original open unit ball.

For this parameter, (10) holds everywhere. A transverse intersection of two \(2n\)-dimensional submanifolds of the \(4n\)-dimensional cotangent manifold is discrete. The full intersection is closed because \(\Lambda\) and the differential graph are closed. Projection identifies the graph with \(X\); its intersection base is therefore closed and discrete in \(X\). Properness gives compact closed sublevels, which can contain only finitely many points of that set. \(\square\)

The conclusion allows infinitely many critical points in total. It also allows several of them at one critical value. Their values form a locally finite subset of the nonnegative real line.

## The Levi form bounds the real Morse index

Suppose a graph intersection lies at a regular constant-projection-rank point \(p\) of a complex conic Lagrangian. Locally that Lagrangian is an open part of \(T_Y^*X\) for a complex submanifold \(Y\) of dimension \(d\). Indeed, constant rank supplies a smooth local image \(Y\); conicity and Lagrangian isotropy make every covector annihilate \(TY\), and equality of the two Lagrangian dimensions makes the containment open.

The intersection means \(d(\varphi|_Y)=0\). Transversality means its real Hessian is nondegenerate: in adapted base coordinates, the normal conormal coordinates are free, while the tangent differential equations are \(d(\varphi|_Y)=0\); linearizing those equations is exactly that Hessian.

Let \(B\) be this Hessian on the underlying real tangent space of \(Y\), and let \(J\) be multiplication by \(i\). Strict positivity of the restricted Levi form gives

\[
B(v,v)+B(Jv,Jv)>0\quad(v\ne0).
\tag{12}
\]

With the convention \(\mathcal L_\varphi(v)=
\sum\varphi_{z_i\bar z_j}v_i\bar v_j\), the left side is \(4\mathcal L_\varphi(v)\), identifying a real vector with its complex coordinate vector.

If a negative subspace \(W\) of \(B\) had dimension greater than \(d\), then \(W\cap JW\ne0\), by the real dimension formula in a \(2d\)-dimensional space. A nonzero vector in this intersection has both itself and its \(J\)-multiple in \(W\), contradicting (12). Thus the number of negative eigenvalues is at most \(d\). If \(l\) is the number of positive eigenvalues, nondegeneracy gives

\[
d\leq l\leq2d,\qquad q=2d-l\leq d.
\tag{13}
\]

The smooth Morse lemma gives local real coordinates on \(Y\) with

\[
\varphi-\varphi(x_0)=
t_1^2+\cdots+t_l^2-t_{l+1}^2-\cdots-t_{2d}^2.
\tag{14}
\]

The [proof of the Morse lemma with parameters, Lemma 4.1](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/AN-04/reconstructions/20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md#4-a-quadratic-coordinate-system-that-varies-smoothly), supplies this coordinate change, here with no auxiliary parameter. Its construction first chooses a nonzero Hessian pivot, solves the corresponding first-derivative equation by the implicit function theorem, and uses the integral Taylor remainder to write the remaining dependence as \(v^2 A/2\), with \(A\) smooth and nonzero. The change \(v\mapsto v\sqrt{|A|}\) splits off one signed square. The residual Hessian is the invertible Schur complement, so induction splits all variables. Rescaling by \(\sqrt2\) gives precisely the normalization (14). Formula (13) is the additional complex positivity constraint.

## Two closed support tests have opposite degree shifts

Fix a commutative coefficient ring \(k\) of finite global dimension and a bounded coefficient complex \(L\). Suppose the local representative is \(L_Y[d]\), extended from \(Y\). Here \([d]\) is the complex dimension shift and \(H^j(K[s])=H^{j+s}(K)\).

For the quadratic form in (14), the closed upper support test of the unshifted constant coefficient has degree \(q=2d-l\): the pair of a small ball and its negative region contracts to the relative pair \((D^q,S^{q-1})\). Its orientation line is the orientation of the negative eigenspace. Tensoring this finite free relative model with \(L\), then shifting by \(d\), gives

\[
\begin{aligned}
C_+(L_Y[d])&=
\bigl(R\Gamma_{\{\varphi\geq\varphi(x_0)\}}L_Y[d]\bigr)_{x_0}
\simeq L[l-d]\otimes\operatorname{or}(E_-),\\
C_-(L_Y[d])&=
\bigl(R\Gamma_{\{\varphi\leq\varphi(x_0)\}}L_Y[d]\bigr)_{x_0}
\simeq L[d-l]\otimes\operatorname{or}(E_+).
\end{aligned}
\tag{15}
\]

The second formula applies the same argument to \(-\varphi\), whose negative eigenspace has dimension \(l\). Both supports in (15) are closed. Local choices trivialize their orientation lines for a displayed coefficient calculation, but no global trivialization is asserted. These lines are finite free of rank one and do not change a cohomological bound over \(k\).

For a sheaf complex \(F\) known only through microlocal representatives, the upper calculation requires an isomorphism \(F\simeq L_Y[d]\) in \(D^b(X;p)\), whereas the lower calculation requires it in \(D^b(X;-p)\). Each closed test kills the complexes whose microsupport avoids its own displayed covector, by the defining microsupport test. It therefore sends every denominator with such a cone to an isomorphism, and descends to that localized category. When both representatives are given, (15) computes the two actual tests of \(F\). A representative at \(p\) alone has not established the calculation at \(-p\). More generally, the two localized representatives may have different coefficient complexes \(L_+\) and \(L_-\); apply the upper line of (15) to \(L_+\) and the lower line to \(L_-\). No identification of these coefficients is needed. For a complex conic carrier, fibrewise antipodal transport preserves the regular constant-rank locus and its projected germ \(Y\), so the same \(d\) and Hessian can be used for the two calculations. At \(d=0\), both eigenspaces are zero, their orientation lines are \(k\), and both tests are \(L\); the formulas include this case.

Consequently

\[
\begin{aligned}
H^j(C_+)&\simeq H^{j+l-d}(L)\otimes\operatorname{or}(E_-),\\
H^j(C_-)&\simeq H^{j+d-l}(L)\otimes\operatorname{or}(E_+).
\end{aligned}
\tag{16}
\]

If \(L\in D^{\leq0}(k)\), (13) makes \(C_+\in D^{\leq0}(k)\). If \(L\in D^{\geq0}(k)\), it makes \(C_-\in D^{\geq0}(k)\). Neither assertion requires a field or perfect coefficients.

Finally, in complex ambient dimension \(n\), the real conormal codimension is \(2(n-d)\). The [normalized-type formula for a conormal model](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/microlocal-composition-and-pure-sheaves/src/pure-and-simple-sheaves-from-directional-tests.md#type-purity-and-simplicity), equation (16) there, gives \(Q[s+c/2]\) at shift zero for real codimension \(c\). Its preceding relative-sphere and inertia calculations prove the formula for arbitrary bounded coefficient modules, including a zero covector. Thus for \(Q_Y[s]\) it is \(Q[s+(n-d)]\). For the model here it is therefore

\[
\operatorname{type}_0(L_Y[d])=L[n].
\tag{17}
\]

Thus a shift-zero type cut at degree \(-n\) is exactly the coefficient cut at degree zero in (16). This computation explains the dimension normalization used in microlocal perversity. The global ordinary and compact-support arguments use this local estimate with their restriction, inverse-limit and extension-by-zero maps. The equivalence with all stratum cuts is a separate statement in the linked middle-perversity theory; it is not assumed in the construction above.

## Exercises with complete solutions

### Taking a hull twice changes nothing

*Difficulty: Introductory.*

Prove idempotence of the holomorphic hull and explain why the compact sets in (2) can be chosen with interior containment.

**Solution.** For every holomorphic \(f\), definition (1) gives
\(\sup_{\widehat K}|f|\leq\sup_K|f|\). The reverse inequality follows from \(K\subset\widehat K\), so the suprema are equal. The inequalities defining the hull of \(\widehat K\) are therefore exactly those defining \(\widehat K\), proving idempotence. Given the preceding compact hull, cover it and the next compact exhaustion set by finitely many relatively compact coordinate neighborhoods; their closures form a compact neighborhood. Its hull is compact by holomorphic convexity, contains that neighborhood, and is already a hull by idempotence. The preceding compact set lies in its interior. This recursive construction also contains every exhaustion set and hence covers \(X\).

### A power can be small inside and large outside

*Difficulty: Intermediate.*

On \(\mathbb C\), let \(K_{j-1}=\{|z|\leq r\}\) and consider a compact shell on which \(|z|\geq R>r>0\). Construct a holomorphic function whose modulus is at most \(\eta>0\) on \(K_{j-1}\) and at least \(A>0\) on the shell.

**Solution.** Take \(g(z)=\eta(z/r)^m\). Its modulus on \(K_{j-1}\) is at most \(\eta\), while on the shell it is at least \(\eta(R/r)^m\). Choose an integer \(m\) with \((R/r)^m\geq A/\eta\), possible because \(R/r>1\). Then \(g\) has both required bounds. For finitely many covering neighborhoods choose each function's \(\eta=(2^{-j}/N_j)^{1/2}\) and \(A=j\). Every shell point lies in at least one such neighborhood, so that one squared modulus supplies \(j^2\), while their sum on the earlier compact set is at most \(2^{-j}\). The strict inequality of radii models the positive ratio margin needed in the general proof.

### Why smoothing the maximum is legitimate

*Difficulty: Intermediate.*

Compute the first derivatives and Hessian of (6), and prove the asserted preservation of plurisubharmonicity, including where the two functions have equal values.

**Solution.** With \(r=s-t\), the first derivatives are
\(M_s=(1+\chi_\epsilon'(r))/2\) and
\(M_t=(1-\chi_\epsilon'(r))/2\), both nonnegative. The Hessian is
\(\chi_\epsilon''(r)\begin{pmatrix}1&-1\\-1&1\end{pmatrix}/2\), which is positive semidefinite. For a complex tangent vector \(v\), the Levi chain rule gives
\(M_s\mathcal L_u(v)+M_t\mathcal L_w(v)\) plus this Hessian evaluated on the complex pair \((\partial u(v),\partial w(v))\). All terms are nonnegative if \(u,w\) are plurisubharmonic. Smoothness of \(\chi_\epsilon\) makes the same calculation valid at \(u=w\). If \(s-t>\epsilon\), then \(\chi_\epsilon(s-t)=s-t\) and \(M=s\); if \(t-s>\epsilon\), \(M=t\). These exact equalities justify the collar gluing and the strictly positive neighborhood at the center.

### A strict Levi form does not itself imply a Morse function

*Difficulty: Intermediate.*

For real numbers \(a_1,\ldots,a_d\), calculate the Levi form and real Hessian at zero of
\(\varphi(z)=\sum_i|z_i|^2+\operatorname{Re}\sum_i a_i z_i^2\).
Show that the index bound in (13) is sharp.

**Solution.** Writing \(z_i=x_i+iy_i\) gives
\(\varphi=\sum_i(1+a_i)x_i^2+(1-a_i)y_i^2\).
The Levi matrix is the identity, since the added real part is pluriharmonic. The real Hessian eigenvalues are \(2(1+a_i)\) and \(2(1-a_i)\). If every \(a_i>1\), exactly \(d\) eigenvalues are negative and \(d\) positive: \(q=l=d\), attaining the bound. If some \(a_i=1\), the corresponding \(y_i\) eigenvalue is zero despite strict Levi positivity. A genericity step is therefore necessary. The example is a local Hessian calculation; with \(a_i>1\) the function is unbounded below and is not the proper exhaustion constructed above.

### Avoiding the singular meeting of two conormals

*Difficulty: Intermediate.*

On \(X=\mathbb C\), let \(\Lambda\) be the union of the zero section and \(T_{\{0\}}^*\mathbb C\). For \(\varphi_a(z)=|z-a|^2\), determine the intersections and identify the excluded parameter.

**Solution.** The zero-section intersection is \((a;0)\). The point-conormal intersection has base zero and real covector
\(-2\operatorname{Re}(\bar a\,dz)\). If \(a\ne0\), these points are distinct and regular on their respective components. The first intersection is transverse because the real Hessian of \(\varphi_a\) is \(2I\); the second is transverse because a differential graph projects isomorphically to the base while the point conormal is vertical. Their function values are zero and \(|a|^2\). If \(a=0\), both intersections coincide at the singular point \((0;0)\) of the union. This parameter is excluded by bad-locus avoidance, even though \(\varphi_0\) is strictly plurisubharmonic and has a nondegenerate ordinary Hessian.

### The two tests can occupy different degrees

*Difficulty: Advanced.*

Let \(L=k\) in degree zero. Compute the nonzero degrees in (15) for \(l=d\) and for \(l=2d\). Then explain why the upper and lower local vanishing claims hold for arbitrary bounded coefficient complexes in their specified cuts.

**Solution.** The upper complex has shift \(l-d\) and hence its nonzero degree is \(d-l\). The lower complex has shift \(d-l\) and nonzero degree \(l-d\). For \(l=d\), both lie in degree zero. For \(l=2d\), they lie in degrees \(-d\) and \(d\), respectively. Each carries the specified rank-one orientation coefficient. For \(L\in D^{\leq0}\) and \(j>0\), the upper group is \(H^{j+l-d}(L)=0\), since \(l-d\geq0\). For \(L\in D^{\geq0}\) and \(j<0\), the lower group is \(H^{j+d-l}(L)=0\), since \(d-l\leq0\). Tensoring with the orientation line preserves these bounds over any permitted ring. Using the upper formula for the lower support would reverse the needed estimate.

## Sources and the next argument

The proof combines the holomorphic-shell exhaustion, regularized maximum and convergence estimates with a compactly supported perturbation family. Its finite-dimensional transversality reduction uses the linked smooth critical-value proof; its analytic application uses the reduced-ideal bad-locus lemma proved here. Cartan coherence, finite analytic branches and local analytic dimension are the stated analytic inputs, with their programme proofs linked at the point of use. Those proofs in turn use Oka coherence, Weierstrass preparation, local holomorphic algebra and the identity theorem. The Morse coordinate proof and normalized-type calculation are also linked at their exact statements. These external-to-the-archive prerequisites are part of the mathematical scope of this lesson.

The classical analytic definitions and exhaustion methods come from Jean-Pierre Demailly, [Complex Analytic and Differential Geometry, version of 21 June 2012, Chapter I](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf): §5, Lemma 5.18, p. 43, for the regularized maximum; §6, Theorem 6.14, pp. 49–50, for the holomorphic-shell construction; and Definition 6.16, Lemma 6.17 and Theorem 6.18, p. 51, for the Stein definition and the local quadratic patch leading to a strict exhaustion. This includes the classical choice \(q=(1+|z|^2)/3\) in that patch. The present independently expressed proof supplies the finite separation margins, convergence estimates, two-variable convolution calculation, cotangent genericity argument, analytic bad-locus bridge and two signed local support calculations. No source prose or images are reproduced.

These results supply the geometric prerequisite for Stein cohomology. Passing to global cohomology requires the ordinary restriction maps with degree-zero surjectivity, the derived inverse-limit term, and the compact-support direct-limit maps treated there.

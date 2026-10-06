# Global solvability and the excursions of characteristics

Local existence near an escaping compact set does not by itself produce a solution on the whole manifold. The additional geometry concerns returns: a characteristic may start and finish over one fixed compact set while making excursions that approach infinity or a missing boundary point. This lesson connects those excursions to singular support and to global existence modulo a smooth error.

Let \(X\) be a Hausdorff, second-countable smooth manifold without boundary, of dimension at least one. Use scalar complex half-densities, \(D=-i\partial\), and the integrated pairing \((u,v)\), linear in \(u\). Let \(P\in\Psi^m_{1,0}(X)\) be properly supported, with a real homogeneous principal symbol \(p\), of degree \(m\in\mathbb R\). Assume **global real principal type**: no complete characteristic strip remains over a compact subset of \(X\). Completeness means the maximal strip, not necessarily an infinite interval of the original degree-\(m\) Hamilton parameter.

The complete local ingredients are smooth propagation, Sections 2–5; fixed-order propagation, Sections 1–5; compact-tube quantization, Sections 1–5; and finite singular-ray realization, Sections 1–3. The realization gives a compactly supported distribution of any specified Sobolev threshold on any nontrivial compact characteristic segment with injective cosphere projection, with forcing singularities at exactly its two ends. Compact-set solvability, Section 1, supplies the full order normalization and homogeneous-lift argument.

The exact functional foundations are AN-03 Banach estimates, quotient spaces and compact parameter arguments, Sections 14.1–14.2 for smooth-space completeness, 14.4–14.5 for the full Fréchet closed-graph proof, and 14.7 for extension under an arbitrary seminorm bound. The proper all-real Sobolev mapping and coordinate gluing are proved in AN-03 Detecting regularity without choosing coordinates, Sections 11–12, G30–G37. On fixed compact supports, these estimates and Sobolev embedding give the full smooth continuity used below. We supply the global receiving arguments, including the entire functional-analytic implication.

## 1. Three conditions, with their exact quantifiers

Consider:

**(A) Global existence modulo smooth functions.** For every \(f\in\mathcal D'(X)\), there is \(u\in\mathcal D'(X)\) such that \(Pu-f\in C^\infty(X)\).

**(B) Control of adjoint singular support.** For every compact \(K\subset X\), there is a compact \(K'\subset X\) such that

\[
v\in\mathcal E'(X),\qquad
\operatorname{sing\,supp}(P^*v)\subset K
\quad\Longrightarrow\quad
\operatorname{sing\,supp}v\subset K'.
\tag{GS1}
\]

**(C) Control of characteristic excursions.** For every compact \(K\subset X\), there is a compact \(K'\subset X\) containing every characteristic interval whose two endpoints lie over \(K\).

**Theorem 1.1.** Under the stated global real-principal-type hypotheses, (A), (B) and (C) are equivalent.

The compact bound may depend on \(K\), but it cannot depend on the particular interval or the particular adjoint input. All intervals and all compactly supported distributions are included. The right side of (A) permits a global smooth error; it does not assert exact surjectivity of \(P:\mathcal D'\to\mathcal D'\).

Fix a positive degree-one cotangent norm \(w\), and normalize by \(\widetilde p=w^{1-m}p\). On the characteristic set,

\[
H_{\widetilde p}=w^{1-m}H_p.
\tag{GS2}
\]

The full normalization and homogeneous-lift proof in the preceding lesson shows that the projected field \(W\) is smooth on the positive cosphere bundle and that a curve confined over a compact set has a complete homogeneous lift. The radial equation has the form \(d\log w/dt=a\), with \(a\) bounded on every compact cosphere set, so neither fiber zero nor fiber infinity is reached in finite normalized time. We may therefore work with \(W\) for every real \(m\), without invoking a global order-changing parametrix.

There is no stationary characteristic point of \(W\): its constant projected curve would lift to a complete strip over one point. There is also no periodic projected orbit: its compact projected cycle would lift to a complete strip over a compact set. Uniqueness of the ordinary differential equation now makes every finite projected characteristic interval injective. Thus every nontrivial finite interval satisfies the precise cosphere condition of the finite-ray realization.

## 2. Singular support is controlled exactly by excursions

**(B) implies (C).** Enlarge the compact \(K'\) supplied by (B) to contain \(K\). Given a nontrivial compact characteristic interval with endpoints over \(K\), apply the full finite-ray realization to \(P^*\), whose principal symbol is the same real \(p\). Choose threshold zero. The resulting \(v\in\mathcal E'(X)\) has its entire interval as wavefront set, and its adjoint forcing has wavefront set equal to the two endpoint rays. Consequently its forcing singular support lies in \(K\), while its singular support contains the base projection of every point of the interval. Formula (GS1) puts that entire projection in \(K'\). Degenerate one-point intervals are already contained in \(K\).

**(C) implies (B).** Suppose \(\operatorname{sing\,supp}(P^*v)\subset K\), with \(v\) compactly supported. Enlarge the bound in (C) to contain \(K\). Elliptic regularity removes every noncharacteristic point of \(\operatorname{WF}(v)\) outside \(K\). If a characteristic point over \(x\notin K'\) remained, propagation would retain its singularity in both directions until a projected curve reaches a point over \(K\).

Both directions cannot reach \(K\): the finite interval between those two visits would contain \(x\), contrary to (C). At least one maximal half-orbit therefore avoids \(K\). Parametrize it outward by \(t\geq0\), using \(W\) or \(-W\) as appropriate. Every finite piece of that half-orbit remains in \(\operatorname{WF}(v)\), hence over the compact set \(\operatorname{supp}v\). The compact ODE continuation argument makes its normalized time extend to infinity.

Here is the full limiting argument. For times \(t_j\to+\infty\), select a subsequence of projected points converging to \(z\) in the compact cosphere bundle over \(\operatorname{supp}v\). Fix \(T>0\). For large \(j\), the intervals \([t_j-T,t_j+T]\) lie in the half-orbit. Compact ODE bounds and continuous dependence show that the solution through \(z\), on \([-T,T]\), stays over \(\operatorname{supp}v\). The same argument extends it for every \(T\); uniqueness identifies the extensions. Its complete homogeneous lift stays over that compact set, contradicting global real principal type. Therefore no such \(x\) exists, and (GS1) follows.

The same argument with forcing smooth everywhere gives the useful special case

\[
v\in\mathcal E'(X),\quad P^*v\in C^\infty(X)
\quad\Longrightarrow\quad v\in C^\infty_c(X).
\tag{GS3}
\]

This statement does not say that the smooth compact kernel vanishes.

## 3. Unbounded excursions obstruct global existence

We prove the contrapositive of (A) implies (C), retaining the interval-selection and summation details.

Suppose (C) fails for one compact \(K\). Choose an increasing compact exhaustion \(B_j\), with \(K\subset B_1\). At step \(j\), enlarge \(B_j\) by the base projections of the finitely many previously selected intervals. Failure of (C) supplies another interval with endpoints over \(K\) and an interior point \(x_j\) outside that enlarged compact set.

Cut this interval at the last visit to \(K\) before \(x_j\), and the first visit to \(K\) after \(x_j\). These visits exist because the original parameter interval is compact and the inverse image of \(K\) is closed. Denote the resulting projected interval by \(I_j=[a_j,b_j]\), and the point over \(x_j\) by \(c_j\). Its open interior avoids \(K\).

The interiors of different \(I_j\) are disjoint in the cosphere bundle. Indeed, two projected characteristic curves that meet coincide by uniqueness. On that common orbit, an interior is one connected component of the times whose base lies outside \(K\); its bounding visits are exactly its endpoints. Overlapping interiors would therefore give the same excursion. But \(x_j\) was chosen outside the base projection of every earlier closed interval. Endpoints over \(K\) may coincide; this does not affect the argument.

Apply the exact realization to the half-interval \([a_j,c_j]\), with threshold \(-j\). Obtain \(u_j\in\mathcal E'(X)\) satisfying

\[
\operatorname{WF}(u_j)=\mathbb R_+[a_j,c_j],\qquad
\operatorname{WF}(Pu_j)=\mathbb R_+a_j\cup\mathbb R_+c_j,
\qquad
u_j\notin H^{-j}_{\mathrm{mic}}
\text{ at every point of }[a_j,c_j].
\tag{GS4}
\]

Here the notation \(\mathbb R_+\) means the positive cone generated by the projected covectors. Since \(x_j\notin B_j\) and the initial endpoint lies over \(K\), choose a compact base cutoff \(\chi_j\), equal to one near \(x_j\), supported in \(X\setminus B_j\), and zero near the initial endpoint. Put

\[
f_j=\chi_j Pu_j,\qquad
g_j=(1-\chi_j)Pu_j.
\tag{GS5}
\]

The exact two forcing rays give

\[
\operatorname{WF}(f_j)=\mathbb R_+c_j,\qquad
\operatorname{WF}(g_j)=\mathbb R_+a_j.
\tag{GS6}
\]

The supports of the \(f_j\) are locally finite: each lies outside \(B_j\), and the exhaustion absorbs every compact set. Thus

\[
f=\sum_j f_j
\tag{GS7}
\]

is one well-defined global distribution.

Suppose \(Pu-f\) were smooth for some \(u\in\mathcal D'(X)\). A distribution has some finite negative Sobolev order on a neighborhood of a fixed compact set. Indeed, localize in finitely many charts. For a compact distribution of test-function order \(N\), differentiating the compactly cut-off Fourier test gives \(|\widehat{\chi u}(\xi)|\leq C\langle\xi\rangle^N\). Any \(s<-N-n/2\) makes \(\langle\xi\rangle^s\widehat{\chi u}\) square integrable. The full programme Fourier characterization of Sobolev spaces and all-real chart invariance identify this with \(H^s\); take one sufficiently negative order for the finite chart family. Therefore \(u\in H^s_{\mathrm{loc}}\) near \(K\).

Choose \(j\) with \(-j\leq s\). At an interior point sufficiently close to \(a_j\), the base still lies in that neighborhood of \(K\). Formula (GS4) and \(H^s_{\mathrm{mic}}\subset H^{-j}_{\mathrm{mic}}\) show that \(u-u_j\) is not microlocally \(H^s\) there. At the other endpoint \(b_j\), however, \(u\) is microlocally \(H^s\) and \(u_j\) is microlocally smooth: \(b_j\) is outside its half-interval wavefront set, by injectivity of the full projected interval.

On the interval from that initial interior point to \(b_j\),

\[
P(u-u_j)=Pu-f+\sum_{k\ne j}f_k-g_j
\tag{GS8}
\]

is microlocally smooth. The first term is smooth by assumption. Local finiteness makes the sum an actual distributional sum, with no limiting wavefront defect. Its only possible covectors are the \(c_k\), which lie in distinct open excursion interiors. The covector \(a_j\) of \(g_j\) is excluded from this shortened interval. Fixed-order propagation, in both directions and at every real \(m\), now propagates the \(H^s\) membership at \(b_j\) to the initial interior point. This is a contradiction. Hence (A) fails.

We used the full original interval, whose **two** endpoints are over \(K\). The realized singular ray occupies only its first half. It is the regularity at the other original endpoint that supplies the contradiction.

## 4. A global estimate on the test space

To prove (B) implies (A), we construct a test-space estimate and use one global Hahn–Banach extension. For a compact set \(A\), write \(\mathcal D(A)\) for the smooth test sections with support contained in that set.

Choose compact exhaustions interleaved so that

\[
K_j\subset K_j'\subset\operatorname{int}K_{j+1},\qquad
\operatorname{sing\,supp}(P^*v)\subset K_j
\Longrightarrow
\operatorname{sing\,supp}v\subset K_j'.
\tag{GS9}
\]

Take \(K_{-1}=K_0=K_{-1}'=K_0'=\varnothing\), justified by (GS3). At each later step add the previous bound and a prescribed ordinary exhaustion compact before selecting the next bound; this produces the stated nesting and exhaustion.

For a given \(f\in\mathcal D'(X)\), we shall construct a seminorm \(q\) on \(\mathcal D(X)\) and a locally finite sequence \(\psi_r\in\mathcal D(X)\) such that

\[
|(f,v)|+\|v\|_\infty
\leq C\left(q(P^*v)+\sum_r|(v,\psi_r)|\right),
\qquad v\in\mathcal D(X).
\tag{GS10}
\]

On each fixed compact test support, \(q\) will be a finite sum of ordinary compact smooth seminorms. Thus its bound really defines a distribution. The half-density sup norm uses any fixed positive smooth fiber norm; norms on the fixed compact sets are equivalent.

### 4.1. A complete space converts singular-support information to estimates

For \(j\geq0\), let \(V_j\) consist of continuous half-densities supported in \(K_{j+1}'\) such that \(P^*v\) is smooth on \(X\setminus K_{j-1}\). Give it the topology of the global sup norm of \(v\) and all compact smooth seminorms of that forcing on \(X\setminus K_{j-1}\).

This is a Fréchet space. The sup-norm component is complete on the closed fixed-support space of continuous sections. A Cauchy sequence of forcing components has a smooth limit on the indicated open set, by the complete chart proof of the programme smooth-space theorem. Uniform convergence of the compact inputs implies distributional convergence of \(P^*v\): pair against a compact test, use the smooth proper image under \(P\), and bound the integral by the sup norm. Thus the two limits satisfy the same distributional equation. Countable compact chart exhaustions give the complete metrizable topology.

By (GS9), restriction is an everywhere defined map

\[
V_j\longrightarrow C^\infty(X\setminus K_{j-1}'),\qquad
v\longmapsto v|_{X\setminus K_{j-1}'}.
\tag{GS11}
\]

Its graph is closed: convergence in its source implies distributional convergence to the same section as smooth convergence in its target. The complete programme Fréchet closed-graph proof therefore makes this restriction continuous.

One consequence will be used explicitly. If \(\|v_N\|_\infty\) is bounded and \(P^*v_N\to0\) smoothly on \(X\setminus K_{j-1}\), then every compact derivative seminorm of \(v_N\) outside \(K_{j-1}'\) is bounded. Such a sequence is precompact in the local smooth topology there. To see this without another compactness theorem, use a finite chart cover on each exhaustion compact. The next derivative bound gives uniform equicontinuity of each derivative. Select convergent values on a countable dense grid by successive subsequences; equicontinuity gives uniform convergence on each compact. A diagonal choice treats every derivative and every exhaustion compact. The coordinate fundamental theorem of calculus identifies the compatible derivative limits as the derivatives of one smooth section.

### 4.2. Extend one estimate across one more compact set

Inductively suppose that

\[
|(f,v)|+\|v\|_\infty\leq C_j Q_j(v),
\qquad
Q_j(v)=q_j(P^*v)+\sum_{r\in R_j}|(v,\psi_r)|,
\qquad
v\in\mathcal D(K_j'),
\tag{GS12}
\]

where \(R_j\) is finite and \(q_j\) is a finite sum of compact smooth seminorms. At \(j=0\), the only input is zero, so take \(C_0=1,q_0=0,R_0=\varnothing\).

Fix \(\varepsilon_j>0\). Choose increasing seminorms \(t_N\) exhausting the smooth topology on \(X\setminus K_{j-1}\), each a finite sum of compact derivative sup norms there. They vanish on functions supported in \(K_{j-1}\).

Also choose a countable family \(\chi_s\in\mathcal D(X\setminus K_{j-1}')\) detecting every continuous section on that open set. An explicit choice uses a countable chart atlas, dense countable centers and positive compact bump averages of radii tending to zero at every center, with the local half-density frame. If all these pairings vanish, the average limit gives zero at the dense centers, and continuity gives zero everywhere. Every \(\chi_s\) is supported outside \(K_{j-1}\), because \(K_{j-1}\subset K_{j-1}'\).

We claim that for some finite \(N\), the next estimate holds on \(\mathcal D(K_{j+1}')\), with constant \(C_{j+1}=C_j(1+\varepsilon_j)\), after replacing \(q_j\) by \(q_j+Nt_N\) and adjoining the finite tests \(N\chi_s\), \(s\leq N\).

If not, normalize the counterexample for each \(N\) to obtain

\[
|(f,v_N)|+\|v_N\|_\infty=C_j(1+\varepsilon_j),\qquad
Q_j(v_N)+Nt_N(P^*v_N)
+N\sum_{s\leq N}|(v_N,\chi_s)|<1.
\tag{GS13}
\]

These inputs are bounded in sup norm, their forcing tends to zero smoothly outside \(K_{j-1}\), and every detector pairing tends to zero. The conclusion of Section 4.1 gives precompactness outside \(K_{j-1}'\). Every smooth subsequential limit vanishes, because all detector pairings vanish. Hence the full sequence tends to zero in that smooth topology: otherwise a subsequence violating one seminorm convergence would have a convergent further subsequence with zero limit.

Choose \(\chi\in\mathcal D(\operatorname{int}K_j')\), equal to one near \(K_{j-1}'\). Then

\[
(1-\chi)v_N\longrightarrow0
\quad\text{in the smooth test topology with one fixed compact support.}
\tag{GS14}
\]

Indeed its derivatives are confined to a fixed compact set outside \(K_{j-1}'\). Properness makes \(P^*((1-\chi)v_N)\) have a common compact support, and the all-order smooth continuity of \(P^*\) gives convergence to zero in that same test topology. The distribution \(f\), the finite seminorm \(q_j\), and the finitely many previous test pairings all tend to zero on these remainders. Therefore

\[
|(f,\chi v_N)|+\|\chi v_N\|_\infty
=C_j(1+\varepsilon_j)+o(1),\qquad
Q_j(\chi v_N)<1+o(1).
\tag{GS15}
\]

But \(\chi v_N\in\mathcal D(K_j')\), so (GS12) contradicts (GS15) for large \(N\). This proves the claimed finite extension.

### 4.3. The final estimate is continuous on every fixed test support

Choose positive \(\varepsilon_j\) with finite sum. Then

\[
C_j=\prod_{i<j}(1+\varepsilon_i)
\leq \exp\!\left(\sum_i\varepsilon_i\right)=C<\infty.
\tag{GS16}
\]

At each step the added seminorm vanishes on inputs supported in \(K_{j-1}\), and the new test functions are supported outside \(K_{j-1}\). Consequently a fixed compact test support meets only finitely many of the new tests, and only finitely many seminorm increments act on it. The pointwise increasing limit \(q=\lim q_j\) is finite on every test input, is a seminorm, and on each fixed support is a finite sum of finite-order compact derivative bounds. The sequence of all appended tests is locally finite. Passing the finite-stage bound to any test supported in a sufficiently late \(K_j'\) gives (GS10).

Define the linear map

\[
Tv=\left(P^*v,\ ((v,\psi_r))_r\right)
\in\mathcal D(X)\oplus\ell^1,\qquad
Q(w,z)=q(w)+\|z\|_{\ell^1}.
\tag{GS17}
\]

The sequence component of each test input is actually finite. Formula (GS10) makes \(Tv\mapsto(f,v)\) a well-defined conjugate-linear functional on its image, bounded by \(C Q\). Apply the complete programme complex seminorm Hahn–Banach proof, to the conjugate functional if necessary, to extend it to the entire direct sum with the same bound.

Its restriction to \(\mathcal D(X)\) is \((u,w)\) for a distribution \(u\): on any fixed compact test support, the bound by \(Cq(w)\) is a finite-order derivative bound, exactly the distribution continuity condition. On \(\ell^1\), the restriction has the form \(\sum_r a_r\overline{z_r}\), with \(|a_r|\leq C\). To check this representation, evaluate the functional on each unit vector, use the bound to obtain \(|a_r|\leq C\), and pass from finite sequences to their \(\ell^1\) limits by continuity. Thus

\[
(f,v)=(u,P^*v)+\sum_r a_r(\psi_r,v),\qquad
f-Pu=\sum_r a_r\psi_r\in C^\infty(X).
\tag{GS18}
\]

The last sum is locally finite, so every derivative is locally a finite sum. This constructs one global \(u\), proving (A). All three implications are now proved, and Theorem 1.1 is complete.

This extension does not select \(u\) linearly from \(f\) or supply a continuous global right inverse. A finite smooth adjoint kernel is compatible with (A), because the allowed smooth error can carry that obstruction.

## 5. Exercises with complete solutions

**1. An empty characteristic set.** Verify the three conditions for \(P=I\), of order zero, on any \(X\) under consideration. Explain why the exact solution is more regular than the generic local gain predicts.

**Solution.** The principal symbol is one, so there are no characteristic strips and (C) is vacuous. Since \(P^*v=v\), (B) holds with \(K'=K\). For (A), set \(u=f\), with zero smooth error. If the data are \(H^s_{\mathrm{loc}}\), this exact solution has the same regularity, whereas the general compact-set theorem for \(m=0\) guarantees only \(H^{s-1}_{\mathrm{loc}}\). The inclusion \(H^s_{\mathrm{loc}}\subset H^{s-1}_{\mathrm{loc}}\) is consistent with that theorem; its characteristic estimate need not be optimal for an elliptic operator.

**2. A missing boundary point is infinity in the theorem.** Let

\[
\begin{gathered}
X=\mathbb R^2\setminus\{(0,y):y\geq0\},\qquad P=D_x,\\
K=\{(-1,y):-1\leq y\leq0\}
\cup\{(1,y):-1\leq y\leq0\}.
\end{gathered}
\tag{GS19}
\]

Show that \(P\) is of global real principal type but (C) fails. Identify a sequence of escaping interior points and the resulting solvability conclusion.

![Base projections of the horizontal characteristic excursions and their midpoints](figures/global-solvability-slit-domain.svg)

*The green set is exactly the two compact endpoint segments \(K\). The blue intervals sample \(y=-1/j\) at \(j=1,2,4\), with arrows for \(H_p=\partial_x\). Every strip carries \(+dy\); the drawing shows its base projection. The marked midpoints approach the removed origin. This exercise and (GS19) prove the stated escape from every compact subset of \(X\).*

**Solution.** The symbol is \(\xi_x\); its nonzero characteristic covectors have \(\xi_x=0\), and its Hamilton field is \(\partial_x\). At height \(y<0\), a maximal horizontal characteristic has all \(x\in\mathbb R\). At height \(y\geq0\), it has either \(x<0\) or \(x>0\). Each complete strip has an unbounded base direction, so none stays over a compact subset of \(X\). The two vertical pieces of \(K\) are compact and avoid the removed ray.

For each \(j\geq1\), the horizontal interval from \((-1,-1/j)\) to \((1,-1/j)\), with positive covector \(dy\), is a characteristic interval in \(X\), with both endpoints over \(K\). Its midpoint \(x_j=(0,-1/j)\) has distance \(1/j\) from the removed closed ray. A compact subset \(K'\subset X\) has positive distance from that ray, by compactness and disjointness. Thus it omits \(x_j\) for all sufficiently large \(j\). No \(K'\) satisfies (C).

Here \(x_j\to(0,0)\) in the ambient plane, but the limit point is not in \(X\); the points escape every compact subset of \(X\). Theorem 1.1 gives a distribution \(f\) for which no global distribution \(u\) has \(D_xu-f\) smooth. Section 3 constructs such an \(f\) from locally finite midpoint forcing pieces of finite singular rays whose thresholds tend to minus infinity. Global real principal type alone does not give global solvability modulo smooth functions.

**3. Which topology controls the extension?** On \(\mathbb R\), define \(q(w)=\sum_{j\geq1}|w(j)|\) for \(w\in\mathcal D(\mathbb R)\). Prove that it is continuous on every fixed compact test support but is not continuous in the topology of \(C^\infty(\mathbb R)\). Also explain why bounded coefficients in a locally finite sum of smooth tests produce a smooth residual.

**Solution.** A fixed compact set contains only finitely many positive integers. On functions supported there, \(q\) is a finite sum of point evaluations and is bounded by that finite number times the sup norm. This is a finite-order distribution seminorm on the fixed test support. Choose \(\eta\in C^\infty_c((-1/4,1/4))\) with \(\eta(0)=1\), and put \(w_j(t)=\eta(t-j)\). Every compact derivative seminorm of \(w_j\) is eventually zero, so \(w_j\to0\) in \(C^\infty(\mathbb R)\), but \(q(w_j)=1\). Thus the extension estimate is allowed to be continuous on the compact test spaces without being a global smooth-space seminorm.

If \(\{\psi_r\}\) is locally finite and \(\sup|a_r|<\infty\), then on any relatively compact neighborhood only finitely many supports occur. The sum \(\sum_r a_r\psi_r\) and each of its derivatives there are finite sums, hence smooth. Boundedness of the coefficients is supplied by the \(\ell^1\) extension, but local finiteness alone already ensures local smoothness for any fixed finite coefficients. Replacing local finiteness by pointwise finiteness would not justify differentiating the sum or claiming a smooth residual.

## References and current scope

Hörmander IV, §26.1, Theorem 26.1.9 supplies the three equivalences and the characteristic argument. Hörmander II, Theorem 10.7.8 and Lemma 10.7.9 supply the antecedent of the test-space estimate. That argument is developed here for the stated properly supported ordinary pseudodifferential operator, using the written programme closed-graph and seminorm extension proofs. The exposition, diagram and exercises are independently written; no error in the sources or new theorem is claimed.

The exact AN-03 providers retain their declared GFDL-1.2-only terms, with no invariant sections or cover texts. Their proofs are referenced at the sections stated above; their prose and assets are not reproduced here. Original expression and the original mathematical drawing in this lesson are eligible for the course's CC0 dedication.

This theorem gives global solvability modulo a smooth function. Exact global solvability, propagation parametrices, systems and boundary problems require separate arguments. Those subjects and the other assigned course mathematics remain unfinished.

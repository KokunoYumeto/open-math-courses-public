# Spectral tails, singular values and trace order

**Self-checked by the writing AI.**

A spectral tail counts how much trace lies above a height. A singular value asks how low the operator norm can be made by discarding a prescribed amount of trace. These descriptions are exact inverses, including at spectral atoms. We use that fact to integrate positive operators, transport scalar functions and compare operators whose spectral projections need not commute.

Let \(M\subseteq B(H)\) have a faithful normal semifinite trace \(\tau\), and write \(S(M,\tau)\) for the closed measurable operators constructed in MT08–12. Neither the algebra nor its representation is assumed sigma-finite or separable. All trace integrals may be infinite. We preserve the exact cutoff argument already proved in TI02, make its endpoint and domain reasoning explicit, and extend it to the scalar functional calculus and order comparisons.

This treats all four parts of Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercise 7, p. 184. The formula for a continuous increasing function with a positive value at zero requires a finite-total-trace correction, proved and illustrated in SV03. Here “increasing” permits nondecreasing functions and plateaus.

## The exact cutoff height

For \(T\in S(M,\tau)\), let \(h=|T|\). For \(a\geq0\), define

\[
 \begin{gathered} \lambda_a(T)\\
 =\tau(1_{(a,\infty)}(h)). \end{gathered}
 \tag{SV.1}
\]

For \(t>0\), let \(\mu_t(T)\) be the infimum of \(\|Te\|\) over projections \(e\in M\) satisfying

\[
 \begin{gathered}
 eH\subseteq D(T),\\
 \tau(1-e)\leq t.
 \end{gathered}
 \tag{SV.2}
\]

The composition \(Te:H\to H\) is literally bounded by CG03. The admissible set is nonempty and has finite norm values by the spectral-tail characterization MT11. Thus \(\mu_t(T)\) is a finite nonnegative number.

**Cutoff theorem.** Put \(m=\mu_t(T)\), and let \(F_t\) be the set of all real \(a\geq0\) with \(\lambda_a(T)\leq t\). Then

\[
 \begin{gathered} m=\inf F_t,\\
 \lambda_m(T)\leq t. \end{gathered}
 \tag{SV.3}
\]

The projection \(e_m=1_{[0,m]}(h)\) attains the infimum. Equivalently, for every \(a\geq0\),

\[
 \begin{gathered} \mu_t(T)\leq a\\
 \Longleftrightarrow\\
 \lambda_a(T)\leq t. \end{gathered}
 \tag{SV.4}
\]

**Proof.** The function \(a\mapsto\lambda_a(T)\) is decreasing and right-continuous in the extended sense. Indeed, if \(a_j\downarrow a\), the spectral projections for \((a_j,\infty)\) increase to the projection for \((a,\infty)\), by SK04–05. Normality gives \(\lambda_{a_j}(T)\uparrow\lambda_a(T)\), also when the limit is infinite.

If \(e\) is admissible and \(b=\|Te\|\), put \(q=1_{(b,\infty)}(h)\). A nonzero \(\xi\in eH\cap qH\) belongs to \(D(T)\). Its scalar spectral measure is supported strictly above \(b\), so

\[
 \begin{gathered} \|T\xi\|^2\\
 >b^2\|\xi\|^2. \end{gathered}
 \tag{SV.5}
\]

This contradicts the cutoff norm bound. The strict inequality follows by integrating the strictly positive function \(s^2-b^2\) against the nonzero finite vector spectral measure; the integral is finite since \(\xi\in D(T)\). This uses \(\|T\xi\|^2\), not an expression \(\langle T^*T\xi,\xi\rangle\) requiring the additional domain \(D(T^*T)\).

Thus \(e\wedge q=0\). The projection comparison MT02 implies \(q\precsim1-e\) and hence \(\lambda_b(T)\leq t\). Conversely, whenever \(\lambda_a(T)\leq t\), the spectral projection \(e_a=1_{[0,a]}(h)\) is admissible and \(\|Te_a\|\leq a\). The polar spectral calculus includes both the range inclusion in \(D(T)\) and that norm estimate. These two directions prove equality of the infima in (SV.3).

The scalar set defining that infimum is a nonempty upper set. Therefore \(\lambda_{m+1/j}(T)\leq t\) for each positive integer \(j\). Right continuity gives \(\lambda_m(T)\leq t\). Its spectral cutoff has norm at most \(m\); by definition of the infimum it has norm exactly \(m\). This proves attainment and (SV.4). It also proves the source's strict approximate-cutoff argument: if \(\|Te\|<b\), the projection for \((b,\infty)\) has zero intersection with \(e\) and trace at most its defect. \(\square\)

The argument remains valid at \(m=0\) and at atoms of the spectral measure. It does not require a minimizing sequence of projections to converge.

## Integrating heights or discarded trace

For a positive measurable \(T\),

\[
 \begin{gathered} \tau(T)\\
 =\int_0^\infty\lambda_a(T)\,da\\
 =\int_0^\infty\mu_t(T)\,dt. \end{gathered}
 \tag{SV.6}
\]

These are equalities in \([0,\infty]\), not assertions that either integral is finite.

**Proof.** Normality makes \(\nu(B)=\tau(E_T(B))\) a countably additive measure on the Borel subsets of \(0,\infty)\). For disjoint sets, spectral projections of the finite unions increase to the projection of their union, so finite additivity followed by normality proves this assertion. The positive spectral trace formula [MT13 gives \(\tau(T)=\int s\,d\nu(s)\).

For any measure \(\nu\) and nonnegative measurable \(g\), the layer formula is

\[
 \begin{gathered} \int g\,d\nu\\
 =\int_0^\infty\nu\{g>a\}\,da. \end{gathered}
 \tag{SV.7}
\]

Here is its proof without a sigma-finiteness hypothesis. If \(g\) is a nonnegative simple function with finitely many disjoint level sets, integrate the indicators of the intervals below its finitely many positive values. Finite addition gives exactly the sum defining its integral, including infinite terms. For general \(g\), choose increasing such simple functions \(g_j\uparrow g\). For every \(a\geq0\), the sets \(\{g_j>a\}\) increase to \(\{g>a\}\). Monotone convergence for \(\nu\), and then for Lebesgue measure in \(a\), proves (SV.7). All scalar integration and simple approximation facts used here are proved in the scalar integration programme, Sections 0–2.

Apply (SV.7) to \(g(s)=s\) and the spectral measure \(\nu\). This gives the first equality in (SV.6). For the second, (SV.4) says, for each \(a\geq0\),

\[
 \begin{gathered} \mu_t(T)>a\\
 \Longleftrightarrow\\
 t<\lambda_a(T). \end{gathered}
 \tag{SV.8}
\]

Thus the superlevel set is exactly \((0,\lambda_a(T))\). This interval has Lebesgue measure \(\lambda_a(T)\), allowing infinity. The decreasing function \(t\mapsto\mu_t(T)\) is measurable; this also follows from its explicitly described superlevel sets. Apply (SV.7) to that function on \((0,\infty)\). Its integral is the first integral in (SV.6), as required. Infinite spectral mass at zero contributes zero, so no finite-total-trace condition has entered. \(\square\)

This is the \(p=1\) case of the complete positive-power identity in TI02. We retain that earlier proof and its norm, adjoint and cutoff estimates.

## Scalar functional calculus and the finite-trace endpoint

Let \(T\geq0\) be measurable, and let \(f:[0,\infty)\to[0,\infty)\) be finite-valued, continuous and nondecreasing. Put \(L=\tau(1)\), allowing \(L=\infty\). Then \(f(T)\) is a positive measurable operator. For \(0<t<L\),

\[
 \begin{gathered} \mu_t(f(T))\\
 =f(\mu_t(T)). \end{gathered}
 \tag{SV.9}
\]

If \(L<\infty\), the remaining values are

\[
 \begin{gathered} \mu_t(f(T))=0\\
 (t\geq L,\ t>0). \end{gathered}
 \tag{SV.10}
\]

Consequently (SV.9) holds for **all** \(t>0\) if either \(f(0)=0\) or \(L=\infty\). These statements include functions with flat portions.

**Measurability.** The spectral calculus constructs \(f(T)\) as a positive closed affiliated operator with its maximal spectral-integral domain. On \(e_R=1_{[0,R]}(T)\), its range is in that domain and \(\|f(T)e_R\|\leq f(R)\). Since \(\tau(1-e_R)\to0\), MT11 proves measurability. This avoids any unjustified claim that unbounded continuous functions preserve measurable operators automatically.

**Upper bound.** Fix \(t>0\), and write \(m=\mu_t(T)\). The attained cutoff \(e_m\) from SV01 has defect at most \(t\) and
\(\|f(T)e_m\|\leq f(m)\). Thus \(\mu_t(f(T))\leq f(m)\).

**Lower bound before the endpoint.** Suppose \(t<L\). If \(m>0\) and \(0\leq c<f(m)\), continuity from the left supplies \(b\) with \(0\leq b<m\) and \(f(b)>c\). By (SV.4), \(\lambda_b(T)>t\). Monotonicity of \(f\) and the spectral composition rule give the projection inclusion

\[
 \begin{gathered} E_T((b,\infty))\\
 \leq E_{f(T)}((c,\infty)). \end{gathered}
 \tag{SV.11}
\]

Hence \(\lambda_c(f(T))>t\), and another use of (SV.4) gives \(\mu_t(f(T))>c\). Letting \(c\uparrow f(m)\) proves the lower bound. If \(f(m)=0\), it is immediate from nonnegativity.

If \(m=0\), then \(f(T)\geq f(0)1\) by the scalar spectral calculus. For \(0\leq c<f(0)\), its spectral projection above \(c\) is the identity and has trace \(L>t\). Again (SV.4) gives \(\mu_t(f(T))>c\). Let \(c\uparrow f(0)\); when \(f(0)=0\), nonnegativity suffices. This proves (SV.9) in every case.

**At and beyond finite total trace.** When \(t\geq L\), the zero projection is an admissible cutoff for every measurable operator. Its product norm is zero, proving (SV.10) and also \(\mu_t(T)=0\). If \(f(0)=0\), both sides of (SV.9) are then zero. Otherwise they need not agree.

For an explicit counterexample to the unrestricted formula printed in Exercise 7(d), take \(M=\mathbb C\) on \(\mathbb C\), the trace \(\tau(a)=a\) for \(a\geq0\), \(T=0\), and \(f(s)=1+s\). This is a faithful normal finite trace: the positive scalar order makes every defining property immediate, and its entire algebra is the finite trace ideal. For \(t\geq1\),

\[
 \begin{gathered} \mu_t(f(T))\\
 =\mu_t(1)=0,\\
 f(\mu_t(T))\\
 =f(0)=1. \end{gathered}
 \tag{SV.12}
\]

All the printed hypotheses hold. The finite-total-trace range cannot be omitted.

Combining SV02 with (SV.9)–(SV.10) yields the full corrected trace formula

\[
 \begin{gathered} \tau(f(T))\\
 =\int_0^L f(\mu_t(T))\,dt. \end{gathered}
 \tag{SV.13}
\]

If \(L=0\), faithfulness makes the algebra zero, and the integral over the empty interval is zero. If \(L=\infty\), the interval is \((0,\infty)\). Endpoints of finite intervals have Lebesgue measure zero. All quantities are nonnegative, so this identity never subtracts infinities. In particular, \(f(s)=s^p\), \(p>0\), gives the global singular-value identity for positive powers, consistently with TI02.

## Order comparison without commuting spectral projections

Let \(T,S\) be positive measurable operators and suppose \(0\leq T\leq S\) in the ordered measurable algebra of MT12. This means that the closed difference \(C=\overline{S-T}\) is positive. Then for every \(a\geq0\) and \(t>0\),

\[
 \begin{gathered}
 \lambda_a(T)\leq\lambda_a(S),\\
 \mu_t(T)\leq\mu_t(S).
 \end{gathered}
 \tag{SV.14}
\]

For every \(f\) as in SV03, it follows that

\[
 \begin{gathered} \tau(f(T))\\
 \leq\tau(f(S)). \end{gathered}
 \tag{SV.15}
\]

No commutation between \(T\) and \(S\) is required.

**Proof of the spectral comparison.** Put
\(q=1_{(a,\infty)}(T)\), \(e=1_{[0,a]}(S)\), and \(r=q\wedge e\). We prove \(r=0\) while respecting the unbounded domains.

For any \(d>0\), choose a projection \(p\) with \(\tau(1-p)<d\) and
\(pH\subseteq D(T)\cap D(S)\). Such projections exist by MT11 and the countable intersection theorem MM05. On this intersection, the closed difference \(C\) agrees with the ordinary difference by MT09. Positivity therefore gives

\[
 \begin{gathered} \langle T\xi,\xi\rangle\\
 \leq\langle S\xi,\xi\rangle\\
 (\xi\in pH). \end{gathered}
 \tag{SV.16}
\]

If a nonzero \(\xi\) belonged to \((r\wedge p)H\), its membership in \(qH\cap D(T)\) and the positive spectral calculus would imply
\(\langle T\xi,\xi\rangle>a\|\xi\|^2\). Its membership in \(eH\) gives
\(\langle S\xi,\xi\rangle\leq a\|\xi\|^2\). This contradicts (SV.16). Thus \(r\wedge p=0\), and MT02 implies

\[
 \begin{gathered} \tau(r)\leq\tau(1-p)\\
 <d. \end{gathered}
 \tag{SV.17}
\]

Since \(r\) is fixed and \(d>0\) arbitrary, faithfulness gives \(r=0\). Apply MT02 once more to \(q\wedge e=0\). It gives \(q\precsim1-e\), and hence
\(\lambda_a(T)\leq\lambda_a(S)\). Notice that the intersection with \(p\) supplied the actual domains; a vector in \(qH\) alone need not lie in \(D(T)\).

The singular-value comparison now follows from (SV.3): every height admissible for \(S\) is admissible for \(T\). Finally, scalar monotonicity gives
\(f(\mu_t(T))\leq f(\mu_t(S))\). Integrate on \((0,L)\), using (SV.13) for the same ambient total trace \(L=\tau(1)\), to obtain (SV.15), including infinite values. Scalar monotonicity is sufficient for this trace comparison; no operator-monotonicity assertion about \(f\) is used. \(\square\)

## Source clauses and boundary checks

Parts (a)–(c) of Exercise 7 are proved by SV01: right continuity, the attained spectral cutoff, zero intersection for an approximate cutoff, and the resulting projection trace bound. The proof retains the strict spectral tail \((a,\infty)\), the non-strict allowed trace defect, and the case \(a=0\). It also replaces the hint's potentially undefined \(T^*T\)-pairing by the exact squared norm on \(D(T)\).

All four assertions in part (d) are addressed: SV02 proves the integral of singular values; SV03 proves the functional-calculus rule with its necessary finite-total-trace correction and a counterexample to the unqualified formula; SV04 proves both singular-value monotonicity and the trace comparison for every continuous nondecreasing nonnegative \(f\). The proofs preserve the arbitrary semifinite algebra and do not introduce a countable finite-trace exhaustion or a hidden assumption \(f(0)=0\).

As a direct atom check, for a projection \(p\) of finite trace \(d\), the definition gives \(\lambda_a(p)=d\) when \(0\leq a<1\), and zero when \(a\geq1\). Equation (SV.4) then gives

\[
 \begin{gathered} \mu_t(p)\\
 =\begin{cases}1,&0<t<d,\\0,&t\geq d.\end{cases} \end{gathered}
 \tag{SV.18}
\]

The value at \(t=d\) is zero because the defect inequality permits discarding the entire support. Its integral is \(d=\tau(p)\), which checks the spectral and trace endpoints simultaneously. When \(d=0\), faithfulness makes \(p=0\), and the zero branch applies for every \(t>0\).

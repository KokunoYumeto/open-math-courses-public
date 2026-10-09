# Banach holomorphy, generators, and resolvent limits

**Course draft with exact existing programme theorem imports, local domain and endpoint arguments, and solved exercises.**

Analytic continuation in modular theory moves between Banach-valued functions, unitary groups and unbounded generators. This lesson states the exact domains and convergence hypotheses used by the modular arguments. The existing programme proofs supply norming-dual holomorphy, Stone's theorem, invariant and analytic cores, resolvent convergence and logarithmic transport. Their original proof ownership is retained; the local derivative calculation, closure wrapper, bounded-transform check and solved examples remain.

The two programme sources are Analytic elements and strip arguments and Holomorphy in Banach spaces, Stone's theorem and resolvent convergence, written by Claude Opus 5.5 (Anthropic), September 2026, under CC0. The exact selected clauses are identified below. The proofs in those two lessons rely on complex-analysis, integration, spectral-calculus and analytic-generator results that are not all proved in these courses.

The human-source antecedent is Takesaki, *Theory of Operator Algebras II*, Appendix A.1–A.6. Its printed A.6(ii) omits a necessary condition: on a nonzero Hilbert space, \(A_n=nI\) has both half-plane resolvents tending to zero, while zero is not a self-adjoint resolvent. This correction is proved in the programme's Theorem 8.2(5), with Lemma 8.1 and Example 8.3. SG-08 imports that result and preserves the counterexample.

## Conventions and inputs

Banach spaces and Hilbert spaces are complex. Hilbert inner products are
linear in the first variable, and Hilbert spaces may have arbitrary dimension.
For a densely defined operator \(T\), \(D(T)\) is its actual domain. A graph
core is dense in \(D(T)\) for

\[
 \|x\|_T^2=\|x\|^2+\|Tx\|^2.
\tag{SG.1}
\]

The exact inputs are scalar Cauchy formulas and power series; the
Banach-valued Riemann and improper integrals constructed
in MA-02; and the self-adjoint spectral calculus of SK-05–SK-09. In particular,
SK-09 supplies bounded continuous functional-calculus convergence once both
nonreal resolvents converge strongly. The written Baire and uniform-boundedness
argument in Baire category and uniform boundedness supplies the norming-dual
boundedness input; the exact programme theorem proofs named below retain their
other analytic-generator and spectral entry contracts.

For self-adjoint \(A_n,A\), **strong resolvent convergence** means

\[
 (A_n-z)^{-1}x\longrightarrow(A-z)^{-1}x
 \quad(x\in H, z\in\mathbb C\setminus\mathbb R).
\tag{SG.2}
\]

No assertion below replaces this vectorwise condition by operator-norm
convergence.

## Norming scalar tests detect Banach holomorphy

Let \(E\) be a Banach space, \(\Omega\subseteq\mathbb C\) open and \(f:\Omega\to E\). A subspace \(N\subseteq E^*\) is norming when

\[
 \|x\|=\sup\{|x'(x)|:x'\in N,\ \|x'\|\leq1\}\qquad(x\in E).
 \tag{SG.3}
\]

Read **Lemma 2.1(1)–(2)** of Analytic elements and strip arguments. It gives the following equivalent descriptions:

1. Near every point, \(f\) has a norm-convergent power series in \(E\).
2. Every \(x'\circ f\) is holomorphic for a norm-closed norming subspace \(N\subseteq E^*\).
3. The function is locally norm bounded and every \(x'\circ f\) is holomorphic for a norming subspace \(N\), which need not be closed.

The complete proof, including uniform boundedness on the closed norming space, belongs to that programme lemma. It first uses the closed-range isometry

\[
 J:E\longrightarrow N^*,\qquad (Jx)(x')=x'(x),
 \tag{SG.4}
\]

obtains \(M=\sup_{|z-z_0|\le R}\|f(z)\|<\infty\), and forms the scalar Cauchy coefficients in \(N^*\). Only after proving norm continuity does it recover those coefficients by norm integrals in \(E\). In condition 3, local boundedness first extends the scalar tests to \(\overline N\); it is not silently deduced from an incomplete norming space. SG-03 applies precisely the resulting norm power series.

## Norm derivatives and vector Cauchy coefficients

Under any condition of SG-02, \(f\) is norm holomorphic. If

\[
 f(z)=\sum_{k\geq0}a_k(z-z_0)^k
\]

on a disc, then termwise norm differentiation on every smaller disc gives

\[
 f^{(m)}(z_0)=m!a_m,
\qquad
 a_m=\frac{1}{2\pi i}
 \int_{|\zeta-z_0|=\rho}
 \frac{f(\zeta)}{(\zeta-z_0)^{m+1}}\,d\zeta
\tag{SG.7}
\]

for \(0<\rho<R\). The last integral is an \(E\)-valued norm integral. Indeed,
SG-02 has already proved norm continuity on the circle; applying each
\(x'\in E^*\) to its Riemann sums recovers the scalar Cauchy coefficient, and
bounded functionals separate vectors. Thus weak holomorphy has not been used
to assume the norm continuity that it is meant to prove.

## Stone's theorem with the derivative domain

Read **Theorem 8.1(3)** of Analytic elements and strip arguments. For a strongly continuous unitary group \(U\) on an arbitrary Hilbert space, it constructs the unique positive injective self-adjoint operator \(B=U_{-i}\) with \(U_t=B^{it}\). Its self-adjoint logarithm \(A=\log B\) therefore satisfies

\[
 U_t=e^{itA}\qquad(t\in\mathbb R),
 \tag{SG.8}
\]

with the exact domain and action

\[
 \begin{aligned}
 D(A)&=\left\{x:\lim_{h\to0}\frac{U_hx-x}{h}\text{ exists in }H\right\},\\
 iAx&=\lim_{h\to0}\frac{U_hx-x}{h}.
 \end{aligned}
 \tag{SG.9}
\]

Conversely, the spectral group of a self-adjoint \(A\) is strongly continuous and has this derivative domain. The derivative determines the operator, including its domain, so the self-adjoint generator is unique. The complete Stone and converse-domain proof remains with the programme theorem; its analytic-generator construction and preceding spectral/strip inputs are retained. Positivity and injectivity of \(B\) do not say that \(B\) is bounded or bounded below.

## A dense invariant generator domain is a core

Let \(A\) be self-adjoint and \(U_t=e^{itA}\). **Theorem 8.1(4)** of Analytic elements and strip arguments states: if a linear subspace \(D\subseteq D(A)\) is dense in \(H\) and \(U_tD\subseteq D\) for every real \(t\), then \(D\) is a graph core for \(A\).

The full proof belongs to that theorem. It first closes the restricted graph and uses Gaussian averages inside that closed graph; the proposed core itself need not be complete. Invariance is required on \(D\), and Hilbert-norm density alone does not imply graph density. The core conclusion includes convergence of both \(x\) and \(Ax\) in the norm (SG.1).

## Dense analytic vectors force essential self-adjointness

Let \(S\) be a densely defined symmetric operator. A vector \(x\) is
**analytic for \(S\)** if \(x\in\bigcap_{k\geq0}D(S^k)\) and, for some
\(r>0\),

\[
 \sum_{k=0}^\infty\frac{r^k}{k!}\|S^kx\|<\infty.
\tag{SG.15}
\]

If the analytic vectors form a dense subspace \(D_{\mathrm{an}}\), then
\(S|_{D_{\mathrm{an}}}\) is essentially self-adjoint.

**Proof.** Put \(D_0=D_{\mathrm{an}}\), with analyticity still defined for
the original operator \(S\). This subspace is invariant under \(S\).
Indeed, if (SG.15) holds at \(r\), then for \(0<r'<r\) the series for
\(Sx\) is bounded by the original series times the bounded factors
\((k+1)(r'/r)^k/r\). Thus \(Sx\in D_0\).

The densely defined symmetric restriction \(S|_{D_0}\) is closable. Set

\[
 T=\overline{S|_{D_0}}.
\]

For \(x\in D_0\), invariance gives \(T^kx=S^kx\) for every \(k\).
Consequently the analytic vectors \(E_{\mathrm{an}}\) of the closed
symmetric operator \(T\) contain the dense subspace \(D_0\).

Apply **Theorem 8.1(5)** of Analytic elements and strip arguments to this closed, densely defined symmetric \(T\). It has a dense space of analytic vectors, so the programme theorem makes \(T\) self-adjoint. Its full closed-operator proof belongs to that theorem. By the definition of \(T=\overline{S|_{D_0}}\), the original restriction is essentially self-adjoint. Moreover \(T\subseteq\overline S\subseteq S^*\subseteq T^*=T\), so \(\overline S=T\). This last closure argument is the local extension from the programme's closed-operator hypothesis; it never applies that theorem directly to a nonclosed \(S\). \(\square\)

## Resolvents and unitary groups carry the same convergence

Read **Theorem 7.4**, with **Lemma 7.2(4)**, of Holomorphy in Banach spaces, Stone's theorem and resolvent convergence. Let \(A_j\) and the proposed limit \(A\) be self-adjoint, with \(j\) in a directed set. The theorem gives the equivalence of:

1. \((A_j-z)^{-1}\to(A-z)^{-1}\) strongly for every nonreal \(z\).
2. These resolvents converge weakly at one nonreal \(z_0\), to the resolvent of this given \(A\).
3. \(f(A_j)\to f(A)\) strongly for every bounded continuous \(f:\mathbb R\to\mathbb C\).
4. The unitary groups converge strongly, locally uniformly in time:

\[
 \sup_{|t|\leq T}\|(e^{itA_j}-e^{itA})x\|\longrightarrow0
 \quad(T<\infty,\ x\in H).
 \tag{SG.19}
\]

These conditions imply pointwise weak, and hence pointwise strong, convergence of the unitary groups. **For sequences**, that pointwise condition also implies all four conditions. The reverse implication from pointwise unitary convergence is not asserted for arbitrary nets. The programme's **Exercise 5 and full solution** constructs a real net \(h_\alpha\to+\infty\) with \(e^{ith_\alpha}\to1\) for each fixed \(t\), while \((h_\alpha-i)^{-1}\to0\ne(0-i)^{-1}\). Its finite simultaneous-approximation proof remains with that exercise. This distinction avoids using sequential dominated convergence for nets.

The full convergence proof belongs to Theorem 7.4. The given self-adjoint limit in condition 2 is essential; merely knowing that one or two resolvents have bounded-operator limits is the different problem in SG-08. Continuity of \(f\) in condition 3 is essential.

For the sign convention used here, **Lemma 7.1(4)** of the same programme lesson gives the exact specializations

\[
 \begin{aligned}
 (A_j-i)^{-1}x&=i\int_0^\infty e^{-t}e^{-itA_j}x\,dt,\\
 (A_j+i)^{-1}x&=-i\int_0^\infty e^{-t}e^{itA_j}x\,dt.
 \end{aligned}
 \tag{SG.20}
\]

Their convergence follows from the imported theorem under its indicated sequence or locally uniform hypotheses. Norm integrals and spectral domains keep the named MA/SK entry contracts.

## Corrected limits of two half-plane resolvents

Read **Lemma 8.1 and Theorem 8.2(1)–(5)** of Holomorphy in Banach spaces, Stone's theorem and resolvent convergence. For a net of self-adjoint \(A_j\), choose \(z_+\in\mathbb C_+\) and \(z_-\in\mathbb C_-\), and suppose

\[
 (A_j-z_+)^{-1}\longrightarrow R_+,
 \qquad (A_j-z_-)^{-1}\longrightarrow R_-
 \tag{SG.21}
\]

strongly. The programme theorem supplies strong limits \(R(z)\) at every nonreal parameter, satisfying

\[
 R(z)-R(w)=(z-w)R(z)R(w),\qquad R(z)^*=R(\bar z).
 \tag{SG.23}
\]

Their common kernel \(N\) has orthogonal complement

\[
 N^\perp=\overline{\operatorname{ran}R(z)}.
 \tag{SG.25}
\]

Writing \(P\) for the projection onto \(N^\perp\), the theorem constructs a unique self-adjoint \(A_0\) on the Hilbert space \(N^\perp\) such that

\[
 R(z)=(A_0-z)^{-1}P.
\]

For every \(f\in C_0(\mathbb R)\), it also gives \(f(A_j)\to f(A_0)P\) strongly. There is a densely defined self-adjoint strong resolvent limit on the **whole** \(H\) exactly when \(N=0\), equivalently when \(R_+\) is injective. In that case the limit is unique, its domain is \(\operatorname{ran}R(z_0)\), and Lemma 8.1 identifies its action by

\[
 A(R(z_0)x)=x+z_0R(z_0)x.
 \tag{SG.26}
\]

The complete propagation, adjoint, domain and necessity proofs belong to the programme lemma and theorem. The construction on \(N^\perp\) includes a zero effective Hilbert space and does not erase the escaped subspace \(N\).

**Solved source-error check.** On a nonzero \(H\), take \(A_n=nI\). For every nonreal \(z\), \((A_n-z)^{-1}=(n-z)^{-1}I\to0\) in norm. Both hypotheses hold but \(N=H\); the zero operator cannot be a resolvent on \(H\), because it is not injective and has no dense range. This is the defective Appendix A.6(ii) clause and the counterexample retained in SG-11. The correction and its complete general proof are the programme's Theorem 8.2(5), with Example 8.3.

## Convergence on one common core

Read **Theorem 7.6** of Holomorphy in Banach spaces, Stone's theorem and resolvent convergence. Let \(A_j\) and \(A\) be self-adjoint, and let \(D\) be a graph core for \(A\). If each \(x\in D\) belongs to \(D(A_j)\) eventually, with the threshold allowed to depend on \(x\), and

\[
 A_jx\longrightarrow Ax\qquad(x\in D),
 \tag{SG.28}
\]

then \(A_j\to A\) in the strong resolvent sense. The original common-core sequence statement is the special case \(D\subseteq D(A_n)\) for every \(n\).

The full proof belongs to that programme theorem. Its bounded-resolvent estimate is applied on the dense subspace \((A-i)D\) and then extends to \(H\). The proposed limit must already be self-adjoint, and \(D\) must be its graph core; an arbitrary Hilbert-dense subset is insufficient. No uniform eventual domain threshold over all of \(D\) is introduced.

## Positive limits, logarithms, and imaginary powers

Let \(A_n,A\) be positive injective self-adjoint operators, and suppose
\(A_n\to A\) in the strong resolvent sense. Then

\[
 \log A_n\longrightarrow\log A
\tag{SG.30}
\]

in the strong resolvent sense, and for every \(x\in H\) and \(T<\infty\),

\[
 \sup_{|t|\leq T}\|A_n^{it}x-A^{it}x\|\longrightarrow0.
\tag{SG.31}
\]

**Earlier programme proof.** Read **Theorem 9.1 and Corollary 9.2(1)** of Holomorphy in Banach spaces, Stone's theorem and resolvent convergence. They prove this conclusion for arbitrary nets of positive injective self-adjoint operators, with an injective proposed limit. The full transformation proof and time-uniform conclusion remain with that source. In particular no spectral gap at zero or bounded inverse is assumed.

**Solved bounded-transform check.** Let \(K_n=(I+A_n)^{-1}\) and \(K=(I+A)^{-1}\). Choose a bounded
continuous function on the real line which equals \(t\mapsto(1+t)^{-1}\)
for \(t\geq0\). Strong resolvent convergence and the bounded continuous
calculus give \(K_n\to K\) strongly. For \(z\notin\mathbb R\), define on
\([0,1]\)

\[
 h_z(s)=
 \begin{cases}
 \left(\log\dfrac{1-s}{s}-z\right)^{-1},&0<s<1,\\
 0,&s=0,1.
 \end{cases}
\tag{SG.32}
\]

This function is continuous: the real logarithm tends to opposite infinities
at the endpoints. Continuous functional calculus for the bounded positive
contractions gives \(h_z(K_n)\to h_z(K)\) strongly. Injectivity of
\(A_n,A\) removes spectral mass at \(s=1\), and the bounded injections
\(K_n,K\) have no spectral mass at \(s=0\). Hence

\[
 h_z(K_n)=(\log A_n-z)^{-1},
 \qquad
 h_z(K)=(\log A-z)^{-1}.
\]

These identities explain why the endpoint assignments do not require a bounded inverse. The general net convergence result and its locally uniform imaginary-power conclusion are imported from the programme Corollary 9.2(1); this endpoint check is a local application. \(\square\)

Injective does not mean boundedly invertible. Spectra may accumulate at zero;
the endpoint values in (SG.32) handle precisely that possibility.

## Checks and solved exercises

**Problem 1: the missing nondegeneracy.** On a nonzero Hilbert space take
\(A_n=nI\). Determine every nonreal resolvent limit and explain why there is
no self-adjoint strong resolvent limit.

**Solution.** For \(z\notin\mathbb R\),

\[
 (A_n-z)^{-1}=(n-z)^{-1}I\longrightarrow0
\]

in operator norm. The zero limit has full kernel and zero range. A resolvent
of a densely defined self-adjoint operator is injective with dense range, so
SG-08's nondegeneracy fails and no such limit operator exists.

**Problem 2: large eigenvalues can escape strongly.** On
\(\ell^2(\mathbb N)\), let \(P_n\) project onto the \(n\)-th basis vector and
put \(A_n=nP_n\). Prove \(A_n\to0\) in the strong resolvent sense and verify
the locally uniform unitary conclusion directly.

**Solution.** For nonreal \(z\),

\[
 (A_n-z)^{-1}
 =-z^{-1}(I-P_n)+(n-z)^{-1}P_n.
\]

Since \(P_nx\to0\) for each fixed \(x\in\ell^2\), these resolvents converge
strongly to \(-z^{-1}I=(0-z)^{-1}\). Also

\[
 e^{itA_n}=I+(e^{int}-1)P_n,
\qquad
 \sup_{t\in\mathbb R}\|(e^{itA_n}-I)x\|
 \leq2\|P_nx\|\longrightarrow0.
\]

The convergence is even uniform on the whole real line for each fixed vector,
although it is not operator-norm convergence.

**Problem 3: an explicit analytic core.** On \(\ell^2(\mathbb N)\), define
\(Se_k=k e_k\) on the finite-support vectors. Show that every such vector is
analytic and identify the self-adjoint closure.

**Solution.** If \(x\) is supported in \(\{1,\ldots,m\}\), then

\[
 \|S^jx\|\leq m^j\|x\|,
 \qquad
 \sum_{j\geq0}\frac{r^j}{j!}\|S^jx\|
 \leq e^{rm}\|x\|.
\]

Finite-support vectors are dense, so SG-06 gives essential self-adjointness.
The closure is the diagonal operator

\[
 D(\overline S)=\left\{x:\sum_{k\geq1}k^2|x_k|^2<\infty\right\},
 \qquad
 (\overline Sx)_k=kx_k,
\]

as follows either by graph truncation or by SK-06's spectral domain formula.

The exact imported programme theorems keep their original owners and CC0 attribution. SG-03, the nonclosed analytic-vector restriction wrapper, the bounded-transform endpoint check and these solved exercises are local applications.

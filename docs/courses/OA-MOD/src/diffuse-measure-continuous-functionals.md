# What a functional can detect in measure

**Self-checked by the writing AI.**

A measure neighborhood allows arbitrary size on a sufficiently small projection. A continuous linear functional must therefore vanish on every operator supported there. In a diffuse algebra, splitting finite projections turns this local observation into a description of the entire continuous dual.

Let \(M\subseteq B(H)\) carry a faithful normal semifinite trace \(\tau\). No separability or sigma-finiteness is assumed. Write \(S=S(M,\tau)\) for the completed measurable algebra, and use the strict neighborhoods \(U(r,d)\) of MT03. The bounded finite trace ideal is \(\mathfrak m_\tau\), as constructed in MT13. We call \(M\) **diffuse** when it has no nonzero minimal projection.

Our main statement makes the boundedness convention explicit: for diffuse \(M\), a complex-linear map \(\varphi:M\to\mathbb C\) is measure-continuous if and only if it is norm-bounded and annihilates \(\mathfrak m_\tau\). Its extension to \(S\) is unique and continuous. When \(\tau(1)<\infty\), the continuous dual of \(S\) is zero. These statements give all clauses of Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercise 2, p. 182, in the bounded-functional meaning of its last clause. DU05 proves that the broader reading with an arbitrary algebraic linear map fails; the missing boundedness must not be suppressed.

## Splitting a finite diffuse projection

**Projection-splitting lemma.** Suppose \(M\) is diffuse, \(e\in M\) is a projection, and \(\tau(e)<\infty\). For every \(t\in[0,\tau(e)]\), there is a projection \(p\leq e\) with

\[
 \tau(p)=t.
 \tag{DU.1}
\]

In particular, for every \(d>0\), \(e\) is a finite orthogonal sum of projections whose traces are strictly smaller than \(d\).

**Proof.** First, every nonzero subprojection \(q\leq e\) contains a nonzero projection with arbitrarily small positive trace. Since \(q\) is not minimal, it has a proper nonzero subprojection \(r\). Both \(r\) and \(q-r\) have positive trace by faithfulness, and the smaller of their two traces is at most \(\tau(q)/2\). Repeat inside that smaller projection. After \(n\) steps the trace is positive and at most \(2^{-n}\tau(q)\). This proves the assertion, without requiring the nested intersection to be nonzero.

For \(0<t<\tau(e)\), consider the projections \(p\leq e\) with \(\tau(p)\leq t\), ordered by inclusion. Every chain has an upper bound in this set: its increasing strong supremum exists by BK04, is a projection beneath \(e\), and has trace at most \(t\) by normality. Zorn's lemma gives a maximal member \(p\). If \(\tau(p)<t\), then \(e-p\ne0\). The preceding construction supplies a nonzero \(r\leq e-p\) with

\[
 \begin{gathered}
 0<\tau(r),\\
 \tau(r)<t-\tau(p).
 \end{gathered}
 \tag{DU.2}
\]

Then \(p+r\) belongs to the same set and strictly contains \(p\), a contradiction. Hence \(\tau(p)=t\). The endpoints are given by \(0,e\).

For the finite partition, if \(e=0\) the empty sum suffices. Otherwise choose an integer \(N\) with \(\tau(e)/N<d\). Repeatedly extract a projection of trace \(\tau(e)/N\) from the remaining corner, using (DU.1), and take the final remainder as the last projection. This gives

\[
 \begin{gathered}
 e=\sum_{j=1}^{N}p_j,\\
 \tau(p_j)=\tau(e)/N.
 \end{gathered}
 \tag{DU.3}
\]

Only finite additivity is needed in this last step. The corner remains diffuse because a minimal projection in \(eMe\) would also be minimal in \(M\). \(\square\)

## Continuity forces trace-ideal annihilation

For every traced \(M\), the identity map from the norm topology to the measure topology is continuous. Indeed, \(\|x\|<r\) implies \(x\in U(r,d)\) for every \(d>0\), with witnessing projection \(1\). This is also the first implication in MG03.

Suppose \(\varphi:M\to\mathbb C\) is complex-linear and measure-continuous. There are \(r,d>0\) such that

\[
 \begin{gathered}
 x\in U(r,d)\\
 \Longrightarrow\quad |\varphi(x)|<1.
 \end{gathered}
 \tag{DU.4}
\]

In particular this holds on the norm ball of radius \(r\). Scaling a nonzero \(x\) by positive numbers increasing to \(r/\|x\|\) proves

\[
 |\varphi(x)|\leq r^{-1}\|x\|.
 \tag{DU.5}
\]

Thus no boundedness assumption is needed for this direction.

If a projection \(q\) has \(\tau(q)<d\), then every scalar multiple of \(xq\) lies in \(U(r,d)\), for every \(x\in M\): the cutoff \(1-q\) makes its bounded norm part zero. Equation (DU.4), applied to all those multiples, implies

\[
 \varphi(xq)=0.
 \tag{DU.6}
\]

Now assume \(M\) is diffuse. For any finite-trace projection \(e\), DU01 gives a finite partition into such \(q\)'s. Linearity then yields \(\varphi(xe)=0\) for every \(x\in M\). No countably additive or normal-functional property has been assumed for \(\varphi\).

Finally let \(a\in\mathfrak m_\tau\), and write \(a=v|a|\) in its bounded polar decomposition. The ideal and finite-positive-domain statements in MT13 give \(\tau(|a|)<\infty\). Let

\[
 e_n=1_{[1/n,\infty)}(|a|).
 \tag{DU.7}
\]

The spectral calculus SK04–08 gives

\[
 \begin{gathered}
 \tau(e_n)\leq n\tau(|a|),\\
 \|a-ae_n\|\leq1/n.
 \end{gathered}
 \tag{DU.8}
\]

We already know \(\varphi(ae_n)=0\). Norm continuity from (DU.5) lets \(n\to\infty\), proving \(\varphi(a)=0\). This proves necessity on all of \(\mathfrak m_\tau\), not just on finite-support operators.

## The converse and the completed algebra

Let \(\varphi\in M^*\) be a norm-bounded complex-linear functional with \(\varphi(\mathfrak m_\tau)=0\). Diffuseness is not needed for this converse. If \(x\in U(r,d)\) is witnessed by \(e\), then \(\tau(1-e)<d<\infty\), so \(1-e\in\mathfrak m_\tau\). Its two-sided ideal property gives \(x(1-e)\in\mathfrak m_\tau\). Therefore

\[
 \begin{gathered}
 \varphi(x)=\varphi(xe),\\
 |\varphi(x)|\leq\|\varphi\|\,\|xe\|,\\
 |\varphi(x)|\leq\|\varphi\|r.
 \end{gathered}
 \tag{DU.9}
\]

For any desired scalar neighborhood, fix for example \(d=1\) and then take \(r\) sufficiently small. The zero functional is immediate. This proves measure continuity.

Denote by \(\mathcal A_\tau\) the set of bounded complex-linear functionals on \(M\) that annihilate \(\mathfrak m_\tau\). Write \(M_\tau\) for \(M\) equipped with the measure topology. Combining DU02 and (DU.9), for diffuse \(M\) we have the equality

\[
 M_\tau'=\mathcal A_\tau.
 \tag{DU.10}
\]

Here the prime on the left means the continuous complex-linear dual, not the operator commutant. The prime will not be used for this purpose elsewhere in the lesson.

Each member of (DU.10) extends uniquely to a continuous complex-linear functional \(\widetilde\varphi:S\to\mathbb C\). We give the completion argument explicitly. By MT05, an element \(A\in S\) is represented by a measure-Cauchy sequence \((a_n)\) in \(M\), and equivalent sequences differ by a sequence tending to zero in measure. A continuous linear map is uniformly continuous for the additive uniformity: its value on a difference is the difference of its values. Thus \((\varphi(a_n))\) is Cauchy in \(\mathbb C\), and equivalent sequences have the same limit. Set

\[
 \begin{gathered}
 \widetilde\varphi(A)\\
 =\lim_n\varphi(a_n).
 \end{gathered}
 \tag{DU.11}
\]

Termwise sums and scalar products of representatives prove linearity and extension of \(\varphi\).

For continuity, given \(\varepsilon>0\), choose a neighborhood \(V\) in \(M\) on which \(|\varphi|<\varepsilon/2\). The completion topology has a neighborhood \(W\) of zero contained in the closure of \(V\), after choosing a smaller original neighborhood as in MT05. Every element of \(W\) is a limit of a sequence from \(V\); the countable neighborhood base in MT03 permits choosing that sequence. Formula (DU.11) consequently bounds \(|\widetilde\varphi|\) by \(\varepsilon/2<\varepsilon\) on \(W\). This proves continuity. Uniqueness follows from density of \(M\) in \(S\) and the Hausdorff scalar target. Conversely, restricting a continuous functional on \(S\) gives one on \(M\). These extension and restriction maps are inverse complex-linear maps, so (DU.10) describes the continuous dual of the completed algebra too.

## Finite diffuse trace leaves no continuous dual

Assume \(M\) is diffuse and \(\tau(1)<\infty\). Then

\[
 \mathfrak m_\tau=M.
 \tag{DU.12}
\]

Indeed, for every \(x\in M\), positivity gives \(\tau(x^*x)\leq\|x\|^2\tau(1)<\infty\). Thus \(\mathfrak n_\tau=M\), and its product span is \(M\), since \(x=1^*x\).

If \(F:S\to\mathbb C\) is continuous and complex-linear, DU02 applied to its restriction gives zero on \(\mathfrak m_\tau=M\). For each \(A\in S\), take bounded approximants \(a_n\to A\) in measure, as constructed in MT05 or by the bounded regularizations in MT13. Then

\[
 \begin{gathered}
 F(A)\\
 =\lim_nF(a_n)=0.
 \end{gathered}
 \tag{DU.13}
\]

The zero algebra causes no exception. This proof also explains why norm-continuous functionals on a finite diffuse algebra, including its trace, need not be continuous for convergence in measure: arbitrarily large scalar multiples of an operator on a small nonzero projection all lie in one fixed measure neighborhood.

For an infinite trace, the same annihilator formula (DU.10) holds. It is the bounded annihilator of the finite trace ideal, rather than a claim that the continuous dual must again vanish. The next construction tests the precise boundedness hypothesis.

## Why an algebraic annihilator is too large

We construct a diffuse von Neumann algebra with a faithful normal semifinite infinite trace and an algebraic complex-linear map that vanishes on \(\mathfrak m_\tau\) but is not measure-continuous.

Use Lebesgue measure on \((0,1)\), with the convergence theorems in the preceding scalar integration proofs. Let \(H_0=L^2(0,1)\) and \(A_0=L^\infty(0,1)\). Put

\[
 \begin{gathered}
 H=\bigoplus_{k\geq1}H_0,\\
 M=\prod_{k\geq1}A_0,\\
 \tau(f)\\
 =\sum_{k\geq1}\int_0^1 f_k\,dt.
 \end{gathered}
 \tag{DU.14}
\]

The trace formula is for \(f\in M_+\). The product means uniformly bounded families, acting by multiplication in each Hilbert summand; its norm is \(\sup_k\|f_k\|_\infty\). We verify the required properties, so the counterexample does not rely on an unproved representation claim.

Here the scalar \(L^2\) space really is a Hilbert space of functions modulo equality almost everywhere. For completeness, start with an \(L^2\)-Cauchy sequence and choose a subsequence whose successive differences \(g_n\) have \(L^2\) norms at most \(2^{-n}\). Cauchy–Schwarz for the integral, obtained by expanding the nonnegative integral of a squared linear combination, gives \(\|g_n\|_1\leq\|g_n\|_2\). Monotone convergence makes \(\sum_n|g_n|\) integrable, hence finite almost everywhere. The subsequence therefore has a pointwise almost-everywhere limit \(f\). The triangle inequality for finite \(L^2\) sums follows from the same Cauchy–Schwarz estimate; Fatou's lemma applied to their squared absolute values bounds the \(L^2\) norm of each limiting tail by the corresponding sum of the \(2^{-n}\)'s. Thus \(f\in L^2\) and the subsequence converges in \(L^2\); the original Cauchy sequence has the same limit. Bounded truncations and scalar dominated convergence approximate any \(L^2\) function by bounded functions, and simple approximation then gives the claimed simple-function density. Finally, the Hilbert direct sum is complete: coordinate limits exist for a Cauchy sequence; bounds on every finite sum of squared coordinate differences pass to those limits and then to their supremum, proving square summability and convergence. These arguments use only the scalar convergence proofs and the Hilbert inequalities in BK01.

First the algebra is its own commutant. An operator commuting with its coordinate projections is block diagonal. On one copy of \(L^2(0,1)\), if \(T\) commutes with all bounded multipliers, put \(g=T1\). For every measurable set \(E\),

\[
 \begin{gathered}
 T1_E=1_Eg,\\
 \int_E|g|^2\\
 \leq\|T\|^2\mu(E).
 \end{gathered}
 \tag{DU.15}
\]

Taking \(E\) where \(|g|>\|T\|+\varepsilon\) shows \(g\in L^\infty\) with \(\|g\|_\infty\leq\|T\|\). The first identity then identifies \(T\) with multiplication by \(g\) on simple functions, and hence everywhere by their \(L^2\) density. This density follows from bounded truncation and simple approximation in the scalar integration proof. The bound is uniform across blocks, giving precisely the indicated product algebra. The converse commutation is pointwise. Hence \(M=M'\) and therefore \(M=M''\), which makes it a von Neumann algebra by BK02.

The formula for \(\tau\) is faithful and tracial. It is normal even for increasing bounded nets: each summand is the positive vector functional of the vector which is constant one in that block. Increasing bounded positive nets converge strongly by BK04, so these summands preserve their suprema. For nonnegative numbers, taking the supremum over the directed net commutes with taking the supremum over finite sums: on a given finite set of indices, directedness supplies one common upper index. This proves normality of their sum. Finite-block truncations of every bounded member of \(M\) lie in \(\mathfrak m_\tau\) and converge strongly, boundedly, to that member. By BK03 they converge ultraweakly, proving semifiniteness. The trace of the identity is infinite.

Every nonzero projection has a component \(1_E\) with \(\mu(E)>0\). Divide \((0,1)\) into finitely many intervals, each of length less than \(\mu(E)\). At least one interval \(I\) has \(\mu(E\cap I)>0\), and that intersection has measure strictly less than \(\mu(E)\). Keeping just this subprojection in that block gives a proper nonzero subprojection of the original projection. Thus \(M\) is diffuse.

Partition \(\mathbb N\) into pairwise disjoint infinite sets \(I_j\). For example, take all integers of the form \(2^{j-1}(2m-1)\), with \(m\geq1\). Let \(q_j\in M\) be the projection equal to one on blocks in \(I_j\), and zero elsewhere. Each \(q_j\) has infinite trace. The cosets of the \(q_j\)'s in the algebraic vector-space quotient \(M/\mathfrak m_\tau\) are linearly independent. To see this, for any nonzero finite combination \(a=\sum_j\alpha_jq_j\), disjointness gives \(|a|=\sum_j|\alpha_j|q_j\), whose trace is infinite. But MT13 proves \(\tau(|a|)<\infty\) for every \(a\in\mathfrak m_\tau\). The intersection with this finite-combination space is therefore zero.

Define a linear functional on their span in the quotient by sending the coset of \(q_j\) to \(j\). It extends algebraically to the whole quotient. Explicitly, order its linear extensions to subspaces by inclusion. A chain has a union extension; Zorn's lemma gives a maximal one. If its domain were proper, adjoining any vector outside it and assigning that vector the value zero would extend it further, a contradiction. Composing with the quotient map gives an algebraic linear map \(\psi:M\to\mathbb C\) satisfying

\[
 \begin{gathered}
 \psi(\mathfrak m_\tau)=0,\\
 \psi(q_j)=j,\\
 \|q_j/j\|=1/j,\\
 \psi(q_j/j)=1.
 \end{gathered}
 \tag{DU.16}
\]

The sequence \(q_j/j\) tends to zero in norm and therefore in measure by DU02, but its images do not tend to zero. This verifies failure of measure continuity directly. Thus annihilating the trace ideal is sufficient for bounded functionals, as proved in DU03; removing boundedness from that assertion changes it to a false statement.

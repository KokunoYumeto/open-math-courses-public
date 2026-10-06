# When countable sums detect extended positive energy

*GPT-6 (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0.*

A bounded positive operator can be tested against every normal positive functional. An unbounded positive energy can be tested the same way, but its value may be infinite. The useful question is whether a proposed function on the positive predual really comes from such an energy. Countable positive sums give an answer even when the Hilbert space is nonseparable and the function takes infinite values.

We use concrete predual completion, the positive-vector expansion from spatial forms, the characterization of normal weights, and the spectral description of extended positive energies. These are precise dependencies of the argument, not claims that their separate course reviews are finished.

## The countable-sum criterion

Let \(N\subseteq B(\mathcal H)\) be a faithful normal concrete representation. There is no dimension or separability restriction on \(\mathcal H\). Suppose

\[
 m:N_*^+\longrightarrow[0,\infty]
\]

is additive, nonnegatively homogeneous, and satisfies \(m(0)=0\), using \(0\cdot\infty=0\). By a positive series \(\psi=\sum_{j\geq1}\psi_j\) in \(N_*\), we mean convergence of its partial sums in predual norm. Since positive functionals have norm \(\psi_j(1)\), this is equivalent to \(\sum_j\psi_j(1)<\infty\).

**Theorem.** The function \(m\) is lower semicontinuous for the predual norm if and only if every positive series of this kind satisfies

\[
 m\!\left(\sum_{j\geq1}\psi_j\right)
   =\sum_{j\geq1}m(\psi_j).
 \tag{CA.1}
\]

Thus the criterion recognizes the full extended positive cone \(\widehat N_+\). In particular, it does not assume \(m(\psi)<\infty\) for any nonzero \(\psi\).

The easier direction is already instructive. Write \(s_k=\sum_{j\leq k}\psi_j\). Positivity and additivity give \(m(s_k)\leq m(\psi)\), while \(s_k\to\psi\) in norm. Lower semicontinuity gives \(m(\psi)\leq\liminf_k m(s_k)\). The two inequalities prove (CA.1), including the case in which both sides are infinite. The converse needs a way to turn a sequence condition into normality for arbitrary increasing nets.

## Trace-class coordinates without separability

For a bounded positive operator \(a\) on \(\mathcal H\), define \(\operatorname{Tr}(a)\) as the supremum of \(\sum_{\xi\in F}\langle a\xi,\xi\rangle\) over finite orthonormal sets \(F\). Parseval identifies this with the corresponding supremum along any orthonormal basis. The trace is additive: to obtain the nontrivial inequality, place finite test subspaces for two positive operators inside their common finite-dimensional span. It is also normal: if a bounded positive net \(a_i\) increases to \(a\), each finite scalar sum converges increasingly, so interchange of the two suprema gives \(\operatorname{Tr}(a)=\sup_i\operatorname{Tr}(a_i)\).

A positive operator has finite trace precisely when it is positive trace class. Indeed, \(\operatorname{Tr}(a)<\infty\) forces \(1_{[\varepsilon,\infty)}(a)\mathcal H\) to be finite-dimensional for every \(\varepsilon>0\); these spectral cutoffs approximate \(a\) in norm. Its nonzero eigenvalues form an at most countable summable list. For a positive trace-class operator \(a=\sum_k\lambda_k|v_k\rangle\langle v_k|\) and \(x\in B(\mathcal H)\), set

\[
 \omega_a(x)=\sum_k\lambda_k\langle xv_k,v_k\rangle.
 \tag{CA.2a}
\]

Finite spectral truncations converge in trace norm. Their vector functionals therefore converge in predual norm, by the positive norm identity \(\|\omega_b\|=\omega_b(1)=\operatorname{Tr}(b)\). The resulting \(\omega_a\) is normal. Formula (CA.2a) is also the meaning of \(\operatorname{Tr}(ax)\) for general \(x\), where \(ax\) need not be positive.

Conversely, the positive-vector expansion supplies, for every \(\omega\in B(\mathcal H)_*^+\), vectors \(\xi_j\) with \(\omega=\sum_j\omega_{\xi_j}\) and \(\sum_j\|\xi_j\|^2=\omega(1)\). The positive finite-rank sums \(a_n=\sum_{j\leq n}|\xi_j\rangle\langle\xi_j|\) are Cauchy in operator norm: the norm of a positive tail is at most its trace, namely the corresponding tail of \(\sum_j\|\xi_j\|^2\). Let \(a\) be their positive limit. Normality of the trace gives \(\operatorname{Tr}(a)=\omega(1)<\infty\), and the positive remainders show \(a_n\to a\) in trace norm. For a unit vector \(\eta\),

\[
\begin{aligned}
 \omega(|\eta\rangle\langle\eta|)
 &=\sum_j|\langle\xi_j,\eta\rangle|^2\\
 &=\langle a\eta,\eta\rangle\\
 &=\omega_a(|\eta\rangle\langle\eta|).
\end{aligned}
 \tag{CA.2c}
\]

Polarization and ultraweak density of finite-rank operators make the two normal functionals equal everywhere. Thus every positive normal functional on \(B(\mathcal H)\) has a positive trace-class coordinate.

We also need the norm of a difference. For \(a,b\geq0\) trace class, let \(c=a-b\). An eigenvector of the compact self-adjoint \(c\) with eigenvalue \(\mu\) satisfies \(|\mu|\leq\langle(a+b)v,v\rangle\). Summing over finite orthonormal eigenfamilies shows \(\operatorname{Tr}|c|\leq\operatorname{Tr}(a)+\operatorname{Tr}(b)\). Its spectral series defines a normal functional \(\omega_c\), with

\[
 |\omega_c(x)|\leq\|x\|\operatorname{Tr}|c|.
 \tag{CA.2b}
\]

On rank-one projections this functional equals \(\omega_a-\omega_b\); polarization and normality extend equality to all of \(B(\mathcal H)\). Testing on the contraction \(\operatorname{sgn}(c)\) gives the reverse norm inequality. Hence

\[
 \|\omega_a-\omega_b\|=\operatorname{Tr}|a-b|=\|a-b\|_1.
\]

This positive-cone identification uses no separable basis and does not require identifying an entire complex tensor quotient with trace class.

## Turning positive series into a normal weight

Assume now that (CA.1) holds, and write \(\mathcal T_+=\mathcal S_1(\mathcal H)_+\). For \(a\in\mathcal T_+\), define

\[
 q(a)=m(\omega_a|_N)+\operatorname{Tr}(a).
 \tag{CA.2}
\]

Adding the trace makes \(q(a)\geq\operatorname{Tr}(a)\), while the trace term can later be removed because it is continuous in trace norm. Extend \(q\) to all bounded positive operators by

\[
 W(a)=
 \begin{cases}
 q(a),&a\in\mathcal T_+,\\
 \infty,&\text{otherwise}.
 \end{cases}
 \tag{CA.3}
\]

The trace-class cone is hereditary. Consequently (CA.3) is an additive, nonnegatively homogeneous weight, even when one or both summands have infinite trace.

To verify normality, take any bounded increasing net \(a_i\uparrow a\). If \(\operatorname{Tr}(a)=\infty\), normality of the trace and \(W\geq\operatorname{Tr}\) yield \(W(a)=\sup_iW(a_i)=\infty\). If \(\operatorname{Tr}(a)<\infty\), all \(a_i\) are trace class. From the net choose increasing indices \(i_k\) for which \(\operatorname{Tr}(a-a_{i_k})<2^{-k}\). Put \(d_1=a_{i_1}\) and \(d_k=a_{i_k}-a_{i_{k-1}}\) for \(k>1\). These positive increments sum to \(a\) in trace-class norm, and their restrictions \(\omega_{d_k}|_N\) sum in predual norm. Apply (CA.1) and ordinary trace additivity to obtain

\[
\begin{aligned}
 W(a)&=q(a)=\sum_kq(d_k),\\
 &=\sup_kW(a_{i_k})\\
 &\leq\sup_iW(a_i).
\end{aligned}
 \tag{CA.4}
\]

Monotonicity gives the reverse inequality. The sequence was extracted only for this one finite-trace element; no countable cofinal subset of the original net or of the algebra was assumed.

The normal-weight characterization now expresses \(W\) as a pointwise supremum of bounded positive normal functionals. In particular, \(W\) is lower semicontinuous in operator norm on \(B(\mathcal H)_+\). If positive trace-class \(a_n\to a\) in trace norm, then also \(a_n\to a\) in operator norm. Applying that lower semicontinuity to (CA.2) and subtracting the convergent finite trace terms shows that \(a\mapsto m(\omega_a|_N)\) is lower semicontinuous in trace norm. By the norm identity above, it defines an extended positive functional on \(B(\mathcal H)_*^+\).

## Descending to the represented algebra

Call that last functional \(\widetilde m\). For every unitary \(u\in N'\) and positive trace-class \(a\), restriction to \(N\) is unchanged under conjugation, so

\[
 m(\omega_{uau^*}|_N)=m(\omega_a|_N).
 \tag{CA.5}
\]

The spectral-form theorem assigns to \(\widetilde m\) a unique pair: a projection \(e\in B(\mathcal H)\) and a positive self-adjoint operator \(A\) on \(e\mathcal H\), with an infinite part off \(e\mathcal H\). Equation (CA.5) and uniqueness force this pair to be invariant under all unitaries in \(N'\). Thus \(e\in N\), and the spectral projections of \(A\) lie in \(eNe\). The same bounded spectral tests define \(H\in\widehat N_+\).

For \(\psi\in N_*^+\), the positive-vector expansion gives a positive trace-class lift \(a=\sum_j|\xi_j\rangle\langle\xi_j|\) with \(\omega_a|_N=\psi\). Each bounded spectral test belongs to \(N\), so it has the same value on \(\psi\) as on its lift. Taking their supremum gives

\[
\begin{aligned}
 H(\psi)&=\widetilde m(\omega_a)\\
 &=m(\omega_a|_N)\\
 &=m(\psi).
\end{aligned}
 \tag{CA.6}
\]

Therefore \(m\) is lower semicontinuous, proving the converse and the theorem. A countable expansion of each individual normal functional is all that was needed; \(\mathcal H\) itself may have arbitrary dimension.

As a boundary example, let \(m(0)=0\) and \(m(\psi)=\infty\) for every nonzero \(\psi\in N_*^+\). It obeys (CA.1). Its representing spectral pair has zero finite-energy subspace. The theorem therefore includes energies that are nowhere finite away from zero; it is not a semifiniteness criterion.

**Example and check.** Let \(I\) be any set and let \(N=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\). Choose numbers \(h_i\in[0,\infty]\), and for \(\psi=(\psi_i)\in\ell^1(I)_+\) put

\[
 m_h(\psi)=\sum_{i\in I}h_i\psi_i,
\]

where the sum is the supremum of finite subsums and \(0\cdot\infty=0\). Verify (CA.1) by interchanging nonnegative sums: both orders are the supremum over finite subsets of \(I\times\mathbb N\). Thus every coordinate may carry a different finite or infinite energy, even when \(I\) is uncountable. The representing extended positive is the diagonal operator with those energies and an infinite part at the coordinates where \(h_i=\infty\).

**References.** M. Takesaki, *Theory of Operator Algebras II*, IX.4, Lemma 4.19 (Springer, 2003), printed p. 224, is the source-range antecedent for the criterion. The trace-class bridge, dependencies, and proof organization above are independently written for this course. The neighboring IX.4 existence theorem and the analytic sum identity still require separate treatment; this lesson does not claim them.

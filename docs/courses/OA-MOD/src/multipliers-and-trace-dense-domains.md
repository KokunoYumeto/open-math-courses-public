# Functions, cutoffs and actual domains

**Self-checked by the writing AI.**

An unbounded multiplier is determined by both a function and the set of square-integrable vectors it can multiply. We first recover that entire domain from the bounded coordinates of a closed graph. The spectral-tail criterion then becomes a condition on level sets of the function. Finally, countable intersections of trace-dense subspaces provide common domains for families of measurable operators.

For MM01–04 let \((X,\Sigma,\mu)\) be a sigma-finite measure space. It need not be standard, countably generated or complete, and \(L^2(\mu)\) need not be separable. Functions mean \(\Sigma\)-measurable representatives modulo equality outside a measurable null set. A function finite almost everywhere is assigned the value zero on its measurable exceptional set. The scalar integration programme, Sections 0–2, supplies measure and convergence facts; SS1 supplies the complete scalar Hilbert space and finite-support simple approximation. Inner products are linear in the first entry.

The same results are treated in with Masamichi Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercises 4 and 5, pp. 182–183. Our construction starts with the concrete representation and closed graph, so the multiplication formula does not conceal a domain assertion. MM05 applies to arbitrary traced von Neumann algebras, without a sigma-finiteness assumption.

## The multiplication algebra and its trace

Put \(H=L^2(\mu)\). For \(g\in L^\infty(\mu)\), let \(M_g:H\to H\) be multiplication by \(g\). Then

\[
 \|M_g\|=\|g\|_\infty.
 \tag{MM.1}
\]

The upper bound follows by integrating \(|g\xi|^2\). For the reverse bound, if \(s<\|g\|_\infty\) is nonnegative, the set where \(|g|>s\) has positive measure. Sigma-finiteness gives a measurable subset \(E\) of finite positive measure. Testing on \(1_E\) gives \(\|M_g1_E\|_2>s\|1_E\|_2\). Let \(s\) increase to the essential supremum. In particular the multiplication representation is faithful. The same test shows that a multiplier is a positive operator exactly when its function is nonnegative almost everywhere.

Let \(M=\{M_g:g\in L^\infty(\mu)\}\). We prove \(M'=M\). Choose a measurable disjoint partition \((E_n)\) of \(X\) with \(\mu(E_n)<\infty\), by disjointizing a countable finite-measure cover. A bounded \(T\in M'\) commutes with every projection \(M_{1_{E_n}}\). On the corresponding Hilbert summand, put \(h_n=T1_{E_n}\). For any measurable \(F\subseteq E_n\), commutation gives \(T1_F=1_Fh_n\). Consequently

\[
 \begin{gathered}
 \int_F|h_n|^2\,d\mu\\
 \leq\|T\|^2\mu(F).
 \end{gathered}
 \tag{MM.2}
\]

Testing where \(|h_n|>\|T\|+\varepsilon\) proves \(|h_n|\leq\|T\|\) almost everywhere on \(E_n\). Patch these representatives to a measurable \(h\), with that same bound. The countable union of the exceptional null sets is null. On simple functions supported in one \(E_n\), then on finite sums of such functions, \(T=M_h\). Those functions are dense in \(H\): first truncate to finitely many pieces, then use SS1 on each finite piece. Thus \(T=M_h\) everywhere. The reverse commutation follows pointwise. The bicommutant theorem BK02 now makes \(M\) a von Neumann algebra.

For nonnegative bounded \(g\), define

\[
 \tau(M_g)=\int_X g\,d\mu.
 \tag{MM.3}
\]

This is a faithful normal semifinite trace. Faithfulness follows from the scalar integral and (MM.1); traciality follows from commutativity and \(|g|^2=|\bar g|^2\). For normality, write the integral as the sum of the positive vector functionals determined by \(1_{E_n}\). Each preserves increasing bounded suprema because those nets converge strongly by BK04. A supremum over a directed set commutes with a sum of nonnegative terms: express the sum as the supremum of finite sums and use a common upper index on each finite set. Thus their sum is normal. Finally, put \(F_N=\bigcup_{n\leq N}E_n\), \(e=M_{1_{F_N}}\), and \(x=M_{g1_{F_N}}\). Both \(e\) and \(x\) belong to \(\mathfrak n_\tau\), since their squared absolute values have integrals bounded respectively by \(\mu(F_N)\) and \(\|g\|_\infty^2\mu(F_N)\). Thus \(x=e^*x\) belongs to \(\mathfrak m_\tau\), directly from its definition in WG002. These truncations converge strongly, with a common norm bound, to \(M_g\), hence ultraweakly by BK03. This proves semifiniteness without first invoking a theorem that assumes it.

## A measurable function defines a full closed operator

Let \(f:X\to\mathbb C\) be measurable and finite almost everywhere. Define \(T_f:D(T_f)\subseteq H\to H\) as follows. Its domain consists exactly of the vectors \(\xi\in H\) satisfying the first condition below; the second formula specifies its action:

\[
 \begin{gathered}
 f\xi\in H,\\
 T_f\xi=f\xi.
 \end{gathered}
 \tag{MM.4}
\]

The domain is linear, and both domain and action depend only on the almost-everywhere class of \(f\). Let \(P_n\) be multiplication by \(1_{\{|f|\leq n\}}\). These projections increase strongly to the identity, by dominated convergence applied to \(|\xi|^2\). Their ranges are contained in \(D(T_f)\), proving density.

The operator is closed. If \(\xi_j\to\xi\) and \(T_f\xi_j\to\eta\) in \(H\), bounded multiplication by \(f1_{\{|f|\leq n\}}\) gives
\(fP_n\xi=P_n\eta\) for every \(n\). Outside the union of the corresponding countably many null sets, these equalities imply \(f\xi=\eta\), because \(f\) is finite almost everywhere. Thus \(\xi\in D(T_f)\) and \(T_f\xi=\eta\).

Every unitary in \(M'=M\) is multiplication by a function of modulus one. Such a unitary preserves (MM.4) in both directions and commutes with the action. Hence \(T_f\) is affiliated with \(M\), with no boundedness assumption on \(f\).

The adjoint and absolute value have their maximal multiplication domains:

\[
 \begin{gathered}
 T_f^*=T_{\bar f},\\
 |T_f|=T_{|f|}.
 \end{gathered}
 \tag{MM.5}
\]

For the adjoint, the scalar pairing first gives \(T_{\bar f}\subseteq T_f^*\). If \(\eta\in D(T_f^*)\) has adjoint image \(\zeta\), test its defining identity on all vectors in \(P_nH\). The bounded multiplier adjoint formula gives \(\bar fP_n\eta=P_n\zeta\). Letting these sets increase to the whole space shows \(\bar f\eta=\zeta\in H\), proving the reverse domain inclusion. For real \(f\), the resulting operator is self-adjoint, and for nonnegative \(f\) its quadratic form is nonnegative. The product \(T_f^*T_f\) is multiplication by \(|f|^2\) on the domain where \(|f|^2\xi\in H\): the additional condition \(f\xi\in H\) follows from \(t^2\leq1+t^4\) and \(\xi\in H\). This is also the square of the positive self-adjoint \(T_{|f|}\), so uniqueness of the positive square root in SK07 proves (MM.5).

For every \(\xi\in D(T_f)\), dominated convergence gives both limits

\[
 \begin{aligned}
 P_n\xi&\longrightarrow\xi,\\
 T_fP_n\xi&\longrightarrow T_f\xi.
 \end{aligned}
 \tag{MM.6}
\]

Thus the bounded cutoffs form a graph core, rather than merely a Hilbert-space dense subspace. The spectral projections of \(T_{|f|}\) are multiplication by the inverse images of Borel sets under \(|f|\). Indeed these projections form a strongly countably additive spectral measure by scalar dominated convergence; their spectral integral has exactly (MM.4) and the action of \(|f|\). Uniqueness of the spectral resolution in SK05–08 identifies it with the self-adjoint operator just constructed.

## Every affiliated operator is such a multiplier

Let \(T:D(T)\subseteq H\to H\) be any closed densely defined operator affiliated with \(M\), and put \(a=|T|\). It is not initially assumed normal or positive. The closed polar decomposition in RD02 and the bounded graph coordinates in MT07 give bounded members \(b,c\in M\) satisfying

\[
 \begin{gathered}
 c=(1+a^2)^{-1/2},\\
 b=Tc,\\
 cH=D(T),\\
 c^2+b^*b=1.
 \end{gathered}
 \tag{MM.7}
\]

The range equality includes all of \(D(T)\): spectral integration puts \(cH\) in \(D(|T|)\), while for \(\xi\in D(|T|)\), the vector \((1+|T|^2)^{1/2}\xi\) maps to \(\xi\) under \(c\). Also \(c\) is injective, since its strictly positive scalar spectral function has zero kernel. These facts are valid for arbitrary closed densely defined \(T\), including a nontrivial kernel of \(T\) itself.

By MM01, write \(c=M_g\) and \(b=M_h\). Positivity and contractivity of \(c\), its injectivity, and (MM.7) imply, almost everywhere,

\[
 \begin{gathered}
 0<g\leq1,\\
 g^2+|h|^2=1.
 \end{gathered}
 \tag{MM.8}
\]

To justify the strict positivity, if \(\{g=0\}\) had positive measure, sigma-finiteness would give a finite positive-measure subset whose nonzero indicator lies in \(\ker c\). The pointwise identity follows from faithfulness of the multiplication representation. Choose one measurable conull set for these finitely many conditions, put \(f=h/g\) there, and set \(f=0\) on its measurable null complement.

We now compare domains, not just formal quotients of operators. For \(\xi\in H\), membership in \(cH\) is equivalent to \(\xi/g\in H\). Equation (MM.8) gives, almost everywhere,

\[
 \frac1{g^2}=1+|f|^2.
 \tag{MM.9}
\]

Thus \(\xi/g\in H\) holds exactly when \(f\xi\in H\). By (MM.4) and (MM.7), \(D(T)=D(T_f)\). On this domain write \(\xi=c\eta\); then

\[
 \begin{aligned}
 T\xi&=b\eta\\
 &=h\eta=f\xi.
 \end{aligned}
 \tag{MM.10}
\]

Hence \(T=T_f\) as closed operators with their complete domains.

The representing function is unique almost everywhere. For a multiplier \(T_f\), (MM.5) makes its graph coordinates multiplication by \((1+|f|^2)^{-1/2}\) and \(f(1+|f|^2)^{-1/2}\). Their quotient is \(f\). Since \(b,c\) are determined by \(T\), and bounded multiplier functions are unique by (MM.1), the recovered class is unique. This proves the full affiliated-operator classification without a disintegration theorem or a standard-space assumption.

## Exactly which functions are trace-measurable

For \(R>0\), let \(Q_R\) be the spectral projection of \(|T_f|\) for the interval \((R,\infty)\). Its trace is now a scalar measure:

\[
 \begin{gathered}
 \tau(Q_R)\\
 =\mu\{|f|>R\}.
 \end{gathered}
 \tag{MM.11}
\]

The full spectral-tail theorem MT11 therefore says that \(T_f\) is \(\tau\)-measurable exactly when

\[
 \begin{gathered}
 \mu\{|f|>R\}\to0\\
 (R\to\infty).
 \end{gathered}
 \tag{MM.12}
\]

Together with MM02–03, this is a bijection between \(S(M,\tau)\) and the almost-everywhere classes of measurable functions satisfying (MM.12). It includes the actual operator domains, not just the spectral distributions.

The condition can equally be written with \(\mu\{|f|\geq n\}\to0\) for positive integers \(n\), as in the source. Write \(A_t=\{|f|>t\}\) and \(B_n=\{|f|\geq n\}\). For \(n\geq2\),

\[
 \begin{gathered}
 A_n\subseteq B_n,\\
 B_n\subseteq A_{n-1}.
 \end{gathered}
 \tag{MM.13}
\]

Monotonicity also equates the integer and real-parameter limits. If one initially permits an extended-valued measurable function, this tail condition forces its infinite-value set to have measure zero, since that set is contained in every tail. It may then be replaced by zero there. A function infinite on a positive-measure set would not yield a dense multiplication domain: every permissible vector would vanish on that set, leaving a nonzero orthogonal indicator on a finite-measure subset.

Equivalently, some high-level set has finite measure. Necessity follows from (MM.12). Conversely, if one tail has finite measure, the larger-level tails decrease to a null set because \(f\) is finite almost everywhere. Subtract their complementary increasing measures inside that one finite tail and use monotone convergence. This proves the limit without subtracting infinite measures.

On a finite measure space every finite-almost-everywhere measurable function satisfies the criterion. On \((0,\infty)\) with Lebesgue measure, multiplication by \(f(x)=x\) is closed, densely defined and affiliated, but is not trace-measurable: every high-level set has infinite measure. By contrast, the function equal to \(1/x\) on \((0,1)\) and zero elsewhere is trace-measurable and unbounded; for \(R\geq1\) its tail has measure \(1/R\). Thus sigma-finiteness alone does not replace the global tail requirement by local finiteness.

## Common domains from small trace defects

Now let \(N\subseteq B(K)\) be an arbitrary von Neumann algebra with a faithful normal semifinite trace \(\rho\). No countability assumption is imposed on \(N\) or \(K\). A linear subspace \(D\subseteq K\), not necessarily closed, is **\(\rho\)-dense** if there are increasing projections \(p_n\in N\) such that

\[
 \begin{gathered}
 p_nK\subseteq D,\\
 \rho(1-p_n)\to0.
 \end{gathered}
 \tag{MM.14}
\]

This is equivalent to the following single-cutoff condition: for every \(d>0\), some projection \(q\in N\) satisfies

\[
 \begin{gathered}
 qK\subseteq D,\\
 \rho(1-q)<d.
 \end{gathered}
 \tag{MM.15}
\]

**Proof of equivalence.** Condition (MM.14) gives (MM.15) by choosing one sufficiently large index. Conversely choose \(q_jK\subseteq D\) with \(\rho(1-q_j)<2^{-j}\), and define the tail intersections

\[
 p_n=\bigwedge_{j\geq n}q_j.
 \tag{MM.16}
\]

They increase and satisfy \(p_nK\subseteq q_nK\subseteq D\). The projection estimate in MT02, valid for noncommuting projections, gives

\[
 \begin{gathered}
 \rho(1-p_n)\\
 \leq\sum_{j\geq n}2^{-j}\\
 =2^{1-n}\longrightarrow0.
 \end{gathered}
 \tag{MM.17}
\]

This proves (MM.14). Taking increasing joins of the \(q_j\)'s would not justify containment in a nonclosed \(D\); the tail intersections are the relevant construction. Faithfulness and normality give \(p_n\uparrow1\) strongly, as proved in MT02, so every \(\rho\)-dense subspace is also Hilbert-space dense. \(\square\)

**Countable intersection theorem.** If \((D_j)_{j\geq1}\) are \(\rho\)-dense subspaces, then \(\bigcap_jD_j\) is \(\rho\)-dense.

**Proof.** Fix \(d>0\), and write \(D=\bigcap_jD_j\). Using the single-cutoff condition, choose \(q_jK\subseteq D_j\) with \(\rho(1-q_j)<d2^{-j-1}\), and put \(q=\bigwedge_jq_j\). Then

\[
 \begin{gathered}
 qK\subseteq D,\\
 \rho(1-q)\\
 \leq d/2<d.
 \end{gathered}
 \tag{MM.18}
\]

The trace bound is again MT02, by summing the geometric majorants. Apply the already proved equivalence to the intersection. No subspace was assumed closed, and no pair of projections was assumed to commute. \(\square\)

In particular, the domains of countably many \(\rho\)-measurable operators have a common \(\rho\)-dense linear subspace, namely their intersection: MT11 gives (MM.15) for each domain, and the theorem applies. This assertion does not say that the operators are bounded on their whole domains, or that arbitrary uncountable intersections retain the same property.

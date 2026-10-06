# The local index formula

*Written by GPT-6.1 Sol (OpenAI), September 2026, at Ultra. Draft chapter; Self-checked by the writing AI and spot-checked by a separate Codex session across all numbered results and solved exercises, under explicit imports. The reviewer authored three clarifications; those edits have not received a second independent check. Exact reviewer model identifier is not independently verified. Not formally verified. Public domain (CC0).*

An index is determined by finite-dimensional defects of an operator. A residue measures an asymptotic spectral coefficient. A local index theorem connects these two kinds of information. Before deriving that connection in general, we need to identify the Fredholm operator being counted and fix the sign and spectral variable in an example where both sides can be computed directly.

Read [Spectral triples and dimension spectrum](../spectral-triples-and-dimension-spectrum.html) for the regularity and complex-power calculus, and [Singular values and the Dixmier trace](../singular-values-and-the-dixmier-trace.html) for logarithmic trace coefficients. We use the Fredholm parametrix criterion and norm stability of the index from [Finite defects under perturbation](../../elliptic-boundary-reduction/fredholm-stability.html#compact-errors-and-approximate-inverses). Section 6 specifies the cyclic differentials and their normalizations. Basic references are [Connes–Moscovici 1995], [Jaffe–Lesniewski–Osterwalder 1988], and [Carey–Phillips–Rennie–Sukochev 2006].

## 1. The positive spectral compression

Let \(D\) be invertible and selfadjoint with compact resolvent, let \(F=\operatorname{sign}D\), and put

\[

P=\frac{1+F}{2}.

\tag{1.1}

\]

This is the orthogonal projection onto the positive spectral subspace. Suppose \(a\) is bounded, preserves \(\operatorname{Dom}D\), and \([D,a]\) extends boundedly.

**Lemma 1.1.** The commutator \([F,a]\) is compact. In particular, bounded first commutators with \(D\), rather than all the higher regularity conditions, suffice for this Fredholm mechanism.

**Proof.** If \(|D|\geq cI\), functional calculus gives the strong integral

\[

F=\frac2\pi\int_0^\infty D(D^2+t^2)^{-1}\,dt.

\]

The integral defining \(F\) itself need not converge in operator norm at infinity. Its commutator does. Set \(R_\pm(t)=(D\pm it)^{-1}\). Since

\[

D(D^2+t^2)^{-1}=\tfrac12(R_+(t)+R_-(t)),\qquad

[R_\pm(t),a]=-R_\pm(t)[D,a]R_\pm(t),

\]

the commutator integrand has norm at most

\[

\frac{\|[D,a]\|}{c^2+t^2}.

\tag{1.2}

\]

This is integrable on the positive half-line. Every \(R_\pm(t)\) is compact, including at \(t=0\), because \(D\) has compact resolvent and is invertible. Thus every commutator integrand is compact; its norm integral is compact as well. To identify that integral with \([F,a]\), truncate the integrals defining \(F\). Scalar functional calculus makes the truncations uniformly bounded and strongly convergent to \(F\). Their commutators converge strongly to \([F,a]\) and in norm to the compact integral just constructed, so the two limits agree. \(\square\)

**Proposition 1.2.** If \(U\) is unitary and satisfies the preceding domain and bounded-commutator conditions, then

\[

T_U=PUP:PH\longrightarrow PH

\tag{1.3}

\]

is Fredholm.

**Proof.** Lemma 1.1 gives \([P,U]\) compact. The abstract compression criterion applies with orthogonal projection \(P\), unitary \(U\), and candidate parametrix \(PU^*P\). Its two errors are

\(PU[P,U^*]P\) and \(PU^*[P,U]P\), hence compact. For example,

\(PUPU^*P-P=PU(PU^*-U^*P)P\). The Fredholm parametrix theorem in the prerequisite gives the conclusion. All of its boundedness and compactness conditions have been identified here. \(\square\)

Our convention is

\[

\operatorname{Index}T_U=\dim\ker T_U-\dim\ker T_U^*.

\tag{1.4}

\]

The two kernels are inside \(PH\). The compressed symbol and its adjoint should not be confused with kernels of \(U\) on \(H\), since a unitary has no such kernels.

## 2. Fixing the sign on a circle

Use the circle triple from the previous lesson:

\[

D=-i\partial_x+\eta,\qquad 0<\eta<1,\qquad

H=L^2(\mathbb R/2\pi\mathbb Z).

\]

The positive spectral space is spanned by \(e_k\), \(k\geq0\). For \(u(x)=e^{imx}\), multiplication sends \(e_k\) to \(e_{k+m}\).

If \(m\geq0\), the compression is injective and misses the first \(m\) basis vectors of \(PH\). Its index is \(-m\). If \(m=-r<0\), its kernel consists of \(e_0,\ldots,e_{r-1}\), and its range is all of \(PH\). Its index is \(r=-m\). Thus in both cases

\[

\operatorname{Index}(PM_uP)=-m.

\tag{2.1}

\]

**Theorem 2.1 (the circle index and its local residue).** For a smooth function \(u:\mathbb R/2\pi\mathbb Z\to S^1\),

\[

\operatorname{Index}(PM_uP)

=-\frac1{2\pi i}\int_0^{2\pi}u^{-1}(x)u'(x)\,dx

=-\operatorname*{Res}_{z=0}

\operatorname{Tr}\bigl(M_u^{-1}[D,M_u]|D|^{-1-2z}\bigr).

\tag{2.2}

\]

**Proof.** The integral divided by \(2\pi i\) is an integer \(m\). To see both the integrality and the relevant homotopy, choose a real argument at \(x=0\) and integrate the real function \(-iu^{-1}u'\). Its exponential is \(u\), by differentiation. The argument increases by \(2\pi m\) over one period. Subtracting \(mx\) produces a smooth periodic real function \(f\), with

\[

u(x)=e^{imx}e^{if(x)}.

\]

The path \(u_t=e^{imx}e^{itf(x)}\), \(0\leq t\leq1\), is smooth and unitary. Its multiplication operators form a norm-continuous path because

\(\|M_{u_t}-M_{u_s}\|\leq |t-s|\|f\|_\infty\).

Each compression is Fredholm by Proposition 1.2. Norm stability of the Fredholm index therefore reduces its value to (2.1).

For the residue, \([D,M_u]=-iM_{u'}\). The diagonal matrix entry of multiplication by any smooth \(g\) in the Fourier basis is its mean \(\widehat g(0)\). Therefore, initially in the trace-class half-plane,

\[

\operatorname{Tr}\bigl(M_u^{-1}[D,M_u]|D|^{-1-2z}\bigr)

=\left(\frac1{2\pi}\int_0^{2\pi}-iu^{-1}u'\,dx\right)

\left(\zeta(1+2z,\eta)+\zeta(1+2z,1-\eta)\right).

\tag{2.3}

\]

The previous lesson proves that each Hurwitz zeta function has residue one at argument one. Substituting \(1+2z\) divides each residue by two. The second factor in (2.3) consequently has residue one at zero, and the first factor is \(m\). This proves the second equality in (2.2). \(\square\)

This example fixes two independent conventions. The positive spectral compression contributes a minus sign relative to the winding integral. The exponent \(-1-2z\) contributes a factor one-half relative to the variable \(-1-z\). Changing either convention without changing the formula would already fail on \(u=e^{ix}\).

## 3. Why only finitely many commutator terms survive

For a regular triple with summability bound \(p\), let \(n\geq1\), \(k=(k_1,\ldots,k_n)\in\mathbb N^n\), and write

\[

T_{n,k}=a^0\nabla^{k_1}(da^1)\cdots\nabla^{k_n}(da^n)

|D|^{-n-2|k|},\qquad |k|=\sum_j k_j.

\tag{3.1}

\]

By the preceding lesson, every factor \(\nabla^{k_j}(da^j)\) has order at most \(k_j\). Thus \(T_{n,k}\) has order at most

\[

|k|-n-2|k|=-n-|k|.

\tag{3.2}

\]

If \(n+|k|>p\), the function

\(\operatorname{Tr}(T_{n,k}|D|^{-2z})\) is holomorphic on a neighborhood of zero: its order remains strictly below \(-p\) there. Every higher residue \(\tau_q(T_{n,k})\), \(q\geq0\), consequently vanishes. This proves the finite bound \(n+|k|\leq p\) on potentially contributing terms, independent of any cocycle assertion.

The degree-zero constant coefficient in the even case behaves differently. A trace-class operator can have a nonzero value at zero despite having no pole. The finite-dimensional example in [Spectral triples and dimension spectrum](../spectral-triples-and-dimension-spectrum.html) exhibits that distinction exactly. It is why the degree-zero term must be specified before claiming a full even index formula.

## 4. A finite part that preserves a cohomology class

The algebraic part of renormalization can be isolated from heat kernels. This is useful because it tells us exactly which analytic facts a heat-kernel argument must supply.

Let \(E^\bullet\) be a complex of complete locally convex spaces, with continuous differential \(d:E^j\to E^{j+1}\) and \(d^2=0\). The application will use cochains and \(d=b+B\). For the next lemma, the cochain spaces and their topology are fixed in advance. Integration and analytic continuation are required in those spaces, rather than only after evaluating on a single cycle.

Suppose \(c(t)\in E^j\), \(0<t\leq1\), is continuously differentiable, and \(K(t)\in E^{j-1}\) is continuous, with

\[

dc(t)=0,\qquad c'(t)=dK(t).

\tag{4.1}

\]

Assume their seminorms grow at most like a fixed negative power of \(t\), allowing additional finite powers of \(|\log t|\). Thus, for sufficiently large \(\operatorname{Re}z\), the integrals

\[

C(z)=\int_0^1t^{z-1}c(t)\,dt,\qquad

J(z)=\int_0^1t^zK(t)\,dt

\tag{4.2}

\]

exist. Assume these integrals continue meromorphically to a neighborhood of zero, with finite pole order there and Laurent coefficients in the indicated cochain spaces. These are hypotheses of the lemma. Scalar meromorphy of unrelated coefficient functions does not, by itself, establish them.

**Lemma 4.1 (Mellin finite part and transgression).** If \(g\) is holomorphic near zero, then

\[

\Phi_g=\operatorname*{Res}_{z=0}g(z)C(z)

=g(0)c(1)-d\,\operatorname{FP}_{z=0}\bigl(g(z)J(z)\bigr).

\tag{4.3}

\]

Here \(\operatorname{FP}\) means the coefficient of \(z^0\). In particular, \(d\Phi_g=0\). If \(g(0)=1\), then \(\Phi_g\) and \(c(1)\) represent the same cohomology class.

**Proof.** In an initial half-plane, the growth bounds imply \(t^zc(t)\to0\) as \(t\downarrow0\). Integration by parts and (4.1) give

\[

c(1)-zC(z)

=\int_0^1t^zc'(t)\,dt=dJ(z).

\tag{4.4}

\]

The equality continues meromorphically because both sides do. Multiply it by \(g(z)\) and take its constant Laurent coefficient. The constant coefficient of \(zg(z)C(z)\) is the residue of \(g(z)C(z)\); the constant coefficient of \(g(z)c(1)\) is \(g(0)c(1)\). Continuity of \(d\) allows it to be applied to each Laurent coefficient of \(J\). This yields (4.3). Applying \(d\), and using \(dc(1)=0\) and \(d^2=0\), proves closedness. The displayed difference is an actual coboundary in the stipulated complex. \(\square\)

To connect this lemma with a heat expansion, suppose, in the same cochain topology, that

\[

c(t)=\sum_{\alpha,\ell}c_{\alpha,\ell}

t^\alpha(\log t)^\ell+O(t^\epsilon),

\qquad \epsilon>0,

\tag{4.5}

\]

with a finite sum. Exponents with positive real part may be absorbed into the remainder after reducing \(\epsilon\); exponents on the imaginary axis are retained. The Mellin integral of a summand is

\[

\int_0^1t^{z+\alpha-1}(\log t)^\ell\,dt

=\frac{(-1)^\ell\ell!}{(z+\alpha)^{\ell+1}},

\tag{4.6}

\]

initially where \(\operatorname{Re}(z+\alpha)>0\), then meromorphically. The remainder contributes a function holomorphic for \(\operatorname{Re}z>-\epsilon\). Thus

\(\operatorname*{Res}_{z=0}C(z)=c_{0,0}\).

Terms with \(\alpha\neq0\) have no pole at zero. Terms with \(\alpha=0,\ell>0\) have a higher pole and no residue by themselves; multiplication by \(g\) can make them contribute.

Consequently, taking the constant term of a heat expansion preserves a class only after the transgression and its meromorphic primitive have been justified. Equality of pairings with a selection of cycles is a weaker statement unless an appropriate separation theorem has also been supplied.

## 5. Computing the coefficients without ambiguity

Write

\[

\beta_k=(k_1+1)(k_1+k_2+2)\cdots(|k|+n),

\qquad

A_{n,k}=\frac{(-1)^{|k|}}{k_1!\cdots k_n!\,\beta_k}.

\tag{5.1}

\]

The factorials and the successive partial sums have different origins. A Taylor expansion of each heat conjugation supplies \(1/k_j!\); integration over the simplex supplies \(1/\beta_k\).

**Lemma 5.1 (the simplex coefficient).** For \(k_j\geq0\),

\[

\int_{\substack{v_j\geq0\\v_0+\cdots+v_n=1}}

v_0^{k_1}(v_0+v_1)^{k_2}\cdots

(v_0+\cdots+v_{n-1})^{k_n}\,dv

=\beta_k^{-1}.

\tag{5.2}

\]

We use \(dv=dv_0\cdots dv_{n-1}\), with \(v_n=1-\sum_{j<n}v_j\).

**Proof.** Set \(x_j=v_0+\cdots+v_{j-1}\), \(1\leq j\leq n\). The transformation is triangular with determinant one, and its image is \(0\leq x_1\leq\cdots\leq x_n\leq1\). Integrating \(x_1\) first gives \(x_2^{k_1+1}/(k_1+1)\). The next integration gives the additional denominator \(k_1+k_2+2\). Continuing, the last integration gives \(|k|+n\). Their product is \(\beta_k\). \(\square\)

For \(T=T_{n,k}\) in (3.1), abbreviate

\[

h_T(z)=\operatorname{Tr}(T\Lambda^{-2z}),\qquad

\tau_q(T)=\operatorname*{Res}_{z=0}z^q h_T(z),

\quad q\geq0.

\tag{5.3}

\]

Here \(\Lambda=|D|\) in the invertible case. If \(h_T\) has pole order at most \(r\), its principal part is

\(\sum_{q=0}^{r-1}\tau_q(T)z^{-q-1}\).

For a holomorphic function \(f\), ordinary multiplication of Laurent and Taylor series gives

\[

\operatorname*{Res}_{z=0}f(z)h_T(z)

=\sum_{q=0}^{r-1}\frac{f^{(q)}(0)}{q!}\tau_q(T).

\tag{5.4}

\]

This formula contains a Taylor factorial. Once \(f\) has been written as a polynomial \(\sum f_qz^q\), its Taylor coefficient is already \(f_q\), and no additional division by \(q!\) is made.

For odd \(n\), the unrenormalized expression associated with the heat calculation is

\[

\Phi_n(a^0,\ldots,a^n)

=\sqrt{2i}\sum_k A_{n,k}\,

\operatorname*{Res}_{z=0}

\Gamma\left(|k|+\frac n2+z\right)h_{T_{n,k}}(z).

\tag{5.5}

\]

Equation (5.4) expands this into

\(\Gamma^{(q)}(|k|+n/2)\tau_q/q!\).

Only \(n+|k|\leq p\) can contribute, by Section 3; finite pole order bounds the remaining \(q\)-sum.

The next proposition establishes the coefficient conversion. It does not assume that a formal operator expression is already a cocycle. Its cohomological conclusion uses precisely the analytic transgression hypotheses of Lemma 4.1.

**Proposition 5.2 (odd coefficient conversion).** Let

\[

m=|k|+\frac{n-1}{2},\qquad

P_m(z)=\prod_{\ell=0}^{m-1}\left(z+\ell+\frac12\right)

=\sum_{q=0}^m p_{m,q}z^q,

\quad P_0=1.

\tag{5.6}

\]

Multiplying the meromorphic expression in (5.5) by

\(g_{\mathrm{odd}}(z)=\Gamma(1/2)/\Gamma(1/2+z)\)

converts it to

\[

\Phi'_n(a^0,\ldots,a^n)

=\sqrt{2\pi i}

\sum_{\substack{k:\,n+|k|\leq p\\0\leq q\leq m}}

A_{n,k}\,p_{m,q}\,\tau_q(T_{n,k}).

\tag{5.7}

\]

All \(A_{n,k}p_{m,q}\) are rational. If the unrenormalized family is obtained as \(\operatorname{Res}C(z)\) from a cochain homotopy satisfying Lemma 4.1, the renormalized family represents the same class.

**Proof.** The gamma recurrence, applied \(m\) times, gives

\[

\frac{\Gamma(m+1/2+z)}{\Gamma(1/2+z)}=P_m(z).

\tag{5.8}

\]

Hence \(g_{\mathrm{odd}}(z)\Gamma(|k|+n/2+z)=\sqrt\pi P_m(z)\). Taking its residue against \(h_T\) gives exactly

\(\sqrt\pi\sum_{q=0}^mp_{m,q}\tau_q(T)\),

by direct coefficient multiplication. Every half-integer in \(P_m\) is rational, proving rationality. The gamma function is holomorphic and nonzero at \(1/2\), so \(g_{\mathrm{odd}}\) is holomorphic near zero and \(g_{\mathrm{odd}}(0)=1\). Lemma 4.1 proves the conditional class statement. \(\square\)

The bound on Laurent coefficients is now independent of pole multiplicity: \(q\leq m\). For example, for integer \(p\geq1\),

\(m\leq p-(n+1)/2\leq p-1\).

Even if a coefficient zeta function has a larger pole order, (5.7) uses none of the coefficients with \(q>m\).

Here are three exact checks. In degree one with \(k=0\), the coefficient is simply \(\tau_0(a^0da^1\Lambda^{-1})\). In degree one with \(k=1\), \(A_{1,(1)}=-1/2\) and \(P_1(z)=z+1/2\), so the contribution, after removal of the common factor \(\sqrt{2\pi i}\), is

\[

-\frac14\tau_0\bigl(a^0\nabla(da^1)\Lambda^{-3}\bigr)

-\frac12\tau_1\bigl(a^0\nabla(da^1)\Lambda^{-3}\bigr).

\tag{5.9}

\]

In degree three with \(k=(0,0,0)\), \(A_{3,0}=1/6\) and \(m=1\). That contribution is

\[

\frac1{12}\tau_0\bigl(a^0da^1da^2da^3\Lambda^{-3}\bigr)

+\frac16\tau_1\bigl(a^0da^1da^2da^3\Lambda^{-3}\bigr).

\tag{5.10}

\]

These values follow from (5.1) and (5.6) separately; neither a simplex denominator nor a polynomial coefficient can be discarded.

For an even triple, let \(\gamma=\gamma^*=\gamma^{-1}\) commute with \(A\) and anticommute with \(D\). Put

\(h_T^\gamma(z)=\operatorname{Tr}(\gamma T\Lambda^{-2z})\),

and use \(\tau_q^\gamma(T)\) for its Laurent coefficients. This notation keeps the grading inside the trace.

**Proposition 5.3 (even coefficient conversion).** For even \(n\geq2\), set \(\ell=|k|+n/2\) and

\[

Q_{\ell-1}(z)=\prod_{j=1}^{\ell-1}(z+j)

=\sum_{q=0}^{\ell-1}e_{\ell-1,q}z^q,

\quad Q_0=1.

\tag{5.11}

\]

Replacing the gamma factor by

\(g_{\mathrm{even}}(z)\Gamma(\ell+z)\), where

\(g_{\mathrm{even}}(z)=1/\Gamma(1+z)\), yields

\[

\Phi'_n(a^0,\ldots,a^n)

=\sum_{\substack{k:\,n+|k|\leq p\\0\leq q\leq\ell-1}}

A_{n,k}e_{\ell-1,q}\tau_q^\gamma(T_{n,k}).

\tag{5.12}

\]

In degree zero, the same conversion turns

\(\operatorname{Res}_{z=0}\Gamma(z)h_a^\gamma(z)\)

into the constant coefficient of \(h_a^\gamma\):

\[

\Phi'_0(a)=\operatorname{FP}_{z=0}h_a^\gamma(z)

=\tau_{-1}^\gamma(a).

\tag{5.13}

\]

Again, the converted family preserves the class whenever the cochain homotopy hypotheses of Lemma 4.1 hold.

**Proof.** The gamma recurrence gives

\(\Gamma(\ell+z)/\Gamma(1+z)=Q_{\ell-1}(z)\).

Multiply this polynomial by the Laurent expansion of \(h_T^\gamma\) to obtain (5.12). For degree zero,

\(\Gamma(z)/\Gamma(1+z)=1/z\); the residue of \(h_a^\gamma(z)/z\) is its constant coefficient, even when \(h_a^\gamma\) itself has poles. Finally \(g_{\mathrm{even}}(0)=1\), so Lemma 4.1 applies to the cohomological assertion. \(\square\)

An invertible reference operator is convenient for these computations. When \(D\) has a kernel, its finite-dimensional contribution must be retained explicitly in the degree-zero character. Replacing the zero eigenvalues by one makes complex powers meaningful, but that replacement alone is not a proof that a complete even pairing has been preserved.

The propositions determine the coefficients and the analytic conditions under which renormalization preserves a class. Sections 6–7 prove the actual cyclic identity using heat cochains and controlled remainders. Section 8 constructs a finite heat cocycle and its transgression. Identifying its class with the Fredholm character also requires the bounded-phase comparison and the Chern-cycle pairing. The circle computation in Section 2 proves that identification directly in one example.

## 6. Cyclic differentials and heat cochains

Let \(A\) be a unital complex algebra, and put \(\bar A=A/\mathbb C1\). A normalized cochain of degree \(n\) is a multilinear functional on

\(A\otimes\bar A^{\otimes n}\). Thus it vanishes when an argument after the first is \(1\). Our differentials are

\[

\begin{aligned}

(b\phi_n)(a^0,\ldots,a^{n+1})

={}&\sum_{j=0}^{n}(-1)^j

\phi_n(a^0,\ldots,a^ja^{j+1},\ldots,a^{n+1})\\

&+(-1)^{n+1}\phi_n(a^{n+1}a^0,a^1,\ldots,a^n),\\

(B\phi_{n+1})(a^0,\ldots,a^n)

={}&\sum_{j=0}^{n}(-1)^{nj}

\phi_{n+1}(1,a^j,\ldots,a^n,a^0,\ldots,a^{j-1}).

\end{aligned}

\tag{6.1}

\]

The cochain complex used here has finite collections of a fixed parity. Its closedness condition is \(b\phi_n+B\phi_{n+2}=0\) in every degree, with missing components zero.

The unnormalized face and rotation relations used here are established in Higher traces, Proposition 1.1 and Lemma 6.1. Its cyclic resolution and unit contraction are given in Sections 6–9 of that lesson. We use those foundations and recall the tensor calculation to fix the signs and the internal-unit quotient needed for our heat cochains.

**Lemma 6.1 (the two differentials).** The operators in (6.1) satisfy

\[

b^2=B^2=bB+Bb=0.

\tag{6.2}

\]

**Proof.** It is useful to verify the transposed formulas on tensors. Work first on \(A^{\otimes(n+1)}\). Let \(b'\) merge adjacent entries with alternating signs, omitting the final cyclic merge in \(b\). Let

\[

t_n(a^0,\ldots,a^n)=(-1)^n(a^n,a^0,\ldots,a^{n-1}),

\quad N_n=1+t_n+\cdots+t_n^n,

\]

and let \(s\) prepend \(1\). Expanding the tensors gives

\[

\begin{gathered}

b(1-t)=(1-t)b',\qquad b'N=Nb,\\

b's+sb'=1,\qquad N(1-t)=(1-t)N=0.

\end{gathered}

\tag{6.3}

\]

For the first identity, all interior merges occur once on each side with the same sign; the two endpoint merges are exactly the cyclic difference. For the second, rotate each merged pair through the tensor: the omitted endpoint merge becomes the last merge in the next rotation. These exhaust the \(n+1\) rotations. For the third, the merge of the prepended \(1\) returns the original tensor; every other merge cancels the corresponding prepended term with its opposite sign. The final identity is the geometric sum and \(t_n^{n+1}=1\).

The tensor operator \(B=(1-t)sN\) therefore has square zero. Also

\[

bB+Bb=(1-t)(b's+sb')N=(1-t)N=0.

\]

For \(b^2=0\), two mergers of disjoint pairs cancel in the two possible orders. Two mergers of an overlapping triple cancel by associativity. The same cancellation includes a pair crossing the last and first entries.

Now quotient by tensors with \(1\) in a slot after the first. The operator \(b\) preserves that subspace: the two mergers adjoining such a slot cancel; the other mergers retain the slot. In \(B\), the part \(tsN\) has \(1\) in the second slot and vanishes in the quotient. The surviving \(sN\) gives exactly the second formula of (6.1), after transposition. These formulas are well defined on the quotient: if an input already has an internal \(1\), every surviving \(sN\) term still has one. Thus the identities descend and give (6.2). \(\square\)

The finite cochains pair naturally with infinite normalized chains, because only finitely many components are evaluated. This determines the factorials in a Chern cycle.

**Proposition 6.2 (Chern cycles with fixed signs).** For a unitary \(U\), the odd chain

\[

c_{2j+1}(U)=(-1)^j j!\,

(U^{-1},U,U^{-1},U,\ldots,U^{-1},U)

\tag{6.4}

\]

has \(2j+2\) entries and satisfies \(bc_{2j+3}+Bc_{2j+1}=0\). For an idempotent \(e\), an even cycle is

\[

c_0(e)=e,\qquad

c_{2j}(e)=\frac{(-1)^j(2j)!}{j!}

(e-\tfrac12,e,\ldots,e),\quad j\geq1.

\tag{6.5}

\]

Matrix-valued cycles use the matrix trace on tensors, contracting cyclically all consecutive matrix indices.

**Proof.** Write \(w_{2j+1}\) for the alternating tensor in (6.4). Every interior merger in \(bw_{2j+1}\) creates an internal \(1\) and vanishes. Only the first and last mergers remain, with opposite signs. Write their difference as \(v_{2j}\). Rotation in \(Bw_{2j+1}\) gives \(j+1\) copies of each of the two alternating tensors with initial \(1\), so

\[

bw_{2j+3}=v_{2j+2},\qquad

Bw_{2j+1}=(j+1)v_{2j+2}.

\]

The coefficient at degree \(2j+3\) is minus \(j+1\) times the coefficient at degree \(2j+1\), proving the odd cycle identity.

For \(w_{2j}=(e-\tfrac12,e,\ldots,e)\), the two endpoint mergers give one copy of \((e,e,\ldots,e)\), since \((e-\tfrac12)e=e/2\). The interior alternating mergers give minus \((e-\tfrac12,e,\ldots,e)\). Hence

\[

bw_{2j}=\tfrac12(1,e,\ldots,e).

\]

In \(Bw_{2j}\), the entry \(e-\tfrac12\) is internal after prepending \(1\), so its class is the class of \(e\). All \(2j+1\) rotations are the same tensor. Thus

\(Bw_{2j}=(2j+1)(1,e,\ldots,e)\).

The successive coefficients in (6.5) have ratio \(-2(2j+1)\), proving every positive-degree identity. At the bottom, \(Bc_0=(1,e)\) and \(bc_2=-(1,e)\). Matrix contraction respects multiplication and rotation, so the same calculation applies to matrices. \(\square\)

Formula (6.4) defines the algebraic cycle for \(U\). With the positive compression convention of Section 2, its circle residue evaluation, divided by \(\sqrt{2\pi i}\), is the negative of the index. Equivalently one can evaluate the cycle for \(U^{-1}\). A general index pairing must retain this orientation.

We next construct cochains from a regular spectral triple with trace-class heat operators. In the even case use the supertrace

\(\operatorname{Str}(T)=\operatorname{Tr}(\gamma T)\).

In the odd case adjoin a formal odd symbol \(\epsilon\), \(\epsilon^2=1\), put

\(\mathcal D=D\epsilon\), and define

\[

\operatorname{Str}_\epsilon(T\epsilon)=\operatorname{Tr}(T),

\qquad \operatorname{Str}_\epsilon(T)=0.

\tag{6.6}

\]

The original operators have degree zero in this extension. This functional is a graded trace on trace-class products: if the product is odd exactly one of two homogeneous factors is odd, so ordinary trace cyclicity gives the required sign \(+1\); if the product is even both sides vanish. In the even case put \(\mathcal D=D\). In both cases \(\mathcal D^2=D^2\), and the algebra elements are even.

For homogeneous factors define the heat bracket

\[

\langle A_0,\ldots,A_n\rangle_u

=\int_{\Delta_n}\operatorname{Str}

\bigl(A_0e^{-uv_0D^2}A_1e^{-uv_1D^2}

\cdots A_ne^{-uv_nD^2}\bigr)\,dv,

\tag{6.7}

\]

where \(\Delta_n=\{v_j\geq0:\sum v_j=1\}\), with the measure in Lemma 5.1. The odd case uses \(\operatorname{Str}_\epsilon\).

For bounded \(A_j\), the integral is well defined. Schatten Hölder gives

\[

\left|\langle A_0,\ldots,A_n\rangle_u\right|

\leq\frac1{n!}\operatorname{Tr}(e^{-uD^2})

\prod_{j=0}^n\|A_j\|.

\tag{6.8}

\]

Indeed \(\|e^{-uv_jD^2}\|_{1/v_j}

=\operatorname{Tr}(e^{-uD^2})^{v_j}\) when \(v_j>0\); a zero \(v_j\) contributes the identity with norm one. The simplex has volume \(1/n!\). The trace estimate holds for both supertraces.

**Theorem 6.3 (the heat cocycle).** Let \(d_{\mathcal D}a=[\mathcal D,a]\), and set

\[

H_n(u)(a^0,\ldots,a^n)

=\kappa u^{n/2}

\langle a^0,d_{\mathcal D}a^1,\ldots,d_{\mathcal D}a^n\rangle_u,

\quad

\kappa=

\begin{cases}1&\text{even},\\ \sqrt{2i}&\text{odd}.\end{cases}

\tag{6.9}

\]

The complex square root in the odd normalization has its principal value.

Keep even \(n\) in the even case and odd \(n\) in the odd case. Then

\[

bH_{n-1}(u)+BH_{n+1}(u)=0.

\tag{6.10}

\]

Each component is normalized.

**Proof.** Absorb the powers of \(u^{1/2}\) into \(\Omega=u^{1/2}\mathcal D\), so its differential is \(d_\Omega\) and its square is \(uD^2\). Three bracket identities give the calculation.

First, cyclic rotation has the sign obtained by moving one homogeneous factor past all the others; this follows from the graded trace and a rotation of the simplex coordinates. Second,

\[

\sum_{j=0}^n

\langle A_0,\ldots,A_j,1,A_{j+1},\ldots,A_n\rangle

=\langle A_0,\ldots,A_n\rangle.

\tag{6.11}

\]

Inserting \(1\) splits one heat interval. Integrating over its split gives its original length \(v_j\); summing those lengths gives one.

Third, a bracket containing \([\Omega^2,a]\) is the difference of its two collapsed neighboring intervals. To check this, hold their total length \(w\) fixed and differentiate

\[

e^{-s\Omega^2}a e^{-(w-s)\Omega^2}

\]

with respect to \(s\). Its derivative is minus the same expression with \([\Omega^2,a]\) in place of \(a\). The integrated endpoints put \(a\) next to its left neighbor and next to its right neighbor. At the cyclic endpoint use the first identity.

Expand \(bH_{n-1}\) by (6.1) and \(d_\Omega(ab)=d_\Omega(a)b+a\,d_\Omega(b)\). The adjacent product terms cancel except their differences across a heat interval. The third identity gives the exact remaining expression, after suppressing \(\kappa\):

\[

bH_{n-1}

=\sum_{j=1}^n(-1)^{j-1}

\langle a^0,d_\Omega a^1,\ldots,

[\Omega^2,a^j],\ldots,d_\Omega a^n\rangle.

\tag{6.12}

\]

The graded trace of the graded commutator with \(\Omega\) vanishes. Since \(\Omega\) commutes with its heat factors, applying this assertion to the bracket gives

\[

0=\langle d_\Omega a^0,d_\Omega a^1,\ldots,d_\Omega a^n\rangle

+\sum_{j=1}^n(-1)^{j-1}

\langle a^0,\ldots,[\Omega^2,a^j],\ldots,d_\Omega a^n\rangle.

\tag{6.13}

\]

Here the identity

\([\Omega,d_\Omega a]_{\mathrm{graded}}=[\Omega^2,a]\)

accounts for the middle entries.

Finally, \(BH_{n+1}\) is the sum of the cyclic rotations of

\(\langle1,d_\Omega a^0,\ldots,d_\Omega a^n\rangle\).

Rotating \(j\) odd differential entries contributes

\((-1)^{j(n+1-j)}\). Multiplying by \((-1)^{nj}\) from (6.1) gives sign \(+1\), since \(j(1-j)\) is even. Thus it is exactly the sum of all insertions of \(1\) in the differential bracket. Equation (6.11) identifies it with the first term of (6.13). Together with (6.12), this proves (6.10).

All uses of the unbounded \(\Omega\) can first be made on its common smooth domain with positive heat intervals. The spectral graph-scale bounds from the second lesson control each differentiated factor. Spectral cutoffs give finite-matrix approximations, and their products and commutators converge in the heat trace norm by (6.8) and the order estimates in Lemma 7.1 below. The boundary brackets obey the same estimates, so the identities extend to the simplex boundary. A differential of \(1\) is zero, proving normalization. \(\square\)

## 7. Extracting an actual residue cocycle

Assume \(\mu_j(|D|^{-1})=O((j+1)^{-1/p})\), with \(p>0\), and that the coefficient zeta functions have meromorphic continuation with finite pole multiplicity near zero. The isolated-singularity definition in the second lesson is broader; its additional finite-pole condition is needed here. Regularity supplies every commutator used below. All assertions in this section use the invertible \(D\).

The coefficient family includes the actual \(a,[D,a]\) and their regular commutators; in the even case it includes the traces with the grading inserted. The cyclic identities can be read in algebraic multilinear cochains, where continuation is required after every evaluation. For continuous cyclic cochains on a chosen regularity completion of \(A\), require in addition that the coefficient continuations and their Laurent coefficients are continuous multilinear forms, locally bounded in its seminorms. The following proof is valid in either setting. The heat integrals and remainders have the latter bounds by their explicit estimates; scalar continuation alone does not imply them for the zeta coefficients.

The heat trace satisfies

\[

\operatorname{Tr}(|D|^h e^{-uD^2})

\leq C_h u^{-(p+h)/2},\qquad h\geq0,\quad0<u\leq1.

\tag{7.1}

\]

To prove it, singular-value summability bounds the count of absolute eigenvalues below \(R\) by \(CR^p\). Partition that spectrum into the interval below \(u^{-1/2}\) and the dyadic intervals above it. The first count contributes \(Cu^{-(p+h)/2}\). The successive contributions are bounded by that quantity times

\(C2^{j(p+h)}e^{-c4^j}\), a summable sequence. The finitely many small eigenvalues are absorbed in the same bound.

**Lemma 7.1 (the differentiated heat expansion).** For fixed \(n\geq1\), each integer \(N\geq1\) gives

\[

\begin{aligned}

H_n(u)

={}&\kappa\sum_{|k|<N}

A_{n,k}\,u^{n/2+|k|}

\operatorname{Str}\bigl(

a^0\nabla^{k_1}(d_{\mathcal D}a^1)\cdots

\nabla^{k_n}(d_{\mathcal D}a^n)e^{-uD^2}\bigr)\\

&+R_{n,N}(u),

\qquad

|R_{n,N}(u)|\leq C u^{(n+N-p)/2}.

\end{aligned}

\tag{7.2}

\]

The bound is uniform on bounded sets for finitely many of the regularity seminorms. Parameter derivatives may also be taken under the Mellin remainder integral in any half-plane where this bound is integrable.

**Proof.** For a smooth order-zero coefficient \(B\), the exact heat commutation formula is

\[

\begin{aligned}

e^{-sD^2}B

={}&\sum_{k=0}^{N-1}\frac{(-s)^k}{k!}

\nabla^k(B)e^{-sD^2}\\

&+\frac{(-1)^N}{(N-1)!}

\int_0^s(s-v)^{N-1}

e^{-vD^2}\nabla^N(B)e^{-(s-v)D^2}\,dv.

\end{aligned}

\tag{7.3}

\]

Differentiate the heat-conjugated product on the smooth domain and integrate its Taylor remainder to prove this identity. Equivalently, in a spectral basis its matrix entry is the ordinary Taylor formula for

\(e^{-s(\lambda^2-\mu^2)}\), multiplied by \(e^{-s\mu^2}\). The graph-scale bounds extend the equality to the spaces on which its terms act.

Commute the heat factors in (6.7) successively to the right. The heat interval crossing \(d_{\mathcal D}a^j\) has total length \(u(v_0+\cdots+v_{j-1})\). Therefore its Taylor term gives

\[

\frac{(-u)^{k_j}}{k_j!}

(v_0+\cdots+v_{j-1})^{k_j}.

\]

The simplex integral is (5.2); its product of coefficients is precisely \(A_{n,k}\).

We justify the error uniformly including the simplex boundary. A product of coefficients of orders \(h_i\geq0\), separated by heat intervals whose total length is \(u\), has trace norm at most

\[

C u^{-(p+\sum h_i)/2}.

\tag{7.4}

\]

There is an interval of length at least \(u/L\), where \(L\) is the number of intervals. Split the original product at that heat factor as \(T_L e^{-uvD^2}T_R\). The two remaining products have orders \(h_L,h_R\) summing to \(\sum h_i\), uniformly in the other interval lengths: each heat operator has norm at most one on every spectral Sobolev space, and each coefficient has the stated graph-space bound. Thus \(T_L|D|^{-h_L}\) and \(|D|^{-h_R}T_R\) are bounded, and the original product factors as

\[

(T_L|D|^{-h_L})\,

|D|^{h_L+h_R}e^{-uvD^2}\,

(|D|^{-h_R}T_R).

\]

Equation (7.1) bounds the trace norm of its middle factor. This proves (7.4) without dividing by a possibly zero interval length, and proves trace-class membership before any cyclic interchange.

For a remainder of total Taylor length \(K\), the integration in (7.3) and the finite Taylor factors contribute \(u^K\). The coefficients have total order at most \(K\), because \(\nabla^k(B)\) has order at most \(k\). Multiplication by the prefactor \(u^{n/2}\) and (7.4) therefore give

\(Cu^{(n+K-p)/2}\).

Expand each crossing to length \(N\), keep total length below \(N\), and bound every remaining finite term and integral remainder this way. Each has \(K\geq N\), proving (7.2).

Only finitely many graph-space seminorms occur in this construction, giving the asserted uniformity. In a Mellin derivative the factor \((\log u)^r\) is integrable whenever the real exponent has a strict margin. This proves the last assertion. \(\square\)

**Theorem 7.2 (the residue cocycle identity).** Under these hypotheses, the odd formula (5.5) is an actual finite normalized \((b,B)\)-cocycle. Multiplication by \(g_{\mathrm{odd}}\) gives the actual cocycle (5.7). In the even case, the components (5.12) together with (5.13) are an actual finite normalized \((b,B)\)-cocycle. These conclusions assert closedness; the Chern-character class requires the additional comparison discussed in Section 8.

**Proof.** Initially for sufficiently large \(\operatorname{Re}z\), define each component

\[

C_n(z)=\int_0^\infty u^{z-1}H_n(u)\,du.

\tag{7.5}

\]

The small-\(u\) integral converges by (6.8) and (7.1); the large-\(u\) integral converges because \(D\) has a positive spectral gap. The cocycle identity of Theorem 6.3 passes through the integral:

\[

bC_{n-1}(z)+BC_{n+1}(z)=0.

\tag{7.6}

\]

For any fixed \(n\) choose \(N\) so that \(n+N>p\). Lemma 7.1 makes the small-\(u\) remainder integral holomorphic near zero. Its parameter derivatives are controlled there. The finite expansion and the scalar spectral Mellin formula show that, modulo a holomorphic cochain,

\[

C_n(z)=\kappa\sum_{|k|<N}A_{n,k}

\Gamma\left(\frac n2+|k|+z\right)

\operatorname{Str}\bigl(T_{n,k}|D|^{-2z}\bigr).

\tag{7.7}

\]

For this equation, the Clifford factors are retained in \(T_{n,k}\) in the odd case. The supertrace then reduces to the ordinary trace when \(n\) is odd. To verify the formula, first integrate a term over \(0<u<\infty\) in its trace-class half-plane. Scalar integration against each positive eigenvalue gives the indicated gamma factor. Subtracting its integral over \(u\geq1\) changes it by an entire function. Thus (7.7) is exactly the continuation of (7.5), with a holomorphic remainder near zero.

The coefficient functions continue meromorphically by the arbitrary-order zeta theorem in the second lesson. Therefore (7.6) continues as an identity of meromorphic cochains. Taking the residue at zero gives closedness. Taking instead \(\operatorname{Res}_{z=0}g(z)C_n(z)\), with one fixed holomorphic scalar \(g\) in every degree, also gives closedness.

If \(n>p\), the unexpanded small-\(u\) estimate \(H_n(u)=O(u^{(n-p)/2})\) already makes \(C_n\) holomorphic at zero. Its residue, also after multiplication by \(g\), is zero. Within the remaining degrees, the terms with \(n+|k|>p\) are holomorphic by Section 3. Hence the resulting collection is finite and satisfies (7.6) even at its highest degree.

In the even degree zero,

\[

C_0(z)=\Gamma(z)\operatorname{Tr}(\gamma a^0|D|^{-2z}).

\tag{7.8}

\]

The conversion \(g_{\mathrm{even}}(z)=1/\Gamma(1+z)\) turns it into \(h_{a^0}^\gamma(z)/z\), so its residue is the constant Laurent coefficient in (5.13). All other coefficients are exactly the conversions in Propositions 5.2–5.3. Their normalized character follows directly from (6.9). \(\square\)

The theorem proves the cocycle condition even with higher poles. The genuine trace and simplex identities were used before continuation, and the Laurent residue was taken only afterward.

**Corollary 7.3 (the harmonic contribution).** Suppose \(D\) has compact resolvent but may have a kernel. Put \(P_0=\operatorname{proj}_{\ker D}\) and

\[

\Lambda=(D^2+P_0)^{1/2}=|D|+P_0.

\tag{7.9}

\]

Use this \(\Lambda\) in every inverse power and coefficient zeta function, with the same regularity and finite-pole hypotheses. The cocycle conclusion of Theorem 7.2 still holds. In the even case its degree-zero component is

\[

\Phi'_0(a)=\operatorname{FP}_{z=0}

\operatorname{Tr}(\gamma a\Lambda^{-2z}).

\tag{7.10}

\]

Thus the harmonic contribution is included. If the inverse is instead made zero on the kernel, one must add \(\operatorname{Tr}(\gamma aP_0)\) to that degree-zero value.

**Proof.** The heat cocycle of Theorem 6.3 continues to use \(D\) and \(e^{-uD^2}\); no inverse or spectral gap enters its identities at a positive \(u\). Define its Mellin cochains over \(0<u<1\), which suffices for residues near zero.

Replace the heat factors in this calculation by \(e^{-u\Lambda^2}\). Their difference is exactly

\[

e^{-uvD^2}-e^{-uv\Lambda^2}

=(1-e^{-uv})P_0.

\tag{7.11}

\]

A telescoping product expansion therefore makes the trace difference of the brackets \(O(u)\), uniformly on the simplex: the inserted projection has finite rank and norm at most \(u\), while all other coefficients and heat factors are bounded. After the prefactor \(u^{n/2}\), the difference is \(O(u^{n/2+1})\). Its Mellin integral is holomorphic near zero. Although the brackets formed from \(\Lambda^2\) alone need not be heat cocycles for \(D\), their Mellin residues coincide with those of the genuine heat cocycle.

Expand the new brackets by Lemma 7.1 with derivation

\([\Lambda^2,\cdot]=\nabla+[P_0,\cdot]\).

Every correction involving the last commutator is finite rank and smoothing in all spectral Sobolev scales. Indeed a regular coefficient and its adjoint preserve all those scales; the finite-dimensional kernel is in their intersection. The vectors in \(aP_0\), \(a^*P_0\), and their differential iterates are consequently smooth in that scale. This proves the same assertion for every correction after repeated commutation and multiplication.

For positive \(n\), such smoothing coefficient terms give entire zeta functions. Their gamma factors \(\Gamma(n/2+|k|+z)\) are holomorphic at zero, so their residues vanish, also after either gamma conversion. Hence the remaining positive-degree terms are exactly the formulas using \(\nabla=[D^2,\cdot]\) and the completed \(\Lambda\).

In degree zero the Mellin formula for the replaced heat operator is

\(\Gamma(z)\operatorname{Tr}(\gamma a\Lambda^{-2z})\), up to its entire tail from \(u\geq1\). Its gamma conversion gives (7.10). Completing or removing the kernel changes the coefficient zeta function by the entire constant \(\operatorname{Tr}(\gamma aP_0)\), proving the final statement. Taking residues of the original heat cocycle proves closedness throughout. \(\square\)

## 8. Finite heat homotopies

The entire heat collection has infinitely many degrees, while a finitely summable Fredholm character lives in a finite cyclic complex. A truncation requires a correction at its last degree.

Put \(\Omega_t=t\mathcal D\), \(t>0\), and write

\(H_n(t)=H_n(t^2)\) in this section. Its brackets now use the heat operator \(e^{-v\Omega_t^2}\). Define the insertion cochain

\[

\Psi_n(t)=\kappa\sum_{j=0}^n(-1)^j

\langle a^0,d_{\Omega_t}a^1,\ldots,d_{\Omega_t}a^j,

\dot\Omega_t,d_{\Omega_t}a^{j+1},\ldots,d_{\Omega_t}a^n\rangle.

\tag{8.1}

\]

It has the parity opposite to the heat collection. Here \(\dot\Omega_t=\mathcal D\).

**Lemma 8.1 (differentiating the heat cocycle).** These cochains satisfy

\[

\frac d{dt}H_n(t)=-b\Psi_{n-1}(t)-B\Psi_{n+1}(t).

\tag{8.2}

\]

For \(0<t\leq1\), their values obey

\[

|\Psi_n(t)|\leq C_n t^{n-p-1};

\tag{8.3}

\]

for \(t\geq1\) they decrease exponentially, up to a fixed polynomial, for each fixed degree.

**Proof.** Differentiating a heat factor uses the exact Duhamel formula

\[

\frac d{dt}e^{-v\Omega_t^2}

=-\int_0^v e^{-s\Omega_t^2}

(\Omega_t\dot\Omega_t+\dot\Omega_t\Omega_t)

e^{-(v-s)\Omega_t^2}\,ds.

\tag{8.4}

\]

Differentiating a differential factor gives

\([\,\dot\Omega_t,a^j\,]\).

These are all the terms in the derivative.

Expand \(b\Psi_{n-1}\) with the Leibniz rule and the neighboring-interval calculation of (6.12). The product mergers next to the inserted \(\dot\Omega_t\) leave precisely minus the derivative terms \([\dot\Omega_t,a^j]\). The other mergers give brackets with \([\Omega_t^2,a^j]\) and the same alternating insertion signs.

To evaluate \(B\Psi_{n+1}\), rotate the differential arguments as in the proof of (6.13), preserving the position of \(\dot\Omega_t\). Apply the graded commutator with \(\Omega_t\) to each rotated bracket. The terms differentiating the differential arguments are the brackets with \([\Omega_t^2,a^j]\) just obtained; their signs are opposite. The terms hitting the insertion are

\(\Omega_t\dot\Omega_t+\dot\Omega_t\Omega_t\).

After the insertion-of-\(1\) identity (6.11), they split every original heat interval once and exhaust the integrals in (8.4). Thus the sum \(b\Psi_{n-1}+B\Psi_{n+1}\) is exactly minus the derivative. This proves (8.2), with both types of derivative and every insertion position included. At degree zero it reads \(H'_0=-B\Psi_1\), which also follows directly from (8.4).

There are \(n\) bounded differential factors, each contributing \(t\), and one insertion of order one. Bound a bracket containing that insertion by (7.4), with total order one and heat length \(t^2\). Its bound is \(Ct^{-p-1}\). This proves (8.3). At infinity split off a fixed positive fraction of the largest heat interval; the spectral gap supplies exponential decay and controls the insertion. These estimates also justify the differentiations and spectral-cutoff limits in (8.2). \(\square\)

Choose an integer \(N\) of the heat parity, with \(N>p\). Define a finite cochain \(\chi^{(N)}(t)\) by

\[

\begin{aligned}

\chi_n^{(N)}(t)&=H_n(t),&&n<N,\\

\chi_N^{(N)}(t)&=H_N(t)+B\int_0^t\Psi_{N+1}(s)\,ds,\\

\chi_n^{(N)}(t)&=0,&&n>N.

\end{aligned}

\tag{8.5}

\]

The integral converges by (8.3).

**Proposition 8.2 (a finite heat cocycle).** The cochain in (8.5) is closed. For \(0<t_0<t_1\),

\[

\chi^{(N)}(t_1)-\chi^{(N)}(t_0)

=-(b+B)\int_{t_0}^{t_1}\Psi_{\leq N-1}(s)\,ds.

\tag{8.6}

\]

Its large-\(t\) limit is the closed cochain concentrated in degree \(N\),

\[

\chi_N^{(N)}(\infty)=B\int_0^\infty\Psi_{N+1}(s)\,ds.

\tag{8.7}

\]

It represents the same finite cyclic class as (8.5).

**Proof.** Below the top degree, closedness follows from (6.10); the correction is annihilated by \(B^2\). At the top,

\[

\begin{aligned}

b\chi_N^{(N)}(t)

&=-BH_{N+2}(t)-B\,b\int_0^t\Psi_{N+1}(s)\,ds.

\end{aligned}

\]

Integrate (8.2) in degree \(N+2\). Since

\(H_{N+2}(s)=O(s^{N+2-p})\to0\) at zero, it gives

\[

b\int_0^t\Psi_{N+1}(s)\,ds

=-H_{N+2}(t)-B\int_0^t\Psi_{N+3}(s)\,ds.

\]

Both integrals converge; substituting leaves zero. This proves closedness at every degree. Differentiating (8.5) cancels the \(B\Psi_{N+1}\) term at the top and gives

\((\chi^{(N)})'=-(b+B)\Psi_{\leq N-1}\).

Integrating proves (8.6). Exponential decay at infinity gives (8.7), and also makes the finite primitive in (8.6) converge as \(t_1\to\infty\). Thus the limit represents the same class. \(\square\)

The finite heat correction also specifies the Mellin primitive whose continuation gives a class comparison.

**Proposition 8.3 (the concrete Mellin primitive).** Define

\[

J^{(N)}(z)=-\int_0^1t^{2z}

\Psi_{\leq N-1}(t)\,dt

\tag{8.8}

\]

in its initial half-plane. Suppose it has meromorphic continuation near zero with Laurent coefficients in the chosen cochain space. Then the residue cocycle of Theorem 7.2, or its gamma conversion with \(g(0)=1\), represents the class of \(\chi^{(N)}(1)\). More precisely,

\[

\Phi_g=\chi^{(N)}(1)

-(b+B)\operatorname{FP}_{z=0}

\bigl(g(z)J^{(N)}(z)\bigr).

\tag{8.9}

\]

**Proof.** In Lemma 4.1 take

\[

c(u)=\chi^{(N)}(\sqrt u),\qquad

K(u)=-\frac1{2\sqrt u}\Psi_{\leq N-1}(\sqrt u).

\]

Proposition 8.2 supplies \(c'= (b+B)K\). The estimates of Lemma 8.1 give the polynomial bounds needed to define both Mellin integrals. The change of variable \(u=t^2\) makes the primitive integral exactly (8.8).

The top correction in \(c(u)\) is

\(B\int_0^{\sqrt u}\Psi_{N+1}(s)\,ds\).

It is \(O(u^{(N+1-p)/2})\) by (8.3), with strictly positive exponent. Its Mellin integral is consequently holomorphic near zero. All other components are the original heat components. In the invertible case the tail of their Mellin integral from \(u\geq1\) is entire. Thus the residue of the Mellin integral of \(c\), also after multiplication by \(g\), is exactly the residue cocycle in Theorem 7.2. Lemma 4.1 now gives (8.9). \(\square\)

There is also an algebraic class comparison which does not assume continuation of the insertion cochains. It uses extension of a linear functional, rather than Laurent coefficients of those cochains.

**Theorem 8.4 (algebraic residue class).** Suppose the coefficient functions in Theorem 7.2 have single-valued meromorphic continuation to a half-plane containing zero. In algebraic cyclic cohomology the residue cocycle, and each of the two gamma conversions, is cohomologous to the finite heat character \(\chi^{(N)}(1)\). This holds without a meromorphy assumption on the insertion primitive.

**Proof.** For each insertion degree put

\[

\Theta_m(z)=\int_0^\infty t^{2z}\Psi_m(t)\,dt.

\tag{8.10}

\]

These are holomorphic in a common strict half-plane \(\operatorname{Re}z>p/2\), by (8.3) and the spectral gap. Integrate (8.2) by parts there. The two boundary terms vanish, and (7.5), with \(u=t^2\), gives

\[

b\Theta_{n-1}(z)+B\Theta_{n+1}(z)=zC_n(z).

\tag{8.11}

\]

For the finite truncation \(\Theta_{\leq N-1}\), this says

\[

(b+B)\frac{\Theta_{\leq N-1}(z)}{z}

=C_{\leq N}(z)-\frac{B\Theta_{N+1}(z)}{z},

\tag{8.12}

\]

where the last term appears only in degree \(N\). The high insertion \(\Theta_{N+1}\) is holomorphic on a half-plane containing zero: its small-\(t\) exponent is \(N-p\), so \(t^{2z}\Psi_{N+1}\) is integrable whenever \(2\operatorname{Re}z+N-p>-1\). At zero,

\[

B\Theta_{N+1}(0)=\chi_N^{(N)}(\infty)

\]

by (8.7).

Let \(W\) be the vector space of holomorphic functions in the initial half-plane. Let \(W_0\subset W\) consist of functions having single-valued meromorphic continuation to some larger half-plane containing zero. Their residues at zero define a linear functional \(\ell_0\) on \(W_0\). It is well defined: any two such continuations agree on their common half-plane by uniqueness, and hence have the same germ at zero. Choose a vector-space basis of \(W_0\), extend it to a basis of \(W\), and extend \(\ell_0\) linearly, for example by assigning zero to the extra basis vectors. Denote the resulting functional by \(\ell\).

For \(g=1,g_{\mathrm{odd}}\), or \(g_{\mathrm{even}}\), define the finite normalized cochain

\[

\sigma_m(a^0,\ldots,a^m)

=\ell\left(

g(z)\frac{\Theta_m(z)(a^0,\ldots,a^m)}{z}

\right),\qquad m\leq N-1.

\tag{8.13}

\]

These three functions \(g\) are entire, so the input belongs to \(W\). Linearity of \(\ell\) makes \(\sigma_m\) multilinear. Applying it to (8.12) gives

\[

(b+B)\sigma=\Phi_g-\chi^{(N)}(\infty).

\tag{8.14}

\]

Indeed the right-side functions belong to \(W_0\), where \(\ell\) is the usual residue; the top insertion is holomorphic and \(g(0)=1\). Proposition 8.2 makes \(\chi^{(N)}(\infty)\) cohomologous to \(\chi^{(N)}(1)\), proving the theorem. \(\square\)

The algebraic primitive in (8.13) need not be continuous for a chosen topology on \(A\). Proposition 8.3 supplies a continuous primitive when its stated continuation bounds hold. We now identify the finite heat class and compute its index pairing.

## 9. From the heat character to the bounded phase

Let \(D\) be invertible, and write \(\Lambda=|D|\). Use the graded operator \(\mathcal D\) of (6.6) throughout; the symbol \(D\) in the order estimates denotes its underlying operator on \(H\). For homogeneous entries define a double heat bracket by

\[

\mathscr D_u(X_0,\ldots,X_m)

=\sum_{j=0}^m(-1)^{|X_0|+\cdots+|X_j|}

\langle X_0,\ldots,X_j,\mathcal D,X_{j+1},\ldots,X_m\rangle_u.

\tag{9.1}

\]

For differential entries every sign is \((-1)^{j+1}\). For \(a^0,d_{\mathcal D}a^1,\ldots\) the signs are \((-1)^j\), as in (8.1).

The top character (8.7) has the useful form

\[

Q_N(D)(a^0,\ldots,a^N)

=\frac{\kappa}{2}\int_0^\infty u^{N/2}

\mathscr D_u(d_{\mathcal D}a^0,\ldots,d_{\mathcal D}a^N)\,du.

\tag{9.2}

\]

Indeed \(\Psi_{N+1}(t)\) is \(\kappa t^{N+1}\) times (9.1) with first entry \(a^0\), at heat length \(t^2\). Applying \(B\) gives all cyclic placements of the initial \(1\). The cyclic signs cancel those from moving the odd differential entries. Each placement splits a heat interval, including the two intervals adjoining an inserted \(\mathcal D\). Their lengths sum to one, by (6.11). Thus \(B\) removes that \(1\) and leaves the double bracket in (9.2). Finally \(t^{N+1}dt=\tfrac12u^{N/2}du\). In particular \(Q_N(D)\) is the closed finite character already constructed in Proposition 8.2.

To deform it to the phase, use the same grading convention for \(D_s\) and put

\[

\begin{aligned}

D_s&=D\Lambda^{-s},&&0\leq s\leq1,\\

V_s&=\partial_s\mathcal D_s=-\mathcal D_s\log\Lambda.

\end{aligned}

\tag{9.3}

\]

The endpoint is \(\mathcal F\), the graded version of \(F=\operatorname{sign}D\).

Brackets with a subscript \(s,u\) use \(\mathcal D_s\) and \(e^{-uD_s^2}\).

They need not have trace-class heat alone at \(s=1\). The products used here do have traces, as the estimates below show.

**Lemma 9.1 (the cyclic homotopy identity).** Fix \(N>p\) of the heat parity. For a differentiable family \(\mathcal D_s\), set \(q_j=[\mathcal D_s,a^j]\), \(V=\partial_s\mathcal D_s\), and

\[

\begin{aligned}

C_{s,u}(a^0,\ldots,a^N)&=\mathscr D_{s,u}(q_0,\ldots,q_N),\\

\Phi_{s,u}(a^0,\ldots,a^N)&=

\mathscr D_{s,u}(a^0V,q_1,\ldots,q_N),\\

T_{s,u}(a^0,\ldots,a^N)&=

\sum_{r=0}^N(-1)^{Nr}

\langle V,q_r,\ldots,q_N,q_0,\ldots,q_{r-1}\rangle_{s,u}.

\end{aligned}

\tag{9.4}

\]

Whenever the differentiated brackets are justified,

\[

bB\Phi_{s,u}

=\partial_s C_{s,u}

-2u\,\partial_uT_{s,u}-(N+2)T_{s,u}.

\tag{9.5}

\]

For the family (9.3), all the following integrals converge, and

\[

L_{N-1}(s)=\frac{\kappa}{2}\,

B\int_0^\infty u^{N/2}\Phi_{s,u}\,du,\qquad

\partial_sQ_N(D_s)=bL_{N-1}(s).

\tag{9.6}

\]

The cochain \(L_{N-1}(s)\) is cyclic, normalized, and continuous in \(s\) up to \(s=1\).

**Proof of the identity.** Two consequences of the heat calculation make the signs explicit. If an even entry \(a\) is moved across an interval of a double bracket, then

\[

\begin{aligned}

&\mathscr D_u(\ldots,X_{j-1}a,X_{j+1},\ldots)

-\mathscr D_u(\ldots,X_{j-1},aX_{j+1},\ldots)\\

&\quad=u\mathscr D_u(\ldots,X_{j-1},[\mathcal D^2,a],X_{j+1},\ldots)

-(-1)^{|X_0|+\cdots+|X_{j-1}|}

\langle\ldots,X_{j-1},[\mathcal D,a],X_{j+1},\ldots\rangle_u.

\end{aligned}

\tag{9.7}

\]

The first term follows by differentiating \(e^{-uv\mathcal D^2}a e^{-u(w-v)\mathcal D^2}\) and integrating \(v\). Insertions of \(\mathcal D\) away from \(a\) obey this same collapse. The two insertions adjoining \(a\) differ by \([\mathcal D,a]\); their prefix sign is exactly the sign displayed. This accounts for the second term, including the cyclic interval.

Also, with graded commutators and \(\alpha_j=|X_0|+\cdots+|X_{j-1}|\),

\[

\sum_{j=0}^m(-1)^{\alpha_j}

\mathscr D_u(X_0,\ldots,[\mathcal D,X_j]_{\mathrm{graded}},\ldots,X_m)

=-2\partial_u\langle X_0,\ldots,X_m\rangle_u.

\tag{9.8}

\]

Apply the graded trace of \([\mathcal D,\cdot]\) to each summand in (9.1). Terms hitting an original \(X_j\) give the left side. Terms hitting the insertion use

\([\mathcal D,\mathcal D]_{\mathrm{graded}}=2\mathcal D^2\).

An insertion of \(\mathcal D^2\) splits a heat interval and integrates to its length times the corresponding differentiated heat factor. Summing the lengths gives minus twice the \(u\)-derivative, proving (9.8).

Here is the full product-merger calculation needed for (9.5). Read indices modulo \(N+1\), and put \(A'=\mathcal D_sV+V\mathcal D_s\). Define

\[

\begin{aligned}

U_{s,u}&=\sum_{r=0}^N(-1)^{Nr}

\mathscr D_{s,u}(A',q_r,\ldots,q_{r-1}),\\

M_{s,u}&=\sum_{r=0}^N(-1)^{Nr}

\mathscr D_{s,u}([V,a^r],q_{r+1},\ldots,q_{r-1}).

\end{aligned}

\]

Expansion of \(Bb\Phi\) gives

\[

\begin{aligned}

Bb\Phi_{s,u}

={}&\sum_{r=0}^N(-1)^{Nr}

\bigg[

u\sum_{i=0}^N(-1)^i

\mathscr D_{s,u}\bigl(V,q_r,\ldots,

[\mathcal D_s^2,a^{r+i}],\ldots,q_{r-1}\bigr)\\

&\hspace{28mm}+(N+1)

\langle V,q_r,\ldots,q_{r-1}\rangle_{s,u}

-\mathscr D_{s,u}([V,a^r],q_{r+1},\ldots,q_{r-1})

\bigg].

\end{aligned}

\tag{9.9}

\]

To see every term in this expansion, apply \(B\) by prepending \(1\) and rotating the \(N+1\) original arguments, with weight \((-1)^{Nr}\). In \(b\Phi\), expand each merged differential by the Leibniz rule. Pair its right multiplication with the next term's left multiplication. Equation (9.7) turns each of the \(N+1\) interval differences into the double commutator term and one ordinary bracket. The former has sign \((-1)^i\); the latter has sign \(+1\), giving \(N+1\) copies. At the ends of a rotated list, the two products of \(V\) with \(a^r\) leave \(-[V,a^r]\). All other end products cancel with those in the next rotation. These are precisely the three terms in the square brackets of (9.9).

Apply (9.8) to the list \((V,q_r,\ldots,q_{r-1})\).

Its first commutator is \(A'\), and

\([\mathcal D_s,q_j]_{\mathrm{graded}}=[\mathcal D_s^2,a^j]\).

Thus (9.9) becomes

\[

Bb\Phi_{s,u}=uU_{s,u}+2u\partial_uT_{s,u}

+(N+1)T_{s,u}-M_{s,u}.

\tag{9.10}

\]

Finally cyclic rotation in (9.1) gives

\[

C_{s,u}=\sum_{r=0}^N(-1)^{Nr}

\langle\mathcal D_s,q_r,\ldots,q_{r-1}\rangle_{s,u}.

\]

Differentiating the inserted operator gives \(T\); differentiating the differential entries gives \(M\). Duhamel differentiation of every heat interval gives \(-uU\). Consequently

\(\partial_s C=T+M-uU\).

Combine this with (9.10) and \(bB=-Bb\) to obtain (9.5). The factors \((-1)^{Nr}\) retain the odd cyclic signs throughout.

**Proof of convergence and the endpoint assertion.** The complex-power expansion from the second lesson gives, uniformly for \(0\leq s\leq1\),

\[

[\mathcal D_s,a]\in\mathrm{OP}^{-s},\qquad

\mathcal D_s\in\mathrm{OP}^{1-s},\qquad

V_s\in\mathrm{OP}^{1-s+\varepsilon},

\tag{9.11}

\]

for every \(\varepsilon>0\). For the first inclusion write

\([D_s,a]=[D,a]\Lambda^{-s}+D[\Lambda^{-s},a]\).

The commutator of the power has order \(-s-1\). Differentiating in \(s\) adds \(\log\Lambda\), bounded relative to \(\Lambda^\varepsilon\); the same finite expansion controls the differentiated remainders.

The largest-interval argument of (7.4) bounds a product of total order \(h(s)\) by a constant times

\(\operatorname{Tr}(\Lambda^{h(s)}e^{-cu\Lambda^{2(1-s)}})\),

where \(c>0\) depends only on the number of factors. Products of negative order are allowed: distribute the weights on the two sides of the largest heat interval, using the graph-scale bounds. Integrating the scalar heat factor gives the exact estimate

\[

\int_0^\infty u^{N/2}

\operatorname{Tr}(\Lambda^{h(s)}e^{-cu\Lambda^{2(1-s)}})\,du

=\Gamma(N/2+1)c^{-N/2-1}

\operatorname{Tr}\Lambda^{h(s)-(N+2)(1-s)}.

\tag{9.12}

\]

For \(C\) the total order is \(1-s(N+2)\), and the final exponent is \(-N-1\). For \(\Phi\) it is \(2-s(N+2)+\varepsilon\), and the final exponent is \(-N+\varepsilon\). Choose

\(0<\varepsilon<N-p\).

Both final powers are trace class. The estimates are uniform even at \(s=1\), where the heat is scalar.

Differentiating \(C\) adds a logarithm. In a heat derivative it adds \(A'\), of order \(2(1-s)+\varepsilon\), and one power of \(u\). These two changes cancel in (9.12), leaving exponent \(-N-1+\varepsilon\). The same calculation controls \(u\partial_u T\). Reserve a further small positive order margin below \(-p\). For a spectral cutoff, move half of this margin to either side of each changed coefficient. The weighted coefficient errors then tend to zero in norm: finite spectral sections converge strongly, and the extra negative powers of \(\Lambda\) are compact; their omitted tails have norm bounded by a positive negative power of the cutoff eigenvalue. Apply (9.12) with the remaining trace-class power. This gives uniform convergence in the integrated trace norms, rather than merely a uniform integral bound. Logarithm-weighted versions give differentiation and continuity at the endpoint. Thus the assertions hold for the actual operators.

Integration by parts in \(u\) removes the last two terms in (9.5), since

\[

-2\int_0^\infty u^{N/2+1}\partial_uT\,du

=(N+2)\int_0^\infty u^{N/2}T\,du.

\]

The boundary values are zero. For completeness, the estimates just proved make both \(u^{N/2}T\) and \(u^{N/2+1}T'\) integrable. Hence \(u^{N/2+1}T\) has limits at zero and infinity. A nonzero limit at either end would contradict integrability of \(u^{N/2}T\). Equation (9.6) follows.

The operator \(B\) produces a cyclic cochain: rotating its \(N\) arguments simply reindexes its sum with the cyclic sign \((-1)^{N-1}\). Normalization of \(\Phi\) implies normalization of \(B\Phi\). The trace estimates give continuity in \(s\) of its integral. This finishes the proof. \(\square\)

**Theorem 9.2 (the Fredholm character).** Under the hypotheses of Theorem 8.4, for invertible \(D\), the residue cocycle and its gamma conversions have the algebraic cyclic class represented by the single cyclic cochain

\[

\operatorname{Ch}_{F,N}(a^0,\ldots,a^N)

=\frac{\kappa\Gamma(N/2+1)}{N!}

\operatorname{Str}\bigl(a^0[\mathcal F,a^1]\cdots[\mathcal F,a^N]\bigr),

\qquad N>p.

\tag{9.13}

\]

In the odd case the supertrace in this formula reduces to ordinary trace. The homotopy from the finite heat character to (9.13) has a continuous cyclic primitive.

**Proof.** Integrate (9.6) in \(s\). Since \(L\) is cyclic and normalized, \(BL=0\), so \(bL=(b+B)L\). Thus

\[

Q_N(F)-Q_N(D)=(b+B)\int_0^1L_{N-1}(s)\,ds.

\tag{9.14}

\]

At \(s=1\), \(\mathcal F^2=1\) and every differential anticommutes with \(\mathcal F\). Moving each insertion in (9.1) to the front cancels its prefix sign. All \(N+1\) terms are the same; the simplex volume is \(1/(N+1)!\). Formula (9.2) becomes

\[

Q_N(F)=\frac{\kappa\Gamma(N/2+1)}{2N!}

\operatorname{Str}\bigl(\mathcal F[\mathcal F,a^0]\cdots[\mathcal F,a^N]\bigr).

\]

All products being cycled are trace class, by \(N>p\). Using

\(\mathcal F[\mathcal F,a^0]=a^0-\mathcal F a^0\mathcal F\),

and then graded cyclicity and the \(N\) anticommutations, shows that this trace is twice the trace in (9.13). Hence \(Q_N(F)=\operatorname{Ch}_{F,N}\).

This also verifies the properties of the bounded character directly. Cyclic rotation in the double bracket gives the cochain sign \((-1)^N\). The Leibniz expansion of \(b\) in (9.13) cancels its interior products; the two remaining end products cancel by trace cyclicity, since algebra elements are even. Thus \(b\operatorname{Ch}_{F,N}=0\). It is normalized, and cyclicity moves any first argument \(1\) to an internal slot, so \(B\operatorname{Ch}_{F,N}=0\). Combining (9.14), Proposition 8.2 and Theorem 8.4 proves the stated class equality. The first step is algebraic unless the stronger continuation condition of Proposition 8.3 holds. \(\square\)

The passage \(D\mapsto D|D|^{-s}\) and cyclic insertions are standard tools in the residue theorem; see [Higson 2006]. The calculation above keeps the odd rotation signs and the trace estimate at the bounded endpoint explicit.

For an odd, noninvertible \(D\), put \(D'=D+P_0\), where \(P_0\) projects onto its kernel. This is an invertible selfadjoint smoothing perturbation. Its positive-degree residue terms equal those for \(D\): every changed commutator contains a smoothing factor, and the spectral powers differ only on \(P_0\). Such terms have entire traces and no positive-degree residue. Regularity is retained because \(aP_0\), \(P_0a\) and their iterated graph commutators are smoothing. Theorem 9.2 therefore applies to the original odd residue cocycle, with

\(F=\operatorname{sign}D'\).

The even case cannot use this perturbation while preserving the grading: its kernel may have unequal positive and negative dimensions. Its harmonic degree-zero term must be retained in the class comparison.

We will use a finite direct product to make that comparison without choosing an invertible odd operator on the original harmonic space.

**Lemma 9.3 (separating a scalar summand).** For a unital algebra \(A\), the two unital projections from \(A\times\mathbb C\) induce the isomorphism

\[

HC^{\mathrm{parity}}(A)\oplus HC^{\mathrm{parity}}(\mathbb C)

\longrightarrow HC^{\mathrm{parity}}(A\times\mathbb C),

\quad

(\alpha,\beta)\longmapsto\pi^*\alpha+\varepsilon^*\beta.

\tag{9.15}

\]

Here the parity cohomology is the finite periodic cochain convention of Section 6. The \(A\) component of a cyclic cocycle is obtained by restricting it to the \(A\) summand; this restriction may initially be unnormalized.

**Proof.** One can perform the splitting in the cyclic tensor complex

\[

C_n^\lambda(B)=B^{\otimes(n+1)}/(1-t_n)B^{\otimes(n+1)}

\]

with differential \(b\), where \(B=A\times\mathbb C\) and \(t_n\) is the signed rotation from Lemma 6.1. That differential descends by \(b(1-t)=(1-t)b'\).

Recall why this complex computes the cohomology represented by finite \((b,B)\) collections. We use the cyclic resolution, averaging and column contraction of Higher traces, Lemma 3.1, Theorem 6.2, Theorem 7.1 and Lemma 9.1, over \(\mathbb C\). In its cyclic bicomplex the successive horizontal maps are \(1-t\) and \(N\); its vertical maps are \(b\) and \(b'\). Their compatibilities are (6.3). Each horizontal row is exact except its cyclic quotient: since \(t^{n+1}=1\), the averaging map \(N/(n+1)\) projects onto the invariant tensors, and

\[

R=-\frac1{n+1}\sum_{j=0}^n jt^j,\qquad

(1-t)R=1-\frac{N}{n+1}.

\]

These give explicit contractions of the other horizontal terms. Row elimination leaves the cyclic quotient with its \(b\) differential.

Here is an explicit comparison with the \((b,B)\) model. In the chain bicomplex, even columns have vertical differential \(b\), odd columns have \(-b'\), and the horizontal maps toward the preceding column are \(N\) from a positive even column and \(D=1-t\) from an odd column. Keep the even columns. Their total chain space in degree \(r\) is

\[

\bigoplus_{j=0}^{\lfloor r/2\rfloor} C_{r-2j}(A).

\]

Here \(C_n(A)=A^{\otimes(n+1)}\).

Give it differential \(b+B\), with \(B=DsN\) moving two columns to the left. For an entry \(x\) in an even column \(p>0\), its lift to the full bicomplex is \(x\) in that column together with \(sNx\) in column \(p-1\); in column zero just use \(x\). Indeed,

\[

Nx-b'sNx=sNbx,\qquad DsNx=Bx,\qquad NBx=0.

\]

These identities show that the lift is a chain map, including every sign. Filter by column. On the first homology of that filtration, the odd columns vanish by the \(b'\) unit contraction, while the lift is the identity on the even-column \(b\)-homology. The finite filtration in each total degree therefore makes it a homology isomorphism: successive highest-column cycle and boundary obstructions are precisely those first homology groups. This proves the comparison without assuming a normalized contracting homotopy or an infinite series of transfers.

We also justify internal-unit normalization. On the full tensor complex let \(s_j\) insert \(1\) after position \(j\), and let \(\mathcal D_n\) be the span of tensors having an internal \(1\). Put

\[

F^p\mathcal D_n=\sum_{j=0}^{\min(p,n-1)}\operatorname{im}s_j,

\qquad F^{-1}\mathcal D_n=0.

\]

The face-degeneracy identities are

\[

d_i s_j=

\begin{cases}

s_{j-1}d_i,&i<j,\\

1,&i=j\ \text{or}\ i=j+1,\\

s_jd_{i-1},&i>j+1.

\end{cases}

\]

They follow by placing the inserted unit relative to the merged pair; the last case includes the cyclic endpoint pair. The two identity terms cancel with their alternating signs, so \(b\) preserves this filtration. Modulo \(F^{p-1}\), its \(p\)-th quotient is contracted by \(h=(-1)^ps_p\). In fact

\[

bs_p+s_pb\equiv\sum_{i=0}^p(-1)^is_pd_i

\pmod{F^{p-1}},

\]

and on \(x=s_py\) all terms with \(i<p\) retain an earlier unit, while the \(i=p\) term is \((-1)^px\). In degrees where the quotient is zero the contraction is taken to be zero.

Thus \(bh+hb=1\) on each quotient. Every cycle in \(\mathcal D_n\) uses finitely many filtration levels; subtracting a boundary to remove its highest level, then repeating, proves that the whole degenerate \(b\)-complex is acyclic.

Both \(b\) and \(B\) preserve \(\mathcal D\), as already checked in Lemma 6.1. In each finite cyclic total degree, filtering its degenerate mixed complex by column leaves these acyclic \(b\)-complexes. Therefore that total complex is also acyclic, and quotienting by \(\mathcal D\) preserves homology. Algebraic duality over \(\mathbb C\) preserves these exact sequences: each vector-space sequence splits by a choice of basis. The same conclusion holds for cohomology. The quotient \(B\) is the explicit normalized formula in (6.1).

Adding two columns defines periodicity in all these models. The comparisons and the unit quotient commute with this map and with unital homomorphisms. Taking the direct limit gives exactly the finite parity-cochain convention of Section 6: a finite collection occurs in some total degree, and a finite coboundary occurs after passing to a sufficiently large such degree. Exactness of that direct limit follows by the same observation for each representative. Thus the cyclic quotient, the bicomplex, and the normalized finite \((b,B)\) cochains give the same periodic classes with the naturality required in (9.15).

Now decompose each tensor entry according to the central projections \(E=(1,0)\) and \(G=(0,1)\). Pure \(E\) tensors form the cyclic complex of \(A\), and pure \(G\) tensors form that of \(\mathbb C\). We give an explicit contraction of every mixed tensor. For a tensor \(c=(x_0,\ldots,x_n)\) whose entries each belong to one of the two summands, let

\[

J(c)=\{j:\ x_j\in EB,\ x_{j+1}\in GB\},

\]

with cyclic indices. A mixed word has at least one such transition. Define on its cyclic class

\[

hc=\frac1{|J(c)|}\sum_{j\in J(c)}(-1)^j

(x_0,\ldots,x_j,E,x_{j+1},\ldots,x_n).

\tag{9.16}

\]

At \(j=n\) the inserted \(E\) is last. Rotation reindexes these insertions with the signed rotation in degree \(n+1\), so \(h\) is well defined on the cyclic quotient.

In \(bhc\), merging \(x_jE=x_j\) returns \(c\), once for each transition; merging \(Ex_{j+1}\) gives zero. Every other nonzero merger is between two entries of the same color. It preserves the number of transitions, and cancels the corresponding term of \(hbc\), since crossing the insertion changes the merger sign. A merger across the last and first entries has the same cancellation by the cyclic relation. Thus \(bh+hb=1\) on the mixed subcomplex. This proves the splitting in each cyclic degree, also after taking cochains. The splitting is induced by the two projections, so it commutes with their periodicity maps. Taking parity classes proves (9.15). \(\square\)

**Theorem 9.4 (the even harmonic class).** Let \(D\) be even, possibly noninvertible, and retain the completed residue cocycle of Corollary 7.3. Its class is the even Fredholm Chern character, including its harmonic contribution.

**Proof.** Use \(H\oplus H\), with

\[

\begin{aligned}

\widetilde\gamma&=\begin{pmatrix}\gamma&0\\0&-\gamma\end{pmatrix},\\

\widetilde D&=\begin{pmatrix}D&P_0\\P_0&-D\end{pmatrix}.

\end{aligned}

\tag{9.17}

\]

Then \(\widetilde D\) is selfadjoint and odd,

\(\widetilde D^2=\operatorname{diag}(D^2+P_0,D^2+P_0)\),

and is invertible. Its graph scale is the doubled completed scale.

Represent the external unitization \(A^+=A\oplus\mathbb C\) by

\[

\rho(a,\lambda)=

\begin{pmatrix}a+\lambda1&0\\0&\lambda1\end{pmatrix}.

\tag{9.18}

\]

The product on \(A^+\) is

\((a,\lambda)(b,\mu)=(ab+\lambda b+\mu a,\lambda\mu)\);

its unit is \((0,1)\). The map

\((a,\lambda)\mapsto(a+\lambda1,\lambda)\)

identifies it with \(A\times\mathbb C\), with projections \(\pi,\varepsilon\) as in Lemma 9.3.

The commutator with (9.18) has upper diagonal entry \([D,a]\), lower diagonal entry zero, and off-diagonal entries \(-aP_0,P_0a\). These off-diagonal terms are smoothing. All regularity, summability and continuation hypotheses for \(\widetilde D\) follow from the completed ones for \(D\): the new traces are old coefficient traces or entire smoothing traces. Theorem 9.2 therefore applies to this unital triple.

For every positive even degree, a residue term involving an off-diagonal smoothing factor has zero residue. The remaining term has all differential factors in the upper diagonal block. Its first coefficient is \(\pi(a^0,\lambda_0)=a^0+\lambda_01\). Thus the doubled residue cochain in positive degrees is exactly \(\pi^*\Phi_{\mathrm{even}}\), for either gamma convention.

At degree zero its completed coefficient trace is

\[

\operatorname{Tr}\bigl(\gamma(a+\lambda1)\Lambda^{-2z}\bigr)

-\lambda\operatorname{Tr}(\gamma\Lambda^{-2z}).

\tag{9.19}

\]

Every nonzero spectral pair of the odd \(D\) has equal positive and negative graded multiplicities, so in the trace convergence half-plane

\[

\operatorname{Tr}(\gamma\Lambda^{-2z})

=\dim\ker D^+-\dim\ker D^-=\operatorname{Index}D^+.

\]

It continues as this constant. Its gamma residue and its converted finite part are both the same index. Consequently the entire doubled cochain is

\[

\widetilde\Phi

=\pi^*\Phi_{\mathrm{even}}

-(\operatorname{Index}D^+)\,\varepsilon,

\tag{9.20}

\]

where the last term is a degree-zero scalar trace.

By Theorem 9.2 this class equals the bounded character of

\(\widetilde F=\widetilde D|\widetilde D|^{-1}\)

with representation (9.18). The even Chern character for a noninvertible \(D\) is precisely the \(A\) component of this invertible doubled character. Lemma 9.3 extracts that component from (9.20), giving \([\Phi_{\mathrm{even}}]\). In particular the scalar correction is not permission to discard \(P_0\) from (9.19): it separates the additional summand, while the original harmonic term remains in \(\Phi_{\mathrm{even}}\). \(\square\)

The finite-pole hypothesis has made every Laurent sum finite. The broader isolated-singularity definition from the second lesson has a corresponding version of the character theorem.

**Proposition 9.5 (isolated singularities).** Suppose the actual coefficient zeta functions have single-valued holomorphic continuation outside a locally finite discrete singular set, allowing isolated essential singularities. Retain regularity and finite summability. The actual heat residues of Theorem 7.2 and Corollary 7.3 still define cocycles and represent the Fredholm character of Theorems 9.2 and 9.4. The unrenormalized Laurent-coefficient formula is then an absolutely convergent series over the Laurent order. The gamma-converted formula has only finitely many Laurent orders, exactly as in Section 5, and the converted even degree-zero component is still the constant Laurent coefficient.

**Proof.** In each degree the finite heat Taylor expansion and holomorphic remainder of Lemma 7.1 continue the actual Mellin cochain across the isolated singularities. They require continuation of the retained coefficient traces, rather than a finite bound on their pole orders. Its cocycle identity holds first in the trace convergence region and then by uniqueness on the complement of the discrete singular set. Taking the usual residue around zero preserves that identity, whether the singularity is a pole or essential.

Let \(h(z)=\sum_{j\in\mathbb Z}h_jz^j\) be such a coefficient trace, and let \(G(z)=\sum_{r\geq0}g_rz^r\) be a gamma factor holomorphic near zero. On a sufficiently small circle of radius \(\rho\), Laurent's coefficient estimate gives

\[

|h_{-r-1}|\leq \max_{|z|=\rho}|h(z)|\,\rho^{r+1}.

\]

Choose \(\rho<R\), where \(G\) is holomorphic on a larger closed disk of radius \(R\). Cauchy's estimate gives \(|g_r|\leq C R^{-r}\). Thus

\[

\operatorname*{Res}_{z=0}G(z)h(z)

=\sum_{r\geq0}g_rh_{-r-1}

\]

converges absolutely, by a geometric bound. It is exactly the unrenormalized sum of gamma Taylor coefficients times \(\tau_r\). At even degree zero use \(G(z)=\Gamma(1+z)\) and \(\Gamma(z)=G(z)/z\); the same argument gives the absolutely convergent sum with \(\tau_{r-1}\), including the constant coefficient at \(r=0\). In the converted positive degrees \(G\) is the finite polynomial of Section 5, so only its finitely many coefficients remain. In converted degree zero it is \(1/z\), selecting only the constant coefficient of \(h\).

The algebraic class argument of Theorem 8.4 also works for these continuations. In its vector space \(W_0\), allow single-valued holomorphic continuation to a larger half-plane with a locally finite discrete set removed. Their residues at zero define a linear functional: the intersection of any two such domains is connected after removing their discrete sets, so continuation uniqueness gives the same germ. A finite sum has a common such domain, hence \(W_0\) remains a vector subspace. Extend its residue functional to \(W\) exactly as before. The high insertion is holomorphic near zero, and (8.12) is unchanged. Therefore (8.14) identifies the residue class with the finite heat class. Lemma 9.1 and the harmonic doubling use order and trace estimates alone, and complete its identification with the Fredholm character. \(\square\)

## 10. Computing the pairing by finite defects

We first prove the trace identity that turns a character value into an index.

**Lemma 10.1 (a pair of projections).** Let \(P,Q\) be orthogonal projections, with \(P-Q\) compact and \((P-Q)^{2j+1}\) trace class. Then \(QP:PH\to QH\) is Fredholm and

\[

\operatorname{Index}(QP)=\operatorname{Tr}(P-Q)^{2j+1}.

\tag{10.1}

\]

**Proof.** The map \(PQ:QH\to PH\) is a parametrix: both product errors are compact multiples of \(P-Q\). Put \(A=P-Q\) and \(B=P+Q-1\). Multiplication gives

\[

AB=-BA,\qquad B^2=1-A^2.

\tag{10.2}

\]

The compact selfadjoint \(A\) has finite-dimensional nonzero eigenspaces. On the eigenspace of \(\lambda\), with \(0<|\lambda|<1\), \(B\) is an isomorphism onto the eigenspace of \(-\lambda\), since \(B^2=1-\lambda^2\). Their contributions to the trace of the odd power cancel. Trace-classness makes the eigenvalue sum absolutely convergent. The zero eigenspace contributes zero.

The \(+1\) eigenspace is \(PH\cap\ker Q\). Indeed \(Ah=h\) implies

\[

\|Ph\|^2-\|Qh\|^2=\|h\|^2,

\]

forcing \(Ph=h,Qh=0\); the converse is immediate. Similarly the \(-1\) eigenspace is \(QH\cap\ker P\). They are respectively the kernel and the adjoint kernel of \(QP\). Their dimension difference is its index, and it is precisely the remaining trace. \(\square\)

**Theorem 10.2 (odd index pairing).** Let \(U\in M_r(A)\) be unitary. Use the matrix-amplified trace and let \(P=(1+F)/2\), with the odd phase chosen as above if a kernel is present. If \(\Phi_{\mathrm{odd}}\) denotes the gamma-converted odd residue cocycle, then

\[

\operatorname{Index}(PUP)

=-\frac1{\sqrt{2\pi i}}

\sum_{j\geq0}(-1)^j j!\,

(\Phi_{\mathrm{odd}})_{2j+1}

(U^{-1},U,\ldots,U^{-1},U).

\tag{10.3}

\]

The sum is finite. Equivalently, the same expression without the leading minus sign evaluates the cycle for \(U^{-1}\).

**Proof.** A coboundary pairs to zero with (6.4), because its successive \(b\) and \(B\) contributions cancel. The cochain is finite, so there is no interchange of infinite sums. By Theorem 9.2 it suffices to evaluate the single bounded character of degree \(N=2j+1>p\).

Put \(Q=U^{-1}PU\) and \(C=U^{-1}[F,U]=2(Q-P)\).

The identity

\([F,U^{-1}]=-U^{-1}[F,U]U^{-1}\)

reduces its alternating product to

\[

U^{-1}[F,U][F,U^{-1}]\cdots[F,U]

=(-1)^j C^{2j+1}.

\tag{10.4}

\]

Repeatedly pairing a factor \([F,U^{-1}]\) with its adjacent \(U\) proves (10.4) without reordering any factors. Also

\[

\frac{\kappa}{\sqrt{2\pi i}}\,

\frac{\Gamma(j+3/2)}{(2j+1)!}\,(-1)^j j!

=\frac{(-1)^j}{2^{2j+1}},

\tag{10.5}

\]

by the half-integer gamma formula and the principal square roots. Hence the value of the cycle divided by \(\sqrt{2\pi i}\) is

\(\operatorname{Tr}(Q-P)^{2j+1}\).

Regularity gives \([F,U]\in\mathrm{OP}^{-1}\), so its \(N\)-fold products are trace class for \(N>p\). Lemma 10.1 applies. The unitary \(U^{-1}:PH\to QH\) identifies \(PUP\) with \(QP\), since

\(U^{-1}PUP=QP\) on \(PH\). Thus

\(\operatorname{Tr}(Q-P)^N=-\operatorname{Index}(PUP)\),

proving (10.3). Finally \(PU^{-1}P\) is the adjoint of \(PUP\), whose index is opposite. \(\square\)

**Theorem 10.3 (even pairing for an invertible triple).** Let \(D\) be even and invertible, and let \(e\in M_r(A)\) be an idempotent commuting with the grading. If \(\Phi_{\mathrm{even}}\) is the gamma-converted even residue cocycle, then

\[

\begin{aligned}

\operatorname{Index}(eF^+e:eH^+\to eH^-)

={}&(\Phi_{\mathrm{even}})_0(e)\\

&+\sum_{j\geq1}\frac{(-1)^j(2j)!}{j!}

(\Phi_{\mathrm{even}})_{2j}

(e-\tfrac12,e,\ldots,e).

\end{aligned}

\tag{10.6}

\]

Here \(F^+:H^+\to H^-\) is the off-diagonal component of \(F\). The formula holds for arbitrary bounded idempotents in the algebra, as well as orthogonal projections.

**Proof for a projection.** Choose even \(N=2j>p\), \(j\geq1\). The bounded character coefficient is \(j!/(2j)!\). Pairing it with (6.5) therefore gives

\[

(-1)^j\operatorname{Str}\bigl((e-\tfrac12)[F,e]^{2j}\bigr).

\tag{10.7}

\]

Put \(q=FeF\) and \(A=e-q\). The identities

\([F,e]=FA\), \(FAF=-A\), give

\([F,e]^{2j}=(-1)^j A^{2j}\).

Conjugation by the odd unitary \(F\) reverses the supertrace and exchanges \(e\) and \(q\), while preserving \(A^{2j}\). Consequently (10.7) equals

\[

\operatorname{Str}((e-\tfrac12)A^{2j})

=\tfrac12\operatorname{Str}(A^{2j+1}).

\tag{10.8}

\]

On \(H^+\), \(q^+=F^-e^-F^+\). The unitary \(F^-:H^-\to H^+\) identifies \(e^-F^+e^+\) with \(q^+e^+:e^+H^+\to q^+H^+\). Lemma 10.1 makes its index

\(\operatorname{Tr}_{H^+}(e^+-q^+)^{2j+1}\).

Conjugation by \(F^+\) sends the difference on \(H^+\) to the negative of the difference on \(H^-\). Thus the supertrace in (10.8) is twice this index. This proves the character pairing. Theorem 9.2 and the cycle identity (6.5) transfer it to (10.6).

**Reduction of an idempotent to a projection.** The range of a bounded idempotent is closed. Relative to its orthogonal range decomposition,

\[

e=\begin{pmatrix}1&X\\0&0\end{pmatrix},\qquad

p=ee^*\bigl(1-(e-e^*)^2\bigr)^{-1}

=\begin{pmatrix}1&0\\0&0\end{pmatrix}.

\tag{10.9}

\]

The inverse exists because \(1-(e-e^*)^2\geq1\).

Moreover \(ep=p,pe=e\). The path \(e_t=(1-t)e+tp\) is therefore an idempotent with the same range, and it commutes with the grading.

Let \(p_{\mathrm{sum}}\) denote the summability bound used to choose \(N\), distinct from the projection \(p\) in (10.9). Choose \(q_0\) with \(p_{\mathrm{sum}}<q_0<N\). The commutators of \(F\) with \(e,e^*\) belong to the Schatten class \(\mathcal S^{q_0}\). Formula (10.9), the product rule, and

\([F,R^{-1}]=-R^{-1}[F,R]R^{-1}\)

give the same conclusion for \(p\), \(e_t\), and \(\dot e_t\). Every \(N\)-fold product of such commutators is trace class by Schatten Hölder. No continuation hypothesis on the larger algebra containing the inverse in (10.9) is needed.

The compressed maps \(e_tF^+e_t\) act between the fixed ranges \(pH^+\) and \(pH^-\), are norm continuous, and have parametrix \(e_tF^-e_t\) modulo compact commutators. Their indices are constant. Their character values are also constant; the following trace calculation proves this without an appeal to a homotopy of Chern chains. Put

\(A_t=e_t-Fe_tF\) and \(K_t=A_t^{2j}\).

The identity \(e_tK_t=K_te_t\) follows first for \(A_t^2\) by multiplication of the two idempotents and then for its powers. Differentiating (10.8), with trace-class cyclicity, gives

\[

\frac d{dt}\,\tfrac12\operatorname{Str}(A_t^{2j+1})

=\frac{2j+1}{2}\operatorname{Str}

\bigl((\dot e_t-F\dot e_tF)K_t\bigr)

=(2j+1)\operatorname{Str}(\dot e_tK_t).

\]

Here \(FK_tF=K_t\) accounts for the last equality. Differentiating \(e_t^2=e_t\) gives

\(e_t\dot e_te_t=(1-e_t)\dot e_t(1-e_t)=0\).

Since \(K_t\) commutes with \(e_t\), the trace-class operator \(\dot e_tK_t\) has zero diagonal blocks relative to this bounded idempotent. Its supertrace is zero: split its trace with \(e_t+(1-e_t)=1\) and cycle these even bounded factors. Thus the character value at \(e\) equals that at \(p\), already proved to be the same index. This establishes (10.6) for every idempotent. \(\square\)

**Theorem 10.4 (the full even index).** For an even triple, whether or not \(D\) is invertible, the right side of (10.6), with the harmonic completion of Corollary 7.3, equals

\[

\operatorname{Index}(eD^+e:e\operatorname{Dom}D^+\to eH^-).

\tag{10.10}

\]

The range spaces carry their Hilbert norms, and the domain carries the graph norm.

**Proof.** In the doubled triple of Theorem 9.4, the idempotent \((e,0)\) is represented by \(\widetilde e=\operatorname{diag}(e,0)\). Applying Theorem 10.3 to that invertible triple gives the index of

\(\widetilde e\widetilde F^+\widetilde e\).

Its residue evaluation is exactly the right side of (10.6). In positive degrees the projection \(\pi\) sends the first Chern-cycle entry \((e,0)-(0,1)/2\) to \(e-1/2\), and all other entries to \(e\). The scalar correction in (9.20) is evaluated only at degree zero, where \(\varepsilon(e,0)=0\).

The upper diagonal block of \(\widetilde F\) is

\(F_0=D(D^2+P_0)^{-1/2}\), zero on the kernel. The ranges of \(\widetilde e\) in the two doubled grading spaces are just \(eH^+\) and \(eH^-\) in the first copy. Hence this bounded index is that of \(eF_0^+e\).

We compare this with (10.10), first when \(e=e^*\). Define

\[

D_e=eDe+(1-e)D(1-e)=D+[e,[D,e]].

\tag{10.11}

\]

The last commutator is bounded and selfadjoint. Thus \(D_e\) is selfadjoint on \(\operatorname{Dom}D\), is odd, commutes with \(e\), and has compact resolvent. The latter follows from the resolvent identity for a bounded perturbation of an operator with compact resolvent. Its restriction to \(eH\) is the selfadjoint operator \(eDe\).

Put \(f(x)=x(1+x^2)^{-1/2}\). The operator \(F_0-f(D)\) is compact by scalar spectral calculus: their eigenvalue difference tends to zero at both ends of the spectrum and is zero on the kernel. Also \(f(D_e)-f(D)\) is compact. To prove this second assertion with norm control, use

\[

f(D)=\frac2\pi\int_0^\infty

D(D^2+1+t^2)^{-1}\,dt

\]

in the strong sense. Express each integrand as half the sum of the two resolvents at \(\pm i\sqrt{1+t^2}\). Their differences for \(D_e,D\) are compact by the resolvent identity, with norm bounded by

\(\|D_e-D\|/(1+t^2)\).

The difference integral therefore converges in norm to a compact operator. Strong convergence of the individual integrals identifies it with \(f(D_e)-f(D)\).

It follows that \(eF_0e\) and \(e f(D_e)e\) differ compactly. On \(eH\) the latter is the bounded transform of \(eDe\). That restriction has compact resolvent, hence only finitely many zero eigenvalues and a gap away from zero. Its bounded transform is Fredholm, with exactly the same kernel in each grading as \(eDe\). Its index is consequently (10.10). Compact perturbation stability proves the assertion for a projection.

For an arbitrary idempotent use the path \(e_t\) from (10.9). Its range is fixed, and \(p\) preserves \(\operatorname{Dom}D\). To justify this last domain fact, apply the product commutator rule to \(1-(e-e^*)^2\). Its positive bounded inverse preserves the domain: expand that inverse in a norm-convergent Neumann series after scaling; the commutator series converges as well, since the differentiated powers have bound \(Cr^{j-1}j\), with \(r<1\). Closedness of \(D\) then gives the domain identity for the inverse and for \(p\).

The domain of each compression is the fixed space

\(pH^+\cap\operatorname{Dom}D\).

On that space,

\[

e_tD^+e_t-pD^+p

=(e_t-p)(1-p)D^+p

=(e_t-p)(1-p)[D^+,p]p,

\tag{10.12}

\]

which is bounded and norm continuous in \(t\). The graph inclusion for \(pD^+p\) is compact, because \(D_p\) has compact resolvent. Thus (10.12) is compact as a map from the fixed graph domain to \(pH^-\). All these unbounded compressions are Fredholm, with the same index as the projection compression. The bounded compressions \(e_tF_0^+e_t\) likewise have constant index: the doubled phase gives their parametrices modulo compact commutators, and they form a norm-continuous family on fixed ranges. Both indices therefore equal their values at \(p\), already proved equal. This proves (10.10) for every idempotent. \(\square\)

The degree-zero term is the finite part specified by (7.10), including the harmonic correction. Exercises 12–13 show explicitly why an ordinary positive-degree residue cannot replace it.

## 11. A formula requiring only finitely many commutators

A single unitary does not require a dimension-spectrum theorem for an entire algebra. Only the finitely many coefficient functions occurring in its Chern cycle need continuation.

Let \(D\) be selfadjoint, invertible, with compact resolvent, and let \(U\) be unitary with a bounded commutator \([D,U]\) on its preserved domain. Define the summability threshold

\[

p=\inf\{q>0:\operatorname{Tr}|D|^{-q}<\infty\}.

\]

Suppose \(p<\infty\). Choose \(q>p\) for which the trace is finite and

\(q<\lfloor p\rfloor+1\), and choose an odd integer \(N>q\).

The finitely many functions we use are

\[

Z_{k,n}(z)=\operatorname{Tr}\left(

U^{-1}[D,U]^{(k_1)}[D,U^{-1}]^{(k_2)}

\cdots[D,U]^{(k_n)}

|D|^{-n-2|k|-2z}\right).

\tag{11.1}

\]

Use odd \(n\) and \(n+|k|\leq p\). Initially these functions are defined in a right half-plane. Here \(X^{(j)}=[D^2,\cdot]^j(X)\); their graph domains are part of the commutator assumptions, as in the second lesson.

**Theorem 11.1 (finite regularity).** Suppose \(U,[D,U]\) belong to \(\operatorname{Dom}\delta^m\) for \(0\leq m\leq M\), where

\[

M=8(N+2),\qquad \delta=[|D|,\cdot].

\tag{11.2}

\]

Suppose the functions (11.1) have single-valued meromorphic continuation from their convergence region to a half-plane containing zero, with finite-order poles there. Then

\[

\begin{aligned}

\operatorname{Index}(PUP)

={}&-\sum_{\substack{n\geq1\ \mathrm{odd}\\n\leq p}}

(-1)^{(n-1)/2}\left(\frac{n-1}{2}\right)!

\mathcal R_n(U),\\

\mathcal R_n(U)

={}&\sum_{|k|\leq p-n}A_{n,k}

\sum_{\ell=0}^{m}c_{m,\ell}\,

\operatorname*{Res}_{z=0}z^\ell Z_{k,n}(z),\\

m={}&|k|+(n-1)/2,\qquad c_{m,\ell}=[z^\ell]P_m(z).

\end{aligned}

\tag{11.3}

\]

The constants \(A_{n,k}\) and the half-integer polynomial \(P_m\) are those in (5.1) and (5.7). The bound (11.2) is sufficient; it makes no claim to be minimal. No meromorphy of other algebra coefficients is assumed.

**Proof.** Work in the algebra of Laurent polynomials in \(U\). The formulas for \(U^{-1}\),

\[

[D,U^{-1}]=-U^{-1}[D,U]U^{-1},\qquad

\delta(U^{-1})=-U^{-1}\delta(U)U^{-1},

\]

and their differentiated product rules give the same finite regularity for every polynomial coefficient used. Only degrees at most \(N+3\) of the heat identities are needed.

We first check that these identities require only the stated number of commutators. Put \(d=\lfloor p\rfloor+1\), so \(q<d\leq N\).

In each odd degree \(n\leq p\), use Taylor depth \(d-n\) in (7.2). Its remainder is

\(O(u^{(d-q)/2})\), with a positive exponent.

The retained multi-indices satisfy \(n+|k|\leq d-1\), exactly \(n+|k|\leq p\).

For \(n>p\), the degree is an integer at least \(d>q\); its heat Mellin integral is already holomorphic near zero.

For this finite-regularity argument, perform the heat expansion with the remaining **total** Taylor-order budget \(R=d-n\). After a monomial prefix of total order \(K<R\), expand the next crossing only through order \(R-K-1\) and retain its exact Duhamel remainder of order \(R-K\). If a remainder occurs, leave the later coefficients and heat factors unexpanded. Thus each retained monomial has total order below \(R\), and each remainder has total coefficient order \(R\), with the later unexpanded differential factors still of order zero. This gives the same retained coefficients as (7.2), but avoids generating discarded products whose total order exceeds \(R\). The graph estimates below therefore need total positive order at most \(N\), not a separate depth \(N\) at every crossing.

Here is a bound for the finite graph estimates in this construction. On the spectral core,

\[

\nabla^j(B)=\sum_{r=0}^j\binom jr2^{j-r}

\delta^{j+r}(B)\Lambda^{j-r}.

\tag{11.4}

\]

This follows by raising the commuting operations

\(\nabla=2\delta(\cdot)\Lambda+\delta^2\) to the \(j\)-th power. Thus a Taylor coefficient or remainder with \(j\leq d-n\leq N\) uses at most \(2N\) commutators before graph conjugation. Its total positive order is at most \(N\), by the total-order construction above. In the largest-interval estimate, the absolute prefix orders and the weights moved across each coefficient are bounded by \(2N+4\), allowing for an inserted \(D\), a differentiated heat factor, and interpolation between adjacent integers. Conjugating a coefficient through such a weight uses at most \(2N+5\) additional commutators by the finite version of (2.3) in the second lesson. The same bound applies to the phase calculation: it has at most \(N+2\) differential factors, each of order between \(-1\) and \(0\). Before a heat derivative there are at most two insertions of order at most \(1\); differentiating the heat in the character instead gives its original order-one insertion and an order-two factor \(\mathcal D_sV_s+V_s\mathcal D_s\). A logarithm costs an arbitrarily small positive order, which we choose below one and within the trace-class margin. These orders fit the same \(2N+4\) bound, also when \(N=1\). A first complex-power commutator remainder, expressed through \(\nabla=2\delta(\cdot)\Lambda+\delta^2\), uses at most two further \(\delta\)-commutators. A conservative combined count is therefore \(2N+(2N+5)+2=4N+7<8(N+2)\). Finite products use the Leibniz rule, rather than multiplying these counts by their number of factors. This proves that the heat expansions, spectral-cutoff limits, insertion identities and phase integral of Sections 6–9 are valid under (11.2), without an infinite regularity assumption.

The heat Mellin evaluation in degree \(n\leq p\) now has the finite continuation, with a remainder \(\mathcal E_n\) holomorphic near zero,

\[

C_n(z)(c_n(U))

=\kappa(-1)^{(n-1)/2}\left(\frac{n-1}{2}\right)!

\sum_{n+|k|\leq p}

A_{n,k}\Gamma(n/2+|k|+z)Z_{k,n}(z)

+\mathcal E_n(z).

\tag{11.5}

\]

The tail from heat length at least one is entire by the spectral gap. The positive remainder exponent just proved gives the other holomorphic term. Thus (11.5) uses exactly the continuations assumed in the theorem.

There is a scalar way to compare its residue with the character which avoids continuation of any insertion cochain. Evaluate (8.12) on the finitely many components \(c_n(U)\), \(n\leq N\), in the original common convergence half-plane. The left side is zero. Indeed each insertion component is evaluated on

\(bc_{m+1}+Bc_{m-1}=0\), including \(bc_1=0\) at the bottom. Therefore

\[

\sum_{\substack{n\leq N\\ n\ \mathrm{odd}}}C_n(z)(c_n(U))

=\frac1z\,B\Theta_{N+1}(z)(c_N(U)).

\tag{11.6}

\]

The high insertion on the right is holomorphic near zero by the strict summability margin \(N>q\). Multiply by

\(g_{\mathrm{odd}}(z)=\Gamma(1/2)/\Gamma(1/2+z)\)

and take residues. Equations (11.5)–(11.6) show that the resulting scalar is exactly \(Q_N(D)(c_N(U))\). Lemma 9.1 identifies this character value with \(Q_N(F)(c_N(U))\): its cyclic coboundary pairs to zero, since its primitive is a \(B\)-image and \(bc_N=-Bc_{N-2}\). The proof of Theorem 10.2 makes this value, divided by \(\sqrt{2\pi i}\), minus the index. Expanding the gamma quotient by (5.7) gives (11.3). \(\square\)

If the coefficient function is instead written with exponent \(-n-2|k|-s\), denote it by \(\zeta_{k,n}(s)\). Then \(Z_{k,n}(z)=\zeta_{k,n}(2z)\), and

\[

\operatorname*{Res}_{z=0}z^\ell Z_{k,n}(z)

=2^{-\ell-1}\operatorname*{Res}_{s=0}s^\ell\zeta_{k,n}(s).

\tag{11.7}

\]

Thus the coefficient of the latter residue in (11.3) includes \(2^{-\ell-1}\). This is the same spectral-variable factor already checked on the circle in Exercise 3.

The theorem also covers a finite-dimensional kernel by replacing \(D\) with \(D+P_0\). Under finite regularity, the changed terms are finite rank with graph regularity through the orders just counted. Their traces against the small positive powers needed near zero are holomorphic there; full smoothing to every order is unnecessary. The odd positive-degree residues are therefore unchanged. When only a summability threshold is given, a strictly larger trace-class exponent \(q\) is used in the estimates. There is no need to assume a weak bound exactly at the threshold \(p\).

**Corollary 11.2 (an index requires a pole).** Under the hypotheses of Theorem 11.1, a nonzero index implies that at least one of the functions (11.1) has a nonremovable pole at zero.

**Proof.** If each is holomorphic there, every residue in (11.3) vanishes. The index would then be zero. Conversely, a pole need not produce a nonzero index: its coefficient can be absent from the finite polynomial or cancel with another term. \(\square\)

The corollary concerns the odd pairing. In an even triple the constant Laurent coefficient and harmonic space can carry an index with no pole, as Exercises 12–13 demonstrate.

## 12. Geometric index formulas

The abstract residue formula now has its analytic and algebraic proofs. Continue with Geometric Dirac operators and their index formulas, after the symbol calculus and closed-domain estimates needed for that specialization.

## 13. Exercises with complete solutions

**Exercise 1 (basic).** For \(u(x)=e^{-3ix}\), identify the kernel and cokernel of the positive compression and evaluate the residue in (2.2).

**Solution.** The kernel is the span of \(e_0,e_1,e_2\); the range is all of \(PH\). The index is three. The commutator coefficient \(u^{-1}(-iu')\) is \(-3\), so the residue is \(-3\), and its negative is three.

**Exercise 2 (intermediate).** Let \(u(x)=\exp(i(2x+\sin x+\tfrac12\sin2x))\). Compute its index without solving the compressed operator's kernel equation.

**Solution.** Here \(m=2\) and \(f(x)=\sin x+\tfrac12\sin2x\) is periodic. The homotopy in Theorem 2.1 reduces the index to that of multiplication by \(e^{2ix}\), namely \(-2\). Direct integration gives the same result, since \(u^{-1}u'=i(2+\cos x+\cos2x)\), whose integral is \(4\pi i\).

**Exercise 3 (intermediate).** Replace \(-1-2z\) in (2.2) by \(-1-z\). What coefficient must precede the new residue?

**Solution.** The sum of the two Hurwitz zeta functions now has residue two at zero. Thus the new residue is \(2m\). The index is \(-\tfrac12\) times that residue. Both the sign and the factor are required.

**Exercise 4 (advanced).** Suppose \(p=3\). List the multi-indices that can contribute to odd degrees one and three through the bound in (3.2).

**Solution.** At degree one, \(k=(k_1)\) may have \(k_1=0,1,2\). At degree three, \(k=(0,0,0)\) is the only possibility. All odd degrees at least five vanish by order. This lists potentially contributing operator terms; finite pole multiplicity or a polynomial gamma normalization may further limit which Laurent coefficients occur.

**Exercise 5 (intermediate).** Compute every coefficient of the degree-one term \(k=(2)\) in (5.7).

**Solution.** Here \(\beta_k=3\), \(k!=2\), so \(A_{1,(2)}=1/6\). The polynomial is

\[

P_2(z)=(z+1/2)(z+3/2)=z^2+2z+3/4.

\]

Thus, after removal of \(\sqrt{2\pi i}\), the term is

\[

\frac18\tau_0(T_{1,(2)})

+\frac13\tau_1(T_{1,(2)})

+\frac16\tau_2(T_{1,(2)}).

\]

In particular, the last coefficient is \(1/6\), since the coefficient of \(z^2\) in \(P_2\) is already one. Dividing it again by \(2!\) would give a different expression.

**Exercise 6 (advanced).** Under the hypotheses of Lemma 4.1, write an explicit coboundary whose differential is \(\Phi_g-\Phi_1\), for \(g(0)=1\).

**Solution.** Subtract (4.3) for \(g\) and for \(1\). The difference is

\[

\Phi_g-\Phi_1=-d\,\operatorname{FP}_{z=0}((g(z)-1)J(z)).

\]

Thus \(-\operatorname{FP}((g-1)J)\) is the required transgression cochain. If \(J\) is holomorphic at zero, this finite part vanishes because \(g(0)-1=0\). If \(J\) has poles, its principal coefficients can contribute; they are still an explicit coboundary.

**Exercise 7 (advanced).** Suppose the even degree-zero zeta function has expansion

\(h_a^\gamma(z)=2z^{-2}-3z^{-1}+5+7z+O(z^2)\).

Find its converted degree-zero value and explain why the double pole does not change that value.

**Solution.** The conversion is multiplication by \(1/z\), followed by taking the residue. Hence

\[

z^{-1}h_a^\gamma(z)=2z^{-3}-3z^{-2}+5z^{-1}+7+O(z),

\]

whose residue is five. The double and simple poles move to powers \(z^{-3}\) and \(z^{-2}\), so neither contributes to the residue. The constant coefficient of the original function is exactly the needed term.

**Exercise 8 (intermediate).** For \(w_1=(U^{-1},U)\) and \(w_3=(U^{-1},U,U^{-1},U)\), compute \(Bw_1\) and \(bw_3\) in normalized tensors. Determine the coefficient of \(w_3\) if the coefficient of \(w_1\) is one.

**Solution.** The normalized formulas give

\[

Bw_1=(1,U^{-1},U)-(1,U,U^{-1}).

\]

In \(bw_3\), the two interior mergers create an internal \(1\) and vanish. Its endpoint mergers give exactly the same displayed difference. Thus \(bw_3=Bw_1\), and the next coefficient must be minus one to give \(bc_3+Bc_1=0\). Repeating the count gives the factorial coefficients of (6.4).

**Exercise 9 (intermediate).** Verify the even Chern cycle identity between degrees two and four, including the coefficients and the shift \(e-\tfrac12\).

**Solution.** Write \(w_2=(e-\tfrac12,e,e)\), \(w_4=(e-\tfrac12,e,e,e,e)\). Proposition 6.2 gives

\[

Bw_2=3(1,e,e,e),\qquad

bw_4=\tfrac12(1,e,e,e).

\]

The coefficients in (6.5) are \(-2\) and \(12\). Hence

\[

B(-2w_2)+b(12w_4)=(-6+6)(1,e,e,e)=0.

\]

Omitting the half shift changes the endpoint-merger calculation and loses the factor \(1/2\).

**Exercise 10 (advanced).** Suppose \(p=3\) and \(n=1\) in Lemma 7.1. Choose a Taylor depth whose Mellin remainder is holomorphic near zero, and specify the terms which can have nonzero residues.

**Solution.** Choose \(N=3\). The remainder is \(O(u^{(1+3-3)/2})=O(u^{1/2})\), so its integral against \(u^{z-1}\), including any logarithmic parameter derivative, is holomorphic for \(\operatorname{Re}z>-1/2\). The retained terms have \(k=0,1,2\). These are exactly the possible terms from \(1+k\leq3\); all deeper terms have trace-class order at zero and zero residue.

**Exercise 11 (advanced).** Explain why the correction in (8.5) is needed at its top degree. Could one replace its lower integration endpoint \(0\) by \(\infty\) and expect the same class?

**Solution.** The naive truncation leaves

\(bH_N=-BH_{N+2}\), so it is not closed at the top. Integrating the transgression from zero gives

\[

b\int_0^t\Psi_{N+1}

=-H_{N+2}(t)-B\int_0^t\Psi_{N+3},

\]

since \(H_{N+2}(0)=0\). The correction \(+B\int_0^t\Psi_{N+1}\) therefore cancels the defect.

If instead one uses \(H_N-B\int_t^\infty\Psi_{N+1}\), the result is also closed, but it is a coboundary. Its derivative is again minus the finite differential of \(\Psi_{\leq N-1}\), and its limit at infinity is zero. Thus it equals

\((b+B)\int_t^\infty\Psi_{\leq N-1}\).

The zero endpoint in (8.5) retains the finite heat character, whose large-\(t\) limit is (8.7).

**Exercise 12 (intermediate).** On \(H=\mathbb C^2\) let

\[

\gamma=\begin{pmatrix}1&0\\0&-1\end{pmatrix},

\qquad D=\begin{pmatrix}0&1\\1&0\end{pmatrix},

\]

and let the algebra of diagonal matrices act on \(H\). Compute the even residue cocycle on \(a=\operatorname{diag}(2,5)\), and its evaluation on the idempotent \(e=\operatorname{diag}(1,0)\).

**Solution.** All regularity conditions hold in finite dimension and \(|D|=I\). Every positive-degree coefficient zeta function is entire, and its gamma factor is holomorphic at zero, so every positive-degree residue vanishes. The degree-zero conversion gives

\[

\Phi'_0(a)=\operatorname{Tr}(\gamma a)=-3,

\qquad \Phi'_0(e)=1.

\]

It is a trace on the diagonal algebra and hence a degree-zero cyclic cocycle. The compression \(eD^+e:eH^+\to eH^-\) has a one-dimensional domain and zero-dimensional codomain, so its index is one. Thus the constant Laurent coefficient carries an index even though none of the coefficient zeta functions has a pole.

**Exercise 13 (intermediate).** Let \(H^+=\mathbb C\), \(H^-=0\), \(A=\mathbb C\), and \(D=0\). Compute the completed even cocycle, and compare it with the rule which discards the kernel.

**Solution.** Here \(P_0=I\), \(\Lambda=I\), and every commutator is zero. The completed cocycle has only degree zero,

\(\Phi'_0(a)=a\).

The operator \(D^+:H^+\to H^-\) has one-dimensional kernel and zero cokernel, so its index is one, equal to \(\Phi'_0(1)\). Discarding the kernel gives the zero zeta function and zero finite part. The correction in Corollary 7.3 is \(\operatorname{Tr}(\gamma aP_0)=a\), which restores the required value.

**Exercise 14 (advanced).** In the phase estimate (9.12), compute the final exponent for the character and for its primitive. Explain why using only the changing summability dimension \(p/(1-s)\) would miss the endpoint.

**Solution.** The character has \(N+1\) differentials of order \(-s\) and one insertion of order \(1-s\), giving total order \(1-s(N+2)\). Integration subtracts \((N+2)(1-s)\), so the final exponent is \(-N-1\). The primitive has \(N\) differentials and two insertions of order \(1-s\), with a logarithm bounded by order \(\varepsilon\), giving \(2-s(N+2)+\varepsilon\). Its final exponent is \(-N+\varepsilon<-p\). Both are uniform in \(s\). The dimension \(p/(1-s)\) diverges as \(s\to1\), but it disregards the increasingly negative order of the commutators. At \(s=1\) those products remain trace class even though the heat alone is a scalar multiple of the identity.

**Exercise 15 (intermediate).** On \(H=\mathbb C^2\), let \(P=\operatorname{diag}(1,0)\), and let \(Q\) project onto \((\cos\theta,\sin\theta)\), where \(0<\theta<\pi/2\). Compute the eigenvalues of \(P-Q\), its odd-power traces, and the index of \(QP:PH\to QH\).

**Solution.** The matrix is

\[

P-Q=\begin{pmatrix}

\sin^2\theta&-\sin\theta\cos\theta\\

-\sin\theta\cos\theta&-\sin^2\theta

\end{pmatrix}.

\]

Its square is \(\sin^2\theta\,I\), and its trace is zero. Its eigenvalues are therefore \(\sin\theta\) and \(-\sin\theta\), so every odd-power trace is zero. The map \(QP\) sends \((1,0)\) to \(\cos\theta(\cos\theta,\sin\theta)\) and is an isomorphism of one-dimensional spaces. Its index is zero, in agreement with Lemma 10.1.

**Exercise 16 (advanced).** Let \(e=\left(\begin{smallmatrix}1&2\\0&0\end{smallmatrix}\right)\). Compute the projection and the idempotent path in (10.9), and check why their ranges are fixed.

**Solution.** Here \(e-e^*=\left(\begin{smallmatrix}0&2\\-2&0\end{smallmatrix}\right)\), so \(1-(e-e^*)^2=5I\) and \(ee^*=\operatorname{diag}(5,0)\). Thus \(p=\operatorname{diag}(1,0)\), and

\[

e_t=\begin{pmatrix}1&2(1-t)\\0&0\end{pmatrix}.

\]

Squaring returns \(e_t\); its range is the first coordinate line for every \(t\). This fixed range permits the index-stability argument on fixed domain and codomain Hilbert spaces.

**Exercise 17 (advanced).** Suppose \(Z(z)=a_{-3}z^{-3}+a_{-2}z^{-2}+a_{-1}z^{-1}+O(1)\), and \(Z(z)=\zeta(2z)\). Express the coefficients in terms of the Laurent coefficients of \(\zeta\), and verify (11.7) for \(\ell=2\).

**Solution.** If \(\zeta(s)=b_{-3}s^{-3}+b_{-2}s^{-2}+b_{-1}s^{-1}+O(1)\), then

\(a_{-3}=b_{-3}/8\), \(a_{-2}=b_{-2}/4\), \(a_{-1}=b_{-1}/2\).

Hence \(\operatorname{Res}z^2Z(z)=b_{-3}/8

=2^{-3}\operatorname{Res}s^2\zeta(s)\), exactly the coefficient \(2^{-\ell-1}\). The spectral-variable correction depends on the Laurent order; a single factor of two would not correct all higher residues.

**Exercise 18 (advanced).** Double the one-dimensional harmonic example of Exercise 13. Compute the unitized degree-zero residue and the bounded degree-two character. Check their values on the external Chern cycle of \((1,0)\).

**Solution.** The doubled grading and phase are

\(\widetilde\gamma=\operatorname{diag}(1,-1)\) and

\(\widetilde F=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).

The unitized representation is

\(\rho(a,\lambda)=\operatorname{diag}(a+\lambda,\lambda)\).

Its degree-zero residue is \(a\), equal to

\(\pi^*(a)-\varepsilon(a,\lambda)\), as in (9.20).

For \(x_j=(a_j,\lambda_j)\), the commutator with the phase is \(a_jJ\), where

\[

J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J^2=-1.

\]

Since the coefficient in degree two is \(1/2\), (9.13) gives

\[

\operatorname{Ch}_{\widetilde F,2}(x_0,x_1,x_2)

=-\tfrac12a_0a_1a_2.

\]

Put \(E=(1,0)\), and recall that the external unit is \(I=(0,1)\). The degree-two cycle is \(-2(E-I/2,E,E)\), so the character value is \(-2(-1/2)=1\). The degree-zero residue on \(E\) is also one. Restricting this cyclic character to the original scalar algebra gives an unnormalized cyclic cochain; its original internal unit differs from the external unit. Lemma 9.3 performs this class extraction, rather than deleting that distinction.

**Exercise 19 (advanced).** Suppose the summability threshold in Section 11 is \(p=2.4\), and choose a trace-class exponent \(q=2.7\). Give one sufficient regularity bound and expand the finite index formula.

**Solution.** Here \(d=3\), and one may take \(N=3\), hence \(M=40\). The only odd degree at most \(p\) is one, with \(k=0,1\).

For \(k=0\), \(A_{1,0}=1\) and \(P_0=1\). For \(k=1\), \(A_{1,1}=-1/2\) and \(P_1=z+1/2\). Formula (11.3) becomes

\[

\operatorname{Index}(PUP)

=-\operatorname{Res}Z_{0,1}

+\tfrac14\operatorname{Res}Z_{1,1}

+\tfrac12\operatorname{Res}zZ_{1,1},

\]

with all residues at zero. The Taylor depth in degree one is two; its remainder exponent is \((3-2.7)/2=0.15>0\). This strict margin justifies the local Mellin continuation even without a weak summability estimate exactly at \(2.4\).

## References

- [Connes–Moscovici 1995] Alain Connes and Henri Moscovici, *The local index formula in noncommutative geometry*, Geometric and Functional Analysis 5 (1995), 174–243; [IHÉS preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_19/M_95_19.pdf).

- [Carey–Phillips–Rennie–Sukochev 2006] Alan L. Carey, John Phillips, Adam Rennie, and Fedor A. Sukochev, *The local index formula in semifinite von Neumann algebras I: spectral flow*, Advances in Mathematics 202 (2006), 451–516; [open preprint](https://arxiv.org/abs/math/0411019).

- [Jaffe–Lesniewski–Osterwalder 1988] Arthur Jaffe, Andrzej Lesniewski, and Konrad Osterwalder, *Quantum K-theory I. The Chern character*, Communications in Mathematical Physics 118 (1988), 1–14; [journal archive](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-118/issue-1/Quantum-K-theory-I-The-Chern-character/cmp/1104161905.full).

- [Higson 2006] Nigel Higson, *The residue index theorem of Connes and Moscovici*, in Nigel Higson and John Roe (eds.), *Surveys in Noncommutative Geometry*, Clay Mathematics Proceedings 6, American Mathematical Society, 2006, 71–126; [publisher edition](https://www.claymath.org/wp-content/uploads/2022/03/cmip06.pdf).

- [Ponge 2003] Raphaël Ponge, *A new short proof of the local index formula and some of its applications*, Communications in Mathematical Physics 241 (2003), 215–234; [open author preprint](https://arxiv.org/abs/math/0211333).

- Higher traces Open Mathematics Courses, *Cyclic cohomology: traces, differentials and symmetry*, draft lesson, September 2026, Sections 1, 3 and 6–9 (CC0).

- Measured foliation index Open Mathematics Courses, *The index theorem for measured foliations*, draft lesson, September 2026, Lemmas 6.24–6.25 and Theorem 6.26 (CC0).


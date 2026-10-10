# Traces, states and the pairing with K-theory

*Written by GPT-6.1 Sol (OpenAI), October 2026, at Ultra. Public domain (CC0).*

Independently authored CC0 lesson; self-checked by the writing AI.

A projection describes a finite projective module. A trace assigns it a numerical size. The size can distinguish ordered K-classes, recover the normalized rank in an inductive limit, and compute a Fredholm index from the two errors of a parametrix. For an unbounded trace, its finite domain is part of the construction: the numerical expression must survive the relations defining K-theory.

We use projections and stable equivalence from Lessons 1 and 3, external unitization from Lesson 4, and matrix stability and sequential continuity from [Lesson 5, Theorems 1.1 and 3.3](KT-OPK-05.md). The index boundary and its sign come from [Lesson 7, Proposition 5.1 and Theorem 6.1](KT-OPK-07.md#5-the-partial-isometry-formula); the extension sequence is the one proved in [Lesson 11, Theorem 2.1](KT-OPK-11.md#2-exactness-at-all-six-groups). Matrix traces are always unnormalized. The unbounded-trace construction uses the written finite-domain, Hilbert-algebra and trace-integration lessons of Modular Theory and Weights; §6 states their exact interfaces and verifies the coefficient and convolution applications.

## 1. A bounded trace measures a K-class

A **bounded positive trace** on a C*-algebra \(A\) is a bounded linear functional \(\tau:A\to\mathbb C\) such that \(\tau(a^*a)\geq0\) and \(\tau(ab)=\tau(ba)\). Positivity gives \(\tau(a^*)=\overline{\tau(a)}\). On matrices put

\[
\tau_n((a_{ij}))=\sum_{i=1}^n\tau(a_{ii}).
\tag{1.1}
\]

The matrix index in this notation records the size, without dividing by it. Multiplication gives

\[
\begin{gathered}
\tau_n(XY)=\sum_{i,j}\tau(x_{ij}y_{ji}),\\
\tau_n(XY)=\tau_n(YX),\\
\tau_n(X^*X)=\sum_{i,j}\tau(x_{ji}^*x_{ji})\geq0.
\end{gathered}
\tag{1.2}
\]

The same calculation applies to rectangular matrices, with the appropriate trace on each product. Block sum adds values, and adding a zero block preserves a value.

**Theorem 1.1 (bounded trace pairing).** There is a homomorphism

\[
\tau_*:K_0(A)\longrightarrow\mathbb R.
\tag{1.3}
\]

For unital \(A\), it sends \([p]-[q]\) to \(\tau_n(p)-\tau_m(q)\). For every \(A\), it is nonnegative on classes represented by projections over \(A\). If \(A\) is unital and \(\tau(1)=1\), then \(\tau_*[1]=1\).

*Proof.* If \(v^*v=p\) and \(vv^*=q\), the rectangular version of (1.2) gives equal values for \(p,q\). Thus the value is constant on stable Murray–von Neumann classes. It is also constant on projection homotopies: sufficiently close projections are unitarily equivalent, by Lesson 1, and a compact parameter interval has a finite subdivision into such close pairs. Additivity therefore gives a monoid homomorphism on \(V(A)\), which extends uniquely to its Grothendieck group when \(A\) is unital.

For a nonunital algebra, let \(A^+=A\oplus\mathbb C\) be its external unitization, with scalar quotient \(\epsilon\). Extend the *linear* trace by

\[
\tau^0(a+\lambda1)=\tau(a).
\tag{1.4}
\]

This is bounded and tracial: the nonscalar part of the commutator of \(a+\lambda1,b+\mu1\) is \(ab-ba\). This extension need not be positive. The preceding invariance and group-completion argument only needs a tracial linear functional, so it gives a map on \(K_0(A^+)\). Restrict it to \(\ker\epsilon_*=K_0(A)\). In the normalized relative form from Lesson 4, its value is

\[
\begin{gathered}
\tau_*([e]-[P])=\tau_n(e-P),\\
P=\epsilon_n(e),\quad e-P\in M_n(A).
\end{gathered}
\tag{1.5}
\]

The scalar projection \(P\) is regarded as a matrix over \(A^+\). Identity padding cancels between the two terms, so the expression agrees with all relative relations. A projection \(p\in M_n(A)\) has value \(\tau_n(p)\geq0\). The unital assertion follows by evaluating its unit. For a unital algebra viewed through external unitization, this agrees with its original Grothendieck pairing. \(\square\)

For a *-homomorphism \(\varphi:A\to D\) and bounded trace \(\rho\) on \(D\), entrywise evaluation proves

\[
(\rho\circ\varphi)_*=\rho_*\circ\varphi_*.
\tag{1.6}
\]

The corner map \(a\mapsto\operatorname{diag}(a,0)\) preserves the value. A normalized trace on each changing matrix size would instead change that value, destroying this compatibility. The degree-zero construction agrees with [Cyclic forms that survive norm completion, §4, Theorem 4.3, degree-zero paragraph](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-CYCLIC/public/reader/n-traces.html#4-the-form-reaches-k-theory). Its boundedness condition is explicit there.

## 2. The cone, the unit and group states

Define \(K_0(A)^+\) to be the image of \(V(A)\) in \(K_0(A)\). This cone contains zero and is closed under addition. For unital \(A\), it generates the group. Write \(x\leq y\) when \(y-x\) lies in the cone.

A unital algebra is **stably finite** if every isometry in every \(M_n(A)\) is unitary. This implies finiteness of every matrix projection: if \(v^*v=P\) and \(vv^*=R\leq P\), then \(v\) lies in the corner \(PM_n(A)P\). The element \(v+(1-P)\) is an isometry, so is unitary. Its range projection is \(R+(1-P)\); hence \(R=P\).

**Theorem 2.1 (order).** If \(A\) is unital and stably finite, then

\[
K_0(A)^+\cap(-K_0(A)^+)=\{0\}.
\tag{2.1}
\]

Consequently the cone defines an ordered abelian group, with order unit \([1]\).

*Proof.* Suppose \(x=[p]\) and \(-x=[q]\), with projections over \(A\). The equality \([p]+[q]=0\) in the Grothendieck group supplies a projection \(r\) such that \(p\oplus q\oplus r\) is stably equivalent to \(r\). In a common enlarged matrix algebra, write

\[
\begin{gathered}
P=p\oplus q\oplus r,\\
R=0\oplus0\oplus r\leq P.
\end{gathered}
\tag{2.2}
\]

Equivalence supplies \(v^*v=P,vv^*=R\). Finiteness of \(P\) gives \(P=R\), forcing \(p=q=0\). Thus \(x=0\). This argument uses the stabilizing \(r\); it does not require cancellation of projection classes.

If \(x=[p]-[q]\), where \(p\in M_n(A)\), \(q\in M_m(A)\), their complementary projections give

\[
-m[1]\leq x\leq n[1].
\tag{2.3}
\]

These bounds prove the order-unit assertion. \(\square\)

A **state of the ordered group** is an additive map \(\sigma:K_0(A)\to\mathbb R\) which is nonnegative on \(K_0(A)^+\) and satisfies \(\sigma[1]=1\). Theorem 1.1 associates such a state to every tracial state. The inequalities (2.3) show that each value of a group state is bounded by an integer depending on the class.

The unital qualification matters. For \(A=C_0(\mathbb R^2)\), the group is \(\mathbb Z\) by Lesson 10, but there is no nonzero matrix projection over \(A\): its continuous rank is constant on the connected plane, while vanishing at infinity makes that rank zero outside a compact set. Thus \(K_0(A)^+=0\), which does not generate the group. This is the distinction in [Blackadar 1998, §6.3.1].

## 3. AF traces are exactly the group states

For a finite-dimensional algebra \(D=\bigoplus_{j=1}^rM_{d_j}(\mathbb C)\), use minimal projections as the basis of \(K_0(D)=\mathbb Z^r\). Its positive cone is \(\mathbb N^r\) and its unit is \((d_1,\ldots,d_r)\). A trace on \(D\) has the form

\[
\begin{gathered}
\tau(x)=\sum_jc_j\operatorname{Tr}(x_j),\\
c_j\geq0.
\end{gathered}
\tag{3.1}
\]

Indeed, the matrix-unit identity \(\tau(e_{ab})=\tau(e_{a1}e_{1b})=\delta_{ab}\tau(e_{11})\) determines each summand. It is a state precisely when \(\sum_jd_jc_j=1\). These are exactly the conditions on a positive homomorphism \(\mathbb Z^r\to\mathbb R\) normalized at the unit. Thus a finite-dimensional group state determines a unique trace, with the same coefficients.

Let \(A=\overline{\bigcup_kD_k}\) be a unital AF-algebra, with an increasing generating sequence of finite-dimensional subalgebras. We may arrange \(1_A\in D_k\) throughout. To see this, choose a stage containing an element \(a\) with \(\|a-1\|<1\). If the unit \(p\) of that stage were different from \(1\), then \((1-p)(1-a)=1-p\), contradicting this estimate. All later stages contain the common unit; discard the earlier ones.

We import [AF-algebras, §10, Theorem 10.4(3)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-09): traces on \(A\) are the projective limit of the finite-stage trace simplices. In coordinates, if \(\alpha_k\) is the multiplicity matrix of \(D_k\subset D_{k+1}\), compatibility is \(c^{(k)}=\alpha_k^Tc^{(k+1)}\). A compatible sequence of normalized positive stage traces has a unique bounded positive tracial extension to \(A\).

The cone here is proper directly by K-theory continuity. If \(x\) and \(-x\) are positive, represent them at a common finite stage. Their sum becomes zero at a later stage; in that stage's \(\mathbb Z^r\), two nonnegative vectors with zero sum are both zero. Hence \(x=0\). The unit bounds are (2.3).

**Theorem 3.1 (AF correspondence).** The map from \(T(A)\) to \(S(K_0(A),K_0(A)^+,[1])\),

\[
\tau\longmapsto\tau_*,
\tag{3.2}
\]

is an affine bijection for every unital AF-algebra with such a generating sequence.

*Proof.* Given a group state \(\sigma\), pull it back along \(K_0(D_k)\to K_0(A)\). The resulting positive normalized homomorphism supplies a unique stage trace \(\tau_k\) by (3.1). Pullback along the next inclusion preserves the group state, so uniqueness on \(D_k\) shows \(\tau_{k+1}|_{D_k}=\tau_k\). The imported projective-limit theorem supplies \(\tau\in T(A)\).

Every class of \(K_0(A)\) comes from a finite stage by Lesson 5, Theorem 3.3. On that stage, \(\tau_*\) and \(\sigma\) agree on the minimal-projection basis, hence on the class. Thus \(\tau_*=\sigma\). Conversely, if two traces give the same group state, their values on all stage minimal projections agree. Formula (3.1) makes their stage restrictions equal; boundedness and density make the traces equal on \(A\). These arguments prove both inverse identities. The constructions preserve convex combinations, giving affinity. No injectivity of the stage maps on K-theory is needed. \(\square\)

For \(M_n\oplus M_m\), all tracial states are

\[
\begin{gathered}
\tau(x,y)=\frac{w}{n}\operatorname{Tr}(x)\\
\qquad{}+\frac{1-w}{m}\operatorname{Tr}(y),\\
0\leq w\leq1.
\end{gathered}
\tag{3.3}
\]

On \(K_0=\mathbb Z^2\), the value at \((a,b)\) is \(wa/n+(1-w)b/m\). In particular the unit \((n,m)\) has value one.

For \(A_n=\varinjlim(M_{n^k},x\mapsto x\otimes1_n)\), \(n\geq2\), normalized traces are compatible and are the only possible stage restrictions of a tracial state. The trace is therefore unique. Lesson 5, Proposition 5.1 identifies its ordered K-group with \((\mathbb Z[1/n],\mathbb Z[1/n]_+,1)\), and its pairing is the inclusion into \(\mathbb R\). The trace values of projections *in \(A_n\)* are exactly

\[
\mathbb Z[1/n]\cap[0,1].
\tag{3.4}
\]

For necessity, positivity applied to \(p\) and \(1-p\) gives both bounds. For sufficiency, \(r/n^k\) in this interval is realized by a rank-\(r\) projection in \(M_{n^k}\). Matrix projections over \(A_n\) instead realize every nonnegative element of \(\mathbb Z[1/n]\).

Finally, for compact \(X\) and a probability measure \(\mu\), let \(\tau(f)=\int_Xf\,d\mu\). Under the bundle–projection correspondence,

\[
\begin{gathered}
\tau_*([E]-[F])\\
=\int_X\bigl(\operatorname{rank}E_x-\operatorname{rank}F_x\bigr)\,d\mu(x).
\end{gathered}
\tag{3.5}
\]

This follows because the ordinary matrix trace of an orthogonal projection equals its rank at each point. On connected \(X\), the integrand is constant; the pairing is the virtual rank and vanishes on reduced K-theory. Distinct probability measures on the circle give distinct traces but the same rank state. The AF bijection is therefore a special result, not a general injectivity assertion.

## 4. The trace of the two parametrix errors

An operator \(K:H_1\to H_0\) is **trace class** when its singular values have finite sum; this sum is its trace norm \(\|K\|_1\). We import the trace ideal, finite-rank approximation and multiplier estimate from [Cyclic forms that survive norm completion, §7, Lemma 7.3a](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-CYCLIC/public/reader/n-traces.html#7-geometric-and-operator-examples). The rectangular versions follow by placing the operator in an off-diagonal corner of \(H_0\oplus H_1\). In particular bounded multipliers preserve trace class, with

\[
\|XKY\|_1\leq\|X\|\|K\|_1\|Y\|.
\tag{4.1}
\]

Here is the precise cyclicity needed below. If \(E:H_1\to H_0\) is trace class and \(T:H_0\to H_1\) is bounded, then

\[
\operatorname{Tr}_{H_0}(ET)=\operatorname{Tr}_{H_1}(TE).
\tag{4.2}
\]

For a rank-one \(E\), expand either trace in an orthonormal basis; completeness gives the same inner product on both sides. Sum this calculation for a finite-rank \(E\). Finite-rank approximation in trace norm, (4.1), and \(|\operatorname{Tr}K|\leq\|K\|_1\) pass the equality to the limit. This also shows that the trace is independent of a basis: the finite-rank trace is the ordinary finite-dimensional trace on a finite-dimensional space containing its range and the range of its adjoint, and its continuous extension is unique. No cyclic rearrangement of two merely bounded operators is being used.

**Theorem 4.1 (Calderón–Fedosov).** Let \(T:H_0\to H_1\) be a bounded Fredholm operator, and \(S:H_1\to H_0\) a bounded parametrix, so that \(a=1-ST\), \(b=1-TS\) are compact. If, for an integer \(m\geq1\), \(a^m\) and \(b^m\) are trace class, then

\[
\operatorname{Index}T
=\operatorname{Tr}_{H_0}(a^m)
-\operatorname{Tr}_{H_1}(b^m).
\tag{4.3}
\]

*Proof.* Fredholmness gives closed range and finite-dimensional kernel and cokernel. Let \(P_0,P_1\) project onto \(\ker T,\ker T^*\). Restricting \(T\) to \((\ker T)^\perp\) gives a bounded bijection onto its closed range; its inverse is bounded by the bounded inverse theorem. Extend that inverse by zero on \(\ker T^*\), obtaining \(R:H_1\to H_0\) with

\[
RT=1-P_0,\qquad TR=1-P_1.
\tag{4.4}
\]

First suppose \(m=1\). Put \(E=S-R\). Then

\[
ET=P_0-a,\qquad TE=P_1-b.
\tag{4.5}
\]

Both are trace class. More particularly,

\[
E=(ET)R+EP_1
\tag{4.6}
\]

because \(TR=1-P_1\). Its first term is trace class by (4.1), and its second is finite rank. Thus \(E\) is rectangular trace class, and (4.2) applies. Taking the difference of the traces in (4.5) gives

\[
\begin{gathered}
\operatorname{Tr}(a)-\operatorname{Tr}(b)\\
=\dim\ker T-\dim\ker T^*.
\end{gathered}
\tag{4.7}
\]

For general \(m\), the identities \(aS=Sb\) and a finite geometric sum give a new parametrix

\[
\begin{gathered}
S_m=(1+a+\cdots+a^{m-1})S\\
=S(1+b+\cdots+b^{m-1}),\\
1-S_mT=a^m,\\
1-TS_m=b^m.
\end{gathered}
\tag{4.8}
\]

For example, \(S_mT=(1+a+\cdots+a^{m-1})(1-a)=1-a^m\); the other product is identical with \(b\). The first-power proof applied to \(S_m\) now proves (4.3). At no point in this reduction were \(a\) or \(b\) individually assumed trace class. \(\square\)

If \(L\) is the unilateral shift and \(S=L^*\), then \(1-SL=0\) and \(1-LS\) is its rank-one cokernel projection. Formula (4.3) gives \(\operatorname{Index}L=-1\) for every \(m\), agreeing with Lesson 7's boundary sign.

**Lemma 4.2 (circle trace calibration).** Let \(P_+\) project onto the nonnegative Fourier modes in \(L^2(\mathbb T)\). For smooth functions \(f,g\), the commutator \([P_+,M_f]\) is trace class and

\[
\begin{gathered}
\operatorname{Tr}\bigl(M_g[P_+,M_f]\bigr)\\
=\frac1{2\pi i}\int_{\mathbb T}g\,df.
\end{gathered}
\tag{4.11}
\]

*Proof.* Orient the circle by increasing \(\theta\) in \(z=e^{i\theta}\), and write \(e_j(z)=z^j\). For an integer \(k\), \([P_+,M_{z^k}]\) has rank \(|k|\) and trace norm \(|k|\). Its nonzero actions cross the boundary between negative and nonnegative modes, with sign positive for \(k>0\) and negative for \(k<0\). The trace of \(M_{z^l}[P_+,M_{z^k}]\) is zero unless \(l=-k\), and is \(k\) in that case: exactly \(|k|\) basis vectors return to themselves, with that sign. The smooth Fourier series \(f=\sum f_kz^k\), \(g=\sum g_lz^l\) have \(\sum|k f_k|<\infty\) and \(\sum|g_l|<\infty\). Thus both the operator series and its trace converge absolutely in trace norm, giving \(\sum_k k f_kg_{-k}\). Termwise differentiation and integration give the right side of (4.11). \(\square\)

For nonvanishing \(f\), set \(g=1/f\). The integral is its winding number, and [Lesson 9's scalar Toeplitz index theorem](KT-OPK-09.md) says that its negative is \(\operatorname{Index}T_f\). In particular \(M_{\bar z}[P_+,M_z]\) is the rank-one projection onto \(e_{-1}\), with trace \(+1\). Equivalently, the continuous integral kernel of \([P_+,M_f]\), against normalized circle measure, is

\[
\begin{gathered}
k_f(z,w)=w\frac{f(z)-f(w)}{z-w},\\
z\ne w,\\
k_f(e^{i\theta},e^{i\theta})\\
=-i\frac{d}{d\theta}f(e^{i\theta}).
\end{gathered}
\tag{4.12}
\]

For a Laurent monomial this follows from its finite Fourier-mode action; smooth Fourier convergence gives the formula generally. The factor \(w\) and the angular sign are fixed by the check \(f=z\).

The related projection-pair identity is stated exactly in [The local index formula, §10, Lemma 10.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-LOCAL-INDEX/the-local-index-formula.html#10-computing-the-pairing-by-finite-defects): if orthogonal projections \(P,Q\) have compact difference and \((P-Q)^{2j+1}\) is trace class, \(j\geq0\), then \(QP:PH\to QH\) is Fredholm with index \(\operatorname{Tr}(P-Q)^{2j+1}\). We cite that result; Theorem 4.1 above proves the parametrix formula independently.

For an extension \(0\to J\to D\to Q\to0\), suppose a unitary \(u\) has a partial-isometry lift \(v\) with defect projections in the ideal. Lesson 7 gives

\[
\partial[u]=[1-v^*v]-[1-vv^*].
\tag{4.9}
\]

Whenever a trace pairing on \(K_0(J)\) is defined and agrees with the finite values on these projections, its numerical boundary is

\[
\begin{gathered}
\tau_*\partial[u]\\
=\tau(1-v^*v)-\tau(1-vv^*).
\end{gathered}
\tag{4.10}
\]

For the compact-operator ideal and the ordinary trace, these are the dimensions of the kernel and cokernel. For a general semifinite trace, finiteness of these two numbers supplies a numerical expression; the domain argument in the next section is what makes it a pairing on the entire ideal's K-group.

## 5. A finite domain for an unbounded trace

A positive trace weight \(\tau:A_+\to[0,\infty]\) is additive, positively homogeneous and satisfies \(\tau(x^*x)=\tau(xx^*)\). It is **lower semicontinuous** if each sublevel set is norm closed. Its finite-trace linear domain is

\[
\begin{gathered}
\mathcal M_\tau\\
=\operatorname{span}\{a\in A_+:\tau(a)<\infty\}.
\end{gathered}
\tag{5.1}
\]

**Lemma 5.0 (the finite trace ideal).** Put

\[
\mathcal N_\tau=\{x\in A:\tau(x^*x)<\infty\}.
\tag{5.0a}
\]

Then \(\mathcal N_\tau\) and \(\mathcal M_\tau\) are two-sided *-ideals. The weight has a unique positive complex-linear extension to \(\mathcal M_\tau\), and

\[
\begin{gathered}
\tau(xy)=\tau(yx),\\
x\in\mathcal M_\tau,\quad y\in A^+.
\end{gathered}
\tag{5.2}
\]

Here \(A^+\) is the external unitization; no finite weight is assigned to its new unit.

*Proof.* The general weight argument is proved in [Finite domains and the GNS space of a C*-weight, “The algebra of finite elements”, (CS.1)–(CS.3)](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/OA-MOD-CS.html#the-algebra-of-finite-elements). It gives a linear left ideal \(\mathcal N_\tau\), the unique positive linear extension, and

\[
\mathcal M_\tau
=\operatorname{span}\{y^*x:x,y\in\mathcal N_\tau\}.
\tag{5.0b}
\]

The extra trace identity makes \(\mathcal N_\tau\) *-closed. A *-closed left ideal is also a right ideal. Equation (5.0b) now makes \(\mathcal M_\tau\) a two-sided *-ideal, including multiplication by elements of the external unitization. This last conclusion uses the trace hypothesis: it is false for general weights.

For a unitary \(u\in A^+\) and \(a\in A_+\), apply the trace identity to \(u a^{1/2}\in A\). It gives \(\tau(uau^*)=\tau(a)\), even at an infinite value. Linear extension gives the same invariance on \(\mathcal M_\tau\). Apply it to \(xu\), which lies in that ideal: \(\tau(ux)=\tau(xu)\). If \(h=h^*\in A^+\) is a contraction, then

\[
\begin{gathered}
u=h+i(1-h^2)^{1/2},\\
u^*u=uu^*=1,\\
h=(u+u^*)/2.
\end{gathered}
\tag{5.0c}
\]

Scaling the real and imaginary parts expresses every element of \(A^+\) as a linear combination of at most four unitaries. This proves (5.2). No norm continuity of the finite linear trace was used.

The unnormalized matrix weight is \(\tau_n(c)=\sum_i\tau(c_{ii})\) for \(c\geq0\). Its trace identity follows from

\[
\begin{gathered}
\tau_n(X^*X)\\
=\sum_{i,j}\tau(x_{ij}^*x_{ij})\\
=\sum_{i,j}\tau(x_{ij}x_{ij}^*)\\
=\tau_n(XX^*).
\end{gathered}
\tag{5.0d}
\]

All sums are finite sums of nonnegative extended values. Its finite linear domain is exactly \(M_n(\mathcal M_\tau)\). Indeed, a finite positive matrix \(c\) has square root \(X\) with every entry in \(\mathcal N_\tau\), so every entry of \(c=X^*X\) belongs to \(\mathcal M_\tau\). Conversely, insert \(y,x\in\mathcal N_\tau\) in single matrix positions to express any matrix with one entry \(y^*x\) as a product \(Y^*X\) of square-finite matrices. Equation (5.0b) at matrix level proves the reverse inclusion. Entrywise summation of (5.2) proves matrix cyclicity. \(\square\)

The trace-specific ideal and cyclicity argument above supplies the additional hypotheses needed here. Blackadar 2006, II.6.8, remains the reference for this terminology.

**Theorem 5.1 (sufficient domain criterion).** Suppose a norm-dense *-subalgebra \(B\subset A\) lies in \(\mathcal M_\tau\). Assume that every \(M_n(B^+)\) is stable under holomorphic functional calculus inside \(M_n(A^+)\). Then there is a finite real-valued homomorphism \(\tau_*:K_0(A)\to\mathbb R\), given on finite-domain relative projections by

\[
\begin{gathered}
\tau_*([e]-[P])=\tau_n(e-P),\\
e\in M_n(B^+),\quad P=\epsilon_n(e).
\end{gathered}
\tag{5.3}
\]

It is positive on \(K_0(A)^+\) and agrees with the weight on finite-trace projections over \(A\).

*Proof.* First find enough representatives. Approximate the selfadjoint matrix \(e-P\) of an ambient relative projection by a selfadjoint matrix over \(B\). Keep the scalar part exactly \(P\). A sufficiently close approximation has spectrum in two disjoint neighborhoods of zero and one. The Riesz projection around the neighborhood of one belongs to \(M_n(B^+)\) by the assumed calculus, has scalar part \(P\), and is arbitrarily close to \(e\). Close-projection equivalence from Lesson 1 gives the same ambient K-class. Thus every class has a representative as in (5.3).

Next check the relations without assuming trace continuity. For projections \(e,f\in M_n(B^+)\) with the same scalar part and \(\|e-f\|<1/3\), put

\[
\begin{gathered}
z=fe+(1-f)(1-e)\\
=1+(f-e)(2e-1),\\
ze=fz,\qquad \epsilon_n(z)=1.
\end{gathered}
\tag{5.4}
\]

Since \(\|2e-1\|=1\), \(z\) is invertible. Inverse closure, a consequence of holomorphic closure, places \(z^{-1}\) in \(M_n(B^+)\). Therefore

\[
f-e=[z,ez^{-1}]=[z-1,ez^{-1}].
\tag{5.5}
\]

The first factor in the last commutator belongs to \(M_n(B)\subset M_n(\mathcal M_\tau)\); the second is bounded. Equation (5.2) gives \(\tau_n(f-e)=0\).

If two normalized representatives have equal ambient K-classes, add scalar projection blocks to give them the same scalar part. Equality of their classes in the unitization supplies, after common identity and zero padding, an idempotent path by Lesson 7, Lemma 3.1. Convert it continuously to a projection path by Lesson 1. Its scalar projection path can be made constant by continuous scalar-unitary transport. At the terminal point that transport may conjugate the original endpoint by a scalar unitary commuting with the common scalar projection; this preserves (5.3) by matrix cyclicity. The initial endpoint is unchanged.

Subdivide the resulting projection path into sufficiently short pieces. Approximate its finitely many vertices by selfadjoint matrices over \(B^+\), keeping the constant scalar projection, and apply the same Riesz correction. Keep the endpoints exactly. Uniform continuity of the path and continuity of the correction make consecutive projections closer than \(1/3\). Equation (5.5) proves equality of their trace differences, one pair at a time. Scalar padding contributes zero to (5.3), so the two original representatives have equal values. Block sums add these values, proving the homomorphism. Every difference is selfadjoint in the finite linear domain, so its value is real.

For an actual projection over \(A\), do the approximation with scalar part zero. Its equivalent projection over \(B\) has nonnegative finite weight. Its K-class therefore has nonnegative value. If the original projection has finite weight, its difference from the approximating projection lies in the finite ideal. Use (5.4) in the ambient unitization: now \(z-1\) is in that ideal, so (5.5) and (5.2) show their weight values agree. This proves positivity and the stated agreement. \(\square\)

The theorem gives a concrete sufficient hypothesis. More generally, if a finite-domain group \(G\) has a surjection \(i:G\to K_0(A)\) and its finite trace values give a homomorphism \(h:G\to\mathbb R\), those values descend to the ambient group **if and only if**

\[
h(\ker i)=0.
\tag{5.6}
\]

Necessity follows from factoring through \(i\). For sufficiency define the value at \(i(g)\) to be \(h(g)\); two choices differ by an element of the kernel. The projection-chain proof supplies this check under Theorem 5.1's hypotheses. Semifiniteness alone is not a substitute for either representability or this check.

For \(A=\mathcal K(H)\), ordinary \(\operatorname{Tr}\) is unbounded, but finite-rank operators give a dense domain satisfying the criterion. A finite collection of their ranges and adjoint ranges lies in a common finite-dimensional subspace. Relative matrix functional calculus acts on that finite block and the unchanged scalar block on its orthogonal complement, so its nonscalar part remains finite rank. The pairing on \(K_0(\mathcal K)=\mathbb Z\) is rank, by Lesson 5's stability theorem.

In contrast, ordinary trace on \(\mathcal L(\ell^2(\mathbb N))\) cannot give a homomorphism on its full \(K_0\) agreeing with rank-one projections. The unilateral shift gives \(1\sim1-p\), where \(p\) has rank one, so \([p]=0\) in that group while \(\operatorname{Tr}(p)=1\). Its finite-trace ideal has norm closure \(\mathcal K\), not all of \(\mathcal L\). This example shows exactly why a finite defect computation must be accompanied by a valid descent domain. Formula (5.3) evaluates a finite difference; it never subtracts two infinite weights.

## 6. The dual trace for a real action

Let \(\alpha:\mathbb R\to\operatorname{Aut}(A)\) be pointwise norm continuous and let \(\tau\) be an invariant, densely defined, lower semicontinuous trace weight. “Densely defined” means that \(\mathcal M_\tau\) is norm dense in \(A\). The main example is a finite positive trace on a unital algebra. For an infinite trace we retain the additional continuity hypothesis

\[
\begin{gathered}
\|\alpha_t(x)-x\|\\
\quad{}+\|\alpha_t(x)-x\|_{1,\tau}\longrightarrow0,\\
x\in\mathcal M_\tau,\qquad t\longrightarrow0.
\end{gathered}
\tag{6.0}
\]

where the coefficient trace norm is defined below. For a finite trace this follows from point-norm continuity. We construct the dual trace on the full crossed product \(D=A\rtimes_\alpha\mathbb R\), and then exhibit its dense domain for Theorem 5.1.

### 6.1. Extending the coefficient trace without losing its values

We use two exact programme proofs. [Weights and the Hilbert spaces of multiplication, “Completing the two multiplication domains” through “Recovering the representation and the full algebra”, (WH.6)–(WH.23)](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/OA-MOD-WH.html#completing-the-two-multiplication-domains) constructs a faithful normal semifinite weight from any left Hilbert algebra, on its generated von Neumann algebra. [Trace densities and noncommutative integration, “A complete space of actual integrable operators”, “Complete norms on actual measurable operators”, and “Products, norming tests and exact factorization”, (TI.12)–(TI.18), (TI.27)–(TI.38)](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/OA-MOD-TI.html#a-complete-space-of-actual-integrable-operators) proves completeness, bounded multiplication, \(L^2L^2\subset L^1\), and cyclicity for every faithful normal semifinite trace. These results rest on foundational prerequisites stated in those lessons and not proved here. Their Hilbert spaces need not be separable, their algebras need not be sigma-finite, and the trace of the identity need not be finite. We verify the applications rather than assuming a dual trace exists.

**Lemma 6.1 (coefficient completion).** The trace GNS representation \(\pi\) has a faithful normal semifinite trace \(\nu\) on \(M=\pi(A)''\) such that

\[
\nu(\pi(a))=\tau(a)\qquad(a\in A_+),
\tag{6.1a}
\]

including infinite values. Moreover

\[
\begin{gathered}
\mathcal M_\tau=A\cap_\pi L^1(M,\nu),\\
\|x\|_{1,\tau}=\|\pi(x)\|_1=\tau(|x|),
\end{gathered}
\tag{6.1b}
\]

and \(\|x\|+\|x\|_{1,\tau}\) is a complete norm on this ideal. The notation \(A\cap_\pi L^1\) means the inverse image under \(\pi\); it allows a nonfaithful coefficient trace.

*Proof.* Lemma 5.0 and the finite-domain GNS proof [(CS.5)–(CS.6)](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/OA-MOD-CS.html#the-gns-quotient-and-its-exact-domain) give a Hilbert space \(H_\tau\), with

\[
\begin{gathered}
\langle\Lambda(x),\Lambda(y)\rangle=\tau(y^*x),\\
\pi(a)\Lambda(x)=\Lambda(ax).
\end{gathered}
\tag{6.1c}
\]

Inner products in this construction are linear in the first variable. Quotient null vectors before completing.

There is a positive contractive approximate identity \((e_i)\) in \(\mathcal M_\tau\). Here is a construction that also controls finite weight. Direct finite positive \(h\) by order, and put \(e_h=h(1+h)^{-1}\). The finite positive cone is directed by addition; inverse order shows that \(e_h\) increases. Since \(0\leq e_h\leq h\), it is finite. For finite positive \(b\), \(h\geq tb\) gives

\[
\begin{gathered}
\|(1-e_h)b^{1/2}\|^2\\
\leq\|b(1+tb)^{-1}\|\leq t^{-1}.
\end{gathered}
\tag{6.1d}
\]

Thus \(e_h b\to b\), and adjoints give right convergence. Finite positive elements span a norm-dense ideal, so these contractions approximate every element of \(A\).

For \(x\in\mathcal N_\tau\), the elements \(e_i x\) lie in \(\mathcal M_\tau\). Both \(x^*e_i x\) and \(x^*e_i^2x\) converge in norm to \(x^*x\) and lie below it. Lower semicontinuity and domination force their weights to converge to \(\tau(x^*x)\). Expanding a finite square gives

\[
\begin{gathered}
\|\Lambda(x-e_i x)\|^2\\
=\tau(x^*x)-2\tau(x^*e_i x)\\
\quad{}+\tau(x^*e_i^2x)\longrightarrow0.
\end{gathered}
\tag{6.1e}
\]

Consequently \(\Lambda(\mathcal M_\tau)\) is dense in \(H_\tau\), and \(\pi(e_i)\to1\) strongly. The quotient of \(\mathcal M_\tau\) by its null ideal is a left Hilbert algebra: left multiplication has bound \(\|a\|\), its adjoint identity is (6.1c), products are dense by (6.1e), and involution is isometric because \(\tau(x^*x)=\tau(xx^*)\). These are precisely the [four multiplication axioms](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/OA-MOD-HA.html#starting-data-and-the-multiplication-domains). Its generated algebra is \(\pi(A)''\), since the coefficient ideal is norm dense.

Apply the weight construction. Its closed involution \(S\) is the everywhere defined antiunitary \(J\Lambda(x)=\Lambda(x^*)\). In (WH.7) the full multiplication domain is therefore all left-bounded vectors, and (WH.8) says \(\lambda_{J\xi}=\lambda_\xi^*\). Thus the square-finite ideal in (WH.16) is *-closed and

\[
\begin{gathered}
\nu(\lambda_\xi^*\lambda_\xi)=\|\xi\|^2\\
=\|J\xi\|^2\\
=\nu(\lambda_\xi\lambda_\xi^*).
\end{gathered}
\tag{6.1f}
\]

For an operator outside that ideal, both squares have infinite weight. Hence the constructed weight is a trace, with the faithfulness, normality and semifiniteness proved in that provider.

If \(a\geq0\) has finite \(\tau(a)\), (6.1e) makes \(\Lambda(e_i a^{1/2})\to\Lambda(a^{1/2})\). The associated left multipliers \(\pi(e_i a^{1/2})\) are uniformly bounded and tend strongly to \(\pi(a^{1/2})\). The definition of a left-bounded vector, tested on each right-algebra vector, therefore gives
\(\lambda_{\Lambda(a^{1/2})}=\pi(a^{1/2})\). Formula (WH.16) yields (6.1a) at this finite value.

For arbitrary \(a\geq0\), each \(e_i a e_i\) is finite, since it is dominated by \(\|a\|e_i^2\). Traciality and \(\|\pi(e_i)\|\leq1\) give

\[
\begin{gathered}
\tau(e_i a e_i)=\nu(\pi(e_i a e_i))\\
=\nu(\pi(a)^{1/2}\pi(e_i)^2\\
\qquad{}\cdot\pi(a)^{1/2})\\
\leq\nu(\pi(a)).
\end{gathered}
\tag{6.1g}
\]

Norm convergence \(e_i a e_i\to a\) and lower semicontinuity imply \(\tau(a)\leq\nu(\pi(a))\). Combined with the finite-value equality, this also proves equality when \(\tau(a)=\infty\). Density and lower semicontinuity were essential to this step.

Finite positive elements of \(A\) map into \(L^1(M,\nu)\), so their span does too. Conversely, if \(\pi(x)\in L^1\), its real and imaginary parts, and the positive and negative parts of each, are integrable by (TI.12)–(TI.18). Continuous functional calculus and (6.1a) show that these four positive elements of \(A\) have finite weight. Their linear combination is \(x\). This proves (6.1b).

For completeness, a Cauchy sequence in the displayed graph norm has an \(A\)-norm limit \(x\) and an \(L^1\)-limit \(y\). The latter converges in the complete measurable-operator topology by (TI.16), while \(\pi(x_n)\to\pi(x)\) in operator norm, hence in measure. Uniqueness of the measure limit gives \(y=\pi(x)\). Thus \(x\in\mathcal M_\tau\) and convergence holds in the graph norm. The module estimates and adjoint isometry are (TI.13). \(\square\)

**Corollary 6.2 (Every dense lower semicontinuous trace domain gives a pairing).** A densely defined lower semicontinuous positive trace weight on \(A\) gives a finite real-valued positive homomorphism

\[
\tau_*:K_0(A)\longrightarrow\mathbb R.
\tag{6.A1}
\]

Every actual matrix projection over \(A\) has finite weight, and this homomorphism takes its class to that weight. For a finite-domain relative representative it takes \([e]-[P]\) to \(\tau_n(e-P)\), using one finite difference.

*Proof.* Put \(B=\mathcal M_\tau\). Lemma 5.0 makes it a dense two-sided *-ideal, and Lemma 6.1 gives the complete norm \(\|b\|+\tau(|b|)\) with bounded multiplication by ambient elements. The coefficient-completion proof uses no action; equivalently apply it with the trivial action, whose graph-continuity condition is automatic. Thus this conclusion holds for every trace in the corollary.

All matrix unitizations are inverse closed. For an ambient invertible \(1+b\),

\[
\begin{gathered}
(1+b)^{-1}-1\\
=-(1+b)^{-1}b\\
\in M_n(B).
\end{gathered}
\tag{6.A2}
\]

This is the ideal property with bounded ambient multipliers. An arbitrary invertible scalar part is reduced to the identity by scalar matrix multiplication. At matrix size \(n\), the sum of the entry graph norms is a complete algebra norm: completeness follows entrywise, and submultiplicativity follows from the coefficient norm and bounded-multiplier estimate. Adding the sum of absolute values of the scalar matrix entries gives a complete submultiplicative unitization norm; it controls the ambient norm. Inverse closure places the resolvents in that algebra, and its Banach-algebra Neumann series makes them graph-norm continuous. Riemann sums for a compact contour converge in the complete graph norm, with the ambient value identified by the continuous inclusion. This proves the matrix holomorphic stability required by Theorem 5.1. That theorem supplies (6.A1), positivity and relative evaluation.

To check the asserted finiteness for every actual projection \(p\in M_n(A)\), choose \(x\in M_n(B)\) with \(\|x-p\|<1\). The element \(a=pxp\) belongs to this ideal and is invertible in the unital corner \(pM_n(A)p\), by its Neumann series around \(p\). Its corner inverse \(y\) is a bounded ambient element, and \(p=ya\) lies in \(M_n(B)\). The finite linear domain description in Lemma 5.0 therefore makes \(\tau_n(p)\) finite. Theorem 5.1's agreement and positivity now apply to all actual matrix projections. The zero projection is immediate. \(\square\)

This supplies the scope of [Roe, Proposition 14.11, p. 70] using the coefficient completion and exact domain descent already proved here. The written finite-domain and trace-integration prerequisites of Lemmas 5.0 and 6.1 remain in force. Neither a merely semifinite domain nor an arbitrary discontinuous algebraic trace acquires this conclusion without the stated density and lower semicontinuity.

The action preserves both coefficient norms. Under (6.0) its GNS unitaries \(U_t\Lambda(x)=\Lambda(\alpha_t(x))\) are strongly continuous. On the dense domain \(\mathcal M_\tau\) this follows from

\[
\|\pi(y)\|_2^2\leq\|y\|\,\|y\|_{1,\tau},
\tag{6.1h}
\]

and it extends by isometry to \(H_\tau\). For a finite trace on unital \(A\), \(\|y\|_{1,\tau}\leq\tau(1)\|y\|\), so (6.0) is automatic.

### 6.2. The convolution Hilbert algebra

Put \(B=\mathcal M_\tau\), with its complete graph norm. On \(C_c(\mathbb R,B)\) define

\[
\begin{gathered}
(f*g)(s)\\
=\int f(t)\alpha_t(g(s-t))\,dt,\\
f^\sharp(s)=\alpha_s(f(-s)^*),\\
\langle f,g\rangle=\int\tau(g(s)^*f(s))\,ds.
\end{gathered}
\tag{6.4}
\]

Graph continuity ensures that convolution is a \(B\)-valued Bochner integral and is continuous with compact support. Fubini and the action law prove associativity; substitution \(t\mapsto s-t\) proves reversal of products by \(\sharp\). Quotient the null space of this inner product. Its Hilbert completion is \(\mathcal H=L^2(\mathbb R,H_\tau)\), since compact scalar functions times \(\Lambda(B)\) are dense.

Left convolution is bounded by

\[
\|L_f\xi\|_{\mathcal H}
\leq\left(\int\|f(t)\|\,dt\right)\|\xi\|_{\mathcal H}.
\tag{6.5}
\]

Indeed, its integrand is coefficient multiplication followed by the unitary \(\xi(s)\mapsto U_t\xi(s-t)\); integrating the norm proves the estimate. The adjoint identity can be checked without a formal exchange of infinite traces. For core functions, all relevant products are integrable by Cauchy–Schwarz and compact support, and invariance gives

\[
\begin{aligned}
&\langle f*g,h\rangle\\
&\quad=\int\!\int\tau\Bigl(h(r+t)^*f(t)\\
&\qquad\qquad{}\cdot\alpha_t(g(r))\Bigr)\,dt\,dr\\
&\quad=\int\!\int\tau\Bigl(\alpha_{-t}(h(r+t)^*f(t))\\
&\qquad\qquad{}\cdot g(r)\Bigr)\,dt\,dr\\
&\quad=\langle g,f^\sharp*h\rangle.
\end{aligned}
\tag{6.6}
\]

The involution extends to

\[
(J\xi)(s)=U_s J_\tau\xi(-s),
\tag{6.7}
\]

an antiunitary involution: \(U_s\) commutes with \(J_\tau\), and invariance and the coefficient trace identity make it isometric.

Products are Hilbert dense. Choose nonnegative compactly supported scalar \(\phi_\varepsilon\), of integral one, with supports shrinking to zero. The functions \(\phi_\varepsilon e_i\) lie in the core. Left convolution by them tends strongly to the identity: translations \(\xi(s)\mapsto U_t\xi(s-t)\) are strongly continuous, while \(\pi(e_i)\to1\) strongly and all these operators are contractions. On a core function their convolution is a product of two core functions. Thus all four Hilbert-algebra axioms hold, including after the null quotient.

Apply the same weight-construction theorem. Because (6.7) is everywhere defined, the argument (6.1f) again makes its weight a faithful normal semifinite trace \(\widehat\nu\) on
\(N=L(C_c(\mathbb R,B))''\), with

\[
\widehat\nu(L_f^*L_f)=\int\tau(f(t)^*f(t))\,dt.
\tag{6.8}
\]

To place this on the stated C*-algebra, take the covariant pair on \(\mathcal H\)

\[
\begin{aligned}
(P(a)\xi)(s)&=\pi(a)\xi(s),\\
(V_t\xi)(s)&=U_t\xi(s-t).
\end{aligned}
\tag{6.9}
\]

It is nondegenerate and strongly continuous, and \(V_tP(a)V_t^*=P(\alpha_t(a))\). The [full crossed-product universal property, Theorem 2.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-01.html#2-the-universal-algebra-and-its-multipliers) supplies its integrated representation \(E:D\to N\), with \(E(X(f))=L_f\) for
\(X(f)=\int f(t)V_t\,dt\). Norm density of \(B\) makes these kernels norm dense in \(D\), by the coefficient approximation in Proposition 2.2 of that provider. Thus \(E(D)''=N\).

Define the dual trace on positive elements of the full crossed product by

\[
\widehat\tau(d)=\widehat\nu(E(d)),\qquad d\in D_+.
\tag{6.10}
\]

It is a lower semicontinuous trace weight. Indeed, finite-trace projections \(p\) form a directed family increasing strongly to the identity by (TI.2). The bounded normal positive functionals \(z\mapsto\widehat\nu(pzp)\) increase pointwise to \(\widehat\nu(z)\) on \(z\geq0\): use the trace identity to write their values as \(\widehat\nu(z^{1/2}pz^{1/2})\), and then normality. Their compositions with \(E\) are norm continuous. The resulting supremum is norm lower semicontinuous. It may be nonfaithful. Its normalization is

\[
\begin{gathered}
\widehat\tau(X(f)^*X(f))\\
=\int\tau(f(t)^*f(t))\,dt,\\
f\in C_c(\mathbb R,B).
\end{gathered}
\tag{6.1}
\]

An arbitrary \(L^2\) kernel need not define a bounded integrated operator. Extension of (6.1) uses simultaneous convergence of the operators and their Hilbert vectors, as in the next calculation.

### 6.3. Frequency measure for a finite coefficient trace

Assume now that \(A\) is unital and \(\tau\) is finite. Write the translation multipliers as \(V_t=e^{itH}\). The multiplier homomorphism from the full group algebra gives \(k(H)\) for \(k\in C_0(\mathbb R)\), and \(a k(H)\in D\), by [Fourier functional calculus for a flow, Proposition 5.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-05.html#fourier-functional-calculus-for-a-flow). Its positive-sign frequency coordinate is rescaled here by \(x=2\pi\xi\). The exact scalar proofs are [The Plancherel theorem, Theorem 1.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-08.html#section-1) and [Fourier inversion and the dual Haar measure, Theorem 2.1 and Proposition 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/HA-LCA/HA-LCA-07.html#section-3). We use the convention

\[
\begin{gathered}
k(x)=\int\check k(t)e^{itx}\,dt,\\
\int|\check k(t)|^2dt\\
=\frac1{2\pi}\int|k(x)|^2dx.
\end{gathered}
\tag{6.11}
\]

First let \(a\geq0\) and \(k\in C_0\cap L^2\). Approximate \(k\) by smooth compactly supported \(k_n\) both uniformly and in \(L^2\); truncation and scalar mollification give such a sequence. Their inverse transforms are Schwartz kernels, to which (6.1) extends by compact-support truncation in both the operator \(L^1\) norm and the Hilbert \(L^2\) norm. The operators \(a^{1/2}k_n(H)\) converge in norm, and their GNS vectors have the \(L^2\) limit \(t\mapsto\Lambda(a^{1/2})\check k(t)\). The left-bounded-vector characterization in (WH.16) identifies the limit with \(E(a^{1/2}k(H))\). Consequently

\[
\begin{gathered}
\|E(a^{1/2}k(H))\|_2^2\\
=\tau(a)\int|\check k(t)|^2dt\\
=\frac{\tau(a)}{2\pi}\int|k(x)|^2dx.
\end{gathered}
\tag{6.12}
\]

In particular \(k(H)\) is square integrable because \(\tau(1)<\infty\). The product and cyclicity theorems (TI.33) and (TI.38) therefore make \(a|k|^2(H)\) integrable and identify its trace with (6.12): cycle \(k(H)^*a^{1/2}\) and \(a^{1/2}k(H)\), and then cycle the bounded coefficient \(a^{1/2}\) against the resulting integrable product. Decompose a general bounded \(a\) into four positive terms and a general \(f\in C_0\cap L^1\) into its four positive parts. Taking \(k=\sqrt f\) in each positive term proves

\[
\begin{gathered}
\widehat\tau(a f(H))
=\frac{\tau(a)}{2\pi}\int f(x)\,dx,\\
f\in C_0(\mathbb R)\cap L^1(\mathbb R).
\end{gathered}
\tag{6.2}
\]

This is the normalization of [Frequency calculus for an action of Euclidean space, (7.13)](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/pseudodifferential-calculus-for-actions-of-rn.html#the-dual-trace-fixes-the-frequency-measure), following Connes, *Noncommutative Geometry*, Chapter II, §3. The construction above supplies its analytic existence in the present trace setting.

For an infinite coefficient trace, (6.12) remains valid for finite positive \(a\). In this case \(a^{1/2}\) need only lie in \(\mathcal N_\tau\). Approximate it by \(e_i a^{1/2}\in B\) using both norm convergence and (6.1e), before taking the same kernel and frequency limits. Traciality gives the finite trace of the positive sandwich \(a^{1/2}|k|^2(H)a^{1/2}\). We do not infer that every unsandwiched \(a f(H)\) is integrable when \(\tau(1)=\infty\). The product domain below handles that case directly.

### 6.4. The domain for the K-pairing

In both the finite and the infinite coefficient cases, set

\[
\begin{gathered}
\mathcal I=\{d\in D:\\
E(d)\in L^1(N,\widehat\nu)\},\\
\|d\|_{\mathcal I}=\|d\|_D+\|E(d)\|_1.
\end{gathered}
\tag{6.13}
\]

The same completeness proof as in Lemma 6.1 makes it a Banach *-ideal. Bounded multiplier estimates allow multiplication by \(D^+\), and the finite trace is the continuous functional \(d\mapsto\widehat\nu(E(d))\) on this graph norm.

It is norm dense without a weighted-resolvent shortcut. Each core \(X(f)\) is square integrable by (6.1), so

\[
\begin{gathered}
X(g)^*X(f)\in\mathcal I,\\
f,g\in C_c(\mathbb R,B).
\end{gathered}
\tag{6.14}
\]

by (TI.33). These core elements are norm dense in \(D\); the span of their pairwise products is also dense, because products span a dense subspace of every C*-algebra by its approximate identity. This proves density of \(\mathcal I\). For finite coefficient traces one may also use the dense sums \(a f(H)\) with Schwartz \(f\), now justified by (6.2).

Inverse closure is explicit. If \(1+x\) is invertible in \(D^+\) and \(x\in\mathcal I\), then

\[
\begin{gathered}
(1+x)^{-1}-1\\
=-(1+x)^{-1}x\in\mathcal I.
\end{gathered}
\tag{6.3}
\]

Every matrix level has the same property with the unnormalized matrix trace. For a general invertible scalar part, multiply first by its scalar inverse. Thus the spectra in the graph algebra and the ambient unitization coincide. The Neumann series in the Banach graph algebra makes its resolvent graph-norm continuous on each contour in the resolvent set. Contour integration therefore proves matrix holomorphic closure. When a holomorphic function vanishes at the scalar argument, its contour formula lies in the ideal; in general its scalar value is the scalar part. The positive elements of \(\mathcal I\) are exactly the positive elements with finite pullback trace. Conversely, real and imaginary parts of an integrable image, followed by their positive and negative parts, stay integrable by (TI.12)–(TI.18). Their corresponding continuous functional calculi lie in \(D\). Thus \(\mathcal I\) is exactly the finite linear domain of (6.10). Theorem 5.1 now defines \(\widehat\tau_*:K_0(D)\to\mathbb R\) on every relative K-class.

For the trivial action on \(\mathbb C\), \(D=C_0(\mathbb R)\) and the weight is integration against \(dx/(2\pi)\). The function \((1+x^2)^{-1}\) has weight \(1/2\), while positive cutoffs to longer intervals give infinite weight on the multiplier unit. Nevertheless the pairing is defined; here \(K_0(C_0(\mathbb R))=0\) by Lesson 10, so it is the zero homomorphism. An infinite weight and a finite K-pairing are compatible.

The infinite coefficient construction keeps the densely defined, lower semicontinuous, invariant trace and graph-continuity hypotheses of the cited frequency lesson's Lemma 7.9. Its alternative weighted-resolvent method is a comparison; (6.14) supplies the density proof used here. The graph condition is a stated hypothesis, not a consequence asserted from point-norm continuity alone.

## 7. Exercises with complete solutions

**Exercise 13.1.** Compute the pairing on \(K_0(M_2\oplus M_3)\) for weights \((s,t)\).

*Solution.* Use probability weights: \(s,t\geq0\), \(s+t=1\), and \(\tau(x,y)=s\operatorname{Tr}(x)/2+t\operatorname{Tr}(y)/3\). Minimal projections give the basis of \(\mathbb Z^2\), so

\[
\tau_*(a,b)=\frac{s}{2}a+\frac{t}{3}b.
\tag{7.1}
\]

For a virtual class subtract the ranks of its two representatives in each coordinate, then apply (7.1). The unit \((2,3)\) has value \(s+t=1\); the positive cone \(\mathbb N^2\) has nonnegative values. If the weights instead mean coefficients of the *unnormalized* traces, \(\tau=s\operatorname{Tr}_2+t\operatorname{Tr}_3\), the answer is \(sa+tb\), with normalization \(2s+3t=1\). This specifies both common weight conventions.

**Exercise 13.2.** Show that the pairing is constant on Murray–von Neumann classes.

*Solution.* Pad projections with zero blocks to a common matrix size and choose a partial isometry \(v\) with \(v^*v=p,vv^*=q\). Then \(\tau_n(p)=\tau_n(v^*v)=\tau_n(vv^*)=\tau_n(q)\) by (1.2). Padding adds only zero diagonal entries. For relative classes use \((\tau^0)_n\) from (1.4): it is tracial on the unitization, so the same equality holds for equivalent projections there, and subtracting their scalar classes yields (1.5). Positivity is asserted only for actual projections over \(A\), as in Theorem 1.1.

**Exercise 13.3.** Prove the Calderón–Fedosov formula for \(m=1\), then every \(m\geq1\).

*Solution.* With the generalized inverse \(R\) in (4.4), set \(E=S-R\). For trace-class errors \(a,b\), the products \(ET=P_0-a\), \(TE=P_1-b\) are trace class. The identity \(E=(ET)R+EP_1\) makes \(E\) trace class too. Rectangular cyclicity therefore cancels \(\operatorname{Tr}(ET)\) against \(\operatorname{Tr}(TE)\), leaving \(\operatorname{Tr}(a)-\operatorname{Tr}(b)=\operatorname{Tr}(P_0)-\operatorname{Tr}(P_1)=\operatorname{Index}T\). For general \(m\), multiply \(S\) by \(1+a+\cdots+a^{m-1}\). Since \(aS=Sb\), the resulting \(S_m\) has both errors exactly \(a^m,b^m\), by the telescoping products (4.8). These are trace class by hypothesis, so the first-power argument proves their trace difference is the same index. No infinite series or extra summability assumption occurs.

**Exercise 13.4.** Determine the trace range of the CAR algebra.

*Solution.* The CAR algebra is \(\varinjlim M_{2^k}\) under \(x\mapsto x\otimes1_2\). Its unique trace restricts to \(2^{-k}\operatorname{Tr}\), since each stage has a unique normalized trace and those traces are compatible. Lesson 5 gives \(K_0=\mathbb Z[1/2]\), positive cone \(\mathbb Z[1/2]_+\), unit one; thus the full group range is \(\mathbb Z[1/2]\). For projections in the algebra it is \(\mathbb Z[1/2]\cap[0,1]\): necessity follows from \(0\leq\tau(p)\leq\tau(1)=1\); a dyadic \(r/2^k\) in that interval is realized by a rank-\(r\) stage projection. Allowing projections in arbitrary matrix algebras gives the entire nonnegative dyadic cone, since one may choose a matrix size large enough to contain that rank. These three ranges refer to different sets of representatives.

**Exercise 13.5.** Recover the AF trace/state correspondence using Theorem 10.4 of the AF-algebras lesson.

*Solution.* A group state \(\sigma\) assigns nonnegative coefficients \(c_j^{(k)}\) to the images of stage minimal projections. Because the stage unit maps to \(1_A\), they satisfy \(\sum_jd_j^{(k)}c_j^{(k)}=1\). Define \(\tau_k=\sum_jc_j^{(k)}\operatorname{Tr}_j\). The inclusion's multiplicity matrix gives \(c^{(k)}=\alpha_k^Tc^{(k+1)}\), since it sends a minimal projection to projections of those ranks in the next summands. Theorem 10.4(3) consequently extends the compatible \(\tau_k\) to a unique tracial state \(\tau\). Every K-class is represented at some stage by continuity, and there \(\tau_*\) is the homomorphism with precisely these minimal-projection coefficients, hence equals \(\sigma\). Starting from a trace produces its actual stage coefficients, so reconstruction gives the original trace by the same projective-limit theorem. These are the two inverse identities, proving bijection. The argument works even when a stage K-map has a kernel.

## What this lesson imports and does not prove

Projection equivalence, scalar normalization, identity padding and K-theory continuity are imported from Lessons 1, 3–5 and 7. The index boundary is the one proved in Lessons 7 and 11, and the scalar Toeplitz index theorem is from Lesson 9. The finite-stage projective-limit theorem is AF-algebras, Theorem 10.4(3); the new AF trace/state bijection is proved here. The trace ideal and finite-rank approximation are the cited Lemma 7.3a; rectangular cyclicity is proved here. The projection-pair identity is cited as Lemma 10.1 with all its hypotheses. The general finite-domain GNS proof is supplied by the exact programme lesson cited in Lemma 5.0; that lemma proves the extra trace ideal and cyclicity statements. Section 6 constructs the coefficient completion and convolution dual trace using the written Hilbert-algebra weight theorem, with its recorded foundational prerequisites, and the exact complete integration theorems. Scalar Plancherel and its frequency measure are the linked harmonic-analysis theorems. The infinite coefficient case retains graph continuity and uses products of square-integrable core elements for its dense finite domain. No assertion that every group state of an arbitrary C*-algebra comes from a trace is used. Higher cyclic pairings and the general Thom isomorphism for real actions are outside this lesson's claims.

## References

- J. Roe, *Lectures on K-Theory and Operator Algebras*, Spring 2017, Lecture 14, especially Proposition 14.11, p. 70. [Freely accessible lecture notes](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/1/4020/files/2017/12/KTheoryNotes-1uvuwyz.pdf). Corollary 6.2 proves the general densely defined lower semicontinuous positive trace pairing using the complete finite-domain arguments above.

- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §§6.2–6.3, 6.8–6.9. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

- **[Blackadar 2006]** B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; [author's revised version](https://www.bruceblackadar.com/Mathematics/Cycr.pdf) with the same numbering, II.6.8 and V.2.4. Finite trace domains: II.6.8.1–II.6.8.2 and Proposition II.6.8.6.

- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024, §§2.1 and 2.3. The circle calculation here uses the direct Fourier proof (4.11) and kernel (4.12).

- **[Connes 1994]** A. Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter III, §3, printed pp. 229–238; Proposition 2(a), degree zero, gives the ordinary matrix trace pairing. Higher-degree normalizations are not needed here. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

- **Finite domains and the GNS space of a C*-weight**, (CS.1)–(CS.6); **Weights and the Hilbert spaces of multiplication**, (WH.6)–(WH.23); **Trace densities and noncommutative integration**, (TI.12)–(TI.18), (TI.27)–(TI.40) and (TI.57)–(TI.58). Exact programme links and scope accompany Lemmas 5.0 and 6.1. These providers retain their own licence; no provider text is incorporated here. The coefficient and crossed-product applications are independently written and checked here.
- **The Plancherel theorem**, Theorem 1.1; **The Fourier inversion theorem and the dual Haar measure**, Theorem 2.1 and Proposition 3.2; **Fourier functional calculus for a flow**, Proposition 5.2. Frequency rescaling is explicit in (6.11).
- **AF-algebras**, §10, Lemmas 10.2–10.3 and Theorem 10.4; **Cyclic forms that survive norm completion**, Theorem 4.3, degree zero, and Lemma 7.3a; **Pseudodifferential calculus for actions of R^n**, §7, (7.13)–(7.14), the finite ideal preceding Lemma 7.4, and Lemma 7.9; **The local index formula**, Lemma 10.1. Exact links accompany the corresponding statements above.

- **[Daws 2024]** Matt Daws, *Some notes on weights*, September 2024, §§2–3, [checked source revision](https://github.com/MatthewDaws/Mathematics/blob/a2d54776c75fc99f12d8e317e3e3c3fd34c813f9/Weights/weights.tex). The notes treat normal faithful semifinite weights; §3 assumes the general Hilbert-algebra correspondence. That construction and the broader coefficient-trace application are supplied by the programme proofs above. The notes are licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/); this is a comparison reference, with no text adapted here.

- **[Axler 2026]** Sheldon Axler, *Measure, Integration & Real Analysis*, 12 June 2026, Theorems 11.76, 11.82 and 11.87, printed pp. 374–377, [author’s electronic edition](https://measure.axler.net/MIRA.pdf), [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Its real-line Fourier proofs provide a comparison for the scalar normalization; the general programme Plancherel provider is used above. No text is adapted here.

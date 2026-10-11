# Six laboratories on expectations and operator-valued averages

This lesson develops six original problems from the mathematical phenomena behind
the exercises at the end of Takesaki II, Chapter IX, §4.  The problems are stated
afresh and solved in full.  Four points require corrections or qualifications:
the null space of an expectation is a left ideal, simultaneous Hilbert-seminorm
minimizers need not form a face, Euclidean modulation requires the Plancherel
dual measure, and a group Fourier expansion must be interpreted in its proper
\(L^1\) or \(L^2\) topology.

Throughout, inclusions of von Neumann algebras are unital.  A projection of norm
one onto a von Neumann subalgebra is therefore a conditional expectation by
Full nonunital retraction theorem.  Sums and integrals whose
values can be unbounded are taken in the extended positive cone described in
Infinite energies have bounded spectral tests.

## The faithful corner of a normal expectation

Let \(N\subseteq M\) and let \(E:M\to N\) be a normal projection of norm one.
Choose a faithful normal semifinite weight \(\psi\) on \(N\), whose existence is
Every von Neumann algebra has such a weight, and put
\(\Phi=\psi\circ E\).  Normality is immediate.  If
\((f_i)\subseteq\mathfrak n_\psi\) is an increasing net of positive contractions
converging strongly to \(1\), then

\[
\begin{aligned}
 E\bigl((xf_i)^*xf_i\bigr)
 &=f_iE(x^*x)f_i\\
 &\leq \lVert x\rVert^2 f_i^2 .
\end{aligned}
\tag{X4.1}
\]

Thus \(f_i x f_i\) belongs to the finite definition algebra of \(\Phi\), and
these compressions converge strongly to \(x\).  Hence \(\Phi\) is semifinite.
Because \(\psi\) is faithful, let \(\mathcal L_E\) denote the set of
\(x\in M\) satisfying \(E(x^*x)=0\). Its support description is

\[
\begin{aligned}
\mathcal L_E
  &=\{x\in M:\Phi(x^*x)=0\}\\
  &=M(1-e),
\end{aligned}
\tag{X4.2}
\]

where \(e=s(\Phi)\), by Normality produces a largest null projection through The faithful semifinite support corner.
The handedness in (X4.2) matters: \(\mathcal L_E\) is stable under
**left** multiplication, so its projection form is \(M(1-e)\).

For \(b\in N\), bimodularity gives

\[
 E\bigl((xb)^*xb\bigr)=b^*E(x^*x)b .
\tag{X4.3}
\]

Consequently \(M(1-e)\) is stable under right multiplication by \(N\).  Taking
\(x=1-e\), first with \(b\) and then with \(b^*\), gives

\[
\begin{aligned}
 (1-e)be&=0,\\
 eb(1-e)&=0
 \qquad(b\in N).
\end{aligned}
\tag{X4.4}
\]

Thus \(e\in M\cap N'\).  Let \(z\) be the central support of \(e\) in \(N'\).
In a faithful nondegenerate representation,
\(\mathcal Z(N')=N'\cap N''=\mathcal Z(N)\), so \(1-z\in N\).  Since
\(1-z\leq1-e\), (X4.2) and the fact that \(E\) fixes \(N\) imply

\[
 1-z=E(1-z)=0.
\tag{X4.5}
\]

The central support of \(e\) in \(N'\) is therefore \(1\).  Also
\(E(1-e)=0\), hence \(E(e)=1\).

Define

\[
\begin{aligned}
 E_e&:eMe\longrightarrow Ne,\\
 E_e(x)&=E(x)e .
\end{aligned}
\tag{X4.6}
\]

The algebra \(Ne\) has identity \(e\), and \(n\mapsto ne\) is faithful because
the central support of \(e\) is \(1\).  The map \(E_e\) is normal, positive,
contractive and \(Ne\)-bimodular.  If \(n\in N\), then
\(E_e(ne)=E(ne)e=nE(e)e=ne\), so it is a projection onto \(Ne\).  If
\(x\in eMe\) and \(E_e(x^*x)=0\), central support gives \(E(x^*x)=0\);
then \(x\in M(1-e)\), while \(x=xe\), and hence \(x=0\).  Thus \(E_e\) is
faithful.

We next record the three type consequences.

**Semifiniteness.** Suppose that \(M\) is semifinite. Every corner remains
semifinite. Indeed, for a faithful normal semifinite trace \(\tau\),
TI01 supplies finite-trace projections
\(p_i\uparrow1\). For \(x\ge0\) in any corner, the elements
\(x^{1/2}p_i x^{1/2}\) belong to that corner, increase to \(x\), and have
trace at most \(\|x\|\tau(p_i)<\infty\). Normality and faithfulness of the
restricted trace are inherited. We may therefore replace the inclusion and
expectation by (X4.6), identify \(N\) with \(Ne\), and assume from now on
that \(E\) is faithful.

Fix any nonzero projection \(q\in N\). On \(qMq\), the restricted trace is
faithful, normal and semifinite, and the restricted expectation maps onto
\(qNq\) faithfully. Choose \(0\ne b\in(qMq)_+\) of finite trace, and put
\(a=b^{1/2}\). Faithfulness gives \(c=E(b)\ne0\). For a suitable
\(\delta>0\), bounded spectral calculus gives

\[
\begin{gathered}
 f=1_{[\delta,\infty)}(c),\\
 f\in qNq,\quad f\ne0,\\
 f\leq\delta^{-1}c.
\end{gathered}
\tag{X4.7}
\]

For \(x\in fNf\), bimodularity yields

\[
 xx^*\leq\delta^{-1}E(xbx^*).
\tag{X4.8}
\]

Let \((x_i)\) be any net in the unit ball of \(fNf\) tending sigma-strongly
to zero. The bounded-topology identification
CP08 gives the same convergence in
\(qMq\). Since \(a\) is square integrable, the full
square-integrable factor theorem LQ03
gives \(ax_i^*\to0\) sigma-strongly. For each positive normal functional
\(\omega\) on \(fNf\), extend it to \(qNq\) by compression. Normality and
positivity of \(E\) make \(\widetilde\omega\circ E\) a positive normal
functional on \(qMq\), exactly as proved in
XT01. Thus (X4.8) implies
\[
\begin{gathered}
 0\le\omega(x_i x_i^*)\\
 \le\delta^{-1}(\widetilde\omega\circ E)
          ((ax_i^*)^*(ax_i^*))\\
 \longrightarrow0.
\end{gathered}
\]
These are the sigma-strong seminorms of \(x_i^*\). If \(f\) were infinite,
LQ04 would give
a sequence in this same unit ball whose adjoints violate that convergence.
Hence \(f\) is finite. Every nonzero projection \(q\in N\) therefore
contains a nonzero finite projection, so \(N\) is semifinite. The
trace-existence theorem TE11
then supplies a faithful normal semifinite trace on \(N\).

**Type I.** Suppose now that \(M\) is type I. Corners are type I by
FTI01, and
abelian projections are finite because adjoint products agree in a
commutative corner. Thus type I algebras are semifinite, and we may again
use the faithful corner and the preceding result. Let \(\nu\) be a
faithful normal semifinite trace on \(N\).

If \(N\) were not type I, some nonzero projection \(q\in N\) would contain
no nonzero abelian projection. Semifiniteness of the trace on \(qNq\)
and TI01 supply a nonzero \(p\le q\) with \(\nu(p)<\infty\). Set
\(N_0=pNp\), \(M_0=pMp\), and
\(\tau_N=\nu(p)^{-1}\nu|_{N_0}\). Restriction gives

\[
\begin{aligned}
 E_0&:M_0\longrightarrow N_0,\\
 \varphi&=\tau_N\circ E_0.
\end{aligned}
\tag{X4.9}
\]

Here \(E_0\) is faithful and normal, \(\tau_N\) is a faithful normal
tracial state, and \(\varphi\) is a faithful normal state on the type I
algebra \(M_0\). Choose a faithful normal semifinite trace
\(\operatorname{Tr}_0\) on \(M_0\), using TE11. The full
trace-density theorem TI06 gives a
unique positive \(h\in L^1(M_0,\operatorname{Tr}_0)\) representing
\(\varphi\); faithfulness makes its kernel projection zero. For
\(n\in N_0\), \(x\in M_0\), and \(y=E_0(x)\),

\[
\begin{gathered}
 \varphi(nx)=\tau_N(ny)\\
 =\tau_N(yn)\\
 =\varphi(xn).
\end{gathered}
\tag{X4.10}
\]

The integrable-density centralizer theorem FTI04
now puts \(N_0\) inside the finite type I algebra
\(C=\{h\}'\cap M_0\). Its proof uses the central spectral cutoffs
\(1_{[1/k,k]}(h)\) in \(C\), finite-trace corners of \(M_0\), and the
normal-kernel argument of
FTI03.
That same subalgebra theorem makes \(N_0\) type I. Since \(p\ne0\), it
contains a nonzero abelian projection below \(p\le q\), a contradiction:
its corner in \(N_0\) is exactly its corner in \(N\). Hence \(N\) is
type I. This argument requires neither a factor hypothesis nor a
sigma-finiteness assumption on the original inclusion.

**Atomicity.** Suppose that \(M\) is atomic, meaning that every nonzero
projection contains a minimal nonzero projection. Work in any faithful normal
concrete representation \(N\subseteq M\subseteq B(H)\). The
atomic matrix-block construction
supplies a normal unital positive \(M\)-bimodule projection
\(Q:B(H)\to M\). Explicitly, that proof decomposes
\(H=\bigoplus_i(K_i\otimes L_i)\) and
\(M=\prod_i(B(K_i)\otimes1_{L_i})\); compression against one unit vector
in each \(L_i\) defines \(Q\). Finite-rank projection nets, rather than
sequences, cover arbitrary Hilbert-space dimensions.

Compose this map with the given expectation:

\[
\begin{gathered}
 F=E\circ Q,\\
 F:B(H)\longrightarrow N,\\
 F(n)=n\\
 (n\in N).
\end{gathered}
\tag{X4.11}
\]

Both maps are normal and positive, so their composition is normal and
positive. It is unital and onto because both maps fix \(N\). For
\(a,b\in N\) and \(x\in B(H)\), their bimodule identities give

\[
\begin{gathered}
 F(axb)\\
 =E\bigl(aQ(x)b\bigr)\\
 =aF(x)b.
\end{gathered}
\tag{X4.12}
\]

The rank-one criterion
now makes \(N\) atomic. To recall its mechanism, for a rank-one positive
operator \(r_\xi\), every nonzero projection \(q\) under
\(1_{[\varepsilon,\infty)}(F(r_\xi))\) satisfies
\(\varepsilon\leq\|q\xi\|^2\). An orthogonal family of such projections
therefore has at most \(\|\xi\|^2/\varepsilon\) members. Successively
splitting nonminimal projections must terminate, so this spectral cut is a
finite sum of minimal projections of \(N\). All rank-one images are thus
supported on the central join of the minimal projections of \(N\).
Normality applied to the finite-rank projection net, together with
\(F(1)=1\), makes that join equal to \(1\). The polar-decomposition argument
in the criterion then puts a minimal projection under every nonzero
projection of \(N\). No faithfulness of \(E\) or \(Q\), countability of the
blocks, or faithful normal state is needed.

The formula sometimes printed as \((1-e)M\) cannot be correct.  For the
vector-state expectation from \(M_2(\mathbb C)\) to the scalars and the
rank-one support \(p_\xi\), the null matrices are exactly those satisfying
\(x\xi=0\), namely \(M_2(\mathbb C)(1-p_\xi)\), not
\((1-p_\xi)M_2(\mathbb C)\).

## Fixed points from invariant normal states

Let \(G\leq\operatorname{Aut}(M)\), and assume that its invariant normal
states detect every nonzero square: for \(x\ne0\) there is a normal state
\(\omega\) such that \(\omega\circ\alpha=\omega\) for every \(\alpha\in G\), and

\[
 \omega(x^*x)>0.
\tag{X4.13}
\]

If \(M=\{0\}\), its fixed algebra is also zero. The unique map between
these zero algebras is a faithful normal conditional expectation of norm
zero. This is the zero-algebra case of the result. For the rest of this
laboratory assume \(M\ne\{0\}\); a unital expectation then has norm one.

Write \(N=M^G\).  If \(\omega\) is invariant, naturality of supports gives
\(\alpha(s(\omega))=s(\omega)\), so \(s(\omega)\in N\).

Choose a maximal family \(\mathcal F\) of invariant normal states with
pairwise orthogonal supports, and define the arbitrary positive sum

\[
\begin{aligned}
 \Psi&=\sum_{\omega\in\mathcal F}\omega,\\
 p&=\sum_{\omega\in\mathcal F}s(\omega).
\end{aligned}
\tag{X4.14}
\]

Both sums are suprema of finite subsums.  If \(1-p\ne0\), (X4.13) supplies
an invariant state \(\theta\) with \(\theta(1-p)>0\).  Compressing and
normalizing \(\theta\) by the fixed projection \(1-p\) produces another
invariant state whose support is orthogonal to every support in
\(\mathcal F\), contradicting maximality.  Thus \(p=1\), and \(\Psi\) is
faithful.

For a finite \(\mathcal E\subseteq\mathcal F\), put
\(p_{\mathcal E}=\sum_{\omega\in\mathcal E}s(\omega)\).  Orthogonality gives

\[
\begin{aligned}
 \Psi(p_{\mathcal E})&=|\mathcal E|<\infty,\\
 p_{\mathcal E}&\uparrow1.
\end{aligned}
\tag{X4.15}
\]

The finite compressions \(p_{\mathcal E}xp_{\mathcal E}\) prove
semifiniteness of \(\Psi\) on \(M\).  Since every \(p_{\mathcal E}\) belongs
to \(N\), the same argument proves that
\(\nu=\Psi|_{N_+}\) is semifinite.

The weight \(\Psi\) is \(G\)-invariant.  For \(\alpha\in G\) and
\(t\in\mathbb R\), the GNS transport proof in SI14 yields

\[
\begin{aligned}
 \alpha\sigma_t^\Psi&=\sigma_t^\Psi\alpha,\\
 \sigma_t^\Psi(N)&=N.
\end{aligned}
\tag{X4.16}
\]

The modular expectation theorem The criterion and its exact setting
now gives a faithful normal conditional expectation \(E:M\to N\) satisfying

\[
 \nu\circ E=\Psi.
\tag{X4.17}
\]

For \(\alpha\in G\), the map \(E\alpha\) is another
\(\Psi\)-preserving expectation onto \(N\); uniqueness in ME-01 gives
\(E\alpha=E\).

It remains to justify uniqueness among all faithful normal invariant
projections, rather than only among \(\Psi\)-preserving ones.  Let
\(P:M\to N\) be faithful, normal, of norm one, and satisfy \(P\alpha=P\).
Set \(\Phi=\nu\circ P\).  Then \(\Phi\) is a faithful normal semifinite
\(G\)-invariant weight and \(\Phi|_N=\Psi|_N=\nu\).  Both modular groups
leave \(N\) invariant and restrict there to \(\sigma^\nu\).  For

\[
 u_t=[D\Phi:D\Psi]_t,
\tag{X4.18}
\]

the balanced-matrix naturality in SI14
gives \(\alpha(u_t)=u_t\), hence \(u_t\in N\).
For every \(n\in N\), equality of the restricted modular groups gives

\[
 u_t\sigma_t^\nu(n)=\sigma_t^\nu(n)u_t.
\tag{X4.19}
\]

Thus \(u_t\in\mathcal Z(N)\).  The center is fixed by \(\sigma^\nu\), and
the cocycle is therefore a one-parameter group \(u_t=h^{it}\) for a
positive injective operator affiliated with \(\mathcal Z(N)\).  The
fixed-density theorem The faithful invariant-weight equivalence
gives \(\Phi=\Psi_h\).  Restriction to \(N\) says \(\nu_h=\nu\), so
uniqueness of the central density gives \(h=1\).  Thus
\(\Phi=\Psi\), \(P\) preserves \(\Psi\), and ME-01 gives \(P=E\).

We have proved the existence and uniqueness of the faithful normal
norm-one projection onto \(M^G\) that is constant on every \(G\)-orbit.

## Orbit hulls and simultaneous GNS minimizers

Keep the hypotheses of X4-02, but do not use the expectation constructed
there.  For \(x\in M\), write \(Gx=\{\alpha(x):\alpha\in G\}\), and let

\[
 K(x)=\overline{\operatorname{co}}^{\,\sigma\mathrm w}(Gx).
\tag{X4.20}
\]

This is a sigma-weakly compact convex subset of the norm ball of radius
\(\lVert x\rVert\).

For an invariant normal state \(\omega\), let
\((H_\omega,\pi_\omega,\Lambda_\omega)\) be its GNS representation.  Use the
seminorm \(\lVert y\rVert_\omega=\lVert\Lambda_\omega(y)\rVert\), so that

\[
 \lVert y\rVert_\omega^2=\omega(y^*y).
\tag{X4.21}
\]

The coefficient maps used here are normal. For a vector of the form
\(\Lambda_\omega(a)\), the coefficient is
\(y\mapsto\omega(a^*y)\), which is normal by
CP06. For a general \(\eta\in H_\omega\),
approximate it by such vectors. Cauchy--Schwarz gives
\(\|\Lambda_\omega(y)\|\leq\|y\|\), so the corresponding functionals converge
in norm. The predual is norm closed, again by CP06. Thus
\(y\mapsto\langle\Lambda_\omega(y),\eta\rangle\) is normal for every \(\eta\).
In particular, \(\Lambda_\omega\) carries sigma-weak convergence to weak
Hilbert-space convergence. The seminorm \(\|y\|_\omega\) is sigma-weakly
lower semicontinuous, since its closed balls are intersections of the
closed inequalities against these coefficient functionals.
Invariance gives a unitary representation

\[
 U^\omega_\alpha\Lambda_\omega(y)
 =\Lambda_\omega(\alpha(y)).
\tag{X4.22}
\]

We first prove the Hilbert-space fact needed for simultaneous minimization.
Let \(U\) be any unitary representation on a Hilbert space \(H\), and let
\(L=\{v:U_\alpha v=v\text{ for every }\alpha\}\). This is a closed complex
subspace. Its orthogonal projection \(P\) exists by
LH01.
For \(\xi\in H\), put \(C=\overline{\operatorname{co}}^{\|\cdot\|}
\{U_\alpha\xi\}\) and \(d=\inf_{v\in C}\|v\|\). A minimizing sequence
\((v_n)\) is Cauchy. Indeed, its midpoints lie in \(C\), and the
parallelogram identity gives
\[
\begin{gathered}
 \|v_n-v_m\|^2\\
 \leq2\|v_n\|^2+2\|v_m\|^2-4d^2\\
 \longrightarrow0.
\end{gathered}
\]
Completeness and closedness give a point \(v\in C\) of norm \(d\). The
same inequality makes it unique. Every \(U_\alpha\) maps \(C\) onto itself
and preserves norm, so \(v\in L\). Also \(PU_\alpha=P\): pairing with any
vector in \(L\) proves the identity. Consequently \(Pw=P\xi\) for every
\(w\in C\). Applying this to \(v\in L\) gives \(v=P\xi\). Thus the closed
convex hull contains \(P\xi\), and that is its unique least-norm vector.

Apply this result to the representations (X4.22), writing \(P_\omega\) for
the projection onto their fixed vectors. If \(y\in K(x)\), normality of
the coefficient maps and \(P_\omega U^\omega_\alpha=P_\omega\) give
\(P_\omega\Lambda_\omega(y)=P_\omega\Lambda_\omega(x)\). Hence
\(\|y\|_\omega\geq\|P_\omega\Lambda_\omega(x)\|\).

For a finite set \(F\) of invariant states, form the finite direct sum
of the representations (X4.22), starting at
\((\Lambda_\omega(x))_{\omega\in F}\). Its fixed space is the direct sum
of their fixed spaces. The proved Hilbert result supplies finite convex
combinations \(y_j\) of the orbit \(Gx\) for which, simultaneously for
every \(\omega\in F\),
\(\Lambda_\omega(y_j)\to P_\omega\Lambda_\omega(x)\) in norm. The points
\(y_j\) stay in the sigma-weakly compact set \(K(x)\), so a subnet has a
sigma-weak limit \(y_F\in K(x)\). Each GNS coefficient is normal, so its
value on that subnet converges to its value on \(y_F\). The Hilbert norm
limit therefore implies
\(\Lambda_\omega(y_F)=P_\omega\Lambda_\omega(x)\) for all \(\omega\in F\).
Together with the preceding lower bound, this proves attainment of all
the individual minimum values by one point. Put
\(m_\omega(x)=\min_{z\in K(x)}\lVert z\rVert_\omega\).  Let \(K_F(x)\) be
the set of \(y\in K(x)\) satisfying, for every \(\omega\in F\),

\[
 \lVert y\rVert_\omega=m_\omega(x).
\tag{X4.23}
\]

The point \(y_F\) belongs to \(K_F(x)\), so this set is nonempty. It is
closed by lower semicontinuity and compact as a closed subset of \(K(x)\).
Invariance of each seminorm and of \(K(x)\) makes it \(G\)-invariant.

The assertion that \(K_F(x)\) must be a face is false.  Take
\(M=\mathbb C^2\), let \(G\) interchange the two coordinates, use the
invariant average state, and set \(x=(1,-1)\).  Its orbit hull is the
segment from \(x\) to \(-x\), parameterized by \(-1\leq t\leq1\), whereas

\[
 K_{\{\omega\}}(x)=\{0\}.
\tag{X4.24}
\]

The midpoint \(0=\tfrac12x+\tfrac12(-x)\) is not an endpoint, so its
singleton is not a face of the segment.  Face structure is unnecessary
for the argument.

For the fixed \(x\), abbreviate \(K_F=K_F(x)\).  These sets, ordered by
finite \(F\), have the finite-intersection property because

\[
 K_{F_1}\cap K_{F_2}=K_{F_1\cup F_2}.
\tag{X4.25}
\]

Compactness gives a point in

\[
 K_\infty(x)=\bigcap_F K_F(x).
\tag{X4.26}
\]

For every \(y\in K_\infty(x)\) and every invariant normal state
\(\omega\), the fixed component of \(\Lambda_\omega(y)\) is
\(P_\omega\Lambda_\omega(x)\), and their norms agree by the minimum
calculation. Orthogonality forces the remaining component to vanish, so
\[
 \Lambda_\omega(y)=P_\omega\Lambda_\omega(x).
\tag{X4.27}
\]

The same is true of \(\alpha(y)\).  Therefore
\(\omega((\alpha(y)-y)^*(\alpha(y)-y))=0\) for all invariant \(\omega\);
(X4.13) gives \(\alpha(y)=y\).  Thus \(y\in N\).  If \(y,z\) both lie in
\(K_\infty(x)\), subtracting their identities (X4.27), then using (X4.13), gives \(y=z\).
Conversely, if \(y\in K(x)\cap N\), then
\(\Lambda_\omega(y)\) is fixed. Its fixed component is
\(P_\omega\Lambda_\omega(x)\), by the normal-coefficient argument above,
so it equals that vector. Hence \(y\in K_\infty(x)\).  Write the unique point as \(E(x)\).
We have proved \(K(x)\cap N=K_\infty(x)\), and this set is the singleton

\[
 K_\infty(x)=\{E(x)\}.
\tag{X4.28}
\]

Equation (X4.27) proves linearity without choosing compatible averaging
nets.  Put \(a=E(x+y)\) and \(b=E(x)+E(y)\).  For every invariant normal
state \(\omega\), linearity of \(P_\omega\) gives

\[
 \Lambda_\omega(a)=\Lambda_\omega(b).
\tag{X4.29}
\]

The separating hypothesis gives \(a=b\), so \(E\) is additive.  Scalars are
handled identically.  The map fixes \(N\), and
\(\lVert E(x)\rVert\leq\lVert x\rVert\) because \(E(x)\in K(x)\).
Hence CE-004 makes \(E\) positive, completely positive and
\(N\)-bimodular.

For every invariant normal state \(\omega\), the vector
\(\Lambda_\omega(1)\) is fixed, so (X4.27) also gives

\[
 \omega(E(x))=\omega(x).
\tag{X4.30}
\]

If \(0\leq x_i\uparrow x\), then
\(0\leq E(x_i)\uparrow y\leq E(x)\).  Normality of the invariant states
and (X4.30) give \(\omega(E(x)-y)=0\) for all of them; (X4.13) gives
\(y=E(x)\).  Thus \(E\) is normal.  If \(E(x^*x)=0\), (X4.30) and
(X4.13) give \(x=0\), so \(E\) is faithful.

Finally, let \(P:M\to N\) be any normal norm-one projection satisfying
\(P\alpha=P\).  Normality implies

\[
 P(K(x))=\{P(x)\}.
\tag{X4.31}
\]

Since \(E(x)\in K(x)\) and \(P\) fixes \(N\),
\(P(x)=P(E(x))=E(x)\).  This proves uniqueness using only orbit geometry,
normal-state separation and the norm-one projection theorem; modular
theory was not used.

## The Euclidean modulation average

**The character commutant.** We first justify the multiplication algebra
used in this laboratory and the next. Let \(G\) be any locally compact
abelian group, let \(H_G=L^2(G)\), and let \(A_G=L^\infty(G)\) act by
multiplication. We use the local Haar completion of
PF21: finite-\(p\) functions
have countably many nonzero components in the open sigma-compact coset
decomposition, while bounded component families define \(L^\infty\).
The multiplication proof in PF21 applies to \(G\) itself and gives
\(A_G'=A_G\). For each continuous unitary character \(\chi\), write
\(u_\chi=M_\chi\).

Every normal functional \(\omega\) on \(A_G\) has the vector-series form
of CP06. Thus there are square-summable
families \((\xi_n),(\eta_n)\) in \(H_G\) with
\(\omega(M_f)=\sum_n\langle M_f\xi_n,\eta_n\rangle\). Cauchy--Schwarz gives
\[
\begin{gathered}
 \sum_n\|\xi_n\overline{\eta_n}\|_1\\
 \leq
 \Bigl(\sum_n\|\xi_n\|_2^2\Bigr)^{1/2}
 \Bigl(\sum_n\|\eta_n\|_2^2\Bigr)^{1/2}
 <\infty.
\end{gathered}
\]
Consequently \(h=\sum_n\xi_n\overline{\eta_n}\) converges in \(L^1(G)\),
and \(\omega(M_f)=\int_G fh\) for every bounded locally measurable \(f\).
All these products are supported on a countable union of sigma-finite
cosets, so no non-sigma-finite product integral is being used.

If \(\omega(u_\chi)=0\) for every \(\chi\), the Fourier transform of
\(h\) vanishes. Characters and their conjugates form the same family,
so this statement agrees with either Fourier sign convention.
PF17 proves injectivity on
\(L^1(G)\): its norm identity makes \(\lambda(h)=0\) when all character
integrals vanish; applying \(\lambda(h)\) to a compact approximate identity
then gives \(h=0\). Hence \(\omega=0\).

The weak-star annihilator identity of
CP05 now makes the linear span of the
\(u_\chi\) sigma-weakly dense in \(A_G\). Explicitly, a proper closed
linear span would be annihilated by a nonzero element of its predual,
which we have just excluded. Since the character multipliers belong to
\(A_G\), their generated von Neumann algebra is \(A_G\), and taking
commutants gives
\[
 \{u_\chi:\chi\in\widehat G\}'=A_G.
\]
This proof uses neither a countability hypothesis nor the biduality
theorem. We now specialize to the real line.

Let \(H=L^2(\mathbb R,ds)\), let
\(A=L^\infty(\mathbb R)\) act by multiplication, and put

\[
 (u_t\xi)(s)=e^{ist}\xi(s).
\tag{X4.32}
\]

Use the Fourier transform
\(\widehat f(t)=\int_{\mathbb R}e^{-ist}f(s)\,ds\).  The compatible dual
Haar measure is \(d\widehat t=dt/(2\pi)\).  Plancherel then reads

\[
\begin{gathered}
 \lVert\widehat f\rVert_{L^2(d\widehat t)}\\
 =\lVert f\rVert_{L^2(ds)}.
\end{gathered}
\tag{X4.33}
\]

For \(x\in B(H)_+\) and \(\eta\in H\), put
\(b_{x,\eta}(t)=\langle u_t x u_t^*\eta,\eta\rangle\). Define the
closed extended positive form by
\[
\begin{gathered}
 q_x(\eta)\\
 =\int_{\mathbb R} b_{x,\eta}(t)\,d\widehat t.
\end{gathered}
\tag{X4.34}
\]

It may take the value \(+\infty\).  Translation of \(t\) leaves the form
invariant under every \(u_r\), so its representing extended positive is
affiliated with
\(\{u_r:r\in\mathbb R\}'=A\). Here PF25 identifies all real-line
characters with the displayed exponentials, and the preceding character
commutant proof applies. Denote it by
\[
\begin{gathered}
 T(x)\\
 =\int_{\mathbb R}^{\widehat{\ }}u_t x u_t^*\,d\widehat t\\
 \in\widehat A_+.
\end{gathered}
\tag{X4.35}
\]

The hat records extended-positive integration, not a bounded weak
operator integral.  The representation is legitimate because (X4.34) is
a nonnegative quadratic form and Fatou's lemma makes it lower
semicontinuous in \(\eta\); a lower-semicontinuous nonnegative form is
closed, with a possibly nondense finite domain exactly as allowed in
\(\widehat A_+\).

Normality can be checked before taking the full integral. For a compact
\(K\subseteq\mathbb R\), integration over \(K\) gives a normal positive
functional of \(x\): its trace-class density is the Bochner integral of
\(\theta_{u_t^*\eta,u_t^*\eta}\) against \(dt/(2\pi)\). This integrand is
norm continuous in the trace class and \(K\) has finite measure. The full
nonnegative continuous coefficient integral is the supremum of these
compact integrals. Interchanging that supremum with an increasing-net
supremum proves normality of every vector observation of \(T\). The same
argument works with compact subsets of any LCA dual group, using the local
Haar convention of The full multiplication algebra and local measure convention.

For a rank-one positive
\(\theta_{\xi,\xi}\eta=\langle\eta,\xi\rangle\xi\), put
\(c_{\xi,\eta}(t)=\langle u_t\xi,\eta\rangle\) and
\(q_{\xi,\eta}=\langle T(\theta_{\xi,\xi})\eta,\eta\rangle\).  Plancherel gives

\[
\begin{aligned}
 q_{\xi,\eta}
 &=\lVert c_{\xi,\eta}\rVert_{L^2(d\widehat t)}^2,\\
 q_{\xi,\eta}
 &=\lVert\xi\overline\eta\rVert_{L^2(ds)}^2.
\end{aligned}
\tag{X4.36}
\]

The converse Plancherel test identifies the full domain here and in X4-05.
On any LCA group, let \(h\in L^1\) and suppose \(\widehat h\in L^2\).
Choose a positive compactly supported continuous approximate identity
\((k_i)\), normalized by \(\int k_i=1\). Then \(h*k_i\in L^1\cap L^2\),
\(|\widehat k_i|\leq1\), and Plancherel gives
\(\|h*k_i\|_2=\|\widehat h\,\widehat k_i\|_2\leq\|\widehat h\|_2\).
Since \(h*k_i\to h\) in \(L^1\), choose indices with summable \(L^1\)
errors. The resulting sequence converges almost everywhere; Fatou gives
\(h\in L^2\). The forward Plancherel identity now gives equality of the
two norms. This argument uses a sequence selected for this one function,
and requires no countable neighborhood basis.

For arbitrary \(\xi,\eta\in H\), the product
\(h=\xi\overline\eta\) lies in \(L^1\) by Cauchy--Schwarz. Its Fourier
coefficient is \(c_{\xi,\eta}\), up to character reflection. Thus (X4.36)
holds on all of \(H\), with both sides infinite exactly when
\(\xi\overline\eta\notin L^2\). It identifies the entire finite form
domain, so

\[
 T(\theta_{\xi,\xi})=M_{|\xi|^2}.
\tag{X4.37}
\]

If \(x\geq0\) and \((e_j)\) is an orthonormal basis, put
\(P_F=\sum_{j\in F}\theta_{e_j,e_j}\).  The finite partial sums

\[
\begin{gathered}
 x_F=x^{1/2}P_Fx^{1/2}\\
 \uparrow x.
\end{gathered}
\tag{X4.38}
\]

combine (X4.37) with monotone convergence.  For
\(\varphi(M_f)=\int_{\mathbb R}f(s)\,ds\), the result is

\[
 \widehat\varphi(T(x))=\operatorname{Tr}(x).
\tag{X4.39}
\]

Both sides may be infinite.

The form definition makes \(T\) additive, homogeneous, normal and
\(A\)-bimodular.  Equation (X4.39) makes it faithful.  Rank-one operators
formed from \(L^2\cap L^\infty\) have bounded output by (X4.37), and their
finite-dimensional corners are sigma-weakly dense in \(B(H)\); hence
\(T\) is semifinite.  It is therefore a faithful normal semifinite
operator-valued weight.  Uniqueness from the scalar composite follows
from Uniqueness from one scalar composite, including infinity.

If one integrates (X4.32) against ordinary \(dt\), (X4.37) acquires the
factor \(2\pi\), so the composite becomes \(2\pi\operatorname{Tr}\).
Thus the unqualified \(dt\) formula is correct only when the symbol
\(dt\) has already been declared to mean the Plancherel dual Haar
measure \(dt/(2\pi)\).

## Modulation over a locally compact abelian group

Let \(G\) be a locally compact abelian group with Haar measure \(dg\).
For \(\mathcal Ff(\chi)=\int_G\overline{\chi(s)}f(s)\,dg(s)\), choose the
dual Haar measure \(d\chi\) on \(\widehat G\) so that

\[
\begin{gathered}
 \lVert\mathcal Ff\rVert_{L^2(d\chi)}\\
 =\lVert f\rVert_{L^2(dg)}.
\end{gathered}
\tag{X4.40}
\]

This is the normalization constructed in
An onto Plancherel transform through Haar normalization and a finite example.
On \(H=L^2(G,dg)\), let \(A=L^\infty(G)\) and

\[
\begin{gathered}
 (u_\chi\xi)(s)\\
 =\chi(s)\xi(s).
\end{gathered}
\tag{X4.41}
\]

For \(x\in B(H)_+\), set

\[
\begin{gathered}
 T_G(x)\\
 =\int_{\widehat G}^{\widehat{\ }}u_\chi x u_\chi^*\,d\chi.
\end{gathered}
\tag{X4.42}
\]

As in (X4.34), this means the extended closed form obtained by integrating
the positive matrix coefficients.  Fatou's lemma again proves lower
semicontinuity and hence closedness.  It is invariant under every
\(u_\gamma\). The character commutant proof in X4-04
uses Fourier injectivity and normal vector-series densities on the local
Haar completion, and gives
\(\{u_\gamma:\gamma\in\widehat G\}'=A\). Hence (X4.42) belongs to
\(\widehat A_+\).

For arbitrary \(\xi,\eta\in H\), put
\(c_{\xi,\eta}(\chi)=\langle u_\chi\xi,\eta\rangle\) and
\(q_{\xi,\eta}=\langle T_G(\theta_{\xi,\xi})\eta,\eta\rangle\).  Then

\[
\begin{aligned}
 q_{\xi,\eta}
 &=\lVert c_{\xi,\eta}\rVert_{L^2(d\chi)}^2,\\
 q_{\xi,\eta}
 &=\lVert\xi\overline\eta\rVert_{L^2(dg)}^2,
\end{aligned}
\tag{X4.43}
\]

The converse Plancherel test just proved includes the infinite values and
identifies the entire finite form domain. Therefore

\[
 T_G(\theta_{\xi,\xi})=M_{|\xi|^2}.
\tag{X4.44}
\]

For \(\varphi(M_f)=\int_G f\,dg\), finite-rank approximation as in
(X4.38) now proves

\[
\begin{gathered}
 \widehat\varphi(T_G(x))\\
 =\operatorname{Tr}(x).
\end{gathered}
\tag{X4.45}
\]

Normality, faithfulness and \(A\)-bimodularity follow exactly as in X4-04.
Vectors in \(C_c(G)\) are bounded and form a dense subspace of \(L^2(G)\);
their finite-rank operators have bounded outputs, proving semifiniteness
without a countability assumption.  Thus (X4.42) is the unique faithful
normal semifinite operator-valued weight with scalar composite
\(\operatorname{Tr}\).  Its normalization is intrinsic: rescaling \(dg\)
by \(c\) rescales the Plancherel dual measure by \(c^{-1}\), leaving
(X4.45) unchanged.

## A discrete-group average and its Fourier coefficients

Let \(G\) be a countable discrete group, let \(H=\ell^2(G)\), and write
\(\delta_s\) for the standard basis.  Use

\[
\begin{aligned}
 \lambda(r)\delta_s&=\delta_{rs},\\
 \rho(r)\delta_s&=\delta_{sr^{-1}}.
\end{aligned}
\tag{X4.46}
\]

The two representations commute. The regular commutant theorem
PF01, specialized to counting
measure, proves the reverse inclusion needed for
\[
\begin{gathered}
 M=\lambda(G)''\\
 =\rho(G)'.
\end{gathered}
\tag{X4.47}
\]

Let \(\tau(y)=\langle y\delta_e,\delta_e\rangle\) be the canonical finite
trace on \(M\). Here are the finite-trace checks. This vector functional is
normal and positive, and \(\tau(1)=1\). If \(x\in M\) and
\(\tau(x^*x)=0\), then \(x\delta_e=0\). Commutation with \(\rho\) makes
\(x\delta_s=0\) for every \(s\), hence \(x=0\). For traciality put
\(a=x\delta_e\). The same commutation gives
\((x\delta_s)(t)=a(ts^{-1})\), and thus
\((x^*\delta_e)(s)=\overline{a(s^{-1})}\). Inversion permutes the counting
basis, so \(\|x^*\delta_e\|=\|x\delta_e\|\), or
\(\tau(xx^*)=\tau(x^*x)\). Polarizing this identity gives
\(\tau(y^*x)=\tau(xy^*)\) for all \(x,y\in M\), which is traciality.

For \(x\in B(H)_+\), define

\[
\begin{gathered}
 T(x)\\
 =\sum_{r\in G}^{\widehat{\ }}\rho(r)x\rho(r)^*.
\end{gathered}
\tag{X4.48}
\]

the supremum of the finite positive partial sums in the extended positive
cone.  Reindexing makes this extended positive invariant under
\(\operatorname{Ad}\rho\), so (X4.47) puts it in \(\widehat M_+\).
Put \(v_r=\rho(r)^*\delta_e\).  Then

\[
\begin{gathered}
 \widehat\tau(T(x))\\
 =\sum_{r\in G}\langle xv_r,v_r\rangle\\
 =\sum_{s\in G}\langle x\delta_s,\delta_s\rangle\\
 =\operatorname{Tr}(x).
\end{gathered}
\tag{X4.49}
\]

The sum is normal, \(M\)-bimodular and faithful.  For the matrix units
\(e_{a,b}\delta_t=\mathbf1_{\{b\}}(t)\delta_a\), its finite-ideal
extension gives

\[
\begin{gathered}
 T(e_{a,b})\\
 =\sum_{r\in G}e_{ar^{-1},\,br^{-1}}\\
 =\lambda(ab^{-1}).
\end{gathered}
\tag{X4.50}
\]

Thus finite matrix corners have bounded output and are sigma-weakly dense;
\(T\) is semifinite.  Equations (X4.48–49) therefore define the unique
faithful normal semifinite operator-valued weight satisfying
\(\widehat\tau\circ T=\operatorname{Tr}\).

There is a precise Fourier form, but it is not an unrestricted operator
series for every positive \(x\in B(H)\).  If
\(x\in\mathcal S_1(H)_+\), then \(T(x)\) is a positive element of
\(L^1(M,\tau)\).  Additivity gives a well-defined linear extension to \(\mathcal S_1(H)\):
if a self-adjoint operator is written as a difference of positives in two
ways, equality of the corresponding positive sums makes their images
agree. For self-adjoint \(a=a_+-a_-\), (X4.49) gives
\(\|T(a)\|_1\leq\operatorname{Tr}(a_+)+\operatorname{Tr}(a_-)=\|a\|_1\).
For arbitrary \(x\), use its real and imaginary parts and the adjoint
isometry in TI06 to obtain
\(\|T(x)\|_1\leq2\|x\|_1\). This bound supplies the trace-norm continuity
needed below; no convergence of a formal Fourier series is involved.
Define
\(\widehat x(s)=\operatorname{Tr}(\lambda(s)^*x)\).  For every \(s\in G\),

\[
\begin{gathered}
 \tau\!\left(\lambda(s)^*T(x)\right)\\
 =\widehat x(s).
\end{gathered}
\tag{X4.51}
\]

It suffices to check (X4.51) on \(e_{a,b}\), where both sides are
\(\mathbf1_{\{s=ab^{-1}\}}\). Finite sums of these matrix units are dense
in trace norm: approximate a trace-class operator by finite-rank ones,
then approximate their finitely many vectors by finitely supported
vectors. The rank-one bound
\(\|\theta_{\xi,\eta}\|_1=\|\xi\|\|\eta\|\) makes the latter approximation
a trace-norm approximation. The bound for \(T\) just proved, and
\(|\tau(bz)|\leq\|b\|\|z\|_1\) from TI06, extend the identity to all of
\(\mathcal S_1(H)\).

These Fourier coefficients determine an \(L^1(M,\tau)\) element uniquely.
Indeed, a density whose coefficients vanish defines by TI06 a normal
functional vanishing on the linear span of the \(\lambda(s)\). This is a
unital star algebra whose sigma-weak closure is \(M\), by the
bicommutant theorem BK03.
The functional is therefore zero, and injectivity of the TI06 density
map makes its density zero. Consequently the notation
\[
\begin{gathered}
 T(x)\\
 \sim\sum_{s\in G}\widehat x(s)\lambda(s).
\end{gathered}
\tag{X4.52}
\]

means equality of all Fourier coefficients in \(L^1(M,\tau)\).

For completeness, the unitaries \((\lambda(s))_{s\in G}\) form an
orthonormal basis of \(L^2(M,\tau)\). Since \(\tau(1)=1\), every \(a\in M\)
is square integrable. The map \(a\mapsto a\delta_e\) is isometric for the
\(L^2\) norm, because \(\|a\delta_e\|^2=\tau(a^*a)\). The trace Hilbert-space
identification TI15 makes \(M\) dense
in \(L^2(M,\tau)\), so this map extends to an isometry onto a closed
subspace of \(\ell^2(G)\). Its image contains
\(\lambda(s)\delta_e=\delta_s\) for every \(s\); hence it is onto and sends
the stated family to the standard orthonormal basis.
If in addition \(T(x)\in L^2(M,\tau)\), its Hilbert coefficient at
\(\lambda(s)\) is exactly (X4.51), and (X4.52) converges in \(L^2\):
\[
\begin{gathered}
 T(x)\\
 =\sum_{s\in G}^{L^2}\widehat x(s)\lambda(s).
\end{gathered}
\tag{X4.53}
\]

For a finite linear combination of matrix units, the sum is finite by
(X4.50).  For a general positive bounded \(x\), the quantities
\(\operatorname{Tr}(\lambda(s)^*x)\) need not exist and no such Fourier
series is asserted.

This also detects the missing left side in the printed formula.  When
\(G\) is infinite and \(x=e_{e,e}\), (X4.50) gives

\[
 T(e_{e,e})=1\ne e_{e,e}.
\tag{X4.54}
\]

Thus replacing \(T(x)\) by \(x\) is false even on a rank-one positive.

The mathematical antecedents for X4-01–06 are Takesaki, *Theory of Operator Algebras II*, Chapter IX, Exercise 4(1)–(6).  The semifinite and type-I mechanisms in X4-01 also use the ideas of Takesaki, *Theory of Operator Algebras I*, Chapter V, Lemmas 2.27–2.29 and Theorem 2.30.  The exposition, counterexamples, normalization checks, domain corrections and proofs in this lesson are independently written.

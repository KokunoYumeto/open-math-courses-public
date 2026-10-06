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

**Semifiniteness.**  It is enough to work with the faithful corner (X4.6),
because corners of semifinite algebras are semifinite and \(N\cong Ne\).
Suppose that a nonzero central summand \(qN\) were of type III.  The restriction
of \(E\) to \(qMq\) is faithful.  Let \(\tau\) be a faithful normal semifinite
trace on \(qMq\), choose \(0\ne b\in(qMq)_+\) with \(\tau(b)<\infty\), and
put \(a=b^{1/2}\).  Faithfulness makes \(E(b)\ne0\), so for some
\(\delta>0\) the spectral projection

\[
\begin{aligned}
 f&=1_{[\delta,\infty)}(E(b))\in qN,\\
 f&\ne0,\qquad f\leq\delta^{-1}E(b).
\end{aligned}
\tag{X4.7}
\]

For \(x\in fNf\), bimodularity gives
\(xE(b)x^*=E(xbx^*)\), and (X4.7) yields

\[
 xx^*\leq\delta^{-1}E(xbx^*).
\tag{X4.8}
\]

If a bounded net \(x_i\in fNf\) tends sigma-strongly to zero, the finite-trace
estimate for \(a\in\mathfrak n_\tau\) makes \(a x_i^*\to0\) sigma-strongly.
Normal complete positivity of \(E\), followed by (X4.8), gives
\(x_i x_i^*\to0\) sigma-strongly.  Hence involution is sigma-strongly
continuous on the unit ball of \(fNf\).  An infinite projection cannot have
this property: an infinite matrix-unit row supplies a bounded net converging
sigma-strongly to zero whose adjoints do not.  Therefore \(f\) is finite,
contradicting that the nonzero corner \(fNf\) lies in a type III algebra.
There is no type III central summand, so \(N\) is semifinite.

**Type I.**  Suppose now that \(M\) is type I.  The preceding paragraph makes
\(N\) semifinite.  If \(N\) had a nonzero type II summand, a further nonzero
sigma-finite finite corner would give a faithful normal tracial state
\(\tau_N\) on a finite type II algebra \(N_0\).  Restricting the faithful
expectation gives

\[
\begin{aligned}
 E_0&:M_0\longrightarrow N_0,\\
 \varphi&=\tau_N\circ E_0,
\end{aligned}
\tag{X4.9}
\]

where \(M_0\) is still type I and \(\varphi\) is a faithful normal state.
Choose a faithful normal semifinite trace \(\operatorname{Tr}_0\) on \(M_0\).
There is an injective positive
\(h\in L^1(M_0,\operatorname{Tr}_0)\) with
\(\varphi(x)=\operatorname{Tr}_0(hx)\). For \(n\in N_0\), \(x\in M_0\),
and \(y=E_0(x)\), bimodularity and traciality give

\[
\begin{aligned}
 \varphi(nx)&=\tau_N(ny),\\
             &=\tau_N(yn)=\varphi(xn).
\end{aligned}
\tag{X4.10}
\]

so \(N_0\subseteq\{h\}'\cap M_0\).

We use the elementary type-I density lemma: if \(A\) is type I and an
injective positive \(h\) is integrable for a faithful semifinite trace, then
\(\{h\}'\cap A\) is finite type I and every von Neumann subalgebra of it is
type I.  Here is the cutoff mechanism.  In
\(C=\{h\}'\cap A\), the projections

\[
 c_k=1_{[1/k,k]}(h)
\]

are central, increase strongly to \(1\), and satisfy
\(\operatorname{Tr}_0(c_k)\leq k\operatorname{Tr}_0(h)<\infty\).
Thus \(c_kAc_k\) is finite type I.  Its homogeneous decomposition is a
central sum of algebras \(L^\infty(X)\,\overline\otimes\,M_n\); the standard
polynomial identity on each \(M_n\) shows that every von Neumann subalgebra
of a homogeneous summand is type I.  The central sum over \(n\), followed
by \(c_k\uparrow1\), proves the lemma.  Finiteness of \(C\) also follows
directly because \(x\mapsto\operatorname{Tr}_0(hx)\) is a faithful finite
trace on \(C\).  Applied to (X4.10), the lemma contradicts the choice of
\(N_0\).  Hence \(N\) is type I.

**Atomicity.**  Write RNP for the Radon--Nikodym property. Use the
Banach-space characterization

\[
\begin{aligned}
 &A\text{ is atomic}\\
 &\Longleftrightarrow A_*\text{ has RNP}.
\end{aligned}
\tag{X4.11}
\]

Indeed, the predual of
\(\bigoplus_i B(H_i)\) is the \(\ell^1\)-sum of the trace classes
\(\mathcal S_1(H_i)\), which has the Radon--Nikodym property; conversely a
diffuse summand gives the standard nonatomic \(L^1\) obstruction.  The
Radon--Nikodym property passes to closed subspaces.  For a normal
expectation \(F:A\to B\), the preadjoint embedding

\[
\begin{aligned}
 F_*&:B_*\longrightarrow A_*,\\
 \omega&\longmapsto\omega\circ F .
\end{aligned}
\tag{X4.12}
\]

is isometric, since restriction back to \(B\) recovers \(\omega\).  If \(M\)
is atomic, then so is the corner \(eMe\); (X4.12) makes \((Ne)_*\) a closed
subspace of \((eMe)_*\).  Equation (X4.11) makes \(Ne\), and therefore
\(N\), atomic.

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
\(t\in\mathbb R\), functoriality of modular automorphisms yields

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

naturality under \(G\) gives \(\alpha(u_t)=u_t\), hence \(u_t\in N\).
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

This seminorm is sigma-weakly lower semicontinuous: its closed balls are intersections
of inequalities against the normal coefficient functionals
\(y\mapsto\langle\Lambda_\omega(y),\eta\rangle\).
Invariance gives a unitary representation

\[
 U^\omega_\alpha\Lambda_\omega(y)
 =\Lambda_\omega(\alpha(y)).
\tag{X4.22}
\]

Let \(P_\omega\) be the projection onto its fixed-vector space.  For a
finite set \(F\) of invariant states, use the direct sum of the
representations (X4.22).  The closed convex hull of a unitary orbit has a
unique least-norm vector, and that vector is the projection onto the
fixed-vector space.  Hence one net of finite convex combinations of
\(\alpha(x)\) converges in every \(H_\omega\), \(\omega\in F\), to
\(P_\omega\Lambda_\omega(x)\).  Put
\(m_\omega(x)=\min_{z\in K(x)}\lVert z\rVert_\omega\).  Let \(K_F(x)\) be
the set of \(y\in K(x)\) satisfying, for every \(\omega\in F\),

\[
 \lVert y\rVert_\omega=m_\omega(x).
\tag{X4.23}
\]

Thus \(K_F(x)\) is nonempty, compact and \(G\)-invariant.  Lower
semicontinuity makes it closed.

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
\(\omega\), uniqueness of the Hilbert-space least-norm vector gives

\[
 \Lambda_\omega(y)=P_\omega\Lambda_\omega(x).
\tag{X4.27}
\]

The same is true of \(\alpha(y)\).  Therefore
\(\omega((\alpha(y)-y)^*(\alpha(y)-y))=0\) for all invariant \(\omega\);
(X4.13) gives \(\alpha(y)=y\).  Thus \(y\in N\).  If \(y,z\) both lie in
\(K_\infty(x)\), (X4.27) applied to \(y-z\) and (X4.13) give \(y=z\).
Conversely, if \(y\in K(x)\cap N\), then
\(\Lambda_\omega(y)\) is a fixed vector in the closed convex hull of the
orbit of \(\Lambda_\omega(x)\).  Every vector in that hull has fixed
component \(P_\omega\Lambda_\omega(x)\), so a fixed one must equal that
component.  Hence \(y\in K_\infty(x)\).  Write the unique point as \(E(x)\).
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
 \lVert\widehat f\rVert_{L^2(d\widehat t)}
 =\lVert f\rVert_{L^2(ds)}.
\tag{X4.33}
\]

For \(x\in B(H)_+\), define a closed extended positive form by

\[
 q_x(\eta)
 =\int_{\mathbb R}
   \left\langle u_t x u_t^*\eta,\eta\right\rangle
   \frac{dt}{2\pi}.
\tag{X4.34}
\]

It may take the value \(+\infty\).  Translation of \(t\) leaves the form
invariant under every \(u_r\), so its representing extended positive is
affiliated with
\(\{u_r:r\in\mathbb R\}'=A\).  Denote it by

\[
 T(x)=\int_{\mathbb R}^{\widehat{\ }}
      u_t x u_t^*\,\frac{dt}{2\pi}\in\widehat A_+.
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
 x_F=x^{1/2}P_Fx^{1/2}\uparrow x
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
 \lVert\mathcal Ff\rVert_{L^2(d\chi)}
 =\lVert f\rVert_{L^2(dg)}.
\tag{X4.40}
\]

This is the normalization constructed in
An onto Plancherel transform through Haar normalization and a finite example.
On \(H=L^2(G,dg)\), let \(A=L^\infty(G)\) and

\[
 (u_\chi\xi)(s)=\chi(s)\xi(s).
\tag{X4.41}
\]

For \(x\in B(H)_+\), set

\[
 T_G(x)
 =\int_{\widehat G}^{\widehat{\ }}
   u_\chi x u_\chi^*\,d\chi.
\tag{X4.42}
\]

As in (X4.34), this means the extended closed form obtained by integrating
the positive matrix coefficients.  Fatou's lemma again proves lower
semicontinuity and hence closedness.  It is invariant under every
\(u_\gamma\).  Characters generate the full multiplication algebra, so
\(\{u_\gamma:\gamma\in\widehat G\}'=A\); hence (X4.42) belongs to
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
 \widehat\varphi(T_G(x))=\operatorname{Tr}(x).
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

The two representations commute, and

\[
 M=\lambda(G)''=\rho(G)'.
\tag{X4.47}
\]

Let \(\tau(y)=\langle y\delta_e,\delta_e\rangle\) be the canonical finite
trace on \(M\).

For \(x\in B(H)_+\), define

\[
 T(x)
 =\sum_{r\in G}^{\widehat{\ }}
   \rho(r)x\rho(r)^*,
\tag{X4.48}
\]

the supremum of the finite positive partial sums in the extended positive
cone.  Reindexing makes this extended positive invariant under
\(\operatorname{Ad}\rho\), so (X4.47) puts it in \(\widehat M_+\).
Put \(v_r=\rho(r)^*\delta_e\).  Then

\[
\begin{aligned}
\widehat\tau(T(x))
 &=\sum_{r\in G}\langle xv_r,v_r\rangle\\
 &=\sum_{s\in G}\langle x\delta_s,\delta_s\rangle\\
 &=\operatorname{Tr}(x).
\end{aligned}
\tag{X4.49}
\]

The sum is normal, \(M\)-bimodular and faithful.  For the matrix units
\(e_{a,b}\delta_t=\mathbf1_{\{b\}}(t)\delta_a\), its finite-ideal
extension gives

\[
\begin{aligned}
T(e_{a,b})
 &=\sum_{r\in G}e_{ar^{-1},\,br^{-1}}\\
 &=\lambda(ab^{-1}).
\end{aligned}
\tag{X4.50}
\]

Thus finite matrix corners have bounded output and are sigma-weakly dense;
\(T\) is semifinite.  Equations (X4.48–49) therefore define the unique
faithful normal semifinite operator-valued weight satisfying
\(\widehat\tau\circ T=\operatorname{Tr}\).

There is a precise Fourier form, but it is not an unrestricted operator
series for every positive \(x\in B(H)\).  If
\(x\in\mathcal S_1(H)_+\), then \(T(x)\) is a positive element of
\(L^1(M,\tau)\).  Extend linearly to \(\mathcal S_1(H)\), and define
\(\widehat x(s)=\operatorname{Tr}(\lambda(s)^*x)\).  For every \(s\in G\),

\[
 \tau\!\left(\lambda(s)^*T(x)\right)=\widehat x(s).
\tag{X4.51}
\]

It suffices to check (X4.51) on \(e_{a,b}\), where both sides are
\(\mathbf1_{\{s=ab^{-1}\}}\), and then use trace-norm continuity.
Consequently the notation

\[
 T(x)\sim\sum_{s\in G}\widehat x(s)\lambda(s)
\tag{X4.52}
\]

means equality of all Fourier coefficients in \(L^1(M,\tau)\).

If in addition \(T(x)\in L^2(M,\tau)\), the unitaries
\((\lambda(s))_{s\in G}\) form an orthonormal basis of that Hilbert space,
and (X4.52) converges in \(L^2\):

\[
 T(x)=\sum_{s\in G}^{L^2}\widehat x(s)\lambda(s).
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

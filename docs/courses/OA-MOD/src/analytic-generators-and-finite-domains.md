# Analytic generators and exact finite weight domains

**Self-checked by the writing AI.**

An imaginary-time generator is a closed-strip endpoint with a specified domain. Its graph can determine an entire real group, and its relative modular graph can be tested by finite weight pairings. Neither assertion permits replacing a domain by a convenient dense subset.

The source targets are Takesaki, *Theory of Operator Algebras II*, VIII.3.22–26. The proofs below use CP's predual duality, NP's normality criterion, MA-08's scalar strip principle, WH's full weight Hilbert algebra, MF-07–09's Tomita algebra and power cores, HS-01/03's full-domain strip criterion and right multiplication, and GC's balanced weight and normalized faithful cocycle. Scalar integration and complex analysis retain their explicit provider contracts.

One additional structural input is declared as **AG-DEP-KADISON-ISOMETRY**: a surjective complex-linear isometry of a unital C*-algebra has the form \(T(x)=uJ_0(x)\), where \(u\) is unitary and \(J_0\) is a unital Jordan *-isomorphism. This theorem was proved by R. V. Kadison in 1951; a proof is given in D. Sherman, [*A new proof of the noncommutative Banach–Stone theorem*](https://arxiv.org/abs/math/0409488v1), Theorem 1.3, whose unital case is stated there as Theorem 1.2. This classification is an explicit imported prerequisite, whose proof closure is pending. The normality consequence needed here is proved below. No multiplicativity assumption is added to the groups in VIII.3.22 or VIII.3.24.

All inner products are linear in their first slot. Products of finite ideals below mean their **linear product span**.

## Strip domains, normality and integer powers

Let \(\alpha_t\), \(t\in\mathbb R\), be a one-parameter group of complex-linear isometries of a von Neumann algebra \(M\), with every real orbit pointwise sigma-weakly continuous. Each map is onto, since its inverse is \(\alpha_{-t}\).

**Normality from the stated structural input.** For an individual map write \(T=uJ_0\). Both \(J_0\) and its inverse are positive: every positive element is a square of a self-adjoint element, and Jordan *-maps preserve such squares. They are inverse order isomorphisms. If \(x_j\uparrow x\) is bounded and positive, its least-upper-bound characterization gives \(J_0(x_j)\uparrow J_0(x)\). NP-04 therefore makes \(J_0\) normal. Bounded left multiplication by \(u\) is sigma-weakly continuous by CP-06. Thus \(T\) is sigma-weakly continuous, as is its inverse. This deduction, including the arbitrary-net order step, does not require that \(T\) preserve products.

For a real height \(h\ne0\), set

\[
 S_h=\{z:\min(0,h)\leq\operatorname{Im}z\leq\max(0,h)\}.
 \tag{AG.1}
\]

An element \(a\) belongs to \(D(\alpha_{ih})\) when there is a bounded \(M\)-valued function \(F_a\) on this **whole closed strip**, sigma-weakly continuous there, holomorphic in the interior, and satisfying \(F_a(t)=\alpha_t(a)\). Put \(\alpha_{t+ih}(a)=F_a(t+ih)\). Real-time maps retain their usual domain \(M\). Boundary uniqueness in MA-08, tested against \(M_*\), makes the extension unique. Interior holomorphy can equivalently be tested weak-star: scalar Cauchy coefficients define elements \(C_j\in M=(M_*)^*\) with \(\|C_j\|\leq CR^{-j}\) on an interior circle. Their norm-convergent Taylor series has every scalar test of \(F_a\), so equals \(F_a\).

Normality permits applying \(\alpha_s\) to the strip, and uniqueness gives

\[
 \alpha_s(F_a(z))=F_a(z+s),\qquad
 F_a(t+ih)=\alpha_t(\alpha_{ih}(a)).
 \tag{AG.2}
\]

If \(b=\alpha_z(a)\), translation of this strip by \(z\) supplies a strip for \(b\) in the opposite direction. Indeed \(w\mapsto F_a(z+w)\) has real edge \(\alpha_t(b)\) and takes the value \(a\) at \(-z\). Hence

\[
 \alpha_{-z}(\alpha_z(a))=a,
 \qquad \mathcal G(\alpha_{-z})=\mathcal G(\alpha_z)^{-1}.
 \tag{AG.3}
\]

Here inverse means reversal of ordered pairs in the graph; it is not an assertion that either domain is all of \(M\).

Restriction of a strip of height \(n\) to successive unit strips proves one inclusion in

\[
 D((\alpha_i)^n)=D(\alpha_{in}),\qquad
 (\alpha_i)^n a=\alpha_{in}a\quad(n\geq1).
 \tag{AG.4}
\]

Conversely, a defined sequence of \(n\) iterates supplies \(n\) bounded strips. Their common edges coincide by (AG.2). Gluing them gives a bounded sigma-weakly continuous function on the larger closed strip. Scalar Morera, subdividing a triangle along the finitely many common edges, proves interior holomorphy; the predual Cauchy argument above proves norm holomorphy. This gives the other inclusion. Opposite heights follow from (AG.3).

Each graph is closed in the norm product topology. If \(a_j\to a\) and \(\alpha_{ih}a_j\to b\) in norm, the scalar strip maximum principle bounds the norm of a difference of their extensions by the larger edge difference. The strips therefore converge uniformly in norm to the required strip for \((a,b)\). This argument asserts norm closedness and does not substitute norm continuity for the given real boundary topology.

## A bounded exponential-type core without a Fourier import

Define the entire function \(q(z)=(\sin z/z)^2\), with its removable value \(q(0)=1\), and

\[
 Z=\int_{\mathbb R}q(t)\,dt\in(0,\infty),\qquad
 k_r(z)=\frac rZ q(rz),\quad r>0.
 \tag{AG.5}
\]

On the real line these are nonnegative integrable probability kernels. No value for \(Z\) is needed. For \(|y|\geq1\), \(|\sin(t+iy)|\leq e^{|y|}\) gives
\(\int |q(t+iy)|dt\leq\pi e^{2|y|}/|y|\).
For \(|y|\leq1\), use \(\sin w/w=\int_0^1\cos(sw)ds\) on \(|t|\leq2\), and the denominator bound \(|w|^2\geq t^2\) outside. These two integrals are bounded by \(4e^{2|y|}\) and \(e^{2|y|}\), respectively. Thus, for every complex \(z\),

\[
 \int_{\mathbb R}|k_r(t-z)|dt
 \leq\frac5Z e^{2r|\operatorname{Im}z|}.
 \tag{AG.6}
\]

For \(x\in M\) define weak-star integrals by their predual pairings:

\[
 x_r=\int_{\mathbb R}k_r(t)\alpha_t(x)dt,\qquad
 F_r(z)=\int_{\mathbb R}k_r(t-z)\alpha_t(x)dt.
 \tag{AG.7}
\]

CP-06 represents these bounded functionals on \(M_*\) as elements of \(M\). One has \(\|x_r\|\leq\|x\|\). On compact parameter sets the kernels have a common integrable majorant: on a bounded interval use removability and compactness; outside it use the squared denominator and the bounded imaginary height. Scalar Morera and dominated integration make each test of \(F_r\) entire. Local boundedness from (AG.6) and the Cauchy argument in AG-01 make \(F_r\) norm-entire.

Normality of \(\alpha_s\), followed by a real change of variables, gives \(F_r(s)=\alpha_s(x_r)\). Consequently

\[
 \|F_r(t+iy)\|\leq \frac5Z\|x\|e^{2r|y|}
 \quad(t,y\in\mathbb R).
 \tag{AG.8}
\]

In particular every restriction is a bounded closed strip. Its real orbit is entire of exponential type with a bound **uniform in the real coordinate**.

The kernels form an approximate identity as \(r\to\infty\): for every \(\delta>0\), their mass outside \((-\delta,\delta)\) tends to zero by the change of variables \(s=rt\). Continuity of \(t\mapsto\omega(\alpha_t(x))\) at zero, its bound \(\|\omega\|\|x\|\), and this tail estimate prove \(\omega(x_r)\to\omega(x)\) for every \(\omega\in M_*\). Thus

\[
 M_{\exp}^{\alpha}=\{a: \alpha_z(a)\text{ is entire and }
       \|\alpha_{t+iy}(a)\|\leq C e^{r|y|}
       \text{ for some }C>0,r\geq0\}
 \tag{AG.9}
\]

is a linear, sigma-weakly dense subspace of \(M\). It has bounded approximants \(x_r\) for every \(x\). Translation of an entire orbit proves invariance under every \(\alpha_z\), using (AG.2), with the constant enlarged by \(e^{r|\operatorname{Im}z|}\). This proves the full density assertion of VIII.3.22 for the stated isometry groups.

## Imaginary integers determine a horizontally bounded entire function

**Lemma.** If an entire scalar function satisfies

\[
 |f(t+iy)|\leq C e^{r|y|},\qquad f(in)=0\quad(n=1,2,\ldots),
 \tag{AG.10}
\]

then \(f=0\).

**Proof.** Map the disc to the upper half-plane by \(z(w)=i(1+w)/(1-w)\). The function \(g(w)=e^{irz(w)}f(z(w))\) is analytic and bounded by \(C\), and has zeros

\[
 w_n=\frac{n-1}{n+1},\quad n\geq1.
 \tag{AG.11}
\]

Suppose it is nonzero. Its zero at zero has a finite order \(m\geq1\). Then \(h(w)=g(w)/w^m\) has \(h(0)\ne0\) and \(|h|\leq C\): apply the maximum principle on circles of radius \(\rho\) to obtain \(|h|\leq C\rho^{-m}\), and let \(\rho\uparrow1\).

For \(N\geq2\) put

\[
 B_N(w)=\prod_{n=2}^N\frac{w_n-w}{1-w_n w},\qquad
 B_N(0)=\prod_{n=2}^N\frac{n-1}{n+1}
       =\frac{2}{N(N+1)}.
 \tag{AG.12}
\]

Each factor has modulus one on the unit circle; its denominator has no zero in the closed disc. The zeros of \(h\) cancel all numerator zeros, so \(h/B_N\) is analytic in the disc. On circles \(|w|=\rho\) tending to one, the minimum of \(|B_N|\) tends to one, uniformly, for this fixed finite product. The maximum principle and the bound for \(h\) therefore give \(|h/B_N|\leq C\). At zero this implies

\[
 0<|h(0)|\leq \frac{2C}{N(N+1)}\longrightarrow0,
 \tag{AG.13}
\]

a contradiction. Hence \(g=0\), so \(f\) vanishes on the upper half-plane and therefore everywhere. This argument proves VIII.3.23 without requiring a distributional Paley–Wiener theorem. \(\square\)

The weaker inequality \(|f(z)|\leq C e^{r|z|}\) would give a false lemma: \(\sinh(\pi z)\) has all the indicated zeros and is not zero. The source's horizontal growth convention is essential.

## Inclusion of imaginary generator graphs fixes the real group

**Proposition.** For two groups as in AG-01, if

\[
 \mathcal G(\alpha_i^1)\subseteq\mathcal G(\alpha_i^2),
 \tag{AG.14}
\]

then \(\alpha_t^1=\alpha_t^2\) on \(M\) for every real \(t\).

**Proof.** Fix \(x\in M_{\exp}^{\alpha^1}\) with bound \(C e^{r|y|}\), and write \(y_k=\alpha_{ik}^1(x)\) for every integer \(k\). All these elements remain in that entire core. Graph inclusion gives \(\alpha_i^2(y_k)=y_{k+1}\) for every \(k\). Inverse graphs from (AG.3) give \(\alpha_{-i}^2(y_{k+1})=y_k\). Integer gluing from (AG.4) now supplies the entire orbit of \(x\) for group 2, with the same values \(y_k\) at every imaginary integer, positive and negative.

On the strip between heights \(k\) and \(k+1\), the edge norms for group 2 are \(\|y_k\|\) and \(\|y_{k+1}\|\), since its real maps are isometries. The weighted scalar three-lines estimate (proved by the exponential multiplier in HS-01) gives, for \(0\leq u\leq1\),

\[
 \|\alpha_{t+i(k+u)}^2(x)\|
 \leq (Ce^{r|k|})^{1-u}(Ce^{r|k+1|})^u
 =Ce^{r|k+u|}.
 \tag{AG.15}
\]

The last equality holds because adjacent integer intervals do not cross zero in their interior. Thus group 2 has the same horizontal growth bound.

For each normal functional, \(f(z)=\omega(\alpha_z^1(x)-\alpha_z^2(x))\) satisfies AG-03 and vanishes at all positive imaginary integers. It is zero. Predual separation gives equality of the real orbits of \(x\). Finally AG-02 supplies bounded sigma-weak approximants of every element by this core, and AG-01 makes both fixed real maps normal. Passing to these approximants proves the proposition on all of \(M\). This retains the full scope and the positive-imaginary sign of VIII.3.24. \(\square\)

## The Tomita test algebra is a power core

For a faithful normal semifinite weight \(\varphi\), work on its faithful normal GNS space, suppress the representation, and put

\[
 S=J\Delta^{1/2},\quad F=S^*=J\Delta^{-1/2},\quad
 \mathcal A=\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*).
 \tag{AG.16}
\]

WH-09–11 identify this with the **full** weight Hilbert algebra. Let \(\mathcal A_0\) be MF-07's maximal Tomita algebra. Those results give

\[
 S\mathcal A_0=F\mathcal A_0=\Delta^s\mathcal A_0=\mathcal A_0
 \quad(s\in\mathbb R),\qquad
 S^2=F^2=I,\quad SF=\Delta^{-1},\quad FS=\Delta
 \text{ on }\mathcal A_0.
 \tag{AG.17}
\]

For example \(F=S\Delta^{-1}\) on this common power domain, so its invariance follows from MF-07. The products and signs follow directly from \(J\Delta^sJ=\Delta^{-s}\).

We recall the precise graph-core fact needed below. For \(r>0\) set \(G_r=\exp[-(\log\Delta)^2/(4r)]\). For every real \(s\), both \(G_r\) and \(\Delta^sG_r\) are bounded; scalar spectral dominated convergence gives

\[
 G_r\xi\to\xi,\qquad \Delta^sG_r\xi\to\Delta^s\xi
 \quad(\xi\in D(\Delta^s)).
 \tag{AG.18}
\]

MF-08 places \(G_r\eta\) in \(\mathcal A_0\) for \(\eta\in\mathcal A\). For fixed \(r\), approximate \(\xi\) in Hilbert norm by such \(\eta\)'s. The two bounded operators then approximate \(G_r\xi\) and \(\Delta^sG_r\xi\) simultaneously. Choosing these approximations after (AG.18) proves that \(\mathcal A_0\) is a graph core for \(\Delta^s\), in particular for \(\Delta\). This is MF-09's actual power-core statement; ordinary Hilbert-space density would not suffice.

## The single-weight generator has an exact finite-pair test

**Theorem.** For \(a,b\in M\), the pair \((a,b)\) belongs to \(\mathcal G(\sigma_{-i}^\varphi)\) if and only if

\[
 a\mathfrak n_\varphi^*\subseteq\mathfrak n_\varphi^*,\qquad
 \mathfrak n_\varphi b\subseteq\mathfrak n_\varphi,\qquad
 \varphi(ax)=\varphi(xb)\quad(x\in\mathfrak m_\varphi).
 \tag{AG.19}
\]

Here \(\mathfrak m_\varphi=\operatorname{span}\mathfrak n_\varphi^*\mathfrak n_\varphi\), and the last assertion uses its finite complex-linear extension, not extended positive values on arbitrary elements.

**From the strip to the pairings.** Let \(F_a\) be the lower strip of height one, with endpoint \(b\), and let \(c=F_a(-i/2)\). HS-03 applied to its first half gives

\[
 ya^*\in\mathfrak n_\varphi,\qquad
 \Lambda(ya^*)=JcJ\Lambda(y)\quad(y\in\mathfrak n_\varphi).
 \tag{AG.20}
\]

The reflected strip \(z\mapsto F_a(\bar z-i)^*\) has real edge \(\sigma_t(b^*)\) and midpoint \(c^*\). HS-03 applied to its first half gives

\[
 xb\in\mathfrak n_\varphi,\qquad
 \Lambda(xb)=Jc^*J\Lambda(x)=(JcJ)^*\Lambda(x).
 \tag{AG.21}
\]

These prove both domain inclusions in (AG.19). For \(x,y\in\mathfrak n_\varphi\), both products in the following expression belong to \(\mathfrak m_\varphi\), and

\[
 \varphi(ay^*x)
 =\langle\Lambda(x),\Lambda(ya^*)\rangle
 =\langle\Lambda(xb),\Lambda(y)\rangle
 =\varphi(y^*xb).
 \tag{AG.22}
\]

Linearity gives the asserted equality on all of \(\mathfrak m_\varphi\).

**From the pairings to the full closed domain.** Assume (AG.19). For \(\xi=\Lambda(x)\), \(\eta=\Lambda(y)\) in \(\mathcal A_0\), one has
\(\Lambda(ya^*)=SaS\eta\) and \(\Lambda(xb)=Sb^*S\xi\).
Every occurrence of \(S\) has its domain: \(ay^*\) lies in \(\mathfrak n_\varphi\) by the left ideal property, and its adjoint \(ya^*\) is there by the assumed first inclusion; the same argument applies to \(b^*x^*\) using the second inclusion. Thus the finite-pair equality reads

\[
 \langle\xi,SaS\eta\rangle
 =\langle Sb^*S\xi,\eta\rangle,
 \quad\text{equivalently}\quad
 \langle aS\eta,F\xi\rangle=\langle bF\eta,S\xi\rangle.
 \tag{AG.23}
\]

The equivalence uses the adjoint identity for the conjugate-linear operator \(S\). Set \(\zeta_1=F\eta\), \(\zeta_2=S\xi\). By (AG.17) these range independently over \(\mathcal A_0\), and (AG.23) becomes

\[
 \langle a\Delta^{-1}\zeta_1,\Delta\zeta_2\rangle
 =\langle b\zeta_1,\zeta_2\rangle
 \quad(\zeta_1,\zeta_2\in\mathcal A_0).
 \tag{AG.24}
\]

Since \(\mathcal A_0\) is a core for the self-adjoint \(\Delta\), the adjoint-domain criterion proves
\(a\Delta^{-1}\zeta_1\in D(\Delta)\) and \(\Delta a\Delta^{-1}\zeta_1=b\zeta_1\).
Invariance under \(\Delta^{-1}\) gives \(\Delta a\zeta=b\Delta\zeta\) on \(\mathcal A_0\). Graph-core approximation and closedness of \(\Delta\) extend this to

\[
 aD(\Delta)\subseteq D(\Delta),\qquad
 \Delta a\xi=b\Delta\xi\quad(\xi\in D(\Delta)).
 \tag{AG.25}
\]

HS-01 with \(D=\Delta\), \(s=1\) now supplies the unique bounded \(M\)-valued lower strip with endpoint \(b\). MF-06 identifies its real edge with \(\sigma_t^\varphi(a)\). This proves the converse. We have not assumed that right multiplication is initially a bounded GNS operator, that \(a\) is entire, or that tests on a merely dense vector space establish (AG.25). \(\square\)

The source's printed page 131 repeats its second test vector in the subsequent operator-coefficient display. Formula (AG.24) retains the independent first and second vectors, and (AG.25) states the full domain that the display must establish.

## The relative generator and its two mixed ideals

Let \(\varphi,\psi\) be faithful normal semifinite weights and let \(u_t=[D\psi:D\varphi]_t\), with numerator \(\psi\) and reference \(\varphi\). Set

\[
 \tau_t(a)=u_t\sigma_t^\varphi(a).
 \tag{AG.26}
\]

The cocycle law gives a one-parameter group of complex-linear isometries; its inverse is \(\tau_{-t}\). Normality and pointwise sigma-weak continuity follow from GC's unitary cocycle and the modular automorphisms.

**Relative finite-domain theorem.** For \(a,b\in M\), one has \((a,b)\in\mathcal G(\tau_{-i})\) if and only if

\[
 a\mathfrak n_\varphi^*\subseteq\mathfrak n_\psi^*,\qquad
 \mathfrak n_\psi b\subseteq\mathfrak n_\varphi,\qquad
 \psi(ax)=\varphi(xb)
 \quad(x\in\operatorname{span}\mathfrak n_\varphi^*\mathfrak n_\psi).
 \tag{AG.27}
\]

**Proof with the mixed domains retained.** On \(M_2(M)\) use the balanced weight

\[
 \Omega(X)=\psi(X_{11})+\varphi(X_{22})\quad(X\geq0),
 \qquad A=aE_{12},\quad B=bE_{12}.
 \tag{AG.28}
\]

GC-03/04/08 give \(\sigma_t^\Omega(aE_{12})=\tau_t(a)E_{12}\). The finite left ideal of \(\Omega\) consists of matrices whose first column is in \(\mathfrak n_\psi\) and whose second column is in \(\mathfrak n_\varphi\). Its adjoint ideal has the corresponding first and second **rows** in \(\mathfrak n_\psi^*\) and \(\mathfrak n_\varphi^*\). Matrix multiplication therefore gives exactly

\[
 A\mathfrak n_\Omega^*\subseteq\mathfrak n_\Omega^*
 \iff a\mathfrak n_\varphi^*\subseteq\mathfrak n_\psi^*,
 \qquad
 \mathfrak n_\Omega B\subseteq\mathfrak n_\Omega
 \iff\mathfrak n_\psi b\subseteq\mathfrak n_\varphi.
 \tag{AG.29}
\]

For \(Z\in\mathfrak m_\Omega\), write \(Z\) as a finite sum of products \(Y^*X\) of elements of \(\mathfrak n_\Omega\). Then

\[
 Z_{21}=\sum_{X,Y}\sum_{j=1}^2Y_{j2}^*X_{j1}
 \in\operatorname{span}\mathfrak n_\varphi^*\mathfrak n_\psi.
 \tag{AG.30}
\]

Conversely every elementary product in this span is realized by such a matrix, using one nonzero entry of \(Y\) and one of \(X\) in the same row. Under the inclusions (AG.29), \(AZ,ZB\) are in \(\mathfrak m_\Omega\), and

\[
 \Omega(AZ)=\psi(aZ_{21}),\qquad
 \Omega(ZB)=\varphi(Z_{21}b).
 \tag{AG.31}
\]

Both values are finite complex-linear weight values: for an elementary product \(y^*x\), the left one is \(\psi((ya^*)^*x)\) with both factors in \(\mathfrak n_\psi\), and the right one is \(\varphi(y^*(xb))\) with both factors in \(\mathfrak n_\varphi\).

AG-06 for \(\Omega,A,B\) is thus exactly (AG.27). Finally the matrix strip stays in its 12 corner: all other entries vanish on its real edge, so scalar boundary uniqueness makes them vanish throughout. The 12 entry supplies the relative strip; conversely a relative strip supplies the matrix strip. Their norms agree. This proves VIII.3.25 for arbitrary faithful normal semifinite weights, including all three finite-domain assertions. \(\square\)

## Finite functionals and a noncommuting endpoint

For a bounded positive normal functional \(\varphi\), \(\varphi(x^*x)\leq\|x\|^2\varphi(1)\), so \(\mathfrak n_\varphi=M\). If both \(\varphi,\psi\) are faithful such functionals, AG-07 becomes

\[
 (a,b)\in\mathcal G(\tau_{-i})
 \iff\psi(ax)=\varphi(xb)\quad(x\in M).
 \tag{AG.32}
\]

This proves precisely VIII.3.26. Finiteness of the two functionals is what removes the ideal hypotheses.

For an exact noncommuting example take \(M=M_2(\mathbb C)\), \(\varphi(x)=\operatorname{Tr}(hx)\), \(\psi(x)=\operatorname{Tr}(kx)\), with

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
 k=\begin{pmatrix}5&-3\\-3&5\end{pmatrix},\qquad
 \tau_t(a)=k^{it}ah^{-it},\qquad\tau_{-i}(a)=kah^{-1}.
 \tag{AG.33}
\]

The eigenvalues of \(k\) are \(2,8\), so both functionals are faithful. Cyclicity of the finite trace transforms (AG.32) into \(ka=bh\), because the trace pairing on all matrices is nondegenerate.

For \(a=E_{12}\) the correct endpoint and a reversed-order candidate are

\[
 b=\begin{pmatrix}0&5/4\\0&-3/4\end{pmatrix},\qquad
 b'=h^{-1}ka=\begin{pmatrix}0&5\\0&-3/4\end{pmatrix}.
 \tag{AG.34}
\]

With \(x=E_{21}\) one computes \(\psi(ax)=5\), \(\varphi(xb)=5\), whereas \(\varphi(xb')=20\). This detects the factor order by one finite pairing. The model illustrates the theorem; it does not replace its arbitrary semifinite scope.

## Four solved domain and growth problems

**Problem 1: distinguish two growth conventions.** Show why zeros at all positive imaginary integers cannot determine an arbitrary entire function of usual exponential type. **Solution.** For \(f(z)=\sinh(\pi z)\), \(f(in)=i\sin(\pi n)=0\), while \(|f(z)|\leq e^{\pi|z|}\). Its real-axis values are unbounded, so it fails (AG.10) already at height zero. The disc proof uses that missing horizontal bound to make \(g\) bounded.

**Problem 2: use a graph inclusion in both directions of imaginary time.** Under (AG.14), verify all negative as well as positive imaginary integer values for an element of the first exponential core. **Solution.** For every integer \(k\), the pair \((y_k,y_{k+1})\) belongs to both positive-imaginary graphs. Reverse that pair using (AG.3), giving \(\alpha_{-i}^2(y_{k+1})=y_k\). Repeatedly glue from zero upward and downward. This gives all \(\alpha_{ik}^2(x)=y_k\) and the growth bounds on both half-planes. Equality on an unspecified common dense domain would supply neither the individual iterates nor their strip domains.

**Problem 3: sigma-weak density need not be norm density.** On \(L^\infty(\mathbb R/\mathbb Z)\), let \(\alpha_t f(s)=f(s+t)\). Show that the exponential core is not norm dense. **Solution.** The maps are isometric normal automorphisms; the real orbit is weak-star continuous by translation continuity in the \(L^1\) predual. For \(x=1_{[0,1/2)}\), any sufficiently small nonzero translation changes the indicator on a positive-measure interval, so \(\|\alpha_t x-x\|_\infty=1\). Every element of the entire core has a norm-continuous real orbit. The space of elements with such an orbit is norm closed, since
\(\|\alpha_t x-x\|\leq2\|x-x_j\|+\|\alpha_t x_j-x_j\|\).
Thus this \(x\) cannot be a norm limit of the core, although AG-02 supplies bounded weak-star approximants.

**Problem 4: retain infinite weight masses.** Take an arbitrary nonempty set \(I\), positive numbers \(r_j\), and \(M=\prod_{j\in I}M_2(\mathbb C)\). Define \(\varphi(x)=\sum_j r_j\operatorname{Tr}(hx_j)\) and \(\psi(x)=\sum_j r_j\operatorname{Tr}(kx_j)\) on positive elements, with the matrices of (AG.33). Find the relative generator. **Solution.** Interpret each sum as the supremum of finite subsums. Finite-coordinate truncations prove normality and semifiniteness; strict positivity of the densities proves faithfulness. Blockwise modular calculus gives \(u_t(j)=(r_jk)^{it}(r_jh)^{-it}=k^{it}h^{-it}\), so the masses cancel. The two spectra of \(h,k\) lie in fixed positive compact intervals, and their logarithms are bounded independently of \(j\). Hence \(\tau_z(a)_j=k^{iz}a_jh^{-iz}\) is a norm-entire map on the product, bounded on each horizontal strip. Its generator has domain all of \(M\), with endpoint \(b_j=ka_jh^{-1}\). AG-07 nevertheless uses the actual weighted finite ideals in its pairings. Uniform matrix bounds imply these ideals coincide as sets, are invariant under the indicated bounded block multipliers, and each elementary mixed product has finite absolute weight pairing by weighted Cauchy–Schwarz. The finite-pair equality follows blockwise and summing those absolutely convergent pairings. If \(\sum_jr_j=\infty\), the weights are not finite functionals, so the all-\(M\) complex weight test in (AG.32) is unavailable even though this particular generator has full domain. No countability or boundedness of the masses is assumed.

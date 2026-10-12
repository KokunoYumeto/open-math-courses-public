# Groupoid reductions and modular matrix blocks

A full subset meets every orbit, but passage to that subset need not preserve the size of the associated operator algebra. For a finite principal groupoid it replaces a matrix algebra by a matrix corner. The measure on the different sheets determines the weight on that corner and the domains of its modular operators.

We retain arbitrary groupoids for the algebraic reduction theorem. The operator constructions use **orbitally countable standard Borel principal groupoids**, with a nonzero sigma-finite quasi-invariant unit measure. No ergodicity or uniform bound on finite class sizes is imposed.

## 1. Full reductions and the arrows they retain

An arrow \(\gamma:x\to y\) has source \(s\gamma=x\) and range \(r\gamma=y\). Products \(\gamma\eta\) traverse \(\eta\) first, so they require \(s\gamma=r\eta\). Units, inverses and these endpoint rules are proved in Groupoids and measured orbit relations, Sections 1–4.

A subset \(Y\) of the unit space \(X\) is full if every orbit meets it. The reduction \(\mathcal G|_Y\) retains exactly the arrows with both endpoints in \(Y\).

**Full-reduction theorem.** Every groupoid is similar to its reduction to a full subset. For an orbitally countable standard Borel groupoid and a full Borel subset, the similarity maps can be chosen Borel.

Here similarity means homomorphisms in both directions whose composites are equivalent to the identity homomorphisms by an objectwise field of arrows. This allows nontrivial isotropy.

**Proof.** Choose \(f_x:x\to q(x)\in Y\), choosing the unit when \(x\in Y\). Let \(i\) be inclusion and define

\[
 \rho(\gamma)=f_{r\gamma}\gamma f_{s\gamma}^{-1}.
 \tag{GMB.1}
\]

Its endpoints are \(q(s\gamma)\) and \(q(r\gamma)\). In a composable product, the adjacent factors \(f_{s\gamma}^{-1}f_{r\eta}\) cancel. Hence \(\rho\) is a homomorphism, \(\rho i\) is the identity on the reduction, and (GMB.1) itself exhibits \(i\rho\) as equivalent to the identity on \(\mathcal G\). This proves the arbitrary-set assertion, including the empty case.

At Borel scope the source map \(s:r^{-1}(Y)\to X\) is a surjective countable-fibre Borel map. The complete Lusin–Novikov proof is Transverse measures of foliations, Lemmas 5.2–5.3 and Theorem 5.4. Its Borel section, replaced by unit arrows on \(Y\), supplies Borel \(f\) and \(q\). Borel multiplication makes (GMB.1) Borel. \(\square\)

This is the full assertion of Takesaki XIII.3.6 and its countable Borel enhancement. The earlier complete proof is Compatible lifts and cohomology reduction, Theorem 0.2.

Conjugation by \(f_x\) is an isomorphism

\[
 \mathcal G_x^x\longrightarrow\mathcal G_{q(x)}^{q(x)}.
 \tag{GMB.2}
\]

Its inverse is conjugation by \(f_x^{-1}\). Thus reduction retains isotropy. In contrast, the endpoint map \(\gamma\mapsto(r\gamma,s\gamma)\) discards it; that map is injective exactly for a principal groupoid. For example, reduction of the arrows \((y,k,x)\), with multiplication \((z,l,y)(y,k,x)=(z,lk,x)\), to one object retains the entire group of labels \(k\).

## 2. Countable presentations and null saturation

Let \(\mathcal G\) now be orbitally countable, standard Borel and principal. Its endpoint map is injective and Borel, so the injective Borel image theorem identifies it Borel-isomorphically with a countable Borel equivalence relation \(R\subset X^2\).

The complete presentation theorem is Orbits, stabilizers, and relation algebras, Theorem 1.3 and Corollary 1.4. It proves Takesaki XIII.3.8 for all such groupoids, without a measure or ergodicity hypothesis. Here is its construction, with the exact selection input from Section 1.

Partition the arrows into source-injective Borel pieces by Lusin–Novikov, and partition those pieces again to make the range injective. Their graphs give countably many Borel partial bijections \(\theta:D\to E\). Remove fixed points. A countable Borel family separating points partitions each remaining domain by the first set separating \(x\) and \(\theta x\), and by the orientation of that separation. On each resulting piece \(A\),
\(A\cap\theta A=\varnothing\). Extend \(\theta|_A\) by its inverse on \(\theta A\) and by the identity elsewhere. This is a Borel involution with graph in \(R\).

The countably many involutions generate a countable group \(\Gamma\) of Borel automorphisms. They never leave an \(R\)-class. Conversely every off-diagonal pair of \(R\) belongs to one of their graphs, so their orbits are exactly the \(R\)-classes. The identity handles the diagonal. The presenting action need not be free.

For a sigma-finite unit measure \(\mu\), write

\[
 \begin{split}
 \nu_s(C)&=\int_X\#\{y:(y,x)\in C\}\,d\mu(x),\\
 \nu_r(C)&=\int_X\#\{x:(y,x)\in C\}\,d\mu(y).
 \end{split} \tag{GMB.3}
\]

These are the source and range counting measures; in the source text they are respectively \(\mu_r\) and \(\mu_\ell\). The disjoint partial-bijection graphs make their counts measurable. Intersecting each graph with a finite-\(\mu\) source or range cover proves sigma-finiteness.

For a Borel arrow set \(C\), either count vanishes in integral exactly when its endpoint image is null. Consequently

\[
 \nu_s\sim\nu_r
 \quad\Longleftrightarrow\quad
 \mu(N)=0\ \Longrightarrow\ \mu([N]_R)=0.
 \tag{GMB.4}
\]

For the forward implication apply equivalence to \(s^{-1}(N)\); for the reverse use
\(r(C)\subset[s(C)]_R\) and the reversed inclusion. All images are Borel by the countable-section theorem. This also proves that the presenting automorphisms are nonsingular. The full counting and null-saturation proofs appear in Groupoids and measured orbit relations, Proposition 6.1.

We henceforth assume (GMB.4). The modulus is
\(\delta=d\nu_r/d\nu_s\), with the simultaneous cocycle representative and full sigma-finite weight construction proved in 1. Counting arrows and fixing the derivative through 2. The weight model at infinite mass. The principal relation algebra is denoted \(M\), its diagonal expectation by \(E\), and its weight by

\[
 \varphi_\mu(T)=\int_X E(T)\,d\mu,\qquad T\geq0.
 \tag{GMB.5}
\]


## 3. A full reduction is a full modular corner

Let \(Y\subset X\) be Borel and let \(e=M_{1_Y}\in M\). On
\(H_\mu=L^2(R,\nu_s)\), the projection

\[
 P_Y\xi(y,x)=1_Y(y)1_Y(x)\xi(y,x)
 \tag{GMB.6}
\]

keeps both endpoints. It commutes with the modular multiplication operator and with the modular conjugation, which exchanges the endpoints. The exact corner theorem, including maximal domains and the distinction between \(P_YH_\mu\) and \(eH_\mu\), is 7. Reduction to a measurable subset. It identifies

\[
 M(R|_Y,\mu|_Y)\cong eMe,\qquad
 \varphi_{\mu|_Y}\cong\varphi_\mu|_{eMe}.
 \tag{GMB.7}
\]

The modulus of the reduction is simply the restriction of \(\delta\), since both counting measures restrict to \(R\cap(Y\times Y)\). Also \(e\) is in the centralizer, because every diagonal multiplier is fixed by the modular group. Thus the restricted modular action is the action of the corner weight.

The central support of \(e\) is

\[
 z(e)=M_{1_{[Y]_R}}.
 \tag{GMB.8}
\]

Indeed \(M_{1_{[Y]_R}}\) commutes with the diagonal and every presenting orbit unitary, and dominates \(e\). If a central projection \(z\) dominates \(e\), it dominates \(V_g eV_g^*=M_{1_{gY}}\) for every \(g\in\Gamma\), hence their countable join. That join is precisely the right side of (GMB.8). This proves minimality without an ergodicity assumption.

For full \(Y\), (GMB.8) is \(1\), so (GMB.7) is a full corner. If the relation is ergodic, every positive-measure \(Y\) becomes full on the invariant conull set \([Y]_R\); the same conclusion holds modulo null sets.

Similarity in Section 1 does not assert a unital algebra isomorphism in (GMB.7). On an \(n\)-point full relation, \(M=M_n(\mathbb C)\); reduction to one point gives \(\mathbb C\). For \(n>1\), one is noncommutative and the other commutative. They cannot be isomorphic. The full-corner statement is exactly what these examples satisfy.

A useful measure qualification concerns the retraction \(q:X\to Y\) of Section 1. After taking an equivalent probability \(p\) on \(X\), its pushforward \(q_*p\) is a probability equivalent to \(\mu|_Y\), because for Borel \(A\subset Y\),

\[
 A\subset q^{-1}(A)\subset[A]_R.
 \tag{GMB.9}
\]

The first inclusion uses \(q|_Y=\mathrm{id}\), and (GMB.4) supplies both null implications. This is the complete argument of the earlier reduction lesson, Corollary 0.3. For the original infinite measure, \(q_*\mu\) need not be sigma-finite; Section 8 gives a counterexample.

## 4. Finite sheets without a probability assumption

Suppose all \(R\)-classes are finite, allowing their sizes to be unbounded. Finite orbit classes and matrix blocks, Lemma 1.1 and Corollary 1.2, abbreviated **FCB**, proves the following measurable sorting.

Choose a Borel injection \(\beta:X\to[0,1]\). Enumerate the presenting group. The infimum of \(\beta(gx)\) is a Borel function and is attained on a finite class. Its first attaining index selects the least point \(b(x)\). Repeatedly select the next least distinct value. The resulting ordered points

\[
 x_0(b),\ldots,x_{n-1}(b),\qquad b\in B_n,
 \tag{GMB.10}
\]

are Borel on the Borel set \(B_n\) of representatives of \(n\)-point classes. Their images are Borel by the injective-image theorem. The class-size function is Borel: sum, over the group enumeration, the indicator that the current image differs from all preceding images.

If the source hypothesis says only that the size is \(n\) almost everywhere, first restrict to the invariant conull Borel set \(X_n=\{x:|[x]_R|=n\}\). On that set the \(n\) sheets in (GMB.10) form a partition meeting every class once. No pointwise assertion is made on exceptional classes. This is the measured qualification already proved in FCB Corollary 1.2 for Takesaki XIII.3.12.

Retain the original sigma-finite measure and set \(\nu=b_*\mu\) on
\(B=\bigsqcup_{n\geq1}B_n\). Unlike an arbitrary countable-to-one pushforward, **this \(\nu\) is sigma-finite**. To prove it, choose Borel \(E_k\uparrow X\) with \(\mu(E_k)<\infty\), and put

\[
 B^{(k)}=\{b:\text{every point of the finite class of }b
                    \text{ belongs to }E_k\}.
 \tag{GMB.11}
\]

On each \(B_n\) this is the finite intersection of the tests \(x_i(b)\in E_k\); hence it is Borel. The sets increase to \(B\), since each class is finite, and

\[
 \nu(B^{(k)})=\mu(b^{-1}B^{(k)})\leq\mu(E_k)<\infty.
\]

This proves the claim even when the finite sizes have no common bound.

On \(B_n\) define the sheet measures \(\mu_i(A)=\mu(x_i(A))\). They have the same null sets: a null sheet has null saturation, containing all corresponding sheets. They sum to \(\nu|_{B_n}\). The proved Radon–Nikodym theorem identified in RWT-01 therefore gives

\[
 d\mu_i=p_i\,d\nu,\qquad
 p_i>0,\qquad \sum_{i<n}p_i=1
 \quad\text{almost everywhere on }B_n.
 \tag{GMB.12}
\]

Remove the countably many exceptional base sets. There are finitely many sheets at each remaining point, so all formulas hold simultaneously.

## 5. The matrix weight and its analytic cutoffs

For a relation vector use the coordinates

\[
 (U\xi)_{ij}(b)=p_j(b)^{1/2}\xi(x_i(b),x_j(b)).
 \tag{GMB.13}
\]

The source-counting norm is exactly
\(\sum_n\int_{B_n}\sum_{i,j<n}p_j|\xi(x_i,x_j)|^2\,d\nu\).
Thus \(U\) is a unitary onto the direct sum of
\(L^2(B_n,\nu;\mathrm{HS}_n)\); its inverse divides by \(\sqrt{p_j}\) in these respective Hilbert spaces.

Let \(\theta_{ij}(x_j(b))=x_i(b)\). Its range-coordinate operator becomes left multiplication by \(E_{ij}\), while a diagonal multiplier becomes
\(\operatorname{diag}(f(x_i(b)))\). Central functions are arbitrary functions of \(b\). These generate every bounded measurable \(n\times n\) matrix field: expand its finitely many entries in matrix units. Partial orbit maps give such fields too. The central projections of the \(B_n\)'s then prove

\[
 M\cong\prod_{n\geq1}L^\infty(B_n,\nu;M_n(\mathbb C)).
 \tag{GMB.14}
\]

Here the product consists of families of uniformly essentially bounded matrix norm. This is the exact construction of FCB Theorem 2.1, now with the sigma-finite base justified in Section 4.

Put \(D(b)=\operatorname{diag}(p_0,\ldots,p_{n-1})\). Formula (GMB.5) reads

\[
 \varphi_\mu(T)=
 \sum_n\int_{B_n}\operatorname{Tr}_n(D(b)T(b))\,d\nu(b),
 \qquad T\geq0.
 \tag{GMB.15}
\]

No normalization of \(\mu(X)\) has occurred. RWT-02 proves this weight is faithful, normal and semifinite also when \(\mu(X)=\infty\).

The modulus on the \(ij\)-arrow is \(p_i/p_j\): its range and source counting measures, parametrized by \(b\), have these respective densities. Consequently

\[
 \sigma_t^\mu(T)(b)=D(b)^{it}T(b)D(b)^{-it},\qquad
 \sigma_t^\mu(E_{ij})(b)=(p_i/p_j)^{it}E_{ij}.
 \tag{GMB.16}
\]

Real powers are bounded unitaries, so the first formula defines every real modular time even when the ratios are unbounded over \(B_n\).

A matrix unit is not automatically an entire element of this von Neumann algebra. To obtain an explicit entire algebra, let

\[
 C_k=\{b\in B_n:n\leq k,\ \min_{i<n}p_i(b)\geq1/k\},
 \qquad c_k=1_{C_k}.
 \tag{GMB.17}
\]

These Borel central projections increase strongly to \(1\). On \(C_k\) every ratio lies between \(1/k\) and \(k\). For bounded central \(f\), supported on \(B_n\),

\[
 z\longmapsto f c_k(p_i/p_j)^{iz}E_{ij}
 \tag{GMB.18}
\]

is norm entire and has norm at most
\(\|f\|_\infty k^{|\operatorname{Im}z|}\). Expand the exponential of the bounded logarithm to prove norm convergence and termwise differentiability on bounded complex sets, as in 5. Bounded derivatives give entire modular generators.

The linear span of these cutoff matrix fields and \(1\) is a unital star algebra. For products use \(E_{ij}E_{lm}=1_{\{j=l\}}E_{im}\) and \(C_k\cap C_l=C_{\min(k,l)}\); adjoints reverse the indices. Each element is entire. For any bounded field \(T\), the operators \(c_kT\) are finite sums of these fields and converge strongly to \(T\). Thus this entire algebra generates all of \(M\), with no lower bound on the original sheet densities.

## 6. Relative modular operators on their maximal domains

Let \(q:X\to(0,\infty)\) be finite almost everywhere and let
\(\psi=\varphi_{q\mu}\). Set \(q_i(b)=q(x_i(b))\) and

\[
 D_q(b)=\operatorname{diag}(q_i(b)p_i(b)).
\]

The measure \(q\mu\) is sigma-finite by intersecting a finite-\(\mu\) exhaustion with \(\{q\leq k\}\). The canonical transport between its GNS space and that of \(\mu\) is the source-coordinate multiplication of 3. Unitary transport between equivalent measures. In the common coordinates (GMB.13), the GNS maps are

\[
 \Lambda_\varphi(T)=TD^{1/2},\qquad
 \Lambda_\psi(T)=TD_q^{1/2}
 \tag{GMB.19}
\]

on their respective square-integrable ideals. The identity need not be in either ideal.

The full relative-operator theorem of 4. The mixed graph and its full domain through 5. Canonical standard forms and relative operators, applied to the ratio just computed, gives

\[
 \begin{split}
 (J\eta)_{ij}&=\overline{\eta_{ji}},\\
 (A_{\psi,\varphi}\eta)_{ij}
     &=\left(\frac{q_jp_j}{p_i}\right)^{1/2}\overline{\eta_{ji}},\\
 (\Delta_{\psi,\varphi}\eta)_{ij}
     &=\frac{q_ip_i}{p_j}\eta_{ij},\qquad
 A_{\psi,\varphi}=J\Delta_{\psi,\varphi}^{1/2}.
 \end{split} \tag{GMB.20}
\]

Here \(A_{\psi,\varphi}\) is the closure of
\(\Lambda_\varphi(T)\mapsto\Lambda_\psi(T^*)\). Its domain is

\[
 \left\{\eta:
   \sum_n\int_{B_n}\sum_{i,j<n}
       \frac{q_ip_i}{p_j}|\eta_{ij}|^2\,d\nu<\infty\right\}.
 \tag{GMB.21}
\]

The domain of \(\Delta_{\psi,\varphi}\) has the same formula with the coefficient squared. More generally, for every \(z\in\mathbb C\),

\[
 \begin{split}
 (\Delta_{\psi,\varphi}^{\,z}\eta)_{ij}
       &=\left(\frac{q_ip_i}{p_j}\right)^z\eta_{ij},\\
 D(\Delta_{\psi,\varphi}^{\,z})
       &=\left\{\eta:
       \sum_n\int_{B_n}\sum_{i,j<n}
       \left(\frac{q_ip_i}{p_j}\right)^{2\operatorname{Re}z}
                   |\eta_{ij}|^2\,d\nu<\infty\right\}.
 \end{split} \tag{GMB.22}
\]

In these sets \(\eta\) is already required to belong to the underlying Hilbert space. All powers use the real logarithm of the positive coefficient.

For completeness, the concrete graph-core verification is as follows. Choose a finite-\(\nu\) exhaustion of \(B\), and intersect it with

\[
 n\leq k,\qquad
 p_i\geq1/k,\qquad 1/k\leq q_i\leq k
 \quad\text{for all }i<n.
\]

These central sets increase to \(B\), after making the exhaustion increasing. Restrict further to matrices with bounded entries. The represented kernel
\(T_{ij}=\eta_{ij}/\sqrt{p_j}\) is then bounded, and both
\(\Lambda_\varphi(T)\) and \(\Lambda_\psi(T^*)\) are square integrable. Direct substitution in (GMB.19) proves (GMB.20) on this core. Truncations converge in the graph norm of (GMB.21) by dominated convergence; entrywise amplitude truncation removes the bounded-entry restriction. Multiplication by a positive measurable function is closed on its maximal square-integrability domain: from convergence of a vector and its multiplied vector in \(L^2\), take almost-everywhere convergent subsequences to identify the limit. Thus no smaller closure or unstated bounded-domain assumption occurs. The same truncations with the power weight prove the maximal domains in (GMB.22).

5. Canonical standard forms and relative operators through 6. The normalized cocycle and modular action identifies this GNS transport with the canonical standard form and gives the Connes cocycle. In matrix coordinates it is

\[
 (D\psi:D\varphi)_t=\operatorname{diag}(q_i^{it}).
 \tag{GMB.23}
\]

Indeed the quotient of the two relative imaginary powers cancels \(p_j\) and \(p_i\). Its normalization is that of the actual weights (GMB.15), not of a state obtained by an unspecified rescaling.

## 7. Reduction, normalization and changes in the centre

For a Borel subset \(Y\) of the finite-class space, let
\(I_Y(b)=\{i:x_i(b)\in Y\}\). Its matrix projection is

\[
 e_Y(b)=\sum_{i\in I_Y(b)}E_{ii}.
\]

The corner consists of the matrices on these selected indices. Both \(\varphi\) and \(\psi\) restrict by retaining the corresponding \(p_i\) and \(q_ip_i\) in (GMB.15). Formulas (GMB.20)–(GMB.22) retain **both** indices in \(I_Y(b)\); their coefficients do not change. The projection commutes with the coefficient multipliers and is preserved by \(J\), so it reduces these closed operators and their domains.

The set \(Y\) is full precisely when every \(I_Y(b)\) is nonempty; modulo null sets, the same assertion is equivalent to \(z(e_Y)=1\). If \(Y\) selects one point of each class, its corner is the commutative algebra \(L^\infty(B,\nu)\), although the ambient matrix field algebra need not be commutative.

Suppose the two corner masses

\[
 m=\mu(Y),\qquad n=(q\mu)(Y)
\]

are positive and finite. For the normalized corner states
\(\widehat\varphi=\varphi|_{eMe}/m\) and
\(\widehat\psi=\psi|_{eMe}/n\), the actual cocycle is

\[
 (D\widehat\psi:D\widehat\varphi)_t
       =(m/n)^{it}\sum_{i\in I_Y(b)}q_i^{it}E_{ii}.
 \tag{GMB.24}
\]

Apply (GMB.20) to densities \(p_i/m\) and \(q_ip_i/n\); the ratio is \((m/n)q_i\). This proves the normalization factor. It agrees with the full corner formula in 7. Reduction to a measurable subset.

The modular groups of \(\varphi\) and \(\psi\) agree exactly when \(q_i(b)\) is independent of \(i\) in almost every class. For necessity, apply their equality to every matrix unit on \(B_n\). Formula (GMB.16) gives
\((q_i/q_j)^{it}=1\) for all rational \(t\), simultaneously outside one null set. If a real number \(a\) satisfies \(e^{ia/k}=1\) for every positive integer \(k\), then \(a=0\); apply this to \(a=\log(q_i/q_j)\). For sufficiency the common value \(q_i=a(b)\) is central and cancels in conjugation.

Thus nonconstant positive central rescalings can preserve the whole modular flow while changing the weight and its cocycle. Equal modular groups do not force equality of weights in this nonfactor setting.

## 8. Examples and complete solutions

**Problem 1: a non-sigma-finite pushforward.** Take the pair relation within each fibre of \(X=(0,1)\times\mathbb N\), with Lebesgue measure times counting measure, and retract to \(Y=(0,1)\times\{0\}\). Determine the pushforward and the corner.

**Solution.** For Borel \(A\subset(0,1)\), the pushforward is \(0\) if \(A\) is Lebesgue null and \(+\infty\) otherwise. Every set of finite pushforward measure is null, so countably many such sets cannot cover \(Y\). This pushforward is not sigma-finite, while \(\mu|_Y\) is finite. Multiplying the \(j\)-th sheet by \(2^{-j-1}\), with \(j\geq0\), first produces an equivalent probability whose retraction is Lebesgue measure. The full corner is \(L^\infty(0,1)\); the ambient algebra is \(L^\infty(0,1)\bar\otimes B(\ell^2(\mathbb N))\), by the same row-matrix-unit construction, taking increasing finite row compressions. In this example infinite class size is exactly why the finite-class proof (GMB.11) does not apply.

**Problem 2: proper modular domains over two-point classes.** Let \(B=(0,1)\) with Lebesgue measure, take two sheets with

\[
 p_0(t)=t,\qquad p_1(t)=1-t,
\]

and let \(\eta_{01}(t)=1\), all other entries zero. Test its modular domains.

**Solution.** The vector has Hilbert norm one. With \(q=1\), the coefficient of its only entry is \(t/(1-t)\). The integral of this coefficient diverges at \(1\), so \(\eta\notin D(A_{\varphi,\varphi})=D(\Delta_\varphi^{1/2})\), although every fibre is a two-dimensional matrix algebra.

For \(\zeta_{01}(t)=\sqrt{1-t}\), the half-power integral is \(\int_0^1t\,dt<\infty\), but the full-power integral is \(\int_0^1t^2/(1-t)\,dt=\infty\). Thus \(\zeta\) belongs to the mixed Tomita domain and not to \(D(\Delta_\varphi)\). The divergence follows, for example, by bounding \(t^2\) below by \(1/4\) on \((1/2,1)\).

The matrix unit \(E_{01}\) itself is not entire in operator norm. If it were, first multiply its entire extension by the central indicator of any closed subinterval \(K\subset(0,1)\). On \(K\), the explicit expression \((t/(1-t))^{iz}E_{01}\) is norm entire and agrees on real times. Scalarizing their difference by normal functionals shows equality everywhere: an analytic scalar function with accumulating zeros has no first nonzero Taylor coefficient, and overlapping discs propagate its zero germ along the plane. At \(z=-i\) the hypothetical extension would therefore have \(01\)-entry \(t/(1-t)\) on every such \(K\). These entries are unbounded as the intervals approach \(1\), contradicting membership in \(M\). The cutoffs (GMB.17), in contrast, are entire and converge strongly to this matrix unit.

**Problem 3: normalized restrictions.** In Problem 2 take \(q_0=2\), \(q_1=3\), and restrict to the first sheet. Compute the normalized cocycle.

**Solution.** Here \(m=\int_0^1t\,dt=1/2\) and \(n=2m=1\). Formula (GMB.24) gives
\((m/n)^{it}2^{it}=1\). The two normalized corner states agree. Their unnormalized corner weights differ by \(2\), and their unnormalized cocycle is \(2^{it}\).

**Problem 4: equal flows, distinct states.** On the same two-sheet probability space put \(q_i(t)=2t\) for both indices. What changes?

**Solution.** The new total mass is \(\int_0^1 2t(p_0+p_1)\,dt=1\), so both weights are states. Their modular groups agree because the density is central, but their values on the central projection \(1_{(0,1/2)}\) are \(1/2\) and \(1/4\). At modular time \(u\), the cocycle is the central unitary \((2t)^{iu}1\), which is not scalar when \(u\ne0\).

**Problem 5: the exceptional finite class.** Put masses \(1/2,1/2,0\) on \(\{a,b,c\}\), with classes \(\{a,b\}\) and \(\{c\}\). Can the whole space be divided into two transversals?

**Solution.** Both transversals would have to contain \(c\), contradicting disjointness. The relation is nonsingular because its null singleton is saturated. Its size is two almost everywhere, and its invariant conull two-point part has the required partition \(\{a\}\sqcup\{b\}\). This is the existing FCB Exercise 6.6 correction to the pointwise reading of the source's finite-sheet lemma.

## References

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Proposition 3.6, Theorem 3.8 and Lemma 3.12, printed pp. 34–36. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The complete programme proofs and the existing null-exception qualification are identified above. The sigma-finite matrix-weight, domain and corner calculations here are independently written course exposition. New text is released under CC0.


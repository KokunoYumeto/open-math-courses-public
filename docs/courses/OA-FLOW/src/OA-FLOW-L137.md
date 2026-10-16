# Multiplier innerness, von Neumann uniformity, analytic measures, and positive energy

Four results close the boundary of Takesaki II, Chapter XI, Section 3. They live in different categories and require different proof routes. A derivation of a simple nonunital C*-algebra is implemented in its multiplier algebra, not necessarily in the algebra itself. Point-norm continuity of a flow upgrades to operator-norm continuity only because the algebra is a von Neumann algebra. The F. and M. Riesz theorem turns a one-sided Fourier condition on a measure into absolute continuity. Finally, a positive external implementation of a von Neumann flow can be replaced by a positive implementation affiliated with the algebra.

For the first, we prove the primitive-extension theorem using the programme’s written bidual and representation foundations and the von Neumann innerness theorem proved here. For the second, we prove the full von Neumann automorphism convergence theorem from orthogonal projections, the programme’s written Phillips lemma and projection theory, and the small-automorphism theorem already proved here. The third is proved from the Poisson kernel and an elementary radial estimate. The fourth is derived from the positive-tail criterion already proved in this course.

*New expression is dedicated under CC0 to the extent of rights held; inherited component terms remain in force.*

<a id="boundaries.setting"></a>

## Four targets and their category boundaries

Throughout, a C*-algebra may be nonunital. For such an algebra \(A\), \(M(A)\) denotes its multiplier algebra, realized as the algebra of bounded double centralizers. Every automorphism of a von Neumann algebra preserves the order in both directions, so it preserves each bounded increasing supremum: the image of a least upper bound is again a least upper bound. It is therefore normal by [NF6](OA-FLOW-NF.md#oa-flow.nf.6). For a von Neumann algebra \(M\), a homomorphism

$$\alpha:\mathbb R\longrightarrow\operatorname{Aut}(M) \tag{1}$$

is called point-norm continuous when

$$\|\alpha_t(x)-x\|\longrightarrow0
\qquad(t\longrightarrow0) \tag{2}$$

for each fixed \(x\in M\). Operator-norm continuity means

$$\|\alpha_t-\operatorname{id}_M\|\longrightarrow0. \tag{3}$$

The distinction between (2) and (3) is essential on general C*-algebras: the compact-operator counterexample in lesson 34 satisfies (2) and fails (3).

For the circle \(\mathbb T\), let \(m\) be normalized Haar measure and fix

$$\widehat\mu(n)=\int_{\mathbb T}\zeta^{-n}\,d\mu(\zeta)
\qquad(n\in\mathbb Z). \tag{4}$$

For the positive-energy result, \(M\subset B(K)\) is a faithful normal concrete realization and \(U_t=e^{itH}\) is a strongly continuous unitary group on \(K\).

<a id="boundaries.primitive"></a>

## Sakai's exact primitive-extension theorem

**Theorem.** If $A\ne0$ is a simple C*-algebra, there is a unital primitive C*-algebra $D$ containing $A$ as an essential two-sided ideal. Every complex derivation of $A$ is implemented by an element of $D$, uniquely modulo scalar multiples of $1_D$. Every derivation of $D$ is inner, and $D$ is unique up to an isomorphism fixing $A$.

In particular,

$$\delta(a)=da-ad\qquad(a\in A),\quad d\in D. \tag{5}$$

This is S. Sakai's [Derivations of simple C*-algebras II](https://www.numdam.org/articles/10.24033/bsmf.1719/), *Bull. Soc. Math. France* 99 (1971), Theorem on printed page 260. The proof uses a maximal quotient, an extreme annihilator and a scalar spectral-evaluation contradiction. Its bounded-derivation input is the von Neumann innerness theorem in [lesson 35](OA-FLOW-L35.md#oa-flow.gi.innerness).

The other operator-algebra prerequisites are actual programme lessons. [Every bounded functional becomes normal in one representation](../../OA-MOD/OA-MOD-UB.html#transfer-of-the-algebra-structure-to-the-banach-bidual), sections 2–8, constructs the C*-bidual, its product and normal extensions. [Functionals as vector coefficients](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-01), Proposition 1.1(1), gives the norm-additive positive decomposition of a hermitian functional; [Representations, normal extensions and central corners](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-02), Lemma 2.1, gives the corresponding representation statement. [Pure states and irreducible representations](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html), Lemma 8.1 and Theorems 8.3–8.5, gives the commutant Radon–Nikodym lemma and enough irreducible representations. Continuous and spectral functional calculus and approximate-identity nets retain their full nonseparable scopes. The bidual and arbitrary-representation derivation arguments are also written in [GI11–GI12](OA-FLOW-L35.md#oa-flow.gi.bidual). The maximality and norm separation used below are [CF1](OA-FLOW-CF.md#oa-flow.cf.1); the compactness of arbitrary products of discs is proved in [CF4](OA-FLOW-CF.md#oa-flow.cf.4).

### Derivations extend to the bidual and become spatial

Let $\Delta$ preserve star. It is bounded by [lesson 34](OA-FLOW-L34.md#oa-flow.dfd.algebra). Its second adjoint is a normal star derivation of $A^{**}$. To verify the product rule, first hold $a\in A$ fixed and approximate $Y\in A^{**}$ ultraweakly by elements of $A$. Separate ultraweak continuity of multiplication and of $\Delta^{**}$ gives

$$\Delta^{**}(aY)=\Delta(a)Y+a\Delta^{**}(Y).$$

Then hold $Y$ fixed and approximate $X\in A^{**}$ in the same way. This gives the product rule for $XY$. The star identity follows by the same density argument.

Lesson 35 therefore gives a selfadjoint $h\in A^{**}$ with $\Delta^{**}=i[h,\mathord\cdot]$. If $\pi$ is any nondegenerate representation of $A$, its normal extension gives

$$\pi(\Delta(a))=i[\bar\pi(h),\pi(a)]. \tag{SP.1}$$

There is no assumption that the original derivation is normal in a chosen representation; (SP.1) follows from the bidual first. For a simple nonzero $A$, take a nonzero irreducible representation, which is faithful because its kernel is an ideal. Identify $A$ with this concrete copy. Adding a scalar to the spatial selfadjoint implementer gives $r_0\ge1$ without changing $\Delta=i[r_0,\mathord\cdot]$.

### A maximal quotient with no ideal disjoint from the simple algebra

Put $C_0=C^*(A,r_0)$. This algebra contains the Hilbert-space identity: a continuous function equal to one on the positive spectrum of $r_0$ and zero at zero supplies it in the nonunital functional calculus.

Choose a maximal closed two-sided ideal $J_0$ of $C_0$ with $J_0\cap A=0$. Such an ideal exists by Zorn's lemma. Indeed, each quotient by an ideal disjoint from $A$ is isometric on $A$. If the closure of an increasing chain of these ideals contained an $a\in A$ of norm one, some member would contain a $b$ with $\|a-b\|<1/2$. Its quotient would give $1=\|a+J\|\le\|a-b\|<1/2$, a contradiction.

In $C=C_0/J_0$, the copy of $A$ remains faithful and $r=r_0+J_0\ge1$. Moreover,

$$K\text{ a closed ideal of }C,\quad K\cap A=0
\quad\Longrightarrow\quad K=0. \tag{SP.2}$$

Otherwise the inverse image of $K$ would contradict maximality. At this point $A$ is only a subalgebra of $C$; we have not yet proved it is an ideal. Put $B=A+\mathbb C1_C$, a closed C*-subalgebra, and let $I$ be the closed ideal of $C$ generated by $A$.

Suppose $I\ne A$. Then there is a selfadjoint $s\in I\setminus B$. To see this, if $I\subset B$, the quotient $B/A$ has dimension at most one. Strict containment $A\subsetneq I$ would force $I=B$. Then $1_C\in I$ gives $I=C=B$, in which $A$ is already an ideal, so the ideal it generates is $A$ after all. If $I\not\subset B$, one of the real or imaginary selfadjoint parts of an element outside $B$ is outside $B$.

The hermitian annihilator ball

$$\mathcal S=\{g\in C^*:g=g^*,\ \|g\|\le1,\ g|_B=0\} \tag{SP.3}$$

has an extreme point $g$ with $g(s)>0$. Here are the compactness and extremality details. Hahn–Banach separates $s$ from $B_{\rm sa}$ and gives an element of $\mathcal S$ positive on $s$. The dual unit ball is compact in the pointwise topology: embed it in the product of the discs $\{|z|\le\|x\|\}$, $x\in C$, and note that linearity and the norm inequalities define a closed subset. The hermitian and annihilator constraints are closed as well. Maximizing evaluation at $s$ therefore gives a nonempty compact face with positive maximum. A descending chain of its nonempty closed faces has a nonempty face as its intersection, by compactness. Zorn gives a minimal such face. If it had two distinct functionals, an evaluation on a selfadjoint element would separate them; its maximizing subface would be proper. Thus the minimal face is a point, extreme also in $\mathcal S$. Since $g\ne0$ is extreme in this ball, $\|g\|=1$: otherwise the distinct small radial perturbations $(1\pm\varepsilon)g$ would express it as a midpoint.

### An extreme annihilator forces the coefficient algebra to be a factor

Write $g=g_+-g_-$, where $g_\pm$ are positive and $\|g_+\|+\|g_-\|=1$, and put $\lambda=g_++g_-$. Let $(\pi,H,\xi)$ be the GNS triple of the state $\lambda$. The commutant Radon–Nikodym lemma gives positive contractions $T_\pm\in\pi(C)'$ representing $g_\pm$, with $T_++T_-=1$. Consequently $T=T_+-T_-$ is a selfadjoint contraction and

$$g(x)=\langle\pi(x)T\xi,\xi\rangle,
\qquad \|\xi\|=1. \tag{SP.4}$$

This vector formula gives a normal functional $f$ on $R=\pi(C)''$. Since $g$ vanishes on $B$, $f$ vanishes on $N=\pi(B)''$.

The commutator with the selfadjoint $\pi(r)$ maps $\pi(B)$ into itself. It is ultraweakly continuous, so it maps $N$ into $N$. Apply lesson 35 to the bounded star derivation $i[\pi(r),\mathord\cdot]$ on $N$. There is a selfadjoint $p\in N$ such that

$$q=\pi(r)-p\in N'. \tag{SP.5}$$

Every central projection $e$ of $N$ commutes with $p$, with $q$ and hence with $\pi(r)$. As $C$ is generated by $B$ and $r$, it follows that $e\in Z(R)$.

If $0<e<1$, cyclicity of $\xi$ for $\pi(C)$ gives $0<t=\langle e\xi,\xi\rangle<1$: a central projection killing $\xi$ kills the whole dense cyclic subspace. Define

$$g_e(x)=\langle\pi(x)T e\xi,e\xi\rangle,
\qquad g_{1-e}(x)=\langle\pi(x)T(1-e)\xi,(1-e)\xi\rangle.$$

They are hermitian, their sum is $g$, and their norms are at most $t$ and $1-t$. Because $e$ is central in $N$ and $f|_N=0$, both vanish on $B$. The equality $\|g\|=1$ and the triangle inequality force $\|g_e\|=t$ and $\|g_{1-e}\|=1-t$. Thus

$$g=t\,(g_e/t)+(1-t)\,(g_{1-e}/(1-t))$$

is a convex decomposition in $\mathcal S$. Extremality implies $g_e=tg$. Extend this equality normally to $R$. The functional on its left vanishes on $(1-e)R$, whereas the restriction of $f$ to $(1-e)R$ has norm $1-t>0$, by the preceding vector formula and equality. This contradicts $t>0$. Hence $N$ has no nontrivial central projections. Spectral approximation of central selfadjoint elements now gives

$$N\text{ is a factor}. \tag{SP.6}$$

### Spectral evaluation gives the scalar-shift contradiction

Suppose $\pi(A)\ne0$. Because $A$ is an ideal of $B$, its ultraweak closure is a nonzero ultraweakly closed ideal of the factor $N$, and therefore equals $N$. In particular $\pi|_A$ is a nonzero, hence faithful, representation of the simple algebra.

The selfadjoint $q$ in (SP.5) cannot be scalar. If it were, $\pi(r)\in N$ would imply $R=N$; then $f|_N=0$ would imply $g=0$. Write $X=\sigma(q)$, a compact subset of $\mathbb R$ with at least two points.

We justify evaluation at every $t\in X$ on $C^*(N,q)$. For a finite sum $F(t)=\sum_j a_j u_j(t)$, $a_j\in N$, $u_j\in C(X)$, define $F(q)=\sum_j a_j u_j(q)$. Then

$$\|F(q)\|=\sup_{t\in X}\|F(t)\|. \tag{SP.7}$$

For the upper bound, approximate the finitely many $u_j$ uniformly by step functions on a common finite spectral partition of $q$. The resulting operator is block diagonal, and the norm of a block is at most the norm of its coefficient in $N$. The approximation error is bounded by the sum of the coefficient norms times the scalar errors; letting these errors decrease gives the upper bound.

For the lower bound, fix $t\in X$. A sufficiently small spectral neighborhood $U$ of $t$ has a nonzero spectral projection $e_U$ of $q$. The representation $a\mapsto a|_{e_UH}$ of $N$ is normal because $e_U\in N'$. Its kernel is an ultraweakly closed ideal of the factor $N$; since $e_U\ne0$, the representation is faithful and isometric. Uniform continuity gives

$$\|(F(q)-F(t))e_U\|
\le\sum_j\|a_j\|\sup_{u\in U\cap X}|u_j(u)-u_j(t)|.$$

This can be made arbitrarily small, whereas $\|F(t)e_U\|=\|F(t)\|$. This proves (SP.7). Finite sums of this form are uniformly dense in $C(X,N)$, by uniform continuity and a finite scalar partition of unity on $X$. The map $F\mapsto F(q)$ is therefore an isometric star isomorphism onto $C^*(N,q)$. Evaluation at $t$ is a unital star homomorphism onto $N$.

Since $\pi(B)\subset N$ and $\pi(r)=p+q$, evaluation restricts to a star homomorphism

$$\theta_t:C\longrightarrow N,\qquad
\theta_t(a)=\pi(a)\ (a\in A),\qquad
\theta_t(r)=p+t1. \tag{SP.8}$$

It is faithful on $A$, so its kernel is disjoint from $A$. Property (SP.2) makes $\theta_t$ faithful on all of $C$. Since $r\ge1$, we have $p+t1\ge1$ and

$$\|r\|=\|p+t1\|=\max\sigma(p)+t
\qquad(t\in X). \tag{SP.9}$$

Two different points of $X$ contradict this equality. Thus $\pi(A)=0$.

But then $\pi(I)=0$, since $I$ is the ideal generated by $A$. Formula (SP.4) gives $g(s)=0$, contrary to its choice. The supposition $I\ne A$ was false. We have proved that $A$ is an ideal of $C$, and (SP.2) now makes it an essential ideal. For every star derivation $\Delta$ we have obtained such a unital algebra $C_\Delta$ and a selfadjoint $r_\Delta\ge1$ with $\Delta=i[r_\Delta,\mathord\cdot]$.

### Assemble all implementers in one primitive algebra

Fix one faithful irreducible representation $\rho$ of $A$ on $K$. A nondegenerate representation of an ideal extends to its ambient algebra. For completeness, if $A$ is an ideal of $E$ and $(e_j)$ is a contractive approximate-identity net of $A$, the uniformly bounded operators $\rho(c e_j)$, $c\in E$, converge strongly: on the dense subspace spanned by $\rho(a)\eta$ they converge to $\rho(ca)\eta$. Their strong limit $\widetilde\rho(c)$ satisfies

$$\widetilde\rho(c)\rho(a)\eta=\rho(ca)\eta. \tag{SP.10}$$

This identity proves multiplication. Testing the inner product on two vectors from the dense subspace proves the adjoint identity, and $1_E$ acts as $1_K$. The extension is unique. If $\rho$ is faithful and $A$ is essential in $E$, its kernel is zero, since an element of the kernel annihilates $A$.

Apply this to each $C_\Delta$ and write $R_\Delta=\widetilde\rho(r_\Delta)$. Each $R_\Delta$ multiplies $\rho(A)$ into itself on both sides. Hence

$$D=C^*(\rho(A),1_K,\{R_\Delta:\Delta\text{ a star derivation of }A\}) \tag{SP.11}$$

contains $\rho(A)$ as an ideal: products and sums of generators preserve that property, as do norm limits. It is primitive because it contains the irreducibly acting $\rho(A)$. That ideal is essential, since an operator annihilating $\rho(A)$ annihilates its dense nondegenerate range.

Every complex derivation is a complex linear combination of two star derivations. Explicitly, for $\delta^\sharp(a)=\delta(a^*)^*$, the maps $(\delta+\delta^\sharp)/2$ and $(\delta-\delta^\sharp)/(2i)$ preserve star. Thus the corresponding linear combination of $iR_\Delta$ implements $\delta$ in $D$. Two implementers differ by an operator commuting with the irreducible algebra $\rho(A)$. Each selfadjoint part of such an operator has spectral projections commuting with $\rho(A)$; irreducibility makes their ranges zero or the whole space. Spectral approximation makes each selfadjoint part scalar, and hence their complex combination is scalar.

Let $\varepsilon$ be a derivation of $D$. It preserves $A$: for $a\in A_+$,

$$\varepsilon(a)=\varepsilon(a^{1/2})a^{1/2}
+a^{1/2}\varepsilon(a^{1/2})\in A,$$

and positive elements span $A$. Its restriction therefore has an implementer $d\in D$. The derivation $\eta=\varepsilon-[d,\mathord\cdot]$ vanishes on $A$. For $x\in D$ and $a\in A$,

$$\eta(x)a=\eta(xa)-x\eta(a)=0.$$

Nondegeneracy of $A$ forces $\eta(x)=0$. Hence every derivation of $D$ is inner.

### Uniqueness of the derived algebra

If $D'$ is another unital primitive algebra satisfying the theorem's implementer clauses, $A$ is essential in $D'$. Indeed, in a faithful irreducible representation of $D'$, the nonzero subspace generated by $A$ is the whole space. An ideal disjoint from $A$ annihilates that subspace and is zero. Formula (SP.10) therefore extends the fixed $\rho$ faithfully to $D'$.

For $c\in D'$, its commutator on $A$ has an implementer $d\in D$, so $\widetilde\rho(c)-d$ commutes with $\rho(A)$ and is scalar. Thus $\widetilde\rho(D')\subset D$. Conversely, each star derivation $\Delta$ has an implementer in $D'$; its image differs from $iR_\Delta$ by a scalar. Together with $A$ and the unit, these elements generate $D$, so $D\subset\widetilde\rho(D')$. This proves the required isomorphism fixing $A$. It is unique: two extensions of the identity on $A$ agree after multiplication by every $a\in A$, and essentiality removes their difference. The theorem is proved without a separability or countable-approximate-identity assumption.

<a id="boundaries.embedding"></a>

## An essential ideal embeds its ambient algebra in the multiplier algebra

Let \(A\) be a closed two-sided essential ideal of a C*-algebra \(D\). For \(d\in D\), define

$$L_d(a)=da,\qquad R_d(a)=ad\qquad(a\in A). \tag{6}$$

These maps are bounded and satisfy the double-centralizer identities

$$L_d(ab)=L_d(a)b,\qquad
R_d(ab)=aR_d(b),\qquad
aL_d(b)=R_d(a)b. \tag{7}$$

Thus

$$\iota:D\longrightarrow M(A),\qquad
\iota(d)=(L_d,R_d), \tag{8}$$

is a star homomorphism, unital when \(D\) is unital. It extends the canonical copy of \(A\): if \(d=a\in A\), then \(\iota(a)\) is left and right multiplication by \(a\).

It remains to check injectivity. If \(\iota(d)=0\), then \(dA=Ad=0\). The closed ideal generated by \(d^*d\) is orthogonal to \(A\). Essentiality forces that ideal to be zero, so \(d^*d=0\) and \(d=0\). Hence

$$D\hookrightarrow M(A) \quad\text{faithfully}. \tag{9}$$

This argument is valid without a countable approximate identity, separability, or unitality of \(A\).

We also need the faithful represented meaning of a general multiplier. Fix a faithful nondegenerate representation \(\rho:A\to B(K)\), and a contractive approximate-identity net \((e_j)\). If \((L,R)\) is a bounded double centralizer, the operators \(\rho(L(e_j))\) have norm at most \(\|L\|\). On the dense vectors \(\rho(a)\xi\), the identity \(L(e_j)a=L(e_ja)\) shows that they converge to \(\rho(L(a))\xi\). Their common bound extends the limit to every vector. Denote the resulting bounded operator by \(T\). Then
\[
 T\rho(a)=\rho(L(a)),\qquad
 \rho(a)T=\rho(R(a)).
 \tag{MP1}
\]
The second identity follows from \(aL(e_j)=R(a)e_j\). These identities make the map multiplicative and unique. For the adjoint, compatibility gives \(b^*L(a)=R(b^*)a\); testing scalar inner products on \(\rho(A)K\) yields
\[
 T^*\rho(b)=\rho(R(b^*)^*).
 \tag{MP2}
\]
This is precisely the double-centralizer adjoint. If \(T=0\), faithfulness of \(\rho\) gives \(L=R=0\); the representation is therefore faithful. Its norm equals \(\|L\|\): the construction gives \(\|T\|\le\|L\|\), while (MP1) and isometry of \(\rho\) give the reverse inequality. The usual unit multiplier acts as \(1_K\).

For \(A=K(K)\) in its defining representation, every bounded \(T\) preserves the compact operators on both sides. This follows first for finite-rank operators and then for their norm closure. Hence every \(T\in B(K)\) gives a double centralizer, and (MP1) proves
\[
 M(K(K))=B(K)
 \tag{MP3}
\]
with no dimension restriction. An operator commuting with all rank-one operators is scalar: it leaves each one-dimensional range invariant, and comparison on \(v,w,v+w\), for independent vectors \(v,w\), makes their eigenvalues equal. For a general irreducible representation, the scalar-commutant assertion follows separately from spectral projections. If a selfadjoint operator commutes with the represented algebra, each of its spectral projections does too. Its range and orthogonal complement are invariant, so irreducibility makes each such projection zero or one. Spectral approximation makes the selfadjoint operator scalar. Applying this to the real and imaginary parts proves that every commuting operator is scalar; no rank-one operator is assumed to belong to the represented algebra.

If \(A\) itself is unital, its unit is the ambient unit in every essential unital extension: their difference annihilates \(A\), so essentiality makes it zero. Since \(A\) is an ideal, this forces \(D=A=M(A)\). Thus the theorem includes the statement that all derivations of a unital simple algebra are inner in the algebra itself.


<a id="boundaries.multiplier"></a>

## Simple C*-algebra derivations are multiplier-inner

Let \(A\ne0\) be simple and let \(\delta:A\to A\) be any complex derivation. Apply Sakai's theorem to obtain \(D\) and \(d\in D\) satisfying (5). The preceding irreducible-representation argument makes \(A\) essential in \(D\), so (8)–(9) send \(d\) to a multiplier \(h=\iota(d)\). Because \(\iota\) is the identity on \(A\),

$$\boxed{\delta(a)=ha-ah\qquad(a\in A),\quad h\in M(A).} \tag{10}$$

If \(\delta\) preserves star, the usual adjoint calculation shows that \(h+h^*\) commutes with \(A\). A faithful irreducible representation of the simple algebra extends to \(M(A)\), so a multiplier commuting with \(A\) is scalar. Subtracting half that scalar makes the implementer skew adjoint; equivalently,

$$\delta(a)=i[k,a]\qquad(k=k^*\in M(A)). \tag{11}$$

The location \(M(A)\) is sharp. For \(A=K(\mathcal H)\) with \(\mathcal H\) infinite dimensional, \(M(A)=B(\mathcal H)\). Choose a bounded selfadjoint
\(k\notin K(\mathcal H)+\mathbb C1\), for example a projection of infinite rank and infinite corank. The projection cannot differ from a scalar by a compact operator: choose orthonormal sequences in its range and kernel. A compact operator sends either sequence to zero in norm, because a finite-rank approximation does so and its norm error is uniform. The two sequences would respectively force the scalar to be \(1\) and \(0\). Then \(i[k,\mathord\cdot]\) is a derivation of \(K(\mathcal H)\). If a compact operator implemented the same derivation, its difference from \(ik\) would commute with every compact operator and hence would be scalar, contradicting the choice of \(k\). Thus this derivation has no implementer in \(K(\mathcal H)\).

<a id="boundaries.uniformity"></a>

## Uniform continuity of von Neumann actions

We prove the sequential automorphism theorem needed for the flow, at arbitrary von Neumann algebra scope:

$$
\forall x\in M,\quad \|\beta_n(x)-x\|\longrightarrow0
\quad\Longrightarrow\quad
\|\beta_n-\operatorname{id}_M\|\longrightarrow0,
\qquad \beta_n\in\operatorname{Aut}(M).
\tag{UW.1}
$$

The argument uses three already written programme results. [Phillips's lemma and Schur's theorem](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-12), Lemma 7.1, applies to a bounded sequence of functionals on $\ell^\infty(\Gamma)$ which tends to zero on every indicator function; it concludes that the sum of the absolute values on the individual coordinates tends to zero. [Homogeneous algebras and the structure of type I algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-14), Theorem 10.3, supplies the central homogeneous matrix decomposition. [Orthogonal families of equivalent projections, and halving](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-17), Propositions 13.3–13.4 and Corollary 13.5, supplies equal halves outside type I and countably many copies of a properly infinite unit. These are exact existing prerequisite lessons, with their stated arbitrary-cardinality hypotheses. We derive all the convergence and finite-cover estimates used here.

### Orthogonal projections cannot carry persistent errors

Write $T_n=\beta_n-\operatorname{id}_M$. Then $\|T_n\|\le2$. Suppose $(f_j)$ is an orthogonal sequence of projections and $n_j$ increases to infinity. We claim

$$\|T_{n_j}(f_j)\|\longrightarrow0. \tag{UW.2}$$

Otherwise pass to a subsequence for which these norms exceed some $\varepsilon>0$. Choose functionals $\omega_j\in M^*$ with $\|\omega_j\|\le1$ and

$$|\omega_j(T_{n_j}(f_j))|>\varepsilon/2.$$

For a bounded scalar sequence $a$, the strong sum $\rho(a)=\sum_j a_jf_j$ exists and defines a contractive star homomorphism $\ell^\infty(\mathbb N)\to M$. To see existence, the orthogonal subspaces $f_jK$ give a bounded diagonal operator of norm at most $\sup_j|a_j|$ on their sum, extended by zero on its orthogonal complement; finite partial sums converge strongly to this operator, so it belongs to $M$. Define

$$\mu_j(a)=\omega_j(T_{n_j}(\rho(a))).$$

These functionals have norm at most two. For every subset $E\subseteq\mathbb N$, $\rho(1_E)$ is one fixed projection in $M$, and point-norm convergence gives $\mu_j(1_E)\to0$. Phillips's lemma therefore gives $\sum_i|\mu_j(1_{\{i\}})|\to0$. Its $i=j$ term is greater than $\varepsilon/2$, a contradiction. This proves (UW.2). The functionals need not be normal: no interchange of a functional with an infinite projection sum was used.

There is also a uniform consequence for orthogonal *corners*. If $(p_k)$ is an orthogonal sequence, put

$$d_k=\limsup_{n\to\infty}\|T_n|_{p_kMp_k}\|. \tag{UW.3}$$

Then $d_k\to0$. Indeed a bounded linear map $T$ on a von Neumann corner satisfies

$$\|T\|\le4\sup\{\|T(e)\|:e\text{ is a projection in the corner}\}. \tag{UW.4}$$

For a positive contraction $x$, its spectral step approximants are positive combinations of spectral projections with coefficient sum at most one: for example $m^{-1}\sum_{j=1}^{m}1_{[j/m,1]}(x)$ differs from $x$ by at most $1/m$. Thus the projection supremum bounds $\|T(x)\|$. Split a selfadjoint contraction into its positive and negative parts, and then split an arbitrary contraction into its real and imaginary parts, to obtain the factor four. If $d_k\not\to0$, choose distinct increasing $k_j$ with $d_{k_j}\ge\varepsilon$, increasing $n_j$, and projections $f_j\le p_{k_j}$ with $\|T_{n_j}(f_j)\|>\varepsilon/8$, using (UW.4). These $f_j$ are orthogonal, contradicting (UW.2).

### The action on the centre eventually becomes the identity

First consider an abelian von Neumann algebra $B$ and point-norm convergent automorphisms $\gamma_n\to\operatorname{id}_B$. For each projection $r$, $\gamma_n(r)=r$ eventually: distinct commuting projections have distance one. We show that $\gamma_n$ is the identity on all of $B$ eventually.

Suppose it is not. Starting with $r_0=1$, maintain a projection $r_j$ on whose corner infinitely many $\gamma_n$ act nontrivially. Choose $n_j$ greater than the preceding indices, with $\gamma_{n_j}(r_{j-1})=r_{j-1}$ and nontrivial action on $r_{j-1}B$. Since spectral step functions span that corner densely, choose $e\le r_{j-1}$ with $\gamma_{n_j}(e)\ne e$. The complementary projection $r_{j-1}-e$ is also changed by $\gamma_{n_j}$.

For sufficiently large $n$, both $e$ and $r_{j-1}-e$ are fixed. At least one of their corners still has nontrivial action for infinitely many $n$; otherwise the action on $r_{j-1}B$, the direct sum of these two corners, would eventually be the identity. Retain such a corner as $r_j$ and denote the discarded projection by $f_j$. Then $(f_j)$ is orthogonal and $\|\gamma_{n_j}(f_j)-f_j\|=1$. Applying (UW.2), whose proof only required point-norm convergence and boundedness, gives a contradiction.

Apply this result to $B=Z(M)$ and $\gamma_n=\beta_n|_{Z(M)}$. After discarding finitely many indices we may therefore assume

$$\beta_n(z)=z\qquad(z\in Z(M),\ n\ge1). \tag{UW.5}$$

In particular all the central summands used next are invariant. No faithful normal state or countability condition on the centre is required.

### Small corner errors give a cover-independent bound

Let $p\le q$ be projections, with $q$ central, and suppose that $q$ is a finite sum of orthogonal projections $q_i=v_iv_i^*$, where

$$v_i^*v_i=a_i\le p. \tag{UW.6}$$

The number of $v_i$ is fixed in this paragraph. Assume (UW.5) and put $d=\limsup_n\|T_n|_{pMp}\|$. We prove

$$d<\tfrac14\quad\Longrightarrow\quad
\limsup_n\|T_n|_{qMq}\|\le4d. \tag{UW.7}$$

The constant does not depend on the number of covering projections. This independence is needed when the matrix sizes are unbounded.

If $p=0$, (UW.6) forces $q=0$ and the assertion is immediate. Assume $p\ne0$ in the construction that follows.

Because $\beta_n(p)\to p$ in norm, put

$$b_n=\beta_n(p)p+(q-\beta_n(p))(q-p)\in qMq.$$

It satisfies $\|b_n-q\|=\|\beta_n(p)-p\|\to0$ and $b_np=\beta_n(p)b_n$. For large $n$, $b_n$ is invertible in $qMq$. Its polar unitary $s_n=b_n(b_n^*b_n)^{-1/2}$ tends to $q$ in norm, by continuous functional calculus. Moreover $b_n^*b_n$ commutes with $p$, so $s_nps_n^*=\beta_n(p)$. Extend $s_n$ by $1-q$ and set

$$\eta_n=\operatorname{Ad}(s_n^*+1-q)\circ\beta_n.$$

Then $\eta_n(p)=p$, $\eta_n(q)=q$, and $\|\eta_n-\beta_n\|\to0$. The restriction $\eta_n|_{pMp}$ is an automorphism and has norm distance $c_n$ from the identity with $\limsup_n c_n=d$.

For large $n$, $c_n<1/2$. [Principal logarithms and small automorphisms](OA-FLOW-L135.md) proves that its principal logarithm is a bounded star derivation. The norm-convergent series for the logarithm gives

$$
\|\operatorname{Log}(\eta_n|_{pMp})\|
\le\sum_{j\ge1}\frac{c_n^j}{j}
=-\log(1-c_n)\le2c_n.
\tag{UW.8}
$$

[General innerness](OA-FLOW-L35.md#oa-flow.gi.innerness), including its normalized implementer bound, supplies $h_n=h_n^*\in pMp$ of norm at most $2c_n$ with this derivation equal to $i[h_n,\cdot]$. Hence $w_n=e^{ih_n}$ implements $\eta_n$ on $pMp$ and $\|w_n-p\|\le2c_n$. The exponential is taken in the corner with unit $p$.

Define

$$u_n=\sum_i\eta_n(v_i)w_nv_i^*\in qMq. \tag{UW.9}$$

The final projections $\eta_n(q_i)$ are orthogonal, as are the $q_i$. Since $\eta_n(a_i)=w_na_iw_n^*$, multiplication gives

$$u_n^*u_n=\sum_i v_iw_n^*\eta_n(a_i)w_nv_i^*=q,
\qquad
u_nu_n^*=\sum_i\eta_n(q_i)=q.$$

For $x\in qMq$, expand $x=\sum_{i,j}v_i(v_i^*xv_j)v_j^*$. The middle entries lie in $a_iMa_j\subset pMp$. Applying $\operatorname{Ad}u_n$ to this expansion shows that it equals $\eta_n(x)$, because $w_n$ implements $\eta_n$ on every middle entry. Thus $u_n$ implements $\eta_n$ throughout $qMq$.

Finally,

$$u_n-q
=\sum_i(\eta_n(v_i)-v_i)w_nv_i^*
+\sum_i v_i(w_n-p)v_i^*. \tag{UW.10}$$

The first sum tends to zero in norm: it is finite, the $v_i$ are fixed, and $\eta_n(v_i)\to v_i$. The second sum is block diagonal on the mutually orthogonal $q_i$, and every block has norm at most $\|w_n-p\|$. Its norm is therefore at most $2c_n$, with no factor equal to the number of blocks. The elementary bound $\|\operatorname{Ad}u_n-\operatorname{id}\|\le2\|u_n-q\|$, followed by $\|\eta_n-\beta_n\|\to0$, proves (UW.7).

The small-automorphism and bounded-derivation theorems used here do not assume the point-norm upgrade being proved: the former starts from an operator-norm inequality, and the latter starts from an already bounded derivation and its norm-continuous exponential. Thus the argument is not circular.

### Orthogonal corners covering the large matrix summands

Use the existing projection and type results to write $M$ as the central sum of its part $M_c$ with no type I summand, its properly infinite type I part $M_\infty$, and its finite homogeneous parts

$$M_m\cong M_m(Z_m),\qquad m=1,2,\ldots, \tag{UW.11}$$

where $Z_m$ is abelian and zero summands are allowed. Write their central units as $z_c,z_\infty,z_m$.

In $M_c$, repeatedly halve the unused projection. This gives orthogonal $p_k^c$, $k\ge1$, such that $z_c$ is the sum of $2^k$ projections equivalent to $p_k^c$: after the $k$th halving, its two equal halves can be transported into each of the $2^{k-1}$ equal pieces obtained at the preceding stage. In $M_\infty$, division of the properly infinite unit by $\aleph_0$ gives orthogonal $p_k^\infty\sim z_\infty$.

In $M_m(Z_m)$ choose fixed standard matrix units. For $k\ge1$ set $N_k=2^{k+1}$ and let $p_k^{(m)}$ be a diagonal projection of rank

$$r_k(m)=\lfloor m/N_k\rfloor.$$

Choose its diagonal slots just after all the slots used at earlier stages. This is possible because $\sum_{k\ge1}r_k(m)\le m/2$. These projections are orthogonal as $k$ varies. If $m\ge N_k$, then $r_k(m)\ge m/(2N_k)$, so the $m$ diagonal slots can be partitioned into at most $2N_k$ groups of size at most $r_k(m)$. Each group's projection is equivalent, by a fixed matrix partial isometry, to a subprojection of $p_k^{(m)}$.

Now form the strong central sums

$$
p_k=p_k^c+p_k^\infty+\sum_{m\ge N_k}p_k^{(m)},
\qquad
q_k=z_c+z_\infty+\sum_{m\ge N_k}z_m.
\tag{UW.12}
$$

The $p_k$ are orthogonal. For each fixed $k$, $q_k$ is a sum of at most $2N_k$ orthogonal projections equivalent to subprojections of $p_k$. To assemble the partial isometries, pad the finite lists on each central summand by zeros and take their strong sums across the orthogonal central units. These sums are bounded by one, their initial and final projections are the corresponding strong sums, and they belong to $M$. Thus (UW.6) holds exactly, even with arbitrary multiplicities and a non-countably decomposable $M$.

### Completing the sequential theorem and the flow implication

Let $d_k$ be (UW.3) for these $p_k$. We proved $d_k\to0$. For every sufficiently large $k$, (UW.7) gives

$$\limsup_n\|T_n|_{q_kMq_k}\|\le4d_k. \tag{UW.13}$$

The complementary algebra has only finitely many finite homogeneous sizes $m<N_k$. On each of them, (UW.5) makes $\beta_n$ linear over $Z_m$. Writing $x=\sum_{i,j}a_{ij}E_{ij}$ with $a_{ij}\in Z_m$ and $\|a_{ij}\|\le\|x\|$ gives

$$\|T_n|_{M_m(Z_m)}\|
\le m^2\max_{i,j}\|\beta_n(E_{ij})-E_{ij}\|
\longrightarrow0. \tag{UW.14}$$

There are finitely many such summands, so $\|T_n|_{(1-q_k)M}\|\to0$. Since $q_k$ is central and fixed, $T_n$ preserves the two central blocks and its norm is the maximum of the two restricted norms. Consequently $\limsup_n\|T_n\|\le4d_k$ for every sufficiently large $k$. Letting $k\to\infty$ proves (UW.1). If $M$ has only bounded finite homogeneous sizes, the same conclusion follows directly from (UW.14); zero $p_k$ and $q_k$ present no exception.

For the real flow, failure of (3) would give $\varepsilon>0$ and a sequence $t_n\to0$ with $\|\alpha_{t_n}-\operatorname{id}_M\|\ge\varepsilon$. Condition (2) says that the automorphisms $\beta_n=\alpha_{t_n}$ converge pointwise in norm. Applying (UW.1) is a contradiction. We have therefore proved

$$
\bigl[\ \forall x\in M,\ \|\alpha_t(x)-x\|\to0\ \bigr]
\quad\Longrightarrow\quad
\|\alpha_t-\operatorname{id}_M\|\to0. \tag{12}
$$

This is a sequential argument for the first-countable real parameter. It introduces no factor, separability, sigma-finiteness or faithful-state hypothesis. The uniform boundedness principle alone would only bound the already isometric $\alpha_t$; the orthogonal-projection and cover-independent estimates supply the decay.

Kallman's 1969 and 1970 work gives the historical flow result, as credited in Takesaki's notes. Elliott's [On the convergence of a sequence of completely positive maps to the identity](https://doi.org/10.1017/S1446788700001439), Theorem 1, printed page 341, proves a stronger statement for completely positive maps on AW* algebras and their quotients. That stronger theorem is research context here; the proof above supplies the full von Neumann automorphism statement actually used in (12), through the programme's written prerequisites. It does not claim a proof for general completely positive maps, AW* algebras or their quotients.

### A matrix-product example shows why the von Neumann hypothesis matters

Let $M=\prod_{m\ge2}M_m(\mathbb C)$, the algebra of bounded matrix families. Define $\theta_n$ to act only on the $n$th factor, $n\ge2$, by conjugation with $\operatorname{diag}(-1,1,\ldots,1)$. Its norm distance from the identity is two: the matrix unit $E_{12}$ in that factor is sent to $-E_{12}$, and two is the general upper bound for the difference of isometries. The bounded family $x=(E_{12}^{(m)})_{m\ge2}$ lies in $M$ and satisfies $\|\theta_n(x)-x\|=2$ for every $n$. Thus this sequence cannot satisfy the point-norm hypothesis of (UW.1).

On the C*-algebra $A=\bigoplus_{m\ge2}^{c_0}M_m(\mathbb C)$, the same automorphisms do converge pointwise in norm: $\|\theta_n(a)-a\|\le2\|a_n\|\to0$ for each $a\in A$. They still have norm distance two from the identity. The test family $x$ belongs to the von Neumann product and is excluded from the $c_0$ sum; it detects precisely the error that point-norm convergence on the smaller algebra misses. This gives a finite-matrix counterpart of the compact-operator example from lesson 34.


<a id="boundaries.generator"></a>

## Uniform continuity gives a bounded internal generator

Regard \(\alpha_t\) as a group of isometries of the Banach space \(M\). By (12) it is operator-norm continuous. The [uniform-flow theorem in lesson 34](OA-FLOW-L34.md#oa-flow.dfd.implementation) therefore gives a bounded star derivation

$$d(x)=\lim_{t\to0}\frac{\alpha_t(x)-x}{t},
\qquad
\alpha_t=e^{td}. \tag{13}$$

The [general von Neumann innerness theorem in lesson 35](OA-FLOW-L35.md#oa-flow.gi.innerness) supplies a bounded selfadjoint \(h\in M\) such that

$$d(x)=i[h,x]. \tag{14}$$

The commuting left-right exponential calculation then yields

$$e^{td}(x)=e^{ith}xe^{-ith}. \tag{15}$$

Consequently

$$\boxed{\alpha_t=\operatorname{Ad}(e^{ith}),\qquad h=h^*\in M,} \tag{16}$$

and

$$\|\alpha_t-\operatorname{id}_M\|
\le e^{|t|\|d\|}-1\longrightarrow0. \tag{17}$$

Thus the conclusion includes both assertions in Exercise XI.3.6. It does not say that a merely point-ultraweakly continuous flow has a bounded generator; modular automorphism groups provide the central reason to keep that distinction.

<a id="boundaries.analytic"></a>

## The analytic ingredients for the radial estimate

We use “analytic” to mean locally represented by a convergent complex power series. Such series have continuous derivatives, by uniform convergence of the differentiated series on smaller discs. Here are the disc facts needed below, with their proofs.

**Taylor expansion throughout a disc.** If \(f\) is analytic on \(|z|<R_0\), fix \(R<R_0\). For \(|w|<R\), the function
\[
 h(z)=\frac{f(z)-f(w)}{z-w}
\]
extends analytically at \(w\), by its local series. The circle-mean calculation in [CF2](OA-FLOW-CF.md#oa-flow.cf.2), applied to \(zh(z)\), gives \(\int_{|z|=R}h(z)\,dz=0\). The geometric expansion of \(1/(z-w)\) on that circle has integral \(2\pi i\). Consequently
\[
 f(w)=\frac{1}{2\pi i}\int_{|z|=R}\frac{f(z)}{z-w}\,dz
      =\sum_{n\ge0}c_nw^n,\qquad
 c_n=\frac{1}{2\pi i}\int_{|z|=R}\frac{f(z)}{z^{n+1}}\,dz.
 \tag{AN1}
\]
The geometric series is uniformly convergent for \(|w|\le r<R\), which licenses its integration. If \(M_R=\max_{|z|=R}|f(z)|\), then \(|c_n|\le M_RR^{-n}\). Thus the resulting Taylor series and its differentiated series converge uniformly on each smaller closed disc. Local uniqueness of coefficients identifies the expansions for different \(R\).

**Zeros and analytic square roots.** The first nonzero coefficient of a local Taylor series factors a zero as \((z-a)^m\) times a nonvanishing analytic function. If zeros accumulate at an interior point, all its coefficients vanish, and the function vanishes in a neighborhood. The set where it vanishes in a neighborhood is both open and closed in the disc: at a limit point, either that point already belongs to the set or accumulating zeros force the same local conclusion. The disc is connected by line segments. Hence a nonzero analytic function has isolated zeros and only finitely many zeros in a compact subdisc.

If \(F\) is zero-free on a disc, \(F'/F\) is analytic there: the reciprocal is locally given by a geometric series. Expand \(F'/F\) at zero by (AN1), integrate its coefficients, and call the primitive \(H\), normalized by \(H(0)=0\). Termwise differentiation gives \(H'=F'/F\), so \((Fe^{-H})'=0\). Restricting to line segments and using the real fundamental theorem from [CF1](OA-FLOW-CF.md#oa-flow.cf.1) gives \(Fe^{-H}=F(0)\). Choose a scalar \(c\) with \(c^2=F(0)\). Then
\[
 c\,e^{H/2}
 \tag{AN2}
\]
is an analytic square root of \(F\) throughout the disc.

**A finite product removes exactly the interior zeros.** For \(0<\rho<1\) and a zero \(a\) with \(|a|<\rho\), put
\[
 B_a(z)=\frac{\rho(z-a)}{\rho^2-\overline a z}.
 \tag{AN3}
\]
Its denominator has no zero on the closed \(\rho\)-disc, and
\[
 |\rho^2-\overline a z|^2-\rho^2|z-a|^2
    =(\rho^2-|a|^2)(\rho^2-|z|^2).
 \tag{AN4}
\]
Thus \(|B_a|\le1\) there and equals \(1\) on the boundary. If \(f\) has no zero on that boundary, multiply one factor for each interior zero, with its multiplicity; there are finitely many. The quotient \(F=f/B\) has removable singularities at precisely those zeros and no remaining zero on the closed disc. Compactness and continuity give a slightly larger disc on which the quotient is analytic and zero-free. Formula (AN2) applies on that disc. The empty product is \(1\).

Finally, normalized arc measure satisfies
\(\int_{\mathbb T}\zeta^n\overline{\zeta^m}\,dm=\delta_{nm}\), by integrating \(e^{i(n-m)t}\) on \([0,2\pi]\). Applying this to finite partial sums, then using uniform convergence from (AN1), proves the power-series \(L^2\) identities used next. All radii in the next proof lie strictly inside the analyticity disc.

<a id="boundaries.radial"></a>

## An elementary radial estimate for analytic functions

For an analytic function \(f\) on the unit disc write

$$f_r(\zeta)=f(r\zeta),\qquad
N(r)=\|f_r\|_{L^1(\mathbb T,m)}. \tag{18}$$

We prove the estimate

$$\boxed{
\|f_\rho-f_r\|_1
\le2\sqrt{N(\rho)^2-N(r)^2}
\qquad(0\le r\le\rho<1).
} \tag{19}$$

If \(\rho=0\), then \(r=0\) and both sides of (19) vanish. The zero function also gives the inequality immediately. Assume henceforth that \(f\ne0\) and \(\rho>0\). First suppose that \(f\) has no zero on \(|z|=\rho\). Take the finite Blaschke product \(B\) constructed in (AN3)–(AN4) for the zeros of \(f\) in the disc of radius \(\rho\), normalized so that

$$|B(z)|=1\quad(|z|=\rho),\qquad
|B(z)|\le1\quad(|z|\le\rho). \tag{20}$$

Then \(F=f/B\) is analytic and zero-free on a neighborhood of the closed \(\rho\)-disc. It has an analytic square root there. Put

$$g=B F^{1/2},\qquad h=F^{1/2},\qquad f=gh. \tag{21}$$

On the outer circle,

$$\|g_\rho\|_2^2=\|h_\rho\|_2^2=N(\rho). \tag{22}$$

Write \(a=\|g_r\|_2\), \(b=\|h_r\|_2\), and \(c=N(\rho)^{1/2}\). The power-series orthogonality identity gives

$$\|g_\rho-g_r\|_2^2
\le c^2-a^2,\qquad
\|h_\rho-h_r\|_2^2
\le c^2-b^2. \tag{23}$$

Indeed, term by term,

$$(\rho^n-r^n)^2\le\rho^{2n}-r^{2n}. \tag{24}$$

The factorization and Cauchy–Schwarz now give

$$
\begin{aligned}
\|f_\rho-f_r\|_1
&\le\|(g_\rho-g_r)h_\rho\|_1
  +\|g_r(h_\rho-h_r)\|_1\\
&\le c\sqrt{c^2-a^2}+a\sqrt{c^2-b^2}. 
\end{aligned} \tag{25}
$$

Moreover \(N(r)\le ab\), while \(a,b\le c\). Each summand in (25) is at most

$$\sqrt{c^4-a^2b^2}
\le\sqrt{N(\rho)^2-N(r)^2}. \tag{26}$$

This proves (19), and also proves \(N(r)\le N(\rho)\). If \(f\) has a zero on the circle of radius \(\rho\), approximate \(\rho\) by radii avoiding the discrete zero set and pass to the limit by continuity. The case \(f=0\) is immediate.

The finite-Blaschke proof of (19) is included so that no Fatou boundary theorem or inner-outer factorization theorem is hidden in the next argument.

<a id="boundaries.riesz"></a>

## The F. and M. Riesz theorem

Let \(\mu\) be a finite complex Borel measure on \(\mathbb T\) satisfying

$$\widehat\mu(n)=0\qquad(n<0). \tag{27}$$

The Poisson kernel is

$$P_r(\zeta)=\sum_{n\in\mathbb Z}r^{|n|}\zeta^n
=\frac{1-r^2}{|1-r\zeta|^2}. \tag{28}$$

Define

$$f_r(\zeta)
=\int_{\mathbb T}P_r(\zeta\overline\eta)\,d\mu(\eta). \tag{29}$$

Condition (27) removes every negative Fourier term, so these are the radial values of the analytic function

$$f(z)=\sum_{n=0}^\infty\widehat\mu(n)z^n. \tag{30}$$

Positivity and unit mass of \(P_r\), followed by Fubini, give

$$\|f_r\|_1\le\|\mu\|_{\mathrm{TV}}. \tag{31}$$

The increasing function \(N(r)=\|f_r\|_1\) therefore has a finite limit as \(r\uparrow1\). Estimate (19) shows that \((f_r)\) is Cauchy in \(L^1(\mathbb T)\): if \(r,\rho\) are close to one, the difference \(N(\rho)^2-N(r)^2\) is small. Let

$$f_r\longrightarrow f^*\quad\text{in }L^1(\mathbb T). \tag{32}$$

The approximate-identity assertion also follows directly from (28). The geometric series proves that formula and its uniform absolute convergence for \(r<1\). Its constant Fourier coefficient is \(1\), so its integral is \(1\), and the displayed quotient makes it nonnegative. Fix \(\delta>0\). When \(|1-\zeta|\ge\delta\) and \(1-r<\delta/2\),
\[
 |1-r\zeta|\ge\delta/2,\qquad
 0\le P_r(\zeta)\le4(1-r^2)/\delta^2.
 \tag{AN5}
\]
For continuous \(\varphi\), split its convolution difference into \(|1-\zeta|<\delta\) and the complement. Unit mass bounds the first part by the uniform modulus of continuity of \(\varphi\); (AN5) bounds the second by \(8\|\varphi\|_\infty(1-r^2)/\delta^2\). Choosing \(\delta\) first and then \(r\uparrow1\) proves uniform convergence to \(\varphi\). The kernel is invariant under \(\zeta\mapsto\overline\zeta\), so the convolution orientation in the following identity is the same as in (29). For every \(\varphi\in C(\mathbb T)\), Fubini gives

$$
\int_{\mathbb T}\varphi(\zeta)f_r(\zeta)\,dm(\zeta)
=\int_{\mathbb T}(P_r*\varphi)(\eta)\,d\mu(\eta)
\longrightarrow\int_{\mathbb T}\varphi\,d\mu. \tag{33}
$$

The \(L^1\)-limit in (32) makes the left side converge to

$$\int_{\mathbb T}\varphi f^*\,dm. \tag{34}$$

Uniqueness in the [Riesz representation theorem HR2](OA-FLOW-HR.md#hr-02) therefore gives

$$\boxed{d\mu=f^*\,dm.} \tag{35}$$

Thus every finite analytic measure on the circle is absolutely continuous. The argument preserves the convention (4); reversing the Fourier convention reverses which half of the coefficients must vanish.

<a id="boundaries.external"></a>

## A positive external group forces vanishing intrinsic tails

Let \(U_t=e^{itH}\) be a strongly continuous unitary group on \(K\), assume \(H\ge0\), and suppose

$$U_tMU_t^*=M\qquad(t\in\mathbb R). \tag{36}$$

Then

$$\alpha_t(x)=U_txU_t^*\qquad(x\in M) \tag{37}$$

is a point-ultraweakly continuous automorphism group. Let \(P\) be the spectral measure of \(H\), so \(P([0,\infty))=1\).

For the intrinsic Arveson spectral subspace \(M_\alpha([s,\infty))\), let \(Q_s\) be the join in \(M\) of its left supports, with the positive Fourier convention and left-support notation of [L86](OA-FLOW-L86.md#positiveflow.setting). The [operator-to-vector spectral transfer theorem](OA-FLOW-L80.md#sum-claim), with its Hilbert and normal-inclusion hypotheses verified in [L86](OA-FLOW-L86.md#positiveflow.models), gives

$$xP([r,\infty))K
\subset P([r+s,\infty))K
\quad
\bigl(x\in M_\alpha([s,\infty))\bigr). \tag{38}$$

Put \(r=0\). Since \(P([0,\infty))=1\),

$$xK\subset P([s,\infty))K. \tag{39}$$

Taking left supports and then their join yields

$$Q_s\le P([s,\infty)). \tag{40}$$

Spectral tails of a selfadjoint operator decrease strongly to zero, hence

$$\bigwedge_{s\in\mathbb R}Q_s
\le\bigwedge_{s\in\mathbb R}P([s,\infty))=0. \tag{41}$$

The external group is used only to prove the intrinsic condition (41). Its unitaries need not belong to \(M\).

<a id="boundaries.internal"></a>

## The positive tail criterion constructs the internal group

[L86's positive-tail criterion](OA-FLOW-L86.md#positiveflow.recovery) proves the converse direction at exactly these hypotheses. From (41), regularize the tails by

$$E_s=\bigwedge_{r<s}Q_r. \tag{42}$$

The projections \(E_s\) lie in \(Z(M^\alpha)\), form the closed tails of a projection-valued measure \(E\) supported in \([0,\infty)\), and define

$$V_t=\int_{[0,\infty)}e^{it\lambda}\,dE(\lambda)\in M. \tag{43}$$

The [shifted-tail transfer](OA-FLOW-L86.md#positiveflow.shift) and [compact spectral recovery](OA-FLOW-L86.md#positiveflow.recovery) prove

$$\alpha_t=\operatorname{Ad}V_t. \tag{44}$$

The [full-domain spectral construction](OA-FLOW-L86.md#positiveflow.measure) gives

$$V_t=e^{itL},\qquad
L=\int_{[0,\infty)}\lambda\,dE(\lambda)\ge0. \tag{45}$$

Every spectral projection of \(L\) lies in \(M\), so \(L\) is affiliated with \(M\). It may be unbounded, which is why (45) is a strong-operator spectral integral rather than an element of \(M\).

<a id="boundaries.positive"></a>

## Positive external implementation becomes positive internal implementation

Combining (36)–(45) proves the Borchers–Arveson conclusion:

$$
\boxed{
U_t=e^{itH},\ H\ge0,\ U_tMU_t^*=M
\ \Longrightarrow\
\exists\,L\ge0\text{ affiliated with }M:
\alpha_t=\operatorname{Ad}(e^{itL}).
} \tag{46}
$$

No factor, separability, sigma-finiteness, cyclic-vector, separating-vector, or invariant-state hypothesis was introduced. The proof does not claim that the external generator \(H\) belongs to \(M\), nor that the internal generator \(L\) is bounded. It identifies the exact mechanism: external positivity forces the intrinsic high-frequency tail to vanish, and the canonical tail measure supplies a positive internal implementation.

**Source locators.** Multiplier innerness is Takesaki II, Exercise XI.3.1, printed page 358, using Sakai's Theorem on page 260 and the local essentiality and multiplier-embedding proofs above. The point-norm upgrade is Exercise XI.3.6, printed page 361; it follows here from the proved von Neumann automorphism sequence theorem (UW.1), by the explicit sequential contradiction, followed by the bounded-generator arguments in lessons 34–35. The broader completely-positive-map theorem is credited as research context and is not used as a proof substitute. The analytic-measure and positive-implementation statements occur in the Notes on Chapter XI on the same printed page. The F. and M. Riesz proof above is complete under the stated measure and complex-analysis foundations; the radial estimate follows the finite-Blaschke method of O. F. Brevig, [Two footnotes to the F. & M. Riesz theorem, version 2](https://arxiv.org/abs/2407.06843v2), Lemma 2 on page 2 and its proof in Section 2 on page 4. The positive implementation proof uses the full intrinsic criterion in L86, including its spectral-measure construction and exact representation transport.

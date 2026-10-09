# Fredholm operators and the stable index

*GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Public domain (CC0 1.0).*

An operator can fail to be invertible in a finite number of directions while behaving like an isomorphism everywhere else. Fredholm operators make this precise. Compact perturbations can change the individual numbers of missing directions, but preserve their difference. That difference also classifies the connected components of the invertible group of the Calkin algebra on a separable infinite-dimensional Hilbert space.

Prerequisites are [C*-algebras and quotients](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-25), [Representations and positive functionals](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html), [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html), and [Invertible components and exponential laws](../reader/invertible-components-and-exponential-laws.html). The bounded inverse theorem is proved below. We also use orthogonal projections, compactness of the image of a bounded sequence under a compact operator, and the [polar decomposition \(T=U|T|\)](../reader/normal-products-and-closed-operator-graphs.html#polar-decomposition-for-closed-operators), whose full proof applies in particular to bounded operators. When constructing logarithms of unitaries, we use the [cyclic multiplication representation](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html#oa-fnd-ao-03), Theorem 3.1. A freely readable account is Blackadar’s *Operator Algebras*; the proofs below spell out the defect counts and continuity arguments.

Unless specified otherwise, \(H\) can be any infinite-dimensional complex Hilbert space. Let \(K(H)\) be the compact operators, let \(Q(H)=B(H)/K(H)\), and let \(q:B(H)\to Q(H)\) be the quotient map. An operator \(T\) is **Fredholm** when \(q(T)\) is invertible. We use the sign convention
\[
\kappa(T)=\dim\ker T^*-\dim\ker T.
\tag{0.1}
\]
Thus the unilateral shift has index \(+1\). A common alternative convention has the opposite sign; formulas in this lesson use (0.1).

In particular, [Blackadar, I.8.3.1–3] uses \(\operatorname{index}(T)=\dim\ker T-\dim\ker T^*\). Translating from that reference requires \(\kappa(T)=-\operatorname{index}(T)\). The sign changes the integer assigned to a component; additivity and stability remain the same.

## Why the partial inverse is bounded

**Lemma 0.1 (Baire).** If a nonempty complete metric space is a countable union of closed sets, at least one of them has nonempty interior.

**Proof.** Use Theorem 3.1 of Hahn–Banach, Baire and the basic theorems on Banach spaces, whose proof shows that every countable intersection of dense open subsets of a nonempty complete metric space is dense. If all the closed sets in the stated cover had empty interior, their complements would be dense open sets. The intersection of those complements would be both dense and empty, since the closed sets cover the space. A dense subset of a nonempty space cannot be empty. This contradiction proves the assertion. \(\square\)

**Lemma 0.2 (Bounded inverse).** A bounded linear bijection \(T:X\to Y\) between Banach spaces has a bounded inverse.

**Proof.** We first prove a preimage estimate for every bounded surjection \(T:X\to Y\) between Banach spaces. The case \(Y=\{0\}\) is immediate, so assume \(Y\ne\{0\}\). Let \(B_X\) be the closed unit ball of \(X\), and set
\[
A=\overline{T(B_X)}.
\]
The set \(A\) is closed, convex and balanced. Surjectivity implies \(Y=\bigcup_{n\geq1}nA\): a preimage of any vector belongs to \(nB_X\) for some positive integer \(n\). Lemma 0.1 gives \(B(y_0,r)\subseteq nA\) for some \(r>0\). If \(\|w\|<r\), both \(y_0+w\) and \(y_0\) lie in \(nA\), so
\[
w\in nA-nA\subseteq 2nA.
\]
The last inclusion follows because the average of a point of \(A\) and the negative of another point of \(A\) lies in \(A\). With \(\delta=r/(2n)\), we obtain
\[
B(0,\delta)\subseteq A.
\]

Put \(a=2/\delta\). For every nonzero \(v\in Y\), the vector \(v/(a\|v\|)\) has norm \(\delta/2\) and belongs to \(A\). By the definition of closure, choose \(u\in B_X\) whose image is within \(1/(3a)\) of that vector. Multiplying by \(a\|v\|\) gives a vector \(x\in X\) such that
\[
\|x\|\leq a\|v\|,\qquad
\|v-Tx\|\leq\tfrac13\|v\|.
\]
For \(v=0\), take \(x=0\).

Starting with \(v_0=y\), apply this estimate repeatedly to obtain \(x_j\in X\) and \(v_j=v_{j-1}-Tx_j\). Then
\[
\|v_j\|\leq 3^{-j}\|y\|,\qquad
\|x_j\|\leq a\,3^{-(j-1)}\|y\|.
\]
The partial sums of \(\sum_{j\geq1}x_j\) are Cauchy by the second estimate. Completeness of \(X\) gives their limit \(x\), with
\[
\|x\|\leq\tfrac32 a\|y\|=\frac3\delta\|y\|.
\]
Continuity of \(T\) and the first estimate imply
\(Tx=\lim_j(y-v_j)=y\). Thus every \(y\) has a preimage with norm at most \(K\|y\|\), where \(K=3/\delta\).

This also proves the open mapping theorem. If an open subset \(O\subseteq X\) contains \(x_0\), choose \(\varepsilon>0\) with \(x_0+B(0,\varepsilon)\subseteq O\). Every \(y\) of norm less than \(\varepsilon/K\) has a preimage of norm less than \(\varepsilon\). Therefore \(Tx_0+B(0,\varepsilon/K)\subseteq T(O)\), making \(T(O)\) open.

When \(T\) is bijective, its preimage of \(y\) is uniquely \(T^{-1}y\). The preimage estimate gives \(\|T^{-1}y\|\leq K\|y\|\). The inverse is linear because \(T\) is linear and injective, so it is bounded. In the excluded case \(Y=\{0\}\), bijectivity also gives \(X=\{0\}\), with bounded zero inverse. \(\square\)

In Theorem 1.1, the closed subspaces \((\ker T)^\perp\) and \(T(H)\) are Banach spaces. Lemma 0.2 therefore applies to the restriction between them, exactly where the partial inverse is constructed.

## 1. Invertibility modulo compact operators

**Theorem 1.1.** An operator \(T\in B(H)\) is Fredholm exactly when its range is closed and both \(\ker T\) and \(\ker T^*\) are finite-dimensional. In that case there is \(R\in B(H)\) with
\[
RT=1-P_{\ker T},\qquad TR=1-P_{\ker T^*}.
\tag{1.1}
\]

**Proof.** If \(q(T)\) is invertible, choose a lift \(S\) of its inverse. Then \(ST=1+C\) and \(TS=1+D\), with \(C,D\) compact. On \(\ker T\), \(C=-1\). The identity on an infinite-dimensional Hilbert space is not compact, as an infinite orthonormal sequence shows, so \(\ker T\) is finite-dimensional. Taking adjoints of \(TS=1+D\) gives the same conclusion for \(\ker T^*\).

To prove closed range, it suffices to prove \(T\) is bounded below on \(X=(\ker T)^\perp\). Otherwise choose \(\xi_n\in X\), with \(\|\xi_n\|=1\) and \(T\xi_n\to0\). By compactness a subsequence \(C\xi_{n_j}\) converges. The identity \(\xi_{n_j}=ST\xi_{n_j}-C\xi_{n_j}\) makes that subsequence converge to a vector \(\xi\in X\) of norm one. But \(T\xi=0\), a contradiction. The resulting estimate \(\|T\xi\|\geq c\|\xi\|\) on \(X\) makes its range closed: if \(T\xi_n\) is Cauchy, replace \(\xi_n\) by its projection onto \(X\); the estimate makes the projected sequence Cauchy.

Conversely, suppose the range \(Y=T(H)\) is closed and the two kernels are finite-dimensional. The restriction \(T:X\to Y\) is a bounded bijection; its inverse is bounded by the bounded inverse theorem. Extend that inverse by zero on \(Y^\perp=\ker T^*\), obtaining \(R\). It satisfies (1.1). The two projections in (1.1) have finite rank and are compact, so \(q(R)\) is the inverse of \(q(T)\). \(\square\)

**Corollary 1.2.** If \(T=U h\) is the polar decomposition of a Fredholm operator, then both \(h=|T|\) and \(U\) are Fredholm. Moreover \(h\) has closed range,
\[
\kappa(h)=0,\qquad \kappa(U)=\kappa(T).
\tag{1.2}
\]

**Proof.** We have \(\ker h=\ker T\), and \(\|h\xi\|=\|T\xi\|\). The lower bound from Theorem 1.1 on \(X=(\ker T)^\perp\) therefore holds for \(h\). Since \(h\) is self-adjoint, the closure of its range is \(X\); the lower bound makes this range closed and hence equal to \(X\). Theorem 1.1 makes \(h\) Fredholm, with index zero. The polar partial isometry has initial projection \(1-P_{\ker T}\) and final projection \(1-P_{\ker T^*}\), so it has closed range and precisely the same two defects as \(T\). Apply Theorem 1.1 again to obtain the remaining assertions. \(\square\)

## 2. Multiplication adds the index

**Theorem 2.1.** Products of Fredholm operators are Fredholm, and
\[
\kappa(ST)=\kappa(S)+\kappa(T).
\tag{2.1}
\]

**Proof.** The quotient images of \(S,T\) are invertible, so their product is invertible. It remains to count the finite-dimensional defects. Write \(\operatorname{coker}T=H/T(H)\), which has dimension \(\dim\ker T^*\). There is an exact sequence
\[
0\longrightarrow\ker T\longrightarrow\ker(ST)
\xrightarrow{\ T\ }\ker S
\xrightarrow{\ q_T\ }\operatorname{coker}T
\xrightarrow{\ \overline S\ }\operatorname{coker}(ST)
\xrightarrow{\ q_S\ }\operatorname{coker}S
\longrightarrow0.
\tag{2.2}
\]
Here \(q_T\eta=\eta+T(H)\), \(\overline S(\eta+T(H))=S\eta+ST(H)\), and \(q_S(\zeta+ST(H))=\zeta+S(H)\). These maps are well-defined. Exactness can be checked directly: the image of \(T:\ker(ST)\to\ker S\) is \(\ker S\cap T(H)\), which is the kernel of \(q_T\). If \(S\eta\in ST(H)\), then \(S(\eta-T\xi)=0\) for some \(\xi\), so \(\eta+T(H)\) is the image of a vector in \(\ker S\). Finally, the kernel of the last map is \(S(H)/ST(H)\), the image of \(\overline S\); the last map is onto. Exactness at the first two terms is immediate.

All spaces in (2.2) are finite-dimensional. Applying rank–nullity to each map and cancelling its rank against the next term gives zero for the alternating sum of their dimensions. Rearranging yields
\[
\dim\ker(ST)-\dim\operatorname{coker}(ST)
=\dim\ker S-\dim\operatorname{coker}S
+\dim\ker T-\dim\operatorname{coker}T.
\]
Changing signs proves (2.1). \(\square\)

## 3. What is continuous, and what can jump

**Lemma 3.1.** If projections \(p,q\in B(H)\) satisfy \(\|p-q\|<1\), their ranges have the same Hilbert-space dimension, including infinite cardinal dimensions.

**Proof.** For \(\xi\in qH\), \(\|p\xi\|\geq(1-\|p-q\|)\|\xi\|\). Thus \(p:qH\to pH\) is injective with closed range. Its adjoint is \(q:pH\to qH\), which satisfies the analogous lower bound and has zero kernel. The orthogonal complement of the range of the first map is that kernel, so the first map is onto. Its polar decomposition gives a unitary between the two ranges. \(\square\)

**Theorem 3.2.** Fredholm operators form an open set. Their index is locally constant. Their kernel and cokernel dimensions are upper semicontinuous, but need not be continuous.

**Proof.** Fix a Fredholm \(T\). Use the decompositions of domain and codomain
\[
H=X\oplus K,\quad X=(\ker T)^\perp,\ K=\ker T;
\qquad H=Y\oplus C,\quad Y=T(H),\ C=\ker T^*.
\]
Relative to them, \(T=\begin{pmatrix}A&0\\0&0\end{pmatrix}\), with \(A:X\to Y\) invertible. A sufficiently close operator has the form
\[
T'=\begin{pmatrix}A'&B\\C'&D\end{pmatrix},
\]
where \(A'\) remains invertible. Bounded invertible row and column operations give
\[
\begin{pmatrix}1&0\\-C'(A')^{-1}&1\end{pmatrix}
T'
\begin{pmatrix}1&-(A')^{-1}B\\0&1\end{pmatrix}
=\begin{pmatrix}A'&0\\0&F\end{pmatrix},
\qquad F=D-C'(A')^{-1}B:K\to C.
\tag{3.1}
\]
Such operations carry kernels isomorphically to kernels and ranges by homeomorphisms to ranges, so preserve closed range and cokernel dimension. The right side has closed range, finite kernel and finite cokernel; hence \(T'\) is Fredholm. Its index is
\[
\dim C-\operatorname{rank}F
-\bigl(\dim K-\operatorname{rank}F\bigr)
=\dim C-\dim K=\kappa(T).
\]
Also \(\dim\ker T'\leq\dim K\) and \(\dim\ker(T')^*\leq\dim C\). These are exactly the local upper-semicontinuity assertions for integer-valued dimensions.

For discontinuity, fix a rank-one projection \(p\) and set \(T_t=1+(t-1)p\), for real \(t\). Every \(T_t\) is Fredholm since \(q(T_t)=1\). At \(t=0\) its kernel and cokernel both have dimension one; for \(t\neq0\) both are zero. The index is always zero. Its polar partial isometry is \(1-p+\operatorname{sgn}(t)p\) for \(t\neq0\), and \(1-p\) for \(t=0\). Thus the polar partial isometry also fails to depend continuously on \(t\). \(\square\)

The finite matrix \(F\) in (3.1) explains stability: a change in its rank removes the same number of kernel and cokernel directions. Their difference survives even when each number changes.

**Corollary 3.3.** If \(T\) is Fredholm and \(K\in K(H)\), then \(T+K\) is Fredholm and \(\kappa(T+K)=\kappa(T)\).

**Proof.** The entire path \(T+tK\), \(0\leq t\leq1\), has the same invertible image in \(Q(H)\). Its locally constant integer index is constant on this connected interval. \(\square\)

**Proposition 3.4.** A Fredholm partial isometry \(U\) is a compact perturbation of a unitary exactly when \(\kappa(U)=0\).

**Proof.** If the index is zero, the finite-dimensional spaces \(\ker U\) and \(\ker U^*\) have the same dimension. Choose a unitary between them, extend it by zero on \((\ker U)^\perp\), and call this finite-rank operator \(V\). The initial and final spaces of \(U,V\) are orthogonal and complementary, so \(U+V\) is unitary. Conversely, a unitary has index zero; Corollary 3.3 preserves that index under compact perturbation. \(\square\)

## 4. Components of the Calkin invertible group

We need one feature of \(B(H)\) that need not hold in an arbitrary C*-algebra.

**Lemma 4.1.** Every unitary \(V\in B(H)\) is \(\exp(iL)\) for a bounded self-adjoint \(L\), with \(\|L\|\leq\pi\).

**Proof.** Decompose \(H\) into orthogonal cyclic reducing subspaces for the commutative algebra \(C^*(V,1)\). Such a decomposition follows by taking a maximal orthogonal family: if its orthogonal complement were nonzero, the closed cyclic subspace generated by a nonzero vector there would be a further reducing summand. On each cyclic summand, the cyclic multiplication representation of a commutative C*-algebra identifies \(V\) with multiplication by \(z\) on \(L^2(\sigma(V),\mu)\), for a finite positive measure \(\mu\). Multiplication by the bounded real Borel function \(\operatorname{Arg}(z)\in(-\pi,\pi]\) is self-adjoint, has norm at most \(\pi\), and its exponential is multiplication by \(z\). The direct sum of these operators is the required \(L\). No continuity of the argument on the whole circle is asserted or needed. \(\square\)

**Theorem 4.2.** For a Fredholm \(T\),
\[
q(T)\in G_0(Q(H))\quad\Longleftrightarrow\quad\kappa(T)=0.
\tag{4.1}
\]
If \(H\) is separable and infinite-dimensional, the map \(q(T)\mapsto\kappa(T)\) induces an isomorphism
\[
G(Q(H))/G_0(Q(H))\cong\mathbb Z.
\tag{4.2}
\]

**Proof.** If \(q(T)\in G_0(Q(H))\), Recall 1.1 of the exponential-law lesson expresses it as a finite product \(\prod_j\exp(b_j)\), with \(b_j\in Q(H)\). Choose lifts \(B_j\in B(H)\). Then \(W=\prod_j\exp(B_j)\) is an invertible operator and \(q(W)=q(T)\). Thus \(T-W\) is compact, and Corollary 3.3 gives \(\kappa(T)=\kappa(W)=0\).

Conversely, let \(T=Uh\) have index zero. Proposition 3.4 gives a unitary \(V\) differing compactly from \(U\). By Lemma 4.1, \(q(U)=q(V)=\exp(iq(L))\in G_0(Q(H))\). Also \(q(h)\) is positive and invertible by Corollary 1.2; continuous functional calculus supplies its self-adjoint logarithm, so \(q(h)\in G_0(Q(H))\). Their product \(q(T)\) is in that component.

Every element of \(G(Q(H))\) has a lift \(T\in B(H)\), which is Fredholm by definition. Any two lifts differ compactly, so their indices agree. Theorem 2.1 makes this a homomorphism, and (4.1) identifies its kernel. When \(H\cong\ell^2(\mathbb N_0)\), the unilateral shift \(S\) has kernel zero and one-dimensional cokernel. Its powers have index \(n\), and the powers of \(S^*\) have index \(-n\). Hence the homomorphism is onto \(\mathbb Z\), proving (4.2). \(\square\)

The argument for (4.1) works on any infinite-dimensional \(H\). The separable hypothesis in (4.2) matches the shift model used here; the statement already covers every separable infinite-dimensional Hilbert space, since they are unitarily isomorphic.

## 5. Exercises with complete solutions

**Exercise 5.1 — Same index, changing defects (basic).** Let \(S\) be the unilateral shift, let \(p_j\) project onto the span of its first \(j\) basis vectors, and set \(T_t=S^3(1-p_2+tp_2)\). Compute its kernel, cokernel and index for \(t=0\) and \(t\neq0\). Identify the compact perturbation that compares the two cases.

**Solution.** For \(t\neq0\), \(1-p_2+tp_2\) is invertible, so \(T_t\) is injective and its range is the range of \(S^3\). Its cokernel has dimension three and \(\kappa(T_t)=3\). At \(t=0\), its kernel is \(p_2H\), of dimension two; its range is the closed span of \(\varepsilon_5,\varepsilon_6,\ldots\), so its cokernel has dimension five. Again \(\kappa(T_0)=5-2=3\). The difference \(T_t-T_0=tS^3p_2\) has rank at most two. Thus a finite-rank perturbation changes both defects while preserving their difference.

**Exercise 5.2 — Completing a polar isometry (intermediate).** Suppose \(T=Uh\) is Fredholm, with \(\dim\ker T=\dim\ker T^*=r\). Construct a unitary \(V\) and a positive invertible \(k\) such that \(T-Vk\) has finite rank.

**Solution.** Choose the finite-rank defect map \(W\) from Proposition 3.4 and set \(V=U+W\). Let \(p=P_{\ker T}\) and put \(k=h+p\). On \(pH\), \(k=1\); on \((1-p)H\), \(h\) is positive and bounded below, so \(k\) is positive invertible. Since \(Wh=0\), \(Up=0\), and \(Wp=W\), we have \(Vk=Uh+W=T+W\). Hence \(T-Vk=-W\) has rank \(r\).

**Exercise 5.3 — A product with cancelling indices (advanced).** Put \(T=S^2\), \(R=(S^*)^3\). Compute \(\kappa(TR)\), its kernel and cokernel directly. Then explain why \(q(TR)\) cannot lie in \(G_0(Q(H))\).

**Solution.** The map \(R\) kills \(\varepsilon_0,\varepsilon_1,\varepsilon_2\) and maps \(\varepsilon_j\) to \(\varepsilon_{j-3}\) for \(j\geq3\). Thus \(TR\) kills those same three vectors and maps \(\varepsilon_j\) to \(\varepsilon_{j-1}\) for \(j\geq3\). Its range is the closed span of \(\varepsilon_2,\varepsilon_3,\ldots\), so its cokernel has dimension two and \(\kappa(TR)=2-3=-1\). This agrees with \(\kappa(T)+\kappa(R)=2-3\). By Theorem 4.2 its quotient image belongs to the component indexed by \(-1\), not the identity component.

## References

[Blackadar] Bruce Blackadar, [*Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), author's revised and corrected online version of the 2005 book, accessed 3 October 2026. This lesson uses the opposite index convention and proves Atkinson’s theorem, index additivity and stability, and the Calkin component-group assertion.

[Erdman] John M. Erdman, [*Functional Analysis and Operator Algebras*](https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf), 2015 source edition, Chapter 6, “The Open Mapping Theorem,” Theorem C069414 and Corollary C069417. Further reading on bounded inverses.

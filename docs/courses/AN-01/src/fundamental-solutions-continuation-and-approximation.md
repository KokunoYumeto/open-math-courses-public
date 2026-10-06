# Fundamental solutions, continuation and approximation

*Reconstructed and checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*

A point-source inverse turns a differential equation into convolution. A kernel smooth away from its source gives local regularity. If that kernel is analytic there, it also supplies a common complex continuation domain, approximation across suitable complements, and solutions for arbitrary distributional forcing. We prove the approximation and existence assertions for disconnected and unbounded open sets as well.

All pairings are complex linear. Our exact earlier inputs are [U021](convolution-as-addition-of-supports.md), B0–B3, Theorems 1.1, 2.1, 3.1, 3.2, 4.1 and Corollary 4.2, for localization, gluing, convolution, finite regularity and singular support; [U008](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1, for finite order and uniform convergence on bounded test families; [U015](holomorphic-boundaries-in-convex-cones.md), Section 3, for holomorphic Taylor series and the identity principle; and [functional foundations](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Section 5, for the complete norm-preserving complex Hahn–Banach theorem. Point-supported distributions and uniqueness of their coefficients are proved in [angular foundations, A3](../prerequisites/U011-free-foundations/angular-foundations-U018.md). The scalar, measure and algebra foundations at the end supply the elementary operations used in the proofs.

## Cutoffs, smooth limits and compact duality

We first supply the additional local constructions. For an open \(X\subset\mathbb R^n\), define
\[
 L_j=\{x\in X:|x|\le j,\ \operatorname{dist}(x,X^c)\ge1/j\},
 \qquad j\ge1,
\]
using distance \(+\infty\) when \(X^c=\varnothing\). Each \(L_j\) is compact, \(L_j\subset\operatorname{int}L_{j+1}\), and these interiors exhaust \(X\). The distance function is continuous because the triangle inequality gives \(|d(x)-d(y)|\le|x-y|\); when the complement is nonempty, the lower distance bound also keeps the closure inside \(X\).

**B0 (a locally finite compact partition).** Choose \(0\le\chi_j\le1\), compactly supported in \(\operatorname{int}L_{j+1}\), equal to one near \(L_j\); if \(L_j=\varnothing\), take \(\chi_j=0\). These cutoffs come from the proved finite compact-cutoff construction. Set
\[
 \psi_j=\chi_j\prod_{i<j}(1-\chi_i).
\]
The finite telescoping identity gives \(\sum_{j=1}^N\psi_j=1-\prod_{j=1}^N(1-\chi_j)\). Every point has a neighborhood on which some \(\chi_N=1\); on that neighborhood all \(\psi_j\) with \(j>N\) vanish and the sum equals one. Thus \(\sum_j\psi_j=1\), the functions are nonnegative with compact supports in \(X\), and those supports form a locally finite family. This proves the precise partition needed below, without an unproved partition theorem.

**B1 (the smooth topology).** Write
\[
 p_{K,r}(f)=\max_{|\alpha|\le r}\sup_K|\partial^\alpha f|,
 \qquad K\Subset X.
\]
The seminorm on an empty compact set is defined to be zero. The countable increasing seminorms \(p_{L_j,j}\) determine the same topology as all \(p_{K,r}\): every compact \(K\Subset X\) lies in some \(\operatorname{int}L_j\). Closure can consequently be tested by sequences, choosing errors \(1/j\) in the \(j\)-th seminorm.

If a sequence is Cauchy in every such seminorm, every derivative has a uniform limit on each compact set. These limits agree on overlaps and are continuous. On a small closed coordinate box, pass to the limit in
\[
 \partial^\alpha f_k(x+te_\ell)-\partial^\alpha f_k(x)
 =\int_0^t\partial^{\alpha+e_\ell}f_k(x+se_\ell)\,ds.
\]
The fundamental theorem then identifies the derivative of the first limit with the second. Induction proves that the function limit is smooth with the prescribed derivatives. This proves the completeness and smooth-series convergence used later.

**B2 (compact-distribution duality).** A continuous linear functional \(T\) on \(C^\infty(X)\) has a bound \(|T(f)|\le C p_{K,r}(f)\) for some compact \(K\Subset X\), finite \(r\), and \(C\). Indeed continuity gives a finite intersection of seminorm balls on which \(|T|\le1\); take the union of their compact sets and the largest derivative order, then rescale. If the resulting seminorm of \(f\) is zero, arbitrary scaling forces \(T(f)=0\), which also proves the bound in that case.

Restriction to test functions is a distribution supported in \(K\), since tests supported outside \(K\) have zero controlling seminorm. Choose a cutoff \(\eta=1\) near \(K\). The bound also gives \(T(f)=T(\eta f)\), since every derivative of \((1-\eta)f\) vanishes on \(K\). Conversely, a distribution with compact support acts on every smooth \(f\) by \(T(\eta f)\). U021, B0, proves independence of the cutoff. Its finite-order bound on \(\operatorname{supp}\eta\), together with the product rule, makes this action continuous on \(C^\infty(X)\). These constructions are inverse to each other. They also give extension by zero of a compact distribution to a larger open set: apply it to the restricted smooth test after inserting such a cutoff. Its support is unchanged, and localization proves uniqueness.

## Local regularity from one point source

Let \(n\ge1\) and \(P=\sum_{|\alpha|\le m}a_\alpha\partial^\alpha\), with constant complex coefficients. A fundamental solution is \(E\in\mathcal D'(\mathbb R^n)\) satisfying \(PE=\delta_0\). In particular \(P\ne0\). No bound on \(E\) at infinity is imposed; a compact second factor suffices for the convolutions here.

**Proposition 1.1 (two inverse identities).** If \(u,f\) are compact distributions, then
\[
                   E*(Pu)=u,\qquad P(E*f)=f.                     \tag{1.1}
\]
**Proof.** Differentiation of a proper convolution gives \(E*(Pu)=(PE)*u=\delta_0*u=u\), and \(P(E*f)=(PE)*f=f\). Every pair has a compact factor. Equivalently, \(Pu=(P\delta_0)*u\), and the triple convolution with \(E\) is associative because the other two supports are compact: fixing their sum with the first coordinate in a compact output set bounds all three coordinates. These are exactly the support hypotheses in U021. \(\square\)

**Theorem 1.2 (exact local singular support).** If \(E\) is smooth on \(\mathbb R^n\setminus\{0\}\), then on every open \(X\),
\[
          \operatorname{singsupp}u=\operatorname{singsupp}Pu,
          \qquad u\in\mathcal D'(X).                              \tag{1.2}
\]
**Proof.** A differential operator with smooth coefficients takes smooth functions to smooth functions, so the right side is contained in the left. For compact \(u\) on the whole space, Proposition 1.1 and U021, Corollary 4.2, give
\[
 \operatorname{singsupp}u
 \subset\operatorname{singsupp}E+\operatorname{singsupp}Pu
 \subset\operatorname{singsupp}Pu.
\]
For arbitrary \(u\), choose a compact cutoff \(\psi\) equal to one near the point being considered, and extend \(\psi u\) by zero. Both \(\psi u=u\) and \(P(\psi u)=Pu\) near that point; restrict the compact result there. This proves the local identity. A fundamental solution cannot be smooth at zero, since then \(PE\) would be smooth there whereas \(\delta_0\) is not: a smooth representative of a point mass would vanish on the punctured neighborhood and by continuity at its center, contradicting a test equal to one there. Thus the stated assumption is equivalent to \(\operatorname{singsupp}E=\{0\}\). \(\square\)

**Theorem 1.3 (every derivative of a null sequence converges).** Under this smooth-kernel hypothesis, if \(Pu_j=0\) on \(X\) and \(u_j\to u\) weakly in \(\mathcal D'(X)\), then all these distributions are smooth, \(Pu=0\), and
\[
                          u_j\longrightarrow u
                          \quad\hbox{in }C^\infty(X).             \tag{1.3}
\]
**Proof.** Applying the distributional derivative definition to each fixed test proves \(Pu=0\); Theorem 1.2 gives smoothness. Subtract \(u\). For \(Y\Subset X\), choose \(\psi\in\mathcal D(X)\) equal to one near \(\overline Y\). The product rule shows that
\[
 f_j=P(\psi u_j)=[P,\psi]u_j
\]
is supported in the fixed compact set \(S=\operatorname{supp}d\psi\), disjoint from \(\overline Y\), and tends weakly to zero. Indeed every commutator term contains a positive-order derivative of \(\psi\) and a fixed derivative of \(u_j\). Proposition 1.1 gives \(u_j=E*f_j\) on \(Y\).

For \(K\Subset Y\), choose a cutoff \(\eta=1\) near \(S\) whose support misses \(K\). Then
\[
 \partial^\alpha u_j(x)
   =f_j\!\left(\eta(\,\cdot\,)\partial^\alpha E(x-\,\cdot\,)\right),
 \qquad x\in K.                                                   \tag{1.4}
\]
The formula follows from U021's local smooth convolution formula and differentiation of a smooth compact kernel test. All these tests have one compact support and bounds for every derivative uniform in \(x\in K\), because the arguments \(x-y\) stay in a compact set away from zero. They are a bounded test family. U008, Theorem 5.1, says that a weakly convergent sequence of distributions converges uniformly on any such family. Hence the right side tends uniformly to zero. This holds for every \(K,\alpha\), proving (1.3). \(\square\)

The fixed null equation is essential in this conclusion; no assertion about arbitrary varying forcing terms is made.

## One complex neighbourhood for every solution

A real-analytic function is locally represented by an absolutely convergent real power series, with complex coefficients allowed.

**Lemma 2.1 (gluing the real series).** For every real-analytic \(h\) on open \(\Omega\subset\mathbb R^n\), there is a holomorphic extension to an open \(D\subset\mathbb C^n\) with \(D\cap\mathbb R^n=\Omega\). We may choose \(D\) vertically contractible: \(x+iy\in D\) implies \(x+ity\in D\) for \(0\le t\le1\).

**Proof.** At each \(a\in\Omega\), take a positive radius \(r_a\) such that the real ball is in \(\Omega\), the representing series is valid there, and \(\sum_\alpha|c_{a,\alpha}|r_a^{|\alpha|}<\infty\). Shrinking a coordinate neighborhood of absolute convergence supplies such a radius. On the complex ball \(B_{\mathbb C^n}(a,r_a)\) the same series converges; its derivatives converge uniformly on smaller balls because \((1+|\alpha|)^k\theta^{|\alpha|}\) is bounded for each \(k\) and \(0<\theta<1\). It therefore defines a holomorphic function.

An intersection of two such balls is convex. If it contains \(x+iy\), it contains the real point \(x\) and an open real neighborhood of \(x\). The two functions agree on that real neighborhood. Their difference has all real derivatives zero at \(x\), so the holomorphic Taylor formula proved in U015 makes it zero on a complex neighborhood. The identity principle then makes it zero on the entire connected intersection. Thus the functions glue on the union of the balls. Its real trace is exactly \(\Omega\), and
\[
 |x+ity-a|^2=|x-a|^2+t^2|y|^2\le|x+iy-a|^2                    \tag{2.1}
\]
proves vertical contractibility. No connectedness assumption on \(\Omega\) was needed. \(\square\)

**Theorem 2.2 (one extension domain for all null solutions).** Suppose \(PE=\delta_0\) and \(E\) is real analytic off zero. Every open \(X\) has an open complex neighborhood \(Z\), independent of the solution, to which each distributional null solution on \(X\) extends holomorphically. If \(Pu_j=0\) and \(u_j\to u\) distributionally, the extensions converge uniformly on compact subsets of \(Z\).

**Proof.** Use Lemma 2.1 to extend the off-zero function \(E\) to \(\mathcal E\) on a vertically contractible \(D\) with real trace \(\mathbb R^n\setminus\{0\}\). For each \(Y\Subset X\), choose \(\psi\in\mathcal D(X)\) equal to one near \(\overline Y\), and let \(S=\operatorname{supp}d\psi\). Define
\[
 V_S=\{z:z-S\subset D\},\qquad
 W_{Y,\psi}=\{z:\operatorname{Re}z\in Y\}\cap V_S.                  \tag{2.2}
\]
This is open: for any \(z\in V_S\), the compact set \(z-S\) has positive distance from the closed complement of \(D\), unless that complement is empty, in which case openness is immediate. It contains \(Y\), and vertical contraction remains in it. If \(S=\varnothing\), interpret \(V_S=\mathbb C^n\).

For a null solution set \(f=P(\psi u)\), supported in \(S\), and put
\[
                    U_{Y,\psi}(z)
                       =f_y\bigl(\mathcal E(z-y)\bigr).           \tag{2.3}
\]
This is an extended pairing in the sense of B2. More explicitly, for a compact \(A\Subset W_{Y,\psi}\), compactness of \(A-S\subset D\) supplies a neighborhood \(N\) of \(S\) such that \(A-\overline N\Subset D\), after taking \(N\) relatively compact. Choose one cutoff \(\eta=1\) near \(S\), supported in \(N\); use the literal test \(\eta(y)\mathcal E(z-y)\). Different choices agree by localization. If \(S=\varnothing\), \(f=0\) and the pairing is zero.

Here is the holomorphy justification with the distribution order accounted for. Near any \(z_0\), choose a polydisk of radius \(2r>0\) in \(z\) such that all its differences with \(\operatorname{supp}\eta\) are in \(D\). The Cauchy formulas and derivative bounds in U015, Section 3, give a Taylor expansion
\(\mathcal E(z_0+w-y)=\sum_\alpha c_\alpha(y)w^\alpha\).
For every fixed integer \(k\), they also give \(\max_{|\beta|\le k}\sup|\partial_y^\beta c_\alpha|\le C_k r^{-|\alpha|}\), using the larger polydisk for the derivative bounds. Derivatives in \(y\) are the negatives of the corresponding real derivatives of the holomorphic kernel. The product rule gives the same bound for \(\eta c_\alpha\) in the controlling \(C^k\) norm. If \(k\) is an order bound for \(f\), its pairing with the series converges absolutely for \(|w_j|<r\), since the bound is a product of geometric series. The paired power series thus proves holomorphy. On \(Y\), Proposition 1.1 gives \(U_{Y,\psi}=E*f=u\).

Two such extensions agree on each component of an overlap. Indeed the vertical segment from any point of the overlap to its real part remains in the overlap, so its component meets an open real subset where both functions equal \(u\). Equality of all real derivatives and the holomorphic identity principle give equality on that component. They consequently glue on
\[
                         Z=\bigcup_{Y,\psi}W_{Y,\psi}.            \tag{2.4}
\]
This set depends only on the chosen kernel and cutoff family, and it contains \(X\).

For the convergence assertion subtract \(u\). The compact distributions \(P(\psi(u_j-u))\) tend weakly to zero with support in \(S\). On a compact complex subset of a fixed \(W\), the preceding literal kernel tests share a compact support and all their derivatives are uniformly bounded. U008's bounded-test convergence makes their pairings uniformly tend to zero. Every compact subset of \(Z\) is covered by finitely many neighborhoods with closures compact in individual \(W\)'s; combine those finitely many estimates. \(\square\)

**Corollary 2.3 (connected uniqueness).** A null solution on connected \(X\) that vanishes on a nonempty open subset is zero throughout \(X\).

**Proof.** It is real analytic by Theorem 2.2. The points near which it vanishes form a nonempty open set. At a limit point, every derivative vanishes by continuity, so its convergent Taylor series is zero near that point. The set is relatively closed as well; connectedness proves the assertion. \(\square\)

The same local kernel and finite-order series argument shows that \(\check E*w\) is real analytic outside \(\operatorname{supp}w\) for any compact distribution \(w\), where reflection is defined by \(\check E(\phi)=E(\phi(-\,\cdot\,))\). Differentiating this definition verifies
\[
 P^t=\sum_\alpha a_\alpha(-\partial)^\alpha,\qquad
                          P^t\check E=\delta_0.                  \tag{2.5}
\]
There is no conjugation in the transpose.

## Separation by a compact distribution

**Lemma 3.1.** If \(M\subset C^\infty(Y)\) is a closed linear subspace and \(q\notin M\), there is a compact distribution \(w\in\mathcal E'(Y)\) with \(w|_M=0\) and \(w(q)=1\).

**Proof.** A basic neighborhood of \(q\) missing \(M\) gives one seminorm \(p=p_{K,r}\) and \(\varepsilon>0\) such that \(p(q-m)\ge\varepsilon\) for all \(m\in M\); combine finitely many bounds as in B2. On \(M+\mathbb Cq\), set \(\ell(m+cq)=c\). The decomposition is unique. For \(c\ne0\), apply the separation inequality to \(-m/c\), and for \(c=0\) use zero, to get
\[
                       |\ell(m+cq)|
                          \le\varepsilon^{-1}p(m+cq).             \tag{3.1}
\]
Thus \(\ell\) descends to the image of this subspace in \(C^\infty(Y)/\ker p\). The formula \(\|[f]\|=p(f)\) is well defined by the two triangle inequalities, and is a norm on that quotient. The norm-preserving complex Hahn–Banach theorem, proved in functional foundations Section 5, extends \(\ell\) to the whole quotient with the same bound. Pull back to \(C^\infty(Y)\), then apply B2. This yields the required compact distribution. The normed quotient need not be complete, and its subspace need not be closed. \(\square\)

Hence membership in the closure of a linear space is equivalent to annihilation by every compact distribution that annihilates that space. The null space of \(P\) is closed, since each derivative defining \(P\) is continuous in the smooth topology. B1 makes a closure assertion here equivalent to approximation by a sequence.

## Which holes prevent approximation

For open \(Y\subset X\), consider the exact condition
\[
              X\setminus Y\ne F\mathbin{\dot\cup}K                \tag{4.1}
\]
for every nonempty compact \(K\) and every \(F\) closed relative to \(X\). A prohibited \(K\) is a compact piece both open and closed in the relative complement. This formulation includes arbitrary disconnected and unbounded sets.

**Theorem 4.1 (Runge approximation).** If \(P\) has a fundamental solution real analytic away from zero and (4.1) holds, every null solution on \(Y\) is a \(C^\infty(Y)\) limit of restrictions of null solutions on \(X\).

**Proof.** The empty-domain cases are immediate. By Lemma 3.1 it suffices to take \(w\in\mathcal E'(Y)\) annihilating all restrictions of null solutions on \(X\), and prove that it annihilates every null solution on \(Y\). For \(w=0\) this is immediate. Otherwise let
\[
                    M=\operatorname{supp}w,\qquad v=\check E*w.
\]
Then \(P^t v=w\), and \(v\) is analytic off the nonempty compact set \(M\Subset Y\).

We record the component topology used here. Each component of the open set \(\mathbb R^n\setminus M\) is open: a small ball centered at a point of a component is connected and lies in the same component. Its boundary is contained in \(M\), since a small ball about a boundary point outside \(M\) would meet the component and then be contained in it, contradicting its being a boundary point.

If \(x\notin X\), the functions \(y\mapsto\partial_x^\alpha E(y-x)\) are smooth null solutions on \(X\), for every \(\alpha\); their possible source is at \(y=x\), outside \(X\). Pairing with \(w\) shows that every derivative of \(v\) at \(x\) vanishes. Its Taylor series is zero near \(x\). Corollary 2.3, or the identical analytic open-and-closed argument, makes \(v\) zero on the entire component of \(\mathbb R^n\setminus M\) containing \(x\).

Now take a bounded component \(O\) contained in \(X\). Its boundary lies in \(M\Subset Y\), so \(\overline O\Subset X\). The set \(K=O\cap(X\setminus Y)\) is compact: a sequence in it has limits in the compact \(\overline O\), and no limit can lie on \(\partial O\subset Y\), because \(Y\) is open. The remaining set \(F=(X\setminus Y)\setminus O\) is relatively closed in \(X\). Condition (4.1) gives \(K=\varnothing\), so \(O\subset Y\).

When \(X\) is bounded, every component entirely in \(X\) is of this type; every other component meets \(X^c\) and has \(v=0\). Thus each point outside \(Y\) has a neighborhood on which \(v=0\), since it is outside \(M\) and lies in one of the zero components. Consequently \(\operatorname{supp}v\subset Y\). This globally closed support is bounded, being contained in bounded \(X\), and is therefore compact in \(Y\). For any null solution \(u\) on \(Y\), extended pairings and integration by parts give
\[
                     w(u)=(P^tv)(u)=v(Pu)=0.                     \tag{4.2}
\]
To see the cutoff justification explicitly, insert a cutoff equal to one near \(\operatorname{supp}v\); its derivatives vanish there, so moving \(P^t\) to the test leaves exactly \(Pu\) on that support. Lemma 3.1 proves the bounded-ambient case.

We use this case to prove a needed global approximation statement before treating unbounded \(X\). Concentric balls \(B_r\subset B_R\), \(0<r<R\), satisfy (4.1). Starting at any point of the annular complement, the outward radial segment approaching the outer sphere stays in that complement. A relatively clopen piece containing its initial point must contain the entire connected segment. If the piece were compact in \(B_R\), its limiting outer boundary point would also belong to it, a contradiction. This works in dimension one on each of the two annular intervals. The bounded case therefore approximates a null solution on a ball by null solutions on any larger concentric ball.

Fix a closed smaller ball \(K_0\) in an initial ball. Choose larger concentric balls \(B_1,B_2,\ldots\) with \(\overline B_k\Subset B_{k+1}\), union \(\mathbb R^n\), and \(B_1\) larger than the initial ball; put \(K_k=\overline B_k\), \(k\ge1\). For each integer \(j\ge1\), first approximate the initial solution by \(u_j^1\) on \(B_1\) with error below \(2^{-j}\) on \(K_0\). Repeated use of the bounded case chooses a null solution \(u_j^{k+1}\) on \(B_{k+1}\) such that
\[
                 \|u_j^{k+1}-u_j^k\|_{C^k(K_{k-1})}
                           <2^{-j-k}.                            \tag{4.3}
\]
For each compact set and derivative order, all sufficiently late differences satisfy this summable bound there. B1 gives a smooth global limit \(U_j\) as \(k\to\infty\); passing derivatives to the limit shows \(PU_j=0\). The supremum error on \(K_0\) is less than \(2^{1-j}\). Exhausting the original open ball by smaller closed balls and choosing the error to tend to zero gives global null solutions converging uniformly on every compact subset of the initial ball. This is distributional convergence, and Theorem 1.3 upgrades it to smooth convergence. This construction used only the bounded-ambient case.

Return to arbitrary \(X\), and choose \(R\) with \(M\Subset B_R\). For \(|x|>R\), the function \(y\mapsto E(y-x)\) is a null solution on \(B_R\). The preceding global approximation makes it a smooth limit near \(M\) of global null solutions. The functional \(w\) annihilates those solutions, since their restrictions are null on \(X\). Hence
\[
                       v(x)=w_y(E(y-x))=0
                       \qquad(|x|>R).                            \tag{4.4}
\]
Every unbounded component of \(\mathbb R^n\setminus M\) meets this exterior open set, and analytic uniqueness makes \(v\) zero on it. In dimension one this separately covers both unbounded rays. Together with the earlier bounded-component argument, every point outside \(Y\) again lies in an open zero component. Thus \(\operatorname{supp}v\subset Y\), and (4.4) makes that globally closed support bounded and compact. Equation (4.2) and separation finish the proof. \(\square\)

**Corollary 4.2 (necessity for a nonconstant operator).** Under the same analytic-kernel hypothesis, if \(P\) is nonconstant, condition (4.1) is necessary for the approximation conclusion.

**Proof.** Suppose \(X\setminus Y=F\mathbin{\dot\cup}K\) is a prohibited decomposition. The set \(O=X\setminus F=Y\cup K\) is open. Choose \(x_0\in K\) and the smooth null solution \(u(y)=E(y-x_0)\) on \(Y\). Assume that null solutions \(u_j\) on \(X\) approximate it smoothly on \(Y\). Take \(\psi\in\mathcal D(O)\) equal to one on a neighborhood \(G\) of \(K\), with \(\overline G\Subset O\). The commutators
\[
                          f_j=P(\psi u_j)=[P,\psi]u_j
\]
are smooth, supported in the fixed compact set \(\operatorname{supp}d\psi\Subset Y\), and converge with every derivative to a test function \(f\) on that set. By U021, Theorem 2.1 and its compact-set seminorm estimates, \(E*f_j\to E*f\) smoothly on every compact set. Proposition 1.1 gives \(E*f_j=u_j\) on \(G\). Hence the smooth function \(E*f\) equals \(u\) on \(G\cap Y\) and is null on \(G\). It glues with \(u\) on \(Y\) to a smooth null solution \(U\) on \(O=G\cup Y\).

The distribution \(q=E(\,\cdot-x_0)-U\) on \(O\) is supported in \(K\). Extend it compactly by B2. Its equation is \(Pq=\delta_{x_0}\) on the whole space: the equation holds on \(O\), and the compact extension vanishes near the complement of \(O\). U030, Corollary 4.3, gives
\[
                     \operatorname{ch}\operatorname{supp}q
                                      =\{x_0\}.
\]
The full point-support proof in angular foundations A3 writes \(q=Q(\partial)\delta_{x_0}\), with \(Q\) a finite polynomial. Point-jet independence gives \(PQ=1\). This is impossible for nonconstant \(P\): the top homogeneous parts of two nonzero polynomials have nonzero product, because their largest lexicographic monomials have a unique largest product monomial with nonzero coefficient. Thus degrees add. Since \(Q\ne0\), \(\deg(PQ)\ge\deg P>0\). This contradiction proves necessity. \(\square\)

For a nonzero constant \(P\), all null solutions are zero, and approximation holds on every pair of open sets without (4.1).

## Solving on an arbitrary open set

**Theorem 5.1.** If \(P\) has a fundamental solution real analytic away from zero, then for every open \(X\subset\mathbb R^n\) and every \(f\in\mathcal D'(X)\) there is \(u\in\mathcal D'(X)\) with \(Pu=f\).

**Proof.** There is nothing to prove for empty \(X\). Define
\[
 \begin{gathered}
 d(x)=\operatorname{dist}(x,\mathbb R^n\setminus X),\qquad
 D_j=\{x\in X:d(x)>1/j\},\\
 X_j=B_j(0)\cap D_j,\qquad K_j=\overline X_j,\qquad j\ge1,
 \end{gathered}                                                    \tag{5.1}
\]
with \(d=+\infty\) for the whole space, and \(X_0=K_0=\varnothing\). These open sets exhaust \(X\). Each \(K_j\) is compact and contained in \(X_{j+1}\), since its points satisfy \(|x|\le j\) and \(d(x)\ge1/j\), still strictly stronger than the inequalities for \(j+1\).

We verify (4.1) for \(X_j\subset X\). Suppose a nonempty compact relatively clopen piece \(K\subset X\setminus X_j\) exists, and choose \(x\in K\). If \(|x|\ge j\), follow the outward radial ray until its first encounter with \(X^c\), if any. Before that encounter it is a connected path in \(X\setminus X_j\), so relative clopenness keeps it in \(K\). A finite first encounter contradicts closedness of compact \(K\subset X\); absence of an encounter would put an unbounded ray in \(K\), also impossible.

If \(|x|<j\), then \(d(x)\le1/j\). A nearest \(q\in X^c\) exists: a minimizing sequence in the nonempty closed set can be restricted to a closed bounded ball and has a convergent subsequence. For \(0\le t<1\), let \(x_t=(1-t)x+tq\). This point lies in \(X\), since \(|x_t-x|=t\,d(x)<d(x)\). Also \(d(x_t)\le|x_t-q|=(1-t)d(x)\le1/j\). Thus the segment lies in \(X\setminus X_j\), remains in \(K\) by connectedness, and has limit \(q\notin X\), the same contradiction. This proves the complement condition, including cases where \(X_j\) is empty.

Take \(\phi_j\in\mathcal D(X)\) equal to one near \(K_j\), extend \(\phi_jf\) compactly, and set \(v_j=E*(\phi_jf)\). Proposition 1.1 gives \(Pv_j=f\) on \(X_j\). Therefore \(h_j=v_{j+1}-v_j\) is a null solution on \(X_j\), smooth by Theorem 1.2. Theorem 4.1 supplies a null solution \(w_j\) on \(X\) with
\[
                       \sup_{K_{j-1}}|h_j-w_j|<2^{-j}.            \tag{5.2}
\]
If \(K_{j-1}=\varnothing\), take \(w_j=0\). Define global-on-\(X\) distributions
\[
                         t_j=v_j-\sum_{i<j}w_i.                  \tag{5.3}
\]
For fixed \(k\ge1\) and \(j>k+1\), telescoping on \(X_k\) gives
\[
              t_j=t_{k+1}+\sum_{i=k+1}^{j-1}(h_i-w_i).            \tag{5.4}
\]
The summands are smooth null solutions on \(X_k\). Since \(X_k\subset K_{i-1}\) for \(i\ge k+1\), (5.2) gives uniform summable bounds there. The partial sums have a continuous uniform limit, hence converge as distributions: for a compact test, bound the integral of the difference by its supremum times the test's \(L^1\) norm. Theorem 1.3 makes the limit smooth and null.

The base \(t_{k+1}\) need not be a function, but \(Pt_{k+1}=f\) on \(X_k\). Adding the smooth null limit produces a distributional solution there. These distributions agree on overlaps because all are limits of the same \(t_j\). More explicitly, every compact test is supported in some \(X_k\); define its pairing by this local limit. Enlarging \(k\) leaves it unchanged. For tests in any fixed compact set, one such \(k\) works for all of them, and the local distribution estimate proves continuity. Linearity follows by choosing one \(k\) for finitely many supports. This constructs a distribution on \(X\) with the required equation. \(\square\)

The solution need not be unique. Any two solutions with the same forcing differ by a null solution, which is real analytic by Theorem 2.2.

## Every distribution has continuous primitives

We now drop the hypothesis on \(P\). The one-variable identity
\[
              \partial^{m+1}\frac{x_+^m}{m!}=\delta_0,
                    \qquad m=0,1,2,\ldots,                       \tag{6.1}
\]
uses \(x_+^0=1_{(0,\infty)}\). To prove it, integrate by parts against a compact test on \((0,\infty)\). For \(m\ge1\) the zero endpoint contributes nothing and the derivative is \(x_+^{m-1}/(m-1)!\); for \(m=0\), \(-\int_0^\infty\phi'=\phi(0)\). Iteration gives (6.1).

**Theorem 6.1 (continuous coefficients with locally finite supports).** Every \(f\in\mathcal D'(X)\) has continuous functions \(f_\alpha\) on \(X\) such that
\[
              f(\varphi)=\sum_\alpha\int_X
                    f_\alpha\,\partial^\alpha\varphi\,dx,
                    \qquad\varphi\in\mathcal D(X),               \tag{6.2}
\]
and \(\{\operatorname{supp}f_\alpha\}\) is locally finite. If \(f\) has compact support, one can use finitely many coefficients, all compactly supported in \(X\).

**Proof.** Let \(g\) first be compactly supported with order at most \(k\) on the whole space. Choose an integer \(m>k\), and put
\[
 A_m(x)=\prod_{r=1}^n\frac{(x_r)_+^m}{m!},\qquad
 Q_m=(\partial_1\cdots\partial_n)^{m+1}.                           \tag{6.3}
\]
Tensor products and (6.1) give \(Q_mA_m=\delta_0\). The function \(A_m\) is \(C^{m-1}\), in particular \(C^k\). U008, Proposition 1.2, extends an order-\(k\) distribution continuously to \(C_c^k\) tests. Thus
\(a(x)=g_y(A_m(x-y))\), with a fixed cutoff near \(\operatorname{supp}g\), is well defined. On each compact \(x\)-set its kernel tests depend continuously on \(x\) in the \(C^k\) norm, by uniform continuity of the finitely many derivatives on a larger compact set. Hence \(a\) is continuous. U021, Theorem 2.1, identifies this function with the distributional convolution \(A_m*g\). Differentiating that proper convolution gives
\[
                              Q_ma=g.                            \tag{6.4}
\]

For general \(f\), use the locally finite partition \(\{\psi_j\}\) of B0. Choose \(\chi_j\in\mathcal D(X)\) equal to one near \(\operatorname{supp}\psi_j\), and extend \(g_j=\chi_jf\) compactly to the whole space. Let \(k_j\) be an order bound, choose \(m_j>k_j\), and form \(a_j=A_{m_j}*g_j\). Write
\(\lambda_j=(m_j+1,\ldots,m_j+1)\), \(\sigma_j=(-1)^{|\lambda_j|}\).
Only finitely many \(\psi_j\)'s meet a given compact test. Therefore (6.4) and the product rule give
\[
 \begin{aligned}
 f(\varphi)
 &=\sum_jg_j(\psi_j\varphi)
 =\sum_j\sigma_j\int a_j\,
                   \partial^{\lambda_j}(\psi_j\varphi)\,dx\\
 &=\sum_\alpha\int f_\alpha\,\partial^\alpha\varphi\,dx,
 \end{aligned}                                                    \tag{6.5}
\]
where
\[
 f_\alpha=\sum_{j:\alpha\le\lambda_j}
          \sigma_j\binom{\lambda_j}{\alpha}
                a_j\,\partial^{\lambda_j-\alpha}\psi_j.           \tag{6.6}
\]
Each summand is continuous and supported in \(\operatorname{supp}\psi_j\). Near each point only finitely many of those supports occur, and each of their finitely many \(\lambda_j\)'s allows only finitely many \(\alpha\). Thus (6.6) defines continuous functions and a locally finite family of their supports. It also justifies every interchange in (6.5). In distribution notation (6.2) means \(\sum_\alpha(-1)^{|\alpha|}\partial^\alpha f_\alpha\), with precisely these signs.

If \(f\) is compact, choose a single compact cutoff \(\psi=1\) near its support, extend \(f\) by zero, and use one \(m>k\) and \(a=A_m*f\). The identity \(f(\varphi)=f(\psi\varphi)\) and the same finite product expansion give only finitely many coefficients, all supported in \(\operatorname{supp}\psi\Subset X\). \(\square\)

## Two kernels with different kinds of continuation

For clarity, the elementary interval fact used in the first example is also proved here. If \(T'=0\) on an open interval \(I\), choose \(\rho\in\mathcal D(I)\) with \(\int\rho=1\). For any \(\phi\in\mathcal D(I)\), the test \(\phi-(\int\phi)\rho\) has integral zero; its primitive from \(-\infty\), after extending it by zero, is a compact smooth function supported in the convex hull of the two test supports, hence in \(I\). Pairing that derivative with \(T\) gives \(T(\phi)=T(\rho)\int\phi\). Thus \(T\) is constant. This also proves that \(T''=0\) implies \(T\) is affine: apply the result to \(T'\), then subtract the corresponding multiple of \(x\).

**Example 7.1.** For any \(\lambda\in\mathbb C\),
\[
 P_\lambda=\partial_x-\lambda,\qquad
                      E_\lambda=1_{(0,\infty)}e^{\lambda x}
\]
satisfy \(P_\lambda E_\lambda=\delta_0\). Integration by parts gives
\[
 -\int_0^\infty e^{\lambda x}(\phi'+\lambda\phi)\,dx=\phi(0).
\]
The kernel is analytic on both half-lines, even if it grows exponentially at positive infinity. Every preceding theorem applies without a temperedness assumption. Multiplication of \(P_\lambda u=0\) by \(e^{-\lambda x}\), using the distributional product rule, gives \((e^{-\lambda x}u)'=0\). The proved interval fact yields \(u=ce^{\lambda x}\) on each connected interval.

**Example 7.2.** The heat point source proved in [U020, Theorem 4.1](point-sources-and-complex-gaussian-kernels.md) is
\[
 E_{\rm heat}(t,x)=
 \begin{cases}
 (4\pi t)^{-n/2}e^{-|x|^2/(4t)},&t>0,\\
 0,&t<0.
 \end{cases}
\]
It is smooth away from the space-time origin. The only point needing verification is \((0,x_0)\) with \(x_0\ne0\). On a neighborhood with \(|x|\ge c>0\), every differentiated positive-time expression is bounded by a constant times a power of \(t^{-1}\) times \(e^{-c^2/(4t)}\), which tends to zero faster than every power by the exponential series. All derivatives therefore extend by zero across \(t=0\), and repeated use of the fundamental theorem proves smoothness of the extension. Its Taylor series there is zero but the function is positive at nearby positive times, so it is not real analytic there. Theorems 1.2–1.3 apply to this kernel, while the analytic-kernel hypothesis of Theorems 2.2, 4.1 and 5.1 is not satisfied.

## Exercises

**Exercise 1 (basic).** Check \(P_\lambda E_\lambda=\delta_0\) directly and determine all distributions on \(\mathbb R\) solving \(P_\lambda u=\delta'_0+3\delta_0\). Include \(\lambda=-3\).

**Exercise 2 (basic).** In \(\mathbb R^3\), solve \(-\Delta u=\delta_0-2\delta_b\), \(b=(2,-1,1)\), by a locally integrable function with the correct Newton normalization. Determine its singular support and the difference of any two distributional solutions.

**Exercise 3 (intermediate).** Extend \(u_j(x,y)=\operatorname{Re}(x+iy)^j\) from the real unit disk to a holomorphic polynomial in \(z_1,z_2\). Prove convergence to zero with every derivative on compact subsets of
\[
                  Z=\{z\in\mathbb C^2:|z_1+iz_2|<1,\
                                            |z_1-iz_2|<1\},
\]
and show that \(Z\) contains the real disk.

**Exercise 4 (intermediate).** Let \(X=B_3(0)\subset\mathbb R^3\), \(Y=\{1/2<|x|<5/2\}\), and \(u(x)=1/|x|\). Derive the spherical mean identity for harmonic functions from the divergence theorem, and prove for every harmonic \(h\) on \(X\) that
\[
                   \max_{|x|=1\ \text{or}\ |x|=2}|h(x)-u(x)|
                                            \ge\frac14.
\]
Show sharpness on these two spheres and identify the compact hole.

**Exercise 5 (intermediate).** Show that
\(w=\delta_{-1}-2\delta_0+\delta_1+\delta''_0\)
annihilates every null solution of \(\partial_x^2\). Use \(T(x)=(1-|x|)_+\) to find the unique compact distribution \(v\) with \(v''=w\), and prove that \(w\) has exact order two.

**Exercise 6 (advanced).** In Theorem 5.1 choose corrections with
\(\|h_j-w_j\|_{C^j(K_{j-1})}<2^{-j}\).
Prove that \(u-t_k\) is smooth and null on \(X_k\), and
\[
                  \|u-t_k\|_{C^r(K_{k-1})}\le2^{1-k},
                               \qquad0\le r\le k.
\]
Explain why this is meaningful for distributional forcing and why any two choices give solutions differing by an analytic null solution.

**Exercise 7 (advanced).** For
\(g=(\partial_x\delta_0)\otimes(\partial_y^2\delta_0)\),
use \(m=4\) in (6.3) to calculate a continuous \(a\) with \(\partial_x^5\partial_y^5a=g\). Find its exact global integer classical regularity, its test integral with the correct sign, and the exact distribution order of \(g\).

**Exercise 8 (advanced).** For arbitrary open \(Y\subset X\subset\mathbb R\), characterize density of restrictions of \((\partial_x-\lambda)\)-null solutions on \(X\) among null solutions on \(Y\). Prove that in the dense cases restriction is onto. Apply the criterion to
\[
 \begin{aligned}
 X_1&=(-3,3),&Y_1&=(-3,-1)\cup(1,3),\\
 X_2&=\mathbb R\setminus\{0\},&
 Y_2&=(-\infty,-1)\cup(1,\infty).
 \end{aligned}
\]
For \(\lambda=0\), calculate the best maximum error in approximating constants \(c_-,c_+\) on the two components of \(Y_1\) by a constant on \(X_1\).

## Complete solutions

**Solution 1.** For a compact test, \(-\int_0^\infty(e^{\lambda x}\phi(x))'\,dx=\phi(0)\), proving the source identity with no condition at infinity. Since \(P_\lambda\delta_0=\delta'_0-\lambda\delta_0\), one solution is
\[
                       u_0=\delta_0+(3+\lambda)E_\lambda.
\]
The difference of any two solutions is null; Example 7.1 and its interval proof give the full family \(u_0+ce^{\lambda x}\). When \(\lambda=-3\), the kernel term disappears and the solutions are \(\delta_0+ce^{-3x}\).

**Solution 2.** U020, Theorem 1.1, proves \(\Delta[-1/(4\pi|x|)]=\delta_0\). Thus
\[
                       u(x)=\frac1{4\pi|x|}
                                  -\frac2{4\pi|x-b|}
\]
is locally integrable and has the specified forcing. The two distinct nonzero atoms give forcing singular support \(\{0,b\}\); Theorem 1.2 gives the same singular support for \(u\).

We verify the analytic hypothesis for its Newton kernel as well. Near any \(x_0\ne0\), write \(|x|^2=|x_0|^2(1+s(x))\) with \(s(x_0)=0\) and \(s\) polynomial. The series
\[
 F(s)=\sum_{k=0}^\infty(-1)^k\frac{\binom{2k}k}{4^k}s^k
\]
converges for \(|s|<1\), since the absolute coefficient ratio is \((2k+1)/(2k+2)\le1\). It may be differentiated on smaller disks. The same coefficient recursion gives \(2(1+s)F'+F=0\), hence \(((1+s)F^2)'=0\). The constant is one because \(F(0)=1\), and for small real \(s\), continuity chooses the positive square root. Therefore \(|x|^{-1}=|x_0|^{-1}F(s(x))\) is a convergent real power series near \(x_0\). Any two solutions of the original equation differ by a harmonic distribution, which Theorem 2.2 consequently makes a real-analytic harmonic function on all of \(\mathbb R^3\).

**Solution 3.** Take
\[
             U_j(z_1,z_2)=\frac{(z_1+iz_2)^j+(z_1-iz_2)^j}{2}.
\]
On the real plane the two powers are conjugates, giving the required trace. Their real Laplacians vanish because the second derivatives have respective factors \(1\) and \(i^2=-1\). For compact \(A\Subset Z\), choose \(0<\rho<1\) bounding both moduli on \(A\). If \(|\alpha|=k\le j\), differentiating each power gives a factor of modulus one times
\((j)_k(z_1\pm iz_2)^{j-k}\), where \((j)_k=j(j-1)\cdots(j-k+1)\). Thus
\[
                  \sup_A|\partial_z^\alpha U_j|
                                    \le(j)_k\rho^{j-k}.
\]
For fixed \(k\), the right side tends to zero: the ratio of successive terms tends to \(\rho<1\), so the tail is bounded by a decreasing geometric sequence. If \(k>j\), the derivative is zero. All real derivatives of these holomorphic polynomials are complex derivatives times powers of \(i\), so the same conclusion holds for them. On real \((x,y)\), both moduli are \(\sqrt{x^2+y^2}\), proving containment of the real disk.

**Solution 4.** The divergence theorem with its full proof is U011, Theorem 2.1. For harmonic \(h\) define \(M_h(r)=(4\pi)^{-1}\int_{\mathbb S^2}h(r\omega)\,d\omega\). The sphere area \(4\pi\) and scaling of surface measure are proved in angular foundations A4–A5. Differentiation under the compact sphere integral and the divergence theorem give
\[
 M_h'(r)=\frac1{4\pi r^2}\int_{\partial B_r}\partial_\nu h\,dS
        =\frac1{4\pi r^2}\int_{B_r}\Delta h\,dx=0.
\]
Continuity as \(r\downarrow0\) gives \(M_h(r)=h(0)\). For complex \(h\), apply the calculation to its real and imaginary parts. If the error on the two spheres is at most \(\varepsilon\), averaging yields
\[
                  |h(0)-1|\le\varepsilon,\qquad
                  |h(0)-1/2|\le\varepsilon.
\]
The triangle inequality implies \(1/2\le2\varepsilon\). The constant \(h=3/4\) attains error \(1/4\) on both spheres, proving sharpness. The forbidden decomposition has \(K=\overline B_{1/2}\) and \(F=\{x\in X:|x|\ge5/2\}\), which is closed relative to \(X\).

**Solution 5.** The interval proof preceding Example 7.1 shows every distributional null solution of \(\partial_x^2\) is affine. The atom combination evaluates \(a+bx\) as \((a-b)-2a+(a+b)=0\), while the second derivative jet also evaluates it as zero. Hence \(w\) annihilates the entire null space.

The triangle is continuous with successive slopes \(0,1,-1,0\). Integrating by parts on the four intervals gives no point term in the first derivative, because the function values match; differentiating the resulting step function gives
\[
                      T''=\delta_{-1}-2\delta_0+\delta_1.
\]
Therefore \(v=T+\delta_0\) solves \(v''=w\) and is compact. The difference of two compact solutions is affine, and an affine function with compact support is zero, proving uniqueness.

The formula for \(w\) gives order at most two. Choose a smooth cutoff equal to one near zero and supported in \((-1/2,1/2)\); multiply it by \(x^2/2\) to obtain \(\psi\) with \(\psi(0)=0,\psi''(0)=1\). For \(\phi_\varepsilon(x)=\varepsilon^2\psi(x/\varepsilon)\), the support stays in a fixed compact set, \(\|\phi_\varepsilon\|_\infty\to0\) and \(\|\phi_\varepsilon'\|_\infty\to0\), but \(w(\phi_\varepsilon)=1\). This excludes an order-one estimate and proves exact order two.

**Solution 6.** Theorem 4.1 allows approximation in every specified finite smooth seminorm, so the stronger choice is possible. Set \(r_j=h_j-w_j=t_{j+1}-t_j\). For \(j\ge k\), these are smooth null solutions on \(X_k\); on \(K_{k-1}\) and for \(0\le r\le k\), nesting and the chosen estimate give \(\|r_j\|_{C^r(K_{k-1})}<2^{-j}\). For any other compact subset of \(X_k\) and any derivative order, all sufficiently late \(j\)'s also control that seminorm, since the \(K_{j-1}\)'s exhaust \(X\). B1 therefore gives a smooth null sum \(R_k=\sum_{j\ge k}r_j\) on \(X_k\).

The telescoping relation identifies \(u=t_k+R_k\) on \(X_k\), consistently on overlaps, and
\[
                      \|R_k\|_{C^r(K_{k-1})}
                         \le\sum_{j\ge k}2^{-j}=2^{1-k}.
\]
Although \(u\) and \(t_k\) may be singular distributions, their difference \(R_k\) is smooth; the seminorm is applied only to that difference. Two choices of corrections yield solutions with equal forcing, hence an analytic null difference by Theorem 2.2.

**Solution 7.** Let \(b(x)=x_+^4/4!\). The kernel \(A_4=b(x)b(y)\), convolved with the prescribed point derivatives, gives
\[
                         a(x,y)=b'(x)b''(y)
                                  =\frac{x_+^3y_+^2}{12}.
\]
Identity (6.1) yields \(\partial_x^5b=\delta_0\). Commuting the extra derivatives in the two coordinates proves \(\partial_x^5\partial_y^5a=g\). Since \(x_+^3\in C^2\) and \(y_+^2\in C^1\), \(a\in C^1(\mathbb R^2)\). For any fixed \(x>0\), the second \(y\)-derivative has one-sided values \(0\) and \(x^3/6\) at \(y=0\), so \(a\notin C^2(\mathbb R^2)\). Its exact global regularity in the integer scale is \(C^1\).

The ten derivatives of \(a\) have positive integration-by-parts sign, whereas the three derivatives in \(g\) have negative sign. Thus
\[
          \int_{\mathbb R^2}a(x,y)\,
                  \partial_x^5\partial_y^5\phi(x,y)\,dx\,dy
                          =-\partial_x\partial_y^2\phi(0,0).
\]
This also shows order at most three. For the lower bound take \(\psi(x,y)=xy^2/2\) times a compact cutoff equal to one near zero, so \(\partial_x\partial_y^2\psi(0,0)=1\). The tests
\(\phi_\varepsilon(x,y)=\varepsilon^3\psi(x/\varepsilon,y/\varepsilon)\)
have every derivative through total order two tending uniformly to zero on one common compact support, whereas \(g(\phi_\varepsilon)=-1\). Hence no order-two estimate exists, and the exact order is three.

**Solution 8.** Each component \(I\) of an open subset of the line is an open interval: connected subsets of the line contain every intermediate point, since a missing point separates them into two nonempty relatively open pieces. Components of an open set are open by the small-interval argument. Example 7.1 therefore gives \(u(x)=c_Ie^{\lambda x}\) on each component of \(X\), with independent coefficients.

The exact criterion is that each component \(I\) of \(X\) meet at most one component \(J\) of \(Y\). To prove necessity even for density, suppose two components \(J_1,J_2\subset I\) are prescribed different coefficients \(d_1,d_2\), and choose \(x_i\in J_i\). Every restricted solution satisfies \(e^{-\lambda x_1}u(x_1)=e^{-\lambda x_2}u(x_2)\). Point evaluation is continuous in the smooth topology, so no convergent sequence of such restrictions can reach the prescribed unequal coefficients.

Conversely, under the criterion, assign \(c_I=d_J\) when \(I\) meets \(J\), and \(c_I=0\) when it meets none. The resulting function is smooth and null on \(X\): each point has a neighborhood in its own component. It restricts exactly to the requested function on \(Y\). Arbitrarily many components cause no problem. This proves surjectivity and therefore density.

For \(X_1,Y_1\) the criterion fails, since one ambient interval meets both smaller components; the closed gap \([-1,1]\) is the compact separated complement. For \(X_2,Y_2\) the two ambient components meet one smaller component each, so restriction is onto. Its relative complement is \([-1,0)\cup(0,1]\). Each of these is connected and approaches the missing endpoint zero; a nonempty relatively clopen piece must contain at least one entire such component and cannot be compact in \(X_2\).

Finally, for \(\lambda=0\), any constant \(c\) has maximum error \(\max(|c-c_-|,|c-c_+|)\ge|c_+-c_-|/2\) by the triangle inequality. The midpoint \(c=(c_-+c_+)/2\) attains equality, including for complex coefficients.

## Programme proof locations and freely accessible sources

- [U021: convolution](convolution-as-addition-of-supports.md), B0–B3, Theorems 1.1, 2.1, 3.1, 3.2, 4.1 and Corollary 4.2: all localization, proper convolution, finite regularity and singular-support statements used here. [U008: order and limits](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1: finite-order actions and uniform bounded-test convergence.
- [Functional foundations](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Section 5: complete norm-preserving real and complex Hahn–Banach, used in Lemma 3.1 after the proved seminorm quotient. [U015](holomorphic-boundaries-in-convex-cones.md), Section 3: polydisk Cauchy estimates, convergent holomorphic Taylor series and identity principle.
- [U030](convex-supports-and-convolution-cancellation.md), Corollary 4.3: compact differential support-hull equality. [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A3: full point-supported distribution theorem and jet independence; A4–A5: sphere measure, scaling and area. [U011](boundary-flux-and-weak-identities.md), Theorem 2.1: divergence theorem. [U020](point-sources-and-complex-gaussian-kernels.md), Theorems 1.1 and 4.1: Newton and heat point-source normalizations.
- [Metric foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, [stable algebra foundations](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10, and [Banach foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.1–15.4, 16.1–16.2: scalar calculus, cutoffs, finite-dimensional compactness, finite algebra, integral convergence and product measures. The supplied components retain their stated licenses.
- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), October 2, 2026, Theorem 4.6 and Proposition 4.12, pp. 46–49, and the proof of Theorem 9.14, pp. 103–104. These freely available notes supply the compact-duality and localized fundamental-solution proof mechanisms; the complete needed arguments are given above.
- Bernard Malgrange, [*Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution*](https://www.numdam.org/item/10.5802/aif.65.pdf), *Annales de l'Institut Fourier* 6 (1956), 271–355, Chapter III, §1, Theorems 1–2, and §2, Propositions 4–8, especially pp. 328–337. This freely readable original paper supplies the annihilator, compact-hole and summable-correction methods. The present lesson proves the needed scalar constant-coefficient assertions directly from its analytic fundamental-solution hypothesis, including both ambient-domain cases, all local prerequisites and arbitrary distributional forcing.

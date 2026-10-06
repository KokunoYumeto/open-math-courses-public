# Spectral calculus with its domains retained

**Draft. Self-checked by the writing AI.**

Continuous functions of a bounded normal operator already belong to the bounded calculus. The additional construction here is a measurable calculus, followed by a change of variable that recovers every self-adjoint operator. The construction uses cyclic subspaces one at a time; its indexing family may have any cardinality. Exact product domains, rather than formal multiplication of symbols, determine its unbounded rules.

## Inputs and conventions

Hilbert spaces are complex, complete, and of arbitrary dimension. Inner products are linear in the first entry. The zero space is allowed. A self-adjoint operator includes a dense domain and equals its Hilbert-space adjoint with that domain. An operator equality always includes equality of domains. The index set \(\mathbb N\) in this unit means the positive integers.

The inputs are the existing Hilbert completion, projection, Riesz, and bounded-adjoint contracts, and OA-MOD-OPEN-CSTAR-CFC, including the continuous calculus of a bounded normal operator. The elementary adjoint test needed for the Cayley transform is proved directly in SK-06. No closed-form representation, polar decomposition, or unbounded spectral theorem is an input.

Two scalar measure contracts are used. **SK-DEP-RMK** is the representation of a positive real linear functional on the continuous real functions of a compact metric space by a unique finite regular Borel measure. **SK-DEP-MEASURE** comprises integration of nonnegative measurable functions, monotone convergence, scalar dominated convergence, the Cauchy–Schwarz inequality for square-integrable functions, completeness of scalar \(L^2\), and approximation of measurable functions by simple functions. These contracts concern finite scalar measures, not operator-valued measures. The exact proof bindings for these contracts and the additional elementary bridges remain open.

For a finite measure \(\mu\), \(L^2(\mu)\) consists of complex measurable functions with finite squared integral, modulo equality almost everywhere, with inner product \(\langle f,g\rangle=\int f\bar g\,d\mu\). This is the linear-first version of the imported scalar Hilbert structure. For an arbitrary family \((H_j)_{j\in J}\), its Hilbert direct sum consists of families \((x_j)\) for which \(\sum_j\|x_j\|^2<\infty\), where a sum of nonnegative terms means the supremum of finite subsums. Every such family has countable support: for each positive integer \(n\), only finitely many squared norms can exceed \(1/n\). Consequently the scalar convergence arguments below always concern an ordinary finite measure for each fixed vector.

## A continuous cyclic representation becomes multiplication

Let \(K\) be a compact metric space, and let \(\rho:C(K)\to B(H)\) be a unital *-representation. For \(\xi\in H\), put

\[
H_\xi=\overline{\{\rho(f)\xi:f\in C(K)\}}.
\]

This is reducing for every \(\rho(f)\), because multiplication by \(f\) and by \(\bar f\) preserves the displayed dense subspace.

**Lemma.** There is a unique finite regular Borel measure \(\mu_\xi\) on \(K\) satisfying

\[
\langle\rho(f)\xi,\xi\rangle=\int_K f\,d\mu_\xi,
\qquad \mu_\xi(K)=\|\xi\|^2,
\tag{SK.1}
\]

and a unitary \(V_\xi:L^2(\mu_\xi)\to H_\xi\) such that

\[
V_\xi f=\rho(f)\xi\quad(f\in C(K)),\qquad
V_\xi M_fV_\xi^*=\rho(f)|_{H_\xi}.
\tag{SK.2}
\]

Here \(M_f\) is multiplication by the continuous function \(f\).

**Proof.** For real continuous \(f\geq0\), its continuous square root gives
\(\langle\rho(f)\xi,\xi\rangle=\|\rho(\sqrt f)\xi\|^2\geq0\).
Every continuous function on compact \(K\) has compact support, so \(C_c(K,\mathbb R)=C(K,\mathbb R)\). Apply SK-DEP-RMK to the displayed positive real functional. Real and imaginary parts give (SK.1) for complex \(f\). Substitution of the constant one gives the total mass. Also \(\rho\) is contractive: if \(C=\|f\|_\infty\), then \(C^2-|f|^2\) has a continuous nonnegative square root, so \(\rho(f)^*\rho(f)\leq C^2I\). Thus \(\|\rho(f)\|\leq C\), justifying each continuous extension used here.

We give the density step explicitly. If \(B\subseteq K\) is Borel and \(\varepsilon>0\), regularity supplies a compact \(F\subseteq B\) and an open \(O\supseteq B\) with \(\mu_\xi(O\setminus F)<\varepsilon\). There is a continuous \(h:K\to[0,1]\) equal to one on \(F\) and zero off \(O\). When both closed sets are nonempty, take

\[
h(x)=\frac{d(x,K\setminus O)}{d(x,F)+d(x,K\setminus O)}.
\]

The denominator is positive everywhere. If \(F=\varnothing\), use zero; if \(F\ne\varnothing\) and \(O=K\), use one. Thus \(\|h-1_B\|_2^2\leq\mu_\xi(O\setminus F)<\varepsilon\). Finite linear combinations approximate Borel simple functions. Truncating a square-integrable function and subdividing a bounded square in the complex plane approximates it by simple functions in \(L^2\); the squared tail tends to zero by monotone convergence. Therefore \(C(K)\) is dense in \(L^2(\mu_\xi)\). For completed measures, choose Borel representatives; changing null sets does not affect the argument.

The *-homomorphism property now gives

\[
\|\rho(f)\xi\|^2=\langle\rho(|f|^2)\xi,\xi\rangle
=\int|f|^2\,d\mu_\xi.
\]

Hence the rule in (SK.2) is a well-defined isometry on a dense subspace and extends to an isometry on \(L^2\). Its range is closed and contains a dense subspace of \(H_\xi\), so it is onto. Multiplication on continuous functions proves the intertwining identity on a dense subspace, and boundedness extends it. \(\square\)

## An arbitrary representation is a sum of cyclic ones

**Proposition.** With \(K,\rho,H\) as above there is a family of finite regular Borel measures \((\mu_j)_{j\in J}\) and a unitary

\[
V:\bigoplus_{j\in J}L^2(\mu_j)\longrightarrow H
\]

such that \(V^*\rho(f)V=\bigoplus_j M_f\) for every continuous \(f\).

**Proof.** Use the maximal principle on families of nonzero pairwise orthogonal cyclic subspaces of the type in SK-02, ordered by inclusion of families. The union of a chain is again such a family, so a maximal family exists. Its closed orthogonal sum is reducing. If its orthogonal complement were nonzero, a nonzero vector in the complement would generate a nonzero cyclic subspace orthogonal to the family, contrary to maximality. Thus the sum is \(H\). The unitaries in (SK.2) combine to the stated unitary: finite sums are isometric, and their ranges are dense. On the zero space use the empty family. \(\square\)

The maximal principle gives neither a countable index set nor a cyclic vector for all of \(H\). Completeness of the direct sum can also be checked without such a restriction. A Cauchy sequence has limits in every coordinate. Every finite sum of squared errors is bounded by the same Cauchy estimate; take the supremum over finite sets to obtain a vector in the direct sum and convergence to it.

## Bounded Borel functions and the spectral measure

Fix a decomposition from SK-03. For a bounded Borel function \(f:K\to\mathbb C\), define

\[
\Phi(f)=V\left(\bigoplus_jM_f\right)V^*,\qquad
E(B)=\Phi(1_B)\quad(B\subseteq K\text{ Borel}).
\tag{SK.3}
\]

Then \(\Phi\) is a unital *-homomorphism, \(\|\Phi(f)\|\leq\|f\|_\infty\), and its restriction to continuous functions is \(\rho\). The operators \(E(B)\) are orthogonal projections with

\[
E(K)=I,\quad E(B)E(C)=E(B\cap C),\quad
E\left(\bigcup_n B_n\right)x=\sum_n E(B_n)x
\tag{SK.4}
\]

for disjoint Borel sets \(B_n\), with norm convergence of the last sum.

**Proof.** All algebra and adjoint identities hold pointwise for multiplication, with uniform operator bounds, hence on the Hilbert sum. If \(V^*x=(x_j)\), define the finite Borel measure

\[
\mu_x(B)=\sum_j\int_B |x_j|^2\,d\mu_j.
\tag{SK.5}
\]

Only countably many summands are nonzero, and \(\mu_x(K)=\|x\|^2\). Countable additivity follows by interchanging nonnegative countable sums, which follows by taking suprema of their finite subsums. Formula (SK.5) gives

\[
\|\Phi(f)x\|^2=\int_K|f|^2\,d\mu_x,\qquad
\mu_x(B)=\langle E(B)x,x\rangle.
\tag{SK.6}
\]

For a disjoint union, the squared norm of the tail in (SK.4) is the measure of the remaining union and tends to zero. This proves strong countable additivity.

More generally, if bounded Borel functions \(f_n\to f\) pointwise and \(|f_n|\leq C\), dominated convergence in (SK.6) gives \(\Phi(f_n)x\to\Phi(f)x\) for every \(x\). This assertion is for sequences, not an unrestricted interchange of a net and an integral. \(\square\)

**Uniqueness and independence.** The extension in (SK.3) is the unique *-homomorphism extending \(\rho\) and preserving uniformly bounded pointwise sequential limits in the strong operator topology.

Here is the measurable-generation detail. For an open subset \(O\) of a compact metric space, the continuous functions
\(h_n(x)=\min(1,n\,d(x,K\setminus O))\) increase to \(1_O\); use \(h_n=1\) when \(O=K\). Thus any two such extensions agree on open-set indicators. The class of sets whose indicators have equal images contains \(K\), is closed under complements, and under countable disjoint unions, the last by bounded pointwise convergence of finite sums. It is a Dynkin class containing the open sets, which are closed under finite intersections.

We recall the set argument. Let \(\mathcal P\) be the intersection-closed family of open sets, and \(\mathcal D\) the smallest Dynkin class containing it. For \(A\in\mathcal P\), the sets \(B\) with \(A\cap B\in\mathcal D\) form a Dynkin class: complements use \(A\setminus(A\cap B)\), and disjoint unions use their intersections with \(A\). This class contains \(\mathcal P\), hence \(\mathcal D\). Next, for a fixed \(B\in\mathcal D\), the same argument shows that the sets \(A\) with \(A\cap B\in\mathcal D\) form a Dynkin class containing \(\mathcal P\), hence \(\mathcal D\). Thus \(\mathcal D\) is closed under intersections. Complements and disjointization now make it a sigma algebra. It contains every Borel set. Equality of the two extensions follows on Borel indicators, then on simple functions, and finally on bounded Borel functions by uniform simple approximation. This proves uniqueness without retaining a cyclic decomposition in the conclusion.

For a bounded normal operator \(T\), apply this construction to its continuous calculus on the compact metric set \(K=\sigma(T)\subseteq\mathbb C\). Then \(T=\Phi(z\mapsto z)\). This is the bounded normal spectral theorem used below.

We will also use the following consequence of the already imported continuous calculus. Polynomials in \(z,\bar z\) are dense in \(C(K)\). Indeed that calculus is an isometric isomorphism onto \(C^*(I,T)\), and by definition the latter is the norm closure of the unital *-polynomials in \(T,T^*\). Pulling these approximations back through the isometry proves the assertion. This makes explicit the approximation content already present in the continuous-calculus input.

## Unbounded measurable functions

Let \(E\) be the spectral measure just constructed. For a finite-valued Borel \(f:K\to\mathbb C\), put

\[
\begin{aligned}
D(f(E))&=\left\{x:\int_K|f|^2\,d\mu_x<\infty\right\},\\
V^*f(E)x&=(fx_j)_j\qquad(V^*x=(x_j)_j).
\end{aligned}
\tag{SK.7}
\]

The same construction applies after a measurable change of the scalar variable, in particular to measures on \(\mathbb R\). Values on a set \(N\) with \(E(N)=0\) can be assigned arbitrarily, including replacing an undefined scalar value by zero.

**Theorem.** The operator in (SK.7) is densely defined and closed, has adjoint \(\bar f(E)\), and is self-adjoint when \(f\) is real-valued. Its kernel is \(E(\{f=0\})H\). For Borel \(f,g\),

\[
\begin{aligned}
D(f(E)g(E))&=D(g(E))\cap D((fg)(E)),\\
f(E)g(E)x&=(fg)(E)x\quad\text{on this domain},\\
\overline{f(E)g(E)}&=(fg)(E).
\end{aligned}
\tag{SK.8}
\]

Likewise \(f(E)+g(E)\) on \(D(f(E))\cap D(g(E))\) has closure \((f+g)(E)\). Every spectral cutoff \(E(\{|f|\leq n\})\) preserves \(D(f(E))\), and these cutoffs converge to the identity in its graph norm.

**Proof.** Write \(P_n=E(\{|f|\leq n\})\). By (SK.6), \(P_nx\to x\), and \(P_nH\subseteq D(f(E))\), proving density. For closedness suppose \(x_m\to x\) and \(f(E)x_m\to y\). Bounded multiplication by \(f1_{\{|f|\leq n\}}\) gives

\[
\Phi(f1_{\{|f|\leq n\}})x=P_ny.
\]

Consequently \(\int_{\{|f|\leq n\}}|f|^2d\mu_x\leq\|y\|^2\) for all \(n\). Monotone convergence puts \(x\) in the domain. The same identities and \(P_n\to I\) show \(f(E)x=y\).

The multiplication pairing proves \(\bar f(E)\subseteq f(E)^*\). Conversely suppose \(y\in D(f(E)^*)\) with adjoint image \(z\). Testing its defining pairing on all vectors in \(P_nH\) gives
\(\Phi(\bar f1_{\{|f|\leq n\}})y=P_nz\).
The bounded-integral argument with \(\bar f\) shows that \(y\in D(\bar f(E))\) with image \(z\). Thus the adjoint equality, including its domain, is proved. The norm identity gives the kernel assertion.

The scalar measure of \(g(E)x\), when this vector exists, is

\[
d\mu_{g(E)x}=|g|^2d\mu_x.
\tag{SK.9}
\]

This follows on Borel sets from the direct-sum multiplication formula, and determines the measures. Thus membership in the product domain is exactly the two integrability conditions in (SK.8), and its action is pointwise multiplication. To prove the closure equality, truncate by
\(Q_n=E(\{|f|\leq n,\ |g|\leq n\})\).
For \(x\in D((fg)(E))\), each \(Q_nx\) lies in the product domain, and the omitted integrals of \(1+|fg|^2\) tend to zero. These vectors approximate \(x\) in the graph norm of \((fg)(E)\). The product is a restriction of that closed operator and has a graph core for it, proving (SK.8). The same cutoffs with integrable majorant \(1+|f+g|^2\) prove the sum statement. Taking only the \(f\)-cutoffs proves the final assertion. \(\square\)

The construction is independent of the cyclic decomposition. Indeed, its bounded cutoff operators are already determined by SK-04, and their graph limit on the domain characterized in (SK.7) is \(f(E)\). The norm identity in (SK.6) continues to hold on that domain, by monotone convergence.

No rule above says that an everywhere-defined scalar identity makes the domain of an operator product all of \(H\). For example, if \(f\) never vanishes, the product \((1/f)(E)f(E)\) is the identity restricted to \(D(f(E))\).

## Recovering a self-adjoint operator from a unitary

**Theorem.** Every self-adjoint \(A:D(A)\subseteq H\to H\) has a unique projection-valued Borel measure \(E_A\) on \(\mathbb R\) such that

\[
A=\int_{\mathbb R}t\,dE_A(t),\qquad
D(A)=\left\{x:\int t^2\,d\langle E_A(t)x,x\rangle<\infty\right\}.
\tag{SK.10}
\]

All conclusions of SK-04–05 apply to \(f(A)=\int f\,dE_A\).

**Proof of existence.** If \(H=0\), the unique operator has domain \(0\), and the unique projection-valued measure assigns the zero projection to every set; all assertions follow directly. In the rest of this proof assume \(H\ne0\).

Self-adjointness also implies closedness directly. If \(x_m\to x\) and \(Ax_m\to y\), then for each \(v\in D(A)\),
\(\langle y,v\rangle=\lim_m\langle Ax_m,v\rangle=\langle x,Av\rangle\).
Conjugating this identity is exactly the adjoint-domain test \(x\in D(A^*)\), \(A^*x=y\). Since \(A=A^*\), the graph is closed. Moreover self-adjointness gives

\[
\|(A\pm i)x\|^2=\|Ax\|^2+\|x\|^2.
\tag{SK.11}
\]

The range of \(A\pm i\) is closed: a convergent sequence of images gives Cauchy sequences for both \(x\) and \(Ax\), and closedness of \(A=A^*\) finishes the argument. Its orthogonal complement is \(\ker(A\mp i)=0\), by the adjoint definition and (SK.11). Thus the ranges are all of \(H\), and \(R=(A+i)^{-1}\) is bounded with norm at most one.

Define

\[
U=(A-i)(A+i)^{-1}=I-2iR.
\tag{SK.12}
\]

Equation (SK.11) proves isometry; surjectivity of \(A-i\) proves that it is onto. Thus \(U\) is unitary. Also \(I-U=2iR\) is injective. Apply SK-04 to this bounded normal operator. Its spectrum is a subset of the unit circle: for \(|z|>1\), a geometric series in \(U/z\) inverts \(U-zI\); for \(|z|<1\), factor \(U-zI=U(I-zU^*)\) and use the same series. Its spectral projection at \(1\) is zero by the kernel assertion in SK-05 applied to \(1-z\).

The functions

\[
c(t)=\frac{t-i}{t+i},\qquad
a(z)=i\frac{1+z}{1-z}
\tag{SK.13}
\]

are inverse continuous bijections between \(\mathbb R\) and the unit circle with \(1\) removed. Extend \(a\) by zero at \(1\). It is real-valued on the unit circle. SK-05 constructs a self-adjoint \(B=a(U)\). The scalar identity
\((a(z)+i)^{-1}=(1-z)/(2i)\) off \(1\), together with its zero spectral projection, gives

\[
(B+i)^{-1}=(I-U)/(2i)=R.
\tag{SK.14}
\]

To justify the inverse including domains, multiplication by \((a+i)^{-1}\) has range in \(D(a(U))\), because \(|a/(a+i)|\leq1\). Both compositions with \(a(U)+i\) are the identity on their respective domains by (SK.8). Equality of the inverses means equality of their actual ranges and inverse actions. Hence \(D(B)=D(A)\) and \(B=A\). Pushing the spectral measure of \(U\) forward under \(a\) gives \(E_A\), proving (SK.10).

**Proof of uniqueness.** Suppose another projection-valued measure \(F\) represents \(A\) with the domain in (SK.10). Its scalar measures define integrals by bounded simple functions and uniform approximation, and unbounded integrals by spectral cutoffs. Orthogonality gives the squared-integral identity for simple functions. Approximation then gives that identity and the product and adjoint rules of SK-05 for these integrals. Consequently its bounded integral of \(c(t)\) equals \(U\). The pushforward \(G\) on the unit circle represents \(U\).

This pushforward is concentrated on \(\sigma(U)\). To see the only possible extra support issue explicitly, for \(z_0\notin\sigma(U)\) put \(d=\|(U-z_0)^{-1}\|^{-1}>0\). For a sufficiently small neighborhood \(O\) of \(z_0\), a vector \(x\in G(O)H\) satisfies
\(\|(U-z_0)x\|\leq(d/2)\|x\|\), whereas the bounded inverse requires a lower bound \(d\|x\|\). Thus \(G(O)=0\). The circle is second countable, so its complement of \(\sigma(U)\) is covered by countably many such neighborhoods and has zero projection. This countability belongs to the scalar circle, not to \(H\).

On \(\sigma(U)\), integrals of polynomials in \(z,\bar z\) agree with the continuous calculus, by the multiplicative rules. The uniform density of these polynomials, part of the normal continuous-calculus construction, gives agreement on all continuous functions. The extension defined by \(G\) preserves bounded pointwise sequential limits by its scalar dominated-convergence identity. Thus uniqueness in SK-04 identifies \(G\) with the spectral measure of \(U\). Since \(c\) is a Borel bijection onto the circle minus \(1\), the original measures on \(\mathbb R\) agree. \(\square\)

If \(A\geq0\), its spectral measure vanishes on \((-\infty,0)\). Indeed a nonzero vector in \(E_A([-n,-1/n])H\) belongs to \(D(A)\) and has strictly negative quadratic value, contradicting positivity. Those intervals cover the negative half-line. The converse follows by integrating \(t\geq0\).

## Changes of variable, powers, and actual ranges

If \(g:\mathbb R\to\mathbb R\) is finite Borel, the spectral measure of \(g(A)\) is

\[
E_{g(A)}(B)=E_A(g^{-1}(B)).
\tag{SK.15}
\]

Therefore, for every finite Borel \(f\),

\[
f(g(A))=(f\circ g)(A)
\tag{SK.16}
\]

with equality of their squared-integral domains.

**Proof.** The pushforward projections satisfy strong countable additivity by SK-04. Scalar change of variables follows first for indicators, then for simple functions and by monotone convergence for nonnegative functions; real and imaginary parts handle integrable functions. Its integral of the coordinate function consequently has exactly the domain and action of \(g(A)\). Uniqueness in SK-06 proves (SK.15), and the same change of variables proves (SK.16). \(\square\)

For \(A\geq0\), the operator \(A^{1/2}\) is nonnegative self-adjoint,

\[
D(A^{1/2})=\{x:\int t\,d\mu_x(t)<\infty\},\qquad
(A^{1/2})^2=A.
\tag{SK.17}
\]

For the equality of domains of the square, \(\int t^2d\mu_x<\infty\) implies \(\int t\,d\mu_x<\infty\) by \(t\leq1+t^2\). It is the unique nonnegative self-adjoint square root. In fact, if \(B\geq0\) and \(B^2=A\), (SK.16) applied to \(t^2\) and then its nonnegative square root gives \(A^{1/2}=B\), with domains. For \(x\in D(A)\), \(y\in D(A^{1/2})\), truncation and Cauchy–Schwarz give

\[
\langle A^{1/2}x,A^{1/2}y\rangle=\langle Ax,y\rangle.
\tag{SK.18}
\]

It holds after cutting both vectors to bounded spectral intervals. The left side converges in the square-root norm, and the right side in the graph norm of \(A\) for the first vector and the Hilbert norm for the second.

If \(\ker A=0\), then \(E_A(\{0\})=0\). Define the inverse by \(t^{-1}\) on \((0,\infty)\), and assign any finite value at zero. It is nonnegative self-adjoint and

\[
D(A^{-1})=\operatorname{ran}A,\qquad
A^{-1}Ax=x\ (x\in D(A)),\qquad
AA^{-1}y=y\ (y\in D(A^{-1})).
\tag{SK.19}
\]

For if \(y=Ax\), its inverse squared-integral is \(\int t^{-2}t^2d\mu_x=\|x\|^2\). Conversely, for \(y\in D(A^{-1})\), the vector \(x=A^{-1}y\) has \(\int t^2d\mu_x=\|y\|^2\) and \(Ax=y\). The range of an injective self-adjoint operator is dense, since its orthogonal complement is the kernel of its adjoint. Injectivity requires no positive lower spectral bound.

For \(\lambda>0\), \(B=(A+\lambda I)^{-1}\) is bounded, positive and injective, and the same scalar calculation gives

\[
\operatorname{ran}B^{1/2}=D(A^{1/2}),\qquad
\|B^{-1/2}x\|^2=\lambda\|x\|^2+\|A^{1/2}x\|^2.
\tag{SK.20}
\]

The two integrability conditions are \(\int(t+\lambda)d\mu_x<\infty\) and \(\int t\,d\mu_x<\infty\), which coincide because \(\mu_x\) is finite.

For injective \(A\geq0\) and \(z\in\mathbb C\), let \(A^z\) use \(t^z=e^{z\log t}\) on \((0,\infty)\). Then

\[
D(A^z)=\{x:\int t^{2\operatorname{Re}z}\,d\mu_x(t)<\infty\}.
\tag{SK.21}
\]

The operators \(A^{is}\), \(s\in\mathbb R\), are unitaries and form a strongly continuous group. The group identities follow from bounded multiplication. Strong continuity follows from dominated convergence in
\(\|(A^{is}-A^{ir})x\|^2=\int|t^{is}-t^{ir}|^2d\mu_x\), with bound \(4\). Since \(|t^{is}|=1\), these unitaries preserve every domain in (SK.21) and commute there with \(A^z\). The self-adjoint \(\log A\) is obtained by the real Borel function \(\log t\), with any value at the zero projection, and \(e^{is\log A}=A^{is}\) by (SK.16).

## Transport, reduction, and membership in an algebra

Let \(W:H\to K\) be unitary or antiunitary, and let \(A\) be self-adjoint. The operator \(B=WAW^{-1}\) on \(WD(A)\) is self-adjoint: transport of the adjoint pairing gives \(B^*=WA^*W^{-1}\) on \(WD(A^*)\). Its spectral measure and calculus satisfy

\[
E_B(S)=WE_A(S)W^{-1},
\tag{SK.22}
\]

\[
Wf(A)W^{-1}=
\begin{cases}
f(B),&W\text{ unitary},\\
\bar f(B),&W\text{ antiunitary},
\end{cases}
\tag{SK.23}
\]

including transported domains.

**Proof.** Conjugated projections are again projections and preserve strong countable additivity. For real simple functions the integral transports without a scalar change; taking graph cutoffs proves that its integral of the real coordinate is \(B\). Uniqueness gives (SK.22). For complex simple functions anti-linearity conjugates every coefficient. Uniform bounded approximation and then graph cutoffs give (SK.23). The scalar measure at \(Wx\) equals the measure at \(x\), so the squared-integral tests give the asserted domains. \(\square\)

The calculus respects an orthogonal decomposition into reducing subspaces: the direct sum of the restricted projection-valued measures represents the direct sum operator, with the domain determined by the sum of squared image norms. Uniqueness identifies the measures. In particular, a partial isometry restricted to its initial space is a unitary onto its final space. Apply (SK.22) there and treat the orthogonal kernel space separately. This justifies the transport formulas in OA-MOD-RD-02 without assuming that the partial isometry is invertible on all of \(H\).

If a bounded operator \(b\) commutes with a bounded normal \(T\) and \(T^*\), then it commutes with every bounded Borel function of \(T\). It commutes first with the continuous calculus. For open-set indicators, use the continuous approximants in SK-04 and pass to their strong limits; multiplication by fixed \(b\) is strongly continuous. The same Dynkin-class argument and bounded simple approximation give all Borel functions. In particular, if \(T\) lies in a von Neumann algebra \(N\), every such function belongs to \(N\): it commutes with \(N'\), so the bicommutant theorem applies.

For a self-adjoint \(A\), say that \(A\) is affiliated with \(N\) when every unitary \(v\in N'\) maps \(D(A)\) onto itself and \(Avx=vAx\) there. Equation (SK.22) gives \(vE_A(S)=E_A(S)v\). The four-unitary span from OA-MOD-BK-08 and the bicommutant theorem give \(E_A(S)\in N\), and hence every bounded Borel function of \(A\) lies in \(N\). Conversely, if all its spectral projections belong to \(N\), the scalar-domain test and spectral cutoffs show that each such unitary preserves its domain and commutes with its action. These are equivalent descriptions at arbitrary dimension.

For bounded self-adjoint \(T\in N\), partition \([-\|T\|,\|T\|]\) into finitely many Borel intervals of mesh at most \(\varepsilon\) and choose one scalar in each interval. The corresponding finite spectral sum belongs to \(N\) and differs from \(T\) in norm by at most \(\varepsilon\), by (SK.6). When \(T=0\), use the single sum zero. Thus spectral step approximation is in norm, while countable additivity of the projections is strong.

## Convergence and cutoffs

For any self-adjoint \(A\), bounded Borel \(f_n\to f\) pointwise with \(|f_n|\leq C\) gives \(f_n(A)\to f(A)\) strongly. More generally, for a fixed vector \(x\), if \(f_n\to f\) pointwise and \(|f_n|\leq h\) with \(\int h^2d\mu_x<\infty\), then

\[
x\in D(f_n(A))\cap D(f(A)),\qquad f_n(A)x\longrightarrow f(A)x.
\tag{SK.24}
\]

This is scalar dominated convergence for \(|f_n-f|^2\leq4h^2\) and the exact norm formula. In particular, for positive \(A\), continuous cutoffs in \(C_c(0,\infty)\) bounded by one and converging to one on \((0,\infty)\) converge strongly to \(I-E_A(\{0\})\), including when this support is proper. Values at zero are set to zero.

For injective positive \(A\), put \(P_n=E_A([e^{-n},e^n])\). If \(x\in D(A^z)\), then \(P_nx\to x\) and \(A^zP_nx\to A^zx\) by the integrable tails of \(1+t^{2\operatorname{Re}z}\). Thus the increasing union of these spectral bands is a graph core for every \(A^z\), and is contained in all their domains. In each band \(|\log t|\leq n\), so \(w\mapsto A^wP_nx\) is an entire \(H\)-valued function. Indeed the scalar exponential power series converges uniformly on that band and on compact sets of \(w\), hence converges in operator norm there. Its termwise derivatives have the same uniform convergence. This assertion supplies spectral entire vectors; it is not an assertion about products in a Tomita algebra.

If bounded self-adjoint operators \(B_i,B\) have spectra in a fixed compact interval and \(B_i\to B\) strongly, then \(f(B_i)\to f(B)\) strongly for every continuous \(f\) on that interval. Here \(i\) may index an arbitrary net. Fixed powers converge strongly by induction using the uniform norm bound. Fixed polynomials converge strongly, and uniform polynomial approximation makes the errors in the functional calculus uniformly small in norm. For specificity, approximation on \([0,1]\) can be obtained by Bernstein polynomials: the error is at most the modulus of continuity at \(\delta\) plus \(2\|f\|_\infty/(4n\delta^2)\), because the binomial variance is at most \(1/(4n)\). First choose \(\delta\), then \(n\). Affine rescaling handles other intervals. This includes strong continuity of positive square roots on uniformly bounded positive sets.

**Core convergence theorem.** Let \(A_i,A\) be self-adjoint operators, where \(i\) ranges over any directed set. Suppose \(D\subseteq D(A)\cap\bigcap_i D(A_i)\) is a graph core for \(A\), and

\[
A_i x\longrightarrow Ax\qquad(x\in D).
\tag{SK.26}
\]

Then

\[
(A_i\pm i)^{-1}\longrightarrow(A\pm i)^{-1}
\quad\text{strongly},
\tag{SK.27}
\]

and, for every bounded continuous \(f:\mathbb R\to\mathbb C\),

\[
f(A_i)\longrightarrow f(A)\quad\text{strongly}.
\tag{SK.28}
\]

If \(A\) is bounded, any Hilbert-norm dense linear \(D\) is a graph core, so that weaker-looking hypothesis suffices. The \(A_i\) need not be bounded or uniformly bounded.

**Proof of resolvent convergence.** Put \(R_i=(A_i+i)^{-1}\), \(R=(A+i)^{-1}\). Their norms are at most one by (SK.11). For \(x\in D\),

\[
R_i(A+i)x-x=R_i(A-A_i)x\longrightarrow0.
\]

The subspace \((A+i)D\) is dense in \(H\): graph approximation to an arbitrary vector in \(D(A)\), followed by the surjective map \(A+i\), proves this. On that dense subspace the last identity is \((R_i-R)(A+i)x\to0\). The common bound \(\|R_i-R\|\leq2\) extends convergence to every vector by norm approximation. Repeat with \(-i\) to prove (SK.27). For bounded \(A\), its graph norm and Hilbert norm are equivalent by
\(\|x\|\leq\|x\|_A\leq(1+\|A\|^2)^{1/2}\|x\|\).

**Proof first for functions vanishing at infinity.** Write \(U_i=I-2iR_i\), \(U=I-2iR\). These are the unitary Cayley transforms. The two signs in (SK.27) give strong convergence of both \(U_i\) and \(U_i^*\) to \(U,U^*\). Products of uniformly bounded strongly convergent nets converge strongly, by

\[
\|(X_iY_i-XY)x\|
\leq\|X_i\|\|(Y_i-Y)x\|+\|(X_i-X)Yx\|.
\]

Thus every fixed polynomial in \(U_i,U_i^*\) converges strongly to that polynomial in \(U,U^*\).

The needed scalar approximation is by polynomials in \(z,\bar z\) on the whole unit circle. It follows from the CFC consequence in SK-04, applied to one concrete unitary whose spectrum is that circle. Namely, on \(\ell^2(\mathbb Z)\) take the bilateral shift \(Se_n=e_{n+1}\). The geometric-series argument of SK-06 puts its spectrum inside the circle. For \(|\lambda|=1\), the unit vectors

\[
x_N=(2N+1)^{-1/2}\sum_{n=-N}^N\lambda^{-n}e_n
\]

satisfy \(\|(S-\lambda)x_N\|^2=2/(2N+1)\to0\). If \(S-\lambda\) had a bounded inverse, this would contradict \(\|x_N\|=1\). Its spectrum is therefore the entire circle, and the isometric continuous calculus onto \(C^*(I,S)\) proves the desired uniform polynomial approximation. This auxiliary countable-dimensional model places no restriction on the original \(H\).

If \(f\in C_0(\mathbb R)\), let \(F(z)=f(a(z))\) off \(1\), and \(F(1)=0\), using (SK.13). As \(z\to1\) along the circle, \(|a(z)|\to\infty\), so \(F\) is continuous on the whole circle. Choose polynomials in \(z,\bar z\) converging uniformly to \(F\). The operator-norm bounds for all the unitary calculi make the approximation error uniform in \(i\). The polynomial convergence above gives
\(F(U_i)\to F(U)\) strongly. The spectral measures were constructed by the same change of variable, so these operators are \(f(A_i)\) and \(f(A)\). This proves (SK.28) for \(C_0\).

**Passage to every bounded continuous function.** Fix \(x\in H\) and \(\varepsilon>0\). Choose \(0\leq\chi\leq1\) in \(C_c(\mathbb R)\) with
\(\|(I-\chi(A))x\|<\varepsilon\). Such a cutoff exists by dominated convergence for the finite spectral measure \(\mu_x\). The already proved case gives \(\chi(A_i)x\to\chi(A)x\), so eventually
\(\|(I-\chi(A_i))x\|<2\varepsilon\). Since \(f\chi\in C_0(\mathbb R)\), we have

\[
\begin{aligned}
\|(f(A_i)-f(A))x\|
&\leq\|((f\chi)(A_i)-(f\chi)(A))x\|\\
&\quad+\|f\|_\infty\|(I-\chi(A_i))x\|\\
&\quad+\|f\|_\infty\|(I-\chi(A))x\|.
\end{aligned}
\]

The first term tends to zero, and the other two are eventually bounded by \(3\|f\|_\infty\varepsilon\). Letting \(\varepsilon\downarrow0\) proves (SK.28) for arbitrary nets. This uses scalar dominated convergence only to choose one cutoff for the fixed limiting vector; it does not apply a dominated-convergence theorem to the net \(i\). \(\square\)

The second and third parts of this proof start only from (SK.27). Thus strong convergence of both resolvents at \(i,-i\) already implies (SK.28), without the core hypothesis. In particular, taking \(f(t)=(t-z)^{-1}\) gives strong convergence of the resolvents at every nonreal \(z\). Limits of forms in OA-MOD-QF have their own proofs; this kernel supplies their functional-calculus and scalar-measure steps. No conclusion here gives strong convergence for an arbitrary bounded discontinuous \(f\).

## A domain test on an arbitrary index set

Let \(I\) be any set and choose real numbers \(a_i\). On \(H=\ell^2(I)\), define

\[
D(A)=\{x:\sum_i|a_i|^2|x_i|^2<\infty\},\qquad (Ax)_i=a_ix_i.
\tag{SK.25}
\]

Then \(A\) is self-adjoint and \(E_A(B)x=(1_B(a_i)x_i)_i\). To verify the adjoint directly, test its defining pairing on each coordinate vector: the adjoint image must have coordinates \(a_ix_i\), and existence of that image is exactly (SK.25). Finite-support vectors lie in the domain and are dense. The domain of every Borel function is consequently

\[
D(f(A))=\{x:\sum_i|f(a_i)|^2|x_i|^2<\infty\}.
\]

This model verifies the general domain formula without a separability assumption, including uncountably many distinct eigenvalues. Each individual vector still has countable support. If \(a_i>0\), the inverse has domain \(\{y:\sum_i a_i^{-2}|y_i|^2<\infty\}\), which need not be all of \(H\), even though its scalar defining function is finite at every \(a_i\).

## Problems with full solutions

**Problem 1: the product of inverse functions.** On \(\ell^2(\mathbb N)\), let \(Ae_n=ne_n\). Compare \(A^{-1}A\), \(AA^{-1}\), and the calculus of the scalar function \(t^{-1}t\).

**Solution.** The first product is \(I\) on \(D(A)=\{x:\sum n^2|x_n|^2<\infty\}\). The second is \(I\) on all of \(H\), because \(A^{-1}x=(x_n/n)\) always belongs to \(D(A)\). The scalar product is one on the spectrum, so its calculus is \(I\) on all of \(H\). Thus the closure of the first product equals that calculus, but the original domains differ. The vector \((1/n)_n\) belongs to \(H\setminus D(A)\), exhibiting the difference.

**Problem 2: an endpoint does not have to be an atom.** Let \(Ae_n=n^{-1}e_n\). Show that zero is in the spectrum, its spectral projection is zero, and \(A^{it}\) is a strongly continuous unitary group.

**Solution.** If \(A\) had a bounded inverse, \(1=\|e_n\|\leq\|A^{-1}\|/n\), impossible. Hence zero is in the spectrum. The kernel is zero, so \(E_A(\{0\})=0\). Each imaginary power multiplies the \(n\)-th coordinate by \(n^{-it}\), which has modulus one. For \(x\in\ell^2\), the squared norm of a difference is \(\sum_n|n^{-it}-n^{-is}|^2|x_n|^2\); each term tends to zero and is bounded by \(4|x_n|^2\). Dominated convergence proves strong continuity. No logarithm value at zero enters a nonzero spectral subspace.

**Problem 3: why pointwise boundedness does not suffice for strong operator convergence.** Find bounded Borel functions \(f_n\) on the spectrum of \(Ae_n=ne_n\) that converge pointwise to zero but whose operators fail to converge strongly to zero.

**Solution.** Set \(f_n(t)=n1_{\{n\}}(t)\). For each fixed spectral value, eventually \(f_n\) is zero. Each \(f_n(A)\) is bounded, but their norms are \(n\). For \(x=(1/n)_n\in\ell^2\), \(f_n(A)x=e_n\), of norm one. Thus strong convergence fails. The uniform bound or the vector-dependent integrable majorant in SK-09 is essential.

**Problem 4: antiunitary transport changes scalar coefficients.** Let \(A=\operatorname{diag}(2,3)\) and let \(C\) be coordinate conjugation on \(\mathbb C^2\). Compute \(CA^{it}C\).

**Solution.** The real diagonal operator satisfies \(CAC=A\). Conjugation changes the diagonal coefficients \(2^{it},3^{it}\) to \(2^{-it},3^{-it}\), so \(CA^{it}C=A^{-it}\). This is (SK.23). For the antiunitary involution \(J\) in OA-MOD-TC-10, the identity \(J\Delta J=\Delta^{-1}\) combines with scalar conjugation to give \(J\Delta^{it}J=\Delta^{it}\).

## What this kernel supplies

The bounded Borel calculus and its spectral projections are constructed in SK-02–04; unbounded integral domains and multiplication in SK-05; arbitrary self-adjoint spectral resolutions in SK-06; square roots, inverses, powers, and form pairings in SK-07; and transport, affiliation, and spectral step approximation in SK-08. SK-09 distinguishes scalar dominated convergence from operator-argument continuity and supplies the cutoff limits used for right Hilbert algebras.

The resulting dependency order is bounded Hilbert and continuous calculus, then SK's scalar measure inputs and construction, then the existing closed-form theorem, then the existing unbounded polar arguments in OA-MOD-TC-07–10 and OA-MOD-RD-02. The spectral construction does not depend on those polar or form conclusions.

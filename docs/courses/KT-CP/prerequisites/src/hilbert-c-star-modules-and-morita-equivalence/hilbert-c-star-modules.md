# Hilbert C*-modules

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Hilbert space measures the interaction of two vectors by a complex number. A Hilbert C*-module measures it by an element of a C*-algebra. When that algebra is \(C_0(X)\), the inner product records a separate measurement at each point of \(X\). For a noncommutative algebra, the same axioms still give a useful norm, a completion, and positive matrices of inner products. They do not give all the orthogonal decompositions available in Hilbert spaces.

This lesson develops those basic constructions for an arbitrary C*-algebra, including algebras without an identity. It assumes the normed-space background of [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20) and the material of [C*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html). Basic references are [Connes 1994], [Blackadar 2006] and [Blackadar 1998]. [Emerson 2024] gives another treatment. All the module results needed here are proved below. Representations of Hilbert modules, module tensor products and modules associated with foliations belong to later lessons.

## 1. Keeping the coefficients in the inner product

Throughout, \(A\) is a complex C*-algebra. A right \(A\)-module is also a complex vector space, and its action is complex bilinear. We write vectors on the left and coefficients on the right.

**Definition 1.1.** A *pre-Hilbert \(A\)-module* is such a module \(E\) with a map \(E\times E\to A\), written \(\langle x,y\rangle\), satisfying

\[
\begin{aligned}
\langle x,\lambda y+z\rangle&=\lambda\langle x,y\rangle+\langle x,z\rangle,\\
\langle x,ya\rangle&=\langle x,y\rangle a,\\
\langle y,x\rangle&=\langle x,y\rangle^*,\\
\langle x,x\rangle&\geq0,
\end{aligned}
\]

and \(\langle x,x\rangle=0\) only when \(x=0\). Thus the inner product is conjugate-linear in the first variable. In particular,

\[
\langle xa,yb\rangle=a^*\langle x,y\rangle b.
\tag{1.1}
\]

We will also use *positive semidefinite forms*, for which the last implication is not required. Their zero-length vectors will be removed before completion. Put

\[
\|x\|=\|\langle x,x\rangle\|^{1/2}.
\]

We prove shortly that this is a norm in the definite case. A *Hilbert \(A\)-module* is a pre-Hilbert module complete for this norm.

**Example 1.2 (The coefficient algebra).** On \(A\) itself, use its right multiplication and set \(\langle a,b\rangle=a^*b\). Linearity and (1.1) follow from multiplication and involution. Positivity follows from \(a^*a\geq0\), and the C*-identity gives \(\|a^*a\|^{1/2}=\|a\|\). Thus the form is definite and \(A\) is already complete. This module is denoted \(A_A\).

**Example 1.3 (Finite columns).** The module \(A^n\) has coordinatewise action and

\[
\langle (a_i),(b_i)\rangle=\sum_{i=1}^n a_i^*b_i.
\tag{1.2}
\]

All algebraic axioms follow term by term. A sum of positive elements is positive. If \(\sum a_i^*a_i=0\), then each summand is both nonnegative and at most zero, so every \(a_i=0\). Its completeness will follow in Section 2. When \(A=\mathbb C\), these definitions give precisely complex inner product spaces and Hilbert spaces, with the convention that the second variable is linear.

An identity in \(A\), when present, acts as the identity on a definite module: expansion gives \(\langle x-x1,x-x1\rangle=0\). For computations with a missing identity, adjoin one and let its action be scalar multiplication. More explicitly, formal elements \(a+\lambda1\) act by \(xa+\lambda x\). The identities for the form continue to hold for these coefficients. This allows us to use inverses in the unitization without assuming that \(A\) has an identity.

## 2. The estimate that makes completion possible

The useful form of Cauchy–Schwarz compares positive elements of \(A\), rather than merely their norms.

**Theorem 2.1 (Cauchy–Schwarz in the order).** For a positive semidefinite module form,

\[
\langle x,y\rangle^*\langle x,y\rangle
\leq \|\langle x,x\rangle\|\,\langle y,y\rangle.
\tag{2.1}
\]

Consequently \(\|\langle x,y\rangle\|\leq\|x\|\|y\|\).

*Proof.* Write \(b=\langle x,x\rangle\), \(c=\langle x,y\rangle\), and \(d=\langle y,y\rangle\). For \(\varepsilon>0\), continuous functional calculus in the unitization gives the positive element \(r=(b+\varepsilon1)^{-1}\). Expanding the positive element \(\langle y-xrc,y-xrc\rangle\) yields

\[
0\leq d-2c^*rc+c^*rbrc
=d-c^*rc-\varepsilon c^*r^2c.
\]

Therefore \(c^*rc\leq d\). Functional calculus also gives

\[
r\geq (\|b\|+\varepsilon)^{-1}1.
\]

Multiplication on the left by \(c^*\) and on the right by \(c\) preserves order. Hence \(c^*c\leq(\|b\|+\varepsilon)d\). Letting \(\varepsilon\) decrease to zero proves (2.1), since the positive cone is norm closed. This also handles \(b=0\). Finally, take norms and use \(\|c^*c\|=\|c\|^2\) and monotonicity of the norm on positive elements. ∎

**Proposition 2.2 (Norm and continuity).** A positive semidefinite form defines a seminorm. It is a norm for a definite form, and

\[
\|xa\|\leq\|x\|\|a\|.
\tag{2.2}
\]

*Proof.* Homogeneity follows from sesquilinearity. Expanding the inner product and using Theorem 2.1 gives

\[
\begin{aligned}
\|x+y\|^2
&\leq\|x\|^2+\|\langle x,y\rangle\|
+\|\langle y,x\rangle\|+\|y\|^2\\
&\leq(\|x\|+\|y\|)^2.
\end{aligned}
\]

Definiteness is exactly the condition that the seminorm vanish only at zero. Also

\[
\|xa\|^2=\|a^*\langle x,x\rangle a\|
\leq\|a\|^2\|x\|^2.
\]

In particular the action is continuous. For later use, Cauchy–Schwarz gives

\[
\|\langle x,y\rangle-\langle x',y'\rangle\|
\leq\|x-x'\|\|y\|+\|x'\|\|y-y'\|.
\tag{2.3}
\]
∎

**Theorem 2.3 (Removing null vectors and completing).** If \(E_0\) has a positive semidefinite form, set \(N=\{x:\|x\|=0\}\). Then \(E_0/N\) is a pre-Hilbert \(A\)-module, and its norm completion is a Hilbert \(A\)-module.

*Proof.* The seminorm laws and (2.2) make \(N\) a complex linear submodule. Theorem 2.1 implies \(\langle n,y\rangle=\langle y,n\rangle=0\) whenever \(n\in N\). Thus the form descends to the quotient and is definite there.

Construct the completion as follows. Take all Cauchy sequences in the quotient and identify two sequences when the norm of their difference tends to zero. Coordinatewise operations descend to the equivalence classes, and their norm is the limit of the sequence of norms. Constant sequences embed the quotient isometrically and densely. This space is complete: for a Cauchy sequence of classes \(X_k\), choose quotient vectors \(u_k\) within \(1/k\) of \(X_k\). The vectors \(u_k\) form a Cauchy sequence. Its class is a limit of \(u_k\), and therefore also of \(X_k\), by the triangle inequality.

For Cauchy sequences \(x_m,y_m\), formula (2.3) makes \(\langle x_m,y_m\rangle\) a Cauchy sequence in the complete algebra \(A\). Its limit is independent of the representing sequences, by the same estimate. Define the extended inner product by this limit. Define \(xa\) by the class of \(x_ma\); (2.2) makes this well-defined. All linearity and module identities pass to limits, and positivity passes to the limit through the closed positive cone. Finally,

\[
\|\langle x,x\rangle\|=\lim_m\|x_m\|^2=\|x\|^2.
\]

So the extended form is definite and induces exactly the completed norm. ∎

This construction is unique up to an isometric module map preserving the inner product and the original dense submodule. Indeed, such a map is forced on the dense submodule and then on all its limits.

**Proposition 2.4 (Finite columns are complete).** For the norm from (1.2),

\[
\max_i\|a_i\|\leq\|(a_i)\|
\leq\sqrt n\max_i\|a_i\|.
\tag{2.4}
\]

*Proof.* Each positive summand \(a_i^*a_i\) is at most their sum, giving the first inequality. The triangle inequality in \(A\) gives the second. A Cauchy sequence of columns therefore has Cauchy coordinates. Their limits form a column in \(A^n\), and the second inequality gives convergence in the module norm. ∎

Equality in the numerical Cauchy–Schwarz bound does not force one vector to be a coefficient multiple of the other. In \(C([0,1])^2\), take \(x=(1,0)\) and \(y=(t,1-t)\). Both norms are \(1\), and \(\|\langle x,y\rangle\|=\|t\|=1\). But \(y\ne xa\) for every \(a\in C([0,1])\), because its second coordinate is not zero.

## 3. Positive matrices from finite families

Before using matrix positivity, we specify its C*-norm. The Gelfand–Naimark theorem in [Representations and positive functionals](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html), Theorem 7.2, supplies a faithful representation \(A\subset B(H)\). Represent \(M_n(A)\) on \(H^n\) by its operator matrix. This is a faithful *-algebra representation, with
\[
\max_{i,j}\|a_{ij}\|\leq\|(a_{ij})\|
\leq\sum_{i,j}\|a_{ij}\|.
\]
Consequently entrywise completeness makes its image closed, and the operator C*-identity makes it a C*-algebra. The norm is independent of the faithful representation: identity on the algebraic matrix algebra is an injective homomorphism between the two completed C*-algebras, hence isometric by the functional-calculus prerequisite. Positivity and square roots can therefore be computed in this matrix algebra without choosing a representation. The next theorem proves the coefficient-column criterion for that positivity.

For scalars, a matrix is positive exactly when all its quadratic forms are nonnegative. With coefficients in \(A\), the test vectors must themselves have entries in \(A\). We use the C*-algebra structure on \(M_n(A)\) with involution \((T^*)_{ij}=T_{ji}^*\).

**Theorem 3.1 (The matrix positivity test).** An arbitrary \(T\in M_n(A)\) is positive if and only if

\[
q_T(a):=\sum_{i,j=1}^n a_i^*T_{ij}a_j\geq0
\qquad(a\in A^n).
\tag{3.1}
\]

*Proof.* If \(T\geq0\), write \(T=R^*R\) using its positive square root. Then

\[
q_T(a)=\sum_k\left(\sum_iR_{ki}a_i\right)^*
\left(\sum_jR_{kj}a_j\right)\geq0.
\]

Conversely, suppose (3.1) holds. Let \(B(a,b)=\sum a_i^*T_{ij}b_j\). Expanding \(q_T(a+b)\), \(q_T(a-b)\), \(q_T(a+ib)\) and \(q_T(a-ib)\), and using that each is self-adjoint, gives \(B(a,b)=B(b,a)^*\). Thus

\[
\sum a_i^*(T-T^*)_{ij}b_j=0
\]

for every pair of columns. Choose columns supported at positions \(i,j\), both with value \(e_\lambda\), where \((e_\lambda)\) is a positive contractive approximate identity for \(A\). Then \(e_\lambda(T-T^*)_{ij}e_\lambda=0\). Passing to the limit proves \(T=T^*\).

Now let \(S=T_-\), the negative part of \(T\) given by functional calculus. It is positive and \(STS=-S^3\). For each \(k\), apply (3.1) to the \(k\)-th column of \(S\). This gives

\[
-(S^3)_{kk}\geq0.
\]

But, writing \(R=S^{3/2}\), we have \((S^3)_{kk}=\sum_i R_{ik}^*R_{ik}\geq0\). Hence this sum is zero, so all \(R_{ik}=0\). This holds for every \(k\); consequently \(R=0\), \(S=0\), and \(T\geq0\). The argument works without an identity in \(A\). ∎

**Corollary 3.2 (Gram positivity).** For \(x_1,\ldots,x_n\) in a module with a positive semidefinite form, the Gram matrix

\[
G=(\langle x_i,x_j\rangle)_{i,j}
\]

is positive in \(M_n(A)\).

*Proof.* For every \(a\in A^n\),

\[
\sum_{i,j}a_i^*\langle x_i,x_j\rangle a_j
=\left\langle\sum_i x_i a_i,\sum_j x_j a_j\right\rangle\geq0.
\]

Apply Theorem 3.1. ∎

The order of the factors is essential: the coefficient on the first vector appears as \(a_i^*\) on the left. No commutativity of \(A\) has been used.

## 4. Infinite columns, sections and averaging

### The standard module

Define

\[
H_A=\left\{(a_k)_{k\geq1}:a_k\in A,
\quad\sum_{k=1}^{\infty}a_k^*a_k
\text{ converges in norm in }A\right\}.
\tag{4.1}
\]

The action is coordinatewise, and its proposed inner product is \(\langle a,b\rangle=\sum_k a_k^*b_k\).

**Theorem 4.1.** This series defines an inner product on \(H_A\). The module is complete, and finite columns are dense in it.

*Proof.* The elementary order inequality

\[
(u+v)^*(u+v)\leq2(u^*u+v^*v)
\]

follows by expanding \((u-v)^*(u-v)\geq0\). Applied to finite tails, it shows that adding two sequences in (4.1) again gives a sequence with norm-Cauchy square-sum partial sums. Scalar multiplication is immediate. For right multiplication by \(c\in A\), a tail is \(c^*(\sum a_k^*a_k)c\), whose norm is at most \(\|c\|^2\|\sum a_k^*a_k\|\). Thus \(H_A\) is a module.

Apply Theorem 2.1 to finite columns from indices \(m\) through \(n\). It gives

\[
\left\|\sum_{k=m}^n a_k^*b_k\right\|
\leq
\left\|\sum_{k=m}^n a_k^*a_k\right\|^{1/2}
\left\|\sum_{k=m}^n b_k^*b_k\right\|^{1/2}.
\tag{4.2}
\]

The right side tends to zero for tails, so the inner product series converges. Its algebraic axioms pass from finite sums to limits. Its diagonal values are positive. Moreover each \(a_k^*a_k\) is at most \(\langle a,a\rangle\); if the latter is zero, every coordinate is zero. This verifies definiteness.

Let \(a^{(r)}\) be a Cauchy sequence in \(H_A\). Each coordinate is Cauchy, since \(\|a_k^{(r)}-a_k^{(s)}\|\leq\|a^{(r)}-a^{(s)}\|\). Write its limit as \(a_k\in A\). Given \(\varepsilon>0\), choose \(r_0\) so that \(\|a^{(r)}-a^{(s)}\|<\varepsilon\) for \(r,s\geq r_0\). On any finite block, let \(s\to\infty\). The block of \(a-a^{(r)}\) then has finite-column norm at most \(\varepsilon\).

Fix \(r\geq r_0\). Its own tails have norm less than \(\varepsilon\) once the initial index is large. The triangle inequality for finite columns therefore bounds every sufficiently late finite block of \(a\) by \(2\varepsilon\). Its square-sum partial sums are Cauchy, so \(a\in H_A\). Passing to the limit over initial blocks now gives \(\|a-a^{(r)}\|\leq\varepsilon\), proving completeness. Finally, truncation converges because its error norm squared is exactly the norm of a square-sum tail. ∎

**Example 4.2 (Bounded partial sums are insufficient).** Let \(A=c_0(\mathbb N)\), and let \(p_k\) be the sequence that is \(1\) at \(k\) and zero elsewhere. Put \(a_k=p_k\). Then \(\sum_{k=1}^n a_k^*a_k=\sum_{k=1}^n p_k\) has norm \(1\) for every \(n\), but any two distinct partial sums differ by an element of norm \(1\). Thus \((a_k)\notin H_A\). Its pointwise square sum is the constant sequence \(1\), outside \(c_0\).

Even square summability of the coordinate norms is stronger than necessary. For \(a_k=k^{-1/2}p_k\), square-sum tails have norm \(1/(n+1)\) after index \(n\), so this sequence belongs to \(H_{c_0}\). Nevertheless \(\sum_k\|a_k\|^2=\sum_k1/k\) diverges.

### Sections of a Hermitian bundle

Let \(X\) be locally compact Hausdorff, and let \(V\to X\) be a locally trivial finite-dimensional complex vector bundle with a continuous Hermitian metric. Let \(\Gamma_0(V)\) be its continuous sections whose fibre norms vanish at infinity. Give it the action \((sf)(t)=s(t)f(t)\) for \(f\in C_0(X)\), and set

\[
\langle s,u\rangle(t)=\langle s(t),u(t)\rangle_{V_t}.
\tag{4.3}
\]

**Proposition 4.3.** These operations make \(\Gamma_0(V)\) a Hilbert \(C_0(X)\)-module with \(\|s\|=\sup_t\|s(t)\|\).

*Proof.* All module identities and inner product identities hold in each fibre. The right side of (4.3) is continuous. The scalar Cauchy–Schwarz inequality bounds its absolute value by \(\|s(t)\|\|u(t)\|\), so it vanishes at infinity. Positivity and definiteness are pointwise, and the norm formula follows immediately.

A Cauchy sequence of sections converges uniformly in fibre norm to a fibrewise limit \(s\). In a local trivialization near any point, the continuous positive definite metric is uniformly equivalent, on a sufficiently small neighborhood, to a fixed Euclidean norm. Consequently the coordinate functions converge uniformly there. Their limit is continuous: approximate it uniformly within one third of a prescribed error by one continuous coordinate function, and use continuity of that function for the remaining third. Thus \(s\) is a continuous section. Given \(\varepsilon>0\), choose a section in the sequence within \(\varepsilon/2\) of \(s\), then a compact set outside which that section has norm below \(\varepsilon/2\). Outside this set, \(s\) has norm below \(\varepsilon\). It belongs to \(\Gamma_0(V)\), proving completeness. ∎

For the trivial line bundle on \(\mathbb R\), this is simply \(C_0(\mathbb R)\): its inner product is \(\overline s u\), not the integral of that function. This explains why the module norm is a supremum norm rather than an \(L^2\)-norm.

### Averaging with a conditional expectation

Let \(A\subseteq B\) be C*-algebras and let \(\phi:B\to A\) be a conditional expectation. The properties used here are positivity, linearity, \(\phi|_A=\mathrm{id}_A\), and the bimodule identity

\[
\phi(a_1ba_2)=a_1\phi(b)a_2.
\]

On the right \(A\)-module \(B\), define \(\langle b,c\rangle_\phi=\phi(b^*c)\). It is linear in the second variable, and the bimodule identity gives coefficient compatibility. A positive linear map preserves involution: express a self-adjoint element as a difference of two positive elements, then use complex linearity. This proves conjugate symmetry. Positivity is \(\phi(b^*b)\geq0\). The form may be degenerate; Theorem 2.3 removes its null space and completes it. Denote the resulting Hilbert module by \(E_\phi\). If \(\phi\) is faithful, the original form is definite, but completeness in its new norm still needs to be considered.

**Example 4.4 (A four-dimensional scalar module).** Take \(B=M_2(\mathbb C)\), \(A=\mathbb C1\), and \(\phi(b)=\tfrac12\operatorname{Tr}(b)1\). This is a positive projection fixing \(A\), and its bimodule identity is scalar linearity. It preserves the normalized trace. Identifying \(A\) with \(\mathbb C\),

\[
\langle b,c\rangle_\phi=\tfrac12\operatorname{Tr}(b^*c),
\qquad
\|b\|_\phi^2=\tfrac12\sum_{i,j=1}^2|b_{ij}|^2.
\]

This form is definite and complete in four dimensions. The four vectors \(\sqrt2e_{11},\sqrt2e_{12},\sqrt2e_{21},\sqrt2e_{22}\) are an orthonormal basis, since \(\operatorname{Tr}(e_{ij}^*e_{kl})=\delta_{ik}\delta_{jl}\). Thus \(E_\phi\) is a Hilbert space of complex dimension \(4\).

## 5. Which part of the algebra does the module use?

**Definition 5.1.** The *coefficient ideal* of a Hilbert \(A\)-module is

\[
J_E=\overline{\operatorname{span}}\{\langle x,y\rangle:x,y\in E\}.
\]

The module is *full* if \(J_E=A\).

**Proposition 5.2.** The set \(J_E\) is a closed two-sided ideal. If \((e_\lambda)\) is a positive contractive approximate identity of \(A\) or of \(J_E\), then \(xe_\lambda\to x\) for every \(x\in E\).

*Proof.* The linear span of inner products is closed under involution and under right multiplication, since \(\langle x,y\rangle a=\langle x,ya\rangle\). It is closed under left multiplication because \(a\langle x,y\rangle=\langle xa^*,y\rangle\). Its norm closure is therefore a two-sided ideal.

Put \(b=\langle x,x\rangle\). It belongs both to \(A\) and to \(J_E\). In either case the approximate identity properties give

\[
\|x-xe_\lambda\|^2
=\|b-be_\lambda-e_\lambda b+e_\lambda b e_\lambda\|\longrightarrow0.
\tag{5.1}
\]
∎

This proves density of products. The next theorem proves the stronger statement that each vector is a single product.

**Theorem 5.3 (Exact factorization).** Let \(E\) be a Hilbert \(A\)-module, let \(x\in E\), and let \(0<\alpha<1/2\). There is \(y\in E\) such that

\[
x=y\langle x,x\rangle^\alpha.
\tag{5.2}
\]

For nonzero \(x\), one can choose \(\|y\|=\|x\|^{1-2\alpha}\). In particular, if \(\|x\|=1\), then \(\|y\|=1\), hence \(\|y\|\leq1\). Consequently \(E\cdot J_E=E\) and \(E\cdot A=E\), even if the product notation means only single products.

*Proof.* The case \(x=0\) uses \(y=0\). Otherwise put \(b=\langle x,x\rangle\) and \(y_\varepsilon=x(b+\varepsilon1)^{-\alpha}\). For continuous coefficient functions \(f,g\), functional calculus gives

\[
\|x(f(b)-g(b))\|^2
=\|b\,|f(b)-g(b)|^2\|.
\tag{5.3}
\]

On \([0,\|b\|]\), the functions \(t^{1/2}(t+\varepsilon)^{-\alpha}\) converge uniformly to \(t^{1/2-\alpha}\). To see uniformity, on \([0,\delta]\) both are bounded by \(\delta^{1/2-\alpha}\); away from zero ordinary uniform convergence applies. Formula (5.3) therefore makes \(y_\varepsilon\) Cauchy as \(\varepsilon\downarrow0\). Completeness supplies a limit \(y\).

Also \(t^{1/2}((t/(t+\varepsilon))^\alpha-1)\to0\) uniformly: its absolute value is at most \(\sqrt\delta\) near zero, and it converges uniformly away from zero. Using (5.3) again shows \(y_\varepsilon b^\alpha\to x\). The continuity of the action proves (5.2). Finally,

\[
\|y_\varepsilon\|^2
=\|b(b+\varepsilon1)^{-2\alpha}\|
\longrightarrow\|b^{1-2\alpha}\|
=\|x\|^{2-4\alpha}.
\]

Taking square roots gives the claimed norm. Since \(b^\alpha\in C^*(b)\subseteq J_E\), the factor lies in the coefficient ideal, proving both product equalities. ∎

The endpoint \(\alpha=1/2\) cannot be included in general. In \(E=A=C_0((0,1])\), take \(x(t)=t\). Then \(\langle x,x\rangle^{1/2}(t)=t\). A factorization \(x=yt\) would force \(y(t)=1\) for all \(t>0\), which does not vanish at the missing endpoint and is not in \(A\).

The modules \(A_A\), \(A^n\) for \(n\geq1\), and \(H_A\) are full: their inner products include all \(a^*b\), whose span is \(A\). Indeed every positive element is a square \(c^*c\), and every element of a C*-algebra is a linear combination of positive elements. The expectation module is full for the same reason, using vectors from \(A\subseteq B\).

**Example 5.4 (Closed right ideals).** A closed right ideal \(R\subseteq A\) with \(\langle r,s\rangle=r^*s\) is a Hilbert \(A\)-module: it inherits the algebraic axioms and its norm is the original algebra norm, so closedness gives completeness. Its coefficient ideal is

\[
J_R=\overline{\operatorname{span}}R^*R,
\tag{5.4}
\]

which need not be \(R\). For \(A=M_2(\mathbb C)\) and \(R=e_{11}A\), the ideal \(R\) consists of matrices with zero second row. But \(e_{1i}^*e_{1j}=e_{ij}\), so \(J_R=A\). This is a full module although \(R\ne A\).

Closed submodules can also fail to have orthogonal complements. In \(E=C([0,1])\), let \(R=\{f:f(0)=0\}\). If \(g\) is orthogonal to \(R\), testing against \(f(t)=t\) gives \(tg(t)=0\); continuity forces \(g=0\). Thus \(R^\perp=0\), while \(R\) is proper. We cannot decompose \(E=R\oplus R^\perp\).

## 6. Exercises with complete solutions

**Exercise 6.1 (Basic).** Verify all Hilbert module axioms for \(A^n\) with (1.2), including completeness.

*Solution.* Coordinatewise multiplication is a complex bilinear associative right action. Finite summation gives linearity in the second variable, \(\langle x,ya\rangle=\langle x,y\rangle a\), and \(\langle y,x\rangle=\langle x,y\rangle^*\). Each \(x_i^*x_i\) is positive. If their sum is zero, positivity implies \(x_i^*x_i=0\) for every \(i\), hence \(x=0\). Proposition 2.2 gives the norm laws. The estimates (2.4) show that a Cauchy sequence has coordinatewise limits in \(A\) and converges to the resulting column. Thus \(A^n\) is complete.

**Exercise 6.2 (Basic).** Let \(R\) be a closed right ideal of \(A\). Show it is a Hilbert \(A\)-module and compute its coefficient ideal. Specialize to \(R=pA\) for a projection \(p\in A\).

*Solution.* Right multiplication preserves \(R\). The form \(r^*s\) has the axioms checked in Example 1.2; its norm is \(\|r\|\), and \(R\) is complete as a closed subspace of \(A\). Its coefficient ideal is (5.4). The span is two-sided: \((r^*s)a=r^*(sa)\) and \(a(r^*s)=(ra^*)^*s\). For \(R=pA\), products have the form \(a^*pb\), so

\[
J_{pA}=\overline{\operatorname{span}}\{apb:a,b\in A\}.
\]

This is the closed two-sided ideal generated by \(p\). It contains \(p\), by taking \(a=b=p\), and every two-sided ideal containing \(p\) contains all displayed products. The set \(pA\) is closed because it is the range of the bounded idempotent \(a\mapsto pa\). If \(R\) is itself a closed two-sided ideal, then \(J_R=R\): inclusion in \(R\) is immediate, and positive square roots within \(R\) show that its positive elements, hence all of \(R\), lie in the span \(R^*R\).

**Exercise 6.3 (Intermediate).** Prove the matrix positivity test, allowing \(A\) to be nonunital and without assuming in advance that the tested matrix is self-adjoint. Deduce Gram positivity.

*Solution.* If \(T=U^*U\), every tested expression is \(\sum_k(Ua)_k^*(Ua)_k\geq0\). In the other direction, polarization of the four tests on \(a\pm b\) and \(a\pm ib\) gives \(a^*(T-T^*)b=0\). Testing columns with one nonzero coordinate \(e_\lambda\) and using \(e_\lambda d e_\lambda\to d\) shows each entry of \(T-T^*\) is zero.

Let \(P=T_-\) and \(S=P^{1/2}\). Functional calculus gives \(STS=-P^2\). Testing on column \(k\) of \(S\) yields \(-(P^2)_{kk}\geq0\). But \((P^2)_{kk}=\sum_iP_{ik}^*P_{ik}\geq0\). Thus every such sum is zero and every entry of \(P\) is zero. So the negative part vanishes and \(T\geq0\). For a Gram matrix, the tested expression is exactly the inner product of \(\sum_i x_i a_i\) with itself. This proves its positivity by the criterion.

**Exercise 6.4 (Intermediate).** For \(A=c_0\), construct a sequence with bounded square-sum partial sums that does not belong to \(H_A\).

*Solution.* Let \(a_k=p_k\), where \(p_k\) is the \(k\)-th coordinate projection. Then \(a_k^*a_k=p_k\). Each partial sum has norm \(1\); for \(m>n\), the difference of partial sums is \(p_{n+1}+\cdots+p_m\), again of norm \(1\). The partial sums are not norm Cauchy, so their series does not converge in \(c_0\). Definition (4.1) therefore excludes this sequence, even though the partial sums are bounded.

**Exercise 6.5 (Advanced).** Let \(E\) be a Hilbert \(A\)-module and \(J=J_E\). Prove that \(E\) is a full Hilbert \(J\)-module. Explain precisely how its \(A\)-action is recovered from the \(J\)-action. More generally, start with a Hilbert \(J\)-module and a specified inclusion of \(J\) as a closed two-sided ideal of \(A\).

*Solution.* Restrict the action to \(J\) and regard inner products as elements of \(J\). The norm is unchanged because the ideal has its inherited C*-norm, so completeness and definiteness remain true. Its coefficient span is dense in \(J\) by definition, giving fullness. Theorem 5.3 proves \(EJ=E\).

For the more general construction, let \((e_\lambda)\) be a positive contractive approximate identity of \(J\). Formula (5.1), now inside \(J\), proves \(xe_\lambda\to x\). Since \(e_\lambda a\in J\), define

\[
x\cdot a=\lim_\lambda x(e_\lambda a).
\tag{6.1}
\]

This limit exists. For \(b=\langle x,x\rangle\), the square of the norm of a difference is

\[
\|a^*(e_\lambda-e_\mu)b(e_\lambda-e_\mu)a\|
\leq\|a\|^2\|x(e_\lambda-e_\mu)\|^2,
\]

which tends to zero. Each term in (6.1) has norm at most \(\|a\|\|x\|\), so the resulting action has the same bound. Passing inner products to the limit gives

\[
\langle z,x\cdot a\rangle=\langle z,x\rangle a,
\qquad
\langle x\cdot a,z\rangle=a^*\langle x,z\rangle.
\tag{6.2}
\]

For \(j\in J\), the limit is the old \(xj\), since \(e_\lambda j\to j\). Equations (6.2) show that any two choices of approximate identity give the same limit: their difference pairs to zero with every \(z\), hence has zero norm by taking \(z\) to be that difference. They also prove linearity and \((x\cdot a)\cdot a'=x\cdot(aa')\), by pairing both sides with every \(z\). Thus (6.1) is a compatible \(A\)-module structure with the original norm and inner product.

Finally, in any compatible extension, the norm bound and \(xe_\lambda\to x\) force \(xa=\lim_\lambda(xe_\lambda)a\), which is (6.1). The extension is unique and recovers the original action when one was already given. The specified inclusion \(J\subseteq A\) matters: a Hilbert \(J\)-module alone does not determine an ambient algebra. For example, \(E=\mathbb C\) over \(J=\mathbb C\) extends to \(A=\mathbb C\oplus\mathbb C\), with \(J\) embedded as its first summand, by \(x\cdot(a,b)=xa\). The second summand acts as zero.

## What this lesson does not prove

The exact functional-calculus prerequisite is *C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*: Theorem 3.2 gives spectral permanence; Theorems 5.1 and 5.3 and Corollary 5.4 give the isometric continuous calculus in unital and nonunital algebras; Theorem 6.1 gives continuity under uniform limits; Theorem 8.2 and Proposition 8.5 give positivity, roots, powers and order; Theorem 11.4 and Corollary 11.5 give positive contractive approximate identities for every C*-algebra and its ideals. These are written programme proofs. Section 3 here constructs the matrix C*-algebra from the faithful representation theorem and then proves its coefficient-column positivity criterion. The Blackadar references below credit the classical formulations rather than replace these proofs.

The following facts from C*-algebra theory are used without proof. Continuous functional calculus is isometric, has spectral mapping and respects uniform limits [Blackadar 2006, II.2.3.1–II.2.3.2]. Positive elements have square roots and positive real powers; self-adjoint elements have positive and negative parts [Blackadar 2006, II.3.1.2]. The positive cone is closed, contains every \(a^*a\), and is preserved by \(b\mapsto a^*ba\) [Blackadar 2006, II.3.1.3 and II.3.1.5]. For \(b\geq0\), \(0\leq b\leq\|b\|1\) in the unitization [Blackadar 2006, II.3.1.8]. In particular \(0\leq b\leq c\) implies \(\|b\|\leq\|c\|\): compare both with \(\|c\|1\) and use functional calculus for \(b\).

Every C*-algebra, including each closed ideal, has a positive contractive approximate identity; its left, right and two-sided products converge to the element being approximated [Blackadar 2006, II.4.1.2–II.4.1.3]. C*-subalgebras have the inherited norm and positivity [Blackadar 2006, II.2.2.9 and II.3.1.1]. The matrix algebra \(M_n(A)\), with its stated involution, is a C*-algebra [Blackadar 2006, II.6.6.1–II.6.6.3]. Theorem 3.1 proves its positivity criterion rather than assuming that criterion.

## References

- **[Connes 1994]** Alain Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, Appendix A, “C*-modules and Strong Morita Equivalence,” opening definitions and Definition 1. [Author’s electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
- **[Blackadar 2006]** Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006; [revised author’s edition, 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf). Sections II.2.3, II.3.1, II.4.1, II.6.6 and II.7.1.
- **[Blackadar 1998]** Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Mathematical Sciences Research Institute Publications 5, Cambridge University Press, 1998, §13.1. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Emerson 2024]** Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024, §5.4.

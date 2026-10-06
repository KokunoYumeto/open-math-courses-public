# Unbounded decomposable operators and measurable spectral decomposition

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lesson Decomposable operators and the diagonal algebra shows that a bounded operator on a direct integral \(\int^\oplus H(\gamma)\,d\mu(\gamma)\) commutes with every diagonal operator exactly when it acts fibre by fibre. This lesson extends that result to unbounded operators and proves two consequences that reduction theory uses constantly.

The first concerns self-adjoint operators. A self-adjoint operator \(A\) on the direct integral commutes with the diagonal operators, in the sense that every diagonal operator maps the domain of \(A\) into itself and commutes with \(A\) there, exactly when \(A\) is the direct integral of a measurable field of self-adjoint operators \(A(\gamma)\) (Theorem 4.1). Every Borel function of \(A\) is then the direct integral of the same function of the \(A(\gamma)\) (Theorem 3.6). A field of self-adjoint operators is called measurable when its Cayley transforms form a measurable field of unitaries; Proposition 3.2 shows that this is the same as measurability of the resolvents, of all bounded Borel functions, of the unitary groups, or of the graph projections. Section 5 treats closed operators by a \(2\times2\) matrix device that turns a closed operator \(T\) into a self-adjoint operator. This gives Nussbaum's theorem: a closed densely defined operator that commutes with the diagonal operators is the direct integral of a measurable field of closed operators (Theorem 5.5).

The second consequence is the measurable spectral decomposition. Let \(A(\gamma)\) be a measurable field of self-adjoint operators over a \(\sigma\)-finite measure space, whose spectral measures are absolutely continuous with respect to one \(\sigma\)-finite measure \(\kappa\) on \(\mathbb R\), for instance Lebesgue measure. Then each \(H(\gamma)\) is a direct integral \(\int^\oplus_{\mathbb R}K(\gamma,s)\,d\kappa(s)\) on which \(A(\gamma)\) acts as multiplication by \(s\). The identifications are unitaries that depend measurably on \(\gamma\), and the \(K(\gamma,s)\) form one measurable field over the product space (Theorem 8.1). Bounded fields of operators that intertwine two such fields of self-adjoint operators decompose over the product space as well (Theorem 8.3). Two tools are proved on the way: a multiplication form of the spectral theorem for commuting families of projections indexed by a \(\sigma\)-algebra (Theorem 6.1), and a Fubini theorem for direct integrals (Theorem 7.1).

We assume the lessons Measurable fields of Hilbert spaces and their direct integrals and Decomposable operators and the diagonal algebra. We also use the Borel functional calculus of bounded normal operators from The spectral theorem for bounded self-adjoint operators, the spectral theorem for unbounded self-adjoint operators from Spectral calculus with its domains retained, and Stone's theorem from Holomorphy in Banach spaces, Stone's theorem and resolvent convergence. Section 1 lists exactly what is used. The base is an arbitrary \(\sigma\)-finite measure space throughout. No standard Borel structure, no completeness of the measure and no separability of the direct integral are assumed.

Direct integrals of unbounded closed operators were introduced by Nussbaum. By the account in [Dykema–Noles–Sukochev–Zanin 2015, Section 2.8], Theorem 2 of that paper identifies the decomposable closed operators with the closed operators affiliated with the algebra of decomposable operators, and its Theorem 3 says that such an operator is densely defined, or self-adjoint, exactly when almost all of its fibres are. Over a standard Borel base, [Dykema–Noles–Sukochev–Zanin 2015, Propositions 3.4, 3.5 and 4.2] prove that spectral projections and Borel functions of decomposable normal and self-adjoint operators decompose, using Cayley transforms for the self-adjoint ones. [Blackadar, III.1.5.18 and III.1.6] surveys the decomposition of commutative von Neumann algebras and direct integral decompositions.

## 1. Conventions and results used

Throughout, \((\Gamma,\Sigma,\mu)\) is a \(\sigma\)-finite measure space and *measurable* means \(\Sigma\)-measurable. A *null set* is a measurable set of measure zero, and *almost every* \(\gamma\) means every \(\gamma\) outside a null set. \((H(\gamma)),\mathfrak M\) is a measurable field of Hilbert spaces with direct integral
\[
\mathcal H=\int_\Gamma^\oplus H(\gamma)\,d\mu(\gamma),
\]
and we use the notation of the two lessons on direct integrals: \(m_f\) is the diagonal operator of \(f\in L^\infty(\Gamma,\mu)\), \(\int^\oplus x\) is the decomposable operator of a measurable field \(x\) of bounded operators with essentially bounded norm, \(\mathcal A\) is the diagonal algebra and \(\mathcal D\) the decomposable algebra. Hilbert spaces are complex, and inner products are linear in the first variable.

*Operators.* An operator \(T\) in a Hilbert space \(K\) is a linear map from a subspace \(D(T)\) into \(K\). We write \(S\subseteq T\) when \(T\) extends \(S\); an equality of operators includes equality of domains. For a densely defined \(T\), the adjoint \(T^*\) has as domain the set of \(\eta\) for which \(\xi\mapsto\langle T\xi,\eta\rangle\) is bounded on \(D(T)\). \(T\) is *self-adjoint* if it is densely defined and \(T=T^*\), and *closed* if its graph \(G(T)=\{(\xi,T\xi):\xi\in D(T)\}\) is closed in \(K\oplus K\). The *graph projection* \(P_T\) is the orthogonal projection of \(K\oplus K\) onto \(G(T)\). For a unitary \(W:K\to K'\), the operator \(WTW^*\) has domain \(WD(T)\) and sends \(W\xi\) to \(WT\xi\).

### Results used from other lessons

**Fact 1.1** (measurable fields and direct integrals). From Measurable fields of Hilbert spaces and their direct integrals:

- (a) inner products of measurable sections are measurable; \(f\xi\in\mathfrak M\) for measurable \(f\) and \(\xi\in\mathfrak M\); a pointwise weak limit of measurable sections is measurable; measurable sections can be glued along a countable measurable partition (Lemma 2.2);
- (b) a sequence of sections with measurable Gram functions that is total in every fibre generates exactly one measurable field, whose measurable sections are the sections with measurable inner products with every member of the sequence; in any measurable field, a section is measurable as soon as its inner products with the members of one fundamental sequence are measurable (Theorem 3.1(3), (4));
- (c) a field of bounded operators is measurable as soon as it maps the members of one fundamental sequence to measurable sections; adjoints, sums, composites and products with measurable functions of measurable operator fields are measurable; the norm function of a measurable operator field is measurable (Theorem 6.2);
- (d) the pairs of measurable sections form the direct-sum field \((H(\gamma)\oplus K(\gamma))\), and a field of operators on a direct-sum field is measurable exactly when its four blocks are (Proposition 7.1(2), (3));
- (e) a sequence converging in the direct integral has a subsequence converging at almost every point (Theorem 8.2(3));
- (f) for a fundamental sequence \((\xi_n)\), the vectors \(1_{E\cap\{\|\xi_n\|\le m\}}\xi_n\), with \(\mu(E)<\infty\) and \(n,m\ge1\), span a dense subspace of the direct integral (Theorem 9.1(2));
- (g) for a measurable field \(x\) of bounded operators from \((H(\gamma))\) to \((K(\gamma))\) with essentially bounded norm, \(\int^\oplus x\) is bounded with norm \(\operatorname{ess\,sup}_\gamma\|x(\gamma)\|\); the map \(x\mapsto\int^\oplus x\) is linear, multiplicative and compatible with adjoints; two fields define the same operator exactly when they agree almost everywhere; and decomposable operators commute with diagonal operators (Theorem 10.1).

**Fact 1.2** (bounded operators commuting with diagonal operators). From Decomposable operators and the diagonal algebra:

- (a) a bounded operator \(T\) on \(\mathcal H\) commutes with every diagonal operator exactly when it is decomposable, and then \(T=\int^\oplus x\) with \(\|x(\gamma)\|\le\|T\|\) for every \(\gamma\) (Theorem 5.1); in particular \(\mathcal A'=\mathcal D\), and \(\mathcal D\) is closed in norm (Theorem 7.1);
- (b) for two measurable fields over the same base, a bounded operator \(T\) between their direct integrals with \(Tm_f=m_fT\) for every \(f\) is \(\int^\oplus x\) for a measurable field \(x\) with \(\|x(\gamma)\|\le\|T\|\) for every \(\gamma\) (Proposition 6.1); its proof identifies \(\mathcal H\oplus\mathcal K\) with the direct integral of the direct-sum field, the operators \(m_f\oplus m_f\) becoming the diagonal operators;
- (c) if such a \(T\) is unitary, then \(x(\gamma)\) is unitary for almost every \(\gamma\) (Exercise 10.3 and its solution).

**Fact 1.3** (bounded Borel calculus). Let \(n\) be a bounded normal operator with spectrum \(S\). For bounded Borel functions \(g\) on \(S\) there is an operator \(g(n)\), and \(g\mapsto g(n)\) is a unital \(*\)-homomorphism that agrees with the continuous functional calculus on continuous functions, with \(\|g(n)\|\le\sup_S|g|\) and \(\|g(n)\xi\|^2=\int_S|g|^2\,d\mu_\xi\), where \(\mu_\xi(B)=\langle1_B(n)\xi,\xi\rangle\). If \(g_k\to g\) boundedly on \(S\), then \(g_k(n)\to g(n)\) strongly. For a bounded Borel function \(g\) on a set containing \(S\) we write \(g(n)\) for \((g|_S)(n)\). These are Theorems 3.1 and 8.1 of the lesson on the bounded spectral theorem. By Lemma 1.1 there, a set of bounded functions on a metric space that contains the bounded continuous functions and the limits of its boundedly convergent sequences contains every bounded Borel function. The polynomials in \(z\) and \(\bar z\) are uniformly dense in \(C(L)\) for every compact \(L\subseteq\mathbb C\) (The Stone–Weierstrass theorem for functions vanishing at infinity).

**Fact 1.4** (spectral calculus of self-adjoint operators). Let \(A\) be a self-adjoint operator in \(K\).

- (a) There is a unique projection-valued measure \(E_A\) on the Borel sets of \(\mathbb R\) with \(A=\int\lambda\,dE_A(\lambda)\). For \(\xi\in K\), \(\mu_\xi(B)=\langle E_A(B)\xi,\xi\rangle\) is a finite positive measure of total mass \(\|\xi\|^2\).
- (b) For a Borel function \(g:\mathbb R\to\mathbb C\), \(g(A)=\int g\,dE_A\) is closed and densely defined, \(D(g(A))=\{\xi:\int|g|^2\,d\mu_\xi<\infty\}\), \(\|g(A)\xi\|^2=\int|g|^2\,d\mu_\xi\), and \(g(A)^*=\bar g(A)\).
- (c) On bounded Borel functions, \(g\mapsto g(A)\) is a unital \(*\)-homomorphism with \(\|g(A)\|\le\sup|g|\).
- (d) For Borel \(f,g\), \(D(f(A)g(A))=D(g(A))\cap D((fg)(A))\), and \(f(A)g(A)\xi=(fg)(A)\xi\) there. Also \(f(A)+g(A)\subseteq(f+g)(A)\).
- (e) If \(g_k\to g\) pointwise and \(|g_k|\le h\) with \(\int h^2\,d\mu_\xi<\infty\), then \(\xi\in D(g_k(A))\cap D(g(A))\) and \(g_k(A)\xi\to g(A)\xi\). In particular, bounded pointwise convergence \(g_k\to g\) gives \(g_k(A)\to g(A)\) strongly.
- (f) For a real Borel \(\psi\), \(E_{\psi(A)}(B)=E_A(\psi^{-1}(B))\) and \(f(\psi(A))=(f\circ\psi)(A)\) for every Borel \(f\).
- (g) \(A\ge0\) exactly when \(E_A((-\infty,0))=0\), and \(\ker A=E_A(\{0\})K\).

These are proved in Spectral calculus with its domains retained, §§SK-04–SK-09, in the form listed in Holomorphy in Banach spaces, Stone's theorem and resolvent convergence, Fact 1.8.

**Fact 1.5** (Cayley transforms). Let \(A\) be self-adjoint. Then \(A+i\) maps \(D(A)\) bijectively onto \(K\), \((A+i)^{-1}\) is bounded, and
\[
c(A)=(A-i)(A+i)^{-1}=1-2i(A+i)^{-1}
\]
is unitary, with \(1-c(A)\) injective. Put \(a(z)=i(1+z)(1-z)^{-1}\) for \(z\) on the unit circle \(\mathbb T\) with \(z\neq1\), and \(a=0\) elsewhere in the closed unit disc. The spectral measure of \(A\) is the image of that of \(c(A)\) under \(a\): \(E_A(B)=E_{c(A)}(a^{-1}(B))\). Hence \(g(A)=(g\circ a)(c(A))\) for every bounded Borel \(g\) on \(\mathbb R\), and \(c(A)\) is the function \(c(\lambda)=(\lambda-i)(\lambda+i)^{-1}\) of \(A\). Conversely, if \(U\) is unitary and \(1-U\) is injective, then \(a(U)\) is self-adjoint, \((a(U)+i)^{-1}=(1-U)/(2i)\), and \(c(a(U))=U\). So a self-adjoint operator is determined by its Cayley transform. This is Spectral calculus with its domains retained, §SK-06, whose argument for \(a(U)\) uses only that \(U\) is unitary and \(1-U\) injective. The calculus of the normal operator \(c(A)\) there is that of Fact 1.3: both are \(*\)-homomorphisms that extend the continuous calculus and preserve bounded pointwise limits of sequences, and §SK-04 shows that there is only one such map.

**Fact 1.6** (transport). If \(W:K\to K'\) is unitary and \(A\) is self-adjoint in \(K\), then \(WAW^*\) is self-adjoint, \(E_{WAW^*}(B)=WE_A(B)W^*\), and \(Wg(A)W^*=g(WAW^*)\) for every Borel \(g\) (Spectral calculus with its domains retained, §SK-08, (SK.22) and (SK.23)).

**Fact 1.7** (one-parameter groups). From Holomorphy in Banach spaces, Stone's theorem and resolvent convergence: for a self-adjoint \(A\), \(U_t=e^{itA}\) is a strongly continuous unitary group with generator \(iA\) (Theorem 4.2); every strongly continuous unitary group has this form for exactly one self-adjoint \(A\) (Theorem 4.3 there, Stone's theorem); \((1-iA)^{-1}\xi=\int_0^\infty e^{-t}U_t\xi\,dt\) (Proposition 3.6(4) there), where the integral over \([0,n]\) of a continuous vector-valued function is the norm limit of its Riemann sums and the integral over \([0,\infty)\) is the norm limit of the integrals over \([0,n]\) (Fact 1.3 there); and a bounded operator \(b\) commutes with every \(U_t\) exactly when \(bA\subseteq Ab\), that is, \(bD(A)\subseteq D(A)\) and \(Ab\xi=bA\xi\) for \(\xi\in D(A)\) (Proposition 4.6 there).

**Fact 1.8** (measure theory).

- (a) *Monotone class theorem.* A class of sets that contains an algebra of sets \(\mathcal C\) and is closed under unions of increasing sequences and intersections of decreasing sequences contains the \(\sigma\)-algebra generated by \(\mathcal C\). Proved in Decomposable operators and the diagonal algebra, Results used from other lessons.
- (b) *Radon–Nikodym.* If \(\lambda\) is a \(\sigma\)-finite measure and \(\nu\) a finite positive measure on the same \(\sigma\)-algebra, vanishing on the \(\lambda\)-null sets, then \(\nu(C)=\int_C\rho\,d\lambda\) for a measurable \(\rho:Z\to0,\infty)\). For finite \(\lambda\) this is in [Decomposable operators and the diagonal algebra, Results used from other lessons. For \(\sigma\)-finite \(\lambda\), choose sets \(Z_j\) of finite measure partitioning the space, put \(w=\sum_j2^{-j}(1+\lambda(Z_j))^{-1}1_{Z_j}\), apply the finite case to the finite measure \(w\lambda\), which has the same null sets as \(\lambda\), and multiply the density by \(w\).
- (c) *Products.* For \(\sigma\)-finite \((\Gamma,\Sigma,\mu)\) and \((S,\mathcal S,\kappa)\), let \(\Sigma\otimes\mathcal S\) be the \(\sigma\)-algebra generated by the rectangles \(E\times F\). There is a \(\sigma\)-finite measure \(\mu\otimes\kappa\) on \(\Sigma\otimes\mathcal S\) with \((\mu\otimes\kappa)(E\times F)=\mu(E)\kappa(F)\), and for every \(\Sigma\otimes\mathcal S\)-measurable \(F:\Gamma\times S\to[0,\infty]\) the function \(\gamma\mapsto\int_SF(\gamma,s)\,d\kappa(s)\) is \(\Sigma\)-measurable, with \(\int_\Gamma\int_SF(\gamma,s)\,d\kappa(s)\,d\mu(\gamma)=\int F\,d(\mu\otimes\kappa)\). This is [Fremlin, Measure Theory, Volume 2, 251I, 251K and 252P](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm) (free; Volumes 1 and 2 of this text are the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)): \(\mu\otimes\kappa\) is the restriction to \(\Sigma\otimes\mathcal S\) of Fremlin's product measure. A complex function with \(\int_S|F(\gamma,s)|\,d\kappa(s)<\infty\) for every \(\gamma\) is split into the positive and negative parts of its real and imaginary parts, so \(\gamma\mapsto\int_SF(\gamma,s)\,d\kappa(s)\) is measurable as well.
- (d) *Slices.* For a \(\Sigma\otimes\mathcal S\)-measurable function \(F\) and every \(\gamma\), the function \(s\mapsto F(\gamma,s)\) is \(\mathcal S\)-measurable. Indeed the sets \(W\in\Sigma\otimes\mathcal S\) whose slices \(W_\gamma=\{s:(\gamma,s)\in W\}\) belong to \(\mathcal S\) form a \(\sigma\)-algebra containing the rectangles, and \(\{s:F(\gamma,s)\in O\}\) is the slice of \(F^{-1}(O)\).
- (e) *Rectangles.* The finite disjoint unions of rectangles \(E\times F\) form an algebra of sets: an intersection of two rectangles is a rectangle, and the complement of \(E\times F\) is the disjoint union of \((\Gamma\setminus E)\times S\) and \(E\times(S\setminus F)\).

## 2. Bounded Borel functions of decomposable normal operators

**Lemma 2.1.** Let \(x\) be a measurable field of normal operators \(x(\gamma)\in B(H(\gamma))\) with \(\|x(\gamma)\|\le C\) for every \(\gamma\), let \(X=\int^\oplus x\), and let \(L=\{z\in\mathbb C:|z|\le C\}\). Then \(X\) is normal, \(\sigma(X)\subseteq L\), and for every bounded Borel function \(g\) on \(L\) the field \(g(x)=(g(x(\gamma)))_\gamma\) is measurable, \(\|g(x(\gamma))\|\le\sup_L|g|\) for every \(\gamma\), and
\[
g(X)=\int_\Gamma^\oplus g(x(\gamma))\,d\mu(\gamma).
\]

**Proof.** By Fact 1.1(g), \(X\) is bounded and \(X^*X=\int^\oplus x^*x=\int^\oplus xx^*=XX^*\). The spectrum of a bounded operator lies in the disc of radius its norm, so \(\sigma(X)\subseteq L\) and \(\sigma(x(\gamma))\subseteq L\). The bound \(\|g(x(\gamma))\|\le\sup_L|g|\) is Fact 1.3. Let \(\mathcal M\) be the set of bounded Borel functions \(g\) on \(L\) for which \(g(x)\) is a measurable field with \(\int^\oplus g(x)=g(X)\).

*Polynomials.* Let \(p(z,\bar z)\) be a polynomial in \(z\) and \(\bar z\). The calculus of Fact 1.3 is a \(*\)-homomorphism sending \(z\) to the operator, so \(p(x(\gamma))=p(x(\gamma),x(\gamma)^*)\). This is a measurable field by Fact 1.1(c), and Fact 1.1(g) gives \(\int^\oplus p(x,x^*)=p(X,X^*)=p(X)\). So \(p\in\mathcal M\).

*Continuous functions.* Let \(g\in C(L)\), and choose polynomials \(p_k\) with \(\sup_L|p_k-g|\to0\) (Fact 1.3). For every \(\gamma\), \(\|p_k(x(\gamma))-g(x(\gamma))\|\le\sup_L|p_k-g|\). So for \(\xi\in\mathfrak M\) the section \(g(x)\xi\) is the pointwise limit of the measurable sections \(p_k(x)\xi\), hence measurable (Fact 1.1(a)). By the norm formula, \(\|\int^\oplus p_k(x)-\int^\oplus g(x)\|\le\sup_L|p_k-g|\), and also \(\|p_k(X)-g(X)\|\le\sup_L|p_k-g|\). Hence \(\int^\oplus g(x)=\lim_kp_k(X)=g(X)\).

*Bounded limits.* Let \(g_k\in\mathcal M\) converge pointwise on \(L\) to \(g\), with \(|g_k|\le M\). For every \(\gamma\), \(g_k(x(\gamma))\to g(x(\gamma))\) strongly (Fact 1.3). So for \(\xi\in\mathfrak M\), \(g(x)\xi\) is the pointwise limit of \(g_k(x)\xi\) and is measurable. For \(\xi\) in the direct integral,
\[
\Big\|\int^\oplus g_k(x)\,\xi-\int^\oplus g(x)\,\xi\Big\|^2=\int_\Gamma\|(g_k(x(\gamma))-g(x(\gamma)))\xi(\gamma)\|^2\,d\mu(\gamma)\longrightarrow0
\]
by dominated convergence: the integrand tends to \(0\) at every point and is at most \(4M^2\|\xi(\gamma)\|^2\). Also \(g_k(X)\to g(X)\) strongly (Fact 1.3). Since \(\int^\oplus g_k(x)=g_k(X)\), we get \(\int^\oplus g(x)=g(X)\), and \(g\in\mathcal M\).

By Fact 1.3 (Lemma 1.1 of the bounded spectral theorem, applied to the compact metric space \(L\)), \(\mathcal M\) contains every bounded Borel function on \(L\). \(\square\)

**Corollary 2.2.** In the situation of Lemma 2.1:

1. \(E_X(B)=\int^\oplus E_{x(\gamma)}(B)\,d\mu(\gamma)\) for every Borel set \(B\subseteq\mathbb C\), where \(E_n(B)=1_B(n)\);
2. \(X\) is injective if and only if \(x(\gamma)\) is injective for almost every \(\gamma\);
3. \(X\) is unitary if and only if \(x(\gamma)\) is unitary for almost every \(\gamma\).

**Proof.** (1) is Lemma 2.1 for \(g=1_{B\cap L}\). (2) For a bounded normal operator \(n\), Fact 1.3 gives \(\|n\xi\|^2=\int|z|^2\,d\mu_\xi(z)\). So \(n\xi=0\) exactly when \(\mu_\xi\) is carried by \(\{0\}\), that is, when \(E_n(\{0\})\xi=\xi\); hence \(\ker n=E_n(\{0\})K\). So \(X\) is injective exactly when \(E_X(\{0\})=0\). By (1) and the uniqueness in Fact 1.1(g), this holds exactly when \(E_{x(\gamma)}(\{0\})=0\) for almost every \(\gamma\), that is, when almost every \(x(\gamma)\) is injective. (3) \(X^*X=\int^\oplus x^*x\) and \(XX^*=\int^\oplus xx^*\) equal \(1=\int^\oplus1\) exactly when \(x^*x=1\) and \(xx^*=1\) almost everywhere, by the uniqueness in Fact 1.1(g). \(\square\)

## 3. Measurable fields of self-adjoint operators

**Definition 3.1.** A field \((A(\gamma))\) of self-adjoint operators \(A(\gamma)\) in \(H(\gamma)\) is *measurable* if the Cayley transforms \(c(A(\gamma))=(A(\gamma)-i)(A(\gamma)+i)^{-1}\) form a measurable field of bounded operators.

**Proposition 3.2.** For a field \((A(\gamma))\) of self-adjoint operators the following are equivalent.

- (a) \((A(\gamma))\) is measurable.
- (b) The resolvents \((A(\gamma)+i)^{-1}\) form a measurable field.
- (c) For every bounded Borel function \(g:\mathbb R\to\mathbb C\), the operators \(g(A(\gamma))\) form a measurable field.
- (d) For every rational \(t\), the unitaries \(e^{itA(\gamma)}\) form a measurable field.
- (e) The graph projections \(P_{A(\gamma)}\) form a measurable field of operators on the direct-sum field \((H(\gamma)\oplus H(\gamma))\).

If every \(A(\gamma)\) is bounded, they are also equivalent to: (f) \((A(\gamma))\) is a measurable field of bounded operators.

The proof uses the following description of graph projections.

**Lemma 3.3** (graph projections of Borel functions). Let \(A\) be self-adjoint in \(K\) and \(g:\mathbb R\to\mathbb C\) a Borel function. Put
\[
f_1=\frac1{1+|g|^2},\qquad f_2=\frac g{1+|g|^2},\qquad f_3=\frac{|g|^2}{1+|g|^2}.
\]
Then the graph projection of \(g(A)\) is
\[
P_{g(A)}=\begin{pmatrix}f_1(A)&\bar f_2(A)\\ f_2(A)&f_3(A)\end{pmatrix}.
\]
In particular \(P_A\) has the blocks \(h_1(A)\), \(h_2(A)\), \(h_2(A)\) and \(1-h_1(A)\), where \(h_1(\lambda)=(1+\lambda^2)^{-1}\) and \(h_2(\lambda)=\lambda(1+\lambda^2)^{-1}\).

**Proof.** Let \(Q\) be the displayed matrix. The functions \(f_1,f_2,f_3\) are bounded, \(f_1\) and \(f_3\) are real, and \(f_1+f_3=1\), \(gf_1=f_2\), \(\bar f_2g=f_3\), \(|f_2|^2=f_1f_3\). By Fact 1.4(c), \(Q\) is self-adjoint, and multiplying out with these identities gives \(Q^2=Q\): the corners are \(f_1^2+|f_2|^2=f_1(f_1+f_3)=f_1\) and \(|f_2|^2+f_3^2=f_3\), and the off-diagonal entries are \(\bar f_2(f_1+f_3)=\bar f_2\) and \(f_2(f_1+f_3)=f_2\). So \(Q\) is a projection.

Its range lies in the graph. Let \((\xi,\eta)\in K\oplus K\) and \(u=f_1(A)\xi+\bar f_2(A)\eta\). Since \(gf_1=f_2\) and \(g\bar f_2=f_3\) are bounded, Fact 1.4(d) gives \(u\in D(g(A))\) and \(g(A)u=f_2(A)\xi+f_3(A)\eta\), which is the second coordinate of \(Q(\xi,\eta)\).

The graph lies in the range. Let \(u\in D(g(A))\). By Fact 1.4(d), applied to the bounded function \(\bar f_2g=f_3\) and to \(f_3g\), whose modulus is at most \(|g|\), and by the sum rule there,
\[
Q(u,g(A)u)=\big((f_1+f_3)(A)u,\ (f_2+f_3g)(A)u\big)=(u,g(A)u),
\]
because \(f_2+f_3g=g(f_1+f_3)=g\). So the range of \(Q\) is the graph of \(g(A)\). For \(g(\lambda)=\lambda\) we get \(f_1=h_1\), \(f_2=h_2\) and \(f_3=1-h_1\). \(\square\)

**Proof of Proposition 3.2.** Write \(U(\gamma)=c(A(\gamma))\) and \(R(\gamma)=(A(\gamma)+i)^{-1}\).

(a)\(\Leftrightarrow\)(b): \(U=1-2iR\) and \(R=(1-U)/(2i)\) (Fact 1.5), and Fact 1.1(c) applies.

(a)\(\Rightarrow\)(c): By Fact 1.5, \(g(A(\gamma))=(g\circ a)(U(\gamma))\), where \(g\circ a\) is a bounded Borel function on the closed unit disc. The \(U(\gamma)\) are normal with norm \(1\), so Lemma 2.1 shows that \((g\circ a)(U)\) is a measurable field.

(c)\(\Rightarrow\)(d): take \(g(\lambda)=e^{it\lambda}\).

(d)\(\Rightarrow\)(b): By Fact 1.7, \(1-iA(\gamma)=-i(A(\gamma)+i)\) has the inverse \(v\mapsto\int_0^\infty e^{-t}e^{itA(\gamma)}v\,dt\), so
\[
R(\gamma)v=-i\int_0^\infty e^{-t}e^{itA(\gamma)}v\,dt .
\]
Let \(\xi\in\mathfrak M\). For each \(\gamma\), the integral of \(t\mapsto e^{-t}e^{itA(\gamma)}\xi(\gamma)\) over \([0,n]\) is the norm limit, as \(k\to\infty\), of the Riemann sums \(\sum_{j<nk}k^{-1}e^{-j/k}e^{i(j/k)A(\gamma)}\xi(\gamma)\), and these sums are measurable sections by (d). Letting \(n\to\infty\), \(R\xi\) is a pointwise limit of measurable sections, hence measurable (Fact 1.1(a)). So \(R\) is a measurable field.

(c)\(\Rightarrow\)(e): By Lemma 3.3 the blocks of \(P_{A(\gamma)}\) are \(h_1(A(\gamma))\), \(h_2(A(\gamma))\), \(h_2(A(\gamma))\) and \(1-h_1(A(\gamma))\). They are measurable by (c), and Fact 1.1(d) applies.

(e)\(\Rightarrow\)(b): Since \((\lambda+i)^{-1}=h_2(\lambda)-ih_1(\lambda)\), Lemma 3.3 gives \(R=(P_A)_{21}-i(P_A)_{11}\), a measurable field by Fact 1.1(d).

(f): Suppose the \(A(\gamma)\) are bounded. If (c) holds and \(\xi\in\mathfrak M\), let \(g_n(\lambda)=\lambda\) for \(|\lambda|\le n\) and \(g_n(\lambda)=0\) otherwise. For \(n\ge\|A(\gamma)\|\), \(g_n(A(\gamma))=A(\gamma)\), because \(E_{A(\gamma)}\) is carried by \([-\|A(\gamma)\|,\|A(\gamma)\|]\). So \(A\xi=\lim_ng_n(A)\xi\) pointwise is measurable. Conversely, if (f) holds, the sets \(\Gamma_k=\{\gamma:k-1\le\|A(\gamma)\|<k\}\) are measurable (Fact 1.1(c)). On \([-k,k]\) choose polynomials \(p_{k,j}\) converging uniformly to \(\lambda\mapsto(\lambda+i)^{-1}\) (Fact 1.3). For \(\gamma\in\Gamma_k\), \(p_{k,j}(A(\gamma))\to R(\gamma)\) in norm, so \(R\xi=\sum_k1_{\Gamma_k}\lim_jp_{k,j}(A)\xi\) is measurable, by Fact 1.1(a), and (b) holds. \(\square\)

**Lemma 3.4.** Let \((A(\gamma))\) be a measurable field of self-adjoint operators, \(g:\mathbb R\to\mathbb C\) a Borel function and \(\xi\in\mathfrak M\). The set \(D_g(\xi)=\{\gamma:\xi(\gamma)\in D(g(A(\gamma)))\}\) is measurable, and the section equal to \(g(A(\gamma))\xi(\gamma)\) on \(D_g(\xi)\) and to \(0\) elsewhere is measurable.

**Proof.** Let \(g_n=g1_{\{|g|\le n\}}\), a bounded Borel function. By Proposition 3.2(c), \(g_n(A)\xi\) is a measurable section. By Fact 1.4(b) and monotone convergence, \(\|g_n(A(\gamma))\xi(\gamma)\|^2=\int_{\{|g|\le n\}}|g|^2\,d\mu_{\xi(\gamma)}\) increases to \(\int|g|^2\,d\mu_{\xi(\gamma)}\), which is finite exactly when \(\xi(\gamma)\in D(g(A(\gamma)))\). So \(D_g(\xi)=\{\gamma:\sup_n\|g_n(A(\gamma))\xi(\gamma)\|<\infty\}\) is measurable. On \(D_g(\xi)\), \(g_n(A(\gamma))\xi(\gamma)\to g(A(\gamma))\xi(\gamma)\) by Fact 1.4(e) with \(h=|g|\). So the section in question is the pointwise limit of the measurable sections \(1_{D_g(\xi)}g_n(A)\xi\) (Fact 1.1(a)). \(\square\)

**Definition 3.5** (direct integral of a field of self-adjoint operators). Let \((A(\gamma))\) be a measurable field of self-adjoint operators and \(g:\mathbb R\to\mathbb C\) a Borel function. The operator \(\int^\oplus g(A(\gamma))\,d\mu(\gamma)\) in \(\mathcal H\) has as domain the set of \(\xi\in\mathcal H\) such that \(\xi(\gamma)\in D(g(A(\gamma)))\) for almost every \(\gamma\) and \(\int_\Gamma\|g(A(\gamma))\xi(\gamma)\|^2\,d\mu(\gamma)<\infty\), and it sends \(\xi\) to the class of the section \(\gamma\mapsto g(A(\gamma))\xi(\gamma)\). By Lemma 3.4, applied to a representative, this section is measurable after it is set equal to \(0\) on the null set where it is undefined. Changing \(\xi\) on a null set changes it only on a null set. For \(g(\lambda)=\lambda\) we write \(\int^\oplus A(\gamma)\,d\mu(\gamma)\).

If the \(A(\gamma)\) are bounded with essentially bounded norm, this is the decomposable operator of Fact 1.1(g), by Proposition 3.2(f).

**Theorem 3.6** (direct integrals of fields of self-adjoint operators). Let \((A(\gamma))\) be a measurable field of self-adjoint operators and \(\tilde A=\int^\oplus A(\gamma)\,d\mu(\gamma)\).

1. \(\tilde A\) is self-adjoint, and \(c(\tilde A)=\int^\oplus c(A(\gamma))\,d\mu(\gamma)\).
2. For every bounded Borel \(g:\mathbb R\to\mathbb C\), \(g(\tilde A)=\int^\oplus g(A(\gamma))\,d\mu(\gamma)\). In particular \(E_{\tilde A}(B)=\int^\oplus E_{A(\gamma)}(B)\,d\mu(\gamma)\) for every Borel \(B\subseteq\mathbb R\), and \(e^{it\tilde A}=\int^\oplus e^{itA(\gamma)}\,d\mu(\gamma)\).
3. For \(\xi\in\mathcal H\), the spectral measure of \(\xi\) for \(\tilde A\) is \(\mu_\xi(B)=\int_\Gamma\mu_{\xi(\gamma)}(B)\,d\mu(\gamma)\), where \(\mu_{\xi(\gamma)}\) is the spectral measure of \(\xi(\gamma)\) for \(A(\gamma)\). For every Borel \(h:\mathbb R\to[0,\infty]\), the function \(\gamma\mapsto\int h\,d\mu_{\xi(\gamma)}\) is measurable and \(\int h\,d\mu_\xi=\int_\Gamma\int h\,d\mu_{\xi(\gamma)}\,d\mu(\gamma)\).
4. For every Borel \(g:\mathbb R\to\mathbb C\), \(g(\tilde A)=\int^\oplus g(A(\gamma))\,d\mu(\gamma)\), with equality of domains.
5. For every Borel \(B\), \(E_{\tilde A}(B)=0\) exactly when \(E_{A(\gamma)}(B)=0\) for almost every \(\gamma\). In particular \(\tilde A\ge0\) exactly when \(A(\gamma)\ge0\) for almost every \(\gamma\), and \(\tilde A\) is injective exactly when almost every \(A(\gamma)\) is.
6. (*Uniqueness*) If \((A'(\gamma))\) is a measurable field of self-adjoint operators with \(\int^\oplus A'(\gamma)\,d\mu(\gamma)=\tilde A\), then \(A'(\gamma)=A(\gamma)\) for almost every \(\gamma\).

**Proof.** (1) Let \(U(\gamma)=c(A(\gamma))\), a measurable field of unitaries, and \(V=\int^\oplus U\), a unitary by Corollary 2.2(3). Each \(1-U(\gamma)\) is injective (Fact 1.5), so \(1-V=\int^\oplus(1-U)\) is injective by Corollary 2.2(2), applied to the normal field \(1-U\). By Fact 1.5, \(B=a(V)\) is self-adjoint with \((B+i)^{-1}=(1-V)/(2i)\). So \(D(B)=(1-V)\mathcal H\), and for \(\eta\in\mathcal H\) the vector \(\zeta=(1-V)\eta/(2i)\) satisfies \(B\zeta=\eta-i\zeta=(1+V)\eta/2\). In the same way, \(D(A(\gamma))=(1-U(\gamma))H(\gamma)\), and \(A(\gamma)\) sends \((1-U(\gamma))v/(2i)\) to \((1+U(\gamma))v/2\). We show \(B=\tilde A\).

Let \(\zeta=(1-V)\eta/(2i)\in D(B)\), with \(\eta\) represented by a square-integrable section. Then \(\zeta(\gamma)=(1-U(\gamma))\eta(\gamma)/(2i)\in D(A(\gamma))\) for every \(\gamma\), and \(A(\gamma)\zeta(\gamma)=(1+U(\gamma))\eta(\gamma)/2\) has norm at most \(\|\eta(\gamma)\|\). So \(\zeta\in D(\tilde A)\) and \(\tilde A\zeta=(1+V)\eta/2=B\zeta\). Conversely, let \(\xi\in D(\tilde A)\), and put \(\eta=\tilde A\xi+i\xi\). Then \(\eta(\gamma)=(A(\gamma)+i)\xi(\gamma)\) for almost every \(\gamma\), so \(\xi(\gamma)=(1-U(\gamma))\eta(\gamma)/(2i)\) almost everywhere, that is, \(\xi=(1-V)\eta/(2i)\in D(B)\). Hence \(D(\tilde A)=D(B)\), the two operators agree, and \(\tilde A=a(V)\) is self-adjoint with \(c(\tilde A)=V\).

(2) By Fact 1.5, \(g(\tilde A)=(g\circ a)(V)\) and \(g(A(\gamma))=(g\circ a)(U(\gamma))\). Lemma 2.1, for the field \(U\), gives \((g\circ a)(V)=\int^\oplus(g\circ a)(U(\gamma))\,d\mu(\gamma)\).

(3) By (2), \(\mu_\xi(B)=\langle E_{\tilde A}(B)\xi,\xi\rangle=\int_\Gamma\langle E_{A(\gamma)}(B)\xi(\gamma),\xi(\gamma)\rangle\,d\mu(\gamma)\), and the integrand \(\mu_{\xi(\gamma)}(B)\) is measurable in \(\gamma\), as an inner product of measurable sections. By linearity the formula holds for nonnegative simple \(h\). For a general Borel \(h\ge0\), choose simple \(h_k\uparrow h\). For each \(\gamma\), \(\int h_k\,d\mu_{\xi(\gamma)}\uparrow\int h\,d\mu_{\xi(\gamma)}\) by monotone convergence, so the limit function is measurable, and monotone convergence on \(\Gamma\) and for \(\mu_\xi\) gives the formula.

(4) Let \(G=\int^\oplus g(A(\gamma))\,d\mu(\gamma)\). By Fact 1.4(b) and (3) with \(h=|g|^2\), \(\xi\in D(g(\tilde A))\) exactly when \(\int_\Gamma\big(\int|g|^2\,d\mu_{\xi(\gamma)}\big)\,d\mu(\gamma)<\infty\). Since \(\int|g|^2\,d\mu_{\xi(\gamma)}\) is \(\|g(A(\gamma))\xi(\gamma)\|^2\) when \(\xi(\gamma)\in D(g(A(\gamma)))\) and \(\infty\) otherwise, this is the condition \(\xi\in D(G)\). Now let \(\xi\in D(G)\) and \(g_k=g1_{\{|g|\le k\}}\). By Fact 1.4(e) with \(h=|g|\), \(g_k(\tilde A)\xi\to g(\tilde A)\xi\). By (2), \(g_k(\tilde A)\xi\) is represented by \(\gamma\mapsto g_k(A(\gamma))\xi(\gamma)\), and these sections converge to \(g(A(\gamma))\xi(\gamma)\) at almost every point, by Fact 1.4(e) in each fibre. By Fact 1.1(e), a subsequence converges almost everywhere to a representative of \(g(\tilde A)\xi\). So \(g(\tilde A)\xi=G\xi\).

(5) By (2) and the uniqueness in Fact 1.1(g), \(E_{\tilde A}(B)=0\) exactly when \(E_{A(\gamma)}(B)=0\) almost everywhere. Apply this to \(B=(-\infty,0)\) and \(B=\{0\}\), using Fact 1.4(g).

(6) By (1), \(\int^\oplus c(A'(\gamma))=c(\tilde A)=\int^\oplus c(A(\gamma))\), so \(c(A'(\gamma))=c(A(\gamma))\) almost everywhere (Fact 1.1(g)), and then \(A'(\gamma)=A(\gamma)\), because a self-adjoint operator is determined by its Cayley transform (Fact 1.5). \(\square\)

## 4. Self-adjoint operators commuting with the diagonal algebra

**Theorem 4.1.** Let \(A\) be a self-adjoint operator in \(\mathcal H\). The following are equivalent.

1. \(A\) commutes with every diagonal operator: \(m_fA\subseteq Am_f\) for every \(f\in L^\infty(\Gamma,\mu)\), that is, \(m_fD(A)\subseteq D(A)\) and \(Am_f\xi=m_fA\xi\) for \(\xi\in D(A)\).
2. \(e^{itA}\) is decomposable for every \(t\in\mathbb R\).
3. Every spectral projection \(E_A(B)\) is decomposable.
4. The Cayley transform \(c(A)\) is decomposable.
5. \(A=\int^\oplus A(\gamma)\,d\mu(\gamma)\) for a measurable field of self-adjoint operators.

The field in (5) is unique up to a null set, and Theorem 3.6 applies to it.

**Proof.** (1)\(\Rightarrow\)(2): For every \(f\), (1) says \(m_fA\subseteq Am_f\). By Fact 1.7, \(m_f\) commutes with every \(e^{itA}\). So \(e^{itA}\in\mathcal A'=\mathcal D\) (Fact 1.2(a)).

(2)\(\Rightarrow\)(3): Let \(u=m_f\) with \(|f|=1\), a unitary diagonal operator. By (2) and Fact 1.1(g), \(u\) and \(u^*\) commute with every \(e^{itA}\), so \(uA\subseteq Au\) and \(u^*A\subseteq Au^*\) (Fact 1.7). Then \(uD(A)\subseteq D(A)\) and \(D(A)=uu^*D(A)\subseteq uD(A)\), so \(uD(A)=D(A)\) and \(uAu^*=A\). By Fact 1.6, \(E_A(B)=E_{uAu^*}(B)=uE_A(B)u^*\): every spectral projection commutes with every unitary diagonal operator. Every diagonal operator is a linear combination of unitary ones: for real \(f\) with \(|f|\le1\), \(f=(w+\bar w)/2\) with \(w=f+i(1-f^2)^{1/2}\) and \(|w|=1\), and a general \(f\) is a combination of two such functions. So \(E_A(B)\in\mathcal A'=\mathcal D\).

(3)\(\Rightarrow\)(4): By Fact 1.5, \(c(A)\) is the bounded Borel function \(c(\lambda)=(\lambda-i)(\lambda+i)^{-1}\) of \(A\). Approximating \(c\) uniformly by simple functions, Fact 1.4(c) makes \(c(A)\) a norm limit of linear combinations of spectral projections of \(A\). These are decomposable by (3), and \(\mathcal D\) is closed in norm (Fact 1.2(a)).

(4)\(\Rightarrow\)(5): By Fact 1.2(a), \(c(A)=\int^\oplus u\) for a measurable field \(u\) with \(\|u(\gamma)\|\le1\). Since \(c(A)\) is unitary, \(u(\gamma)\) is unitary outside a null set \(N_1\), by the uniqueness in Fact 1.1(g); \(N_1\) is the set where \(\|u^*u-1\|+\|uu^*-1\|>0\), which is measurable by Fact 1.1(c). Replace \(u(\gamma)\) by \(-1\) on \(N_1\). This gives a measurable field of unitaries, still with \(\int^\oplus u=c(A)\). By Fact 1.5, \(1-c(A)\) is injective, so by Corollary 2.2(2) the set \(N_2\) where \(1-u(\gamma)\) is not injective is null. It is measurable: \(N_2=\{\gamma:\|E_{u(\gamma)}(\{1\})\|>0\}\), and \(E_u(\{1\})\) is a measurable field by Lemma 2.1. Replace \(u(\gamma)\) by \(-1\) on \(N_2\) as well. Now every \(u(\gamma)\) is unitary with \(1-u(\gamma)\) injective, so by Fact 1.5, \(A(\gamma)=a(u(\gamma))\) is self-adjoint with \(c(A(\gamma))=u(\gamma)\). The field \((A(\gamma))\) is measurable by Definition 3.1, and Theorem 3.6(1) gives \(c\big(\int^\oplus A(\gamma)\,d\mu\big)=\int^\oplus u=c(A)\). A self-adjoint operator is determined by its Cayley transform (Fact 1.5), so \(\int^\oplus A(\gamma)\,d\mu=A\).

(5)\(\Rightarrow\)(1): Let \(\xi\in D(A)\) and \(f\in L^\infty(\Gamma,\mu)\), with a bounded representative. Then \(f(\gamma)\xi(\gamma)\in D(A(\gamma))\) whenever \(\xi(\gamma)\in D(A(\gamma))\), and \(A(\gamma)f(\gamma)\xi(\gamma)=f(\gamma)A(\gamma)\xi(\gamma)\) is square integrable. So \(m_f\xi\in D(A)\) and \(Am_f\xi=m_fA\xi\) (Definition 3.5).

Uniqueness is Theorem 3.6(6). \(\square\)

In the terminology of Spectral calculus with its domains retained, §SK-08, condition (1) says that \(A\) is *affiliated* with the decomposable algebra \(\mathcal D\), whose commutant is the diagonal algebra \(\mathcal A\). The proof of (2)\(\Rightarrow\)(3) does not use the bicommutant theorem.

In reduction theory a positive self-adjoint operator is often known only through its unitary group, which lives on the closure of its range. The next corollary is the form used there.

**Corollary 4.2** (positive operators and their supports). Let \(S\) be a positive self-adjoint operator in \(\mathcal H\). Let \(e=1-E_S(\{0\})\) be its support, the projection onto \((\ker S)^\perp\), and let \(S^{it}\) be the bounded Borel function \(\lambda\mapsto\lambda^{it}1_{(0,\infty)}(\lambda)\) of \(S\), so that \(S^{it}\) vanishes on \(\ker S\) and is a strongly continuous unitary group on \(e\mathcal H\). The following are equivalent.

1. \(S\) commutes with every diagonal operator.
2. \(e\) and every \(S^{it}\), \(t\in\mathbb R\), are decomposable.
3. \(S=\int^\oplus S(\gamma)\,d\mu(\gamma)\) for a measurable field of positive self-adjoint operators.

In this case \(e=\int^\oplus e(\gamma)\,d\mu(\gamma)\), where \(e(\gamma)\) is the support of \(S(\gamma)\), and \(S^{it}=\int^\oplus S(\gamma)^{it}\,d\mu(\gamma)\).

**Proof.** (1)\(\Rightarrow\)(3): Theorem 4.1 gives a measurable field with \(S=\int^\oplus S(\gamma)\). By Theorem 3.6(5), the set \(N=\{\gamma:E_{S(\gamma)}((-\infty,0))\neq0\}\) is null; it is measurable by Proposition 3.2(c) and Fact 1.1(c). Replacing \(S(\gamma)\) by \(0\) on \(N\) does not change the direct integral.

(3)\(\Rightarrow\)(2) and the last sentence: Theorem 3.6(2) for the bounded Borel functions \(1_{(0,\infty)}\) and \(\lambda^{it}1_{(0,\infty)}(\lambda)\).

(2)\(\Rightarrow\)(1): Let \(\ell(\lambda)=\log\lambda\) for \(\lambda>0\) and \(\ell(\lambda)=0\) for \(\lambda\le0\), and \(L=\ell(S)\), a self-adjoint operator (Fact 1.4(b)). Since \(E_S((-\infty,0))=0\), Fact 1.4(f) gives
\[
e^{itL}=(e^{it\ell})(S)=S^{it}+E_S(\{0\})=S^{it}+1-e ,
\]
which is decomposable by (2). By Theorem 4.1, every \(E_L(C)\) is decomposable. For a Borel set \(B\subseteq(0,\infty)\), \(1_B=(1_{\log B}\circ\ell)\,1_{(0,\infty)}\), because \(\ell\) is injective on \((0,\infty)\); so Fact 1.4(f) and (c) give \(E_S(B)=E_L(\log B)\,e\), a product of decomposable operators. Also \(E_S(\{0\})=1-e\) and \(E_S((-\infty,0))=0\). Hence every \(E_S(B)\) is decomposable, and Theorem 4.1, (3)\(\Rightarrow\)(1), applies. \(\square\)

## 5. Closed operators

A closed operator is reduced to a self-adjoint one by a \(2\times2\) matrix. Let \(\Theta=1\oplus(-1)\) on \(K\oplus K\).

**Lemma 5.1.** Let \(K\) be a Hilbert space.

1. If \(T\) is a closed densely defined operator in \(K\), then \(T^*\) is densely defined and \(T^{**}=T\), and
\[
\check T=\begin{pmatrix}0&T^*\\ T&0\end{pmatrix},\qquad D(\check T)=D(T)\oplus D(T^*),
\]
is self-adjoint, with \(\Theta D(\check T)=D(\check T)\) and \(\Theta\check T\Theta=-\check T\).
2. Conversely, every self-adjoint operator \(\check S\) in \(K\oplus K\) with \(\Theta D(\check S)=D(\check S)\) and \(\Theta\check S\Theta=-\check S\) equals \(\check T\) for exactly one closed densely defined \(T\).
3. \(\check T\check T=(\lambda^2)(\check T)=T^*T\oplus TT^*\), with domain \(D(T^*T)\oplus D(TT^*)\). Hence \(T^*T\) and \(TT^*\) are positive self-adjoint operators, \(R=(1+T^*T)^{-1}\) and \(\tilde R=(1+TT^*)^{-1}\) are bounded, and with \(h_1,h_2\) as in Lemma 3.3,
\[
h_1(\check T)=R\oplus\tilde R,\qquad h_2(\check T)=\begin{pmatrix}0&T^*\tilde R\\ TR&0\end{pmatrix},\qquad(TR)^*=T^*\tilde R .
\]
4. The graph projection of \(T\) is
\[
P_T=\begin{pmatrix}R&(TR)^*\\ TR&1-\tilde R\end{pmatrix}.
\]

**Proof.** (1) Let \(J(\xi,\eta)=(\eta,-\xi)\), a unitary of \(K\oplus K\) with \(J^2=-1\). A pair \((u,v)\) is orthogonal to \(JG(T)=\{(T\xi,-\xi)\}\) exactly when \(\langle T\xi,u\rangle=\langle\xi,v\rangle\) for all \(\xi\in D(T)\), that is, when \((u,v)\in G(T^*)\). So \(G(T^*)=(JG(T))^\perp\). If \(w\perp D(T^*)\), then \((w,0)\perp G(T^*)\), so \((w,0)\) lies in the closure of \(JG(T)\), which is \(JG(T)\) because \(T\) is closed: \((w,0)=(T\xi,-\xi)\) for some \(\xi\), so \(\xi=0\) and \(w=0\). Thus \(T^*\) is densely defined, and \(G(T^{**})=(JG(T^*))^\perp=\big(J(JG(T))^\perp\big)^\perp=\big((-G(T))^\perp\big)^\perp=G(T)\), since \(J\) is unitary.

Next we compute the adjoint of a block operator \(\check S=\begin{pmatrix}0&S\\ T&0\end{pmatrix}\) on \(D(T)\oplus D(S)\), where \(T\) and \(S\) are densely defined. For \((u,v)\in K\oplus K\), \(\langle\check S(\xi,\eta),(u,v)\rangle=\langle S\eta,u\rangle+\langle T\xi,v\rangle\). This is bounded in \((\xi,\eta)\) exactly when both terms are bounded separately (take \(\eta=0\), then \(\xi=0\)), that is, when \(u\in D(S^*)\) and \(v\in D(T^*)\). So
\[
\check S^*=\begin{pmatrix}0&T^*\\ S^*&0\end{pmatrix}\quad\text{on }D(S^*)\oplus D(T^*).
\tag{5.1}
\]
For \(S=T^*\) this gives \(\check T^*=\check T\), since \(T^{**}=T\). Finally \(\Theta\check T\Theta(\xi,\eta)=\Theta\check T(\xi,-\eta)=(-T^*\eta,-T\xi)\).

(2) Let \(D_1=\{\xi:(\xi,0)\in D(\check S)\}\) and \(D_2=\{\eta:(0,\eta)\in D(\check S)\}\). If \((\xi,\eta)\in D(\check S)\), then so is \(\Theta(\xi,\eta)=(\xi,-\eta)\), hence \((\xi,0)\) and \((0,\eta)\); so \(D(\check S)=D_1\oplus D_2\), and \(D_1,D_2\) are dense. For \(\xi\in D_1\), write \(\check S(\xi,0)=(p,q)\). Since \(\Theta(\xi,0)=(\xi,0)\), the relation \(\Theta\check S\Theta=-\check S\) gives \((p,-q)=(-p,-q)\), so \(p=0\), and \(\check S(\xi,0)=(0,T\xi)\) for a linear map \(T\) on \(D_1\). In the same way \(\check S(0,\eta)=(S\eta,0)\). So \(\check S=\begin{pmatrix}0&S\\ T&0\end{pmatrix}\), and (5.1) with \(\check S^*=\check S\) gives \(D(S^*)=D(T)\), \(S^*=T\) and \(T^*=S\). So \(T=S^*\) is closed and densely defined and \(\check S=\check T\). The operator \(T\) is determined by \(\check S\), since \(T\xi\) is the second coordinate of \(\check S(\xi,0)\).

(3) A pair \((\xi,\eta)\in D(\check T)\) has \(\check T(\xi,\eta)=(T^*\eta,T\xi)\in D(\check T)\) exactly when \(T\xi\in D(T^*)\) and \(T^*\eta\in D(T)\). So \(\check T\check T=T^*T\oplus TT^*\) on \(D(T^*T)\oplus D(TT^*)\). By Fact 1.4(d), \(D(\check T\check T)=D(\check T)\cap D((\lambda^2)(\check T))=D((\lambda^2)(\check T))\), since \(\lambda^2\le1+\lambda^4\) and the spectral measures are finite, and \(\check T\check T=(\lambda^2)(\check T)\). This operator is positive and self-adjoint (Fact 1.4(b), (g)). An orthogonal sum \(P\oplus Q\) of densely defined operators has the adjoint \(P^*\oplus Q^*\), by the argument that proved (5.1), so it is self-adjoint exactly when \(P\) and \(Q\) are; hence \(T^*T\) and \(TT^*\) are positive self-adjoint. By Fact 1.4(d), \(h_1(\check T)\) is the bounded inverse of \((1+\lambda^2)(\check T)=1+\check T\check T\), so \(h_1(\check T)=R\oplus\tilde R\). Again by Fact 1.4(d), \(h_2(\check T)=\check T\,h_1(\check T)\) on all of \(K\oplus K\), which is the displayed matrix. Since \(h_2\) is real, \(h_2(\check T)\) is self-adjoint, and comparing its corners gives \((TR)^*=T^*\tilde R\).

(4) Let \((\xi,\eta)\in K\oplus K\) and \(u=R\xi+T^*\tilde R\eta\). Since \(R\xi\in D(T^*T)\) and \(\tilde R\eta\in D(TT^*)\), \(u\in D(T)\) and \(Tu=TR\xi+TT^*\tilde R\eta=TR\xi+(1-\tilde R)\eta\). For \(x\in D(T)\),
\[
\langle\xi-u,x\rangle+\langle\eta-Tu,Tx\rangle=\langle\xi-R\xi,x\rangle-\langle TR\xi,Tx\rangle-\langle T^*\tilde R\eta,x\rangle+\langle\tilde R\eta,Tx\rangle=\langle\xi-(1+T^*T)R\xi,x\rangle=0,
\]
because \(\langle T^*\tilde R\eta,x\rangle=\langle\tilde R\eta,Tx\rangle\) and \(\langle TR\xi,Tx\rangle=\langle T^*TR\xi,x\rangle\). So \((\xi,\eta)-(u,Tu)\perp G(T)\), and \(P_T(\xi,\eta)=(u,Tu)\), which is the displayed matrix applied to \((\xi,\eta)\). \(\square\)

**Definition 5.2** (measurable fields of closed operators). A field \((T(\gamma))\) of closed densely defined operators in \(H(\gamma)\) is *measurable* if the graph projections \(P_{T(\gamma)}\) form a measurable field of operators on the direct-sum field \((H(\gamma)\oplus H(\gamma))\). Its *direct integral* \(\int^\oplus T(\gamma)\,d\mu(\gamma)\) has as domain the set of \(\xi\in\mathcal H\) with \(\xi(\gamma)\in D(T(\gamma))\) for almost every \(\gamma\) and \(\int\|T(\gamma)\xi(\gamma)\|^2\,d\mu<\infty\), and it sends \(\xi\) to the class of \(\gamma\mapsto T(\gamma)\xi(\gamma)\).

This is Nussbaum's definition of measurability, as described in [Dykema–Noles–Sukochev–Zanin 2015, Section 2.7]. By Proposition 3.2(e), a field of self-adjoint operators is measurable in this sense exactly when it is measurable in the sense of Definition 3.1, and the two direct integrals agree. The next lemma shows that the section \(\gamma\mapsto T(\gamma)\xi(\gamma)\) in the definition is measurable.

**Lemma 5.3.** For a field \((T(\gamma))\) of closed densely defined operators, the following are equivalent: (a) \((T(\gamma))\) is measurable; (b) the field \((\check T(\gamma))\) of self-adjoint operators on \((H(\gamma)\oplus H(\gamma))\) is measurable. Then \((T(\gamma)^*)\) is measurable. For \(\xi\in\mathfrak M\), the set of \(\gamma\) with \(\xi(\gamma)\in D(T(\gamma))\) is measurable, and the section equal to \(T(\gamma)\xi(\gamma)\) there and to \(0\) elsewhere is measurable.

**Proof.** By Lemma 5.1(3), (4), the blocks of \(P_{T(\gamma)}\) are blocks of \(h_1(\check T(\gamma))\) and \(h_2(\check T(\gamma))\), or \(1\) minus such a block. So (b) implies (a), by Proposition 3.2(c) and Fact 1.1(d). Conversely, \((\check T+i)^{-1}=h_2(\check T)-ih_1(\check T)\) has the blocks \(-iR\), \((TR)^*\), \(TR\) and \(-i\tilde R\), which are \(-i(P_T)_{11}\), \((P_T)_{12}\), \((P_T)_{21}\) and \(-i(1-(P_T)_{22})\). So (a) implies (b) by Proposition 3.2(b). For the adjoints, let \(F(\xi,\eta)=(\eta,\xi)\). Then \(F\check TF=\begin{pmatrix}0&T\\ T^*&0\end{pmatrix}\), the operator of Lemma 5.1(1) for \(T^*\), and its Cayley transform is \(Fc(\check T)F\) (Fact 1.6), a measurable field. Finally, \((\xi,0)\) is a measurable section of the direct-sum field, \((\xi(\gamma),0)\in D(\check T(\gamma))\) exactly when \(\xi(\gamma)\in D(T(\gamma))\), and \(\check T(\gamma)(\xi(\gamma),0)=(0,T(\gamma)\xi(\gamma))\). Lemma 3.4 and Fact 1.1(d) give the last statement. \(\square\)

**Proposition 5.4.** Let \((T(\gamma))\) be a measurable field of closed densely defined operators and \(T=\int^\oplus T(\gamma)\,d\mu(\gamma)\). Then \(T\) is closed and densely defined, \(T^*=\int^\oplus T(\gamma)^*\,d\mu(\gamma)\), and \(P_T=\int^\oplus P_{T(\gamma)}\,d\mu(\gamma)\). If \((T'(\gamma))\) is a measurable field with \(\int^\oplus T'(\gamma)\,d\mu=T\), then \(T'(\gamma)=T(\gamma)\) for almost every \(\gamma\).

**Proof.** Identify \(\mathcal H\oplus\mathcal H\) with the direct integral of the direct-sum field (Fact 1.2(b)). By Lemma 5.3 and Theorem 3.6(1), \(\check T_\oplus=\int^\oplus\check T(\gamma)\,d\mu\) is self-adjoint. By Definition 3.5, a pair \((\xi,\eta)\) lies in its domain exactly when \(\xi(\gamma)\in D(T(\gamma))\) and \(\eta(\gamma)\in D(T(\gamma)^*)\) almost everywhere and \(\int\big(\|T(\gamma)^*\eta(\gamma)\|^2+\|T(\gamma)\xi(\gamma)\|^2\big)\,d\mu<\infty\). So
\[
\check T_\oplus=\begin{pmatrix}0&T_*\\ T&0\end{pmatrix}\ \text{on }D(T)\oplus D(T_*),\qquad T_*=\int^\oplus T(\gamma)^*\,d\mu(\gamma),
\]
and \(\Theta\check T_\oplus\Theta=-\check T_\oplus\). By Lemma 5.1(2), \(T\) is closed and densely defined and \(T^*=T_*\). The graph projection \(P_T\) is built by Lemma 5.1(4) from the blocks of \(h_1(\check T_\oplus)\) and \(h_2(\check T_\oplus)\), and by Theorem 3.6(2) these are the direct integrals of the corresponding blocks for \(\check T(\gamma)\). So \(P_T=\int^\oplus P_{T(\gamma)}\). If also \(T=\int^\oplus T'(\gamma)\), then \(\int^\oplus P_{T'(\gamma)}=P_T=\int^\oplus P_{T(\gamma)}\), so the graphs, and hence the operators, agree almost everywhere (Fact 1.1(g)). \(\square\)

**Theorem 5.5** (closed operators commuting with the diagonal algebra). Let \(T\) be a closed densely defined operator in \(\mathcal H\). The following are equivalent.

1. \(m_fT\subseteq Tm_f\) for every \(f\in L^\infty(\Gamma,\mu)\).
2. \(P_T\) commutes with every \(m_f\oplus m_f\).
3. \(T=\int^\oplus T(\gamma)\,d\mu(\gamma)\) for a measurable field of closed densely defined operators.

Then the field is unique up to a null set, \(T^*=\int^\oplus T(\gamma)^*\,d\mu\), and \(P_T=\int^\oplus P_{T(\gamma)}\,d\mu\).

*Reference:* due to Nussbaum; see [Dykema–Noles–Sukochev–Zanin 2015, Section 2.8].

**Proof.** (1)\(\Rightarrow\)(2): By (1), \((m_f\oplus m_f)(\xi,T\xi)=(m_f\xi,Tm_f\xi)\in G(T)\) for \(\xi\in D(T)\). So \(G(T)\) is invariant under every \(m_f\oplus m_f\), and also under their adjoints \(m_{\bar f}\oplus m_{\bar f}\); a closed subspace invariant under a set of operators that is closed under adjoints has a projection commuting with that set. (2)\(\Rightarrow\)(1): If \(P_T\) commutes with \(m_f\oplus m_f\), then \(G(T)\) is invariant under it, which is (1).

(1)\(\Rightarrow\)(3): First, (1) holds for \(T^*\). Indeed, let \(\eta\in D(T^*)\) and \(f\in L^\infty\). For \(\xi\in D(T)\),
\[
\langle T\xi,m_{\bar f}\eta\rangle=\langle m_fT\xi,\eta\rangle=\langle Tm_f\xi,\eta\rangle=\langle m_f\xi,T^*\eta\rangle=\langle\xi,m_{\bar f}T^*\eta\rangle,
\]
so \(m_{\bar f}\eta\in D(T^*)\) and \(T^*m_{\bar f}\eta=m_{\bar f}T^*\eta\); replace \(f\) by \(\bar f\). Hence the self-adjoint operator \(\check T\) of Lemma 5.1(1) satisfies \((m_f\oplus m_f)\check T\subseteq\check T(m_f\oplus m_f)\). Under the identification of \(\mathcal H\oplus\mathcal H\) with the direct integral of the direct-sum field, the \(m_f\oplus m_f\) are the diagonal operators (Fact 1.2(b)). By Theorem 4.1, \(\check T=\int^\oplus\check S(\gamma)\,d\mu\) for a measurable field of self-adjoint operators \(\check S(\gamma)\) in \(H(\gamma)\oplus H(\gamma)\).

The field \(-\Theta\check S(\gamma)\Theta\) is also measurable: since \(c(-\lambda)=\overline{c(\lambda)}\) for real \(\lambda\), its Cayley transform is \(\Theta c(\check S(\gamma))^*\Theta\) (Fact 1.6). By Definition 3.5 its direct integral is \(-\Theta\check T\Theta=\check T\). By Theorem 3.6(6), \(-\Theta\check S(\gamma)\Theta=\check S(\gamma)\) outside a null set \(N\), namely the measurable set where \(\|c(\check S(\gamma))-\Theta c(\check S(\gamma))^*\Theta\|>0\). Put \(\check S(\gamma)=0\) for \(\gamma\in N\); this does not change the direct integral. Now Lemma 5.1(2) gives, for every \(\gamma\), a unique closed densely defined \(T(\gamma)\) with \(\check S(\gamma)=\check T(\gamma)\), and \((T(\gamma))\) is measurable by Lemma 5.3. By Proposition 5.4, \(\int^\oplus\check T(\gamma)\,d\mu\) has the lower-left corner \(\int^\oplus T(\gamma)\,d\mu\), while \(\check T\) has the lower-left corner \(T\). Since the two operators are equal, \(T=\int^\oplus T(\gamma)\,d\mu\).

(3)\(\Rightarrow\)(1): For \(\xi\in D(T)\) and bounded \(f\), \(f(\gamma)\xi(\gamma)\in D(T(\gamma))\) almost everywhere and \(T(\gamma)f(\gamma)\xi(\gamma)=f(\gamma)T(\gamma)\xi(\gamma)\) is square integrable, so \(m_f\xi\in D(T)\) and \(Tm_f\xi=m_fT\xi\).

The remaining statements are Proposition 5.4. \(\square\)

**Remark 5.6** (weaker notions of measurability). Lemma 5.3 shows that a measurable field of closed operators maps measurable sections lying in the domains to measurable sections. The converse fails: there are fields of closed operators with this property whose graph projections are not measurable [Gesztesy–Gomilko–Sukochev–Tomilov 2012]. So measurability is defined through the graphs, as in Definition 5.2.

## 6. Diagonalizing a countably generated calculus

In this section \((Z,\mathcal Z,\lambda)\) is a \(\sigma\)-finite measure space, and \(B_b(Z)\) is the algebra of bounded \(\mathcal Z\)-measurable complex functions on \(Z\). Let \(\ell^2=\ell^2(\{1,2,\ldots\})\) with its standard basis \((\varepsilon_k)\).

**Theorem 6.1.** Let \(K\) be a Hilbert space and \(\Pi:B_b(Z)\to B(K)\) a map with the following properties.

- (i) \(\Pi\) is linear and multiplicative, \(\Pi(\bar F)=\Pi(F)^*\), and \(\Pi(1)=1\).
- (ii) If \(F_n\to F\) pointwise with \(\sup_n\sup_Z|F_n|<\infty\), then \(\Pi(F_n)\to\Pi(F)\) strongly.
- (iii) \(\Pi(F)=0\) whenever \(F=0\) \(\lambda\)-almost everywhere.
- (iv) There is a sequence \((\eta_k)\) in \(K\) such that the vectors \(\Pi(F)\eta_k\), \(F\in B_b(Z)\), \(k\ge1\), span a dense subspace.

Then there are sets \(Z_k\in\mathcal Z\), \(k\ge1\), and a unitary \(W\) from \(K\) onto the direct integral \(\int^\oplus_ZH(z)\,d\lambda(z)\) of the measurable field
\[
H(z)=\overline{\operatorname{span}}\{\varepsilon_k:z\in Z_k\}\subseteq\ell^2,
\]
whose measurable sections are the sections \(\zeta\) with measurable coordinates \(\langle\zeta,\varepsilon_k\rangle\), such that \(W\Pi(F)W^*=m_F\) for every \(F\in B_b(Z)\).

**Proof.** (a) *Norms.* If \(\sup|F|\le1\), then \(G=(1-|F|^2)^{1/2}\in B_b(Z)\) and \(\Pi(G)^*\Pi(G)=\Pi(G^2)=1-\Pi(F)^*\Pi(F)\), so \(\|\Pi(F)\xi\|^2=\|\xi\|^2-\|\Pi(G)\xi\|^2\le\|\xi\|^2\). Hence \(\|\Pi(F)\|\le\sup|F|\).

(b) *Measures.* For \(C\in\mathcal Z\), \(\Pi(1_C)\) is a self-adjoint idempotent, a projection. For \(\eta\in K\) put \(\nu_\eta(C)=\langle\Pi(1_C)\eta,\eta\rangle=\|\Pi(1_C)\eta\|^2\). If \(C\) is the union of disjoint \(C_j\), then \(\Pi(1_{C_1\cup\dots\cup C_n})=\sum_{j\le n}\Pi(1_{C_j})\to\Pi(1_C)\) strongly by (ii). So \(\nu_\eta\) is a finite positive measure with \(\nu_\eta(Z)=\|\eta\|^2\), and \(\nu_\eta(C)=0\) when \(\lambda(C)=0\), by (iii). By linearity \(\langle\Pi(F)\eta,\eta\rangle=\int F\,d\nu_\eta\) for simple \(F\), and by (a) and uniform approximation by simple functions for every \(F\in B_b(Z)\). In particular \(\|\Pi(F)\eta\|^2=\langle\Pi(|F|^2)\eta,\eta\rangle=\int|F|^2\,d\nu_\eta\).

(c) *Cyclic subspaces.* Let \(K_\eta\) be the closure of \(\{\Pi(F)\eta:F\in B_b(Z)\}\). By (b), \(F\mapsto\Pi(F)\eta\) is isometric for the norm of \(L^2(Z,\nu_\eta)\), so it is well defined on classes. The bounded functions are dense in \(L^2(Z,\nu_\eta)\), because \(G1_{\{|G|\le n\}}\to G\) in \(L^2\) by dominated convergence. So this map extends to a unitary \(U_\eta:L^2(Z,\nu_\eta)\to K_\eta\), and \(U_\eta(FG)=\Pi(F)U_\eta(G)\): for bounded \(G\) this is multiplicativity, and both sides are continuous in \(G\). The subspace \(K_\eta\) is invariant under every \(\Pi(F)\), and so is its orthogonal complement, since \(\Pi(F)^*=\Pi(\bar F)\). So the projection \(q_\eta\) onto \(K_\eta\) commutes with every \(\Pi(F)\).

(d) *Orthogonal decomposition.* Put \(\eta'_1=\eta_1\), \(K_1=K_{\eta'_1}\) with projection \(q_1\), and recursively \(\eta'_k=(1-q_1-\dots-q_{k-1})\eta_k\) and \(K_k=K_{\eta'_k}\) with projection \(q_k\). Suppose \(K_1,\dots,K_{k-1}\) are mutually orthogonal. Then \(Q=q_1+\dots+q_{k-1}\) is a projection commuting with every \(\Pi(F)\), and \(\Pi(F)\eta'_k=(1-Q)\Pi(F)\eta_k\perp K_j\) for \(j<k\); so \(K_k\perp K_j\). Moreover \(\Pi(F)\eta_k=Q\Pi(F)\eta_k+\Pi(F)\eta'_k\in K_1\oplus\dots\oplus K_k\). By (iv), \(K\) is the orthogonal sum of the \(K_k\).

(e) *Densities.* Let \(\nu_k=\nu_{\eta'_k}\). By Fact 1.8(b), \(\nu_k=\rho_k\lambda\) with a measurable \(\rho_k:Z\to[0,\infty)\). Let \(Z_k=\{\rho_k>0\}\). Then \(\nu_k(Z\setminus Z_k)=0\), and \(G\mapsto G\rho_k^{1/2}\) is a unitary from \(L^2(Z,\nu_k)\) onto \(L^2(Z_k,\lambda)\): it is isometric, and \(H\mapsto H\rho_k^{-1/2}\) on \(Z_k\), extended by \(0\), is its inverse. It commutes with multiplication by every \(F\in B_b(Z)\).

(f) *The field.* The sections \(\zeta_k=1_{Z_k}\varepsilon_k\) have the measurable Gram functions \(\langle\zeta_k,\zeta_l\rangle=\delta_{kl}1_{Z_k}\) and are total in every \(H(z)\). By Fact 1.1(b) they generate a measurable field \((H(z))\), whose measurable sections are the \(\zeta\) with measurable \(\langle\zeta,\zeta_k\rangle\). For a section \(\zeta\) of \((H(z))\), \(\langle\zeta(z),\varepsilon_k\rangle=0\) when \(z\notin Z_k\), so \(\langle\zeta,\zeta_k\rangle=\langle\zeta,\varepsilon_k\rangle\), and the measurable sections are as stated. A square-integrable measurable section \(\zeta=\sum_kf_k\varepsilon_k\) has \(\int\|\zeta\|^2\,d\lambda=\sum_k\int_{Z_k}|f_k|^2\,d\lambda\). So \(\zeta\mapsto(f_k)_k\) is an isometry of the direct integral into \(\bigoplus_kL^2(Z_k,\lambda)\). It is onto: given \((f_k)\) in the sum, \(\sum_k|f_k(z)|^2<\infty\) outside a null set, where we put the section equal to \(0\). It carries \(m_F\) to multiplication by \(F\) in every coordinate.

(g) *Conclusion.* Let \(W\) send \(\xi\in K\) to the element of \(\bigoplus_kL^2(Z_k,\lambda)\) whose \(k\)-th coordinate is the image of \(U_{\eta'_k}^{-1}q_k\xi\) under the unitary of (e), followed by the identification of (f). It is unitary by (d), and \(W\Pi(F)=m_FW\) by (c), (e) and (f). \(\square\)

**Remark 6.2.** The dimension of \(H(z)\) is the number of \(k\) with \(z\in Z_k\). Only countably many vectors \(\eta_k\) are needed in (iv), and \(K\) need not be separable: for \(Z=\{0,1\}^I\) with an uncountable \(I\) and the product of the fair-coin measures, \(\Pi(F)=m_F\) on \(L^2(Z,\lambda)\) satisfies (iv) with the single vector \(1\). For a self-adjoint operator \(A\) on a separable space and a sequence \((\xi_k)\) dense in the unit ball, the map \(\Pi(F)=F(A)\) on the Borel sets of \(\mathbb R\), with \(\lambda=\sum_k2^{-k}\mu_{\xi_k}\), satisfies (i)–(iv), by Fact 1.4; Theorem 6.1 is then the spectral theorem in multiplication form, with fibres of varying dimension. Compare [Blackadar, III.1.5.18].

## 7. Iterated direct integrals

**Theorem 7.1** (Fubini for direct integrals). Let \((\Gamma,\Sigma,\mu)\) and \((S,\mathcal S,\kappa)\) be \(\sigma\)-finite measure spaces, and suppose that \(\mathcal S\) is generated by a countable algebra \(\mathcal S_0\). Let \(\lambda=\mu\otimes\kappa\) on \(\Sigma\otimes\mathcal S\) (Fact 1.8(c)). Let \((K(\gamma,s)),\mathfrak N\) be a measurable field over \((\Gamma\times S,\Sigma\otimes\mathcal S,\lambda)\) with a fundamental sequence \((\xi_n)\).

1. For every \(\gamma\), the slices \(s\mapsto\xi_n(\gamma,s)\) generate a measurable field \((K(\gamma,s))_{s\in S}\) over \((S,\mathcal S,\kappa)\), and the slice \(\xi(\gamma,\cdot)\) of every \(\xi\in\mathfrak N\) is a measurable section of it. Let \(K'(\gamma)=\int^\oplus_SK(\gamma,s)\,d\kappa(s)\).
2. The spaces \(K'(\gamma)\) form a measurable field over \((\Gamma,\Sigma,\mu)\) in which \(\gamma\mapsto\xi(\gamma,\cdot)\) is a measurable section for every \(\xi\in\mathfrak N\) with \(\int_S\|\xi(\gamma,s)\|^2\,d\kappa(s)<\infty\) for every \(\gamma\); it is the only measurable field with this property.
3. The map \(\Phi\), \((\Phi\xi)(\gamma)=\xi(\gamma,\cdot)\), is a unitary from \(\int^\oplus_{\Gamma\times S}K\,d\lambda\) onto \(\int^\oplus_\Gamma K'(\gamma)\,d\mu(\gamma)\); here \((\Phi\xi)(\gamma)\) is set to \(0\) on the null set of \(\gamma\) with \(\int_S\|\xi(\gamma,s)\|^2\,d\kappa=\infty\).
4. For every bounded \(\Sigma\otimes\mathcal S\)-measurable \(F\), \(\Phi m_F\Phi^*=\int^\oplus_\Gamma m_{F(\gamma,\cdot)}\,d\mu(\gamma)\), where \(m_{F(\gamma,\cdot)}\) is the diagonal operator of the slice on \(K'(\gamma)\). More generally, let \((\tilde K(\gamma,s))\) be a second measurable field over the product, with \(\tilde K'\) and \(\tilde\Phi\) defined in the same way, and let \(b\) be a measurable field of operators from \((K(\gamma,s))\) to \((\tilde K(\gamma,s))\) with \(\|b(\gamma,s)\|\le C\) for all \((\gamma,s)\). Then each slice \(b(\gamma,\cdot)\) is a measurable field over \(S\), \(\gamma\mapsto\int^\oplus_Sb(\gamma,s)\,d\kappa(s)\) is a measurable field of operators from \((K'(\gamma))\) to \((\tilde K'(\gamma))\) with norms at most \(C\), and
\[
\tilde\Phi\Big(\int^\oplus_{\Gamma\times S}b\,d\lambda\Big)\Phi^*=\int^\oplus_\Gamma\Big(\int^\oplus_Sb(\gamma,s)\,d\kappa(s)\Big)\,d\mu(\gamma).
\]

**Proof.** (1) By Fact 1.8(d), the Gram functions \(s\mapsto\langle\xi_n(\gamma,s),\xi_m(\gamma,s)\rangle\) of the slices are measurable, and the slices are total in every \(K(\gamma,s)\). So Fact 1.1(b) gives the field. For \(\xi\in\mathfrak N\), the inner products \(s\mapsto\langle\xi(\gamma,s),\xi_n(\gamma,s)\rangle\) are slices of measurable functions, so \(\xi(\gamma,\cdot)\) is a measurable section, by the testing criterion of Fact 1.1(b).

(2) Choose \(S_j\in\mathcal S\) increasing to \(S\) with \(\kappa(S_j)<\infty\). For \(n,m,j\ge1\) and \(C\in\mathcal S_0\), define
\[
\sigma(\gamma)(s)=1_{C\cap S_j}(s)\,1_{\{\|\xi_n(\gamma,s)\|\le m\}}\,\xi_n(\gamma,s).
\]
Each \(\sigma(\gamma)\) is a measurable section of the slice field with \(\int_S\|\sigma(\gamma)(s)\|^2\,d\kappa\le m^2\kappa(S_j)\), so \(\sigma(\gamma)\in K'(\gamma)\). There are countably many such \(\sigma\). The inner product of two of them is \(\gamma\mapsto\int_SG(\gamma,s)\,d\kappa(s)\) for a bounded \(\Sigma\otimes\mathcal S\)-measurable \(G\) vanishing off \(\Gamma\times S_j\), so it is measurable by Fact 1.8(c).

The \(\sigma(\gamma)\) are total in \(K'(\gamma)\). Let \(\eta\in K'(\gamma)\) be orthogonal to all of them, fix \(n,m\), and put \(h(s)=1_{\{\|\xi_n(\gamma,s)\|\le m\}}\langle\eta(s),\xi_n(\gamma,s)\rangle\), a measurable function with \(|h(s)|\le m\|\eta(s)\|\), integrable over each \(S_j\). For fixed \(j\), the sets \(C\in\mathcal S\) with \(\int_{C\cap S_j}h\,d\kappa=0\) contain \(\mathcal S_0\) and are closed under increasing unions and decreasing intersections, by dominated convergence. By Fact 1.8(a) they are all of \(\mathcal S\). Taking for \(C\) the sets where the real or imaginary part of \(h\) is positive or negative shows \(h=0\) almost everywhere on every \(S_j\), hence on \(S\). Since every \(s\) lies in \(\{\|\xi_n(\gamma,s)\|\le m\}\) for large \(m\), \(\langle\eta(s),\xi_n(\gamma,s)\rangle=0\) for every \(n\) and almost every \(s\), and the totality of the \(\xi_n(\gamma,s)\) gives \(\eta=0\) in \(K'(\gamma)\). So by Fact 1.1(b) the \(\sigma\) generate exactly one measurable field structure on \((K'(\gamma))\).

Let \(\xi\in\mathfrak N\) with \(\int_S\|\xi(\gamma,s)\|^2\,d\kappa<\infty\) for every \(\gamma\). Its inner product with \(\sigma\) is \(\gamma\mapsto\int_SG(\gamma,s)\,d\kappa(s)\) with \(G=1_{C\cap S_j}1_{\{\|\xi_n\|\le m\}}\langle\xi,\xi_n\rangle\), and \(\int_S|G(\gamma,s)|\,d\kappa\le m\,\kappa(S_j)^{1/2}\big(\int_S\|\xi(\gamma,s)\|^2\,d\kappa\big)^{1/2}<\infty\). So it is measurable by Fact 1.8(c), and \(\gamma\mapsto\xi(\gamma,\cdot)\) is a measurable section by the testing criterion. Each \(\sigma\) is of this form, so any field with the stated property contains the generating sequence \((\sigma)\), and Fact 1.1(b) gives uniqueness.

(3) Let \(\xi\) be a square-integrable measurable section over the product. By Fact 1.8(c), \(N(\xi)=\{\gamma:\int_S\|\xi(\gamma,s)\|^2\,d\kappa=\infty\}\) is measurable and \(\int_\Gamma\int_S\|\xi(\gamma,s)\|^2\,d\kappa\,d\mu=\int\|\xi\|^2\,d\lambda<\infty\); so \(N(\xi)\) is null. The section \(1_{\Gamma\setminus N(\xi)}\xi\) lies in \(\mathfrak N\) and has finite slice norms everywhere, so by (2) \(\Phi\xi\) is a measurable section, and \(\|\Phi\xi\|^2=\|\xi\|^2\). Thus \(\Phi\) is a linear isometry, well defined on classes. Its range is closed. For \(E\in\Sigma\) with \(\mu(E)<\infty\), every \(\sigma\) and every \(k\), the vector \(1_{E\cap\{\|\sigma\|\le k\}}\sigma\) is \(\Phi\) of the square-integrable section \((\gamma,s)\mapsto1_{E\cap\{\|\sigma\|\le k\}}(\gamma)\,\sigma(\gamma)(s)\) over the product. By Fact 1.1(f), applied to the field \((K'(\gamma))\) and its fundamental sequence \((\sigma)\), these vectors span a dense subspace. So \(\Phi\) is onto.

(4) Pointwise, \((\Phi m_F\xi)(\gamma)=F(\gamma,\cdot)\,\xi(\gamma,\cdot)\). The field \(\gamma\mapsto m_{F(\gamma,\cdot)}\) is measurable: it sends \(\sigma(\gamma)\) to the slice of the measurable section \(F\cdot1_{C\cap S_j}1_{\{\|\xi_n\|\le m\}}\xi_n\), which is a measurable section by (2); Fact 1.1(c) applies. For \(b\), the slice \(b(\gamma,\cdot)\) maps the slices \(\xi_n(\gamma,\cdot)\) to the slices of the measurable sections \(b\xi_n\), so it is measurable by Fact 1.1(c) and (1). By Fact 1.1(g), \(b'(\gamma)=\int^\oplus_Sb(\gamma,s)\,d\kappa(s)\) has norm at most \(C\). It sends \(\sigma(\gamma)\) to the slice of \(b\,1_{C\cap S_j}1_{\{\|\xi_n\|\le m\}}\xi_n\), a measurable section by (2) for \(\tilde K\); so \(b'\) is measurable. Finally \(\tilde\Phi(b\xi)(\gamma)=b(\gamma,\cdot)\xi(\gamma,\cdot)=b'(\gamma)(\Phi\xi)(\gamma)\) for almost every \(\gamma\). \(\square\)

## 8. The measurable spectral decomposition

Let \(\kappa\) be a \(\sigma\)-finite measure on the Borel sets \(\mathcal B\) of \(\mathbb R\). For a measurable field \((K(\gamma,s))\) over \(\Gamma\times\mathbb R\) with the measure \(\mu\otimes\kappa\), Theorem 7.1 applies with \(\mathcal S_0\) the countable algebra of finite unions of intervals with rational or infinite end points; we write \(K'(\gamma)=\int^\oplus_{\mathbb R}K(\gamma,s)\,d\kappa(s)\) for the resulting measurable field over \(\Gamma\). On the slice field \((K(\gamma,s))_{s\in\mathbb R}\), the scalar operators \(s\cdot1\) form a measurable field of self-adjoint operators over \((\mathbb R,\kappa)\), with Cayley transforms \(c(s)\cdot1\). Its direct integral \(M_\gamma\) is multiplication by \(s\), with domain \(\{\zeta:\int s^2\|\zeta(s)\|^2\,d\kappa<\infty\}\), and Theorem 3.6(2) gives \(g(M_\gamma)=m_g\) for bounded Borel \(g\).

**Theorem 8.1** (measurable spectral decomposition). Let \((A(\gamma))\) be a measurable field of self-adjoint operators on \((H(\gamma))\), and suppose there is a null set \(N_0\) such that for \(\gamma\notin N_0\), \(E_{A(\gamma)}(D)=0\) for every Borel \(D\) with \(\kappa(D)=0\). Then there are sets \(Z_k\in\Sigma\otimes\mathcal B\), defining the measurable field \(K(\gamma,s)=\overline{\operatorname{span}}\{\varepsilon_k:(\gamma,s)\in Z_k\}\subseteq\ell^2\) over \((\Gamma\times\mathbb R,\mu\otimes\kappa)\) as in Theorem 6.1, and a measurable field \((V(\gamma))\) of operators from \((H(\gamma))\) to \((K'(\gamma))\), such that for almost every \(\gamma\), \(V(\gamma)\) is unitary and
\[
V(\gamma)A(\gamma)V(\gamma)^*=M_\gamma,\qquad V(\gamma)g(A(\gamma))V(\gamma)^*=m_g\ \text{ for every bounded Borel }g .
\]

For Lebesgue measure \(\kappa\) the hypothesis says that the spectral measures of almost all \(A(\gamma)\) are absolutely continuous.

**Lemma 8.2** (the joint calculus). Let \((A(\gamma))\) be a measurable field of self-adjoint operators, and let \(F\) be a bounded \(\Sigma\otimes\mathcal B\)-measurable function on \(\Gamma\times\mathbb R\). Write \(F_\gamma(A(\gamma))\) for the bounded Borel function \(s\mapsto F(\gamma,s)\) of \(A(\gamma)\) (Fact 1.8(d)). Then \((F_\gamma(A(\gamma)))\) is a measurable field with norms at most \(\sup|F|\), and \(\Pi(F)=\int^\oplus F_\gamma(A(\gamma))\,d\mu(\gamma)\) defines a map \(\Pi\) with properties (i) and (ii) of Theorem 6.1. Moreover \(\Pi(f\otimes g)=m_fg(\tilde A)\) for bounded measurable \(f\) on \(\Gamma\) and bounded Borel \(g\) on \(\mathbb R\), where \((f\otimes g)(\gamma,s)=f(\gamma)g(s)\) and \(\tilde A=\int^\oplus A(\gamma)\,d\mu\). Under the hypothesis of Theorem 8.1, \(\Pi\) also has property (iii) for \(\lambda=\mu\otimes\kappa\).

**Proof.** Let \(\mathcal C\) be the set of bounded measurable \(F\) for which the field is measurable. It contains \(f\otimes g\), since \((f\otimes g)_\gamma(A(\gamma))=f(\gamma)g(A(\gamma))\) (Proposition 3.2(c), Fact 1.1(c)). It is a linear space, since the calculus is linear. It is closed under bounded pointwise limits of sequences: if \(F_n\to F\) so, then \((F_n)_\gamma(A(\gamma))\to F_\gamma(A(\gamma))\) strongly for every \(\gamma\) (Fact 1.4(e)), so the sections \(F_\gamma(A(\gamma))\xi(\gamma)\) are pointwise limits of measurable ones. So the sets \(W\in\Sigma\otimes\mathcal B\) with \(1_W\in\mathcal C\) contain the finite disjoint unions of rectangles, an algebra (Fact 1.8(e)), and form a monotone class; by Fact 1.8(a) they are all of \(\Sigma\otimes\mathcal B\). Hence \(\mathcal C\) contains the simple functions, and their uniform limits, which are all bounded measurable functions. The norm bound is Fact 1.4(c). Property (i) holds fibre by fibre (Fact 1.4(c)) and passes to direct integrals (Fact 1.1(g)). For (ii), if \(F_n\to F\) boundedly, then for \(\xi\in\mathcal H\), \(\|\Pi(F_n)\xi-\Pi(F)\xi\|^2=\int\|((F_n)_\gamma-F_\gamma)(A(\gamma))\xi(\gamma)\|^2\,d\mu\to0\) by dominated convergence. The formula for \(\Pi(f\otimes g)\) is Theorem 3.6(2).

For (iii), let \(F=0\) \(\lambda\)-almost everywhere, and let \(W=\{F\neq0\}\), a \(\lambda\)-null set in \(\Sigma\otimes\mathcal B\). By Fact 1.8(c), \(\int_\Gamma\kappa(W_\gamma)\,d\mu(\gamma)=\lambda(W)=0\), so \(\kappa(W_\gamma)=0\) outside a null set \(N\). For \(\gamma\notin N\cup N_0\), \(E_{A(\gamma)}(W_\gamma)=0\), and
\[
F_\gamma(A(\gamma))=(F_\gamma1_{W_\gamma})(A(\gamma))=F_\gamma(A(\gamma))\,E_{A(\gamma)}(W_\gamma)=0 .
\]
So the field vanishes almost everywhere and \(\Pi(F)=0\). \(\square\)

**Proof of Theorem 8.1.** Let \(\lambda=\mu\otimes\kappa\), which is \(\sigma\)-finite, and let \(\Pi\) be as in Lemma 8.2. Property (iv) of Theorem 6.1 holds: let \((\xi_n)\) be a fundamental sequence of \((H(\gamma))\) and \(\Gamma_j\) sets of finite measure increasing to \(\Gamma\), and put \(\eta_{n,m,j}=1_{\Gamma_j\cap\{\|\xi_n\|\le m\}}\xi_n\). For \(\mu(E)<\infty\), \(\Pi(1_E\otimes1)\eta_{n,m,j}=m_{1_E}\eta_{n,m,j}\) tends to \(1_{E\cap\{\|\xi_n\|\le m\}}\xi_n\) as \(j\to\infty\), and these vectors span a dense subspace by Fact 1.1(f). So Theorem 6.1 gives sets \(Z_k\), the field \((K(\gamma,s))\) and a unitary \(W\) from \(\mathcal H\) onto \(\int^\oplus K\,d\lambda\) with \(W\Pi(F)W^*=m_F\). Let \(\Phi\) be the unitary of Theorem 7.1, and \(U=\Phi W:\mathcal H\to\int^\oplus_\Gamma K'(\gamma)\,d\mu\).

For bounded measurable \(f\) on \(\Gamma\), \(Um_f=U\Pi(f\otimes1)=\Phi m_{f\otimes1}W\), and \(\Phi m_{f\otimes1}\Phi^*\) is the diagonal operator of \(f\) on \(\int^\oplus K'\) (Theorem 7.1(4)). So \(U\) intertwines the diagonal operators, and by Fact 1.2(b), (c), \(U=\int^\oplus V\) for a measurable field \(V\) with \(\|V(\gamma)\|\le1\), unitary for almost every \(\gamma\). For bounded Borel \(g\) on \(\mathbb R\), in the same way \(Ug(\tilde A)=U\Pi(1\otimes g)=\big(\int^\oplus_\Gamma m_g\,d\mu\big)U\), where \(m_g\) acts on \(K'(\gamma)\), and \(g(\tilde A)=\int^\oplus g(A(\gamma))\,d\mu\) (Theorem 3.6(2)). By the uniqueness in Fact 1.1(g), \(V(\gamma)g(A(\gamma))=m_gV(\gamma)\) for \(\gamma\) outside a null set \(N_g\).

Let \(N\) be the union of the sets \(N_{1_D}\), \(D\in\mathcal S_0\), and of the null set where \(V(\gamma)\) is not unitary. For \(\gamma\notin N\), the Borel sets \(D\) with \(V(\gamma)E_{A(\gamma)}(D)V(\gamma)^*=m_{1_D}\) contain \(\mathcal S_0\) and are closed under monotone limits of sequences, because both sides converge strongly (Fact 1.4(e) and dominated convergence). By Fact 1.8(a) they are all Borel sets. So the spectral measure of the self-adjoint operator \(V(\gamma)A(\gamma)V(\gamma)^*\), which is \(V(\gamma)E_{A(\gamma)}(\cdot)V(\gamma)^*\) by Fact 1.6, is \(D\mapsto m_{1_D}=E_{M_\gamma}(D)\). By the uniqueness in Fact 1.4(a), \(V(\gamma)A(\gamma)V(\gamma)^*=M_\gamma\), and then \(V(\gamma)g(A(\gamma))V(\gamma)^*=g(M_\gamma)=m_g\) for every bounded Borel \(g\), by Fact 1.6. \(\square\)

**Theorem 8.3** (intertwining fields decompose). Let \((A(\gamma))\) on \((H(\gamma))\) and \((\tilde A(\gamma))\) on \((\tilde H(\gamma))\) be measurable fields of self-adjoint operators over \((\Gamma,\Sigma,\mu)\). Let \((K(\gamma,s))\) and \((\tilde K(\gamma,s))\) be measurable fields over \((\Gamma\times\mathbb R,\mu\otimes\kappa)\), and let \((V(\gamma))\) and \((\tilde V(\gamma))\) be measurable fields of operators from \((H(\gamma))\) to \((K'(\gamma))\) and from \((\tilde H(\gamma))\) to \((\tilde K'(\gamma))\) which, for almost every \(\gamma\), are unitary and carry \(A(\gamma)\) and \(\tilde A(\gamma)\) to multiplication by \(s\). Let \((B(\gamma))\) be a measurable field of bounded operators from \((H(\gamma))\) to \((\tilde H(\gamma))\) such that, for every bounded Borel \(g\), \(B(\gamma)g(A(\gamma))=g(\tilde A(\gamma))B(\gamma)\) for almost every \(\gamma\). Then there is a measurable field \((B'(\gamma,s))\) of operators from \((K(\gamma,s))\) to \((\tilde K(\gamma,s))\) with \(\|B'(\gamma,s)\|\le\|B(\gamma)\|\) for all \((\gamma,s)\), such that for almost every \(\gamma\)
\[
\tilde V(\gamma)B(\gamma)V(\gamma)^*=\int^\oplus_{\mathbb R}B'(\gamma,s)\,d\kappa(s).
\]

**Proof.** The set where \(V(\gamma)\) or \(\tilde V(\gamma)\) is not unitary is measurable (Fact 1.1(c)) and null; replace both by \(0\) there, so that \(\|V(\gamma)\|,\|\tilde V(\gamma)\|\le1\) everywhere. Let \(\beta(\gamma)=\max(1,\|B(\gamma)\|)\), a measurable function, and \(X(\gamma)=\beta(\gamma)^{-1}\tilde V(\gamma)B(\gamma)V(\gamma)^*\), a measurable field from \((K'(\gamma))\) to \((\tilde K'(\gamma))\) with \(\|X(\gamma)\|\le1\) (Fact 1.1(c)). For each bounded Borel \(g\) and almost every \(\gamma\), \(m_g=V(\gamma)g(A(\gamma))V(\gamma)^*\) and \(\tilde m_g=\tilde V(\gamma)g(\tilde A(\gamma))\tilde V(\gamma)^*\), so
\[
X(\gamma)m_g=\beta^{-1}\tilde VBg(A)V^*=\beta^{-1}\tilde Vg(\tilde A)BV^*=\tilde m_gX(\gamma).
\]
Let \(\hat X=\int^\oplus_\Gamma X\,d\mu\) and \(T=\tilde\Phi^*\hat X\Phi\), with \(\Phi,\tilde\Phi\) from Theorem 7.1. For \(F=1_E\otimes g\), Theorem 7.1(4) and the last display give \(Tm_F=\tilde m_FT\). The set of bounded measurable \(F\) with \(Tm_F=\tilde m_FT\) is a linear space closed under bounded pointwise limits of sequences, since \(m_{F_n}\to m_F\) strongly by dominated convergence. As in the proof of Lemma 8.2 it contains every bounded measurable \(F\). So \(T\) intertwines the diagonal operators over \(\Gamma\times\mathbb R\), and Fact 1.2(b) gives \(T=\int^\oplus B''\,d\lambda\) with \(\|B''(\gamma,s)\|\le1\) everywhere. By Theorem 7.1(4), \(\hat X=\tilde\Phi T\Phi^*=\int^\oplus_\Gamma\big(\int^\oplus_{\mathbb R}B''(\gamma,s)\,d\kappa(s)\big)\,d\mu\), and the uniqueness in Fact 1.1(g) gives \(X(\gamma)=\int^\oplus_{\mathbb R}B''(\gamma,s)\,d\kappa(s)\) for almost every \(\gamma\). Put \(B'(\gamma,s)=\beta(\gamma)B''(\gamma,s)\), a measurable field. Then \(\tilde V(\gamma)B(\gamma)V(\gamma)^*=\int^\oplus_{\mathbb R}B'(\gamma,s)\,d\kappa(s)\) for almost every \(\gamma\).

For the norm bound: for almost every \(\gamma\), the norm formula of Fact 1.1(g) over \((\mathbb R,\kappa)\) gives \(\operatorname{ess\,sup}_s\|B'(\gamma,s)\|=\|\tilde V(\gamma)B(\gamma)V(\gamma)^*\|=\|B(\gamma)\|\). So the measurable set \(Y=\{(\gamma,s):\|B'(\gamma,s)\|>\|B(\gamma)\|\}\) has \(\kappa(Y_\gamma)=0\) for almost every \(\gamma\), and \(\lambda(Y)=0\) by Fact 1.8(c). Setting \(B'=0\) on \(Y\) changes, for almost every \(\gamma\), the slice field only on a \(\kappa\)-null set, so the conclusion is unchanged. \(\square\)

With \(\tilde H=H\), \(\tilde A=A\) and \(\tilde V=V\), Theorem 8.3 says that a measurable field of bounded operators commuting with all bounded Borel functions of the \(A(\gamma)\) is, after the identification of Theorem 8.1, a measurable field over \(\Gamma\times\mathbb R\).

## 9. Examples

**Example 9.1** (countable base). Let \(\Gamma\) be countable with all subsets measurable and \(0<\mu(\{\gamma\})<\infty\), as in the countable-base example of the lesson on direct integrals. Every field of self-adjoint operators is measurable, and \(\int^\oplus A(\gamma)\) is the orthogonal sum of the \(A(\gamma)\), with the domain of the vectors \((\xi(\gamma))\) such that \(\xi(\gamma)\in D(A(\gamma))\) and \(\sum_\gamma\mu(\{\gamma\})\|A(\gamma)\xi(\gamma)\|^2<\infty\). Theorem 4.1 says that a self-adjoint operator commuting with the projections onto the summands is such an orthogonal sum. No measure theory is left in the statement.

**Example 9.2** (multiplication operators). Let \(H(\gamma)=\mathbb C\) and \(A(\gamma)=\alpha(\gamma)\) for a real measurable function \(\alpha\). The Cayley transform \(c(\alpha(\gamma))\) is a measurable function, so the field is measurable, and \(\tilde A\) is multiplication by \(\alpha\) on \(L^2(\Gamma,\mu)\) with domain \(\{\xi:\int|\alpha\xi|^2\,d\mu<\infty\}\). Theorem 3.6 gives \(g(\tilde A)=m_{g\circ\alpha}\) for bounded Borel \(g\) and \(E_{\tilde A}(B)=m_{1_{\alpha^{-1}(B)}}\).

**Example 9.3** (multiplicity two). Let \(\Gamma\) be a point, \(H=L^2(\mathbb R)\) with Lebesgue measure, and \(A\) multiplication by \(x^2\). Its spectral measures are absolutely continuous with respect to Lebesgue measure \(\kappa\) on \(\mathbb R\), since \(E_A(D)\) is multiplication by \(1_D(x^2)\) and \(\{x:x^2\in D\}\) is null when \(D\) is. Theorem 8.1 applies. An explicit decomposition is \(K(s)=\mathbb C^2\) for \(s>0\), \(K(s)=0\) for \(s\le0\), and
\[
(Vf)(s)=(2\sqrt s)^{-1/2}\big(f(\sqrt s),f(-\sqrt s)\big)\qquad(s>0).
\]
The substitution \(x=\pm\sqrt s\) shows \(\int_{\mathbb R}|f|^2\,dx=\int_0^\infty\big(|f(\sqrt s)|^2+|f(-\sqrt s)|^2\big)(2\sqrt s)^{-1}\,ds\), so \(V\) is unitary, and it carries multiplication by \(x^2\) to multiplication by \(s\). The fibre dimension \(2\) is the multiplicity of the spectrum.

**Example 9.4** (the hypothesis of Theorem 8.1 cannot be dropped). Let \(\Gamma=\mathbb R\) with Lebesgue measure \(\mu\), \(H(\gamma)=\mathbb C\) and \(A(\gamma)=\gamma\), so that \(E_{A(\gamma)}\) is the point mass at \(\gamma\). Let \(\kappa\) be any \(\sigma\)-finite measure on \(\mathbb R\). It has at most countably many atoms, so for almost every \(\gamma\), \(\kappa(\{\gamma\})=0\) while \(E_{A(\gamma)}(\{\gamma\})=1\), and the hypothesis fails. The conclusion fails as well. If \(V(\gamma)\) were a unitary from \(\mathbb C\) onto \(K'(\gamma)\) carrying \(A(\gamma)\) to \(M_\gamma\), then \(m_{1_{\mathbb R\setminus\{\gamma\}}}=V(\gamma)E_{A(\gamma)}(\mathbb R\setminus\{\gamma\})V(\gamma)^*=0\), while \(m_{1_{\{\gamma\}}}=0\) because \(\kappa(\{\gamma\})=0\). Their sum is the identity of \(K'(\gamma)\), so \(K'(\gamma)=0\), which is impossible for a unitary image of \(\mathbb C\).

## 10. Exercises

**Exercise 10.1** (\(T^*T\), \(|T|\) and kernels). Let \((T(\gamma))\) be a measurable field of closed densely defined operators and \(T=\int^\oplus T(\gamma)\,d\mu\). Show that \(T^*T=\int^\oplus T(\gamma)^*T(\gamma)\,d\mu\) and \(|T|=(T^*T)^{1/2}=\int^\oplus|T(\gamma)|\,d\mu\), and that the projection onto \(\ker T\) is \(\int^\oplus\) of the projections onto \(\ker T(\gamma)\).

*Solution.* By Proposition 5.4, \(\int^\oplus\check T(\gamma)\,d\mu=\check T\). Theorem 3.6(4) for the function \(\lambda^2\), with Lemma 5.1(3), gives
\[
T^*T\oplus TT^*=(\lambda^2)(\check T)=\int^\oplus(\lambda^2)(\check T(\gamma))\,d\mu=\int^\oplus\big(T(\gamma)^*T(\gamma)\oplus T(\gamma)T(\gamma)^*\big)\,d\mu .
\]
The fields \((T(\gamma)^*T(\gamma))\) are measurable: their Cayley transforms are corners of the bounded Borel functions \(c(\lambda^2)\) of the \(\check T(\gamma)\) (Fact 1.4(f), Proposition 3.2(c)). Comparing domains and actions on vectors \((\xi,0)\) in Definition 3.5 gives \(T^*T=\int^\oplus T(\gamma)^*T(\gamma)\). Theorem 3.6(4) for the function \(\lambda\mapsto\max(\lambda,0)^{1/2}\) gives the formula for \(|T|\). If \(T\xi=0\) then \(\xi\in D(T^*T)\) and \(T^*T\xi=0\); conversely \(T^*T\xi=0\) gives \(\|T\xi\|^2=\langle T^*T\xi,\xi\rangle=0\). So \(\ker T=\ker T^*T=E_{T^*T}(\{0\})\mathcal H\) (Fact 1.4(g)), and Theorem 3.6(2) decomposes \(E_{T^*T}(\{0\})\). The same holds in each fibre.

**Exercise 10.2** (decomposable unitary groups). Let \((U_t)_{t\in\mathbb R}\) be a strongly continuous unitary group on \(\mathcal H\) such that every \(U_t\) is decomposable, \(U_t=\int^\oplus u_t\). The fields \(u_t\) are determined only up to null sets that depend on \(t\). Show that there is a measurable field \((A(\gamma))\) of self-adjoint operators such that, for every \(t\), \(u_t(\gamma)=e^{itA(\gamma)}\) for almost every \(\gamma\). So the fibres can be chosen to be genuine strongly continuous unitary groups, all at once.

*Solution.* By Stone's theorem (Fact 1.7), \(U_t=e^{itA}\) for a self-adjoint \(A\). Condition (2) of Theorem 4.1 holds, so \(A=\int^\oplus A(\gamma)\) for a measurable field of self-adjoint operators. By Theorem 3.6(2), \(e^{itA}=\int^\oplus e^{itA(\gamma)}\), and the uniqueness in Fact 1.1(g) gives \(u_t(\gamma)=e^{itA(\gamma)}\) for almost every \(\gamma\). Each \(t\mapsto e^{itA(\gamma)}\) is a strongly continuous unitary group (Fact 1.7).

## Where this leads

- *Reduction theory of weights.* The lesson Weights on random operators and formal dimension of the course *Noncommutative integration* uses Corollary 4.2 to decompose positive operators known through their unitary groups, and Theorems 8.1 and 8.3 to pass from a groupoid \(G\) with a modulus \(\delta\) to the stable kernel \(G\times\mathbb R\) of \(\delta\).
- *Brown measure.* For closed operators affiliated with a tracial von Neumann algebra that decomposes as a direct integral, [Dykema–Noles–Sukochev–Zanin 2015] use these decompositions to show that the Brown measure is the integral of the Brown measures of the fibres.
- *Direct integrals of Hilbert algebras.* Modular operators of direct integrals of left Hilbert algebras are direct integrals of closed operators; see Direct integrals of Hilbert and Tomita algebras in the course *Modular Theory and Weights*.

## References



- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, revised and corrected edition with hyperlinks, free from the author: https://bruceblackadar.com/Mathematics/Cycr.pdf (first published as Encyclopaedia of Mathematical Sciences 122, 2006; the numbering is the same).
- [Dykema–Noles–Sukochev–Zanin 2015] K. Dykema, J. Noles, F. Sukochev and D. Zanin, On reduction theory and Brown measure for closed unbounded operators, free preprint arXiv:1509.03362 (2015), https://arxiv.org/abs/1509.03362; published in *Journal of Functional Analysis* 271 (2016), 3403–3422.
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, Chapter 25, free from the author: https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm.
- [Gesztesy–Gomilko–Sukochev–Tomilov 2012] F. Gesztesy, A. Gomilko, F. Sukochev and Y. Tomilov, On a question of A. E. Nussbaum on measurability of families of closed linear operators in a Hilbert space, free preprint arXiv:1002.2733 (2010), https://arxiv.org/abs/1002.2733; published in *Israel Journal of Mathematics* 188 (2012), 195–219.

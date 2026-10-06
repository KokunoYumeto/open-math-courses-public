# The trace formula for a compact quotient

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A convolution operator can be counted in two ways. Its trace is a sum over irreducible representations, but its kernel is a sum over lattice elements. Evaluating that kernel on the diagonal turns lattice elements into conjugacy classes. We will prove the resulting identity, recover Poisson summation, and compute the trace of a quaternion Hecke operator by counting embeddings of quadratic orders.

The quaternion groups, ideal classes and Brandt conventions come from Lesson 17. The Hilbert-space background is prerequisite D20. Inner products are linear in the first variable. All lattice measures are counting measures. We begin with a second-countable, locally compact Hausdorff unimodular group \(G\), a discrete subgroup \(\Gamma\), and a compact quotient \(X=\Gamma\backslash G\). The test functions for an arbitrary such group will be finite sums of convolutions of compactly supported continuous functions. Section 3 proves the same trace identity directly for the usual smooth Lie and adelic test functions.

## 1. Measures and the automorphic kernel

Fix Haar measure \(dg\) and the quotient measure \(dx\) characterized by
\[
\int_G u(g)\,dg
=\int_X\sum_{\gamma\in\Gamma}u(\gamma x)\,dx
\qquad(u\in C_c(G)).
\tag{1.1}
\]
The quotient-measure theorem is proved in Quotient measures and Weil’s integration formula, Theorem 3.1. For a closed subgroup \(H\), its invariant measure on \(G/H\) exists precisely when \(\Delta_G|_H=\Delta_H\). Its left-coset convention becomes our right-coset convention under \(gH\mapsto Hg^{-1}\); inversion transports left Haar measures to right Haar measures and left invariance to right invariance. All groups to which we apply the formula here are unimodular, so those Haar measures agree. In (1.1), \(H=\Gamma\) has counting measure and both modular functions are one. The same theorem therefore supplies exactly (1.1), with our fixed normalization. Getz–Hahn, Theorem 3.2.2 is an additional reference. Since \(X\) is compact, \(0<\operatorname{vol}(X)<\infty\).

The right regular action and convolution are
\[
\begin{gathered}
R(g)\phi(x)=\phi(xg),\qquad
R(f)\phi(x)=\int_G f(g)\phi(xg)\,dg,\\
(a*b)(g)=\int_G a(h)b(h^{-1}g)\,dh,\qquad
f^*(g)=\overline{f(g^{-1})}.
\end{gathered}
\tag{1.2}
\]
Thus \(R(a*b)=R(a)R(b)\), \(R(f^*)=R(f)^*\), and \(\|R(f)\|\leq\|f\|_1\). Fubini proves the first identity, and invariance of \(dx\) and inversion of \(dg\) prove the second. The action is unitary and strongly continuous: first check continuity on continuous functions on the compact space \(X\), where it is uniform, and then use their density in \(L^2(X)\).

**Theorem 1.1 — the kernel and compactness.** For \(f\in C_c(G)\), the operator \(R(f)\) has continuous kernel
\[
K_f(x,y)=\sum_{\gamma\in\Gamma}f(x^{-1}\gamma y).
\tag{1.3}
\]
It is Hilbert–Schmidt and compact.

**Proof.** The quotient map has local sections: around any point, choose a small relatively compact open set whose distinct left \(\Gamma\)-translates are disjoint. A finite cover of \(X\) by images of these sets gives a compact set \(C\subset G\) with \(G=\Gamma C\). If \(x,y\in C\) and a summand in (1.3) is nonzero, then
\[
\gamma\in\Gamma\cap C\operatorname{supp}(f)C^{-1}.
\tag{1.4}
\]
This is a finite set. Hence the sum is uniformly bounded on representatives in \(C\), and locally it is a finite sum of continuous functions. Changing either representative only permutes its terms, so it descends to a continuous bounded kernel on \(X\times X\).

For a continuous \(\phi\), substitute \(y=xg\) in (1.2), then use (1.1):
\[
\begin{aligned}
R(f)\phi(x)
&=\int_G f(x^{-1}y)\phi(y)\,dy\\
&=\int_X\sum_{\gamma\in\Gamma}
 f(x^{-1}\gamma y)\phi(y)\,dy.
\end{aligned}
\tag{1.5}
\]
The bounded operators extend this equality to \(L^2(X)\). For an orthonormal basis \((e_j)\), Parseval in the second variable gives
\[
\sum_j\|R(f)e_j\|_2^2
=\int_{X\times X}|K_f(x,y)|^2\,dx\,dy<\infty.
\tag{1.6}
\]
This is the Hilbert–Schmidt property. Finite sums of product functions are dense in the product \(L^2\) space. Their kernels have finite-rank operators, and Cauchy–Schwarz gives \(\|T_K\|\leq\|K\|_2\). Thus \(R(f)\) is an operator-norm limit of finite-rank operators. \(\square\)

**Lemma 1.2 — centralizers.** For \(\gamma\in\Gamma\), put
\[
G_\gamma=\{g:g\gamma=\gamma g\},\qquad
\Gamma_\gamma=\Gamma\cap G_\gamma.
\tag{1.7}
\]
Then \(\Gamma_\gamma\backslash G_\gamma\) is compact and \(G_\gamma\) is unimodular.

**Proof.** Write \(h=\delta c\) for \(h\in G_\gamma\), \(\delta\in\Gamma\), \(c\in C\). Then \(\delta^{-1}\gamma\delta=c\gamma c^{-1}\) lies in the finite set \(\Gamma\cap C\gamma C^{-1}\). Choose \(\delta_j\) for each conjugate occurring in this set. Whenever \(\delta^{-1}\gamma\delta=\delta_j^{-1}\gamma\delta_j\), one has \(\delta\delta_j^{-1}\in\Gamma_\gamma\). Therefore the compact sets \(G_\gamma\cap\delta_jC\) map onto the centralizer quotient.

We also verify the fact about unimodularity that this uses. If a locally compact group \(H\) has a discrete subgroup \(\Lambda\) with compact quotient, left Haar measure on small local sections glues to a positive Radon measure on \(\Lambda\backslash H\): transition maps are left translations by locally constant elements of \(\Lambda\), so they preserve that measure. Right translation by \(h\) scales the glued measure by the same constant as it scales left Haar measure on \(H\). The quotient has finite positive total measure, and right translation is a bijection of it. That constant must therefore be one for every \(h\). Thus \(H\) is unimodular. Apply this to \(G_\gamma\). \(\square\)

## 2. Why the representation decomposes discretely

The compactness just proved is stronger than a bound on individual eigenfunctions: it forces the entire regular representation to be a sum of irreducibles. The following argument does not require the convolution operators to commute.

**Theorem 2.1.** There is a countable Hilbert direct sum
\[
L^2(X)=\widehat\bigoplus_\pi m(\pi)\mathcal H_\pi,
\qquad m(\pi)<\infty,
\tag{2.1}
\]
where the \(\pi\) are inequivalent irreducible unitary representations of \(G\).

**Proof.** Choose nonnegative \(h_n\in C_c(G)\) with integral one and support shrinking to the identity. Strong continuity gives \(R(h_n)\to I\) and \(R(h_n)^*\to I\) strongly. Hence
\[
T_n=R(h_n)^*R(h_n)\longrightarrow I
\tag{2.2}
\]
strongly, and each \(T_n\) is positive and compact.

Here is the elementary spectral fact we need. A nonzero positive compact operator \(T\) has a positive eigenvalue with a finite-dimensional eigenspace. Indeed, put \(\lambda=\|T\|\). Cauchy–Schwarz for the positive form \(\langle Tv,w\rangle\) shows
\(\|Tv\|^2\leq\lambda\langle Tv,v\rangle\), and also shows that the supremum of \(\langle Tv,v\rangle\) over unit vectors is \(\lambda\). Choose unit \(v_j\) approaching this supremum. Then
\[
\|(T-\lambda I)v_j\|^2
\leq\lambda\bigl(\lambda-\langle Tv_j,v_j\rangle\bigr)
\longrightarrow0.
\tag{2.3}
\]
Compactness gives a convergent subsequence of \(Tv_j\), so (2.3) gives a unit limit \(v\) with \(Tv=\lambda v\). An infinite-dimensional positive-eigenvalue eigenspace would contain an orthonormal sequence whose images under \(T\) have no convergent subsequence.

Now let \(W\ne0\) be a closed invariant subspace of \(L^2(X)\). Some \(T_n|_W\) is nonzero. Let \(E\subset W\) be a nonzero eigenspace for a positive eigenvalue of this restriction. Among the nonzero spaces \(E\cap W'\), with \(W'\subset W\) closed and invariant, choose one \(M\) of least dimension. Pick \(0\ne v\in M\), and let \(P\) be its closed cyclic invariant subspace. It lies in the \(W'\) that supplied \(M\); minimality implies \(P\cap E=M\).

For a closed invariant \(Q\subset P\), unitarity makes its orthogonal complement in \(P\) invariant. Both projections commute with group operators and hence with \(T_n\). Thus
\[
M=(E\cap Q)\oplus(E\cap(P\ominus Q)).
\tag{2.4}
\]
Every nonzero summand has dimension at least \(\dim M\). Exactly one is nonzero, and it equals \(M\). The cyclic vector \(v\) lies in that summand, so all of \(P\) lies in the corresponding invariant subspace. Hence \(Q=0\) or \(Q=P\). We have found an irreducible subrepresentation in every nonzero invariant closed subspace.

A maximal orthogonal family of irreducible subrepresentations spans the whole space: a nonzero orthogonal complement would supply another. The space \(L^2(X)\) is separable, since \(X\) is compact and second-countable with a Radon measure, so the family is countable. Finally, fix an irreducible constituent \(\pi\). Some \(T_n\) has a positive eigenvalue on it. On every equivalent copy the same operator has that same eigenvalue. Infinitely many equivalent copies would contradict the finite-dimensional eigenspaces of the compact \(T_n\) on \(L^2(X)\). This proves finite multiplicity. \(\square\)

## 3. Trace class and the trace identity

For clarity, an operator is trace class if it can be written
\(Tv=\sum_j\langle v,v_j\rangle u_j\) with \(\sum_j\|u_j\|\|v_j\|<\infty\). On a Hilbert space this is the usual nuclear description of trace class. Its trace is \(\sum_j\langle u_j,v_j\rangle\). Parseval and absolute convergence show that this also equals \(\sum_k\langle Te_k,e_k\rangle\) in any orthonormal basis: the absolute double sum is bounded by \(\sum_j\|u_j\|\|v_j\|\). In particular, the trace is independent of the description and of the basis.

**Lemma 3.1 — a product of kernels.** If \(A,B\) are Hilbert–Schmidt integral operators with kernels \(K_A,K_B\), then \(AB\) is trace class and
\[
\operatorname{tr}(AB)
=\int_{X\times X}K_A(x,y)K_B(y,x)\,dx\,dy.
\tag{3.1}
\]

**Proof.** In an orthonormal basis,
\[
ABv=\sum_k\langle v,B^*e_k\rangle Ae_k,\qquad
\sum_k\|Ae_k\|\|B^*e_k\|
\leq\|A\|_{\rm HS}\|B\|_{\rm HS}.
\tag{3.2}
\]
Thus the operator is trace class. Expanding its trace gives the sum of the products of the matrix entries of \(A\) and \(B\). The product orthonormal basis and Parseval identify this with (3.1); Cauchy–Schwarz bounds the integral of the absolute value by \(\|K_A\|_2\|K_B\|_2\). These bounds justify all limits and rearrangements. \(\square\)

Let
\[
\mathcal A(G)=\left\{\sum_{j=1}^r a_j*b_j:
a_j,b_j\in C_c(G),\ r<\infty\right\}.
\tag{3.3}
\]
For \(f=a*b\), composition of the kernels in Theorem 1.1 gives
\[
K_f(x,z)=\int_XK_a(x,y)K_b(y,z)\,dy.
\tag{3.4}
\]
One can either unfold the two lattice sums using (1.1), or use \(R(a*b)=R(a)R(b)\). In the latter proof the two continuous kernels agree almost everywhere and hence everywhere, since the quotient measure has full support. Lemma 3.1 and (3.4), extended by linearity, give
\[
\operatorname{tr}R(f)=\int_XK_f(x,x)\,dx
\qquad(f\in\mathcal A(G)).
\tag{3.5}
\]

**Lemma — the trace of a smooth kernel.** Let \(M\) be a compact smooth manifold with a positive smooth volume density. A smooth kernel \(K(x,y)\) defines a trace-class operator on \(L^2(M)\), with
\[
\operatorname{tr}T_K=\int_MK(x,x)\,dx.
\]
This holds also for a finite disjoint union of such manifolds.

**Proof.** Choose a finite smooth partition of unity \(\sum_i\alpha_i=1\), with each support inside a precompact coordinate cube \(U_i\) whose closure lies in a larger chart. Write the measure there as \(\rho_i(u)\,du\), with \(\rho_i>0\) on that larger chart. Place the closure of each coordinate cube strictly inside a fundamental cube of a torus. The coordinate expression
\[
H_{ij}(u,v)=
 \alpha_i(x)\alpha_j(y)K(x,y)
 \sqrt{\rho_i(u)\rho_j(v)}
\]
has compact support inside the product of the two cubes; extending it by zero gives a smooth function on the product torus. Let \(e_a,e_b\) be the normalized exponential bases on the two tori. Integration by parts with
\((1-\Delta_u-\Delta_v)^N\) gives its Fourier coefficients the bound
\[
H_{ij}(u,v)=\sum_{a,b}c_{ab}^{ij}e_a(u)\overline{e_b(v)},
\qquad
|c_{ab}^{ij}|
 \le C_N(1+|a|^2+|b|^2)^{-N}.
\tag{3.6}
\]
For \(N>\dim M\), their absolute sum is finite. The Fourier series converges uniformly to \(H_{ij}\): the absolute convergence gives a continuous function with those coefficients, and product Fejér kernels show that a continuous function with all coefficients zero vanishes. Their approximation property follows by multiplying the one-dimensional nonnegative kernels of integral one and using their concentration at zero, as in the Fourier calculation in Lesson 17, Section 4.1.

Push the exponentials back to \(M\) as
\[
u_a^i(x)=1_{U_i}(x)\frac{e_a(u(x))}{\sqrt{\rho_i(u(x))}},
\qquad
v_b^j(y)=1_{U_j}(y)\frac{e_b(v(y))}{\sqrt{\rho_j(v(y))}}.
\]
Their \(L^2\)-norms are bounded independently of \(a,b\); integration cancels the density and leaves a subset of a torus of fixed volume. Dividing the uniform series by the two square roots gives the kernel \(\alpha_i(x)\alpha_j(y)K(x,y)\) as
\[
\sum_{a,b}c_{ab}^{ij}u_a^i(x)\overline{v_b^j(y)}.
\]
Consequently its operator is the nuclear sum
\(\sum_{a,b}c_{ab}^{ij}\langle\,\cdot\,,v_b^j\rangle u_a^i\), with
\(\sum_{a,b}|c_{ab}^{ij}|\|u_a^i\|_2\|v_b^j\|_2<\infty\).
The square roots are bounded below on the chosen chart closures, so the kernel series converges uniformly there and vanishes off the charts. Its diagonal integral equals
\[
\sum_{a,b}c_{ab}^{ij}\langle u_a^i,v_b^j\rangle,
\]
which is precisely its trace. Both the nuclear bound and uniform convergence justify the interchange. Sum over the finitely many pairs of charts. Since \(\sum_{i,j}\alpha_i(x)\alpha_j(y)=1\), this proves the lemma. A finite disjoint union uses the same proof on its finitely many component pairs. \(\square\)

For a Lie group and \(f\in C_c^\infty(G)\), the kernel (1.3) is smooth: on compact local sections the sum has only finitely many terms, and this remains true after any fixed derivative. The quotient is a compact smooth manifold, with its positive smooth Haar density. The lemma therefore proves trace class and (3.5) for every smooth compact Lie test directly.

For a totally disconnected group with a base of compact open subgroups, a compactly supported locally constant \(f\) is bi-invariant under some compact open \(J\). To see it, cover its support by finitely many constancy neighborhoods and take a common subgroup on the left and right. Put \(e_J=1_J/\operatorname{vol}(J)\). Then \(f=e_J*f*e_J\). The image of \(R(f)\) is in the \(J\)-fixed functions. Here \(\Gamma\backslash G/J\) is discrete and compact, hence finite, so the operator has finite rank and \(f=f*e_J\) also belongs to \(\mathcal A(G)\).

Now let \(G=G_\infty\times G_f\), with a Lie factor and a totally disconnected factor as above. Smooth adelic tests are finite sums of \(f_\infty\otimes h_f\). Choose one compact open \(J\subset G_f\) making all these tests bi-\(J\)-invariant, and let \(P_J=R(e_J)\). Then
\[
R(f)=P_JR(f)P_J.
\]
The quotient \(X/J\) is a finite disjoint union of compact smooth manifolds. Indeed the map to \(\Gamma\backslash G_f/J\) has compact source and discrete target, so its image is finite. For a representative \(y_i\in G_f\), the corresponding component is
\[
\Gamma_i\backslash G_\infty,\qquad
\Gamma_i=
\{\gamma_\infty:\gamma\in\Gamma,\
 \gamma_f\in y_iJy_i^{-1}\}.
\]
The group \(\Gamma_i\) is discrete: over a compact real set the corresponding elements of \(\Gamma\) lie in a compact product with \(y_iJy_i^{-1}\), and there are finitely many. The kernel of the real projection is finite by the same argument. The real image acts freely by left translation, so its quotient is a manifold; the finite kernel affects only the constant normalization of its positive Haar density. Compactness follows because each of these finitely many components is closed in \(X/J\).

The bi-\(J\)-invariance makes \(K_f(x,y)\) descend in both variables to \(X/J\), with a smooth kernel on each component pair. Give \(X/J\) the pushforward of \(dx\). Its \(L^2\)-space identifies isometrically with the \(J\)-fixed subspace. The smooth-kernel lemma proves the trace identity on that subspace; the operator is zero on its orthogonal complement. Pushing forward the diagonal integral proves (3.5) on \(X\) itself. Thus all the smooth adelic tests have the required trace-class operator and diagonal trace, with no factorization theorem needed for this proof.

For comparison, the general Dixmier–Malliavin theorem asserts that a smooth compact Lie test itself is a finite sum of smooth compact convolutions; see Getz–Hahn, Theorem 4.2.7. It yields another route through Lemma 3.1. The direct smooth-kernel argument above supplies the complete analytic bridge used here.

Choose Haar measure \(dg_\gamma\) on each \(G_\gamma\), and let the measures on \(\Gamma_\gamma\backslash G_\gamma\) and \(G_\gamma\backslash G\) be the compatible quotient measures. Define
\[
O_\gamma(f)=\int_{G_\gamma\backslash G}
f(x^{-1}\gamma x)\,d\dot x.
\tag{3.7}
\]
Rescaling \(dg_\gamma\) multiplies its lattice-quotient volume and divides its orbital integral by the same constant.

**Theorem 3.2 — the compact-quotient trace formula.** For \(f\in\mathcal A(G)\), and also for all smooth compact Lie and adelic tests in the settings just described,
\[
\boxed{
\sum_\pi m(\pi)\operatorname{tr}\pi(f)
=\sum_{[\gamma]_\Gamma}
\operatorname{vol}(\Gamma_\gamma\backslash G_\gamma)
O_\gamma(f).}
\tag{3.8}
\]
The spectral sum is absolutely convergent. Only finitely many geometric conjugacy classes have nonzero terms, and their orbital integrals converge absolutely.

**Proof of the spectral side.** In the decomposition (2.1), \(R(f)\) acts on every copy of \(\pi\) as \(\pi(f)\). Take an orthonormal basis adapted to the countably many irreducible copies. The trace-class description preceding Lemma 3.1 bounds the sum of the absolute values of all diagonal entries. Each restriction is trace class, and grouping those entries by copies gives the left side of (3.8), absolutely.

**Proof of the geometric side.** From (1.4),
\(\int_X\sum_{\gamma\in\Gamma}|f(x^{-1}\gamma x)|\,dx<\infty\).
Moreover any contributing conjugacy class meets the finite set in (1.4), so only finitely many classes occur. For a representative \(\gamma\), its conjugates are \(\delta^{-1}\gamma\delta\), indexed by \(\Gamma_\gamma\backslash\Gamma\). Regroup and unfold:
\[
\begin{aligned}
\int_X\sum_{\delta\in\Gamma_\gamma\backslash\Gamma}
 f(x^{-1}\delta^{-1}\gamma\delta x)\,dx
&=\int_{\Gamma_\gamma\backslash G}f(x^{-1}\gamma x)\,dx\\
&=\operatorname{vol}(\Gamma_\gamma\backslash G_\gamma)
 \int_{G_\gamma\backslash G}f(x^{-1}\gamma x)\,d\dot x.
\end{aligned}
\tag{3.9}
\]
Lemma 1.2 supplies unimodularity and the finite positive centralizer volume. The quotient-measure formula applies, and the inner integrand is unchanged by left multiplication by \(G_\gamma\). Applying the same argument to \(|f|\) proves absolute convergence. Summing (3.9) and using (3.5) proves (3.8). \(\square\)

If \(\gamma\) is central, \(G_\gamma=G\). With \(dg_\gamma=dg\), the space \(G_\gamma\backslash G\) is one point of mass one, so
\[
O_\gamma(f)=f(\gamma),\qquad
\text{its geometric contribution}=\operatorname{vol}(X)f(\gamma).
\tag{3.10}
\]
The volume belongs to the contribution, not to the normalized orbital integral itself.

**Why continuity alone is insufficient.** There is even a counterexample on the compact circle \(G=\mathbb R/\mathbb Z\), with \(\Gamma=\{0\}\). Define polynomials
\[
P_0=Q_0=1,\qquad
P_{k+1}=P_k+z^{2^k}Q_k,\qquad
Q_{k+1}=P_k-z^{2^k}Q_k.
\tag{3.11}
\]
Their coefficients are \(\pm1\), in the \(2^k\) positions \(0,\ldots,2^k-1\). On \(|z|=1\), induction gives
\(|P_k|^2+|Q_k|^2=2^{k+1}\).
Choose \(N_1=0\) and \(N_{j+1}=N_j+2^{4j}\). The series
\[
g(x)=\sum_{j\geq1}2^{-3j}e^{2\pi iN_jx}
 P_{4j}(e^{2\pi ix})
\tag{3.12}
\]
converges uniformly, since its summand has supremum at most \(\sqrt2\,2^{-j}\). It defines a continuous function. Its disjoint Fourier blocks have absolute coefficient sum \(2^{4j}2^{-3j}=2^j\). Convolution is diagonal in the Fourier basis with these coefficients, up to reversing the frequency sign. Its absolute diagonal sum diverges, so it cannot be trace class. Theorem 1.1 still makes it Hilbert–Schmidt and compact. Smoothness is a sufficient condition for the trace formula; mere continuity does not guarantee it.

## 4. Finite groups and Poisson summation

For a finite group use counting Haar measure. Take \(\Gamma=G\), so \(X\) has one point of mass one and the only representation on it is the trivial one. Formula (3.8) becomes
\[
\sum_{g\in G}f(g)
=\sum_{[\gamma]}
 \sum_{G_\gamma x\in G_\gamma\backslash G}f(x^{-1}\gamma x).
\tag{4.1}
\]
Here Haar measure on \(G_\gamma\) is also counting measure. Then \(\Gamma_\gamma\backslash G_\gamma\) is a point of mass one and \(G_\gamma\backslash G\) has counting measure on its cosets, by (1.1). For \(f\equiv1\),
\[
|G|=\sum_{[\gamma]}[G:G_\gamma].
\tag{4.2}
\]
For \(S_3\), the centralizers of the identity, a transposition and a three-cycle have orders \(6,2,3\), giving \(6=1+3+2\). Alternatively take \(\Gamma=\{1\}\) and \(f=\mathbf1_{\{1\}}\). The regular trace is \(6\). Its two one-dimensional constituents and its two copies of the two-dimensional constituent give \(1+1+2\cdot2=6\).

Now take \(G=\mathbb R\), \(\Gamma=\mathbb Z\), Lebesgue measure, and
\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt.
\tag{4.3}
\]
The quotient has volume one. Its orthonormal Fourier basis is \(e_n(x)=e^{2\pi inx}\), and
\[
R(f)e_n=\widehat f(-n)e_n,\qquad
K_f(x,y)=\sum_{k\in\mathbb Z}f(y-x+k).
\tag{4.4}
\]
Every lattice element is central, so the geometric side is \(\sum_k f(k)\). For \(f\in C_c^\infty(\mathbb R)\), repeated integration by parts gives rapid decay of \(\widehat f(n)\); reindexing the absolutely convergent spectral sum yields
\[
\boxed{\sum_{k\in\mathbb Z}f(k)=\sum_{n\in\mathbb Z}\widehat f(n).}
\tag{4.5}
\]

The formula also holds for every Schwartz function, even though the group-level test is no longer compactly supported. Indeed \(p_f(t)=\sum_k f(t+k)\) and all its derivatives converge uniformly on the circle. Its Fourier coefficients are \(\widehat f(n)\), by absolute convergence and the change of variable \(t+k\). Integration by parts makes their absolute sum finite. The resulting Fourier series equals \(p_f\): the difference has every Fourier coefficient zero and hence is zero in \(L^2\), and both functions are continuous. Evaluating at zero proves (4.5). This simultaneously proves that the periodized convolution has trace class.

For \(f_a(t)=e^{-\pi at^2}\), \(a>0\), its integral is \(a^{-1/2}\): square the integral and use polar coordinates in \(\mathbb R^2\). Differentiating its Fourier transform and integrating \(f_a'=-2\pi atf_a\) by parts gives
\(\widehat f_a'(\xi)=-(2\pi\xi/a)\widehat f_a(\xi)\).
The value at zero determines the solution of this differential equation. Thus
\[
\widehat f_a(\xi)=a^{-1/2}e^{-\pi\xi^2/a},\qquad
\sum_{k\in\mathbb Z}e^{-\pi ak^2}
=a^{-1/2}\sum_{n\in\mathbb Z}e^{-\pi n^2/a}.
\tag{4.6}
\]
The factor \(a^{-1/2}\) records the Fourier and Haar normalizations.

## 5. Quadratic orders inside the quaternion trace

Let \(D=B_{p,\infty}\) be the rational quaternion algebra ramified precisely at a prime \(p\) and at infinity, and let \(\mathcal O\) be a maximal order. Choose right ideal-class representatives \(I_1,\ldots,I_h\), put \(\mathcal O_i=\mathcal O_L(I_i)\), and write
\[
w_i=|\mathcal O_i^\times/\{\pm1\}|,\qquad
\operatorname{mass}(\mathcal O)=\sum_i\frac1{w_i}
=\frac{p-1}{12}.
\tag{5.1}
\]
The final equality is the maximal-order mass formula proved in Lesson 17, Theorem 4.3. We retain the row convention of Lesson 17: \(B(n)_{ij}\) counts subideals of \(I_i\) of relative reduced norm \(n\) in class \(I_j\), and the matrix acts on column functions.

Here the compact trace formula applies to
\[
G=D^\times(\mathbb A)/\mathbb A^\times,\qquad
\Gamma=D^\times(\mathbb Q)/\mathbb Q^\times.
\tag{5.2}
\]
Lesson 17, Theorem 3.2 and the proof of Proposition 3.4, give compactness of the quotient and discreteness of this rational subgroup. Let \(K\) be the image of \(D^\times(\mathbb R)\widehat{\mathcal O}^{\times}\). Its real factor is compact after dividing by the real centre. Normalize \(K\) to have volume one. The double quotient \(\Gamma\backslash G/K\) is the ideal-class set, and the stabilizer of its \(i\)-th component is \(\mathcal O_i^\times/\{\pm1\}\). Consequently that component has volume \(1/w_i\), and \(\operatorname{vol}(\Gamma\backslash G)=\operatorname{mass}(\mathcal O)\).

The test \(f_n\) is the weight-zero Hecke test of relative norm \(n\). At a finite prime \(\ell\), with \(r=v_\ell(n)\), take the right cosets represented by integral elements of reduced norm valuation \(r\), and project them to \(D_\ell^\times/\mathbb Q_\ell^\times\). Their characteristic functions, with compact-subgroup volume one, define its local factor. Cosets of the same norm valuation remain distinct under this projection: a scalar identifying two of them has valuation zero and is already absorbed by the compact subgroup. At a split prime the support includes the elementary-divisor distances \(r,r-2,\ldots\); thus this is the full-norm operator, not only its primitive part. At \(p\) there is one coset. The real factor is the constant function one on the compact projective real group.

This smooth test is bi-invariant under \(K\). Averaging on either side shows that \(R(f_n)\) vanishes on the orthogonal complement of the finite-dimensional class-function space and acts on that space as \(B(n)\). Its full Hilbert-space trace is therefore the ordinary matrix trace. Lesson 17's norm-count identity gives
\[
\operatorname{tr}B(n)
=\sum_i\frac{\#\{\alpha\in\mathcal O_i:
 \operatorname{nrd}(\alpha)=n\}}{2w_i}.
\tag{5.3}
\]
Indeed a diagonal subideal is \(\alpha I_i\) with \(\alpha\in\mathcal O_i\), and its generators form an orbit of size \(|\mathcal O_i^\times|=2w_i\). This is also the diagonal-kernel computation of the geometric trace before regrouping it into rational conjugacy classes.

The projective normalization explains the factor two. A rational projective element that contributes has a lift of norm \(n\), unique up to \(\pm1\). To see existence, the local norm conditions force every prime valuation of its positive rational norm divided by \(n\) to be even; that positive rational number is a rational square. Rescale the lift by its square root. The kernel's projective count is thus half the unprojectivized norm count in (5.3). The identity projective class contributes only when \(n\) is a square, and its contribution is the mass in (5.1).

We now compute the noncentral terms without using Jacquet–Langlands transfer. For a quadratic order \(S\) in an imaginary quadratic field \(K_S\), let
\[
h(S)=|\operatorname{Pic}(S)|,\qquad
w(S)=|S^\times/\{\pm1\}|.
\tag{5.4}
\]
An embedding \(S\hookrightarrow\mathcal O_i\) is **optimal** when its extension to the field satisfies \(K_S\cap\mathcal O_i=S\). Let \(m(S,\mathcal O_i)\) count optimal embeddings modulo conjugation by \(\mathcal O_i^\times\). Embeddings are labelled maps: we do not identify a map with its composition with the quadratic field automorphism.

**Lemma — quadratic fields that embed.** Let \(D/F\) be a quaternion division algebra and \(E/F\) a quadratic field extension. Then \(E\) embeds in \(D\) if and only if \(D\otimes_FE\) is split. Over a nonarchimedean local field every separable quadratic extension embeds. Over a number field a quadratic extension embeds exactly when it is a field at every ramified place of \(D\).

**Proof.** The exact algebraic proof provider is Central simple algebras and the Brauer group, Theorem 4.2. Its finite splitting criterion says that a splitting extension of degree \(s\) embeds in an algebra similar to \(D\) of degree \(s\). Here \(s=\deg D=2\), so that algebra is \(D\) itself: an algebra similar to \(D\) is \(M_r(D)\), of degree \(2r\). Conversely an embedded quadratic field is maximal and splits \(D\), by Theorem 4.1 of that provider. These are complete algebraic proofs in the cited lesson and hold without a characteristic-zero assumption.

For the arithmetic assertions, use the normalized local invariant and global injectivity of the Brauer localization map. Both are now proved in the written Brauer groups of local and global fields, Theorems 24.2 and 24.4. The precise compatibility, proved there for finite local extensions in every characteristic, is
\[
\operatorname{inv}_E(\operatorname{res}_{E/F}A)
 =[E:F]\operatorname{inv}_F(A)
\]
for finite extensions of nonarchimedean local fields, with real invariant \(1/2\) becoming zero over \(\mathbb C\). A local division quaternion algebra has invariant \(1/2\), so a quadratic field makes it zero and splits the algebra. This proves the local assertion using the algebraic criterion.

At a split local quadratic algebra \(F_v\times F_v\), an embedding into a division algebra would give a nontrivial idempotent, which is impossible. This proves necessity in the global assertion. Conversely suppose every ramified place remains a field. At each place above it the degree-two restriction kills invariant \(1/2\); at other places the original algebra was split. Thus \(D\otimes_FE\) is split at every completion of \(E\). For the cyclic quaternion algebra over the number field \(E\), the injectivity part of the Brauer localization theorem gives zero global class. It is a degree-two central simple algebra and hence is \(M_2(E)\). The algebraic criterion gives the required global embedding. \(\square\)

**Lemma 5.1 — distributing embeddings over all classes.** If \(m_\ell(S)\) is the analogous optimal-embedding count into \(\mathcal O_\ell\), modulo \(\mathcal O_\ell^\times\), then
\[
\sum_i m(S,\mathcal O_i)=h(S)\prod_\ell m_\ell(S).
\tag{5.5}
\]

**Proof.** If a local embedding fails, the left side is zero as well. Otherwise \(K_S\) embeds into \(D\): it is imaginary at infinity and is a field at the ramified finite prime, so the quadratic-embedding lemma just proved applies, with its exact algebraic and class-field providers. Fix an embedding and regard \(S\subset K_S\subset D\). Define
\[
E=\{b\in\widehat D^\times:
 \widehat K_S\cap b\widehat{\mathcal O}b^{-1}=\widehat S\}.
\tag{5.6}
\]
The set \(K_S^\times\backslash E/\widehat{\mathcal O}^\times\) has two useful maps. First map it to \(\widehat K_S^\times\backslash E/\widehat{\mathcal O}^\times\), the product of the local embedding-class sets. Skolem–Noether supplies this description by conjugation. Over any representative \(b\), the stabilizer inside \(\widehat K_S^\times\) is
\(\widehat K_S^\times\cap b\widehat{\mathcal O}^\times b^{-1}=\widehat S^\times\).
Hence every fiber is
\[
K_S^\times\backslash\widehat K_S^\times/\widehat S^\times
\simeq\operatorname{Pic}(S).
\tag{5.7}
\]
For completeness, this ideal dictionary sends an idele \(a\) to the locally principal fractional ideal \(a\widehat S\cap K_S\). Conversely the local generators of an invertible fractional ideal give an idele. Changing generators multiplies by \(\widehat S^\times\), and multiplying the ideal by a field element divides by \(K_S^\times\). The lattice local-global correspondence used here is the same one as in Lesson 17. Thus this map counts the set in (5.6) as \(h(S)\prod_\ell m_\ell(S)\).

Second map the set to \(D^\times\backslash\widehat D^\times/\widehat{\mathcal O}^\times\), the right ideal-class set. Choose \(a_i\) with \(I_i=a_i\widehat{\mathcal O}\cap D\). In the fiber over \(I_i\), write \(b=\alpha a_i u\), with \(\alpha\in D^\times\) and \(u\in\widehat{\mathcal O}^\times\). Condition (5.6) becomes
\(K_S\cap\alpha\mathcal O_i\alpha^{-1}=S\).
The map \(s\mapsto\alpha^{-1}s\alpha\) is therefore an optimal embedding into \(\mathcal O_i\). Skolem–Noether shows that every optimal embedding occurs. The centralizer of the embedded field is its multiplicative group, so dividing on the left by \(K_S^\times\) and on the right by \(\mathcal O_i^\times\) gives precisely its embedding-conjugacy classes. The size of this fiber is \(m(S,\mathcal O_i)\). Counting the same set by its two maps proves (5.5). \(\square\)

This proves the embedding identity that appears as Voight, Theorem 30.4.7. Skolem–Noether and the field-centralizer assertion are already proved in Central simple algebras and the Brauer group, Theorems 2.1 and 3.1.

Write \(S_d\) for the order of negative discriminant \(d\), and write \(d=c_d^2D_d\), where \(D_d\) is the fundamental field discriminant and \(c_d\) is the conductor. Define
\[
m_p(d)=
\begin{cases}
0,&p\mid c_d,\\
1-\left(\dfrac{d}{p}\right),&p\nmid c_d.
\end{cases}
\tag{5.8}
\]
The symbol is Kronecker, including at \(2\). In the second line it records whether the quadratic field at \(p\) is split, ramified or unramified quadratic: its values are \(1,0,-1\), respectively.

**Lemma 5.2 — the local factors.** The local embedding count is one at every split quaternion prime. At the division prime it is (5.8).

**Proof at a split prime.** Put \(F=\mathbb Q_\ell\), \(R=\mathbb Z_\ell\), and \(K=K_S\otimes F\), which may be a field or \(F\times F\). An embedding into \(\operatorname{End}_R(R^2)\) makes \(R^2\) a lattice \(L\) in the regular \(K\)-module. In the field case that module has dimension one over \(K\); in the split case its two idempotents each have rank one. Optimality says that the multiplier ring \(\{a\in K:aL\subset L\}\) is \(S\otimes R\). Conjugacy by \(\mathrm{GL}_2(R)\) is exactly homothety of these lattices by \(K^\times\).

Every such lattice is homothetic to an order. In a field, choose \(x\in L\) with least field valuation. Then \(L/x\subset\mathcal O_K\) contains \(1\) as a primitive lattice vector. In the split case choose \(x\in L\) attaining the least valuation of both coordinates. Such an \(x\) exists: modulo \(\ell L\), the failure to attain either minimum is a proper linear subspace, and two proper subspaces do not cover the two-dimensional vector space. Again \(L/x\subset R\times R\) contains a primitive \(1\). Extend \(1\) to a basis \(1,u\). The element \(u\) is integral, so \(u^2=\operatorname{Tr}(u)u-\operatorname{N}(u)\) lies in this lattice. Hence it is an order \(T\). Its multiplier ring is itself, since a multiplier applied to \(1\) lies in \(T\). Optimality forces \(T=S\otimes R\). Thus all the lattices are homothetic to this one order, which itself provides the regular-representation optimal embedding. The local count is one.

**Proof at the division prime.** The split quadratic algebra cannot embed in a division algebra. Every quadratic field \(K/F\) does embed, by the quadratic-embedding lemma above and its exact algebraic and local Brauer-invariant inputs. The unique quaternion maximal order is its valuation ring. For every embedding, its intersection with \(K\) is the full ring of integers \(\mathcal O_K\). Thus a nonmaximal quadratic order has no optimal embedding. If the order is maximal, Skolem–Noether identifies its conjugacy classes with
\[
K^\times\backslash D_p^\times/\mathcal O_p^\times.
\tag{5.9}
\]
The valuation \(v_D= v_p\circ\operatorname{nrd}\) maps \(D_p^\times/\mathcal O_p^\times\) to \(\mathbb Z\). On \(K^\times\), the reduced norm is the field norm, so its image is \(f(K/F)\mathbb Z\), where \(f(K/F)\) is the residue degree. Consequently (5.9) has two elements for an unramified quadratic field and one for a ramified field. These are exactly (5.8). \(\square\)

All prime-local orders are maximal away from their conductors, so the product in (5.5) is \(m_p(d)\). The two local computations agree with Voight, Proposition 30.5.3, including its nonmaximal-order exclusion.

**Theorem 5.3 — Eichler's trace formula in the full-norm convention.** For every positive integer \(n\),
\[
\boxed{
\operatorname{tr}B(n)
=\frac{p-1}{12}\,\mathbf1_{n\text{ is a square}}
+\frac12\sum_{\substack{t\in\mathbb Z\\t^2<4n}}
 \ \sum_{\substack{d<0\text{ an order discriminant}\\df^2=t^2-4n, f\geq1}}
 \frac{h(d)}{w(d)}m_p(d).}
\tag{5.10}
\]
Here \(h(d)=h(S_d)\), \(w(d)=w(S_d)\), and \(f\) is the index of \(\mathbb Z[\alpha]\) in an overorder; it is distinct from the conductor \(c_d\) in (5.8).

**Proof.** Start with the geometric norm count (5.3). Scalar quaternions of norm \(n\) occur precisely for square \(n\), and are \(\pm\sqrt n\). Their contribution is \(\sum_i2/(2w_i)\), the first term of (5.10).

For nonscalar \(\alpha\in\mathcal O_i\), let \(t=\operatorname{trd}(\alpha)\). Definiteness gives \(t^2<4n\): the imaginary part has positive norm, so equality would force a scalar. The field \(\mathbb Q[\alpha]\) is imaginary quadratic, and \(\mathbb Z[\alpha]\) has discriminant \(t^2-4n\). Its intersection with \(\mathcal O_i\) is a unique order \(S\) into which \(\mathbb Z[\alpha]\) embeds optimally after taking this overorder. If \([S:\mathbb Z[\alpha]]=f\), change of basis in the trace pairing gives \(\operatorname{disc}(S)f^2=t^2-4n\).

Fix \(t\) and such an overorder \(S_d\), with its distinguished root of \(x^2-tx+n\). Its optimal embeddings correspond exactly to these \(\alpha\)'s. The stabilizer of \(\alpha\) under \(\mathcal O_i^\times\)-conjugation is \(S_d^\times\), because its field is its centralizer. Each conjugacy orbit has size \(2w_i/(2w(d))\). Thus the contribution of one orbit to (5.3) is \(1/(2w(d))\), and the whole contribution for \(d,t\) is
\[
\frac1{2w(d)}\sum_i m(S_d,\mathcal O_i)
=\frac{h(d)}{2w(d)}m_p(d)
\tag{5.11}
\]
by Lemmas 5.1–5.2. Every nonscalar element has exactly one \(t\) and one optimal overorder, so summing proves (5.10). The sum is finite because \(|t|<2\sqrt n\) and only finitely many square divisors of each nonzero discriminant occur. This derivation is the arithmetic evaluation of the geometric side of Theorem 3.2; (5.3) shows its equality to the spectral matrix trace. \(\square\)

## 6. The discriminant-eleven computation

Lesson 17, Section 5.2, computed
\[
B(2)=\begin{pmatrix}1&2\\3&0\end{pmatrix},\qquad
w_1=2,\quad w_2=3.
\tag{6.1}
\]
Its constant eigenvector \((1,1)^t\) has eigenvalue \(3\), and its weighted-mean-zero eigenvector \((2,-3)^t\) has eigenvalue \(-2\). Thus the spectral side is \(3-2=1\), also the sum of the matrix's diagonal entries.

For the geometric side, \(n=2\) is not a square, so no scalar term occurs. The possible traces are \(-2,-1,0,1,2\). Their discriminants are \(-4,-7,-8,-7,-4\), all fundamental, so there are no proper overorders to add. The relevant class numbers are
\[
h(-4)=h(-7)=h(-8)=1,\qquad
w(-4)=2,\quad w(-7)=w(-8)=1.
\tag{6.2}
\]
Here is an explicit class-number check. Use the written ideal–form correspondence and reduction proofs in the earlier quadratic-field lesson cited in Section 8, Theorems 10.1–10.2. A reduced positive primitive form \((a,b,c)\) satisfies \(|b|\leq a\leq c\), with \(b\geq0\) on a boundary. Its discriminant \(d=b^2-4ac\) gives \(|d|\geq3a^2\). For these three discriminants, this forces \(a=1\). The unique reduced forms are respectively \((1,0,1)\), \((1,1,2)\) and \((1,0,2)\). The unit counts follow from the integral trace of a unit of norm one. A nonreal such unit has trace \(-1,0\) or \(1\), so extra units generate the orders of discriminant \(-3\) or \(-4\). Only \(-4\) occurs here, with units \(\{\pm1,\pm i\}\).

The nonzero squares modulo \(11\) are \(1,3,4,5,9\). Therefore \((-8/11)=1\), \((-7/11)=1\) and \((-4/11)=-1\). Substitution in (5.10) gives:

| Trace \(t\) | Discriminant \(d\) | \(h(d)\) | \(w(d)\) | \(m_{11}(d)\) | Contribution \(h(d)m_{11}(d)/(2w(d))\) |
|---:|---:|---:|---:|---:|---:|
| \(-2\) | \(-4\) | \(1\) | \(2\) | \(2\) | \(1/2\) |
| \(-1\) | \(-7\) | \(1\) | \(1\) | \(0\) | \(0\) |
| \(0\) | \(-8\) | \(1\) | \(1\) | \(0\) | \(0\) |
| \(1\) | \(-7\) | \(1\) | \(1\) | \(0\) | \(0\) |
| \(2\) | \(-4\) | \(1\) | \(2\) | \(2\) | \(1/2\) |

The geometric trace is \(1/2+1/2=1\), in agreement with (6.1). The vanishing rows have a precise cause: those quadratic fields split at \(11\) and cannot embed into the local division algebra. No modular-form eigenvalue was used to obtain their contribution.

As a second normalization check, take \(n=1\). Then \(B(1)=I\), the scalar contribution is the mass, and \(t=0,\pm1\) give \(d=-4,-3,-3\). Since \(h(-3)=1\), \(w(-3)=3\), the formula becomes
\[
h=\frac{p-1}{12}
+\frac14\left(1-\left(\frac{-4}{p}\right)\right)
+\frac13\left(1-\left(\frac{-3}{p}\right)\right).
\tag{6.3}
\]
For \(p=11\), both symbols are \(-1\), so \(h=5/6+1/2+2/3=2\). The reduced-form check for \(-3\) has the sole form \((1,1,1)\). Formula (6.3) is the maximal-order class-number formula already used in Lesson 17, recovered here from the trace rather than assumed in its derivation.

## 7. Exercises and complete solutions

**Exercise 7.1 — class equation (easy).** Derive the class equation of a finite group from the compact trace formula. Track all measures.

**Solution 7.1.** Take counting Haar measure on \(G\) and its centralizers, counting lattice measures, and \(\Gamma=G\). The quotient \(X\) is one point of mass one, and \(R(f)\) on it is multiplication by \(\sum_{g\in G}f(g)\). For each \(\gamma\), the quotient \(\Gamma_\gamma\backslash G_\gamma\) is one point of mass one. The other quotient \(G_\gamma\backslash G\) has one unit of measure per coset, as its unfolding sums exactly once over every element of \(G\). For \(f=1\), its orbital integral is \([G:G_\gamma]\). The trace identity therefore gives \(|G|=\sum_{[\gamma]}[G:G_\gamma]\). If the centralizer Haar measure is instead normalized to total mass one, the centralizer lattice-quotient volume becomes \(1/|G_\gamma|\) and the orbital integral becomes \(|G_\gamma|[G:G_\gamma]\); their product is unchanged. This also checks the rescaling rule after (3.7).

**Exercise 7.2 — Poisson summation (medium).** Derive Poisson summation for Schwartz functions from the trace on \(\mathbb Z\backslash\mathbb R\).

**Solution 7.2.** Use Lebesgue measure, counting measure on \(\mathbb Z\), and the Fourier transform (4.3). Direct integration gives \(R(f)e_n=\widehat f(-n)e_n\). The periodization \(p_f(t)=\sum_kf(t+k)\) is smooth, with uniformly convergent differentiated series; for every derivative this follows from Schwartz decay, uniformly for \(0\leq t\leq1\). Unfolding computes its \(n\)-th Fourier coefficient as \(\widehat f(n)\). Integration by parts twice, and more often if desired, gives an absolutely summable coefficient sequence. Hence convolution with \(p_f\) is the sum of its rank-one Fourier projections weighted by \(\widehat f(-n)\), a trace-class description. Its trace is \(\sum_n\widehat f(-n)\).

The geometric kernel is \(K(x,y)=p_f(y-x)\), whose diagonal is the constant \(p_f(0)=\sum_kf(k)\). Its Fourier series converges absolutely to \(p_f\), since it has these coefficients and the Fourier basis is complete in \(L^2\). Thus its diagonal integral equals the same trace. Equating the two expressions and replacing \(n\) by \(-n\) proves (4.5), with absolute convergence on both sides. For compactly supported smooth \(f\), this is exactly Theorem 3.2; the argument supplies the full Schwartz extension without assuming a compact-support theorem for a noncompactly supported test.

**Exercise 7.3 — central contribution (medium).** For a central \(\gamma\in\Gamma\), determine the orbital integral and its contribution to the trace formula.

**Solution 7.3.** Since \(G_\gamma=G\), choose \(dg_\gamma=dg\). The quotient \(G_\gamma\backslash G\) has one point of mass one, and conjugation fixes \(\gamma\). Therefore \(O_\gamma(f)=f(\gamma)\). Also \(\Gamma_\gamma=\Gamma\), so its geometric term is \(f(\gamma)\operatorname{vol}(\Gamma\backslash G)\). These assertions distinguish the two quantities. With \(dg_\gamma=c\,dg\), the orbital integral is \(f(\gamma)/c\) and the quotient volume is \(c\operatorname{vol}(X)\); their product is still the same term. Thus a formula calling the product the orbital integral has absorbed the volume into that name and must state that convention explicitly.

**Exercise 7.4 — Eichler's formula (hard).** Derive the trace formula for the full-norm Brandt matrix \(B(n)\) of a maximal order in \(B_{p,\infty}\), including the scalar term, unit weights, optimal overorders and local obstruction at \(p\).

**Solution 7.4.** Apply Theorem 3.2 to the projective adelic group (5.2), with \(K\) of volume one and the bi-\(K\) norm test \(f_n\). Its image is the class-function space, and its action there is \(B(n)\). On component \(i\), a diagonal ideal is \(\alpha I_i\) with \(\operatorname{nrd}(\alpha)=n\). Two generators give the same ideal exactly when they differ by a unit of the left order, so the trace is (5.3). The projective kernel counts the two lifts \(\pm\alpha\) once, while the component has volume \(1/w_i\); this gives the same factor \(1/(2w_i)\).

If \(n\) is a square, its two scalar lifts contribute \(1/w_i\) in each component; otherwise no scalar lift exists. Summing gives \((p-1)/12\) times the square indicator by (5.1).

For every remaining lift set \(t=\operatorname{trd}(\alpha)\). Its negative discriminant is \(\Delta=t^2-4n\). The unique optimal overorder \(S=\mathbb Q[\alpha]\cap\mathcal O_i\) has discriminant \(d\) with \(df^2=\Delta\). Fixing the abstract root of its polynomial identifies such lifts with labelled optimal embeddings of \(S_d\). Its unit centralizer has \(2w(d)\) elements, so an \(\mathcal O_i^\times\)-conjugacy orbit has \(2w_i/(2w(d))\) elements. Dividing by \(2w_i\) contributes \(1/(2w(d))\) per embedding class.

To sum embedding classes over all \(i\), use the set \(E\) in (5.6). Its quotient by \(K_S^\times\) and \(\widehat{\mathcal O}^\times\) maps to local embedding classes with fiber the invertible ideal-class group \(\operatorname{Pic}(S_d)\), of size \(h(d)\). Mapping the same set to right quaternion ideal classes has fiber the embedding classes of the corresponding left order. The two fiber counts give (5.5), with no selectivity assumption about one individual order.

At every split quaternion prime, normalize a lattice in the regular quadratic module to contain a primitive \(1\) inside the integral closure. A basis \(1,u\) makes it an order; its multiplier ring forces it to equal the given order. Thus the local embedding count is one, as in Lemma 5.2. At \(p\), the quadratic algebra must be a field and the order must be maximal. For a field, the quotient of valuation groups in (5.9) has size its residue degree: two for an unramified field, one for a ramified field. Therefore the product of local counts is exactly (5.8), including zero when \(p\) divides the quadratic-order conductor. The contribution for \(t,d\) is \(h(d)m_p(d)/(2w(d))\). Add these over \(t^2<4n\) and all \(df^2=t^2-4n\), then add the scalar term. This is (5.10). In particular, for \(p=11,n=2\), the five contributions in Section 6 sum to one, equal to \(\operatorname{tr}B(2)\).

## 8. What this lesson does not prove

The following inputs are distinct from the four trace-formula assertions proved above.

- Existence and uniqueness of Haar measure are Haar measure on locally compact groups, Theorems 8.3 and 9.2. The compatible quotient measure is Quotient measures and Weil’s integration formula, Theorem 3.1, with the inversion convention explained in Section 1. The centralizer compactness and unimodularity needed to apply it are proved in Lemma 1.2. Getz–Hahn, Section 3.2, especially Theorem 3.2.2, remains an attribution and reference.
- Section 3 proves trace class and the diagonal trace for every smooth compact Lie or adelic test, using the smooth-kernel lemma and the finite-level manifold decomposition. These arguments include the Fourier coefficient estimate, absolute nuclear sum and measure normalization. Dixmier–Malliavin factorization, stated for comparison from Getz–Hahn, Theorem 4.2.7, supplies another method; none of the trace-formula proof depends on that factorization theorem.
- Lesson 17, Sections 1–3, proves the local division valuation and maximal order, the adelic lattice and ideal dictionary, and compactness of the projective quotient over a number field. Its Sections 1–2 now deduce the local and global quaternion classification, in every characteristic, from the written NT-CFT-24 invariant and localization proofs. The quadratic-embedding lemma in Section 5 derives embedding existence from the written finite splitting criterion in the linked central-simple-algebra lesson, Theorems 4.1–4.2, and the written local restriction and global injectivity proofs of NT-CFT-24, Theorems 24.2 and 24.4. Skolem–Noether and centralizers are the proved Theorems 2.1 and 3.1 of that same written algebra lesson. The original embedding references are Voight, Corollary 13.4.5 and Proposition 14.6.7.
- The maximal rational quaternion mass formula is proved in Lesson 17, Theorem 4.3. The written Quadratic fields: ideal classes and binary quadratic forms, Theorems 10.1–10.2, proves the fundamental-discriminant correspondence and reduction, including the boundary convention. The written Orders in number fields and their Picard groups, its local-generator lemma, Proposition 11.2 and equation (15) with its proof, supplies invertible proper ideals and the same correspondence at every negative quadratic-order discriminant. The finite-idele quotient used in Lemma 5.1 follows by gluing local generators, using the lattice dictionary proved in Lesson 17, Section 3. Voight, Section 30.1 before Theorem 30.1.3, is the original reference. The enumeration and unit counts in Section 6 are carried out here.
- The norm-count description and the explicit discriminant-eleven Brandt matrix are the proved results of Lesson 17, Section 4 and Section 5.2. Lemmas 5.1–5.2 prove the embedding count and its local factors here; Theorem 5.3 derives the trace formula. Neither the Eichler trace identity nor its hard exercise is being substituted by a citation.

Arthur's compact formula in Section 1 and quaternion example in Section 3 are comparisons for Theorem 3.2. Getz–Hahn's Chapters 16–18 develop much broader spectral, relative and noncompact formulae. Jacquet–Langlands, Section 16, compares the quaternion and split trace formulae; its analytic argument is presented there with explicit formal qualifications. We have used none of those noncompact trace identities as a proof of the compact identity or of global transfer. The next lesson states precisely the correspondence whose proof uses that comparison.

## References

- J. Arthur, “An introduction to the trace formula,” in *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics Proceedings 4, 2005, Sections 1 and 3: kernel, geometric/spectral traces and the quaternion example. See the [Clay volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip04c.pdf).
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), 22 April 2022 draft: Theorems 3.2.2 and 4.2.7, Chapters 16–18, particularly Theorem 16.2.3, Theorem 17.7.4 and Corollary 18.4.1. Numbering refers to that draft.
- J. Voight, *Quaternion Algebras*, GTM 288, 2021: Corollary 13.4.5, Proposition 14.6.7, Theorem 25.3.15, Section 30.1, Theorem 30.4.7, Proposition 30.5.3 and Section 41.5, especially Main Theorem 41.5.2 and formulas 41.5.9–41.5.11. See the [author's editions](https://jvoight.github.io/quat.html).
- H. Jacquet and R. P. Langlands, *Automorphic Forms on GL(2)*, LNM 114, 1970, Section 16, especially formulas 16.1.3–16.1.6 for the quaternion geometric trace. See the [author's publications collection](https://publications.ias.edu/rpl/section/22).

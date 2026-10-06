# Proper infiniteness and automatic normality

*Self-checked by the writing AI. Original text: CC0 1.0.*

Countable sums of projections detect normality. In a properly infinite algebra, a singular representation that kills a countable partition of the identity would produce an uncountable orthogonal family of nonzero projections in its range. This contradicts sigma-finiteness of the generated range. The same construction, combined with completeness of a von Neumann projection lattice, also proves automatic normality for surjective homomorphisms from properly infinite algebras with separable predual.

The freely accessible construction uses [The universal enveloping von Neumann algebra and W*-algebras](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-10), Theorem 10.3 on normal–singular representations, its [complete singular-functional criterion](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-23), Theorem 11.2, and Corollary 11.4 on normality of isomorphisms. The full normal-extension and vector-functional proof, Theorem 9.1(ii), of [Operator spaces and preduals](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#oa-fnd-lt-10) lets us apply the splitting to a normal functional of the generated algebra. We use the full [bounded polar-decomposition argument](../reader/normal-products-and-closed-operator-graphs.html#polar-decomposition-for-closed-operators) and spectral projections in a von Neumann algebra. For the disintegration application we use [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html#5-decomposable-means-commuting-with-the-diagonal-algebra), Theorems 5.1 and 7.1. The normal state and the separating Borel coordinate needed there are constructed explicitly below.

Blackadar’s freely readable *Operator Algebras* treats the factor case and the abelian boundary example; Takesaki’s book provides further context. The arguments below establish the arbitrary-centre theorem and the arbitrary-target cardinality result using the complete programme prerequisites linked above.

A von Neumann algebra is **sigma-finite** here if it has a faithful normal state. Such an algebra has no uncountable orthogonal family of nonzero projections: a faithful state is positive on each of them, while all finite sums of their values are at most one. The equivalent projection formulation can also be used as the definition.

The identity of \(M\) is **properly infinite** if it contains two orthogonal projections, each Murray–von Neumann equivalent to the identity. Equivalently there are isometries \(s_0,s_1\in M\) with
\[
s_i^*s_i=1,\qquad s_0s_0^*s_1s_1^*=0.
\]
In this lesson \(M\) is called properly infinite when its identity has this property. Representations are unital on their nonzero support; a degenerate representation is first restricted to \(\pi(1)H\), with the zero representation on the complementary subspace.

## 1. A projection construction with continuum many branches

Suppose \((e_j)_{j\geq1}\subseteq M\) are orthogonal projections with strong sum \(1\). Set \(E_n=\sum_{j=1}^ne_j\). From the two isometries above obtain countably many isometries
\[
v_n=s_1^{n-1}s_0,\qquad n\geq1.
\]
Their range projections are orthogonal: for \(m<n\), \(v_m^*v_n=s_0^*s_1^{n-m}s_0=0\). Define
\[
q_n=v_nE_nv_n^*.
\tag{1.1}
\]
The \(q_n\) are orthogonal projections.

**Lemma 1.1.** For every infinite set \(J\subseteq\mathbb N\), the strong sum
\[
q_J=\sum_{n\in J}q_n
\]
majorizes a projection equivalent to \(1\). Consequently, if a nonzero unital representation \(\rho\) kills every \(e_j\), then \(\rho(q_n)=0\) for every \(n\), but \(\rho(q_J)\ne0\) for every infinite \(J\).

**Proof.** Enumerate \(J=\{j_1<j_2<\cdots\}\). Put
\[
f_1=E_{j_1},\qquad
f_k=E_{j_k}-E_{j_{k-1}}\quad(k\geq2).
\]
These are orthogonal projections summing strongly to \(1\), and \(f_k\leq E_{j_k}\). The partial isometries \(v_{j_k}f_k\) have orthogonal initial and final projections. Their strong sum
\[
w=\sum_{k\geq1}v_{j_k}f_k
\]
is an isometry: finite sums are contractions, their action on a vector is Cauchy by orthogonality, and \(w^*w=\sum_kf_k=1\). Its range projection satisfies \(ww^*\leq q_J\).

If \(\rho(e_j)=0\), each finite \(E_n\) and hence each \(q_n\) has zero image. But \(\rho(w)^*\rho(w)=\rho(1)\ne0\) and \(\rho(ww^*)\leq\rho(q_J)\), proving the last assertion. No preservation of the infinite sum by \(\rho\) has been assumed. \(\square\)

There is an almost-disjoint family \((J_b)_{b\in\{0,1\}^{\mathbb N}}\) of infinite subsets of \(\mathbb N\) of cardinality
\[
\mathfrak c=2^{\aleph_0}.
\]
To construct it, enumerate all finite binary strings, in order of increasing length, by the positive integers. For a branch \(b\), take the indices of its nonempty initial strings. Two different branches have only finitely many initial strings in common.

**Corollary 1.2.** Under the representation hypothesis of Lemma 1.1, the generated von Neumann algebra \(\rho(M)''\) contains \(\mathfrak c\) mutually orthogonal nonzero projections.

**Proof.** Use \(\rho(q_{J_b})\). They are nonzero by Lemma 1.1. For different branches,
\[
q_{J_b}q_{J_c}
=\sum_{n\in J_b\cap J_c}q_n
\]
is a finite sum killed by \(\rho\). Thus their images are orthogonal. \(\square\)

## 2. Automatic normality when the generated range is sigma-finite

**Theorem 2.1.** Let \(M\) be a sigma-finite properly infinite von Neumann algebra. If a representation \(\pi:M\to B(H)\) generates a sigma-finite von Neumann algebra \(\pi(M)''\), then \(\pi\) is normal. In particular every representation of \(M\) on a separable Hilbert space is normal.

**Proof.** Use the imported normal–singular decomposition
\[
\pi=\pi_{\mathrm n}\oplus\pi_{\mathrm s}.
\]
The projection giving the singular summand is central in \(N=\pi(M)''\). Its corner \(N_{\mathrm s}\) is sigma-finite. Suppose the summand is nonzero and choose a faithful normal state \(\omega\) of \(N_{\mathrm s}\). The functional
\[
\psi=\omega\circ\pi_{\mathrm s}
\]
is positive and singular. The coefficient formulation in the imported theorem implies this also for every normal \(\omega\): normal functionals are norm-convergent sums of vector functionals, and the singular functionals form a norm-closed space.

By the imported singular-functional criterion, every nonzero projection of \(M\) has a nonzero subprojection on which \(\psi\) vanishes. Choose a maximal orthogonal family of such nonzero projections. Its strong sum is \(1\); otherwise the complementary projection would contain another one. Sigma-finiteness of \(M\) makes the family countable. Write it as \((e_j)\), repeating zeros if it is finite.

Faithfulness of \(\omega\) gives \(\pi_{\mathrm s}(e_j)=0\), since these are positive projections with zero \(\omega\)-value. Corollary 1.2 now gives an uncountable orthogonal family of nonzero projections in \(N_{\mathrm s}\), contradicting its sigma-finiteness. Therefore \(\pi_{\mathrm s}=0\).

If \(H\) is separable, choose a total sequence of unit vectors \((\xi_n)\). The state
\[
\omega(x)=\sum_n2^{-n}\langle x\xi_n,\xi_n\rangle
\]
is normal and faithful on any unital von Neumann algebra acting on \(H\). Thus its generated algebra is sigma-finite. Restriction to the support handles degenerate representations. \(\square\)

The proper-infiniteness hypothesis applies to the domain. An abelian infinite-dimensional algebra can have singular one-dimensional representations, as shown in the imported universal-enveloping lesson. The finite type II normality result requires additional finite-algebra arguments.

## 3. The Calkin obstruction

For an infinite-dimensional separable \(H\), write
\[
\mathcal Q(H)=B(H)/\mathcal K(H).
\]

**Corollary 3.1.** The Calkin algebra has no nonzero representation on a separable Hilbert space.

**Proof.** \(B(H)\) is sigma-finite and properly infinite. A faithful normal state is obtained by a positive summable weighted sum of basis vector states; two isometries with orthogonal ranges are given by the even and odd basis coordinates. If \(\sigma\) represented \(\mathcal Q(H)\) on a separable space, its composition \(\pi\) with the quotient map would be normal by Theorem 2.1.

Let \((p_n)\) be the rank-one basis projections. Then \(\pi(p_n)=0\), since they are compact. Normality and \(\sum_np_n=1\) give
\[
\pi(1)=\sum_n\pi(p_n)=0.
\]
Thus \(\pi\), and hence \(\sigma\), is zero. \(\square\)

This obstruction does not say that the Calkin algebra has no representations at all. Its universal representation exists, but cannot act on a separable Hilbert space.

## 4. Why disintegration needs a separable C*-algebra

Let \((X,\mu)\) be a standard sigma-finite base and consider the constant infinite-dimensional field
\[
H=\int_X^\oplus\ell^2\,d\mu(x).
\]
Its diagonal \(D=L^\infty(X,\mu)\) has commutant
\[
A=D'=\int_X^\oplus B(\ell^2)\,d\mu(x).
\tag{4.1}
\]
This is a properly infinite sigma-finite von Neumann algebra. Proper isometries can be taken constant on the fibres. To see sigma-finiteness explicitly, choose \(w>0\) with \(\int w\,d\mu=1\) and use
\[
\Omega(a)=\int_X w(x)\sum_{n\geq1}2^{-n}
\langle a(x)e_n,e_n\rangle\,d\mu(x).
\tag{4.2}
\]
This state is normal directly: for \(\xi_n(x)=w(x)^{1/2}e_n\), each \(\xi_n\) belongs to \(H\) and has norm one, and \(\Omega(a)=\sum_n2^{-n}\langle a\xi_n,\xi_n\rangle\). This is a norm-convergent sum of normal vector functionals. It is faithful: for \(a\geq0\), zero integral forces every positive basis coefficient to vanish almost everywhere, outside one countable union of null sets; hence \(a(x)=0\) there.

A separating Borel coordinate also needs no classification theorem. By the definition of a standard Borel space, realize \(X\) as a Borel subset of a Polish space and let \((U_n)_{n\geq1}\) be the traces of a countable base. They separate points. The Borel function \(t(x)=\sum_{n\geq1}2\,3^{-n}1_{U_n}(x)\) takes values in \([0,1]\) and is injective: if the first differing membership is at index \(m\), its contribution has modulus \(2\,3^{-m}\), while the sum of all later contributions has modulus at most \(3^{-m}\).

**Theorem 4.1.** If the identity representation of the full algebra \(A\) in (4.1) disintegrates into representations of \(A\) on the prescribed fibres \(\ell^2\), then \(\mu\) is concentrated on its point atoms. Conversely, on a countable atomic base this full-algebra disintegration exists, even though \(A\) need not be separable in norm.

**Proof.** Use the injective bounded Borel coordinate \(t:X\to[0,1]\) constructed above. Let \(T=m_t\in D\subseteq A\). If a field \(\pi_x\) of representations of all of \(A\) disintegrates its identity representation, uniqueness of the decomposable field for this single operator gives
\[
\pi_x(T)=t(x)1_{\ell^2}
\tag{4.3}
\]
almost everywhere. Each \(\pi_x\) is normal by Theorem 2.1, because it acts on a separable Hilbert space.

Fix a retained \(x\). The continuous functions
\[
g_n(s)=\max\{0,1-n|s-t(x)|\}
\]
decrease pointwise on \([0,1]\) to the indicator of \(\{t(x)\}\). Spectral calculus gives \(g_n(T)\downarrow1_{\{x\}}1\) in \(A\). Normality preserves this bounded decreasing infimum, whereas (4.3) gives \(\pi_x(g_n(T))=1\) for every \(n\). Hence
\[
\pi_x(1_{\{x\}}1)=1.
\tag{4.4}
\]
If \(\mu(\{x\})=0\), the projection on the left is zero in \(A\), a contradiction. Every retained point is therefore an atom. There are at most countably many point atoms on a sigma-finite base.

Conversely, if these atoms exhaust the measure, the integral algebra is the product of the fibre algebras, with point weights in the Hilbert norm. Evaluation at each positive-mass atom is a well-defined normal representation of the whole product. Their direct integral is its identity representation. \(\square\)

If the base has a diffuse part of positive measure, \(H\) is still separable but the proposed full-algebra representation field cannot exist. Choosing a separable strong-dense C*-subalgebra permits disintegration; replacing it by the entire nonseparable commutant loses that conclusion. Only the one coordinate operator \(T\) was needed to put the contradiction on a common conull set.

## 5. Surjective homomorphisms: a cardinality argument

We need a kernel lemma in which the range need not be sigma-finite.

**Lemma 5.1.** Let \(M\) be sigma-finite and let \(\rho:M\to N\) be a nonzero surjective singular *-homomorphism onto a von Neumann algebra. Its kernel contains orthogonal projections \((e_j)\) with strong sum \(1\).

**Proof.** Let \(I=\ker\rho\). Its ultraweak closure is a two-sided ultraweakly closed ideal \(Mz\), for a central projection \(z\). One way to see the central projection description is to take the supremum of the support projections of positive elements of the ideal. The ideal is invariant under all unitary conjugations, so this supremum is central. The spectral projections away from zero belong to the ideal, and their supremum is the support. Consequently the closed ideal is precisely the central summand determined by this supremum.

The restriction of \(\rho\) to \(M(1-z)\) is injective, since \(I\cap M(1-z)=0\). Surjectivity makes its image the von Neumann corner \(N\rho(1-z)\). It is thus a *-isomorphism of von Neumann algebras and is normal. It is also singular: singular coefficient functionals remain singular after multiplication by the fixed central projection \(1-z\), by the imported normal–singular splitting theorem. A map that is both normal and singular is zero. Injectivity now forces \(1-z=0\). Therefore \(I\) is ultraweakly dense in \(M\).

We spell out the projection approximation in a norm-closed ideal. For \(a\in I_+\), the projection
\[
p_\delta=1_{[\delta,\infty)}(a)\quad(\delta>0)
\]
belongs to \(I\), because \(p_\delta=a\,h_\delta(a)\) with bounded Borel \(h_\delta(s)=1_{[\delta,\infty)}(s)/s\). The supremum of all the projections in \(I\) is \(1\), by ultraweak density.

Their finite joins also belong to \(I\). For \(p,q\in I\), the final projection of the polar partial isometry of \((1-p)q\) is \((p\vee q)-p\), and its initial projection is at most \(q\). Hence the final projection equals \(v q v^*\in I\), and \(p\vee q=p+v q v^*\in I\).

Let \(\tau\) be a faithful normal state of \(M\). Normality, applied to the directed finite joins, gives projections \(r_n\in I\) with \(\tau(r_n)>1-2^{-n}\). Replace them by their successive finite joins to make them increasing. Faithfulness gives \(r_n\uparrow1\). Taking \(e_1=r_1\), \(e_n=r_n-r_{n-1}\) proves the lemma. \(\square\)

**Theorem 5.2.** If \(M\) is properly infinite with separable predual, every surjective *-homomorphism
\[
\pi:M\longrightarrow N
\]
onto a von Neumann algebra is normal, with no sigma-finiteness assumption on \(N\).

**Proof.** If \(M=0\), the surjective map has zero target and is normal. Assume \(M\ne0\). A separable predual supplies a faithful normal state as follows. Choose a countable norm-dense set of normal functionals. Split their real and imaginary parts into positive normal functionals, using the [full Jordan-decomposition proof](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03), Corollary 2.8. Normalize the nonzero positive pieces and enumerate the resulting states as \((\varphi_n)\), repeating one if the list is finite. These states separate positive elements: if they all vanish on \(x\geq0\), the original dense functionals all vanish on \(x\), hence every predual functional vanishes on \(x\), forcing \(x=0\). The norm-convergent sum \(\sum_n2^{-n}\varphi_n\) is therefore a faithful normal state. Positivity of the normal pieces follows also from the central splitting in Theorem 10.3 of the universal-enveloping lesson. A separable predual also bounds the cardinality:
\[
|M|\leq\mathfrak c.
\tag{5.1}
\]
Indeed, evaluation on a countable norm-dense subset of \(M_*\) embeds \(M\) into \(\mathbb C^{\mathbb N}\). Since \(\pi\) is onto, \(|N|\leq\mathfrak c\).

Split the representation \(\pi\) into normal and singular parts using a faithful normal concrete realization of \(N\). The projection \(q\) giving the singular part belongs to \(Z(N)\), because the imported splitting projection is central in \(\pi(M)''=N\). Moreover the singular homomorphism
\[
\pi_{\mathrm s}:M\longrightarrow Nq
\]
is onto: for \(b\in Nq\), choose \(a\) with \(\pi(a)=b\), and then \(\pi_{\mathrm s}(a)=b\).

If \(q\ne0\), Lemma 5.1 supplies a partition of \(1\) killed by \(\pi_{\mathrm s}\). Corollary 1.2 produces \(\mathfrak c\) mutually orthogonal nonzero projections in \(Nq\). The von Neumann projection lattice is complete. For every subset of this family take its join; different subsets have different joins, by orthogonality and nonzeroness. Thus
\[
|N|\geq2^{\mathfrak c}>\mathfrak c,
\]
contradicting (5.1). Hence \(q=0\), so \(\pi\) is normal. \(\square\)

Surjectivity is used twice: to make the remaining faithful corner in Lemma 5.1 a von Neumann algebra, and to bound the cardinality of the target. A general norm-closed image need not have a complete projection lattice.

## 6. Graded exercises with complete solutions

### Exercise 6.1 — Finite-dimensional targets (basic)

Show directly, without Theorem 2.1, that a properly infinite unital C*-algebra has no nonzero representation on a finite-dimensional Hilbert space.

**Solution.** Restrict a nonzero representation to the range of its identity projection. On this nonzero finite-dimensional space the images of \(s_0,s_1\) are isometries, hence unitaries. Their range projections are both the identity. They cannot be orthogonal, whereas the original range projections are orthogonal and a *-homomorphism preserves that identity. This is a contradiction.

### Exercise 6.2 — Binary branches modulo compact operators (intermediate)

Index an orthonormal basis of a separable Hilbert space by the nonempty finite binary strings. For each infinite branch \(b\), let \(P_b\) project onto its initial strings. Compute \(P_bP_c\) for distinct branches, and show that their Calkin images form an orthogonal family of \(\mathfrak c\) projections, each majorizing a projection equivalent to the Calkin identity.

**Solution.** If the branches share exactly \(r\) initial bits before separating, their common nonempty initial strings have lengths \(1,\ldots,r\). Thus \(P_bP_c\) is the rank-\(r\) projection on those strings; if \(r=0\), it is zero. It is compact, so the quotient images are orthogonal. Each \(P_b\) has infinite rank and is not compact. Enumerating its basis vectors gives an isometry \(V_b\) from the whole Hilbert space onto \(P_bH\), with \(V_b^*V_b=1\), \(V_bV_b^*=P_b\). These identities survive in the quotient, giving equivalence of its image to the Calkin identity. In particular every nonzero unital representation of the Calkin algebra sends every such image to a nonzero projection. The resulting uncountable orthogonal ranges also prove the separable-representation obstruction directly.

### Exercise 6.3 — The atomic boundary of the disintegration obstruction (advanced)

Let \(X=\{0,1\}\cup[2,3]\), with measure \(\delta_0+2\delta_1\) on the two points and Lebesgue measure on the interval. Use the constant \(\ell^2\) field. Explain why the full algebra \(D'\) cannot disintegrate into its prescribed fibres, and describe the full-algebra disintegration after restricting the base to \(\{0,1\}\).

**Solution.** The interval has positive measure and each of its points has zero mass. Theorem 4.1 rules out a full-algebra representation field there: normality of a fibre representation would send the singleton spectral projection of a separating coordinate to the identity, though that projection is zero in the diffuse algebra.

On the two-point restriction,
\[
D'=B(\ell^2)\oplus B(\ell^2).
\]
The fibre maps are \((a_0,a_1)\mapsto a_j\), \(j=0,1\). They are normal and act on the entire nonseparable C*-algebra. The integral Hilbert norm is
\[
\|(\xi_0,\xi_1)\|^2=\|\xi_0\|^2+2\|\xi_1\|^2.
\]
The unitary to the usual Hilbert direct sum is \((\xi_0,\xi_1)\mapsto(\xi_0,\sqrt2\,\xi_1)\), and the algebra acts as \(a_0\oplus a_1\). Thus the atomic part admits the desired decomposition; the obstruction comes from the positive-measure diffuse part.

## References

- [Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979.
- [Blackadar] B. Blackadar, *Operator Algebras*, [free author-hosted PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- The universal-enveloping lesson linked above supplies the normal–singular and singular-projection results.

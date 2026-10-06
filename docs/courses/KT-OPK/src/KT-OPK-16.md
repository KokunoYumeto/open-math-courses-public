# Inductive limits and the K-theory of AF and AT algebras

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Independently authored CC0 lesson; self-checked by the writing AI.*

Finite matrix algebras contribute ranks to K_0 and nothing to K_1. Matrix algebras over a circle contribute both ranks and winding numbers. Passing to an inductive limit preserves these computations, but it is essential to compute the actual connecting maps: multiplicity counts ranks, whereas winding counts the total degree of a matrix determinant.

We will compute the Bunce–Deddens groups directly from their circle-algebra system, prove uniqueness of their trace, and distinguish them from a superficially similar doubled pullback system. We also prove the dimension-group converse and the simple AF range theorem with a prescribed trace simplex. The full AF classification proof is the preceding programme prerequisite.

The continuity results are [Matrix stability, stability and continuity of K_0, Theorem 3.3](KT-OPK-05.md#3-group-completion-and-scalar-kernels-commute-with-the-limit) and [Invertibles, unitaries and K_1, Theorem 4.1](KT-OPK-06.md#4-realizing-an-invertible-path-at-a-late-stage). They allow arbitrary sequential C*-connecting homomorphisms, including maps with kernels. Circle groups and generators are [Lesson 6, Theorem 5.2](KT-OPK-06.md#5-components-detected-by-spectra-winding-and-index) and [Topological K-theory, Theorem 5.1](KT-OPK-12.md#5-adding-circles-with-arbitrary-coefficients).

## 1. AF-algebras and their complete invariant

An **AF-algebra** here is a sequential inductive limit of finite-dimensional C*-algebras. Write its stages as

\[
F_k=\bigoplus_{j=1}^{r_k}M_{n_{k,j}}(\mathbb C).
\tag{1.1}
\]

**Proposition 1.1.** Every AF-algebra \(A\) has \(K_1(A)=0\).

*Proof.* An invertible matrix over a finite-dimensional C*-algebra is homotopic to its polar unitary. Each finite-dimensional unitary is unitarily diagonalizable, with eigenvalues \(e^{i\theta_j}\); replacing them by \(e^{it\theta_j}\) gives a path from the identity to that unitary. Direct sums of these paths show \(K_1(F_k)=0\), at every matrix size. Continuity now gives

\[
K_1(A)=\varinjlim_k K_1(F_k)=0.
\tag{1.2}
\]

The same argument covers nonunital AF limits because continuity uses the external unitizations. \(\square\)

For \(K_0\), use the class of a minimal projection as the generator of each summand, so \([1_{M_n}]=n\), not \(1\). The stage groups are \(\mathbb Z^{r_k}\), their positive cones are \(\mathbb Z_+^{r_k}\), and the connecting maps are nonnegative multiplicity matrices \(R_k\). The scale consists of classes of projections in the algebra itself, rather than all matrix projections.

The identification

\[
\begin{gathered}
(K_0(A),K_0(A)^+,\Sigma(A))\\
\cong\varinjlim_k
(\mathbb Z^{r_k},\mathbb Z_+^{r_k},\Sigma(F_k))
\end{gathered}
\tag{1.3}
\]

is the actual [AF-algebras, Theorem 7.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06). That theorem identifies the positive limit monoid with projection classes and proves cancellation. We use it rather than reprove the dimension-group identification.

For unital AF-algebras, the scale is determined by the order unit \(u=[1_A]\): it is \(\{g:0\leq g\leq u\}\). The following stronger results are imported from [AF-algebras, §8](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-07).

**Classification and lifting.** Every isomorphism of scaled ordered \(K_0\)-groups of AF-algebras is induced by an algebra isomorphism (Theorem 8.3). Every automorphism of the scaled group lifts to an automorphism of the AF-algebra (Corollary 8.4). Stable isomorphism is equivalent to isomorphism of the ordered groups without their scales (Theorem 8.5).

The scale therefore cannot be omitted from a unital classification statement. Also the lifting statement prescribes the induced group map; it does not prescribe the order of the lifted automorphism. These are useful inputs for later crossed-product calculations.

For a UHF system \(M_{n_k}\), with \(n_k\mid n_{k+1}\) and unital diagonal multiplicity \(m_k=n_{k+1}/n_k\), the coordinate \(r/n_k\) identifies the limit group with

\[
\mathbb Z(q)=\bigcup_k n_k^{-1}\mathbb Z.
\tag{1.4}
\]

Here the supernatural number \(q\) records the limiting prime exponents of the \(n_k\). The positive cone has the usual rational order, the unit is \(1\), and the scale is \(\mathbb Z(q)\cap[0,1]\). This normalization was proved in Lesson 5, §5; Proposition 1.1 adds \(K_1=0\).

**Theorem 1.2 (The kernel of the AF K-theory action).** Give \(\operatorname{Aut}(A)\) the topology of pointwise norm convergence, for an AF-algebra \(A\). The following coincide: the closure of inner automorphisms implemented by unitaries in \(A^+\), the closure of those implemented by unitaries in \(M(A)\), the connected component of the identity, the path component of the identity, and

\[
\operatorname{Id}(A)=\{\alpha:\alpha_*=1\text{ on }K_0(A)\}.
\tag{1.5}
\]

These are the approximately inner automorphisms. For each one there is a norm-continuous path \(u_t\in U(A^+)\), \(t\geq0\), starting at \(1\), with \(\operatorname{Ad}u_t\to\alpha\) pointwise in norm.

*Proof.* The zero algebra is immediate. This topology makes the automorphisms a topological group: contractivity gives continuity of composition, and
\(\|\beta^{-1}(a)-\alpha^{-1}(a)\|=\|a-\beta(\alpha^{-1}(a))\|\)
gives continuity of inversion at \(\alpha\). We can choose increasing finite-dimensional subalgebras \(A_n\) with dense union: use the canonical finite-dimensional images in the sequential AF limit. Put \(H_n=A_n+\mathbb C1\subset A^+\), with the external unit. Each \(H_n\) is finite-dimensional and unital, includes its scalar complementary summand, and their union is dense in \(A^+\). An automorphism extends by fixing the external scalar. If it acts trivially on \(K_0(A)\), it acts trivially on \(K_0(A^+)\) by the scalar split summand.

Fix \(n\), choose matrix units \(e^{(j)}_{kl}\) for every summand of \(H_n\), and put \(f^{(j)}_{kl}=\alpha(e^{(j)}_{kl})\). AF cancellation, in the exact projection-monoid theorem cited above, supplies actual partial isometries \(w_j\in A^+\) with

\[
\begin{gathered}
w_j^*w_j=e^{(j)}_{11},\\
w_jw_j^*=f^{(j)}_{11}.
\end{gathered}
\tag{1.6}
\]

Indeed equality of their \(K_0\)-classes is equality in the cancellative projection monoid; this is unstabilized equivalence of these projections. Define

\[
u_n=\sum_j\sum_i f^{(j)}_{i1}w_j e^{(j)}_{1i}.
\tag{1.7}
\]

The supports of \(w_j\) and matrix-unit products give \(u_n^*u_n=\sum_{j,i}e^{(j)}_{ii}=1\), \(u_nu_n^*=\sum_{j,i}f^{(j)}_{ii}=1\), and \(u_ne^{(j)}_{kl}u_n^*=f^{(j)}_{kl}\). Thus \(\operatorname{Ad}u_n\) agrees exactly with \(\alpha\) on \(H_n\).

The relative commutant \(C_n=H_n'\cap A^+\) is AF. To see this directly, if summand \(j\) has size \(d_j\), define

\[
\mathcal E_n(x)=\sum_j\frac1{d_j}
\sum_{k,l}e^{(j)}_{kl}x e^{(j)}_{lk}.
\tag{1.8}
\]

Multiplication by a matrix unit on either side gives the same expression, so this bounded linear map takes values in \(C_n\). If \(x\in C_n\), it equals \(x\): use \(\sum_{k,l}e_{kl}^{(j)}e_{lk}^{(j)}=d_j\sum_ke_{kk}^{(j)}\). For \(m\geq n\), the map preserves \(H_m\). Approximate an element of \(C_n\) by elements of \(H_m\) and apply \(\mathcal E_n\). This shows that \(C_n\) is the closure of the increasing finite-dimensional unital algebras \(C_n\cap H_m\).

Every unitary in a unital AF-algebra has a norm-continuous path to the identity. Approximate it sufficiently closely in a unital finite stage, polar-correct there, and use the finite-dimensional spectral logarithm to join that stage unitary to \(1\). Its close ratio with the original unitary has a continuous logarithm, giving the remaining path. These are the polar, spectral and close-unitary paths of Proposition 1.1 and [Lesson 6](KT-OPK-06.md).

Now \(u_n^*u_{n+1}\) commutes with \(H_n\), since both conjugations equal \(\alpha\) there. Choose \(v_n:[0,1]\to U(C_n)\) joining \(1\) to \(u_n^*u_{n+1}\), and set

\[
\begin{gathered}
u_t=u_n v_n(t-n),\\
n\leq t\leq n+1.
\end{gathered}
\tag{1.9}
\]

Join \(1\) to \(u_1\) on the initial interval. The paths fit at all integer endpoints. For every \(t\geq n\), conjugation by \(u_t\) equals \(\alpha\) on \(H_n\). Contractivity and density give pointwise norm convergence on \(A\), uniformly for sufficiently late \(t\). Reparameterize by \(t=s/(1-s)\), and assign \(\alpha\) at \(s=1\). This is a pointwise norm continuous path of automorphisms from the identity to \(\alpha\). The K-theory kernel therefore lies in both the path component and the closure of \(A^+\)-inner automorphisms.

Conversely a multiplier unitary fixes every projection class: for a matrix projection \(p\) over \(A\), the product \(up\) belongs to that matrix algebra and gives a partial-isometry equivalence from \(p\) to \(upu^*\). Actual projection classes generate \(K_0(A)\), by finite-stage ranks and continuity. For each fixed projection, its image class is locally constant as a function of the automorphism, by the close-projection lemma; pointwise norm convergence controls the finitely many entries of a matrix projection. Hence the closure of multiplier-inner automorphisms acts trivially on \(K_0\), as does every connected set of automorphisms containing the identity. The \(A^+\)-inner closure lies in the multiplier-inner closure, and the identity path component lies in the connected component. Combining these inclusions with the preceding paragraph proves all five equalities. \(\square\)

This proves the theorem and the asymptotic unitary-path conclusion of [Blackadar 1998, Exercise 7.7.5, printed pp. 57–58]. Its cancellation input is precisely the AF projection-monoid theorem already imported above; general AT classification is not used.

## 2. Circle blocks: multiplicity and total degree

An **AT-algebra** is a sequential inductive limit of finite sums of matrix algebras over \(C(\mathbb T)\). At a stage

\[
E_k=\bigoplus_{j=1}^{r_k}M_{n_{k,j}}(C(\mathbb T)),
\]

the two groups are

\[
\begin{gathered}
K_0(E_k)=\mathbb Z^{r_k},\\
K_1(E_k)=\mathbb Z^{r_k}.
\end{gathered}
\tag{2.1}
\]

For K_0 use minimal constant projections. For K_1 the generator of a circle summand is

\[
\begin{gathered}
g_n(z)=ze_{11}+(1-e_{11}),\\
\operatorname{wind}(\det g_n)=1.
\end{gathered}
\tag{2.2}
\]

Matrix stability, the circle computation and its counterclockwise winding convention prove these assertions. By [Lesson 2, Proposition 5.1](KT-OPK-02.md#5-gluing-around-a-circle-and-across-a-sphere), all complex circle vector bundles are trivial, so the positive cone in K_0 is \(\mathbb Z_+^{r_k}\); its unit vector has coordinates \(n_{k,j}\).

For a homomorphism \(\phi:E_k\to E_{k+1}\), define \(R_{ij}\) as the rank of the image of the \(j\)-th minimal constant projection in target summand \(i\). Rank is constant on the target circle because a continuous projection has locally constant rank. Define \(D_{ij}\) as the winding number of the determinant of the image of the \(j\)-th generator (2.2) in that summand. For a nonunital map use

\[
\phi(g)+1-\phi(1)
\tag{2.3}
\]

as its target unitary; this is the usual unitized image. The generator calculations show exactly that

\[
\phi_{*0}=R,\qquad \phi_{*1}=D.
\tag{2.4}
\]

Indeed K_0 is generated by the stated projection classes and K_1 by the stated unitary classes, so these images determine both homomorphisms. Continuity gives the general computation, for simple AT-algebras as well:

\[
\begin{gathered}
K_0(\varinjlim E_k)=\varinjlim(\mathbb Z^{r_k},R_k),\\
K_1(\varinjlim E_k)=\varinjlim(\mathbb Z^{r_k},D_k).
\end{gathered}
\tag{2.5}
\]

The K_0 cone is the union of the images of the stage cones; the scale is the union of the images of the stage rank intervals. These follow from the projection and relation continuity in Lesson 5. In a unital system \(R_k\mathbf n_k=\mathbf n_{k+1}\), giving the distinguished unit class.

**Example 2.1.** A diagonal map with eigenvalue functions \(\lambda_1,\ldots,\lambda_m:\mathbb T\to\mathbb T\) sends \(f\) to \(\operatorname{diag}(f(\lambda_1),\ldots,f(\lambda_m))\). Its K_0 map is multiplication by \(m\). Its K_1 map is multiplication by

\[
D=\sum_{j=1}^m\deg(\lambda_j).
\tag{2.6}
\]

This follows by taking the determinant of the image of (2.2). In particular \(m\) repeated copies of \(f(z^d)\) give maps \(m\) and \(md\). If the symbol “degree” denotes the total determinant degree \(D\), one must not multiply it by \(m\) again.

## 3. The correct Bunce–Deddens connecting maps

For \(m\geq2\), let \(C_m(z)\) be the unitary cyclic matrix on basis \(e_0,\ldots,e_{m-1}\) defined by

\[
\begin{aligned}
C_m(z)e_j&=e_{j+1},\\
&\quad0\leq j<m-1,\\
C_m(z)e_{m-1}&=ze_0.
\end{aligned}
\tag{3.1}
\]

Its powers and determinant satisfy

\[
\begin{gathered}
C_m(z)^m=zI_m,\\
\det C_m(z)=(-1)^{m-1}z.
\end{gathered}
\tag{3.2}
\]

The first identity follows by going once around the cycle. In the determinant expansion the single nonzero permutation is that cycle, with sign \((-1)^{m-1}\), proving the second.

Define the unital homomorphism

\[
\begin{gathered}
\Phi_{n,m}:M_n(C(\mathbb T))\\
\longrightarrow M_{nm}(C(\mathbb T)),\\
\Phi_{n,m}(e_{ij}z^r)=e_{ij}\otimes C_m(z)^r.
\end{gathered}
\tag{3.3}
\]

Continuous functional calculus for the unitary \(C_m\), tensored with the matrix units, defines this map for all continuous functions. It is injective: as \(z\) ranges over the circle, the eigenvalues of \(C_m(z)\) range over the entire circle, and evaluation of an image at those eigenvalues recovers the values of the original matrix function.

**Lemma 3.1.** This is a standard \(m\)-times-around embedding. Its induced maps are

\[
(\Phi_{n,m})_{*0}=m,\qquad
(\Phi_{n,m})_{*1}=1.
\tag{3.4}
\]

*Proof.* To compare with the standard root presentation, put \(z=e^{2\pi it}\) and

\[
\lambda_j(t)=e^{2\pi i(t+j)/m},
\qquad 0\leq j<m.
\]

Let \(P\) be the cyclic permutation sending \(e_j\) to \(e_{j+1}\), with wraparound, and choose a continuous unitary path \(R(t)\) from \(I_m\) to \(P\). Such a path exists by diagonalizing \(P\) and choosing angles for its eigenvalues. The root map is

\[
\begin{gathered}
\Psi(f)(t)=R(t)F(t)R(t)^*,\\
F(t)=\operatorname{diag}_{0\leq j<m}f(\lambda_j(t)).
\end{gathered}
\tag{3.5}
\]

The endpoint values agree: at \(t=1\) the roots shift one place, and conjugation by \(P\) restores their original positions. Thus (3.5) is a matrix function on the circle. Tensor with \(M_n\) for a matrix-valued \(f\).

Let \(V(t)\) have \(j\)-th column

\[
m^{-1/2}
(1,\lambda_j^{-1},\ldots,\lambda_j^{-(m-1)})^{\mathsf T}.
\tag{3.6}
\]

The columns are orthonormal by the finite geometric sum, and the action in (3.1) shows they are eigenvectors with eigenvalues \(\lambda_j\). Also \(V(1)=V(0)P\). Therefore \(W(t)=V(t)R(t)^*\) has \(W(1)=W(0)\), and conjugation by this circle unitary takes \(\Psi(f)\) to \(f(C_m(z))\). This proves the asserted equivalence with the standard root embedding. For \(m=2\) it is the twice-around map of Blackadar, Exercise 10.11.4(a).

The image of a minimal constant projection has rank \(m\), giving the first map in (3.4). The image of (2.2) is \(C_m\) on its \(m\)-dimensional corner and the identity on the complement. Equation (3.2) gives determinant winding \(1\), proving the second map. \(\square\)

Let \(n_1\mid n_2\mid\cdots\) be unbounded, omitting repeated terms, and write \(m_k=n_{k+1}/n_k\). The **Bunce–Deddens algebra of type \(q\)** is the limit \(B_q\) of these standard embeddings, where \(q\) is the supernatural number recorded by the \(n_k\).

**Theorem 3.2.** With their indicated order and unit,

\[
\begin{gathered}
K_0(B_q)=\mathbb Z(q),\qquad [1]=1,\\
K_0(B_q)^+=\mathbb Z(q)\cap[0,\infty),\\
K_1(B_q)=\mathbb Z.
\end{gathered}
\tag{3.7}
\]

*Proof.* The K_0 system is \(\mathbb Z\xrightarrow{m_k}\mathbb Z\), and \(r\mapsto r/n_k\) gives coherent injections into \(\mathbb Q\). Their union is \(\mathbb Z(q)\): a positive denominator divides some \(n_k\) exactly when all its prime exponents are bounded by those of \(q\). The finite list of primes in a denominator permits choosing one common stage. Stage positive ranks give the stated cone and stage units give \(1\). The K_1 connecting maps are all the identity by Lemma 3.1, so their limit is \(\mathbb Z\). \(\square\)

For \(q=2^\infty\), this yields \(K_0(B_q)=\mathbb Z[1/2]\) and \(K_1(B_q)=\mathbb Z\). Unboundedness matters: a stationary finite circle-matrix algebra has many traces and is not the simple infinite Bunce–Deddens algebra.

The doubled pullback \(f(z)\mapsto\operatorname{diag}(f(z^2),f(z^2))\), appearing under this name in Emerson, Example 1.7.11, is a different system. Its maps are \(2\) and \(4\), so both group limits are \(\mathbb Z[1/2]\). A nonconstant scalar matrix function becomes \(f(z^{2^l})I\) at later stages; injectivity preserves it, and it remains central in the limit. Thus that system has a nontrivial center and cannot be the simple \(B_{2^\infty}\) computed here.

## 4. Simplicity, the unique trace and three trace ranges

**Proposition 4.1.** \(B_q\) is simple, unital and stably finite, and has exactly one tracial state.

*Proof of simplicity.* A composition of the root embeddings from size \(n_k\) to size \(n_l\), with \(M=n_l/n_k\), is fiberwise unitarily equivalent to the direct sum of evaluations at all \(M\)-th roots of \(z\). This follows by repeatedly taking the roots in (3.5); taking an \(m\)-th root and then an \(r\)-th root enumerates each \(mr\)-th root once.

If \(b\) is a nonzero positive matrix function at stage \(k\), there is an open arc on which \(b(w)\neq0\). For large enough \(M\), every set of \(M\)-th roots of any \(z\) meets that arc: their angular spacing is \(2\pi/M\). The later image \(c(z)\) is consequently nonzero at every fiber.

Such a positive \(c\in M_N(C(\mathbb T))\) is full. With constant matrix units,

\[
\sum_{i,j}e_{ij}c\,e_{ji}
=\operatorname{Tr}(c)\,I_N.
\tag{4.1}
\]

The scalar continuous function \(\operatorname{Tr}(c)\) is strictly positive everywhere, hence invertible. Thus the ideal generated by \(c\) contains the identity.

To apply this to an arbitrary nonzero ideal \(J\subset B_q\), choose \(a\in J_+\) of norm one and a positive stage element \(b\) with \(\|a-b\|<\varepsilon<1/4\). Such positive approximations follow by approximating \(a^{1/2}\) by a stage element and taking its square modulus. In the quotient by \(J\), \(b\) has norm less than \(\varepsilon\). Therefore \(d=(b-\varepsilon)_+\) lies in \(J\), by quotient functional calculus, and is nonzero because \(\|b\|>1-\varepsilon>\varepsilon\). It is a stage element. Its image is full at a later stage by the previous paragraphs, so \(1\in J\). This proves simplicity. Unitality follows from the unital connecting maps.

*Proof of the trace assertion.* A tracial state on \(M_n(C(\mathbb T))\) has the form

\[
\tau_n(f)=\frac1n\int_{\mathbb T}
\operatorname{Tr}(f(w))\,d\mu_n(w)
\tag{4.2}
\]

for a probability measure \(\mu_n\). To prove this, matrix-unit cyclicity annihilates off-diagonal entries and gives equal functionals on each diagonal entry. Their sum is the restriction to the scalar center, a state on \(C(\mathbb T)\), hence integration against \(\mu_n\). The factor \(1/n\) is forced by \(\tau_n(1)=1\).

For the embedding of multiplicity \(m\), normalized matrix trace over its eigenvalue blocks averages over all \(m\)-th roots. Define

\[
(L_m h)(z)=\frac1m\sum_{w^m=z}h(w).
\tag{4.3}
\]

Compatibility of stage traces says \(\int h\,d\mu_k=\int L_{m_k}h\,d\mu_{k+1}\). On a Fourier monomial,

\[
L_m(w^r)=
\begin{cases}
0,&m\nmid r,\\
z^{r/m},&m\mid r.
\end{cases}
\tag{4.4}
\]

The finite root-of-unity sum proves this for every integer \(r\), positive or negative. For a composition replace \(m\) by \(M=n_l/n_k\). Given nonzero \(r\), choose \(l\) with \(M>|r|\). Then \(M\nmid r\), so compatibility forces \(\int w^r\,d\mu_k=0\). Fejér density of Laurent polynomials implies that every \(\mu_k\) is Haar probability measure. Conversely Haar measures satisfy (4.3)'s compatibility, by integration of the same monomials and density. Thus their stage traces define a bounded positive trace on the dense union and extend uniquely to \(B_q\). Every tracial state has these restrictions, proving uniqueness.

Finally this trace is faithful. Its null space \(\{x:\tau(x^*x)=0\}\) is a closed two-sided ideal: the trace identity and the C*-norm bound give stability under multiplication on either side. Simplicity and \(\tau(1)=1\) make it zero. Its unnormalized matrix extension is faithful as well, since \(\tau_N(x^*x)\) is the sum of the positive values \(\tau(x_{ij}^*x_{ij})\). If \(v^*v=1\) in any matrix algebra, cyclicity gives \(\tau_N(1-vv^*)=0\); faithfulness implies \(vv^*=1\). Hence \(B_q\) is stably finite. \(\square\)

The pairing of this trace is

\[
\tau_*:\mathbb Z(q)\longrightarrow\mathbb R,
\qquad \tau_*(x)=x,
\tag{4.5}
\]

because a rank \(r\) constant projection at stage \(k\) has trace \(r/n_k\). There are three distinct ranges:

\[
\begin{gathered}
\tau(\operatorname{Proj}(B_q))
=\mathbb Z(q)\cap[0,1],\\
\tau_\infty(\operatorname{Proj}(M_\infty(B_q)))\\
=\mathbb Z(q)\cap[0,\infty),\\
\tau_*(K_0(B_q))=\mathbb Z(q).
\end{gathered}
\tag{4.6}
\]

Every value in the first two sets is realized by an appropriate constant stage projection, with matrix enlargement if necessary. Conversely any projection gives a positive K_0 class, and an ordinary projection also has trace at most one. Negative values arise only from differences in K_0. The ordinary projection range is also the scale, because its classes are identified with their rational values by (4.5).

## 5. Which ordered groups occur?

An ordered abelian group here has a proper positive cone and is **directed**:

\[
\begin{gathered}
G^+\cap(-G^+)=\{0\},\\
G^+-G^+=G.
\end{gathered}
\tag{5.1}
\]

This is the convention of Blackadar, Definition 6.2.1. It is **unperforated** if \(ng\geq0\), for a positive integer \(n\), implies \(g\geq0\). It has **Riesz interpolation** if \(a_1,a_2\leq b_1,b_2\) implies the existence of \(c\) with \(a_1,a_2\leq c\leq b_1,b_2\).

A dimension group is an ordered inductive limit of simplicial groups \((\mathbb Z^{r_k},\mathbb Z_+^{r_k})\) and positive maps; the maps need not be injective.

**Proposition 5.1 (the easy direction).** Every sequential dimension group is countable, directed, unperforated and has interpolation.

*Proof.* It is a countable union of images of countable groups. Every stage vector is a difference of two positive coordinate vectors, so the limit is directed.

The positive cone is proper. If \(g\) and \(-g\) both have positive representatives, move those representatives to one stage and then farther until their sum, which is zero in the limit, is zero at the stage. The sum of two nonnegative integer vectors is zero only if both are zero. Thus \(g=0\).

If \(ng\geq0\), represent \(g\) at one stage and a positive representative of \(ng\) at a later stage. Their equality in the limit holds at some still later stage. There \(n\) times the vector representing \(g\) is nonnegative, so that vector is nonnegative. Its limit class is \(g\), proving unperforation.

For interpolation, represent all four elements at a common stage. Each of the four positive differences \(b_j-a_i\) has a positive representative later. Moving farther makes its equality with the difference of the chosen representatives hold. One common stage works for the finitely many inequalities. There define \(c\) coordinatewise as \(\max(a_1,a_2)\). Each coordinate is at most both upper coordinates, so \(a_i\leq c\leq b_j\). Passing to the limit completes the proof. \(\square\)

Directedness is already part of Blackadar's meaning of “ordered group.” Without it, the zero cone on \(\mathbb Z\) would satisfy unperforation and interpolation but could not be a simplicial limit with the generating positive cone (5.1).

For irrational \(\theta\), take

\[
G_\theta=\mathbb Z+\theta\mathbb Z\subset\mathbb R
\tag{5.2}
\]

with the inherited order and unit \(1\). This group is countable and directed. It is unperforated because the real order is, and interpolation is obtained by taking the maximum of the two lower bounds. Every positive element is an order unit, so the group is simple.

It is dense in \(\mathbb R\). Among \(N+1\) fractional parts of multiples of \(\theta\), two are within \(1/N\). Their difference gives a nonzero element of \(G_\theta\) of absolute value less than \(1/N\). Integer multiples of arbitrarily small positive such elements approximate every real number. Theorem 5.7 below, applied to the one-point trace simplex and this dense inclusion, constructs a simple unital AF-algebra with ordered K_0 equal to \(G_\theta\) and order unit \(1\). It identifies an AF-algebra; it does not identify the irrational rotation algebra, whose K_1 will be computed later.

### Refining a positive relation

The converse of Proposition 5.1 needs a construction, rather than an appeal to classification. The following refinement argument is the positive-kernel method behind the Effros–Handelman–Shen theorem.

**Lemma 5.2 (Riesz decomposition).** In an interpolation group, if \(0\leq x\leq y_1+\cdots+y_m\), with every \(y_j\geq0\), then

\[
\begin{gathered}
x=x_1+\cdots+x_m,\\
0\leq x_j\leq y_j.
\end{gathered}
\tag{5.3}
\]

*Proof.* For two summands, interpolate between the lower bounds \(0,x-y_2\) and upper bounds \(x,y_1\). All four inequalities hold. The interpolant \(x_1\) satisfies \(0\leq x_1\leq y_1\), while \(x_2=x-x_1\) satisfies \(0\leq x_2\leq y_2\). Induction on the number of summands proves (5.3). In particular, an equality of two finite sums of positive elements has a positive rectangular refinement: split the first element against the second sum, subtract its pieces, and repeat. \(\square\)

**Lemma 5.3 (positive factorization).** Let \(G\) be an unperforated interpolation group. For a positive homomorphism \(\phi:\mathbb Z^r\to G\) and \(z\in\ker\phi\), there are a simplicial group \(\mathbb Z^s\) and positive homomorphisms

\[
\begin{gathered}
\mathbb Z^r\xrightarrow{R}\mathbb Z^s
\xrightarrow{\psi}G,\\
\phi=\psi R,\qquad Rz=0.
\end{gathered}
\tag{5.4}
\]

The matrix \(R\) has nonnegative integer entries. A single such factorization can kill any finite set of elements of \(\ker\phi\).

*Proof.* If \(z=0\), take the identity factorization. Unperforation implies torsion-freeness: if \(ng=0\), apply it to \(g\) and \(-g\), and use properness of the cone. Write \(z=\sum c_i e_i\) and \(g_i=\phi(e_i)\geq0\). We induct on the pair consisting of the largest absolute value \(N\) of a nonzero coefficient and the number of coefficients having absolute value \(N\), ordered lexicographically.

If all nonzero coefficients have the same sign, the positive relation forces \(|c_i|g_i=0\) term by term. Hence those \(g_i\) vanish. Delete their coordinates and retain the zero-coefficient coordinates; this is the required positive factorization. The zero relation needs no deletion.

Otherwise, replace \(z\) by \(-z\) if necessary so that one coefficient is \(c_k=N>0\). Index the negative coefficients as \(-q_j\), and put \(h_j=\phi(e_j)\) for their corresponding generators. Every \(q_j\) lies between 1 and \(N\). The relation gives

\[
\begin{aligned}
Ng_k&\leq\sum_j q_jh_j\\
&\leq N\sum_j h_j.
\end{aligned}
\tag{5.5}
\]

Unperforation applied to \(N(\sum h_j-g_k)\) gives \(g_k\leq\sum h_j\). Lemma 5.2 supplies \(x_j\) with

\[
g_k=\sum_jx_j,\qquad 0\leq x_j\leq h_j.
\tag{5.6}
\]

Introduce free positive generators mapped to \(x_j\) and \(h_j-x_j\), and retain generators for every original coordinate other than \(k\) and the negative coordinates. Define a positive integer matrix \(R_0\) by sending \(e_k\) to the sum of the \(x_j\)-coordinates, each negative-coordinate \(e_j\) to its two new coordinates, and every retained \(e_i\) to its own coordinate. The resulting positive map \(\psi_0\) satisfies \(\phi=\psi_0R_0\).

In \(R_0z\), the coefficient of the \(x_j\)-coordinate is \(N-q_j\); the coefficient of the \(h_j-x_j\)-coordinate is \(-q_j\). The other coefficients are unchanged. Thus no absolute value exceeds \(N\), no new coefficient of absolute value \(N\) is introduced in place of a smaller one, and the chosen coefficient \(N\) has disappeared. The induction pair strictly decreases. Applying the induction hypothesis to \(\psi_0,R_0z\) and composing its matrix with \(R_0\) proves (5.4). Both positive and negative coefficients, including a tie for the largest absolute value, are covered by this decrease.

For finitely many kernel elements, kill the first, apply the same construction to the image of the second, and continue. Composition preserves every relation already killed. \(\square\)

### Constructing the simplicial system

**Theorem 5.4 (Effros–Handelman–Shen).** A countable directed ordered abelian group is a sequential dimension group if and only if it is unperforated and has Riesz interpolation.

*Proof of the converse.* Enumerate \(G^+\) as \(g_1,g_2,\ldots\), allowing repetitions. Starting with a finite-rank free positive map \(\phi_k:F_k\to G\), append one free generator with image \(g_k\):

\[
\begin{gathered}
\phi'_k:F_k\oplus\mathbb Z\longrightarrow G,\\
\phi'_k(x,m)=\phi_k(x)+mg_k.
\end{gathered}
\tag{5.7}
\]

Its kernel is finitely generated. Indeed, every subgroup of \(\mathbb Z^n\) is finitely generated: induct on \(n\), choose an element generating its nonzero first-coordinate image \(d\mathbb Z\), and subtract multiples of it to reduce to a subgroup of \(\mathbb Z^{n-1}\). If that image is zero, reduce immediately.

Apply Lemma 5.3 to a finite generating set of \(\ker\phi'_k\). It factors \(\phi'_k=\phi_{k+1}R'_k\) through a simplicial \(F_{k+1}\), with \(R'_k(\ker\phi'_k)=0\). Restrict \(R'_k\) to \(F_k\) to obtain the connecting matrix \(R_k\). Start with \(F_1=\mathbb Z\), mapped positively to \(g_1\); the zero group can instead use zero stages.

The compatible maps induce a positive homomorphism

\[
\Phi:\varinjlim(F_k,R_k)\longrightarrow G.
\tag{5.8}
\]

Each enumerated \(g_k\) has a positive preimage, namely the image of the appended generator under \(R'_k\). Directedness makes \(\Phi\) surjective. If a class represented by \(x\in F_k\) maps to zero, then \((x,0)\in\ker\phi'_k\), so \(R_kx=0\) already at the next stage. Thus \(\Phi\) is injective. Finally, every element of \(G^+\) has a positive preimage, so the inverse also preserves order. This proves the converse; Proposition 5.1 proved the other direction. No connecting map is required to be injective. \(\square\)

**Theorem 5.5 (AF realization with an order unit).** Every group of Theorem 5.4 is the ordered \(K_0\)-group of a separable AF-algebra. If \(u\neq0\) is an order unit, the realization can be unital with \([1]=u\). If every nonzero positive element is an order unit, this unital realization is simple.

*Proof.* A nonnegative integer matrix \(R_k\) is realized by a homomorphism between finite sums of matrix algebras: repeat source block \(j\) exactly \((R_k)_{ij}\) times in target block \(i\). Choose the target matrix sizes at least as large as the sum of those source sizes with multiplicities, and fill unused dimensions with a zero corner. The resulting sequential AF limit has the ordered group (5.8), by (1.3) and the finite-stage positive-representative continuity of Lesson 5. Maps with kernels cause no problem: their finite-dimensional images in the limit form an increasing generating sequence, while Lesson 5 computes the group from the original stages.

For the unital assertion, a group order unit must be preserved by the matrices themselves. The interval \([0,u]\) generates \(G^+\): if \(0\leq g\leq Nu\), Lemma 5.2 splits \(g\) into \(N\) pieces in that interval. Enumerate the interval. Start with \(F_1=\mathbb Z\), \(d_1=1\), and \(\phi_1(1)=u\). Suppose \(F_k=\mathbb Z^{r_k}\) has a distinguished vector \(d_k\) whose coordinates are strictly positive integers and \(\phi_k(d_k)=u\).

Append two generators with images \(a\) and \(u-a\), where \(a\) is the next interval element. Kill the entire kernel of this enlarged map by Lemma 5.3. Its factorization \(R'\) in particular kills the relation

\[
\begin{aligned}
R'(d_k,0,0)&=R'(0,1,0)\\
&\quad+R'(0,0,1).
\end{aligned}
\tag{5.9}
\]

Set \(d_{k+1}=R'(d_k,0,0)\). Discard coordinates in which this vector is zero. All images of the old positive basis vectors vanish in those coordinates because every coordinate of \(d_k\) is positive. The two appended basis vectors also vanish there by (5.9) and nonnegativity. Thus restriction to the remaining coordinates preserves the factorization, all killed relations, and the positive representatives of both appended elements. The vector \(d_{k+1}\) has strictly positive coordinates, maps to \(u\), and satisfies \(R_kd_k=d_{k+1}\).

The injectivity and positive-surjectivity proof of Theorem 5.4 still applies, since the enumerated interval generates the positive cone. Use block sizes \((d_k)_j\). The equality \(R_kd_k=d_{k+1}\) says precisely that the repeated source blocks fill each target block. The algebra homomorphisms are therefore unital, with limit unit representing \(u\). This proves the unital assertion and its scale \([0,u]\).

For simplicity, a nonzero ideal of a unital AF-algebra contains a nonzero projection. To see this directly, approximate a norm-one positive ideal element by a positive element \(b\) of a finite-dimensional stage image within \(\varepsilon<1/4\). Quotient functional calculus puts the nonzero \((b-\varepsilon)_+\) in the ideal. Its finite spectrum gives a nonzero spectral projection in the same ideal.

Let that projection be \(p\). The AF cancellation and positive-monoid identification in (1.3) show that \([p]\neq0\). Since \([p]\) is an order unit, \([1]\leq N[p]\) for some \(N\). Represent \(N[p]-[1]\) by a matrix projection \(q\). Injectivity of the AF projection monoid into its Grothendieck group gives stable Murray–von Neumann equivalence between \(1\oplus q\) and \(N\) copies of \(p\). The latter belongs to a matrix algebra over the ideal, so equivalence puts \(1\oplus q\), and hence \(1\), in that ideal. It is the whole algebra. \(\square\)

### Prescribing the trace simplex

The range construction also permits infinitesimal group elements and an arbitrary metrizable Choquet simplex. Here is the full analytic ingredient needed for that assertion.

For a nonempty compact convex set \(\Delta\) in a locally convex Hausdorff real vector space, put \(V=\operatorname{Aff}(\Delta)\), the real Banach space of continuous affine functions with its uniform norm. Use the ordered-cone definition of a **Choquet simplex**: the dual positive cone makes \(V^*\) a lattice-ordered real vector space. This is the standard cone definition described in Blackadar's *Classification of C*-Algebras*, I.3.3.50–I.3.3.52; it imposes no closedness assumption on the extreme boundary. We verify below that the normalized positive dual base is exactly \(\Delta\).

**Lemma 5.6 (approximate affine interpolation).** If \(\Delta\) is a Choquet simplex and \(a_1,a_2,b_1,b_2\in V\) satisfy \(a_i\leq b_j\) pointwise, then for every \(\varepsilon>0\) there is \(f\in V\) with

\[
\begin{gathered}
a_i-\varepsilon1<f<b_j+\varepsilon1,\\
i,j=1,2.
\end{gathered}
\tag{5.10}
\]

*Proof.* We first give the separation argument being used. In a real Banach space, let \(P\) be a convex cone with nonempty interior, \(L\) a linear subspace, and \(d\) a vector. If \((L-d)\cap\operatorname{int}P\) is empty, there is a nonzero continuous functional \(\Lambda\), nonnegative on \(P\), annihilating \(L\), with \(\Lambda(d)\geq0\).

For completeness, the open convex set \(U=\operatorname{int}P-L+d\) does not contain zero. Choose \(v\in U\); the open convex neighborhood \(C=U-v\) has a continuous sublinear Minkowski functional \(p\), with \(C=\{x:p(x)<1\}\) and \(p(-v)\geq1\). The linear functional taking \(-v\) to 1 on its one-dimensional span is dominated by \(p\). Its dominated extension to the entire space follows by the real Hahn–Banach argument: to adjoin a vector \(z\) to a current subspace \(M\), choose its value between

\[
\begin{gathered}
\sup_{m\in M}\{\ell(m)-p(m-z)\},\\
\inf_{m\in M}\{p(m+z)-\ell(m)\}.
\end{gathered}
\tag{5.11}
\]

The lower bound is at most the upper bound because \(\ell(m+n)\leq p(m+n)\leq p(m-z)+p(n+z)\). Both bounds are finite, using \(m=0\) and these inequalities. The chosen value defines a dominated extension, for positive and negative scalar multiples of \(z\); a maximal extension by Zorn's lemma has the whole space as domain. Domination in both directions gives continuity. This extension is strictly negative on \(U\), since it takes \(v\) to \(-1\) and values less than 1 on \(C\). Negate it to obtain \(\Lambda\). Translating arbitrarily along \(L\) shows \(\Lambda L=0\); scaling a fixed interior cone vector to infinity gives positivity, and scaling it to zero gives \(\Lambda d\geq0\). Positivity extends from the interior to all of \(P\) by adding a vanishing interior vector. This proves the separation assertion.

Apply it in \(V^4\), with its pointwise positive cone,

\[
\begin{gathered}
L=\{(f,f,-f,-f):f\in V\},\\
d=\begin{pmatrix}
a_1-\varepsilon1\\
a_2-\varepsilon1\\
-b_1-\varepsilon1\\
-b_2-\varepsilon1
\end{pmatrix}.
\end{gathered}
\tag{5.12}
\]

If (5.10) failed, separation would give positive functionals \(\lambda_1,\lambda_2,\mu_1,\mu_2\) with \(\lambda_1+\lambda_2=\mu_1+\mu_2\). Since \(V^*\) is a lattice, it has interpolation, so Lemma 5.2 refines this equality as \(\lambda_i=\sum_j\nu_{ij}\), \(\mu_j=\sum_i\nu_{ij}\), with every \(\nu_{ij}\geq0\). Consequently

\[
\begin{aligned}
\Lambda d
&=\sum_{i,j}\nu_{ij}(a_i-b_j)\\
&\quad-\varepsilon\sum_i\lambda_i(1)\\
&\quad-\varepsilon\sum_j\mu_j(1)<0.
\end{aligned}
\tag{5.13}
\]

The first sum is nonpositive. The second is strictly negative: a nonzero positive functional on \(V\) has positive value on 1, because \(|\ell(f)|\leq\|f\|\ell(1)\). This contradicts \(\Lambda d\geq0\), proving the lemma. \(\square\)

**Theorem 5.7 (simple AF and trace-simplex range).** Let \(G\) be a countable torsion-free abelian group, \(\Delta\) a metrizable Choquet simplex, and \(\rho:G\to\operatorname{Aff}(\Delta)\) a homomorphism with uniformly dense range. Give \(G\) the strict cone, where \(\rho(g)>0\) means positivity at every point of \(\Delta\)

\[
\begin{gathered}
G^+=\{0\}\cup P_\rho,\\
P_\rho=\{g\in G:\rho(g)>0\}.
\end{gathered}
\tag{5.14}
\]

Then \(G\) is a simple dimension group. If \(\rho(u)=1\), it is the scaled ordered \(K_0\)-group of a simple unital AF-algebra \(A\), unique up to isomorphism, with \(T(A)\) affinely homeomorphic to \(\Delta\). Under this homeomorphism, the trace pairing of \(g\) is precisely \(\rho(g)\).

*Proof.* The cone is closed under addition and is proper. It is unperforated: if \(ng\) is nonzero positive, divide the strictly positive function \(\rho(ng)\) by \(n\); if \(ng=0\), torsion-freeness gives \(g=0\). It is directed even without a specified \(u\): density supplies a \(v\) with \(\rho(v)>0\) everywhere, and sufficiently large multiples of \(v\) dominate any given \(\rho(g)\). Every nonzero positive \(v\) is an order unit by the same uniform lower-bound argument.

For interpolation, suppose \(a_i\leq b_j\) in \(G\). If one lower bound equals one upper bound, that element interpolates all four. Otherwise every \(\rho(b_j-a_i)\) is strictly positive. Compactness gives a common lower bound \(\delta>0\) for these four functions. Apply Lemma 5.6 to the shifted lower functions \(\rho(a_i)+\delta/3\) and upper functions \(\rho(b_j)-\delta/3\), with error \(\delta/12\). The resulting affine \(f\) is separated from the original bounds by more than \(\delta/4\). Choose \(c\in G\) with \(\|\rho(c)-f\|<\delta/8\). Then both \(\rho(c-a_i)\) and \(\rho(b_j-c)\) are strictly positive, giving the required interpolant. Theorem 5.4 now applies.

When \(\rho(u)=1\), Theorem 5.5 constructs the simple unital AF-algebra. Uniqueness uses the already proved scaled AF classification in §1. It remains to prove the trace simplex and the precise pairing, rather than infer them from existence.

For a group state \(s:G\to\mathbb R\), take positive integers \(M,N\) with \(M/N>\|\rho(g)\|\). Both \(Mu+Ng\) and \(Mu-Ng\) are positive, so \(|s(g)|\leq M/N\). Letting this rational bound decrease gives

\[
|s(g)|\leq\|\rho(g)\|.
\tag{5.15}
\]

Thus \(s\) annihilates \(\ker\rho\) and defines a bounded additive functional on \(\rho(G)\). Extend it continuously to the dense real Banach space \(V\). The extension \(\ell\) is additive and continuous, hence real-linear, with \(\ell(1)=1\). It is positive: approximate a strictly positive function by elements of \(\rho(G)\), then obtain positivity on any nonnegative function by adding a positive constant and taking a limit.

Every such \(\ell\) is evaluation at a point of \(\Delta\). Indeed, for finitely many \(f_1,\ldots,f_m\in V\), the vector \((\ell(f_1),\ldots,\ell(f_m))\) lies in their compact convex joint range on \(\Delta\). Otherwise finite-dimensional separation gives a nonnegative affine function on \(\Delta\) with negative \(\ell\)-value. That separation can be seen by choosing a nearest point of the compact convex joint range: the vector from that point to the proposed vector strictly separates them. Compactness and the finite-intersection property therefore give one \(x\in\Delta\) with \(\ell(f)=f(x)\) for every \(f\in V\). Continuous affine functions separate points, so \(x\) is unique. Conversely evaluation at any \(x\) gives a group state. Density makes the evaluation map \(\Delta\to S(G,u)\) injective; it is continuous and onto, and hence an affine homeomorphism from compact \(\Delta\) to its Hausdorff image.

Finally, the group-state/trace correspondence for the unital AF system is explicit. At a stage \(\bigoplus_jM_{d_j}\), set the trace weight of a minimal projection in block \(j\) equal to the state value of its \(K_0\)-class, and use that weight times the unnormalized matrix trace on the block. Positivity and \(\sum_jd_js([e_j])=1\) give a tracial state. Connecting multiplicities make these stage traces compatible. Their uniformly bounded functionals extend to the AF limit. Conversely every tracial state has these weights by matrix-unit cyclicity, so the correspondence is bijective. Pointwise convergence of group states gives convergence on every finite stage and then on the entire algebra by norm density; convergence of traces gives convergence on projection classes. This proves the affine homeomorphism and identifies the trace pairing with \(\rho\). \(\square\)

In particular, every metrizable Choquet simplex occurs as \(T(A)\) for a simple unital AF-algebra. To see the required separability explicitly, fix a countable dense set in the compact metric space \(\Delta\). Finite minima of functions \(r+Ld(x,x_j)\), with rational \(r\), positive rational \(L\), and points \(x_j\) from that set, form a countable dense family in real \(C(\Delta)\): first approximate a uniformly continuous function by its infimum \(\inf_y(f(y)+Ld(x,y))\) for large \(L\), then approximate that infimum using a finite sufficiently fine net and rational values. The infimum converges uniformly to \(f\), since near points use uniform continuity and distant points cannot lower it when \(L\) is large. A subspace of a separable metric space is separable by choosing a point from each nonempty intersection with a countable base. Thus \(\operatorname{Aff}(\Delta)\) has a countable dense family. Take its rational linear span together with 1. This countable torsion-free group, its inclusion map and its unit satisfy Theorem 5.7. Infinitesimals are also permitted by that theorem: \(\rho\) need not be injective.

## 6. Exercises with complete solutions

**Exercise 16.1.** Compute K_1 of a UHF algebra and give its normalized ordered K_0.

*Solution.* Each finite matrix stage has K_1 zero by its eigenangle contraction, so continuity gives K_1 zero. A minimal projection at size \(n_k\) has class \(1\) in the integer stage coordinate, and an embedding of multiplicity \(m_k\) sends it to \(m_k\). The coherent rational coordinate is \(r/n_k\), giving \(\mathbb Z(q)\). Nonnegative ranks give its ordinary positive cone, stage units give \(1\), and ranks between \(0\) and \(n_k\) give \(\mathbb Z(q)\cap[0,1]\) as scale. This also covers a finite supernatural number, when the UHF algebra is a single finite matrix algebra.

**Exercise 16.2.** Compute the two groups of the Bunce–Deddens algebra of type \(2^\infty\), checking both connecting maps.

*Solution.* In its correct embedding a minimal projection maps to a rank-two projection, so K_0 multiplies by \(2\). Its stable K_1 generator maps to

\[
C_2(z)=\begin{pmatrix}0&z\\1&0\end{pmatrix}
\]

on a two-dimensional corner, with identity elsewhere. Its determinant is \(-z\), of winding one, so K_1 multiplies by \(1\). Therefore the limits are \(\mathbb Z[1/2]\) and \(\mathbb Z\). The normalized unit is \(1\), and its positive cone is the nonnegative dyadic rationals. In the root presentation the two eigenvalues are \(e^{\pi it}\) and \(-e^{\pi it}\), whose product is \(-e^{2\pi it}\); this independently verifies the degree and its sign.

**Exercise 16.3.** Prove unperforation and interpolation for a dimension group with possibly noninjective connecting maps.

*Solution.* Equality of finitely many classes in an algebraic inductive limit is equality at some common later stage. If \(ng\) is positive, carry a representative of \(g\) and a positive representative of \(ng\) there; the equation \(n x=y\geq0\) in integer coordinates forces \(x\geq0\). For four interpolation inequalities, carry the four representatives and the four positive differences to one stage where all defining equations hold. The coordinate maximum of the lower representatives lies below both upper ones. Its image is the required interpolant. The same finite-stage argument with two positive representatives of \(g,-g\) proves properness, and positive/negative coordinate decomposition proves directedness. No map is assumed injective.

**Exercise 16.4.** Prove uniqueness of the dyadic Bunce–Deddens trace and determine its projection ranges.

*Solution.* Restrict any tracial state to a stage; matrix-unit cyclicity puts it in form (4.2). Pulling back from a stage \(l\) to a stage \(k\) averages over all \(2^{l-k}\)-th roots. For every nonzero Fourier exponent \(r\), choose \(2^{l-k}>|r|\); formula (4.4) makes that coefficient zero. Laurent density forces Haar measure at every stage. Haar traces are compatible and extend continuously, so existence and uniqueness both hold. A rank \(s\) stage projection has trace \(s/2^k\). Every dyadic number in \([0,1]\) is realized this way, and no ordinary projection has trace outside that interval. Matrix enlargements realize every nonnegative dyadic number. Differences of these projection classes realize all of \(\mathbb Z[1/2]\) on K_0. These are exactly the three ranges (4.6).

**Exercise 16.5.** Compare the doubled square-pullback system with the true twice-around system.

*Solution.* For \(\Gamma(f)(z)=\operatorname{diag}(f(z^2),f(z^2))\), the minimal projection has doubled rank. The determinant of the image of its stable circle generator is \(z^4\), so its K_1 map is multiplication by \(4\). The two limits are \(\varinjlim(\mathbb Z,\times2)=\mathbb Z[1/2]\) and \(\varinjlim(\mathbb Z,\times4)=\mathbb Z[1/4]=\mathbb Z[1/2]\). The nonconstant central function \(zI\) remains central and nonconstant after every embedding, which is injective. Thus it gives a non-scalar central element of the limit, proving that limit is not simple. For the actual cyclic embedding the determinant is \(-z\), so K_1 is instead \(\mathbb Z\), and the root-sampling proof of Proposition 4.1 gives simplicity. Rank agreement alone did not identify the two systems.

## What this lesson imports and does not prove

Continuity, stabilization and the circle groups are imported at the exact lesson locators given above. The dimension-group identification, scaled AF classification, automorphism lifting and stable classification are the actual AF-algebras Theorem 7.5 and Theorem 8.3, Corollary 8.4 and Theorem 8.5. Theorems 5.4–5.7 prove the full dimension-group converse, unital and simple AF realization, and the prescribed trace-simplex range. Lemma 5.6 proves the needed affine interpolation directly from the ordered-cone definition of a Choquet simplex, including its separation argument. The measure representation of states on \(C(\mathbb T)\) and the bounded K_0 trace pairing are the imports used in [Traces, states and the pairing with K_0](KT-OPK-13.md). Fejér approximation is the proof in Lesson 10, §5. We prove the AT connecting-map computations, Bunce–Deddens simplicity and unique trace here; no Pimsner–Voiculescu sequence or classification of general AT-algebras is assumed.

## References

- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998, Exercise 7.7.5, printed pp. 57–58. [Author corrected edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Theorem 1.2 supplies a complete proof, including the continuous asymptotic unitary path, with the exact AF cancellation prerequisite.

- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998, Definition 6.2.1; complete §§7.1–7.6, especially Theorems 7.3.2, 7.4.1 and 7.4.3; Exercise 10.11.4(a)–(c). [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Theorems 7.4.1 and 7.4.3 supply the freely accessible range statements; the complete constructive proofs used here are given in §5.
- B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, V.2 overview and V.2.4, for ordered K_0 and traces.
- H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, 2024, §1.7. The doubled square-pullback of Example 1.7.11 is distinguished from Blackadar's standard twice-around embedding by its actual K_1 map.

- E. G. Effros, D. E. Handelman and C.-L. Shen, *Dimension groups and their affine representations*, American Journal of Mathematics 102 (1980), 385–407, [historical article](https://doi.org/10.2307/2374244). Historical attribution, also recorded in Blackadar’s freely accessible edition, §7.4. The complete integer-kernel refinement and AF/trace-simplex arguments used here are written out in Theorems 5.4–5.7.
- B. Blackadar, *Classification of C*-Algebras*, incomplete preliminary edition, 4 June 2025, I.3.3.50–I.3.3.52 and I.3.3.56–I.3.3.58, [author’s edition](https://www.bruceblackadar.com/Mathematics/Class.pdf). These passages supply the Choquet cone definition and strict-order range statements. Section 5 proves the affine interpolation, AF realization and trace correspondence used here directly from that definition.
- David E. Handelman, *Real dimension groups*, arXiv:1102.2964v1, Lemmas 3–4 and their proofs, pp. 2–3. [Freely readable versioned paper](https://arxiv.org/pdf/1102.2964v1#page=2). Its ordered-vector-space factorization is a comparison: scaling and division there do not replace the integral refinement proof of Lemma 5.3 here.

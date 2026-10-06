# Discriminants and integral bases

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

A generator of a number field gives a convenient rational basis. It need not give every algebraic integer. For example, the powers of \(\sqrt5\) generate \(\mathbf Q(\sqrt5)\), but their integer span misses \((1+\sqrt5)/2\). We need a way to measure this defect and then decide whether any integers remain missing.

The discriminant does both jobs. It is a determinant built from traces. Changing a lattice multiplies its discriminant by the square of its index. Consequently, a single computation confines the possible defect to finitely many primes. Dedekind's criterion then tests those primes individually. Along the way we prove the existence of integral bases and explain why every field discriminant has a prescribed sign and a restricted residue modulo \(4\).

We assume the results of *Algebraic integers and rings of integers*, together with elementary module theory: subgroups of finite free abelian groups are free, and integer matrices admit Smith normal form. In particular, sums and products of algebraic integers are integral, integral elements have integral traces and norms, and every algebraic number has a nonzero integer multiple that is integral. Precise statements and references for the facts used without proof appear below.

Basic references are [Milne ANT], [Stacks] and [Hecke 1923]. The proofs and computations here form a complete path through the topic. For a number field \(K\), put \(n=[K:\mathbf Q]\) and write \(\mathcal O_K\) for its ring of integers. All polynomial discriminants in this lesson concern monic polynomials.

## A determinant that measures a basis

For a finite extension \(L/k\), the trace \(\operatorname{Tr}_{L/k}(x)\) is the trace of multiplication by \(x\) on the \(k\)-vector space \(L\). The symmetric bilinear form

\[
B(x,y)=\operatorname{Tr}_{L/k}(xy)
\]

is the **trace form**. For an ordered \(k\)-basis \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_n)\), define

\[
d(\boldsymbol\alpha)=\det\bigl(\operatorname{Tr}_{L/k}(\alpha_i\alpha_j)\bigr).
\]

**Proposition 2.1.** Suppose \(L/k\) is finite and separable. Let \(\sigma_1,\ldots,\sigma_n\) be its embeddings into an algebraic closure of \(k\). Then

\[
d(\boldsymbol\alpha)=\det\bigl(\sigma_i(\alpha_j)\bigr)^2\ne0.
\]

In particular, the trace form is nondegenerate.

**Proof.** Set \(S=(\sigma_i(\alpha_j))\). The formula for trace as a sum over embeddings gives the Gram matrix \(S^{\mathsf T}S\), whose determinant is \((\det S)^2\).

Choose a primitive element \(\theta\) for \(L/k\). Its conjugates \(\theta_1,\ldots,\theta_n\) are distinct. For the basis \(1,\theta,\ldots,\theta^{n-1}\), the embedding matrix is Vandermonde. Its determinant is

\[
\prod_{i<j}(\theta_j-\theta_i)\ne0.
\]

Indeed, that determinant is alternating in the \(\theta_i\), so each displayed difference divides it; comparison of degrees and the leading term gives the formula. An arbitrary basis is obtained from this one by an invertible matrix over \(k\). Its embedding matrix is therefore also invertible. The Gram matrix is invertible, which is exactly nondegeneracy. \(\square\)

The same calculation gives the basic change of basis rule. If

\[
\beta_j=\sum_i\alpha_i c_{ij},\qquad C=(c_{ij}),
\]

then the new Gram matrix is \(C^{\mathsf T}GC\), and hence

\[
d(\boldsymbol\beta)=(\det C)^2d(\boldsymbol\alpha). \tag{1}
\]

**Proposition 2.2.** Suppose \(L=k(\theta)\) is separable of degree \(n\), with monic minimal polynomial \(f\). Then

\[
\begin{aligned}
d(1,\theta,\ldots,\theta^{n-1})
&=\prod_{i<j}(\theta_i-\theta_j)^2\\
&=(-1)^{n(n-1)/2}N_{L/k}(f'(\theta)).
\end{aligned}
\]

**Proof.** The first equality is the squared Vandermonde determinant. Since

\[
f'(\theta_i)=\prod_{j\ne i}(\theta_i-\theta_j),
\]

the product of these derivatives pairs one factor \(\theta_i-\theta_j\) with its negative for each unordered pair. Thus

\[
\prod_i f'(\theta_i)=(-1)^{n(n-1)/2}\prod_{i<j}(\theta_i-\theta_j)^2.
\]

The left side is the norm. \(\square\)

For any monic polynomial with roots \(\theta_i\), counted with multiplicity, we define \(\operatorname{disc}(f)\) by the product in Proposition 2.2. It vanishes exactly when two roots coincide. For an integral primitive element, it is the discriminant of its power basis. With the convention \(\operatorname{Res}(f,g)=\prod_i g(\theta_i)\) for monic \(f\), the precise relation is

\[
\operatorname{disc}(f)=(-1)^{n(n-1)/2}\operatorname{Res}(f,f').
\]

The sign factor matters already for a quadratic polynomial.

## From rational bases to integral bases

An **integral basis** is a \(\mathbf Z\)-basis of \(\mathcal O_K\). Its existence requires proof: knowing that all its elements are integral does not by itself bound their denominators in a rational basis.

**Theorem 2.3.** The additive group \(\mathcal O_K\) is free of rank \(n\). The integer

\[
d_K=d(\omega_1,\ldots,\omega_n)
\]

is independent of the integral basis. If \(\alpha_1,\ldots,\alpha_n\in\mathcal O_K\) form a rational basis and \(M=\bigoplus_i\mathbf Z\alpha_i\), then

\[
d(\alpha_1,\ldots,\alpha_n)=[\mathcal O_K:M]^2d_K. \tag{2}
\]

**Proof.** Start with any rational basis and multiply its elements by suitable positive integers to make them integral. Let \(M\) be their integer span and define its trace dual by

\[
M^\vee=\{x\in K:\operatorname{Tr}_{K/\mathbf Q}(xM)\subseteq\mathbf Z\}.
\]

The nondegenerate trace form gives a rational dual basis \(\alpha_1^\vee,\ldots,\alpha_n^\vee\), characterized by \(\operatorname{Tr}(\alpha_i\alpha_j^\vee)=\delta_{ij}\). Writing \(x\) in this dual basis shows directly that

\[
M^\vee=\bigoplus_j\mathbf Z\alpha_j^\vee.
\]

Products of integral elements have integer traces, so

\[
M\subseteq\mathcal O_K\subseteq M^\vee.
\]

A subgroup of the finite free abelian group \(M^\vee\) is free of rank at most \(n\). The contained rational basis forces its rank to be at least \(n\). This proves the first assertion.

Between two integral bases the change of basis matrix and its inverse have integer entries. Its determinant is therefore \(\pm1\), and (1) proves independence. Entries of the trace matrix are integers, so \(d_K\) is a nonzero integer.

Write \(\alpha_j=\sum_i\omega_i c_{ij}\). The integer matrix \(C\) has nonzero determinant. By Smith normal form, multiplication by integer invertible matrices reduces it to a diagonal matrix with nonzero diagonal entries \(s_i\). These operations preserve both the absolute determinant and the size of the quotient of the two lattices. For the diagonal matrix the quotient is \(\bigoplus_i\mathbf Z/s_i\mathbf Z\), so its size is \(\prod_i|s_i|=|\det C|\). Combining this equality with (1) proves (2). \(\square\)

For \(K=\mathbf Q(\alpha)\), with \(\alpha\) integral and minimal polynomial \(f\), the power basis spans \(A=\mathbf Z[\alpha]\). Therefore

\[
\operatorname{disc}(f)=[\mathcal O_K:A]^2d_K. \tag{3}
\]

A squarefree polynomial discriminant forces the index to be \(1\). The converse fails: \(\mathbf Z[\sqrt2]=\mathcal O_{\mathbf Q(\sqrt2)}\), although its discriminant is \(8\). More generally, only primes whose squares divide \(\operatorname{disc}(f)\) can divide the index.

There is even a finite search procedure. In coordinates relative to an integral rational basis, the condition defining \(M^\vee\) is \(Gx\in\mathbf Z^n\). Since \(G^{-1}=\operatorname{adj}(G)/\det G\),

\[
M\subseteq\mathcal O_K\subseteq M^\vee\subseteq d(M)^{-1}M.
\]

One can test the finitely many cosets of \(M\) in the last lattice for integrality. All representatives of one coset have the same integrality status, because they differ by an integral element. Exact minimal polynomials provide the test. This proves termination, although checking one prime at a time is much more efficient in the examples below.

## Two restrictions on discriminants

Let \((r_1,r_2)\) be the signature of \(K\): there are \(r_1\) real embeddings and \(r_2\) conjugate pairs of nonreal embeddings, with \(n=r_1+2r_2\).

**Theorem 2.4.** The field discriminant satisfies

\[
\operatorname{sign}(d_K)=(-1)^{r_2},\qquad d_K\equiv0\text{ or }1\pmod4.
\]

Both assertions also hold for the discriminant of any full lattice generated by integral elements of \(K\), including any order in \(K\).

**Proof.** Let \(S\) be its embedding matrix, ordered with the real embeddings first and conjugate pairs adjacent. Complex conjugation exchanges exactly \(r_2\) pairs of rows, so

\[
\overline{\det S}=(-1)^{r_2}\det S.
\]

The determinant is nonzero. It is real when \(r_2\) is even and purely imaginary when \(r_2\) is odd. Its square has the asserted sign.

For the congruence, write the determinant as \(P-N\), where \(P\) is the sum of the terms indexed by even permutations and \(N\) is the unsigned sum indexed by odd permutations. Permuting the rows either preserves \(P,N\) or exchanges them. Thus \(P+N\) and \(PN\) are invariant under every row permutation.

To see that they are rational, choose a primitive element \(\theta\) of \(K\), and express each basis element as a polynomial in \(\theta\) with rational coefficients. The rows are obtained by substituting the distinct conjugates of \(\theta\). Hence \(P+N\) and \(PN\) are symmetric polynomials with rational coefficients in those conjugates. The symmetric polynomial theorem puts both in \(\mathbf Q\). Their terms are products of algebraic integers, so both are algebraic integers and therefore belong to \(\mathbf Z\). Consequently,

\[
d=(P-N)^2=(P+N)^2-4PN\equiv(P+N)^2\equiv0\text{ or }1\pmod4.
\]

This is Stickelberger's congruence. The argument uses integrality of the basis elements, and does not require a maximal order. \(\square\)

## Testing one prime at a time

Fix an integral primitive element \(\alpha\), its monic minimal polynomial \(f\in\mathbf Z[x]\), and a rational prime \(p\). We call \(\mathbf Z[\alpha]\) **\(p\)-maximal** if

\[
p\nmid[\mathcal O_K:\mathbf Z[\alpha]].
\]

Factor the reduction of \(f\) as

\[
\bar f=\prod_{i=1}^s\bar g_i^{e_i}
\]

with distinct monic irreducible \(\bar g_i\in\mathbf F_p[x]\). Choose monic integer lifts \(g_i\) of the same degrees, and set

\[
h=\prod_i g_i,\qquad q=\prod_i g_i^{e_i-1},\qquad f=hq+pF. \tag{4}
\]

The polynomial \(F\) has integer coefficients. Its definition includes the sign in (4).

**Proposition 2.5 (Eisenstein).** If \(f\) is Eisenstein at \(p\), then \(\mathbf Z[\alpha]\) is \(p\)-maximal.

We will deduce this proposition immediately after proving the following more general test. Eisenstein at one prime makes a claim about that prime only.

**Theorem 2.6 (Dedekind's criterion).** With (4),

\[
p\nmid[\mathcal O_K:\mathbf Z[\alpha]]
\quad\Longleftrightarrow\quad
\bar g_i\nmid\bar F\text{ for every }i\text{ with }e_i\ge2.
\]

Here \(\bar F\) is a polynomial over \(\mathbf F_p\); the test concerns divisibility by each repeated irreducible factor, rather than the multiplicity of that factor alone.

**Proof.** We first turn a missing integer into an element preserving a specific ideal. Put

\[
R=\mathbf Z_{(p)}=\{a/b\in\mathbf Q\mid p\nmid b\},\quad
A=R[\alpha],\quad B=R\mathcal O_K.
\]

In Smith normal form, each diagonal entry is a unit of \(R\) times a power of \(p\). Thus the finite quotient \(\mathcal O_K/\mathbf Z[\alpha]\) gives \(A=B\) exactly when the desired index is prime to \(p\). It also gives \(p^kB\subseteq A\) for some \(k\ge0\).

The ring \(B\) is the integral closure of \(R\) in \(K\). Indeed, its elements are integral over \(R\). Conversely, if \(b\) satisfies a monic equation over \(R\), choose an integer \(m\) prime to \(p\) clearing its coefficients' denominators. If the coefficients are \(c_j\), the equation for \(mb\) has coefficients \(m^jc_j\in\mathbf Z\). Thus \(mb\in\mathcal O_K\), so \(b\in B\).

Let

\[
J=(p,h(\alpha))\subset A,\qquad
E=\{b\in K:bJ\subseteq J\}.
\]

Monic polynomial division and minimality of \(f\) identify \(A\) with \(R[x]/(f)\). Thus \(A/pA=\mathbf F_p[x]/(\bar f)\), and the elements nilpotent modulo \(pA\) are exactly \(J\): a power of a polynomial is divisible by \(\bar f\) if and only if each \(\bar g_i\) divides that polynomial. In particular, \(J^N\subseteq pA\) for some \(N\), and

\[
A/J=\mathbf F_p[x]/(\bar h)
\]

has no nonzero nilpotents: \(\bar h\) is a product of distinct irreducibles.

We claim that \(A=B\) if and only if \(E=A\). The ideal \(J\) is a free \(R\)-module of rank \(n\): it is obtained by localizing the subgroup \((p,h(\alpha))\) of \(\mathbf Z[\alpha]\), which contains \(p\mathbf Z[\alpha]\). If \(b\in E\), multiplication by \(b\) has a matrix \(C\) over \(R\) in a basis \(\boldsymbol e\) of \(J\). The equation \(\boldsymbol e(bI-C)=0\), multiplied by the adjugate matrix, gives \(\det(bI-C)\boldsymbol e=0\). A basis element is nonzero in the field \(K\), so \(b\) is a root of the monic polynomial \(\det(TI-C)\in R[T]\). Thus \(A\subseteq E\subseteq B\). In particular, \(A=B\) implies \(E=A\).

Conversely suppose \(A\ne B\). The inclusions above give \(J^{Nk}B\subseteq A\). Choose the smallest positive \(t\) with \(J^tB\subseteq A\), and an element \(b\in J^{t-1}B\setminus A\). Then \(bJ\subseteq A\). For \(x\in J\), set \(y=bx\in A\). A monic integral equation for \(b\) over \(R\), multiplied by a power of \(x\), reduces modulo \(J\) to \(y^m=0\). Since \(A/J\) has no nonzero nilpotents, \(y\in J\). Therefore \(b\in E\setminus A\), proving the claim.

It remains to compute when \(E\ne A\). For \(b\in E\), the condition \(pb\in J\) allows us to subtract an element of \(A\) and write

\[
b=\frac{h(\alpha)t(\alpha)}p,\qquad t\in R[x].
\]

Its other required condition is \(bh(\alpha)\in J\). In \(R[x]\), this is equivalent to

\[
h^2t\in(p^2,ph,f).
\]

Thus for some polynomials \(v,w,z\) we have \(h^2t=p^2v+phw+fz\). Reducing modulo \(p\) and cancelling \(\bar h\) in \(\mathbf F_p[x]\) gives

\[
\bar h\bar t=\bar q\bar z.
\]

Write \(ht=qz+py\) with \(y\in R[x]\). Evaluating at \(\alpha\), and using (4), now gives

\[
bh(\alpha)=-F(\alpha)z(\alpha)+h(\alpha)y(\alpha).
\]

Its membership in \(J\) says \(\bar h\mid\bar F\bar z\). Also \(b\notin A\) exactly when \(\bar f\nmid\bar h\bar t=\bar q\bar z\), or equivalently \(\bar h\nmid\bar z\). We have obtained the three conditions

\[
\bar h\mid\bar q\bar z,\qquad
\bar h\mid\bar F\bar z,\qquad
\bar h\nmid\bar z. \tag{5}
\]

Conversely, given a polynomial \(\bar z\) satisfying (5), take \(\bar t=\bar q\bar z/\bar h\), lift \(z,t\), and use the displayed identity to construct \(b\in E\setminus A\). Thus (5) is an exact test for failure of maximality.

Because \(\bar h\) is squarefree, (5) has a solution precisely when some \(\bar g_i\) divides both \(\bar q\) and \(\bar F\). If such a factor exists, take \(\bar z=\bar h/\bar g_i\). If none exists, each factor of \(\bar h\) must divide \(\bar z\) by one of the first two conditions, contradicting the third. Finally, \(\bar g_i\mid\bar q\) means exactly \(e_i\ge2\). Together with the claim about \(E\), this proves the theorem. \(\square\)

**Proof of Proposition 2.5.** For an Eisenstein polynomial of degree at least \(2\), \(\bar f=x^n\). Take \(g=x\) and \(F=(f-x^n)/p\). Its constant coefficient is not divisible by \(p\), because the constant coefficient of \(f\) is not divisible by \(p^2\). Hence \(x\nmid\bar F\), and Theorem 2.6 applies. In degree \(1\), the field and its ring of integers are \(\mathbf Q\) and \(\mathbf Z\), so the assertion is immediate. \(\square\)

The choice of lifts does not affect the answer. Replacing \(g_i\) by \(g_i+pu_i\) changes \(F\), modulo \(p\), by a sum of terms

\[
-e_i\bar u_i\bar g_i^{e_i-1}\prod_{j\ne i}\bar g_j^{e_j}.
\]

Every such term is divisible by any fixed repeated factor \(\bar g_k\). Thus the tests \(\bar g_k\mid\bar F\) for \(e_k\ge2\) remain unchanged.

## Four computations

### Quadratic fields

Let \(d\ne0,1\) be a squarefree integer, including negative integers. The quadratic integer theorem gives

\[
\mathcal O_{\mathbf Q(\sqrt d)}=
\begin{cases}
\mathbf Z[(1+\sqrt d)/2],&d\equiv1\pmod4,\\
\mathbf Z[\sqrt d],&d\equiv2,3\pmod4.
\end{cases}
\]

For any quadratic basis \((1,\omega)\), Proposition 2.2 gives \(d(1,\omega)=(\omega-\omega')^2\). The differences are \(\sqrt d\) and \(2\sqrt d\), respectively. Therefore

\[
d_{\mathbf Q(\sqrt d)}=
\begin{cases}
d,&d\equiv1\pmod4,\\
4d,&d\equiv2,3\pmod4.
\end{cases}
\]

The power order \(\mathbf Z[\sqrt d]\) has discriminant \(4d\) in both cases. In the first case it has index \(2\); in the second it has index \(1\). The sign agrees with the presence or absence of a complex pair. For example, the discriminants for \(d=5,2,-3\) are \(5,8,-3\).

### A useful cubic formula

For \(f(x)=x^3+ax+b\), multiplication by \(3\alpha^2+a\) in the basis \(1,\alpha,\alpha^2\) has matrix

\[
\begin{pmatrix}
a&-3b&0\\
0&-2a&-3b\\
3&0&-2a
\end{pmatrix}.
\]

Its determinant is \(4a^3+27b^2\), so Proposition 2.2 yields

\[
\operatorname{disc}(x^3+ax+b)=-4a^3-27b^2. \tag{6}
\]

The computation can be made in the quotient algebra by \(f\) even when \(f\) is reducible. For distinct roots its multiplication matrix is diagonalized by evaluation at the roots, so the same formula holds. Both expressions are polynomial functions of \(a,b\); hence the identity holds for repeated roots as well.

### Two cubic integral bases

For \(\alpha=\sqrt[3]2\), the polynomial \(x^3-2\) has no rational root: such a root would be an integer whose cube is \(2\). It is therefore irreducible, and it is Eisenstein at \(2\). Formula (6) gives discriminant \(-108=-2^2\cdot3^3\). Only \(2\) and \(3\) can divide the index. The prime \(2\) is excluded by Proposition 2.5. Put \(\beta=\alpha+1\); then

\[
(x-1)^3-2=x^3-3x^2+3x-3
\]

is its Eisenstein polynomial at \(3\). Since \(\mathbf Z[\beta]=\mathbf Z[\alpha]\), that prime is excluded too. Thus

\[
\mathcal O_{\mathbf Q(\sqrt[3]2)}=\mathbf Z[\sqrt[3]2],\qquad d_K=-108.
\]

For \(f=x^3-x-1\), a rational root would be \(1\) or \(-1\), and neither is a root. A cubic without a rational root is irreducible. Formula (6) gives

\[
\operatorname{disc}(f)=4-27=-23.
\]

This is squarefree. Hence its root \(\alpha\) gives the integral basis \(1,\alpha,\alpha^2\), and \(d_K=-23\). Notice that the two examples reach maximality by different tests.

### A biquadratic basis with a denominator

Put \(u=\sqrt2\), \(v=\sqrt3\), and \(K=\mathbf Q(u,v)\). The complete proof in *Algebraic integers and rings of integers*, Exercise 6 establishes that

\[
\left(1,u,v,w\right),\qquad w=\frac{u+uv}{2},
\]

is an integral basis. Its notation there is \(s=u\), \(t=v\), \(u_{\mathrm{there}}=uv\), and \(v_{\mathrm{there}}=w\). We now apply the discriminant and index formulas to this established basis.

The four embeddings independently change the signs of \(u,v\). Summing their values gives the trace Gram matrix

\[
\begin{pmatrix}
4&0&0&0\\
0&8&0&4\\
0&0&12&0\\
0&4&0&8
\end{pmatrix}.
\]

Its determinant is \(4\cdot12\cdot(64-16)=2304=2^8\cdot3^2\). Thus \(d_K=2304\). As a separate index check, the basis \((1,u,v,uv)\) has diagonal trace matrix \(\operatorname{diag}(4,8,12,24)\), of determinant \(9216\). Its span has index \(2\), exactly as (2) predicts.

## What this lesson does not prove

The following prerequisite facts are used with their stated hypotheses.

- A finite separable extension has a primitive element and exactly as many embeddings into an algebraic closure as its degree. See [Stacks, Tag 030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element) and [Stacks, Tag 09HA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-separable-equality).
- For a finite separable extension, trace and norm are the sum and product over its embeddings. If the base is the fraction field of an integrally closed domain and the element is integral over that domain, these trace and norm values belong to the domain. See [Milne ANT, Corollaries 2.20–2.21]. We use this also for relative traces and norms between number fields.
- Elements integral over a ring form a subalgebra; a finite collection of integral elements lies in a subalgebra finite as a module; integrality is transitive. See [Stacks, Tags 00GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-closure-is-ring), [00GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-integral), and [00GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-transitive).
- An algebraic number is integral precisely when its monic rational minimal polynomial has integer coefficients. A rational algebraic integer is an integer, and any algebraic number has a nonzero integer multiple that is integral. Rings of integers are integrally closed in their fraction fields. See [Milne ANT, Proposition 2.11, Example 2.10(a), Proposition 2.6, Corollary 2.16].
- A subgroup of \(\mathbf Z^n\) is finite free of rank at most \(n\). See [Hecke 1923, Chapter II, §11, Satz 34 and Satz 37]. Integer matrices admit Smith normal form, with invertible integer row and column operations; see [Milne ANT, Chapter II, “Review of bases of A-modules”]. We prove the discriminant–index relation here, using that algebraic fact.
- A symmetric polynomial in finitely many variables is a polynomial in their elementary symmetric functions, over the same coefficient ring. See [Milne ANT, Theorem 2.2].
- For squarefree \(d\ne0,1\), the quadratic rings of integers are the two rings displayed in the quadratic example. See [Milne ANT, Example 2.41]. This lesson computes their discriminants from those bases.

The general discriminant theorem for orders over Dedekind domains is developed in *Orders and the discriminant theorem*. The present lesson establishes the lattice formula and computational tests needed there. Ramification and the different are developed later in *Decomposition of primes in extensions* and *The different and the discriminant*.

## Exercises and complete solutions

**Exercise 1 (easy).** Compute \(\operatorname{disc}(x^3+ax+b)\) directly from a trace matrix, obtaining (6).

**Solution.** Let the three roots be \(\theta_i\), with multiplicity, and put \(s_m=\sum_i\theta_i^m\). The coefficient identities and the equation \(\theta_i^3=-a\theta_i-b\) give

\[
s_0=3,\quad s_1=0,\quad s_2=-2a,\quad s_3=-3b,\quad s_4=2a^2.
\]

For example, \(s_2=s_1^2-2\sum_{i<j}\theta_i\theta_j=-2a\), and multiplying the root equation by \(\theta_i\) gives \(s_4=-as_2-bs_1\). The matrix \((s_{i+j})_{0\le i,j\le2}\) is

\[
\begin{pmatrix}
3&0&-2a\\
0&-2a&-3b\\
-2a&-3b&2a^2
\end{pmatrix}.
\]

It is the product of the transpose of the root evaluation matrix with that matrix, even when roots repeat. Its determinant is therefore the squared Vandermonde product. Expanding gives \(3(-4a^3-9b^2)+8a^3=-4a^3-27b^2\).

**Exercise 2 (medium).** Prove the sign rule by finding the signature of the trace form over \(\mathbf R\).

**Solution.** Send an element to its real embeddings and to one embedding from each complex pair, splitting the latter into real and imaginary parts. On real linear combinations of a rational basis this is an isomorphism to \(\mathbf R^{r_1}\times\mathbf C^{r_2}\): after recombining each pair of real coordinates into conjugate complex coordinates, its matrix is the invertible embedding matrix from Proposition 2.1. In these coordinates,

\[
\operatorname{Tr}(xy)=\sum_{i=1}^{r_1}x_i y_i+
2\sum_{j=1}^{r_2}\operatorname{Re}(z_jt_j).
\]

Writing \(z=a+ib\), \(t=c+id\) gives \(2\operatorname{Re}(zt)=2ac-2bd\). Each complex factor therefore contributes one positive and one negative diagonal entry; each real factor contributes one positive entry. The signature is \((r_1+r_2,r_2)\). Changing a real basis changes the determinant by a positive square, so every basis discriminant has sign \((-1)^{r_2}\).

**Exercise 3 (medium).** Show that \(\mathbf Z[\sqrt[3]2]\) is the full ring of integers using Eisenstein tests at \(2\) and \(3\).

**Solution.** The polynomial \(x^3-2\) is Eisenstein at \(2\). Its discriminant is \(-27\cdot2^2=-108\), so (3) restricts possible index primes to \(2,3\). At \(3\), use \(\beta=1+\sqrt[3]2\), whose minimal polynomial is \(x^3-3x^2+3x-3\). All its nonleading coefficients are divisible by \(3\), and its constant coefficient is not divisible by \(9\). Proposition 2.5 excludes \(3\) from the index of \(\mathbf Z[\beta]\); this order equals \(\mathbf Z[\sqrt[3]2]\). The same proposition excludes \(2\). Hence the index is \(1\).

**Exercise 4 (medium).** Use Dedekind's criterion to show that \(\mathbf Z[\sqrt7]\) is \(2\)-maximal, while \(\mathbf Z[\sqrt5]\) is not.

**Solution.** In both cases \(x^2-d\equiv(x-1)^2\pmod2\). Choose \(g=x-1\); then

\[
F=\frac{x^2-d-(x-1)^2}{2}=x-\frac{d+1}{2}.
\]

For \(d=7\), \(F=x-4\), whose reduction at \(x=1\) is \(1\). Thus \(x-1\nmid\bar F\), giving \(2\)-maximality. For \(d=5\), \(F=x-3\), and \(\bar F=x-1\). The test fails. The missing integer is \((1+\sqrt5)/2\), and the quadratic example shows that the index is exactly \(2\).

**Exercise 5 (hard).** Let \(d\) be a nonzero squarefree integer with \(|d|>1\), and let \(\alpha=\sqrt[3]d\). Prove

\[
\mathbf Z[\alpha]=\mathcal O_{\mathbf Q(\alpha)}
\quad\Longleftrightarrow\quad d\not\equiv\pm1\pmod9.
\]

In the exceptional cases, determine an integral basis as well.

**Solution.** A rational root of \(x^3-d\) would be an integer whose cube is \(d\), which is impossible for squarefree \(|d|>1\). Thus the polynomial is irreducible and its discriminant is \(-27d^2\). The only possible index primes are \(3\) and primes dividing \(d\). For every prime dividing \(d\), squarefreeness makes \(x^3-d\) Eisenstein, so that prime does not divide the index. If \(3\mid d\), this already finishes the proof.

Suppose \(3\nmid d\), and choose \(r\in\{1,-1\}\) with \(d\equiv r\pmod3\). Then \(\bar f=(x-r)^3\). With \(g=x-r\),

\[
F=rx^2-r^2x+\frac{r^3-d}{3},\qquad
F(r)=\frac{r^3-d}{3}.
\]

The sole repeated factor divides \(\bar F\) exactly when \(9\mid d-r^3\). Since \(r^3=r\), Dedekind's criterion excludes \(3\) from the index exactly when \(d\not\equiv\pm1\pmod9\). Every possible index prime has now been tested, proving the equivalence for positive and negative \(d\).

For completeness suppose \(d\equiv r\pmod9\). Define

\[
\omega=\frac{1+r\alpha+\alpha^2}{3}.
\]

The trace, second elementary symmetric function, and norm of \(\omega\) are

\[
1,\qquad \frac{1-rd}{3},\qquad \frac{(d-r)^2}{27}.
\]

To obtain the middle quantity, expand \(\omega^2\) and use \(\operatorname{Tr}(\alpha)=\operatorname{Tr}(\alpha^2)=0\): its trace is \((1+2rd)/3\), and the second symmetric function is \((\operatorname{Tr}(\omega)^2-\operatorname{Tr}(\omega^2))/2\). The norm follows by multiplying the three conjugates; equivalently, expansion gives

\[
N(a+b\alpha+c\alpha^2)=a^3+b^3d+c^3d^2-3abcd.
\]

Consequently \(\omega\) satisfies

\[
T^3-T^2+\frac{1-rd}{3}T-\frac{(d-r)^2}{27}=0.
\]

Its coefficients are integers: \(d-r\) is divisible by \(9\). Thus \(M=\mathbf Z+\mathbf Z\alpha+\mathbf Z\omega\) is a full integral lattice. It contains the power order with index \(3\), and has discriminant \(-3d^2\) by (1). If \(\mathcal O_K/M\) had nontrivial index, its primes would divide the index of the contained power order. All primes except \(3\) have already been excluded. But \(-3d^2\) has exactly one factor of \(3\), so (2) excludes \(3\) as well. Therefore \((1,\alpha,\omega)\) is an integral basis. In these exceptional cases the power order has index exactly \(3\) and the field discriminant is \(-3d^2\); in all other cases the field discriminant is \(-27d^2\).

## References

- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08, 2020, Chapter II. [Author's lecture notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Stacks]** *The Stacks Project*, “Discriminants and Differents,” especially [Tag 0BVH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-section-discriminant), with the algebra and field-theory tags cited above. The [official Stacks project](https://stacks.math.columbia.edu/) is the upstream work. The AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks project's maintainers; the tag links lead to its English reader. The determinant construction in Tag 0BVH extends to finite locally free algebras over general bases.
- **[Hecke 1923]** E. Hecke, [*Vorlesungen über die Theorie der algebraischen Zahlen*](https://archive.org/details/vorlesungenber00heckuoft), Leipzig, 1923, Chapter V, §22, Satz 64; Chapter II, §11 for the abelian-group facts.

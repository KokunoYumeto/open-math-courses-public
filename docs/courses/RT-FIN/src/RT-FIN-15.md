# The symmetric groups III: characters and symmetric functions

*Written by GPT-6.1 Sol (OpenAI), at Ultra in Codex, October 2026. Self-checked by the AI that wrote it. Independent AI review is not yet recorded. Independently authored text is public domain (CC0); the explicitly credited kernel-expansion proof paragraph in Lemma 1.2 is adapted under CC BY 4.0.*

A cycle of length \(r\) will become the power sum \(p_r\). Disjoint cycles become products. Under this translation, inducing representations of two symmetric groups becomes multiplying symmetric functions, and the irreducible \(V_\lambda\) becomes the Schur function \(s_\lambda\). The translation gives both a character algorithm and a way to decompose permutation representations.

We use [Young tableaux and Young symmetrizers](RT-FIN-13.md), Lemma 2.2 and Theorem 4.3, with the convention \(V_\lambda=\mathbb C[S_n]a_tb_t\), and the standard-tableau dimensions in [Branching, Jucys–Murphy elements and Young's seminormal form](RT-FIN-14.md), Corollary 4.3 and Theorem 6.3. Character orthogonality comes from [Characters and the orthogonality relations](RT-FIN-02.md), and the induction formula and Frobenius reciprocity from [Induced representations and Frobenius reciprocity](RT-FIN-06.md), Proposition 2.1 and Theorem 3.1. We prove the symmetric-function tools and the Littlewood–Richardson rule here. Basic comparisons are [Grinberg–Reiner] and [Stembridge].

## 1. A ring that retains every number of variables

Let \(\Lambda_{\mathbb Z}^{n}\) consist of compatible homogeneous symmetric polynomials of degree \(n\) in \(L\) variables, for \(L=0,1,2,\ldots\). Compatibility means that setting the last variable to zero gives the preceding polynomial. Put

\[
\Lambda_{\mathbb Z}=\bigoplus_{n\geq0}\Lambda_{\mathbb Z}^{n},
\qquad \Lambda_K=K\otimes_{\mathbb Z}\Lambda_{\mathbb Z}
\quad(K=\mathbb Q,\mathbb C).
\tag{1}
\]

This is the graded inverse limit: we take the inverse limit separately in each degree, then a direct sum. Its elements have bounded degree. An unrestricted inverse limit would also admit incompatible degree bounds, such as the compatible sequence \(\prod_{i=1}^L(1+x_i)\); that larger completion is not the ring in (1).

For a partition \(\lambda\vdash n\), \(m_\lambda\) is the sum of the distinct monomials obtained by permuting its parts and padded zeros. These sums form a basis in \(L\) variables for \(\ell(\lambda)\leq L\). The coefficient of each such sum stabilizes, and all partitions of \(n\) occur once \(L\geq n\). Thus the \(m_\lambda\), \(\lambda\vdash n\), form a \(\mathbb Z\)-basis of \(\Lambda_{\mathbb Z}^{n}\).

Define

\[
e_r=\sum_{i_1<\cdots<i_r}x_{i_1}\cdots x_{i_r},
\qquad h_r=\sum_{i_1\leq\cdots\leq i_r}x_{i_1}\cdots x_{i_r},
\qquad p_r=\sum_i x_i^r \quad(r\geq1).
\tag{2}
\]

Set \(e_0=h_0=1\), and \(h_r=0\) for \(r<0\). For any of these letters, a partition subscript means a product over its parts, for example \(h_\lambda=\prod_i h_{\lambda_i}\). The empty product is \(1\).

**Proposition 1.1 (the elementary bases).** The families \(m_\lambda,e_\lambda,h_\lambda\) are integral bases degree by degree. The \(p_\lambda\) are a rational basis, and

\[
\Lambda_{\mathbb Z}=\mathbb Z[e_1,e_2,\ldots]
=\mathbb Z[h_1,h_2,\ldots],
\qquad \Lambda_{\mathbb Q}=\mathbb Q[p_1,p_2,\ldots].
\tag{3}
\]

**Proof.** First work in \(L\) variables, ordered lexicographically with \(x_1\) first. The leading monomial of a symmetric homogeneous polynomial has exponent sequence \(\alpha_1\geq\cdots\geq\alpha_L\): swapping an increasing pair would produce a larger monomial. The product

\[
e_1^{\alpha_1-\alpha_2}e_2^{\alpha_2-\alpha_3}\cdots e_L^{\alpha_L}
\tag{4}
\]

has leading monomial \(x^\alpha\), with coefficient \(1\). Subtract a suitable integer multiple of (4). Repetition terminates because there are only finitely many monomials of the fixed degree. Distinct products (4) have distinct leading monomials, so they are independent. This proves generation and algebraic independence of \(e_1,\ldots,e_L\). In degree \(n\) no \(e_r\) with \(r>n\) is needed. The expansions therefore stabilize and give the first equality in (3) and the \(e\)-basis assertion.

Choosing or repeating variables in (2) gives, coefficient by coefficient,

\[
E(t)=\sum_{r\geq0}e_rt^r=\prod_i(1+x_it),
\qquad H(t)=\sum_{r\geq0}h_rt^r=\prod_i(1-x_it)^{-1}.
\tag{5}
\]

Hence \(E(-t)H(t)=1\). Its degree-\(r\) coefficient expresses \(h_r\) as \((-1)^{r-1}e_r\) plus an integral polynomial in the earlier \(e_i\); solving in the other direction does the same for \(e_r\). These mutually inverse triangular substitutions prove the \(h\)-basis assertion over \(\mathbb Z\).

Over \(\mathbb Q\), logarithmic differentiation of (5) gives

\[
H(t)=\exp\!\left(\sum_{r\geq1}\frac{p_r t^r}{r}\right),
\qquad n h_n=\sum_{r=1}^n p_r h_{n-r}.
\tag{6}
\]

Thus \(p_n=n h_n\) plus a polynomial in earlier \(h_i\), and conversely \(h_n=p_n/n\) plus a polynomial in earlier \(p_i\). The invertible rational substitution proves the last assertion. All series operations are formal: each coefficient involves finitely many terms. \(\square\)

The word “rational” matters. For example \(p_2=m_2\) and \(p_1^2=m_2+2m_{(1,1)}\), so these two power-sum products do not form an integral basis in degree two.

Write \(m_r(\mu)\) for the number of parts of \(\mu\) equal to \(r\), and put

\[
z_\mu=\prod_{r\geq1}r^{m_r(\mu)}m_r(\mu)!.
\tag{7}
\]

Define the Hall form over \(\mathbb Q\) by \(\langle p_\lambda,p_\mu\rangle=z_\lambda\delta_{\lambda\mu}\), with different degrees orthogonal. Over \(\mathbb C\) we use its Hermitian extension, linear in the first argument. It is positive definite because every \(z_\lambda\) is positive.

**Lemma 1.2 (the kernel and duality).** As a formal series of equal degrees in two alphabets,

\[
\begin{aligned}
\mathcal K(x,y)&=\prod_{i,j}(1-x_i y_j)^{-1}\\
&=\sum_\mu h_\mu(x)m_\mu(y)
=\sum_\mu \frac{p_\mu(x)p_\mu(y)}{z_\mu}.
\end{aligned}
\tag{8}
\]

Consequently \(\langle h_\lambda,m_\mu\rangle=\delta_{\lambda\mu}\).

**Proof.** First take finite alphabets. In \(\prod_j H_x(y_j)\), the coefficient of \(y^\alpha\) is \(\prod_j h_{\alpha_j}(x)\); collecting equal sorted exponent sequences yields \(\sum_\mu h_\mu(x)m_\mu(y)\). For the power-sum expansion, formal logarithms turn the product into the exponential of \(\sum_{r\geq1}p_r(x)p_r(y)/r\). Its factor indexed by \(r\) is

\[
\sum_{a\geq0}\frac{p_r(x)^a p_r(y)^a}{r^a a!}.
\]

Choosing each multiplicity \(a=m_r(\mu)\) gives coefficient \(\prod_r(r^{m_r(\mu)}m_r(\mu)!)^{-1}=z_\mu^{-1}\). Each fixed degree has finitely many choices, and specialization is compatible with setting variables to zero. The finite-alphabet identities therefore give (8) in the degreewise completion.

*Credit for the preceding kernel-expansion paragraph and displayed series:* adapted by GPT-6.1 Sol from Darij Grinberg and Victor Reiner, [*Hopf Algebras in Combinatorics*](https://www.cip.ifi.lmu.de/~grinberg/algebra/HopfComb.pdf), Proposition 2.5.15 and its proof, pp. 64–66, July 27, 2020 text with minor corrections dated September 6, 2026; [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The AI adaptation uses finite alphabets first, this lesson's notation, and an explicit degreewise specialization argument. The following duality argument is independently authored.

For rational \(f\), the second sum satisfies \(\langle f(x),\mathcal K(x,y)\rangle=f(y)\), as one checks on the \(p\)-basis. Substitute \(f=m_\lambda\) into the first sum and compare coefficients in the \(m(y)\)-basis. This gives \(\langle m_\lambda,h_\mu\rangle=\delta_{\lambda\mu}\). Symmetry over \(\mathbb Q\), and then Hermitian extension, gives the displayed duality. \(\square\)

*Comparison:* [Grinberg–Reiner, Proposition 2.5.15 and Corollary 2.5.17]. The complete generating function \(H(t)\) is infinite even in finitely many variables: for one variable, \(H(t)=(1-xt)^{-1}=\sum_{r\geq0}x^rt^r\), and every degree can be nonzero. A finite alphabet therefore permits degreewise specialization, not truncation at its size. The component credit in Lemma 1.2 describes the exact adapted part.

## 2. Determinants, tableaux and orthogonality

For \(L\geq\ell(\lambda)\), pad \(\lambda\) by zeros and set

\[
\delta=(L-1,L-2,\ldots,0),\qquad
a_\alpha(x)=\det[x_i^{\alpha_j}]_{i,j=1}^L,
\qquad \Delta(x)=a_\delta(x)=\prod_{i<j}(x_i-x_j).
\tag{9}
\]

Define the Schur polynomial by

\[
s_\lambda(x_1,\ldots,x_L)=\frac{a_{\lambda+\delta}(x)}{\Delta(x)}.
\tag{10}
\]

The numerator vanishes when \(x_i=x_j\), so each prime factor \(x_i-x_j\) divides it in \(\mathbb Z[x_1,\ldots,x_L]\). Distinct such factors are nonassociate primes, and their product divides it. The quotient is integral, symmetric and of degree \(|\lambda|\). Setting \(x_L=0\), determinant expansion gives the \(L-1\)-variable quotient if \(\lambda_L=0\): each remaining numerator and denominator row has a common factor \(x_i\), which cancels. If \(\lambda_L>0\), the numerator specializes to zero while the specialized denominator is nonzero as a polynomial, so the quotient specializes to zero. Thus (10) gives a compatible symmetric function, whose specialization is zero when there are too few variables.

**Theorem 2.1 (Jacobi–Trudi and tableaux).** With the conventions following (2),

\[
s_\lambda=\det[h_{\lambda_i-i+j}]_{i,j=1}^L
=\sum_T x^T,
\tag{11}
\]

where \(T\) ranges over semistandard tableaux of shape \(\lambda\): entries are positive integers, weakly increasing along rows and strictly increasing down columns. Here \(x^T=\prod_{(i,j)\in\lambda}x_{T(i,j)}\).

**Proof of the determinant identity.** Work first in the rational function field of distinct variables. Put \(D_a=\prod_{b\ne a}(x_a-x_b)\). Partial fractions of \(H(t)=\prod_a(1-x_a t)^{-1}\) give

\[
h_k=\sum_{a=1}^L\frac{x_a^{k+L-1}}{D_a}\quad(k\geq0).
\tag{12}
\]

Indeed, the coefficient of \((1-x_a t)^{-1}\) is \(x_a^{L-1}/D_a\), by multiplying by \(1-x_a t\) and setting \(t=1/x_a\). Formula (12) remains valid for \(1-L\leq k<0\), when its right side is zero: interpolate the polynomial \(z^{k+L-1}\) at the \(x_a\) and compare coefficients of \(z^{L-1}\). For degree \(L-1\) that comparison also gives the value \(1\) at \(k=0\).

Every index \(\lambda_i-i+j\) is at least \(1-L\). Thus the matrix in (11) factors as

\[
[h_{\lambda_i-i+j}]_{i,j}
=[x_a^{\lambda_i+L-i}]_{i,a}
[x_a^{j-1}/D_a]_{a,j}.
\tag{13}
\]

The first determinant is \(a_{\lambda+\delta}\), by transposition. The second is \(1/\Delta\), since its numerator is \((-1)^{\binom L2}\Delta\) and \(\prod_aD_a=(-1)^{\binom L2}\Delta^2\). This proves (11) in the rational function field and hence as a polynomial identity. Stability gives the identity in \(\Lambda\).

**Proof of the tableau identity.** Use \(N\) variables and a finite directed grid with east and north steps. An east step at height \(a\in\{1,\ldots,N\}\) has weight \(x_a\); a north step has weight \(1\). The generating function of paths from

\[
A_j=(-j,1)\quad\text{to}\quad B_i=(\lambda_i-i,N)
\tag{14}
\]

is \(h_{\lambda_i-i+j}(x_1,\ldots,x_N)\): the heights of the required east steps form exactly a weakly increasing sequence. Negative numbers of east steps give no paths. Paths with zero east steps have weight \(1\).

Expand the determinant as signed families of paths joining the sources to a permutation of the endpoints. Cancel all families with a common vertex as follows. Order grid vertices first by \(x+y\), then by \(x\); at the first common vertex choose the lexicographically first pair of source labels meeting there. Exchange the two tails starting at this vertex. The product of weights is unchanged and the endpoint permutation changes by a transposition. Every tail proceeds to larger \(x+y\), so no earlier common vertex is affected; the chosen pair at the chosen vertex is unchanged. The exchange is therefore an involution, with opposite signs.

The surviving families have no common vertices. Their sources and endpoints must have the same left-to-right order. To see this directly, at each integer height each path occupies an interval of horizontal positions. Disjoint paths have disjoint intervals, and their vertical connecting steps prevent two intervals from reversing order between consecutive heights. Since both the \(A_j\) and the \(B_i\) are strictly ordered in decreasing index, the endpoint permutation is the identity.

Record the east-step heights of path \(i\) as row \(i\) of a tableau. Rows are weakly increasing. Compare the paths for adjacent rows at the vertical line \(x=j-i-1\): it lies just before the \(j\)-th east step of row \(i\), and just after the \(j\)-th east step of row \(i+1\). The paths avoid a common vertex precisely when

\[
T(i,j)<T(i+1,j)\qquad(j\leq\lambda_{i+1}).
\tag{15}
\]

Here is the converse check as well. If (15) first fails at column \(j\), the upper path's vertical interval at this line ends at \(T(i,j)\) and starts at its preceding height (or \(1\) for \(j=1\)). The lower interval starts at \(T(i+1,j)\) and ends at its next height (or \(N\)). The preceding strict inequality and weak row increase make these intervals overlap. If all inequalities hold, the upper interval ends below the lower one's start at every common vertical line; neither their vertical nor horizontal steps meet. Adjacent paths are separated, and hence all paths are disjoint. This proves a weight-preserving bijection between the surviving families and semistandard tableaux, in both directions. Every survivor has positive determinant sign, proving the second identity in (11). \(\square\)

Let \(K_{\lambda\mu}\) count semistandard tableaux of shape \(\lambda\) with exactly \(\mu_i\) entries equal to \(i\). Symmetry of (11) shows that the count is unchanged by permuting the content, and

\[
s_\lambda=\sum_{\mu\vdash n}K_{\lambda\mu}m_\mu.
\tag{16}
\]

**Lemma 2.2 (triangularity).** For partitions of the same integer,

\[
K_{\lambda\mu}=0\ \text{unless }\lambda\unrhd\mu,
\qquad K_{\lambda\lambda}=1.
\tag{17}
\]

In particular, the Schur functions form an integral basis.

**Proof.** An entry in row \(i\) is at least \(i\), by strict increase from the top of its column. Thus every entry at most \(k\) belongs to the first \(k\) rows. Counting these entries gives \(\sum_{i\leq k}\mu_i\leq\sum_{i\leq k}\lambda_i\). If \(\mu=\lambda\), all \(\lambda_1\) ones fill the first row. Inductively all \(\lambda_i\) copies of \(i\) fill row \(i\), so there is exactly one tableau. In any linear extension of dominance order the matrix in (16) is triangular with diagonal \(1\). Its inverse is integral, proving the basis assertion. \(\square\)

For example,

\[
s_{(2,1)}=m_{(2,1)}+2m_{(1,1,1)}.
\tag{18}
\]

The coefficient \(2\) is visible in the two fillings with one of each of \(1,2,3\):

\[
\begin{array}{cc}\boxed{1}&\boxed{2}\\\boxed{3}&\end{array}
\qquad
\begin{array}{cc}\boxed{1}&\boxed{3}\\\boxed{2}&\end{array}.
\tag{19}
\]

**Theorem 2.3 (Cauchy identity and orthonormality).**

\[
\mathcal K(x,y)=\sum_\lambda s_\lambda(x)s_\lambda(y),
\qquad \langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}.
\tag{20}
\]

**Proof.** In two alphabets of length \(L\), the Cauchy determinant identity is

\[
\det\!\left[\frac1{1-x_i y_j}\right]
=\frac{\Delta(x)\Delta(y)}{\prod_{i,j}(1-x_i y_j)}.
\tag{21}
\]

For completeness, multiply the left side by the denominator. The resulting polynomial is alternating in each alphabet and has degree at most \(L-1\) in each individual variable. It is consequently a constant times \(\Delta(x)\Delta(y)\). To find the constant, expand the determinant as a series in \(x\). It has no terms of total \(x\)-degree below \(\binom L2\), because it is alternating. The coefficient of \(x^\delta\) is \(\det[y_j^{L-i}]=\Delta(y)\). Multiplication by the denominator, whose constant term in \(x\) is \(1\), does not change this lowest-degree coefficient. Thus the constant is \(1\), proving (21).

Expand \((1-x_i y_j)^{-1}=\sum_{k\geq0}x_i^k y_j^k\). The determinant-of-a-product expansion gives

\[
\det[(1-x_i y_j)^{-1}]
=\sum_{k_1>\cdots>k_L\geq0}
\det[x_i^{k_j}]\det[y_i^{k_j}].
\tag{22}
\]

This expansion requires no infinite linear-algebra assumption: truncate the sum of powers at \(M\), expand the two finite determinants, group terms by their selected indices, and observe that repeated indices have zero determinant. The resulting identity stabilizes coefficient by coefficient as \(M\) increases. The two reversals needed to put indices in decreasing order have cancelling signs.

Write \(k_j=\lambda_j+L-j\), divide (22) by the Vandermonde products, and use (21). This proves (20) in \(L\) variables. Taking \(L\) larger than the degree under consideration proves the stable identity. The kernel reproduces the Hall form by Lemma 1.2. Substitute a Schur basis vector into this identity and compare coefficients in the other Schur basis; orthonormality follows. \(\square\)

Combining (16), Hall duality and (20) also gives

\[
h_\mu=\sum_\lambda K_{\lambda\mu}s_\lambda.
\tag{23}
\]

Indeed, its coefficient of \(s_\lambda\) is \(\langle h_\mu,s_\lambda\rangle=K_{\lambda\mu}\). This is an identity of symmetric functions, established before any assertion about character labels.

*Comparison:* [Grinberg–Reiner, Proposition 2.6.4 and Corollary 2.6.7], for alternants and the tableau formula. The partial-fraction determinant, intersecting-path involution and determinant expansion above supply the Jacobi–Trudi and Cauchy proofs in this lesson. An unproved tableau formula in another treatment is not a premise here.

## 3. Translating induction and fixing the labels

A permutation's conjugacy class is determined by its cycle type \(\mu\). Its centralizer has order \(z_\mu\): a commuting permutation may rotate each \(r\)-cycle in \(r\) ways and permute the \(m_r\) cycles of that length, with no other choices. Its class therefore has size \(n!/z_\mu\). Corollary 4.4 of *Young tableaux and Young symmetrizers* gives rational models, so the irreducible characters here are real-valued. We retain the Hermitian convention for general complex class functions.

For a complex class function on \(S_n\), define

\[
\operatorname{ch}(f)=\sum_{\mu\vdash n}\frac{f(\mu)}{z_\mu}p_\mu
=\frac1{n!}\sum_{g\in S_n}f(g)p_{\operatorname{type}(g)}.
\tag{24}
\]

Let \(R(S_n)\) be the integral group of virtual complex characters, with irreducible characters as its \(\mathbb Z\)-basis. For \(f\) on \(S_m\) and \(g\) on \(S_n\), their induction product is

\[
f\star g=\operatorname{Ind}_{S_m\times S_n}^{S_{m+n}}(f\boxtimes g),
\qquad (f\boxtimes g)(u,v)=f(u)g(v).
\tag{25}
\]

The factor groups act on disjoint consecutive blocks. Include \(S_0\), with its unique character \(1\), as degree zero.

**Theorem 3.1 (Frobenius characteristic).** The map (24) is an isometric isomorphism from complex class functions on \(S_n\) onto \(\Lambda_{\mathbb C}^{n}\). It takes the product (25) to ordinary multiplication and induces an integral graded-ring isomorphism

\[
\bigoplus_{n\geq0}R(S_n)\ \xrightarrow{\ \operatorname{ch}\ }\ \Lambda_{\mathbb Z}.
\tag{26}
\]

For a composition \(\mu\) of \(n\), let \(S_\mu=\prod_i S_{\mu_i}\), and let \(M^\mu=\operatorname{Ind}_{S_\mu}^{S_n}1\). With the irreducibles defined by Young symmetrizers,

\[
\operatorname{ch}(M^\mu)=h_\mu,
\qquad \operatorname{ch}(\chi^\lambda)=s_\lambda.
\tag{27}
\]

**Proof: class functions and products.** The class indicator functions map to \(p_\mu/z_\mu\), so (24) is bijective. Using class sizes and Hall norms,

\[
\langle\operatorname{ch}(f),\operatorname{ch}(g)\rangle
=\sum_\mu\frac{f(\mu)\overline{g(\mu)}}{z_\mu}
=\frac1{n!}\sum_{w\in S_n}f(w)\overline{g(w)}.
\tag{28}
\]

This proves the Hermitian isometry even for arbitrary complex class functions.

If \(H\subset G=S_N\) and \(F\) is a class function on \(H\), the induced-character formula gives

\[
\frac1{|G|}\sum_{w\in G}(\operatorname{Ind}_H^G F)(w)p_{\operatorname{type}(w)}
=\frac1{|H|}\sum_{u\in H}F(u)p_{\operatorname{type}(u)}.
\tag{29}
\]

To verify this, substitute \(|H|^{-1}\sum_{x:x^{-1}wx\in H}F(x^{-1}wx)\) for the induced function. Reindex by \((x,u)\in G\times H\); conjugation does not change cycle type, and the factor \(|G|\) cancels. For \(H=S_m\times S_n\), the power sum attached to \((u,v)\) is the product of the two cycle-type power sums. Thus the right side of (29) factors into \(\operatorname{ch}(f)\operatorname{ch}(g)\).

Expanding (6) gives \(h_n=\sum_{\mu\vdash n}p_\mu/z_\mu\), so \(\operatorname{ch}(1_{S_n})=h_n\). Transitivity of induction and the product identity give \(\operatorname{ch}(M^\mu)=h_\mu\). Associativity, commutativity and the unit for (25) now also follow from bijectivity and the corresponding properties in \(\Lambda\).

**Proof: integrality and positive irreducibles.** Jacobi–Trudi expresses \(s_\lambda\) as an integer signed sum of products of \(h_r\). Each nonzero product is the characteristic of an actual induced character; its factors have total degree \(n\). Hence \(\psi_\lambda=\operatorname{ch}^{-1}(s_\lambda)\) is an integral virtual character. Its norm is \(1\) by (20) and (28). In an expansion in irreducible characters, integral coefficients of squared sum \(1\) have exactly one nonzero entry, equal to \(1\) or \(-1\). Distinct \(\psi_\lambda\) give distinct irreducibles up to sign.

The sign is positive. Formula (24) and the Hall norm show

\[
\psi_\lambda(1)=\langle s_\lambda,p_1^n\rangle
=\langle s_\lambda,h_{(1^n)}\rangle
=K_{\lambda,(1^n)}=f^\lambda>0.
\tag{30}
\]

The last equality counts standard tableaux; one exists by filling successive rows. Thus the \(\psi_\lambda\) are the irreducible characters, in some order. Since the Schur functions are an integral basis, this already proves that (26) is an integral ring isomorphism. It remains essential to identify that order.

**Proof: agreement with the Young-ideal labels.** Write \(A=\mathbb C[S_n]\). The averaging idempotent \(a_t/|S_\mu|\) projects any representation onto its \(S_\mu\)-invariant vectors when \(t\) has shape \(\mu\). If \(V_\nu=Aa_ub_u\) occurs in \(M^\mu\), Frobenius reciprocity says \(a_tV_\nu\ne0\). Lemma 2.2 of *Young tableaux and Young symmetrizers* gives

\[
a_t A b_u=0\quad\text{unless }\mu\unlhd\nu.
\tag{31}
\]

As \(a_tAa_ub_u\subset a_tAb_u\), occurrence forces \(\nu\unrhd\mu\).

Let \(\phi\) be the bijection defined by \(\psi_\lambda=\chi^{\phi(\lambda)}\). Equations (23), (27)'s already proved first identity, and \(K_{\lambda\lambda}=1\) show that \(\psi_\lambda\) occurs in \(M^\lambda\). Therefore \(\phi(\lambda)\unrhd\lambda\) by (31). Follow a cycle of the finite permutation \(\phi\). The resulting dominance inequalities return to the starting partition; antisymmetry forces equality at every step. Every cycle is trivial, so \(\phi(\lambda)=\lambda\). This proves the second identity in (27), with the required preceding labels. \(\square\)

**Theorem 3.2 (Young's rule).** For a partition or composition \(\mu\) of \(n\),

\[
M^\mu\cong\bigoplus_{\lambda\vdash n}K_{\lambda\mu}V_\lambda.
\tag{32}
\]

**Proof.** Under (27), the multiplicity is \(\langle h_\mu,s_\lambda\rangle\). By (16) and Hall duality this is exactly the semistandard count \(K_{\lambda\mu}\). Complete reducibility turns the character equality into (32). For a composition, the same coefficient calculation applies to the monomial \(x^\mu\); sorting its parts changes neither \(h_\mu\) nor the tableau count, by symmetry. \(\square\)

The argument above explicitly identifies the Schur labels with the earlier Young symmetrizers: Lemma 2.2 of the Young-symmetrizer lesson supplies the dominance vanishing, while positive degree selects the sign of the norm-one virtual character. These are the internal proof steps needed for the labelled characteristic isomorphism.

## 4. Coefficients and border strips

**Corollary 4.1 (Frobenius's formula).** If \(\lambda,\mu\vdash n\) and \(L\geq\ell(\lambda)\), then

\[
\chi^\lambda(\mu)
=[x_1^{\lambda_1+L-1}x_2^{\lambda_2+L-2}\cdots x_L^{\lambda_L}]
\,\Delta(x)p_\mu(x_1,\ldots,x_L).
\tag{33}
\]

The degree-zero case uses empty products and has value \(1\).

**Proof.** By (24), (27) and orthonormality,

\[
p_\mu=\sum_{\nu\vdash n}\chi^\nu(\mu)s_\nu.
\tag{34}
\]

After specializing to \(L\) variables, terms of length greater than \(L\) vanish by the tableau formula. Multiply by \(\Delta\) to obtain alternants \(a_{\nu+\delta}\). Their exponent lists are strictly decreasing; therefore \(x^{\lambda+\delta}\) occurs in exactly one of them, namely \(a_{\lambda+\delta}\), with coefficient \(1\). Taking that coefficient proves (33). This works even when \(L<n\). \(\square\)

A **border strip** \(\lambda/\eta\) is a nonempty skew diagram connected by shared edges and containing no \(2\times2\) block. Its height is its number of occupied rows minus one. A diagonal touching does not give edge connectivity.

**Lemma 4.2 (the border-strip product).** For \(r\geq1\),

\[
p_r s_\eta=\sum_{\lambda:\,\lambda/\eta\text{ border strip of size }r}
(-1)^{\operatorname{ht}(\lambda/\eta)}s_\lambda.
\tag{35}
\]

**Proof.** Choose \(L\geq|\eta|+r\), so every relevant shape fits, and put \(\beta_i=\eta_i+L-i\). Alternating a monomial and multiplying by the symmetric function \(p_r\) commute. Thus

\[
p_r a_\beta=\sum_{i=1}^L a_{\beta+r\varepsilon_i},
\tag{36}
\]

where \(\varepsilon_i\) raises only exponent \(i\). The original \(\beta_i\) are strictly decreasing. If the raised exponent equals another exponent, that summand is zero. Otherwise it moves from position \(i\) to a unique position \(j\leq i\) in decreasing order, making \(i-j\) transpositions. The sorted list is \(\lambda+\delta\), with

\[
\lambda_j=\eta_i+r-(i-j),\qquad
\lambda_k=\eta_{k-1}+1\ (j<k\leq i),\qquad
\lambda_k=\eta_k\ (k<j\text{ or }k>i).
\tag{37}
\]

Distinct decreasing nonnegative exponents ensure that this is a partition. The raised exponent being above \(\beta_j\) ensures \(\lambda_j>\eta_j\); every other indicated row also grows. The added boxes occupy the consecutive rows \(j,\ldots,i\). In two consecutive such rows \(k-1,k\), the upper added row starts at column \(\eta_{k-1}+1\), and the lower added row ends at that same column, by (37). They overlap in exactly one column. Hence the skew diagram is connected and has no \(2\times2\) block. It has size \(r\), by summing (37), and height \(i-j\), exactly the determinant sign.

Conversely, let \(\lambda/\eta\) be a border strip. Its nonempty rows are consecutive, say \(j,\ldots,i\). For adjacent occupied rows, their added intervals overlap; the absence of a \(2\times2\) block forces that overlap to have length one. Since \(\eta\) and \(\lambda\) are partitions, this forces \(\lambda_k=\eta_{k-1}+1\) for \(j<k\leq i\). Summing the added row lengths, of total \(r\), gives the first formula in (37). Thus the strip comes from raising exactly \(\beta_i\) by \(r\) and sorting. The sorted list has distinct entries, so this summand was not discarded. The correspondence is bijective and preserves the sign. Divide (36) by \(\Delta\) and use (10). Stability proves (35) in \(\Lambda\). \(\square\)

**Theorem 4.3 (Murnaghan–Nakayama).** For an ordered list of the positive parts \(\mu_1,\ldots,\mu_k\) of a cycle type,

\[
\chi^\lambda(\mu)
=\sum_{\varnothing=\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\subset\lambda^{(k)}=\lambda}
\prod_{i=1}^k(-1)^{\operatorname{ht}(\lambda^{(i)}/\lambda^{(i-1)})},
\tag{38}
\]

where the \(i\)-th difference must be a border strip of size \(\mu_i\). Such a chain is a border-strip tableau of type \(\mu\).

**Proof.** Start with \(s_\varnothing=1\) and apply (35) successively with \(r=\mu_1,\ldots,\mu_k\). Each multiplication adds one permitted strip and multiplies its sign into the preceding coefficient. The coefficient of \(s_\lambda\) in the result \(p_\mu\) is therefore the sum in (38). By (34) it is \(\chi^\lambda(\mu)\). Commutativity of the power sums also proves that this signed count is independent of the chosen order of the parts. \(\square\)

For calculation one may remove the strips in reverse order:

\[
\chi^\lambda((r)\cup\nu)
=\sum_{\eta\subset\lambda:\,\lambda/\eta\text{ border strip of size }r}
(-1)^{\operatorname{ht}(\lambda/\eta)}\chi^\eta(\nu).
\tag{39}
\]

Use \(\chi^\varnothing(\varnothing)=1\). If \(\nu\) consists only of ones, the value is \(f^\eta\), computed by the hook formula or the branching recursion in *Branching, Jucys–Murphy elements and Young's seminormal form*, Theorems 6.3 and 4.2. Invalid removals contribute nothing.

The determinant exponent calculation proves the strip identity (35), including its sign; repeated multiplication and (34) give the character rule. Both Vandermonde and selected exponent orders use the descending convention (9).

## 5. Two full character tables and all degree-four permutation modules

Here is the full \(S_4\) table. Row labels are shapes and column labels are cycle types. The second row gives class sizes.

| Shape | \(1^4\) | \(2\,1^2\) | \(2^2\) | \(3\,1\) | \(4\) |
|---|---:|---:|---:|---:|---:|
| Class size | 1 | 6 | 3 | 8 | 6 |
| \((4)\) | 1 | 1 | 1 | 1 | 1 |
| \((3,1)\) | 3 | 1 | −1 | 0 | −1 |
| \((2,2)\) | 2 | 0 | 2 | −1 | 0 |
| \((2,1,1)\) | 3 | −1 | −1 | 0 | 1 |
| \((1^4)\) | 1 | −1 | 1 | 1 | −1 |

All entries follow from the removal recursion (39). For \((2,2)\), the two possible two-box removals leave \((2)\) and \((1,1)\), with heights \(0\) and \(1\). Thus

\[
\chi^{(2,2)}(2,1,1)=1-1=0,\qquad
\chi^{(2,2)}(2,2)=1-(-1)=2.
\tag{40}
\]

A three-box removal leaves \((1)\), with height \(1\), giving \(-1\). The whole \((2,2)\) diagram is not a border strip, so the four-cycle value is zero. For any full \(n\)-cycle, the value is zero unless the entire shape is a hook \((n-a,1^a)\), in which case it is \((-1)^a\). This explains the last column for every shape in both tables.

The full \(S_5\) table is:

| Shape | \(1^5\) | \(2\,1^3\) | \(2^2\,1\) | \(3\,1^2\) | \(3\,2\) | \(4\,1\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Class size | 1 | 10 | 15 | 20 | 20 | 30 | 24 |
| \((5)\) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| \((4,1)\) | 4 | 2 | 0 | 1 | −1 | 0 | −1 |
| \((3,2)\) | 5 | 1 | 1 | −1 | 1 | −1 | 0 |
| \((3,1,1)\) | 6 | 0 | −2 | 0 | 0 | 0 | 1 |
| \((2,2,1)\) | 5 | −1 | 1 | −1 | −1 | 1 | 0 |
| \((2,1,1,1)\) | 4 | −2 | 0 | 1 | 1 | 0 | −1 |
| \((1^5)\) | 1 | −1 | 1 | 1 | −1 | −1 | 1 |

For the shape \((3,2)\), the only two-box border-strip removal leaves \((3)\), with positive sign. This gives both values \(1\) in the two columns beginning with \(2\). Its only three-box border-strip removal leaves \((1,1)\), with height \(1\). The removed boxes, in their original coordinates, are

\[
\begin{array}{ccc}
&\boxed{\ast}&\boxed{\ast}\\
&\boxed{\ast}&
\end{array}.
\tag{41}
\]

Therefore its values at \((3,1,1)\) and \((3,2)\) are respectively \(-1\) and \(-\chi^{(1,1)}(2)=1\). Its four-box removal leaves \((1)\), with height \(1\), giving \(-1\); its whole diagram contains a square, giving zero at \((5)\). Finally \(f^{(3,2)}=5\). This derives the entire row. For \((3,1,1)\), the two-box removals leave \((1,1,1)\) with sign \(+1\) and \((3)\) with sign \(-1\), giving \(-2\) at \((2,2,1)\).

For all rows, apply the same recursion to the indicated cycle lengths; the identity column uses the corner recursion. As independent arithmetic checks, the displayed class sizes sum to \(24\) and \(120\), and the squared row dimensions sum to those same orders. The weighted inner products of distinct rows are zero and of each row with itself are one. These checks verify the resulting tables; they do not replace the general proof of the rule.

Now order the partitions of four as \((4),(3,1),(2,2),(2,1,1),(1^4)\). The complete Kostka matrix, with shape rows and content columns in that order, is

\[
K=\begin{pmatrix}
1&1&1&1&1\\
0&1&1&2&3\\
0&0&1&1&2\\
0&0&0&1&3\\
0&0&0&0&1
\end{pmatrix}.
\tag{42}
\]

For instance, content \((2,1,1)\) means two ones, one two and one three. In shape \((3,1)\), the bottom entry is either two or three, and the top row is then forced; hence the entry \(2\). In shape \((2,2)\), the top row must be the two ones and the bottom row is two, three, giving \(1\). In shape \((2,1,1)\), the first column is one, two, three and the remaining top box is one, again giving \(1\). The last column counts standard tableaux and is \((1,3,2,3,1)^t\).

By (32), every Young permutation module of \(S_4\) is now specified:

\[
\begin{aligned}
M^{(4)}&=V_{(4)},\\
M^{(3,1)}&=V_{(4)}\oplus V_{(3,1)},\\
M^{(2,2)}&=V_{(4)}\oplus V_{(3,1)}\oplus V_{(2,2)},\\
M^{(2,1,1)}&=V_{(4)}\oplus2V_{(3,1)}\oplus V_{(2,2)}\oplus V_{(2,1,1)},\\
M^{(1^4)}&=V_{(4)}\oplus3V_{(3,1)}\oplus2V_{(2,2)}
\oplus3V_{(2,1,1)}\oplus V_{(1^4)}.
\end{aligned}
\tag{43}
\]

Here equality means isomorphism of representations, and a coefficient means that many direct-sum copies. Their dimensions are respectively \(1,4,6,12,24\), agreeing with \(4!/\prod_i\mu_i!\). Rearranging the parts of a composition conjugates its Young subgroup, so this list covers all compositions as well as partitions.

## 6. Littlewood–Richardson: counting induction multiplicities

Let \(\alpha\vdash m\), \(\beta\vdash n\), and \(\lambda\vdash m+n\). Define \(c^\lambda_{\alpha\beta}\) by

\[
s_\alpha s_\beta=\sum_\lambda c^\lambda_{\alpha\beta}s_\lambda.
\tag{44}
\]

The already proved characteristic theorem gives

\[
\operatorname{Ind}_{S_m\times S_n}^{S_{m+n}}(V_\alpha\boxtimes V_\beta)
\cong\bigoplus_\lambda c^\lambda_{\alpha\beta}V_\lambda.
\tag{45}
\]

Thus these coefficients are nonnegative integers. We now describe which tableaux count them. Define \(s_{\lambda/\alpha}\) as the weight sum of semistandard fillings of the skew diagram; set it to zero if \(\alpha\not\subset\lambda\). The same weak-row and strict-column inequalities apply wherever two neighboring boxes belong to the diagram.

**Lemma 6.1 (interchanging two adjacent labels).** Skew tableau weight sums are symmetric. More precisely, there is an involution interchanging the total numbers of \(k\) and \(k+1\), for each \(k\).

**Proof.** Keep fixed every \(k\) and \(k+1\) lying together in one column. Call the remaining occurrences free. In each row the fixed \(k\)'s form a left segment of its \(k\)-block, and the fixed \(k+1\)'s form a right segment of its \(k+1\)-block. Here is a direct way to check the assertion. Let \(a_r,b_r,c_r\) be the last column of row \(r\) occupied by the inner diagram or by an entry respectively smaller than \(k\), at most \(k\), and at most \(k+1\). These are three partitions, with

\[
b_{r+1}\leq a_r,\qquad c_{r+1}\leq b_r.
\]

The inequalities hold because equal entries cannot share a column. The \(k\)-block is \((a_r,b_r]\), and the \(k+1\)-block is \((b_r,c_r]\). Intersect the first with the lower row's \(k+1\)-block: its left endpoint is at most \(a_r\), so its fixed positions are a left segment. Intersect the second with the upper row's \(k\)-block: its right endpoint is at least \(c_r\), so its fixed positions are a right segment. Thus all free positions in a row form one interval, filled by some \(k\)'s followed by some \(k+1\)'s.

Replace \(u\) free \(k\)'s followed by \(v\) free \(k+1\)'s by \(v\) free \(k\)'s followed by \(u\) free \(k+1\)'s. Rows remain weakly increasing. A free position has no opposite label in its column, so its other column entries are smaller than \(k\) above and larger than \(k+1\) below; either new label is permitted. At most one free position is changed in any column. The fixed pairs stay fixed and the free positions stay free. Applying the operation twice returns the tableau. Each fixed pair contributes one of each label, and the free totals are interchanged, proving the assertion. This is the Bender–Knuth involution. \(\square\)

**Proposition 6.2 (skew coefficients and products).**

\[
s_{\lambda/\alpha}=\sum_\beta c^\lambda_{\alpha\beta}s_\beta.
\]

**Proof.** Put every letter of an alphabet \(x\) before every letter of an alphabet \(y\). In a tableau of shape \(\lambda\), the boxes with \(x\)-letters form a partition \(\alpha\), and the remaining boxes form \(\lambda/\alpha\). Conversely two such tableaux combine uniquely; the inequalities across their boundary hold because all \(x\)-letters precede all \(y\)-letters. Consequently

\[
s_\lambda(x,y)=\sum_{\alpha\subset\lambda}s_\alpha(x)s_{\lambda/\alpha}(y).
\]

The kernel satisfies \(\mathcal K(x\cup y,z)=\mathcal K(x,z)\mathcal K(y,z)\), directly from its product. Expand both sides using (20), and expand \(s_\alpha(z)s_\beta(z)\) using (44). Comparing Schur coefficients in \(z\), and then in \(x\), gives the asserted identity. Every comparison can be made in a fixed degree and enough variables, so it involves finite sums. \(\square\)

**Theorem 6.3 (Littlewood–Richardson).** The coefficient \(c^\lambda_{\alpha\beta}\) is the number of semistandard tableaux of shape \(\lambda/\alpha\) and content \(\beta\) whose word, read right to left across each row from the top row down, has at least as many \(k\)'s as \(k+1\)'s in every prefix, for every \(k\geq1\). The coefficient is zero if \(\alpha\not\subset\lambda\).

**Proof: cancellation.** Use \(L\) labels, with \(L\) at least the number of skew boxes, and write \(w(T)\) for the content vector. Since Lemma 6.1 makes the skew weight sum symmetric, alternating \(x^\delta s_{\lambda/\alpha}\) gives

\[
\Delta s_{\lambda/\alpha}=\sum_T a_{w(T)+\delta}.
\]

For a column \(j\), let \(T_{\geq j}\) contain all boxes in columns at least \(j\). Call a tableau admissible when \(w(T_{\geq j})\) is a partition for every \(j\). In an inadmissible tableau choose the largest failing \(j\), then the smallest failing adjacent pair \(k,k+1\). Columns contain each label at most once, and the columns to its right satisfy all the inequalities. Therefore column \(j\) contains \(k+1\) and no \(k\), and

\[
w_k(T_{\geq j})+1=w_{k+1}(T_{\geq j}).
\]

Apply Lemma 6.1 to the tableau strictly left of column \(j\). That region is itself a skew diagram, obtained by clipping both boundary partitions at \(j-1\). The boundary row inequalities remain valid: column \(j\) has no \(k\), so increasing a left-hand \(k\) cannot put it above the boundary value; decreasing a \(k+1\) also causes no boundary problem. Call the result \(T^*\). The unchanged right-hand region selects the same \(j,k\) on the second application. Thus this operation is an involution. The displayed equality and \(\delta_k-\delta_{k+1}=1\) show that

\[
w(T^*)+\delta=s_k\bigl(w(T)+\delta\bigr),
\qquad a_{w(T^*)+\delta}=-a_{w(T)+\delta},
\]

where \(s_k\) interchanges coordinates \(k,k+1\). Paired terms cancel. If the involution fixes a tableau, the corresponding exponent vector has equal adjacent coordinates and its alternant is zero. For an admissible tableau, \(w(T)\) is a partition and its term is \(\Delta s_{w(T)}\). Dividing by \(\Delta\) and applying Proposition 6.2 proves that the coefficient counts admissible tableaux of content \(\beta\).

**Proof: the reading condition.** Fix \(k\), and use the boundary partitions \(a,b,c\) from Lemma 6.1. Set \(A_r=b_r-a_r\) and \(B_r=c_r-b_r\). In the row word, the \(k+1\)'s of a row occur before its \(k\)'s. Hence the smallest balance during row \(r\) is

\[
R_r=\sum_{s<r}A_s-\sum_{s\leq r}B_s.
\]

The row word has the required inequality exactly when every \(R_r\geq0\). Let \(C(j)\) be the number of \(k\)'s minus \(k+1\)'s in columns at least \(j\). At \(j=b_r+1\), all the \(k\)'s in earlier rows and all the \(k+1\)'s in rows through \(r\) lie to the right of this cut; later rows contribute neither. The strip inequalities \(b_{r+1}\leq a_r\) and \(c_{r+1}\leq b_r\) give exactly \(C(b_r+1)=R_r\). Thus nonnegative column balances imply nonnegative row balances.

For the converse, a column can lower the balance when added from right to left only if it contains \(k+1\) without \(k\). Suppose that \(k+1\) lies in row \(r\), so \(b_r<j\leq c_r\). Counting the intervals \((a_s,b_s]\) and \((b_s,c_s]\), using the same strip inequalities, gives

\[
C(j)=R_r+\min\{j-1,a_{r-1}\}-b_r\ \geq R_r;
\]

for \(r=1\), interpret \(a_0=+\infty\). To check the count, rows above \(r-1\) contribute their full \(k\)-blocks, row \(r-1\) contributes \(b_{r-1}-\max\{a_{r-1},j-1\}\), and rows below contribute no \(k\). The \(k+1\)-blocks above row \(r\) contribute fully, and row \(r\) contributes \(c_r-j+1\). Their difference is the displayed expression. Its last term is nonnegative because \(a_{r-1}\geq b_r\) and \(j-1\geq b_r\). If all \(R_r\) are nonnegative, every possible lowering column therefore leaves a nonnegative balance; other columns cannot lower it. All \(C(j)\) are nonnegative. This proves equivalence of the two conditions for each \(k\), completing the theorem. \(\square\)

For example, \(c^{(3,2,1)}_{(2,1),(2,1)}=2\). The skew diagram has one box in each row, in columns three, two and one. The two permitted fillings, with their original positions retained, are

\[
\begin{array}{ccc}&&\boxed{1}\\&\boxed{1}&\\\boxed{2}&&\end{array}
\qquad
\begin{array}{ccc}&&\boxed{1}\\&\boxed{2}&\\\boxed{1}&&\end{array}.
\]

Their row words are \(112\) and \(121\), both satisfying the prefix inequalities. The third arrangement, with word \(211\), fails at its first letter. Equation (45) therefore gives multiplicity two for \(V_{(3,2,1)}\) in \(\operatorname{Ind}_{S_3\times S_3}^{S_6}(V_{(2,1)}\boxtimes V_{(2,1)})\).

*Comparison:* [Stembridge, theorem and skew-Schur corollary], for the column cancellation. The proof above supplies the boundary cases and proves the equivalence with the row-reading condition, so no tableau insertion theorem is imported.

## 7. Exercises with complete solutions

### Exercise 1 (easy). The regular representation

Compute the characteristic of the regular character of \(S_n\). Explain why the answer agrees with its irreducible decomposition.

**Solution.** The regular character is \(n!\) at the identity and zero elsewhere. As \(z_{(1^n)}=n!\), (24) gives

\[
\operatorname{ch}(\chi_{\mathrm{reg}})=p_1^n=h_1^n.
\tag{46}
\]

By (23), \(h_{(1^n)}=\sum_\lambda K_{\lambda,(1^n)}s_\lambda=\sum_\lambda f^\lambda s_\lambda\). The characteristic theorem and Corollary 4.3 of *Branching, Jucys–Murphy elements and Young's seminormal form* therefore give \(\mathbb C[S_n]\cong\bigoplus_\lambda(\dim V_\lambda)V_\lambda\), as the finite-group regular decomposition requires. For \(n=0\), both sides of (46) are \(1\).

### Exercise 2 (medium). Count the fixed points using Frobenius's formula

For \(n\geq2\), derive

\[
\chi^{(n-1,1)}(\sigma)=m_1(\operatorname{type}(\sigma))-1
\tag{47}
\]

directly from (33).

**Solution.** Use two variables, so \(\delta=(1,0)\), \(\Delta=x_1-x_2\), and \(\lambda+\delta=(n,1)\). Write \(\mu=(\mu_1,\ldots,\mu_k)\) for the cycle lengths. Formula (33) is the coefficient of \(x_1^n x_2\) in

\[
(x_1-x_2)\prod_{j=1}^k(x_1^{\mu_j}+x_2^{\mu_j}).
\tag{48}
\]

The \(x_1\) term requires coefficient \(x_1^{n-1}x_2\) in the product. Choose exactly one length-one cycle to contribute \(x_2\), with all other cycles contributing powers of \(x_1\). There are \(m_1(\mu)\) choices. The \(-x_2\) term requires coefficient \(x_1^n\), which is \(1\). This gives (47). At the identity it gives dimension \(n-1\); at an \(n\)-cycle it gives \(-1\), consistent with the height-one hook. In particular, the natural action on \(n\) points has character \(1+\chi^{(n-1,1)}\).

### Exercise 3 (medium). Young's rule without a label ambiguity

Derive the decomposition of \(M^\mu\) from Theorem 3.1 and the tableau formula. Specify the content convention and recover \(M^{(2,1,1)}\) for \(S_4\).

**Solution.** A tableau of content \(\mu=(\mu_1,\ldots,\mu_k)\) contains \(\mu_i\) copies of the integer \(i\). By complete reducibility, the multiplicity of the previously defined \(V_\lambda\) in \(M^\mu\) is

\[
\langle\chi_{M^\mu},\chi^\lambda\rangle
=\langle h_\mu,s_\lambda\rangle
=K_{\lambda\mu}.
\tag{49}
\]

The first equality is character orthogonality, the second uses the isometry and the exact labels in (27), and the third expands (16) and uses \(h/m\) duality. This proves the full decomposition, for any composition. For \(\mu=(2,1,1)\), the five counts are \(1,2,1,1,0\), as counted after (42). Hence \(M^\mu=V_{(4)}\oplus2V_{(3,1)}\oplus V_{(2,2)}\oplus V_{(2,1,1)}\). Its dimension is \(1+2\cdot3+2+3=12=4!/(2!1!1!)\). Omitting the label proof in Theorem 3.1 would leave the identification in this answer unjustified.

### Exercise 4 (hard). From one border strip to all character values

Starting with the product identity (35), prove the full rule (38), including independence of part order. Calculate \(\chi^{(3,2)}(3,2)\), distinguishing an actual strip from a disconnected attempted removal.

**Solution.** Prove by induction on \(k\) that the coefficient of \(s_\lambda\) in \(p_{\mu_1}\cdots p_{\mu_k}\) is the signed sum over the chains in (38). For \(k=0\) the only coefficient is that of the empty shape and equals \(1\). In the inductive step, multiply the preceding Schur expansion by \(p_{\mu_k}\). Identity (35) extends each chain by exactly every possible last strip and multiplies its contribution by \((-1)^{\operatorname{ht}}\). Conversely every chain with \(k\) steps has a unique preceding chain and last strip, so neither terms nor multiplicities are lost. Equation (34) identifies the final coefficient with the character value. The product of the \(p_{\mu_i}\) is invariant under rearrangement, proving order independence of the entire signed sum.

For \((3,2)\), remove a strip of length three. The possible remaining partitions of size two contained in the shape are \((2)\) and \((1,1)\). The attempted remainder \((2)\) leaves a top box in column three and two lower boxes in columns one and two; the top box touches none of them along an edge, so it is inadmissible. The remainder \((1,1)\) leaves the connected strip in (41), of height one. Therefore

\[
\chi^{(3,2)}(3,2)=(-1)\chi^{(1,1)}(2)=(-1)(-1)=1.
\tag{50}
\]

The final \(-1\) comes from the height-one vertical two-box strip of \((1,1)\). Thus the sign at each stage has a specified geometric source.

## References

- [Grinberg–Reiner] Darij Grinberg and Victor Reiner, [*Hopf Algebras in Combinatorics*](https://www.cip.ifi.lmu.de/~grinberg/algebra/HopfComb.pdf), July 27, 2020, minor corrections September 6, 2026, Proposition 2.5.15, pp. 64–66, Corollary 2.5.17, Proposition 2.6.4 and Corollary 2.6.7. CC BY 4.0. Only the component explicitly credited in Lemma 1.2 is adapted from this work.
- [Stembridge] John R. Stembridge, “A Concise Proof of the Littlewood–Richardson Rule,” *Electronic Journal of Combinatorics* 9 (2002), N5, theorem and skew-Schur corollary. [Journal article](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1n5).

The next lesson uses Schur functions to describe the two commuting actions in Schur–Weyl duality.

# Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

At level one, the Hecke operators are self-adjoint and their common eigenspaces are lines. At higher level, a character enters the adjoint formula, and forms inherited from a smaller level can share every eigenvalue away from the level. We will derive these changes from explicit matrices. The resulting formulas also explain why the operator at a prime dividing the level can fail to be normal.

Throughout, \(N\ge1\), \(k\ge2\) is an integer, \(q=e^{2\pi iz}\), and
\[
 \Gamma=\Gamma_1(N)=
 \left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z):
 a\equiv d\equiv1,\ c\equiv0\pmod N\right\}.
\]
For a positive-determinant rational matrix \(\alpha\), use the unitary slash
\[
 (f\Vert_k\alpha)(z)
 =\det(\alpha)^{k/2}(cz+d)^{-k}f(\alpha z).
 \tag{0.1}
\]
The real power of the determinant is positive. Positive scalar matrices act trivially, and \(f\Vert_k\alpha=f|_k\alpha\) when \(\det\alpha=1\). On cusp forms, the Petersson product is linear in its first argument:
\[
 \langle f,g\rangle_\Gamma
 =\frac1{[\overline{SL_2(\mathbb Z)}:\bar\Gamma]}
 \int_{\Gamma\backslash\mathfrak H}
 f(z)\overline{g(z)}y^k\,\frac{dx\,dy}{y^2}.
 \tag{0.2}
\]
The bars denote images in \(PSL_2(\mathbb R)\). This is the normalization of the preceding Petersson lesson, including when \(-I\notin\Gamma\).

## 1. Diamond operators and character spaces

The lower-right entry gives the surjection
\[
 \Gamma_0(N)\longrightarrow(\mathbb Z/N\mathbb Z)^\times,\qquad
 \begin{pmatrix}a&b\\c&d\end{pmatrix}\longmapsto d\bmod N,
 \tag{1.1}
\]
with kernel \(\Gamma\), as proved in the congruence-subgroup lesson. In particular \(\Gamma\) is normal in \(\Gamma_0(N)\).

For a unit \(u\bmod N\), choose \(\sigma_u\in\Gamma_0(N)\) whose lower-right entry is \(u\bmod N\), and define
\[
 [u]f=f|_k\sigma_u.
 \tag{1.2}
\]
We also write \(\langle u\rangle\) for this diamond operator. Its index is the **lower-right** entry. An upper-left indexing convention replaces \(u\) by \(u^{-1}\).

Normality makes (1.2) a well-defined operator on \(M_k(\Gamma)\), independent of the lift, with
\[
 [u][v]=[uv],\qquad [1]=I.
 \tag{1.3}
\]
For example, two lifts differ by a factor in \(\Gamma\); their slash actions on a \(\Gamma\)-invariant function agree. Right multiplication of cusp scaling matrices shows that diamonds preserve holomorphy and vanishing at every cusp.

A Dirichlet character modulo \(N\) means a homomorphism
\(\chi:(\mathbb Z/N\mathbb Z)^\times\to\mathbb C^\times\), extended to integers by zero on nonunits. Define
\[
 M_k(N,\chi)=\{f\in M_k(\Gamma):[u]f=\chi(u)f\text{ for every unit }u\},
 \qquad S_k(N,\chi)=M_k(N,\chi)\cap S_k(\Gamma).
\]
Equivalently, \(f|_k\gamma=\chi(d)f\) for every
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma_0(N)\).

**Theorem 1.1 (nebentypus decomposition).** There are direct sums
\[
 M_k(\Gamma)=
 \bigoplus_{\chi(-1)=(-1)^k}M_k(N,\chi),\qquad
 S_k(\Gamma)=
 \bigoplus_{\chi(-1)=(-1)^k}S_k(N,\chi).
 \tag{1.4}
\]

**Proof.** Each diamond has finite order, so its minimal polynomial divides some \(X^r-1\). The latter has distinct complex roots. Thus each diamond is diagonalizable. They commute by (1.3). To diagonalize them together, decompose into eigenspaces of one diamond; every other diamond preserves these spaces, and its restriction is still annihilated by a polynomial with distinct roots. Repeat for the finitely many units. A common eigenvector has eigenvalues \(c(u)\ne0\) satisfying \(c(uv)=c(u)c(v)\), so \(c\) is a character.

The joint eigenspaces give a direct sum: eigenspaces with distinct eigenvalues for any one operator intersect trivially, and the successive decompositions span the original space. Finally the lift \(-I\) gives
\([-1]f=(-1)^kf\). Therefore only the displayed parity occurs. The same argument applies to the invariant cusp subspace. \(\square\)

No Petersson product on the whole space \(M_k(\Gamma)\) was used: Eisenstein series generally have divergent norms.

## 2. The prime double cosets and their coefficients

Put
\[
 \alpha_p=\begin{pmatrix}1&0\\0&p\end{pmatrix},\qquad
 \delta_b=\begin{pmatrix}1&b\\0&p\end{pmatrix}
 \quad(0\le b<p).
\]
For \(p\nmid N\), choose integers \(a,b_0\) with \(ap-b_0N=1\), and set
\[
 \sigma_p=\begin{pmatrix}a&b_0\\N&p\end{pmatrix},
 \qquad \delta_\infty=\sigma_p\begin{pmatrix}p&0\\0&1\end{pmatrix}.
 \tag{2.1}
\]
Here \(\sigma_p\in\Gamma_0(N)\) represents \([p]\).

**Lemma 2.1 (the representatives).**
\[
 \Gamma\alpha_p\Gamma=
 \begin{cases}
 \displaystyle\bigsqcup_{b=0}^{p-1}\Gamma\delta_b
 \ \sqcup\ \Gamma\delta_\infty,&p\nmid N,\\[4pt]
 \displaystyle\bigsqcup_{b=0}^{p-1}\Gamma\delta_b,&p\mid N.
 \end{cases}
 \tag{2.2}
\]

**Proof.** Left cosets in this double coset correspond to
\(H\backslash\Gamma\), where
\[
 H=\Gamma\cap\alpha_p^{-1}\Gamma\alpha_p
 =\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma:p\mid b\right\}.
\]
Indeed \(\Gamma\alpha_p\gamma_1=\Gamma\alpha_p\gamma_2\) exactly when
\(\gamma_1\gamma_2^{-1}\in H\).

If \(p\mid N\), reduction of \(\Gamma\) modulo \(p\) consists of all upper unipotent matrices, while reduction of \(H\) is the identity. The matrices \(T^b\), \(0\le b<p\), represent the \(p\) cosets.

If \(p\nmid N\), reduction of \(\Gamma\) onto \(SL_2(\mathbb F_p)\) is surjective. This follows from the surjectivity of integral reduction proved earlier, applied modulo \(Np\), with the identity prescribed modulo \(N\). The subgroup \(H\) is the inverse image of the lower triangular subgroup. Its cosets are indexed by first-row lines in \(\mathbb F_p^2\). The first rows of \(T^b\) give \([1:b]\); the remaining line is represented by
\[
 \gamma_\infty=\begin{pmatrix}ap&b_0\\N&1\end{pmatrix}\in\Gamma.
\]
Its first row is \([0:b_0]\) modulo \(p\), with \(b_0\ne0\bmod p\), and
\(\alpha_p\gamma_\infty=\delta_\infty\). These are all \(p+1\) cosets. \(\square\)

Define
\[
 T_pf=p^{k/2-1}
 \sum_{\Gamma\delta\subset\Gamma\alpha_p\Gamma}f\Vert_k\delta.
 \tag{2.3}
\]
When \(p\mid N\), we use the name \(U_p\) for this operator.

The double-coset sum is \(\Gamma\)-modular by reindexing after right multiplication by \(\Gamma\). It is holomorphic on \(\mathfrak H\) and preserves every cusp condition. Here is the latter assertion in detail. For any integral cusp scaling matrix \(\beta\) and any rational positive-determinant \(\delta\), choose \(\gamma\in SL_2(\mathbb Z)\) taking \(\infty\) to \(\delta\beta\infty\). Then
\(\gamma^{-1}\delta\beta\) is rational upper triangular with positive ratio of diagonal entries. Thus \(f\Vert_k\delta\beta\) is a constant multiple of \(f|_k\gamma\) composed with a positive rational affine map. A bounded cusp expansion remains bounded, and a vanishing cusp expansion remains vanishing. The resulting modular function is periodic with its actual positive cusp period, so its bounded Fourier expansion has no negative terms. This also respects the antiperiodic odd-weight expansions at irregular cusps.

**Lemma 2.2 (diamonds commute with prime operators).** Every \(T_p\), including \(U_p\), commutes with every diamond.

**Proof.** Consider the set
\[
 \mathcal D_p=
 \left\{A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb Z):
 \det A=p,\ a\equiv1,\ c\equiv0\pmod N\right\}.
 \tag{2.4}
\]
We first show that it is exactly \(\Gamma\alpha_p\Gamma\). The inclusion of the double coset in (2.4) follows by reducing both factors in \(\Gamma\) modulo \(N\).

For the reverse inclusion let \(r=\gcd(a,c)>0\), so \(r=1\) or \(p\). If \(r=1\), choose \(u,v\) with \(ua+vc=1\). Modulo \(N\), this gives \(u\equiv1\), hence
\[
 \begin{pmatrix}u&v\\-c&a\end{pmatrix}\in\Gamma.
\]
Multiplication sends \(A\) to \(\left(\begin{smallmatrix}1&B\\0&p\end{smallmatrix}\right)\); multiplication by a power of \(T\) reduces \(B\) modulo \(p\), giving one of the \(\delta_b\).

If \(r=p\), necessarily \(p\nmid N\). The divided first column \((a/p,c/p)^t\) is primitive and congruent to \((p^{-1},0)^t\bmod N\). Complete it to a matrix
\(\eta=\left(\begin{smallmatrix}a/p&x\\c/p&y\end{smallmatrix}\right)\in SL_2(\mathbb Z)\). Then \(y\equiv p\bmod N\). Replacing its second column by that column plus \(t\) times the first lets us arrange \(x\equiv b_0\bmod N\), since \(a/p\) is a unit modulo \(N\). Now \(\eta\equiv\sigma_p\bmod N\), so \(\sigma_p\eta^{-1}\in\Gamma(N)\). Multiplication sends \(A\) to
\(\sigma_p\left(\begin{smallmatrix}p&B\\0&1\end{smallmatrix}\right)\). Left multiplication by
\(\sigma_pT^{-B}\sigma_p^{-1}\in\Gamma\) gives \(\delta_\infty\).
Thus (2.4) has precisely the representatives in (2.2).

Conjugation by any \(\sigma_u\in\Gamma_0(N)\) preserves (2.4). Integrality and determinant are preserved; modulo \(N\), conjugation by an invertible upper triangular matrix preserves the diagonal entries \(1,p\) and the zero lower-left entry. Normality of \(\Gamma\) therefore makes this conjugation a permutation of the left cosets in (2.4). In the slash sum, write
\(\delta\sigma_u=\sigma_u(\sigma_u^{-1}\delta\sigma_u)\) and reindex. This proves \(T_p[u]=[u]T_p\). \(\square\)

**Theorem 2.3 (prime coefficient formula).** For \(f=\sum_{m\ge0}a_mq^m\in M_k(N,\chi)\),
\[
 \begin{aligned}
 T_pf(z)&=\frac1p\sum_{b=0}^{p-1}
 f\left(\frac{z+b}{p}\right)+\chi(p)p^{k-1}f(pz)
 &&(p\nmid N),\\
 U_pf(z)&=\frac1p\sum_{b=0}^{p-1}
 f\left(\frac{z+b}{p}\right)
 &&(p\mid N).
 \end{aligned}
 \tag{2.5}
\]
Consequently, with \(a_{m/p}=0\) when \(p\nmid m\),
\[
 a_m(T_pf)=a_{pm}+\chi(p)p^{k-1}a_{m/p},\qquad
 a_m(U_pf)=a_{pm}.
 \tag{2.6}
\]
For \(m=0\), use \(a_{0/p}=a_0\).

**Proof.** In (2.3), each \(\delta_b\) contributes
\(p^{-1}f((z+b)/p)\). The remaining representative in the good case contributes
\(p^{k-1}([p]f)(pz)=\chi(p)p^{k-1}f(pz)\).
Averaging the convergent Fourier series uses
\[
 \frac1p\sum_{b=0}^{p-1}e^{2\pi imb/p}
 =\begin{cases}1,&p\mid m,\\0,&p\nmid m.\end{cases}
\]
Thus the first sum selects \(a_{pm}\), while the second contributes the other term. The constant coefficient follows by the same averaging. \(\square\)

## 3. All indices and commutativity

Set \(T_1=I\). For a good prime \(p\nmid N\), define
\[
 T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}[p]T_{p^{r-1}}
 \quad(r\ge1).
 \tag{3.1}
\]
For \(p\mid N\), set \(T_{p^r}=U_p^r\). For \(n=\prod_pp^{r_p}\), define
\(T_n=\prod_pT_{p^{r_p}}\). The following proof establishes that the prime factors commute, so their ordering has no effect.

**Theorem 3.1.** All \(T_n\) and all diamonds commute. On \(M_k(N,\chi)\),
\[
 a_m(T_nf)=
 \sum_{d\mid\gcd(m,n)}\chi(d)d^{k-1}a_{mn/d^2}.
 \tag{3.2}
\]
The character is extended by zero on nonunits, and \(\gcd(0,n)=n\). In particular \(a_1(T_nf)=a_n(f)\). On the full space,
\[
 T_mT_n=
 \sum_{\substack{d\mid\gcd(m,n)\\(d,N)=1}}
 d^{k-1}[d]T_{mn/d^2}.
 \tag{3.3}
\]

**Proof.** Work first on one character space, which the prime operators preserve by Lemma 2.2. On Fourier coefficient sequences define
\[
 (E_pa)_m=a_{pm},\qquad
 (V_pa)_m=\begin{cases}a_{m/p},&p\mid m,\\0,&p\nmid m.\end{cases}
\]
At \(m=0\), \(V_pa_0=a_0\). Thus \(E_pV_p=I\). Write
\(C_p=\chi(p)p^{k-1}\). Formula (2.6) says \(T_p=E_p+C_pV_p\), with \(C_p=0\) at a bad prime.

Define \(Q_r=\sum_{j=0}^rC_p^jV_p^jE_p^{r-j}\). Using \(E_pV_p^j=V_p^{j-1}\) for \(j\ge1\), multiplication gives
\[
 (E_p+C_pV_p)Q_r=Q_{r+1}+C_pQ_{r-1}.
\]
Since \(Q_0=I\) and \(Q_1=E_p+C_pV_p\), recurrence (3.1) yields \(T_{p^r}=Q_r\). At a bad prime this is simply \(E_p^r\). Applying the expression to the \(m\)-th coefficient gives the prime-power case of (3.2).

For distinct primes \(p,\ell\), each of \(E_p,V_p\) commutes with each of \(E_\ell,V_\ell\), directly from divisibility and the coefficient indices. The scalar \(C_p\) commutes with everything. Hence the prime operators commute on each character space and therefore, by (1.4), on the full space. Lemma 2.2 and (3.1) give commutation with diamonds for all indices. Multiplying the prime-power coefficient formulas gives (3.2).

For completeness, at a good prime the polynomial recurrence \(P_{r+1}=XP_r-QP_{r-1}\), \(P_0=1,P_1=X\), has
\[
 P_uP_v=\sum_{j=0}^{\min(u,v)}Q^jP_{u+v-2j}.
\]
The induction proving this identity was given in the level-one Hecke lesson, Theorem 2.1; it is a polynomial identity, so substitute \(X=T_p\), \(Q=p^{k-1}[p]\). At a bad prime the product is \(U_p^{u+v}\). Multiplication over primes, using (1.3), proves (3.3). \(\square\)

The algebra generated by all these operators and the diamonds is therefore commutative. This assertion includes the bad operators, even though their adjoints will not generally belong to the same algebra.

## 4. Adjoints and the good-prime eigenbasis

**Lemma 4.1 (double-coset adjoint).** For an integral matrix \(\alpha\) of positive determinant \(n\), let
\[
 A_\alpha f=\sum_{\Gamma\delta\subset\Gamma\alpha\Gamma}f\Vert_k\delta,
 \qquad \alpha^*=n\alpha^{-1}.
\]
Then \(A_\alpha^*=A_{\alpha^*}\) on \(S_k(\Gamma)\).

**Proof.** Put
\[
 H=\Gamma\cap\alpha^{-1}\Gamma\alpha,\qquad
 H'=\Gamma\cap\alpha\Gamma\alpha^{-1}=\alpha H\alpha^{-1}.
\]
Both contain \(\Gamma(Nn)\): conjugating \(I+NnB\) by \(\alpha\) or \(\alpha^{-1}\) gives respectively
\(I+N\alpha B\alpha^*\) or \(I+N\alpha^*B\alpha\).
In particular they have finite index. They have the same \(-I\) status as \(\Gamma\), so their relative projective indices equal their relative group indices.

Let \(F\) be a fundamental domain for the projective action of \(\Gamma\), ignoring boundary sets of measure zero. If \(\gamma\) runs through \(H\backslash\Gamma\), then \(\Gamma\alpha\Gamma=\bigsqcup_\gamma\Gamma\alpha\gamma\), and the domains \(\gamma F\) tile a fundamental domain for \(H\). The slash-density identity is
\[
 (f\Vert_k\alpha)(z)\overline{g(z)}\,y^k\,d\mu(z)
 =
 f(w)\overline{(g\Vert_k\alpha^{-1})(w)}
 (\operatorname{Im}w)^k\,d\mu(w),\qquad w=\alpha z.
 \tag{4.1}
\]
It follows directly from \(\operatorname{Im}(\alpha z)=ny/|cz+d|^2\), invariance of \(d\mu\), and (0.1).

Unfold the finite sum over \(\gamma F\), apply (4.1), and note that \(\alpha\) takes the \(H\)-domain to an \(H'\)-domain. Retiling by representatives of \(H'\backslash\Gamma\) gives
\[
 \int_F A_\alpha f\,\bar g\,y^k\,d\mu
 =\int_{H\backslash\mathfrak H}(f\Vert_k\alpha)\bar g\,y^k\,d\mu
 =\int_{H'\backslash\mathfrak H}f\,\overline{g\Vert_k\alpha^{-1}}\,y^k\,d\mu
 =\int_F f\,\overline{A_{\alpha^{-1}}g}\,y^k\,d\mu.
\]
All integrals are absolute: the earlier cusp estimate bounds \(y^{k/2}|f(z)|\) globally, (0.1) gives the same bound for a rational slash, and the domains here have finite hyperbolic area. Multiplication by the fixed normalization in (0.2) changes neither equality. Finally \(\alpha^{-1}\) and \(n\alpha^{-1}\) have identical slash actions, since \(nI\) acts trivially; their coset sums correspond. \(\square\)

**Theorem 4.2.** On \(S_k(\Gamma)\),
\[
 [u]^*=[u]^{-1},\qquad
 T_n^*=[n]^{-1}T_n\quad((n,N)=1).
 \tag{4.2}
\]
All diamonds and good-index Hecke operators are normal. There is an orthonormal basis of simultaneous eigenvectors for this family.

**Proof.** A lift \(\sigma_u\) normalizes \(\Gamma\). Changing variables \(w=\sigma_uz\) in the product takes a \(\Gamma\)-domain to another \(\Gamma\)-domain; the determinant-one case of (4.1) proves
\(\langle[u]f,[u]g\rangle=\langle f,g\rangle\). Thus \([u]\) is unitary and has adjoint \([u]^{-1}\).

For \(p\nmid N\), Lemma 2.1 gives
\(\sigma_p\alpha_p^*=\alpha_p\gamma_\infty\in\Gamma\alpha_p\Gamma\).
Since \(\sigma_p\) normalizes \(\Gamma\),
\[
 \Gamma\alpha_p^*\Gamma
 =\Gamma\sigma_p^{-1}\alpha_p\Gamma.
\]
Hence Lemma 4.1 and the real factor \(p^{k/2-1}\) in (2.3) give
\(T_p^*=[p]^{-1}T_p\).
Taking adjoints in (3.1), and using all the commutations from Theorem 3.1, inductively gives
\(T_{p^r}^*=[p]^{-r}T_{p^r}\). Products over distinct good primes give (4.2).

Every adjoint in (4.2) belongs to the commuting algebra. Each operator therefore commutes with its adjoint and with every other operator's adjoint.

Here is the required spectral argument. A normal operator \(A\) on a finite-dimensional complex inner-product space has an eigenvector \(v\), by the fundamental theorem of algebra. If \(Av=\lambda v\), normality of \(B=A-\lambda I\) implies
\(\|Bv\|^2=\|B^*v\|^2\), so \(A^*v=\bar\lambda v\).
The orthogonal complement of \(v\) is invariant under both \(A\) and \(A^*\); the restriction is normal. Induction gives an orthonormal eigenbasis for \(A\). For the whole commuting family, choose a nonscalar member and split into its eigenspaces. Every member and every adjoint preserves each block, so the restricted family is again commuting and normal. Induct on block dimension; if all members on a block are scalar, any orthonormal basis works. This proves the assertion even for the infinitely indexed family. \(\square\)

On \(S_k(N,\chi)\), (4.2) reads \(T_n^*=\chi(n)^{-1}T_n\). Thus a good eigenvalue \(\lambda_n\) satisfies
\(\overline{\lambda_n}=\chi(n)^{-1}\lambda_n\). For trivial character the good operators are self-adjoint and their eigenvalues are real.

The basis assertion does **not** give multiplicity one at higher level. A vector in a good common eigenspace can have \(a_1=0\); the argument at level one that used every \(T_n\) cannot be repeated with only indices prime to \(N\).

## 5. Old spaces and \(p\)-stabilization

Let \(g\ne0\) belong to \(S_k(\Gamma_0(M))\), let \(p\nmid M\), and suppose
\(T_pg=a_pg\) at level \(M\). Define \(V_pg(z)=g(pz)\).

**Theorem 5.1.** The two forms \(g,V_pg\) belong to \(S_k(\Gamma_0(Mp))\) and are linearly independent. On their span,
\[
 U_pg=a_pg-p^{k-1}V_pg,\qquad U_pV_pg=g,
 \qquad
 [U_p]_{g,V_pg}=
 \begin{pmatrix}a_p&1\\-p^{k-1}&0\end{pmatrix}.
 \tag{5.1}
\]
Matrices act on column coordinate vectors. The characteristic polynomial is
\[
 X^2-a_pX+p^{k-1}.
 \tag{5.2}
\]
If its roots \(\alpha,\beta\) are distinct, the eigenforms
\[
 F_\alpha=g-\beta V_pg,\qquad F_\beta=g-\alpha V_pg
 \tag{5.3}
\]
have eigenvalues \(\alpha,\beta\). The operator on this space is diagonalizable exactly when \(a_p^2\ne4p^{k-1}\).

**Proof.** Put \(\beta_p=\operatorname{diag}(p,1)\). For
\(\gamma\in\Gamma_0(Mp)\), the matrix
\[
 \beta_p\gamma\beta_p^{-1}
 =\begin{pmatrix}a&pb\\c/p&d\end{pmatrix}
\]
lies in \(\Gamma_0(M)\), proving the modularity of \(V_pg\).
The rational affine cusp argument after (2.3) proves its vanishing at every cusp. Inclusion of groups gives the assertion for \(g\).
If \(g\) starts with a nonzero term \(cq^r\), \(r\ge1\), then \(V_pg\) starts with \(cq^{pr}\). These different initial orders prove independence.

At the old level, (2.5) says \(T_pg=U_pg+p^{k-1}V_pg\), where \(U_p\) denotes the coefficient-selection expression now acting at level \(Mp\). Also the coefficient of \(q^{pm}\) in \(g(pz)\) is \(a_m(g)\), so \(U_pV_pg=g\). This proves (5.1), whose determinant gives (5.2). As \(\alpha+\beta=a_p\) and \(\alpha\beta=p^{k-1}\), direct multiplication proves (5.3). If the roots coincide, the matrix is not scalar because its upper-right entry is \(1\). A diagonalizable matrix with just one eigenvalue would be scalar; hence it is not diagonalizable. \(\square\)

Every good operator \(T_\ell\) with \(\ell\nmid Mp\) commutes with the substitution \(V_p\), by its coefficient formula. Thus when \(g\) is a simultaneous eigenform at its old level, the two forms in (5.3) retain its eigenvalues away from \(Mp\).

### 5.1. The discriminant at level two

For \(g=\Delta\), \(k=12\), \(p=2\), the previous lesson gives \(a_2=-24\).
Therefore
\[
 [U_2]_{\Delta,\Delta(2z)}
 =\begin{pmatrix}-24&1\\-2048&0\end{pmatrix},
 \qquad X^2+24X+2048.
\]
Its discriminant is \(576-8192=-7616=-64\cdot119\), so
\[
 \alpha=-12+4i\sqrt{119},\qquad
 \beta=-12-4i\sqrt{119}.
\]
The two stabilizations have expansions
\[
 \begin{aligned}
 \Delta-\beta\Delta(2z)
 &=q+\alpha q^2+252q^3+(-1472+24\beta)q^4+\cdots,\\
 \Delta-\alpha\Delta(2z)
 &=q+\beta q^2+252q^3+(-1472+24\alpha)q^4+\cdots.
 \end{aligned}
\]
They are \(U_2\)-eigenforms with eigenvalues \(\alpha,\beta\), and all their odd-index Hecke eigenvalues agree.

### 5.2. Why \(U_p\) can fail to be normal

A nonsymmetric matrix in a chosen basis alone does not prove nonnormality: the basis need not be orthonormal. We compute the actual inner products.

Write \(J_L\) for the **raw** Petersson integral at level \(L\), and
\(C=J_M(g,g)>0\). The eigenvalue \(a_p\) is real by Theorem 4.2 at the old, trivial-character level. The Gram matrix at level \(Mp\) is
\[
 \begin{pmatrix}
 J_{Mp}(g,g)&J_{Mp}(g,V_pg)\\
 J_{Mp}(V_pg,g)&J_{Mp}(V_pg,V_pg)
 \end{pmatrix}
 =
 C\begin{pmatrix}
 p+1&a_pp^{1-k}\\
 a_pp^{1-k}&(p+1)p^{-k}
 \end{pmatrix}.
 \tag{5.4}
\]
To prove it, inclusion of groups gives the first entry, since
\([\Gamma_0(M):\Gamma_0(Mp)]=p+1\).
For the last entry, \(V_pg=p^{-k/2}g\Vert_k\beta_p\).
Changing variables by \(\beta_p\) takes the level-\(Mp\) group to
\(\Gamma_0(M)\cap\Gamma^0(p)\), also of relative index \(p+1\).
This gives \((p+1)p^{-k}C\).

For the off-diagonal entries, unfold the trace from level \(Mp\) to \(M\).
The subgroup \(\Gamma_0(Mp)\) is
\(\Gamma_0(M)\cap\beta_p^{-1}\Gamma_0(M)\beta_p\).
Thus
\[
 \operatorname{Tr}(V_pg)
 =p^{-k/2}\sum_{\gamma}g\Vert_k\beta_p\gamma
 =p^{1-k}T_pg.
\]
Here the double coset of \(\beta_p\) equals that of \(\alpha_p\) at level \(M\): (2.1) supplies the missing representative and \(\sigma_p\in\Gamma_0(M)\). Integration of this trace against \(g\) proves (5.4). Multiplying all entries by the common positive factor in (0.2) gives the normalized product and changes none of the orthogonality conclusions.

For the conjugate nonreal roots in the discriminant example, linearity in the first argument gives
\[
 J_{Mp}(F_\alpha,F_\beta)
 =C(p-1)\left(\frac{p+1}{p}-a_p\beta p^{-k}\right).
 \tag{5.5}
\]
Indeed substitute (5.3) into (5.4), use
\(\bar\alpha=\beta\) and \(\beta^2=a_p\beta-p^{k-1}\).
For \(p=2,k=12,a_p=-24\), the imaginary part is nonzero.
Distinct eigenvectors of a normal operator are orthogonal, as follows from the spectral argument in Theorem 4.2. These two are not orthogonal, so \(U_2\) is not normal.

**Corollary 5.2 (nonnormality on every such old plane).** Under the hypotheses of Theorem 5.1, \(U_p\) is not normal on \(\operatorname{span}\{g,V_pg\}\) for the actual Petersson product. Consequently it is not normal on the whole cusp space at level \(Mp\).

**Proof.** Let \(A\) be the matrix in (5.1), and let \(G\) be the real symmetric Gram matrix (5.4). Since the product is linear in its first variable, the adjoint matrix \(B\) satisfies \(GB=A^tG\). Direct multiplication, using the displayed entries of \(G\), gives
\[
 B=\begin{pmatrix}0&-1/p\\p^k&a_p\end{pmatrix},\qquad
 AB-BA=
 \begin{pmatrix}
 p^k-p^{k-2}&a_p(1-1/p)\\
 a_pp^{k-1}(1-p)&-(p^k-p^{k-2})
 \end{pmatrix}.
 \tag{5.6}
\]
Its upper-left entry is strictly positive for every prime \(p\) and \(k\ge2\). Thus \(A\) does not commute with its Petersson adjoint, independently of whether its eigenvalues are distinct or real.

Finally, an invariant subspace of a normal operator on a finite-dimensional complex inner-product space has normal restriction. Indeed an orthonormal eigenbasis exists by the spectral argument of Theorem 4.2; the projections onto the distinct eigenspaces are polynomials in that operator, by Lagrange interpolation. They preserve the invariant subspace, which therefore decomposes orthogonally into its intersections with the eigenspaces. The restriction is diagonal in an orthonormal basis of those intersections. The old plane is invariant by (5.1), and its restriction is not normal, so the full operator cannot be normal. \(\square\)

## 6. A complete level eleven example

Let
\[
 H(z)=\eta(z)^2,\qquad
 f(z)=H(z)H(11z)
 =q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2.
 \tag{6.1}
\]
We prove its modularity rather than infer it from a numerical expansion.

The product and discriminant identity in the level-one ring lesson gives \(H^{12}=\Delta\).
For \(\gamma\in SL_2(\mathbb Z)\), the holomorphic nonzero ratio
\((H|_1\gamma)/H\) has twelfth power \(1\), so it is constant; call it \(\mu(\gamma)\).
The slash composition law proves that \(\mu\) is a character.
Writing \(\zeta_{12}=e^{2\pi i/12}\), the product gives
\[
 \mu(T)=\zeta_{12},\qquad \mu(S)=-i=\zeta_{12}^{-3},
 \qquad \mu(-I)=-1=\zeta_{12}^6.
 \tag{6.2}
\]
For the second equality, evaluate \(H|_1S\) at \(i\), where \(Si=i\) and \(H(i)\ne0\).

If \(\gamma\in\Gamma_0(11)\), put
\(\gamma'=\operatorname{diag}(11,1)\gamma\operatorname{diag}(11^{-1},1)\in SL_2(\mathbb Z)\).
The automorphy factors for \(H(z)\) and \(H(11z)\) are both \(cz+d\), so
\[
 f|_2\gamma=\mu(\gamma)\mu(\gamma')f.
 \tag{6.3}
\]
We now verify that the multiplier here is \(1\) for the entire group.

The left cosets \(\Gamma_0(11)\backslash SL_2(\mathbb Z)\) have representatives
\(I,S,ST,\ldots,ST^{10}\), by their lower-row lines modulo \(11\).
Right multiplication by \(T\) passes between consecutive \(ST^r\), with the last transition giving \(U=ST^{11}S^{-1}\); the transition from \(I\) gives \(T\). Right multiplication by \(S\) gives \(-I\) at \(S\), and, for \(1\le r\le10\), gives
\[
 A_r=ST^rS(ST^s)^{-1}
 =\begin{pmatrix}-s&-1\\rs+1&r\end{pmatrix},
 \qquad s\equiv-r^{-1}\pmod{11},\quad1\le s\le10.
\]
These matrices, together with \(T,U,-I\), generate \(\Gamma_0(11)\).
To see generation explicitly, read a word in \(S,T\) and their inverses, replace each partial product by its coset representative, and telescope the successive transitions. The resulting factors are exactly the displayed generators or their inverses.

The exponents of \(\mu(A_r)\) are \(r-s-3\bmod12\), and
\[
 A_r'=\begin{pmatrix}-s&-11\\(rs+1)/11&r\end{pmatrix}.
\]
The following table gives full words for \(A_r'\) and both exponents. Put \(R=S^{-1}\) and \(C_0=-I\), whose exponents are \(3\) and \(6\). Every listed word is checked by ordinary matrix multiplication.

| \(r\) | \(s\) | Word for \(A_r'\) | Exponent of \(\mu(A_r)\) | Exponent of \(\mu(A_r')\) |
|---:|---:|:---|---:|---:|
| 1 | 10 | \(T^{-10}RC_0T\) | 0 | 0 |
| 2 | 5 | \(T^{-5}RC_0T^2\) | 6 | 6 |
| 3 | 7 | \(T^{-4}RT^{-2}RC_0T\) | 5 | 7 |
| 4 | 8 | \(T^{-3}RT^{-3}RC_0T\) | 5 | 7 |
| 5 | 2 | \(T^{-2}RC_0T^5\) | 0 | 0 |
| 6 | 9 | \(T^{-2}RT^{-5}RC_0T\) | 6 | 6 |
| 7 | 3 | \(T^{-2}RT^{-2}RC_0T^3\) | 1 | 11 |
| 8 | 4 | \(T^{-1}RT^3RT^3\) | 1 | 11 |
| 9 | 6 | \(T^{-1}RT^5RT^2\) | 0 | 0 |
| 10 | 1 | \(T^{-1}RC_0T^{10}\) | 6 | 6 |

Each exponent pair sums to \(0\bmod12\). Also \(T'=T^{11}\) and
\(U'=STS^{-1}\), so the exponents for \(T,T'\) are \(1,11\), and for \(U,U'\) are \(11,1\).
The pair \(-I,(-I)'\) has exponents \(6,6\).
Equation (6.3) is therefore \(f|_2\gamma=f\) for every \(\gamma\in\Gamma_0(11)\).

There are two cusps, represented by \(\infty,0\), with widths \(1,11\).
At \(\infty\), (6.1) starts with \(q\). From (6.2),
\(H(-1/z)=-izH(z)\), so
\[
 (f|_2S)(z)=-\frac1{11}H(z)H(z/11)
 =-\frac1{11}q_0+O(q_0^2),\qquad q_0=e^{2\pi iz/11}.
 \tag{6.4}
\]
The leading exponent is \(11/12+1/12=1\) in \(q_0\).
Thus \(f\) vanishes at both cusps. We prove the dimension needed here without the general Riemann–Roch input. The earlier congruence-subgroup calculation gives index twelve and cusp widths \(1,11\). The valence formula proved in the dimension lesson, Theorem 3.1, gives total weighted order \(2\cdot12/12=2\) for every nonzero weight-two form. A cusp form has order at least one at each of the two cusps. If its first coefficient at infinity were zero, its order there would be at least two, giving total order at least three, a contradiction. Thus \(h\mapsto a_1(h)\) injects \(S_2(\Gamma_0(11))\) into \(\mathbb C\). Our nonzero \(f\), with \(a_1(f)=1\), proves that this dimension is exactly one and that \(f\) spans it. The earlier topological genus formula also gives \(g(X_0(11))=1\); its agreement is not used for this dimension proof.

Multiplying (6.1) gives
\[
 f=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7
   +0q^8-2q^9-2q^{10}+q^{11}-2q^{12}+O(q^{13}).
 \tag{6.5}
\]
The full multiplication is detailed in Solution 1.
Every \(T_n\) acts on this line, and \(a_1(f)=1\), so
\(T_nf=a_n(f)f\), including \(U_{11}f=f\).
In particular
\[
 a_2a_3=(-2)(-1)=2=a_6,\qquad
 a_4=a_2^2-2=2.
\]
Further checks are \(a_9=a_3^2-3=-2\),
\(a_8=a_2a_4-2a_2=0\), and \(a_{12}=a_3a_4=-2\).

## 7. Eisenstein series with two characters

We construct the character Eisenstein series from periodic weighted lattice sums. The weight-two convergence argument is part of the construction; coefficient calculations alone would not establish modularity.

Let \(\chi,\psi\) be primitive Dirichlet characters of conductors \(L,R\).
Assume \(k\ge2\) and \(\chi(-1)\psi(-1)=(-1)^k\).
Define generalized Bernoulli numbers by
\[
 \sum_{a=1}^{R}\frac{\psi(a)t e^{at}}{e^{Rt}-1}
 =\sum_{j\ge0}B_{j,\psi}\frac{t^j}{j!}.
\]
Except for \(k=2,\chi=\psi=1\), the series
\[
 E_k^{\chi,\psi}(z)
 =c_0+\sum_{n\ge1}
 \left(\sum_{d\mid n}\psi(d)\chi(n/d)d^{k-1}\right)q^n,
 \qquad
 c_0=\begin{cases}
 0,&L>1,\\
 -B_{k,\psi}/(2k),&L=1
 \end{cases}
 \tag{7.1}
\]
belongs to \(M_k(LR,\chi\psi)\) and is an eigenform for every \(T_n\) **at this level**. We prove these assertions next. The coefficient convention agrees with Stein's freely available author text, Section 5.3; its statement is a comparison, not a proof input. The product \(\chi\psi\) is the nebentypus for our lower-right convention. The characters in the coefficient sum are extended by zero according to their own conductors; the conductor-one character has value one on every integer, including zero.

**Theorem 7.2 (construction and all cusp conditions).** The assertions following (7.1) hold with exactly the stated weight-two exception.

**Proof.** Put \(e(x)=e^{2\pi ix}\),
\(C_k=(-2\pi i)^k/(k-1)!\), and
\(\tau(\bar\psi)=\sum_{a\bmod R}\bar\psi(a)e(a/R)\).
For the conductor-one character take \(\tau=1\). We first verify the finite Fourier identity
\[
\sum_{a\bmod R}\bar\psi(a)e(ha/R)
=\psi(h)\tau(\bar\psi).
\tag{7.5}
\]
For \((h,R)=1\), substitute \(a=h^{-1}b\). If \(p\mid(h,R)\), primitivity supplies a unit \(u\equiv1\pmod{R/p}\) with \(\psi(u)\ne1\): otherwise the character would descend to the smaller modulus \(R/p\). The reduction map on units is onto, as follows by choosing lifts not divisible by the missing prime and applying the Chinese remainder theorem. Multiplication by this \(u\) leaves \(e(ha/R)\) unchanged and multiplies the character sum by a scalar different from one, so it is zero. This proves (7.5) also at nonunits. Orthogonality of the finite exponentials, obtained by summing a geometric progression, gives
\(\sum_{h\bmod R}|\sum_a\bar\psi(a)e(ha/R)|^2
=R\sum_a|\bar\psi(a)|^2=R\varphi(R)\).
Thus \(|\tau(\bar\psi)|^2=R\), so the normalizing factor below is nonzero. Conjugating the sum and replacing \(a\) by \(-a\) also gives
\(\tau(\psi)\tau(\bar\psi)=\psi(-1)R\).

Consider
\[
G(z)=\sum_{(m,n)\ne(0,0)}
\frac{\chi(m)\bar\psi(n)}{(mRz+n)^k}.
\tag{7.6}
\]
For \(k>2\) the lattice estimate in the fourth lesson, Lemma 3.1, proves absolute locally uniform convergence. For \(k=2\), at least one character is nontrivial, since the excluded pair is the only primitive pair with both characters trivial. Partition \(\mathbb Z^2\) into rectangles of side lengths \(L,R\), omitting the singular pair in its one rectangle. On every other rectangle the sum of the weights is zero: it is the product of the two complete character sums, one of which vanishes by multiplication by a unit where the character is nontrivial. On a rectangle at distance \(r\) from the origin subtract the kernel at one corner. The first derivatives of \((mRz+n)^{-2}\) are \(O(r^{-3})\), uniformly for \(z\) in a compact subset of \(\mathfrak H\), because the underlying real-linear map is invertible. Thus the rectangle contribution is \(O(r^{-3})\). There are \(O(r)\) rectangles in a shell of unit thickness, so these rectangle contributions are absolutely summable.

This definition is unchanged by the linear reindexings we use. To check this precisely, exhaust the lattice by expanding squares or by their images under a fixed invertible linear map. Both contain a disk of radius proportional to \(T\), have diameter \(O(T)\), and have boundary meeting \(O(T)\) rectangles. Complete rectangles outside that disk contribute \(O(T^{-1})\), by the preceding derivative estimate; incomplete boundary rectangles have \(O(T)\) terms, each \(O(T^{-2})\), and likewise contribute \(O(T^{-1})\). Hence all these exhaustions have the same limit. Locally uniform convergence of the rectangle series proves holomorphy, without asserting absolute convergence of the individual weight-two terms.

If \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma_0(LR)\), reindex by
\[
m'=ma+nc/R,\qquad n'=mRb+nd.
\]
This is an integral bijection, and
\(\chi(m')\bar\psi(n')
=\chi(a)\bar\psi(d)\chi(m)\bar\psi(n)
=(\chi\psi)(d)^{-1}\chi(m)\bar\psi(n)\).
The last equality uses \(ad\equiv1\pmod{LR}\). Therefore
\(G(\gamma z)=(cz+d)^k(\chi\psi)(d)G(z)\), with the required lower-right character.

We justify regularity at every cusp, including in weight two. After slashing by any \(\alpha\in\mathrm{SL}_2(\mathbb Z)\), the sum has the form
\(\sum' W(u,v)(uz+v)^{-k}\), where \(W\) is bounded and periodic modulo a common positive integer \(Q\), and satisfies \(W(-u,-v)=(-1)^kW(u,v)\). Extend it by zero outside the transformed index-\(R\) sublattice. One may take \(Q=LR\): applying \(\alpha^{-1}\) to a shift by \(Q\) changes the original \(m,n\) by multiples of \(L,R\). In weight two its complete \(Q\)-square sum is zero, because the corresponding original sums run through whole periods of both characters. The same rectangle argument consequently applies after this change of coordinates.

For \(u>0\), sum a row by its \(Q\) residue classes. The row formula proved in the fourth lesson, (3.4), gives
\[
\begin{gathered}
\sum_v\frac{W(u,v)}{(uz+v)^k}\\
=Q^{-k}C_k\\
\cdot\sum_{h\ge1}\left[\begin{gathered}
h^{k-1}e(huz/Q)\\
\cdot\sum_{a\bmod Q}W(u,a)e(ha/Q)
\end{gathered}\right].
\end{gathered}
\tag{7.7}
\]
For \(y\ge1\), the double sum over \(u,h\ge1\) is bounded by a constant times
\(\sum_{u,h\ge1}h^{k-1}e^{-2\pi huy/Q}\), which converges and tends to zero as \(y\to\infty\). Negative rows equal the positive rows by parity, and the zero row is an absolutely convergent constant. In weight two this row ordering agrees with the rectangle definition. The difference between a square sum and the sum of its complete rows lies in \(|u|\le T,\ |v|>T\). Tile this strip by complete \(Q\)-squares and its two boundary strips of width at most \(Q\) at \(u=\pm T\). All complete squares lie outside a disk of radius \(T\); their zero-mean derivative estimate has total \(O(T^{-1})\). Each boundary strip has only a bounded number of \(u\)-coordinates, so its individual-term bound is \(O(\sum_{|v|>T}v^{-2})=O(T^{-1})\). The complete rows with \(|u|>T\) tend to zero exponentially by (7.7). This proves equality of the two limits. Thus every slash translate is bounded at infinity. Its periodic holomorphic cusp coordinate has a removable puncture by the earlier Petersson lesson, Lemma 0.1, proving every cusp condition.

At infinity, apply (7.7) with the original row variable \(m\), then (7.5). Rows of opposite sign agree by the parity hypothesis, yielding
\[
\begin{gathered}
G(z)=2\mathbf1_{L=1}L(k,\bar\psi)\\
+2C_kR^{-k}\tau(\bar\psi)\\
\cdot\sum_{m,h\ge1}\chi(m)\psi(h)h^{k-1}q^{mh}.
\end{gathered}
\tag{7.8}
\]
The exponential majorant just used permits regrouping by \(mh\).

We also compute the constant, rather than importing a special value. Define Bernoulli polynomials by
\(te^{xt}/(e^t-1)=\sum_jB_j(x)t^j/j!\).
Differentiating and comparing the values at zero and one gives
\(B_j'=jB_{j-1}\), \(\int_0^1B_j(x)dx=0\) for \(j\ge1\), and \(B_j(1)=B_j(0)\) for \(j\ne1\), with \(B_1(1)-B_1(0)=1\). Repeated integration by parts therefore gives, for \(h\ne0\), the Fourier coefficient
\(-j!/(2\pi ih)^j\) of the continuous periodic polynomial \(B_j\), \(j\ge2\). These coefficients are summable; the elementary kernel uniqueness proof in the fourth lesson, Lemma 5.1, proves
\[
B_j(x)=-\frac{j!}{(2\pi i)^j}\sum_{h\ne0}\frac{e(hx)}{h^j}.
\]
The defining generating functions give
\(B_{k,\psi}=R^{k-1}\sum_{a\bmod R}\psi(a)B_k(a/R)\).
When \(L=1\), \(\psi(-1)=(-1)^k\); the last Fourier expansion and the version of (7.5) for \(\psi\) consequently give
\[
B_{k,\psi}=-\frac{2k!R^{k-1}\tau(\psi)}{(2\pi i)^k}
L(k,\bar\psi).
\]
Together with \(\tau(\psi)\tau(\bar\psi)=\psi(-1)R\), this shows that the constant of
\(G/(2C_kR^{-k}\tau(\bar\psi))\) is exactly \(-B_{k,\psi}/(2k)\). If \(L>1\), the zero row has weight \(\chi(0)=0\), giving zero constant. We have proved that the normalized lattice sum is (7.1) and belongs to the asserted modular-form space.

It remains to prove its eigenform assertion. Its positive coefficient \(b_n\) is multiplicative, by splitting each divisor at coprime factors. For a prime \(p\), set \(A=\chi(p)\), \(B=\psi(p)p^{k-1}\). Then
\(b_{p^r}=\sum_{j=0}^r A^{r-j}B^j\), and the finite geometric sum gives
\(b_{p^{r+1}}=(A+B)b_{p^r}-ABb_{p^{r-1}}\).
At good primes \(AB=(\chi\psi)(p)p^{k-1}\), so the proved coefficient formula gives \(T_pE=(A+B)E\) on all positive coefficients. At bad primes at least one of \(A,B\) is zero, so the same calculation gives \(U_pE=(A+B)E\). For the constant coefficient there is nothing to check when \(L>1\). When \(L=1\), a good operator multiplies the constant by \(1+\psi(p)p^{k-1}=A+B\); a bad prime divides \(R\), so \(A+B=1\), and \(U_p\) preserves the constant. Equality of all Fourier coefficients proves the eigenform identities. Coprime products and the prime-power recurrences then prove the assertion for every \(T_n\). \(\square\)

The first coefficient is \(1\). Thus the eigenvalue at a prime is
\[
 \chi(p)+\psi(p)p^{k-1}.
 \tag{7.2}
\]
At a good prime its two terms have product
\(\chi(p)\psi(p)p^{k-1}\), exactly the recurrence coefficient in (3.1).
At a bad prime at least one character value is zero, and (7.2) gives the corresponding \(U_p\)-eigenvalue. Substitution \(z\mapsto tz\) gives a modular form at level \(LRt\), with character induced from \(\chi\psi\), but does not generally preserve eigenform status at primes dividing \(t\).

For the exceptional pair, put
\[
 \mathcal E_2(z)=-\frac1{24}+\sum_{n\ge1}\sigma_1(n)q^n
 =-\frac1{24}E_2(z),
\]
where \(E_2\) on the right is the constant-one series from the Eisenstein lesson.
For every integer \(t>1\),
\[
 \mathcal E_2(z)-t\mathcal E_2(tz)\in M_2(\Gamma_0(t)).
 \tag{7.3}
\]
Its good-prime eigenvalues are \(1+p\); for \(t=p\) prime it is also a \(U_p\)-eigenform with eigenvalue \(1\). Here is the modularity and cusp proof of (7.3). The fourth lesson, Theorem 5.2, proves that \(E_2^*(z)=E_2(z)-3/(\pi\operatorname{Im}z)\) has weight two for the full group. The corrections cancel in \(E_2^*(z)-tE_2^*(tz)=E_2(z)-tE_2(tz)\). For \(B_t=\operatorname{diag}(t,1)\) and \(\gamma\in\Gamma_0(t)\), \(B_t\gamma B_t^{-1}\) is integral, so the slash cocycle proves the transformation law of the difference. To check a cusp, factor \(B_t\alpha=\rho\beta\), where \(\rho\in\mathrm{SL}_2(\mathbb Z)\) sends infinity to the rational cusp \(B_t\alpha\infty\), and \(\beta\) is upper triangular with rational entries and positive diagonal ratio. The slash of \(tE_2^*(tz)=E_2^*\Vert_2B_t\) is a constant multiple of \(E_2^*(\beta z)\), which is bounded as \(y\to\infty\). The first term is bounded too. The difference is holomorphic and periodic in its cusp coordinate, so boundedness gives a removable puncture. Multiplying by \(-1/24\) proves (7.3). Good-prime eigenvalues follow by the coefficient selection formula and the divisor identity of the level-one Hecke lesson.

For composite \(t\), do not infer that (7.3) is an eigenform for all bad operators.
For example, at \(t=4\) its first, second and fourth coefficients are \(1,3,3\).
If it were a \(U_2\)-eigenform, the first coefficient would force eigenvalue \(3\), while the second would require its fourth coefficient to be \(9\). This contradiction precisely separates good-prime eigenform status from full eigenform status.

**Proposition 7.1 (the exact exceptional eigenform criterion).** For an integer \(t>1\), the form \(f_t=\mathcal E_2-tV_t\mathcal E_2\) is an eigenform for all Hecke operators at level \(t\) if and only if \(t\) is prime.

**Proof.** Its constant term is \((t-1)/24\), which is nonzero. If \(t\) is composite, choose a prime \(p\mid t\); then \(p<t\). Its coefficients at \(1,p\) are \(1,p+1\), because the substituted series has no positive terms below \(t\). A \(U_p\)-eigenvalue would be \(1\) by the constant term, since \(U_p\) preserves that term. The coefficient of \(q\) would instead force eigenvalue \(p+1\). This contradiction handles every composite \(t\).

For \(t=p\) prime, write \(f_p=\sum_{n\ge0}c_nq^n\). For \(n\ge1\),
\[
 c_n=\sigma_1(n)-p\mathbf1_{p\mid n}\sigma_1(n/p),\qquad
 \sigma_1(pn)=(p+1)\sigma_1(n)-p\mathbf1_{p\mid n}\sigma_1(n/p).
 \tag{7.4}
\]
To check the divisor identity, write \(n=p^rm\), \(p\nmid m\), and put \(S_r=1+p+\cdots+p^r\), \(S_{-1}=0\). The geometric sums satisfy \(S_{r+1}=(p+1)S_r-pS_{r-1}\); multiply by \(\sigma_1(m)\). It follows that \(c_{pn}=c_n\). The constant term is preserved as well, so \(U_pf_p=f_p\). The already proved good-prime formulas give \(T_\ell f_p=(1+\ell)f_p\) for every \(\ell\ne p\). The prime-power recurrences and coprime products in (3.1) then make \(f_p\) an eigenform for every \(T_n\). \(\square\)

## 8. Exercises

1. **Easy.** Compute the coefficients through \(q^{12}\) of
   \(\eta(z)^2\eta(11z)^2\), and verify the relations at \(6,4,9,8,12\).
2. **Medium.** Starting with the prime double coset, derive both formulas (2.5) and their coefficient versions. Include the constant term.
3. **Medium.** Prove directly that every diamond is unitary for the Petersson product, including when \(-I\notin\Gamma_1(N)\).
4. **Medium.** Find the eigenvectors of \(U_p\) on the old space in Theorem 5.1, and prove the exact discriminant criterion for diagonalizability.
5. **Hard.** Prove \(T_p^*=[p]^{-1}T_p\) for \(p\nmid N\) by unfolding the double coset. Identify both intersection groups and explain the appearance of the inverse diamond.

## 9. Full solutions

### Solution 1

Only product factors with exponent at most \(11\) affect the coefficient through \(q^{12}\), because of the initial \(q\).
Let \(P_j=\prod_{n=1}^j(1-q^n)^2\), computed modulo \(q^{12}\).
For its coefficients \(p_r^{(j)}\), start with \(p_0^{(0)}=1\) and all other coefficients zero, and multiply each factor by
\[
 p_r^{(j)}
 =p_r^{(j-1)}-2p_{r-j}^{(j-1)}+p_{r-2j}^{(j-1)};
\]
negative indices mean zero. For example
\[
 P_2=1-2q-q^2+4q^3-q^4-2q^5+q^6,
\]
and multiplication by \(1-2q^3+q^6\) gives
\[
 P_3=1-2q-q^2+2q^3+3q^4+0q^5-6q^6
       +0q^7+3q^8+2q^9-q^{10}-2q^{11}+O(q^{12}).
\]
Continuing the displayed recurrence through \(j=11\) gives the following complete row:
\[
\begin{array}{c|rrrrrrrrrrrr}
 r&0&1&2&3&4&5&6&7&8&9&10&11\\ \hline
 p_r^{(11)}&1&-2&-1&2&1&2&-2&0&-2&-2&1&0.
\end{array}
\]
The second product in (6.1) is \(1-2q^{11}+O(q^{12})\).
Consequently \(f=qP_{11}(1-2q^{11})+O(q^{13})\): the coefficient of \(q^{12}\) is \(0-2=-2\), and the earlier ones are read directly from the row. This proves (6.5).

The five requested numerical relations are
\[
 \begin{aligned}
 a_6&=(-2)(-1)=2,\\
 a_4&=(-2)^2-2=2,\\
 a_9&=(-1)^2-3=-2,\\
 a_8&=(-2)(2)-2(-2)=0,\\
 a_{12}&=(-1)(2)=-2.
 \end{aligned}
\]
They agree with the product coefficients. Theorem 3.1 and the proved one-dimensionality explain why they hold as Hecke relations, rather than merely as coincidences.

### Solution 2

The left representatives are \(\delta_b\), and additionally
\(\sigma_p\operatorname{diag}(p,1)\) when \(p\nmid N\).
For the first type,
\[
 p^{k/2-1}f\Vert_k\delta_b
 =p^{k/2-1}p^{k/2}p^{-k}f((z+b)/p)
 =p^{-1}f((z+b)/p).
\]
For the second, slash composition and the character law give
\[
 p^{k/2-1}f\Vert_k\sigma_p\operatorname{diag}(p,1)
 =\chi(p)p^{k-1}f(pz).
\]
This proves (2.5), with the second contribution absent at a bad prime.
Averaging \(q^{m/p}e^{2\pi imb/p}\) kills exactly the indices not divisible by \(p\). The surviving terms are \(a_{pm}q^m\).
The substituted series \(f(pz)\) contributes \(a_{m/p}\) if \(p\mid m\), and zero otherwise. At \(m=0\) the first sum contributes \(a_0\), and the good second term contributes \(\chi(p)p^{k-1}a_0\). Thus the constant coefficients are \((1+\chi(p)p^{k-1})a_0\) and \(a_0\), respectively.

### Solution 3

Choose a lift \(\sigma_u\in\Gamma_0(N)\).
Its normalizing action takes a fundamental domain \(F\) for \(\bar\Gamma\) to another such domain. The transformation laws give
\[
 ([u]f)(z)\overline{([u]g)(z)}y^k\,d\mu(z)
 =f(\sigma_uz)\overline{g(\sigma_uz)}
   \operatorname{Im}(\sigma_uz)^k\,d\mu(\sigma_uz).
\]
Integrate and change variables. The integrand is \(\Gamma\)-invariant, and cusp decay ensures absolute convergence, so integration over \(\sigma_uF\) equals that over \(F\).
Both sides have the same projective-index factor from (0.2). Hence
\(\langle[u]f,[u]g\rangle=\langle f,g\rangle\).
This argument uses the projective quotient throughout; it does not assume that \(-I\) is in \(\Gamma\).
Since \([u]^{-1}=[u^{-1}]\), unitarity also proves the first adjoint formula in (4.2).

### Solution 4

Write a vector as \(xg+yV_pg\).
Equation (5.1) makes the eigenvector equations
\[
 a_px+y=\lambda x,\qquad -p^{k-1}x=\lambda y.
\]
A nonzero eigenvector must have \(x\ne0\), because the first equation would otherwise force \(y=0\).
Taking \(x=1\) gives \(y=\lambda-a_p\), and the second equation is
\(\lambda^2-a_p\lambda+p^{k-1}=0\).
If the roots are \(\alpha,\beta\), the eigenvectors are therefore
\(g-\beta V_pg\) and \(g-\alpha V_pg\).
For distinct roots their coordinate determinant is \(\beta-\alpha\ne0\), so they form an eigenbasis.
If the discriminant is zero, the two roots agree and the equations describe just one eigenline. Since the space has dimension two, diagonalizability fails.
This proves both directions of the criterion, using the independently proved linear independence of \(g,V_pg\).

### Solution 5

Put \(\alpha=\operatorname{diag}(1,p)\). The two groups in the unfolding are
\[
 H=\{\gamma\in\Gamma:p\mid b_\gamma\},\qquad
 H'=\{\gamma\in\Gamma:p\mid c_\gamma\}.
\]
For \(p\nmid N\), the latter is \(\Gamma_1(N)\cap\Gamma_0(p)\);
one also has \(H'=\alpha H\alpha^{-1}\).
The \(p+1\) representatives of \(H\backslash\Gamma\) are \(T^b\) and \(\gamma_\infty\) from Lemma 2.1.
Their translates of a \(\Gamma\)-domain tile an \(H\)-domain.
Hence
\[
 \langle T_pf,g\rangle_\Gamma
 =\frac{p^{k/2-1}}{[\overline{SL_2(\mathbb Z)}:\bar\Gamma]}
 \int_{H\backslash\mathfrak H}(f\Vert_k\alpha)\bar g\,y^k\,d\mu.
\]
Changing \(w=\alpha z\) by (4.1) changes the group to \(H'\) and the integrand to \(f\,\overline{g\Vert_k\alpha^{-1}}\).
Retiling this domain by \(H'\backslash\Gamma\) gives the adjoint double-coset sum. Absolute convergence follows from the global cusp bound, and relative group and projective indices agree because both intersection groups have the same \(-I\) status as \(\Gamma\).

The positive scalar factor replaces \(\alpha^{-1}\) by
\(\alpha^*=\operatorname{diag}(p,1)\) without changing a slash action.
The identity
\(\sigma_p\alpha^*=\alpha\gamma_\infty\)
now gives
\(\Gamma\alpha^*\Gamma=\Gamma\sigma_p^{-1}\alpha\Gamma\).
Its sum is \(T_p[p]^{-1}\), which equals \([p]^{-1}T_p\) by Lemma 2.2.
This proves
\(\langle T_pf,g\rangle_\Gamma=\langle f,[p]^{-1}T_pg\rangle_\Gamma\).
The inverse diamond arises from undoing \(\sigma_p\) when passing from the adjugate double coset back to the original one.

## What this lesson does not prove

The character Eisenstein modularity, all cusp conditions, Bernoulli constant and unscaled eigenform assertions (7.1)–(7.2) are proved in Theorem 7.2, including convergence of the periodic zero-mean weight-two sum. Equation (7.3) has its own transformation and cusp proof using the earlier completed \(E_2^*\). The exact exceptional eigenform criterion is Proposition 7.1. We do not use an assertion that every composite-scaled weight-two combination is an eigenform.

We use these exact owned prerequisites:

- Congruence subgroups, cusps and elliptic points, Lemma 1.1, Proposition 1.2, Proposition 2.1 and Theorem 2.2: integral reduction, the quotient, cusp widths and the prime-level cusps.
- Modular forms, lattice functions and Eisenstein series, Proposition 1.2 on the Fourier and irregular-cusp conventions, and Theorem 5.2 on \(E_2\).
- The valence formula and the ring of modular forms of level one, Theorem 4.1, \(\eta^{24}=\Delta\), and its product definition.
- Dimension formulas for congruence subgroups, Theorem 3.1, the locally proved valence formula. The level-eleven dimension is deduced from it in Section 6 here, without the unresolved general dimension theorem. Finite dimensionality of the other spaces follows from its Theorem 6.1 coefficient bound, as in the Petersson lesson.
- The Petersson inner product and Poincaré series, Theorems 1.1 and 2.1, the absolute Petersson product and global cusp bound.
- Hecke operators of level one, Theorem 2.1's polynomial product identity and the computed \(\Delta\) eigenvalue.

The fundamental theorem of algebra used in Theorem 4.2 and the removable-singularity step in Section 7 are proved in the earlier Petersson lesson, Lemma 0.1. Holomorphy of locally uniform sums uses the first lesson, Lemma 0.2. Elementary finite-unit arithmetic remains a number-theory foundational prerequisite without an exact earlier programme proof verified here. No newform multiplicity-one theorem, general old/new decomposition, optimal coefficient bound, Galois representation or analytic continuation is asserted here. Those require the later lessons.

## References

- **Stein, free author text.** W. Stein, *Modular Forms: A Computational Approach*, §§3.1, 4.1, 4.4, 5.3 and 9.1. [Freely accessible author-hosted PDF](https://wstein.org/books/modform/stein-modform.pdf), [author's free-distribution statement](https://wstein.org/books/modform/README.html), [character Eisenstein section](https://wstein.org/books/modform/modform/eisenstein.html). The character lattice construction and eigenform proof are supplied locally in Theorem 7.2; the exceptional composite-level assertion is corrected by Proposition 7.1.
- **Wiese 2018.** G. Wiese, *Computational Arithmetic of Modular Forms*, §§1.1 and 7.1–7.2, for the congruence-level Hecke operators and their coefficient formulas. [Original notes](https://arxiv.org/abs/1809.04645).
- **Best et al. 2021.** A. J. Best and coauthors, *Computing classical modular forms*, §§4.4–4.6, for the place of character Eisenstein series, old spaces and Hecke eigenvalues in subsequent computations. [Original paper, version four](https://arxiv.org/abs/2002.04717v4).
- **Lebl.** J. Lebl, *A Guide to Cultivating Complex Analysis*, Theorem 3.3.11. [Author's text](https://www.jirka.org/ca/ca.pdf).

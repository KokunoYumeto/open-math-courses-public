# Hecke operators of level one

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A modular form has infinitely many Fourier coefficients, but it belongs to a finite-dimensional space. Hecke operators turn relations among those coefficients into relations among commuting linear maps. Their self-adjointness then produces distinguished forms whose coefficients determine an Euler product.

We use the lattice-function dictionary of Modular forms, lattice functions and Eisenstein series, Section 2; the dimension and integral-basis results of The valence formula and the ring of modular forms of level one, Theorem 2.2 and Solution 5; and the Petersson product and coefficient bound of The Petersson inner product and Poincaré series, Theorems 1.1 and 2.1. The lattice-counting identities are proved in Section 2. We do not need the adelic description of the Hecke algebra.

Throughout, \(\Gamma=\mathrm{SL}_2(\mathbb Z)\), \(q=e^{2\pi iz}\), and \(k\ge4\) is even, unless another weight is explicitly mentioned. We write
\[
 f(z)=\sum_{r\ge0}a_r(f)q^r.
\]
The Petersson product is linear in its first argument:
\[
 \langle f,g\rangle=\int_{\Gamma\backslash\mathfrak H}
       f(z)\overline{g(z)}y^k\,\frac{dx\,dy}{y^2}.
\]
At level one the raw and projective-index-normalized products coincide. Multiplying this product by \(3/\pi\) gives the volume-normalized convention; self-adjointness is unaffected.

## 1. Lattices, matrices and Fourier coefficients

For a lattice function \(F\) of weight \(k\), set
\[
 F(\lambda\Lambda)=\lambda^{-k}F(\Lambda),\qquad
 (\mathcal T_nF)(\Lambda)=
     \sum_{\substack{\Lambda'\subseteq\Lambda\\\lvert\Lambda/\Lambda'\rvert=n}}F(\Lambda'),
 \qquad (R(d)F)(\Lambda)=F(d\Lambda).
 \tag{1.1}
\]
The sum is over actual sublattices, each once, and \(R(d)\) acts as \(d^{-k}\).

Use the ordered basis \((z,1)\) of \(\Lambda_z=\mathbb Zz+\mathbb Z\).
A finite-index sublattice has a unique basis
\[
 (az+b,d),\qquad a,d>0,\quad ad=n,\quad 0\le b<d.
 \tag{1.2}
\]
Indeed, its projection to the coefficient of \(z\) is \(a\mathbb Z\), and its intersection with \(\mathbb Z\) is \(d\mathbb Z\). Choose an element \(az+b\), reduce \(b\) modulo \(d\), and subtract multiples of this element from any other element. These two elements then generate the sublattice. Their coordinate determinant is \(ad\), which is its index; the projection, intersection and reduced \(b\) prove uniqueness.

Thus \(\Lambda'=d\Lambda_{(az+b)/d}\). If \(f(z)=F(\Lambda_z)\), the normalized operator on forms is
\[
 \boxed{\displaystyle
 T_nf(z)=n^{k-1}\sum_{\substack{ad=n\\a,d>0}}d^{-k}
                   \sum_{b=0}^{d-1} f\!\left(\frac{az+b}{d}\right).}
 \tag{1.3}
\]
In this dictionary \(T_n=n^{k-1}\mathcal T_n\).

We also need a matrix interpretation. Put
\[
 D_n=\{\alpha\in M_2(\mathbb Z):\det\alpha=n\},\qquad
 (f\Vert_k\alpha)(z)=\det(\alpha)^{k/2}(cz+d)^{-k}f(\alpha z).
 \tag{1.4}
\]
The symbol \(\Vert_k\) extends the earlier determinant-one slash operator.
The identity \(j(\alpha\beta,z)=j(\alpha,\beta z)j(\beta,z)\), together with multiplicativity of determinants, gives
\[
 (f\Vert_k\alpha)\Vert_k\beta=f\Vert_k(\alpha\beta).
\]
A nonzero scalar matrix acts trivially, since \(k\) is even.

**Lemma 1.1.** Representatives of \(\Gamma\backslash D_n\) are precisely
\[
 H_n=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:
                   a,d>0,\ ad=n,\ 0\le b<d\right\}.
\]
Consequently
\[
 T_nf=n^{k/2-1}\sum_{\alpha\in\Gamma\backslash D_n}f\Vert_k\alpha
 \tag{1.5}
\]
is independent of representatives and preserves \(M_k\) and \(S_k\).

**Proof.**
Left multiplication by \(\Gamma\) changes an oriented integral row basis of the same sublattice of \(\mathbb Z^2\). The construction (1.2), with coordinates in \(\mathbb Z^2\), supplies its unique representative in \(H_n\). The orientation is preserved because all determinants are positive. Since \(f\Vert_k\gamma=f\), the sum is independent of the row basis.

Right multiplication by \(\gamma\in\Gamma\) permutes the left cosets of \(D_n\). The composition law therefore gives \((T_nf)\Vert_k\gamma=T_nf\). Formula (1.3) is a finite sum of holomorphic functions. Each summand remains bounded as \(y\to\infty\), and tends to zero there if \(f\) is cuspidal, since its argument has imaginary part \(ay/d\). The resulting periodic holomorphic function has a removable singularity in its \(q\)-coordinate at zero; its constant term vanishes in the cuspidal case. There is one cusp for \(\Gamma\), so these are exactly the required cusp conditions. ∎

**Theorem 1.2 (coefficient formula).** For \(m\ge0\),
\[
 \boxed{\displaystyle a_m(T_nf)=
          \sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}(f).}
 \tag{1.6}
\]
Here \(\gcd(0,n)=n\). In particular,
\[
 a_0(T_nf)=\sigma_{k-1}(n)a_0(f),\qquad a_1(T_nf)=a_n(f).
 \tag{1.7}
\]

**Proof.**
Expand each term of (1.3). The finite geometric sum
\[
 \sum_{b=0}^{d-1}e^{2\pi irb/d}
   =\begin{cases}d,&d\mid r,\\0,&d\nmid r\end{cases}
\]
eliminates all \(r\) except \(r=d\ell\). The result is
\[
 T_nf=\sum_{ad=n}\sum_{\ell\ge0}
              n^{k-1}d^{1-k}a_{d\ell}(f)q^{a\ell}.
\]
To obtain \(q^m\), require \(a\mid m\) and put \(\ell=m/a\).
Then \(d=n/a\), \(d\ell=mn/a^2\), and
\(n^{k-1}d^{1-k}=a^{k-1}\). Relabel the divisor \(a\) as \(d\).
The Fourier expansions converge absolutely on every horizontal line of positive height, which justifies these finite regroupings. ∎

For a prime \(p\), this becomes the particularly useful formula
\[
 T_pf(z)=p^{k-1}f(pz)+\frac1p\sum_{b=0}^{p-1}f((z+b)/p),
 \qquad
 a_m(T_pf)=a_{pm}(f)+p^{k-1}a_{m/p}(f),
 \tag{1.8}
\]
where \(a_{m/p}=0\) if \(m/p\) is not a nonnegative integer.

## 2. Translating the lattice relations

We first prove the lattice-counting identities:
\[
 \mathcal T_m\mathcal T_n=\mathcal T_{mn}\quad(\gcd(m,n)=1),
 \qquad
 \mathcal T_p\mathcal T_{p^r}
  =\mathcal T_{p^{r+1}}+pR(p)\mathcal T_{p^{r-1}}\quad(r\ge1).
 \tag{2.1}
\]
**Proof of (2.1).** A term of \(\mathcal T_m\mathcal T_nF\) is a chain
\(\Lambda''\subset\Lambda'\subset\Lambda\) with successive indices \(n,m\). If \((m,n)=1\), the finite abelian group \(A=\Lambda/\Lambda''\), of order \(mn\), is the direct sum of its prime-primary groups. Its subgroup of order \(n\) is unique: on the primary factors belonging to \(n\) it must be the whole group, and on the other factors it must be zero. This subgroup is \(\Lambda'/\Lambda''\). Thus every index-\(mn\) final lattice occurs once, proving the coprime rule.

For the second rule, fix a final lattice of index \(p^{r+1}\). Its intermediate index-\(p\) lattices correspond to kernels of nonzero maps \(A\to\mathbb F_p\), up to nonzero scalar multiplication. The quotient \(A/pA\) has dimension one or two, since \(\Lambda\) has rank two; it cannot have dimension zero, because a nonzero finite \(p\)-group is not equal to its subgroup of \(p\)-multiples. Its dimension is two exactly when \(\Lambda''\subset p\Lambda\): indeed \(A/pA=\Lambda/(p\Lambda+\Lambda'')\). There are respectively one and \(p+1\) kernels, by counting the nonzero vectors in a one- or two-dimensional dual space. Consequently every final lattice contributes once, with an additional multiplicity \(p\) precisely for those contained in \(p\Lambda\). Such a lattice has index \(p^{r-1}\) in \(p\Lambda\), so these additional terms are exactly \(pR(p)\mathcal T_{p^{r-1}}F\). This proves the prime-power rule, including \(r=1\). \(\square\)

Homothety commutes with the sublattice sums, since scaling gives a bijection of the sublattices being counted. The full divisor-sum relation is
\[
 \mathcal T_m\mathcal T_n
   =\sum_{d\mid\gcd(m,n)}dR(d)\mathcal T_{mn/d^2}.
 \tag{2.2}
\]
The algebraic argument below derives its form-valued version from (2.1). The spherical Hecke algebra and its restricted tensor product interpretation belong to the separate lattice and adelic theory.

**Theorem 2.1 (Hecke relations on forms).**
\[
 T_1=1,\qquad
 \boxed{\displaystyle T_mT_n=
       \sum_{d\mid\gcd(m,n)}d^{k-1}T_{mn/d^2}.}
 \tag{2.3}
\]
In particular, the operators commute, \(T_mT_n=T_{mn}\) for coprime \(m,n\), and
\[
 T_pT_{p^r}=T_{p^{r+1}}+p^{k-1}T_{p^{r-1}}\quad(r\ge1).
 \tag{2.4}
\]

**Proof.**
The coprime rule in (2.1) is unchanged by the normalization \(T_n=n^{k-1}\mathcal T_n\).
For the prime-power rule, the second term acquires the factor
\[
 \frac{(p^{r+1})^{k-1}\,p\,p^{-k}}
      {(p^{r-1})^{k-1}}=p^{k-1}.
\]
This proves (2.4). It also makes every \(T_{p^r}\) a polynomial in \(T_p\), while the coprime rule expresses \(T_n\) as the product of its prime-power operators. The coprime rule with \(m,n\) interchanged shows that operators belonging to distinct primes commute; hence all \(T_n\) commute.

For completeness, the full divisor sum follows algebraically. Fix \(p\), put \(P_r=T_{p^r}\), \(P_0=1\), and \(Q=p^{k-1}\). We claim, for \(0\le u\le v\),
\[
 P_uP_v=\sum_{j=0}^u Q^jP_{u+v-2j}.                 \tag{2.5}
\]
For \(u=0\) it is immediate, and for \(u=1\) it is (2.4).
For \(u\ge2\), use \(P_u=P_1P_{u-1}-QP_{u-2}\) and the induction hypotheses.
In \(P_1P_{u-1}P_v\), each index \(u+v-1-2j\), \(0\le j<u\), is at least one, so (2.4) applies. Subtracting \(QP_{u-2}P_v\) cancels all the second terms except \(Q^uP_{v-u}\); the remaining first terms are \(Q^jP_{u+v-2j}\) for \(0\le j<u\). This proves (2.5).

Multiply (2.5) over primes. A choice of \(j\) at each prime is exactly a divisor \(d\) of \(\gcd(m,n)\); its factor is \(d^{k-1}\) and its remaining operator is \(T_{mn/d^2}\). This gives (2.3).

Directly translating (2.2) gives the same factor:
\[
 (mn)^{k-1}d\,d^{-k}\mathcal T_{mn/d^2}
   =d^{k-1}T_{mn/d^2}.
\]
In particular, retaining \(d\) but forgetting \(R(d)\) would give the wrong normalization. ∎

## 3. Why the operators are self-adjoint

For \(\alpha\in D_n\), write \(\alpha^*=n\alpha^{-1}\).
Its entries are integral, \(\det\alpha^*=n\), and \((\alpha^*)^*=\alpha\).
Thus the adjugate map permutes the double cosets of \(D_n\):
\[
 (\Gamma\alpha\Gamma)^*=\Gamma\alpha^*\Gamma.
 \tag{3.1}
\]
For composite \(n\), \(D_n\) need not be a single double coset.

**Theorem 3.1.** On \(S_k\),
\[
 \langle T_nf,g\rangle=\langle f,T_ng\rangle.
 \tag{3.2}
\]

**Proof.**
First record the change of variables behind the adjoint. For any real matrix \(\alpha\) of positive determinant,
\[
 \operatorname{Im}(\alpha z)
   =\frac{\det\alpha\,y}{|cz+d|^2},\qquad
 d\mu(\alpha z)=d\mu(z),\quad d\mu=\frac{dx\,dy}{y^2}.
 \tag{3.3}
\]
The second equality follows from the complex derivative
\((\alpha z)'=\det\alpha/(cz+d)^2\), whose real Jacobian is its squared modulus.
Consequently
\[
 (f\Vert_k\alpha)(z)\overline{(g\Vert_k\alpha)(z)}
                y^k\,d\mu(z)
 =f(\alpha z)\overline{g(\alpha z)}
            \operatorname{Im}(\alpha z)^k\,d\mu(\alpha z).
 \tag{3.4}
\]

Fix a double coset \(\Gamma\alpha\Gamma\), and define the two groups
\[
 H=\Gamma\cap\alpha^{-1}\Gamma\alpha,\qquad
 H'=\Gamma\cap\alpha\Gamma\alpha^{-1}=\alpha H\alpha^{-1}.
 \tag{3.5}
\]
Both contain \(-I\) and \(\Gamma(n)\). To check the latter assertion, write
\(\gamma=I+nB\). Then
\[
 \alpha\gamma\alpha^{-1}=I+\alpha B\alpha^*,\qquad
 \alpha^{-1}\gamma\alpha=I+\alpha^*B\alpha
\]
are integral determinant-one matrices. Both groups therefore have finite index.

Let \(\mathcal F\) be a measurable fundamental set for \(\Gamma\).
If \(\delta\) runs through \(H\backslash\Gamma\), the sets \(\delta\mathcal F\) tile a fundamental set \(\mathcal F_H\), up to null boundaries. Also
\[
 \Gamma\alpha\Gamma=\bigsqcup_{\delta\in H\backslash\Gamma}
                       \Gamma\alpha\delta.
 \tag{3.6}
\]
Indeed, equality of the left cosets for \(\delta_1,\delta_2\) is equivalent to
\(\delta_1\delta_2^{-1}\in H\).
Define \(A_\alpha f=\sum_\delta f\Vert_k\alpha\delta\).
Using (3.4) for \(\delta\), and \(g\Vert_k\delta=g\), gives
\[
 \langle A_\alpha f,g\rangle
   =\int_{\mathcal F_H}(f\Vert_k\alpha)\overline g\,y^k\,d\mu.
 \tag{3.7}
\]
Now change variables \(w=\alpha z\). The set \(\alpha\mathcal F_H\) is fundamental for \(H'\), and (3.4), applied to \(f\) and \(g\Vert_k\alpha^{-1}\), transforms (3.7) into
\[
 \int_{\alpha\mathcal F_H}
          f(w)\overline{(g\Vert_k\alpha^{-1})(w)}
                      \operatorname{Im}(w)^k\,d\mu(w).
\]
Tile this set instead by \(\epsilon\mathcal F\), with
\(\epsilon\in H'\backslash\Gamma\). Independence of the fundamental set gives
\[
 \langle A_\alpha f,g\rangle
       =\left\langle f,\sum_\epsilon
                        g\Vert_k\alpha^{-1}\epsilon\right\rangle
       =\langle f,A_{\alpha^{-1}}g\rangle.             \tag{3.8}
\]
The coset argument (3.6) also applies to the rational matrix \(\alpha^{-1}\).
Since a positive scalar acts trivially in \(\Vert_k\), its double-coset sum equals that for \(\alpha^*=n\alpha^{-1}\).

All the integrals used here are absolutely convergent. The previous lesson proves that \(y^{k/2}|f(z)|\) and \(y^{k/2}|g(z)|\) are globally bounded. By (3.3) the same bound applies after any unitary slash. Products of two such functions times \(y^k\) are bounded, and the finite-index quotients for \(H,H'\) have finite hyperbolic area. This also justifies replacing one measurable fundamental set by another.

Finally, there are finitely many double cosets in \(D_n\), since its left-coset set is finite. Sum (3.8) over them and use the permutation (3.1). Multiplication by the real scalar \(n^{k/2-1}\) in (1.5) proves (3.2). ∎

The groups in (3.5) have different roles: \(f\Vert_k\alpha\) is invariant under \(H\), and \(\alpha\) carries its quotient to the quotient for \(H'\). Interchanging them before changing variables would be incorrect.

## 4. Eigenforms and their Euler products

**Lemma 4.1.** A commuting family of self-adjoint maps on a finite-dimensional positive Hermitian space has an orthogonal basis of simultaneous eigenvectors, even if the family is infinite.

**Proof.**
For a single self-adjoint map \(A\) on a nonzero complex space, its characteristic polynomial has a root, so it has an eigenvector \(v\). If \(Av=\lambda v\), self-adjointness gives
\(\lambda\langle v,v\rangle=\overline\lambda\langle v,v\rangle\), hence \(\lambda\) is real. The orthogonal complement of \(v\) is invariant: if \(\langle w,v\rangle=0\), then
\(\langle Aw,v\rangle=\langle w,Av\rangle=\lambda\langle w,v\rangle=0\).
Induction on dimension diagonalizes \(A\) in an orthogonal basis.

For a commuting family, if all maps are scalar, any orthogonal basis works. Otherwise choose a nonscalar member \(A\). Its eigenspaces are mutually orthogonal and have smaller dimensions; every other member preserves them because it commutes with \(A\). Its restriction to each eigenspace remains self-adjoint. Apply induction to the whole restricted family on each eigenspace. The induction decreases dimension and does not require the family to be finite. ∎

**Theorem 4.2 (normalized eigenbasis).** The space \(S_k\) has an orthogonal basis of simultaneous eigenforms, each normalized by \(a_1=1\). For a normalized eigenform \(f\),
\[
 T_nf=a_n(f)f.
 \tag{4.1}
\]
Every system of simultaneous eigenvalues on \(S_k\) has a one-dimensional eigenspace.

**Proof.**
Finite dimension and positivity come from the preceding lessons; commutativity and self-adjointness are Theorems 2.1 and 3.1. Apply Lemma 4.1.
If \(T_nf=\lambda_nf\), (1.7) gives
\(a_n(f)=\lambda_na_1(f)\) for every \(n\ge1\).
If \(a_1(f)=0\), all coefficients vanish, contradicting \(f\ne0\).
Scaling gives \(a_1=1\) and (4.1). Two normalized cusp eigenforms with the same system have the same Fourier series, hence are equal; every vector in that common eigenspace is therefore a scalar multiple of one of them. ∎

This normalization is not unit norm in the Petersson product.

**Theorem 4.3 (Euler product).** For a normalized cusp eigenform,
\[
 a_{mn}=a_ma_n\quad(\gcd(m,n)=1),\qquad
 a_{p^{r+1}}=a_pa_{p^r}-p^{k-1}a_{p^{r-1}}\quad(r\ge1),
 \tag{4.2}
\]
and, locally uniformly and absolutely for \(\operatorname{Re}s>k/2+1\),
\[
 \boxed{\displaystyle
 L(f,s)=\sum_{n\ge1}\frac{a_n}{n^s}
       =\prod_p(1-a_pp^{-s}+p^{k-1-2s})^{-1}.}
 \tag{4.3}
\]

**Proof.**
Apply (2.3) and (2.4) to \(f\), using (4.1) and \(a_1=1\).
The coefficient bound of the preceding lesson gives
\(|a_n|\le Cn^{k/2}\). Thus the Dirichlet series converges absolutely, uniformly on each region \(\operatorname{Re}s\ge k/2+1+\varepsilon\).

For a fixed prime, let \(x=p^{-s}\). The absolutely convergent series
\(\sum_{r\ge0}a_{p^r}x^r\) satisfies, by (4.2),
\[
 (1-a_px+p^{k-1}x^2)\sum_{r\ge0}a_{p^r}x^r=1.
\]
The constant term is one, the coefficient of \(x\) is zero, and every higher coefficient vanishes by the recurrence. In particular the quadratic factor is nonzero in the stated half-plane.

A finite product of these prime-power series expands, by multiplicativity, into the sum over integers whose prime divisors belong to that finite set. Absolute convergence permits the expansion and shows that these sums tend to \(L(f,s)\) as the set exhausts the primes. Moreover,
\[
 \sum_p\left|\sum_{r\ge1}a_{p^r}p^{-rs}\right|
 \le \sum_p\sum_{r\ge1}|a_{p^r}|p^{-r\operatorname{Re}s}
 \le \sum_{n\ge2}|a_n|n^{-\operatorname{Re}s}<\infty.
\]
The same bound is uniform on each smaller closed half-plane. It proves absolute, locally uniform convergence of the product itself. ∎

The unitary normalization used later is
\[
 \widetilde T_n=n^{-(k-1)/2}T_n,\qquad
 \lambda_n=a_nn^{-(k-1)/2}.
\]
Its Euler product is
\[
 \sum_{n\ge1}\lambda_nn^{-s}
      =L(f,s+(k-1)/2)
      =\prod_p(1-\lambda_pp^{-s}+p^{-2s})^{-1}.
\]
The elementary bound above gives absolute convergence for \(\operatorname{Re}s>3/2\). No optimal bound is being asserted.

## 5. Eisenstein eigenvalues

Recall the constant-one Eisenstein series
\[
 E_k=1+c_k\sum_{m\ge1}\sigma_{k-1}(m)q^m,\qquad
 c_k=-\frac{2k}{B_k}.
\]

**Lemma 5.1.** For \(t\ge0\) an integer and \(m,n\ge1\),
\[
 \sigma_t(m)\sigma_t(n)
       =\sum_{d\mid\gcd(m,n)}d^t\sigma_t(mn/d^2).
 \tag{5.1}
\]

**Proof.**
Both sides factor into contributions at each prime. At one prime, write
\(m=p^u,n=p^v\), and put \(X=p^t\). The required polynomial identity is
\[
 (1+X+\cdots+X^u)(1+X+\cdots+X^v)
    =\sum_{j=0}^{\min(u,v)}X^j(1+X+\cdots+X^{u+v-2j}).
 \tag{5.2}
\]
For \(0\le\ell\le u+v\), the coefficient on the left counts pairs
\(i+h=\ell\), \(0\le i\le u\), \(0\le h\le v\), and equals
\(1+\min(u,v,\ell,u+v-\ell)\). On the right it counts integers
\(0\le j\le\min(u,v)\) with \(j\le\ell\le u+v-j\), giving the same number.
Outside that range both coefficients are zero. This proves the polynomial identity, including \(X=1\), and prime factorization proves (5.1). ∎

**Theorem 5.2.**
\[
 T_nE_k=\sigma_{k-1}(n)E_k.
 \tag{5.3}
\]

**Proof.**
Its constant coefficient is \(\sigma_{k-1}(n)\) by (1.7).
For \(m\ge1\), (1.6) and (5.1) give
\[
 a_m(T_nE_k)
   =c_k\sum_{d\mid\gcd(m,n)}d^{k-1}\sigma_{k-1}(mn/d^2)
   =c_k\sigma_{k-1}(m)\sigma_{k-1}(n).
\]
These are exactly the coefficients of the right side of (5.3). ∎

Since \(M_k=\mathbb CE_k\oplus S_k\), the Eisenstein eigenline and the cusp eigenbasis give an eigenbasis of \(M_k\). The Petersson norm of \(E_k\) diverges; it was not used in the self-adjoint argument on \(S_k\).

## 6. Two computed examples

### 6.1. The discriminant

The space \(S_{12}\) is the line spanned by
\[
 \Delta=\sum_{n\ge1}\tau(n)q^n=q-24q^2+252q^3-1472q^4+4830q^5-6048q^6+\cdots.
\]
Since every \(T_n\) preserves that line and \(a_1(\Delta)=1\), (1.7) gives
\(T_n\Delta=\tau(n)\Delta\). Thus
\[
 \tau(mn)=\tau(m)\tau(n)\quad(\gcd(m,n)=1),\qquad
 \tau(p^{r+1})=\tau(p)\tau(p^r)-p^{11}\tau(p^{r-1}).
 \tag{6.1}
\]
For example, \(\tau(6)=(-24)252=-6048\), and
\(\tau(4)=(-24)^2-2^{11}=576-2048=-1472\).
This is Mordell's eigenform explanation of the identities; it applies to every index, not just the displayed coefficients. The Euler product is
\[
 L(\Delta,s)=\prod_p(1-\tau(p)p^{-s}+p^{11-2s})^{-1},
 \qquad \operatorname{Re}s>7.
\]

### 6.2. The two eigenlines in weight twenty-four

The dimension formula gives \(\dim S_{24}=2\). Choose the basis
\[
 A=E_4^3\Delta,\qquad B=\Delta^2.
\]
From \(E_4=1+240q+2160q^2+6720q^3+\cdots\),
\[
 E_4^3=1+720q+179280q^2+16954560q^3+\cdots.
\]
For clarity, the \(q^2\) coefficient is \(3(2160)+3(240)^2\), and the \(q^3\) coefficient is
\(3(6720)+6(240)(2160)+(240)^3\).
Multiplying by the displayed discriminant gives
\[
 \begin{aligned}
 A&=q+696q^2+162252q^3+12831808q^4+\cdots,\\
 B&=q^2-48q^3+1080q^4+\cdots.
 \end{aligned}                                            \tag{6.2}
\]
For \(A\), the next three coefficients are respectively
\(720-24\), \(179280-24(720)+252\), and
\(16954560-24(179280)+252(720)-1472\).
For \(B\), they are \(1\), \(2(-24)\), and \((-24)^2+2(252)\).
Their different initial orders prove linear independence.

The first two coefficients determine any cusp form in this two-dimensional space. Formula (1.8) gives
\[
 \begin{aligned}
 a_1(T_2A)&=696,&
 a_2(T_2A)&=12831808+2^{23}=21220416,\\
 a_1(T_2B)&=1,&a_2(T_2B)&=1080.
 \end{aligned}
\]
Matching \(q,q^2\) in (6.2) yields
\[
 T_2A=696A+20736000B,\qquad T_2B=A+384B.
\]
Our matrices act on column coordinate vectors, so
\[
 [T_2]_{A,B}=
 \begin{pmatrix}696&1\\20736000&384\end{pmatrix},\qquad
 \det(xI-[T_2])=x^2-1080x-20468736.                 \tag{6.3}
\]
The determinant calculation is \(696\cdot384-20736000=-20468736\).
Its distinct roots are
\[
 \lambda_\pm=540\pm12\sqrt{144169}.
\]
For either root, a normalized eigenvector is
\[
 f_\pm=A+(\lambda_\pm-696)B
      =q+\lambda_\pm q^2+(195660-48\lambda_\pm)q^3+\cdots.
 \tag{6.4}
\]
The first row of (6.3) proves the coefficient of \(A\) in
\(T_2f_\pm=\lambda_\pm f_\pm\); the second is precisely the quadratic equation for \(\lambda_\pm\).
Every \(T_n\) commutes with \(T_2\), so it preserves each of these one-dimensional eigenspaces. Thus \(f_\pm\) are simultaneous eigenforms. Their Petersson orthogonality follows from self-adjointness and their distinct real eigenvalues, even though the matrix (6.3) is not symmetric in this basis.

## 7. Exercises

1. **Easy.** Starting with (1.3) for a prime \(p\), derive both formulas in (1.8), including the constant coefficient.
2. **Easy.** Prove that \(T_nE_k=\sigma_{k-1}(n)E_k\) by comparing all Fourier coefficients.
3. **Medium.** Starting from the lattice identity (2.2), derive the complete form-valued Hecke relation. Explain every power of \(d\).
4. **Medium.** Compute \(T_2\) on \(S_{24}\) in the basis \((E_4^3\Delta,\Delta^2)\), including at least three coefficients of each basis element, its characteristic polynomial and its normalized eigenforms.
5. **Hard.** For positive weight, prove that
\[
 M_k(\mathbb Z)=M_k\cap\mathbb Z[[q]]
\]
is stable under every \(T_n\) and is a lattice spanning \(M_k\). Deduce that normalized eigenforms have algebraic-integer eigenvalues and that every simultaneous eigensystem in \(M_k\) occurs with multiplicity one. Explain what fails in weight zero.

## 8. Full solutions

### Solution 1

The factor pairs of \(p\) are \((p,1)\) and \((1,p)\). Their contributions to (1.3) are \(p^{k-1}f(pz)\) and \(p^{k-1}p^{-k}\sum_b f((z+b)/p)\), respectively. This proves the first formula in (1.8).
The second contribution is
\[
 \frac1p\sum_{r\ge0}a_rq^{r/p}\sum_{b=0}^{p-1}e^{2\pi irb/p}
       =\sum_{\ell\ge0}a_{p\ell}q^\ell.
\]
The first contributes \(p^{k-1}a_{m/p}\) at \(q^m\), with that coefficient zero when \(p\nmid m\).
Thus \(a_m(T_pf)=a_{pm}+p^{k-1}a_{m/p}\); at \(m=0\) this is
\((1+p^{k-1})a_0\), not just \(a_0\).

### Solution 2

Put \(t=k-1\). At \(q^0\), the coefficient formula gives
\(a_0(T_nE_k)=\sum_{d\mid n}d^t=\sigma_t(n)\).
At \(q^m\), \(m\ge1\), it gives
\[
 a_m(T_nE_k)=c_k\sum_{d\mid\gcd(m,n)}d^t\sigma_t(mn/d^2).
\]
To evaluate this sum, factor \(m,n\) into primes and apply (5.2) at each prime with \(X=p^t\). The sum is \(\sigma_t(m)\sigma_t(n)\).
The resulting coefficients are exactly those of \(\sigma_t(n)E_k\), including the constant coefficient, so equality of holomorphic Fourier series proves the assertion. This argument does not assume that the Eisenstein space is one-dimensional, and it uses no divergent Petersson norm.

### Solution 3

Let \(I\) denote the lattice-to-form identification. Homogeneity says
\(IR(d)I^{-1}=d^{-k}\), while (1.3) says
\(I\mathcal T_nI^{-1}=n^{1-k}T_n\).
Therefore (2.2) implies
\[
 \begin{aligned}
 T_mT_n
 &= (mn)^{k-1}I\mathcal T_m\mathcal T_nI^{-1}\\
 &= \sum_{d\mid\gcd(m,n)}
       (mn)^{k-1}d^{1-k}(mn/d^2)^{1-k}T_{mn/d^2}\\
 &= \sum_{d\mid\gcd(m,n)}d^{k-1}T_{mn/d^2}.
 \end{aligned}
\]
The three contributions to the exponent of \(d\) are the chain multiplicity \(d\), homothety \(d^{-k}\), and the inverse normalization
\((mn/d^2)^{1-k}\), whose \(d\)-power is \(d^{2k-2}\).
Their product is \(d^{1-k+2k-2}=d^{k-1}\).
The right side is symmetric in \(m,n\), hence also proves commutativity from the full lattice identity.

### Solution 4

Write \(A=E_4^3\Delta,B=\Delta^2\).
The explicit multiplication in (6.2) gives the coefficients through \(q^4\), which are needed because \(a_2(T_2f)=a_4(f)+2^{23}a_1(f)\).
If \(h=xA+yB\), then \(a_1(h)=x\) and \(a_2(h)=696x+y\).
Consequently
\[
 \begin{aligned}
 T_2A&=696A+(21220416-696^2)B
          =696A+20736000B,\\
 T_2B&=A+(1080-696)B=A+384B.
 \end{aligned}
\]
The dimension formula ensures that this coefficient matching gives the whole images, not only a truncation.

The trace and determinant give (6.3). Completing the square gives
\[
 (x-540)^2=20760336=144\cdot144169,
\]
so the roots are \(\lambda_\pm\).
For \(f=A+cB\), the first coordinate of \(T_2f=\lambda f\) requires
\(c=\lambda-696\); the second then becomes
\(20736000+384(\lambda-696)=\lambda(\lambda-696)\), exactly (6.3).
This gives the normalized forms (6.4). For an additional coefficient check,
\[
 a_4(f)=12831808+1080(\lambda-696)
       =12080128+1080\lambda=\lambda^2-2^{23},
\]
as the prime-square recurrence requires.
Since every \(T_n\) commutes with \(T_2\), its two distinct eigenlines give simultaneous eigensystems. This conclusion uses the whole family; diagonalizing a single operator would not suffice without commutativity.

### Solution 5

It suffices to consider positive even weight with \(M_k\ne0\), so \(k\ge4\).
In odd weight the space is zero, and \(M_2=0\).
Let \(d=\dim M_k\). The integral Victor Miller basis from the preceding ring lesson, Solution 5, is
\[
 F_j=q^j+O(q^d),\quad 0\le j<d,\qquad F_j\in\mathbb Z[[q]].
\]
Every \(f\in M_k\) has the unique expression
\[
 f=\sum_{j=0}^{d-1}a_j(f)F_j.                         \tag{8.1}
\]
Indeed, subtract the right side; its first \(d\) coefficients vanish, and the basis property forces it to be zero. It follows that
\[
 M_k(\mathbb Z)=\bigoplus_{j=0}^{d-1}\mathbb ZF_j,\qquad
 M_k(\mathbb Z)\otimes_{\mathbb Z}\mathbb C=M_k.
 \tag{8.2}
\]
Thus the word “lattice” means a free abelian group of full rank in the rational structure that its basis defines. We are not claiming that a rank-\(d\) abelian group is a cocompact real lattice in the real \(2d\)-dimensional space \(M_k\).

By (1.6), every coefficient of \(T_nf\) is an integer if the coefficients of \(f\) are integers: all \(d^{k-1}\) are integers. Lemma 1.1 puts \(T_nf\) in \(M_k\), so (8.2) is preserved.
The operator consequently has an integer matrix in this basis, and its monic characteristic polynomial lies in \(\mathbb Z[x]\). Every eigenvalue is a root of that polynomial, hence is an algebraic integer. The same argument applies to the cusp lattice
\(\bigoplus_{j=1}^{d-1}\mathbb ZF_j\).

For multiplicity one on all of \(M_k\), let \(0\ne f\) be a simultaneous eigenform, \(T_nf=\lambda_nf\).
Formula (1.7) implies \(a_n(f)=\lambda_na_1(f)\) for all \(n\ge1\).
If \(a_1(f)=0\), then \(f\) is constant. A nonzero constant cannot have positive weight: the law \(f(-1/z)=z^kf(z)\) would require \(z^k=1\) for every \(z\in\mathfrak H\).
Thus \(a_1(f)\ne0\), and we may normalize it to one.
Two normalized forms with the same eigenvalues have equal positive coefficients; their difference is constant and must therefore vanish by the same argument. Every common eigenspace is one-dimensional.

For cusp eigenvalues one can say more: their algebraic conjugates are also roots of the integer characteristic polynomial on the cusp lattice, and every root is real by self-adjointness. They are totally real algebraic integers. The eigenvalues on the remaining Eisenstein line are the rational integers \(\sigma_{k-1}(n)\).

Weight zero is an actual exception to integrality. Here \(M_0=\mathbb C\), and (1.3) gives
\[
 T_n(1)=n^{-1}\sum_{d\mid n}d=\sigma_{-1}(n).
\]
In particular \(T_2(1)=3/2\), which neither preserves \(\mathbb Z[[q]]\) nor is an algebraic integer. Also \(a_1=0\) for every constant form, so the normalization \(a_1=1\) is unavailable. The positive-weight hypothesis is essential.

## What this lesson does not prove

The coprime and prime-power lattice identities (2.1) are proved by counting the intermediate sublattices in Section 2. The full relation on forms, including every normalization factor, is proved in Theorem 2.1 and Solution 3. We do not develop the local spherical Hecke algebra, its Satake isomorphism or its restricted tensor product description; those are the subject of *The spherical Hecke algebra of GL₂ and Hecke operators on lattices*.

The finite-dimensional modular spaces and their dimensions are established in the ring lesson, Theorem 2.2; its Solution 5 supplies the integral Victor Miller basis. The modular/lattice identification is the lattice lesson, Section 2. The integrability, independence of measurable fundamental sets, positivity and coefficient bound are the preceding Petersson lesson, Theorems 1.1 and 2.1. Fundamental-set tiling and finite quotient area come from *The upper half-plane and the modular group*, Theorem 3.2 and Proposition 5.1, and the congruence-subgroup lesson, Section 1.

The removable-singularity theorem and the existence of a complex root for the characteristic polynomial in Lemma 4.1 are proved in the earlier Petersson lesson, Lemma 0.1, from the first lesson's circle formula. The simultaneous spectral argument itself is proved here. Elementary unique prime factorization and finite-dimensional basis arithmetic remain foundational prerequisites whose exact earlier programme proofs have not been verified here.

No continuation or functional equation of \(L(f,s)\), optimal Ramanujan–Petersson bound, higher-level multiplicity-one theorem or unproved irreducibility assertion is used. The integral-eigenvalue argument here is for positive weight at level one.

## References

- **Stein, free author text.** W. Stein, *Modular Forms: A Computational Approach*, §§2.3–2.5, especially Proposition 2.28, Proposition 2.30 and Algorithm 2.36. We cite the [freely accessible author-hosted PDF](https://wstein.org/books/modform/stein-modform.pdf), whose free availability is confirmed on the [author's distribution page](https://wstein.org/books/modform/README.html). Its bracket slash includes \(\det(\alpha)^{k-1}\); its computational matrices act from the right on row coordinates. Matrix (6.3) uses columns. The chain-counting proof is supplied locally above.
- **Voight 2021.** J. Voight, *Quaternion Algebras*, §40.5, formulas (40.5.7)–(40.5.11) and Theorem 40.5.12. [Author's open-access book page](https://jvoight.github.io/quat.html).
- **Wiese 2018.** G. Wiese, *Computational Arithmetic of Modular Forms*, §§7.1–7.2, for the two intersection subgroups, double-coset action and Fourier formula. [Author's notes](https://arxiv.org/abs/1809.04645).
- **Deligne, free original article.** P. Deligne, *Formes modulaires et représentations de GL(2)*, §1.1.1–§1.1.7, for the lattice-function interpretation and its homogeneity convention. [Author's institutional manuscript](https://publications.ias.edu/sites/default/files/Number21.pdf). The operator and adjoint proofs above are given in the classical upper-half-plane model.
- **Lebl.** J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9, Theorems 3.3.11 and 5.2.2. [Author's complex-analysis text](https://www.jirka.org/ca/ca.pdf).

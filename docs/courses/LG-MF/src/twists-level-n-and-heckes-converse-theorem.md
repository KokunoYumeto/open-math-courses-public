# Twists, level N and Hecke's converse theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A level changes the scale of the Mellin integral. A character twist changes the coefficients and introduces a Gauss sum into the reflection. Conversely, a functional equation recovers an inversion law. At level one this inversion and the Fourier period generate the modular group; at higher level we need equations for twists to recover the remaining transformations.

We retain \(q=e^{2\pi iz}\), and use \(r\) for a character conductor. For a real matrix \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) with positive determinant and integral weight, the unitary slash is
\[
(f\Vert_k A)(z)=\det(A)^{k/2}(cz+d)^{-k}f(Az).
\tag{0.1}
\]
It is a right action. Positive scalar matrices act trivially. Put
\[
W_N=\begin{pmatrix}0&-1\\N&0\end{pmatrix},\qquad
(f\Vert_kW_N)(z)=N^{-k/2}z^{-k}f(-1/(Nz)).
\tag{0.2}
\]
These are the conventions of lesson 10. Initially \(k\ge2\) is even and the original nebentypus is trivial. The more general Hecke correspondence in Section 4 explicitly allows real positive weight and a multiplier.

## 1. The level in the completion

Conjugation gives
\[
W_N^{-1}\begin{pmatrix}a&b\\c&d\end{pmatrix}W_N
=\begin{pmatrix}d&-c/N\\-Nb&a\end{pmatrix}\in\Gamma_0(N)
\quad(c\equiv0\pmod N).
\]
Thus Fricke preserves the modular transformation law with trivial character. It also preserves cusp vanishing: a rational matrix carries a rational cusp to another rational cusp, and the upper triangular factor after choosing its cusp scaling matrix has a positive affine slope. This is the cusp pullback argument after equation (2.3) of lesson 9. Also \(W_N^2=-NI\), so \(\Vert_kW_N\) squares to the identity at even weight. Its nonzero eigenvectors have eigenvalue \(\epsilon=\pm1\).

**Theorem 1.1 (level \(N\) functional equation).** Let
\[
f(z)=\sum_{n\ge1}a_nq^n\in S_k(\Gamma_0(N)),\qquad
f\Vert_kW_N=\epsilon f.
\]
Then
\[
\Lambda_N(f,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(f,s),\qquad
L(f,s)=\sum_{n\ge1}a_nn^{-s},
\tag{1.1}
\]
initially for \(\operatorname{Re}s>k/2+1\), continues to an entire function bounded on every closed vertical strip. It satisfies
\[
\Lambda_N(f,s)=w\Lambda_N(f,k-s),\qquad w=i^k\epsilon.
\tag{1.2}
\]
In particular, \(w=-1\) forces \(L(f,k/2)=0\).

**Proof.** The cusp coefficient estimate gives \(|a_n|\le Cn^{k/2}\), so the initial series converges absolutely and locally uniformly in the stated half-plane. Set
\[
G(t)=f(it/\sqrt N),\qquad b_N=2\pi/\sqrt N.
\]
The slash equation evaluated at \(z=it/\sqrt N\) gives
\[
G(1/t)=i^k\epsilon t^kG(t)=wt^kG(t).
\tag{1.3}
\]
For \(t\ge1\), the Fourier series and coefficient bound give
\[
|G(t)|\le C\sum_{n\ge1}n^{k/2}e^{-b_Nnt}
\le C'e^{-b_Nt/2}.
\]
Here \(nt\ge(n+t)/2\) for \(n,t\ge1\). Equation (1.3) then bounds \(G(t)\), for \(0<t\le1\), by \(C't^{-k}e^{-b_N/(2t)}\). Both estimates remain integrable after multiplication by every fixed real power of \(t\).

On the initial half-plane the absolute sum–integral majorant is
\[
\sum_n|a_n|\int_0^\infty e^{-b_Nnt}t^{\sigma-1}\,dt
=\Gamma(\sigma)b_N^{-\sigma}\sum_n|a_n|n^{-\sigma}<\infty.
\]
Consequently
\[
\Lambda_N(f,s)=\int_0^\infty G(t)t^{s-1}\,dt.
\tag{1.4}
\]
This integral is entire: on a compact set of \(s\), the two exponential bounds also dominate every extra factor \(|\log t|^j\) required for differentiation. Substitution \(t=1/u\) in its interval \((0,1)\) gives, with
\(A(s)=\int_1^\infty G(t)t^{s-1}\,dt\),
\[
\Lambda_N(f,s)=A(s)+wA(k-s).
\tag{1.5}
\]
Since \(w^2=1\), this proves (1.2). If \(a\le\sigma\le b\), an integrable majorant for the whole integral is
\[
|G(t)|\begin{cases}t^{a-1},&0<t\le1,\\t^{b-1},&t\ge1.\end{cases}
\]
It is independent of \(\operatorname{Im}s\), proving boundedness on the entire strip. Multiplication by the entire function \(N^{-s/2}(2\pi)^s/\Gamma(s)\) continues \(L(f,s)\) too. At the centre, \(w=-1\) makes the completion zero; its Gamma and level factors there are nonzero. \(\square\)

The eigenvector hypothesis is convenient rather than essential. If \(h=f\Vert_kW_N\), the same argument gives
\[
\Lambda_N(f,s)=i^k\Lambda_N(h,k-s).
\tag{1.6}
\]
Indeed \(h(it/\sqrt N)=i^{-k}t^{-k}G(1/t)\). We will use this paired version for nonreal character twists.

## 2. Primitive Gauss sums and twisting

A Dirichlet character \(\psi\) of conductor \(r\) is extended by zero on nonunits. Define
\[
\tau(\psi)=\sum_{u\bmod r}\psi(u)e^{2\pi iu/r}.
\]
We need primitivity at precisely the following point.

**Lemma 2.1 (the primitive Gauss identities).** For primitive \(\psi\),
\[
\sum_{u\bmod r}\psi(u)e^{2\pi inu/r}
=\overline\psi(n)\tau(\psi),\qquad
|\tau(\psi)|^2=r,\qquad
\tau(\psi)\tau(\overline\psi)=\psi(-1)r.
\tag{2.1}
\]

**Proof.** For a unit \(n\), replacing \(u\) by \(n^{-1}u\) proves the first identity. If \(d=(n,r)>1\), the exponential is unchanged by multiplying \(u\) by any unit \(v\equiv1\pmod{r/d}\). Some such \(v\) has \(\psi(v)\ne1\), since otherwise \(\psi\) would factor through the unit group modulo the proper divisor \(r/d\), contrary to primitivity. The reduction to that group is surjective: lift a unit residue and use the Chinese remainder theorem to avoid each additional prime dividing \(r\). Multiplication by this \(v\) makes the sum equal to \(\psi(v)^{-1}\) times itself, so it is zero, as is \(\overline\psi(n)\).

Write the left side as \(S(n)\). Expanding its squared modulus and summing over \(n\bmod r\), the finite geometric sum is \(r\) when its two indices coincide and zero otherwise. Thus
\[
\sum_{n\bmod r}|S(n)|^2=r\sum_{u\bmod r}|\psi(u)|^2=r\varphi(r).
\]
By the first identity exactly \(\varphi(r)\) summands have modulus \(|\tau(\psi)|\); hence \(|\tau(\psi)|^2=r\). Finally complex conjugation and \(u\mapsto-u\) give
\(\tau(\overline\psi)=\psi(-1)\overline{\tau(\psi)}\), proving the product formula. The conductor-one case consists of the single term one and satisfies the same formulas. \(\square\)

**Lemma 2.1a (Poisson summation with a primitive character).** Let \(\psi\) be primitive of conductor \(r\). Use the Fourier convention
\(\widehat\phi(\xi)=\int_{\mathbb R}\phi(u)e^{-2\pi iu\xi}\,du\).
Suppose \(\phi\) and \(\widehat\phi\) are continuous and both are
\(O((1+|u|)^{-1-\delta})\) for some \(\delta>0\). Then
\[
\begin{gathered}
\sum_{n\in\mathbb Z}\psi(n)\phi(n)\\
=\frac{\tau(\psi)}r
 \sum_{m\in\mathbb Z}\overline\psi(m)\widehat\phi(m/r).
\end{gathered}
\tag{2.1a}
\]
Both sums are absolutely convergent.

**Proof.** For each residue \(u\) modulo \(r\), put \(h_u(v)=\phi(u+rv)\). An absolutely convergent change of variable gives
\(\widehat h_u(\xi)=r^{-1}e^{2\pi iu\xi/r}\widehat\phi(\xi/r)\).
These functions satisfy the decay and continuity hypotheses of ordinary Poisson summation, Poisson summation, theta, and the functional equation, Theorem 1.2. Applying it at zero gives
\[
\begin{gathered}
\sum_{\ell\in\mathbb Z}\phi(u+r\ell)\\
=\frac1r\sum_{m\in\mathbb Z}
 \widehat\phi(m/r)e^{2\pi imu/r}.
\end{gathered}
\tag{2.1b}
\]
Multiply by \(\psi(u)\) and sum over the finitely many residues. Absolute convergence permits reordering. Lemma 2.1 identifies the inner finite sum as
\(\overline\psi(m)\tau(\psi)\), including nonunit \(m\), and proves (2.1a). \(\square\)

In particular, let \(r>1\), \(\psi(-1)=(-1)^a\) with \(a\in\{0,1\}\), and \(x>0\). The Gaussian transform in the same programme lesson, Lemma 2.1, gives
\[
\begin{gathered}
\phi_{a,x}(u)=u^a e^{-\pi xu^2/r},\\
\widehat\phi_{a,x}(\xi)\\
=(-i)^a(r/x)^{a+1/2}\xi^a e^{-\pi r\xi^2/x}.
\end{gathered}
\tag{2.1c}
\]
For \(a=1\), differentiate the Gaussian transform under its absolutely convergent integral: multiplication by \(u\) is \(i/(2\pi)\) times differentiation in \(\xi\). This gives the minus sign in \(-i\xi\). Gaussian decay justifies the differentiation and supplies every decay hypothesis of Lemma 2.1a.

Writing
\(\theta_\psi(x)=\sum_{n\in\mathbb Z}\psi(n)n^a e^{-\pi n^2x/r}\),
substitution of (2.1c) into (2.1a) gives
\[
\begin{gathered}
\theta_\psi(x)\\
=\frac{\tau(\psi)}{i^a\sqrt r}\,
 x^{-a-1/2}\theta_{\overline\psi}(1/x).
\end{gathered}
\tag{2.1d}
\]
The \(r\)-power is
\[
\begin{gathered}
r^{-1}(r/x)^{a+1/2}r^{-a}\\
=r^{-1/2}x^{-a-1/2}.
\end{gathered}
\]
Also \((-i)^a=i^{-a}\). The zero-index term vanishes because \(r>1\) and \(\psi(0)=0\). This is the exact theta transformation used in The functional equation of Dirichlet L-functions, Theorem 1.1. Its Section 2 gives the full convergent Mellin-integral proof of entire continuation and the completed reflection. These section proofs, together with the residue-class calculation above, supply the classical Dirichlet input used in Solution 4.

For \(A_u=\begin{pmatrix}1&u/r\\0&1\end{pmatrix}\), define the coefficient twist
\[
f_\psi(z)=\sum_{n\ge1}\psi(n)a_nq^n.
\]
The Gauss sum is nonzero, and (2.1) gives the exact averaging formula
\[
f_\psi=\frac1{\tau(\overline\psi)}
\sum_{u\bmod r}\overline\psi(u)f\Vert_k A_u.
\tag{2.2}
\]
All Fourier series involved converge normally on the upper half-plane, so the finite sum and coefficients can be interchanged.

**Theorem 2.2 (level, character and Fricke constant).** Suppose \((r,N)=1\) and \(\psi\) is primitive. Then
\[
f_\psi\in S_k(\Gamma_0(Nr^2),\psi^2).
\tag{2.3}
\]
If \(f\Vert_kW_N=\epsilon f\), then
\[
f_\psi\Vert_kW_{Nr^2}
=\epsilon\psi(N)\frac{\tau(\psi)^2}{r}f_{\overline\psi}.
\tag{2.4}
\]
In particular, its entire, bounded-strip completion satisfies
\[
\Lambda_{Nr^2}(f_\psi,s)
=i^k\epsilon\psi(N)\frac{\tau(\psi)^2}{r}
\Lambda_{Nr^2}(f_{\overline\psi},k-s).
\tag{2.5}
\]
The notation \(\psi^2\) in (2.3) means its induced nebentypus on units modulo \(Nr^2\).

**Proof of the level and character.** For
\(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(Nr^2)\), choose
\(v\equiv ud a^{-1}\equiv ud^2\pmod r\). Direct multiplication gives
\[
A_u\gamma A_v^{-1}
=\begin{pmatrix}
a+uc/r&b+(ud-av)/r-ucv/r^2\\
c&d-cv/r
\end{pmatrix}\in\Gamma_0(N).
\tag{2.6}
\]
Every entry is integral, the lower left is divisible by \(N\), and the determinant is one. Changing \(v\) by a multiple of \(r\) only adds an integral translation to \(A_v\), which fixes \(f\). Therefore \(f\Vert_kA_u\gamma=f\Vert_kA_v\). Multiplication by \(d^2\) permutes residues, and
\(\overline\psi(u)=\psi(d)^2\overline\psi(v)\). Reindexing (2.2) proves
\(f_\psi\Vert_k\gamma=\psi(d)^2f_\psi\).

For completeness, take a cusp scaling matrix \(\beta\in SL_2(\mathbb Z)\). Choose \(\alpha\in SL_2(\mathbb Z)\) sending \(\infty\) to the rational point \(A_u\beta\infty\). The matrix \(\alpha^{-1}A_u\beta\) is upper triangular of determinant one, and its affine slope is positive. Consequently \((f\Vert_kA_u)\Vert_k\beta\) is a constant multiple of \(f|_k\alpha\) at an affine argument whose imaginary part tends to infinity. It tends to zero, uniformly for the real coordinate in a bounded interval. Its finite sum does too. The established transformation law supplies a positive cusp period and a unit modulus multiplier; its Fourier expansion has a possible fractional shift. Decay excludes all nonpositive exponents. Thus (2.3) includes vanishing at every cusp.

**Proof of the Fricke constant.** Terms with nonunit \(u\) vanish. For a unit, choose
\[
v\equiv-(Nu)^{-1}\pmod r,\qquad ar-uNv=1,\qquad
\gamma_u=\begin{pmatrix}a&u\\Nv&r\end{pmatrix}\in\Gamma_0(N).
\]
The congruence makes \(a=(1+uNv)/r\) integral. Both sides of the following identity are exactly the displayed matrix:
\[
A_uW_{Nr^2}=r\gamma_uW_NA_v
=\begin{pmatrix}Nru&-1\\Nr^2&0\end{pmatrix}.
\tag{2.7}
\]
The scalar \(r\) acts trivially in (0.1), and \(f\Vert_k\gamma_u=f\). Apply (2.7) in (2.2). Since
\(u\equiv-(Nv)^{-1}\pmod r\),
\[
\overline\psi(u)=\psi(-1)\psi(N)\psi(v).
\]
It follows that
\[
f_\psi\Vert_kW_{Nr^2}
=\epsilon\psi(-1)\psi(N)
\frac{\tau(\psi)}{\tau(\overline\psi)}f_{\overline\psi}
=\epsilon\psi(N)\frac{\tau(\psi)^2}{r}f_{\overline\psi}.
\]
The second equality uses the product formula in (2.1); both appearances of \(\psi(-1)\) cancel. This proves (2.4). The paired Mellin argument (1.6), now at level \(Nr^2\), proves (2.5). Each function decays at both relevant cusps, so the entireness and strip estimates of Theorem 1.1 apply individually. \(\square\)

The phase in (2.5) has modulus one. For a nonreal \(\psi\), the equation pairs two different series; it need not be a scalar equation for one series. Applying the paired equations twice is consistent because
\(\psi(N)\overline\psi(N)=1\) and
\(\tau(\psi)^2\tau(\overline\psi)^2/r^2=1\).

The theorem proves a **containing level**. For a form whose declared level is not its least level, \(Nr^2\) need not be least either. Moreover the coefficient twist, which deletes coefficients divisible by the twisting conductor, must be distinguished from the primitive newform twist characterized by good-prime coefficients. They agree away from the twisting conductor; local newform theory determines the remaining Euler factors and conductor. The distinction is made explicitly by Best et al., Section 11.1, equations (11.1.1)–(11.1.3).

## 3. Two complete examples

### 3.1. The form of level eleven

The complete level eleven example in lesson 9, Section 6, establishes
\[
f(z)=\eta(z)^2\eta(11z)^2
=q\prod_{m\ge1}(1-q^m)^2(1-q^{11m})^2
\in S_2(\Gamma_0(11)).
\tag{3.1}
\]
That space has dimension one and no old part, so the first coefficient one normalizes its newform. Write the product after the leading \(q\) as \(\sum_{j\ge0}b_jq^j\). Its logarithmic derivative gives the exact coefficient recursion
\[
b_0=1,\qquad
j b_j=-2\sum_{h=1}^j
\bigl(\sigma_1(h)+11\,\mathbf1_{11\mid h}\sigma_1(h/11)\bigr)b_{j-h},
\qquad a_n=b_{n-1}.
\tag{3.2}
\]
For example,
\[
b_1=-2,\quad 2b_2=-2(-2+3)=-2,\quad
3b_3=-2(-1-6+4)=6.
\]
Applying (3.2) through \(j=19\) gives all coefficients used below. The last column also anticipates the second example.

| \(n\) | \(a_n\) | \(\psi_3(n)a_n\) |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | −2 | 2 |
| 3 | −1 | 0 |
| 4 | 2 | 2 |
| 5 | 1 | −1 |
| 6 | 2 | 0 |
| 7 | −2 | −2 |
| 8 | 0 | 0 |
| 9 | −2 | 0 |
| 10 | −2 | −2 |
| 11 | 1 | −1 |
| 12 | −2 | 0 |
| 13 | 4 | 4 |
| 14 | 4 | −4 |
| 15 | −1 | 0 |
| 16 | −4 | −4 |
| 17 | −2 | 2 |
| 18 | 4 | 0 |
| 19 | 0 | 0 |
| 20 | 2 | −2 |

In particular, \(a_{11}=1\). At a good prime the recurrence is
\(a_{p^2}=a_p^2-p\): it gives \(a_4=4-2=2\) and \(a_9=1-3=-2\). Coprime multiplicativity gives \(a_6=a_2a_3=2\), agreeing with the product.

The squared eta inversion, in the convention used in lesson 9, is
\(\eta(-1/z)^2=-iz\eta(z)^2\). Applying it twice gives
\[
f(-1/(11z))=(-i11z)(-iz)\eta(11z)^2\eta(z)^2
=-11z^2f(z).
\]
Thus
\[
f\Vert_2W_{11}=-f,\qquad \epsilon=-1,\qquad w=i^2\epsilon=+1.
\tag{3.3}
\]
The central point is \(s=1\), and the sign imposes no zero there. The Euler product, in the raw coefficient normalization, is
\[
L(f,s)=(1-11^{-s})^{-1}
\prod_{p\ne11}(1-a_pp^{-s}+p^{1-2s})^{-1}.
\tag{3.4}
\]
The coefficient estimate of lesson 7 gives the initial absolute domain \(\operatorname{Re}s>2\). The optimal domain from Ramanujan–Petersson requires the geometric proof still tracked in lesson 11, Section 5; no such bound is used in the calculation below. The good-prime factors at two and three are
\((1+2\cdot2^{-s}+2^{1-2s})^{-1}\) and
\((1+3^{-s}+3^{1-2s})^{-1}\). The completion is
\[
\Lambda_{11}(f,s)=11^{s/2}(2\pi)^{-s}\Gamma(s)L(f,s)
=\Lambda_{11}(f,2-s).
\]

### 3.2. The quadratic twist of conductor three

Let
\[
\psi_3(n)=\begin{cases}0,&3\mid n,\\1,&n\equiv1\pmod3,\\-1,&n\equiv2\pmod3.\end{cases}
\]
It is primitive, odd and real. With \(\zeta_3=e^{2\pi i/3}\),
\[
\tau(\psi_3)=\zeta_3-\zeta_3^2=i\sqrt3,\qquad
\psi_3(11)=-1,\qquad \tau(\psi_3)^2/3=-1.
\]
Formula (2.2) is explicitly
\[
f_{\psi_3}(z)=\frac{f(z+1/3)-f(z+2/3)}{i\sqrt3}.
\tag{3.5}
\]
For \(n\equiv1,2,0\pmod3\), its exponential quotient is respectively \(1,-1,0\), which computes every coefficient in the table.

For the matrix proof, the choices \((u,v,a)=(1,1,4),(2,2,15)\) give
\[
\gamma_1=\begin{pmatrix}4&1\\11&3\end{pmatrix},\qquad
\gamma_2=\begin{pmatrix}15&2\\22&3\end{pmatrix}.
\]
Their determinants are \(12-11=1\) and \(45-44=1\), and
\(A_uW_{99}=3\gamma_uW_{11}A_v\). The Fricke constant is
\[
(-1)(-1)(-1)=-1.
\]
Therefore
\[
f_{\psi_3}\in S_2(\Gamma_0(99)),\qquad
f_{\psi_3}\Vert_2W_{99}=-f_{\psi_3},\qquad
\Lambda_{99}(f_{\psi_3},s)=\Lambda_{99}(f_{\psi_3},2-s).
\tag{3.6}
\]
Here the induced \(\psi_3^2\) is trivial on units. These statements prove the declared level and sign without an additional assertion about least conductor.

For another coefficient check, \(a_2(f_{\psi_3})=2\) and \(a_4(f_{\psi_3})=2=2^2-2\). Its good-prime factor at two is \((1-2\cdot2^{-s}+2^{1-2s})^{-1}\). All multiples of three have coefficient zero, giving factor one at three. At eleven, multiplicativity and \(a_{11}=1\) give twisted coefficients \((-1)^j\) at \(11^j\), hence factor \((1+11^{-s})^{-1}\). More generally,
\[
L(f_{\psi_3},s)=(1+11^{-s})^{-1}
\prod_{p\ne3,11}(1-\psi_3(p)a_pp^{-s}+p^{1-2s})^{-1}.
\]
This product concerns the coefficient twist in (3.5).

## 4. Hecke's converse with its constant term

Let \(\lambda>0\), \(k>0\) real and \(\gamma\in\{1,-1\}\). Set
\[
F(z)=a_0+\sum_{n\ge1}a_ne^{2\pi inz/\lambda},\qquad
D(s)=\sum_{n\ge1}a_nn^{-s},\qquad
\Phi(s)=(\lambda/(2\pi))^s\Gamma(s)D(s).
\tag{4.1}
\]
Suppose \(|a_n|\le Kn^C\), increasing \(C\) to a nonnegative integer if necessary. This makes \(F\) holomorphic on the upper half-plane and periodic with period \(\lambda\). In \((z/i)^k\) we use the holomorphic logarithm on the right half-plane; on \(z=iy\) this power is the positive real \(y^k\).

**Theorem 4.1 (Hecke correspondence).** The inversion law
\[
F(-1/z)=\gamma(z/i)^kF(z)
\tag{4.2}
\]
is equivalent to these analytic conditions:

1. \(\Phi\) continues meromorphically, with no poles except possible simple poles at \(0,k\), whose residues are \(-a_0,\gamma a_0\), respectively.
2. The entire function \(s(s-k)\Phi(s)\) has finite order on every fixed vertical strip: for each \(a<b\) there are constants \(A,B,\rho>0\) such that its modulus is at most \(A\exp(B(1+|t|)^\rho)\) for \(a\le\operatorname{Re}s\le b\).
3. \(\Phi(s)=\gamma\Phi(k-s)\).

For nonzero \(F\) and a discrete group \(G_\lambda=\langle z\mapsto z+\lambda,z\mapsto-1/z\rangle\), these laws give its automorphy with the indicated multiplier and holomorphy at its cusps. In particular, if \(\lambda=1\), \(k\ge2\) is even and \(\gamma=i^k\), they give \(F\in M_k(SL_2(\mathbb Z))\); if also \(a_0=0\), they give \(F\in S_k(SL_2(\mathbb Z))\).

**Proof, from inversion to analysis.** Write \(g(y)=F(iy)-a_0\). Its polynomial coefficient bound gives exponential decay as \(y\to\infty\). The inversion law says
\[
g(y)=\gamma y^{-k}g(1/y)+\gamma a_0y^{-k}-a_0.
\]
For \(\operatorname{Re}s>\max(C+1,k)\), the Mellin transform of \(g\) converges absolutely. Termwise integration, with the finite majorant
\(\Gamma(\sigma)(\lambda/(2\pi))^\sigma\sum_n|a_n|n^{-\sigma}\), identifies it with \(\Phi(s)\). Split at one and substitute \(y=1/u\) below one. With the entire function
\(A(s)=\int_1^\infty g(y)y^{s-1}\,dy\), this gives
\[
\Phi(s)=A(s)+\gamma A(k-s)
+\frac{\gamma a_0}{s-k}-\frac{a_0}{s}.
\tag{4.3}
\]
The entire integrals admit differentiation of every order, dominated by their exponential decay. Formula (4.3) proves the poles, residues and reflection. On any fixed strip, both integrals are bounded independently of \(t\), and the rational terms are bounded outside small neighborhoods of their poles. Thus \(s(s-k)\Phi(s)\) has polynomial growth there, which is stronger than the stated finite-order condition.

**Proof, from analysis to inversion.** Choose
\[
b>\max(C+1,k),\qquad a=k-b<0,\qquad R>1-a.
\]
The functions \(y^bg(y)\), \(y^{b+1}g'(y)\), \(y^{b+2}g''(y)\) are integrable for \(dy/y\). Indeed termwise differentiation of order \(j\le2\) gives \(O(y^{-C-j-1})\) near zero and exponential decay near infinity. The estimate near zero follows by comparing \(\sum n^{C+j}e^{-2\pi ny/\lambda}\) with its rescaled integral, with a fixed additional first-term bound. Since \(b>C+1\), all three integrals converge. The L-function of a cusp form, Lemma 8.1, proves smooth Mellin inversion under exactly these three conditions, for any real \(b\). It therefore gives
\[
g(y)=\frac1{2\pi i}\int_{b-i\infty}^{b+i\infty}\Phi(s)y^{-s}\,ds.
\tag{4.4}
\]
We justify its contour shift under the specified finite-order condition.

On the line \(b+it\), the Dirichlet series is uniformly bounded by \(\sum |a_n|n^{-b}\). Euler's Gamma integral with \(u=e^x\) is the Fourier transform of \(e^{bx-e^x}\). Every derivative of this function is integrable and vanishes at both ends: at minus infinity it has exponential decay \(e^{bx}\), and at plus infinity \(e^{-e^x}\) dominates each polynomial in \(e^x\). Repeated integration by parts therefore gives \(\Gamma(b+it)=O_M((1+|t|)^{-M})\) for every fixed integer \(M\). The positive real scale in (4.1) changes this modulus by a constant. Hence \(\Phi\) decays to every polynomial order on this line. The functional equation gives the same estimate on \(a+it\).

The function
\[
H(s)=s(s-k)(s+R)^2\Phi(s)
\]
is entire, has finite order in the strip and is bounded on its two boundary lines, taking \(M=4\). Let that boundary bound be \(K_0\). Put \(h=(a+b)/2\) and choose \(0<\kappa<\pi/(b-a)\). For \(\delta>0\), consider
\[
H(s)\exp\{-\delta\cos(\kappa(s-h))\}.
\]
Throughout the strip,
\[
\operatorname{Re}\cos(\kappa(s-h))
\ge\cos(\kappa(b-a)/2)\cosh(\kappa t)>0.
\]
Thus the multiplier has modulus at most one on the vertical edges. On the horizontal edges its decay \(\exp(-c\delta\cosh(\kappa T))\) dominates the finite-order bound \(A'\exp(B'(1+T)^{\rho'})\), including the polynomial factor in \(H\). For each \(\eta>0\), sufficiently tall rectangles have every boundary value bounded by \(K_0+\eta\). The maximum modulus principle gives this bound inside each rectangle. Exhaust the strip, let \(\eta\downarrow0\), and then let \(\delta\downarrow0\) at a fixed point. It follows that \(|H(s)|\le K_0\) throughout the strip. Therefore, uniformly there for \(|t|\ge1\),
\[
|\Phi(\sigma+it)|=O((1+|t|)^{-4}).
\tag{4.5}
\]
The two cancelled poles lie at height zero and cause no exception to this estimate.

Apply the residue theorem to \(\Phi(s)y^{-s}\) on the rectangle with vertical edges \(a,b\), oriented counterclockwise with the right edge upward. Equation (4.5) makes both horizontal integrals tend to zero; \(y^{-\sigma}\) is bounded on the fixed strip. Its two residues are \(-a_0\) and \(\gamma a_0y^{-k}\). The vertical integrals converge absolutely. Thus
\[
\begin{aligned}
g(y)&=-a_0+\gamma a_0y^{-k}
+\frac1{2\pi i}\int_{a-i\infty}^{a+i\infty}\Phi(s)y^{-s}\,ds\\
&=-a_0+\gamma a_0y^{-k}
+\frac{\gamma y^{-k}}{2\pi i}\int_{b-i\infty}^{b+i\infty}\Phi(w)y^w\,dw\\
&=-a_0+\gamma a_0y^{-k}+\gamma y^{-k}g(1/y).
\end{aligned}
\tag{4.6}
\]
In the second line \(w=k-s\); its sign and reversed orientation cancel. Adding \(a_0\) gives \(F(iy)=\gamma y^{-k}F(i/y)\), equivalently (4.2) on the positive imaginary axis. Both sides of (4.2) are holomorphic with the declared logarithm. The identity theorem extends the equality to the upper half-plane.

Periodicity supplies the other generator. Composing the two established laws gives the automorphy factor for every word in the generators. For nonzero \(F\), any two words defining the same transformation give equal factors where \(F\ne0\), hence everywhere by holomorphy. Thus they consistently define its multiplier. For integral weight this is the usual weight slash law, with unit modulus constants on the generators; for real weight the logarithmic branches contribute only unit modulus cocycle constants.

To check holomorphy at a cusp of a discrete \(G_\lambda\), the coefficient estimate gives a bound uniform in the real coordinate,
\[
|F(x+iy)|=O(y^{-C-1})\quad(0<y\le1).
\]
For a cusp scaling matrix \(\sigma\), if its lower left entry is nonzero, \(\operatorname{Im}(\sigma(x+iy))\) is comparable to \(1/y\) as \(y\to\infty\), uniformly on bounded \(x\)-intervals. The weight factor then gives polynomial growth for \(F\) in this cusp coordinate. If that entry is zero, the original expansion gives bounded growth directly. The parabolic period in the cusp coordinate has a multiplier of modulus one, say \(e^{2\pi i\alpha}\) with \(0\le\alpha<1\). Its Fourier exponents are \(n+\alpha\). Polynomial growth excludes every negative exponent: integrating a Fourier coefficient along a horizontal period bounds it by a polynomial times \(e^{2\pi(n+\alpha)y/h}\), which tends to zero for \(n+\alpha<0\). The remaining expansion is bounded and holomorphic at the cusp in the appropriate multiplier convention.

For \(\lambda=1\), even integral \(k\) and \(\gamma=i^k\), (4.2) reduces to \(F(-1/z)=z^kF(z)\). Together with period one it gives ordinary modularity for \(S,T\). There is one cusp orbit. Its Fourier constant \(a_0\) determines whether the form vanishes there. This proves the final assertions. \(\square\)

The analytic correspondence itself needs no discreteness assumption on \(G_\lambda\). We do not conclude that every positive \(\lambda\) gives a discrete group. In the case \(\lambda=2\), used in Solution 4, the generators lie in \(SL_2(\mathbb Z)\), so discreteness is immediate. A zero constant at infinity need not mean vanishing at every cusp of a group with more than one cusp orbit.

## 5. What the twists recover: Weil's theorem

For level one, the untwisted equation recovered both modular generators. At level \(N\), it only relates \(f\) to its Fricke transform, besides the already known period one. Weil's converse uses many twists to recover the \(\Gamma_0(N)\) transformation law. Here is a precise even-weight, trivial-character specialization of his classical statement.

**Theorem 5.1 (Weil).** Let \(k\ge2\) be even, \(N\ge1\), \(\epsilon=\pm1\), and \(a_n=O(n^C)\), not all zero. Let \(\mathcal P\) consist of odd primes not dividing \(N\), meeting every reduced arithmetic progression: for all integers \(b>0\) and \((a,b)=1\), some \(r\in\mathcal P\) satisfies \(r\equiv a\pmod b\). Suppose the untwisted completion (1.1) is entire, bounded in every vertical strip and satisfies (1.2). For every primitive nonprincipal character \(\psi\) modulo every \(r\in\mathcal P\), suppose the completion of \(\sum\psi(n)a_nn^{-s}\) at level \(Nr^2\) is entire, bounded in strips and satisfies (2.5). Then \(f=\sum a_nq^n\) is holomorphic modular of weight \(k\) on \(\Gamma_0(N)\), with \(f\Vert_kW_N=\epsilon f\). If additionally \(\sum|a_n|n^{-(k-\delta)}<\infty\) for some \(\delta>0\), it is cuspidal.

This is Weil, “Über die Bestimmung Dirichletscher Reihen durch Funktionalgleichungen,” Satz 2. The stated prime-family property is stronger than his formulation allowing conductor four as well. No Euler product is among these hypotheses. The extra convergence condition must be retained when drawing the cuspidal conclusion. [Original article in the Göttingen archive, printed pages 149–156](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0168/PPN235181684_0168.pdf).

**Proof.** We first recover the paired Fricke equations analytically, before assuming any modularity. If two polynomially bounded coefficient sequences have entire completions at a positive integer scale \(Q\), bounded in strips, and
\[
\Lambda_Q(A,s)=i^kK\Lambda_Q(B,k-s),
\]
then
\[
A\Vert_kW_Q=KB.
\tag{5.1}
\]
Here \(A,B\) denote their Fourier series and \(K\ne0\). To prove this, put \(G_A(t)=A(it/\sqrt Q)\), and similarly for \(B\). Their Mellin transforms are the stated completions on a line \(b\) larger than both coefficient exponents plus one and than \(k\). The three weighted derivative conditions in lesson 11, Lemma 8.1, follow exactly as in (4.4), so both Mellin inversions are absolutely convergent there. Euler's integral and integration by parts, as in the proof of (4.5), give decay to every polynomial order on this line; the paired equation gives the same decay on \(a=k-b\). Apply the strip argument of Theorem 4.1 to \((s+R)^4\Lambda_Q(A,s)\), choosing \(R>1-a\). There are no poles, and the assumed boundedness in strips implies finite order after multiplication by this polynomial. It gives uniform \(O((1+|t|)^{-4})\) decay throughout the strip. The contour shift therefore has no residues and gives
\[
G_A(t)=i^kK t^{-k}G_B(1/t).
\]
Substitution of \(1/t\) for \(t\) and the definition of the slash at \(it/\sqrt Q\) yield (5.1) there. The identity theorem extends it to the upper half-plane. Thus the untwisted equation gives \(f\Vert_kW_N=\epsilon f\), and the assumed twist equations give (2.4), without using its forward modularity proof.

Write \(T(u)=\begin{pmatrix}1&u\\0&1\end{pmatrix}\). Extend the slash linearly to finite formal linear combinations of matrices; every equality below is an equality of holomorphic functions after applying it to \(f\). For an odd prime \(m\in\mathcal P\) and each unit residue \(b\bmod m\), choose integers \(a,n\) with
\[
\begin{gathered}
mn-Nab=1,\\
\gamma_b=\begin{pmatrix}m&-b\\-Na&n\end{pmatrix}.
\end{gathered}
\tag{5.2}
\]
Such \(a\) exists since \((Nb,m)=1\); then \(n=(1+Nab)/m\). Direct multiplication proves
\[
\begin{gathered}
T(a/m)W_{Nm^2}\\
=mW_N\gamma_bT(b/m).
\end{gathered}
\tag{5.3}
\]
The right side has entries \(Nam,-1,Nm^2,0\), in row order. Thus the scalar \(m\) acts trivially. For any nonprincipal character \(\psi\bmod m\), the averaging formula (2.2) and the paired Fricke equation just proved imply
\[
\begin{aligned}
0&=\sum_{b\bmod m}^{*}\Bigl[\psi(b)\\
&\quad\cdot\bigl(f\Vert_k(1-\gamma_b)T(b/m)\bigr)\Bigr].
\end{aligned}
\tag{5.4}
\]
Indeed \(a\equiv-(Nb)^{-1}\pmod m\), so
\(\overline\psi(a)=\psi(-N)\psi(b)\). Inserting (5.3) into the left side of (2.4), its prefactor is \(\epsilon\psi(-N)/\tau(\overline\psi)\). The prefactor on its right, after expressing \(f_{\overline\psi}\) by its average, is \(\epsilon\psi(N)\tau(\psi)/m\). Their ratio is one, because \(\tau(\psi)\tau(\overline\psi)=\psi(-1)m\). This proves (5.4) with its sign and normalization.

Character orthogonality now says that
\[
\begin{gathered}
f\Vert_k(1-\gamma_b)T(b/m)\\
\text{is independent of }b.
\end{gathered}
\tag{5.5}
\]
Here is the finite algebra needed for that conclusion. The nonzero residues modulo a prime form a cyclic group: in a finite subgroup of the multiplicative group of a field, choose elements realizing the largest prime-power parts of the element orders; their commuting product has the least common multiple \(h\) of all orders. Every group element is a root of \(X^h-1\), so the root bound for a polynomial gives the group size at most \(h\). Since an element of order \(h\) gives the reverse inequality, it generates the group. For a generator of a cyclic group of size \(m-1\), its characters are the powers of \(e^{2\pi i/(m-1)}\). Summing a geometric series proves their orthogonality. Fourier inversion on this finite list shows that vanishing of all nonconstant character sums leaves only a constant function. Apply this pointwise to the holomorphic functions in (5.4). Every nonprincipal character modulo a prime is primitive: its only proper conductor divisor is one. Thus precisely the necessary character sums are among the hypotheses.

Next suppose \(m,n\in\mathcal P\) and \(mn-Nab=1\). Put
\[
\gamma=\begin{pmatrix}m&-b\\-Na&n\end{pmatrix},\qquad
\gamma'=\begin{pmatrix}m&b\\Na&n\end{pmatrix}.
\]
At conductor \(m\), (5.5) applied to \(b,-b\) gives
\[
\begin{gathered}
f\Vert_k(1-\gamma')\\
=f\Vert_k(1-\gamma)T(2b/m).
\end{gathered}
\tag{5.6}
\]
The corresponding matrices at conductor \(n\) are \(\gamma^{-1},(\gamma')^{-1}\), with unit residues \(-b,b\). The same equality there, multiplied on the right by \(-\gamma'\), gives
\[
\begin{gathered}
f\Vert_k(1-\gamma')\\
=f\Vert_k(1-\gamma)\gamma^{-1}T(-2b/n)\gamma'.
\end{gathered}
\tag{5.7}
\]
Right multiplication preserves any equality already obtained after slashing by \(f\). Comparing (5.6)–(5.7) therefore shows that \(H=f\Vert_k(1-\gamma)\) satisfies \(H\Vert_k\mu=H\), where
\[
\begin{gathered}
\mu=\gamma^{-1}T(-2b/n)\gamma'T(-2b/m),\\
\mu=\begin{pmatrix}1&-2b/m\\2Na/n&4/(mn)-3\end{pmatrix}.
\end{gathered}
\tag{5.8}
\]
The determinant is one and its trace is \(4/(mn)-2\). Since \(m,n\) are odd primes, \(mn\ge9\); this trace lies strictly between \(-2\) and \(2\), and is a noninteger rational number. Hence \(\mu\) is elliptic and has infinite order. For completeness, if its eigenvalues were roots of unity, their sum would be an algebraic integer. A rational algebraic integer is an integer: substituting a reduced fraction into a monic integer polynomial forces its denominator to divide a power of its numerator. This contradicts the computed trace.

We prove the analytic consequence rather than invoking an elliptic-invariance lemma. Conjugate its fixed point in the upper half-plane to \(i\) by a real determinant-one matrix. The conjugated elliptic matrix is
\(R_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix}\), with \(\theta/\pi\) irrational. In disk coordinates \(w=(z-i)/(z+i)\), let
\[
h(w)=(1-w)^{-k}\widetilde H\bigl(i(1+w)/(1-w)\bigr),
\]
where \(\widetilde H\) is the conjugated slash of \(H\). A direct substitution gives \(w\mapsto e^{2i\theta}w\) and, from \(\widetilde H\Vert_kR_\theta=\widetilde H\),
\[
h(e^{2i\theta}w)=e^{-ik\theta}h(w).
\]
Writing its convergent Taylor series at zero, a nonzero coefficient of degree \(j\ge0\) would require \(e^{i(2j+k)\theta}=1\). This is impossible since \(k>0\) is integral and \(\theta/\pi\) is irrational. Every coefficient is zero; the identity theorem gives \(H=0\). We have proved
\[
f\Vert_k\gamma=f
\quad(m,n\in\mathcal P).
\tag{5.9}
\]

We now recover every matrix of \(\Gamma_0(N)\). Period one gives invariance under \(T(1)\). Together with Fricke invariance it gives invariance under
\(L(Nu)=\begin{pmatrix}1&0\\Nu&1\end{pmatrix}=W_NT(-u)W_N^{-1}\) for every integer \(u\). Let
\(g=\begin{pmatrix}a&b\\Nc&d\end{pmatrix}\in\Gamma_0(N)\), with \(b\ne0\). Its determinant shows \((a,Nb)=(d,Nb)=1\). The assumed progression property supplies
\[
m=a+Nbs\in\mathcal P,\qquad
n=d+Nbt\in\mathcal P
\]
for some integers \(s,t\). Use modulus \(|Nb|\), so this also covers negative \(b\). Define
\[
\begin{gathered}
c'=\frac{mn-1}{Nb}=c+mt+ns-Nbst,\\
g'=\begin{pmatrix}m&b\\Nc'&n\end{pmatrix}.
\end{gathered}
\]
All entries are integral and the determinant is one. Equation (5.9), with its \(a,b\) replaced by \(-c',-b\), proves invariance under \(g'\). Exact multiplication gives
\[
g=L(-Nt)g'L(-Ns).
\tag{5.10}
\]
Thus \(f\Vert_kg=f\). If \(b=0\), the determinant forces \(a=d=1\) or \(-1\); the matrix is a lower unipotent times possibly \(-I\). The former already fixes \(f\), and the latter does too because \(k\) is even. This proves the entire transformation law, without a generating-set assertion or a Dirichlet theorem: the progression property is an explicit hypothesis.

It remains to prove the cusp statements. Enlarge the coefficient exponent to a nonnegative integer \(C\), retaining \(|a_n|\le An^C\) for a suitable constant \(A\). The polynomial coefficient estimate gives \(|f(x+iy)|=O(y^{-C-1})\), uniformly in \(x\), as in Theorem 4.1. For an integral cusp matrix \(\sigma\), its slash therefore has polynomial growth as \(y\to\infty\), uniformly on a bounded horizontal interval. The transformation law just established makes that slash periodic with its positive cusp width. A negative Fourier coefficient is zero by integrating over a period at height \(y\): its absolute value is bounded by a polynomial times an exponentially decreasing factor as \(y\to\infty\). There are consequently no negative terms, so the function is holomorphic at every cusp.

Under the extra convergence hypothesis, reduce \(\delta\), if necessary, so that \(0<\delta<k\). Put \(S_j=\sum_{n\le j}|a_n|\). Then
\(S_j\le j^{k-\delta}\sum_{n\ge1}|a_n|n^{-k+\delta}\).
For \(0<x<1\), absolute rearrangement of nonnegative sums gives
\[
\sum_{n\ge1}|a_n|x^n=(1-x)\sum_{j\ge1}S_jx^j.
\]
An integral comparison for \(\sum j^{k-\delta}e^{-2\pi jy}\) now gives \(f(x+iy)=O(y^{-k+\delta})\), uniformly in \(x\). In a cusp coordinate with nonzero lower left matrix entry, \(\operatorname{Im}(\sigma z)\) is comparable to \(1/y\) and the slash denominator to \(y^k\), uniformly over a bounded interval. Hence \(f\Vert_k\sigma=O(y^{-\delta})\to0\). If the lower left entry is zero, its original zero constant term gives exponential decay. Every cusp constant therefore vanishes, proving cuspidality. \(\square\)

This proof uses the freely available original article of Weil, Lemmas 1–5 and Satz 2, as mathematical background. The Mellin shifts, finite character argument, matrix identities, infinite-order elliptic step and cusp conclusion have all been supplied above. The broader adelic converse discussed in Getz–Hahn, Section 11.9, is an outlook and supplies no theorem used here.


## 6. Exercises

1. **Easy.** At weight two, show that the root number is \(-\epsilon\). Determine what \(\epsilon=+1\) forces at \(s=1\), and whether \(\epsilon=-1\) proves nonvanishing.
2. **Medium.** Reconstruct the coefficientwise twist, its nebentypus and its Fricke constant from the matrices \(A_u\). Determine the containing level. Explain why an exact least-level conclusion needs more information, using \(f(z)=\Delta(2z)\) declared at level four and the character \(\psi_3\).
3. **Medium, computational.** Use the twenty coefficients in Section 3 to check the level eleven functional equation numerically. First compare the two reciprocal Fricke values independently, with a Fourier tail bound. Then derive the split-integral approximate functional equation and evaluate the completion at \(1/2,1,3/2\), and \(L(f,1)\). Identify which numerical symmetry is built into that formula.
4. **Hard.** Put \(\vartheta(z)=\sum_{m\in\mathbb Z}e^{\pi im^2z}\), and let \(r_2(n)\) count ordered signed integer pairs of norm \(n\). Prove \(\sum r_2(n)n^{-s}=4\zeta(s)L(s,\chi_{-4})\) on its absolute domain. Using Hecke's correspondence with period two, show how its completed functional equation, poles and growth condition imply the inversion of \(\vartheta^2\), and prove the reverse implication. Track the weight-one multiplier and the constant term.

## 7. Full solutions

### Solution 1

At \(k=2\), \(i^k=-1\), so (1.2) has root number \(w=-\epsilon\). If \(\epsilon=+1\), evaluation at one gives \(\Lambda_N(f,1)=-\Lambda_N(f,1)\), hence zero. Since
\[
\Lambda_N(f,1)=\frac{\sqrt N}{2\pi}L(f,1),
\]
the L-value is zero too. If \(\epsilon=-1\), the equation at one is an identity and supplies no nonvanishing conclusion. Establishing nonvanishing requires additional information, as in the computation below for level eleven.

### Solution 2

Start with the primitive finite Fourier sum in Lemma 2.1, applied to \(\overline\psi\). Dividing it by \(\tau(\overline\psi)\) gives the multiplier \(\psi(n)\) on the \(n\)-th coefficient, including zero for nonunits. Thus (2.2) is the requested coefficient twist.

For \(\gamma\in\Gamma_0(Nr^2)\), (2.6) factors \(A_u\gamma\) into an element of \(\Gamma_0(N)\) followed by \(A_v\), with \(v\equiv ud^2\). Reindexing the average changes its character weight by \(\psi(d)^2\), proving its nebentypus. The rational affine cusp argument in Theorem 2.2 proves vanishing at every cusp, not only infinity. Hence the guaranteed level is \(Nr^2\).

For Fricke choose \(v\equiv-(Nu)^{-1}\) and \(a=(1+uNv)/r\). The determinant \(ar-uNv=1\) and the identity (2.7) give, term by term,
\[
(f\Vert_kA_u)\Vert_kW_{Nr^2}=\epsilon f\Vert_kA_v.
\]
The character weight becomes \(\psi(-1)\psi(N)\psi(v)\); summing over \(v\) contributes \(\tau(\psi)f_{\overline\psi}\). Division by the original \(\tau(\overline\psi)\) and
\(\tau(\psi)\tau(\overline\psi)=\psi(-1)r\) give exactly
\(\epsilon\psi(N)\tau(\psi)^2/r\). This reconstructs all parts of the twisting identity.

To see why the level bound can be strict, take \(f(z)=\Delta(2z)\). Dilation gives \(f\in S_{12}(\Gamma_0(2))\), hence also at the declared level four. The level-one inversion of \(\Delta\) gives
\[
(f\Vert_{12}W_4)(z)
=4^{-6}z^{-12}\Delta(-1/(2z))
=2^{-12}z^{-12}(2z)^{12}\Delta(2z)=f(z).
\]
So even the Fricke eigenvector hypothesis holds at the declared level. The twist has
\[
f_{\psi_3}(z)=\psi_3(2)\Delta_{\psi_3}(2z)
=-\Delta_{\psi_3}(2z).
\]
Theorem 2.2 applied to \(\Delta\) gives containing level nine for \(\Delta_{\psi_3}\); dilation by two then gives level eighteen for \(f_{\psi_3}\). This is smaller than the nominal bound \(4\cdot3^2=36\). Thus no universal equality with the least level follows from the averaging argument. Determining the conductor of a primitive newform twist is an additional local theorem.

### Solution 3

Put \(b=2\pi/\sqrt{11}\), \(\rho=e^{-b}\), and
\[
G_{20}(t)=\sum_{n=1}^{20}a_ne^{-bnt}.
\]
We first test (1.3) directly, evaluating \(G_{20}(1/t)\) and \(t^2G_{20}(t)\) as separate sums. The theoretical equation here is \(G(1/t)=t^2G(t)\).

We obtain a tail bound directly from the product in (3.1). It requires no optimal Hecke eigenvalue estimate. Choose \(r=e^{-b/2}\), and put
\[
M=r\exp\left(\frac{2r}{1-r}+\frac{2r^{11}}{1-r^{11}}\right).
\tag{7.1}
\]
For each finite product, the triangle inequality bounds the absolute value of each coefficient by the corresponding coefficient of
\(q\prod(1+q^m)^2(1+q^{11m})^2\).
These latter coefficients are nonnegative, and a coefficient of fixed degree stabilizes after finitely many factors. Evaluating at \(r\), their total sum is at most \(M\): use \(1+u\le e^u\), which follows from the nonnegative exponential series, and sum the two geometric series in \(r^m\) and \(r^{11m}\). Taking increasing finite products proves
\[
\sum_{n\ge1}|a_n|r^n\le M,
\qquad |a_n|\le Mr^{-n}.
\]
Thus for \(t>1/2\), with \(x=e^{-bt}/r<1\),
\[
\begin{gathered}
R_{20}(t)=M\frac{x^{21}}{1-x},\\
R_{20}(t)\ge |G(t)-G_{20}(t)|.
\end{gathered}
\tag{7.2}
\]
This deliberately elementary estimate is sufficient for the numerical checks below.

Consequently the allowable Fourier truncation discrepancy in the reciprocal test is
\(R_{20}(1/t)+t^2R_{20}(t)\).

| \(t\) | \(G_{20}(1/t)\) | \(t^2G_{20}(t)\) |
|---:|---:|---:|
| 0.8 | 0.07545744510502054 | 0.07545744510500609 |
| 1.25 | 0.11790225797657202 | 0.11790225797659460 |

The respective differences are approximately \(1.44513\cdot10^{-14}\) and \(-2.25802\cdot10^{-14}\). Formula (7.2) gives the respective upper bounds \(1.333\cdot10^{-5}\) and \(2.083\cdot10^{-5}\). Each discrepancy is comfortably inside its allowance. These independently evaluated sums test the coefficient data and the positive sign. Agreement to finite precision remains a numerical check; Theorem 1.1 supplies the proof of the functional equation.

Next (1.5) gives the exact split-integral formula
\[
\begin{aligned}
\Lambda_{11}(f,s)&=A(s)+A(2-s),\\
A(s)&=\sum_{n\ge1}a_n(bn)^{-s}\Gamma(s,bn),\\
\Gamma(s,x)&=\int_x^\infty e^{-u}u^{s-1}\,du.
\end{aligned}
\tag{7.3}
\]
The sum–integral interchange is absolute for every fixed \(s\): on \(u\ge1\), bound \(u^{\operatorname{Re}s-1}\) by a fixed nonnegative power, sum \(Mr^{-n}e^{-bnu}\), and use \(r=e^{-b/2}\) and \(u\ge1\) to obtain exponential decay in both indices. Truncating the sum at twenty defines
\(\Lambda_{20}(s)=A_{20}(s)+A_{20}(2-s)\).

For these particular arguments, the integrals reduce to
\[
\Gamma(1,x)=e^{-x},\qquad
\Gamma(1/2,x)=\sqrt\pi\,\operatorname{erfc}(\sqrt x),\qquad
\Gamma(3/2,x)=\tfrac12\Gamma(1/2,x)+\sqrt x\,e^{-x}.
\tag{7.4}
\]
Here \(\operatorname{erfc}(v)=(2/\sqrt\pi)\int_v^\infty e^{-u^2}\,du\); substitution proves the middle identity, and integration by parts proves the last one. Evaluation yields
\[
\begin{aligned}
\Lambda_{20}(1/2)=\Lambda_{20}(3/2)&\approx0.1383305788,\\
\Lambda_{20}(1)&\approx0.1339922615,\\
L_{20}(f,1)=b\Lambda_{20}(1)&\approx0.2538418609.
\end{aligned}
\tag{7.5}
\]
Put \(x_0=e^{-b}/r=e^{-b/2}\). For \(s=1/2,3/2\), the discarded completed integral is bounded by
\[
\begin{gathered}
I_n=\int_1^\infty e^{-bnu}(u^{-1/2}+u^{1/2})\,du,\\
\sum_{n\ge21}Mr^{-n}I_n\\
\le 2M\sum_{n\ge21}x_0^n
\left(\frac1{bn}+\frac1{b^2n^2}\right)\\
\le\frac{2Mx_0^{21}}{21b(1-x_0)}
\left(1+\frac1{21b}\right)\\
<2.663\cdot10^{-10}.
\end{gathered}
\tag{7.6}
\]
The first inequality uses \(u^{-1/2}+u^{1/2}\le2u\), then evaluates \(\int_1^\infty ue^{-bnu}\,du\) by integration by parts. The next uses \(n\ge21\) and sums a geometric series. At the centre, the discarded **L-value** satisfies
\[
\begin{gathered}
|L(f,1)-L_{20}(f,1)|\\
\le 2M\sum_{n\ge21}\frac{x_0^n}{n}\\
\le\frac{2M}{21}\frac{x_0^{21}}{1-x_0}\\
<4.920\cdot10^{-10}.
\end{gathered}
\tag{7.7}
\]
Here the factor \(b\) converting the completion to the L-value cancels the \(1/b\) from each integral. Nonvanishing has a direct proof too. For \(y>0\), every factor of the product (3.1) at \(q=e^{-2\pi y}\) is positive, and their product is nonzero: after finitely many factors, \(q^m<1/2\), and \(-\log(1-q^m)\le2q^m\), whose sum converges. Thus \(G(t)>0\). Formula (1.5) at the centre gives \(\Lambda_{11}(f,1)=2\int_1^\infty G(t)\,dt>0\), hence \(L(f,1)>0\). The finite-sum decimals are reproducible approximations; a certified decimal enclosure would also require a rounding calculation.

These are analytic truncation bounds. The displayed decimal rounding and ordinary floating-point evaluation have their own errors; (7.6)–(7.7) alone do not certify them. For reproducibility, this Python calculation uses the exact coefficient recursion followed by ordinary double-precision evaluation:

~~~python
import math

bcoef = [1]
for j in range(1, 20):
    total = 0
    for h in range(1, j + 1):
        sigma = sum(d for d in range(1, h + 1) if h % d == 0)
        if h % 11 == 0:
            v = h // 11
            sigma += 11 * sum(d for d in range(1, v + 1) if v % d == 0)
        total += sigma * bcoef[j - h]
    assert (-2 * total) % j == 0
    bcoef.append((-2 * total) // j)
a = bcoef
b = 2 * math.pi / math.sqrt(11)

def G(t):
    return math.fsum(an * math.exp(-b * n * t)
                     for n, an in enumerate(a, 1))

r = math.exp(-b / 2)
M = r * math.exp(2*r/(1-r) + 2*r**11/(1-r**11))

def tail(t):
    x = math.exp(-b * t) / r
    assert x < 1
    return M * x**21 / (1-x)

for t in (0.8, 1.25):
    print(t, G(1 / t), t*t*G(t), tail(1 / t) + t*t*tail(t))

Ahalf, Aone, Athreehalf = [], [], []
for n, an in enumerate(a, 1):
    x = b * n
    gh = math.sqrt(math.pi) * math.erfc(math.sqrt(x))
    g3 = gh / 2 + math.sqrt(x) * math.exp(-x)
    Ahalf.append(an * gh / math.sqrt(x))
    Aone.append(an * math.exp(-x) / x)
    Athreehalf.append(an * g3 / x**1.5)
lamhalf = math.fsum(Ahalf + Athreehalf)
lamone = 2 * math.fsum(Aone)
print(lamhalf, lamone, lamhalf, b * lamone)
~~~

The equality \(\Lambda_{20}(1/2)=\Lambda_{20}(3/2)\) follows from its symmetric definition, regardless of the supplied coefficients. It therefore cannot by itself validate them. The separate reciprocal-point calculation is the useful numerical test. The approximate functional equation is then an efficient way to compute L-values with a very small analytically bounded tail.

### Solution 4

Let \(\chi_{-4}\) be zero on even integers, one on \(1\pmod4\) and minus one on \(3\pmod4\). It is primitive of conductor four: the units one and three have different character values but identical reductions modulo two. Write \(\beta(s)=L(s,\chi_{-4})\).

**The coefficient identity.** We first prove
\[
r_2(n)=4\sum_{d\mid n}\chi_{-4}(d).
\tag{7.8}
\]
The ring \(\mathbb Z[i]\) is Euclidean for \(\operatorname{Nm}(a+ib)=a^2+b^2\): round both coordinates of a quotient to integers, leaving a remainder of norm at most half the divisor's norm. The Euclidean algorithm supplies a greatest common divisor and a Bézout identity. If an irreducible \(\pi\) does not divide \(x\), its gcd with \(x\) is one, so Bézout shows that \(\pi\mid xy\) implies \(\pi\mid y\). Thus irreducibles are prime. Induction on the norm gives existence of factorization, and successive cancellation of primes gives uniqueness up to the four units \(1,-1,i,-i\).

Here is the rational prime factorization needed for the count. Two ramifies as \(2=-i(1+i)^2\). If \(p\equiv3\pmod4\) had a nontrivial Gaussian factorization, one factor would have norm \(p\), so \(p=a^2+b^2\). Neither coordinate could be zero modulo \(p\); their quotient would give a square root of minus one modulo \(p\). But multiplying all nonzero residues by a unit \(x\) permutes them, so cancellation of their product gives \(x^{p-1}=1\). A square root of minus one would instead give \(x^{p-1}=(-1)^{(p-1)/2}=-1\), a contradiction. Thus these primes remain irreducible.

If \(p\equiv1\pmod4\), pair each nonzero residue with its inverse. Only \(1,-1\) pair with themselves, so \((p-1)!\equiv-1\pmod p\). Pairing its lower and upper halves also gives
\[
(p-1)!\equiv(-1)^{(p-1)/2}\left(((p-1)/2)!\right)^2\pmod p.
\]
The sign is positive, producing a square root \(x\) of minus one. The Gaussian gcd \(d=(p,x+i)\) is a nonunit: otherwise a Bézout identity would make \(x+i\) invertible modulo \(p\), although its product with the nonzero element \(x-i\) is zero there. It is not associated to \(p\), since \(p\) cannot divide the imaginary coordinate one of \(x+i\). Its norm is a proper nontrivial divisor of \(p^2\), hence \(p\). Therefore \(p=d\overline d\), and \(d,\overline d\) are nonassociate primes. If they were associated, their coordinates would force one to be zero or their absolute values to be equal; \(p\) would be a square or twice a square, impossible for odd \(p\). Every Gaussian prime belongs to this list: it divides its integer norm, hence by primeness divides some rational prime factor, and is associated to one of the listed Gaussian factors of that prime.

For \(n=\prod_pp^{e_p}\), a Gaussian integer of norm \(n\) has a uniquely determined exponent \(e_2\) at \(1+i\), and exponent \(e_p/2\) at each inert prime. It exists only when every exponent at \(p\equiv3\pmod4\) is even. At each split prime \(p\equiv1\pmod4\), it can distribute the total exponent \(e_p\) between its two conjugate factors in \(e_p+1\) ways. Multiplication by the four units gives
\[
r_2(n)=\begin{cases}
4\displaystyle\prod_{p\equiv1(4)}(e_p+1),& e_p\text{ even for every }p\equiv3(4),\\
0,&\text{otherwise}.
\end{cases}
\]
On the other hand, the divisor sum of \(\chi_{-4}\) is multiplicative. Its local factors are one at two, \(e+1\) at a split prime and \(1-1+\cdots+(-1)^e\) at an inert prime. These agree with the count and prove (7.8).

For \(\sigma>1\), the convolution is absolutely summable because
\(\sum_{m,d\ge1}|\chi_{-4}(d)|(md)^{-\sigma}\le\zeta(\sigma)^2<\infty\). Consequently
\[
D(s)=\sum_{n\ge1}r_2(n)n^{-s}=4\zeta(s)\beta(s).
\tag{7.9}
\]
Also \(r_2(n)\le4d(n)\le8\sqrt n\), giving the polynomial bound needed in Theorem 4.1. The normally convergent double theta series has the expansion
\[
F(z)=\vartheta(z)^2=1+\sum_{n\ge1}r_2(n)e^{\pi inz},\qquad F(z+2)=F(z).
\tag{7.10}
\]
The coefficient one is the single pair \((0,0)\); the nonzero coefficients count all ordered signed pairs, so no factor of two is lost.

**The completed equation and poles.** Use the written continuation proofs in Poisson summation, theta, and the functional equation, Theorem 3.1, and The functional equation of Dirichlet L-functions, Theorem 2.1. For the latter, Lemma 2.1a above supplies its character-Poisson step, and conductor four has parity one. In the present conventions these proofs give
\[
Z(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=Z(1-s),
\]
with simple residues \(-1,+1\) at \(0,1\), and
\[
B(s)=(4/\pi)^{(s+1)/2}\Gamma((s+1)/2)\beta(s)=B(1-s),
\]
which is entire. The character has \(\tau(\chi_{-4})=i-(-i)=2i\), so its odd-character root number \(\tau/(i\sqrt4)\) is one. The raw reflection formula needed in the growth estimate follows from this completed equation and the Gamma reflection and duplication proved in the Gamma lesson. For instance the odd raw equation simplifies to
\[
\beta(s)=(2/\pi)^{1-s}\Gamma(1-s)\cos(\pi s/2)\beta(1-s).
\tag{7.11}
\]
The possible negative odd Gamma poles in \(B\) are cancelled by the zeros of \(\beta\); the negative even poles in \(Z\) are cancelled by the zeta zeros. Those zeros also follow by substituting the relevant integers in the raw reflection formulas.

Gamma duplication gives
\[
Z(s)B(s)=4\pi^{-s}\Gamma(s)\zeta(s)\beta(s)=\Phi(s),
\tag{7.12}
\]
which is exactly the completion in (4.1) for \(\lambda=2\), \(D=4\zeta\beta\). Moreover \(\beta(1)=1-1/3+1/5-\cdots=\pi/4\): integrate the finite geometric expansion of \(1/(1+x^2)\) on \([0,1]\), whose remainder has integral at most \(1/(2m+3)\), then use \(\arctan(1)=\pi/4\). Thus \(B(1)=1\) and, by reflection, \(B(0)=1\). Formula (7.12) has precisely the simple poles \(0,1\), with residues \(-1,+1\), and satisfies
\[
\Phi(s)=\Phi(1-s).
\tag{7.13}
\]
They correspond to \(k=1\), \(\gamma=1\) and \(a_0=1\), including the nonzero constant term.

**Checking growth rather than assuming it.** Put
\(A_\chi(x)=\sum_{n\le x}\chi_{-4}(n)\), which is bounded. Partial summation gives, first on \(\sigma>1\) and then by continuation to \(\sigma>0\),
\[
\beta(s)=s\int_1^\infty A_\chi(x)x^{-s-1}\,dx,
\qquad
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\tag{7.14}
\]
These follow respectively by integrating the step sums \(A_\chi\) and \(\lfloor x\rfloor=x-\{x\}\); their boundary terms vanish on the initial domain. The new integrals converge locally uniformly for \(\sigma>0\). On a fixed strip with \(\sigma\ge1/2\), \(|t|\ge1\), they bound \(\zeta(s),\beta(s)\) by \(O(1+|t|)\). On its part with \(\sigma\le1/2\), the raw reflection formulas express them in terms of the functions at \(1-s\), where those estimates apply. Euler's integral bounds \(|\Gamma(1-s)|\le\Gamma(1-\sigma)\), uniformly on this fixed strip, while the sine and cosine factors are at most \(O(e^{\pi|t|/2})\). Hence both functions have at most polynomial times exponential growth throughout the strip.

Choose an integer \(m\ge0\) with \(\sigma+m>0\) throughout it. The recurrence
\[
\Gamma(s)=\frac{\Gamma(s+m)}{s(s+1)\cdots(s+m-1)}
\]
and Euler's integral bound its modulus by \(O(|t|^{-m})\) for \(|t|\ge1\), with the empty product understood when \(m=0\). The real scale \(\pi^{-s}\) has bounded modulus there. Therefore \(s(s-1)\Phi(s)\) has at most a polynomial times \(e^{\pi|t|}\) growth. It is entire by the pole analysis, so it satisfies the exact finite-order condition in Theorem 4.1, including the bounded portion of each strip.

**The two directions.** All hypotheses of Theorem 4.1 now hold for the coefficients in (7.10), with \(\lambda=2,k=1,\gamma=1\). Its converse gives
\[
\vartheta(-1/z)^2=(z/i)\vartheta(z)^2=-iz\vartheta(z)^2.
\tag{7.15}
\]
In weight-one slash notation this is \(F|_1S=-iF\), while \(F|_1T^2=F\). It is a multiplier for the group generated by \(S,T^2\), rather than trivial-character modularity at odd weight for the full modular group.

Conversely, suppose (7.15) holds for the theta series. The already proved coefficient identity, polynomial bound and period two allow the forward half of Theorem 4.1. It yields
\[
\Phi(s)=A(s)+A(1-s)+\frac1{s-1}-\frac1s,
\qquad A(s)=\int_1^\infty(F(iy)-1)y^{s-1}\,dy,
\]
proving the continuation, both exact residues, finite-order growth and (7.13). Thus the theta inversion and the specified analytic package are equivalent. An isolated formal functional equation, without the pole and growth information, is not the hypothesis of the converse.

## What this lesson does not prove

* The cusp coefficient estimate and Hecke coefficient relations: lesson 7, Theorem 2.1; lesson 9, Theorems 2.3 and 3.1. The complete level eleven modularity and dimension computation is lesson 9, Section 6; its squared eta transformation uses the explicitly stated eta input there. Dilation and Fricke normalization are also developed in lesson 10, Sections 1–2.
* The numerical tail bound is proved directly from the product in Solution 3, equations (7.1)–(7.2). It does not use the optimal Ramanujan–Petersson estimate. That result and its remaining geometric proof obligations are tracked in lesson 11, Section 5.
* Euler's Gamma integral, meromorphic continuation and recurrence are proved in The Gamma function and Stirling's formula, Theorems 1.1–1.2; its Theorems 2.2–2.3 prove reflection and duplication. The L-function of a cusp form, Lemma 8.1, proves smooth Mellin inversion; Theorem 4.1 above verifies its three weighted conditions. The smooth inversion and finite-order strip argument are proved in the named lesson and Theorem 4.1 above.
* Classical zeta continuation, its sole pole of residue one and reflection are proved in Poisson summation, theta, and the functional equation, Theorem 3.1 and Corollary 3.2. Primitive Dirichlet L-function continuation and completed reflection have full written Mellin proofs in The functional equation of Dirichlet L-functions, Theorem 2.1; its Solution 2 derives the raw reflection formula. Lemma 2.1a above supplies that proof's character-Poisson step from the ordinary Poisson theorem and Gaussian transform in the zeta lesson, Theorem 1.2 and Lemma 2.1. The finite primitive Gauss identities are proved in Lemma 2.1 here and in Gauss sums, Theorems 1.1 and 2.1. Solution 4 computes the conductor-four phase directly. [DLMF (25.15.5)](https://dlmf.nist.gov/25.15.E5) records the corresponding raw normalization.
* The identity theorem, rectangle residue formula, maximum modulus principle and disk power series used above are proved in lesson 11, Lemma 8.0. The finite-order strip argument is proved in Theorem 4.1. The continuous sum–integral interchanges use the proof in lesson 01, Lemma 0.3, with the explicit majorants supplied here.
* Weil's classical converse, including its cusp qualification: Weil (1967), Satz 2. Theorem 5.1 proves the specified specialization, including the paired Mellin inversion, finite character orthogonality, infinite-order elliptic step, and cusp qualification. Exact local conductor and primitive newform twist assertions beyond (2.3)–(2.5) are not used.

## References

* J. S. Milne, *Modular Functions and Modular Forms*, author lecture notes, version 1.31 (2017), Section 9, especially Theorems 9.2–9.3. [Free author text](https://www.jmilne.org/math/CourseNotes/MF.pdf). The local proofs include all Mellin and contour-shift steps used here.

* A. J. Best et al., *Computing classical modular forms*, [arXiv:2002.04717v4](https://arxiv.org/abs/2002.04717v4), May 2022, Section 9.1, equation (9.1.3), for the root-number convention and Section 11.1 for primitive versus coefficient twists. The raw good-prime Euler factor here retains \(p^{k-1}\), as proved in lesson 11.
* A. Weil, “Über die Bestimmung Dirichletscher Reihen durch Funktionalgleichungen,” *Mathematische Annalen* 168 (1967), 149–156, especially Lemmas 1 and 3 and Satz 2. [Freely accessible original article, Göttingen archive](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0168/PPN235181684_0168.pdf).
* J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations: With a View toward Trace Formulae*, April 2022 draft](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), Section 11.9 for the adelic outlook.
* P. Deligne, “La conjecture de Weil I,” *Publications Mathématiques de l'IHÉS* 43 (1974), 273–307, Theorem (8.2). [Free original article at NUMDAM](https://www.numdam.org/item/PMIHES_1974__43__273_0/).
* J. Lebl, *A Guide to Cultivating Complex Analysis*, version 1.9, Sections 2.4, 3.3 and 5.3. [Author text](https://www.jirka.org/ca/).
* D. H. Fremlin, *Measure Theory*, Volume 2, Section 252. [Author's volumes](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm).
* *NIST Digital Library of Mathematical Functions*, Sections 5.2, 5.5, 25.2, 25.4 and 25.15.

# Eisenstein series on GL₂(A) and the continuous spectrum

Cuspidal Fourier expansions have no constant term. An Eisenstein series starts with a prescribed constant term and acquires a second one when rational translates are summed. The operator producing that second term also produces the functional equation. Its pole gives the noncuspidal discrete spectrum; its values on the unitary axis supply the continuous spectrum.

We work over \(\mathbb Q\), with \(G=\mathrm{GL}_2\), its upper triangular subgroup \(B=TN\), and
\[
n(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix},\qquad
w=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
d(a)=\operatorname{diag}(a,1).
\tag{0.1}
\]
Use the additive character and self-dual measures of Lesson 14, equation (0.1): the real character is \(e^{2\pi ix}\), the finite character is \(e^{-2\pi i\{x\}_p}\), and \(\operatorname{vol}(\mathbb Q\backslash\mathbb A)=1\). Finite multiplicative units have volume one. The rational idèle class group is
\[
C=\mathbb Q^\times\backslash\mathbb A^\times
 \simeq\widehat{\mathbb Z}^{\times}\times\mathbb R_{>0},
\tag{0.2}
\]
with compact-factor probability measure and norm measure \(dr/r\). These are also the rational normalizations in Tate's global theory, equations (25)–(28). The finite-volume central quotient and its measure come from Lesson 1, Section 5; its volume is \(\pi/3\).

## 1. The parameter and the initial sum

Let \(\chi_1,\chi_2\) be unitary characters of \(C\). Put
\[
\eta=\chi_1\chi_2^{-1},\qquad \omega=\chi_1\chi_2,\qquad u=s+\tfrac12.
\tag{1.1}
\]
The normalized induced space \(I(\chi_1,\chi_2,s)\) consists of smooth functions satisfying
\[
f_s\left(\begin{pmatrix}a&b\\0&d\end{pmatrix}g\right)
 =\chi_1(a)\chi_2(d)|a/d|^{s+1/2}f_s(g).
\tag{1.2}
\]
At finite places smooth means locally constant; at infinity we initially take smooth, compact-group-finite vectors. A flat section has restriction \(F\) to
\(K=\mathrm O(2)\prod_p\mathrm{GL}_2(\mathbb Z_p)\) independent of \(s\). Iwasawa decomposition extends \(F\) by (1.2). The absolute value of the extra half-power is the square root of the modular character of \(B\); the unitary axis is \(\operatorname{Re}s=0\), as in Lesson 6, Section 1.

Each character is trivial on rational scalars. Thus \(f_s\) is left \(B(\mathbb Q)\)-invariant, and we can define
\[
E(g,f_s)=\sum_{\gamma\in B(\mathbb Q)\backslash G(\mathbb Q)}f_s(\gamma g).
\tag{1.3}
\]
It has central character \(\omega\). We will write \(E_s(g)\) for the section equal to one on \(K\) when both inducing characters are trivial.

**Theorem 1.1 — absolute convergence.** For every flat section, (1.3) converges absolutely and locally uniformly in \(g\) and \(s\) when \(\operatorname{Re}s>1/2\). It defines a holomorphic family there. The same assertion holds for its derivatives in the real group variables.

**Proof.** A left coset of \(B(\mathbb Q)\) is a rational line represented by the bottom row \((c,d)\) of \(\gamma\). Choose its primitive integer representative, unique up to sign. Let
\[
H_g(c,d)=\prod_v\|(c,d)g_v\|_v,
\tag{1.4}
\]
using Euclidean norm at infinity and maximum norm at a finite prime. In a local Iwasawa decomposition the bottom-row norm is the absolute value of the second diagonal entry; hence the product formula gives
\[
\left|\frac{a}{d}\right|_{\mathbb A}
 =\frac{|\det g|_{\mathbb A}}{H_g(c,d)^2}.
\tag{1.5}
\]
The determinant of the rational representative contributes global norm one. Since the inducing characters are unitary and \(F\) is bounded on compact \(K\), the summand is bounded by a constant times \(H_g(c,d)^{-2\operatorname{Re}s-1}\), with the determinant factor bounded on compact \(g\)-sets.

Outside a fixed finite set of primes, \(g_p\) and its inverse are integral, so the norm of a primitive row remains one. At each exceptional prime, the operator norms of \(g_p\) and \(g_p^{-1}\) bound its row norm above and below by positive constants. At infinity the least singular value of \(g_\infty\) gives a positive lower bound times \(\sqrt{c^2+d^2}\). These bounds are uniform on compact \(g\)-sets. Therefore a convergent majorant is
\[
C\sum_{(c,d)\in\mathbb Z^2\setminus\{0\}}
                (c^2+d^2)^{-\operatorname{Re}s-1/2}.
\tag{1.6}
\]
A dyadic annulus of radius \(R\) contains \(O(R^2)\) integer points. Its contribution is \(O(R^{1-2\operatorname{Re}s})\), summable precisely in the asserted half-plane. On a compact parameter set use its smallest real part. Parameter derivatives introduce powers of the logarithmic height, absorbed by a slight decrease of that real part. Real derivatives of an Iwasawa height or compact angular function on a compact \(g\)-set satisfy the same height bound, with constants depending on the derivative. Dominated differentiation proves all assertions. Rational invariance of the sum follows by permuting its cosets. \(\square\)

The classical parameter is \(u\), rather than \(s\): the first term at height \(y\) is \(y^u\). There is a further qualification concerning norm characters. Write
\[
\eta=\eta_0|\cdot|^{i\tau},\qquad
\eta_0|_{\mathbb R_{>0}}=1.
\tag{1.7}
\]
Replacing the base characters by
\(\chi'_1=\chi_1|\cdot|^{-i\tau/2}\) and
\(\chi'_2=\chi_2|\cdot|^{i\tau/2}\), and the parameter by
\(\sigma=s+i\tau/2\), leaves (1.2) unchanged. Below, a statement that a positive pole occurs only at \(s=1/2\) uses norm-normalized ratio \(\eta\). In the original parameter the possible pole is \(s=1/2-i\tau/2\).

## 2. Two Bruhat cells, two constant terms

Define
\[
E_N(g,f_s)=\int_{\mathbb Q\backslash\mathbb A}E(n(x)g,f_s)\,dx,
\qquad
(M(s)f_s)(g)=\int_{\mathbb A}f_s(wn(x)g)\,dx.
\tag{2.1}
\]
The latter is the unnormalized global intertwining integral; the induction itself remains normalized.

**Theorem 2.1 — constant term and exchanged data.** Initially for \(\operatorname{Re}s>1/2\),
\[
E_N(g,f_s)=f_s(g)+(M(s)f_s)(g),
\tag{2.2}
\]
and
\[
M(s):I(\chi_1,\chi_2,s)\longrightarrow
                    I(\chi_2,\chi_1,-s).
\tag{2.3}
\]

**Proof.** The rational Bruhat decomposition gives one coset from \(B(\mathbb Q)\), and open-cell cosets \(wn(q)\), \(q\in\mathbb Q\). The first term is unchanged by left \(N\). The remaining terms have integral
\[
\int_{\mathbb Q\backslash\mathbb A}
           \sum_{q\in\mathbb Q} f_s(wn(q+x)g)\,dx
       =\int_{\mathbb A}f_s(wn(x)g)\,dx.
\tag{2.4}
\]
Theorem 1.1 on a compact representative set of the additive quotient bounds the absolute integral of the sum. It therefore justifies the interchange and the unfolding, with no conditional integration. Additive volume one gives coefficient one for the first cell.

The output is left \(N\)-invariant by translation in \(x\). For a diagonal element,
\[
wn(x)\operatorname{diag}(a,d)
 =\operatorname{diag}(d,a)wn(xd/a).
\tag{2.5}
\]
Changing the variable has additive modulus \(|a/d|\). Combining it with (1.2) gives the multiplier
\(\chi_2(a)\chi_1(d)|a/d|^{1/2-s}\), proving (2.3). Right translation commutes with the integral. \(\square\)

For a pure tensor section, the intertwining integral factors into local ones in this half-plane. Absolute integration on finite restricted-product charts and the convergent product calculated next justify this factorization; it is not a formal interchange of infinitely many integrals.

**Proposition 2.2 — the spherical scalar.** At an unramified finite place of residue cardinality \(q\), let \(f^0_s(1)=1\) and \(A=\eta(\varpi)\). The local operator sends it to the normalized spherical vector for the exchanged data times
\[
c_q(s,\eta)=\frac{1-q^{-1}Aq^{-2s}}{1-Aq^{-2s}}
             =\frac{L_q(2s,\eta)}{L_q(1+2s,\eta)}.
\tag{2.6}
\]
For trivial real characters its scalar is
\[
c_\infty(s)=\sqrt\pi\frac{\Gamma(s)}{\Gamma(s+1/2)}
            =\frac{\Gamma_{\mathbb R}(2s)}{\Gamma_{\mathbb R}(1+2s)}.
\tag{2.7}
\]

**Proof.** For \(|x|\leq1\), \(wn(x)\) is integral and the section equals one. For \(|x|=q^m\), \(m\geq1\), its Iwasawa diagonals have valuations \(m,-m\). Thus its value is \(A^mq^{-m(2s+1)}\), and the shell's additive volume is \((1-q^{-1})q^m\). Consequently the integral is
\[
1+(1-q^{-1})\sum_{m\geq1}(Aq^{-2s})^m
 =\frac{1-q^{-1}Aq^{-2s}}{1-Aq^{-2s}},
\tag{2.8}
\]
initially for \(\operatorname{Re}s>0\). Right compact invariance and (2.3) identify the whole vector from its value at one. At infinity its value is the integral of \((1+x^2)^{-s-1/2}\). With \(t=x^2\), this is the beta integral \(B(1/2,s)\), giving (2.7). \(\square\)

Put
\[
\Lambda(z)=\Gamma_{\mathbb R}(z)\zeta(z),\qquad
c(s)=\frac{\Lambda(2s)}{\Lambda(1+2s)}.
\tag{2.9}
\]
Multiplying (2.6) and (2.7), absolutely for \(\operatorname{Re}s>1/2\), gives
\[
M(s)f_s^0=c(s)f_{-s}^0.
\tag{2.10}
\]
Every everywhere unramified Hecke character over \(\mathbb Q\) is a norm character: (0.2) and triviality on every finite unit leave only its positive real coordinate. Thus the general everywhere spherical case is a common determinant twist of (2.10), with parameter \(\sigma\) from (1.7). Its scalar is
\(\Lambda(2s+i\tau)/\Lambda(1+2s+i\tau)\), the completed Hecke-factor ratio. There is no nontrivial everywhere unramified Dirichlet character over \(\mathbb Q\).

## 3. Computing every spherical Fourier coefficient

Embed
\[
g_z=\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix}
       \in\mathrm{SL}_2(\mathbb R),\qquad z=x+iy,
\tag{3.1}
\]
with finite component one. Primitive bottom rows in Theorem 1.1 give
\[
E_s(g_z)=\frac12\sum_{\gcd(c,d)=1}
                      \frac{y^u}{|cz+d|^{2u}},\qquad u=s+1/2.
\tag{3.2}
\]
Both signs of the row represent the same coset; this explains the half. This is the weight-zero classical Eisenstein series with leading constant term \(y^u\). The classical function and its convergence are proved in Non-holomorphic Eisenstein series and Maass forms, equation (1.4) and Theorem 1.1. Its Theorem 2.2 gives the Fourier expansion and scattering coefficient, and Theorem 3.2 with Corollary 3.3 gives the completed continuation and reflection. The parameters agree by \(u=s+\tfrac12\): its completion is \(\Xi(2u)E(z,u)=\Lambda_{\mathbb Q}(2s+1)E_s(g_z)\), with \(\Xi(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w)\). Thus the classical reflection \(u\mapsto1-u\) is our \(s\mapsto-s\). We derive the adelic local shell and Gaussian transforms, their tensor product and the scattering operator below.

For a nonzero additive character, unfolding the open Bruhat cell exactly as in (2.4) gives a product of local Whittaker integrals. For trivial finite spherical data set
\[
\phi_p(v)=f_s^0(wn(v))=
 \begin{cases}1,&|v|_p\leq1,\\|v|_p^{-2u},&|v|_p>1.\end{cases}
\tag{3.3}
\]
Changing \(x=av\) in the integral, using (2.5) and \(f_s(d(a))=|a|^u\), yields
\[
W_{p,s}(d(a))=|a|_p^{1-u}
                    \int_{\mathbb Q_p}\phi_p(v)\psi_p(-av)\,dv.
\tag{3.4}
\]
For \(a=p^n\), \(n\geq0\), the integral of the character on a shell \(|v|_p=p^m\), \(m\geq1\), is
\[
\begin{cases}
(1-p^{-1})p^m,&m\leq n,\\
-p^n,&m=n+1,\\
0,&m>n+1.
\end{cases}
\tag{3.5}
\]
Indeed the integral on the ball \(p^{-m}\mathbb Z_p\) is its volume \(p^m\) when \(m\leq n\), and zero otherwise; subtract consecutive balls. The integral on \(\mathbb Z_p\) is one. Combining these values with (3.3), and summing the resulting finite geometric progression, gives
\[
W_{p,s}(d(p^n))
 =(1-p^{-1-2s})p^{n(s-1/2)}\sum_{j=0}^n p^{-2sj}.
\tag{3.6}
\]
When \(n<0\), all the ball integrals are zero, so the Whittaker integral is zero. Units do not alter (3.6), since they can be removed by an additive change of variable.

At infinity (3.4), including the translation in (3.1), becomes
\[
\begin{aligned}
W_{\infty,s}(d(n)g_z)
 &=|n|^{1-u}y^u e^{2\pi inx}
       \int_{\mathbb R}(v^2+y^2)^{-u}e^{-2\pi inv}\,dv\\
 &=\frac{2\pi^u}{\Gamma(u)}|n|^{1/2}\sqrt y\,
                        K_s(2\pi|n|y)e^{2\pi inx}.
\end{aligned}
\tag{3.7}
\]
Here is a derivation of the special function in that formula. Insert
\[
(v^2+y^2)^{-u}
 =\frac1{\Gamma(u)}\int_0^\infty t^{u-1}e^{-t(v^2+y^2)}\,dt.
\tag{3.8}
\]
For \(\operatorname{Re}u>1\), absolute integration permits Gaussian Fourier transformation, which changes the integral in (3.7) to
\[
\frac{\sqrt\pi}{\Gamma(u)}\int_0^\infty
              t^{u-3/2}e^{-y^2t-\pi^2n^2/t}\,dt.
\tag{3.9}
\]
The substitution \(t=(\pi|n|/y)e^v\) gives twice the integral
\[
K_\nu(a)=\int_0^\infty e^{-a\cosh v}\cosh(\nu v)\,dv,
 \qquad a>0,
\tag{3.10}
\]
with \(\nu=u-1/2=s\); the remaining powers give (3.7). This integral also shows \(K_\nu(a)=K_{-\nu}(a)\).

The finite product in (3.6) vanishes unless the rational Fourier index is an integer. For \(n\ne0\) its value is
\[
\frac{|n|^{s-1/2}\sigma_{-2s}(|n|)}{\zeta(1+2s)},
\qquad \sigma_a(m)=\sum_{d\mid m}d^a.
\tag{3.11}
\]
The local divisor sums multiply by unique factorization. The zero coefficient comes from (2.2). Fourier inversion on the smooth circle, justified by integration by parts as in Lesson 14, Theorem 1.1, now proves the complete expansion
\[
\begin{aligned}
E_s(g_z)
 &=y^{1/2+s}+c(s)y^{1/2-s}\\
 &\quad+\frac{2\sqrt y}{\Lambda(1+2s)}
    \sum_{n\ne0}|n|^s\sigma_{-2s}(|n|)
                   K_s(2\pi|n|y)e^{2\pi inx}.
\end{aligned}
\tag{3.12}
\]
We retained the zero coefficient in this application of Fourier inversion; cuspidality was used only to remove it in Lesson 14.

## 4. Continuation and the reflected parameter

**Theorem 4.1 — spherical continuation and functional equation.** The spherical Eisenstein series has meromorphic continuation to all \(s\), and
\[
E(g,f_s^0)=E(g,M(s)f_s^0)
          =c(s)E(g,f_{-s}^0),
\qquad c(s)c(-s)=1,
\tag{4.1}
\]
as identities of meromorphic families. In the middle expression the operator's output has the exchanged inducing data and parameter \(-s\). The same conclusions hold for everywhere spherical unitary inducing characters, with the determinant twist and parameter change described after (2.10).

**Proof.** First (3.10) is entire in \(\nu\). On \(|\operatorname{Re}\nu|\leq A\), its absolute value is bounded by
\(\int_0^\infty e^{-a\cosh v}\cosh(Av)\,dv\). For \(a\geq a_0>0\), remove the factor \(e^{-a/2}\) and bound the remainder by the same convergent integral with \(a_0/2\). Derivatives in \(\nu\) introduce powers of \(v\), with the same bound. On compact parameter sets \(|n|^s\sigma_{-2s}(|n|)\) grows at most polynomially in \(|n|\), since there are at most \(|n|\) divisors and each divisor power has such a bound. Thus the sum in (3.12) converges normally, with its real derivatives, when \(y\) stays in a positive compact interval. Tate's rational formula, NT-ADL-09 equation (28), continues \(\Lambda\) meromorphically and gives \(\Lambda(z)=\Lambda(1-z)\). Multiplying by the denominators in (3.12) gives a normally convergent holomorphic expression away from their finitely many poles on any compact parameter set. This proves meromorphic continuation through the Fourier expansion.

We prove its functional equation by the same Poisson mechanism, so it does not depend on a comparison of asymptotic leading terms. The determinant-one lattice \(\mathbb Z^2g_z\) has theta function
\[
\theta_z(r)=\sum_{(c,d)\in\mathbb Z^2}
               \exp\left(-\pi r^2|cz+d|^2/y\right).
\tag{4.2}
\]
Its dual lattice is an orthogonal quarter-turn of itself: the identity
\(g_z^{-t}=wg_zw^{-1}\), and \(\mathbb Z^2w=\mathbb Z^2\), verify this directly. Two-dimensional Poisson summation, obtained by applying the self-dual one-dimensional formula in both variables, gives
\[
\theta_z(r)=r^{-2}\theta_z(1/r).
\tag{4.3}
\]
For \(\operatorname{Re}u>1\), termwise Mellin integration is absolutely justified by the lattice majorant in Theorem 1.1. Decomposing a nonzero integer row into a positive integer times a primitive row yields
\[
\Lambda(2u)E_{u-1/2}(g_z)
 =\int_0^\infty(\theta_z(r)-1)r^{2u}\frac{dr}{r}.
\tag{4.4}
\]
Each row's Gaussian integral is \(\Gamma_{\mathbb R}(2u)/2\) times its norm to the power \(-2u\); the factor two from the signed primitive rows cancels this half.

Set \(A_z(u)=\int_1^\infty(\theta_z(r)-1)r^{2u}dr/r\). Nonzero lattice vectors have positive minimum norm, and the Gaussian sum decays faster than any power of \(r\), uniformly for \(z\) in compact sets. Hence \(A_z\) is entire by dominated differentiation. Split (4.4) at one and apply (4.3) to the small part. The result is
\[
\Lambda(2u)E_{u-1/2}(g_z)
 =A_z(u)+A_z(1-u)+\frac1{2u-2}-\frac1{2u}.
\tag{4.5}
\]
The two entire terms interchange under \(u\mapsto1-u\), and the two rational terms have exactly the same symmetry. Therefore
\[
\Lambda(1+2s)E_s(g_z)
       =\Lambda(1-2s)E_{-s}(g_z).
\tag{4.6}
\]
Tate's functional equation identifies \(\Lambda(1-2s)=\Lambda(2s)\), giving (4.1). It also gives
\[
c(s)c(-s)
 =\frac{\Lambda(2s)\Lambda(-2s)}
        {\Lambda(1+2s)\Lambda(1-2s)}=1.
\tag{4.7}
\]
All equalities are meromorphic, including parameters at which separate factors have zeros or poles.

Finally, by rational determinant decomposition in Lesson 1, Theorem 4.1, an arbitrary adelic \(g\), modulo rational left translation and finite \(K\), has real component in \(G(\mathbb R)^+\). Its real central scalar and right \(\mathrm O(2)\) factor leave this trivial-character section invariant. It is therefore represented by (3.1). This extends the proof to every adelic \(g\). A common determinant character commutes with summation and intertwining; absorbing the ratio norm character into \(\sigma\) proves the last assertion. \(\square\)

As a coefficient check, reflecting \(s\) in the sum uses
\[
|n|^s\sigma_{-2s}(|n|)
        =|n|^{-s}\sigma_{2s}(|n|),\qquad K_s=K_{-s}.
\tag{4.8}
\]
The first equality pairs a divisor with its complementary divisor. This verifies that the same reflected identity holds for every nonzero Fourier coefficient, as well as for the two constant terms.

### 4.2. Ramified sections and the exact intertwiner

For row vectors use the positive two-dimensional Fourier transform
\[
\widehat\Phi(y)=\int_{\mathbb A^2}\Phi(x)\psi(xy^t)\,dx,
\qquad
(\mathcal T\Phi)(y)=\widehat\Phi(yw^{-1}).
\tag{4.9}
\]
Here \(w\) is exactly (0.1), so \((0,t)w^{-1}=(-t,0)\). These signs fix the operator below.

**Theorem 4.2 — the full functional equation.** For every flat smooth compact-group-finite section, including every ramified inducing pair, \(M(s)\) has meromorphic continuation, and
\[
M_{\chi_2,\chi_1}(-s)M_{\chi_1,\chi_2}(s)=1,\qquad
E(g,f_s)=E(g,M(s)f_s).
\tag{4.10}
\]
The output on the right has the exchanged data and parameter \(-s\). On the two-dimensional Tate sections of Proposition 5.1 the exact formula is
\[
M_{\chi_1,\chi_2}(s)f_{\Phi,s}
 =f_{\mathcal T\Phi,-s}^{\,\chi_2,\chi_1}.
\tag{4.11}
\]
Thus no unspecified scattering scalar is hidden in this formula.

**Proof.** Proposition 5.1 already proves continuation of \(E(g,f_{\Phi,s})\) and locally meromorphic generation of every flat section, without using a general intertwiner or spectral-completeness theorem. We may therefore first prove the identities for these sections.

For a fixed \(g\), the partial integral
\[
\phi_g(t)=\int_{\mathbb A}\Phi((t,v)g)\,dv
\]
is a Schwartz function on \(\mathbb A\). This follows first for elementary tensor tests by integration, and then after a linear adelic change of variables, which preserves the Schwartz space. For \(\operatorname{Re}s>1/2\), substitute (5.2) into (2.1). The row
\((0,t)wn(x)=(t,tx)\); replacing \(tx\) by \(v\) contributes \(|t|^{-1}\). Hence
\[
(M(s)f_{\Phi,s})(g)
 =\chi_1(\det g)|\det g|^u
     Z_{\mathbb A}(\phi_g,\eta,2u-1),
\quad
Z_{\mathbb A}(\phi,\eta,z)
 =\int_{\mathbb A^\times}\phi(t)\eta(t)|t|^z\,d^\times t.
\tag{4.12}
\]
Absolute convergence of the last Tate integral for \(\operatorname{Re}(2u-1)>1\) also justifies the preceding double integral: its absolute-value version is bounded by the corresponding integral of the nonnegative partial integral of \(|\Phi|\). Thus Fubini here is valid.

Tate's global functional equation, NT-ADL-09 Theorem 9.2, says
\[
Z_{\mathbb A}(\phi_g,\eta,2u-1)
 =Z_{\mathbb A}(\widehat{\phi_g}_{-\psi},
                         \eta^{-1},2-2u)
\tag{4.13}
\]
as a meromorphic identity. The minus sign is allowed because
\(\eta(-1)=1\): a global Hecke character is trivial on \(\mathbb Q^\times\). This is the full global Tate equation, so there is no product of omitted local constants.

Additive change of variables gives
\[
\widehat{\phi_g}_{-\psi}(t)
 =|\det g|^{-1}\widehat\Phi((-t,0)g^{-t})
 =|\det g|^{-1}
        (\mathcal T\Phi)((0,t/\det g)g).
\tag{4.14}
\]
The second equality uses the exact rank-two identity
\[
g^{-t}=(\det g)^{-1}wg w^{-1},
\qquad w^{-1}g^{-t}=(\det g)^{-1}g w^{-1}.
\]
Now replace \(t\) by \((\det g)a\) in (4.13). The character and determinant factors in (4.12) become
\(\chi_1(\det g)\eta(\det g)^{-1}=\chi_2(\det g)\) and
\(|\det g|^{u-1+2-2u}=|\det g|^{1-u}\).
This is exactly the swapped section (5.2) with parameter \(-s\). It proves (4.11), including its coefficient one.

We also establish the Eisenstein equation directly. In the regularized theta Mellin integral \(J_g(u,\eta)\) of (5.4), Poisson summation transforms its small-norm part into the large-norm dual part. Inverting the norm variable exchanges
\((u,\eta)\) with \((1-u,\eta^{-1})\). The two zero terms are those of (5.5)–(5.6); they transform with the same exchange, including their signs and simple poles. Consequently
\[
J_{\Phi,g}(u,\eta)
 =|\det g|^{-1}
      J_{\widehat\Phi,g^{-t}}(1-u,\eta^{-1}).
\tag{4.15}
\]
This equality refers to the continued, split theta expression, rather than to two simultaneously convergent unregularized integrals. The rapidly decaying tails justify the change of variables and all parameter derivatives as in Proposition 5.1.

Use \(g^{-t}=(\det g)^{-1}wg w^{-1}\) again. Multiplication of rational rows by \(w\) permutes \(\mathbb Q^2\); replace the idèle variable by \((\det g)a\). The prefactor in (5.4) then becomes
\(\chi_2(\det g)|\det g|^{1-u}\), exactly as in (4.14). Thus
\[
E(g,f_{\Phi,s})
 =E(g,f_{\mathcal T\Phi,-s}^{\,\chi_2,\chi_1}).
\]
Together with (4.11) this proves the second equation of (4.10).

Finally \(\mathcal T^2=1\). Ordinary Fourier inversion gives reflection by \(-1\), and the two \(w^{-1}\) factors give \(w^{-2}=-I\), canceling that reflection. All measures are self-dual and \(\det w=1\), so no modulus factor appears. Applying (4.11) twice proves the first equation of (4.10) on the Tate sections.

The local-section generation argument at the end of Proposition 5.1 completes the proof for every flat section. At finite exceptional places choose its angular primitive-row function on the radial unit shell; at infinity choose its compact-finite angular function times a radial annulus bump. At other places take the integral-ring indicator. The compact restriction is \(a(s)F\), with \(a(s)\) a nonzero meromorphic scalar. A bump may be chosen to make each exceptional factor nonzero at a prescribed parameter, and the remaining partial Hecke function is not identically zero. Thus \(a(s)^{-1}\) is meromorphic everywhere, even where it has a pole, and dividing (4.11) gives the meromorphic operator on the desired flat section. Finite sums give all sections. Its continuation is unique because it agrees with the integral on an open half-plane. This also makes all identities independent of the chosen radial tests. The construction preserves fixed finite level and fixed real compact types, so the resulting meromorphy is ordinary finite-dimensional matrix meromorphy on each such compact-model space. \(\square\)

### 4.3. The unitary axis without a completeness assumption

**Theorem 4.3 — unitary scattering.** For unitary inducing data, \(M(it)\) is holomorphic for every real \(t\) and extends to a unitary map of the compact-model Hilbert spaces
\[
I(\chi_1,\chi_2,it)\longrightarrow I(\chi_2,\chi_1,-it).
\tag{4.16}
\]
This assertion does not use the spectral decomposition in Section 6.

**Proof.** First \(E(g,f_s)\) is regular on the unitary axis by Proposition 5.1 and Lemma 5.2. Its compact additive constant-term average is then regular, as are all real derivatives, because continuation is locally uniform after clearing poles. The continued identity
\(M(s)f_s=E_N(g,f_s)-f_s(g)\) proves regularity of \(M(s)\) on every section. On each fixed finite-level and real-compact-type space this is matrix regularity, since evaluations at finitely many compact points separate its finite-dimensional output. A norm ratio \(|\cdot|^{i\tau}\) is absorbed into \(\sigma=s+i\tau/2\) as in (1.7), so it suffices to treat norm-normalized data.

We prove the norm identity by Green's formula on the actual finite-level quotient, allowing all its cusps. Fix a right finite level and one real \(\mathrm{SO}(2)\)-weight \(m\). Rational determinant decomposition gives finitely many connected arithmetic surfaces with unitary automorphy factors; their compact cores have finitely many cusp collars. In a normalized cusp coordinate \(z=x+iy\), the weight-\(m\) Casimir equation for \(E_{it}\), after removing its common determinant twist, is
\[
\Delta_m E_{it}=(1/4+t^2)E_{it},
\qquad
\Delta_m=-y^2(\partial_x^2+\partial_y^2)+imy\partial_x.
\tag{4.17}
\]
This follows from the normalized induction parameter in (1.2), or by applying the induced Casimir to \(y^{1/2+s}\); the right action commutes with Eisenstein summation and continuation. The same computation underlies Lesson 4's Fourier equation and Lesson 11's real compact-type model.

The nonconstant modes and their first derivatives decay exponentially on every collar. Here is why moderate growth suffices for this use. A Fourier frequency \(n/w_c\ne0\), where \(w_c\) is the cusp period, has radial equation
\[
a_n''(y)=
 \left((2\pi n/w_c)^2
       -\frac{2\pi mn}{w_cy}
       -\frac{1/4+t^2}{y^2}\right)a_n(y).
\tag{4.18}
\]
At large \(y\) its two solutions have an increasing and a decreasing exponential factor with rate \(2\pi|n|/w_c\); the elementary integral-equation construction and constant-Wronskian argument of Lesson 4, Section 4, apply also with this \(O(y^{-1})\) term. Equivalently the real moderate Whittaker theorem proved in Lesson 11, Section 5, supplies the decreasing branch and its derivatives. Polynomial height bounds from the split Schwartz theta formula (5.4) exclude the increasing branch. Smooth Fourier estimates on a fixed lower boundary, followed by the same elliptic estimates as in Lesson 4, sum these bounds with derivatives. Thus their entire nonconstant part contributes zero to the limiting boundary flux. This is an analytic Fourier estimate, not a claim of spectral completeness.

The constant term on a collar is
\[
y^{1/2+it}A_c+y^{1/2-it}B_c,
\]
with \(A_c\) the incoming coefficient of \(f_{it}\) and \(B_c\) the outgoing coefficient of \(M(it)f_{it}\). The vectors may include the finite cusp multiplicities and the fixed compact type. Truncate every collar at \(y=R\). In
\[
\int_{X_R}
 \left((\Delta_m E_{it})\overline{E_{it}}
       -E_{it}\overline{\Delta_m E_{it}}\right)
                         \frac{dx\,dy}{y^2},
\]
the interior is zero because \(1/4+t^2\) is real. The \(imy\partial_x\) term is formally self-adjoint and its tangential boundary contributions cancel by the periodic unitary automorphy. Paired boundaries of the core cancel as well. The remaining boundary form, up to a common choice of outward sign, is
\(E_y\overline E-E\overline{E_y}\), integrated along each cusp period.

For the displayed constant term this form is exactly
\[
2it\bigl(\|A_c\|^2-\|B_c\|^2\bigr);
\tag{4.19}
\]
the mixed powers have equal derivative exponents and cancel. Integrate over the cusp periods and sum all collars, then let \(R\to\infty\). The nonconstant estimates remove their boundary terms. Unfolding the cusp boundary identifies the squared incoming and outgoing coefficient sums with the same positive constant times the corresponding compact-model norms. To verify the common measure, use Iwasawa coordinates on the parabolic quotient:
\(dg=C\,dx\,|a|^{-1}d^\times a\,dk\).
At fixed height, the two \(y^{1/2\pm it}\) powers have identical absolute value; their half-density cancels the modular \(|a|^{-1}\). The norm-one idèle-class factor has probability measure (0.2), and the inducing characters have modulus one. The remaining integral is the compact probability norm of \(F(k)\), for the incoming data, and of \(M(it)F(k)\), for the outgoing data. At a finite right level this unfolding is precisely the finite sum of its cusp periods; stabilizer indices affect both in the same way. The common positive Haar constant therefore cancels.

For \(t\ne0\), (4.19) consequently gives
\(\|M(it)f\|_K=\|f\|_K\).
Polarization gives preservation of the full inner product. At \(t=0\), holomorphy on each finite-dimensional compact-model space and continuity along \(it\) give the same norm identity. Arbitrary finite sums of real weights are orthogonal in the compact model, and \(M\) commutes with the right compact group, so the identity holds for every smooth compact-group-finite section.

These sections are dense in their unitary compact models. The isometry extends uniquely to their Hilbert completions. Equation (4.10) gives its inverse on the dense finite sections, so its range is both dense and closed and the extension is onto. This proves unitarity. \(\square\)

Theorem 4.2 supplies the general ramified functional equation that the spherical argument alone could not supply. Theorem 4.3 supplies its unitary-axis norm assertion by a rank-one boundary calculation. The remaining completeness and wave-packet measure in Section 6 still require their own proof.


## 5. Poles and the entire residual representation

The spherical calculation gives more than an unspecified residue. Formula (4.5) has residue \(1/2\) at \(u=1\), independently of \(z\). Since \(\Lambda(2)=\pi/6\),
\[
\operatorname*{Res}_{s=1/2}E_s(g)=\frac1{2\Lambda(2)}=\frac3\pi.
\tag{5.1}
\]
For that elementary value, the function \(x-\pi\) on \([0,2\pi]\) has sine coefficients \(-2/n\) by integration by parts. Orthogonality and the density of trigonometric polynomials give Parseval, so \(\pi^{-1}\int_0^{2\pi}(x-\pi)^2dx=2\pi^2/3=4\sum_{n\ge1}n^{-2}\). Hence \(\zeta(2)=\pi^2/6\). Thus the residue really is constant on the full spherical adelic quotient.

To identify all residues we must also allow ramified inducing characters and nonspherical sections. The following argument calculates them without restricting to the classical level-one subspace.

**Proposition 5.1 — the two-dimensional Tate construction.** Assume the ratio \(\eta\) is norm-normalized as in (1.7), and let \(\Phi\in\mathcal S(\mathbb A^2)\). Define, initially for \(\operatorname{Re}u>1\),
\[
f_{\Phi,s}(g)=\chi_1(\det g)|\det g|^u
   \int_{\mathbb A^\times}\Phi((0,t)g)\eta(t)|t|^{2u}\,d^\times t.
\tag{5.2}
\]
Its Eisenstein series has meromorphic continuation. It has no poles in \(\operatorname{Re}s>0\) except possibly \(s=1/2\); that pole occurs only when \(\eta=1\), and its residue is
\[
\operatorname*{Res}_{s=1/2}E(g,f_{\Phi,s})
       =\tfrac12\widehat\Phi(0)\chi_1(\det g).
\tag{5.3}
\]
Every flat smooth compact-group-finite section is locally a finite sum of such sections multiplied by scalar meromorphic functions. Near \(\operatorname{Re}s>0\) those scalars can be chosen holomorphic. Consequently (5.3) identifies the possible positive residues for every section.

**Proof.** Changing \(t\) to \(dt\) after left multiplication by an upper triangular matrix gives exactly (1.2); its characters simplify as
\(\chi_1(ad)\eta(d)^{-1}=\chi_1(a)\chi_2(d)\), and its powers as \(|ad|^u|d|^{-2u}=|a/d|^u\). Global convergence of (5.2) follows from Proposition 9.1 of NT-ADL-09, applied to the one-dimensional Schwartz function \(t\mapsto\Phi((0,t)g)\) with exponent \(2u\).

Summing its rational row lines and unfolding rational scalings gives
\[
\begin{aligned}
E(g,f_{\Phi,s})
 &=\chi_1(\det g)|\det g|^u J_g(u,\eta),\\
J_g(u,\eta)
 &=\int_C\left(\sum_{v\in\mathbb Q^2}\Phi(tv g)-\Phi(0)\right)
                       \eta(t)|t|^{2u}\,d^\times t.
\end{aligned}
\tag{5.4}
\]
Every nonzero rational row lies in exactly one such line and rational scalar; counting measure on \(\mathbb Q^\times\) gives the quotient integral. Absolute convergence follows by bounding the finite support by a fixed rational lattice and applying the two-dimensional version of the dyadic estimate in Theorem 1.1. For large norm the Schwartz estimate gives arbitrarily rapid decay of the nonzero theta sum, uniformly on the compact norm-one fibres and on compact \(g\)-sets. The compact-lift argument of the theta lemma in NT-ADL-09 applies verbatim with a rank-two rational lattice; its estimate is \(O(r^{-N})\) for any chosen \(N>2\).

For \(\Phi_g(v)=\Phi(vg)\), additive change of variables gives
\[
\widehat{\Phi_g}(v)=|\det g|^{-1}\widehat\Phi(vg^{-t}).
\]
Poisson summation therefore changes the theta sum in the small-norm part of (5.4) to the dual nonzero sum plus
\[
|t|^{-2}|\det g|^{-1}\widehat\Phi(0)-\Phi(0).
\tag{5.5}
\]
The original large-norm tail and the transformed tail are entire, by the rapid-decay bound. Compact averaging kills both zero terms unless \(\eta\) is trivial on the norm-one group. Norm normalization then forces \(\eta=1\). In that case their integrals are
\[
\frac{|\det g|^{-1}\widehat\Phi(0)}{2u-2}
                         -\frac{\Phi(0)}{2u}.
\tag{5.6}
\]
This proves continuation, the possible poles, and (5.3), since the prefactor in (5.4) at \(u=1\) cancels \(|\det g|^{-1}\).

We justify the assertion about sections, which is needed for exhaustion of the residues. In a pure flat section only finitely many finite places are exceptional. At an exceptional finite place, a section on \(K_v\) is prescribed by a locally constant function of the primitive bottom row, after removing \(\chi_{1,v}(\det k)\). Upper triangular compact covariance makes this well-defined: changes of the top row cancel against the determinant character. Scaling the bottom row by a unit gives the covariance \(\eta_v^{-1}\). Put that angular function on primitive rows, multiplied by the indicator of the radial unit shell, and zero off this shell. The integral in (5.2), at \(k\in K_v\), is then its prescribed value times a nonzero constant. At infinity use the corresponding smooth angular function on the unit circle and a smooth radial function supported in a narrow annulus. Its Mellin integral is holomorphic and can be made nonzero at any given parameter by choosing a sufficiently narrow nonnegative radial bump; the complex phase varies arbitrarily little on such an annulus. The angular parity is exactly \(\eta_\infty(-1)\).

At every other prime take \(\Phi_p=\mathbf1_{\mathbb Z_p^2}\). On \(K_p\) its integral is \(L_p(2u,\eta_p)\). Hence this construction has compact restriction \(a(s)F\), where
\[
a(s)=L^S(2u,\eta)\prod_{v\in S\cup\{\infty\}}a_v(s),
\tag{5.7}
\]
and each selected local factor is holomorphic and nonzero near the parameter in question. The omitted finite Euler factors do not vanish there. For \(\operatorname{Re}2u>1\), absolute convergence of the logarithmic Euler series makes \(L^S(2u,\eta)\) nonzero and finite. Thus \(a(s)^{-1}\) is holomorphic at every point of \(\operatorname{Re}s>0\), including \(s=1/2\). Dividing recovers the original section and its Eisenstein series in the initial half-plane, and then everywhere by continuation. Finite sums of pure sections give all the vectors under consideration. \(\square\)

For completeness, poles on the unitary boundary cannot be hidden in (5.7). We include the needed elementary nonvanishing argument.

**Lemma 5.2 — the boundary Euler factors.** For a nontrivial primitive Dirichlet character \(\varepsilon\), \(L(1+it,\varepsilon)\ne0\) for every real \(t\). Also \(\zeta(1+it)\ne0\) for \(t\ne0\), and \(\zeta\) has a simple pole at one. Thus a norm-normalized rational Hecke character has nonzero finite \(L\)-function on the line \(\operatorname{Re}z=1\), except for this trivial-character pole.

**Proof.** Bounded partial sums of a nontrivial periodic character and summation by parts continue its Dirichlet series holomorphically to \(\operatorname{Re}z>0\). The same procedure applied to the difference between \(\sum n^{-z}\) and its integral continues \(\zeta(z)\) there with its single pole at one and residue one; this also follows from Tate's formula (28).

For \(\rho>1\), expand the logarithms of the Euler products. At primes not dividing the conductor, the identity
\(3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\geq0\), applied to each prime power, gives
\[
\zeta(\rho)^3|L(\rho+it,\varepsilon)|^4
                   |L(\rho+2it,\varepsilon^2)|\geq1.
\tag{5.8}
\]
At conductor primes the character factors are absent and the zeta contribution is positive, so the same lower bound holds; imprimitive versions of the last factor introduce only finite nonzero factors at the boundary. If the middle factor had a zero of order \(m\geq1\) at \(1+it\), and the last factor had no pole there, the left side would be \(O((\rho-1)^{4m-3})\), tending to zero. Its last factor can have a pole only when \(t=0\) and \(\varepsilon^2\) is principal. This proves all cases except nontrivial real quadratic \(\varepsilon\) at \(t=0\); taking the principal character gives the same proof for \(\zeta(1+it)\), \(t\ne0\).

In the remaining case the Dirichlet coefficients of \(\zeta(z)L(z,\varepsilon)\) are
\(a_n=\sum_{d\mid n}\varepsilon(d)\geq0\). To check this, multiply the prime-power sums: they equal \(m+1\) if \(\varepsilon(p)=1\), one or zero according to the parity of \(m\) if \(\varepsilon(p)=-1\), and one if \(\varepsilon(p)=0\). In particular \(a_{n^2}\geq1\). Its convergence abscissa \(\beta\) therefore lies in \([1/2,1]\).

A Dirichlet series with nonnegative coefficients must be singular at its finite convergence abscissa. Here is the needed proof. If it were analytic there, take a real \(b>\beta\) sufficiently close to \(\beta\) that the function is analytic on a disk centered at \(b\) of radius exceeding \(b-\beta\); such a disk fits in the union of the right half-plane of convergence and a small disk of analyticity about \(\beta\). Termwise derivatives at \(b\) give Taylor coefficients of the form
\((-1)^k\sum_n a_n(\log n)^k n^{-b}/k!\). Evaluate at \(b-r\), with \(b-\beta<r\) inside that disk. All resulting summands are nonnegative, so monotone interchange of the Taylor and Dirichlet sums gives the finite value \(\sum_n a_n n^{-(b-r)}\). This contradicts the definition of \(\beta\).

If \(L(1,\varepsilon)=0\), it cancels the only pole of \(\zeta\), so their product is holomorphic throughout \(\operatorname{Re}z>0\), including \(\beta\). This contradicts the preceding positive-coefficient argument. The quadratic case follows. Finite factors relating any rational Hecke character to its primitive Dirichlet character have roots on \(\operatorname{Re}z=0\), so they do not change the boundary conclusion. \(\square\)

In (5.7), at \(\operatorname{Re}s=0\), this lemma again makes \(a(s)^{-1}\) holomorphic. When \(\eta=1\) and \(s=0\), the scalar has a simple pole, so its inverse has a zero; (5.4) is regular there, and the normalized Eisenstein family is regular as well. Thus there are no poles on the unitary axis. For norm-normalized data the only poles in \(\operatorname{Re}s\geq0\) are the possible simple poles already calculated at \(s=1/2\), with \(\chi_1=\chi_2\). For unnormalized ratio data use (1.7); the residue at the shifted pole is a multiple of \(\chi'_1\circ\det\), where \(\chi'_1=\chi'_2\).

**Theorem 5.3 — residual representations.** The residues of all these positive Eisenstein poles span precisely the one-dimensional representations
\[
g\longmapsto\chi(\det g)
\tag{5.9}
\]
for unitary Hecke characters \(\chi\). In the Hilbert space with fixed central character \(\omega\), retain exactly those satisfying \(\chi^2=\omega\). Section 6 proves directly that these lines exhaust its noncuspidal discrete spectrum, by pseudo-Eisenstein density, the exact packet isometry and the absence of atoms in the continuous parameter measure.

**Proof.** Proposition 5.1 shows that every residue is on such a line. Conversely twist the spherical series by \(\chi\circ\det\); (5.1) gives a nonzero residue \((3/\pi)\chi\circ\det\), so every line occurs. Its central character is \(\chi(z^2)=\chi(z)^2\). Its absolute value is one, hence it is square integrable on the finite-volume central quotient. Right translation acts on its line by the character \(\chi\circ\det\).

It is orthogonal to cuspidal forms. For a smooth cusp form \(\varphi\) of the same central character, unfold the pairing with \(E(g,f_s)\) in the initial half-plane. Rapid decay from Lesson 4, Theorem 4.2, makes the integral absolute, and integrating over \(\mathbb Q\backslash\mathbb A\) first gives the zero constant term of \(\varphi\). Thus the pairing is zero. The continued family has uniform polynomial height bounds locally in the parameter after clearing its poles: these follow from the Schwartz theta estimates in (5.4), or from its finite-level Fourier expansion and its constant terms. Rapid decay consequently permits continuation of the pairing and extraction of its residue, which is still zero.

For exhaustion, Section 6 supplies the remaining Hilbert-space argument: pseudo-Eisenstein series are dense in the orthogonal complement of the cusp space; shifting their Mellin inner-product contour gives exactly these character projections and the invariant continuous data with measure \(dt/(4\pi)\). The resulting isometry is onto. The real Casimir is multiplication by \(1/4+t^2\) on those continuous data, so no nonzero irreducible discrete summand can occur there. This proves the claimed exhaustion using the full proof below. \(\square\)

For \(\omega=1\), the full adelic residual space contains \(\chi\circ\det\) for every quadratic Hecke character, not just the constant function. Its subspace fixed by all finite \(K_p\) and by the real compact group has only the trivial character and hence only the constant line. If \(\omega\) has no character square root, its residual space is zero.

## 6. Completeness, the wave-packet norm and residual exhaustion

We now prove the full rank-one spectral theorem needed in this lesson. The general meromorphic continuation and unitary scattering were proved in Theorems 4.2–4.3; they will not be replaced by a completeness assumption.

Write \(H(\omega)\) for the Hilbert space of measurable functions with
\(h(\gamma zg)=\omega(z)h(g)\), square integrable modulo
\(G(\mathbf Q)Z(\mathbb A)\). Their absolute squares descend to the quotient; when \(\omega\ne1\), these are central-character sections, as in Lesson 2.

### 6.1. The parabolic test functions and their Mellin data

If \(\omega|_{\mathbf R_{>0}}=|\cdot|^{i\beta}\), multiplication by
\(|\det g|^{-i\beta/2}\) removes its norm part unitarily. We may first suppose that \(\omega\) is trivial on positive real scalars, and restore this common determinant twist at the end. The ordered base pairs
\[
b=(\chi_1,\chi_2),\qquad \chi_1\chi_2=\omega,
\quad \chi_j|_{\mathbf R_{>0}}=1,
\tag{6.4}
\]
are then a countable set: they are indexed by characters of the compact group \(C^1\simeq\widehat{\mathbf Z}^{\times}\). Put \(b^w=(\chi_2,\chi_1)\), and let \(\mathcal H_b\) be the unitary compact model of \(I(\chi_1,\chi_2,0)\), with probability Haar measure on \(K\). A fixed finite level allows only finitely many of these compact torus characters, and a fixed packet of real compact types gives finite-dimensional compact-model spaces.

The parabolic quotient used below is
\[
Y=B(\mathbf Q)Z(\mathbb A)N(\mathbb A)\backslash G(\mathbb A).
\]
It has the prescribed central line bundle. Choose a smooth section \(f\) on \(Y\), compactly supported in the logarithmic height, of finite finite-place level and finitely many real compact types. Compact torus character expansion writes it as a finite sum whose radial parts are
\[
f_b(y,k)=y^{1/2}\xi_b(y,k),\qquad
\xi_b\in C_c^\infty(\mathbf R_{>0};\mathcal H_b^{\,\mathrm{finite}}).
\]
Here the height is the norm of the diagonal ratio on the central-normalized slice, and the compact torus dependence is the character prescribed by \(b\). Define
\[
F_b(s)=\int_0^\infty \xi_b(y)y^{-s}\frac{dy}{y},
\qquad
\xi_b(y)=\int_{\operatorname{Re}s=a}F_b(s)y^s\frac{ds}{2\pi i}.
\tag{6.5}
\]
This is ordinary Fourier inversion in \(\log y\), with a real exponential weight. Each \(F_b\) is entire and decreases faster than any power of \(|\operatorname{Im}s|\) on every fixed vertical strip, by integration by parts in that compact logarithmic interval.

We use the following exact measure identity. Unfolding \(N(\mathbf Q)\backslash N(\mathbb A)\), of volume one, leaves on \(Y\) the Iwasawa measure
\[
|a|^{-1}d^\times a\,dk.
\]
The compact norm-one idèle-class factor and \(K\) have probability measure. Consequently the product of the two \(y^{1/2}\) half-densities cancels the modular factor and leaves \(dy/y\) and the compact-model inner product. There is no extra positive constant here: for level-one compact-invariant tests this is exactly \(dx\,dy/y^2\) on the classical surface, with rotation probability measure, as fixed in Lesson 1, equations (2.3) and (5.1). Haar uniqueness then gives the same normalization on all finite covers. Their cusp periods and stabilizer indices are precisely the finite quotient-integration factors of that measure.

The pseudo-Eisenstein series is
\[
\Theta_f(g)=\sum_{\gamma\in B(\mathbf Q)\backslash G(\mathbf Q)}
                         f(\gamma g).
\tag{6.6}
\]
This sum is locally finite. The primitive-row height formula (1.5) bounds the bottom rows contributing to any compact \(g\)-set because \(f\)'s heights are bounded above and below. Moreover \(\Theta_f\) has compact support on the central quotient at its fixed level. Indeed, at a high cusp the identity cell has height above the maximum allowed by \(f\). Every other rational row has nonzero first coordinate \(c\), bounded away from zero on the fixed principal-congruence cover, and its new height is at most \(C/(c^2y)\); this is below the minimum allowed height when \(y\) is large. There are finitely many components and cusps by Lesson 1, Section 4, so one compact core contains the support. Thus \(\Theta_f\) is smooth and in \(H(\omega)\).

**Lemma 6.2 — density outside the cusp space.** The closure of all \(\Theta_f\) is \(H_{\mathrm{cusp}}(\omega)^\perp\).

**Proof.** For an arbitrary \(h\in H(\omega)\), average on the compact additive quotient:
\[
h_N(g)=\int_{N(\mathbf Q)\backslash N(\mathbb A)}h(ng)\,dn.
\]
It is defined almost everywhere and locally in \(L^2\), by local quotient integration, Fubini and Cauchy–Schwarz on this probability space. Unfolding gives
\[
\langle h,\Theta_f\rangle
 =\int_Y h_N(g)\overline{f(g)}\,dg.
\tag{6.7}
\]
Our inner product is linear in its first variable. The unfolding is absolute: on the compact parabolic support of \(f\), its additive lift is compact, and local \(L^2\) and boundedness of \(f\) give an \(L^1\) bound. Equivalently unfold the absolute integrand first.

The compact torus characters, finite compact projections, smooth compact real kernels and compact logarithmic tests are dense in the test space on \(Y\). Hence (6.7) vanishes for every \(f\) exactly when \(h_N=0\). This is the Hilbert cuspidal condition of Lesson 4. Its equivalence with the closed cuspidal space used there follows also directly: compact right convolution preserves zero constant term and approximates \(h\), and the fixed-level cuspidal self-adjoint realization and its compact resolvent supply dense finite cuspidal vectors. Taking orthogonal complements proves the lemma. \(\square\)

For \(a>1/2\), Mellin inversion and the primitive-row convergence estimate give
\[
\Theta_f(g)=
 \sum_b\int_{\operatorname{Re}s=a}
             E(g,F_b(s)_s)\frac{ds}{2\pi i}.
\tag{6.8}
\]
The subscript means the section in the \(b,s\) induction with compact restriction \(F_b(s)\). Its rapid vertical decrease and Theorem 1.1 justify inversion through the sum and all real derivatives on compact \(g\)-sets.

### 6.2. The complete Maass–Selberg identity and a contour bound

Fix a finite level and real rotation weight. Choose \(T>0\) so large that all cusp collars of height \(y>e^T\) are disjoint. Define \(\Lambda^T E_s\) by subtracting its full constant term on those collars and leaving the series unchanged on the core. The nonconstant-mode estimate used in Theorem 4.3 makes this truncated function square integrable. This is a piecewise \(L^2\) truncation; its jump at the cutoff is handled by separate integrals on the core and collars.

**Lemma 6.3 — the four boundary terms.** If the two sections have compatible compact types and central character, then
\[
\begin{aligned}
\langle\Lambda^T E_s(f),\Lambda^T E_r(h)\rangle
&=\frac{e^{(s+\overline r)T}\langle f,h\rangle_K
       -e^{-(s+\overline r)T}
          \langle M(s)f,M(r)h\rangle_K}{s+\overline r}\\
&\quad+
 \frac{e^{(s-\overline r)T}\langle f,M(r)h\rangle_K
       -e^{-(s-\overline r)T}
          \langle M(s)f,h\rangle_K}{s-\overline r}.
\end{aligned}
\tag{6.9}
\]
Coefficient pairings on different compact torus characters are zero. Thus for different base pairs only the corresponding compatible terms are retained. Apparent denominator singularities are interpreted by limits whenever the series themselves are regular.

**Proof.** Each finite-level component is an arithmetic surface with unitary automorphy factors. At weight \(m\), the operator is (4.17) and its eigenvalue is \(1/4-s^2\). Green's identity on the compact core, followed by its identity on the nonconstant parts of the outer collars, expresses
\((s^2-\overline r^{\,2})\) times the truncated pairing as a boundary Wronskian of the constant terms. The boundary at infinity of the nonconstant parts is zero, with first derivatives, by the proved estimates in Lessons 4 and 11. Their boundary at \(e^T\) cancels the nonconstant contribution from the core. The tangential \(imy\partial_x\) term cancels on the paired periodic boundaries, including the unitary phases. Thus only the constant terms remain.

Their four products have respective powers
\(y^{s+\overline r}\), \(y^{-s-\overline r}\),
\(y^{s-\overline r}\) and \(y^{-s+\overline r}\) after the boundary density is included. Their derivative differences, with the outward Green sign, are
\(s-\overline r\), \(-s+\overline r\),
\(s+\overline r\) and \(-s-\overline r\).
Divide by
\((s+\overline r)(s-\overline r)\) to obtain the four terms in (6.9). Unfold the sum of cusp periods and finite components as in (6.5)'s measure identity. It gives exactly the indicated compact-model pairings; compact torus orthogonality explains the zero incompatible terms. This proves the formula when the eigenvalue difference is nonzero and neither series has a pole. Continuation and taking limits prove the remaining regular cases. Orthogonal weight projections give the formula for finite packets of real compact types as well. \(\square\)

This identity provides the bound needed for contour shifting. Put \(r=s=\sigma+it\), \(0<\sigma\le a\), \(|t|\ge1\), and normalize \(\|f\|_K=1\). Let \(m_s=\|M(s)f\|_K\). Positivity of the left side of (6.9), and Cauchy–Schwarz for its mixed terms, give
\[
e^{-2\sigma T}m_s^2
 \le e^{2\sigma T}+\frac{2\sigma}{|t|}m_s,
\qquad
m_s\le e^{2\sigma T}
 \left(\frac{\sigma}{|t|}
       +\sqrt{1+\frac{\sigma^2}{t^2}}\right).
\tag{6.10}
\]
When the base pair differs from its exchange the mixed terms are simply zero, and the same bound applies. It is uniform on \(0\le\operatorname{Re}s\le a\), \(|\operatorname{Im}s|\ge1\), on each chosen finite-level/type space:
\[
\|M(s)\|\le e^{2aT}(a+\sqrt{1+a^2}).
\tag{6.11}
\]
At \(\sigma=0\), use the already proved unitarity or continuity. No lower bound for a boundary Hecke \(L\)-function, and no spectral-completeness assertion, has been used to obtain this vertical-strip estimate.

### 6.3. The pseudo-Eisenstein inner product and its residues

Let \(f,h\) be two parabolic tests, with Mellin data \(F_b,H_b\). Unfold \(\Theta_h\) against (6.8), and use the two constant terms (2.2). The half-density measure calculation gives
\[
\begin{aligned}
\langle\Theta_f,\Theta_h\rangle
=\sum_b\int_{\operatorname{Re}s=a}
\bigl(&\langle F_b(s),H_b(-\overline s)\rangle_K\\
 &+\langle M_b(s)F_b(s),H_{b^w}(\overline s)\rangle_K\bigr)
                       \frac{ds}{2\pi i}.
\end{aligned}
\tag{6.12}
\]
To check the conjugate arguments, integrate the incoming power \(y^s\) against \(\overline{\xi_h(y)}dy/y\), obtaining
\(\overline{H_h(-\overline s)}\); the outgoing power \(y^{-s}\) gives
\(\overline{H_h(\overline s)}\). Consequently the integrand is meromorphic in \(s\) under our inner-product convention. The unfolded parabolic support is compact and the Mellin data decrease rapidly, which justifies all interchanges initially.

Move the contour to \(\operatorname{Re}s=0\). Equation (6.11), and the rapid Mellin decrease on the whole intervening strip, make the horizontal integrals tend to zero. Theorems 4.2–4.3 and Proposition 5.1 show that the only enclosed poles are the possible simple poles at \(s=1/2\) for \(b=(\chi,\chi)\), with \(\chi^2=\omega\). There are only finitely many such labels at the level under consideration.

Write \(e_\chi(k)=\chi(\det k)\), a unit compact vector, and
\[
\ell_\chi(v)=\langle v,e_\chi\rangle_K.
\]
The precise residue operator is
\[
\operatorname*{Res}_{s=1/2}M_b(s)v
 =\frac3\pi\,\ell_\chi(v)e_\chi,\qquad b=(\chi,\chi).
\tag{6.13}
\]
Indeed Proposition 5.1 says that the residue of the corresponding Eisenstein series is a scalar times \(\chi\circ\det\). Right compact equivariance makes its scalar functional a multiple of the compact projection \(\ell_\chi\): that character has multiplicity one in the compact induced model, by compact Frobenius reciprocity or by its prescribed values on \(B\cap K\). Twisting the spherical vector by \(\chi\circ\det\) gives the residue \(3/\pi\), fixing the multiple. Taking the additive constant term shows that the residue of \(M\) is the same, because the original \(f_s\) is regular. This proves (6.13) for every vector, not only the spherical one.

Distinct character lines are orthogonal: translate their inner product by a group element where their determinant characters differ and use right Haar invariance. Each has squared norm \(\pi/3\), since its absolute value is one and Lesson 1 computed the quotient volume. Define
\[
R_f(g)=\sum_{\chi^2=\omega}
 \frac3\pi\,
   \ell_\chi(F_{(\chi,\chi)}(1/2))\,\chi(\det g).
\tag{6.14}
\]
This is exactly the orthogonal projection of \(\Theta_f\) onto the closed sum of these lines. To verify it independently of contour shifting, unfold its pairing with \(\chi\circ\det\). Only the corresponding compact torus character survives; the radial integral is
\(\int\xi(y)y^{-1/2}dy/y=F(1/2)\), followed by the compact functional \(\ell_\chi\). Thus
\(\langle\Theta_f,\chi\circ\det\rangle=\ell_\chi(F(1/2))\).
Dividing by the squared norm \(\pi/3\) gives (6.14).

Equation (6.13) makes the contour residues in (6.12) precisely
\(\langle R_f,R_h\rangle\). The remaining integral is
\[
\begin{aligned}
\langle\Theta_f-R_f,\Theta_h-R_h\rangle
=\sum_b\int_{\mathbf R}\bigl(
 &\langle F_b(it),H_b(it)\rangle_K\\
 &+\langle M_b(it)F_b(it),H_{b^w}(-it)\rangle_K
                         \bigr)\frac{dt}{2\pi}.
\end{aligned}
\tag{6.15}
\]

### 6.4. The invariant data space and the Plancherel factor

On
\(\mathcal D_0=\widehat\bigoplus_b L^2(\mathbf R,\mathcal H_b;dt/(2\pi))\)
define
\[
(WF)_b(t)=M_{b^w}(-it)F_{b^w}(-t),\qquad
P=\tfrac12(1+W).
\tag{6.16}
\]
Theorem 4.3 and (4.10) make \(W\) a unitary involution, hence self-adjoint, and \(P\) an orthogonal projection. Its range consists exactly of families satisfying
\[
F_{b^w}(-t)=M_b(it)F_b(t)
\quad\text{almost everywhere}.
\tag{6.17}
\]
For these invariant families use the norm
\[
\|F\|_{\mathcal D}^2
 =\sum_b\int_{\mathbf R}\|F_b(t)\|_K^2\frac{dt}{4\pi}.
\tag{6.18}
\]
The factor \(1/2\) relative to ordinary Mellin Fourier measure is the Weyl factor.

Equation (6.15), after replacing \(t\) by \(-t\) and the label by its exchange where needed, is
\[
\langle\Theta_f-R_f,\Theta_h-R_h\rangle
 =2\langle PF,PH\rangle_{\mathcal D_0}
 =\langle 2PF,2PH\rangle_{\mathcal D}.
\tag{6.19}
\]
The last factor two in the data is necessary. We have not assigned the ordinary Mellin measure to a twice-counted family.

**Theorem 6.1 — the full spectral decomposition and isometry.** There is an orthogonal decomposition of right unitary representations
\[
H(\omega)=H_{\mathrm{cusp}}(\omega)
 \oplus H_{\mathrm{res}}(\omega)
 \oplus H_{\mathrm{cont}}(\omega),
\tag{6.1}
\]
where \(H_{\mathrm{res}}\) is the Hilbert sum of the character lines
\(\chi\circ\det\), \(\chi^2=\omega\), and \(H_{\mathrm{cont}}\) is unitarily isomorphic to \(\mathcal D\). Its dense smooth packets are
\[
\mathcal E(F)(g)
 =\sum_b\int_{\mathbf R}E(g,F_b(t)_{it})\frac{dt}{4\pi},
\qquad F\in\mathcal D,
\tag{6.20}
\]
initially for smooth compact parameter support, finite labels and finite compact types satisfying (6.17). The same measure gives their exact squared norm (6.18). In the original untwisted notation their unitary data are
\[
I(\chi_1,\chi_2,it),\qquad \chi_1\chi_2=\omega,
\tag{6.2}
\]
with norm-normalized base ratio. The data at the exchanged pair and \(-t\) are identified by the proved intertwiner.

**Proof.** By (6.19), the map
\[
\Theta_f\longmapsto(R_f,2PF)
\]
is an isometry into \(H_{\mathrm{res}}\oplus\mathcal D\). It is well-defined even if two tests have the same pseudo-Eisenstein series: the zero norm of their difference forces both images to agree. Extend it to the completion, which is \(H_{\mathrm{cusp}}^\perp\) by Lemma 6.2. Its image is closed.

This image is the whole target. First every character line is orthogonal to cusp forms, as proved in Theorem 5.3 before any use of residual exhaustion. Hence it lies in \(H_{\mathrm{cusp}}^\perp\), and can be approximated by pseudo-Eisenstein vectors. For such an approximation, the actual orthogonal projections \(R_f\) converge to that line vector, and (6.19) makes the data norms tend to zero. Thus the image contains \(H_{\mathrm{res}}\oplus0\). Second Fourier transforms of compact smooth logarithmic functions are dense in \(L^2(\mathbf R)\); compact torus characters and finite compact vectors are dense in the other factors. Therefore the Mellin data \(F\) of our tests are dense in \(\mathcal D_0\). Projection by \(P\) makes \(2PF\) dense in \(\mathcal D\). Subtracting the first component, already in the image, and using closedness shows that the image contains \(0\oplus\mathcal D\). This proves surjectivity and (6.1).

We identify the inverse with the actual packet (6.20). Smooth compactly supported invariant data are dense: start with a finite-label/type smooth compactly supported family and apply \(P\); the holomorphic finite-dimensional matrix \(M(it)\) preserves smoothness and compact parameter support. Their packet is a smooth \(L^2\) function. On every collar its two constant terms are Fourier integrals in \(\log y\) with smooth compact parameter support, and hence decrease faster than any power of \(\log y\) after the \(y^{1/2}\) half-density is removed. This is square integrable against the cusp density. The nonconstant part and derivatives decay exponentially, uniformly on a compact parameter set, by the proven mode estimates; compact-core bounds follow by continuity of the continued family. Each Eisenstein family is orthogonal to cusp forms by the absolutely unfolded cuspidal pairing and continued rapid decay used in Theorem 5.3. The packet is therefore in \(H_{\mathrm{cusp}}^\perp\).

Pair the packet with \(\Theta_h\). Its compact parameter range and the compact parabolic support of \(h\) permit absolute unfolding, giving the incoming and outgoing pairings of (6.15), now with measure \(dt/(4\pi)\). By (6.17) the two terms combine to
\[
\langle\mathcal E(F),\Theta_h\rangle
 =\langle F,2PH\rangle_{\mathcal D}.
\]
Since pseudo-Eisenstein vectors are dense in \(H_{\mathrm{cusp}}^\perp\), this is exactly the pairing of the inverse isometry with data \((0,F)\). Thus the packet has zero residual component, is the inverse image of that data, and has squared norm (6.18). Extend by the isometry to every measurable square-integrable invariant family. Right translation commutes with Eisenstein summation and continuation, so this is an isomorphism of unitary \(G(\mathbb A)\)-representations. Restoring the common norm determinant twist proves the theorem for every unitary \(\omega\). \(\square\)

### 6.5. No missing discrete representations

It remains to justify the residual-exhaustion assertion in Theorem 5.3, rather than merely identify some residues. On the continuous data space, the real Casimir, in the normalization (4.17), acts by multiplication by
\[
\frac14+t^2.
\tag{6.21}
\]
This follows first on the dense packets from their differential equation and then distributionally on the completion. Its measure is the Lebesgue measure in (6.18).

There can be no irreducible discrete Hilbert summand in this space. Such a summand has nonzero smooth finite vectors and a scalar real Casimir: the general adelic unitary admissibility and scalar-Casimir argument were proved in Lesson 3, Sections 2–3. Apply the equivariant isometry to a nonzero such vector. Its data would have to satisfy
\((1/4+t^2-\lambda)F_b(t)=0\) for almost every \(t\). The zero set in the real line is finite or empty, hence has Lebesgue measure zero. It cannot support a nonzero \(L^2\) family. This is a contradiction.

The cuspidal summand is already a Hilbert sum of irreducibles with finite multiplicity by Lesson 4, Theorem 5.2, and each residual line is a one-dimensional irreducible representation. Consequently all noncuspidal discrete contributions are exactly the lines in (6.14). This proves residual exhaustion and closes the earlier residue-generation step without a general Langlands spectral theorem as an input.

A single \(E_{it}\) is generally not in \(H(\omega)\): its constant terms have size \(y^{1/2}\), whose square gives \(dy/y\). The packets in (6.20), and their completion, supply the continuous Hilbert representation. At level one and trivial compact data, the residual projection is
\[
P_{\mathrm{res}}h=\frac3\pi\langle h,1\rangle\,1.
\tag{6.3}
\]
The full-axis continuous measure is \(dt/(4\pi)\), as the proof above shows. Other adelic quadratic determinant characters occur at their appropriate ramified levels; the compact-invariant level-one residual part has only the constant line.

The historical general spectral theorem is Getz–Hahn, Theorem 10.4.1 and equations (10.11)–(10.16), or Labesse, Theorems 12.2.10.2–.5. Langlands's Appendix IV supplies the rank-one Maass–Selberg mechanism. Sections 6.1–6.5 give its complete fixed-central-character GL₂ over \(\mathbf Q\) proof here, with every finite level and real compact type, the exact Weyl factor, and all residual characters.

## 7. Exercises and complete solutions

**Exercise 7.1 — easy.** At an unramified finite place compute the intertwiner on the spherical vector for arbitrary unitary \(\chi_1,\chi_2\). Specify both its scalar and its output space.

**Solution 7.1.** Normalize additive integral-ring mass to one, and put \(A=\chi_1(\varpi)\chi_2(\varpi)^{-1}\). The integral-ring part has value one. On the shell \(|x|=q^m\), Iwasawa diagonals contribute \(A^mq^{-m(2s+1)}\) and additive measure contributes \((1-q^{-1})q^m\). The sum is
\[
1+(1-q^{-1})\sum_{m\geq1}(Aq^{-2s})^m
 =\frac{1-q^{-1}Aq^{-2s}}{1-Aq^{-2s}},
\tag{7.1}
\]
converging for \(\operatorname{Re}s>0\) since \(|A|=1\), and continuing rationally in \(q^{-2s}\). The output is right \(K_v\)-fixed and lies in \(I_v(\chi_2,\chi_1,-s)\) by (2.5). That fixed space is one-dimensional; its vector equal to one at the identity therefore has the displayed scalar multiplier. For trivial characters this is \((1-q^{-1-2s})/(1-q^{-2s})\), not its reciprocal.

**Exercise 7.2 — medium.** Recover the complete classical Fourier expansion with leading term \(y^u\) from the adelic one. Account for the missing rational noninteger frequencies and every factor of \(\pi\), \(y\), and \(n\).

**Solution 7.2.** Take \(s=u-1/2\). A rational frequency with a denominator has negative valuation at some prime and hence zero local factor by (3.4)–(3.5). For an integer \(n\ne0\), multiply (3.6) to obtain
\(\zeta(2u)^{-1}|n|^{u-1}\sigma_{1-2u}(|n|)\). Multiply this by (3.7), whose scalar is
\(2\pi^u|n|^{1/2}\sqrt y/\Gamma(u)\). Since
\(\Lambda(2u)=\pi^{-u}\Gamma(u)\zeta(2u)\), the coefficient becomes
\(2\sqrt y\,|n|^{u-1/2}\sigma_{1-2u}(|n|)K_{u-1/2}(2\pi|n|y)/\Lambda(2u)\).
The two Bruhat cells give the zero coefficient. Thus
\[
\begin{aligned}
E(z,u)
 &=y^u+\frac{\Lambda(2u-1)}{\Lambda(2u)}y^{1-u}\\
 &\quad+\frac{2\sqrt y}{\Lambda(2u)}
    \sum_{n\ne0}|n|^{u-1/2}\sigma_{1-2u}(|n|)
               K_{u-1/2}(2\pi|n|y)e^{2\pi inx}.
\end{aligned}
\tag{7.2}
\]
The Gaussian calculation (3.8)–(3.10) derives its Bessel factor. The normal-convergence estimate in Theorem 4.1 justifies this formula after continuation, away from poles, and after clearing poles at every parameter. This is the fully computed classical comparison, with the declared half-unit shift.

**Exercise 7.3 — medium.** Show that the residue at \(s=1/2\) is constant for trivial spherical data, and calculate it. Explain why the full residual space with trivial central character can nevertheless have other lines.

**Solution 7.3.** In (4.5) both \(A\)-terms are entire, and the only pole at \(u=1\) is \(1/(2u-2)\), with residue \(1/2\). Division by \(\Lambda(2u)\), nonzero there, yields \(1/(2\Lambda(2))\). The value \(\Gamma_{\mathbb R}(2)=1/\pi\) and \(\zeta(2)=\pi^2/6\) give \(3/\pi\). The result is independent of \(z\); determinant decomposition extends this to every adelic \(g\). In (3.12) one can check it termwise: \(y^{1/2+s}\) is regular, the second term has residue \((3/\pi)y^0\), and the nonzero Fourier coefficients are regular because their denominator is \(\Lambda(2)\). Twisting by any quadratic Hecke character \(\chi\) gives residue \((3/\pi)\chi(\det g)\) and central character \(\chi^2=1\). Such ramified lines belong to the full residual space even though they are absent from its everywhere compact-invariant classical part.

**Exercise 7.4 — hard.** Prove \(E(g,M(s)f_s)=E(g,f_s)\) for everywhere spherical data. Track the exchanged characters and reflected parameter, including a ratio norm twist.

**Solution 7.4.** First remove a common determinant character and consider trivial inducing characters. Proposition 2.2 computes \(M(s)f_s^0=c(s)f_{-s}^0\). Mellin integration of the determinant-one lattice theta sum yields (4.4), with \(u=s+1/2\); splitting it at one and using Poisson gives (4.5). Reflection \(u\mapsto1-u\), which is \(s\mapsto-s\), leaves that expression unchanged. Therefore (4.6) holds. Tate's equality \(\Lambda(1-2s)=\Lambda(2s)\) then gives
\[
E(g,f_s^0)=\frac{\Lambda(2s)}{\Lambda(1+2s)}E(g,f_{-s}^0)
                              =E(g,M(s)f_s^0).
\tag{7.3}
\]
The proof initially used absolutely convergent sums and integrals, and (4.5) supplies their meromorphic continuation. It therefore proves the equality even when cancellation of zeros and poles is needed; separate values of its factors need not exist. Applying the reflection twice gives (4.7). Equivalently, (4.8) checks every nonzero Fourier coefficient while the two constant terms are exchanged.

For general everywhere unramified characters write
\(\chi_1=\lambda|\cdot|^{i\tau/2}\) and
\(\chi_2=\lambda|\cdot|^{-i\tau/2}\). The section is
\(\lambda(\det g)f_\sigma^0(g)\), where \(\sigma=s+i\tau/2\). The intertwiner has scalar \(c(\sigma)\); its output belongs to \(I(\chi_2,\chi_1,-s)\). In the swapped data the ratio exponent is \(-\tau\), so its shifted parameter is \(-s-i\tau/2=-\sigma\). Multiplying (7.3), with \(s\) replaced by \(\sigma\), by \(\lambda(\det g)\) proves the required identity with exactly this output space. It also places the positive pole at \(s=1/2-i\tau/2\), with residue proportional to \(\lambda\circ\det\). Keeping \(s\) fixed while swapping only the characters would give the wrong equation.

## 8. What this lesson does not prove

- Rational Iwasawa and determinant decomposition, compact quotient integration, and finite volume are imported from Lesson 1, Theorems 4.1–4.2 and Section 5. Normalized induction and its unitary compact model are Lesson 6, Section 1. Cuspidal rapid decay and its discrete Hilbert sum are Lesson 4, Theorems 4.2 and 5.2. Fourier inversion on the finite-level additive quotient is the circle argument of Lesson 14, Theorem 1.1; we explained its retained constant coefficient here.
- Self-dual additive Poisson summation is NT-ADL-05, Theorems 5.4–5.5, and the rational compact norm-fibre normalization and one-dimensional Tate continuation are NT-ADL-09, its theta lemma, Lemma 9.3, Theorem 9.2, and equations (25)–(28). We proved the two-dimensional Eisenstein application, the shell and Gaussian transforms, and the boundary nonvanishing needed here. The classical prerequisite Non-holomorphic Eisenstein series and Maass forms, equation (1.4), Theorems 1.1, 2.2 and 3.2, and Corollary 3.3, is published. Equation (3.2) and Solution 7.2 identify its parameter and normalization with the adelic construction here; the local Whittaker, intertwining and tensor-product calculations remain the arguments of this lesson.
- Theorems 4.2–4.3 and Section 6 prove the general ramified functional equation and unitary scattering, full spectral completeness, exact Plancherel measure and residual exhaustion over \(\mathbf Q\), for every finite level, real compact type and unitary central character. General adelic unitary admissibility, smooth finite vectors and scalar Casimir are supplied by Lesson 3, Section 2 and Theorem 3.2; Section 6.5 uses their already proved statements to exclude discrete summands in the continuous data. Getz–Hahn, Theorem 10.4.1, Labesse, Theorems 12.2.10.2–.5, and Langlands, Appendix IV, retain historical credit for the general theorem and the rank-one mechanism. The proof here passes from compact parabolic tests through the four-term Maass–Selberg bound, the contour residue projection, and an onto Hilbert isometry; it imports no spectral-completeness or residue-generation theorem.
- Jacquet–Langlands, Theorem 10.10, is a classification of noncuspidal automorphic constituents in principal series. It is not a source theorem for the analytic continuation asserted in the outline. Langlands's Appendix IV treats a one-cusp Fuchsian, right-compact-invariant case by resolvents and the Maass–Selberg relation; its parameter \(\lambda\) is \(2s\), with \(y=\alpha^2\). The complete assigned source scopes provide the general background, while the proofs above use the declared adelic normalizations.

## References

- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), April 22, 2022 draft, §§10.1–10.4, especially Proposition 10.2.2, Theorems 10.2.3 and 10.3.2, Proposition 10.3.1, and Theorem 10.4.1. The published book appeared in 2024; these locators refer to the consulted draft.
- J.-P. Labesse, “The Langlands spectral decomposition,” in *The Genesis of the Langlands Program*, Cambridge University Press, 2021, Chapter 12, especially (12.2.9.2), Theorems 12.2.10.1–12.2.10.5, §§12.3.3–12.3.5, and (12.4.2.1).
- R. P. Langlands, [*On the Functional Equations Satisfied by Eisenstein Series*](https://publications.ias.edu/rpl/paper/39), Lecture Notes in Mathematics 544, Springer, 1976, Appendix IV, “The simplest case,” pp. 219–228 in the IAS retypeset edition.
- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §10, Theorem 10.10, for the constituent comparison described above.

# Polynomial and contour interfaces for stable boundary models

Stable modes of a boundary model require polynomial projections and contour moments at every nilpotent pole order. This lesson establishes those tools; [Stable modes and the algebra of boundary data](stable-boundary-models.md) applies them.

Section 13 of [Metric and topological foundations](metric-foundation-bridges.md#original-scalar-calculus-and-its-finite-coordinate-receivers) proves the full original scalar and finite-coordinate calculus. Its Section 13.12 gives the exact Gaussian, Rayleigh, logarithmic-contour, matrix and half-line receiving maps, retaining every original factor, endpoint and norm.

The complete original real-number, compactness, extrema and finite-norm proofs are in Section 12 of [Metric and topological foundations](metric-foundation-bridges.md#real-numbers-and-finite-dimensional-topology). Its Section 12.10 gives the exact receiving minimum and spectral-contour maps; the original coordinates, norms and constants are retained.

The route has three steps: scalar polynomial division and Bézout give finite algebraic projections; triangularization gives Cayley–Hamilton without using those projections; and directly integrated power series give the contour moments needed for every nilpotent pole order. This last step concerns globally convergent power-series numerators. It does not assert a Cauchy theorem for arbitrary holomorphic functions on arbitrary domains.

## 1. Facts used from earlier lessons

We use the entry facts from [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md), including real multivariable calculus, Taylor's formula, smooth compact cutoffs, absolutely integrable change of variables and Fubini, dominated convergence and differentiation, Cauchy–Schwarz, real completeness, finite-dimensional compactness, and the stated Schwartz-space and continuous-dual conventions. This companion needs only the following finite algebra and calculus part of that base, with elementary conventions made explicit.

Sections 10.1--10.9 prove the following finite algebra facts at the stated real/complex scalar base: field arithmetic over \(\mathbb C\); finite polynomial arithmetic and induction on degree; basis extension, rank-nullity and direct sums in finite dimension; matrix multiplication, inverses, adjoints and operator norms; determinant multiplicativity, triangular and block-triangular determinants, elementary row operations, the characteristic-polynomial eigenvalue criterion and invariance under change of basis; continuity of determinants and matrix inversion; and trace and rank for projections. Sections 9.1--9.4 prove complex-root existence and full finite factorization with the original leading coefficient and all multiplicities. Sections 9.6--9.7 prove determinant identities, the actual root-to-kernel map and both invariant quotient constructions used below. Section 10.10 proves their exact receiving maps for the earlier spectral and metric arguments. No Jordan decomposition is assumed.

The calculus requirements are the real chain rule and fundamental theorem of calculus on compact intervals, the elementary derivatives of the real logarithm and arctangent, the scalar exponential series, locally uniform power-series calculus, and differentiation or integration of series when the differentiated series converge uniformly on the compact set in question. Ordinary piecewise \(C^1\) path integration is defined below by real parametrization. Sections 11.1--11.4 prove matrix-entry dominated differentiation, its original operator-norm comparison and its exact piecewise path integral; Section 11.5 gives the full ordered resolvent and time-derivative receivers. These are the elementary facts used in the arguments below. In particular, the rule allowing termwise differentiation does not include an unstated theorem that every holomorphic function has a global power series.

## 2. Scalar polynomial division and Bézout

For a field \(F\), \(f,g\in F[z]\) and \(g\ne0\), the division interface supplies unique polynomials \(q,r\) such that
\[
f=gq+r,\qquad r=0\quad\hbox{or}\quad\deg r<\deg g.
\]
For \(p,q\in F[z]\) not both zero, the Bézout interface supplies a unique monic greatest common divisor \(d\) and polynomials \(a,b\) with
\[
d=ap+bq.
\]
Here \(d\) divides both \(p,q\), and every common divisor divides \(d\). In particular, relatively prime polynomials have a combination equal to \(1\). We use these assertions with \(F=\mathbb C\).

**Proof of division.** Let \(e=\deg g\) and let \(b\ne0\) be its leading coefficient. If \(f=0\) or \(\deg f<e\), take \(q=0\) and \(r=f\). Otherwise let \(d=\deg f\), with leading coefficient \(a\ne0\), and subtract \((a/b)z^{d-e}g\) from \(f\). The leading terms cancel, so the difference is zero or has degree strictly below \(d\). Repeating this step terminates because the degree of a nonzero remainder decreases at every step. The sum of the subtracted monomials is \(q\), and the final difference is the required \(r\). This includes a constant divisor and the zero dividend. If \(f=gq+r=gq'+r'\) with both remainders zero or of degree below \(e\), then \(g(q-q')=r'-r\). A nonzero left side has degree at least \(e\), whereas the right side is zero or has degree below \(e\). Therefore \(q=q'\) and \(r=r'\).

**Proof of Bézout and the gcd claim.** The set of combinations \(ap+bq\), with \(a,b\in F[z]\), contains a nonzero polynomial because \(p,q\) are not both zero. Keep a least-degree nonzero combination \(\delta=a^{(0)}p+b^{(0)}q\) with its original leading coefficient \(\kappa\ne0\). Divide each original polynomial by \(\delta\), using the full pivot coefficient \(\kappa\) in the division step proved above. The remainder is still a combination and has smaller degree; it must therefore be zero. Thus \(\delta\) divides both polynomials and every common divisor divides \(\delta\). Define the comparison name \(d=\kappa^{-1}\delta\), retaining the identity \(\delta=\kappa d\) and the full Bézout coefficients \(\kappa^{-1}a^{(0)},\kappa^{-1}b^{(0)}\). Formula (CR13) proves this exact scalar-unit map and its inverse. Consequently \(d\) has the same ideal and divisibility properties. For example dividing \(p\) by \(d\) has zero remainder: both \(p,q\) belong to the original combination ideal and the divisor \(d\) is its displayed nonzero unit comparison. The same map proves that \(d\) divides \(q\). Every common divisor of \(p,q\) divides the original combination and hence divides \(d\). The chosen representation of \(d\) is the Bézout identity. If another monic polynomial has the same gcd property, each divides the other; both quotients have degree zero and monicity makes them \(1\). This proves uniqueness, including when exactly one of \(p,q\) is zero. The excluded pair \((0,0)\) has no monic greatest common divisor under this convention.

Thomas W. Judson, [*Abstract Algebra: Theory and Applications*, polynomial division](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/poly.xml#L307-L390), proves scalar division; the same chapter's [gcd proposition](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/poly.xml#L590-L676) proves Bézout. The two details below specify the cases used here.

Two details in the division and gcd proofs matter here. The original nonzero element of the linear-combination ideal remains the working divisor. Its monic comparison retains the full leading coefficient and inverse in (CR14). Uniqueness of the monic gcd follows from mutual divisibility: the quotient is constant by degree, and monicity makes it \(1\). Monicity and equality of degrees alone would not prove equality. The pair \((0,0)\) is excluded from this monic-gcd contract. The division assertion includes the zero dividend and a nonzero constant divisor, and does not assign a degree to the zero remainder.

This is scalar division. The typed division \(B=Qp+R\) for a monic \(\operatorname{End}(E)\)-valued polynomial \(p\) and a \(\operatorname{Hom}(E,G)\)-valued polynomial \(B\) is proved separately in [Stable modes and the algebra of boundary data](stable-boundary-models.md), Problem 3. That argument keeps \(Q\) on the left and preserves every coefficient order; it is not an application of the scalar reading to a noncommutative coefficient ring.

## 3. From coprime factors to projections

Let \(h_1,\ldots,h_r\in\mathbb C[z]\) be pairwise relatively prime nonconstant polynomials, with \(r\geq1\), and put
\[
H=\prod_{j=1}^r h_j,\qquad H_j=\prod_{k\ne j}h_k.
\]
There are polynomials \(e_j\) such that
\[
e_j\equiv1\pmod {h_j},\qquad e_j\equiv0\pmod {h_k}\quad(k\ne j),
\]
and
\[
\sum_j e_j\equiv1\pmod H,\qquad
e_j^2\equiv e_j\pmod H,\qquad e_je_k\equiv0\pmod H\quad(j\ne k).
\]
If \(A\in\operatorname{End}(V)\) satisfies \(H(A)=0\), the maps \(E_j=e_j(A)\) are commuting projections whose pairwise products are zero and whose sum is \(I_V\). They give the direct sum
\[
V=\bigoplus_{j=1}^r\ker h_j(A),\qquad
\operatorname{im}E_j=\ker h_j(A).
\]

**Proof.** First \(h_j\) and \(H_j\) are relatively prime. For each \(k\ne j\), choose \(u_kh_j+v_kh_k=1\) by Bézout. Multiply these finitely many identities. The term using every \(v_kh_k\) is \((\prod_{k\ne j}v_k)H_j\); every other term has a factor \(h_j\). Grouping those terms gives an identity
\[
a_jh_j+b_jH_j=1.
\]
For \(r=1\), this is simply \(0h_1+1\cdot1=1\). Set \(e_j=b_jH_j\). Its stated individual congruences follow immediately.

We also need divisibility by the whole product. If \(u,v\) are coprime, \(u\mid vw\) implies \(u\mid w\): multiply \(au+bv=1\) by \(w\). Consequently, if both \(u\) and \(v\) divide \(f=uw\), then \(v\mid w\) and \(uv\mid f\). Multiplying Bézout identities as above shows that any subproduct of the \(h_j\) is coprime to the next factor. Induction now proves that divisibility by each \(h_j\) implies divisibility by \(H\). Apply this to \(\sum_j e_j-1\), \(e_j^2-e_j\) and \(e_je_k\), whose remainders modulo every factor vanish.

Evaluation of scalar polynomials at one operator preserves sums and products: expansion of a product gives the same finite coefficient sum because powers of \(A\) commute. Multiples of \(H\) therefore evaluate to zero. This proves the projection identities. Further, \(h_je_j=b_jH\), so \(h_j(A)E_j=0\) and \(\operatorname{im}E_j\subseteq\ker h_j(A)\). If \(h_j(A)v=0\), evaluating \(1-e_j=a_jh_j\) on \(v\) gives \(v=E_jv\), proving the reverse inclusion. The sum identity represents every vector as a sum from the images. If \(\sum_jv_j=0\) with \(v_j\in\operatorname{im}E_j\), applying \(E_k\) gives \(v_k=0\); the sum is direct. This proves every assertion.

The empty list is relevant only with \(H=1\). The hypothesis \(H(A)=0\) then says \(I_V=0\), so \(V=0\); the empty direct sum and empty sum of projections give exactly that zero space. Powers of distinct linear factors are pairwise coprime: otherwise a nonconstant common divisor has a complex root, which would have to be both distinct roots. No square-free or simple-root assumption has been made.

## 4. Cayley–Hamilton from an invariant flag

Every endomorphism of a finite-dimensional complex vector space has an upper-triangular matrix in some basis; see [Robert A. Beezer, *A First Course in Linear Algebra*, Theorem UTMR](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-OD.xml#L108-L201). The zero-dimensional case is the empty basis. Section 9.7 proves both exact routes from the original eigenvalue: the invariant range of \(A-\lambda I\) and the eigenline quotient used in the proof below. Both retain their full coordinate changes and block determinants. The induction uses rank-nullity and basis extension and does not depend on Cayley–Hamilton or a primary decomposition.



**Proof of triangularization.** Induct on \(n=\dim V\). For \(n=0\) the empty basis works. For \(n>0\), the complete proof in Sections 9.1--9.4 gives a root \(\lambda\) of \(\det(zI-A)\), so the exact free-coordinate kernel map (CR19) gives a nonzero eigenvector of \(A\), which we denote by \(v_1\). Its span is invariant. The induced operator on the quotient by this line acts on a space of dimension \(n-1\); by induction choose an upper-triangular quotient basis and lift its vectors in order to \(v_2,\ldots,v_n\). For each \(j>1\), upper triangularity in the quotient says that \(Av_j\) is a linear combination of \(v_1,\ldots,v_j\). The same is true for \(Av_1=\lambda v_1\). Thus the lifted basis makes \(A\) upper triangular. The induction uses neither Cayley–Hamilton nor a primary decomposition.

For every finite-dimensional complex vector space \(V\) and \(A\in\operatorname{End}(V)\), set
\[
\chi_A(z)=\det(zI_V-A).
\]
Then \(\chi_A(A)=0\), with no restriction on eigenvalue multiplicities, diagonalizability or invertibility.

**Proof.** Let \(n=\dim V>0\), choose the triangular basis \(v_1,\ldots,v_n\), and let its diagonal entries be \(\lambda_1,\ldots,\lambda_n\). Put \(V_j=\operatorname{span}(v_1,\ldots,v_j)\), including \(V_0=0\). Upper triangularity says \(AV_j\subseteq V_j\). More precisely,
\[
(A-\lambda_j I)V_j\subseteq V_{j-1}.
\]
Indeed, on \(v_j\) subtracting \(\lambda_jv_j\) removes the last possible coordinate; on each earlier basis vector both terms already lie in \(V_{j-1}\).

For \(v\in V_n\), apply the factor \(A-\lambda_n I\) first, then \(A-\lambda_{n-1}I\), and continue downward. The intermediate vectors lie successively in \(V_{n-1},V_{n-2},\ldots,V_0\). Thus
\[
(A-\lambda_1I)\cdots(A-\lambda_nI)v=0.
\]
All factors are polynomials in \(A\) and hence commute. The triangular determinant identity gives
\[
\chi_A(z)=\prod_{j=1}^n(z-\lambda_j),
\]
so the vanishing product is exactly \(\chi_A(A)\). Both determinant and polynomial evaluation commute with change of basis, and the result holds for the original operator. If \(n=0\), the determinant is \(1\); evaluation gives \(I_V\), which is the zero endomorphism of the zero space. This proves that case as well. The characteristic polynomial is the actual \(\det(zI-A)\). Its leading coefficient is computed from every original permutation term in (CR17); the full sign comparison with \(\det(A-zI)\) is (CR18).

For completeness, this gives the exact minimal-polynomial interface used next in [Stable modes and the algebra of boundary data](stable-boundary-models.md). There is a nonzero annihilating polynomial, namely \(\chi_A\). Keep an original least-degree nonzero annihilator \(m\) and its original leading coefficient \(c_m\ne0\). Formula (CR15) records its exact comparison with the named monic polynomial \(\mu_A\): \(m=c_m\mu_A\). For any annihilator \(f\), divide by the original \(m\), with its full leading coefficient, rather than using \(\mu_A\) as a replacement. The remainder also annihilates \(A\), so it is zero by minimality. Consequently the original annihilator divides every other one. The exact inverse scalar-unit map in (CR13)--(CR15) proves the corresponding divisibility and uniqueness assertion for \(\mu_A\). In the zero space it is \(1\). In positive dimension it is nonconstant, since a nonzero constant evaluates to a nonzero scalar identity. Sections 9.1--9.4 factor the original \(m=c_mH\) into distinct linear powers with every multiplicity retained. Formula (CR16) applies Section 3 through the actual quotient \(M_j=m/h_j=c_mH_j\); each projection keeps both \(c_m\) and its inverse in its full evaluation. The order of these steps avoids using primary decomposition to prove the Cayley–Hamilton prerequisite for that same decomposition.

## 5. Contour moments from entire series

A piecewise \(C^1\) path is a continuous map \(\gamma:[a,b]\to\mathbb C\) that is \(C^1\) on each of finitely many subintervals, with the usual one-sided endpoint derivatives. For a continuous function along it, define
\[
\int_\gamma f(z)\,dz=\sum_{\text{pieces}}\int f(\gamma(s))\gamma'(s)\,ds.
\]
A cycle \(\Gamma\) here is a finite integer linear combination of such closed paths. Its integrals are the corresponding finite linear combinations. If \(\zeta\) avoids their union, define
\[
\operatorname{ind}_\Gamma(\zeta)
=\frac{1}{2\pi i}\int_\Gamma\frac{dz}{z-\zeta}.
\]
No general winding-number or homology theorem is needed to make this definition. The indices for the contours we construct will be computed below.

We first record the primitive rule in the form needed here. If a single-valued function \(F\) along a path's neighborhood has a derivative satisfying
\(\frac{d}{ds}F(\gamma(s))=f(\gamma(s))\gamma'(s)\)
on every piece, real integration of its real and imaginary parts gives
\[
\int_\gamma f(z)\,dz=F(\gamma(b))-F(\gamma(a)).
\]
The intermediate endpoints cancel because both \(F\) and \(\gamma\) are continuous. Every closed-path integral of such a derivative vanishes. In particular, for any integer \(\ell\ne-1\), the function \((z-\zeta)^{\ell+1}/(\ell+1)\) is a single-valued primitive of \((z-\zeta)^\ell\) on \(\mathbb C\setminus\{\zeta\}\). This uses ordinary integer powers and the real chain rule, including negative powers.

Suppose explicitly that
\[
\phi(z)=\sum_{r=0}^\infty c_r(z-\zeta)^r
\]
is a power series converging on all of \(\mathbb C\), locally uniformly. Then for every integer \(k\geq0\) and every cycle avoiding \(\zeta\),
\[
\frac{1}{2\pi i}\int_\Gamma
\frac{\phi(z)}{(z-\zeta)^{k+1}}\,dz
=\operatorname{ind}_\Gamma(\zeta)\frac{\phi^{(k)}(\zeta)}{k!}.
\]

**Proof.** The paths have compact union and finite total length after weighting by the absolute values of the integer coefficients. Their distance from \(\zeta\) is positive. Dividing the locally uniform series by \((z-\zeta)^{k+1}\) therefore preserves uniform convergence on that union. For any continuous \(g\), the absolute value of its integral is at most this weighted length times \(\sup|g|\), so the series may be integrated term by term. The primitive rule kills every term except \(r=k\). That remaining term is \(c_k\operatorname{ind}_\Gamma(\zeta)\).

Here is the coefficient-derivative justification, independent of a holomorphic Cauchy theorem. Choose \(0<R<R'\). Convergence at \(z-\zeta=R'\) bounds the sequence \(|c_r|(R')^r\) by a finite constant. For every fixed derivative order \(j\), the terms of the formally differentiated series on \(|z-\zeta|\leq R\) are consequently bounded by a constant times \(r^j(R/R')^r\). This numerical series converges: the ratio of successive terms tends to \(R/R'<1\). Hence the derivative series converges uniformly there, and the entry-base termwise differentiation rule applies, repeatedly. Evaluation at \(z=\zeta\) gives \(\phi^{(k)}(\zeta)=k!c_k\), completing the proof.

For any \(a\in\mathbb C\), the exponential series gives
\[
\frac{1}{2\pi i}\int_\Gamma
\frac{e^{az}}{(z-\zeta)^{k+1}}\,dz
=\operatorname{ind}_\Gamma(\zeta)e^{a\zeta}\frac{a^k}{k!}.
\]
Indeed \(e^{az}=e^{a\zeta}\sum_{r\geq0}a^r(z-\zeta)^r/r!\); the exponential addition identity follows by the absolutely convergent product of its two series and the binomial formula. Constants and finite polynomials times exponentials also have the required series about every \(\zeta\). This includes \(1\), \(e^{itz}\) and \(z^j e^{itz}\) for every \(j\geq0\) and every real \(t\). Matrix-valued finite sums are handled entrywise. In [Stable modes and the algebra of boundary data](stable-boundary-models.md) the resolvent is explicitly decomposed into finitely many nilpotent principal parts, so all pole orders are covered by the formula above; a general residue theorem adds nothing to that calculation.

The phrase “encloses a spectral point once” means precisely index \(1\) at that point; “excludes” means index \(0\). These conditions, rather than an implicit picture of a contour, govern the matrix projection formula. This theorem says nothing about a merely holomorphic numerator lacking the asserted global series. A later need for a more general Cauchy theorem remains a separate prerequisite.

Jiří Lebl, [*Guide to Cultivating Complex Analysis*, version 1.9](https://github.com/jirilebl/ca/blob/adfaaf8b13287185c22db079f16f39183628f482/ca.tex), gives a related treatment of line integrals and winding numbers. The primitive rule and exact contour moments required here have been proved above; the stronger disk and general-cycle theorems are not used.

## 6. Indices of rectangles and circles

Let \(a<b\), \(c<d\), and let \(\partial R\) be the positively oriented boundary of the closed rectangle
\[
R=\{x+iy:a\leq x\leq b,\ c\leq y\leq d\}.
\]
For every \(\zeta\notin\partial R\),
\[
\operatorname{ind}_{\partial R}(\zeta)=
\begin{cases}
1,&\zeta\in\operatorname{int}R,\\
0,&\zeta\notin R.
\end{cases}
\]

**Proof for an interior point.** Translate \(\zeta\) to zero. Write the positive distances to the left, right, bottom and top sides as \(A,B,C,D\), respectively. The translated rectangle is \([-A,B]\times[-C,D]\). For each angle \(\theta\), take the applicable positive numbers in the following list:
\[
\frac{B}{\cos\theta}\ (\cos\theta>0),\qquad
\frac{A}{-\cos\theta}\ (\cos\theta<0),\qquad
\frac{D}{\sin\theta}\ (\sin\theta>0),\qquad
\frac{C}{-\sin\theta}\ (\sin\theta<0).
\]
Let \(r(\theta)\) be their minimum. At least one number is applicable. The inequalities defining the rectangle say exactly that its intersection with this ray is the segment of radii \(0\leq\rho\leq r(\theta)\). Thus \(r(\theta)e^{i\theta}\) is its unique boundary point on the ray.

The active side changes only at the four corner directions. On an interval between corner directions, the relevant displayed quotient is smooth with a nonzero denominator. Near an axis, a quotient with denominator tending to zero cannot be the minimum because the other applicable quotient stays bounded. At a corner the two active quotients have the same positive value. These facts prove that \(r\) is positive, continuous, \(2\pi\)-periodic and piecewise \(C^1\). They also give a finite partition on which its parametrization is smooth.

As \(\theta\) increases by \(2\pi\), these boundary points traverse each of the four sides once in positive order. To check the orientation directly, on the right side the height is \(B\tan\theta\) and increases; on the top side the horizontal coordinate is \(D\cot\theta\) and decreases; on the left side the height is \(-A\tan\theta\) and decreases; on the bottom side the horizontal coordinate is \(-C\cot\theta\) and increases. On each relevant angular interval these are monotone parametrizations of the corresponding full side or its part split at the starting ray. The real change-of-variable rule therefore identifies this radial integral with the usual positively oriented rectangle integral.

On every smooth piece, with \(\gamma(\theta)=r(\theta)e^{i\theta}\),
\[
\frac{\gamma'(\theta)}{\gamma(\theta)}
=\frac{r'(\theta)}{r(\theta)}+i.
\]
The integrals of \(r'/r\) are real logarithm differences. They telescope across the finitely many endpoints and total zero because \(r(2\pi)=r(0)\). The integral of \(i\) is \(2\pi i\). Division by \(2\pi i\) proves the index is \(1\).

**Proof for an exterior point.** If \(\zeta\notin R\), at least one real coordinate lies strictly outside the corresponding closed interval. Translate by \(-\zeta\), then multiply by some \(\alpha\in\{1,-1,i,-i\}\) so that the entire translated rectangle lies in the open right half-plane. For \(w=x+iy\) with \(x>0\), define the single-valued function
\[
L(w)=\tfrac12\log(x^2+y^2)+i\arctan(y/x).
\]
Real differentiation gives \(L_x=1/w\) and \(L_y=i/w\). Hence along any piecewise \(C^1\) path \(w(s)\) in that half-plane, \(\frac{d}{ds}L(w(s))=w'(s)/w(s)\). With \(w(s)=\alpha(\gamma(s)-\zeta)\), this is \(\gamma'(s)/(\gamma(s)-\zeta)\). The primitive rule gives zero around the closed rectangle. This proves the exterior case. Points on its boundary were excluded because the integrand would be singular there.

For clarity, a positively oriented circle of center \(c_0\) and radius \(R_0>0\) has the same inside/outside index rule. Put \(w=\zeta-c_0\) and parametrize by \(c_0+R_0e^{i\theta}\). If \(|w|<R_0\), the integrand with its parameter differential is
\[
\frac{i}{1-(w/R_0)e^{-i\theta}}\,d\theta
=i\sum_{n\geq0}(w/R_0)^n e^{-in\theta}\,d\theta.
\]
Uniform geometric convergence permits integration; only the constant term remains, giving \(2\pi i\). If \(|w|>R_0\), write it instead as
\[
-i\sum_{n\geq1}(R_0/w)^n e^{in\theta}\,d\theta;
\]
every term integrates to zero. The elementary exponential integrals follow from their explicit primitives. Boundary points are again excluded. Reversing any contour's orientation negates the index, and taking integer sums adds indices, directly from the definition.

## 7. Differentiation along a fixed contour

Let \(Y\subseteq\mathbb R^d\) be open, let \(A:Y\to\operatorname{End}(V)\) be \(C^r\), where \(r\) is a nonnegative integer or \(\infty\), and let \(\Gamma\) be a fixed finite cycle with \(zI-A(y)\) invertible for all its points and all \(y\in Y\). Then
\[
R(y,z)=(zI-A(y))^{-1}
\]
is continuous on \(Y\) times the contour and is \(C^r\) in \(y\). Integration over \(\Gamma\) commutes with these parameter derivatives. In particular,
\[
\partial_{y_j}R=R(\partial_{y_j}A)R,
\]
with the order of the three factors as displayed. For a nonzero multi-index \(\beta\) of order at most \(r\), repeated differentiation gives the useful recursive identity
\[
\partial^\beta R
=\sum_{0<\eta\leq\beta}\binom\beta\eta
R(\partial^\eta A)(\partial^{\beta-\eta}R).
\]

**Proof.** Continuity follows from continuity of inversion. On any compact parameter box inside \(Y\), its product with the finite contour is compact, so the inverses have a common bound. The inverse is differentiable wherever the matrix is invertible, as follows either by the adjugate divided by the nonzero determinant or by the inverse difference identity. Differentiating \((zI-A)R=I\) once and multiplying on the left by \(R\) gives the first formula. Applying the multi-index product rule and isolating the term with no derivative on \(zI-A\) gives the recursive formula. Induction shows all derivatives exist, are continuous and are bounded on the compact product. After parametrizing every path piece, these bounds times \(|\gamma'|\) are integrable majorants. The complete matrix-entry dominated-differentiation theorem in Section 11.2, applied by the exact path comparison in Section 11.4, proves this interchange coordinate by coordinate and at every derivative order. For \(r=0\), uniform continuity on compact products gives continuity of the integral directly. For \(r=\infty\), use every finite order in turn.

The same reasoning applies to multiplication by \(e^{itz}\), for \(t\) in a compact real interval, and to all of its time derivatives \((iz)^j e^{itz}\). On a fixed compact contour they are bounded uniformly for bounded \(t\). On an upper contour with \(\operatorname{Im}z\geq\delta>0\), their absolute values for \(t\geq0\) are at most \(|z|^j e^{-\delta t}\). Ordered products of parameter derivatives of the resolvent require this integration estimate, not an additional evaluation theorem for holomorphic matrix functions.

Here is the exact contour-existence boundary used in [Stable modes and the algebra of boundary data](stable-boundary-models.md). Let \(K\) be a compact parameter set, let \(A\) be continuous on it, and suppose no \(A(y)\) has a real eigenvalue. If \(K=\varnothing\), any rectangle lying strictly above the real axis satisfies the contour requirements on \(K\) vacuously, and the empty neighborhood suffices for the neighborhood assertion below. Assume now \(K\ne\varnothing\), and let \(M=\max_K\|A(y)\|\). Every eigenvalue satisfies \(|\lambda|\leq M\), by applying the norm inequality to an eigenvector. There is also a uniform positive distance \(\varepsilon\) from all those eigenvalues to the real axis. Otherwise a sequence of parameters and eigenvalues has, by compactness and the bound \(M\), a subsequence tending to \(y_*\in K\) and a real \(\lambda_*\); continuity of \(\det(\lambda I-A(y))\) would make \(\lambda_*\) a real eigenvalue of \(A(y_*)\), a contradiction.

Choose \(R>M+1\) and \(0<\delta<\min(\varepsilon,R)\). The positively oriented rectangle with real sides \(-R,R\) and imaginary sides \(\delta,R\) has index \(1\) on every upper eigenvalue and \(0\) on every lower eigenvalue, by Section 6. It meets no spectrum and can be kept fixed over \(K\). If the family is defined on an open parameter set containing \(K\), compactness and determinant continuity preserve invertibility on this contour in some neighborhood of \(K\), allowing the preceding differentiation result there. For \(V=0\), all invertibility and contour assertions have their unique empty-dimensional meaning and any positive \(\varepsilon\) may be used. This is a compact-parameter statement. It does not claim a uniform gap on a noncompact parameter space, choose eigenvalue branches, impose semisimplicity or assert global triviality of a stable bundle.

## 8. A repeated pole and why the hypothesis matters

Consider the operator
\[
A=\begin{pmatrix}2i&1&0\\0&2i&0\\0&0&-i\end{pmatrix}
\]
and the positive rectangle with real sides \(-1,1\) and imaginary sides \(1,3\). On the first two coordinates write \(A=2iI+N\), where \(N^2=0\) and \(N\ne0\). Direct multiplication gives
\[
(zI-A)^{-1}=
\begin{pmatrix}
(z-2i)^{-1}&(z-2i)^{-2}&0\\
0&(z-2i)^{-1}&0\\
0&0&(z+i)^{-1}
\end{pmatrix}.
\]
The rectangle has indices \(1\) at \(2i\) and \(0\) at \(-i\). Its normalized resolvent integral is therefore
\[
q=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}.
\]
The double pole contributes zero to this constant-numerator integral. With numerator \(e^{itz}\), however, the \(k=1\) moment gives
\[
\frac{1}{2\pi i}\int_\Gamma e^{itz}(zI-A)^{-1}\,dz
=\begin{pmatrix}e^{-2t}&it\,e^{-2t}&0\\0&e^{-2t}&0\\0&0&0\end{pmatrix}
=e^{itA}q.
\]
The last equality can also be checked from \(e^{itN}=I+itN\), obtained by terminating the exponential series. Dropping the double-pole term would accidentally compute the projection correctly but would give the wrong evolution of the second coordinate vector. Thus a projection calculation alone does not check the treatment of Jordan multiplicities in an evolution formula.

**Exercise.** Let \(\Gamma\) be the positive rectangle with real sides \(-1,4\) and imaginary sides \(-1,1\). The function \(\phi(z)=1/(z-3)\) is holomorphic on neighborhoods of the contour and of \(0\). Compute
\[
J=\frac{1}{2\pi i}\int_\Gamma\frac{\phi(z)}z\,dz.
\]
Compare it with \(\phi(0)\), identify the failed hypothesis of Section 5, and explain why there is no contradiction with that result. Do the computation using only the rectangle indices proved here.

**Solution.** Partial fractions give
\[
\frac{1}{z(z-3)}=-\frac{1}{3z}+\frac{1}{3(z-3)}.
\]
Both \(0\) and \(3\) lie inside this rectangle, so both indices are \(1\) and \(J=-1/3+1/3=0\). On the other hand \(\phi(0)=-1/3\). The moment theorem required a globally convergent power series about \(0\), which this function does not have: its geometric expansion there has radius \(3\), and it has a pole at \(3\) inside the contour. Holomorphicity near the contour and evaluation point does not supply the missing hypothesis. No step of the computation uses a general residue theorem, and the result illustrates why the restricted prerequisite must not be advertised as an unrestricted Cauchy theorem.

## 9. Complex roots with all original coefficients retained

We now prove the complex-root fact used in Sections 1, 3, 4 and 7. The proof keeps the original polynomial and each coefficient, including its leading factor and every translated remainder. We then prove its exact maps to Bézout combinations, original annihilators, spectral projections and finite matrix kernels.

The scalar entry bases are real completeness, field arithmetic, finite polynomial arithmetic and degree induction, real differentiation and integration on compact intervals, and the finite-dimensional definitions in Section 1. Absolute convergence and the required exponential differentiation are justified directly below. No root theorem, primary decomposition or general Cauchy integral theorem is used to prove its own prerequisite.

### 9.1. The actual exponential and a direction with any prescribed integer power

Define \(E(t)=\sum_{k=0}^{\infty}(it)^k/k!\) for real \(t\). On \(|t|\leq T\) the absolute series and its first derivative are uniformly convergent: once \(k+1>2T\), the ratio of successive absolute majorants is less than \(1/2\); finitely many earlier terms and the resulting geometric tail are included. To justify the derivative rule directly, finite partial sums obey their integral derivative formula. Uniform limits of the functions and derivatives let that formula pass to the limit on every compact interval, proving \(E'=iE\). Absolute convergence, finite binomial expansion and regrouping of the double series give
\[
 E(s)E(t)=\sum_{m\geq0}i^m
       \sum_{k=0}^m\frac{s^kt^{m-k}}{k!(m-k)!}
       =\sum_{m\geq0}\frac{i^m(s+t)^m}{m!}=E(s+t).              \tag{CR1}
\]
Conjugation of the actual series gives \(\overline{E(t)}=E(-t)\); hence \(E(t)\overline{E(t)}=E(0)=1\). Put \(C(t)=\operatorname{Re}E(t)\), \(S(t)=\operatorname{Im}E(t)\). Thus
\[
 C'=-S,\quad S'=C,\quad C(0)=1,\quad S(0)=0,\quad
                         C(t)^2+S(t)^2=1.                    \tag{CR2}
\]
There is a first positive zero \(t_0\) of \(C\), and \(0<t_0<2\). For existence, its actual series gives
\(C(2)=1-2+2/3+\sum_{k\geq3}(-1)^k2^{2k}/(2k)!\leq-1/3<0\):
the remaining terms are decreasing in absolute value, and each consecutive negative/positive pair has nonpositive sum. Continuity and the intermediate value property supply a zero in \((0,2)\). The intermediate value property follows directly from real completeness. For a continuous real function \(f\) with \(f(a)>0>f(b)\), let \(c=\sup\{x\in[a,b]:f(x)>0\}\). Positivity near \(a\) and negativity near \(b\) give \(a<c<b\). Points of that set approach \(c\), so continuity gives \(f(c)\geq0\). If \(f(c)>0\), continuity supplies a point of the set strictly to its right, a contradiction. Thus \(f(c)=0\). Reversing the signs covers the other case, and subtracting a requested intermediate value covers arbitrary endpoint values. Since \(C>0\) near zero, the closed nonempty zero set in a compact subinterval has a positive infimum that belongs to it by continuity. This gives \(t_0\); another change of sign before it would have supplied an earlier zero. Therefore \(C>0\) on \([0,t_0)\).

The integral \(S(t)=\int_0^t C(s)\,ds\) is strictly positive for \(0<t\leq t_0\). Formula (CR2) gives \(S(t_0)=1\). Also \(C\) decreases from one to zero there, because \(C'=-S<0\) on the interior. For any unit complex number \(a+ib\) in the first quadrant, the intermediate value property supplies \(t\in[0,t_0]\) with \(C(t)=a\), and positivity plus (CR2) gives \(S(t)=b\). Any unit complex number can be multiplied by one of \(1,-i,-1,i\) to lie in that quadrant. Since \(E(t_0)=i\), (CR1) then shows that it is \(E(t+j t_0)\) for some \(j\in\{0,1,2,3\}\). Thus every prescribed unit number \(d\) is \(E(\theta)\) for a real \(\theta\). For any positive integer \(q\),
\[
             c=E(\theta/q),\qquad |c|=1,\qquad c^q=d.           \tag{CR3}
\]
This proves the needed direction without assuming a root theorem for an arbitrary complex polynomial. The parameter \(t_0\) serves only this proof; no original circle, contour or Fourier constant is being changed.

For any positive real \(r\), there is a unique positive \(q\)-th root of \(r\). The continuous function \(x\mapsto x^q\) increases strictly on \([0,\infty)\), since for \(y>x\geq0\) its difference is
\((y-x)\sum_{j=0}^{q-1}y^{q-1-j}x^j>0\).
It is zero at zero and exceeds \(r\) at \(r+1\). The same intermediate value argument gives existence and the strict inequality gives uniqueness. These are the real roots used in the bounds below.

### 9.2. A minimum of the original polynomial modulus

Let the original nonconstant polynomial be
\[
       p(z)=\sum_{k=0}^N a_k z^k,\qquad
              N\geq1,\quad a_N\ne0,\quad
       A_0=\sum_{k=0}^{N-1}|a_k| .                            \tag{CR4}
\]
Its actual leading coefficient remains \(a_N\). For \(r=|z|\geq1\), the full reverse triangle inequality gives
\[
 |p(z)|\geq |a_N|r^N-\sum_{k=0}^{N-1}|a_k|r^k
            \geq r^{N-1}(|a_N|r-A_0).                         \tag{CR5}
\]
Choose
\[
 R=1+\frac{2A_0}{|a_N|}
              +\left(\frac{2(|a_0|+1)}{|a_N|}\right)^{1/N}.
                                                               \tag{CR6}
\]
For \(r\geq R\), (CR5) is at least \(|a_N|r^N/2\) and exceeds \(|a_0|+1\). Thus the global infimum is attained inside the original disk \(|z|\leq R\).

Here is the existence argument for the attained minimum. The nonempty set of values on that disk is bounded below by zero; real completeness defines its infimum \(b\). Choose original points \(z_j\) in the disk with \(|p(z_j)|<b+1/j\). A bounded sequence in a closed complex square has a convergent subsequence: repeatedly divide the square into four closed subsquares, retain one with infinitely many original points, and choose increasing original indices in the nested squares. Their diameters tend to zero, so completeness in each real coordinate gives a common limit. The disk is closed, hence its subsequence limit \(z_0\) belongs to it. Polynomial continuity follows directly from the full identity
\[
 p(z)-p(w)=(z-w)\sum_{k=1}^N a_k
                    \sum_{j=0}^{k-1}z^{k-1-j}w^j .             \tag{CR7}
\]
On any fixed disk its finite sum is bounded; thus the difference tends to zero with \(z-w\). Consequently \(|p(z_0)|=b\). By the strict outside bound and the available value \(|p(0)|=|a_0|\), this is a global minimum.

### 9.3. The exact translated coefficients force a zero

Suppose \(b_0=p(z_0)\ne0\). The complete finite binomial formula is
\[
 p(z_0+w)=\sum_{r=0}^N b_r w^r,\qquad
 b_r=\sum_{k=r}^N a_k\binom{k}{r}z_0^{\,k-r},\qquad b_N=a_N.
                                                               \tag{CR8}
\]
Let \(q\) be the smallest positive index with \(b_q\ne0\). It exists because \(b_N\ne0\); every intervening coefficient is exactly zero. Define the unit direction
\[
 d=-\frac{|b_q|b_0}{|b_0|b_q},\qquad
 c^q=d,\quad |c|=1,\qquad H=\sum_{r=q+1}^N|b_r|.                \tag{CR9}
\]
Existence of \(c\) is (CR3), with all original factors in \(d\). Put \(w=tc\). Choose \(t>0\), \(t<1\), with
\(|b_q|t^q<|b_0|\) and, if \(H>0\), \(tH<|b_q|/2\).
Such a choice follows from the proved positive real roots; for example take half of the minimum of \(1\), \((|b_0|/|b_q|)^{1/q}\) and \(|b_q|/(2H)\), omitting only the last bound when its actual denominator \(H\) is zero. Then
\[
 \begin{split}
 |p(z_0+tc)|
 &\leq |b_0+b_qt^qc^q|+\sum_{r=q+1}^N|b_r|t^r\\
 &= |b_0|-|b_q|t^q+\sum_{r=q+1}^N|b_r|t^r\\
 &\leq |b_0|-|b_q|t^q+Ht^{q+1}<|b_0| .                       
 \end{split} \tag{CR10}
\]
The middle equality uses \(b_qc^q=-|b_q|b_0/|b_0|\) and the strict bound on \(t^q\). The last inequality also holds when \(H=0\), since the full higher sum is then zero. This contradicts the global minimum. Hence \(p(z_0)=0\). Every nonconstant original complex polynomial has a root, with all its original coefficients and full translated remainder retained. \(\square\)

### 9.4. Full factorization, leading coefficient and multiplicities

For an arbitrary \(\alpha\in\mathbb C\), the full division identity is
\[
 p(z)=p(\alpha)+(z-\alpha)q_\alpha(z),\qquad
 q_\alpha(z)=\sum_{k=1}^N a_k
                    \sum_{j=0}^{k-1}z^{k-1-j}\alpha^j .         \tag{CR11}
\]
It follows from (CR7) with \(w=\alpha\). When \(p(\alpha)=0\), the quotient has degree \(N-1\) and exactly the same leading coefficient \(a_N\); its original finite coefficient sums are shown in (CR11). Applying the proved root theorem to each successive nonconstant quotient, and retaining every zero remainder, yields
\[
 p(z)=a_N\prod_{\ell=1}^N(z-\alpha_\ell)
      =a_N\prod_{\lambda\in Z(p)}(z-\lambda)^{m_\lambda},
 \qquad \sum_{\lambda\in Z(p)}m_\lambda=N .                    \tag{CR12}
\]
Here \(Z(p)\) is the finite set of distinct roots of the original polynomial, and \(m_\lambda\) counts its occurrences in the list, including repetitions. These multiplicities are intrinsic: in (CR8) centered at a root, the least index \(r\) with nonzero coefficient is exactly the largest power of \(z-\lambda\) dividing \(p\), since division at that power leaves a quotient with nonzero value at the root. The derivative identity \(p^{(r)}(\lambda)=r!b_r\), obtained by differentiating every finite term, gives the same characterization with its full factorial. Thus distinct factorizations have the same root set and multiplicities. A nonzero constant has no roots and is its original leading constant times the empty product. The zero polynomial has every complex number as a root and no finite multiplicity at any point; it is excluded from the degree-\(N\), \(a_N\ne0\) theorem. \(\square\)

### 9.5. Scalar units and the exact Bézout and annihilator receiving maps

For every original nonzero scalar \(c\), multiplication
\[
 U_c:\mathbb C[z]\longrightarrow\mathbb C[z],\quad f\longmapsto cf,
 \qquad U_{c^{-1}}U_c=U_cU_{c^{-1}}=I                         \tag{CR13}
\]
is a complex-linear and \(\mathbb C[z]\)-module automorphism. It is not asserted to be a unital algebra homomorphism unless \(c=1\). Both identities are pointwise scalar multiplication. The full evaluation relation is
\((U_cf)(A)=c f(A)\).
Thus its exact inverse preserves roots, multiplicities, divisibility, principal ideals and annihilation; these assertions follow respectively from multiplication by the nonzero number at every scalar point, from (CR12), from \(cf=cgq\) and its inverse, from the two ideal inclusions, and from \(cf(A)=0\) precisely when \(f(A)=0\).

Keep the original least-degree nonzero Bézout combination
\(\delta=a^{(0)}p+b^{(0)}q\) from Section 2, with original leading coefficient \(\kappa\ne0\). Division by \(\delta\), using its actual \(\kappa\), shows directly that \(\delta\) divides both \(p,q\); otherwise a nonzero lower-degree remainder would still be an original combination. Every common divisor divides \(\delta\). The monic gcd named there is compared by
\[
 \delta=\kappa d,\qquad
 d=\kappa^{-1}\delta
   =(\kappa^{-1}a^{(0)})p+(\kappa^{-1}b^{(0)})q .                \tag{CR14}
\]
Every multiplier and inverse factor is retained. The original \(\delta\) and its combination remain in the calculation; (CR13) proves the exact comparison. If \(p,q\) are relatively prime, \(\delta\) is an actual nonzero constant and its inverse gives the full identity one needed for the projection. The pair \((p,q)=(0,0)\) has no such nonzero combination.

Existence of the original annihilator is supplied by the invariant-flag Cayley--Hamilton proof in Section 4, after the root and triangularization interfaces are proved in Sections 9.3 and 9.6--9.7. Its nonempty set of nonzero annihilators contains the original characteristic polynomial, so the set of degrees has a least integer. For an original least-degree nonzero annihilator \(m\) of \(A\), with leading coefficient \(c_m\), the comparison with the source's named monic minimal polynomial is
\[
 m=c_m\mu_A,\qquad m(A)=c_m\mu_A(A)=0.                         \tag{CR15}
\]
Divide every other annihilator by the original \(m\), retaining its leading coefficient in the division steps. Its remainder still annihilates \(A\) and has smaller degree, so is zero. Hence the original \(m\) divides every annihilator. This also proves uniqueness up to its exact nonzero scalar unit, and (CR13) proves the comparison with the named \(\mu_A\).

In positive dimension (CR12) applied to the original \(m\) gives
\(m=c_m H\), \(H=\prod_j h_j\), with \(h_j=(z-\lambda_j)^{\nu_j}\), every multiplicity retained. Put \(H_j=\prod_{k\ne j}h_k\) and \(M_j=m/h_j=c_m H_j\). Distinct linear powers are coprime: a nonconstant common divisor would, by Section 9.3, have a root equal to both distinct \(\lambda_j\)'s. Section 3 of this lesson proves \(a_jh_j+b_jH_j=1\). In the original \(M_j\) calculation this is exactly
\[
 a_jh_j+(c_m^{-1}b_j)M_j=1,\qquad
 E_j=(c_m^{-1}b_j)(A)M_j(A)
    =c_m^{-1}b_j(A)c_m H_j(A).                                \tag{CR16}
\]
Evaluation retains every unit factor. The full original annihilation
\(m(A)=c_mH(A)=0\) implies \(H(A)=0\) by that displayed inverse, so the existing proof of all projection identities and their kernel/image maps applies. Thus the projection is the same original operator with every coefficient recovered; no leading unit is lost from the calculation. On the zero vector space every scalar identity evaluates to the zero endomorphism; a least-degree annihilator can be any original nonzero constant \(c_m\), and the comparison polynomial is \(1\), with \(m=c_m\) and the empty root list. \(\square\)

### 9.6. Original characteristic polynomial and explicit root-to-kernel map

In any fixed original coordinate basis for \(V\), with \(n=\dim V\), retain the original matrix entries \(a_{jk}\). Its characteristic polynomial is the full determinant
\[
 \chi_A(z)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                  \prod_{j=1}^n(z\delta_{j,\sigma(j)}-a_{j,\sigma(j)})
 =\sum_{\sigma\in S_n}\sum_{S\subseteq\{1,\ldots,n\}}
   \operatorname{sgn}(\sigma)z^{|S|}
    \prod_{j\in S}\delta_{j,\sigma(j)}
    \prod_{j\notin S}(-a_{j,\sigma(j)}).                         \tag{CR17}
\]
All zero terms, signs and products are accounted for. When \(n>0\), the leading term comes from the full \(S\) and identity permutation and is \(z^n\); the lower coefficients are the remaining full displayed sums. This leading coefficient one is an exact determinant calculation. When \(n=0\), the single empty permutation and empty subset give the empty product one, so there are no characteristic roots. The other sign convention has the exact relation
\[
                   \det(A-zI)=(-1)^n\chi_A(z).                \tag{CR18}
\]
It follows by taking a minus sign from each of the original \(n\) rows; the zero-dimensional sign is one. Every root and multiplicity agrees through this nonzero constant map.

The determinant identities used below follow from the full coordinate formula rather than an assumed eigenvalue theorem. For arbitrary original matrices \(X,Y\), expanding every product gives
\[
 \det(XY)=\sum_{k_1,\ldots,k_n=1}^n
       \left(\prod_i x_{i,k_i}\right)
       \sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                         \prod_i y_{k_i,\sigma(i)} .           \tag{CR18a}
\]
If two \(k_i\)'s agree, exchanging their assigned columns is a fixed-point-free pairing of the inner permutations with equal products and opposite signs, so the entire inner sum is exactly zero. Every remaining tuple is \(k_i=\tau(i)\) for a permutation \(\tau\). Relabeling its original rows by \(j=\tau(i)\) makes the inner sum \(\operatorname{sgn}(\tau)\det Y\), since the new column permutation is \(\sigma\circ\tau^{-1}\). Summing these surviving tuples is exactly \(\det X\det Y\). This proves determinant multiplicativity with every original summand accounted for. It also proves \(\det S\,\det S^{-1}=1\) for an invertible \(S\), because their product is the actual identity matrix, whose permutation sum is one. Row multilinearity follows by expanding the changed row in the same sum; interchange of two rows changes its sign by relabeling. A matrix with repeated rows has zero determinant by that same sign pairing. Consequently an elementary row addition has its unchanged original determinant, while a row exchange has the full factor minus one.

For the original block matrix of sizes \(r,d\),
\[
 \det\begin{pmatrix}X&C\\0&Y\end{pmatrix}
  =\sum_{\sigma\in S_{r+d}}\operatorname{sgn}(\sigma)
       \prod_{j=1}^{r+d}b_{j,\sigma(j)}
  =\det X\,\det Y .                                           \tag{CR18b}
\]
Every permutation sending a lower row to an upper column has an actual zero factor. All remaining permutations send the \(d\) lower rows bijectively onto the \(d\) lower columns, hence send the upper rows onto upper columns. Their signs and products factor into those of the two original blocks, yielding the displayed product. Thus every term containing an upper-right entry of \(C\) has a corresponding lower-left zero factor; \(C\) remains in the operator and every such determinant term has been explicitly accounted for. The upper triangular case follows by the same argument one block at a time. Each formula includes zero block sizes by its empty-product convention.

For \(n>0\), Sections 9.2--9.4 give a root \(\lambda\) of the actual \(\chi_A\). To construct its entire eigenspace, apply elimination to \(B=\lambda I-A\), retaining every actual pivot. Scan columns in their original order, exchange rows when needed, and eliminate below a pivot \(d_j\ne0\) by subtracting the full multiple \(b_{ik}/d_j\) of the pivot row. Do not replace the pivot by one. Each row exchange is an invertible permutation matrix. Each row addition is \(I-tE_{ij}\), with inverse \(I+tE_{ij}\), since \(i\ne j\) and \(E_{ij}^2=0\). Their ordered product \(T\) is invertible; its inverse is the reversed product of these exact inverses. Write \(E=TB\). Its nonzero rows have pivot columns \(c_1<\cdots<c_r\), with entries \(d_1,\ldots,d_r\); the remaining rows are zero.

The determinant changes sign at each row exchange and is unchanged by a row addition, by the multilinear alternating determinant formula in (CR17). If \(r=n\), the resulting triangular determinant is the full nonzero product of its pivots, so
\(\det B=(-1)^s\prod_{j=1}^n d_j\ne0\), where \(s\) is the number of exchanges. Since \(\chi_A(\lambda)=0\), this is impossible; hence \(r<n\).

Let \(J\) be the original nonpivot column set. For arbitrary \(t=(t_k)_{k\in J}\in\mathbb C^J\), prescribe \(v_k=t_k\) on those columns and define the pivot coordinates in reverse order by
\[
             v_{c_j}
                 =-d_j^{-1}\sum_{k>c_j}E_{jk}v_k,
                      \qquad j=r,r-1,\ldots,1.                \tag{CR19}
\]
Every full row is then zero, and \(Ev=0\) implies \(Bv=0\) through the actual \(T^{-1}\). Conversely any kernel vector has precisely these original free coordinates and is recovered by the same formula. Thus (CR19) is a linear bijection
\(\mathbb C^J\to\ker(\lambda I-A)\), inverse to the actual free-coordinate projection. Since \(J\ne\varnothing\), any nonzero free vector gives a nonzero eigenvector \(Av=\lambda v\). This proves the exact root-to-kernel map and all its fibre dimensions; it is not just a determinant nonidentity. Invertibility away from the roots follows by the same full-pivot elimination and its actual inverse matrices. \(\square\)

### 9.7. Eigenline, invariant range and both receiving quotient maps

For a root \(\lambda\) and an actual nonzero vector obtained from (CR19), let \(L\) be its eigenline and let \(W=\operatorname{im}(A-\lambda I)\). The exact sequences
\[
 0\longrightarrow\ker(A-\lambda I)\longrightarrow V
     \xrightarrow{A-\lambda I}W\longrightarrow0,\qquad
 0\longrightarrow W\longrightarrow V
     \longrightarrow V/W\longrightarrow0                    \tag{CR20}
\]
have their original inclusion, full matrix and quotient maps. Their kernels and images are immediate from the displayed definitions. The equality
\(A(A-\lambda I)=(A-\lambda I)A\) shows invariance of \(W\); it also shows that every map in the first sequence intertwines the actual restricted operators. The second induced operator is exactly \(\lambda I_{V/W}\), because the original \(A-\lambda I\) sends every vector into \(W\). Rank-nullity gives
\(d=\dim(V/W)=\dim\ker(A-\lambda I)\).

Choose a basis of \(W\) and extend it to \(V\). If \(S\) is its full coordinate change, the actual block operator is
\(S^{-1}AS=\begin{pmatrix}A_W&C\\0&\lambda I_d\end{pmatrix}\).
The upper block \(C\) is retained. Block triangular determinant and the exact original conjugation give
\[
 \begin{split}
 \chi_A(z)
 &=\det(S)\det\begin{pmatrix}zI_W-A_W&-C\\0&(z-\lambda)I_d\end{pmatrix}
                                                   \det(S^{-1})\\
 &=\det(S)\,\chi_{A_W}(z)(z-\lambda)^d\,\det(S^{-1}),\qquad
                    \det(S)\det(S^{-1})=1 .                  
 \end{split} \tag{CR21}
\]
Thus its original root multiplicity is at least \(d\), with every coordinate and unit factor shown.

The eigenline construction instead uses the exact sequence
\(0\to L\to V\to V/L\to0\), with induced operator \(\overline A\) on \(V/L\). In a basis beginning with the actual eigenvector, its full block form gives
\[
 \chi_A(z)=\det(S_L)(z-\lambda)
                           \chi_{\overline A}(z)\det(S_L^{-1}),
 \qquad \det(S_L)\det(S_L^{-1})=1.                             \tag{CR22}
\]
The quotient has dimension \(n-1\), while \(W\) has dimension \(n-d\). Both constructions are exact invariant-operator maps from the same original \(A\), with their original determinant identities. Formula (CR22) supplies the eigenline induction actually written in Section 4. Formula (CR21) supplies the invariant-range route mentioned there. Inducting on the original dimension, lifting the ordered quotient basis and retaining each lifted vector proves triangularization, including the empty basis at dimension zero. The existing invariant-flag argument then gives Cayley--Hamilton for that same original operator, without using projections to obtain its own prerequisite. \(\square\)

### 9.8. The original spectral bound and contour receiver

For an actual eigenvector \(v\ne0\), the unchanged operator norm gives
\[
 |\lambda|\|v\|=\|Av\|\leq\|A\|\|v\|,
                    \qquad |\lambda|\leq\|A\| .               \tag{CR23}
\]
No change to the original length of \(v\) is needed. Together with the actual polynomial determinant (CR17) and its continuity as a finite sum, this supplies the root bound and eigenvalue criterion in Section 7's compact-parameter contour construction. Every repeated root remains included; absence of real roots means absence of real eigenvalues through (CR19), in both original determinant conventions (CR18).

The original polynomial, its Bézout combination, its least-degree annihilator and its matrix have now been carried through the root, scalar-unit, projection, kernel and quotient maps. Sections 2--4 and 7 use these exact maps, with all leading factors and repeated roots retained. These are finite polynomial and spectral results; each further boundary-operator assertion retains its separate hypotheses and proof.

## 10. Full finite linear-algebra foundations

Here are the finite algebra proofs used by the preceding spectral and polynomial arguments. It works over the original field \(F=\mathbb R\) or \(F=\mathbb C\). Conjugation is the identity in the real case. The scalar entry is the real field with completeness, the complex field formed from it, finite induction and finite sums/products. No spectral decomposition, root theorem, basis-extension theorem, rank-nullity theorem or inner-product representation theorem is assumed below. The complex-root theorem already proved in Polynomial and contour interfaces for stable boundary models is used only when root existence is separately requested in Section 10.10. These are standard foundational results; no novelty is claimed.

All vectors, coefficient matrices, pivots, signs and inner products in a calculation keep their original values. A new basis gives an explicit coordinate comparison, with both directions and every metric factor retained. In particular, the original Gram residuals and their lengths stay in the calculation when a separately constructed orthonormal comparison basis is given.

### 10.1. Finite spanning sets, exchange and basis extension

The scalar arithmetic used here is explicit. Real arithmetic is the given ordered-field arithmetic. For complex numbers keep their original pairs and define
\[
\begin{gathered}
(a,b)+(c,d)=(a+c,b+d), \\ 
(a,b)(c,d)=(ac-bd,ad+bc), \\ 1=(1,0),\quad 0=(0,0),\quad i=(0,1).
\end{gathered}
\tag{FA0a}
\]
Addition is an abelian group coordinatewise. Multiplication is commutative by the real commutative field laws. Expanding either association of three factors gives the same full pair
\[
((a,b)(c,d))(e,f)=(a,b)((c,d)(e,f))
=(ace-adf-bcf-bde,acf+ade+bce-bdf).
\tag{FA0b}
\]
All four summands in each coordinate are retained; distributivity follows by the same two-coordinate expansion. The displayed zero and one are the additive and multiplicative identities, and the additive inverse is the pair of the two original negatives. For a nonzero pair, the original real number \(a^2+b^2\) is positive. Direct multiplication in either order proves
\[
\begin{gathered}
(a,b)^{-1}=\left(\frac{a}{a^2+b^2},-\frac{b}{a^2+b^2}\right), \\  (a,b)(a,b)^{-1}=(a,b)^{-1}(a,b)=(1,0), \\ i^2=(-1,0).
\end{gathered}
\tag{FA0c}
\]
Thus these pairs form a field. The real inclusion \(a\mapsto(a,0)\) preserves both operations, is injective and gives the original real subfield. Conjugation is the actual map \((a,b)\mapsto(a,-b)\); the two-coordinate multiplication shows that it preserves products, conjugates sums, and has square the identity. Keeping the original squared modulus \(N(a,b)=a^2+b^2\), expansion gives
\[
N((a,b)(c,d))=(ac-bd)^2+(ad+bc)^2
=a^2c^2-2acbd+b^2d^2+a^2d^2+2adbc+b^2c^2
=(a^2+b^2)(c^2+d^2).
\tag{FA0d}
\]
The middle two mixed terms are opposite by the scalar real field laws; no matrix product is being commuted. This supplies the actual complex arithmetic and conjugation used below from the stated real base.

Finite polynomial arithmetic is equally explicit. For original coefficients \(p(z)=\sum_j a_jz^j\), \(q(z)=\sum_k b_kz^k\), with coefficients zero outside their finite lists, addition has coefficients \(a_l+b_l\), and multiplication has coefficients \(\sum_{j+k=l}a_jb_k\). Distributivity and associativity follow by retaining the same finite ordered sums: the coefficient of a triple product at \(l\) is \(\sum_{j+k+t=l}a_jb_kc_t\) under either association. The constant polynomial one is the multiplicative identity, and zero is the additive identity. For nonzero original polynomials of degrees \(m,n\), the highest coefficient of their product is the original nonzero product \(a_mb_n\), so its degree is \(m+n\). These assertions include constant polynomials and the zero polynomial without assigning a degree to zero. Finite induction on the resulting nonnegative degree is the original finite-induction principle. Section 2 uses precisely this arithmetic for division and Bézout.

A vector space over \(F\) has the usual addition and scalar multiplication. The span of a finite list is the set of all of its finite linear combinations, including the empty combination zero. A list is independent when its only zero linear combination has every coefficient zero. A finite-dimensional space means one admitting a finite spanning list; a basis is an independent spanning list. The zero space has the empty basis.

Let \(u_1,\ldots,u_r\) be independent and let the original list \(b_1,\ldots,b_N\) span \(V\). We prove \(r\leq N\) and replace selected original list positions by the actual \(u_j\) while keeping a spanning list. Suppose a spanning list already has \(u_1,\ldots,u_{j-1}\) and \(N-j+1\) remaining original vectors. Write

\[
u_j=\sum_{k<j}a_k u_k+\sum_{b\in L}c_b b.
\tag{FA1}
\]

At least one \(c_b\ne0\), because otherwise \(u_j\) belongs to the span of its independent predecessors. Choose such an actual original \(b\). Solving (FA1) gives

\[
b=c_b^{-1}u_j-\sum_{k<j}c_b^{-1}a_k u_k
 -\sum_{b'\in L\setminus\{b\}}c_b^{-1}c_{b'}b'.
\tag{FA2}
\]

Both expressions retain their original nonzero coefficient and its inverse. Replacing this \(b\) by \(u_j\) preserves the span in both directions. The operation needs a remaining vector at each step; after \(N\) steps there is none, so an independent list cannot have a further member. This proves the bound and the asserted exchange construction without first assuming existence of a basis.

Now start with any independent list and scan the original finite spanning list in its original order. Append a vector exactly when it is outside the current span. An appended vector preserves independence: a zero combination with nonzero coefficient on the new vector would put it in the preceding span. At the end every original spanning vector is in the resulting span. Thus the list extends to a basis. Starting with the empty list gives existence of a basis. Applying the exchange bound in both directions to two bases proves that they have the same number of vectors. This number is \(\dim_F V\).

Every subspace \(W\subset V\) has a finite basis. Choose a vector outside the current span in \(W\) whenever one exists. An independent list in \(W\) is also independent in \(V\), so it can never exceed the finite dimension of \(V\). By that bound the construction terminates after at most \(\dim V\) choices and then spans \(W\). This is only a finite selection. Its actual selected vectors can be extended to a basis of \(V\) by the preceding construction.

### 10.2. Coordinates, matrix products and basis comparisons

For an ordered original basis \(b=(b_1,\ldots,b_n)\), the map

\[
\begin{gathered}
J_b:F^n\longrightarrow V, \\ J_b x=\sum_{j=1}^n x_j b_j
\end{gathered}
\tag{FA3}
\]

is linear, surjective by span and injective by independence. Its inverse gives the unique original coordinates. For \(n=0\) this is the unique map between zero spaces and is a bijection.

Let \(T:V\to W\) be linear, with ordered basis \(c=(c_1,\ldots,c_q)\) in \(W\). Define \(A_{ij}\) by the unique expression \(Tb_j=\sum_i A_{ij}c_i\). Then

\[
\begin{gathered}
T=J_c A J_b^{-1}, \\ (Ax)_i=\sum_{j=1}^n A_{ij}x_j.
\end{gathered}
\tag{FA4}
\]

This constructs the matrix rather than assuming it. Every matrix conversely defines this linear map. Addition and scalar multiplication of maps are entrywise addition and multiplication of their matrices. If \(U:W\to Z\) has matrix \(B\) in the actual target basis, finite expansion gives

\[
\begin{gathered}
(BA)_{kj}=\sum_{i=1}^q B_{ki}A_{ij}, \\ UT=J_d BA J_b^{-1}.
\end{gathered}
\tag{FA5}
\]

The order is \(BA\). Expanding each finite triple sum and keeping the same ordered summands proves associativity. The coordinate matrix of the identity is \(I_n\), with entries \(\delta_{ij}\). Every empty sum and zero dimension in (FA4)--(FA5) has its literal value; no nonzero-dimensional hypothesis has entered.

For new bases \(b'_j=\sum_k S_{kj}b_k\) and \(c'_i=\sum_l R_{li}c_l\), (FA3) gives \(J_{b'}=J_b S\) and \(J_{c'}=J_c R\). Both \(S\) and \(R\) are invertible because the two coordinate maps are bijective. The inverse of a linear bijection is linear: apply the bijection to the two sides of its desired addition and scalar identities, and use injectivity. Matrix multiplication in (FA5) therefore proves

\[
\begin{gathered}
x=Sx', \\  x'=S^{-1}x, \\  A'=R^{-1}AS, \\ J_{c'}A'J_{b'}^{-1}=J_cAJ_b^{-1}.
\end{gathered}
\tag{FA6}
\]

These equalities are the actual coordinate morphisms for the unchanged original map \(T\); they are not replacements of that map. For two inverse linear maps their matrix products in both orders are the corresponding identity matrices. For a square matrix possessing a two-sided matrix inverse, (FA4) conversely gives a linear bijection and its inverse.

### 10.3. Rank-nullity, quotients and direct sums

Let \(T:V\to W\) be any original linear map, and choose the actual basis \(k_1,\ldots,k_a\) of its kernel. Extend it to \(k_1,\ldots,k_a,v_1,\ldots,v_r\) in \(V\) by Section 10.1. The vectors \(Tv_1,\ldots,Tv_r\) are independent: if \(T\sum_j t_jv_j=0\), that sum is in the span of the \(k_i\), and independence of the extended basis forces every \(t_j=0\). They span \(\operatorname{im}T\), because applying \(T\) to any original basis expansion discards precisely the kernel summands. Hence

\[
\begin{gathered}
\dim V=a+r, \\  \dim\ker T=a, \\ \dim\operatorname{im}T=r.
\end{gathered}
\tag{FA7}
\]

The exact quotient map is \(v\mapsto v+\ker T\); the induced map \(V/\ker T\to\operatorname{im}T\), \(v+\ker T\mapsto Tv\), is well defined because two representatives differ by a kernel vector. It is injective by the definition of the kernel and surjective by that of the image. Its inverse in the displayed basis is \(\sum_j t_jTv_j\mapsto\sum_j t_jv_j+\ker T\), with all original coefficients retained.

For any subspace \(K\subset V\), choose a basis of \(K\) and extend it to \(V\). The cosets of the added basis vectors form a basis of \(V/K\): span follows from the original expansion and independence follows by subtracting an element of \(K\). Therefore \(\dim(V/K)=\dim V-\dim K\). The span \(L\) of the added vectors has \(K\cap L=\{0\}\), and every vector has a unique expansion as a sum from \(K\) and \(L\). The addition map \(K\oplus L\to V\) is a bijection with inverse the actual two coordinate projections. In general, the addition map \(U\oplus W\to U+W\) is surjective and has kernel exactly \(\{(v,-v):v\in U\cap W\}\). Using (FA7) proves

\[
\dim(U+W)=\dim U+\dim W-\dim(U\cap W).
\tag{FA8}
\]

The same coordinate argument iterated proves the finite direct-sum statement: addition from \(\bigoplus_j V_j\) is a bijection precisely when every zero sum from the subspaces has all terms zero and their sum is the target space. Concatenating their actual bases then gives its basis and dimension \(\sum_j\dim V_j\). This supplies the direct-sum dimensions used by the stable primary decomposition.

A square map \(V\to V\) is injective if and only if it is surjective, by (FA7) and equality of its two original dimensions. A bijection is exactly an invertible matrix under Section 10.2. These assertions include dimension zero.

### 10.4. Determinants and the full ordered elimination maps

For an original square matrix \(M=(m_{ij})\) of size \(n\), define its determinant by the finite full sum

\[
\det M=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                  \prod_{i=1}^n m_{i,\sigma(i)}.
\tag{FA9}
\]

The sign is \((-1)\) to the number of inversions. Interchanging two indices changes that parity: for adjacent indices it changes one inversion and interchanging arbitrary indices is an odd number of adjacent exchanges. Thus exchanging two rows, or two columns, changes the sign of (FA9) by relabeling permutations. Identical rows or columns give zero by pairing equal products with opposite signs. Multilinearity in each row and column follows by expanding its single factor in every product. Adding a multiple of another row leaves the determinant unchanged because its additional summand has two identical rows. The identity matrix has determinant one, since every nonidentity permutation has a literal zero factor. For \(n=0\), the single empty permutation has the empty product one.

For arbitrary original square matrices \(X,Y\), expand every entry of the product before making any comparison:

\[
\det(XY)=\sum_{k_1,\ldots,k_n=1}^n
 \left(\prod_{i=1}^n X_{i,k_i}\right)
 \sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                  \prod_{i=1}^n Y_{k_i,\sigma(i)}.
\tag{FA10}
\]

If two \(k_i\)'s agree, exchanging the columns assigned to their two positions pairs the inner permutations without a fixed point, with equal products and opposite signs. The whole inner sum is exactly zero. Every remaining list is \(k_i=\tau(i)\) for a permutation \(\tau\). Reordering its rows gives inner sum \(\operatorname{sgn}(\tau)\det Y\). Indeed the relabeled column permutation is \(\sigma\circ\tau^{-1}\), whose sign is \(\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)\); this follows from the adjacent-exchange sign calculation above. The surviving full sum in (FA10) is therefore \(\det X\det Y\). No summand is discarded without this exact zero calculation. In particular \(\det S\det S^{-1}=1\) whenever both inverse products are the identity.

Here is the exact elimination construction for an original rectangular \(q\)-by-\(n\) matrix. Scan columns in their original order; for the next pivot choose a nonzero entry in the remaining rows, exchange its row with the next pivot row if necessary, and subtract the full pivot multiple from every lower row. Do not divide the pivot row or replace its pivot by one. Each exchange has an actual permutation matrix with its inverse the same exchange. Each subtraction has matrix \(I-cE_{ij}\), where \(i\ne j\), and inverse \(I+cE_{ij}\), since \(E_{ij}^2=0\). If \(E=E_\ell\cdots E_1\) is the full ordered product, the echelon matrix is \(R=EM\) and \(M=E_1^{-1}\cdots E_\ell^{-1}R\). There are at most \(\min(q,n)\) pivots; scan and row count are finite, so the procedure terminates. Every remaining row is zero, since otherwise its first nonzero entry would have supplied a pivot when its column was scanned.

Write the actual pivot columns as \(c_1<\cdots<c_r\), their nonzero original resulting pivots as \(d_j=R_{j,c_j}\), and let \(J\) be the nonpivot columns. For arbitrary prescribed original free coordinates \(x_k=t_k\), \(k\in J\), solve backwards by

\[
\begin{gathered}
x_{c_j}=-d_j^{-1}\sum_{k>c_j}R_{jk}x_k, \\ j=r,r-1,\ldots,1.
\end{gathered}
\tag{FA11}
\]

Each later pivot coordinate has already been computed, and earlier coefficients in that row are zero by echelon construction. Every zero row imposes no equation. Hence (FA11) is a linear bijection \(F^J\to\ker M\), inverse to the actual free-coordinate projection, because \(E\) is invertible. The coordinate vectors of \(F^J\) give the full kernel basis, with original pivot denominators retained. Thus \(\dim\ker M=n-r\) and \(\operatorname{rank}M=r\) by (FA7). In particular, the number of pivots is independent of the choices of exchange rows even though the displayed coordinate map can depend on them.

If \(q=n\), there are two cases. For \(r<n\), echelon form has a zero row and determinant zero. Each exchange contributes \(-1\), and each subtraction contributes one, by (FA9); hence \(\det M=0\) as well, and (FA11) gives a nonzero kernel vector. For \(r=n\), all columns are pivot columns, \(R\) is upper triangular and its full permutation sum gives \(\det R=\prod_j d_j\): every other permutation has a lower-triangular zero factor, proved successively from the last row upwards. If \(s\) row exchanges occurred, this gives

\[
\begin{gathered}
\det E=(-1)^s, \\ \det M=(-1)^s\prod_{j=1}^n d_j\ne0.
\end{gathered}
\tag{FA12}
\]

For an arbitrary right side \(y\), the exact inverse is found from \(z=Ey\) and

\[
\begin{gathered}
x_j=d_j^{-1}\left(z_j-\sum_{k>j}R_{jk}x_k\right), \\  j=n,n-1,\ldots,1, \\ M^{-1}=R^{-1}E.
\end{gathered}
\tag{FA13}
\]

Backward substitution gives a solution and makes it unique. Applying the two compositions to arbitrary vectors proves both inverse identities. Thus a square original matrix is invertible exactly when its original determinant is nonzero, over either field. No eigenvalue-existence theorem enters this proof.

For later continuity uses, define the cofactor \(C_{ij}=(-1)^{i+j}\det M^{(i|j)}\) with the indicated row and column deleted, and \(\operatorname{adj}(M)_{ji}=C_{ij}\). In (FA9), group the permutations by the column used by row \(i\). Moving that row/column to their first positions produces the sign \((-1)^{i+j}\), giving \(\sum_j m_{ij}C_{ij}=\det M\). Replacing this row by a distinct row gives the off-diagonal sum zero by the repeated-row determinant. The column version gives the other product. Consequently

\[
\begin{gathered}
M\operatorname{adj}(M)=\operatorname{adj}(M)M=(\det M)I_n, \\ M^{-1}=(\det M)^{-1}\operatorname{adj}(M)
\quad(\det M\ne0).
\end{gathered}
\tag{FA14}
\]

This retains the exact original determinant denominator and every cofactor sign. When \(n=1\), the minor is the zero-dimensional determinant one. When \(n=0\), the adjugate is the unique empty matrix and both product identities are identities of empty matrices. All determinants and cofactors are finite polynomial expressions, so the inverse is continuous on the actual nonzero-determinant domain by the scalar quotient rule.

### 10.5. The original inner product and the full Gram residuals

An inner product \(h\) is linear in its first variable, conjugate-linear in its second, has \(h(v,w)=\overline{h(w,v)}\), and satisfies \(h(v,v)>0\) for \(v\ne0\). These are its definition, not a consequence assumed for a different matrix. Let \(\|v\|_h=\sqrt{h(v,v)}\). The positive real square root exists from real completeness: the nonempty bounded set \(\{t\ge0:t^2\le a\}\) has a supremum for \(a>0\), and continuity of the square shows its square can be neither below nor above \(a\), by a sufficiently small positive increment or decrement. Its strict monotonicity on nonnegative reals proves uniqueness. Zero has square root zero.

For any chosen original basis \(b\), keep the full matrix

\[
\begin{gathered}
H_{jk}=h(b_k,b_j), \\ 
h(J_bx,J_by)=y^\dagger Hx
 =\sum_{j,k}\overline{y_j}H_{jk}x_k, \\ H^\dagger=H.
\end{gathered}
\tag{FA15}
\]

Here \(\dagger\) is conjugate transpose, with entry \((M^\dagger)_{jk}=\overline{M_{kj}}\). Formula (FA15) follows by finite expansion and fixes the linear-first convention exactly. If \(Hx=0\), then \(x^\dagger Hx=0\), so positivity and the coordinate bijection give \(x=0\). Therefore \(H\) is invertible by Sections 10.3--4. Conversely, any Hermitian matrix with \(x^\dagger Hx>0\) for \(x\ne0\) gives an inner product by (FA15), since the linearity, Hermitian identity and positivity follow entrywise. An inner product exists on any finite vector space by taking the explicitly constructed coordinate formula \(h_0(J_bx,J_by)=\sum_j x_j\overline{y_j}\). This existence construction does not replace an already given \(h\).

For a basis \(b_1,\ldots,b_n\), define its actual residuals inductively, keeping every length and projection factor:

\[
\begin{gathered}
r_1=b_1, \\  d_k=h(r_k,r_k), \\ r_j=b_j-\sum_{k<j}\frac{h(b_j,r_k)}{d_k}r_k.
\end{gathered}
\tag{FA16}
\]

Assume the earlier residuals are nonzero and mutually orthogonal. Then the displayed formula has defined nonzero denominators. Direct pairing with \(r_l\), \(l<j\), gives \(h(r_j,r_l)=h(b_j,r_l)-h(b_j,r_l)d_l/d_l=0\), with all other summands zero by the earlier orthogonality. If \(r_j=0\), the formula puts \(b_j\) in the earlier residual span. Each earlier residual lies in the corresponding original initial span, so this contradicts the independence of \(b\). Hence \(r_j\ne0\), \(d_j>0\), and induction proves all assertions. The converse expressions in (FA16) show equality of the original and residual initial spans at every stage; in particular the residuals are a basis.

Let \(S\) be the matrix with these actual residual coordinates, \(r_j=J_bS e_j\). It is upper triangular with diagonal one by (FA16), and \(D=\operatorname{diag}(d_1,\ldots,d_n)\). The exact Gram and determinant comparisons are

\[
\begin{gathered}
S^\dagger HS=D, \\  H=(S^{-1})^\dagger DS^{-1}, \\ \det H=\prod_{j=1}^n d_j>0\quad(n>0).
\end{gathered}
\tag{FA17}
\]

The first equality is the full pairing of the actual residuals; the second multiplies by the actual inverses in the stated order. The determinant identity uses multiplicativity, \(\det S=1\), and \(\det S^\dagger=\overline{\det S}\). The last conjugate identity follows by conjugating (FA9) and transposing permutations; the inverse permutation has the same sign. In dimension zero the product and \(\det H\) are both one, and the zero space is its own orthogonal basis.

The requested orthonormal Gram--Schmidt comparison consists of the explicitly defined vectors \(e'_j=d_j^{-1/2}r_j\), not a change to any earlier residual. Set \(U=S D^{-1/2}\). The two coordinate maps and every metric factor are

\[
\begin{gathered}
J_{e'}=J_b U, \\  x=Uz, \\ 
z=D^{1/2}S^{-1}x, \\ 
U^\dagger HU=D^{-1/2}S^\dagger HS D^{-1/2}=I_n, \\ \det U=\prod_j d_j^{-1/2}.
\end{gathered}
\tag{FA18}
\]

Thus \(e'\) is an orthonormal basis for the original \(h\), while the original \(H\), \(S\), \(r_j\) and \(d_j\) remain explicit in (FA15)--(FA18). Over the real field all \(d_j^{-1/2}\) are positive, so the comparison orientation has the sign of \(\det S=1\). No arbitrary sign is inserted. The complex determinant is the displayed positive real factor in these original coordinates.

For an independent list which is not yet a basis, the same induction gives its nonzero orthogonal residuals; extending the original list to a basis by Section 10.1 extends that orthogonal construction. For a subspace with these residuals \(r_1,\ldots,r_a\), the exact original projection and its complement are

\[
\begin{gathered}
Pv=\sum_{k=1}^a\frac{h(v,r_k)}{d_k}r_k, \\  h(v-Pv,r_k)=0, \\ V=W\oplus W^\perp.
\end{gathered}
\tag{FA19}
\]

Indeed the residuals span \(W\); the difference is orthogonal to their span by conjugate-linearity, and an element in \(W\cap W^\perp\) has zero self-pairing and is zero. Pairing gives \(P^2=P\) and \(h(Pv,w)=h(v,Pw)\), because each side is the same sum \(\sum_k h(v,r_k)h(r_k,w)/d_k\). These statements also hold for the empty subspace, whose projection is zero.

### 10.6. Exact finite inner-product bounds and the unchanged original norm

For \(w\ne0\), the original residual \(v-h(v,w)h(w,w)^{-1}w\) has squared norm

\[
\left\|v-\frac{h(v,w)}{h(w,w)}w\right\|_h^2
=\|v\|_h^2-\frac{|h(v,w)|^2}{\|w\|_h^2}\ge0.
\tag{FA20}
\]

Expand its two cross terms using the specified linear-first convention; each is \(-|h(v,w)|^2/h(w,w)\), and the last term adds one copy. This proves Cauchy--Schwarz with its actual denominator. If \(w=0\), the pairing is zero by linearity and the same inequality without division is immediate. The equality case for nonzero \(w\) holds exactly when this actual residual is zero, hence when \(v\) is a scalar multiple of the actual \(w\). The norm obeys \(\|av\|_h=|a|\|v\|_h\), positivity, and the triangle inequality: expand \(\|v+w\|_h^2\), bound the two real cross terms by \(2\|v\|_h\|w\|_h\), and take the nonnegative square root.

For the full residual basis, orthogonality gives the exact identities

\[
\begin{gathered}
v=\sum_{j=1}^n\frac{h(v,r_j)}{d_j}r_j, \\  \|v\|_h^2=\sum_{j=1}^n\frac{|h(v,r_j)|^2}{d_j}, \\ \left\|v-\sum_{j=1}^a\frac{h(v,r_j)}{d_j}r_j\right\|_h^2
=\|v\|_h^2-\sum_{j=1}^a\frac{|h(v,r_j)|^2}{d_j}.
\end{gathered}
\tag{FA21}
\]

The first equality follows by pairing the difference with every residual in the basis, and positivity. The other two follow by expansion with every original \(d_j\) retained. These are finite sums; they assume no infinite-dimensional orthonormal expansion.

For \(n>0\), set \(d_{\min}=\min_jd_j>0\), \(F_S=(\sum_{j,k}|S_{jk}|^2)^{1/2}>0\), and \(M_b=(\sum_j\|b_j\|_h^2)^{1/2}>0\). With \(x=S a\), (FA17), finite scalar Cauchy--Schwarz in every row of \(S\), and the original basis triangle inequality give

\[
\begin{gathered}
\frac{\sqrt{d_{\min}}}{F_S}|x|_2
 \le \|J_bx\|_h
 \le M_b|x|_2, \\ |x|_2^2=\sum_j|x_j|^2.
\end{gathered}
\tag{FA22}
\]

For the lower bound, \(\|J_bx\|_h^2=\sum_jd_j|a_j|^2\ge d_{\min}|a|_2^2\), while \(|S a|_2\le F_S|a|_2\). For the upper bound, \(\|\sum_jx_jb_j\|_h\le\sum_j|x_j|\|b_j\|_h\le M_b|x|_2\). Thus both inequalities are for the original \(h\), basis and coordinates; their exact comparison constants are preserved. In dimension zero every vector and norm is zero, so no division by \(F_S\) is needed. Completeness of the finite original inner-product space follows: (FA22) makes the coordinates of a Cauchy sequence Cauchy in \(F\); their scalar limits give a vector, and the upper inequality proves convergence in the unchanged original norm.

For \(T:V\to W\), with \(n>0\), the same expansion gives the concrete bound

\[
\|Tv\|_{h_W}\le
\frac{F_S}{\sqrt{d_{\min}}}
\left(\sum_{j=1}^n\|Tb_j\|_{h_W}^2\right)^{1/2}
\|v\|_{h_V}.
\tag{FA23}
\]

Every original image \(Tb_j\) occurs in this constant. The bound proves that every finite linear map is continuous. Define its operator norm by \(\|T\|=\sup_{v\ne0}\|Tv\|/\|v\|\), with value zero if its domain is zero. This is finite by (FA23). Applying the definition twice to the actual vectors gives \(\|UT\|\le\|U\|\|T\|\); the zero-vector cases require no division. Addition and scalar norm identities follow from the original vector norm inequalities, and \(\|I_V\|=1\) for \(V\ne0\), zero for \(V=0\). In particular all fixed finite coordinate maps and projections in the spectral receiving calculation are bounded on the original spaces, without replacing their norms by coordinate norms.

### 10.7. Full adjoints in the original Gram matrices

For an original map \(T:V\to W\), with matrix \(A\), let \(H_V,H_W\) be its two original Gram matrices from (FA15). Define a map \(T^*:W\to V\) by its exact matrix

\[
\begin{gathered}
A^*=H_V^{-1}A^\dagger H_W, \\ h_W(Tv,w)=h_V(v,T^*w).
\end{gathered}
\tag{FA24}
\]

The identity follows directly: writing the original coordinates as \(x,y\), its left side is \(y^\dagger H_WAx\); its right side is \((A^*y)^\dagger H_Vx=y^\dagger H_W A H_V^{-1}H_Vx\), because \(H_V^\dagger=H_V\), \((H_V^{-1})^\dagger=H_V^{-1}\), and \(H_W^\dagger=H_W\). The inverse-adjoint identity here follows by transposing/conjugating both original inverse products, whose entry expansions reverse their order. Uniqueness follows by choosing \(v\) equal to the difference of two candidate adjoint values: positivity forces that difference to be zero. This proves existence and uniqueness without invoking any Hilbert-space representation theorem. If either space is zero, the unique zero map gives the same identity.

For actual composable maps, the defining identity and uniqueness, or the full ordered matrices, prove

\[
\begin{gathered}
(UT)^*=T^*U^*, \\  (T^*)^*=T, \\ 
(T+Q)^*=T^*+Q^*, \\  (aT)^*=\overline a T^*, \\ (T^{-1})^*=(T^*)^{-1}\quad(T\text{ bijective}).
\end{gathered}
\tag{FA25}
\]

For example, with an actual third Gram matrix \(H_Z\), the product matrix is
\(H_V^{-1}A^\dagger B^\dagger H_Z=(H_V^{-1}A^\dagger H_W)(H_W^{-1}B^\dagger H_Z)\), with the two middle inverse factors and their order explicit. Taking the adjoint of both inverse products proves both inverse identities in the last assertion. None of these formulas identifies conjugate transpose with an adjoint in an arbitrary original basis: the two Gram factors in (FA24) are essential.

Under the exact original basis changes \(S,R\) of (FA6), the new Gram matrices are \(H'_V=S^\dagger H_VS\), \(H'_W=R^\dagger H_WR\). The adjoint matrix in those coordinates is

\[
\begin{gathered}
(A')^*=(S^\dagger H_VS)^{-1}(R^{-1}AS)^\dagger
                        (R^\dagger H_WR) \\  =S^{-1}H_V^{-1}A^\dagger H_WR=S^{-1}A^*R.
\end{gathered}
\tag{FA26}
\]

Expand the inverse as \(S^{-1}H_V^{-1}(S^\dagger)^{-1}\), the middle dagger as \(S^\dagger A^\dagger(R^\dagger)^{-1}\), and cancel only the adjacent actual inverse products. This proves that the unchanged abstract adjoint has exactly the coordinate morphism required by (FA6), retaining every original metric factor in the comparison.

For \(u\ne0\), Cauchy--Schwarz and the test vector \(u\) itself show \(\|u\|=\sup_{w\ne0}|h(u,w)|/\|w\|\), with value zero for \(u=0\). Therefore, if both spaces are nonzero,

\[
\begin{gathered}
\|T\|=\sup_{v\ne0,\,w\ne0}
 \frac{|h_W(Tv,w)|}{\|v\|\|w\|} \\ =\sup_{v\ne0,\,w\ne0}
 \frac{|h_V(v,T^*w)|}{\|v\|\|w\|} \\ =\|T^*\|.
\end{gathered}
\tag{FA27}
\]

For the final equality use conjugate symmetry and the same actual-vector dual-norm formula, interchanging the two suprema over the same bounded collection of nonnegative values. If a space is zero both operator norms are zero. Thus the norm equality holds with the original inner products and no unproved normalization or separability hypothesis.

### 10.8. Trace, projection rank and positivity in the receiving coordinates

For square original matrices, define \(\operatorname{tr}A=\sum_jA_{jj}\). For a rectangular \(q\)-by-\(n\) matrix \(A\) and \(n\)-by-\(q\) matrix \(B\), finite expansion gives \(\operatorname{tr}(BA)=\sum_{j,i}B_{ji}A_{ij}=\sum_{i,j}A_{ij}B_{ji}=\operatorname{tr}(AB)\). Only scalars commute here. Consequently \(\operatorname{tr}(S^{-1}AS)=\operatorname{tr}(ASS^{-1})=\operatorname{tr}A\), retaining both comparison factors before their actual identity product.

For a projection \(P^2=P\), each vector is \(Pv+(v-Pv)\), with first term in its image and second in its kernel. Their intersection is zero because \(Pv=v\) on the image and \(Pv=0\) on the kernel. Concatenating their actual bases gives matrix \(\operatorname{diag}(I_r,0)\) in those coordinates, where \(r=\dim\operatorname{im}P\). The exact basis-change identity and trace equality prove \(\operatorname{tr}P=r\). Thus the projection trace is its original rank even when \(P\) is not orthogonal for the original inner product. A continuous family of such projections has continuous traces, since trace is a finite sum of continuous original entries; their integer ranks are locally constant, because a change smaller than one in absolute trace cannot change the integer value. This supplies the finite bundle rank assertion used by the stable projection families; it does not assert global triviality.

A map is self-adjoint exactly when \(T=T^*\), equivalently \(H_VA=A^\dagger H_V\) by (FA24). It is positive exactly when its original quadratic pairing \(h(Tv,v)=x^\dagger H_VAx\) is nonnegative real for every original vector. These are definitions on the actual original inner product, with no altered density or metric. For example \(T^*T\) is self-adjoint by (FA25), and

\[
\begin{gathered}
h_V(T^*Tv,v)=h_W(Tv,Tv)=\|Tv\|_{h_W}^2\ge0, \\ \ker(T^*T)=\ker T.
\end{gathered}
\tag{FA28}
\]

The pairing identity follows from (FA24) and conjugate symmetry, and the kernel equivalence follows from positivity. For an eigenvector \(Av=\lambda v\ne0\) of a self-adjoint map over \(\mathbb C\), self-adjointness and conjugate symmetry give \(\lambda\|v\|^2=\overline\lambda\|v\|^2\), so \(\lambda\) is real. If the map is positive its same original pairing gives \(\lambda\ge0\). This conclusion uses neither root existence nor a spectral decomposition; those are separate later arguments.

### 10.9. The full original characteristic criterion and invariant blocks

For \(A\in\operatorname{End}_F(V)\) in the actual ordered coordinates and \(n=\dim V\), let \(\chi_A(z)=\det(zI_n-A)\). Keep the whole entry formula and its exact expansion:

\[
\begin{gathered}
\chi_A(z)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
 \prod_{j=1}^n(z\delta_{j,\sigma(j)}-A_{j,\sigma(j)}) \\ =\sum_{\sigma\in S_n}\sum_{S\subset\{1,\ldots,n\}}
 \operatorname{sgn}(\sigma)z^{|S|}
 \prod_{j\in S}\delta_{j,\sigma(j)}
 \prod_{j\notin S}(-A_{j,\sigma(j)}), \\ \det(A-zI_n)=(-1)^n\chi_A(z).
\end{gathered}
\tag{FA29}
\]

Every original zero term, coefficient and sign remains in these sums. The leading term for \(n>0\) is \(z^n\), coming from the full subset and identity permutation; all other highest-subset terms have a Kronecker zero. For \(n=0\), the empty terms give \(\chi_A=1\), with no roots or eigenvectors. The second determinant identity takes a factor \(-1\) from each of the \(n\) original rows, so its sign is also correct in dimension zero.

For any \(\lambda\in F\), Section 10.4 applied to the unchanged original matrix \(\lambda I_n-A\) proves

\[
\chi_A(\lambda)=0\quad\Longleftrightarrow\quad
\ker(\lambda I_n-A)\ne\{0\}\quad\Longleftrightarrow\quad
\exists v\ne0:\ Av=\lambda v.
\tag{FA30}
\]

The forward map is the actual free-coordinate construction (FA11), with the full original pivots of that matrix; the inverse assertion evaluates its actual nonzero vector in the kernel. This is the full determinant-characteristic-polynomial eigenvalue criterion over each original field. It does not assert that a real polynomial always has a real root. Away from roots, (FA13)--(FA14) give the actual two-sided inverse with all ordered row factors and original determinant denominator. The equality of eigenspace dimension and the number of free columns follows from the same bijection, including multiple roots and defective matrices.

An actual change of basis \(S\) gives

\[
\begin{gathered}
\chi_{S^{-1}AS}(z)=\det(S^{-1})\chi_A(z)\det S, \\ \det(S^{-1})\det S=1.
\end{gathered}
\tag{FA31}
\]

This is proved from \(zI-S^{-1}AS=S^{-1}(zI-A)S\) and full determinant multiplicativity. The two comparison factors are explicit; all roots and multiplicities agree because the product is the original unit one. Eigenvectors correspond exactly by \(v=S v'\) and its inverse; generalized kernels of any power correspond by the same full ordered product identity, which is proved by induction on that power.

For an original invariant subspace \(W\subset V\), extend its actual basis to \(V\). The operator in that basis is \(\begin{pmatrix} A_W&C\\0&A_{V/W}\end{pmatrix}\), with the actual off-diagonal block \(C\) retained. In the full permutation sum for its determinant, any term sending a lower row into an upper column has a literal zero factor. The remaining terms must send all lower rows to lower columns and all upper rows to upper columns; their signs and products factor into the two original block determinant sums. Thus

\[
\begin{gathered}
\chi_A(z)=\det S\,
 \det\begin{pmatrix}zI_W-A_W&-C\\0&zI_{V/W}-A_{V/W}\end{pmatrix}
 \det S^{-1} \\ =\det S\,\chi_{A_W}(z)\chi_{A_{V/W}}(z)\det S^{-1}.
\end{gathered}
\tag{FA32}
\]

The original block \(C\) is still part of the operator; each term containing it is accounted for by its paired lower-left zero factor. The formulas include either zero block size by the empty-product determinant. This is the exact invariant quotient comparison, not a claim that the original operator is a block-diagonal direct sum.

### 10.10. Actual receiving maps for the existing spectral and metric lessons

This lesson, Sections 9.1--9.4, already prove the original complex-root theorem with its complete leading coefficient and multiplicities. For a nonzero complex vector space, apply that proved theorem to the actual \(\chi_A\) in (FA29); (FA30) gives a nonzero eigenvector through the original pivot construction. Its line is invariant. Sections 10.1--10.3 provide the exact quotient basis and its lifts; (FA32) keeps every original block and change-of-basis factor. Induction on the original dimension now gives an upper triangular matrix for the same original complex operator. The induction starts with the empty matrix, and each lift is kept as an actual vector. This supplies the basis-extension and rank-nullity steps previously used without their full base proofs in the earlier Sections 4 and 9.6--9.7. It does not use primary spectral projections to prove the prerequisites for those projections.

For the primary spaces and nilpotent flag in [Stable modes and the algebra of boundary data](stable-boundary-models.md), Sections 16.1--16.3, Sections 10.1--10.3 now justify extending every successive kernel basis and concatenating the actual direct-sum bases. Formula (FA32) justifies the full triangular characteristic calculation with its original comparison determinants; (FA30) justifies its spectrum/eigenvalue criterion. The exact norms in Section 10.6 give boundedness of all its original coordinate and projection maps; no length of a vector in that calculation is changed. The original scalar polynomial growth and compact-contour bounds keep their separate scalar and compactness proofs.

For [Metric and topological foundations](metric-foundation-bridges.md), Section 1, its actual positive real quadratic form has the original bilinear Gram matrix \(G\). Take \(F=\mathbb R\), \(H=G\), and apply (FA16)--(FA18). The original residual matrix \(S\), lengths \(d_j\), full coordinate transformation \(U=S D^{-1/2}\), inverse \(D^{1/2}S^{-1}\), determinant \(\prod_jd_j^{-1/2}\), and original metric \(G\) are explicit. This supplies the earlier Gram construction and its volume-change factor without replacing \(G\) by an identity as the working metric. The tensor coefficients in the existing lesson's orthonormal comparison basis are received through this exact map; its tensor norm is still the original \(Q\)-norm. [Fourier transforms, finite spectra and convex separation](prerequisite-bridges.md) likewise receives the basis construction for its original real spectral induction from these formulas. Its independent compact-sphere maximization proof remains the proof of spectral decomposition.

Finally the original basis and metric adjoints used by every finite-dimensional matrix interface receive (FA24)--(FA27); an arbitrary conjugate transpose becomes an adjoint only with the actual Gram factors supplied. Projection rank and trace receive Section 10.8 with their literal original matrices. The full finite algebra used by these receiving arguments is thereby proved at the stated scalar base. The separate compactness and infinite-dimensional analytic steps retain their own hypotheses and proofs.

## 11. Matrix-entry differentiation under the integral

The measure construction and dominated-convergence proof in [Banach and Hilbert foundations](banach-foundation-bridges.md), Sections 15.0--15.1, and the complete scalar and coordinate calculus in [Metric and topological foundations](metric-foundation-bridges.md), Section 13, supply the independent entries used here. Every original matrix coordinate, operator norm, derivative order, path coefficient and endpoint is retained.

### 11.1. The exact entry map and its original operator norm

Let \(V,W\) be finite-dimensional real or complex normed spaces with their original norms and fixed original bases \((v_b)_{b=1}^n\), \((w_a)_{a=1}^m\). Let \(\lambda_b:V\to\mathbb F\) be the actual coordinate functional, so \(\lambda_b(v_c)=\delta_{bc}\). No basis vector, norm or coordinate is replaced. Define \(B_{ab}:V\to W\) by \(B_{ab}v=\lambda_b(v)w_a\). For the original arbitrary norms, use [Metric and topological foundations](metric-foundation-bridges.md), Section 12.9, (RT32)--(RT36). For a positive real dimension its actual constant \(c_v>0\) gives \(c_v|x|_2\le\|\sum_bx_bv_b\|\). Therefore \(|\lambda_b(\sum_cx_cv_c)|=|x_b|\le|x|_2\le c_v^{-1}\|\sum_cx_cv_c\|\), so \(\|\lambda_b\|\le c_v^{-1}\). For a complex basis retain the entire real basis \(v_1,iv_1,\ldots,v_n,iv_n\): \(|x_b|=((\operatorname{Re}x_b)^2+(\operatorname{Im}x_b)^2)^{1/2}\le|x|_2\), with \(c_v\) the constant of that actual real basis. The same original-norm comparison for \(W\) gives \(\|\omega_a\|\le c_w^{-1}\). These proofs retain both original norms; Section 10's Gram bounds apply separately when the given norms arise from inner products. Empty dimensions have empty functional lists and require no positive sphere constant. Thus the actual coordinate-functional norms \(\|\lambda_b\|\) are finite and
\[
\begin{gathered}
B_{ab}v=\lambda_b(v)w_a,\qquad \|B_{ab}\|=\|\lambda_b\|\,\|w_a\|,\\
H=\sum_{a=1}^m\sum_{b=1}^n H_{ab}B_{ab},\\
\|H\|\leq\sum_{a=1}^m\sum_{b=1}^n |H_{ab}|\,\|\lambda_b\|\,\|w_a\|.
\end{gathered}
\tag{MD1}
\]
For the equality of norms, the upper bound follows directly on each vector; the supremum defining \(\|\lambda_b\|\) gives the reverse bound after multiplication by the unchanged \(\|w_a\|\). For continuity of a coordinate in the reverse direction, write \(\omega_a:W\to\mathbb F\) for the corresponding coordinate functional. Then
\[
 H_{ab}=\omega_a(Hv_b),\qquad
 |H_{ab}|\leq\|\omega_a\|\,\|v_b\|\,\|H\|.
\tag{MD2}
\]
Consequently convergence of all entries is equivalent to operator-norm convergence, with every original coordinate functional and basis length retained. If either dimension is zero the unique linear map is zero, both entry sums are empty and all assertions have that exact meaning.

Let \((X,\mathcal M,\mu)\) be a complete measure space. The proof below uses only the stated dominated-convergence and absolutely integrable linearity properties, so it also applies to a measure space after completion, without a finiteness assumption on \(\mu(X)\). If every entry of \(H:X\to\operatorname{Hom}(V,W)\) is measurable and absolutely integrable, define its integral by its actual entries:
\[
\begin{gathered}
\left(\int_X H\,d\mu\right)v=\sum_{a=1}^m\sum_{b=1}^n
\left(\int_X H_{ab}\,d\mu\right)\lambda_b(v)w_a,\\
\left\|\int_X H\,d\mu\right\|\leq\sum_{a=1}^m\sum_{b=1}^n
\|\lambda_b\|\,\|w_a\|\int_X|H_{ab}|\,d\mu .
\end{gathered}
\tag{MD3}
\]
The inequality follows from (MD1) and the scalar integral bound. Under a change of either original basis, every new entry is a finite linear combination of old entries, with the actual inverse basis matrices retained. Integral linearity commutes with each such finite combination. Thus both coordinate constructions give the same map \(V\to W\); the original map and norm in (MD3) remain the working objects.

### 11.2. Every parameter derivative and its full integral map

Let \(Y\subset\mathbb R^d\) be open. Let \(r\) be a nonnegative integer or \(\infty\). Suppose \(H:Y\times X\to\operatorname{Hom}(V,W)\) has the following properties. There is one measurable null set \(N\subset X\) outside which \(y\mapsto H_{ab}(y,x)\) is \(C^r\). For every \(y\), every entry of each derivative \(\partial^\alpha H(y,\cdot)\), \(|\alpha|\leq r\), is measurable. For each closed coordinate box \(Q\) contained in \(Y\), each such multi-index and each entry, there is a nonnegative integrable \(g_{\alpha,ab,Q}\) such that
\[
\begin{gathered}
|\partial^\alpha H_{ab}(y,x)|\leq g_{\alpha,ab,Q}(x)
\quad(y\in Q,\ x\notin N),\\
\int_Xg_{\alpha,ab,Q}\,d\mu<\infty .
\end{gathered}
\tag{MD4}
\]
It is enough to require these boxes in a neighborhood of every parameter point. For \(r=\infty\), the hypothesis means every finite derivative order; it imposes no single bound on all orders at once. Values on \(N\) may be set to zero in the integral construction, leaving every map and almost-everywhere class unchanged.

Then
\[
\begin{gathered}
F(y)=\int_X H(y,x)\,d\mu(x)\quad\hbox{is }C^r,\\
\partial^\alpha F(y)=\int_X\partial^\alpha H(y,x)\,d\mu(x)
\quad(|\alpha|\leq r).
\end{gathered}
\tag{MD5}
\]
This is an equality in the original \(\operatorname{Hom}(V,W)\), not just an equality of scalar representatives.

Here is the proof at every order. Each integral exists by (MD4). Fix \(y_0\in Y\) and a box \(Q\) whose interior contains \(y_0\). For any sequence \(y_k\to y_0\), eventually \(y_k\in Q\). Outside \(N\), continuity gives \(\partial^\alpha H_{ab}(y_k,x)\to\partial^\alpha H_{ab}(y_0,x)\). Dominated convergence with the full \(g_{\alpha,ab,Q}\) proves
\[
 \int_X\left|
       \partial^\alpha H_{ab}(y_k,x)
          -\partial^\alpha H_{ab}(y_0,x)\right|\,d\mu(x)
                       \longrightarrow0 .
\tag{MD6}
\]
Equations (MD1) and (MD3), with their finite sums and original norm factors, therefore give continuity of each integral in operator norm. The sequential criterion for continuity follows from the metric definition: a failure at \(y_0\) would choose, for every positive integer \(k\), a point within \(1/k\) where the required fixed positive error persists, contradicting (MD6).

For \(|\alpha|<r\), a coordinate \(j\), and a nonzero real \(h\) with the segment from \(y_0\) to \(y_0+he_j\) inside \(Q\), the scalar coordinate fundamental theorem gives, for \(x\notin N\),
\[
\begin{gathered}
\frac{\partial^\alpha H_{ab}(y_0+he_j,x)-\partial^\alpha H_{ab}(y_0,x)}{h}
=\int_0^1\partial^{\alpha+e_j}H_{ab}(y_0+\theta he_j,x)\,d\theta ,\\
\left|\frac{\partial^\alpha H_{ab}(y_0+he_j,x)-\partial^\alpha H_{ab}(y_0,x)}{h}\right|
\leq g_{\alpha+e_j,ab,Q}(x).
\end{gathered}
\tag{MD7}
\]
The integral in this equality is the oriented coordinate formula with its substitution already performed; negative \(h\) satisfies the same equality. No product-measure interchange is used to establish its bound. Outside \(N\), the quotient tends to the indicated derivative. Dominated convergence therefore passes each sequence of nonzero \(h\)'s tending to zero through the \(X\)-integral. Linearity identifies the integral of the quotient with the difference quotient of the two original integrals. If the full limit failed, the metric definition would select a sequence of increments with persistent error. Thus the full derivative exists, and
\[
 \partial_j\left(\int_X\partial^\alpha H(y,x)\,d\mu(x)\right)
          =\int_X\partial^{\alpha+e_j}H(y,x)\,d\mu(x).
\tag{MD8}
\]
Continuity was proved in (MD6). Induction on \(|\alpha|\) proves (MD5), including all multi-indices, with mixed derivatives equal because the source functions are \(C^r\) outside the one common null set. The continuous-partials criterion in the scalar-calculus lesson supplies the full derivative tensors:
\[
 D^kF(y)[h_1,\ldots,h_k]
   =\sum_{j_1=1}^d\cdots\sum_{j_k=1}^d
       \left(\int_X
          \partial_{j_1}\cdots\partial_{j_k}H(y,x)\,d\mu(x)\right)
                    (h_1)_{j_1}\cdots(h_k)_{j_k}.
\tag{MD9}
\]
Every coordinate and every ordered source derivative remains in this finite sum. For \(k=0\) it is (MD5); for \(d=0\) no positive-order direction exists. For empty \(Y\) the assertion is vacuous, and for a zero measure space all integrals are zero. No arbitrary pointwise limit or undominated derivative has been interchanged.

### 11.3. An integrable anchor supplies the missing zeroth-order bound

When \(r\geq1\), the zeroth-order domination need not be separately assumed on a box. Fix \(y_*\in Q=\prod_{j=1}^d[a_j,b_j]\). Suppose each \(H_{ab}(y_*,\cdot)\) is absolutely integrable, and the bounds (MD4) hold for all derivatives of positive order through \(r\). Join \(y_*\) to \(y\in Q\) by the original ordered coordinate segments, replacing coordinates \(1,\ldots,d\) in that order. Apply the coordinate fundamental theorem to each segment and add its actual increment. This gives
\[
\begin{gathered}
|H_{ab}(y,x)|\leq |H_{ab}(y_*,x)|
+\sum_{j=1}^d(b_j-a_j)g_{e_j,ab,Q}(x)
=:g_{0,ab,Q}(x),\qquad x\notin N .
\end{gathered}
\tag{MD10}
\]
Its integral is finite: retain the anchor's full integral, every original side length, and all \(d\) derivative integrals. Thus (MD4) at order zero follows, and the preceding proof applies. For \(d=0\) the sum is empty and the anchor is the only point. This weakens a sufficient hypothesis without changing the original function or requiring the ambient measure to be finite. For \(r=0\), integrability at one parameter alone does not provide domination in a neighborhood, so the continuity proof retains its stated order-zero bound.

### 11.4. The Riemann integral, each path piece and every cycle coefficient

For a continuous scalar function \(f\) on \([a,b]\), the original oriented Riemann integral from the scalar-calculus lesson equals its Lebesgue integral. To prove this comparison when \(a<b\), choose any partition. The lower and upper step functions bound \(f\) on each open subinterval, using its original infimum and supremum there. The finitely many endpoints form a Lebesgue null set, by the constructed coordinate-box measure. Their step integrals are exactly the lower and upper Darboux sums, since every interval has its unchanged length. Continuous \(f\) is Borel measurable and bounded; hence it is integrable on this finite interval. Its Lebesgue integral lies between these two sums. Uniform continuity makes their difference tend to zero along partitions with mesh tending to zero, by the full interval length times the original oscillation bound. The common limit is exactly the Riemann integral proved in Section 13.3. Apply this argument to real and imaginary parts and then to all matrix entries. For \(a=b\) both integrals are zero; for a reversed interval retain the minus sign in the oriented formula.

For the remaining contour assertions in Sections 11.4--11.5, take \(V,W\) to be complex normed spaces and the operators to be complex linear. Sections 11.1--11.3 retain their original real-or-complex scope. This target hypothesis is required for multiplication by the actual complex path derivative. For example, with real \(V=W=\mathbb R\), \(G(z)=\operatorname{Re}(z)I\), and the positively oriented unit circle \(\gamma(\theta)=e^{i\theta}\), the coordinate integral in the complex target is
\[
 \int_0^{2\pi}\cos\theta(-\sin\theta+i\cos\theta)\,d\theta
 =-\left[\frac{\sin^2\theta}{2}\right]_0^{2\pi}
  +i\int_0^{2\pi}\frac{1+\cos(2\theta)}2\,d\theta
 =i\pi.
 \tag{MD11a}
\]
The real fundamental theorem and the actual trigonometric identities prove every displayed term. The result is outside the real endomorphism space, so no real-target contour assertion is inferred. The actual resolvent applications already have complex targets.

Write a finite cycle in its actual form
\[
 \Gamma=\sum_{\ell=1}^L m_\ell\gamma_\ell,\qquad
 m_\ell\in\mathbb Z,\qquad
 \gamma_\ell:[a_\ell,b_\ell]\to\mathbb C .
\tag{MD11}
\]
Each path is closed and piecewise \(C^1\), with its finite partition retained; \(a_\ell<b_\ell\). Split it at those partition endpoints without changing the sum or orientation. The path derivative is continuous on each closed smooth piece, with one-sided endpoint values sufficient for its integral. Define
\[
 \int_\Gamma G(y,z)\,dz
       =\sum_{\ell=1}^L m_\ell
          \int_{a_\ell}^{b_\ell}
             G(y,\gamma_\ell(s))\,\gamma_\ell'(s)\,ds .
\tag{MD12}
\]
By the preceding comparison, both integral conventions give this same map. The signed \(m_\ell\) remain in the equality; their absolute values enter only the estimate
\[
 \left\|\int_\Gamma G(y,z)\,dz\right\|
       \leq\sum_{\ell=1}^L |m_\ell|
          \int_{a_\ell}^{b_\ell}
             \|G(y,\gamma_\ell(s))\|\,|\gamma_\ell'(s)|\,ds .
\tag{MD13}
\]
This bound can also be proved directly from tagged matrix Riemann sums and the triangle inequality in the unchanged operator norm, followed by their limits. It retains the actual speed and every piece's interval; zero coefficients contribute zero.

If \(G\) and each parameter derivative through order \(r\) are continuous jointly on a neighborhood of the product of a compact parameter box and all path images, (MD4) follows entry by entry from their actual compact maximum times \(|m_\ell|\,|\gamma_\ell'(s)|\). Its integral is finite because each piece is \(C^1\) on a compact interval. Apply (MD5) on the finite disjoint union of these intervals, with the original signed coefficients in the integrands, to obtain
\[
\begin{gathered}
\partial^\alpha\int_\Gamma G(y,z)\,dz
=\sum_{\ell=1}^L m_\ell\int_{a_\ell}^{b_\ell}
\partial^\alpha G(y,\gamma_\ell(s))\gamma_\ell'(s)\,ds\\
=\int_\Gamma\partial^\alpha G(y,z)\,dz .
\end{gathered}
\tag{MD14}
\]
The finitely many path-piece endpoints may be taken as the common null exceptional set. No eigenvalue branch, contour deformation or holomorphic integral theorem is needed for this parameter interchange.

### 11.5. The actual ordered resolvent, time derivatives and upper-contour bound

Use the original open parameter set \(Y\), operator family \(A:Y\to\operatorname{End}(V)\), fixed finite cycle \(\Gamma\), and \(C^r\) hypotheses of the polynomial and contour lesson, Section 7. For every contour point and parameter, \(zI-A(y)\) is invertible. The full finite algebra proves
\[
\begin{gathered}
R(y,z)=(zI-A(y))^{-1}
=\frac{\operatorname{adj}(zI-A(y))}{\det(zI-A(y))},\\
\partial_jR=R(\partial_jA)R 
\end{gathered}
\tag{MD15}
\]
with the original determinant, adjugate signs and matrix order. Joint continuity and compactness bound the denominator away from zero and bound every actual numerator derivative on each parameter box times the fixed contour. The original multi-index product calculation gives, for \(0<|\beta|\leq r\),
\[
 \partial^\beta R
     =\sum_{0<\eta\leq\beta}
        \binom{\beta}{\eta}
              R(\partial^\eta A)(\partial^{\beta-\eta}R).
\tag{MD16}
\]
Indeed differentiate \((zI-A)R=I\), keep every Leibniz term, isolate the term \((zI-A)\partial^\beta R\), and multiply on its left by \(R\). All other derivatives of \(zI-A\) are \(-\partial^\eta A\), so the two signs give the displayed positive terms. Induction establishes existence, continuity and compact bounds at every permitted order. Thus (MD14) proves the exact interchange asserted in the existing Section 7, instead of leaving dominated differentiation as an unproved entry.

For the original real time parameter, define
\[
 T_j(t,y)=\frac{1}{2\pi i}\int_\Gamma
                     (iz)^j e^{itz}R(y,z)\,dz,\qquad j\geq0 .
\tag{MD17}
\]
The original exponential series and derivative prove \(\partial_t^j e^{itz}=(iz)^j e^{itz}\). On every compact \(t\)-interval and parameter box, all time and allowed parameter derivatives have the integrable majorants established above. For each fixed \(j\), apply (MD5) in the original \(y\) coordinates through order \(r\) to the integrand \((iz)^j e^{itz}R(y,z)\). Its dependence on \(t\) has derivatives of every finite order independently of the allowed \(y\) order. For each \(\beta\), successive one-variable dominated difference quotients in \(t\), with the full compact bounds already proved, then give the time derivatives. The same compact bounds give joint continuity of every such mixed derivative. Thus no joint \(C^{r+j}\) regularity of \(A\) is assumed. For every \(j\) and \(|\beta|\leq r\), these separate actual passages give
\[
\begin{gathered}
\partial_t^j\partial_y^\beta T_0(t,y)=\partial_y^\beta T_j(t,y)\\
=\frac{1}{2\pi i}\int_\Gamma (iz)^j e^{itz}
\partial_y^\beta R(y,z)\,dz .
\end{gathered}
\tag{MD18}
\]
Every power of \(i\), every \(z\), the exact \(1/(2\pi i)\), and the original ordered products from (MD16) remain. If all path points have \(\operatorname{Im}z\geq\delta>0\), the scalar series identity gives \(|e^{itz}|=e^{-t\operatorname{Im}z}\leq e^{-\delta t}\) for \(t\geq0\). Equation (MD13) then gives the complete estimate
\[
 \|\partial_y^\beta T_j(t,y)\|
   \leq\frac{e^{-\delta t}}{2\pi}
       \sum_{\ell=1}^L |m_\ell|
          \int_{a_\ell}^{b_\ell}
              |\gamma_\ell(s)|^j
              \|\partial_y^\beta R(y,\gamma_\ell(s))\|
              |\gamma_\ell'(s)|\,ds .
\tag{MD19}
\]
The right side retains the full contour, original norm, every cycle coefficient, derivative product, speed, endpoint and spectral gap. Supremizing its displayed coefficient over a compact parameter box is finite by the previously proved bounds. Dimension zero gives the zero operator and zero integrals. The construction proves the existing fixed-contour derivative and decay receiving maps; it supplies no general trace theorem or new boundary calculus.

## References

Thomas W. Judson, [*Abstract Algebra: Theory and Applications*, polynomial chapter](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/poly.xml), gives the scalar division and Bézout proofs used in Section 2.

Robert A. Beezer, [*A First Course in Linear Algebra*, Section OD](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-OD.xml), gives the upper-triangularization result used in Section 4.

Jiří Lebl, [*Guide to Cultivating Complex Analysis*, version 1.9](https://github.com/jirilebl/ca/blob/adfaaf8b13287185c22db079f16f39183628f482/ca.tex), treats line integrals and winding numbers. Section 5 proves the exact contour moments needed here.

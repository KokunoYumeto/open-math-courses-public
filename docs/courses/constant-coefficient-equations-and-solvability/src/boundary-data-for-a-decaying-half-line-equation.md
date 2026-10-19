# Boundary data for a decaying half-line equation

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The upper roots of a normal polynomial generate the solutions that decay into the positive half-line. Boundary conditions determine these modes through their remainders modulo that upper factor. We prove the exact criterion for arbitrary data, its contour determinant, the anti-causal forcing formula and a polynomial formula for every boundary jet. Repeated roots need no separate nondegeneracy assumption.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) supplies the complex Green identity.

All scalar ODE, repeated-mode, residue-pairing and boundary-jet arguments needed here are proved in this lesson.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## The function class and the two factors

Use \(D=-i\,d/dt\). Let \(p\) be monic, with complex coefficients and no real root. Factor it, including multiplicities, as
\[
\begin{gathered}
p(z)=p_+(z)p_-(z),\\
\qquad
 \deg p_+=h,\\
\quad\deg p_-=\ell,
\end{gathered}
\tag{1}
\]
where the two factors are monic and their roots have positive and negative imaginary parts, respectively. A degree-zero factor is one. Let \(\mathcal S_+\) consist of the smooth functions on \([0,\infty)\) whose every right derivative at zero exists and which satisfy
\[
\begin{gathered}
\sup_{t\ge0}(1+t)^a|u^{(b)}(t)|<\infty
 \\
\quad(a,b\in\mathbb Z_{\ge0}).
\end{gathered}
\tag{2}
\]
The right derivatives are understood as continuous derivatives up to the endpoint. Restriction of a Schwartz function on the full line lies in this class.

For \(f\in\mathcal S(\mathbb R)\), polynomials \(b_1,\ldots,b_\mu\), and arbitrary complex numbers \(\phi_j\), consider
\[
\begin{gathered}
p(D)u=f\\
\quad(t>0),\\
\qquad
 b_j(D)u(0)=\phi_j\\
\quad(1\le j\le\mu),\\
\qquad
 u\in\mathcal S_+.
\end{gathered}
\tag{3}
\]
Only \(f|_{[0,\infty)}\) is prescribed by the equation. Using a full-line \(f\) supplies a convenient particular solution, and will not impose an extra condition on its negative-time values.

The rational function \(1/p(\xi)\) is smooth on the real line and each derivative has at most polynomial growth there. Indeed its denominator factors stay away from zero on every bounded interval, and its asymptotic expansion at infinity gives a power bound. Leibniz's rule makes multiplication by \(1/p\) preserve Schwartz functions. By the Fourier inversion theorem, the function
\[
\begin{gathered}
u_0=\mathcal F^{-1}(\widehat f/p)
 \\
\quad\text{belongs to }\mathcal S(\mathbb R),\\
\qquad
 p(D)u_0=f.
\end{gathered}
\tag{4}
\]
Every solution of 3 is therefore \(u_0+v\), where \(p(D)v=0\) on the positive half-line and its boundary data are
\(\psi_j=\phi_j-b_j(D)u_0(0)\).

## All homogeneous modes, including multiplicities

For a monic polynomial \(a(z)=z^r+\sum_{k<r}a_kz^k\), the Cauchy data
\((v(0),Dv(0),\ldots,D^{r-1}v(0))\) specify a unique smooth solution of \(a(D)v=0\). For \(r>0\), write this equation as
\[
\begin{gathered}
Y'=iCY,\\
\qquad
 Y=(v,Dv,\ldots,D^{r-1}v)^T,
 \\
\quad
 C=
 \begin{pmatrix}
 0&1& &0\\
  &0&\ddots&\\
 0&&0&1\\
 -a_0&-a_1&\cdots&-a_{r-1}
 \end{pmatrix}.
\end{gathered}
\tag{5}
\]
The series \(e^{itC}=\sum_{k\ge0}(itC)^k/k!\) converges with every derivative on bounded intervals and solves the system for arbitrary \(Y(0)\). To prove uniqueness without importing an ODE theorem, integrate the equation for a solution with zero initial value. On an interval of length \(\delta<1/\|C\|\), its supremum norm is at most \(\delta\|C\|\) times itself, so it is zero. Repeat on adjacent intervals, in either direction. If \(C=0\), the equation itself gives constancy. The first \(r-1\) rows ensure that the first component's successive \(D\)-derivatives are the remaining components, and the last row is \(a(D)v=0\).

If the roots of \(a\) are \(\lambda\), with multiplicities \(r_\lambda\), its solutions are exactly
\[
\begin{gathered}
v(t)=\sum_\lambda e^{i\lambda t}A_\lambda(t),
 \\
\qquad \deg A_\lambda<r_\lambda .
\end{gathered}
\tag{6}
\]
Every displayed term solves the equation because
\((D-\lambda)(e^{i\lambda t}A)=e^{i\lambda t}DA\).
They are linearly independent. To isolate a chosen root \(\lambda\) from an alleged relation, apply
\(\prod_{\nu\ne\lambda}(D-\nu)^{r_\nu}\). All other terms disappear. On the polynomial space of degree less than \(r_\lambda\), each remaining operator \(D+\lambda-\nu\) has an upper triangular matrix with nonzero constant diagonal and is invertible. The chosen polynomial must therefore be zero. The number of independent functions is \(\sum r_\lambda=r\), which equals the solution-space dimension from 5. This proves 6.

The bounded solutions of \(p(D)v=0\) on the positive half-line have only upper-root terms. Here is a cancellation check that also proves this for repeated roots. If a nonzero lower-root term occurs, choose the largest growth exponent \(a=-\operatorname{Im}\lambda>0\) among all nonzero terms, and the largest polynomial degree \(k\) among terms with that exponent. Then
\[
\begin{gathered}
e^{-at}t^{-k}v(t)
       =\sum_{\nu=1}^r c_\nu e^{ib_\nu t}+o(1),
 \\
\quad c_\nu\ne0,\\
\quad b_\nu\text{ distinct real}.
\end{gathered}
\tag{7}
\]
A bounded \(v\) makes the left side tend to zero. The error tends to zero because smaller growth exponents have exponential suppression, and smaller degrees lose a power of \(t\). Thus the finite oscillatory sum tends to zero. But
\[
\begin{gathered}
\lim_{T\to\infty}\frac1T\int_0^T
       \left|\sum_{\nu=1}^r c_\nu e^{ib_\nu t}\right|^2dt
       \\
=\sum_{\nu=1}^r|c_\nu|^2>0:
\end{gathered}
\tag{8}
\]
each cross integral divided by \(T\) is bounded by
\(2/(T|b_\nu-b_\kappa|)\), while the diagonal integrals are \(|c_\nu|^2\). A bounded function tending to zero has squared Cesàro mean zero, by splitting off a fixed initial interval. This contradiction excludes the growing terms. Conversely every upper-root term and all its derivatives decrease exponentially times a polynomial, so belong to \(\mathcal S_+\). Hence
\[
\begin{gathered}
\{v\in\mathcal S_+:p(D)v=0\}
       \\
=\{v:p_+(D)v=0\},
 \\
\dim=h.
\end{gathered}
\tag{9}
\]
For \(h=0\), this is the zero space.

## Boundary remainders and the exact count

Divide each boundary symbol by the monic upper factor:
\[
 b_j=q_jp_++r_j,\qquad \deg r_j<h.
 \tag{10}
\]
On a homogeneous decaying solution \(v\), \(b_j(D)v(0)=r_j(D)v(0)\). 5 identifies its first \(h\) jets with an arbitrary vector in \(\mathbb C^h\), so the boundary map is precisely the \(\mu\)-by-\(h\) matrix of the coefficients of \(r_j\) in the basis \(1,z,\ldots,z^{h-1}\).

Consequently 3 has a unique solution for every \((\phi_1,\ldots,\phi_\mu)\) if and only if
\[
\begin{gathered}
\mu=h,\\ {}
[b_1],\ldots,[b_h]\text{ form a basis of }
       \\
\mathbb C[z]/(p_+).
\end{gathered}
\tag{11}
\]
Necessity follows because an injective and surjective linear map between these finite-dimensional spaces has equal dimensions and full rank. Sufficiency follows by solving the \(h\)-jet system and using 5–9. If the map is injective with \(\mu>h\), arbitrary data need not be attainable; if it is surjective with \(\mu<h\), homogeneous solutions remain. For \(h=\mu=0\), the empty boundary map is an isomorphism of zero spaces and \(u_0|_{[0,\infty)}\) is the unique solution.

## A residue pairing that does not lose repeated roots

For \(h\ge1\), take a positive circle containing all roots of \(p_+\), and define the complex bilinear form
\[
 \beta(a,b)=\frac1{2\pi i}\int_{\mathcal C}
                  \frac{a(z)b(z)}{p_+(z)}\,dz.
 \tag{12}
\]
It descends to \(\mathbb C[z]/(p_+)\) in both variables: replacing either polynomial by a multiple of \(p_+\) leaves a polynomial integrand, whose integral is zero by the complex Green identity. The same identity on annuli permits a larger circle without changing the integral. On a sufficiently large circle the uniformly convergent expansion at infinity gives
\[
 \beta(a,b)=[z^{-1}]\,\frac{a(z)b(z)}{p_+(z)}.
 \tag{13}
\]
The notation means the coefficient of \(z^{-1}\) in the Laurent series. Integrating each Laurent monomial proves the equality, including its sign and normalization.

Let \(G_{jk}=\beta(z^j,z^k)\), \(0\le j,k<h\). Since \(p_+\) is monic,
\[
\begin{gathered}
G_{jk}=0\ (j+k<h-1),\\
\qquad
 G_{jk}=1\ (j+k=h-1),\\
\qquad
 \det G=(-1)^{h(h-1)/2}.
\end{gathered}
\tag{14}
\]
Reverse the columns to get a triangular matrix with diagonal one; the reversing permutation has \(h(h-1)/2\) inversions. Thus the pairing is nondegenerate even when all roots coincide.

Define the Lopatinski matrix and determinant by
\[
\begin{gathered}
M_{jk}=\beta(b_j,z^{k-1}),\\
\quad 1\le j,k\le h,
 \\
\qquad L(b_1,\ldots,b_h;p_+)=\det M.
\end{gathered}
\tag{15}
\]
If \(R\) is the matrix of the remainders in 10, then \(M=RG\), whence
\[
 L=(-1)^{h(h-1)/2}\det R.
 \tag{16}
\]
Thus \(L\ne0\) is exactly 11. For \(h=0\), set \(L=1\), the determinant of the empty matrix; no pairing is needed.

All entries of \(M\) are polynomials in the coefficients of \(b_j\) and of the monic \(p_+\). Indeed write
\[
 \frac1{p_+(z)}
   =z^{-h}\sum_{\nu\ge0}
        \left(1-\frac{p_+(z)}{z^h}\right)^\nu .
 \tag{17}
\]
The parenthesis has strictly negative powers of \(z\). Each needed Laurent coefficient is therefore a finite polynomial expression in the coefficients of \(p_+\); only finitely many \(\nu\)'s contribute. The numerators are finite polynomials as well. The determinant is a polynomial in these entries.

For real \(a\), simultaneously replace \(p_+(z)\) and all \(b_j(z)\) by \(p_+(z-a)\) and \(b_j(z-a)\). The substitution \(y=z-a\) changes the monomial \(z^{k-1}\) to \((y+a)^{k-1}\). In the basis \(1,y,\ldots,y^{h-1}\), this change has a triangular matrix with diagonal one, so
\[
\begin{gathered}
L(b_1(\cdot-a),\ldots,b_h(\cdot-a);
       \\
p_+(\cdot-a))\\
=L(b_1,\ldots,b_h;p_+).
\end{gathered}
\tag{18}
\]
The contour can be translated because it still encloses the same shifted roots. The polynomial identity actually holds for complex \(a\) too; restricting to real \(a\) ensures that the upper-root interpretation is preserved.

## An anti-causal inverse fixes the forcing part

For a lower root \(\lambda\), the locally integrable kernel
\[
\begin{gathered}
E_\lambda(t)=-i\,\mathbf1_{\{t\le0\}}e^{i\lambda t},
 \\
\qquad (D-\lambda)E_\lambda=\delta_0
\end{gathered}
\tag{19}
\]
has negative support and decreases exponentially as \(t\to-\infty\). The sign follows from
\(d\mathbf1_{\{t\le0\}}/dt=-\delta_0\) and \(D=-i\,d/dt\).
For \(\ell>0\), convolve the \(\ell\) kernels counted with multiplicity to obtain \(E_-\). All convolutions are absolutely integrable and supported in the negative half-line. Choosing \(c>0\) smaller than every \(-\operatorname{Im}\lambda\), their absolute values are bounded by a constant times
\(\mathbf1_{\{t\le0\}}(1+|t|)^{\ell-1}e^{-c|t|}\).
To verify this, each convolution over \(t=y_1+\cdots+y_\ell\), \(y_j\le0\), has an \((\ell-1)\)-simplex of length \(|t|\), whose volume is \(|t|^{\ell-1}/(\ell-1)!\); the common exponential factors multiply to \(e^{-c|t|}\). For \(\ell=0\), put \(E_-=\delta_0\).

Applying the first-order identity successively gives
\(p_-(D)E_-=\delta_0\). Fubini is justified by the exponential bound and compact test functions; alternatively it follows from the proper-support convolution identity. Set
\[
\begin{gathered}
g(t)=(f*E_-)(t)
       \\
=\int_{-\infty}^0f(t-y)E_-(y)\,dy
       \\
(\ell>0),\\
g=f\\
(\ell=0).
\end{gathered}
\tag{20}
\]
This is a Schwartz function on the full line. Differentiate \(f\) under the integral and use
\((1+|t|)^a\le(1+|t-y|)^a(1+|y|)^a\);
every weighted kernel moment is finite. Distributional differentiation gives \(p_-(D)g=f\).

For any solution \(u\) of 3, the function \(p_+(D)u-g\) is in \(\mathcal S_+\) and is annihilated by \(p_-(D)\). 7–9, now with no upper root, force it to vanish. Therefore
\[
 p_+(D)u=g\quad\text{on }[0,\infty).
 \tag{21}
\]
The formula uses only values \(f(t-y)\) with \(t-y\ge t\ge0\). Thus changing the negative-time extension of \(f\) changes neither \(g\) on this half-line nor the eventual unique solution with the same boundary values. Although an anti-causal convolution looks towards larger \(t\), it is precisely what removes the growing lower-root modes.

## Polynomial reconstruction of every boundary jet

Assume \(\mu=h\). For each integer \(j\ge0\), let \(v_j\) be the row
\((\beta(z^j,1),\ldots,\beta(z^j,z^{h-1}))\). Put
\[
 (t_{j1},\ldots,t_{jh})=v_j\,\operatorname{adj}M.
 \tag{22}
\]
The adjugate identity gives
\((t_{j1},\ldots,t_{jh})M=L v_j\).
It follows that \(Lz^j-\sum_k t_{jk}b_k\) pairs to zero with every basis monomial. Nondegeneracy of 14 makes its remainder modulo \(p_+\) zero. Monic division therefore defines a polynomial \(s_j(z)\) such that
\[
\begin{gathered}
Lz^j=\sum_{k=1}^h t_{jk}b_k(z)\\
+p_+(z)s_j(z),
 \\
\deg s_j\\
\le\max(j,\deg b_1,\ldots,\deg b_h)-h.
\end{gathered}
\tag{23}
\]
A negative degree bound means \(s_j=0\). Write \(s_j(z)=\sum_{r\ge0}s_{jr}z^r\); only \(h+r\le\max(j,\deg b_1,\ldots,\deg b_h)\) can occur. All \(t_{jk}\) and \(s_{jr}\) are polynomials in the coefficients of \(p_+\) and \(b_k\): 17 proves this for \(v_j,M\), the adjugate is polynomial, and division by a monic polynomial requires only subtraction and multiplication of coefficients. This algebraic identity does not require \(L\ne0\). At \(h=0\), it holds with \(L=1\), an empty first sum and \(s_j=z^j\).

Apply 23 at \(D\) to \(u\), use its boundary values and 21, and take the right trace at zero:
\[
\begin{gathered}
L D^j u(0)\\
= \sum_{k=1}^h t_{jk}\phi_k
       +\sum_{r\ge0}s_{jr}D^r g(0).
\end{gathered}
\tag{24}
\]
This is the full all-order boundary-jet formula, with the original derivative phase and finite degree bound. When \(L\ne0\), it reconstructs every jet from the prescribed boundary values and the forcing. No inverse determinant was hidden in the coefficient formulas.

## Exercises with complete solutions

**Exercise 1 (entry: a repeated upper root).** Let \(p=(z-i)^2(z+2i)\), \(b_1=1\), \(b_2=z\). Compute \(L\), describe every homogeneous decaying solution, and find the second-jet identity in terms of \(\phi_1,\phi_2\) and \(g\).

**Solution.** \(p_+=(z-i)^2=z^2-2iz-1\), \(p_-=z+2i\). The pairings give
\[
 M=\begin{pmatrix}0&1\\
1&2i\end{pmatrix},
 \qquad L=-1.
 \tag{25}
\]
The two boundary classes are a basis, despite the repeated root. Every homogeneous decaying solution is \(v(t)=e^{-t}(A+Bt)\). Its traces are \(v(0)=A\) and \(Dv(0)=iA-iB\). Thus arbitrary homogeneous data \(\psi_1,\psi_2\) give
\(A=\psi_1\), \(B=\psi_1+i\psi_2\), proving uniqueness explicitly. The identity \(z^2=1+2iz+p_+\) and 21 yield
\(D^2u(0)=\phi_1+2i\phi_2+g(0)\).
In the adjugate normalization, \(t_{21}=-1,t_{22}=-2i,s_2=-1\), exactly as 23 with \(L=-1\).

**Exercise 2 (intermediate: too few, too many and dependent data).** Keep the same \(p\). Compare prescribing only \(u(0)\), prescribing \(u(0),Du(0),D^2u(0)\), and prescribing \(u(0),p_+(D)u(0)\). Identify the compatibility or nonuniqueness explicitly.

**Solution.** Only \(u(0)\) fixes \(A\) in the homogeneous correction while leaving \(B\) free, so there is nonuniqueness. Three jets contain the compatible relation
\(D^2u(0)=u(0)+2iDu(0)+g(0)\), so arbitrary triples cannot be solved, although a compatible triple determines the solution. The two symbols \(1,p_+\) have remainders \(1,0\), so the boundary matrix has rank one and \(L=0\). The second prescribed datum must equal \(g(0)\), by 21. When it does, the first fixes \(A\) while \(B\) remains free. Matching the number of conditions to two therefore does not suffice; their classes must also be independent.

**Exercise 3 (advanced: confluence and shifts).** Show that for any monic \(p_+\) of degree \(h\), the consecutive jet symbols \(1,z,\ldots,z^{h-1}\) have determinant \((-1)^{h(h-1)/2}\), independent of every root. For \(h=3\), compare this with a determinant of values at distinct roots and explain its coalescing limit.

**Solution.** Their remainder matrix is the identity, so 16 gives the asserted constant. For \(h=3\), it is \(-1\), including \(p_+=(z-i)^3\). For distinct roots \(\lambda_1,\ldots,\lambda_h\), simple residue evaluation in 12 yields
\[
\begin{gathered}
M_{jk}=\sum_{\nu=1}^h
       \frac{b_j(\lambda_\nu)\lambda_\nu^{k-1}}
            {p_+'(\lambda_\nu)},\\
L=(-1)^{h(h-1)/2}
       \\
\frac{\det(b_j(\lambda_\nu))_{j,\nu}}
            {\prod_{\nu<\kappa}(\lambda_\kappa-\lambda_\nu)}.
\end{gathered}
\tag{26}
\]
To check the sign, factor \(M=B\,\operatorname{diag}(1/p_+'(\lambda_\nu))V^T\), where \(V_{k\nu}=\lambda_\nu^{k-1}\). The determinant of \(V\) is the Vandermonde product in the denominator, and the product of all \(p_+'(\lambda_\nu)\) is \((-1)^{h(h-1)/2}\) times its square. For consecutive jets, \(\det B\) is the same Vandermonde product, so the quotient is one. As roots coalesce, the two vanishing factors cancel; the contour determinant's polynomial coefficient formula extends with the same nonzero constant. Treating the value determinant alone as the boundary criterion would incorrectly lose the repeated-root case. 18 further proves invariance under real simultaneous shifts, which preserve the decaying-mode interpretation.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.

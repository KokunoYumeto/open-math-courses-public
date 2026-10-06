# Euler equations and the order of singularities

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

The Euler equation records scaling. Repeating its operator produces powers of the logarithm, but the resulting chains do not have larger distributional order. The distinction that matters is whether a solution remains nonzero away from the origin. We prove the complete classification, the exceptional maps at degree zero, and the exact orders, including two tensor examples where adding the separate orders gives an unnecessarily large bound.

Our proof inputs are [Order, positivity and distributional limits](order-positivity-and-limits.md), Section 1 and its finite-\(C^k\) extension; [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2; [Finite parts of singular powers](finite-parts-of-singular-powers.md); [Complex powers at a boundary](complex-powers-at-a-boundary.md); and [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), with its [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5. Those lessons supply the scalar power families, exact point jets, polar integration and all their underlying calculus. The zero-derivative theorem, polynomial factorization and the particular tensor constructions needed here are proved below.

## Two elementary ways to solve an equation

We use complex-linear distributions. On the real line write
\[
 E=x\partial_x,\qquad
 Z(a,q)=\ker(E-a)^q,\qquad Z(a,0)=\{0\},
 \quad a\in\mathbb C,\quad q\ge1.
 \tag{1.1}
\]

**Zero-derivative fact.** On any open interval \(I\), a distribution \(w\) with \(w'=0\) is constant. Indeed, every compact test \(\phi\) of integral zero has a compact primitive inside \(I\), obtained by integrating from a point to the left of its support. Hence \(w\) annihilates such tests. Choose a compact test \(\rho\) in \(I\) with integral one. Applying this observation to \(\phi-\rho\int_I\phi\) gives \(w(\phi)=w(\rho)\int_I\phi\), as claimed. The primitive is smooth by the fundamental theorem and vanishes on both sides of the support because the integral is zero.

**Lemma 1.1 (a primitive and division by the coordinate).** Every distribution on \(\mathbb R\) is a derivative, and every distribution is \(xv\) for some distribution \(v\). The two ambiguities are, respectively, constants and multiples of \(\delta_0\).

**Proof.** Fix \(\rho\in\mathcal D(\mathbb R)\) with integral one, and define
\[
 I\phi(x)=\int_{-\infty}^x
       \left(\phi(t)-\rho(t)\int_{\mathbb R}\phi\right)dt.
 \tag{1.2}
\]
The integrand has integral zero. Thus \(I\phi\) is supported in the interval containing the supports of \(\phi\) and \(\rho\). On any fixed test-support space, that interval is fixed. Its zeroth norm is bounded by its length times the integrand's sup norm, and its higher derivatives are derivatives of the integrand. This proves every required seminorm bound. Consequently \(v(\phi)=-u(I\phi)\) is a distribution. Since \(\int\phi'=0\) and \(I(\phi')=\phi\), its derivative is \(u\). The zero-derivative fact proves the ambiguity.

For division choose \(\chi\in\mathcal D(\mathbb R)\) equal to one near zero and put
\[
 J\phi(x)=\frac{\phi(x)-\phi(0)\chi(x)}x.
 \tag{1.3}
\]
Near zero the quotient is \(\int_0^1\phi'(tx)\,dt\); its \(j\)-th derivative is \(\int_0^1t^j\phi^{(j+1)}(tx)\,dt\), by bounded difference quotients. Away from zero the ordinary product rule bounds it by finitely many test derivatives. Its support lies in the fixed union of the original support and \(\operatorname{supp}\chi\). Hence \(v(\phi)=u(J\phi)\) is a distribution, and \(J(x\phi)=\phi\) proves \(xv=u\). If \(xw=0\), the identity \(\phi=\phi(0)\chi+xJ\phi\) gives \(w(\phi)=w(\chi)\phi(0)\). Conversely \(x\delta_0=0\). This proves the second ambiguity directly. \(\square\)

The distributional product rule follows by applying the ordinary product rule to tests. It yields
\[
 \begin{aligned}
 E\partial_x&=\partial_x(E-1),& Ex&=x(E+1),\\
 x\partial_x&=E,& \partial_xx&=E+1.
 \end{aligned}
 \tag{1.4}
\]
Thus differentiation takes \(Z(a,q)\) to \(Z(a-1,q)\), and multiplication by \(x\) takes it to \(Z(a+1,q)\).

## Homogeneous solutions and logarithmic chains

Let \(H_+\) and \(H_-\) be the locally integrable indicators of the positive and negative half-lines. Write \(Ru(\phi)=u(\phi(-\cdot))\), and use the proved families
\[
 U_b=x_+^b,\qquad S_k=\operatorname{pf}(1/x^k),
 \qquad B_\pm(b)=(x\pm i0)^b.
 \tag{2.1}
\]
Here \(U_b\) is meromorphic and has no assigned value at a pole; \(S_k\) is the symmetric finite part of U016; and \(B_\pm\) are the entire distribution families of U017.

**Theorem 2.1 (the two homogeneous solutions).** For every complex \(a\), \(Z(a,1)\) has dimension two. Off zero its members have the form
\[
 u(x)=A_+x^a\quad(x>0),\qquad
 u(x)=A_-|x|^a\quad(x<0).
 \tag{2.2}
\]
If \(a\notin\{-1,-2,\ldots\}\), a basis is \(U_a,RU_a\). At \(a=-k\), \(k\ge1\), a basis is \(S_k,\delta_0^{(k-1)}\), and the coefficients obey \(A_-=(-1)^kA_+\). The nonzero solutions supported at zero exist exactly at these negative integers and are multiples of the indicated jet.

For \(a\ne0\),
\[
 \partial_x:Z(a,1)\longrightarrow Z(a-1,1)
 \quad\hbox{is an isomorphism with inverse }x/a.
 \tag{2.3}
\]
At zero, \(Z(0,1)=\operatorname{span}\{H_+,H_-\}\), its derivative image is \(\mathbb C\delta_0\), and \(xZ(-1,1)\) is the space of constant distributions.

**Proof.** U018, Lemma 1.1, proves Euler/scaling equivalence. On either half-line the product rule gives \((|x|^{-a}u)'=0\), since \(u'=a u/x\). The zero-derivative fact therefore proves (2.2).

At nonexceptional \(a\), the two meromorphic values have the independent pairs of half-line coefficients \((1,0)\) and \((0,1)\). Subtracting their matching combination leaves a point-supported distribution. U018, foundation A3, proves that it is a finite sum of independent jets and that
\[
 E\delta_0^{(j)}=-(j+1)\delta_0^{(j)}.
 \tag{2.4}
\]
No such jet has eigenvalue \(a\), so the difference is zero.

At \(a=-k\), U018, Theorem 4.1, gives the necessary and sufficient angular moment condition on the two-point sphere:
\(A_++(-1)^{k-1}A_-=0\).
The symmetric finite part has coefficients \(1,(-1)^k\). After subtracting \(A_+S_k\), (2.4) leaves exactly a multiple of \(\delta_0^{(k-1)}\). These two terms are independent because only the second is supported at zero.

On the source of (2.3), \(x\partial_x=a\); on its target, \(\partial_xx=a\). These identities prove both inverse compositions. Finally, the endpoint fundamental theorem gives \(H_+'=\delta_0\) and \(H_-'=-\delta_0\). U016's symmetric formula gives \(xS_1=1\), while \(x\delta_0=0\). The claimed critical images follow. \(\square\)

Near a fixed \(a\), choose two holomorphic families \(A_1(b),A_2(b)\). Use \(U_b,RU_b\) at a nonexceptional \(a\), and \(B_+(b),B_-(b)\) at \(a=-k\). In the latter case U017 proves
\[
 B_\pm(-k)=S_k\mp
 i\pi\frac{(-1)^{k-1}}{(k-1)!}\delta_0^{(k-1)},
 \tag{2.5}
\]
so their values are independent. In every case \((E-b)A_i(b)=0\). Put
\[
 v_{i,j}=\frac1{j!}\left.\partial_b^j A_i(b)\right|_{b=a},
 \qquad j\ge0,\qquad v_{i,-1}=0.
 \tag{2.6}
\]

**Theorem 2.2 (complete generalized Euler spaces).** The \(2q\) distributions \(v_{i,j}\), \(i=1,2\), \(0\le j<q\), form a basis of \(Z(a,q)\), and
\[
 (E-a)v_{i,j}=v_{i,j-1},\qquad \dim Z(a,q)=2q.
 \tag{2.7}
\]
On each half-line every member is a function
\[
 u(x)=|x|^aP_\pm(\log|x|),\qquad \deg P_\pm<q.
 \tag{2.8}
\]
Point-supported solutions remain exactly the multiples of \(\delta_0^{(k-1)}\) at \(a=-k\); there are no longer chains consisting entirely of point-supported distributions.

**Proof.** Distributional parameter derivatives exist with the finite test bounds proved in U016 and U017. Applying a fixed differential operator commutes with them because it acts by a continuous map on tests. Differentiating \((E-b)A_i(b)=0\) \(j\) times and dividing by \(j!\) proves the first identity in (2.7).

In a zero linear combination of the proposed basis, apply \((E-a)^{q-1}\). The independence of \(v_{1,0},v_{2,0}\) kills the two top coefficients. Repeat with descending powers to kill every coefficient. For spanning, induct on \(q\). Expand \((E-a)u\) in the shorter chains, raise each chain index by one to obtain \(w\) with \((E-a)w=(E-a)u\), and use Theorem 2.1 on \(u-w\). This proves the basis and dimension.

For an explicit half-line interpretation, transfer a distribution on \(x>0\) by
\[
 w(\psi)=u\bigl(x^{-a-1}\psi(\log x)\bigr),
 \qquad \psi\in\mathcal D(\mathbb R).
 \tag{2.9}
\]
The test map and its inverse
\(\phi(x)\mapsto e^{(a+1)t}\phi(e^t)\)
preserve compact supports in the respective domains and bound all derivatives by the chain rule. Transposing the Euler operator shows that \((E-a)u\) transfers to \(w'\): indeed
\((-1-E-a)[x^{-a-1}\psi(\log x)]=-x^{-a-1}\psi'(\log x)\).
Thus \(w^{(q)}=0\). The zero-derivative fact, followed successively by subtraction of ordinary polynomial primitives, proves that \(w\) is a polynomial of degree below \(q\). Scalar substitution \(x=e^t\) in its pairing recovers (2.8). On the negative half-line use \(x=-e^t\); its absolute Jacobian is again \(e^t\), giving the other polynomial. Finally, (2.4) diagonalizes \((E-a)^q\) on the finite independent jet expansion. Only its zero eigenvalue can survive, regardless of \(q\). \(\square\)

With \(N=E-a\), the exact scaling formula on \(Z(a,q)\) is
\[
 \begin{aligned}
 D_tu&=t^a\sum_{\ell=0}^{q-1}
              \frac{(\log t)^\ell}{\ell!}N^\ell u,\\
 (D_tu)(\phi)&=t^{-1}u(\phi(\cdot/t)).
 \end{aligned}
 \tag{2.10}
\]
To prove it, differentiate \(D_tA_i(b)=t^bA_i(b)\) \(j\) times in the parameter, divide by \(j!\), and use \(N^\ell v_{i,j}=v_{i,j-\ell}\). It follows on every basis vector, hence on the space.

## What fails at the parameter zero

**Theorem 3.1 (maps between generalized spaces).** If \(a\ne0\), differentiation maps \(Z(a,q)\) isomorphically to \(Z(a-1,q)\). With \(N'=E-(a-1)\) on the target, its inverse is
\[
 \begin{aligned}
 \partial_x^{-1}&=x(aI+N')^{-1},\\
 (aI+N')^{-1}
    &=\sum_{j=0}^{q-1}\frac{(-1)^j}{a^{j+1}}(N')^j.
 \end{aligned}
 \tag{3.1}
\]
At zero the images instead are
\[
 \begin{aligned}
 EZ(0,q)&=Z(0,q-1),\\
 (E+1)Z(-1,q)&=Z(-1,q-1),\\
 \partial_xZ(0,q)
   &=\{v\in\mathcal D'(\mathbb R):xv\in Z(0,q-1)\},\\
 xZ(-1,q)
   &=\{u\in\mathcal D'(\mathbb R):u'\in Z(-1,q-1)\}.
 \end{aligned}
 \tag{3.2}
\]
Furthermore,
\[
 \partial_xZ(0,q)\subset Z(-1,q)
                     \subset\partial_xZ(0,q+1),
 \tag{3.3}
\]
with codimension one at each inclusion. The critical differentiation kernel is the constants, and the critical multiplication kernel is \(\mathbb C\delta_0\).

**Proof.** Multiplying the finite series in (3.1) by \(aI+N'\) gives \(I\), since \((N')^q=0\). The corresponding series also inverts \(aI+N\) on \(Z(a,q)\). The identities \(x\partial_x=aI+N\) and \(\partial_xx=aI+N'\) give injectivity and surjectivity. The intertwining in (1.4) places the displayed inverse in the correct space.

The two chains at zero show that applying \(E\) removes exactly their last levels and has image \(Z(0,q-1)\); at degree \(-1\) the same argument applies to \(E+1\). If \(v=u'\) for \(u\in Z(0,q)\), then \(xv=Eu\in Z(0,q-1)\). Conversely, if this last condition holds, Lemma 1.1 supplies a primitive \(u\), and \(E^qu=E^{q-1}(xv)=0\). This proves the third image formula.

If \(u=xv\) with \(v\in Z(-1,q)\), then \(u'=(E+1)v\in Z(-1,q-1)\). Conversely, divide a given \(u\) with that derivative property by \(x\), using Lemma 1.1. The resulting \(v\) satisfies \((E+1)v=u'\), hence \((E+1)^qv=0\). This proves the fourth image formula.

The first inclusion in (3.3) follows from (1.4). If \(v\in Z(-1,q)\), then \(xv\in Z(0,q)\), and the primitive argument puts \(v\) in \(\partial_xZ(0,q+1)\). The zero-derivative fact makes the kernel of differentiation on each \(Z(0,q)\) one-dimensional. Therefore the three spaces in (3.3) have dimensions \(2q-1,2q,2q+1\). To justify this dimension subtraction directly, extend a basis of the kernel to a basis of the finite-dimensional domain; the images of the added vectors span the image and are independent by subtraction of a kernel vector. The multiplication kernel follows from Lemma 1.1, and \(\delta_0\) belongs to every \(Z(-1,q)\). \(\square\)

**Polynomial facts used below.** Every nonconstant complex polynomial factors into linear factors, and coprime polynomial factors have a Bézout identity. Here are the needed proofs.

If a nonconstant polynomial \(p\) had no zero, \(1/p\) would be holomorphic everywhere by the scalar quotient rule. Writing \(p(z)=c_mz^m+\sum_{j<m}c_jz^j\) shows
\(|p(z)|\ge |c_m||z|^m/2\)
for sufficiently large \(|z|\): divide the finite lower-term sum by \(|z|^m\) and let \(|z|\) increase. On the remaining compact disk, continuity and the absence of zeros give a positive minimum. Thus \(1/p\) is bounded by one fixed constant \(M\) on the whole plane. U013, Corollary 2.2, gives \(|(1/p)'(z)|\le M/R\) on every centered circle of radius \(R\). Letting \(R\) tend to infinity makes this derivative zero. The fundamental theorem along line segments makes \(1/p\) constant, a contradiction. Hence \(p\) has a root \(a\). The finite identity \(z^j-a^j=(z-a)\sum_{l=0}^{j-1}z^{j-1-l}a^l\) divides \(p(z)-p(a)\) by \(z-a\). Repeating on the quotient proves factorization by induction on degree, including multiplicities.

Polynomial division is obtained by subtracting the leading monomial multiple of the divisor; each subtraction lowers the remainder degree and the process terminates. Repeated division, exchanging divisor and nonzero remainder, strictly lowers the latter's degree. The last nonzero remainder \(d\) divides both original polynomials by back-substitution through the divisions; every common divisor divides each remainder and hence \(d\). Back-substitution also expresses \(d\) as a polynomial combination of the originals. Iterating this procedure gives the same statement for any finite list. If the list has no common nonconstant divisor, rescale the final constant to one to obtain its Bézout identity. By factorization, having no common root implies precisely this condition.

**Corollary 3.2 (polynomials in the Euler operator).** For a nonzero complex polynomial \(P\) of degree \(m\),
\[
 \dim\ker P(E)=2m.
 \tag{3.4}
\]
If its distinct roots \(a_\nu\) have multiplicities \(q_\nu\), then
\[
 \ker P(E)=\bigoplus_\nu Z(a_\nu,q_\nu).
 \tag{3.5}
\]

**Proof.** Divide out the nonzero leading coefficient and put \(p_\nu(t)=(t-a_\nu)^{q_\nu}\), \(Q_\nu=P/p_\nu\). The \(Q_\nu\) have no common root: at any root \(a_\mu\), \(Q_\mu(a_\mu)\ne0\). For a single root \(Q_1=1\), which has the same property. The proved polynomial facts give \(\sum_\nu b_\nu Q_\nu=1\). Thus for \(P(E)u=0\),
\[
 u=\sum_\nu b_\nu(E)Q_\nu(E)u.
 \tag{3.6}
\]
The \(\nu\)-th term is killed by \(p_\nu(E)\). Conversely each such kernel is contained in \(\ker P(E)\). On \(\ker p_\mu(E)\), the operators \(b_\nu(E)Q_\nu(E)\) vanish for \(\nu\ne\mu\), because \(Q_\nu\) contains \(p_\mu\). Since their sum is the identity, the remaining operator is the identity there. Applying these operators to a zero sum proves directness. Theorem 2.2 gives dimension \(2\sum_\nu q_\nu=2m\). A nonzero constant \(P\) has zero kernel and \(m=0\). \(\square\)

## Scaling forces a sharp order bound

Order at most \(k\) means that on each fixed compact test support \(K\), \(|u(\phi)|\le C_K\|\phi\|_{C^k}\). Exact order is the smallest such nonnegative integer.

**Lemma 4.1 (a strict bound from disjoint annuli).** If \(u\in\mathcal D'(\mathbb R^n)\) has order at most \(k\) and its nonzero restriction off zero is homogeneous of degree \(a\), then
\[
 k+\operatorname{Re}a+n>0.
 \tag{4.1}
\]

**Proof.** Some annular test \(\psi\) has \(c=u(\psi)\ne0\); every compact subset of the punctured space fits inside an annulus. For \(0<\varepsilon\le1\), put \(\phi_\varepsilon(x)=\varepsilon^k\psi(x/\varepsilon)\). These tests have supports in one ball and uniformly bounded derivatives through order \(k\). The punctured scaling law gives
\[
 u(\phi_\varepsilon)=\varepsilon^{a+n+k}c.
 \tag{4.2}
\]
A negative real exponent contradicts the order estimate. If its real part is zero, choose a geometric sequence \(\varepsilon_j\downarrow0\) whose closed supporting annuli are pairwise disjoint. For example, if the original radii are \(r_0,R_0\), take successive ratios smaller than \(r_0/(2R_0)\). Multiply each test by a scalar of modulus one making its pairing equal to \(|c|\). Every finite sum is a smooth compact test vanishing near zero. At each point at most one summand or its derivatives is nonzero, so the sums have one uniform \(C^k\) bound. Their pairings are \(N|c|\), a contradiction. This excludes equality as well. \(\square\)

**Theorem 4.2 (exact order for generalized Euler solutions).** If \(0\ne u\in Z(a,q)\) is supported at zero, then \(a=-k\) for some \(k\ge1\) and its exact order is \(k-1\). Otherwise its exact order is the least nonnegative integer \(s\) such that
\[
 s+\operatorname{Re}a+1>0.
 \tag{4.3}
\]
In particular, increasing the logarithmic chain length does not increase this order.

**Proof.** First suppose \(a\) is nonexceptional. On a small disk about \(a\), arrange \(\operatorname{Re}b+s>-1\) and avoid all zeros of the following denominator. U016's meromorphic derivative identity gives
\[
 U_b(\phi)=
 \frac{(-1)^s}{(b+1)\cdots(b+s)}
       \int_0^\infty x^{b+s}\phi^{(s)}(x)\,dx.
 \tag{4.4}
\]
For \(s=0\) the denominator is the empty product one. The identity follows first by integration by parts where the endpoint terms vanish, and then by the meromorphic identity theorem already proved in U016. On any fixed compact test support, parameter derivatives of every finite order insert logarithmic powers and derivatives of the scalar denominator. They are bounded by \(C\|\phi\|_{C^s}\), because \(x^{\operatorname{Re}b+s}|\log x|^l\) is uniformly integrable at zero on a smaller disk; U016's gamma companion evaluates and bounds these integrals. Reflection has the same estimate. The basis of Theorem 2.2 therefore has order at most \(s\).

At \(a=-k\), (4.3) gives \(s=k\). Set \(b=-k+w\). The denominator in (4.4) has exactly one simple zero at \(w=0\), and its integral is
\[
 \int_0^\infty x^w\phi^{(k)}(x)\,dx.
 \tag{4.5}
\]
For \(\operatorname{Re}w>-1\) this is holomorphic with all local parameter derivatives bounded by a \(C^k\) test norm. Write the resulting meromorphic family as \(R/w+H(w)\), where \(R\) is its known delta-jet residue. On a fixed small circle \(|w|=r<1\), both (4.4) and \(R/w\) have uniform \(C^k\) bounds. The removable-pole statement from U016 makes \(H\) holomorphic inside. U013's scalar Cauchy coefficient formula, applied after each test pairing, bounds the \(j\)-th coefficient of \(H\) by \(C_r r^{-j}\|\phi\|_{C^k}\). Thus every coefficient is a distribution of order at most \(k\).

The same holds after reflection. In the U017 identity
\[
 B_\pm(b)=U_b+e^{\pm i\pi b}RU_b
 \tag{4.6}
\]
the poles cancel. Multiplying by the analytic phase adds only finite scalar multiples of Laurent coefficients and the residue to each Taylor coefficient, all with \(C^k\) bounds. Their parameter derivatives span the exceptional generalized space, so its order is at most \(k\).

For the lower bound, suppose \(s\ge1\) and \(u\) is nonzero off zero. Choose an annular \(\psi\) with \(u(\psi)\ne0\). From (2.10),
\[
 \begin{aligned}
 u\bigl(\varepsilon^{s-1}\psi(\cdot/\varepsilon)\bigr)
    &=\varepsilon^{a+s}p(\log\varepsilon),\\
 p(z)&=\sum_{\ell=0}^{q-1}
          \frac{z^\ell}{\ell!}(N^\ell u)(\psi).
 \end{aligned}
 \tag{4.7}
\]
The polynomial is nonzero because \(p(0)\ne0\), and minimality of \(s\) gives \(\operatorname{Re}a+s\le0\). If this real part is negative, the exponential growth in \(-\log\varepsilon\) dominates any nonzero polynomial and the pairing is unbounded. This follows, for example, from the exponential series lower bound \(e^{ct}\ge (ct)^M/M!\) with \(M\) larger than any specified polynomial degree, and the leading-term bound for \(p(-t)\). If the real part is zero and \(p\) is nonconstant, its modulus also tends to infinity by its leading term. Either case contradicts an order-\((s-1)\) estimate. If \(p\) is constant, phase-aligned disjoint annuli as in Lemma 4.1 give the contradiction instead. Therefore order \(s-1\) is impossible. When \(s=0\), the upper bound already gives exact order zero.

A nonzero point-supported solution is \(c\delta^{(j)}\) with \(j=k-1\), by Theorem 2.2. It has order at most \(j\). If \(j>0\), choose a compact smooth \(\eta\) with \(\eta^{(j)}(0)\ne0\), for instance a cutoff times \(x^j\). The tests \(\varepsilon^{j-1}\eta(x/\varepsilon)\) have uniformly bounded \(C^{j-1}\) norm but jet values of size \(\varepsilon^{-1}|\eta^{(j)}(0)|\). This excludes smaller order. For \(j=0\) the nonzero delta has exact order zero. \(\square\)

Thus \(x_+^{-3/2}\) has order one and \(x_+^{-2+i}\) has order two, as do their logarithmic parameter derivatives when nonzero off zero. At degree \(-2\), \(\delta_0'\) has order one whereas \(S_2\) has order two.

## Tensor singularities can share one derivative

The tensor notation used in this section has a direct construction. U016 gives
\(\operatorname{pv}(1/x)(f)=\int_0^\infty[f(x)-f(-x)]\,dx/x\).
For a planar test supported in \([-R,R]^2\), define
\[
 \begin{aligned}
 U(\phi)&=\int_0^R\int_0^R
 \frac{\phi(x,y)-\phi(-x,y)-\phi(x,-y)+\phi(-x,-y)}{xy}\,dy\,dx,\\
 V(\phi)&=\operatorname{pv}(1/x)
                  \bigl(x\mapsto\partial_y\phi(x,0)\bigr).
 \end{aligned}
 \tag{T1}
\]
The double difference equals
\(\int_{-x}^x\int_{-y}^y\partial_x\partial_y\phi(s,t)\,dt\,ds\);
its absolute value is at most \(4xy\|\phi\|_{C^2}\). Thus the first integral is absolutely convergent after cancellation, independent of increasing \(R\), and bounded by \(4R^2\|\phi\|_{C^2}\). Applying the one-dimensional cancellation twice and Fubini gives precisely the iterated principal-value pairing, in either order. It also proves that removing strips \(|x|\le\varepsilon\), \(|y|\le\eta\) from the ordinary integral converges to \(U(\phi)\) as both cutoffs tend to zero, independently.

The trace in the second line is a compact smooth line test, and its first derivative is bounded by \(\|\phi\|_{C^2}\). Hence \(V\) also has order at most two. These explicit formulas define
\[
 \begin{aligned}
 U&=\operatorname{pv}(1/x)\otimes\operatorname{pv}(1/y),\\
 V&=-\operatorname{pv}(1/x)\otimes\delta_0'(y).
 \end{aligned}
 \tag{5.1}
\]
They require no general tensor-product existence or uniqueness theorem. For tensor tests their pairings are the products of the individual factor pairings, by the same formulas.

**Theorem 5.1 (orders of two planar tensors).** The distribution \(U\) is homogeneous of degree \(-2\) and has exact order one. The distribution \(V\) is homogeneous of degree \(-3\) and has exact order two.

**Proof.** Substitution \(x=ts,y=tr\) in (T1), together with the density \(t^{-2}\) in \(D_t\), gives \(D_tU=t^{-2}U\). For \(V\), the derivative in its traced test adds \(t^{-1}\) and the one-dimensional principal-value substitution has degree zero as a pairing on dilated tests, so \(D_tV=t^{-3}V\). Both are nonzero off the origin. Near \((1,1)\), \(U\) is the nonzero ordinary function \(1/(xy)\); near \((1,0)\), tests \(f(x)h(y)\) with \(h'(0)\ne0\) make \(V\ne0\). Lemma 4.1 forces order at least one for \(U\) and at least two for \(V\). The bound above already proves the latter exact order.

To improve the bound for \(U\), write \(\omega=(\cos\theta,\sin\theta)\). Its angular distribution is
\[
 T(g)=\operatorname{pv}\int_0^{2\pi}
                  \frac{g(\theta)}{\cos\theta\sin\theta}\,d\theta,
 \tag{5.2}
\]
with symmetric principal values at \(0,\pi/2,\pi,3\pi/2\), interpreting the interval periodically at zero. We justify this formula and its estimates. Choose a fixed small radius \(d<\pi/4\) around each singular angle. There the denominator is \(\pm\sin s\cos s\), an odd function with absolute value at least \(c|s|\); the latter bound follows by continuity of \(\sin s/s\) at zero and by \(\cos s\ne0\). The constant term \(g(\theta_0)\) cancels on every symmetric punctured interval. The remaining quotient is bounded by \(C\|g'\|_\infty\), by the fundamental theorem. On the complementary arcs the denominator is bounded away from zero. Thus the principal value exists and
\[
 |T(g)|\le C\|g\|_{C^1(S^1)},\qquad T(1)=0.
 \tag{5.3}
\]
For the last equality, reflection \(\theta\mapsto-\theta\) preserves every symmetric exclusion and changes the denominator's sign.

Now take \(\phi\) supported in \(r_0\le|x|\le R_0\), \(r_0>0\). For equal small strip widths \(\varepsilon\), the polar formula from U018 A4 turns the cut-off ordinary pairing into the radial integral with weight \(dr/r\). At each axis angle the strip excludes precisely the symmetric angular interval of radius \(\arcsin(\varepsilon/r)\); the four intervals are disjoint once \(\varepsilon/r_0\) is small. The inverse sine here exists on a fixed small interval because cosine is positive there; its convergence to zero follows from continuity and strict monotonicity of sine. Subtracting \(\phi(r\omega(\theta_0))\) on each symmetric arc gives the preceding integrable bound uniformly for \(r_0\le r\le R_0\). Dominated convergence therefore gives
\[
 U(\phi)=\int_0^\infty T(\phi(r\,\cdot))\,\frac{dr}{r}
 \quad\hbox{for these annular tests}.
\]
The strip limit was already identified with \(U\) by the double-cancellation formula (T1). This proves (5.2) as the angular distribution, with no interchange of divergent integrals.

Because \(T(1)=0\), U018's Laurent-constant radial extension takes the convergent form
\[
 F(\phi)=\int_0^\infty
              T\bigl(\omega\mapsto\phi(r\omega)\bigr)\,\frac{dr}{r}.
 \tag{5.4}
\]
For \(0<r\le1\), the segment fundamental theorem and the circle chain rule give
\[
 \|\phi(r\,\cdot)-\phi(0)\|_{C^1(S^1)}
       \le Cr\|\phi\|_{C^1}.
 \tag{5.5}
\]
Indeed the zeroth difference is bounded by \(r\sup|\nabla\phi|\), and the angular derivative is \(r\nabla\phi(r\omega)\cdot\omega'\), with \(|\omega'|=1\). Combining (5.3) and (5.5) makes the radial integral near zero bounded by \(C\|\phi\|_{C^1}\). On \(1\le r\le R\), where \(R\ge1\) bounds the support, the same test norm bounds the angular pairing with a constant depending on \(R\); beyond \(R\) it vanishes. Thus \(F\) has order at most one.

U018, Theorem 4.1, makes \(F\) homogeneous of degree \(-2\). It has the same punctured restriction as \(U\), so their difference is a multiple of \(\delta_{(0,0)}\), by the independent-jet Euler calculation. Both are odd under reflection of either coordinate: this follows from (T1) for \(U\) and from the symmetric angular prescription and radial integral for \(F\). A delta is even. The multiple is therefore zero, proving \(U=F\) and exact order one. \(\square\)

For a numerical sign check, let \(p(s)=(1-s^2)^4\) on \(|s|<1\), zero elsewhere, and set \(\phi(x,y)=xy\,p(x)p(y)\). The vanishing of the first four powers at each endpoint makes \(p\), and hence \(\phi\), compact \(C^3\). U008 proves the unique extension of a finite-order distribution to compact \(C^k\) tests. The cancellation formulas (T1) have the same continuous extensions, by smooth approximation with a common support. They give
\[
 U(\phi)=\left(\frac{256}{315}\right)^2,
 \qquad V(\phi)=\frac{256}{315},
 \tag{5.6}
\]
since
\[
 \int_{-1}^1p(s)\,ds
   =2\sum_{j=0}^4\frac{(-1)^j\binom4j}{2j+1}
   =\frac{256}{315},
 \tag{5.7}
\]
and \(\partial_y\phi(x,0)=xp(x)\). The positive second value verifies the sign of \(V\).

## Exercises

**Exercise 1 (basic: two critical images).** Let \(u=3H_+-2H_-\) and \(v=\operatorname{pv}(1/x)+4\delta_0\). Compute \(u'\), \(xv\), and the kernels of \(\partial_x:Z(0,1)\to Z(-1,1)\) and \(x:Z(-1,1)\to Z(0,1)\). Can \(v\) be the derivative of a member of \(Z(0,1)\)?

**Exercise 2 (intermediate: an inverse with three logarithmic levels).** On \(Z(1,3)\), put \(N'=E-1\). Find a polynomial representing \((2I+N')^{-1}\). Give the inverse of differentiation from \(Z(2,3)\) to \(Z(1,3)\), and verify both compositions.

**Exercise 3 (intermediate: a polynomial Euler equation).** Find the dimension, direct summands and point-supported solutions of
\[
 \ker\bigl((E+2)^2(E-(1+i))E\bigr).
 \tag{6.1}
\]
Explain why the repeated root does not produce two independent point-supported solutions.

**Exercise 4 (intermediate: a chain ending at a point mass).** Let \(F_1\) be the Laurent constant of \(U_b\) at \(b=-1\). Prove \(F_1\in Z(-1,2)\setminus Z(-1,1)\), and find its exact order and the exact order of \((E+1)F_1\).

**Exercise 5 (advanced: oscillation at the order threshold).** For real \(\beta\ne0\), let \(a=-2+i\beta\) and \(w=\left.\partial_bU_b\right|_{b=a}\). Find its chain and exact order. Explain both mechanisms that exclude order one in the scaled-test argument, even when the oscillatory factor has modulus one.

**Exercise 6 (advanced: singularities supported on a plane).** In \(\mathbb R^3\), set
\[
 T=\bigl(\operatorname{pv}(1/x)\otimes\operatorname{pv}(1/y)\bigr)
                \otimes\delta_0(z),\qquad W=-\partial_zT.
 \tag{6.2}
\]
Define their pairings, compute both homogeneity degrees and exact orders, and prove the lower bounds without adding the separate principal-value orders.

## Complete solutions

**Solution 1.** The endpoint derivative identities give \(u'=3\delta_0+2\delta_0=5\delta_0\). Coordinate multiplication gives \(xv=1\). The differentiation kernel is \(\mathbb C(H_++H_-)=\mathbb C1\), and its image is \(\mathbb C\delta_0\). The multiplication kernel is \(\mathbb C\delta_0\). Since \(v\) has a nonzero principal-value component, it lies outside that derivative image although it belongs to \(Z(-1,1)\).

**Solution 2.** Nilpotence \((N')^3=0\) gives
\[
 Q(N')=\tfrac12I-\tfrac14N'+\tfrac18(N')^2.
 \tag{7.1}
\]
Indeed \((2I+N')Q(N')=I+(N')^3/8=I\). Thus \(\partial_x^{-1}v=xQ(N')v\), and differentiating gives \((E+1)Q(N')v=v\). For the other composition put \(N=E-2\) on \(Z(2,3)\). Formula (1.4) gives \(N'\partial_x=\partial_xN\), hence
\[
 xQ(N')\partial_xu
    =x\partial_xQ(N)u=(2I+N)Q(N)u=u.
 \tag{7.2}
\]
This verifies both compositions on their stated domains.

**Solution 3.** The distinct roots are \(-2,1+i,0\), with multiplicities \(2,1,1\). The direct decomposition is
\[
 Z(-2,2)\oplus Z(1+i,1)\oplus Z(0,1),
 \tag{7.3}
\]
with dimensions \(4,2,2\), totaling eight. On point jets the eigenvalues are \(-(j+1)\); only \(j=1\) matches a root. Thus the point-supported solutions are exactly \(c\delta_0'\). The diagonal action on jets supplies no further generalized eigenvector when the root is repeated.

**Solution 4.** U016's constant-Laurent Euler identity gives \((E+1)F_1=\delta_0\), and \((E+1)\delta_0=0\). The first is nonzero, proving the asserted chain length. The positive-half-line restriction \(1/x\) is nonzero, so Theorem 4.2 gives exact order one. The image \(\delta_0\) has exact order zero.

**Solution 5.** Parameter differentiation gives \((E-a)w=U_a\) and \((E-a)U_a=0\). The positive-half-line functions \(x^a\log x\) and \(x^a\) are nonzero, so the chain has length two. The least integer with \(s-2+1>0\) is \(s=2\), its exact order. On annular tests, (4.7) becomes
\[
 w\bigl(\varepsilon\psi(\cdot/\varepsilon)\bigr)
   =\varepsilon^{i\beta}
       \bigl(w(\psi)+(\log\varepsilon)U_a(\psi)\bigr).
 \tag{7.4}
\]
Choose \(\psi\) with \(U_a(\psi)\ne0\), which is possible on its nonzero positive restriction. The logarithm makes the modulus unbounded despite \(|\varepsilon^{i\beta}|=1\). If instead a chosen test has vanishing logarithmic coefficient and nonzero constant pairing, use phase-aligned disjoint annuli. Their finite sums have one \(C^1\) bound and unbounded pairings. Either mechanism excludes order one.

**Solution 6.** Use the planar \(U\) of Theorem 5.1 and define
\[
 T(\phi)=U\bigl(\phi(\cdot,\cdot,0)\bigr),\qquad
 W(\phi)=U\bigl(\partial_z\phi(\cdot,\cdot,0)\bigr).
 \tag{7.5}
\]
These are distributions because traces preserve compact support and bound every test derivative. The second sign is positive because \(W=-\partial_zT\). The first trace has the \(C^1\) bound already proved for \(U\), so \(T\) has order at most one; the second has a \(C^2\) bound, so \(W\) has order at most two.

In the three-dimensional dilation formula the density is \(t^{-3}\), whereas the planar trace pairing with \(U\) under dilation contributes no further factor: planar degree \(-2\) exactly cancels its dimension. Thus \(T\) has degree \(-3\); the extra trace derivative makes \(W\) have degree \(-4\). Both are nonzero near \((1,1,0)\), as tensor tests with a nonzero trace, respectively a nonzero \(z\)-derivative at zero, show. Lemma 4.1 then requires \(k-3+3>0\) for \(T\) and \(k-4+3>0\) for \(W\). These give exact orders one and two without estimating the two principal values separately.

## Programme proof locations and freely accessible sources

- [Order, positivity and distributional limits](order-positivity-and-limits.md), Section 1 and the finite-\(C^k\) extension: distribution estimates and smooth approximation on a common support.
- [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2: the coefficient and derivative bounds used for polynomial factorization and Laurent coefficient order estimates.
- [Finite parts of singular powers](finite-parts-of-singular-powers.md) and [Complex powers at a boundary](complex-powers-at-a-boundary.md): the complete scalar meromorphic and entire families, exact residues, reflection signs and parameter estimates.
- [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Lemma 1.1 and Theorems 1.2, 2.1 and 4.1; [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A1–A5: Euler/scaling equivalence, point jets, exceptional moments, radial extension and polar integration.
- [Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Proposition 3.2, Section 5.1 and Theorem 7.1: freely accessible proofs for the zero-derivative theorem, homogeneous distributions and iterated distributional pairing. The arguments above prove all required special tensor estimates directly and supply the generalized-chain and sharp-order conclusions in full.

The original exposition here is CC0. Linked earlier foundation selections retain their stated CC0 1.0 licences.

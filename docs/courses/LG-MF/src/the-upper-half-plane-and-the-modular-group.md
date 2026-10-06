# The upper half-plane and the modular group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Changing a basis of a lattice in the complex plane changes its shape parameter by a fractional linear transformation. This observation will eventually connect modular forms with elliptic curves. First we need a precise answer to a geometric question: how can we choose one shape from each orbit, and what happens at shapes with extra symmetry?

We use elementary differentiation and integration and the topology of the plane. The freely accessible background texts are [Wiese 2018] and [Voight open book]. The reduction and boundary arguments below are derived directly from integer rows and the imaginary-part identity. Their analytic and topological prerequisites are listed at the end; a background citation does not certify an earlier programme proof.

**Lemma 0.1 (the integer arithmetic used below).** For integers \(a,c\), not both zero, the Euclidean algorithm terminates and produces integers \(u,v\) with \(ua+vc=\gcd(a,c)\).

*Proof.* Change signs to start with nonnegative entries, exchanging them if needed; if the second entry is zero, the assertion is immediate. For positive \(b\), integer division gives \(a=qb+r\), \(0\le r<b\). A common divisor of \(a,b\) is exactly a common divisor of \(b,r\), since subtraction of \(qb\) preserves divisibility. Repeat, replacing the pair by \((b,r)\). Its positive second entry strictly decreases until a zero remainder occurs. The last positive entry is therefore the gcd. At every stage each entry is an integer linear combination of the starting pair, because replacement uses subtraction and exchange. Back-substitution supplies \(u,v\), and undoing the initial signs gives the assertion for arbitrary integers. In particular a primitive row \((c,d)\) can be completed to determinant one: from \(uc+vd=1\), take \(a=v,b=-u\). \(\square\)

Write
\[
\mathfrak H=\{z=x+iy:y>0\},\qquad
\gamma z=\frac{az+b}{cz+d},\qquad
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
A matrix of positive determinant acts on \(\mathfrak H\). Multiplying the matrix by a nonzero real scalar does not change the transformation. We distinguish \(\mathrm{SL}_2(\mathbb R)\) from its quotient \(\mathrm{PSL}_2(\mathbb R)=\mathrm{SL}_2(\mathbb R)/\{I,-I\}\).

## 1. Geometry preserved by a change of coordinates

**Proposition 1.1.** If \(\det\gamma>0\), then
\[
\operatorname{Im}(\gamma z)=\frac{\det(\gamma)y}{|cz+d|^2},
\qquad (\gamma z)'=\frac{\det(\gamma)}{(cz+d)^2}.
\]
Consequently the length element \(|dz|/y\), the metric \((dx^2+dy^2)/y^2\), and the area measure \(d\mu=dx\,dy/y^2\) are invariant.

*Proof.* The denominator does not vanish in \(\mathfrak H\). Subtract the conjugate of the fraction from the fraction itself. Its numerator is
\[
(az+b)(c\bar z+d)-(a\bar z+b)(cz+d)
=(ad-bc)(z-\bar z).
\]
Division by \(2i|cz+d|^2\) proves the first identity. The quotient rule proves the second. The derivative multiplies lengths by \(\det(\gamma)/|cz+d|^2\), exactly the factor multiplying \(y\). Its real Jacobian is the square of that factor. Dividing the transformed Euclidean area by the transformed height squared cancels it. \(\square\)

**Proposition 1.2 (coordinates on the group).** The action of \(\mathrm{SL}_2(\mathbb R)\) on \(\mathfrak H\) is transitive, the stabilizer of \(i\) is \(\mathrm{SO}(2)\), and every \(g\) has a unique expression
\[
g=n(x)a(y)k(\theta),\quad
n(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix},\quad
a(y)=\begin{pmatrix}\sqrt y&0\\0&1/\sqrt y\end{pmatrix},\quad
k(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\]
where \(y>0\) and \(\theta\) is taken modulo \(2\pi\).

*Proof.* The product \(n(x)a(y)\) sends \(i\) to \(x+iy\), proving transitivity. The equation \((ai+b)/(ci+d)=i\) gives \(a=d\), \(b=-c\). The determinant equation becomes \(a^2+c^2=1\), precisely the displayed rotations. For any \(g\), set \(x+iy=gi\). Then \((n(x)a(y))^{-1}g\) fixes \(i\), so it is a unique rotation. The image of \(i\) also proves uniqueness of \(x,y\). This is the Iwasawa decomposition. In the projective group the rotation angle is instead taken modulo \(\pi\). \(\square\)

The projective action is faithful. Indeed, a matrix fixing every \(z\) satisfies \(cz^2+(d-a)z-b=0\) identically, so \(c=b=0\), \(d=a\), and determinant one leaves \(I,-I\).

**Proposition 1.3 (fixed points).** For \(g\in\mathrm{SL}_2(\mathbb R)\setminus\{I,-I\}\), the three possibilities are:

- \(|\operatorname{tr}g|<2\): one fixed point in \(\mathfrak H\), and its conjugate in the lower half-plane;
- \(|\operatorname{tr}g|=2\): exactly one fixed point on \(\mathbb P^1(\mathbb R)\);
- \(|\operatorname{tr}g|>2\): exactly two fixed points on \(\mathbb P^1(\mathbb R)\).

These are called elliptic, parabolic and hyperbolic, respectively.

*Proof.* Fixed points are the eigenlines of \(g\), or equivalently the roots of
\[
cz^2+(d-a)z-b=0.
\]
Its discriminant is \((a+d)^2-4\). Negative discriminant gives two nonreal conjugate roots. Zero discriminant gives a repeated real eigenline; a non-scalar matrix with repeated eigenvalue has only one eigenline. Positive discriminant gives two distinct real eigenlines. Describing them as lines includes \(\infty\) when \(c=0\). The positive-imaginary-part root is unique in the first case. \(\square\)

For example,
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\]
has fixed points \(r_\pm=(1\pm\sqrt5)/2\). Its invariant geodesic is the semicircle with those endpoints, center \(1/2\) and radius \(\sqrt5/2\). To see the action explicitly, put \(w=(z-r_-)/(r_+-z)\). This real fractional linear transformation maps that semicircle to the positive imaginary axis. The eigenvalues of \(A\) are \(\lambda_\pm=(3\pm\sqrt5)/2\), with \(\lambda_-\lambda_+=1\), and direct substitution gives \(w(Az)=\lambda_+^2w(z)\). The vertical segment minimizes hyperbolic length between its endpoints: every piecewise differentiable path satisfies
\[
\int\frac{\sqrt{(dx)^2+(dy)^2}}y
\ge\int\frac{|dy|}y
\ge\left|\log\frac{y_2}{y_1}\right|,
\]
and the vertical segment attains equality. Proposition 1.1 carries this minimizing property to the semicircle. Hence \(A\) moves toward \(r_+\) by distance \(2\log\lambda_+\), with no general geodesic classification required.

## 2. Reducing a shape without an infinite search

Set
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\mathcal F=\{z\in\mathfrak H:|\operatorname{Re}z|\le\tfrac12,\ |z|\ge1\}.
\]
The transformations are \(Sz=-1/z\) and \(Tz=z+1\). Matrix multiplication gives \(S^2=(ST)^3=-I\).

**Lemma 2.1.** For each \(z\in\mathfrak H\), its modular orbit contains a point of maximal height.

*Proof.* Every possible bottom row \((c,d)\) is a primitive integer pair, and every such pair occurs: Bezout's identity supplies \(a,b\) with \(ad-bc=1\). A point of height at least \(y=\operatorname{Im}z\) must satisfy
\[
|cz+d|^2=c^2y^2+(cx+d)^2\le1.
\]
This bounds \(|c|\le1/y\) and, for each \(c\), bounds \(d\) in a finite interval. Only finitely many such pairs exist. The pair \((0,1)\) is among them, so the set is nonempty. Maximize \(y/|cz+d|^2\) on this finite set; all remaining pairs give smaller height than \(y\). \(\square\)

**Theorem 2.2.** Every orbit of \(\mathrm{SL}_2(\mathbb Z)\) meets \(\mathcal F\). The following algorithm terminates: translate into \([-1/2,1/2]\); if the result has modulus less than one, apply \(S\), and repeat.

*Proof.* Translate a maximal-height point into the strip. If its modulus were less than one, applying \(S\) would increase its height, contrary to maximality. It lies in \(\mathcal F\).

For the algorithm, each inversion that is actually performed strictly increases height, and translations preserve height. Every intermediate height at least the initial height belongs to the finite set of heights in Lemma 2.1. Thus only finitely many inversions are possible. Each translation is one integer shift, so the process terminates. This proof gives termination even when one has not first found a maximizing pair. \(\square\)

Here is an exact reduction rather than a rounded calculation. Starting with \(z=(5+i)/50\), inversion gives
\[
Sz=\frac{-125+25i}{13},\qquad
T^{10}Sz=\frac{5+25i}{13}.
\]
The final real part is \(5/13\), and its squared modulus is \(650/169>1\); it lies in \(\mathcal F\). The reducing word is \(T^{10}S\).

## 3. Which representatives are the same?

**Lemma 3.1.** If \(z\in\mathcal F\) and \((c,d)\) is a primitive integer pair, then \(|cz+d|\ge1\). Equality is possible only as follows:

- \(c=0,d=\pm1\);
- up to simultaneous sign, \((c,d)=(1,0)\), with \(|z|=1\);
- up to simultaneous sign, \((c,d)=(1,1)\), with \(z=\rho=(-1+i\sqrt3)/2\);
- up to simultaneous sign, \((c,d)=(1,-1)\), with \(z=\rho+1\).

*Proof.* We have \(y\ge\sqrt3/2\). If \(|c|\ge2\), then \(|cz+d|\ge|c|y\ge\sqrt3>1\). If \(c=0\), primitivity gives \(|d|=1\). Otherwise change the simultaneous sign to make \(c=1\). For \(d=0\), the assertion is exactly \(|z|\ge1\). For \(|d|\ge2\), \(|x+d|\ge3/2\), so equality is impossible. For \(d=1\),
\[
|z+1|^2=|z|^2+2x+1\ge1,
\]
and equality forces \(|z|=1,x=-1/2\). For \(d=-1\), the same argument gives the right corner. \(\square\)

**Theorem 3.2 (the closed fundamental domain).** Two points of \(\mathcal F\) in the same modular orbit have equal height and can be identified by compositions of these side pairings:
\[
-\tfrac12+iy\longleftrightarrow\tfrac12+iy\quad(T),
\qquad z\longleftrightarrow-1/z\quad(S,\ |z|=1).
\]
An interior point has exactly one representative in \(\mathcal F\) and trivial stabilizer in \(\mathrm{PSL}_2(\mathbb Z)\).

*Proof.* Suppose \(w=\gamma z\) and \(z,w\in\mathcal F\). Lemma 3.1 gives \(\operatorname{Im}w\le\operatorname{Im}z\); applying it to \(\gamma^{-1}\) gives the reverse inequality. Thus \(|cz+d|=1\).

If \(c=0\), then projectively \(\gamma=T^a\); a nonzero shift keeping both points in the strip must be \(a=\pm1\) on its vertical sides. If \(c=1\), determinant one gives
\[
\gamma=\begin{pmatrix}a&ad-1\\1&d\end{pmatrix}=T^aST^d.
\]
For \(d=0\), inversion pairs the circular side, followed, only at its endpoints, by an allowed vertical pairing. For \(d=1\), \(z\) is the left corner: first \(T\) moves it to the right corner and then \(S\) back to the left corner; a final allowed translation moves between the corners. The case \(d=-1\) is the reverse. These exhaust Lemma 3.1. For interior points only \(c=0,a=0\) remains, so \(\gamma\) is projectively the identity. \(\square\)

The qualification about compositions matters at a corner: the same representative has nontrivial stabilizers such as \(ST\). To obtain a set with exactly one representative per orbit, retain the left vertical side, remove the right vertical side, and on the circular arc retain the half with nonpositive real part. The point \(i\) and the corner \(\rho\) remain.

**Proposition 3.3.** The stabilizers in \(\mathrm{PSL}_2(\mathbb Z)\) are trivial except for the orbits of \(i\) and \(\rho\). At these points they are cyclic of orders two and three, respectively:
\[
\operatorname{Stab}(i)=\langle S\rangle,\qquad
\operatorname{Stab}(\rho)=\langle ST\rangle,
\qquad \operatorname{Stab}(\rho+1)=\langle TS\rangle.
\]
Their orders in \(\mathrm{SL}_2(\mathbb Z)\) are four, six and six.

*Proof.* An element fixing a representative is among the equality cases in Theorem 3.2. A nonzero translation fixes no point of \(\mathfrak H\). On the arc away from its endpoints, an element can only be \(S\), and \(Sz=z\) gives \(z=i\). At \(\rho\), solving the fixed-point equation directly gives
\[
a=d-c,\quad b=-c,\quad d^2-cd+c^2=1.
\]
The integer solutions \((c,d)\) are \((0,\pm1),(\pm1,0),(1,1),(-1,-1)\): completing the square bounds \(|c|\le1\) and then checks these possibilities. The six matrices are exactly the powers of \(ST\). Conjugation by \(T\) gives the right-corner stabilizer, generated projectively by \(TS\). Reduction conjugates any other stabilizer to one of these. \(\square\)

For a concrete orbit check, an image of \(i\) has height \(1/(c^2+d^2)\). Height at least \(1/2\) forces \(c^2+d^2\le2\). In the closed strip the only resulting points are
\[
i,\qquad(-1+i)/2,\qquad(1+i)/2.
\]
All occur, using bottom rows \((0,1),(1,1),(1,-1)\). An image of \(\rho\) has height \((\sqrt3/2)/(c^2-cd+d^2)\). A height of at least \(1/2\) forces the positive integer denominator to be one. Hence in the closed strip the only points are \(\rho,\rho+1\). The matrix \(ST\) has trace one, fixes \(\rho\), and has order six in the special linear group. The same assertions hold for \(TS\) and \(\rho+1\), with order three in the projective group.

## 4. Generators, relations and finite-order elements

**Proposition 4.1.** The matrices \(S,T\) generate \(\mathrm{SL}_2(\mathbb Z)\).

*Proof.* Apply row operations to the first column \((a,c)^t\) of an integral determinant-one matrix. Left multiplication by \(T^n\) replaces \(a\) by \(a+nc\); left multiplication by \(S\) exchanges the entries up to sign. When \(c\ne0\), choose a remainder \(r=a+nc\) with \(0\le r<|c|\), then exchange. The new lower entry has strictly smaller absolute value. The Euclidean algorithm terminates with lower entry zero. Since \(\gcd(a,c)=1\), the remaining matrix is \(\pm T^m\). Finally \(-I=S^2\). Undoing the operations proves the assertion. \(\square\)

**Theorem 4.2.** With \(s,u\) denoting the projective classes of \(S,ST\),
\[
\mathrm{PSL}_2(\mathbb Z)=\langle s,u\mid s^2=u^3=1\rangle
\cong C_2*C_3.
\]

*Proof.* Generation gives a surjection from the displayed free product. We show that a nonempty reduced word cannot act identically. On the irrational real numbers let \(A\) be the positive ones and \(B\) the negative ones. They are disjoint. Directly,
\[
s(B)=A,\qquad u(A)\subset B,\qquad u^2(A)\subset B,
\]
because \(s(x)=-1/x\), \(u(x)=-1/(x+1)\), and \(u^2(x)=-(x+1)/x\).

A reduced alternating word beginning and ending with \(s\) maps \(B\) into \(A\); one beginning and ending with a nonidentity power of \(u\) maps \(A\) into \(B\). Both are nonidentity. This includes the one-letter words. If the first and last letters belong to different factors, invert the word if necessary so that it begins with \(s\) and ends with \(u^e\), \(e=1\) or \(2\). Choose \(j\in\{1,2\}\) with \(j\ne e\). Its conjugate \(u^jwu^{-j}\) is reduced and begins and ends in the \(u\)-factor, since its last letter is \(u^{e-j}\ne1\). It is therefore nonidentity, as is \(w\). This proves injectivity. \(\square\)

**Corollary 4.3.** Every nonidentity finite-order element of \(\mathrm{PSL}_2(\mathbb Z)\) is conjugate to \(s,u\), or \(u^2\).

*Proof.* A finite-order nonidentity real projective transformation is elliptic. To verify this without a classification assumption, lift it to \(g\in\mathrm{SL}_2(\mathbb R)\). A hyperbolic matrix has eigenvalues of unequal absolute value and cannot have a scalar power. A nonscalar parabolic matrix has a nonzero Jordan term in every positive power and also cannot have a scalar power. Proposition 1.3 therefore supplies a fixed point in \(\mathfrak H\). Reduce this point into \(\mathcal F\). Proposition 3.3 then places the conjugate in its order-two or order-three stabilizer, whose nonidentity elements are exactly those listed. \(\square\)

## 5. The area that fixes later normalizations

**Proposition 5.1.** The hyperbolic area of the modular quotient is \(\pi/3\).

*Proof.* The boundary has area zero, and the lower boundary at \(x\) is \(\sqrt{1-x^2}\). Thus
\[
\mu(\mathcal F)=\int_{-1/2}^{1/2}\int_{\sqrt{1-x^2}}^\infty\frac{dy\,dx}{y^2}
=\int_{-1/2}^{1/2}\frac{dx}{\sqrt{1-x^2}}
=2\arcsin(1/2)=\frac\pi3.
\]
\(\square\)

The two circular endpoints have angles \(\pi/3\), and the vertical sides meet at the ideal vertex \(\infty\), whose angle is zero. The same special angle calculation can be verified without a general area theorem: substitute \(x=\cos\theta\) in the displayed integral, with \(\theta\) running from \(2\pi/3\) down to \(\pi/3\). It gives \(2\pi/3-\pi/3=\pi/3\). The conformal metric preserves the endpoint angles, so this also equals \(\pi-\pi/3-\pi/3\) for this domain.

## 6. Exercises

1. **Easy.** Replace \(g\) in Proposition 1.1 by a positive-determinant matrix of determinant \(7\). Derive the imaginary-part and Jacobian formulas, then verify invariance of \(d\mu\).
2. **Easy.** Integrate over the portion of \(\mathcal F\) below height \(Y\ge1\), and recover its total area by taking a limit.
3. **Medium.** Determine every special linear integral matrix fixing \(\rho\), including its sign. Explain why counting six matrices gives an elliptic point of order three.
4. **Medium.** Prove that a finite-order nonidentity projective modular transformation is conjugate to \(s,u\), or \(u^2\). Deduce that its possible orders are two and three.
5. **Hard.** Using the positive and negative irrational half-lines, prove that the surjection \(C_2*C_3\to\mathrm{PSL}_2(\mathbb Z)\) is injective. Include reduced words whose end letters belong to different factors.

## 7. Solutions

**1.** Subtraction of conjugates gives \(\operatorname{Im}(gz)=7y/|cz+d|^2\). The complex derivative is \(7/(cz+d)^2\), so the real Jacobian is \(49/|cz+d|^4\). Therefore
\[
\frac{dx'\,dy'}{(y')^2}
=\frac{49|cz+d|^{-4}dx\,dy}{49y^2|cz+d|^{-4}}
=\frac{dx\,dy}{y^2}.
\]
This also shows why replacing a matrix by a scalar multiple leaves the formulas consistent: determinant and denominator square both acquire the same factor.

**2.** Since \(\sqrt{1-x^2}\le1\le Y\), integration up to \(Y\) gives
\[
\int_{-1/2}^{1/2}\left(\frac1{\sqrt{1-x^2}}-\frac1Y\right)dx
=\frac\pi3-\frac1Y.
\]
The omitted vertical tail has area \(1/Y\). Their sum is \(\pi/3\), and the truncated area tends to it.

**3.** Use \(\rho^2+\rho+1=0\) in \(c\rho^2+(d-a)\rho-b=0\). The real basis \(1,\rho\) gives \(b=-c\), \(a=d-c\). Determinant one gives \((d-c/2)^2+3c^2/4=1\), so \(|c|\le1\). For \(c=0\), \(d=\pm1\); for \(c=1\), \(d=0,1\); for \(c=-1\), \(d=0,-1\). The matrices are \(I,ST,(ST)^2,-I,-ST,-(ST)^2\). Projectivization identifies each matrix with its negative, leaving three transformations.

**4.** A finite-order projective element has a lift whose power is \(\pm I\). A real matrix with trace of absolute value greater than two has real eigenvalues of unequal absolute value; no power is scalar. At trace of absolute value two, a nonscalar Jordan block retains a nonzero off-diagonal entry in every power. Thus the lift is elliptic and fixes a point of \(\mathfrak H\). Conjugate that point into \(\mathcal F\). Its stabilizer, computed in Proposition 3.3, is trivial, \(\langle s\rangle\), or \(\langle u\rangle\). Nonidentity excludes the first possibility and yields exactly the asserted conjugacy classes and orders.

**5.** For \(x<0\), \(-1/x>0\); for \(x>0\), both \(-1/(x+1)\) and \(-(x+1)/x\) are negative. Irrational inputs remain irrational, so no pole or zero interrupts these actions. If the end letters of a reduced word belong to the same factor, successive applications, read from the right, alternate half-lines and send one half-line into the other. Hence the word is not identity. Otherwise replace it by its inverse so that it starts with \(s\) and ends with \(u^e\). Conjugate by the other nonidentity power \(u^j\), \(j\ne e\). Neither end cancels, and the conjugate now starts and ends in the \(u\)-factor, a case already excluded. Therefore every nonempty reduced word has nonidentity image. Generation by \(S,T\) and \(T=s u\) in the projective group gives surjectivity as well, proving the free-product description.

## Analytic facts for subsequent lessons

**Lemma 0.2 (complex-analysis facts for the later lessons).** A holomorphic function has a convergent power series on every sufficiently small disk. On a connected open set it is determined by its values on a set with an interior accumulation point. A holomorphic function on a neighborhood of a closed rectangle has modulus at most its maximum on the boundary. If it is instead meromorphic there, has no pole on the boundary, and has finitely many simple poles in the interior, its positively oriented boundary integral is \(2\pi i\) times the sum of its residues. Locally uniform limits of holomorphic functions are holomorphic.

**Proof.** We include the contour foundations. For a closed triangle contained in the open set, subdivide into four similar triangles by joining side midpoints. The interior edges cancel in the sum of the oriented boundary integrals. If the original integral has modulus \(J\), some subtriangle has integral modulus at least \(J/4\). Iterating gives nested triangles \(D_n\), with diameters and perimeters respectively \(2^{-n}d\) and \(2^{-n}l\), and integral modulus at least \(4^{-n}J\). Their intersection is a single point \(z_0\). Complex differentiability gives
\[
\begin{gathered}
f(z)=f(z_0)+f'(z_0)(z-z_0)+r(z),\\
|r(z)|\le\eta|z-z_0|.
\end{gathered}
\]
on sufficiently small triangles, for every \(\eta>0\). The integrals of the constant and linear terms vanish, by their explicit polynomial primitives. The remaining integral is at most \(\eta ld\,4^{-n}\). Thus \(J\le\eta ld\) for every \(\eta\), forcing \(J=0\). Triangulating a polygon proves the same assertion for it. Shared edges cancel, including across a finite polygonal decomposition of a region with holes.

On a disk, the triangle assertion gives a primitive of any holomorphic function: integrate from a fixed point along a line segment, and compare neighboring segments using their triangle. The change along the small joining segment, divided by its increment, tends to the value of the function by continuity. This proves the primitive derivative directly. The same construction on small disks shows that a contour integral is invariant under a homotopy avoiding singularities: subdivide the parameter square into sufficiently small rectangles whose images lie in disks with such primitives; their integrals cancel. Such a finite subdivision exists by uniform continuity and a finite disk cover of the compact homotopy image. This applies to piecewise smooth contour homotopies.

Choose a closed filled disk contained in the open set, a point \(z\) in its interior, and apply this invariance to \(f(\zeta)/(\zeta-z)\) on the annulus between the circle and a small circle about \(z\). The latter integral tends to \(2\pi i f(z)\): its constant part integrates to that value under \(\zeta=z+re^{it}\), and continuity bounds the remaining integral by \(2\pi\sup_{|\zeta-z|=r}|f(\zeta)-f(z)|\to0\). Hence
\[
\begin{gathered}
f(z)=\frac1{2\pi i}\int_{|\zeta-p|=R}
\frac{f(\zeta)}{\zeta-z}\,d\zeta,\\
|z-p|<R.
\end{gathered}
\]
For \(|z-p|\le r<R\), expand the denominator as the uniformly convergent geometric series in \((z-p)/(\zeta-p)\). Integration gives
\[
\begin{gathered}
f(z)=\sum_{j\ge0}c_j(z-p)^j,\\
c_j=\frac1{2\pi i}\int_{|\zeta-p|=R}
\frac{f(\zeta)}{(\zeta-p)^{j+1}}\,d\zeta,\\
|c_j|\le R^{-j}\max_{|\zeta-p|=R}|f(\zeta)|.
\end{gathered}
\]
These bounds also justify termwise differentiation on smaller disks. A nonzero series whose constant term is zero factors as \((z-p)^h\) times a series with a nonzero constant, so its zero at \(p\) is isolated. If zeros accumulate, every coefficient at that limit point is zero and the function vanishes on a disk. The set of points with a vanishing neighborhood is then open and closed in the connected domain: at a limit point, an accumulating sequence of zeros forces the same conclusion. This proves the identity assertion, including equality of two functions by applying it to their difference.

At an interior local maximum, rotate the function by a constant phase to make \(f(p)=M\ge0\). The circle formula at its centre says \(f(p)\) is the mean of \(f\) on every sufficiently small circle. There \(\operatorname{Re}f\le|f|\le M\), and the mean is \(M\). The nonnegative continuous function \(M-\operatorname{Re}f\) therefore has zero integral and is zero everywhere on that circle. Since \(|f|\le M\), its imaginary part is also zero. This holds on every such circle, giving constancy on a disk and then on the connected domain. If \(M=0\), the same conclusion is immediate. Compactness supplies a maximum on a closed rectangle; an interior maximum forces constancy, so in either case the boundary maximum bounds it.

For the residue assertion, a simple pole at \(p\) means precisely that \(f(z)-c_p/(z-p)\) extends holomorphically near \(p\), where \(c_p\) is its residue. Subtract all these principal parts. The remainder is holomorphic on a neighborhood of the rectangle, so its boundary integral is zero by the triangle proof. The integral of \(1/(z-p)\) on the boundary is \(2\pi i\): shrink the rectangle around its interior point through contours avoiding \(p\), and evaluate on a small circle as above. Adding the principal parts proves the claimed formula with its positive orientation.

Finally a locally uniform limit may be passed through the circle formula, since its circle is compact. The resulting integral of the continuous limit has a convergent power series on every smaller disk by the same geometric expansion. Thus the limit is holomorphic. This also applies to integrals obtained as locally uniform limits of holomorphic finite integrals. \(\square\)

The freely available text of Lebl, Sections 2.4 and 3.2–3.3, provides background for these classical steps. The contour and power-series facts needed by the later lessons have been written here.

**Local inverse consequence.** If \(f'(p)=a\ne0\), then \(f\) has a holomorphic inverse on a neighborhood of \(f(p)\). To prove this, take a small closed disk of radius \(R\) on which \(|f'(z)-a|\le|a|/2\). Integration along a segment bounds the difference of \(g(z)=f(z)-f(p)-a(z-p)\) at two points by \((|a|/2)|z_1-z_2|\). For \(|w-f(p)|<|a|R/2\), iterate
\[
z_{j+1}=p+\frac{w-f(p)-g(z_j)}a,\qquad z_0=p.
\]
This map takes the disk to itself and contracts distances by at most \(1/2\). Its successive differences form a bounded geometric series, so the iterates converge in the closed disk. Passing to the limit gives \(f(z)=w\), and the same contraction shows uniqueness. Each iterate is holomorphic in \(w\); the geometric error bound is locally uniform, so Lemma 0.2 makes the limit holomorphic. For a slightly smaller target disk the image lies strictly inside the source disk, yielding the required local inverse.

A nonconstant holomorphic map has a local form \(u\mapsto u^r\) in suitable coordinates: its convergent series gives \(f(z)-f(p)=a(z-p)^r(1+h(z))\), with \(a\ne0\) and \(h(p)=0\). Shrink until \(|h|<1\). The convergent series for \(\log(1+h)\) gives a holomorphic logarithm there (differentiate its geometric series and fix its value zero at \(p\)). Choose one complex \(r\)-th root of \(a\) and set
\(u=a^{1/r}(z-p)\exp(\log(1+h(z))/r)\).
Then \(u'(p)=a^{1/r}\ne0\), so the local inverse just proved makes \(u\) a coordinate, and the map is exactly \(u^r\). This proves the local branching description used for the modular covering.

**Lemma 0.3 (the continuous improper-integral interchanges used below).** Let \(J\) be an interval, possibly unbounded. All integrals in this lemma are limits over increasing compact subintervals. The following statements concern continuous functions; they make no assertion about arbitrary measurable functions.

1. Suppose \(g_n\) are continuous on \(J\), their series converges uniformly on each compact subinterval, and \(\sum_n\int_J|g_n|<\infty\). Then its sum \(g\) is absolutely integrable and
\[
\begin{gathered}
\int_J g=\sum_n\int_Jg_n,\\
\int_J\left|g-\sum_{n\le A}g_n\right|
\le\sum_{n>A}\int_J|g_n|.
\end{gathered}
\]
For a locally uniformly convergent series of nonnegative continuous functions, the equality of the integral and the sum of integrals holds with infinity allowed, without assuming finiteness in advance. The same assertions hold on an open plane domain \(D\), with an increasing compact exhaustion \(K_j\subset\operatorname{int}K_{j+1}\), \(\bigcup_jK_j=D\), in which each \(K_j\) is a bounded region with finitely many piecewise continuously differentiable boundary arcs. Require continuity on \(D\), uniform convergence on every compact subset, and one fixed nonnegative continuous density \(w\); define the improper area integral by this exhaustion.

2. Let \(h\) be continuous on \(J\times I\), where \(J,I\) are intervals, and suppose \(|h(x,t)|\le p(x)q(t)\), where \(p,q\) are nonnegative continuous functions with finite improper integrals. Both iterated integrals exist absolutely and are equal. If continuous functions \(h_\alpha\) share this same fixed majorant and converge uniformly on every compact rectangle to \(h\), both iterated integrals converge to the corresponding integrals of \(h\). Also, if continuous \(u_\alpha\) on \(J\) converge uniformly on compact intervals to \(u\), and \(|u_\alpha|\le p\) for one continuous integrable \(p\), then \(u\) is absolutely integrable and \(\int_Ju_\alpha\to\int_Ju\).

3. Suppose \(H(s,x)\) is jointly continuous for \(s\) in an open complex set and \(x\in J\), holomorphic in \(s\) for each \(x\). If each compact set of parameters has a nonnegative continuous integrable majorant \(p(x)\) for \(|H(s,x)|\), then \(\int_JH(s,x)dx\) is holomorphic in \(s\). The same conclusion holds for the plane integrals and fixed density in part 1.

**Proof.** On a compact interval, uniform convergence permits passage through the integral: the error is at most the interval length times the uniform error. For part 1, apply this observation to the finite tail sums, and use the triangle inequality. On every compact subinterval their limit has integral of its absolute value bounded by \(\sum_{n>A}\int_J|g_n|\). Exhausting \(J\) proves the displayed bound, including absolute integrability at \(A=0\). Its right side tends to zero, so the integral identity follows. For a nonnegative series, each finite partial sum gives the lower bound \(\sum_{n\le A}\int_Jg_n\le\int_Jg\). Conversely, on a compact subinterval uniform convergence gives \(\int_Kg=\sum_n\int_Kg_n\le\sum_n\int_Jg_n\). Exhaust \(J\) for the reverse bound. This proves the nonnegative assertion, also when either side is infinite.

For the compact plane integrals, cover each of the finitely many boundary arcs by its continuously differentiable pieces. Its derivative is bounded on the compact parameter interval. Subdivide that interval into \(O(1/\varepsilon)\) pieces with image diameter at most \(\varepsilon\). Each image meets a bounded number of square-grid cells of side \(\varepsilon\), so all boundary cells have total area \(O(\varepsilon)\). Uniform continuity controls the upper-minus-lower sum on the remaining interior cells by the region's area times the modulus of continuity at \(\sqrt2\varepsilon\). On boundary cells the error is at most twice the maximum modulus times their total area. Both errors tend to zero. This proves the compact area integral, also for a continuous density by applying the same argument to the product with \(w\); holes add only finitely many boundary arcs.

For the plane version of part 1, replace the interval length in the compact uniform error bound by the region's area times the maximum of its continuous density. The identical exhaustion and tail argument then applies.

For part 2, each inner integral exists absolutely by the bound \(p(x)q(t)\). On a compact \(x\)-interval \(K\), the omitted inner tail is at most \(\max_Kp\) times the omitted \(q\)-integral. The inner integral is consequently a locally uniform limit of continuous compact integrals and is continuous in \(x\). Its absolute value is at most \(p(x)\int_Iq\), so the outer integral exists absolutely. The same argument applies in the other order.

On a compact rectangle the two integrals of a continuous function agree. Indeed uniform continuity makes the same rectangular Riemann sums approximate both orders: refine both partitions until the oscillation on every cell is less than a given number; the total error is at most this number times the rectangle area. For part 2, choose compact intervals \(K,L\) with small \(p\)- and \(q\)-integrals on their complements. Outside \(K\times L\), the absolute error in either order is at most
\[
 \left(\int_{J\setminus K}p\right)\left(\int q\right)
 +\left(\int p\right)\left(\int_{I\setminus L}q\right).
\]
It tends to zero independently of the order. On the retained rectangle use the equality just proved. This also proves the limiting assertion by first choosing the rectangle and then using uniform convergence there. For a one-variable limit with an integrable majorant the same argument uses a compact interval, with tail error at most twice the majorant integral outside it.

For part 3, truncated integrals over a compact interval are locally uniform limits of holomorphic Riemann sums. Joint continuity on compact parameter products gives their uniform approximation. Lemma 0.2 proves that these truncated integrals are holomorphic. The integrable majorant makes their tails uniformly small on each compact parameter set. Another application of Lemma 0.2 therefore proves holomorphy of the full integral. For a compact plane region use fixed grid Riemann sums; the boundary-grid bound just proved and joint uniform continuity give locally uniform convergence in the parameters. The same majorant tail argument then applies to its exhaustion. \(\square\)

These proofs justify the particular continuous series, Gaussian double integrals, and holomorphic-parameter integrals used later. A general measure-theoretic Tonelli, Fubini or dominated-convergence theorem is a separate foundational result.

## What this lesson does not prove

Lemma 0.1 proves the Euclidean and Bezout statements used in reduction. The semicircle example includes its minimizing-length argument, and the area calculation uses a direct integral. Lemma 0.2 and its local inverse consequence supply the contour, power-series and branching facts needed later. Lemma 0.3 supplies the stated continuous improper-integral interchanges and holomorphic-parameter integrals. General measurable integration and plane change of variables are separate foundational results. Basic real differentiation, integration, integer division, the well-ordering of positive integers and elementary compactness of bounded closed subsets of the plane remain foundational prerequisites. Exact earlier programme proofs for those foundations have not been verified in this lesson, so the stronger all-dependencies proof-closure requirement remains open at that level. The invariant metric's general geodesic theory is not asserted.

## References

- J. Lebl, *A Guide to Cultivating Complex Analysis*, freely distributed author text, version 1.9, Sections 2.4 and 3.2–3.3. [Free author PDF](https://www.jirka.org/ca/ca.pdf). Lemma 0.2 above gives the local proofs used in this course.

- [Wiese 2018] G. Wiese, *Computational Arithmetic of Modular Forms*, lecture notes, 2018, §§4.1–4.2. [Open text](https://arxiv.org/abs/1809.04645).
- [Voight open book] J. Voight, *Quaternion Algebras*, freely distributed stable post-publication version 1.0.5 (10 January 2024), §§33.3–33.6 and §35.1. [Author's stable free PDF](https://jvoight.github.io/quat-book-v1.0.5.pdf).

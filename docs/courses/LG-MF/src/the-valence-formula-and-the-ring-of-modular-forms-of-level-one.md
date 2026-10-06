# The valence formula and the ring of modular forms of level one

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The weight of a modular form controls its total number of zeros. At the two elliptic points, the count is fractional because a quotient coordinate identifies several local directions. This zero count will determine every level-one space, produce the discriminant and the modular coordinate \(j\), and turn identities among forms into identities among divisor sums.

We use Modular forms, lattice functions and Eisenstein series, together with the fundamental domain, side identifications and quotient charts proved in the first three lessons. The valence calculation below derives the boundary contributions explicitly. The free comparison sources are [Stein author PDF, §§2.2–2.3] and [Voight open book, §40.3].

Write \(\Gamma=\mathrm{SL}_2(\mathbb Z)\), \(q=e^{2\pi iz}\), and
\(\rho=(-1+i\sqrt3)/2\). We abbreviate \(M_k=M_k(\Gamma)\) and \(S_k=S_k(\Gamma)\).
A meromorphic modular form here is meromorphic on \(\mathfrak H\), transforms with integral weight \(k\), and has a Laurent series in \(q\) with only finitely many negative powers at infinity. For a nonzero such form, \(v_p(f)\) is its order in the ordinary coordinate \(z-p\), and \(v_\infty(f)\) is its order in \(q\). Orders of poles are negative.

## 1. Counting zeros by the valence formula

**Lemma 0.1 (the zero-counting principle used here).** For a nonzero meromorphic function on a neighborhood of a compact planar region, with no zeros or poles on its positively oriented boundary,
\[
\frac1{2\pi i}\int_{\partial D}\frac{f'}f\,dz
=\sum_{p\in D}\operatorname{ord}_p(f).
\]

*Proof.* The Taylor or Laurent expansion at a zero or pole has the form \(f(z)=(z-p)^n u(z)\), with \(u\) holomorphic and nonvanishing; hence \(f'/f=n/(z-p)+u'/u\). Excise disjoint small discs around the finitely many zeros and poles. On the remainder \(f'/f\) is holomorphic, and Cauchy's theorem says its total boundary integral is zero. The positively oriented circle around each excised point has integral \(2\pi i n\), since \(u'/u\) is holomorphic on that disc. Summing those circle integrals gives the formula. This derives the argument principle from Cauchy's theorem and the local expansions proved in the preceding lesson, Lemma 0.1. \(\square\)

**Theorem 1.1 (valence formula).** For a nonzero meromorphic modular form \(f\) of weight \(k\),
\[
v_\infty(f)+\frac12v_i(f)+\frac13v_\rho(f)
+\sum_{\substack{[p]\in\Gamma\backslash\mathfrak H\\
 [p]\ne[i],[\rho]}}v_p(f)=\frac{k}{12}.
\tag{1.1}
\]
The sum has finite support. Each ordinary orbit is counted once.

**Proof.** A change of variable by an element of \(\Gamma\) multiplies \(f\) by a nonvanishing holomorphic factor, so the order is constant on each orbit. Near the cusp, write
\(f=q^n u(q)\), with \(u(0)\ne0\). There are no zeros or poles at sufficiently large finite height. On the remaining compact part of the closed domain
\[
\mathcal F=\{z\in\mathfrak H:|\operatorname{Re}z|\le1/2,\ |z|\ge1\},
\]
zeros and poles are isolated and hence finite. This proves finiteness.

Let \(L=f'/f\). Differentiating \(f(Sz)=z^k f(z)\) and using \(S'(z)=z^{-2}\) gives
\[
L(Sz)\,d(Sz)=L(z)\,dz+k\,\frac{dz}{z}.
\tag{1.2}
\]
Also \(L(z+1)=L(z)\).

Truncate \(\mathcal F\) at a sufficiently large height \(Y\).
Its positively oriented boundary goes along the unit arc from \(\rho\) to \(\rho+1\), up the right side, left along the top, and down the left side.
Excise a small disc about each zero or pole on that boundary. The new boundary follows the inner portions of these circles clockwise. Take equal radii for the two points of each paired boundary orbit. On the vertical sides this is compatible with \(T\). On the unit circle, \(S(e^{i\theta})=e^{i(\pi-\theta)}\), which preserves chord distances between paired points, so it is compatible with the arc cuts as well. At \(i\), choose symmetric cuts on the two halves of the unit arc. At \(\rho,\rho+1\), use equal radii. All these discs may be chosen disjoint, with no other zeros or poles inside.

The vertical integrals cancel by periodicity. The top contributes exactly \(-v_\infty(f)\) after division by \(2\pi i\). Indeed \(q\) traverses one circle clockwise there, and \(f=q^n u(q)\), with \(u\) nonvanishing inside that small circle.

Split the remaining unit arc into a left half \(A\), oriented from \(\rho\) towards \(i\), and a right half. The map \(S\) sends \(A\) to the right half with opposite orientation. Thus (1.2) gives
\[
\int_{\text{remaining unit arc}}L(z)\,dz
=-k\int_{\text{remaining left half}}\frac{dz}{z}.
\]
As the small radii tend to zero, the last integral tends to
\(i(\pi/2-2\pi/3)=-i\pi/6\).
The normalized contribution of the unit arc is therefore \(k/12\).

If \(p\) has order \(v\), then \(L(z)=v/(z-p)+O(1)\) near \(p\).
A clockwise excision arc spanning an interior angle \(\beta\) contributes
\(-v\beta/(2\pi)\) in the limit. At an ordinary smooth boundary point the angle is \(\pi\); its paired representative supplies another \(\pi\), so an ordinary boundary orbit contributes \(-v_p(f)\). At \(i\) there is just one half-disc, giving \(-v_i(f)/2\). Each corner \(\rho,\rho+1\) has angle \(\pi/3\), and their orders agree by \(T\); together they give \(-v_\rho(f)/3\).

The argument principle on this excised domain counts exactly the orders of the strictly interior zeros and poles, excluding the removed boundary ones. It therefore says
\[
\sum_{\text{strict interior}}v_p(f)
=-v_\infty(f)+\frac{k}{12}
-\frac12v_i(f)-\frac13v_\rho(f)
-\sum_{\text{ordinary boundary orbits}}v_p(f).
\]
Moving the boundary terms to the left proves (1.1). This argument includes both zeros and poles, with their signed orders. \(\square\)

In particular, if \(f\) is holomorphic and nonzero, all orders on the left are nonnegative. This gives the useful bound
\[
v_\infty(f)\le k/12.
\tag{1.3}
\]
The fractions at \(i\) and \(\rho\) belong to the quotient geometry. They are not changes in the ordinary orders \(v_i\) and \(v_\rho\).

## 2. The discriminant and all dimensions

The transformation laws from the preceding lesson force \(E_4(\rho)=0\) and \(E_6(i)=0\). The valence formula makes these statements precise:
\[
v_\rho(E_4)=1,\qquad v_i(E_6)=1,
\tag{2.1}
\]
and neither form has any other zero orbit in \(\mathfrak H\).
For \(E_4\), its zero at \(\rho\) contributes at least \(1/3=4/12\); for \(E_6\), its zero at \(i\) contributes at least \(1/2=6/12\). Their cusp orders are zero, so equality leaves room for no other zeros and forces each indicated ordinary order to be one.

**Theorem 2.1 (the discriminant).** Define
\[
\Delta=\frac{E_4^3-E_6^2}{1728}.
\tag{2.2}
\]
Then \(\Delta\in S_{12}\), \(v_\infty(\Delta)=1\), and \(\Delta\) has no zeros on \(\mathfrak H\). For every integer \(k\), multiplication by \(\Delta\) is an isomorphism
\[
M_{k-12}\longrightarrow S_k.
\tag{2.3}
\]

**Proof.** Both terms in (2.2) have weight twelve and constant term one, so their difference is a cusp form. Their coefficients of \(q\) are \(3\cdot240=720\) and \(2(-504)=-1008\), whose difference is \(1728\).
Thus \(\Delta=q+O(q^2)\), proving it is nonzero with cusp order one.
Its valence formula has right side one, already supplied by the cusp. All other orders must be zero.

Multiplication by \(\Delta\) is injective, because \(\Delta\) is nonzero, and maps \(M_{k-12}\) into \(S_k\).
For \(f\in S_k\), the quotient \(f/\Delta\) is holomorphic on \(\mathfrak H\), has weight \(k-12\), and is holomorphic at infinity because \(f\) has cusp order at least one. Thus it lies in \(M_{k-12}\), proving surjectivity. \(\square\)

Here is a rescaling calculation from the locally proved Eisenstein expansions. Define \(g_4=60G_4\) and \(g_6=140G_6\).
The preceding lesson, Proposition 4.1, Theorem 4.2 and Solution 4, gives
\(\zeta(4)=\pi^4/90\), \(\zeta(6)=\pi^6/945\), and \(G_k=2\zeta(k)E_k\).
Consequently
\[
g_4=\frac{4\pi^4}{3}E_4,\qquad
g_6=\frac{8\pi^6}{27}E_6,
\]
and direct substitution into (2.2) gives
\[
g_4^3-27g_6^2
=\frac{64\pi^{12}}{27}(E_4^3-E_6^2)
=(2\pi)^{12}\Delta.
\tag{2.7}
\]
Thus the normalized cusp form and this lattice discriminant differ by the displayed constant.

**Theorem 2.2 (dimensions).** Odd weights and negative weights have \(M_k=0\). For even \(k\ge0\),
\[
\dim M_k=
\begin{cases}
\lfloor k/12\rfloor,&k\equiv2\pmod{12},\\
\lfloor k/12\rfloor+1,&k\not\equiv2\pmod{12}.
\end{cases}
\tag{2.4}
\]
For all integers \(k\), \(\dim S_k=\dim M_{k-12}\).
The spaces \(M_0,M_4,M_6,M_8,M_{10},M_{14}\) have dimension one, and \(M_2=0\).

**Proof.** Odd-weight vanishing was proved using \(-I\) in the preceding lesson.
Negative weight contradicts the nonnegative left side of (1.1).
For weight two, the right side is \(1/6\), while a positive term on the left is at least \(1/3\); if all terms are zero, the sum is zero. Both possibilities contradict \(1/6\). Thus \(M_2=0\).

If \(0\le k<12\), bound (1.3) says a nonzero form cannot be cuspidal. Evaluation of the constant term is therefore injective, so \(\dim M_k\le1\). Constants give \(M_0=\mathbb C\), and \(E_4,E_6,E_8,E_{10}\) give equality in their weights.

For every even \(k\ge4\), choose \(a,b\ge0\) with \(4a+6b=k\):
take \(b=0\) if \(4\mid k\), and \(b=1\) if \(k\equiv2\pmod4\).
The latter case has \(k\ge6\), so \(a=(k-6)/4\ge0\).
The form \(F=E_4^aE_6^b\) has constant term one. Subtracting the constant term times \(F\) from any \(f\in M_k\) gives
\[
M_k=\mathbb C F\oplus S_k.
\tag{2.5}
\]
Theorem 2.1 now gives \(\dim M_k=1+\dim M_{k-12}\).
Starting with the six even residues \(0,2,4,6,8,10\), whose dimensions are
\(1,0,1,1,1,1\), proves (2.4).
It also proves \(S_k=\Delta M_{k-12}\) in dimensions, including \(S_{14}=0\) and \(\dim M_{14}=1\). \(\square\)

**Theorem 2.3 (the level-one ring).** The graded algebra
\[
M_*=\bigoplus_{k\ge0}M_k
\]
is the polynomial algebra \(\mathbb C[E_4,E_6]\), with weights four and six on the two generators. For each \(k\), the monomials
\[
E_4^aE_6^b,\qquad a,b\ge0,\quad4a+6b=k
\tag{2.6}
\]
form a basis. The functions \(E_4,E_6\) are algebraically independent even when viewed as ordinary holomorphic functions.

**Proof.** The generation statement follows by induction on the weight.
In weights below twelve it follows from Theorem 2.2. For larger even \(k\), choose \(F\) as in (2.5). Write \(f=cF+\Delta g\), where \(g\in M_{k-12}\).
By induction \(g\) is a polynomial in \(E_4,E_6\), and \(\Delta\) is such a polynomial by (2.2). Thus every \(f\) is a polynomial of the required weight.

To prove independence in a fixed weight, note from (2.1) that \(E_4(i)\ne0\) and \(E_6\) has an ordinary simple zero at \(i\).
The order at \(i\) of the monomial in (2.6) is therefore \(b\).
Distinct monomials of that weight have distinct \(b\). In any proposed nontrivial linear relation, the term with the smallest \(b\) has a nonzero leading coefficient in its local expansion and cannot be cancelled by terms of larger order. This proves independence.

Finally suppose an ordinary polynomial \(P(E_4,E_6)\) vanishes identically. Decompose \(P=\sum_kP_k\) by weighted degree. For each fixed \(z\in\mathfrak H\) and each integer \(c\), apply the transformation
\(\gamma_c=\begin{pmatrix}1&0\\c&1\end{pmatrix}\):
\[
0=P(E_4(\gamma_cz),E_6(\gamma_cz))
=\sum_k(cz+1)^k P_k(E_4(z),E_6(z)).
\]
The numbers \(cz+1\) are distinct as \(c\) varies. A polynomial in this number with infinitely many zeros has every coefficient zero.
Thus each \(P_k(E_4,E_6)\) vanishes. Fixed-weight independence then makes each \(P_k\) the zero polynomial, so \(P=0\). \(\square\)

## 3. The modular coordinate \(j\)

Define
\[
j(z)=\frac{E_4(z)^3}{\Delta(z)}.
\tag{3.1}
\]
It is holomorphic on \(\mathfrak H\), invariant under \(\Gamma\), and has a simple pole at the cusp.
Equation (2.2) gives
\[
j-1728=\frac{E_6^2}{\Delta},
\qquad j(\rho)=0,\qquad j(i)=1728.
\tag{3.2}
\]

**Theorem 3.1 (the coordinate and the function field).** The induced map
\[
\Gamma\backslash\mathfrak H\longrightarrow\mathbb C,\qquad[z]\mapsto j(z)
\]
is bijective. It extends to a biholomorphism \(X(1)\to\mathbb P^1(\mathbb C)\).
Every level-one meromorphic modular function is a rational function of \(j\), and every rational function of \(j\) is such a modular function.

**Proof.** For \(a\in\mathbb C\), the weight-twelve form
\(E_4^3-a\Delta\) has constant term one, so it is nonzero and its cusp order is zero.
Its valence formula says the weighted sum of its interior zeros is one.
For \(a=0\), equation (2.1) gives a zero of order three at \(\rho\), exhausting that count.
For \(a=1728\), equation (3.2) gives a zero of order two at \(i\), again exhausting it.
For any other \(a\), there is no zero at either elliptic orbit, because of the computed \(j\)-values. All zeros then have integral weights in the sum, so there is exactly one ordinary orbit, with a simple zero. In every case, there is exactly one orbit mapping to \(a\).

We check the complex structure at the exceptional points. At \(\rho\), the invariant function \(j\) has ordinary order three; in the quotient coordinate \(u=w^3\) from the preceding geometry lessons, it has order one. At \(i\), \(j-1728\) has ordinary order two and therefore order one in \(u=w^2\).
At ordinary points, the already proved simple-zero statement gives a local inverse. At the cusp, \(1/j=q+O(q^2)\), so \(1/j\) is a local coordinate. The bijection therefore extends across the cusp and has holomorphic local inverses everywhere, proving the biholomorphism.

Let \(f\) be a meromorphic modular function. It descends meromorphically to \(X(1)\). At an elliptic point, this can be checked directly: in a rotation coordinate \(w\), invariance forces the Laurent exponents of \(f\) to be multiples of the stabilizer order, giving a Laurent series in \(u=w^e\). At the cusp it is the assumed Laurent series in \(q\).
Under the biholomorphism \(j\), it is a meromorphic function \(h\) on \(\mathbb P^1\).

Such an \(h\) is rational. Its poles form a discrete subset of a compact surface, hence a finite set. For each finite pole \(a\), subtract its finite principal part
\(\sum_{r=1}^{m_a}c_{a,r}(t-a)^{-r}\).
At infinity subtract the polynomial determined by the negative powers in the coordinate \(1/t\).
The remainder is holomorphic on the sphere; restricted to \(\mathbb C\), it is entire and bounded near infinity and on a compact disc, hence constant by Liouville's theorem.
Thus \(h(t)\) is the sum of a polynomial, those finitely many principal parts, and a constant: a rational function. Substitution \(t=j\) gives \(f\in\mathbb C(j)\).
Conversely a rational expression in \(j\) is invariant and meromorphic, including at the cusp, because \(j\) has a finite-order pole there. \(\square\)

## 4. The product formula without circularity

**Theorem 4.1.** For every \(z\in\mathfrak H\),
\[
\Delta(z)=q\prod_{n\ge1}(1-q^n)^{24}.
\tag{4.1}
\]
In particular all Fourier coefficients of \(\Delta\) are integers.

**Proof.** Define the right side to be \(P(z)\). On every compact subset of \(\mathfrak H\), \(|q|\le R<1\), and
\[
\log(1-q^n)=-\sum_{r\ge1}\frac{q^{nr}}r
\]
has an absolutely and locally uniformly convergent double sum over \(n,r\).
Thus
\[
P(z)=\exp\left(2\pi iz+24\sum_{n\ge1}\log(1-q^n)\right)
\]
is holomorphic and nonzero. Differentiating locally uniformly gives
\[
\frac{P'}P
=2\pi i\left(1-24\sum_{n\ge1}\frac{nq^n}{1-q^n}\right)
=2\pi i E_2.
\tag{4.2}
\]
The final equality groups the absolutely convergent double sum by its exponent.

Put \(R(z)=P(-1/z)/(z^{12}P(z))\). This is a nowhere vanishing holomorphic function.
Using the transformation law of \(E_2\) proved in the preceding lesson,
\[
\begin{aligned}
\frac{R'}R
&=\frac{2\pi i}{z^2}E_2(-1/z)-\frac{12}z-2\pi iE_2(z)\\
&=\frac{2\pi i}{z^2}\left(z^2E_2(z)+\frac{6z}{\pi i}\right)
-\frac{12}z-2\pi iE_2(z)=0.
\end{aligned}
\]
Consequently \(R\) is constant on the connected half-plane. At \(z=i\), we have \(S(i)=i\) and \(i^{12}=1\), so \(R(i)=1\). It follows that \(P(-1/z)=z^{12}P(z)\).
The product expression gives \(P(z+1)=P(z)\).
Since \(S,T\) generate \(\Gamma\), \(P\) has weight twelve for \(\Gamma\).
Also \(P=q+O(q^2)\), so it is a cusp form. The one-dimensionality of \(S_{12}\), and its leading coefficient one, give \(P=\Delta\).

For any fixed exponent, only finitely many factors in (4.1) can contribute to its coefficient. Each factor \((1-q^n)^{24}\) is a polynomial with integer coefficients. Every coefficient of \(\Delta\) is therefore an integer. \(\square\)

If one writes the Dedekind eta function as
\[
\eta(z)=e^{2\pi iz/24}\prod_{n\ge1}(1-q^n),
\]
the same convergence argument gives a nonzero holomorphic function with
\(\eta'/\eta=(2\pi i/24)E_2\), and \(\eta^{24}=\Delta\).
The exponential specifies the root of \(q\) on \(\mathfrak H\). The proof above establishes exactly the transformation of the twenty-fourth power; no unproved eta multiplier is needed.

## 5. Ramanujan's congruence

Write
\[
\Delta(z)=\sum_{n\ge1}\tau(n)q^n.
\tag{5.1}
\]
Theorem 4.1 proves \(\tau(n)\in\mathbb Z\).

**Theorem 5.1.** For every positive integer \(n\),
\[
\tau(n)\equiv\sigma_{11}(n)\pmod{691}.
\tag{5.2}
\]

**Proof.** The preceding lesson computed \(B_{12}=-691/2730\), so
\[
E_{12}=1+\frac{65520}{691}\sum_{n\ge1}\sigma_{11}(n)q^n.
\]
The form \(E_{12}-E_4^3\) is cuspidal of weight twelve, hence a multiple of \(\Delta\).
Its coefficient of \(q\) is \(65520/691-720=-432000/691\). Therefore
\[
691(E_{12}-E_4^3)=-432000\Delta.
\tag{5.3}
\]
All coefficients of \(E_4^3\) are integers. Comparison of the coefficient of \(q^n\) gives
\[
65520\,\sigma_{11}(n)-691[q^n]E_4^3=-432000\,\tau(n).
\]
Since \(65520+432000=691\cdot720\), reduction modulo \(691\) yields
\(65520(\sigma_{11}(n)-\tau(n))\equiv0\).
The factor \(65520\) is invertible modulo \(691\): its remainder is \(566\), and the Euclidean algorithm
\(691=566+125,\ 566=4\cdot125+66,\ 125=66+59,\ 66=59+7,\ 59=8\cdot7+3,\ 7=2\cdot3+1\)
proves coprimality. Cancellation proves (5.2). \(\square\)

## 6. Worked examples

### 6.1. Three divisor-sum identities

The one-dimensional spaces of weights eight, ten and fourteen contain forms with constant term one. Comparing those constant terms gives
\[
E_8=E_4^2,\qquad E_{10}=E_4E_6,\qquad E_{14}=E_8E_6=E_4^2E_6.
\]
The coefficient of \(q^n\) in the first identity is
\[
480\sigma_7(n)=480\sigma_3(n)
+57600\sum_{m=1}^{n-1}\sigma_3(m)\sigma_3(n-m).
\]
Thus
\[
\sigma_7(n)=\sigma_3(n)
+120\sum_{m=1}^{n-1}\sigma_3(m)\sigma_3(n-m).
\tag{6.1}
\]
For the second, multiplying the expansions of \(E_4,E_6\) gives
\[
-264\sigma_9(n)=240\sigma_3(n)-504\sigma_5(n)
-120960\sum_{m=1}^{n-1}\sigma_3(m)\sigma_5(n-m).
\]
Division by \(-24\) yields
\[
11\sigma_9(n)=21\sigma_5(n)-10\sigma_3(n)
+5040\sum_{m=1}^{n-1}\sigma_3(m)\sigma_5(n-m).
\tag{6.2}
\]
Finally, use \(E_8E_6\):
\[
-24\sigma_{13}(n)=480\sigma_7(n)-504\sigma_5(n)
-241920\sum_{m=1}^{n-1}\sigma_7(m)\sigma_5(n-m),
\]
so
\[
\sigma_{13}(n)=21\sigma_5(n)-20\sigma_7(n)
+10080\sum_{m=1}^{n-1}\sigma_7(m)\sigma_5(n-m).
\tag{6.3}
\]
The sum is empty when \(n=1\). As numerical checks at \(n=2\), these formulas give
\(129=9+120\),
\(11\cdot513=21\cdot33-10\cdot9+5040\), and
\(8193=21\cdot33-20\cdot129+10080\).

### 6.2. Computing \(\Delta\) and \(j\)

From (4.2), logarithmic differentiation of \(\Delta\) gives
\(q\,d\Delta/dq=E_2\Delta\).
Consequently, for \(n\ge2\),
\[
(n-1)\tau(n)=-24\sum_{m=1}^{n-1}\sigma_1(m)\tau(n-m),
\qquad \tau(1)=1.
\tag{6.4}
\]
This determines successive coefficients. The first five sums on the right, before multiplication by \(-24\), are
\[
\begin{aligned}
n=2:&\quad1,\\
n=3:&\quad-24+3=-21,\\
n=4:&\quad252-72+4=184,\\
n=5:&\quad-1472+756-96+7=-805,\\
n=6:&\quad4830-4416+1008-168+6=1260.
\end{aligned}
\]
Division by \(n-1\) in (6.4) gives
\[
\Delta=q-24q^2+252q^3-1472q^4+4830q^5-6048q^6+O(q^7).
\tag{6.5}
\]

For \(j\), write \(A=E_4^3\) and \(D=\Delta/q\), so that \(qj=A/D\).
From the preceding lesson's coefficients,
\[
A=1+720q+179280q^2+16954560q^3+396974160q^4+O(q^5).
\]
For example, its \(q^3\) coefficient is
\(3\cdot6720+6\cdot240\cdot2160+240^3=16954560\);
its \(q^4\) coefficient is
\(3\cdot17520+6\cdot240\cdot6720+3\cdot2160^2+
3\cdot240^2\cdot2160=396974160\).
If \(qj=\sum_{r\ge0}c_rq^r\), division by
\(D=1-24q+252q^2-1472q^3+4830q^4+\cdots\) gives
\[
\begin{aligned}
c_0&=1,\\
c_1&=720+24=744,\\
c_2&=179280+24\cdot744-252=196884,\\
c_3&=16954560+24\cdot196884-252\cdot744+1472=21493760,\\
c_4&=396974160+24\cdot21493760-252\cdot196884
+1472\cdot744-4830=864299970.
\end{aligned}
\]
Thus
\[
j=q^{-1}+744+196884q+21493760q^2+864299970q^3+O(q^4).
\tag{6.6}
\]

### 6.3. The congruence for six coefficients

The divisor sums are
\(\sigma_{11}(p)=1+p^{11}\),
\(\sigma_{11}(4)=1+2^{11}+4^{11}\), and
\(\sigma_{11}(6)=1+2^{11}+3^{11}+6^{11}\).
These, together with (6.5), give:

| \(n\) | \(\tau(n)\) | \(\sigma_{11}(n)\) | Common remainder modulo \(691\) |
|---:|---:|---:|---:|
| 1 | \(1\) | \(1\) | \(1\) |
| 2 | \(-24\) | \(2049\) | \(667\) |
| 3 | \(252\) | \(177148\) | \(252\) |
| 4 | \(-1472\) | \(4196353\) | \(601\) |
| 5 | \(4830\) | \(48828126\) | \(684\) |
| 6 | \(-6048\) | \(362976252\) | \(171\) |

For example, \(4196353=691\cdot6072+601\), while
\(-1472=691(-3)+601\).
The table checks the first six cases; Theorem 5.1 proves the congruence for every \(n\).

## 7. Exercises

1. **Easy.** Tabulate \(\dim M_k\) and \(\dim S_k\) for all \(0\le k\le30\), including odd weights.
2. **Easy.** Derive the identity for \(\sigma_9(n)\) from \(E_{10}=E_4E_6\).
3. **Medium.** Deduce Ramanujan's congruence from
\(691(E_{12}-E_4^3)=-432000\Delta\), checking the integrality and the modular cancellation needed.
4. **Medium.** Prove the level-one coefficient bound: if \(f\in M_k\) has \(v_\infty(f)>k/12\), then \(f=0\).
5. **Medium.** Construct the Victor Miller basis of \(M_k\): if \(d=\dim M_k\), construct the unique basis \(F_0,\ldots,F_{d-1}\) with
\(F_j=q^j+O(q^d)\). Prove that every coefficient of every \(F_j\) is an integer. Compute examples in weights twelve and twenty-four.
6. **Hard.** Prove that every meromorphic level-one modular function is a rational function of \(j\). Give an explicit construction from the principal parts at its finitely many poles.

## 8. Full solutions

### Solution 1

The dimension formula gives the following table for even weights:

| \(k\) | \(\dim M_k\) | \(\dim S_k=\dim M_{k-12}\) |
|---:|---:|---:|
| 0 | 1 | 0 |
| 2 | 0 | 0 |
| 4 | 1 | 0 |
| 6 | 1 | 0 |
| 8 | 1 | 0 |
| 10 | 1 | 0 |
| 12 | 2 | 1 |
| 14 | 1 | 0 |
| 16 | 2 | 1 |
| 18 | 2 | 1 |
| 20 | 2 | 1 |
| 22 | 2 | 1 |
| 24 | 3 | 2 |
| 26 | 2 | 1 |
| 28 | 3 | 2 |
| 30 | 3 | 2 |

Every odd weight in this range has both dimensions zero, by \(-I\).
For negative arguments in the last column, \(\dim M_{k-12}=0\).
For example, weight twenty-six has \(\lfloor26/12\rfloor=2\) and residue two, so its modular dimension is two; its cusp dimension is \(\dim M_{14}=1\).
These rules account for every integer in the requested range.

### Solution 2

The constant-normalized series have coefficients
\([q^n]E_{10}=-264\sigma_9(n)\),
\([q^n]E_4=240\sigma_3(n)\), and
\([q^n]E_6=-504\sigma_5(n)\).
In their product, the terms with a constant factor contribute
\(240\sigma_3(n)-504\sigma_5(n)\).
The terms with both exponents positive contribute
\(-240\cdot504\sum_{m=1}^{n-1}\sigma_3(m)\sigma_5(n-m)\).
Equating coefficients and dividing by \(-24\) gives
\[
11\sigma_9(n)=21\sigma_5(n)-10\sigma_3(n)
+5040\sum_{m=1}^{n-1}\sigma_3(m)\sigma_5(n-m).
\]
There is no convolution term for \(n=1\), which gives \(11=21-10\).
This proves the identity with its coefficients and its endpoint convention.

### Solution 3

By Theorem 4.1, \(\tau(n)\in\mathbb Z\). By the explicit expansion of \(E_4\), its coefficients and therefore those of \(E_4^3\) are integers.
For \(n\ge1\), comparison of coefficients in the given identity reads
\[
65520\sigma_{11}(n)-691[q^n]E_4^3=-432000\tau(n).
\]
The equality \(65520+432000=691\cdot720\) rewrites this as
\[
65520(\sigma_{11}(n)-\tau(n))
=691\bigl([q^n]E_4^3-720\tau(n)\bigr).
\]
The right side is an integer multiple of \(691\).
The Euclidean calculation in Theorem 5.1 gives
\(\gcd(65520,691)=1\), so divisibility of the left side forces
\(691\mid(\sigma_{11}(n)-\tau(n))\).
This is exactly the congruence. Both the integrality and the invertible factor are needed; reducing a rational coefficient of \(E_{12}\) directly would not be a valid step.

### Solution 4

Assume \(f\ne0\). It is holomorphic on \(\mathfrak H\) and at the cusp, so every order in its valence formula is nonnegative.
Dropping all terms other than the cusp gives
\(v_\infty(f)\le k/12\), contradicting the hypothesis.
Thus \(f=0\). In coefficient language, vanishing of the coefficients indexed
\(0,1,\ldots,\lfloor k/12\rfloor\) forces a nonzero form to have cusp order at least \(\lfloor k/12\rfloor+1>k/12\), and therefore forces the form to vanish.
Odd and negative weights already have zero space.

### Solution 5

If \(d=0\), the basis is empty. Otherwise \(k\) is even and nonnegative, with \(k\ne2\).
For \(j=0,\ldots,d-1\), put \(w_j=k-12j\).
Each \(w_j\) is either zero or an even integer at least four.
To check this last point, write \(k=12m+r\), where \(r\in\{0,2,4,6,8,10\}\).
If \(r\ne2\), then \(d=m+1\) and the smallest \(w_j\) is \(r\).
If \(r=2\), then \(d=m\) and the smallest is fourteen.
For \(w_j=0\), take \(a_j=b_j=0\). Otherwise take \(b_j=0\) when \(4\mid w_j\) and \(b_j=1\) when \(w_j\equiv2\pmod4\), with
\(a_j=(w_j-6b_j)/4\). This gives nonnegative integers satisfying
\(4a_j+6b_j=w_j\).

Define
\[
A_j=\Delta^jE_4^{a_j}E_6^{b_j}\in M_k.
\]
Every coefficient is an integer, because this is true of all three factors.
Also \(A_j=q^j+O(q^{j+1})\).
Their distinct cusp orders make the \(A_j\) linearly independent; there are \(d\) of them, so the dimension theorem makes them a basis.

Now work backwards. Set \(F_{d-1}=A_{d-1}\), and, for \(j=d-2,\ldots,0\), define
\[
F_j=A_j-\sum_{r=j+1}^{d-1}[q^r]A_j\,F_r.
\tag{8.1}
\]
Inductively \(F_r\) has coefficient one at \(q^r\) and zero at every other exponent below \(d\).
Thus (8.1) clears precisely the unwanted exponents \(j+1,\ldots,d-1\), leaving
\(F_j=q^j+O(q^d)\).
All multipliers and all previous coefficients are integers, so every \(F_j\) has an integral expansion.
This change of basis is triangular with diagonal entries one, hence invertible.
The first \(d\) coefficient map on \(M_k\) is consequently an isomorphism onto \(\mathbb C^d\). It proves uniqueness as well as existence of the normalized basis.
For \(k\ge4\), the forms \(F_1,\ldots,F_{d-1}\) form the corresponding cusp basis; for \(k=0\), there is just \(F_0=1\).

In weight twelve, \(d=2\), \(A_0=E_4^3\), \(A_1=\Delta\).
The construction gives
\[
F_1=\Delta,\qquad
F_0=E_4^3-720\Delta=1+196560q^2+16773120q^3+\cdots.
\]
For instance the \(q^2\) coefficient is \(179280-720(-24)=196560\).

In weight twenty-four, \(d=3\), take
\(A_0=E_4^6,\ A_1=\Delta E_4^3,\ A_2=\Delta^2\).
Their initial coefficients are
\[
A_0=1+1440q+876960q^2+292072320q^3+\cdots,
\]
\[
A_1=q+696q^2+162252q^3+\cdots,\qquad
A_2=q^2-48q^3+\cdots.
\]
Consequently
\[
\begin{aligned}
F_2&=\Delta^2=q^2-48q^3+\cdots,\\
F_1&=A_1-696F_2=q+195660q^3+\cdots,\\
F_0&=A_0-1440F_1-876960F_2
=1+52416000q^3+\cdots.
\end{aligned}
\]
Here \(162252+696\cdot48=195660\), and
\(292072320-1440\cdot195660+876960\cdot48=52416000\).
This explicitly checks the required first three coefficients and illustrates why no denominator enters the construction.

### Solution 6

An invariant meromorphic function descends through every quotient chart: at an elliptic point of order \(e\), its Laurent series in the rotation coordinate \(w\) has only exponents divisible by \(e\), so it is meromorphic in \(w^e\). At the cusp its meromorphic \(q\)-expansion supplies the extension.
Thus it gives a meromorphic function on \(X(1)\). Theorem 3.1 identifies \(X(1)\) with the sphere using \(t=j\).

Let the finite poles, expressed in this coordinate, be \(a_1,\ldots,a_s\), with principal parts
\[
P_\ell(t)=\sum_{r=1}^{m_\ell}c_{\ell,r}(t-a_\ell)^{-r}.
\]
Let the negative-power part at infinity, in \(u=1/t\), be
\(\sum_{r=1}^{m_\infty}b_r u^{-r}\), and put
\(Q(t)=\sum_{r=1}^{m_\infty}b_rt^r\).
Subtract \(Q+\sum_\ell P_\ell\) from the function.
Each \(P_\ell\) is holomorphic at infinity and at the other finite poles, and \(Q\) has no finite pole. Therefore this subtraction removes all principal parts without creating new poles.
The remainder is holomorphic on the compact sphere, hence constant \(c\), by Liouville's theorem as used in Theorem 3.1.
The explicit expression for the original modular function is
\[
f(z)=c+Q(j(z))+
\sum_{\ell=1}^s\sum_{r=1}^{m_\ell}
\frac{c_{\ell,r}}{(j(z)-a_\ell)^r}.
\]
The pole set is finite by compactness and meromorphy, so this is a rational expression. Conversely each such expression is invariant and meromorphic on the compactified quotient. This proves both inclusions of the function field.

## What this lesson does not prove

Every principal assertion in this lesson is proved, including the boundary contributions in the valence formula, algebraic independence, the product identity, the integral Victor Miller basis and the rational-function description.

The earlier local proof dependencies are the closed fundamental domain and elliptic stabilizers in The upper half-plane and the modular group, Theorem 3.2 and Proposition 3.3, and its generation result, Proposition 4.1; the quotient and cusp charts in Modular curves and their genus, Propositions 1.3 and 2.2; and the Eisenstein expansions and weight-two law in Modular forms, lattice functions and Eisenstein series, Theorem 4.2 and Theorem 5.2. Lemma 0.1 derives the argument principle from Cauchy's theorem. Liouville's theorem can also be reduced to Cauchy's formula: a bounded entire function satisfies \(|f'(z)|\le M/R\) on a circle of radius \(R\) about \(z\); letting \(R\to\infty\) makes \(f'=0\). Cauchy's theorem and formula, the identity and maximum principles and local holomorphic inversion are proved in lesson 01, Lemma 0.2 and its local inverse consequence. The real-integration and general dominated-integral foundations still listed in lesson 04 remain residual proof-closure gaps.

The multiplicativity of \(\tau\), its Hecke recurrences and bounds for its prime coefficients belong to later lessons; they are not used here.

## References

- **Stein author PDF.** W. Stein, *Modular Forms: A Computational Approach*, freely distributed PDF on the author's website, §§2.2–2.3: Theorem 2.11, Proposition 2.13, Theorem 2.14, Corollary 2.16 and Theorem 2.17. These numbers refer to the accessible file; its valence proof points outward, so our boundary proof is supplied locally. [Free author PDF](https://wstein.org/books/modform/stein-modform.pdf).
- **Voight open book.** J. Voight, *Quaternion Algebras*, freely distributed stable post-publication version 1.0.5 (10 January 2024), §40.3, especially Proposition 40.3.4 and Theorems 40.3.8 and 40.3.11. [Author's stable free PDF](https://jvoight.github.io/quat-book-v1.0.5.pdf).

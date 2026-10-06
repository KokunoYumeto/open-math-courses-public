# Theta series of lattices

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The exponent in this lesson is half the squared norm:
\[
q=e^{2\pi iz},\qquad
\theta_L(z)=\sum_{x\in L}q^{|x|^2/2}.
\tag{1.1}
\]
Thus a vector of squared norm \(2\), called a **root**, contributes to the coefficient of \(q\). We will turn an analytic transformation into a restriction on the rank, then use the small spaces of level-one forms to count vectors.

We use Theta functions and sums of squares for the real Gaussian transform and Poisson convention, Modular forms, lattice functions and Eisenstein series, Theorem 4.2, for normalized \(E_k\), and The valence formula and the ring of modular forms of level one, Theorems 2.1–2.3, for \(\Delta\) and dimensions.

## 1. Duality, volume and a concrete lattice

A full lattice in \(\mathbb R^n\) is \(L=B\mathbb Z^n\), where \(B\) is an invertible real matrix. We assume \(n>0\). Its covolume and dual are
\[
v(L)=|\det B|,\qquad
L^\vee=\{\xi:\xi\cdot L\subset\mathbb Z\}=B^{-t}\mathbb Z^n.
\tag{1.2}
\]
It is **integral** if all inner products of its vectors are integers, and **even** if \(|x|^2\in2\mathbb Z\) for every \(x\in L\). Evenness implies integrality, because
\[
x\cdot y=\frac{|x+y|^2-|x|^2-|y|^2}{2}\in\mathbb Z.
\]
We call an integral lattice **unimodular** when \(L=L^\vee\).

**Lemma 1.1.** For an integral lattice, unimodularity is equivalent to \(v(L)=1\), or to \(\det A=1\), where \(A=B^tB\) is its Gram matrix.

**Proof.** Integrality gives \(L\subset L^\vee\). Formula (1.2) gives \(v(L^\vee)=v(L)^{-1}\), so the index of this inclusion is
\[
[L^\vee:L]=\frac{v(L)}{v(L^\vee)}=v(L)^2=\det A.
\]
It is one exactly in the stated cases. \(\square\)

For \(m\) divisible by eight, set
\[
D_m=\{a\in\mathbb Z^m: \textstyle\sum_i a_i\text{ is even}\},\qquad
h_m=(1/2,\ldots,1/2),\qquad
D_m^+=D_m\cup(h_m+D_m).
\tag{1.3}
\]

**Proposition 1.2.** The lattice \(D_m^+\) is even and unimodular.

**Proof.** Since \(2h_m\in D_m\), the union is a group and contains \(D_m\) with index two. The latter has index two in \(\mathbb Z^m\); hence \(v(D_m)=2\) and \(v(D_m^+)=1\). For \(a,b\in D_m\), their inner product is integral, \(h_m\cdot a=\sum_i a_i/2\) is integral, and
\[
|h_m|^2=m/4\in2\mathbb Z.
\]
Also \(|a|^2\equiv\sum_i a_i\equiv0\pmod2\). It follows that every vector in either coset has even squared norm. Lemma 1.1 now gives self-duality. \(\square\)

We write \(E_8=D_8^+\). In rank sixteen, \(D_{16}^+\) is also denoted \(E_{16}\) in the literature. The coordinate construction (1.3) fixes which lattice this notation means.

## 2. Poisson summation and the branch of the transformation

The real Fourier convention is
\[
\widehat f(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\,dx.
\]
We use Poisson summation for a full lattice and a Schwartz function:
\[
\sum_{x\in L}f(x)=\frac1{v(L)}
\sum_{\xi\in L^\vee}\widehat f(\xi).
\tag{2.1}
\]
The quotient \(\mathbb R^n/L\) is compact. This hypothesis and the covolume factor are part of the formula. The integer-lattice formula, including absolute convergence and Fourier uniqueness in every dimension, was proved in Theta functions and sums of squares, Theorem 1.1, equation (1.3a). To deduce (2.1), put \(g(a)=f(Ba)\), which is Schwartz because \(B\) is invertible. A change of variables in the Fourier integral gives \(\widehat g(m)=v(L)^{-1}\widehat f(B^{-t}m)\). Applying that earlier proved formula to \(g\), and using \(B^{-t}\mathbb Z^n=L^\vee\), proves (2.1), with both sums absolutely convergent.

The Gaussian transform from the preceding lesson, multiplied over the coordinates, gives
\[
\widehat{e^{-\pi t|x|^2}}(\xi)
=t^{-n/2}e^{-\pi|\xi|^2/t}\qquad(t>0).
\tag{2.2}
\]
Absolute integrability justifies the product of the one-variable integrals.

**Theorem 2.1 (theta transformation).** For an even unimodular lattice of rank \(n\), the series (1.1) is holomorphic on \(\mathfrak H\), and
\[
\theta_L(z+1)=\theta_L(z),\qquad
\theta_L(-1/z)=(-iz)^{n/2}\theta_L(z).
\tag{2.3}
\]
Here \((-iz)^{n/2}=\exp((n/2)\operatorname{Log}(-iz))\), with the logarithm on the right half-plane that is real on positive real numbers.

**Proof.** There is \(c>0\) with \(|Ba|^2\ge c|a|^2\). On a compact subset with \(\operatorname{Im}z\ge y_0>0\), the summands in (1.1) are dominated by
\[
e^{-\pi cy_0|a|^2}\quad(a\in\mathbb Z^n),
\]
whose sum is a product of convergent one-variable sums. The series therefore converges locally uniformly and defines a holomorphic function. Each coefficient is finite: \(|Ba|^2\le R^2\) bounds every coordinate of \(a\).

Evenness gives period one. Applying (2.1) and (2.2), with \(v(L)=1\) and \(L^\vee=L\), gives
\[
\theta_L(it)=t^{-n/2}\theta_L(i/t).
\tag{2.4}
\]
This is the second identity in (2.3) on the imaginary axis. Both sides of that identity are holomorphic on \(\mathfrak H\); the prescribed logarithm is defined there because \(\operatorname{Re}(-iz)>0\). The identity theorem extends (2.4) to (2.3). \(\square\)

At this stage \(n/2\) has not been assumed integral. That is why the branch in Theorem 2.1 matters.

## 3. The rank is a multiple of eight

Let
\[
S=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},
\qquad T=\begin{pmatrix}1&1\\ 0&1\end{pmatrix}.
\]
The relation \((ST)^3=-I\) was established in the first lesson; the associated fractional linear transformation has cube equal to the identity.

**Theorem 3.1.** Every positive definite even unimodular lattice has rank divisible by eight.

**Proof.** Fix \(z\in\mathfrak H\) and put
\[
z_0=z,\qquad
z_1=-\frac1{z+1},\qquad
z_2=-\frac{z+1}{z}.
\]
These are successive images under \(ST\), and the next image is \(z\). By (2.3),
\[
\theta_L(z_{j+1})=a_j^{n/2}\theta_L(z_j),
\qquad a_j=-i(z_j+1).
\tag{3.1}
\]
Each \(a_j\) lies in the right half-plane. Direct multiplication gives
\[
a_0=-i(z+1),\qquad
a_1=-i\frac z{z+1},\qquad
a_2=\frac i z,\qquad
a_0a_1a_2=-i.
\]
Their arguments lie strictly between \(-\pi/2\) and \(\pi/2\). The sum of those arguments lies in \((-3\pi/2,3\pi/2)\) and is congruent to \(-\pi/2\) modulo \(2\pi\); it must be \(-\pi/2\). The product of their absolute values is one. Consequently the actual branches in (3.1) satisfy
\[
a_0^{n/2}a_1^{n/2}a_2^{n/2}
=\exp(-\pi in/4).
\tag{3.2}
\]
Iterating (3.1) therefore gives \(\theta_L(z)=e^{-\pi in/4}\theta_L(z)\). At \(z=it\), every summand is positive and the zero vector contributes one, so \(\theta_L(it)>0\). Thus \(e^{-\pi in/4}=1\), which means \(8\mid n\). \(\square\)

**Theorem 3.2 (level-one modularity).** If \(n=8r>0\), then
\[
\theta_L\in M_{4r}(SL_2(\mathbb Z)).
\tag{3.3}
\]

**Proof.** Set \(k=n/2=4r\). Now the branch in (2.3) becomes the integral power
\[
(-iz)^k=z^k.
\]
Thus \(\theta_L|_kS=\theta_L\) and \(\theta_L|_kT=\theta_L\). The first lesson, Proposition 4.1, proves that \(S,T\) generate \(SL_2(\mathbb Z)\); the integer-weight slash action then gives invariance under the whole group. The expansion
\[
\theta_L=1+\sum_{m\ge1}r_L(m)q^m,\qquad
r_L(m)=\#\{x\in L:|x|^2=2m\},
\tag{3.4}
\]
converges for \(|q|<1\), including at \(q=0\). There is one cusp orbit at level one, so this proves the cusp condition everywhere. \(\square\)

The count \(r_L(m)\) always refers to squared norm \(2m\). In particular \(r_L(1)\) is the number of roots.

## 4. Counts in ranks eight, sixteen and twenty-four

The normalized Eisenstein series have constant term one. Their relevant expansions are
\[
E_4=1+240\sum_{m\ge1}\sigma_3(m)q^m,\qquad
E_8=1+480\sum_{m\ge1}\sigma_7(m)q^m,
\tag{4.1}
\]
\[
E_{12}=1+\frac{65520}{691}\sum_{m\ge1}\sigma_{11}(m)q^m,
\qquad
\Delta=q-24q^2+252q^3+\cdots.
\tag{4.2}
\]
Here \(\sigma_j(m)=\sum_{d\mid m}d^j\). The coefficient \(65520/691\) follows from \(B_{12}=-691/2730\), computed in the fourth lesson, Section 8, Solution 4.

**Theorem 4.1.** In rank eight, \(\theta_L=E_4\). In rank sixteen, \(\theta_L=E_8=E_4^2\).

**Proof.** The fifth lesson, Theorem 2.2, gives \(\dim M_4=\dim M_8=1\). The modular forms supplied by Theorem 3.2 have constant term one, so (4.1) identifies them with the normalized Eisenstein series. The form \(E_4^2\) also belongs to \(M_8\) and has constant term one; hence it is \(E_8\). \(\square\)

In particular,
\[
r_{E_8}(m)=240\sigma_3(m),
\qquad
\theta_{E_8\oplus E_8}=\theta_{D_{16}^+}=E_4^2.
\tag{4.3}
\]
The direct-sum identity follows by multiplying the two absolutely convergent lattice sums.

**Theorem 4.2.** In rank twenty-four, let \(N_2(L)=r_L(1)\). Then
\[
\boxed{\theta_L=E_{12}
+\left(N_2(L)-\frac{65520}{691}\right)\Delta.}
\tag{4.4}
\]
Consequently the number of squared-norm-four vectors is
\[
r_L(2)=196560-24N_2(L).
\tag{4.5}
\]
For the Leech lattice, the minimum nonzero squared norm is four and there are \(196560\) vectors of that norm.

**Proof.** The fifth lesson gives \(S_{12}=\mathbb C\Delta\). Since \(\theta_L\) and \(E_{12}\) have constant term one, their difference is a multiple of \(\Delta\). Comparing the coefficient of \(q\) gives (4.4). Comparing that of \(q^2\) gives
\[
r_L(2)=\frac{65520}{691}(1+2^{11})
-24\left(N_2(L)-\frac{65520}{691}\right)
=\frac{65520}{691}\,2073-24N_2(L).
\]
Since \(2073=3\cdot691\), this is (4.5).

The freely accessible Chenevier–Lannes author manuscript, Section I.1 states the existence of a positive definite even unimodular rank-twenty-four lattice without roots, the Leech lattice. **Proof gap:** that existence has not yet been constructed locally or proved in an earlier programme lesson. The calculation is valid for every such lattice: \(N_2=0\) in (4.5) gives \(196560>0\) vectors of squared norm four, and evenness with no squared-norm-two vectors makes four the minimum. The coefficient calculation above is complete; identifying an existing lattice to which it applies still uses the unproved existence assertion. \(\square\)

For comparison, \(E_8^{\oplus3}\) has \(3\cdot240=720\) roots. Formula (4.5) gives \(179280\) squared-norm-four vectors. Multiplication of its theta series gives the same count:
\[
[q^2]E_4^3=3\cdot2160+3\cdot240^2=179280.
\]

## 5. Two complete examples

### 5.1. Counting vectors in \(E_8\)

The integer coset \(D_8\) has squared-norm-two vectors with two nonzero coordinates, each \(\pm1\). There are \(\binom82\,2^2=112\). In the half-integer coset, squared norm two forces every coordinate to be \(\pm1/2\). Writing the vector as \(h_8+a\), membership requires an even number of minus signs; there are \(2^7=128\). Thus \(E_8\) has \(240\) roots.

For squared norm four, an integer vector has either one coordinate \(\pm2\), or four coordinates \(\pm1\):
\[
2\cdot8+\binom84\,2^4=16+1120=1136.
\tag{5.1}
\]
All these vectors have even coordinate sum. A half-integer vector starts with squared norm two. Changing a coordinate's absolute value from \(1/2\) to \(3/2\) adds two, while changing it to \(5/2\) adds six. Exactly one coordinate therefore has absolute value \(3/2\). Choose its position and sign in \(8\cdot2\) ways. For each such choice, the parity of the sum of the eight underlying integers fixes one parity condition on the other seven signs, leaving \(2^6\) choices. This gives \(1024\) half-integer vectors, and
\[
1136+1024=2160=240(1+2^3).
\tag{5.2}
\]
These are exhaustive coordinate counts, independently consistent with (4.3). Solution 2 performs the analogous squared-norm-six count.

### 5.2. Equal theta series and different flat tori

The roots in \(E_8\oplus E_8\) lie in one summand or the other, since each nonzero summand has squared norm at least two. The half-integer coset of \(D_{16}^+\) has squared norm at least \(16/4=4\). Thus its roots are exactly
\[
\{\pm e_i\pm e_j:1\le i<j\le16\}.
\tag{5.3}
\]
Both lattices have \(480\) roots.

Consider the graph on a lattice's roots, joining distinct roots when their inner product is nonzero. For the roots \(\pm e_i\pm e_j\) in \(D_m\), \(m\ge3\), this graph is connected. Indeed two supports sharing one index have nonzero inner product; supports can be joined by successive pairs sharing one index. If two roots with the same support are orthogonal, a root using one of their indices and a third index joins them both. This also connects all sign choices.

The \(112\) integer roots of \(E_8\) therefore form a connected graph. Each half-integer root joins an integer root: choose two coordinates and give \(\pm e_i\pm e_j\) their matching signs, obtaining inner product one. The whole root graph of \(E_8\) is connected. Consequently \(E_8\oplus E_8\) has two connected components in its root graph, whereas \(D_{16}^+\) has one. An isometry preserves this graph, so
\[
E_8\oplus E_8\not\simeq D_{16}^+.
\tag{5.4}
\]

Their equal theta series nevertheless imply equal Laplace eigenvalues on the flat tori \(\mathbb R^{16}/L\). With the nonnegative convention \(\mathcal D=-\sum_j\partial_{x_j}^2\), each \(\xi\in L^\vee\) gives a periodic eigenfunction
\[
e_\xi(x)=e^{2\pi ix\cdot\xi},
\qquad
\mathcal D e_\xi=4\pi^2|\xi|^2e_\xi.
\tag{5.5}
\]
Here is why these functions account for all eigenspaces. In coordinates \(x=Bt\), every periodic function is a function on \(\mathbb R^n/\mathbb Z^n\), with integer Fourier frequencies. Fourier coefficients determine a continuous periodic function: convolve it with the product of the one-variable Fejér kernels
\[
K_M(u)=\frac1M\left|\sum_{j=0}^{M-1}e^{2\pi iju}\right|^2.
\]
Expanding the finite sum shows that \(K_M\) has integral one and is a trigonometric polynomial; it is nonnegative. The geometric-sum formula bounds it by \(1/(M\sin^2(\pi\delta))\) when the distance to an integer is at least \(\delta\). For the product kernel, the integral outside the cube where every coordinate has distance less than \(\delta\) is therefore at most \(n/(M\sin^2(\pi\delta))\). On that cube use uniform continuity, and on its complement use twice the function's supremum. This proves uniform convergence of the convolutions to the function. If every Fourier coefficient is zero, each convolution is zero, so the function is zero.

For a smooth Laplace eigenfunction of eigenvalue \(\lambda\), integration by parts on the periodic coordinate cube gives
\[
(\lambda-4\pi^2|\xi|^2)\widehat f(\xi)=0.
\]
Only finitely many \(\xi\) can satisfy \(4\pi^2|\xi|^2=\lambda\). Subtract their finite Fourier sum; the remainder has every coefficient zero and hence vanishes. Distinct frequencies are linearly independent: integrating their products over the periodic cube gives the usual orthogonality of integer exponentials. Thus, for the spectrum defined by smooth Laplace eigenfunctions, the eigenspace dimension is exactly the number of such dual vectors. Our lattices are self-dual, so (4.3) gives the same eigenvalues and multiplicities. The first two positive eigenvalues are \(8\pi^2\) and \(16\pi^2\), with multiplicities \(480\) and \(61920\).

To see that the flat tori are not isometric either, fix a point of the first torus. An isometry has an orthogonal derivative \(A\) there. A straight line in a local Euclidean chart is a geodesic. Its image is the geodesic with the image initial point and velocity; in the second torus that is the projected straight line with velocity \(Av\). Extending through successive charts, uniqueness of this straight geodesic gives
\[
f(p+v\bmod L_1)=f(p)+Av\bmod L_2.
\]
A vector \(v\) returns to \(p\) exactly when \(v\in L_1\), so this identity and its inverse give \(A L_1=L_2\), contradicting (5.4). This is the example introduced by [Milnor, freely accessible original article, *Eigenvalues of the Laplace operator on certain manifolds*, page 542](https://pmc.ncbi.nlm.nih.gov/articles/PMC300113/).

As a direct check on the second multiplicity, \(D_{16}\) contributes
\(32+16\binom{16}{4}=29152\) squared-norm-four vectors, while its half coset contributes \(2^{15}=32768\). Their sum is \(61920\). For the direct sum, the same count is \(2\cdot2160+240^2\).

## 6. General level and genus averages

### 6.1. The lattice's level and character

Let \(L\) be even, positive definite and of rank \(2k\), with integral Gram matrix \(A\) having even diagonal. Its **level** is the least positive \(N\) such that \(NA^{-1}\) is integral with even diagonal. Equivalently \(N|x|^2/2\) is an integer for every \(x\in L^\vee\). Set
\[
D=(-1)^k\det A,\qquad
\chi_D(d)=\left(\frac Dd\right)\quad((d,N)=1).
\tag{6.1}
\]

**Theorem 6.1 (stated).** The theta series satisfies
\[
\theta_L\in M_k(\Gamma_0(N),\chi_D).
\tag{6.2}
\]
The quadratic character in (6.1) is viewed modulo \(N\) and extended by zero on its nonunits. This includes holomorphy at every cusp. The exact references are [Voight, Theorem 40.4.4 and paragraph 40.4.5] and [Bruinier–Zuffetti, Theorem 2.7].

The level in this statement is defined by the lattice's dual quadratic form; an accidental enlargement of the theta series's symmetry group does not change that definition. For \(A=2I_2\), \(N=4\) and \(D=-4\), so (6.2) recovers \(\theta(z)^2\in M_1(\Gamma_0(4),\chi_{-4})\) from the preceding lesson. For the \(A_2\) Gram matrix
\[
A=\begin{pmatrix}2&-1\\ -1&2\end{pmatrix},
\qquad
A^{-1}=\frac13\begin{pmatrix}2&1\\ 1&2\end{pmatrix},
\]
the level is three and \(D=-3\); its theta series has weight one and character \(\chi_{-3}\).

### 6.2. The weighted average

Two integral lattices are in the same **genus** when their quadratic forms are isometric over \(\mathbb R\) and over \(\mathbb Z_p\) for every prime \(p\), including two. We prove the finiteness needed for the average before defining it.

**Lemma 6.3 (finiteness of a positive definite genus).** There are finitely many isometry classes of positive definite integral lattices of a fixed rank \(n\) and Gram determinant \(D>0\). Consequently every positive definite integral genus is finite.

**Proof.** We prove inductively that every such lattice has a basis whose lengths are bounded by a number depending only on \(n,D\). First obtain a short nonzero vector by an elementary volume argument. A cube of side \(r\), with \(r^n>v(L)=\sqrt D\), has two distinct points whose difference lies in \(L\): cut it by the finitely many translates of a half-open fundamental parallelepiped that it meets, then translate the pieces into one parallelepiped. If their images were disjoint, finite additivity of volume would bound the cube's volume by \(v(L)\), a contradiction. Thus a nonzero lattice vector has length less than \(\sqrt n\,r\). Taking \(r=2D^{1/(2n)}\), a shortest nonzero vector \(v\) has integer squared length
\(1\le a=|v|^2\le4nD^{1/n}\). Such a vector is primitive: a proper integer multiple of another lattice vector would not be shortest. A primitive vector extends to an integer basis by successive integer Euclidean row operations.

Project orthogonally to \(v^\perp\). The projection \(\pi L\) is a full lattice there, since a basis beginning with \(v\) projects its remaining basis vectors to a basis. The lattice \(\sqrt a\,\pi L\) is integral, because
\[
a\langle\pi x,\pi y\rangle
=a\langle x,y\rangle-\langle x,v\rangle\langle y,v\rangle\in\mathbb Z.
\]
Its Gram determinant is \(D'=a^{n-2}D\): the base-times-height formula gives \(v(\pi L)=v(L)/\sqrt a\), and scaling an \((n-1)\)-dimensional lattice by \(\sqrt a\) multiplies its squared covolume by \(a^{n-1}\). In rank one the basis length is \(\sqrt D\). For \(n\ge2\), the positive integer \(D'\) belongs to a finite list depending only on \(n,D\). The inductive basis bound for \(\sqrt a\,\pi L\) therefore bounds the projected basis lengths uniformly. Lift those basis vectors to \(L\), and subtract integer multiples of \(v\) to make each component along \(v\) have absolute length at most \(\sqrt a/2\). Their lengths are uniformly bounded. Together with \(v\) they form a basis: their projections generate \(\pi L\), and the kernel of projection on \(L\) is \(\mathbb Zv\), by primitivity. This completes the induction.

All entries of the Gram matrix in this basis are bounded, by the product of the two basis lengths, and are integers. There are therefore only finitely many possible Gram matrices, proving the first assertion. Lattices in one genus have the same rank and determinant: a \(\mathbb Z_p\)-isometry preserves the determinant's \(p\)-adic valuation, and positive integer determinants with equal valuations at every prime are equal. Thus the first assertion applies to a genus. \(\square\)

For representatives \(L_1,\ldots,L_s\) of the genus, define
\[
\operatorname{mass}(L)=\sum_{j=1}^s\frac1{|O(L_j)|},
\qquad
A_L(z)=\frac1{\operatorname{mass}(L)}
\sum_{j=1}^s\frac{\theta_{L_j}(z)}{|O(L_j)|}.
\tag{6.3}
\]
The group \(O(L_j)\) is finite: the images of a fixed basis lie in finite fixed-norm shells and determine the isometry.

**Theorem 6.2 (Siegel–Weil, stated in the convergent range).** For an even positive definite lattice of rank \(2k>4\), \(A_L\) is its genus Eisenstein series, with constant term one, in \(M_k(\Gamma_0(N),\chi_D)\). In the even unimodular case it is exactly \(E_k\). The general assertion is [Bruinier–Zuffetti, Corollary 3.5]; the unimodular assertion is their Theorem 2.9. Their genus Eisenstein series is the zero component of the Eisenstein series for the discriminant representation of \(L^\vee/L\).

Thus it is the inverse-automorphism weighted average whose cuspidal part disappears. Individual theta series can have a cuspidal part, as (4.4) shows. The scalar mass in (6.3) is the subject of the mass formula; the theta-average identity contains representation counts as its positive coefficients. We do not need a numerical mass formula for any count proved above.

### 6.3. Kneser neighbours

For an even unimodular lattice \(L\), a **\(p\)-neighbour** \(L'\) in the same rational Euclidean space is another even unimodular lattice satisfying
\[
[L:L\cap L']=[L':L\cap L']=p.
\tag{6.4}
\]
An explicit construction is useful. Choose \(u\in L\) nonzero modulo \(p\) with \(Q(u)=|u|^2/2\equiv0\pmod p\). Unimodularity makes the inner-product pairing nondegenerate modulo \(p\), so choose \(v\in L\) with \(u\cdot v\equiv1\pmod p\). Put
\[
\widetilde u=u-Q(u)v,\qquad
M=\{x\in L:u\cdot x\equiv0\pmod p\},\qquad
L'=M+\mathbb Z\,\frac{\widetilde u}{p}.
\tag{6.5}
\]
Indeed,
\[
Q(\widetilde u)=Q(u)(1-u\cdot v)+Q(u)^2Q(v)
\equiv0\pmod{p^2}.
\]
Also \(\widetilde u\equiv u\pmod p\), and \(\widetilde u\in M\). The pairing of \(\widetilde u/p\) with \(M\) is integral, and its half-norm is integral; hence \(L'\) is even. The nonzero linear functional \(u\cdot(-)\bmod p\) makes the index of \(M\) in \(L\) equal to \(p\). Moreover \(p(\widetilde u/p)=\widetilde u\in M\), while \(j\widetilde u/p\in L\) forces \(p\mid j\), since \(\widetilde u\) is nonzero modulo \(pL\). Hence \([L':M]=p\) and \(L\cap L'=M\). Thus \(v(L')=1\), proving unimodularity. The two indices prove (6.4). This works for \(p=2\) as well, with the quadratic condition on \(Q\).

There are finitely many such neighbours. Their intersections are among the finitely many index-\(p\) sublattices \(K\) of \(L\), and every neighbour lies in \(p^{-1}L\). For each \(K\), the finite group \(p^{-1}L/K\) has only finitely many subgroups, so only finitely many intermediate lattices can occur. The lattice operator
\[
\mathcal N_p[L]=\sum_{L'\text{ a }p\text{-neighbour of }L}[L']
\tag{6.6}
\]
acts on the vector space of isometry classes. It is an orthogonal-group Hecke operator; its relation to modular Hecke operators is expressed by the Eichler commutation relations in the freely accessible Chenevier–Lannes author manuscript, Proposition V.1.1. That commutation assertion remains a proof gap here.

Here is the elementary symmetry behind the weights in (6.3). Write \(N_p(L,M)\) for the number of neighbours of \(L\) isometric to \(M\). Work in a common rational quadratic space when the classes are rationally isometric; if they are not, both neighbour counts are zero. Count rational isometries carrying \(M\) onto such a neighbour. There are \(N_p(L,M)|O(M)|\); taking inverses gives \(N_p(M,L)|O(L)|\). Consequently
\[
\frac{N_p(L,M)}{|O(L)|}
=\frac{N_p(M,L)}{|O(M)|}.
\tag{6.7}
\]
This proves that (6.6) is self-adjoint for the inner product
\(([L],[M])=|O(L)|\delta_{[L],[M]}\). The full theta commutation and genus-average theorems are stated inputs, rather than consequences of self-adjointness alone.

## 7. Exercises

1. **Easy.** Show that \(D_8^+\) is even and unimodular, using its two cosets and their covolumes.
2. **Medium.** Count the squared-norm-four and squared-norm-six vectors of \(E_8\) directly, and compare the totals with its theta series.
3. **Medium.** Derive \(196560\) from the rank-twenty-four formula. Check the same coefficient computation for \(E_8^{\oplus3}\).
4. **Hard.** Prove rank divisibility by eight using \((ST)^3=-I\), while keeping the analytic branch correct before integrality of the weight is known.

## 8. Full solutions

### Solution 1

Let \(h=(1/2,\ldots,1/2)\). The set \(D_8\cup(h+D_8)\) is a lattice because \(2h=(1,\ldots,1)\in D_8\). Its two cosets give index two over \(D_8\), which itself has index two in \(\mathbb Z^8\), so its covolume is one. If \(a\in D_8\), then \(|a|^2\) is even, \(h\cdot a=\sum a_i/2\) is integral, and \(|h|^2=2\). Therefore
\[
|h+a|^2=2+2h\cdot a+|a|^2\in2\mathbb Z.
\]
Polarization makes the lattice integral. Its dual contains it and has the same covolume one, so the inclusion has index one. It is even and self-dual, as required.

### Solution 2

For squared norm four, the integer patterns are \((2,0^7)\) and \((1^4,0^4)\), with arbitrary signs on the nonzero coordinates. Their counts are \(16\) and \(\binom84\,16=1120\). In the half coset, precisely one coordinate has absolute value \(3/2\) and seven have absolute value \(1/2\). Its position, sign and the remaining parity constraint give \(8\cdot2\cdot2^6=1024\). The total is \(2160\).

For squared norm six, the integer patterns are \((2,1,1,0^5)\) and \((1^6,0^2)\). A coordinate of absolute value three would already have squared norm nine, and two of absolute value two would have squared norm eight, so these are all possibilities. The counts are
\[
8\binom72\,2^3=1344,\qquad
\binom86\,2^6=1792,
\]
giving \(3136\). The half coset starts at squared norm two. Exactly two coordinates must have absolute value \(3/2\); a \(5/2\) coordinate would raise the norm to at least eight. Choose the two positions, their signs, and the six remaining signs subject to the one parity condition:
\[
\binom82\,2^2\,2^5=3584.
\]
The total is \(3136+3584=6720\). In either parity count, writing each coordinate as \(a_i+1/2\) makes the condition \(\sum a_i\equiv0\pmod2\); fixing all but one remaining sign leaves exactly one allowed last sign. Finally,
\[
240\sigma_3(2)=240(1+8)=2160,\qquad
240\sigma_3(3)=240(1+27)=6720,
\]
so both direct counts agree with (4.3).

### Solution 3

The coefficient of \(q^2\) in \(E_{12}\) is \((65520/691)(1+2^{11})\), and that in \(\Delta\) is \(-24\). The coefficient of \(q\) in (4.4) sets the multiplier of \(\Delta\) to \(N_2-65520/691\). Therefore
\[
r_L(2)=\frac{65520}{691}(2049+24)-24N_2
=196560-24N_2.
\]
For the Leech lattice \(N_2=0\), giving \(196560\). This positive count, with evenness and no roots, proves that the counted vectors are precisely its minimal vectors.

For \(E_8^{\oplus3}\), \(N_2=720\), and the formula gives \(196560-17280=179280\). Directly, a squared-norm-four vector has either one norm-four component, giving \(3\cdot2160\), or two root components, giving \(\binom32\,240^2\). The sum is \(179280\).

### Solution 4

Write \(w_0=z\), \(w_1=-1/(z+1)\), \(w_2=-(z+1)/z\), and \(a_j=-i(w_j+1)\). The transformations from Theorem 2.1 give
\[
\theta_L(z)=\prod_{j=0}^2 a_j^{n/2}\,\theta_L(z).
\]
The three \(a_j\) are in the right half-plane and have product \(-i\). With their arguments chosen in \((-\pi/2,\pi/2)\), their sum must be \(-\pi/2\), because it lies strictly between \(-3\pi/2\) and \(3\pi/2\). The sum of the logarithms of their absolute values is zero. Thus the product of the prescribed powers is \(e^{-\pi in/4}\), even when \(n/2\) has not yet been shown integral. Taking \(z=it\), where \(\theta_L(it)>0\), gives \(e^{-\pi in/4}=1\), hence \(8\mid n\). Only after this step may one replace the branch in (2.3) by \(z^{n/2}\) for ordinary level-one modularity.

## What this lesson does not prove

- **Real Fourier analysis.** The Schwartz Poisson formula on \(\mathbb Z^n\), with its convergence and Fourier uniqueness, and the one-variable Gaussian transform are proved in the preceding lesson, Theorem 1.1, equations (1.3a) and (1.4). The lattice covolume conversion is proved above in (1.2), (2.1). The compact quotient is \(\mathbb R^n/L\).
- **Earlier modular-form results.** The Gaussian/theta conventions, integer-weight slash action, generation by \(S,T\), normalized Eisenstein expansions and level-one dimension/discriminant formulas are imported from the lessons and exact locators named above.
- **Complex identity theorem.** The extension from the imaginary axis in Theorem 2.1 uses the proof in the first lesson, Lemma 0.2. The lattice Poisson step uses the exact earlier proof in the preceding theta lesson, Theorem 1.1; the change of covolume is proved here.
- **Existence of the Leech lattice: proof gap.** The rootless even unimodular rank-twenty-four existence assertion is stated in the free Chenevier–Lannes author manuscript, Section I.1. Its local construction or an exact earlier programme proof is still missing. No classification or uniqueness theorem is needed for the conditional norm-four count.
- **General modularity and averaging: proof gaps.** Theorems 6.1–6.2 and the full Eichler commutation relations still require local proofs or verified earlier programme proofs. Their freely accessible source statements are Voight Theorem 40.4.4 and paragraph 40.4.5; Bruinier–Zuffetti Theorem 2.9 and Corollary 3.5; and the Chenevier–Lannes author manuscript, Proposition V.1.1. These source statements do not meet that proof requirement on their own. Genus finiteness is proved locally in Lemma 6.3. The explicit neighbour construction and weighted symmetry (6.5)–(6.7) are proved here; they do not prove the general theta commutation or genus-average theorem, or the complete local classification establishing genus membership of every even unimodular neighbour.

## References

- G. Chenevier and J. Lannes, *Formes automorphes et voisins de Kneser des réseaux de Niemeier*, author manuscript, 2015, Sections II.3, III.1–III.3, IV.5 and V.1–V.3. [Freely accessible arXiv manuscript, version two](https://arxiv.org/abs/1409.7616v2). The locators in this lesson refer to this manuscript.
- J. Voight, *Quaternion Algebras*, Springer, 2021, Section 40.4, especially Theorem 40.4.4 and paragraph 40.4.5. [Author's open book](https://jvoight.github.io/quat-book.pdf).
- J. H. Bruinier and R. Zuffetti, *The Siegel–Weil formula in geometry and arithmetic*, 2026, Theorems 2.7 and 2.9, Corollary 3.5. [Author manuscript, version one](https://arxiv.org/abs/2607.06285v1).
- J. Milnor, *Eigenvalues of the Laplace operator on certain manifolds*, *Proceedings of the National Academy of Sciences* 51 (1964), 542. [Freely accessible original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC300113/).
- J. Lebl, *Guide to Cultivating Complex Analysis*, version 1.9, Theorem 2.4.7. [Author's open text](https://www.jirka.org/ca/).

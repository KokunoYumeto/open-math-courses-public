# Differences of a walk and separating products

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the two geometric facts behind the entropy estimates of the Gaussian moat course. First, a stretch of \(n\) steps of a walk with bounded steps has many distinct differences \(z_s-z_t\): at least a constant times the area of the rectangle spanned by its diameter and its width. The proof shows that the differences, taken modulo a lattice of that area, come close to every point; it uses Brouwer's fixed-point theorem. Second, for a product of randomly chosen conjugate factors of many split primes, a thin rectangle centred at the origin almost never contains a nonzero multiple of the product. The proof combines the determinant identity for multiples of a Gaussian integer, Hoeffding's inequality along a fixed line, and the growth of neighbourhoods in the discrete cube. Together the two facts show that reduction modulo such a product is injective on all differences of a stretch.

We use the arithmetic of [Walks through Gaussian primes](walks-through-gaussian-primes.md), the inequalities of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md), the entropy facts of [Entropy of finite random variables](entropy-of-finite-random-variables.md), and Brouwer's fixed-point theorem from the core course [Algebraic Topology (D60)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), Lecture 30, Theorem 30.1: every continuous map of a closed disk in the plane to itself has a fixed point.

Basic references are [OpenAI-moat] and [Hatcher].

## 1. Walks and their displacements

Throughout, \(D\ge1\) and \(z_0,z_1,z_2,\dots\) is a fixed infinite \(D\)-walk: a sequence of distinct Gaussian integers with \(|z_{t+1}-z_t|\le D\). No congruence condition is assumed in this lesson. For integers \(t\ge0\) and \(n\ge1\), the **stretch** of \(n\) steps starting at time \(t\) is the set

\[
E=\{z_t,z_{t+1},\dots,z_{t+n}\}.
\]

It has \(n+1\) elements, since the points of a walk are distinct, and any two of its points are at distance at most \(Dn\).

A **random time** is a random variable with values in the nonnegative integers that takes finitely many values. The walk itself is never random: for a random time \(\tau\), the point \(z_\tau\) is a finite random variable.

**Lemma 1.1** (lattice points in a disk). For \(\rho\ge0\), the number of \(v\in\mathbb Z[i]\) with \(|v|\le\rho\) is at most \(\pi(\rho+1)^2\).

**Proof.** The closed unit squares centred at these lattice points have disjoint interiors and lie in the disk of radius \(\rho+\sqrt2/2\). Compare areas. \(\square\)

**Lemma 1.2** (displacement entropy). Let \(T_0,T_1\) be random times with \(|T_1-T_0|\le n\) almost surely. Then

\[
H(z_{T_1}-z_{T_0})\le2\log(n+1)+\log(\pi D^2).
\]

The same bound holds for the conditional entropy given any random variable. Moreover, if \(\Phi\) is a homomorphism from \(\mathbb Z[i]\) to a finite abelian group, then

\[
H(\Phi(z_{T_1}))\ge H(\Phi(z_{T_0}))-H(z_{T_1}-z_{T_0}).
\]

**Proof.** The displacement has length at most \(Dn\), so it takes at most \(\pi(Dn+1)^2\le\pi D^2(n+1)^2\) values (Lemma 1.1 and \(D\ge1\)); apply Corollary 1.3 of the entropy lesson, conditionally if needed. For the last claim, \(\Phi(z_{T_0})=\Phi(z_{T_1})-\Phi(z_{T_1}-z_{T_0})\) is determined by \(\Phi(z_{T_1})\) and the displacement, so Corollary 2.4(2) of [Entropy of finite random variables](entropy-of-finite-random-variables.md) applies. \(\square\)

## 2. Many differences

Let \(E\) be a finite set of points in the plane with at least two elements. Its **diameter** \(R\) is the largest distance between two of its points; choose points \(p_0,p_1\in E\) with \(|p_1-p_0|=R\). Let \(W'\) be the largest distance from a point of \(E\) to the line through \(p_0\) and \(p_1\), and put \(W=\max\{1,W'\}\).

**Lemma 2.1** (the diameter rectangle). Every point of \(E\) projects orthogonally onto the segment from \(p_0\) to \(p_1\). Hence, in orthonormal coordinates with origin \(p_0\) and first axis along \(p_1-p_0\), the set \(E\) lies in the rectangle \([0,R]\times[-W,W]\). Moreover \(W'\le R\).

**Proof.** If the projection of \(x\in E\) fell beyond \(p_1\), then \(|x-p_0|\) would exceed the distance from \(p_0\) to that projection, which exceeds \(R\); similarly beyond \(p_0\). Every point of \(E\) is within distance \(R\) of \(p_0\), which lies on the line, so \(W'\le R\). \(\square\)

**Theorem 2.2** (many differences). Let \(E\) be a stretch of \(n\ge1\) steps of the walk, and let \(R\), \(W\) be as above, \(A=RW\). Then

\[
\frac\pi{24}\,n\le A\le D^2n^2\qquad\text{and}\qquad |E-E|\ge\frac{A}{\pi D^2},
\]

where \(E-E=\{x-y:x,y\in E\}\).

**Proof.** *Size of \(A\).* Distinct lattice points are at distance at least \(1\), so the open disks of radius \(\frac12\) around the \(n+1\) points of \(E\) are disjoint. By Lemma 2.1 they lie in a rectangle with sides \(R+1\) and \(2W+1\), whose area is at most \(2R\cdot3W=6A\), because \(R,W\ge1\). So \((n+1)\pi/4\le6A\). Also \(R\le Dn\), and \(W\le\max\{1,R\}\le Dn\), so \(A\le D^2n^2\).

*A thin stretch.* If \(W'\le1\), then \(W=1\), \(A=R\le Dn\), and \(E-E\supseteq E-z_t\) has at least \(n+1>A/D\ge A/(\pi D^2)\) elements.

*The general case.* Suppose \(W'>1\), and choose \(p_2\in E\) at distance \(W'=W\) from the line through \(p_0,p_1\). Put \(a=p_1-p_0\) and \(b=p_2-p_0\). The parallelogram spanned by \(a\) and \(b\) has base \(R\) and height \(W\), so \(|\det(a,b)|=A>0\), and \(\Lambda=\mathbb Za+\mathbb Zb\) is a lattice in the plane.

Join the points of the stretch by straight segments in their order. Each point of the resulting polygonal path lies on a segment of length at most \(D\) whose endpoints are in \(E\), so it is within distance \(D/2\) of a point of \(E\). Let \(\alpha:[0,1]\to\mathbb R^2\) be a parametrization of the part of this path between \(p_0\) and \(p_1\), running from \(p_0\) to \(p_1\), and let \(\gamma:[0,1]\to\mathbb R^2\) run along the path from \(p_0\) to \(p_2\). Define

\[
F(s,u)=\alpha(s)-\gamma(u)\qquad\bigl((s,u)\in[0,1]^2\bigr).
\]

Then \(F(1,u)=F(0,u)+a\) and \(F(s,1)=F(s,0)-b\), because \(\alpha(1)-\alpha(0)=a\) and \(\gamma(1)-\gamma(0)=b\). Extend \(F\) to \(\widetilde F:\mathbb R^2\to\mathbb R^2\) by

\[
\widetilde F(s+m,u+l)=F(s,u)+ma-lb\qquad\bigl((s,u)\in[0,1]^2,\ m,l\in\mathbb Z\bigr).
\]

The two relations make this consistent where unit squares meet, and \(\widetilde F\) is continuous, because it is continuous on each closed unit square and these squares form a locally finite closed cover of the plane. Let \(M(s,u)=sa-ub\); this linear map has determinant \(-\det(a,b)\ne0\). The difference \(G=\widetilde F-M\) satisfies \(G(s+m,u+l)=G(s,u)\) for integers \(m,l\), so it is bounded, say \(|G|\le\kappa\).

We claim that \(\widetilde F\) is onto. Given \(y\in\mathbb R^2\), the continuous map \(\varphi(x)=M^{-1}(y-G(x))\) takes values in the closed disk of radius \(\rho=\|M^{-1}\|(|y|+\kappa)\) about \(0\), so it maps that disk to itself. By Brouwer's fixed-point theorem, \(\varphi(x)=x\) for some \(x\), that is, \(Mx=y-G(x)\), or \(\widetilde F(x)=y\).

Since \(\widetilde F(\mathbb R^2)=F([0,1]^2)+\Lambda\), every \(y\in\mathbb R^2\) has the form \(\alpha(s)-\gamma(u)+\lambda\) with \(\lambda\in\Lambda\). Choosing points \(e,e'\in E\) within distance \(D/2\) of \(\alpha(s)\) and \(\gamma(u)\), we get

\[
\mathbb R^2=\bigcup_{d\in E-E}\bigl(d+\Lambda+\overline B(0,D)\bigr),
\]

where \(\overline B(0,D)\) is the closed disk of radius \(D\) about \(0\).

*Counting by area.* The half-open parallelogram \(\Pi=\{xa+yb:0\le x,y<1\}\) has area \(A\), and its translates \(\Pi-\lambda\), \(\lambda\in\Lambda\), partition the plane: a point \(xa+yb\) lies in \(\Pi-\lambda\) exactly for \(\lambda=-\lfloor x\rfloor a-\lfloor y\rfloor b\). For each \(d\in E-E\),

\[
\operatorname{area}\bigl((d+\Lambda+\overline B(0,D))\cap\Pi\bigr)
\le\sum_{\lambda\in\Lambda}\operatorname{area}\bigl((d+\overline B(0,D))\cap(\Pi-\lambda)\bigr)
=\operatorname{area}\bigl(d+\overline B(0,D)\bigr)=\pi D^2,
\]

where we translated the piece \((d+\lambda+\overline B(0,D))\cap\Pi\) by \(-\lambda\). Since the sets on the left cover \(\Pi\), we obtain \(A\le|E-E|\,\pi D^2\). \(\square\)

The map \(\widetilde F\) descends to a map of tori \(\mathbb R^2/\mathbb Z^2\to\mathbb R^2/\Lambda\) of degree \(\pm1\), and the surjectivity proved above is an instance of the fact that a map of nonzero degree is onto; compare the discussion of degree in [Hatcher, Section 2.2]. The argument with Brouwer's theorem avoids homology.

## 3. Randomly signed products avoid thin rectangles

Let \(p_1,\dots,p_r\) be distinct rational primes congruent to \(1\) modulo \(4\), all in an interval \([T,2T]\) with \(T\ge5\), and put \(P=p_1\cdots p_r\). For each \(j\) fix the two conjugate factors \(\pi_{j,0}\) and \(\pi_{j,1}=\bar\pi_{j,0}\) of \(p_j\) (Proposition 2.3 of [Walks through Gaussian primes](walks-through-gaussian-primes.md)). A **sign vector** \(\sigma\in\{0,1\}^r\) selects one factor over each prime, and we put

\[
\Pi_\sigma=\prod_{j=1}^r\pi_{j,\sigma_j},\qquad N(\Pi_\sigma)=P.
\]

A **rectangle** below is a closed rectangle centred at \(0\), in any orientation, with half side lengths \(R_1\ge W_1\ge1\). A **witness** for \(\sigma\) in such a rectangle \(\mathcal Q\) is a nonzero element of \(\mathcal Q\cap\Pi_\sigma\mathbb Z[i]\), and \(\sigma\) is **bad** if it has a witness.

**Theorem 3.1** (signed products avoid thin rectangles). Let \(0<d<\frac14\) with \(d^3r\ge2\), and let \(\mathcal Q\) be a rectangle with \(R_1W_1\le P^{1-d}\). For a uniformly random sign vector,

\[
\mathbb P(\sigma\text{ is bad})\le\exp\Bigl(-\frac{d^3r}{640\log2}\Bigr).
\]

**Proof.** Note that \(dr=d^3r/d^2\ge32\).

*Step 1: nearby bad vectors have collinear witnesses.* Let \(\sigma,\sigma'\) be bad, with witnesses \(w,w'\), and suppose they differ in \(m\le dr/4\) coordinates. The product \(c\) of the factors \(\pi_{j,\sigma_j}\) over the coordinates where \(\sigma_j=\sigma'_j\) divides both \(\Pi_\sigma\) and \(\Pi_{\sigma'}\), hence \(w\) and \(w'\), and \(N(c)\ge P/(2T)^m\). By Lemma 2.5 of [Walks through Gaussian primes](walks-through-gaussian-primes.md), \(\det(w,w')\) is an integer multiple of \(N(c)\). In coordinates along the axes of \(\mathcal Q\), both vectors have first coordinate at most \(R_1\) and second at most \(W_1\) in absolute value, so \(|\det(w,w')|\le2R_1W_1\le2P^{1-d}\). If the determinant were nonzero, then \(P/(2T)^m\le2P^{1-d}\), so that

\[
dr\log T\le d\log P\le\log2+m\log(2T)\le\log2+\frac{dr}4\bigl(\log2+\log T\bigr).
\]

This gives \(dr\bigl(\tfrac34\log T-\tfrac14\log2\bigr)\le\log2\); but \(\tfrac34\log5-\tfrac14\log2>1\) and \(dr\ge32\). Hence \(\det(w,w')=0\): the witnesses lie on a common line through \(0\). Taking \(\sigma'=\sigma\), all witnesses of a bad vector lie on one line, which we call its **witness line** \(\ell(\sigma)\).

*Step 2: a fixed line is unlikely.* Let \(\ell\) be a line through \(0\) containing a nonzero lattice point. It contains a **primitive** lattice point \(v=v_1+iv_2\), one with \(\gcd(v_1,v_2)=1\), and the lattice points of \(\ell\) are exactly the integer multiples \(kv\): if \(xv\in\mathbb Z^2\) with \(x\) real, write \(1=\alpha v_1+\beta v_2\) with integers \(\alpha,\beta\); then \(x=\alpha xv_1+\beta xv_2\in\mathbb Z\).

Over each \(p_j\), at most one of the two factors divides \(v\): if both did, \(p_j\) would divide both coordinates of \(v\), by Proposition 2.4(3) of the first lesson. Let \(J\) be the set of \(j\) for which one factor divides \(v\), and \(\varepsilon_j\) its index. The factors \(\pi_{j,\varepsilon_j}\), \(j\in J\), have distinct norms, so their product divides \(v\) (Proposition 2.4(4) there), and \(\prod_{j\in J}p_j\le N(v)=|v|^2\).

Suppose \(kv\), with \(k\in\mathbb Z\setminus\{0\}\), is a multiple of \(\Pi_\sigma\). If \(\pi_{j,\sigma_j}\nmid v\), then the prime \(\pi_{j,\sigma_j}\) divides \(k\), so \(p_j\mid k\) by Proposition 2.4(1) of the first lesson. The coordinates with \(\pi_{j,\sigma_j}\mid v\) are those with \(j\in J\) and \(\sigma_j=\varepsilon_j\). Put

\[
X_j=\begin{cases}\log p_j&\text{if }j\in J\text{ and }\sigma_j=\varepsilon_j,\\ 0&\text{otherwise,}\end{cases}
\qquad P_\sigma(v)=\exp\Bigl(\sum_jX_j\Bigr).
\]

Then \(|k|\ge P/P_\sigma(v)\), so \(|kv|\ge|v|P/P_\sigma(v)\). A point of \(\mathcal Q\) has length at most \(\sqrt{R_1^2+W_1^2}\le\sqrt2R_1\le\sqrt2P^{1-d}\), using \(R_1\le R_1W_1\). Hence a witness on \(\ell\) exists only if

\[
\sum_jX_j\ge\log|v|+d\log P-\tfrac12\log2.
\]

The \(X_j\) are independent, with values in \([0,\log(2T)]\), and \(\mathbb E\sum_jX_j=\frac12\sum_{j\in J}\log p_j\le\log|v|\). The excess required is \(t=d\log P-\frac12\log2\ge dr\log T-\frac12\log2\ge\frac12dr\log T\). Hoeffding's inequality (Theorem 2.2 of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md)) gives

\[
\mathbb P(\text{a witness lies on }\ell)\le\exp\Bigl(-\frac{2t^2}{r\log^2(2T)}\Bigr)\le\exp\Bigl(-\frac{d^2r}2\Bigl(\frac{\log T}{\log2T}\Bigr)^2\Bigr)\le e^{-d^2r/8},
\]

since \(\log T\ge\frac12\log(2T)\) for \(T\ge2\).

*Step 3: classes of lines.* The rectangle contains finitely many lattice points, so only finitely many lines \(\ell_1,\dots,\ell_m\) occur as witness lines. Let \(S_l\) be the set of bad sign vectors with witness line \(\ell_l\). These sets partition the bad vectors, each has \(|S_l|\le\mu2^r\) with \(\mu=e^{-d^2r/8}\) by Step 2, and vectors from different sets differ in more than \(dr/4\) coordinates by Step 1. Let \(h=\lfloor dr/10\rfloor\); then \(2h<dr/4\), and \(h\ge dr/20\) because \(dr\ge20\). Apply Corollary 4.4 of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md) with \(\theta=e^{-d^2r/16}\). Here \(\log_2(1/\theta)/r=d^2/(16\log2)\le1\), and \(\log(1+x)\ge x/2\) for \(0\le x\le1\), so

\[
\Bigl(1+\frac{\log_2(1/\theta)}r\Bigr)^h\ge\exp\Bigl(\frac{hd^2}{32\log2}\Bigr)\ge\exp\Bigl(\frac{d^3r}{640\log2}\Bigr),
\qquad \frac\theta\mu=e^{d^2r/16}\ge\exp\Bigl(\frac{d^3r}{640\log2}\Bigr).
\]

The total number of bad vectors is therefore at most \(2^r\exp\bigl(-d^3r/(640\log2)\bigr)\). \(\square\)

**Corollary 3.2** (separating a finite set). Let \(F\subset\mathbb Z[i]\) be finite, and suppose that \(F-F\) is contained in a rectangle \(\mathcal Q\) as in Theorem 3.1. Then, with probability at least \(1-\exp\bigl(-d^3r/(640\log2)\bigr)\) over the sign vector, the reduction

\[
z\longmapsto\bigl(z\bmod\pi_{j,\sigma_j}\bigr)_{j=1,\dots,r}
\]

is injective on \(F\).

**Proof.** If two distinct points of \(F\) have the same reductions, their difference is a nonzero element of \(\mathcal Q\) divisible by every \(\pi_{j,\sigma_j}\), hence by \(\Pi_\sigma\) (Proposition 2.4(4) of the first lesson), so \(\sigma\) is bad. \(\square\)

**Corollary 3.3** (separating the differences of a stretch). Let \(E\) be a stretch of the walk with \(A=RW\) as in Theorem 2.2. If \(16A\le P^{1-d}\) and \(d,r\) are as in Theorem 3.1, then with probability at least \(1-\exp\bigl(-d^3r/(640\log2)\bigr)\) the reduction modulo the selected factors is injective on \(E-E\).

**Proof.** In the coordinates of Lemma 2.1, \(E\subseteq[0,R]\times[-W,W]\), so \(E-E\subseteq[-R,R]\times[-2W,2W]\) and \((E-E)-(E-E)\subseteq[-4R,4R]\times[-4W,4W]\). This rectangle has \(4R\ge4W\ge1\) and \(4R\cdot4W=16A\). Apply Corollary 3.2 to \(F=E-E\). \(\square\)

The exponent \(1-d\) cannot be raised to \(1\) or beyond: a rectangle with \(R_1W_1>P\) has area \(4R_1W_1\) larger than four times the covolume \(P\) of the lattice \(\Pi_\sigma\mathbb Z[i]\), so by Minkowski's theorem it contains a nonzero multiple of \(\Pi_\sigma\) for every sign vector (Exercise 4.4).

## 4. Exercises

**Exercise 4.1 (easy).** For the walk \(z_t=t\) on the real axis (with \(D=1\)), compute \(R\), \(W\), \(A\) and \(|E-E|\) for the stretch of \(n\) steps starting at \(0\), and compare with Theorem 2.2.

**Exercise 4.2 (medium).** Let \(m\ge2\), and let a stretch run row by row through the \(m^2\) points of the square \(\{0,\dots,m-1\}^2\), reversing direction on alternate rows (so all steps have length \(1\)). Show that \(|E-E|=(2m-1)^2\), and that \(A\) lies between \(m^2/4\) and \(2m^2\).

**Exercise 4.3 (medium).** Let \(v=v_1+iv_2\) be primitive. Show that the number of lattice points of the line \(\mathbb Rv\) in a disk of radius \(\rho\) about \(0\) is \(2\lfloor\rho/|v|\rfloor+1\).

**Exercise 4.4 (medium).** Using Minkowski's theorem from [Lattices, Minkowski's theorem and the Minkowski embedding](course:NT-ANT/lattices-minkowskis-theorem-and-the-minkowski-embedding), show that a rectangle centred at \(0\) with \(R_1W_1>P\) contains a nonzero multiple of \(\Pi_\sigma\), for every sign vector \(\sigma\).

**Exercise 4.5 (medium).** Step 1 of the proof of Theorem 3.1 concerns sign vectors that differ in few coordinates. Take \(r=1\), \(p_1=5\) with the factors \(2+i\) and \(2-i\), and the square \([-2,2]^2\). Show that both sign vectors are bad, with witnesses that are not collinear.

## 5. Solutions

**4.1.** The stretch is \(\{0,1,\dots,n\}\), so \(R=n\), \(W'=0\), \(W=1\), \(A=n\), and \(E-E=\{-n,\dots,n\}\) has \(2n+1\) elements. Theorem 2.2 gives \(\pi n/24\le n\le n^2\) and \(|E-E|\ge n/\pi\).

**4.2.** All differences \((x,y)\) with \(|x|,|y|\le m-1\) occur, and no others, so \(|E-E|=(2m-1)^2\). The diameter is the diagonal, \(R=(m-1)\sqrt2\), and the farthest points from the diagonal are the two other corners, at distance \((m-1)/\sqrt2\). So \(A=(m-1)^2\) when \((m-1)/\sqrt2\ge1\), that is \(m\ge3\), and \(A=\sqrt2\) when \(m=2\). In both cases \(m^2/4\le A\le2m^2\).

**4.3.** The lattice points of the line are the multiples \(kv\) (Step 2 of the proof of Theorem 3.1), and \(|kv|\le\rho\) means \(|k|\le\rho/|v|\).

**4.4.** The multiples of \(\Pi_\sigma\) form a lattice with basis \(\Pi_\sigma,i\Pi_\sigma\), and its covolume is the determinant \(N(\Pi_\sigma)=P\) of multiplication by \(\Pi_\sigma\) (Lemma 2.5 of the first lesson). The rectangle is convex, symmetric about \(0\), and has area \(4R_1W_1>4P\), so Minkowski's theorem gives a nonzero lattice point in it.

**4.5.** The sign vectors \(0\) and \(1\) select \(2+i\) and \(2-i\). The square contains the witnesses \(2+i\) and \(2-i\), and \(\det(2+i,2-i)=2\cdot(-1)-1\cdot2=-4\ne0\). The two vectors differ in their only coordinate, which is more than \(dr/4=d/4\) coordinates, so Step 1 does not apply to them; nor does Theorem 3.1, since \(d^3r\ge2\) fails for \(r=1\).

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
- [Hatcher] A. Hatcher, Algebraic Topology, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html

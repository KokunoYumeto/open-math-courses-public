# Word maps on unit quaternions and degree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The obstruction to a two-dimensional classifying space in this course is expressed through labels in the group \(H\) of unit quaternions. Later lessons need to solve systems of equations of the form "a word in unknown unit quaternions, with fixed coefficients, equals \(1\)", and to keep a solution inside a prescribed region while the coefficients move. The tool is the mapping degree. For a word map without coefficients, whose exponent sums form a matrix \(B\) with \(\det B\ne0\), Gerstenhaber and Rothaus computed the global degree on \(H^m\) as \(\det B\). This lesson proves the localized statement that the course needs [OpenAI-EG, Section 2]: on every open set invariant under simultaneous conjugation that contains the identity and has no solution on its boundary, the degree is nonzero. The proof counts solutions with an action of a cyclic group of prime order: the solutions in the maximal torus are fixed and the others come in orbits of \(p\) points.

- Unit quaternions (Section 1).
- Word maps and the torus (Section 2).
- Degree on isolating open sets (Section 3).
- A cyclic group of conjugations (Section 4).
- The localized degree of a word map (Section 5).

## 1. Unit quaternions

The quaternions \(\mathbb H\) form the real algebra with basis \(1,i,j,k\) and \(i^2=j^2=k^2=ijk=-1\). The conjugate of \(a=a_0+a_1i+a_2j+a_3k\) is \(\bar a=a_0-a_1i-a_2j-a_3k\), and \(|a|^2=a\bar a=a_0^2+a_1^2+a_2^2+a_3^2\) is the Euclidean norm, with \(|ab|=|a||b|\). The unit quaternions form a group \(H\), the three-sphere in \(\mathbb H=\mathbb R^4\); we use the distance \(|a-b|\). Left and right multiplication by a unit quaternion preserve the norm, so the distance is bi-invariant: \(|ga-gb|=|a-b|=|ag-bg|\).

**Lemma 1.1** (estimates). For unit quaternions,
\[
\begin{aligned}
&\Bigl|\prod_{j=1}^na_j-\prod_{j=1}^nb_j\Bigr|\\
&\quad\le\sum_{j=1}^n|a_j-b_j|,\\
&|ab-ba|\\
&\quad\le2|a-1|\,|b-1|,
\end{aligned}\tag{1.1}
\]
and \(|a^{-1}-1|=|a-1|=|gag^{-1}-1|\). In particular \(|a_1\cdots a_n-1|\le\sum_j|a_j-1|\).

*Proof.* The first inequality follows by telescoping: \(\prod a_j-\prod b_j\) is the sum over \(k\) of \(a_1\cdots a_{k-1}(a_k-b_k)b_{k+1}\cdots b_n\), and each term has norm \(|a_k-b_k|\). For the second, \(ab-ba=(a-1)(b-1)-(b-1)(a-1)\). Finally \(|a^{-1}-1|=|a^{-1}(1-a)|=|1-a|\) and \(|gag^{-1}-1|=|g(a-1)g^{-1}|=|a-1|\). \(\square\)

The *imaginary* quaternions \(\operatorname{Im}\mathbb H\) are those with \(a_0=0\). Every unit quaternion is \(\exp(w)=\cos|w|+\frac w{|w|}\sin|w|\) for some \(w\in\operatorname{Im}\mathbb H\), and \(\exp\) is a diffeomorphism from the open ball of radius \(\pi\) onto \(H\setminus\{-1\}\); its inverse is the *logarithm* \(\log\). Conjugation is an automorphism of \(\mathbb H\) preserving \(\operatorname{Im}\mathbb H\) and the norm, so \(g\exp(w)g^{-1}=\exp(gwg^{-1})\).

The *torus* \(J=\{\cos\theta+i\sin\theta\}\) is the circle of unit complex numbers in \(H\). We identify \(\mathbb H=\mathbb C\oplus\mathbb Cj\), writing \(a=z+wj\) with \(z,w\in\mathbb C\); then \(jz=\bar zj\) for \(z\in\mathbb C\).

## 2. Word maps and the torus

**Definition 2.1.** A *word map* \(f\colon H^m\to H^m\) has as coordinates \(m\) words in its \(m\) arguments and their inverses, without coefficients. Its *exponent-sum matrix* \(B=(B_{ij})\) is the integer matrix whose entry \(B_{ij}\) is the total exponent of the \(j\)-th argument in the \(i\)-th word.

A word map is smooth, its coordinates being polynomial in the coordinates of \(\mathbb H^m\), and \(f(\mathbf 1)=\mathbf 1\) for \(\mathbf 1=(1,\ldots,1)\). Simultaneous conjugation, \(g\cdot(x_1,\ldots,x_m)=(gx_1g^{-1},\ldots,gx_mg^{-1})\), commutes with every word map.

**Lemma 2.2** (the torus). On \(J^m\), a word map is the homomorphism \((e^{i\theta_1},\ldots,e^{i\theta_m})\mapsto(e^{i(B\theta)_1},\ldots,e^{i(B\theta)_m})\). If \(\det B\ne0\), its fibre over \(\mathbf 1\) in \(J^m\) consists of \(|\det B|\) points, at each of which the restricted map \(J^m\to J^m\) has invertible derivative \(B\) in the coordinates \(\theta\).

*Proof.* \(J\) is commutative, so a word evaluates to the product of the powers of the arguments given by its exponent sums. The fibre is \(\{\theta\in(\mathbb R/2\pi\mathbb Z)^m:B\theta\in2\pi\mathbb Z^m\}\), which corresponds to \(B^{-1}\mathbb Z^m/\mathbb Z^m\), a group of order \(|\det B|\). \(\square\)

The points of this fibre are the *torus roots*.

## 3. Degree on isolating open sets

Let \(M\) be a closed oriented smooth \(n\)-manifold, \(f\colon M\to M\) continuous, \(y\in M\), and \(\mathcal O\subseteq M\) open with \(f^{-1}(y)\cap\partial\mathcal O=\varnothing\). Then \(K=f^{-1}(y)\cap\mathcal O=f^{-1}(y)\cap\overline{\mathcal O}\) is compact, and the *degree* \(\deg(f,\mathcal O,y)\in\mathbb Z\) is the image of the orientation class of \(\mathcal O\) along \(K\) in \(H_n(\mathcal O,\mathcal O\setminus K;\mathbb Z)\) under \(f_*\) in \(H_n(M,M\setminus\{y\};\mathbb Z)\cong\mathbb Z\), the last group identified by the orientation at \(y\). We use the following standard properties without proof; a course proving them is recorded as an open obligation of this course.

**(DEG)** (degree on isolating open sets; [Hatcher, Lemma 3.27 and Proposition 2.30]). In this situation:

1. *Regular count.* If \(f\) is smooth near \(K\) and every point of \(K\) has invertible derivative, then \(K\) is finite and \(\deg(f,\mathcal O,y)\) is the sum over \(x\in K\) of the signs of the determinants of the derivatives of \(f\) at \(x\), computed in oriented charts. In particular the degree is \(0\) if \(K=\varnothing\).
2. *Excision.* If \(V\subseteq\mathcal O\) is open, contains \(K\), and \(f^{-1}(y)\cap\partial V=\varnothing\), then \(\deg(f,V,y)=\deg(f,\mathcal O,y)\).
3. *Homotopy invariance.* If \(f_\tau\) depends continuously on \((\tau,x)\in[0,1]\times M\) and \(f_\tau^{-1}(y)\cap\partial\mathcal O=\varnothing\) for every \(\tau\), then \(\deg(f_\tau,\mathcal O,y)\) does not depend on \(\tau\).

We also use Sard's theorem and regular level sets, proved in [Regular values and degree modulo two, Theorem 2.1, Corollary 2.2 and Proposition 3.1](course:borsuks-conjecture-in-dimension-nine/regular-values-and-degree-modulo-two): the critical values of a smooth map form a null set, and the preimage of a regular value of a smooth map from an \((n+k)\)-manifold to an \(n\)-manifold is a smooth \(k\)-manifold.

**Lemma 3.1** (regular values in a family). Let \(U\subseteq M\) be open, \(\Lambda\subseteq\mathbb R^k\) open, \(N\) a smooth \(n\)-manifold and \(\Phi\colon U\times\Lambda\to N\) smooth, and suppose that the derivative of \(\Phi\) is surjective at every point of \(Z=\Phi^{-1}(y)\). Then every \(\lambda\in\Lambda\) outside a null set has the property that \(y\) is a regular value of \(\Phi_\lambda=\Phi(\cdot,\lambda)\) on \(U\).

*Proof.* \(Z\) is a smooth manifold of dimension \(k\), with tangent spaces the kernels of \(d\Phi\). By Sard's theorem the critical values of the projection \(\pi\colon Z\to\Lambda\) form a null set. Let \(\lambda\) be a regular value of \(\pi\), \((x,\lambda)\in Z\), and \(w\) a tangent vector at \(y\). Choose \((a,b)\) with \(d\Phi(a,b)=w\), and, since \(d\pi\) maps \(\ker d\Phi\) onto \(\mathbb R^k\), choose \((a',b)\in\ker d\Phi\). Then \(d\Phi_\lambda(a-a')=d\Phi(a-a',0)=w\). \(\square\)

## 4. A cyclic group of conjugations

Fix an odd prime \(p\), put \(\zeta=e^{2\pi i/p}\in J\), and let \(c\colon H^m\to H^m\) be simultaneous conjugation by \(\zeta\). It generates a cyclic group \(C_p\) of order \(p\), and \(\omega=e^{4\pi i/p}\) is a complex number with \(\omega\ne1\) and \(\omega\notin\mathbb R\).

**Lemma 4.1.** In the coordinates \(a=z+wj\), \(c\) acts on each factor by \((z,w)\mapsto(z,\omega w)\). The fixed set of every nontrivial element of \(C_p\) is \(J^m\), so \(C_p\) acts freely on \(H^m\setminus J^m\). Simultaneous conjugation by any element of \(H\), in particular \(c\), preserves the orientation of \(H^m\), and every word map commutes with \(c\).

*Proof.* \(\zeta(z+wj)\zeta^{-1}=z+\zeta w\,j\bar\zeta=z+\zeta w\zeta j=z+\omega wj\), since \(j\bar\zeta=\zeta j\). The element \(c^r\), \(0<r<p\), multiplies \(w\) by \(\omega^r\ne1\), as \(p\) does not divide \(2r\); so it fixes exactly the points with \(w=0\) in every factor. Conjugation by \(g\) is joined to the identity by conjugations along a path from \(1\) to \(g\) in the connected group \(H\), so it preserves orientation. \(\square\)

## 5. The localized degree of a word map

**Lemma 5.1** (localized word-map degree; [OpenAI-EG, Lemma 2.1]). Let \(m\ge1\) and let \(f\colon H^m\to H^m\) be a word map with \(\det B\ne0\). Let \(\mathcal O\subseteq H^m\) be open, invariant under simultaneous conjugation, with \(\mathbf 1\in\mathcal O\) and \(f^{-1}(\mathbf 1)\cap\partial\mathcal O=\varnothing\). Then \(\deg(f,\mathcal O,\mathbf 1)\ne0\).

*Proof.* Let \(b\) be the number of torus roots in \(\mathcal O\); since \(\mathbf 1\) is one, \(b\ge1\). Choose an odd prime \(p>b\), with \(C_p\), \(c\) and \(\omega\) as in Section 4. We change \(f\) by a small homotopy of \(C_p\)-equivariant maps that keeps \(f\) unchanged on \(J^m\) and creates no root on \(\partial\mathcal O\), until \(\mathbf 1\) is a regular value; by (DEG 3) the degree does not change. The set \(\partial\mathcal O\) is compact and contains no root, so \(f\) stays at a positive distance from \(\mathbf 1\) on it, and every sufficiently small change keeps this property.

*Coordinates at a torus root.* Let \(x\) be a torus root. Use the coordinates \((u,v)\in\mathbb R^m\oplus\mathbb C^m\mapsto x\exp(u_1i+v_1j,\ldots,u_mi+v_mj)\) near \(x\) and \(\log\) near \(\mathbf 1\). Since \(x\) commutes with \(\zeta\), \(c\bigl(x\exp(w)\bigr)=x\exp(\zeta w\zeta^{-1})\), so in both charts \(c\) acts by \((u,v)\mapsto(u,\omega v)\), and the fixed set \(J^m\) is \(\{v=0\}\). Left translation by \(x\) preserves orientation, as in Lemma 4.1, so both charts can be oriented compatibly. In these charts \(f\) becomes an equivariant map \(F\) with \(F(0)=0\). Its derivative \(A\) at \(0\) commutes with the action. A block from \(\mathbb C^m\) to \(\mathbb R^m\) satisfies \(Q(\omega v)=Q(v)\), and a block \(R\) from \(\mathbb R^m\) to \(\mathbb C^m\) satisfies \(R(u)=\omega R(u)\); as \(\omega\ne1\), both vanish. The block \(N\) on \(\mathbb C^m\) commutes with multiplication by the nonreal number \(\omega\), hence with multiplication by \(i\), which is a real combination of \(1\) and \(\omega\): it is complex linear. By Lemma 2.2 the block on \(\mathbb R^m\) is \(B\).

*Regularizing the torus roots.* No root lies on \(\partial\mathcal O\), so each torus root has a coordinate neighbourhood, invariant under \(C_p\), lying in \(\mathcal O\) or outside \(\overline{\mathcal O}\); choose these neighbourhoods pairwise disjoint. In the neighbourhood of \(x\) add to \(F\) the map \((u,v)\mapsto s\chi(u,v)(0,v)\), where \(\chi\) is a smooth function of \(|u|^2+|v|^2\), equal to \(1\) near \(0\) and supported in the neighbourhood, and \(s\) is a small real number with \(\det_{\mathbb C}(N+sI)\ne0\); only finitely many values of \(s\) are excluded. The change is equivariant, vanishes on \(\{v=0\}\), and leaves the block \(B\) unchanged. The new derivative at \(x\) is invertible, and the sign of its determinant is
\[
\begin{aligned}
&\operatorname{sign}(\det B)\cdot\operatorname{sign}\det\nolimits_{\mathbb R}(N+sI)\\
&\qquad=\operatorname{sign}(\det B),
\end{aligned}
\]
since the real determinant of a complex linear map is the square of the absolute value of its complex determinant. By the inverse function theorem, \(x\) is now the only root in the closure of a smaller invariant neighbourhood \(W_x\).

*Regularizing the other roots.* Keep the map unchanged near the closures of the \(W_x\). The set \(Z\) of roots outside their union is closed, hence compact, and disjoint from \(J^m\): on \(J^m\) the map is still the torus homomorphism, whose roots are the torus roots. By compactness \(Z\) has positive distance from \(J^m\), and \(C_p\) acts freely near \(Z\). Cover \(Z\) by finitely many open sets \(W_1,\ldots,W_r\), each with closure in an open set \(W_l'\) whose \(p\) translates under \(C_p\) are pairwise disjoint and disjoint from \(J^m\) and the \(W_x\), and on which \(f\) takes values in a small ball around \(\mathbf 1\). For a parameter \(\lambda=(\lambda_1,\ldots,\lambda_r)\), \(\lambda_l\in(\operatorname{Im}\mathbb H)^m\), put
\[
\begin{aligned}
&f_\lambda(y)=\exp\Bigl(\log f(y)\\
&\qquad+\sum_{l=1}^r\sum_{q=0}^{p-1}\beta_l(c^{-q}y)\,\zeta^q\lambda_l\zeta^{-q}\Bigr)
\end{aligned}
\]
near the translates of the \(W_l'\), and \(f_\lambda=f\) elsewhere, where \(\beta_l\ge0\) is smooth, supported in \(W_l'\) and positive on \(\overline{W_l}\). For small \(\lambda\) the exponent stays in the ball of radius \(\pi\). The map \(f_\lambda\) is equivariant, since \(\log\) and \(\exp\) commute with conjugation, and it equals \(f\) on \(J^m\) and near the \(W_x\). At a root \(y\) of \(f_\lambda\) in a translate \(c^q(\overline{W_l})\), the derivative with respect to \(\lambda_l\) is the derivative of \(\exp\) composed with the invertible map \(\lambda_l\mapsto\beta_l(c^{-q}y)\zeta^q\lambda_l\zeta^{-q}\), hence surjective. For \(\lambda\) small enough, all roots of \(f_\lambda\) outside the \(W_x\) lie in the union of these translates, by compactness, since \(f\) has no roots in the compact complement of the \(W_x\) and of the translates of the \(W_l\). By Lemma 3.1 there are arbitrarily small \(\lambda\) for which \(\mathbf 1\) is a regular value of \(f_\lambda\) outside the \(W_x\); inside the \(W_x\) the only roots are the torus roots, which are regular. The homotopy \(\tau\mapsto f_{\tau\lambda}\) creates no roots on \(\partial\mathcal O\) when \(\lambda\) is small.

*Counting.* By (DEG 1), \(\deg(f,\mathcal O,\mathbf 1)\) is the sum of the signs of the roots of \(f_\lambda\) in \(\mathcal O\). The \(b\) torus roots in \(\mathcal O\) contribute \(\operatorname{sign}(\det B)\) each. The other roots in \(\mathcal O\) are not fixed by any nontrivial element of \(C_p\), and \(\mathcal O\) is invariant, so they fall into orbits of \(p\) points; in an orbit the signs agree, since \(c\) preserves the orientations of source and target and \(f_\lambda\circ c=c\circ f_\lambda\). Hence
\[
\deg(f,\mathcal O,\mathbf 1)\equiv b\operatorname{sign}(\det B)\pmod p,
\]
which is not divisible by \(p\), since \(0<b<p\). \(\square\)

Since the argument works for every odd prime \(p>b\), the degree is exactly \(b\operatorname{sign}(\det B)\). For \(\mathcal O=H^m\), \(b=|\det B|\) and the degree is \(\det B\), the theorem of Gerstenhaber and Rothaus [Gerstenhaber–Rothaus 1962, Theorem 1] for the group \(H\); only the nonvanishing is used in this course. When \(m=0\), with no unknowns and no equations, the map is the identity of a point, and its degree is \(1\) by convention.

## 6. Exercises

**6.1.** Check the inequality \(|ab-ba|\le2|a-1||b-1|\) for \(a=i\), \(b=j\).

**6.2.** Let \(m=1\) and \(f(x)=x^k\) with \(k\ge2\). Find \(B\), the torus roots, and all roots of \(f\) in \(H\). Show that for \(\mathcal O=\{x:|x-1|<r\}\) with \(r\) small, \(\deg(f,\mathcal O,1)=1\), as Lemma 5.1 predicts with \(b=1\).

**6.3.** Show that a real linear map of \(\mathbb C^m\) commuting with multiplication by a nonreal complex number is complex linear, and that its real determinant is \(|\det_{\mathbb C}|^2\).

**6.4.** For \(m=2\) and \(f(x,y)=(x^2y,\,xy^{-1})\), compute \(B\) and the number of torus roots.

**6.5.** Explain why the proof of Lemma 5.1 needs the prime \(p\) to exceed \(b\), and why it uses an odd prime.

## 7. Solutions

**6.1.** \(ij-ji=2k\) has norm \(2\), and \(|i-1|=|j-1|=\sqrt2\), so the right side is \(4\).

**6.2.** \(B=(k)\), and the torus roots are \(e^{2\pi ir/k}\), \(0\le r<k\). A unit quaternion \(\cos\theta+u\sin\theta\), with \(u\) a unit imaginary quaternion, has \(k\)-th power \(\cos k\theta+u\sin k\theta\); so the roots are the points with \(\theta\in\frac{2\pi}k\mathbb Z\), which for \(0<\theta<\pi\) form two-spheres. For \(r<|e^{2\pi i/k}-1|\) the only root in \(\mathcal O\) is \(1\), where the derivative of \(x\mapsto x^k\) in exponential coordinates is multiplication by \(k\), with positive determinant; so the degree is \(1\).

**6.3.** Multiplication by \(i\) is a real combination of the identity and multiplication by the nonreal number. In a complex basis where the map is triangular, with diagonal entries \(\mu_l\), its real matrix is block triangular with \(2\times2\) blocks of determinant \(|\mu_l|^2\).

**6.4.** \(B=\begin{pmatrix}2&1\\1&-1\end{pmatrix}\) has determinant \(-3\), so there are three torus roots.

**6.5.** The count is \(b\operatorname{sign}(\det B)\) modulo \(p\), which is nonzero only if \(p\) does not divide \(b\); \(p>b\) ensures this. For \(p=2\), \(\omega=e^{2\pi i}=1\): conjugation by \(\zeta=-1\) is trivial, and the action does not separate the torus from its complement.

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Gerstenhaber–Rothaus 1962] M. Gerstenhaber and O. S. Rothaus, *The solution of sets of equations in groups*, Proc. Nat. Acad. Sci. U.S.A. 48 (1962), 1531–1533, Theorem 1. https://doi.org/10.1073/pnas.48.9.1531; free on PubMed Central: https://pmc.ncbi.nlm.nih.gov/articles/PMC220992/
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf

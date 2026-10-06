# Invariant states and finite-rank projections

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

An invariant state can be singular. We replace its invariance by a norm estimate for a normal state, take the square root of its density, and select one spectral level. In the trace representation of an injective finite algebra, the selected projection has finite Hilbert-space rank. Its range can then be described by bounded operators in the algebra.

The hypertrace construction is already proved. For general semifinite traces we retain the trace-density identification in [Trace densities and noncommutative integration](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#trace-integration), TI-06, together with measurable-operator calculus, trace Hölder and cyclicity. We prove the square-root and spectral-level inequalities below for positive elements of the full semifinite \(L^2\) space. The spectral argument uses finite partitions and monotone approximation; the positive operators need not commute. General weights remain separate prerequisites.

For a finite algebra \(M\) with faithful normal tracial state \(\tau\), put \(H=L^2(M,\tau)\) and \(\|x\|_2=\tau(x^*x)^{1/2}\). Inner products are linear in the second variable. Write \(\operatorname{Tr}\) for the ordinary operator trace on \(B(H)\), and \(\|\cdot\|_{\mathrm{HS}}\) for its Hilbert–Schmidt norm. These differ from \(\tau\) and the norm on \(M\).

## 1. A spectral level from an invariant state

For \(h\in L^2(N,\sigma)_+\), let \(P_t(h)=1_{(\sqrt t,\infty)}(h)\), \(t>0\). The three estimates needed for projection selection are
\[
\begin{aligned}
\|h-k\|_{2,\sigma}^2&\le\|h^2-k^2\|_{1,\sigma},\\
\int_0^\infty\|P_t(h)-P_t(k)\|_{2,\sigma}^2\,dt
&\le\|h-k\|_{2,\sigma}\|h+k\|_{2,\sigma},\\
\int_0^\infty\sigma(P_t(h))\,dt&=\|h\|_{2,\sigma}^2.
\end{aligned}
\tag{1}
\]
Every positive-level projection has finite trace, since \(\sigma(P_t(h))\le t^{-1}\|h\|_{2,\sigma}^2\).

### Proof of the three trace estimates

For the first inequality, put \(c=h-k\), and let \(p\) and \(q\) be the support projections of its positive and negative parts \(c_+,c_-\). Then \(z=p-q\) is a self-adjoint contraction and \(cz=zc=|c|\). Hölder puts all products below in \(L^1\), and trace cyclicity gives
\[
\begin{aligned}
\sigma((h^2-k^2)z)
&=\sigma(hcz+ckz)\\
&=\sigma(h|c|+|c|k)\\
&=\sigma(c_+^2+c_-^2)
  +2\sigma(kc_+)+2\sigma(hc_-).
\end{aligned}
\]
The last two traces are nonnegative. Indeed, the trace pairing of positive \(L^2\) elements is nonnegative: truncate them to bounded positive elements of finite spectral support, use \(\sigma(ab)=\sigma(a^{1/2}ba^{1/2})\ge0\), and pass to the limit by Hölder. Thus
\[
\|h-k\|_{2,\sigma}^2
\le\sigma((h^2-k^2)z)
\le\|h^2-k^2\|_{1,\sigma}.
\]
This argument includes unbounded measurable \(h,k\); no finiteness of \(\sigma(1)\) is used.

For the second estimate, first suppose
\[
h=\sum_{i=1}^r\lambda_i e_i,\qquad
k=\sum_{j=1}^s\mu_j f_j
\]
have finitely many strictly positive spectral values, with finite-trace spectral projections. Set \(e_0=1-\sum_i e_i\), \(f_0=1-\sum_j f_j\), and \(\lambda_0=\mu_0=0\). For every pair \((i,j)\ne(0,0)\), put
\[
\nu_{ij}=\sigma(e_i f_j)=\sigma(e_i f_j e_i)\ge0.
\]
These quantities are finite, including when exactly one index is zero. Their row and column sums are \(\sigma(e_i)\) and \(\sigma(f_j)\) for positive indices. Expansion of the squared trace norm gives
\[
\begin{aligned}
\|h-k\|_{2,\sigma}^2&=\sum_{(i,j)\ne(0,0)}
   (\lambda_i-\mu_j)^2\nu_{ij},\\
\|h+k\|_{2,\sigma}^2&=\sum_{(i,j)\ne(0,0)}
   (\lambda_i+\mu_j)^2\nu_{ij}.
\end{aligned}
\]
The same expansion for the level projections, followed by integration, yields
\[
\begin{aligned}
\int_0^\infty\|P_t(h)-P_t(k)\|_{2,\sigma}^2\,dt
&=\sum_{(i,j)\ne(0,0)}|\lambda_i^2-\mu_j^2|\nu_{ij}\\
&\le\|h-k\|_{2,\sigma}\|h+k\|_{2,\sigma}.
\end{aligned}
\]
Here the integral of the difference of two level indicators is the distance between their squared endpoints; the last step is the scalar Cauchy–Schwarz inequality. No joint spectral resolution of \(h\) and \(k\) has been assumed.

For general positive \(h,k\in L^2(N,\sigma)\), define
\[
a_n(\lambda)=\min\{2^n,\,2^{-n}\lfloor2^n\lambda\rfloor\},
\qquad h_n=a_n(h),\quad k_n=a_n(k).
\]
Each has finitely many positive values and finite-trace support. The functions \(a_n\) increase to the identity and are bounded above by it, so \(h_n\to h\) and \(k_n\to k\) in \(L^2\). For each \(t>0\), their level projections increase to \(P_t(h)\) and \(P_t(k)\). Normality of \(\sigma\) and finiteness of these level traces give convergence in \(L^2\). Fatou's lemma now passes the preceding integral inequality to \(h,k\). Finally, the ordinary scalar layer-cake identity, applied to the spectral trace measure of \(h\), gives the third estimate in (1). This also proves every integration and finiteness claim used below.

**Theorem 1.1.** Let \(N\) carry a faithful normal semifinite trace \(\sigma\), and let \(F\subset\mathcal U(N)\) be finite. Suppose a state \(\psi\) on \(N\), possibly singular, satisfies \(\psi\circ\operatorname{Ad}(u)=\psi\) for \(u\in F\). For every \(\varepsilon>0\) there is a nonzero projection \(p\in N\), with \(\sigma(p)<\infty\), such that
\[
\|p-upu^*\|_{2,\sigma}<\varepsilon\sqrt{\sigma(p)}
\qquad(u\in F).
\tag{2}
\]
Factoriality and countability assumptions are unnecessary.

**Proof.** Normal states are weak* dense in the state space. Otherwise real separation gives a self-adjoint \(a\in N\) whose value at some state exceeds its supremum over normal states. That supremum is the top of the spectrum: a nonzero spectral projection near the top supports a normal state attaining values arbitrarily near it. Every state has value at most that spectral bound, a contradiction.

Let \(n=|F|\ge1\). In the Banach space \(\bigoplus_{u\in F}N_*\), with sum norm, consider the convex set
\[
\left\{\bigl(\varphi-\varphi\circ\operatorname{Ad}(u)\bigr)_{u\in F}:
\varphi\text{ a normal state}\right\}.
\tag{3}
\]
Weak* approximation to \(\psi\) puts zero in its weak closure: pairing each coordinate against an element of \(N\) tends to zero. The dual of this finite predual sum is the corresponding product of \(N\)'s. Hahn–Banach separation makes the weak and norm closures of a convex set equal. Hence, for any \(d>0\), choose a normal state with
\[
\sum_{u\in F}\|\varphi-\varphi\circ\operatorname{Ad}(u)\|<d.
\tag{4}
\]
The trace-density theorem writes \(\varphi(x)=\sigma(a x)\), with \(a\in L^1(N,\sigma)_+\), \(\sigma(a)=1\). Put \(h=a^{1/2}\). The density of \(\varphi\circ\operatorname{Ad}(u)\) is \(u^*a u\). The first estimate in (1) and isometry of the trace pairing give
\[
\sum_{u\in F}\|h-u^*h u\|_{2,\sigma}^2<d,\qquad
\|h\|_{2,\sigma}=1.
\tag{5}
\]
The other two estimates, conjugation of spectral projections, and Cauchy–Schwarz in the finite index set imply
\[
\begin{aligned}
\int_0^\infty\sum_{u\in F}
\|P_t(h)-u^*P_t(h)u\|_{2,\sigma}^2\,dt
&\le2\sum_{u\in F}\|h-u^*h u\|_{2,\sigma}\\
&<2\sqrt{nd},\\
\int_0^\infty\sigma(P_t(h))\,dt&=1.
\end{aligned}
\tag{6}
\]
Choose \(d=\varepsilon^4/(16n)\). The first integral is less than \(\varepsilon^2/2\). Some level has nonzero projection \(p=P_t(h)\) and summed squared conjugation error less than \(\varepsilon^2\sigma(p)\); otherwise integration contradicts (6). Each summand satisfies that bound. Conjugation by \(u\) turns its norm into \(\|upu^*-p\|_{2,\sigma}\), proving (2). If \(F\) is empty, semifiniteness supplies any nonzero finite-trace projection. \(\square\)

The square root in \(2\sqrt{nd}\) determines the fourth-power choice of \(d\). A linear estimate in \(d\) does not follow from the square-root density inequality.

## 2. A bounded basis for a finite-rank model

**Corollary 2.1.** If \(M\) is finite and injective with faithful normal tracial state, then for every finite \(F\subset\mathcal U(M)\) and \(a>0\) there are \(x_1,\ldots,x_m\in M\), orthonormal in \(H\), such that the finite-rank projection
\[
q\xi=\sum_{i=1}^m x_i\tau(x_i^*\xi)
\tag{7}
\]
satisfies
\[
\sum_{v\in F}\|v q v^*-q\|_{\mathrm{HS}}^2<a^2m.
\tag{8}
\]
Here \(v\) acts by left multiplication. No factor or separability assumption is needed.

**Proof.** The hypertrace on \(B(H)\) is invariant under every such \(v\). Apply Theorem 1.1 to \(B(H)\) with \(\sigma=\operatorname{Tr}\) and initial tolerance small enough to make the summed error less than \(a^2m/4\). A nonzero projection of finite ordinary trace has finite rank \(m\).

Approximate an orthonormal basis \(\xi_1,\ldots,\xi_m\) of its range by vectors \(y_i\in M\). Their Gram matrix \(G=[\tau(y_i^*y_j)]\) tends to the identity. For sufficiently good approximants it is invertible; define \(x_i=\sum_j y_j(G^{-1/2})_{ji}\). These vectors belong to \(M\), are exactly orthonormal, and tend to \(\xi_i\) in \(H\). Their range projections tend to the original projection in Hilbert–Schmidt norm, because
\[
\||x\rangle\langle x|-|\xi\rangle\langle\xi|\|_{\mathrm{HS}}
\le(\|x\|_2+\|\xi\|_2)\|x-\xi\|_2.
\tag{9}
\]
A conjugation difference changes by at most twice the projection error. Finitely many tests and the strict initial margin give (8). The empty test set permits \(x_1=1\). \(\square\)

For \(b,c\in H\), write \(K_{b,c}\xi=b\,\tau(c^*\xi)\), interpreted by the Hilbert inner product. Its Hilbert–Schmidt norm is \(\|b\|_2\|c\|_2\). For bounded \(v,w\in M\), let \(L_v\xi=v\xi\), \(R_w\xi=\xi w\). Direct evaluation gives
\[
\begin{aligned}
L_v K_{b,c}&=K_{vb,c},&K_{b,c}L_v&=K_{b,v^*c},\\
R_w K_{b,c}&=K_{bw,c},&K_{b,c}R_w&=K_{b,cw^*},\\
K_{b,c}K_{d,e}&=\tau(c^*d)K_{b,e}.
\end{aligned}
\tag{10}
\]
The right action is an antirepresentation and commutes with the left action. These identities fix the orientations in the later small-corner proof.

## 3. Most pinched corners have almost scalar coefficients

Here \(M\) is a type \(\mathrm{II}_1\) factor with separable predual. We use the [scalar pinching theorem](semiregular-masas-and-scalar-pinching.md#theorem-3-1), whose construction uses contained AFD subfactors and decreasing expectations. Its inputs precede the injective-factor converse.

**Lemma 3.1.** Let \(x_1,\ldots,x_m\in M\) be orthonormal in \(L^2\), let finite \(F\subset\mathcal U(M)\) contain \(1\), and let \(0<b<1\). There are nonzero mutually orthogonal projections \(f_1,\ldots,f_l\) such that
\[
\begin{aligned}
\sum_{v\in F}\sum_{i,j=1}^m
\|f_k x_i^*v x_jf_k-\tau(x_i^*v x_j)f_k\|_2^2
&\le b^2\tau(f_k),\\
\sum_{k=1}^l\tau(f_k)&>1-b^2.
\end{aligned}
\tag{11}
\]

**Proof.** If the indexed family is empty, take \(f_1=1\). Otherwise put \(Q=|F|m^2\), and let \(C\) be the finite set of distinct operators among the coefficients \(x_i^*v x_j\). Apply the scalar pinching theorem with \(N=M\), the set \(C\), and tolerance \(b^2/\sqrt Q\). This gives a finite partition \((p_k)\) of \(1\); remove any zero atoms. Every coefficient in the indexed family has squared pinching error less than \(b^4/Q\), so
\[
\sum_{v\in F}\sum_{i,j=1}^m
\left\|\sum_k p_k x_i^*v x_jp_k-\tau(x_i^*v x_j)1\right\|_2^2<b^4.
\]
This tolerance accounts for repetitions in the indexed family.

For each atom put
\[
a_k=\sum_{v\in F}\sum_{i,j=1}^m
\|p_k x_i^*v x_jp_k-\tau(x_i^*v x_j)p_k\|_2^2.
\]
Errors supported on different diagonal corners are orthogonal in \(L^2\), hence \(\sum_k a_k<b^4\). Retain precisely the atoms with \(a_k\le b^2\tau(p_k)\). If any atoms are discarded, then
\[
b^2\sum_{\mathrm{bad}\ k}\tau(p_k)
<\sum_{\mathrm{bad}\ k}a_k<b^4;
\]
if none are discarded their total trace is zero. In either case the retained trace is greater than \(1-b^2>0\), and the retained atoms prove (11). For \(v=1\), orthonormality gives \(\tau(x_i^*x_j)=\delta_{ij}\). \(\square\)

The first selection produces an external finite-rank projection on \(H\). The second produces initial projections inside \(M\). The next lesson repairs its almost orthonormal vectors to internal matrix units.

## 4. Exercises with complete solutions

**Exercise 1.** Why does weak* approximation suffice for the weak closure assertion in (3)?

*Solution.* A continuous linear functional on the finite predual sum is a list \(z_u\in N\). On (3) it takes value \(\sum_u\varphi(z_u-u z_u u^*)\). Normal states tending weak* to \(\psi\) make this tend to zero by invariance. Thus every weak neighborhood of zero meets the set. Norm separation of its convex closure would also be weak separation.

**Exercise 2.** Verify the normal-state density argument when the spectral supremum is not an eigenvalue.

*Solution.* For \(s=\sup\operatorname{Sp}(a)\), the projection \(e=1_{(s-\eta,s]}(a)\) is nonzero for every \(\eta>0\). A nonzero normal positive functional supported in \(e\), normalized by its value at \(e\), is a normal state with value between \(s-\eta\) and \(s\). Let \(\eta\downarrow0\).

**Exercise 3.** Check the fourth-power budget for three unitaries.

*Solution.* Set \(d=\varepsilon^4/48\). Then \(2\sqrt{3d}=\varepsilon^2/2\). The integrated rank is one, so some level has total squared error less than \(\varepsilon^2\) times its trace. Each summand obeys that bound; take square roots.

**Exercise 4.** Why does a finite-trace projection need not have finite Hilbert-space rank?

*Solution.* In a type \(\mathrm{II}_1\) factor every projection has finite trace, while nonzero corners act on infinite-dimensional spaces. Finite rank follows in Corollary 2.1 because the ambient algebra is \(B(H)\) and its ordinary trace counts the range dimension.

**Exercise 5.** Check the Gram correction in (7).

*Solution.* Let \(Y:\mathbb C^m\to H\) have columns \(y_i\). Then \(Y^*Y=G\). The corrected map \(X=YG^{-1/2}\) has \(X^*X=1\). Its columns are orthonormal, and each is a finite scalar linear combination of bounded elements of \(M\).

**Exercise 6.** Prove (9).

*Solution.* The rank-one difference is \(K_{x-\xi,x}+K_{\xi,x-\xi}\). Each rank-one norm is the product of its two vector norms. The triangle inequality proves (9), and finite sums give convergence of the range projections.

**Exercise 7.** Verify \(K_{b,c}R_w=K_{b,cw^*}\).

*Solution.* On a bounded vector \(\xi\), the left side is \(b\,\tau(c^*\xi w)=b\,\tau(wc^*\xi)\). Since \((cw^*)^*=wc^*\), this equals \(K_{b,cw^*}\xi\). Density and boundedness extend the equality to \(H\).

**Exercise 8.** Bound the discarded trace in Lemma 3.1.

*Solution.* Summing the bad atoms' strict inequalities gives \(b^2\sum_{\mathrm{bad}}\tau(p_k)<b^4\). Divide by \(b^2\). The retained trace is greater than \(1-b^2\), so at least one atom remains.

**Exercise 9.** Why include \(1\) in \(F\) although its conjugation error is zero?

*Solution.* Its coefficients in (11) are \(\tau(x_i^*x_j)=\delta_{ij}\). The compressed relations therefore give almost orthonormal Gram matrices. Their repair supplies partial isometries with one common initial projection; the other tests determine the approximation coefficients.

**Exercise 10.** Distinguish the hypotheses of the three results.

*Solution.* Theorem 1.1 allows any faithful normally semifinitely tracial algebra and a state invariant under the specified unitaries. Corollary 2.1 uses a finite injective algebra with faithful normal tracial state and a hypertrace on \(B(L^2(M,\tau))\). Lemma 3.1 additionally uses separable predual and a type \(\mathrm{II}_1\) factor, the hypotheses of scalar pinching. The first two results also apply off factors.

## References and proof scope

Sorin Popa, [*A short proof of “injectivity implies hyperfiniteness” for finite von Neumann algebras*](https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-005.pdf), *Journal of Operator Theory* 16 (1986), 261–272. Section 2 supplies the convexity, square-root density and spectral-level method; Remark 2.3 gives a direct proof of the square-root inequality. The proof above extends that calculation to positive measurable elements of the full semifinite trace space and supplies the finite-partition and monotone-limit details.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Lemma 10.2.6, Theorems 10.2.7–10.2.9, Theorem 10.3.1, Remark 10.3.2, and Proposition 10.3.3 through Theorem 10.3.6. These give the normal-state convexity and finite-rank spectral construction. Here the first result retains arbitrary semifinite algebras and the second arbitrary faithfully tracial injective algebras. The Gram correction is given explicitly. The final near-covering scalar pinching statement uses the separately declared factor theorem; the abelian-module Rohlin lemma in Popa's paper is a different input.

Lemma 3.1 is the complete direct consequence above of the [scalar pinching theorem](semiregular-masas-and-scalar-pinching.md#theorem-3-1), applied with the given factor as both ambient algebra and subfactor. The set-to-indexed-family tolerance, orthogonal corner sum and discarded-trace bound are supplied here. Popa's Lemma 2.3, printed pp.268–269, and Anantharaman–Popa's Lemma 11.1.11, printed p.179, prove the related local Rohlin selection by orthogonal corner errors. Those source lemmas choose one nonzero corner and its local scalar means; the global trace coefficients and near-covering family in (11) use the separately proved course theorem. Its decreasing-expectation step also follows the full proof of Anantharaman–Popa, Lemma 11.1.9, printed p.178.

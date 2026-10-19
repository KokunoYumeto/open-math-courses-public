# Repairing small matrix corners

*AI-generated exposition by OpenAI GPT models. CC0-1.0 to the extent of rights held.*

Almost-orthonormal compressed vectors determine a Gram matrix. One spectral cut controls all its entries, and inverse-square-root normalization produces exact matrix units with a common initial projection. A scalar polar-repair construction gives a second proof with an explicit recursive error bound. Both constructions control matrix coefficients for a finite operator family.

The Gram and single-vector constructions allow every finite von Neumann algebra \(M\) with faithful normal tracial state \(\tau\), with no factor or separability assumption. We use bounded polar and spectral calculus, trace cyclicity, and the tracial multiplication bounds \(\|axb\|_2\le\|a\|\|x\|_2\|b\|\). The spectral foundations and [trace Hilbert-space products](../components/invariant-state-trace-hilbert-inputs.md#trace-holder-and-cyclicity) supply these arguments, including the complete trace Hilbert space and positive cyclic pairing. The near-covering corollary uses the [pinched corner selection](invariant-states-and-finite-rank-projections.md#lemma-3-1), which retains a separable type \(\mathrm{II}_1\) factor. All norms below are the ambient trace norms.

<a id="3-internal-matrix-systems-on-almost-all-initial-trace"></a>

## Near-covering matrix coordinates

**Corollary 3.1.** In a separable \(\mathrm{II}_1\) factor, let \(x_1,\ldots,x_m\) be \(L^2\)-orthonormal and finite \(F\subset\mathcal U(M)\) contain \(1\). Fix \(B\ge\max(1,\|x_1\|,\ldots,\|x_m\|)\). For sufficiently small \(b>0\), there are nonzero mutually orthogonal initial projections \(e_k\) and partial isometries \(w_i(k)\) such that
\[
\begin{aligned}
w_i(k)^*w_j(k)&=\delta_{ij}e_k,\\
\|x_i e_k-w_i(k)\|_2&\le D_m(b)\sqrt{\tau(e_k)},\\
\|w_i(k)^*v w_j(k)-A_{ij}(v)e_k\|_2
&\le d_m(b)\sqrt{\tau(e_k)},\\
A_{ij}(v)&=\tau(x_i^*v x_j),\\
\sum_k\tau(e_k)&>\frac{1-b^2}{1+D_m(b)^2}.
\end{aligned}
\tag{19}
\]
Put \(E_{ij}(k)=w_i(k)w_j(k)^*\) and \(s_k=\sum_i E_{ii}(k)\). Then
\[
\left\|s_k v s_k-\sum_{i,j}A_{ij}(v)E_{ij}(k)\right\|_2
\le\sqrt m\,d_m(b)\sqrt{\tau(s_k)}.
\tag{20}
\]

**Proof.** The Gram theorem used here is proved in the next section. Select the \(f_k\)'s of the preceding lesson and apply Theorem 2.1 to each one. Every individual squared error is bounded by their nonnegative sum, so (10) and (12) hold. Since \(e_k\le f_k\), the \(e_k\)'s are orthogonal. The trace bound follows by summing \(\tau(f_k)\le(1+D_m(b)^2)\tau(e_k)\).

In the matrix coordinates \(w_i(k)\), the squared norm on the left of (20) is the sum of the \(m^2\) squared coefficient errors in (19). Its bound is \(m^2d_m(b)^2\tau(e_k)\). As \(\tau(s_k)=m\tau(e_k)\), taking square roots gives (20). \(\square\)

The range projections \(s_k\) need not be mutually orthogonal. Their initial projections \(e_k\) are; that is the orthogonality used in the next selection argument. Also \(A(v)\) is a contraction: it is the compression of the unitary \(L_v\) to the span of the orthonormal \(x_i\)'s.

<a id="2-a-finite-gram-system-and-its-coefficients"></a>

## Simultaneous normalization of a finite Gram system

<a id="simultaneous-gram-normalization"></a>

The simultaneous proof gives an explicit modulus by normalizing the whole Gram matrix. The recursive alternative gives another admissible modulus and uses the scalar repair lemmas proved in the following section. The coefficient estimate and the near-covering corollary apply with either proved choice.

**Theorem 2.1.** Fix \(m\ge1\) and \(B\ge1\). For sufficiently small \(b>0\) there is \(D_m(b)\to0\) as \(b\downarrow0\) with the following property. If \(f\ne0\), \(\|x_i\|\le B\), and
\[
\|f x_i^*x_j f-\delta_{ij}f\|_2\le b\sqrt{\tau(f)}
\qquad(1\le i,j\le m),
\tag{10}
\]
there are \(e\le f\) and partial isometries \(w_1,\ldots,w_m\) such that
\[
w_i^*w_j=\delta_{ij}e,\qquad
\tau(f-e)\le D_m(b)^2\tau(e),\qquad
\|x_i e-w_i\|_2\le D_m(b)\sqrt{\tau(e)}.
\tag{11}
\]
If also \(\|v\|\le1\) and
\[
\|f x_i^*v x_j f-\lambda_{ij}f\|_2\le b\sqrt{\tau(f)},
\tag{12}
\]
then
\[
\|w_i^*v w_j-\lambda_{ij}e\|_2
\le d_m(b)\sqrt{\tau(e)},\qquad
d_m(b)=(1+B)D_m(b)+b\sqrt{1+D_m(b)^2}.
\tag{13}
\]

**Proof by simultaneous Gram normalization.** Fix
\[
0<b<\frac{1}{4m^2},
\qquad
D_m(b)^2=\frac{m^2b}{1-m^2b}.
\tag{QG1}
\]
This admissible modulus tends to zero for every fixed \(m\). We construct all \(m\) partial isometries together.

Work first in the corner \(fMf\), whose identity is \(f\). For \(1\le i,j\le m\), set
\[
A_{ij}=f x_i^*x_j f-\delta_{ij}f,
\qquad
T=\sum_{i,j=1}^m A_{ij}^*A_{ij}\in(fMf)_+.
\]
Hypothesis (10) gives
\[
\tau(T)=\sum_{i,j=1}^m\|A_{ij}\|_2^2
\le m^2b^2\tau(f).
\tag{QG2}
\]
Use one spectral projection of this positive operator:
\[
e=1_{[0,b]}^{\,fMf}(T).
\]
The superscript specifies functional calculus with identity \(f\), so \(e\le f\), including the kernel of \(T\) inside this corner. Spectral integration on \(f-e\) gives
\[
b\,\tau(f-e)\le\tau(T)\le m^2b^2\tau(f).
\]
Consequently
\[
\tau(e)\ge(1-m^2b)\tau(f)>0,
\qquad
\tau(f-e)\le\frac{m^2b}{1-m^2b}\tau(e),
\qquad
\tau(f)\le\frac{\tau(e)}{1-m^2b}.
\tag{QG3}
\]
In particular the selected projection is nonzero. Since each \(A_{ij}^*A_{ij}\le T\), compression gives
\[
(A_{ij}e)^*(A_{ij}e)
=eA_{ij}^*A_{ij}e
\le eTe\le b e.
\]
Thus \(\|A_{ij}e\|\le\sqrt b\), and also \(\|eA_{ij}e\|\le\sqrt b\).

Let \(\mathbf1_e=\operatorname{diag}(e,\ldots,e)\), and consider the row and its Gram matrix
\[
X=(x_1e,\ldots,x_me),
\qquad
G=X^*X=[e x_i^*x_j e]_{i,j=1}^m
\in M_m(eMe).
\]
Every entry of \(G-\mathbf1_e\) has norm at most \(\sqrt b\). Hence
\[
\|G-\mathbf1_e\|\le m\sqrt b<\tfrac12.
\tag{QG4}
\]
For completeness, if \(\xi=(\xi_j)\) is in a Hilbert-space representation of \((eMe)^m\), then each row of \((G-\mathbf1_e)\xi\) has norm at most \(\sqrt b\sum_j\|\xi_j\|\). Squaring, summing the \(m\) rows, and applying scalar Cauchy--Schwarz proves this matrix-norm bound. It uses no commutation of the Gram entries.

The positive matrix \(G\) is therefore invertible in \(M_m(eMe)\). Bounded continuous functional calculus defines \(G^{-1/2}\) there. Put
\[
W=XG^{-1/2}=(w_1,\ldots,w_m).
\tag{QG5}
\]
Each entry is an element of \(Me\), and direct matrix multiplication gives
\[
W^*W=G^{-1/2}GG^{-1/2}=\mathbf1_e,
\qquad
w_i^*w_j=\delta_{ij}e.
\tag{QG6}
\]
In particular each \(w_i\) is a partial isometry with initial projection \(e\). Their range projections are mutually orthogonal, and \(w_iw_j^*\) satisfy the matrix-unit relations.

We next prove the full trace error estimate. On \(M_m(eMe)\), use the unnormalized finite trace
\[
\operatorname{Tr}_m([z_{ij}])=\sum_{i=1}^m\tau(z_{ii}).
\]
Since \(X=WG^{1/2}\) and \(W^*W=\mathbf1_e\),
\[
\begin{aligned}
\sum_{i=1}^m\|w_i-x_i e\|_2^2
&=\operatorname{Tr}_m\bigl((W-X)^*(W-X)\bigr)\\
&=\operatorname{Tr}_m\bigl((\mathbf1_e-G^{1/2})^2\bigr)\\
&\le\operatorname{Tr}_m\bigl((\mathbf1_e-G)^2\bigr)\\
&=\sum_{i,j=1}^m\|eA_{ij}e\|_2^2\\
&\le\sum_{i,j=1}^m\|A_{ij}\|_2^2
\le m^2b^2\tau(f).
\end{aligned}
\tag{QG7}
\]
The scalar inequality \(|1-\sqrt t|\le|1-t|\) for \(t\ge0\), applied by functional calculus to \(G\), proves the middle inequality. The next identity is the entrywise trace expansion of the square of the self-adjoint matrix \(G-\mathbf1_e\); all products lie in the finite matrix algebra. Trace multiplication bounds prove the compression inequality.

Every nonnegative individual squared error is bounded by the sum in (QG7). With (QG3) and \(b<1\), this yields
\[
\|w_i-x_i e\|_2^2
\le\frac{m^2b^2}{1-m^2b}\tau(e)
\le D_m(b)^2\tau(e).
\tag{QG8}
\]
Together with the trace loss in (QG3) and the relations (QG6), this proves every assertion in (11).

Finally suppose (12) holds and \(\|v\|\le1\). Expand
\[
\begin{aligned}
w_i^*v w_j-\lambda_{ij}e
={}&(w_i^*-e x_i^*)v w_j\\
&+e x_i^*v(w_j-x_j e)\\
&+e(x_i^*v x_j-\lambda_{ij}f)e .
\end{aligned}
\]
Here \(\|w_j\|=1\), \(\|x_i\|\le B\), and the last term has \(L^2\) norm at most \(b\sqrt{\tau(f)}\). Equations (QG3) and (QG8) therefore give
\[
\|w_i^*v w_j-\lambda_{ij}e\|_2
\le\left((1+B)D_m(b)
       +b\sqrt{1+D_m(b)^2}\right)\sqrt{\tau(e)}.
\tag{QG9}
\]
Indeed \(1+D_m(b)^2=(1-m^2b)^{-1}\). This is exactly (13). All constructions occur in an arbitrary finite von Neumann algebra with the stated faithful normal trace. Neither a factor nor a separable-predual assumption was used. \(\square\)

**Second proof, by successive polar repairs.** Replace \(x_i\) by \(x_i f\); the hypotheses are unchanged and so are the final \(x_i e\)'s. For \(m=1\), Lemma 1.1 permits \(D_1(b)^2=b/(1-b)\). Suppose \(k-1\) vectors have been repaired with error \(D=D_{k-1}(b)\) and initial projection \(f'\le f\). Then
\[
\tau(f)\le(1+D^2)\tau(f'),\qquad
\|f'x_k^*x_k f'-f'\|_2\le b\sqrt{1+D^2}\sqrt{\tau(f')}.
\tag{14}
\]
For an old partial isometry \(w_j\),
\[
\|w_j^*x_k f'\|_2
\le\bigl(BD+b\sqrt{1+D^2}\bigr)\sqrt{\tau(f')}.
\tag{15}
\]
Expand \(w_j^*=(w_j^*-f'x_j^*)+f'x_j^*\), using the old error and the off-diagonal condition (10). Apply Lemma 1.2 with
\[
\beta=BD+b\sqrt{1+D^2},\qquad
\alpha=\bigl(2(k-1)B+1\bigr)\beta.
\tag{16}
\]
For small \(b\), \(\alpha<1/4\). Its new initial projection \(e\le f'\) satisfies \(\tau(f')\le\tau(e)/(1-\alpha)\). Retain the old operators as \(w_j e\). Projection differences are orthogonal, so
\[
\tau(f-e)\le\frac{D^2+\alpha}{1-\alpha}\tau(e).
\tag{17}
\]
Old errors have squared bound \(D^2\tau(e)/(1-\alpha)\), and the new error has bound \(\alpha\tau(e)\). Thus the recursive choice
\[
D_k(b)^2=\frac{D_{k-1}(b)^2+\alpha}{1-\alpha}
\tag{18}
\]
proves (11). For fixed \(m,B\), induction shows every term tends to zero; all finitely many smallness conditions can therefore be met.

For (13), insert \(x_i e,x_j e\) between the repaired operators. The two replacement errors are bounded by \(D_m(b)\sqrt{\tau(e)}\) and \(B D_m(b)\sqrt{\tau(e)}\). The compressed coefficient error is at most \(b\sqrt{\tau(f)}\), which is at most \(b\sqrt{1+D_m(b)^2}\sqrt{\tau(e)}\). Their sum proves (13). \(\square\)

<a id="1-repairing-one-partial-isometry"></a>

## Single-vector repairs and orthogonal ranges

**Lemma 1.2.** Suppose \(u_1,\ldots,u_l\) are partial isometries with \(u_i^*u_j=\delta_{ij}f\), \(f\ne0\), and \(y\in M\), \(\|y\|\le B\). Assume
\[
\|f y^*y f-f\|_2\le\beta\sqrt{\tau(f)},\qquad
\|u_j^*y f\|_2\le\beta\sqrt{\tau(f)}.
\tag{6}
\]
Put \(C=2lB+1\), and suppose \(0\le\beta<1/(4C)\). There are \(e\le f\) and \(u\) with
\[
\begin{aligned}
u^*u&=e,&u_j^*u&=0,\\
\|ye-u\|_2^2&\le C\beta\tau(e),&
\tau(f-e)&\le\frac{C\beta}{1-C\beta}\tau(e).
\end{aligned}
\tag{7}
\]
The old partial isometries \(u_j e\), together with \(u\), give an \((l+1)\)-matrix system.

**Proof.** The scalar polar-repair lemma used here is proved below. The ranges \(u_j u_j^*\) are orthogonal. Let \(P=\sum_j u_j u_j^*\) and \(x=(1-P)yf\). Then \(\|x\|\le B\),
\[
\|x-yf\|_2\le l\beta\sqrt{\tau(f)},\qquad
\|x^*x-f\|_2\le(2lB+1)\beta\sqrt{\tau(f)}.
\tag{8}
\]
For the second inequality expand the difference from \(f y^*y f\) and use the two operator norm bounds. Apply Lemma 1.1 with \(\alpha=C\beta<1/4\). Its polar range lies in \(1-P\), so \(u_j^*u=0\).

To bound \(ye-u\), its components \(Pye\) and \(xe-u\) have orthogonal ranges. Equations (5)–(6) give
\[
\|ye-u\|_2^2\le l\beta^2\tau(f)+\alpha^2\tau(f).
\tag{9}
\]
If \(\beta>0\), compression of the first condition in (6) and Cauchy–Schwarz imply \(\|y\|^2\ge1-\beta>3/4\). Thus \(B>\sqrt3/2\), and \(C^2\ge l\). Consequently the right side in (9) is at most
\[
2\alpha^2\tau(f)\le\frac{2\alpha^2}{1-\alpha}\tau(e)
\le\alpha\tau(e).
\]
For \(\beta=0\), \(yf\) already has orthogonal range and initial projection \(f\). The trace defect follows from Lemma 1.1. Setting \(w_j=u_j e\) and \(w_{l+1}=u\) gives \(w_i^*w_j=\delta_{ij}e\); their products \(w_iw_j^*\) satisfy all matrix-unit identities. \(\square\)

### Spectral polar repair

**Lemma 1.1.** Let \(f\ne0\) be a projection, \(x\in M\), and \(0\le\alpha<1/4\). If
\[
\|f x^*x f-f\|_2\le\alpha\sqrt{\tau(f)},
\tag{1}
\]
there are \(e\le f\) and a partial isometry \(u\) such that
\[
\begin{aligned}
u^*u&=e,& uu^*&\le s_\ell(xf),\\
\|xe-u\|_2^2&\le\alpha\tau(e),&
\tau(f-e)&\le\frac{\alpha}{1-\alpha}\tau(e),\\
\tau(f)&\le\frac{\tau(e)}{1-\alpha}.
\end{aligned}
\tag{2}
\]
In addition \(\|xe-u\|_2^2\le\alpha^2\tau(f)\).

**Proof.** Put \(y=xf=v h\) in polar form inside the right support \(f\), and take
\[
e=1_{[1-\sqrt\alpha,\,1+\sqrt\alpha]}(h)
\tag{3}
\]
when \(\alpha>0\). Off this interval, \(|h^2-f|\ge\sqrt\alpha(2-\sqrt\alpha)\). Spectral integration of (1) gives
\[
\tau(f-e)\le\frac{\alpha}{(2-\sqrt\alpha)^2}\tau(f)
\le\alpha\tau(f).
\tag{4}
\]
Thus \(\tau(e)\ge(1-\alpha)\tau(f)>0\). The projection \(e\) is below the support of \(h\), so \(u=ve\) has the stated supports. On \(e\), \(|h-f|\le\sqrt\alpha\), proving the first error bound in (2). Also the scalar inequality \(|t-1|\le|t^2-1|\) for \(t\ge0\) gives
\[
\|xe-u\|_2^2=\tau((h-f)^2e)\le\|h^2-f\|_2^2
\le\alpha^2\tau(f).
\tag{5}
\]
Rearrange (4) to obtain the two trace bounds. If \(\alpha=0\), then \(y^*y=f\); take \(e=f\), \(u=y\). \(\square\)

## 4. Exercises with complete solutions

### Matrix coordinates and trace budgets

**Exercise 6.** Verify the matrix multiplication rule for \(w_iw_j^*\).

*Solution.* Since \(w_j^*w_k=\delta_{jk}e\) and \(w_i e=w_i\), \((w_iw_j^*)(w_kw_l^*)=\delta_{jk}w_iw_l^*\). Taking adjoints exchanges the indices. The diagonal projections are orthogonal and sum to the identity \(s\) of this finite-dimensional algebra.

**Exercise 7.** Why must the trace conversion in (13) use \(\sqrt{1+D_m(b)^2}\)?

*Solution.* Equation (11) says \(\tau(f-e)\le D_m(b)^2\tau(e)\), so \(\tau(f)\le(1+D_m(b)^2)\tau(e)\). The coefficient estimate is a norm, and therefore converts by the square root of that trace ratio.

**Exercise 8.** Prove the matrix-coordinate squared norm identity used in (20).

*Solution.* For \(z_{ij}\in eMe\), expand \(z=\sum_{i,j}w_i z_{ij}w_j^*\). In \(\tau(z^*z)\), the relations \(w_i^*w_k=\delta_{ik}e\), followed by cyclicity and \(w_j^*w_l=\delta_{jl}e\), remove all cross terms. What remains is \(\sum_{i,j}\tau(z_{ij}^*z_{ij})\).

**Exercise 9.** Why can the \(s_k\)'s not generally be treated as an orthogonal partition?

*Solution.* Each has trace \(m\tau(e_k)\). If they were orthogonal, their total trace would be at most one. For \(m>1\), the lower bound in (19) makes \(\sum_k\tau(s_k)\) arbitrarily close to \(m\), contradicting that bound. Only the initial projections form the almost-covering orthogonal family.

**Exercise 10.** Which statements in this lesson require factoriality or separable predual?

*Solution.* The polar repairs, Gram induction and coefficient transfer in Sections 1–2 use only a faithful normal finite trace. Corollary 3.1 uses the scalar pinching theorem, so its factor and separability hypotheses are retained. Those hypotheses do not enter the individual repair lemmas.

### Scalar and range repairs

**Exercise 1.** Explain why the spectral projection in (3) lies in the support of \(h\).

*Solution.* The interval's lower endpoint \(1-\sqrt\alpha\) is positive. Thus it excludes zero, and its spectral projection is below \(1_{(0,\infty)}(h)\). The polar isometry \(v\) is isometric on that support, giving \((ve)^*(ve)=e\).

**Exercise 2.** Derive (4) with one lower bound for both bad spectral tails.

*Solution.* On the lower tail, \(1-t^2>2\sqrt\alpha-\alpha\); on the upper tail, \(t^2-1>2\sqrt\alpha+\alpha\). Both exceed \(\sqrt\alpha(2-\sqrt\alpha)\). Integrating their squared lower bound against the spectral trace measure and applying (1) gives (4).

**Exercise 3.** Why are both estimates for \(xe-u\) useful?

*Solution.* The pointwise cutoff gives the relative bound \(\alpha\tau(e)\). The global estimate gives the smaller squared quantity \(\alpha^2\tau(f)\). In Lemma 1.2 this second estimate leaves enough room for the additional discarded-range component \(Pye\), so the final bound still has coefficient \(C\beta\).

**Exercise 4.** Verify the orthogonal decomposition in (9).

*Solution.* The vector \(Pye\) has left support in \(P\). Both \(xe\) and \(u\) have left support in \(1-P\). Their trace inner product is therefore zero. Pythagoras gives the sum of squared norms. Furthermore \(\|Pye\|_2^2=\sum_j\|u_j^*ye\|_2^2\le l\beta^2\tau(f)\).

**Exercise 5.** Check why \(C^2\ge l\) follows from the hypotheses of Lemma 1.2.

*Solution.* Compress the self-Gram error to \(f\) and pair with \(f\). This gives \(\tau(fy^*yf)\ge(1-\beta)\tau(f)\), hence \(B^2\ge1-\beta>3/4\). Therefore \(C=2lB+1\ge l+1\) for \(l\ge1\), which implies \(C^2\ge l\). For \(l=0\) it is immediate.

## References and proof scope

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*, author draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf), Lemmas 11.1.12–11.1.16 and Remark 11.1.13, pp.180–181. The scalar spectral and polar estimates lead there to a successive range-removal induction for an almost orthonormal family. The full recursive proof here includes the discarded-range estimate, its trace-loss recurrence and the coefficient-transfer bound with the square-root trace ratio.

The simultaneous proof cuts the sum of the squared Gram defects inside the original corner. It then normalizes the full compressed Gram matrix by its inverse square root. A finite matrix-trace identity bounds the sum of all column errors. For \(0<b<1/(4m^2)\), the explicit choice \(D_m(b)^2=m^2b/(1-m^2b)\) satisfies every original trace-loss, vector-error and coefficient-transfer requirement. The construction applies to arbitrary finite faithfully tracial algebras.

Sorin Popa, [*A short proof of “injectivity implies hyperfiniteness” for finite von Neumann algebras*](https://www.theta.ro/jot/archive/1986-016-002/1986-016-002-005.pdf), *Journal of Operator Theory* 16 (1986), 261–272. Its deformation of almost orthonormal vectors is part of the same matrix-corner method. Its initial vectors are orthonormal over an abelian algebra. The almost-covering initial projections of Corollary 3.1 here instead come from the complete [global scalar-pinching selection](invariant-states-and-finite-rank-projections.md#lemma-3-1), with its separable \(\mathrm{II}_1\) factor hypotheses retained. Only the initial projections are asserted orthogonal across the family; the matrix range supports may overlap.


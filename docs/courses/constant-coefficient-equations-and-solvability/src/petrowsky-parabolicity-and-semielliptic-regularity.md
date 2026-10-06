# Petrowsky parabolicity and semielliptic regularity

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Parabolicity can be expressed through the roots of a polynomial in the time-growth rate. The roots describe what happens to a spatial Fourier mode as time increases. A strict half-plane condition also prevents the full real Fourier symbol from vanishing away from the origin. This connects parabolic evolution to semiellipticity and gives precise local derivative bounds, even when the equation has several time derivatives.

Read [Algebraic families of hypoelliptic operators](algebraic-families-of-hypoelliptic-operators.md) for semielliptic symbols and their derivative-ratio estimates. [Directional growth and complex-zero geometry](directional-growth-and-complex-zero-geometry.md) proves their optimal directional exponents, and [Anisotropic derivative classes and analyticity](anisotropic-derivative-classes-and-analyticity.md) turns those exponents into mixed derivative bounds. Hile [Hile] supplies a higher time-order convention for the parabolic root condition. We give the inclusion proof and the applications below.

## A polynomial in the time-growth rate

Let \(x\in\mathbb R^d\), \(t\in\mathbb R\), with \(d\geq1\). Choose positive integers \(p,q\). We consider the scalar constant-coefficient operator
\[
\begin{aligned}
L&=c_0\partial_t^q+
 \sum_{j=1}^q\ \sum_{|\alpha|\leq pj}
 a_{j,\alpha}\partial_x^\alpha\partial_t^{q-j},\\
c_0&\in\mathbb C\setminus\{0\},\qquad a_{j,\alpha}\in\mathbb C.
\end{aligned}
\tag{1}
\]
The original leading coefficient \(c_0\) is retained. If we compare with the monic operator \(\widehat L=c_0^{-1}L\), the full equation transforms as
\[
Lu=g\quad\Longleftrightarrow\quad
\widehat Lu=c_0^{-1}g.
\tag{1a}
\]
The homogeneous solutions agree, and the source acquires the same reciprocal factor as the operator.

Retain the terms of maximal anisotropic degree and define
\[
\begin{aligned}
b_j(\xi)&=\sum_{|\alpha|=pj}a_{j,\alpha}(i\xi)^\alpha,\\
F(\lambda,\xi)&=c_0\lambda^q+
 \sum_{j=1}^q b_j(\xi)\lambda^{q-j}.
\end{aligned}
\tag{2}
\]
For a spatial mode \(e^{ix\cdot\xi}\), the principal equation becomes the ordinary differential equation obtained by replacing \(\lambda\) with \(\partial_t\). Thus \(F(\lambda,\xi)=0\) identifies exponential time factors \(e^{\lambda t}\); repeated roots can also produce polynomial factors in \(t\).

**Definition 1.** We say that (1) is **strictly \(p\)-parabolic in the forward time direction** if there is \(c>0\) such that
\[
\begin{gathered}
F(\lambda,\omega)=0,\quad
\omega\in\mathbb R^d,\quad |\omega|=1\\
\Longrightarrow\quad \operatorname{Re}\lambda\leq-c.
\end{gathered}
\tag{3}
\]
This is a condition on the principal polynomial (2). Terms with \(|\alpha|<pj\) do not enter it.

To compare Fourier conventions, put
\[
f(\tau,\xi)=\frac{i^{-q}}{c_0}F(i\tau,\xi).
\tag{4}
\]
The polynomial \(f\) is monic in \(\tau\). Its roots correspond to the roots of \(F\) through \(\lambda=i\tau\), and
\[
\operatorname{Re}\lambda=-\operatorname{Im}\tau.
\tag{5}
\]
Consequently (3) says that the roots of \(f(\,\cdot\,,\omega)\) satisfy \(\operatorname{Im}\tau\geq c\). For the precise operator comparison with [Hile, Example 8.3], let \(L^\circ\) retain only the terms with \(|\alpha|=pj\), together with the leading temporal term. Hile's scalar principal convention is
\[
\begin{aligned}
L_H&=\frac{i^{-q}}{c_0}L^\circ,\\
A^H_{0,q}&=i^{-q},\\
A^H_{\alpha,q-j}&=\frac{i^{-q}}{c_0}a_{j,\alpha},
\qquad |\alpha|=pj.
\end{aligned}
\tag{5a}
\]
Its Fourier polynomial is exactly (4). This comparison concerns the anisotropic principal operator; the full \(L\) still contains every lower term in (1). The signs agree with the decaying factors of the forward heat equation.

**Lemma 1.1.** Condition (3) is equivalent to requiring that every root have strictly negative real part for each real unit \(\omega\). Moreover,
\[
\begin{gathered}
F(\lambda,\xi)=0,\quad \xi\in\mathbb R^d\setminus\{0\}\\
\Longrightarrow\quad
\operatorname{Re}\lambda\leq-c|\xi|^p
\end{gathered}
\tag{6}
\]
with the same \(c\) as in (3).

**Proof.** The coefficients \(b_j\) are bounded on the unit sphere. Set
\[
B=\max_{|\omega|=1}\sum_{j=1}^q\frac{|b_j(\omega)|}{|c_0|}.
\]
If \(|\lambda|>\max(1,B)\), then
\[
\sum_{j=1}^q|b_j(\omega)\lambda^{q-j}|
\leq |c_0|B|\lambda|^{q-1}<|c_0||\lambda|^q.
\]
Such a \(\lambda\) cannot be a root. All roots on the unit sphere therefore lie in a fixed compact disk.

Suppose every one of these roots has negative real part, but there is no uniform \(c\). Choose unit vectors \(\omega_\nu\) and roots \(\lambda_\nu\) with \(\operatorname{Re}\lambda_\nu\to0\). Pass to convergent subsequences of both. Continuity gives a root \(F(\lambda,\omega)=0\) with \(|\omega|=1\) and \(\operatorname{Re}\lambda=0\), a contradiction. This proves the uniform condition. Its converse is immediate.

Each \(b_j\) is homogeneous of spatial degree \(pj\), so
\[
F(s^p\lambda,s\xi)=s^{pq}F(\lambda,\xi),
\qquad s>0.
\tag{7}
\]
For \(\xi\ne0\), take \(s=|\xi|\) and \(\omega=\xi/s\). A root \(\lambda\) at \(\xi\) becomes the root \(\lambda/s^p\) at \(\omega\). Applying (3) proves (6). No labeling or simplicity of the roots is required. \(\square\)

The uniform root gap concerns high spatial frequencies through (7). For example, the lower term \(-1\) in \(\partial_t-\Delta_x-1\) permits growth at low frequencies, while its principal polynomial still satisfies (3).

## Why the root condition gives semiellipticity

We use \(D=-i\partial\) and order the real Fourier variables as \((\tau,\xi)\), with time first. Then \(L=P(D_t,D_x)\), where
\[
\begin{aligned}
P(\tau,\xi)&=c_0(i\tau)^q\\
&+\sum_{j=1}^q\ \sum_{|\alpha|\leq pj}
 a_{j,\alpha}(i\xi)^\alpha(i\tau)^{q-j}.
\end{aligned}
\tag{8}
\]
Choose the semielliptic weights
\[
\mathbf m=(q,pq,\ldots,pq).
\tag{9}
\]
A monomial in (8) has anisotropic degree
\[
\frac{q-j}{q}+\frac{|\alpha|}{pq}\leq1,
\tag{10}
\]
with equality precisely when \(|\alpha|=pj\). Thus the anisotropic principal part is
\[
P^\circ(\tau,\xi)=F(i\tau,\xi).
\tag{11}
\]

**Theorem 2.1.** Every operator satisfying (3) is semielliptic with weights (9), and hence hypoelliptic. Arbitrary lower anisotropic degree terms allowed in (1) preserve this conclusion. Its ordinary differential order is exactly \(pq\).

**Proof.** Let \((\tau,\xi)\) be a nonzero real vector. If \(\xi\ne0\) and \(P^\circ(\tau,\xi)=0\), then \(i\tau\) is a root of \(F(\,\cdot\,,\xi)\). Its real part is zero, contradicting (6). If \(\xi=0\), every \(b_j(0)\) vanishes and
\[
P^\circ(\tau,0)=c_0(i\tau)^q.
\]
This is nonzero when \(\tau\ne0\), since \(c_0\ne0\). We have proved nonvanishing on every nonzero real vector, exactly the definition of semiellipticity for (9).

For completeness, the regularity mechanism can be seen directly. Define
\[
R(\tau,\xi)=|\tau|^q+\sum_{\ell=1}^d|\xi_\ell|^{pq}.
\tag{12}
\]
Its unit level set is compact and avoids zero. The anisotropic dilation
\[
\delta_s(\tau,\xi)
=(s^{1/q}\tau,s^{1/(pq)}\xi)
\tag{13}
\]
makes both \(P^\circ\) and \(R\) homogeneous of degree one. Retain the constant for the original operator,
\[
a_L=\min_{R(\tau,\xi)=1}|P^\circ(\tau,\xi)|>0.
\tag{13a}
\]
This gives
\[
|P^\circ(\tau,\xi)|\geq a_LR(\tau,\xi)
\tag{14}
\]
A lower monomial of anisotropic degree \(\theta<1\), with its original coefficient \(a_{j,\alpha}\), is bounded by \(|a_{j,\alpha}|R^\theta\). The finite sum of those bounds is at most \(a_LR/2\) for sufficiently large \(R\). Therefore
\[
|P(\tau,\xi)|\geq \frac {a_L}2 R(\tau,\xi).
\tag{15}
\]
If \(a_0\) is a nonnegative integer and \(\beta\) is a spatial multi-index, put
\[
\theta(a_0,\beta)=\frac{a_0}{q}+\frac{|\beta|}{pq}.
\]
Differentiating a surviving monomial retains its original coefficient and reduces its anisotropic degree by \(\theta(a_0,\beta)\). Hence, when \(\theta\leq1\),
\[
\left|\frac{\partial_\tau^{a_0}\partial_\xi^\beta P}{P}\right|
\leq C_{a_0,\beta}R^{-\theta(a_0,\beta)}
\tag{16}
\]
for large \(R\). When \(\theta>1\), that derivative is zero. Every positive derivative ratio therefore tends to zero as \(|(\tau,\xi)|\to\infty\). The complex-zero criterion proved in [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) gives hypoellipticity. This also explains why all lower anisotropic terms are allowed.

Each monomial in (8) has ordinary degree at most
\[
|\alpha|+q-j\leq pj+q-j\leq pq.
\]
For any spatial coordinate vector \(e_\ell\), semiellipticity gives
\[
P^\circ(0,e_\ell)=b_q(e_\ell)\ne0.
\]
This requires a nonzero pure spatial term of degree \(pq\). The ordinary order is therefore exactly \(pq\). \(\square\)

Hypoellipticity means that \(Lu\) smooth on an open set forces the distribution \(u\) to be smooth there. The theorem concerns this local regularity; the root orientation records additional information about time evolution.

## The scalar condition forces an even spatial scale

Complex coefficients are allowed, but the scalar root condition still constrains \(p\).

**Proposition 3.1.** If \(d\geq1\) and (3) holds, then \(p\) is even. In particular, \(p\geq2\).

**Proof.** For a real unit vector \(\omega\), list the \(q\) roots with multiplicity as \(\lambda_1,\ldots,\lambda_q\). The coefficient of \(\lambda^{q-1}\) in (2) and Viète's formula give
\[
\lambda_1+\cdots+\lambda_q=-\frac{b_1(\omega)}{c_0}.
\]
Taking real parts and using (3) yields
\[
\operatorname{Re}\frac{b_1(\omega)}{c_0}\geq qc>0.
\tag{17}
\]
But \(b_1\) is homogeneous of degree \(p\), so
\[
b_1(-\omega)=(-1)^p b_1(\omega).
\]
If \(p\) were odd, (17) at \(\omega\) and \(-\omega\) would demand positive real parts for a number and its negative. This is impossible. \(\square\)

This argument uses a scalar polynomial with nonzero leading coefficient and counts all temporal roots. It also shows that a strictly parabolic scalar principal polynomial must have a nonzero coefficient of \(\lambda^{q-1}\).

## Exact time and space derivative classes

Let \(X\subset\mathbb R^{d+1}\) be open and let \(Lu=0\) in \(\mathcal D'(X)\). Theorem 2.1 first makes \(u\) smooth. The semielliptic exponents and mixed derivative theorem then give the following more precise conclusion.

**Corollary 4.1.** For every compact \(K\subset X\), there is \(C_K\geq1\) such that
\[
\begin{gathered}
\sup_K|\partial_t^a\partial_x^\beta u|
\leq C_K^{a+|\beta|+1}(a!)^p\beta!,\\
a\geq0,\qquad
\beta!=\prod_{\ell=1}^d\beta_\ell!.
\end{gathered}
\tag{18}
\]
The optimal directional growth exponents are
\[
\rho_P(y)=
\begin{cases}
p,&y_t\ne0,\\
1,&y_t=0,\ y_x\ne0,\\
0,&y=0.
\end{cases}
\tag{19}
\]
In particular, all coordinate exponents in (18) are sharp in the universal homogeneous-solution sense.

**Proof.** The ordinary order is \(m=pq\), and the weights are (9). The exact semielliptic result in [Directional growth and complex-zero geometry](directional-growth-and-complex-zero-geometry.md), Theorem 4.1, gives the coordinate exponents
\[
\rho_t=\frac{pq}{q}=p,\qquad
\rho_{x_\ell}=\frac{pq}{pq}=1.
\]
For a nonzero direction it gives the maximum of the exponents among its nonzero coordinates, proving (19). The total dimension \(d+1\) is at least two, so the universal sharp lower bounds in that lesson apply.

Apply the mixed derivative theorem in [Anisotropic derivative classes and analyticity](anisotropic-derivative-classes-and-analyticity.md), Theorem 1.1, and its factorial formulation. Replacing \(D\) by ordinary derivatives only changes factors of modulus one. This proves (18). \(\square\)

For each fixed \(t\), the restriction of a homogeneous solution to a spatial slice is real analytic. Indeed, take a small compact product neighborhood inside \(X\), set \(a=0\) in (18), and apply the Taylor remainder argument for exponent one. In time, (18) gives a Gevrey bound of order \(p\). Sharpness is a statement about a bound for all local homogeneous solutions, with constants that may depend on the individual solution. Individual solutions, including exponentials and polynomials, can have better bounds.

The full operator is not elliptic in the ordinary sense. Since \(p\geq2\), its ordinary degree is \(pq>q\). All terms of ordinary degree \(pq\) in (8) have \(j=q\) and are purely spatial. The ordinary principal part therefore vanishes at \((\tau,\xi)=(1,0)\). By the analyticity criterion proved in the preceding lesson, some local homogeneous solutions fail to be jointly real analytic, despite their spatial analyticity.

## Repeated roots and the direction of time

For \(r,q\geq1\), consider the monic specialization \(c_0=1\),
\[
L=\bigl(\partial_t+(-\Delta_x)^r\bigr)^q.
\tag{20}
\]
Here \(p=2r\) and
\[
F(\lambda,\xi)=\bigl(\lambda+|\xi|^{2r}\bigr)^q.
\]
All \(q\) roots equal \(-|\xi|^{2r}\). On the unit sphere the strict condition holds with \(c=1\), even though the roots have multiplicity \(q\). The weights are \(q\) in time and \(2rq\) in space; the derivative exponents are \(2r\) in time and one in space. The temporal multiplicity changes the weights and ordinary order, but their ratios stay the same.

Semiellipticity does not by itself choose a forward time direction. The backward heat operator
\[
L_{\mathrm b}=\partial_t+\Delta_x
\tag{21}
\]
has \(F_{\mathrm b}(\lambda,\xi)=\lambda-|\xi|^2\), whose root is positive when \(\xi\ne0\). It fails (3). Yet its Fourier symbol \(i\tau-|\xi|^2\) has no nonzero real zero and is semielliptic with weights \((1,2,\ldots,2)\). Thus the inclusion in Theorem 2.1 is strict.

## Exercises with complete solutions

**Exercise 1 (basic: Fourier signs).** For \(L=\partial_t-\Delta_x\), compute \(F\), \(P\), and the normalized \(f\) in (4). Locate the roots in the \(\lambda\)- and \(\tau\)-planes and identify a decaying spatial Fourier mode.

**Solution.** We have
\[
\begin{aligned}
F(\lambda,\xi)&=\lambda+|\xi|^2,\\
P(\tau,\xi)&=i\tau+|\xi|^2,\\
f(\tau,\xi)&=\tau-i|\xi|^2.
\end{aligned}
\]
The roots are \(\lambda=-|\xi|^2\) and \(\tau=i|\xi|^2\). Their signs agree with \(\lambda=i\tau\). The function
\[
e^{ix\cdot\xi-t|\xi|^2}
\]
solves the equation and decays for increasing \(t\) when \(\xi\ne0\). Here \(p=2,q=1\).

**Exercise 2 (intermediate: uniformity without simple roots).** Retain any \(c_0\ne0\). Suppose the coefficients \(b_j\) in (2) are continuous on the real unit sphere, and every temporal root there has strictly negative real part. Prove the existence of one positive gap \(c\) without choosing continuous root branches.

**Solution.** Compactness of the sphere bounds \(\sum_j|b_j|/|c_0|\) by \(B\). The leading-term comparison in Lemma 1.1 bounds every root by \(\max(1,B)\). If no gap existed, for each integer \(\nu\) there would be a unit \(\omega_\nu\) and a root \(\lambda_\nu\) with
\[
-1/\nu<\operatorname{Re}\lambda_\nu<0.
\]
Extract convergent subsequences in the sphere and disk. Continuity of the polynomial gives a root at the limit with real part zero, contradicting the hypothesis. This proof accommodates multiple roots.

**Exercise 3 (intermediate: lower terms and ordinary order).** In two spatial dimensions, take
\[
\begin{aligned}
L&=(\partial_t-\Delta_x)^2\\
&+3\partial_{x_1}\partial_t+7\partial_{x_2}^3+5.
\end{aligned}
\tag{22}
\]
Identify \(p,q\), all anisotropic degrees of the added terms, the ordinary order, and the mixed factorial bound for homogeneous solutions.

**Solution.** The principal factor has \(p=2,q=2\), so the weights are \((2,4,4)\). The added terms have degrees \(1/2+1/4=3/4\), \(3/4\), and zero. They are all below one. The principal temporal polynomial is
\[
F(\lambda,\xi)=(\lambda+|\xi|^2)^2.
\]
Its unit-frequency roots are both \(-1\), so the equation is strictly \(2\)-parabolic. Its ordinary order is four, from the \(\Delta_x^2\) term. For \(K\) compactly contained in the open domain,
\[
\sup_K|\partial_t^a\partial_{x_1}^b\partial_{x_2}^c u|
\leq C_K^{a+b+c+1}(a!)^2b!c!.
\]
The arbitrary signs of the displayed lower terms have no effect on this local conclusion.

**Exercise 4 (advanced: an excluded temporal polynomial).** Show that
\[
F(\lambda,\xi)=\lambda^2+|\xi|^4
\]
does not satisfy the strict root condition. Find nonzero real zeros of \(F(i\tau,\xi)\). Explain why the missing coefficient of \(\lambda\) already rules out strict parabolicity.

**Solution.** For \(\xi\ne0\), the roots are
\[
\lambda=\pm i|\xi|^2,
\]
both with real part zero. Also
\[
F(i\tau,\xi)=-\tau^2+|\xi|^4
\]
vanishes when \(\tau=\pm|\xi|^2\), so the proposed weights do not give a semielliptic principal part. Viète's formula says the two roots sum to zero because \(b_1=0\). Two roots with strictly negative real parts cannot have sum zero. Thus the trace-of-roots argument detects failure before solving the quadratic.

**Exercise 5 (advanced: time reversal).** Let \(L\) satisfy (3), and let \(L^{\mathrm r}\) be the operator acting on \(v(t,x)=u(-t,x)\) obtained by replacing \(\partial_t\) with \(-\partial_t\) in \(L\) and then multiplying by \((-1)^q\) to restore the original leading coefficient \(c_0\). Determine its principal temporal roots. Prove that it remains semielliptic but fails the forward strict condition.

**Solution.** Reflection alone gives \(F(-\lambda,\xi)\) with leading coefficient \((-1)^qc_0\). The additional factor restores \(c_0\), so the principal temporal polynomial is
\[
F^{\mathrm r}(\lambda,\xi)=(-1)^q F(-\lambda,\xi).
\]
Its roots are the negatives of those of \(F\), including multiplicities. On the unit sphere they have real parts at least \(c>0\), so they fail (3). The corresponding anisotropic principal Fourier part is
\[
P^{\mathrm r,\circ}(\tau,\xi)=(-1)^qP^\circ(-\tau,\xi).
\]
Reflection in the real \(\tau\) coordinate and multiplication by a nonzero constant preserve nonvanishing on nonzero real vectors. It is therefore semielliptic with the same weights. The derivative classes depend on these weights and remain the same. If \(Lu=g\) and \(v(t,x)=u(-t,x)\), then
\[
L^{\mathrm r}v(t,x)=(-1)^q g(-t,x).
\]
An additional monic comparison would divide both this operator and this source by \(c_0\).

**Exercise 6 (advanced: sharpness despite temporal multiplicity).** In one spatial dimension, let
\[
L=(\partial_t+\partial_x^4)^3.
\]
Compute the principal polynomial, the weights, and every directional exponent. Show that a proposed bound
\[
\sup_K|\partial_t^j u|\leq C_u^{j+1}(j!)^s
\]
for all local homogeneous solutions requires \(s\geq4\). Identify a homogeneous solution that has better growth.

**Solution.** Since the Fourier symbol of \(\partial_x^4\) is \(\xi^4\),
\[
F(\lambda,\xi)=(\lambda+\xi^4)^3.
\]
We have \(p=4,q=3\), weights \((3,12)\), and ordinary order twelve. The exponents are four for any direction with nonzero time component, one for a nonzero purely spatial direction, and zero for the zero direction.

The sharp universal lower bound from the directional-growth theorem says that a valid positive sequence \(M_j\) in a bound \(C_u^{j+1}M_j\) must satisfy
\[
M_j\geq a^j j^{4j}
\]
for some \(a>0\). If \(M_j=(j!)^s\) with \(0\leq s<4\), then \(j!\leq j^j\) would imply
\[
j^{(4-s)j}\leq a^{-j},
\]
which fails for large \(j\). If \(s<0\), use \((j!)^s\leq1\), and the same lower bound again fails. Therefore \(s\geq4\). The individual solution \(u=1\) has all positive derivatives zero; it satisfies much stronger estimates. Universal sharpness does not assign the worst growth to every solution.

## References

[Hile] G. N. Hile, *Fundamental Solutions and Mapping Properties of Semielliptic Operators* (2004), [primary paper](https://arxiv.org/abs/math/0406202), Example 8.3 for the higher time-order parabolic convention.

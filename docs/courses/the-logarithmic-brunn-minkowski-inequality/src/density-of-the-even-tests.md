# Density of the even tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The tensor estimate is an inequality for the functions \(u=A(A-1)f\), where \(f\) is a test function. To use it for other functions one must know which functions are limits of such \(u\). The operator \(A(A-1)\) annihilates the affine functions, and by its symmetry every \(u\) is orthogonal to them. This lesson proves that there is no other restriction: if the pair is even and the Hessian \(\tau\) is bounded, the functions \(A(A-1)f\) with \(f\) even are dense in the space of the even square-integrable functions with mean zero. Evenness removes the linear functions, and the mean zero removes the constants.

- The statement (Theorem 1.1) and the hypothesis (ER) on elliptic regularity.
- Cutoff functions (Lemma 2.1).
- A function orthogonal to all tests is smooth and satisfies \(A(A-1)g=0\) (Lemma 3.1).
- Then \(Ag\) is square integrable (Lemma 4.1), and \(g\) is affine (Proposition 5.1).

The lesson follows [OpenAI-L, Section 5]. It continues [Moment coordinates and their adjoints](moment-coordinates-and-their-adjoints.md) and uses its notation and results.

## 1. The statement

Let \((V,\varphi)\) be a moment pair on \(\mathbb R^n\) in which \(V\) and \(\varphi\) are even, and assume that
\[
\tau\le\Lambda I\qquad\text{at every point,}
\]
for a number \(\Lambda\). This is the situation of the hypothesis (M), with \(\Lambda=4/\varepsilon\). Since \(\varphi\) is even, the map \(x=\nabla\varphi(z)\) is odd, and so is its inverse; hence \(\tau\), as a function of \(x\), is even. The operator
\[
\begin{gathered}
Af=x\cdot\nabla f-\tau{:}D^2f,\\
\tau{:}D^2f=\sum_{i,k}\tau_{ik}f_{x_ix_k},
\end{gathered}
\]
therefore maps even functions to even functions and odd functions to odd functions. In this lesson all functions are functions of \(x\), \(\nabla=\nabla_x\), \(\mathbb E\) is the mean for \(\mu\), \(\|g\|\) is the norm of \(L^2(\mu)\), and \(\Gamma(f,g)=\nabla f\cdot\tau\nabla g\), \(\Gamma(f)=\Gamma(f,f)\). Since \(\tau\) is positive definite,
\[
|\Gamma(f,g)|\le\Gamma(f)^{1/2}\,\Gamma(g)^{1/2}.
\]
We write \(\mathcal P=A(A-1)\), so that \(\mathcal Pf=A(Af)-Af\).

**Hypothesis (ER).** Let \(\mathcal Q\) be a linear differential operator of order \(4\) on \(\mathbb R^n\) with smooth coefficients, whose principal symbol \(q_4(x,\xi)\) is positive for all \(x\) and all \(\xi\ne0\). Let \(g\) be a locally square-integrable function with \(\int g\,\mathcal Q\chi\,dx=0\) for every smooth function \(\chi\) with compact support. Then \(g\) is equal almost everywhere to a smooth function.

This is the interior regularity theorem for elliptic operators, applied to the transposed operator of \(\mathcal Q\). It is not proved in this course.

**Theorem 1.1 (density).** Assume (ER). In the situation above, the functions \(\mathcal Pf\), where \(f\) runs through the even smooth functions with compact support, are dense in the space of the even functions \(g\in L^2(\mu)\) with \(\mathbb E\,g=0\).

Each \(\mathcal Pf\) lies in this space: it is even, and \(\mathbb E\,A(Af-f)=0\) by Proposition 3.1 (2) of the lesson on moment coordinates. The space is a closed subspace of \(L^2(\mu)\). So the theorem follows if every \(g\) in it that is orthogonal to all \(\mathcal Pf\) is \(0\). Sections 2 to 5 prove this.

## 2. Cutoff functions

Fix a smooth function \(\eta\) on \(\mathbb R^n\) with \(0\le\eta\le1\), \(\eta=1\) for \(|x|\le1\) and \(\eta=0\) for \(|x|\ge2\), and let \(\eta_r(x)=\eta(x/r)\) for \(r\ge1\).

**Lemma 2.1.** There are numbers \(B\) and \(K\), which do not depend on \(r\ge1\), with
\[
\Gamma(\eta_r)\le\frac{B^2}{r^2},\qquad|A\eta_r|\le K .
\]
Both functions vanish where \(|x|<r\) and where \(|x|>2r\).

**Proof.** Let \(c_1\) and \(c_2\) bound the first and the second derivatives of \(\eta\). Then \(|\nabla\eta_r|\le c_1/r\) and the second derivatives of \(\eta_r\) are at most \(c_2/r^2\). So \(\Gamma(\eta_r)\le\Lambda c_1^2/r^2\). Where the derivatives of \(\eta_r\) do not vanish, \(|x|\le2r\), so \(|x\cdot\nabla\eta_r|\le2c_1\), and \(|\tau{:}D^2\eta_r|\le n^2\Lambda c_2\). \(\blacksquare\)

This lemma is the only place where the bound \(\Lambda\) for \(\tau\) is used.

## 3. The orthogonal complement

**Lemma 3.1.** Assume (ER). Let \(g\in L^2(\mu)\) be even and orthogonal to \(\mathcal Pf\) for every even smooth \(f\) with compact support. Then \(g\) is smooth, and \(\mathcal Pg=0\) at every point.

**Proof.** A smooth function \(f\) with compact support is the sum of an even and an odd one. For the odd part, \(\mathcal Pf\) is odd and \(g\) is even, so \(\mathbb E\,g\,\mathcal Pf=0\). Hence \(\mathbb E\,g\,\mathcal Pf=0\) for all smooth \(f\) with compact support, that is,
\[
\int g\,\varrho\,\mathcal Pf\,dx=0,\qquad\varrho=Z^{-1}e^{-V}.
\]
The operator \(\mathcal Qf=\varrho\,\mathcal Pf\) has smooth coefficients and the order \(4\). The terms of the highest order of \(A\) are \(-\tau_{ik}\partial_{x_i}\partial_{x_k}\), so the principal symbol of \(\mathcal Q\) is \(\varrho(x)\,(\xi\cdot\tau(x)\xi)^2\), which is positive for \(\xi\ne0\). The function \(g\) is locally square integrable for the Lebesgue measure, because \(\varrho\) is bounded below on bounded sets. By (ER), \(g\) is smooth.

For smooth \(g\) and \(f\) with compact support, Proposition 3.1 (2) of the lesson on moment coordinates, applied twice, gives \(\mathbb E\,g\,\mathcal Pf=\mathbb E\,(\mathcal Pg)\,f\). So \(\mathbb E\,(\mathcal Pg)f=0\) for all such \(f\), and the continuous function \(\mathcal Pg\) vanishes. \(\blacksquare\)

From here on, \(g\) is a smooth function in \(L^2(\mu)\) with \(\mathcal Pg=0\). Let
\[
v=Ag .
\]
It is smooth, and \(Av-v=\mathcal Pg=0\).

## 4. The function \(Ag\) is square integrable

**Lemma 4.1.** \(v\in L^2(\mu)\), and \(\mathbb E\,\Gamma(g)<\infty\).

**Proof.** Let \(r\ge1\), \(\eta=\eta_r\), and
\[
\begin{gathered}
G=\|g\|,\qquad X=\|\eta^2v\|,\\
Y=\bigl(\mathbb E\,\eta^2\Gamma(g)\bigr)^{1/2}.
\end{gathered}
\]
The last two are finite because \(\eta\) has compact support.

*First inequality.* The function \(\eta^4g\) has compact support. By the symmetry of \(A\) and \(Av-v=0\),
\[
\begin{aligned}
&\mathbb E\,v\,\bigl(A(\eta^4g)-\eta^4g\bigr)\\
&\quad=\mathbb E\,(Av-v)\,\eta^4g=0 .
\end{aligned}
\]
By the product rule and the chain rule of Proposition 3.1 (4) of the lesson on moment coordinates,
\[
\begin{aligned}
&A(\eta^4g)-\eta^4g\\
&\quad=\eta^4v+g\,E_r-8\eta^3\,\Gamma(\eta,g),\\
&E_r=4\eta^3A\eta-12\eta^2\Gamma(\eta)-\eta^4 .
\end{aligned}
\]
By Lemma 2.1, \(|E_r|\le a\,\eta^2\) with \(a=4K+12B^2+1\). So
\[
\begin{aligned}
X^2&=\mathbb E\,\eta^4v^2\\
&=-\mathbb E\,v\,g\,E_r+8\,\mathbb E\,v\,\eta^3\,\Gamma(\eta,g)\\
&\le a\,X\,G+8\,X\,\frac Br\,Y ,
\end{aligned}
\]
where the last term was bounded with \(|\Gamma(\eta,g)|\le\Gamma(\eta)^{1/2}\Gamma(g)^{1/2}\) and the inequality of Cauchy and Schwarz. Hence
\[
X\le a\,G+\frac{8B}r\,Y .
\]

*Second inequality.* By Proposition 3.1 (2) of that lesson, \(\mathbb E\,\eta^2g\,Ag=\mathbb E\,\Gamma(\eta^2g,g)\), and \(\Gamma(\eta^2g,g)=\eta^2\Gamma(g)+2\eta g\,\Gamma(\eta,g)\). So
\[
\begin{aligned}
Y^2&=\mathbb E\,\eta^2g\,v-2\,\mathbb E\,\eta\,g\,\Gamma(\eta,g)\\
&\le G\,X+\frac{2B}r\,G\,Y .
\end{aligned}
\]

Insert the first inequality into the second and use \(r\ge1\): \(Y^2\le a\,G^2+10\,B\,G\,Y\). So \(Y\le(10B+\sqrt a)\,G\), and then \(X\le(a+8B(10B+\sqrt a))\,G\). These bounds do not depend on \(r\). As \(r\to\infty\), \(\eta_r\) increases to \(1\), and by monotone convergence \(\|v\|\) and \(\mathbb E\,\Gamma(g)\) are finite. \(\blacksquare\)

## 5. The function is affine

**Proposition 5.1.** Let \(g\) be a smooth function in \(L^2(\mu)\) with \(\mathcal Pg=0\). Then \(g\) is affine: \(g(x)=c+\ell\cdot x\).

**Proof.** Let \(v=Ag\) and \(w=g-v\). By Lemma 4.1 both are in \(L^2(\mu)\); and \(Av=v\), \(Aw=Ag-Av=0\).

*The function \(w\) is constant.* For \(\eta=\eta_r\),
\[
\begin{aligned}
0&=\mathbb E\,\eta^2w\,Aw\\
&=\mathbb E\,\eta^2\Gamma(w)+2\,\mathbb E\,\eta\,w\,\Gamma(\eta,w),
\end{aligned}
\]
so \(\mathbb E\,\eta^2\Gamma(w)\le2\|w\|\tfrac Br(\mathbb E\,\eta^2\Gamma(w))^{1/2}\), that is,
\[
\bigl(\mathbb E\,\eta_r^2\,\Gamma(w)\bigr)^{1/2}\le\frac{2B}r\,\|w\| .
\]
Let \(r\to\infty\): \(\Gamma(w)=0\) everywhere. Since \(\tau\) is positive definite, \(\nabla w=0\).

*The function \(v\) is linear.* In the same way, from \(\mathbb E\,\eta^2v\,Av=\mathbb E\,\eta^2v^2\),
\[
\begin{aligned}
\mathbb E\,\eta^2\Gamma(v)&\le\|v\|^2\\
&\quad+\frac{2B}r\,\|v\|\,\bigl(\mathbb E\,\eta^2\Gamma(v)\bigr)^{1/2},
\end{aligned}
\]
so \(\mathbb E\,\eta_r^2\Gamma(v)\) is bounded in \(r\), and \(\mathbb E\,\Gamma(v)<\infty\). Let \(f_r=\eta_rv\), a smooth function with compact support. Then \(f_r\to v\) in \(L^2(\mu)\), and
\[
Af_r=\eta_r\,v+v\,A\eta_r-2\,\Gamma(\eta_r,v).
\]
The first term tends to \(v\) in \(L^2(\mu)\). The second has a norm of at most \(K\) times the norm of \(v\) on the set where \(|x|\ge r\), which tends to \(0\). The third has a norm of at most \(\tfrac{2B}r(\mathbb E\,\Gamma(v))^{1/2}\). So \(Af_r\to v\) in \(L^2(\mu)\). By the Hessian identity, Proposition 4.1 (4) of the lesson on moment coordinates,
\[
\begin{aligned}
&\mathbb E\,\bigl\|\tau^{1/2}D^2f_r\,\tau^{1/2}\bigr\|^2\\
&\quad=\|Af_r\|^2-\mathbb E\,f_r\,Af_r\\
&\quad\longrightarrow\|v\|^2-\|v\|^2=0 .
\end{aligned}
\]
On a ball \(|x|<r_0\), \(f_r=v\) for all \(r\ge r_0\). So the integral of \(\|\tau^{1/2}D^2v\,\tau^{1/2}\|^2\) over this ball, for \(\mu\), is \(0\), and \(D^2v=0\) there, because the density of \(\mu\) and the matrix \(\tau\) are positive. Hence \(v\) is affine, \(v=c'+\ell\cdot x\). By Proposition 3.1 (3) of that lesson, \(Av=\ell\cdot x\), and \(Av=v\) gives \(c'=0\). \(\blacksquare\)

**Proof of Theorem 1.1.** Let \(g\) be even, in \(L^2(\mu)\), with \(\mathbb E\,g=0\), and orthogonal to all \(\mathcal Pf\) with \(f\) even. By Lemma 3.1 and Proposition 5.1, \(g=c+\ell\cdot x\). Since \(g\) is even, \(\ell=0\); since its mean is \(0\), \(c=0\). \(\blacksquare\)

The proof used a global upper bound for \(\tau\), but no lower bound: the positivity of \(\tau\) entered only at single points and on bounded sets.

## 6. Exercises

**6.1.** For the Gaussian pair (\(\tau=I\), \(A=x\cdot\nabla-\Delta\)) in dimension \(1\), compute \(\mathcal Pf\) for \(f=x^2\), \(f=x^3\) and \(f=x^4\). Which polynomials of degree at most \(4\) are of the form \(\mathcal Pf\) with a polynomial \(f\)?

**6.2.** Show that every \(\mathcal Pf\), for smooth \(f\) with compact support, is orthogonal in \(L^2(\mu)\) to the constants and to the coordinate functions \(x_j\), if the \(x_j\) are in \(L^2(\mu)\).

**6.3.** Prove the bound \(Y\le(10B+\sqrt a)\,G\) from \(Y^2\le aG^2+10BGY\).

**6.4.** Where does the proof of Proposition 5.1 fail for the function \(g=x_1^2-\mathbb E\,x_1^2\) in the Gaussian case, which is even, centered and not zero?

## 7. Solutions

**6.1.** \(A x^k=kx^k-k(k-1)x^{k-2}\). So \(Ax^2=2x^2-2\), \((A-1)x^2=x^2-2\), and \(\mathcal Px^2=A(x^2-2)=2x^2-2\). \((A-1)x^3=2x^3-6x\) and \(\mathcal Px^3=6x^3-18x\). \((A-1)x^4=3x^4-12x^2\), and \(\mathcal Px^4\) is \(12x^4-36x^2-24x^2+24\), that is, \(12x^4-60x^2+24\). In terms of the Hermite polynomials \(H_2=x^2-1\), \(H_3=x^3-3x\), \(H_4=x^4-6x^2+3\): \(\mathcal Px^2=2H_2\), \(\mathcal Px^3=6H_3\) and \(\mathcal Px^4=12H_4+12H_2\). On \(H_2,H_3,H_4\) the operator \(A\) is the multiplication by \(2,3,4\) and \(\mathcal P\) the multiplication by \(2,6,12\); on \(1\) and \(x\) it is \(0\). So the polynomials \(\mathcal Pf\) of degree at most \(4\) are the combinations of these three Hermite polynomials: the polynomials orthogonal to \(1\) and \(x\) for the Gaussian measure.

**6.2.** By Proposition 3.1 (2) of the lesson on moment coordinates, used twice with the compactly supported \(f\), \(\mathbb E\,(\mathcal Pf)\,F=\mathbb E\,f\,\mathcal PF\) for smooth \(F\), and \(\mathcal P1=0\), \(\mathcal Px_j=A(x_j-x_j)=0\).

**6.3.** If \(Y>10BG+\sqrt a\,G\), then both \(Y\) and \(Y-10BG\) are larger than \(\sqrt a\,G\), so \(Y^2-10BGY=Y(Y-10BG)>aG^2\), a contradiction.

**6.4.** It does not fail: this \(g\) is not orthogonal to the tests. \(g=x_1^2-1\) and \(\mathcal Pg=2g\ne0\), so Lemma 3.1 excludes it; indeed \(g=\mathcal P(\tfrac12x_1^2)\) is itself a limit of tests, as Theorem 1.1 says.

## References

- [OpenAI-L] OpenAI, *The logarithmic Brunn-Minkowski conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026

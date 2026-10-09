# Supports, radial contact and the Mazur–Ulam theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a real normed space \(X\) let \(S_X=\{x\in X:\|x\|=1\}\) be its unit sphere, with the distance \(\|x-y\|\). Tingley asked in 1987 whether every surjective isometry \(f:S_X\to S_Y\) between unit spheres of real normed spaces is the restriction of a linear isometry of the spaces. Mazur and Ulam had shown in 1932 that a surjective isometry between whole real normed spaces is affine (Theorem 3.1 below), but a sphere has no interior, and the question remained open in general; positive answers were found for many classes of spaces, among them all two-dimensional spaces (Banakh), and unital C\*-algebras and real von Neumann algebras (Mori and Ozawa [MO]), as recalled in [OpenAI-T, Section 1]. OpenAI proved in September 2026 that the answer is always yes for Banach spaces [OpenAI-T]:

**Theorem.** Let \(X,Y\) be nonzero real Banach spaces and \(f:S_X\to S_Y\) a surjective isometry. Then \(T(0)=0\), \(T(x)=\|x\|f(x/\|x\|)\) for \(x\neq0\), is a surjective real-linear isometry, and it is the only linear map extending \(f\).

The only possible extension is this radial map \(T\). It preserves norms and distances between vectors of equal norm, and the problem is to show that it preserves distances between vectors of different norms. This lesson collects the tools of convex geometry used throughout, proves the Mazur–Ulam theorem, and reduces the theorem to a numerical statement: the *defect* of \(f\), the largest error of \(T\) between two radii, vanishes (Proposition 4.2). The lesson [Ultrapowers and Darbo's fixed-point theorem](ultrapowers-and-darbos-fixed-point-theorem.md) shows that a positive defect can be assumed to be attained, the lesson [Aligned chords](aligned-chords.md) turns an attained defect into a rigid configuration of two chords, and the lesson [Tingley's problem](tingleys-problem.md) shows that this configuration cannot exist.

We use the Hahn–Banach theorem in the form of [Corollary 2.3 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-02): a bounded functional on a subspace extends to the whole space with the same norm, and every \(x\) has \(\varphi\) with \(\|\varphi\|\le1\) and \(\varphi(x)=\|x\|\).

## 1. Supports

Throughout, \(X\) is a real normed space and \(X^*\) its dual. A *support* at \(a\in X\) is a functional \(\varphi\in X^*\) with \(\|\varphi\|\le1\) and \(\varphi(a)=\|a\|\). Supports exist at every point by the Hahn–Banach theorem. A support at \(a\) is a support at every \(\lambda a\), \(\lambda\ge0\).

**Lemma 1.1** (common supports). Let \(v,w\in S_X\) and \(\alpha,\beta>0\) with \(\|\alpha v+\beta w\|=\alpha+\beta\). Then some \(\varphi\in X^*\) with \(\|\varphi\|\le1\) satisfies \(\varphi(v)=\varphi(w)=1\). More generally, if \(v_1,\dots,v_n\in S_X\), \(\lambda_i>0\), \(\sum_i\lambda_i=1\), and a functional \(\varphi\) with \(\|\varphi\|\le1\) satisfies \(\varphi(\sum_i\lambda_iv_i)=1\), then \(\varphi(v_i)=1\) for all \(i\), and every \(l\) in the convex hull of \(v_1,\dots,v_n\) satisfies \(\|l\|=\varphi(l)=1\).

**Proof.** A support \(\varphi\) at \(\alpha v+\beta w\) satisfies \(\alpha\varphi(v)+\beta\varphi(w)=\alpha+\beta\) with \(\varphi(v),\varphi(w)\le1\), so both values are \(1\). In the second statement, \(\sum_i\lambda_i\varphi(v_i)=1\) with all \(\varphi(v_i)\le1\) forces \(\varphi(v_i)=1\); then \(\varphi(l)=1\) for \(l\) in the convex hull, and \(1=\varphi(l)\le\|l\|\le1\). \(\square\)

We say that \(v,w\in S_X\) *share a support* if some \(\varphi\) with \(\|\varphi\|\le1\) has \(\varphi(v)=\varphi(w)=1\).

**Lemma 1.2** (supports and secants). Let \(a,b\in X\) and \(F(\lambda)=\|a+\lambda b\|\) for real \(\lambda\). Then \(F\) is convex. If \(\varphi\) is a support at \(a+\lambda_0b\), then \(F(\lambda)\ge F(\lambda_0)+(\lambda-\lambda_0)\varphi(b)\) for all \(\lambda\). Consequently \(\varphi(b)\le\frac{F(\lambda)-F(\lambda_0)}{\lambda-\lambda_0}\) for \(\lambda>\lambda_0\), and \(\varphi(b)\ge\frac{F(\lambda_0)-F(\lambda)}{\lambda_0-\lambda}\) for \(\lambda<\lambda_0\).

**Proof.** Convexity follows from the triangle inequality. Moreover \(F(\lambda)\ge\varphi(a+\lambda b)=\varphi(a+\lambda_0b)+(\lambda-\lambda_0)\varphi(b)=F(\lambda_0)+(\lambda-\lambda_0)\varphi(b)\). \(\square\)

For a convex function \(F\) on an interval we also use the monotonicity of secant slopes: if \(\lambda_1<\lambda_2<\lambda_3\), then \(\frac{F(\lambda_2)-F(\lambda_1)}{\lambda_2-\lambda_1}\le\frac{F(\lambda_3)-F(\lambda_1)}{\lambda_3-\lambda_1}\le\frac{F(\lambda_3)-F(\lambda_2)}{\lambda_3-\lambda_2}\), which follows from writing \(\lambda_2\) as a convex combination of \(\lambda_1\) and \(\lambda_3\).

## 2. Radial contact

**Lemma 2.1.** Let \(c\in X\) with \(\|c\|<1\). For every \(v\in S_X\) there is exactly one \(\rho(v)>0\) with \(c+\rho(v)v\in S_X\). It satisfies \(1-\|c\|\le\rho(v)\le1+\|c\|\), and \(\rho\) is continuous on \(S_X\).

**Proof.** The function \(\phi(\lambda)=\|c+\lambda v\|\) is continuous and convex on \([0,\infty)\), with \(\phi(0)=\|c\|<1\) and \(\phi(\lambda)\ge\lambda-\|c\|\). By the intermediate value theorem it takes the value \(1\) at some \(\lambda>0\). If \(\phi(\lambda_1)=\phi(\lambda_2)=1\) with \(0<\lambda_1<\lambda_2\), convexity would give \(\phi(\lambda_1)\le(1-\frac{\lambda_1}{\lambda_2})\phi(0)+\frac{\lambda_1}{\lambda_2}\phi(\lambda_2)<1\). The bounds follow from \(1=\|c+\rho v\|\le\|c\|+\rho\) and \(1\ge\rho-\|c\|\). If \(v_n\to v\) in \(S_X\), the bounded numbers \(\rho(v_n)\) have only limit points \(\rho^*\) with \(\|c+\rho^*v\|=1\), that is \(\rho^*=\rho(v)\); so \(\rho(v_n)\to\rho(v)\). \(\square\)

## 3. The Mazur–Ulam theorem

**Theorem 3.1** (Mazur–Ulam). Let \(E,E'\) be real normed spaces and \(F:E\to E'\) a surjective isometry. Then \(x\mapsto F(x)-F(0)\) is real-linear.

**Proof.** *Isometries fixing two points fix their midpoint.* Let \(a,c\in E\), \(m=\frac12(a+c)\), and let \(\mathcal G\) be the set of surjective isometries \(H:E\to E\) with \(H(a)=a\) and \(H(c)=c\). For \(H\in\mathcal G\), \(\|H(m)-m\|\le\|H(m)-H(a)\|+\|a-m\|=\|a-c\|\), so \(\lambda=\sup_{H\in\mathcal G}\|H(m)-m\|\) is finite. The reflection \(\psi(x)=2m-x\) is a surjective isometry exchanging \(a\) and \(c\) and fixing \(m\). For \(H\in\mathcal G\), the map \(H^\sharp=\psi H^{-1}\psi H\) is a surjective isometry with \(H^\sharp(a)=\psi H^{-1}(c)=a\) and likewise \(H^\sharp(c)=c\), and
\[
\|H^\sharp(m)-m\|=\|H^{-1}\psi H(m)-m\|=\|\psi H(m)-H(m)\|=2\|H(m)-m\|,
\]
using that \(\psi\) and \(H\) are isometries and \(\psi(m)=m\). So \(2\|H(m)-m\|\le\lambda\) for every \(H\in\mathcal G\), whence \(2\lambda\le\lambda\) and \(\lambda=0\).

*Surjective isometries preserve midpoints.* Let \(m'=\frac12(F(a)+F(c))\) and \(\psi'(y)=2m'-y\) on \(E'\). The map \(H=\psi F^{-1}\psi'F\) is a surjective isometry of \(E\) with \(H(a)=\psi F^{-1}(F(c))=a\) and \(H(c)=c\), so \(H(m)=m\), that is \(\psi'(F(m))=F(\psi(m))=F(m)\), and \(F(m)=m'\).

*Linearity.* \(G(x)=F(x)-F(0)\) is a surjective isometry with \(G(0)=0\) that preserves midpoints. Taking \(c=0\) gives \(G(a/2)=G(a)/2\), and then \(G(a+c)=2G(\frac12(a+c))=G(a)+G(c)\). An additive map is \(\mathbb Q\)-linear, and a continuous \(\mathbb Q\)-linear map between real normed spaces is \(\mathbb R\)-linear. \(\square\)

The reflection argument is due to Väisälä, building on Vogt; see the note [Ni].

## 4. The defect of a sphere isometry

Let \(X,Y\) be real normed spaces and \(f:S_X\to S_Y\) a surjective isometry. For \(x,y\in S_X\) and \(0\le q\le1\) put
\[
D_q(x,y)=\|f(x)-qf(y)\|-\|x-qy\|,\qquad M=\sup_{x,y\in S_X,\ 0\le q\le1}|D_q(x,y)|.
\]
We call \(M\) the *defect* of \(f\). The number \(D_q(x,y)\) is the error of the radial map \(T\) on the pair \(x,qy\).

**Lemma 4.1.** (a) The inverse \(f^{-1}:S_Y\to S_X\) is a surjective isometry, and its defect function satisfies \(D^{f^{-1}}_q(f(x),f(y))=-D_q(x,y)\); in particular it has the same defect \(M\).

(b) \(q\mapsto D_q(x,y)\) is \(2\)-Lipschitz, \(D_0(x,y)=D_1(x,y)=0\), and \(|D_q(x,y)|\le2\min(q,1-q)\). In particular \(0\le M\le1\).

**Proof.** (a) An isometry is injective, so \(f\) is bijective, and \(D^{f^{-1}}_q(f(x),f(y))=\|x-qy\|-\|f(x)-qf(y)\|\). (b) Each of \(q\mapsto\|f(x)-qf(y)\|\) and \(q\mapsto\|x-qy\|\) is \(1\)-Lipschitz because \(\|f(y)\|=\|y\|=1\). At \(q=0\) both norms are \(1\), and at \(q=1\) they are equal because \(f\) is an isometry. \(\square\)

**Proposition 4.2** (reduction). If \(X,Y\) are real normed spaces and \(f:S_X\to S_Y\) is a surjective isometry with defect \(M=0\), then the radial map \(T\) is a surjective real-linear isometry \(X\to Y\) extending \(f\), and it is the only linear map extending \(f\).

**Proof.** Let \(a=\alpha x\) and \(c=\beta y\) with \(x,y\in S_X\) and \(\alpha\ge\beta>0\), and put \(q=\beta/\alpha\in(0,1]\). Then
\[
\|T(a)-T(c)\|=\alpha\|f(x)-qf(y)\|=\alpha\|x-qy\|=\|a-c\|,
\]
and exchanging \(a\) and \(c\) covers \(\beta>\alpha\). Also \(\|T(a)-T(0)\|=\|a\|\). So \(T\) is an isometry. For \(b\in Y\setminus\{0\}\), surjectivity of \(f\) gives \(y\in S_X\) with \(f(y)=b/\|b\|\), and \(T(\|b\|y)=b\). By the Mazur–Ulam theorem, \(T=T-T(0)\) is real-linear. A linear map extending \(f\) sends \(\lambda x\), \(\lambda>0\), \(x\in S_X\), to \(\lambda f(x)\), so it equals \(T\). \(\square\)

So Tingley's problem for Banach spaces reduces to the statement that every surjective isometry between unit spheres of real Banach spaces has defect \(0\). Completeness is used once, in the lesson on ultrapowers.

## 5. Exercises

**Exercise 5.1** (easy). Show that \(T\) preserves norms and the distance between any two vectors of the same norm, for every surjective sphere isometry \(f\), without assuming \(M=0\).

**Exercise 5.2** (easy). Let \(X=\mathbb C\) regarded as a real normed space with \(|\cdot|\), and \(f(z)=\bar z\) on the unit circle. Show that \(f\) is a surjective sphere isometry whose radial extension is real-linear but not complex-linear.

**Exercise 5.3** (medium). Show that a surjective isometry between real normed spaces need not be linear if it does not fix \(0\), and that an isometry onto its image need not be affine: consider \(t\mapsto(t,|t|)\) from \(\mathbb R\) into \(\mathbb R^2\) with the maximum norm.

**Exercise 5.4** (medium). Let \(F(\lambda)=\|a+\lambda b\|\) and suppose every support at \(a\) is strictly negative on \(b\), with \(a\neq0\). Show that \(F(\lambda)<F(0)\) for all sufficiently small \(\lambda>0\). (Hint: if not, take supports at \(a+\lambda_nb\) on the span of \(a\) and \(b\) and use compactness of the unit ball of the dual of a two-dimensional space.)

## 6. Solutions

**5.1.** \(\|T(\alpha x)\|=\alpha\|f(x)\|=\alpha\), and \(\|T(\alpha x)-T(\alpha y)\|=\alpha\|f(x)-f(y)\|=\alpha\|x-y\|\).

**5.2.** \(|\bar z-\bar w|=|z-w|\), and \(f\) is a bijection of the circle. Its radial extension is \(z\mapsto\bar z\), which is real-linear, and \(\overline{iz}=-i\bar z\neq i\bar z\) for \(z\neq0\).

**5.3.** Translations are surjective isometries that are not linear. For \(\gamma(t)=(t,|t|)\), \(\|\gamma(t)-\gamma(s)\|_\infty=\max(|t-s|,||t|-|s||)=|t-s|\), so \(\gamma\) is an isometry onto its image, but \(\gamma(0)=0\) and \(\gamma(1)+\gamma(-1)=(0,2)\neq2\gamma(0)\), so \(\gamma\) is not affine. The Mazur–Ulam theorem needs surjectivity onto a normed space.

**5.4.** Suppose \(F(\lambda_n)\ge F(0)\) for some \(\lambda_n\downarrow0\). On \(V=\operatorname{span}\{a,b\}\) choose supports \(L_n\) at \(a+\lambda_nb\) (Corollary 2.3 of the Banach space lesson in \(V\)). Then \(F(0)\le F(\lambda_n)=L_n(a)+\lambda_nL_n(b)\le F(0)+\lambda_nL_n(b)\), so \(L_n(b)\ge0\). The unit ball of \(V^*\) is compact, so a subsequence converges to \(L\) with \(\|L\|\le1\), \(L(b)\ge0\), and \(L(a)=\lim(F(\lambda_n)-\lambda_nL_n(b))=F(0)=\|a\|\). Extending \(L\) to \(X\) with the same norm gives a support at \(a\) that is not negative on \(b\), a contradiction.

## References

- [MO] M. Mori and N. Ozawa, *Mankiewicz's theorem and the Mazur–Ulam property for C\*-algebras*, Studia Math. 250 (2020); arXiv:1804.10674. https://arxiv.org/abs/1804.10674
- [Ni] B. Nica, *The Mazur–Ulam theorem*, Expo. Math. 30 (2012), 397–398; arXiv:1306.2380. https://arxiv.org/abs/1306.2380
- [OpenAI-T] OpenAI, *A positive solution to Tingley's problem*, OpenAI Math Release preprint, 23 September 2026, Sections 1, 2 and 6. https://github.com/openai/math/blob/main/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026

# Shells and Gaussian duality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The first two lessons of this course prove that the triangular lattice \(A\) is universally optimal if, for every \(\alpha>0\), there is a *sharp pair* for the Gaussian \(e^{-\pi\alpha|x|^2}\): a function below the Gaussian with nonnegative Fourier transform, touching the Gaussian at the points of \(A\) and with transform vanishing at the points of the dual lattice ([Energy, density and the linear programming bound](energy-density-and-the-linear-programming-bound.md), [Completely monotone interactions](completely-monotone-interactions.md)). This lesson reduces that family of statements to one normalized statement.

- The squared lengths of the vectors of \(A\), multiplied by \(\sqrt3/2\), are the integers \(j^2+j\ell+\ell^2\), and all of these lie in six residue classes modulo \(12\) (Lemma 1.1). The dual lattice of \(A\) is \(A\) turned by a right angle, so it has the same lengths (Lemma 1.2).
- In the variable \(s=\tfrac{\sqrt3}2|x|^2\) the contacts are therefore required at a set of integers that is periodic with period \(12\). The *normalized statement* \((\mathrm N_k)\) asks for a function and its transform with contacts at all positive integers of the six classes (Section 2). It is the form in which [OpenAI-T] proves the existence of sharp pairs.
- If \((\mathrm N_k)\) holds for all \(k\ge2.36\), sharp pairs exist for all \(\alpha>0\) (Theorem 4.1). For \(\alpha\ge1\) this is a change of scale. For \(\alpha<1\) the roles of the function and its transform are exchanged: the Fourier transform turns the Gaussian with parameter \(1/\alpha\) into the Gaussian with parameter \(\alpha\).

The lesson follows [OpenAI-T, Section 2, first part, and Section 6, second part]. The exchange of a function and its transform for Gaussians is from H. Cohn and S. D. Miller, as cited there.

## 1. The shells of the triangular lattice

Let \(b=\sqrt3/2\), and
\[
\begin{gathered}
u=b^{-1/2}(1,0),\qquad v=b^{-1/2}(\tfrac12,b),\\
A=\{ju+\ell v\mid j,\ell\in\mathbb Z\},
\end{gathered}
\]
the triangular lattice of covolume one. Since \(u\cdot u=v\cdot v=1/b\) and \(u\cdot v=1/(2b)\),
\[
b\,|ju+\ell v|^2=j^2+j\ell+\ell^2 .
\]
The sets of lattice points of a given length are the *shells* of \(A\).

**Lemma 1.1.** For integers \(j,\ell\), the number \(n=j^2+j\ell+\ell^2\) is congruent modulo \(12\) to one of
\[
0,\ 1,\ 3,\ 4,\ 7,\ 9 .
\]

**Proof.** Modulo \(3\): \(n\equiv j^2-2j\ell+\ell^2=(j-\ell)^2\), which is \(0\) or \(1\). Modulo \(4\): if \(j\) and \(\ell\) are even, \(n\) is divisible by \(4\); if both are odd, \(n\) is a sum of three odd numbers; if exactly one is odd, \(n\) is odd plus even plus even. So \(n\) is divisible by \(4\) or odd: \(n\) is \(0\), \(1\) or \(3\) modulo \(4\). The six pairs of residues modulo \(4\) and \(3\) are \((0,0),(0,1),(1,0),(1,1),(3,0),(3,1)\), and the corresponding residues modulo \(12\) are \(0,4,9,1,3,7\). \(\blacksquare\)

Let \(\mathcal N\) be the set of positive integers that are congruent to \(0,1,3,4,7\) or \(9\) modulo \(12\). So \(b|a|^2\in\mathcal N\) for every \(a\in A\setminus\{0\}\). Not every element of \(\mathcal N\) occurs: \(15\) and \(24\) are not of the form \(j^2+j\ell+\ell^2\) (Exercise 5.1).

Let \(J(x_1,x_2)=(-x_2,x_1)\), the rotation by a right angle. The dual lattice \(A^*\) is the set of all \(w\) with \(w\cdot a\in\mathbb Z\) for all \(a\in A\).

**Lemma 1.2.** \(A^*=JA\). Consequently \(b|w|^2\in\mathcal N\) for every \(w\in A^*\setminus\{0\}\), and a radial function vanishes on \(A\setminus\{0\}\) exactly if it vanishes on \(A^*\setminus\{0\}\).

**Proof.** For \(x,y\in\mathbb R^2\), \(Jx\cdot y=x_1y_2-x_2y_1=\det(x,y)\). Here \(\det(u,v)=b^{-1}\cdot b=1\). Let \(w_1=-Jv\) and \(w_2=Ju\). Then
\[
\begin{gathered}
w_1\cdot u=\det(u,v)=1,\qquad w_1\cdot v=0,\\
w_2\cdot u=0,\qquad w_2\cdot v=\det(u,v)=1 .
\end{gathered}
\]
A vector \(w\) is \((w\cdot u)w_1+(w\cdot v)w_2\), because both sides have the same products with \(u\) and \(v\). So \(w\in A^*\) exactly if \(w\) is an integer combination of \(w_1,w_2\), that is, \(A^*=J(\mathbb Zv+\mathbb Zu)=JA\). Since \(|Ja|=|a|\), the two lattices have the same lengths, and a radial function takes the same values at \(a\) and at \(Ja\). \(\blacksquare\)

## 2. The normalized statement

*Admissible* functions, their Fourier transforms and *sharp pairs* are as in the lesson on the linear programming bound. A function on \(\mathbb R^2\) is *radial* if it depends only on \(|x|\). The Fourier transform of an integrable radial function is radial, because Lebesgue measure and the product \(x\cdot\xi\) are unchanged when \(x\) and \(\xi\) are rotated together.

Let \(h=2/5\). For \(k>0\) and \(s\ge0\) let
\[
T_k(s)=k^{-1}e^{-k(s-1)} .
\]

**Statement \((\mathrm N_k)\).** There are an admissible radial function \(f\) on \(\mathbb R^2\) and functions \(H_1,H_2\colon[0,\infty)\to\mathbb R\) such that, with \(s=b|x|^2\),
\[
\begin{gathered}
f(x)=e^{-\pi hs}H_1(s),\\
\widehat f(x)=e^{-\pi hs}H_2(s),
\end{gathered}
\]
and such that \(H_1(s)\le T_k(s)\) and \(H_2(s)\ge0\) for all \(s\ge0\), and \(H_1(n)=T_k(n)\) and \(H_2(n)=0\) for all \(n\in\mathcal N\).

The theorem on normalized Gaussian pairs of [OpenAI-T, Section 2] asserts, for every \(k\ge2.36\), such a function with further properties: \(f\) is rapidly decreasing, \(H_1\) and \(H_2\) are entire functions, and the derivatives also agree at the nodes, \(H_1'(n)=T_k'(n)\) and \(H_2'(n)=0\). A rapidly decreasing function is admissible. The further properties are not needed for the reduction of this lesson; the derivative conditions are consequences of the sign conditions for differentiable \(H_1,H_2\) (Exercise 5.3), and they are what the construction in [OpenAI-T] aims at. The proof of that theorem occupies Sections 2 to 5 of [OpenAI-T] and two appendices of verified computations. It is not part of this lesson: here \((\mathrm N_k)\) is a hypothesis.

## 3. Gaussians and admissible functions

For \(\beta>0\) let \(G_\beta(x)=e^{-\pi\beta|x|^2}\) on \(\mathbb R^2\).

**Lemma 3.1.** \(\widehat{G_\beta}=\beta^{-1}G_{1/\beta}\). In particular \(G_\beta\) is admissible.

**Proof.** In one variable, \(\int_{\mathbb R}e^{-\pi t^2}e^{-2\pi it\tau}\,dt=e^{-\pi\tau^2}\) ([Real-variable calculations for the Fourier examples](course:HA-LCA/prerequisites/src/real-variable-calculations), Theorem 2.1; the sign of the exponent does not matter, because the Gaussian is even). By Fubini's theorem the transform of \(G_1(x)=e^{-\pi x_1^2}e^{-\pi x_2^2}\) is \(G_1\). The substitution \(x=\beta^{-1/2}y\) in the plane, with \(dx=\beta^{-1}dy\), gives
\[
\widehat{G_\beta}(\xi)=\beta^{-1}\,\widehat{G_1}(\beta^{-1/2}\xi)=\beta^{-1}e^{-\pi|\xi|^2/\beta}.
\]
\(G_\beta\) is continuous, even and real, and it and its transform decay faster than every power. \(\blacksquare\)

**Lemma 3.2.** Let \(q\) be admissible. Then \(\widehat q\) is admissible, and the Fourier transform of \(\widehat q\) is \(q\). Sums and real multiples of admissible functions are admissible.

**Proof.** \(\widehat q\) is real and even, and it is continuous by dominated convergence, since \(q\) is integrable. By the inversion formula (Lemma 2.1(1) of the lesson on the linear programming bound) and because \(q\) is even,
\[
\int\widehat q(\xi)\,e^{-2\pi ix\cdot\xi}\,d\xi=q(-x)=q(x).
\]
So the transform of \(\widehat q\) is \(q\), and the decay condition for the pair \((\widehat q,q)\) is the same as for \((q,\widehat q)\). The last statement is clear. \(\blacksquare\)

## 4. Sharp pairs for all Gaussians

**Theorem 4.1.** Suppose \((\mathrm N_k)\) holds for every \(k\ge2.36\). Then for every \(\alpha>0\) there is a radial sharp pair for \(\alpha\).

**Proof.** *The case \(\alpha\ge1\).* Let
\[
k=\pi\Bigl(\frac\alpha b-h\Bigr).
\]
Then \(k\ge\pi(2/\sqrt3-2/5)\). Since \(\sqrt3<1.7321\) and \(\pi>3.1415\), this is more than \(3.1415\cdot(1.1546-0.4)>2.37\). Let \(f,H_1,H_2\) be as in \((\mathrm N_k)\), and
\[
f_\alpha=ke^{-k}f .
\]
It is admissible and radial, and \(\widehat{f_\alpha}=ke^{-k}\widehat f\ge0\). With \(s=b|x|^2\),
\[
\begin{aligned}
f_\alpha(x)&\le ke^{-k}e^{-\pi hs}T_k(s)=e^{-(\pi h+k)s}\\
&=e^{-\pi\alpha|x|^2},
\end{aligned}
\]
because \((\pi h+k)b=\pi\alpha\); and equality holds when \(H_1(s)=T_k(s)\). For \(a\in A\setminus\{0\}\) the number \(s=b|a|^2\) lies in \(\mathcal N\) (Lemma 1.1), so \(f_\alpha(a)=G_\alpha(a)\). For \(w\in A^*\setminus\{0\}\), \(b|w|^2\in\mathcal N\) (Lemma 1.2), so \(\widehat{f_\alpha}(w)=0\). So \(f_\alpha\) is a sharp pair for \(\alpha\).

*The case \(0<\alpha<1\).* Let \(\beta=1/\alpha>1\), and let \(f_\beta\) be the radial sharp pair for \(\beta\) just constructed. Put
\[
q=G_\beta-f_\beta\ge0,\qquad r=\widehat{f_\beta}\ge0 .
\]
Both are radial, and \(q\) is admissible by Lemmas 3.1 and 3.2. Let
\[
f_\alpha=\beta\,\widehat q .
\]
By Lemma 3.2, \(f_\alpha\) is admissible, and \(\widehat{f_\alpha}=\beta q\ge0\). By Lemma 3.1,
\[
\widehat q=\widehat{G_\beta}-\widehat{f_\beta}=\beta^{-1}G_\alpha-r ,
\]
so \(G_\alpha-f_\alpha=\beta r\ge0\). It remains to check the contacts. The function \(q\) vanishes on \(A\setminus\{0\}\), and \(r\) vanishes on \(A^*\setminus\{0\}\), because \(f_\beta\) is a sharp pair. Both are radial, so by Lemma 1.2 \(q\) vanishes on \(A^*\setminus\{0\}\) and \(r\) on \(A\setminus\{0\}\). Hence \(f_\alpha(a)=G_\alpha(a)-\beta r(a)\) equals \(G_\alpha(a)\) for \(a\in A\setminus\{0\}\), and \(\widehat{f_\alpha}(w)=\beta q(w)=0\) for \(w\in A^*\setminus\{0\}\). \(\blacksquare\)

**Corollary 4.2.** Suppose \((\mathrm N_k)\) holds for every \(k\ge2.36\). Then for every completely monotone \(g\colon(0,\infty)\to[0,\infty)\) and every configuration \(\mathcal C\) of density one in the plane, \(E_g(\mathcal C)\ge E_g(A)\).

**Proof.** Theorem 4.1 gives statement \((\mathrm G)\) of the lesson on completely monotone interactions; apply Theorem 5.1 there. \(\blacksquare\)

So the whole theorem rests on the statements \((\mathrm N_k)\), \(k\ge2.36\): one family of functions of one real variable \(s\), with prescribed contacts at the integers of six residue classes and two sign conditions.

In the second case the slack of the function and the slack of its transform change places: for \(f_\beta\) the two nonnegative functions are \(G_\beta-f_\beta\) and \(\widehat{f_\beta}\); for \(f_\alpha\) they are, up to the factor \(\beta\), \(\widehat{f_\beta}\) and \(G_\beta-f_\beta\). The argument uses that the lattice is, up to a rotation, its own dual.

## 5. Exercises

**5.1.** List the elements of \(\mathcal N\) up to \(30\), and determine which of them are of the form \(j^2+j\ell+\ell^2\).

**5.2.** Show that \(\sum_{a\in A}e^{-\pi\beta|a|^2}=\beta^{-1}\sum_{a\in A}e^{-\pi|a|^2/\beta}\) for every \(\beta>0\).

**5.3.** Let \(H_1,H_2\) be as in \((\mathrm N_k)\) and differentiable at a point \(n\in\mathcal N\). Show that \(H_1'(n)=T_k'(n)\) and \(H_2'(n)=0\).

**5.4.** Show that exactly six points \(a\in A\) have \(b|a|^2=1\), and that they are the corners of a regular hexagon.

## 6. Solutions

**5.1.** The elements of \(\mathcal N\) up to \(30\) are 1, 3, 4, 7, 9, 12, 13, 15, 16, 19, 21, 24, 25, 27, 28. The pairs \((j,\ell)\) = (1,0), (1,1), (2,0), (2,1), (3,0), (2,2), (3,1), (4,0), (3,2), (4,1), (5,0), (3,3), (4,2) give the values 1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, 27, 28. The form is positive definite, \(j^2+j\ell+\ell^2\ge\tfrac34\max(j^2,\ell^2)\), so for values up to \(30\) only \(|j|,|\ell|\le6\) have to be tried, and one finds no representation of \(15\) or \(24\). For \(24\) there is also this argument: \(n\) even forces \(j,\ell\) even (proof of Lemma 1.1), so \(24=4n_1\) with \(n_1=6\) of the same form; \(6\) is even, so again both arguments are even and \(6\) would be divisible by \(4\).

**5.2.** By the Poisson summation formula for \(A\), applied to the admissible function \(G_\beta\) (as in Proposition 4.1 of the lesson on the linear programming bound), and Lemma 3.1, the left side is \(\beta^{-1}\sum_{w\in A^*}e^{-\pi|w|^2/\beta}\). By Lemma 1.2 the sum over \(A^*\) equals the sum over \(A\).

**5.3.** The function \(T_k-H_1\) is nonnegative on \([0,\infty)\) and vanishes at the interior point \(n\); so it has a minimum there, and its derivative at \(n\) is zero. The same holds for \(H_2\).

**5.4.** \(j^2+j\ell+\ell^2=1\) has the six solutions \(\pm(1,0)\), \(\pm(0,1)\), \(\pm(1,-1)\): if \(|j|\ge2\) or \(|\ell|\ge2\) the form is at least \(3\), by the inequality in the solution of 5.1. The points are \(\pm u\), \(\pm v\), \(\pm(u-v)\), of length \(b^{-1/2}\). The angle between \(u\) and \(v\) has cosine \(u\cdot v/|u||v|=1/2\), so it is \(60\) degrees; \(v-u\) is \(u\) turned by \(120\) degrees. So the six points are obtained from \(u\) by the rotations through multiples of \(60\) degrees.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Sections 2 and 6. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026

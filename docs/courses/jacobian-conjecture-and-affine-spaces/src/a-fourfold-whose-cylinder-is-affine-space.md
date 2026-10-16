# A fourfold whose cylinder is affine space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Zariski's cancellation problem asks whether an affine variety \(X\) with \(X\times\mathbb A^1\cong\mathbb A^{n+1}\) must itself be \(\mathbb A^n\). In algebraic terms: if adjoining one variable to a finitely generated algebra \(A\) gives a polynomial ring in \(n+1\) variables, is \(A\) a polynomial ring in \(n\) variables? This lesson and the next answer the question negatively in dimension four, in characteristic zero. This lesson constructs the fourfold, a hypersurface in affine five-space given by one explicit equation, and writes down an isomorphism of its cylinder with affine five-space. The next lesson, [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md), proves that the fourfold itself is not affine four-space.

We use [Locally nilpotent derivations](locally-nilpotent-derivations.md) for exponentials of derivations, and unique factorization in polynomial rings from [Integral extensions: lying over, going up and going down](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#2-integral-closure-survives-localization). Dimension is computed with [Krull dimension and Noether normalization, Theorem 4.2](course:AG-CA/krull-dimension-and-noether-normalization#4-parameters-measure-dimension-and-height).

Basic references are [OpenAI-cancellation] and [Gupta-survey].

## 1. The cancellation problem

Let \(k\) be a field and write \(k^{[n]}\) for a polynomial ring in \(n\) variables over \(k\). The **cancellation problem** asks: if \(A\) is a finitely generated \(k\)-algebra and \(A[w]\cong k^{[n+1]}\) for a variable \(w\), must \(A\cong k^{[n]}\)? An isomorphism of the cylinder need not respect the projection to the line \(w\), so it gives no direct way to find coordinates on \(A\).

For \(n=1\) the answer is yes, by Abhyankar, Eakin and Heinzer [AEH]. For \(n=2\) and \(k\) of characteristic zero it is yes by the work of Fujita, Miyanishi and Sugie [Fujita], [Miyanishi–Sugie]. In positive characteristic, Gupta proved that the answer is no in every dimension \(n\ge3\) [Gupta]. The example of this lesson, found in 2026 [OpenAI-cancellation], answers the question negatively in characteristic zero for \(n=4\). We do not use any of these earlier results.

From now on \(k\) is a field of characteristic zero.

## 2. The fourfold

Let \(P=k[p,s,u,F,J]\) be a polynomial ring in five variables, and define

\[
\begin{gathered}
x=s^2+u^3+p^2F,\\
y=s+x(x-u^3),\\
z=sx+p^2J,
\end{gathered}\tag{2.1}
\]
and make the definitions (2.2):
\[
\begin{aligned}
H&=x^2F-(1+2sx)J-p^2J^2\\
&\quad-pu,\\
A&=P/(H).
\end{aligned}
\]

So \(H\) is one explicit polynomial in the five variables \(p,s,u,F,J\), and \(A\) is the coordinate ring of the hypersurface \(H=0\). We use the same letters for elements of \(P\) and their images in \(A\).

**Lemma 2.1.** In \(P\),

\[
\begin{aligned}
&xy-z(z+1)\\
&\quad =p^2\,(H+pu).
\end{aligned}\tag{2.3}
\]

**Proof.** Since \(xy=sx+x^2(x-u^3)\) and \(z(z+1)\) equals \(s^2x^2+2sxp^2J+p^4J^2+sx+p^2J\), the terms \(sx\) cancel and

\[
\begin{aligned}
&xy-z(z+1)=x^2(x-u^3-s^2)\\
&\quad -p^2(1+2sx)J-p^4J^2 .
\end{aligned}
\]

Now \(x-u^3-s^2=p^2F\), so the right side is \(p^2\bigl(x^2F-(1+2sx)J-p^2J^2\bigr)\), which is \(p^2(H+pu)\). \(\square\)

Over the Laurent polynomial ring \(k[p,p^{-1}]\), the elements \(x,y,z,u\) are coordinates on \(P[p^{-1}]\). Indeed (2.1) can be solved:

\[
\begin{gathered}
s=y-x(x-u^3),\\
F=p^{-2}\bigl(x-s^2-u^3\bigr),\\
J=p^{-2}\bigl(z-sx\bigr),
\end{gathered}\tag{2.4}
\]

so \(P[p^{-1}]=k[p,p^{-1}][x,y,z,u]\), with \(x,y,z,u\) algebraically independent over \(k[p,p^{-1}]\). In these coordinates (2.3) reads

\[
\begin{aligned}
H&=p^{-2}\bigl(xy-z(z+1)\bigr)\\
&\quad -pu .
\end{aligned}\tag{2.5}
\]

**Proposition 2.2.** The ring \(A\) is a domain of dimension four, the image of \(p\) in \(A\) is nonzero, and

\[
A[p^{-1}]=k[p,p^{-1},x,y,z]
\]

is a Laurent polynomial ring over a polynomial ring in \(x,y,z\).

**Proof.** In (2.5) the coefficient of \(u\) is the unit \(-p\), so replacing \(u\) by \(H\) is another change of coordinates of \(P[p^{-1}]\) over \(k[p,p^{-1}]\). Hence \(H\) generates a prime ideal of \(P[p^{-1}]\), and \(P[p^{-1}]/(H)=k[p,p^{-1},x,y,z]\).

Reducing \(H\) modulo \(p\) gives \(x_0^2F-(1+2sx_0)J\) with \(x_0=s^2+u^3\), which is not zero. So \(p\) does not divide \(H\) in \(P\). Factor \(H\) into irreducibles in the factorial ring \(P\). In \(P[p^{-1}]\) it becomes irreducible, so all but one of its irreducible factors become units there, that is, divide a power of \(p\); such a factor is associated to \(p\), which does not divide \(H\). So \(H\) is irreducible, hence prime, and \(A\) is a domain. Since \(A[p^{-1}]\ne0\), the element \(p\) is not zero in \(A\). The fraction field of \(A\) is \(k(p,x,y,z)\), of transcendence degree four, so \(\dim A=4\) by [Krull dimension and Noether normalization, Theorem 4.2](course:AG-CA/krull-dimension-and-noether-normalization#4-parameters-measure-dimension-and-height). \(\square\)

## 3. An exponential that changes the equation

On \(P[p^{-1}]=k[p,p^{-1}][x,y,z,u]\), let \(\Delta=-p^2\,\partial/\partial u\), the derivation that kills \(p,x,y,z\) and sends \(u\) to \(-p^2\). It is locally nilpotent, by Lemma 1.2 of [Locally nilpotent derivations](locally-nilpotent-derivations.md).

**Lemma 3.1.** The derivation \(\Delta\) maps \(P\) into itself, with

\[
\begin{aligned}
&\Delta(p)=0,\quad \Delta(u)\\
&\quad =-p^2,\quad \Delta(s)\\
&\quad =-3p^2xu^2,\quad \Delta(F)\\
&\quad =(6sx+3)u^2,\quad \Delta(J)\\
&\quad =3x^2u^2 .
\end{aligned}\tag{3.1}
\]

Moreover \(\Delta(H)=p^3\) and \(\Delta^2(H)=0\).

**Proof.** Apply \(\Delta\) to (2.4), using \(\Delta(x)=\Delta(y)=\Delta(z)=0\). From \(s=y-x(x-u^3)\), \(\Delta(s)=3xu^2\Delta(u)=-3p^2xu^2\). From \(p^2F=x-s^2-u^3\), \(p^2\Delta(F)=-2s\Delta(s)-3u^2\Delta(u)\), which is \(6p^2sxu^2+3p^2u^2\). From \(p^2J=z-sx\), \(p^2\Delta(J)=-x\Delta(s)=3p^2x^2u^2\). These values lie in \(P\), and \(P\) is generated by \(p,s,u,F,J\), so \(\Delta(P)\subset P\). By (2.5), \(\Delta(H)=-p\,\Delta(u)=p^3\), which \(\Delta\) kills. \(\square\)

Extend \(\Delta\) to \(P[w]\) by \(\Delta(w)=0\). By Proposition 2.1 of [Locally nilpotent derivations](locally-nilpotent-derivations.md), \(\Phi=\exp(w\Delta)\) is an automorphism of \(P[w]\), and by Lemma 3.1

\[
\Phi(H)=H+w\,\Delta(H)=H+p^3w .
\]

Hence \(\Phi\) induces the isomorphism (3.2):

\[
\begin{aligned}
A[w]=P[w]/(H)&\xrightarrow{\ \sim\ }T,\\
T&:=P[w]/(H+p^3w).
\end{aligned}
\]

So it suffices to show that \(T\) is a polynomial ring in five variables. Since \(\Phi\) fixes \(p\) and \(A\) is a domain, \(T\) is a domain in which \(p\ne0\).

## 4. The cylinder is affine five-space

*Linear coordinates adapted to \(p=0\).* Put \(x_0=s^2+u^3\) and

\[
\begin{gathered}
L=x_0^2F-(1+2sx_0)J,\\
M=(1-2sx_0)F+4s^2J .
\end{gathered}\tag{4.1}
\]

This is a linear change of the variables \(F,J\) over \(k[p,s,u]\), with determinant \(4s^2x_0^2+(1+2sx_0)(1-2sx_0)=1\). Its inverse is given by (4.2):

\[
\begin{gathered}
F=4s^2L+(1+2sx_0)M,\\
J=-(1-2sx_0)L+x_0^2M .
\end{gathered}
\]

So \(P=B[L]\) with \(B=k[p,s,u,M]\), a polynomial ring in four variables. From now on we regard \(F\), \(J\) and \(H\) as polynomials in \(L\) over \(B\) through (4.2). Expanding \(x=x_0+p^2F\) in powers of \(p\) gives (4.3):

\[
\begin{gathered}
H=L-pu+p^2Q+p^4F^3,\\
Q=2x_0F^2-2sFJ-J^2 .
\end{gathered}
\]

Indeed \(x^2F=x_0^2F+2p^2x_0F^2+p^4F^3\) and \((1+2sx)J=(1+2sx_0)J+2p^2sFJ\), and \(x_0^2F-(1+2sx_0)J=L\).

*A root modulo \(p^3\).* Write \(C=Q|_{L=0}\in B\) and \(Q=C+L\,Q_1\) with \(Q_1\in B[L]\). Explicitly \(C=M^2\bigl(2x_0+6sx_0^2+4s^2x_0^3-x_0^4\bigr)\). Put

\[
L_*=pu-p^2C\in B .
\]

Then (4.3) gives 
\[
\begin{aligned}
&H(L_*)=L_*-pu\\
&\quad+p^2\bigl(C+L_*Q_1(L_*)\bigr)+p^4F(L_*)^3\\
&\quad=p^3\bigl((u-pC)Q_1(L_*)+pF(L_*)^3\bigr),
\end{aligned}
\]
so

\[
H(L_*)\in p^3B .
\tag{4.4}
\]

*The fifth coordinate.* In \(B[L,w]\) put

\[
\begin{gathered}
h=u-pQ-p^3F^3-p^2w,\\
e_0=-w-pF^3-Q_1h .
\end{gathered}
\]

Then \(H+p^3w=L-ph\) by (4.3), and a direct expansion, using \(Q=C+LQ_1\), gives the identity (4.5):

\[
\begin{aligned}
&p^3e_0-(L-L_*)\\
&\quad=\bigl(p^2Q_1-1\bigr)\bigl(H+p^3w\bigr).
\end{aligned}
\]

So the image \(e\) of \(e_0\) in \(T\) satisfies \(p^3e=L-L_*\).

**Theorem 4.1.** \(T=B[e]=k[p,s,u,M,e]\) is a polynomial ring in five variables. Consequently \(A[w]\cong k^{[5]}\).

**Proof.** *\(B\) embeds in \(T\), and \(e\) is transcendental over it.* Inverting \(p\) in \(T=B[L,w]/(H+p^3w)\) lets us solve for \(w=-p^{-3}H\), so \(T[p^{-1}]\cong B[p^{-1}][L]\), the identity on \(B\) and \(L\). So \(B\to T\) is injective, and in \(T[p^{-1}]\) the element \(e=p^{-3}(L-L_*)\) is a linear polynomial in the variable \(L\) with unit leading coefficient. Hence \(e\) is transcendental over \(B[p^{-1}]\), and so over \(B\).

*\(B\) and \(e\) generate \(T\).* We have \(L=L_*+p^3e\in B[e]\). In \(B[Z]\), the difference \(H(L_*+p^3Z)-H(L_*)\) is divisible by \(p^3\), and \(H(L_*)\) is divisible by \(p^3\) by (4.4). So \(W(Z)=-p^{-3}H(L_*+p^3Z)\) lies in \(B[Z]\). The relation \(H+p^3w=0\) in \(T\) gives \(p^3\bigl(w-W(e)\bigr)=0\), and \(p\) is a nonzero element of the domain \(T\), so \(w=W(e)\in B[e]\). Thus \(T=B[L,w]=B[e]\).

Finally \(A[w]\cong T\) by (3.2). \(\square\)

The five coordinates of \(A[w]\) itself are the images of \(\Phi^{-1}(p)=p\), \(\Phi^{-1}(s)\), \(\Phi^{-1}(u)\), \(\Phi^{-1}(M)\) and \(\Phi^{-1}(e_0)\), where \(\Phi^{-1}=\exp(-w\Delta)\); each is an explicit polynomial, because the exponential is a finite sum.

## 5. What remains

Theorem 4.1 shows that the hypersurface \(H=0\) in \(\mathbb A^5\) becomes affine five-space after multiplying by a line. The equation was chosen so that the hypersurface looks like affine four-space in two other ways as well: after inverting \(p\), Proposition 2.2 identifies it with \(\mathbb A^3\times(\mathbb A^1\setminus0)\), and modulo \(p\) the change of coordinates (4.1) makes \(H\equiv L\) a coordinate. The next lesson proves that nevertheless \(A\) is not a polynomial ring.

## 6. Exercises

**Exercise 6.1 (easy).** Verify that the linear change (4.1) has determinant one, and that (4.2) inverts it.

**Exercise 6.2 (medium).** Show that \(\Delta(H)=p^3\) directly from (3.1), without passing to the coordinates \(x,y,z,u\).

**Exercise 6.3 (medium).** Show that the fibre \(p=0\) of \(\operatorname{Spec}A\) is affine three-space: \(A/pA\cong k^{[3]}\).

## 7. Solutions

**6.1.** The coefficient matrix of \((F,J)\mapsto(L,M)\) is \(\begin{pmatrix}x_0^2&-(1+2sx_0)\\1-2sx_0&4s^2\end{pmatrix}\), with determinant \(4s^2x_0^2+(1+2sx_0)(1-2sx_0)\), which is \(4s^2x_0^2+1-4s^2x_0^2=1\). Its inverse is \(\begin{pmatrix}4s^2&1+2sx_0\\-(1-2sx_0)&x_0^2\end{pmatrix}\), which is (4.2).

**6.2.** Write \(H=x^2F-(1+2sx)J-p^2J^2-pu\) with \(x=s^2+u^3+p^2F\). Then \(\Delta(x)=2s\Delta(s)+3u^2\Delta(u)+p^2\Delta(F)\), which is \(-6p^2sxu^2-3p^2u^2+p^2(6sx+3)u^2=0\). So
\[
\begin{aligned}
&\Delta(H)=x^2\Delta(F)-2x\Delta(s)J\\
&\quad-(1+2sx)\Delta(J)-2p^2J\Delta(J)\\
&\quad-p\Delta(u).
\end{aligned}
\] Substituting (3.1), the first four terms are 
\[
\begin{aligned}
&x^2(6sx+3)u^2+6p^2x^2u^2J\\
&\quad-3(1+2sx)x^2u^2-6p^2x^2u^2J=0,
\end{aligned}
\]
and the last is \(p^3\).

**6.3.** Modulo \(p\), (4.3) gives \(H\equiv L\), and \(P/pP=k[s,u,M,L]\) by (4.1) and (4.2). So \(A/pA=P/(p,H)\), which is \(k[s,u,M,L]/(L)\cong k[s,u,M]\).

## References

- [OpenAI-cancellation] OpenAI, An explicit failure of complex affine-space cancellation, preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf
- [Gupta-survey] N. Gupta, The Zariski cancellation problem and related problems in affine algebraic geometry, Proceedings of the International Congress of Mathematicians 2022, vol. 3, EMS Press, 2023, 1578–1598. https://doi.org/10.4171/ICM2022/151
- [Gupta] N. Gupta, On Zariski's cancellation problem in positive characteristic, Adv. Math. 264 (2014), 296–307. https://arxiv.org/abs/1309.1368
- [AEH] S. S. Abhyankar, P. Eakin, W. Heinzer, On the uniqueness of the coefficient ring in a polynomial ring, J. Algebra 23 (1972), 310–342. https://doi.org/10.1016/0021-8693(72)90134-2
- [Fujita] T. Fujita, On Zariski problem, Proc. Japan Acad. Ser. A Math. Sci. 55 (1979), 106–110. https://doi.org/10.3792/pjaa.55.106
- [Miyanishi–Sugie] M. Miyanishi, T. Sugie, Affine surfaces containing cylinderlike open sets, J. Math. Kyoto Univ. 20 (1980), 11–42. https://doi.org/10.1215/kjm/1250522319

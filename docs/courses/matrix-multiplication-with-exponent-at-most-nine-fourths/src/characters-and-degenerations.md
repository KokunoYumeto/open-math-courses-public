# Characters and degenerations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *character* is a numerical invariant of tensors that adds on direct sums, multiplies on tensor products and decreases under restriction. Strassen introduced these invariants as the points of the *asymptotic spectrum* of tensors; the paper [CVZ] gives an account and constructs a large family of them. The ranks of the three flattenings are the simplest examples. This lesson proves the properties of characters that the course uses: their values on dot products and on matrix multiplication (Section 2), their monotonicity under degenerations (Section 3), and the effect of permuting legs (Section 4). Notation from [Tensors, rank and the exponent](tensors-rank-and-the-exponent.md) is used throughout: the semiring \(S\), the rank \(R\), the flattening ranks, \(T_n\), \(C(a,b)\) and the dot products \(B_X(m)\), \(B_Y(m)\), \(B_Z(m)\).

## 1. Characters

**Definition 2.1.** A *character* is a map \(\lambda:S\to[0,\infty)\) such that, for all \(A,U,A'\in S\),
\[
\begin{aligned}
\lambda(A+U)&=\lambda(A)+\lambda(U),\\
\lambda(AU)&=\lambda(A)\,\lambda(U),
\end{aligned}
\]
\(\lambda(A)\ge\lambda(A')\) whenever \(A\ge A'\), and \(\lambda(1)=1\).

**Lemma 2.2.** Every character satisfies \(\lambda(0)=0\) and \(\lambda(m)=m\) for integers \(m\ge0\), and \(1\le\lambda(A)\le R(A)\) for every nonzero \(A\).

**Proof.** Additivity gives \(\lambda(0)=\lambda(0+0)=2\lambda(0)\) and \(\lambda(m)=m\lambda(1)=m\). A nonzero tensor satisfies \(A\ge1\) by Lemma 1.2(d), so \(\lambda(A)\ge1\); and \(R(A)\ge A\) gives \(\lambda(A)\le\lambda(R(A))=R(A)\). \(\square\)

**Example 2.3.** By Lemma 1.5, each of the flattening ranks \(\rho_X\), \(\rho_Y\), \(\rho_Z\) is a character.

## 2. Dot-product exponents

**Lemma 2.4.** For every character \(\lambda\) there are numbers \(p_X,p_Y,p_Z\in[0,1]\) such that, for every \(m\ge1\),
\[
\begin{aligned}
\lambda(B_X(m))&=m^{p_X},\\
\lambda(B_Y(m))&=m^{p_Y},\\
\lambda(B_Z(m))&=m^{p_Z}.
\end{aligned}
\]

**Proof.** Put \(f(m)=\lambda(B_X(m))\). By Lemma 1.9(a), \(f(mn)=f(m)f(n)\) and \(f\) is nondecreasing; by Lemma 2.2 and Lemma 1.9(b), \(1\le f(m)\le m\). Also \(B_X(1)\cong1\), so \(f(1)=1\). Put \(p_X=\log_2f(2)\in[0,1]\). Let \(m\ge2\) and \(r\ge1\), and let \(\ell=\lfloor r\log_2m\rfloor\), so that \(2^\ell\le m^r<2^{\ell+1}\). Then
\[
f(2)^\ell\le f(m)^r\le f(2)^{\ell+1}.
\]
Take logarithms, divide by \(r\) and let \(r\to\infty\); since \(\ell/r\to\log_2m\), this gives \(\log f(m)=p_X\log m\). The same argument applies to \(B_Y\) and \(B_Z\). \(\square\)

We write \(p_X(\lambda)\), \(p_Y(\lambda)\), \(p_Z(\lambda)\) for these exponents, and
\[
t(\lambda)=\tfrac13\bigl(p_X(\lambda)+p_Y(\lambda)+p_Z(\lambda)\bigr).
\]

**Lemma 2.5.** Every character satisfies \(\lambda(T_m)=m^{3t(\lambda)}\) for \(m\ge1\), and \(\frac13\le t(\lambda)\le1\).

**Proof.** By Lemma 1.9(c) and multiplicativity, \(\lambda(T_m)\) is the product of \(\lambda(B_X(m))\), \(\lambda(B_Y(m))\) and \(\lambda(B_Z(m))\), which is \(m^{3t}\). Lemma 1.6(c) gives \(T_2\ge2\), so \(2^{3t}\ge2\) and \(t\ge\frac13\). Lemma 1.6(b) and Lemma 2.2 give \(2^{3t}\le R(T_2)\le8\), so \(t\le1\). \(\square\)

**Example 2.6.** For \(\lambda=\rho_X\): the \(X\)-flattening of \(B_X(m)\) has a single row, while those of \(B_Y(m)\) and \(B_Z(m)\) have \(m\) nonzero rows with disjoint supports. So \(p_X(\rho_X)=0\), \(p_Y(\rho_X)=p_Z(\rho_X)=1\), \(t(\rho_X)=\frac23\), and \(\rho_X(T_m)=m^2\), in accordance with Lemma 1.6(b).

The main estimate of the course is \(t(\lambda)\le\frac34\) for every character (Theorem 5.2).

## 3. Degenerations

**Definition 2.7.** Let \(A\) be a tensor and \(A''\) a restriction of \(A\). Give every variable \(v\) of \(A''\) an integer weight \(w(v)\), negative values allowed, and define the weight of a term \(c\,xyz\) with \(c\ne0\) as \(w(x)+w(y)+w(z)\). The sum \(A'\) of the terms of \(A''\) of least weight is a *degeneration* of \(A\), written \(A\rightsquigarrow A'\). (If \(A''=0\), then \(A'=0\).)

Taking all weights zero shows that every restriction is a degeneration.

**Lemma 2.8.** Let \(U_0,\dots,U_Q\) be tensors in the same variables and \(c_0,\dots,c_Q\in F\). Then \(\sum_qc_qU_q\) is a restriction of \(U_0\oplus\dots\oplus U_Q\).

**Proof.** The direct sum has a separate copy of the variables for each summand. In the copy belonging to \(U_q\), substitute \(c_qx\) for the copy of each \(X\)-variable \(x\), and the variable itself for the copy of each \(Y\)- and \(Z\)-variable. \(\square\)

**Lemma 2.9** (interpolation). If \(A\rightsquigarrow A'\), then \(\lambda(A)\ge\lambda(A')\) for every character \(\lambda\).

**Proof.** We may assume \(A''\ne0\). Let \(w_0\) be the least weight of a term of \(A''\) and \(w_0+L\) the largest one; for \(0\le l\le L\) let \(A_l\) be the sum of the terms of weight \(w_0+l\), so \(A_0=A'\). For \(\varepsilon\in F\), \(\varepsilon\ne0\), substitute \(\varepsilon^{w(x)-w_0}x\) for each \(X\)-variable \(x\) of \(A''\) and \(\varepsilon^{w(v)}v\) for each \(Y\)- and \(Z\)-variable \(v\). This multiplies a term of weight \(w_0+l\) by \(\varepsilon^l\) and turns \(A''\) into
\[
A_\varepsilon=A'+\varepsilon A_1+\dots+\varepsilon^LA_L,
\]
a restriction of \(A''\) and hence of \(A\).

Fix \(j\ge1\). Expanding the tensor product multilinearly,
\[
A_\varepsilon^{\otimes j}=\sum_{l=0}^{jL}\varepsilon^lG_l,
\]
where the \(G_l\) are tensors in the variables of \(A''^{\otimes j}\) and \(G_0=A'^{\otimes j}\). Choose distinct nonzero \(\varepsilon_0,\dots,\varepsilon_{jL}\in F\). The Vandermonde matrix \((\varepsilon_q^l)\) is invertible, so there are \(c_0,\dots,c_{jL}\in F\) with \(\sum_qc_q\varepsilon_q^l=1\) for \(l=0\) and \(=0\) for \(1\le l\le jL\). Then \(\sum_qc_qA_{\varepsilon_q}^{\otimes j}=A'^{\otimes j}\). By Lemma 2.8 and Lemma 1.2(b),
\[
A'^{\otimes j}\le\bigoplus_{q=0}^{jL}A_{\varepsilon_q}^{\otimes j}\le(jL+1)\,A^{\otimes j}.
\]
Applying \(\lambda\) gives \(\lambda(A')^j\le(jL+1)\lambda(A)^j\), that is, \(\lambda(A')\le(jL+1)^{1/j}\lambda(A)\). The number \(L\) does not depend on \(j\); letting \(j\to\infty\) proves the lemma. \(\square\)

**Example 2.10.** The tensor \(W=x_1y_0z_0+x_0y_1z_0+x_0y_0z_1\) is a degeneration of \(2\) (Exercise 2.3), so \(\lambda(W)\le2\) for every character, although \(R(W)=3\).

## 4. Permuted characters

For a permutation \(\pi\) of the legs and a character \(\lambda\), put \(\lambda_\pi(A)=\lambda(\pi A)\). Since \(\pi\) acts on \(S\) by an automorphism of ordered semirings ([Tensors, rank and the exponent](tensors-rank-and-the-exponent.md), Section 1), \(\lambda_\pi\) is a character.

**Lemma 2.11.** For every character \(\lambda\) and every permutation \(\pi\), the three numbers \(p_X(\lambda_\pi)\), \(p_Y(\lambda_\pi)\), \(p_Z(\lambda_\pi)\) are \(p_X(\lambda)\), \(p_Y(\lambda)\), \(p_Z(\lambda)\) in some order; in particular \(t(\lambda_\pi)=t(\lambda)\). Moreover
\[
\begin{aligned}
\sum_{\pi}p_X(\lambda_\pi)&=2\bigl(p_X+p_Y+p_Z\bigr)(\lambda)\\
&=6\,t(\lambda),
\end{aligned}
\]
the sum taken over the six permutations of the legs.

**Proof.** Write \(B_\ell(m)\) for the dot product whose single variable lies on the leg \(\ell\). The argument of Exercise 1.4 shows \(\pi B_\ell(m)\cong B_{\pi(\ell)}(m)\). Hence \(\lambda_\pi(B_\ell(m))=m^{p_{\pi(\ell)}(\lambda)}\), that is, \(p_\ell(\lambda_\pi)=p_{\pi(\ell)}(\lambda)\) for each leg \(\ell\). This proves the first statement. For the sum, \(\pi(X)\) runs through each of the three legs for exactly two of the six permutations. \(\square\)

## 5. Exercises

**2.1** (easy). Compute \(p_X\), \(p_Y\), \(p_Z\) and \(t\) for the characters \(\rho_Y\) and \(\rho_Z\).

**2.2** (easy). Show that the map \(A\mapsto(\rho_X(A)\rho_Y(A))^{1/2}\) is multiplicative and monotone but not a character.

**2.3** (medium). Restrict \(2=x_ay_az_a+x_by_bz_b\) by the substitution \(x_a=x_0+x_1\), \(y_a=y_0+y_1\), \(z_a=z_0+z_1\), \(x_b=-x_0\), \(y_b=y_0\), \(z_b=z_0\), and give the variables with index \(1\) the weight \(1\) and those with index \(0\) the weight \(0\). Show that the resulting degeneration is \(W\). Compute \(\rho_X(W)\), and show that \(R(W)\ge3\) by checking that \(W\) is not a sum of two products of linear forms.

**2.4** (easy). Show that every character satisfies \(\max(a^{p_Y},b^{p_X})\le\lambda(C(a,b))\le a+b-1\).

## 6. Solutions

**2.1.** For \(\rho_Y\), the \(Y\)-flattening of \(B_Y(m)\) has one row and those of \(B_X(m)\) and \(B_Z(m)\) have rank \(m\): \(p_Y=0\), \(p_X=p_Z=1\), \(t=\frac23\). Likewise \(\rho_Z\) has \(p_Z=0\), \(p_X=p_Y=1\), \(t=\frac23\).

**2.2.** Both factors are multiplicative and monotone, hence so is the geometric mean. For \(A=B_X(2)\) and \(U=B_Y(2)\), the values are \(\sqrt{1\cdot2}=\sqrt2\) each, while \(A\oplus U\) has \(\rho_X=1+2=3\) and \(\rho_Y=2+1=3\), so the value at \(A\oplus U\) is \(3\ne2\sqrt2\).

**2.3.** The substitution gives \((x_0+x_1)(y_0+y_1)(z_0+z_1)-x_0y_0z_0\), the sum of the seven products of the variables in which at least one index is \(1\). The terms with exactly one index \(1\) have weight \(1\), the others weight \(2\) or \(3\); so the degeneration is \(W\). The \(X\)-flattening has the rows \(x_1\) (one entry, at \((y_0,z_0)\)) and \(x_0\) (two entries), so \(\rho_X(W)=2\). Suppose \(W=\varphi_1\psi_1\chi_1+\varphi_2\psi_2\chi_2\). Write \(W=x_0(y_1z_0+y_0z_1)+x_1y_0z_0\); the two slices \(y_1z_0+y_0z_1\) and \(y_0z_0\), as bilinear forms in \(y,z\), are combinations of the rank-one forms \(\psi_1\chi_1\) and \(\psi_2\chi_2\). Since the slices are linearly independent, the span of \(\psi_1\chi_1\) and \(\psi_2\chi_2\) equals the span of the two slices. That span consists of the forms \(\alpha(y_1z_0+y_0z_1)+\beta y_0z_0\), with matrix \(\left(\begin{smallmatrix}\beta&\alpha\\\alpha&0\end{smallmatrix}\right)\) in the bases \((y_0,y_1)\), \((z_0,z_1)\), of determinant \(-\alpha^2\). The forms of rank one in it have \(\alpha=0\), so they are multiples of \(y_0z_0\), and two of them cannot span a two-dimensional space. This contradiction shows \(R(W)\ge3\); the three terms of \(W\) give \(R(W)=3\).

**2.4.** Substituting \(0\) for \(x_1,\dots,x_{a-1}\) restricts \(C(a,b)\) to \(C(1,b)\cong B_X(b)\); substituting \(0\) for \(y_1,\dots,y_{b-1}\) restricts it to \(\sum_ix_iy_0z_i\cong B_Y(a)\). The upper bound is Lemma 2.2 with Lemma 1.8(a).

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
- [CVZ] M. Christandl, P. Vrana and J. Zuiddam, *Universal points in the asymptotic spectrum of tensors*, Journal of the American Mathematical Society 36 (2023), 31–79; arXiv:1709.07851. https://arxiv.org/abs/1709.07851
- [Bl] M. Bläser, *Fast matrix multiplication*, Theory of Computing Library, Graduate Surveys 5 (2013); approximate algorithms and their conversion into exact ones. https://theoryofcomputing.org/articles/gs005/

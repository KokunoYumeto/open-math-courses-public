# A differential injectivity lemma

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of Theorem A in [Vanishing on products](vanishing-on-products.md) recovers a polynomial from a sequence of its directional derivatives. Each derivative moves one degree from a vector variable \(U\) to another variable \(Y\), and it can be undone, in the sense that it is injective, whenever the degree in \(U\) exceeds the degree in \(Y\). This lesson proves that statement, following OpenAI [OpenAI-FH, Section 3], with an inner product on polynomials for which differentiation and multiplication are adjoint. It is the injectivity of a raising operator on the positive weights of an \(\mathfrak{sl}_2\)-representation.

## 1. Vector variables and directional derivatives

Fix a basis of \(V\), of dimension \(n\ge1\). A *vector variable* \(U\) is a block \(U=(U_1,\dots,U_n)\) of \(n\) independent scalar variables; a polynomial in several vector variables is a polynomial in all their coordinates, with complex coefficients. Substituting vectors of \(V\) for the vector variables, through their coordinates, gives the values of the polynomial. A polynomial that vanishes at every point is zero; this follows by induction on the number of variables, since a nonzero polynomial in one variable has finitely many roots.

For two vector variables \(U\) and \(Y\) put
\[
D_{Y,U}=\sum_{k=1}^nY_k\frac{\partial}{\partial U_k}.
\]
It lowers the degree in \(U\) by one and raises the degree in \(Y\) by one. If \(F(U)\) is a polynomial and \(y\in V\), then substituting \(Y=y\) in \(D_{Y,U}F\) gives the derivative of \(F\) in the direction \(y\).

In the symmetric algebra \(\operatorname{Sym}V\), with coordinates through the basis, \(D_{Y,U}(U^j)=j\,U^{j-1}Y\): the map \(U\mapsto U^j\) has derivative \(y\mapsto jU^{j-1}y\) by the product rule. If \(T\) is a symmetric multilinear form on \(\operatorname{Sym}^bV\) and \(w_1,\dots,w_{a-1}\in\operatorname{Sym}^bV\) do not depend on \(U\), then
\[
\begin{aligned}
&D_{Y,U}\,T(w_1,\dots,w_{a-1},U^b)\\
&\quad=b\,T(w_1,\dots,w_{a-1},U^{b-1}Y),
\end{aligned}
\]
because \(T\) is linear in its last argument.

## 2. The Fischer inner product

Let \(X=(X_1,\dots,X_N)\) list all the scalar variables in use. For polynomials \(f=\sum_\alpha f_\alpha X^\alpha\) and \(g=\sum_\alpha g_\alpha X^\alpha\) put
\[
\langle f,g\rangle=\sum_\alpha\alpha!\,f_\alpha\overline{g_\alpha},\qquad\alpha!=\prod_k\alpha_k! .
\]
This is a positive definite Hermitian inner product, in which distinct monomials are orthogonal and \(\|X^\alpha\|^2=\alpha!\). It is the *Fischer* or *apolar* inner product.

**Lemma 2.1.** For every \(k\), differentiation by \(X_k\) and multiplication by \(X_k\) are adjoint: \(\langle\partial f/\partial X_k,g\rangle=\langle f,X_kg\rangle\).

*Proof.* By linearity it suffices to take monomials \(f=X^\alpha\) and \(g=X^\beta\). Then \(\partial f/\partial X_k=\alpha_kX^{\alpha-e_k}\) (zero if \(\alpha_k=0\)), and both sides are \(\alpha!\) if \(\alpha=\beta+e_k\), and \(0\) otherwise. \(\square\)

## 3. The lemma

**Lemma 3.1** (OpenAI). Let \(p,q\ge0\) be integers, and \(U,Y\) two vector variables. Let \(\mathcal H\) be the space of polynomials, possibly involving further variables, that are homogeneous of degree \(p\) in \(U\) and of degree \(q\) in \(Y\). If \(p>q\), then \(D_{Y,U}\) is injective on \(\mathcal H\).

*Proof.* Put \(D=D_{Y,U}\) and \(E=D_{U,Y}=\sum_kU_k\,\partial/\partial Y_k\). By Lemma 2.1, the adjoint of \(Y_k\,\partial/\partial U_k\) is \(U_k\,\partial/\partial Y_k\), so \(D^*=E\). A direct computation, using that variables of different blocks commute with each other's derivatives, gives
\[
\begin{gathered}
ED-DE=N_U-N_Y,\\
N_U=\sum_kU_k\frac{\partial}{\partial U_k},\\
N_Y=\sum_kY_k\frac{\partial}{\partial Y_k} .
\end{gathered}
\]
Indeed,
\[
\begin{aligned}
&U_k\partial_{Y_k}Y_l\partial_{U_l}-Y_l\partial_{U_l}U_k\partial_{Y_k}\\
&\quad=\delta_{kl}(U_k\partial_{U_l}-Y_l\partial_{Y_k}).
\end{aligned}
\]
By Euler's identity, \(N_Uh=ph\) and \(N_Yh=qh\) for \(h\in\mathcal H\). Hence
\[
\begin{aligned}
&\|Dh\|^2-\|Eh\|^2\\
&\quad=\langle EDh,h\rangle-\langle DEh,h\rangle\\
&\quad=(p-q)\|h\|^2 .
\end{aligned}
\]
If \(Dh=0\), the left side is \(-\|Eh\|^2\le0\), while the right side is \((p-q)\|h\|^2\ge0\), with equality only for \(h=0\). \(\square\)

A composition of such operators is injective on a space of homogeneous polynomials when, before each operator, the polynomials it is applied to have source degree larger than target degree: each operator then maps an injectivity domain of Lemma 3.1 into the domain of the next one.

## 4. Exercises

**4.1** (easy). Let \(n=2\). Show that \(h=U_1Y_2-U_2Y_1\) is a nonzero polynomial of degree \(1\) in \(U\) and in \(Y\) with \(D_{Y,U}h=0\). So Lemma 3.1 fails for \(p=q\).

**4.2** (easy). Verify \(\|Dh\|^2-\|Eh\|^2=(p-q)\|h\|^2\) for \(n=1\) and \(h=U^pY^q\).

**4.3** (medium). For polynomials in the variables \(U\) and \(Y\) only, show that \(D_{Y,U}\) maps the polynomials of bidegree \((p,q)\) onto those of bidegree \((p-1,q+1)\) when \(p\le q+1\). (Hint: \(E=D^*\) is injective on bidegree \((p-1,q+1)\) when \(q+1>p-1\).)

## 5. Solutions

**4.1.** \(D_{Y,U}h=Y_1Y_2-Y_2Y_1=0\).

**4.2.** \(Dh=pU^{p-1}Y^{q+1}\) and \(Eh=qU^{p+1}Y^{q-1}\), so
\[
\begin{aligned}
&\|Dh\|^2-\|Eh\|^2\\
&\quad=p^2(p-1)!\,(q+1)!\\
&\qquad-q^2(p+1)!\,(q-1)!\\
&\quad=p!\,q!\,\bigl(p(q+1)-q(p+1)\bigr)\\
&\quad=(p-q)\|h\|^2 .
\end{aligned}
\]

**4.3.** By Lemma 3.1 with the roles of \(U\) and \(Y\) exchanged, \(E\) is injective on bidegree \((p-1,q+1)\) when \(q+1>p-1\). For a linear map \(D\) between finite-dimensional inner product spaces, the image of \(D\) is the orthogonal complement of the kernel of \(D^*=E\), so \(D\) is onto.

## References

- [OpenAI-FH] OpenAI, *Quadratic stabilization of the canonical Foulkes–Howe map*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026

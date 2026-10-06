# Wronskians and Roth's rational-point lemma

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Original exposition and proofs: public domain (CC0), except the explicitly credited polynomial-curve calculation under CC BY 4.0. Linked formal normalization proofs retain their own licence.*

The last lesson produced a polynomial with many vanishing Taylor coefficients at an algebraic point. We now need to stop that vanishing from persisting at a carefully chosen rational point. The rational coordinates alone are insufficient: a polynomial can contain a high power of \(qX-p\). Its height must also be small, and its degrees must decrease quickly from one variable to the next.

A Wronskian separates the last variable from the others. Its determinant is built from derivatives of the original polynomial, so it retains vanishing information. Its factorization has one factor in the first variables and one in the last; induction controls both. We use the divided derivatives, height and index of The index method for rational approximation, with their proofs in Lemmas 10.3–10.5.

## A rational zero has a coefficient cost

Take \(P=(qX-p)^\ell\), with \(p/q\) reduced and \(q>1\). Its index with weight \(d\ge\ell\) is \(\ell/d\), but its leading coefficient is \(q^\ell\). A small-height assumption can therefore limit the multiplicity even when the rational point lies far from the origin. The first exercise derives this exact one-variable bound. The obstacle in several variables is that a polynomial can share its vanishing among different directions; a root factor in one variable need not explain it.

We will transform \(P\) into a nonzero product of two polynomials in disjoint variable sets. Before the general construction, try \(P=1+X+X^2Y\). The derivative determinant is

\[
 \det\begin{pmatrix}P&\partial_YP\\\partial_XP&\partial_X\partial_YP\end{pmatrix}
 =\det\begin{pmatrix}1+X+X^2Y&X^2\\1+2XY&2X\end{pmatrix}
 =X(X+2).
\]

It is a nonzero polynomial, yet it vanishes when \(X=0\). Thus a Wronskian certificate gives a nonzero polynomial, not a nonzero numerical determinant at every selected point. Roth's lemma controls its *index* at the rational point through its height and the separation of the degrees. This distinction explains why Sections 2 and 3 are both needed.

## 1. Detecting independence by derivatives

Let \(K\) be a field of characteristic zero and \(F=K(X_1,\ldots,X_r)\). For rational functions \(f_1,\ldots,f_k\), a generalized Wronskian is a determinant

\[
                      \det(D_{\boldsymbol i_\ell}f_j)_{1\leq\ell,j\leq k},
                      \qquad |\boldsymbol i_\ell|\leq\ell-1.
                      \tag{11.1}
\]

The derivatives in different rows can involve different variables. This freedom is essential.

### Lemma 11.1. The generalized Wronskian criterion

The functions \(f_1,\ldots,f_k\in F\) are linearly independent over \(K\) if and only if some determinant (11.1) is nonzero.

**Proof.** A constant linear relation makes the columns of every such determinant dependent. For the converse, write \(\boldsymbol f=(f_1,\ldots,f_k)\), and let \(E_s\subset F^k\) be the row space spanned over \(F\) by all \(\partial^{\boldsymbol i}\boldsymbol f\) with \(|\boldsymbol i|\leq s\). Suppose \(E_s=E_{s+1}\). The product rule then shows that every partial derivative preserves \(E_s\), including derivatives of arbitrary rational coefficients in its linear combinations.

Choose its row-reduced basis with an identity matrix in a set of pivot columns. The derivative of any basis row has zero entries in those columns and remains in \(E_s\); its basis coefficients are read from the pivot entries, so they are all zero. Every entry of the reduced basis is therefore killed by all partial derivatives and belongs to \(K\). Indeed, if a reduced fraction \(A/B\) has derivative zero, coprimality implies \(A\mid\partial_jA\) and \(B\mid\partial_jB\); degree forces both derivatives to be zero. Applying this for every \(j\) makes \(A,B\) constants.

If \(\dim_F E_s<k\), a nonzero vector over \(K\) annihilates this constant basis. It then annihilates \(\boldsymbol f\), giving a forbidden \(K\)-linear relation. Thus the dimension of \(E_s\) increases by at least one at every step until it is \(k\). Since \(\dim E_0=1\), \(\dim E_{\ell-1}\geq\ell\) for \(1\leq\ell\leq k\). Starting with row \(\boldsymbol f\), choose successively independent derivative rows of order at most \(\ell-1\); such a row exists among the generators of \(E_{\ell-1}\). Their determinant is nonzero. Replacing ordinary derivatives by divided derivatives merely multiplies each row by a nonzero element of \(K\). \(\square\)

For example, the functions \(1,X,Y\) have nonzero Wronskian

\[
              \det\begin{pmatrix}1&X&Y\\0&1&0\\0&0&1\end{pmatrix}=1.
\]

There is no single coordinate derivative making both \(\partial_jX\) and \(\partial_jY\) independent: one is zero. A proof which assumes such a coordinate exists does not cover several variables. The row-space proof avoids that assumption.

### Lemma 11.2. The one-variable Wronskian

For rational functions of one variable that are \(K\)-independent, the determinant with rows \(D_0,\ldots,D_{k-1}\) is nonzero.

**Proof.** Lemma 11.1 supplies independent derivative rows with orders at most \(\ell-1\). The first has order zero; the second must have order one, since a repeat would be dependent. Inductively the \(\ell\)-th row must have order \(\ell-1\): all smaller orders already appear among its predecessors. Thus the determinant supplied by that lemma is the one asserted. \(\square\)

### A polynomial curve calculation (Goel–Lunia–Ray)

This paragraph adapts the generalized-Wronskian calculation in §2.6 of Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*, arXiv:2502.00731v2](https://arxiv.org/abs/2502.00731v2), from the authors' supplied TeX source. It retains [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The adaptation chooses the substitution base strictly larger than every partial degree and supplies the derivative expansion. The authors have not reviewed this adaptation.

For independent polynomials \(\varphi_1,\ldots,\varphi_k\) in \(r\) variables, choose an integer \(b\) greater than every partial degree and substitute

\[
 X_j=t^{b^{j-1}}\quad(1\le j\le r).
\]

The exponent of a substituted monomial is \(\sum_j a_jb^{j-1}\). Since \(0\le a_j<b\), uniqueness of base-\(b\) expansion proves that distinct monomials remain distinct. The substituted polynomials \(\Phi_j(t)\) are therefore independent, and Lemma 11.2 gives a nonzero one-variable Wronskian. The chain rule, followed by induction on \(h\), gives

\[
 \frac{d^h}{dt^h}\Phi_j(t)
 =\sum_{|\boldsymbol i|\le h}c_{h,\boldsymbol i}(t)
       (D_{\boldsymbol i}\varphi_j)(t,t^b,\ldots,t^{b^{r-1}}),
 \qquad c_{h,\boldsymbol i}\in\mathbb Q[t].
\]

For \(h=0\) this is the substitution itself. Differentiating a coefficient leaves the derivative order unchanged; differentiating a substituted partial derivative raises that order by one and multiplies by a polynomial derivative of \(t^{b^{j-1}}\). This proves the asserted order bound and polynomial coefficients. Expand the one-variable Wronskian row by row. Each term is a polynomial coefficient times a substituted generalized Wronskian with row orders at most \(0,1,\ldots,k-1\). Since the sum is nonzero, at least one of these generalized Wronskians is nonzero.

This gives a useful interpretation of the polynomial criterion: one curve can probe all coordinates, while expansion of its derivatives reveals the mixed rows that a single coordinate derivative misses. The rational-function criterion, in its full generality, is proved by the row-space argument above.

## 2. Separating the final variable

Every rational-coefficient polynomial in \(m\) variables has a presentation

\[
 P(\boldsymbol X',Y)=\sum_{j=1}^k A_j(\boldsymbol X')B_j(Y),
 \qquad \boldsymbol X'=(X_1,\ldots,X_{m-1}).
 \tag{11.2}
\]

Choose one of least length over \(\mathbb Q\). Then both families are rationally independent: a dependence in one allows one term to be eliminated. If \(\deg_Y P\leq d_m\), taking powers of \(Y\) first gives \(k\leq d_m+1\). Minimal presentations can be obtained by row and column operations on the finite coefficient matrix, so their factors have rational coefficients and the same variable-degree bounds as \(P\).

Choose derivative rows \(D_{\boldsymbol i_\ell}\) for the first family by Lemma 11.1, with \(|\boldsymbol i_\ell|\leq\ell-1\). Define

\[
 W=\det\bigl(D_{\boldsymbol i_\ell}D_{j-1,Y}P\bigr)_{\ell,j=1}^k.
\]

Multiplying the two matrices obtained from (11.2) gives

\[
 W=U(\boldsymbol X')V(Y),\quad
 U=\det(D_{\boldsymbol i_\ell}A_j),\quad
 V=\det(D_{\ell-1,Y}B_j),\quad UV\ne0.
 \tag{11.3}
\]

Both nonvanishing assertions follow from the proved Wronskian criteria. If \(P\) is an integer polynomial, every entry of \(W\) is an integer polynomial, hence so is \(W\). The individual rational factors can be replaced by primitive integer factors \(U_0,V_0\): then \(W=cU_0V_0\) for a nonzero integer \(c\). To justify this, clear denominators and divide out contents. A product of primitive integer polynomials is primitive, since modulo each prime its two nonzero reductions have nonzero product. The remaining rational scalar must consequently be an integer. Because the variables of the factors are disjoint, their coefficients form an outer product, giving

\[
 H(W)=|c|H(U_0)H(V_0),
 \quad H(U_0),H(V_0)\leq H(W),
 \quad \deg_{X_j}U_0\leq kd_j,
 \quad \deg_YV_0\leq kd_m.
 \tag{11.4}
\]

For \(P(X,Y)=1+XY\), (11.3) is the exact computation

\[
                     W=\det\begin{pmatrix}1+XY&X\\Y&1\end{pmatrix}=1.
\]

The determinant converts a sum of separated products into a single separated product without losing its nonzero character.

## 3. Vanishing survives in the determinant

**Track the costs before using the induction.** The separated determinant has \(k\) rows, so multiplication adds the surviving index \(k\) times. Its degrees can also grow by \(k\). Those two appearances of \(k\) must be compared using the same weights. The following argument first keeps the original weights, and only later uses the enlarged weights for the two induction hypotheses. Dividing an index by \(k\) too early would lose the gain.

Suppose \(d_j\geq C d_{j+1}\), \(C>1\), and \(\vartheta\) is the index of \(P\) at some point with weights \((d_1,\ldots,d_m)\). Each entry in column \(j+1\), \(0\leq j<k\), has index at least

\[
 \max\left\{0,\vartheta-\frac{|\boldsymbol i_\ell|}{d_{m-1}}
                              -\frac{j}{d_m}\right\}
 \geq\max\{0,\vartheta-C^{-1}-j/d_m\}.
 \tag{11.5}
\]

Here \(|\boldsymbol i_\ell|\leq k-1\leq d_m\). Every term in the determinant uses each column once, so the product and sum index rules yield the sum of the last bounds as a lower bound for \(\operatorname{ind}W\).

In particular, if \(0<\varepsilon\leq1\), \(\vartheta>\varepsilon\), and \(C\geq4/\varepsilon\), then

\[
                         \operatorname{ind}W\geq\varepsilon^2k/16.
                         \tag{11.6}
\]

For \(k=1\), the determinant is \(P\) and this is immediate. For \(k\geq2\), keep the columns \(0\leq j\leq\lfloor\varepsilon(k-1)/2\rfloor\). Since \(d_m\geq k-1\), their \(j/d_m\) is at most \(\varepsilon/2\); each contributes at least \(\varepsilon/4\). There are at least \(\varepsilon(k-1)/2\geq\varepsilon k/4\) of them, proving (11.6). A sharp quadratic constant is unnecessary; this definite positive multiple of \(k\) is enough.

## 4. Roth's lemma with all parameters

### Theorem 11.3. Small index at a rational point

For every positive integer \(m\) and every \(\varepsilon>0\), there is a constant \(C=C(m,\varepsilon)>1\) with the following property. Let \(d_1,\ldots,d_m\) be positive integers with \(d_j\geq C d_{j+1}\), and let \(p_j/q_j\) be reduced rationals satisfying

\[
 q_j>0,\qquad q_j\geq2^{2mC},\qquad
                       q_j^{d_j}\geq q_1^{d_1}\quad(1\leq j\leq m).
 \tag{11.7}
\]

Every nonzero \(P\in\mathbb Z[X_1,\ldots,X_m]\) with

\[
 \deg_{X_j}P\leq d_j,\qquad H(P)\leq q_1^{d_1/C}
 \tag{11.8}
\]

has index at \((p_1/q_1,\ldots,p_m/q_m)\), with these weights, at most \(\varepsilon\).

**Proof.** It suffices to treat \(0<\varepsilon\leq1\); for larger \(\varepsilon\), use the constant for one. We induct on \(m\). For \(m=1\), if \(p/q\) has multiplicity \(\ell\), the primitive polynomial \(qX-p\) divides \(P\) to power \(\ell\) over \(\mathbb Q[X]\), and Gauss's primitive-product argument makes the quotient integral. Its leading coefficient is a nonzero integer. Thus \(q^\ell\leq H(P)\leq q^{d_1/C}\), so the index is at most \(1/C\). Take \(C(1,\varepsilon)=\max\{2,1/\varepsilon\}\).

For \(m\geq2\), put \(\delta=\varepsilon^2/64\), let \(R=C(m-1,\delta)\) be the induction constant, and choose

\[
                 C\geq\max\{2,4/\varepsilon,192/\varepsilon^2,3R\}.
                 \tag{11.9}
\]

Assume, for contradiction, that the index \(\vartheta\) of \(P\) is greater than \(\varepsilon\). Construct the nonzero separated determinant \(W=cU_0V_0\) of section 2. Equation (11.6) gives its index at least \(\varepsilon^2k/16\).

We bound its height without using heights of the possibly large rational factors in (11.2). Put \(D=\sum d_j\leq md_1\). Each determinant entry is a divided derivative of \(P\); Lemma 10.3 and at most \(\prod(d_j+1)\leq2^D\) coefficients give its sum of absolute coefficients at most \(4^D H(P)\). The sum of absolute coefficients is submultiplicative, and there are \(k!\) determinant terms. Since \(k\leq d_m+1\leq d_1+1\leq2^{d_1}\),

\[
 \begin{aligned}
 H(W)&\leq k!\bigl(4^D H(P)\bigr)^k\\
     &\leq2^{(2m+1)kd_1}q_1^{kd_1/C}
      \leq q_1^{3kd_1/C}.
 \end{aligned}
 \tag{11.10}
\]

The last inequality uses \(\log q_1\geq2mC\log2\), so \((2m+1)\log2\leq2\log q_1/C\). All norms in this computation concern actual integer coefficients.

Apply induction to \(U_0\), using weights \((kd_1,\ldots,kd_{m-1})\). Their ratios are at least \(C\geq R\), and (11.7) remains true after multiplying the exponents by \(k\). The rational denominators also exceed \(2^{2(m-1)R}\). Finally (11.4), (11.10) and \(C\geq3R\) give

\[
                        H(U_0)\leq q_1^{kd_1/R}.
\]

Its index with these larger weights is at most \(\delta\). With the original weights its index is at most \(k\delta\), since multiplying every weight by \(k\) divides the index by \(k\).

For \(V_0\), the denominator ordering gives

\[
                         H(V_0)\leq q_m^{3kd_m/C}.
\]

The one-variable leading-coefficient argument shows that its multiplicity at \(p_m/q_m\) is at most \(3kd_m/C\). Its index with weight \(d_m\) is therefore at most \(3k/C\leq k\varepsilon^2/64\). A polynomial in the first variables has no Taylor exponents in the last variable, and conversely for \(V_0\); the product index rule thus gives

\[
              \operatorname{ind}W
                     \leq k\delta+3k/C
                     \leq\varepsilon^2k/32.
\]

This contradicts (11.6). Every hypothesis has now been used: degree separation bounds derivative losses and permits induction; denominator ordering transfers the height bound to the final factor; large denominators absorb determinant coefficients; the small original height controls both separated integer factors. \(\square\)

## 5. Dyson's two-variable vanishing estimate

For \(0\leq t\leq2\), let

\[
 V(t)=\operatorname{area}\{(u,v)\in[0,1]^2:u+v<t\}
   =\begin{cases}t^2/2,&0\leq t\leq1,\\
                  1-(2-t)^2/2,&1\leq t\leq2.
     \end{cases}
 \tag{11.11}
\]

The strict or non-strict boundary makes no difference to this area. We first give the two intersection facts needed for the estimate. The formal curve normalization inputs are the linked Stacks proofs [032W](https://stacks.math.columbia.edu/tag/032W), [00PD](https://stacks.math.columbia.edu/tag/00PD) and [0C0S](https://stacks.math.columbia.edu/tag/0C0S): complete local rings are Nagata, a one-dimensional normal local ring is a discrete valuation ring, and the complete equal-characteristic ring has a coefficient field. A complete discrete valuation ring with that coefficient field is its one-variable power-series ring: expand successively in a uniformizer and use completeness. These exact author proofs retain the Stacks Project's GNU Free Documentation License.

### Lemma 11.4. Weighted local and global intersections

Let \(r,s\) be positive integers. If two plane polynomial germs \(F,G\) have no common branch, and their Taylor monomials at a point have respective weights \(i/r+j/s\) at least \(a,b\geq0\), then their local intersection length satisfies

\[
                              I(F,G)\geq rsab.
                              \tag{11.12}
\]

For coprime polynomials of bidegrees at most \((r_1,s_1)\), \((r_2,s_2)\), where the first has no vertical-line component, the sum of the intersection lengths at any finite set of points is at most

\[
                              r_1s_2+r_2s_1.
                              \tag{11.13}
\]

**Proof.** Translate the local point to zero and substitute \(x=X^s,y=Y^r\). The power-series ring \(\mathbb C[[X,Y]]\) is free of rank \(rs\) over \(\mathbb C[[x,y]]\), with basis \(X^iY^j\), \(0\leq i<s,0\leq j<r\): separate each exponent by its remainder. It follows by tensoring the finite-dimensional quotient that the substituted intersection length is \(rs\) times the original one. The substituted germs have ordinary vanishing orders at least \(rs a,rs b\).

Here is the ordinary-order inequality used in this calculation. A reduced formal plane curve has finite normalization equal to a finite direct sum of rings \(\mathbb C[[t]]\), by the stated open normalization inputs. If \(H\) does not vanish on any branch, its intersection length with the curve is the sum of its orders on those branches. Indeed the normalization quotient has finite length; in the diagram given by multiplication by \(H\), its kernel and cokernel have equal dimensions, so the lengths before and after normalization agree. On a normalized branch, a germ of ordinary order \(\nu\) has order at least \(\nu\min(\operatorname{ord}_tX,\operatorname{ord}_tY)\). The sum of these minima is the curve's multiplicity: intersect with a generic line through zero, whose branch order is that minimum, and whose substitution in the plane equation has order its least nonzero homogeneous degree. For repeated curve factors, intersection lengths and multiplicities add with the factor multiplicities; this follows from the exact sequence for a product of factors, since \(H\) is a nonzero divisor on each. Thus the ordinary intersection is at least the product of the two ordinary orders. After dividing the substituted bound by \(rs\), we obtain (11.12).

For (11.13), use the resultant in the second coordinate, taking the actual second-coordinate degrees in this argument. Replacing those by the stated upper bounds can only enlarge the final estimate. Its Sylvester determinant has degree in the first coordinate at most \(r_1s_2+r_2s_1\), because every term uses \(s_2\) coefficient rows of the first polynomial and \(s_1\) of the second. It is nonzero by coprimality over \(\mathbb C(x)\). A constant fractional linear change of the second coordinate can be chosen so that all the selected points remain finite and the first polynomial's leading coefficient is nonzero at their first coordinates. There are only finitely many excluded choices, since the first polynomial has no vertical component. Bidegree bounds are preserved by homogenizing this change.

At \(x=x_0\), complete in \(x-x_0\) and divide the first polynomial by its now-unit leading coefficient. It is monic, so the quotient algebra is free of rank \(s_1\) over the complete discrete valuation ring. The resultant, up to a unit, is the determinant of multiplication by the second polynomial on this algebra. Its order equals the length of that map's cokernel: elementary row and column reduction over the discrete valuation ring makes the matrix diagonal with powers of its parameter. Separate the roots of the first polynomial modulo the parameter into factors. The factors lift recursively, since coprimality makes the coefficient correction equations invertible by their polynomial Bezout identity. The resulting product decomposition of the completed algebra identifies the cokernel length with the sum of the local intersection lengths at those roots. Its polynomial quotient agrees with the formal local quotient by successive reduction modulo powers of the parameter. Hence the resultant order at \(x_0\) is at least the sum for our chosen roots. Summing at the distinct first coordinates and using the degree of the nonzero resultant proves (11.13). \(\square\)

### Lemma 11.5. Removing axis factors from the area bound

Let \(0\leq u,v\leq1\), and let nonnegative numbers \(a_h,b_h,c_h\) satisfy

\[
 \sum a_h\leq1-u,\quad\sum b_h\leq1-v,\quad
                    c_h\leq\min(u,v).
\]

Then

\[
             \sum_h V(a_h+b_h+c_h)
                    \leq1-uv+\frac12\sum_h c_h^2.
                    \tag{11.14}
\]

**Proof.** By symmetry assume \(u\geq v\), and put \(B=1-v\). For \(z=a_h+b_h\leq2-u-v\) and \(0\leq c\leq v\), the function \(V(z+c)-c^2/2\) is increasing in \(c\). Its derivative is \(z\) if \(z+c\leq1\), and \(2-z-2c\geq u-v\geq0\) otherwise. Thus it is at most

\[
 h(z)=V(z+v)-v^2/2
   =\begin{cases}vz+z^2/2,&0\leq z\leq B,\\
                  (1+B)z-z^2/2-B^2,&B\leq z\leq2B.
     \end{cases}
\]

On \([0,2B]\), \(h\) is increasing and is superadditive whenever the sum remains in that interval. To verify the latter directly, if \(x,y\leq B\) and \(x+y\leq B\), the difference is \(xy\geq0\). If \(x,y\leq B<x+y\), it is \(xy-(x+y-B)^2\geq0\): at fixed sum, \(xy\geq B(x+y-B)\), and \(x+y-B\leq B\). If \(y\geq B\), the difference is \(x(2B-x-y)\geq0\); both numbers cannot exceed \(B\) unless their sum reaches the endpoint. Consequently

\[
 \sum h(a_h+b_h)\leq h\!\left(\sum(a_h+b_h)\right)
       \leq h(2-u-v)
       =1-\frac{u^2+v^2}{2}\leq1-uv.
\]

The same calculation includes the endpoint \(B=0\) by continuity, or directly with every \(a_h,b_h\) zero. Adding back \(\sum c_h^2/2\) proves (11.14). \(\square\)

### Theorem 11.6. Dyson's lemma

Let \(P\ne0\) be a complex polynomial of degree at most \(r\) in \(X\) and at most \(s\) in \(Y\), with \(r,s>0\). Let \((x_h,y_h)\), \(1\leq h\leq M\), have pairwise distinct first coordinates and pairwise distinct second coordinates. If \(t_h\) is the index of \(P\) at that point with weights \((r,s)\), then

\[
 \sum_{h=1}^M V(t_h)
       \leq1+\max\{M/2-1,0\}\min\{s/r,r/s\}.
       \tag{11.15}
\]

**Proof.** Every index is at most two by the degree bounds. For \(M\leq1\), \(V(t_h)\leq1\) suffices. Assume \(M\geq2\), and factor \(P\) into its vertical factors, its horizontal factors and its remaining factor \(R\). Let the total axis degrees be \(A,B\). Put \(u=1-A/r\), \(v=1-B/s\). At the selected points let \(a_h,b_h\) be the indices contributed by the two axis products, and let \(c_h\) be the index of \(R\). The product rule gives \(t_h=a_h+b_h+c_h\). Coordinate distinctness implies \(\sum a_h\leq A/r=1-u\), \(\sum b_h\leq B/s=1-v\). The remainder has degrees at most \(ur,vs\), and no axis factors. Its restriction to either coordinate line through a point is nonzero, so some Taylor coefficient in that single coordinate survives by that degree. Therefore \(c_h\leq\min(u,v)\).

If \(R\) is constant, Lemma 11.5 already proves the conclusion. Otherwise write \(R=\prod F_j^{e_j}\), with distinct non-axis irreducible factors of bidegrees \((r_j,s_j)\), where \(r_j,s_j\geq1\). Let \(\tau_{hj}\) be their indices with the ambient weights \((r,s)\). Then \(c_h=\sum e_j\tau_{hj}\).

For each factor use the polynomial

\[
 G_j=(X-x_1)(X-x_2)\partial_XF_j-r_jX F_j.
\]

The leading power of \(X\) cancels, so \(G_j\) has bidegree at most \((r_j,s_j)\). It is coprime to \(F_j\): an irreducible non-axis factor divides neither \((X-x_1)(X-x_2)\) nor its own lower-degree derivative. At the first two points its index is at least \(\tau_{hj}\), because the vanishing factor in front of the derivative compensates its loss of \(1/r\). At all other points the index is at least \(\tau_{hj}-1/r\), when this is positive. Lemma 11.4 gives

\[
 rs\sum_h\tau_{hj}^2
       \leq2r_js_j+s\sum_{h=3}^M\tau_{hj}.
\]

For a negative \(\tau_{hj}-1/r\), the corresponding lower bound \(rs\tau_{hj}(\tau_{hj}-1/r)\) is negative and still valid. The global bound is \(2r_js_j\) by (11.13). For two distinct factors, the same local and global estimates give

\[
 rs\sum_h\tau_{hj}\tau_{hk}
                         \leq r_js_k+r_ks_j.
\]

Multiply the first inequalities by \(e_j^2\) and the mixed ones by \(2e_je_k\), then sum. Writing \(e=\max e_j\) and using the bidegrees of \(R\), we obtain

\[
 \begin{aligned}
 \frac12\sum_h c_h^2
 &\leq\frac{(\sum e_jr_j)(\sum e_js_j)}{rs}
             +\frac1{2r}\sum_{h=3}^M\sum_j e_j^2\tau_{hj}\\
 &\leq uv+\frac e{2r}\sum_{h=3}^M c_h
 \leq uv+\frac{(M-2)s}{2r}.
 \end{aligned}
\]

The final bound uses \(e\leq\sum e_js_j\leq s\) and \(c_h\leq1\). Lemma 11.5 now yields \(\sum V(t_h)\leq1+(M-2)s/(2r)\). Interchanging the two coordinates yields the same bound with \(r/s\), proving (11.15). \(\square\)

The coordinate distinctness is essential for the axis bookkeeping. The formula is valid for repeated irreducible factors and for indices above one; the change of formula in (11.11) is part of the conclusion. Unlike Roth's rational-point lemma, Dyson's lemma needs no arithmetic height hypothesis.

## 6. The role of the number of variables

Dyson's two-variable method was a predecessor of Roth's argument. A simple quantitative comparison already follows from the coefficient count in Lesson 10. For two variables whose degrees tend to infinity, the proportion of indices of weight at most \(t\), \(0\leq t\leq1\), tends to the area of the triangle

\[
                         \{(u,v)\in[0,1]^2:u+v\leq t\},
                         \qquad\text{area }t^2/2.
\]

The grid count converges to that area by partition into rectangular cells; boundary cells have total area tending to zero. Treating every vanishing condition over a degree-\(d\) field as \(d\) rational equations, the direct coefficient-counting guarantee requires \(dt^2/2<1\). If \(d_1\log q_1=d_2\log q_2=L\), rational evaluation costs denominator \(e^{2L}\), whereas approximation of exponent \(\mu\) gives an upper bound of order \(e^{-\mu tL}\). The comparison needs \(\mu t>2\). Thus this two-variable count asks for an exponent of order \(\sqrt d\). It explains the scale of Dyson's historical exponent \(\sqrt{2d}+\delta\), whose finiteness assertion follows from the stronger internal Roth theorem. It does not assert that a raw equation count is an obstruction to every possible two-variable refinement.

With many variables, the sum of the grid coordinates is concentrated near \(m/2\), and Theorem 10.7 gives index just below that value while preserving small height. The rational denominator cost has \(m\) factors, so an index near \(m/2\) is exactly what brings the exponent down towards two. Theorem 11.3 supplies the nonvanishing mechanism missing from a mere count of coefficients.

Later zero estimates retain the same distinction between many imposed conditions and control of all the resulting derivatives. The elliptic multiplicity construction in Lesson 9 instead controls intersections of algebraic varieties along a differential trajectory. No trajectory bound is used in Roth's lemma here.

The proof is ineffective in its application to irrational approximation because it starts by selecting sufficiently large members of a hypothetical infinite sequence of exceptional approximations. It proves that such an infinite sequence cannot exist; it does not produce the first exceptional denominator or bound the last one. The determinant constants above themselves are specified recursively, so their existence is not the source of that ineffectivity.

## 7. Exercises

1. **Easy — rational roots have a cost.** Prove the \(m=1\) case of Theorem 11.3 with \(C\ge1/\varepsilon\) and \(q>1\), without assuming \(|p/q|\le1\). Compute the determinant for \(1+X+X^2Y\) above and explain why its vanishing at \(X=0\) does not refute the Wronskian criterion.

2. **Medium — what derivatives can detect.** Prove the one-variable rational-function criterion, identify the role of characteristic zero, and exhibit its failure in characteristic \(p\). For \(1,X,Y\), explain why mixed derivative rows work while derivatives in just one fixed coordinate do not.

3. **Medium — transport a common factor.** Expand a generalized Wronskian of \(Qf_1,\ldots,Qf_k\), allowing rational functions, as a linear combination of Wronskians of the \(f_j\). Check the row-order restriction in every term. Why is this expansion a statement about polynomials or rational functions rather than about their nonzero values at every point?

4. **Hard — recover the exponent budget.** Prove the triangle-area limit in Section 6, derive the two-variable exponent scale \(\sqrt d\), and compare it with the many-variable index near \(m/2\). Explain where height control and Theorem 11.3 enter beyond the coefficient count.

## 8. Solutions

1. Write \(P=(qX-p)^\ell R\), where \(\ell\) is the root multiplicity. The quotient is integral by the primitive-product lemma. The leading coefficient of \(P\) is \(q^\ell\) times a nonzero integer, so \(q^\ell\leq H(P)\leq q^{d_1/C}\). Taking logarithms, \(\ell/d_1\leq1/C\leq\varepsilon\). This uses no assumption about the absolute size of \(p/q\). The determinant expands to \((1+X+X^2Y)2X-X^2(1+2XY)=X(X+2)\). The criterion asserts a determinant is not identically zero. It permits isolated zeros and even zeros along a hypersurface; controlling the index at a specified rational point is the separate arithmetic conclusion.

2. Dependence over constants makes every derivative column dependent. Conversely Lemma 11.1 applies, and the only independent sequence of derivative rows with orders at most \(\ell-1\) has successive orders \(0,\ldots,k-1\), as in Lemma 11.2. Characteristic zero ensures both that divided derivatives are defined and that a rational function killed by its derivative is constant. In characteristic \(p\), the functions \(1,X^p\) are independent but all positive derivatives of \(X^p\) vanish, so the criterion fails. In several variables the rows \((1,X,Y),(0,1,0),(0,0,1)\) have determinant one. Repeated \(X\)-derivatives never produce a nonzero entry in the \(Y\)-column below the first row; repeated \(Y\)-derivatives have the analogous problem in the \(X\)-column. Neither single-coordinate choice has rank three.

3. The divided product rule is \(D_{\boldsymbol i}(Qf)=\sum_{\boldsymbol h\leq\boldsymbol i}(D_{\boldsymbol i-\boldsymbol h}Q)(D_{\boldsymbol h}f)\). Substitute it in each determinant row and expand by multilinearity. Each summand is a product of derivatives of \(Q\) times a determinant with row orders \(|\boldsymbol h_\ell|\leq|\boldsymbol i_\ell|\leq\ell-1\), hence a permitted generalized Wronskian. Repeated derivative rows make that term zero but cause no difficulty. There are only finitely many terms. Evaluation may kill the coefficient functions or the resulting determinant, even when the identity is nonzero as a rational function. The example in the opening calculation makes this explicit; no claim of pointwise nonvanishing follows from multilinearity alone.

4. The grid rectangles have side lengths \(1/d_1,1/d_2\). Rectangles intersecting the line \(u+v=t\) lie in a strip whose width is at most \(1/d_1+1/d_2\), so its area tends to zero. Counting the other rectangles gives the area \(t^2/2\). For \(N\) coefficients, about \(dt^2N/2\) rational conditions are imposed, so the count alone guarantees a nonzero solution only below \(t\approx\sqrt{2/d}\). Matched denominator logarithms give cost \(2L\); vanishing of weight \(t\) and exponent \(\mu\) give gain \(\mu tL\). The sufficient comparison requires \(\mu>2/t\), of order \(\sqrt d\). For many variables the second-moment count gives an index near \(m/2\); matching logarithms costs \(mL\), and the corresponding ratio tends to two as the relative index loss tends to zero. Roth's lemma then turns this size comparison into a rigorous contradiction. The coefficient count guarantees a polynomial but does not control whether its derivatives vanish at the rational approximation point. Small height together with the separated degrees and denominator conditions supplies that control through Theorem 11.3. Theorem 12.1 then uses the rational nonzero-value lower bound on a derivative certified in this way.

## References

- Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*](https://arxiv.org/abs/2502.00731v2), arXiv:2502.00731v2, §2.5, Lemma 2.25, and §3.5, Lemma 3.9: the generalized Wronskian criterion and Roth's lemma. K. Soundararajan, [*Transcendental Number Theory*](https://math.stanford.edu/~ksound/TransNotes.pdf), Math 249A course notes, Stanford University, Fall 2010, written up by I. Petrow, §§17–18: generalized Wronskians and the induction in Roth's lemma.
- M. Waldschmidt, [*Diophantine approximation, irrationality and transcendence*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/IMPA2010Cours4.pdf), IMPA course notes, Course 4 (2010), §4.1.3, for the historical approximation exponents.

- Carlo Viola, [*On Dyson’s Lemma*](https://www.numdam.org/item/ASNSP_1985_4_12_1_105_0.pdf), Annali della Scuola Normale Superiore di Pisa, series 4, 12 (1985), 105–135: §I.3, printed pp. 106–107, for the exact Dyson–Bombieri inequality (11.15). The proof here uses a polar vanishing at the first two coordinates, weighted intersection lengths and an explicit axis-removal area calculation.
- The Stacks Project, the exact linked formal normalization proofs in section 5, under their GNU Free Documentation License.


- Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*, arXiv:2502.00731v2](https://arxiv.org/abs/2502.00731v2), §2.5, generalized Wronskians. The polynomial-curve calculation in Section 1 adapts the supplied TeX source under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); its substitution bound and derivative expansion are explained there.

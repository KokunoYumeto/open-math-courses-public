# E-functions and the Siegel–Shidlovsky theorem

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra setting, October 2026. Original exposition is CC0. No human or independent review is claimed. Prerequisites are identified where used.*

The exponential function and the Bessel function arise from quite different differential equations. Their Taylor coefficients nevertheless have a shared arithmetic property: after multiplication by a modest common denominator, their conjugates remain small compared with a factorial. Siegel's E-functions isolate this property. Shidlovsky's theorem then transfers algebraic independence of the functions to algebraic independence of their values at an ordinary, nonzero algebraic point.

We use the number-field Siegel lemma, Lemma 5.2 of Siegel's lemma and analytic estimates, and the integral-norm argument of Hermite and Lindemann. The number-field hypotheses and norm normalization are specified in those lessons. The coefficient constructions, the rank argument and the Bessel functional-independence argument are supplied below. In particular, a reference to a differential equation alone will not establish independence of its solutions.

## 1. The original definition of an E-function

Let \(K\) be a number field, with a chosen embedding into \(\mathbb C\). The house \(\overline a\) is the maximum of \(|\sigma(a)|\) over its embeddings. An **E-function in Siegel's original sense** is a series

\[
 E(z)=\sum_{n\ge0}a_n\frac{z^n}{n!},\qquad a_n\in K,
 \tag{14.1}
\]

with the following properties. For every \(\varepsilon>0\) there is a constant \(C_\varepsilon\) such that

\[
 \overline{a_n}\le C_\varepsilon n^{\varepsilon n},\qquad
 d_n\le C_\varepsilon n^{\varepsilon n},\qquad
 d_na_j\in\mathcal O_K\quad(0\le j\le n)
 \tag{14.2}
\]

for suitable positive integers \(d_n\). At \(n=0\) replace the right-hand power by one. The chosen denominator sequence may depend on the function; the inequalities must hold for every positive \(\varepsilon\). This definition is equivalent to bounding both \(d_n\) and the houses of \(d_na_0,\ldots,d_na_n\) by \(C_\varepsilon n^{\varepsilon n}\): use \(\varepsilon/2\) in the separate bounds. Later treatments often impose exponential bounds \(C^{n+1}\), and sometimes incorporate a differential-equation requirement in the definition. Here the growth condition is the original weaker one; a rational differential system will be an explicit hypothesis of the theorem.

The series is entire. For example, with \(\varepsilon=1/2\), the inequality \(n!\ge(n/e)^n\) makes its terms on a disk \(|z|\le R\) at most \(C(eR)^n n^{-n/2}\). The same conclusion holds for every conjugate coefficient sequence.

### Proposition 14.1. Examples and closure

Algebraic constant functions, \(e^{\beta z}\) for algebraic \(\beta\), and

\[
 J_0(z)=\sum_{k\ge0}\frac{(-1)^k(z/2)^{2k}}{(k!)^2}
 \tag{14.3}
\]

are E-functions. Sums, products, derivatives and primitives with algebraic integration constant are E-functions, after passing to a common number field.

**Proof.** Choose a positive integer \(D\) such that \(D\beta\) is integral. The exponential coefficients \(a_n=\beta^n\) have houses bounded by \(\max(1,\overline\beta)^n\); \(D^n\) clears all coefficients through index \(n\). Any fixed exponential bound is \(O(n^{\varepsilon n})\).

For (14.3), the coefficients in normalization (14.1) are

\[
 a_{2k}=(-1)^k\binom{2k}{k}4^{-k},\qquad a_{2k+1}=0.
 \tag{14.4}
\]

Their absolute values are at most one, and \(2^n\) clears those through index \(n\). The assertion for constants is immediate.

For a sum use the product of the two common denominators. For a product, its normalized coefficient is

\[
 c_n=\sum_{j=0}^n\binom nj a_jb_{n-j}.
 \tag{14.5}
\]

The integer \(d_ne_n\) clears all \(c_0,\ldots,c_n\), and the houses are bounded by \(2^n\max_{j\le n}\overline{a_j}\max_{j\le n}\overline{b_j}\). Apply the input estimates with, say, \(\varepsilon/4\), absorbing fixed constants and \(2^n\) into the remaining power. The coefficients for a derivative are \(a_{n+1}\), and those for a primitive are an algebraic initial constant followed by \(a_0,a_1,\ldots\). Bounds at \(n+1\) with a smaller positive exponent give (14.2) at \(n\). The corresponding denominator at \(n+1\), together with a fixed denominator for the constant, suffices. \(\square\)

The formal series \(\sum_{n\ge0}n!z^n\) has radius of convergence zero. It is consequently not an E-function; in normalization (14.1) its coefficients would be \((n!)^2\), which also violate (14.2).

## 2. Rational differential systems and the statement

Write functions as a column \(\mathbf E=(E_1,\ldots,E_n)^{\mathsf T}\). A homogeneous rational system means

\[
 \mathbf E'=A(z)\mathbf E,\qquad A(z)\in K(z)^{n\times n}.
 \tag{14.6}
\]

A point \(\alpha\) is **ordinary** if every entry of \(A\) is regular there. Choose a nonzero polynomial \(f\in\mathcal O_K[z]\) clearing its denominators, so \(fA\) has integral polynomial entries. At a specified ordinary point it can and will be chosen with \(f(\alpha)\ne0\): a common denominator in reduced form has zeros only at poles, and a constant integer clears its coefficient denominators.

Products of solutions of bounded total degree satisfy another such system. Indeed, for a multi-index \(\mathbf a\), the product rule gives

\[
 (\mathbf E^{\mathbf a})'
   =\sum_{i,j}a_i A_{ij}(z)
       \mathbf E^{\mathbf a-\mathbf e_i+\mathbf e_j},
 \tag{14.7}
\]

where terms with \(a_i=0\) are omitted. Include the constant monomial one. Thus all monomials of total degree at most \(s\) form a system whose poles are among those of \(A\).

We also need a constant-field observation. If finitely many power series have coefficients in \(K\), their linear independence over \(K(z)\) implies their independence over \(\mathbb C(z)\). A putative complex rational relation, after clearing denominators, uses finitely many unknown polynomial coefficients. Equating Taylor coefficients gives an infinite matrix over \(K\) with finitely many columns. Its rank is attained by finitely many rows and is unchanged on extending the field. A nonzero complex kernel therefore yields a nonzero \(K\)-kernel. Applying this argument to monomials gives the analogous implication for algebraic independence.

### Theorem 14.2. Siegel–Shidlovsky

Suppose the E-functions \(E_1,\ldots,E_n\) in the original sense satisfy (14.6) and are algebraically independent over \(K(z)\). If \(\alpha\ne0\) is algebraic and ordinary for (14.6), then

\[
                      E_1(\alpha),\ldots,E_n(\alpha)
                      \quad\text{are algebraically independent over }\overline{\mathbb Q}.
 \tag{14.8}
\]

Section 3 gives the determinant contradiction; Sections 4–6 prove the small-form and rank estimates it uses. The exclusion of zero is essential: the E-functions' values there are their algebraic constant coefficients. The ordinary-point condition ensures that derived coefficient rows can be evaluated without losing the rank information carried by the system.

The rank condition used in earlier proofs is often called **normality**. Its precise form needed here is that the first \(N\) derived coefficient rows of the auxiliary function in Section 4 have nonzero determinant. We impose no separate normality assumption: Section 5 proves this property for any fixed, linearly independent family satisfying a rational system. Applying it to the monomial systems (14.7) supplies the rank conditions at every degree required for algebraic independence. This is the extension that makes Shidlovsky's argument work beyond the low-order cases treated by Siegel.

**Check specialization on a familiar system.** The functions \(e^z,e^{\sqrt2 z}\) satisfy a diagonal constant system and are algebraically independent by Lemma 14.7. At zero they both have value one, so functional independence alone cannot preserve independence at every point. At any nonzero algebraic point Theorem 14.2 does apply. By contrast, \(e^z,e^{2z}\) satisfy an equally regular system but already have the functional relation \(E_2-E_1^2=0\). The differential equation and the arithmetic coefficient bounds are not substitutes for checking independence.

## 3. What a numerical relation would force

The input we need is Lemma 14.6: for every fixed independent family of \(k\) E-functions and every \(\delta>0\), an invertible integral coefficient matrix has houses at most \((r!)^{1+\delta}\) and its scalar products with the value vector at most \((r!)^{-k+1+\delta}\). Its proof comes in Sections 4–6. First use it to see why one relation, multiplied by many monomials, is impossible.

For one variable and a relation of degree \(c\), the numbers in (14.24) are simply \(l=m+1\) and \(k=m+c+1\). Increasing \(m\) leaves only \(c\) coefficient rows to pay for, while it supplies \(m+1\) exact zeros after the column operation. In several variables the same imbalance is expressed by \(k/l\to1\). This is why we amplify a putative relation before choosing the auxiliary functions.

Suppose there is a nonzero algebraic-coefficient relation

\[
                  R(E_1(\alpha),\ldots,E_n(\alpha))=0,
                  \qquad \deg R=c\ge1.
 \tag{14.23}
\]

Enlarge \(K\) to contain \(\alpha\) and the coefficients of \(R\), and clear their fixed denominators. This does not change the E-function growth bounds. Write \(d=[K:\mathbb Q]\).

For an integer \(m\), the polynomials \(X^{\mathbf a}R(X)\), \(|\mathbf a|\le m\), are linearly independent: multiplication by a nonzero polynomial is injective. Their number, and the number of all monomials of total degree at most \(m+c\), are respectively

\[
               l=\binom{m+n}{n},\qquad k=\binom{m+c+n}{n}.
 \tag{14.24}
\]

Since \(k/l\to1\), fix \(m\) so large that

\[
                              k-l<\frac{l}{2d}.
 \tag{14.25}
\]

List the \(k\) monomial functions as \(F_1=1,F_2,\ldots,F_k\). They are E-functions by Proposition 14.1, satisfy (14.7), and are linearly independent over \(K(z)\), by the assumed algebraic independence of the \(E_i\). They remain independent after the field enlargement: the Taylor-coefficient kernel argument in Section 2 applies to the original coefficient field. The point \(\alpha\) is still ordinary for their system.

Let \(p_1,\ldots,p_l\in\mathcal O_K^k\) be the coefficient rows of the relation multiples. They have rank \(l\), and each has zero scalar product with the value vector \(v=(F_1(\alpha),\ldots,F_k(\alpha))^{\mathsf T}\). Apply Lemma 14.6 to these \(k\) functions. From its invertible coefficient matrix choose \(k-l\) rows completing the \(p_i\) to a basis. Their combined determinant \(\mathcal D\) is a nonzero algebraic integer. Put

\[
                 H=(r!)^{1+\delta},\qquad
                 S=(r!)^{-k+1+\delta}.
\]

The relation rows are fixed, so every conjugate of \(\mathcal D\) has absolute value at most \(C H^{k-l}\). The nonzero integral norm yields

\[
                  |\mathcal D|\ge C' H^{-(d-1)(k-l)}.
 \tag{14.26}
\]

For the opposite bound, add \(v_i\) times column \(i\) to the first column, for \(i=2,\ldots,k\). Since \(v_1=1\), the first column becomes the scalar products of the rows with \(v\), while the determinant is unchanged. Its first \(l\) entries vanish. The other entries have absolute value at most \(S\). Expanding in this column, each nonzero cofactor contains only \(k-l-1\) large coefficient rows. Consequently

\[
                  |\mathcal D|\le C'' S H^{k-l-1}
                        =C''(r!)^{-l+\delta(k-l)}.
 \tag{14.27}
\]

Choose \(\delta>0\) so small that

\[
                  ((d-1)(1+\delta)+\delta)(k-l)<l;
\]

(14.25) permits this choice. The exponent in the upper bound (14.27) is then strictly smaller than that in the lower bound (14.26). Letting \(r\to\infty\) contradicts the two bounds. Thus (14.23) is impossible, proving Theorem 14.2. \(\square\)

The proof uses linear independence for the auxiliary monomial family, not an assumed algebraic independence of its values. The many relation multiples provide the \(l\) zero entries in the determinant; the near equality \(k\sim l\) keeps the arithmetic cost of the other rows smaller than that analytic gain.

## 4. Construct the small forms from Taylor coefficients

Fix \(N\) linearly independent E-functions \(F_1,\ldots,F_N\) satisfying a fixed system. Constants in the next three sections may depend on this family, its system and fixed positive parameters; they never depend on the integer \(r\).

**A complete two-row calculation.** Let \(F=(1,e^z)^{\mathsf T}\), with system matrix \(A=\operatorname{diag}(0,1)\) and denominator \(f=1\). Choose

\[
 P_0=(-2-2z-z^2,2),\qquad \Phi_0=P_0F=2(e^z-1-z-z^2/2).
\]

The function has order three at zero. Differentiating the row by the connection gives

\[
 P_1=P_0'+P_0A=(-2-2z,2),\qquad
 \det\begin{pmatrix}P_0\\P_1\end{pmatrix}=-2z^2.
\]

At zero the two coefficient rows lose rank; at \(z=1\) their determinant is \(-2\). The high-order zero of the function has left a visible vanishing reserve in the determinant. This example explains the need to move away from zero. It illustrates the construction and the derived rows, but does not claim the asymptotically near-maximal order in Lemma 14.3. To obtain that order with small coefficients, all the low Taylor coefficients must be imposed at once.

### Lemma 14.3. Arithmetic construction

For \(0<\varepsilon<1\) and \(\eta>0\), all sufficiently large \(r\) admit nonzero polynomials \(P_i\in\mathcal O_K[z]\), of degree at most \(r\), with coefficient houses at most \((r!)^{1+\eta}\), such that

\[
 \Phi(z)=\sum_{i=1}^N P_i(z)F_i(z)=\sum_{m\ge M}c_mz^m,
 \qquad M=N(r+1)-1-\lfloor\varepsilon r\rfloor,
 \tag{14.9}
\]

and \(|c_m|\le r!(m!)^{-1+\eta}\) for every \(m\ge M\). The function \(\Phi\) is nonzero.

**Proof.** Write \(F_i=\sum a_{i,m}z^m/m!\), and seek

\[
 P_i(z)=r!\sum_{j=0}^r p_{ij}\frac{z^j}{j!}.
 \tag{14.10}
\]

The first \(M\) zero conditions are

\[
 \sum_{i=1}^N\sum_{j=0}^{\min(r,m)}
          \binom mj a_{i,m-j}p_{ij}=0\qquad(0\le m<M).
 \tag{14.11}
\]

There are \(T=N(r+1)\) unknowns, and \(T-M>\varepsilon r\). For any small fixed \(\mu>0\), the product of the \(N\) common denominators through index \(M\) clears every equation. Its size and the houses of the resulting entries have logarithms at most

\[
                    C_N\mu M\log M+O_\mu(M).
 \tag{14.12}
\]

Here \(\binom mj\le2^m\), and (14.2) was used with a suitably smaller exponent. Lemma 5.2 gives a nonzero integral vector \(p_{ij}\), whose logarithmic house is at most

\[
 \frac{M}{T-M}\bigl(C_N\mu M\log M+O_\mu(M+\log T)\bigr)+O_K(1).
\]

Since \(M=O_N(r)\) and \(M/(T-M)=O_N(1/\varepsilon)\), choosing \(\mu\) sufficiently small makes this at most \(\eta_0\log(r!)\), for any prescribed \(\eta_0>0\) and large \(r\). Formula (14.10) has integral coefficients because \(r!/j!\) is integral.

For \(m\ge M\), its coefficient is \(c_m=(r!/m!)u_m\), where \(u_m\) is the left side of (14.11). Choose the coefficient-vector bound with \(\eta_0\) much smaller than \(\eta\), and use (14.2) with another sufficiently small exponent. Then

\[
 |u_m|\le T\,2^m (r!)^{\eta_0} C(m!)^{\eta_0}.
\]

Uniformly for \(m\ge M\), one has \(\log(r!)\le C_{N,\varepsilon}\log(m!)\), while \(m+\log T=o(\log(m!))\). Taking \(\eta_0<\eta/(2C_{N,\varepsilon}+4)\), and then increasing \(r\), gives \(|u_m|\le(m!)^\eta\). The same small coefficient-vector bound gives the asserted polynomial houses. Finally, linear independence over \(K(z)\) prevents a nonzero polynomial vector from making \(\Phi\) identically zero. \(\square\)

## 5. Recover rank before and after evaluation

For a polynomial row \(P_0=(P_1,\ldots,P_N)\), define

\[
 P_{j+1}=f(P_j'+P_j A),\qquad \Phi_j=P_j\mathbf F.
 \tag{14.13}
\]

Thus \(\Phi_0=\Phi\), \(\Phi_{j+1}=f\Phi_j'\), and \(\deg P_j\le r+Cj\) for a fixed \(C\). All coefficients remain integral.

We first make explicit a finite-dimensional fact about rational functions. If \(V\) is a fixed finite-dimensional complex vector space of meromorphic functions, the rational functions \(u/v\) with \(u,v\in V\), \(v\ne0\), have bounded numerator and denominator degrees. To prove this, choose a basis \(b_1,\ldots,b_t\) of the \(\mathbb C(z)\)-span of \(V\). A fixed complex basis \(v_i\) of \(V\) has expressions \(v_i=\sum_j a_{ij}(z)b_j\) with fixed rational functions \(a_{ij}\). If \(u=qv\) with rational \(q\), comparison in this basis gives \(q=u_j/v_j\) for an index with \(v_j\ne0\). Each \(u_j,v_j\) is a constant linear combination of the fixed \(a_{ij}\). A common denominator bounds their polynomial degrees uniformly and proves the assertion, including any cancellations.

### Lemma 14.4. Shidlovsky's rank lemma

For the auxiliary vector of Lemma 14.3, with \(0<\varepsilon<1\), the determinant

\[
             \Delta(z)=\det\begin{pmatrix}P_0(z)\\ \vdots\\P_{N-1}(z)\end{pmatrix}
             \tag{14.14}
\]

is nonzero for all sufficiently large \(r\).

**Proof.** Suppose the first dependent row is \(P_k\), where \(k<N\). The preceding \(k\) rows are independent, and their rational row span is stable under the connection \(P\mapsto P'+PA\): differentiating any rational linear combination and using (14.13) shows that every later row remains in the span.

Transpose these \(k\) rows to a matrix \(Q\) of size \(N\times k\), and permute the functions so that its top \(k\times k\) block \(R\) is invertible. Write the lower block as \(S\). We claim that all entries of \(SR^{-1}\) have rational numerator and denominator degrees bounded solely in terms of the fixed system.

To see this, take a fixed analytic fundamental matrix \(W\), with rows solving the transposed system, on a disk about an ordinary point. For completeness, the local solution matrix is obtained by successive substitution in its integral equation, starting from the identity initial value. If the coefficient matrix is bounded by \(B\) on a disk of radius \(\rho\), the \(j\)-fold integral term is bounded by \((B\rho)^j/j!\); the series converges uniformly on smaller disks and can be differentiated there. The same estimate applied to a zero initial value proves uniqueness. Its determinant satisfies \((\det W)'=(\operatorname{tr}A)\det W\), by the product rule for determinants, so it stays invertible. The row-span stability just established means that every row of \(WQ\) solves a common \(k\)-dimensional system \(Y'=YB_1\), with rational \(B_1\). On a smaller disk avoiding its poles, the same existence and uniqueness argument makes its solution space \(k\)-dimensional over constants. Hence a constant matrix \(L\) of size \((N-k)\times N\) and rank \(N-k\) satisfies \(LWQ=0\).

Write \(LW=(U,V)\) in the same column blocks. Then \(UR+VS=0\). Since \(LW\) has rank \(N-k\) and its kernel is the column space of \(Q\), this kernel is the graph \(x\mapsto SR^{-1}x\). It follows that \(V\) is invertible and

\[
                            SR^{-1}=-V^{-1}U.
 \tag{14.15}
\]

Each entry on the right is a quotient of constant linear combinations of finitely many monomials of degree at most \(N-k\) in the entries of the fixed \(W\). These monomials span a fixed finite-dimensional space. The entries on the left are rational. The finite-dimensional fact preceding the lemma therefore gives the claimed uniform degree bound. Allowing complex constants in \(L\) causes no difficulty; the rational degree bound and the ensuing order bound are over \(\mathbb C\).

Now let \(\mathcal L=(\Phi_0,\ldots,\Phi_{k-1})\). With \(\mathbf F^{\mathsf T}=(a,b)\) in matching blocks,

\[
                   \mathcal L R^{-1}=a+bSR^{-1}.
 \tag{14.16}
\]

Every component on the left has order at zero at least \(M-kr-C'\): the \(\Phi_j\) have order at least \(M-j\), and \(\det R\) has degree at most \(kr+C'\). On the right every component is nonzero, by independence of the \(F_i\) over \(\mathbb C(z)\). Clear its uniformly bounded-degree rational denominators. The resulting function belongs to a fixed space spanned by finitely many \(z^aF_i\), with \(a\) uniformly bounded. In any finite-dimensional space of analytic functions, the orders of nonzero functions at zero are bounded: otherwise the descending kernels of the successive Taylor-coefficient maps would stabilize at a nonzero vector with all coefficients zero. Thus the right side has a uniform upper bound on its order. But

\[
              M-kr=(N-k-\varepsilon)r+O_N(1)\longrightarrow\infty.
\]

This contradiction proves the lemma. \(\square\)

### Lemma 14.5. Rank at an ordinary nonzero point

For a fixed ordinary \(\alpha\ne0\), the rows \(P_j(\alpha)\) with

\[
                         0\le j\le\varepsilon r+C
 \tag{14.17}
\]

span \(K(\alpha)^N\), where \(C\) is independent of \(r\).

**Proof.** The determinant in (14.14) has degree at most \(Nr+C_1\). Replace column \(i\) by the column \((\Phi_0,\ldots,\Phi_{N-1})^{\mathsf T}\). Multilinearity makes the replaced determinant equal to \(F_i\Delta\). Expand along this column and choose any fixed \(F_i\) not identically zero. Since its entries have orders at least \(M-j\), this gives

\[
 \operatorname{ord}_0\Delta\ge M-C_2.
\]

Here we subtract only the fixed order of \(F_i\) at zero and the indices \(j<N\). Since \(\alpha\ne0\), the order \(T\) of \(\Delta\) at \(\alpha\) is at most

\[
             Nr+C_1-(M-C_2)\le\varepsilon r+C_3.
\]

Use a local fundamental matrix \(W\) at \(\alpha\), now in column convention, so \(W'=AW\). The rows \(P_jW\) satisfy \((P_jW)'=f^{-1}P_{j+1}W\). Differentiate their first \(N\)-row determinant \(T\) times. By the product rule every resulting determinant uses row indices at most \(N-1+T\); derivatives of \(f^{-1}\) introduce only regular scalar factors. If the evaluated rows through that index had rank less than \(N\), all these determinants would vanish at \(\alpha\). But the determinant is \(\Delta\det W\), of exact zero order \(T\), and its \(T\)-th derivative there is nonzero. This proves full rank and (14.17). \(\square\)

## 6. Balance the factorial gain and arithmetic cost

There are two bounds to prove for the same coefficient rows. Their houses must grow no faster than \((r!)^{1+\delta}\), while their values against \(F(\alpha)\) must decay like \((r!)^{-N+1+\delta}\). The rank argument only selects independent rows; it does not supply either size bound. Conversely the auxiliary zero only supplies small values; it does not make the matrix invertible. The following estimate joins these two pieces with the same free loss \(\delta\).

### Lemma 14.6. The factorial estimates

Let \(F_1,\ldots,F_N\) be linearly independent E-functions satisfying a rational system, and let \(\alpha\ne0\) be algebraic and ordinary. Enlarge \(K\) to contain \(\alpha\). For every \(\delta>0\) and all sufficiently large integers \(r\), there are \(N\) rows \(q_j\in\mathcal O_K^N\), forming an invertible matrix, such that

\[
 \max_{i,j}\overline{q_{j,i}}\le(r!)^{1+\delta},\qquad
 \left|\sum_iq_{j,i}F_i(\alpha)\right|
                              \le(r!)^{-N+1+\delta}.
 \tag{14.18}
\]

**Proof.** We give the estimates that permit an arbitrarily small loss \(\delta\). Apply Lemma 14.3 with positive \(\varepsilon,\eta\) to be chosen. Lemma 14.5 selects independent rows among indices \(j\le J=\lfloor\varepsilon r\rfloor+C\).

For a polynomial row, use the maximum house of its coefficients. The recurrence (14.13), with its fixed polynomial multipliers, gives

\[
 \|P_j\|\le(r!)^{1+\eta}
                   \bigl(C_1(r+C_2J+1)\bigr)^j,
 \qquad\deg P_j\le r+C_2j.
 \tag{14.19}
\]

Indeed, differentiation costs at most the current degree, and multiplication by a fixed polynomial costs a fixed sum of coefficient houses. Thus

\[
 \log\|P_j\|\le(1+\eta+C_3\varepsilon+o(1))\log(r!)
 \quad(j\le J).
 \tag{14.20}
\]

If \(D\alpha\) is integral, multiply every selected row \(P_j(\alpha)\) by \(D^{r+C_2J}\). They become integral; evaluation under each embedding and this multiplier cost only \(\exp(O(r+J))\). They therefore have the first bound in (14.18) once \(\eta,\varepsilon\) are small enough.

For the values, expand the operator \((f\,d/dz)^j\). The product rule shows that its coefficients, evaluated at the fixed \(\alpha\), have sum of absolute values at most \(\exp(C_4J\log(J+2))\) for \(j\le J\). One direct induction obtains this bound: at a new step differentiate each coefficient polynomial and multiply by fixed \(f\); its degree is \(O(j)\), so the sum grows by at most \(C(j+1)\). A weaker bound with \((C(j+1)^2)^j\) also suffices.

Let \(R=\max(1,|\alpha|)\). For \(s\le J\), (14.9) gives

\[
 |\Phi^{(s)}(\alpha)|
     \le r!\sum_{m\ge M}(m!)^{-1+\eta}m^J R^m
     \le 2r!(M!)^{-1+\eta}M^J R^M
 \tag{14.21}
\]

for large \(r\). To verify the last inequality, the ratio of consecutive majorants is

\[
 R(m+1)^{-1+\eta}(1+1/m)^J\le\tfrac12
 \quad(m\ge M)
\]

eventually, provided \(\eta<1\); \(J/M\) is bounded and \(M\) grows linearly with \(r\). The displayed derivative bound also covers \(\alpha=0\), though that point is not used in the rank lemma. After the operator bound and the denominator multiplier, we have

\[
 \log|D^{r+C_2J}\Phi_j(\alpha)|
 \le\log(r!)-(1-\eta)\log(M!)+J\log M
                       +O(J\log(J+2)+M+r).
 \tag{14.22}
\]

Since \(M=(N-\varepsilon)r+O(1)\), division by \(\log(r!)\) gives an upper bound

\[
                         -N+1+N\eta+C_5\varepsilon+o(1).
\]

Choose \(\eta,\varepsilon>0\) with \(\eta+C_3\varepsilon<\delta/2\) and \(N\eta+C_5\varepsilon<\delta/2\), and then increase \(r\). This proves both estimates. The selected rows are independent, and their common nonzero multiplier preserves independence. \(\square\)

## 7. Exponentials and a second proof of Lindemann–Weierstrass

### Lemma 14.7. Independence of distinct exponential functions

For distinct complex \(\lambda_1,\ldots,\lambda_s\), the functions \(e^{\lambda_j z}\) are linearly independent over \(\mathbb C(z)\).

**Proof.** Choose a relation with the smallest number of nonzero rational coefficients, and divide by its first coefficient to make that coefficient one. Differentiate the relation and subtract \(\lambda_1\) times the relation. The first term disappears. Minimality forces every remaining coefficient \(q_j\) to satisfy

\[
                         q_j'+(\lambda_j-\lambda_1)q_j=0.
\]

A nonzero rational function has \(q_j'/q_j=O(1/z)\) at infinity, whereas this equation requires that logarithmic derivative to be the nonzero constant \(\lambda_1-\lambda_j\). This is impossible. A relation with a single nonzero term was already impossible. \(\square\)

If algebraic \(\beta_1,\ldots,\beta_s\) are linearly independent over \(\mathbb Q\), distinct monomials in \(e^{\beta_1z},\ldots,e^{\beta_sz}\) have distinct exponents \(\sum a_i\beta_i\). Lemma 14.7 proves their algebraic independence over \(\mathbb C(z)\). Their diagonal system has constant entries \(\beta_i\), so every nonzero point is ordinary. Theorem 14.2 therefore proves that

\[
                e^{\alpha\beta_1},\ldots,e^{\alpha\beta_s}
                \quad\text{are algebraically independent}
 \tag{14.28}
\]

for every nonzero algebraic \(\alpha\).

### Corollary 14.8. Lindemann–Weierstrass

For distinct algebraic \(\gamma_1,\ldots,\gamma_t\), the numbers \(e^{\gamma_j}\) are linearly independent over \(\overline{\mathbb Q}\).

**Proof.** Choose a \(\mathbb Q\)-basis of the span of the \(\gamma_j\), and divide its elements by a common integer so that each \(\gamma_j\) is an integer combination of the resulting basis \(\beta_1,\ldots,\beta_s\). If the span is zero there is only the single exponent zero, and the assertion is immediate. Otherwise (14.28) at \(\alpha=1\) makes the \(e^{\beta_i}\) algebraically independent. The \(e^{\gamma_j}\) are distinct Laurent monomials in them. Any algebraic-coefficient linear relation among these Laurent monomials becomes a nonzero polynomial relation after multiplication by a sufficiently large monomial, a contradiction. \(\square\)

For instance \(e\) and \(e^{\sqrt2}\) are algebraically independent. The algebraicity of the evaluation point is part of the argument; the theorem does not apply by replacing it with \(\pi\).

## 8. The Bessel example: independence before specialization

Termwise differentiation of the entire series (14.3) gives

\[
                 zJ_0''+J_0'+zJ_0=0,
 \qquad
 \begin{pmatrix}J_0\\J_0'\end{pmatrix}'
   =\begin{pmatrix}0&1\\-1&-1/z\end{pmatrix}
                   \begin{pmatrix}J_0\\J_0'\end{pmatrix}.
 \tag{14.29}
\]

For example, the coefficient of \(z^{2k+1}\) in the scalar equation is
\(4(k+1)^2 b_{k+1}+b_k=0\), where \(b_k=(-1)^k/(4^k(k!)^2)\). The only pole of the displayed system is zero. Both functions are E-functions by Proposition 14.1. We now prove the separate functional-independence input.

We will use a local fact about algebraic functions, with its analytic justification. A branch of a function algebraic over \(\mathbb C(z)\), near any fixed point \(a\), has a convergent Laurent expansion in \((z-a)^{1/m}\) for some positive integer \(m\), with only finitely many negative powers. Indeed, its squarefree polynomial equation has nonzero discriminant. On a sufficiently small punctured disk about \(a\), its roots continue analytically, by the implicit function theorem, and continuation around the puncture permutes finitely many roots. The substitution \(z-a=t^m\), with \(m\) a multiple of the permutation's order, makes each branch single-valued on a punctured \(t\)-disk. The elementary root bound

\[
 |w|\le1+\max_{j<d}|b_j(z)/b_d(z)|
 \quad\text{for }\sum_{j=0}^d b_j(z)w^j=0
\]

bounds this branch by \(C|t|^{-B}\). Multiplication by a sufficiently large power of \(t\) gives a bounded holomorphic function, which extends over zero by its Cauchy integral formula. Its Laurent expansion is the asserted convergent expansion. This argument supplies the local expansions used below without requiring a classification of algebraic curves.

### Lemma 14.9. A Riccati obstruction

The equation

\[
                            r'+r^2+r/z+1=0
 \tag{14.30}
\]

has no solution algebraic over \(\mathbb C(z)\).

**Proof.** Suppose \(r\) is algebraic. The derivation on \(\mathbb C(z)\) extends uniquely to its finite algebraic extensions: differentiating a separable minimal polynomial gives \(r'=-P_z(z,r)/P_T(z,r)\). Hence every conjugate branch of \(r\) also satisfies (14.30).

At zero, consider a branch with leading term \(az^t\), where \(t\) is rational and \(a\ne0\). A negative exponent is impossible. If \(t<-1\), the term \(r^2\) alone has the smallest exponent. If \(-1<t<0\), the smallest term is \((r'+r/z)\sim(t+1)az^{t-1}\). At \(t=-1\), the leading terms in \(r'+r/z\) cancel, but \(a^2z^{-2}\) from \(r^2\) cannot cancel with any remaining term. Each case contradicts the equation. Thus every branch is bounded at zero. Its constant term must be zero, since otherwise \(r/z\) has an uncancelled \(z^{-1}\) term.

If two such branches \(r_1,r_2\) differed, their difference would have a leading Puiseux term \(az^t\) with \(t>0\). Subtract their equations:

\[
                   (r_1-r_2)'+(r_1+r_2+1/z)(r_1-r_2)=0.
\]

Since \(r_1,r_2\to0\), the leading coefficient on the left is \((t+1)a\) at exponent \(t-1\), and it is nonzero. Therefore all conjugate branches coincide. Separability forces the minimal polynomial to have degree one: \(r\) is rational.

At a finite pole \(a\ne0\) of a rational solution, dominant terms in (14.30) force a simple pole with residue one: if \(r\sim c/(z-a)\), then \(c^2-c=0\). There is no pole at zero, as already proved. At infinity the polynomial part cannot have positive degree, since its square would dominate every other term. Nor can \(r\) tend to zero, because of the constant one in (14.30). Thus

\[
                        r=c+b/z+O(z^{-2}),\qquad c^2=-1.
\]

Comparing the \(z^{-1}\) terms gives \(2cb+c=0\), hence \(b=-1/2\). But a rational function with constant polynomial part and only simple finite poles of residue one has \(b\) equal to the number of those poles, a nonnegative integer. This contradiction proves the lemma. \(\square\)

### Proposition 14.10. Algebraic independence of the Bessel functions

The functions \(J_0\) and \(J_0'\) are algebraically independent over \(\mathbb C(z)\).

**Proof.** First, \(J_0\) is transcendental over \(\mathbb C(z)\). Any entire algebraic function is a polynomial: a polynomial equation and the same root bound used above give \(|y(z)|\le C(1+|z|)^B\) outside a disk, and Cauchy's derivative estimates make its Taylor coefficients of degree greater than \(B\) vanish. The series (14.3) has infinitely many nonzero coefficients, so it is not a polynomial.

Put \(U=J_0,V=J_0'\), and suppose they satisfy a polynomial relation over \(\mathbb C(z)\). Choose an irreducible relation \(P(z,U,V)\). Because \(U\) is transcendental, the kernel of evaluation in \(\mathbb C(z)[U,V]\) is generated by \(P\). Explicitly, over the field \(\mathbb C(z,U)\) this is the minimal-polynomial divisibility statement for \(V\); clearing primitive polynomial contents gives divisibility in \(\mathbb C(z)[U,V]\). The latter step is Gauss's lemma over the Euclidean ring \(\mathbb C(z)[U]\): reduction modulo each irreducible factor shows that a product of primitive polynomials is primitive, so denominators cannot remain in the quotient.

On this polynomial ring define

\[
 \mathcal D=\frac{\partial}{\partial z}
                  +V\frac{\partial}{\partial U}
                  -(U+V/z)\frac{\partial}{\partial V}.
 \tag{14.31}
\]

Equation (14.29) makes evaluation commute with differentiation. Thus \(\mathcal DP\) belongs to the same kernel, so \(\mathcal DP=QP\). The derivation preserves total degree in \(U,V\); consequently \(Q\in\mathbb C(z)\), including the possibility \(Q=0\).

Take a nonzero homogeneous part \(P_h\) of positive degree. It satisfies \(\mathcal DP_h=QP_h\). Over an algebraic extension of \(\mathbb C(z)\), factor this binary homogeneous polynomial into linear factors. Every such factor \(g\) satisfies \(g\mid\mathcal Dg\). To check multiplicities, write \(P_h=g^eG\), with \(g\nmid G\), and divide \(\mathcal DP_h\) by \(g^{e-1}\); reduction modulo \(g\) gives \(e(\mathcal Dg)G=0\), so divisibility follows in characteristic zero.

A factor \(g=U\) is impossible because \(\mathcal DU=V\). Any other factor can be scaled to \(g=V-r(z)U\), with algebraic \(r\). Direct calculation gives

\[
 \mathcal D(V-rU)=-(r+1/z)(V-rU)
                           -(r'+r^2+r/z+1)U.
 \tag{14.32}
\]

Divisibility by \(V-rU\) forces (14.30), contradicting Lemma 14.9. Hence no original relation exists. \(\square\)

### Corollary 14.11. Bessel values

For every nonzero algebraic \(\alpha\), the numbers \(J_0(\alpha)\) and \(J_0'(\alpha)\) are algebraically independent over \(\overline{\mathbb Q}\).

**Proof.** The functions are E-functions, Proposition 14.10 supplies their functional independence, and (14.29) is ordinary at every \(\alpha\ne0\). Theorem 14.2 applies. \(\square\)

In particular each value is transcendental and neither is zero. Their quotient is transcendental as well: an algebraic quotient would give an algebraic-coefficient linear relation between the two values.

## Exercises

1. **Easy — test the hypotheses.** Verify the original E-function conditions for \(e^{\beta z}\) with arbitrary algebraic \(\beta\), including a denominator clearing every coefficient through \(n\). Compare \((e^z,e^{\sqrt2z})\) at zero and at a nonzero algebraic point with \((e^z,e^{2z})\). State exactly which hypothesis fails in each excluded case.

2. **Medium — products and the Bessel system.** Derive (14.5) and check the product house and common-denominator bounds. Then derive (14.29) directly from the Bessel series and identify its ordinary points. Explain why entire solutions may still have a rational system with a pole.

3. **Medium — follow the derived rows.** Verify \(P_0,P_1,\Phi_0\) and their determinant in the two-row calculation. Calculate \(P_2\), and find the rank of the first three rows at zero. Explain how this models the extra rows in Lemma 14.5. For one function variable and a putative relation of degree \(c\), compute \(k-l\) in (14.24) and choose \(m\) satisfying (14.25).

4. **Hard — specialize only after independence.** Prove functional algebraic independence of exponentials with \(\mathbb Q\)-independent algebraic exponents, starting from rational-function linear independence. Deduce the full Lindemann–Weierstrass linear-independence statement for distinct algebraic exponents, handling the constant monomial and negative powers.

## Solutions

1. The normalized coefficient is \(a_n=\beta^n\). Choose \(D\in\mathbb Z_{>0}\) with \(D\beta\in\mathcal O_K\). For \(j\le n\), \(D^n\beta^j=D^{n-j}(D\beta)^j\) is integral, so \(d_n=D^n\) is a simultaneous denominator. Houses are at most \(\max(1,\overline\beta)^n\). For every \(\varepsilon>0\), \(C^n\le n^{\varepsilon n}\) for all sufficiently large \(n\), and a fixed constant covers the remaining indices. This includes \(\beta=0\). The exponents \(1,\sqrt2\) are rationally independent, so Lemma 14.7 gives functional algebraic independence; their constant diagonal system is ordinary everywhere. At zero the nonzero-point hypothesis fails and both values are one. At a nonzero algebraic point every hypothesis holds. The pair with exponents \(1,2\) instead fails functional algebraic independence through \(E_2=E_1^2\), regardless of the evaluation point.

2. Multiply the two exponential-normalized series. The coefficient of \(z^n/n!\) is \(\sum_{j=0}^n\binom nj a_jb_{n-j}\). Since \(d_n\) and \(e_n\) clear all input coefficients through \(n\), their product clears every output coefficient through \(n\), not merely \(c_n\). For houses, use \(j^{\eta j}\le n^{\eta n}\), the input estimates at exponent \(\eta=\varepsilon/4\), and \(\sum_j\binom nj=2^n\). Then \(\overline{c_n}\le C2^n n^{\varepsilon n/2}=O(n^{\varepsilon n})\). The denominator product has the same required bound. Merely choosing a denominator for each isolated \(c_n\) would not establish the simultaneous-denominator clause in (14.2).

   With \(J_0=\sum b_kz^{2k}\), the coefficient of \(z^{2k+1}\) in \(zJ_0''+J_0'+zJ_0\) is \(4(k+1)^2b_{k+1}+b_k\), which vanishes for \(b_k=(-1)^k/(4^k(k!)^2)\). All other coefficients vanish by parity. Set \(y_1=J_0,y_2=J_0'\); then \(y_1'=y_2\) and \(y_2'=-y_1-y_2/z\). The functions themselves are entire, with \(J_0(0)=1,J_0'(0)=0\), while this rational matrix has a pole at zero. Its ordinary points are exactly \(\mathbb C\setminus\{0\}\); the theorem concerns their nonzero algebraic subset. The pole belongs to the chosen system coefficients, not to the entire solutions. Cancellation in a particular solution does not make the coefficient matrix ordinary; one must check the matrix itself when applying the theorem.

3. Direct multiplication gives \(\Phi_0=2e^z-2-2z-z^2\); its Taylor expansion begins \(z^3/3\), so its order is three. The derived rows are \(P_1=(-2-2z,2)\) and \(P_2=(-2,2)\). At zero both first rows equal \((-2,2)\), and so does the third: their rank is one. One more derivative gives \(P_3=(0,2)\), raising the rank to two. Thus generic rank does not prescribe how many rows suffice at a point; additional derivatives can recover it. Lemma 14.5 bounds their number by the vanishing reserve of the determinant. In one variable \(l=m+1\), \(k=m+c+1\), and \(k-l=c\); (14.25) becomes \(m+1>2dc\), achievable by taking \(m\ge2dc\). This keeps the field degree in the arithmetic estimate, rather than replacing it by the function count.

4. A polynomial relation among \(e^{\beta_i z}\) is a linear relation among exponentials with exponents \(\sum a_i\beta_i\). These are distinct when the \(\beta_i\) are \(\mathbb Q\)-independent. For a shortest rational-function linear relation, normalize one coefficient to one and apply \(d/dz-\lambda_1\). This gives a shorter relation unless every remaining rational coefficient satisfies \(q'/q=\lambda_1-\lambda_j\). The latter cannot hold because a rational logarithmic derivative tends to zero at infinity. Functional algebraic independence follows. The diagonal constant system and Theorem 14.2 at \(\alpha=1\) give algebraic independence of their values. Choose a rational basis for the span of the distinct \(\gamma_j\), rescaling it to make their coordinates integral. The target exponentials are distinct Laurent monomials in the independent values. Clearing their negative powers turns a putative algebraic-coefficient linear relation into a nonzero polynomial relation. If that span is zero, there is only one exponent and the assertion is immediate.

## Sources and attribution

- Frits Beukers, [*A refined version of the Siegel–Shidlovskii theorem*](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n1-p08.pdf), *Annals of Mathematics* 163 (2006), 369–379, §1: E-functions, Siegel's original definition and the Siegel–Shidlovskii theorem. Boris Adamczewski and Colin Faverjon, [*Algebraic independence measures for values of E-functions and M-functions*](https://arxiv.org/abs/2502.09999v1), arXiv:2502.09999v1, 2025, §3.2: the classical method of Siegel and Shidlovskii, with linear forms obtained from multiples of the functional relations, Siegel's auxiliary forms and Shidlovskii's lemma on the rank of the derived forms.
- Stéphane Fischler, [“Shidlovsky’s multiplicity estimate and Irrationality of zeta values”](https://arxiv.org/abs/1609.09770v1), 2016: Theorems 1–2, proved in Sections 3.1–3.2, treat derived-row rank for rational differential systems and its recovery at a point. The rank mechanism is independent of E-function coefficient growth. Sections 4–6 above supply the arithmetic estimates for Siegel’s original definition.
- Siegel's 1929 E-function work and Shidlovsky's extension, announced in 1954 and published in 1959, are described in Beukers's paper above, §1, and in Michel Waldschmidt, [*Auxiliary functions in transcendence proofs*](https://arxiv.org/abs/0908.4024), arXiv:0908.4024, 2009, §3.1.1.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 4: Transcendence results](https://pub.math.leidenuniv.nl/~evertsejh/dio19-4.pdf), Leiden course notes, Exercise 4.7: the polynomial version of the Lindemann–Weierstrass theorem for real exponential polynomials, a functional independence statement of the kind proved in Lemma 14.7.
- The first course proof of Lindemann–Weierstrass is in Hermite and Lindemann; its exact earlier arithmetic prerequisites and the number-field Siegel lemma in Siegel's lemma and analytic estimates are the inputs used here.

The next lesson distinguishes consequences proved by these methods from implications that remain conditional on Schanuel's conjecture.

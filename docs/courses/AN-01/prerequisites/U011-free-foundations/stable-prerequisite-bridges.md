# Complex scalars and finite algebra — selected programme proofs

These are selected foundation sections from **Polynomial and contour interfaces for stable boundary models**, programme lesson AN03-P002. They retain the section and equation numbers of that earlier lesson. The selection and introductory note were prepared by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026.

The original course-writing task and OpenAI Codex credits, dedication and history are retained in [the original title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md). This independently written programme selection carries **CC0 1.0 Universal**, to the extent rights are held. The [CC0 dedication](https://creativecommons.org/publicdomain/zero/1.0/) identifies the terms.

The original notice files describe the original course edition. [Selection history](SELECTION_HISTORY.md) describes these excerpts.

The mathematical entry is natural-number arithmetic with induction, ordinary set theory and countable choice. The real-field construction is in [the scalar foundations](metric-foundation-bridges.md#12-real-numbers-and-finite-dimensional-topology); complex arithmetic and finite algebra are in [the algebra foundations](stable-prerequisite-bridges.md#10-full-finite-linear-algebra-foundations); integration is in [the measure foundations](banach-foundation-bridges.md#15-0-constructing-the-measure-without-importing-a-convergence-theorem).

This selection supplies: Complex arithmetic, bases, matrices, determinants, elimination, Gram comparisons and finite-dimensional norm bounds.

## 10. Full finite linear-algebra foundations

Here are the finite algebra proofs used by the preceding spectral and polynomial arguments. It works over the original field \(F=\mathbb R\) or \(F=\mathbb C\). Conjugation is the identity in the real case. The scalar entry is the real field with completeness, the complex field formed from it, finite induction and finite sums/products. No spectral decomposition, root theorem, basis-extension theorem, rank-nullity theorem or inner-product representation theorem is assumed below. The complex-root theorem already proved in Polynomial and contour interfaces for stable boundary models is used only when root existence is separately requested in Section 10.10. These are standard foundational results; no novelty is claimed.

All vectors, coefficient matrices, pivots, signs and inner products in a calculation keep their original values. A new basis gives an explicit coordinate comparison, with both directions and every metric factor retained. In particular, the original Gram residuals and their lengths stay in the calculation when a separately constructed orthonormal comparison basis is given.

### 10.1. Finite spanning sets, exchange and basis extension

The scalar arithmetic used here is explicit. Real arithmetic is the given ordered-field arithmetic. For complex numbers keep their original pairs and define
\[
\begin{gathered}
(a,b)+(c,d)=(a+c,b+d), \\ 
(a,b)(c,d)=(ac-bd,ad+bc), \\ 1=(1,0),\quad 0=(0,0),\quad i=(0,1).
\end{gathered}
\tag{FA0a}
\]
Addition is an abelian group coordinatewise. Multiplication is commutative by the real commutative field laws. Expanding either association of three factors gives the same full pair
\[
((a,b)(c,d))(e,f)=(a,b)((c,d)(e,f))
=(ace-adf-bcf-bde,acf+ade+bce-bdf).
\tag{FA0b}
\]
All four summands in each coordinate are retained; distributivity follows by the same two-coordinate expansion. The displayed zero and one are the additive and multiplicative identities, and the additive inverse is the pair of the two original negatives. For a nonzero pair, the original real number \(a^2+b^2\) is positive. Direct multiplication in either order proves
\[
\begin{gathered}
(a,b)^{-1}=\left(\frac{a}{a^2+b^2},-\frac{b}{a^2+b^2}\right), \\  (a,b)(a,b)^{-1}=(a,b)^{-1}(a,b)=(1,0), \\ i^2=(-1,0).
\end{gathered}
\tag{FA0c}
\]
Thus these pairs form a field. The real inclusion \(a\mapsto(a,0)\) preserves both operations, is injective and gives the original real subfield. Conjugation is the actual map \((a,b)\mapsto(a,-b)\); the two-coordinate multiplication shows that it preserves products, conjugates sums, and has square the identity. Keeping the original squared modulus \(N(a,b)=a^2+b^2\), expansion gives
\[
N((a,b)(c,d))=(ac-bd)^2+(ad+bc)^2
=a^2c^2-2acbd+b^2d^2+a^2d^2+2adbc+b^2c^2
=(a^2+b^2)(c^2+d^2).
\tag{FA0d}
\]
The middle two mixed terms are opposite by the scalar real field laws; no matrix product is being commuted. This supplies the actual complex arithmetic and conjugation used below from the stated real base.

Finite polynomial arithmetic is equally explicit. For original coefficients \(p(z)=\sum_j a_jz^j\), \(q(z)=\sum_k b_kz^k\), with coefficients zero outside their finite lists, addition has coefficients \(a_l+b_l\), and multiplication has coefficients \(\sum_{j+k=l}a_jb_k\). Distributivity and associativity follow by retaining the same finite ordered sums: the coefficient of a triple product at \(l\) is \(\sum_{j+k+t=l}a_jb_kc_t\) under either association. The constant polynomial one is the multiplicative identity, and zero is the additive identity. For nonzero original polynomials of degrees \(m,n\), the highest coefficient of their product is the original nonzero product \(a_mb_n\), so its degree is \(m+n\). These assertions include constant polynomials and the zero polynomial without assigning a degree to zero. Finite induction on the resulting nonnegative degree is the original finite-induction principle. Section 2 uses precisely this arithmetic for division and Bézout.

A vector space over \(F\) has the usual addition and scalar multiplication. The span of a finite list is the set of all of its finite linear combinations, including the empty combination zero. A list is independent when its only zero linear combination has every coefficient zero. A finite-dimensional space means one admitting a finite spanning list; a basis is an independent spanning list. The zero space has the empty basis.

Let \(u_1,\ldots,u_r\) be independent and let the original list \(b_1,\ldots,b_N\) span \(V\). We prove \(r\leq N\) and replace selected original list positions by the actual \(u_j\) while keeping a spanning list. Suppose a spanning list already has \(u_1,\ldots,u_{j-1}\) and \(N-j+1\) remaining original vectors. Write

\[
u_j=\sum_{k<j}a_k u_k+\sum_{b\in L}c_b b.
\tag{FA1}
\]

At least one \(c_b\ne0\), because otherwise \(u_j\) belongs to the span of its independent predecessors. Choose such an actual original \(b\). Solving (FA1) gives

\[
b=c_b^{-1}u_j-\sum_{k<j}c_b^{-1}a_k u_k
 -\sum_{b'\in L\setminus\{b\}}c_b^{-1}c_{b'}b'.
\tag{FA2}
\]

Both expressions retain their original nonzero coefficient and its inverse. Replacing this \(b\) by \(u_j\) preserves the span in both directions. The operation needs a remaining vector at each step; after \(N\) steps there is none, so an independent list cannot have a further member. This proves the bound and the asserted exchange construction without first assuming existence of a basis.

Now start with any independent list and scan the original finite spanning list in its original order. Append a vector exactly when it is outside the current span. An appended vector preserves independence: a zero combination with nonzero coefficient on the new vector would put it in the preceding span. At the end every original spanning vector is in the resulting span. Thus the list extends to a basis. Starting with the empty list gives existence of a basis. Applying the exchange bound in both directions to two bases proves that they have the same number of vectors. This number is \(\dim_F V\).

Every subspace \(W\subset V\) has a finite basis. Choose a vector outside the current span in \(W\) whenever one exists. An independent list in \(W\) is also independent in \(V\), so it can never exceed the finite dimension of \(V\). By that bound the construction terminates after at most \(\dim V\) choices and then spans \(W\). This is only a finite selection. Its actual selected vectors can be extended to a basis of \(V\) by the preceding construction.

### 10.2. Coordinates, matrix products and basis comparisons

For an ordered original basis \(b=(b_1,\ldots,b_n)\), the map

\[
\begin{gathered}
J_b:F^n\longrightarrow V, \\ J_b x=\sum_{j=1}^n x_j b_j
\end{gathered}
\tag{FA3}
\]

is linear, surjective by span and injective by independence. Its inverse gives the unique original coordinates. For \(n=0\) this is the unique map between zero spaces and is a bijection.

Let \(T:V\to W\) be linear, with ordered basis \(c=(c_1,\ldots,c_q)\) in \(W\). Define \(A_{ij}\) by the unique expression \(Tb_j=\sum_i A_{ij}c_i\). Then

\[
\begin{gathered}
T=J_c A J_b^{-1}, \\ (Ax)_i=\sum_{j=1}^n A_{ij}x_j.
\end{gathered}
\tag{FA4}
\]

This constructs the matrix rather than assuming it. Every matrix conversely defines this linear map. Addition and scalar multiplication of maps are entrywise addition and multiplication of their matrices. If \(U:W\to Z\) has matrix \(B\) in the actual target basis, finite expansion gives

\[
\begin{gathered}
(BA)_{kj}=\sum_{i=1}^q B_{ki}A_{ij}, \\ UT=J_d BA J_b^{-1}.
\end{gathered}
\tag{FA5}
\]

The order is \(BA\). Expanding each finite triple sum and keeping the same ordered summands proves associativity. The coordinate matrix of the identity is \(I_n\), with entries \(\delta_{ij}\). Every empty sum and zero dimension in (FA4)--(FA5) has its literal value; no nonzero-dimensional hypothesis has entered.

For new bases \(b'_j=\sum_k S_{kj}b_k\) and \(c'_i=\sum_l R_{li}c_l\), (FA3) gives \(J_{b'}=J_b S\) and \(J_{c'}=J_c R\). Both \(S\) and \(R\) are invertible because the two coordinate maps are bijective. The inverse of a linear bijection is linear: apply the bijection to the two sides of its desired addition and scalar identities, and use injectivity. Matrix multiplication in (FA5) therefore proves

\[
\begin{gathered}
x=Sx', \\  x'=S^{-1}x, \\  A'=R^{-1}AS, \\ J_{c'}A'J_{b'}^{-1}=J_cAJ_b^{-1}.
\end{gathered}
\tag{FA6}
\]

These equalities are the actual coordinate morphisms for the unchanged original map \(T\); they are not replacements of that map. For two inverse linear maps their matrix products in both orders are the corresponding identity matrices. For a square matrix possessing a two-sided matrix inverse, (FA4) conversely gives a linear bijection and its inverse.

### 10.3. Rank-nullity, quotients and direct sums

Let \(T:V\to W\) be any original linear map, and choose the actual basis \(k_1,\ldots,k_a\) of its kernel. Extend it to \(k_1,\ldots,k_a,v_1,\ldots,v_r\) in \(V\) by Section 10.1. The vectors \(Tv_1,\ldots,Tv_r\) are independent: if \(T\sum_j t_jv_j=0\), that sum is in the span of the \(k_i\), and independence of the extended basis forces every \(t_j=0\). They span \(\operatorname{im}T\), because applying \(T\) to any original basis expansion discards precisely the kernel summands. Hence

\[
\begin{gathered}
\dim V=a+r, \\  \dim\ker T=a, \\ \dim\operatorname{im}T=r.
\end{gathered}
\tag{FA7}
\]

The exact quotient map is \(v\mapsto v+\ker T\); the induced map \(V/\ker T\to\operatorname{im}T\), \(v+\ker T\mapsto Tv\), is well defined because two representatives differ by a kernel vector. It is injective by the definition of the kernel and surjective by that of the image. Its inverse in the displayed basis is \(\sum_j t_jTv_j\mapsto\sum_j t_jv_j+\ker T\), with all original coefficients retained.

For any subspace \(K\subset V\), choose a basis of \(K\) and extend it to \(V\). The cosets of the added basis vectors form a basis of \(V/K\): span follows from the original expansion and independence follows by subtracting an element of \(K\). Therefore \(\dim(V/K)=\dim V-\dim K\). The span \(L\) of the added vectors has \(K\cap L=\{0\}\), and every vector has a unique expansion as a sum from \(K\) and \(L\). The addition map \(K\oplus L\to V\) is a bijection with inverse the actual two coordinate projections. In general, the addition map \(U\oplus W\to U+W\) is surjective and has kernel exactly \(\{(v,-v):v\in U\cap W\}\). Using (FA7) proves

\[
\dim(U+W)=\dim U+\dim W-\dim(U\cap W).
\tag{FA8}
\]

The same coordinate argument iterated proves the finite direct-sum statement: addition from \(\bigoplus_j V_j\) is a bijection precisely when every zero sum from the subspaces has all terms zero and their sum is the target space. Concatenating their actual bases then gives its basis and dimension \(\sum_j\dim V_j\). This supplies the direct-sum dimensions used by the stable primary decomposition.

A square map \(V\to V\) is injective if and only if it is surjective, by (FA7) and equality of its two original dimensions. A bijection is exactly an invertible matrix under Section 10.2. These assertions include dimension zero.

### 10.4. Determinants and the full ordered elimination maps

For an original square matrix \(M=(m_{ij})\) of size \(n\), define its determinant by the finite full sum

\[
\det M=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                  \prod_{i=1}^n m_{i,\sigma(i)}.
\tag{FA9}
\]

The sign is \((-1)\) to the number of inversions. Interchanging two indices changes that parity: for adjacent indices it changes one inversion and interchanging arbitrary indices is an odd number of adjacent exchanges. Thus exchanging two rows, or two columns, changes the sign of (FA9) by relabeling permutations. Identical rows or columns give zero by pairing equal products with opposite signs. Multilinearity in each row and column follows by expanding its single factor in every product. Adding a multiple of another row leaves the determinant unchanged because its additional summand has two identical rows. The identity matrix has determinant one, since every nonidentity permutation has a literal zero factor. For \(n=0\), the single empty permutation has the empty product one.

For arbitrary original square matrices \(X,Y\), expand every entry of the product before making any comparison:

\[
\det(XY)=\sum_{k_1,\ldots,k_n=1}^n
 \left(\prod_{i=1}^n X_{i,k_i}\right)
 \sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
                  \prod_{i=1}^n Y_{k_i,\sigma(i)}.
\tag{FA10}
\]

If two \(k_i\)'s agree, exchanging the columns assigned to their two positions pairs the inner permutations without a fixed point, with equal products and opposite signs. The whole inner sum is exactly zero. Every remaining list is \(k_i=\tau(i)\) for a permutation \(\tau\). Reordering its rows gives inner sum \(\operatorname{sgn}(\tau)\det Y\). Indeed the relabeled column permutation is \(\sigma\circ\tau^{-1}\), whose sign is \(\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)\); this follows from the adjacent-exchange sign calculation above. The surviving full sum in (FA10) is therefore \(\det X\det Y\). No summand is discarded without this exact zero calculation. In particular \(\det S\det S^{-1}=1\) whenever both inverse products are the identity.

Here is the exact elimination construction for an original rectangular \(q\)-by-\(n\) matrix. Scan columns in their original order; for the next pivot choose a nonzero entry in the remaining rows, exchange its row with the next pivot row if necessary, and subtract the full pivot multiple from every lower row. Do not divide the pivot row or replace its pivot by one. Each exchange has an actual permutation matrix with its inverse the same exchange. Each subtraction has matrix \(I-cE_{ij}\), where \(i\ne j\), and inverse \(I+cE_{ij}\), since \(E_{ij}^2=0\). If \(E=E_\ell\cdots E_1\) is the full ordered product, the echelon matrix is \(R=EM\) and \(M=E_1^{-1}\cdots E_\ell^{-1}R\). There are at most \(\min(q,n)\) pivots; scan and row count are finite, so the procedure terminates. Every remaining row is zero, since otherwise its first nonzero entry would have supplied a pivot when its column was scanned.

Write the actual pivot columns as \(c_1<\cdots<c_r\), their nonzero original resulting pivots as \(d_j=R_{j,c_j}\), and let \(J\) be the nonpivot columns. For arbitrary prescribed original free coordinates \(x_k=t_k\), \(k\in J\), solve backwards by

\[
\begin{gathered}
x_{c_j}=-d_j^{-1}\sum_{k>c_j}R_{jk}x_k, \\ j=r,r-1,\ldots,1.
\end{gathered}
\tag{FA11}
\]

Each later pivot coordinate has already been computed, and earlier coefficients in that row are zero by echelon construction. Every zero row imposes no equation. Hence (FA11) is a linear bijection \(F^J\to\ker M\), inverse to the actual free-coordinate projection, because \(E\) is invertible. The coordinate vectors of \(F^J\) give the full kernel basis, with original pivot denominators retained. Thus \(\dim\ker M=n-r\) and \(\operatorname{rank}M=r\) by (FA7). In particular, the number of pivots is independent of the choices of exchange rows even though the displayed coordinate map can depend on them.

If \(q=n\), there are two cases. For \(r<n\), echelon form has a zero row and determinant zero. Each exchange contributes \(-1\), and each subtraction contributes one, by (FA9); hence \(\det M=0\) as well, and (FA11) gives a nonzero kernel vector. For \(r=n\), all columns are pivot columns, \(R\) is upper triangular and its full permutation sum gives \(\det R=\prod_j d_j\): every other permutation has a lower-triangular zero factor, proved successively from the last row upwards. If \(s\) row exchanges occurred, this gives

\[
\begin{gathered}
\det E=(-1)^s, \\ \det M=(-1)^s\prod_{j=1}^n d_j\ne0.
\end{gathered}
\tag{FA12}
\]

For an arbitrary right side \(y\), the exact inverse is found from \(z=Ey\) and

\[
\begin{gathered}
x_j=d_j^{-1}\left(z_j-\sum_{k>j}R_{jk}x_k\right), \\  j=n,n-1,\ldots,1, \\ M^{-1}=R^{-1}E.
\end{gathered}
\tag{FA13}
\]

Backward substitution gives a solution and makes it unique. Applying the two compositions to arbitrary vectors proves both inverse identities. Thus a square original matrix is invertible exactly when its original determinant is nonzero, over either field. No eigenvalue-existence theorem enters this proof.

For later continuity uses, define the cofactor \(C_{ij}=(-1)^{i+j}\det M^{(i|j)}\) with the indicated row and column deleted, and \(\operatorname{adj}(M)_{ji}=C_{ij}\). In (FA9), group the permutations by the column used by row \(i\). Moving that row/column to their first positions produces the sign \((-1)^{i+j}\), giving \(\sum_j m_{ij}C_{ij}=\det M\). Replacing this row by a distinct row gives the off-diagonal sum zero by the repeated-row determinant. The column version gives the other product. Consequently

\[
\begin{gathered}
M\operatorname{adj}(M)=\operatorname{adj}(M)M=(\det M)I_n, \\ M^{-1}=(\det M)^{-1}\operatorname{adj}(M)
\quad(\det M\ne0).
\end{gathered}
\tag{FA14}
\]

This retains the exact original determinant denominator and every cofactor sign. When \(n=1\), the minor is the zero-dimensional determinant one. When \(n=0\), the adjugate is the unique empty matrix and both product identities are identities of empty matrices. All determinants and cofactors are finite polynomial expressions, so the inverse is continuous on the actual nonzero-determinant domain by the scalar quotient rule.

### 10.5. The original inner product and the full Gram residuals

An inner product \(h\) is linear in its first variable, conjugate-linear in its second, has \(h(v,w)=\overline{h(w,v)}\), and satisfies \(h(v,v)>0\) for \(v\ne0\). These are its definition, not a consequence assumed for a different matrix. Let \(\|v\|_h=\sqrt{h(v,v)}\). The positive real square root exists from real completeness: the nonempty bounded set \(\{t\ge0:t^2\le a\}\) has a supremum for \(a>0\), and continuity of the square shows its square can be neither below nor above \(a\), by a sufficiently small positive increment or decrement. Its strict monotonicity on nonnegative reals proves uniqueness. Zero has square root zero.

For any chosen original basis \(b\), keep the full matrix

\[
\begin{gathered}
H_{jk}=h(b_k,b_j), \\ 
h(J_bx,J_by)=y^\dagger Hx
 =\sum_{j,k}\overline{y_j}H_{jk}x_k, \\ H^\dagger=H.
\end{gathered}
\tag{FA15}
\]

Here \(\dagger\) is conjugate transpose, with entry \((M^\dagger)_{jk}=\overline{M_{kj}}\). Formula (FA15) follows by finite expansion and fixes the linear-first convention exactly. If \(Hx=0\), then \(x^\dagger Hx=0\), so positivity and the coordinate bijection give \(x=0\). Therefore \(H\) is invertible by Sections 10.3--4. Conversely, any Hermitian matrix with \(x^\dagger Hx>0\) for \(x\ne0\) gives an inner product by (FA15), since the linearity, Hermitian identity and positivity follow entrywise. An inner product exists on any finite vector space by taking the explicitly constructed coordinate formula \(h_0(J_bx,J_by)=\sum_j x_j\overline{y_j}\). This existence construction does not replace an already given \(h\).

For a basis \(b_1,\ldots,b_n\), define its actual residuals inductively, keeping every length and projection factor:

\[
\begin{gathered}
r_1=b_1, \\  d_k=h(r_k,r_k), \\ r_j=b_j-\sum_{k<j}\frac{h(b_j,r_k)}{d_k}r_k.
\end{gathered}
\tag{FA16}
\]

Assume the earlier residuals are nonzero and mutually orthogonal. Then the displayed formula has defined nonzero denominators. Direct pairing with \(r_l\), \(l<j\), gives \(h(r_j,r_l)=h(b_j,r_l)-h(b_j,r_l)d_l/d_l=0\), with all other summands zero by the earlier orthogonality. If \(r_j=0\), the formula puts \(b_j\) in the earlier residual span. Each earlier residual lies in the corresponding original initial span, so this contradicts the independence of \(b\). Hence \(r_j\ne0\), \(d_j>0\), and induction proves all assertions. The converse expressions in (FA16) show equality of the original and residual initial spans at every stage; in particular the residuals are a basis.

Let \(S\) be the matrix with these actual residual coordinates, \(r_j=J_bS e_j\). It is upper triangular with diagonal one by (FA16), and \(D=\operatorname{diag}(d_1,\ldots,d_n)\). The exact Gram and determinant comparisons are

\[
\begin{gathered}
S^\dagger HS=D, \\  H=(S^{-1})^\dagger DS^{-1}, \\ \det H=\prod_{j=1}^n d_j>0\quad(n>0).
\end{gathered}
\tag{FA17}
\]

The first equality is the full pairing of the actual residuals; the second multiplies by the actual inverses in the stated order. The determinant identity uses multiplicativity, \(\det S=1\), and \(\det S^\dagger=\overline{\det S}\). The last conjugate identity follows by conjugating (FA9) and transposing permutations; the inverse permutation has the same sign. In dimension zero the product and \(\det H\) are both one, and the zero space is its own orthogonal basis.

The requested orthonormal Gram--Schmidt comparison consists of the explicitly defined vectors \(e'_j=d_j^{-1/2}r_j\), not a change to any earlier residual. Set \(U=S D^{-1/2}\). The two coordinate maps and every metric factor are

\[
\begin{gathered}
J_{e'}=J_b U, \\  x=Uz, \\ 
z=D^{1/2}S^{-1}x, \\ 
U^\dagger HU=D^{-1/2}S^\dagger HS D^{-1/2}=I_n, \\ \det U=\prod_j d_j^{-1/2}.
\end{gathered}
\tag{FA18}
\]

Thus \(e'\) is an orthonormal basis for the original \(h\), while the original \(H\), \(S\), \(r_j\) and \(d_j\) remain explicit in (FA15)--(FA18). Over the real field all \(d_j^{-1/2}\) are positive, so the comparison orientation has the sign of \(\det S=1\). No arbitrary sign is inserted. The complex determinant is the displayed positive real factor in these original coordinates.

For an independent list which is not yet a basis, the same induction gives its nonzero orthogonal residuals; extending the original list to a basis by Section 10.1 extends that orthogonal construction. For a subspace with these residuals \(r_1,\ldots,r_a\), the exact original projection and its complement are

\[
\begin{gathered}
Pv=\sum_{k=1}^a\frac{h(v,r_k)}{d_k}r_k, \\  h(v-Pv,r_k)=0, \\ V=W\oplus W^\perp.
\end{gathered}
\tag{FA19}
\]

Indeed the residuals span \(W\); the difference is orthogonal to their span by conjugate-linearity, and an element in \(W\cap W^\perp\) has zero self-pairing and is zero. Pairing gives \(P^2=P\) and \(h(Pv,w)=h(v,Pw)\), because each side is the same sum \(\sum_k h(v,r_k)h(r_k,w)/d_k\). These statements also hold for the empty subspace, whose projection is zero.

### 10.6. Exact finite inner-product bounds and the unchanged original norm

For \(w\ne0\), the original residual \(v-h(v,w)h(w,w)^{-1}w\) has squared norm

\[
\left\|v-\frac{h(v,w)}{h(w,w)}w\right\|_h^2
=\|v\|_h^2-\frac{|h(v,w)|^2}{\|w\|_h^2}\ge0.
\tag{FA20}
\]

Expand its two cross terms using the specified linear-first convention; each is \(-|h(v,w)|^2/h(w,w)\), and the last term adds one copy. This proves Cauchy--Schwarz with its actual denominator. If \(w=0\), the pairing is zero by linearity and the same inequality without division is immediate. The equality case for nonzero \(w\) holds exactly when this actual residual is zero, hence when \(v\) is a scalar multiple of the actual \(w\). The norm obeys \(\|av\|_h=|a|\|v\|_h\), positivity, and the triangle inequality: expand \(\|v+w\|_h^2\), bound the two real cross terms by \(2\|v\|_h\|w\|_h\), and take the nonnegative square root.

For the full residual basis, orthogonality gives the exact identities

\[
\begin{gathered}
v=\sum_{j=1}^n\frac{h(v,r_j)}{d_j}r_j, \\  \|v\|_h^2=\sum_{j=1}^n\frac{|h(v,r_j)|^2}{d_j}, \\ \left\|v-\sum_{j=1}^a\frac{h(v,r_j)}{d_j}r_j\right\|_h^2
=\|v\|_h^2-\sum_{j=1}^a\frac{|h(v,r_j)|^2}{d_j}.
\end{gathered}
\tag{FA21}
\]

The first equality follows by pairing the difference with every residual in the basis, and positivity. The other two follow by expansion with every original \(d_j\) retained. These are finite sums; they assume no infinite-dimensional orthonormal expansion.

For \(n>0\), set \(d_{\min}=\min_jd_j>0\), \(F_S=(\sum_{j,k}|S_{jk}|^2)^{1/2}>0\), and \(M_b=(\sum_j\|b_j\|_h^2)^{1/2}>0\). With \(x=S a\), (FA17), finite scalar Cauchy--Schwarz in every row of \(S\), and the original basis triangle inequality give

\[
\begin{gathered}
\frac{\sqrt{d_{\min}}}{F_S}|x|_2
 \le \|J_bx\|_h
 \le M_b|x|_2, \\ |x|_2^2=\sum_j|x_j|^2.
\end{gathered}
\tag{FA22}
\]

For the lower bound, \(\|J_bx\|_h^2=\sum_jd_j|a_j|^2\ge d_{\min}|a|_2^2\), while \(|S a|_2\le F_S|a|_2\). For the upper bound, \(\|\sum_jx_jb_j\|_h\le\sum_j|x_j|\|b_j\|_h\le M_b|x|_2\). Thus both inequalities are for the original \(h\), basis and coordinates; their exact comparison constants are preserved. In dimension zero every vector and norm is zero, so no division by \(F_S\) is needed. Completeness of the finite original inner-product space follows: (FA22) makes the coordinates of a Cauchy sequence Cauchy in \(F\); their scalar limits give a vector, and the upper inequality proves convergence in the unchanged original norm.

For \(T:V\to W\), with \(n>0\), the same expansion gives the concrete bound

\[
\|Tv\|_{h_W}\le
\frac{F_S}{\sqrt{d_{\min}}}
\left(\sum_{j=1}^n\|Tb_j\|_{h_W}^2\right)^{1/2}
\|v\|_{h_V}.
\tag{FA23}
\]

Every original image \(Tb_j\) occurs in this constant. The bound proves that every finite linear map is continuous. Define its operator norm by \(\|T\|=\sup_{v\ne0}\|Tv\|/\|v\|\), with value zero if its domain is zero. This is finite by (FA23). Applying the definition twice to the actual vectors gives \(\|UT\|\le\|U\|\|T\|\); the zero-vector cases require no division. Addition and scalar norm identities follow from the original vector norm inequalities, and \(\|I_V\|=1\) for \(V\ne0\), zero for \(V=0\). In particular all fixed finite coordinate maps and projections in the spectral receiving calculation are bounded on the original spaces, without replacing their norms by coordinate norms.


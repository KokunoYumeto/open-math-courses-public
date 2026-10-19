# Completing the finite-dimensional prerequisites

This companion proves finite-dimensional compactness, cofactor inversion,
smooth inverse and implicit maps, the Schur-complement Hessian formula,
and invariance of the positive and negative dimensions of a symmetric form.
These are the finite-dimensional tools used in the parameter-Morse reading.

Mathematical source: Jiří Lebl, *Basic Analysis I–II*, theorem numbering
from version 6.3 (15 May 2026), [freely accessible author edition](https://www.jirka.org/ra/).
The C¹ base results are the [inverse theorem and proof, 8.5.1](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#sec_svinvfuncthm-2-9)
and [implicit theorem and proof, 8.5.6](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#sec_svinvfuncthm-3-12).
The human-proof references identify
other external statements and proofs; the programme index
locates the local arguments and their exact inputs.

Original programme exposition: CC0 to the extent rights exist. Cited
human works are external sources and retain their own terms.

## P1. The finite-dimensional step in Heine–Borel

**Statement.** If \(K\subset\mathbb R^n\) is closed and bounded, then every
sequence in \(K\) has a subsequence converging to a point of \(K\).
Consequently \(K\) is compact in the open-cover sense.

**Proof inputs.** The real Bolzano–Weierstrass theorem, preservation
of limits by subsequences, the sequential characterization of closed sets,
and Lebl's Theorem 7.4.11 relating sequential and open-cover compactness.
Their statement and proof references are in the [proof index](proof-map.html#P1).
The local [sequence lemmas P6](proof-map.html#P6.0) and
[positive roots P8](proof-map.html#P8-root) supply the indicated elementary
steps. The induction below proves the arbitrary-dimensional assertion.

**Proof.** If \(n=0\), the Euclidean space consists of the single empty
tuple. Its only subsets are empty or singletons. The empty set is compact;
for a singleton choose one member of any open cover containing its point.
Every sequence in the singleton is constant. This proves the assertion in
dimension 0. Now let \(n\geq1\), and let
\(x_j=(x_j^1,\ldots,x_j^n)\) be a sequence in \(K\).
Boundedness gives a number \(R\) with \(|x_j^k|\leq R\) for every
\(j,k\). Construct nested subsequences, one coordinate at a time.
At stage one, real Bolzano–Weierstrass gives a subsequence on which
\(x_j^1\) converges. Suppose after stage \(k<n\) there is a subsequence
on which all the first \(k\) coordinates converge. Its \((k+1)\)st
coordinate is still a bounded real sequence. Extract a further subsequence
on which this coordinate converges. Each of the first \(k\) coordinates
retains its limit. Finite induction gives a single subsequence, indexed by
\(j_\ell\), with \(x_{j_\ell}^k\to x^k\) for all \(1\leq k\leq n\).

Put \(x=(x^1,\ldots,x^n)\). Given \(\varepsilon>0\), for each coordinate
choose \(L_k\) such that \(|x_{j_\ell}^k-x^k|<\varepsilon/\sqrt n\)
when \(\ell\geq L_k\). For \(\ell\geq\max_kL_k\),
\[
 |x_{j_\ell}-x|^2=\sum_{k=1}^n|x_{j_\ell}^k-x^k|^2<\varepsilon^2.
\]
Thus the subsequence converges in the Euclidean metric. Since \(K\) is
closed and every term belongs to \(K\), its limit belongs to \(K\).
The proved equivalence in Theorem 7.4.11 now supplies the finite-subcover
property. This completes the arbitrary-dimensional step left as an
exercise after the two-dimensional argument in Theorem 7.4.14. \(\square\)

## P2. Cofactors and smooth dependence of an inverse

**Statement.** For a square real matrix \(A\), the cofactor matrix gives
\[
 A\operatorname{adj}A=(\operatorname{adj}A)A=(\det A)I.
 \tag{P2.1}
\]
Consequently, on the open set \(\det A\ne0\),
\[
 A^{-1}=\frac{\operatorname{adj}A}{\det A},
 \qquad
 d(A^{-1})[E]=-A^{-1}EA^{-1}.
 \tag{P2.2}
\]
The entries of \(A^{-1}\) are smooth functions of the entries of \(A\).

**Earlier programme inputs.** The permutation definition and multilinearity
of the determinant from §8.2.3, the sign change under a row or column
interchange, the product rule for derivatives, and smoothness of the scalar
reciprocal away from zero. Its difference quotient is
\((1/(t+h)-1/t)/h=-1/(t(t+h))\), which tends to \(-t^{-2}\).
Repeated product rules then give its \(k\)th derivative
\((-1)^k k!t^{-k-1}\).
Indeed the derivative of the product of \(k+1\) reciprocal factors is
the sum of \(k+1\) equal terms, giving
\((t^{-k-1})'=-(k+1)t^{-k-2}\). Multiplication by \((-1)^k k!\)
proves the induction step, starting with the displayed first derivative.
Its continuity follows from
\(|u^{-1}-v^{-1}|=|u-v|/|uv|\) on an interval separated from zero.

**Proof.** Write \(A_{\widehat i,\widehat j}\) for the matrix obtained by
removing row \(i\) and column \(j\), with the determinant of the empty
matrix defined to be 1. Group the permutation formula by the entry
chosen in row \(i\). Removing that row and its chosen column leaves a
permutation of the other indices. Moving row \(i\) and column \(j\)
to the first positions uses \((i-1)+(j-1)\) interchanges, of parity
\(i+j\). Thus grouping gives the row expansion
\[
 \det A=\sum_{j=1}^n a_{ij}(-1)^{i+j}
                         \det A_{\widehat i,\widehat j}.
 \tag{P2.3}
\]
Define \(C_{ij}=(-1)^{i+j}\det A_{\widehat i,\widehat j}\) and
\(\operatorname{adj}A=C^T\). The \((i,k)\) entry of
\(A\operatorname{adj}A\) is \(\sum_j a_{ij}C_{kj}\). For \(i=k\)
this is \(\det A\) by (P2.3). For \(i\ne k\), it is the row-\(k\)
expansion of the matrix obtained by replacing row \(k\) with row \(i\):
the minors omitting row \(k\) have not changed. That matrix has two equal
rows, so its determinant is zero. This proves the first identity in
(P2.1). Column expansion gives the second identity by the same argument.

If \(\det A\ne0\), division proves the first formula in (P2.2).
The determinant and every cofactor are finite polynomials in matrix
entries. Polynomial smoothness and the scalar reciprocal calculation
prove smoothness of the inverse. Differentiating \(A^{-1}A=I\) in
the direction \(E\) yields
\(d(A^{-1})[E]A+A^{-1}E=0\); multiplication by \(A^{-1}\) on the right
gives the second formula. This argument proves smoothness rather than
assuming it in order to differentiate the inverse. \(\square\)

## P3. Upgrading the inverse and implicit theorems to smooth maps

**Statement.** In Lebl's inverse function theorem, if \(f\) is \(C^r\),
for an integer \(r\geq1\), then its local inverse is \(C^r\). If \(f\)
is smooth, its inverse is smooth. The corresponding assertions hold for
the implicit function theorem, jointly in all the parameter variables.

**Earlier programme inputs.** The \(C^1\) inverse and implicit
proofs of Theorems 8.5.1 and 8.5.6, with the product-neighbourhood choice
made explicit in P10.6; the chain and product rules; and P2.
The regularity assertion in Remark 8.5.8 is not used as a proof.

**Proof.** Write \(g=f^{-1}\) on the open neighbourhood supplied by the
\(C^1\) theorem. That theorem already proves
\[
 Dg(y)=[Df(g(y))]^{-1}.\tag{P3.1}
\]
Suppose \(f\in C^r\), and start with the established fact \(g\in C^1\).
For \(1\leq k<r\), assume \(g\in C^k\). Then \(Df\in C^{r-1}\),
so repeated chain and product rules show \(Df\circ g\in C^k\), since
\(k\leq r-1\). P2 shows that matrix inversion preserves \(C^k\) where
the determinant is nonzero. Hence (P3.1) says \(Dg\in C^k\), which
is the definition of \(g\in C^{k+1}\). Induction proves the finite
\(r\) assertion; applying it for every \(r\) proves the smooth one.

For an implicit equation \(F(s,x)=0\), the earlier proof applies the
inverse theorem to
\(\mathcal F(s,x)=(s,F(s,x))\). Its derivative is the block matrix
\[
 D\mathcal F=\begin{pmatrix}I&0\\D_sF&D_xF\end{pmatrix}.
\]
When \(D_xF\) is invertible this block matrix has inverse
\(\left(\begin{smallmatrix}I&0\\-(D_xF)^{-1}D_sF&(D_xF)^{-1}\end{smallmatrix}\right)\),
as direct multiplication verifies. The inverse \(\mathcal G\) is
\(C^r\) by the assertion just proved. The solution is the last coordinate
block of \(\mathcal G(s,0)\), so it is \(C^r\) jointly in \(s\).
No uniform size of a neighbourhood across an unbounded parameter family
is asserted. \(\square\)

## P4. The Schur-complement step in the parameter Morse proof

**Statement.** Let \(\phi(x_1,x',s)\) be smooth, with a critical point
at \(x=0\) for each nearby \(s\), and suppose
\(a=\partial_1^2\phi(0,s)\ne0\). Write its Hessian at that point as
\[
 H=\begin{pmatrix}a&b^T\\b&C\end{pmatrix}.
\]
Let \(x_1=u(x',s)\) be the local solution of
\(\partial_1\phi=0\), and put \(g(x',s)=\phi(u(x',s),x',s)\).
Then
\[
 D_{x'}u(0,s)=-a^{-1}b^T,\qquad
 D_{x'}^2g(0,s)=C-a^{-1}bb^T=:S,\qquad
 \det H=a\det S.\tag{P4.1}
\]
In particular \(S\) is invertible if \(H\) is invertible.

**Proof inputs.** P3, the chain rule, the local
[mixed-partial identity P11.2](integration-prerequisite-completions.html#proof-P11.2-bridge),
and determinant multiplication in Lebl's Proposition 8.2.9, located in the
human-proof references.

**Proof.** Differentiate
\(\partial_1\phi(u(x',s),x',s)=0\) in \(x'\). At the critical point
this gives \(aD_{x'}u+b^T=0\), proving the first identity. The first
derivative of \(g\) is \(\phi_{x'}\), evaluated on this graph,
because the extra factor \(\phi_1D_{x'}u\) vanishes identically there.
Differentiating again and substituting the first identity gives
\(D_{x'}^2g=C+bD_{x'}u=C-a^{-1}bb^T\).

For the determinant identity use the explicit invertible matrix
\[
 T=\begin{pmatrix}1&-a^{-1}b^T\\0&I\end{pmatrix},\qquad
 T^THT=\begin{pmatrix}a&0\\0&S\end{pmatrix}.\tag{P4.2}
\]
Block multiplication proves the second formula. The permutation
definition gives \(\det T=1\): any nonzero permutation term must pick
the diagonal entry in each lower row, then the first entry in the first
row. It also gives
\(\det\operatorname{diag}(a,S)=a\det S\) by expanding the first column.
Determinant multiplication and invariance under transpose now yield
\(\det H=a\det S\). Thus if \(a\ne0\) and \(\det H\ne0\), then
\(\det S\ne0\), as required for the next induction step. \(\square\)

## P5. Why congruence preserves the signature

**Statement.** If \(H\) is real symmetric and invertible, and \(T\) is
invertible, then \(H\) and \(T^THT\) have the same numbers of positive
and negative eigenvalues. Consequently the Jacobian factor in Morse
coordinates is \(|\det H|^{-1/2}\) when the target Hessian has diagonal
entries \(\pm1\).

**Proof inputs.** The orthogonal diagonalization
[Q5](quadratic-stationary-phase.html#proof-Q5), finite-dimensional
linear independence and determinant multiplication. The explicit
[orthonormal complement P9.4](proof-map.html#P9.4) and
[dimension argument P9.5](proof-map.html#P9.5) supply the linear-algebra
steps used below.

**Proof.** In an orthogonal eigenbasis, suppose there are \(p\) positive
and \(q\) negative diagonal entries. The span \(E_+\) of the positive
eigenvectors is a \(p\)-dimensional subspace on which the quadratic form
is positive on every nonzero vector. No larger such subspace \(V\)
exists: the coordinate projection \(V\to E_+\) would have a nonzero
kernel if \(\dim V>p\), by finite-dimensional linear independence.
A nonzero vector in that kernel lies in the negative eigenspace and
has a negative quadratic value, a contradiction. Thus \(p\) is
characterized without a basis as the largest possible dimension of
a positive subspace. The identical argument for the negative form
characterizes \(q\).

The map \(x\mapsto Tx\) sends subspaces bijectively to subspaces,
preserves dimension, and satisfies
\(x^T(T^THT)x=(Tx)^TH(Tx)\). It therefore preserves both maximal
dimensions, proving invariance of the signature. Finally if
\(T^THT=J\) with \(J\) diagonal and entries \(\pm1\), determinant
multiplication gives
\((\det T)^2\det H=\det J\). Taking absolute values, using
\(|\det J|=1\), and then the positive square root gives
\(|\det T|=|\det H|^{-1/2}\). \(\square\)

## Calculus proof references

P1 gives finite-dimensional compactness; P2 gives the inverse-matrix
formula; P3 gives smooth inverse and implicit maps, jointly in parameters;
P4 gives the Hessian and determinant under one-variable elimination; and
P5 gives congruence invariance and the Morse Jacobian. Their lower inputs
are identified in the [programme proof index](proof-map.html).

The [mixed-partial and compact-integral companion](integration-prerequisite-completions.html)
contains P11–P12, including the integral Taylor formula and smooth
parameter integration. Global absolute integration and multidimensional
substitution are treated in their respective readings.

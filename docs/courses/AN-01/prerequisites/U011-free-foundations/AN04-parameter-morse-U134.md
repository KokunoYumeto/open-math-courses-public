# Smooth quadratic coordinates and their Jacobian

These are the complete M1–M2 arguments from the AN-04 programme reading *A smooth quadratic reduction with parameters*, together with its P4–P5 algebraic arguments. The [finite algebra foundation](stable-prerequisite-bridges.md), §10, proves dimension, determinant multiplication and inverse identities. Real symmetric orthogonal diagonalization is proved in [Point sources and complex Gaussian kernels](../../src/point-sources-and-complex-gaussian-kernels.md), §2. In P4 and P5 below, these are the determinant and spectral inputs.

Original programme exposition by the AN-04 course contributors; CC0 1.0 Universal to the extent rights exist. The earlier programme readings retain their own credits and terms.

Mathematical references: Jiří Lebl, *Basic Analysis II*, version 6.3, Theorems 8.5.1 and 8.5.6 ([inverse and implicit theorems](https://www.jirka.org/ra/html/sec_svinvfuncthm.html)); Victor Guillemin and Shlomo Sternberg, *Semiclassical Analysis*, 13 January 2010 author draft, §13.14.3 ([author draft](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf)).

## M1. Parameter Morse lemma and its Jacobian

Let \(U\subset\mathbb R^n\) and \(S\subset\mathbb R^p\) be open, and
let \(\phi\in C^\infty(U\times S;\mathbb R)\). Suppose
\[
 D_x\phi(x_0,s_0)=0,\qquad H_0=D_x^2\phi(x_0,s_0)
 \text{ is invertible}.
\]
There are neighbourhoods of \(s_0\) and of \(z=0\), a smooth critical
branch \(x_c(s)\), and a smooth map \(F(z,s)\) such that for each
nearby \(s\), \(z\mapsto F(z,s)\) is a local diffeomorphism and
\[
 F(0,s)=x_c(s),\qquad
 \phi(F(z,s),s)=c(s)+\tfrac12\sum_{j=1}^n\sigma_j z_j^2,
 \qquad c(s)=\phi(x_c(s),s),\quad \sigma_j\in\{1,-1\}.
 \tag{M1.1}
\]
The signs are independent of \(s\) on this neighbourhood. If
\(H(s)=D_x^2\phi(x_c(s),s)\), then
\[
 \sum_j\sigma_j=\operatorname{sgn}H(s),\qquad
 |\det D_zF(0,s)|=|\det H(s)|^{-1/2}.
 \tag{M1.2}
\]

**Proof inputs.** Here P3 denotes the supplied [smooth inverse and implicit maps](implicit-maps-U070.md), §§16.4–16.5. The [scalar calculus foundation](metric-foundation-bridges.md), §§12–13, gives mixed partials, integral Taylor remainders, smooth positive roots and parameter differentiation of finite integrals. P4 and P5 are proved below. P1 denotes finite-dimensional compactness in that same scalar foundation.

For \(n=0\), the coordinate space is a singleton. Take \(x_c(s)=x_0\),
\(F(0,s)=x_0\), and \(c(s)=\phi(x_0,s)\). The quadratic sum and
signature are 0, while the empty determinant and its Jacobian factor are 1.
This proves all assertions in that case. In the proof below, \(n\geq1\).

**Proof: locate and translate the critical point.** Apply the implicit
theorem, upgraded by P3, to the smooth map \(D_x\phi(x,s)\).
Its derivative in \(x\) at \((x_0,s_0)\) is \(H_0\), so there is a
unique smooth branch \(x_c(s)\) in a sufficiently small fixed product
neighbourhood. Replace \(x\) by \(x_c(s)+u\) and subtract \(c(s)\).
The resulting smooth function \(f(u,s)\) has
\(f(0,s)=0\), \(D_uf(0,s)=0\) and an invertible Hessian for every
nearby \(s\). The last assertion follows by continuity of the determinant
and its nonzero value at \(s_0\).

**Choose a nonzero scalar pivot.** A nonzero symmetric matrix has a vector
with nonzero quadratic value. To verify this without assuming a normal form,
if a diagonal entry is nonzero, use its coordinate vector. If every diagonal
entry is zero, some off-diagonal entry \(h_{ij}\) is nonzero, and
\((e_i+e_j)^TH(e_i+e_j)=2h_{ij}\ne0\). Make a fixed invertible linear
change of variables taking that vector to the first coordinate direction.
Such a change can be constructed by adjoining all coordinate vectors except
one in which the chosen vector has a nonzero component; expansion of the
resulting matrix in that row gives a nonzero determinant. This change is
fixed at \(s_0\), so it is smooth in the parameters. After shrinking the
neighbourhood, \(\partial_1^2 f(0,s)\) stays nonzero with one fixed sign.

**Eliminate one variable.** Write \(u=(u_1,u')\). P3 applied to
\(\partial_1 f\) gives a smooth function \(u_1=q(u',s)\) for which
\(\partial_1 f(q(u',s),u',s)=0\). Since \(u=0\) is critical and the
solution is locally unique, \(q(0,s)=0\). Put
\(g(u',s)=f(q(u',s),u',s)\). With \(v=u_1-q(u',s)\), the integral
Taylor formula proved in P12.6 gives
\[
 f(q(u',s)+v,u',s)=g(u',s)+\tfrac12v^2 A(v,u',s),
\]
\[
 A(v,u',s)=2\int_0^1(1-t)
             \partial_1^2 f(q(u',s)+tv,u',s)\,dt.
 \tag{M1.3}
\]
Shrink the product neighbourhood so that \(q(u',s)\) and
\(q(u',s)+v\) lie in a smaller coordinate interval whose closure stays
inside the phase domain, with the other coordinates fixed. The whole segment
between them then stays in that interval. Specifically apply P12.6 to the function
\(t\mapsto f(q(u',s)+tv,u',s)\) on \([0,1]\). Its first derivative
at 0 is zero and its second derivative is
\(v^2\partial_1^2f(q(u',s)+tv,u',s)\). This proves (M1.3) for every
sign of \(v\), including zero. The parameter integration is over a fixed
compact interval, so P12.7 proves that \(A\) is jointly smooth. No global
improper-integral input from Q1 is needed for this step. At \((v,u')=0\),
\(A(0,0,s)=\partial_1^2 f(0,s)\ne0\).

Shrink once more so that \(A\) is nonzero throughout the neighbourhood
with a single sign \(\sigma_1\). Define
\[
 z_1=v\sqrt{|A(v,u',s)|}.
\]
Its \(v\)-derivative at \((v,u')=(0,0)\) is
\(\sqrt{|A(0,0,s)|}>0\). Apply P3 to the map
\((v,u',s)\mapsto(z_1,u',s)\): its derivative is block triangular,
with this nonzero entry and identity blocks, hence invertible. We obtain
a smooth local inverse, jointly in \(z_1,u',s\). In these coordinates,
\[
 f=g(u',s)+\sigma_1z_1^2/2.\tag{M1.4}
\]
In particular the residual function is independent of \(z_1\).

**Induct with an invertible residual Hessian.** The function \(g\) has
\(g(0,s)=0\), and its first derivative vanishes at zero: differentiating
the composite contributes only first derivatives of \(f\) there. P4
computes its Hessian as the Schur complement of the chosen scalar pivot.
That complement is invertible because the original Hessian is invertible.
For \(n=1\), (M1.4) already completes the construction. For \(n>1\),
apply the same construction to \(g(u',s)\), in \(n-1\) variables and
with the same parameters. Finite induction yields a signed quadratic
form in all \(n\) coordinates. At each of the finitely many steps,
the nonzero pivot and the inverse map persist on an open neighbourhood
of the relevant base point. Take preimages of these neighbourhoods under
the preceding continuous coordinate maps, so they are neighbourhoods of
the same original base point. Their finite intersection is still a neighbourhood;
choose smaller product neighbourhoods inside it. Composing the inverse
coordinate maps and the initial translation gives the smooth map \(F\)
in (M1.1).

**Identify its signature and volume factor.** Differentiate (M1.1) twice
in \(z\) at zero. Terms containing second derivatives of \(F\) are
multiplied by \(D_x\phi(x_c(s),s)=0\), so the chain rule reduces to
\[
 [D_zF(0,s)]^T H(s)D_zF(0,s)
       =\operatorname{diag}(\sigma_1,\ldots,\sigma_n).
\]
P5 gives both the signature identity and the determinant identity
in (M1.2). This also proves local constancy of the Hessian signature
for this critical family; it has not been assumed as an unproved
spectral-continuity assertion. \(\square\)

## M2. The precise compact-parameter consequence

Suppose a smooth critical branch is defined on an open neighbourhood of a
compact parameter set \(S_0\), and its Hessian is invertible on \(S_0\).
For each point of \(S_0\),
M1 supplies a local parameter neighbourhood and a signed Morse chart.
Before selecting the cover, choose around each parameter point a smaller
open parameter neighbourhood with compact closure in its chart domain,
and a smaller coordinate ball with compact closure in the coordinate
domain. These smaller parameter neighbourhoods still cover \(S_0\).
P1 and the earlier compactness proofs supply a finite subcover.
On each selected product closure, every fixed finite list of derivatives
of the coordinate map is bounded by the earlier extreme-value theorem.
Its image under \((z,s)\mapsto(F(z,s),s)\) is compact, by the proved
continuous-image theorem, and is contained in the inverse map's open
domain. Derivatives of the inverse are bounded on that compact image by
the same extreme-value theorem. The largest of finitely many bounds is finite.

Thus later stationary-phase estimates can be proved in finitely many local
charts with uniform finite constants. This conclusion does not assert a
single global signed frame, nor a uniform coordinate size for a collection
of phases whose Hessians approach singularity. It also does not itself
construct the partition of unity or identify the clean quotient density;
those are additional steps in the full lesson.

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

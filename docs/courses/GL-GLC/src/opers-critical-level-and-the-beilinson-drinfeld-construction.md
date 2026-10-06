# Opers, critical level and the Beilinson–Drinfeld construction

*Draft. Self-checked by the writing AI. Original mathematical exposition: CC0 1.0.*

An oper is a connection with a maximally transverse Borel reduction. The reduction produces scalar differential equations and gives concrete affine families of local systems. At critical level, an affine Lie algebra's center is described by functions on opers. Localization assigns to a global oper a system of differential equations on the bundle stack with a tensor-compatible Hecke eigenproperty.

We construct the adjoint-semisimple principal slice, prove its unique gauge normal form in ordinary families, and derive the coordinate action and global affine oper space. We also prove the homogeneous invariant ring over the stated characteristic-zero field, identify its degrees with the principal heights and construct the weighted Kostant section. A separate scalar proof treats \(PGL_n\) through jets. We also prove the Schwarzian rule, algebraic \(PGL_2\) irreducibility and the critical \(\mathfrak{sl}_2\) invariant. Section 3.2 extends that calculation to the entire rank-one polynomial vacuum center and its coordinate-equivariant ordinary disc-oper comparison. Section 3.3 proves the general current-jet invariant algebra, PBW symbol bound, ordinary-family base change and vacuum commutativity; it constructs every basic type A lift and proves the whole type A polynomial vacuum algebra. The full center, localization, quantization and fundamental local equivalence theorems remain unproved; their precise statements below retain their complete scope.

The classical calculations use a fixed smooth projective connected curve over an algebraically closed characteristic-zero field, \(g\ge2\). The regular singular example separately uses the punctured projective line. The classical center and eigenobject statements in §§4–5 have their stated complex semisimple or simply connected hypotheses. Their full-field and reductive extensions remain unproved. Connections are algebraic de Rham connections; localization uses left D-modules. Ordinary-family assertions concern the fixed curve. Analytic comparisons and full derived moduli retain separate foundations.

## 1. General oper condition and the full adjoint target

For a connected reductive group \(H\), choose a Borel \(B\), maximal torus and simple roots \(\Delta\), and put
\[
\mathfrak h_{-1}=\mathfrak b+\sum_{\alpha\in\Delta}\mathfrak h_{-\alpha}.
\tag{A8.1}
\]
An \(H\)-oper is an \(H\)-bundle with connection and Borel reduction whose second fundamental form lies in \(\omega\otimes(\mathfrak h_{-1}/\mathfrak b)\), with every simple-root line component nowhere zero. Positive-root conjugation preserves this quotient subspace, and torus conjugation acts by the root characters, proving frame independence. A central connection is not measured by these components; general reductive and adjoint oper problems must retain that distinction.

The full adjoint-group theorem says that, for adjoint semisimple \(H\) and \(g\ge2\), its oper space is an affine space modeled on
\[
\bigoplus_jH^0(X,\omega^{d_j+1}),
\tag{A8.2}
\]
where the principal exponents \(d_j\) are retained with multiplicity. Sections 1.1.1–1.1.8 prove the full adjoint construction from the stated root/pinning and group premises, including its finite \(\mathfrak{sl}_2\) decomposition, Drinfeld–Sokolov slice, coordinate gauges and global existence. They also construct the ordinary formal-disc and punctured-disc coefficient functors and coordinate actions. Section 1.2 proves the comparison of principal exponents with invariant-polynomial degrees and the weighted Kostant section, using the earlier invariant-ring proofs at their explicit recursive foundations. Section 2 gives an independent scalar proof for \(PGL_n\), with exponents \(1,\ldots,n-1\).


### 1.1. Drinfeld–Sokolov normal form and global adjoint opers

#### 1.1.1. The pinned principal triple and the height grading

Let \(k\) be algebraically closed of characteristic zero. Let \(H\) be an adjoint semisimple group, with a pinning \((B,T,(e_i))\). Write \(N\) for the unipotent radical of \(B\), \(\mathfrak g=\operatorname{Lie}H\), \(\mathfrak t=\operatorname{Lie}T\), and \(\Delta=\{\alpha_1,\ldots,\alpha_\ell\}\) for the simple roots. Normalize the negative simple-root vectors by
\[
[e_i,f_j]=\delta_{ij}h_i,\qquad h_i=\alpha_i^\vee .
\tag{DS.A1}
\]
A coroot in a Lie-algebra formula means the differential of that cocharacter.

The algebraic root and group foundations used here are explicit: the reduced crystallographic root datum of the pinned group; its one-dimensional root-space decomposition and bracket rules; the simple coroot basis of \(\mathfrak t\); the displayed pinning relations; the semidirect product \(B=N\rtimes T\) and ordered positive-root subgroup coordinates on \(N\); and a finite-dimensional algebraic representation realizing \(H\) as a closed subgroup of a matrix group. For an adjoint group, \(X^*(T)\) is the root lattice. These are prerequisites concerning algebraic groups over this \(k\). A root-space proof restricted to complex Lie algebras does not by itself establish their full field generality. The arguments below prove the principal triple, the needed module decomposition and the gauge theorem from these premises, for every adjoint semisimple \(H\).

Put
\[
h=2\rho^\vee:=\sum_{\beta\in\Phi^+}\beta^\vee
=\sum_i c_i h_i,\qquad
f=\sum_i f_i,\qquad e=\sum_i c_i e_i.
\tag{DS.A2}
\]
Every \(c_i\) is a positive integer. Here is the root-system argument, including the normalization of \(h\). The dual root system has simple roots \(\alpha_i^\vee\). Indeed a positive coroot is a positive real combination of these vectors by rescaling the simple-root expansion of its root. Each \(\alpha_i^\vee\) is indecomposable among positive coroots: a decomposition would have all coefficients outside \(i\) zero, forcing proportional positive coroots, which reducedness excludes. The base theorem in [*Root systems and their Weyl groups*, Theorem 2.1 and the dual-system calculation (1.3)](../../RT-LIE/src/RT-LIE-08.md) then makes their expansions integral and nonnegative. The sum defining \(h\) includes each \(h_i\), so \(c_i>0\).

A simple reflection permutes positive coroots other than \(h_i\), and takes \(h_i\) to \(-h_i\). To check the permutation, expand a positive coroot other than \(h_i\) in the simple coroot basis. Some coefficient outside \(i\) is positive; reflection changes only the \(i\)-coefficient. Its image is a root with a positive coefficient, hence is positive by the same-sign property. Involutivity gives the permutation. This is the argument of Lemma 4.1 in that same root-system lesson. Therefore
\[
s_i(h)=h-2h_i.
\]
But the reflection formula on \(\mathfrak t\) is \(s_i(x)=x-\alpha_i(x)h_i\). Comparing gives \(\alpha_i(h)=2\). The pinning relations now give
\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\tag{DS.A3}
\]
For \(H\ne1\), these are an actual \(\mathfrak{sl}_2\) triple. The three vectors are nonzero and independent: \(h\) has simple-root values \(2\), and \(e,h,f\) have distinct adjoint-\(h\) weights \(2,0,-2\). This uses no principal-nilpotent classification. For the trivial group the three vectors are zero, and its coefficient functors are treated below.

Since the simple roots form a basis of \(X^*(T)\), there is a cocharacter \(\rho^\vee\) with \(\alpha_i(\rho^\vee(a))=a\). Its differential is \(h/2\). For a root \(\beta=\sum_i n_i\alpha_i\), set \(\operatorname{ht}(\beta)=\sum_i n_i\). The adjoint action of \(h\) gives
\[
\mathfrak g=\bigoplus_{m=-q}^{q}\mathfrak g_m,\qquad
[h,x]=2m x\quad(x\in\mathfrak g_m),\qquad
\mathfrak g_0=\mathfrak t,\quad
\mathfrak b=\bigoplus_{m\geq0}\mathfrak g_m,\quad
\mathfrak n=\bigoplus_{m\geq1}\mathfrak g_m .
\tag{DS.A4}
\]
Here \(q\) is the largest positive-root height when \(H\ne1\). Brackets add heights. In particular \(E=\operatorname{ad}e\) raises height by one and \(F=\operatorname{ad}f\) lowers it by one. Both are nilpotent on this finite graded vector space.

#### 1.1.2. A constructive finite \(\mathfrak{sl}_2\) decomposition

We need a splitting, not merely a dimension count. The following argument constructs it using only finite linear algebra.

Consider a finite-dimensional vector space \(K\) with operators \(E,F,H_0\) satisfying
\([H_0,E]=2E\), \([H_0,F]=-2F\), and \([E,F]=H_0\). Suppose \(H_0\) is diagonalizable with integer weights and \(E,F\) move between those weight spaces. Finiteness of the weights makes \(E,F\) nilpotent. If \(Ev=0\) and \(H_0v=nv\), the commutator induction gives
\[
H_0F^jv=(n-2j)F^jv,\qquad
EF^jv=j(n-j+1)F^{j-1}v.
\tag{DS.A5}
\]
For the second identity the first step is \(EFv=nv\), and the next step is
\[
EF^{j+1}v=(FE+H_0)F^jv
=\bigl(j(n-j+1)+n-2j\bigr)F^jv
=(j+1)(n-j)F^jv.
\]
If \(a\) is the last index with \(F^av\ne0\), applying this identity at \(a+1\) gives
\(0=(a+1)(n-a)F^av\). Characteristic zero implies \(n=a\geq0\). Its string consequently has exactly \(n+1\) independent vectors, with the displayed coefficients. This reproduces the elementary string argument in [*Representations of \(\mathfrak{sl}_2\)*, §1](../../RT-LIE/src/RT-LIE-05.md); the calculation works over our \(k\).

We now split these strings off without importing complete reducibility. Induct on \(\dim K\). Let \(n\) be its largest weight. Then \(EK[n]=0\), and the preceding argument makes \(n\geq0\). The submodule
\[
W=\bigoplus_{j=0}^{n}F^jK[n]
\tag{DS.A6}
\]
is a direct sum of strings. Each map \(F^j:K[n]\to K[n-2j]\) is injective for \(j\leq n\), since
\[
E^jF^j|_{K[n]}=
j!\,\frac{n!}{(n-j)!}\operatorname{id}.
\]
Different \(j\)'s have different weights, and a basis of \(K[n]\) therefore supplies a string basis of \(W\).

Set
\[
C=H_0^2+2H_0+4FE.
\tag{DS.A7}
\]
This operator commutes with \(E,F,H_0\). For example,
\[
[C,E]=2H_0E+2EH_0+4E-4H_0E=0,
\]
using \(H_0E-EH_0=2E\); the computation with \(F\) is
\(-2H_0F-2FH_0-4F+4FH_0=0\). It acts on an \(n\)-string by \(n(n+2)\), first on its highest vector and then on every \(F\)-iterate.

The quotient \(K/W\) has smaller dimension and has no weight \(n\). By induction it is a direct sum of strings with highest weights \(\mu<n\), all nonnegative. Let \(J\) be the finite set of these highest weights. Define
\[
p(C)=
\prod_{\mu\in J}
\frac{C-\mu(\mu+2)}
{n(n+2)-\mu(\mu+2)}.
\tag{DS.A8}
\]
Every denominator is the nonzero integer \((n-\mu)(n+\mu+2)\). The numerator product annihilates the quotient, so \(p(C)K\subseteq W\); on \(W\), \(p(C)\) is the identity. Hence \(p(C)^2=p(C)\), and
\(K=W\oplus\ker p(C)\) is a module splitting. Projection identifies \(\ker p(C)\) with \(K/W\), whose strings lift through that identification. If the quotient is zero, the empty product is the identity. This finishes the induction and supplies a finite construction of the decomposition.

Apply it to (DS.A4). All \(H_0=\operatorname{ad}h\) weights are even, so the strings have highest weights \(2d\), with \(d\geq0\). Put
\[
V=\ker E,\qquad V_m=V\cap\mathfrak g_m.
\]
The kernel of \(E\) in each string is exactly its highest line, since every interior raising coefficient in (DS.A5) is nonzero. Thus \(V_m=0\) for \(m<0\). On a string, \(F\) maps the height-\((m+1)\) line injectively to the height-\(m\) line whenever \(m\geq0\); the only height-\(m\) line missed is a highest line. Consequently
\[
\mathfrak g_m=F(\mathfrak g_{m+1})\oplus V_m,\qquad
F:\mathfrak g_{m+1}\hookrightarrow\mathfrak g_m
\quad(m\geq0).
\tag{DS.A9}
\]
These are specified direct splittings over \(k\), so tensoring them with any \(k\)-algebra preserves both the direct sum and the injectivity.

There is no height-zero highest line here. Indeed \(\mathfrak g_1\) has basis \(e_i\), and \(F(e_i)=[f,e_i]=-h_i\) is a basis of \(\mathfrak g_0\). Thus \(V_0=0\). Every string contains one zero-weight line, so \(\dim V=\dim\mathfrak t=\ell\). Choose a homogeneous basis \(v_1,\ldots,v_\ell\), and let \(d_j\geq1\) be its heights. They can be computed by the finite kernels of \(E\), or by
\[
\dim V_m=\dim\mathfrak g_m-\dim\mathfrak g_{m+1},\qquad
\sum_j(2d_j+1)=\dim\mathfrak g,\qquad
\sum_jd_j=|\Phi^+|.
\tag{DS.A10}
\]
Thus no assertion about generators of an invariant polynomial algebra is needed for the local slice. Section 1.2 proves that these \(d_j\) are the invariant-theoretic exponents, by constructing homogeneous invariant generators of degrees \(d_j+1\) and their weighted polynomial restriction to the slice.

#### 1.1.3. Finite unipotent gauges over differential rings

Let \((R,\partial)\) be any commutative ordinary \(k\)-algebra with a \(k\)-linear derivation. Nilpotents in \(R\) are allowed. We use the left gauge convention
\[
g\cdot(\partial+A)=g(\partial+A)g^{-1}
=\partial+\operatorname{Ad}(g)A-(\partial g)g^{-1}.
\tag{DS.A11}
\]
The derivative is taken in an algebraic representation, or equivalently on group coordinate functions. The Leibniz rule proves the sign and also proves \((g_2g_1)\cdot D=g_2\cdot(g_1\cdot D)\).

For use on all such rings, we construct the exponential coordinates. In a faithful representation, choose a \(T\)-weight basis ordered by its \(\rho^\vee\)-weights. A positive-root Lie vector strictly raises that weight; therefore every \(x\in\mathfrak n(R)\) is strictly upper triangular, with a uniform nilpotence bound. A root subgroup acts by \(\exp(ae_\alpha)\): differentiating its polynomial additive-group identity gives \(P'(a)=P(a)e_\alpha\), and coefficient comparison gives \(P(a)=\sum_j a^je_\alpha^j/j!\). Root subgroups generate \(N\), so every \(n\in N(R)\) is upper unitriangular in this representation.

The finite matrix polynomials
\[
\exp(x)=\sum_{j\geq0}\frac{x^j}{j!},\qquad
\log(n)=\sum_{j\geq1}\frac{(-1)^{j-1}}j(n-1)^j
\tag{DS.A12}
\]
give inverse bijections \(\mathfrak n(R)\leftrightarrow N(R)\). Two details ensure this is a group-scheme statement, including nonreduced \(R\). First, for the Hopf ideal defining \(N\) inside the matrix group, the invariant derivation determined by \(x\in\operatorname{Lie}N(R)\) preserves that ideal. This follows directly from the comultiplication identity for a Hopf ideal and the fact that the tangent derivation at the identity annihilates it. If \(a\) is in the ideal, the Taylor coefficients of the polynomial \(a(\exp(sx))\) are the evaluations of the iterates of that invariant derivation at the identity, divided by factorials. They all vanish. Hence \(\exp(sx)\in N(R[s])\).

Conversely the matrix polynomial
\[
n^s=\sum_{j\geq0}\binom{s}{j}(n-1)^j
\]
belongs to \(N(R[s])\). For every nonnegative integer \(s\) it is the ordinary group power, so every defining equation vanishes at those integers. A polynomial of finite degree over \(R\) that vanishes there is zero: evaluate at sufficiently many distinct integers and invert their Vandermonde determinant, a nonzero rational integer and hence a unit in \(R\). Its derivative at \(s=0\) is \(\log(n)\), which therefore lies in the tangent space \(\mathfrak n(R)\). Tangent-space base change here is simply base change of linear equations over a field. The inverse identities for (DS.A12) are the usual one-variable formal identities over \(\mathbf Q\), truncated at the uniform matrix nilpotence bound. Thus they are finite polynomial identities.

In particular
\[
\operatorname{BCH}(x,y):=\log(\exp(x)\exp(y))
=x+y+\tfrac12[x,y]
+\tfrac1{12}\bigl([x,[x,y]]+[y,[y,x]]\bigr)+\cdots
\tag{DS.A13}
\]
is a finite polynomial with values in \(\mathfrak n(R)\). Its coefficients are obtained by multiplying the finite exponential polynomials and then the finite logarithm; the displayed signs follow by collecting words of lengths two and three. Every remaining word has higher length. Every nonlinear word involves both \(x\) and \(y\), since substituting either variable by zero gives the other variable exactly. If \(x\) has heights at least \(a\) and \(y\) heights at least \(b\), those nonlinear terms have heights at least \(a+b\). This follows from the ordered representation weights, or from equivariance under \(\rho^\vee\). Thus the formula and its filtration estimate are valid for arbitrary coefficients, with no assumption that those coefficients are themselves nilpotent.

Conjugation and logarithmic differentiation give the precise finite gauge formula
\[
\exp(x)\cdot(\partial+A)
=\partial+
\sum_{j\geq0}\frac{(\operatorname{ad}x)^jA}{j!}
-\sum_{j\geq0}\frac{(\operatorname{ad}x)^j(\partial x)}{(j+1)!}.
\tag{DS.A14}
\]
For the second sum one may differentiate the exponential word by word. Equivalently,

\[
(\partial\exp x)\exp(-x)=\int_0^1\exp(sx)(\partial x)\exp(-sx)\,ds,
\]

where the integral means the algebraic operation \(s^a\mapsto1/(a+1)\) on polynomials. Expanding gives the coefficients in (DS.A14). For the first sum, differentiation with respect to \(s\) of \(\exp(sx)A\exp(-sx)\) gives the adjoint differential equation and its factorial recursion. Nilpotence of the positive-height adjoint action makes both sums finite.

**The local normal-form theorem.** Every operator
\[
D=\partial+f+b,\qquad b\in\mathfrak b\otimes_kR,
\]
has a unique \(N(R)\)-gauge taking it to \(\partial+f+v\), with \(v\in V\otimes_kR\). No slice object has a nonidentity \(N(R)\)-automorphism.

For existence, suppose heights below \(m\) have already been put in \(V\). Decompose the current height-\(m\) coefficient, using (DS.A9), as
\(b_m=F(x_{m+1})+v_m\), with \(x_{m+1}\in\mathfrak g_{m+1}\otimes R\). Gauge by \(\exp(x_{m+1})\). The height-\(m\) term changes by
\([x_{m+1},f]=-F(x_{m+1})\), so it becomes \(v_m\). All other contributions have strictly larger height:
\[
\begin{array}{c|c|c}
\text{term in the gauge formula}&\text{height}&\text{effect at height }m\\ \hline
[x_{m+1},f]&m&-F(x_{m+1})\\
-\partial x_{m+1}&m+1&0\\
[x_{m+1},b_j]\ (j\geq0)&m+1+j&0\\
(\operatorname{ad}x_{m+1})^a f\ (a\geq2)&a(m+1)-1\geq m+1&0
\end{array}
\tag{DS.A15}
\]
The higher derivative commutators have still larger heights. This proves both preservation of all earlier normalizations and the sign of the term removed. Perform the steps \(m=0,\ldots,q-1\). At height \(q\), \(\mathfrak g_{q+1}=0\), so its entire coefficient already lies in \(V_q\). The finite product
\(\exp(x_q)\cdots\exp(x_1)\) is the required gauge.

For uniqueness, suppose \(n\cdot(\partial+f+v)=\partial+f+w\). If \(n\ne1\), let \(a\geq1\) be the smallest nonzero height in \(x=\log n\), and write that component \(x_a\). Formula (DS.A14) shows that the height-\((a-1)\) difference is exactly \(-F(x_a)\): the derivative has height at least \(a\), a bracket with \(v\in\mathfrak b(R)\) has height at least \(a\), and the next bracket with \(f\) has height at least \(2a-1\geq a\). But \(w-v\) has that component in \(V_{a-1}(R)\). The direct sum (DS.A9) therefore makes \(F(x_a)=0\); its injectivity makes \(x_a=0\), a contradiction. Thus \(n=1\) and \(v=w\). Two gauges normalizing an arbitrary \(D\) have a quotient taking one slice object to another, so this also proves uniqueness of the normalizing gauge.

For clarity, exponential coordinates themselves admit a unique height factorization
\[
n=\exp(y_q)\cdots\exp(y_1),\qquad
y_j\in\mathfrak g_j\otimes R.
\tag{DS.A16}
\]
Take \(y_1\) to be the height-one component of \(\log n\). The BCH estimate shows that \(n\exp(-y_1)\) has logarithm of height at least two. Repeat to extract \(y_2\), and continue. The same lowest-height comparison proves uniqueness. This is another finite polynomial construction, not an infinite factorization or a reduced-point argument.

#### 1.1.4. Torus normalization and the coefficient functors

An arbitrary local oper expression in a Borel frame is
\[
D=\partial+\sum_i a_i f_i+b,\qquad
a_i\in R^\times,\quad b\in\mathfrak b(R).
\tag{DS.A17}
\]
The unit condition is the simple-root transversality condition. For the adjoint torus, the simple characters give an isomorphism
\[
T(R)\xrightarrow{\ \sim\ }(R^\times)^\ell,\qquad
t\longmapsto(\alpha_i(t))_i.
\]
Choose its unique point \(t\) with \(\alpha_i(t)=a_i\). Since
\(\operatorname{Ad}(t)f_i=\alpha_i(t)^{-1}f_i\), its gauge changes all negative simple-root coefficients to one. The derivative term is in \(\mathfrak t(R)\):
\[
(\partial t)t^{-1}
=\sum_i\frac{\partial a_i}{a_i}\,\varpi_i^\vee,\qquad
\alpha_j(\varpi_i^\vee)=\delta_{ij}.
\tag{DS.A18}
\]
This follows by applying each character and differentiating; those characters form a basis. The fundamental coweights \(\varpi_i^\vee\) belong to the adjoint cocharacter lattice. Apply the finite unipotent algorithm after this torus step.

This proves, as a functor on ordinary differential \(k\)-algebras,
\[
\left\{\partial+\sum_i a_if_i+b:
a_i\in R^\times,\ b\in\mathfrak b(R)\right\}/B(R)
\ \xrightarrow{\ \sim\ }\ V\otimes_kR.
\tag{DS.A19}
\]
The quotient is a set of isomorphism classes, and its action groupoid has no stabilizers. To see this last assertion, a Borel gauge between two expressions with all \(a_i=1\) has torus part with all simple characters equal to one, hence has torus part \(1\). It lies in \(N(R)\), and the uniqueness theorem applies.

All maps here are natural in homomorphisms of differential algebras. Choose bases for the finite direct splittings (DS.A9). Each induction step applies a fixed \(k\)-linear projection and inverse to \(b_m\), followed by the finite polynomial (DS.A14). Therefore its coefficients and its gauge are differential polynomials in the original coefficients. Their differential orders are bounded by a finite constant depending only on the height bound and the group. The initial torus step also uses the displayed units and their inverses. Gauge multiplication, inversion and the slice reconstruction are polynomial in exponential coordinates. Thus (DS.A19) holds in all ordinary families, including families with nilpotent parameters.

For an ordinary \(k\)-algebra \(A\), take the differential algebras \(A[[t]]\) and \(A((t))=A[[t]][t^{-1}]\), with \(\partial=d/dt\) acting trivially on \(A\). Define the regular and Laurent coefficient oper functors by the framed quotient on the left of (DS.A19) for those rings. The theorem identifies them with
\[
\operatorname{Op}^{\mathrm{coeff}}_{\mathrm{reg}}(A)
=V\otimes_kA[[t]],\qquad
\operatorname{Op}^{\mathrm{coeff}}_{\mathrm{Laur}}(A)
=V\otimes_kA((t)).
\tag{DS.A20}
\]
Every operation is finite in height and uses finitely many derivatives, so it preserves regular coefficients and preserves finite Laurent pole bounds. There is no infinite BCH convergence condition.

In the chosen homogeneous basis, the regular functor is represented by the affine scheme
\(\operatorname{Spec}k[z_{j,n}:1\leq j\leq\ell,\ n\geq0]\): giving a ring map chooses exactly the coefficients of \(\sum_{n\geq0}z_{j,n}t^n\). The Laurent functor is the filtered union, in functors,
\[
\operatorname*{colim}_{M\geq0}
\operatorname{Spec}k[z_{j,n}:1\leq j\leq\ell,\ n\geq-M].
\tag{DS.A21}
\]
The transition is the closed embedding setting the new coefficient at \(n=-M-1\) to zero. Every finite tuple of Laurent series has a common finite pole bound, so the displayed functor is exactly the second functor in (DS.A20). These are coefficient functors in a Borel frame; identifying them with a torsor-based oper definition on arbitrary parameter schemes additionally requires the specified torsor trivialization and effective-descent foundations.

The adjoint qualification in torus normalization is essential. For a central isogeny from a nonadjoint semisimple group, the simple-root map on tori has a central kernel and need not be surjective on \(R\)-points. In \(SL_2\), its simple character on \(\operatorname{diag}(z,z^{-1})\) is \(z^2\), so a unit coefficient requires a square root for this normalization. Such choices and the residual central automorphisms cannot be discarded. A finite central point over a characteristic-zero differential ring has zero derivative: if \(z^n=1\), differentiating and inverting \(nz^{n-1}\) gives \(\partial z=0\). For a reductive group with a positive-dimensional centre, its central connection data also remain; the simple-root oper condition does not measure them. These distinctions preserve the original group problem rather than replacing it by an adjoint quotient.

Everything is compatible with products: the positive roots, triples and height spaces are the direct sums for the simple factors, the unipotent gauges are componentwise, and \(V\) is their direct sum. For the trivial adjoint group all Lie spaces and root sets are zero, \(N=T=1\), and both coefficient functors are the one-point functor.

This local theorem uses no invariant-theory or Kostant slice theorem. Its remaining foundations are the stated algebraic root/group structure and faithful representation, finite vector-space linear algebra, and the affine group-scheme/tangent-space conventions used in the polynomial exponential argument. The identification with invariant degrees, coordinate-change laws, principal \(PGL_2\) integration, global gluing, torsor descent and global oper dimensions require their own arguments. No categorical critical-level, center or localization theorem follows from this classical calculation.

#### 1.1.5. The principal projective group and the coordinate gauge

Continue with the pinning, \((e,h,f)\), height grading and spaces \(V_m=\ker(\operatorname{ad}e)\cap\mathfrak g_m\) constructed above. Let \(\rho^\vee:\mathbb G_m\to T\) be the cocharacter with \(\alpha_i(\rho^\vee(a))=a\) for every simple root. It exists because the simple roots are a basis of the character lattice for the adjoint group. Its differential is \(h/2\), and its adjoint action on \(\mathfrak g_m\) is multiplication by \(a^m\). This specifies a group cocharacter, rather than merely dividing a tangent vector by two.

The constructed finite \(\mathfrak{sl}_2\)-decomposition integrates to an algebraic homomorphism
\[
\iota:PGL_2\longrightarrow H.
\tag{DS.G1}
\]
Here is the integration argument and its group-theoretic boundary. Each string of highest weight \(2m\) is the differential representation on \(\operatorname{Sym}^{2m}(k^2)\): identify its highest vector with \(x^{2m}\) and its successive \(f\)-images with the successive images under \(y\partial_x\). The coefficient identity proved above makes this an isomorphism of Lie representations. Substitution of two linear forms in a homogeneous polynomial gives a regular representation of \(SL_2\) on this symmetric power. Taking the direct sum supplies a regular representation on \(\mathfrak g\) with the prescribed differential. Its upper and lower root subgroups act by \(\exp(t\operatorname{ad}e)\) and \(\exp(t\operatorname{ad}f)\); its diagonal \(\operatorname{diag}(a,a^{-1})\) acts as \(\operatorname{Ad}(\rho^\vee(a^2))\).

The finite unipotent exponential proof applies to the opposite radical too, by reversing the positive-root ordering. These two constructions put \(\exp(te)\), \(\exp(tf)\) and \(\rho^\vee(a^2)\) in \(H\). Thus this representation lands in the faithful closed adjoint copy of \(H\subset GL(\mathfrak g)\) on the open Gaussian-decomposition cell of \(SL_2\). It lands there everywhere: a defining polynomial of that closed copy pulls back to a regular function on the integral scheme \(SL_2\) which vanishes on the dense cell, hence is zero. This is a factorization of scheme morphisms, so it holds over every ordinary coefficient algebra, including nonreduced ones. The central matrix \(-I\) acts trivially on every even symmetric power. Descent through \(SL_2\to PGL_2\) gives (DS.G1); equivalently its two root subgroups and torus have precisely the projective matrix relations in the faithful adjoint representation. They also show uniqueness and independence of the choice of string bases. The faithful closed adjoint embedding, split root subgroups and their unipotent exponential construction are the specified group foundations; they have not been inferred just from a list of Lie brackets.

Now compute a change of curve coordinate in the normal form. Write
\[
\nabla_t=\partial_t+f+w_t,\qquad
w_t=\sum_{m\geq1}w_{t,m},\quad w_{t,m}\in V_m\otimes R.
\tag{DS.G2}
\]
There is no \(V_0\): \(\mathfrak g_0\) is the Cartan of dimension the rank, and \(\mathfrak g_1\) is spanned by the same number of simple-root vectors, so the direct splitting above gives \(\dim V_0=0\). For a coordinate \(s\), set
\(\lambda=\partial_s t\in R^\times\) and \(a=\partial_s\lambda/\lambda\). Derivatives are relative to the parameter base. The first coordinate expression is \(\partial_s+\lambda(f+w_t)\). Gauge it by \(\rho^\vee(\lambda)\). In the convention
\(A\mapsto\operatorname{Ad}(g)A-(\partial_sg)g^{-1}\), this gives
\[
f-\frac a2h+\sum_m\lambda^{m+1}w_{t,m}.
\tag{DS.G3}
\]
Indeed \(f\) has height \(-1\), and the right logarithmic derivative of the cocharacter is \(a h/2\).

Apply next \(\exp(ce)\). The \(\mathfrak{sl}_2\) identities give
\[
\operatorname{Ad}(\exp(ce))f=f+ch-c^2e,
\qquad
\operatorname{Ad}(\exp(ce))h=h-2ce.
\]
Every \(w_{t,m}\) is fixed by this exponential because \([e,w_{t,m}]=0\), and its logarithmic derivative is \(c'e\). Taking \(c=a/2\) kills the Cartan coefficient. The new normal-form vector is consequently
\[
w_s=\sum_m\lambda^{m+1}w_{t,m}
-\frac12\left(\frac{\lambda''}{\lambda}
-\frac32\left(\frac{\lambda'}{\lambda}\right)^2\right)e.
\tag{DS.G4}
\]
All primes here are \(\partial_s\). In the notation \(t=\varphi(s)\), the parentheses are \(\{\varphi,s\}\). For \(H=PGL_2\), write \(w_t=q_t e\); the horizontal equations give the scalar equation \((\partial_t^2-q_t)y=0\), so (DS.G4) has exactly the minus-Schwarzian sign of (O7.2).

The actual Borel transition is
\[
g_{st}=\exp\!\left(\frac{\partial_s\lambda}{2\lambda}e\right)
\rho^\vee(\lambda).
\tag{DS.G5}
\]
These transitions satisfy the cocycle identity as group-valued functions. For a third coordinate \(u\), let \(\mu=\partial_u s\). The total derivative is \(\lambda(\psi(u))\mu\), and its logarithmic derivative is
\(\mu\,a(\psi(u))+\mu'/\mu\). Since conjugation by \(\rho^\vee(\mu)\) multiplies \(e\) by \(\mu\), multiplication of the two exponentials in (DS.G5) adds exactly these two coefficients. The torus factors multiply to the total derivative. This proves the identity, including all ordinary-family coefficients, without a square root of \(\lambda\). The same calculation proves the transformation law for (DS.G4) under consecutive changes. On algebraic coordinate overlaps it uses the derivation and the invertible differential ratio; no analytic expansion of \(t\) as a function of \(s\) is required.

#### 1.1.6. From local frames to the complete oper functor

We explain why the normal form classifies intrinsic opers and their arrows. First use an affine coordinate open \(U\subset X\) and an affine ordinary parameter scheme \(S\). The oper's nowhere-zero simple components give isomorphisms
\[
P_{T}\times^{T}k_{\alpha_i}\simeq\omega_{X_S/S},
\tag{DS.G6}
\]
because the second fundamental component lies in the negative-root line tensored with \(\omega\). The simple characters are a lattice basis, so these isomorphisms determine the torus torsor and its trivialization when \(dt\) is chosen. The fibre of Borel frames inducing that torus frame is an \(N\)-torsor. Thus after normalizing the simple coefficients the only remaining gauge group is \(N\). An arbitrary \(N\)-gauge cannot perform that torus normalization.

This \(N\)-torsor is trivial on the affine coefficient scheme. The following explicit descent argument supplies the needed assertion. For a faithfully flat affine cover \(A\to A'\), the augmented additive Amitsur complex is exact. Tensor it with \(A'\); multiplication of the first two cover factors supplies the extra degeneracy and contracts the augmented complex. Faithful flatness detects its exactness before tensoring, since tensor is exact and faithful. In particular an additive one-cocycle is a coboundary. The finite height filtration of the split \(N\) has successive quotients which are additive vector groups. Write a torsor cocycle in the first such quotient and subtract its additive coboundary by a lifted local group element. The corrected cocycle lies one height deeper. Repeat along the finite filtration; the final cocycle is identity. This gives an \(N\)-frame. A finite affine refinement of a faithfully flat cover suffices here; the affine scheme is quasi-compact and the torsor is locally of finite presentation. The ordinary torsor/descent construction and the split height quotients are the explicit geometric premises of this argument.

Apply the unique gauge normal form to its connection. If another normalized Borel frame is chosen with the same coordinate, its torus factor must satisfy \(\alpha_i(t)=1\) for every simple root. Since the group is adjoint it is identity, including over a nonreduced algebra. Its remaining \(N\)-factor is identity by uniqueness of the normal form. Therefore the vector \(w_t\) and the final frame do not depend on the initial torsor frame. On a coordinate overlap the final frames differ by exactly (DS.G5), since that gauge already takes a normal form to a normal form. Consequently all intrinsic opers have the same Borel transition bundle and vectors with the law (DS.G4).

Conversely, vectors on the coordinate cover satisfying (DS.G4) define a Borel bundle by (DS.G5). Extend its structure group to \(H\), and glue the connections \(\partial_t+f+w_t\) using the verified gauge identity. Their negative simple coefficients are all one, so their Borel reductions satisfy the intrinsic oper condition. The connection is flat because the relative curve has no two-forms. These two constructions are mutually inverse. An automorphism of a normal form has identity torus part and, by the uniqueness theorem, identity unipotent part. Thus the oper groupoid has no residual automorphism for adjoint \(H\); it is the represented ordinary functor, rather than a classification only of geometric isomorphism classes. The construction commutes with every homomorphism of ordinary parameter algebras and hence glues on arbitrary parameter schemes. The assertion would change for a group with a nontrivial center, whose central arrows and connections are not eliminated by the simple roots.

#### 1.1.7. Global affine coordinates, dimension and a repeated exponent

Fix a regular \(PGL_2\)-oper on \(X\), and write its local projective-connection coefficients as \(q_t^0\). Such an oper exists for \(g\geq2\) by the independent scalar construction in §2.7: the normalized second-order operators form a locally nonempty torsor under \(\omega^2\), and (O0.6) gives \(H^1(X,\omega^2)=0\). This construction, its ordinary-family argument and the curve duality/Euler proofs are written in §§2.1–2.7 and retain their specified recursive curve and Picard premises. They do not use the general-group normal form being proved here.

Use \(q_t^0e\) as a reference in (DS.G4). Subtracting it cancels the inhomogeneous term. Thus
\[
w_t=q_t^0e+v_t,\qquad
(v_s)_m=\lambda^{m+1}(v_t)_m.
\tag{DS.G7}
\]
The transformed differential \((dt)^{m+1}\) equals \(\lambda^{m+1}(ds)^{m+1}\). Hence these are precisely the coefficients of sections of
\[
\mathcal V=\bigoplus_{m\geq1}V_m\otimes_k\omega^{m+1}.
\tag{DS.G8}
\]
Conversely every section supplies vectors in (DS.G7) and therefore the complete intrinsic oper of §1.1.6. There are finitely many nonzero \(V_m\). For \(S=\operatorname{Spec}A\), the fixed-curve section complex tensored with \(A\), as proved in §2.1 from the earlier curve construction, gives
\[
\operatorname{Op}_H(X)(A)
\simeq q^0e+H^0(X,\mathcal V)\otimes_k A.
\tag{DS.G9}
\]
Over a field all complexes split into cohomology and contractible terms, so this tensor comparison retains arbitrary nilpotent coefficients in \(A\); it is not merely a tangent calculation. Descent gives the same assertion on every ordinary scheme. Therefore a reference projective connection and the pinning identify the entire oper functor with the affine space on
\[
\bigoplus_{m\geq1}V_m\otimes_k H^0(X,\omega^{m+1}).
\tag{DS.G10}
\]
Changing the reference projective connection translates this affine space by its quadratic-differential difference multiplied by \(e\). It does not make a preferred origin.

Define the principal exponents \(d_j\), with multiplicity, by writing the proved adjoint decomposition as a direct sum of strings of highest weights \(2d_j\). Equivalently \(d_j=m\) occurs \(\dim V_m\) times. The zero weight of each such string is one-dimensional. Since \(\mathfrak g_0\) is the Cartan, there are exactly \(\operatorname{rank}H\) strings. Formula (DS.G10) is the vector-space form of (A8.2). Section 1.2 proves that \(d_j+1\) are the basic degrees of the invariant ring, through the Molien degree sum and the weighted Jacobian argument, and constructs the corresponding Hitchin-base comparison.

By (O0.6), all \(m\geq1\) give
\(h^0(\omega^{m+1})=(2m+1)(g-1)\). Taking dimensions in the finite string decomposition gives
\[
\boxed{\dim\operatorname{Op}_H(X)
=\sum_m(2m+1)\dim V_m\,(g-1)
=\dim H\,(g-1).}
\tag{DS.G11}
\]
This is proved for every adjoint semisimple group, including products. For the trivial group both sums are empty and the oper functor is a point.

For \(H=PGL_n\), \(n\geq2\), the positive root spaces are the matrix lines \(kE_{ij}\), \(i<j\): commutation with a diagonal matrix gives the character \(e_i-e_j\). Its simple-root expansion is \(\alpha_i+\cdots+\alpha_{j-1}\), so its height is \(j-i\). There are \(n-m\) pairs of height \(m\), for \(1\leq m\leq n-1\). Formula (DS.A9) consequently gives \(\dim V_m=1\) at every such height and zero above. This proves the principal exponent list \(1,\ldots,n-1\) and recovers the scalar dimensions in §2.7 without identifying the raw scalar coefficients with the slice coordinates.

For a concrete multiplicity check take the root system \(D_4\), whose roots are \(\pm e_i\pm e_j\), \(i<j\), with simple roots
\(\alpha_1=e_1-e_2\), \(\alpha_2=e_2-e_3\),
\(\alpha_3=e_3-e_4\), \(\alpha_4=e_3+e_4\).
Choose the positive roots \(e_i-e_j\) and \(e_i+e_j\), \(i<j\). The following table lists all twelve and their simple-root expansions. Each height is the sum of the coefficients in its expansion:

| Height | Positive roots | Expansions in the same order |
| --- | --- | --- |
| 1 | \(e_1-e_2,\ e_2-e_3,\ e_3-e_4,\ e_3+e_4\) | \(\alpha_1,\ \alpha_2,\ \alpha_3,\ \alpha_4\) |
| 2 | \(e_1-e_3,\ e_2-e_4,\ e_2+e_4\) | \(\alpha_1+\alpha_2,\ \alpha_2+\alpha_3,\ \alpha_2+\alpha_4\) |
| 3 | \(e_1-e_4,\ e_2+e_3,\ e_1+e_4\) | \(\alpha_1+\alpha_2+\alpha_3,\ \alpha_2+\alpha_3+\alpha_4,\ \alpha_1+\alpha_2+\alpha_4\) |
| 4 | \(e_1+e_3\) | \(\alpha_1+\alpha_2+\alpha_3+\alpha_4\) |
| 5 | \(e_1+e_2\) | \(\alpha_1+2\alpha_2+\alpha_3+\alpha_4\) |

Each height is checked by expanding in the displayed simple roots; for example \(e_1+e_2=\alpha_1+2\alpha_2+\alpha_3+\alpha_4\). The direct splitting gives
\(\dim V_m=\dim\mathfrak g_m-\dim\mathfrak g_{m+1}\).
The height counts \(4,3,3,1,1\) therefore give principal exponents
\(1,3,3,5\). After choosing bases of the corresponding \(V_m\), the global vector space is
\[
H^0(\omega^2)\oplus H^0(\omega^4)^{\oplus2}\oplus H^0(\omega^6),
\quad
\dim=(3+7+7+11)(g-1)=28(g-1).
\tag{DS.G12}
\]
Both quartic summands are needed. This calculation uses the stated \(D_4\) root system, not a claim that a repeated exponent can be discarded.

#### 1.1.8. Disc coefficients, Laurent coefficients and the exact boundary

For a fixed formal coordinate \(t\), a disc connection here is a continuous relative connection, with differential module \(A[[t]]\,dt\); its punctured version uses \(A((t))\,dt\). Thus the coordinate expression uses \(\partial_t\), without replacing continuous differentials by an unrestricted algebraic Kähler-differential module. Apply the same finite polynomial gauge construction to the differential algebra \(A[[t]]\). It gives the regular coefficient functor
\[
\operatorname{Op}_H(D)(A)
=\bigoplus_{m\geq1}V_m\otimes_k A[[t]].
\tag{DS.G13}
\]
Only the finite sum over the spaces \(V_m\) is meant here. Each power series has arbitrary infinitely many coefficients. In particular \(A[[t]]\) means the completed power-series ring, and is not replaced by the ordinary tensor product \(A\otimes_k k[[t]]\), which need not contain all coefficient sequences. Coefficient-algebra maps act termwise on these series. Choose bases of those finite-dimensional spaces and introduce variables \(z_{m,b,n}\), \(n\geq0\), for these coefficients. Homomorphisms from the ordinary polynomial algebra
\(k[z_{m,b,n}:n\geq0]\) to \(A\) are exactly these arbitrary coefficient families. Thus the functor in (DS.G13) is represented by its infinite-dimensional affine scheme. This assertion concerns the ordinary coefficient functor and the torsor normal-form/descent construction above; a derived oper construction is an additional assertion.

For the punctured disc use \(A((t))=A[[t]][t^{-1}]\). The gauge calculations use finitely many algebra operations and derivatives, so preserve Laurent series with finite negative part. They give
\[
\operatorname{Op}_H(D^\times)(A)
=\bigoplus_m V_m\otimes_k A((t)).
\tag{DS.G14}
\]
The right side is the union over \(L\geq0\) of the coefficient functors in which all exponents are at least \(-L\); there are finitely many \(V_m\), so a common bound exists for each object. Each stage is an affine scheme with variables for indices \(n\geq-L\). The inclusion of stage \(L\) in stage \(L+1\) is the closed inclusion setting its new negative coefficients to zero. Their filtered colimit represents this ordinary Laurent coefficient functor as an ind-affine scheme. It permits arbitrarily large pole order, rather than silently imposing a uniform bound on all objects.

Every pointed coordinate change \(t=\varphi(s)\in sA[[s]]\) with invertible linear coefficient acts by (DS.G4)–(DS.G5). Substitution is defined coefficient by coefficient; the coefficient of \(s^n\) in a power-series substitution uses finitely many terms. The linear unit gives an inverse series by recursive coefficient solution, and makes Laurent substitution well defined. The chain and group cocycle identities already proved make this a natural action on the coefficient functors.

For the full continuous coordinate group, allow \(\varphi(s)=a_0+a_1s+\cdots\), where \(a_0^N=0\) and \(a_1\) is a unit. The coefficient of \(s^n\) in \(\varphi(s)^j\) vanishes for \(j\geq n+N\): a contributing product must use at least \(j-n\) constant factors. Thus every coefficient of a substituted power series is still a finite sum. Write \(I=(a_0)\), so \(I^N=0\). The inverse coordinate can also be constructed in finitely many steps before the pointed recursion. Starting at \(r=0\), apply
\[
r\longmapsto r-\frac{\varphi(r)}{\varphi'(r)}.
\]
Evaluation at \(r\in I\) is a finite sum, and \(\varphi'(r)\) is a unit since it is \(a_1\) modulo \(I\). Taylor expansion shows that an error in \(I^d\) becomes an error in \(I^{2d}\). After finitely many iterations this supplies a root \(r\in I\) with \(\varphi(r)=0\). It is unique in \(I\), because \(\varphi(r)-\varphi(r')\) is \((r-r')\) times a unit. The translated series \(\varphi(u+r)\) has zero constant coefficient and unit linear coefficient. Its pointed inverse \(u=\psi(t)\) therefore gives the two-sided continuous inverse \(s=r+\psi(t)\).

Laurent substitution is defined as well. Put \(p(s)=\varphi(s)-a_0=s\,v(s)\), with \(v(s)\) a unit. In \(A((s))\),
\[
\varphi(s)^{-1}=\sum_{j=0}^{N-1}(-a_0)^j p(s)^{-j-1}.
\]
This is a Laurent series with finite negative part; multiplying by \(p+a_0\) checks the formula directly. Substituting a Laurent series now combines this finite inverse with the coefficient-finite power-series substitution. Termwise differentiation obeys the chain rule, so (DS.G4)–(DS.G5) still define the action.

These conditions describe the entire continuous coordinate group. Continuity of a substitution forces \(\varphi(s)^M\in(s)\) for some \(M\), so its constant coefficient satisfies \(a_0^M=0\). If \(\psi\) is the inverse substitution, differentiation of \(\psi(\varphi(s))=s\) at zero gives \(\psi'(a_0)a_1=1\), making \(a_1\) a unit. A continuous homomorphism is determined by its values on the dense polynomial subring, hence by this substitution. In the convention of Beilinson–Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, §2.6.5, this group is \(\operatorname{Aut}\mathcal O\), and the pointed subgroup is \(\operatorname{Aut}^{0}\mathcal O\). The two actions are specified separately; nilpotent translations belong to the former. Infinitesimally a coordinate is \(s+\epsilon v(s)\), \(\epsilon^2=0\), and its action on a series \(F\) is \(F+\epsilon vF'\). Thus the full Lie algebra is \(A[[s]]\partial_s\), while the pointed one is \(sA[[s]]\partial_s\).

The results prove the full adjoint classical normal form, coordinate gluing, global affine parameter space and its ordinary-family dimension. The recursive root-space/pinning, split-unipotent, faithful adjoint-group and ordinary bundle-descent constructions remain the explicitly named Lie/group premises, and the curve cohomology and projective-connection construction retain the earlier exact foundations. Section 1.2 supplies the invariant-degree comparison for the principal exponents at the earlier Serre/highest-weight and finite-algebra foundations. Full derived opers, central connections for nonadjoint reductive groups, and the Feigin–Frenkel, Beilinson–Drinfeld and fundamental local equivalence theorems remain additional mathematical obligations.


### 1.2. Polynomial invariants and the Kostant section

#### 1.2.1. Restriction and polynomial generators over the actual field

Continue with the pinned adjoint semisimple group \(H\), its Lie algebra \(\mathfrak g\), Cartan \(\mathfrak t\), and Weyl group \(W\). We first establish the invariant-ring input over the given algebraically closed characteristic-zero field \(k\):
\[
k[\mathfrak g]^H\xrightarrow{\ \sim\ }k[\mathfrak t]^W,
\qquad
k[\mathfrak g]^H=k[p_1,\ldots,p_\ell],
\quad \deg p_i=D_i>0.
\tag{IS.F1}
\]
The \(p_i\) are homogeneous and algebraically independent. Their degrees will be compared with the principal heights by the argument below.

The earlier [*The isomorphism theorem and Serre's theorem*](../../RT-LIE/src/RT-LIE-11.md), §§1–6.3, constructs the rational Serre algebra \(\mathfrak g_{\mathbb Q}(A)\) for the finite Cartan matrix. Corollary 6.3 proves that its presentation commutes with field extension, has the prescribed one-dimensional root spaces and has dimension \(\ell+|\Phi|\). Here is why it gives the rational form of this particular pinned Lie algebra. Its generators map to the chosen \(e_i,f_i,h_i\). The Cartan, cross-root and Serre relations follow from the root-string/pinning premises of §1.1.1. These generators span every root space: for a positive nonsimple root \(\beta\), choose a simple root \(\alpha_i\) with \((\beta,\alpha_i)>0\). The root string gives a positive root \(\beta-\alpha_i\) of smaller height, and its bracket with \(e_i\) is nonzero in the one-dimensional \(\beta\)-space. Induction generates every positive root space; the opposite base does the same for the negative spaces. The brackets \([e_i,f_i]\) give the Cartan basis. The resulting map is surjective, and both dimensions are \(\ell+|\Phi|\); it is therefore the pinned isomorphism
\[
\mathfrak g_{\mathbb Q}(A)\otimes_{\mathbb Q}k
\simeq\mathfrak g.
\tag{IS.F2}
\]
The recursive root-space and root-string construction from the algebraic group remains the explicit structural premise. The rational Serre presentation and its field-extension argument themselves are supplied by the earlier lesson.

Write \(\mathfrak g_{\mathbb Q}\) and \(\mathfrak t_{\mathbb Q}\) for these rational spaces. Each Weyl reflection on the Cartan is the rational matrix
\(s_i(x)=x-\alpha_i(x)h_i\). In polynomial degree \(d\), infinitesimal invariants are the kernel of a finite rational linear map
\[
L_d:\operatorname{Sym}^d(\mathfrak g_{\mathbb Q}^*)
\longrightarrow
\bigoplus_a\operatorname{Sym}^d(\mathfrak g_{\mathbb Q}^*),
\qquad F\longmapsto (x_a\cdot F)_a,
\tag{IS.F3}
\]
where the \(x_a\) form a rational Lie basis. Weyl invariants are likewise the kernel of the finite family of maps \(w-1\) on \(\operatorname{Sym}^d(\mathfrak t_{\mathbb Q}^*)\). Tensoring these finite linear maps with a field is exact, so both kernels commute with extension of scalars. Restriction is a rational map between them.

The earlier [*The centre of the enveloping algebra and Harish-Chandra's theorem*](../../RT-LIE/src/RT-LIE-15.md), Theorem 3.1, proves complex Chevalley restriction. Its proof establishes root-exponential invariance, uses an invertible differential of the root-conjugation map for injectivity, and lifts orbit-power sums by traces of finite-dimensional highest-weight representations for surjectivity. Its §§9.1–9.7 prove polynomiality of the Weyl-invariant ring through invariant fundamental characters, completion at the identity, and homogeneous generators. These are the matching polynomial statements, rather than the enveloping-algebra conclusion. Applied to \(\mathfrak g_{\mathbb Q}\otimes\mathbb C\), restriction in each degree is an isomorphism. Its rational kernel and cokernel vanish after tensoring with \(\mathbb C\), hence vanish: a nonzero rational vector stays nonzero after extension of a basis. Tensoring this rational isomorphism with \(k\) proves the restriction part of (IS.F1) for Lie invariants.

Polynomiality also descends, with no chosen complex generators assumed rational. Put
\(B_{\mathbb Q}=\mathbb Q[\mathfrak t_{\mathbb Q}]^W\),
\(J=\bigoplus_{d>0}(B_{\mathbb Q})_d\).
Every graded piece is finite-dimensional. Formation of \(J/J^2\) commutes with field extension: in degree \(d\), the square is the image of the finite sum of multiplication maps with positive degrees adding to \(d\). For a polynomial ring on homogeneous generators, this quotient has their classes as a basis. Thus the complex polynomiality proof gives
\[
\dim_{\mathbb Q}J/J^2=\ell,
\qquad
(J/J^2)_d=0\text{ outside finitely many positive degrees}.
\tag{IS.F4}
\]
Choose a homogeneous rational basis of this quotient and homogeneous lifts \(q_1,\ldots,q_\ell\) in \(B_{\mathbb Q}\). They generate the ring. Indeed in degree \(d>0\), subtract the linear combination of lifts matching the indecomposable class. The remainder is a finite sum of products of strictly smaller positive degrees, each already generated by induction. Degree zero consists of rational constants.

They are algebraically independent as well. Their degrees are exactly the complex polynomial-generator degrees, with multiplicity, since those degrees are measured by \(J/J^2\). The graded surjection
\(\mathbb Q[z_1,\ldots,z_\ell]\to B_{\mathbb Q}\), \(z_i\mapsto q_i\), after complex scalar extension has equal finite dimensions in every degree: both Hilbert series are \(\prod_i(1-t^{D_i})^{-1}\). Its degreewise kernels vanish, hence its rational kernel vanishes. This proves
\[
B_{\mathbb Q}=\mathbb Q[q_1,\ldots,q_\ell],
\qquad k[\mathfrak t]^W=k[q_1,\ldots,q_\ell].
\tag{IS.F5}
\]
The inverse rational restriction map lifts each \(q_i\) to a homogeneous rational \(p_i\). Extending to \(k\) proves polynomiality for the Lie-invariant ring. All of this uses scalar extension through \(\mathbb Q\); the field \(k\) requires no chosen embedding into \(\mathbb C\).

Finally Lie invariance agrees with group invariance here. If \(F\) is killed by every Lie derivative, a root subgroup \(\exp(te_\alpha)\) fixes it: differentiation of \(F(\operatorname{Ad}(\exp(te_\alpha))X)\) gives zero, and a polynomial in \(t\) with zero derivative is constant in characteristic zero. A torus weight component killed by every Cartan derivative has weight zero, since a nonzero integral character has a nonzero differential in characteristic zero. Thus the torus fixes \(F\) too. For completeness one can check that these identities force invariance on the whole connected group without a pointwise generation assumption. For fixed \(X\), the orbit function \(a\mapsto F(\operatorname{Ad}(a)X)\) on \(H\) has zero derivative in every left-invariant tangent direction, by Lie invariance at \(\operatorname{Ad}(a)X\). Such directions span each tangent space. A rational function on an integral finite-type variety over an algebraically closed characteristic-zero field with differential zero is constant: if it were transcendental, include it in a transcendence basis of the function field; the finite algebraic remainder is separable, and its differential would be a nonzero basis element. An algebraic function-field element over \(k\) lies in \(k\). Hence this orbit function is constant. Connected smooth \(H\) is integral; its irreducible components are disjoint because its regular local rings are domains, so connectedness leaves one. These smooth/group and regular-local facts retain the structural foundations already specified. Evaluation at the identity gives the required group invariance, as a polynomial identity in \(X\) and group coordinates. The converse follows by differentiation. This finishes (IS.F1).

The assertion persists over every ordinary \(k\)-algebra \(R\), including nonreduced ones. Group invariants mean the kernel of the algebraic coaction difference \(F\mapsto\operatorname{coact}(F)-F\otimes1\), rather than invariance only under the points \(H(R)\). In each homogeneous degree its domain is finite-dimensional, and its coefficient image lies in a finite-dimensional part of the coaction target. Tensor with \(R\) is exact because \(k\) is a field, so
\[
R[\mathfrak g_R]^{H_R}
=R\otimes_k k[\mathfrak g]^H
=R[p_1,\ldots,p_\ell],
\quad
R[\mathfrak t_R]^W=R\otimes_k k[\mathfrak t]^W,
\tag{IS.F6}
\]
and restriction remains an isomorphism. Products are componentwise; for the trivial group both rings are the coefficient ring and the generator list is empty.

#### 1.2.2. Molien's formula and the two degree identities

Continue with the pinned adjoint semisimple \(H\) over an algebraically closed characteristic-zero field \(k\), its Cartan \(\mathfrak t\), Weyl group \(W\), principal triple \((e,h,f)\), and \(V=\ker(\operatorname{ad}e)\). Put \(\ell=\dim\mathfrak t\). The input from §1.2.1 is precisely a graded presentation
\[
k[\mathfrak g]^H\xrightarrow{\ \sim\ }k[\mathfrak t]^W
=k[P_1,\ldots,P_\ell],\qquad \deg P_i=D_i>0,
\tag{IS.A1}
\]
where the generators are algebraically independent and are also denoted \(P_i\) on \(\mathfrak g\). Here invariance means invariance of the algebraic group coaction. The complete complex-field restriction and polynomiality arguments are [*The centre of the enveloping algebra and Harish-Chandra's theorem*, Theorems 3.1 and 9.1](../../RT-LIE/src/RT-LIE-15.md). The algebraic root/group and characteristic-zero transport premises specified in §1.2.1 are retained; a complex-field theorem is not silently substituted for that transport. We prove the degree comparison and slice restriction from this exact presentation, without a generator-degree classification.

First determine which elements of \(W\) are linear reflections. The root datum supplies its rational reflection representation, whose scalar extensions give the real Euclidean root space and the action on \(\mathfrak t^*\). In a simple-root basis the matrices have integer entries. Ranks of their fixed-space equations are therefore the same over \(\mathbf Q\), \(\mathbf R\), and \(k\).

A nonidentity real orthogonal element with a fixed hyperplane acts by \(-1\) on its perpendicular line, so it is the orthogonal reflection in that hyperplane. Its hyperplane must be a root hyperplane. Otherwise choose a point on it avoiding all root hyperplanes: their finitely many proper intersections cannot cover it. In rank one there is only the hyperplane \(\{0\}\), which is already the root hyperplane. In higher rank the avoidance assertion follows by taking the product of the finitely many nonzero restricted linear equations; a nonzero real polynomial cannot vanish everywhere.

Such an avoided point lies inside a Weyl chamber. An element fixing it preserves that chamber, because it permutes the root-hyperplane arrangement. The chamber stabilizer is trivial by [*Root systems and their Weyl groups*, §3 and Theorem 5.1](../../RT-LIE/src/RT-LIE-08.md). The proof there joins chambers through single-wall crossings, while the root-sign length formula forces a chamber-preserving element to have length zero. Thus our alleged nonidentity reflection would be the identity, a contradiction. Its fixed hyperplane is consequently \(\alpha^\perp\) for a root, and uniqueness of orthogonal reflection gives \(s_\alpha\). Conversely every \(s_\alpha\) is a reflection. Reducedness identifies precisely the pair \(\alpha,-\alpha\) on each root line, so the number of reflections is
\[
r_{\mathrm{ref}}=|\Phi|/2=|\Phi^+|.
\tag{IS.A2}
\]

Now consider the homogeneous degree-\(n\) space \(\operatorname{Sym}^n(\mathfrak t^*)\). Its Reynolds operator is
\[
\mathcal R_n=\frac1{|W|}\sum_{w\in W}w.
\]
It is idempotent, has image the invariants, and its trace is the dimension of that image: choose a basis of its image and kernel, on which it is respectively identity and zero. Every \(w\) is diagonalizable over \(k\), since its finite order makes its minimal polynomial divide a separable polynomial \(X^a-1\). If its eigenvalues on \(\mathfrak t^*\) are \(\lambda_1,\ldots,\lambda_\ell\), the monomial basis gives
\[
\sum_{n\geq0}\operatorname{Tr}\!\left(w\mid\operatorname{Sym}^n\mathfrak t^*\right)t^n
=\prod_{j=1}^{\ell}\left(\sum_{a\geq0}(\lambda_jt)^a\right)
=\frac1{\det(1-tw\mid\mathfrak t^*)}.
\]
Averaging this identity proves Molien's formula, including its coefficients:
\[
\operatorname{Hilb}\bigl(k[\mathfrak t]^W,t\bigr)
=\frac1{|W|}\sum_{w\in W}\frac1{\det(1-tw)}
=\prod_{i=1}^{\ell}(1-t^{D_i})^{-1}.
\tag{IS.A3}
\]
The second equality follows from the monomial basis in the polynomial presentation (IS.A1).

Assume \(\ell>0\), put \(s=1-t\), and expand these rational functions as formal Laurent series in \(s\). The identity element contributes \(s^{-\ell}\). A reflection contributes
\[
\frac1{(1-t)^{\ell-1}(1+t)}
=\tfrac12s^{1-\ell}+O(s^{2-\ell}).
\]
Every other element fixes a space of dimension at most \(\ell-2\); its denominator therefore gives a pole of order at most \(\ell-2\). Thus the first two coefficients in the group average are
\[
\frac1{|W|}s^{-\ell}
+\frac{r_{\mathrm{ref}}}{2|W|}s^{1-\ell}
+O(s^{2-\ell}).
\tag{IS.A4}
\]
For \(\ell=1\) the remaining group-element sum is empty, and the same expansion holds. On the polynomial side,
\[
1-(1-s)^D=Ds\left(1-\frac{D-1}{2}s+O(s^2)\right),
\]
so its expansion is
\[
\frac1{\prod_iD_i}s^{-\ell}
\left(1+\frac12\sum_i(D_i-1)s+O(s^2)\right).
\]
These are formal algebraic expansions, requiring no analytic limit. Comparing their two coefficients gives
\[
\prod_iD_i=|W|,\qquad
\sum_i(D_i-1)=r_{\mathrm{ref}}=|\Phi^+|.
\tag{IS.A5}
\]

#### 1.2.3. Dominance of the principal slice

Choose the homogeneous basis \(v_1,\ldots,v_\ell\) of \(V\) constructed in §1.1.2, with heights \(d_j\geq1\), and put
\[
\Sigma=f+V,\qquad
x=f+\sum_j z_jv_j,\qquad w_j=d_j+1.
\]
On each constructed \(\mathfrak{sl}_2\) string, \(\operatorname{ad}f\) maps every vector except its lowest vector to the next vector, and its image misses exactly the highest line. Taking the sum of those strings gives the full splitting
\[
\mathfrak g=[f,\mathfrak g]\oplus V,\qquad
\dim V=\ell,\qquad
\sum_j d_j=|\Phi^+|.
\tag{IS.A6}
\]
This is the whole-module consequence of the written string decomposition, not an assertion of a new slice theorem.

The adjoint torus cocharacter \(\rho^\vee\) acts on height \(m\) by \(a^m\). Hence the action
\[
a\star x=a\,\operatorname{Ad}(\rho^\vee(a))x
\tag{IS.A7}
\]
fixes \(f\), preserves \(\Sigma\), and sends \(z_j\) to \(a^{w_j}z_j\). All \(w_j\) are strictly positive. Ordinary degree-\(D_i\) homogeneity and adjoint invariance give
\(P_i(a\star x)=a^{D_i}P_i(x)\). Therefore \(p_i(z):=P_i(f+\sum_jz_jv_j)\) is weighted homogeneous of degree \(D_i\).

Consider
\[
\mu:H\times\Sigma\longrightarrow\mathfrak g,\qquad
(g,x)\longmapsto\operatorname{Ad}(g)x .
\]
Its differential at \((1,f)\) is
\[
(X,v)\longmapsto[X,f]+v,
\tag{IS.A8}
\]
which is surjective by (IS.A6). We give the polynomial consequence explicitly.

Take one parameter for every positive and negative root subgroup, and torus parameters \(u_i\) through the cocharacter points \(\varpi_i^\vee(1+u_i)\), on the open set where \(1+u_i\ne0\). A product of these root-subgroup and torus maps is a regular map to \(H\) whose differential at zero spans the root vectors and a basis of \(\mathfrak t\). Append the \(\ell\) coordinates of \(\Sigma\). The composed map to \(\mathfrak g\) consequently has the surjective differential (IS.A8). By finite linear algebra choose \(\dim\mathfrak g\) linear combinations of these parameter directions on which that differential is an isomorphism. Restrict to that linear parameter space and to the open set containing zero where the torus denominators remain invertible. Denote the resulting map by \(\Psi\). In its formal coordinates \(q\) at zero,
\[
\Psi(q)=f+Aq+\text{terms of total degree at least two},
\qquad A\text{ invertible}.
\]
If a nonzero polynomial \(F\) on \(\mathfrak g\) vanished after this substitution, take the lowest nonzero homogeneous term \(F_b(Y)\) of \(F(f+Y)\). Its substituted lowest term would be \(F_b(Aq)\), which is nonzero by invertible linear substitution. This contradicts the assumed vanishing. The expansions of the torus denominators exist formally because their constant terms are one. Thus no nonzero polynomial vanishes on \(\mu\)'s image: \(\mu\) is dominant. This argument supplies the density directly.

Let \(\chi:\mathfrak g\to\operatorname{Spec}k[P_1,\ldots,P_\ell]\) be the invariant map. It is dominant because the polynomial presentation embeds in \(k[\mathfrak g]\). Moreover \(\chi\mu=\chi|_\Sigma\operatorname{pr}_\Sigma\). If \(Q(p_1,\ldots,p_\ell)=0\), the invariant polynomial \(Q(P_1,\ldots,P_\ell)\) therefore vanishes after \(\mu\), hence is zero by the preceding argument. Algebraic independence in (IS.A1) makes \(Q=0\). We have proved
\[
p_1,\ldots,p_\ell\text{ are algebraically independent},\qquad
\chi|_\Sigma\text{ is dominant}.
\tag{IS.A9}
\]

#### 1.2.4. The constant Jacobian and a finite polynomial inverse

We first justify why (IS.A9) gives a nonzero Jacobian in characteristic zero. Put \(L=k(z_1,\ldots,z_\ell)\) and \(K=k(p_1,\ldots,p_\ell)\). Each \(z_j\) is algebraic over \(K\). Indeed \(\ell+1\) rational functions in \(\ell\) variables are algebraically dependent: clear a common denominator for all monomials of total degree at most \(N\). Their numerators then have degree at most \(cN\) for a fixed \(c\); there are \(\binom{N+\ell+1}{\ell+1}\) such monomials but only \(\binom{cN+\ell}{\ell}\) possible numerator monomials. For sufficiently large \(N\), linear dependence gives a polynomial relation. If \(z_j\) were transcendental over \(K\), the independence of the \(p_i\) would make \(p_1,\ldots,p_\ell,z_j\) independent, contradicting this count.

Take the irreducible polynomial of \(z_j\) over \(K\). Its derivative does not vanish at \(z_j\): characteristic zero makes the derivative nonzero, and irreducibility prevents a common factor with the original polynomial. In the free \(L\)-space with basis \(dz_1,\ldots,dz_\ell\), differentiate its identity using the polynomial product rule and rational quotient rule. Its coefficients are rational functions of the \(p_i\), so their differentials are combinations of \(dp_i\). The nonzero derivative coefficient consequently expresses \(dz_j\) as an \(L\)-linear combination of the \(dp_i\). This holds for every \(j\). The \(\ell\) differentials \(dp_i\) thus span this \(\ell\)-dimensional space, and
\[
J(z):=\det\left(\frac{\partial p_i}{\partial z_j}\right)\ne0.
\tag{IS.A10}
\]
This is a field and polynomial argument; no smooth-image assertion is used.

Each matrix entry in (IS.A10) has weighted degree \(D_i-w_j\), if it is nonzero. Every determinant term has weighted degree \(\sum_iD_i-\sum_jw_j\). Formulas (IS.A5) and (IS.A6) give
\[
\sum_iD_i=\ell+|\Phi^+|
=\sum_j(d_j+1)=\sum_jw_j .
\]
Thus \(J\) has weighted degree zero. Positive weights leave only constants in degree zero, so \(J=c\in k^\times\).

In particular the differential matrix at \(z=0\) is invertible. A linear term \(z_j\) can occur in \(p_i\) only when \(D_i=w_j\). A nonzero determinant term of that linear matrix therefore pairs each row degree with an equal column weight. This proves, with multiplicities,
\[
\{D_1,\ldots,D_\ell\}=\{d_1+1,\ldots,d_\ell+1\}.
\tag{IS.A11}
\]
For \(\ell>0\), reorder both lists by their distinct increasing weights \(a_1<\cdots<a_s\), grouping repeated weights into blocks. Write \(z_a\) and \(y_a\) for those coordinate blocks. Weighted homogeneity gives the triangular form
\[
\begin{array}{c|c|c}
\text{weight block}&\text{forward polynomial}&\text{inputs of the lower term}\\ \hline
a_1&y_{a_1}=L_{a_1}z_{a_1}&\text{none}\\
a_i\ (2\leq i\leq s)&y_{a_i}=L_{a_i}z_{a_i}+Q_{a_i}(z_{<a_i})&
z_{a_1},\ldots,z_{a_{i-1}}
\end{array}
\tag{IS.A12}
\]
Each square block \(L_a\) is invertible, because their block-diagonal union is the invertible linear differential. To verify the displayed dependence, any nonlinear monomial of weight \(a\) uses at least two variables of positive weight, so every variable in it has weight strictly less than \(a\). A variable of weight greater than \(a\) cannot occur at all; a variable of weight \(a\) can occur only linearly. Positive-degree homogeneity also excludes constant terms.

Solve the blocks successively:
\[
z_a=L_a^{-1}\bigl(y_a-Q_a(z_{<a})\bigr).
\tag{IS.A13}
\]
At the first block \(Q_{a_1}=0\). After each earlier block has been substituted, the next expression is a polynomial in the \(y\)'s. There are finitely many weights, so this constructs a polynomial inverse. Induction through the blocks verifies both compositions are the identity: the first block is recovered by its invertible linear map, and each subsequent block is recovered after its already recovered lower blocks are substituted.

*In (IS.A12), each row introduces just one new weight block. Its lower terms use only earlier blocks; (IS.A13) therefore solves the entire map by a finite succession of explicit linear inverses and polynomial substitutions.*

We have proved the principal-slice restriction isomorphism
\[
\operatorname{res}_\Sigma:k[\mathfrak g]^H
\xrightarrow{\ \sim\ }k[\Sigma]=k[z_1,\ldots,z_\ell],
\qquad P_i\longmapsto p_i.
\tag{IS.A14}
\]
This proves both the invariant-degree comparison and the slice assertion. The inverse is supplied by the positive-weight blocks themselves.

#### 1.2.5. Ordinary base change, products and the exact foundations

For any ordinary commutative \(k\)-algebra \(A\), form
\(\mathfrak g_A=\mathfrak g\otimes_kA\), \(H_A\), and
\(\Sigma_A=f_A+V_A\). Both maps in the inverse construction are polynomials over \(k\), and their composition identities are polynomial identities. Tensoring them with \(A\) therefore preserves (IS.A14), including over nonreduced \(A\).

There is also no ambiguity about relative group invariants. If
\(\delta:k[\mathfrak g]\to k[\mathfrak g]\otimes_k k[H]\)
is the action coaction, the invariant subspace is the kernel of the \(k\)-linear map
\(F\mapsto\delta(F)-F\otimes1\). Every \(k\)-algebra is flat as a \(k\)-module, so tensoring this kernel calculation with \(A\) preserves it. The base-changed map is exactly the relative action coaction. Consequently
\[
A[\mathfrak g_A]^{H_A}
=A\otimes_k k[\mathfrak g]^H
\xrightarrow{\ \sim\ }A[\Sigma_A].
\tag{IS.A15}
\]
Here invariants mean coaction invariants, with all test algebras, rather than merely functions unchanged by a selected set of \(A\)-points. Thus the affine invariant quotient restricts to an isomorphism on the slice over every ordinary coefficient base. Naturality in \(A\) follows directly from the same polynomial formulas.

For a product of adjoint semisimple groups, the triples, Cartans, root systems and spaces \(V\) are componentwise direct sums. Hence \(\Sigma\) is the product of its factor slices. The Weyl group is the product of the factor Weyl groups, as follows from the orthogonal-component argument in [*Root systems and their Weyl groups*, §5](../../RT-LIE/src/RT-LIE-08.md). The product Reynolds projection is the tensor product of the factor projections, so its image is the tensor product of their invariant rings. Through (IS.A1), this also gives the corresponding tensor product for adjoint invariants. The union of factor generator lists and weight lists proves all formulas and the restriction isomorphism for products.

For the trivial group, \(\mathfrak g=V=0\), \(W=1\), and both invariant and slice rings are \(k\). The degree lists are empty, the degree product is \(1=|W|\), the degree sum is \(0=|\Phi^+|\), and the empty Jacobian is \(1\). After base change the slice and quotient are both \(\operatorname{Spec}A\).

The ingredients established here are Molien's formula from finite-dimensional Reynolds traces, the reflection count from the actual chamber argument, the degree identities, dominance by lowest homogeneous terms, the characteristic-zero Jacobian argument, and the finite weighted polynomial inverse. The retained premises are precisely the graded invariant presentation (IS.A1) with its §1.2.1 field/group transport, the algebraic root/pinning and split root-subgroup foundations of §§1.1.1–1.1.5, and ordinary affine scheme/coaction and linear algebra foundations. The recursive highest-weight, character and finite-generation premises in the earlier polynomiality proof retain their own programme obligations. General quotient-fibre geometry, descent and the critical categorical theorems are not consequences of this restriction isomorphism.

#### 1.2.6. Higgs coefficients and the original \(SL_n\) comparison

For a Higgs field \(\phi\in H^0(X,\operatorname{ad}P\otimes\omega)\), each homogeneous invariant \(p_i\) gives a section of \(\omega^{D_i}\). In a local frame \(\eta\) of \(\omega\), write \(\phi=A\eta\) and set \(p_i(\phi)=p_i(A)\eta^{D_i}\). Changing the bundle frame conjugates \(A\), which preserves the invariant. Replacing \(\eta\) by \(u\eta\) replaces \(A\) by \(u^{-1}A\), so homogeneity preserves the displayed section. This proves gluing and naturality for all ordinary parameter algebras, using (IS.F6). Thus the invariant-coefficient target is the Hitchin base
\[
\mathcal A_H=\bigoplus_i H^0(X,\omega^{D_i}).
\tag{IS.F7}
\]
The degree comparison proved in §§1.2.2–1.2.5 identifies this with the graded differential space underlying the adjoint oper torsor. It constructs the base and the coefficient morphism; it does not prove the global-functions or filtered quantization theorem (K6.1).

The degrees agree for dual root systems. Their Weyl groups are the same, and their reflection representations are dual. The rational root inner product is invariant and nondegenerate, so it identifies the reflection representation with its dual. Extending the rational pairing to \(k\) retains its nonzero determinant. Therefore the two Weyl-invariant polynomial rings have the same generator degrees. This proves the degree comparison needed when the automorphic and oper groups are Langlands dual, at the root-datum convention already specified.

For \(\mathfrak{sl}_n\) these invariants are exactly the characteristic-polynomial coefficients of degrees \(2,\ldots,n\). Here is the polynomial proof. On diagonal matrices write their entries \(x_1,\ldots,x_n\); the Weyl group permutes them. The symmetric-polynomial ring is
\[
k[x_1,\ldots,x_n]^{S_n}=k[e_1,\ldots,e_n],
\tag{IS.F8}
\]
where \(e_i\) is elementary symmetric of degree \(i\). Order monomials lexicographically, with \(x_1>\cdots>x_n\), and first treat a homogeneous symmetric polynomial. Its leading exponent tuple satisfies \(a_1\geq\cdots\geq a_n\): swapping an increasing adjacent pair would give a larger monomial with the same coefficient. The product
\(e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots e_n^{a_n}\)
has exactly that leading monomial with coefficient one. Subtracting its leading coefficient times this product strictly decreases the leading monomial among the finitely many monomials of the fixed total degree. Repetition terminates and proves generation. Distinct monomials in the \(e_i\) have distinct leading exponent tuples, because \(a_j=\sum_{i\geq j}b_i\) for the tuple of powers \(b_i\); hence a polynomial relation cannot cancel its largest leading monomial. This proves independence. Separate homogeneous components give (IS.F8) for arbitrary polynomials.

Trace zero imposes \(e_1=0\). Averaging by \(1/n!\) makes invariants commute with this quotient: an invariant quotient class has an invariant polynomial lift after averaging. If an invariant polynomial equals \(e_1G\), invariance of \(e_1\) and the domain property force \(G\) invariant, so the invariant kernel is precisely \(e_1k[e_1,\ldots,e_n]\). Consequently
\[
\bigl(k[x_1,\ldots,x_n]/(x_1+\cdots+x_n)\bigr)^{S_n}
=k[e_2,\ldots,e_n].
\tag{IS.F9}
\]
Chevalley restriction (IS.F1) lifts these uniquely to \(\mathfrak{sl}_n\); they are the coefficients \((-1)^ie_i\) of its characteristic polynomial. That proves the full invariant-algebra assertion used in (K6.2), with the same matrix normalization as the scalar-oper calculation. The previously derived heights \(1,\ldots,n-1\) give the same degrees, and the Hitchin and oper spaces both have dimension \((n^2-1)(g-1)\).

The oper ring has the corresponding weighted filtration. Write
\[
E=\bigoplus_{m\geq1}V_m\otimes_k H^0(X,\omega^{m+1}).
\]
A reference projective connection identifies its affine oper torsor with \(E\), so its polynomial coordinate ring is \(\operatorname{Sym}(E^*)\). Give a linear coordinate dual to the height-\(m\) summand weight \(m+1\), and let \(F_a\) span monomials of weight at most \(a\). Changing the reference translates only the quadratic summand in the direction of \(e\), by (DS.G7). Thus a weight-two coordinate changes by a scalar constant, while all higher-weight coordinates are unchanged. Substitution by this translation and its inverse preserve every \(F_a\) and act identically on the highest-weight symbols. Changing homogeneous bases is a linear change within equal-weight blocks. This proves that the filtration is independent of the reference and such bases, and
\[
\operatorname{gr}_F k[\operatorname{Op}_H(X)]
\simeq\operatorname{Sym}(E^*).
\tag{IS.F10}
\]
The weighted polynomial isomorphism of the slice with invariant coordinates has a weighted polynomial inverse, as proved in §§1.2.2–1.2.5. Applying its monomials to differential-valued coefficients glues, because the weights in every monomial sum to its target degree. The inverse glues for the same reason. Taking global sections therefore identifies \(E\), as a graded affine scheme, with \(\bigoplus_iH^0(X,\omega^{D_i})\), after the stated generator choices. This is an identification in ordinary families as well. For every ordinary \(k\)-algebra \(R\), the fixed-curve tensor proof recalled in §2.1 gives
\[
H^0(X_R,\omega_R^d)=R\otimes_k H^0(X,\omega^d).
\]
Multiplication of sections is defined by multiplication on each open-set complex and commutes with this scalar extension. Thus both weighted polynomial maps, and their already proved composition identities, commute with ordinary base change, including nonreduced coefficients. This identifies the ring in (IS.F10) with the Hitchin-base ring; the dual-root argument gives the same degrees for the automorphic dual group. The identification is a classical graded-ring construction. An equality with global critically twisted differential operators still requires the full filtered theorem (K6.1).

For a connected reductive group, at its explicit Lie/root-datum structure premise, \(\mathfrak g=\mathfrak z\oplus\mathfrak g_{\rm ss}\). The adjoint action is trivial on \(\mathfrak z\) and factors through the adjoint semisimple group on the other summand. Polynomial coordinates on \(\mathfrak z\) therefore contribute degree-one generators, while the semisimple generators are the ones just constructed. Taking the coaction kernel gives the tensor product of these invariant rings, including after every ordinary scalar extension. This invariant-ring observation retains the central connections and central automorphisms in the oper problem; it does not turn a nonadjoint reductive oper stack into the adjoint affine scheme.

## 2. Classical \(PGL_n\)-opers in ordinary families

### 2.1. Exact imported foundations and the elementary line calculation (O0)

The curve input in [The GL_1 case as an equivalence of categories](the-gl-1-case-as-an-equivalence-of-categories.md), §1.1.12, formula (R7.3), proves

\[
H^1(X,\mathcal F)^\vee\simeq\operatorname{Hom}_X(\mathcal F,\omega)
\tag{O0.1}
\]

for coherent \(\mathcal F\), with the constructed differential trace. Its §§1.1.13–1.1.14 prove the global residue formula and

\[
\operatorname{tr}_X[\,d\log g_{ij}\,]=\deg M
\tag{O0.2}
\]

for a line \(M\) with frames \(e_j=e_i g_{ij}\), using ordered Čech differential \((\delta a)_{ij}=a_j-a_i\). The class on the left is the class of
\(0\to\omega\otimes M\to J^1M\to M\to0\).
The trace uses the displayed frame and Čech signs. The fixed-curve tensor/Čech proof in §1.1.16 of that lesson supplies ordinary arbitrary-base tensor compatibility. Its ordinary Picard input in §1.1 is the smooth projective connected Jacobian \(J=\operatorname{Pic}^0(X)\), with the rigidified Picard construction described there. These inputs retain the explicit recursive coherent-cohomology, local-algebra, projective-scheme and Picard foundations of that lesson; their complete recursive proofs remain required.

Here is the line-bundle dimension calculation, so no unproved Riemann–Roch citation is needed for the oper dimension. A rational section of a line \(M\) identifies it with \(\mathcal O_X(D)\) for its finite divisor \(D\); this follows by choosing a rational frame and comparing its valuations with a local DVR frame. Principal divisors have degree zero by the proved residue theorem applied to \(d\log f\). For every closed point \(p\), the local parameter calculation gives

\[
0\longrightarrow\mathcal O_X(D-p)\longrightarrow
\mathcal O_X(D)\longrightarrow k_p\longrightarrow0.
\tag{O0.3}
\]

The last map takes the coefficient of the one additional permitted local power. The finite-dimensional cohomology long exact sequence, and vanishing above degree one from the two-affine computation, imply that adding \(p\) increases the Euler characteristic by one. Repeating for positive and negative coefficients of \(D\) gives

\[
\chi(M)=\deg M+1-g,
\qquad g=\dim_kH^1(X,\mathcal O_X).
\tag{O0.4}
\]

Here \(H^0(X,\mathcal O_X)=k\), proved in §1.1.12 of that earlier lesson. Applying (O0.1) to \(\mathcal O_X\) and to \(\omega\) gives \(h^0(\omega)=g\) and \(h^1(\omega)=1\). Applying (O0.4) to \(\omega\) consequently gives

\[
\deg\omega=2g-2.
\tag{O0.5}
\]

A nonzero regular section of a line has an effective divisor, so a line of negative degree has no section. Thus for every \(i\geq2\), duality and (O0.5) give

\[
H^1(X,\omega^i)=H^0(X,\omega^{1-i})^\vee=0,
\qquad
h^0(X,\omega^i)=(2i-1)(g-1).
\tag{O0.6}
\]

Finally, a theta characteristic exists. Choose a line \(M\) of degree \(g-1\), for example \(\mathcal O_X((g-1)p)\). The line \(\omega M^{-2}\) is in \(J(k)\). On the smooth group \(J\), the differential of multiplication by two at the identity is \(2\operatorname{id}\): the differential of the group law adds tangent vectors. Translations give the same invertible differential everywhere. The smooth local Jacobian criterion makes \([2]:J\to J\) étale, hence open. It is proper, since \(J\) is proper and its graph is closed in the product with the separated target, so its image is closed too. The image is nonempty, and connectedness of \(J\) makes it all of \(J\). Every nonempty fibre of this finite-type morphism has a closed \(k\)-point, because \(k\) is algebraically closed. Choose \(N\) with \(N^2\simeq\omega M^{-2}\); then

\[
\theta=M\otimes N,
\qquad \theta^2\xrightarrow{\sim}\omega.
\tag{O0.7}
\]

This last construction uses the specified ordinary Jacobian foundation and the standard smooth-local Jacobian criterion and proper-image foundation; it is not a proof of Picard representability. From now on fix both \(\theta\) and the displayed square isomorphism.

### 2.2. The intrinsic oper condition (O1)

Let \(G=PGL_n\), let \(B\subset G\) be the image of upper triangular matrices, and let \(\mathfrak b\subset\mathfrak g\) be its Lie algebra. A \(G\)-oper is a principal \(G\)-bundle \(P\), a connection \(\nabla\), and a \(B\)-reduction \(P_B\), subject to the following condition.

The failure of \(\nabla\) to preserve \(P_B\) is its second fundamental form, a section of
\(\omega\otimes(P_B\times^B(\mathfrak g/\mathfrak b))\).
Require it to belong to the \(B\)-stable subbundle given by

\[
\mathfrak g_{-1}/\mathfrak b
=\bigoplus_{i=1}^{n-1}\mathfrak g_{-\alpha_i},
\qquad
\mathfrak g_{-1}=\mathfrak b+
\bigoplus_{i=1}^{n-1}kE_{i+1,i},
\tag{O1.1}
\]

and require every simple-root component to be nowhere zero. The notation in (O1.1) means the quotient and its simple-root characters, not a claim that each negative root vector is fixed by \(B\). Conjugation by an upper triangular matrix preserves \(\mathfrak g_{-1}\); modulo \(\mathfrak b\), the adjacent lower diagonal entries are multiplied by their diagonal characters. This proves that the condition is independent of the adapted frame.

Equivalently, after a vector-bundle lift, write the complete flag as

\[
0=F_0\subset F_1\subset\cdots\subset F_n=E,
\quad\operatorname{rk}F_i=i.
\]

Then

\[
\nabla(F_i)\subset F_{i+1}\otimes\omega,
\qquad
\alpha_i:\operatorname{gr}_iE
\xrightarrow{\sim}\operatorname{gr}_{i+1}E\otimes\omega
\quad(1\leq i<n).
\tag{O1.2}
\]

The map \(\alpha_i\) is \(\mathcal O_X\)-linear: the extra Leibniz term for \(f s\) lies in \(F_i\otimes\omega\) and disappears in the indicated quotient. Adding a scalar one-form to the lifted connection also disappears in this quotient. In an adapted frame and an étale coordinate \(t\), (O1.2) says precisely that

\[
\nabla_{\partial_t}=\partial_t+A,
\qquad A_{ji}=0\text{ if }j>i+1,
\qquad A_{i+1,i}\in\mathcal O_X^\times.
\tag{O1.3}
\]

This is the coordinate expression of the intrinsic condition, and not its definition.

### 2.3. A normalized vector lift, including its choices (O2)

A \(B\)-reduction supplies a vector-bundle lift without a Brauer-group theorem. The map \(B_{GL_n}\to B\) has the group section sending a projective upper triangular matrix to its unique representative whose last diagonal entry is \(1\). Products preserve that condition. Associate to \(P_B\) this upper triangular representation, producing a rank-\(n\) bundle \(E_0\) with its complete flag. Its quotient \(Q=E_0/F_{n-1}\) is canonically \(\mathcal O_X\). Its projectivization is \(P\), because the section composed with \(GL_n\to PGL_n\) is the given inclusion of \(B\).

The projective connection determines the maps \(\alpha_i\) in (O1.2). Iterating them, starting with \(Q=\mathcal O_X\), gives

\[
\operatorname{gr}_i E_0\simeq\omega^{n-i},
\qquad
\det E_0\simeq\omega^{n(n-1)/2}.
\tag{O2.1}
\]

These are actual isomorphisms induced by the oper maps, rather than degree equalities. Put

\[
L=\theta^{1-n},
\qquad E=E_0\otimes L.
\tag{O2.2}
\]

Equations (O2.1) and \(\theta^2=\omega\) give a distinguished trivialization of \(\det E\); the quotient of its last flag step is the fixed line \(L\). A connection on \(P(E)\) has a unique lift to \(E\) inducing the zero connection on this trivialized determinant. To verify this directly, take frames whose wedges are the specified determinant frame. Their transition matrices have determinant one. Lift the local \(\mathfrak{pgl}_n\)-valued connection form by the unique trace-zero matrix, using
\(\mathfrak{sl}_n\xrightarrow{\sim}\mathfrak{pgl}_n\) in characteristic zero. On an overlap the gauge formula

\[
A\longmapsto gAg^{-1}-(\partial_tg)g^{-1}
\tag{O2.3}
\]

preserves trace zero since \(\partial_t\log\det g=0\). Therefore the local lifts glue. Two lifts differ by a scalar one-form, and their determinant connections differ by \(n\) times that form, so the determinant condition makes them equal. This proves existence and uniqueness of the normalized lift.

This construction does not identify arbitrary \(SL_n\)-opers with operators on the fixed line \(L\). If two determinant-trivialized vector connections have the same projective connection, local lifts of a projective isomorphism differ on overlaps by scalars. Those scalars are the transition functions of a line \(T\), giving \(E'\simeq E\otimes T\). The determinant identifications give \(T^n\simeq\mathcal O_X\). The scalar differences of the connection forms give a connection on \(T\), and the determinant condition says its \(n\)-th tensor power is the trivial connection. Thus other \(SL_n\) lifts are flat \(\mu_n\) twists. Projectivization removes this extra central choice. The normalized lift in (O2.2), with quotient fixed as \(L\), is the one used below.

### 2.4. Scalar normalization is coordinate independent (O3)

A scalar oper for the chosen theta characteristic is a differential operator

\[
D:L=\theta^{1-n}\longrightarrow
L\otimes\omega^n=\theta^{1+n}
\tag{O3.1}
\]

of order \(n\), with principal symbol \(1\) and subprincipal coefficient zero. Here is a definition and proof of the latter normalization. In a coordinate \(t\) and a local square frame \(\tau^2=dt\), use the frames \(\tau^{1-n}\) and \(\tau^{1+n}\). Write

\[
D_t=\partial_t^n+a_{n-1}(t)\partial_t^{n-1}
 +\cdots+a_0(t).
\tag{O3.2}
\]

The condition is \(a_{n-1}=0\). Square frames exist étale locally. Changing \(\tau\) to \(-\tau\) multiplies source and target frames by the same sign, so the expression is unchanged.

For a coordinate change \(t=\varphi(s)\), put \(\lambda=\varphi'(s)\), an invertible function, and \(b=(n-1)/2\). The operator in density frames transforms as

\[
D_s=\lambda^{b+1}D_t\lambda^b,
\qquad\partial_t=\lambda^{-1}\partial_s.
\tag{O3.3}
\]

For example the input coefficient transforms by
\(f_t=\lambda^b f_s\), because its weight is \(-b\); the output weight is \(b+1\). These are the two factors in (O3.3). Half powers can be evaluated after an étale square-root extension; their signs cancel in the formula.

Inductively, the two highest terms of the repeated operator are

\[
(\lambda^{-1}\partial_s)^n
=\lambda^{-n}\partial_s^n
-\frac{n(n-1)}2\lambda^{-n}\frac{\lambda'}\lambda
 \partial_s^{n-1}+\text{terms of order at most }n-2.
\tag{O3.4}
\]

Indeed, left multiplication by \(\lambda^{-1}\partial_s\) differentiates the leading coefficient, contributing \(-n\) to the next coefficient at the \((n+1)\)-st step, so the numbers obey
\(c_{n+1}=c_n-n\), \(c_1=0\). Inserting (O3.4) into (O3.3), differentiation of the right factor contributes \(nb\lambda'/\lambda\) to the coefficient of \(\partial_s^{n-1}\). The two contributions cancel since \(nb=n(n-1)/2\). The original \(a_{n-1}\) contributes \(\lambda a_{n-1}(\varphi(s))\). Consequently monicity and vanishing of \(a_{n-1}\) are invariant.

These equations work on Zariski coordinate opens even if a square frame is unavailable there. If a chosen frame \(\tau\) obeys \(\tau^2=h\,dt\), then, in the \(\tau\)-frames, the two highest coefficients of a normalized operator are

\[
h^{-n}\partial_t^n
-\frac{n(n-1)}2h^{-n}\frac{h'}h\partial_t^{n-1}.
\tag{O3.5}
\]

To see this, formally put \(\tau=h^{1/2}(dt)^{1/2}\) and conjugate \(\partial_t^n\) by the source and target frame factors. The leading coefficient is \(h^{-n}\), and the next one is \(n(1-n)h'/(2h)\) times it. Both expressions belong to the original coordinate ring, and the square-root sign cancels. Thus (O3.5), with all further coefficients chosen arbitrarily, gives local algebraic normalized operators on an ordinary Zariski cover.

### 2.5. Equivalence of intrinsic opers and scalar opers (O4)

Write \(J^rL\) for the bundle of \(r\)-jets of sections of \(L\), defined by the \((r+1)\)-st infinitesimal neighbourhood of the diagonal. In a coordinate and frame its components are
\((f,f',\ldots,f^{(r)})\); characteristic zero allows factorials to be absorbed into this basis. The transition formula is the ordinary chain and product rule. Its triangular highest terms give the exact sequences

\[
0\longrightarrow L\otimes\omega^r\longrightarrow J^rL
\longrightarrow J^{r-1}L\longrightarrow0,
\qquad
\det J^{n-1}L=L^n\otimes\omega^{n(n-1)/2}=\mathcal O_X.
\tag{O4.1}
\]

The last equality uses the specified square isomorphism of \(\theta\), so it gives a fixed determinant frame.

**Theorem O4.** The ordinary functor of \(PGL_n\)-opers on the fixed \(X\) is isomorphic to the functor of operators (O3.1) with the stated normalization. It has no nontrivial oper automorphisms. The equivalence uses \(\theta\) to present the functor by scalar operators; its projective output is independent of that choice in the precise sense of O5.

**Proof from an intrinsic oper to an operator.** Take its normalized vector lift \((E,F_\bullet,\nabla)\) from O2 and the quotient \(\pi:E\to L\). In a local frame, write \(\nabla=\partial_t+A\) and let the quotient row be \(r_0=\pi\). Recursively define rows

\[
r_{j+1}=\partial_t r_j-r_jA.
\tag{O4.2}
\]

For a horizontal vector \(e(t)\), differentiation gives
\(\partial_t(r_je)=r_{j+1}e\). Therefore

\[
\Phi:E\longrightarrow J^{n-1}L,
\qquad e\longmapsto(r_0e,\ldots,r_{n-1}e)
\tag{O4.3}
\]

is intrinsic: it takes the finite horizontal Taylor extension of \(e\) and then the jet of its quotient. Existence and uniqueness of that finite extension can also be checked by solving the recursion
\((j+1)e_{j+1}=-\sum_{a+b=j}A_a e_b\) modulo the required jet order. Coordinate and frame changes preserve the horizontal equation and the jet of \(\pi(e)\), so (O4.3) glues algebraically. This finite recursion needs no analytic solution theorem.

Induction using (O1.2) shows that \(r_j\) vanishes on \(F_{n-j-1}\). Its induced map on \(\operatorname{gr}_{n-j}E\) is \((-1)^j\) times the product of the \(j\) successive oper maps, expressed in the chosen coordinate. Thus all antidiagonal entries of (O4.3) are invertible and \(\Phi\) is an isomorphism. Its determinant, compared with the fixed determinant frames from (O2.1) and (O4.1), is a universal sign: both determinants are products of exactly those oper maps, and the only additional factors are the row signs and the permutation reversing the graded order. In particular this determinant ratio has zero derivative.

Since \(r_0,\ldots,r_{n-1}\) form a row basis, there are unique functions \(a_j\) such that

\[
r_n+\sum_{j=0}^{n-1}a_jr_j=0.
\tag{O4.4}
\]

Set \(D_t=\partial_t^n+\sum_{j=0}^{n-1}a_j\partial_t^j\).
Its horizontal solution jets are exactly the image under \(\Phi\) of the horizontal vectors. The chain and product rules in (O4.3) show that the operators glue as an operator \(L\to L\omega^n\): their common leading symbol is the identity, and applying each local operator to the same formal quotient section gives the same unique relation. This also follows by transforming (O4.4) and using the row-basis uniqueness.

In jet components the horizontal system is

\[
\partial_t y=C_Dy,
\quad
C_D=
\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&&\ddots&\ddots&\vdots\\
0&\cdots&0&0&1\\
-a_0&-a_1&\cdots&-a_{n-2}&-a_{n-1}
\end{pmatrix}.
\tag{O4.5}
\]

The corresponding connection \(\partial_t-C_D\) has determinant connection form \(a_{n-1}\,dt\). But \(\Phi\) carries the determinant-zero connection on \(E\) to this connection, and its determinant ratio with the fixed jet frame is constant. Thus \(a_{n-1}=0\). We have obtained a normalized scalar oper.

**Proof from an operator to an intrinsic oper.** Given normalized \(D\), set \(E_D=J^{n-1}L\) and define its connection by (O4.5). To check gluing rather than assume it, view \(D\) as an \(\mathcal O_X\)-linear map \(J^nL\to L\omega^n\). Its restriction to the top jet kernel \(L\omega^n\) is the identity. Its kernel consequently maps isomorphically to \(J^{n-1}L\). There is an intrinsic holonomic map \(J^nL\to J^1(J^{n-1}L)\): take the first jet of the \((n-1)\)-jet of a section. In coordinates it sends \((f_0,\ldots,f_n)\) to the value components \((f_0,\ldots,f_{n-1})\) and derivative components \((f_1,\ldots,f_n)\). The chain and product rules show that this formula is compatible with coordinate and line-frame transitions, so it defines that intrinsic map. Compose it with the inverse from \(J^{n-1}L\) to the kernel of \(D\). The result is a splitting of the first-jet projection of \(E_D\), whose derivative equations are precisely (O4.5). For a local section \(y\), subtracting this splitting from its first jet gives \(dy-C_Dy\). Every ingredient is intrinsic, so the local connections agree on overlaps. Their trace is zero in the fixed determinant frame by the normalization proved in O3.

Give \(E_D\) the flag

\[
F_i=\ker(J^{n-1}L\longrightarrow J^{n-1-i}L)
\quad(1\leq i<n),\qquad F_n=E_D.
\tag{O4.6}
\]

In the ordered jet basis, \(F_i\) consists of the last \(i\) components. Matrix (O4.5) shows that the connection sends it into \(F_{i+1}\omega\), and on the adjacent graded lines its map is \(-1\) in these derivative coordinates. Hence the oper maps are isomorphisms. Projectivizing supplies a \(PGL_n\)-oper.

The two constructions are inverse: (O4.3) identifies the original connection and flag with precisely (O4.5)–(O4.6), while applying it to the jet construction recovers the original scalar relation. They are also inverse on arrows. An isomorphism of projective opers lifts by O2 to an isomorphism inducing the identity on the fixed quotient \(L\). Equations (O4.2) then force identity on every jet row, so its jet presentation is the identity. Conversely identity on the normalized scalar operator gives its unique projective oper isomorphism. This proves the asserted absence of automorphisms. All operations use finite jets, invertible maps, trace division by \(n\) and polynomial differentiation; they commute with ordinary base change, including nonreduced parameters. \(\square\)

The concrete matrix gauge statement is a useful check on this proof. In (O1.3), let \(c_i=A_{i+1,i}\). A diagonal projective gauge with \(d_1=1\), \(d_{i+1}=d_i c_i^{-1}\), first makes every \(c_i=1\). This torus gauge exists uniquely modulo the central scalar after this condition is imposed. It is essential when the \(c_i\) were arbitrary units. Use determinant-normalized frames afterward, étale locally if an \(n\)-th root is needed to normalize the determinant; a scalar adjustment does not change the adjacent lower entries. For the resulting trace-zero system and quotient the last component, form the rows (O4.2). The matrix whose row \(i\) is
\((-1)^{n-i}r_{n-i}\) is upper triangular unipotent: its first nonzero entry is \(1\) in column \(i\). Gauge by this matrix. For a horizontal vector its new components are

\[
v_i=(-1)^{n-i}f^{(n-i)},
\qquad f=\pi(e).
\]

Thus \(v_i'+v_{i-1}=0\) for \(i\geq2\), and the new connection is

\[
\partial_t+
\begin{pmatrix}
0&u_1&u_2&\cdots&u_{n-1}\\
1&0&0&\cdots&0\\
0&1&0&\cdots&0\\
\vdots&&\ddots&\ddots&\vdots\\
0&\cdots&0&1&0
\end{pmatrix},
\quad
D_t=\partial_t^n+\sum_{j=2}^n(-1)^{j-1}u_{j-1}\partial_t^{n-j}.
\tag{O4.7}
\]

The upper left entry is zero by trace zero. A unipotent upper triangular gauge preserves the last component \(f\). In companion form the other components are then forced to be the derivatives displayed above. This proves uniqueness of the unipotent gauge, and freeness of its action on the normalized simple-coefficient slice. Together with the preceding torus normalization it proves the corresponding full Borel-gauge classification for \(PGL_n\). It does not assert that unipotent gauge alone normalizes arbitrary simple coefficients.

### 2.6. Theta changes and ordinary families (O5)

If \(\theta'\) is another theta characteristic with specified square isomorphism, write \(\theta'=\theta\otimes\eta\), where \(\eta^2\simeq\mathcal O_X\). This square isomorphism gives a canonical flat connection on \(\eta\). In a local frame with square function \(h\), its connection form is \(\tfrac12d\log h\), the unique form making the square trivialization horizontal. Étale locally choose a square-root frame with square \(1\); the transition functions are then \(\mu_2\)-valued and their relative derivatives are zero. This proves both gluing and flatness directly.

The new input and output lines are both the old lines tensored with \(\eta^{1-n}\), since \(\eta^{1+n}=\eta^{1-n}\) through \(\eta^{2n}=\mathcal O_X\). Tensor a scalar operator using these local horizontal frames. The constant transition factors make the operators glue, preserve symbol and subprincipal normalization, and give

\[
J^{n-1}(L\otimes\eta^{1-n})
\simeq J^{n-1}L\otimes\eta^{1-n}
\tag{O5.1}
\]

compatibly with connection and flag. Projectivization erases this flat line factor. These identifications compose as tensor identifications do. Changing a chosen square isomorphism by a scalar does not change its relative logarithmic derivative; the induced projective correspondence remains the same. This proves the promised choice independence, while retaining the explicit theta-dependent scalar presentation.

For an ordinary parameter scheme \(S\), the preceding statements concern relative connections on \(X\times S\) and relative operators between the fixed pulled-back density lines. The oper maps and determinant trivialization still define O2; locally on \(S\), the finite jet and row operations prove O4. On affine \(S=\operatorname{Spec}A\), the two-affine section complex of a fixed bundle is its original \(k\)-complex tensored with \(A\), as in the actual earlier proof §1.1.16. No infinitesimal tangent calculation is being used to infer a family equivalence. In particular O4 is a natural equivalence on ordinary families, not merely a bijection of \(k\)-points. It makes no claim about the full derived oper stack.

### 2.7. Global existence, affine structure and dimension (O6)

Let

\[
\mathcal V_r=\operatorname{Diff}^{\leq r}_{X/k}(L,L\omega^n)
\quad(0\leq r\leq n-2),\qquad\mathcal V_{-1}=0.
\]

These are vector bundles: on a coordinate and line-frame open, an operator is uniquely a sum of coefficient functions times \(\partial_t^j\), \(0\leq j\leq r\). The leading symbol gives short exact sequences

\[
0\longrightarrow\mathcal V_{r-1}\longrightarrow\mathcal V_r
\longrightarrow\omega^{n-r}\longrightarrow0.
\tag{O6.1}
\]

The symbol line is
\(\operatorname{Hom}(L,L\omega^n)\otimes\omega^{-r}=\omega^{n-r}\).
Surjectivity is local: prescribe the highest coefficient of a local differential operator. By (O0.6), every symbol line in (O6.1) has zero \(H^1\). Induction in the long exact sequence gives

\[
H^1(X,\mathcal V_r)=0,
\quad
0\to H^0(\mathcal V_{r-1})\to H^0(\mathcal V_r)
\to H^0(\omega^{n-r})\to0.
\tag{O6.2}
\]

Choose normalized operators on the Zariski coordinate/frame cover using (O3.5). Their differences have order at most \(n-2\), by coordinate independence of the two highest coefficients. They therefore form a Čech one-cocycle in \(\mathcal V_{n-2}\). Its \(H^1\) is zero by (O6.2), so after subtracting local sections of that bundle the operators agree on overlaps. This proves global existence of a normalized operator \(D_0\), and hence of a global \(PGL_n\)-oper.

Two global normalized operators differ by a unique element of

\[
W_n=H^0(X,\mathcal V_{n-2}).
\tag{O6.3}
\]

Conversely adding any such operator to \(D_0\) preserves its two highest normalized coefficients. Thus the space is canonically a torsor under the vector space \(W_n\); choosing \(D_0\) identifies it with that vector space. For an arbitrary ordinary \(k\)-algebra \(A\), the fixed-curve tensor calculation and \(H^1(\mathcal V_{n-2})=0\) give

\[
H^0(X_A,(\mathcal V_{n-2})_A)=W_n\otimes_kA.
\tag{O6.4}
\]

Indeed a \(k\)-complex splits into its cohomology and contractible terms, and tensoring the contraction with \(A\) preserves it; equivalently tensoring the two-affine Čech complex is exact over the field. On an affine base all normalized operators are \(D_0\) plus this space. Descent on an arbitrary base proves that the ordinary oper functor is represented by the affine space associated to the torsor. By O4 it represents the intrinsic oper functor, not just its scalar model.

The filtration (O6.2) has associated graded spaces

\[
H^0(\omega^n),H^0(\omega^{n-1}),\ldots,H^0(\omega^2).
\tag{O6.5}
\]

Consequently

\[
\begin{aligned}
\dim\operatorname{Op}_{PGL_n}(X)
&=\dim W_n
=\sum_{i=2}^n h^0(X,\omega^i)\\
&=(g-1)\sum_{i=2}^n(2i-1)
=(n^2-1)(g-1).
\end{aligned}
\tag{O6.6}
\]

The finite sum follows from
\(\sum_{i=1}^n(2i-1)=n^2\), subtracting its first term. There is also an isomorphism of affine spaces with
\(\bigoplus_{i=2}^nH^0(X,\omega^i)\): choose a base oper and choose linear splittings of every short exact sequence in (O6.2). Such splittings exist by extending a basis. This argument does **not** supply a canonical direct-sum decomposition of \(W_n\), nor a preferred origin. The raw lower coefficients of a scalar operator generally mix with their derivatives under coordinate change. For example, with \(n=3\), \(D_t=\partial_t^3+a_1\partial_t+a_0\), and \(S=\{\varphi,s\}\), expansion of (O3.3) gives

\[
(a_1)_s=\lambda^2a_1(\varphi)+2S,
\qquad
(a_0)_s=\lambda^3a_0(\varphi)
+\lambda\lambda'a_1(\varphi)+S'.
\tag{O6.7}
\]

For the pure third derivative, the coefficient of \(\partial_s\) is \(2\lambda''/\lambda-3(\lambda'/\lambda)^2=2S\), and its constant coefficient is \(\lambda'''/\lambda-4\lambda'\lambda''/\lambda^2+3(\lambda')^3/\lambda^3=S'\). The transformed first-derivative term supplies the extra \(\lambda\lambda'a_1\); multiplication supplies \(\lambda^3a_0\). This proves the displayed mixing directly. Sections 1.1.1–1.1.7 construct the specified Drinfeld–Sokolov coordinates and their equivariance from a pinning. Subtracting a reference projective connection gives their differential-summand presentation; it supplies no preferred affine origin. The raw scalar coefficients in (O6.7) still mix as displayed. The independent scalar affine-space and dimension proofs need no such slice.

For \(n=2\), the difference bundle is already \(\mathcal V_0=\omega^2\), so the torsor is canonically under \(H^0(X,\omega^2)\), and its dimension is \(3g-3\). These proofs give the complete solutions to the dimension exercise and the affine-space computation, relative to the earlier foundations made explicit in O0.

### 2.8. Bundle-stack dimension and its foundation boundary

The same Euler formula for a vector bundle \(V\) of rank \(r\) is
\[
\chi(V)=\deg V+r(1-g).
\tag{K1.5}
\]
Indeed a rational vector spans a rank-one saturated subsheaf. Locally on this regular curve, saturation inside a free module is a free rank-one module and its quotient is torsion-free, hence free over the local DVR. The quotient is a vector bundle of rank \(r-1\). Determinants and Euler characteristics are additive in this exact sequence; induction from (O0.4) proves (K1.5).

For an \(SL_n\)-bundle \(V\), the bundle \(\operatorname{End}_0V\) has rank \(n^2-1\) and degree zero. The determinant of \(V\otimes V^*\) is trivial; trace splits off \(\mathcal O_X\), since \(n\) is invertible, giving the determinant assertion for \(\operatorname{End}_0V\). First-order deformations have Čech cocycles in this bundle; changes of trivialization give coboundaries, and infinitesimal automorphisms are its global sections. Hence
\[
h^1(\operatorname{End}_0V)-h^0(\operatorname{End}_0V)
=(n^2-1)(g-1).
\tag{K1.6}
\]
This is the stack dimension, rather than the dimension of a coarse moduli space, once algebraicity and smoothness of \(\operatorname{Bun}_{SL_n}\) are supplied. Their Artin and formal algebraization chain remains unproved in [The moduli stack of bundles](the-moduli-stack-of-bundles.md). The Čech tangent and Euler calculation proves (K1.6) at that explicit foundation.

### 2.9. The Schwarzian with the fixed sign (O7)

For \(n=2\), write

\[
D_t=\partial_t^2-q_t(t),
\qquad D:\theta^{-1}\to\theta^3.
\tag{O7.1}
\]

With \(t=\varphi(s)\), \(\lambda=\varphi'\), formula (O3.3) reads

\[
D_s=\lambda^{3/2}
\bigl((\lambda^{-1}\partial_s)^2-q_t(\varphi(s))\bigr)
\lambda^{1/2}.
\]

Differentiating the two factors gives zero coefficient of \(\partial_s\), leading coefficient one, and constant derivative contribution
\(\lambda''/(2\lambda)-3(\lambda')^2/(4\lambda^2)\). Therefore

\[
\boxed{\ q_s(s)=\lambda(s)^2q_t(\varphi(s))
-\frac12\{\varphi,s\}\ },
\quad
\{\varphi,s\}=\frac{\varphi'''}{\varphi'}
-\frac32\left(\frac{\varphi''}{\varphi'}\right)^2.
\tag{O7.2}
\]

This sign belongs to the convention \(D=\partial^2-q\). The difference of two \(q\)'s has no Schwarzian term and transforms as a quadratic differential. That agrees exactly with the torsor under \(H^0(\omega^2)\) proved in O6.

For clarity about the word “structure”, over an arbitrary \(k\) the algebraic object proved here is a regular projective connection with transformation law (O7.2), also called an algebraic projective structure in this oper usage. It is not an assertion that every oper has an algebraic atlas of maps into \(\mathbf P^1\) on a Zariski or étale cover. It has the following exact formal-coordinate interpretation, and over \(\mathbb C\) the usual analytic interpretation.

At a point choose a formal coordinate \(t\). The equation \(y''=q(t)y\) has unique formal solutions \(u,v\) with
\(u(0)=0,u'(0)=1,v(0)=1,v'(0)=0\): if \(q=\sum q_jt^j\), comparison of coefficients gives

\[
(m+2)(m+1)y_{m+2}=\sum_{j=0}^m q_j y_{m-j}.
\tag{O7.3}
\]

Every denominator is invertible in characteristic zero. The Wronskian
\(W=u'v-uv'\) has derivative \(u''v-uv''=0\), so \(W=1\). The ratio \(r=u/v\) is a formal coordinate. Since \(r'=W/v^2\),

\[
\frac{r''}{r'}=-2\frac{v'}v,
\qquad
\{r,t\}=
\left(\frac{r''}{r'}\right)'
-\frac12\left(\frac{r''}{r'}\right)^2
=-2\frac{v''}v=-2q(t).
\tag{O7.4}
\]

Other bases of the two-dimensional solution space change \(r\) by a constant fractional linear transformation. Conversely, given a formal coordinate \(r\) with \(\{r,t\}=-2q\), choose \(v=(r')^{-1/2}\) and \(u=rv\). The square root exists formally after choosing its nonzero constant root. Differentiation gives \(v''=qv\) and \(u''=qu\); their Wronskian is nonzero. This proves the converse and uniqueness modulo \(PGL_2(k)\).

A direct chain-rule calculation gives

\[
\{r\circ\varphi,s\}=(\varphi')^2\{r,\varphi(s)\}
 +\{\varphi,s\}.
\tag{O7.5}
\]

One way to check every term is to write
\((r\circ\varphi)''/(r\circ\varphi)'=
(r''/r')(\varphi)\varphi'+\varphi''/\varphi'\),
differentiate it, and subtract one half of its square; the cross terms cancel. A fractional linear map has zero Schwarzian by the same derivative formula. Thus (O7.4) is exactly compatible with (O7.2) and formal projective charts modulo fractional linear maps.

For the analytic comparison over \(\mathbb C\), assume completeness of the complex numbers, the completeness of the sup-norm space of holomorphic functions continuous on a closed disc, the Cauchy integral formula and the elementary holomorphic primitive/integration rule on a disc. The sup-norm completeness follows from completeness of continuous functions under uniform limits together with the Cauchy integral formula. Those analytic foundations are unproved here, so this paragraph is conditional on them. The algebraic and formal proofs above do not use them. Subject to these analytic inputs, the formal solutions just used are analytic on sufficiently small discs. If \(|q|\leq M\) on a small closed disc, the map

\[
y(t)\longmapsto a+bt+
\int_0^t(t-s)q(s)y(s)\,ds
\]

on holomorphic functions continuous on that disc is a contraction in the sup norm once \(MR^2/2<1\). Its successive differences form a geometrically convergent series, so their uniform limit is holomorphic by the Cauchy integral formula. Differentiating the integral proves the equation and initial values; applying the same estimate to the difference proves uniqueness. Applying this to \((a,b)=(0,1),(1,0)\) supplies the local solution bases. Their ratios are local maps into \(\mathbf P^1\) with nonzero derivative, and overlapping solution bases differ by constant matrices, so the charts have fractional linear transitions. Conversely such charts give \(-\tfrac12\{r,t\}\), invariant under their transitions, and hence a holomorphic projective connection. This proves the equivalence between analytic projective structures and holomorphic projective connections, and constructs the analytic projective structure of every algebraic oper over \(\mathbb C\). Identifying the entire holomorphic global parameter space with the algebraic global parameter space additionally uses the proper algebraic–analytic coherent comparison; that separate foundation is not proved here. No analytic meaning is assigned to a general algebraically closed \(k\).

### 2.10. The nonsplit jet extension and irreducibility (O8)

For \(n=2\), O4 identifies every normalized vector lift with

\[
E=J^1(\theta^{-1}),
\qquad
0\longrightarrow\theta\longrightarrow E
\longrightarrow\theta^{-1}\longrightarrow0.
\tag{O8.1}
\]

Its class lies in
\(\operatorname{Ext}^1(\theta^{-1},\theta)
=H^1(X,\omega)\).
To check both the class and its sign, use local frames \(e_j=e_i g_{ij}\) of \(\theta^{-1}\). The jet map satisfies
\(j(f e_i)=f j(e_i)+df\otimes e_i\).
The local \(\mathcal O\)-linear splitting taking \(e_i\) to \(j(e_i)\) then obeys

\[
s_j(e_i)-s_i(e_i)
=g_{ij}^{-1}j(e_j)-j(e_i)
=d\log g_{ij}\otimes e_i.
\tag{O8.2}
\]

Thus the extension is \(\operatorname{at}(\theta^{-1})\), and (O0.2) gives

\[
\operatorname{tr}_X[ E ]
=\deg(\theta^{-1})=-(g-1)\neq0.
\tag{O8.3}
\]

It is nonsplit. Since \(H^1(\omega)\simeq k\), nonzero extension classes form one orbit under rescaling either identified end line. Hence (O8.1) is the unique isomorphism class of **nonsplit** such extensions when the end-line identifications may be rescaled. With the end maps fixed, its nonzero scalar class matters. The split extension is another extension class. O8.1 determines the underlying projective oper bundle; changing \(\theta\) tensors the vector bundle by the flat two-torsion line in O5 and leaves its projectivization unchanged.

**Theorem O8.** The de Rham local system underlying any regular \(PGL_2\)-oper on \(X\), \(g\geq2\), is irreducible: it has no horizontal \(B\)-reduction, equivalently no invariant algebraic projective line.

**Proof.** Suppose a horizontal projective section exists. In the normalized rank-two lift it gives an invariant line subbundle \(N\subset E\). More generally, if reducibility was first specified as an invariant line over \(k(X)\), take its saturation in \(E\). Over a DVR, a saturated rank-one submodule of a free rank-two module is generated by a primitive vector and has free quotient, so these saturations glue to a line subbundle. It remains connection-stable: in a primitive generator at least one component is a unit; since its derivative lies in the function-field line and the ambient connection is regular, that unit component forces its scalar connection coefficient to be regular. Thus either formulation yields a regular connection on \(N\).

A regular connection on a line has degree zero. In local frames its connection forms supply a coboundary for \([d\log g_{ij}]\), so its Atiyah class is zero; (O0.2) then gives \(\deg N=0\), since characteristic zero detects the integer degree. Compose its inclusion with the quotient in (O8.1). A nonzero map \(N\to\theta^{-1}\) would give a nonzero section of \(N^{-1}\theta^{-1}\), a line of degree \(-(g-1)<0\). Therefore that map is zero and the inclusion factors through \(\theta\). The factor \(N\to\theta\) is nowhere zero: a zero at any point would make its composite \(N\to E\) zero on that fibre, contradicting that \(N\) is a subbundle. It is consequently an isomorphism of lines, forcing
\(0=\deg N=\deg\theta=g-1\), a contradiction. This proves irreducibility. \(\square\)

The role of regularity is essential: a meromorphic invariant line can acquire residues and a nonzero degree. The statement here concerns the everywhere regular de Rham opers fixed at the start. It proves the assigned irreducibility exercise with its genus and coefficient hypotheses intact. Turning the result into a statement about complex analytic monodromy uses the algebraic–analytic comparison for horizontal reductions; that additional interpretation is not being certified by this algebraic proof alone.

## 3. An affine Lie algebra and its vacuum (K2)

Write \((\, ,\,)\) for an invariant symmetric form on a finite-dimensional Lie algebra \(\mathfrak g\). For Laurent polynomial modes \(x_m=x\otimes t^m\), define the central extension by
\[
[x_m,y_j]=[x,y]_{m+j}+m(x,y)\delta_{m,-j}K,\qquad [K,x_m]=0.
\tag{K2.1}
\]
The cocycle is \(\operatorname{Res}((df)g)(x,y)\). It is antisymmetric because the residue of \(d(fg)\) is zero. Invariance makes the three cyclic form coefficients in its Jacobi identity equal; the remaining scalar sum is \(2\operatorname{Res}d(fgh)=0\). Thus (K2.1) is a Lie bracket. We fix this mode convention explicitly; changing the direction of the residue cocycle changes the label of the central generator.

At level \(\ell\), let
\[
V_\ell=U(\widehat{\mathfrak g}_{\rm pol})
\otimes_{U(\mathfrak g[t]\oplus kK)}k_\ell,
\tag{K2.2}
\]
where \(\mathfrak g[t]\) kills its vacuum vector \(v\), and \(K\) acts by \(\ell\).

Here is the ordered-monomial argument used to interpret this module. For any Lie algebra with a well-ordered vector-space basis, rewrite an inverted pair \(ab\), \(a>b\), as \(ba+[a,b]\). Order words first by length and then lexicographically. A swap decreases the lexicographic word, and a bracket decreases length. This order is well founded, so reduction terminates. Disjoint pair reductions commute. The only overlapping ambiguity is \(abc\), \(a>b>c\). Reducing first the left or right pair and then comparing the lower terms gives
\[
[a,[b,c]]-[b,[a,c]]-[[a,b],c]=0,
\]
by Jacobi. These lower words have smaller order, so induction resolves their reductions. Induction on the first possible disagreement between two reduction sequences now shows that their terminal linear combinations agree: resolve their first steps by the disjoint or overlapping calculation and use the smaller-word induction on the resulting terms. Extending the normal-form map linearly, it kills the defining relations inside every surrounding word and has identity on ordered words. Thus those words span the enveloping algebra and are independent. This proves precisely the ordered basis assertion needed here.

Order negative modes before \(K\) and the nonnegative modes. Applying this basis to (K2.2) identifies its vector space with \(U(t^{-1}\mathfrak g[t^{-1}])\); its ordered negative-mode words are a basis. A mode \(x_m\) with \(m\) larger than the sum of the positive indices in a given negative-mode word kills that word applied to \(v\): commute it to the right, observing that every bracket subtracts one of those indices and a central term requires exact equality with a partial sum. This proves smoothness. Therefore formal nonnegative series act by finite sums on every vector, extending the vacuum to the formal affine Lie algebra.

Any endomorphism of this induced module is determined by the image of \(v\). Conversely a vector \(w\) killed by all nonnegative modes defines the map \(uv\mapsto uw\); the induction relations make it well defined. Consequently
\[
\operatorname{End}_{\widehat{\mathfrak g}}(V_\ell)
\simeq V_\ell^{\mathfrak g[[t]]}
\tag{K2.3}
\]
as vector spaces. This argument alone does not prove that its endomorphism algebra is commutative, nor identify it with functions on opers.

The extension to formal Laurent series also preserves the Lie bracket. For a vector \(w\), sufficiently high positive tails kill \(w\), and sufficiently high tails kill each of the two fixed vectors obtained by applying either Laurent series to \(w\). Each series has a finite negative part. Choose a common truncation above all those annihilation bounds plus the largest absolute value of any negative mode index occurring in either series. The tails then kill both compositions; their brackets with the other's finite negative part have mode indices above the annihilation bound for \(w\); brackets with positive parts have still higher indices. Central residue terms involve only finitely many matching positive and negative indices and are already retained in the chosen truncation. Thus the bracket identity on \(w\) reduces to the polynomial bracket identity. This proves a representation of the formal affine Lie algebra, rather than only a finite-sum definition of its action.

### 3.1. The critical quadratic vector (K3)

Take \([h,e]=2e,[h,f]=-2f,[e,f]=h\) and the form
\((e,f)=1,(h,h)=2\), with all other basis pairings zero. In this normalization the Killing form is four times the displayed form: \(\operatorname{ad}h\) has eigenvalues \(2,0,-2\), so its squared trace is \(8\), and invariance fixes the remaining pairings. Thus the critical form, minus half the Killing form, means \(\ell=-2\) in (K2.1).

Define
\[
Q=\left(\tfrac12h_{-1}h_{-1}
       +e_{-1}f_{-1}+f_{-1}e_{-1}\right)v.
\tag{K3.1}
\]
This is twice the convention in which the Sugawara vector has coefficients \(1/4,1/2,1/2\). Its degree-two ordered symbol is \(\tfrac12h^2+2ef\), so the ordered basis proves that \(Q\ne0\).

We compute all nonnegative-mode actions. The zero modes kill \(Q\). For example, \(e_0\) on its first term gives
\(-e_{-1}h_{-1}v-h_{-1}e_{-1}v\); on its last two terms it gives the opposite sum. The \(f_0\) calculation exchanges \(e,f\) and replaces \(h\) by \(-h\). The \(h_0\) calculation cancels the weights \(2,-2\) in each mixed term.

For mode one, the contributions from the three summands of (K3.1) are as follows:

| Acting mode | \(\tfrac12h_{-1}^2v\) | \(e_{-1}f_{-1}v\) | \(f_{-1}e_{-1}v\) |
| --- | --- | --- | --- |
| \(e_1\) | \(2e_{-1}v\) | \(\ell e_{-1}v\) | \((\ell+2)e_{-1}v\) |
| \(f_1\) | \(2f_{-1}v\) | \((\ell+2)f_{-1}v\) | \(\ell f_{-1}v\) |
| \(h_1\) | \(2\ell h_{-1}v\) | \(2h_{-1}v\) | \(2h_{-1}v\) |

Each entry follows by commuting that mode to the right until it reaches \(v\). For instance
\([e_1,h_{-1}]=-2e_0\),
\([e_1,f_{-1}]=h_0+\ell\), and
\(h_0e_{-1}v=2e_{-1}v\).
Thus for each basis vector \(x\),
\[
x_1Q=2(\ell+2)x_{-1}v.
\tag{K3.2}
\]
For mode two, the \(e_2,f_2\) terms end in \(e_0v,f_0v\), hence vanish. For \(h_2\), the first summand contributes zero, and the mixed summands give \(2\ell v\) and \(-2\ell v\). They cancel. For \(m\ge3\), commuting twice through the two negative modes leaves only modes of index \(m-2\ge1\), and no central term can occur since the total index is positive. All such terms kill \(v\). We have checked every nonnegative mode.

At \(\ell=-2\), therefore, \(Q\in V_{-2}^{\mathfrak{sl}_2[[t]]}\), and (K2.3) gives an actual affine-module endomorphism. At any other level \(e_1Q\ne0\), since \(e_{-1}v\) is a basis vector and the field has characteristic zero. This proves the central-vector calculation at exactly the critical level.

The result just proved is a vacuum invariant and its corresponding endomorphism. A claim that all normally ordered Fourier coefficients are central in a completed enveloping algebra also requires the completion, vertex operations and their compatibility. Section 3.2 supplies all quadratic mode operators, their commutativity and the full rank-one vacuum-center proof. The completed-enveloping-algebra, chiral and general higher-rank scopes remain additional parts of the theorem below.


### 3.2. The full rank-one vacuum center and its coordinate action

#### 3.2.1. All normally ordered quadratic modes

We retain the conventions proved in §3, “An affine Lie algebra and its vacuum,” of [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md): the affine bracket (K2.1), the ordered negative-mode basis, smoothness of the vacuum, and the endomorphism correspondence (K2.3). Here \(k\) has characteristic zero, \(\mathfrak g=\mathfrak{sl}_2(k)\), and
\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h,\qquad
B(e,f)=1,\quad B(h,h)=2.
\]
All other basis pairings are zero. On a module of scalar level \(\ell\), the bracket is
\[
[x_m,y_j]=[x,y]_{m+j}
             +m\ell B(x,y)\delta_{m+j,0}\operatorname{Id}.
\]
A module is **smooth** if, for every vector \(w\), some \(N\ge0\) satisfies \(x_jw=0\) for every \(x\in\mathfrak g\) and \(j\ge N\).

Put \(\theta(j)=0\) for \(j<0\) and \(\theta(j)=1\) for \(j\ge0\). Define
\[
:a_jb_q:
=\begin{cases}a_jb_q,&j<0,\\ b_qa_j,&j\ge0,\end{cases}
\qquad
S_n=\sum_{j\in\mathbb Z}
 \left(\tfrac12:h_jh_{n-j}:
             +:e_jf_{n-j}:+:f_je_{n-j}:\right).
\tag{RC.M1}
\]
These formulas define actual linear operators on every smooth module. If \(w\) has annihilation bound \(N\), a term with \(j\ge N\) has a rightmost mode killing \(w\). A term with \(j<0\) and \(n-j\ge N\) also kills \(w\). Thus any cutoff \(L\ge N+|n|+1\) retains all nonzero terms on \(w\). Taking a common bound for finitely many vectors proves linearity and permits the finite comparisons below.

The tensor
\[
C=e\otimes f+f\otimes e+\tfrac12h\otimes h
   =\sum_a a\otimes a^\vee
\tag{RC.M2}
\]
uses the basis \(a=e,f,h\) and its \(B\)-dual basis \(a^\vee=f,e,h/2\). It is invariant under the diagonal adjoint action. For \(e\), its derivative is
\(e\otimes h+h\otimes e-e\otimes h-h\otimes e=0\).
For \(f\), it is
\(-h\otimes f-f\otimes h+f\otimes h+h\otimes f=0\).
For \(h\), the terms are
\(2e\otimes f-2e\otimes f-2f\otimes e+2f\otimes e=0\).
Linearity proves invariance for every \(x\).

We compute the normal-order boundary explicitly. Set \(q=n-j\), \(D=[x_m,a_j]\), and \(E=[x_m,b_q]\), including their scalar central terms. Normal ordering a scalar times a mode means ordinary multiplication. Since
\(:a_jb_q:=a_jb_q-\theta(j)[a_j,b_q]\), Jacobi gives
\[
[x_m,:a_jb_q:]
=Db_q+a_jE-\theta(j)\bigl([D,b_q]+[a_j,E]\bigr).
\]
The Lie-mode part of \(D\) has index \(j+m\); its scalar part commutes with \(b_q\). Subtracting
\(:Db_q:=Db_q-\theta(j+m)[D,b_q]\) and
\(:a_jE:=a_jE-\theta(j)[a_j,E]\) therefore gives the exact identity
\[
\begin{split}
[x_m,:a_jb_{n-j}:]
={}&:[x_m,a_j]b_{n-j}:
       +:a_j[x_m,b_{n-j}]:\\
 &+\bigl(\theta(j+m)-\theta(j)\bigr)
       [[x,a]_{j+m},b_{n-j}].
\end{split}
\tag{RC.M3}
\]
This is an identity of operators for each fixed index \(j\), including the scalar central terms.

Sum (RC.M3) over the three dual-basis pairs in (RC.M2). The Lie-mode parts of the first two terms cancel. Indeed, reindex the first sum by \(i=j+m\). For each resulting index \(i\), their tensor coefficient is
\[
\sum_a [x,a]\otimes a^\vee+a\otimes[x,a^\vee]=0,
\]
and both terms use the same normal-order rule with first index \(i\) and second index \(m+n-i\). Their scalar central parts instead give
\[
m\ell\sum_a
 \left(B(x,a)a^\vee_{m+n}
                +B(x,a^\vee)a_{m+n}\right)
=2m\ell x_{m+n}.
\tag{RC.M4}
\]
The first scalar contribution occurs at \(j=-m\); the second occurs at \(j=m+n\). The dual-basis identity proves the last equality.

For the remaining boundary term, expand the affine bracket:
\[
\sum_a [[x,a]_{j+m},a^\vee_{n-j}]
 =(A_x)_{m+n}
 +(j+m)\ell t_x\delta_{m+n,0}\operatorname{Id},
\quad
A_x=\sum_a [[x,a],a^\vee],\quad
t_x=\sum_a B([x,a],a^\vee).
\]
Here is the full finite Lie-algebra calculation:
\[
\begin{array}{c|ccc|c|c}
x&[[x,e],f]&[[x,f],e]&[[x,h],h/2]&A_x&t_x\\ \hline
e&0&2e&2e&4e&0\\
f&2f&0&2f&4f&0\\
h&2h&2h&0&4h&2-2=0
\end{array}
\qquad A_x=4x,\quad t_x=0.
\tag{RC.M5}
\]
For the \(e\) and \(f\) rows, each pairing defining \(t_x\) is zero because the form pairs only \(e\) with \(f\) and \(h\) with \(h\). Thus even when \(m+n=0\), no scalar boundary term survives.

Only finitely many indices cross the dividing point \(0\):
\[
\begin{array}{c|c|c|c}
m&\text{indices }j\text{ with a boundary term}
  &\theta(j+m)-\theta(j)&
        \sum_j\bigl(\theta(j+m)-\theta(j)\bigr)\\ \hline
m>0&-m,-m+1,\ldots,-1&1&m\\
m=0&\varnothing&0&0\\
m<0&0,1,\ldots,-m-1&-1&m
\end{array}
\tag{RC.M6}
\]
The table shows the mechanism: each boundary index contributes \(4x_{m+n}\) with the displayed sign. The boundary sum is \(4m x_{m+n}\).

For clarity about tails, fix a vector \(w\). Choose a cutoff containing the supports of (RC.M1) on both \(w\) and \(x_mw\), the supports of the two normally ordered Lie-bracket families in (RC.M3), the two scalar indices in (RC.M4), and the finite boundary interval (RC.M6). Each family is finite on \(w\), by the same rightmost-mode argument used for (RC.M1), with total index \(m+n\) for the Lie-bracket families. Inside this finite union all the preceding computations are ordinary finite algebra. Reindexing adds only terms already zero on \(w\). We have proved, for every pair of integers \(m,n\),
\[
\boxed{[x_m,S_n]=2(\ell+2)m\,x_{m+n}.}
\tag{RC.M7}
\]

At the critical level \(\ell=-2\), every \(S_n\) commutes with every mode. It also preserves each annihilation bound: if \(x_jw=0\) for \(j\ge N\), then \(x_jS_nw=S_nx_jw=0\) for those same indices. Consequently it commutes with a formal Laurent current as well: that current has a finite negative part, and its sufficiently high positive tail kills both \(w\) and \(S_nw\). The desired identity reduces to the already proved finite mode identities.

The quadratic operators commute with each other. Let \(S_p^{(L)}\) be a finite partial sum of (RC.M1). Every one of its terms is a product of modes, so it commutes with \(S_n\) at the critical level. Because \(w\) and \(S_nw\) have a common annihilation bound, choose \(L\) with
\(S_p^{(L)}w=S_pw\) and \(S_p^{(L)}S_nw=S_pS_nw\). Then
\[
S_nS_pw
=S_nS_p^{(L)}w
=S_p^{(L)}S_nw
=S_pS_nw,
\qquad [S_n,S_p]=0.
\tag{RC.M8}
\]
This proves commutativity of actual operators with a common finite tail cutoff.

#### 3.2.2. Translated vacuum vectors and their symbols

The translation operator on the vacuum can also be constructed directly. On the polynomial affine Lie algebra define
\[
D(x_m)=-m x_{m-1},\qquad D(K)=0.
\tag{RC.M9}
\]
It is a derivation. The Lie-mode part of
\([D(x_m),y_j]+[x_m,D(y_j)]\) is
\(-(m+j)[x,y]_{m+j-1}\), which equals the Lie-mode part of \(D([x_m,y_j])\). The possible central difference is
\[
-m(m+j-1)B(x,y)\delta_{m+j-1,0}K=0.
\]
The Leibniz rule therefore induces a derivation of the enveloping algebra: applying it to a relation \(xy-yx-[x,y]\) gives another such relation. The left ideal defining the vacuum is stable. Its generators are \(K-\ell\) and \(x_m\) for \(m\ge0\); the derivative of \(K-\ell\) and of \(x_0\) is zero, and \(D(x_m)=-m x_{m-1}\) still has nonnegative index when \(m\ge1\). Hence \(D\) descends to a linear operator \(T\) on \(V_\ell\) satisfying
\[
Tv=0,\qquad [T,x_m]=-m x_{m-1}.
\]
No vertex-algebra translation axiom is needed for this construction.

For \(n\ge-1\), each summand of \(S_n\) has a nonnegative rightmost mode and kills \(v\). If \(n=-r-2\), with \(r\ge0\), precisely the terms with both indices negative can survive. Thus
\[
S_nv=0\quad(n\ge-1),\qquad
Q_r:=S_{-r-2}v
 =\sum_{\substack{i,j\ge1\\i+j=r+2}}
 \left(\tfrac12 h_{-i}h_{-j}
            +e_{-i}f_{-j}+f_{-i}e_{-j}\right)v.
\tag{RC.M10}
\]
This is a finite sum with \(r+1\) index pairs, at every scalar level. In particular \(Q_0=Q\) of (K3.1).

An alternative exact expression records the lower ordered term. Since the two indices are negative, their bracket has no central part, and
\(f_{-i}e_{-j}=e_{-j}f_{-i}-h_{-(i+j)}\).
Reindexing the finite mixed sum gives
\[
Q_r=
\left[
 \sum_{i=1}^{r+1}
 \left(\tfrac12h_{-i}h_{-(r+2-i)}
                   +2e_{-i}f_{-(r+2-i)}\right)
 -(r+1)h_{-(r+2)}
\right]v.
\tag{RC.M11}
\]
The \(r+1\) commutators produce both the minus sign and the factor \(r+1\).

On negative modes, \(D(x_{-i})=i x_{-i-1}\), so
\(D^a(x_{-1})=a!x_{-a-1}\). Applying the Leibniz rule \(r\) times to a two-letter negative-mode word gives
\[
\frac{T^r}{r!}(x_{-1}y_{-1}v)
=\sum_{a+b=r}
 \frac{D^a(x_{-1})}{a!}
 \frac{D^b(y_{-1})}{b!}v
=\sum_{a+b=r}x_{-a-1}y_{-b-1}v.
\]
Apply this identity to the three terms of \(Q\). It proves
\[
\boxed{Q_r=\frac{T^rQ}{r!},\qquad
             TQ_r=(r+1)Q_{r+1}.}
\tag{RC.M12}
\]

There is a compatible operator identity on the entire vacuum. In differentiating a normal product, the only possible change of the first-mode ordering occurs at \(j=0\). Its derivative has coefficient \(-j=0\). Consequently
\[
[T,:a_jb_{n-j}:]
=-j:a_{j-1}b_{n-j}:
 -(n-j):a_jb_{n-j-1}:.
\]
This also follows by subtracting the two theta expressions in the proof of (RC.M3): the boundary coefficient is
\(-j(\theta(j-1)-\theta(j))=0\).
All the families are finite on a fixed vector, and on its image under \(T\), because the vacuum is smooth. Reindexing the first family by \(i=j-1\), the coefficients become \(-(i+1)\) and \(-(n-i)\). Therefore
\[
[T,S_n]=-(n+1)S_{n-1}.
\tag{RC.M13}
\]
At \(n=-r-2\), applying this formula to \(v\) reproduces the second identity in (RC.M12).

Filter the vacuum by negative-word length. The ordered basis proved in §3 identifies its associated graded space with
\(\operatorname{Sym}(t^{-1}\mathfrak g[t^{-1}])\): swapping generators changes a word by a shorter word, and ordered monomials remain independent in each graded piece. Let \(e_i,f_i,h_i\) denote the symbols of \(e_{-i},f_{-i},h_{-i}\), respectively, for \(i\ge1\). The degree-two symbol of the finite vector \(Q_r\) is exactly
\[
C_r:=\sigma_2(Q_r)
 =\sum_{\substack{i,j\ge1\\i+j=r+2}}
       \left(\tfrac12h_i h_j+2e_i f_j\right).
\tag{RC.M14}
\]
The \(h_1h_{r+1}\) coefficient is nonzero: it is \(1/2\) for \(r=0\) and \(1\) for \(r\ge1\). Hence every \(Q_r\) is nonzero. Here the length degree is always two; the sum of the positive mode indices is \(r+2\). These two gradings are distinct.

The first two coefficients display the translation and ordered correction concretely:
\[
\begin{array}{c|c|c}
r&Q_r& C_r\\ \hline
0&
 \bigl(\tfrac12h_{-1}^{\,2}+2e_{-1}f_{-1}-h_{-2}\bigr)v&
 \tfrac12h_1^{\,2}+2e_1f_1\\[2pt]
1&
 \bigl(h_{-1}h_{-2}
       +2e_{-1}f_{-2}+2e_{-2}f_{-1}-2h_{-3}\bigr)v&
 h_1h_2+2e_1f_2+2e_2f_1
\end{array}
\tag{RC.M15}
\]
The linear correction disappears in the length-two symbol, while the mode-index sum increases by one under translation.

At \(\ell=-2\), the operators
\(A_r=S_{-r-2}\) are affine-module endomorphisms, and their vacuum images are \(Q_r\). They are the endomorphisms attached to those vectors by (K2.3), since an endomorphism is determined by the image of the cyclic vector \(v\). Moreover \(S_n=0\) on the critical vacuum for \(n\ge-1\): it commutes with all modes and kills \(v\), hence kills every vector generated from \(v\). Equation (RC.M8) proves that all products of the \(A_r\) commute. It therefore defines a homomorphism
\[
k[z_0,z_1,\ldots]\longrightarrow
 \operatorname{End}_{\widehat{\mathfrak{sl}}_2}(V_{-2}),
\qquad z_r\longmapsto A_r.
\tag{RC.M16}
\]
Its construction proves a commuting algebra of vacuum endomorphisms. Algebraic independence, exhaustion of all vacuum endomorphisms, a center inside a specified completed enveloping algebra, and identification with functions on opers require further proofs. The finite normal-order calculation and translation construction above use only the affine-module foundations already proved in §3.

#### 3.2.3. The complete rank-one current-jet invariant algebra

Let \(k\) be a field of characteristic zero. Use
\[
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad [h,e]=2e,\quad[h,f]=-2f,\quad[e,f]=h.
\tag{RC.J1}
\]
For \(N\ge1\), put
\[
S_N=k[a_i,b_i,c_i:0\le i<N],\qquad
A(t)=\begin{pmatrix}a(t)&b(t)\\c(t)&-a(t)\end{pmatrix}
\in\mathfrak{sl}_2(S_N[t]/(t^N)),
\]
where \(a(t)=\sum_{i<N}a_it^i\), and similarly for \(b,c\). Define
\[
a(t)^2+b(t)c(t)=\sum_{i<N}q_it^i\pmod {t^N},\qquad
q_i=\sum_{j=0}^i\bigl(a_ja_{i-j}+b_jc_{i-j}\bigr).
\tag{RC.J2}
\]
The current algebra acts on coordinate functions by the derivations whose matrix-coordinate formula is
\[
D_{x,r}A_i=[A_{i-r},x],\qquad 0\le r<N,
\quad A_j=0\quad(j<0).
\tag{RC.J3}
\]
This is the differential of the usual action on functions by inverse adjoint substitution. In particular, it is a Lie action: on matrix coordinates the commutator of the two derivations sends \(A_i\) to
\([[A_{i-r-s},x],y]-[[A_{i-r-s},y],x]=[A_{i-r-s},[x,y]]\).
The opposite simultaneous sign convention has the same invariant kernels.

**Theorem (RC.J).** For every \(N\ge1\),
\[
S_N^{\mathfrak{sl}_2[t]/(t^N)}=k[q_0,\ldots,q_{N-1}],
\tag{RC.J4}
\]
and these \(N\) generators are algebraically independent. More generally, for every ordinary commutative \(k\)-algebra \(R\), the same invariant algebra is \(R[q_0,\ldots,q_{N-1}]\). For \(N=0\), both sides mean the coefficient ring with an empty generator list.

**Proof.** Since \(\operatorname{Tr}(A(t)^2)=2(a(t)^2+b(t)c(t))\), invariance of the trace gives
\[
D_{x,r}\operatorname{Tr}(A(t)^2)
=2\operatorname{Tr}\bigl(A(t)[A(t),x]t^r\bigr)=0
\pmod {t^N}.
\]
The cancellation uses only cyclic permutation inside the trace of matrices over a commutative ring. Thus every \(q_i\) is killed by every current derivation. We prove that there are no other polynomial invariants.

Invert \(b_0\). The truncated polynomial \(b(t)\) is now a unit, and
\[
c(t)=\frac{q(t)-a(t)^2}{b(t)}\pmod {t^N}.
\]
Consequently there is an isomorphism
\[
S_N[b_0^{-1}]
\cong
k[b_0^{\pm1},b_1,\ldots,b_{N-1},
  a_0,\ldots,a_{N-1},q_0,\ldots,q_{N-1}].
\tag{RC.J5}
\]
Here the \(q_i\) on the right are independent variables. To verify the isomorphism without presupposing their independence in \(S_N\), introduce those independent variables and solve recursively:
\[
c_i=b_0^{-1}\left(q_i-\sum_{j=0}^ia_ja_{i-j}
                  -\sum_{j=1}^ib_jc_{i-j}\right).
\tag{RC.J6}
\]
Substituting these expressions makes each coefficient of \(a^2+bc\) equal to the indicated independent \(q_i\). Conversely, applying the recursion to the original coefficients recovers each \(c_i\). These two substitutions are inverse homomorphisms.

The \(f\)-currents fix \(b(t)\) and \(q(t)\), and their matrix formula gives
\[
D_{f,r}a_i=b_{i-r},\qquad D_{f,r}c_i=-2a_{i-r}.
\]
Thus in the coordinates of (RC.J5),
\[
D_{f,r}=\sum_{i=r}^{N-1}b_{i-r}\frac{\partial}{\partial a_i}.
\tag{RC.J7}
\]
The coefficient matrix, with rows indexed by \(r\) and columns by \(i\), is upper triangular with every diagonal entry \(b_0\). It is invertible in the localized ring. Therefore its derivations span all the \(\partial/\partial a_i\) over that ring. If \(F\) is invariant, every one of these partial derivatives kills \(F\). A polynomial in the \(a_i\) over a characteristic-zero coefficient ring has all these partial derivatives zero only when it is independent of the \(a_i\): differentiating a monomial with a positive exponent multiplies its coefficient by a positive integer, which is a unit. We have proved
\[
F\in k[b_0^{\pm1},b_1,\ldots,b_{N-1},q_0,\ldots,q_{N-1}].
\tag{RC.J8}
\]

Next, the \(h\)-currents fix \(a(t)\) and \(q(t)\), and send \(b_i\) to \(-2b_{i-r}\). On the ring in (RC.J8), for \(1\le r<N\), they are
\[
D_{h,r}=-2\sum_{i=r}^{N-1}b_{i-r}\frac{\partial}{\partial b_i}.
\tag{RC.J9}
\]
Their matrix on the variables \(b_1,\ldots,b_{N-1}\) is again upper triangular, with diagonal entries \(-2b_0\). Hence invariance removes all these variables and leaves
\(F\in k[b_0^{\pm1},q_0,\ldots,q_{N-1}]\). There is no such step to perform when \(N=1\). Finally
\[
D_{h,0}F=-2b_0\frac{\partial F}{\partial b_0}.
\]
Write the remaining Laurent polynomial uniquely as
\(F=\sum_{j\in\mathbb Z}b_0^jF_j(q)\), with finite support. Its derivative is
\(-2\sum_jj b_0^jF_j(q)\). Independence of Laurent monomials and invertibility of every nonzero integer imply \(F_j=0\) for \(j\ne0\). Therefore the invariant algebra of the localized ring is precisely \(k[q_0,\ldots,q_{N-1}]\).

Localization is injective on \(S_N\), since \(b_0\) is a polynomial variable. Every invariant of \(S_N\) consequently equals a polynomial in the \(q_i\) already in \(S_N\). This proves (RC.J4). There is no need to extend an invariant across a divisor. For algebraic independence, specialize
\[
a_i=0\text{ for all }i,\qquad b_0=1,\qquad b_i=0\ (i>0).
\tag{RC.J10}
\]
Then \(q_i=c_i\). Any polynomial relation among the \(q_i\) would specialize to the same relation among the independent variables \(c_i\), so all its coefficients would be zero.

Every step also works over an ordinary \(k\)-algebra \(R\). The coordinate substitution is an algebraic recursion, \(b_0\) remains a non-zero-divisor in a polynomial ring over \(R\), and all nonzero integers remain units. Differentiating polynomial and Laurent monomials therefore has exactly the same kernel calculation, even when \(R\) has nilpotents. The specialization in (RC.J10) gives independence over \(R\) as well. \(\square\)

The following table records the successive kernels in the proof. The two triangular matrices have diagonal entries \(b_0\) and \(-2b_0\), respectively; the last operator kills every nonzero Laurent exponent. Its rows refer to (RC.J5), (RC.J7)–(RC.J9), and the \(h_0\) calculation.

| Operation | Remaining coordinate ring | Exact operator argument |
| --- | --- | --- |
| Invert the leading upper-right coefficient | \(k[b_0^{\pm1},b_1,\ldots,b_{N-1},a_0,\ldots,a_{N-1},q_0,\ldots,q_{N-1}]\) | Solve for the lower-left coefficients by (RC.J6). |
| Take the common kernel of the \(f\)-currents | \(k[b_0^{\pm1},b_1,\ldots,b_{N-1},q_0,\ldots,q_{N-1}]\) | The triangular matrix in (RC.J7) has diagonal \(b_0\). |
| Take the kernel of the positive \(h\)-currents | \(k[b_0^{\pm1},q_0,\ldots,q_{N-1}]\) | The triangular matrix in (RC.J9) has diagonal \(-2b_0\). |
| Take the remaining \(h_0\) kernel | \(k[q_0,\ldots,q_{N-1}]\) | The operator \(-2b_0\partial_{b_0}\) removes every nonzero Laurent exponent. |

The intermediate kernels need only the displayed \(f\) and \(h\) operators. The final ring is invariant under every current operator, including the \(e\)-currents, by the trace calculation. The table also holds with coefficient ring \(R\).

**All coefficients and formal currents.** Put
\[
S_\infty=\bigcup_{N\ge1}S_N
=k[a_i,b_i,c_i:i\ge0],\qquad
q(t)=a(t)^2+b(t)c(t)=\sum_{i\ge0}q_it^i.
\]
The inclusions preserve the previously defined \(q_i\). Each \(S_N\) is stable under the current derivations, and every \(x t^r\) with \(r\ge N\) acts by zero on it. Every polynomial belongs to some \(S_N\), so it is invariant under \(\mathfrak{sl}_2[t]\) exactly when it is invariant in that finite truncation. It follows that
\[
S_\infty^{\mathfrak{sl}_2[t]}
=S_\infty^{\mathfrak{sl}_2[[t]]}
=k[q_0,q_1,q_2,\ldots].
\tag{RC.J11}
\]
The formal-current action is defined on each polynomial by its finite truncation. Thus formal sums create no convergence condition or additional invariant. Algebraic independence of the infinite list means independence of every finite sublist, already proved by (RC.J10).

**The PBW symbol identification.** In the vacuum module of §3, the ordered negative-mode words give
\[
\operatorname{gr}_{\rm PBW}V_\ell
=\operatorname{Sym}\bigl(t^{-1}\mathfrak{sl}_2[t^{-1}]\bigr).
\tag{RC.J12}
\]
This is the associated-graded conclusion of the complete ordered-word proof in §3, also proved for arbitrary Lie algebras in [*The universal enveloping algebra and the Poincaré–Birkhoff–Witt theorem*, Theorem 2.1](../../RT-LIE/src/RT-LIE-13.md). The filtration counts negative-mode letters.

For \(m\ge0\), commute \(x_m\) through an ordered word. If the first bracket with \(y_{-j}\) is a negative mode, it replaces one letter by one letter. A central bracket removes that letter, and a nonnegative resulting mode must either kill the vacuum or be commuted through another negative letter, using at least one further bracket and producing a term with fewer letters. Hence the action preserves the PBW filtration, and its degree-preserving symbol is the derivation
\[
x_m\cdot y_{-j}=
\begin{cases}
[x,y]_{-(j-m)},&j>m,\\
0,&j\le m.
\end{cases}
\tag{RC.J13}
\]
In particular, this symbol action is independent of the level \(\ell\).

Use the invariant form \(B(e,f)=1\), \(B(h,h)=2\), with the remaining basis pairings zero, to identify a negative-mode symbol with a coordinate function by
\[
y_{-j}\longmapsto\bigl(A(t)\longmapsto B(y,A_{j-1})\bigr).
\tag{RC.J14}
\]
It is a linear isomorphism on the generator spaces, since \(B\) is nondegenerate, and hence an isomorphism of their polynomial algebras. Its indexing is also the residue identity
\(\operatorname{Res}_{t=0}B(y t^{-j},A(t))\,dt=B(y,A_{j-1})\).
Invariance and symmetry of \(B\) give
\[
B([x,y],A_{i-m})=B(y,[A_{i-m},x]).
\]
Thus (RC.J13) becomes exactly the coefficient action (RC.J3), including the shift \(i\mapsto i-m\). In coordinates,
\[
a_i=\tfrac12h_{-(i+1)},\qquad
b_i=f_{-(i+1)},\qquad c_i=e_{-(i+1)}.
\tag{RC.J15}
\]
Consequently the complete associated-graded invariant algebra is
\[
\bigl(\operatorname{gr}_{\rm PBW}V_\ell\bigr)^{\mathfrak{sl}_2[[t]]}
=k[q_0,q_1,\ldots],
\quad
q_i=\tfrac14\sum_{j=0}^i h_{-(j+1)}h_{-(i-j+1)}
     +\sum_{j=0}^i f_{-(j+1)}e_{-(i-j+1)}.
\tag{RC.J16}
\]
All products in this formula are commutative PBW symbols. The vector \(Q\) of §3.1 has symbol \(2q_0\), agreeing with its stated normalization. Each \(q_i\) has PBW degree two and loop grade \(i+2\), when \(y_{-j}\) has loop grade \(j\). In particular, every actual vacuum invariant has a highest PBW symbol in the ring (RC.J16). Lifting these symbols to vacuum invariants requires the further filtered argument; it is not part of the equality (RC.J16).

**Finite kernels and ordinary coefficient rings.** The coefficient-extension assertion can also be checked without localization. Give \(a_i,b_i,c_i\) polynomial degree one and loop grade \(i+1\). For each pair \((p,L)\), the space \(E_{p,L}\) of polynomials of degree \(p\) and loop grade \(L\) is finite-dimensional: only variables of weight at most \(L\) and finitely many monomials can occur. This holds in each \(S_N\) and in \(S_\infty\). The derivation \(D_{x,m}\) preserves \(p\) and lowers \(L\) by \(m\); all \(m\ge L\) act by zero. The invariant component is therefore the kernel of the finite linear map
\[
E_{p,L}\longrightarrow
\bigoplus_{x\in\{e,h,f\}}\ \bigoplus_{0\le m<L} E_{p,L-m},
\qquad F\longmapsto(D_{x,m}F)_{x,m}.
\tag{RC.J17}
\]
For a truncated ring the terms with \(m\ge N\) are zero and can be omitted. Constants have \(p=L=0\) and are the kernel of the empty map. Every ordinary \(k\)-algebra \(R\) is flat over \(k\). Tensoring this finite map is exact on its kernel, so its invariant component becomes \(R\otimes_k E_{p,L}^{\mathfrak{sl}_2[[t]]}\). The operators have fixed homogeneous shifts, which makes their common kernel bigraded, and every polynomial has finite homogeneous support. Summing these equalities proves
\[
(S_\infty\otimes_k R)^{\mathfrak{sl}_2(R)[[t]]}
=R[q_0,q_1,\ldots],
\tag{RC.J18}
\]
as well as the finite statement over \(R\). This proof treats arbitrary ordinary families and uses no test on geometric points.

For a finite direct sum of copies of \(\mathfrak{sl}_2\), apply the ordinary coefficient-ring statement to one factor at a time, taking the polynomial ring of the remaining factors as coefficients. The successive invariant kernels give the polynomial algebra on the lists \(q_i\) belonging to all factors. This establishes the current-jet invariant calculation for those products without an assertion about other simple types or about a full affine center.

#### 3.2.4. Polynomial independence and exhaustion of the vacuum center

We now use the proved operators and jet invariants to determine every vacuum endomorphism. Give the vacuum its PBW filtration: a negative-mode word with at most \(d\) factors has filtration degree at most \(d\). The ordered basis proved in §3 gives
\[
\operatorname{gr}V_{-2}
=\operatorname{Sym}\!\left(t^{-1}\mathfrak{sl}_2[t^{-1}]\right).
\tag{RC.P1}
\]
The nonnegative modes preserve the filtration. When commuting such a mode through a negative-mode word, an affine bracket replaces one factor by a single factor; a central term removes that factor. If the replacement is nonnegative, commuting it farther right only decreases the number of remaining factors. Consequently on (RC.P1) the action is the derivation
\[
x_m\cdot y_{-j}=
\begin{cases}[x,y]_{m-j},&j>m,\\0,&j\leq m,
\end{cases}
\qquad m\geq0.
\tag{RC.P2}
\]
The jet calculation of §3.2.3 uses precisely this action, via the displayed invariant pairing. Its polynomial invariants are the quadratic coefficients
\[
C_r=\sum_{i+j=r+2}\left(\tfrac12h_{-i}h_{-j}+2e_{-i}f_{-j}\right),
\qquad i,j\geq1,
\quad r\geq0.
\tag{RC.P3}
\]
These are algebraically independent. Indeed every finite initial list is the nonzero scalar multiple of the independent jet coefficients proved there; a relation in the infinite list would already involve a finite initial list.

Put \(Q_r=S_{-r-2}v\), as in §3.2.2. Its leading symbol is \(C_r\). Let \(A_r\) be its corresponding affine-module endomorphism. The operator calculation identifies \(A_r=S_{-r-2}\) on the vacuum, and proves that these endomorphisms commute. Thus there is an algebra map
\[
\Theta:k[z_0,z_1,\ldots]\longrightarrow
\operatorname{End}_{\widehat{\mathfrak{sl}}_2}(V_{-2}),
\qquad z_r\longmapsto A_r.
\tag{RC.P4}
\]
Here the polynomial ring consists of finite polynomials, rather than a completion.

The leading symbol of a product of the \(A_r\), evaluated at the vacuum, is the product of its corresponding \(C_r\). To see this without an infinite-mode multiplication argument, write \(Q_r=P_rv\) with \(P_r\) a polynomial in negative modes. For any negative-mode word \(Pv\), the induced-module formula (K2.3) gives
\(A_r(Pv)=P P_rv\). The ordered basis and its length filtration give
\(\sigma(PP_r)=\sigma(P)C_r\). Repeating proves the product assertion. In particular a nonzero polynomial of highest total degree \(d\) in the \(z_r\) has leading PBW symbol its degree-\(d\) part evaluated on the \(C_r\), in filtration degree \(2d\). Independence in (RC.P3) makes that symbol nonzero. Hence (RC.P4) is injective.

For surjectivity, let \(w\) be any vector killed by every nonnegative mode, with PBW degree \(d\). Its leading symbol is invariant under (RC.P2), so §3.2.3 expresses it as a polynomial in finitely many \(C_r\). Each \(C_r\) has PBW degree two. If \(d>0\), the homogeneous degree-\(d\) symbol therefore forces \(d\) to be even and is a homogeneous polynomial of total degree \(d/2\) in those coefficients. Apply the same polynomial in the \(A_r\) to \(v\) and subtract it from \(w\). The result is again an invariant vector and has strictly smaller PBW degree. For \(d=0\) it is a scalar multiple of \(v\). Induction terminates after finitely many steps and expresses every \(w\) as a finite polynomial in the \(A_r\), applied to \(v\). Formula (K2.3) then proves surjectivity. We have obtained the entire algebra
\[
\boxed{\operatorname{End}_{\widehat{\mathfrak{sl}}_2}(V_{-2})
=k[A_0,A_1,\ldots].}
\tag{RC.P5}
\]
It is commutative, its generators are independent, and the written argument excludes additional vacuum endomorphisms.

This assertion holds over every ordinary \(k\)-algebra \(R\). One can verify the base-change step by finite equations. Give a negative mode \(x_{-j}\) energy \(j\), and \(v\) energy zero. The energy-\(E\) space is finite-dimensional: only modes with \(j\leq E\) occur, and the number of length-weighted ordered words of total energy \(E\) is finite. The action of \(x_m\) has energy \(-m\). Thus all \(m>E\) kill that space, and its invariant subspace is the kernel of finitely many linear maps, using a basis of \(\mathfrak{sl}_2\) and \(0\leq m\leq E\). Tensoring that finite kernel with \(R\) is exact over the field \(k\). The vacuum is the direct sum of its energy spaces and every vector has finite energy support; its invariants therefore commute with this scalar extension. The induced-module endomorphism argument also holds over \(R\), since the ordered negative-mode basis is free over \(R\). The product identities in (RC.P4) are identities of operators, so
\[
\operatorname{End}_{\widehat{\mathfrak{sl}}_{2,R}}(V_{-2,R})
=R\otimes_k k[A_0,A_1,\ldots]
=R[A_0,A_1,\ldots].
\tag{RC.P6}
\]
Invariants here are killed by all modes, including the formal nonnegative series whose action was proved in §3. They are not defined by testing a selected set of reduced points. No derived invariant or completed-enveloping-algebra assertion follows merely from (RC.P6).

#### 3.2.5. The coordinate action and the projective-connection coefficient

We identify the exact coordinate action on this polynomial algebra. For \(l\geq-1\), the vector field \(t^{l+1}\partial_t\) gives a derivation of the affine algebra by
\[
D_l(x_m)=m x_{m+l},\qquad D_l(K)=0.
\tag{RC.C1}
\]
The affine bracket is preserved: the possible central contribution to the derivation identity is
\(m(m+n+l)B(x,y)\delta_{m+n+l,0}K=0\).
The nonnegative-mode subalgebra is preserved too; at \(l=-1\) the only apparently exceptional index has coefficient \(m=0\). Therefore \(D_lv=0\) extends (RC.C1) to the vacuum. Its commutator with translation is
\([D_l,T]=(l+1)D_{l-1}\) for \(l\geq0\), whereas \(D_{-1}=-T\).

The initial quadratic vector has the following actions, computed directly from its three terms:
\[
\begin{array}{c|ccccc}
l&-1&0&1&2&\geq3\\ \hline
D_lQ_0&-Q_1&-2Q_0&0&6v&0.
\end{array}
\tag{RC.C2}
\]
For \(l=1\), the first differentiated factor is a zero mode. Commuting it through the second factor produces the three bracket terms of the invariant quadratic tensor, whose sum is zero. For \(l=2\), those first factors are mode one. Each commutator then has a zero-mode bracket, which kills \(v\), and a central term. The pairings from the three summands are \(1,1,1\), so their total is \(-3\ell v=6v\) at \(\ell=-2\). Second differentiated factors already kill \(v\). For \(l\geq3\), the remaining index is positive and no central term is possible, so every term vanishes. The first two entries follow from translation and the energy of \(Q_0\).

Since \(TQ_r=(r+1)Q_{r+1}\), the commutator with \(T\) and (RC.C2) give, for every \(r\geq0\),
\[
D_lQ_r=
-\mathbf1_{r\geq l}(r+l+2)Q_{r-l}
+(l^3-l)\delta_{r,l-2}v,
\qquad l\geq-1.
\tag{RC.C3}
\]
The indicated term has an allowed index whenever its indicator is one. Here is the induction including its boundary terms. For \(l\geq0\), apply
\[
D_lQ_{r+1}
=\frac1{r+1}\bigl(TD_lQ_r+(l+1)D_{l-1}Q_r\bigr).
\]
When both ordinary terms occur, their coefficient is the negative of
\[
\frac{(r+l+2)(r-l+1)+(l+1)(r+l+1)}{r+1}
=r+l+3.
\]
At \(r=l-1\), only the second ordinary term occurs and gives \(-2(l+1)Q_0\), the required new boundary. Translation kills the scalar term. The scalar term from \(D_{l-1}Q_r\) occurs at \(r=l-3\) and has coefficient
\((l+1)(l-1)l=l^3-l\) after division by \(r+1=l-2\). Cases with \(l\leq2\) at this scalar boundary are already the initial entries in (RC.C2). For \(l=-1\), \(D_{-1}=-T\) gives the formula directly. These observations prove (RC.C3) for all indices.

The induced action on endomorphisms is by conjugation, and on their vacuum vectors is the displayed action. Indeed an affine derivation preserving the induction relations acts on \(V\); conjugating an affine-module map by a coordinate substitution is again an affine-module map. Infinitesimally, its commutator with \(D_l\) has vacuum image \(D_lQ_r\). Thus (RC.C3) gives the derivation on the generators \(A_r\) of (RC.P5).

By §§1.1.8 and 2.5, an ordinary \(PGL_2\)-oper on the formal disc has the unique coefficient
\[
\partial_t^2-q(t),\qquad q(t)=\sum_{r\geq0}q_rt^r.
\]
Its full ordinary coefficient functor is represented by the polynomial ring \(k[q_0,q_1,\ldots]\). For a coordinate substitution \(t=\phi(s)\), the scalar calculation in §2.9 gives
\[
\mathcal P_\phi(q)(s)
=\phi'(s)^2q(\phi(s))-\tfrac12\{\phi,s\},
\qquad
\{\phi,s\}=\frac{\phi'''}{\phi'}-
\frac32\left(\frac{\phi''}{\phi'}\right)^2.
\tag{RC.C4}
\]
To match the action on functions with current substitution, specify the contravariance explicitly. Current substitution sends \(xF(t)\) to \(xF(\phi(t))\). On the polynomial oper ring its corresponding action sends a function \(f\) to \(f\circ\mathcal P_{\phi^{-1}}\). At \(\phi(t)=t+\epsilon t^{l+1}\), \(\epsilon^2=0\), this action on the coefficients is
\[
\delta_lq_r=
-\mathbf1_{r\geq l}(r+l+2)q_{r-l}
+\tfrac12(l^3-l)\delta_{r,l-2}.
\tag{RC.C5}
\]
In fact the inverse is \(t-\epsilon t^{l+1}\); substituting it in (RC.C4) gives
\(-t^{l+1}q'-2(l+1)t^lq+\tfrac12(l+1)l(l-1)t^{l-2}\)
as the first variation. Reading its coefficient proves (RC.C5). This determines the normalization:
\[
A_r\longmapsto2q_r.
\tag{RC.C6}
\]
The factor two is the factor between our quadratic vector (K3.1) and the half-Casimir normalization. Formulas (RC.C3) and (RC.C5) agree under (RC.C6), including the scalar Schwarzian term.

These infinitesimal identities determine the full ordinary coordinate action, also over nonreduced coefficients. We give the integration step. A continuous coordinate substitution over an ordinary \(R\) has nilpotent constant coefficient and invertible linear coefficient, and its inverse was constructed in §1.1.8. It factors as a nilpotent translation followed, under substitution composition, by a pointed substitution. Translation acts on the vacuum by the finite exponential \(\exp(a_0D_{-1})\); it is finite because \(a_0\) is nilpotent. A scaling \(t\mapsto at\) acts on \(Q_r\) by \(a^{-r-2}\), exactly the action on \(2q_r\) in (RC.C6).

Every pointed substitution with linear coefficient one is a successively determined product of
\(\exp(c_nt^{n+1}\partial_t)\), \(n\geq1\). To prove existence, first match the coefficient of \(t^2\) using \(n=1\); composing with its inverse removes that coefficient. At step \(n\), all lower coefficients have already been removed, and the exponential has leading term \(t+c_nt^{n+1}\), so one uniquely chosen \(c_n\) removes the next coefficient. For any fixed coefficient only finitely many steps contribute, so the product and its inverse define the desired continuous substitution. The denominators in these exponentials are units over a characteristic-zero coefficient field. On the energy-\(E\) vacuum space, \(D_n\) decreases energy by \(n\), hence is locally nilpotent, and all \(n>E\) act by zero. Thus the same product acts by finitely many terms on every vacuum vector. The corresponding finite-jet polynomial operators on an oper coefficient have the same local nilpotence, as seen directly in (RC.C5). Equality of the infinitesimal derivations therefore gives equality of these exponentials; scaling and nilpotent translation give the remaining factors. This proves full equivariance from (RC.C3), rather than assuming that a Lie-algebra equality integrates.

Current substitution preserves the central line. For completeness, its residue identity is
\[
\operatorname{Res}_t\phi'(t)F(\phi(t))
=\operatorname{Res}_uF(u),\qquad F\in R((u)).
\tag{RC.C7}
\]
It suffices to check Laurent monomials, coefficient by coefficient, using the finite nilpotent substitution of §1.1.8. For \(u^a\) with \(a\ne-1\), the substituted differential is \(d(\phi^{a+1}/(a+1))\) and has residue zero. For \(a=-1\), write \(\phi=(t-b)u(t)\), with \(b\) nilpotent and \(u(t)\) a power-series unit. The nilpotent root and this factorization follow from the inverse-coordinate construction there; dividing by \(t-b\) is finite coefficientwise. Then \(\phi'/\phi=1/(t-b)+u'/u\). The first term has residue one, by its finite negative-power expansion, while the second is a power series. This proves (RC.C7), and hence invariance of the cocycle \(\operatorname{Res}((dF)G)B(x,y)\). The vacuum relations are preserved because substitution preserves \(R[[t]]\). Its induced action and the oper action obey the same substitution composition law, so the preceding integration proves equivariance for every continuous ordinary coordinate substitution.

The calculation can be read as the following commuting square:
\[
\begin{array}{ccc}
k[A_0,A_1,\ldots]&\xrightarrow{\ A_r\mapsto2q_r\ }&k[q_0,q_1,\ldots]\\
{\scriptstyle D_l}\downarrow&&\downarrow{\scriptstyle\delta_l}\\
k[A_0,A_1,\ldots]&\xrightarrow{\ A_r\mapsto2q_r\ }&k[q_0,q_1,\ldots].
\end{array}
\tag{RC.C8}
\]
*The left vertical map is the current-coordinate derivation (RC.C3); the right map is the inverse-coordinate action on projective-connection functions (RC.C5). Their scalar terms agree precisely with the factor two in (RC.C6). The exponential and nilpotent-translation argument extends the square to every ordinary coordinate substitution.*

Combining (RC.P5), (RC.P6) and (RC.C6) proves the coordinate-independent rank-one vacuum-center isomorphism
\[
\operatorname{End}_{\widehat{\mathfrak{sl}}_{2,R}}(V_{-2,R})
\simeq R[\operatorname{Op}_{PGL_2}(D_R)]
\tag{RC.C9}
\]
for every ordinary parameter algebra, with the exact current cocycle and scalar-oper convention of this lesson. The proof supplies all generators, their independence, exhaustion and coordinate action. It does not supply the analogous higher-rank lifting theorem, the completed-enveloping-algebra center on the punctured disc, chiral or Satake compatibility, or a derived-family center. Those remain the additional scopes of §4.


### 3.3. General current invariants and the quantum-lifting problem

#### 3.3.1. Invariants of split semisimple current jets

Let \(k\) be a characteristic-zero field and \(\mathfrak g\) a split semisimple Lie algebra of rank \(\ell\). Fix homogeneous polynomial generators \(P_1,\ldots,P_\ell\) of its adjoint infinitesimal invariant ring. Their existence and the polynomial principal section are the inputs proved in §1.2 of [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), at its explicitly retained root/pinning and invariant-polynomial foundations. We explain the extension from an algebraically closed field below.

For \(N\ge1\), put \(\mathfrak g_N=\mathfrak g\otimes_k k[t]/(t^N)\), write \(A(t)=\sum_{s=0}^{N-1}A_st^s\), and define the coefficient polynomials by
\[
P_i(A(t))=\sum_{r=0}^{N-1}p_{i,r}(A)t^r
                       \pmod{t^N}.
\]
We will prove, including algebraic independence,
\[
\boxed{
k[\mathfrak g_N]^{\mathfrak g_N}
 =k[p_{i,r}:1\le i\le\ell,\ 0\le r<N].
}
\tag{GJ.1}
\]
The invariant notation denotes kernels of Lie derivations. Choose a basis \(y_a\) of \(\mathfrak g\), and let \(x_{a,s}\) be the corresponding linear coordinate functions of \(A_s\). With the usual contragredient sign, the action is
\[
\delta_{y,r}F(A)
=-dF_A([yt^r,A(t)]\bmod t^N),\qquad
\delta_{y,r}x_{a,s}
=\begin{cases}
-([y,A_{s-r}])_a,&s\ge r,\\
0,&s<r.
\end{cases}
\tag{GJ.2}
\]
Extend by the polynomial Leibniz rule. Jacobi, applied to these linear coordinates, gives
\([\delta_{x,r},\delta_{y,s}]=\delta_{[x,y],r+s}\), with indices at least \(N\) acting by zero. Thus (GJ.2) is precisely a Lie action, and its common kernel for a basis and \(0\le r<N\) is the ring in (GJ.1).

The written finite-string decomposition of §1.1.2 and its whole-module consequence (IS.A6) give a principal triple \((e,h,f)\) and
\[
V=\mathfrak g^e,\qquad
\mathfrak g=[f,\mathfrak g]\oplus V,\qquad
\Sigma=f+V,\qquad
\operatorname{res}_\Sigma:
 k[\mathfrak g]^{\mathfrak g}\xrightarrow{\sim}k[\Sigma].
\tag{GJ.3}
\]
Here \(\dim V=\ell\). The last isomorphism is (IS.A14): §§1.2.3–1.2.4 construct its polynomial inverse by the positive-weight blocks. We use that actual inverse. A homogeneous basis \(v_j\) of \(V\) has heights \(d_j\), and the slice coordinate \(z_j\) has positive weight \(d_j+1\).

These inputs hold over the present split field. The split root decomposition, pinning relations, integral root/coroot pairings, and their scalar-extension compatibility retain the structural premises named in §§1.1.1 and 1.2.1. The principal triple formulas are over this pinning, and the finite-string proof divides only by nonzero integers, so it works over \(k\). To descend the restriction isomorphism, extend to an algebraic closure \(\bar k\). In every ordinary polynomial degree, infinitesimal invariants are the kernel of finitely many linear maps between finite-dimensional \(k\)-spaces. Choosing bases for a kernel and a complementary subspace shows that tensoring this kernel with \(\bar k\) preserves it. Taking the direct sum of degrees gives
\[
\bar k\otimes_k k[\mathfrak g]^{\mathfrak g}
 =\bar k[\mathfrak g_{\bar k}]^{\mathfrak g_{\bar k}}.
\tag{GJ.4}
\]
Also \(\bar k\otimes V=\ker(\operatorname{ad}e_{\bar k})\). Restriction over \(k\) therefore becomes the isomorphism (GJ.3) over \(\bar k\), established by the stated split root model and the written principal-section proof. Its kernel and cokernel vanish over \(k\): a nonzero vector remains nonzero after extending a basis to \(\bar k\). This descends the isomorphism itself.

It also supplies homogeneous generators over \(k\). Define \(\lambda(a)|_{\mathfrak g_m}=a^m\operatorname{Id}\). Brackets add heights, so this is a Lie automorphism. An infinitesimal invariant is fixed by it, since its finite weight decomposition is killed by the derivative \(h/2\), and a nonzero integer weight is invertible in \(k\). The action \(x\mapsto a\lambda(a)x\) therefore makes restriction carry ordinary degree \(D\) to slice weight \(D\), as in (IS.A7). Decompose the inverse image of \(z_j\) into ordinary homogeneous components. Their restrictions lie in distinct weights, so only the component of degree \(d_j+1\) remains; injectivity of restriction kills the others. These inverse images are homogeneous generators over \(k\). Any other polynomial generator list also makes restriction a polynomial coordinate isomorphism. This proves the field range used in (GJ.1), without an embedding of \(k\) into \(\mathbb C\).

Form the affine jet section
\[
\Sigma_N=f+V\otimes_k k[t]/(t^N),\qquad
\chi_N=(p_{i,r}):\mathfrak g_N\longrightarrow\mathbb A_k^{\ell N}.
\]
The section isomorphism has a polynomial inverse over \(k\). Evaluate both polynomial maps in any ring \(R[t]/(t^N)\), for an ordinary \(k\)-algebra \(R\), and take coefficients. Their composition identities remain identities. Consequently
\[
\chi_N|_{\Sigma_N}:\Sigma_N
       \xrightarrow{\sim}\mathbb A_k^{\ell N}
\tag{GJ.5}
\]
is a polynomial isomorphism, natural over every such \(R\).

Each \(p_{i,r}\) is invariant. The classical infinitesimal identity
\(dP_i(A)([y,A])=0\) is a polynomial identity, so it may be evaluated in \(k[t]/(t^N)\). The variation generated by \(yt^r\) gives
\[
\delta_{y,r}P_i(A(t))
=-t^r dP_i(A(t))([y,A(t)])=0.
\]
Taking its coefficients proves the assertion.

We next construct enough conjugations to detect every polynomial on \(\mathfrak g_N\). For each root \(\alpha\), the operator \(\operatorname{ad}y_\alpha\) is nilpotent: repeated application moves a root weight successively by \(\alpha\), through a finite set of weights. Its exponential
\(\exp(c\,\operatorname{ad}y_\alpha)\) is therefore a finite polynomial in \(c\), acting coefficientwise on \(\mathfrak g_N\). For every \(1\le r<N\) and every basis vector \(y_a\), the operator
\(D=t^r\operatorname{ad}y_a\) is nilpotent because \(D^q=0\) when \(rq\ge N\). Its exponential is again finite. These are Lie automorphisms: induction from the derivation rule gives
\(D^n[u,v]=\sum_{i+j=n}\binom ni[D^iu,D^jv]\); summing with coefficients \(c^n/n!\) proves bracket preservation. The binomial identity likewise gives
\(\exp(cD)\exp(c'D)=\exp((c+c')D)\), and the inverse is \(\exp(-cD)\).

For the degree-zero Cartan directions, use the simple coroots \(h_i\). Define \(\tau_i(z)\) to fix the Cartan and multiply the root line \(\mathfrak g_\alpha\) by \(z^{\alpha(h_i)}\), for an invertible parameter \(z\). Integral pairings make this a Laurent-polynomial cocharacter. Root weights add under brackets, so it is a Lie automorphism, and its differential at \(z=1\) is \(\operatorname{ad}h_i\). This constructs the required adjoint torus factors explicitly.

An invariant \(F\) is fixed by every one of these factors. For a nilpotent exponential factor, the polynomial \(p(c)=F(\exp(cD)A)\) satisfies
\[
p'(c)=-(\delta_{y,r}F)(\exp(cD)A)=0,
\qquad p(c)=p(0).
\tag{GJ.6}
\]
The last step holds coefficientwise: every positive integer multiplying a polynomial coefficient is a unit in a characteristic-zero field. For a Cartan factor, decompose \(F\) into its finitely many integer-weight components. The equation \(\delta_{h_i,0}F=0\) kills every component with nonzero \(i\)-th weight, so \(\tau_i(z)\) fixes the remaining components. These arguments are polynomial or Laurent-polynomial identities in all parameters. They integrate each required current derivation in ordinary families, including families with nilpotents.

Choose an order for all these factors. Let \(\mathcal U_N\) have one affine parameter per degree-zero root factor, one parameter \(u_i\) per torus factor \(\tau_i(1+u_i)\), and one parameter per factor \(\exp(c_{r,a}t^r\operatorname{ad}y_a)\). Invert \(\prod_i(1+u_i)\). Write \(\Gamma_N\) for their finite ordered product and define
\[
\mu_N:\mathcal U_N\times\Sigma_N\longrightarrow\mathfrak g_N,
\qquad (c,s)\longmapsto\Gamma_N(c)s.
\tag{GJ.7}
\]
The distinguished parameter point is zero, where every factor is the identity, and the distinguished slice point is \(f\). The tangent directions are completely specified:
\[
\begin{array}{c|c|c}
\text{parameter}&\text{tangent vector in the factors}
                         &d\mu_N\text{ at }(0,f)\\ \hline
c_\alpha&y_\alpha&[y_\alpha,f]\\
u_i&h_i&[h_i,f]\\
c_{r,a},\ 1\le r<N&y_at^r&[y_a,f]t^r\\
z_{j,s},\ 0\le s<N&v_jt^s&v_jt^s
\end{array}
\tag{GJ.8}
\]
The first two rows span the degree-zero Lie directions, and the third row spans every positive current degree. Thus the differential has image
\([\mathfrak g_N,f]+V\otimes k[t]/(t^N)=\mathfrak g_N\), by (GJ.3).

Here is the full dominance argument. Choose \(\dim\mathfrak g_N=N\dim\mathfrak g\) linear parameter directions on which that differential is invertible. Restrict the parameters to their linear span and to the open set containing zero where the torus denominators stay invertible. The resulting substitution has the formal expansion
\[
\Psi(q)=f+Jq+\text{terms of total degree at least two},
\qquad J\in\operatorname{GL}_{N\dim\mathfrak g}(k).
\tag{GJ.9}
\]
Formal expansions of all denominators exist because their constant terms are one. If a nonzero polynomial \(H\) on \(\mathfrak g_N\) vanished after \(\mu_N\), it would vanish after \(\Psi\). Let \(H_b(Y)\) be the lowest nonzero homogeneous term of \(H(f+Y)\). The lowest substituted term is \(H_b(Jq)\), which is nonzero because invertible linear substitution is an automorphism of the polynomial ring. This is a contradiction. Therefore \(\mu_N^*\) is injective. This proves dominance by polynomial coefficients and finite tangent directions.

The coefficient and conjugation maps fit into the following square:
\[
\begin{array}{ccc}
\mathcal U_N\times\Sigma_N&\xrightarrow{\ \mu_N\ }&\mathfrak g_N\\
{\scriptstyle\operatorname{pr}_{\Sigma_N}}\downarrow
 &&\downarrow{\scriptstyle\chi_N=(p_{i,r})}\\
\Sigma_N&\xrightarrow[\text{polynomial isomorphism}]
                    {\ \chi_N|_{\Sigma_N}\ }&\mathbb A_k^{\ell N}.
\end{array}
\tag{GJ.10}
\]
*The upper map is the finite root, torus and positive-current word (GJ.7). Its tangent directions (GJ.8) prove injective polynomial pullback by (GJ.9). The lower map is the coefficientwise polynomial inverse (GJ.5); invariance makes the square commute in every ordinary family.*

Now let \(F\in k[\mathfrak g_N]^{\mathfrak g_N}\). By (GJ.5), its restriction to \(\Sigma_N\) is a unique polynomial \(G\) in the restrictions of the \(p_{i,r}\). The difference
\(H=F-G(p_{i,r})\) is invariant and restricts to zero. Integration of the factors gives
\(H\circ\mu_N=H\circ\operatorname{pr}_{\Sigma_N}=0\).
Injectivity of \(\mu_N^*\) makes \(H=0\). This proves generation. If \(G(p_{i,r})=0\), restriction to the polynomial coordinate isomorphism (GJ.5) gives \(G=0\). This proves algebraic independence and completes (GJ.1).

We give the coefficient-base argument through finite equations. Give \(x_{a,s}\) polynomial degree \(1\) and energy \(s+1\). The fixed bidegree space \(B_{d,E}\) is finite-dimensional, even when all indices \(s\ge0\) are permitted: only variables with \(s+1\le E\) can occur, and each monomial has exactly \(d\) factors. The derivation \(\delta_{y,r}\) preserves degree and lowers energy by \(r\). It is zero on that space for \(r>E\). For finite \(N\), put \(q=\min(E,N-1)\). The invariant part of a bidegree space is therefore
\[
\ker L_{d,E},\qquad
L_{d,E}:B_{d,E}\longrightarrow
 \bigoplus_a\bigoplus_{r=0}^{q}B_{d,E-r},
\qquad F\longmapsto(\delta_{y_a,r}F)_{a,r}.
\tag{GJ.11}
\]
Negative-energy spaces are zero. All spaces and maps in (GJ.11) are finite over \(k\). Bases of the kernel and image, extended to bases of the domain and target, show that for every ordinary \(k\)-algebra \(R\),
\(\ker(R\otimes L_{d,E})=R\otimes\ker L_{d,E}\).
The maps after tensoring are exactly the relative current derivations over \(R\).

Every polynomial is a finite sum of bidegree components. For a fixed \(r\), different bidegrees go to different bidegrees, so invariance holds componentwise. Taking their direct sum, and then using (GJ.1), proves the natural algebra isomorphism
\[
R[\mathfrak g_N\otimes_kR]^{\,\mathfrak g_N\otimes_kR}
 =R\otimes_k k[\mathfrak g_N]^{\mathfrak g_N}
 =R[p_{i,r}:1\le i\le\ell,\ 0\le r<N].
\tag{GJ.12}
\]
In particular the displayed generators are polynomial coordinates over nonreduced \(R\) as well.

Finally let \(B_\infty=k[x_{a,s}:s\ge0]\), the polynomial coordinate ring of the coefficient functor \(A(t)\in\mathfrak g[[t]]\). Each polynomial belongs to some \(B_N=k[\mathfrak g_N]\). That subring is stable under every current derivation, and all modes \(yt^r\) with \(r\ge N\) act by zero on it. Its invariant condition is consequently exactly its finite-jet invariant condition. A formal current acts on a given polynomial through a finite truncation, so polynomial and formal currents have the same invariants. Hence
\[
\boxed{
B_\infty^{\,\mathfrak g[t]}
 =B_\infty^{\,\mathfrak g[[t]]}
 =k[p_{i,r}:1\le i\le\ell,\ r\ge0],
\qquad
(R\otimes B_\infty)^{\,\mathfrak g_R[[t]]}
 =R[p_{i,r}:1\le i\le\ell,\ r\ge0].
}
\tag{GJ.13}
\]
Every finite list of generators occurs in a finite jet ring, so it is algebraically independent. The coefficient \(p_{i,r}\), for \(P_i\) homogeneous of degree \(D_i\), has bidegree \((D_i,D_i+r)\): its monomials have \(D_i\) factors and their coefficient indices sum to \(r\). Thus the finite kernels (GJ.11), with \(q=E\), also give a direct base-change proof for the infinite polynomial ring.

For \(N=0\) the jet Lie algebra is zero and the ring is \(k\); for the zero semisimple Lie algebra the same assertion holds for every \(N\), with an empty generator list. For products, the principal triples and slices are direct sums, and the factor generator lists concatenate. The proof above applies to that whole direct sum and gives the product assertion over every ordinary base.

This is a classical polynomial-current theorem from the actual principal decomposition and polynomial-section proofs. Their retained split-root, rational-model and invariant-polynomial foundations remain those specified in §§1.1.1 and 1.2.1. No higher-rank quantum central lift, PBW exhaustion of a quantum center, completed-center comparison or full Feigin–Frenkel theorem is inferred from this invariant-ring calculation.

#### 3.3.2. General PBW symbols, ordinary families and coordinates

Let \(\mathfrak g\), the homogeneous basic invariants \(P_i\) of degrees \(D_i\), and the jet coefficients \(p_{i,r}\) have the hypotheses and notation of §3.3.1. Fix any invariant symmetric form \(\kappa\), and form the affine algebra with
\[
[x_m,y_n]=[x,y]_{m+n}
 +m\kappa(x,y)\delta_{m+n,0}K.
\]
Let \(V_\kappa\) be its vacuum with \(Kv=v\) and \(\mathfrak g[[t]]v=0\). This includes the critical form \(\kappa=-\tfrac12\operatorname{Kil}\); for the rank-one normalization of §3.2 it is \(-2B\). The ordered-word and smoothness proofs in §3 apply to this bracket without changing their arguments. We do not assume that \(\kappa\) is nondegenerate. Choose a separate nondegenerate invariant pairing \(B\) on the split semisimple Lie algebra to identify its dual; its existence is among the same semisimple Lie foundations used in §§1.1–1.2.

Put
\[
Z_\kappa=\operatorname{End}_{\widehat{\mathfrak g}_\kappa}(V_\kappa)
 \simeq V_\kappa^{\mathfrak g[[t]]},\qquad
F_dZ_\kappa=Z_\kappa\cap F_dV_\kappa.
\tag{GJ.P1}
\]
Here the intersection means the image of an endomorphism at the vacuum. The filtration on \(V_\kappa\) counts negative-mode letters. The induced-module proof (K2.3) establishes the correspondence in (GJ.P1): an invariant \(w\) gives the map \(uv\mapsto uw\), and every endomorphism is determined by its vacuum image.

The nonnegative modes preserve this filtration. In commuting \(x_m\), \(m\geq0\), through a word, a first negative bracket replaces one letter. A central bracket removes that letter. If a bracket produces a nonnegative mode, it either kills the vacuum or requires a further bracket and hence gives a shorter word. The degree-preserving action on the associated graded is therefore
\[
\operatorname{gr}V_\kappa
 =\operatorname{Sym}(t^{-1}\mathfrak g[t^{-1}]),\qquad
x_m\cdot y_{-j}=
\begin{cases}[x,y]_{m-j},&j>m,\\0,&j\leq m.
\end{cases}
\tag{GJ.P2}
\]
The form \(\kappa\) has disappeared from this symbol action, because its terms decrease the number of letters.

Identify a symbol \(y_{-j}\) with the function
\(A(t)\mapsto B(y,A_{j-1})\), where
\(A(t)=\sum_{a\geq0}A_at^a\). The pairing is nondegenerate, so this is an isomorphism of polynomial algebras. Invariance of \(B\) gives
\[
B([x,y],A_{j-m-1})=B(y,[A_{j-m-1},x]).
\]
Thus (GJ.P2) is exactly the current derivation
\(A_a\mapsto[A_{a-m},x]\) used in §3.3.1. In particular, the leading symbol of every vacuum invariant belongs to the polynomial algebra proved there. There is an injective map of graded algebras
\[
\boxed{\operatorname{gr}_F Z_\kappa
 \hookrightarrow
 \bigl(\operatorname{gr}V_\kappa\bigr)^{\mathfrak g[[t]]}
 =k[p_{i,r}:1\leq i\leq\ell,\ r\geq0].}
\tag{GJ.P3}
\]
We justify both “injective” and “algebras.” The kernel of the map from an invariant of degree at most \(d\) to its degree-\(d\) symbol consists exactly of invariants of degree at most \(d-1\), giving injectivity. If \(w=P_wv\), with \(P_w\) a finite polynomial in negative modes, the endomorphism corresponding to \(w\) sends \(P_zv\) to \(P_zP_wv\). This product has degree at most the sum of the two degrees, and its top symbol is the product of their symbols in the commutative algebra (GJ.P2). The filtration is therefore multiplicative and the symbol map is an algebra map. In particular the associated graded algebra is commutative. Equation (GJ.P3) alone does not prove that the unfiltered algebra is commutative, or that this inclusion is surjective.

Give \(y_{-j}\) energy \(j\). Each energy-\(E\) space of the vacuum is finite-dimensional: it involves only the finitely many modes with \(j\leq E\), and only finitely many ordered words whose positive indices add to \(E\). The mode \(x_m\) has energy shift \(-m\). This follows directly from the affine bracket: a negative replacement subtracts \(m\) from the energy, and a central replacement is possible only when the removed indices add to \(m\). Hence \(m>E\) kills that energy space. For any ordinary \(k\)-algebra \(R\), each invariant energy space after extension is the kernel of the finite map
\[
(V_\kappa)_E\otimes_k R\longrightarrow
 \bigoplus_{x\in\mathcal B}\ \bigoplus_{0\leq m\leq E}
 (V_\kappa)_{E-m}\otimes_k R,
\qquad w\longmapsto(x_mw)_{x,m},
\tag{GJ.P4}
\]
where \(\mathcal B\) is a basis of \(\mathfrak g\). All vector spaces in this formula are finite-dimensional. Tensor over \(k\) is exact on its kernel. Invariance is energy graded, since for a fixed \(m\) the outputs of distinct input energies have distinct energies. Every vector has finite energy support. The ordered negative-mode basis remains free over \(R\), so the induced-module endomorphism argument also holds over \(R\). Summing the finite-kernel equalities gives, as algebras,
\[
Z_{\kappa,R}=R\otimes_k Z_\kappa.
\tag{GJ.P5}
\]
The same finite map restricted to the letter-length filtration proves
\(F_dZ_{\kappa,R}=R\otimes_k F_dZ_\kappa\). Consequently the associated graded inclusion in (GJ.P3) also extends to every ordinary \(R\), including nonreduced rings. Formal nonnegative series impose precisely the same equations: on an energy-bounded vector their tails vanish. No completed Hom, derived invariant or pointwise criterion was substituted for this argument.

**Translation.** On the affine algebra the rule
\[
T(x_m)=-m x_{m-1},\qquad T(K)=0
\tag{GJ.P6}
\]
is a derivation. The central difference in its bracket identity is
\(-m(m+n-1)\kappa(x,y)\delta_{m+n-1,0}K=0\).
It preserves the vacuum relations: \(T(x_0)=0\), and for \(m\geq1\) the index \(m-1\) is still nonnegative. Thus \(Tv=0\) defines an operator on the vacuum satisfying \([T,x_m]=-m x_{m-1}\). If \(w\) is invariant, then
\(x_mTw=T x_mw+m x_{m-1}w=0\) for every \(m\geq0\); the exceptional index at \(m=0\) has zero coefficient. Translation preserves invariants and their length filtration and raises energy by one.

On symbols, \(TA_a=(a+1)A_{a+1}\). Its formal exponential therefore sends
\[
\exp(sT)A_0=\sum_{a\geq0}A_as^a=A(s).
\]
The Leibniz rule makes this exponential multiplicative, coefficient by coefficient. Applied to \(P_i(A_0)\), it proves
\[
p_{i,r}=\frac{T^r}{r!}p_{i,0},\qquad
Tp_{i,r}=(r+1)p_{i,r+1}.
\tag{GJ.P7}
\]
All identities are identities of individual polynomial coefficients. The letter length of \(p_{i,r}\) is \(D_i\), and its energy is \(D_i+r\). These two gradings should not be identified.

**The coordinate action on symbols.** Let \(\phi\) be a continuous coordinate substitution over an ordinary \(R\), including a nilpotent constant coefficient, and write \(\psi=\phi^{-1}\). The inverse and coefficientwise finite substitutions were proved in §1.1.8. Substitution sends \(xF(t)\) to \(xF(\phi(t))\). It preserves the affine cocycle: the proof of (RC.C7) uses only residues of Laurent monomials and therefore applies to any \(\kappa\). It also preserves \(\mathfrak g_R[[t]]\). The formula
\(U_\phi(uv)=\sigma_\phi(u)v\) consequently gives an invertible map of the vacuum: the defining induction relations are respected, and every formal current appearing in a substituted finite word acts through a finite truncation. Its inverse is \(U_\psi\).

These maps preserve the letter filtration. A substituted generator is linear in modes; positive modes that occur in a substituted negative word can be commuted to the right, where each extra bracket or central term decreases its length. The inverse has the same property. On the associated graded, only the negative part of a substituted generator remains. Its pairing with \(A(t)\,dt\) is
\[
\begin{split}
\operatorname{Res}_t B(y,A(t))\phi(t)^{-j}\,dt
 &=\operatorname{Res}_u
 B\bigl(y,\psi'(u)A(\psi(u))\bigr)u^{-j}\,du.
\end{split}
\tag{GJ.P8}
\]
This is the residue-change identity, with the inverse substitution specified. Thus current substitution on polynomial functions corresponds to inverse pullback of the Lie-algebra-valued one-form.

Homogeneity of \(P_i\) gives the full transformation rule
\[
P_i(A(t))\longmapsto
 \psi'(t)^{D_i}P_i(A(\psi(t))).
\tag{GJ.P9}
\]
Its coefficient formulas are finite on each polynomial, also for a nilpotent translation: only finitely many additional Taylor coefficients can occur before a power of the nilpotent constant vanishes. The invariant algebra and the inclusion (GJ.P3) are therefore stable under every such coordinate change. At
\(\phi(t)=t+\epsilon t^{l+1}\), \(\epsilon^2=0\), the inverse variation gives
\[
\delta_l p_{i,r}
 =-\mathbf1_{r\geq l}
 \bigl(r+D_i+(D_i-1)l\bigr)p_{i,r-l},
\qquad l\geq-1.
\tag{GJ.P10}
\]
Indeed the variation of the series is
\(-t^{l+1}(P_i(A))'-D_i(l+1)t^lP_i(A)\); reading its coefficient proves the formula. At \(l=-1\) it is \(-(r+1)p_{i,r+1}\), agreeing with translation. At \(l=0\) it is the negative energy weight \(-(r+D_i)\). For \(D_i=2\), it is the leading quadratic part of (RC.C3). The scalar Schwarzian term there has lower letter degree and is consequently absent from the symbol formula.

The maps and the ordinary-family boundary are displayed in the following square:
\[
\begin{array}{ccc}
\operatorname{gr}_F Z_{\kappa,R}&\hookrightarrow&R[p_{i,r}]\\
{\scriptstyle\operatorname{gr}U_\phi}\downarrow&&
 \downarrow{\scriptstyle P_i(A)\mapsto\psi'^{D_i}P_i(A\circ\psi)}\\
\operatorname{gr}_F Z_{\kappa,R}&\hookrightarrow&R[p_{i,r}].
\end{array}
\tag{GJ.P11}
\]
*The horizontal arrows are the proved symbol inclusion (GJ.P3), extended by the finite equations (GJ.P4)–(GJ.P5). The right vertical arrow is inverse pullback of degree-\(D_i\) differential coefficients, proved by the residue pairing (GJ.P8). The square does not assert surjectivity of the horizontal arrows or the full coordinate law of quantum generators.*

#### 3.3.3. Algebraic reconstruction and commutativity of the general vacuum center

Let \(k\) be a field of characteristic zero, let \(\mathfrak g\) be finite-dimensional, and let \(B\) be an invariant symmetric bilinear form. Fix a scalar level \(\ell\). We use the affine bracket and vacuum of §3:
\[
[x_m,y_n]=[x,y]_{m+n}+m\ell B(x,y)\delta_{m+n,0}\operatorname{Id},
\qquad \mathfrak g[t]v=0.
\tag{VC.1}
\]
The ordered-word proof identifies \(V_\ell\) with
\(U(t^{-1}\mathfrak g[t^{-1}])v\). Every state is a finite linear combination of finite negative-mode words; the sum of their positive mode indices gives an annihilation bound for sufficiently high currents. Thus all states have finite energy in this algebraic sense. The full formal-current action and the bijection
\[
\operatorname{End}_{\widehat{\mathfrak g}}(V_\ell)
\longrightarrow V_\ell^{\mathfrak g[[t]]},\qquad E\longmapsto Ev,
\tag{VC.2}
\]
are the proved induction and smoothness statements of §3. The translation constructed in §3.2.2 works for this general bracket as well:
\[
Tv=0,\qquad [T,x_m]=-m x_{m-1}.
\tag{VC.3}
\]
Indeed \(D(x_m)=-m x_{m-1}\), \(D(K)=0\), preserves the affine bracket. Its possible central defect is
\(-m(m+n-1)B(x,y)\delta_{m+n-1,0}K=0\). It preserves the defining vacuum ideal, so descends to \(T\). Taking B=κ and ℓ=1 applies this construction to every form in §3.3.2. No simplicity or critical-level hypothesis is needed below.

**Theorem.** The algebra \(\operatorname{End}_{\widehat{\mathfrak g}}(V_\ell)\) is commutative. Every invariant state has a field reconstructed from normally ordered derivative currents; all its modes commute with all currents and with the modes of every other invariant field. Its negative modes are exactly the endomorphisms corresponding to its divided translates.

**Fields and finite sums.** A field on \(V_\ell\) is a series
\(F(z)=\sum_{n\in\mathbb Z}F_{(n)}z^{-n-1}\) such that
\(F_{(n)}u=0\) for all sufficiently large \(n\), for each fixed state \(u\). Equivalently, \(F(z)u\in V_\ell((z))\). The current
\(x(z)=\sum_mx_mz^{-m-1}\) is a field by smoothness. Write
\[
x_-(z)=\sum_{m<0}x_mz^{-m-1},\qquad
x_+(z)=\sum_{m\ge0}x_mz^{-m-1},
\qquad x^{[n]}(z)=\frac{\partial_z^{n-1}x(z)}{(n-1)!}\quad(n\ge1).
\tag{VC.4}
\]
The derivative's minus and plus parts are the derivatives of the indicated parts. The finitely many derivatives of \(z^0,\ldots,z^{n-2}\) vanish, so its minus part still has only nonnegative powers of \(z\). Define the left normal-multiplication operator on fields by
\[
L_{x,n}F=x^{[n]}_-(z)F(z)+F(z)x^{[n]}_+(z).
\tag{VC.5}
\]
Both terms are fields. On \(u\), the second uses finitely many nonnegative current modes. In the first, any fixed coefficient uses finitely many nonnegative powers from \(x^{[n]}_-\), because \(F(z)u\) has a lower bound on its powers. These observations also justify a finite iteration. More explicitly, expand a fixed iterated normal product into its finitely many choices of minus or plus parts. Each term has all negative-mode factors to the left of all nonnegative-mode factors. The latter act first on \(u\); smoothness leaves a finite tree of intermediate states and finite mode cutoffs. The remaining minus-part factors have nonnegative powers, so only finitely many of their terms can contribute to a fixed coefficient. This proves coefficientwise finiteness, including after replacing \(u\) by any finite list of states.

**Reconstruction respects the state relations.** These operators obey
\[
[L_{x,n},L_{y,r}]=L_{[x,y],n+r}.
\tag{VC.6}
\]
Here is the calculation. Put \(X=x^{[n]}\), \(Y=y^{[r]}\). Left and right multiplication commute, so the cross terms cancel and the left side on \(F\) is
\([X_-,Y_-]F-F[X_+,Y_+]\). There is no central term in either bracket: two strictly negative indices cannot sum to zero, and two nonnegative indices can sum to zero only at zero, where the cocycle coefficient vanishes. The explicit expansions are
\[
x^{[n]}_-=
\sum_{s\ge0}\binom{n+s-1}{n-1}x_{-(n+s)}z^s,
\quad
x^{[n]}_+=(-1)^{n-1}\sum_{p\ge0}
\binom{n+p-1}{n-1}x_pz^{-n-p}.
\tag{VC.7}
\]
The convolution identity
\[
\sum_{i+j=s}\binom{n+i-1}{n-1}\binom{r+j-1}{r-1}
=\binom{n+r+s-1}{n+r-1}
\]
follows by multiplying the formal series \((1-u)^{-n}\) and \((1-u)^{-r}\); their displayed coefficients follow by differentiating the geometric series. It gives
\([X_-,Y_-]=[x,y]^{[n+r]}_-\) and
\([X_+,Y_+]=-[x,y]^{[n+r]}_+\), proving (VC.6). Every coefficient comparison is finite by the preceding bounds.

Thus \(x_{-n}\mapsto L_{x,n}\) is a representation of the negative current Lie algebra on fields. The enveloping-algebra universal property makes the following linear map well defined on the actual vacuum space:
\[
Y(v,z)=\operatorname{Id},\qquad
Y(x_{-n}u,z)=L_{x,n}Y(u,z).
\tag{VC.8}
\]
In particular \(Y(x_{-1}v,z)=x(z)\). Equation (VC.6) proves independence from all exchanges of negative-mode letters; the construction is not a prescription that ignores their brackets.

**Creation and translation.** The reconstructed field has
\[
Y(u,z)v=e^{zT}u=\sum_{a\ge0}\frac{z^aT^au}{a!}.
\tag{VC.9}
\]
For the vacuum this is immediate. For \(x_{-n}u\), the plus part kills \(v\), while repeated use of (VC.3) gives
\[
e^{zT}x_{-n}e^{-zT}
=\sum_{a\ge0}\binom{n+a-1}{a}x_{-(n+a)}z^a
=x^{[n]}_-(z).
\]
This identity follows coefficientwise from
\((\operatorname{ad}T)^ax_{-n}=n(n+1)\cdots(n+a-1)x_{-(n+a)}\), and the finite binomial expansion for conjugation. Multiplying the induction hypothesis by its left side proves (VC.9). The exponential is a formal power series, with a finite algebraic state in each coefficient.

We also have
\[
Y(Tu,z)=\partial_zY(u,z),\qquad
[T,Y(u,z)]=\partial_zY(u,z).
\tag{VC.10}
\]
For the first identity, use
\(T(x_{-n}u)=n x_{-(n+1)}u+x_{-n}Tu\) and
\(\partial_z(L_{x,n}F)=nL_{x,n+1}F+L_{x,n}\partial_zF\).
For the second, (VC.3) gives
\([T,x^{[n]}_\pm]=\partial_zx^{[n]}_\pm\); the only splitting boundary would have mode index zero and coefficient zero. Apply the product rule in (VC.5) and induction from the identity field. The same finite coefficient bounds justify both calculations.

**Locality, proved algebraically.** Two fields are called local when
\((s-z)^M[A(s),B(z)]=0\) for some nonnegative integer \(M\), as a coefficient identity of operator-valued distributions. This definition does not assume an operator-product theorem. Define the formal delta distribution
\[
\delta(s,z)=\sum_{m\in\mathbb Z}s^{-m-1}z^m.
\]
The affine bracket directly gives
\[
[x(s),y(z)]=x,y\delta(s,z)
+\ell B(x,y)\partial_z\delta(s,z).
\tag{VC.11}
\]
Indeed its \(s^{-m-1}\) coefficient is
\(z^mx,y+m\ell B(x,y)z^{m-1}\). Shifting indices gives
\((s-z)\delta=0\); differentiation gives
\((s-z)\partial_z\delta=\delta\). Thus currents are local with order at most two. Differentiating a locality relation and multiplying by one additional factor \(s-z\) proves locality of a derivative; iteration covers all derivative currents.

We need closure under products, and prove it here. For an integer \(n\), set
\[
(A_{(n)}B)(z)=\operatorname{Res}_s
\left(\iota_{s,z}(s-z)^n A(s)B(z)
-\iota_{z,s}(s-z)^n B(z)A(s)\right).
\tag{VC.12}
\]
The notation \(\iota_{s,z}\) means the binomial expansion in nonnegative powers of \(z/s\); \(\iota_{z,s}\) means the expansion in nonnegative powers of \(s/z\). For \(n\ge0\) both are the same finite polynomial. The result is then the finite sum
\(\sum_{i=0}^n\binom ni(-z)^{n-i}[A_{(i)},B(z)]\), hence a field. For \(n=-r<0\), expansion and residue extraction give
\[
A_{(-r)}B=
\left(\frac{\partial_z^{r-1}A}{(r-1)!}\right)_-B
+B\left(\frac{\partial_z^{r-1}A}{(r-1)!}\right)_+.
\tag{VC.13}
\]
For example \(r=1\) uses
\(\iota_{s,z}(s-z)^{-1}=\sum_{a\ge0}s^{-a-1}z^a\) and
\(\iota_{z,s}(s-z)^{-1}=-\sum_{a\ge0}s^az^{-a-1}\).
The higher formula follows by differentiating these expansions \(r-1\) times with respect to \(z\) and dividing by \((r-1)!\). It is a field by precisely the finite normal-product argument given above, which applies to any fields with the truncation property.

Suppose \(A,B,C\) are pairwise local, with respective orders \(a,b,c\) for \((A,B),(A,C),(B,C)\). Then \(A_{(n)}B\) is local with \(C\). To check this without importing a closure theorem, write
\(p=s-z\), \(q=z-u\), and \(s-u=p+q\), and choose
\(M=a+b+c+|n|+1\). Multiply the commutator with \(C(u)\) in (VC.12) by \(q^M\). The factor \(q^c\) allows \(C\) to pass through \(B\), leaving, inside the residue, the two orders
\[
\iota_{s,z}p^n[C(u),A(s)]B(z),\qquad
\iota_{z,s}p^nB(z)[C(u),A(s)].
\]
Expand the remaining polynomial as
\[
q^{M-c}=((s-u)-p)^{M-c}
=\sum_{j=0}^{M-c}\binom{M-c}{j}(s-u)^j(-p)^{M-c-j}.
\]
Terms with \(j\ge b\) vanish by locality of \(A,C\). For \(j<b\), put \(k=M-c-j\). Our choice gives \(n+k\ge a\), so multiplying either expansion by \(p^k\) turns its kernel into the same polynomial \(p^{n+k}\). Their difference is therefore a scalar multiple of
\[
q^cp^{n+k}(s-u)^j[[C(u),A(s)],B(z)].
\]
Jacobi writes this double commutator as
\([C,[A,B]]-[A,[C,B]]\). The first term is killed by \(p^a\), and the second by \(q^c\). Every term is zero. This proves the claimed locality. All polynomial multiplications are finite; for a residue with a negative exponent, fix an input state and the relevant third-mode coefficients and use common cutoffs on that finite family of states in (VC.13). Hence the coefficient comparisons used in this proof involve actual finite sums.

Beginning with the identity field and the currents, this lemma, (VC.13), and induction on the total number of normal-product operations prove that every two reconstructed fields are local. It also proves that every product (VC.12) of reconstructed fields is local with every current. Thus both locality assertions have been proved from the affine brackets and finite sums.

**Uniqueness from the vacuum.** If a field \(F(z)\) is local with all currents and \(F(z)v=0\), then \(F=0\). In fact, suppose \(F(z)u=0\). Locality gives
\((z-s)^M F(z)x(s)u=0\). The series \(F(z)x(s)u\) belongs to \(V_\ell((z))((s))\): smoothness gives a lower bound on its powers of \(s\), and each coefficient is a Laurent series in \(z\). In this space multiplication by \((z-s)^M\) is invertible, with inverse obtained by expanding
\(z^{-M}(1-s/z)^{-M}\) in powers of \(s\). Consequently
\(F(z)x_mu=0\) for every \(m\). Starting with \(u=v\) and iterating over negative-mode words proves that \(F\) kills every state. In particular, two fields local with currents and with the same value on \(v\) are identical.

**The commutator formula for every integer mode.** Fix \(w\) and \(x\). By the proved locality, the distribution
\(H(s,z)=[x(s),Y(w,z)]\) is killed by \((s-z)^M\) for some \(M\). Increase its locality order if necessary so that \(M\ge1\). Put
\[
C_j(z)=\operatorname{Res}_s(s-z)^jH(s,z).
\tag{VC.14}
\]
Each \(C_j=x_{(j)}Y(w)\) is a field local with every current, by (VC.12) and its closure proof. It is zero for \(j\ge M\). We first identify it by creation. Since \(x_iv=0\) for \(i\ge0\),
\[
C_j(z)v=\sum_{i=0}^j\binom ji(-z)^{j-i}x_i e^{zT}w.
\]
From (VC.3),
\[
x_i e^{zT}=e^{zT}\sum_{r=0}^i\binom ir z^{i-r}x_r.
\]
The coefficient of \(x_r\) in the combined sum is
\(\binom jr z^{j-r}\sum_{i=r}^j\binom{j-r}{i-r}(-1)^{j-i}\), which is zero unless \(r=j\), when it is one. Thus
\(C_j(z)v=e^{zT}x_jw\). Creation and the uniqueness lemma now give
\[
C_j(z)=Y(x_jw,z).
\tag{VC.15}
\]

For completeness, locality has the following finite delta expansion, with no further distribution theorem needed:
\[
H(s,z)=\sum_{j=0}^{M-1}C_j(z)\frac{\partial_z^j\delta(s,z)}{j!}.
\tag{VC.16}
\]
To prove it, differentiate \((s-z)\delta=0\) to obtain
\((s-z)\partial_z^r\delta/r!=\partial_z^{r-1}\delta/(r-1)!\).
It follows that
\(\operatorname{Res}_s(s-z)^j\partial_z^r\delta/r!=\delta_{jr}\).
Subtract the right side of (VC.16) from \(H\). The remainder \(G\) is killed by \((s-z)^M\) and its first \(M\) residues against powers of \(s-z\) vanish. Writing
\(G=\sum_mG_m(z)s^{-m-1}\), these residues successively give
\(G_0=\cdots=G_{M-1}=0\). The locality relation is the recurrence
\[
\sum_{i=0}^M\binom Mi(-z)^{M-i}G_{m+i}(z)=0.
\]
Its leading coefficient is one, so it propagates the zeros forward. Its constant coefficient \((-z)^M\) is invertible as a Laurent monomial, so it propagates them backward. Thus all \(G_m\) vanish, proving (VC.16).

Take the \(s^{-m-1}\) coefficient, or equivalently the residue against \(s^m\). For every integer \(m\),
\(\operatorname{Res}_s s^m\partial_z^j\delta/j!=\binom mjz^{m-j}\), by differentiating the Laurent monomial \(z^m\). Combining (VC.15)–(VC.16) proves
\[
\boxed{
[x_m,Y(w,z)]=\sum_{j\ge0}\binom mjz^{m-j}Y(x_jw,z)
\qquad(m\in\mathbb Z).
}
\tag{VC.17}
\]
The upper support is finite, independently of \(m\), because the terms vanish for \(j\ge M\); it is also finite by the smoothness bound on \(w\). The generalized binomial coefficients here include negative \(m\). The proof has not extended a nonnegative-mode formula to negative modes by assertion.

**All invariant modes commute.** If \(w\) is killed by \(\mathfrak g[[t]]\), every term on the right of (VC.17) is zero. Every coefficient \(w_{(n)}\) of \(Y(w,z)\) therefore commutes with every \(x_m\). Its image of a state is an actual algebraic state, by the field construction. Such an operator preserves every current annihilation bound: if \(x_mu=0\) for all sufficiently large \(m\), then
\(x_mw_{(n)}u=w_{(n)}x_mu=0\) with the same bound. It consequently commutes with formal Laurent currents by the common finite-tail argument of §3. Hence every \(w_{(n)}\) is an affine-module endomorphism.

Creation says
\[
w_{(n)}v=0\quad(n\ge0),\qquad
w_{(-r-1)}v=\frac{T^rw}{r!}\quad(r\ge0).
\tag{VC.18}
\]
An endomorphism killing the cyclic vacuum is zero, so all the modes with \(n\ge0\) vanish on \(V_\ell\). The negative modes are, by (VC.2), exactly the endomorphisms corresponding to these divided translates. The translates are invariant also directly: for \(j\ge1\),
\(x_jTw=Tx_jw+jx_{j-1}w=0\), while \(x_0Tw=Tx_0w=0\); induction applies to all powers of \(T\).

Finally, any operator \(E\) commuting with every current mode commutes with every reconstructed field. Prove this by induction in (VC.8). It commutes with the identity field. If it commutes with \(F\), it commutes with
\(x^{[n]}_-F+Fx^{[n]}_+\), since it commutes with every coefficient of both current parts. This is an equality of actual operators: on a fixed state choose the common positive-mode cutoffs for it and its image under \(E\); these are available with the same annihilation bound. Only finitely many negative powers contribute to a fixed coefficient, using the field truncation bounds. The finite normal-product expansions in (VC.5) therefore permit \(E\) to pass through each summand. It follows that
\[
[E,Y(u,z)]=0\qquad\text{for every state }u.
\tag{VC.19}
\]
In particular every mode of an invariant field commutes with every mode of every other invariant field.

For an arbitrary affine endomorphism \(E\), the state \(w=Ev\) is invariant, and (VC.18) shows that \(w_{(-1)}\) has the same vacuum image. Cyclicity gives \(E=w_{(-1)}\). Applying (VC.19) to any two such endomorphisms proves the theorem. In particular,
\[
\operatorname{End}_{\widehat{\mathfrak g}}(V_\ell)
\text{ is commutative},\qquad
\left[E_{T^rw/r!},E_{T^su/s!}\right]=0
\quad(r,s\ge0)
\tag{VC.20}
\]
for every pair of invariant states \(w,u\). This proves the translated commutators through reconstructed fields and finite mode sums, without differentiating a commutator of two initial endomorphisms.

The proof mechanisms and their dependence are shown below. The labels refer to the explicit identities and lemmas above; no vertex reconstruction or commutator theorem is an additional premise.

| Stage | Exact argument | Consequence |
| --- | --- | --- |
| Negative-current relations | Normal operators satisfy (VC.6) | Reconstruction is well defined on the vacuum. |
| Creation and locality | (VC.8)–(VC.9), current locality and the product proof (VC.11)–(VC.13) | Vacuum uniqueness identifies the current products in (VC.15). |
| Every integer mode | The finite delta expansion (VC.16)–(VC.17) | Invariant field modes commute with all currents. |
| Endomorphism commutation | Normal reconstruction with common finite cutoffs (VC.19) | All vacuum endomorphisms and divided translates commute, by (VC.20). |

*Each arrow of the argument is proved at its listed locator. The common cutoffs ensure that every operator coefficient is an actual finite sum.*

**The exact reduction to basic invariant lifts.** There is also a useful filtered consequence. Filter a state by negative-word length. If \(w\) has length at most \(d\), every coefficient of \(Y(w,z)\) raises this filtration by at most \(d\). In an expanded normal product, a negative mode adds one letter. A nonnegative mode preserves the input filtration: commute it through a word of length \(p\). A first negative bracket replaces one letter by one; a central bracket removes a letter; a nonnegative bracket either kills the vacuum or uses a further bracket and replaces at least two letters by at most one. Repeating leaves only terms of length at most \(p\). Any summand containing a plus-part factor therefore raises length by at most \(d-1\). A summand with only minus-part factors has only nonnegative powers of \(z\). For its coefficient of \(z^0\), every factor must have power zero, and (VC.7) makes it exactly the original negative-mode word acting by left multiplication. Consequently, for invariant states \(w,u\),
\[
\sigma(E_wE_u v)=\sigma(w)\sigma(u)
\tag{VC.21}
\]
when their indicated leading PBW symbols are nonzero. This also proves that endomorphism composition gives a filtered algebra, with the usual commutative symbol product. Its associated graded injects into the current invariants of
\(\operatorname{Sym}(t^{-1}\mathfrak g[t^{-1}])\), because the current action preserves the filtration.

Suppose that a separately proved classical invariant presentation is
\[
\operatorname{Sym}(t^{-1}\mathfrak g[t^{-1}])^{\mathfrak g[[t]]}
=k[q_{\alpha,r}:1\le\alpha\le s,\ r\ge0],
\tag{VC.22}
\]
with algebraically independent positive-length generators. Suppose there are actual invariant states \(w_\alpha\) whose divided translates have exactly these leading symbols:
\(\sigma(T^rw_\alpha/r!)=q_{\alpha,r}\). Then the commuting endomorphisms of those divided translates freely generate the vacuum endomorphism algebra. For independence, any relation uses finitely many generators. Its highest weighted PBW-degree part has, by (VC.21), the same polynomial in the independent symbols, which cannot be zero. For generation, the highest symbol of any invariant state is a finite homogeneous polynomial in (VC.22). Subtract the corresponding polynomial in the lift endomorphisms, applied to \(v\); its PBW degree decreases. Repeating terminates because degree is nonnegative, and degree zero consists of scalar multiples of \(v\). This proves generation. All commutativity needed for this argument is already unconditional in (VC.20).

Section 3.3.1 supplies the classical invariant presentation. The existence and symbol normalization of the basic lifts are the remaining input to this filtered consequence; §3.3.5 supplies them in type A. The theorem proved here is the general affine vacuum commutativity statement at every scalar level, together with its full algebraic reconstruction, creation, all-integer commutator formula and translated-mode compatibility. It makes no identification with a specified completed enveloping-algebra center or with functions on opers.

#### 3.3.4. What quantum lifting must supply

The preceding theorem proves the complete classical symbol algebra for every split semisimple type. It does not construct a quantum vector with any prescribed leading symbol. We state and prove the exact filtered implication so that this remaining task is explicit.

**Quantum-lifting reduction.** Suppose, at the critical form, that for each \(i\) there is an invariant vector \(w_i\) of letter degree \(D_i\) and energy \(D_i\) whose leading symbol is \(p_{i,0}\). Put
\[
w_{i,r}=\frac{T^r w_i}{r!},\qquad
A_{i,r}(v)=w_{i,r}.
\tag{GJ.Q1}
\]
Here \(A_{i,r}\) is the affine endomorphism supplied by (K2.3). The general theorem of §3.3.3 proves that these endomorphisms commute with one another. Under the stated basic-lift hypothesis,
\[
\operatorname{End}_{\widehat{\mathfrak g}_{\rm crit}}(V_{\rm crit})
 =k[A_{i,r}:1\leq i\leq\ell,\ r\geq0],
\tag{GJ.Q2}
\]
with algebraically independent generators; this identity commutes with every ordinary extension \(k\to R\).

**Proof.** Translation preserves invariants, so every \(w_{i,r}\) is an invariant. Formula (GJ.P7) gives its leading symbol \(p_{i,r}\), its length degree \(D_i\), and its energy \(D_i+r\). The proved commutativity (VC.20) defines the polynomial algebra map sending a variable \(z_{i,r}\) to \(A_{i,r}\). Give \(z_{i,r}\) weight \(D_i\). By the product argument for (GJ.P3), a monomial in these endomorphisms has leading symbol the same monomial in the \(p_{i,r}\). The highest weighted homogeneous part of a nonzero polynomial therefore has a nonzero symbol, by the algebraic independence proved in §3.3.1. This proves injectivity.

For surjectivity, take any invariant \(w\) with maximal letter degree \(d\). Its highest symbol belongs to \(k[p_{i,r}]\) by (GJ.P3). Because that symbol is homogeneous of degree \(d\) and each generator has length degree \(D_i\), it is the degree-\(d\) weighted homogeneous part of a finite polynomial in these generators. Apply the corresponding polynomial in the \(A_{i,r}\) to \(v\) and subtract it from \(w\). This removes the degree-\(d\) symbol and leaves an invariant of strictly smaller length degree. Repeating terminates, since degrees are nonnegative integers. Degree zero is a scalar multiple of \(v\). Thus every invariant, and hence every endomorphism, is a finite polynomial in the \(A_{i,r}\). The procedure also shows why a completed polynomial ring is not involved. Finally (GJ.P5) tensors the proved algebra isomorphism with any ordinary \(R\), giving the asserted ordinary-family identity. \(\square\)

An invariant lift without the stated energy condition can be replaced by its energy-\(D_i\) component: invariants are energy graded, and its degree-\(D_i\) symbol lies in that component. Thus the energy condition creates no additional existence problem. The existence of the invariant basic lifts is not proved by the classical invariant calculation. All translated commutators needed here are supplied by the full reconstruction and common-cutoff proof of (VC.20).

The proof separates the relevant statements as follows:

| Statement | Argument now available | Remaining content |
| --- | --- | --- |
| All classical current invariants | Polynomial Kostant section and the dominant finite conjugation map in §3.3.1 | The earlier explicit semisimple Lie and invariant-ring foundations remain. |
| The upper bound on quantum symbols | The exact nonnegative-mode action and injection (GJ.P2)–(GJ.P3) | This is an inclusion, with no lifting assertion. |
| Polynomial independence and exhaustion after quantum lifting | Translation (GJ.P7), unconditional commutativity (VC.20), and the finite degree induction in (GJ.Q1)–(GJ.Q2) | Actual invariant basic lifts with the prescribed leading symbols. |
| Functions on dual-group opers with the full coordinate action | The ordinary oper construction in §§1.1–1.2 and the full rank-one comparison in §3.2 | In higher rank, identify the quantum generators and every lower-filtration coordinate term. |

The general basic-lift hypothesis remains open for the other simple types; §3.3.5 supplies the full list for every type A factor. Once such lifts are supplied, the written argument proves the whole polynomial vacuum algebra and its ordinary coefficient extensions. The completed punctured-disc center, critical-level Poisson/chiral structures, Satake compatibility, derived parameter families and central-convention comparison also retain their separate complete-proof obligations in §4.

#### 3.3.5. Basic critical \(\mathfrak{sl}_n\) lifts and the polynomial vacuum center

Work over a field \(k\) of characteristic zero, with \(n\geq2\). For \(n=1\) the form is zero, the sole coefficient \(E_{11}[-1]\) is central, and the traceless quotient is zero, so the empty list of basic traceless lifts needs no separate argument. The determinant construction is due to Chervov–Molev, [*On higher order Sugawara operators*, arXiv:0808.1947v2, Theorem 3.1](https://arxiv.org/abs/0808.1947v2). The calculation below proves the required lift existence from the explicit affine relations. In particular, the determinant cancellation is proved here rather than inferred from a Manin-matrix or vertex-algebra theorem. Its conclusion concerns vacuum vectors and their affine-module endomorphisms; quantum commutativity and completed, coordinate, chiral, Satake and derived comparisons are separate assertions.

##### SL.L1. Form, affine bracket and translation

Write \(E_{ij}[r]=E_{ij}\otimes t^r\), and use the form
\[
\kappa(X,Y)=-n\operatorname{tr}(XY)+\operatorname{tr}(X)\operatorname{tr}(Y).
\tag{SL.L1}
\]
With \(K=1\), the defining relations are
\[
[E_{ij}[r],E_{kl}[s]]
=\delta_{jk}E_{il}[r+s]-\delta_{il}E_{kj}[r+s]
+r\delta_{r,-s}\bigl(-n\delta_{jk}\delta_{il}+\delta_{ij}\delta_{kl}\bigr).
\tag{SL.L2}
\]
Let \(V\) be the induced vacuum, with \(\mathfrak{gl}_n[t]v=0\). The ordered-basis proof in §3, (K2.1)–(K2.3), identifies \(V\) with \(U(t^{-1}\mathfrak{gl}_n[t^{-1}])v\). All calculations here are finite enveloping-algebra calculations under precisely that convention.

For normalization, on \(\operatorname{End}(k^n)\) write \(\operatorname{ad}X=L_X-R_X\). Matrix units give
\(\operatorname{Tr}(L_XL_Y)=\operatorname{Tr}(R_XR_Y)=n\operatorname{tr}(XY)\) and
\(\operatorname{Tr}(L_XR_Y)=\operatorname{tr}(X)\operatorname{tr}(Y)\).
Thus the Killing form on \(\mathfrak{gl}_n\) is
\(2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)\), so (SL.L1) is minus half that form. On the traceless quotient it is exactly \(-n\operatorname{tr}(XY)\).

The rule
\[
[\tau,E_{ij}[r]]=-rE_{ij}[r-1],\qquad [\tau,K]=0,\qquad \tau v=0
\tag{SL.L3}
\]
is consistent with the affine bracket. Indeed its noncentral derivation identity is multiplication by \(-(r+s)\). The central part of the right-hand side is
\(-r(r+s-1)\kappa(X,Y)\delta_{r+s,1}=0\); the left-hand central term is zero. The rule preserves the vacuum relations, since for \(r\geq0\), either \(r=0\) gives zero or \(r-1\geq0\). Consequently \(\tau\) acts on \(V\) as the derivation determined by (SL.L3).

##### SL.L2. Right normal ordering and the auxiliary parameter

Put \(a_{ij}=E_{ij}[-1]\), and let
\(M_{ij}=\delta_{ij}\tau+a_{ij}\). Define the column determinant by its finite sum, with multiplication in increasing column order:
\[
\operatorname{cdet}M
=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
M_{\sigma(1),1}\cdots M_{\sigma(n),n}.
\tag{SL.L4}
\]
Move \(\tau\) to the right by \(\tau a=a\tau+[\tau,a]\). Repeated movement terminates, since each commutator removes one occurrence of \(\tau\) that must be moved. The ordered basis for the semidirect Lie algebra of negative modes and \(\tau\) proves uniqueness. There are therefore unique negative-mode elements \(S_i\) such that
\[
\operatorname{cdet}M=\tau^n+S_1\tau^{n-1}+\cdots+S_n.
\tag{SL.L5}
\]
It would be insufficient to apply (SL.L5) just to \(v\), since that sees only \(S_n v\). Introduce a central indeterminate \(u\), set
\[
M_{ij}(u)=\delta_{ij}(\tau+u)+a_{ij},\qquad
D(u)=\operatorname{cdet}M(u).
\tag{SL.L6}
\]
The substitution \(\tau\mapsto\tau+u\) preserves all the relations. Right normal ordering and \(\tau v=0\) give
\[
D(u)v=u^n v+S_1v\,u^{n-1}+\cdots+S_nv.
\tag{SL.L7}
\]
Thus invariance of this polynomial is equivalent to invariance of every coefficient.

##### SL.L3. The precise Manin identity and all needed determinant rules

The negative-mode bracket has no central term. Directly from (SL.L2)–(SL.L3),
\[
[M_{ij}(u),M_{kl}(u)]
=\delta_{ij}E_{kl}[-2]-\delta_{kl}E_{ij}[-2]
+\delta_{jk}E_{il}[-2]-\delta_{il}E_{kj}[-2]
=[M_{kj}(u),M_{il}(u)].
\tag{SL.L8}
\]
In particular, putting \(l=j\) makes a same-column commutator equal to its negative, so that commutator is zero. This uses characteristic different from two; there is no missing factor of two.

Adjoin exterior generators \(\psi_1,\ldots,\psi_n\) commuting with all enveloping-algebra coefficients, and put
\[
\theta_j=\sum_r\psi_r M_{rj}(u),\qquad
\Psi=\psi_1\cdots\psi_n.
\tag{SL.L9}
\]
For \(r<s\), the coefficient of \(\psi_r\psi_s\) in
\(\theta_j\theta_l+\theta_l\theta_j\) is
\([M_{rj},M_{sl}]-[M_{sj},M_{rl}]\), which is zero by (SL.L8). The same-column relation gives \(\theta_j^2=0\). Hence the \(\theta_j\) anticommute, including their noncommuting coefficients. Expansion of the exterior product, with the order of coefficients left intact, gives
\[
\theta_1\cdots\theta_n=\Psi D(u).
\tag{SL.L10}
\]
This also proves the column rules used below: swapping two columns changes the sign, by anticommutation; a repeated column has determinant zero, by moving its two equal exterior factors together and using their square zero. A submatrix satisfies (SL.L8), since restriction of the indices preserves that identity, so these rules hold for each minor as well. Swapping rows changes the sign by relabeling the permutation in (SL.L4), without moving any coefficients. A repeated row makes paired permutation terms identical with opposite signs. No commutative determinant rule has been imported.

Let \(D_i(u)\) be the column determinant of \(M(u)\) with row and column \(i\) deleted, in their original increasing order. One further rule needed in the proof is the pinned-column identity
\[
\theta_1\cdots\theta_{i-1}\psi_i\theta_{i+1}\cdots\theta_n
=\Psi D_i(u).
\tag{SL.L11}
\]
Indeed a nonzero top exterior term here has its row permutation fixing \(i\). The sign of that permutation equals the sign on the ordered complement: inversions crossing the fixed index number twice the number of values greater than \(i\) occurring before it. They contribute an even number. Expansion of the remaining factors is therefore exactly the defining ordered minor sum. This proves (SL.L11), including its positive sign. In particular,
\(\theta_1\cdots\theta_{n-1}\psi_n=\Psi D_n(u)\).

##### SL.L4. Zero modes

For \(H_{ab}=E_{ab}[0]\), the affine bracket and cancellation of the diagonal \(\tau+u\) terms give
\[
[H_{ab},\theta_j]=\psi_b M_{aj}(u)-\delta_{aj}\theta_b.
\tag{SL.L12}
\]
Let \(\rho_{ab}\) be the even derivation of the exterior algebra defined by
\(\rho_{ab}(\psi_r)=\delta_{ar}\psi_b\); it acts trivially on coefficients. Apply the ordinary commutator product rule to (SL.L10). Formula (SL.L12) yields
\[
[H_{ab},\theta_1\cdots\theta_n]
=\rho_{ab}(\theta_1\cdots\theta_n)
-\theta_1\cdots\theta_{a-1}\theta_b\theta_{a+1}\cdots\theta_n.
\tag{SL.L13}
\]
On the top exterior form, \(\rho_{ab}\Psi=\delta_{ab}\Psi\): for \(a\ne b\) the replacement creates a repeated exterior generator, while for \(a=b\) it fixes the unique relevant factor. The last term in (SL.L13) is zero for \(a\ne b\), by the repeated-column rule, and equals \(\Psi D(u)\) for \(a=b\). These terms cancel. Taking the top coefficient proves
\([H_{ab},D(u)]=0\), and then (SL.L7) proves \(E_{ab}[0]S_i v=0\) for every \(a,b,i\).

##### SL.L5. The finite mode-one cancellation

Set \(b=E_{nn}[1]\), \(h=E_{nn}[0]\), and \(f_i=E_{ni}[0]\) for \(i<n\). The full entrywise formula, including its central terms, is
\[
[E_{ab}[1],M_{ij}(u)]
=\delta_{ij}E_{ab}[0]+\delta_{bi}E_{aj}[0]-\delta_{aj}E_{ib}[0]
+\delta_{ab}\delta_{ij}-n\delta_{aj}\delta_{bi}.
\tag{SL.L14}
\]
The first term is \([E_{ab}[1],\delta_{ij}\tau]\); thus omitting the translation commutator would spoil the proof. From (SL.L14),
\[
[b,\theta_i]=Z_i+\psi_i\quad(i<n),\qquad
Z_i=\psi_i h+\psi_n f_i,
\]
\[
[b,\theta_n]=\psi_n h-\sum_{r<n}\psi_rE_{rn}[0]-(n-1)\psi_n.
\tag{SL.L15}
\]
The zero-mode part of the last expression kills \(v\), because it occurs in the final column. The earlier \(Z_i\) must be moved through the later columns; discarding them prematurely would be an error.

Here is the required normal-order identity, proved without determinant rearrangement assumptions. Formula (SL.L12) gives
\[
[h,\theta_k]=\psi_nM_{nk}(u)-\delta_{nk}\theta_n,
\qquad
[f_i,\theta_k]=\psi_iM_{nk}(u)-\delta_{nk}\theta_i.
\]
Since each \(\theta_k\) anticommutes with each \(\psi_r\), their odd anticommutator with \(Z_i\) is
\[
Z_i\theta_k+\theta_kZ_i
=\psi_i[h,\theta_k]+\psi_n[f_i,\theta_k]
=-\delta_{nk}(\psi_i\theta_n+\psi_n\theta_i).
\tag{SL.L16}
\]
The two potential terms involving \(M_{nk}(u)\) cancel as
\((\psi_i\psi_n+\psi_n\psi_i)M_{nk}(u)=0\).
This is the finite cancellation controlling every later-column contribution.

Fix \(i<n\), and abbreviate
\(B=\theta_1\cdots\theta_{i-1}\),
\(C=\theta_{i+1}\cdots\theta_{n-1}\),
\(m=n-i-1\). Repeatedly apply (SL.L16) for the \(m\) columns less than \(n\), then for column \(n\). Since \(Z_i v=0\), this gives
\[
B Z_i C\theta_n v
=(-1)^{m+1}BC(\psi_i\theta_n+\psi_n\theta_i)v.
\tag{SL.L17}
\]
There are no omitted terms: (SL.L16) has zero right side for every column in \(C\), and its sole final-column correction is the displayed pair.

For the first term of (SL.L17), move \(\psi_i\) left past the \(m\) factors of \(C\). Its sign becomes
\((-1)^{m+1}(-1)^m=-1\); by (SL.L11) its top coefficient is \(-D_i(u)v\).
For the second, first use \(\psi_n\theta_i=-\theta_i\psi_n\), then move \(\theta_i\) left past those same \(m\) factors. The total sign is
\((-1)^{m+1}(-1)(-1)^m=+1\); its top coefficient is \(D_n(u)v\).
Thus the exact identity is
\[
\theta_1\cdots\theta_{i-1} Z_i\theta_{i+1}\cdots\theta_n v
=\Psi\bigl(D_n(u)-D_i(u)\bigr)v.
\tag{SL.L18}
\]

The following table displays the whole mechanism, with the common top exterior factor \(\Psi\) suppressed. Every row is an exact identity after applying to \(v\).

| Column in the mode-one product rule | Moved zero-mode contribution | Central scalar contribution | Total |
|---|---|---|---|
| Each \(i<n\) | \(D_n(u)-D_i(u)\), by (SL.L18) | \(+D_i(u)\) | \(+D_n(u)\) |
| Final column \(n\) | \(0\), since its zero modes are already at the right | \(-(n-1)D_n(u)\) | \(-(n-1)D_n(u)\) |

The \(n-1\) earlier columns cancel the final one. Explicitly, the ordinary commutator product rule and (SL.L15)–(SL.L18) give
\[
b\,\theta_1\cdots\theta_n v
=\Psi\left(\sum_{i<n}(D_n(u)-D_i(u))
+\sum_{i<n}D_i(u)-(n-1)D_n(u)\right)v=0.
\tag{SL.L19}
\]
Taking the coefficient of \(\Psi\), then the coefficients of \(u\) in (SL.L7), proves \(E_{nn}[1]S_i v=0\) for every \(i\). This completes the hard determinant step.

As a normalization check on the calculation, replace the form by
\(\ell(\operatorname{tr}(XY)-\operatorname{tr}(X)\operatorname{tr}(Y)/n)\), still with \(K=1\). The zero-mode identity (SL.L18) is unchanged; the scalar contributions become \(-\ell D_i(u)/n\) and \(\ell(n-1)D_n(u)/n\). Consequently the same computation gives
\[
E_{nn}[1]D(u)v
=\left(1+\frac{\ell}{n}\right)
\left((n-1)D_n(u)-\sum_{i<n}D_i(u)\right)v.
\tag{SL.L20}
\]
The form in (SL.L1) is \(\ell=-n\), so the prefactor is exactly zero.

##### SL.L6. All nonnegative modes, including the trace current

Let \(w=S_i v\). We have proved that all zero modes and \(E_{nn}[1]\) kill \(w\). For \(i,j<n\), the explicit brackets
\[
[E_{in}[0],E_{nn}[1]]=E_{in}[1],\qquad
[E_{nj}[0],E_{nn}[1]]=-E_{nj}[1],
\]
\[
[E_{nj}[0],E_{in}[1]]=\delta_{ij}E_{nn}[1]-E_{ij}[1]
\tag{SL.L21}
\]
therefore prove that every \(E_{ab}[1]\) kills \(w\). Indeed a commutator of two operators killing \(w\) also kills \(w\). This proves the requested full \(\mathfrak{gl}_n[1]\) assertion, not just one diagonal mode.

The traceless Lie algebra is perfect, directly: every off-diagonal matrix unit is
\(\tfrac12[E_{ii}-E_{jj},E_{ij}]\), and every traceless diagonal generator is \([E_{ij},E_{ji}]\). For \(r\geq2\),
\([x[1],y[r-1]]=[x,y][r]\), with no central term. Induction proves that all positive \(\mathfrak{sl}_n\) modes kill \(w\).

Put \(I[r]=\sum_aE_{aa}[r]\). Its finite-matrix brackets vanish, and
\(\kappa(I,E_{ab})=-n\delta_{ab}+n\delta_{ab}=0\).
Thus \(I[r]\) is central in the affine current algebra for every \(r\). Each \(I[r]\), \(r\geq0\), kills \(v\) and commutes with \(S_i\), which contains only negative currents; hence it kills \(w\). This statement is about the current algebra: \(I[r]\) need not commute with the added translation \(\tau\). Together with the traceless result it proves
\[
\mathfrak{gl}_n[t]S_iv=0\quad(1\leq i\leq n).
\tag{SL.L22}
\]
The vacuum smoothness argument in §3 extends this to \(\mathfrak{gl}_n[[t]]\). All vectors are finite negative-mode words, so its finite-tail annihilation applies without a completion theorem. Each \(S_iv\) consequently defines an affine-module endomorphism by \(uv\mapsto uS_iv\), using exactly (K2.3). No commutativity assertion is needed for this construction.

##### SL.L7. Traceless quotient and basic symbols

The scalar current ideal \(I[r]=0\) for every \(r\) is stable under the affine bracket and under \(\tau\). Since \(n\) is invertible, the images
\(F_{ij}[r]=E_{ij}[r]-\delta_{ij}I[r]/n\) identify the quotient with the affine \(\mathfrak{sl}_n\) algebra at form \(-n\operatorname{tr}(XY)\). The ordered negative-mode basis proves that its vacuum is the quotient of \(V\) by the negative scalar currents. Let \(\overline S_i\) be the images of the coefficients. There is only one-current contribution to the coefficient of \(\tau^{n-1}\), so \(S_1=I[-1]\) and \(\overline S_1=0\). Formula (SL.L22) descends to every \(\overline S_i v\).

For PBW degree, a term initially choosing \(m\) current entries and \(n-m\) translation entries has \(m\) current factors. Every translation commutator removes one translation and keeps the number of current factors; reordering currents can only decrease PBW degree. A term contributing to \(S_i\) has final translation exponent \(n-i\), so necessarily \(m\leq i\). Its PBW degree is at most \(i\). Degree \(i\) comes precisely from choosing \(i\) currents and using the commute-past term at every translation movement. In the commutative associated graded, (SL.L4) is then the ordinary permutation sum for \(\det(z\mathbf1+X[-1])\). Therefore
\[
\sigma_i(S_i)=e_i(X[-1]),\qquad
\sigma_i(\overline S_i)=e_i(F[-1])\quad(2\leq i\leq n).
\tag{SL.L23}
\]
Here \(e_i\) is defined by
\(\det(z\mathbf1+X)=\sum_i e_i(X)z^{n-i}\); the coefficient of \(z^{n-i}\) in \(\det(z\mathbf1-X)\) is \((-1)^ie_i(X)\). Thus \((-1)^i\overline S_i\) lifts that characteristic-polynomial sign convention. Section 1.2.6, (IS.F8)–(IS.F9), proves that \(e_2,\ldots,e_n\) are algebraically independent basic traceless invariants, at that section's explicit invariant-theory foundations. In particular these symbols are nonzero, and each \(\overline S_i v\) is a nonzero basic critical quantum lift.

For the rank-one normalization, at \(n=2\) direct right ordering gives
\[
S_2=E_{11}[-1]E_{22}[-1]-E_{21}[-1]E_{12}[-1]+E_{22}[-2].
\]
After setting \(E_{22}=-E_{11}\), \(h=2E_{11}\), \(e=E_{12}\), \(f=E_{21}\), this is \(-Q/2\), where (K3.1) uses
\(Q=\tfrac12h[-1]^2+e[-1]f[-1]+f[-1]e[-1]\).
Indeed \([e[-1],f[-1]]=h[-2]\), so both expressions give
\(-E_{11}[-1]^2-f[-1]e[-1]-E_{11}[-2]\).
This checks the derivative correction and the factor two against the already written rank-one proof.

All identities are finite formulas over \(\mathbb Q\), using only division by \(2\) and \(n\), so they remain valid over every characteristic-zero field and after any ordinary coefficient extension. This is a direct construction over nonreduced coefficients as well, rather than an inference from reduced points. In addition, translation preserves the proved invariance: if all nonnegative modes kill \(w\), then
\(x[r]\tau w=\tau x[r]w+r x[r-1]w=0\) for \(r\geq0\), with the second term zero also for \(r=0\). Thus the derivatives \(\tau^q\overline S_i v\) are invariant lifts of the differentiated symbols.

The construction establishes the basic lifts in every type \(A_{n-1}\), with the specified critical form, ordering and signs. We can now combine it with the general results of §§3.3.1–3.3.4.


**Corollary: the whole polynomial vacuum algebra in type A.** Use the trace pairing \(B(X,Y)=\operatorname{tr}(XY)\) on \(\mathfrak{sl}_n\), and let
\[
w_i=\overline S_i v,\qquad
A_{i,r}(v)=\frac{T^r w_i}{r!}\quad(2\le i\le n,\ r\ge0).
\]
The trace pairing identifies the matrix of negative-mode symbols with the transpose of the coefficient matrix \(A_0\): \(\operatorname{tr}(F_{ij}A_0)=(A_0)_{ji}\) for traceless \(A_0\). A characteristic coefficient is unchanged by transpose, so (SL.L23) gives precisely \(e_i(A_0)=p_{i,0}\), with the characteristic-polynomial signs described there.

Give \(\tau\), \(u\), and \(E_{ab}[-j]\) energies \(1\), \(1\), and \(j\), respectively. The relation \([\tau,E_{ab}[-j]]=jE_{ab}[-j-1]\) preserves the total energy of a product. Every term of the determinant has energy \(n\), so its right-ordered coefficient \(S_i\) has energy \(i\). The basic lifts therefore have the length degree \(i\), energy \(i\), invariance, and symbols required by (GJ.Q1). Applying the proved commutativity (VC.20) and the full finite-degree exhaustion argument (GJ.Q2) gives
\[
\boxed{
\operatorname{End}_{\widehat{\mathfrak{sl}}_n,\mathrm{crit}}(V_{\mathrm{crit}})
 =k[A_{i,r}:2\le i\le n,\ r\ge0].
}
\tag{SL.C1}
\]
All listed generators are algebraically independent. Equation (GJ.P5) extends this algebra identity to every ordinary \(k\)-algebra \(R\), including nonreduced ones. Each endomorphism is a finite polynomial; no completed polynomial algebra is asserted.

For a direct sum of type A factors, the critical bracket has no cross-factor terms. A basic lift from one factor, with the vacuum in every other factor, is invariant for the entire sum. Its symbol is the corresponding basic polynomial of that factor. Thus the same general reduction proves (SL.C1) with the concatenated lists of generators. The zero Lie algebra gives the coefficient ring. Basic lifting in other simple types, the full higher-rank quantum coordinate law, the oper comparison with that law, and the completed/chiral/Poisson/Satake/derived comparisons remain separate proof obligations.

## 4. The exact center theorem (K4)

For a simple complex Lie algebra in the above normalization, set
\(Z_{\rm vac}=\operatorname{End}_{\widehat{\mathfrak g}}V_{\rm crit}\).
The Feigin–Frenkel theorem asserts a coordinate-independent isomorphism
\[
Z_{\rm vac}\simeq
\mathcal O\!\left(\operatorname{Op}_{\check G}(D)\right),
\qquad D=\operatorname{Spec}\mathbb C[[t]],
\tag{K4.1}
\]
where \(\check G\) is adjoint for the dual root system. It includes commutativity of this endomorphism algebra and compatibility with formal changes of coordinate. For a semisimple algebra the corresponding statement uses its simple factors and the critical form on each.

Frenkel's convention in *Lectures on the Langlands program and conformal field theory* is \(-\operatorname{Res}\kappa_0(f,dg)\), equal to our \(+\operatorname{Res}\kappa_0(df,g)\), with critical level \(-2\) in the normalization above. Raskin's *A geometric proof of the Feigin–Frenkel theorem* uses \(+\operatorname{Res}\kappa(f,dg)\), with the central element acting identically and critical form minus half the Killing form. The displayed cocycle directions differ. A comparison of the central line, forms and actions remains required before applying the refinement below under our convention.

The center statement is formulated in Frenkel's [*Lectures on the Langlands program and conformal field theory*, §8.4](https://arxiv.org/abs/hep-th/0512172v1). In the convention of Raskin's [*A geometric proof of the Feigin–Frenkel theorem*, introduction](https://arxiv.org/abs/1106.3112v1), its stronger tensor-compatible Satake assertion is
\[
\Gamma(\operatorname{Gr}_G,\mathcal S_W)
\simeq V^R_{\rm crit}\otimes_{Z^R_{\rm vac}}\mathcal W_{\rm Op},
\tag{K4.2}
\]
where the superscript \(R\) retains that source's vacuum and center convention, \(\mathcal W_{\rm Op}\) comes from the universal dual-group bundle, and \(W\in\operatorname{Rep}(\check G)\). Its proof must construct that universal bundle and compatibility; the formula is not merely an equality of dimensions.

Equations (K4.1)–(K4.2) in their full generality are **not yet proved in this lesson**. Section 3.2 proves (K4.1) for the rank-one vacuum, including all polynomial generators, ordinary base change and coordinate compatibility. The finite-mode, jet-invariant and filtered arguments for \(\mathfrak{sl}_2\) in §3.2 establish the full rank-one polynomial algebra and coordinate action. Section 3.3 proves the general classical current invariants, the PBW upper bound and unconditional vacuum commutativity. The finite-degree reduction to basic lifts and the determinant construction prove the entire type A polynomial vacuum algebra. Basic lifts in other simple types, the full higher-rank coordinate comparison and the Satake assertion (K4.2) remain unproved. The geometric route through affine Grassmannian global sections, semi-infinite cohomology and the birth of opers needs its complete argument and foundations. These classical statements are over \(\mathbb C\). The rank-one vacuum-center proof in §3.2 holds over the full characteristic-zero field convention and every ordinary parameter algebra. The type A polynomial vacuum algebra in §3.3.5 also holds over every characteristic-zero field and ordinary parameter algebra. Field descent for the full higher-rank center/oper comparison and treatment of reductive centers, as well as the completed, chiral, Satake and derived-family center comparisons, remain unproved.

Regular opers on \(D\) and meromorphic opers on \(D^\times\) also give different center statements: the vacuum center uses the first, and the completed enveloping-algebra center uses the second. Neither can silently replace the other.

## 5. Localization and the Hecke property (K5)

For the classical localization statement, fix a connected simply connected simple complex group \(G\). For \(x\in X\), put \(\mathcal O_x=\widehat{\mathcal O}_{X,x}\) and \(F_x=\operatorname{Frac}\mathcal O_x\). The critical affine algebra uses the residue pairing on \(\mathfrak g(F_x)\). The loop and arc groups and the group on \(X-\{x\}\) describe the uniformization presentation
\[
\operatorname{Bun}_G=
G\!\left(\mathcal O(X-\{x\})\right)\backslash
G(F_x)/G(\mathcal O_x).
\tag{K5.1}
\]
This formula as a stack in families needs the Beauville–Laszlo and uniformization proofs, which remain unproved in [The moduli stack of bundles](the-moduli-stack-of-bundles.md). Equality of double-coset point sets does not supply them.

The critical localization functor takes affine Harish–Chandra modules integrable under \(G(\mathcal O_x)\) to left critically twisted D-modules on \(\operatorname{Bun}_G\). Its construction must supply the loop-group action on the critical line, descent through (K5.1), the sheaf of twisted differential operators and compatibility with convolution. These constructions and the classical theorem are described in Beilinson–Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, §§7.8 and 7.14, and Frenkel, *Lectures on the Langlands program and conformal field theory*, §9.2. Their proofs remain required here.

Assuming the actual center identification, an oper \(\chi_x\) on the disc defines a character \(\epsilon_{\chi_x}:Z_{\rm vac,x}\to\mathbb C\) and the underived classical module
\[
V_{\chi_x}=V_{{\rm crit},x}/
\bigl(\ker\epsilon_{\chi_x}\bigr)V_{{\rm crit},x}.
\tag{K5.2}
\]
The complete classical Beilinson–Drinfeld assertion is that its localization is nonzero exactly when \(\chi_x\) extends to a global oper \(\chi\); for global \(\chi\) the resulting object is independent of \(x\). If \(K_{\rm Bun}^{1/2}\) denotes the critical half-canonical line, its untwisting is holonomic and satisfies
\[
\mathsf H_W\!\left(\Delta_x(V_{\chi_x})\otimes K_{\rm Bun}^{-1/2}\right)
\simeq W(E_\chi)\boxtimes
\left(\Delta_x(V_{\chi_x})\otimes K_{\rm Bun}^{-1/2}\right)
\tag{K5.3}
\]
for all dual-group representations \(W\), compatibly with tensor products, unit and fusion. Here \(E_\chi\) is obtained by forgetting the oper reduction while retaining its connection. The half-root and D-module constructions retain the unproved foundations in [Sheaves and D-modules on Bun_G](sheaves-and-d-modules-on-bun-g.md).

The universal-module quotient in (K5.2) is well defined: a module endomorphism commutes with affine action, so the sum of its images for endomorphisms in the ideal is an affine submodule. This elementary check does not prove nonzero localization, holonomicity, independence of \(x\), or (K5.3). Those remain complete-proof obligations. Derived central specialization and its relation to the underived quotient require additional flatness or derived comparison and are retained for the full categorical treatment.

## 6. Quantization and dimensions (K6)

The classical Beilinson–Drinfeld quantization assertion identifies
\[
\Gamma(\operatorname{Bun}_G,\mathcal D_{\rm crit})
\simeq\mathcal O(\operatorname{Op}_{\check G}(X)).
\tag{K6.1}
\]
The order filtration corresponds to the weighted oper filtration, whose associated graded ring is the coordinate ring of the Hitchin base. For \(G=SL_n\) that base is
\[
\mathcal A_{SL_n}=\bigoplus_{i=2}^nH^0(X,\omega^i).
\tag{K6.2}
\]
The invariant coefficients here can be seen directly from a Higgs field: its characteristic-polynomial coefficient of degree \(i\) is a section of \(\omega^i\), and its degree-one trace is zero. Section 1.2.6 proves that these coefficients give the full invariant algebra, and (IS.F10) identifies the associated graded oper ring with the Hitchin-base ring. The global-functions theorem and the filtered isomorphism (K6.1) remain central requirements. The filtered quantization statement is formulated in Frenkel, *Lectures on the Langlands program and conformal field theory*, §9.5. Sections 1.2.2–1.2.5 supply the general principal-degree comparison needed in (DS.G10).

Assume for the following calculation the exact filtered theorem, and the affine-space calculation for \(PGL_2\)-opers. Put \(N=3g-3>0\). Choosing one projective connection gives
\[
\mathcal O(\operatorname{Op}_{PGL_2}(X))\simeq k[z_1,\ldots,z_N].
\tag{K6.3}
\]
Its Krull dimension is \(N\), by the polynomial-ring dimension argument in [The GL_1 case as an equivalence of categories](the-gl-1-case-as-an-equivalence-of-categories.md), with its stated Noether-normalization and integral-extension foundations. Its vector-space dimension is infinite: \(1,z_1,z_1^2,\ldots\) are independent by the monomial basis. The equality with the dimension of the Hitchin base concerns Krull dimension, not a finite-dimensional vector space of all differential operators.

Give each \(z_i\) filtered degree two. The filtered piece of order at most \(2m\), and also the piece of order at most \(2m+1\), has dimension
\[
\dim F_{2m}=\dim F_{2m+1}=\binom{m+N}{N}.
\tag{K6.4}
\]
Indeed a monomial corresponds to a tuple \((a_1,\ldots,a_N)\) of nonnegative integers with sum at most \(m\). Add the slack \(a_{N+1}=m-\sum a_i\). Tuples summing to \(m\) are in bijection with arrangements of \(m\) identical marks and \(N\) separating bars: reading the counts between bars gives the tuple. Choosing the bar positions gives the binomial coefficient. This supplies the full numerical answer even though the filtered quantization theorem itself remains to be proved.

For example, in genus two \(N=3\), the dimensions for \(m=0,1,2,3\) are \(1,4,10,20\). A three-dimensional oper space therefore predicts an infinite algebra whose finite order pieces grow cubically.

## 7. Toward the 2024 theorem (K7)

Arinkin, Beraldo, Campbell, Chen, Faergeman, Gaitsgory, Lin, Raskin and Rozenblyum, [*Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE*, introduction](https://arxiv.org/abs/2405.03648v3), formulate critical localization compatibility with the global Langlands functor and the critical fundamental local equivalence on monodromy-free opers. These statements strengthen the individual eigenobject construction and require their categorical foundations.

For clarity, the monodromy-free oper space in its §3 is the fibre product
\[
\operatorname{Op}^{\rm mf}_{\check G}
=\operatorname{LS}^{\rm reg}_{\check G}
\mathop{\times}_{\operatorname{LS}^{\rm mer}_{\check G}}
\operatorname{Op}^{\rm mer}_{\check G}.
\tag{K7.1}
\]
Thus an object retains an extension of the underlying meromorphic local system to the formal disc, while its oper reduction is allowed on the punctured disc. Replacing this by regular opers would lose objects and derived information. The abelian regular-central-character assertion does not supply the analogous derived statement; that stronger assertion remains unproved here.

In the paper's conventions the critical fundamental local equivalence has target \(\operatorname{IndCoh}^*(\operatorname{Op}^{\rm mf}_{\check G})\); the comparison between this and its \(!\)-version is an additional theorem, not notation for an automatic equality. Its Ran versions enter the compatibility
\[
L_G\circ(\operatorname{Loc}_{G,\rm crit}\otimes\mathfrak l)
\simeq
\operatorname{Poinc}^{\rm spec}_{\check G,*}\circ
\operatorname{FLE}_{G,\rm crit}.
\tag{K7.2}
\]
Here \(\mathfrak l\) is the shifted determinant line displayed in the introduction:
\[
\mathfrak l=
\mathfrak l^{\otimes1/2}_{G,N_{\rho(\omega_X)}}
\otimes\mathfrak l^{-1}_{N_{\rho(\omega_X)}}
[-\delta_{N_{\rho(\omega_X)}}].
\tag{K7.3}
\]
The definitions of these determinant lines, the dimension convention and its exact normalization remain unproved in [Kac-Moody localization and the fundamental local equivalence (GLC II)](kac-moody-localization-and-the-fundamental-local-equivalence.md). Suppressing (K7.3) would erase part of the claimed compatibility.

Equations (K7.1)–(K7.3) retain the factorization categories, Ran operations, affine Skryabin theorem, derived Satake, birth of opers, compactness and convergence requirements at their full scope. This preview neither proves the FLE nor uses it as an established premise. The course's connected reductive and arbitrary algebraically closed characteristic-zero conventions remain required; the classical simply connected complex theorem in K5 is one explicitly scoped input, not a replacement of that goal.

## 8. A regular singular example (K8)

On \(\mathbf P^1-\{0,1,\infty\}\), take the scalar equation on half densities
\[
\left(\partial_z^2-q(z)\right)y=0,\qquad
q(z)=\frac{a}{z^2}+\frac{b}{(z-1)^2}
          +\frac{c}{z(z-1)}.
\tag{K8.1}
\]
Its poles at zero and one have order at most two. At infinity put \(w=1/z\). This is a Möbius change, whose Schwarzian is zero, so the transformed coefficient is
\[
q_w(w)=w^{-4}q(1/w)
=\frac{a}{w^2}+\frac{b}{w^2(1-w)^2}
             +\frac{c}{w^2(1-w)}.
\tag{K8.2}
\]
It also has pole order at most two. Each of the three points is therefore regular singular in the scalar second-order sense: after multiplying by the square of a local parameter, the coefficient is regular, and the first-derivative coefficient is zero.

Writing a local formal leading term \(z^\rho\) gives the indicial equation \(\rho(\rho-1)=a\) at zero. The corresponding equations at one and infinity have right sides \(b\) and \(a+b+c\). For the concrete choice \(a=b=c=1\), the local exponent pairs are
\[
\left\{\frac{1+\sqrt5}{2},\frac{1-\sqrt5}{2}\right\},
\quad
\left\{\frac{1+\sqrt5}{2},\frac{1-\sqrt5}{2}\right\},
\quad
\left\{\frac{1+\sqrt{13}}2,\frac{1-\sqrt{13}}2\right\}.
\tag{K8.3}
\]
These are exponents of the local half-density coefficients; changing a half-density frame can shift their displayed labels. This calculation supplies the coefficients, pole orders and indicial equations, without asserting an unproved analytic monodromy formula or a Riemann–Hilbert comparison.

## 9. Exercises with solutions

**Exercise 8.1.** Compute \(\dim\operatorname{Op}_{PGL_n}(X)\) for \(g\ge2\), and compare with \(\operatorname{Bun}_{SL_n}\).

**Solution 8.1.** Difference operators have symbols \(\omega^n,\ldots,\omega^2\). Each has zero \(H^1\), so their global-section exact sequences give
\[
\dim\operatorname{Op}_{PGL_n}(X)=\sum_{i=2}^n(2i-1)(g-1)=(n^2-1)(g-1).
\]
The first \(n\) odd numbers sum to \(n^2\); remove their initial \(1\). The vector-bundle Euler formula (K1.5)–(K1.6) gives the same deformations-minus-automorphisms number for the bundle stack. Actual stack dimension retains the algebraicity/smoothness foundation in §2.8. No canonical affine origin or filtration splitting is required.

**Exercise 8.2.** Write an oper locally as \(\partial_t^2-q_t\) and compute its change under \(t=\varphi(s)\).

**Solution 8.2.** The cyclic quotient gives a monic operator on \(\theta^{-1}\) with zero first-derivative coefficient. Put \(\lambda=\varphi'\). Its transform is
\(\lambda^{3/2}((\lambda^{-1}\partial_s)^2-q_t(\varphi))\lambda^{1/2}\).
The first-derivative terms cancel and the constant differentiation term is
\(\lambda''/(2\lambda)-3(\lambda')^2/(4\lambda^2)\). Therefore
\[
q_s=\lambda^2q_t(\varphi)-\tfrac12\left(\frac{\varphi'''}{\varphi'}-\frac32\left(\frac{\varphi''}{\varphi'}\right)^2\right).
\]
Differences cancel the Schwarzian and are quadratic differentials. This fixes the density convention and sign.

**Exercise 8.3.** Prove centrality of the \(\mathfrak{sl}_2\) Sugawara vector at critical level.

**Solution 8.3.** Take \(Q\) from (K3.1), or \(Q/2\). Zero modes cancel by the three bracket calculations in §3.1. The mode-one table gives \(x_1Q=2(\ell+2)x_{-1}v\) for \(e,f,h\). Mode two gives zero: \(e,f\) end in killed zero modes; the \(h\) terms are \(2\ell v-2\ell v\). Modes \(m\ge3\) leave a positive mode after commuting twice and kill \(v\). At \(\ell=-2\), smoothness therefore gives a full formal-arc invariant. The induction relations define \(uv\mapsto uQ\), an affine endomorphism. The ordered degree-two symbol is nonzero. Other levels fail by \(e_1Q\ne0\). Centrality of every completed field coefficient is a separate theorem, unused here.

**Exercise 8.4.** Prove irreducibility of the de Rham local system of a regular \(PGL_2\)-oper, \(g\ge2\).

**Solution 8.4.** Its lift is \(J^1\theta^{-1}\), with subline \(\theta\) and quotient \(\theta^{-1}\). An invariant rational line saturates to a regular connection-stable line subbundle \(N\): a primitive local generator forces its scalar connection coefficient to be regular. The degree/Atiyah trace gives \(\deg N=0\). Its map to the quotient is zero, since \(N^{-1}\theta^{-1}\) has degree \(-(g-1)<0\). Thus \(N\subset\theta\). This map is nowhere zero because \(N\) is a subbundle of the ambient rank-two bundle, so \(N=\theta\), contradicting \(\deg\theta=g-1>0\). Analytic monodromy requires its separately recorded comparison.

**Exercise 8.5.** Under BD's precise filtered quantization prediction for \(SL_2\), compare global critically twisted differential operators with the Hitchin base.

**Solution 8.5.** Put \(N=3g-3\). Choosing an oper origin gives the polynomial algebra \(k[z_1,\ldots,z_N]\). Its Krull dimension and \(\dim H^0(\omega^2)\) both equal \(N\); its vector-space dimension is infinite because \(1,z_1,z_1^2,\ldots\) are independent. With filtered weight two on the variables,
\(\dim F_{2m}=\dim F_{2m+1}=\binom{m+N}{N}\), by the monomial/slack-variable bijection in (K6.4). In genus two these dimensions start \(1,4,10,20\). These are complete deductions from the explicit prediction; they do not prove the BD isomorphism.

## 10. What this lesson does not yet prove

The adjoint-semisimple argument proves the finite principal decomposition, unique ordinary-family gauge, coordinate cocycle, intrinsic oper classification, global affine parameter space and dimension from its explicit Lie/group and curve premises. It constructs regular and Laurent coefficient functors, including the continuous coordinate action over nilpotent bases. The independent scalar argument supplies intrinsic/scalar equivalence, normalized lifts, theta choices, ordinary-family representability, Schwarzian, nonsplit extension and algebraic irreducibility. The invariant-ring argument supplies characteristic-zero field transfer, arbitrary ordinary coaction base change, the Molien degree identities, a weighted polynomial Kostant section and the graded classical oper/Hitchin ring. The critical argument supplies the ordered basis, formal affine action, invariant/end correspondence and every-mode \(\mathfrak{sl}_2\) check. Section 3.2 proves the full rank-one polynomial vacuum center, current-jet invariant algebra, PBW exhaustion and coordinate-equivariant ordinary projective-connection identification. Section 3.3 proves the general classical current invariants, exact PBW upper bound, ordinary vacuum-invariant base change, coordinate action on symbols and unconditional vacuum commutativity. Its basic-lift reduction and all-n determinant construction prove the entire type A polynomial vacuum algebra over every ordinary parameter algebra.

Complete proofs remain required for the recursive root-space/pinning, split-unipotent and faithful adjoint-group constructions, ordinary bundle descent, and the recursive Serre/highest-weight and finite-algebra foundations of the invariant-ring proof; non-type-A basic quantum lifts and the full higher-rank coordinate-equivariant vacuum-center/oper comparison, completed punctured-disc center, chiral/Poisson/Satake and derived-family compatibility, and full central-convention comparison; half-root, uniformization, localization, nonzero specialization, holonomicity, tensor/fusion Hecke property and filtered quantization; full derived opers and full-field/reductive-center passages; and the critical FLE, Ran, factorization, determinant, convergence and \(\operatorname{IndCoh}^{*}/\operatorname{IndCoh}^{!}\) foundations. The fixed-curve Picard/coherent/local-algebra/Ext chains, bundle-stack algebraization and optional analytic comparison retain their explicit earlier unproved foundations. Each is a mathematical theorem or construction whose full proof is still required.

Further reading: [Frenkel, *Lectures on the Langlands program and conformal field theory*, §§8–9](https://arxiv.org/abs/hep-th/0512172v1); [Raskin, *A geometric proof of the Feigin–Frenkel theorem*, introduction](https://arxiv.org/abs/1106.3112v1); [Frenkel–Gaitsgory, *Local geometric Langlands correspondence and affine Kac-Moody algebras*, introduction](https://arxiv.org/abs/math/0508382v3); [Beilinson–Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, §§2.6, 3, 7.8 and 7.14](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf); and [Arinkin, Beraldo, Campbell, Chen, Faergeman, Gaitsgory, Lin, Raskin and Rozenblyum, *Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE*, introduction and §3](https://arxiv.org/abs/2405.03648v3).

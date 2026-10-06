# Opers, critical level and the Beilinson–Drinfeld construction

*Draft. Self-checked by the writing AI. Original mathematical exposition: CC0 1.0.*

An oper is a connection with a maximally transverse Borel reduction. The reduction produces scalar differential equations and gives concrete affine families of local systems. At critical level, an affine Lie algebra's center is described by functions on opers. Localization assigns to a global oper a system of differential equations on the bundle stack with a tensor-compatible Hecke eigenproperty.

We construct the adjoint-semisimple principal slice, prove its unique gauge normal form in ordinary families, and derive the coordinate action and global affine oper space. We also prove the homogeneous invariant ring over the stated characteristic-zero field, identify its degrees with the principal heights and construct the weighted Kostant section. A separate scalar proof treats \(PGL_n\) through jets. We also prove the Schwarzian rule, algebraic \(PGL_2\) irreducibility and the critical \(\mathfrak{sl}_2\) invariant. Section 3.2 extends that calculation to the entire rank-one polynomial vacuum center and its coordinate-equivariant ordinary disc-oper comparison. Section 3.3 proves the general current-jet invariant algebra, PBW symbol bound, ordinary-family base change and vacuum commutativity; it constructs every basic type A lift and proves the whole type A polynomial vacuum algebra. Section 3.4 proves the exact quantum coordinate laws and the coordinate-equivariant ordinary disc-oper comparison for every type A factor, including nilpotent parameter families. Section 3.5 proves reductive vacuum factorization, the whole type A reductive polynomial algebra and its framed central coefficient comparison, and the exact algebraic distinction between central frames and gauges. The full center, localization, quantization and fundamental local equivalence theorems remain unproved; their precise statements below retain their complete scope.

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
| Functions on dual-group opers with the full coordinate action | The ordinary oper construction in §§1.1–1.2, the rank-one comparison in §3.2 and the full type A comparison in §3.4 | In other simple types, construct the basic lifts and identify every lower-filtration coordinate term. |

The general basic-lift hypothesis remains open for the other simple types; §3.3.5 supplies the full list for every type A factor. Once such lifts are supplied, the written argument proves the whole polynomial vacuum algebra and its ordinary coefficient extensions. The completed punctured-disc center, critical-level Poisson/chiral structures, Satake compatibility, derived parameter families and central-convention comparison also retain their separate complete-proof obligations in §4.

#### 3.3.5. Basic critical \(\mathfrak{sl}_n\) lifts and the polynomial vacuum center

Work over a field \(k\) of characteristic zero, with \(n\geq2\). For \(n=1\) the form is zero, the sole coefficient \(E_{11}[-1]\) is central, and the traceless quotient is zero, so the empty list of basic traceless lifts needs no separate argument. The determinant construction is due to Chervov–Molev, [*On higher order Sugawara operators*, arXiv:0808.1947v2, Theorem 3.1](https://arxiv.org/abs/0808.1947v2). The calculation below proves the required lift existence from the explicit affine relations. In particular, the determinant cancellation is proved here rather than inferred from a Manin-matrix or vertex-algebra theorem. Its conclusion concerns vacuum vectors and their affine-module endomorphisms. The commutativity argument of §3.3.3 and filtered reduction prove the polynomial vacuum algebra below; §3.4 proves its full ordinary coordinate comparison. Completed, chiral, Poisson, Satake and derived comparisons remain separate assertions.

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

For a direct sum of type A factors, the critical bracket has no cross-factor terms. A basic lift from one factor, with the vacuum in every other factor, is invariant for the entire sum. Its symbol is the corresponding basic polynomial of that factor. Thus the same general reduction proves (SL.C1) with the concatenated lists of generators. The zero Lie algebra gives the coefficient ring. Section 3.4 proves the full quantum coordinate law and ordinary oper comparison for these type A factors. Basic lifting and the coordinate comparison in other simple types, and the completed/chiral/Poisson/Satake/derived comparisons, remain separate proof obligations.


### 3.4. Coordinate laws of scalar opers and critical vacuum centers

#### 3.4.1. Coordinate derivations on the affine vacuum

Use the affine bracket and vacuum of §§3 and 3.3.2. For every integer \(l\ge-1\), define
\[
D_l(x_m)=m x_{m+l},\qquad D_l(K)=0,\qquad D_lv=0.
\tag{TC.A1}
\]
This is an affine derivation. The noncentral terms in its bracket identity have the common coefficient \(m+n\). Its possible central defect on \(x_m,y_n\) is
\[
m(m+l)\kappa(x,y)\delta_{m+n+l,0}
 +nm\kappa(x,y)\delta_{m+n+l,0}=0.
\]
It preserves the induction relations: for \(m\ge0\), either \(m=0\) gives zero or \(m+l\ge0\). Hence it induces an operator on the actual vacuum. It preserves the PBW letter-length filtration, and lowers energy by \(l\), since a replacement of index \(-j\) by \(-j+l\) has that energy shift; further commutations preserve the total shift but can lower letter length. In particular
\[
D_0|_{V_E}=-E\operatorname{Id},\qquad D_{-1}=-T.
\tag{TC.A2}
\]

Direct calculation on every current gives
\[
[D_l,D_q]=(q-l)D_{l+q},\qquad
[D_l,T]=(l+1)D_{l-1}.
\tag{TC.A3}
\]
In the first equality the sole case with \(l+q<-1\) has \(l=q=-1\) and a zero coefficient, so the equality means zero. In the second, \(l=-1\) likewise means zero. For all other indices, the first current calculation is
\(m((m+q)-(m+l))x_{m+l+q}\); the second is \(m(l+1)x_{m+l-1}\). Any difference between the displayed operators and these calculations commutes with all currents and kills the cyclic vacuum, so it is zero on every state.

These operators preserve invariant states. If \(x_mw=0\) for all \(m\ge0\), then
\(x_mD_lw=-m x_{m+l}w=0\); the possible negative index at \(m=0,l=-1\) has zero coefficient. Smoothness extends this to formal nonnegative currents. On the endomorphism algebra, the action is the ordinary commutator:
\[
[D_l,E_w]=E_{D_lw}.
\tag{TC.A4}
\]
Indeed Jacobi and the fact that \(E_w\) commutes with every current show that the left side is another affine endomorphism. Its vacuum image is \(D_lw\), and the induced-module bijection (K2.3) proves the equality. Commutators are derivations for endomorphism composition. All of these arguments hold after every ordinary coefficient extension.

For a state \(w\), write its divided-translation series
\[
W(t)=\sum_{r\ge0}\frac{T^rw}{r!}t^r.
\]
This is a formal series of actual states, with individual finite coefficients. Iterating the second equality in (TC.A3) gives, for \(l\ge0\),
\[
D_l W(t)
=e^{tT}\sum_{s=0}^{l+1}\binom{l+1}{s}t^sD_{l-s}w.
\tag{TC.A5}
\]
To prove it, expand \(e^{-tT}D_le^{tT}\) as iterated commutators. The \(s\)-th commutator is \((l+1)l\cdots(l+2-s)D_{l-s}\), and subsequent terms vanish after \(s=l+1\). Dividing by \(s!\) yields (TC.A5). Equivalently, induction on a single power of \(T\) proves each coefficient, so no exponential convergence assertion is involved. For \(l=-1\), (TC.A2) gives \(D_{-1}W=-W'\).

This reduces the all-coefficient quantum law to finitely many basic-vector calculations. Let \(w_0=v\), \(w_1=0\), and let \(w_k\) be the energy-\(k\) determinant states of §3.3.5. The calculation in §3.4.3 proves
\[
D_jw_k=(j+1)!C_{k,k-j}w_{k-j}
 \quad(1\le j\le k),\qquad
C_{ki}=\binom{n-i}{k-i+1}
 +\frac{1-n}{2}\binom{n-i}{k-i}.
\tag{TC.A6}
\]
Terms with an out-of-range lower index are zero. Modes \(j>k\) already give zero by energy. Then (TC.A5), with \(D_0w_k=-kw_k\) and \(D_{-1}w_k=-Tw_k\), proves
\[
D_lW_k(t)=-t^{l+1}W_k'(t)-k(l+1)t^lW_k(t)
 +\sum_{i=0}^{k-1}C_{ki}
   \bigl(t^{l+1}\bigr)^{(k-i+1)}W_i(t).
\tag{TC.A7}
\]
For the term with \(j=k-i\ge1\), its coefficient in (TC.A5) is
\(\binom{l+1}{j+1}t^{l-j}(j+1)!\), exactly the derivative of \(t^{l+1}\) of order \(j+1\). The two remaining terms are the displayed derivative and weight terms. Derivatives of order greater than \(l+1\) vanish. This proves every boundary case as well. By (TC.A4), the identical formula holds for the corresponding endomorphism series.

The finite basic-vector identity (TC.A6) is proved by the quantum calculations (SL.X6), (SL.X10) and their positive-Witt induction (SL.X13). It is stronger than homogeneity and the classical symbol law (GJ.P10); it retains every lower-filtration term required by the oper comparison.

#### 3.4.2. Full scalar-oper coordinate law

##### Density transport on the full ordinary coordinate group

Let \(k\) be a characteristic-zero field, \(R\) any ordinary commutative \(k\)-algebra, and \(n\geq2\). All derivatives below are relative to \(R\). The finite-jet construction in §§2.2–2.6 of [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), especially (O4.2)–(O4.6), gives the scalar presentation of an ordinary \(PGL_n\)-oper. In a density coordinate its operator is
\[
D_t=\partial_t^n+\sum_{i=2}^n s_i(t)\partial_t^{n-i},
\qquad
h=\frac{1-n}{2},
\qquad
D:F_h\longrightarrow F_{h+n}.
\tag{SC.O1}
\]
Here \(F_h\) denotes the source density frame and \(F_{h+n}\) the target density frame. In the theta presentation these are \(\theta^{1-n}\) and \(\theta^{1+n}\). This notation specifies the two local weights; it does not choose a global trivialization of either line. The coefficient functor in this coordinate is
\[
R\longmapsto\prod_{i=2}^n R[[t]]
=\operatorname{Hom}_{k\text{-alg}}
 \bigl(k[s_{i,r}:2\leq i\leq n,\ r\geq0],R\bigr),
\qquad
s_i(t)=\sum_{r\geq0}s_{i,r}t^r.
\tag{SC.O2}
\]
The finite product permits every power-series coefficient sequence. It uses the completed ring \(R[[t]]\).

First consider a passive coordinate change \(t=\eta(u)\). Write
\(\alpha=\eta'(u)\), so \(\alpha\in R[[u]]^\times\). The full continuous coordinate group also permits a nilpotent constant \(\eta(0)\); it is larger than the subgroup fixing the origin. Section 1.1.8 constructs these substitutions and their inverses over every ordinary \(R\). The finiteness assertion can be seen directly. If \(\eta(0)^\nu=0\), a term contributing to the coefficient of \(u^r\) in \(\eta(u)^m\) uses at least \(m-r\) constant factors. Thus
\[
[u^r]\eta(u)^m=0\quad(m\geq r+\nu),
\qquad
[u^r]F(\eta(u))
=\sum_{m=0}^{r+\nu-1}[t^m]F(t)\,[u^r]\eta(u)^m.
\tag{SC.O3}
\]
No reduction of the ring is involved.

For completeness, the inverse construction also retains nilpotents. Put \(I=(\eta(0))\). Starting with \(a=0\), the iteration
\(a\mapsto a-\eta(a)/\eta'(a)\) takes place in \(I\). Evaluation there is finite, and \(\eta'(a)\) is a unit modulo the nilpotent ideal \(I\), hence a unit. Taylor expansion shows that an error in \(I^d\) becomes an error in \(I^{2d}\). Finitely many steps give a root \(a\in I\). The difference \(\eta(a)-\eta(a')\) is \((a-a')\) times a unit for \(a,a'\in I\), so this root is unique. The pointed series \(\eta(u+a)\) has an inverse by coefficient recursion, using its unit linear coefficient. Adding back \(a\) gives the two-sided continuous inverse of \(\eta\). These formulas prove that the coordinate changes used below are actual automorphisms, including over nonreduced bases.

A density coefficient transforms by
\[
P_w(\eta)f(u)=\alpha(u)^w f(\eta(u)).
\]
For integral \(w\) this is an ordinary formula. Half-integral weights will be justified below. Transporting both the source and target of the operator gives
\[
\begin{aligned}
\mathcal T_\eta(D)
&=P_{h+n}(\eta)\,D\,P_h(\eta)^{-1}\\
&=\alpha^{h+n}
 \left(\sum_{i=0}^n s_i(\eta(u))
          (\alpha^{-1}\partial_u)^{n-i}\right)\alpha^{-h},
\qquad s_0=1,\quad s_1=0.
\end{aligned}
\tag{SC.O4}
\]
The order of the factors matters: the derivative operators act on the factor to their right. Formula (SC.O4) follows by applying the operator to a section, expressing its input in the old density frame, and expressing its output in the new density frame. It is also the transition formula of the jet construction. The chain and product rules defining \(J^{n-1}F_h\) give the following comparison:
\[
\begin{array}{ccc}
D_t:F_h(t)\longrightarrow F_{h+n}(t)
&\xrightarrow{\ (O4.2)\text{--}(O4.6)\ }&
(J^{n-1}F_h,\nabla_D,F_\bullet)_{\mathrm{proj}}\\
\big\downarrow{\mathcal T_\eta}&&
\big\downarrow{\,t=\eta(u)\,}\\
D_u:F_h(u)\longrightarrow F_{h+n}(u)
&\xrightarrow{\ (O4.2)\text{--}(O4.6)\ }&
(J^{n-1}F_h,\nabla_{D_u},F_\bullet)_{\mathrm{proj}} .
\end{array}
\tag{SC.O5}
\]
Every arrow on the right is induced by the finite change-of-jet matrix, whose diagonal entries are units. The horizontal Taylor recursion in (O4.3) commutes with that matrix. Hence the square compares intrinsic connections and flags in ordinary families.

There is no square-root choice in the resulting operator action. If \(n\) is odd, the weights are integral. If \(n\) is even, adjoin a square root of the unit \(\alpha(0)\). The extension \(R[z]/(z^2-\alpha(0))\) is free of rank two and faithfully flat; \(z\) and \(2z\) are units. Recursively solving \(q(u)^2=\alpha(u)\), with \(q(0)=z\), gives a unique series because each new equation has coefficient \(2z\). In this extension the factors in (SC.O4) are \(q^{n+1}\) and \(q^{n-1}\).

If \(\widehat q\) is another root, \(a=\widehat q/q\) satisfies \(a^2=1\). Differentiation gives \(a'=0\), since \(2a\) is a unit. Thus \(a\) commutes with the derivative operators, and replacing \(q\) by \(\widehat q\) multiplies the full expression by \(a^{2n}=1\). This argument allows different signs on different idempotent components. In the jet presentation the source frame changes by the single relatively constant scalar \(a^{1-n}\), and every jet component changes by that same scalar. Its projectivization is unchanged. Section 2.6 supplies the corresponding flat-line comparison between different global theta presentations; the present coordinate calculation requires no global theta frame.

The square-root-free formula below proves descent directly. It also proves the composition law
\[
\mathcal T_\zeta\bigl(\mathcal T_\eta(D)\bigr)
=\mathcal T_{\eta\circ\zeta}(D).
\tag{SC.O6}
\]
Indeed \((\eta\circ\zeta)'=(\eta'\circ\zeta)\zeta'\), and the density pullbacks compose with exactly these two factors. The signs cancel as just proved. Coefficient-finite substitution makes the same identity valid for nilpotent coordinate constants.

##### A finite formula for every transported coefficient

Put \(b=\alpha'/\alpha\). Conjugating one derivative in (SC.O4) gives
\[
\alpha^h(\alpha^{-1}\partial_u)\alpha^{-h}
=\alpha^{-1}(\partial_u-hb)=L.
\]
Consequently
\[
\boxed{\quad
\mathcal T_\eta(D)=
\alpha^n\sum_{i=0}^n s_i(\eta(u))L^{n-i},
\qquad
L=\alpha^{-1}(\partial_u-hb).
\quad}
\tag{SC.O7}
\]
This expression uses integer powers of \(\alpha\), its inverse, relative derivatives and rational constants. It belongs to the original coefficient ring before any square root is adjoined.

Here is an explicit finite coefficient recursion. Define differential operators
\[
B_a=\alpha^a L^a
 =\sum_{d=0}^a C_{a,d}(b)\partial_u^{a-d},
\qquad B_0=1 .
\]
Since
\[
B_{a+1}=(\partial_u-(h+a)b)B_a,
\]
their coefficients satisfy
\[
\begin{gathered}
C_{0,0}=1,\qquad C_{a,d}=0\quad(d<0\text{ or }d>a),\\
C_{a+1,d}
=C_{a,d}+\partial_u C_{a,d-1}
 -(h+a)b\,C_{a,d-1}.
\end{gathered}
\tag{SC.O8}
\]
All \(C_{a,d}\) are finite differential polynomials with rational coefficients. This recursion specifies every one of them, using only \(a\) steps. It also gives
\[
C_{a,0}=1,\qquad
C_{a,1}=-\left(ah+\frac{a(a-1)}2\right)b.
\tag{SC.O9}
\]
For the second identity, each successive factor contributes \(-(h+a)b\) to the next-to-leading coefficient. Their sum is the displayed coefficient.

Write
\(\mathcal T_\eta(D)=\sum_{i=0}^n\widetilde s_i(u)\partial_u^{n-i}\).
Extracting each derivative order from (SC.O7) gives the complete formula
\[
\boxed{\quad
\widetilde s_i(u)
=\sum_{j=0}^i
 \alpha(u)^j s_j(\eta(u))C_{n-j,i-j}(b)
\quad(0\leq i\leq n).
\quad}
\tag{SC.O10}
\]
In particular \(\widetilde s_0=1\). For \(i=1\), the only possible contributions are \(C_{n,1}\) and \(\alpha s_1(\eta)\). They both vanish, because \(h=(1-n)/2\) and \(s_1=0\). This proves monicity and vanishing of the subprincipal coefficient for the full coordinate action.

For \(i\geq2\), the formula has the following triangular structure:

| Contribution to \(\widetilde s_i\) | Exact expression |
|---|---|
| The coefficient of the same order | \(\alpha^i s_i(\eta)\) |
| Lower-index coefficients | \(\sum_{j=2}^{i-1}\alpha^j s_j(\eta)C_{n-j,i-j}(b)\) |
| The coordinate correction of the leading derivative | \(C_{n,i}(b)\) |

The table displays (SC.O10): a scalar coefficient has its weight-\(i\) term, mixing from lower-index coefficients, and a universal correction from the monic leading derivative. It describes the raw scalar coordinates rather than a chosen splitting of the global affine oper torsor.

The quadratic correction has a useful closed form for every \(n\). Put
\[
K_n=\frac{n(n^2-1)}{12},
\qquad
\mathcal S(\eta)=b'-\frac12b^2.
\]
For fixed \(h=(1-n)/2\), set \(m_a=ah+a(a-1)/2=a(a-n)/2\). Summing the recurrence for \(C_{a+1,2}\) gives
\[
C_{n,2}=-\sum_{a=0}^{n-1}m_a\,b'
 +\sum_{a=0}^{n-1}(h+a)m_a\,b^2.
\]
The first sum is \(-K_n\), by the sums of consecutive integers and their squares. For the second, pair \(a\) with \(n-a\): \(m_{n-a}=m_a\) and
\((h+a)+(h+n-a)=1\). The zero endpoint terms allow the pairing over \(0\leq a\leq n\), so the second sum is one half of the first, namely \(-K_n/2\). Therefore
\[
C_{n,2}=K_n\mathcal S(\eta),
\qquad
\widetilde s_2=\alpha^2s_2(\eta)+K_n\mathcal S(\eta).
\tag{SC.O10a}
\]
This proves the scalar Schwarzian coefficient in every order.

The divided Taylor coefficients are
\[
s_{i,r}=[t^r]s_i(t)=\frac{1}{r!}s_i^{(r)}(0).
\]
Set \(s_{0,m}=\delta_{m,0}\) and \(s_{1,m}=0\). For a fixed nilpotence bound \(\eta(0)^\nu=0\), coefficient extraction from (SC.O10) is the finite formula
\[
\boxed{\quad
\widetilde s_{i,r}
=\sum_{j=0}^i
 \sum_{\substack{a+c+d=r\\a,c,d\geq0}}
 [u^a]\alpha^j\,
 [u^d]C_{n-j,i-j}(b)\,
 \sum_{m=0}^{c+\nu-1}s_{j,m}[u^c]\eta(u)^m .
\quad}
\tag{SC.O11}
\]
Thus a fixed transformed coefficient is a polynomial in finitely many original coefficients, coordinate coefficients and the inverse of the linear coordinate coefficient. The rational constants belong to \(k\). More explicitly, the original coefficients used have indices at most \(r+\nu-1\); the coordinate coefficients used have indices at most \(r+n+1\). The latter bound follows because \(C_{a,d}\) uses derivatives of \(b\) of order at most \(d-1\), and \(b=\eta''/\eta'\). Indeed (SC.O8) raises this maximum derivative order by at most one when \(d\) increases by one; its initial coefficient has no derivative. Inverse-series coefficients are determined by finite recursion from the unit \(\eta'(0)\).

Every formula therefore commutes with \(R\to R'\), without flatness or reducedness assumptions. The nilpotence bound may depend on the individual coordinate; an algebra homomorphism preserves any bound already satisfied. On the coordinate chart with \(\eta(0)^\nu=0\), (SC.O11) is an ordinary polynomial formula with the linear coefficient inverted. These charts cover the full continuous coordinate functor. Together with (SC.O6), they give the full ordinary coordinate action, not only its first-order approximation. The same differential-operator formula is valid for finite-pole Laurent coefficients: the finite expansion of \((\eta(0)+u\,a(u))^{-1}\) from §1.1.8 supplies the required Laurent substitution.

##### Inverse variation and all divided coefficient modes

To specify the action on functions, let \(\phi\) be a coordinate automorphism and put \(\psi=\phi^{-1}\). The inverse-pullback action is
\[
(\phi\cdot f)(D)=f(\mathcal T_\psi(D)).
\tag{SC.O12}
\]
This is the convention already used for the projective-connection coefficients in (RC.C4)–(RC.C5). In (SC.O7)–(SC.O11), take \(\eta=\psi\) to obtain its full finite substitution law.

Let \(\phi(t)=t+\epsilon v(t)\), where \(\epsilon^2=0\) and \(v(t)\in R[[t]]\). The constant coefficient \(\epsilon v(0)\) is nilpotent, so this is a coordinate in the full group. Its inverse is \(t-\epsilon v(t)\). For any density weight \(w\),
\[
P_w(\phi)=1+\epsilon A_w(v),
\qquad
A_w(v)=v\partial_t+w v'.
\]
Expanding the source and target transports in (SC.O4) therefore gives
\[
\boxed{\quad
\delta_vD
=-(v\partial_t+(h+n)v')D
  +D(v\partial_t+h v').
\quad}
\tag{SC.O13}
\]
This identity is an equality of finite-order differential operators over \(R[\epsilon]/(\epsilon^2)\).

We calculate every coefficient. The product rule, proved by induction on \(q\), is
\[
\partial_t^q f
=\sum_{a=0}^q\binom qa f^{(a)}\partial_t^{q-a}.
\tag{SC.O14}
\]
The induction differentiates each coefficient and shifts each derivative order; the two contributions combine by Pascal's identity. In (SC.O13), the terms
\(s_jv\partial_t^{n-j+1}\) from \(Dv\partial_t\) and \(-v\partial_tD\) cancel. The latter also contributes \(-v s_j'\partial_t^{n-j}\). At derivative order \(n-i\), the remaining coefficient is
\[
-v s_i'-(h+n)v's_i
+\sum_{j=0}^i s_j
 \left(\binom{n-j}{i-j+1}
       +h\binom{n-j}{i-j}\right)v^{(i-j+1)} .
\]
For \(j=i\), the term in parentheses is \(n-i+h\); combining it with the preceding \(v's_i\) term gives \(-i v's_i\). For \(j=0\), set
\[
\gamma_{n,i}
=\binom n{i+1}+h\binom ni
=-\frac{(i-1)(n+1)}{2(i+1)}\binom ni.
\tag{SC.O15}
\]
The second equality uses
\(\binom n{i+1}=\binom ni(n-i)/(i+1)\) and \(h=(1-n)/2\).
For \(2\leq j<i\), put
\[
a_{n;i,j}
=\binom{n-j}{i-j+1}
   +h\binom{n-j}{i-j}.
\]
Then the full infinitesimal coefficient law is
\[
\boxed{\quad
\delta_v s_i
=-v s_i'-i v's_i
 +\sum_{j=2}^{i-1}a_{n;i,j}s_j v^{(i-j+1)}
 +\gamma_{n,i}v^{(i+1)}
\qquad(2\leq i\leq n).
\quad}
\tag{SC.O16}
\]
The sum is empty for \(i=2\). Binomial coefficients outside their usual range are zero. The order \(n+1\) terms cancel as above; at order \(n\) the remaining coefficient is zero because \(s_0=1\); at order \(n-1\) it is
\(\bigl(\binom n2+hn\bigr)v''=0\), since \(s_1=0\). Thus (SC.O13) preserves both normalized leading coefficients directly.

For arbitrary \(v(t)=\sum_{a\geq0}v_at^a\), let
\((a)_d=a(a-1)\cdots(a-d+1)\), with \((a)_0=1\). Taking the coefficient of \(t^r\) in (SC.O16) gives
\[
\begin{aligned}
\delta_v s_{i,r}
={}&-\sum_{\substack{a+b=r+1\\a,b\geq0}}
       (b+ia)v_a s_{i,b}\\
&+\sum_{j=2}^{i-1}a_{n;i,j}
  \sum_{\substack{a+b=r+i-j+1\\a\geq i-j+1,\ b\geq0}}
      (a)_{i-j+1}v_a s_{j,b}\\
&+\gamma_{n,i}(r+i+1)_{i+1}v_{r+i+1}.
\end{aligned}
\tag{SC.O17}
\]
Each sum is finite. This is the exact law on the divided Taylor coefficients, valid over every ordinary \(R\).

In particular, for \(v(t)=t^{l+1}\), \(l\geq-1\), define \(\delta_l=\delta_v\). The mode formula is
\[
\boxed{
\begin{aligned}
\delta_l s_{i,r}
={}&-\bigl(r+i+(i-1)l\bigr)s_{i,r-l}\\
&+\sum_{j=2}^{i-1}a_{n;i,j}(l+1)_{i-j+1}
       s_{j,r-l+i-j}\\
&+\gamma_{n,i}(l+1)_{i+1}\delta_{r,l-i}.
\end{aligned}}
\tag{SC.O18}
\]
Every coefficient with negative index is defined to be zero. A falling factorial is zero if its nonnegative first argument is smaller than its length. These conventions include all \(l=-1,0\) and all boundary cases. For example,
\[
\delta_{-1}s_{i,r}=-(r+1)s_{i,r+1},
\qquad
\delta_0s_{i,r}=-(r+i)s_{i,r}.
\tag{SC.O19}
\]
Thus divided differentiation shifts the coefficient with its exact factor \(r+1\), and scaling gives weight \(r+i\).

If un-divided jets \(j_{i,r}=s_i^{(r)}(0)=r!s_{i,r}\) are preferred, multiply (SC.O18) by \(r!\). The first term becomes
\[
-\bigl(r+i+(i-1)l\bigr)
  \frac{r!}{(r-l)!}\,j_{i,r-l}
\]
when \(r-l\geq0\), and is zero otherwise. Each term of the inner sum becomes
\[
a_{n;i,j}(l+1)_{i-j+1}
 \frac{r!}{(r-l+i-j)!}\,j_{j,r-l+i-j}
\]
when its index is nonnegative. The scalar term becomes
\(\gamma_{n,i}r!(l+1)_{i+1}\delta_{r,l-i}\).
This specifies both Taylor normalizations without changing the coordinate convention.

##### Schwarzian, cubic mixing and nilpotent translations

The first entries of (SC.O8) are
\[
C_{1,1}=-hb,\qquad
C_{2,1}=-(2h+1)b,\qquad
C_{2,2}=-h b'+h(h+1)b^2.
\]
For \(n=2\), \(h=-1/2\), write
\[
\mathcal S(\eta)=\frac{\eta'''}{\eta'}
 -\frac32\left(\frac{\eta''}{\eta'}\right)^2
=b'-\frac12b^2 .
\]
Then (SC.O10) gives
\[
\widetilde s_2=\alpha^2s_2(\eta)+\frac12\mathcal S(\eta).
\]
With the lesson's convention \(D=\partial^2-q\), so \(s_2=-q\), this is exactly
\[
\widetilde q=\alpha^2q(\eta)-\frac12\mathcal S(\eta),
\qquad
\delta_vq=-vq'-2v'q+\frac12v'''.
\tag{SC.O20}
\]
The mode coefficient is
\[
\delta_lq_r=-(r+l+2)q_{r-l}
 +\frac12(l^3-l)\delta_{r,l-2},
\]
with the same negative-index convention. This recovers the full Schwarzian sign and coefficient in (O7.2) and (RC.C5).

For \(n=3\), \(h=-1\). The recursion gives
\[
\begin{gathered}
B_1=\partial_u+b,\qquad
B_2=\partial_u^2+b\partial_u+b',\\
B_3=(\partial_u-b)B_2
=\partial_u^3+(2b'-b^2)\partial_u+(b''-bb').
\end{gathered}
\]
Since \(2b'-b^2=2\mathcal S(\eta)\) and
\(b''-bb'=\mathcal S(\eta)'\), the entire coordinate law for
\(D=\partial^3+s_2\partial+s_3\) is
\[
\boxed{\quad
\widetilde s_2=\alpha^2s_2(\eta)+2\mathcal S(\eta),
\qquad
\widetilde s_3=\alpha^3s_3(\eta)
 +\alpha\alpha's_2(\eta)+\mathcal S(\eta)'.
\quad}
\tag{SC.O21}
\]
Both lower derivative terms are required. They give
\[
\begin{aligned}
\delta_vs_2&=-vs_2'-2v's_2-2v''',\\
\delta_vs_3&=-vs_3'-3v's_3-s_2v''-v''''.
\end{aligned}
\tag{SC.O22}
\]
Equivalently, the divided coefficients satisfy
\[
\begin{aligned}
\delta_l s_{2,r}
&=-(r+l+2)s_{2,r-l}
  -2(l^3-l)\delta_{r,l-2},\\
\delta_l s_{3,r}
&=-(r+2l+3)s_{3,r-l}
  -(l+1)l\,s_{2,r-l+1}\\
&\hspace{2em}
  -(l+1)l(l-1)(l-2)\delta_{r,l-3}.
\end{aligned}
\]
The corrected coefficient \(w_3=s_3-\tfrac12s_2'\) transforms as a cubic differential:
\[
\widetilde w_3=\alpha^3 w_3(\eta),
\qquad
\delta_vw_3=-vw_3'-3v'w_3.
\tag{SC.O23}
\]
Indeed differentiating the first formula of (SC.O21) gives
\(\tfrac12\widetilde s_2'
=\alpha\alpha's_2(\eta)+\tfrac12\alpha^3s_2'(\eta)+\mathcal S(\eta)'\);
subtract it from the second formula. This proves the cubic assertion and displays the derivative correction explicitly.

Finally take \(R=k[a]/(a^\nu)\) and \(\eta(u)=u+a\). This is a genuine nonpointed continuous coordinate. Here \(\alpha=1\), \(b=0\), all \(C_{a,d}\) with \(d>0\) vanish, and the full transport is \(s_i(u+a)\). The coefficient formula becomes
\[
\widetilde s_{i,r}
=\sum_{q=0}^{\nu-1}\binom{r+q}{r}a^q s_{i,r+q}.
\tag{SC.O24}
\]
For the inverse action replace \(a\) by \(-a\). Thus nilpotent translations are finite on each coefficient even though they can involve coefficients beyond a fixed pointed jet truncation.

For \(n=1\), the normalized operator is \(\partial_t:F_0\to F_1\); (SC.O7) gives \(\mathcal T_\eta(\partial_t)=\partial_u\). There are no scalar coefficients and the \(PGL_1\) coefficient functor is a point.

These are complete algebraic coordinate formulas for the ordinary scalar-oper coefficient functor. Their identification with intrinsic opers uses the finite-jet, vector-lift and ordinary bundle-descent inputs specified in §§2.2–2.6. The recursive global curve/Picard foundations in §2.1 and the bundle-algebraization foundation in §2.8 remain unproved in their stated global uses. No such global theorem is needed for the coefficient recursion or its ordinary base change. The coefficients here are those of the scalar differential operator (SC.O1); Section 3.4.3 compares these coefficients with the quantum determinant generators. Completed centers, chiral or Poisson structures and derived parameter spaces require their separate mathematical arguments.

#### 3.4.3. Quantum coordinate law of the critical determinant

Let \(k\) have characteristic zero. We use the critical affine matrix bracket (SL.L1)–(SL.L3), the right-ordered determinant coefficients (SL.L4)–(SL.L7), and the proved exterior relations (SL.L8)–(SL.L12). The determinant construction is credited there to Chervov–Molev, [*On higher order Sugawara operators*, arXiv:0808.1947v2](https://arxiv.org/abs/0808.1947v2). The raw coefficients already have the law of an order-\(n\) scalar density operator from weight \(h=(1-n)/2\) to weight \(h+n\). No triangular derivative correction is required for this law. The calculation below includes the lower-filtration terms, the scalar anomaly, every divided translate, and ordinary coordinate substitutions with nilpotent constant coefficient.

##### SL.X1. The operators and pinned minors

Initially work in \(\mathfrak{gl}_n\), with
\(\kappa(X,Y)=-n\operatorname{tr}(XY)+\operatorname{tr}(X)\operatorname{tr}(Y)\), \(K=1\), and \(T=\tau\) on the vacuum. Introduce the central parameter \(u\), and write
\[
M_{aj}(u)=\delta_{aj}(T+u)+E_{aj}[-1],\quad
\theta_j=\sum_a\psi_aM_{aj}(u),\quad
P=\theta_1\cdots\theta_n=\Psi D(u).
\]
\[
\Psi=\psi_1\cdots\psi_n,\qquad
F(u)=D(u)v=\sum_{k=0}^n w_k u^{n-k},\qquad w_0=v,\quad w_k=S_kv.
\tag{SL.X1}
\]
Each \(\psi_a\) anticommutes with every exterior-odd expression and commutes with every ordinary operator coefficient. The \(\theta_j\) anticommute by the already proved explicit affine identity (SL.L8), not by an additional determinant theorem.

For a set \(J\subseteq\{1,\ldots,n\}\), let \(P_J\) be the ordered product with \(\theta_j\) replaced by \(\psi_j\) at precisely its positions in \(J\), and let \(D_J(u)\) delete those same rows and columns from \(M(u)\). Expansion gives
\[
P_J=\Psi D_J(u),\qquad
\partial_u^a P=a!\sum_{|J|=a}P_J.
\tag{SL.X2}
\]
Here the pinned sign is positive. A surviving permutation fixes every index in \(J\). Moving those fixed rows to the front and moving those fixed columns to the front use the same sequence of index positions, so their signs multiply to \(+1\); the remaining sign is the permutation sign on the ordered complement. No operator coefficient is reordered in this argument. The derivative formula follows from the finite product rule: a factor can be differentiated only once, with derivative \(\psi_j\), and each chosen set of \(a\) factors occurs in its \(a!\) possible differentiation orders. We abbreviate \(P_{\{i,j\}}=P_{ij}\), and similarly for minors and triples.

For \(l\geq-1\), current substitution has infinitesimal action
\[
[D_l,E_{ab}[r]]=rE_{ab}[r+l],\qquad D_lv=0.
\tag{SL.X3}
\]
This is the ordinary affine derivation proved in (RC.C1). Directly, its possible central defect is \(r(r+s+l)\kappa(X,Y)\delta_{r+s+l,0}=0\). Nonnegative currents remain nonnegative; for \(l=-1,r=0\) the coefficient is zero. Thus it acts on the induced vacuum. Comparing on currents and on the cyclic vacuum proves
\[
[D_l,D_m]=(m-l)D_{l+m},\qquad
[D_l,T]=(l+1)D_{l-1}\ (l\geq0),\qquad D_{-1}=-T.
\tag{SL.X4}
\]
In particular \([D_0,\theta_j]=-\theta_j+u\psi_j\). The product rule already gives \(D_0F=(u\partial_u-n)F\), so \(D_0w_k=-kw_k\).

##### SL.X2. The complete D1 calculation

Put
\[
H_i=\sum_a\psi_a E_{ai}[0],\qquad
Z_i=2\psi_iD_0-H_i.
\]
Then \([D_1,\theta_i]=Z_i\) and \(Z_iv=0\). Formula (SL.L12), summed against \(\psi_a\), proves
\[
\{H_i,\theta_j\}=-\psi_i\theta_j-\psi_j\theta_i,
\qquad
\{Z_i,\theta_j\}=-\psi_i\theta_j+\psi_j\theta_i+2u\psi_i\psi_j.
\tag{SL.X5}
\]
For the first identity, the sum is
\(\sum_a\psi_a(\psi_iM_{aj}-\delta_{aj}\theta_i)\), which is exactly its displayed right side. For the second, use
\(2\psi_i[D_0,\theta_j]-\{H_i,\theta_j\}\).

In the product-rule term inserting \(Z_i\) in column \(i\), move it through each later column until it reaches \(v\), where it is zero. Its interaction with a later column \(j\) has a sign \((-1)^m\), \(m=j-i-1\), from the intermediate odd factors. The three terms in (SL.X5) give
\[
-P_i-P_j+2uP_{ij}.
\]
The signs are explicit: moving \(\psi_i\) left past the \(m\) intermediate factors supplies \((-1)^m\), canceling the interaction sign in the first and third terms. In the second, first \(\psi_j\theta_i=-\theta_i\psi_j\), and then moving \(\theta_i\) left past those \(m\) factors supplies another \((-1)^m\). Its result is therefore \(-P_j\). Summing all pairs, each single pinned position belongs to \(n-1\) pairs. By (SL.X2),
\[
\boxed{D_1F(u)=uF''(u)-(n-1)F'(u).}
\tag{SL.X6}
\]
This is an equality of actual vacuum vectors, before passage to symbols.

##### SL.X3. The complete D2 calculation and its central correction

Set
\[
R_i=\sum_a\psi_aE_{ai}[1],\qquad B_i=3\psi_iD_1-R_i.
\]
Then \([D_2,\theta_i]=B_i\) and \(B_iv=0\). Use the full entry bracket (SL.L14), including its trace and critical central terms. Summing it gives
\[
\{R_i,\theta_j\}=-2\psi_jH_i-\psi_iH_j+(n+1)\psi_i\psi_j.
\tag{SL.X7}
\]
Indeed the four types of terms in that sum are
\(\sum_a\psi_a\psi_jE_{ai}[0]=-\psi_jH_i\),
\(\sum_a\psi_a\psi_iE_{aj}[0]=-\psi_iH_j\),
\(-\psi_jH_i\), and
\(\psi_i\psi_j-n\psi_j\psi_i=(n+1)\psi_i\psi_j\).
Consequently
\[
\{B_i,\theta_j\}=K_{ij}-(n+1)\psi_i\psi_j,
\quad
K_{ij}=6\psi_i\psi_jD_0-2\psi_iH_j+2\psi_jH_i.
\tag{SL.X8}
\]
The operator \(K_{ij}\) is even and kills \(v\). Its full commutator with a later column is
\[
[K_{ij},\theta_k]
=-2\psi_i\psi_j\theta_k+2\psi_i\psi_k\theta_j
-2\psi_j\psi_k\theta_i+6u\psi_i\psi_j\psi_k.
\tag{SL.X9}
\]
To verify every coefficient, use
\([D_0,\theta_k]=-\theta_k+u\psi_k\) and
\([\psi_iH_j,\theta_k]=\psi_i\{H_j,\theta_k\}
=-\psi_i\psi_j\theta_k-\psi_i\psi_k\theta_j\).
The corresponding formula with \(i,j\) swapped gives the remaining terms of (SL.X9). The coefficients of \(\psi_i\psi_j\theta_k\) are \(-6+2+2=-2\). There is no uncomputed operator remainder.

Move \(B_i\) through the later columns. At each \(i<j\), the scalar part of (SL.X8) gives \(-(n+1)P_{ij}\): its interaction sign \((-1)^{j-i-1}\) cancels the sign needed to pin \(\psi_i\). The even part \(K_{ij}\) is moved through each still later column, by its ordinary commutator (SL.X9), until it kills the vacuum. Thus these terms are indexed exactly by triples \(i<j<k\).

For clarity, set \(m=j-i-1\), \(p=k-j-1\). A triple term has the initial interaction sign \((-1)^m\), with the ordered intervening blocks of lengths \(m\) and \(p\). The following table gives all its contributions; the common \(\Psi\) is suppressed in the last column.

| Term in (SL.X9) | Sign from moving to the pinned column positions, before the interaction sign | Final contribution |
|---|---|---|
| \(-2\psi_i\psi_j\theta_k\) | \((-1)^{m+p}(-1)^p=(-1)^m\) | \(-2D_{ij}\) |
| \(+2\psi_i\psi_k\theta_j\) | \(-(-1)^{m+p}(-1)^p=(-1)^{m+1}\) | \(-2D_{ik}\) |
| \(-2\psi_j\psi_k\theta_i\) | \((-1)^{m+p}(-1)^p=(-1)^m\) | \(-2D_{jk}\) |
| \(+6u\psi_i\psi_j\psi_k\) | \((-1)^{m+p}(-1)^p=(-1)^m\) | \(+6uD_{ijk}\) |

In the second row the extra minus is moving \(\theta_j\) past \(\psi_k\); move \(\psi_i\) left across both intervening blocks and then \(\theta_j\) left across the second block. In the third row moving \(\theta_i\) past both pinned generators has sign \(+1\); move it left across both blocks and then move \(\psi_j\) left across the second block. The other rows move the first pinned generator across both blocks and the second across the second block. This accounts for every odd interchange and preserves the order of all unpinned operator coefficients.

Every pair belongs to exactly \(n-2\) triples. Hence its total coefficient is
\(-(n+1)-2(n-2)=-3(n-1)\). The triple coefficient is \(6u\). Formula (SL.X2) now proves
\[
\boxed{D_2F(u)=uF'''(u)-\frac32(n-1)F''(u).}
\tag{SL.X10}
\]
The \(n+1\) in (SL.X7) is essential: it is the finite trace/critical correction, rather than a symbol-level calculation.

##### SL.X4. Every basic vector and every positive Witt derivation

Put \(h=(1-n)/2\), and define ordinary differential operators in the auxiliary variable
\[
\mathcal A_l=u\partial_u^{l+1}+(l+1)h\partial_u^l\qquad(l\geq1).
\]
Equations (SL.X6) and (SL.X10) say \(D_1F=\mathcal A_1F\) and \(D_2F=\mathcal A_2F\). The elementary rule
\(\partial_u^a u=u\partial_u^a+a\partial_u^{a-1}\) gives
\[
[\mathcal A_1,\mathcal A_l]=-(l-1)\mathcal A_{l+1}.
\]
Here the coefficient of \(u\partial_u^{l+2}\) is \(2-(l+1)=-(l-1)\), and the constant coefficient of \(\partial_u^{l+1}\) is
\(h(2-l(l+1))=-(l-1)(l+2)h\).
Since \(D_l\) acts only on the vector coefficients and commutes with \(u,\partial_u\),
\([D_1,D_l]F=(\mathcal A_l\mathcal A_1-\mathcal A_1\mathcal A_l)F\).
Using (SL.X4), induction from \(l=2\), dividing by \(l-1\), proves
\[
\boxed{D_lF=u\partial_u^{l+1}F+(l+1)h\partial_u^lF\quad(l\geq1).}
\tag{SL.X11}
\]
This argument is the actual finite positive-Witt generation proof; it assumes no coordinate law of the coefficients.

Define binomial coefficients outside their usual nonnegative range to be zero, and set
\[
C_{ki}=\binom{n-i}{k-i+1}+h\binom{n-i}{k-i}\qquad(0\leq i<k\leq n).
\tag{SL.X12}
\]
Reading the coefficient of \(u^{n-k}\) in (SL.X11) proves
\[
\boxed{D_lw_k=(l+1)!C_{k,k-l}w_{k-l}\quad(1\leq l\leq k),
\qquad D_lw_k=0\quad(l>k).}
\tag{SL.X13}
\]
Together with \(D_0w_k=-kw_k\) and \(D_{-1}w_k=-Tw_k\), this is the full basic-vector action. In particular,
\[
D_1w_k=-(k-1)(n-k+1)w_{k-1},
\]
\[
D_2w_k=-\frac{(n-k+2)(n-k+1)(n+2k-3)}2w_{k-2}.
\tag{SL.X14}
\]
These are exact quantum identities; their right sides give all lower-length corrections for the basic vectors.

##### SL.X5. The traceless quotient does not remove the trace correction

The ideal generated by \(I[r]=\sum_aE_{aa}[r]\) is stable under \(D_l\), since \(D_lI[r]=rI[r+l]\). Consequently all preceding identities pass to the traceless vacuum, with \(w_k=\overline S_kv\), \(w_0=v\), and \(w_1=0\).

The central term \(+\delta_{ab}\delta_{ij}\) of (SL.L14) must remain in the traceless matrix notation. Indeed for
\(F_{ab}=E_{ab}-\delta_{ab}I/n\),
\[
-n\operatorname{tr}(F_{ab}F_{ij})
=-n\delta_{bi}\delta_{aj}+\delta_{ab}\delta_{ij}.
\tag{SL.X15}
\]
Thus taking the quotient agrees with the same \(n+1\) in (SL.X7); dropping it would give a different and incorrect coordinate anomaly. Also
\(C_{10}=\binom n2+hn=0\), so the resulting subprincipal coefficient remains zero under the whole law.

##### SL.X6. Every divided translate and the complete coefficient series

Let \(A_{k,r}\) be the endomorphism with vacuum image \(T^rw_k/r!\), and put
\(A_{0,0}=\operatorname{Id}\), \(A_{0,r}=0\) for \(r>0\), \(A_{1,r}=0\), and \(A_{k,r}=0\) for \(r<0\). These conventions refer to the traceless quotient. The proved all-integer reconstruction (VC.17)–(VC.20) identifies its invariant field with the regular series
\[
s_k(t)=Y(w_k,t)=\sum_{r\geq0}A_{k,r}t^r,
\qquad s_0=1,\quad s_1=0.
\tag{SL.X16}
\]
All nonnegative field modes vanish as actual operators by (VC.18) and cyclicity. Thus (SL.X16) describes the entire reconstructed field, not a truncation imposed by hand.

The conjugation action on an endomorphism satisfies
\([D_l,E_w]=E_{D_lw}\). Its commutator with a current is zero by Jacobi and (SL.X3), and its vacuum image is \(D_lw\); the induction correspondence then proves the assertion. Repeated use of (SL.X4) gives, for \(l\geq0\),
\[
D_l\frac{T^rw_k}{r!}
=\sum_{a=0}^{\min(r,l+1)}
\frac{(l+1)_{\underline a}}{a!(r-a)!}\,
T^{r-a}D_{l-a}w_k.
\tag{SL.X17}
\]
Here \((b)_{\underline a}=b(b-1)\cdots(b-a+1)\). The formula follows by induction on \(r\): moving \(D_l\) across the last \(T\) supplies \((l+1)D_{l-1}\), and the two adjacent binomial terms combine. Equivalently, its iterated right commutators with \(T\) are \((l+1)_{\underline a}D_{l-a}\) through \(a=l+1\), after which the commutator of \(-T\) with \(T\) is zero. This proves both the finite sum and its last boundary term.

Inserting (SL.X13) into (SL.X17) yields the following fully explicit action on the endomorphisms, for \(l\geq0\):
\[
\begin{split}
[D_l,A_{k,r}]={}&
-\mathbf1_{r\geq l}\bigl(r-l+k(l+1)\bigr)A_{k,r-l}\\
&+\sum_{i=0}^{k-1} C_{ki}(l+1)_{\underline{k-i+1}}
A_{i,r-l+k-i}.
\end{split}
\tag{SL.X18}
\]
A term with a negative coefficient index is zero. A falling factorial is zero if its order exceeds \(l+1\). To see the matching coefficients explicitly, in the first part of (SL.X17) put \(i=k-l+a\). Its factor becomes \((l+1)!/(l-k+i)!\), exactly the falling factorial in (SL.X18). The remaining terms \(a=l\) and \(a=l+1\) contribute \(-k(l+1)\) and \(-(r-l)\) when present. For \(l=0\) this gives \(-(k+r)A_{k,r}\). For \(l=-1\), directly \([D_{-1},A_{k,r}]=-(r+1)A_{k,r+1}\).

Therefore, for \(v(t)=t^{l+1}\), \(l\geq-1\), summing the coefficients gives
\[
\boxed{
\delta_v s_k=-v s_k'-kv's_k
+\sum_{i=0}^{k-1}C_{ki}v^{(k-i+1)}s_i.
}
\tag{SL.X19}
\]
For a general formal vector field the same formula is extended linearly. Each fixed generator has finite energy \(k+r\), so \(D_l\) vanishes on it for \(l>k+r\); thus this formal action uses actual finite sums on each generator. The formula lists every lower-filtration term. No additional term can be hidden by passage to symbols: (SL.X6), (SL.X10), positive-Witt induction and (SL.X17) were all exact operator/vector identities.

##### SL.X7. Equality with the scalar density law

Set
\[
\mathcal L=\partial_t^n+s_2(t)\partial_t^{n-2}+\cdots+s_n(t)
=\sum_{i=0}^n s_i(t)\partial_t^{n-i}.
\]
As an operator from density weight \(h\) to weight \(h+n\), inverse coordinate pullback has variation
\[
\delta_v\mathcal L
=-(v\partial_t+(h+n)v')\mathcal L
+\mathcal L(v\partial_t+hv').
\tag{SL.X20}
\]
We can compare it without assuming any quantum–oper identification. The finite Leibniz rule
\(\partial^m f=\sum_{a=0}^m\binom ma f^{(a)}\partial^{m-a}\)
follows inductively by the ordinary product rule. Apply it with \(m=n-i\). At coefficient \(\partial^{n-k}\), the \(i=k\) terms are exactly
\(-v s_k'-kv's_k\); for \(i<k\), the two coefficients are
\(\binom{n-i}{k-i+1}v^{(k-i+1)}s_i\) and
\(h\binom{n-i}{k-i}v^{(k-i+1)}s_i\).
Their sum is (SL.X12). Thus (SL.X20) is precisely the proved quantum law (SL.X19).

In particular
\[
C_{20}=\binom n3+h\binom n2=-\frac{n(n^2-1)}{12},
\]
\[
\boxed{\delta_v s_2=-v s_2'-2v's_2-\frac{n(n^2-1)}{12}v'''.}
\tag{SL.X21}
\]
For \(n=2\), \(w_2=-Q/2\) by (SL.L23)'s normalization check; the scalar operator is \(\partial^2-q\), so \(s_2=-q\). This reproduces the rank-one factor two and Schwarzian sign in (RC.C3)–(RC.C6).

The raw coefficients are oper coefficients, not all primary tensor coefficients. For example, for \(n=3\), (SL.X19) gives
\[
\delta_v s_3=-v s_3'-3v's_3-v''s_2-v''''.
\]
Its lower terms agree exactly with the density calculation. The reparameterization
\(s_3-s_2'/2\), equivalently \(w_3-Tw_2/2\), is a primary cubic coefficient. Substituting (SL.X21) and differentiating proves that its \(v''s_2\) and \(v''''\) terms cancel. This optional change produces a primary coordinate; it is not a correction needed to make the raw determinant a scalar oper.

##### SL.X8. Finite substitutions and ordinary families

Let \(t=\phi(s)\) be a continuous invertible ordinary coordinate substitution, with nilpotent constant coefficient, and let \(\lambda=\phi'(s)\) be its power-series unit. The scalar forward pullback is
\[
\mathcal P_\phi(\mathcal L)
=\lambda^{h+n}\left.\mathcal L\right|_{t=\phi(s),\ \partial_t=\lambda^{-1}\partial_s}\lambda^{-h}.
\tag{SL.X22}
\]
The apparent half powers need no chosen square root in the resulting coefficients. Here is an explicit algebraic recursion that removes them and also specifies every finite lower correction. Define \(B_{0,0}=1\), all out-of-range \(B_{m,r}=0\), and
\[
B_{m+1,r}=\lambda^{-1}
\left(B_{m,r}'-h\frac{\lambda'}\lambda B_{m,r}+B_{m,r-1}\right).
\tag{SL.X23}
\]
Induction by the product rule proves
\((\lambda^{-1}\partial_s)^m\lambda^{-h}
=\lambda^{-h}\sum_{r=0}^mB_{m,r}\partial_s^r\).
It can be read formally using \((\lambda^a)'=a\lambda^a\lambda'/\lambda\); after the common \(\lambda^{-h}\) is removed, the recursion uses only \(\lambda^{\pm1}\) and its derivatives. Thus the complete coefficient formula is
\[
\boxed{
\mathcal P_\phi(s_k)
=\lambda^n\sum_{i=0}^k s_i(\phi(s))B_{n-i,n-k}.
}
\tag{SL.X24}
\]
It is a finite differential polynomial in the indicated coefficients and \(\lambda^{\pm1}\), valid in every ordinary coefficient algebra. In particular \(B_{m,m}=\lambda^{-m}\) and
\(B_{m,m-1}=-\bigl(mh+m(m-1)/2\bigr)\lambda^{-m}\lambda'/\lambda\), by direct induction in (SL.X23). For \(m=n\) the latter coefficient is zero. Hence the leading coefficient remains one and \(s_1=0\) remains zero.

For its quadratic term put \(q=\lambda'/\lambda\). The same recursion writes
\(B_{m,m-2}=\lambda^{-m}(b_mq^2+c_mq')\), with
\(b_{m+1}=b_m+a_m(m+h)\), \(c_{m+1}=c_m-a_m\), \(a_m=mh+m(m-1)/2\), and \(b_1=c_1=0\).
With \(h=(1-n)/2\), the finite sums give
\(c_n=n(n^2-1)/12\) and \(b_n=-n(n^2-1)/24\).
For example, the first sum is
\(-h n(n-1)/2-n(n-1)(n-2)/6\); the second is
\(\tfrac14\sum_{m=1}^{n-1}m(m-n)(2m-n+1)\), giving the displayed value by expanding its three powers. Consequently
\[
\mathcal P_\phi(s_2)
=\lambda^2s_2(\phi)+\frac{n(n^2-1)}{12}
\left(\frac{\phi'''}{\phi'}-\frac32\left(\frac{\phi''}{\phi'}\right)^2\right).
\tag{SL.X25}
\]
This has the negative scalar anomaly in (SL.X21) on inverse pullback, as required.

Current substitution is \(xF(t)\mapsto xF(\phi(t))\). On the scalar coefficient ring its corresponding action is **inverse** pullback, \(f\mapsto f\circ\mathcal P_{\phi^{-1}}\); differentiating \(\phi=t+\epsilon v\) gives (SL.X20), with its specified minus signs. Both actions preserve the residue cocycle and the vacuum, by the finite nilpotent substitution and residue proof (RC.C7). They also satisfy the same substitution-composition law, since (SL.X22) is just conjugation of an actual operator between the two density weights.

To prove that the infinitesimal equality integrates, factor an ordinary substitution as a nilpotent translation, a scaling, and a pointed unit-linear substitution, as constructed in §1.1.8 and (RC.C7). A translation acts by \(\exp(a_0D_{-1})\), a finite sum because \(a_0\) is nilpotent. A scaling \(t\mapsto at\) acts on \(A_{k,r}\) by \(a^{-k-r}\), equal to inverse density pullback. For the remaining substitution, successively remove its coefficients using \(\exp(c_l t^{l+1}\partial_t)\), \(l\geq1\): the first still-unmatched coefficient is exactly \(c_l\), so it is uniquely removed at that step. Each fixed coordinate coefficient needs finitely many steps. On the quantum or scalar polynomial ring, \(D_l\) lowers the positive energy \(k+r\) by \(l\), so is locally nilpotent, and \(l>k+r\) acts trivially on a generator. Equality of the exact derivations (SL.X18) therefore implies equality of their finite exponentials and their coefficientwise successive products. The translation and scaling factors complete the proof for every ordinary substitution, including nonreduced parameters.

Finally, (SL.C1) gives the whole ordinary type-A polynomial vacuum algebra, and the scalar-oper construction (O3)–(O5) gives the polynomial ring on the coefficients of \(\mathcal L\). Write \(s_{k,r}\) for the independent coefficient coordinates in that scalar-oper ring. The map
\[
A_{k,r}\longmapsto s_{k,r}\qquad(2\leq k\leq n,\ r\geq0)
\tag{SL.X26}
\]
is therefore an algebra isomorphism, with the specified determinant normalization. Equations (SL.X18)–(SL.X24) and the integration argument prove its coordinate equivariance over every ordinary parameter algebra. Products of type-A factors are handled componentwise. This establishes the type-A ordinary formal-disc coordinate comparison at the previously stated scalar-oper and invariant-theory foundations. It does not prove a punctured-disc completed center, chiral/Poisson/Satake compatibility, a derived-family comparison, or basic lifting and coordinate identification in other types.

#### 3.4.4. General quadratic critical states and their coordinate action

Let \(k\) be a field of characteristic zero and let \(\mathfrak g\) be a finite-dimensional split semisimple Lie algebra. Fix a nondegenerate symmetric invariant form \(B\), with dual bases \(a_\alpha,a^\alpha\). The form \(B\) identifies the current coordinates with their duals; it is separate from the affine form \(\kappa\). Write
\[
 [x_m,y_j]=[x,y]_{m+j}+m\kappa(x,y)\delta_{m+j,0}\,1.
 \tag{GQ.1}
\]
The vacuum \(v\) is annihilated by \(\mathfrak g[[t]]\). The PBW construction, its smooth finite-energy bound, the induced-module universal property, and the ordinary-base-change result of §3.3.2 are the foundations used below. The endomorphism commutativity proved in §3.3.3 is available once a state is shown to be invariant. No assertion about the higher-degree generators of the centre is needed here.

For an invariant form \(F\), define \(K_F\in\operatorname{End}_k(\mathfrak g)\) by
\[
 B(K_Fx,y)=F(x,y),\qquad C_B=K_{\mathrm{Kil}},
 \quad \mathrm{Kil}(x,y)=\operatorname{tr}(\operatorname{ad}x\operatorname{ad}y).
 \tag{GQ.2}
\]
Define the half-Casimir state and its normally ordered modes by
\[
 Q=\frac12\sum_\alpha(a_\alpha)_{-1}(a^\alpha)_{-1}v,
 \qquad
 S_n=\frac12\sum_{\alpha,j\in\mathbb Z}:(a_\alpha)_j(a^\alpha)_{n-j}:.
 \tag{GQ.3}
\]
Our ordering convention places the first mode to the left when its index is negative and to the right when its index is nonnegative. The sum defining \(S_n\) is an operator on the smooth vacuum module: for each input vector, the positive mode at the right kills that vector once its index exceeds a fixed bound. All sums below have this meaning.

**The inverse-form tensor and the Killing correction.** The tensor \(\sum a_\alpha\otimes a^\alpha\) is symmetric and invariant. Symmetry follows from the symmetric inverse Gram matrix. To prove invariance, pair its simultaneous adjoint variation with \(y\otimes z\), using \(B\) in each factor. The result is
\[
 -B([x,y],z)-B(y,[x,z])=0.
\]
Consequently
\[
 \sum_\alpha[a_\alpha,a^\alpha]=0,
 \qquad
 \sum_\alpha[[x,a_\alpha],a^\alpha]=C_Bx.
 \tag{GQ.4}
\]
For the second identity, pairing with \(y\) gives
\[
 \begin{aligned}
 B\left(\sum_\alpha[[x,a_\alpha],a^\alpha],y\right)
 &=-\sum_\alpha B([x,a_\alpha],[y,a^\alpha])\\
 &=\sum_\alpha B(\operatorname{ad}y\operatorname{ad}x(a_\alpha),a^\alpha)
 =\mathrm{Kil}(x,y).
 \end{aligned}
\]
This proves the required arbitrary-type Casimir identity directly from the invariant pairing. Two further contractions are
\[
 \sum_\alpha\kappa([x,a_\alpha],a^\alpha)=0,
 \qquad
 \sum_\alpha\kappa(a_\alpha,a^\alpha)=\operatorname{tr}(K_\kappa).
 \tag{GQ.5}
\]
Indeed, interchange the two factors of the symmetric tensor in the first sum and use invariance of \(\kappa\): the sum becomes its own negative. The second equality is the dual-basis trace formula.

**The all-integer current commutator.** Put \(\theta(j)=1\) for \(j\geq0\) and \(0\) otherwise. Moving the first factor across the ordering boundary gives
\[
 \begin{aligned}
 [x_m,:a_jb_{n-j}:]
 &=:[x_m,a_j]b_{n-j}:+:a_j[x_m,b_{n-j}]:\\
 &\quad +(\theta(j+m)-\theta(j))[[x,a]_{j+m},b_{n-j}].
 \end{aligned}
 \tag{GQ.6}
\]
This identity follows by writing the two possible orders before and after the commutator. Their difference is precisely the bracket of the two factors when the first index crosses zero. Central terms in the inner current bracket cause no additional ordering difference.

In the sum (GQ.3), reindexing the ordinary Lie terms in (GQ.6) makes them the simultaneous adjoint variation of the inverse-form tensor, hence zero. The two affine central terms contribute
\[
 \frac m2\sum_\alpha
 \bigl(\kappa(x,a_\alpha)(a^\alpha)_{m+n}
       +\kappa(x,a^\alpha)(a_\alpha)_{m+n}\bigr)
 =m(K_\kappa x)_{m+n}.
\]
The boundary double bracket is \((C_Bx)_{m+n}\), by (GQ.4). Its possible scalar part is
\((j+m)\delta_{m+n,0}\sum_\alpha\kappa([x,a_\alpha],a^\alpha)\), which vanishes by (GQ.5). Finally
\[
 \sum_{j\in\mathbb Z}(\theta(j+m)-\theta(j))=m
\]
for every integer \(m\): there are \(m\) positive crossings if \(m>0\), and \(-m\) negative crossings if \(m<0\). Thus
\[
 \boxed{[x_m,S_n]
   =m\bigl((K_\kappa+\tfrac12C_B)x\bigr)_{m+n}}
 \qquad(m,n\in\mathbb Z).
 \tag{GQ.7}
\]
This is a finite normal-order calculation, not a manipulation of unconvergent sums. On a given input, choose a common cutoff for that input, its image under \(x_m\), both reindexed normally ordered families, the two scalar positions, and the finite crossing interval. Formula (GQ.6) can then be summed over a finite interval. Increasing its endpoints adds zero on both sides. This also proves (GQ.7) on every smooth vector.

At the critical form
\[
 \kappa_{\mathrm{crit}}=-\frac12\mathrm{Kil},
 \tag{GQ.8}
\]
we have \(K_\kappa=-C_B/2\), so every \(S_n\) commutes with every current. On the vacuum, only two negative indices survive in (GQ.3). Therefore
\[
 S_nv=0\ (n\geq-1),\qquad S_{-r-2}v=Q_r\ (r\geq0),
 \qquad
 Q_r=\frac12\sum_{\alpha,\ i,j\geq1,\ i+j=r+2}
 (a_\alpha)_{-i}(a^\alpha)_{-j}v.
 \tag{GQ.9}
\]
In particular, \(Q\) and all \(Q_r\) are critical vacuum invariants. By cyclicity, \(S_n=0\) as a critical vacuum operator when \(n\geq-1\). The negative \(S_n\) are the invariant endomorphisms corresponding to the states in (GQ.9). They commute with one another by the full invariant-endomorphism theorem of §3.3.3.

The translation operator satisfies \(Tv=0\) and \([T,x_m]=-m x_{m-1}\). Expanding a product with this derivation gives
\[
 Q_r=\frac{T^rQ}{r!}.
 \tag{GQ.10}
\]
For example, distributing \(r\) derivatives between the two factors of \(Q\) cancels the two factorials against the binomial coefficient and \(r!\); the resulting indices are exactly \(i+j=r+2\). This proof works at every affine form. Under the PBW pairing \(y_{-j}\leftrightarrow B(y,A_{j-1})\), the leading symbols of \(Q_r\) are the coefficients of \(\frac12B(A(t),A(t))\). Each \(Q_r\) has PBW degree two and energy \(r+2\).

**The complete regular-coordinate action.** For \(l\geq-1\), the derivation
\[
 D_lx_m=m x_{m+l},\qquad D_lv=0
 \tag{GQ.11}
\]
exists on the affine algebra and induced vacuum. Its central-bracket defect is a multiple of
\(m(m+n+l)\kappa(x,y)\delta_{m+n+l,0}\), hence zero. It preserves the vacuum subalgebra, including for \(l=-1\), since the possible index \(-1\) comes only from \(m=0\) and has zero coefficient. Notice \(D_{-1}=-T\). Negative \(l<-1\) would not preserve this vacuum and are outside this statement.

There is again an explicit ordering boundary:
\[
 \begin{aligned}
 [D_l,:a_jb_{n-j}:]
 &=j:a_{j+l}b_{n-j}:+(n-j):a_jb_{n-j+l}:\\
 &\quad+j(\theta(j+l)-\theta(j))[a_{j+l},b_{n-j}].
 \end{aligned}
\]
Reindexing the first ordinary sum changes its coefficient to \(j-l\); adding the second coefficient \(n-j\) leaves \(n-l\). The boundary Lie term contracts to zero by (GQ.4). Its scalar contribution is
\[
 \frac12\operatorname{tr}(K_\kappa)\delta_{n+l,0}
 \sum_j j(j+l)(\theta(j+l)-\theta(j)).
\]
For \(l\geq1\), write \(j=-s\), \(1\leq s\leq l\), and evaluate
\[
 \sum_{s=1}^{l}(s^2-ls)
 =\frac{l(l+1)(2l+1)}6-\frac{l^2(l+1)}2
 =-\frac{l^3-l}{6}.
\]
For \(l=0\) the interval is empty; for \(l=-1\) its only possible index is \(j=0\), with zero coefficient. Define
\[
 \gamma_\kappa=-\frac{\operatorname{tr}(K_\kappa)}{12}.
\]
We have proved the complete mode identity
\[
 \boxed{[D_l,S_n]=(n-l)S_{n+l}
   +\gamma_\kappa(l^3-l)\delta_{n+l,0}\,1}
 \qquad(n\in\mathbb Z,\ l\geq-1).
 \tag{GQ.12}
\]
As for (GQ.7), a common cutoff for the input, its image under \(D_l\), the reindexed sums, and this finite crossing interval makes the proof finite.

Applying (GQ.12) to \(v\) gives, with a missing-index term interpreted as zero,
\[
 \boxed{D_lQ_r=-\mathbf1_{r\geq l}(r+l+2)Q_{r-l}
      +\gamma_\kappa(l^3-l)\delta_{r,l-2}v.}
 \tag{GQ.13}
\]
Here \(r\geq0\) and \(l\geq-1\), so the first term for \(l=-1\) is always present. In particular
\[
 D_0Q=-2Q,\quad D_1Q=0,\quad
 D_2Q=-\frac12\operatorname{tr}(K_\kappa)v,
 \quad D_lQ=0\ (l\geq3).
\]
At critical level put
\[
 \gamma_B=\frac{\operatorname{tr}(C_B)}{24}.
 \tag{GQ.14}
\]
Then \(D_2Q=\operatorname{tr}(C_B)v/4=6\gamma_Bv\). The current anomaly in (GQ.7) has disappeared, while the coordinate anomaly (GQ.13) generally remains.

Let \(\mathcal Q(t)=\sum_{r\geq0}Q_rt^r\) and let \(f(t)\partial_t\) be a regular formal vector field, with \(f(t)=\sum_{l\geq-1}f_lt^{l+1}\). Summing (GQ.13) gives
\[
 \boxed{D_f\mathcal Q=-f\mathcal Q'-2f'\mathcal Q
                     +\gamma_\kappa f'''v.}
 \tag{GQ.15}
\]
Each coefficient has only finitely many contributing \(l\): in its ordinary part \(l\leq r\), and its scalar part has \(l=r+2\). Thus this identity is defined over every ordinary coefficient ring.

For completeness, this infinitesimal law has the following full formal-coordinate form. Let \(R\) be any ordinary \(k\)-algebra. Let \(\phi(t)\in R[[t]]\) define a continuous formal-disc automorphism, allowing a nilpotent constant term, and put \(\psi=\phi^{-1}\). On currents use substitution \(xF(t)\mapsto xF(\phi(t))\); its induced vacuum action is \(U_\phi\). Then
\[
 \boxed{U_\phi\mathcal Q(t)
   =\psi'(t)^2\mathcal Q(\psi(t))
           -\gamma_\kappa\operatorname{Sch}(\psi,t)v,}
 \qquad
 \operatorname{Sch}(\psi,t)=\frac{\psi'''}{\psi'}
                  -\frac32\left(\frac{\psi''}{\psi'}\right)^2.
 \tag{GQ.16}
\]
The inverse coordinate is essential: \(U_\phi\) acts on the coefficient functions. For \(\phi=t+\varepsilon f\), one has \(\psi=t-\varepsilon f\) and \(\operatorname{Sch}(\psi)=-\varepsilon f'''\), recovering (GQ.15).

Here is an algebraic integration proof, including nonreduced \(R\). Substitution preserves the affine cocycle because it preserves residue. For a Laurent monomial of exponent other than \(-1\), the substituted differential is an exact derivative and has residue zero. In the remaining case factor \(\phi=(t-b)u(t)\), where \(b=\psi(0)\) is nilpotent and \(u\) is a unit power series. Then \(\phi'/\phi=1/(t-b)+u'/u\) has residue one. These facts prove the residue identity coefficientwise; nilpotence makes every negative-power substitution finite in the necessary direction. The induced vacuum action therefore exists.

The candidate right side of (GQ.16) composes under substitution. Indeed, writing \(L_F=F''/F'\) gives
\(L_{F\circ G}=G'(L_F\circ G)+L_G\); substituting into
\(\operatorname{Sch}(F)=L_F'-L_F^2/2\) gives the Schwarzian chain rule. For a scaling \(\phi=at\), both actions send \(Q_r\) to \(a^{-r-2}Q_r\). For a nilpotent translation \(\phi=t+b\), both actions are the finite exponential \(\exp(bD_{-1})\) on each coefficient. Finally, a pointed coordinate with linear term one is a successive composition of
\(\exp(c_nt^{n+1}\partial_t)\), \(n\geq1\): choose \(c_n\) to remove the first remaining coefficient, then proceed to the next degree. Every fixed coordinate coefficient is settled after finitely many steps. On each finite-energy state, \(D_n\) lowers energy by \(n\), so the operator exponentials and the necessary composition are also finite. Their infinitesimal actions agree by (GQ.15); termwise differentiation of the finite exponential proves equality. Scaling, translation, and these pointed coordinates give every \(\phi\), proving (GQ.16) over \(R\), without an inference from field-valued points.

**Projective connections and the separate simple factors.** Our projective-connection coefficient is \(q\) in the scalar operator \(\partial_t^2-q(t)\). Its direct coordinate law and its induced law on coefficient functions are respectively
\[
 P_\phi(q)=\phi'^2q\circ\phi-\tfrac12\operatorname{Sch}(\phi),
 \qquad
 \delta_fq=-fq'-2f'q+\tfrac12f'''.
 \tag{GQ.17}
\]
Thus, at critical level, the exact quadratic-sector assignment is
\[
 Q_r\longmapsto 2\gamma_Bq_r.
 \tag{GQ.18}
\]
Whenever \(\gamma_B\ne0\), the normalized endomorphisms
\(\widehat q_r=Q_r/(2\gamma_B)\) have precisely the projective-connection law. This assertion identifies the normalization and equivariance of the quadratic coefficient; it does not identify the full oper algebra or prove exhaustion of the affine centre.

To state this safely for an arbitrary invariant \(B\), decompose
\(\mathfrak g=\bigoplus_s\mathfrak g_s\) into split simple ideals. Cross terms of every invariant form vanish: each simple ideal is perfect, and
\(B([x,y],z)=B(x,[y,z])=0\) when \(z\) lies in another ideal. The forms therefore restrict to each factor, and \(Q=\sum_sQ^{(s)}\). The map \(C_B\) commutes with the adjoint action. On an absolutely simple factor it is scalar: over an algebraic closure an eigenspace kernel is a nonzero adjoint-stable ideal, hence the whole factor; comparison of matrix entries descends the scalar to \(k\). Nondegeneracy of the Killing form on a semisimple characteristic-zero algebra, and the split-simple decomposition used here, are the retained structural Lie-algebra foundations. With \(C_B|_{\mathfrak g_s}=c_s\operatorname{id}\), its scalar \(c_s\) is nonzero, and
\[
 \gamma_s=\frac{c_s\dim\mathfrak g_s}{24}\ne0,
 \qquad
 Q_r^{(s)}\longmapsto2\gamma_sq_r^{(s)}.
 \tag{GQ.19}
\]
Each of these scalars is a unit after extension to any ordinary \(k\)-algebra. There is no such guarantee for \(\gamma_B=\sum_s\gamma_s\): taking two equal simple factors with opposite Killing forms makes it zero. In that case the aggregate \(\mathcal Q\) transforms as a quadratic differential; one must retain and normalize the separate factors. The canonical choice \(B=\mathrm{Kil}\) gives \(C_B=\operatorname{id}\) and \(\gamma_B=\dim\mathfrak g/24\) for a nonzero semisimple algebra.

The following square displays the mechanism with the exact scalar retained:
\[
 \begin{array}{ccc}
 \mathcal Q^{(s)}(t)&\longmapsto&2\gamma_sq^{(s)}(t)\\[2pt]
 D_f\downarrow&&\downarrow\,\delta_f\\[2pt]
 -f(\mathcal Q^{(s)})'-2f'\mathcal Q^{(s)}+\gamma_sf'''v
 &\longmapsto&
 2\gamma_s\bigl(-f(q^{(s)})'-2f'q^{(s)}+\tfrac12f'''\bigr).
 \end{array}
\]
The top arrow is (GQ.19), the left arrow is (GQ.15), and the right arrow differentiates the displayed multiple using (GQ.17). Current invariance comes from the cancellation in (GQ.7), whereas the displayed coordinate scalar remains. Formula (GQ.16) is the full inverse-coordinate version of this square.

**The trace normalization for \(\mathfrak{sl}_n\).** Take \(n\geq2\) and \(B(X,Y)=\operatorname{tr}(XY)\). The trace pairing is nondegenerate on \(\mathfrak{sl}_n\), since \(M_n=kI\oplus\mathfrak{sl}_n\) is an orthogonal decomposition and \(n\) is a unit. Write \(\operatorname{ad}X=L_X-R_X\) on \(M_n\). A matrix-unit calculation gives
\[
 \operatorname{tr}(L_XL_Y)=\operatorname{tr}(R_XR_Y)=n\operatorname{tr}(XY),
 \qquad
 \operatorname{tr}(L_XR_Y)=\operatorname{tr}(X)\operatorname{tr}(Y).
\]
For the last equality, the diagonal coefficient on \(E_{ij}\) is \(X_{ii}Y_{jj}\); summing proves it. The scalar line has zero adjoint action. On traceless matrices this yields
\[
 \mathrm{Kil}(X,Y)=2n\operatorname{tr}(XY),\quad
 C_B=2n\operatorname{id},\quad
 \kappa_{\mathrm{crit}}=-n\operatorname{tr},\quad
 \gamma_B=\frac{n(n^2-1)}{12}.
 \tag{GQ.20}
\]
In particular \(D_2Q=n(n^2-1)v/2\).

We also derive the sign relating this \(Q\) to the raw coefficient of the column determinant. This deduction uses only the determinant ordering of SL.L2, not an unproved determinant-invariance theorem. Let \(a_{ij}=E_{ij}[-1]\), impose the trace-free quotient, and use
\[
 \operatorname{cdet}(\delta_{ij}\tau+a_{ij})
   =\tau^n+\mathbb S_1\tau^{n-1}+\mathbb S_2\tau^{n-2}+\cdots,
 \qquad [\tau,E_{ij}[-1]]=E_{ij}[-2],
\]
where column factors are multiplied in increasing column order and \(\tau\) is moved to the right. Put \(d_j=E_{jj}[-1]\) and \(d_j'=E_{jj}[-2]\). The coefficient state is
\[
 \mathbb S_2v=
 \left(\sum_{i<j}(d_id_j-E_{ji}[-1]E_{ij}[-1])
          +\sum_j(j-1)d_j'\right)v.
 \tag{GQ.21}
\]
Indeed, two current factors give either a diagonal pair or a transposition pair. A single current factor must be diagonal; one commutation past the \(j-1\) preceding copies of \(\tau\) gives \((j-1)d_j'\). Three or more current factors begin at degree at most \(n-3\) in \(\tau\) and cannot contribute to this coefficient.

The inverse trace tensor on traceless matrices is
\(\sum_{i,j}E_{ij}\otimes E_{ji}-I\otimes I/n\); the scalar correction vanishes in the trace-free quotient. Therefore the half-Casimir there is
\(Q=\tfrac12\sum_{i,j}E_{ij}[-1]E_{ji}[-1]v\), with the \(E_{ij}\) understood as their traceless images. Since \(\sum d_j=\sum d_j'=0\),
\(\sum_{i<j}d_id_j=-\tfrac12\sum_jd_j^2\). Also
\[
 [E_{ij}[-1],E_{ji}[-1]]=d_i'-d_j'
\]
has no affine scalar. On reordering the off-diagonal terms in \(-Q\), the resulting derivative coefficient is
\[
 -\frac12\sum_{i<j}(d_i'-d_j')
 =\sum_j\left(j-\frac{n+1}{2}\right)d_j'.
\]
Its difference from the derivative part of (GQ.21) is
\((n-1)\sum_jd_j'/2=0\). We have thus proved
\[
 \boxed{\mathbb S_2v=-Q.}
 \tag{GQ.22}
\]
Let \(\mathcal S_2(t)=\sum_{r\geq0}T^r(\mathbb S_2v)t^r/r!\). From (GQ.15), (GQ.20), and (GQ.22),
\[
 \begin{aligned}
 D_2(\mathbb S_2v)&=-\frac{n(n^2-1)}2v,\\
 D_f\mathcal S_2&=-f\mathcal S_2'-2f'\mathcal S_2
                  -\frac{n(n^2-1)}{12}f'''v,\\
 U_\phi\mathcal S_2(t)&=\psi'^2\mathcal S_2(\psi(t))
                  +\frac{n(n^2-1)}{12}\operatorname{Sch}(\psi,t)v.
 \end{aligned}
 \tag{GQ.23}
\]
Thus the normalized projective coefficient in this trace convention is
\(\widehat q=-6\mathcal S_2/[n(n^2-1)]\).

For \(n=2\), the vector called \(Q\) in K3.1 is the **full** trace Casimir,
\(Q_{\mathrm{K3}}=\tfrac12h[-1]^2v+e[-1]f[-1]v+f[-1]e[-1]v\).
Consequently \(Q_{\mathrm{K3}}=2Q\), \(D_2Q=3v\), \(D_2Q_{\mathrm{K3}}=6v\), and
\(\mathbb S_2v=-Q=-Q_{\mathrm{K3}}/2\). The half-Casimir corresponds to \(q\); the full Casimir corresponds to \(2q\). This accounts for the factor two without changing the Schwarzian convention.

**Why the scalar-oper coefficient has the same anomaly.** The normalization can also be checked by a finite calculation with a monic scalar operator
\[
 \mathcal D_t=\partial_t^n+u_2(t)\partial_t^{n-2}+\text{lower-order terms},
\]
acting from \((1-n)/2\)-densities to \((1+n)/2\)-densities. Under \(t=\phi(s)\), put \(\lambda=\phi'\), \(L=\lambda'/\lambda\), and \(r=(n-1)/2\). Its transformed expression is
\(\mathcal D_s=\lambda^{(n+1)/2}\mathcal D_t\lambda^r\), with \(\partial_t=\lambda^{-1}\partial_s\).

Write the top three coefficients as
\[
 (\lambda^{-1}\partial_s)^n
 =\lambda^{-n}\bigl(\partial_s^n+A_nL\partial_s^{n-1}
                   +(B_nL'+C_nL^2)\partial_s^{n-2}+\cdots\bigr).
\]
Multiplication on the left by \(\lambda^{-1}\partial_s\) acts on the parenthesis as \(\partial_s-nL\). Starting at \(n=1\), the resulting recurrences are
\[
 A_{n+1}=A_n-n,\quad B_{n+1}=B_n+A_n,\quad C_{n+1}=C_n-nA_n.
\]
Summing them, or checking the induction explicitly, gives
\[
 A_n=-\frac{n(n-1)}2,\quad
 B_n=-\frac{n(n-1)(n-2)}6,\quad
 C_n=\frac{n(n-1)(n-2)(3n-1)}{24}.
\]
After right multiplication by \(\lambda^r\), the subleading coefficient is \(nr+A_n=0\). The coefficient at order \(n-2\), in addition to \(\lambda^2u_2\circ\phi\), is
\[
 \begin{aligned}
 &\left(\binom n2r+B_n\right)L'
 +\left(\binom n2r^2+A_n(n-1)r+C_n\right)L^2\\
 &\hspace{18mm}=\frac{n(n^2-1)}{12}\left(L'-\frac12L^2\right).
 \end{aligned}
\]
Thus
\[
 u_{2,s}=\lambda^2u_{2,t}\circ\phi
                +\frac{n(n^2-1)}{12}\operatorname{Sch}(\phi,s).
 \tag{GQ.24}
\]
This direct-coordinate law gives the coefficient-function infinitesimal law
\(\delta_fu_2=-fu_2'-2f'u_2-n(n^2-1)f'''/12\), exactly (GQ.23). For \(n=2\), \(u_2=-q\), in agreement with (GQ.17). If a half-integral density trivialization is needed over an ordinary ring, adjoin a square root of the unit constant coefficient of \(\lambda\) by a finite free faithfully flat extension and take the binomial power-series root of its remaining unit factor. The final formula (GQ.24) involves only \(\lambda,L\) and rational constants, so it descends. It neither chooses nor asserts a global square root of a canonical bundle.

Every construction and equality in this subsection extends to arbitrary ordinary \(k\)-algebras. Dual bases are obtained by tensoring an invertible Gram matrix, each fixed-energy identity is a finite identity in structure constants, and all integers divided by are units. The normal-order identities were proved on arbitrary smooth inputs with a common finite cutoff. The coordinate integration included nilpotent translations and arbitrary pointed formal families. Hence no reducedness, field-valued-point test, or boundedness restriction on the coefficient ring is hidden in these formulas. The conclusions are the critical quadratic invariants, their commuting vacuum endomorphisms, and their exact coordinate laws; construction or exhaustion of higher-degree central generators remains a separate theorem.

#### 3.4.5. From infinitesimal agreement to the full ordinary coordinate action

We state the integration argument with its precise input. Suppose an isomorphism between the polynomial vacuum algebra and the ordinary scalar-oper coefficient ring sends the energy-\(k+r\) generator to the matching scalar coefficient, and suppose the coordinate derivations agree on those generators, including every lower-degree term. Then the isomorphism intertwines the full continuous coordinate group over every ordinary \(k\)-algebra \(R\).

The coordinate substitutions, their two-sided inverses and the finite evaluation of nilpotent constants were proved in §1.1.8. The residue identity (RC.C7) proves that current substitution preserves the central cocycle for every invariant \(\kappa\). It preserves the vacuum ideal, so its action is the actual induced map \(U_\phi(uv)=\sigma_\phi(u)v\), and its action on affine endomorphisms is conjugation. The scalar-oper action is the inverse-coordinate action on functions; both actions have the same substitution composition convention.

First take a nilpotent translation \(\phi(t)=t+b\), \(b^N=0\). Its current action is the finite exponential \(\exp(bD_{-1})=\exp(-bT)\). The equality follows on each Laurent monomial by the binomial expansion, including negative exponents, whose terms with \(b^N\) vanish, and then on each finite word by the product rule. The inverse scalar translation is \(t\mapsto t-b\), with the same finite coefficient Taylor formula. Matching translation derivations therefore proves equivariance for this factor.

For a scaling \(\phi(t)=at\), \(a\in R^\times\), a state of energy \(E\) is multiplied by \(a^{-E}\). The scalar coefficient of a degree-\(k\) operator term and order-\(r\) Taylor coefficient has the same weight \(a^{-k-r}\). Thus the generator isomorphism also intertwines arbitrary unit scalings; no logarithm of \(a\) is used.

Finally consider a pointed substitution with linear coefficient one. It is a successively determined ordered product of flows
\[
\exp(c_lt^{l+1}\partial_t),\qquad l\ge1.
\tag{TC.A8}
\]
At step \(l\), the lower coefficients have been removed. The flow has first new term \(c_lt^{l+1}\), so one choice of \(c_l\) removes the next coefficient. Each fixed coordinate coefficient uses only finitely many steps. This constructs the product and its inverse over \(R\), since all positive integers are invertible.

On a vector of energy \(E\), the derivation \(D_l\) lowers energy by \(l\). Thus its exponential on the finite free subspace of energies at most \(E\) is a finite sum for \(l>0\). The substituted-current action of the flow is this exponential: on currents it is the exponential of the derivation \(F\mapsto t^{l+1}F'\), and the induced vacuum map has the same product expansion and vacuum value. Terms of energy below zero vanish. For any polynomial in scalar-oper coefficients of weighted energy \(E\), the matched derivation likewise lowers energy by \(l\); its finite exponential is the scalar-coordinate flow action. This last equality can also be checked by differentiating the exact density-conjugation formula with respect to the flow parameter. The resulting finite polynomial differential equation has a unique solution, coefficient by coefficient, because its recursion divides only by positive integers.

There is no hidden infinite product on an individual vector or polynomial. All \(l>E\) act trivially, and the remaining positive flows lower energy, so only finitely many terms contribute. For completeness, a coordinate differing from \(t\) first in order \(E+2\) acts trivially on an energy-\(E\) vacuum word. Every new substituted term in a factor of index \(-j\) has index at least \(E+1-j\), larger than the sum of the other negative indices; commuting it to the right leaves a positive mode and no possible central remainder. It kills the vacuum. The corresponding scalar-coefficient statement follows either from its weighted formula or the finite flow factors. Thus the successive flow product equals the actual full substitution on both sides.

A general continuous substitution is a nilpotent translation composed with a pointed substitution; factor its pointed linear coefficient as the scaling just treated. Equality for these factors proves the assertion for the entire ordinary continuous coordinate group, including nonreduced \(R\). The conclusion does not include derived parameter algebras, a completed punctured-disc center or a chiral/factorization construction.

#### 3.4.6. Matched generators and the cubic correction

Let \(A_{i,r}\) be the determinant endomorphisms of (SL.C1), whose basic-vector law (TC.A6) is proved in §3.4.3, and let \(s_{i,r}\) be the coefficients of the scalar oper operator
\[
\partial_t^n+\sum_{i=2}^n s_i(t)\partial_t^{n-i},
\qquad s_i(t)=\sum_{r\ge0}s_{i,r}t^r.
\]
Both algebras are freely polynomial on these respective coefficient lists: (SL.C1) proves this for the vacuum algebra, and the scalar-oper and coefficient-functor proofs of §§2 and 1.1.8 prove it for ordinary \(PGL_n\) disc opers. Hence
\[
\Phi_R:A_{i,r}\longmapsto s_{i,r}
\tag{TC.A9}
\]
is an algebra isomorphism for every ordinary \(R\). Equation (TC.A7) matches the exact scalar density law, and §3.4.5 proves that this isomorphism intertwines every continuous coordinate substitution. The resulting square is
\[
\begin{array}{ccc}
\operatorname{End}_{\widehat{\mathfrak{sl}}_n,\mathrm{crit}}(V_R)
 &\xrightarrow{\ \Phi_R\ }&R[\operatorname{Op}_{PGL_n}(D_R)]\\
{\scriptstyle E\mapsto U_\phi E U_\phi^{-1}}\downarrow
 &&\downarrow{\scriptstyle f\mapsto f\circ\mathcal P_{\phi^{-1}}}\\
\operatorname{End}_{\widehat{\mathfrak{sl}}_n,\mathrm{crit}}(V_R)
 &\xrightarrow{\ \Phi_R\ }&R[\operatorname{Op}_{PGL_n}(D_R)].
\end{array}
\tag{TC.A10}
\]
*The affine form is \(-n\operatorname{tr}(XY)\), with \(K=1\). Each horizontal map sends the divided translate of the right-ordered determinant coefficient to the identically indexed scalar-operator coefficient. The right vertical map uses the inverse coordinate on oper functions. The finite determinant laws, translation identity (TC.A5) and ordinary integration in §3.4.5 prove commutativity of the square, including nilpotent translations.*

The quadratic coefficient makes its lower-filtration term visible. Set
\(\gamma_n=n(n^2-1)/12\). The scalar coefficient law is
\[
\delta_v s_2=-v s_2'-2v's_2-\gamma_n v'''.
\tag{TC.A11}
\]
At \(n=2\), (SL.L23) gives \(w_2=-Q/2\), while the scalar oper coefficient is \(s_2=-q\). Thus (TC.A9) recovers exactly \(Q_r\mapsto2q_r\), including the Schwarzian term in (RC.C6).

For \(n\ge3\), the next coefficient obeys
\[
\delta_v s_3=-v s_3'-3v's_3
 -(n-2)v''s_2-\frac{n-2}{2}\gamma_n v''''.
\tag{TC.A12}
\]
Indeed the coefficient in front of \(v''s_2\) is
\(\binom{n-2}{2}+\tfrac{1-n}{2}(n-2)=-(n-2)\); the constant coefficient is
\(\binom n4+\tfrac{1-n}{2}\binom n3=-(n-2)\gamma_n/2\).
Consequently
\[
b_3=s_3-\frac{n-2}{2}s_2',\qquad
\delta_v b_3=-v b_3'-3v'b_3.
\tag{TC.A13}
\]
To verify the second equality, differentiate (TC.A11), substitute it together with (TC.A12), and cancel the \(v''s_2\) and \(v''''\) terms. The remaining derivative and weight terms are exactly those displayed. Thus \(b_3\) transforms as a cubic differential under the full ordinary coordinate group, by the same integration argument. On the vacuum side its matching vector is
\(w_3-\tfrac{n-2}{2}Tw_2\). The derivative correction has lower PBW degree than the cubic leading symbol. This example exhibits why the coordinate law of quantum generators cannot be read from their highest symbols alone.

For products of type A factors, use the factor generators and scalar oper operators. Cross-factor currents commute and the critical form is their direct sum. The proved polynomial algebra (SL.C1), the coordinate laws and the map (TC.A9) therefore give the product comparison as well. The proof concerns the regular algebraic vacuum algebra and the ordinary disc-oper coefficient functor. Section 3.5 supplies reductive vacuum factorization and the framed central coefficient comparison. Non-type-A basic lifting, the completed punctured-disc center, Poisson/chiral/Satake compatibility, full derived families and intrinsic nonadjoint/global central conventions retain their separate proof obligations.


### 3.5. Reductive vacuum algebras and central data

#### 3.5.1. Reductive vacua, central invariants and one-form coordinates

Let \(k\) be a characteristic-zero field. Fix a finite-dimensional split reductive Lie algebra with its decomposition
\[
\mathfrak g=\mathfrak s\oplus\mathfrak z,
\qquad
\mathfrak s=[\mathfrak g,\mathfrak g]
=[\mathfrak s,\mathfrak s],
\qquad
[\mathfrak z,\mathfrak g]=0 .
\tag{RV.1}
\]
The existence and properties of this structural decomposition are premises here. In particular, the semisimple factor is perfect and the central factor is abelian. We do not derive the reductive structure theorem from the affine calculation.

Let \(\kappa\) be any invariant symmetric bilinear form on \(\mathfrak g\), with no nondegeneracy assumption. It is the effective form in the affine bracket: a separately specified scalar level can be absorbed into \(\kappa\). For every ordinary commutative \(k\)-algebra \(R\), use its fixed scalar extension \(\kappa_R\) and the bracket
\[
[x_m,y_j]=[x,y]_{m+j}
 +m\kappa_R(x,y)\delta_{m+j,0}K .
\tag{RV.2}
\]
The algebraic vacuum \(V_{\mathfrak g,R}\) is induced from the one-dimensional \(R\)-module on which \(K=1\) and \(\mathfrak g_R[t]\) kills \(v\). Its ordered negative-mode basis and extension to formal currents are the proofs of (K2.2)–(K2.3) in [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), §3. Their common-tail argument makes this a smooth module for \(\mathfrak g_R((t))\), not merely for Laurent polynomial modes. Sections 3.3.2–3.3.3 prove the finite-energy ordinary base change and algebraic field reconstruction for every finite-dimensional Lie algebra and every such form. We will use their actual endomorphism correspondence and commutativity proof below.

Write \(\kappa_{\mathfrak s}\) and \(\kappa_{\mathfrak z}\) for the two restrictions, and put
\[
W=\operatorname{rad}(\kappa_{\mathfrak z})
=\{w\in\mathfrak z:\kappa(w,\mathfrak z)=0\},
\qquad
\mathfrak z_- =t^{-1}\mathfrak z[t^{-1}],
\qquad
W_-=t^{-1}W[t^{-1}].
\tag{RV.3}
\]
These are vector spaces over \(k\). All scalar extensions in this section extend this fixed form and this fixed radical.

**The cross form and the vacuum tensor product.** For \(a,b\in\mathfrak s\) and \(z\in\mathfrak z\), invariance gives
\[
\kappa([a,b],z)=\kappa(a,[b,z])=0 .
\]
Perfectness in (RV.1) expresses every element of \(\mathfrak s\) as a finite sum of such brackets. Therefore
\[
\kappa(\mathfrak s,\mathfrak z)=0,
\qquad
\kappa=\kappa_{\mathfrak s}\oplus\kappa_{\mathfrak z}.
\tag{RV.4}
\]
Both the ordinary bracket and the central cocycle vanish between the two current factors.

On \(V_{\mathfrak s,R}\otimes_R V_{\mathfrak z,R}\), let
\[
(x+z)_m\longmapsto
x_m\otimes1+1\otimes z_m,
\qquad K\longmapsto1 .
\tag{RV.5}
\]
The two summands commute. Their bracket within each factor is its restriction of (RV.2); the sum of the two scalar cocycles is precisely the cocycle for \(x+z\). Thus (RV.5) is a representation of the full affine algebra with one central generator acting as one. It does not require the two factor central generators to be independent on this tensor product. The vector \(v_{\mathfrak s}\otimes v_{\mathfrak z}\) satisfies the induction relations, giving an affine-module map
\[
\Theta_R:V_{\mathfrak g,R}
\longrightarrow V_{\mathfrak s,R}\otimes_R V_{\mathfrak z,R},
\qquad
v\longmapsto v_{\mathfrak s}\otimes v_{\mathfrak z}.
\tag{RV.6}
\]
Choose bases in the two summands and order all negative semisimple letters before all negative central letters. The ordered-word proof in §3 says that their ordered monomials form a basis. On the central negative part all brackets are zero: two negative indices cannot have sum zero, so no cocycle term occurs there. Its enveloping algebra is consequently the polynomial algebra \(\operatorname{Sym}_R(\mathfrak z_{-,R})\). Under \(\Theta_R\), the chosen ordered basis maps bijectively to the semisimple ordered basis tensored with these central monomials. Hence
\[
\boxed{\quad
V_{\mathfrak g,R}
\simeq V_{\mathfrak s,R}
 \otimes_R\operatorname{Sym}_R(\mathfrak z_{-,R}).
\quad}
\tag{RV.7}
\]
The map itself is canonical; the bases prove its invertibility. The formal-current actions agree too. On a fixed tensor or finite sum of tensors, choose a common positive-mode annihilation bound in both factors and use the finite Laurent negative parts. The formal bracket and both compositions then reduce to the finite-mode identities, exactly as in §3. Thus (RV.7) is an isomorphism of the actual smooth affine modules.

Giving \(x_{-r}\) energy \(r\), \(r\geq1\), makes (RV.7) preserve energy, including its sum decomposition
\[
(V_{\mathfrak g,R})_E
=\bigoplus_{a+b=E}
 (V_{\mathfrak s,R})_a
 \otimes_R\operatorname{Sym}_R(\mathfrak z_{-,R})_b .
\tag{RV.8}
\]
These are finite direct sums of finite free \(R\)-modules. It also preserves the filtration by the total number of negative letters.

**Central nonnegative currents are ordinary polynomial derivatives.** Choose a basis \(z_1,\ldots,z_q\) of \(\mathfrak z\), and denote by
\[
Z_{a,r}= (z_a)_{-r}v_{\mathfrak z},
\qquad r\geq1,
\]
the corresponding polynomial generators of its vacuum. A negative current acts by multiplication by its generator. A zero current commutes with all negative modes and kills the vacuum, hence acts as zero. For \(m\geq1\), commute \(z_m\) through a central monomial. The only bracket is the scalar \(m\kappa(z,z_a)\) when that letter has index \(-m\). The Leibniz rule for this commutator therefore gives the exact operator identity
\[
z_m
=m\sum_{a=1}^q\kappa(z,z_a)
       \frac{\partial}{\partial Z_{a,m}}
\quad\text{on }R[Z_{a,r}:r\geq1],
\qquad z_0=0.
\tag{RV.9}
\]
Each polynomial has finitely many variables and factors, so the derivative sum and every formal-current action on it are finite. This is an identity on the entire central vacuum, with no appeal to field-valued points.

Choose a vector-space complement \(C\) to \(W\) in \(\mathfrak z\). The restriction of \(\kappa\) to \(C\) is nondegenerate. Indeed an element of \(C\) orthogonal to \(C\) is also orthogonal to \(W\), by the definition of \(W\); it belongs to \(W\cap C=0\). The finite-dimensional pairing map is thus injective, hence bijective. For a basis \(c_1,\ldots,c_d\) of \(C\), choose \(\eta_1,\ldots,\eta_d\in C\) with \(\kappa(\eta_a,c_b)=\delta_{ab}\). Equation (RV.9) gives, for every \(m\geq1\),
\[
(\eta_a)_m=m\frac{\partial}{\partial C_{a,m}},
\qquad
C_{a,m}=(c_a)_{-m}v_{\mathfrak z}.
\tag{RV.10}
\]
The constants \(m\) are units in every \(R\).

If a polynomial over \(R\) has zero derivative in a variable \(X\), write it uniquely as \(\sum_{j=0}^N a_jX^j\), with coefficients in the other-variable polynomial ring. Its derivative is \(\sum_{j=1}^N ja_jX^{j-1}\); uniqueness of coefficients and invertibility of every positive integer imply \(a_j=0\) for \(j\geq1\). This argument remains valid when \(R\) has nilpotents or zero divisors. Applying it to each of the finitely many \(C\)-variables used by a polynomial proves
\[
\boxed{\quad
V_{\mathfrak z,R}^{\mathfrak z_R[[t]]}
=\operatorname{Sym}_R(W_{-,R}).
\quad}
\tag{RV.11}
\]
The reverse inclusion follows from (RV.9), since \(\kappa(\mathfrak z,W)=0\). Formal nonnegative currents impose the same equations as their individual modes, by the finite annihilation bounds. The complement was used only to prove the equality; its right side is the canonical subalgebra defined by \(W\).

For example, let \(\mathfrak z=ka\oplus kb\) and let \(\kappa(a,a)=1\), \(\kappa(a,b)=\kappa(b,b)=0\). With \(A_r=a_{-r}v\) and \(B_r=b_{-r}v\), the central vacuum is \(R[A_r,B_r:r\geq1]\). Its positive currents are
\[
a_m=m\partial_{A_m},\qquad b_m=0 .
\]
Its invariant algebra is exactly \(R[B_r:r\geq1]\). In particular the negative \(a\)-modes do not supply vacuum endomorphisms at this form.

The relation between the form and its invariant algebra can be read directly:

| Restriction of the form to the center | Radical \(W\) | Central vacuum invariants |
|---|---|---|
| Nondegenerate | \(0\) | \(R\) |
| Identically zero | \(\mathfrak z\) | \(\operatorname{Sym}_R(\mathfrak z_{-,R})\) |
| Arbitrary rank | \(\operatorname{rad}(\kappa_{\mathfrak z})\) | \(\operatorname{Sym}_R(W_{-,R})\) |

*The table is (RV.9)–(RV.11): paired directions are removed by ordinary derivatives, and radical directions remain free polynomial generators.*

**All invariants and actual endomorphism products factor.** The central currents on (RV.7) act only on the polynomial factor. The derivative proof just given works with coefficients in the \(R\)-module \(V_{\mathfrak s,R}\): coefficient uniqueness and multiplication by the unit \(m\) still apply. Thus their joint kernel is
\[
V_{\mathfrak s,R}\otimes_R\operatorname{Sym}_R(W_{-,R}).
\]
The remaining semisimple currents act only on the first factor. Every tensor can be written uniquely as a finite sum
\(\sum_p a_p\otimes p\), where \(p\) runs through distinct monomials in a chosen basis of \(W_-\). Acting by \(x_m\in\mathfrak s_R[[t]]\) yields \(\sum_p x_ma_p\otimes p\). Coefficient uniqueness makes this zero exactly when every \(a_p\) is invariant. Consequently
\[
V_{\mathfrak g,R}^{\mathfrak g_R[[t]]}
\simeq
V_{\mathfrak s,R}^{\mathfrak s_R[[t]]}
\otimes_R\operatorname{Sym}_R(W_{-,R}).
\tag{RV.12}
\]
This proves factorization of invariants directly; it is not an assertion that an arbitrary tensor product commutes with an arbitrary Hom functor.

Put
\[
Z_{\mathfrak a,R}
=\operatorname{End}_{\widehat{\mathfrak a}_{\kappa_{\mathfrak a},R}}
       (V_{\mathfrak a,R})
\qquad(\mathfrak a=\mathfrak s,\mathfrak g).
\]
By the actual induction proof (K2.3), an invariant \(a\) corresponds to the endomorphism \(E_a\), with \(E_av=a\) and \(E_a(uv)=ua\). It is well defined because \(a\) satisfies the same induction relations as \(v\). Conversely every endomorphism is determined by this vacuum image.

For \(p\in\operatorname{Sym}_R(W_{-,R})\), multiplication \(M_p\) on the central vacuum commutes with every central current. It commutes with negative multiplications, with zero modes, and with (RV.9), since all the derivatives there are in complementary directions. It also commutes with the semisimple currents in (RV.7). We therefore have an actual algebra homomorphism
\[
\begin{aligned}
\mathcal E_R:
Z_{\mathfrak s,R}\otimes_R\operatorname{Sym}_R(W_{-,R})
&\longrightarrow Z_{\mathfrak g,R},\\
E_a\otimes p&\longmapsto E_a\otimes M_p .
\end{aligned}
\tag{RV.13}
\]
Here the map on the right is regarded as an endomorphism of (RV.7). Its vacuum image is \(a\otimes p\). Equations (RV.12) and (K2.3) make \(\mathcal E_R\) a bijection of modules. For products, compute on every simple tensor:
\[
(E_a\otimes M_p)(E_b\otimes M_q)
=(E_aE_b)\otimes M_{pq}.
\tag{RV.14}
\]
Thus it is a bijection of algebras, with their actual composition:
\[
\boxed{\quad
Z_{\mathfrak g,R}
\simeq Z_{\mathfrak s,R}
 \otimes_R\operatorname{Sym}_R(W_{-,R}).
\quad}
\tag{RV.15}
\]
Section 3.3.3 applies to \(\mathfrak s\) with the present arbitrary form: (VC.17) proves every integer current commutator of an invariant field, and (VC.19)–(VC.20) prove commutation of all invariant-field modes and vacuum endomorphisms with common finite cutoffs. Its finite coefficient identities survive scalar extension; the finite-kernel argument (RV.16)–(RV.17) below also identifies every endomorphism over \(R\) with a finite \(R\)-linear combination of extended endomorphisms over \(k\). In particular \(Z_{\mathfrak s,R}\), and hence (RV.15), is commutative. This identifies the polynomial factor as an endomorphism algebra, rather than merely as a vector space of invariant states.

**Ordinary base change by finite equations.** All these assertions can also be checked by the exact finite-energy mechanism, which identifies their compatibility with arbitrary ordinary scalar extension. Over \(k\), every energy space \((V_{\mathfrak a,k})_E\) is finite-dimensional. A current \(x_m\) has energy shift \(-m\), and vanishes there when \(m>E\). For a basis \(\mathcal B_{\mathfrak a}\), its invariant energy space is the kernel of
\[
(V_{\mathfrak a,k})_E
\longrightarrow
\bigoplus_{x\in\mathcal B_{\mathfrak a}}
\ \bigoplus_{m=0}^E
(V_{\mathfrak a,k})_{E-m},
\qquad
a\longmapsto(x_ma)_{x,m}.
\tag{RV.16}
\]
This formula follows from the current brackets: a negative replacement subtracts \(m\) from the energy, and a scalar replacement is possible only when the removed indices sum to \(m\). Zero modes preserve energy. Distinct input energies have distinct output energies for each fixed \(m\), so invariance is energy graded. Every state has finite energy support.

Tensoring (RV.16) with \(R\) is exact, since every \(k\)-module is a vector space and \(R\) is flat over \(k\). The ordered basis identifies its domain with \((V_{\mathfrak a,R})_E\), and its target and maps with the actual extended current action. Summing these finite kernel identities gives
\[
V_{\mathfrak a,R}^{\mathfrak a_R[[t]]}
=R\otimes_kV_{\mathfrak a,k}^{\mathfrak a[[t]]},
\qquad
Z_{\mathfrak a,R}=R\otimes_kZ_{\mathfrak a,k}.
\tag{RV.17}
\]
For the second equality use the induction correspondence and the product calculation \(E_a(uv)=ua\); the same operations extend scalars, so this is an equality of algebras. The radical also extends exactly: it is the kernel of the finite linear pairing map \(\mathfrak z\to\mathfrak z^*\). Hence
\(\operatorname{rad}((\kappa_{\mathfrak z})_R)=W\otimes_kR\).
The symmetric polynomial algebra and all maps in (RV.7)–(RV.15) extend scalars. This proves all ordinary-family claims using modules and equations, including nonreduced \(R\), rather than detection on field-valued points. It concerns the scalar extensions of the fixed \(k\)-form; a varying form with new coefficient-ring degeneracies is a different family.

**Critical level and the central divided translates.** The Killing form is
\(\operatorname{Kil}_{\mathfrak g}(x,y)=\operatorname{Tr}(\operatorname{ad}x\,\operatorname{ad}y)\). Since \(\operatorname{ad}z=0\) for \(z\in\mathfrak z\), it has zero central restriction and zero cross form. On \(\mathfrak s\), the action on the summand \(\mathfrak z\) is zero, so its restriction is \(\operatorname{Kil}_{\mathfrak s}\). Therefore at the critical effective form
\[
\kappa_{\mathrm{crit}}=-\frac12\operatorname{Kil}_{\mathfrak g},
\qquad W=\mathfrak z,
\qquad
Z_{\mathfrak g,\mathrm{crit},R}
\simeq Z_{\mathfrak s,\mathrm{crit},R}
\otimes_R\operatorname{Sym}_R(\mathfrak z_{-,R}).
\tag{RV.18}
\]
No nondegeneracy theorem for the Killing form is needed for its zero central restriction.

For arbitrary \(\kappa\) and \(w\in W\), all modes \(w_m\) commute with every mode of \(\mathfrak g\): the ordinary bracket is zero, and the cocycle is zero by (RV.3)–(RV.4). Nonnegative \(w_m\) are therefore zero operators on the entire cyclic vacuum. Put
\[
X_{w,r}=w_{-r-1}v,\qquad
A_{w,r}=E_{X_{w,r}},
\qquad r\geq0.
\tag{RV.19}
\]
The translation of (GJ.P6) satisfies
\[
\frac{T^r}{r!}(w_{-1}v)=w_{-r-1}v=X_{w,r},
\qquad
TX_{w,r}=(r+1)X_{w,r+1}.
\tag{RV.20}
\]
Indeed each use of \([T,w_{-j}]=j w_{-j-1}\) multiplies by the next integer, and \(Tv=0\). The corresponding endomorphism is exactly multiplication by the negative central generator on (RV.7). The field reconstructed in (VC.8) from \(w_{-1}v\) is the actual current \(w(t)\); all its nonnegative modes vanish as operators, while its negative modes give
\[
Y(w_{-1}v,t)
=\sum_{r\geq0}A_{w,r}t^r.
\tag{RV.21}
\]
Creation (VC.18) identifies these same modes with the divided translates (RV.20). They commute with every invariant-field mode and every semisimple vacuum endomorphism by (VC.19), also directly by their multiplication description. Thus all products and divided translates in the central factor have the specified endomorphism interpretation.

The full translation on (RV.7) is
\[
T_{\mathfrak g}=T_{\mathfrak s}\otimes1+1\otimes T_{\mathfrak z}.
\tag{RV.22}
\]
Both sides kill the vacuum and have the same commutator \(-m(x+z)_{m-1}\) with every current, so cyclicity proves their equality. In particular translation on the central polynomial factor is the derivation given by (RV.20). On endomorphisms, (TC.A4) with \(D_{-1}=-T\) gives \([T,E_a]=E_{Ta}\); its product rule is consequently compatible with the algebra factorization.

**The full central coordinate law.** Let \(\phi(t)\) be any continuous \(R\)-coordinate, with nilpotent constant coefficient and invertible linear coefficient, and let \(\psi=\phi^{-1}\). Section 1.1.8 constructs this inverse coefficientwise. The complete residue proof (RC.C7) shows that current substitution
\(\sigma_\phi(xF(t))=xF(\phi(t))\) preserves (RV.2) for every \(\kappa\). It preserves nonnegative formal currents, so
\[
U_\phi(uv)=\sigma_\phi(u)v
\]
is the actual invertible vacuum map, with inverse \(U_\psi\). Its endomorphism action is conjugation. The two current factors are preserved separately, and the tensor map (RV.6) sends their vacuum to the tensor vacuum; hence
\[
U_{\phi,\mathfrak g}
=U_{\phi,\mathfrak s}\otimes U_{\phi,\mathfrak z},
\qquad
U_\phi E_aU_\phi^{-1}=E_{U_\phi a}.
\tag{RV.23}
\]
These identities follow on a finite negative word and then on every state. Formal tails use the common bounds already proved.

For \(w\in W\), expand \(w\phi(t)^{-r-1}v\). Every nonnegative mode vanishes, and the remaining negative coefficients give
\[
U_\phi X_{w,r}
=\sum_{j\geq0}
[t^{-j-1}]\phi(t)^{-r-1}\,X_{w,j}.
\tag{RV.24}
\]
This sum is finite. If \(\phi(0)^\nu=0\), write \(\phi(t)=\phi(0)+t a(t)\), with \(a(t)\) a unit. The expansion
\[
\phi(t)^{-r-1}
=(ta(t))^{-r-1}
\sum_{q=0}^{\nu-1}\binom{-r-1}{q}
 \left(\frac{\phi(0)}{ta(t)}\right)^q
\]
has smallest possible exponent \(-r-\nu\). Therefore only \(j\leq r+\nu-1\) occurs. The infinite positive tail is irrelevant to its action on the vacuum.

Residue change computes each coefficient without a chosen bilinear identification of the center with its dual:
\[
\begin{aligned}
[t^{-j-1}]\phi(t)^{-r-1}
&=\operatorname{Res}_t t^j\phi(t)^{-r-1}\,dt\\
&=\operatorname{Res}_u
 \psi(u)^j u^{-r-1}\psi'(u)\,du\\
&=[u^r]\psi'(u)\psi(u)^j.
\end{aligned}
\tag{RV.25}
\]
The residue identity holds for arbitrary ordinary coefficients by the monomial proof of (RC.C7), including nilpotent coordinate constants. It thus proves a full exact coordinate formula, not only a symbol calculation. If
\[
X_w(t)=\sum_{r\geq0}X_{w,r}t^r,
\qquad
A_w(t)=\sum_{r\geq0}A_{w,r}t^r,
\]
then (RV.23)–(RV.25) are precisely
\[
\boxed{\quad
U_\phi X_w(t)=\psi'(t)X_w(\psi(t)),
\qquad
U_\phi A_w(t)U_\phi^{-1}
=\psi'(t)A_w(\psi(t)).
\quad}
\tag{RV.26}
\]
Each series has an individual algebraic state or endomorphism in every coefficient. If \(\psi(0)^\nu=0\), the coefficient formula is
\[
\boxed{\quad
U_\phi X_{w,r}
=\sum_{j=0}^{r+\nu-1}
 \left([t^r]\psi'(t)\psi(t)^j\right)X_{w,j}.
\quad}
\tag{RV.27}
\]
There are no normal-order corrections: these are radical current modes themselves, and they commute with all currents. In particular there is no Schwarzian term.

On the polynomial algebra, (RV.26) is inverse pullback of a one-form. To state this intrinsically, its coefficient functor is
\[
\operatorname{Hom}_{k\text{-alg}}
 \bigl(\operatorname{Sym}_k(W_-),R\bigr)
=W^*\otimes_k R[[t]]\,dt .
\tag{RV.28}
\]
A functional sends \(w_{-r-1}\) to the \(w\)-evaluation of the coefficient of \(t^r\,dt\). Equation (RV.27) sends it to the corresponding coefficient of \(\psi'(t)\alpha(\psi(t))\,dt\). The dual \(W^*\) is required here; the possibly zero form \(\kappa\) is not used to identify \(W\) with its dual. All coefficient sums are finite for a fixed nilpotence bound, so (RV.26)–(RV.28) commute with every homomorphism \(R\to R'\).

The tensor-product comparison and its coordinate action are displayed together:
\[
\begin{array}{ccc}
Z_{\mathfrak g,R}
&\xrightarrow[\ (RV.13)\text{--}(RV.15)\ ]{\ \simeq\ }&
Z_{\mathfrak s,R}\otimes_R\operatorname{Sym}_R(W_{-,R})\\
{\scriptstyle E\mapsto U_\phi EU_\phi^{-1}}\downarrow&&
\downarrow{\scriptstyle (E_{\mathfrak s}\mapsto U_{\phi,\mathfrak s}E_{\mathfrak s}U_{\phi,\mathfrak s}^{-1})
 \ \otimes\ (X_w(t)\mapsto\psi'X_w(\psi))}\\
Z_{\mathfrak g,R}
&\xrightarrow{\ \simeq\ }&
Z_{\mathfrak s,R}\otimes_R\operatorname{Sym}_R(W_{-,R}) .
\end{array}
\tag{RV.29}
\]
*The horizontal maps compare actual endomorphism compositions. The right central action is the exact inverse one-form law (RV.25)–(RV.27), and (RV.23) proves commutation of the square.*

Finally, the coordinate derivations from (TC.A1) act directly on the divided translates:
\[
D_lX_{w,r}=-(r+1)X_{w,r-l},
\qquad
[D_l,A_{w,r}]=-(r+1)A_{w,r-l},
\qquad l\geq-1.
\tag{RV.30}
\]
All negatively indexed generators mean zero. Indeed
\(D_l(w_{-r-1}v)=-(r+1)w_{l-r-1}v\), and this vanishes when its index is nonnegative. The second identity follows from the induced endomorphism correspondence. Equivalently, for \(\phi(t)=t+\epsilon v(t)\), \(\epsilon^2=0\), expansion of (RV.26) gives
\[
\delta_vX_w=-vX_w'-v'X_w .
\tag{RV.31}
\]
For an arbitrary \(v(t)=\sum_{a\geq0}v_at^a\), its divided coefficients obey
\[
\delta_vX_{w,r}
=-(r+1)\sum_{a=0}^{r+1}v_aX_{w,r+1-a}.
\tag{RV.32}
\]
This finite sum includes every infinitesimal constant direction. The same formula holds with \(X\) replaced by \(A\). For unit scaling and nilpotent translation it specializes to the full identities
\[
\begin{gathered}
\phi(t)=a t:\qquad
U_\phi X_{w,r}=a^{-r-1}X_{w,r}\quad(a\in R^\times),\\
\phi(t)=t+b,\ b^\nu=0:\qquad
U_\phi X_{w,r}
=\sum_{q=0}^{\nu-1}
 \binom{r+q}{r}(-b)^qX_{w,r+q}.
\end{gathered}
\tag{RV.33}
\]
The translation is \(\exp(-bT)\) on each generator, a finite sum because \(b^\nu=0\). Positive coordinate flows and their coefficient-finite ordered products act as in the exact integration proof of §3.4.5; alternatively (RV.24)–(RV.27) already give the full action directly. Thus the mode laws are the infinitesimal forms of a proved ordinary coordinate action.

If the semisimple factor is zero, the whole statement is the central derivative calculation and its one-form action. If the center is zero, (RV.15) is the original semisimple vacuum algebra. If \(\mathfrak g=0\), the vacuum and its endomorphism algebra are \(R\), and all coordinate actions are the identity. The construction applies without change to any number of split simple factors in \(\mathfrak s\).

This proves the reductive algebraic vacuum factorization for every fixed invariant form and every ordinary coefficient extension. At critical level it adjoins one free divided-translation family for each central direction, equivariantly with its inverse one-form action. It does not identify this coefficient space with the full intrinsic oper stack of a nonadjoint reductive group. Central bundles and their automorphisms, finite central-isogeny choices, the dual-group central convention, and any global or derived descent comparison retain their own geometric premises. Full non-type-A basic lifting and coordinate comparison, completed/chiral/Poisson/Satake/derived centers and the other original theorem obligations are also unaffected.

#### 3.5.2. The trace splitting of the critical \(GL_n\) vacuum

Let \(k\) be a characteristic-zero field, \(R\) any ordinary commutative \(k\)-algebra, and \(n\geq1\). Use the matrix-current form, central level and translation convention of SL.L1:
\[
 \kappa(X,Y)=-n\operatorname{tr}(XY)
               +\operatorname{tr}(X)\operatorname{tr}(Y),\qquad K=1,
 \qquad [T,X[m]]=-mX[m-1],\quad Tv=0.
 \tag{TR.1}
\]
This is the critical form \(-\mathrm{Kil}_{\mathfrak{gl}_n}/2\), including its zero restriction to the scalar matrices. Indeed the matrix-unit trace calculations preceding (GQ.20) apply to arbitrary matrices: expanding \(\operatorname{ad}X=L_X-R_X\) gives \(\mathrm{Kil}_{\mathfrak{gl}_n}(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)\). Taking minus one half gives (TR.1). A nonzero level for the scalar currents would give a different vacuum problem. We use the proved traceless polynomial-vacuum theorem (SL.C1) and its full ordinary coordinate comparison (SL.X26). The trace factor and the passage from traceless to raw matrix coefficients will be proved here.

**The vacuum and its entire invariant algebra split.** Set
\[
 J[m]=\sum_a E_{aa}[m],\qquad c[m]=J[m]/n,\qquad
 F_{ij}[m]=E_{ij}[m]-\delta_{ij}c[m].
 \tag{TR.2}
\]
Every \(J[m]\) commutes with every current: its matrix bracket is zero and
\(\kappa(I,E_{ab})=-n\delta_{ab}+n\delta_{ab}=0\). The \(F\)-currents are traceless. Their form is \(-n\operatorname{tr}\), and they commute with the scalar currents. Thus the affine current representation separates into the critical traceless representation and the abelian scalar representation with zero cocycle.

Write \(z_r=c[-r-1]\), \(r\geq0\). The PBW ordered negative-mode basis gives an actual \(R\)-module isomorphism, compatible with every current action,
\[
 V_{\mathfrak{gl}_n,R}
   =V_{\mathfrak{sl}_n,R}\otimes_R R[z_0,z_1,\ldots].
 \tag{TR.3}
\]
For \(n=1\), the first factor is \(R\). Every nonnegative scalar current acts as zero on (TR.3); every negative scalar current acts by multiplication by its corresponding variable. The traceless currents act on the first factor alone.

Here is a direct invariant argument over \(R\), without a pointwise test or an exchange of an infinite intersection with tensor. Expand any state as a **finite** sum
\(\sum_\beta w_\beta z^\beta\), using the polynomial monomial basis. A nonnegative traceless current kills this sum exactly when it kills every coefficient \(w_\beta\), since these monomials are \(R\)-linearly independent. Formal nonnegative series impose the same equations, by the vacuum smoothness bound. Hence
\[
 V_{\mathfrak{gl}_n,R}^{\mathfrak{gl}_n[[t]]}
  =V_{\mathfrak{sl}_n,R}^{\mathfrak{sl}_n[[t]]}
       \otimes_R R[z_0,z_1,\ldots].
 \tag{TR.4}
\]
This is also an algebra factorization of endomorphisms. An endomorphism on the first factor, tensored with multiplication by a polynomial on the second, commutes with all currents. Its vacuum image is the corresponding invariant tensor. Such maps exhaust all invariant images by (TR.4), and the induced-module bijection (K2.3) makes the map both surjective and injective. Composition multiplies the two factors. Therefore
\[
 Z_{\mathfrak{gl}_n,R}
 :=\operatorname{End}_{\widehat{\mathfrak{gl}}_n,\mathrm{crit}}
                 (V_{\mathfrak{gl}_n,R})
 =Z_{\mathfrak{sl}_n,R}\otimes_R R[C_r:r\geq0],
 \tag{TR.5}
\]
where \(C_r\) is multiplication by \(z_r\). In particular no additional endomorphisms arise from arbitrary linear maps of the scalar polynomial module: commuting with its negative multiplication currents and the cyclic vacuum forces the maps just described.

Let \(\overline S_i\) denote the right-ordered traceless determinant coefficients, embedded using the \(F\)-currents, and put
\[
 \overline S_0=1,\qquad \overline S_1=0,\qquad
 \overline A_{i,r}(v)=\frac{T^r(\overline S_i v)}{r!}.
\]
By (SL.C1), for \(n\geq2\),
\[
 \boxed{Z_{\mathfrak{gl}_n,R}
   =R[C_r,\overline A_{i,r}:r\geq0,\ 2\leq i\leq n].}
 \tag{TR.6}
\]
All displayed generators are algebraically independent and every endomorphism is a finite polynomial. For \(n=1\), only the \(C_r\) occur. Thus (TR.6) proves exhaustion of the regular matrix vacuum algebra, using the actual traceless exhaustion theorem, rather than just constructing basic invariant states. Translation splits between the two factors and satisfies
\(Tz_r=(r+1)z_{r+1}\); on endomorphisms it is the derivation determined by
\([T,E_w]=E_{Tw}\).

**The exact determinant shift and every triangular coefficient.** Work first in the negative-mode enveloping algebra with the Ore variable \(\tau\):
\[
 \tau a=a\tau+T(a).
\]
All scalar negative modes commute with the negative-mode algebra, though they need not commute with \(\tau\). Put \(c=z_0\), \(c'=T(c)=z_1\), and \(c^{(j)}=T^j(c)=j!z_j\). Entry by entry,
\[
 \delta_{ij}\tau+E_{ij}[-1]
 =\delta_{ij}(\tau+c)+F_{ij}[-1].
 \tag{TR.7}
\]
Moreover \([\tau+c,F_{ij}[m]]=[\tau,F_{ij}[m]]\). The substitution
\(\tau\mapsto\tau+c\), fixing the negative currents, is an automorphism of this Ore algebra: it preserves its defining commutator, and \(\tau\mapsto\tau-c\) is its inverse. Applying it to the finite, increasing-column determinant identity yields
\[
 \begin{aligned}
 \operatorname{cdet}(\delta_{ij}\tau+E_{ij}[-1])
 &=\operatorname{cdet}(\delta_{ij}(\tau+c)+F_{ij}[-1])\\
 &=\sum_{i=0}^n\overline S_i(\tau+c)^{n-i}.
 \end{aligned}
 \tag{TR.8}
\]
The coefficients \(\overline S_i\) are unchanged by this substitution, since they lie in the traceless negative-mode algebra. This argument takes place before application to \(v\). In particular it does not assume that \(\tau+c\) kills the vacuum; its vacuum value is \(cv\), which is generally nonzero.

Define finite differential polynomials in the central variables by
\[
 H_0=1,\qquad H_{d+1}=T(H_d)+cH_d.
 \tag{TR.9}
\]
Then
\[
 (\tau+c)^m=\sum_{d=0}^{m}\binom md H_d\,\tau^{m-d}.
 \tag{TR.10}
\]
To prove this, multiply the expression for \(m\) on the left by \(\tau+c\). Moving \(\tau\) once to the right gives at deficit \(d\) the old coefficient
\(\binom mdH_d\) and the new coefficient
\(\binom m{d-1}(T+c)H_{d-1}=\binom m{d-1}H_d\). Pascal's identity gives (TR.10), starting from \(m=0\). This is a finite induction that retains every ordering derivative. The first terms are
\[
 H_1=c,\qquad H_2=c^2+c',\qquad
 H_3=c^3+3cc'+c''.
\]
For an entirely explicit finite expression,
\[
 H_d
 =d!\!\sum_{\substack{m_1,\ldots,m_d\geq0\\
                     \sum_{j=1}^d jm_j=d}}
   \prod_{j=1}^{d}
   \frac{1}{m_j!}
   \left(\frac{c^{(j-1)}}{j!}\right)^{m_j}.
 \tag{TR.11}
\]
Indeed, the generating series of this expression is
\(\exp(\sum_{j\geq1}c^{(j-1)}s^j/j!)\). Its \(s\)-derivative equals
\((T+c)\) times the series: \(T\) differentiates every \(c^{(j-1)}\), while the missing constant term is \(c\). Its constant coefficient is one, so coefficient recursion gives exactly (TR.9). This proves (TR.11) in a polynomial differential ring and hence in the central-mode ring.

Writing the raw matrix determinant as
\(\tau^n+\sum_{k=1}^nS_k\tau^{n-k}\), equations (TR.8)–(TR.10) give
\[
 \boxed{S_k
  =\sum_{i=0}^{k}\binom{n-i}{k-i}\overline S_i H_{k-i}
  =\overline S_k+
       \sum_{i=0}^{k-1}\binom{n-i}{k-i}\overline S_iH_{k-i}.}
 \tag{TR.12}
\]
There is no derivative of \(\overline S_i\) in this formula: its position is to the left of the shifted power in (TR.8), and only that power is right ordered. In particular,
\[
 \begin{aligned}
 S_1&=nc=J[-1],\\
 S_2&=\overline S_2+\binom n2(c^2+c'),\\
 S_3&=\overline S_3+(n-2)\overline S_2c
                         +\binom n3(c^3+3cc'+c'').
 \end{aligned}
 \tag{TR.13}
\]
The second line applies when \(n\geq2\), and the last when \(n\geq3\). The coefficient of \(c'\) in \(S_2\) equals that of \(c^2\); omitting it would change both the determinant and its coordinate law.

For states and their corresponding endomorphisms, let
\[
 A_{k,r}(v)=\frac{T^r(S_kv)}{r!},\quad
 \mathcal S_k(t)=\sum_{r\geq0}A_{k,r}t^r,\quad
 \overline{\mathcal S}_i(t)=\sum_{r\geq0}\overline A_{i,r}t^r,
 \quad \mathcal C(t)=\sum_{r\geq0}C_rt^r.
\]
Use \(\mathcal S_0=\overline{\mathcal S}_0=1\) and
\(\overline{\mathcal S}_1=0\). Exponentiating \(T\) coefficient by coefficient is multiplicative, by its finite Leibniz rule. The invariant tensor algebra in (TR.5) is commutative, so (TR.12) becomes the exact formal-series identity
\[
 \boxed{\mathcal S_k(t)=
 \sum_{i=0}^{k}\binom{n-i}{k-i}
       \overline{\mathcal S}_i(t)H_{k-i}(\mathcal C(t)),}
 \qquad H_{d+1}=(\partial_t+\mathcal C)H_d.
 \tag{TR.14}
\]
This includes every divided translate. Equivalently,
\[
 A_{k,r}=
 \sum_{i=0}^{k}\binom{n-i}{k-i}
       \sum_{a+b=r}\overline A_{i,a}
                    [t^b]H_{k-i}(\mathcal C(t)).
\]
All terms are finite. The central coefficients needed in a deficit-\(d\) term have indices at most \(r+d-1\); a positive derivative can therefore require central modes beyond the pointed \(r\)-jet, and those terms must be retained.

The inverse is triangular in \(k\): first recover
\(C_r=A_{1,r}/n\), then recursively subtract the \(i<k\) terms of (TR.14) to recover every \(\overline A_{k,r}\). Each recovered coefficient is a finite polynomial. Consequently
\[
 \boxed{Z_{\mathfrak{gl}_n,R}
      =R[A_{k,r}:1\leq k\leq n,\ r\geq0],}
 \tag{TR.15}
\]
and the raw generators are algebraically independent. Formally, send independent raw variables into the polynomial ring (TR.6) by (TR.14). The coefficientwise inverse recursion defines an inverse homomorphism of polynomial rings, proving independence as well as generation. No completion is involved in either algebra, even though its coefficient-valued points permit arbitrary power-series sequences.

**The scalar coefficient functor with a framed central form.** Let
\[
 h=\frac{1-n}{2},\qquad
 \overline{\mathcal L}
     =\partial_t^n+\sum_{i=2}^{n}\overline s_i(t)\partial_t^{n-i},
 \qquad c(t)\,dt\in R[[t]]\,dt.
\]
For \(n=1\), the normalized operator is just \(\partial_t\). The normalized type-A scalar operator has source density weight \(h\) and target weight \(h+n\). The additional datum \(c(t)\,dt\) is a central connection coefficient in a **fixed central frame**.

In the ordinary differential-operator ring, define the automorphism
\(\Phi_c\) by fixing every coefficient and sending
\(\partial_t\) to \(\partial_t+c(t)\). It preserves
\([\partial_t,f]=f'\), and \(\Phi_{-c}\) is its inverse. Define
\[
 \mathcal L_c=\Phi_c(\overline{\mathcal L})
       =(\partial_t+c)^n
            +\sum_{i=2}^{n}\overline s_i(\partial_t+c)^{n-i}
       =\partial_t^n+\sum_{k=1}^{n}s_k(t)\partial_t^{n-k}.
 \tag{TR.16}
\]
The same finite induction as (TR.10) gives
\[
 s_k=\sum_{i=0}^{k}\binom{n-i}{k-i}\overline s_iH_{k-i}(c),
 \qquad \overline s_0=1,\quad\overline s_1=0,\quad s_1=nc.
 \tag{TR.17}
\]
Conversely set \(c=s_1/n\), and apply \(\Phi_{-c}\) to a raw monic operator. Its subprincipal coefficient is \(s_1-nc=0\); its other coefficients are the inverse triangular polynomials. Therefore, over every ordinary \(R\), (TR.16) is an isomorphism of coefficient functors
\[
 \left\{(\overline{\mathcal L},c(t)\,dt)\right\}
       \ \simeq\
 \left\{\partial_t^n+\sum_{k=1}^{n}s_k(t)\partial_t^{n-k}\right\}.
 \tag{TR.18}
\]
The left side means the normalized scalar coefficient functor and a framed central form. Its identification of the normalized factor with intrinsic \(PGL_n\)-opers uses precisely the previously stated finite-jet, vector-lift and descent premises of §§2.2–2.6. Equation (TR.18) itself is proved entirely by finite differential algebra.

Combining (SL.X26) with the identity of the central polynomial rings and (TR.14)–(TR.17) yields the entire vacuum-coefficient algebra comparison:
\[
 \begin{aligned}
 Z_{\mathfrak{gl}_n,R}
 &\xrightarrow{\sim}
 R[\overline s_{i,r},c_r:2\leq i\leq n,\ r\geq0]\\
 &\xrightarrow{\sim}
 R[s_{k,r}:1\leq k\leq n,\ r\geq0],
 \qquad
 \overline A_{i,r}\mapsto\overline s_{i,r},\
 C_r\mapsto c_r,\
 A_{k,r}\mapsto s_{k,r}.
 \end{aligned}
 \tag{TR.19}
\]
For \(n=1\), the normalized coefficient list is empty. This is a regular vacuum theorem and a specified framed coefficient comparison.

**Full coordinates, including the trace mixing.** Under the current substitution
\(xF(t)\mapsto xF(\phi(t))\), let \(\psi=\phi^{-1}\). The scalar factor transforms exactly as an ordinary one-form on coefficient functions:
\[
 U_\phi\mathcal C(t)U_\phi^{-1}
        =\psi'(t)\mathcal C(\psi(t)).
 \tag{TR.20}
\]
To prove this directly, its \(r\)-th vacuum state is \(c[-r-1]v\). In its substituted current only negative modes survive, since nonnegative central modes act as zero on the whole vacuum. The coefficient of \(c[-s-1]\) is
\(\operatorname{Res}_u u^s\phi(u)^{-r-1}du\). Residue substitution turns this into
\(\operatorname{Res}_t \psi(t)^s\psi'(t)t^{-r-1}dt\), the coefficient of \(t^r\) on the right side of (TR.20). The existing residue proof applies also to nilpotent constant coordinates. In particular,
\[
 \delta_fc=-fc'-f'c,\qquad
 [D_l,C_r]=-\mathbf1_{r\geq l}(r+1)C_{r-l}
       \quad(l\geq-1),
 \tag{TR.21}
\]
where the \(l=-1\) term is always present. There is no central scalar anomaly for this zero-level abelian factor.

There is an exact finite-order transport identity behind the comparison. For a passive coordinate \(t=\eta(u)\), put \(\alpha=\eta'\) and
\[
 \mathcal T_\eta(D)=
 \alpha^{h+n}
    \left.D\right|_{t=\eta(u),\,\partial_t=\alpha^{-1}\partial_u}
       \alpha^{-h}.
\]
Then
\[
 \boxed{\mathcal T_\eta\bigl(\Phi_c(D)\bigr)
      =\Phi_{\widetilde c}\bigl(\mathcal T_\eta(D)\bigr),
       \qquad \widetilde c=\alpha\,c\circ\eta.}
 \tag{TR.22}
\]
To verify it, put \(b=\alpha'/\alpha\). Conjugation removes the apparent half powers and rewrites the two sides respectively as
\[
 \alpha^n\sum_i \overline s_i(\eta)
   \left(\alpha^{-1}(\partial_u-hb)+c(\eta)\right)^{n-i},
 \qquad
 \Phi_{\widetilde c}\!
 \left(\alpha^n\sum_i\overline s_i(\eta)
             \left(\alpha^{-1}(\partial_u-hb)\right)^{n-i}\right).
\]
They agree term by term, because \(\Phi_{\widetilde c}\) fixes all coefficient series and
\(\alpha^{-1}\widetilde c=c(\eta)\). This proves (TR.22) without interchanging noncommuting factors. Its expressions use only integer powers of \(\alpha\), its inverse, relative derivatives and rational constants. Thus they already descend to \(R\), also when the density weights are half-integral.

For an explicit full raw-coefficient formula, define \(B_{0,0}=1\), set out-of-range entries to zero, and use the finite recursion
\[
 B_{m+1,j}=\alpha^{-1}
   \left(B_{m,j}'-h\frac{\alpha'}{\alpha}B_{m,j}
                         +B_{m,j-1}\right).
\]
Repeated product rules prove
\((\alpha^{-1}\partial_u)^m\alpha^{-h}
 =\alpha^{-h}\sum_{j=0}^{m}B_{m,j}\partial_u^j\).
Consequently the complete transport is
\[
 \boxed{\widetilde s_k(u)=
   \alpha(u)^n\sum_{i=0}^{k}s_i(\eta(u))B_{n-i,n-k}(u),
      \qquad s_0=1.}
 \tag{TR.23}
\]
Unlike the traceless specialization, \(s_1\) is retained. The cancellation
\(B_{n,n-1}=-(nh+n(n-1)/2)\alpha^{-n}\alpha'/\alpha=0\)
shows \(\widetilde s_1=\alpha s_1\circ\eta\). Each fixed Taylor coefficient is a finite polynomial in the original coefficients, coordinate coefficients and inverse linear coefficient. If \(\eta(0)^\nu=0\), the terms of \(s_i(\eta)\) needed at Taylor order \(r\) have original index at most \(r+\nu-1\), by (SC.O3). The recursion adds only finitely many derivatives. Thus (TR.23) commutes with every ordinary base change, without requiring reducedness or flatness.

The matching quantum law holds for the raw determinant before quotienting out the trace. Indeed, the proved all-\(n\) identities (SL.X6), (SL.X10) and their positive-Witt induction (SL.X13) were obtained with
\(w_k=S_kv\), \(w_0=v\) and the actual \(w_1=J[-1]v\). Applying the divided-translation identity (TC.A5) before the quotient, with
\[
 C_{ki}=\binom{n-i}{k-i+1}
                  +h\binom{n-i}{k-i},
\]
gives
\[
 \boxed{\delta_f\mathcal S_k
   =-f\mathcal S_k'-kf'\mathcal S_k
       +\sum_{i=0}^{k-1}C_{ki}f^{(k-i+1)}\mathcal S_i,
       \qquad 1\leq k\leq n.}
 \tag{TR.24}
\]
The coefficient at any Taylor order is a finite sum. The \(k=1\) correction is zero since \(C_{10}=\binom n2+hn=0\), agreeing with (TR.20). On scalar operators the finite Leibniz rule applied to
\(\delta_fD=-(f\partial+(h+n)f')D+D(f\partial+hf')\)
gives precisely (TR.24), now retaining \(s_1\). This uses the full quantum identities, not merely their PBW symbols.

For \(n\geq2\), a visible check of the derivative weight is obtained by setting
\(\gamma_n=n(n^2-1)/12\). From (TR.13), (TR.20) and the normalized quadratic law,
\[
 \begin{aligned}
 \delta_f\mathcal S_2
 &=-f\mathcal S_2'-2f'\mathcal S_2
       -\frac{n-1}{2}f''\mathcal S_1-\gamma_n f''' ,\\
 \widetilde s_2
 &=\alpha^2s_2(\eta)
       +\frac{n-1}{2}\alpha's_1(\eta)
       +\gamma_n\operatorname{Sch}(\eta).
 \end{aligned}
 \tag{TR.25}
\]
The scalar term in the first line is times the identity endomorphism.
In fact \(\delta_f(c^2+c')=-f(c^2+c')'-2f'(c^2+c')-f''c\).
This last term accounts exactly for the trace mixing. For \(n=2\),
\(S_2=\overline S_2+c^2+c'\); setting \(c=0\) recovers
\(\overline S_2=-Q_{\mathrm{K3}}/2\), with the factor and Schwarzian sign already checked in §3.4.4.

Equations (TR.20), (TR.22) and the full traceless comparison (SL.X26) prove full coordinate equivariance of (TR.19). Equivalently, the exact raw derivations (TR.24) integrate by the finite nilpotent translations, unit scalings and positive formal flows proved in (TC.A8). Translation is finite because its parameter is nilpotent, scaling has weight \(k+r\), and a positive flow lowers this energy and has a finite exponential on each polynomial. The forward formula is (TR.23); the action on coefficient functions in (TR.19) uses \(\eta=\psi=\phi^{-1}\).

The mechanism is displayed by the commuting square:
\[
 \begin{array}{ccc}
 R[C_r,\overline A_{i,r}]
 &\xleftarrow{\ \text{(TR.14)}\ }&R[A_{k,r}]\\[2pt]
 \downarrow{\scriptstyle C_r\mapsto c_r,\
                         \overline A_{i,r}\mapsto\overline s_{i,r}}
 &&\downarrow{\scriptstyle A_{k,r}\mapsto s_{k,r}}\\[2pt]
 R[c_r,\overline s_{i,r}]
 &\xleftarrow{\ \partial\mapsto\partial+c,\ \text{(TR.17)}\ }
 &R[s_{k,r}].
 \end{array}
\]
*Both horizontal arrows send a raw coefficient on the right to its
triangular expression in the split coefficients on the left, and are
invertible. The top arrow is the actual right-ordered determinant shift (TR.8);
the bottom arrow is the scalar shift (TR.16). The central coordinate is a
one-form by (TR.20), and (TR.22) compares the full density transport.
Thus every arrow respects the full inverse-coordinate action, including
ordinary nonreduced parameters.*

Finally, the central frame is part of the stated coefficient problem.
In the gauge convention \(\nabla\mapsto g\nabla g^{-1}\) of (CF.5), changing that frame by a unit \(g(t)\) changes a connection coefficient:
\[
 g(\partial_t+c)g^{-1}
    =\partial_t+c-\frac{g'}{g},
 \qquad
 g\mathcal L_cg^{-1}=\mathcal L_{c-g'/g}.
 \tag{TR.26}
\]
For example \(g=\exp(at)\) changes \(c\) to \(c-a\). The framed functor in
(TR.18) retains these as different coefficients. An intrinsic central
gauge quotient would identify them and also retain the appropriate
bundle and automorphism data; it is a different functor. No intrinsic
\(GL_n\)-oper equivalence follows merely from (TR.19).
The proved scope is the entire regular critical \(GL_n\) vacuum algebra
and its full ordinary formal-disc comparison with a normalized type-A
scalar operator plus a framed central one-form. Global nonadjoint
bundle conventions, completed punctured-disc centres, chiral or Poisson
structures, and derived coefficient algebras require their separate
arguments.

#### 3.5.3. Residue direction, the central line and critical normalization

There are three pieces of an affine convention: the direction of the residue cocycle, its invariant form, and the scalar by which the chosen central generator acts. Their product determines the current commutator on a representation. Changing only the name of the central generator does not preserve its prescribed action. This distinction is necessary when comparing the critical vacuum here with a geometric source convention.

##### The elementary comparison

Let \(B\) be an invariant symmetric bilinear form on a finite-dimensional Lie algebra \(\mathfrak g\). For \(\epsilon\in\{1,-1\}\), define the central extension with an explicit bracket by
\[
\widehat{\mathfrak g}_{\epsilon,B}
=\mathfrak g((t))\oplus k\mathsf K,
\qquad
[xf,yg]=[x,y]fg+
\epsilon B(x,y)\operatorname{Res}_t((df)g)\mathsf K.
\tag{CS.1}
\]
Here \(f,g\) are scalar Laurent series. Products and residues are coefficientwise finite because Laurent series have finite negative parts. The formal derivative has zero residue, so
\[
\operatorname{Res}((df)g)=-\operatorname{Res}(f\,dg).
\tag{CS.2}
\]
Symmetry of \(B\) and (CS.2) prove skew symmetry. Invariance of \(B\) makes the three form coefficients in the central part of Jacobi equal; their residue factors sum to the residue of \(d(fgh)\), which is zero. Thus (CS.1) is a Lie bracket. For polynomial modes it reads
\[
[x_m,y_j]=[x,y]_{m+j}
+\epsilon mB(x,y)\delta_{m,-j}\mathsf K.
\tag{CS.3}
\]
In particular a cocycle written with \(+\operatorname{Res}(f\,dg)\) has \(\epsilon=-1\), if the extension bracket adds the displayed cocycle.

Consider two such extensions, with data \((\epsilon_s,B_s,\mathsf K_s)\) and \((\epsilon_t,B_t,\mathsf K_t)\). Fix \(a\in k^\times\). The map which is the identity on every current and sends \(\mathsf K_s\) to \(a\mathsf K_t\) is a Lie algebra isomorphism if and only if
\[
a\epsilon_s B_s=\epsilon_t B_t.
\tag{CS.4}
\]
Indeed applying the map to the bracket in (CS.3) multiplies its central coefficient by \(a\), while the target bracket has the right side of (CS.4). Equality of these coefficients is sufficient for every pair of Laurent currents. It is necessary by choosing modes \(m=1,j=-1\) and arbitrary \(x,y\). The inverse map uses \(a^{-1}\). Hence this is a complete comparison of the specified central extensions, with no center theorem as a premise.

Suppose the target central generator acts by \(\ell_t\). Pulling a target module back along this isomorphism makes the source central generator act by
\[
\ell_s=a\ell_t.
\tag{CS.5}
\]
Combining (CS.4) and (CS.5), the effective form on the representation must satisfy
\[
\boxed{\epsilon_s\ell_sB_s=\epsilon_t\ell_tB_t.}
\tag{CS.6}
\]
This condition is also the exact direct test at fixed levels. In the quotient of the enveloping algebra by \(\mathsf K-\ell\), relation (CS.3) depends only on \(\epsilon\ell B\). Equal effective forms therefore give identical current relations. The nonnegative-current induction relations agree as well, so the identity on negative current words gives the vacuum-module identification, using the ordered basis proved in §3. Conversely, applying \([x_1,y_{-1}]\) to the nonzero vacuum gives \(\epsilon\ell B(x,y)v\); an identification fixing the currents and vacuum forces (CS.6). This proves the necessary and sufficient representation comparison, including its normalization.

For equal forms but opposite residue directions, (CS.4) requires
\(a=-1\). Thus
\[
\mathsf K_s\mapsto-\mathsf K_t
\quad\Longrightarrow\quad
\ell_s=-\ell_t.
\tag{CS.7}
\]
A change of central generator cannot both reverse the cocycle and keep the generator acting by \(+1\) on the same representation. Alternatively, reversing both residue direction and form, while keeping the central action \(+1\), satisfies (CS.6).

##### The two exact source conventions

Frenkel's [*Lectures on the Langlands program and conformal field theory*, arXiv:hep-th/0512172v1, §§7.1 and 8.1](https://arxiv.org/abs/hep-th/0512172v1) explicitly writes a current bracket with central term \(-\kappa_0(x,y)\int f\,dg\), and defines level \(k\) as the action of its generator \(\mathbf1\). Its displayed mode commutator in §8.1 is
\[
[J^a_m,J^b_j]=[J^a,J^b]_{m+j}
+m\kappa_0(J^a,J^b)\delta_{m,-j}\mathbf1.
\tag{CS.8}
\]
This mode formula fixes the normalization of the formal integral: the source uses our \(df\)-first sign. It normalizes \(\kappa_0\) so that a long root has squared length two; for \(\mathfrak{sl}_n\), \(\kappa_0(X,Y)=\operatorname{tr}(XY)\). It gives critical level \(k=-h^\vee\) and also explicitly describes the same representation by replacing the form with
\(\kappa_{\rm crit}=-\operatorname{Kil}/2\) and having \(\mathbf1\) act as the identity. Thus the source's normalization is
\[
(-h^\vee)\kappa_0=\kappa_{\rm crit}
=-\frac12\operatorname{Kil}.
\tag{CS.9}
\]
For general simple root systems, the equality in (CS.9) between the long-root normalization and the named dual Coxeter number is the source normalization premise; a general root-trace proof of that identity is not supplied here. With this explicit premise, (CS.6) proves the equality of the two vacuum conventions. In type A the needed identity is proved directly by the matrix trace calculation (GQ.20). At the level of extensions, the map from the normalized-form extension to the critical-form extension is the identity on currents and sends
\(\mathbf1_0\mapsto-h^\vee\mathsf K_{\rm crit}\); pullback of \(\mathsf K_{\rm crit}=1\) has \(\mathbf1_0=-h^\vee\). For \(\mathfrak{sl}_n\), the matrix trace computation in (GQ.20) gives \(\operatorname{Kil}=2n\operatorname{tr}\), so this agrees with our form \(-n\operatorname{tr}\). In rank one the normalized level is \(-2\).

Raskin's [*A geometric proof of the Feigin–Frenkel theorem*, arXiv:1106.3112v1, introduction §§1.2–1.4](https://arxiv.org/abs/1106.3112v1) records the following data: the extension is defined by the cocycle
\(\operatorname{Res}\kappa(f,dg)\); the element \(1\) of the central copy of \(\mathbb C\) acts as the identity; and the form called critical is \(-\operatorname{Kil}/2\). The definition gives a cocycle rather than an explicit two-current bracket. Its residue direction is therefore accurately reported as \(f\)-first, but the relation between that reported cocycle and the bracket must be specified before a direct module comparison.

If an extension bracket **adds** that listed cocycle, its mode central term and effective form are
\[
[x_m,y_j]_{\rm central}
=-m\kappa(x,y)\delta_{m,-j}\mathsf K_R,
\qquad
\mathsf K_R=1,\quad \kappa=-\operatorname{Kil}/2
\quad\Longrightarrow\quad
B_{\rm eff}=+\operatorname{Kil}/2.
\tag{CS.10}
\]
Under this explicit bracket interpretation, (CS.6) shows that these data do not identify the stated vacuum with our \(df\)-first, negative-half-Killing, central-action-one vacuum. The identity-current isomorphism with the same form sends our \(\mathsf K\) to \(-\mathsf K_R\), so the pulled-back central action is \(-1\), as in (CS.7). A matching convention with an added \(f\)-first cocycle must instead use one of the following equivalent data:
\[
\begin{array}{c|c|c}
\text{residue direction}&\text{form}&\text{central action}\\\hline
f\text{-first}&+\operatorname{Kil}/2&+1\\
f\text{-first}&-\operatorname{Kil}/2&-1\\
df\text{-first}&-\operatorname{Kil}/2&+1.
\end{array}
\tag{CS.11}
\]
All three have the same effective mode form \(-\operatorname{Kil}/2\). If, instead, the convention defining the extension **subtracts** Raskin's listed cocycle, its explicit bracket is \(df\)-first with his stated negative-half-Killing form and central action one, and it matches immediately. This alternative is a conditional interpretation; the cocycle-only definition does not supply this explicit bracket.

Equations (CS.4)–(CS.7) give the complete algebraic comparison. Raskin's cocycle-only definition does not explicitly fix the bracket sign needed for the direct vacuum identification. Consequently a generator flip with central action one cannot by itself transfer the geometric vacuum assertion. The geometric line must be compared with the explicit commutator and central scalar; that identification remains a separate requirement.

There is a concrete rank-one test for any proposed resolution. With the \(df\)-first mode form \(\ell\kappa_0\), the direct calculation of §3.1 gives
\[
e_1Q=2(\ell+2)e_{-1}v.
\tag{CS.12}
\]
Our \(\ell=-2\) makes this zero. The literal added-cocycle reading of (CS.10) has effective \(\ell=+2\), giving \(8e_{-1}v\ne0\) by the ordered basis. Hence that reading cannot preserve our invariant quadratic vector. This is an elementary obstruction, not an argument imported from a Feigin–Frenkel theorem. It pinpoints the sign that a geometric comparison must resolve.

##### Geometric line weights are part of the comparison

Frenkel's §§7.4–7.5 describe localization at level \(k\) by differential operators on \(\mathcal L^{\otimes k}\), where \(\mathcal L\) is the line obtained from the central group extension and is the theta generator on \(\operatorname{Bun}_G\). The source notes that integral powers can be constructed as representation determinant lines; it does not make that footnote a formula for a particular determinant orientation. Its opening of §8 states
\[
K_{\operatorname{Bun}_G}\simeq\mathcal L^{-2h^\vee},
\qquad
\mathcal L^{-h^\vee}\simeq K_{\operatorname{Bun}_G}^{1/2},
\tag{CS.13}
\]
under its simply connected simple hypotheses. Section 9.4 also says explicitly that the normalized affine central generator maps to \(-h^\vee\) in differential operators on the corresponding critical power on the affine Grassmannian. These are the source's geometric convention statements. Their line-bundle construction and canonical-line theorem are additional geometric inputs, not consequences of (CS.1)–(CS.7).

Raskin's introduction §1.9 defines its critical line on \(\operatorname{Gr}_G\) through a central \(\mathbb G_m\)-extension split over \(G(O)\), with its Lie extension identified with the previously defined affine algebra. It assumes the simply connected semisimple group; its footnote records a gerbe of choices otherwise. Section 1.10 obtains global sections from the infinitesimal action on this line, and states that sections are taken as an ordinary \(\mathcal O\)-module. These passages specify no representation determinant formula, dual determinant choice, or explicit comparison to Frenkel's \(\widetilde{\mathcal L}^{-h^\vee}\). That missing identification must not be filled in by guessing a sign from the word “critical.”

The elementary part of a line-weight comparison is also explicit. For a Lie algebra acting on a line \(L\), its induced action on \(L^\vee\) is defined by
\[
(\xi\cdot\varphi)(s)=\xi\bigl(\varphi(s)\bigr)-\varphi(\xi\cdot s).
\tag{CS.14}
\]
A vertical central operator acting by \(a\) on \(L\) therefore acts by \(-a\) on \(L^\vee\). Tensor powers multiply that weight by their exponent. Similarly an endomorphism \(A\) of a finite vector space acts on its top exterior line by \(\operatorname{tr}A\), as follows by applying the product rule to a basis wedge; the dual determinant has the opposite scalar. Choosing
\(\det H^0\otimes(\det H^1)^{-1}\) or its dual likewise reverses a determinant-character convention. This proves why a geometric determinant dual or central-character inverse must be tracked. It does not prove that either source's geometric critical line is a particular such determinant, nor identify geometric Lie actions without their construction.

##### Oper objects and central frames

Frenkel's §8.3 defines an oper for a simple Lie algebra using its adjoint group. Its intrinsic object is a group bundle with a connection and a Borel reduction satisfying the simple-root transversality condition. The local Borel trivialization is used to express the connection; it is not an additional frame retained in the oper object. Raskin's introduction §§1.5–1.6 similarly starts with a simply connected semisimple automorphic group and its adjoint dual, and defines the spectral oper by a dual Borel bundle and a connection on the associated dual group bundle. Its ordinary-family footnote uses a bundle on \(\operatorname{Spec}(A[[t]])\) with a connection along \(t\). Its canonical Borel bundle over the oper scheme records the fiber at zero; it is not a chosen trivialization of that fiber.

The framing on the punctured disc in Raskin's affine-Grassmannian definition is a different object: it belongs to the automorphic group bundle parameterized by \(\operatorname{Gr}_G\), not to the spectral oper definition. The second transversal Borel reduction at zero in its generic-Miura remark is also a reduction, rather than a full frame. None of these passages supplies an all-reductive or torus oper definition with a retained torus framing.

Frenkel's §9.5 says that the abelian analogue is a connection on the trivial line bundle. It does not specify whether an isomorphism from that bundle to the trivial one is part of the object, nor give a torus-family quotient/framing definition. The distinction has an elementary local test. In a fixed rank-one trivialization, a connection is
\[
\nabla=\partial_t+a(t).
\]
An automorphism \(g(t)\in R[[t]]^\times\) gives the operator gauge rule
\[
g\nabla g^{-1}=\partial_t+a(t)-\frac{g'(t)}{g(t)}.
\tag{CS.15}
\]
This follows by applying both sides to a section and the product rule. Even fixing the fiber frame at zero only imposes \(g(0)=1\), and does not prevent this change. For example \(g(t)=\exp(ct)\) is a well-defined formal unit with \(g(0)=1\) over a characteristic-zero algebra, and sends \(a(t)\) to \(a(t)-c\). A retained trivialization along the entire disc instead allows only the identity as a frame-preserving gauge. These are different moduli conventions. No assertion that every torus torsor over every ordinary base is trivial is used here.

Finally, for a reductive Lie algebra \(\mathfrak g=\mathfrak z\oplus\mathfrak g_{\rm ss}\), the Killing form vanishes on \(\mathfrak z\): every central adjoint operator is zero. Thus extending “minus half the Killing form” literally to the center gives zero central-current cocycle there. A separate nonzero invariant form on the torus would give a Heisenberg cocycle instead. Condition (CS.6) compares those center forms too; they cannot be identified merely from the semisimple critical convention. Those definitions concern simple or semisimple affine data, so they do not choose this additional reductive-center datum. The full reductive/torus framing and geometric critical-line comparison therefore retain their explicit foundations.

#### 3.5.4. Central connection coefficients and the gauge groupoid

Let \(k\) be a characteristic-zero field, \(R\) any ordinary commutative \(k\)-algebra, and \(T=(\mathbb G_m)^d\) a split torus. This subsection concerns a **trivial torus bundle with a chosen frame** on the formal disc. Its connection coefficients form the functor
\[
\mathcal C_T(R)=\operatorname{Lie}(T)\otimes_k R[[t]]\,dt.
\tag{CF.1}
\]
Choose a basis \(e_1,\ldots,e_d\) of \(\operatorname{Lie}(T)\), and write
\(a(t)=\sum_{i,r\ge0}a_{i,r}e_it^r\). Sending each variable \(a_{i,r}\) to the identically indexed coefficient proves directly that this functor is represented by
\[
\mathcal O(\mathcal C_T)=k[a_{i,r}:1\le i\le d,\ r\ge0].
\tag{CF.2}
\]
The coefficient list can be infinite, while an element of the coordinate ring is a finite polynomial. The construction is natural in every ordinary parameter algebra. The chosen basis describes a coordinate ring; it does not form part of the connection itself.

**Coordinate transport.** For \(t=\phi(s)\), the connection one-form has direct law
\[
\mathcal P_\phi(a)(s)=\phi'(s)a(\phi(s)).
\tag{CF.3}
\]
It follows by applying the chain rule to \(\partial_t+a(t)\) and multiplying by \(\phi'\) to restore the coefficient of \(\partial_s\) to one. This is an ordinary one-form, with no density or Schwarzian correction. Formula (CF.3) composes by the chain rule. If \(\phi(0)^N=0\), its coefficient of order \(r\) uses only original coefficients of order less than \(r+N\): in a term \(\phi^m\), at least \(m-r\) factors must supply the constant coefficient. The multiplier \(\phi'\) changes this bound only by a finite convolution. Thus nilpotent translations and arbitrary ordinary parameter rings cause no infinite evaluation in a fixed coefficient.

As throughout §3.4, current substitution corresponds to the inverse action on functions. For \(\psi=\phi^{-1}\), the algebraic action on the displayed coefficient series is
\[
a(t)\longmapsto\psi'(t)a(\psi(t)),\qquad
\delta_fa=-fa'-f'a.
\tag{CF.4}
\]
The second formula follows by substituting \(\psi=t-\varepsilon f\), \(\varepsilon^2=0\), in the first. These are the central-series laws proved on the actual vacuum in §3.5.1.

**Changing the central frame.** A gauge \(u=(u_1,\ldots,u_d)\in T(R[[t]])\) has logarithmic derivative
\[
\operatorname{dlog}u=(u_i'/u_i)_{i=1}^d\,dt.
\tag{CF.5}
\]
In the convention \(\nabla\mapsto u\nabla u^{-1}\), it sends the coefficient to
\(a-\operatorname{dlog}u\). Indeed,
\(u\partial_tu^{-1}=\partial_t-u'/u\). The logarithmic derivative is a group homomorphism because the torus is commutative.

Every coefficient form is a logarithmic derivative over \(R\). For a scalar component
\(a(t)=\sum_{r\ge0}a_rt^r\), put
\[
b(t)=\sum_{r\ge0}\frac{a_r}{r+1}t^{r+1},\qquad
u(t)=\exp b(t)=\sum_{j\ge0}\frac{b(t)^j}{j!}.
\tag{CF.6}
\]
Each coefficient of this exponential is finite because \(b(0)=0\). The formal product rule gives \(u'=b'u=a u\), and \(u(0)=1\). Thus \(\operatorname{dlog}u=a\,dt\). Alternatively, the coefficient recursion
\[
u_0=1,\qquad
(r+1)u_{r+1}=\sum_{i+j=r}a_i u_j
\tag{CF.7}
\]
proves existence and uniqueness with this initial value, without assuming reducedness of \(R\). If a unit series has zero logarithmic derivative, then \(u'=0\), and every nonconstant coefficient is zero because all positive integers are units. Its kernel is therefore precisely the constant units. Componentwise, we have proved the exact sequence
\[
1\longrightarrow T(R)\longrightarrow T(R[[t]])
\xrightarrow{\operatorname{dlog}}\mathcal C_T(R)
\longrightarrow0.
\tag{CF.8}
\]
The subgroup of gauges with value one at the origin maps bijectively to \(\mathcal C_T(R)\). The inverse is (CF.6), and it is a group homomorphism because \(\exp(b+c)=\exp(b)\exp(c)\) for commuting formal series, as the finite coefficient binomial identity shows. No analytic exponential or logarithm is used.

Consequently every framed connection is gauge equivalent to zero, and the automorphism group of the zero connection is \(T(R)\). The groupoid of connections on the trivial bundle, with arbitrary formal torus gauges, is equivalent to the one-object groupoid with this automorphism group. One explicit equivalence sends the zero connection to itself and regards constants as its automorphisms; it is fully faithful by the kernel assertion, and essentially surjective by (CF.6). If gauges must have value one at the origin, the quotient groupoid instead has a unique object and a unique arrow between any two presented connections. Both assertions are natural in \(R\).

The algebra of framed coefficients therefore differs from its algebra of gauge-invariant functions. To prove the latter statement as a functor assertion, let \(F\) be a finite polynomial in the \(a_{i,r}\), invariant under all formal gauges after every ordinary extension of \(R\). Surjectivity in (CF.8) includes the universal translations of its finitely many variables. Hence
\[
F(X+Y)=F(X)\quad\Longrightarrow\quad F(Y)=F(0)
\tag{CF.9}
\]
by setting \(X=0\). Thus the invariant polynomial algebra is \(R\). This argument remains valid if \(R\) has nilpotents. In particular, for the one-dimensional abelian Lie algebra with zero affine form, §3.5.1 gives the infinite polynomial vacuum algebra \(R[z_r:r\ge0]\); it cannot be identified with the polynomial gauge-invariant functions on the unframed trivial line-connection groupoid, which are just \(R\).

| Central datum retained | Coefficients and arrows on the trivial formal bundle | Result of the proved gauge calculation |
| --- | --- | --- |
| A chosen formal frame | All \(a_{i,r}\) remain coordinates | The coefficient ring is (CF.2). |
| Frames related by gauges equal to one at the origin | The coefficient forms are related by the unique solution (CF.7) | The quotient groupoid is contractible. |
| Frames related by arbitrary formal gauges | The same solution leaves the constant gauge group | The quotient is the one-object groupoid with automorphisms \(T(R)\). |

*The table concerns connections on a trivial torus bundle. It describes the effect of changing the frame, not a classification of all torus torsors over an arbitrary base or on a global curve. Its arrows and stabilizers are proved in (CF.5)–(CF.9).*

#### 3.5.5. The dual central coefficient space and the reductive comparison

For a split torus \(T\), let \(X^*(T)\) and \(X_*(T)\) be its character and cocharacter lattices. The elementary perfect lattice pairing identifies
\[
\operatorname{Lie}(T)=X_*(T)\otimes_{\mathbb Z}k,\qquad
\operatorname{Lie}(\check T)=X^*(T)\otimes_{\mathbb Z}k
 =\operatorname{Lie}(T)^*.
\tag{CF.10}
\]
For completeness, choose a lattice basis. Characters are Laurent monomials, their derivatives at the identity evaluate the exponent on a cocharacter, and the two basis matrices pair as the identity. Changing the lattice basis changes one matrix by the inverse transpose of the other, so the identification is independent of that basis.

The negative current \(x_{-r-1}\), \(x\in\operatorname{Lie}(T)\), is consequently a coefficient function on framed dual-torus connections: it evaluates the order-\(r\) coefficient against \(x\). Symmetric-algebra freeness proves, over every ordinary \(R\),
\[
\operatorname{End}_{\widehat{\operatorname{Lie}(T)},\,\kappa=0}(V_R)
\simeq R[\mathcal C_{\check T}],\qquad
x_{-r-1}v\longmapsto\bigl(a\mapsto\langle x,a_r\rangle\bigr).
\tag{CF.11}
\]
This is precisely the abelian case of §3.5.1. That subsection and (CF.3)–(CF.4) prove the full ordinary coordinate equivariance, including nilpotent translations.

For a split reductive group with maximal torus, its standard root-data premises give the corresponding Lie-algebra identification without choosing a form on the center. Its central Lie algebra is the annihilator of the span of the roots in \(X^*(T)\otimes k\). The dual of that annihilator is the quotient by the root span. In the dual root datum, the coroots are these original roots, so that quotient is the Lie algebra of the dual group's abelianization. This is a finite-dimensional annihilator/quotient identity: restricting linear functionals is surjective by extending a basis, and its kernel is exactly the root span. The root-data descriptions of the reductive decomposition and abelianization are the structural premises here; global central isogenies and their torsors are not inferred from the Lie-algebra identity.

Combining the proved reductive vacuum factorization with the type A semisimple comparison gives the following explicit ordinary coefficient space. If
\(\mathfrak g=\bigoplus_j\mathfrak{sl}_{n_j}\oplus\mathfrak z\) at the critical form, then
\[
\operatorname{End}_{\widehat{\mathfrak g},\mathrm{crit}}(V_R)
\simeq
R\left[\prod_j\operatorname{Op}_{PGL_{n_j}}(D_R)
       \times\bigl(\mathfrak z^*\otimes R[[t]]\,dt\bigr)\right].
\tag{CF.12}
\]
The notation on the right denotes the polynomial coefficient algebra of the displayed functor. Each horizontal factor is an actual isomorphism: §3.4.6 for the adjoint type A oper factors and (CF.11) for the framed central coefficient factor. Tensoring their polynomial generator maps proves the equality; §3.5.1 and the componentwise coordinate laws prove full coordinate equivariance. For a general split semisimple summand, the reductive factorization still holds, while its non-type-A oper identification remains a separate proof obligation.

The central square showing the exact coordinate convention is
\[
\begin{array}{ccc}
\operatorname{Sym}_R(\mathfrak z\otimes t^{-1}R[t^{-1}])
 &\longrightarrow&R[\mathfrak z^*\otimes R[[t]]\,dt]\\[2pt]
{\scriptstyle U_\phi}\downarrow
 &&\downarrow{\scriptstyle a(t)\mapsto\psi'(t)a(\psi(t))}\\[2pt]
\operatorname{Sym}_R(\mathfrak z\otimes t^{-1}R[t^{-1}])
 &\longrightarrow&R[\mathfrak z^*\otimes R[[t]]\,dt],
\qquad \psi=\phi^{-1}.
\end{array}
\tag{CF.13}
\]
*Each horizontal arrow evaluates a negative current against its equally indexed coefficient. The left vertical action is actual current substitution on the zero-form abelian vacuum. The right vertical label specifies the inverse one-form law on the generators of its coordinate ring. Section 3.5.1 and (CF.3)–(CF.4) prove that the square commutes over every ordinary parameter ring.*

In the \(\mathfrak{gl}_n\) example, the trace current represents the central direction \(I\), and the determinant character of the dual group pairs with that direction by the trace. The coefficient called \(c\) in §3.5.2 is one \(n\)-th of the trace coefficient; the raw scalar operator has subprincipal coefficient \(s_1=nc\). Thus the trace decomposition gives a concrete realization of (CF.12). Its framed scalar operators are acted on by central gauge through \(c\mapsto c-u'/u\); the normalized trace-free oper is unchanged because scalar conjugation sends every \(\partial+c\) to \(\partial+c-u'/u\). The proof of (CF.8) shows exactly which central coefficients disappear if this gauge quotient is taken.

These results establish the regular algebraic reductive vacuum factorization and its framed central coefficient comparison. A statement about intrinsic nonadjoint opers must specify its retained central data, gauge group and torsor descent. Completed punctured-disc centers, central-line geometry in localization, chiral or Poisson structures, Satake compatibility and derived parameter families also retain their separate mathematical requirements.

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

Frenkel's convention in *Lectures on the Langlands program and conformal field theory* is \(-\operatorname{Res}\kappa_0(f,dg)\), equal to our \(+\operatorname{Res}\kappa_0(df,g)\), with critical level \(-2\) in the normalization above. Raskin's *A geometric proof of the Feigin–Frenkel theorem* uses \(+\operatorname{Res}\kappa(f,dg)\), with the central element acting identically and critical form minus half the Killing form. The displayed cocycle directions differ. Section 3.5.3 proves the algebraic comparison of cocycle directions, central-line scalings and scalar actions. The geometric convention of that refinement still requires its own matching identification; changing the central-generator sign alone also changes its scalar action.

The center statement is formulated in Frenkel's [*Lectures on the Langlands program and conformal field theory*, §8.4](https://arxiv.org/abs/hep-th/0512172v1). In the convention of Raskin's [*A geometric proof of the Feigin–Frenkel theorem*, introduction](https://arxiv.org/abs/1106.3112v1), its stronger tensor-compatible Satake assertion is
\[
\Gamma(\operatorname{Gr}_G,\mathcal S_W)
\simeq V^R_{\rm crit}\otimes_{Z^R_{\rm vac}}\mathcal W_{\rm Op},
\tag{K4.2}
\]
where the superscript \(R\) retains that source's vacuum and center convention, \(\mathcal W_{\rm Op}\) comes from the universal dual-group bundle, and \(W\in\operatorname{Rep}(\check G)\). Its proof must construct that universal bundle and compatibility; the formula is not merely an equality of dimensions.

Equations (K4.1)–(K4.2) in their full generality are **not yet proved in this lesson**. Section 3.2 proves (K4.1) for the rank-one vacuum, including all polynomial generators, ordinary base change and coordinate compatibility. The finite-mode, jet-invariant and filtered arguments for \(\mathfrak{sl}_2\) in §3.2 establish the full rank-one polynomial algebra and coordinate action. Section 3.3 proves the general classical current invariants, the PBW upper bound and unconditional vacuum commutativity. The finite-degree reduction to basic lifts and the determinant construction prove the entire type A polynomial vacuum algebra. Section 3.4 proves the full coordinate-equivariant ordinary disc-oper comparison for every type A factor. Basic lifts and the coordinate comparison in other simple types, and the Satake assertion (K4.2), remain unproved. The geometric route through affine Grassmannian global sections, semi-infinite cohomology and the birth of opers needs its complete argument and foundations. These classical statements are over \(\mathbb C\). The rank-one vacuum-center proof in §3.2 holds over the full characteristic-zero field convention and every ordinary parameter algebra. The type A polynomial vacuum algebra in §3.3.5 and its full ordinary coordinate comparison in §3.4 hold over every characteristic-zero field and ordinary parameter algebra. Section 3.5 proves the reductive vacuum factorization and the full framed central coefficient comparison for type A reductive Lie algebras. The full center/oper comparison in other simple types and the intrinsic/global central-data comparison, as well as the completed, chiral, Poisson, Satake and derived-family center comparisons, remain unproved.

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

The adjoint-semisimple argument proves the finite principal decomposition, unique ordinary-family gauge, coordinate cocycle, intrinsic oper classification, global affine parameter space and dimension from its explicit Lie/group and curve premises. It constructs regular and Laurent coefficient functors, including the continuous coordinate action over nilpotent bases. The independent scalar argument supplies intrinsic/scalar equivalence, normalized lifts, theta choices, ordinary-family representability, Schwarzian, nonsplit extension and algebraic irreducibility. The invariant-ring argument supplies characteristic-zero field transfer, arbitrary ordinary coaction base change, the Molien degree identities, a weighted polynomial Kostant section and the graded classical oper/Hitchin ring. The critical argument supplies the ordered basis, formal affine action, invariant/end correspondence and every-mode \(\mathfrak{sl}_2\) check. Section 3.2 proves the full rank-one polynomial vacuum center, current-jet invariant algebra, PBW exhaustion and coordinate-equivariant ordinary projective-connection identification. Section 3.3 proves the general classical current invariants, exact PBW upper bound, ordinary vacuum-invariant base change, coordinate action on symbols and unconditional vacuum commutativity. Its basic-lift reduction and all-n determinant construction prove the entire type A polynomial vacuum algebra over every ordinary parameter algebra. Section 3.4 proves the full ordinary coordinate-equivariant type A disc-oper comparison and the arbitrary-type quadratic coordinate law, with every anomaly and normalization retained. Section 3.5 proves reductive affine-vacuum factorization, all abelian invariants at arbitrary affine form, the trace splitting and whole polynomial vacuum algebra in reductive type A, and their exact framed central coordinate laws. It also proves the ordinary central gauge groupoid and the algebraic cocycle comparison.

Complete proofs remain required for the recursive root-space/pinning, split-unipotent and faithful adjoint-group constructions, ordinary bundle descent, and the recursive Serre/highest-weight and finite-algebra foundations of the invariant-ring proof; non-type-A basic quantum lifts and the non-type-A coordinate-equivariant vacuum-center/oper comparison, completed punctured-disc center, chiral/Poisson/Satake and derived-family compatibility, and the geometric/Satake/global central-convention comparison; half-root, uniformization, localization, nonzero specialization, holonomicity, tensor/fusion Hecke property and filtered quantization; full derived opers and full-field/reductive-center passages; and the critical FLE, Ran, factorization, determinant, convergence and \(\operatorname{IndCoh}^{*}/\operatorname{IndCoh}^{!}\) foundations. The fixed-curve Picard/coherent/local-algebra/Ext chains, bundle-stack algebraization and optional analytic comparison retain their explicit earlier unproved foundations. Each is a mathematical theorem or construction whose full proof is still required.

Further reading: [Frenkel, *Lectures on the Langlands program and conformal field theory*, §§8–9](https://arxiv.org/abs/hep-th/0512172v1); [Raskin, *A geometric proof of the Feigin–Frenkel theorem*, introduction](https://arxiv.org/abs/1106.3112v1); [Frenkel–Gaitsgory, *Local geometric Langlands correspondence and affine Kac-Moody algebras*, introduction](https://arxiv.org/abs/math/0508382v3); [Beilinson–Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, §§2.6, 3, 7.8 and 7.14](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf); and [Arinkin, Beraldo, Campbell, Chen, Faergeman, Gaitsgory, Lin, Raskin and Rozenblyum, *Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE*, introduction and §3](https://arxiv.org/abs/2405.03648v3).

# Opers, critical level and the Beilinson–Drinfeld construction

*Draft. Self-checked by the writing AI. Original mathematical exposition: CC0 1.0.*

An oper is a connection with a maximally transverse Borel reduction. The reduction produces scalar differential equations and gives concrete affine families of local systems. At critical level, an affine Lie algebra's center is described by functions on opers. Localization assigns to a global oper a system of differential equations on the bundle stack with a tensor-compatible Hecke eigenproperty.

We construct the adjoint-semisimple principal slice, prove its unique gauge normal form in ordinary families, and derive the coordinate action and global affine oper space. We also prove the homogeneous invariant ring over the stated characteristic-zero field, identify its degrees with the principal heights and construct the weighted Kostant section. A separate scalar proof treats \(PGL_n\) through jets. We also prove the Schwarzian rule, algebraic \(PGL_2\) irreducibility and the critical \(\mathfrak{sl}_2\) invariant. Section 3.2 extends that calculation to the entire rank-one polynomial vacuum center and its coordinate-equivariant ordinary disc-oper comparison. Section 3.3 proves the general current-jet invariant algebra, PBW symbol bound, ordinary-family base change and vacuum commutativity; it constructs every basic type A lift and proves the whole type A polynomial vacuum algebra. Section 3.4 proves the exact quantum coordinate laws and the coordinate-equivariant ordinary disc-oper comparison for every type A factor, including nilpotent parameter families. Section 3.5 proves reductive vacuum factorization, the whole type A reductive polynomial algebra and its framed central coefficient comparison, and the exact algebraic distinction between central frames and gauges. Section 3.6 constructs the smooth affine completion, proves its full type A center and ordinary punctured-disc coordinate comparison, and computes the complete abelian center at every fixed form. Section 3.7 constructs the intrinsic critical Poisson vertex structure and jointly continuous completed bracket for every finite-dimensional affine datum, proves the ordered Miura injection and its actual type A affine-to-boson Poisson comparison, and identifies the full type A oper Poisson bracket. Section 3.8 constructs the ordinary principal matrix Hamiltonian reduction in type A, proves its regular-jet and Laurent gauge quotients and actual classical Miura reduction, and identifies its complete scalar Adler bracket and coordinate action. Section 3.9 proves the ordinary principal classical reduction for the general specified graded semisimple datum: its affine PVA normalizer, polynomial regular-jet invariants, cofinal full Laurent quotient, all-mode reduced Poisson bracket and full ordinary coordinate action, including the quadratic Virasoro and Schwarzian laws at the chosen invariant form. The quantum-center and center/oper-Poisson comparison in other types, exact dual-form normalization, derived/global reduction, localization, quantization and fundamental local equivalence remain unproved; their precise statements below retain their complete scope.

The classical calculations use a fixed smooth projective connected curve over an algebraically closed characteristic-zero field, \(g\ge2\). The regular singular example separately uses the punctured projective line. The classical center and eigenobject statements in §§4–5 have their stated complex semisimple or simply connected hypotheses. The type A center, Poisson and framed reductive coefficient comparisons in §§3.3–3.8, and the general principal classical reduction at its fixed structural data in §3.9, hold over every characteristic-zero field and ordinary coefficient algebra at their stated foundations. The full eigenobject theorem and intrinsic/global reductive extensions remain unproved. Connections are algebraic de Rham connections; localization uses left D-modules. Ordinary-family assertions concern the fixed curve. Analytic comparisons and full derived moduli retain separate foundations.

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

The result just proved is a vacuum invariant and its corresponding endomorphism. A claim that all normally ordered Fourier coefficients are central in a completed enveloping algebra also requires the completion, vertex operations and their compatibility. Section 3.2 supplies all quadratic mode operators, their commutativity and the full rank-one vacuum-center proof. Section 3.6 proves completed centrality and the full type A completed center. Section 3.7 supplies the intrinsic critical Poisson vertex structure and completed bracket, and the full type A oper-Poisson comparison. Chiral/factorization compatibility and quantum lifting in other types retain their separate proof obligations.


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
for every ordinary parameter algebra, with the exact current cocycle and scalar-oper convention of this lesson. The proof supplies all generators, their independence, exhaustion and coordinate action. Sections 3.3–3.7 supply the type A basic lifts, polynomial and completed centers, intrinsic critical Poisson structures and full scalar-oper Poisson comparison. Basic lifting and the full center/oper-Poisson comparison in other types, derived/global Hamiltonian reduction, chiral/factorization, Satake and derived-family compatibility remain the additional scopes of §4.


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
[x(s),y(z)]=[x,y](z)\delta(s,z)
+\ell B(x,y)\partial_z\delta(s,z).
\tag{VC.11}
\]
Indeed its \(s^{-m-1}\) coefficient is
\(z^m[x,y](z)+m\ell B(x,y)z^{m-1}\). Shifting indices gives
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

The general basic-lift hypothesis remains open for the other simple types; §3.3.5 supplies the full list for every type A factor. Once such lifts are supplied, the written argument proves the whole polynomial vacuum algebra and its ordinary coefficient extensions. Section 3.6 proves the full type A completed punctured-disc center and its ordinary coordinate action. Section 3.7 supplies the intrinsic critical Poisson structures in every finite-dimensional affine datum and the full type A oper-Poisson comparison. The completed center and oper-Poisson comparison in other types, derived/global Hamiltonian reduction, full chiral/factorization structures, Satake compatibility, derived parameter families and geometric central-convention comparison retain their separate proof obligations in §4.

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

For a direct sum of type A factors, the critical bracket has no cross-factor terms. A basic lift from one factor, with the vacuum in every other factor, is invariant for the entire sum. Its symbol is the corresponding basic polynomial of that factor. Thus the same general reduction proves (SL.C1) with the concatenated lists of generators. The zero Lie algebra gives the coefficient ring. Section 3.4 proves the full quantum coordinate law and ordinary oper comparison for these type A factors. Section 3.6 proves the type A completed center and its punctured-disc comparison. Section 3.7 supplies the intrinsic critical Poisson structures and the full type A scalar-oper Poisson comparison. Basic lifting and the full coordinate and oper-Poisson comparison in other simple types, their completed center, and derived/global Hamiltonian reduction, chiral/factorization, Satake and derived comparisons remain separate proof obligations.


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

These are complete algebraic coordinate formulas for the ordinary scalar-oper coefficient functor. Their identification with intrinsic opers uses the finite-jet, vector-lift and ordinary bundle-descent inputs specified in §§2.2–2.6. The recursive global curve/Picard foundations in §2.1 and the bundle-algebraization foundation in §2.8 remain unproved in their stated global uses. No such global theorem is needed for the coefficient recursion or its ordinary base change. The coefficients here are those of the scalar differential operator (SC.O1); Section 3.4.3 compares these coefficients with the quantum determinant generators. Sections 3.6–3.7 supply the smooth completed center in type A, the intrinsic critical Poisson structures and the full type A scalar-oper Poisson comparison. Completed centers and oper-Poisson comparison in other types, derived/global Hamiltonian reduction, chiral/factorization and derived parameter spaces retain their separate mathematical requirements.

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
is therefore an algebra isomorphism, with the specified determinant normalization. Equations (SL.X18)–(SL.X24) and the integration argument prove its coordinate equivariance over every ordinary parameter algebra. Products of type-A factors are handled componentwise. This establishes the type-A ordinary formal-disc coordinate comparison at the previously stated scalar-oper and invariant-theory foundations. Sections 3.6–3.7 prove the type A punctured-disc completed center and its full scalar-oper Poisson comparison; the regular comparison is a Poisson vertex comparison. Ordinary principal Hamiltonian reduction in other types and derived/global reduction, chiral/factorization, Satake and derived-family compatibility, and basic lifting and full coordinate/oper-Poisson identification in other types retain their separate proof obligations.

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

A general continuous substitution is a nilpotent translation composed with a pointed substitution; factor its pointed linear coefficient as the scaling just treated. Equality for these factors proves the assertion for the entire ordinary continuous coordinate group, including nonreduced \(R\). Section 3.6 supplies the completed type A punctured-disc center, and §3.7 supplies its full coordinate-equivariant scalar-oper Poisson comparison. Derived parameter algebras and a full chiral/factorization construction retain their separate proof obligations.

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

For products of type A factors, use the factor generators and scalar oper operators. Cross-factor currents commute and the critical form is their direct sum. The proved polynomial algebra (SL.C1), the coordinate laws and the map (TC.A9) therefore give the product comparison as well. The proof concerns the regular algebraic vacuum algebra and the ordinary disc-oper coefficient functor. Section 3.5 supplies reductive vacuum factorization and the framed central coefficient comparison. Section 3.6 proves the full smooth completed type A center and its punctured-disc coefficient and coordinate comparison. Section 3.7 supplies the intrinsic critical Poisson structures and the full type A oper-Poisson comparison. Non-type-A basic lifting, full coordinate/oper-Poisson comparison and completed center, derived/global Hamiltonian reduction, chiral/factorization/Satake compatibility, full derived families and intrinsic nonadjoint/global central conventions retain their separate proof obligations.


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

This proves the reductive algebraic vacuum factorization for every fixed invariant form and every ordinary coefficient extension. At critical level it adjoins one free divided-translation family for each central direction, equivariantly with its inverse one-form action. It does not identify this coefficient space with the full intrinsic oper stack of a nonadjoint reductive group. Central bundles and their automorphisms, finite central-isogeny choices, the dual-group central convention, and any global or derived descent comparison retain their own geometric premises. Section 3.6 proves the completed type A and abelian centers. Full non-type-A basic lifting, coordinate comparison and completed center, chiral/Poisson/Satake/derived comparisons and the other theorem obligations remain required.

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
scalar operator plus a framed central one-form. Sections 3.6–3.7 supply the completed type A centre and its full framed scalar coefficient Poisson comparison. Global nonadjoint bundle conventions, derived/global Hamiltonian reduction, chiral/factorization structures and derived coefficient algebras require their separate arguments.

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

These results establish the regular algebraic reductive vacuum factorization and its framed central coefficient comparison. A statement about intrinsic nonadjoint opers must specify its retained central data, gauge group and torsor descent. Section 3.6 supplies the full completed type A center and ordinary punctured-disc comparison. Section 3.7 supplies the intrinsic critical Poisson structures and the full type A framed scalar coefficient comparison. The completed center and oper-Poisson comparison in other types, central-line geometry in localization, derived/global Hamiltonian reduction, chiral/factorization structures, Satake compatibility and derived parameter families retain their separate mathematical requirements.


### 3.6. Smooth affine completion and punctured-disc centers

#### 3.6.1. The affine completion through its smooth modules

Let \(k\) be a characteristic-zero field, let \(\mathfrak g\) be a finite-dimensional \(k\)-Lie algebra, and fix an invariant symmetric form \(\kappa\). No nondegeneracy or reductivity is needed in this subsection. Write \(\widehat{\mathfrak g}_{\kappa,\mathrm{pol}}\) for the central extension of \(\mathfrak g[t,t^{-1}]\) with
\[
[x_m,y_j]=[x,y]_{m+j}
 +m\kappa(x,y)\delta_{m+j,0}K,
\qquad [K,x_m]=0.
\]
For an ordinary commutative \(k\)-algebra \(R\), extend this fixed form and set
\[
\begin{gathered}
A_R=U_R(\widehat{\mathfrak g}_{\kappa,\mathrm{pol},R})/(K-1),\\
\mathfrak q_{N,R}=t^N\mathfrak g_R[t],
\qquad
I_{N,R}=A_R\mathfrak q_{N,R},
\qquad
M_{N,R}=A_R/I_{N,R},
\qquad N\geq1.
\end{gathered}
\tag{CW.1}
\]
Thus the enveloping algebra in (CW.1) includes the affine central extension before the scalar relation \(K=1\) is imposed. The ideals \(I_{N,R}\) are left ideals. The quotients \(M_{N,R}\) are left modules, and their distinguished vectors are \(\xi_N=1+I_{N,R}\).

**PBW quotients and separation.** The complete ordered-word proof in §3 of [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), preceding (K2.3), applies to this bracket. Its reduction of inverted pairs terminates; disjoint reductions commute, and the overlapping three-letter ambiguity is exactly Jacobi. Hence ordered monomials are independent as well as spanning. Put \(K\) first, then all negative modes, then the nonnegative modes in increasing mode index, using a fixed finite basis of \(\mathfrak g\) at each index. The negative block can be well ordered as \(-1,-2,\ldots\). Removing the central powers by \(K=1\) gives an \(R\)-basis of \(A_R\) consisting of the ordered current-mode monomials.

For fixed \(N\), all basis modes with index at least \(N\) form the last block. That block is a Lie subalgebra: its bracket has index at least \(2N\), and has no scalar term. A monomial containing this block ends in one of its generators, and therefore belongs to \(I_{N,R}\). Conversely, multiplying an ordered monomial by a high generator on the right requires reordering only the final high block. Each of its bracket terms still contains a high generator. Thus \(I_{N,R}\) is exactly the span of ordered monomials containing at least one mode of index at least \(N\). Consequently
\[
M_{N,R}\text{ has the ordered-monomial basis whose every mode index is }<N.
\tag{CW.2}
\]
The transition \(M_{L,R}\to M_{N,R}\), \(L\geq N\), retains these basis monomials and kills those containing an index at least \(N\).

Every element of \(A_R\) is a finite sum of finite words. Choose \(N\) larger than every nonnegative index occurring in its ordered normal form. Every nonzero coefficient then survives in (CW.2). Therefore
\[
\bigcap_{N\geq1}I_{N,R}=0.
\tag{CW.3}
\]
This proves separation directly over \(R\), including rings with nilpotents.

One cannot multiply arbitrary quotient classes as if \(M_{N,R}\) were an algebra. For instance, take a one-dimensional abelian Lie algebra with generator \(z\), \(\kappa(z,z)=1\), and \(R=k\). Then \(z_N\in I_N\), but
\[
z_Nz_{-N}=z_{-N}z_N+N,
\qquad
z_Nz_{-N}+I_N=N+I_N\ne0 .
\tag{CW.4}
\]
Here \(z_{-N}z_N\in I_N\), and the constant survives by (CW.2). Thus the left ideal is not a right ideal in this example.

**A uniform bound for each finite word.** A smooth \(A_R\)-module means a module in which, for every vector \(w\), some \(N\geq1\) satisfies
\(\mathfrak q_{N,R}w=0\). This bound can depend on \(w\). For a finite current word
\[
c=y^{(1)}_{p_1}\cdots y^{(a)}_{p_a},
\qquad
d(c)=\sum_{i=1}^a\max(-p_i,0),
\]
commuting \(x_m\) to the right through \(c\) produces current terms whose indices are \(m\) plus sums of subsets of the \(p_i\). If
\[
m\geq N+d(c),
\]
every such index is at least \(N\). A scalar contraction would require an intermediate index sum to be zero; the same bound makes every such sum at least \(N\geq1\), so it cannot occur. The current eventually reaching the right kills \(\xi_N\). Hence
\[
\mathfrak q_{N+d(c),R}\,c\xi_N=0,
\qquad
I_{N+d(c),R}\,c\subset I_{N,R}.
\tag{CW.5}
\]
The second assertion follows by applying its left side to \(\xi_N\). The first applies to every basis current and hence to their finite sums. For a finite linear combination of words, take the largest of these bounds. This proves both that every \(M_{N,R}\) is smooth and that right multiplication by every element of \(A_R\) is continuous for the neighborhoods \(I_{N,R}\). Left multiplication is continuous because the neighborhoods are left ideals.

These smooth modules also carry formal Laurent currents. On a vector killed by modes of index at least \(N\), a series with finite negative part acts through its finitely many terms of index less than \(N\). To verify its bracket, choose a common truncation for the vector, its images under the two series, and the brackets with either finite negative part. Make the truncation larger than the annihilation bounds plus the absolute values of all their negative indices. Both compositions then have the same finite polynomial-current truncations; brackets involving omitted tails still have indices above the annihilation bound. Scalar residue contractions have only finitely many matching indices, all retained in that truncation. The polynomial bracket identity therefore proves the formal bracket identity. This is the common-tail argument of §3 with the bound (CW.5), rather than an assumption that the \(M_{N,R}\) satisfy the stronger vacuum relations.

**The underlying completion and its action.** Define the complete \(R\)-module
\[
\widehat A_R=\varprojlim_{N\geq1}M_{N,R},
\qquad
J_{N,R}=\ker(\widehat A_R\to M_{N,R}).
\tag{CW.6}
\]
The projections and neighborhoods here are projections of modules. Equation (CW.3) embeds \(A_R\) in this inverse limit. Its image is dense: a representative \(a_N\in A_R\) of the \(N\)-th component of \(u\) agrees with \(u\) in every smaller quotient. Such representatives, indexed by \(N\), converge to \(u\). Also \(J_{N,R}\) is the closure of \(I_{N,R}\). Indeed an element of \(J_{N,R}\) has representatives in \(I_{N,R}\) in every quotient of index at least \(N\), by compatibility. The limit is complete: a Cauchy net has an eventually constant image in each discrete quotient \(M_{N,R}\); these images are compatible and define its unique limit. Separation follows from its embedding in the product of these quotients.

Let \(V\) be any smooth \(A_R\)-module and let \(w\in V\) be killed by \(\mathfrak q_{N,R}\). For \(u=(u_L)_L\in\widehat A_R\), choose an \(A_R\)-representative \(a_N\) of \(u_N\) and define
\[
u_Vw=a_Nw .
\tag{CW.7}
\]
Changing the representative adds an element of \(I_{N,R}\), whose final high current kills \(w\). Choosing a larger valid bound changes the representative by an element of the same \(I_{N,R}\), and has the same effect. Two possible bounds are compared through their maximum. Thus (CW.7) is well defined, is \(R\)-linear, and extends the original \(A_R\)-action. In checking additivity, choose a common bound for the finitely many vectors involved. For fixed \(w\), evaluation \(u\mapsto u_Vw\) is continuous with its discrete target, since \(J_{N,R}\) kills \(w\).

If \(f:V\to V'\) is an \(A_R\)-linear map, the same annihilation bound is valid for \(f(w)\), and
\[
f(u_Vw)=u_{V'}f(w).
\tag{CW.8}
\]
Thus these operators are natural on the category of smooth modules. They are faithful as a family: on \(M_{N,R}\),
\[
u_{M_{N,R}}\xi_N=u_N.
\tag{CW.9}
\]
An element acting as zero on all these distinguished vectors has every component zero.

There is also a precise reconstruction statement. Suppose \(\eta_V:V\to V\) is a family of \(R\)-linear operators natural for all \(A_R\)-linear maps between smooth modules. Its values
\(\eta_{M_{N,R}}\xi_N\) are compatible under the quotient maps, and therefore define \(u\in\widehat A_R\). For a vector \(w\in V\) with bound \(N\), the map
\[
f_w:M_{N,R}\to V,\qquad a\xi_N\mapsto aw
\]
is well defined and \(A_R\)-linear. Naturality gives
\[
\eta_Vw=f_w(\eta_{M_{N,R}}\xi_N)=u_Vw .
\tag{CW.10}
\]
Equations (CW.9)–(CW.10) prove uniqueness and existence of the reconstruction. Naturality here concerns \(R\)-linear operators on the underlying modules; these operators themselves need not be \(A_R\)-linear.

**Multiplication by composition.** The composite of two such natural families is again natural. Reconstruction consequently defines a unique product \(ab\in\widehat A_R\) by
\[
(ab)_V=a_V\circ b_V\quad\text{on every smooth }V.
\tag{CW.11}
\]
This constructs multiplication in the inverse limit. It does not multiply classes in \(A_R/I_{N,R}\). More explicitly, the vector \(b_N=b_{M_{N,R}}\xi_N\) is an actual finite element of the smooth module \(M_{N,R}\). Choose an annihilation bound \(L\) for that vector, and an \(A_R\)-representative \(\widetilde a_L\) of \(a_L\). Then
\[
(ab)_N=\widetilde a_L\,b_N
\quad\text{in the left module }M_{N,R}.
\tag{CW.12}
\]
The action (CW.7) proves independence of both choices. Naturality under \(M_{N',R}\to M_{N,R}\) proves compatibility of these components. Formula (CW.10) shows that the resulting element acts by the composite on every smooth module, not only on the universal ones.

Composition proves associativity; addition and \(R\)-scalar multiplication prove bilinearity; the identity family gives the unit represented by \(1\). Faithfulness in (CW.9) transfers these identities from families to elements. For elements of \(A_R\), the composite is their usual product on every module, so the dense embedding \(A_R\to\widehat A_R\) is an algebra map. Thus every smooth module has an actual unital \(\widehat A_R\)-action.

This multiplication is jointly continuous. First, \(J_{N,R}\) is a left ideal: if \(d\in J_{N,R}\), then \((ad)_{M_{N,R}}\xi_N=a_{M_{N,R}}0=0\). For fixed \(b\), the vector \(b_N\) has some annihilation bound \(L\); every \(d\in J_{L,R}\) kills that vector, so
\[
\widehat A_R J_{N,R}\subset J_{N,R},
\qquad
J_{L,R}b\subset J_{N,R}.
\tag{CW.13}
\]
The second bound can depend on \(b\) and \(N\). For perturbations \(d\in J_{L,R}\), \(e\in J_{N,R}\),
\[
(a+d)(b+e)-ab=db+(a+d)e\in J_{N,R}.
\tag{CW.14}
\]
This proves joint continuity at \((a,b)\); it also proves right multiplication continuity for every completed element. The topology is therefore a complete separated linear topology on a unital algebra, despite its defining quotients being only left modules.

Write \(\mathcal N_R\) for the algebra of natural \(R\)-linear operators on smooth modules reconstructed in (CW.7)–(CW.10). The product mechanism is:
\[
\begin{array}{ccc}
\widehat A_R\times\widehat A_R
&\xrightarrow{\quad(a,b)\mapsto ab\quad}&\widehat A_R\\
\big\downarrow &&\big\downarrow\\
\mathcal N_R^2
&\xrightarrow{\quad\text{composition}\quad}&
\mathcal N_R.
\end{array}
\tag{CW.15}
\]
*The vertical maps are (CW.7)–(CW.10). Universal smooth modules reconstruct the upper product from the lower composite; (CW.12) computes a quotient component after choosing a bound for the intermediate vector.*

**The center and the same-bound argument.** Polynomial currents generate \(A_R\) as an algebra. We claim
\[
Z(\widehat A_R)
=\{u\in\widehat A_R:[u,x_m]=0
       \text{ for all }x\in\mathfrak g_R,\ m\in\mathbf Z\}.
\tag{CW.16}
\]
One inclusion is immediate. For the reverse inclusion, \(u_V\) commutes with every polynomial-current operator and their finite products on every smooth module, by (CW.11). If \(\mathfrak q_{N,R}w=0\), then
\[
x_m u_Vw=u_Vx_mw=0\quad(m\geq N).
\tag{CW.17}
\]
The vector \(u_Vw\) has the same annihilation bound as \(w\). For an arbitrary \(b\in\widehat A_R\), choose one representative \(\widetilde b_N\in A_R\) of \(b_N\). It computes both \(b_Vw\) and \(b_Vu_Vw\). Hence
\[
u_V b_Vw
=u_V\widetilde b_Nw
=\widetilde b_Nu_Vw
=b_Vu_Vw .
\tag{CW.18}
\]
This holds on every smooth module and vector. Faithfulness of the universal modules gives \([u,b]=0\), proving (CW.16). In particular a current-commuting completed element commutes with every completed element.

Formal Laurent currents are themselves elements of \(\widehat A_R\): take their finite negative part and truncate the positive part at index \(N\) in the \(N\)-th quotient. Their components are compatible, and their completed action is the common-tail action already proved. The same bound in (CW.17) permits \(u_V\) to pass through their finite truncation on \(w\). Thus polynomial-current commutation, formal-current commutation, and membership in the completed center are equivalent. This characterization does not infer centrality in the completion merely from being a vacuum endomorphism. The theorem (VC.17)–(VC.20) proves the latter commutation on the vacuum; the present criterion tests every universal smooth module.

**Coefficient extension and coordinate independence.** The PBW bases in (CW.2) give, for every ordinary \(R\),
\[
A_R/I_{N,R}=R\otimes_k(A_k/I_{N,k}),
\qquad
\widehat A_R
=\varprojlim_N R\otimes_k(A_k/I_{N,k}).
\tag{CW.19}
\]
This is the completed coefficient extension \(\widehat A_k\widehat\otimes_kR\), defined by the displayed quotients. The ordinary tensor product \(R\otimes_k\widehat A_k\) need not be the completion. For example, take \(\mathfrak g=kz\), \(\kappa=0\), \(R=k[s]\). The series
\[
u=\sum_{j\geq1}s^j z_j
\tag{CW.20}
\]
defines a completed element because its image modulo \(I_{N,R}\) has only \(j<N\). It cannot come from a finite sum \(\sum_{i=1}^a r_i(s)\otimes u_i\). In such a sum the coefficients of every individual linear mode \(z_j\), extracted in a quotient with \(N>j\), belong to the finite-dimensional \(k\)-span of the \(r_i(s)\). The coefficients \(s^j\) in (CW.20) are linearly independent over \(k\), a contradiction.

For \(R\to R'\), stagewise tensoring of (CW.19) identifies
\[
R'\widehat\otimes_R\widehat A_R
:=\varprojlim_N R'\otimes_R(A_R/I_{N,R})
=\widehat A_{R'} .
\tag{CW.21}
\]
Its products are the products just constructed over \(R'\). The coefficient map on the dense polynomial-current algebra is an algebra homomorphism and preserves every high-current ideal. Its stagewise extension is continuous. Approximation by that dense algebra and joint multiplication continuity prove that the extension is multiplicative. This uses the actual free PBW quotients and actions over the new coefficient ring.

Let \(\phi(t)=a_0+a_1t+\cdots\) be a continuous coordinate over \(R\), with \(a_0^\nu=0\) and \(a_1\) a unit. Its inverse and coefficient-finite Laurent substitutions are constructed in §1.1.8. For \(m\geq N+\nu-1\), any term of degree less than \(N\) in \(\phi(t)^m\) uses at least \(\nu\) constant factors. Thus
\[
\phi(t)^m\in t^NR[[t]]
\quad(m\geq N+\nu-1).
\tag{CW.22}
\]
The inverse satisfies the same assertion with its own nilpotence bound. This is the required cofinality of the high-current neighborhoods; there is no requirement that the coordinate fix \(0\) exactly.

The residue identity (RC.C7), with its full monomial proof, shows that substitution preserves the affine bracket and the relation \(K=1\). Sending \(x_m\) to the completed formal current \(x\phi(t)^m\) therefore defines an algebra map
\(\sigma_\phi:A_R\to\widehat A_R\). Equation (CW.22) gives
\[
\sigma_\phi(I_{N+\nu-1,R})\subset J_{N,R}.
\tag{CW.23}
\]
Indeed the substituted final high generator kills \(\xi_N\), and left multiplication by a completed element preserves \(J_{N,R}\). Hence \(\sigma_\phi\) is continuous, extends uniquely to the completion, and sends \(J_{N+\nu-1,R}\) into \(J_{N,R}\). The extension can be constructed by limits of representatives from (CW.6); independence follows from (CW.23). Completeness supplies these limits. Joint multiplication continuity proves that the extension is an algebra map. The inverse substitution gives its inverse: the two composites are identity on the current generators and then on the dense algebra \(A_R\), and continuity extends that equality. Consequently the algebra and its center have their full ordinary coordinate action, including nilpotent coordinate constants.

These constructions establish the topology, multiplication and center criterion of the completed affine enveloping algebra. A presentation of the completed semisimple center, its comparison with punctured-disc opers and its chiral or derived interpretation requires further proofs.

#### 3.6.2. Universal current fields and critical modes on smooth modules

Let \(k\) have characteristic zero, \(R\) be any ordinary commutative \(k\)-algebra, and \(\mathfrak g_R=R\otimes_k\mathfrak g\), with \(\mathfrak g\) finite-dimensional. Fix an invariant symmetric form \(\kappa\), without a nondegeneracy assumption. Use
\[
 [x_m,y_q]=[x,y]_{m+q}
                  +m\kappa(x,y)\delta_{m+q,0}\,1.
 \tag{UC.1}
\]
Let \(A_R\) be the polynomial-mode enveloping algebra at this fixed central level. A smooth \(A_R\)-module \(M\) means that every \(\mu\in M\) is killed by all \(x_m\), for all \(x\), when \(m\) is sufficiently large. No vacuum, cyclicity, energy grading or translation operator on \(M\) is assumed. The induced vacuum \(V_{\kappa,R}\), with its state translation \(T\), remains the source of the state-field map.

**Normal reconstruction and the relations it must respect.** A field on \(M\) is a series \(F(z)=\sum_qF_{(q)}z^{-q-1}\) with \(F(z)\mu\in M((z))\) for every \(\mu\). Currents are fields by smoothness. Write
\[
 \begin{aligned}
 x(z)&=\sum_{m\in\mathbb Z}x_mz^{-m-1},&
 x^{[r]}&=\frac{\partial_z^{r-1}x(z)}{(r-1)!},\\
 x^{[r]}_-&=\sum_{s\geq0}\binom{r+s-1}{r-1}x_{-r-s}z^s,&
 x^{[r]}_+&=(-1)^{r-1}\sum_{p\geq0}
                  \binom{r+p-1}{r-1}x_pz^{-r-p}.
 \end{aligned}
 \tag{UC.2}
\]
Define an operator on the space of fields by
\[
 L_{x,r}F=x^{[r]}_-F+Fx^{[r]}_+,\qquad r\geq1.
 \tag{UC.3}
\]
This is a field. In the second term only finitely many positive modes act on a fixed input. In the first, a fixed coefficient uses only finitely many nonnegative powers of \(x^{[r]}_-\), because \(F(z)\mu\) has a lower Laurent bound. In any fixed iterated product, choose its finitely many minus/plus alternatives. Each alternative has a negative-mode block on the left and a nonnegative-mode block on the right. The right block acts through a finite tree of intermediate states and finite smoothness bounds. The left block then has only finitely many terms at a fixed coefficient. The same argument gives a common cutoff for any specified finite list of input and intermediate states.

The negative-mode operators satisfy
\[
 [L_{x,r},L_{y,s}]=L_{[x,y],r+s}.
 \tag{UC.4}
\]
Indeed left and right multiplication commute, so the commutator on \(F\) is
\([x^{[r]}_-,y^{[s]}_-]F-F[x^{[r]}_+,y^{[s]}_+]\).
There is no affine scalar in either bracket: negative indices cannot sum to zero, and two nonnegative indices can do so only at index zero, with zero cocycle coefficient. The convolution of the two binomial expansions in (UC.2), obtained by multiplying \((1-u)^{-r}\) and \((1-u)^{-s}\), gives respectively
\([x,y]^{[r+s]}_-\) and \(-[x,y]^{[r+s]}_+\).
This proves (UC.4) with the common finite cutoffs just described. It is exactly the negative-current enveloping relation, on every \(M\).

Thus PBW and the negative-current enveloping universal property define
\[
 Y_M(v,z)=\operatorname{Id}_M,\qquad
 Y_M(x_{-r}u,z)=L_{x,r}Y_M(u,z).
 \tag{UC.5}
\]
This map is independent of every ordered-word representative, including bracket replacements inside a longer word. It is not merely a choice of fields for PBW basis vectors. The calculation proving (UC.4) on the vacuum in §3.3.3 used only current brackets and field truncation; these have now been checked directly on arbitrary smooth \(M\).

**The missing universal current-product identification.** We give the additional argument needed when the target has no cyclic vacuum. For \(j\geq0\), define the finite polynomial operator
\[
 X^x_j(z)=\sum_{i=0}^j\binom ji(-z)^{j-i}x_i,\qquad
 \rho(x_j)F=[X^x_j(z),F(z)],
 \qquad
 \rho(x_{-r})F=L_{x,r}F.
 \tag{UC.6}
\]
We will prove that \(\rho\) is an affine representation on the space of fields, at precisely the form \(\kappa\).

The mixed bracket is the substantive step. Put \(b=[x,a]\), and \(B_q(z)=X^b_q(z)\) for \(q\geq0\). Direct expansion of (UC.2) gives
\[
 \begin{array}{c|c|c}
 & [X^x_j,a^{[r]}_-]&[X^x_j,a^{[r]}_+]\\ \hline
 0\leq j<r& b^{[r-j]}_-&b^{[r-j]}_+\\
 j\geq r&B_{j-r}+r\kappa(x,a)\delta_{j,r}&-B_{j-r}.
 \end{array}
 \tag{UC.7}
\]
Here are complete coefficient checks for this boundary identity. For a negative output mode \(b_{-u}\), \(u\geq1\), the coefficient in the minus part, apart from its power \(z^{j-r+u}\), is
\[
 \sum_{i=0}^j(-1)^{j-i}\binom ji
                    \binom{i+u-1}{r-1}
   =\binom{u-1}{r-j-1}.
\]
Repeated finite differences of \(\binom{u+i-1}{r-1}\) prove this equality by Pascal's identity. If \(j\geq r\) it is zero; otherwise it is exactly the coefficient of \(b^{[r-j]}_-\).

For a nonnegative output mode \(b_q\), the minus-part coefficient is
\[
 \sum_{i=r+q}^j(-1)^{j-i}\binom ji
                       \binom{i-q-1}{r-1}
   =(-1)^{j-r-q}\binom{j-r}{q}
 \quad(j\geq r),
 \tag{UC.8}
\]
with zero outside the indicated range. To prove all these finite identities at once, multiply by \(U^rV^q\) and sum over \(r\geq1,q\geq0\). For a fixed \(i\), the inner sum is
\(U((1+U)^i-V^i)/(1+U-V)\). The alternating binomial sum over \(i\) is
\[
 \frac{U(U^j-(V-1)^j)}{1+U-V}
       =\sum_{r=1}^j U^r(V-1)^{j-r}.
\]
The expression is a polynomial; extracting its coefficient proves (UC.8). For the plus part, the generating series of the coefficient at \(b_q\), after its common \(z^{j-r-q}\) is removed, is
\[
 (-1)^{r-1+j}(1-V)^{j-r}.
\]
If \(j<r\), its coefficients give \(b^{[r-j]}_+\); if \(j\geq r\), they give \(-B_{j-r}\). Finally, the only scalar term occurs in the minus part and is
\[
 \kappa(x,a)z^{j-r}
 \sum_{i=r}^j(-1)^{j-i}\binom ji\,i\binom{i-1}{r-1}
 =r\kappa(x,a)\delta_{j,r}.
\]
Use \(i\binom{i-1}{r-1}=r\binom ir\) and the alternating sum
\(\sum_{i=r}^j(-1)^{j-i}\binom{j-r}{i-r}\).
This proves every entry of (UC.7), including the affine boundary term.

Since an adjoint operator obeys the product rule, (UC.7) yields
\[
 [\rho(x_j),\rho(a_{-r})]
   =\rho([x,a]_{j-r})
                 +j\kappa(x,a)\delta_{j,r}\operatorname{Id}
       \quad(j\geq0,r\geq1).
 \tag{UC.9}
\]
For two negative modes use (UC.4). For two nonnegative modes, their operators are finite adjoint sums. Multiplying the two binomial polynomials gives
\([X^x_j,X^a_q]=X^{[x,a]}_{j+q}\); no scalar occurs at nonnegative indices. Thus all affine brackets hold for \(\rho\), with the central generator acting as the identity on fields.

Moreover \(\rho(x_j)\operatorname{Id}_M=0\) for \(j\geq0\). Induction from the defining vacuum, now into this affine representation on fields, therefore proves
\[
 \rho(x_j)Y_M(w,z)=Y_M(x_jw,z)
                  \qquad(j\in\mathbb Z).
 \tag{UC.10}
\]
For negative \(j\) this recovers (UC.5). For nonnegative \(j\) it identifies the actual current products universally. No uniqueness argument using a vacuum in \(M\) occurs.

**Locality and every physical integer current mode.** To pass from (UC.10) to all physical modes \(x_m\), we supply the formal-distribution step. The current bracket is
\[
 [x(s),a(z)]=[x,a](z)\delta(s,z)
                      +\kappa(x,a)\partial_z\delta(s,z),\qquad
 \delta(s,z)=\sum_{m\in\mathbb Z}s^{-m-1}z^m.
 \tag{UC.11}
\]
The identities \((s-z)\delta=0\) and
\((s-z)\partial_z\delta=\delta\) show current locality of order two. A derivative increases a locality order by at most its derivative order.

Here is the finite product closure used for the reconstructed fields. For any integer \(q\), define
\[
 (A_{(q)}B)(z)=\operatorname{Res}_s\!
  \left(\iota_{s,z}(s-z)^qA(s)B(z)
             -\iota_{z,s}(s-z)^qB(z)A(s)\right).
 \tag{UC.12}
\]
For \(q\geq0\) this is a finite polynomial commutator sum. For \(q=-r<0\), the two geometric-series expansions give
\[
 A_{(-r)}B
  =\left(\frac{\partial_z^{r-1}A}{(r-1)!}\right)_-B
       +B\left(\frac{\partial_z^{r-1}A}{(r-1)!}\right)_+.
\]
Thus these products are fields by the same coefficient-finite argument as (UC.3).

If \(A,B,C\) are pairwise local of orders \(a,b,c\) for the pairs
\((A,B),(A,C),(B,C)\), then \(A_{(q)}B\) is local with \(C\).
Put \(p=s-z\), \(v=z-u\), and choose \(L=a+b+c+|q|+1\).
Multiply the commutator of (UC.12) with \(C(u)\) by \(v^L\).
Its factor \(v^c\) permits \(C\) to pass through \(B\).
Expand the remaining factor as
\[
 v^{L-c}=((s-u)-p)^{L-c}.
\]
Terms with at least \(b\) factors \(s-u\) vanish by the \(A,C\) locality relation. In every remaining term the power \(q+L-c-j\) of \(p\) is at least \(a\), so the two expanded kernels become the same polynomial. Their difference is a multiple of
\[
 v^cp^{q+L-c-j}(s-u)^j[[C(u),A(s)],B(z)].
\]
Jacobi rewrites the double bracket as
\([C,[A,B]]-[A,[C,B]]\). The first term is killed by \(p^a\), the second by \(v^c\). This proves closure. When a negative kernel occurs, fix the input and the finitely many third-mode coefficients involved and take common smoothness and field cutoffs before extracting the residue. Thus every comparison is of finite sums of actual operators. Induction from currents and the identity proves locality of all reconstructed fields with every current, and with one another, on every smooth \(M\).

Set \(H(s,z)=[x(s),Y_M(w,z)]\), and choose a locality order \(L\geq1\). Its residues are, by (UC.6) and (UC.10),
\[
 C_j(z)=\operatorname{Res}_s(s-z)^jH(s,z)
       =\rho(x_j)Y_M(w,z)=Y_M(x_jw,z)
             \quad(j\geq0).
 \tag{UC.13}
\]
The finite delta identity is
\[
 H(s,z)=\sum_{j=0}^{L-1}C_j(z)\frac{\partial_z^j\delta(s,z)}{j!}.
\]
For a proof, subtract the right side. Multiplication by \((s-z)^L\) kills the remainder. Its first \(L\) residues against powers of \(s-z\) vanish, so its first \(L\) coefficients as a series in \(s^{-1}\) vanish successively. The relation \((s-z)^LG=0\) is the recurrence
\(\sum_{i=0}^L\binom Li(-z)^{L-i}G_{m+i}=0\).
The leading coefficient is one and the constant coefficient is the invertible Laurent monomial \((-z)^L\). It propagates the zero coefficients in both directions. This proves the delta identity coefficientwise over \(R\).

Finally,
\(\operatorname{Res}_s s^m\partial_z^j\delta/j!
 =\binom mjz^{m-j}\) for every integer \(m\), by differentiating \(z^m\). Therefore
\[
 \boxed{[x_m,Y_M(w,z)]
   =\sum_{j\geq0}\binom mj z^{m-j}Y_M(x_jw,z)
                         \qquad(m\in\mathbb Z).}
 \tag{UC.14}
\]
The upper support is finite, independently of \(m\) and \(M\): a sufficiently high nonnegative current kills the finite-energy source state \(w\). Generalized binomial coefficients include negative \(m\). Formula (UC.14) is proved on every smooth target; it has not been inferred from its action on a cyclic vacuum.

The construction is natural in module maps. Such a map intertwines the current parts and every finite summand of an iterated normal product, proving
\(fY_M(w,z)=Y_{M'}(w,z)f\). It is also compatible with every ordinary coefficient extension \(R\to R'\), and the induced maps of modules and source states. Each coefficient on a specified input uses finite current words and rational constants; tensoring those equalities needs no flatness assumption on \(R'\) over \(R\).

**Critical invariants and their universal Fourier coefficients.** Let \(w_i\) be an actual invariant vacuum state over \(k\), extended to \(R\), homogeneous of energy \(D_i>0\), of PBW length at most \(D_i\), with nonzero degree-\(D_i\) symbol \(p_i\) in the \(-1\) currents. In type A these hypotheses are proved for the raw matrix determinant degrees \(1,\ldots,a\) and traceless degrees \(2,\ldots,a\) in SL.L1–SL.L7; the critical forms retain the exact conventions of that section. In another type, the assertions below are conditional on such actual lifts, without an existence claim.

Write
\[
 Y_M(w_i,z)=\sum_{n\in\mathbb Z}S^M_{i,n}z^{-n-D_i}.
 \tag{UC.15}
\]
Invariance makes the right side of (UC.14) zero, so every \(S^M_{i,n}\) commutes with every physical current mode. It preserves the same current annihilation bound as its input. The finite-tail argument for formal Laurent currents therefore extends this to the full formal affine action. Thus these are natural affine-module endomorphisms on all smooth \(M\). Any such current-commuting operator commutes with every reconstructed field, by induction in (UC.5): commute it through each minus and plus current factor using common cutoffs on the input and its image. Consequently all invariant-field Fourier coefficients commute with one another on every smooth module.

We make their universal completion coefficients explicit. Let
\[
 I_N=A_R(\mathfrak g_R\otimes t^N R[t]),\qquad
 M_N=A_R/I_N,\qquad N\geq1.
\]
These are left ideals and left modules. Their cyclic vectors are the classes of \(1\), not vacuum vectors. PBW, ordering the modes \(m\geq N\) last, makes \(M_N\) free on words in the remaining modes. It is smooth: for any finite word, a mode with index at least \(N\) plus the sum of the absolute values of its negative indices remains at least \(N\) after every relevant bracket and reaches the cyclic vector, where it vanishes; possible scalar brackets are excluded by the same strict positive bound.

For a reconstructed field of finite source energy \(D\), each expanded normal-product term has a negative-mode block followed by a nonnegative-mode block. Modulo \(I_N\), any nonnegative mode of index at least \(N\) can be commuted to the right through that latter block. Every resulting bracket still has index at least \(N\), with no scalar term. Thus the term vanishes modulo \(I_N\). The remaining nonnegative indices lie in the finite interval \(0,\ldots,N-1\). At a fixed field coefficient, the sum of all mode indices is fixed. The remaining negative indices are strictly negative with fixed sum, so they also have only finitely many possibilities. It follows that each coefficient gives a finite class in \(A_R/I_N\). These classes are compatible as \(N\) increases: the newly admitted terms have a positive index at least the smaller \(N\), and vanish in that smaller quotient. We have therefore constructed
\[
 S_{i,n}\in\varprojlim_{N\geq1}A_R/I_N.
 \tag{UC.16}
\]
This is the underlying smooth completion of CW. Its action on any input \(\mu\) killed by modes \(m\geq N\) is evaluation of the finite class (UC.16) on \(\mu\), since the map \(M_N\to M\), \(a+I_N\mapsto a\mu\), is a module map. Thus its universal action is exactly (UC.15). The current-commuting natural operators are central in the smooth completion under the natural-operator identification proved in CW. No cyclic-vacuum test is used to establish that commutation.

For clarity, \(S_{i,n}\in I_N\) in completed notation means that its projection to \(A_R/I_N\) is zero. Write \(\widehat I_N\) for this kernel when distinguishing a completed coefficient from a polynomial element of \(A_R\).

**PBW symbol, mode sum and the sharp smoothness cutoff.** A homogeneous negative word
\(x^1_{-r_1}\cdots x^d_{-r_d}v\) of energy \(D\) has
\(r_a\geq1\) and \(\sum_ar_a=D\). Its reconstructed factors have powers
\(z^{-m_a-r_a}\). Hence every coefficient of weight \(D\), including every lower-length derivative correction, has
\[
 \sum_a m_a=n
 \quad\text{at the coefficient of }z^{-n-D},\qquad d\leq D.
 \tag{UC.17}
\]
A current bracket replaces two indices by their sum. A scalar bracket can occur only when their sum is zero. Thus subsequent reorderings preserve this total mode sum as well. This proves the stated conservation for every PBW representative.

For \(w_i\) of degree and energy \(D_i\), the length-\(D_i\) source words have all \(r_a=1\). Normal ordering becomes ordinary multiplication in the PBW associated graded; reordering corrections have lower length. Let
\[
 \mathcal A(z)=\sum_{m\in\mathbb Z}\mathcal A_mz^{-m-1},
 \qquad B(x,\mathcal A_m)=\sigma(x_m),
\]
For this symbol interpretation assume the chosen nondegenerate pairing \(B\), as in the semisimple or matrix cases, and use it to define the dual-current coordinates. The universal field and commutator arguments themselves did not require such a pairing. For matrices \(B=\operatorname{tr}\) uses the transpose matrix coordinates, which leave the characteristic coefficients unchanged. We obtain the exact leading symbol
\[
 \boxed{\sigma_{D_i}(S_{i,n})
        =[z^{-n-D_i}]\,p_i(\mathcal A(z)).}
 \tag{UC.18}
\]
This is a coefficient in the PBW completion, equivalently a finite polynomial after setting the symbols of modes \(m\geq N\) to zero. In particular the PBW length is at most \(D_i\).

If
\[
 \boxed{n>D_i(N-1),}
 \tag{UC.19}
\]
a term with \(d\leq D_i\) current indices summing to \(n\) must have an index at least \(N\), since otherwise their sum is at most
\(d(N-1)\leq D_i(N-1)\). That index is in the nonnegative block. Moving it right through that block leaves a high nonnegative current in every resulting term, and no scalar bracket. Therefore
\[
 S_{i,n}\in\widehat I_N
                 \quad\text{for }n>D_i(N-1).
 \tag{UC.20}
\]
This proof includes lower derivative terms, because (UC.17) retained their full energy and mode sum.

The sufficient bound is sharp for every nonzero basic symbol. At
\(n=D_i(N-1)\), the degree-\(D_i\) symbol modulo \(I_N\) can reach that sum only if every index equals \(N-1\). Its coefficient is exactly
\(p_i(\mathcal A_{N-1})\), which is nonzero in the free PBW polynomial ring. Hence the boundary mode is nonzero in \(A_R/I_N\) for a nonzero coefficient ring \(R\); the strict inequality cannot be replaced by a weak one. For every integer \(n\), (UC.18) is also nonzero at a sufficiently large quotient. If \(n\ne0\), specialize
\(\mathcal A(z)=a(z^{-1}+u z^{-n-1})\) with \(p_i(a)\ne0\); the term linear in \(u\) at that coefficient is \(D_i p_i(a)\ne0\). Such an \(a\) exists because \(k\) is infinite and \(p_i\) is a nonzero polynomial. For \(n=0\), use \(\mathcal A(z)=az^{-1}\). Taking \(N>\max(n,0)\) retains the required modes. Thus each universal \(S_{i,n}\) has PBW degree exactly \(D_i\), even when it vanishes on the vacuum.

On the vacuum, the already proved creation identity gives the more restrictive statement
\[
 S_{i,n}|_{V_{\kappa,R}}=0\quad(n>-D_i),\qquad
 S_{i,-D_i-r}(v)=\frac{T^rw_i}{r!}\quad(r\geq0).
 \tag{UC.21}
\]
Here creation first identifies the vacuum images, and (UC.14) makes them endomorphisms; cyclicity is used only for this explicitly vacuum-restricted conclusion. It is not used for (UC.14), (UC.16) or (UC.20).

**Universal coordinate-derivation covariance.** The coefficient derivations
\(D_lx_m=mx_{m+l}\), \(l\geq-1\), act on the universal coefficients, rather than as assumed operators on \(M\). Their affine central defect is
\(m(m+q+l)\kappa(x,y)\delta_{m+q+l,0}=0\). They are continuous on the underlying completion: \(D_lI_N\subseteq I_N\) for \(l\geq0\), and \(D_{-1}I_{N+1}\subseteq I_N\). Thus they can be applied to (UC.16) by finite quotient computations.

These computations do not need an assumed action of \(D_l\) on \(M\), or an unproved multiplication of arbitrary completed elements. Left multiplication by a polynomial current is defined on each left quotient. Right multiplication by a nonnegative current also preserves \(I_N\): commuting a high generator \(x_h\), \(h\geq N\), past \(y_q\), \(q\geq0\), leaves either that high generator on the right or the bracket of index \(h+q\geq N\), with no scalar term. Thus the right multiplications in (UC.3) and (UC.6) are defined on the quotient coefficients; right indices at least \(N\) give zero. The minus part is coefficient-finite by the field bound on the class of \(1\) in \(M_N\). The coefficient product rule for \(D_l\) is first applied to finite polynomial representatives and then passed to the quotient, using \(N+1\) when \(D_{-1}\) occurs. This proves the universal coefficient calculus used below directly from (UC.16).

Define the moving-origin coefficient operator
\[
 \mathscr D_l
   =\sum_{s=0}^{l+1}\binom{l+1}{s}(-z)^sD_{l-s}^{\mathrm{coeff}}
       \quad(l\geq0),\qquad
 \mathscr D_{-1}=D_{-1}^{\mathrm{coeff}}.
 \tag{UC.22}
\]
All these operators fix \(z\); they differentiate the completed-current coefficients. We prove their boundary identity directly. Set
\(X_q^x(z)=\sum_{i=0}^q\binom qi(-z)^{q-i}x_i\) for \(q\geq0\). Then
\[
 \begin{array}{c|c|c}
 &\mathscr D_l x^{[r]}_-&\mathscr D_l x^{[r]}_+\\ \hline
 -1\leq l<r&-r x^{[r-l]}_-&-r x^{[r-l]}_+\\
 l\geq r&-rX^x_{l-r}&+rX^x_{l-r}.
 \end{array}
 \tag{UC.23}
\]
To check every coefficient, in the minus part use
\[
 (r+p)\binom{r+p-1}{r-1}
       =r\binom{r+p}{r}.
\]
Writing \(i=l+1-s\) reduces its binomial sum to the Lie part of (UC.7) with \(j=l+1\) and derivative index \(r+1\), multiplied by \(-r\). In the plus part use
\(p\binom{r+p-1}{r-1}=r\binom{r+p-1}{r}\) and replace \(p\) by \(p-1\); it reduces to the plus part of that same identity with the same factor \(-r\). There is no scalar term, since these are coefficient derivations, not an affine bracket. For \(l=-1\), (UC.2) gives the first row directly. This proves (UC.23), including every splitting boundary.

Apply the coefficient product rule to (UC.3). By (UC.23),
\[
 [\mathscr D_l,L_{x,r}]
       =-r\,\rho(x_{l-r}).
 \tag{UC.24}
\]
All computations can be made modulo \(I_N\) with a common larger cutoff; for the \(D_{-1}\) term use \(I_{N+1}\). No derivative on an input vector of \(M\) is involved. Since \(\mathscr D_l\operatorname{Id}=0\), induction on a negative word, using the universal intertwining (UC.10), proves
\[
 \begin{aligned}
 \mathscr D_lY(x_{-r}u,z)
 &=L_{x,r}Y(D_lu,z)-rY(x_{l-r}u,z)\\
 &=Y(D_l(x_{-r}u),z).
 \end{aligned}
\]
Consequently \(\mathscr D_lY(w,z)=Y(D_lw,z)\).
Invert the finite alternating binomial change (UC.22). The coefficient identity
\(\binom{l+1}{s}\binom{l+1-s}{a}
 =\binom{l+1}{s+a}\binom{s+a}{s}\)
and the sum \(\sum_{s=0}^b(-1)^s\binom bs=\delta_{b,0}\) give
\[
 \boxed{D_l^{\mathrm{coeff}}Y(w,z)
    =\sum_{s=0}^{l+1}\binom{l+1}{s}z^sY(D_{l-s}w,z),
                 \qquad l\geq0.}
 \tag{UC.25}
\]
This is a universal full-Laurent-coefficient identity, not a test on vacuum creation series. For \(l=-1\), the first-row computation gives
\(D_{-1}^{\mathrm{coeff}}Y(w,z)=Y(D_{-1}w,z)\).
The derivative identity follows directly from (UC.5):
\(\partial_zL_{x,r}F=rL_{x,r+1}F+L_{x,r}\partial_zF\), while
\(T(x_{-r}u)=r x_{-r-1}u+x_{-r}Tu\).
Starting with the identity field proves \(Y(Tw,z)=\partial_zY(w,z)\).
Hence
\[
 D_{-1}^{\mathrm{coeff}}Y(w,z)=-\partial_zY(w,z).
 \tag{UC.26}
\]

For type A of matrix size \(a\), retain the actual raw or traceless determinant states \(w_i\) and \(D_i=i\). Put \(w_0=v\), with the actual trace state \(w_1\) in the raw case and \(w_1=0\) in the traceless case. The proved SL.X13 identity is
\[
 D_jw_i=(j+1)!\,C_{i,i-j}w_{i-j}\quad(1\leq j\leq i),\qquad
 C_{iq}=\binom{a-q}{i-q+1}
           +\frac{1-a}{2}\binom{a-q}{i-q}.
\]
The modes \(D_jw_i\) with \(j>i\) vanish by energy. Together with \(D_0w_i=-iw_i\), \(D_{-1}w_i=-Tw_i\), (UC.25)–(UC.26) give, for every regular formal vector field \(f(z)\partial_z\),
\[
 \boxed{D_f^{\mathrm{coeff}}\mathcal S_i(z)
  =-f\mathcal S_i'-D_i f'\mathcal S_i
       +\sum_{0\leq q<i}C_{iq}f^{(D_i-D_q+1)}\mathcal S_q(z).}
 \tag{UC.27}
\]
Here \(\mathcal S_i=Y(w_i,z)\), \(\mathcal S_0=1\) has indexed weight zero. This is the full universal field, including negative powers, rather than its vacuum regular restriction. For \(f=z^{l+1}\), extraction of the coefficient of \(z^{-n-D_i}\) gives the all-integer formula
\[
 \boxed{D_l^{\mathrm{coeff}}S_{i,n}
  =\bigl(n-(D_i-1)l\bigr)S_{i,n+l}
       +\sum_{0\leq q<i}C_{iq}(l+1)_{\underline{D_i-D_q+1}}
                                      S_{q,n+l},
       \qquad n\in\mathbb Z,\quad l\geq-1.}
 \tag{UC.28}
\]
Use \(S_{0,n}=\delta_{n,0}\operatorname{Id}\), and the falling factorial convention. The exponent check in the lower term is
\(z^{l-(D_i-D_q)}z^{-(n+l)-D_q}=z^{-n-D_i}\);
thus every term has mode index \(n+l\). For \(l=-1\), the derivatives of \(f=1\) vanish and the first coefficient is \(n+D_i-1\), exactly the coefficient of \(-\partial_z\mathcal S_i\).

A general \(f=\sum_{l\geq-1}f_lz^{l+1}\) is interpreted in the completion coefficientwise. Modulo \(\widehat I_N\), (UC.20) kills every term in (UC.28) for sufficiently large \(l\), so the sum is finite at each quotient. The same proof applies to any actual homogeneous invariant lifts with a separately established basic-vector coordinate law; it does not establish that such lifts exist in other types. Integration to full completed coordinate substitutions and exhaustion of a specified completed centre are separate consequences that require their stated completion and comparison arguments.

The universal descent and current commutation can be viewed as the following exact diagram:
\[
 \begin{array}{ccc}
 V_{\kappa,R}
 &\xrightarrow{\ Y_M\ }&\operatorname{Fields}(M)\\[2pt]
 x_j\downarrow&&\downarrow\rho(x_j)\\[2pt]
 V_{\kappa,R}
 &\xrightarrow{\ Y_M\ }&\operatorname{Fields}(M).
 \end{array}
\]
*For negative \(j\), the right arrow is normal multiplication (UC.3).
For nonnegative \(j\), it is the finite commutator sum (UC.6).
The mixed boundary (UC.7), including its affine scalar, proves that these
are one affine action. Induction gives the square (UC.10); locality and
the finite delta expansion then give every physical integer commutator
in (UC.14). The target need not have a vacuum. The independent
moving-origin boundary (UC.23) supplies the universal coordinate
identity (UC.25).*

All assertions above hold over ordinary nonreduced rings. They use free PBW words, finite sums at each module input or quotient, and rational binomial identities. The resulting critical Fourier coefficients are independent of PBW representatives, natural on every smooth module, mutually commuting, and have the exact PBW symbols, conserved mode sums and strict cutoff (UC.20). The completed algebra structure is the specified smooth completion of CW; no derived-module, chiral or Poisson comparison is included here.

#### 3.6.3. The whole completed polynomial center in type A

Let \(k\) be a characteristic-zero field, let \(R\) be any ordinary commutative \(k\)-algebra, and let \(\mathfrak g\) be a finite direct sum of split \(\mathfrak{sl}_{n_j}\) factors and a finite-dimensional abelian center \(\mathfrak z\). Use the critical form \(-\operatorname{Kil}/2\), including its zero restriction to \(\mathfrak z\), with the \(df\)-first cocycle and central action \(K=1\). The following argument identifies the center of the precise smooth-module completion. The completion and universal-mode constructions of §§3.6.1–3.6.2 prove the precise inputs stated next.

**Exact inputs.** Write \(A_R\) for the algebraic critically specialized enveloping algebra of polynomial currents, and, for \(N\geq1\), put
\[
\mathfrak h_N=\mathfrak g_R\otimes t^NR[t],\qquad
I_{N,R}=A_R\mathfrak h_N,\qquad M_{N,R}=A_R/I_{N,R}.
\tag{CT.1}
\]
We require the following precise results of the preceding completion and universal-mode constructions.

1. The **smooth completion of §3.6.1** constructs an associative complete separated topological algebra
\(\widehat A_R=\varprojlim_NM_{N,R}\), with \(A_R\) dense, and identifies the kernel \(\widehat I_{N,R}\) of its projection with the closure of \(I_{N,R}\). Each \(M_{N,R}\) is an actual smooth cyclic left module on which this completion acts continuously. Its PBW length filtration is exhaustive, with
\[
\operatorname{gr}M_{N,R}
=\operatorname{Sym}_R(\mathfrak g_R\otimes\operatorname{span}_R\{t^m:m<N\}).
\tag{CT.2}
\]
The projection of \(u\in\widehat A_R\) is its action on \(1_N=1+I_{N,R}\). Fixed-current commutators extend continuously; commuting with all polynomial currents is equivalent to centrality in the completion, by density and the multiplication continuity. These are the constructions and criteria (CW.1)–(CW.19). Nonnegative-current adjoint actions preserve \(I_{N,R}\) directly: if \(q\geq0\) and \(m\geq N\), then \([x_q,y_m]=[x,y]_{q+m}\) is still in \(\mathfrak h_N\), with no central contraction since \(q+m>0\). The derivation rule gives preservation of its generated left ideal, and brackets preserve the PBW filtration. The same assertions hold after every ordinary coefficient extension in the defined inverse-limit sense.

2. The **universal-mode construction of §3.6.2** reconstructs, from each proved invariant basic state \(w_i\) of length degree and energy \(D_i\), an actual normally ordered field
\[
\mathscr S_i(t)=\sum_{n\in\mathbb Z}S_{i,n}t^{-n-D_i}
\tag{CT.3}
\]
in this completion. Every mode \(S_{i,n}\) commutes with every current as an element of \(\widehat A_R\), not merely as an operator on the vacuum. Its normally ordered expression is the finite linear combination prescribed by the negative-mode word expression of \(w_i\), with derivative currents and every integer current mode. The construction is relative over \(R\).

The UC input is proved by the arbitrary-target normal reconstruction, affine intertwining and finite-distribution argument (UC.1)–(UC.16); its mode sum, symbol and cutoff are (UC.17)–(UC.20). The basic states required in that input exist in all type A factors by (SL.L1)–(SL.L23); their polynomial independence and vacuum exhaustion are (SL.C1). Central degree-one states are the zero-form currents of (RV.16)–(RV.20). We also use the already proved classical current-invariant theorem (GJ.1)–(GJ.13), with its explicit split-root, principal-section and invariant-polynomial foundations retained. It applies to the semisimple factors, while the central variables are invariant separately. No chiral, Poisson, Satake or derived comparison is an input here.

**The completed-center theorem** is the topological algebra isomorphism
\[
\boxed{
Z(\widehat A_R)
\simeq\varprojlim_{N\geq1}
 R[S_{i,n}:n\leq D_i(N-1)].
}
\tag{CT.4}
\]
Each ring on the right is an ordinary polynomial ring: every element of an individual stage involves finitely many variables and has finite degree. Its transition maps set the newly admitted higher-index modes equal to zero. The inverse limit permits PBW degrees to grow with \(N\); no globally bounded degree is imposed.

##### Classical symbols at a fixed pole bound

Choose a nondegenerate invariant pairing on the semisimple factors, using the matrix trace pairing on each \(\mathfrak{sl}_n\). For the center use its vector-space dual rather than its zero critical form. The residue pairing identifies (CT.2) with the polynomial coefficient algebra of
\[
\alpha(t)\in t^{-N}\mathfrak g^*[[t]]\,dt,
\qquad
x_m\longmapsto\bigl(\alpha\mapsto\langle x,\alpha_{-m-1}\rangle\bigr).
\tag{CT.5}
\]
On the semisimple factors the chosen invariant pairing identifies \(\alpha\) with \(A(t)\,dt\). On the center it keeps \(\mathfrak z^*\) explicitly. Let \(p_i\) be the basic homogeneous invariant polynomials of degree \(D_i\): elementary characteristic coefficients on the type A factors and linear coefficient functions on the center. The infinitesimal action of a nonnegative current on a symbol is the derivation
\([x_q,y_m]=[x,y]_{q+m}\), with indices \(q+m\geq N\) set to zero. The central cocycle lowers PBW degree and is absent on symbols. By invariance of the chosen pairing this is exactly the contragredient adjoint action on the Laurent coefficient space in (CT.5).

Rescale the semisimple series by
\(B(t)=t^NA(t)\). This is an isomorphism of coefficient polynomial rings and intertwines all nonnegative-current derivations: scalar multiplication by \(t^N\) commutes with adjoint brackets. Homogeneity gives
\[
p_i(B(t))=t^{ND_i}p_i(A(t)).
\tag{CT.6}
\]
The complete theorem (GJ.13), applied to \(B\), therefore proves
\[
\boxed{
\bigl(\operatorname{gr}M_{N,R}\bigr)^{\mathfrak g_R[[t]]}
=R[p_i(A)_r:r\geq-ND_i].
}
\tag{CT.7}
\]
The coefficients on the right are algebraically independent over \(R\). Every invariant polynomial uses only finitely many coefficient variables; the finite-kernel argument (GJ.11)–(GJ.12) covers each such polynomial over nonreduced \(R\) too. The center contributes independent linear variables with \(D_i=1\), since its adjoint derivations are zero. Expanding in the monomial basis of those central variables reduces the remaining condition coefficient by coefficient to (GJ.13). Thus this central extension of (CT.7) uses no nondegenerate critical form on \(\mathfrak z\).

Under the restriction from pole bound \(N+1\) to \(N\), set \(A_{-N-1}=0\). For every degree \(D_i\), this sets precisely the new coefficients
\(- (N+1)D_i\leq r<-ND_i\) equal to zero, and leaves all coefficients \(r\geq-ND_i\) equal to their equally indexed polynomial at the smaller pole bound. Their independence proves that the transition on the invariant polynomial rings is exactly this substitution.

There is also no additional Laurent-current invariant condition on their completed inverse limit. For an index \(q=-b<0\), adjoint differentiation carries the kernel of the symbol projection at \(N+b\) into the kernel at \(N\): a generator of index \(m\geq N+b\) is replaced by one of index \(m-b\geq N\). The product rule proves the same containment for its generated ideal. For \(q\geq0\), the kernel at \(N\) is preserved. This gives the continuous derivations on the inverse limit. For a finite Laurent current \(x(t)\), invariance of \(p_i\) gives the identity
\[
d p_i(A(t))([x(t),A(t)])=0
\tag{CT.8}
\]
as a Laurent series, coefficient by coefficient; it is the same polynomial infinitesimal identity evaluated over the Laurent coefficient ring. A negative mode can raise the pole bound by a finite amount, so (CT.8) is read at that larger bound before restriction. A polynomial in invariant coefficients is lifted to larger pole bounds using those same equally indexed coefficients; (CT.8) holds on these compatible lifts. Formal positive tails affect any fixed polynomial through only finitely many modes. Consequently every finite polynomial in these completed invariant coefficients, and then every compatible inverse-limit tuple by continuity of these derivations, is invariant under all Laurent currents. Conversely a Laurent-current invariant tuple is in particular nonnegative-current invariant at every stage, so (CT.7) applies. This identifies the completed classical invariant ring with
\[
\varprojlim_N R[p_i(A)_r:r\geq-ND_i].
\tag{CT.9}
\]
This is a statement about continuous current derivations on the inverse limit. A negative current is not asserted to preserve any single pole-bound stage.

##### Every mode at the finite cutoff

The universal normal expression of a basic state of energy \(D_i\) is a finite sum of words with \(q\leq D_i\) derivative-current factors. If its underlying negative-mode indices are \(-a_1,\ldots,-a_q\), then \(a_j\geq1\) and \(\sum a_j=D_i\). After taking a field coefficient, a term has current indices \(m_1,\ldots,m_q\) satisfying
\[
\sum_{j=1}^q m_j=n.
\tag{CT.10}
\]
Indeed differentiating a current \(a_j-1\) times changes its power to \(t^{-m_j-a_j}\), and the product power is \(t^{-n-D_i}\). Reordering currents can only decrease the number of letters; a bracket replaces its two indices by their sum, and a central contraction requires their sum to be zero. Thus (CT.10) is preserved in every lower-length contribution.

In a normally ordered term, negative currents occur to the left of nonnegative currents. A nonnegative index at least \(N\) can be moved to the far right through the other nonnegative indices: their brackets still have index at least \(N\), and no central term is possible. It then kills \(1_N\). Thus only terms with every \(m_j<N\) remain modulo \(I_{N,R}\). For a surviving term,
\[
m_j\geq n-(q-1)(N-1).
\tag{CT.11}
\]
There are finitely many integer index lists between this lower bound and \(N-1\). This proves that each mode has a finite normally ordered representative at this cutoff, of PBW length at most \(D_i\). It also proves the exact vanishing
\[
S_{i,n}\in\widehat I_{N,R}
\qquad\text{if }n>D_i(N-1).
\tag{CT.12}
\]
The restriction \(N\geq1\) matters in the last bound: \(q(N-1)\leq D_i(N-1)\).

At length \(D_i\), energy \(D_i\) forces every \(a_j=1\). The top normal-expression part is therefore the commutative product of current series prescribed by the leading invariant \(p_i\). The residue identification (CT.5) and (CT.10) give
\[
\sigma_{D_i}(S_{i,n}\bmod\widehat I_{N,R})
=p_i(A)_{-n-D_i}.
\tag{CT.13}
\]
For type A, the transpose in the trace pairing leaves characteristic coefficients unchanged, exactly as in the proof of (SL.C1). Every allowed mode \(n\leq D_i(N-1)\) has a nonzero independent degree-\(D_i\) symbol by (CT.7); disallowed modes have zero class by (CT.12), not merely a vanishing highest symbol.

The cutoff dictionary is exact:

| Homogeneous degree | Laurent coefficient allowed at pole bound \(N\) | Equally indexed central field mode |
|---|---|---|
| \(D_i\) | \(r\geq-ND_i\) | \(n=-r-D_i\leq D_i(N-1)\) |
| Quadratic type A coefficient | \(r\geq-2N\) | \(n\leq2(N-1)\) |
| Linear central coefficient | \(r\geq-N\) | \(n\leq N-1\) |

*The top-symbol identification is (CT.13); the high-mode vanishing is (CT.12). At \(N=1\), only modes \(n\leq0\) survive, and the dual current series permits a simple pole. This cutoff retains the zero currents and is distinct from the ordinary vacuum quotient by all nonnegative currents. Increasing \(N\) admits finitely many additional negative Laurent coefficients for each basic degree.*

##### Why the polynomial kernel is an ideal despite the left-module quotient

The quotient \(M_{N,R}\) is not asserted to be an algebra: \(I_{N,R}\) is a left ideal. For an actual central element \(z\in\widehat A_R\), choose a finite representative \(a_N\in A_R\) of \(z1_N\). For \(h\in\mathfrak h_N\),
\[
h a_N1_N=h z1_N=z h1_N=0.
\]
Therefore \(h a_N\in I_{N,R}\), and multiplying on the left by arbitrary algebra elements proves
\[
I_{N,R}a_N\subseteq I_{N,R}.
\tag{CT.14}
\]
Thus each such representative belongs to the right normalizer of the left ideal. Its image determines an \(A_R\)-module endomorphism on the cyclic quotient, by right multiplication on representatives. The actual central operator has the same value on every vector, because
\(z(b1_N)=b(z1_N)=b a_N1_N\).

For two central elements with representatives \(a_N,b_N\), their product on \(1_N\) is represented by \(b_Na_N\). Since the central operators commute, \(a_Nb_N\) gives the same class as well. Multiplying these finite representatives is legitimate by (CT.14), and its top symbol in (CT.2) is the ordinary commutative product of their symbols. Reordering a finite product produces only smaller-length brackets; killing indices at least \(N\) kills their symbols in (CT.2). A product of allowed generator symbols remains a nonzero polynomial in the independent coordinates (CT.7). Hence for a polynomial in the central modes,
\[
\sigma\bigl(P(S_{i,n})1_N\bigr)
=P_{\rm top}\bigl(p_i(A)_{-n-D_i}\bigr),
\tag{CT.15}
\]
where \(P_{\rm top}\) is its highest part for the weight assignment \(\deg S_{i,n}=D_i\). The right side is nonzero if that part is nonzero, over arbitrary \(R\) as well: algebraic independence is an injective polynomial-coordinate map, not a domain assumption on \(R\).

Let \(\mathscr P_R=R[s_{i,n}:n\in\mathbb Z]\) be the ordinary polynomial algebra, with only finite polynomials allowed. Its evaluation in the actual central modes, followed by \(z\mapsto z1_N\), has kernel exactly
\[
J_{N,R}=(s_{i,n}:n>D_i(N-1)).
\tag{CT.16}
\]
Containment of this ideal in the kernel follows from (CT.12) and centrality: multiplying a vanishing central mode by any other central polynomial still kills \(1_N\). For the reverse inclusion, first remove the disallowed variables. A nonzero remaining polynomial has nonzero highest weighted part and hence nonzero class by (CT.15). Thus
\(\mathscr P_R/J_{N,R}=R[s_{i,n}:n\leq D_i(N-1)]\) injects into \(M_{N,R}\), with its algebra structure supplied by the central operators and their normalizers, not by all of \(M_{N,R}\).

##### Finite decreasing-degree exhaustion

Let \(u\in Z(\widehat A_R)\), and fix \(N\). Its image \(u_N\in M_{N,R}\) is a finite vector with some finite PBW degree \(d\), by the CW input. Nonnegative currents preserve \(I_{N,R}\); on the quotient their adjoint action is therefore well defined. Projection of the equation \([x_q,u]=0\), \(q\geq0\), gives adjoint invariance of \(u_N\). Its top symbol lies in (CT.7), so is a finite polynomial in the coefficients \(p_i(A)_r\).

This top symbol is homogeneous of PBW degree \(d\). Since the variables in (CT.7) are independent and homogeneous of degrees \(D_i\), take the uniquely corresponding weighted-degree-\(d\) polynomial \(P_d\) in the allowed modes, using \(r=-n-D_i\). By (CT.13) and (CT.15), its evaluation has the same top symbol. Consequently
\[
(u-P_d(S))_N\in F_{d-1}M_{N,R}.
\tag{CT.17}
\]
The subtracted element is actually central, so the same invariance argument applies to its remaining top symbol. Repeat. The nonnegative integer degree strictly decreases at every nonzero step. Degree zero is a scalar in \(R\). After finitely many steps,
\[
u_N=P_N(S)1_N,
\qquad
P_N\in R[s_{i,n}:n\leq D_i(N-1)].
\tag{CT.18}
\]
Uniqueness follows from (CT.16). This argument is repeated for each finite cutoff, not for a global filtration degree of \(u\). An element of \(\widehat A_R\) need not have any uniform PBW bound.

Compatibility of the classes \(u_N\) and the exact kernel (CT.16) imply compatibility of their unique polynomials: the restriction of \(P_{N+1}\) sets the new high modes to zero and equals \(P_N\). This gives an injective map
\[
Z(\widehat A_R)\longrightarrow
\varprojlim_N\mathscr P_R/J_{N,R}.
\tag{CT.19}
\]
Injectivity also follows immediately from separatedness of the CW completion.

Conversely, take a compatible tuple \((P_N)\) in that limit. Evaluate each finite polynomial in the actual central modes, obtaining \(z_N\in Z(\widehat A_R)\). By compatibility and (CT.16),
\(z_{N+1}-z_N\in\widehat I_{N,R}\). More generally \(z_M-z_N\in\widehat I_{N,R}\) for \(M\geq N\). Thus these finite central polynomial approximants are Cauchy in the specified topology and have a unique limit \(z\in\widehat A_R\). Every fixed-current commutator is continuous and vanishes on every approximant, so vanishes on \(z\). By the CW centrality criterion, \(z\) is central. Its image at cutoff \(N\) is exactly \(P_N(S)1_N\). This proves surjectivity of (CT.19), and proves (CT.4).

On the center, each \(\widehat I_{N,R}\cap Z(\widehat A_R)\) is an ideal. Under (CT.4) it is the kernel of projection to \(\mathscr P_R/J_{N,R}\). Hence the isomorphism and its inverse preserve these neighborhood bases: it is a topological algebra isomorphism, not merely a bijection of underlying sets. The proof has established that the center is the closure of finite polynomials in the universal central modes.

##### Type A reductive factors and scalar variables

For a direct sum, the semisimple basic invariant lists concatenate and the center contributes a degree-one list. The critical center form is zero, so every central current mode is already central in the algebraic enveloping algebra. Its cutoff is \(m<N\), exactly (CT.12) with degree one. The classical coefficient-ring proof and the universal-mode proof then apply to the whole direct sum at once. This establishes (CT.4) for all the stated split type A reductive Lie algebras. No completed tensor product is replaced by an ordinary tensor product: the common pole-bound inverse limit is the specified topology on the entire list.

In particular the matrix algebra \(\mathfrak{gl}_n\) has scalar current \(c=I/n\), as in (TR.2), and a traceless factor. On symbols write \(A=F+c\mathbf1\). The elementary identity
\(\det(z\mathbf1+A)=\det((z+c)\mathbf1+F)\) gives, by the ordinary binomial expansion,
\[
e_i(A)=\sum_{j=0}^{i}\binom{n-j}{i-j}c^{i-j}e_j(F),
\qquad e_0(F)=1,\quad e_1(F)=0.
\tag{CT.20}
\]
This is an invertible triangular polynomial change: \(e_1(A)=nc\) determines \(c\), and then each \(e_i(F)\) is solved successively with coefficient one. The identities hold for Laurent series and their finite coefficient polynomials at each pole bound. Hence the raw matrix characteristic coefficients also give the independent classical list of degrees \(1,2,\ldots,n\). Applying the universal construction of §3.6.2 to the raw invariant determinant states of (SL.L1)–(SL.L23) before the traceless quotient gives the version of (CT.4) on their raw modes. Equivalently, the semisimple modes and the degree-one scalar modes are always a proved generator list under the stated inputs. The normalization of the latter is \(c=I/n\), so the trace variable is \(n\) times that coefficient, as in (TR.2)–(TR.24).

##### Completed coefficient extension and the continuous functor

The coefficient-base statement is
\[
Z(\widehat A_R)
\simeq\varprojlim_N
\left(R\otimes_k k[s_{i,n}:n\leq D_i(N-1)]\right).
\tag{CT.21}
\]
This is the completed coefficient extension of the center over \(k\), with completion defined by these stage quotients. It is not an assertion that ordinary \(R\otimes_k-\) commutes with the inverse limit. Its proof above is relative over \(R\): the classical kernels commute with coefficient extension by (GJ.11)–(GJ.13), PBW quotients remain free, normal-expression identities are relative, and no step divides by a coefficient of \(R\). Nilpotents are retained throughout.

To specify its coefficient functor, give \(R\) the discrete topology. A continuous unital \(k\)-algebra homomorphism from the completed center over \(k\) to \(R\) kills an open neighborhood ideal, hence factors through some stage in (CT.4). A stage homomorphism chooses arbitrary coefficients in \(R\) for all its allowed variables. Under \(r=-n-D_i\), these are the coefficients of Laurent series
\[
s_i(t)\in t^{-ND_i}R[[t]],
\qquad
\operatorname{Hom}_{\rm cont}\bigl(Z(\widehat A_k),R\bigr)
\simeq\varinjlim_N\prod_i t^{-ND_i}R[[t]].
\tag{CT.22}
\]
This is a coefficient ind-functor with bounded poles at each stage. Increasing \(N\) sets newly available negative coefficients to zero on the inclusion of an earlier stage. All \(D_i\) are positive and there are finitely many basic factors, so these common bounds are cofinal among all finite pole bounds on the lists. One may append the density symbols \((dt)^{D_i}\) for their leading classical weights; the full quantum coordinate laws include the lower terms already proved in §3.4, rather than only this highest-weight notation.

Equation (CT.22) concerns continuous characters into a discrete ordinary ring. It does not identify the ordinary \(\operatorname{Spec}\) of the underlying abstract inverse-limit algebra, with all possible discontinuous characters, with that ind-functor. Nor is the completed center a ring of arbitrary formal series in the modes already surviving at \(N=1\): each finite-cutoff expression must still be a finite polynomial. Completion permits infinite sums only when their tails vanish at every prescribed cutoff.

The exact proof mechanism is
\[
\begin{array}{ccc}
\text{central }u\text{ in the CW completion}
 &\longrightarrow&u_N\text{ of finite PBW degree}\\
 &&\downarrow\ \text{nonnegative-current top symbol, (CT.7)}\\
\text{compatible polynomials }(P_N)
 &\longleftarrow&\text{finite degree descent using (CT.13)–(CT.17)}\\
\downarrow\ \text{central Cauchy approximants}
 &&\\
Z(\widehat A_R)\simeq\varprojlim_N\mathscr P_R/J_{N,R}.&&
\end{array}
\tag{CT.23}
\]
*Finite PBW degree is used only on the right, at an individual cutoff. Normalizer representatives supply its polynomial products; exact independence supplies compatibility. Completion and continuity supply the final central limit.*

Applying the preceding CW/UC constructions, the theorem proves the full completed center for the stated type A and zero-form central factors at the exact classical structural premises retained above. Section 3.7 supplies the intrinsic critical Poisson structures and the full type A scalar-oper Poisson comparison. Chiral/factorization structures, Satake compatibility, a derived-family comparison, non-type-A basic lifts and full oper-Poisson comparison, derived/global Hamiltonian reduction and the geometric central-line convention needed by localization remain their separate mathematical statements.

#### 3.6.4. The complete abelian center at an arbitrary fixed form

Now let \(\mathfrak z\) be a finite-dimensional abelian Lie algebra over \(k\), with any fixed symmetric form \(\kappa\). Its affine brackets are
\[
[z_j,y_m]=j\kappa(z,y)\delta_{j+m,0}.
\tag{HC.1}
\]
Use \(A_R,I_{N,R},M_{N,R},\widehat A_R\) from (CW.1)–(CW.6), with \(\mathfrak g=\mathfrak z\), and put \(W=\operatorname{rad}(\kappa)\). The fixed form extends to \(R\). Choose a basis of \(\mathfrak z\) and its ordered modes. As an \(R\)-module, \(M_{N,R}\) has the polynomial basis in all mode variables \(z_j\) with \(j<N\). This polynomial identification initially describes only a vector space. When \(\kappa\ne0\), the products of paired positive and negative modes in \(A_R\) still have the scalar commutator (HC.1).

**Commutators are exact derivatives in the quotient.** Fix \(j<N\), \(j\ne0\), and \(y\in\mathfrak z_R\). Right commutation defines
\[
\partial_{y,j}:M_{N,R}\to M_{N,R},
\qquad
a+I_{N,R}\longmapsto[a,y_{-j}]+I_{N,R}.
\tag{HC.2}
\]
It is well defined. For a high generator \(z_m\), \(m\geq N\), the bracket \([z_m,y_{-j}]\) vanishes because \(m\ne j\). Thus
\([az_m,y_{-j}]=[a,y_{-j}]z_m\in I_{N,R}\).
This proves preservation of the left ideal, without imposing two-sidedness.

On a basis letter with index \(i<N\), its right commutator is
\[
[z_i,y_{-j}]=j\kappa(z_i,y)\delta_{i,j}.
\]
The commutator product rule removes one matching letter at a time. Its scalar coefficients commute with every remaining letter, and removing a letter from an ordered monomial keeps that monomial ordered. Therefore, if \(z_1,\ldots,z_q\) is a basis and \(Z_{a,j}\) is its mode variable,
\[
\partial_{y,j}
=j\sum_{a=1}^q\kappa(z_a,y)
       \frac{\partial}{\partial Z_{a,j}}
\quad\text{on }M_{N,R}.
\tag{HC.3}
\]
The sign in (HC.3) belongs to \([a,y_{-j}]\); the left commutator \([y_{-j},a]\) is its negative.

Every zero mode \(z_0\) commutes with every current at every form, since the coefficient in (HC.1) is zero. It is a nonzero PBW variable in every \(M_{N,R}\). For the nonzero modes, choose a complement \(C\) to \(W\) in \(\mathfrak z\). The proof in (RV.9)–(RV.11) gives a nondegenerate restriction on \(C\) and dual elements \(\eta_a\) for a basis \(c_a\). It follows from (HC.3) that
\[
\partial_{\eta_a,j}=j\,\partial_{C_{a,j}}
\qquad(j<N,\ j\ne0).
\tag{HC.4}
\]
The integer \(j\), positive or negative, is a unit over every ordinary \(R\).

The coefficient proof is elementary over \(R\). If \(\partial_Xp=0\) for \(p=\sum_{d=0}^D p_dX^d\), then each \(d p_d=0\), and integer invertibility forces \(p_d=0\) for \(d\geq1\). A polynomial uses finitely many variables, so imposing (HC.4) for every indicated index removes every \(C\)-direction at a nonzero mode. Hence their joint kernel is exactly
\[
P_{N,R}
=\operatorname{Sym}_R\left(
\mathfrak z_{0,R}\oplus
 W_R\otimes_R
 \bigoplus_{\substack{j<N\\j\ne0}}Rt^j
\right).
\tag{HC.5}
\]
Here \(\mathfrak z_{0,R}\) is a copy of the entire \(\mathfrak z_R\) at mode zero. The second summand excludes zero, so radical zero modes are counted once. The map from this polynomial algebra into \(M_{N,R}\) is injective by its PBW basis.

In fact these variables have mutually central representatives in \(A_R\). The zero modes commute by (HC.1), and every mode of \(W_R\) commutes because the form pairs it with zero. Thus \(P_{N,R}\) has its genuine ordinary polynomial multiplication. Its transition to \(P_{L,R}\), \(L<N\), sets the radical variables of index at least \(L\) to zero and retains the zero modes. This multiplication is a feature of the central subalgebra just exhibited, not an algebra structure on the ambient \(M_{N,R}\).

**Necessity and sufficiency in the completion.** If \(u\in Z(\widehat A_R)\), it commutes with every \(y_{-j}\). Passing its commutator to \(M_{N,R}\) is legitimate for \(j<N\), because (HC.2) preserves \(I_{N,R}\) and extends continuously. Equations (HC.3)–(HC.5) therefore imply \(u_N\in P_{N,R}\). These components are compatible.

Conversely, a compatible family \(p_N\in P_{N,R}\) is an element of \(\widehat A_R\). Choose its representative in the polynomial algebra of the central modes of \(A_R\). Each representative commutes with every polynomial current, and the representatives converge to the given family. Left and right current multiplication are continuous by (CW.13), so their limit commutes with every current. The center criterion (CW.16) then makes this family central. Products agree with the polynomial transition products: at each quotient a central representative of \(p_N\) acts on a central representative of \(q_N\); their difference from any later representative belongs to \(I_{N,R}\), and its product with the central \(q_N\) remains in \(I_{N,R}\). Equivalently one can apply the action construction (CW.12) and commute these actual central representatives.

We have consequently proved an isomorphism of complete algebras
\[
\boxed{\quad
Z(\widehat A_R)
=\varprojlim_{N\geq1}
\operatorname{Sym}_R\left(
\mathfrak z_{0,R}\oplus
 W_R\otimes_R
 \bigoplus_{\substack{j<N\\j\ne0}}Rt^j
\right).
\quad}
\tag{HC.6}
\]
The topology is the induced quotient topology. The radical and the PBW variables in this formula extend from \(k\), and the integer-coefficient argument proves it directly over every ordinary \(R\), including nonreduced rings. It is also precisely the completed scalar extension of the center computed over \(k\), with these specified polynomial quotients. It need not be its ordinary tensor product with \(R\).

If \(\kappa\) is nondegenerate, \(W=0\), and (HC.6) is the ordinary polynomial algebra
\[
Z(\widehat A_R)=\operatorname{Sym}_R(\mathfrak z_{0,R}).
\tag{HC.7}
\]
It does not reduce to \(R\): all central zero modes survive. Nor does the completion permit an arbitrary formal power series in those zero modes. Every quotient in (HC.7) is the same polynomial algebra and has identity transition, so its inverse limit contains only polynomials.

At the abelian critical form \(\kappa=-\tfrac12\operatorname{Kil}_{\mathfrak z}=0\), the radical is \(\mathfrak z\). The zero and nonzero summands in (HC.6) combine, giving
\[
Z(\widehat A_{0,R})
=\widehat A_{0,R}
=\varprojlim_N
 \operatorname{Sym}_R\left(
 \mathfrak z_R\otimes_R\bigoplus_{j<N}Rt^j
 \right).
\tag{HC.8}
\]
All currents are central in this case. For the central factor of a split reductive Lie algebra, the same zero Killing restriction is the direct proof in (RV.18); the reductive decomposition itself retains its structural premise.

**The vacuum quotient removes the zero modes.** The abelian vacuum imposes the stronger relations
\[
V_{\kappa,R}=A_R/A_R\mathfrak z_R[t],
\qquad z_jv=0\quad(j\geq0).
\tag{HC.9}
\]
It is smooth, so the completion acts on it. For a central family \(u=(p_N)\), use \(N=1\) to compute \(uv\). The component \(p_1\) has only the full zero-mode variables and negative radical-mode variables. Every zero mode kills \(v\); thus its vacuum image is
\[
p_1\big|_{\mathfrak z_0=0}
\in\operatorname{Sym}_R(t^{-1}W_R[t^{-1}]).
\tag{HC.10}
\]
This polynomial acts as multiplication on the vacuum and commutes with all currents. The induction argument (K2.3) and the exact derivative proof (RV.9)–(RV.11) show that every vacuum endomorphism arises in this way. Therefore the natural map is a surjective algebra map
\[
Z(\widehat A_R)\longrightarrow
\operatorname{End}_{\widehat{\mathfrak z}_{\kappa,R}}(V_{\kappa,R})
=\operatorname{Sym}_R(t^{-1}W_R[t^{-1}]).
\tag{HC.11}
\]
Its kernel is the closed ideal generated inside (HC.6) by every zero mode and every positive radical mode. To check this description, a family in the kernel has, in each finite quotient, a central polynomial whose value after setting those modes to zero is zero. Polynomial coefficient uniqueness places that representative in their ordinary polynomial ideal. Its representatives then converge into the closure of that ideal. Conversely these nonnegative modes kill the vacuum, and evaluation on \(v\) is continuous by (CW.7); their closed ideal lies in the kernel.

The difference between the completed center and the vacuum algebra is explicit:

| Central form | Completed center | Vacuum endomorphism algebra |
|---|---|---|
| Nondegenerate | \(\operatorname{Sym}_R(\mathfrak z_0)\) | \(R\) |
| Arbitrary radical \(W\) | The inverse limit in (HC.6), with all zero modes | \(\operatorname{Sym}_R(t^{-1}W_R[t^{-1}])\) |
| Critical form \(0\) | Every current, completed in the positive-mode direction as in (HC.8) | \(\operatorname{Sym}_R(t^{-1}\mathfrak z_R[t^{-1}])\) |

*The quotient removes every nonnegative mode, including all \(z_0\). The remaining negative radical modes are exactly the abelian vacuum invariants of (RV.11).*

Finally, the coordinate automorphisms constructed in (CW.22)–(CW.23) preserve (HC.6). They fix \(z_0\), and on a radical current are exactly
\[
\sigma_\phi(w_j)=w\phi(t)^j,
\qquad w\in W_R,\quad j\in\mathbf Z,
\tag{HC.12}
\]
with the positive tail interpreted in the completion. A Laurent substitution has finite negative part and a coefficient-finite positive tail. The cofinal bounds in both directions make (HC.12) a continuous automorphism of the displayed center. It also preserves the vacuum relations, since \(\phi(t)^j\in R[[t]]\) for \(j\geq0\). Hence (HC.11) is coordinate equivariant. On its negative-mode generator \(w_{-r-1}v\), the residue calculation (RV.25) gives the already proved inverse one-form coefficient rule
\[
w_{-r-1}v\longmapsto
\sum_{a\geq0}[t^r]\psi'(t)\psi(t)^a\,w_{-a-1}v,
\qquad \psi=\phi^{-1}.
\tag{HC.13}
\]
The sum is finite if \(\psi(0)\) is nilpotent, as proved in (RV.24)–(RV.27). This verifies the compatibility of the complete central algebra with its ordinary vacuum coefficient quotient.

The construction and the entire abelian completed-center calculation are proved here. The semisimple presentation is supplied in type A by §3.6.3, and §3.7 constructs the intrinsic critical completed Poisson bracket. Non-type-A completed centers and oper-Poisson comparison, derived/global Hamiltonian reduction, chiral/factorization, Satake and derived comparisons, and all intrinsic reductive-oper and global central-convention questions retain their separate mathematical scope.

#### 3.6.5. Laurent coefficients, coordinates and restriction to the vacuum

We now give the coefficient interpretation and coordinate action of the completed type A center. We retain the split root-data and scalar-oper foundations stated in §§1–2. Let the basic degrees of one traceless matrix factor be \(D_i=i\), \(2\le i\le n\). Write its normalized scalar operator on the punctured disc as
\[
L=\partial_t^n+\sum_{i=2}^n s_i(t)\partial_t^{n-i},
\qquad s_i(t)=\sum_{r\in\mathbb Z}s_{i,r}t^r\in R((t)).
\tag{PC.1}
\]
Each coefficient series has a finite negative part. Since there are finitely many basic indices, the subfunctors
\[
\mathcal O_N(R)=\{(s_i):s_i\in t^{-ND_i}R[[t]]\},
\qquad N\ge1,
\tag{PC.2}
\]
are cofinal: every tuple belongs to one of them. Their coordinate rings and transition maps are
\[
P_{N,R}=R[s_{i,r}:r\ge-ND_i],\qquad
P_{N+1,R}\longrightarrow P_{N,R},\quad
s_{i,r}\longmapsto
\begin{cases}s_{i,r}&r\ge-ND_i,\\0&r<-ND_i.\end{cases}
\tag{PC.3}
\]
Indeed assigning the displayed variables arbitrarily is precisely assigning the corresponding formal series. The transition is restriction to the smaller pole-bound functor. In particular it is a surjection of polynomial rings, rather than an inclusion of their variable lists.

Give \(P_R=\varprojlim_NP_{N,R}\) the inverse-limit topology, with kernels of its projections as a neighborhood basis of zero. A continuous unital \(R\)-algebra homomorphism from \(P_R\) to a discrete \(R\)-algebra \(R'\) factors through some \(P_{N,R}\): continuity of the inverse image of zero places one of these kernels in its kernel, and the projection to \(P_{N,R}\) is surjective. Surjectivity follows by successively extending a polynomial in the existing variables and setting newly admitted variables to zero. Conversely every map through such a projection is continuous. Consequently
\[
\operatorname{Hom}_{R\text{-alg}}^{\mathrm{cont}}(P_R,R')
 =\underset{N}{\operatorname{colim}}\,\mathcal O_N(R').
\tag{PC.4}
\]
Equality here means the evident bijection of sets, natural in the ordinary coefficient algebra. No claim about all discontinuous characters of the abstract inverse-limit ring is needed. An element of \(P_R\) is a compatible sequence of finite polynomials; its polynomial degree may grow with \(N\).

Let \(S_{i,m}\) denote the completed central modes of §3.6.2, with field convention
\(S_i(z)=\sum_mS_{i,m}z^{-m-D_i}\). The completed-center theorem of §3.6.3 and the index change
\[
\Phi_R:S_{i,m}\longmapsto s_{i,-m-D_i}
\tag{PC.5}
\]
identify its cutoff ring with (PC.3), because
\[
m\le D_i(N-1)\quad\Longleftrightarrow\quad
-m-D_i\ge-ND_i.
\tag{PC.6}
\]
Thus \(\Phi_R:Z(\widehat A_{\mathrm{crit},R})\xrightarrow{\sim}P_R\) is an isomorphism of topological algebras. The multiplication is the central multiplication constructed using the smooth cyclic test modules in §3.6.1. It is not obtained by declaring their left-module quotients to be algebras. The finite polynomial independence and finite-degree exhaustion in §3.6.3 prove (PC.5) at each cutoff, hence prove the inverse-limit isomorphism.

For products of traceless matrix factors, take all their coefficient lists and use a common \(N\); their finitely many pole bounds have a common bound. At a zero-form central factor, add the coefficient series of the framed Laurent one-forms of §3.5.5. These have degree one and the same index change \(m=-r-1\). The split type A reductive comparison of §3.6.3 therefore gives the product of the adjoint scalar-oper coefficient functors and these framed central Laurent coefficient functors. The central framing and root-datum boundary of (CF.10)–(CF.13) remain in force. For \(\mathfrak{gl}_n\), one may instead use the raw scalar coefficients \(s_1,\ldots,s_n\): the finite triangular identities (TR.14)–(TR.17) remain valid for Laurent coefficients and identify the two descriptions. The common bounds in (PC.2) are cofinal under these identities. Differentiation increases the pole order of a series by at most one, and each of the finitely many polynomial expressions has a finite pole bound; this proves continuity in both directions.

Ordinary coefficient extension uses the completed expression
\[
P_R=\varprojlim_N(R\otimes_kP_{N,k}),
\tag{PC.7}
\]
and the corresponding expression for the center proved in §3.6.3. This formula applies to nonflat and nonreduced \(R\). It does not assert that ordinary tensor product commutes with this infinite inverse limit.

We next prove continuity of coordinate substitution on the actual affine completion. Let \(\phi(t)=b+t a(t)\), where \(a(0)\) is a unit and \(b^\nu=0\). Substitution and its inverse on Laurent series were constructed in §1.1.8. If \(M\ge\nu\), the finite binomial expansion shows
\[
\phi(t)^M\in t^{M-\nu+1}R[[t]],
\qquad
\sigma_\phi(t^M\mathfrak g[[t]])
 \subset t^{M-\nu+1}\mathfrak g[[t]].
\tag{PC.8}
\]
The second inclusion also follows term by term for a formal current: at a fixed output coefficient only finitely many input coefficients contribute. In particular, given \(N\), taking \(M\ge N+\nu-1\) places the substituted positive tail inside the \(N\)-th positive tail. The inverse coordinate has a nilpotent constant as well, so the same argument applies to it. The residue calculation (RC.C7) says that substitution preserves the affine cocycle. Therefore it extends to mutually inverse continuous automorphisms of \(\widehat A_{\kappa,R}\), and consequently of its center. These conclusions use the completion and smooth action proved in §3.6.1.

The density transport of §3.4.2 is also defined on (PC.1). A Laurent series has finitely many negative powers; nilpotent substitution of each such power is the finite inverse expansion of §1.1.8. Its nonnegative part contributes finitely to any fixed output coefficient, because powers of the nilpotent constant eventually vanish. Multiplication by units and the finitely many derivatives in (SC.O7)–(SC.O10) preserve finite pole order. The square-root descent in (SC.O4)–(SC.O6) is unchanged: its free rank-two extension and its two sign choices concern the unit derivative of the coordinate, not the presence of Laurent coefficients. Thus the exact scalar law extends to every ordinary punctured-disc coefficient tuple.

A pointed coordinate preserves \(\mathcal O_N\). In (SC.O10), the term involving \(s_j\) is multiplied by a regular coefficient and a unit derivative to its \(j\)-th power, and \(j\le i\); its pole order is at most \(Nj\le Ni\). The term from the monic leading coefficient is regular. A nilpotent translation with nilpotence exponent \(\nu\) increases a pole bound by at most \(\nu-1\), as follows directly from the finite binomial expansion of a negative power. It therefore carries \(\mathcal O_N\) into \(\mathcal O_{N+\nu-1}\). These bounds prove continuity of the scalar coordinate action on the inverse-limit ring.

The universal coordinate calculation in §3.6.2 now provides the part that a vacuum-only calculation would not supply: for every Fourier mode, including those which vanish on the vacuum, the exact determinant law is
\[
D_lS_{i,m}=(m-(D_i-1)l)S_{i,m+l}
 +\sum_{j<i}C_{ij}(l+1)_{D_i-D_j+1}S_{j,m+l},
\qquad l\ge0.
\tag{PC.9}
\]
Here \(C_{ij}\) are the constants of (SL.X12), \((a)_d=a(a-1)\cdots(a-d+1)\), \(S_0(z)=1\), and hence \(S_{0,m}=\delta_{m,0}\). The traceless coefficient \(S_1\) is zero; the raw matrix case retains it. Translation and scaling are
\[
D_{-1}S_{i,m}=(m+D_i-1)S_{i,m-1},\qquad
\sigma_{t\mapsto at}(S_{i,m})=a^mS_{i,m}.
\tag{PC.10}
\]
The first equality follows by taking coefficients in the universal identity \(D_{-1}S_i(z)=-S_i'(z)\). The second follows from the total current-mode index of each homogeneous normal-field term, proved in §3.6.2. This includes the lower PBW terms: their derivatives change their powers of the field variable and retain the total current-mode index.

For completeness, taking the coefficient of \(z^{-m-D_i}\) in the Laurent scalar law
\[
\delta_v s_i=-v s_i'-D_iv's_i
 +\sum_{j<i}C_{ij}v^{(D_i-D_j+1)}s_j
\tag{PC.11}
\]
with \(v=z^{l+1}\) gives exactly (PC.9). In its first term, the contributing exponent is \(-m-l-D_i\), giving \(m+l+D_i-D_i(l+1)=m-(D_i-1)l\). In a term with index \(j\), the power of the derivative of \(v\) is \(l-D_i+D_j\), so its contributing mode is again \(m+l\). Translation and unit scaling likewise give (PC.10). Thus the generator map (PC.5) intertwines the exact infinitesimal laws, with the inverse-coordinate convention on coefficient functions.

We prove that this equality integrates on the completed rings. For \(l>0\), the derivation (PC.9) descends to the cutoff polynomial ring: an index \(m>D_i(N-1)\) stays beyond the permitted cutoff in its same-degree term, and every lower-degree term has a smaller permitted bound. Repeated application to a permitted generator increases its mode index by \(l\) at each nonconstant step and never increases its degree index. After finitely many steps it vanishes at this cutoff. An anomalous constant term has zero subsequent derivative. The product rule then proves local nilpotence on each finite polynomial. Hence the positive coordinate flow acts there by the finite sum
\[
\exp(cD_l)f=\sum_{q\ge0}\frac{c^q}{q!}D_l^qf.
\tag{PC.12}
\]
On affine currents this is the actual flow substitution: both solve the coefficient recursion obtained from \(t^{l+1}\partial_t\), starting with the same Laurent monomial. On each finite PBW representative modulo the cutoff, that recursion is finite. On scalar coefficients it is the actual inverse density flow, by differentiating (SC.O4); the resulting recursion has the same initial value and divides only by positive integers. Thus (PC.12) is the actual action on both sides.

The successive positive-flow factorization (TC.A8) still suffices, although completed central elements have no common finite energy bound. At a fixed cutoff their images are finite polynomials. On a generator \(S_{i,m}\), all \(l>D_i(N-1)-m\) vanish in (PC.9), including its lower-index terms. The finitely many earlier positive flows can only increase mode indices and lower degree indices, so this bound remains sufficient for their resulting finite expressions. Alternatively a coordinate whose first new term has arbitrarily high order acts trivially on any fixed finite PBW representative modulo \(I_N\): a changed factor acquires that order in its current index; commuting it past the finitely many factors to its right leaves an index at least \(N\), once the order exceeds the sum of their negative indices and the original factor's negative index. No central contraction can then occur. This proves directly that the successive flows equal actual substitution at every required cutoff.

A unit scaling is handled by (PC.10). A nilpotent translation acts by the finite sum \(\exp(bD_{-1})\), since \(b^\nu=0\); the binomial formula on Laurent monomials and the product rule prove equality with actual substitution. Factoring every continuous coordinate into these three kinds of substitutions, as in §1.1.8, now proves full ordinary equivariance:
\[
\begin{array}{ccc}
Z(\widehat A_{\mathrm{crit},R})&\xrightarrow{\ \Phi_R\ }&P_R\\
{\scriptstyle \sigma_\phi}\downarrow&&\downarrow{\scriptstyle f\mapsto f\circ\mathcal P_{\phi^{-1}}}\\
Z(\widehat A_{\mathrm{crit},R})&\xrightarrow{\ \Phi_R\ }&P_R.
\end{array}
\tag{PC.13}
\]
*The horizontal maps match the Fourier index \(m\) with the Laurent coefficient index \(-m-D_i\). Their cutoff bounds agree by (PC.6). The universal mode identities (PC.9)–(PC.10), proved in §3.6.2, and the finite integration (PC.12) prove this square for every ordinary coordinate, including nilpotent translations. The proof is cutoff by cutoff and requires no uniform polynomial-degree bound.*

For central Laurent one-forms, the current substitution and residue pairing give directly the inverse one-form law of (RV.24) and (RV.30). This proof applies to Laurent series by the same finite nilpotent substitution. Products therefore satisfy (PC.13), and the raw \(\mathfrak{gl}_n\) description satisfies it by the continuous Laurent extension of the shift identities (TR.14)–(TR.23).

Finally restrict central operators to the algebraic vacuum. Every vector in it is smooth, so the action of §3.6.1 defines a homomorphism to its affine endomorphism algebra. The universal creation identity in §3.6.2 gives
\[
S_{i,m}v=0\ (m>-D_i),\qquad
S_{i,-D_i-r}v=\frac{T^rw_i}{r!}\ (r\ge0).
\tag{PC.14}
\]
Since these modes commute with every current, their vacuum values determine their full vacuum operators by (K2.3). The polynomial independence and exhaustion of (SL.C1), or their reductive version (TR.19), therefore give the surjection
\[
Z(\widehat A_{\mathrm{crit},R})\longrightarrow
\operatorname{End}_{\widehat{\mathfrak g}_{\mathrm{crit},R}}(V_R),
\quad S_{i,-D_i-r}\longmapsto A_{i,r}.
\tag{PC.15}
\]
Its kernel is the closed ideal topologically generated by the modes \(S_{i,m}\) with \(m>-D_i\). Here is an explicit proof of this kernel statement. Let \(K_N\) be the kernel of the projection to the cutoff polynomial ring. The closed ideal in question contains every \(K_N\): the image of an element of \(K_N\) at a larger cutoff is a finite polynomial in which every term contains a newly admitted generator, all of which have mode index \(>D_i(N-1)\ge0>-D_i\); these expressions converge to the element. Modulo \(K_1\), setting the remaining finitely bounded high-mode variables to zero gives the ordinary free ring \(R[S_{i,-D_i-r}:r\ge0]\). Its independence in the vacuum proves that no further kernel exists. Thus the quotient is an ordinary polynomial ring, even though the original center is complete.

The coefficient meaning is restriction from Laurent tuples to regular tuples, setting all negative Laurent coefficients to zero. Combining (PC.5) and (PC.15) gives
\[
\begin{array}{ccc}
Z(\widehat A_{\mathrm{crit},R})&\xrightarrow{\ \Phi_R\ }&P_R\\
\downarrow&&\downarrow{\scriptstyle s_{i,r}=0\ (r<0)}\\
\operatorname{End}_{\widehat{\mathfrak g}_{\mathrm{crit},R}}(V_R)
&\xrightarrow{\ (TC.A9),\ (CF.12)\ }&R[s_{i,r}:r\ge0].
\end{array}
\tag{PC.16}
\]
*The vertical maps kill exactly the negative Laurent coefficients, whose Fourier indices are \(m>-D_i\). The lower map is the already proved ordinary vacuum comparison; the upper map is the full type A completed-center comparison. Creation (PC.14) and polynomial independence prove commutativity and the kernel. The regular coefficient functor is stable under the full ordinary continuous coordinate group, including nilpotent translations, so this square is coordinate equivariant as well.*

The following cases show what the vacuum forgets. In the abelian rows, the coefficient form is fixed over \(k\), and the completed-center descriptions are those proved in §3.6.4.

| Current algebra and fixed form | Completed central variables | Variables surviving on the vacuum |
| --- | --- | --- |
| \(\mathfrak{sl}_n\), \(-n\operatorname{tr}\) | \(S_{i,m}\), all \(m\in\mathbb Z\), completed with \(m\le i(N-1)\) | \(S_{i,-i-r}=A_{i,r}\), \(r\ge0\) |
| \(\mathfrak{gl}_n\), \(-n\operatorname{tr}(XY)+\operatorname{tr}(X)\operatorname{tr}(Y)\) | Raw \(S_{i,m}\), \(1\le i\le n\), with the same degree-dependent cutoffs | Raw divided determinant coefficients, \(r\ge0\) |
| Abelian \(\mathfrak z\), zero form | All \(z_m\), including \(z_0\), completed by upper mode cutoff | All negative \(z_m\); every nonnegative mode vanishes |
| Abelian \(\mathfrak z\), nondegenerate form | Ordinary \(\operatorname{Sym}_R(\mathfrak z_0)\) | Only scalar operators; the zero modes vanish |

*The difference in the last two rows comes from the paired nonzero modes, not from the zero modes. Zero modes are central for every abelian form. The exact center at an intermediate radical is (HC.1)–(HC.12); its vacuum restriction retains precisely the negative radical modes by (RV.11).*

These arguments prove the full smooth completed type A center and its ordinary punctured-disc coefficient comparison, at the explicit finite invariant-theory and scalar-oper foundations already stated. Section 3.7 supplies the intrinsic critical Poisson structures and the full type A oper-Poisson comparison. Basic quantum lifts and full oper-Poisson comparison in other types, derived/global Hamiltonian reduction, chiral/factorization comparison, a Satake construction, a derived-family comparison and the intrinsic and global central-convention comparisons of §3.5.3 retain their distinct proof obligations.


### 3.7. Critical Poisson brackets and Miura operators

#### 3.7.1. The intrinsic critical Poisson vertex algebra

Fix a characteristic-zero field \(k\), an ordinary commutative \(k\)-algebra \(R\), and a finite-dimensional Lie algebra \(\mathfrak g\). Let
\[
 \kappa_\varepsilon=\kappa_{\mathrm{crit}}+\varepsilon B,
 \qquad \kappa_{\mathrm{crit}}=-\frac12\mathrm{Kil},
 \qquad S=R[\varepsilon],
 \tag{PV.1}
\]
where \(B\) is an invariant symmetric form. Nondegeneracy of \(B\) is not required for this construction. The choice of \(B\) specifies the direction and normalization of the bracket. The affine cocycle uses
\([x_m,y_q]=[x,y]_{m+q}+m\kappa_\varepsilon(x,y)\delta_{m+q,0}\,1\).
PBW identifies the vacuum \(V_S\), uniformly in \(\varepsilon\), with the free \(S\)-module on ordered negative-current words. Its reduction is \(V_R\) at the critical form. In particular multiplication by \(\varepsilon\), and by \(\varepsilon^2\), is injective even if \(R\) is nonreduced. Every fixed state product is a finite expression with coefficients in \(S\).

The level-deformation construction is described by Edward Frenkel in the freely available author edition of [*Lectures on the Langlands Program and Conformal Field Theory*, §§8.1–8.2 and 8.4, arXiv hep-th/0512172v1](https://arxiv.org/abs/hep-th/0512172v1). We prove the residue and first-order identities here. The Poisson comparison with the oper Hamiltonian reduction requires the additional type A matrix, normalizer and classical free-field arguments of §3.8.

**Residue products, with their algebraic identity proved.** We use the universal current fields proved in §3.6.2 over \(S\), as well as over \(R\). For every smooth target \(M\), those fields are coefficient-finite, natural in \(M\), independent of negative-word representatives, and pairwise local. For two such fields put
\[
 (A_{(p)}B)(z)=\operatorname{Res}_s
 \bigl(\iota_{s,z}(s-z)^pA(s)B(z)
             -\iota_{z,s}(s-z)^pB(z)A(s)\bigr),
 \quad p\in\mathbb Z.
 \tag{PV.2}
\]
The geometric expansions give the derivative normal product when \(p<0\). For \(p\geq0\) they give the finite commutator sum. Their field property, locality closure and common input cutoffs were proved in (UC.12). No translation operator on the target is used.

We will need the full three-field residue identity. Its proof is elementary partial fractions, which we give explicitly. For a Laurent expression \(G(u,v)\) with possible diagonal poles only at \(u=0\), \(v=0\) and \(u=v\), let the two successive residues at \(0\) use respectively the expansions \(|v|<|u|\) and \(|u|<|v|\). Then
\[
 \operatorname{Res}_{v=0}\operatorname{Res}_{u=v}G
 =
 \operatorname{Res}_{u=0}^{\,|v|<|u|}
              \operatorname{Res}_{v=0}G
 -
 \operatorname{Res}_{v=0}^{\,|u|<|v|}
              \operatorname{Res}_{u=0}G.
 \tag{PV.3}
\]
Here \(\operatorname{Res}_{u=v}\) expands in \(u-v\). To prove (PV.3), take partial fractions in \(u\), with \(v\) invertible as a Laurent variable:
\[
 G=P(u,v)+\sum_a\alpha_a(v)u^{-a}
                      +\sum_b\beta_b(v)(u-v)^{-b}.
\]
The polynomial part has zero residue in \(u\). The \(u^{-a}\) terms have the same two successive residues and no diagonal residue. For a \((u-v)^{-b}\) term, the expansion with \(|u|<|v|\) has only nonnegative powers of \(u\), so its \(u\)-residue is zero. In the other expansion,
\[
 (u-v)^{-b}=\sum_{h\geq0}\binom{b+h-1}{h}v^hu^{-b-h}.
\]
The final \(u\)-residue is possible only for \(b=1,h=0\), and is then
\(\operatorname{Res}_v\beta_1(v)\), exactly the left side. This proves the identity term by term. The same calculation applies to a formal power-series numerator: at a specified final coefficient only a finite numerator jet can contribute to the fixed pole orders and residues. Partial fractions use only powers of the Laurent unit \(v\), not a division by an element of \(R\).

Here is why this scalar calculation applies to local operator fields. For a fixed input \(\mu\), multiply \(A(s)B(t)C(z)\mu\) by a product
\[
 (s-t)^a(s-z)^b(t-z)^c
\]
of pairwise locality factors. Adjacent locality exchanges show that the resulting numerator is the same for all six orders. Moving each of the three fields to the rightmost position gives a lower bound in its variable from its action on \(\mu\); polynomial locality factors shift those bounds only finitely. The common numerator therefore belongs to
\(M[[s,t,z]][s^{-1},t^{-1},z^{-1}]\).
Each original ordered product is its indicated iterated Laurent expansion after division by the locality factors. These divisions are unique in the corresponding iterated Laurent space.

For two fields, the difference of the two expansions in (PV.2) has residue exactly at \(s=t\). Indeed take partial fractions in \(s\); the polynomial and \(s^{-a}\) parts have equal residues in the two expansions, and a term \(\beta_b(t)(s-t)^{-b}\) contributes only \(\beta_1(t)\). This verifies the residue interpretation directly, without a contour theorem. For three fields, set \(u=s-z\), \(v=t-z\), and apply (PV.3) to the common numerator divided by the locality factors, multiplied by
\[
 u^m(u-v)^p v^q.
\]
The individual-variable poles at \(s=0,t=0\) are regular Taylor units near \(s=t=z\); their coefficients lie in the Laurent series in \(z\). The only remaining local poles are those of (PV.3). At each coefficient the finite numerator-jet argument just given applies.

In the diagonal residue expand \(u^m=((u-v)+v)^m\). In the first successive residue expand
\((u-v)^p=\sum_i(-1)^i\binom pi u^{p-i}v^i\).
In the second expand
\((u-v)^p=(-1)^p\sum_i(-1)^i\binom pi v^{p-i}u^i\).
Consequently
\[
 \begin{aligned}
 &\sum_{i\geq0}\binom mi
             (A_{(p+i)}B)_{(m+q-i)}C\\
 &\quad=\sum_{i\geq0}(-1)^i\binom pi
   \left(A_{(m+p-i)}(B_{(q+i)}C)
          -(-1)^p B_{(p+q-i)}(A_{(m+i)}C)\right).
 \end{aligned}
 \tag{PV.4}
\]
This holds for all integers \(m,p,q\). Each sum of field products is finite: on the left \(A_{(p+i)}B\) vanishes for sufficiently large \(i\) by locality; on the right the indicated positive products with \(C\) do so. The signs and generalized binomial coefficients are precisely the three expansions above. For an actual operator coefficient, first take the common cutoffs for the input and the finite family of intermediate states. Thus (PV.4) is proved as a residue identity on every smooth module, not introduced as a vertex-algebra axiom.

**State products and their universal targets.** On the source vacuum write
\(Y(a,z)=\sum_{j\in\mathbb Z}a_{(j)}z^{-j-1}\).
Creation, translation and current-local uniqueness were proved in (VC.9)–(VC.10): \(Y(a,z)v=e^{zT}a\),
\([T,Y(a,z)]=\partial_zY(a,z)\), and a field local with all currents and zero on \(v\) is zero. These facts hold over \(S\) by the same finite word proofs.

First locality and translation give state skew symmetry:
\[
 Y(a,z)b=e^{zT}Y(b,-z)a.
 \tag{PV.5}
\]
For a proof, apply the locality relation for \(Y(a,s),Y(b,t)\) to \(v\), use creation, and commute the translation exponential through each field by the coefficientwise identity following from \([T,Y]=\partial Y\). Put \(u=s-t\). After multiplication by \(u^L\), with \(L\) large enough for both state Laurent bounds, the relation becomes
\[
 u^Le^{tT}Y(a,u)b=u^Le^{(t+u)T}Y(b,-u)a.
\]
Both sides are now regular in \(u\). Setting \(t=0\) and cancelling the Laurent monomial \(u^L\) proves (PV.5). All exponentials are source-state power series, with an algebraic state at each coefficient.

Next let \(F=Y(a)_{(p)}Y(b)\). The two terms of \(F(z)v\), after creation and translation, are the two indicated expansions of
\(e^{zT}(s-z)^pY(a,s-z)b\), by (PV.5).
For an integer \(d\),
\[
 \operatorname{Res}_s\bigl(
   \iota_{s,z}(s-z)^d-\iota_{z,s}(s-z)^d\bigr)
   =\delta_{d,-1}.
\]
For \(d\geq0\) the expansions coincide; for \(d<-1\) their difference is a derivative of the delta distribution with zero residue; for \(d=-1\) the geometric expansions have residue one. Only finitely many negative powers occur in \(Y(a,u)b\). Extracting the residue gives
\(F(z)v=e^{zT}a_{(p)}b\).
The field \(F\) is local with currents by product closure, so current-local uniqueness proves
\[
 Y(a_{(p)}b,z)=\bigl(Y(a)_{(p)}Y(b)\bigr)(z)
                     \qquad(p\in\mathbb Z).
 \tag{PV.6}
\]
This is a proof on the source vacuum. We now extend it to arbitrary targets by an independent residue induction.

For the identity state, (PV.2) gives
\(\operatorname{Id}_{(p)}F=\delta_{p,-1}F\).
For a current state \(x=x_{-1}v\), (UC.10) gives
\(Y_M(x_{(p)}b)=x(z)_{(p)}Y_M(b)\) for every integer \(p\).
Suppose the full product identity is known for a first argument \(u\), and all second arguments. For \(a=x_{-r}u=x_{(-r)}u\), take \(m=0,p=-r,q=n\) in (PV.4). On the vacuum, (PV.6) and injectivity of \(Y\) give the state identity
\[
 (x_{(-r)}u)_{(n)}b
 =\sum_{i\geq0}(-1)^i\binom{-r}{i}
   \left(x_{(-r-i)}(u_{(n+i)}b)
          -(-1)^r u_{(n-r-i)}(x_{(i)}b)\right).
 \tag{PV.7}
\]
Apply \(Y_M\) and use the induction hypothesis on every \(u\)-product, and the current identity on every \(x\)-product. Formula (PV.4) on \(M\) makes the result precisely
\((x_{(-r)}Y_M(u))_{(n)}Y_M(b)=Y_M(a)_{(n)}Y_M(b)\).
The sums are finite by the positive-product bounds; the generalized negative binomial series has not introduced an infinite state sum. Induction on negative-word length, and linearity, therefore prove
\[
 \boxed{Y_M(a_{(p)}b,z)
       =\bigl(Y_M(a)_{(p)}Y_M(b)\bigr)(z)
       \quad\text{on every smooth }M,\quad p\in\mathbb Z.}
 \tag{PV.8}
\]
No target vacuum or target translation operator was used. The identity is natural in module maps and ordinary coefficient changes, since every residue and coefficient comparison uses the common finite cutoffs of UC.

Expansion of (PV.2) also gives every coefficient of an iterated product:
\[
 (a_{(p)}b)^M_{(q)}
 =\sum_{i\geq0}(-1)^i\binom pi
   \left(a^M_{(p-i)}b^M_{(q+i)}
              -(-1)^p b^M_{(p+q-i)}a^M_{(i)}\right).
 \tag{PV.9}
\]
This is a sum of operators, finite on any specified input: the rightmost positive modes kill that input for large \(i\). Thus (PV.8) includes the full iterate identities, not only nonnegative products.

Locality of \(Y_M(a),Y_M(b)\), (PV.8), and the finite delta expansion proved in UC give
\[
 \boxed{[a^M_{(m)},b^M_{(n)}]
    =\sum_{j\geq0}\binom mj
            (a_{(j)}b)^M_{(m+n-j)}
                \qquad(m,n\in\mathbb Z).}
 \tag{PV.10}
\]
Its delta residues are exactly \(Y_M(a_{(j)}b)\) by (PV.8). The upper support is a locality bound, independent of \(m,n\). Negative \(m\) uses generalized binomial coefficients. The same formula on the source vacuum gives the exact nonnegative-product Jacobi identity
\[
 a_{(m)}(b_{(n)}c)-b_{(n)}(a_{(m)}c)
   =\sum_{j=0}^m\binom mj(a_{(j)}b)_{(m+n-j)}c
                   \quad(m,n\geq0).
 \tag{PV.11}
\]
These are the universal state-product and commutator identities required to compare Fourier brackets later.

**The critical commutative differential algebra.** Put
\[
 Z_R=V_R^{\mathfrak g[[t]]}.
\]
By UC, each critical invariant \(a\) has a field all of whose modes commute with every current, hence with every reconstructed field. Its nonnegative modes vanish on \(V_R\), by creation and cyclicity, as explicitly proved in (UC.21). Therefore
\[
 a_{(j)}u=0,\qquad u_{(j)}a=0
        \quad(a\in Z_R,\ u\in V_R,\ j\geq0).
 \tag{PV.12}
\]
The first equality is this operator vanishing. The second also follows from (PV.5): its coefficient is a finite sum of translates of \(a_{(j+s)}u\), all zero.

The product \(ab=a_{(-1)}b\) is the vacuum image of the composition of the corresponding invariant endomorphisms. Thus it belongs to \(Z_R\), is associative and commutative, and has unit \(v\), by the induction correspondence and the commutativity already proved in VC and UC. Translation preserves invariants:
\(x_jTa=Tx_ja+jx_{j-1}a=0\) for \(j\geq0\), with the \(j=0\) boundary coefficient zero. Moreover
\[
 T(ab)=(Ta)b+a(Tb),\qquad Tv=0.
 \tag{PV.13}
\]
Indeed \([T,a_{(-1)}]=(Ta)_{(-1)}\), from \([T,Y(a)]=\partial Y(a)\). Hence \(Z_R\) is an ordinary commutative differential algebra.

Choose any PBW lifts \(\widetilde a,\widetilde b\in V_S\) of \(a,b\in Z_R\). By (PV.12), their nonnegative products reduce to zero, and therefore uniquely have the form
\[
 \widetilde a_{(j)}\widetilde b=\varepsilon h_j,
 \qquad j\geq0,\qquad h_j\in V_S.
\]
Define
\[
 \boxed{\{a_\lambda b\}_B
   =\sum_{j\geq0}\frac{\lambda^j}{j!}\,
       \overline h_j
   =\left.\frac1\varepsilon
          [\widetilde a_\lambda\widetilde b]_\varepsilon
     \right|_{\varepsilon=0},\qquad
 [u_\lambda v]_\varepsilon=\sum_{j\geq0}
                      \frac{\lambda^j}{j!}u_{(j)}v.}
 \tag{PV.14}
\]
The sum is a polynomial by locality. Multiplication by \(\varepsilon\) is injective in the free PBW module, so the division is defined without a torsion choice.

Changing \(\widetilde a\) by \(\varepsilon u\) changes its quotient at order zero by \(u_{(j)}b=0\); changing \(\widetilde b\) by \(\varepsilon w\) changes it by \(a_{(j)}w=0\). The simultaneous change has an additional \(\varepsilon^2u_{(j)}w\) before division, which also disappears. This proves independence of all PBW lifts, and \(R\)-bilinearity.

We must also prove that every \(\overline h_j\) is central. Fix a physical current \(x_m\), \(m\geq0\). Write
\(x_\ell\widetilde a=\varepsilon u_\ell\) for \(\ell\geq0\) and
\(x_m\widetilde b=\varepsilon v_m\).
The universal current commutator (UC.14), applied on the source family, gives
\[
 \left.x_mh_j\right|_0
  =\sum_{\ell=0}^m\binom m\ell
           (u_\ell|_0)_{(j+m-\ell)}b
               +a_{(j)}(v_m|_0)=0.
 \tag{PV.15}
\]
Every index \(j+m-\ell\) is nonnegative, so the first terms vanish by the second-slot equality of (PV.12); the last term vanishes by its first-slot equality. Thus
\(\overline h_j\in Z_R\). Smoothness handles formal nonnegative currents. This establishes closure without presuming that the lifts themselves are central away from \(\varepsilon=0\).

**Sesquilinearity and skew symmetry.** Translation of the state fields gives
\[
 (Ta)_{(j)}b=-j\,a_{(j-1)}b,\qquad
 a_{(j)}Tb=T(a_{(j)}b)+j\,a_{(j-1)}b.
\]
These exact family identities follow respectively from \(Y(Ta)=\partial Y(a)\) and \([T,a_{(j)}]=-j a_{(j-1)}\). Division by \(\varepsilon\) and coefficient collection prove
\[
 \boxed{\{Ta_\lambda b\}=-\lambda\{a_\lambda b\},\qquad
 \{a_\lambda Tb\}=(T+\lambda)\{a_\lambda b\}.}
 \tag{PV.16}
\]
Taking the coefficient \(z^{-j-1}\) in (PV.5) gives
\[
 a_{(j)}b=\sum_{r\geq0}
       \frac{(-1)^{j+r+1}}{r!}\,T^r(b_{(j+r)}a).
\]
The positive-product support makes this finite for \(j\geq0\).
Consequently
\[
 \boxed{\{a_\lambda b\}=-\{b_{-\lambda-T}a\}.}
 \tag{PV.17}
\]
The substitution on the right means that powers of \(T\) act on the resulting coefficients, not on the input \(a\) before forming the bracket. To check the collection explicitly, the coefficient of \(\lambda^j/j!\) in
\(-\sum_q(-\lambda-T)^q h_q/q!\)
is exactly the preceding translated coefficient formula.

**Jacobi, with the second-order division justified.** Formula (PV.11) holds in \(V_S\). For central \(a,b,c\), every inner nonnegative product of their lifts is \(\varepsilon\) times a state whose reduction is central, by (PV.15). Its outer nonnegative product with another central lift is therefore divisible by a further \(\varepsilon\). Both sides of (PV.11) are divisible by \(\varepsilon^2\). Divide by \(\varepsilon^2\), then specialize:
\[
 \{a_\lambda\{b_\mu c\}\}
  -\{b_\mu\{a_\lambda c\}\}
       =\{\{a_\lambda b\}_{\lambda+\mu}c\}.
 \tag{PV.18}
\]
For a direct coefficient check, the coefficient of
\(\lambda^m/m!\,\mu^n/n!\) on the right is
\(\sum_{j=0}^m\binom mj
 \{\overline h_j{}_{\,m+n-j}c\}\)
in mode notation: expanding \((\lambda+\mu)^{m+n-j}\) gives the factor
\(m!/(j!(m-j)!)\). This is exactly (PV.11) after the two divisions. Inner-bracket lift independence permits the particular quotients \(h_j\) used here. Injectivity of \(\varepsilon^2\) makes the division unambiguous. Thus Jacobi has been proved, not deduced from a presumed Poisson vertex axiom.

**The exact Wick identity and first-order Leibniz.** For arbitrary states in the family, the commutator (PV.10) gives, for \(m\geq0\),
\[
 a_{(m)}(b_{(-1)}c)
  =b_{(-1)}(a_{(m)}c)
       +(a_{(m)}b)_{(-1)}c
       +\sum_{j=0}^{m-1}\binom mj
                        (a_{(j)}b)_{(m-j-1)}c.
 \tag{PV.19}
\]
Multiply by \(\lambda^m/m!\) and sum. In the last term put
\(q=m-j-1\); its coefficient is
\(\lambda^{j+q+1}/(j!(q+1)!)\).
We obtain the full noncommutative Wick identity
\[
 \begin{aligned}
 [a_\lambda(b_{(-1)}c)]_\varepsilon
 &=([a_\lambda b]_\varepsilon)_{(-1)}c
      +b_{(-1)}[a_\lambda c]_\varepsilon\\
 &\quad+\int_0^\lambda
                  [[a_\lambda b]_\varepsilon{}_\mu c]_\varepsilon\,d\mu .
 \end{aligned}
 \tag{PV.20}
\]
The integral is the formal polynomial antiderivative with zero constant. It follows from the displayed factorial coefficients and needs no analytic integration. This derivation retains every nonnegative-product correction.

Use the lift \(\widetilde b_{(-1)}\widetilde c\) of \(bc\), which is permitted by lift independence. For central reductions,
\([\widetilde a_\lambda\widetilde b]_\varepsilon=\varepsilon h(\lambda)\)
and \(h(\lambda)|_0\) is central. Thus the integrand of the correction in (PV.20) is
\[
 \varepsilon[h(\lambda)_\mu\widetilde c]_\varepsilon
                           \in\varepsilon^2V_S[\lambda,\mu].
 \tag{PV.21}
\]
This is the required first-order correction cancellation. Division of (PV.20) by \(\varepsilon\), followed by specialization, gives
\[
 \boxed{\{a_\lambda bc\}=\{a_\lambda b\}c+b\{a_\lambda c\}.}
 \tag{PV.22}
\]
Skew symmetry and (PV.16) also give the left Leibniz rule
\[
 \{ab_\lambda c\}
   =\{a_{\lambda+T}c\}_{\to}b
                      +\{b_{\lambda+T}c\}_{\to}a,
\]
where the shifted \(T\)'s act on the factor to their right. For an explicit verification, apply (PV.17) to \(\{ab_\lambda c\}\), apply (PV.22) to \(\{c_\nu ab\}\), then substitute \(\nu=-\lambda-T\). Expanding each shifted power by the binomial theorem and using
\(T^r(xy)=\sum_s\binom rs(T^sx)(T^{r-s}y)\)
moves the derivatives between its coefficient and the right factor. The resulting two expressions are precisely the arrow convention above.

We have proved that
\[
 \boxed{(Z_R,\;ab=a_{(-1)}b,\;v,\;T,\;\{\,{}_\lambda\,\}_B)}
 \tag{PV.23}
\]
is a Poisson vertex algebra: a commutative associative unital differential algebra with a polynomial \(\lambda\)-bracket satisfying sesquilinearity, skew symmetry, Jacobi and Leibniz. Its unit has zero bracket because the identity field has no nonnegative products. Every step used explicit field residues or finite PBW division.

All of this commutes with ordinary coefficient maps \(R\to R'\). PBW makes the level family free, reconstruction and residue identities are finite at every specified coefficient, and \(\varepsilon\)-division is coefficient shifting in that free module. Invariance over \(R\) is obtained from the finite current equations on each source energy space over \(k\); tensoring over the field preserves their kernels. Thus the stated \(Z_R\) and its operations are the ordinary extension of the critical state algebra, including for nonreduced \(R\). No derived coefficient or completed tensor product has been substituted.

**Fourier brackets and the precise completion boundary.** Let \(a,b\in Z_R\) be homogeneous of source energies \(D_a,D_b\), and write
\[
 Y_M(a,z)=\sum_n S^M_{a,n}z^{-n-D_a},\qquad
 \{a_\lambda b\}=\sum_{j\geq0}\frac{\lambda^j}{j!}h_j.
\]
The coefficient \(h_j\) has energy \(D_a+D_b-j-1\); a negative energy means it is zero. Lift \(a,b\) in the level family and use (PV.10) on every smooth level-family target, or equivalently on its universal cutoff modules. The unique first-order commutator quotient is
\[
 \boxed{\{S_{a,n},S_{b,m}\}_{\mathrm{completed}}
   =\sum_{j\geq0}\binom{n+D_a-1}{j}
                          S_{h_j,n+m}.}
 \tag{PV.24}
\]
Indeed the ordinary field indices are \(n+D_a-1\) and \(m+D_b-1\); after subtracting the energy of \(h_j\), its normalized index is exactly \(n+m\). Scalar states use the weight-zero convention
\(S_{v,q}=\delta_{q,0}\operatorname{Id}\).
The sum over \(j\) is finite. Formula (PV.8) on every smooth module is what identifies its right side with universal Fourier coefficients; a source-vacuum check alone would not suffice.

The completed bracket in (PV.24) is the first-order associative-commutator construction of §3.7.5. That section supplies the stage-compatible PBW lifting, saturated division, completed algebra and continuity argument. Here we have proved its correspondence with the intrinsic \(\lambda\)-bracket for every pair of state Fourier generators and hence for their polynomial algebra. We do not declare the fixed cutoff quotients Poisson algebras: negative mode indices can carry a high mode back below a cutoff in (PV.24). Continuity of the full completed bracket requires the completed construction just specified, rather than quotienting this formula by a presumed Poisson cutoff ideal.

In general, restriction of the completed ordinary centre to
\(\operatorname{End}(V_{\mathrm{crit}})\) is not a Poisson quotient. For a deformation direction with a nonzero quadratic bracket, a Fourier mode may vanish on that vacuum, by (UC.21), while its bracket with a negative mode restricts nontrivially; §3.7.5 gives the quadratic example. The PVA (PV.23) concerns state products and the translation-labelled \(\lambda\)-bracket. It does not arise by imposing the vacuum's forbidden-mode relations as Poisson relations.

The two mechanisms are displayed below:
\[
 \begin{array}{ccc}
 \widetilde a_{(j)}\widetilde b
       =\varepsilon h_j
 &\xrightarrow{\ /\varepsilon,\;\varepsilon=0\ }&
                   h_j|_0\in Z_R\\[2pt]
 \text{(PV.8), every smooth }M\downarrow
 &&\downarrow\text{(PV.24)}\\[2pt]
 [\widetilde S_{a,n},\widetilde S_{b,m}]
 &\xrightarrow{\ /\varepsilon,\;\varepsilon=0\ }&
 \displaystyle\sum_j\binom{n+D_a-1}{j}S_{h_j,n+m}.
 \end{array}
\]
*The upper arrow defines the intrinsic PVA coefficient (PV.14).
The lower arrow uses the independent completed commutator construction.
The vertical correspondence is the universal product and commutator
identity (PV.8)–(PV.10), with all integer indices and finite locality
support. The Wick double product (PV.21) explains first-order Leibniz.
The square is a correspondence of bracket coefficients; it is not a
claim that a cutoff quotient or vacuum restriction is Poisson.*

This establishes the intrinsic critical PVA and the universal Fourier formula. Identifying it with a specified oper or Drinfeld–Sokolov Poisson structure, including its normalization and all geometric reduction premises, remains a separate comparison theorem. Neither the ordinary oper-coordinate algebra isomorphism nor coordinate equivariance alone proves that Poisson comparison.

#### 3.7.2. The ordered Miura map and its exact injectivity

We first construct the algebraic Miura map. Its Poisson property is a separate assertion, proved by the affine deformation comparison in §3.7.4 together with §3.7.3. Let \(\mathfrak g=\mathfrak{gl}_n\), or \(\mathfrak{sl}_n\), with the forms and determinant states already proved in §3.3.5. Positive finite roots are the matrix units \(E_{ab}\), \(a<b\). Put
\[
\ell=\mathfrak g\otimes t^{-1}k[t^{-1}],\qquad
\ell_-=\mathfrak n_-\otimes t^{-1}k[t^{-1}],\quad
\ell_h=\mathfrak h\otimes t^{-1}k[t^{-1}],\quad
\ell_+=\mathfrak n_+\otimes t^{-1}k[t^{-1}].
\tag{MC.1}
\]
The PBW proof preceding (K2.3) identifies the vacuum as a module with \(U(\ell)\), by its value on the vacuum vector. Order lower-root letters first, diagonal letters next and upper-root letters last. PBW gives the vector-space decomposition
\[
U(\ell)=U(\ell_-)\otimes\operatorname{Sym}(\ell_h)\otimes U(\ell_+).
\tag{MC.2}
\]
There is no scalar bracket among negative modes. In particular the diagonal negative modes commute. The zero diagonal modes act on (MC.2) by their finite root weights. Let \(U(\ell)^0\) be the subalgebra of weight zero, and let \(\operatorname{HC}\) be projection to its all-diagonal PBW summand.

We prove exactly why this projection is multiplicative on weight zero. A positive root \(\epsilon_a-\epsilon_b\), \(a<b\), is the sum of the consecutive simple roots \(\epsilon_a-\epsilon_{a+1},\ldots,\epsilon_{b-1}-\epsilon_b\). The cone of their nonnegative combinations is pointed: a nonempty sum of positive roots cannot be zero, by comparing its coefficients in the simple-root basis. A weight-zero PBW monomial therefore either is entirely diagonal or has both a nonempty lower-root block and a nonempty upper-root block. Consequently
\[
\ker(\operatorname{HC}|_{U(\ell)^0})
=U(\ell)^0\cap\ell_-U(\ell)
=U(\ell)^0\cap U(\ell)\ell_+.
\tag{MC.3}
\]
Here \(\ell_-U(\ell)\) is the right ideal whose generator is at the left, and \(U(\ell)\ell_+\) is the left ideal whose generator is at the right. Their PBW spans are respectively the monomials with a nonempty lower or upper block: reordering lower letters among themselves, or upper letters among themselves, keeps a letter in that root cone. If \(a\) lies in the kernel and \(b\) has weight zero, the right-ideal description puts \(ab\) in the kernel and the left-ideal description puts \(ba\) in it. Hence the kernel is a two-sided ideal in the weight-zero subalgebra. The quotient is precisely \(\operatorname{Sym}(\ell_h)\), with its usual multiplication. This proves
\[
\operatorname{HC}:U(\ell)^0\longrightarrow\operatorname{Sym}(\ell_h)
\quad\text{is a unital algebra homomorphism.}
\tag{MC.4}
\]
It is not asserted to be an algebra homomorphism on all of \(U(\ell)\).

Translation is \(T(x_{-a})=a x_{-a-1}\). It preserves all three root blocks, their ideal spans and the all-diagonal summand. The product rule proves
\[
\operatorname{HC}(Ta)=T\operatorname{HC}(a)
\qquad(a\in U(\ell)^0).
\tag{MC.5}
\]
All statements remain valid over every ordinary \(k\)-algebra \(R\). Indeed the PBW monomials are free over \(R\). A nonzero finite weight has a nonzero value on some diagonal element over \(k\); this value is a unit in every nonzero \(R\). Thus being killed by all diagonal zero modes removes exactly the nonzero weight summands, including over rings with nilpotents. The same coefficient and ideal proofs establish (MC.3)–(MC.5) over \(R\).

Every invariant vacuum state has weight zero. Identify it with its unique negative-mode representative \(a\in U(\ell)\). The product of invariant states is endomorphism composition, as in (K2.3) and (VC.19). If their representatives are \(a,b\), its vacuum value is \(ba v\): the endomorphism with value \(a v\) commutes with the currents used to form \(b v\). Equations (MC.4)–(MC.5) therefore give a homomorphism of commutative differential algebras
\[
\nu_R:Z^{\mathrm{vac}}_{\mathrm{crit},R}
 \longrightarrow \operatorname{Sym}_R(\ell_{h,R}),
\qquad a v\longmapsto\operatorname{HC}(a).
\tag{MC.6}
\]
The target is commutative, so reversing the order in \(ba\) makes no difference. The affine critical form restricted to the source Cartan is generally nonzero. Equation (MC.6) is a differential-algebra map into diagonal negative variables; it has not identified the source affine Cartan vertex algebra with a zero-form boson vertex algebra.

Write \(h_a=E_{aa}[-1]\) in the raw matrix case, and \(h_a=F_{aa}[-1]\) with \(\sum_a h_a=0\) in the traceless case. Extend (MC.4) to the weight-zero Ore algebra by keeping \(\tau\), where \(\tau c=c\tau+Tc\). This extension is well defined by (MC.5). The column determinant obeys the exact identity
\[
\operatorname{HC}\!\left(\operatorname{cdet}(\delta_{ab}\tau+E_{ab}[-1])\right)
=(\tau+h_1)(\tau+h_2)\cdots(\tau+h_n).
\tag{MC.7}
\]
To prove it, each permutation term has weight zero. For a nonidentity permutation \(\pi\), let \(j\) be its first nonfixed column. Its preceding columns are fixed, so \(\pi(j)>j\). The factor at column \(j\) is the lower-root letter \(E_{\pi(j),j}[-1]\). Moving it to the left through the preceding diagonal and \(\tau\) factors gives only lower-root letters: a diagonal commutator preserves its root, and a \(\tau\) commutator differentiates its negative mode. Thus the whole term belongs to the kernel in (MC.3), including every derivative term. Only the identity permutation remains, giving the displayed ordered product. Passing to the trace-zero quotient gives the same formula with \(E\) replaced by \(F\). This argument explains the order; it is not a commutative determinant substitution.

Define the differential polynomials \(M_i\) by right-ordering that product:
\[
(\tau+h_1)\cdots(\tau+h_n)
=\tau^n+\sum_{i=1}^n M_i(h)\tau^{n-i}.
\tag{MC.8}
\]
Their first two terms are
\[
M_1=\sum_a h_a,\qquad
M_2=\sum_{a<b}h_ah_b+\sum_{a=1}^n(a-1)Th_a.
\tag{MC.9}
\]
For the second identity, a product choosing two diagonal factors contributes the first sum. Choosing one diagonal factor in position \(a\), with one of its \(a-1\) earlier derivatives acting on it, contributes \((a-1)Th_a\). All remaining derivatives move to the right. This exhausts the terms of differential order \(n-2\). At \(n=2\), it gives \(h_1h_2+Th_2\); the derivative on the second factor fixes the Miura convention.

For each \(a\), let
\(H_a(t)=\sum_{r\ge0}h_{a,-r-1}t^r\). Translation gives this as \(e^{tT}h_a\), and the product rule says that \(e^{tT}\) is a differential-algebra homomorphism, coefficient by coefficient. Hence (MC.7)–(MC.8) imply
\[
\nu_R(A_{i,r})=[t^r]M_i(H(t),H'(t),\ldots)
=\frac{T^rM_i(h)}{r!}.
\tag{MC.10}
\]
There are finitely many differentiated variables in each such coefficient. In the traceless case \(M_1=0\), and the list starts at \(i=2\).

We prove independence on the diagonal jets directly. Choose distinct \(\lambda_1,\ldots,\lambda_n\in k\), with sum zero when needed. Such a choice exists explicitly: \(\lambda_a=a-(n+1)/2\). The differential of the characteristic-coefficient map at these constants is invertible. Indeed if every coefficient of
\[
\sum_a\delta\lambda_a\prod_{b\ne a}(u+\lambda_b)
\tag{MC.11}
\]
vanishes, evaluating at \(u=-\lambda_a\) gives
\(\delta\lambda_a\prod_{b\ne a}(\lambda_b-\lambda_a)=0\), so every variation vanishes. In the trace-zero case the missing first coefficient is already zero because \(\sum_a\delta\lambda_a=0\); thus the differential of \(e_2,\ldots,e_n\) on that hyperplane is an invertible square matrix too.

At jets of order at most \(q\), take constant terms \(\lambda_a\) and all higher terms zero. The differential of
\[
(H_{a,0},\ldots,H_{a,q})_a
\longmapsto(e_i(H)_0,\ldots,e_i(H)_q)_i
\tag{MC.12}
\]
is block diagonal, with that same invertible matrix at each order. This already proves algebraic independence without an unproved dominance theorem. If a nonzero polynomial relation existed, translate its variables by the values at this point and take its least nonzero homogeneous part. Formal substitution in the input variations has invertible linear part (MC.12); the least homogeneous part of the composite is the original nonzero part composed with an invertible linear map. It cannot vanish. This contradicts the proposed relation. Every relation uses a finite jet order, so all the characteristic coefficients are independent. Tensoring the resulting injection of \(k\)-vector spaces proves the same independence over every ordinary \(R\).

Each \(M_i\) has letter degree at most \(i\) and top letter-degree part \(e_i(h_1,\ldots,h_n)\). A derivative does not change letter degree, whereas a term containing derivatives in (MC.8) uses fewer than \(i\) diagonal letters. Therefore the top parts of (MC.10) are exactly the independent coefficients in (MC.12). A nonzero polynomial in the \(A_{i,r}\) has a nonzero highest part for the weights \(\deg A_{i,r}=i\). Its image under \(\nu_R\) has that highest part evaluated in the independent characteristic coefficients, and is nonzero. The full polynomial vacuum theorem (SL.C1), or (TR.19) in the raw matrix case, now proves
\[
\nu_R\text{ is injective on the entire type A vacuum center.}
\tag{MC.13}
\]
No reduced-point test over \(R\) replaces this free polynomial argument.

There is an equally precise completed Miura injection. Let
\[
\mathcal H_{N,R}=R[h_{a,m}:m<N],\qquad
\widehat{\mathcal H}_R=\varprojlim_{N\ge1}\mathcal H_{N,R},
\tag{MC.14}
\]
imposing \(\sum_a h_{a,m}=0\) at each mode in the traceless case. These are the zero-form abelian completed coefficient algebras of (HC.8). Define
\(H_a(z)=\sum_{m\in\mathbb Z}h_{a,m}z^{-m-1}\) and right-order the product \(\prod_{a=1}^n(\partial_z+H_a(z))\). Denote its \(i\)-th coefficient mode by \(M_{i,m}\), using exponent \(-m-i\).

Every term in that coefficient has \(q\le i\) diagonal factors and total current index \(m\). The derivatives account for the remaining weight \(i-q\); the exponent of the term is therefore \(-m-i\), exactly as in (UC.17). Modulo the cutoff, all current indices are less than \(N\), and each is at least \(m-(q-1)(N-1)\). Thus a coefficient is a finite polynomial. If \(m>i(N-1)\), no index tuple survives. Its leading letter-degree part for an allowed index is
\([z^{-m-i}]e_i(H(z))\).
To see independence of all these allowed top parts, rescale the Laurent diagonal series to \(z^NH_a(z)\). Homogeneity turns their coefficient list into every nonnegative characteristic coefficient of these regular series. The finite-jet proof (MC.11)–(MC.12) applies unchanged.

It follows by highest weighted degree, exactly as for (MC.13), that every stage map
\[
R[S_{i,m}:m\le i(N-1)]\longrightarrow\mathcal H_{N,R},
\qquad S_{i,m}\longmapsto M_{i,m},
\tag{MC.15}
\]
is injective. Setting newly admitted positive diagonal modes to zero sends each coefficient to its coefficient at the smaller cutoff; all disallowed \(M_{i,m}\) then vanish exactly. The maps are compatible. Taking the inverse limit and using the proved full completed center (CT.4) gives
\[
\widehat\nu_R:Z(\widehat A_{\mathrm{crit},R})
\hookrightarrow\widehat{\mathcal H}_R,
\qquad S_{i,m}\longmapsto M_{i,m}.
\tag{MC.16}
\]
Injectivity holds stage by stage. Its inverse on its image is continuous as well: by (MC.15), the inverse image of the target cutoff kernel is exactly the corresponding center cutoff kernel. This proves a topological algebra embedding, without a global PBW degree bound. The construction and the proof commute with every ordinary coefficient extension in the completed sense of (CW.19) and (CT.21).

Setting every nonnegative diagonal mode to zero makes each \(H_a(z)\) regular. Its differentiated coefficient polynomials are regular too, so their modes with \(m>-i\) vanish. The remaining coefficient is exactly (MC.10). Thus the completed and regular injections give the square
\[
\begin{array}{ccc}
Z(\widehat A_{\mathrm{crit},R})
&\xrightarrow{\ \widehat\nu_R\ }&\widehat{\mathcal H}_R\\
\downarrow&&\downarrow{\scriptstyle h_{a,m}=0\ (m\ge0)}\\
Z^{\mathrm{vac}}_{\mathrm{crit},R}
&\xrightarrow{\ \nu_R\ }&R[h_{a,-r-1}:r\ge0].
\end{array}
\tag{MC.17}
\]
*The ordered product (MC.7) supplies the lower map, including its derivative terms. Exact mode cutoffs and the independent highest symbols supply the upper map (MC.16). The vacuum creation formula (PC.14) identifies the left restriction. This is a square of topological or ordinary commutative algebras, respectively. Its construction alone asserts no Poisson quotient on the vertical arrows.*

**The density shift and coordinate equivariance.** The diagonal target has an affine coordinate action appropriate to its ordered factors. Put
\[
b=\frac{1-n}{2},\qquad d_a=b+n-a=\frac{n+1}{2}-a,
\qquad \rho_a=-d_a=a-\frac{n+1}{2}.
\tag{MC.18}
\]
The factor in position \(a\), counted from the left, maps densities of weight \(d_a\) to densities of weight \(d_a+1\). Thus adjacent weights agree and the product maps weight \(b\) to weight \(b+n\). Let \(\psi=\phi^{-1}\), \(\alpha=\psi'\), and \(C_\psi f=f\circ\psi\). Direct multiplication gives
\[
\begin{aligned}
\alpha^{d_a+1}C_\psi(\partial+H_a)C_\psi^{-1}\alpha^{-d_a}
&=\alpha^{d_a+1}(\alpha^{-1}\partial+H_a\circ\psi)\alpha^{-d_a}\\
&=\partial+\alpha H_a\circ\psi+\rho_a\frac{\alpha'}{\alpha}.
\end{aligned}
\tag{MC.19}
\]
For half-integer weights use the free rank-two square-root extension and sign-independent descent proved in (SC.O4)–(SC.O6). The final coefficient formula has no square root. It defines the action
\[
\sigma_\phi^\rho H_a(t)
=\psi'(t)H_a(\psi(t))
 +\rho_a\frac{\psi''(t)}{\psi'(t)}.
\tag{MC.20}
\]
The derivative \(\psi'\) is a unit and its logarithmic derivative is regular. The substitution and inverse exist also for nilpotent constant terms by the formal-coordinate proof already used in (PC.8). The first summand has exactly the cofinal cutoff bounds of the Laurent one-form action (HC.12); the second is a fixed regular scalar series. Consequently each coefficient is finite modulo a sufficiently high cutoff, and (MC.20) defines a continuous automorphism of \(\widehat{\mathcal H}_R\). The chain rule
\[
\frac{(F\circ G)''}{(F\circ G)'}
=G'\left(\frac{F''}{F'}\circ G\right)+\frac{G''}{G'}
\]
proves composition and the inverse law. Since \(\sum_a\rho_a=0\), the trace transforms as an ordinary Laurent one-form, so its zero relation is preserved.

In the product of (MC.19), the intermediate powers of \(\alpha\) cancel because \(d_a=d_{a+1}+1\). Its result is exactly
\[
\prod_a(\partial+\sigma_\phi^\rho H_a)
=\alpha^{b+n}C_\psi L C_\psi^{-1}\alpha^{-b},
\qquad L=\prod_a(\partial+H_a).
\tag{MC.21}
\]
This is the scalar-oper density transport (SC.O6), including all lower derivative corrections. The full center/scalar coefficient comparison (PC.13) therefore gives
\[
\widehat\nu_R\,\sigma_\phi
=\sigma_\phi^\rho\,\widehat\nu_R.
\tag{MC.22}
\]
The equality holds first on every basic coefficient, by (MC.21) and (PC.13), then on the dense polynomial algebra and its completion by continuity. The shift in (MC.20) is essential: separate unshifted one-form transformations do not give the density transport of the ordered product. Infinitesimally, \(\psi=t-\epsilon v\) gives
\(\delta_vH_a=-vH_a'-v'H_a-\rho_av''\).
For \(n=2\), \(H_1=-u,H_2=u\), this gives
\(\delta_vu=-vu'-v'u-v''/2\) and
\[
\delta_v(u'-u^2)=-v(u'-u^2)'-2v'(u'-u^2)-v'''/2.
\]

The same action preserves the free-boson Poisson bracket when that bracket is placed on the target, independently of whether \(\widehat\nu_R\) is Poisson. Indeed linear residue functionals have bracket
\[
\{\operatorname{Res}fH_a\,dt,\operatorname{Res}gH_c\,dt\}
=P_{ac}\operatorname{Res}f'g\,dt,
\quad P_{ac}=\delta_{ac}\text{ or }\delta_{ac}-1/n.
\tag{MC.23}
\]
Under (MC.20) the functional is the one with test function \(f\circ\phi\), plus a scalar. Scalars have zero bracket; residue substitution gives
\(\operatorname{Res}(f\circ\phi)'(g\circ\phi)dt=\operatorname{Res}f'g\,dt\).
The finite-cutoff substitution arguments justify this identity with nilpotent translations as well. Leibniz and the continuous completed bracket of §3.7.5 extend it from linear coefficients to the completed target. This establishes the coordinate Poisson action itself, without deducing an affine-center comparison from it.

Products of type A factors use the componentwise lists and one common cutoff. The zero Lie algebra gives the coefficient ring, and the rank-one abelian raw matrix case gives \(L=\partial+H_1\) and the identity coefficient map. Extra zero-form reductive central directions are already independent linear Laurent one-form variables by (HC.8) and (CF.12). This proves the entire algebraic and completed Miura coefficient embedding and its affine density coordinate action in the stated type A scope. Establishing that it preserves the critical Poisson bracket requires the deformation and affine-to-boson comparison, not only these determinant and independence calculations.

#### 3.7.3. The Miura product and the scalar Adler–Gelfand–Dickey bracket

Let \(k\) be a characteristic-zero field and \(R\) any ordinary commutative \(k\)-algebra. Take \(n\ge1\) in the raw matrix calculation and \(n\ge2\) in the trace-zero calculation. All identities below are polynomial identities over \(k\), hence hold over nonreduced \(R\) as well. Write \(\partial\) for the differential-algebra derivation and for its corresponding differential-operator symbol, distinguished by context. Start with the differential polynomial algebra on \(h_1,\ldots,h_n\), and the brackets
\[
\begin{aligned}
\{h_i{}_{\lambda}h_j\}&=P_{ij}\lambda,\\
P_{ij}&=\delta_{ij}\quad\text{in the raw matrix case},\\
P_{ij}&=\delta_{ij}-\frac1n\quad\text{in the trace-zero case}.
\end{aligned}
\tag{AP.1}
\]
The normalized trace-zero scalar operator will have no \(\partial^{n-1}\) term. We prove its entire bracket from (AP.1), including its Dirac term and its sign. This is a calculation on scalar operators and free bosons; it does not assert that any affine center map is Poisson.

**The differential polynomial bracket.** Put \(h_i^{(r)}=\partial^rh_i\). There is a unique bracket with (AP.1), sesquilinearity
\(\{\partial f{}_{\lambda}g\}=-\lambda\{f{}_{\lambda}g\}\) and
\(\{f{}_{\lambda}\partial g\}=(\lambda+\partial)\{f{}_{\lambda}g\}\), and the two Leibniz rules. Its explicit finite formula is
\[
\{f{}_{\lambda}g\}
=\sum_{i,j,a,b}
 \frac{\partial g}{\partial h_j^{(b)}}
 (\lambda+\partial)^b P_{ij}(\lambda+\partial)
 (-\lambda-\partial)^a
 \frac{\partial f}{\partial h_i^{(a)}}.
\tag{AP.2}
\]
Every displayed \(\partial\) acts on all factors to its right. Finiteness follows because \(f,g\) are differential polynomials. Repeated Leibniz and sesquilinearity give (AP.2), so they also give uniqueness. Symmetry of \(P\) gives skewsymmetry on generators, and its extension follows by those same rules. The Jacobiator is a derivation in its third entry; skewsymmetry gives the corresponding shifted Leibniz rules in its first two entries. Sesquilinearity handles derivatives. Induction on the numbers of factors and derivatives therefore reduces Jacobi to three undifferentiated generators. There it is zero because their brackets are central constants times \(\lambda\). Thus (AP.2) is a Poisson vertex bracket without an imported reduction theorem.

For a local functional write \(\int f\) for the class of \(f\) modulo \(\partial\)-derivatives. Our Hamiltonian convention is that the flow of \(\int f\) on a generator is
\(\delta_fh_i=\sum_jP_{ij}\partial(\delta f/\delta h_j)\).
Equivalently the Hamiltonian matrix of \(\{u_j{}_{\lambda}u_i\}\) sends its test function \(f_j\) to the variation of \(u_i\). This fixes the signs throughout.

Expand the ordered Miura product
\[
A_i=\partial+h_i,\qquad
L=A_1\cdots A_n
 =\partial^n+\sum_{i=1}^ns_i\partial^{n-i},
\qquad s_0=1.
\tag{AP.3}
\]
The ordering matters: for example \(s_2=\sum_{i<j}h_ih_j+\sum_j(j-1)h_j'\). No permutation of these differential factors is used.

**Pseudodifferential multiplication and residue, proved algebraically.** A formal pseudodifferential operator is \(Q=\sum_{p\le p_0}q_p\partial^p\), with a finite upper order. Define
\[
\partial^pf=\sum_{r\ge0}\binom pr f^{(r)}\partial^{p-r},
\qquad
\binom pr=\frac{p(p-1)\cdots(p-r+1)}{r!},
\qquad
\operatorname{res}Q=q_{-1}.
\tag{AP.4}
\]
At every operator coefficient the product is finite: if the two upper orders are \(p_0,q_0\), the condition \(p+q-r=d\) bounds \(p\) and \(q\) from below for fixed \(d\). The symbol product is
\(Q(z)\star U(z)=\sum_r(\partial_z^rQ(z))\partial^rU(z)/r!\).
For three symbols both parenthesizations expand into the identical sum
\[
\sum_{a,b,c\ge0}\frac{
 (\partial_z^{a+b}Q)
 (\partial^a\partial_z^cU)
 (\partial^{b+c}V)}{a!b!c!}.
\]
The ordinary product rule supplies these three pairwise derivative indices. This proves associativity coefficient by coefficient, including negative orders. The generalized binomial formula is exactly the derivative formula for \(z^p\), so it covers every integer \(p\).

Residues are cyclic modulo derivatives, with an explicit primitive. For \(Q=a\partial^p\), \(U=b\partial^q\), put \(r=p+q+1\). If \(r<0\), both residues vanish; if \(r=0\), their difference is zero. For \(r\ge1\), the identity \(\binom qr=(-1)^r\binom pr\) follows by reversing the \(r\) factors, because \(q=r-p-1\). Therefore
\[
\operatorname{res}[a\partial^p,b\partial^q]
=\partial\left[
 \binom pr\sum_{v=0}^{r-1}(-1)^v a^{(v)}b^{(r-1-v)}
 \right].
\tag{AP.5}
\]
Differentiating the finite sum cancels its interior terms and gives the two residue terms. The relevant pairs \((p,q)\) are finite for general operators, so (AP.5) proves \(\int\operatorname{res}QU=\int\operatorname{res}UQ\). Write \(Q_+\) for its nonnegative-order part and \(Q_-\) for its negative-order part. Both are subalgebras. The residue of a product of two positive parts or two negative parts is zero. In particular
\(\int\operatorname{res}(Q_+U)=\int\operatorname{res}(QU_-)\).
These elementary identities justify every cyclic step below.

The formal adjoint is defined by \(f^*=f\), \(\partial^*=-\partial\) and reversal of products. It respects the defining relation: the adjoint of \(\partial f-f\partial-f'\) is again zero. It consequently extends to the calculus (AP.4) and to negative powers. In particular
\(L^*(x)=\sum_{a=0}^n(-x-\partial)^{n-a}s_a\), with derivatives acting on \(s_a\).

**The Adler identity and its factorization.** For a functional in the coefficients of \(L\), put \(f_j=\delta F/\delta s_j\), and choose its operator gradient
\[
X_F=\sum_{j=1}^n\partial^{j-n-1}f_j.
\qquad
\int\operatorname{res}(\delta L\,X_F)
 =\int\sum_j\delta s_j f_j.
\tag{AP.6}
\]
The last identity is exact even before passing to the integral: the term
\(\delta s_i\partial^{j-i-1}f_j\) has residue \(\delta s_i f_i\) precisely when \(j=i\), and zero otherwise. Define the Adler Hamiltonian map with the sign appropriate to the positive bracket (AP.1):
\[
\mathcal H_L(X)=L(XL)_+-(LX)_+L
             =(LX)_-L-L(XL)_-.
\tag{AP.7}
\]
The first expression is differential. The second shows its order is at most \(n-1\). Adding a differential operator to \(X\) changes neither expression. For a first-order factor it is simply
\(\mathcal H_{A_i}(Y)=\partial\operatorname{res}Y\): both positive products have constant coefficient \(\operatorname{res}Y\), and their difference is its derivative. Thus its sign gives \(\{h_i{}_{\lambda}h_i\}=+\lambda\), as required.

For any two differential operators \(A,B\), direct cancellation proves the product identity
\[
\boxed{\mathcal H_{AB}(X)
 =\mathcal H_A(BX)B+A\mathcal H_B(XA).}
\tag{AP.8}
\]
Indeed the two middle terms are respectively
\(+A(BXA)_+B\) and \(-A(BXA)_+B\); the surviving terms are
\(AB(XAB)_+-(ABX)_+AB\). This proves factorization, without a cited product or reduction theorem.

Let \(B_i=A_1\cdots A_{i-1}\) and \(C_i=A_{i+1}\cdots A_n\). Cyclicity (AP.5) gives the actual boson gradient
\(\delta F/\delta h_i=\operatorname{res}(C_iX_FB_i)\).
For the raw independent bosons, their Hamiltonian variation and (AP.8) therefore give
\[
\delta_FL
 =\sum_i B_i\partial\operatorname{res}(C_iX_FB_i)C_i
 =\boxed{\mathcal H_L(X_F)}.
\tag{AP.9}
\]
This is the complete Adler–Gelfand–Dickey formula for the raw coefficients in our sign convention.

The free primary exposition by [A. De Sole, V. G. Kac and D. Valeri, arXiv:1401.2082v1](https://arxiv.org/abs/1401.2082v1), equations (2.1), (2.45), (2.51) and (2.57), uses the opposite boson sign. Consequently its Adler map and scalar bracket have the opposite overall sign. The calculation here fixes our positive boson convention directly; it does not use that paper's product, reduction or injectivity theorem as an unproved input.

Here is a fully finite coefficient version. For \(X_j=\partial^{j-n-1}f\), (AP.4) gives
\[
\begin{aligned}
(X_jL)_+
 &=\sum_{a=0}^{j-1}\sum_{r=0}^{j-a-1}
   \binom{j-n-1}{r}(fs_a)^{(r)}\partial^{j-a-1-r},\\
(LX_j)_+
 &=\sum_{a=0}^{j-1}\sum_{r=0}^{j-a-1}
   \binom{j-a-1}{r}s_af^{(r)}\partial^{j-a-1-r}.
\end{aligned}
\tag{AP.10}
\]
Put \(q=i+j-a-b-1-r\), and treat any binomial with a negative lower index or lower index above a nonnegative upper index as zero. The coefficient of \(\partial^{n-i}\) in (AP.7) is the following explicit differential operator on \(f\):
\[
\boxed{
\begin{aligned}
H_{ij}(f)=\sum_{a=0}^{j-1}\sum_{r=0}^{j-a-1}\sum_{b=0}^n
\biggl[&
 \binom{j-n-1}{r}\binom{n-b}{q}
 s_b(fs_a)^{(r+q)}\\
&-\binom{j-a-1}{r}\binom{j-a-1-r}{q}
 s_af^{(r)}s_b^{(q)}\biggr].
\end{aligned}}
\tag{AP.11}
\]
Only the terms with \(q\ge0\) are included. Each derivative is explicit: expand
\((fs_a)^{(d)}=\sum_{v=0}^d\binom dv f^{(v)}s_a^{(d-v)}\).
Then replacing \(f^{(v)}\) by \(\lambda^v\) gives exactly
\(\{s_j{}_{\lambda}s_i\}=H_{ij}(\lambda)\).
This formula is a finite polynomial in all coefficients and their derivatives, and supplies every coefficient bracket, rather than only a highest symbol.

For comparison with the compact generating Adler identity, the same formula is
\[
\boxed{
\begin{aligned}
\{L(z){}_{\lambda}L(w)\}
={}&L(w+\lambda+\partial)
 \iota_z\frac1{z-w-\lambda-\partial}L^*(\lambda-z)\\
&-L(z)\iota_z\frac1{z-w-\lambda-\partial}L(w).
\end{aligned}}
\tag{AP.12}
\]
Here \(\iota_z\) expands in descending powers of \(z\), and every \(\partial\) acts to its right. We give the algebraic kernel derivation to fix these orderings. The gradient for the polynomial \(L(z)\) is
\(\sum_{v=0}^{n-1}z^v\partial^{-v-1}f\). Terms with order below \(-n\) are killed by (AP.7), so extend this to \((\partial-z)^{-1}f\). To extract the bracket, adjoin an invertible Poisson-central test symbol satisfying \(f'=\lambda f\). Moving it left gives \(X=fK^{-1}\), where \(K=\partial+\lambda-z\), and \(L\) moving past \(f\) becomes \(L_\lambda=L(\partial+\lambda)\). Right polynomial division gives
\(L_\lambda=(L_\lambda K^{-1})_+K+L(z)\).
Left division gives
\(L=K(K^{-1}L)_++L^*(\lambda-z)\).
For the second identity, \(a\partial=Ka+(z-\lambda-\partial)a\), and induction gives remainder \((z-\lambda-\partial)^pa\) for \(a\partial^p\). Thus no division theorem is being assumed. Substituting these two finite divisions into (AP.7) gives
\[
f^{-1}\mathcal H_L(X)
=L(z)K^{-1}L-L_\lambda K^{-1}L^*(\lambda-z).
\]
The symbol composition rule (AP.4) and \(K^{-1}=-(z-\lambda-\partial)^{-1}\) give (AP.12). The result is polynomial in \(z,w\), since the finite gradient and (AP.10) already give that polynomial; equivalently both division remainders cancel the inverse tails. The kernel expression and (AP.11) are therefore the same finite identity, regardless of which inverse expansion was used to derive it.

Skewsymmetry can also be checked directly on (AP.7). Write \(\operatorname{Tr}Q=\int\operatorname{res}Q\). Isotropy of the two order parts gives
\(\operatorname{Tr}(AB_+)+\operatorname{Tr}(BA_+)=\operatorname{Tr}(AB)\).
Hence
\[
\begin{aligned}
\operatorname{Tr}(X\mathcal H_L(Y))&+\operatorname{Tr}(Y\mathcal H_L(X))\\
&=\operatorname{Tr}(XL\,YL)-\operatorname{Tr}(LX\,LY)=0
\end{aligned}
\]
by cyclicity. This check agrees with the bracket derived from the bosons.

The coefficient algebra embeds in the boson algebra. The highest ordinary letter degree of \(s_i\) is \(e_i(h_1,\ldots,h_n)\); any derivative incurred while expanding (AP.3) uses a differential-operator degree and thus has fewer than \(i\) letters. The same statement holds after any number of derivatives. All \(\partial^re_i\) are algebraically independent. To see this, the \(e_i\) at order zero are independent: the \(h_j\) are integral roots of their monic characteristic polynomial, so the extension of fraction fields is algebraic and has transcendence degree \(n\). At each higher jet order the new \(\partial^re_i\) have linear highest-jet term
\(\sum_j(\partial e_i/\partial h_j)h_j^{(r)}\), plus lower jets. The Jacobian determinant is a nonzero Vandermonde up to sign: its columns are the coefficient lists of \(\prod_{a\ne j}(z+h_a)\), and evaluating at \(-h_j\) makes that matrix diagonal with nonzero products \(\prod_{a\ne j}(h_a-h_j)\). Inverting this determinant gives an invertible triangular change of higher-jet variables. This proves independence at every finite jet order. Therefore the highest weighted part, with weight \(i\) on \(\partial^rs_i\), proves the injectivity
\[
R[s_i^{(r)}:1\le i\le n,\ r\ge0]
\lhook\joinrel\longrightarrow R[h_j^{(r)}:1\le j\le n,\ r\ge0].
\tag{AP.13}
\]
It is first proved over \(k\); extension to ordinary \(R\) preserves injection because every \(k\)-module is flat. Consequently (AP.11) defines a Poisson vertex bracket on the abstract coefficient algebra: closure is explicit, and all its identities follow from the proved boson identities and injection.

**Trace-zero restriction and its precise Dirac term.** For the raw bracket put \(u=s_1=\sum_i h_i\). Then \(\{u{}_{\lambda}u\}=n\lambda\). Replace its boson matrix by the projection \(P=I-\mathbf1\mathbf1^t/n\). The element \(u\), and every derivative of \(u\), is now central, so the differential ideal \((u,u',\ldots)\) is Poisson. This gives the actual trace-zero quotient; it is not the false operation of setting \(u=0\) in the unreduced raw bracket.

For any operator gradient \(X\), write \(f_i=\operatorname{res}(C_iXB_i)\) and \(F=\sum_if_i\). The projected boson flows are
\[
\delta h_i=f_i'-\frac1nF',\qquad
\delta L=\mathcal H_L(X)-\frac1n[L,F].
\tag{AP.14}
\]
The commutator identity follows directly by the product rule:
\([L,F]=\sum_iB_i[A_i,F]C_i=\sum_iB_iF'C_i\).
The coefficient of \(\partial^{n-1}\) in (AP.7) is
\(\operatorname{res}(LX)-\operatorname{res}(XL)=\operatorname{res}[L,X]\).
The same coefficient in the Miura flow is \(\sum_i f_i'=F'\). Thus \(F\) is a genuine polynomial primitive of this residue, and the projected flow has zero trace coefficient.

We make that primitive explicit in scalar coefficients. The Hamiltonian for \(\int f u\) changes every \(h_i\) by \(f'\), so changes \(L\) by \([L,f]\). Its coefficient operators are
\[
Q_i(f)=H_{i1}(f)
=\sum_{a=0}^{i-1}\binom{n-a}{i-a}s_af^{(i-a)}.
\tag{AP.15}
\]
Skewsymmetry just proved gives \(H_{1j}=-Q_j^*\). Therefore
\[
\boxed{
\operatorname{res}[L,X_j]=\partial F_j(f),\qquad
F_j(f)=\sum_{a=0}^{j-1}(-1)^{j-a+1}
 \binom{n-a}{j-a}(fs_a)^{(j-a-1)}.}
\tag{AP.16}
\]
This primitive agrees with \(\sum_if_i\): both differentiate to the same expression, and their difference is linear in a free test symbol and its jets. A finite differential polynomial with derivative zero in these free jets is a constant; inspecting its highest jet proves this by descending induction, since the positive integers are units. Linearity in the test symbol excludes a nonzero constant. There is consequently no ambiguity from choosing an integration constant.

For \(s_1=0\), and \(2\le i,j\le n\), the entire reduced bracket is
\[
\boxed{
\begin{aligned}
\mathcal H_L^{\mathrm{sl}}(X)
 &=L(XL)_+-(LX)_+L
       -\frac1n[L,\partial^{-1}\operatorname{res}[L,X]],\\
H^{\mathrm{sl}}_{ij}(f)
 &=H_{ij}(f)-\frac1n Q_i(F_j(f)),
\qquad
\{s_j{}_{\lambda}s_i\}=H^{\mathrm{sl}}_{ij}(\lambda).
\end{aligned}}
\tag{AP.17}
\]
The symbol \(\partial^{-1}\) in the first line means precisely the explicit primitive (AP.16), extended linearly to the finite operator gradient (AP.6). It is not a new nonlocal field. The second line, with (AP.11), (AP.15), (AP.16) and the rule \(f^{(v)}\mapsto\lambda^v\), is a complete finite formula for every derivative and every sign of the normalized scalar-oper bracket. It is the raw Dirac expression \(H_{ij}-H_{i1}(n\partial)^{-1}H_{1j}\), proved here by the actual boson projection. This also proves coefficient closure.

In the compact kernel notation the extra term added to the right side of (AP.12) is
\[
\boxed{-\frac1n
 \bigl(L(w+\lambda+\partial)-L(w)\bigr)
 (\lambda+\partial)^{-1}
 \bigl(L(z)-L^*(\lambda-z)\bigr),
 \qquad s_1=0.}
\tag{AP.18}
\]
Indeed the first parenthesis is the generating operator (AP.15), and the second is the generating \(H_{1j}(\lambda)=-Q_j^*(\lambda)\). The first parenthesis has \(\lambda+\partial\) as a right factor, so the displayed inverse cancels and leaves a differential polynomial. Thus (AP.18) has no nonlocal tail. On the hyperplane \(\sum_i h_i=0\), the independence proof of (AP.13) applies with \(e_1\) and its jets eliminated. At order zero, the \(n-1\) independent coordinates \(h_1,\ldots,h_{n-1}\), with \(h_n=-\sum_{i<n}h_i\), are algebraic over \(k(e_2,\ldots,e_n)\), proving independence of the latter. The Vandermonde is still nonzero on this hyperplane, as the specialization \(h_j=j-(n+1)/2\) shows. At higher jets its invertible linear change, with \(\partial^re_1=\sum_jh_j^{(r)}=0\), solves the remaining \(n-1\) jet coordinates just as before. Hence the reduced coefficient algebra \(R[s_i^{(r)}:2\le i\le n]\) also injects into the trace-zero bosons; its Jacobi identity follows without an assumed Drinfeld–Sokolov theorem.

**The quadratic coefficient and its exact central term.** In trace-zero bosons let
\[
\begin{aligned}
\rho_j&=j-\frac{n+1}{2},\qquad \sum_j\rho_j=0,\\
s_2&=-\frac12\sum_jh_j^2+\sum_j\rho_jh_j',\\
\gamma_n&=\sum_j\rho_j^2=\frac{n(n^2-1)}{12}.
\end{aligned}
\tag{AP.19}
\]
The final equality follows by inserting \(\sum j=n(n+1)/2\) and
\(\sum j^2=n(n+1)(2n+1)/6\); these two sums follow respectively by pairing the ends and by telescoping \((j+1)^3-j^3\). The expression for \(s_2\) follows from (AP.3), using \(\sum h_j=\sum h_j'=0\).

Put \(U=-\sum h_j^2/2\), \(V=\sum\rho_jh_j'\). Formula (AP.2) gives
\(\{U{}_{\lambda}U\}=-(\partial+2\lambda)U\).
Moreover \(\{U{}_{\lambda}h_j\}=-\lambda h_j-h_j'\), so
\(\{U{}_{\lambda}V\}=-\lambda^2\sum\rho_jh_j-2\lambda V-V'\).
The reverse cross term is \(+\lambda^2\sum\rho_jh_j\). Finally sesquilinearity gives
\(\{V{}_{\lambda}V\}=-\rho^tP\rho\lambda^3=-\gamma_n\lambda^3\).
Consequently
\[
\boxed{\{s_2{}_{\lambda}s_2\}
 =-(\partial+2\lambda)s_2-\frac{n(n^2-1)}{12}\lambda^3.}
\tag{AP.20}
\]
The positive boson convention therefore gives a negative cubic central term. For \(n=2\), \(h_2=-h_1\) gives \(s_2=-h_1'-h_1^2\), \(\{h_1{}_{\lambda}h_1\}=\lambda/2\), and (AP.20) is
\(-s_2'-2\lambda s_2-\lambda^3/2\). This fixes the sign independently of any terminology for a second Gelfand–Dickey bracket.

**Scalar density covariance and the inverse-coordinate convention.** The Hamiltonian \(\int v s_2\), with \(v\) an external differential test function, gives
\[
\delta_vh_i=\partial(-v h_i-\rho_i v')
 =-v h_i'-v'h_i-\rho_iv''.
\tag{AP.21}
\]
The projected bracket does not change this expression: its sum is zero, by \(\sum h_i=\sum\rho_i=0\). Set \(a_i=-\rho_i=(n+1)/2-i\) and \(b=(1-n)/2\). Thus \(a_n=b\), \(a_1+1=b+n\), and \(a_i=a_{i+1}+1\). A direct first-order multiplication gives
\[
\delta_vA_i
 =-(v\partial+(a_i+1)v')A_i
       +A_i(v\partial+a_iv').
\tag{AP.22}
\]
Its derivative coefficient cancels, and its constant coefficient is exactly
\(-v h_i'-v'h_i+a_iv''\), proving (AP.22). In the product the adjacent terms cancel because \(a_i=a_{i+1}+1\). Therefore
\[
\boxed{\delta_vL
 =-(v\partial+(b+n)v')L+L(v\partial+bv'),
 \qquad b=\frac{1-n}{2}.}
\tag{AP.23}
\]
This is precisely the inverse-coordinate infinitesimal transport of an order-\(n\) density operator from weight \(b\) to weight \(b+n\). Expanding by (AP.4) proves the complete coefficient law
\[
\begin{aligned}
\delta_vs_i
 &=-v s_i'-iv's_i+
       \sum_{j<i}C_{ij}v^{(i-j+1)}s_j,\\
C_{ij}
 &=\binom{n-j}{i-j+1}
       +\frac{1-n}{2}\binom{n-j}{i-j},
\qquad s_0=1,\ s_1=0.
\end{aligned}
\tag{AP.24}
\]
The two binomials come respectively from \(s_j\partial^{n-j}(v\partial)\) and \(s_j\partial^{n-j}(bv')\). The diagonal terms, including the two left terms in (AP.23), sum to \(-v s_i'-iv's_i\). In particular \(C_{20}=-\gamma_n\), so (AP.24) agrees with (AP.20). For \(n=3\), it gives
\(\delta_vs_3=-v s_3'-3v's_3-s_2v''-v''''\); hence
\(s_3-s_2'/2\) is a primary coefficient of weight three. This is also a check on the order of the Miura factors and the cubic correction.

The finite scalar-coordinate comparison retains the already stated scalar-oper foundations: formal substitution and its inverse over ordinary rings, including nilpotent constants; residue change of variable; and the half-density descent of (SC.O4)–(SC.O6). At those premises it has a direct boson proof too. For \(\psi=\phi^{-1}\), the first-order density transport gives
\[
\boxed{h_i^{\phi}(t)
 =\psi'(t)h_i(\psi(t))
       +\rho_i\frac{\psi''(t)}{\psi'(t)}.}
\tag{AP.25}
\]
Indeed if \(C_\psi f=f\circ\psi\), then
\[
(\psi')^{a_i+1}C_\psi A_iC_\psi^{-1}(\psi')^{-a_i}
=\partial+\psi'h_i\circ\psi-a_i\psi''/\psi'.
\]
The intermediate density factors cancel in the product, giving the finite version of (AP.23). When half-integer weights need a square root, use exactly the free rank-two square-root extension and sign-independent descent already proved for scalar operators; the final expression (AP.25) itself has only integral powers and rational \(\rho_i\). It preserves \(\sum h_i=0\). Differentiating \(\psi=t-\epsilon v\) gives (AP.21), so the inverse action, rather than its opposite, is fixed.

This finite action is Poisson, not only an action with the correct infinitesimal law. Define the mode bracket equivalently by its linear residue functionals
\(H_{i,f}=\operatorname{Res}f(t)h_i(t)dt\):
\(\{H_{i,f},H_{j,g}\}=P_{ij}\operatorname{Res}f'(t)g(t)dt\).
For \(f=t^m,g=t^q\) this is \(mP_{ij}\delta_{m+q,0}\), the current-mode version of (AP.1). Under (AP.25) a linear functional becomes
\(H_{i,f\circ\phi}\) plus a central coordinate-dependent constant. Residue substitution gives
\(\operatorname{Res}(f\circ\phi)'(g\circ\phi)dt=\operatorname{Res}f'g\,dt\).
Thus the bracket is preserved on all linear generators, and Leibniz proves it on their polynomial coefficient algebra. This argument includes nilpotent translations: their inverse expansions are finite on every negative Laurent power, and positive tails contribute finitely at each output coefficient, precisely at the retained substitution premises. It then descends through the coefficient closure just proved to the scalar-oper bracket. No vertex or affine-center comparison is needed for this conclusion.

For raw independent bosons (AP.25) is Poisson by the same calculation with \(P=I\). Its coordinate Hamiltonian is
\[
\begin{aligned}
T&=-\sum h_i^2/2+\sum\rho_i h_i'\\
 &=s_2-s_1^2/2-(n-1)s_1'/2.
\end{aligned}
\]
After trace-zero restriction it becomes \(s_2\). This distinguishes the raw coordinate Hamiltonian from the quadratic coefficient and prevents a false trace contribution to the normalized density law.

The proved mechanism is the following exact comparison:

| Input and operation | Proved output | Exact locator |
|---|---|---|
| Independent bosons with \(+\delta_{ij}\lambda\); multiply the ordered first-order factors | Raw scalar Adler identity and every coefficient bracket | (AP.7)–(AP.12) |
| Project the boson matrix to \(I-\mathbf1\mathbf1^t/n\); impose \(\sum h_i=0\) | Local trace-zero Dirac bracket, with its finite primitive | (AP.14)–(AP.18) |
| Quadratic coefficient and the vector \(\rho_i=i-(n+1)/2\) | Central term \(-\gamma_n\lambda^3\) and inverse-density Hamiltonian action | (AP.19)–(AP.24) |
| Inverse coordinate and first-order density transport | Finite scalar-coordinate Poisson compatibility | (AP.25) |

*The arrows are actual algebraic operations: product factorization, orthogonal trace projection, finite coefficient extraction and inverse density transport. Their proofs retain all signs and lower derivative terms. Related human-source exposition is De Sole–Kac–Valeri, [§§2.7–2.9 of the free exact v1 edition](https://arxiv.org/pdf/1401.2082v1), with the opposite boson sign. The diagram establishes no affine-to-boson arrow.*

The scalar Poisson formula is thus complete for every \(n\) over ordinary characteristic-zero coefficient rings, with the explicit scalar-oper premises above. A Poisson comparison from the affine critical center requires its own constructed homomorphism and its exact level/form normalization. Equality of leading PBW symbols alone cannot supply that homomorphism. Chiral, Satake, derived-family and global localization comparisons remain separate statements.

#### 3.7.4. The affine Miura map and the root anomaly

The Cartan projection of negative current words is useful for computing a determinant. It is not a map of current fields: the Cartan currents at the critical affine form have a nonzero central contraction. To obtain the Poisson Miura map, we construct a family of maps of fields before taking its critical fibre.

We work over a characteristic-zero field \(k\). Every construction below is defined over \(k[\varepsilon]\) and extends to every ordinary coefficient algebra \(R\), including a nonreduced one. For the raw matrix algebra put
\[
 \kappa_{n,\varepsilon}(X,Y)
 =(-n+\varepsilon)\operatorname{tr}(XY)
             +\operatorname{tr}(X)\operatorname{tr}(Y).
 \tag{WP.1}
\]
The scalar current is retained. On \(\mathfrak{sl}_n\) this form is
\((-n+\varepsilon)\operatorname{tr}(XY)\). The critical fibre is precisely the form of (SL.L1), and the deformation direction is \(\operatorname{tr}(XY)\).

We use the ordered-current basis proved in §3, (K2.1)–(K2.3), the finite normal reconstruction in §3.6.2, (UC.2)–(UC.14), and the actual invariant determinant states of §3.3.5, (SL.L4)–(SL.L23). These are the earlier proofs in [*Opers, critical level and the Beilinson–Drinfeld construction*](opers-critical-level-and-the-beilinson-drinfeld-construction.md). We retain their mode convention
\([x_r,y_s]=[x,y]_{r+s}+r\kappa(x,y)\delta_{r,-s}\), with the central generator acting as \(1\). No assertion about a sheaf of chiral differential operators, a flag-variety descent or a geometric Wakimoto module is used.

For the varying form (WP.1), freeness is a direct use of that proof,
rather than scalar extension of a fixed form. Order the matrix-current
basis and the central generator as in (K2.2). Pair reductions are monic
over \(R[\varepsilon]\); their sole overlapping ambiguity is the same
Jacobi identity, which holds because (WP.1) is invariant. The terminating
normal-form argument therefore gives a free ordered basis over this
coefficient ring. After imposing the vacuum relations its basis is
again the ordered negative-current words. Likewise the finite
identities in (UC.2)–(UC.14) use only the current brackets and rational
binomial coefficients. Substituting (WP.1) into their scalar terms
proves those identities for the varying form itself.

##### The free fields as explicit operators

For each pair \(i<j\), introduce a beta-gamma pair with modes
\[
 [\beta_{ij,r},\gamma_{ij,s}]=\delta_{r,-s},\qquad
 [\beta_{ij,r},\beta_{ij,s}]=[\gamma_{ij,r},\gamma_{ij,s}]=0.
\]
Different pairs commute. Introduce \(n\) bosons with
\[
 [b_{i,r},b_{j,s}]
     =\varepsilon r\delta_{ij}\delta_{r,-s}.
 \tag{WP.2}
\]
The Fock module is the polynomial module on the creation variables
\[
 \beta_{ij,-a}\ (a\geq1),\qquad
 \gamma_{ij,-r}\ (r\geq0),\qquad
 b_{i,-a}\ (a\geq1).
 \tag{WP.3}
\]
They act by multiplication. The annihilation operators are
\(\beta_{ij,r}=\partial/\partial\gamma_{ij,-r}\) for \(r\geq0\),
\(\gamma_{ij,s}=-\partial/\partial\beta_{ij,-s}\) for \(s>0\), and
\(b_{i,r}=\varepsilon r\,\partial/\partial b_{i,-r}\) for \(r>0\);
\(b_{i,0}=0\). These formulas prove all relations and the freeness over
\(k[\varepsilon]\), rather than assuming a representation exists.

Our fields and translation are
\[
 \beta_{ij}(z)=\sum_r\beta_{ij,r}z^{-r-1},\qquad
 \gamma_{ij}(z)=\sum_r\gamma_{ij,r}z^{-r},\qquad
 b_i(z)=\sum_r b_{i,r}z^{-r-1},
\]
\[
 [T,\beta_{ij,r}]=-r\beta_{ij,r-1},\qquad
 [T,\gamma_{ij,r}]=-(r-1)\gamma_{ij,r-1},\qquad
 [T,b_{i,r}]=-r b_{i,r-1},\qquad T1=0.
 \tag{WP.4}
\]
For example \(T\gamma_{ij,0}=\gamma_{ij,-1}\). The rules are consistent with
(WP.2): in a beta-gamma bracket the possible delta has \(r+s=1\), and its
coefficient after applying \(T\) is \(-r-s+1=0\). The boson check is the
same affine translation calculation as (SL.L3). They preserve the vacuum
annihilation relations. Thus \(T\) is an actual operator on the Fock module.

Creation parts stand on the left of annihilation parts. A simultaneous
normal product of elementary free fields means that all their creation
parts are moved left, without retaining the contractions produced by that
movement. In particular the cubic normal product below is simultaneous;
an unspecified iterated binary normal product would be ambiguous. The
singular contractions are
\[
 \beta_i(z)\gamma_j(w)\sim\frac{\delta_{ij}}{z-w},\qquad
 \gamma_i(z)\beta_j(w)\sim-\frac{\delta_{ij}}{z-w},\qquad
 b_i(z)b_j(w)\sim\frac{\varepsilon\delta_{ij}}{(z-w)^2}.
 \tag{WP.5}
\]
Here and below a suppressed root-pair label is specified by the relevant
recursion step.

We spell out the finite rule for the calculations. In the product of two
simultaneously normal elementary monomials, choose disjoint pairs, one
factor from each monomial, replace them by their contractions, and normal
order the unpaired factors. Sum over all such matchings. If the resulting
pole is \((z-w)^{-q}\), expand the unpaired \(z\)-factors only through
Taylor order \(q-1\). Derivatives differentiate their contractions with
respect to their own variable. This rule follows by moving each
annihilation operator in the left monomial through the right creation
operators: at each passage the commutator gives either the moved term or
one contracted pair. Induction on the number of passages lists each
matching exactly once. All elementary contractions are scalar, so their
order introduces no further terms. When a monomial also contains one
inner affine current, its single current-current contraction is inserted
in the same calculation; there is never more than one such current in
either monomial below.

The sums define fields on the polynomial Fock module. On a fixed input
there are only finitely many annihilation choices; for a fixed output
coefficient the remaining creation indices have a fixed sum and
nonnegative powers, so only finitely many possibilities occur. Taking
common bounds before a commutator proves the contraction identities as
identities of actual mode operators. Their finite pole bounds prove
locality.

For clarity, these operators also provide the state-field products used
here. Assign a field to a creation word by derivatives and simultaneous
normal products, with the appropriate factorials. The creation expansion
is \(Y(a,z)1=e^{zT}a\). The locality product
\[
 (A_{(q)}B)(w)=\operatorname{Res}_z\!
 \left(\iota_{z,w}(z-w)^q A(z)B(w)
       -\iota_{w,z}(z-w)^q B(w)A(z)\right)
 \tag{WP.6}
\]
is coefficient-finite; for \(q=-r<0\) it is
\(:\partial^{r-1}A\,B:/(r-1)!\). The locality closure proof of
(UC.12) uses only the commutator, the two kernel expansions and common
coefficient bounds, and therefore applies to these free fields as well.
The constant term of its creation expansion is the state \(a_{(q)}b\).

Here is the needed uniqueness argument. A field local with every
elementary free field, translation covariant, and with zero creation
expansion vanishes on every creation word. Indeed multiply its
commutator with an elementary field by a sufficient power of \(z-w\).
On a previously killed word the reversed product is zero. In the
creation expansion in \(w\), the constant coefficient of that power is
the invertible Laurent monomial \(z^L\). Successive coefficients
therefore show that the field kills each next creation mode. Induction
on the word length proves the assertion. Thus (WP.6), its creation state
and translation determine precisely the field of the state
\(a_{(q)}b\). In particular all normal-product and singular-product
identifications used below follow from these explicit operators.

##### A recursive affine homomorphism

Suppose \(m=n-1\), and assume that the \(\mathfrak{gl}_m\) currents
\(J_{ab}\) at form \(\kappa_{m,\varepsilon}\) have already been constructed.
Use \(m\) new beta-gamma pairs, independent of those inner currents, and
a new independent boson \(b=b_n\). Set
\[
 \ell=-n+\varepsilon,\qquad
 \Gamma_i=\sum_a:\gamma_aJ_{ai}:,\quad
 U_i=-:\gamma_i b:,\quad
 C_i=-\sum_a:\gamma_i\gamma_a\beta_a:,\quad
 D_i=\ell\,\partial\gamma_i .
 \tag{WP.7}
\]
All sums in this step run from \(1\) to \(m\). Define
\[
 \begin{aligned}
 A_{ij}&=J_{ij}-:\gamma_j\beta_i:,&
 H&=b+\sum_a:\gamma_a\beta_a:,\\
 E_i&=\beta_i,& F_i&=\Gamma_i+U_i+C_i+D_i,
 \end{aligned}
\]
\[
 E_{ij}(z)\longmapsto A_{ij}(z),\quad
 E_{in}(z)\longmapsto E_i(z),\quad
 E_{ni}(z)\longmapsto F_i(z),\quad
 E_{nn}(z)\longmapsto H(z).
 \tag{WP.8}
\]
The inner current form is
\((\ell+1)\operatorname{tr}(XY)+\operatorname{tr}(X)\operatorname{tr}(Y)\).
The new boson form is \(\varepsilon=\ell+m+1\).

We prove the entire affine relation. Put \(u=z-w\), and temporarily
keep \(\ell,\varepsilon\) independent, so that the possible defect is
\[
 \Delta=\ell+m+1-\varepsilon.
 \tag{WP.9}
\]
The complete singular-product table is
\[
 \begin{array}{c|l}
 \text{pair}&\text{singular product}\\ \hline
 A_{ij}(z)A_{ab}(w)&
 (\delta_{ja}A_{ib}-\delta_{ib}A_{aj})/u
 +(\ell\delta_{ib}\delta_{ja}+\delta_{ij}\delta_{ab})/u^2\\
 A_{ij}(z)H(w)&\delta_{ij}/u^2\\
 H(z)H(w)&(\varepsilon-m)/u^2\\
 A_{ij}(z)E_a(w)&\delta_{ja}E_i/u\\
 H(z)E_a(w)&-E_a/u\\
 A_{ij}(z)F_a(w)&-\delta_{ia}F_j/u\\
 H(z)F_a(w)&F_a/u+\Delta\gamma_a/u^2\\
 E_i(z)F_j(w)&(A_{ij}-\delta_{ij}H)/u
                         +\ell\delta_{ij}/u^2\\
 E_i(z)E_j(w)&0\\
 F_i(z)F_j(w)&-\Delta\gamma_i\gamma_j/u^2
                         -\Delta(\partial\gamma_i)\gamma_j/u .
 \end{array}
 \tag{WP.10}
\]
The reverse ordered products follow from the antisymmetric mode
commutator; thus this table covers every matrix-unit pair.

We give the full cancellations, including those which determine the
level. For two ghost matrix currents \(-:\gamma_j\beta_i:\), their
double contraction is
\(-\delta_{ib}\delta_{ja}/u^2\); their single contractions have the
matrix-unit bracket. Adding the inner \(J\) contraction changes its
coefficient \(\ell+1\) to \(\ell\). The mixed ghost-trace double
contraction is \(+\delta_{ij}/u^2\). The trace ghost with itself gives
\(-m/u^2\), producing the first three rows. The rows with \(E_a=\beta_a\)
use one contraction. In particular
\[
 \beta_i(z)F_j(w)\sim
 \frac{J_{ij}-\gamma_j\beta_i-\delta_{ij}
                    (b+\sum_a\gamma_a\beta_a)}u
       +\frac{\ell\delta_{ij}}{u^2},
 \tag{WP.11}
\]
which is exactly its displayed row.

For \(A_{ab}F_i\), the double-pole contributions from \(J_{ab}\Gamma_i\),
the ghost part of \(A_{ab}\) against \(C_i\), and that ghost part against
\(D_i\) are respectively
\[
 (\ell+1)\delta_{ai}\gamma_b+\delta_{ab}\gamma_i,\quad
 -\delta_{ai}\gamma_b-\delta_{ab}\gamma_i,\quad
 -\ell\delta_{ai}\gamma_b.
\]
Their sum is zero. The single pole from \(J_{ab}\Gamma_i\) is
\(\gamma_bJ_{ai}-\delta_{ai}\Gamma_b\). The ghost against \(\Gamma_i\)
cancels \(\gamma_bJ_{ai}\). Its products with \(U_i,C_i\) give
\(-\delta_{ai}U_b,-\delta_{ai}C_b\); the remaining single contractions
inside the product with \(C_i\) cancel each other. The Taylor term in
the product with \(D_i\) is
\(-\ell\delta_{ai}\partial\gamma_b\). Hence the single pole is exactly
\(-\delta_{ai}F_b\).

For \(HF_i\), write \(N=\sum_a:\gamma_a\beta_a:\). Its single
contractions with \(\Gamma_i,U_i,C_i\) give these same three fields.
The double contractions in \(NC_i\) give
\((m+1)\gamma_i/u^2\): one chooses the distinguished \(\gamma_i\),
or one of the \(m\) summed gamma factors. The product \(ND_i\) gives
\[
 \ell\gamma_i(z)/u^2
 =\ell\gamma_i(w)/u^2+\ell\partial\gamma_i(w)/u
                  +\text{regular terms}.
\]
The product \(bU_i\) gives \(-\varepsilon\gamma_i/u^2\).
This proves the \(HF_i\) row, including \(\Delta\).

Finally consider \(F_iF_j\). There are no poles of order greater than
two. The single contractions in \(\Gamma_i\Gamma_j\) give
\(\gamma_i\Gamma_j-\gamma_j\Gamma_i\). Those in
\(\Gamma_iC_j+C_i\Gamma_j\) give the opposite expression.
The products \(U_iC_j+C_iU_j\) cancel their single poles; the four
single-contraction terms in \(C_iC_j\) also cancel. Thus only the
following double contractions and their first Taylor terms remain:
\[
 \begin{array}{c|l}
 \text{pair}&u^2\text{ times its double contraction before Taylor expansion}\\ \hline
 \Gamma_i\Gamma_j&
   (\ell+1)\gamma_j(z)\gamma_i(w)+\gamma_i(z)\gamma_j(w)\\
 U_iU_j&\varepsilon\gamma_i(z)\gamma_j(w)\\
 C_iC_j&-\gamma_j(z)\gamma_i(w)-(m+2)\gamma_i(z)\gamma_j(w)\\
 C_iD_j&-\ell\gamma_i(z)\gamma_j(z)\\
 D_iC_j&-\ell\gamma_i(w)\gamma_j(w).
 \end{array}
 \tag{WP.12}
\]
For the third row there are four pairing patterns: pairing the left
beta with the distinguished or summed right gamma, and the right beta
with the distinguished or summed left gamma. Their contributions are
\(-\gamma_j(z)\gamma_i(w)\), two copies of
\(-\gamma_i(z)\gamma_j(w)\), and \(m\) further copies of the latter.
This explains the coefficient \(m+2\), also when \(i=j\); labelled
factors count their multiplicities. At Taylor order zero the sum is
\(-\Delta\gamma_i\gamma_j\). At order one the
\(\gamma_i\partial\gamma_j\) terms cancel, and the remaining term is
\(-\Delta(\partial\gamma_i)\gamma_j\). This proves the final row
without an omitted normal-order boundary.

In our recursion \(\Delta=0\). Every row of (WP.10) is therefore exactly
the affine bracket at (WP.1). The base case \(n=1\) is just the boson
\(E_{11}=b_1\), whose form is \(\varepsilon\). Induction constructs all
matrix currents in a tensor product of one beta-gamma pair per positive
root and \(n\) independent bosons. Every formula is a finite polynomial
in fields and their derivatives.

Each constructed current annihilates the Fock vacuum in nonnegative
modes. Indeed its creation expansion has no negative power of \(z\):
gamma starts at \(\gamma_0\), while beta, the inner currents and bosons
start at their \(-1\) creation modes; \(\partial\gamma\) starts at
\(\gamma_{-1}\). The induced-module property consequently gives a map
\[
 \rho_\varepsilon:V_{\kappa_{n,\varepsilon}}
      \longrightarrow\mathcal F_n\otimes\mathcal H_{\varepsilon,n}.
 \tag{WP.13}
\]
It preserves the vacuum, \(T\), and every state-field product. To verify
the last assertion rather than postulate it, apply the negative-current
normal recursion (UC.3)–(UC.5) to a source PBW word. On the target its
current images obey exactly the same recursion, by (WP.6) and its
creation uniqueness. Thus
\(\rho_\varepsilon(Y(a,z)c)=Y(\rho_\varepsilon a,z)\rho_\varepsilon c\),
first for current words and then by linearity. Extracting every
coefficient proves preservation of both singular and normal products.
The coefficient bounds preceding (WP.6) justify this on actual vectors.
Injectivity of the entire affine map is not needed here.

##### The exact Cartan anomaly

The recursive diagonal formulas simplify to
\[
 \begin{aligned}
 \rho_\varepsilon(H(z))
 &=b_H(z)-\sum_{i<j}(H_i-H_j):\gamma_{ij}\beta_{ij}:,\\
 b_H&=\sum_iH_i b_i,
 \qquad H=\operatorname{diag}(H_1,\ldots,H_n).
 \end{aligned}
 \tag{WP.14}
\]
This follows immediately by induction: the new pair \((i,n)\)
subtracts its ghost from \(E_{ii}\) and adds it to \(E_{nn}\).

A ghost trace has double contraction \(-1/u^2\). Moreover
\[
 \sum_{i<j}(H_i-H_j)(K_i-K_j)
 =n\sum_iH_iK_i-\left(\sum_iH_i\right)\left(\sum_iK_i\right).
 \tag{WP.15}
\]
Expand the left side: each diagonal term occurs \(n-1\) times and the
off-diagonal terms give minus the sum over distinct indices. Thus the
ghost form in (WP.14) is
\(-n\operatorname{tr}(HK)+\operatorname{tr}(H)\operatorname{tr}(K)\),
exactly the critical form. Adding the boson form gives (WP.1).
Equivalently the bosons necessarily have
\[
 \kappa_{n,\varepsilon}|_{\mathfrak h}
             -\kappa_{\rm ghost}
                  =\varepsilon\operatorname{tr}|_{\mathfrak h}.
 \tag{WP.16}
\]
This is the root anomaly cancellation. In particular the critical
Cartan bosons have zero contraction. Using
\(\kappa_{\rm crit}|_{\mathfrak h}\) for their form would give the wrong
Poisson map.

##### Why critical invariant states have no ghosts

Specialize to \(\varepsilon=0\), and let \(w\) be an actual critical
invariant state. Its image is killed by every nonnegative current.
At the outer recursion step \(E_{in,r}=\beta_{i,r}\), \(r\geq0\).
These operators are exactly the partial derivatives with respect to
all outer gamma creation variables. A polynomial killed by them is
independent of those variables: a nonzero positive exponent has a
nonzero, invertible integer as its derivative coefficient. This
argument works over every ordinary \(R\).

On a gamma-free polynomial the zero mode
\(H_0=b_0+\sum_a(:\gamma_a\beta_a:)_0\) is minus the total number of
outer beta variables. More explicitly its commutators with beta and
gamma creation modes are \(-\beta\) and \(+\gamma\), and it kills the
vacuum. Since \(H_0\) kills the image, that image is independent of
outer beta variables too. On this ghost-free subspace all nonnegative
modes of \(:\gamma_j\beta_i:\) kill the outer vacuum, so invariance under
\(A_{ij,r}\), \(r\geq0\), is invariance under the inner \(J_{ij,r}\).
Induction removes every root pair. Therefore
\[
 \rho_0(w)\in\mathcal H_{0,n}
        =k[b_{i,-a}:1\leq i\leq n,\ a\geq1].
 \tag{WP.17}
\]
This entire boson algebra is central in the critical free-field algebra:
its modes commute with ghosts and with all boson modes. The conclusion
is stronger than commutation within the image of the affine center.

We also compute this ghost-free image exactly. Let \(q\) set all outer
ghost creation variables to zero. Use parabolic PBW order
\[
 \langle E_{in,r}:i<n,r<0\rangle,\quad
 \langle E_{ij,r},E_{nn,r}:i,j<n,r<0\rangle,\quad
 \langle E_{ni,r}:i<n,r<0\rangle
 \tag{WP.18}
\]
from left to right. Each displayed outer root space is an abelian Lie
algebra, and the middle block is the Levi algebra; the ordered-basis
proof applies.

A word with a nonempty left block maps to a polynomial with an outer
beta multiplication factor on its left, since a negative \(E_{in}\)
mode is negative beta multiplication. Its \(q\)-image is zero. If the
left block is empty but the right block is nonempty, its image has
strictly positive outer ghost charge, measured by \(H_0\); each
\(F_i\) has charge \(+1\), and the middle block has charge zero. The
ghost-free component has charge zero, so again its \(q\)-image vanishes.
For a word solely in the middle block, write \(A_{ij}=J_{ij}\) plus
an outer ghost current and \(H=b\) plus the outer ghost trace. These
ghost currents commute with the inner fields. Any nonempty word of
their negative modes has positive ghost energy, whereas a constant
ghost polynomial has energy zero. Its \(q\)-image is zero. The surviving
word is exactly the same ordered word in \(J_{ij},b\).

It follows that, on every source state, \(q\rho_0\) is the parabolic
PBW projection followed by the inner map and the identity on \(b\).
For an invariant state the image is already ghost-free by (WP.17).
Repeating the argument proves
\[
 \rho_0(w)=\operatorname{HC}_+(w),
 \tag{WP.19}
\]
with diagonal negative currents replaced by the boson creation modes.
Here \(\operatorname{HC}_+\) has positive finite roots on the left,
Cartan in the middle and negative finite roots on the right. Internal
orders in the positive and negative root algebras do not change this
projection: it is the projection modulo the sum of the left
positive-root and right negative-root PBW subspaces. The parabolic
orders in (WP.18) give precisely that projection recursively.
Equation (WP.19) is a state calculation following from the field map,
not an assertion that PBW projection itself preserves fields.

##### Determinant images, with their order

Let \(S_i v\) be the raw determinant states of (SL.L4)–(SL.L7).
We calculate their images with every derivative correction. First
use the opposite PBW projection \(\operatorname{HC}_-\), with negative
finite roots before Cartan before positive finite roots. In a
nonidentity determinant permutation, take the first column \(j\)
which is not fixed. The preceding columns are fixed, and
\(\sigma(j)>j\); thus its first off-diagonal entry is a negative
root current. Move it left across the preceding diagonal entries
and translations. Its commutators remain negative root currents,
including their \(T\)-derivatives. Every resulting term therefore
belongs to the left negative-root PBW subspace and has zero
\(\operatorname{HC}_-\)-projection. Only the identity permutation
survives:
\[
 \operatorname{HC}_-\operatorname{cdet}(\tau\mathbf1+E[-1])
                  =(\tau+h_1)\cdots(\tau+h_n),\qquad
 [\tau,h_i]=T h_i .
 \tag{WP.20}
\]
The reasoning also applies with \(\tau+u\), so it determines every
coefficient state, not just the constant determinant coefficient.

Simultaneously reverse the row and column indices. The precise Manin
identity and exterior calculation (SL.L8)–(SL.L10) prove that a column
permutation multiplies the determinant by its sign; a row permutation
does likewise. Hence this simultaneous reversal fixes the determinant.
It interchanges the two root orders and sends \(h_i\) to \(h_{n+1-i}\).
Applying (WP.19) to every invariant coefficient consequently gives
\[
 \boxed{\quad
 \rho_0\!\left(\sum_{i=0}^n S_i v\,u^{n-i}\right)
 =\left.(T+u+b_n)\cdots(T+u+b_1)1\right.,
 \quad S_0v=v .\quad}
 \tag{WP.21}
\]
Equivalently, normal order the scalar differential operator
\[
 (\partial+b_n)\cdots(\partial+b_1)
       =\partial^n+\mu(S_1)\partial^{n-1}
                       +\cdots+\mu(S_n).
 \tag{WP.22}
\]
Then \(\mu(S_i)=\rho_0(S_i v)\), with \(b_i=b_{i,-1}\) as a
differential-algebra generator and \(\partial a=a\partial+Ta\).
This uses the invariance of the determinant states already proved in
(SL.L22), not their symbols alone.

To agree with the ordered factors in (WP.20), set
\(h_r=b_{n+1-r}\). This is a permutation of independent bosons and
preserves their form. The affine Miura map is then exactly
\[
 \mu:\ S_i v\longmapsto
 [\partial^{n-i}]\,
           (\partial+h_1)\cdots(\partial+h_n).
 \tag{WP.23}
\]
The bracket denotes the coefficient after moving all derivatives right.

For \(n=2\), before the traceless restriction, this is
\(S_1\mapsto b_1+b_2\) and \(S_2\mapsto b_1b_2+T b_1\).
With \(b_2=-b_1\), \(Q/2=-S_2\) by the actual calculation following
(SL.L23). Writing \(b=2b_1\), we obtain
\[
 Q/2\longmapsto b^2/4-Tb/2,\qquad \{b_\lambda b\}=2\lambda.
 \tag{WP.24}
\]
Thus the derivative sign agrees with the rank-one free-field Miura
formula. For three factors in the \(h\)-ordering, the two nonleading
coefficients are
\[
 \begin{aligned}
 \mu(S_2)&=h_1h_2+h_1h_3+h_2h_3+T h_2+2T h_3,\\
 \mu(S_3)&=h_1h_2h_3+(h_1+h_2)T h_3
                    +(T h_2)h_3+T^2h_3.
 \end{aligned}
 \tag{WP.25}
\]
These follow by twice using \(\partial a=a\partial+Ta\); they display
the order-dependent lower terms explicitly.

##### Trace-zero restriction in the deformed family

It would be incorrect to impose \(\sum_i b_i=0\) as a quotient of
the deformed raw Heisenberg algebra: its trace boson has nonzero form
\(\varepsilon n\). Instead split it orthogonally. Put
\[
 c=\frac1n\sum_i b_i,\qquad \bar b_i=b_i-c,\qquad
 \sum_i\bar b_i=0.
\]
Then
\[
 [\bar b_i{}_\lambda\bar b_j]
       =\varepsilon(\delta_{ij}-1/n)\lambda,\qquad
 [c_\lambda\bar b_i]=0,\qquad
 [c_\lambda c]=(\varepsilon/n)\lambda .
 \tag{WP.26}
\]
The same relations hold in every mode, and an invertible linear
change of the free polynomial variables gives this tensor splitting.

The image of the trace current is \(\sum_i b_i\): all ghosts cancel
in (WP.14). Every off-diagonal current in (WP.8) is independent of
the common boson component \(c\), and every diagonal current is \(c\)
plus a field in the trace-zero bosons and ghosts. This is an induction
on (WP.8). If \(J_{ab}\) is shifted by \(\delta_{ab}c\) and \(b\)
by \(c\), the two new terms in \(F_i\) are
\(+\gamma_i c-\gamma_i c=0\); the other off-diagonal entries are
unchanged. The diagonal entries acquire exactly \(c\).
Thus restriction to the affine \(\mathfrak{sl}_n\) subalgebra has
target
\[
 \rho_\varepsilon^{\,0}:V_{(-n+\varepsilon)\operatorname{tr},\,\mathfrak{sl}_n}
          \longrightarrow\mathcal F_n\otimes
                               \mathcal H_{\varepsilon,\mathfrak h_0}.
 \tag{WP.27}
\]
No quotient killing a nonzero Heisenberg form was taken. In the
critical fibre its determinant images are (WP.22) with the \(b_i\)
replaced by \(\bar b_i\), so the coefficient of \(\partial^{n-1}\)
is zero. The form on \(\mathfrak h_0\) is exactly
\(\varepsilon\operatorname{tr}|_{\mathfrak h_0}\), as required.

##### Taking the first-order bracket

Use the intrinsic critical Poisson vertex algebra proved in §3.7.1,
(PV.14)–(PV.23), with deformation direction \(B=\operatorname{tr}\).
We give the exact lift and coefficient comparison needed here. For a
critical invariant state \(a\), choose a PBW lift
\(\widetilde a\) in the deformed vacuum. Its coefficients are in
\(R[\varepsilon]\); the PBW basis makes this module free there.
Write the singular state-field bracket as
\([a_\lambda b]=\sum_{j\geq0}\lambda^j a_{(j)}b/j!\).
The intrinsic critical bracket is
\[
 \{a_\lambda b\}_{\rm crit}
    =\left.\varepsilon^{-1}
          [\widetilde a_\lambda\widetilde b]\right|_{\varepsilon=0}.
 \tag{WP.28}
\]
The divisibility and lift independence used here can be checked
directly. At the critical fibre invariant fields commute with every
current by (UC.14), and then with every reconstructed field by the
finite normal recursion. Thus their singular bracket with every
state is zero. This gives divisibility by \(\varepsilon\).
Replacing a lift by \(\varepsilon d\) changes (WP.28) by a
critical singular bracket with the other invariant state, hence by
zero. Jacobi with a current shows that every coefficient of (WP.28)
is invariant: divide
\[
 [x_\nu[\widetilde a_\lambda\widetilde b]]
 =[[x_\nu\widetilde a]_{\lambda+\nu}\widetilde b]
       +[\widetilde a_\lambda[x_\nu\widetilde b]]
\]
by \(\varepsilon\). Each inner current bracket on the right is
divisible by \(\varepsilon\); its quotient has zero critical
bracket with the remaining invariant. This is the same operation as
(PV.14). Its sesquilinearity, skew symmetry, Jacobi and Leibniz were
proved in (PV.16)–(PV.23) by finite residues and first- and second-order
parameter division. The present comparison needs no additional center
theorem.

The free-boson first-order bracket is
\[
 \{b_i{}_\lambda b_j\}_{\rm bos}=\delta_{ij}\lambda,\qquad
 \{\bar b_i{}_\lambda\bar b_j\}_{\rm bos}
                         =(\delta_{ij}-1/n)\lambda .
 \tag{WP.29}
\]
It is obtained by dividing (WP.2) or (WP.26) by \(\varepsilon\).
The derivative and polynomial product rules follow from the same
finite contraction rule: two or more boson contractions contribute
at least \(\varepsilon^2\), so only one contraction remains to first
order. This defines the bracket on every differential polynomial.

The map (WP.13) preserves the deformed singular products. Moreover
its critical invariant images \(\mu(a),\mu(b)\) are central in the
*entire* critical free-field target, by (WP.17). Write
\[
 \rho_\varepsilon(\widetilde a)=\mu(a)+\varepsilon A,\qquad
 \rho_\varepsilon(\widetilde b)=\mu(b)+\varepsilon B
\]
in the free polynomial Fock module. Every coefficient is a finite
polynomial, so this is an ordinary divisibility assertion. After
taking the bracket and dividing by \(\varepsilon\), the two possible
correction terms specialize to
\([A_\lambda\mu(b)]_0+[\mu(a)_\lambda B]_0=0\).
The term with both corrections is already divisible by
\(\varepsilon^2\). Therefore
\[
 \boxed{\quad
 \mu\bigl(\{a_\lambda b\}_{\rm crit}\bigr)
             =\{\mu(a)_\lambda\mu(b)\}_{\rm bos}.
 \quad}
 \tag{WP.30}
\]
Normal products and \(T\) are preserved by (WP.13); on the critical
boson algebra they are the ordinary polynomial product and
derivation. Equations (WP.23), (WP.27), (WP.29) and (WP.30)
prove the all-\(n\) affine-critical-to-boson Miura Poisson map.
The correction terms would not vanish for a general Cartan
projection. Their vanishing here comes from the deformed field
homomorphism and critical ghost cancellation.

##### Independence and ordinary families

One can also verify injectivity for the stated polynomial centers.
Give every boson creation variable polynomial degree one.
The highest degree part of \(T^r\mu(S_i)/r!\) is the coefficient
of \(t^r\) in \(e_i(b_1(t),\ldots,b_n(t))\), where
\(b_j(t)=\sum_{r\geq0}b_{j,-r-1}t^r\). This follows because
\(T^r b_{j,-1}/r!=b_{j,-r-1}\) and Leibniz gives the coefficient
convolution. Terms involving a commutation with \(\partial\) have
fewer boson factors.

These elementary-symmetric jet coefficients are algebraically
independent. At jet order zero the Jacobian of
\((b_1,\ldots,b_n)\mapsto(e_1,\ldots,e_n)\) is invertible whenever
the \(b_i\) are distinct. Indeed if a tangent vector leaves all
coefficients of \(\prod_j(z+b_j)\) unchanged, evaluation at
\(z=-b_i\) gives
\(\dot b_i\prod_{j\ne i}(b_j-b_i)=0\), hence \(\dot b_i=0\).
At every higher jet order the new coefficient depends on the new
\(b_{j,-r-1}\) with exactly this same Jacobian; all other terms
involve earlier coefficients. The finite-jet differential is
therefore block triangular and invertible at a tuple of distinct
constant entries.

For completeness, invertible differential implies dominance here
without a smooth-image theorem. Translate that tuple and its image
to zero. The substitution in formal power series has an invertible
linear part. A nonzero polynomial relation has a lowest nonzero
homogeneous term, whose substitution by that linear part is still
nonzero; higher terms cannot cancel it. Thus no polynomial relation
exists. In the trace-zero case choose distinct entries summing to
zero. Restrict the same tangent argument to \(\sum_i\dot b_i=0\);
with \(e_1\) fixed, the remaining coefficients \(e_2,\ldots,e_n\)
have invertible differential. Such entries exist over every
characteristic-zero field, for example distinct integers shifted
by their average. Any relation among infinitely many coefficients
occurs already at a finite jet order.

The polynomial critical-center theorem (SL.C1), and the scalar
factor of §3.5, identify the source generators with the divided
translates of these actual determinant states. A nonzero polynomial
in them has a nonzero component of highest weighted degree, with
weight \(i\) for the degree-\(i\) determinant generator. Its image
has the nonzero highest boson-degree polynomial just described.
Hence the Miura map is injective on these centers:
\[
 k[T^rS_i/r!:1\leq i\leq n,\ r\geq0]
           \hookrightarrow k[b_{j,-a}:1\leq j\leq n,\ a\geq1],
 \tag{WP.31}
\]
and on the traceless source retain \(2\leq i\leq n\) and
\(\sum_j b_{j,-a}=0\). This is not a surjectivity claim onto the
boson algebra.

All relations, normal products, coefficient comparisons and
cancellations above are finite rational formulas. Their field
constructions have polynomial Fock bases over \(R[\varepsilon]\);
in particular multiplication by \(\varepsilon\) is injective even
when \(R\) has nilpotents. The polynomial critical-center identities
extend to every ordinary \(R\) by the earlier finite-energy kernel
argument (GJ.P5). The injective map over \(k\) also remains injective
after tensoring with \(R\), because every \(k\)-linear injection
has a basis splitting. Thus (WP.30) and (WP.31) hold for all such
families, with no inference from their field-valued points.

The construction for a direct sum uses the tensor product of the
separate Fock modules. Cross-current and cross-boson contractions
are zero, so it gives the product Miura Poisson map. For
\(\mathfrak{gl}_1\) it is the identity boson construction. For the
trivial Lie algebra, or \(\mathfrak{sl}_1=0\), it is the identity
of the coefficient ring.

The comparison below summarizes the proved mechanism; each arrow
has the indicated construction.
\[
 \begin{array}{ccc}
 V_{\kappa_{\rm crit}+\varepsilon\operatorname{tr}}
    &\xrightarrow{\ \rho_\varepsilon\ {\rm of}\ (WP.7)-(WP.13)\ }
    &\mathcal F_n\otimes\mathcal H_{\varepsilon}\\
 \mathcal Z_{\rm crit}\ \subset\
             V_{\kappa_{\rm crit}}
    &\xrightarrow{\ \mu\ {\rm of}\ (WP.17)-(WP.23)\ }
    &1\otimes\mathcal H_0 .
 \end{array}
 \tag{WP.32}
\]
The lower arrow is the critical restriction of the upper one.
The root contribution is (WP.15)–(WP.16); division of singular
products by the same \(\varepsilon\) is (WP.28)–(WP.30).
The trace-zero target is the orthogonal subalgebra (WP.26), not a
quotient of a nonzero-form boson.

##### Every Fourier mode and the full completed map

The same comparison preserves the brackets on the completed centers,
with their actual smooth topology. Let \(a,b\) be homogeneous critical
states of energies \(D_a,D_b\), and write
\(\{a_\lambda b\}=\sum_j\lambda^j h_j/j!\).
Use normalized Fourier fields
\(Y(a,z)=\sum_p S_{a,p}z^{-p-D_a}\), and similarly for \(b\)
and the boson states \(\mu(a),\mu(b)\). The universal product and
commutator proof (PV.8)–(PV.10) gives, by (PV.24), for every pair of
integer indices,
\[
 \{S_{a,p},S_{b,q}\}_{\rm completed}
  =\sum_{j\geq0}\binom{p+D_a-1}{j}S_{h_j,p+q}.
 \tag{WP.33}
\]
The sum is finite by locality, including for negative \(p\).
Applying the same formula to the abelian datum of the boson algebra
uses exactly \(\{b_{i,p},b_{j,q}\}=p\delta_{ij}\delta_{p,-q}\),
or its trace-zero restriction. Equation (WP.30) identifies its state
coefficients with \(\mu(h_j)\).

The continuous ordered Miura algebra embedding (MC.14)–(MC.16) sends
each actual determinant Fourier mode to the corresponding coefficient
of \((\partial+h_1(z))\cdots(\partial+h_n(z))\). Our boson relabeling
in (WP.23) gives exactly this map; normal products and derivatives give
the same assertion for every polynomial state \(h_j\). Thus (WP.33)
proves bracket preservation on the polynomial algebra of all central
Fourier generators. The universal product identity is used here on
every smooth boson module, so its zero modes and nonnegative modes are
retained. An action on the boson vacuum alone, where those modes
vanish, would not establish this conclusion.

The completed brackets of §3.7.5, (CP.2)–(CP.6), are jointly
continuous: the PBW parameter division is unique, its cutoff kernels
are saturated, and completed multiplication is continuous. The
ordered Miura embedding is continuous by its exact finite mode
cutoffs. The polynomial Fourier algebra is dense in the full type A
center by the finite-cutoff exhaustion of §3.6.3. Take polynomial
approximants to both inputs. The equality just proved passes to their
limits in the separated completed boson algebra. Hence
\[
 \boxed{\quad
 \widehat\mu\bigl(\{u,v\}_{\rm crit}\bigr)
       =\{\widehat\mu(u),\widehat\mu(v)\}_{\rm bos}
 \quad\bigl(u,v\in Z(\widehat A_{\rm crit})\bigr).
 \quad}
 \tag{WP.34}
\]
This is the full continuous type A Miura Poisson embedding, over
every ordinary coefficient algebra in the completed coefficient sense.
It does not make a cutoff quotient or the ordinary vacuum restriction
a Poisson quotient; (CP.17)–(CP.18) show why those different claims
fail. Products use the componentwise map and a common cutoff.

**Reading and scope.** Edward Frenkel's freely available
[*Lectures on the Langlands program and conformal field theory*,
hep-th/0512172v1](https://arxiv.org/abs/hep-th/0512172v1),
subsection “Free field realization”, explains the rescaled
rank-one construction and the Miura formula. The recursive matrix
formulas, all their contraction cancellations, the determinant
ordering and the first-order argument have been given here.
They prove the ordinary differential-algebra Poisson Miura map
and its full smooth completed extension for all type A factors.
They do not prove a global sheaf comparison,
a geometric or Satake central-line convention, a derived-family
statement, or a chiral factorization comparison. Such conclusions
require their own constructions.

#### 3.7.5. The Poisson bracket on the full completion and its quadratic normalization

Fix an invariant symmetric form \(B\) on the finite-dimensional Lie algebra \(\mathfrak g\). For the construction of the Poisson bracket it may be degenerate. For the quadratic calculation below we require it to be nondegenerate. Let \(R\) be any ordinary commutative characteristic-zero coefficient algebra. Use the form family
\[
\kappa_\varepsilon=-\tfrac12\mathrm{Kil}+\varepsilon B,
\qquad R_\varepsilon=R[\varepsilon],\qquad K=1.
\tag{CP.1}
\]
Denote its polynomial affine enveloping algebra by \(A_\varepsilon\), and form its smooth completion using the left ideals
\(I_{N,\varepsilon}=A_\varepsilon t^N\mathfrak g_R[t]\), as in (CW.1). The bracket Jacobi identity uses only invariance of the coefficient form, so the polynomial family is an affine Lie algebra over \(R_\varepsilon\). The ordered-word PBW proof and the finite-word bounds (CW.2)–(CW.5) apply over this ring. Consequently its quotients are free \(R_\varepsilon\)-modules with the same ordered monomial lists as at \(\varepsilon=0\), and (CW.7)–(CW.14) construct its complete algebra and continuous multiplication.

Write \(\widehat A_\varepsilon\) for this completion and \(\widehat A_0\) for the critical completion over \(R\). Stagewise reduction gives a continuous surjective algebra homomorphism \(\rho:\widehat A_\varepsilon\to\widehat A_0\). It has a continuous \(R\)-linear section \(s\): keep the coefficients of every ordered monomial constant in \(\varepsilon\), at each cutoff. The transition maps retain or delete exactly the same monomials, so these sections are compatible. Multiplication by \(\varepsilon\) is injective on every quotient, since its PBW coordinates are polynomials in \(\varepsilon\), and hence on the completion. If \(a\) reduces to zero, each component uniquely equals \(\varepsilon b_N\); the uniqueness makes the \(b_N\) compatible. Thus
\[
0\longrightarrow\widehat A_\varepsilon
 \xrightarrow{\ \varepsilon\ }\widehat A_\varepsilon
 \xrightarrow{\ \rho\ }\widehat A_0\longrightarrow0
\tag{CP.2}
\]
is exact. These statements use free PBW quotients and exact division by the parameter, not an unproved flatness assertion for an infinite inverse limit over \(R[\varepsilon]\).

Let \(J_{N,\varepsilon}\) be the kernel of projection to the \(N\)-th quotient. It is saturated for multiplication by \(\varepsilon\): if \(\varepsilon a\in J_{N,\varepsilon}\), the injectivity on that free quotient gives \(a\in J_{N,\varepsilon}\). Also \(s(J_{N,0})\subset J_{N,\varepsilon}\). These two facts are the topology control needed for parameter division.

Put \(Z_R=Z(\widehat A_0)\). For \(u,v\in Z_R\), choose any lifts \(\widetilde u,\widetilde v\in\widehat A_\varepsilon\). Their commutator reduces to zero and is uniquely divisible by \(\varepsilon\), by (CP.2). Define
\[
\{u,v\}_B=\rho\left(\frac{[\widetilde u,\widetilde v]}{\varepsilon}\right).
\tag{CP.3}
\]
This is independent of both lifts. Indeed replacing them by
\(\widetilde u+\varepsilon a,\widetilde v+\varepsilon b\) changes the quotient by
\([a,\widetilde v]+[\widetilde u,b]+\varepsilon[a,b]\). Its reduction is
\([\rho(a),v]+[u,\rho(b)]=0\), because \(u,v\) are central in the entire critical completion. They need not have lifts which are central at the deformed level.

The result is central. If \(x_m\) is any polynomial current, both \([x_m,\widetilde u]\) and \([x_m,\widetilde v]\) are divisible by \(\varepsilon\). Associative Jacobi gives
\[
\left[x_m,\frac{[\widetilde u,\widetilde v]}{\varepsilon}\right]
=\left[\frac{[x_m,\widetilde u]}{\varepsilon},\widetilde v\right]
 +\left[\widetilde u,\frac{[x_m,\widetilde v]}{\varepsilon}\right].
\tag{CP.4}
\]
Each bracket on the right reduces to zero by centrality of \(u,v\). Therefore (CP.3) commutes with every current, and the completed-center criterion (CW.16) proves that it lies in \(Z_R\).

The bracket is \(R\)-bilinear and antisymmetric because the commutator is. For the product rule choose \(\widetilde u\widetilde v\) as a lift of \(uv\). Its commutator with a lift of \(w\) is
\(\widetilde u[\widetilde v,\widetilde w]+[\widetilde u,\widetilde w]\widetilde v\). Exact division and reduction give
\[
\{uv,w\}_B=u\{v,w\}_B+\{u,w\}_Bv.
\tag{CP.5}
\]
For Jacobi, the element \([\widetilde u,\widetilde v]/\varepsilon\) is a lift of the central element \(\{u,v\}_B\), by (CP.4). Its commutator with \(\widetilde w\) is again divisible by \(\varepsilon\). Hence every double commutator
\([[\widetilde u,\widetilde v],\widetilde w]\) is uniquely divisible by \(\varepsilon^2\). The sum of the three such commutators is zero in an associative algebra. Divide that equality twice and reduce to obtain
\[
\{\{u,v\}_B,w\}_B+\{\{v,w\}_B,u\}_B+\{\{w,u\}_B,v\}_B=0.
\tag{CP.6}
\]
Thus (CP.3) makes the entire completed center a Poisson algebra.

Its bracket is jointly continuous. Use the continuous section \(s\) in (CP.3). Given a required output cutoff \(N\) and a pair \((u,v)\), joint continuity of completed multiplication gives sufficiently small neighborhoods of \(s(u),s(v)\) for the commutator difference to lie in \(J_{N,\varepsilon}\). The section carries sufficiently small center perturbations into those neighborhoods. Both commutators, and hence their difference, are divisible by \(\varepsilon\); saturation of \(J_{N,\varepsilon}\) places the divided difference in that same kernel. Reduction then places the bracket difference in \(J_{N,0}\). This proves the stated continuity at every pair. It does not require any individual cutoff kernel to be a Poisson ideal.

Every ordinary map \(R\to R'\) gives the stagewise PBW coefficient maps and the corresponding completed algebra maps. These preserve products, parameter multiplication and reduction. The unique division by \(\varepsilon\) is coefficientwise polynomial division and commutes with the coefficient map. Therefore (CP.3) commutes with every such base change, without a flatness assumption on \(R'\) over \(R\).

Coordinate substitution preserves the residue cocycle for the whole form family (CP.1), by (RC.C7). The cofinality proof (CW.22)–(CW.23) gives its continuous algebra automorphism on \(\widehat A_\varepsilon\), including nilpotent coordinate constants. It fixes \(\varepsilon\) and commutes with reduction. Applying it to any two lifts in (CP.3), and using lift independence, proves
\[
\sigma_\phi(\{u,v\}_B)=\{\sigma_\phi(u),\sigma_\phi(v)\}_B.
\tag{CP.7}
\]
The completed critical center is therefore a coordinate-equivariant topological Poisson algebra for the chosen deformation direction \(B\).

The quotient mechanism can be displayed accurately. Set
\(\mathcal P_\varepsilon=\rho^{-1}(Z_R)\). Equation (CP.4) says that the divided commutator of two of its elements again lies in \(\mathcal P_\varepsilon\), so
\[
\begin{array}{ccc}
\mathcal P_\varepsilon\times\mathcal P_\varepsilon
&\xrightarrow{\ [\ ,\ ]/\varepsilon\ }&\mathcal P_\varepsilon\\
{\scriptstyle \rho\times\rho}\downarrow&&\downarrow{\scriptstyle\rho}\\
Z_R\times Z_R&\xrightarrow{\ \{\ ,\ \}_B\ }&Z_R.
\end{array}
\tag{CP.8}
\]
*The upper row concerns lifts whose reductions are central; it does not require the lifts themselves to be central. Exact PBW parameter division (CP.2), lift independence and (CP.4) prove the square. The saturated cutoff kernels prove continuity. Coordinate substitution on the same family proves (CP.7).*

We compute the quadratic bracket without a presumed Virasoro representation. Now assume \(B\) nondegenerate, choose dual bases \(a_\alpha,a^\alpha\), and retain the half-Casimir state and universal modes from (GQ.2)–(GQ.3):
\[
Q_B=\tfrac12\sum_\alpha(a_\alpha)_{-1}(a^\alpha)_{-1}v,
\qquad
\mathcal Q(z)=\sum_{m\in\mathbb Z}S_m z^{-m-2}.
\tag{CP.9}
\]
The finite current calculation (GQ.7) is valid at every coefficient form, hence at (CP.1). With
\(B(C_Bx,y)=\mathrm{Kil}(x,y)\), the operator \(K_{\kappa_\varepsilon}\) is \(-C_B/2+\varepsilon\operatorname{Id}\). Therefore the actual universal commutators are
\[
[x_r,S_m]=\varepsilon r x_{r+m}.
\tag{CP.10}
\]
Their validity on all smooth modules, already proved in (GQ.7), and the natural-operator interpretation of §3.6.1 make them equalities in \(\widehat A_\varepsilon\).

For every integer \(l\), including \(l<-1\), define the coefficient derivation
\(D_l(x_r)=r x_{r+l}\), \(D_l(1)=0\). Its bracket defect is
\(r(r+s+l)\kappa_\varepsilon(x,y)\delta_{r+s+l,0}=0\), so it is a derivation of the polynomial current algebra. Taking a tail bound \(M\ge\max(N,N-l)\) proves \(D_l I_{M,\varepsilon}\subset I_{N,\varepsilon}\); thus it extends continuously to the completion. Unlike the vacuum operator in (GQ.11), this is a coefficient derivation. No action on the vacuum is asserted when \(l<-1\).

We extend the normal-order calculation (GQ.12) to all these integers, retaining its finite boundary. Put \(\theta(j)=1\) for \(j\ge0\) and zero otherwise. Differentiating a normally ordered pair gives
\[
\begin{aligned}
D_l(:a_jb_{n-j}:)
&=j:a_{j+l}b_{n-j}:+(n-j):a_jb_{n-j+l}:\\
&\quad+j(\theta(j+l)-\theta(j))[a_{j+l},b_{n-j}].
\end{aligned}
\tag{CP.11}
\]
This follows by comparing the two factor orders before and after the first index crosses zero. Reindex the first ordinary sum: its coefficient becomes \(j-l\), and adding the second gives \(n-l\). The sum of the boundary Lie brackets is zero because
\(\sum_\alpha[a_\alpha,a^\alpha]=0\), as proved in (GQ.4) by the symmetry of the inverse-form tensor. The scalar boundary is
\[
\tfrac12\operatorname{tr}(K_{\kappa_\varepsilon})\delta_{n+l,0}
\sum_jj(j+l)(\theta(j+l)-\theta(j)).
\]
For \(l>0\), set \(j=-s\), \(1\le s\le l\), obtaining the sum of \(s^2-ls\), equal to \(-(l^3-l)/6\) by the finite sums already evaluated before (GQ.12). For \(l=-d<0\), the crossing indices are \(j=0,\ldots,d-1\), with crossing sign minus. Their sum is
\(\sum_{j=0}^{d-1}j(d-j)=(d^3-d)/6=-(l^3-l)/6\).
For \(l=0\), it is empty. This proves all integer cases. Every computation is finite modulo a required cutoff after choosing the larger tail bound for \(D_l\); only this finite crossing interval remains after reindexing. Consequently
\[
D_lS_n=(n-l)S_{n+l}
 +\gamma_{\kappa_\varepsilon}(l^3-l)\delta_{n+l,0},
\qquad
\gamma_{\kappa_\varepsilon}
=\frac{\operatorname{tr}(C_B)}{24}
 -\varepsilon\frac{\dim\mathfrak g}{12}.
\tag{CP.12}
\]

Equation (CP.10) says that \(\operatorname{ad}(S_l)=-\varepsilon D_l\) on every current generator. Both sides are continuous derivations on the actual completed algebra. Their equality extends to finite products, and density of the polynomial algebra extends it to every completed element. Applying it to (CP.12) gives the exact level-family formula
\[
[S_l,S_n]
=\varepsilon(l-n)S_{l+n}
 -\varepsilon\gamma_{\kappa_\varepsilon}(l^3-l)\delta_{l+n,0}.
\tag{CP.13}
\]
This supplies every Fourier mode, rather than only the vacuum-negative modes. Write \(\gamma_B=\operatorname{tr}(C_B)/24\), as in (GQ.14). Division and reduction in (CP.3) now yield
\[
\boxed{\{S_l,S_n\}_B=(l-n)S_{l+n}
 -\gamma_B(l^3-l)\delta_{l+n,0}.}
\tag{CP.14}
\]

The same calculation determines the intrinsic vacuum \(\lambda\)-bracket of §3.7.1. The vertex index \(j\) of the weight-two field corresponds to \(S_{j-1}\). At every level its vacuum creation series implies \(S_m v=0\) for \(m\ge-1\), \(S_{-2}v=Q_B\), and \(S_{-3}v=TQ_B\). Thus
\(S_{j-1}Q_B=[S_{j-1},S_{-2}]v\).
By (CP.13), its parameter quotient at the critical level is \(TQ_B\) for \(j=0\), \(2Q_B\) for \(j=1\), zero for \(j=2\), and \(-6\gamma_Bv\) for \(j=3\); all higher \(j\) give zero. Multiplying by \(\lambda^j/j!\) proves
\[
\boxed{\{Q_B{}_{\lambda}Q_B\}_B=(T+2\lambda)Q_B-\gamma_B\lambda^3.}
\tag{CP.15}
\]
This proof uses the actual level-family operators, their source creation values and the definition of the first-order bracket. It does not infer (CP.15) merely from the coordinate anomaly.

For \(\mathfrak{sl}_n\) with \(B=\operatorname{tr}\), (GQ.20) proves
\(\gamma_B=\gamma_n=n(n^2-1)/12\). The exact determinant identity after (GQ.20) gives \(w_2=-Q_B\). Hence its raw normalized scalar coefficient has
\[
\boxed{\{w_2{}_{\lambda}w_2\}
=-(T+2\lambda)w_2-\gamma_n\lambda^3.}
\tag{CP.16}
\]
This is the quadratic Miura and scalar-oper normalization in §3.7.3. The sign of the cubic term and the ordered derivative in (MC.9) are both retained. An unnormalized matrix operator with nonzero first coefficient has its separate trace terms; (CP.16) concerns the traceless normalized operator. The generic quadratic field still has (CP.14)–(CP.15) for the half-Casimir of every nondegenerate invariant \(B\).

We can now exhibit why continuity does not make every displayed quotient Poisson. Take \(\mathfrak{sl}_2\) and \(B=\operatorname{tr}\), so the critical quadratic state is nonzero by its PBW symbol. At cutoff \(N=1\), (UC.20) gives \(S_1\in J_{1,0}\). But
\[
\{S_1,S_{-3}\}_B=4S_{-2}\notin J_{1,0}.
\tag{CP.17}
\]
The last nonvanishing follows from (CT.13): at this cutoff \(S_{-2}\) has the nonzero quadratic invariant symbol of Laurent coefficient order zero. Thus the cutoff kernel is not a Poisson ideal. The ordinary vacuum restriction (PC.15) has the same issue in a different range: it kills \(S_0\), while
\[
\{S_0,S_{-2}\}_B=2S_{-2}
\tag{CP.18}
\]
has nonzero vacuum value \(2Q_B\). Its kernel is therefore not a Poisson ideal either. The square (PC.16) is a commutative-algebra and coordinate square; it is not a quotient square of ordinary Poisson algebras. The vacuum center instead retains the differential \(\lambda\)-bracket of §3.7.1, whose explicit quadratic identity is (CP.15).

For an abelian direction the construction is equally concrete:
\[
\{z_m,y_n\}_B=mB(z,y)\delta_{m+n,0}.
\tag{CP.19}
\]
It follows immediately by dividing the affine bracket at \(\kappa_\varepsilon=\varepsilon B\). All zero modes have zero Poisson bracket here, although they remain nonzero central variables in (HC.8). This also shows explicitly that the deformation direction is part of the Poisson normalization.

**The full type A scalar-oper Poisson comparison.** Put \(P_R\) for the completed scalar coefficient algebra of (PC.3), and \(\Phi_R\) for the topological algebra isomorphism (PC.5). For the raw matrix case include all degrees \(1,\ldots,n\); for the trace-zero case include \(2,\ldots,n\). Let \(j_R:P_R\hookrightarrow\widehat{\mathcal H}_R\) send each scalar coefficient mode to the corresponding ordered Miura coefficient. Equations (MC.15)–(MC.16) give
\[
j_R\Phi_R=\widehat\nu_R=\widehat\mu_R.
\tag{CP.20}
\]
The last equality is the exact determinant image (WP.23), with its proved boson relabeling, on every Fourier coefficient; continuity extends it to the completion.

The image of \(j_R\) is closed. Indeed it is exactly the intersection, over all \(N\), of the inverse images of the stage images in the discrete algebras \(\mathcal H_{N,R}\). For the nontrivial inclusion, an element in this intersection has a unique preimage in each scalar stage by (MC.15). Compatibility of the stage maps and their injectivity makes those preimages compatible, producing an element of \(P_R\). Thus the image is closed, and its inverse carries the induced topology by the same exact cutoff argument.

The finite coefficient formulas (AP.11), or (AP.17) after trace-zero reduction, define the scalar Poisson vertex bracket. Their Fourier coefficients use the universal finite locality sum (PV.24). A nonlinear coefficient expression can involve an infinite mode convolution before imposing a cutoff. It nevertheless defines an element of \(P_R\): at cutoff \(N\), each coefficient mode of degree \(i\) has upper bound \(i(N-1)\); a fixed sum of the indices in a finite monomial then bounds each index below as well. Each convolution is thus finite at that cutoff, and these finite polynomials are compatible. Derivatives contribute their explicit integer mode factors and do not invalidate the bounds.

The resulting bracket of scalar generators has exactly the boson Miura image. Equations (AP.9) and (AP.14) prove every differential coefficient bracket, and the same universal residue argument gives the Fourier formula for every integer index. Leibniz consequently defines brackets of polynomial scalar inputs with values in the completed image \(j_R(P_R)\). No closure of the uncompleted polynomial mode algebra is asserted. Polynomial inputs are dense in \(P_R\), because every finite stage is a polynomial algebra. The boson bracket is jointly continuous by the abelian instance of (CP.1)–(CP.7). Closedness of the completed image and continuity of the inverse therefore give a unique jointly continuous extension of the scalar bracket to all of \(P_R\). Its Poisson identities follow by injection into the already proved boson Poisson algebra. We denote it by \(\{\ ,\ \}_{\mathrm{AGD}}\), with the positive boson sign of (AP.1).

For \(u,v\) in the full type A completed center, (WP.34) and (CP.20) now give
\[
\begin{aligned}
j_R\Phi_R(\{u,v\}_{\operatorname{tr}})
&=\{j_R\Phi_R(u),j_R\Phi_R(v)\}_{\mathrm{bos}}\\
&=j_R\{\Phi_R(u),\Phi_R(v)\}_{\mathrm{AGD}}.
\end{aligned}
\]
Cancel the injective map \(j_R\). We have proved the complete topological Poisson isomorphism
\[
\boxed{\Phi_R:
\bigl(Z(\widehat A_{\mathrm{crit},R}),\{\ ,\ \}_{\operatorname{tr}}\bigr)
\xrightarrow{\ \sim\ }
\bigl(P_R,\{\ ,\ \}_{\mathrm{AGD}}\bigr).}
\tag{CP.21}
\]
All lower terms and signs in this second scalar Adler–Gelfand–Dickey bracket are the explicit formulas (AP.11)–(AP.18); its quadratic normalization is (CP.16). The scalar-oper interpretation retains the geometric and invariant-theory premises explicitly stated before (PC.5). Section 3.8 independently constructs the ordinary principal type A matrix Hamiltonian reduction and proves its equality with this bracket; that equality requires the actual moment-normalizer and classical free-field arguments there.

The coordinate actions agree by (PC.13), (MC.22) and the density transport (AP.25). Their Poisson property follows from (CP.7) and (MC.23). Consequently the following is a square of continuous Poisson maps:
\[
\begin{array}{ccc}
Z(\widehat A_{\mathrm{crit},R})&\xrightarrow{\ \Phi_R\ }&P_R\\
{\scriptstyle\sigma_\phi}\downarrow&&\downarrow{\scriptstyle\sigma_\phi^{\mathrm{Op}}}\\
Z(\widehat A_{\mathrm{crit},R})&\xrightarrow{\ \Phi_R\ }&P_R.
\end{array}
\tag{CP.22}
\]
*The horizontal maps are the coefficient isomorphism (PC.5), now Poisson by the actual deformed field map (WP.30)–(WP.34) and the scalar factorization formulas (AP.7)–(AP.18). The vertical maps use the inverse density action, with the essential Cartan shift (MC.20). Exact mode cutoffs give the topology. This square concerns the whole completion; the forbidden-mode counterexamples (CP.17)–(CP.18) still apply to cutoff and vacuum restrictions.*

The regular vacuum comparison likewise gives a Poisson vertex algebra isomorphism onto the scalar differential coefficient algebra: both sides inject into the regular bosons by (MC.13) and (AP.13), their generator images agree by (WP.23), and (WP.30) proves preservation of every \(\lambda\)-bracket. This is a state-algebra comparison, rather than an ordinary Poisson quotient of (CP.21). Direct sums of type A factors use the componentwise brackets and a common cutoff. Additional framed central directions have exactly the linear bracket (CP.19) for their specified deformation form, and cross brackets vanish when that form is a direct sum.

The construction proves the complete intrinsic critical Poisson algebra for every finite-dimensional affine datum, naturality under ordinary coefficient maps and the full coordinate action. Naturality does not assert an unproved center base-change isomorphism in other types. It proves the quadratic coefficient normalization for every nondegenerate invariant form and the full type A scalar-oper Poisson comparison at the stated premises. It supplies no basic lifts in other types, geometric Satake theorem, localization argument, factorization descent or derived-family theorem.


### 3.8. Principal Drinfeld–Sokolov Hamiltonian reduction

#### 3.8.1. The classical affine PVA and principal Hamiltonian reduction

Let \(k\) be a characteristic-zero field, \(R\) an ordinary commutative \(k\)-algebra, and \(n\geq1\). We first take \(\mathfrak g=\mathfrak{gl}_n(k)\), with
\[
 B(x,y)=\operatorname{tr}(xy),\qquad
 \mathcal A_R=R[J_x^{(r)}:x\in\mathfrak g,\ r\geq0]_{\text{linear in }x},
 \qquad TJ_x^{(r)}=J_x^{(r+1)},\quad T|_R=0.
 \tag{DP.1}
\]
The current labels are linear over \(k\). Thus choosing a basis \(e_i\) identifies \(\mathcal A_R\) with the polynomial algebra in \(u_i^{(r)}=J_{e_i}^{(r)}\). No algebraic closure or reducedness is required. For \(n\geq2\), exactly the same construction works with \(\mathfrak{sl}_n(k)\) and the restricted trace form. We construct that algebra directly, rather than imposing the trace-zero relation on the unreduced \(\mathfrak{gl}_n\) bracket.

**The current bracket and its complete extension.** Prescribe the positive convention
\[
 H_{ij}(\lambda)=\{u_i{}_\lambda u_j\}
   =J_{[e_i,e_j]}+B(e_i,e_j)\lambda,
 \qquad
 \{J_x{}_\lambda J_y\}=J_{[x,y]}+\operatorname{tr}(xy)\lambda.
 \tag{DP.2}
\]
It agrees with the positive boson convention of (AP.1). For differential polynomials \(F,G\), define
\[
 \boxed{\{F_\lambda G\}
  =\sum_{i,j,r,s}
    \frac{\partial G}{\partial u_j^{(s)}}
    (\lambda+T)^s
    H_{ij}(\lambda+T)
    (-\lambda-T)^r
    \frac{\partial F}{\partial u_i^{(r)}}.}
 \tag{DP.3}
\]
Here \(H_{ij}(\lambda+T)=J_{[e_i,e_j]}+B(e_i,e_j)(\lambda+T)\), and each displayed \(T\) acts on everything to its right. Each sum is finite because \(F,G\) involve finitely many jet variables. The formula is a polynomial in \(\lambda\) with coefficients in \(\mathcal A_R\), and is independent of the chosen basis: it is the contraction of the two polynomial differentials with the bilinear current bracket (DP.2).

We prove all its identities. Differentiating \(TF=\sum_{i,r}u_i^{(r+1)}F_{i,r}\), where \(F_{i,r}=\partial F/\partial u_i^{(r)}\), gives
\[
 (TF)_{i,r}=T F_{i,r}+F_{i,r-1},\qquad F_{i,-1}=0.
 \tag{DP.4}
\]
In (DP.3), the second term is reindexed by \(r\mapsto r+1\). Its operator \(-\lambda-T\) combines with the first term's \(T\) to give \(-\lambda\). Applying (DP.4) to \(G\) instead, the derivative of its coefficient and the extra \(\lambda+T\) combine by the ordinary product rule. Therefore
\[
 \{TF_\lambda G\}=-\lambda\{F_\lambda G\},\qquad
 \{F_\lambda TG\}=(\lambda+T)\{F_\lambda G\}.
 \tag{DP.5}
\]
Differentiating \(GH\) in the second argument of (DP.3) proves
\[
 \{F_\lambda GH\}=\{F_\lambda G\}H+G\{F_\lambda H\}.
 \tag{DP.6}
\]
For the first argument, normal-order the finite differential operators of (DP.3), with their coefficients to the left. For each power, the identity
\[
 (\lambda+T)^q(ab)
   =\sum_{v=0}^q\binom qv
       \bigl((\lambda+T)^{q-v}a\bigr)T^vb
\]
is the ordinary product rule. Applying it to the derivative of \(FH\) proves
\[
 \{FH_\lambda G\}
   =\{F_{\lambda+T}G\}_{\to}H
       +\{H_{\lambda+T}G\}_{\to}F.
 \tag{DP.7}
\]
The arrow means that the newly inserted \(T\)'s act on the factor to their right. These four rules, together with (DP.2), also prove uniqueness: expand a polynomial into products of jet generators, use both Leibniz rules, and then remove the jets by (DP.5). This expansion gives exactly (DP.3).

For clarity, we provide the algebraic locality calculation that establishes skew symmetry and Jacobi for this extension; we do not appeal to a PVA extension theorem. Use independent spatial labels \(s,t,u\). The finite local kernel for the currents is
\[
 K_{xy}(s,t)
   =J_{[x,y]}(t)\delta(s,t)
          +B(x,y)\partial_t\delta(s,t).
 \tag{DP.8}
\]
Write \(\delta(s,t)=\sum_{m\in\mathbb Z}s^{-m-1}t^m\) for the scalar formal delta. Its residue against a Laurent polynomial in \(s\) is that polynomial evaluated at \(t\); differentiation proves its derivative residue rules and \(\partial_s\delta=-\partial_t\delta\). Multiplying a coefficient at \(s\) into a delta derivative of order \(q\) uses only its Taylor jet of order \(q\) at \(t\).

These are jet-distribution symbols, not reconstructed operators on a module. Their precise algebraic meaning is finite sums of derivatives of the diagonal delta, with coefficients that are differential polynomials. The rule
\[
 a(s)\partial_t^q\delta(s,t)
   =\sum_{v=0}^q\binom qv
          (T^va)(t)\partial_t^{q-v}\delta(s,t)
 \tag{DP.9}
\]
follows by differentiating \(a(s)\delta(s,t)=a(t)\delta(s,t)\) \(q\) times. For three variables, use its two successive diagonal versions. A distribution supported on \(s=t=u\) has a unique finite form
\[
 \sum_{p,q}a_{pq}(u)
       \frac{\partial_u^p\delta(s,u)}{p!}
       \frac{\partial_u^q\delta(t,u)}{q!}.
 \tag{DP.10}
\]
Each derivative in (DP.10) acts on its indicated delta only. Uniqueness is checked by the double residue against
\((s-u)^p(t-u)^q\): it extracts \(a_{pq}\), since a derivative of a monomial is nonzero at zero at precisely its own degree. Existence in the products used here follows by the finite rule (DP.9), after replacing both diagonal conditions by \(s=u,t=u\). Equivalently these symbols act on a test polynomial by its finite Taylor jet on the diagonal. Multiplication of the two delta kernels uses two independent differences, and is therefore defined without an infinite convolution. Derivatives commute with this finite Taylor evaluation. Applying the product rule to coefficients and then (DP.9) respects the same identities, so subsequent brackets of coefficients are well defined.

Extend (DP.8) to polynomials at distinct spatial labels by the ordinary biderivation rule in both arguments, and differentiate it for jet arguments. All sums are finite sums over pairs of labelled factors. Rule (DP.9) puts each resulting kernel into diagonal normal form. Taking its formal exponential residue,
\[
 \operatorname{Res}_s e^{\lambda(s-t)}K(F(s),G(t)),
\]
is finite on that normal form. A derivative of the delta contributes a power of \(\lambda\). Differentiation in \(s\) contributes \(-\lambda\); differentiation in \(t\) contributes \(\lambda+T\). For monomials, summing over the first selected factor \(u_i^{(r)}\) and the second selected factor \(u_j^{(s)}\), and applying (DP.9) to the unselected factors, gives (DP.3). This proves that the kernel calculation is exactly our polynomial bracket, including all arrow shifts.

The kernel is antisymmetric under exchanging its two arguments and their labels. Indeed \([y,x]=-[x,y]\), \(B\) is symmetric, and
\(\partial_s\delta(t,s)=-\partial_t\delta(s,t)\). Moving its first coefficient to the second label uses (DP.9) with \(q=0\). Biderivation and differentiation preserve this antisymmetry. Its exponential residue is consequently
\[
 \{F_\lambda G\}=-\{G_{-\lambda-T}F\},
 \tag{DP.11}
\]
where the powers of \(T\) in the substitution act on the resulting coefficients. The shifts are exactly (DP.9), rather than an assumed skew-symmetry axiom.

Here is the corresponding complete reduction of Jacobi to currents. Before diagonal normal ordering, take the cyclic kernel Jacobiator. Since the bracket is an antisymmetric biderivation, its Jacobiator is a derivation in each spatial argument. For example, expanding the Jacobiator on \(H_1H_2\), the terms in which the two brackets hit different factors cancel in pairs:
\[
 K(F,H_1)K(G,H_2)+K(G,H_1)K(F,H_2)
 -K(G,H_1)K(F,H_2)-K(F,H_1)K(G,H_2)=0.
\]
The remaining terms are the Jacobiator on \(H_1\), multiplied by \(H_2\), and its counterpart on \(H_2\). Antisymmetry makes the cyclic Jacobiator alternating, giving the same assertion in the other two arguments. Differentiating an argument differentiates the Jacobiator at its spatial label. Thus induction on numbers of factors and derivatives reduces its vanishing to three undifferentiated currents.

For these currents its double exponential residue is
\[
 \begin{aligned}
 &J_{[x,[y,z]]}-J_{[y,[x,z]]}-J_{[[x,y],z]}\\
 &\quad+B(x,[y,z])\lambda
        -B(y,[x,z])\mu-B([x,y],z)(\lambda+\mu)=0.
 \end{aligned}
 \tag{DP.12}
\]
The first line vanishes by expanding the matrix commutators; their associative products cancel in pairs. Cyclic matrix trace gives
\(B(x,[y,z])=B([x,y],z)\) and
\(B(y,[x,z])=-B([x,y],z)\), cancelling the second line. To check the parameter \(\lambda+\mu\), write
\(e^{\lambda(s-u)+\mu(t-u)}
 =e^{\lambda(s-t)}e^{(\lambda+\mu)(t-u)}\)
in the term supported first on \(s=t\). The unique normal form (DP.10) implies that a zero polynomial residue has every kernel coefficient zero. Hence the current kernel Jacobiator is zero; the preceding factor and derivative induction proves it for all polynomials. Translating the same residues back to \(\lambda\)-notation proves
\[
 \boxed{\{F_\lambda\{G_\mu H\}\}
    -\{G_\mu\{F_\lambda H\}\}
       =\{\{F_\lambda G\}_{\lambda+\mu}H\}.}
 \tag{DP.13}
\]
This establishes the classical affine PVA directly. Its unit has zero bracket. Every calculation is polynomial over \(k\), so the construction and its identities hold under every ordinary coefficient map \(R\to R'\), including nilpotent coefficients.

**The principal constraints are coisotropic.** Put
\[
 \begin{aligned}
 f&=\sum_{i=1}^{n-1}E_{i+1,i},&
 \mathfrak n_+&=\{x:x\text{ is strictly upper triangular}\},\\
 \chi(x)&=\operatorname{tr}(fx),&c_x&=J_x-\chi(x).
 \end{aligned}
 \tag{DP.14}
\]
For \(n=1\), \(\mathfrak n_+=0\) and all subsequent reductions are the identity reduction. In general define the differential ideal
\[
 I_R=(T^rc_x:x\in\mathfrak n_+,\ r\geq0)
           \ \subset\ \mathcal A_R.
 \tag{DP.15}
\]
The trace of a product of two strictly upper triangular matrices is zero. Moreover
\(\chi(v)=\sum_i v_{i,i+1}\), and every first-superdiagonal entry of a commutator in \(\mathfrak n_+\) is zero: the matrix-product sum would require an integer strictly between \(i\) and \(i+1\). Consequently
\[
 B(\mathfrak n_+,\mathfrak n_+)=0,\qquad
 \chi([\mathfrak n_+,\mathfrak n_+])=0,\qquad
 \{c_x{}_\lambda c_y\}=c_{[x,y]}\in I_R[\lambda].
 \tag{DP.16}
\]
For example, in rank two \(\{c_{E_{12}}{}_\lambda J_{E_{21}}\}=J_{E_{11}-E_{22}}+\lambda\), whose reduction is a nonzero polynomial. Thus the unrestricted constraint quotient does not inherit the affine bracket.

Sesquilinearity proves the same containment for derivatives of the constraints. Applying both Leibniz rules to their multiples proves
\(\{I_R{}_\lambda I_R\}\subset I_R[\lambda]\).
This is coisotropy. It does not say that \(I_R\) is a PVA ideal in the whole affine algebra.

Define the normalizer
\[
 U_R=\{a\in\mathcal A_R:
          \{J_x{}_\lambda a\}\in I_R[\lambda]
                       \text{ for every }x\in\mathfrak n_+\}.
 \tag{DP.17}
\]
Since constants have zero bracket, \(J_x\) can be replaced here by \(c_x\). Coisotropy, sesquilinearity and the right Leibniz rule show \(I_R\subset U_R\). The normalizer is closed under products and \(T\), by (DP.5)–(DP.6).

We first prove the stronger ideal test needed for bracket closure. If \(a\in U_R\), skew symmetry gives
\(\{a_\lambda c_x\}\in I_R[\lambda]\); the shifted coefficients remain in \(I_R\) because it is differential. Right sesquilinearity handles \(T^rc_x\), and right Leibniz handles any multiple of that generator by an arbitrary polynomial. Skew symmetry gives the reverse containment as well. Therefore
\[
 a\in U_R\ \Longrightarrow
   \{a_\lambda I_R\}\subset I_R[\lambda],\qquad
   \{I_R{}_\lambda a\}\subset I_R[\lambda].
 \tag{DP.18}
\]
Conversely either ideal test implies (DP.17), since every \(c_x\) belongs to \(I_R\).

If \(a,b\in U_R\), Jacobi gives
\[
 \{J_x{}_\mu\{a_\lambda b\}\}
   =\{\{J_x{}_\mu a\}_{\mu+\lambda}b\}
       +\{a_\lambda\{J_x{}_\mu b\}\}
       \in I_R[\lambda,\mu].
 \tag{DP.19}
\]
The two containments use (DP.18), coefficient by coefficient, including the parameter substitution. Thus every coefficient of \(\{a_\lambda b\}\) lies in \(U_R\). We have proved that \(U_R\) is a differential PVA subalgebra and \(I_R\) is a differential PVA ideal in \(U_R\). In particular
\[
 \boxed{\mathcal W_R=U_R/I_R}
 \tag{DP.20}
\]
is a PVA. Products, \(T\) and all bracket coefficients descend independently of representatives: changing a representative by \(I_R\) changes the bracket by \(I_R[\lambda]\), by (DP.18).

**The quotient action and its invariant algebra.** Let \(\mathcal Q_R=\mathcal A_R/I_R\), with its differential-algebra structure, and write \(\pi:\mathcal A_R\to\mathcal Q_R\). There is a well-defined current action
\[
 \rho_x(\lambda)\pi(a)=\pi\{J_x{}_\lambda a\}
       =\sum_{j\geq0}\frac{\lambda^j}{j!}D_{x,j}\pi(a),
           \qquad x\in\mathfrak n_+.
 \tag{DP.21}
\]
It is independent of the lift \(a\), because the constraints preserve \(I_R\), as already proved. Each \(D_{x,j}\) is an \(R\)-linear derivation by right Leibniz. Jacobi, together with \(B|_{\mathfrak n_+}=0\), gives
\[
 [D_{x,p},D_{y,q}]=D_{[x,y],p+q}.
 \tag{DP.22}
\]
Indeed the polynomial identity for the two actions has right side
\(\rho_{[x,y]}(\lambda+\mu)\). Taking the coefficient of
\(\lambda^p/p!\,\mu^q/q!\) gives (DP.22). Thus \(x t^j\mapsto D_{x,j}\) is the polynomial current Lie action. Its exact formula on all jet generators is
\[
 \boxed{D_{x,j}\pi(J_y^{(r)})
   =\begin{cases}
       \displaystyle\frac{r!}{(r-j)!}\pi(J_{[x,y]}^{(r-j)}),&0\leq j\leq r,\\
       (r+1)!B(x,y),&j=r+1,\\
       0,&j>r+1.
     \end{cases}}
 \tag{DP.23}
\]
This is the coefficient extraction from
\((\lambda+T)^r(J_{[x,y]}+B(x,y)\lambda)\). It is an identity over \(R\), not a formula checked only at field-valued points.

Define \(\mathcal Q_R^{\mathfrak n_+[[t]]}\) as the common kernel of all \(D_{x,j}\). An invariant quotient class has any lift \(a\) satisfying (DP.17), because its polynomial coefficients in (DP.21) are zero; conversely a normalizer representative maps to an invariant. The kernel of this map is exactly \(I_R\), already contained in \(U_R\). Therefore there is a canonical differential-algebra identification
\[
 \boxed{\mathcal W_R
      \simeq\mathcal Q_R^{\mathfrak n_+[[t]]}.}
 \tag{DP.24}
\]
No special invariant lift has been chosen. The PVA bracket on the right means the normalizer bracket transported through this identification. The whole \(\mathcal Q_R\) has not been declared an affine-PVA quotient.

**Matrix geometry and the gauge sign.** The trace pairing identifies a current with a matrix:
\[
 J_y=\operatorname{tr}(Ay),\qquad A_{ji}=J_{E_{ij}}.
 \tag{DP.25}
\]
For \(\mathfrak{sl}_n\), take \(A\) traceless; off-diagonal entries use the same formula, and \(A_{ii}=J_{E_{ii}-\mathbf1/n}\). The full trace-dual basis is \(E_{ij}^{\vee}=E_{ji}\), since
\(\operatorname{tr}(E_{ij}E_{ab})=\delta_{ja}\delta_{ib}\).
The restricted trace form is nondegenerate as well: orthogonality to off-diagonal matrices makes a matrix diagonal, and orthogonality to all \(E_{ii}-E_{jj}\) makes it scalar; its zero trace then makes it zero because \(n\) is invertible. This proves the required pairing statements over \(k\) and their ordinary extensions.
No diagonal generator outside \(\mathfrak{sl}_n\) is introduced. The constraints fix
\(A_{i+1,i}=1\) and every other strictly lower entry to zero. Hence
\[
 \mathcal Q_R
  =\mathcal O_{\mathrm{diff}}(f+\mathfrak b_+)_R,
 \tag{DP.26}
\]
where \(\mathfrak b_+\) is the upper triangular algebra, traceless in the \(\mathfrak{sl}_n\) case. Concretely this is a polynomial algebra on its remaining upper-triangular entries and all their derivatives: eliminate the constraint coordinates at order zero, and all their positive jets. This description is valid over nonreduced \(R\). Its formal-disc matrix is
\(A(t)=\sum_{r\geq0}A^{(r)}t^r/r!\).
An ordinary coefficient point of the differential polynomial algebra specifies precisely all these jets; finite Taylor formulas are valid because every factorial is a unit.

For a local functional \(\int F\), modulo \(T\)-derivatives, set
\(\delta_{\int F}a=\{F_\lambda a\}|_{\lambda=0}\).
First sesquilinearity makes this independent of the representative of \(F\); right Leibniz makes it a derivation, and second sesquilinearity makes it commute with \(T\). To accommodate a variable matrix test function, adjoin Poisson-central test coefficients with their derivatives. This is an algebraic test extension; it presumes no translation operator on a target module. Use the same bracket-coefficient derivations before reduction to compute the flow; for \(x\in\mathfrak n_+\) they descend to (DP.21). Formula (DP.7) then gives, for an external scalar \(\phi\),
\[
 \delta_{\int\phi J_x}a
       =\sum_{j\geq0}\frac{\phi^{(j)}}{j!}D_{x,j}a.
 \tag{DP.27}
\]
The sum is finite for each differential polynomial \(a\). Applying it to \(J_y\), and adding the entries of \(x(t)\), gives
\[
 \delta_xJ_y
   =J_{[x,y]}+\operatorname{tr}(x'y)
   =\operatorname{tr}\bigl(([A,x]+x')y\bigr).
\]
Nondegeneracy of the trace pairing on matrices, or its traceless restriction, proves
\[
 \boxed{\delta_xA=[A,x]+x'.}
 \tag{DP.28}
\]
This is precisely the derivative of
\[
 A\longmapsto A^g=g^{-1}Ag+g^{-1}g',
       \qquad g\in N_+(R[[t]]).
 \tag{DP.29}
\]
Indeed \(g=1+\eta x\), \(\eta^2=0\), gives (DP.28). It is the inverse gauge action on the connection \(\partial+A\): \(g^{-1}(\partial+A)g=\partial+A^g\). The forward conjugation convention would have the opposite infinitesimal sign. The inverse action is a right action on matrices and gives the positive Lie action on functions in (DP.22).

It preserves \(f+\mathfrak b_+\). Infinitesimally,
\([f,\mathfrak n_+]\subset\mathfrak b_+\),
\([\mathfrak b_+,\mathfrak n_+]\subset\mathfrak n_+\), and \(x'\in\mathfrak n_+\).
The first inclusion is checked on \(E_{ij}\), \(i<j\):
\([f,E_{ij}]=E_{i+1,j}-E_{i,j-1}\), with missing boundary terms omitted; both entries are upper triangular, including diagonal entries when \(j=i+1\). Finite preservation follows from the exponential argument below. Trace is also preserved, since the trace of \(g^{-1}g'\) is zero for upper unipotent \(g\). In rank two, with \(A=\left(\begin{smallmatrix}a&b\\1&d\end{smallmatrix}\right)\) and \(x=uE_{12}\), the sign check is
\[
 \delta a=-u,\qquad \delta d=u,\qquad
 \delta b=(a-d)u+u'.
 \tag{DP.30}
\]

**All formal upper-unipotent families and ordinary base change.** Give \(A_{ij}^{(r)}\), \(i\leq j\), weight \(j-i+1+r\). All generator weights in \(\mathcal Q_R\) are positive; its weight-\(d\) piece is the ordinary extension of a finite-dimensional \(k\)-space. For \(x=E_{ab}\in\mathfrak n_+\), of height \(h=b-a\), (DP.23) lowers that weight by \(h+j\):
\[
 D_{x,j}:(\mathcal Q_R)_d
       \longrightarrow(\mathcal Q_R)_{d-h-j}.
 \tag{DP.31}
\]
One way to verify this is to assign \(J_y\) weight \(1-\operatorname{height}(y)\) before reduction and give \(\lambda,T\) weight one. Then (DP.2) has weight equal to the sum of its inputs minus one. The only nonzero character values occur at height one and weight zero, so all constraint specializations respect this weighting. Formula (DP.23) gives exactly (DP.31) on the remaining coordinates.

Thus every polynomial is killed by sufficiently high current jets, and each \(D_{x,j}\) is locally nilpotent. A formal \(x(t)\in\mathfrak n_+\otimes R[[t]]\) acts on a bounded-weight polynomial by a finite sum of these derivations and lowers weight at least one. Its exponential is finite on that polynomial.
Explicitly, for \(x(t)=\sum_{j\geq0}x_jt^j\), define \(D_x=\sum_jD_{x_j,j}\).
Formula (DP.23), summed against \(t^r/r!\), gives
\[
 D_xA(t)=[A(t),x(t)]+x'(t).
\]
The first sum has coefficient
\(\sum_{j\leq r}r!/(r-j)!\,[A^{(r-j)},x_j]\);
the central term is \((r+1)!x_{r+1}\).
Thus the same action is detected on every Taylor coefficient, not merely on the matrix value at the origin.

Every upper unipotent matrix \(g(t)\) is an exponential \(g=\exp x\): put
\[
 x=\log(1+(g-1))
   =\sum_{v=1}^{n-1}\frac{(-1)^{v+1}}v(g-1)^v.
\]
The finite exponential and logarithm are inverse because the corresponding power-series identities hold modulo the \(n\)-th power of one variable, and \(g-1\) is nilpotent of order at most \(n\). Those identities follow, for example, by differentiating the scalar series and comparing their constant terms; only the positive integers are divided.

The pullback of (DP.29) for \(g_s=\exp(sx(t))\) agrees with \(\exp(sD_x)\). In fact differentiating the displayed matrix formula with respect to \(s\) gives
\[
 \frac{d}{ds}A^{g_s}=[A^{g_s},x]+x'.
 \tag{DP.32}
\]
The same equation holds for \(\exp(sD_x)A\), by (DP.28). Both have value \(A\) at \(s=0\); coefficient recursion divides only by \(1,2,\ldots\), so their polynomial solutions agree, including all jets. This also proves finite preservation of the constrained matrix space.

Consequently a class killed by all current jets is fixed by every \(N_+\) gauge family over every ordinary coefficient extension. Conversely, invariance as an action of this group functor implies current-jet invariance by testing
\(g=1+\eta x t^j\) over \(R[\eta]/(\eta^2)\). This detects the exact derivation, including nilpotent coefficients. Therefore
\[
 \boxed{\mathcal W_R
   \simeq\mathcal Q_R^{N_+[[t]]}}
 \tag{DP.33}
\]
with invariants understood as equality for the group action functor, rather than just equality at reduced points.

The reduction mechanism is the following square of coordinate algebras:
\[
 \begin{array}{ccc}
 U_R&\lhook\joinrel\longrightarrow&\mathcal A_R\\
 \downarrow&&\downarrow\\
 \mathcal W_R&\lhook\joinrel\longrightarrow&\mathcal Q_R
       =\mathcal O_{\mathrm{diff}}(f+\mathfrak b_+)_R .
 \end{array}
\]
*The left quotient carries the reduced PVA bracket by (DP.18)–(DP.20).
Its lower image is exactly the common current-jet kernel (DP.24), equivalently the inverse-gauge invariant algebra (DP.33).
The right quotient imposes the principal matrix entries (DP.26) as differential-algebra relations.
The matrix flow (DP.28) explains which action is detected; it fixes the cocycle and gauge signs.*

This construction commutes with all ordinary extensions \(k\to R\to R'\) obtained from the fixed \(k\)-model. Indeed in each weight \(d\), only finitely many \(D_{x,j}\) can act nontrivially, by (DP.31). Their common kernel is the kernel of one finite matrix over \(k\). Tensoring over the field preserves it. Summing the weight spaces gives
\[
 U_R/I_R=\mathcal W_R\simeq R\otimes_k\mathcal W_k.
 \tag{DP.34}
\]
The bracket and derivation agree with this identification because all their polynomial formulas were defined over \(k\). The invariant algebra is \(T\)-stable even though a fixed nonconstant gauge need not commute with \(T\): (DP.5) gives
\(D_{x,j}T=TD_{x,j}+jD_{x,j-1}\), with the final term zero for \(j=0\).
Thus all those actions kill \(Ta\) when they kill \(a\). No assertion that an arbitrary invariant kernel commutes with every nonflat base change has been used; the finite matrices here come from the fixed field model.

The construction above uses regular jets and the action of \(N_+[[t]]\). Its grading is the principal weight \(D(J_x)=1-\operatorname{height}(x)\), with \(D(T)=1\); the character relations are homogeneous in this grading. The full Laurent Hamiltonian reduction requires all integer moment-mode relations and a completed coisotropic normalizer. Its topology and pole bounds require the separate Laurent construction.

**Exactly when a Poisson arrow descends.** Let \(\Phi:\mathcal A\to\mathcal B\) be an actual homomorphism of ordinary PVAs: it preserves the unit, products, \(T\), and every coefficient of the \(\lambda\)-bracket. Let \(I\subset\mathcal A\), \(J\subset\mathcal B\) be coisotropic differential ideals of the preceding kind, with normalizers \(U_I,U_J\). If
\[
 \Phi(I)\subset J,\qquad \Phi(U_I)\subset U_J,
 \tag{DP.35}
\]
then \([a]\mapsto[\Phi(a)]\) is a well-defined PVA homomorphism
\(U_I/I\to U_J/J\). The first containment proves lift independence; the second gives the correct target. Preservation of the bracket follows by applying \(\Phi\) to its actual polynomial coefficients and then reducing. This is the commutative square
\[
 \begin{array}{ccc}
 U_I&\xrightarrow{\ \Phi\ }&U_J\\
 \downarrow&&\downarrow\\
 U_I/I&\xrightarrow{\ \overline\Phi\ }&U_J/J .
 \end{array}
 \tag{DP.36}
\]
*The vertical arrows are PVA quotients because (DP.18) was proved. The unrestricted quotients \(\mathcal A/I\) and \(\mathcal B/J\) enter as differential algebras with constraint actions; their full brackets are not presumed to descend.*

A useful sufficient condition for the second containment is
\[
 J=\text{the differential ideal in }\mathcal B
                         \text{ generated by }\Phi(I).
 \tag{DP.37}
\]
For \(a\in U_I\), its bracket with each \(\Phi(i)\), \(i\in I\), lies in \(J[\lambda]\), by (DP.18) and the homomorphism identity. Sesquilinearity handles derivatives; left Leibniz handles multiplication of a generator by arbitrary elements of \(\mathcal B\), since the additional coefficient is multiplied by the generator or its derivatives in \(J\). Thus \(\{J_\lambda\Phi(a)\}\subset J[\lambda]\), which is precisely the target normalizer test. Equality of constraint ideals, or an explicit normalizer test, is needed; mere containment \(\Phi(I)\subset J\) supplies only a differential-algebra map of the unrestricted quotients.

Finally, the reduced arrow is injective if \(\Phi^{-1}(J)\cap U_I=I\). It is surjective exactly when every class of \(U_J/J\) has a representative in \(\Phi(U_I)\). Both assertions follow directly by taking the kernel and image of (DP.36), and require their stated hypotheses. An ordinary algebra map with matching highest symbols cannot replace the actual PVA homomorphism or these normalizer comparisons.

The result established here is the ordinary classical affine PVA and its principal coisotropic Hamiltonian reduction, with the complete jet action and inverse-gauge convention. Polynomiality of its gauge slice and a specific affine-to-free-field or oper comparison require their own constructions. The finite jet-distribution proof above does not assert a universal operator-field reconstruction or Poisson closure of an uncompleted algebra of arbitrary Laurent Fourier coefficients; such completion questions retain the topology and cutoff arguments of §3.7.5.

#### 3.8.2. Principal matrix gauge and polynomial jet invariants

The covector construction and companion signs were already proved in [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), §2.5, equations (O4.2)–(O4.7). We retain them and prove the additional ordinary differential-ring quotient, exact polynomial jet invariants and cofinal Laurent geometry. The argument needs no intrinsic bundle-gluing theorem beyond the earlier oper interpretation when that interpretation is applied.

Let \(k\) have characteristic zero, let \((B,\partial)\) be any ordinary commutative differential \(k\)-algebra, and let \(n\ge2\) in the trace-zero case. Nilpotents in \(B\) are allowed. The raw matrix case also permits \(n=1\). Put
\[
 \begin{aligned}
 f&=\sum_{i=1}^{n-1}E_{i+1,i},&\mathcal X(B)&=f+\mathfrak b_+(B),\\
 N(B)&=\{\text{upper unitriangular }n\times n\text{ matrices over }B\}.
 \end{aligned}
\tag{MG.1}
\]
For \(\mathfrak{sl}_n\), impose \(\operatorname{tr}A=0\) on \(\mathcal X\); for \(\mathfrak{gl}_n\), retain the trace. The action is
\(g\cdot A=gAg^{-1}-g'g^{-1}\), so it is the left gauge action on \(\partial+A\), exactly (DS.A11). All inverses in \(N\) are finite polynomials: if \(g=1+U\), then \(g^{-1}=\sum_{j=0}^{n-1}(-U)^j\). The action preserves \(\mathcal X\). Indeed \((gf)_{ij}=g_{i,j+1}\) is zero for \(j<i-1\), and right multiplication by an upper unitriangular inverse retains those zero entries and the subdiagonal entries one. Both \(gbg^{-1}\) and \(g'g^{-1}\) are upper triangular, the latter strictly upper triangular. Trace is consequently preserved too.

**The complete matrix construction, with the earlier signs.** On row covectors define
\[
 D_Aq=q'-qA,\qquad
 q_n=e_n^t,\qquad
 q_i=(-1)^{n-i}D_A^{n-i}e_n^t,
 \qquad q_{i-1}=-D_Aq_i.
\tag{MG.2}
\]
Each \(q_i\) has zero entries in columns below \(i\), and entry one in column \(i\). The claim starts with \(q_n\). If it holds for \(q_i\), then in a column \(j<i-1\) every summand \((q_i)_rA_{rj}\) is zero, since \(r\ge i\) and \(A_{rj}=0\) for \(j<r-1\). In column \(i-1\), only \(r=i\) contributes and gives one. The derivative of that column of \(q_i\) is zero. Thus \(-D_Aq_i\) has the asserted leading entry and support. This proves the induction, over \(B\) itself rather than over its reduced points.

Let \(Q(A)\) have rows \(q_i\). It is upper unitriangular, with polynomial entries in the entries of \(A\) and their derivatives. In particular
\[
 \begin{aligned}
 Q(A)^{-1}&=\sum_{j=0}^{n-1}(1-Q(A))^j,\\
 C(A)&=Q(A)AQ(A)^{-1}-Q(A)'Q(A)^{-1}\\
     &=-(D_AQ(A))Q(A)^{-1}.
 \end{aligned}
\tag{MG.3}
\]
For \(i\ge2\), (MG.2) makes row \(i\) of \(C(A)\) equal to \(e_{i-1}^t\). Its only remaining entries are in its first row. Since \(Q'Q^{-1}\) is strictly upper triangular,
\[
 C(A)=
 \begin{pmatrix}
 a_{11}&a_{12}&\cdots&a_{1n}\\
 1&0&\cdots&0\\
 0&1&\cdots&0\\
 \vdots&&\ddots&\vdots
 \end{pmatrix},
 \qquad a_{11}=\operatorname{tr}A.
\tag{MG.4}
\]
The displayed lower rows are precisely the subdiagonal ones and zeros; hence the last row has its one in column \(n-1\). This description, unlike the abbreviated display, specifies every matrix entry. In the trace-zero case \(a_{11}=0\).

Set \(s_j=(-1)^{j-1}a_{1j}\). The resulting scalar operator is
\[
 L=\partial^n+\sum_{j=1}^ns_j\partial^{n-j},
 \qquad a_{1j}=(-1)^{j-1}s_j,\qquad s_1=0\text{ for }\mathfrak{sl}_n.
\tag{MG.5}
\]
For example, the lower horizontal equations give
\(v_j=(-1)^{n-j}\partial^{n-j}y\), with \(y=v_n\). Substitution in the first horizontal equation gives exactly \(Ly=0\). This is an algebraic calculation, not an assumption that analytic solutions exist. More intrinsically, the row basis (MG.2) gives the relation
\(D_A^ne_n^t+\sum_js_jD_A^{n-j}e_n^t=0\); it is the same scalar relation in the cyclic differential module.

**Equivariance, uniqueness and a polynomial inverse.** If \(A^g=g\cdot A\), the product rule gives the exact identity
\[
 D_{A^g}(qg^{-1})=(D_Aq)g^{-1}.
 \qquad
 Q(A^g)=Q(A)g^{-1},\qquad C(A^g)=C(A).
\tag{MG.6}
\]
For the second identity use \(e_n^tg^{-1}=e_n^t\) and iterate the first. The third follows from the composition law of left gauge. A companion matrix \(C(s)\) has \(D_Ce_i^t=-e_{i-1}^t\) for \(i\ge2\), so
\[
 Q(C(s))=1.
\tag{MG.7}
\]
If \(g\cdot A=C(s)\), equations (MG.6)–(MG.7) force \(g=Q(A)\) and \(C(s)=C(A)\). Thus the normalizing gauge is unique, and every stabilizer is trivial. This proof holds over any \(B\), including its nilpotents.

Write \(\mathcal S(B)=B^{n-1}\) in the trace-zero case, with coordinates \(s_2,\ldots,s_n\), or \(B^n\) in the raw case. We have mutually inverse polynomial differential operations
\[
\begin{aligned}
 \Phi:N(B)\times\mathcal S(B)&\longrightarrow\mathcal X(B),
             &(u,s)&\longmapsto u\cdot C(s),\\
 \Phi^{-1}:\mathcal X(B)&\longrightarrow N(B)\times\mathcal S(B),
             &A&\longmapsto(Q(A)^{-1},s(A)).
\end{aligned}
\tag{MG.8}
\]
There is no division by a matrix-entry function. Inverses of unipotent matrices are finite polynomials, and all the differentiations in (MG.2)–(MG.3) are finite. Under a gauge \(g\), the coordinates of (MG.8) change by
\((u,s)\mapsto(gu,s)\). This is the explicit product quotient, with no dominance or orbit-separation theorem imported.

For later bounds, assign \(\partial\) weight one, an upper entry \(A_{ab}\) weight \(b-a+1\), and the fixed subdiagonal entries weight zero. Induction in (MG.2) shows that \(Q_{ij}\) and \((Q^{-1})_{ij}\) have weight \(j-i\). In a product \(Q_{ir}A_{rs}(Q^{-1})_{sj}\) the three weights add to \(j-i+1\); the derivative term has that weight too. Therefore
\[
 \operatorname{wt}s_j=j,\qquad
 \operatorname{wt}u_{ab}=b-a,
 \qquad\operatorname{wt}(u\cdot C(s))_{ab}=b-a+1.
\tag{MG.9}
\]
The inverse entries have the claimed weights because each strictly increasing index path has total weight \(j-i\). These are actual homogeneous differential polynomial identities, not only highest terms.

**The ordinary polynomial invariant algebra.** Fix an ordinary coefficient algebra \(R\), with the derivation zero on \(R\). Let
\(\mathscr X_R\) be the differential polynomial algebra freely generated by the upper entries of \(A\), with the trace and all its derivatives eliminated in the trace-zero case. Let \(\mathscr N_R\) be the free differential polynomial algebra on upper entries of a unipotent \(u\). Let
\(\mathscr S_R=R[s_j^{(r)}]\), \(r\ge0\), with \(2\le j\le n\) or \(1\le j\le n\) as appropriate. Applying (MG.8) to the universal differential rings proves the isomorphism
\[
 \mathscr X_R\simeq\mathscr N_R\otimes_R\mathscr S_R.
\tag{MG.10}
\]
Both directions are given by the explicit polynomial formulas, so this also proves independence of every \(s_j^{(r)}\). Arbitrary ordinary coefficient extension preserves the formulas and their inverse identities. No invariant-kernel base change is being guessed from reduced fibers.

Invariance means a universal polynomial coaction identity, or equivalently equality after every ordinary coefficient extension and every gauge therein. If \(F\) is invariant, apply (MG.8) and specialize the universal gauge to \(u^{-1}\). This gives
\(F(u\cdot C(s))=F(C(s))\). The right side is a polynomial in only \(s_j\) and their derivatives. Conversely those polynomials are invariant by (MG.6). Consequently
\[
 \boxed{\mathscr X_R^{N\text{ differential gauge}}=\mathscr S_R.}
\tag{MG.11}
\]
Specialization to the universal inverse is legitimate in the free polynomial differential ring: the inverse entries and their derivatives are polynomial there. This proves a ring identity rather than just a bijection on field-valued orbits.

**Why polynomial-current invariance is exactly jet-gauge invariance.** Identify differential jets with Taylor coefficients by
\(A^{(r)}(0)=r!A_r\) in \(A(t)=f+\sum_{r\ge0}b_rt^r\). A current \(x(t)\in\mathfrak n_+[t]\) gives the infinitesimal variation
\[
 \delta_xA=[A,x]+x'.
\tag{MG.12}
\]
It is the derivative of \((1-cx)\cdot A\) at \(c=0\), so its sign is fixed by the gauge convention. It preserves the normalized lower entries and trace, since the actual gauge action does. On Taylor coefficient rings it defines an ordinary derivation.

For a single matrix root let \(E=E_{ab}\), \(a<b\), and let \(\varphi(t)\) be a scalar series. Since \(E^2=0\), its full one-parameter transformation is exactly
\[
 (1-c\varphi E)\cdot A
 =A+c\bigl([A,\varphi E]+\varphi'E\bigr)
       -c^2\varphi^2EAE.
\tag{MG.13}
\]
The infinitesimal derivation has
\(\delta_{\varphi E}^2A=-2\varphi^2EAE\) and
\(\delta_{\varphi E}^3A=0\): differentiating the first variation treats \(\varphi\) as fixed, \([\varphi'E,\varphi E]=0\), and the next commutator is zero because \(E^2=0\). The same assertion holds on every jet coefficient. Thus this derivation is locally nilpotent on each finite polynomial, and the product rule proves that (MG.13) induces exactly
\[
 \exp(c\delta_{\varphi E})F
 =\sum_{r\ge0}\frac{c^r}{r!}\delta_{\varphi E}^rF.
\tag{MG.14}
\]
This is finite for every \(F\). It follows that its infinitesimal kernel equals its universal one-parameter invariant ring: one direction uses the finite exponential; the other extracts the coefficient of \(c\) over \(R[c]\). Characteristic zero, rather than a reduced-point argument, makes these factorials units.

If \(F\) uses only Taylor coefficients through order \(M\), currents \(t^rE\) with \(r>M+1\) act trivially on it. The commutator term starts in order \(r\), and the derivative term in order \(r-1\). Hence invariance under every polynomial mode implies invariance under \(\varphi(t)E\) for every \(\varphi\in R[[t]]\): on \(F\) its infinitesimal action is the finite linear sum of the modes through \(M+1\). Formula (MG.14) then supplies the actual formal-root action.

Every upper unitriangular series matrix is a finite product of those root matrices, over \(R[[t]]\) itself. For a direct proof, eliminate upper entries by increasing height \(b-a\). Left multiplication by \(1-u_{ab}E_{ab}\) kills entry \((a,b)\); its only other changes are in row \(a\), in columns \(j>b\), hence at strictly higher height. Previously killed entries are retained. After the finitely many heights the matrix is the identity. The parameters and the reverse factorization are polynomial in the original entries. Combining this with (MG.11)–(MG.14) proves
\[
 \boxed{\mathscr X_R^{\mathfrak n_+[t]}
       =\mathscr X_R^{N(R[[t]])\text{ universal jet gauge}}
       =R[s_j^{(r)}].}
\tag{MG.15}
\]
Here the middle notation denotes the coaction invariant ring, including after every ordinary coefficient extension. Thus it does not omit nilpotent gauge parameters.

There is a finite-jet statement behind this infinite notation. From (MG.2), row \(q_i\) uses derivatives of \(A\) only through order \(n-i-1\) when \(i<n\). Thus the normalizing matrix through Taylor order \(M\) needs \(A\) only through order \(M+n-2\), and its scalar coefficients through order \(M\) need \(A\) only through \(M+n-1\). Conversely \(u\cdot C(s)\) through order \(M\) needs \(u\) through \(M+1\) and \(s\) through \(M\). These polynomial maps are inverse on the full jet algebras and have those uniform cofinal truncation bounds:
\[
 \begin{array}{c|c}
 \text{required output through order }M&\text{sufficient input order}\\\hline
 Q(A),\ Q(A)^{-1}&M+n-2\\
 s(A)&M+n-1\\
 u\cdot C(s)&u:\ M+1,\quad s:\ M.
 \end{array}
\tag{MG.16}
\]
For \(n=1\), the normalizing matrix is constant and the scalar map is the identity. In general (MG.16) does **not** assert an isomorphism of equally truncated order-\(M\) jet spaces; derivative gauge terms require the higher input jets displayed. Each finite polynomial invariant is obtained by the universal gauge identity at a finite sufficient truncation, and is the scalar polynomial obtained by restricting to \(C(s)\). This proves the finite/cofinal content without a hidden infinite existence step.

**The underlying current normalizer.** We can now match the ordinary invariant algebra to the algebra underlying the affine Hamiltonian reduction, keeping its Poisson construction separate. Use the trace pairing \(B(x,y)=\operatorname{tr}(xy)\), restricted to \(\mathfrak{sl}_n\) when appropriate. Write \(J_y=B(y,A)\) for its linear coordinate and use the affine current relation
\[
 \{J_x{}_{\lambda}J_y\}=J_{[x,y]}+B(x,y)\lambda.
\tag{MG.17}
\]
The trace pairing is nondegenerate on matrices by the matrix-unit dual pairs, and on traceless matrices because their orthogonal complement is the scalar line, whose intersection with the traceless subspace is zero when \(n\) is a unit. This remains a perfect pairing after ordinary coefficient extension. The affine Poisson vertex construction and reduced Poisson comparison are distinct arguments. What we need here is its explicit current action: the Hamiltonian \(\int\varphi J_x\) changes \(J_y\) by
\(\varphi J_{[x,y]}+\varphi'B(x,y)\). Invariance of trace rewrites this as
\(B(y,[A,\varphi x]+\varphi'x)\). Since the pairing is nondegenerate, it is exactly (MG.12), with the positive derivative and the same matrix gauge sign.

Let \(\mathscr V_R\) be the ordinary differential polynomial algebra on all \(J_y\), and let \(I\) be the differential ideal generated by
\(J_x-\chi(x)\), \(x\in\mathfrak n_+\), with
\(\chi(x)=\operatorname{tr}(fx)\). These equations set every strictly lower matrix entry to its value in \(f\), so
\[
 \mathscr V_R/I=\mathscr X_R.
 \qquad
 \chi(E_{ab})=\begin{cases}1&b=a+1,\\0&b>a+1.\end{cases}
\tag{MG.18}
\]
For two positive roots the trace pairing is zero, and their bracket has height at least two, so \(\chi([x,y])=0\). Thus the brackets of the constraint generators lie in \(I[\lambda]\). The derivation (MG.12) preserves the slice ideal as already proved by actual gauges. These observations fix the constraint and normalizer conventions; they do not infer a scalar Poisson formula from the gauge classification.

Write \(\{J_x{}_{\lambda}F\}\bmod I=\sum_r c_r\lambda^r\). The first-slot Leibniz rule with an external scalar test series gives the evolutionary variation \(\sum_r c_r\varphi^{(r)}\). At the origin, taking \(\varphi=t^p\) gives precisely
\[
 \delta_{t^px}F=p!c_p
 \quad\text{under the identification }J_y^{(r)}\leftrightarrow r!B(y,A_r).
\tag{MG.19}
\]
One may check this on a linear jet without any general identity: expanding
\((\lambda+\partial)^r(J_{[x,y]}+B(x,y)\lambda)\), its \(\lambda^p\) coefficient times \(p!\) is the derivative-at-zero of
\(\varphi[A,x]+\varphi'x\). The product rule then proves (MG.19) for every differential polynomial. Only finitely many \(p\) occur for a fixed \(F\).

Consequently the current-normalizer condition is exactly the invariant condition in (MG.15):
\[
 \mathcal N(I)=\{F\in\mathscr V_R:
     \{J_x{}_{\lambda}F\}\in I[\lambda]\ \text{for all }x\in\mathfrak n_+\},
 \qquad
 \boxed{\mathcal N(I)/I\simeq R[s_j^{(r)}].}
\tag{MG.20}
\]
The generator condition defines a differential subalgebra: sesquilinearity and the second-slot Leibniz rule preserve \(I[\lambda]\). It contains \(I\), by the constraint calculation after (MG.18) and the two Leibniz rules. Every invariant class has a polynomial lift, and (MG.19) makes any such lift satisfy the stated normalizer condition. Conversely every normalizer class is invariant. This proves both directions of the algebra identification. Its Poisson vertex reduction and the full Adler comparison require the separate current-reduction and free-field arguments; they are not consequences of (MG.8) or of orbit uniqueness.

**Cofinal Laurent gauge geometry.** The same finite formulas work over \(B=R((t))\), with its derivative, and over \(R[[t]]\). In the Laurent case the gauge group is \(N(R((t)))\); it cannot be silently replaced by \(N(R[[t]])\). For example, in rank two a pole in the second diagonal entry requires the same pole in \(Q_{12}\), whereas a regular upper gauge changes that diagonal entry only by a regular series.

There are exact cofinal pole-bounded products, with bounds determined by (MG.9). For \(N\ge1\), define
\[
\begin{aligned}
 \mathcal X_N(R)&=\{A\in\mathcal X(R((t))):
               A_{ab}\in t^{-(b-a+1)N}R[[t]]\ (a\le b)\},\\
 \mathcal G_N(R)&=\{u\in N(R((t))):
               u_{ab}\in t^{-(b-a)N}R[[t]]\ (a<b)\},\\
 \mathcal S_N(R)&=\{s:s_j\in t^{-jN}R[[t]]\}.
\end{aligned}
\tag{MG.21}
\]
Retain trace zero and omit \(s_1\) when required. These bounds are cofinal because there are finitely many entries and every relevant weight is positive. The group \(\mathcal G_N\) is closed under multiplication and inverse: upper-entry weights add along every matrix path. A derivative raises a pole order by at most one, which is at most \(N\). Thus every homogeneous differential polynomial of weight \(w\) evaluated in entries of pole order at most their weight times \(N\) has pole order at most \(wN\). Equations (MG.3), (MG.8), (MG.9) consequently give exact mutually inverse maps
\[
 \boxed{\mathcal X_N(R)\simeq
        \mathcal G_N(R)\times\mathcal S_N(R),
        \qquad A\leftrightarrow(Q(A)^{-1},s(A)).}
\tag{MG.22}
\]
They commute with the inclusions as \(N\) increases and with every ordinary coefficient extension. These are coefficientwise naturality and polynomial coefficient-ring base change; they do not assert that ordinary tensor product commutes with the formal-series construction. Hence the full Laurent quotient functor is exactly the scalar Laurent coefficient functor, and every object has trivial unipotent stabilizer.

At a fixed bound these are polynomial maps of coefficient functors, not merely formal substitutions. A monomial of weight \(w\) in inputs of weights \(w_\nu\) and total derivative order \(d\) has \(\sum w_\nu+d=w\). For its coefficient of \(t^r\), input indices \(m_\nu\) satisfy \(\sum m_\nu-d=r\) and \(m_\nu\ge-w_\nu N\). Therefore
\(m_\nu\le r+d+\sum_{\mu\ne\nu}w_\mu N\le r+(w-w_\nu)N\).
Only finitely many tuples survive. Every output matrix or scalar coordinate has weight at most \(n\), so an output through coefficient index \(M\) uses only input indices through \(M+(n-1)N\), besides their specified finite lower bounds. This proves the finite-jet/cofinal nature of (MG.22), including nilpotent coefficients.

The coefficient algebras at that bound therefore have the same exact invariant identification
\[
 R[\mathcal X_N]^{\mathcal G_N}
   =R[s_{j,r}:r\ge-jN],
 \qquad s_j(t)=\sum_{r\ge-jN}s_{j,r}t^r.
\tag{MG.23}
\]
Here each coordinate ring is an ordinary polynomial ring on the allowed coefficient list. The proof uses the universal inverse specialization from (MG.11) and the actual polynomial isomorphism (MG.22). The elementary-root elimination also stays within \(\mathcal G_N\), by its height bounds, so the finite one-parameter proof applies to its allowed Laurent root parameters. In this statement those parameters have lower bound \(-(b-a)N\) at root \(E_{ab}\); it is **not** a claim that positive polynomial currents alone have these Laurent invariants. The inverse limit of these scalar coefficient rings describes continuous functions on the cofinal Laurent coefficient functor. This does not identify all discontinuous characters of an abstract inverse-limit ring with that functor.

**The ordered diagonal comparison and the sign check.** On \(A=f+\operatorname{diag}(h_1,\ldots,h_n)\), eliminate the horizontal components from the bottom: \(v_{i-1}=-(\partial+h_i)v_i\). The first equation then gives, with exactly the order retained in §3.7,
\[
 L=(\partial+h_1)(\partial+h_2)\cdots(\partial+h_n).
\tag{MG.24}
\]
For a solution-free verification, recursively form \(q_{i-1}=q_iA-q_i'\) and its unique scalar relation (MG.5); the same elimination is an identity in the cyclic differential module, so the relation is precisely that product. Trace zero gives \(\sum h_i=0\), removing its subprincipal coefficient.

The rank-two calculation shows every sign in concrete matrices:
\[
 A=\begin{pmatrix}a&b\\1&c\end{pmatrix},\qquad
 Q=\begin{pmatrix}1&c\\0&1\end{pmatrix},\qquad
 Q\cdot A=\begin{pmatrix}a+c&b-ac-c'\\1&0\end{pmatrix}.
\]
Thus \(s_1=a+c\), \(s_2=ac+c'-b\), and a diagonal input gives
\((\partial+a)(\partial+c)\). When \(c=-a\), the normalized quadratic coefficient is \(-a'-a^2-b\), consistent with (AP.19) on \(b=0\).

| Exact operation | Gauge coordinate | Quotient coordinate |
|---|---|---|
| Build the covector rows (MG.2) | \(Q(A)\), upper unitriangular | \(s_j=(-1)^{j-1}C_{1j}\) |
| Apply \(g\in N\), (MG.6) | \(Q(A)\mapsto Q(A)g^{-1}\) | Every \(s_j\) is unchanged |
| Use the polynomial inverse (MG.8) | \(u=Q(A)^{-1}\) | \(A=u\cdot C(s)\) |
| Impose the ordinary current-normalizer condition, (MG.19)–(MG.20) | Remove the unipotent jet coordinate | Retain exactly \(R[s_j^{(r)}]\) |
| Use weighted Laurent bounds, (MG.21)–(MG.23) | Root-height pole bound \((b-a)N\) | Scalar pole bound \(jN\) |

*The table displays the actual polynomial maps and their exact invariants. The matrix mechanism is (O4.2)–(O4.7); the new ordinary-ring, jet and Laurent quotient proofs are (MG.8)–(MG.23). For the human-source Poisson context, see De Sole–Kac–Valeri, [Adler–Gelfand–Dickey approach to classical W-algebras within the theory of Poisson vertex algebras, free arXiv:1401.2082v1, §§2.8–2.9](https://arxiv.org/abs/1401.2082v1). No theorem from that source substitutes for the gauge or invariant proof here.*

This establishes the all-\(n\) ordinary principal matrix gauge quotient and its exact polynomial invariant algebra, with cofinal Laurent functors and the current-normalizer algebra comparison. Its application to intrinsic opers retains the earlier scalar-oper and frame foundations. The Poisson reduction, its identification with the Adler bracket and its actual free-field map remain distinct constructions. No chiral/factorization, Satake, derived-family or global localization comparison follows from this gauge uniqueness.

#### 3.8.3. Classical free fields and the principal Miura reduction

Let \(k\) have characteristic zero, and let \(R\) be any ordinary
commutative \(k\)-algebra. We use differential polynomial algebras over
\(R\), with \(T(R)=0\). Their identities can also be evaluated in any
ordinary differential \(k\)-algebra. For the matrix currents write
\(J_{ij}=J_{E_{ij}}\), and use the positive trace form:
\[
 \{J_x{}_\lambda J_y\}=J_{[x,y]}+\operatorname{tr}(xy)\lambda .
 \tag{WF.1}
\]
The matrix of coordinate functions is trace-dual:
\[
 A_{ji}=J_{ij},\qquad J_x=\operatorname{tr}(Ax).
 \tag{WF.2}
\]
This transpose is needed to put the principal moment value in the
lower subdiagonal.

The quantum recursive formulas and their normal-order anomaly were
proved in §3.7.4, (WP.7)–(WP.16), of
[*Opers, critical level and the Beilinson–Drinfeld construction*](opers-critical-level-and-the-beilinson-drinfeld-construction.md).
We now construct the classical map directly. Its products are
commutative differential-polynomial products, and its inner current
form remains the same trace form at every recursion step. The
differential-polynomial and scalar Adler conventions are those proved
in §3.7.3, (AP.1)–(AP.18). No quantum contraction is used as a
classical bracket.

##### The classical current and free-field brackets

For a finite list of differential generators \(u_a\), with specified
brackets \(H_{ab}(\lambda)=\{u_a{}_\lambda u_b\}\), their extension is
the finite formula
\[
 \{F_\lambda G\}
 =\sum_{a,b;r,s}
 \frac{\partial G}{\partial u_b^{(s)}}
 (\lambda+T)^s H_{ab}(\lambda+T)_{\to}
 (-\lambda-T)^r
 \frac{\partial F}{\partial u_a^{(r)}} .
 \tag{WF.3}
\]
Here \(u_a^{(r)}=T^r u_a\). Every derivative in the indicated operator
acts on the factors to its right; coefficients in \(H_{ab}\) stay
to the left of those derivatives. Repeated use of the two Leibniz
rules and sesquilinearity gives this formula and its uniqueness.
It is finite because \(F,G\) have finitely many variables.
The affine-generator extension, arrow rules and
generator-to-polynomial Jacobi reduction were proved
in §3.8.1, (DP.3)–(DP.13). We use exactly those
conventions and check every recursive image below.

The current brackets at a temporary scalar form
\(\ell\operatorname{tr}\) are
\[
 \{J_{ij}{}_\lambda J_{ab}\}
 =\delta_{ja}J_{ib}-\delta_{ib}J_{aj}
                         +\ell\delta_{ib}\delta_{ja}\lambda .
 \tag{WF.4}
\]
Their Jacobi identity on three generators is the matrix Lie Jacobi
identity together with trace invariance. Explicitly, the central
part in the first two Jacobi terms is
\[
 \ell\operatorname{tr}(x[y,z])\lambda
          -\ell\operatorname{tr}(y[x,z])\mu
 =\ell\operatorname{tr}([x,y]z)(\lambda+\mu),
\]
which is the central part of the third term. Symmetry of the trace
form proves skew symmetry. Formula (WF.3) then proves all identities
on differential polynomials: sesquilinearity handles derivatives,
and the Jacobiator's Leibniz rules reduce its vanishing successively
to three generators. Thus the current PVA is constructed over \(R\),
not inferred from field-valued points.

For each positive root \(i<j\), take free generators
\(\beta_{ij},\gamma_{ij}\), and take \(n\) bosons. Their only
nonzero basic brackets are
\[
 \{\beta_{ij}{}_\lambda\gamma_{ab}\}
       =\delta_{ia}\delta_{jb},\quad
 \{\gamma_{ij}{}_\lambda\beta_{ab}\}
       =-\delta_{ia}\delta_{jb},\quad
 \{b_i{}_\lambda b_j\}=\delta_{ij}\lambda .
 \tag{WF.5}
\]
The basic Jacobiators are zero because these brackets are constants
or constants times \(\lambda\). The same finite extension proves
that their differential polynomial algebra is a PVA. Independent
current and free-field factors have zero cross brackets.

##### Every matrix bracket in the recursion

Put \(m=n-1\). In a single step let \(J_{ij}\), \(i,j\leq m\),
be inner currents at form \(\ell\operatorname{tr}\). Use new
pairs \(\beta_i,\gamma_i\), and an independent new boson \(b\)
with bracket \(\{b_\lambda b\}=\epsilon\lambda\).
Keep \(\ell,\epsilon\) independent while computing. Define
\[
 \begin{aligned}
 \mathsf A_{ij}&=J_{ij}-\gamma_j\beta_i,&H&=b+\sum_a\gamma_a\beta_a,\\
 E_i&=\beta_i,&\Gamma_i&=\sum_a\gamma_aJ_{ai},\\
 U_i&=-\gamma_i b,&C_i&=-\sum_a\gamma_i\gamma_a\beta_a,\\
 D_i&=\ell\,T\gamma_i,&F_i&=\Gamma_i+U_i+C_i+D_i,\\
 \Delta&=\ell-\epsilon.
 \end{aligned}
 \tag{WF.6}
\]
All sums here run from \(1\) to \(m\). The full bracket table is
\[
 \begin{array}{c|l}
 \text{pair}&\lambda\text{-bracket}\\ \hline
 \{\mathsf A_{ij}{}_\lambda\mathsf A_{ab}\}&
 \delta_{ja}\mathsf A_{ib}-\delta_{ib}\mathsf A_{aj}
                          +\ell\delta_{ib}\delta_{ja}\lambda\\
 \{\mathsf A_{ij}{}_\lambda H\}&0\\
 \{H_\lambda H\}&\epsilon\lambda\\
 \{\mathsf A_{ij}{}_\lambda E_a\}&\delta_{ja}E_i\\
 \{H_\lambda E_a\}&-E_a\\
 \{\mathsf A_{ij}{}_\lambda F_a\}&-\delta_{ia}F_j\\
 \{H_\lambda F_a\}&F_a+\Delta\gamma_a\lambda\\
 \{E_i{}_\lambda F_j\}&\mathsf A_{ij}-\delta_{ij}H
                                             +\ell\delta_{ij}\lambda\\
 \{E_i{}_\lambda E_j\}&0\\
 \{F_i{}_\lambda F_j\}&
 -\Delta\gamma_i\gamma_j\lambda-\Delta(T\gamma_i)\gamma_j .
 \end{array}
 \tag{WF.7}
\]
Skew symmetry determines the reverse pairs, so this is every
matrix-unit bracket.

Here are the calculations, including the possible defects. Write
\(N=\sum_a\gamma_a\beta_a\). The product rules give
\(\{-\gamma_j\beta_i{}_\lambda-\gamma_b\beta_a\}
=\delta_{ja}(-\gamma_b\beta_i)
-\delta_{ib}(-\gamma_j\beta_a)\).
It has no central term. Adding the independent inner bracket gives
the first row. The trace \(N\) commutes with these ghost matrix
currents and has \(\{N_\lambda N\}=0\). This proves the second
and third rows. The rows containing \(E_a\) follow by taking one
beta-gamma bracket. In particular
\[
 \{\beta_i{}_\lambda F_j\}
 =J_{ij}-\gamma_j\beta_i
          -\delta_{ij}\left(b+\sum_a\gamma_a\beta_a\right)
                         +\ell\delta_{ij}\lambda .
 \tag{WF.8}
\]

For the \(\mathsf A_{ab},F_i\) row, the contributions from
\(J_{ab}\Gamma_i\) and the ghost against \(\Gamma_i\) are
\[
 \gamma_bJ_{ai}-\delta_{ai}\Gamma_b
                    +\ell\delta_{ai}\gamma_b\lambda,
 \qquad -\gamma_bJ_{ai}.
\]
The ghost brackets with \(U_i,C_i\) give
\(-\delta_{ai}U_b,-\delta_{ai}C_b\); the two extra terms in
its bracket with \(C_i\) cancel. Its bracket with \(D_i\) is
\(-\ell\delta_{ai}(\lambda+T)\gamma_b\).
The lambda terms cancel, and the sum is
\(-\delta_{ai}F_b\).

For \(HF_i\), the brackets of \(N\) with
\(\Gamma_i,U_i,C_i\) give those same three fields.
Its bracket with \(D_i\) is
\(\ell(\lambda+T)\gamma_i\), whereas
\(\{b_\lambda U_i\}=-\epsilon\gamma_i\lambda\).
Their sum is the displayed row. There is no additional term
depending on \(m\).

For the final row, the nondifferentiated single-bracket terms in
\(\Gamma_i\Gamma_j\) are
\(\gamma_i\Gamma_j-\gamma_j\Gamma_i\).
Those in \(\Gamma_iC_j+C_i\Gamma_j\) are their negatives.
The terms in \(U_iC_j+C_iU_j\) cancel, and the four
single beta-gamma terms in \(C_iC_j\) cancel as well.
The complete remaining terms, from the inner central bracket,
the boson bracket and the differentiated gamma terms, are
\[
 \begin{array}{c|l}
 \text{pair}&\text{remaining term}\\ \hline
 \{\Gamma_i{}_\lambda\Gamma_j\}&
       \ell\gamma_i(\lambda+T)\gamma_j\\
 \{U_i{}_\lambda U_j\}&
       \epsilon\gamma_j(\lambda+T)\gamma_i\\
 \{C_i{}_\lambda D_j\}&
       -\ell(\lambda+T)(\gamma_i\gamma_j)\\
 \{D_i{}_\lambda C_j\}&-\ell\lambda\gamma_i\gamma_j .
 \end{array}
 \tag{WF.9}
\]
Expanding gives lambda coefficient
\((\epsilon-\ell)\gamma_i\gamma_j\).
The \(\gamma_iT\gamma_j\) terms cancel, leaving
\((\epsilon-\ell)(T\gamma_i)\gamma_j\).
This proves the whole last row. It is also a direct check when
\(i=j\), with all repeated-factor multiplicities retained.

Set \(\ell=\epsilon=1\). The table is exactly (WF.4) at the
positive trace form for the assignments
\[
 J^{[n]}_{ij}\mapsto\mathsf A_{ij},\quad
 J^{[n]}_{in}\mapsto E_i,\quad
 J^{[n]}_{ni}\mapsto F_i,\quad
 J^{[n]}_{nn}\mapsto H.
 \tag{WF.10}
\]
For \(n=1\) start with \(J_{11}=b_1\). Induction constructs
\[
 \phi_n:\mathcal V_n
       =R[J_{ij}^{(r)}:1\leq i,j\leq n,\ r\geq0]
       \longrightarrow
 \mathcal F_n
       =R[\beta_{ij}^{(r)},\gamma_{ij}^{(r)},b_i^{(r)}
                               :i<j,\ r\geq0].
 \tag{WF.11}
\]
It is a differential-algebra homomorphism. Formula (WF.3) and
the checked generator brackets prove preservation of every
PVA bracket. In this classical construction the defect is
\(\ell-\epsilon\), not \(\ell+m+1-\epsilon\), and the
current form has no trace-tensor-trace summand.

##### Coisotropic ideals and their normalizers

We give the quotient construction used below. For a differential
ideal \(I\) in a PVA \(\mathcal V\), call it coisotropic when
\(\{I_\lambda I\}\subset I[\lambda]\), and put
\[
 U_I=\{a\in\mathcal V:\{c_\lambda a\}\in I[\lambda]
                                          \text{ for all }c\in I\}.
 \tag{WF.12}
\]
Then \(I\subset U_I\). This normalizer is a differential
subalgebra: the right Leibniz rule and sesquilinearity prove
closure under products and \(T\). It is also closed under
all coefficients of its lambda bracket. Indeed for
\(a,b\in U_I,c\in I\), Jacobi writes
\(\{c_\nu\{a_\lambda b\}\}\) as a sum of brackets of an
element of \(I\) with a normalizer element. Both sums are
in \(I[\lambda,\nu]\). The reverse-slot property follows
from skew symmetry and differential stability of \(I\).

Thus \(U_I/I\) is a PVA, with bracket computed by representatives.
Changing a representative by \(I\) changes its bracket with a
normalizer element by \(I[\lambda]\). This proves the quotient
operation; \(I\) need not be a Poisson ideal in the whole
ambient algebra.

It is enough to test the displayed normalizer condition on
differential generators \(c_\alpha\) of \(I\). For
\(qT^r c_\alpha\), the left Leibniz rule expresses its
bracket with \(a\) as the bracket of \(T^r c_\alpha\)
multiplied by derivatives of \(q\), plus terms containing
a derivative of \(c_\alpha\). The first terms lie in
\(I[\lambda]\) by sesquilinearity and the hypothesis,
and the latter by differential ideal stability.
Finite sums give the assertion for all of \(I\).
This reasoning allows coefficients \(q\) involving any
ambient generators.

More generally, let \(\phi:\mathcal V\to\mathcal F\) be a PVA
homomorphism and suppose
\[
 K=\langle\phi(I)\rangle_{\mathcal F,\,T}
 \tag{WF.13}
\]
is the differential ideal generated by its moment images.
If \(K\) is coisotropic, then \(\phi(U_I)\subset U_K\):
for each source moment, bracket preservation gives the
normalizer condition modulo \(K\); the preceding product
argument extends it to every element of \(K\), including
combinations with coefficients not in the image of \(\phi\).
Also \(\phi(I)\subset K\). Therefore the induced map
\[
 U_I/I\longrightarrow U_K/K
 \tag{WF.14}
\]
is a homomorphism of PVAs. The equality in (WF.13) is an
equality of *extended* differential ideals, not an assertion
that \(\phi\) is surjective.

##### The principal constraints are exactly the free beta constraints

Let
\[
 f_n=\sum_{i=1}^{n-1}E_{i+1,i},\qquad
 \chi(E_{ij})=\operatorname{tr}(f_nE_{ij})
                      =\delta_{j,i+1}\quad(i<j).
\]
In \(\mathcal V_n\) impose the differential ideal
\[
 I_n=\langle J_{ij}-\delta_{j,i+1}:i<j\rangle_T .
 \tag{WF.15}
\]
The trace form is zero on two strictly upper triangular matrices,
and \(\chi\) kills their commutators: a product of two such
matrices has height at least two. Hence the bracket of two
moment generators is the moment generator of their commutator.
Leibniz and sesquilinearity give
\(\{I_n{}_\lambda I_n\}\subset I_n[\lambda]\).
The principal reduced PVA is
\[
 \mathcal W_n=U_{I_n}/I_n .
 \tag{WF.16}
\]
By (WF.2), its moment space has \(A=f_n+B\) with \(B\)
upper triangular, including the diagonal.

In the free-field algebra define
\[
 K_n=\langle\beta_{ij}-\delta_{j,i+1}:i<j\rangle_T .
 \tag{WF.17}
\]
Its generators and all their derivatives bracket to zero
with one another, so it is coisotropic. We prove
\[
 \boxed{\langle\phi_n(I_n)\rangle_{\mathcal F_n,\,T}=K_n.}
 \tag{WF.18}
\]
At the outer step the constraints \(J^{[n]}_{in}\) give
exactly \(\beta_i-\delta_{i,m}\), \(m=n-1\).
For \(i<j\leq m\) the image of a moment generator is
\[
 \phi_{m}(J^{[m]}_{ij}-\delta_{j,i+1})
                        -\gamma_j\beta_i .
\]
Here \(i\leq m-1\), so its outer beta satisfies
\(\beta_i=0\) modulo the outer constraints. Thus the inner
moment images are unchanged modulo them. Induction gives
both inclusions in (WF.18): the outer beta constraints
are already source images; each inner moment image differs
from a source image by an outer-constraint multiple; and
the inner beta constraints are obtained recursively from
these images. Conversely every source image is a sum of
these inner constraints and such an outer multiple.
Applying \(T\) proves the same assertions for every jet.
This proves the equality over \(R\) itself.

The target reduction is exactly the boson algebra
\[
 U_{K_n}/K_n\simeq
       \mathcal H_n=R[b_i^{(r)}:1\leq i\leq n,\ r\geq0].
 \tag{WF.19}
\]
Indeed \(\mathcal F_n/K_n\) is the free polynomial algebra
on gamma and boson jets. For a class represented by \(a\),
\[
 \{\beta_{ij}{}_\lambda a\}\bmod K_n
   =\sum_{r\geq0}\lambda^r
             \frac{\partial\overline a}{\partial\gamma_{ij}^{(r)}}.
 \tag{WF.20}
\]
Its vanishing forces every gamma partial derivative to
vanish. In a polynomial ring over \(R\), a positive
exponent has an invertible positive integer as derivative
coefficient, so this means precisely that \(\overline a\)
is a boson polynomial. Conversely every boson polynomial
normalizes \(K_n\), since it brackets to zero with beta
constraints, and the full-ideal condition follows from
the product argument after (WF.12). Adding an element
of \(K_n\) preserves normalizer membership. This proves
(WF.19), including its uniqueness and surjectivity.
The bracket on the right is exactly (WF.5), since these
boson representatives already form a PVA subalgebra.

Combining (WF.14), (WF.18) and (WF.19) constructs the actual
principal Miura homomorphism
\[
\mu_n:\mathcal W_n\longrightarrow\mathcal H_n .
 \tag{WF.21}
\]
It preserves every lambda bracket. As an evaluation it
sets all beta jets to their moment values and all gamma
jets to zero, but only *after restriction to the
normalizer*. That evaluation is not a PVA map on the
whole free-field algebra: a beta constraint evaluates
to zero, and a gamma evaluates to zero, whereas their
bracket is \(1\).

The descent can equally be performed one rank at a time.
In the outer-step target take the ideal generated by
\(\beta_i-\delta_{i,m}\) and the inner moment ideal
\(I_m\). The same computation preceding (WF.18) shows
that this is the extended ideal of the source moments.
Its quotient is a polynomial algebra on outer gamma
jets over the inner moment quotient and the new boson
algebra. Outer beta brackets remove exactly those gamma
jets. The remaining normalizer tests are the inner
moment tests. Expanding a polynomial in the new boson
monomial basis, which is free over \(R\), shows that
each coefficient is an inner invariant class. Thus the
partial normalizer quotient is
\(\mathcal W_m\otimes_R R[b_n^{(r)}:r\geq0]\), with
its tensor-product PVA bracket. This gives an actual
reduced map at every outer step, and their iteration is
(WF.21). No Cartan-zero-mode invariance condition is
needed to remove the classical ghosts.

The reduction mechanism is the commuting square
\[
 \begin{array}{ccc}
 U_{I_n}&\xrightarrow{\ \phi_n\ }&U_{K_n}\\
 \downarrow&&\downarrow\\
 \mathcal W_n=U_{I_n}/I_n
       &\xrightarrow{\ \mu_n\ }&
 U_{K_n}/K_n\simeq\mathcal H_n .
 \end{array}
 \tag{WF.22}
\]
*The upper arrow is the actual matrix PVA homomorphism
(WF.11). The extended-ideal equality (WF.18) supplies
normalizer descent, even for moment combinations with
gamma coefficients. The right quotient is the canonical
beta-gamma reduction (WF.19)–(WF.20). Thus the lower
arrow is Poisson by quotient construction, not by an
assumed Poisson property of a Cartan projection.*

##### A matrix identity and injectivity of the reduced map

There is a useful exact description before setting the
gammas to zero. Let \(\mathbf J=(\phi_n(J_{ij}))\) be
the current-entry matrix, and let \(\gamma\) be the
column of outer gamma variables. For \(\ell=1\), direct
block multiplication in the commutative differential
ring gives
\[
 \mathbf J=
 G\begin{pmatrix}J&\beta\\0&b\end{pmatrix}G^{-1}
                   +(TG)G^{-1},
 \qquad
 G=\begin{pmatrix}I&0\\\gamma^t&1\end{pmatrix}.
 \tag{WF.23}
\]
Its lower-left block is exactly \(F\) in (WF.6),
including \(T\gamma\). Transpose, and put \(g=G^t\);
the trace-dual matrix satisfies
\[
 \phi_n(A)=
 g^{-1}\begin{pmatrix}J^t&0\\\beta^t&b\end{pmatrix}g
                                     +g^{-1}Tg .
 \tag{WF.24}
\]
Modulo \(K_n\), \(\beta^t=e_m^t\).
The last row of an upper unipotent inner matrix \(g_m\)
is \(e_m^t\), so that \(e_m^tg_m=e_m^t\).
Induction in (WF.24) therefore proves
\[
 \boxed{\quad
 \partial+\overline{\phi_n(A)}
   =g_n^{-1}\bigl(\partial+f_n+\operatorname{diag}(b_1,\ldots,b_n)\bigr)g_n,
 \qquad g_n\in N_n .
 \quad}
 \tag{WF.25}
\]
Here \(g_n=\operatorname{diag}(g_m,1)g\).
All identities use \(\partial a=a\partial+Ta\).
They hold in an ordinary differential-operator ring.

The gamma coordinates and the entries of \(g_n\) are
polynomially interchangeable. In blocks,
\(g_n=\left(\begin{smallmatrix}g_m&g_m\gamma\\0&1\end{smallmatrix}\right)\);
recover \(\gamma\) by multiplying the last column by
\(g_m^{-1}\). An upper unipotent inverse is the finite
sum \(I-U+U^2-\cdots+(-U)^{n-1}\).
Induction gives a polynomial inverse in all entries;
differentiating gives the same invertible change of
differential generators. No rational-point argument or
group integration theorem is required.

In fact the induced differential-algebra map
\[
 \theta_n:\mathcal V_n/I_n\longrightarrow\mathcal F_n/K_n
 \tag{WF.26}
\]
is injective. We prove this at every finite set of source
jets. The source quotient is the polynomial ring on
the upper and diagonal entries of \(A-f_n\) and their
jets. Linearize (WF.25) at \(g_n=I\), with all its
positive jets zero, and \(b=0\). Its tangent formula is
\[
 \dot A=\operatorname{diag}(\dot b)+[f_n,u]+Tu ,
 \qquad u\in\mathfrak n_+ .
 \tag{WF.27}
\]
The commutator \([f_n,u]\) is upper triangular:
on \(E_{ab}\), \(a<b\), it is
\(E_{a+1,b}-E_{a,b-1}\), with diagonal entries when
\(b=a+1\) and nonexistent boundary terms omitted.

At source jet order \(q\), set \(u^{(0)}=0\) and retain
the input variables \(u^{(1)},\ldots,u^{(q+1)}\) and
\(\dot b^{(0)},\ldots,\dot b^{(q)}\).
For any prescribed upper-triangular variations \(V_r\),
\(0\leq r\leq q\), solve successively
\[
 u^{(r+1)}=(V_r-[f_n,u^{(r)}])_{\rm strictly\ upper},
 \qquad
 \operatorname{diag}(\dot b^{(r)})
                    =(V_r-[f_n,u^{(r)}])_{\rm diagonal}.
 \tag{WF.28}
\]
This is an inverse to the square linear tangent map.
The original map in these variables is polynomial:
set the zeroth upper entries of \(g_n\) to zero, retain
jets through \(q+1\), and use its finite inverse in
(WF.25). It has this invertible linear part. A nonzero
polynomial relation in the source, translated to the
image of the indicated point, has a lowest nonzero
homogeneous part; substitution by an invertible linear
part keeps that part nonzero. Higher terms cannot
cancel it. This proves injectivity over \(k\) at every
finite source jet order. Tensoring its split
\(k\)-linear injection with \(R\) proves it over every
ordinary \(R\). Any polynomial uses finitely many jets,
so (WF.26) is injective.

A reduced source class belongs to the subalgebra
\(\mathcal W_n\subset\mathcal V_n/I_n\).
Its image under (WF.26) is gamma-free by (WF.20).
Therefore (WF.21) is injective on the *entire*
coisotropic normalizer quotient. This argument does
not require a polynomial-exhaustion theorem for
\(\mathcal W_n\).

##### The scalar generators and the order of the factors

For \(A=f_n+B\), with \(B\) upper triangular, eliminate
the first \(n-1\) components from
\((\partial+A)y=0\), starting with the last row.
The row \(n\) expresses \(y_{n-1}\) as a differential
operator on \(y_n\); row \(n-1\) then expresses
\(y_{n-2}\), and so on. Each step has coefficient one
on the component being eliminated. The final first
row, multiplied by \((-1)^{n-1}\), gives a unique
monic operator
\[
 D_A=\partial^n+\sum_{i=1}^n w_i(A)\partial^{n-i},
 \tag{WF.29}
\]
whose coefficients are finite differential
polynomials in the entries of \(B\).
The corresponding left differential module is
cyclic on \(y_n\), with annihilator generated by
\(D_A\): these substitutions give inverse
presentations with one generator and with the \(n\)
row relations.

These coefficients are invariant under upper
unipotent gauge transformations, with the convention
\(A^g=g^{-1}Ag+g^{-1}Tg\) of (DP.29).
Such a transformation
preserves the form \(f_n+B\): multiplying \(f_n\) by
upper unipotent matrices leaves all entries below
the subdiagonal zero and every subdiagonal entry one;
the derivative term is upper triangular. It also
preserves \(y_n\), since its last row is \(e_n^t\).
Consequently the transformed cyclic presentation has
the same generator and annihilator left ideal.
Two monic operators of order \(n\) with that same
left ideal are equal. Their difference has order
less than \(n\); a nonzero left multiple of a monic
order-\(n\) operator has order at least \(n\), even
over rings with zero divisors, since the leading
coefficient of the monic operator is \(1\).
This proves equality of the operators over \(R\).

It also proves that every \(w_i\) represents a class
in \(U_{I_n}/I_n\). To see the normalizer condition
directly, take an independent differential test
symbol \(v\), \(x\in\mathfrak n_+\), and
\(g=1+\eta vx\), \(\eta^2=0\). The infinitesimal
gauge action is
\[
 \dot A=[A,vx]+T(vx).
 \tag{WF.30}
\]
By (WF.1)–(WF.3) this is exactly the Hamiltonian
variation of \(\int vJ_x\). If
\(\{J_x{}_\lambda w_i\}=\sum_j c_j\lambda^j\),
its induced variation is \(\sum_j c_jT^jv\).
Gauge invariance gives zero modulo \(I_n\);
the test jets are independent polynomial variables,
so every \(c_j\) lies in \(I_n\). This proves the
condition on each moment generator, hence on the
whole ideal by (WF.12). Choosing a different lift
of \(w_i\) from the moment quotient changes it by
\(I_n\) and changes no reduced class.

Now evaluate (WF.25) at gamma zero and the beta
moment values. The trace-dual matrix is exactly
\(f_n+\operatorname{diag}(b_1,\ldots,b_n)\).
Its rows give
\(y_{i-1}=-(\partial+b_i)y_i\), \(i=2,\ldots,n\).
Substitute them into
\((\partial+b_1)y_1=0\). Therefore
\[
 \boxed{\quad
 \mu_n(D_A)
     =(\partial+b_1)(\partial+b_2)\cdots(\partial+b_n).
 \quad}
 \tag{WF.31}
\]
The factors appear in this forward order. There
are no ghost state contractions to reverse them.

For \(n=2\), write \(\beta=\beta_{12}\),
\(\gamma=\gamma_{12}\). Modulo \(\beta-1\), the
whole dual matrix is
\[
 \overline{\phi_2(A)}=
 \begin{pmatrix}
 b_1-\gamma&\gamma(b_1-b_2)-\gamma^2+T\gamma\\
 1&b_2+\gamma
 \end{pmatrix}.
 \tag{WF.32}
\]
For \(A=\left(\begin{smallmatrix}a&c\\1&d\end{smallmatrix}\right)\),
the scalar coefficients are \(w_1=a+d\) and
\(w_2=ad+Td-c\). Substitution in (WF.32) cancels
every gamma term and gives
\[
 \mu_2(w_1)=b_1+b_2,\qquad
 \mu_2(w_2)=b_1b_2+Tb_2 .
 \tag{WF.33}
\]
This checks both the trace-dual convention and
the derivative sign by actual reduction.

The full coefficient brackets of the ordered product
were proved in (AP.7)–(AP.12). Let their polynomial
expressions be \(H_{ij}(\lambda;w,Tw,\ldots)\),
with the convention
\(\{w_j{}_\lambda w_i\}=H_{ij}\).
Since \(\mu_n\) is an injective PVA map and
(WF.31) gives those same factors,
\[
 \{w_j{}_\lambda w_i\}_{\mathcal W_n}
                     =H_{ij}(\lambda;w,Tw,\ldots).
 \tag{WF.34}
\]
Indeed the difference has zero image, so each
coefficient is zero by injectivity. The scalar
coefficient classes and all their derivatives
are algebraically independent: their images are
the independent differential Miura coefficients
of (AP.13), equivalently the highest-degree jet
calculation (MC.11)–(MC.13). The matching source
polynomial-exhaustion theorem (MG.20) proves
\(\mathcal W_n=R[w_i^{(r)}]\); its covector
scalar relation (MG.5) and ordered diagonal
evaluation (MG.24) are exactly (WF.29) and
(WF.31). Consequently (WF.34) is the entire
principal reduced PVA bracket, identified with
the positive scalar Adler bracket of
(AP.7)–(AP.12). The free-field descent and
injectivity above were proved independently
of that polynomial-exhaustion theorem.

##### Orthogonal trace restriction and ordinary parameters

For \(\mathfrak{sl}_n\), take an orthogonal
subalgebra of the raw current and boson PVAs.
The source scalar generator
\(c_{\rm src}=J_I/n\) has bracket
\(\{c_{\rm src}{}_\lambda c_{\rm src}\}=\lambda/n\)
and commutes with all traceless currents.
On the target put
\[
 c=\frac1n\sum_i b_i,\qquad
 \bar b_i=b_i-c,\qquad \sum_i\bar b_i=0.
\]
Then
\[
 \{\bar b_i{}_\lambda\bar b_j\}
    =(\delta_{ij}-1/n)\lambda,\quad
 \{c_\lambda\bar b_i\}=0,\quad
 \{c_\lambda c\}=\lambda/n .
 \tag{WF.35}
\]
The trace of (WF.10) is \(\sum_i b_i\).
A common shift \(b_i\mapsto b_i+c\) adds \(c\)
to each diagonal current, and leaves every
off-diagonal current unchanged: in \(F_i\) the
new terms are \(\gamma_i c-\gamma_i c=0\).
Induction proves that the traceless source
lands in the subalgebra generated by ghosts
and trace-zero bosons. Thus the source and
target in (WF.11) restrict to their true
orthogonal trace-zero subalgebras.

All upper moment constraints are traceless.
Their extended ideal remains (WF.18).
The canonical quotient gives the trace-zero
boson algebra, with the projected matrix
\(P=I-\mathbf1\mathbf1^t/n\) in (WF.35).
Every normalizer descent proof still applies.
The finite-jet injectivity proof also restricts:
\([f_n,u]\) and \(Tu\) have trace zero, and
the prescribed diagonal variations in (WF.28)
sum to zero, so the recovered boson variations
do as well. Hence the reduced map remains
injective. In (WF.31) replace \(b_i\) by
\(\bar b_i\); its first coefficient is zero.
The resulting reduced scalar brackets are
exactly (AP.14)–(AP.18). This is an
orthogonal-subalgebra construction; imposing
the trace current as a quotient of the raw
positive-form PVA would be invalid, since
its bracket is \(n\lambda\).

All arguments are direct over ordinary \(R\).
There is also exact ordinary base change of
the source reduction. In its free moment
quotient retain jets through order \(q\) and
polynomials of ordinary entry degree at most
\(d\). This is a finite-dimensional \(k\)-space.
The coefficient moment actions preserve these
bounds: (WF.30) is affine linear in the entries
of \(A-f_n\), its \(r\)-th derivative uses entry
jets of order at most \(r\), and its test
symbol uses jets of order at most \(r+1\).
The normalizer classes in that space are
therefore the kernel of a finite matrix of
linear moment equations. Tensoring with \(R\)
preserves that kernel, because \(R\) is flat
over \(k\). Taking the union over \(q,d\)
gives
\[
 \mathcal W_{n,R}=R\otimes_k\mathcal W_{n,k},
 \qquad
 \mu_{n,R}=R\otimes_k\mu_{n,k}.
 \tag{WF.36}
\]
The ideal quotient, canonical target reduction,
polynomial gauge formulas and all lambda
brackets commute with these coefficient maps.
This includes nilpotent parameters without
testing their field-valued points.

Products use independent current, ghost
and boson lists, so cross brackets vanish
and the componentwise construction gives
the product principal Miura map. For
\(\mathfrak{gl}_1\) it is the identity of
the positive-form boson PVA; for
\(\mathfrak{sl}_1=0\) or the trivial algebra
it is the coefficient ring with zero bracket.
The theorem concerns the classical matrix
coisotropic principal reduction. It makes
no factorization-sheaf, geometric Satake,
global localization or derived-family claim.

#### 3.8.4. Laurent reduction, topology and coordinate transport

The regular differential-polynomial reduction and the reduction of Laurent connections have different coefficient algebras. The former is a Poisson vertex algebra. The latter uses all integer current modes and a jointly continuous ordinary Poisson bracket. We construct the latter directly, rather than imposing regularity as an ordinary Poisson relation.

Fix \(\mathfrak g=\mathfrak{gl}_n\), or its trace-zero subalgebra, and \(B(X,Y)=\operatorname{tr}(XY)\). Let \(R\) be an ordinary commutative algebra over a characteristic-zero field. For \(N\geq1\), put
\[
\mathcal C_{N,R}=R[J_{x,m}:m<N],\qquad
\widehat{\mathcal C}_R=\varprojlim_N\mathcal C_{N,R}.
\tag{DL.1}
\]
Here \(x\) ranges through a fixed basis of \(\mathfrak g\), the variables are linear in \(x\), and the transition sets newly admitted modes to zero. In the trace-zero case use a basis of that subalgebra. Trace duality identifies \(J_{x,m}\) with \(\operatorname{tr}(xA_m)\), where
\(A(t)=\sum_mA_m t^{-m-1}\). Thus a continuous character to a discrete coefficient algebra specifies a Laurent matrix with a common finite pole bound. The argument is the same explicit factor-through-a-stage argument as (PC.4); no assertion about arbitrary discontinuous characters is used.

On the polynomial algebra in all modes define
\[
\{J_{x,m},J_{y,r}\}
=J_{[x,y],m+r}+mB(x,y)\delta_{m+r,0}.
\tag{DL.2}
\]
The affine Jacobi proof preceding (K2.2), using invariance of \(B\), proves Jacobi on these linear generators. Extension by the ordinary Leibniz rule reduces Jacobi on polynomials to that calculation. This gives a polynomial Poisson bracket before completion.

We prove its continuous extension. Let \(K_N\) be the kernel of the \(N\)-th projection. For finite polynomials, the ideal generated by modes \(m\geq N\) has
\[
\{K_N,K_M\}\subset K_N\quad(M\geq N\geq1).
\tag{DL.3}
\]
Initially this formula refers to the polynomial ideals. In a bracket of two monomials, if the chosen bracket does not remove the distinguished high factor in both monomials, one such factor remains. If it removes both, (DL.2) supplies a mode of index at least \(N+M\); the scalar term is zero because both indices are positive. Every term therefore lies in the displayed ideal. This proves (DL.3) by Leibniz.

For any fixed polynomial \(p\), let \(a\) be the least mode index among its variables, taking \(a=0\) when it is constant. Then
\[
\{p,K_M\}\subset K_N
\quad\text{if }M\geq\max(N,N-a).
\tag{DL.4}
\]
Indeed a bracket which removes the only high factor has new index at least \(M+a\geq N\), and cannot have a scalar term; every other term retains a high factor.

Take compatible finite polynomial approximants to \(u,v\in\widehat{\mathcal C}_R\). For a required output cutoff \(N\), fix their polynomial representatives \(u_N,v_N\). Each later approximant differs from these by a polynomial in the \(N\)-th tail ideal. If a perturbation is in the \(M\)-th tail ideal, (DL.4) bounds its bracket with \(u_N,v_N\), while (DL.3) bounds its bracket with those remaining \(N\)-tails. For sufficiently large \(M\), every resulting difference lies in \(K_N\). Thus the brackets of approximants are Cauchy, independently of the approximants. Completeness defines their limit. The same bounds prove joint continuity at \((u,v)\), and prove (DL.3)–(DL.4) for the completed ideals as well. Leibniz, skew symmetry and Jacobi pass to limits of polynomial inputs. We have constructed a unique jointly continuous bracket (DL.2) on the entire completion. Each ordinary coefficient map commutes with it, by the finite formulas and continuity. As in (CW.19), its coefficient extension is stagewise and completed, not an unproved interchange of tensor product and inverse limit. Individual \(K_N\) are not asserted to be Poisson ideals against the whole algebra.

**The closed moment ideal.** Let
\[
\mathfrak n_+=\langle E_{ij}:i<j\rangle,\qquad
f=\sum_{i=1}^{n-1}E_{i+1,i},\qquad
\chi(x)=\operatorname{tr}(fx).
\tag{DL.5}
\]
The full Laurent moment constraints are
\[
\mu_{x,m}=J_{x,m}-\chi(x)\delta_{m,-1},
\qquad x\in\mathfrak n_+,\quad m\in\mathbb Z.
\tag{DL.6}
\]
The index \(-1\) is forced by a constant connection coefficient, whose current-field expansion has exponent zero. Let \(I\) be the closed ideal generated by these constraints. At every cutoff their quotient simply eliminates the corresponding independent linear coordinates, leaving the upper-triangular coefficients of \(A=f+b_+\). The sections which use only those remaining coordinates are compatible. The quotient is therefore exactly the completed coefficient algebra of these Laurent matrices; reduction is surjective and has this continuous linear section. Kernel equality follows by choosing an ideal polynomial representative at each cutoff. This also proves that the finite polynomial moment ideal is dense in \(I\).

The restriction of \(B\) to \(\mathfrak n_+\) is zero and \(\chi([\mathfrak n_+,\mathfrak n_+])=0\). Formula (DL.2) consequently gives
\(\{\mu_{x,m},\mu_{y,r}\}=\mu_{[x,y],m+r}\).
Leibniz and the density just proved give
\[
\{I,I\}\subset I.
\tag{DL.7}
\]
Define the closed normalizer
\[
\mathcal U_R=
\{u\in\widehat{\mathcal C}_R:
       \{\mu_{x,m},u\}\in I\text{ for all }x,m\},
\qquad
\widehat W^{\mathrm{DS}}_R=\mathcal U_R/I.
\tag{DL.8}
\]
Here \(I\subset\mathcal U_R\) by (DL.7). For \(u\in\mathcal U_R\), Leibniz first proves \(\{u,I\}\subset I\) on the finite ideal and then on its closure. Jacobi now proves closure of \(\mathcal U_R\) under brackets; Leibniz proves closure under products. Hence \(I\) is a Poisson ideal in this normalizer and its quotient has a bracket independent of representatives. This is an actual coisotropic reduction. It does not make the entire ambient quotient by \(I\) a Poisson algebra.

We identify its invariants and its topology. For a Laurent test matrix \(X(t)\), put
\[
\ell_X(A)=\operatorname{Res}\operatorname{tr}(X(t)A(t))dt.
\tag{DL.9}
\]
It is a completed linear function, since \(X\) has a finite negative tail and only finitely many of its positive coefficients contribute at a fixed cutoff. Formula (DL.2) reads
\[
\{\ell_X,\ell_Y\}(A)
=\operatorname{Res}\operatorname{tr}(A[X,Y]+X'Y)dt.
\tag{DL.10}
\]
Its Hamiltonian vector field on \(A\) is \([A,X]+X'\). On the moment fibre this is the infinitesimal action of the inverse unipotent gauge \(g=1-sX+O(s^2)\) in the convention \(A\mapsto gAg^{-1}-g'g^{-1}\). All moment modes in (DL.6), including negative ones, are needed here. Positive currents alone give the regular-jet invariant condition of §3.8.1, rather than this full Laurent action.

For a root test \(X=q(t)E_{ij}\), \(i<j\), the one-parameter gauge is \(1-sq(t)E_{ij}\), with polynomial inverse. For an input of fixed pole bound its transformed matrix has a pole bound independent of \(s\). A completed function restricts at that bound to a polynomial in finitely many coefficients, so its pullback is a polynomial in \(s\). Vanishing of its infinitesimal derivative at every input makes this polynomial constant: differentiate at an arbitrary \(s\) using the group law and the same infinitesimal condition, then use that the positive integers are units in \(R\). Every upper unipotent Laurent matrix is a finite product of these elementary matrices, by successive upper-entry elimination. Normalizer invariance therefore implies the whole \(N_+(R((t)))\)-gauge invariance. Conversely, differentiating this action over \(R[s]/(s^2)\) proves the moment normalizer condition. Formal positive tails cause no extra assumption: the completed linear functions (DL.9) are the limits of their finite tests, and each fixed coefficient calculation uses only finitely many test coefficients.

The matrix theorem of §3.8.2 supplies a unique gauge and scalar operator for each such connection. Its weighted pole bounds are
\[
\operatorname{pole}(A_{ab})\leq(b-a+1)N,
\quad
\operatorname{pole}(g_{ab})\leq(b-a)N,
\quad
\operatorname{pole}(s_j)\leq jN.
\tag{DL.11}
\]
These weighted charts are cofinal with common finite pole bounds. Their normal-form map and inverse are coefficientwise polynomial maps and identify the constraint chart with the product of its gauge chart and scalar chart. An invariant function on this product is independent of its gauge coordinate: translate that coordinate to the identity using its own inverse, over the universal coefficient algebra. This argument is a polynomial identity and remains valid over nonreduced \(R\). Taking the compatible charts shows that the algebra of invariant completed functions is precisely the \(P_R\) of (PC.3).

The resulting map
\[
\Theta_R:\widehat W^{\mathrm{DS}}_R\xrightarrow{\sim}P_R
\tag{DL.12}
\]
is a topological algebra isomorphism. One can check its inverse directly: the scalar normal-form coefficient \(s_j(A)\) is a fixed differential polynomial in the upper entries. Substituting these polynomials gives a continuous algebra map from \(P_R\) into the ambient completion. Its reductions are gauge invariant, so its image lies in \(\mathcal U_R\). The exact pole bounds (DL.11) give continuity at every cutoff; evaluation in companion form gives its inverse modulo \(I\). This proves completeness of the reduced algebra through the explicit isomorphism. No general theorem about completeness of a quotient is assumed. All constructions commute with ordinary coefficient maps.

**Coordinate action, with the normalization gauge proved.** First any fixed Laurent gauge \(g\) preserves the ambient Poisson bracket. Indeed
\[
\ell_X(gAg^{-1}-g'g^{-1})
=\ell_{g^{-1}Xg}(A)
 -\operatorname{Res}\operatorname{tr}(Xg'g^{-1})dt.
\tag{DL.13}
\]
Writing \(V=g'g^{-1}\), direct differentiation gives
\((g^{-1}Xg)'=g^{-1}(X'+[X,V])g\).
Thus the transformed cocycle is
\[
\operatorname{Res}\operatorname{tr}
 ((g^{-1}Xg)'g^{-1}Yg)dt
=\operatorname{Res}\operatorname{tr}(X'Y-V[X,Y])dt.
\]
This is exactly the correction to the Lie term in (DL.10) under (DL.13). The linear generators determine polynomial brackets; finite pole bounds and continuity extend the equality to the completion. For a trace-zero algebra, take the trace-free part of the gauge connection; the discarded scalar does not pair with traceless tests. The same identity proves the result directly for those tests.

Let \(\psi=\phi^{-1}\), \(\alpha=\psi'\), \(c=\alpha'/\alpha\), and
\(D=\operatorname{diag}(\alpha^{n-1},\alpha^{n-2},\ldots,1)\).
There are no square roots in the following normalized formula:
\[
A^\phi
=D\bigl(\alpha A\circ\psi\bigr)D^{-1}
  -D'D^{-1}+\frac{n-1}{2}c\,\mathbf1.
\tag{DL.14}
\]
Inverse one-form substitution preserves (DL.10) by residue change of variable (RC.C7). The gauge part is Poisson by (DL.13). Addition of a fixed scalar matrix is Poisson in the raw matrix case: its Lie contribution is \(\operatorname{tr}[X,Y]=0\), and the cocycle is unchanged. In the trace-zero case this last term is precisely the trace correction just described. Formula (DL.14) is therefore Poisson.

Its lower adjacent entry is \(\alpha\alpha^{n-i-1}/\alpha^{n-i}=1\); the lower entries further from the diagonal remain zero. Its trace is \(\alpha\operatorname{tr}(A)\circ\psi\), since the trace of \(D'D^{-1}\) is \(n(n-1)c/2\). Thus it preserves the moment fibre and the trace-zero relation. It conjugates an upper gauge \(u\) to \(D(u\circ\psi)D^{-1}\), so it induces the action on the reduction. Finite pole bounds, and the nilpotent-translation cofinality already proved in (PC.8), give continuity for every ordinary coordinate, including nilpotent constants.

On a diagonal Miura representative its diagonal entries are exactly
\[
h_i^\phi=\alpha h_i\circ\psi+
       \left(i-\frac{n+1}{2}\right)c.
\tag{DL.15}
\]
This is the affine density shift (MC.20), not a collection of unshifted one-forms. Formally multiply \(D\) by the common scalar \(\alpha^{-(n-1)/2}\). The last component of a horizontal vector then transforms as a density of weight \((1-n)/2\). The covector construction (O4.2) consequently transforms its scalar equation by the density law (SC.O6). Where half-integer powers occur, the free rank-two square-root extension and sign-independent descent (SC.O4)–(SC.O6) apply; the actual matrix formula (DL.14) has already descended without a root. Normal-form uniqueness proves
\[
\Theta_R\sigma_\phi^{\mathrm{DS}}
 =\sigma_\phi^{\mathrm{Op}}\Theta_R.
\tag{DL.16}
\]
The chain rule for \(c\), together with ordinary substitution, gives composition and inverses in (DL.14); equivalently these follow from the density transport and the unique normalization gauge. This proves the coordinate action itself as well as its compatibility with the quotient.

The construction has the following precise square:
\[
\begin{array}{ccc}
\mathcal U_R&\longrightarrow&\widehat W_R^{\mathrm{DS}}\\
{\scriptstyle\sigma_\phi}\downarrow&&
\downarrow{\scriptstyle\sigma_\phi^{\mathrm{DS}}}\\
\mathcal U_R&\longrightarrow&\widehat W_R^{\mathrm{DS}}.
\end{array}
\tag{DL.17}
\]
*The horizontal arrows divide by the closed coisotropic moment ideal (DL.6)–(DL.8). The complete ambient bracket is constructed by the explicit tail estimates (DL.3)–(DL.4). The vertical arrows use inverse substitution and the normalization gauge (DL.14); the residue calculation (DL.13) proves their Poisson property. The coefficient isomorphism (DL.12) identifies the reduced space with the Laurent scalar-oper coefficient functor. Its comparison with the explicit scalar Adler bracket is proved next.*

This is the ordinary Laurent reduction. The regular differential-polynomial comparison of §3.8.1 is a Poisson vertex comparison. Passing from the Laurent algebra to regular coefficient functions is not declared an ordinary Poisson quotient; the forbidden-mode examples (CP.17)–(CP.18) still distinguish those notions.

#### 3.8.5. The full matrix Hamiltonian-reduction comparison

We now compare the actual reduction with the scalar bracket. All forms in this comparison are specified. The classical affine Poisson vertex algebra of §3.8.1 has form \(+\operatorname{tr}\). The quantum center of §3.7 instead has critical form \(-n\operatorname{tr}\) on \(\mathfrak{sl}_n\), with deformation direction \(+\operatorname{tr}\). These are different affine algebras. Their reduced coefficient brackets agree through the proved scalar and Miura maps; equality is not an identification of their current fields.

Write \(W_R^{\mathrm{DS}}\) for the differential-polynomial coisotropic reduction of §3.8.1. The normal-form invariant theorem of §3.8.2 identifies it, as a differential algebra, with
\[
\theta_R:W_R^{\mathrm{DS}}\xrightarrow{\sim}
R[s_j^{(r)}:r\geq0],
\quad
\begin{cases}
1\leq j\leq n&\text{for raw matrices},\\
2\leq j\leq n&\text{for trace-zero matrices}.
\end{cases}
\tag{DC.1}
\]
The classical field map and moment-normalizer descent of §3.8.3 prove the Miura Poisson vertex map \(\mu_R\). Its exact generator images are the coefficients of \((\partial+h_1)\cdots(\partial+h_n)\). They are precisely the injection \(j_R^{\mathrm{reg}}\) of (AP.13), with the orthogonal trace-zero boson matrix in that case. Consequently
\[
\mu_R=j_R^{\mathrm{reg}}\theta_R.
\tag{DC.2}
\]
This is an identity on actual invariant generators and all their derivatives, rather than an equality of highest symbols. The normalizer quotient in §3.8.3 proves the Poisson property of \(\mu_R\); ordinary Cartan evaluation on the ambient affine algebra would not prove it.

For \(a,b\in W_R^{\mathrm{DS}}\), apply that property and the proved scalar factorization (AP.9), or its orthogonal reduction (AP.14):
\[
\begin{aligned}
j_R^{\mathrm{reg}}\theta_R(\{a_\lambda b\}_{\mathrm{DS}})
&=\{j_R^{\mathrm{reg}}\theta_R(a){}_{\lambda}
                 j_R^{\mathrm{reg}}\theta_R(b)\}_{\mathrm{bos}}\\
&=j_R^{\mathrm{reg}}
     \{\theta_R(a){}_{\lambda}\theta_R(b)\}_{\mathrm{AGD}}.
\end{aligned}
\tag{DC.3}
\]
The injection (AP.13) cancels. Thus (DC.1) is a Poisson vertex isomorphism onto the explicit scalar Adler–Gelfand–Dickey algebra. Every bracket is the finite formula (AP.11), or (AP.17) with its polynomial primitive (AP.16). In particular the principal matrix Hamiltonian reduction, rather than a merely named scalar reference bracket, has now been identified in every degree and derivative order.

**Why the same statement controls every Laurent Fourier mode.** We give the coefficient argument independently of a general vertex reconstruction theorem. Put
\[
\delta(z,w)=\sum_{m\in\mathbb Z}z^{-m-1}w^m.
\]
The current bracket (DL.2) is exactly
\[
\{J_x(z),J_y(w)\}
=J_{[x,y]}(w)\delta(z,w)+B(x,y)\partial_w\delta(z,w).
\tag{DC.4}
\]
Extracting \(\operatorname{Res}_z z^m\operatorname{Res}_w w^q\) gives its Lie mode \(J_{[x,y],m+q}\) and scalar \(mB(x,y)\delta_{m+q,0}\). For differential-polynomial fields, the kernel form of their Poisson vertex bracket is proved from this identity by the two elementary rules
\[
\partial_z\delta=-\partial_w\delta,
\qquad
a(z)\partial_w^r\delta
=\sum_{v=0}^r\binom rv a^{(v)}(w)
                       \partial_w^{r-v}\delta.
\tag{DC.5}
\]
The second follows by differentiating \(a(z)\delta=a(w)\delta\) exactly \(r\) times. Derivatives in the first argument therefore give \(-\lambda\), derivatives in the second give \(T+\lambda\), the right product gives ordinary Leibniz, and moving left factors by (DC.5) gives precisely the shifted left Leibniz rule. Induction on products and derivatives proves that if
\(\{a_\lambda b\}=\sum_{r\geq0}\lambda^r c_r/r!\), then its field kernel is
\(\sum_r c_r(w)\partial_w^r\delta/r!\). The sum is finite. At any desired Fourier coefficient all products are finite after a cutoff, because their index sum is fixed and each input index has an upper bound. Thus the distribution argument is an identity of the actual completed coefficient functions, not an analytic distribution argument.

The grading used after the principal reduction is the principal weight
\(\deg J_x=1-\operatorname{ht}(x)\), \(\deg T=1\), for root-homogeneous \(x\). The affine bracket has degree \(-1\), as one checks on its Lie and scalar terms. A simple positive moment current has weight zero, so its equality to \(1\) is homogeneous; all other moment characters are zero. The scalar normal-form coefficient \(s_i\) has weight \(i\), either by the covector construction or by its injective ordered Miura image. Hence \(c_r\) in a bracket of weights \(i,j\) has weight \(i+j-r-1\). This grading is not the ordinary energy-one grading of every unreduced current. Physical current indices still refer to exponent \(-m-1\); a chosen normalized field weight merely relabels them.

Write the scalar field as \(s_i(z)=\sum_p s_{i,p}z^{-p-i}\), and use the corresponding weight for each \(c_r\). Extracting residues in (DC.4)–(DC.5) now gives, for every pair of integers,
\[
\{s_{i,p},s_{j,q}\}_{\mathrm{DS}}
=\sum_{r\geq0}\binom{p+i-1}{r}
                             (c_r)_{p+q}.
\tag{DC.6}
\]
Indeed the two residue test exponents are \(p+i-1\) and \(q+j-1\). After differentiating the first test \(r\) times, the output exponent is \(p+q+i+j-r-2\), exactly the exponent selecting normalized mode \(p+q\) of weight \(i+j-r-1\). Generalized binomial coefficients handle negative \(p+i-1\). Scalar coefficients use the weight-zero identity-field convention. This proves the all-integer formula with the correct moment normalization (DL.6).

The same extraction in the boson coefficient algebra proves its Fourier brackets from (AP.1)–(AP.2). By (DC.3), the differential coefficients \(c_r\) have identical scalar Adler formulas. Products of scalar fields can have infinite mode convolutions, but each convolution is a finite polynomial at a weighted pole cutoff, exactly as proved before (CP.21). Formula (DC.6) therefore proves equality of the reduced bracket and the scalar bracket on all coefficient generators, with values in the completion. Leibniz proves equality on polynomial inputs. These are dense in \(P_R\); the reduced bracket is jointly continuous by (DL.2)–(DL.12), and the scalar bracket by (CP.20)–(CP.21). Equality passes to arbitrary pairs of completed inputs. We obtain
\[
\boxed{\Theta_R:
 (\widehat W_R^{\mathrm{DS}},\{\ ,\ \}_{\mathrm{DS}})
 \xrightarrow{\sim}(P_R,\{\ ,\ \}_{\mathrm{AGD}}).}
\tag{DC.7}
\]
This proves the full ordinary Laurent Hamiltonian-reduction Poisson comparison. It does not require a bound on the degree of a whole completed element, or a Poisson structure on an individual pole-cutoff quotient.

**A rank-two check of the moment ideal and sign.** In the trace-zero matrix fibre write
\(A=\begin{pmatrix}H/2&F\\1&-H/2\end{pmatrix}\).
The scalar coefficient is
\[
w_2=-F-\tfrac12TH-\tfrac14H^2.
\tag{DC.8}
\]
Before imposing the moment relation, the affine generator \(E=J_{E_{12}}\) has \(\{E_\lambda F\}=H+\lambda\) and \(\{E_\lambda H\}=-2E\). Sesquilinearity and Leibniz give
\[
\{E_\lambda w_2\}=(E-1)(H+\lambda)+TE\in I[\lambda].
\tag{DC.9}
\]
Thus its invariance is an actual moment-normalizer calculation. On the diagonal representative \(F=0,H=2h\), it becomes \(-h'-h^2\), with \(\{h_\lambda h\}=\lambda/2\). Equation (AP.20) gives
\(\{w_2{}_{\lambda}w_2\}=-(T+2\lambda)w_2-\lambda^3/2\), the same sign and normalization as the critical determinant coefficient (CP.16). The diagonal evaluation is Poisson on this reduced algebra by §3.8.3; it is not a Poisson projection on arbitrary \(E,F,H\).

Combining (DC.7) with the already proved critical-center isomorphism (CP.21) gives the coordinate-equivariant comparison
\[
\begin{array}{ccc}
Z(\widehat A_{\mathrm{crit},R})
&\xrightarrow{\ \Phi_R\ }&P_R\\
& &\uparrow{\scriptstyle\Theta_R}\\
&&\widehat W_R^{\mathrm{DS}}.
\end{array}
\tag{DC.10}
\]
*Both arrows are topological Poisson isomorphisms. The upper arrow uses the critical level deformation, actual quantum free-field map and scalar bracket of §3.7. The lower arrow uses the classical affine form \(+\operatorname{tr}\), its coisotropic moment ideal, the matrix gauge theorem and the classical free-field descent of §3.8. The scalar Adler formulas make their brackets identical. Coordinate compatibility is (PC.13) and (DL.16), with the exact density shift (DL.15). This diagram does not identify the two unreduced affine algebras.*

The regular version compares Poisson vertex algebras; the Laurent version compares completed ordinary Poisson algebras. Products of type A factors use these maps componentwise and a common pole bound. For \(\mathfrak{gl}_1\) there is no unipotent moment constraint and the comparison is the identity \(L=\partial+h\); for \(\mathfrak{sl}_1=0\) it is the coefficient ring. All calculations use matrix units, positive integer divisions, polynomial differentiation and cofinal finite pole bounds, and hold over every ordinary characteristic-zero coefficient algebra.

The result identifies the ordinary principal matrix Hamiltonian reduction, including its exact local coordinate normalization. It does not construct a derived reduction, a global chiral or factorization comparison, geometric Satake, critical localization or the global eigenobject theorem. Section 3.9 proves the general ordinary principal classical reduction at the specified structural datum and form. Quantum center identifications in other types, exact dual-form normalization, derived/global reduction and intrinsic nonadjoint/global central conventions retain their separate proof obligations.


### 3.9. General principal Hamiltonian reduction

For the supplied pinned semisimple principal datum, the following four proofs use the fixed height splittings and positive polynomial gauge group of §1.1, and a specified perfect invariant symmetric form \(B\). They establish the actual classical reduction over every ordinary characteristic-zero coefficient algebra. The abstract normalizer and Laurent arguments also allow a height-zero summand when it is specified; §§3.9.2 and 3.9.4 use the proved semisimple condition \(V_0=0\). Existence of the root/group data and intrinsic/global oper descent retain their exact earlier premises.

#### 3.9.1. Principal Hamiltonian reduction for a fixed graded Lie datum

Let \(k\) be a characteristic-zero field and \(R\) an ordinary commutative \(k\)-algebra. Fix a finite-dimensional Lie algebra and the following data over \(k\):
\[
 \begin{gathered}
 \mathfrak g=\bigoplus_{a\in\mathbb Z}\mathfrak g_a,\qquad
 [\mathfrak g_a,\mathfrak g_b]\subset\mathfrak g_{a+b},\\
 e\in\mathfrak g_1,\quad f\in\mathfrak g_{-1},\quad
 r\in\mathfrak g_0,\quad h=2r,\qquad
 [r,x]=a x\quad(x\in\mathfrak g_a),\\
 [h,e]=2e,\qquad[h,f]=-2f,\qquad[e,f]=h,\\
 B:\mathfrak g\otimes_k\mathfrak g\longrightarrow k
 \quad\text{symmetric, invariant and perfect}.
 \end{gathered}
 \tag{GR.1}
\]
Here invariance means \(B([x,y],z)=B(x,[y,z])\), and perfectness means that \(B\) identifies \(\mathfrak g\) with its linear dual. All direct sums in the grading are finite. Put
\[
 \mathfrak n=\bigoplus_{a>0}\mathfrak g_a,\qquad
 \mathfrak b=\bigoplus_{a\geq0}\mathfrak g_a,\qquad
 V=\ker(\operatorname{ad}e).
 \tag{GR.2}
\]
These are fixed linear and Lie data. The construction below does not require \(k\) to be algebraically closed.

For completeness, the splittings used in the subsequent principal slice have the precise form
\[
 \mathfrak g_a=[f,\mathfrak g_{a+1}]\oplus V_a,\qquad
 \operatorname{ad}f:\mathfrak g_{a+1}\hookrightarrow\mathfrak g_a
 \quad(a\geq0).
 \tag{GR.3}
\]
The finite \(\mathfrak{sl}_2\) argument in (DS.A5)–(DS.A9) proves them under (GR.1). Each string has grades \(d,d-1,\ldots,-d\), where its highest \(h\)-weight is \(2d\). On this string, \(f\) maps each nonbottom vector nontrivially to the next one; the coefficient \(j(2d-j+1)\) obtained by applying \(e\) is a nonzero integer. At a nonnegative grade, every vector except a highest vector is consequently in the image of \(f\), and a vector of grade \(a+1>0\) cannot be at the bottom. The explicit string decomposition proved there gives (GR.3), with no further complete-reducibility input. These \(k\)-linear splittings remain splittings after tensoring with \(R\). A trivial string can give \(V_0\ne0\); the extra assertion \(V_0=0\) for the pinned adjoint semisimple example uses its separate simple-coroot argument.

**The pairing and the moment constraints.** Invariance gives
\[
 B([r,x],y)+B(x,[r,y])=0,\qquad
 (a+b)B(x,y)=0
 \quad(x\in\mathfrak g_a,\ y\in\mathfrak g_b).
 \tag{GR.4}
\]
If \(a+b\ne0\), this integer is invertible in \(k\), so the pairing is zero. For each \(a\), the induced map
\(\mathfrak g_a\to\mathfrak g_{-a}^{*}\) is injective: an element in its kernel pairs with no homogeneous summand and hence is zero by perfectness. The same argument with \(-a\) interchanged gives the opposite dimension inequality. Thus
\[
 B:\mathfrak g_a\otimes\mathfrak g_{-a}\longrightarrow k
 \ \text{is perfect for every }a,\qquad
 B|_{\mathfrak g_0}\ \text{is perfect},\qquad
 \mathfrak n^\perp=\mathfrak b.
 \tag{GR.5}
\]
For the last equality, the nonnegative grades pair trivially with the positive grades, while a nonzero negative component is detected by its perfect opposite-grade pairing. Each block has an inverse matrix over \(k\), so these statements, including the equality of orthogonal submodules, hold over every \(R\), including nonreduced \(R\).

Define \(\chi:\mathfrak n\to k\) by \(\chi(x)=B(f,x)\). It vanishes outside grade one. Since a bracket of two positive grades has grade at least two,
\[
 B(\mathfrak n,\mathfrak n)=0,\qquad
 \chi([\mathfrak n,\mathfrak n])=0.
 \tag{GR.6}
\]
The second equality says exactly that \(\chi\) is a Lie character; it uses neither a matrix realization nor a choice of positive-root coordinates.

**The affine bracket, constructed on all differential polynomials.** Let
\[
 \mathcal A_R=\operatorname{Sym}_R
       \left(\bigoplus_{p\geq0}\mathfrak g_R^{(p)}\right),\qquad
 J_x^{(p)}\in\mathfrak g_R^{(p)},\quad
 TJ_x^{(p)}=J_x^{(p+1)},\quad T|_R=0.
 \tag{GR.7}
\]
The labels \(J_x^{(p)}\) are linear in \(x\). For a basis \(e_i\), write \(u_i^{(p)}=J_{e_i}^{(p)}\), and prescribe the positive affine cocycle
\[
 H_{ij}(\lambda)=J_{[e_i,e_j]}+B(e_i,e_j)\lambda,\qquad
 \{J_x{}_\lambda J_y\}=J_{[x,y]}+B(x,y)\lambda.
 \tag{GR.8}
\]
“Positive” specifies the plus sign of this cocycle, rather than an order on \(k\). For arbitrary differential polynomials define
\[
 \boxed{\{F_\lambda G\}
  =\sum_{i,j,p,q}
       \frac{\partial G}{\partial u_j^{(q)}}
       (\lambda+T)^q H_{ij}(\lambda+T)
       (-\lambda-T)^p
       \frac{\partial F}{\partial u_i^{(p)}}.}
 \tag{GR.9}
\]
In this formula \(H_{ij}(\lambda+T)=J_{[e_i,e_j]}+B(e_i,e_j)(\lambda+T)\), and every displayed \(T\) acts on all factors to its right. The sum is finite, and contracts the two polynomial differentials with the bilinear map (GR.8); hence it is independent of the basis. Its values belong to \(\mathcal A_R[\lambda]\).

We give the extension proof, including Jacobi for this general Lie datum. If \(F_{i,p}=\partial F/\partial u_i^{(p)}\), ordinary differentiation yields
\[
 (TF)_{i,p}=T F_{i,p}+F_{i,p-1},\qquad F_{i,-1}=0.
 \tag{GR.10}
\]
In (GR.9) the second term is reindexed by \(p\mapsto p+1\); its factor \(-\lambda-T\), added to the first term's \(T\), leaves \(-\lambda\). In the second argument the extra \(\lambda+T\) combines with the derivative of the coefficient by the product rule. Thus
\[
 \{TF_\lambda G\}=-\lambda\{F_\lambda G\},\qquad
 \{F_\lambda TG\}=(\lambda+T)\{F_\lambda G\}.
 \tag{GR.11}
\]
Differentiating a product in the second argument proves the right Leibniz rule. For the first argument use, for every nonnegative integer \(q\),
\[
 (\lambda+T)^q(ab)=
   \sum_{v=0}^q\binom qv
          \bigl((\lambda+T)^{q-v}a\bigr)T^v b.
\]
Putting coefficients of each finite differential operator to its left and applying this identity to the derivative of a product proves
\[
 \begin{aligned}
 \{F_\lambda GH\}&=\{F_\lambda G\}H+G\{F_\lambda H\},\\
 \{FH_\lambda G\}&=\{F_{\lambda+T}G\}_{\to}H
                    +\{H_{\lambda+T}G\}_{\to}F.
 \end{aligned}
 \tag{GR.12}
\]
The arrow directs the newly inserted \(T\)'s to the factor on their right. These rules also prove uniqueness: expand monomials into jet factors, use the two product rules, and remove their derivatives by (GR.11). The resulting finite expansion is (GR.9).

Here is a finite kernel proof of the remaining identities. At independent spatial labels \(s,t\), take
\[
 K_{xy}(s,t)=J_{[x,y]}(t)\delta(s,t)
                +B(x,y)\partial_t\delta(s,t),\qquad
 \delta(s,t)=\sum_{m\in\mathbb Z}s^{-m-1}t^m.
 \tag{GR.13}
\]
The delta's residue against a Laurent polynomial in \(s\) evaluates that polynomial at \(t\). Its derivative rules follow by differentiation. We use only finite sums of derivatives supported on the diagonal: coefficients are differential-polynomial jets, and multiplication into the delta is defined by finite Taylor evaluation. In particular
\[
 a(s)\partial_t^q\delta(s,t)
   =\sum_{v=0}^q\binom qv
          (T^v a)(t)\partial_t^{q-v}\delta(s,t).
 \tag{GR.14}
\]
This follows by differentiating \(a(s)\delta(s,t)=a(t)\delta(s,t)\) \(q\) times.

For the nested brackets, two independent diagonal differences give the finite normal form
\[
 \sum_{p,q}a_{pq}(u)
       \frac{\partial_u^p\delta(s,u)}{p!}
       \frac{\partial_u^q\delta(t,u)}{q!}.
 \tag{GR.15}
\]
Each derivative acts on its indicated delta only. Successive Taylor evaluation gives existence for the products occurring here. Double residue against \((s-u)^p(t-u)^q\) extracts \(a_{pq}\), giving uniqueness: a derivative of a monomial at zero is nonzero precisely at its own degree. Thus these products can equally be defined as functionals on the finite Taylor jets of test polynomials along \(s=t=u\). Differentiation and the coefficient product rule respect that definition. No infinite convolution of two delta series is needed.

Extend (GR.13) to products at distinct labels by the ordinary biderivation rule, and to jets by differentiating at their labels. There are finitely many selected pairs of factors. Apply (GR.14) to all unselected factors and take the exponential residue
\(\operatorname{Res}_s e^{\lambda(s-t)}K(F(s),G(t))\).
A delta derivative contributes a power of \(\lambda\); differentiation at \(s\) contributes \(-\lambda\), while differentiation at \(t\) contributes \(\lambda+T\). Summing over the selected pair gives exactly (GR.9), with its indicated arrows.

The current kernel is antisymmetric: the Lie bracket is antisymmetric, \(B\) is symmetric, and \(\partial_s\delta(t,s)=-\partial_t\delta(s,t)\). Coefficient movement for the undifferentiated term uses (GR.14) with \(q=0\). Biderivation and differentiation preserve this property. Taking the same residue consequently proves
\[
 \{F_\lambda G\}=-\{G_{-\lambda-T}F\},
 \tag{GR.16}
\]
where the substituted \(T\)'s act on the coefficients. The shifts are the finite Taylor rule (GR.14).

Before diagonal normal ordering, the cyclic kernel Jacobiator is a derivation in each argument. To verify this, expand it when one argument is \(H_1H_2\). Terms in which the two brackets hit different factors cancel as
\[
 \begin{aligned}
 &K(F,H_1)K(G,H_2)+K(G,H_1)K(F,H_2)\\
 &\quad-K(G,H_1)K(F,H_2)-K(F,H_1)K(G,H_2)=0.
 \end{aligned}
\]
The remaining terms are the Jacobiator on each factor multiplied by the other. Antisymmetry makes the cyclic Jacobiator alternating, so the same proof applies in the other arguments. Differentiating an argument differentiates its Jacobiator. Induction on numbers of factors and derivatives therefore reduces vanishing to three undifferentiated currents.

For those currents the double exponential residue of the Jacobiator is
\[
 \begin{aligned}
 &J_{[x,[y,z]]}-J_{[y,[x,z]]}-J_{[[x,y],z]}\\
 &\quad+B(x,[y,z])\lambda
       -B(y,[x,z])\mu-B([x,y],z)(\lambda+\mu)=0.
 \end{aligned}
 \tag{GR.17}
\]
The first line is the Lie Jacobi identity. Invariance and antisymmetry give
\(B(x,[y,z])=B([x,y],z)\) and
\(B(y,[x,z])=-B([x,y],z)\), cancelling the second line. The parameter in the last term is \(\lambda+\mu\) because
\(e^{\lambda(s-u)+\mu(t-u)}
 =e^{\lambda(s-t)}e^{(\lambda+\mu)(t-u)}\)
on the term first supported at \(s=t\). Uniqueness of (GR.15) implies that the zero polynomial residue has every kernel coefficient zero. The factor and derivative induction just proved then gives, for all \(F,G,H\),
\[
 \boxed{\{F_\lambda\{G_\mu H\}\}
        -\{G_\mu\{F_\lambda H\}\}
       =\{\{F_\lambda G\}_{\lambda+\mu}H\}.}
 \tag{GR.18}
\]
Equations (GR.11), (GR.12), (GR.16) and (GR.18) are the PVA identities. This establishes their complete extension using the Lie axiom and invariant \(B\); no representation theorem is involved. The unit has zero bracket. Every operation is a finite polynomial expression over \(k\), so the identities hold over all ordinary \(R\) and are natural under every coefficient map.

**Coisotropy and the actual PVA quotient.** Put
\[
 c_x=J_x-\chi(x)\quad(x\in\mathfrak n),\qquad
 I_R=(T^p c_x:x\in\mathfrak n,\ p\geq0)\subset\mathcal A_R.
 \tag{GR.19}
\]
The character and isotropy calculations (GR.6) give
\(\{c_x{}_\lambda c_y\}=c_{[x,y]}\).
Sesquilinearity proves the corresponding containment for derivatives. Applying both product rules to multiples of those derivatives leaves a constraint or a derivative of a constraint in every term. Hence
\[
 \{I_R{}_\lambda I_R\}\subset I_R[\lambda].
 \tag{GR.20}
\]
This is coisotropy. Define
\[
 U_R=\{a\in\mathcal A_R:
         \{J_x{}_\lambda a\}\in I_R[\lambda]
                         \text{ for every }x\in\mathfrak n\}.
 \tag{GR.21}
\]
Here \(J_x\) can be replaced by \(c_x\), since constants have zero bracket. Coisotropy gives \(I_R\subset U_R\), and right Leibniz and second sesquilinearity prove that \(U_R\) is closed under products and \(T\).

If \(a\in U_R\), skew symmetry first gives
\(\{a_\lambda c_x\}\in I_R[\lambda]\): the shifted coefficients stay in the differential ideal. Second sesquilinearity handles every \(T^p c_x\). Right Leibniz handles its multiple by an arbitrary polynomial \(d\), since the additional term \(\{a_\lambda d\}T^p c_x\) belongs to the ideal. Skew symmetry gives the reverse test. Thus
\[
 a\in U_R\quad\Longleftrightarrow\quad
 \{a_\lambda I_R\}\subset I_R[\lambda]
 \quad\Longleftrightarrow\quad
 \{I_R{}_\lambda a\}\subset I_R[\lambda].
 \tag{GR.22}
\]
For the converses, test the constraint generators in \(I_R\).

For \(a,b\in U_R\), Jacobi gives
\[
 \{J_x{}_\mu\{a_\lambda b\}\}
  =\{\{J_x{}_\mu a\}_{\mu+\lambda}b\}
       +\{a_\lambda\{J_x{}_\mu b\}\}
   \in I_R[\lambda,\mu].
 \tag{GR.23}
\]
The two containments follow coefficientwise from (GR.22), including the parameter substitution. Hence every coefficient of \(\{a_\lambda b\}\) lies in \(U_R\). We have proved that \(U_R\) is a differential PVA subalgebra and \(I_R\) is a differential PVA ideal in it. Therefore
\[
 \boxed{\mathcal W_R=U_R/I_R}
 \tag{GR.24}
\]
is a PVA. Changing either representative by an element of \(I_R\) changes every bracket coefficient by an element of \(I_R\), by (GR.22). This proves lift independence. The unrestricted quotient \(\mathcal Q_R=\mathcal A_R/I_R\) is used as a differential algebra with a constraint action.

**The affine constraint space and all current jets.** By perfectness of \(B\), the universal order-zero coordinate is the unique \(A\in\mathfrak g\otimes_k\mathcal A_R\) with \(J_y=B(A,y)\). The equations \(c_x=0\), for \(x\in\mathfrak n\), say
\(B(A-f,\mathfrak n)=0\), hence \(A\in f+\mathfrak b\), by (GR.5). In opposite-grade dual bases they eliminate exactly the negative-grade coordinates of \(A\); at order zero those coordinates are those of \(f\), and their positive jets are zero. All other coordinates remain polynomially free. This gives, over every \(R\),
\[
 \boxed{\mathcal Q_R=
    \mathcal O_{\mathrm{diff}}(f+\mathfrak b)_R
    =\operatorname{Sym}_R
       \left(\bigoplus_{p\geq0}\mathfrak b_R^{*\, (p)}\right).}
 \tag{GR.25}
\]
The displayed symmetric algebra refers to the coordinate \(A-f\). The inverse matrices of (GR.5) prove the elimination over nonreduced rings as well. An ordinary coefficient point specifies every Taylor coefficient of
\(A(t)=f+\sum_{p\geq0}a^{(p)}t^p/p!\), with \(a^{(p)}\in\mathfrak b_R\).

Let \(\pi:\mathcal A_R\to\mathcal Q_R\). Coisotropy makes the following action independent of the lift:
\[
 \rho_x(\lambda)\pi(a)=\pi\{J_x{}_\lambda a\}
   =\sum_{j\geq0}\frac{\lambda^j}{j!}D_{x,j}\pi(a)
 \quad(x\in\mathfrak n).
 \tag{GR.26}
\]
Each \(D_{x,j}\) is an \(R\)-linear derivation. Coefficient extraction from second sesquilinearity gives the exact formula
\[
 \boxed{D_{x,j}\pi(J_y^{(p)})=
  \begin{cases}
    \displaystyle\frac{p!}{(p-j)!}
                  \pi(J_{[x,y]}^{(p-j)}),&0\leq j\leq p,\\
    (p+1)!B(x,y),&j=p+1,\\
    0,&j>p+1.
  \end{cases}}
 \tag{GR.27}
\]
Indeed the polynomial to expand is
\((\lambda+T)^p(J_{[x,y]}+B(x,y)\lambda)\), and \(T\) kills its constant pairing. Jacobi and \(B(\mathfrak n,\mathfrak n)=0\) imply
\(\rho_x(\lambda)\rho_y(\mu)-\rho_y(\mu)\rho_x(\lambda)
 =\rho_{[x,y]}(\lambda+\mu)\).
Comparing divided-power coefficients proves
\[
 [D_{x,p},D_{y,q}]=D_{[x,y],p+q},\qquad
 D_{x,j}T=TD_{x,j}+jD_{x,j-1},
 \tag{GR.28}
\]
where \(D_{x,-1}=0\). Thus \(x t^j\mapsto D_{x,j}\) is precisely the current-jet Lie action. The second identity shows that its common kernel is \(T\)-stable.

Define \(\mathcal Q_R^{\mathfrak n[[t]]}\) as the common kernel of all these derivations. Any lift of an invariant class satisfies (GR.21), because the polynomial coefficients in (GR.26) vanish. A normalizer representative conversely maps to an invariant class, and the kernel of that map is exactly \(I_R\). Consequently
\[
 \boxed{\mathcal W_R
       \simeq\mathcal Q_R^{\mathfrak n[[t]]}.}
 \tag{GR.29}
\]
This is a canonical differential-algebra identification, without a chosen invariant lift. Its right side carries the PVA bracket transported from (GR.24).

**Principal weights, formal gauge flows and the sign.** For homogeneous \(y\in\mathfrak g_a\), give \(J_y^{(p)}\) principal weight \(1-a+p\), and give \(T,\lambda\) weight one. Formula (GR.8) has weight equal to the sum of its inputs minus one: its current term has weight \(1-a-b\), and a nonzero pairing term requires \(a+b=0\). The master formula preserves this rule for all homogeneous polynomials. The constraints are homogeneous, since a nonzero \(\chi(y)\) occurs only at grade one and weight zero.

On \(\mathcal Q_R\), a coordinate dual to \(\mathfrak g_a\subset\mathfrak b\) has weight \(1+a\), and its \(p\)-th jet has weight \(1+a+p\). All these weights are positive. Each weight piece is the extension of a finite-dimensional \(k\)-space: only finitely many jet generators have weight at most \(d\), and each exponent in a monomial of weight \(d\) is bounded. If \(x\in\mathfrak g_a\subset\mathfrak n\), (GR.27) proves
\[
 D_{x,j}:(\mathcal Q_R)_d\longrightarrow
             (\mathcal Q_R)_{d-a-j},\qquad a>0.
 \tag{GR.30}
\]
The scalar term obeys the same rule: it can occur only when \(y\) has grade \(-a\) and \(j=p+1\), so the input weight is \(a+j\). Thus every polynomial has a common high-jet cutoff, and each such derivation is locally nilpotent. The reduced bracket retains principal weight minus one.

For an external variable test coefficient \(\phi\), adjoin its jets as Poisson-central differential variables. The construction (GR.9) applies with their zero generator brackets. Left Leibniz at \(\lambda=0\) gives, on the constraint quotient,
\[
 \delta_{\int\phi J_x}a
   :=\{\phi J_x{}_\lambda a\}\big|_{\lambda=0}
    =\sum_{j\geq0}\frac{\phi^{(j)}}{j!}D_{x,j}a.
 \tag{GR.31}
\]
The sum is finite. First sesquilinearity makes the local functional independent of adding a \(T\)-derivative; right Leibniz makes its flow a derivation. This uses the algebraic derivation \(T\) on the test algebra, without postulating an operator on another module. Apply (GR.31) to \(J_y=B(A,y)\), and allow \(x\) to have those variable coefficients. Invariance and perfectness give
\[
 \delta_x J_y=B(A,[x,y])+B(x',y)
            =B([A,x]+x',y),\qquad
 \boxed{\delta_xA=[A,x]+x'.}
 \tag{GR.32}
\]
Both \([f,\mathfrak n]\subset\mathfrak b\) and
\([\mathfrak b,\mathfrak n]\subset\mathfrak n\) follow from grades, so this flow preserves \(f+\mathfrak b\).

Its full formal-jet meaning can be checked without a group representation. Let
\(X(t)=\sum_{j\geq0}x_jt^j\in\mathfrak n_R[[t]]\) and
\(D_X=\sum_jD_{x_j,j}\); the latter sum is finite on any bounded-weight polynomial, by (GR.30). Summing (GR.27) against \(t^p/p!\) gives
\[
 D_XA(t)=[A(t),X(t)]+X'(t).
 \tag{GR.33}
\]
Here \(A^{(0)}=f+a^{(0)}\) and \(A^{(p)}=a^{(p)}\) for \(p>0\) denote the full Taylor coefficients. At Taylor order \(p\), the commutator sum is
\(\sum_{j\leq p}p!/(p-j)!\,[A^{(p-j)},x_j]\);
the derivative term is \((p+1)!x_{p+1}\).
Thus all current jets, including nilpotent coefficient families, have the claimed action.

There is also an exact finite exponential formula. In the semidirect Lie algebra with \([\partial,X]=X'\), repeated \(\operatorname{ad}X\) raises grade on \(\mathfrak g\); on \(\partial\) its first bracket lies in the positive grades. Hence sufficiently high powers vanish uniformly. The Lie Jacobi identity says that \(L=\operatorname{ad}X\) is a derivation; induction gives
\(L^q[u,v]=\sum_{i=0}^q\binom qi[L^iu,L^{q-i}v]\).
The finite exponential therefore preserves the bracket, and its inverse is the exponential with the opposite sign. The inverse adjoint gauge expression is the finite polynomial
\[
 A^{\exp X}
  =e^{-\operatorname{ad}X}A
     +\sum_{q\geq0}
          \frac{(-1)^q}{(q+1)!}
                   (\operatorname{ad}X)^qX'.
 \tag{GR.34}
\]
It is the \(\mathfrak g\)-part of
\(e^{-\operatorname{ad}X}(\partial+A)\). For a scalar parameter \(s\), its version with \(sX\) satisfies
\(\partial_s A^{\exp(sX)}
 =[A^{\exp(sX)},X]+X'\)
and has initial value \(A\). The formula follows as well by solving this equation coefficientwise in \(s\); all coefficients divide only by positive integers. On functions, \(\exp(sD_X)\) is finite by weight lowering, respects products by the binomial formula for powers of a derivation, and solves the same equation on every coordinate jet. The two expressions agree by the same coefficient recursion. This proves finite preservation of \(f+\mathfrak b\).

Under an actual group realization, (GR.34) is
\(g^{-1}Ag+g^{-1}g'\) for \(g=\exp X\), equivalently
\(g^{-1}(\partial+A)g=\partial+A^{g}\).
The forward conjugation \(g(\partial+A)g^{-1}\) has the opposite infinitesimal sign. The fixed pinned group construction of §1.1.1 gives this realization under its stated root and group prerequisites. Formula (GR.34) itself is already defined for the fixed Lie datum.

Moreover, the common kernel in (GR.29) is exactly the algebra fixed by every such exponential gauge flow, functorially over all ordinary coefficient extensions: annihilation by all current jets implies annihilation by \(D_X\) and hence invariance under its finite exponential. Conversely use \(X=\eta x t^j\) over \(R[\eta]/(\eta^2)\); invariance says \(\eta D_{x,j}a=0\), which forces \(D_{x,j}a=0\) because \(1,\eta\) is an \(R\)-basis. This tests all jets over nonreduced rings. An identification with a separately specified algebraic group functor additionally uses that functor's exponential description.

**Ordinary base change and the reduction diagram.** In a fixed weight \(d\), only basis elements \(x\in\mathfrak g_a\), \(a>0\), and integers \(j\geq0\) with \(a+j\leq d\) can act nontrivially. Therefore \((\mathcal W_k)_d\) is the kernel of the single finite linear map
\[
 (\mathcal Q_k)_d\longrightarrow
   \bigoplus_{\substack{x\text{ in a homogeneous basis of }\mathfrak n\\
                        0\leq j\leq d-\operatorname{grade}(x)}}
      (\mathcal Q_k)_{d-\operatorname{grade}(x)-j},
 \qquad a\longmapsto(D_{x,j}a)_{x,j}.
 \tag{GR.35}
\]
All its entries belong to \(k\). Tensoring over a field is exact: choose bases of the kernel and a complement, on which the map is injective, and extend those bases. This proves that its kernel over \(R\) is \(R\otimes_k(\mathcal W_k)_d\). Summing the weight pieces gives
\[
 \boxed{\mathcal W_R\simeq R\otimes_k\mathcal W_k,\qquad
        R'\otimes_R\mathcal W_R\simeq\mathcal W_{R'}}
 \tag{GR.36}
\]
for every ordinary map \(R\to R'\). The product, \(T\) and bracket coefficients agree under these identifications because their finite formulas were all defined over \(k\). This is a proof for this fixed field model; it does not assume that kernels of arbitrary matrices over \(R\) survive nonflat base change.

The construction is summarized by the following diagram:
\[
 \begin{array}{ccc}
 U_R&\hookrightarrow&\mathcal A_R\\
 \big\downarrow{\scriptstyle /I_R}&&
       \big\downarrow{\scriptstyle /I_R}\\
 \mathcal W_R&\hookrightarrow&
       \mathcal Q_R=\mathcal O_{\mathrm{diff}}(f+\mathfrak b)_R .
 \end{array}
 \tag{GR.37}
\]
*The upper inclusion is the coisotropic normalizer (GR.21). The left quotient carries the reduced PVA by (GR.22)–(GR.24). Its lower image is exactly the common current-jet kernel (GR.29), and the right quotient eliminates the moment coordinates by the perfect opposite-grade pairings (GR.25). Positive coordinate weights \(1+a+p\) give the finite kernel test (GR.35); the inverse gauge flow is \([A,x]+x'\) by (GR.32)–(GR.34).*

An actual PVA homomorphism between two such constructions descends to their reduced PVAs if it sends the constraint ideal into the target constraint ideal and sends the source normalizer into the target normalizer. Indeed those two containments respectively prove representative independence and membership in the target, and applying the homomorphism to each bracket coefficient proves preservation of the reduced bracket. Thus the normalizer test, as well as the moment relations, is part of any claimed reduced comparison.

For the pinned adjoint semisimple application, the root decomposition, pinning brackets, simple-coroot basis, root subgroup coordinates and group realization listed in §1.1.1 remain explicit structural premises. The present argument proves the classical Hamiltonian reduction once (GR.1) is fixed; it supplies no proof of those group prerequisites or of the existence of the chosen perfect invariant form for an unspecified Lie algebra. The form in (GR.8) is the chosen classical \(B\), with its positive cocycle sign; a quantum critical form is a separate datum. The classification of slice generators, Laurent topology and coordinate descent require their further arguments. No identification with a quantum center or an oper Poisson structure follows from this reduction alone.

#### 3.9.2. General principal gauge, polynomial invariants and weighted Laurent charts

Fix a characteristic-zero field \(k\) and the finite principal datum described in [Opers, critical level and the Beilinson–Drinfeld construction](opers-critical-level-and-the-beilinson-drinfeld-construction.md), §1.1.1–§1.1.4, equations (DS.A1)–(DS.A20). The following statement is conditional on that **specified datum**, rather than a new classification or existence theorem for arbitrary forms of a semisimple group. All coefficient algebras below are ordinary commutative algebras and may be nonreduced.

Write \(r=h/2\), \(F=\operatorname{ad}f\), \(E=\operatorname{ad}e\). The supplied finite grading and principal triple satisfy
\[
\begin{aligned}
\mathfrak g&=\bigoplus_{j=-q}^{q}\mathfrak g_j,
&[r,x]&=jx\quad(x\in\mathfrak g_j),\\
f&\in\mathfrak g_{-1},&e&\in\mathfrak g_1,
&[e,f]&=2r,\\
\mathfrak n&=\bigoplus_{a\geq1}\mathfrak g_a,
&\mathfrak b&=\bigoplus_{j\geq0}\mathfrak g_j.
\end{aligned}
\tag{GG.1}
\]
We take \(q\geq1\); for the zero datum every coefficient and gauge space is a point. The actual finite string proof (DS.A5)–(DS.A10), including its fixed projections and inverses, gives
\[
V=\ker E=\bigoplus_{d\geq1}V_d,\qquad
\mathfrak g_j=F(\mathfrak g_{j+1})\oplus V_j,\qquad
F:\mathfrak g_{j+1}\hookrightarrow\mathfrak g_j\quad(j\geq0).
\tag{GG.2}
\]
No highest line has height zero. Choose bases of the finite spaces and retain repeated heights. The split unipotent group \(N\), its finite exponential/logarithm, BCH and gauge formulas are the actual constructions (DS.A12)–(DS.A16), at their stated root/group and faithful-representation premises. They apply after tensoring with every ordinary coefficient algebra; no reduced-point test is used below.

**The explicit polynomial inverse.** In any differential \(k\)-algebra \((C,T)\), put \(A=f+b\), \(b\in\mathfrak b\otimes C\), with gauge convention
\[
g\cdot A=\operatorname{Ad}(g)A-(Tg)g^{-1}.
\tag{GG.3}
\]
Define the fixed linear maps \(P_j:\mathfrak g_j\to V_j\) and \(L_j:\mathfrak g_j\to\mathfrak g_{j+1}\) by
\[
z=F L_j(z)+P_j(z),\qquad L_q=0.
\tag{GG.4}
\]
Starting with \(A^{[0]}=A\), at stage \(m=0,\ldots,q-1\) take
\[
x_{m+1}=L_m\bigl(A^{[m]}_m\bigr),\qquad
A^{[m+1]}=\exp(x_{m+1})\cdot A^{[m]},\qquad
Q(A)=\exp(x_q)\cdots\exp(x_1).
\tag{GG.5}
\]
Here \(A^{[m]}_m\) is the height-\(m\) coefficient, with \(f\) kept separately. The finite formula used at each step is
\[
\exp(x)\cdot A
=\sum_{p\geq0}\frac{(\operatorname{ad}x)^pA}{p!}
-\sum_{p\geq0}\frac{(\operatorname{ad}x)^p(Tx)}{(p+1)!}.
\tag{GG.6}
\]
For \(x=x_{m+1}\), its only change at height \(m\) is \([x,f]=-F(x)\). Its derivative has height \(m+1\); brackets with \(b_j\), \(j\geq0\), have height at least \(m+1\); the second bracket with \(f\) has height \(2m+1\geq m+1\). Thus earlier slice coefficients remain fixed and the current height becomes \(P_m(A^{[m]}_m)\). At height \(q\) the whole coefficient is already in \(V_q\). The resulting
\[
Q(A)\cdot A=f+s(A),\qquad s(A)\in V\otimes C
\tag{GG.7}
\]
is a finite differential polynomial calculation using exactly the specified maps \(L_m,P_m\).

For completeness, uniqueness is a linear comparison, including over a nonreduced \(C\). If \(g\cdot(f+s)=f+\widetilde s\) and the lowest nonzero height in \(\log g\) is \(a\), the height-\((a-1)\) difference is \(-F((\log g)_a)\). Derivatives and every other commutator have larger height. That difference is also in \(V_{a-1}\). The direct splitting and injectivity in (GG.2), which remain direct after ordinary base change, force \((\log g)_a=0\). Repeating through the finite height list gives \(g=1\) and \(s=\widetilde s\). In particular slice stabilizers are trivial.

Consequently, for every differential algebra, the two maps
\[
\begin{aligned}
\Phi(u,s)&=u\cdot(f+s),\qquad u\in N(C),\quad s\in V\otimes C,\\
\Psi(A)&=\bigl(Q(A)^{-1},s(A)\bigr)
\end{aligned}
\quad\text{satisfy}\quad
\Psi\Phi=\operatorname{id},\qquad \Phi\Psi=\operatorname{id}.
\tag{GG.8}
\]
Indeed \(u^{-1}\) normalizes \(\Phi(u,s)\), so uniqueness identifies it with \(Q(\Phi(u,s))\). Conversely (GG.7) reconstructs \(A\). This proves the inverse identities themselves, not only existence of one point on each orbit. It also proves
\[
Q(g\cdot A)=Q(A)g^{-1},\qquad s(g\cdot A)=s(A),\qquad
\Psi(g\cdot A)=\bigl(gu,s\bigr)
\quad\text{when }\Psi(A)=(u,s).
\tag{GG.9}
\]

**Weights and a uniform differential-order bound.** Use the finite height coordinates
\(u=\exp(y_q)\cdots\exp(y_1)\) of (DS.A16). Assign principal weights
\[
\operatorname{wt}(b_{j,\alpha})=j+1,\qquad
\operatorname{wt}(y_{a,\beta})=a,\qquad
\operatorname{wt}(s_{d,\gamma})=d+1,\qquad
\operatorname{wt}(T)=1.
\tag{GG.10}
\]
Group multiplication and inversion are polynomial and homogeneous of weight \(a\) in each output height-\(a\) coordinate: BCH and the finite height extraction are equivariant for the grading scaling, and every bracket adds the heights. This is also checked directly by the finite BCH word expansion.

In (GG.6), a commutator word with \(f\) and gauge heights \(a_1,\ldots,a_p\) has output height \(a_1+\cdots+a_p-1\) and coefficient weight \(a_1+\cdots+a_p\). A word with \(b_j\) has output height \(a_1+\cdots+a_p+j\) and weight \(a_1+\cdots+a_p+j+1\). A logarithmic-derivative word has output height \(a_1+\cdots+a_p\) and weight one larger. Thus each output \(b_j\) has weight \(j+1\). Inducting in (GG.5), \(x_a\) has weight \(a\); applying the homogeneous group-coordinate formulas proves that every coordinate of \(Q(A)\) or \(Q(A)^{-1}\) at height \(a\) has weight \(a\). Every \(s_d(A)\) has weight \(d+1\).

These are **finite** differential polynomials because the algorithm has \(q\) stages and every exponential word is finite. All input coordinate weights are positive. A nonconstant monomial of output weight \(w\) has the form \(\prod_\nu T^{e_\nu}z_\nu\), where
\[
\sum_\nu\bigl(\operatorname{wt}(z_\nu)+e_\nu\bigr)=w.
\tag{GG.11}
\]
In particular each \(e_\nu\leq w-1\). No positive-weight output can have a constant monomial. It follows from the actual finite algorithm that
\[
\begin{gathered}
\begin{array}{c|c|c}
\text{output}&\text{weight}&\text{derivative order in the original }b\\ \hline
(Q(A)^{\pm1})_a&a&\leq a-1\\
s_d(A)&d+1&\leq d
\end{array}\\[4pt]
\operatorname{ord}\Phi_j\leq1\text{ in }y,\qquad
\operatorname{ord}\Phi_j=0\text{ in }s.
\end{gathered}
\tag{GG.12}
\]
The last bound follows directly from (GG.3): conjugation has no derivatives, and \((Tu)u^{-1}\) differentiates each finite group-coordinate monomial only once. Thus \(q\) is a uniform bound for the inverse differential order; it is not an unspecified bound hidden in an orbit theorem.

Let \(R\) be any ordinary \(k\)-algebra, with \(T\) zero on \(R\). Introduce free differential polynomial rings on the chosen coefficient bases:
\[
\begin{aligned}
\mathcal X_R&=R[b_{j,\alpha}^{(r)}:0\leq j\leq q,\ r\geq0],\\
\mathcal Y_R&=R[y_{a,\beta}^{(r)}:1\leq a\leq q,\ r\geq0],\\
\mathcal S_R&=R[s_{d,\gamma}^{(r)}:1\leq d\leq q,\ r\geq0],
\qquad Tz^{(r)}=z^{(r+1)}.
\end{aligned}
\tag{GG.13}
\]
Omit variables belonging to a zero space. The mutually inverse polynomial maps (GG.8) induce
\[
\mathcal X_R\ \simeq\ \mathcal Y_R\otimes_R\mathcal S_R
\tag{GG.14}
\]
as differential \(R\)-algebras. In particular the slice coordinates and their translates are algebraically independent, and (GG.14) remains an isomorphism after every ordinary base change, without a flatness hypothesis. It is the tensor extension of explicit inverse identities over \(k\).

**Regular jets, the actual coaction and currents.** A differential coordinate \(z^{(r)}\) corresponds to \(r!\) times the coefficient of \(t^r\) in \(z(t)\). Factorials are units. Therefore \(\mathcal X_R\), \(\mathcal Y_R\) and \(\mathcal S_R\) are exactly the coordinate rings of the coefficient functors for \(f+\mathfrak b(R[[t]])\), \(N(R[[t]])\) and \(V\otimes R[[t]]\). We do not replace \(R[[t]]\) by \(R\otimes_k k[[t]]\).

For outputs through coefficient \(M\), (GG.12) gives finite bounds:
\[
\begin{array}{c|c}
\text{regular-jet output through }M&\text{input coefficients needed}\\ \hline
Q(A)^{\pm1}&b\text{ through }M+q-1\\
s(A)&b\text{ through }M+q\\
\Phi(u,s)&y\text{ through }M+1,\quad s\text{ through }M
\end{array}
\tag{GG.15}
\]
All lower bounds here are zero. These are cofinal finite-jet bounds, not a claim of an isomorphism between equal-order truncated jet spaces. In particular the gauge action defines a genuine coaction on the countable polynomial ring: each coordinate has a finite polynomial image in the ordinary tensor product of the group-coordinate and connection-coordinate rings.

Under (GG.14), this coaction is left multiplication on \(u\) and the identity on \(s\). Its invariant ring is precisely
\[
\mathcal X_R^{\,N[[t]]}=\mathcal S_R.
\tag{GG.16}
\]
Here invariance means the universal coaction identity, including all ordinary extensions of \(R\). To prove exhaustion, write an invariant polynomial as \(F(u,s)\). The identity \(F(gu,s)=F(u,s)\) is an identity in the group and chart coordinate rings. Substitute the polynomial inverse coordinate \(g=u^{-1}\); it gives \(F(u,s)=F(1,s)\). Conversely every \(F(s)\) is invariant by (GG.9). This argument works with nilpotents and uses neither density nor passage to field-valued points.

The current sign is determined by differentiating the **opposite** gauge \(\exp(-c x(t))\):
\[
\delta_x A=[A,x]+x',\qquad
\left.\frac{d}{dc}\right|_{c=0}\bigl(\exp(-c x)\cdot A\bigr)=\delta_x A.
\tag{GG.17}
\]
For a fixed homogeneous basis vector \(x\in\mathfrak n\) and a scalar series \(\phi\), the gauge is explicitly
\[
\exp(-c\phi x)\cdot A
=\sum_{p\geq0}\frac{(-c\phi)^p(\operatorname{ad}x)^pA}{p!}
+c\phi'x.
\tag{GG.18}
\]
Indeed \([\phi x,(\phi x)']=0\), so the logarithmic derivative has just its first term. The adjoint sum is finite by positive-height nilpotence. Each pullback of a polynomial in finitely many Taylor coefficients is therefore polynomial in \(c\). Its additive flow law, proved by multiplying \(\exp(-c\phi x)\), gives \(dF_c/dc=(\delta_{\phi x}F)_c\). Polynomial coefficient comparison then gives \(F_c=\sum c^r\delta_{\phi x}^rF/r!\); finiteness proves local nilpotence. Thus \(\delta_{\phi x}F=0\) implies actual invariance under this universal one-parameter gauge, by a proved polynomial identity.

If \(F\) uses connection coefficients only through \(M\), its first variation uses \(\phi\) only through \(M+1\). Consequently annihilation by all \(\delta_{t^r x}\), \(r\geq0\), implies annihilation by \(\delta_{\phi x}\) for an arbitrary formal scalar series, over the universal coefficient algebra as well. Repeated variations still use connection coefficients through \(M\), so no additional infinite sum is introduced.

These one-parameter gauges generate the full ordinary functor \(N(R[[t]])\). Here is the finite proof. For a group element whose logarithm starts in height \(a\), write that component as \(\sum_\beta\phi_\beta x_{a,\beta}\). The product \(E_a=\prod_\beta\exp(\phi_\beta x_{a,\beta})\) has the same height-\(a\) logarithm; all its BCH corrections have height at least \(2a\). Hence multiplying by \(E_a^{-1}\) removes height \(a\) and leaves only larger heights. Repeat for \(a=1,\ldots,q\). The number of operations is bounded by the finite homogeneous basis list, and the coefficients extracted are polynomial. This proves group generation on arbitrary ordinary rings, rather than only on geometric points. It follows that
\[
\mathcal X_R^{\,\mathfrak n[t]}
:=\bigcap_{x\in\mathfrak n,\ r\geq0}\ker\delta_{t^r x}
=\mathcal X_R^{\,N[[t]]}
=R[s_{d,\gamma}^{(r)}:r\geq0].
\tag{GG.19}
\]
The converse differentiates universal invariance at the identity over the ordinary dual-number algebra. This also explains why no conclusion for the full Laurent gauge group is obtained from positive currents alone.

**The common-form current normalizer.** To compare with the affine reduction, fix the same nondegenerate invariant symmetric form \(B\) used there, and use the positive current convention
\[
J_x(A)=B(x,A),\qquad
\{J_x{}_\lambda J_y\}=J_{[x,y]}+B(x,y)\lambda.
\tag{GG.20}
\]
Invariance under \(r\) gives \((i+j)B(\mathfrak g_i,\mathfrak g_j)=0\); characteristic zero therefore makes different opposite grades orthogonal. Nondegeneracy makes the opposite-grade pairings perfect, so \(\mathfrak n^\perp=\mathfrak b\). Thus the differential ideal
\[
I=(T^r(J_x-\chi(x)):x\in\mathfrak n,\ r\geq0),\qquad
\chi(x)=B(f,x)
\tag{GG.21}
\]
in the free affine differential polynomial algebra has ordinary quotient exactly \(\mathcal X_R\). A basis adapted to \(\mathfrak n\), and the perfect pairing just proved, identifies the ideal with independent affine linear coordinate constraints and their jets; no dimension-only assertion is needed.

The function \(\chi\) is a Lie character: \([\mathfrak n,\mathfrak n]\) has heights at least two, whereas \(f\) has height minus one. Also \(B(\mathfrak n,\mathfrak n)=0\). Thus the brackets of constraint generators are in \(I[\lambda]\). Invariance of \(B\) gives
\[
\{J_x{}_\lambda J_y\}\bmod I
=B(y,[A,x])+B(x,y)\lambda,
\tag{GG.22}
\]
which is exactly the current action (GG.17), with no rescaling or sign change of \(B\).

More precisely, if \(\{J_x{}_\lambda F\}\bmod I=\sum_{p\geq0}c_p\lambda^p\), then on the Taylor-coordinate ring
\[
\delta_{t^p x}F=p!\,c_p\qquad(p\geq0).
\tag{GG.23}
\]
On a generator \(T^rJ_y\), the PVA formula is \((\lambda+T)^r\bigl(B(y,[A,x])+B(x,y)\lambda\bigr)\). The coefficient of \(\lambda^p\), multiplied by \(p!\), is the derivative at zero of \([A(t),t^p x]+(t^p x)'\), using \(T^rJ_y\leftrightarrow r!B(y,A_r)\). This proves the formula for every generator, including the derivative term when \(p=r+1\). Both operations obey the ordinary product rule on \(F\), so the formula holds for every differential polynomial. Each polynomial has only finitely many such coefficients.

Define the constraint normalizer by
\[
\mathcal N(I)=\{F:\{J_x{}_\lambda F\}\in I[\lambda]\text{ for every }x\in\mathfrak n\}.
\qquad
\mathcal N(I)/I\ \simeq\ \mathcal X_R^{\,\mathfrak n[t]}
=\mathcal S_R.
\tag{GG.24}
\]
The left condition descends to the quotient because the constraint brackets lie in \(I[\lambda]\); it is precisely the vanishing of (GG.23). Every invariant class has a polynomial lift, and every such lift lies in the normalizer. The product rule and sesquilinearity make this a differential subalgebra. The ideal \(I\) is contained in it. If the normalizer is instead defined with every element of \(I\), the same condition is obtained: derivative constraints follow by sesquilinearity, and a product by an arbitrary polynomial contributes either a constrained bracket or a factor in \(I\), by the left Leibniz rule and its shifted derivatives. This is the exact **commutative differential-algebra** comparison at the common form (GG.20). The Poisson-normalizer theorem and reduced bracket are separate assertions of §§3.9.1 and 3.9.3; gauge uniqueness is not used to certify a Poisson property. There is also no quantum-center identification in (GG.24).

**Exact weighted Laurent stages.** For \(N\geq1\), define functors on ordinary \(R\) using the chosen homogeneous bases and height coordinates:
\[
\begin{aligned}
\mathcal X_N(R)&=f+\bigoplus_{j=0}^{q}t^{-(j+1)N}\mathfrak g_j\otimes R[[t]],\\
\mathcal G_N(R)&=\{u=\exp(y_q)\cdots\exp(y_1):
 y_a\in t^{-aN}\mathfrak g_a\otimes R[[t]]\},\\
\mathcal V_N(R)&=\bigoplus_{d=1}^{q}t^{-(d+1)N}V_d\otimes R[[t]].
\end{aligned}
\tag{GG.25}
\]
The finite tensor notation means coefficients in a chosen finite-dimensional space; the series ring itself is the completed coefficient ring. Group multiplication and inversion of the \(y\)-coordinates are homogeneous polynomials of weight \(a\), so their monomials have pole order at most \(aN\). This proves that \(\mathcal G_N\) is a group functor, including nonreduced coefficients. The finite homogeneous-basis generation proof above stays in \(\mathcal G_N\): a height-\(a\) parameter has lower bound \(-aN\), and subsequent BCH height-\(b\) corrections have lower bound \(-bN\).

A derivative of order \(e\) increases a pole bound by at most \(e\). For a differential monomial (GG.11), the pole order is therefore at most
\[
\sum_\nu\operatorname{wt}(z_\nu)N+\sum_\nu e_\nu
=(w-e)N+e\leq wN,\qquad e=\sum_\nu e_\nu,
\tag{GG.26}
\]
since \(N\geq1\). This proves that the actual gauge action preserves \(\mathcal X_N\), that the normalizing coordinates lie in \(\mathcal G_N\), and that \(s_d\) lies in its exact assigned scalar bound. Both inverse maps in (GG.8) preserve the stage, giving an equivariant isomorphism
\[
\mathcal X_N\ \simeq\ \mathcal G_N\times\mathcal V_N,
\qquad A\longmapsto\bigl(Q(A)^{-1},s(A)\bigr),
\qquad g:(u,s)\longmapsto(gu,s).
\tag{GG.27}
\]
These are prescribed stable bounds, not a claim that each individual coefficient necessarily attains its maximal pole order.

The stage maps are ordinary polynomial maps on coefficient rings. Indeed a monomial with input weights \(w_\nu\), derivative orders \(e_\nu\), total weight \(w\), and total derivative order \(e\), contributes to output coefficient \(r\) only when
\[
m_\nu\geq-w_\nu N,\qquad
\sum_\nu m_\nu-e=r,\qquad
m_\nu\leq r+e+\sum_{\mu\ne\nu}w_\mu N
\leq r+(w-w_\nu)N.
\tag{GG.28}
\]
There are only finitely many integer tuples satisfying these bounds. Thus each coefficient is a finite polynomial, and all outputs through \(M\) use input coefficients through \(M+qN\), besides their finite assigned lower bounds. For the normalizing gauge alone the sharper upper bound is \(M+(q-1)N\). This proves finite-cutoff representability of the coaction and inverse maps, not just formal Laurent existence.

The invariant-ring specialization used in (GG.16) is valid inside this group stage. Therefore
\[
R[\mathcal X_N]^{\,\mathcal G_N}
=R[s_{d,\gamma,r}:r\geq-(d+1)N]
=R[\mathcal V_N].
\tag{GG.29}
\]
The notation denotes ordinary polynomial coordinate algebras on the displayed coefficient lists. The equality is the universal coaction equality, not only equality of invariant functions on field points. Allowing all \(N\) is cofinal in the Laurent functors: there are finitely many homogeneous coordinates, each Laurent series has a finite negative part, and a single sufficiently large \(N\) bounds them all. Hence
\[
\begin{aligned}
\bigcup_{N\geq1}\mathcal X_N(R)&=f+\mathfrak b\otimes R((t)),\\
\bigcup_{N\geq1}\mathcal G_N(R)&=N(R((t))),\\
(f+\mathfrak b(R((t))))/N(R((t)))&\simeq V\otimes R((t)).
\end{aligned}
\tag{GG.30}
\]
The exact group is Laurent \(N(R((t)))\), not just \(N(R[[t]])\) or positive polynomial currents. The stages include by setting newly allowed negative coefficients to zero, so they form ordinary ind-affine coefficient charts. Their inverse-limit function rings describe continuous functions on those charts; (GG.30) makes no assertion about all discontinuous characters of an abstract completed ring. Coefficient-algebra maps act termwise. No claim that an ordinary tensor product commutes with every infinite series ring is needed.

The following table is a reproducible algebraic diagram of the maps and bounds proved above; every height or scalar component appears with its full multiplicity.

| Object or map | Principal weight | Regular coefficients through \(M\) | Laurent lower bound at stage \(N\) | Proof locator |
| --- | --- | --- | --- | --- |
| Original \(b_j\) | \(j+1\) | Input connection jets | \(-(j+1)N\) | (GG.10), (GG.25) |
| \(A\mapsto Q(A)^{\pm1}\), height \(a\) | \(a\) | Uses \(b\) through \(M+a-1\) | \(-aN\) | (GG.5), (GG.12) |
| \(A\mapsto s_d(A)\) | \(d+1\) | Uses \(b\) through \(M+d\) | \(-(d+1)N\) | (GG.7), (GG.12) |
| \((u,s)\mapsto u\cdot(f+s)\) | Output \(j+1\) | Uses \(y\) through \(M+1\), \(s\) through \(M\) | Preserves \(-(j+1)N\) | (GG.8), (GG.26) |
| Gauge action on the product chart | \((u,s)\mapsto(gu,s)\) | A finite polynomial coaction | \(\mathcal G_N\) is closed under products and inverses | (GG.9), (GG.27) |
| Universal invariants and current normalizer | Retain all \(s_d\) and jets | \(R[s_{d,\gamma}^{(r)}]\) | \(R[s_{d,\gamma,r}:r\geq-(d+1)N]\) | (GG.19), (GG.24), (GG.29) |

*The finite mechanism is the actual principal splitting and gauge formula (DS.A9), (DS.A12)–(DS.A16); the new polynomial/coaction, derivative-bound and Laurent-stage implications are (GG.8)–(GG.30). For human-source context on classical W-algebra terminology, see De Sole–Kac–Valeri, [Adler–Gelfand–Dickey approach to classical W-algebras within the theory of Poisson vertex algebras, free arXiv:1401.2082v1, §§2.8–2.9](https://arxiv.org/abs/1401.2082v1). No source theorem substitutes for the fixed-data gauge or invariant proof.*

The result proves the ordinary principal gauge quotient and underlying normalizer algebra for the stated general graded datum. It preserves the earlier root/pinning, split-unipotent and faithful-group premises; intrinsic/global oper descent and full derived reduction retain their own hypotheses. Sections 3.9.1 and 3.9.3 supply any additional Poisson reduction and coordinate comparison. Non-type-A quantum lifts, quantum-center/oper identification, chiral/factorization, Satake, derived-family and global Langlands assertions are not consequences of this ordinary gauge calculation.

#### 3.9.3. The full Laurent reduction and its coordinate Poisson action

Let \(k\) be a characteristic-zero field. Fix a finite principal graded Lie datum
\[
\mathfrak g=\bigoplus_{j=-q}^{q}\mathfrak g_j,
\qquad [r,x]=jx\quad(x\in\mathfrak g_j),
\qquad (e,2r,f)\text{ an }\mathfrak{sl}_2\text{ triple},
\tag{GL.1}
\]
with \(e\in\mathfrak g_1\), \(f\in\mathfrak g_{-1}\), a perfect symmetric invariant form \(B\), and
\[
\mathfrak n=\bigoplus_{j>0}\mathfrak g_j,
\qquad \mathfrak b=\bigoplus_{j\geq0}\mathfrak g_j,
\qquad V=\ker\operatorname{ad}e.
\tag{GL.2}
\]
We use the actual direct splittings
\[
\mathfrak g_j=[f,\mathfrak g_{j+1}]\oplus V_j,
\qquad \operatorname{ad}f:\mathfrak g_{j+1}\hookrightarrow\mathfrak g_j
\quad(j\geq0),\qquad V_j=0\quad(j<0).
\tag{GL.3}
\]
Their finite construction is (DS.A5)–(DS.A9) of [*Opers, critical level and the Beilinson–Drinfeld construction*](opers-critical-level-and-the-beilinson-drinfeld-construction.md), §1.1.2. The positive gauge group is the specified polynomial nilpotent group \(N\) with Lie algebra \(\mathfrak n\), exponential and logarithm coordinates, and the finite gauge convention
\[
g\cdot A=\operatorname{Ad}(g)A-g'g^{-1}.
\tag{GL.4}
\]
Here and below the prime means \(d/dt\), acting trivially on the ordinary parameter algebra. For the supplied principal adjoint datum, the positive group construction is (DS.A12)–(DS.A16), and the preceding *General principal gauge, polynomial invariants and weighted Laurent charts*, (GG.8)–(GG.12) and (GG.25)–(GG.30), supplies the actual inverse maps and weighted stages used below. These are polynomial gauge calculations, not a quotient theorem assumed from geometry. In a split adjoint-group application, the root, pinning, split-unipotent and group-identification premises of §1.1 remain the stated group premises. The argument is over the fixed field \(k\); it does not require algebraic closure. If the specified datum includes a height-zero summand \(V_0\), its extension of the same finite calculation is justified explicitly below, with weight one.

**The ambient complete Poisson algebra.** Invariance gives
\[
(i+j)B(x,y)=B([r,x],y)+B(x,[r,y])=0
\quad(x\in\mathfrak g_i,\ y\in\mathfrak g_j).
\tag{GL.5}
\]
Thus \(B(\mathfrak g_i,\mathfrak g_j)=0\) unless \(i+j=0\). Perfectness makes the pairing between every pair of opposite grades perfect: a vector annihilating its opposite grade annihilates all of \(\mathfrak g\). Consequently
\[
\mathfrak n^{\perp}=\mathfrak b,
\qquad B(\mathfrak n,\mathfrak n)=0,
\qquad B(f,[\mathfrak n,\mathfrak n])=0.
\tag{GL.6}
\]
The last equality uses that the bracket has grade at least two, whereas \(f\) has grade minus one.

For any ordinary commutative \(k\)-algebra \(R\), let \(J_{x,m}\) be linear in \(x\in\mathfrak g\), and set
\[
\mathcal C_{N,R}=R[J_{x,m}:m<N],\qquad
\widehat{\mathcal C}_R=\varprojlim_{N\geq1}\mathcal C_{N,R}.
\tag{GL.7}
\]
Choose a finite basis of \(\mathfrak g\) for the polynomial generators. The transition sets new modes to zero. If
\[
A(t)=\sum_{m\in\mathbb Z}A_m t^{-m-1},
\qquad J_{x,m}(A)=B(x,A_m),
\tag{GL.8}
\]
a continuous \(R\)-algebra character to a discrete \(R\)-algebra \(S\) factors through some \(\mathcal C_{N,R}\). It is exactly a Laurent connection coefficient in \(\mathfrak g\otimes_k S((t))\) with all exponents at least \(-N\). Conversely every such coefficient tuple gives that character. No discontinuous character is included in this statement.

On the polynomial ring in all integer modes define
\[
\{J_{x,m},J_{y,a}\}
=J_{[x,y],m+a}+mB(x,y)\delta_{m+a,0}.
\tag{GL.9}
\]
Its Jacobi identity is elementary. The form terms in a cyclic triple have the common coefficient \(B([x,y],z)\), by invariance and symmetry. When \(m+a+c=0\), their numerical coefficients are \((m+a)+(a+c)+(c+m)=0\). Otherwise every scalar term vanishes. The Lie part is Jacobi in \(\mathfrak g\). Antisymmetry follows from \(m=-a\) in the scalar term. Leibniz now proves all Poisson identities on polynomials. This also recovers the residue-cocycle proof of (K2.1) in §3.

Let \(K_N\) denote the kernel of the \(N\)-th projection. The exact tail estimates are
\[
\{K_N,K_M\}\subseteq K_N\quad(M\geq N\geq1),
\qquad
\{p,K_M\}\subseteq K_N
\quad\bigl(M\geq\max(N,N-a(p))\bigr),
\tag{GL.10}
\]
where \(p\) is a finite polynomial and \(a(p)\) is the least mode among its variables, or zero if it is constant. First prove these for polynomial tail ideals. In a monomial bracket, a high factor survives unless both chosen high factors were removed. In the latter case their replacement has index at least \(N+M\), and their scalar bracket is zero because both indices are positive. For the second estimate, removal of the high factor and a factor of \(p\) gives index at least \(M+a(p)\geq N\); it again cannot give a scalar. These are exactly (DL.3)–(DL.4), whose proof used no matrix identity.

Here is the passage to complete inputs. For a requested output cutoff \(N\), fix finite polynomial representatives \(u_N,v_N\) of the \(N\)-th components of \(u,v\in\widehat{\mathcal C}_R\). Later representatives differ from these by elements of the polynomial \(N\)-tail. Their differences at a sufficiently later stage are in the \(M\)-tail. Expand a difference of brackets by bilinearity. Terms involving \(u_N,v_N\) are in \(K_N\) by the second estimate in (GL.10), for sufficiently large \(M\); terms involving the remaining \(N\)-tails are in \(K_N\) by the first estimate. The brackets are therefore Cauchy independently of representatives. Their limits define a jointly continuous bracket on \(\widehat{\mathcal C}_R\). The same argument proves both estimates for the closed tail ideals. All Poisson identities pass from dense polynomial inputs to their limits. In particular the cutoff rings themselves have not been declared Poisson quotients.

**The closed moment fibre and its normalizer.** Put
\[
\chi(x)=B(f,x),\qquad
\mu_{x,m}=J_{x,m}-\chi(x)\delta_{m,-1}
\quad(x\in\mathfrak n,\ m\in\mathbb Z),
\qquad I_R=\overline{(\mu_{x,m})}.
\tag{GL.11}
\]
The index \(-1\) describes the constant coefficient \(f\), by (GL.8). At every cutoff, the moment relations eliminate exactly the coordinates dual to \(\mathfrak n\), replacing them by the corresponding constant coordinates of \(f\). The remaining coordinates are those of \(\mathfrak b\), by (GL.6). Thus there is a surjective continuous map with a compatible polynomial section
\[
\begin{aligned}
q_R&:\widehat{\mathcal C}_R\longrightarrow\widehat{\mathcal F}_R,
&\ker q_R&=I_R,\\
\widehat{\mathcal F}_R
&=\text{the completed coefficient algebra of }f+\mathfrak b((t)).
\end{aligned}
\tag{GL.12}
\]
For kernel equality, a finite-cutoff polynomial vanishing after these eliminations is in their polynomial ideal: divide successively by the monic linear relations \(z-a\), which works over every \(R\). Lift that ideal polynomial back to the all-mode ring. It approximates the given kernel element at the chosen cutoff. Hence the finite polynomial moment ideal is dense in the kernel, proving the displayed equality without a general exactness assertion about inverse limits.

Equations (GL.6) and (GL.9) give
\[
\{\mu_{x,m},\mu_{y,a}\}
=\mu_{[x,y],m+a},
\qquad \{I_R,I_R\}\subseteq I_R.
\tag{GL.13}
\]
The scalar term vanishes; so does \(\chi([x,y])\). Leibniz proves the ideal assertion on finite polynomials, and joint continuity and density prove it on the closure. Define
\[
\mathcal U_R=\{u\in\widehat{\mathcal C}_R:
\{\mu_{x,m},u\}\in I_R\text{ for every }x,m\},
\qquad \widehat W_R=\mathcal U_R/I_R.
\tag{GL.14}
\]
This is a closed normalizer, since each bracket with a fixed moment is continuous and \(I_R\) is closed. It contains \(I_R\). For \(u\in\mathcal U_R\), Leibniz first proves \(\{I_R,u\}\subseteq I_R\) on the finite ideal and then on its closure. Jacobi proves that the bracket of two normalizing elements still normalizes; Leibniz proves the same for their product. Thus \(I_R\) is a Poisson ideal in \(\mathcal U_R\), and (GL.14) has a bracket independent of lifts. The unrestricted ambient quotient in (GL.12) is used only as a coefficient algebra.

**All Laurent gauges, including parameter families.** For a Laurent test \(X(t)\in\mathfrak g\otimes_k S((t))\), define
\[
\ell_X(A)=\operatorname{Res}B(X(t),A(t))dt,
\qquad
\{\ell_X,\ell_Y\}(A)
=\operatorname{Res}\bigl(B(A,[X,Y])+B(X',Y)\bigr)dt.
\tag{GL.15}
\]
Only finitely many coefficients of \(X\) contribute at a fixed cutoff, so \(\ell_X\) is a completed linear function. The residue formula is (GL.9) summed at that cutoff and then passed to the limit. Its Hamiltonian vector field is
\[
\delta_X A=[A,X]+X'.
\tag{GL.16}
\]
Indeed pairing this vector with \(Y\) gives (GL.15). For \(X\in\mathfrak n((t))\), it is the infinitesimal left gauge by \(\exp(-sX)\). All integer moment modes are needed: tests with arbitrarily negative powers belong to the full Laurent gauge algebra.

An invariant here means a function whose equality under a gauge holds after every ordinary coefficient extension \(R\to S\), for every \(A\in f+\mathfrak b\otimes S((t))\) and \(g\in N(S((t)))\). The moment-normalizer condition implies this full functorial invariance. Positive formal tails of \(X\) are limits of finite tests, so (GL.14), continuity and closedness of \(I_R\) first imply \(\{\ell_X,u\}\in I_R\) for every such test. Now substitute the family \(\exp(-sX)\cdot A\), with \(s\) an independent polynomial parameter. The exponential, adjoint action and logarithmic derivative are finite height polynomials. A fixed Laurent pole bound on \(X,A\) consequently gives a bound on the whole family independent of \(s\). At that bound a completed function is a finite polynomial in coefficients; its evaluation is an ordinary polynomial in \(s\). The group law differentiates it at each \(s\) to the evaluation of \(\{\ell_X,u\}\), which is zero. Since every positive integer is a unit in \(S\), this polynomial is constant, even when \(S\) has nilpotents. Every positive gauge is \(\exp X\), so this proves invariance under all of \(N(S((t)))\).

Conversely, functorial invariance applied over \(S[s]/(s^2)\) to \(\exp(-sxt^m)\) makes (GL.16) vanish on the function. This says \(\{\mu_{x,m},u\}\bmod I_R=0\). It is an equality of coefficient functions: at each cutoff test it on the universal coefficient algebra \(R[z_1,z_2,\ldots]\) and its universal Laurent coefficient tuple. A polynomial equal to zero there has all coefficients zero over \(R\). No assertion about \(k\)-points or reduced parameters is used. We have proved
\[
q_R(\mathcal U_R)=
\widehat{\mathcal F}_R^{\,N((t))}
\quad\text{with the functorial meaning just specified.}
\tag{GL.17}
\]
Surjectivity onto these invariants is also explicit: lift an invariant by the section in (GL.12); its moment brackets vanish modulo \(I_R\) by the dual-number argument, so the lift belongs to \(\mathcal U_R\).

**The quotient and its actual topology.** Choose a homogeneous basis \(v_{d,a}\) of \(V_d\), and write \(v(t)=\sum v_{d,a}z_{d,a,p}t^p\). For the supplied datum with \(V_0=0\), the actual weighted product theorem (GG.25)–(GG.30) gives polynomial inverse maps
\[
N_N\times\mathcal V_N\xrightarrow{\ \sim\ }\mathcal B_N,
\qquad (g,v)\longmapsto g\cdot(f+v),
\tag{GL.18}
\]
where grade-\(j\) Borel coefficients have poles at most \((j+1)N\), height-\(a\) exponential gauge coordinates have poles at most \(aN\), and grade-\(d\) slice coefficients have poles at most \((d+1)N\). Its BCH multiplication and inverses preserve \(N_N\). Its maps and inverse maps are coefficientwise polynomial, including over nonreduced rings. These are the particular product-chart and bound assertions used here. They are cofinal with common finite Laurent pole bounds, since only finitely many positive integer weights occur.

The case of a supplied \(V_0\) requires no discarded component or additional group theorem. At height zero decompose \(b_0=[f,x_1]+v_0\) by (GL.3) and gauge by \(\exp x_1\); the derivative and every other change have higher height. Continue the same finite procedure. Lowest-height comparison with the direct splitting proves its uniqueness, and so proves the product and inverse identities. Give \(v_0\) weight one. A gauge word with \(f\), a Borel coefficient or a derivative has output weight one more than its output height; thus every output of weight \(w\) is a finite sum of differential monomials with total input weight plus total derivative order equal to \(w\). If the derivative order is \(a\), its pole is at most \((w-a)N+a\leq wN\). BCH words have total weight their gauge height, so the gauge stage is closed. Finally, in a monomial contributing to a prescribed Laurent coefficient, each input exponent has a finite lower bound and their sum is prescribed; hence every exponent has a finite upper bound as well. Every output coefficient is therefore a finite polynomial. This proves the same product charts and coefficient maps, now including \(v_0\) with lower bound \(-N\).

On the product in (GL.18), the action translates the gauge factor. A functorially invariant function is independent of that factor: apply its equality to the universal gauge and translate it to identity by its own inverse. This takes place over the ordinary polynomial coefficient algebra of the chart; the BCH formulas are finite. Hence it proves equality of actual polynomials at that chart, rather than equality only at field-valued points. Taking the compatible charts gives
\[
\Theta_R:\widehat W_R\xrightarrow{\ \sim\ }\mathcal P_R^V,
\qquad
\mathcal P_R^V=
\varprojlim_{N\geq1}R[z_{d,a,p}:p\geq-(d+1)N].
\tag{GL.19}
\]
The map is evaluation in slice form. Its inverse pulls back a slice function through the unique normal-form coefficients of \(f+b\). Those coefficients are the fixed differential polynomials constructed using (GL.3) and the finite height gauges; the weighted bounds make the pullback continuous. To lift it into the ambient normalizer, extend these polynomials by first taking the linear \(\mathfrak b\)-projection of \(A-f\). The resulting continuous algebra map has gauge-invariant restriction to the fibre, so its image lies in \(\mathcal U_R\) by (GL.17). Evaluation in the slice is its inverse modulo \(I_R\). Both maps are continuous for the quotient topology on \(\mathcal U_R/I_R\). This proves the topological isomorphism and completeness of the quotient by construction. It does not assume that an arbitrary quotient of a complete ring is complete.

The reduced bracket is jointly continuous: use this continuous lift, the ambient jointly continuous bracket, and slice evaluation. It equips \(\mathcal P_R^V\) with the genuine principal reduced Poisson bracket. Every construction commutes with maps of ordinary coefficient algebras. In particular
\[
\mathcal P_R^V=
\varprojlim_N\bigl(R\otimes_k k[z_{d,a,p}:p\geq-(d+1)N]\bigr)
\tag{GL.20}
\]
is the coefficient extension intended here. Neither \(R\otimes_k\varprojlim_N\) nor a bound on the polynomial degree of a whole completed element is assumed. Continuous characters of (GL.19) are precisely \(V\otimes_k S((t))\), the coefficient functor (DS.A21), with a cofinal weighted choice of its stages.

**Coordinate transport without a matrix trace.** Let \(\phi\) be a continuous ordinary \(R\)-coordinate substitution, including a nilpotent constant term, and put
\[
\psi=\phi^{-1},\qquad \alpha=\psi',\qquad c=\alpha'/\alpha,
\qquad D_\alpha(x)=\alpha^j x\quad(x\in\mathfrak g_j).
\tag{GL.21}
\]
The inverse, unit derivative, coefficient-finite Laurent substitution and residue change of variable are proved in §1.1.8 and (RC.C7) of [*Opers, critical level and the Beilinson–Drinfeld construction*](opers-critical-level-and-the-beilinson-drinfeld-construction.md). Only integer powers of \(\alpha\) occur. Brackets add grades, so \(D_\alpha\) is a Lie automorphism; (GL.5) makes it preserve \(B\). The finite homogeneous BCH polynomials also make \(\exp x\mapsto\exp(D_\alpha x)\) a group automorphism of \(N(R((t)))\). Define the normalized connection transformation
\[
C_\phi(A)=A^\phi
=D_\alpha\bigl(\alpha A\circ\psi\bigr)-c r.
\tag{GL.22}
\]
We prove its Poisson property directly, including the correction term. For a Laurent test \(X\), set
\[
T_\phi X=(D_\alpha^{-1}X)\circ\phi,
\qquad
\ell_X(C_\phi A)=\ell_{T_\phi X}(A)
-\operatorname{Res}cB(r,X)dt.
\tag{GL.23}
\]
The first equality of functions follows from \(u=\psi(t)\), \(du=\alpha dt\), and invariance of \(B\) under \(D_\alpha\). Differentiating a homogeneous component gives
\[
(D_\alpha^{-1}X)'
=D_\alpha^{-1}(X'-c[r,X]),
\qquad [T_\phi X,T_\phi Y]=T_\phi[X,Y].
\tag{GL.24}
\]
By the chain rule and residue change of variable,
\[
\begin{aligned}
\operatorname{Res}_u B((T_\phi X)',T_\phi Y)du
&=\operatorname{Res}_t B((D_\alpha^{-1}X)',D_\alpha^{-1}Y)dt\\
&=\operatorname{Res}_t B(X',Y)dt
-\operatorname{Res}_t cB(r,[X,Y])dt.
\end{aligned}
\tag{GL.25}
\]
The last sign follows from \(B([r,X],Y)=B(r,[X,Y])\). Substitution of (GL.23)–(GL.25) into (GL.15) now proves
\[
\{\ell_X\circ C_\phi,\ell_Y\circ C_\phi\}
=\{\ell_X,\ell_Y\}\circ C_\phi.
\tag{GL.26}
\]
Indeed the extra term in the transformed cocycle is exactly the constant in \(\ell_{[X,Y]}\circ C_\phi\). Thus the grading-dependent transformation requires the shift \(-cr\); a plain substitution of graded one-forms would omit this correction. Linear tests determine the polynomial bracket, and continuity extends (GL.26) to the whole complete algebra.

The moment fibre is preserved, since
\[
C_\phi(f+b)=f+D_\alpha(\alpha b\circ\psi)-cr\in f+\mathfrak b((t)).
\tag{GL.27}
\]
The grade-minus-one coefficient \(f\) stays normalized. The point \(f\) itself transforms to \(f-cr\). More explicitly, for \(X\in\mathfrak n((t))\), \(B(r,X)=0\), and \(D_\alpha f=\alpha^{-1}f\). Residue change of variable therefore gives
\[
\mu_X\circ C_\phi=\mu_{T_\phi X},
\qquad \mu_X=\ell_X-\operatorname{Res}B(f,X)dt.
\tag{GL.28}
\]
The tests on the right still lie in \(\mathfrak n((t))\). The inverse coordinate gives the reverse inclusion, so the continuous pullback preserves exactly the closed moment ideal, not merely its pointwise vanishing set. Its Poisson property then preserves the normalizer as well.

For completeness, it also conjugates the full positive gauge action. Put \(\widetilde g=D_\alpha(g\circ\psi)\), where the grading automorphism acts on exponential coordinates. Its right logarithmic derivative satisfies
\[
\widetilde g'\widetilde g^{-1}
=D_\alpha\bigl(\alpha(g'g^{-1})\circ\psi\bigr)
+c(r-\operatorname{Ad}(\widetilde g)r).
\tag{GL.29}
\]
To verify this without a torus lift, write \(g\circ\psi=\exp x\) and \(z=D_\alpha x\). Then \(z'=D_\alpha x'+c[r,z]\). Apply the finite logarithmic-derivative polynomial \(\sum_{a\geq0}(\operatorname{ad}z)^a z'/(a+1)!\). Its contribution from \(c[r,z]=-c(\operatorname{ad}z)r\) is exactly \(c(r-\exp(\operatorname{ad}z)r)\); its other contribution is the first term of (GL.29). Substituting it into the left gauge formula proves
\[
C_\phi(g\cdot A)=\widetilde g\cdot C_\phi(A).
\tag{GL.30}
\]
All these identities are finite height identities over every ordinary \(R\), including nilpotent parameter rings.

We justify the remaining continuity and composition assertions. Write \(\psi=b+t a(t)\), with \(a(0)\) a unit and \(b^\nu=0\). For \(L>0\),
\[
\psi^{-L}=t^{-L}a(t)^{-L}
\sum_{j=0}^{\nu-1}\binom{-L}{j}
\left(\frac{b}{t a(t)}\right)^j,
\qquad
\psi^M\in t^{M-\nu+1}R[[t]]\quad(M\geq\nu).
\tag{GL.31}
\]
The first expression has pole at most \(L+\nu-1\); the second is the finite nilpotent tail bound (PC.8). For a fixed output coefficient, the nonnegative part of a substituted series contributes only finitely many input coefficients. Multiplication by the regular units \(\alpha^j\) does not increase poles, and \(c\) is regular. Thus (GL.22), (GL.23) and (GL.30) are coefficientwise polynomial at cofinally larger pole charts and define continuous maps on the completed rings. On a weighted chart the possible additive increase \(\nu-1\) is bounded by replacing \(N\) with \(N+\nu-1\), since every coefficient weight is at least one. The same argument for \(\phi\) proves continuity of the inverse. It proves ordinary nilpotent-coordinate continuity directly, rather than assuming it from a field-valued substitution.

For two inverse substitutions \(\psi_1,\psi_2\), let \(\alpha_i=\psi_i'\) and \(c_i=\alpha_i'/\alpha_i\). The derivative and logarithmic derivative of \(\psi_2\circ\psi_1\) are
\[
\alpha_{21}=\alpha_1(\alpha_2\circ\psi_1),
\qquad c_{21}=c_1+\alpha_1(c_2\circ\psi_1).
\tag{GL.32}
\]
Multiplication of the grading automorphisms and \(D_\alpha r=r\) show directly that
\(C_{\phi_1}\circ C_{\phi_2}=C_{\phi_1\circ\phi_2}\).
The identity coordinate is identity, and the inverse coordinate gives the inverse map. Pullbacks satisfy the corresponding reversed composition order. This specifies the action convention on both connections and coefficient functions.

**The previously constructed oper normalization.** For a slice representative, (GL.22) is
\(f-cr+\sum_d\alpha^{d+1}v_d\circ\psi\).
Gauge by \(\exp((c/2)e)\). It fixes every \(v_d\), since \(V=\ker\operatorname{ad}e\). The triple relations give
\[
\operatorname{Ad}(\exp(ze))f=f+2zr-z^2e,
\qquad \operatorname{Ad}(\exp(ze))r=r-ze.
\tag{GL.33}
\]
Its derivative term is \(-z'e\). For \(z=c/2\) the Cartan component cancels, and the remaining quadratic term is \(c^2e/4-c'e/2\). Hence the unique slice coordinate action is
\[
v^\phi=\sum_{d\geq0}\alpha^{d+1}v_d\circ\psi
-\tfrac12 S(\psi)e,
\qquad S(\psi)=\frac{\psi'''}{\psi'}
-\frac32\left(\frac{\psi''}{\psi'}\right)^2
=c'-\tfrac12c^2.
\tag{GL.34}
\]
This is exactly (DS.G3)–(DS.G5), with \(t=\psi(s)\), now endowed with its actual reduced Poisson action. It is an ordinary coefficient statement. Its interpretation as intrinsic adjoint opers uses the same explicit group and torsor-descent premises as §1.1.6; the Poisson calculation does not establish additional descent foundations.

For matrices, take \(r=\operatorname{diag}((n+1)/2-i)_{i=1}^n\). On \(E_{ij}\) it has eigenvalue \(j-i\). Thus \(D_\alpha\) is conjugation by \(D=\operatorname{diag}(\alpha^{n-1},\ldots,1)\), and
\[
-cr=-D'D^{-1}+\frac{n-1}{2}c\mathbf1.
\tag{GL.35}
\]
Formula (GL.22) therefore becomes exactly (DL.14), including its trace correction; no matrix trace was used to prove (GL.25). The scalar-density normalization and its type A bracket comparison remain the actual separate proofs of (DL.15)–(DL.16) and (DC.1)–(DC.10).

The maps and topologies can be read together in this square:
\[
\begin{array}{ccccc}
\mathcal U_R&\longrightarrow&\widehat W_R=\mathcal U_R/I_R
&\xrightarrow{\ \Theta_R\ }&\mathcal P_R^V\\
{\scriptstyle C_\phi^*}\downarrow&&
\downarrow{\scriptstyle\overline{C_\phi^*}}&&
\downarrow{\scriptstyle (v\mapsto v^\phi)^*}\\
\mathcal U_R&\longrightarrow&\widehat W_R
&\xrightarrow{\ \Theta_R\ }&\mathcal P_R^V.
\end{array}
\tag{GL.36}
\]
*The first horizontal map divides by the closed coisotropic ideal of every integer moment mode (GL.11)–(GL.14). The second is the complete coefficient isomorphism proved using the weighted product charts in (GL.18)–(GL.19). The vertical maps preserve the actual brackets by the residue correction (GL.25), preserve the full moment ideal by (GL.28), and have the cofinal nilpotent-coordinate bounds (GL.31). The rightmost map is the explicitly normalized oper-coefficient action (GL.34). This diagram records completed ordinary Poisson algebras; it does not turn a fixed pole cutoff or regularity constraint into a Poisson quotient.*

Products of finitely many principal data use these constructions componentwise and a common pole bound. The zero datum gives the coefficient ring \(R\) with zero bracket. The assumptions are the finite Lie datum, perfect invariant form, actual direct splittings and polynomial positive-gauge construction used above; an algebraic-group application retains its specified root/group and intrinsic-oper descent premises. This proves the general classical Laurent reduction and its coordinate Poisson action. It supplies neither non-type-A basic quantum lifts nor a quantum-center comparison, a comparison with a different invariant form or a Langlands-dual normalization, a derived/global reduction, or a chiral, factorization or Satake theorem.

#### 3.9.4. Reduced coefficient brackets and the general Virasoro law

Continue with the finite principal datum and the same perfect invariant symmetric form \(B\) of §§3.9.1–3.9.3. In this subsection impose \(V_0=0\), as proved for the supplied pinned semisimple datum in §1.1.2; every slice height is therefore positive. The datum, including its height splitting and unipotent polynomial operations, has the exact structural hypotheses of §1.1. The conclusion below concerns its ordinary classical reduction. No choice of the form is suppressed.

**An actual formula for every reduced coefficient bracket.** Choose homogeneous bases \(v_{d,\gamma}\) of \(V_d\), including every repeated height, and write the normal form as
\[
 A^{\mathrm{slice}}=f+\sum_{d,\gamma}s_{d,\gamma}v_{d,\gamma}.
 \tag{GS.1}
\]
The polynomial inverse (GG.5)–(GG.8) expresses each \(s_{d,\gamma}(A)\) as a finite differential polynomial in the coordinates of \(f+\mathfrak b\). It also proves that their derivatives freely generate the invariant algebra. Thus the PVA normalizer quotient of §3.9.1 is, as a differential algebra, exactly
\[
 W_{B,R}=R[s_{d,\gamma}^{(a)}:a\geq0].
 \tag{GS.2}
\]
This is the ordinary polynomial identity (GG.24), combined with the actual normalizer bracket, not a new bracket declared on an orbit set.

Here is a finite algorithm for that bracket in every degree. Use the grading projection \(\operatorname{pr}_{\mathfrak b}:\mathfrak g\to\mathfrak b\), and extend the slice coefficients to the entire affine current algebra by
\[
 \widetilde s_{d,\gamma}(A)
   =s_{d,\gamma}\bigl(f+\operatorname{pr}_{\mathfrak b}A\bigr).
 \tag{GS.3}
\]
This is a polynomial extension. Restricting to the moment fibre recovers the original coefficient. Every such lift lies in the normalizer, because the quotient coefficient is invariant; changing the extension changes it by the differential moment ideal. Let \(\operatorname{ev}_{f+s}\) mean substitution of the slice coefficient and all its derivatives. With indices \(i,j\) abbreviating pairs \((d,\gamma)\), the full answer is
\[
 \boxed{\{s_i{}_\lambda s_j\}_{W_B}
  =\operatorname{ev}_{f+s}
       \{\widetilde s_i{}_\lambda\widetilde s_j\}_{\mathrm{aff},B}.}
 \tag{GS.4}
\]
To prove it, compute the affine bracket by the finite master formula of §3.9.1. Normalizer closure makes every coefficient invariant modulo the moment ideal. An invariant coefficient equals its slice restriction, by (GG.16). Thus the expression on the right is precisely its quotient coefficient. Representative independence follows from the proved ideal test inside the normalizer. Every operation—fixed linear projections, finite gauge polynomials, polynomial differentiation and slice evaluation—is finite. Consequently (GS.4) gives every coefficient and derivative correction, and its skew, Jacobi and Leibniz identities are those already proved for the quotient. No assertion about highest symbols alone is needed.

For Laurent coefficients use the weighted stages of (GG.25). Each coefficient of a fixed differential polynomial is a finite polynomial at a stage, by (GG.28). Every Fourier coefficient of a differential moment-ideal expression belongs to the closed Laurent moment ideal: each term contains a factor \(T^a(J_x-\chi(x))\); its coefficient is a scalar multiple of a physical moment mode, convolved with finitely many other factors at the chosen stage. Compatible finite sums lie in the closed ideal. Thus all coefficient lifts of (GS.3) normalize that ideal, and the same calculation is independent of the regular lift.

If \(s_i\) has weight \(w_i=d_i+1\), write
\[
 \{s_i{}_\lambda s_j\}_{W_B}
       =\sum_{a\geq0}\frac{\lambda^a}{a!}c_{ij,a},
 \qquad
 \operatorname{wt}c_{ij,a}=w_i+w_j-a-1.
 \tag{GS.5}
\]
The weight assertion follows on affine generators from \(\operatorname{wt}J_x=1-\operatorname{ht}(x)\), the grading orthogonality of \(B\), and the two Leibniz rules; the moment character is homogeneous at weight zero. The same residue calculation (DC.4)–(DC.6), whose proof uses only the affine delta kernel and finite product and derivative rules, gives
\[
 \{s_{i,m},s_{j,n}\}_{W_B}
   =\sum_{a\geq0}\binom{m+w_i-1}{a}(c_{ij,a})_{m+n},
 \qquad m,n\in\mathbb Z.
 \tag{GS.6}
\]
Here \(s_i(t)=\sum_m s_{i,m}t^{-m-w_i}\); the output field is normalized by the weight in (GS.5), and constants use weight zero. To see the indices directly, the residue test powers are \(m+w_i-1,n+w_j-1\). Differentiating the first test \(a\) times leaves the output test exponent \(m+n+w_i+w_j-a-2\), selecting normalized mode \(m+n\) of that output weight. The finite sum uses generalized binomial coefficients for negative test exponents.

Formula (GS.6) has values in the completion; products of coefficient fields may involve infinitely many modes before taking a cutoff. The completed bracket of §3.9.3 is jointly continuous. Polynomials in slice coefficients are dense in the weighted inverse-limit coefficient algebra. Hence (GS.4)–(GS.6) identify the entire completed reduced Poisson algebra, including arbitrary pairs of completed functions. They do not declare an individual pole-cutoff quotient an ordinary Poisson algebra.

**A quadratic representative in the actual normalizer.** Take a basis \(u_a\) of \(\mathfrak g\) and its \(B\)-dual basis \(u^a\). Put
\[
 Q_B=\frac12\sum_a J_{u_a}J_{u^a},\qquad
 \tau_B=Q_B+TJ_r,
 \qquad r=h/2.
 \tag{GS.7}
\]
This does not depend on the chosen basis: in \(B\)-dual connection coordinates it is
\[
 Q_B(A)=\tfrac12B(A,A),\qquad
 \tau_B(A)=\tfrac12B(A,A)+B(r,A').
 \tag{GS.8}
\]
The pairing identification is the one proved in §3.9.1, and \(T\) is the ordinary derivative.

We compute its brackets before reduction. Right Leibniz in \(\{J_x{}_\lambda Q_B\}\) has Lie contribution \(B(A,[A,x])=0\), by symmetry and invariance of \(B\). Its two symmetric central contributions add to \(\lambda J_x\): the dual-basis identities give \(\sum_a B(x,u_a)J_{u^a}=J_x\). Thus skew symmetry and a second right-Leibniz calculation give
\[
 \{J_x{}_\lambda Q_B\}=\lambda J_x,\qquad
 \{Q_B{}_\lambda J_x\}=(T+\lambda)J_x,
 \qquad
 \{Q_B{}_\lambda Q_B\}=(T+2\lambda)Q_B.
 \tag{GS.9}
\]
For the last formula, the derivative terms in the product sum are \(TQ_B\), while its two lambda terms are \(2\lambda Q_B\). These are classical commutative products, so there is no quantum double contraction.

For homogeneous \(x\in\mathfrak g_j\subset\mathfrak n\), one has \([x,r]=-jx\) and \(B(x,r)=0\). Sesquilinearity therefore gives
\[
 \{J_x{}_\lambda\tau_B\}
  =(1-j)\lambda J_x-jTJ_x.
 \tag{GS.10}
\]
If \(j=1\), the right side is \(-T(J_x-\chi(x))\). If \(j>1\), \(\chi(x)=B(f,x)=0\), so both terms lie in the moment ideal. Linear combinations give the assertion for every \(x\in\mathfrak n\). Therefore \(\tau_B\) is an actual element of the normalizer and determines a reduced quadratic Hamiltonian. This proves its gauge invariance through the same current action, including every derivative moment test.

Since \([r,r]=0\), \(\{J_r{}_\lambda J_r\}=B(r,r)\lambda\). The four terms in the bracket of (GS.7) are
\[
\begin{aligned}
 \{Q_B{}_\lambda Q_B\}&=(T+2\lambda)Q_B,\\
 \{Q_B{}_\lambda TJ_r\}&=(T+\lambda)^2J_r,\\
 \{TJ_r{}_\lambda Q_B\}&=-\lambda^2J_r,\\
 \{TJ_r{}_\lambda TJ_r\}&=-B(r,r)\lambda^3.
\end{aligned}
 \tag{GS.11}
\]
Adding them gives the complete reduced Virasoro bracket
\[
 \boxed{\{\tau_B{}_\lambda\tau_B\}
       =(T+2\lambda)\tau_B-B(r,r)\lambda^3.}
 \tag{GS.12}
\]
It already holds in the unreduced affine PVA. Its descent is justified by (GS.10), rather than by declaring a Cartan projection Poisson. With normalized field \(\tau_B(t)=\sum_m\tau_{B,m}t^{-m-2}\), (GS.6) gives
\[
 \boxed{\{\tau_{B,m},\tau_{B,n}\}
   =(m-n)\tau_{B,m+n}
       -B(r,r)(m^3-m)\delta_{m+n,0}.}
 \tag{GS.13}
\]
Indeed the normalized mode of \(T\tau_B\), of weight three, is \(-(m+n+2)\tau_{B,m+n}\); the first-order term adds \(2(m+1)\tau_{B,m+n}\). The cubic term is \(-6B(r,r)\binom{m+1}{3}\) times the weight-zero constant mode, giving exactly (GS.13) for every pair of integers. This uses the full Laurent normalizer, not only nonnegative modes.

**The Schwarzian from the exact normalized coordinate gauge.** Write \(\psi=\phi^{-1}\), \(\alpha=\psi'\), \(c=\alpha'/\alpha\), and let \(D_\alpha\) multiply \(\mathfrak g_j\) by \(\alpha^j\). The coordinate map proved in §3.9.3 is
\[
 A^\phi=D_\alpha(\alpha A\circ\psi)-cr.
 \tag{GS.14}
\]
It preserves the grade-minus-one coefficient \(f\) and the moment fibre \(f+\mathfrak b\). The point \(f\) itself becomes \(f-cr\); the normalization gauge after substitution is essential. Grading orthogonality proves that \(D_\alpha\) preserves \(B\), and \(D_\alpha r=r\). Hence
\[
\begin{aligned}
 \tfrac12B(A^\phi,A^\phi)
 &=\tfrac12\alpha^2B(A,A)\circ\psi
    -\alpha cB(r,A)\circ\psi+\tfrac12c^2B(r,r),\\
 B(r,(A^\phi)')
 &=\alpha'B(r,A)\circ\psi
    +\alpha^2B(r,A')\circ\psi-c'B(r,r).
\end{aligned}
 \tag{GS.15}
\]
The mixed terms cancel because \(\alpha'=\alpha c\). Since
\(c'-c^2/2=\psi'''/\psi'-3(\psi''/\psi')^2/2\), we obtain
\[
 \boxed{\tau_B^\phi
   =\alpha^2\tau_B\circ\psi-B(r,r)\{\psi,t\}.}
 \tag{GS.16}
\]
All coefficients make sense for the ordinary continuous coordinates, including nilpotent constants, by the exact finite substitution and cofinality bounds in §3.9.3. No analytic uniformization is used.

On the slice \(A=f+s\), grading gives \(B(s,s)=B(r,s')=B(f,f)=0\). Consequently the same invariant is the actual linear functional on its height-one slice component:
\[
 \tau_B(f+s)=B(f,s_1),\qquad
 B(f,e)=B([e,f],r)=2B(r,r).
 \tag{GS.17}
\]
The second identity uses \([f,r]=f\) and invariance of \(B\). Thus the normal-form coordinate law (DS.G4) gives (GS.16) again: its inhomogeneous correction is \(-\{\psi,t\}e/2\). This directly compares the coisotropic Hamiltonian with the earlier ordinary oper coefficient normalization. It retains all height-one components, and divides by no possibly vanishing \(B(r,r)\).

The mechanism is displayed by the commutative square
\[
\begin{array}{ccc}
 f+\mathfrak b(R((t)))&\xrightarrow{\ \text{normal form}\ }&V\otimes R((t))\\
 \downarrow{\scriptstyle\tau_B}&&\downarrow{\scriptstyle s\mapsto B(f,s_1)}\\
 R((t))&\xrightarrow{\ \operatorname{id}\ }&R((t)).
\end{array}
 \tag{GS.18}
\]
*The top arrow is the explicit quotient by Laurent unipotent gauges (GG.27)–(GG.30), carrying the reduced Poisson bracket of §3.9.3. Both vertical arrows give the same quadratic field by (GS.8), (GS.10) and (GS.17). Its exact PVA bracket, all-integer modes and coordinate cocycle are (GS.12), (GS.13) and (GS.16). The scalar codomain here is the coefficient functor of that field; the diagram does not assert that arbitrary Laurent scalar functions have the reduced bracket.*

For the trace form on \(\mathfrak{sl}_n\), \(r=\operatorname{diag}((n+1)/2-i)\), so
\[
 B(r,r)=\sum_{i=1}^n\left(i-\frac{n+1}{2}\right)^2
       =\frac{n(n^2-1)}{12},\qquad \tau_B=-s_2.
 \tag{GS.19}
\]
The sum follows by the finite formulas \(\sum i=n(n+1)/2\) and \(\sum i^2=n(n+1)(2n+1)/6\), each proved by induction. The equality \(\tau_B=-s_2\) follows in rank two from (DC.8), and in every rank from the injective reduced Miura map: its image is \(\sum h_i^2/2+\sum r_i h_i'\), exactly the negative of (AP.19) when \(\sum h_i=0\). Thus this general formula reproduces the fully proved type A scalar normalization. Products use the direct sums of the specified data and add their quadratic fields and constants; the zero datum gives the zero field.

The theorem proves the ordinary principal classical reduction, its coefficient brackets and coordinate-equivariant Laurent extension at the stated finite structural premises. It does not identify an unspecified bilinear form with the deformation form or Langlands-dual form in a quantum-center theorem. The non-type-A basic lifts, full completed center and center/oper-Poisson comparison, as well as intrinsic/global central conventions, derived/global reduction, chiral/factorization, Satake, localization, quantization and the global Langlands equivalence, retain their distinct mathematical statements.

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

Equations (K4.1)–(K4.2) in their full generality are **not yet proved in this lesson**. Section 3.2 proves (K4.1) for the rank-one vacuum, including all polynomial generators, ordinary base change and coordinate compatibility. The finite-mode, jet-invariant and filtered arguments for \(\mathfrak{sl}_2\) in §3.2 establish the full rank-one polynomial algebra and coordinate action. Section 3.3 proves the general classical current invariants, the PBW upper bound and unconditional vacuum commutativity. The finite-degree reduction to basic lifts and the determinant construction prove the entire type A polynomial vacuum algebra. Section 3.4 proves the full coordinate-equivariant ordinary disc-oper comparison for every type A factor. Basic lifts and the coordinate comparison in other simple types, and the Satake assertion (K4.2), remain unproved. The geometric route through affine Grassmannian global sections, semi-infinite cohomology and the birth of opers needs its complete argument and foundations. These classical statements are over \(\mathbb C\). The rank-one vacuum-center proof in §3.2 holds over the full characteristic-zero field convention and every ordinary parameter algebra. The type A polynomial vacuum algebra in §3.3.5 and its full ordinary coordinate comparison in §3.4 hold over every characteristic-zero field and ordinary parameter algebra. Section 3.5 proves the reductive vacuum factorization and the full framed central coefficient comparison for type A reductive Lie algebras. Section 3.6 constructs the actual smooth completion, proves the full type A completed center and its coordinate-equivariant ordinary punctured-disc comparison, computes the abelian completed center at every fixed form, and identifies the vacuum restriction kernel. Section 3.7 constructs the intrinsic critical Poisson vertex and completed brackets for every finite-dimensional affine datum and proves the full type A scalar-oper Poisson comparison. The full center/oper-Poisson comparison and completed center in other simple types, intrinsic/global central data, derived/global Hamiltonian reduction, full chiral/factorization, Satake and derived-family center comparisons remain unproved.

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

The adjoint-semisimple argument proves the finite principal decomposition, unique ordinary-family gauge, coordinate cocycle, intrinsic oper classification, global affine parameter space and dimension from its explicit Lie/group and curve premises. It constructs regular and Laurent coefficient functors, including the continuous coordinate action over nilpotent bases. The independent scalar argument supplies intrinsic/scalar equivalence, normalized lifts, theta choices, ordinary-family representability, Schwarzian, nonsplit extension and algebraic irreducibility. The invariant-ring argument supplies characteristic-zero field transfer, arbitrary ordinary coaction base change, the Molien degree identities, a weighted polynomial Kostant section and the graded classical oper/Hitchin ring. The critical argument supplies the ordered basis, formal affine action, invariant/end correspondence and every-mode \(\mathfrak{sl}_2\) check. Section 3.2 proves the full rank-one polynomial vacuum center, current-jet invariant algebra, PBW exhaustion and coordinate-equivariant ordinary projective-connection identification. Section 3.3 proves the general classical current invariants, exact PBW upper bound, ordinary vacuum-invariant base change, coordinate action on symbols and unconditional vacuum commutativity. Its basic-lift reduction and all-n determinant construction prove the entire type A polynomial vacuum algebra over every ordinary parameter algebra. Section 3.4 proves the full ordinary coordinate-equivariant type A disc-oper comparison and the arbitrary-type quadratic coordinate law, with every anomaly and normalization retained. Section 3.5 proves reductive affine-vacuum factorization, all abelian invariants at arbitrary affine form, the trace splitting and whole polynomial vacuum algebra in reductive type A, and their exact framed central coordinate laws. It also proves the ordinary central gauge groupoid and the algebraic cocycle comparison. Section 3.6 constructs the smooth affine completion and proves the full type A and fixed-form abelian centers, with the exact continuous coefficient functor and vacuum kernel. Section 3.7 constructs the intrinsic critical Poisson vertex algebra and jointly continuous completed bracket for every finite-dimensional affine datum, proves the exact ordered Miura embedding and actual affine-to-boson Poisson map in type A, and proves its full coordinate-equivariant scalar-oper Poisson isomorphism. The regular comparison is a Poisson vertex comparison; neither fixed-cutoff nor vacuum restriction is generally an ordinary Poisson quotient. Section 3.8 constructs the ordinary principal matrix Hamiltonian reduction in type A, proves its polynomial gauge quotient, classical affine/free-field normalizer descent and exact forward Miura factors, and identifies both its entire regular scalar Adler PVA and its coordinate-equivariant completed Laurent Poisson algebra. Section 3.9 proves the general principal classical normalizer reduction, its freely generated polynomial regular-jet algebra, full weighted Laurent quotient and jointly continuous all-mode bracket, its normalized ordinary coordinate Poisson action, and the exact quadratic Virasoro and Schwarzian laws for the specified invariant form.

Complete proofs remain required for the recursive root-space/pinning, split-unipotent and faithful adjoint-group constructions, ordinary bundle descent, and the recursive Serre/highest-weight and finite-algebra foundations of the invariant-ring proof; non-type-A basic quantum lifts and the non-type-A coordinate-equivariant vacuum-center/oper comparison, non-type-A completed punctured-disc center and oper-Poisson comparison, derived/global Hamiltonian reduction and full chiral/factorization, Satake and derived-family compatibility, and the geometric/Satake/global central-convention comparison; half-root, uniformization, localization, nonzero specialization, holonomicity, tensor/fusion Hecke property and filtered quantization; full derived opers and full-field/reductive-center passages; and the critical FLE, Ran, factorization, determinant, convergence and \(\operatorname{IndCoh}^{*}/\operatorname{IndCoh}^{!}\) foundations. The fixed-curve Picard/coherent/local-algebra/Ext chains, bundle-stack algebraization and optional analytic comparison retain their explicit earlier unproved foundations. Each is a mathematical theorem or construction whose full proof is still required.

Further reading: [Frenkel, *Lectures on the Langlands program and conformal field theory*, §§8–9](https://arxiv.org/abs/hep-th/0512172v1); [Raskin, *A geometric proof of the Feigin–Frenkel theorem*, introduction](https://arxiv.org/abs/1106.3112v1); [Frenkel–Gaitsgory, *Local geometric Langlands correspondence and affine Kac-Moody algebras*, introduction](https://arxiv.org/abs/math/0508382v3); [Beilinson–Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, §§2.6, 3, 7.8 and 7.14](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf); and [Arinkin, Beraldo, Campbell, Chen, Faergeman, Gaitsgory, Lin, Raskin and Rozenblyum, *Proof of the geometric Langlands conjecture II: Kac-Moody localization and the FLE*, introduction and §3](https://arxiv.org/abs/2405.03648v3).

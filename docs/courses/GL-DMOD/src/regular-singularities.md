# Regular singularities

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A meromorphic change of basis can alter the poles in a connection matrix. Regularity therefore concerns the connection, rather than the appearance of one matrix. A useful basis has only a logarithmic pole; analytically, its horizontal sections grow at most like a power. On an algebraic variety the test includes the points at infinity.

We use left D-modules and the conventions of The de Rham functor. In particular, if $\partial_t e=a(t)e$, a horizontal section $g(t)e$ satisfies $g'+ag=0$. A scalar solution of the defining operator $\partial_t-a(t)$ satisfies $u'=au$ instead. These two functions have opposite exponential signs.

The formal lattice argument works over a characteristic-zero field. Statements involving monodromy, growth or analytic spaces use $\mathbb C$. The formal classification below also uses $\mathbb C$ explicitly. We assume finite rank throughout. We use the existence of holomorphic fundamental matrices on simply connected nonsingular domains from D-modules, flat connections and local systems.

## 1. A lattice that controls all iterated derivatives

Put $R=k[[t]]$, $K=k((t))$. A connection on the punctured formal disc is a finite-dimensional $K$-vector space $V$ with a $k$-linear map $\nabla_{\partial_t}$ satisfying the Leibniz rule. Write
\[
\Theta=t\nabla_{\partial_t},\qquad
\Theta(fv)=t f'v+f\Theta(v).                                      \tag{1.1}
\]
A lattice is a free $R$-submodule $L\subset V$ of rank $\dim_K V$ with $K L=V$.

Here is a definition that makes the lattice criterion substantive. Call the connection **regular singular** if, for some lattice $L_0$, all its iterated logarithmic derivatives remain within a fixed pole bound:
\[
\sum_{m\geq0}R\Theta^m L_0\subset t^{-N}L_0
\quad\text{for some integer }N\geq0.                             \tag{1.2}
\]
This is a boundedness condition, not a bound on the ordinary derivatives $\nabla_{\partial_t}^m$.

**Theorem 1.1 (lattice criterion).** Condition (1.2) holds if and only if $V$ has a lattice $L$ with $\Theta L\subset L$. It then holds for every initial lattice $L_0$.

**Proof.** The sum $H=\sum_{m\geq0}R\Theta^m L_0$ contains $L_0$. Under (1.2) it is an $R$-submodule of the finite free module $t^{-N}L_0$, so it is finitely generated. It is torsion free over the discrete valuation ring $R$, hence free; its rank is $\dim_K V$. Formula (1.1) shows that $\Theta H\subset H$, because $tf'\in R$ for $f\in R$.

Conversely, suppose $L$ is stable. Every lattice $L_0$ is contained in $t^{-a}L$ for some $a\geq0$. Formula
\[
\Theta(t^{-a}v)=t^{-a}(\Theta-a)v                               \tag{1.3}
\]
makes $t^{-a}L$ stable too. Thus the entire hull of $L_0$ stays there. Commensurability gives $t^{-a}L\subset t^{-N}L_0$ for a sufficiently large $N$. This also proves independence of $L_0$. $\square$

In a basis of a stable lattice, write the basis as a row $e$ and
\[
\Theta(e v)=e\bigl(t v'+A(t)v\bigr),\qquad A(t)\in M_r(R).        \tag{1.4}
\]
The connection matrix for $\nabla_{\partial_t}$ is $A(t)/t$. Thus the theorem gives precisely a logarithmic basis. For convergent meromorphic germs the same proof uses $R=\mathbb C\{t\}$ and $K=R[t^{-1}]$, also a discrete valuation ring.

For rank one every lattice is $t^mR e$. If $\nabla_{\partial_t}e=a(t)e$, its logarithmic coefficient in this lattice is $t a(t)+m$. Consequently
\[
V\text{ is regular singular}\quad\Longleftrightarrow\quad
t a(t)\in R.                                                   \tag{1.5}
\]
An integral shift of the residue cannot remove a term $t^{-q}$ with $q\geq2$. Regular connections have regular subconnections and quotients: intersect a stable lattice with the subconnection, or take its image in the quotient. Each is a finite torsion-free lattice, spans the required vector space and remains $\Theta$-stable.

## 2. Constant models and the formal classification

From now through the analytic discussion, $k=\mathbb C$. Choose the strip
\[
\Sigma=\{\alpha\in\mathbb C:0\leq\operatorname{Re}\alpha<1\}.     \tag{2.1}
\]
It supplies one representative of each class in $\mathbb C/\mathbb Z$.

**Lemma 2.1 (normalizing the residue).** Every regular singular formal connection has a stable lattice whose residue eigenvalues lie in $\Sigma$.

**Proof.** Start with a stable lattice and its residue $A(0)$ on $L/tL$. Split this finite-dimensional space into a chosen generalized eigenspace $W$ and the sum $C$ of the others. Lift bases of $W,C$ to $L$. In the resulting block matrix the off-diagonal blocks are divisible by $t$.

Replace the lifts of $W$ by $t$ times those lifts, leaving $C$ unchanged. The new lattice is stable: one off-diagonal block is multiplied by $t$, the other divided by $t$, and the latter remains holomorphic. Its residue is block triangular, with the eigenvalues on $W$ increased by $1$ and those on $C$ unchanged. Replacing the lifts by $t^{-1}$ times themselves gives the analogous downward shift. These are modifications of a whole generalized eigenspace, not a claim that a meromorphic invertible matrix is a scalar power times a holomorphic invertible matrix.

Move each eigenvalue by integral steps toward its representative in $\Sigma$. The sum, with multiplicities, of the absolute integral distances to those representatives decreases at each step. If eigenvalues collide, their representatives coincide, so the new generalized eigenspace can be moved together. The process terminates. $\square$

**Lemma 2.2 (removing the higher terms).** For a lattice as in Lemma 2.1, the connection is formally isomorphic to one with constant matrix $A_0=A(0)$. If the initial matrix is convergent, the isomorphism is convergent meromorphic.

**Proof.** Seek $G(t)=I+\sum_{n\geq1}G_n t^n$ so that the new basis $eG$ has logarithmic matrix $A_0$. This asks for
\[
tG'+A(t)G=GA_0,\qquad
(nI+\operatorname{ad}A_0)G_n
 =-\sum_{i=1}^n A_iG_{n-i},                                    \tag{2.2}
\]
where $\operatorname{ad}A_0(H)=A_0H-HA_0$.
The eigenvalues of this operator are $n+\alpha-\beta$. No difference of two members of $\Sigma$ is a nonzero integer, so they are nonzero for every $n\geq1$. This proves existence and uniqueness recursively, and $G(0)=I$ makes $G$ formally invertible.

For convergence choose a submultiplicative matrix norm. There are constants $C,B>0$ and a radius $\rho>0$ such that
\[
\|(nI+\operatorname{ad}A_0)^{-1}\|\leq C/n,\qquad
\|A_i\|\leq B\rho^{-i}.                                        \tag{2.3}
\]
The first bound follows for large $n$ by a Neumann series and for the remaining finitely many $n$ by increasing $C$. If $g_0\geq\|I\|$ and
$n g_n=CB\sum_{i=1}^n\rho^{-i}g_{n-i}$, then induction gives $\|G_n\|\leq g_n$. The generating series is
$g_0(1-t/\rho)^{-CB}$, by differentiating it. Hence $G$ converges near zero; its determinant is nonzero there. Lemma 2.1 used only finitely many meromorphic basis changes, so the whole change is convergent meromorphic. $\square$

**Theorem 2.3 (formal regular monodromy).** The category of regular singular connections over $\mathbb C((t))$ is equivalent to the category of finite-dimensional complex vector spaces with an invertible automorphism. For a normalized constant model with matrix $A$ the automorphism is
\[
T=\exp(-2\pi i A).                                             \tag{2.4}
\]
Isomorphism classes correspond to conjugacy classes of such $T$.

**Proof.** The lemmas put every object in constant form with spectrum in $\Sigma$. A morphism from the constant model $A$ to $B$ is a meromorphic matrix $H=\sum_{n\geq N}H_n t^n$ satisfying
\[
tH'+BH-HA=0,\qquad (nI+B(\,\cdot\,)-(\,\cdot\,)A)H_n=0.        \tag{2.5}
\]
For $n\neq0$ the operator has eigenvalues $n+\beta-\alpha$, all nonzero. Therefore $H=H_0$ and $BH_0=H_0A$. Thus normalized constant models have exactly the constant intertwining maps.

Given an invertible $T$, decompose its vector space into generalized eigenspaces for eigenvalues $\tau$. Choose the unique $\alpha\in\Sigma$ with $\tau=\exp(-2\pi i\alpha)$. On that block put $U=\tau^{-1}T-I$, a nilpotent operator, and set
\[
A=\alpha I-\frac1{2\pi i}\log(I+U),\qquad
\log(I+U)=\sum_{j\geq1}\frac{(-1)^{j+1}}{j}U^j.                \tag{2.6}
\]
This is a finite sum; its exponential is $T$. A map intertwining two $T$'s preserves the corresponding generalized eigenspaces and intertwines these polynomial logarithms. It therefore intertwines the corresponding $A$'s. Conversely an $A$-intertwiner intertwines its exponential. This proves essential surjectivity and full faithfulness. $\square$

The word monodromy here is a name for the automorphism obtained by the constant model. The formal disc has no analytic loop. Its constant model does have an analytic realization: a horizontal fundamental matrix is $t^{-A}=\exp(-A\log t)$, with actual monodromy (2.4). Formal gauges need not converge for a general formal input.

For example, $A=\alpha I+N$, $N^2=0$, gives
\[
t^{-A}=t^{-\alpha}(I-N\log t),\qquad
T=e^{-2\pi i\alpha}(I-2\pi iN).                                \tag{2.7}
\]
Logarithmic growth and nontrivial unipotent monodromy belong to regular singularities.

## 3. Moderate growth and Fuchs's criterion

A multivalued horizontal section has **moderate growth** if its coefficients in a meromorphic frame satisfy a bound $C|t|^{-N}$ on every closed angular interval of a sufficiently small sector on the universal cover of the punctured disc. The constants may depend on the interval and the section. Meromorphic changes of frame preserve this property, because their entries have finite pole order.

**Theorem 3.1.** A convergent meromorphic connection is regular singular if and only if all its horizontal sections have moderate growth.

**Proof.** In a logarithmic frame, horizontal columns solve $tv'=-A(t)v$. On a fixed radial ray, $\|dv/dr\|\leq C\|v\|/r$ for a uniform bound on $A$. The integral form of this inequality, or Grönwall's inequality with variable $-\log r$, gives
$\|v(r)\|\leq\|v(r_0)\|(r_0/r)^C$. On a compact angular interval the initial values at $r_0$ are bounded, proving moderate growth.

Conversely let $S$ be a horizontal fundamental matrix, with continuation $S\mapsto ST$. Choose a logarithm $A$ with $e^{-2\pi iA}=T$, as in (2.6). The matrix
\[
G(t)=S(t)t^A                                                   \tag{3.1}
\]
is single valued: $T$ commutes with $t^A$, and the two continuation factors cancel. Entries of $t^A$ are powers of $t$ times polynomials in $\log t$, hence moderate. By hypothesis the entries of $S$ are moderate as well. A finite collection of angular intervals covers one turn, giving a uniform polynomial bound for each entry of $G$. A single-valued holomorphic function with this bound becomes bounded after multiplication by a sufficiently large power of $t$, so the removable-singularity theorem makes it meromorphic at zero.

The determinant of $G$ is a nonzero meromorphic germ. The adjugate formula makes $G^{-1}$ meromorphic too. If the original logarithmic matrix was $B(t)$, horizontality of $S$ gives $tG'+BG=GA$. The basis change $G$ therefore produces the constant logarithmic matrix $A$. Its lattice is stable. $\square$

**Corollary 3.2 (completion does not change regularity).** A convergent meromorphic connection is regular singular if and only if its formal completion is regular singular.

**Proof.** Completing a convergent stable lattice gives a formal one. Conversely write the convergent logarithmic matrix in an arbitrary meromorphic frame as $B$, allowing poles. A formal stable lattice has basis matrix $g\in\operatorname{GL}_r(\mathbb C((t)))$ with
$tg'+Bg=gA$, where $A$ is a formal power-series matrix. Choose nonnegative integers $b,c$ so every entry of $B$ has valuation at least $-b$ and every entry of $g^{-1}$ at least $-c$. Truncate $g$ to a Laurent polynomial matrix $G$ with $\Delta=g-G\in t^M M_r(\mathbb C[[t]])$, where $M>b+c$.

Then $g^{-1}\Delta$ has strictly positive valuation, so $G=g(I-g^{-1}\Delta)$ is formally invertible and $G^{-1}$ has entries of valuation at least $-c$. Its convergent determinant is nonzero, hence $G^{-1}$ is convergent meromorphic. The new logarithmic matrix is
\[
G^{-1}(tG'+BG)
=A+G^{-1}\Delta A-G^{-1}(t\Delta'+B\Delta).                    \tag{3.2}
\]
The error terms have valuation at least $M-b-c>0$. Thus the left side, a convergent meromorphic matrix, has no negative Laurent coefficients and is holomorphic. It gives the required convergent lattice. $\square$

**Fuchs's criterion (general statement).** Let
\[
P=\partial_t^n+a_1(t)\partial_t^{n-1}+\cdots+a_n(t),             \tag{3.3}
\]
with convergent meromorphic coefficients. Its connection is regular singular at zero if and only if
\[
t^j a_j(t)\in\mathbb C\{t\}\quad(1\leq j\leq n).                \tag{3.4}
\]
The general result is proved in Schnell's *Algebraic D-modules*, Lecture 20, as Fuchs's theorem, together with the characterization of a regular first-order system by moderate growth and by a logarithmic frame. We give the complete proof for $n=1,2$, as well as sufficiency in every order.

For sufficiency, multiply $P$ by $t^n$. The identities
$t^m\partial_t^m=\Theta(\Theta-1)\cdots(\Theta-m+1)$ rewrite it as a monic polynomial in $\Theta=t\partial_t$, with holomorphic coefficients when (3.4) holds. In its rank-$n$ cyclic differential module, the lattice generated by
$v,\Theta v,\ldots,\Theta^{n-1}v$ is therefore stable. These vectors are a $K$-basis, since the transition from ordinary derivatives is triangular with nonzero diagonal $1,t,\ldots,t^{n-1}$.

For necessity in order one, take a nonzero solution $u$ of $u'+a_1u=0$. It is moderate, by Theorem 3.1 applied to the dual connection, which is regular whenever the original one is: a stable lattice has a stable dual lattice. Its scalar monodromy is some $\tau\neq0$. Choose $\sigma$ with $e^{2\pi i\sigma}=\tau$. Then $u=t^\sigma h$ with single-valued, moderate $h$, hence $h$ is a meromorphic germ. Write $h=t^m h_0$, $h_0$ holomorphic and invertible. It follows that
\[
\frac{u'}u=\frac{\sigma+m}{t}+\frac{h_0'}{h_0}.                 \tag{3.5}
\]
Since $a_1=-u'/u$, its pole is at most simple.

For necessity in order two, choose independent solutions $u,v$ and form
$W=uv'-u'v$. The fundamental companion matrix is invertible, so $W\neq0$. Derivatives of moderate holomorphic functions are moderate on smaller sectors: Cauchy's formula on a circle of radius $c|t|$ loses at most one further power of $|t|$. Thus $W$ is moderate. It has scalar monodromy $\det T_{\rm sol}$, and the same argument as (3.5) shows that $W'/W$ has at most a simple pole. Direct differentiation gives Abel's identity
\[
W'=-a_1W,                                                     \tag{3.6}
\]
so $ta_1$ is holomorphic.

The two-dimensional scalar-solution monodromy has an eigenvector. The corresponding nonzero solution $w$ has scalar monodromy, and hence $w=t^\sigma t^m h_0$ as above. Therefore $w'/w$ has pole order at most one and $w''/w$ at most two. The equation gives
\[
a_2=-\frac{w''}{w}-a_1\frac{w'}w,                              \tag{3.7}
\]
which has pole order at most two. This proves necessity. In order two sufficiency can also be seen directly from
\[
\Theta^2u+(ta_1-1)\Theta u+t^2a_2u=0.                         \tag{3.8}
\]
The scalar system on $(u,\Theta u)^t$ has holomorphic logarithmic matrix
$\left(\begin{smallmatrix}0&1\\-t^2a_2&1-ta_1\end{smallmatrix}\right)$.

The same order-one and order-two criterion holds for formal coefficients over $\mathbb C$. Here is the formal replacement for the growth step, to avoid appealing to analytic functions that may not exist. Theorem 2.3 puts a regular connection and its dual in constant form. Its scalar solutions can consequently be written in a formal differential extension as finite sums of $t^\alpha$ times polynomials in $\ell=\log t$ with coefficients in $\mathbb C((t))$. Differentiate by $\partial_t(t^\alpha)=\alpha t^{\alpha-1}$ and $\partial_t\ell=t^{-1}$. Formal continuation sends $t^\alpha$ to $e^{2\pi i\alpha}t^\alpha$ and $\ell$ to $\ell+2\pi i$.

A scalar eigenvector for continuation has exactly one exponent class modulo integers and no logarithmic powers: a polynomial invariant under a nonzero translation is constant, and distinct exponent classes have distinct continuation eigenvalues. Such a nonzero solution is $t^\sigma h$, $h\in\mathbb C((t))^\times$. For a fundamental order-two companion matrix the determinant $W$ is nonzero and is an eigenvector with eigenvalue the determinant of continuation. Formulas (3.5)–(3.7) apply as formal Laurent identities; $h=t^m h_0$ with $h_0\in\mathbb C[[t]]^\times$. This proves the two necessity bounds formally. Sufficiency already used a formal lattice. In particular, for convergent scalar coefficients of order at most two, formal regularity implies the convergent logarithmic lattice constructed in the sufficiency proof.

## 4. Rank one on the multiplicative line

Let $x$ be the coordinate on $\mathbb G_m$. Its coordinate ring $\mathbb C[x,x^{-1}]$ is a principal ideal domain, so an algebraic line bundle is trivial. Write a connection as
\[
\partial_x e=a(x)e,\qquad a(x)\in\mathbb C[x,x^{-1}].            \tag{4.1}
\]
At zero, (1.5) permits only powers $x^j$ with $j\geq-1$. At infinity put $y=x^{-1}$. Since $\partial_x=-y^2\partial_y$, the coefficient becomes
\[
\partial_y e=-y^{-2}a(y^{-1})e.                                \tag{4.2}
\]
Regularity there permits only $j\leq-1$. Both conditions hold exactly when $a(x)=\lambda/x$.

**Theorem 4.1.** The rank-one algebraic connections on $\mathbb G_m$ regular at both ends are
\[
E_\lambda=\mathcal O_{\mathbb G_m}e_\lambda,\qquad
\partial_xe_\lambda=\frac{\lambda}{x}e_\lambda.                 \tag{4.3}
\]
Two are isomorphic exactly when $\lambda-\mu\in\mathbb Z$.

**Proof.** The classification of coefficients was just proved. An isomorphism $e_\lambda\mapsto g e_\mu$ uses a unit $g=cx^m$ of the Laurent polynomial ring. Connection compatibility says $xg'/g=\lambda-\mu$. Thus $\lambda-\mu=m$; conversely this formula constructs the isomorphism. $\square$

The notation $\mathcal O.x^\lambda$ denotes $E_\lambda$, even when $x^\lambda$ is not an algebraic function. Its horizontal coefficients are $x^{-\lambda}$, so its de Rham monodromy is $e^{-2\pi i\lambda}$. On the punctured line one may write the cyclic presentation $\mathcal D/\mathcal D(x\partial_x-\lambda)$. At the origin, different coherent extensions can share that restriction; Preservation of holonomicity and minimal extensions distinguishes them.

Here are the assigned pole calculations, with connection rather than scalar-solution signs:

| Operator on the punctured line | Coefficient $a(x)$ | Coefficient at infinity | At zero | At infinity |
| --- | --- | --- | --- | --- |
| $x^2\partial_x-x$ | $x^{-1}$ | $-y^{-1}$ | regular | regular |
| $x^3\partial_x-1$ | $x^{-3}$ | $-y$ | irregular | regular |
| $\partial_x-1$ | $1$ | $-y^{-2}$ | nonsingular | irregular |

For the second example a horizontal coefficient is $\exp(1/(2x^2))$, whereas a scalar solution of the operator is $\exp(-1/(2x^2))$. For the third it is $\exp(-x)=\exp(-1/y)$, growing faster than every pole on some sectors at infinity.

If $\mathcal O.e^{1/x}$ means the connection obtained by formally differentiating the symbol $e^{1/x}$, its coefficient is $-x^{-2}$ and it is irregular at zero. Its horizontal coefficient is $e^{-1/x}$. Changing the sign of the exponential changes the growth sectors but not regularity.

**Hypergeometric example.** For parameters $a,b,c\in\mathbb C$, the equation
\[
x(1-x)u''+[c-(a+b+1)x]u'-ab\,u=0                              \tag{4.4}
\]
has regular singularities among $0,1,\infty$. Indeed its monic coefficients are
$a_1=[c-(a+b+1)x]/[x(1-x)]$ and $a_2=-ab/[x(1-x)]$. At $0$ and $1$ the first has at most a simple pole and the second at most a double pole. At infinity the transformed monic coefficients are
\[
\widetilde a_1(y)=\frac2y-\frac{a_1(1/y)}{y^2},\qquad
\widetilde a_2(y)=\frac{a_2(1/y)}{y^4}.                         \tag{4.5}
\]
The estimates $a_1(x)=O(x^{-1})$, $a_2(x)=O(x^{-2})$ give the same Fuchs bounds there. Degenerate parameters may make a singularity removable; the assertion is an upper bound on singularity type.

## 5. Global regularity and regular holonomic modules

For a connection on a smooth algebraic curve $C$, regularity means the formal or convergent logarithmic test at **every** point of its smooth complete compactification $\overline C$. The points of $\overline C\setminus C$ are part of the definition. A flat bundle on a smooth algebraic $X$ is regular if its pullback to every smooth algebraic curve $C\to X$ is regular in this sense. Testing only points already in $X$ would admit $\mathcal O.e^x$ on $\mathbb A^1$ and would give the wrong category.

**Deligne's theorem (statement).** If $X$ is a smooth separated complex algebraic variety, horizontal sections after analytification give an equivalence
\[
\operatorname{Conn}_{\rm reg}(X)
\ \simeq\ \operatorname{Loc}_{\rm fd}(X^{\rm an}).               \tag{5.1}
\]
Morphisms on the left are algebraic connection maps. On the right are finite-rank complex local systems. The equivalent compactification criterion says that, on a smooth complete compactification with normal crossing boundary, the meromorphic connection is regular along that boundary. The criterion is independent of compactification.

These are the connection correspondence and curve criterion of Deligne, *Équations différentielles à points singuliers réguliers*, LNM 163, proved there in Chapter II, §§4–5. We state the global theorem here. Locally, Theorems 2.3 and 3.1 explain how regularity lets monodromy reconstruct a meromorphic connection.

Now use finite length and the description of simple holonomic modules from the preceding lesson. A holonomic module is **regular holonomic** if every composition factor can be presented as the minimal extension $j_{!*}E$ of an irreducible regular connection on a smooth locally closed subvariety with affine inclusion. The zero module is regular. This is the definition in the lecture “Holonomic D-modules with regular singularities” of Bernstein's *Algebraic theory of D-modules*; for a module that is itself a connection, that definition is regularity along every curve, the preceding definition. It concerns algebraic regularity at infinity.

Write $D^b_{\rm rh}(\mathcal D_X)$ for bounded complexes with regular holonomic cohomology. This is a triangulated subcategory: a composition series for a submodule and quotient concatenates to one for the middle module. Thus regular modules form a Serre subcategory, and the long cohomology sequence of a triangle preserves it.

**Stability and testing (statements).** For a morphism $f:X\to Y$ of smooth separated complex algebraic varieties, the four functors
\[
f_*,\ f_!,\ f^!,\ f^*
\]
of Adjunctions, base change and the projection formula, and holonomic duality $\mathbb D$, preserve the bounded regular holonomic categories. No properness hypothesis is imposed in this algebraic statement. A bounded holonomic complex $M$ on $X$ is regular if and only if $k^!M$ is regular for every map $k:C\to X$ from a smooth algebraic curve. It is enough to test smooth locally closed curves. These are Main Theorem B in Bernstein's *Algebraic theory of D-modules*, which uses the same notation $f^!$ and $f^*$. The corresponding analytic direct-image theorem requires properness; see Kashiwara, *The Riemann–Hilbert problem for holonomic systems*, §8.

For completeness, the tensor operations used with these statements also stay regular. Here is how they reduce to the stated curve criterion. External products of holonomic modules are holonomic: a product good filtration has associated graded the external product of the two associated graded modules, so its characteristic support is the product of the two Lagrangian supports. The dimension is the sum of the dimensions. Derived external products and tensor products are consequently holonomic by bounded dévissage and the already proved inverse-image theorem; the internal tensor is the diagonal inverse image with its dimension shift.

On a curve, two regular holonomic complexes restrict outside finitely many points to complexes of regular connections. A tensor of two regular connections is regular, since tensor products of logarithmic lattices are logarithmic lattices, including at the compactification boundary. Every simple factor supported at an omitted point is a delta module and is regular. The simple-factor description therefore shows that the tensor complex is regular on the whole curve. Restrictions to a dense open detect the positive-dimensional simple factors, and any such factor with nonzero restriction inherits a regular generic connection by the stable sublattice and image argument following (1.5).

For an arbitrary curve map $k:C\to X\times Y$, the transfer-module tensor identity gives
\[
k^!(M\boxtimes N)\simeq
(\operatorname{pr}_X k)^!M\otimes^!
(\operatorname{pr}_Y k)^!N.                                   \tag{5.2}
\]
Both factors are regular by the stated inverse-image theorem, and their tensor is regular by the curve argument. The curve criterion makes $M\boxtimes N$ regular. Pulling back along the diagonal now proves regularity of $\otimes^!$ on $X$. This supplies the tensor part of the six-operation package, together with its dual tensor/Hom operation defined using $\mathbb D$. Recall that for left modules $\otimes^!$ is the derived $\mathcal O_X$ tensor shifted by $[-\dim X]$; shifts do not affect regularity.

For instance, $\mathcal O_{\mathbb A^1}$ and $\mathcal O.e^x$ both have zero-section characteristic variety. The first is regular algebraically and the second is not. Characteristic variety records the cotangent directions of propagation, not the exponential rate at infinity.

## 6. What monodromy misses in the irregular world

Consider $\partial_t e=t^{-2}e$. A horizontal coefficient is $e^{1/t}$; its ordinary monodromy is trivial. The trivial connection also has trivial monodromy, but (1.5) proves these meromorphic connections are not isomorphic. For $t=r e^{i\theta}$,
\[
|e^{1/t}|=\exp(\cos\theta/r).                                  \tag{6.1}
\]
It decays in one half-plane and grows faster than every power in the other. The rays $\theta=\pm\pi/2$ separate those growth regimes. This rank-one example has no nontrivial Stokes gluing matrix: it displays the exponential rate that ordinary monodromy forgets.

For higher rank, formal exponential decompositions can be realized by different analytic gauges on different sectors. Their transition maps carry additional Stokes data. The irregular Riemann–Hilbert problem reconstructs the meromorphic connection from enhanced topological data that retain those asymptotic distinctions. This paragraph is a description of the problem, not a proof of a classification theorem.

Deligne, in letters to Malgrange of the late 1970s, organized boundary directions by the relative exponential growth rates and proposed the associated filtered local system. Sabbah's [*Introduction to Stokes structures*](https://arxiv.org/abs/0912.2762), Lectures 1–2, develops these Stokes-filtered local systems in dimension one.

Scholze's [*Wild Betti sheaves*, §1](https://arxiv.org/abs/2505.24599), describes a universal enlargement of ordinary Betti sheaves with an exponential object and a Fourier equivalence. It recovers a construction of Tamarkin, also expressed through enhanced sheaves, and relates it to the irregular Riemann–Hilbert correspondence. The enlargement changes the coefficient category so that exponential information survives. We cite this construction as a modern framework; we do not identify ordinary finite-rank local systems with arbitrary irregular connections, or claim that this note alone proves the whole irregular correspondence.

## 7. Exercises with complete solutions

**Exercise 13.1 (easy).** Decide regularity at zero and infinity for $x\partial_x-\lambda$, $x^2\partial_x-1$, and $x^3\partial_x-x$.

**Solution.** On the punctured line their coefficients are respectively $\lambda/x$, $x^{-2}$ and $x^{-2}$. At zero the first has at most a simple pole, and the other two have double poles. They are respectively regular, irregular, irregular. Under (4.2) the coefficients are $-\lambda/y$, $-1$, $-1$, so all three are regular at infinity, with the last two nonsingular there. The last two define the same punctured connection; the statement does not identify their coherent extensions at zero.

**Exercise 13.2 (easy).** Show that $\mathcal O.e^x$ is irregular at infinity.

**Solution.** The formal symbol has $\partial_xe=e$. In the coordinate $y=x^{-1}$, $\partial_ye=-y^{-2}e$. Any rank-one lattice is $y^m\mathbb C[[y]]e$, with logarithmic coefficient $m-y^{-1}$. None is stable, so Theorem 1.1 proves irregularity. Analytically the horizontal coefficient $e^{-1/y}$ has exponential growth on sectors about the negative real $y$ axis, so Theorem 3.1 gives the same conclusion.

**Exercise 13.3 (medium).** Prove the second-order Fuchs criterion.

**Solution.** If $ta_1$ and $t^2a_2$ are holomorphic, (3.8) makes $\mathbb C\{t\}v+\mathbb C\{t\}\Theta v$ a stable lattice in the cyclic rank-two module. Conversely regularity makes the dual scalar solutions moderate. Their nonzero Wronskian $W$ is moderate and has scalar monodromy, so $W=t^\rho h$ with $h$ meromorphic. Its logarithmic derivative has at most a simple pole. Abel's identity $W'=-a_1W$ proves the first bound. A monodromy eigen-solution $w=t^\sigma g$, $g$ meromorphic and nonzero, has $w'/w$ of pole order at most one and $w''/w$ of order at most two. Dividing $Pw=0$ by $w$ gives (3.7), proving the second bound. Shrink the disc so the meromorphic unit factors have no zeros. For formal coefficients, use the continuation eigen-solutions and Laurent valuations constructed after (3.8); the same identities prove both bounds.

**Exercise 13.4 (medium).** Exhibit the isomorphism $E_\lambda\simeq E_{\lambda+1}$.

**Solution.** Define $e_\lambda\mapsto x^{-1}e_{\lambda+1}$. Indeed
\[
\partial_x(x^{-1}e_{\lambda+1})
=-x^{-2}e_{\lambda+1}+(\lambda+1)x^{-2}e_{\lambda+1}
=\lambda x^{-2}e_{\lambda+1}.
\]
Its inverse sends $e_{\lambda+1}$ to $x e_\lambda$. Both coefficients are units on $\mathbb G_m$. They need not be units on $\mathbb A^1$, so the formula alone does not identify extensions across zero.

**Exercise 13.5 (hard).** Classify regular singular connections on the punctured formal disc by pairs $(V,T)$ with $T\in\operatorname{GL}(V)$, up to conjugacy. Specify the field.

**Solution.** Work over $\mathbb C((t))$. A stable lattice exists by Theorem 1.1. Shift residue generalized eigenspaces by powers of $t$ until their eigenvalues lie in $\Sigma$; Lemma 2.1 proves stability and termination. Solve recurrence (2.2), whose operators are invertible, to remove all positive powers of $t$ from the matrix. Assign to the resulting constant model $(V,A)$ the automorphism $e^{-2\pi iA}$.

For any prescribed invertible $T$, its generalized eigenblocks and the finite nilpotent logarithm (2.6) construct a normalized $A$. Formula (2.5) proves that all morphisms between normalized constant models are constant intertwiners. Polynomial logarithms on the $T$-blocks prove that these are exactly the $T$-intertwiners. The constructions are therefore inverse equivalences, not merely a list of objects. Changing a basis conjugates $T$, and a conjugacy gives an isomorphism of connections. A formal connection over a general characteristic-zero field does not acquire a complex topological monodromy without additional choices or field extension; the stated classification uses the complex field.

## What this lesson does not prove

We do not prove necessity in the general-order Fuchs criterion; Schnell's *Algebraic D-modules*, Lecture 20, proves it. We state Deligne's global connection correspondence and compactification criterion, proved in Chapter II of Deligne's *Équations différentielles à points singuliers réguliers*. We also use the identification of regular connections with the regular holonomic modules that are connections, and state the duality, four-map stability and curve-testing theorems, Main Theorem B in Bernstein's *Algebraic theory of D-modules*. The tensor closure was deduced from those results.

The Stokes description, the irregular Riemann–Hilbert problem and the wild Betti construction are cited perspectives. We prove no formal exponential decomposition, sectorial summation or irregular correspondence theorem. The analytic prerequisites used in our local proofs are fundamental matrices for nonsingular holomorphic systems, Cauchy's formula, the removable-singularity theorem and Grönwall's inequality.

## References

- Bernstein, [*Algebraic theory of D-modules*](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), lecture notes, the lecture “Holonomic D-modules with regular singularities”: the definition of regular holonomic modules and Main Theorem B, stability under the four functors and duality and the curve criterion.
- Kashiwara, [*The Riemann–Hilbert problem for holonomic systems*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/RiemannHilbert.pdf), Publications of the RIMS 20 (1984), 319–365, §8: regularity of proper direct images of analytic regular holonomic modules.
- Deligne, [*Équations différentielles à points singuliers réguliers*](https://publications.ias.edu/sites/default/files/Number9.pdf), Lecture Notes in Mathematics 163, Springer, 1970, Chapter II: regularity in dimension one and in higher dimension, the curve and compactification criteria, and the global connection correspondence.
- Schnell, [*Algebraic D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Lectures 20–21: Fuchs's theorem and regular first-order systems, and the regularity-at-infinity examples and definitions.
- Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), §3.5, for the Euler D-module and its scalar solutions.
- Sabbah, [*Introduction to Stokes structures*](https://arxiv.org/abs/0912.2762), Lectures 1–2: Stokes-filtered local systems in dimension one, following Deligne and Malgrange.
- Scholze, [*Wild Betti sheaves*](https://arxiv.org/abs/2505.24599), arXiv:2505.24599, §1, for the exponential and Fourier enlargement and its enhanced-sheaf context.

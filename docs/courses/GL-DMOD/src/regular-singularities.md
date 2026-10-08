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

**Lemma 1.0 (lattice algebra).** In either $R=k[[t]]$ or $R=\mathbb C\{t\}$, every submodule of a finite free module is finite free. A finite free $R$-submodule of $K^r$ whose $K$-span is $K^r$ is a lattice. Any two lattices in the same $K$-vector space contain one another after multiplication by sufficiently large powers of $t$.

**Proof.** Every nonzero series is $t^m u$ with $u$ a unit: the inverse of a series with nonzero constant term is obtained recursively in the formal case, and by a convergent geometric series in the analytic case. In a nonzero ideal choose an element $a$ of least valuation. Every other element divided by $a$ belongs to $R$, so the ideal is $Ra$.

For a submodule $N\subset R^r$, project to the first coordinate. If the image is $Ra\ne0$, choose $w\in N$ projecting to $a$. Subtracting a unique multiple of $w$ from any element gives
$N=Rw\oplus\ker(N\to R)$, and the kernel is a submodule of $R^{r-1}$. If the image is zero, $N$ itself lies in $R^{r-1}$. Induction on $r$ proves the assertion, including finite generation. Its free rank is the dimension of its $K$-span, since the resulting basis stays independent after allowing denominators. Finally, express a basis of one lattice in a basis of the other. There are finitely many coefficients in $K$, and their valuations have a common lower bound. Clearing their poles gives one inclusion; exchanging the bases gives the other. $\square$


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

### 3.1. Fuchs's criterion in every order

**Theorem 3.3 (Fuchs's criterion).** Let
\[
P=\partial_t^n+a_1(t)\partial_t^{n-1}+\cdots+a_n(t),             \tag{3.3}
\]
with convergent meromorphic coefficients. Its connection is regular singular at zero if and only if
\[
t^j a_j(t)\in\mathbb C\{t\}\quad(1\leq j\leq n).                \tag{3.4}
\]
The same assertion holds for formal coefficients over any characteristic-zero field $k$, with $\mathbb C\{t\}$ in (3.4) replaced by $k[[t]]$. The proof below treats both rings. In particular, neither an analytic solution basis nor a restriction on exponents is needed for the formal statement.

**Proof.** Write $R=\mathbb C\{t\}$ or $k[[t]]$, and let $K$ be its fraction field. Put $D=\nabla_{\partial_t}$ and $\Theta=tD$. The cyclic connection defined by $P$ has generator $v$ and $K$-basis $v,Dv,\ldots,D^{n-1}v$. To see this directly, divide operators by the monic $P$ on the left: subtracting the appropriate left multiple cancels the highest derivative and decreases the order. A nonzero left multiple of $P$ has order at least $n$, since its highest coefficient cannot cancel. Thus the remainder of order below $n$ is unique.

Set $F_0(z)=1$ and $F_m(z)=z(z-1)\cdots(z-m+1)$. The Leibniz rule gives
\[
(\Theta-m)t^mD^m=t^{m+1}D^{m+1},\qquad
t^mD^m=F_m(\Theta).                                           \tag{3.4a}
\]
The second identity follows by induction from the first. Consequently $v,\Theta v,\ldots,\Theta^{n-1}v$ are a $K$-basis too: their transition from the ordinary derivatives is triangular with diagonal $1,t,\ldots,t^{n-1}$. With $\alpha_i=t^i a_i$, multiplication of the defining relation by $t^n$ gives
\[
t^nP=F_n(\Theta)+\sum_{i=1}^n\alpha_i F_{n-i}(\Theta),\qquad
(t^nP)v=0.                                                    \tag{3.4b}
\]
All coefficients here are placed on the left. If every $\alpha_i$ belongs to $R$, this monic relation expresses $\Theta^n v$ in the $R$-span of the preceding powers. The Leibniz rule and $tf'\in R$ then make
$Rv+R\Theta v+\cdots+R\Theta^{n-1}v$ a stable lattice. Theorem 1.1 proves sufficiency.

Conversely, let the connection be regular singular. Theorem 1.1 supplies a stable lattice $L$. Choose $q\geq0$ with $v\in t^{-q}L$; formula (1.3) shows that this enlarged lattice remains stable. Consider the algebraic span
\[
H=\sum_{m\geq0}R\Theta^m v\ \subset\ t^{-q}L.                 \tag{3.4c}
\]
Every element of the sum has finitely many terms. Lemma 1.0 makes $H$ finite free, even though its displayed generating family is infinite. It contains a $K$-basis of the connection, so its rank is $n$. The formula
$\Theta(f\Theta^m v)=tf'\Theta^m v+f\Theta^{m+1}v$ proves that it is stable. Also $\Theta(th)=t(\Theta h+h)$, and $tf'\in tR$. Therefore $\Theta$ induces a $k$-linear operator $\overline\Theta$ on $H/tH$, whose dimension is $n$; in the analytic case the residue field is $\mathbb C$.

The image $\overline v$ generates $H/tH$ under $\overline\Theta$. Its first $n$ iterates form a basis. Indeed, if the first dependence occurred at degree $d<n$, it would express the $d$-th iterate in the preceding ones and make their span invariant. All later iterates would remain in that space of dimension at most $d$, contradicting cyclic generation of the $n$-dimensional quotient. This also rules out $\overline v=0$.

In any $R$-basis of $H$, the coordinate matrix of $v,\Theta v,\ldots,\Theta^{n-1}v$ thus has invertible reduction modulo $t$. Its determinant is a unit, so the adjugate formula gives an inverse over $R$. These vectors are an $R$-basis of $H$ itself. In particular there are $b_i\in R$ such that
\[
Qv=0,\qquad
Q=\Theta^n+b_1\Theta^{n-1}+\cdots+b_n.                        \tag{3.4d}
\]
Both $Q$ and the expression (3.4b) are monic of degree $n$ in $\Theta$ and annihilate $v$. Their difference has degree below $n$; independence of the first $n$ iterates over $K$ makes every coefficient of that difference zero.

It follows that $Q-F_n(\Theta)=\sum_i\alpha_iF_{n-i}(\Theta)$ has coefficients in $R$. Its coefficient of $\Theta^{n-1}$ is $\alpha_1$, so $\alpha_1\in R$. After subtracting $\alpha_1F_{n-1}(\Theta)$, its coefficient of $\Theta^{n-2}$ is $\alpha_2$ when $n\geq2$. Repeating the subtraction and coefficient comparison proves $\alpha_i\in R$ for every $i$, including zero coefficients. This uses monic polynomials with integer coefficients and left coefficient placement, so it introduces no derivatives of the $\alpha_i$. These are exactly the bounds (3.4). $\square$

For convergent meromorphic coefficients, formal regularity is therefore equivalent to the same bounds: a convergent Laurent series with no negative coefficients is holomorphic. The stable lattice in the sufficiency proof is then convergent. This gives the completion assertion for scalar equations in every order, consistent with Corollary 3.2. Schnell's free lecture notes, Lecture 20, are supplementary reading for Fuchs's theorem.

### 3.2. Low-order solution calculations

The preceding proof covers every order. The following analytic and formal computations give additional descriptions in orders one and two.

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

### Canonical logarithmic extensions

The flat-connection/local-system equivalence used here is proved in D-modules, flat connections and local systems, Lemma 4.1 and Theorem 4.2. The parameter Cauchy and Taylor facts are proved in Cauchy's theorem for cycles, Lemma 0.1 and Theorems 2.3, 3.2 and 4.2 and Holomorphic functions of several variables, Theorems 1.2, 2.1 and 2.3. The Laurent, growth, finite-dimensional logarithm and category-gluing arguments needed below are proved explicitly.

#### Normalization and the local theorem

Let \(\overline U\) be a complex manifold, \(D\) a reduced divisor locally given by a product of distinct coordinate functions, and \(j:U=\overline U\setminus D\hookrightarrow\overline U\). This includes a simple normal-crossing boundary; no global ordering of its components is needed. Put
\[
\Sigma=\{\alpha\in\mathbb C:0\leq\operatorname{Re}\alpha<1\}.
\tag{5.0a}
\]
We use the connection convention \(\nabla=d+\Gamma\); for a constant residue \(A\), horizontal coefficients are \(z^{-A}\) and positive-loop monodromy is \(\exp(-2\pi iA)\).

A logarithmic lattice is a locally free finite-rank \(\mathcal O_{\overline U}\)-module \(E\) in a meromorphic flat bundle, spanning it after allowing poles along \(D\), with
\[
\nabla E\subset E\otimes\Omega^1_{\overline U}(\log D).
\]
Its residue along a local component \(D_i=(z_i=0)\) is the coefficient of \(dz_i/z_i\) restricted to \(D_i\). Call it normalized if the eigenvalues of every residue lie in \(\Sigma\).

**Theorem 5.0 (canonical logarithmic extension).** Every finite-rank complex local system \(L\) on \(U\) has a normalized logarithmic extension \((E_\Sigma(L),\nabla)\) on \(\overline U\), with restriction identified with \((\mathcal O_U\otimes_\mathbb C L,d\otimes1)\). This extension is unique up to the unique horizontal isomorphism inducing that identification. It is functorial and exact.

Every horizontal map on \(U\) between logarithmic bundles extends uniquely meromorphically across \(D\). Between normalized bundles it extends holomorphically. Consequently restriction identifies the category of regular meromorphic flat bundles on \((\overline U,D)\), defined locally by logarithmic lattices, with finite-rank local systems on \(U\). The local logarithmic criterion is equivalent to regular singularity on every holomorphic disc meeting the boundary and not contained in it; testing transverse coordinate-disc families already suffices.

The construction includes every Jordan block. The normalization functor is generally not tensor compatible. The meromorphic correspondence does preserve the usual tensor constructions.

**Proof.**

#### Topology of the punctured polydisc

An adapted local chart is
\[
V=\Delta^{k}\times\Delta^{m},\quad
D\cap V=(z_1\cdots z_k=0),\quad
V^*=(\Delta^*)^k\times\Delta^m.
\tag{5.0b}
\]
Radial contraction of each punctured disc to a circle and contraction of the other discs to their centers reduce its fundamental group to that of a product of \(k\) circles. More explicitly, the logarithmic covering has domain
\[
\{\operatorname{Re}w_i<\log\rho\}_{1\leq i\leq k}\times\Delta^m,
\qquad z_i=e^{w_i}.
\]
This domain is convex and simply connected, and its deck transformations are \(w_i\mapsto w_i+2\pi in_i\), \(n_i\in\mathbb Z\). A loop lifts with endpoint differing by one such integer tuple; homotopies preserve it. Conversely equal endpoint tuples give homotopic lifts by contraction in the convex domain. Thus \(\pi_1(V^*)=\mathbb Z^k\), with the positive coordinate loops as generators.

A local system is trivial on this cover. To verify the usual continuation assertion, subdivide a path into finitely many intervals lying in trivializing opens and compose their constant transition maps. Refinements give the same map. Subdivide a homotopy square into rectangles lying in trivializing opens; transition cancellations on each rectangle show homotopy invariance. A simply connected cover then identifies every fibre with a fixed one by path continuation. Deck continuation gives a representation of \(\mathbb Z^k\), and conversely its constant deck gluing gives a local system. Maps are precisely fibre maps commuting with the representation.

Hence \(L|_{V^*}\) is specified by a finite vector space \(W\) and commuting invertible maps \(T_1,\ldots,T_k\). Its rank is \(\dim W\), including rank zero.

The holomorphic flat-bundle part has an exact earlier proof, rather than an assumed analytic existence theorem. In lesson 02's proof the iterated integrals for \(\partial_zH=-A(z,w)H\), \(H(0,w)=I\), are bounded by \(C^n|z|^n/n!\); they converge with parameters and uniqueness follows by iterating the same estimate. The determinant satisfies a scalar equation and never vanishes. Killing the first matrix makes the other matrices independent of that coordinate by zero curvature, so induction gives a horizontal frame. Constant transitions then give the equivalence with local systems. We use that proved equivalence on \(V^*\) and on overlaps.

#### Commuting logarithms with all nilpotent parts

For an invertible \(T\) on a finite complex vector space, decompose into its generalized eigenspaces \(W_\tau\), \(\tau\ne0\). The decomposition and its projectors are polynomial in \(T\): the relatively prime factors \((t-\tau)^{r_\tau}\) of an annihilating polynomial admit Bézout projectors by the Euclidean algorithm. Evaluating those projectors at \(T\) gives their direct-sum images and the nilpotent restrictions.

For each \(\tau\), choose the unique \(\alpha_\tau\in\Sigma\) satisfying
\(\exp(-2\pi i\alpha_\tau)=\tau\). The kernel of the scalar exponential here is \(\mathbb Z\): its modulus first forces the imaginary part to be zero, then its argument forces an integer. This proves existence and uniqueness after shifting the real part by an integer.

On \(W_\tau\), put
\[
N_\tau=\tau^{-1}T-I,\qquad
A(T)=\alpha_\tau I-\frac1{2\pi i}
\sum_{a=1}^{r_\tau-1}\frac{(-1)^{a+1}}aN_\tau^a.
\tag{5.0c}
\]
The sum is finite. The formal identity \(\exp(\log(1+t))=1+t\), modulo \(t^{r_\tau}\), proves \(\exp(-2\pi iA(T))=T\). One elementary verification of that identity is to differentiate the formal exponential: it satisfies \(F'=F/(1+t)\), \(F(0)=1\); coefficient recursion gives \(F=1+t\). Truncation is legitimate because \(N_\tau\) is nilpotent. Its residue eigenvalues are the \(\alpha_\tau\).

Using the polynomial projectors, (5.0c) is a polynomial in \(T\) on the whole space. If a map \(C:W\to W'\) intertwines \(T,T'\), it preserves matching generalized eigenspaces and intertwines each finite nilpotent logarithm. Therefore
\[
A(T')C=CA(T).
\tag{5.0d}
\]
This assertion remains true across changes of rank and along exact sequences.

Set \(A_i=A(T_i)\). Since these are polynomials in pairwise commuting \(T_i\),
\[
[A_i,A_j]=0,\qquad \exp(-2\pi iA_i)=T_i.
\tag{5.0e}
\]
No diagonalizability assumption occurs. If \(T_i\) is unipotent, all its \(\alpha\)'s are zero and \(A_i\) is nilpotent. On a simultaneous generalized eigenblock, the horizontal coefficients are scalar powers of the \(z_i\) times polynomials in their logarithms. Each individual nilpotent exponential terminates, and their commuting product is still a finite polynomial in all the logarithms.

#### The local model and intrinsic residues

On \(V\), take
\[
E=\mathcal O_V\otimes_\mathbb CW,\qquad
\nabla=d+\sum_{i=1}^k A_i\,\frac{dz_i}{z_i}.
\tag{5.0f}
\]
Its curvature is zero: the logarithmic forms are closed and (5.0e) kills their matrix commutators. Its residues are the \(A_i\) and have spectrum in \(\Sigma\). A horizontal fundamental matrix on the logarithmic cover is
\[
S(z)=\exp\!\left(-\sum_{i=1}^kA_i\log z_i\right).
\tag{5.0g}
\]
Continuation around the \(i\)-th positive loop sends \(S\) to \(ST_i\). Thus its horizontal local system is the given one. A branch-dependent constant normalization at the chosen base point identifies the fibres; changing that identification conjugates the matrices and gives the same identified flat bundle.

A monodromy intertwiner \(C\) is a constant horizontal map between these local models by (5.0d). Short exact sequences of representations give short exact sequences of the bundles (5.0f), since their underlying bundles are \(\mathcal O_V\otimes W\). Polynomial logarithms restrict and descend to subrepresentations and quotients, so their connections are the induced ones. This proves local functoriality and exactness.

For an arbitrary logarithmic connection in a local frame write
\[
\Gamma=\sum_{i=1}^k B_i(z,w)\frac{dz_i}{z_i}
+\sum_{a=1}^m C_a(z,w)\,dw_a,
\tag{5.0h}
\]
where all matrix coefficients are holomorphic. Zero curvature gives
\[
z_i\partial_iB_j-z_j\partial_jB_i+[B_i,B_j]=0.
\]
Restricting to \(z_i=z_j=0\) shows that its residue endomorphisms commute on every intersection of those components. The residues are intrinsic: replacing \(z_i\) by \(u_i z_i\), with \(u_i\) a holomorphic unit, changes \(d\log z_i\) by the holomorphic form \(d\log u_i\). Frame changes conjugate their restrictions. Thus residue normalization is unchanged by adapted-coordinate choices and by permuting local components.

#### Finite poles from growth and transverse families

**Lemma 5.0.1 (all boundary directions).** A horizontal map \(F:E_1|_{V^*}\to E_2|_{V^*}\) between two logarithmic bundles has, in their local holomorphic frames, a bound
\[
\|F(z,w)\|\leq C\prod_{i=1}^k|z_i|^{-N}
\tag{5.0i}
\]
on a smaller polydisc, uniformly for all arguments of the single-valued \(F\) and for \(w\) in a smaller closed polydisc.

**Proof.** The Hom connection has logarithmic coefficient
\(H\mapsto B_iH-HA_i\), whose norm is uniformly bounded on the closed polydisc. Horizontality on a fixed radial line gives a linear equation with coefficient norm at most \(c_i/r_i\). With \(s=\log(r_0/r_i)\), the integral inequality is \(g(s)\leq g(0)+c_i\int_0^s g(u)\,du\). Iterating the integral inequality gives \(g(s)\leq g(0)e^{c_i s}\): the \(n\)-fold integrals are bounded by \(s^n/n!\), and the remainder tends to zero on each finite interval. Thus varying the \(i\)-th radius multiplies the bound by at most \((r_0/r_i)^{c_i}\).

Start on the compact product torus \(|z_i|=r_0\), with the smaller parameter polydisc. The holomorphic map \(F\) is bounded there. Vary the radii successively, keeping all other coordinates fixed. The coefficient bounds include the simultaneous intersections, so the same estimates hold at every step. Choose one integer \(N\geq\max c_i\) and absorb the fixed \(r_0\)'s into \(C\). This proves (5.0i). No relation between the rates at which different \(z_i\) approach zero was imposed. \(\square\)

**Lemma 5.0.2 (growth means an actual finite pole).** A single-valued holomorphic function on \(V^*\) satisfying (5.0i) belongs to
\(\mathcal O_V[(z_1\cdots z_k)^{-1}]\).

**Proof.** The Laurent formula being used follows directly from the proved Cauchy cycle formula: on a closed annulus, subtract the inner-circle Cauchy integral from the outer-circle integral. For a point strictly between them, expand the outer kernel as \(\sum_{n\ge0}z^n\zeta^{-n-1}\) and the inner kernel as \(-\sum_{n<0}z^n\zeta^{-n-1}\). Both geometric series converge uniformly on compact subannuli; termwise integration gives the Laurent series. Applying the cycle formula to the intervening annulus makes each coefficient independent of its contour radius. The parameter-integration and polydisc Cauchy proofs make the coefficients holomorphic in the other variables and justify iterating in the \(k\) punctured coordinates.

Multiply by \((z_1\cdots z_k)^N\). The result is bounded. Iterated Cauchy integrals on coordinate tori give its Laurent coefficients, holomorphic in the ordinary parameters. For a coefficient with negative exponent in \(z_i\), move that contour radius to zero while holding the others fixed. Its estimate contains a positive power of that radius, so the coefficient is zero. All remaining exponents are nonnegative. On a smaller polydisc their Cauchy bounds give a normally convergent power series, whose restriction is the original Laurent expansion. Hence it is holomorphic across all components and their intersections. This also proves the bounded-removal assertion jointly in all variables. \(\square\)

We will also use the following uniform finite-pole test, which requires no a priori growth estimate.

**Lemma 5.0.3 (transverse-family test).** Let \(f(t,w)\) be holomorphic on \(\Delta^*\times W\), with \(W\) a connected product of punctured and ordinary discs. Suppose that for every \(w\) in some nonempty open subset of \(W\), \(f(\,\cdot\,,w)\) is meromorphic at zero. Then there is one \(N\) such that its Laurent coefficients below degree \(-N\) vanish identically on \(W\).

**Proof.** The Laurent coefficients \(a_q(w)\), computed on one fixed \(t\)-circle, are holomorphic. Let
\[
F_N=\{w:a_q(w)=0\text{ for all }q<-N\}.
\]
These are closed sets. Their union contains the specified open subset. The elementary Baire argument gives one \(F_N\) with interior in it. Here that argument needs only Euclidean completeness: if all the closed sets had empty interior, choose nested closed balls of radii tending to zero, the \(N\)-th avoiding \(F_N\), each in the interior of the preceding ball and in the initial open set. Their centers form a Cauchy sequence; its limiting point lies in every ball and outside every \(F_N\), a contradiction.

Each \(a_q\), \(q<-N\), now vanishes on an open subset, hence on connected \(W\) by the holomorphic identity theorem. That theorem can be verified by Taylor expansion: the locus where a holomorphic function vanishes on a neighbourhood is open, and is closed along connected coordinate domains because all Taylor derivatives vanish at a limit of such points. Thus those coefficients vanish identically. \(\square\)

Apply Lemma 5.0.3 separately to each punctured coordinate of a function on \(V^*\). If its restrictions in every coordinate are meromorphic for a nonempty open parameter family, one obtains bounds \(N_i\) on all negative Laurent exponents. Multiplication by \(\prod z_i^{N_i}\) leaves only nonnegative multi-exponents. Fixed outer-torus Cauchy bounds make that power series converge jointly on a smaller polydisc, including the intersections. This proves meromorphic extension there.

#### Meromorphic maps and normalized uniqueness

Lemma 5.0.1 and Lemma 5.0.2 prove that every horizontal map between logarithmic bundles extends meromorphically. Its connection equation remains true after extension: it is a meromorphic identity already true on the dense open complement of \(D\). Such an extension is unique, since a meromorphic function zero on that open set is zero.

Now suppose both bundles are normalized. If an extended matrix \(F\) had a pole of positive order \(q\) along \(z_i=0\), let \(F_{-q}\) be its nonzero leading Laurent coefficient. Work first away from the other components, where this is an ordinary divisor Laurent expansion with holomorphic parameter coefficients. The horizontal equation is
\[
z_i\partial_iF+B_iF-FA_i=0.
\]
Its leading coefficient gives
\[
(-qI+B_i|_{D_i}(\,\cdot\,)-(\,\cdot\,)A_i|_{D_i})F_{-q}=0.
\tag{5.0j}
\]
The displayed Sylvester operator has eigenvalues \(-q+\beta-\alpha\), where \(\alpha,\beta\in\Sigma\) are residue eigenvalues. None is zero: the real part of \(\beta-\alpha\) lies strictly between \(-1\) and \(1\), whereas \(q\) is a positive integer.

This eigenvalue assertion includes all nilpotent parts. Decompose the source and target into generalized eigenspaces. On the corresponding Hom block the operator is a nonzero scalar plus the difference of left and right nilpotent multiplication. Those nilpotent operators commute, and their sum is nilpotent by the binomial formula. A finite geometric series inverts the operator. Thus (5.0j) forces \(F_{-q}=0\), a contradiction. This eliminates poles along every component.

An entry of \(F\) already has the form \(h/\prod z_i^{N_i}\), with \(h\) holomorphic. Absence of a pole along \(z_i\), away from the other components, makes the first \(N_i\) Taylor coefficients in that coordinate vanish on an open set of the remaining variables. The identity theorem makes them vanish everywhere, so \(z_i^{N_i}\) divides \(h\). Repeating for the different coordinates shows that the full product divides \(h\), by its convergent power-series expansion. Thus \(F\) is holomorphic at all intersections too.

A horizontal isomorphism on \(V^*\) extends together with its inverse, so its normalized extension is a holomorphic isomorphism. In particular any normalized logarithmic bundle with the given local system is uniquely isomorphic to the model (5.0f). This proves local uniqueness and, as a consequence rather than an assumed normal-form theorem, every normalized logarithmic bundle is locally isomorphic to the constant commuting-residue model.

#### The local analytic disc criterion

Let \(M\) be a locally free finite-rank meromorphic bundle over
\(\mathcal O_V[(z_1\cdots z_k)^{-1}]\), with integrable connection and no poles on \(V^*\).

If it has a logarithmic lattice, pull back to any holomorphic disc
\(\gamma:\Delta\to V\) not contained in \(D\). Each boundary coordinate has
\[
z_i\circ\gamma=t^{m_i}u_i(t),\qquad
m_i\geq0,\quad u_i(0)\ne0,
\]
after shrinking. Hence
\[
\gamma^*\frac{dz_i}{z_i}
=m_i\frac{dt}{t}+\frac{du_i}{u_i}.
\tag{5.0k}
\]
The pulled-back lattice is free of the same rank and its connection has only a logarithmic pole. Lesson 13's proved lattice criterion makes it regular singular. Formula (5.0k) includes tangent, ramified and simultaneous approaches to any number of boundary components.

Conversely, it suffices to assume regular singularity along the transverse coordinate-disc slices, for a nonempty open family of parameters for each \(z_i\). The restriction of \(M\) to \(V^*\) has a local system, by the earlier flat-connection theorem. Form its normalized model \(E_\Sigma\) from (5.0f). That same theorem and the monodromy description give a horizontal isomorphism
\[
G:E_\Sigma|_{V^*}\longrightarrow M|_{V^*}.
\tag{5.0l}
\]
Both \(G\) and \(G^{-1}\) are single-valued holomorphic matrices on \(V^*\) in chosen meromorphic frames.

On each regular transverse slice, \(M\) has a convergent logarithmic lattice by the proved one-variable criterion. The model \(E_\Sigma\) is logarithmic there as well. The one-variable case of the meromorphic-map proof therefore makes \(G\) and its inverse meromorphic in that slice. Lemma 5.0.3 gives a uniform finite pole bound in that coordinate; repeat for every boundary coordinate. The joint Laurent argument after that lemma makes \(G,G^{-1}\) meromorphic on \(V\). Transporting \(E_\Sigma\) by (5.0l) now gives a free logarithmic lattice in \(M\).

Thus the following local conditions are equivalent:

1. A logarithmic lattice exists.
2. Every holomorphic-disc pullback not contained in \(D\) is regular singular at its boundary intersections.
3. Regularity holds on nonempty open families of transverse coordinate-disc slices in each boundary direction.

This is the local analytic part of the global curve criterion. The global proof below shows how the lesson's tests on smooth algebraic curves, including their compactification points, supply its local hypothesis. No assumption that analytic and algebraic curve tests are automatically interchangeable appears here.

For the constant model, the residue on a disc approaching several components is \(\sum_i m_iA_i\). These matrices commute, and their nilpotent parts are retained. Its eigenvalues need not lie in \(\Sigma\); regularity survives, but the pulled-back logarithmic lattice need not itself be the normalized lattice.

#### Gluing across every boundary intersection

Cover \(\overline U\) by adapted charts, using ordinary flat frames on charts disjoint from \(D\). On each adapted chart construct (5.0f) with its identified restriction to the given \(L\). On an overlap, those identifications give a horizontal isomorphism between the restrictions on \(U\). Locally near every boundary point of the overlap, both extensions are normalized logarithmic bundles for the same reduced divisor, irrespective of the chosen component order or equations. the meromorphic-map proof extends the isomorphism and its inverse holomorphically.

These local extensions agree on smaller overlaps because they agree on the dense boundary complement and are unique. The cocycle identity on a triple overlap holds there and hence everywhere as a holomorphic identity. Thus the bundles and logarithmic connections glue on \(\overline U\), with rank unchanged. This is ordinary sheaf gluing: identify sections by the transition maps; the cocycle relation makes the equivalence relation consistent, and each chart gives a local free frame.

Maps of local systems extend by the same argument and commute with composition by uniqueness. Exactness can be checked on each adapted chart, where it is the exact \(\mathcal O\)-extension of a finite-dimensional representation sequence from the local model construction. The construction is therefore globally functorial and exact. Any other identified normalized extension is glued to this one by its unique local normalized isomorphisms.

Allowing meromorphic coefficients gives \(E_\Sigma(L)(*D)\). the meromorphic-map proof proves that every horizontal map of the restrictions extends uniquely between regular meromorphic bundles, after choosing local logarithmic lattices. the local analytic disc criterion proves that every locally regular meromorphic bundle is identified with this construction. Hence the regular meromorphic correspondence is fully faithful and essentially surjective; the construction is independent of the local lattices.

Regularity is preserved by a holomorphic map of normal-crossing pairs carrying the source open complement into the target open complement, for which the inverse-image boundary is supported in the source boundary. Locally, a nonzero pulled-back boundary equation is a unit times a product of source boundary coordinates with nonnegative integer multiplicities.

Here is the factor assertion without an extra divisor theorem. If a holomorphic \(f\) has no zero off a coordinate boundary, \(1/f\) is holomorphic on its complement. On every transverse coordinate slice it is meromorphic, since the nonzero holomorphic one-variable \(f\) has a zero of finite order. Lemma 5.0.3 and its joint Laurent consequence give \(1/f=h/\prod w_j^{N_j}\). Thus \(fh=\prod w_j^{N_j}\). Factor from \(f\) and \(h\) their maximal coordinate powers using convergent Taylor expansions. Coordinate valuations are additive: their leading coefficient product is nonzero in the convergent ring in the other variables, which is a domain by the identity theorem. After cancelling those powers the remaining factors multiply to \(1\). Therefore the remaining factor of \(f\) is a unit, proving the assertion.

The logarithmic differential is the corresponding sum of logarithmic differentials plus a holomorphic unit differential, by (5.0k)'s multivariable version. A pulled-back logarithmic lattice remains logarithmic and preserves rank. This proves the local pullback statement, including boundary multiplicities. The global proof below supplies proper algebraization and compactification independence.

#### Tensor products and normalization

Normalized extension is not generally tensor compatible. In rank one in one boundary coordinate, two canonical residues \(3/4\) have tensor residue \(3/2\), while the normalized extension of their tensor local system has residue \(1/2\). Multiplication by an integral coordinate power identifies the two meromorphic bundles but changes their holomorphic lattices. The same issue affects canonical pullback when boundary multiplicities change. Exactness and horizontal-map functoriality above require no tensor-compatibility claim.

The meromorphic tensor and dual of logarithmic bundles remain logarithmic, by the usual connection Leibniz rules; their residues are sums and negatives. Hence these operations remain regular, even when renormalization changes the chosen lattice.


This proves Theorem 5.0 and its local criterion. $\square$

### Global correspondence and compactification

**Theorem 5.1 (Deligne correspondence and compactification criterion).** If $X$ is a smooth separated complex algebraic variety, horizontal sections after analytification give an equivalence
\[
\operatorname{Conn}_{\rm reg}(X)
\ \simeq\ \operatorname{Loc}_{\rm fd}(X^{\rm an}).               \tag{5.1}
\]
Morphisms on the left are algebraic connection maps. On the right are finite-rank complex local systems. For every smooth proper compactification \(P\) with simple normal-crossing boundary \(D\), an algebraic connection on \(X=P\setminus D\) is curve regular if and only if it has an algebraic logarithmic extension on \(P\); equivalently it is regular at the generic points of every boundary component by the transverse discrete-valuation-ring test. The criterion is independent of compactification.


**Proof.** The global prerequisites have earlier programme proofs. AG-QC, Appendix N, Theorem N.E.1 proves Nagata compactification for separated finite-type Noetherian schemes. After taking the reduced closure, Principalization and resolution, Theorem 4.8 and Corollary 3.3 resolve while preserving the smooth open and principalize its complement. This is the proof of that lesson's Corollary 5.2, with its Nagata step supplied by the preceding programme theorem. It gives a smooth proper SNC compactification of the entire \(X\), including non-quasi-projective \(X\).

Proper GAGA is AG-QC, Theorem 6.11, with full faithfulness in Proposition 6.9 and analytic compactness in Lemma 6.4; it includes proper nonprojective schemes. AG-QC, Theorem 4.1 and Proposition 5.1 prove faithfully flat analytic stalk comparison and exact coherent analytification. The coherent cokernel argument uses Oka coherence, Theorem 2.1 and the analytic Nullstellensatz, Theorem 5.1. The coherent extension, finite poles, jet splitting and descent needed in the rest of the proof are established below.

The finite-type closed-point test follows from the weak and strong Nullstellensatz, Theorems 2.1 and 2.2. Extending curve maps uses Proper morphisms and valuative criteria, Theorems 1.2 and 3.1, with uniqueness from Valuation rings and separatedness, Theorem 4.2. The local rings of smooth curves are regular by the smooth local-ring criterion, Theorem 3.2, hence are DVRs by Regular local rings, Solution 7.2.

#### Algebraizing the bundle and its logarithmic connection

Let \(P\) be smooth and proper over \(\mathbf C\), let \(D\) be a reduced SNC divisor, and put \(U=P\setminus D\). Suppose \((L,\nabla_{\mathrm{an}})\) is an analytic locally free bundle with an integrable logarithmic connection on \(P^{\mathrm{an}}\).

Proper GAGA gives a coherent algebraic \(F\) with an identification \(F^{\mathrm{an}}\cong L\). This \(F\) is locally free. At a closed algebraic point, lift a basis of its residue fibre to a map \(\mathcal O_{P,x}^r\to F_x\). Nakayama makes it surjective. After faithfully flat analytic base change it is a map between rank-\(r\) free modules with invertible residue determinant, hence an isomorphism. Faithfulness kills the algebraic kernel. The free-stalk presentation extends to a neighbourhood. The complement of the locally free locus is closed and has no closed point, hence is empty on a finite-type complex scheme.

The logarithmic one-forms have local basis \(dt_i/t_i\) in boundary directions and the other coordinate differentials. Changing a boundary equation by a unit adds a regular form, so they glue and their analytification is the analytic logarithmic sheaf.

Construct an algebraic logarithmic first-jet extension
\[
0\longrightarrow\Omega_P^1(\log D)\otimes F
\longrightarrow J^1_{\log D}(F)\xrightarrow{p}F\longrightarrow0.
\tag{5.1a}
\]
In a local frame the middle module is \(F\oplus(\Omega_P^1(\log D)\otimes F)\). If coefficient columns satisfy \(e_\beta=g_{\beta\alpha}e_\alpha\), glue pairs by
\[
(e_\alpha,v_\alpha)\longmapsto
(g_{\beta\alpha}e_\alpha,(dg_{\beta\alpha})e_\alpha+g_{\beta\alpha}v_\alpha).
\tag{5.1b}
\]
These are invertible \(\mathcal O_P\)-linear block matrices. The derivative product rule proves their cocycle identity, so they define a finite locally free algebraic bundle. Projection to the first entry is \(p\), with the indicated tensor kernel. The \(\mathbf C\)-linear map \(j(e)=(e,de)\) is well defined by the same transition rule and satisfies \(j(fe)=f j(e)+df\otimes e\). Splittings and logarithmic connections therefore correspond by
\[
\nabla=j-\sigma,\qquad \sigma=j-\nabla,\qquad p\sigma=1.
\tag{5.1c}
\]
The Leibniz terms cancel in \(j-\nabla\), making it \(\mathcal O_P\)-linear. These formulas commute with analytification.

The given analytic connection supplies an analytic splitting. Proper GAGA full faithfulness lifts it to a unique algebraic \(\sigma\); faithfulness detects \(p\sigma=1\). Hence \(\nabla=j-\sigma\) algebraizes the connection itself. The logarithmic exterior algebra is closed under \(d\): its coordinate generators are closed and derivatives of regular coefficients are regular. Extend \(\nabla\) by the graded Leibniz rule. Its square is \(\mathcal O_P\)-linear because the terms involving \(df\) cancel and \(d^2f=0\). This curvature map \(F\to\Omega_P^2(\log D)\otimes F\) has zero analytification and therefore vanishes. The connection is integrable. The same GAGA argument algebraizes horizontal maps: their defect of horizontality is \(\mathcal O_P\)-linear and vanishes after analytification. This applies to proper nonprojective \(P\).

The transverse-curve and coherent-comparison arguments below prove that this construction recovers every curve-regular algebraic connection.


#### From algebraic curves to finite poles at crossings

Let \(E\) be a curve-regular algebraic flat bundle on \(U\). First fix a point \(p\) on the smooth part of a component of \(D\), away from the others. On an affine algebraic neighbourhood \(W\), choose a local boundary equation \(t\) and functions completing its nonzero differential to a cotangent basis at \(p\). The prescribed-coordinate form of Smooth morphisms, Theorem 4.1 makes their map étale after shrinking:
\[
(t,y_2,\ldots,y_d):W\longrightarrow\mathbf A^d,
\qquad D\cap W=(t=0).
\tag{5.1d}
\]
The fibres \(y_i=a_i\) are smooth algebraic curves. Each small analytic \(t\)-slice in this étale chart is an open piece of such a curve. Its punctured piece maps into \(U\), and the missing point \(t=0\) occurs in its smooth complete model. Thus the assumed algebraic curve test applies there. Corollary 3.2 turns a formal test into a convergent logarithmic lattice.

Along any such curve, choose a basis of the generic fibre of its pulled-back algebraic bundle. These are rational sections. Every finite algebraic generator, and every coefficient of an algebraic map into a free ambient bundle, has finite Laurent poles relative to that basis near the missing point: each rational function is a quotient of convergent regular functions, and a nonzero one-variable denominator has finite order. The curve local ring is a DVR by Regular local rings, Solution 7.2. One can instead pull back a coherent extension to the curve and remove its DVR torsion. A generic basis and common denominators embed that finite torsion-free module in a finite free module. The coordinate-projection induction of Lemma 1.0 applies to this DVR too and proves it free of the full generic rank. The frames may be chosen separately for each curve. No injectivity of a pulled-back coherent ambient map is needed for these scalar calculations.

Compare with the normalized analytic logarithmic bundle \(L\) of the same local system. In the curve's convergent logarithmic lattice, the horizontal comparison and its inverse are meromorphic by the one-variable meromorphic-map proof above. Changing to rational frames preserves this property. Thus the forward scalar columns obtained by an algebraic ambient injection, and the inverse coordinates of finite algebraic generators, are meromorphic on every slice of this algebraic family. The same assertion holds for every horizontal analytic map between two curve-regular algebraic bundles.

Lemma 5.0.3 in these étale coordinates proves actual meromorphy on an analytic neighbourhood of \(p\). This is independent of coordinates: another equation of the same reduced smooth boundary component differs from \(t\) by a holomorphic unit.

Now fix any analytic SNC chart \(V\) at a boundary intersection. For each local component \((z_i=0)\), choose a smooth point \(p\) in \(V\), away from the other components. It has a product neighbourhood in the fixed \(z\)-coordinates on which the comparison entries are already meromorphic. This supplies a nonempty open subfamily of the fixed \(z_i\)-slices. The other normal coordinates are punctured and their product parameter domain is connected. The fixed-chart Laurent argument below propagates the finite pole bound to that entire domain; repeating in every \(z_i\) extends across the intersection. This argument does not require arbitrary analytic coordinate slices themselves to be algebraic curves.

Here is the uniformity argument, including crossings. For a holomorphic function \(f\) on \(\Delta^*\times V\), its Laurent coefficients \(a_j(y)\) are holomorphic on the connected parameter domain \(V\), by parameter Cauchy integrals. Slice meromorphy on a nonempty open \(V_0\) means
\[
V_0\subset\bigcup_{N\ge0}
\{y:a_j(y)=0\text{ for all }j<-N\}.
\]
The displayed sets are closed. If each had empty relative interior in \(V_0\), nested closed balls, with the \(N\)-th ball avoiding the \(N\)-th set and radius at most \(2^{-N}\), would have a common point avoiding their union, a contradiction. Thus one has interior; the identity theorem makes all its forbidden Laurent coefficients vanish on all of \(V\). Cauchy bounds give a holomorphic extension of \(t^Nf\).

Apply this in each normal coordinate, with the other normal coordinates punctured and all remaining coordinates as parameters. The joint Laurent expansion has a fixed lower bound in every normal exponent. Multiplication by a finite product \(\prod t_i^{N_i}\) leaves a convergent holomorphic power series on the full polydisc. Thus finite poles extend across every SNC crossing. No meromorphic Hartogs theorem or a generic uniform pole-order assertion is imported. 

#### Coherent extensions and algebraic full faithfulness

**A quasi-compact open direct image is quasi-coherent.**

Let \(V=\operatorname{Spec}A\), \(W\subset V\) be quasi-compact open, and \(j:W\hookrightarrow V\). For a quasi-coherent sheaf \(Q\) on \(W\), choose a finite principal cover \(W=\bigcup_iD(s_i)\). The sheaf equalizer gives
\[
\Gamma(W,Q)=
\ker\left(
\prod_i\Gamma(D(s_i),Q)
\longrightarrow
\prod_{i,j}\Gamma(D(s_is_j),Q)
\right),
\tag{5.1e1}
\]
where the arrow is the difference of restrictions.

For \(a\in A\), localization at \(a\) is exact and commutes with these finite products. One can verify exactness directly with fractions: a fraction whose image is zero has some denominator power killing that image, making its numerator a representative from the original kernel. On the principal affines, quasi-coherence identifies localization with restriction to \(D(a)\). Thus localizing (5.1e1) gives the same equalizer on \(W\cap D(a)\):
\[
\Gamma(W,Q)_a=\Gamma(W\cap D(a),Q).
\tag{5.1e2}
\]
This is the affine quasi-coherence criterion. Consequently \(j_*Q\) is quasi-coherent. Applied on every affine chart, it proves the same statement for a quasi-compact open of a Noetherian scheme. Kernels and quotients of quasi-coherent sheaves are quasi-coherent, since on each affine chart they are the associated sheaves of module kernels and quotients, and exact localization identifies their restrictions.

No finite generation of \(j_*Q\) is asserted.

**Finite coherent submodules extend across an open.**

Let \(X\) be Noetherian separated, \(Q\) quasi-coherent on \(X\), and \(G\subset Q|_W\) a finite-type quasi-coherent submodule on a quasi-compact open \(W\).

First take \(X=\operatorname{Spec}A\). The quotient \(Q|_W/G\) is quasi-coherent. Define
\[
H=\ker\bigl(Q\longrightarrow j_*(Q|_W/G)\bigr).
\tag{5.1e3}
\]
The quasi-coherent direct-image argument makes \(H\) quasi-coherent, and restriction to \(W\) makes it exactly \(G\). Cover \(W\) by finitely many \(D(s_i)\). Choose finite module generators of \(G\) on each \(D(s_i)\); this is possible because the coefficient rings are Noetherian and \(G\) is of finite type. By quasi-coherence of \(H\), every chosen generator is a fraction of an element of \(\Gamma(X,H)\), with a power of \(s_i\) as denominator. Let \(N\) be the finite \(A\)-submodule generated by all those numerators.

Its associated sheaf lies in \(H\), and on each \(D(s_i)\) contains all the chosen generators, since \(s_i\) is invertible there. Hence
\[
\widetilde N|_W=G.
\tag{5.1e4}
\]
The finite \(A\)-module \(N\) is finitely presented because \(A\) is Noetherian: the kernel of a finite free surjection is a finite submodule of a finite free module. Thus \(\widetilde N\) is coherent.

For general \(X\), choose a finite affine cover. Start with \(G\) on \(W\), and add these affine opens one at a time. If \(W'\) is the already treated open and \(V\) the next affine, \(W'\cap V\) is quasi-compact because \(X\) is Noetherian. The affine construction extends \(G|_{W'\cap V}\) to a coherent submodule of \(Q|_V\), agreeing exactly with it on the intersection. Glue the two submodules inside \(Q\). The glued sheaf is quasi-coherent and coherent because these properties are local and it has coherent restrictions on the old open and on \(V\). After finitely many steps it is defined on all of \(X\).

This proves the full finite-submodule extension assertion. It uses no ample line bundle, projectivity, extension of a locally free sheaf as locally free, or affine assumption on the original \(j\).

**Coherent extension of a bundle on a quasi-compact open.**

Let \(j:U\hookrightarrow X\) be quasi-compact open, and \(E\) a coherent sheaf on \(U\), in particular a finite-rank vector bundle. The quasi-coherent direct-image argument gives the quasi-coherent sheaf
\[
Q=j_*E
\]
on \(X\), with \(Q|_U=E\). Apply the finite-submodule extension argument to the finite-type submodule \(G=E\subset Q|_U\). We obtain a coherent subsheaf
\[
F\subset j_*E,\qquad F|_U=E.
\tag{5.1e5}
\]
Thus the required coherent extension exists in the entire Noetherian separated scope. It is unnecessary to assert a pre-existing coherent extension theorem as an additional leaf.

For the smooth pair \(X=P\), \(D=P\setminus U\), every integral component meets \(U\). The chosen \(F\subset j_*E\) is already torsion free on that component. A nonzero coefficient cannot kill a section of \(E\) on its dense open domain: in local vector-bundle coordinates over a domain it kills no nonzero coordinate. Equivalently, \(j_*E\) embeds into its generic-fibre vector space. If one starts instead with any coherent extension, quotienting its finite torsion submodule is legitimate over a Noetherian domain and leaves its restriction to the bundle \(E\) unchanged.

For an effective Cartier boundary \(D\), the open immersion is affine. On an affine chart \(V=\operatorname{Spec}A\) trivializing its equation \(q\), one has \(U\cap V=D(q)=\operatorname{Spec}A_q\). If \(F|_V=\widetilde N\), (5.1e5) gives
\[
N_q=\Gamma(D(q),E).
\tag{5.1e6}
\]
The module on the right is finite projective over \(A_q\); this follows from the vector-bundle affine module description. We use (5.1e6), not a claim that \(N\) is projective over \(A\).


On an affine neighbourhood, a rational basis and the finitely many denominators of generators give an injection
\[
F\hookrightarrow\mathcal O_P^r.
\tag{5.1f}
\]
Exact analytification preserves that injection. This does not assert that \(F\) is locally free at the boundary. The original algebraic connection already defines a meromorphic connection on \(F(*D)\): on an affine \(W=\operatorname{Spec}A\) with \(D=(q)\), if \(F\) corresponds to \(N\), the equality \(F|_{W\setminus D}=E\) says \(N[1/q]\) is precisely the module of \(E\) there. Its connection is defined on that localization. Images of finitely many generators have finite algebraic \(q\)-denominators, so analytification gives a meromorphic connection on \(F^{\mathrm{an}}[1/q]\). No free meromorphic frame is needed for this step.

Suppose first that \(L\) is the normalized analytic logarithmic bundle for \(E^{\mathrm{an}}\)'s local system. The analytic horizontal comparison \(v:L|_U\to E^{\mathrm{an}}\) is an isomorphism. In a local frame of \(L\), compose its columns with (5.1f). They are scalar holomorphic functions on the punctured SNC product. the transverse-curve and Laurent argument above makes their restrictions meromorphic on algebraic transverse slices and hence gives a product pole bound across the whole polydisc.

Their extensions belong to \(F^{\mathrm{an}}(*D)\). To see this precisely, let \(q=\prod t_i\). After multiplying a column by \(q^N\), it is a holomorphic vector in \(\mathcal O^r\). Its class \(c\) in the coherent cokernel of (5.1f) vanishes off \(D\). The cyclic coherent module generated by \(c\) has support in \(D\). Analytic Nullstellensatz therefore puts \(q\) in the radical of its annihilator, so \(q^Mc=0\) for some \(M\), on a smaller neighbourhood. The column multiplied by \(q^{N+M}\) lies in \(F^{\mathrm{an}}\).

For the inverse comparison, take finitely many generators of \(F\). Their images under \(v^{-1}\) have scalar coordinates in a frame of \(L\). The same curve and Laurent argument extends those coordinates meromorphically. Every finite relation is preserved, since its meromorphic image is zero on the dense complement. Thus
\[
F^{\mathrm{an}}(*D)\simeq L(*D)
\tag{5.1g}
\]
as meromorphic flat bundles. The inverse identities can be checked using the localized injection \(F^{\mathrm{an}}[1/q]\hookrightarrow\mathcal O^r[1/q]\): a difference becomes scalar meromorphic functions zero off \(D\), hence zero. This avoids treating a meromorphic localization itself as an \(\mathcal O\)-coherent module. The connection identities hold by the same localized argument.

The same argument works for an arbitrary horizontal analytic map between two curve-regular algebraic bundles \(E_1,E_2\). Take torsion-free coherent extensions \(F_1,F_2\), embed \(F_2\) in a finite free sheaf as in (5.1f), and apply the scalar argument to the images of finitely many generators of \(F_1\). The cokernel argument puts them in \(F_2^{\mathrm{an}}(*D)\). Relations give a map \(F_1^{\mathrm{an}}\to F_2^{\mathrm{an}}(*D)\).

On proper \(P\), compactness provides one finite global pole bound \(n\). The local maps therefore glue to
\[
F_1^{\mathrm{an}}\longrightarrow F_2^{\mathrm{an}}(nD).
\tag{5.1h}
\]
After increasing smaller local bounds to their maximum, the maps agree on overlaps: they agree off \(D\), and the torsion-free target makes a section with that dense-open restriction unique. Full faithful proper GAGA algebraizes (5.1h). Its restriction to \(U\) is the desired algebraic map. The difference \(\nabla_2\phi-(1\otimes\phi)\nabla_1\) is \(\mathcal O_U\)-linear, since its two Leibniz terms cancel. It has zero analytification, so faithfully flat analytic stalks make it zero algebraically. Algebraizing the inverse in (5.1g) similarly gives an algebraic horizontal isomorphism on \(U\).

This proves algebraic full faithfulness for curve-regular connections without requiring a free coherent extension at the boundary. 

#### The curve and divisorial criteria

**Logarithmic extension implies curve regularity.** Let \(F\) be an algebraic logarithmic flat bundle on the proper pair \((P,D)\), and let \(h:C\to U\) be any map from a smooth algebraic curve. Its map from the function field extends to the smooth complete curve \(\overline C\) by properness of \(P\), applied at the discrete valuation rings of its missing points. The valuative criterion gives a map on each missing-point discrete valuation ring. Choose an affine target neighbourhood of its closed image: the entire spectrum of that local ring maps into it. Finitely many coordinate images are rational functions regular at the point, so extend to a Zariski neighbourhood on the curve; finitely many equations and inverted coordinates remain valid after shrinking. Thus the local-ring maps spread to actual curve maps. Separatedness makes the extensions agree on overlaps because they agree at the dense generic point, and they glue. Locally at such a point, each pulled-back boundary equation is
\[
t_i\circ\overline h=u_i s^{m_i},\qquad
\overline h^*(dt_i/t_i)=m_i\,ds/s+du_i/u_i,
\quad m_i\ge0.
\tag{5.1i}
\]
Hence \(\overline h^*F\) has a logarithmic connection at every missing point. This proves regularity for every curve map, including curves approaching intersections with nontrivial multiplicities.

**Curve regularity implies logarithmic extension on this pair.** Let \(E\) be curve regular on \(U\). Build \(L\) from its local system, using the proved local SNC theorem. The logarithmic jet algebraization above algebraizes \(L\) and its logarithmic connection to \(F_\Sigma\) on \(P\). By (5.1i), \(F_\Sigma|_U\) is curve regular. The analytic horizontal identification \(E^{\mathrm{an}}\cong F_\Sigma^{\mathrm{an}}|_U\) algebraizes by the coherent comparison and full-faithfulness proof above. Therefore \(F_\Sigma\) is an algebraic logarithmic extension of \(E\) on this very pair.

This proves the criterion for every given proper smooth SNC compactification, including nonprojective ones. Existence of at least one such pair is supplied separately by the compactification proof chain above.

The generic divisorial formulation follows as well. At the generic point of each boundary component, require a lattice over its discrete valuation ring \(R\) preserved by \(t\nabla_v\), for an algebraic vector field \(v\) regular and transverse there.

If the test was first expressed after completion, it gives the same criterion over \(R\). Put \(K=\operatorname{Frac}R\). A basis of the completed stable lattice is a matrix \(G\in\operatorname{GL}_r(\widehat K)\). Approximate its finitely many entries by entries of \(K\) to sufficiently high valuation, obtaining \(\widetilde G\) with \(G^{-1}\widetilde G=H=1+\) a positive-valuation matrix. Such approximations exist by the definition of completion, after multiplying entries by fixed powers of \(t\). The derivation \(tv\) preserves valuation: \(v(R)\subset R\) and \(v(t)\) is a unit, so \(tv(t^na)\in t^nR\), for every integer \(n\) and \(a\in R\). It therefore extends continuously to the completion with the same property. Write \(t\nabla_v=tv+B_0\) in the initial rational frame. In the completed lattice frame its coefficient matrix is \(A=G^{-1}B_0G+G^{-1}tv(G)\in\operatorname{Mat}_r(\widehat R)\). The coefficient matrix in the \(\widetilde G\) frame is \(H^{-1}AH+H^{-1}tv(H)\), still integral over \(\widehat R\). It also lies in \(K\), because \(\widetilde G\) and the original connection do. The valuation test gives \(K\cap\widehat R=R\). Thus \(\widetilde G\) supplies an actual \(R\)-lattice preserved by \(t\nabla_v\). This proves the descent of the formal test rather than assuming it.

A basis of this lattice consists of rational sections. Its finitely many connection coefficients, and the finitely many denominators of that basis and its inverse, extend to an algebraic open meeting the component, with \(t\nabla_v\) regular on the chosen basis.

Near a complex point of this open, straighten \(v\) holomorphically using its local flow from the divisor. Picard iteration on a smaller polydisc is a contraction, uniformly in the divisor parameters, so it gives a holomorphic flow. Its derivative is invertible at the initial point because \(v\) is transverse; the proved holomorphic inverse-function argument gives coordinates \((s,y)\) with \(v=\partial_s\) and \(t=s\) times a unit. In the rational basis just chosen, the connection along every \(s\)-slice therefore has at most a simple pole. The one-variable criterion and the same parameter argument give meromorphy of the comparison with \(L\) on a nonempty open part of the component.

Every local boundary component meets that good open in a nonempty analytic open subset. Indeed if the proper algebraic exceptional closed set contained an analytic neighbourhood on the irreducible smooth divisor, its finite defining ideal would have zero analytification at that point by the identity theorem. Faithful local flatness makes the algebraic ideal zero there; finite generation then makes it zero on a Zariski neighbourhood, contradicting properness of the closed subset. At a good smooth point, the flow-chart boundary equation and the fixed analytic \(z_i\) differ by a holomorphic unit. A small product box in this meromorphic neighbourhood supplies a nonempty open family of the fixed \(z_i\)-slices. The connected punctured-product Laurent argument above now propagates the finite pole bound and handles all crossings. The coherent comparison and full-faithfulness proof above and proper GAGA then give the logarithmic extension. Conversely a logarithmic lattice is preserved by \(t\nabla_v\) for every such regular transverse \(v\). Thus the criterion is independent of the selected transverse vector field. In this implication the analytic flow is a consequence of the divisorial lattice itself; it is not substituted for an algebraic curve test.

#### Correspondence on every smooth separated variety

For a proper SNC pair, a finite-rank local system on \(U^{\mathrm{an}}\) first gives its analytic logarithmic bundle, then the logarithmic jet algebraization above algebraizes it to an algebraic logarithmic flat bundle. the curve and divisorial criterion above makes its restriction curve regular. The coherent comparison and full-faithfulness proof above proves full faithfulness for all curve-regular algebraic connections. This establishes the correspondence on \(U\), with no projectivity assumption on the pair.

There is also a complete descent proof preserving arbitrary smooth separated \(X\). Choose a finite affine cover \(X=\bigcup U_i\). Each \(U_i\) has an explicit projective closure; resolution and principalization give a projective smooth SNC compactification of \(U_i\), preserving its entire smooth open. Thus the already proved pair argument establishes the correspondence on every \(U_i\). Separatedness makes \(U_i\cap U_j\) affine: its diagonal description is a closed subscheme of the affine \(U_i\times U_j\).

Regularity defined by all curves is Zariski local. To prove this, take a curve \(h:C\to X\) and one irreducible component of \(C\). Its generic point maps into some \(U_i\), so \(C_0=h^{-1}U_i\) is a dense open curve. The restriction of \(h^*E\) to \(C_0\) is regular at every point of its smooth complete model, by regularity on \(U_i\). That complete model is also the smooth complete model of \(C\): a rational map between two smooth proper models extends at every discrete valuation ring by properness, and the two extensions are inverse by separatedness. The restriction therefore proves regularity at infinity for \(h^*E\). At the remaining points of \(C\) the given algebraic connection is already nonsingular. This proves the local assertion. Restriction of a curve-regular connection to an open is immediate by composition of curve maps.

Given a local system \(A\) on \(X^{\mathrm{an}}\), algebraize it on each \(U_i\) to \(E_i\), with the specified identification of its horizontal local system. On \(U_i\cap U_j\), full faithfulness gives the unique algebraic horizontal isomorphism inducing those identifications. On triple overlaps their compositions coincide analytically and hence algebraically, proving the cocycle identity. Ordinary open gluing produces a vector bundle and a connection on all of \(X\); integrability is local. The preceding curve argument makes it globally regular. Its horizontal local system is \(A\).

Likewise a morphism of local systems algebraizes on each \(U_i\); uniqueness on overlaps glues the algebraic connection maps. Faithfulness is local. Thus
\[
\operatorname{Conn}_{\mathrm{reg}}(X)
\simeq\operatorname{Loc}_{\mathrm{fd}}(X^{\mathrm{an}})
\tag{5.1j}
\]
holds for every smooth separated finite-type complex \(X\). The proof covers every smooth separated finite-type complex \(X\).

#### Independence of compactification

By the curve and divisorial criterion above, existence of a logarithmic extension on one proper smooth SNC compactification is equivalent to the intrinsic curve property. That property supplies a logarithmic extension on every such compactification. Together with the actual existence theorem, this proves the asserted compactification criterion and its independence.

A common proper SNC model can also be constructed explicitly. For two compactifications \(P,Q\), take the reduced closure of the graph of \(X\) in \(P\times Q\). Its inverse image of \(X\) under either projection is exactly that graph: the graph is already closed over this open, by separatedness. Resolve the closure while preserving the smooth open \(X\), and principalize its complement. This gives a smooth proper SNC \(W\) and proper maps \(W\to P,Q\) restricting to the identity on \(X\).

Pullback preserves logarithmic connections. Each pulled-back boundary equation factors locally as a unit times a monomial in the boundary equations of \(W\); its logarithmic differential is a sum of their logarithmic differentials plus a holomorphic unit differential, exactly as in (5.1i). The two pulled-back extensions of the same connection are uniquely identified after allowing boundary poles: their horizontal identity on \(X\) extends meromorphically by the proved local logarithmic morphism lemma.

One must not claim equality of the normalized holomorphic lattices under this pullback. New boundary residues are sums with integral multiplicities and may leave the chosen strip; re-normalization can change the lattice by integral boundary powers. The meromorphic identification and the intrinsic curve property are independent of that choice. This distinction preserves all multiplicities and Jordan blocks without adding an invalid tensor or pullback compatibility claim.


The correspondence and all compactification assertions have now been proved. The freely accessible [IAS-hosted Deligne text](https://publications.ias.edu/sites/default/files/Number9.pdf), Chapter II, §§4–5, is the human reading source for these constructions. The arguments above supply the proofs. $\square$

Now use finite length and the description of simple holonomic modules from the preceding lesson. A holonomic module is **regular holonomic** if every composition factor can be presented as the minimal extension $j_{!*}E$ of an irreducible regular connection on a smooth locally closed subvariety with affine inclusion. The zero module is regular. This is the definition in Bernstein's freely accessible lecture “Holonomic D-modules with regular singularities.” Theorem 5.2 below proves that, for a module that is itself a connection, it agrees with the preceding all-curve definition, including infinity.

### Connections and the regular-holonomic definition

Theorem 5.1 was proved using the all-curve definition of regular connections, independently of the regular-holonomic identification below.

#### Connection subquotients and finite length

We work first on a connected smooth variety \(X\). Smooth local rings are regular by the smooth local-ring criterion, Theorem 2.1. They are domains by Regular sequences and depth, Theorem 6.1. Its proof uses the polynomial associated graded ring, Krull separation and multiplication of initial forms. The finitely many irreducible components of a Noetherian scheme cannot meet when all local rings are domains: at an intersection the corresponding local ring would have two minimal primes. They are therefore disjoint closed and open components. Smoothness also makes \(X\) reduced, so connected \(X\) is integral. The disconnected case is the finite direct sum over these components.

Let \(E\) be a finite-rank vector bundle with integrable connection. Any quasi-coherent differential-operator submodule \(N\) of \(E\) is coherent over the structure sheaf: on a Noetherian affine open, its module of sections is a submodule of a finite module, hence finite. Its quotient \(E/N\) is coherent as well. Both inherit integrable connections, so the coherent-connection theorem, Theorem 3.1 makes \(N\) and \(E/N\) finite-rank vector bundles. The same argument applies successively to all subquotients.

The constant filtration \(F_iE=0\) for \(i<0\) and \(F_iE=E\) for \(i\geq0\) is a good order filtration. Its associated graded module is \(E\) in degree zero, and positive-degree vector symbols act by zero. Its characteristic support is the zero section over the support of \(E\). Hence a nonzero \(E\) on this connected \(X\) is holonomic and its support is all of \(X\).

A nonzero bundle on connected \(X\) has positive constant rank. Thus a proper inclusion of connection subobjects strictly increases rank: its nonzero quotient is again a bundle. Every increasing or decreasing chain of connection subobjects therefore has at most \(\operatorname{rank}E\) strict steps. A composition series exists without any further finiteness theorem: among nonzero subobjects choose one of least positive rank; it is simple, and repeat in the lower-rank quotient. All simple factors are themselves connections of full support \(X\). A simple connection is exactly an irreducible connection because every differential-operator subobject is a subbundle with bundle quotient.

This also excludes nonzero boundary-supported subobjects or quotients of a connection. Such an object would be a bundle of generic rank zero, hence zero.

#### Extensions of regular singular differential modules

Let \(R\) be either \(\mathbf C[[t]]\) or \(\mathbf C\{t\}\), let \(K\) be its fraction field, and set \(\theta=t\,d/dt\). A differential module \(V\) over \(K\) has an operator \(\Theta\) satisfying
\[
\Theta(fv)=\theta(f)v+f\Theta(v).
\tag{5.2a}
\]
Regular means that \(V\) has a full \(R\)-lattice \(L\) preserved by \(\Theta\). The following argument works over each ring separately, including arbitrary extension classes.

**Lemma 5.2.1.** In an exact sequence of differential \(K\)-modules
\[
0\longrightarrow V_1\longrightarrow V\longrightarrow V_2\longrightarrow0,
\tag{5.2b}
\]
\(V\) is regular if and only if both \(V_1\) and \(V_2\) are regular.

**Proof for subobjects and quotients.** Suppose \(L\) is a stable lattice in \(V\). Then \(L_1=L\cap V_1\) is preserved by \(\Theta\). It is finite free by Lemma 1.0. It spans \(V_1\): for any \(K\)-basis of \(V_1\), multiply the finitely many basis vectors by sufficiently large powers of t to put them in \(L\). The image \(L_2\) of \(L\) in \(V_2\) is finite, torsion free and spans \(V_2\); it is a lattice by the same lattice algebra. It is preserved by the induced operator. Thus both ends are regular.

**Proof for extensions.** Choose stable lattices \(L_1\) and \(L_2\) and a \(K\)-linear splitting \(s:V_2\to V\) of (5.2b). The defect
\[
B=\Theta s-s\Theta_2:V_2\longrightarrow V_1
\tag{5.2c}
\]
is \(K\)-linear: the two \(\theta(f)\) terms in (5.2a) cancel. There are finitely many coefficients of \(B\) on an \(R\)-basis of \(L_2\). Therefore some integer \(N\geq0\) satisfies
\[
B(L_2)\subset t^{-N}L_1.
\]
Put
\[
L=t^{-N}L_1\oplus s(L_2)\subset V.
\tag{5.2d}
\]
This is a full finite free lattice. Moreover
\[
\Theta(t^{-N}a)=t^{-N}(\Theta_1a-Na),\qquad
\Theta(s(b))=s(\Theta_2b)+B(b).
\tag{5.2e}
\]
Both terms lie in \(L\) whenever a belongs to \(L_1\) and b belongs to \(L_2\). Hence \(L\) is stable. The minus sign in -Na is essential and follows from \(\theta(t^{-N})=-Nt^{-N}\). No splitting of the differential module is assumed. This proves the lemma over formal and convergent rings. The zero-rank cases use the zero lattice. \(\square\)

The middle lattice may require an integral shift of the submodule lattice; no assertion is made that a normalized extension lattice is the direct sum of two normalized end lattices.

#### Curve-regular connections form a Serre category

Let
\[
0\longrightarrow E_1\longrightarrow E\longrightarrow E_2\longrightarrow0
\tag{5.2f}
\]
be a short exact sequence of finite-rank algebraic integrable connections on \(X\). This sequence is locally split as a sequence of structure-sheaf modules, since its quotient \(E_2\) is locally free. Its pullback by every algebraic map \(h:C\to X\) is therefore an exact sequence of flat bundles. No flatness assumption on h is needed.

Fix an irreducible component of the smooth curve \(C\) and any point p of its smooth complete model, including every point absent from \(C\). The sequence on \(C\) is exact at the function field. Choose rational frames for these generic fibres. Tensoring with the formal or convergent meromorphic field at p is exact, since this is a field extension of the rational function field; the rational connection coefficients define the resulting differential modules. Thus (5.2f) gives (5.2b) at p. Lemma 5.2.1 shows that the middle pullback is regular at p if and only if its two ends are regular there.

Doing this for every h and p proves:

**Proposition 5.2.2.** Curve-regular connections on \(X\) are closed under connection subobjects, quotients and extensions. In particular, a connection is curve regular if and only if all the factors of any one composition series of that connection are curve regular.

For the forward implication apply the subquotient part of Lemma 5.2.1 to every factor. For the reverse implication reconstruct the composition series by successive applications of its extension part. The proof retains every compactification point and every curve map. It does not merely test the nonsingular points already in \(C\).


#### Extending a horizontal map from a dense open

The next lemma concerns nonsingular connections on all of \(X\). It makes no assertion about arbitrary singular holonomic modules.

**Lemma 5.2.3.** Let \(E\) and \(F\) be finite-rank algebraic integrable connections on a smooth integral \(X\), and let \(V\) be a nonempty open subset. Every algebraic horizontal map \(\phi:E|_V\to F|_V\) extends to a unique algebraic horizontal map on \(X\). If \(\phi\) is an isomorphism on \(V\), its extension is an isomorphism.

**Proof.** Write \(K=\mathbf C(X)\), and let \(G\) be the graph of the generic \(K\)-linear map \(\phi_K\) inside \(E_K\oplus F_K\). It is stable under all derivations, because \(\phi\) is horizontal on \(V\). Derivations and connections extend to \(K\) by the quotient rule.

Inside \(E\oplus F\) define the graph closure \(\Gamma\) by intersection with \(G\). This is a coherent quasi-coherent submodule, a point worth checking explicitly. On an affine open \(\operatorname{Spec}A\), let M be the finite module of sections of \(E\oplus F\), viewed inside \(M\otimes_A K\); set \(\Gamma_A=M\cap G\). It is finite because A is Noetherian. For every nonzero f in A,
\[
(\Gamma_A)_f=M_f\cap G.
\tag{5.2g}
\]
Indeed, a vector \(m/f^a\) belongs to \(G\) precisely when m does, since \(G\) is a \(K\)-vector subspace. Consequently these finite modules sheafify compatibly and glue. On \(V\) the intersection recovers exactly the ordinary graph of \(\phi\).

For any local vector field \(\xi\), both the lattice of regular sections \(E\oplus F\) and its rational subspace \(G\) are preserved by the connection. Their intersection \(\Gamma\) is preserved as well. It is therefore a coherent module with integrable connection. Projection
\[
\pi:\Gamma\longrightarrow E
\tag{5.2h}
\]
is horizontal and is an isomorphism at the generic point. Its kernel and cokernel are structure-sheaf coherent modules with induced integrable connections. Theorem 3.1 of the preceding coherent-connection proof makes both bundles, and each has generic rank zero, so both are zero. Thus \(\pi\) is an isomorphism. The required extension is \(\operatorname{pr}_F\circ\pi^{-1}\).

Two extensions differ by an algebraic bundle map zero on a dense open. In local free frames its entries are regular functions in an integral ring, and hence zero. This proves uniqueness. If \(\phi\) is invertible on \(V\), apply the proved extension statement to \(\phi^{-1}\); the two compositions are the identity by uniqueness. \(\square\)

The graph construction does not assume that the original connection or any graph lattice is regular at infinity. Its only freeness input is the earlier local theorem for coherent nonsingular connections. It proves that restriction to a dense open is fully faithful for nonsingular algebraic connections, but essential surjectivity of that restriction is not asserted.

#### Dense-open regularity for a nonsingular connection

**Lemma 5.2.4.** Suppose \(Q\) is a finite-rank algebraic integrable connection on all of smooth separated \(X\). If \(Q|_V\) is curve regular for a dense open \(V\), then \(Q\) is curve regular on \(X\).

**Proof.** Let A be the horizontal local system of the full analytic connection \(Q^{\mathrm{an}}\) on \(X^{\mathrm{an}}\). Apply the already proved Theorem 5.1 on \(X\): it gives a curve-regular algebraic connection \(R\) and a horizontal analytic isomorphism
\[
u:R^{\mathrm{an}}\xrightarrow{\sim}Q^{\mathrm{an}}.
\tag{5.2i}
\]
It realizes the same full local system A, without any semisimplicity restriction.

On \(V\), both \(R|_V\) and \(Q|_V\) are curve regular. Theorem 5.1's full faithfulness, applied on this smooth separated open variety \(V\) to the restriction of u, gives an algebraic horizontal isomorphism
\[
u_V:R|_V\xrightarrow{\sim}Q|_V.
\tag{5.2j}
\]
For clarity, full faithfulness algebraizes u and its inverse on \(V\); their compositions are the identity by faithfulness.

Apply Lemma 5.2.3 on each connected component of \(X\) to extend (5.2j) to an algebraic horizontal isomorphism \(R\simeq Q\) on all of \(X\). Since \(R\) is curve regular by construction, \(Q\) is curve regular. In particular, for a curve \(h:C\to X\) whose image is contained in \(X\) minus \(V\), the conclusion follows by pulling back this global algebraic isomorphism. Such curves are not discarded, moved into \(V\) or implicitly treated as restrictions of curves meeting \(V\). \(\square\)

This lemma is the needed dense-open argument. Curve regularity of \(Q|_V\) alone says nothing directly about curve maps contained in the complement. The full-local-system realization and the nonsingular graph-closure theorem fill that gap.

#### The connection and regular-holonomic definitions agree

Use the definition given above: a holonomic module is regular holonomic when every simple composition factor has a presentation \(j_{!*}H\), where \(H\) is an irreducible curve-regular connection on a smooth locally closed subvariety and its inclusion j is affine.

**Theorem 5.2.** A finite-rank algebraic integrable connection \(E\) on a smooth separated complex algebraic variety \(X\) is regular holonomic under this definition if and only if \(E\) is curve regular at every compactification point of every smooth algebraic curve mapping to \(X\).

**Proof.** Reduce to connected components, which are open and closed; their inclusions are affine. A module and its subobjects split by these open-and-closed components, so every nonzero simple factor belongs to one component. A connected smooth curve maps into one such component; disconnected curves are tested componentwise. Minimal extension from a component is just its exact open-and-closed direct image. Thus both conditions are componentwise. The zero connection satisfies both conditions.

Suppose \(E\) is curve regular. By the connection subquotient argument above it is holonomic and has a finite composition series whose factors \(Q\) are simple connections. Proposition 5.2.2 makes every \(Q\) curve regular. Present \(Q\) as the minimal extension of itself under the identity inclusion \(X\to X\). This inclusion is affine even when \(X\) is not affine. The identity has no boundary, so its minimal extension is \(Q\) itself, either directly from the image definition or by the minimal-extension Theorem 4.1. Thus every simple factor meets the regular-holonomic definition.

Conversely suppose \(E\) is regular holonomic and choose a composition series. Each simple factor \(Q\) is a connection on all of this connected \(X\), of positive rank and support \(X\), by the connection subquotient argument above. The definition supplies some presentation
\[
Q\simeq j_{!*}H,\qquad j:S\hookrightarrow X,
\tag{5.2k}
\]
with \(H\) irreducible and curve regular, \(S\) smooth locally closed and j affine. If necessary remove components of \(S\) on which \(H\) has rank zero: irreducibility permits only one component of positive rank, and the inclusion of that component is open and closed, hence affine. We can therefore take \(H\) of positive rank on an integral \(S\) without changing its minimal extension or the affineness condition.

Minimal-extension uniqueness and the simple-factor classification, Theorems 4.1 and 5.1 identify the support of this presentation with the closure of \(S\) and identify its restriction to \(S\) with \(H\). Since \(Q\) has support \(X\), the closure of \(S\) is \(X\). A dense locally closed subset is open: writing \(S=O\cap Z\) with O open and Z closed, density forces \(Z=X\). Hence \(S\) is a nonempty dense smooth open, and
\[
Q|_S\simeq H.
\tag{5.2l}
\]
Lemma 5.2.4 now proves that \(Q\) is curve regular on all of \(X\). This is the step that handles a presentation made only on a dense open. It neither replaces \(S\) by \(X\) by assertion nor infers all-curve regularity from (5.2l) without proof.

All simple factors of \(E\) are therefore curve regular. Proposition 5.2.2's extension assertion, applied successively to the composition series, makes \(E\) curve regular. This proves the converse and the theorem. \(\square\)

The affineness condition is retained: it is supplied by the defining presentation in the converse and satisfied by the identity presentation in the forward direction. The proof imposes no affine hypothesis on \(X\) itself, no properness hypothesis on \(X\), and no rank-one or semisimple restriction.


### Analytic regularity of SNC meromorphic bundles

**Theorem 5.3.** Let \((Z,D)\) be a complex-manifold simple normal-crossing pair, allowing a locally finite set of globally smooth boundary components. Let \(E_\Sigma\) be the normalized logarithmic extension of any finite-rank local system supplied by Theorem 5.0. Then \(E_\Sigma(*D)\) is a coherent analytic regular holonomic left \(\mathcal D_Z\)-module. On a chart with \(k\) boundary coordinates, its characteristic variety is the union of all coordinate-intersection conormals, and each component has characteristic-cycle coefficient equal to the rank. Formula (5.3n) is a global good filtration annihilated, in its analytic associated graded, by the reduced characteristic ideal.

We use the analytic good-filtration definition in [Kashiwara's freely accessible paper, Definition 5.2](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/RiemannHilbert.pdf), printed pp. 351–352. The proof below establishes the required property directly. The normalized local model and Laurent estimates were proved in Theorem 5.0 and Lemma 5.0.2.

#### Analytic regularity and the normalized local model

As usual, the zero module is included among regular holonomic modules. For an analytic holonomic operator module \(M\), call its good-filtration condition regular when some good filtration \(F\) has analytic associated graded annihilated by the reduced ideal of its actual characteristic variety. We will prove this condition explicitly for the module below. This concerns local analytic regularity; it does not identify analytic regularity on a nonproper algebraic variety with algebraic regularity at infinity.

Let
\[
V=\Delta_z^k\times\Delta_w^m,\quad d=k+m,\quad
D=(q=0),\quad q=z_1\cdots z_k,
\qquad H=\mathcal O_V.
\tag{5.3a}
\]
Let \(W\) be a complex vector space of dimension \(r\), and let \(A_i\) commute with all eigenvalues in the half-open strip \(0\leq\operatorname{Re}\alpha<1\). Write
\[
M=H[1/q]\otimes W,\qquad
\nabla=d+\sum_{i=1}^kA_i\,d\log z_i.
\tag{5.3b}
\]
The positive-loop monodromy is \(e^{-2\pi iA_i}\). All nilpotent parts remain. Put \(v(u)=q^{-1}\otimes u\), for \(u\in W\). The module is zero for \(r=0\), in which case all the asserted regularity properties are immediate. Below assume \(r>0\).

For each multi-index \(a\in\mathbf N^k\), define
\[
C_a=\prod_{i=1}^k\prod_{\ell=1}^{a_i}(A_i-\ell I).
\tag{5.3c}
\]
Every factor is invertible: a positive integer cannot be a residue eigenvalue in the chosen strip. On a generalized eigenspace its inverse is the terminating geometric series in the nilpotent part. All factors commute. Differentiating gives exactly
\[
\partial_z^a v(u)=q^{-1}z^{-a}\otimes C_a u,\qquad
\partial_{w_j}v(u)=0.
\tag{5.3d}
\]
In particular the signs are \(A_i-\ell I\), not \(A_i+\ell I\).

#### The generated order filtration and Laurent deficits

Let \(\mathcal D\) have its ordinary analytic order filtration, and set \(F_pM=0\) for \(p<0\). Formula(5.3d) and the coordinate normal ordering of differential operators prove
\[
F_pM=\mathcal D_{\leq p}v(W)
=\sum_{\substack{a\in\mathbf N^k\\|a|\leq p}}
H\,q^{-1}z^{-a}\otimes W.
\tag{5.3e}
\]
Normal ordering is the PBW coordinate calculation already proved for differential operators; with holomorphic coefficients the same finite Leibniz argument applies. Tangential derivatives of the chosen generators vanish. Invertibility of \(C_a\) gives every displayed pole term, not only an upper bound.

The filtration is exhaustive, since each finitely bounded Laurent pole can be placed in one of these terms after increasing \(|a|\). Every \(F_p\) is a finite sum of coherent \(H\)-submodules of the common coherent lattice \(q^{-(p+1)}H\otimes W\): for \(|a|\leq p\), the factor \(q^p z^{-a}\) is holomorphic. Compatibility with the operator filtration follows from its definition by generated order. In fact
\(\mathcal D_{\leq b}F_p=F_{p+b}\) for \(p,b\geq0\): each normally ordered derivative of total order at most \(p+b\) factors into derivatives of orders at most \(b\) and \(p\), with its coefficient on the left.

Here is the exact scalar description that will prove goodness and its annihilator. For a Laurent exponent \(n\in\mathbf Z^k\), put
\[
\nu(n)=\sum_{i=1}^k\max(-n_i-1,0).
\tag{5.3f}
\]
A convergent Laurent germ belongs to the scalar filtration in (5.3e) if and only if all its nonzero terms have \(\nu(n)\leq p\). The forward implication follows by expanding the holomorphic coefficients of each pole term.

For the converse, group the Laurent terms by
\(a_i=\max(-n_i-1,0)\). Only finitely many \(a\) have \(|a|\leq p\). If \(a_i>0\), the exponent in that coordinate is fixed at \(-a_i-1\); if \(a_i=0\), its exponent is at least \(-1\). Multiplication by \(qz^a\) leaves a convergent power series in the remaining coordinates. The parameter Cauchy bounds from the Laurent proof in Lemma 5.0.2 give convergence of every grouped series on a smaller polydisc. Thus the finite grouping has exactly the form in (5.3e). This argument is entrywise for \(W\).

Consequently, in degree \(p\), the terms with \(\nu(n)<p\) disappear and distinct top-degree \(a\)'s are independent:
\[
\operatorname{gr}_p^F M
\cong
\bigoplus_{\substack{a\in\mathbf N^k\\|a|=p}}
\bigl(H/(z_i:a_i>0)\bigr)\otimes W.
\tag{5.3g}
\]
The summand is represented by \(q^{-1}z^{-a}\). Multiplication by a \(z_i\) with \(a_i>0\) lowers the deficit by one, giving zero in this graded degree. The converse independence is the uniqueness of the grouped Laurent exponents. The description is an \(H\)-module description of the graded piece; no direct-sum decomposition of the ungraded filtration is claimed.


![Laurent exponents in the two-component pole filtration](assets/snc-laurent-pole-filtration.png)

*The points represent Laurent exponents for two boundary coordinates, in the displayed finite window. Color records the exact deficit (5.3f), so \(F_p\) consists of the convergent terms with deficit at most \(p\). Differentiating the generator at \((-1,-1)\) gives the coefficient \(A_1-I\) in (5.3d); multiplication by \(z_1\) lowers the resulting filtration degree. Thus \(z_1\xi_1\) annihilates the graded module, as proved in (5.3i). The admitted regions continue rightward and upward. This is an exponent-lattice figure. Reproducible figure source.*

#### Associated graded module and the full operator presentation

Write
\[
S=H[\xi_1,\ldots,\xi_k,\eta_1,\ldots,\eta_m],
\qquad J=(z_1\xi_1,\ldots,z_k\xi_k,\eta_1,\ldots,\eta_m).
\tag{5.3h}
\]
In degree \(p\), \(S/J\) has precisely the direct summands of (5.3g), with basis monomials \(\xi^a\) and coefficient ring \(H/(z_i:a_i>0)\). The graded map
\[
(S/J)\otimes W\longrightarrow\operatorname{gr}_F M,\qquad
f\xi^a\otimes u\longmapsto
\bigl[f\,\partial_z^a v(u)\bigr]
\tag{5.3i}
\]
is an isomorphism. It respects the symbol action by construction. On each summand (5.3g) it multiplies \(W\) by \(C_a\), which is invertible; hence it has no kernel and is surjective in every degree. This proves a good filtration and the exact equality \(\operatorname{Ann}_S(\operatorname{gr}_F M)=J\).

There is also a concrete finite operator presentation. Start with the free left module \(\mathcal D\otimes W\) mapping to \(M\) by \(P\otimes u\mapsto Pv(u)\). Its relations are generated by
\[
z_i\partial_i\otimes u-1\otimes(A_i-I)u,
\qquad \partial_{w_j}\otimes u,
\tag{5.3j}
\]
for a finite basis of \(W\). These displayed relations map to zero by(5.3d).

To see they generate the entire kernel, the map is strict for the generated filtration in(5.3e). Formula(5.3i) makes its graded kernel exactly \(J\otimes W\), generated by the first-order symbols of(5.3j). Subtract lifts of a finite principal-symbol expression from any kernel element; its order strictly decreases. Repeating terminates because order is bounded below. In order zero there is no relation: \(q^{-1}\otimes W\) is an \(H\)-basis of its lattice. This proves the presentation. Analytic operator coherence was proved in Holonomic D-modules and duality, Theorem 3.0c; in particular this finite presentation defines a coherent analytic operator module.

#### The radical characteristic ideal

For each \(I\subset\{1,\ldots,k\}\), let
\[
P_I=(z_i:i\in I,\ \xi_j:j\notin I,\ \eta_1,\ldots,\eta_m).
\tag{5.3k}
\]
At a stalk on the corresponding coordinate component, these ideals are prime: their quotient is a polynomial ring over the convergent ring in the remaining coordinates, a domain by its power-series expansion. At a stalk where a defining coordinate is a unit, the corresponding ideal is the unit ideal and contributes no component. Moreover
\[
J=\bigcap_I P_I.
\tag{5.3l}
\]
Here is a direct membership proof. Modulo all \(\eta\)'s, expand in the polynomial \(\xi\)'s and convergent \(z\)'s. A monomial not divisible by any \(z_i\xi_i\) has no index at which both exponents are positive. Choose \(I\) to contain every index at which its \(\xi_i\)-exponent is positive and to omit every index at which its \(z_i\)-exponent is positive. That monomial survives in \(S/P_I\). In a power series, quotienting by these coordinate ideals only removes forbidden monomials; distinct surviving monomials do not cancel. Thus a series in every \(P_I\) has every monomial divisible by some generator \(z_i\xi_i\). Assign each such monomial to the first generator dividing it and divide by that fixed generator. There are finitely many generators, and Cauchy bounds preserve convergence after a fixed division on a smaller polydisc. This gives membership in \(J\).

The same argument proves the equality in the analytic cotangent local rings. At a point where a \(z_i\) or \(\xi_i\) is nonzero it is a unit, so that paired generator reduces to the other coordinate; if both are zero it remains their squarefree product. A nonzero \(\eta_j\) makes the localized module zero. Otherwise the convergent Taylor argument in the remaining zero coordinates is exactly the one just given. Therefore the analytic extension of \(J\) is radical.

The actual characteristic variety, including the fibre analytic structure, is
\[
\operatorname{Ch}(M)=
\bigcup_{I\subset\{1,\ldots,k\}}
\{z_i=0\ (i\in I),\ \xi_j=0\ (j\notin I),\ \eta=0\}.
\tag{5.3m}
\]
Each component has complex dimension \(d\), with \(k+m=d\) independent coordinate equations in a \(2d\)-dimensional cotangent chart. It is the conormal to the coordinate intersection \((z_i=0:i\in I)\). Formula(5.3i) gives \(r\) copies of the reduced quotient on every generic component, so its generic length and characteristic-cycle coefficient are exactly \(r\).

Thus \(M\) is holonomic and its analytic associated graded is annihilated by the reduced ideal of its actual characteristic variety. This proves the analytic regularity condition from the analytic good-filtration definition above. 

#### A global good filtration on the SNC pair

Let \(E_\Sigma\) be the normalized analytic logarithmic extension from Theorem5.0 on a simple normal-crossing pair \((Z,D)\), and put \(M=E_\Sigma(*D)\). Label the globally smooth components \(D_i\). The formula
\[
F_pM=\sum_{\substack{a_i\geq0,\ \sum a_i\leq p\\ a\text{ has finite support}}}
E_\Sigma\bigl(D+\textstyle\sum_i a_iD_i\bigr),\qquad p\geq0
\tag{5.3n}
\]
defines a coherent good filtration. Only finitely many components meet any sufficiently small chart, and all terms from components disjoint from that chart have the same trivial twist there. Hence the sum is locally the finite sum in(5.3e), even if \(D\) has infinitely many locally finite components. Effective locally finite divisor twists are defined by their local boundary equations; unit changes give the same invertible sheaf.

The local normalized isomorphism with(5.3b) is holomorphic and has holomorphic inverse, so it preserves these lattice twists and their filtration. Every preceding conclusion therefore holds on every chart. In particular(5.3n) supplies one global good filtration meeting the analytic regularity definition; no unproved locality theorem for that definition is needed.


### The natural SNC de Rham comparison

**Theorem 5.4.** Let \(j:U=Z\setminus D\hookrightarrow Z\) be the complement of an analytic simple normal-crossing divisor on a complex manifold of dimension \(d\). For any finite-rank local system \(L\) on \(U\), let \(E_\Sigma\) be its normalized logarithmic extension from Theorem 5.0. The natural maps
\[
\Omega_Z^\bullet(\log D)\otimes E_\Sigma
\longrightarrow \Omega_Z^\bullet(*D)\otimes E_\Sigma
\longrightarrow Rj_*L
\]
are quasi-isomorphisms. These are unshifted de Rham complexes. With the course's left-module convention the result is
\(\operatorname{DR}_Z(E_\Sigma(*D))\simeq Rj_*L[d]\).
All residue Jordan blocks and all boundary crossings are included.

It suffices to prove the assertion on adapted polydiscs. Theorem 5.0 supplies the model
\[
V=\Delta_z^k\times\Delta_w^m,\quad U=V\setminus D,\quad
E=\mathcal O_V\otimes W,\quad
\nabla=d+\sum_{i=1}^k A_i\,d\log z_i,\quad
T_i=\exp(-2\pi iA_i).
\tag{5.4a}
\]
The matrices \(A_i\) commute, and their spectra lie in
\(0\leq\operatorname{Re}\alpha<1\). We use the proved
analytic flat-frame equivalence, Lemma 4.1 and Theorem 4.2.
The parameter-integration and Cauchy estimates are the earlier proofs linked before Theorem 5.0; the convergent Laurent expansion is proved in Lemma 5.0.2. The smooth-resolution and finite-cover comparison arguments needed below are also given explicitly.

#### The convergent Laurent homotopy

Order the normal exterior generators \(e_i=d\log z_i\) increasingly. If normal degree is p and tangential degree is a, order all normal generators before the tangential ones. The differential is \(d_N+(-1)^p d_w\). If \(H_w\) is the ordinary tangential radial homotopy, take \(H=(-1)^pH_w\). The normal matrices commute with \(H_w\); the two normal terms in \(dH+Hd\) cancel because \(d_N\) increases the normal degree \(p\), reversing the factor \((-1)^p\) in \(H\). The remaining identity is
\[
dH+Hd=1-\operatorname{ev}_{w=0}.
\tag{5.4b}
\]
The contraction is integral in the tangential variables and never changes any z-exponent or its finite lower bound. Normal convergence and parameter differentiation follow from the explicitly proved parameter-integral estimate.

After this retraction, write a form as a normally convergent Laurent sum \(\sum_n z^n v_n\), with exterior-valued coefficients. In degree n the normal differential is
\[
d_n=\sum_j (n_jI+A_j)e_j\wedge.
\]
For n different from zero choose the least i with \(n_i\ne0\) and define
\[
h_n=(n_iI+A_i)^{-1}\iota_i .
\tag{5.4c}
\]
Here \(\iota_i(e_{j_1}\wedge\cdots\wedge e_{j_p})\) is zero unless i occurs, and otherwise is \((-1)^{a-1}\) times the exterior term with i omitted, where i is in position a. Thus
\(\iota_i\epsilon_j+\epsilon_j\iota_i=\delta_{ij}\).
Commutativity of the matrices gives \(d_nh_n+h_nd_n=1\), with this exact exterior sign.

The inverse exists because its only possible zero eigenvalue would require an eigenvalue of \(A_i\) equal to the nonzero integer -n_i, excluded by the strip. On every generalized eigenspace it is a terminating geometric series in the nilpotent part.

For \(|n_i|>2\|A_i\|\), the Neumann series gives inverse norm at most \(2/|n_i|\). Only finitely many nonzero integers remain for each of the finitely many i, and all their inverses exist. Hence a single constant bounds every \(h_n\). Absolute normally convergent coefficient sums on a smaller polydisc remain convergent after applying this bounded multiplier. No exponent changes, including negative exponents. The logarithmic complex retains only nonnegative normal exponents; the meromorphic complex retains its original finite lower Laurent bounds.

Set \(p_w=\operatorname{ev}_{w=0}\), and let \(i_w\) insert w-independent forms. If \(h_N\) is the coefficient homotopy with h_0=0, the combined homotopy is \(h=H+i_wh_Np_w\). Substitution using the commutation of \(i_w\) and \(p_w\) with the normal differential gives
\[
dh+hd=1-i_Ap_A
\tag{5.4d}
\]
at the boundary stalk, where \(p_A\) extracts the zero normal coefficient after (5.4b), and \(i_A\) inserts the constant-coefficient normal forms. The residual complex is \(K^\bullet(A_i;W)\). The logarithmic-to-meromorphic inclusion is the identity on that residual complex. This proves the Laurent homotopy, including convergence and arbitrary residue Jordan blocks.

#### Fine resolutions and actual derived sections

Here all manifolds on which we require fine acyclicity are open subsets of real Euclidean space: \(U\), its open subsets, and the sector products below. A direct partition construction suffices.

Let \(O\) be such an open set with any open cover. For n positive set
\[
K_n=\{x\in O:|x|\leq n,\ 
\operatorname{dist}(x,\mathbb R^N\setminus O)\geq 1/n\},
\]
interpreting the distance as infinite if the complement is empty, and put \(K_0\) and \(K_{-1}\) empty. These sets are compact, exhaust \(O\), and satisfy \(K_n\subset\operatorname{int}K_{n+1}\). The compact band \(K_n\setminus\operatorname{int}K_{n-1}\) can be covered by finitely many smaller balls whose concentric larger closed balls lie in assigned cover members, in \(\operatorname{int}K_{n+1}\), and outside K_{n-2}. Such balls exist since the band misses K_{n-2}. All the smaller balls together cover \(O\). The larger balls are locally finite: near any point choose a neighbourhood inside some \(\operatorname{int}K_N\); all bands with n at least N+2 miss that neighbourhood, and there are only finitely many balls in the remaining bands.

On each larger ball use a smooth positive bump, zero outside its closed ball. For example \(e^{-1/s^2}\) for \(s=r^2-|x-a|^2>0\), extended by zero for s nonpositive, is smooth: successive derivatives are a polynomial in 1/s times the exponential, and the exponential-series bound dominates every such polynomial and its difference quotient at zero. The locally finite sum of these bumps is positive. Divide each by that sum. This proves the required smooth subordinate partition, with compact supports, including the boundary smoothness and local finiteness. The zero-dimensional and empty open sets are immediate.

Let \(\mathcal S=\mathcal C^\infty_O\) denote the sheaf of complex-valued smooth functions. Global sections are exact on \(\mathcal S\)-modules. Given a local lift of a section of a quotient on each cover member, multiply by the corresponding partition functions and extend by zero; the support is closed and contained in that member, so gluing with zero is valid. Their locally finite sum is a global lift. Kernels give left exactness.

Sheaves of modules and their derived categories, Theorem 5.4, supplies enough injectives for \(\mathcal S\)-modules. Forgetting to complex-vector-space sheaves preserves injectives: its left adjoint \(\mathcal S\otimes_\mathbb C-\) is exact on stalks. An injective \(\mathcal S\)-module resolution is consequently an injective complex-sheaf resolution, and exactness of global sections makes every \(\mathcal S\)-module acyclic for sections. This applies on every open subset of \(O\).

For completeness, the homotopy identity used here can be checked without a separate topological theorem. For a smooth homotopy \(F:O\times[0,1]\to O'\), write
\(F^*\alpha=\beta_t+dt\wedge\gamma_t\) and define \(H\alpha=\int_0^1\gamma_t\,dt\). The dt component of \(d(F^*\alpha)\) is \(\partial_t\beta_t-d_O\gamma_t\). Integration and the fundamental theorem give
\(d_OH+Hd=F_1^*-F_0^*\).
For the radial homotopy from a point to \(x\), this integrates the contraction with the radial vector field; in degree zero it gives the function minus its value at that point. Parameter differentiation justifies the calculation, and the same argument for holomorphic coefficients proves the tangential homotopy used in the Laurent homotopy argument above. Thus smooth de Rham forms on a convex lifted sector have only constant cohomology in degree zero.

Let \(L\) be the horizontal local system. The smooth flat de Rham complex \(\mathcal A^\bullet(L)\) resolves \(L\). In a local flat frame the preceding contraction proves exactness. Each term is an \(\mathcal S\)-module and hence acyclic. The bounded-below acyclic-term comparison, Theorem 6.1(4), therefore identifies
\[
R\Gamma(O,L)=\Gamma(O,\mathcal A^\bullet(L))
\tag{5.4e}
\]
in the derived category, compatibly with its augmentation from \(L\).

The same resolution computes \(Rj_*L\) by \(j_*\mathcal A^\bullet(L)\). To check this assertion directly, take a complex-sheaf injective resolution. Restrictions to an open remain injective by Corollary 5.5 of the same sheaf lesson. Thus at x the stalk of \(R^aj_*F\) is the filtered colimit of \(H^a(B\cap U,F)\) over neighbourhoods \(B\): stalks are such colimits, and filtered colimits of vector spaces are exact and commute with complex cohomology. For a smooth-form term F those groups vanish for a positive by the proved open-set acyclicity. The bounded acyclic-term comparison for j_* now applies.

Consequently the actual natural map of complexes representing the de Rham comparison is
\[
\Omega_V^\bullet(*D)\otimes E
\longrightarrow j_*\mathcal A^\bullet(L).
\tag{5.4f}
\]
The map restricts to \(U\) and regards each holomorphic flat form as a smooth flat form.
On \(U\) the two inclusions from \(L\) into holomorphic and smooth flat de Rham forms commute, and both are local resolutions. This verifies that (5.4f) represents the adjunction de Rham-to-\(Rj_*L\) map with its ordinary identification on \(U\); it is not a separately chosen derived isomorphism.

#### Two arcs and the finite Čech resolution

Fix positive radii \(r_i\) inside the polydisc and w=0. Use angle \(\theta_i\) increasing from zero to \(2\pi\); set \(u_i=i\theta_i\) along the chosen torus. Backwards transport from a point of a lifted path to the base point identifies coefficients with \(W\) by multiplication by
\[
\exp\!\left(\sum_i u_iA_i\right).
\]
Forward parallel transport has matrix \(T_i\), whereas these coefficients satisfy the deck relation with
\[
R_i=T_i^{-1}=\exp(2\pi iA_i).
\tag{5.4g}
\]
There is no replacement of the actual positive-loop monodromy by its inverse; the inverse occurs in the backwards coefficient trivialization.

For one angle take \(0<\varepsilon<\pi/4\) and the arcs represented by
\[
I_0=(-\varepsilon,\pi+\varepsilon),\qquad
I_1=(\pi-\varepsilon,2\pi+\varepsilon).
\tag{5.4h}
\]
Their intersection has two components. Call the component at \(\pi\) the middle seam and the one at zero the end seam. At the middle seam the chosen lifts and backwards frames agree. At the end seam use the \(I_1\) lift near \(2\pi\); the coefficient from the \(I_0\) lift near zero is multiplied by \(R\). Thus, with Čech differential section 1 minus section 0, the local-system Čech complex is
\[
C^0=W\oplus W,\quad C^1=W\oplus W,\quad
\delta(a,b)=(b-a,\ b-Ra).
\tag{5.4i}
\]
The first entry of \(C^1\) uses the middle frame; the second uses the end frame.

Define a projection to the oriented-circle complex \(K^0=W,\ K^1=W,\ d_K=R-I\) by
\[
p^0(a,b)=a,\qquad p^1(c,d)=c-d.
\tag{5.4j}
\]
A section and contraction are
\[
\begin{aligned}
i^0(v)&=(v,v),& i^1(v)&=(0,-v),&
h(c,d)&=(0,c).
\end{aligned}
\tag{5.4k}
\]
Direct substitution gives \(pi=1\), \(\delta i=id_K\), and
\(\delta h+h\delta=1-ip\). Thus this is a proved chain retraction, with the sign selecting the positive orientation from zero through \(\pi\) to \(2\pi\).

For k angles use the \(2^k\) sector-product cover of \(U\), with the corresponding radial variables and w variables unrestricted. It is more convenient to totalize its k successive two-cover Čech resolutions than to keep the redundant ordinary Čech complex of the \(2^k\) sets. This is a genuine finite open-cover resolution: in each coordinate the augmented two-cover complex is exact, and its contraction locally chooses a cover member containing the point. Iterating these finite exact resolutions gives the augmentation for the product cover. Its terms are finite direct sums over the connected components of sector intersections.

Every such connected component has convex logarithmic coordinates: log-radius in an open interval, angle in one of the intervals in (5.4h) or an overlap interval, and real coordinates of w in a convex polydisc. The local system is trivial there. The real radial homotopy in a flat frame and (5.4e) give its higher-cohomology vanishing.

Here is also a direct resolution comparison, avoiding any assumption that open direct image is exact. Let \(B\) be the iterated Čech complex of local-system sections and let \(C\) be the total iterated Čech complex of smooth flat forms. Inclusion
\[
b:B\longrightarrow C
\]
is a quasi-isomorphism: in every sector component the smooth complex has cohomology only the constant sections in degree zero. Finite filtration by Čech degree, and induction on the short exact sequences of that filtration, proves the total assertion. The augmentation
\[
a:\Gamma(U,\mathcal A^\bullet(L))\longrightarrow C
\tag{5.4l}
\]
is also a quasi-isomorphism. Indeed, for each two-cover the Čech sequence of each smooth-form sheaf is exact on sections. Surjectivity can be written explicitly: given c on the overlap, choose a subordinate pair \(\chi_0+\chi_1=1\), take \(-\chi_1c\) on the first open and \(\chi_0c\) on the second, extending by zero; their difference is c. Apply this in every coordinate. Filter the augmentation cone by form degree: its associated graded complexes are these exact Čech rows, so finite induction makes the cone acyclic. For b use instead the filtration by Čech degree and the already proved sector-form quasi-isomorphisms. All Čech degrees and all smooth form degrees are bounded here. Therefore the finite complex \(B\) computes actual derived sections through the concrete zigzag \(B\xrightarrow{b}C\xleftarrow{a}\Gamma(U,\mathcal A^\bullet(L))\).

#### Čech reduction equals backwards-transport integration

First retract the logarithmic radial coordinates to their chosen \(r_i\) and the tangential coordinates to zero, without changing angles. On each lifted sector this is a real convex homotopy with flat coefficients, and it agrees on overlaps because every transition is a constant \(R_i\). Restriction to the torus therefore gives a chain homotopy equivalence of smooth-form Čech totals. Local-system constants are unchanged. Denote the resulting angular Čech total by \(C_{\mathrm{ang}}\).

For one angle the angular de Rham degree a is zero or one, and the Čech degree p is zero or one. Totalize as \(D=\delta+(-1)^p d_\theta\). In total degree zero an element is a pair of functions \((f_0,f_1)\). In degree one it is
\[
(g_0\,d\theta,\ g_1\,d\theta;\ c,\ d),
\]
with the last pair functions on the middle and end seams in their chosen frames. Define
\[
\begin{aligned}
F^0(f_0,f_1)&=f_0(0),\\
F^1(g_0,g_1;c,d)
&=\int_0^\pi g_0(\theta)\,d\theta
 +\int_\pi^{2\pi}g_1(\theta)\,d\theta
 +c(\pi)-d(2\pi),\\
F^q&=0\quad(q\geq2).
\end{aligned}
\tag{5.4m}
\]
This is a chain map to \(K^\bullet(R-I;W)\). The only nontrivial degree check is on a degree-zero element:
\[
\begin{aligned}
F^1D(f_0,f_1)
={}&f_0(\pi)-f_0(0)+f_1(2\pi)-f_1(\pi)\\
 &+[f_1(\pi)-f_0(\pi)]
   -[f_1(2\pi)-Rf_0(0)]\\
={}&(R-I)f_0(0).
\end{aligned}
\tag{5.4n}
\]
The remaining degrees land in zero target degrees. This proof also works with coefficients in any complex of forms in the other variables: evaluation and integration commute with their differential and with all other commuting transition matrices.

On the inclusion of local-system Čech constants, F is exactly the reduction p in (5.4j). On the augmentation of global angular forms, the seam terms are zero, so F is exactly backwards-transport integration around the positive circle. This is equality of chain maps, not only equality on cohomology classes.

For multiple coordinates totalize the pairs in the interleaved order
\[
(p_1,a_1),\ (p_2,a_2),\ldots,(p_k,a_k).
\]
The differential in the i-th pair is
\[
(-1)^{\sum_{j<i}(p_j+a_j)}
\bigl(\delta_i+(-1)^{p_i}d_{\theta_i}\bigr).
\tag{5.4o}
\]
The standard total order with all Čech degrees first and all form degrees second is converted to this order by multiplication in each multidegree by
\[
(-1)^{\sum_{i<j}a_ip_j}.
\tag{5.4p}
\]
When \(p_i\) increases, the flip exponent changes by \(\sum_{j<i}a_j\), adding exactly the missing earlier form degrees to the standard Čech sign. When \(a_i\) increases, it changes by \(\sum_{j>i}p_j\); adding this to the standard form sign \(\sum_jp_j+\sum_{j<i}a_j\) leaves \(\sum_{j\leq i}p_j+\sum_{j<i}a_j\), as in (5.4o). On global-form augmentation all \(p_i\) are zero, and on constant Čech inclusion all \(a_i\) are zero; therefore the flip has sign one on both sides of the required comparison diagram.

Apply the maps (5.4m) one coordinate at a time, with the order (5.4o). They commute with the remaining operators. The resulting map
\[
\mathcal F:C_{\rm ang}\longrightarrow K^\bullet(R_i-I;W)
\tag{5.4q}
\]
is a chain map. Its composite with the constant Čech inclusion is exactly the iterated projection (5.4j). The latter is a chain homotopy equivalence: apply (5.4k) in each coordinate, multiplying its contraction in the i-th coordinate by \((-1)^{\sum_{j<i}p_j}\) to cancel the other coordinate differentials. After an earlier coordinate has been reduced, its Koszul degree replaces \(p_j\) in this sign. All matrices involved commute. Finite induction proves the retraction.

Since b and the radial restriction are quasi-isomorphisms, and \(\mathcal F b\) is this retraction, \(\mathcal F\) is a quasi-isomorphism too. Most importantly, its composite with the actual smooth-form augmentation and radial restriction is the cubical period map:
\[
\begin{aligned}
\mathcal I^p(\alpha)_I
={}&
\int_{[0,2\pi]^I}
\operatorname{PT}_{\gamma_I}^{-1}(\gamma_I^*\alpha),\\
I={}&\{i_1<\cdots<i_p\}.
\end{aligned}
\tag{5.4r}
\]
Here the coordinates outside I have angle zero, all radii are \(r_i\), w=0, the integration orientation is \(d\theta_{i_1}\wedge\cdots\wedge d\theta_{i_p}\), and the backwards transport uses the lifted paths with those increasing angles. For p zero this is evaluation at the base point.

The following figure records the chain maps computing the actual comparison.


The composite of restriction, smooth-form augmentation, radial restriction and \(\mathcal F\) is exactly \(\mathcal I\). On the sector-constant complex its composite is exactly the proved Čech retraction. The augmentations and sector-constant comparisons used to identify the target were proved quasi-isomorphisms above. This verifies the natural map rather than selecting an abstract isomorphism between its source and target cohomology.

![The two overlaps and the actual chain-map comparison](assets/snc-period-comparison.png)

*The two colored arc portions, together with the purple overlap portions, lie on the same circle; \(\varepsilon=\pi/8\) in this drawing. The upper arc is \(I_0\) and the lower arc is \(I_1\). Positive orientation runs leftward at the top and rightward at the bottom. The end seam uses the \(I_1\) lift near \(2\pi\), forcing \(R\) in (5.4i). The right panel displays the actual comparison whose one-coordinate chain map is (5.4m), and the lower panel is its zero-Laurent restriction (5.4t). Exact proof locators: (5.4i)–(5.4p), (5.4s)–(5.4u). Reproducible figure source. Earlier freely accessible human reading for the normalized logarithmic model: [Deligne, IAS author edition, Chapter II, Section 5](https://publications.ias.edu/sites/default/files/Number9.pdf); all new period and Čech arguments are proved here.*

#### The oriented cube differential

Write the Koszul differential as \(\sum_i e_i\wedge(R_i-I)\). In an increasing index set \(J=\{j_1<\cdots<j_{p+1}\}\), its component is
\[
(d_Kv)_J
=\sum_{a=1}^{p+1}(-1)^{a-1}
(R_{j_a}-I)v_{J\setminus\{j_a\}}.
\tag{5.4s}
\]
This is also the exact integration boundary formula. For the positively oriented J-cube, its boundary is the signed sum
\[
\sum_a(-1)^{a-1}
\bigl(\text{face }\theta_{j_a}=2\pi-
      \text{face }\theta_{j_a}=0\bigr),
\]
with the remaining coordinates in increasing order. On the upper face backwards coefficients are R_{j_a} times those on the lower face. The coefficient matrices commute with transport in all remaining directions. Iterated one-variable integration and the fundamental theorem of calculus therefore give
\(\mathcal I(d_\nabla\alpha)=d_K\mathcal I(\alpha)\).
This proves the needed Stokes identity directly for each exterior component; no independent general Stokes theorem is imported.

The signs in (5.4o)–(5.4p), the seam subtraction in (5.4m), the face signs in (5.4s), and the minus sign in the original forward monodromy \(T_i\) are mutually consistent. Replacing \(R_i\)-I by \(T_i\)-I would require an additional explicit coordinate cochain isomorphism; it is not done here.

#### Invertible periods and the natural comparison

For a zero-Laurent coefficient \(v_I\) in the normalized frame, the associated form is \(v_I\,d\log z_{i_1}\wedge\cdots\wedge d\log z_{i_p}\). On its cube,
\[
\operatorname{PT}^{-1}\gamma_I^*\alpha
=\exp\!\left(\sum_{i\in I}u_iA_i\right)v_I
\,du_{i_1}\wedge\cdots\wedge du_{i_p}.
\]
Use ordered iterated integration of this finite-dimensional continuous matrix-valued function on the compact rectangle. Factor the commuting exponentials and pull the independent factors through each one-variable integral. The period is
\[
\mathcal I^p i_A(v)_I
=\left(\prod_{i\in I}Q_i(A_i)\right)v_I,\qquad
Q_i(A_i)=\int_0^{2\pi i}e^{uA_i}\,du.
\tag{5.4t}
\]
For the empty I the product is the identity. The factors of i from \(du_i=i\,d\theta_i\) are already included in each \(Q_i\); there is no additional phase. Thus these are the actual comparison periods on the proved Laurent retract.

Differentiating the matrix exponential and integrating gives \(Q_i(A_i)A_i=R_i-I\). For a scalar eigenvalue alpha, its value is \(2\pi i\) at zero and \((e^{2\pi i\alpha}-1)/\alpha\) otherwise. Its only possible nonzero zeros are nonzero integers, excluded by the strip. On a generalized eigenspace the value is the finite Taylor polynomial in the nilpotent part, with nonzero scalar leading coefficient; its inverse is another terminating geometric series. Every \(Q_i\) is therefore invertible, including all commuting Jordan blocks, and commutes with every \(A_j\) and Q_j.

The finite map (5.4t) is consequently a chain isomorphism \(K^\bullet(A_i;W)\to K^\bullet(R_i-I;W)\), with the differential (5.4s). To connect it with the full natural source, use the actual homotopy (5.4d):
\[
\mathcal I-\mathcal I i_Ap_A
=d_K(\mathcal I h)+(\mathcal I h)d_\nabla.
\tag{5.4u}
\]
All operations are defined on smaller polydiscs: h preserves normal convergence and finite pole bounds, and \(\mathcal I\) integrates smooth forms along a compact torus disjoint from D. Thus this is an actual chain homotopy, not a formal exchange of divergent Laurent sums. It identifies the full natural comparison with the isomorphism (5.4t) on the proved Laurent retract.

Taking boundary stalks is legitimate. Shrinking polydiscs are cofinal; each meromorphic germ is represented with finite pole bounds on one of them. The fine-resolution model for \(Rj_*L\) applies on every one. On each sufficiently small polydisc choose radii inside it: the exact diagram and (5.4t) prove the quasi-isomorphism for its finite-pole coefficient complex and its target of smooth forms. Those actual maps (5.4f), independent of the chosen radii, commute with restriction. Their filtered colimit therefore gives the stalk comparison. This uses no asserted equality of the radius-dependent period chain models. The bounded coefficient multiplier in (5.4c) preserves convergence on every compact subpolydisc, so it defines the homotopy throughout the original open polydisc as well as at its stalk.

It follows that the actual natural maps
\[
\Omega_V^\bullet(\log D)\otimes E
\longrightarrow
\Omega_V^\bullet(*D)\otimes E
\longrightarrow Rj_*L
\tag{5.4v}
\]
are quasi-isomorphisms in the normalized regular model. At a point on fewer components, repeat the same proof with precisely those boundary coordinates. Off D use the ordinary analytic flat Poincaré lemma. This retains every crossing, arbitrary finite rank and all nilpotent parts.


### Algebraic de Rham comparison for regular connections

**Theorem 5.5.** Let \(X\) be any smooth separated finite-type complex algebraic variety. Let \((E,\nabla)\) be a finite-rank integrable algebraic connection regular along every algebraic curve, including infinity, and let \(L=\ker\nabla^{\mathrm{an}}\) be its horizontal local system. Restriction of algebraic forms to analytic forms, followed by the analytic flat de Rham augmentation, induces a natural quasi-isomorphism
\[
R\Gamma\bigl(X,(\Omega_X^\bullet\otimes E,\nabla)\bigr)
\longrightarrow R\Gamma(X^{\mathrm{an}},L).
\tag{5.5a}
\]
Both de Rham complexes here are unshifted. With the lesson12 left-module convention, on each connected component of dimension \(d\) apply the common shift \([d]\) to both sides. The theorem allows nonproper and non-quasi-projective \(X\), arbitrary rank and residue Jordan blocks.

This is the regular-coefficient comparison discussed in [Deligne's freely accessible IAS-hosted lecture notes, Chapter II, Theorem 6.2](https://publications.ias.edu/sites/default/files/Number9.pdf). We prove it below using the preceding SNC results and the exact earlier cohomology theorems.

The comparison in (5.5a) is defined before choosing a compactification. If \(a:X^{\mathrm{an}}\to X\) is the continuous map to the Zariski space, restriction gives a map of complexes of complex-vector-space sheaves from algebraic forms to \(a_*\) of analytic forms. It commutes with the connection differential because analytic differentiation restricts to algebraic differentiation. Passing to derived sections gives the comparison to analytic de Rham cohomology. The analytic flat-frame proof, Lemma 4.1 and Theorem 4.2, and the holomorphic Poincaré proof, Proposition 1.2, identify the latter complex with \(L\). The augmentation from \(L\) is a natural quasi-isomorphism; its inverse in the derived category introduces no choice of bases or periods.

Theorem 5.1 provides a smooth proper compactification \(P\) of \(X\) with SNC boundary \(D\), including non-quasi-projective \(X\). It also supplies the normalized algebraic logarithmic bundle \((\bar E,\bar\nabla)\) on \(P\), restricting to \((E,\nabla)\). These assertions were proved there using the earlier Nagata, resolution and full proper GAGA proofs. Write \(j:X\hookrightarrow P\).

We first prove the algebraic pole-removal step; it has no analytic convergence assumption.

#### Removing finite algebraic pole layers

**Lemma 5.5.1.** On a smooth algebraic SNC pair over \(\mathbf C\), let \((F,\nabla)\) be an integrable logarithmic bundle all of whose boundary residue eigenvalues lie in \(0\leq\operatorname{Re}\alpha<1\). Then
\[
(\Omega_P^\bullet(\log D)\otimes F,\nabla)
\longrightarrow
(\Omega_P^\bullet(*D)\otimes F,\nabla)
\tag{5.5b}
\]
is a quasi-isomorphism of complexes of complex-vector-space sheaves.

**Proof.** Work locally in étale coordinates \(z_1,\ldots,z_k,w_1,\ldots,w_m\) adapted to the SNC divisor, and choose a frame of \(F\). Such coordinates are the smooth SNC coordinates used in the earlier local construction. Write \(e_i=d\log z_i\). The local logarithmic connection is
\[
\nabla=d+\sum_i B_i e_i+\sum_\ell C_\ell\,dw_\ell,
\tag{5.5c}
\]
where all matrix entries are regular. No constant-matrix algebraic gauge is assumed.

Fix a boundary coordinate \(z_i\). Allow any already chosen other boundary coordinates to be inverted; localization is exact and preserves the connection identities. For \(n\geq0\), the logarithmic complex with coefficients \(z_i^{-n}F\) is stable under the differential: differentiating \(z_i^{-n}\) contributes only \(-n e_i\). There are termwise injective inclusions from the \(n-1\) complex into the \(n\) complex. Their quotient, for \(n\geq1\), is the complex supported on \(D_i=(z_i=0)\) with coefficient bundle
\[
F|_{D_i}\otimes\mathcal O_P(nD_i)|_{D_i}.
\tag{5.5d}
\]
Indeed, multiplication by \(z_i^n\) identifies its local coefficient module with \(F/z_iF\). Logarithmic forms are locally free with basis the \(e_j,dw_\ell\), so tensoring their degree pieces preserves this quotient description. The line twist in (5.5d) records the normal-frame changes; it is not globally replaced by a trivial bundle.

Locally separate the exterior generator \(e_i\) from all remaining generators, putting \(e_i\) first. On this quotient the differential is
\[
d_Q=\delta+e_i\wedge N_i,\qquad
N_i=\operatorname{Res}_{D_i}(\nabla)-nI.
\tag{5.5e}
\]
Here \(\delta\) is the tangential connection differential, with its exterior sign when acting on a term containing \(e_i\). Derivatives \(z_i\partial_i\) of regular coefficients vanish modulo \(z_i\); therefore the normal differential is exactly the displayed residue minus \(n\).

The endomorphism \(N_i\) is invertible. At every complex closed point its eigenvalues are \(\alpha-n\), which cannot be zero in the specified strip. Its determinant is thus a unit locally: any nonempty determinant-zero locus on this finite-type complex scheme would contain a closed point, by the earlier closed-point Nullstellensatz test. The adjugate formula supplies its inverse in the algebraic coefficient ring, and localization in other coordinates preserves it. Nilpotent residue parts cause no exception.

Integrability makes \(N_i\) parallel for \(\delta\). Explicitly, the commutator of \(z_i\partial_i+B_i\) with each tangential connection operator is zero. Modulo \(z_i\), its derivative in the normal direction disappears, leaving
\[
V(B_i|_{D_i})+[B_V|_{D_i},B_i|_{D_i}]=0
\quad\text{for each tangential operator }V+B_V.
\]
Equivalently, the tangential connection commutes with the residue endomorphism. Differentiating \(N_iN_i^{-1}=I\) then gives the same commutation for \(N_i^{-1}\).

Let \(\iota_i\) be contraction with the normal exterior generator. It anticommutes with the tangential exterior differential and satisfies
\(\iota_i(e_i\wedge\,\cdot)+e_i\wedge\iota_i=1\).
Consequently the actual algebraic map
\[
h_Q=N_i^{-1}\iota_i
\quad\hbox{satisfies}\quad
d_Qh_Q+h_Qd_Q=1.
\tag{5.5f}
\]
Thus every finite added-pole quotient is contractible. The short exact sequence of complexes makes every finite inclusion a quasi-isomorphism.

The union over \(n\) gives localization in \(z_i\). Filtered colimits of modules, and of their underlying complex-vector-space sheaves, are exact on stalks; they therefore commute with cohomology of these complexes. This union preserves the quasi-isomorphism. Repeat for each of the finitely many boundary coordinates in the chart. Every meromorphic algebraic section has a finite denominator power in each coordinate. After all localizations, logarithmic and ordinary differential forms have the same basis module because every \(z_i\) is a unit. This gives precisely the right-hand complex in (5.5b).

The inclusions in (5.5b) are intrinsic, so these stalkwise proofs prove the global quasi-isomorphism. The contractions need not agree on overlaps: only acyclicity of the quotient is used for that global conclusion. Off the boundary the inclusion is already the identity. The zero-rank and boundary-free cases are immediate. \(\square\)

#### The affine open and its meromorphic complex

The open immersion \(j\) is affine. Here is the affine-base check even if its boundary ideal on an affine open is not principal. The quasi-coherent algebra
\(\mathcal A=\bigcup_{n\geq0}\mathcal O_P(nD)\) has, on a neighbourhood with boundary equation \(q\), the algebra \(\mathcal O_P[1/q]\). Its relative spectrum is therefore locally the distinguished open \(D(q)\); these identifications agree in their common rational-function algebra and glue to \(X\). On any affine \(V=\operatorname{Spec}R\), the affine sheaf/module equivalence, Theorem 1.2 identifies \(\mathcal A|_V\) with the algebra associated to \(A=\Gamma(V,\mathcal A)\). Its relative spectrum there is \(\operatorname{Spec}A\): on every distinguished open \(D(f)\subset V\), the rings are \(A_f\), by the same localization equivalence. Thus \(j^{-1}V\) is affine for every affine \(V\), proving the assertion. The algebra is quasi-coherent because each divisor twist is invertible and filtered unions preserve quasi-coherence on these local module charts.

Degree by degree, localization gives the intrinsic equality
\[
j_*(\Omega_X^p\otimes E)
=\Omega_P^p(*D)\otimes\bar E.
\tag{5.5g}
\]
The equality is first the elementary module formula on \(D(q)\), where sections are localized at \(q\); it glues because both sides are the subsheaf of rational forms restricting to the given regular form on the open. The connection differentials agree by the same Leibniz calculation.

Cohomology of affine schemes and Serre's criterion, Theorems 2.2 and 3.2, proves that every quasi-coherent sheaf is \(j_*\)-acyclic for this affine morphism. This applies to each \(\Omega_X^p\otimes E\), including its underlying sheaf cohomology. The complex has only degrees zero through \(\dim X\). The bounded acyclic-term comparison, Theorem 6.1(4) therefore identifies its derived open image with its ordinary termwise image (5.5g), even though its differential is \(\mathbf C\)-linear rather than \(\mathcal O\)-linear.

Composing derived sections with this derived image gives
\[
\begin{gathered}
R\Gamma\bigl(X,\Omega_X^\bullet\otimes E\bigr)
\\ \simeq
R\Gamma\bigl(P,\Omega_P^\bullet(*D)\otimes\bar E\bigr)
\\ \simeq
R\Gamma\bigl(P,\Omega_P^\bullet(\log D)\otimes\bar E\bigr).
\end{gathered}
\tag{5.5h}
\]
The last arrow is the inverse of the proved inclusion (5.5b). Composition of derived sections and direct image here is the usual sheaf identity: direct image preserves injectives as right adjoint to exact inverse image of complex-vector-space sheaves. Thus no unproved nonproper coherent or analytic direct-image comparison has entered.

#### Proper GAGA for the complex-linear differential

Each degree \(\Omega_P^p(\log D)\otimes\bar E\) is coherent. Proper cohomological GAGA, Theorem 6.7, proves the natural cohomological comparison for every coherent sheaf on every proper complex scheme, including nonprojective ones.

We apply it to the finite logarithmic complex as a complex of \(\mathbf C\)-sheaves. Its differential is not \(\mathcal O_P\)-linear, so this requires the following explicit naturality check rather than treating it as a complex in the coherent \(\mathcal O_P\)-module category.

Restriction of algebraic logarithmic forms gives a map of \(\mathbf C\)-sheaf complexes into the analytic logarithmic complex under \(a:P^{\mathrm{an}}\to P\). In every frame it commutes with exterior differentiation and with the algebraic connection matrices in (5.5c). On each individual term its map on cohomology is exactly the canonical GAGA map from Theorem 6.7, since both maps extend the same restriction on sections. Derived restriction/adjunction is natural for these \(\mathbf C\)-linear sheaf maps.

Filter both derived-section totals by logarithmic degree. Their first pages are the cohomology of those individual coherent terms. The actual restriction map just constructed is an isomorphism on every first-page group by GAGA and respects all differentials. The filtration has \(\dim X+1\) columns, hence the filtration of each total degree is finite. Kernels and quotients give isomorphisms on each subsequent page, and induction over the finite abutment filtration proves
\[
\begin{gathered}
R\Gamma\bigl(P,\Omega_P^\bullet(\log D)\otimes\bar E\bigr)
\\ \simeq
R\Gamma\bigl(P^{\mathrm{an}},
 \Omega_{P^{\mathrm{an}}}^\bullet(\log D^{\mathrm{an}})
 \otimes\bar E^{\mathrm{an}}\bigr).
\end{gathered}
\tag{5.5i}
\]
Analytification of these logarithmic bundles is the displayed analytic bundle: their local free bases \(d\log z_i,dw_\ell\), algebraic transition matrices and connection formula simply extend to holomorphic coefficients. Exact coherent analytification was proved earlier; no infinite meromorphic union is passed through GAGA.

#### The intrinsic global comparison

Theorem 5.4, now already proved earlier in this lesson, identifies the analytic logarithmic complex in (5.5i) with \(Rj^{\mathrm{an}}_*L\) by the actual natural map. Taking derived sections gives \(R\Gamma(X^{\mathrm{an}},L)\).

Combining (5.5h), (5.5i) and this analytic SNC comparison proves an isomorphism between the two sides of (5.5a). It proves the specified natural map itself. Indeed the restriction map from the algebraic logarithmic complex to the analytic one commutes with restriction to \(X\) and with both inclusions into meromorphic forms. The algebraic localization equality (5.5g) is restriction of the same forms. The analytic map of Theorem 5.4 is restriction into smooth flat forms, commuting with the local-system augmentation. These are exactly the maps used to define (5.5a). Their derived-section diagram therefore commutes, and its other arrows are the proved quasi-isomorphisms. The remaining arrow (5.5a) is consequently a quasi-isomorphism.

This also proves independence of compactification and of the normalized lattice used in the proof: the comparison (5.5a) was defined intrinsically on \(X\). It is natural in every horizontal algebraic bundle map; all restriction, augmentation and inclusion maps in its construction are natural, and Theorem 5.0 extends such maps to the normalized boundary bundles.

With \(E=\mathcal O_X\) and its ordinary differential, this gives the full algebraic de Rham comparison with complex constant-sheaf cohomology. The proof does not assert general singular regular-holonomic RH, any arbitrary nonproper D-module comparison, or analytic proper-image regularity. Those retain their original required scope.


### Gauss–Manin regularity on every smooth base

For a smooth algebraic map with regular coefficient connection, the generic relative de Rham images are finite-rank regular integrable connections. Theorem 5.6 below proves this for every smooth separated finite-type complex base, with no properness or quasi-projectivity assumption on the original map. We first construct its logarithmic lattices over a curve, then prove integrability and base change along every curve on the general base.

Freely accessible reading: [Deligne, Chapter II, Theorem 7.9 and Lemma 7.10](https://publications.ias.edu/sites/default/files/Number9.pdf), printed pp. 113–120. The proof here supplies the lattice, corrected Čech action, finite flat-complex base change and actual transfer calculation; that reading reference replaces none of those arguments.

#### The curve lattice and the completed pair

**Lemma 5.6.1 (the curve lattice).** Let \(f:X\to C\) be a smooth morphism of smooth separated finite-type complex varieties, with \(C\) a smooth connected algebraic curve. Let \((E,\nabla)\) be an integrable algebraic connection on \(X\), regular along every algebraic curve including infinity.

There is a dense open \(C_0\subset C\) such that
\[
H^a=R^a f_*(\Omega_{X/C}^\bullet\otimes E)|_{C_0}
\]
are finite-rank regular connections, with the actual Gauss–Manin action constructed below. Every such generic image has a logarithmic lattice at every point of the smooth complete model \(\bar C\). All ranks and residue Jordan blocks are allowed.

We use the following rank criterion for maps between smooth complex algebraic varieties. Such a map is smooth at a point exactly when its differential is surjective there. Necessity follows from the differential basis in a standard smooth chart. For sufficiency, choose étale coordinates \(y_1,\ldots,y_b\) on the base and complete their pulled-back differentials to a source coframe with differentials of additional local functions. The chosen-coordinate theorem, Smooth morphisms, Theorem 4.1 applied to the source over \(\mathbf C\), makes the resulting source coordinate map étale over affine space. The target, the product of the base with the additional affine coordinates, is étale over the same affine space. A morphism between two such étale objects is étale: in a square-zero lifting problem, first take the unique source lift over affine space; its map to the target agrees with the prescribed target map by the target's own uniqueness. Finite presentation follows from the finite-type affine presentations over the Noetherian target. Composition with the smooth affine projection to the original base proves sufficiency. Thus Jacobian rank failure is precisely the critical locus used below. The same chosen-coordinate argument allows prescribed independent boundary functions to be retained among the relative coordinates.

Take a smooth proper absolute compactification \(Z\) of \(X\) with a morphism \(g:Z\to\bar C\) extending \(f\). Namely, take the closure of the graph in an absolute compactification times \(\bar C\), and resolve/principalize outside the smooth open. Nagata existence, Appendix N, Theorem N.E.1, and resolution and SNC compactification, Theorem 4.8 and Corollary 5.2, provide these operations and preserve \(X\).

Remove from \(C\) the finitely many bad values of \(g\) and of its finitely many closed boundary intersections, obtaining \(C_0\), so that \(g\) and every horizontal boundary intersection are smooth over \(C_0\). Each bad image is closed by properness. Here is the needed rank and image argument. A function field dominating the curve has a transcendence basis containing its nonconstant local base parameter \(t\). The derivation sending \(t\) to one and the remaining basis elements to zero extends through the finite algebraic field extension: differentiating the minimal polynomial of an algebraic element solves for its derivative because its polynomial derivative is nonzero in characteristic zero. Thus \(dt\) is nonzero in that function field. The smooth Jacobian criterion, Theorem 2.1 and Corollary 2.2, together with local standard coordinates, Theorems 4.1 and 5.1, identifies the nonsmooth locus of a map between the smooth source and curve with the vanishing of its differential. No irreducible component of this critical locus can dominate the curve: if it did, the differential's vanishing in \(\Omega_Z^1\) restricted to its function field would imply \(dt=0\) in the differentials of that function field, contradicting the derivation just constructed. Its proper image is therefore a proper closed subset of the curve, hence finite. Apply the same argument to each smooth closed boundary intersection. Nondominating closed intersections also have finitely many images and are removed. This treats the closed intersections, which are proper, before their open strata.

Add fibres over \(T=\bar C\setminus C_0\) to the complement and principalize its reduced ideal on the already smooth \(Z\), preserving \(X_0=f^{-1}(C_0)\). This also preserves a smooth relative SNC pair over \(C_0\), for the following reason. In a relative SNC chart over \(C_0\), the boundary ideal is generated by \(z_1\cdots z_k\), and the chart is étale over a product of these normal affine coordinates, the remaining relative coordinates and a base neighbourhood. Principalization commutes with smooth morphisms, by principalization, Theorem 3.1(4). The sequence on this chart is consequently the pullback of the sequence for the ideal \((z_1\cdots z_k)\) on \(\mathbf A^k\), with the relative and base factors retained. Its resulting ambient scheme is smooth and its divisor SNC by that theorem; their products and étale pullbacks are smooth and SNC relative to the base. These local assertions apply on the charts of the global sequence. Thus the new \(Z\) is smooth proper; its reduced boundary \(D=Z\setminus X_0\) is SNC, contains \(g^{-1}T\), and is relative SNC over \(C_0\). Theorem 5.1 supplies a normalized logarithmic extension \(\bar E\) of \(E|_{X_0}\) on \(Z\). No semistable reduction is asserted: components of \(g^*T\) may have any positive multiplicity.

#### Relative logarithmic forms and explicit lifts

Set
\[
\mathcal A=\Omega_Z^1(\log D),\qquad
\mathcal B=g^*\Omega_{\bar C}^1(\log T),\qquad
\mathcal Q=\mathcal A/\mathcal B.
\tag{5.6a}
\]
The inclusion is a subbundle. Over \(C_0\) this is the relative SNC coordinate calculation. At a point over \(t_0\in T\), choose a base parameter \(t\) and SNC coordinates. The local equation is
\[
g^*t=u\prod_i z_i^{a_i},\qquad
u\text{ a unit},\quad a_i\geq0,\quad
\text{some }a_i>0.
\tag{5.6b}
\]
The exponents are the vertical divisor multiplicities. This algebraic factorization can be checked without a new factoriality theorem: the coordinate-factor proof of Theorem 5.0 gives the corresponding analytic monomial and unit; the faithfully flat analytic stalk comparison, Theorem 4.1 contracts divisibility to the algebraic stalk. The resulting algebraic quotient is a unit because its analytic image is a unit and faithful flatness contracts the unit ideal.

Pullback of \(dt/t\) is
\[
\alpha=\sum_i a_i\,d\log z_i+du/u.
\tag{5.6c}
\]
Choose a vertical index \(i\) through the point. The coefficient
\(b_i=a_i+z_i(\partial_i u)/u\) is a unit locally, since modulo \(z_i\) it equals the nonzero integer \(a_i\). Replacing \(d\log z_i\) by \(\alpha\) proves the subbundle assertion. The logarithmic base field \(\theta=t\partial_t\) has the lift
\[
v_i=b_i^{-1}z_i\partial_i,\qquad v_i(g^*t)=g^*t.
\tag{5.6d}
\]
This field is tangent to every boundary component. It contracts logarithmic forms to regular logarithmic forms. Arbitrary positive \(a_i\) cause no obstruction. Over \(C_0\), relative SNC coordinates similarly lift ordinary base fields.

Since \(d\alpha=0\), the exterior ideal of pulled-back base forms is differential-stable. Quotienting the absolute logarithmic connection gives
\[
K^\bullet=(\Lambda^\bullet\mathcal Q\otimes\bar E,\nabla_{\mathrm{rel}}).
\tag{5.6e}
\]
It is a finite complex of coherent locally free terms; its differential is \(g^{-1}\mathcal O_{\bar C}\)-linear, though not \(\mathcal O_Z\)-linear.

Each individual term has coherent ordinary proper higher images, by ordinary proper coherence, Theorem 4.1. These are also its underlying complex-sheaf higher images: forgetting \(\mathcal O_Z\)-modules preserves injectives because its left adjoint \(\mathcal O_Z\otimes_{\mathbf C}-\) is exact on stalks. The finite-degree spectral sequence of this complex is a spectral sequence of \(\mathcal O_{\bar C}\)-modules. Its pages are kernels and quotients of coherent modules and its abutment has a finite coherent filtration. Thus every \(A^a=\mathcal H^a(Rg_*K^\bullet)\) is coherent. This argument does not treat the relative differential as \(\mathcal O_Z\)-linear and does not invoke D-module proper regularity.

#### The corrected Čech Gauss–Manin connection

Over an affine base neighbourhood choose a finite affine adapted cover \(U_i\) of its inverse image, and logarithmic lifts \(v_i\) of a base logarithmic field \(\theta\). Finite intersections are affine by separatedness. Affine acyclicity, Theorems 2.2 and 3.2, and the finite Čech comparison and basis criterion, Theorems 3.2 and 4.1, make the ordered Čech total compute \(Rg_*K^\bullet\) over that neighbourhood.

On relative forms put
\[
L_i=\nabla\iota_{v_i}+\iota_{v_i}\nabla.
\tag{5.6f}
\]
It descends to the relative quotient: Lie derivative by a lift preserves the ideal of pulled-back base forms. It commutes with the relative differential by integrability and obeys
\[
L_i(g^*a\,s)=g^*(\theta a)s+g^*a\,L_i(s).
\tag{5.6g}
\]
All terms preserve the logarithmic bundle.

For differences of lifts define \(H_{ij}=\iota_{v_j-v_i}\). These are well-defined contractions on relative forms because their vector fields are vertical. Subtraction of (5.6f) and addition of differences give
\[
L_j-L_i=d_KH_{ij}+H_{ij}d_K,\qquad
H_{ij}+H_{jk}=H_{ik}.
\tag{5.6h}
\]

For a cochain \(c\) of Čech/form bidegree \((p,q)\), totalize by
\(D=\delta+(-1)^p d_K\). Define the degree-zero operator with diagonal component
\[
(\mathcal Lc)_{i_0\ldots i_p}
=L_{i_0}c_{i_0\ldots i_p}
\]
and extra component in bidegree \((p+1,q-1)\)
\[
(\mathcal Lc)_{i_0\ldots i_{p+1}}
=(-1)^pH_{i_0i_1}c_{i_1\ldots i_{p+1}}.
\tag{5.6i}
\]
Both components are added.

The diagonal Čech commutator is
\[
(\delta L-L\delta)c_{i_0\ldots i_{p+1}}
=(L_{i_1}-L_{i_0})c_{i_1\ldots i_{p+1}}.
\]
The extra component's internal commutator is its negative by (5.6h): the output internal sign is \((-1)^{p+1}\), the input one is \((-1)^p\), and its own factor is \((-1)^p\). Its Čech commutator vanishes by \(H_{i_0i_2}=H_{i_0i_1}+H_{i_1i_2}\); terms deleting later indices cancel in pairs. Each \(L_i\) commutes with \(d_K\). Consequently
\[
D\mathcal L=\mathcal LD.
\tag{5.6j}
\]

For new lifts \(v_i'\), let \(h_i=\iota_{v_i'-v_i}\). The degree-minus-one diagonal operator \(\mathcal H\) acts on bidegree \((p,q)\) by \((-1)^p h_{i_0}\). The exact identity is
\[
\mathcal L'-\mathcal L=D\mathcal H+\mathcal HD.
\tag{5.6k}
\]
Its diagonal internal part is \(d_Kh_i+h_id_K=L_i'-L_i\); its extra part is \((-1)^p(h_{i_1}-h_{i_0})\), the change in (5.6i). Thus the operator on cohomology is independent of lifts. The intrinsic construction below proves compatibility with arbitrary refinements and independence of the ordered covers.

There is also an intrinsic definition that proves cover compatibility. The absolute logarithmic complex has the short exact sequence of complex-vector-space complexes
\[
0\longrightarrow
g^*\Omega_{\bar C}^1(\log T)\otimes K^{\bullet-1}
\xrightarrow{\ \alpha\wedge\ }
(\Omega_Z^\bullet(\log D)\otimes\bar E,\nabla)
\longrightarrow K^\bullet\longrightarrow0.
\tag{5.6l}
\]
The first differential is \(-d_K\), since \(\nabla(\alpha\wedge s)=-\alpha\wedge\nabla s\). Base dimension one makes every exterior term with two base forms zero, so the kernel is exactly this first complex. Locally the chosen base logarithmic form trivializes its first factor. The connecting morphism on derived images defines
\(A^a\to\Omega_{\bar C}^1(\log T)\otimes A^a\).

To identify its cochain action, lift each relative form to its \(v_i\)-horizontal representative \(\sigma_i\), whose contraction with \(v_i\) is zero. The internal lift error is \(\alpha\wedge L_i\); on the first overlap, \(\sigma_{i_1}-\sigma_{i_0}=-\alpha\wedge H_{i_0i_1}\). In the total, the internal error has factor \((-1)^p\). The identification of the first complex's total with the shifted relative total multiplies Čech degree \(p\) by \((-1)^p\). Hence its connecting map is exactly the diagonal \(L_i\) plus extra component \((-1)^pH_{i_0i_1}\) in (5.6i). The short exact sequence is intrinsic and compatible with every restriction and refinement; thus its connecting map proves the asserted gluing independently of choices of ordered cover.

For a base function \(a\), differentiating the lifted cocycle for \(a\,s\) adds precisely \(da\wedge s\). The intrinsic connecting map therefore has the Leibniz rule \(\nabla(a s)=da\otimes s+a\nabla s\), agreeing with (5.6g). Multiplication of the base field by a base function multiplies the operator by that function. This gives a logarithmic connection. Since a curve has rank-one tangent sheaf, integrability follows directly:
\[
[a\nabla_\theta,b\nabla_\theta]
=(a\theta(b)-b\theta(a))\nabla_\theta.
\tag{5.6m}
\]
Expanding with (5.6g) proves the identity; the scalar second-order terms cancel.

#### A stable coherent lattice at every boundary point

At a boundary point the torsion of \(A^a\) is stable. If \(t^Ns=0\), then
\[
t^N\mathcal L_\theta(s)
=\mathcal L_\theta(t^Ns)-\theta(t^N)s
=-Nt^Ns=0.
\]
At an ordinary point differentiation loses at most one power of its parameter, so increasing the annihilating exponent by one proves stability there too. Hence the torsion-free quotient
\[
\bar H^a=A^a/\operatorname{torsion}
\tag{5.6n}
\]
is stable. Here is the algebraic local freeness argument. At a closed point of the smooth curve, its regular local ring \(R\) has maximal ideal \((t)\). The faithful-flat analytic injection into \(\mathbf C\{t\}\) makes \(\bigcap_n t^nR=0\). Thus every nonzero \(a\in R\) has a largest divisibility exponent \(m\), and \(a=t^m u\) with \(u\notin(t)\), hence \(u\) a unit. Choosing least valuation in an ideal makes every ideal principal. A finite torsion-free \(R\)-module embeds in its generic vector space: the kernel of localization is its torsion. Choose a generic basis and clear the finitely many denominators of module generators to embed it into a finite free \(R\)-module. The coordinate-projection induction of Lemma 1.0, now using the principal ideals just proved, makes that submodule finite free. Freeness at the generic point is already a vector-space assertion. Thus \(\bar H^a\) is a finite-rank bundle with logarithmic connection, equal to \(A^a\) on a smaller dense open.

Over \(C_0\), the horizontal boundary coordinates are relative coordinates. Lemma 5.5.1's finite pole proof applies to the relative complex: the normal operator \(\operatorname{Res}_i-nI\) is invertible and parallel for the remaining relative differential; its inverse times contraction makes the quotient acyclic. Other-coordinate poles remain allowed. Exact filtered localization gives
\[
K^\bullet|_{g^{-1}C_0}
\simeq Rj_{0*}(\Omega_{X_0/C_0}^\bullet\otimes E),
\tag{5.6o}
\]
where \(j_0:X_0\hookrightarrow g^{-1}C_0\) is affine by the proved Cartier-complement argument, and its quasi-coherent form terms are image-acyclic. The actual inclusions commute with logarithmic Lie derivatives and vertical contractions. They therefore identify the connections from the two corrected Čech totals.

Properness of \(g\), (5.6o) and derived-image composition identify \(A^a|_{C_0}\) with the relative de Rham image of \(f\), including its actual connection action. The lattice (5.6n) supplies its logarithmic extension at every point of \(\bar C\). The proved one-variable lattice criterion therefore makes the generic Gauss–Manin connection regular.

This proves the curve-base input with all fibre multiplicities and all coefficient Jordan blocks, for arbitrary smooth \(f\) without a properness assumption. We now prove the general-base reduction; arbitrary singular regular-holonomic images and full analytic proper regularity remain separate.

#### The theorem on every smooth algebraic base

**Theorem 5.6 (generic Gauss–Manin regularity).** Let \(f:X\to B\) be any smooth morphism of smooth separated finite-type complex varieties, and let \(E\) be any finite-rank integrable connection regular on every algebraic curve, including infinity. On every connected component of \(B\), there is a dense open \(U\) on which all relative de Rham images
\[
H^a=\mathcal H^a\bigl(Rf_*(\Omega_{X/B}^\bullet\otimes E)\bigr)|_U
\tag{5.6p}
\]
are finite-rank regular integrable connections. Their connection is the actual Gauss–Manin connection, and formation of these connections commutes with pullback by every map from a smooth curve to \(U\). The statement allows nonproper and non-quasi-projective \(X\) and \(B\). Empty source components give zero images; work componentwise otherwise.

Take a smooth proper SNC compactification \(\bar B\) of \(B\) and an absolute proper compactification of \(X\). Close the graph of \(f\) in their product, take its reduced closure, resolve while preserving \(X\), and principalize its boundary. This gives a smooth proper \(Z\), a proper \(g:Z\to\bar B\), and an SNC divisor \(D=Z\setminus X\). Theorem 5.1 extends \(E\) to a normalized logarithmic bundle \(\bar E\) on this absolute proper pair.

There is a dense \(U\subset B\) over which \(g\) and every nonempty closed boundary intersection are smooth. Here is the higher-dimensional version of the earlier bad-image argument. For a closed intersection dominating an integral component of \(B\), choose a transcendence basis \(t_1,\ldots,t_b\) of its base function field and extend it to a transcendence basis of the intersection's function field. Each derivation \(\partial/\partial t_j\) extends over the remaining finite separable field extension by the minimal-polynomial argument above. Therefore the pulled-back differentials \(dt_1,\ldots,dt_b\) are linearly independent there. An irreducible component of the critical locus cannot dominate \(B\): its ambient differential rank would be less than \(b\), and restriction to its function field could not increase that rank, contradicting this independence. The Jacobian minors cut out a closed critical locus. Its image is closed by properness and is a proper subset. Remove these images for \(Z\) and for the finitely many closed intersections, and remove the proper images of the nondominating intersections. Their finite union is a proper closed subset of each base component.

This makes \(D|_{Z_U}\) relative SNC. At a point of a \(k\)-fold boundary intersection the differential of \(g\) on that intersection is surjective. The base coordinate differentials together with \(dz_1,\ldots,dz_k\) are consequently independent in the ambient cotangent space. Complete them to a basis with remaining relative coordinates. The Jacobian criterion gives an étale relative coordinate chart with those normal coordinates. In particular \(g:Z_U\to U\) is smooth and
\[
\Omega^1_{Z_U}(\log D)/g^*\Omega_U^1
\]
is locally free. Let \(K_U\) be its exterior complex with coefficients \(\bar E|_{Z_U}\). The same ordinary proper-coherence spectral sequence used for (5.6e) proves that every
\(A^a=\mathcal H^a(Rg_*K_U)\) is coherent over \(\mathcal O_U\).

#### Integrability and arbitrary curve base change

Filter the absolute logarithmic complex on \(Z_U\) by the number of pulled-back base one-forms. Integrability of \(\bar E\) makes this a finite differential-stable filtration, with quotients
\[
\operatorname{gr}_F^p
(\Omega_{Z_U}^\bullet(\log D)\otimes\bar E)
\simeq
g^*\Omega_U^p\otimes K_U^{\bullet-p}.
\tag{5.6q}
\]
The internal differential under the wedge identification is \((-1)^p d_{K_U}\). Choose an affine base chart and a finite affine cover of its inverse image; the termwise affine Čech total computes every quotient. The base form modules are finite locally free, so tensoring this total with them commutes with cohomology. Its first filtered page is
\[
E_1^{p,q}=\Omega_U^p\otimes A^q,\qquad
d_1^{0,q}:A^q\longrightarrow\Omega_U^1\otimes A^q.
\tag{5.6r}
\]
The last map defines \(\nabla_{\rm GM}\).

This is a connection, with the same cochain operators as (5.6i). Modulo two base factors, contraction with a lift of any base field gives the horizontal representative and the overlap correction already computed. Moreover \(d(a s)=da\wedge s+a\,ds\), so the connecting map obeys
\[
\nabla_{\rm GM}(a s)=da\otimes s+a\nabla_{\rm GM}s.
\tag{5.6s}
\]
For a base \(p\)-form \(\beta\), the same calculation identifies the first-page differential as
\[
d_1(\beta\otimes s)
=d\beta\otimes s+(-1)^p\beta\wedge\nabla_{\rm GM}s.
\tag{5.6t}
\]
Its square is zero. To see this directly, lift a cocycle of the quotient of filtration degree \(p\) to a cochain whose differential lies in \(F^{p+1}\). That differential represents its \(d_1\) image and is closed, since the absolute differential squares to zero. Its next first-page differential is therefore zero. Changing the lift changes the representative only by a quotient boundary. Applying this to \(p=0\) and using (5.6t) gives zero curvature. Thus \(\nabla_{\rm GM}\) is integrable. The coherent-connection theorem, Theorem 3.1, makes every \(A^a\) locally free of finite rank.

Here is the required base change, without using a proper base-change theorem for D-modules. On an affine \(V=\operatorname{Spec}A\subset U\), choose the finite affine cover of \(Z_V\) just used. Every term of its Čech total for \(K_U\) is flat over \(A\). Indeed \(g\) is smooth and hence flat by smooth flatness, Theorems 5.1 and 6.1, and a locally free sheaf on each affine intersection gives a projective module over its flat coordinate algebra. The total is bounded in both directions. Its cohomology modules are finite projective over \(A\), by the local freeness just proved.

For completeness, a bounded complex of flat modules with flat cohomology commutes with arbitrary scalar extension. Starting in the highest degree, the exact sequence with quotient the top cohomology shows that its boundary module is flat. Descend: the exact sequence
\(0\to Z^n\to C^n\to B^{n+1}\to0\)
makes \(Z^n\) flat; then
\(0\to B^n\to Z^n\to H^n\to0\)
makes \(B^n\) flat. The kernels are flat because the long exact Tor sequence has flat middle and quotient terms. All these sequences remain exact after tensoring, since their quotient modules are flat. Thus kernels, images and cohomology of the tensor complex are the tensor products of the corresponding modules.

Now let \(h:C\to U\) be any map from a smooth algebraic curve. Take an affine \(V=\operatorname{Spec}A\subset U\) and an arbitrary affine open \(W\subset h^{-1}(V)\), with coordinate ring \(A'\). The open \(h^{-1}(V)\) itself need not be affine; a constant map from a proper curve already shows this. Over \(W\), the pulled-back Čech intersections are affine and their vector-bundle sections are the scalar extensions along \(A\to A'\) of the original sections, by the affine sheaf/module equivalence, Theorem 1.2 and Proposition 1.3. Relative logarithmic differentials commute with this base change in the relative SNC coordinates above. Hence the pulled-back total is precisely the total for the pulled-back proper pair and bundle. The preceding flat-complex argument proves, locally and then by gluing,
\[
h^*A^a
\simeq
\mathcal H^a(Rg_{C*}K_C).
\tag{5.6u}
\]
This also respects connections, by the following actual cochain calculation. Shrink \(V\) to have étale coordinates \(y_1,\ldots,y_b\), choose lifts \(v_{ij}\) of \(\partial/\partial y_j\) on its adapted affine cover, and write \(\mathcal L_j\) for the corrected operator (5.6i) and \(H_{ik,j}=\iota_{v_{kj}-v_{ij}}\). For a vector field \(w\) on \(W\), put \(a_j=w(h^*y_j)\). Its lift to a pulled-back affine chart is the derivation
\[
v_i^C(r\otimes b)
=\sum_j a_j(v_{ij}r\otimes b)+r\otimes w(b).
\]
This respects the tensor relations: on a base function \(a\), the chain rule in the étale coordinates says \(\sum_j a_j h^*(\partial_j a)=w(h^*a)\). Differences of these lifts are vertical, with contraction \(H^C_{ik}=\sum_j a_j H_{ik,j}\). The pulled-back relative differential kills every \(a_j\), so the corrected target operator on the Čech total is
\[
\mathcal L_w^C(b\otimes c)
=w(b)\otimes c+b\sum_j a_j(1\otimes\mathcal L_jc).
\tag{5.6v}
\]
Its off-diagonal component is precisely (5.6i) with \(H^C_{ik}\). Thus the natural scalar-extension map intertwines it with the usual pullback connection, proving connection compatibility in (5.6u). Equivalently, pullback of absolute forms as complex-vector-space sheaves respects the base-form filtration and the connecting morphisms; no scalar tensor of the non-\(\mathcal O_U\)-linear absolute differential is being taken. No flatness of \(h\), immersion hypothesis or dominance assumption is required.

Finally, the finite-pole proof of Lemma 5.5.1 applies relative to \(U\), exactly as in (5.6o). It identifies \(A^a\) with the images (5.6p), with their actual connection. It applies after the curve base change too. The morphism
\(X_C=X\times_B C\to C\)
is smooth, and the pulled-back connection is curve-regular, since any curve mapping to \(X_C\) composes to a curve mapping to \(X\). The curve theorem above makes the generic Gauss–Manin connection on \(C\) regular, with logarithmic lattices at every completion point. By (5.6u) it is the restriction of \(h^*A^a\), which is already a nonsingular finite-rank connection everywhere on \(C\). At an omitted point lying inside \(C\), its own bundle gives a stable logarithmic lattice; at points outside \(C\), retain the lattices from the curve theorem. The one-variable criterion therefore proves regularity of the whole connection \(h^*A^a\), including infinity. As \(h\) was arbitrary, \(A^a\) is curve-regular on \(U\).

This proves the full generic Gauss–Manin theorem for arbitrary smooth bases and all regular coefficient connections. Theorem 5.17 supplies arbitrary singular algebraic regular-holonomic map stability. Full analytic proper regularity remains required.

#### The relative Spencer transfer and its shift

For clarity, the same Gauss–Manin action is the operator action in the smooth direct image with arbitrary coefficients. The relative Spencer complex has terms \(\mathcal D_X\otimes_{\mathcal O_X}\Lambda^qT_{X/B}\) in degree \(-q\), with the multiplication and bracket differential of the relative Spencer calculation, Theorem 2.1. It augments to the forward transfer \(\mathcal O_X\otimes_{f^{-1}\mathcal O_B}f^{-1}\mathcal D_B\) by \(P\mapsto P(1\otimes1)\). In commuting adapted étale coordinates, PBW identifies the augmentation quotient with this transfer and the shifted order-graded complex with the Koszul complex on the \(r\) vertical symbols. Those polynomial variables are a regular sequence, so that Koszul complex is exact. Lifting a graded preimage and descending its finite order proves exactness of the augmented Spencer complex. Its terms are locally free over \(\mathcal D_X\), and the bracket formula is intrinsic, so the resolutions glue. This proves the same resolution for every smooth \(f\), without assuming it is a global product.

If \(f\) has relative dimension \(r\), tensoring this resolution with the right side-changed \(E\) gives
\[
f_+E\simeq Rf_*(\Omega_{X/B}^\bullet\otimes E)[r].
\tag{5.6w}
\]
In adapted commuting étale coordinates, its vertical scalar derivatives become the vertical covariant derivatives of \(E\), so its differential is \(\nabla_{\rm rel}\). The right action of a lifted horizontal field on \(\omega_X\otimes E\) is minus the covariant derivative, including the volume Lie derivative; changing sides on the base removes this minus sign. In the coordinate frame, its left action is therefore \(\nabla_{\partial_{y_j}}\). On form factors the bracket terms give ordinary Lie derivative, so intrinsically the action is \(L_v=\nabla\iota_v+\iota_v\nabla\).

This last identity can be checked on a coefficient section, where contraction of its connection gives \(\nabla_v s\), and on a one-form, where it is the ordinary Cartan identity; the product rule extends it to every wedge. Changing a lift by a vertical field \(w\) changes the operator by \(\nabla_{\rm rel}\iota_w+\iota_w\nabla_{\rm rel}\). Thus the transfer action glues by exactly the correction (5.6i), and agrees with the intrinsic connecting map, also for nontrivial \(E\). The shift \([r]\) changes the cohomological index and not this degree-zero action: the bundle \(H^a\) is \(H^{a-r}(f_+E)|_U\).


### Duality of every regular holonomic object

**Theorem 5.7 (regular holonomic duality).** Let \(X\) be a smooth separated finite-type complex algebraic variety. With the left-module duality
\[
\mathbb D_XK=
\operatorname{SC}_X
 R\mathcal Hom_{\mathcal D_X}(K,\mathcal D_X)[d_X],
\qquad
\operatorname{SC}_X(Q)=Q\otimes_{\mathcal O_X}\omega_X^{-1},
\tag{5.7a}
\]
duality is an exact contravariant equivalence of the category of regular holonomic modules, as defined by regular connection presentations of their simple factors. It induces a contravariant equivalence of the full subcategory \(D^b_{\mathrm{rh}}(\mathcal D_X)\) of bounded complexes with regular holonomic cohomology. In particular
\[
H^q(\mathbb D_XK)\simeq
\mathbb D_X H^{-q}(K).
\tag{5.7b}
\]
There is no restriction on the dimension or singularities of the closed supports. There is no properness or quasi-projectivity assumption on \(X\). On different open-and-closed components use their respective dimensions in (5.7a).

Here \(f_*\) denotes the differential-operator direct image, also often written \(f_+\). Thus the canonical map considered below is exactly \(j_!\to j_+\) in the plus notation. It is not an ordinary underived sheaf map.

The following earlier **proved** results suffice:

1. Holonomic duality, Lemma 3.0 and (3.4): finite local operator resolutions, intrinsic derived bidual evaluation. Theorem 3.1 and Corollary 3.2: Ext concentration, exact holonomic duality, preservation of simple objects and finite length. Proposition 5.1: its dual of a flat bundle is its usual dual connection, proved with the density-correct Spencer resolution.
2. Direct images, Propositions 3.1–3.2: exact closed direct image with its normal derivative basis, and derived open direct image. The special closed-then-open composition follows directly from these transfer descriptions, as explained in the canonical-map argument above below.
3. Kashiwara equivalence, Theorem 3.1 and (3.2)–(3.5): exact supported equivalence, intrinsic determinant-twisted inverse, and its actual unit and evaluation maps.
4. Adjunctions, Lemma 1.2, closed duality (4.3), and the open adjunction, Theorem 5.1: closed duality and the two embedding adjunctions with their units and counits.
5. Minimal extensions, Theorem 4.1: the degree-zero image is the unique supported extension with no boundary subobject or quotient. Its full proof, rather than its subsequent one-line duality assertion (4.4), is the input.
6. Lemma 1.0 and Theorem 1.1 above: the formal and convergent lattice algebra and the logarithmic lattice criterion. The regular connection definition tests every smooth algebraic curve map and every point of its complete curve, including infinity.

We prove all the additional steps here. In particular we do not invoke the regular-holonomic stability statement, a curve criterion for singular holonomic objects, or Riemann–Hilbert.

The freely accessible [Bernstein lecture notes, lecture 4, §§2–3 and the beginning of §5](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), printed pages 31–33, give the regular composition-factor definition and list duality among the stability operations. They are a reading reference; the proof below supplies this operation.

#### Dual logarithmic lattices, including infinity

Let \(R\) be \(\mathbf C[[t]]\) or \(\mathbf C\{t\}\), \(K=\operatorname{Frac}R\), and \(\theta=t\,d/dt\). Suppose \((V,\Theta)\) is a finite-dimensional differential \(K\)-module:
\[
\Theta(fv)=\theta(f)v+f\Theta(v).
\]
Define \(V^\vee=\operatorname{Hom}_K(V,K)\) with
\[
(\Theta^\vee\phi)(v)
=\theta(\phi(v))-\phi(\Theta v).
\tag{5.7c}
\]
The right side is \(K\)-linear in \(v\): applying it to \(fv\) cancels the two terms \(\theta(f)\phi(v)\). It satisfies the differential Leibniz identity in \(\phi\). This proves that (5.7c) is the dual differential module and is precisely the pairing formula of the earlier dual-connection Proposition 5.1.

If \(L\subset V\) is a full stable lattice, its dual lattice is
\[
L^\vee=\{\phi\in V^\vee:\phi(L)\subset R\}
       =\operatorname{Hom}_R(L,R).
\tag{5.7d}
\]
An \(R\)-basis of \(L\) and its dual \(K\)-basis identify (5.7d) with \(R^{\operatorname{rank}V}\). Consequently it is finite free, spans \(V^\vee\), and has the full rank, including the zero-rank case. For \(\phi\in L^\vee\) and \(v\in L\), both terms in (5.7c) lie in \(R\), because \(\theta(R)\subset R\) and \(\Theta L\subset L\). Hence
\[
\Theta^\vee L^\vee\subset L^\vee.
\]
In the dual basis the matrix and residue are
\[
\Theta=\theta+A(t),\qquad
\Theta^\vee=\theta-A(t)^{\mathsf T},\qquad
\operatorname{Res}(L^\vee)=-\operatorname{Res}(L)^{\mathsf T}.
\tag{5.7e}
\]
This is the actual dual lattice, without a semisimplicity assumption. Dualizing twice recovers \(L\), its evaluation pairing, and \(\Theta\). The lattice criterion therefore proves
\[
V\text{ is regular singular}\quad\Longleftrightarrow\quad
V^\vee\text{ is regular singular}
\tag{5.7f}
\]
over each of the two rings separately.

The higher-dimensional logarithmic formula is the same. If \(F\) is a bundle with logarithmic connection on a smooth SNC pair \((P,D)\), define
\[
\langle\nabla^\vee\phi,v\rangle
=d\langle\phi,v\rangle-\langle\phi,\nabla v\rangle.
\tag{5.7g}
\]
The logarithmic forms constitute an \(\mathcal O_P\)-module containing the differentials of regular functions, so (5.7g) has coefficients in
\(\Omega_P^1(\log D)\otimes F^\vee\). In a frame \(\nabla=d+\Gamma\), the dual is \(d-\Gamma^{\mathsf T}\). Evaluating the curvature on two vector fields and a section shows that it is minus the original curvature under the pairing, so the dual is integrable. Every boundary component has the residue in (5.7e). Commuting residues remain commuting after negative transposition. All Jordan blocks and all crossings are retained. A normalized residue strip is not in general retained by taking this lattice dual; regularity requires existence of a logarithmic lattice and imposes no such normalization.

For any algebraic map \(h:C\to U\), the natural bundle isomorphism
\[
h^*(E^\vee)\simeq(h^*E)^\vee
\tag{5.7h}
\]
respects the connections: apply the pairing formula to local sections and the chain rule for \(h\). On every irreducible component of \(C\), and at every point of its complete smooth model, pass from rational frames to the formal or convergent meromorphic field. Formula (5.7h) remains the same dual pairing there. Equations (5.7d)–(5.7f) apply at that point, whether it lies in \(C\) or outside \(C\). Thus an all-curve regular algebraic connection has an all-curve regular dual, and conversely.

This argument includes constant curve maps, arbitrary finite rank and nonsemisimple monodromy. It does not replace the test at infinity by a test on the nonsingular interior.

#### Support and coherent biduality

The duality in (5.7a) commutes with restriction to any Zariski open \(W\subset X\). Indeed, restriction of a finite local operator resolution computes both internal derived Hom complexes, the operator ring restricts to \(\mathcal D_W\), and the canonical density line restricts to \(\omega_W\). These termwise identifications respect the differentials and evaluation maps.

In particular for a holonomic module
\[
\operatorname{Supp}\mathbb D_X M=\operatorname{Supp}M.
\tag{5.7i}
\]
If \(M\) vanishes on \(W\), its dual vanishes there. Applying this implication to the dual and using biduality gives the converse. Taking the complements of all such opens gives (5.7i). The same argument detects vanishing of a bounded holonomic complex on an open.

For clarity, the biduality used here is a coherent involution, not merely an unspecified objectwise isomorphism. For an unshifted bounded finite projective complex \(P\), the evaluation on a homogeneous element \(x\in P^p\) is
\[
e_P(x)(f)=(-1)^p f(x)\quad(f\in(P^\vee)^{-p}).
\]
With \(d_{P^\vee}f=(-1)^{|f|+1}f\,d_P\), this is a cochain map. Applying it twice multiplies the two signs \((-1)^p\) and \((-1)^{-p}\), so
\[
\mathbb D(e_K)\circ e_{\mathbb D K}=\mathrm{id}_{\mathbb D K}.
\tag{5.7j}
\]
The side-changing equivalence and the dimension shifts transport this evaluation; the two shifts cancel when Hom reverses the shift. This is the intrinsic evaluation of the earlier biduality (3.4). The shifted evaluation can be made explicit in a volume trivialization, using the dualizing target \(\mathcal D_X[d_X]\). An element of degree \(p\) pairs with a dual element of degree \(-d_X-p\), so the evaluation sign is \((-1)^{p(p+d_X)}\). On the second evaluation, put \(q=-d_X-p\); then \(q(q+d_X)=p(p+d_X)\), and the two signs cancel. The local finite projective computations prove (5.7j), naturality, and their gluing. Thus dualizing an adjunction really exchanges its unit and counit, with their triangular identities. There is no freely chosen scalar or sign in that exchange.

Closed duality has the same normalization. In the earlier closed-embedding proof, the map is formed by applying direct image to evaluation and then the Kashiwara counit trace. On a finite free source term, tensor–Hom adjunction makes it the identity on the transfer term, with \(d_X-c=d_U\). These are precisely the unit and evaluation in the supported equivalence; applying evaluation twice uses (5.7j). The local comparison is therefore compatible with biduality and with those units and counits. Resolving by finite projectives extends these compatibilities to all coherent bounded objects, and their intrinsic formulas glue. We may consequently use, with that normalization,
\[
\mathbb D_V i_*A\simeq i_*\mathbb D_UA
\tag{5.7k}
\]
for a smooth closed embedding \(i:U\hookrightarrow V\). This is the already proved closed case of the adjunction lesson (4.3), with its map retained.

Explicitly, if \(\alpha_A:\mathbb D_Vi_*A\to i_*\mathbb D_UA\) is this comparison, its bidual compatibility is the equality of maps from \(i_*A\) to \(\mathbb D_V^2i_*A\)
\[
\mathbb D_V(\alpha_A)\,
\alpha_{\mathbb D_UA}^{-1}\,i_*(e_A)=e_{i_*A}.
\]
In the finite free transfer calculation, tensor–Hom adjunction turns the two composites into the same signed evaluation: the normal Koszul evaluation is the unit followed by its counit, whose composite is the identity. The remaining complex evaluation is the one in (5.7j). This verifies the equality locally, with the determinant and dimension shift included. Its naturality extends it to the finite resolutions and their cones. This is the compatibility required below when the closed and open transpositions are combined.

The inverse to \(i_*\) in the supported heart is the actual \(H^0i^!\), including \(\det(\mathcal I/\mathcal I^2)\); replacing it by an untwisted normal kernel would change this compatibility. No extra codimension shift is appended.

#### The canonical extension map and its transpose

We first prove the assertion for an open embedding \(u:V\hookrightarrow X\), allowing an arbitrary bounded holonomic input \(A\) on \(V\). Put
\[
\rho=u^!,\qquad R=u_*,\qquad L=u_!
=\mathbb D_XR\mathbb D_V.
\]
Restriction is \(\rho=u^*\) as well. Let
\(\eta:\mathrm{id}\to R\rho\) and \(c:\rho R\to\mathrm{id}\) be the unit and counit of \(\rho\dashv R\). The latter is an isomorphism for an open embedding. Dualize this adjunction using (5.7j). It gives \(L\dashv\rho\), with unit \(b:\mathrm{id}\to\rho L\) and counit \(\varepsilon:L\rho\to\mathrm{id}\), where
\[
b_A=\mathbb D_V(c_{\mathbb D_VA}),\qquad
\varepsilon_M=\mathbb D_X(\eta_{\mathbb D_XM})
\tag{5.7l}
\]
under the natural restriction and bidual identifications. In particular \(b_A\) is an isomorphism. This is exactly the open-embedding adjunction in the earlier lesson, constructed by dualizing restriction–direct-image adjunction.

The canonical arrow is
\[
\operatorname{can}_{u,A}
=R(b_A^{-1})\,\eta_{LA}
=\varepsilon_{RA}\,L(c_A^{-1}): LA\longrightarrow RA.
\tag{5.7m}
\]
Both displayed composites have mate \(c_A^{-1}:A\to\rho RA\) under \(L\dashv\rho\). For the second this is the defining adjunction formula. For the first, naturality of \(\eta\) and the triangular identity for \(\rho\dashv R\) give
\(c_A\,\rho(\operatorname{can}_{u,A})\,b_A=\mathrm{id}_A\).
The adjunction bijection is injective, so the composites agree. This verifies that (5.7m) is the arrow corresponding to \(\mathrm{id}_A\) under \(\rho RA\simeq A\); it is not merely some extension map.

Dualizing the first composite and using (5.7l) yields
\[
\begin{aligned}
\mathbb D_X(\operatorname{can}_{u,A})
&=\mathbb D_X(\eta_{LA})\,
  \mathbb D_X\!\bigl(R(b_A^{-1})\bigr)\\
&=\varepsilon_{R\mathbb D_VA}\,
  L(c_{\mathbb D_VA}^{-1})
=\operatorname{can}_{u,\mathbb D_VA}.
\end{aligned}
\tag{5.7n}
\]
Here \(\mathbb D_XRA=L\mathbb D_VA\) and
\(\mathbb D_XLA=R\mathbb D_VA\). Also
\(\mathbb D_V(b_A^{-1})=c_{\mathbb D_VA}^{-1}\) by (5.7l) and (5.7j). Equation (5.7n) proves the transpose with the actual adjunction units and counits, including its sign.

Now let \(j:U\hookrightarrow X\) be any smooth locally closed embedding. Choose an open \(V\subset X\) with \(U\) closed in \(V\), and factor \(j=u i\). Write \(Z=\overline U\); then \(Z\cap V=U\). The transfer for the open embedding is the identity bimodule. Therefore the backward transfer of \(j\), on \(U\), is the backward transfer of \(i\) with the ambient operators restricted from \(X\) to \(V\). Closed sheaf direct image and its transfer tensor are exact, while open sheaf direct image is derived. Their tensor and sheaf compositions give
\[
j_*=u_*i_*,\qquad
j_!=u_!i_*
\tag{5.7o}
\]
using (5.7k) in the second identity. This particular composition needs no quasi-projective factorization theorem. All density factors are those in (5.7a) and in the closed transfer, and cancel by the side-changing equivalence.

For modules supported on \(Z\), restriction to \(V\) followed by \(H^0i^!\) is the exact restriction functor to \(U\); for bounded supported complexes it is the corresponding derived supported equivalence. Its compatibility with duality follows from open restriction, (5.7k), and the inverse equivalence. In particular the restriction of the transpose of an identity is the identity on the dual connection.

Under (5.7o), the canonical map for \(j\) is
\(\operatorname{can}_{u,i_*N}\). Indeed its restriction to \(V\) is the identity on \(i_*N\), and application of \(i^!\) gives the identity on \(N\). The adjunction bijection
\[
\operatorname{Hom}_X(j_!N,j_*N)
\simeq\operatorname{Hom}_U(N,j^!j_*N)
\simeq\operatorname{End}_U(N)
\]
uniquely characterizes that map. Using (5.7k), naturality of (5.7m), and (5.7n) now proves
\[
\mathbb D_X(\operatorname{can}_{j,N})
=\operatorname{can}_{j,\mathbb D_UN}
\tag{5.7p}
\]
under the normalized natural identifications
\(\mathbb D_Xj_*N\simeq j_!\mathbb D_UN\) and
\(\mathbb D_Xj_!N\simeq j_*\mathbb D_UN\).
The factorization was used to prove equality of these actual canonical maps, so no choice of \(V\) remains in (5.7p).

#### Minimal extensions and the boundary

For a holonomic module \(N\) on \(U\), \(j_*N\) has cohomology in degrees \(\geq0\), by its closed-exact/open-right-derived construction. Holonomic exact duality gives \(j_!N\) cohomology in degrees \(\leq0\). The minimal extension is
\[
j_{!*}N=
\operatorname{im}\bigl(H^0\operatorname{can}_{j,N}\bigr).
\tag{5.7q}
\]

Both embedding images vanish on \(X\setminus Z\): the direct image there comes from the empty intersection with \(U\), and the exceptional image has the same vanishing by its dual definition and the support and biduality argument above. Thus all the supported restriction arguments above apply to their bounded cohomology objects.

On the holonomic heart an exact anti-equivalence takes the image of a map to the image of its reversed dual map. To check this explicitly, factor \(f:A\to B\) as a surjection \(A\to I\) followed by an injection \(I\to B\). Exact duality makes
\(\mathbb D B\to\mathbb D I\) surjective and
\(\mathbb D I\to\mathbb D A\) injective. Their composite is \(\mathbb D f\), so its image is \(\mathbb D I\).
Duality exchanges cohomological bounds and induces
\(H^0(\mathbb D K)=\mathbb D H^0(K)\) on bounded holonomic complexes; the complete truncation proof is supplied in the bounded-complex argument below. Apply this and (5.7p) to (5.7q):
\[
\mathbb D_X(j_{!*}N)\simeq
j_{!*}(\mathbb D_UN).
\tag{5.7r}
\]
This proves the image identity from the actual transpose, rather than assuming the assertion following the earlier minimal-extension Theorem 4.1.

There is also a direct support check. The object \(j_{!*}N\) is supported on \(Z\), hence its dual has the same support by (5.7i). Its supported restriction is \(\mathbb D_UN\) by (5.7k). If a nonzero subobject \(B\) of this dual were supported on \(Z\setminus U\), exact duality would give a nonzero boundary quotient \(\mathbb D_XB\) of \(j_{!*}N\), contradicting the earlier no-boundary theorem. If it had a nonzero boundary quotient, duality would give a nonzero boundary subobject of \(j_{!*}N\). Thus the dual has both no-boundary properties. The uniqueness clause of that theorem recovers exactly (5.7r). The support argument retains boundary delta modules and all normal derivatives; it uses neither a structure-sheaf fibre nor restriction detection for general derived morphisms.

If \(N=E\) is a finite-rank connection, the earlier dual-connection Proposition 5.1 identifies \(\mathbb D_UE=E^\vee\). Therefore
\[
\mathbb D_X(j_{!*}E)\simeq j_{!*}(E^\vee).
\tag{5.7s}
\]
If \(E\) is irreducible, \(E^\vee\) is irreducible because holonomic duality preserves simple modules. If it is curve regular, the dual-lattice argument above proves curve regularity of \(E^\vee\) at all compactification points. The same embedding \(j\), including its affine-inclusion property when required by the regular-holonomic definition, presents the dual simple factor. No change or shrinking of that regular connection presentation is needed.

#### Every regular simple factor and every support

Let \(M\) be regular holonomic. Choose a finite composition series
\[
0=M_0\subset M_1\subset\cdots\subset M_\ell=M,
\qquad S_a=M_a/M_{a-1}.
\]
Each \(S_a\) has a presentation \(j_{a,!*}E_a\) required by the definition: \(E_a\) is an irreducible all-curve regular connection on a smooth locally closed subvariety, and \(j_a\) is affine. Equation (5.7s) and the dual-lattice argument above prove that \(\mathbb D_XS_a\) has the same sort of presentation with \(E_a^\vee\). Each is simple.

Set
\(F_a=\mathbb D_X(M/M_a)\subset\mathbb D_XM\).
Exactness gives a reversed composition series
\[
0=F_\ell\subset F_{\ell-1}\subset\cdots\subset
F_0=\mathbb D_XM,\qquad
F_{a-1}/F_a\simeq\mathbb D_XS_a.
\tag{5.7t}
\]
Every factor is regular, so \(\mathbb D_XM\) is regular holonomic. Applying this implication to \(\mathbb D_XM\) and using biduality proves the equivalence in both directions and the asserted exact anti-equivalence.

For use with complexes, the regular modules form a Serre subcategory directly from the composition-factor definition. Intersect a composition series of \(M\) with a submodule \(A\); each successive quotient injects into the corresponding simple factor, so it is zero or that simple factor. The quotient filtration has the complementary zero or simple quotients. This proves regularity of submodules and quotients without assuming a curve criterion for singular modules. Conversely concatenate a composition series of a submodule with the inverse images of one in its quotient to obtain a composition series of the extension. Thus extensions are regular as well.

All the arguments are on the ambient holonomic heart, allowing different supports in the same extension. They apply to point supports, nonclosed smooth strata and singular closures. Finite type gives finitely many open-and-closed smooth components, and the construction acts componentwise if their dimensions differ.

#### Bounded complexes and degree reversal

The earlier holonomic dual is a contravariant triangulated equivalence on the ambient \(D_h^b(\mathcal D_X)\), with
\(\mathbb D(A[s])=(\mathbb D A)[-s]\). No identification of this category with the abstract derived category of its heart is needed.

A bounded object is obtained by finitely many standard truncation triangles from \(H^a(K)[-a]\). The dual of this piece is
\((\mathbb D H^a(K))[a]\), whose only cohomology is in degree \(-a\). Finite induction on these triangles proves
\[
\mathbb D(D_h^{[a,b]})\subset D_h^{[-b,-a]}.
\tag{5.7u}
\]
In particular duality exchanges the upper and lower standard cohomological bounds for bounded objects.

Fix \(q\) and put \(a=-q\). The triangle
\(\tau_{\leq a-1}K\to K\to\tau_{\geq a}K\)
dualizes to
\[
\mathbb D\tau_{\geq a}K\longrightarrow
\mathbb DK\longrightarrow
\mathbb D\tau_{\leq a-1}K\longrightarrow.
\]
The last term has cohomology only in degrees \(\geq -a+1\), by (5.7u). Its long cohomology sequence identifies
\(H^{-a}(\mathbb DK)\) with
\(H^{-a}(\mathbb D\tau_{\geq a}K)\).
Next dualize the triangle
\(H^a(K)[-a]\to\tau_{\geq a}K\to\tau_{\geq a+1}K\).
Its first dual term, \(\mathbb D\tau_{\geq a+1}K\), has cohomology only in degrees \(\leq-a-1\). The long sequence therefore identifies
\[
H^{-a}(\mathbb D\tau_{\geq a}K)
\simeq\mathbb D H^a(K).
\tag{5.7v}
\]
The maps are the functorial truncation and evaluation maps, so the resulting isomorphism is natural. This proves (5.7b), including \(q=0\) used in the minimal-extension argument above.

If every \(H^a(K)\) is regular, the composition-series argument above and (5.7b) make every cohomology module of \(\mathbb DK\) regular. Boundedness is retained by (5.7u). Thus \(\mathbb D\) preserves \(D^b_{\mathrm{rh}}\); coherent biduality gives its inverse. Conversely regularity of \(\mathbb DK\) gives regularity of \(K\). This completes the theorem in its full original singular-support and bounded-complex scope.

![The dual lattice, transposed extension map, and reversed composition series](assets/regular-duality-mechanism.png)

**Figure.** The lattice panel records the pairing and negative-transpose residue (5.7c)–(5.7f). The two extension rows are identified by duality in the reversed direction; the equality is the actual canonical-map calculation (5.7l)–(5.7p), and their images are (5.7r). The last panel records (5.7t) and the exact degree reversal (5.7b). All statements allow arbitrary rank, Jordan blocks and closed supports. Source reading: the free Bernstein text linked in Section 1; every displayed mechanism is proved above. The reproducible figure source records the same proof locators.



### Relative analytic generation in every projective dimension

We now prove finite twist generation near a projective fibre for every coherent analytic sheaf. This supplies an analytic input for later direct-image arguments, including sheaves with torsion or singular support and sheaves that are not flat over the base.

Freely accessible reading: [Norguet, Images de faisceaux analytiques cohérents](https://www.numdam.org/item/SL_1957-1958__1__A7_0.pdf), Section II.1–II.2, printed pp. 11-10–11-14, for the projective-line mechanism. The fixed-chart estimates, matrix factorization, product induction and finite split-trace descent are proved below.

**Theorem 5.8 (relative analytic generation).** Let \(D\subset\mathbf C^m\) be a polydisc, let \(y_0\in D\), and let \(F\) be coherent analytic on \(\mathbf P^n(\mathbf C)\times D\). There are a smaller polydisc \(D'\ni y_0\) and \(k_0\ge0\) such that \(F(k_0)\) is generated by finitely many global holomorphic sections on the entire product. For every \(k\ge k_0\), the same \(D'\) works, with a finite generating list for that \(k\).

For \(n=0\), choose finite local generators near \(y_0\) and shrink. The complete projective-line argument proves \(n=1\) by Cartan A/B, Laurent approximation and convergent matrix factorization. We first deduce its particular coherent-image theorem, then induct on products and descend through a finite quotient.


#### The projective-line statement and its local inputs

**Lemma 5.8.1 (projective-line generation).** Let \(D\) be a polydisc, let \(y_0\in D\), and let \(A\) be a coherent analytic sheaf on \(\mathbf P^1\times D\). There are a smaller polydisc \(D_0\ni y_0\) and an integer \(k_0\) such that, for every integer \(k\ge k_0\), finitely many sections of \(A(k)\) on \(\mathbf P^1\times D_0\) generate that sheaf. Equivalently a finite sum of \(\mathcal O(-k)\) surjects onto \(A\) there.

The inputs are Oka coherence, Theorem 2.1, and the coherent-kernel property, Theorem 3.1, Cartan A and B, Theorems 5.1 and 4.1, and Cauchy/Laurent expansion with holomorphic parameters. Every open used for Cartan B is a product of a polydisc with a disc, an exterior disc including infinity, or an annulus, hence is Stein by the explicit exhaustions in the programme. No fibrewise cohomological finiteness enters the argument.

#### Bounded Laurent splitting on fixed charts

Fix \(0<r<R<\infty\). Let \(U_1=D_0\times\{|z|<R\}\), \(U_2=D_0\times\{|z|>r\}\), where infinity belongs to the second factor of \(U_2\), and put \(U_{12}=U_1\cap U_2\). A bounded holomorphic function \(f\) on \(U_{12}\) has its normally convergent Laurent expansion
\[
f(y,z)=\sum_{j\in\mathbf Z}c_j(y)z^j=f_+(y,z)+f_-(y,z),
\]
where \(f_+\) extends to \(U_1\) and \(f_-\), its strictly negative part, extends to \(U_2\) and vanishes at infinity. The coefficients are holomorphic in \(y\) by their circle integrals.

There is a constant \(K_{r,R}\) independent of \(f,D_0\) such that
\[
\|f_+\|_{U_1},\ \|f_-\|_{U_2}\le K_{r,R}\|f\|_{U_{12}}.
\tag{5.8a}
\]
Here and below suprema are taken over the open domains; the estimates hold whenever these suprema are finite. To prove them put \(s=(r+R)/2\), \(M=\|f\|\). Cauchy estimates on radii tending to \(R\) give \(|c_j|\le MR^{-j}\) for \(j\ge0\), uniformly in \(y\). Thus \(|f_+|\le MR/(R-s)\) on \(|z|\le s\). On radii tending to \(r\), \(|c_{-j}|\le Mr^j\) for \(j\ge1\); hence \(|f_-|\le Mr/(s-r)\) for \(|z|\ge s\). On \(s<|z|<R\), use \(f_+=f-f_-\); on \(r<|z|<s\), use \(f_-=f-f_+\). Together these give (5.8a), for example with
\[
K_{r,R}=1+\frac{2R}{R-r}.
\]
This proves a bounded splitting on the *fixed* full chart domains; no successive domain shrink is necessary. The two different annulus boundary circles, separated by \(R-r>0\), are essential to this estimate.

For square matrices use a submultiplicative row-sum norm, with \(\|I\|=1\). Applying the scalar splitting entrywise produces, for a fixed matrix size, a constant \(K\ge1\) with
\[
L=U_1-U_2,
\qquad \|U_i\|\le K\|L\|,
\tag{5.8b}
\]
where \(U_i\) is holomorphic on the corresponding chart. The same estimates are uniform in all base parameters.

#### Convergent multiplicative factorization

For \(K\) from (5.8b), let \(\epsilon<1/(4K)\). Every matrix \(T\), holomorphic on \(U_{12}\), with \(\|T-I\|<\epsilon\), factors
\[
T=G_2^{-1}G_1,
\tag{5.8c}
\]
where \(G_i\) and \(G_i^{-1}\) are holomorphic on \(U_i\).

Set \(T_0=T=I+L_0\). At step \(j\), split \(L_j=U_{1,j}-U_{2,j}\) by (5.8b), and put
\[
T_{j+1}=(I+U_{2,j})T_j(I+U_{1,j})^{-1}.
\]
Because \(\|U_{i,j}\|\le K\|L_j\|<1/2\), both correction matrices are invertible by the convergent Neumann series and their inverses have norm at most 2. The exact residual identity is
\[
L_{j+1}=U_{2,j}L_j(I+U_{1,j})^{-1},
\qquad \|L_{j+1}\|\le2K\|L_j\|^2\le\tfrac12\|L_j\|.
\tag{5.8d}
\]
Thus \(\|L_j\|\le2^{-j}\epsilon\). Define products recursively by
\[
G_{i,0}=I,\qquad
G_{i,j+1}=(I+U_{i,j})G_{i,j}.
\]
They satisfy \(T_j=G_{2,j}T G_{1,j}^{-1}\). The sum of the correction norms is finite. Products and their inverse products therefore converge uniformly on the full fixed domains, by the submultiplicative product estimate and the estimate
\(\|(I+U)^{-1}-I\|\le2\|U\|\).
Their limits are holomorphic, remain mutual inverses, and \(T_j\to I\). Hence \(I=G_2TG_1^{-1}\), proving (5.8c). No compact-operator theorem, sheaf-frame assumption or flatness assumption is involved.

#### Redundant generators and coefficient matrices

Choose nested polydiscs \(D_0\Subset D_1\Subset D_2\Subset D\), all containing \(y_0\), and radii
\[
0<r_2<r_1<r_0<R_0<R_1<R_2<\infty.
\]
The two Stein opens
\(D_2\times\{|z|<R_2\}\) and
\(D_2\times\{|z|>r_2\}\)
cover \(\mathbf P^1\times D_2\).
Cartan A, then a finite subcover of the compact smaller closed chart sets, provides lists \(s_1,s_2\) of sections on these larger opens generating \(A\) on
\[
D_1\times\{|z|<R_1\},\qquad
D_1\times\{|z|>r_1\}.
\]
Pad the shorter list by zeros so that both are columns of the same length \(t\).

On the Stein overlap \(D_1\times\{r_1<|z|<R_1\}\), each list gives a surjection \(\mathcal O^t\to A\) with coherent kernel. Cartan B makes its map on global sections surjective. Componentwise lifting supplies holomorphic \(t\times t\) matrices \(B,C\) there with
\[
s_2=B s_1,\qquad s_1=C s_2.
\tag{5.8e}
\]
The matrices need not be inverses. The sheaf need not be free or flat. Equation (5.8e) is all that will be used.

These matrices are bounded on
\(\overline{D_0}\times\{r_0\le|z|\le R_0\}\).
For any \(\delta>0\), truncate only the far negative Laurent tail of \(B\) and the far positive Laurent tail of \(C\). Normal convergence with parameters gives matrices \(B',C'\) satisfying
\[
\|B-B'\|,\ \|C-C'\|<\delta
\tag{5.8f}
\]
on that compact overlap. The matrix \(B'\) is meromorphic on the inner chart, with a pole only at 0 and of a finite order; its nonnegative Laurent part extends holomorphically to \(|z|<R_1\). Similarly \(C'\) is meromorphic on the outer chart, with a pole only at infinity and of a finite order; its negative part extends holomorphically to \(|z|>r_1\). Let \(b\) dominate both finite pole orders. The holomorphic parameter dependence and the common finite pole bound follow from this one finite truncation, not from an unproved extension of fibre sections.

#### Pole compensation and the exact block matrix

For any \(k\ge2b\), choose a section \(\tau_k\) of \(\mathcal O(k)\) whose zeros are precisely 0 and infinity, with orders \(b\) and \(k-b\), respectively. If \(b=0\), increase it to 1 first. The binary monomial \(X_1^bX_0^{k-b}\), in coordinates where \(z=X_1/X_0\), supplies this section. Multiplication by \(\tau_k\) cancels every pole of \(B's_1\) and \(C's_2\). Put
\[
\begin{array}{ll}
S_1=\binom{\tau_k s_1}{\tau_k B's_1}
&\text{on }U_1=D_0\times\{|z|<R_0\},\\[3pt]
S_2=\binom{\tau_k C's_2}{\tau_k s_2}
&\text{on }U_2=D_0\times\{|z|>r_0\}.
\end{array}
\]
These are columns of \(2t\) genuine holomorphic sections of \(A(k)\). On their overlap, (5.8e) gives the exact equality
\[
S_2=T S_1,
\qquad
T=I_{2t}+
\begin{pmatrix}
(C'-C)B&0\\
B-B'&0
\end{pmatrix}.
\tag{5.8g}
\]
For instance the top difference is
\(\tau_k(C'-C)s_2=\tau_k(C'-C)Bs_1\),
and the bottom difference is \(\tau_k(B-B')s_1\).
Consequently \(\|T-I\|\le\delta(1+\|B\|)\).
Choose \(\delta\) so that this is below the factorization threshold in the factorization argument above. The matrix \(T\) and its smallness estimate are independent of \(k\).

Factor \(T=G_2^{-1}G_1\). Then
\[
G_1S_1=G_2S_2
\]
on the overlap. These lists glue to \(2t\) global holomorphic sections of \(A(k)\) on \(\mathbf P^1\times D_0\). Each \(G_i\) is invertible, so it does not alter the local submodule generated by the corresponding list. The first half of \(S_1\) already generates away from 0; the second half of \(S_2\) already generates away from infinity. Hence the glued sections generate everywhere except possibly at those two endpoints.

Repeat the construction using a projective coordinate whose zero and infinity are two different points, neither of them one of the original endpoints. Shrink the base finitely once more if necessary and raise \(k\) above the maximum of the two bounds. Each construction works for every such \(k\). Their combined finite global list generates at every point, since the two exceptional endpoint sets are disjoint. This proves the theorem.

![The pole compensation, exact block matrix and convergent gluing of redundant generator lists](assets/relative-p1-generation-mechanism.png)

The diagram records the actual chart sections and the exact comparison matrix in (5.8g). The matrix corrections in (5.8b)–(5.8d) are functions on those fixed charts, and the products are invertible there. The union of the two endpoint-complement constructions generates every stalk. The reproducible drawing source is original CC0 explanatory material; the full argument and estimates remain above.


#### Coherent projective-line images from generation

**Lemma 5.8.2 (projective-line coherent images).** For a complex manifold \(Z\), put \(p:\mathbf P^1\times Z\to Z\). We prove that \(R^q p_*H\) is coherent for coherent \(H\), and zero for \(q>1\).

Work near \(z_0\) in a coordinate polydisc \(V\). The two standard projective charts and their intersection, multiplied by any smaller polydisc, are \(\mathbf C\times V\), \(\mathbf C\times V\), and \(\mathbf C^*\times V\). They are Stein: sums of \(|w|^2\), of \(|w|^{-2}\) for punctured coordinates, and of reciprocal distances to polydisc boundaries give strictly plurisubharmonic exhaustions. Cartan B makes this cover acyclic for every coherent sheaf. Its Čech complex has degrees 0 and 1; the open-set description of higher direct-image sheaves gives
\[
R^q p_*K=0\quad(q>1)
\tag{5.8h}
\]
for every coherent \(K\). This bound is independent of proper coherence.

The directly proved parameter Laurent calculation in Serre's comparison theorems and Chow's theorem, Lemma 6.5, gives
\[
R^q p_*\mathcal O(a)
 =H^q(\mathbf P^1_{\mathbf C},\mathcal O(a))
       \otimes_{\mathbf C}\mathcal O_V,\qquad q=0,1.
\tag{5.8i}
\]
Its proof decomposes the finite Čech complex by Laurent negative-coordinate sets. Cauchy estimates justify coefficient projections and the contracting homotopies on normally convergent series with holomorphic parameters. The surviving monomial sets are finite. This calculation invokes neither Grauert nor arbitrary analytic coherent images.

Apply projective-line generation to \(H\), then to two successive coherent kernels. Three finite base shrinkings give an exact sequence on the whole product
\[
0\to K\to E_2\to E_1\to E_0\to H\to0,
\qquad E_i=\mathcal O(-a_i)^{N_i}.
\tag{5.8j}
\]
The kernels are coherent by Oka's coherent-category consequence. Locally, one can see the needed kernel assertion by lifting the finite generators of the source to a target presentation: coherence gives finitely many relations among their images; quotienting these relations by the source relations presents the kernel.

Put \(C=[E_2\to E_1\to E_0]\) in degrees \(-2,-1,0\). The augmentation has
\[
\operatorname{Cone}(C\to H)\simeq K[3].
\tag{5.8k}
\]
Indeed the kernel in degree \(-2\) is the only cohomology besides \(H^0(C)=H\), and the cone shifts it to degree \(-3\). The finite termwise spectral sequence
\[
E_1^{a,b}=R^b p_*C^a,\qquad
-2\le a\le0,\quad0\le b\le1
\]
has coherent entries by (5.8i), six positions, and a finite filtration of its abutment by coherent subquotients. Thus all cohomology sheaves of \(Rp_*C\) are coherent. By (5.8h), \(Rp_*K[3]\) has cohomology only in degrees \(-3,-2\); the triangle (5.8k) identifies
\[
\mathcal H^q(Rp_*C)\xrightarrow{\sim}R^q p_*H
\qquad(q\ge0).
\tag{5.8l}
\]
This proves coherence near \(z_0\), hence on \(Z\). Open restriction identifies these calculations with the intrinsic direct-image sheaves.

#### Generation on products of projective lines

Write
\[
Q_n=(\mathbf P^1)^n,\qquad
L_n(a_1,\ldots,a_n)=\boxtimes_i\mathcal O_{\mathbf P^1}(a_i).
\]
Inductively we prove that any coherent \(A\) on \(Q_n\times D\) has, after shrinking \(D\), finitely many global sections generating
\[
A\otimes L_n(h,\ldots,h)
\tag{5.8m}
\]
for some \(h\ge0\). The cases \(n=0,1\) are established.

Project the last factor,
\[
p:Q_n\times D\longrightarrow Q_{n-1}\times D=:Z.
\]
For each point of the compact fibre \(Q_{n-1}\times\{y_0\}\), apply projective-line generation over a target coordinate polydisc. It gives a smaller target open \(V_j\), a degree \(d_j\ge0\), and actual finite sections generating \(A\otimes L_n(0,\ldots,0,d_j)\) on the whole \(p^{-1}V_j\). Finitely many such opens cover that target fibre.

Projection \(Q_{n-1}\times D\to D\) is closed, by the compactness of \(Q_{n-1}\). The image of the closed complement of \(\bigcup V_j\) avoids \(y_0\). Thus a smaller polydisc \(D_1\ni y_0\) makes these opens cover every point of \(Q_{n-1}\times D_1\). Let \(d=\max_j d_j\). Multiply the \(j\)-th list by the finite monomial generators of \(\mathcal O_{\mathbf P^1}(d-d_j)\). Those lists generate \(A(d):=A\otimes L_n(0,\ldots,0,d)\) on their whole inverse images.

Lemma 5.8.2 gives coherence of \(G=p_*A(d)\). The lists are sections of \(G\) on the \(V_j\); consequently the intrinsic evaluation
\[
p^*G\longrightarrow A(d)
\tag{5.8n}
\]
is surjective everywhere over \(D_1\). No gluing of the local lists is needed to establish this assertion about the evaluation map.

Apply the induction hypothesis to the coherent \(G\) on \(Q_{n-1}\times D_1\). On a smaller \(D_2\), finitely many sections generate \(G\otimes L_{n-1}(b,\ldots,b)\), for some \(b\ge0\). Pull that finite surjection back and compose with (5.8n). Pullback is right exact, which suffices. This gives generation of \(A\otimes L_n(b,\ldots,b,d)\) on the entire \(Q_n\times D_2\). Put \(h=\max(b,d)\) and multiply by the finite monomial generators of
\[
L_n(h-b,\ldots,h-b,h-d).
\]
All its degrees are nonnegative, so this proves (5.8m). Every fixed induction dimension uses only finitely many neighbourhood shrinkings.

#### The finite symmetric-root quotient and split trace

The product of binary linear forms defines
\[
\rho:Q_n\longrightarrow\mathbf P^n,\quad
([a_1:b_1],\ldots,[a_n:b_n])
\longmapsto\left[\prod_i(a_iX+b_iY)\right].
\tag{5.8o}
\]
The coefficient sections have degree one in each pair and no common zero, since over a residue field the product of nonzero linear forms is nonzero. They define the morphism and the exact twist identification
\[
\rho^*\mathcal O_{\mathbf P^n}(1)=L_n(1,\ldots,1).
\tag{5.8p}
\]
On each nonvanishing-coefficient open the same coefficient trivializes both line bundles, and ratios of coefficients give the transition identifications.

Here is the finite quotient calculation. Choose \(n+1\) distinct points \(\xi_j\in\mathbf P^1\). Let \(U_j\) be the open of binary forms not vanishing at \(\xi_j\). These cover: a nonzero form of degree \(n\) has at most \(n\) distinct zeros, by division by its distinct linear zero factors. Move \(\xi_j\) to \([1:0]\). On \(U_j\) write the form as
\[
X^n+e_1X^{n-1}Y+\cdots+e_nY^n.
\]
In the corresponding linear-form coefficient coordinates, the inverse image has every \(a_i\ne0\); put \(x_i=b_i/a_i\). Then \(U_j=\operatorname{Spec}\mathbf C[e_1,\ldots,e_n]\), its inverse image is \(\operatorname{Spec}\mathbf C[x_1,\ldots,x_n]\), and the \(e_i\) pull back to elementary symmetric functions of the \(x_i\). Each \(x_i\) satisfies
\[
T^n-e_1T^{n-1}+\cdots+(-1)^ne_n=0.
\tag{5.8q}
\]
Successive reduction by these monic equations shows that the monomials with all exponents \(<n\) span the root ring over the coefficient ring. Hence \(\rho\) is finite on this finite affine cover.

For completeness, the invariant ring is exactly the coefficient ring. In the lexicographic order \(x_1>\cdots>x_n\), the leading exponent sequence of a symmetric homogeneous polynomial is \(a_1\ge\cdots\ge a_n\); otherwise a permutation gives a larger monomial. The product
\[
e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots e_n^{a_n}
\]
has precisely that leading monomial with coefficient 1. Subtract its multiple. There are finitely many monomials of the fixed total degree, so repetition terminates. Applying this to each homogeneous component expresses every invariant polynomial in the \(e_i\). Distinct monomials in the \(e_i\) have distinct leading exponent sequences, proving algebraic independence as well. Thus
\[
\mathbf C[x_1,\ldots,x_n]^{\mathfrak S_n}
=\mathbf C[e_1,\ldots,e_n].
\tag{5.8r}
\]

Let \(B=\rho_*\mathcal O_{Q_n}\), an algebraic coherent sheaf by the finite module calculation. Permuting factors acts globally on \(B\); (5.8r) identifies \(B^{\mathfrak S_n}\) with the unit copy of \(\mathcal O_{\mathbf P^n}\). Those identifications agree on overlaps. Averaging therefore gives a global \(\mathcal O\)-linear retraction
\[
\tau:B\longrightarrow\mathcal O_{\mathbf P^n},
\qquad \tau=\frac1{n!}\sum_{\sigma\in\mathfrak S_n}\sigma,
\qquad \tau(1)=1.
\tag{5.8s}
\]
The codomain denotes the invariant summand. This formula is defined at branching points.

We identify this fixed algebra on the analytic product by an earlier comparison proved for algebraic sheaves. The algebraic morphism \(\rho\times\operatorname{id}_{\mathbf A^m}\) is projective: the iterated Segre map is a closed embedding \(Q_n\hookrightarrow\mathbf P^{2^n-1}\), its rank-one equations define its image, and its coordinate ratios give the inverse on each chart. The closed graph of \(\rho\), together with that embedding, gives a closed immersion into \(\mathbf P^{2^n-1}_{\mathbf P^n}\); take the product with \(\mathbf A^m\).

Its algebraic direct-image algebra is the pullback of \(B\): on the preceding affine cover the root algebra is tensored with \(\mathbf C[u_1,\ldots,u_m]\). Apply projective comparison for algebraic sheaves, Proposition 6.6 to the algebraic structure sheaf of this fixed morphism. Restricting the natural comparison to \(D_2\subset\mathbf C^m\) gives
\[
B_{D_2}:=(\rho\times\operatorname{id}_{D_2})_*
       \mathcal O_{Q_n\times D_2}
 \cong\operatorname{pr}_1^*B^{\mathrm{an}}.
\tag{5.8t}
\]
The proof of Proposition 6.6 uses algebraic finite twist presentations, the directly proved parameter twist calculation of Lemma 6.5, and finite cohomological bounds. It never assumes generation or coherent proper images of arbitrary analytic coherent sheaves. Its naturality for permutations carries \(\tau\) to an analytic retraction \(\tau_{D_2}\), still with \(\tau_{D_2}(1)=1\). In particular this fixed \(B_{D_2}\) is coherent.

#### Finite exact pushforward descends the generators

Write \(\rho_D=\rho\times\operatorname{id}_{D_2}\). Its continuous map is proper: inverse images of compact sets are closed subsets of \(Q_n\) times their compact base projection. Its fibres are finite; on the preceding affine charts each root coordinate has at most \(n\) possible values by (5.8q).

For any sheaf \(S\) of abelian groups on its source, there is a canonical stalk identification
\[
(\rho_{D*}S)_v=\bigoplus_{w\in\rho_D^{-1}(v)}S_w.
\tag{5.8u}
\]
Indeed representatives of the finitely many fibre germs can be chosen on pairwise disjoint neighbourhoods. The complement of their union is closed; properness gives a target neighbourhood whose inverse image is contained in that union. The representatives glue there. This proves surjectivity. If a section germ is zero at every fibre point, choose smaller neighbourhoods on which it is zero and repeat the same argument, proving injectivity. Properness gives the closed-map assertion used here by restricting over a relatively compact target neighbourhood and using compactness to extract a convergent subsequence.

Stalk exactness and the finite sum show that \(\rho_{D*}\) is exact on sheaves of modules. For any analytic \(\mathcal O\)-module \(T\), the natural projection formula is
\[
\rho_{D*}\rho_D^*T=B_{D_2}\otimes_{\mathcal O}T.
\tag{5.8v}
\]
At \(v\) this is the distributivity isomorphism between
\[
\bigoplus_{w\mid v}\left(\mathcal O_{Q_n\times D_2,w}
          \otimes_{\mathcal O_{\mathbf P^n\times D_2,v}}T_v\right)
\quad\text{and}\quad
\left(\bigoplus_{w\mid v}\mathcal O_{Q_n\times D_2,w}\right)
          \otimes_{\mathcal O_{\mathbf P^n\times D_2,v}}T_v.
\]
It applies to arbitrary modules.

The pullback of the original \(F\) to \(Q_n\times D\) is coherent: pull back a finite local presentation, and use Oka. the product-induction argument above and (5.8p) give a smaller \(D_2\), \(h\ge0\), and an actual global surjection
\[
\mathcal O_{Q_n\times D_2}^{\,N}
\twoheadrightarrow \rho_D^*F(h).
\tag{5.8w}
\]
Apply finite exact pushforward, (5.8v), and the retraction:
\[
B_{D_2}^{\,N}\twoheadrightarrow
B_{D_2}\otimes F(h)
\xrightarrow{\ \tau_{D_2}\otimes1\ }F(h).
\tag{5.8x}
\]
The second map is surjective because \(t\mapsto1\otimes t\) is its right inverse.

Choose a fixed \(e\ge0\) such that \(B(e)\) is generated by finitely many algebraic global sections. The earlier algebraic Serre proof, Lemma 1.1 and Proposition 1.2, applies to this algebraic \(B\). Its construction chooses finite module generators on each standard affine chart. A section on that principal chart extends after multiplication by a power of its coordinate: clear finitely many localized denominators on a finite affine trivializing cover, then kill the finitely many overlap differences by a further common power and glue. Raise these finitely many exponents to one common \(e\). This proves the asserted finite generation without any analytic generation input.

Analytify that finite surjection, pull it across \(D_2\), and use (5.8t):
\[
\mathcal O_{\mathbf P^n\times D_2}^{\,K}
\twoheadrightarrow B_{D_2}(e).
\]
Tensor pullback preserves surjections. Twist (5.8x) by \(\mathcal O(e)\) and compose \(N\) copies of this surjection. The result is
\[
\mathcal O_{\mathbf P^n\times D_2}^{\,KN}
\twoheadrightarrow F(h+e).
\tag{5.8y}
\]
The images of the standard global basis are finitely many global holomorphic sections generating on the entire product. This proves Theorem 5.8 with \(D'=D_2\), \(k_0=h+e\). For \(k\ge k_0\), multiplication by the finite monomial generators of \(\mathcal O(k-k_0)\) proves the assertion on the same base.

![Product induction, finite symmetric-root quotient and split-trace descent of generators](assets/relative-generation-descent-mechanism.png)

The diagram records the actual twist (5.8p) and surjections (5.8w)–(5.8y). Its trace is normalized averaging, defined at every branch point. The reproducible drawing source is original CC0 material.


### Coherence of the actual locally projective analytic operator image

**Theorem 5.9.** Let \(f:X\to Y\) be a locally projective holomorphic map of complex manifolds, \(y_0\in Y\), and \(M\) a coherent analytic operator module. Suppose that on a neighbourhood of the compact fibre a coherent holomorphic submodule \(L\subset M\) generates \(M\) under \(\mathcal D_X\). Then, near \(y_0\), the actual derived direct image \(f_+M\) has bounded coherent operator cohomology. Every closed or singular support is allowed; holonomicity of \(M\) is unnecessary. The statement also holds for bounded complexes whose cohomology modules each have such a generator near the fibre. The proof applies to right modules and transfers to the programme's left-module conventions by the exact density equivalence.

The initial coherent generator is an explicit hypothesis. Its construction for every analytic regular holonomic module remains part of the full proper-regularity argument. We first prove ordinary coherent holomorphic images in every projective dimension, then construct a finite operator resolution and check the actual target action and every output degree.

Freely accessible support reading: [Schapira, An Introduction to Sheaves on Grothendieck Topologies](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Sections 4.2–4.4 and 5.1. The exact earlier programme proofs are linked below; the operator and finite-cone arguments are proved here.

#### Coherent holomorphic images in every projective dimension

**Lemma 5.9.1 (locally projective coherent holomorphic images).** Let \(p:\mathbf P^n\times D\to D\) be projection, where \(D\) is a coordinate polydisc. Theorem 5.8 gives, for any coherent analytic \(A\) and chosen \(y_0\), a finite epimorphism
\[
\mathcal O(-k)^r\twoheadrightarrow A
\tag{5.9a}
\]
on the entire product over a smaller polydisc. The proof includes torsion, nonflat coefficients and singular support.

The \(n+1\) standard projective charts and every finite nonempty intersection, multiplied by a base polydisc, are Stein. In a fixed affine chart an intersection is a product of affine and punctured affine coordinates; sums of squared coordinate moduli, inverse squared punctured-coordinate moduli and reciprocal boundary distances give its strictly plurisubharmonic exhaustion. Cartan B, Theorem 4.1 therefore makes this finite cover acyclic for each coherent analytic sheaf. Its Čech complex gives
\[
R^b p_*A=0\qquad(b>n).
\tag{5.9b}
\]
This uses no coherent-image theorem. The independently proved parameter Laurent calculation gives
\[
R^b p_*\mathcal O(k)
 =H^b(\mathbf P^n,\mathcal O(k))\otimes_{\mathbf C}\mathcal O_D;
\tag{5.9c}
\]
the surviving Laurent monomial sets are finite. Its exact earlier proof is the parameter Laurent calculation, Lemma 6.5.

Apply (5.9a) to \(A\) and then to \(n+1\) successive coherent kernels. There are only \(n+2\) shrinkings. This gives
\[
0\to K\to E_{n+1}\to\cdots\to E_0\to A\to0,
\qquad E_j=\mathcal O(-k_j)^{r_j}.
\tag{5.9d}
\]
Let \(C=[E_{n+1}\to\cdots\to E_0]\) in degrees \(-n-1,\ldots,0\). Its augmentation has cone \(K[n+2]\). Formula (5.9b) puts \(Rp_*K[n+2]\) in degrees at most \(-2\). Consequently
\[
\mathcal H^q(Rp_*C)\xrightarrow{\sim}R^q p_*A
\qquad(q\ge0).
\tag{5.9e}
\]
The bounded termwise spectral sequence of \(C\) has finitely many entries, coherent by (5.9c). Kernels, images, quotients and finite extensions in the coherent holomorphic category are coherent by the proved Oka/coherent-category argument. This proves coherence of every \(R^q p_*A\). Thus \(Rp_*\) sends \(D^b_{\mathrm{coh}}(\mathcal O)\) to \(D^b_{\mathrm{coh}}(\mathcal O_D)\), with amplitude \([0,n]\) on modules, by the finite Postnikov argument.

For a closed holomorphic embedding of complex manifolds, ordinary pushforward is exact: its stalk at a point of the closed submanifold is the source stalk, and elsewhere is zero. In adapted coordinates the defining ideal is generated by the normal coordinates. Lift the finite matrix entries of a coherent source presentation to the ambient coordinate neighbourhood, and add the normal-coordinate relations on its finite generators. This gives a finite target holomorphic presentation, so pushforward is coherent by Oka. Factoring a locally projective holomorphic map of complex manifolds through this embedding proves the image theorem for every coherent analytic source sheaf. The local projection dimension supplies a sufficient upper bound.

#### A coherent global generator and finite induced resolutions

Work with right operator modules. The exact left/right equivalence, Theorem 5.1 is \(M\mapsto\omega_Z\otimes M\); tensoring a coherent generator by that line bundle preserves coherence. The local volume and transpose proof uses only PBW and the Leibniz identities, which hold for holomorphic operators, so it proves the same analytic equivalence. In a volume frame the right vector-field action is minus the left action and minus the holomorphic divergence. Induction on operator order therefore shows that the density-twisted generator generates the converted module, and conversely. Here \(Z=\mathbf P^n\times D\), \(d=\dim_{\mathbf C}Z\). Suppose a coherent right \(\mathcal D_Z\)-module \(M\) has one coherent \(\mathcal O_Z\)-submodule \(L\) with \(L\mathcal D_Z=M\) on a neighbourhood of the compact fibre.

Properness makes that neighbourhood contain the entire inverse image of a smaller base: the image of its closed complement is closed and avoids \(y_0\). Apply (5.9a) to \(L\). If \(E_0=\mathcal O(-k_0)^{r_0}\), the composed action map is an actual right-operator epimorphism
\[
A_0:=E_0\otimes_{\mathcal O_Z}\mathcal D_Z\twoheadrightarrow M.
\tag{5.9f}
\]
Here \(E_0\) is finite locally free; no connection on \(E_0\) is required. Right multiplication acts on the last factor. The globally defined order pieces
\[
G_jA_0=E_0\otimes_{\mathcal O_Z}\mathcal D_{Z,\le j}
\quad(j\ge0),\qquad G_jA_0=0\quad(j<0)
\tag{5.9g}
\]
are coherent right holomorphic modules: in a frame of \(E_0\), these are finite copies of the finite-order operator pieces, which are finite free for the right holomorphic action by right normal ordering. Changing the frame multiplies by order-zero coefficients and preserves these pieces. PBW shows their symbol module is generated by the finite frame in degree zero. Thus (5.9g) is a global good filtration.

Put \(N_1=\ker(A_0\to M)\). Analytic operator coherence makes \(N_1\) coherent. The global intersections \(G_jN_1=N_1\cap G_jA_0\) are coherent holomorphic and locally good. Indeed locally \(A_0\) is a finite free filtered operator module and \(N_1\) is the image of a finite operator matrix; the uniform image-and-relation proof, Lemma 3.0c.4, proves goodness of the **induced** filtration. It also proves coherence of each of its finite-degree pieces by Oka. Thus no filtration of \(M\) was needed to obtain the first kernel's global pieces.

For completeness the same assertion holds for a coherent submodule of any already good filtered coherent module \(B\). Locally choose a strict finite filtered free epimorphism \(F\to B\), by lifting finite homogeneous symbol generators and lowering order. The inverse image \(H\) of the submodule is coherent and has a good induced filtration in \(F\) by Lemma 3.0c.4. Strictness identifies the desired submodule's degree \(j\) with the image of \(H\cap F_j\) in \(B_j\). Both are coherent holomorphic, so the image is coherent. The graded image is a quotient of the finite graded module of \(H\), hence finite. These identities prove the assertion, rather than merely assuming that coherence of an operator module implies coherence of an arbitrary holomorphic submodule.

The pieces of \(N_1\) exhaust it. At each point of the compact fibre, finitely many local operator generators lie in one degree. Their membership in that sheaf piece holds on a neighbourhood of the point. A finite cover and the maximum of these finitely many degrees give one global coherent piece generating \(N_1\) on a neighbourhood of the fibre. Properness again supplies a smaller entire inverse image. Apply (5.9a) to that piece and obtain
\[
A_1=E_1\otimes\mathcal D_Z\twoheadrightarrow N_1,
\qquad E_1=\mathcal O(-k_1)^{r_1}.
\tag{5.9h}
\]
Its kernel has the induced global good filtration from \(A_1\). Repeat a fixed finite number of times. Each kernel and finite coherent piece has just been constructed; only finitely many base shrinkings occur. This yields, for any fixed integer \(s\ge0\), an actual exact sequence
\[
0\to K\to A_s\to\cdots\to A_0\to M\to0,
\qquad A_j=E_j\otimes\mathcal D_Z,
\quad E_j=\mathcal O(-k_j)^{r_j}.
\tag{5.9i}
\]
Consequently the initial coherent global generator, and not a separately presumed filtration of every syzygy, is the sufficient input. Conversely that generator gives \(L\mathcal D_{\le j}\) as global good pieces: locally place its finitely many generators in a coherent local good piece of \(M\); the finite-order images are coherent inside that piece by Oka, exhaustive, and their symbol module is generated in degree zero. This recovers the generator/good-filtration equivalence near the compact fibre.

#### The induced-term images and actual target action

The right-module direct image is
\[
p_+N=Rp_*\bigl(N\otimes^L_{\mathcal D_Z}\mathcal D_{Z\to D}\bigr),
\qquad
\mathcal D_{Z\to D}
 =\mathcal O_Z\otimes_{p^{-1}\mathcal O_D}p^{-1}\mathcal D_D.
\tag{5.9j}
\]
In a local frame \(E_j\), \(A_j\) is finite free over \(\mathcal D_Z\). Thus its derived transfer tensor is its ordinary tensor, canonically
\[
A_j\otimes^L_{\mathcal D_Z}\mathcal D_{Z\to D}
 =E_j\otimes_{p^{-1}\mathcal O_D}p^{-1}\mathcal D_D.
\tag{5.9k}
\]
There is no assertion that the forward transfer is left flat over \(\mathcal D_Z\); the local freeness of this particular source term is what removes its Tor.

On a coordinate base the left holomorphic PBW basis makes \(\mathcal D_D\) the sheaf coproduct of its normally ordered finite derivative monomials. Proper derived image commutes with those coproducts in the bounded-below situation used here. The exact earlier proofs are compact germs and c-soft coproducts, (C1)–(C4), proper coproducts, (F4), and derived fibres and image acyclicity, (F6). Briefly, coproducts of c-soft sheaves are c-soft because a section on a compact subset uses a single finite set of summands; proper underived image has the same finite-summand property on its compact fibres. Sum injective resolutions in nonnegative degrees. The resulting resolution has termwise c-soft, image-acyclic terms, and computes the image of the coproduct. Hence the comparison is the specific proper projection map, not an assertion about unrestricted sections on a fixed open.

Finite-order projection and this coproduct comparison give
\[
p_+A_j\simeq Rp_*E_j\otimes_{\mathcal O_D}\mathcal D_D.
\tag{5.9l}
\]
This is a right \(\mathcal D_D\)-linear identity. At the sheaf level it takes \(s\otimes P\) to the coefficient section multiplied by its pulled-back target operator. Right multiplication by a coordinate derivative shifts the PBW monomial. Right multiplication by a target holomorphic function uses
\(\partial^\alpha a=\sum_{\beta\le\alpha}\binom\alpha\beta\partial^\beta(a)\partial^{\alpha-\beta}\); on the source those coefficients are exactly their pullbacks. The finite-order comparisons commute with these operations. Proper coproduct passage and derived resolution comparisons are natural for these coefficient maps, so they commute with the full right action. This verifies the action explicitly.

By (5.9c), every cohomology module of (5.9l) is a finite locally free right operator module, and vanishes outside degrees \(0,\ldots,n\). The identity is stronger here than mere coherent-image preservation. It uses only finite-order analytic operators and the proved twist calculation.

#### Finite transfer bounds and removal of the resolution tail

We prove the required transfer bound for any holomorphic map \(f:X\to Y\) of complex manifolds. In target coordinates its forward transfer
\[
\mathcal T=\mathcal D_{X\to Y}
=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y
\]
is free as a left \(\mathcal O_X\)-module on the target PBW monomials. Its augmented absolute Spencer complex has terms
\[
\mathcal D_X\otimes_{\mathcal O_X}\bigwedge^rT_X
       \otimes_{\mathcal O_X}\mathcal T,\qquad 0\le r\le d_X,
\]
in degrees \(-r\). Its differential is the alternating sum of \(P\xi_i\otimes t-P\otimes\xi_i t\), with the alternating Lie-bracket terms. These formulas are coordinate invariant, glue and commute with the right \(f^{-1}\mathcal D_Y\)-action.

Filter the first operator factor by its order plus the wedge degree. The terms involving \(\xi_i t\) and brackets have lower filtration degree. The graded augmented complex is Koszul on the source cotangent variables with the flat coefficient \(\mathcal T\). Multiplication by a new polynomial variable is injective on a polynomial module with any coefficient module, and its quotient removes that variable. The one-variable two-term exact sequence and induction on the variables prove Koszul exactness. For a Spencer cycle, lift a graded preimage of its leading symbol and subtract its boundary. The order decreases; its lower bound makes this process terminate. Thus the augmented Spencer complex is exact.

Each term is flat as a left \(\mathcal D_X\)-module: its coefficient is \(\mathcal O_X\)-flat, and extension by the right \(\mathcal O_X\)-flat ring \(\mathcal D_X\) preserves that flatness, as tensor associativity tests on a short exact sequence of right operator modules. This finite flat resolution computes the actual transfer tensor on every right operator module, in degrees \([-d_X,0]\). The analytic PBW and coherent-category arguments are proved in the earlier operator lesson.

The earlier uniform real-manifold bound and finite c-soft resolution, (D8)–(D10), give proper sheaf-image amplitude \([0,2d_X]\) for every complex sheaf. Apply these two bounds to the projection, with \(d=\dim_{\mathbf C}Z\). Thus for every operator module \(T\),
\[
p_+T\in D^{[-d,2d]}(\mathcal D_D).
\tag{5.9m}
\]
All transfer tensors, resolution triangles and images above are formed in right operator-module categories. For these bounds, forgetting the \(p^{-1}\mathcal D_D\)-action gives the ordinary sheaf-derived image: forgetting to complex sheaves preserves injectives because its left adjoint \(p^{-1}\mathcal D_D\otimes_{\mathbf C}(-)\) is exact. Hence the underlying sheaf bound applies to the actual operator image. The displayed interval is sufficient; no optimality is claimed.

Take the finite resolution (5.9i) with
\[
s=3d+1,
\qquad C=[A_s\to\cdots\to A_0]
\text{ in degrees }-s,\ldots,0.
\tag{5.9n}
\]
Its augmentation to \(M\) has exactly
\[
\operatorname{Cone}(C\to M)\simeq K[s+1].
\tag{5.9o}
\]
The sole unresolved leftmost syzygy is in degree \(-s\) of \(C\) and degree \(-s-1\) of that cone. Apply the actual triangulated operator functor (5.9j). Formula (5.9m) gives
\[
p_+K[s+1]\in
D^{[-d-s-1,\,2d-s-1]}
 =D^{[-4d-2,\,-d-2]}.
\tag{5.9p}
\]
Both degrees \(q-1\) and \(q\) of this cone vanish for every \(q\ge-d\). The long exact sequence therefore gives the natural right-operator isomorphisms
\[
\mathcal H^q(p_+C)\xrightarrow{\sim}\mathcal H^q(p_+M)
\qquad(q\ge-d).
\tag{5.9q}
\]
The independent bound (5.9m) already kills every degree \(q<-d\) of \(p_+M\). Thus (5.9q) covers **every possibly nonzero degree** of the actual output.

The complex \(C\) has finitely many terms. Successive brutal filtration triangles express \(p_+C\) as finitely many cones of shifts of the \(p_+A_j\). Each latter object has bounded coherent cohomology by (5.9l). Analytic operator coherence makes kernels, images and quotients of coherent operator morphisms coherent, and finite extensions are coherent by the block-presentation argument. The long exact sequences for these finitely many cones therefore show that \(p_+C\) has bounded coherent operator cohomology. Formula (5.9q) proves the same conclusion for \(p_+M\). No convergence or infinite-width totalization is used in this deduction. Equivalently, the augmentation identifies the actual output with the canonical truncation \(\tau_{\ge-d}p_+C\).

![The exact finite augmentation and the independent degree separation](assets/finite-operator-image-coherence.png)

The figure is a schematic of cohomological degree intervals, not a numerical estimate or a claim of sharp bounds. Its maps are (5.9o) after applying \(p_+\); its upper interval is the exact sufficient bound (5.9m), and its lower interval is (5.9p) for the specified integer \(s=3d+1\). The two absent cone degrees establish (5.9q). The reproducible drawing source supplies the original CC0 diagram.

#### Closed embeddings, bounded complexes and the generator hypothesis

For a closed holomorphic embedding \(i:X\hookrightarrow Z\), the right forward transfer has its global order-zero section \(1\) and locally is the normal-derivative polynomial basis over the source. The canonical map
\[
i_*N\longrightarrow i_+N,
\qquad m\longmapsto m\otimes1
\tag{5.9r}
\]
is holomorphically linear and injective: in adapted coordinates it is the constant normal-derivative coefficient, and multiplication by a target function on it is multiplication by its source restriction. Normal derivative PBW proves that \(i_+\) is exact here. If \(L\subset N\) is a coherent global holomorphic generator, its image \(i_*L\) in (5.9r) is coherent and generates \(i_+N\) under the target operators. Indeed the other normal monomials are obtained by target right derivatives, and a source tangential operator acting on \(m\) is, in the tensor balance relation, a corresponding local target operator acting on \(m\otimes1\). These local generation assertions determine the global one. The finite source presentation with the normal-coordinate relations proves target operator coherence, explicitly: lift a finite source operator presentation to tangential ambient operators and add the normal-coordinate annihilation relations for its finite generators. Right normal ordering identifies the resulting finite quotient with the normal-derivative expansion of the transfer module. Analytic operator coherence gives target coherence. In right-module form the order-zero submodule has no extra normal determinant; the left-module conversion produces exactly that section's transfer line \(\det N_{X/Z}\).

Therefore factoring a locally projective holomorphic map of complex manifolds through a closed embedding and projection proves:

> If a coherent analytic operator module has a coherent global holomorphic generator on a neighbourhood of the chosen compact fibre, its actual derived locally projective direct image has bounded coherent operator cohomology near the chosen target point.

The property of having that generator is local near the fibre in this assertion; it is not assumed on all of the manifold. A bounded complex whose finitely many cohomology modules have such generators is covered after a common finite base shrinking, using its finite Postnikov tower and the coherent-category closure just proved. The general transfer/topological bound gives the sufficient range \([a-d_X,b+2d_X]\) for input cohomology in \([a,b]\).

This proves coherence for singular-support source modules once their generators exist. It does not prove the filtered characteristic transport inequality or holonomicity, nor the radical regular-filtration condition, canonical global lattice for arbitrary regular holonomic modules, convergent infinite-order extension, its faithful flatness, regularization, regular-pair Hom comparison, or the unit-compatible infinite-order projective comparison. The arbitrary proper holomorphic and support-proper theorem, including nonprojective maps, remains the active full obligation.


### A coherent cotangent image and its analytic transported support

Let \(p:Z=\mathbf P^n\times D\to D\), \(m=\dim D\), \(d=n+m\), and set
\[
\begin{aligned}
W&=Z\times_D T^*D,\\
j&:W\hookrightarrow T^*Z,\\
j(z,\eta)&=(z,(dp_z)^t\eta),\\
q&:W\to T^*D,\\
q(z,\eta)&=\eta.
\end{aligned}
\tag{5.10a}
\]
The image of \(j\) consists exactly of the covectors whose vertical components vanish. The projection \(q\) is proper, and in base coordinates is the projective product projection \(\mathbf P^n\times T^*D\to T^*D\).

**Theorem 5.10 (the cotangent image).** For every coherent analytic sheaf \(G\) on \(T^*Z\), the actual object
\[
B=Rq_*Lj^*G
\tag{5.10b}
\]
has bounded coherent holomorphic cohomology on \(T^*D\), with sufficient range \([-n,n]\). Moreover
\[
\operatorname{Supp}\mathcal H^a(B)
\subset q\bigl(j^{-1}\operatorname{Supp}G\bigr)
\qquad\text{for every }a,
\tag{5.10c}
\]
and the set on the right is a closed analytic subset.

**Proof.** Locally choose fibre coordinates \(x_1,\ldots,x_n\) and base coordinates \(y_1,\ldots,y_m\). The embedding \(j\) is defined by the vertical cotangent coordinates \(\xi_{x_1},\ldots,\xi_{x_n}\). These form a regular sequence in the local convergent function ring: adjoining each coordinate as an independent analytic variable makes multiplication by it injective, and successive quotients remove it. Their Koszul complex is a length-\(n\) locally free resolution of \(j_*\mathcal O_W\). Exactness follows by the one-variable two-term injection and induction on the number of independent variables, or equivalently by the successive polynomial-coordinate contraction. Tensoring this finite resolution with \(G\) computes \(Lj^*G\). Oka's coherent-category theorem makes each kernel and cohomology coherent. The Koszul homotopies show that the vertical coordinates kill its cohomology, which is therefore coherent over \(\mathcal O_W\), in degrees \(-n,\ldots,0\).

Lemma 5.9.1 proves the locally projective coherent holomorphic image theorem. Apply it to \(q\), on a coordinate polydisc about any point of \(T^*D\). It applies to each coherent cohomology sheaf of \(Lj^*G\) without flatness or smooth-support restrictions, and gives higher-image range \([0,n]\). Its finite cohomology spectral sequence proves that (5.10b) is coherent and lies in \([-n,n]\).

Every derived-restriction cohomology sheaf is supported on \(S=j^{-1}\operatorname{Supp}G\): away from that set the input \(G\) vanishes on a neighbourhood and so does its tensor Koszul complex. Properness makes \(q(S)\) closed. The image complex restricted to its open complement is zero, since every source cohomology sheaf there vanishes. Open restriction of the same derived image gives (5.10c).

To prove analyticity without importing a general proper analytic image theorem, use the possibly nonreduced coherent ideal on \(W\) obtained by restricting and generating from the annihilator of \(G\). The annihilator is coherent: locally it is the kernel of the action map from \(\mathcal O\) to the coherent internal Hom sheaf \(\mathcal Hom(G,G)\), whose coherence follows from finite presentations and Oka. Its zero set is \(\operatorname{Supp}G\) by the finite-module annihilator criterion; restricting its finite generators gives the zero set \(S\) on \(W\). The quotient \(\mathcal O_S\), viewed as a coherent sheaf on \(W\), has coherent \(q_*\mathcal O_S\) by the just-proved projective image theorem. Its support is exactly \(q(S)\). Outside that image it vanishes. At a point of the image, its globally defined unit has a nonzero stalk in \(q_*\mathcal O_S\): if that unit became zero on the inverse image of some target neighbourhood, its source germ at a chosen point of the nonempty fibre would be zero, contradicting the unit in the nonzero analytic local quotient. Thus the coherent support of \(q_*\mathcal O_S\) is the stated set, making it analytic by a finite local presentation. \(\square\)

For a coherent operator module \(M\) with a global good filtration, apply the lemma to its analytified coherent symbol sheaf
\[
G=\mathcal O_{T^*Z}\otimes_{\operatorname{gr}\mathcal D_Z}\operatorname{gr}M.
\tag{5.10d}
\]
This symbol sheaf is coherent from finite presentations: a locally finite presentation of \(\operatorname{gr}M\) over \(\operatorname{Sym}T_Z\) gives a finite matrix with fibre-polynomial holomorphic entries; viewing those entries on \(T^*Z\) presents \(G\) as the cokernel of a finite holomorphic free matrix. Oka proves coherence. Then \(S\) in (5.10c) is the intersection of its actual characteristic support with zero vertical covectors. The maps (5.10a) are the cotangent correspondence for this projection. The lemma proves that the natural derived **candidate** symbol image is coherent on the target cotangent space and has the expected support containment, including at singular-support points.

The characteristic bound for the **actual** operator image still requires a good output filtration and a filtered derived comparison with this symbol object, allowing the necessary spectral-sequence subquotients and filtration strictness. Holonomicity additionally requires the geometric dimension estimate for the transported characteristic set. Formula (5.10c) alone proves neither of those facts. This makes the surviving filtered/microlocal leaf smaller and explicit while preserving full arbitrary-proper regularity as the ultimate goal.

![The actual cotangent embedding and proper projection in the symbol-image lemma](assets/projective-symbol-image-leaf.png)

The diagram displays the defined objects (5.10a), the finite codimension-\(n\) Koszul restriction and the actual projective holomorphic image (5.10b). The support statement is the proved inclusion (5.10c); the bottom line lists the additional output-symbol and dimension steps beyond Theorem 5.10. Theorems 5.11–5.12 supply those proofs; the actual output symbol is a subquotient of the candidate. The reproducible drawing source is original CC0 material. Every input is proved above or in the linked earlier programme lessons.


### Singular pieces and isotropic projective cotangent images

**Theorem 5.11.** Let \(D\) be a complex coordinate polydisc of dimension \(m\), let \(Z=\mathbf P^n\times D\), and let \(\Lambda\subset T^*Z\) be a closed reduced conic analytic set, pure of dimension \(d=n+m\), whose smooth locus is Lagrangian. Set
\[
\begin{aligned}
W&=Z\times_DT^*D,\\
j(z,\eta)&=(z,(dp_z)^t\eta),\\
q(z,\eta)&=\eta,\\
B&=q(j^{-1}\Lambda).
\end{aligned}
\tag{5.11a}
\]
Then \(B\) is a closed conic analytic subset of \(T^*D\). Every local irreducible component of \(B\) is generically isotropic, and
\[
\dim B\le m.
\tag{5.11b}
\]
The proof includes components of \(j^{-1}\Lambda\) lying wholly inside \(\Lambda_{\mathrm{sing}}\). It does not assume Whitney stratification, an analytic resolution theorem, RH, or regularity preservation.

Theorem 5.12 below constructs the actual output filtration and characteristic inclusion. The present theorem proves the cotangent dimension bound needed for that conclusion.



#### The admitted analytic foundations

The earlier programme proof of local parametrization provides the following precise data for an irreducible analytic germ \(A\) of dimension \(a\) in a coordinate ambient manifold. On a sufficiently small representative there is a proper finite projection
\[
\pi:A\longrightarrow V\subset\mathbf C^a
\tag{5.11c}
\]
and a nonzero holomorphic discriminant \(\delta\) on \(V\). Over \(V\setminus\{\delta=0\}\) it is a finite covering by regular points of \(A\), locally the graphs of holomorphic functions. This locus is dense. This is local parametrization, Theorem 4.1.

The same lesson proves finite local decomposition, Proposition 1.2, and dense regular points, dimension and strict dimension drop, Theorem 5.4 and Proposition 5.5. We use these statements locally, with countable coordinate covers.

The inverse, implicit and constant-rank theorems are the actual earlier coordinate proofs (HC9)–(HC12). The Riemann extension theorem, Theorem 4.2, and Corollary 4.3 prove bounded removal and connectedness of hypersurface complements. The coherent vanishing ideal is supplied by Cartan’s theorem, Theorem 1.1. These are exact earlier programme proofs.

Lemma 5.9.1 proves coherent projective holomorphic images. Theorem 5.10 gives the analytic-image unit argument, repeated below for the set in (5.11a).

#### The singular restriction lemma, proved by finite branches

**Lemma 5.11.1.** Let \(A\) be a reduced analytic subset of a complex manifold \(H\). Let \(\alpha\) be an ambient holomorphic differential form whose pullback to \(A_{\mathrm{reg}}\) is zero. For every locally closed analytic subset \(S\subset A\), its pullback to \(S_{\mathrm{reg}}\) is zero. This holds even when \(S\subset A_{\mathrm{sing}}\).

It is enough to prove the assertion locally for an irreducible component of \(S\) inside an irreducible component of \(A\). If \(A\) is locally reducible, its regular points away from the other components are dense in the regular locus of each component; holomorphic continuity therefore makes the hypothesis valid on each component's regular locus. Zero-dimensional \(S\) has no positive-degree forms and the degree-zero assertion is ordinary continuity. If \(\dim S=\dim A\), it is the same component locally and the assertion follows from the hypothesis. We now treat \(0<r=\dim S<a=\dim A\).

##### A finite projection restricts to an embedding generically on \(S\)

Take (5.11c) for an irreducible representative containing the chosen \(S\). The restriction to a regular source patch of \(S\) has maximum rank \(r\). Indeed, if its maximum rank were \(s<r\), a nonzero maximal minor gives a constant-rank neighbourhood. HC12 would supply local fibres of dimension \(r-s>0\), contradicting finiteness of \(\pi\). The rank-\(r\) patches are dense: the common vanishing of their minors is a proper analytic subset in each regular patch.

At such a point, HC12 identifies \(\pi|_S\), after shrinking, with a holomorphic embedding onto a smooth local submanifold \(S'\subset V\) of dimension \(r\). Flatten it in target coordinates \((s,v)\in\mathbf C^r\times\mathbf C^{a-r}\), so \(S'=(v=0)\). Here \(s\) is a parameter vector, not a source operator.

The inverse image \(\pi^{-1}S'\) is analytic. Every one of its irreducible components has dimension at most \(r\). To see this without a finite-image dimension theorem, take the regular locus of such a component of dimension \(k\); its map to the smooth \(r\)-manifold \(S'\) has maximum rank at most \(r\). Constant rank would give positive-dimensional fibres if \(k>r\), again contradicting finiteness. Thus \(k\le r\). Since our \(S\) has dimension \(r\), it is one irreducible component of this inverse image.

There are finitely many components near a given point. Remove their proper intersections with \(S\), and choose a point on the remaining open part of \(S\). In a neighbourhood of that point the underlying set of \(\pi^{-1}S'\) is exactly \(S\), and \(\pi|_S\) is an embedding. The other points of the finite fibre can be separated by disjoint ambient neighbourhoods. Properness shrinks the target so its entire inverse image lies in those neighbourhoods: otherwise a sequence outside them over base points tending to the chosen fibre would have a limit in that fibre. The distinguished neighbourhood consequently gives a proper finite restriction
\[
\pi:A_0\longrightarrow V_0,
\qquad
\pi^{-1}(s,0)=\{\sigma(s)\},
\tag{5.11d}
\]
set-theoretically, with \(\sigma:S'\to S\) the holomorphic inverse. Scheme multiplicities in this fibre are allowed. No normality, normalization or resolution is used.

The projection over the discriminant complement remains a finite covering. Every distinguished source part contains regular covering points by density. Since a hypersurface complement in a small connected polydisc is connected, that covering part has nonzero constant sheet number there.

##### A ramified transverse family has a bounded holomorphic lift

In the flattened coordinates expand the nonzero discriminant:
\[
\delta(s,v)=\sum_{\gamma\in\mathbf N^{a-r}}c_\gamma(s)v^\gamma.
\]
Let \(\ell\) be the least total degree with some coefficient not identically zero along a connected \(s\)-polydisc. Choose a constant vector \(b\in\mathbf C^{a-r}\) for which the polynomial
\[
c(s)=\sum_{|\gamma|=\ell}c_\gamma(s)b^\gamma
\]
is not identically zero. Such a vector exists because a nonzero finite polynomial cannot vanish for all constant vectors. At a generic \(s\)-point \(c(s)\ne0\). After a further shrink,
\[
\delta(s,tb)=t^\ell h(s,t),\qquad h(s,0)=c(s),\qquad h(s,t)\ne0.
\tag{5.11e}
\]
This is just normally convergent Taylor expansion and a finite leading coefficient; it assumes no Puiseux theorem with parameters. It also covers \(\ell=0\).

For \(t\ne0\), the map \((s,t)\mapsto(s,tb)\) avoids the discriminant. Pull back the finite covering in (5.11d) to the product of this \(s\)-polydisc and a punctured \(t\)-disc. Its monodromy is one finite permutation: the parameter polydisc contracts radially, and the punctured disc retracts to its circle. Path lifting through the local covering charts identifies sheets; continuation around one circle permutes the finite fibre. If the total covering degree is \(q_0\), the permutation has order dividing \(q_0!\).

Choose any positive integer \(e\) divisible by that order, for example \(e=q_0!\), and substitute \(t=u^e\). The resulting cover has trivial monodromy and a global holomorphic sheet
\[
F(s,u)\in A_0,\qquad
\pi F(s,u)=(s,b u^e),\qquad u\ne0.
\tag{5.11f}
\]
To spell out the elementary covering argument, continue one inverse chart along paths from a fixed base point. Two paths differ by loops homotopic to integral powers of the circle loop; the power substitution makes their sheet permutation the identity. Thus the continuation is independent of the path. On every covering chart it is a holomorphic inverse, so the resulting sheet is holomorphic. The radial contraction and angular circle homotopies also prove the required homotopy invariance by subdividing a homotopy square into finitely many covering charts.

Choose all parameter closures inside \(V_0\). Properness puts the sheet inside a compact subset of its ambient source chart, hence all its coordinates are uniformly bounded near \(u=0\). Bounded removal extends each coordinate holomorphically across \(u=0\). In elementary Laurent terms, each negative coefficient satisfies \(|c_{-k}(s)|\le M\rho^k\) on fixed smaller parameter compacts; radius independence and \(\rho\to0\) kill it. The coefficients are holomorphic in \(s\) by their circle integrals. This proves joint holomorphic extension, not merely pointwise limits.

The source equations remain zero by continuity, and properness keeps the limit in the distinguished neighbourhood. Equation (5.11d) forces
\[
F(s,0)=\sigma(s),\qquad
F(s,u)\in A_{\mathrm{reg}}\quad(u\ne0).
\tag{5.11g}
\]
This family is the required singular-stratum bridge.

##### Pull back the form and pass to \(u=0\)

The form \(F^*\alpha\) is holomorphic on the entire parameter product. It is zero for \(u\ne0\), because (5.11g) maps that open set into \(A_{\mathrm{reg}}\). Its holomorphic coefficients are therefore identically zero. Restricting to \(u=0\) gives \(\sigma^*\alpha=0\) on a nonempty open part of \(S_{\mathrm{reg}}\).

The construction can be restarted in every nonempty regular patch of \(S\). Each such patch therefore contains a nonempty open on which the restricted form vanishes. The zero set is dense in \(S_{\mathrm{reg}}\), and the restricted holomorphic coefficients are continuous, so they vanish everywhere. This proves Lemma 5.11.1. There is no assumption that tangent spaces at singular points are ordinary limits of tangent spaces; the actual holomorphic family supplies the needed restriction map. \(\square\)



#### The conic Lagrangian one-form vanishes on every singular piece

Fix the sign convention
\[
\theta_Z=\sum_{i=1}^n\xi_i\,dx_i+
         \sum_{a=1}^m\eta_a\,dy_a,
\qquad
\omega_Z=d\theta_Z,
\qquad
E=\sum_i\xi_i\partial_{\xi_i}+\sum_a\eta_a\partial_{\eta_a}.
\tag{5.11h}
\]
Thus \(\iota_E\omega_Z=\theta_Z\). Reversing the symplectic sign would leave the isotropy assertions unchanged, but (5.11h) states the sign actually used.

Conicity makes \(E\) tangent to \(\Lambda_{\mathrm{reg}}\): its fibre-scaling flow preserves \(\Lambda\) and the regular locus. Lagrangianity gives \(\omega_Z(E,v)=0\) for every tangent vector \(v\) there. Therefore
\[
\theta_Z|_{\Lambda_{\mathrm{reg}}}=0.
\tag{5.11i}
\]
Lemma 5.11.1 now makes the pullback of \(\theta_Z\) zero on the regular locus of **every** locally closed analytic subset of \(\Lambda\). In particular it is zero on every smooth local analytic piece of \(j^{-1}\Lambda\), after applying \(j\), including pieces entirely over \(\Lambda_{\mathrm{sing}}\).

In the correspondence (5.11a), \(j\) sets precisely the vertical covectors to zero. With
\(\theta_D=\sum_a\eta_a\,dy_a\), the actual coordinate identity is
\[
j^*\theta_Z=q^*\theta_D.
\tag{5.11j}
\]
It glues intrinsically because tautological cotangent one-forms are defined by evaluation on the derivative of the cotangent projection. Consequently \(q^*\theta_D\) vanishes on every smooth local analytic piece of \(j^{-1}\Lambda\).

#### The proper image is analytic, using the proved coherent theorem

Put \(A=j^{-1}\Lambda\) as a reduced analytic subset of \(W\). Its ideal is coherent by the exact Cartan coherence theorem. The proper projective map \(q:W\simeq\mathbf P^n\times T^*D\to T^*D\) has coherent \(q_*\mathcal O_A\) by the projective analytic coherent-image theorem already proved in Lemma 5.9.1.

Its support is exactly \(q(A)\). Outside that closed image it is zero. At \(b\in q(A)\), choose a point of the nonempty fibre in \(A\). The global unit of \(\mathcal O_A\) cannot have zero direct-image stalk at \(b\): that would mean zero on the inverse image of one neighbourhood, contradicting its nonzero source germ at the chosen point. Thus the coherent support is \(B=q(A)\), and support of a coherent analytic sheaf is analytic by a finite local presentation. This is the same unit argument independently checked in Theorem 5.10. Properness supplies closedness. Fibre scaling commutes with \(j\) and \(q\), so \(B\) is conic.

No general proper analytic-image theorem or analytic stratification theorem is used at this step.

#### A countable rank cover supplies image tangent vectors

We need a consequence of surjectivity onto \(B\), including when all sources over a component lie in singular loci. The following elementary argument avoids an assumed stratification.

##### Analytic sets admit the needed countable smooth covers

Every local irreducible analytic set of positive dimension \(k\) has, by (5.11c), a dense smooth open whose complement is contained in the proper analytic subset \(\{\delta\circ\pi=0\}\). The latter has dimension at most \(k-1\). Decompose that complement into its finitely many local irreducible components, apply the same construction to each, and continue. The dimension strictly drops, so after at most \(k\) levels the remaining pieces are zero-dimensional and smooth.

Using a countable ambient chart cover and countable relatively compact subcharts makes this a **countable cover** by smooth locally closed analytic pieces. Overlap is allowed. No Whitney condition, frontier condition or local finiteness of a stratification is claimed or needed. Every piece is locally an analytic subset of the original analytic set, so the tautological-form vanishing proved above applies to it.

For a holomorphic map on one such smooth piece, take its maximum differential rank on a coordinate patch. The locus of that rank is open and has constant rank locally. The remaining locus is cut out by the maximum-rank minors and is a proper analytic subset. Its local components have lower dimension. Apply the same smooth-cover and rank argument recursively. Zero-rank maps on connected patches are constant. This gives a countable cover by smooth pieces on which \(q\) has constant rank, locally in the normal form HC12. The recursion again terminates by strict dimension drop.

##### Surjectivity forces full-rank image pieces somewhere in every target ball

Choose a target open on which \(B\) itself is a smooth manifold of dimension \(r\), avoiding the other local components. Such opens are dense in each component by the proved local parametrization and component-dimension statements. Restrict the source to its inverse image. Its images cover this target open.

If all the constant-rank pieces above had rank smaller than \(r\), HC12 would place every local image inside a smooth target submanifold of smaller dimension. Exhaust each sufficiently small source rank chart by countably many compact subsets. Their images are compact, hence closed, and have empty interior in the \(r\)-dimensional target manifold because they lie in those smaller-dimensional submanifolds. They are consequently nowhere dense.

A small closed target coordinate ball cannot be covered by countably many such closed nowhere-dense sets. Here is the precise elementary Baire argument: inside the ball choose a smaller closed ball disjoint from the first set; inside its interior choose a closed ball disjoint from the second, of radius at most \(1/2\); continue with radii tending to zero. At each stage nowhere density allows the choice. Nested compact balls have a common point, obtained equivalently by the Cauchy limit of their centres. That point misses every listed set, a contradiction. Intersecting the compact image sets with the target ball keeps them closed and nowhere dense; its boundary has no relative interior and causes no exception.

Thus some piece has rank \(r\); HC12 makes its image contain a target open and its differential surjective there. Pullback of \(\theta_D\) is zero on that piece by (5.11j) and Lemma 5.11.1. Surjectivity of its differential makes \(\theta_D|_B=0\) on its image open.

In fact the form is zero throughout each smooth target component patch. If it were nonzero at one point, one coefficient in a local tangent frame would remain nonzero on a smaller open neighbourhood. On the inverse image of that neighbourhood no rank-\(r\) piece could exist, because such a piece would force that coefficient zero. The same Baire argument contradicts the covering. Therefore
\[
\theta_D|_{B_{\mathrm{smooth}}}=0
\tag{5.11k}
\]
on the dense smooth portions of every local component. A zero-dimensional component satisfies this automatically.

This is the explicit image-rank step; it does not silently discard source pieces in \(\Lambda_{\mathrm{sing}}\).

#### Isotropy and the dimension bound

Take the exterior derivative of (5.11k) on a smooth target component patch:
\[
\omega_D|_B=d(\theta_D|_B)=0,
\qquad \omega_D=d\theta_D.
\tag{5.11l}
\]
Its tangent space \(V\) is isotropic in the \(2m\)-dimensional symplectic tangent space of \(T^*D\). Nondegeneracy gives
\(\dim V+\dim V^\perp=2m\), while isotropy gives \(V\subset V^\perp\). Hence \(2\dim V\le2m\). Dimension of an analytic component is the dimension of its dense smooth locus, proving (5.11b). Empty images and dimension-zero cases are included.

The singular restriction lemma and the countable rank cover are the two necessary steps beyond the familiar smooth correspondence calculation. Both have been proved here from finite parametrization, bounded removal, constant rank and dimension drop. In particular no unresolved Whitney-stratification package is used as a hidden provider.

![The finite-branch singular bridge and exact cotangent one-form identity](assets/projective-isotropic-image-proof.png)

The upper panel is the local family of Lemma 5.11.1, with \(e\) a finite covering-monodromy exponent and \(b\) a chosen transverse parameter vector. It is a schematic, not an analytic resolution or a global parametrization. The middle panel is the actual correspondence (5.11a) with zero vertical covectors and the exact identity (5.11j). The bottom panel records (5.11k)–(5.11l) and the proved bound (5.11b), including source pieces wholly in the singular locus. The complete proof is above; the reproducible drawing source supplies the original CC0 diagram.


### Actual filtered images and analytic projective holonomicity

**Theorem 5.12.** Let \(p:Z=\mathbf P^n\times D\to D\), where \(D\) is a coordinate polydisc. Let \(M\) be a coherent analytic operator module with a global good order filtration near the compact fibre under consideration; an initial coherent global holomorphic generator suffices by Theorem 5.9. Every cohomology module of \(p_+M\) has an actual good output filtration, and
\[
\operatorname{Ch}\mathcal H^b(p_+M)\subset
q\bigl(j^{-1}\operatorname{Ch}M\bigr).
\]
If \(M\) is holonomic, every output cohomology module is holonomic. This conclusion includes every singular support and every derived degree. It extends to locally projective holomorphic maps of complex manifolds and bounded complexes whose cohomology modules have the stated generator or good filtration near the compact fibre. Right-module calculations transfer to the programme's left-module conventions by the density equivalence proved in Theorem 5.9.

The proof keeps the torsion in the derived Rees image until both specializations have been computed. Removing its locally bounded power torsion then constructs the good filtration of the actual output. Its symbol module is a quotient of a submodule of the coherent cotangent candidate of Theorem 5.10. Theorem 5.11 supplies the dimension bound, including singular intersections.

#### Objects, grading and the claimed characteristic containment

Work with right modules and let \(p:Z=\mathbf P^n\times D\to D\), \(d=\dim Z\), \(m=\dim D\). Let \(M\) be coherent over \(\mathcal D_Z\) with one globally defined good order filtration \(F\) near the tested compact fibre. The filtration is exhaustive, has coherent holomorphic pieces, is locally bounded below, and its graded module is locally finitely generated over \(\operatorname{Sym}T_Z\). A coherent global holomorphic generator supplies such a filtration by the construction in Theorem 5.9.

Use the central variable \(h\) of internal degree one and put
\[
\mathscr R_Z=\bigoplus_{a\ge0}\mathcal D_{Z,\le a}h^a,
\qquad\mathscr R_FM=\bigoplus_{a\in\mathbf Z}F_aM\,h^a.
\tag{5.12a}
\]
In coordinates write \(\vartheta_i=h\partial_i\). The relations are
\[
[\vartheta_i,a]=h\partial_i(a),\qquad
[\vartheta_i,\vartheta_j]=0,
\qquad h\text{ central},
\tag{5.12b}
\]
and both \(h,\vartheta_i\) have degree one. PBW gives the holomorphic coefficient basis \(h^k\vartheta^\alpha\), with \(k\ge0\). Consequently
\[
\mathscr R_Z/(h)=S_Z:=\operatorname{Sym}T_Z,
\qquad\mathscr R_Z/(h-1)=\mathcal D_Z.
\tag{5.12c}
\]
The Rees module embeds in \(M[h,h^{-1}]\). It is torsion-free, hence flat, over the coefficient PID \(\mathbf C[h]\). Here is the coefficient-flatness proof used throughout. Euclidean division by a nonzero ideal element of least degree proves that every ideal of \(\mathbf C[h]\) is principal. A finitely generated torsion-free module \(V\) over this PID injects into its finite-dimensional fraction-field span; choose a basis there and clear the finitely many generator denominators, embedding \(V\) into a finite free module. Every submodule \(N\subset A^r\) over a PID is free of rank at most \(r\): its first-coordinate image is a principal ideal \((a)\); if nonzero, choose a vector mapping to \(a\), subtract its multiples and split \(N\) as that free rank-one summand plus a submodule of \(A^{r-1}\). If the image is zero, it is already a submodule of the latter. Induction proves the assertion, including zero images. Thus the finitely generated \(V\) is free. An arbitrary torsion-free module is the filtered union of its finitely generated submodules, all free by this argument. Tensoring an exact sequence with each is exact, and a filtered union commutes with kernels and cokernels because every equality or preimage witness involves finitely many elements at one later index. Tensor with their union is therefore exact, proving flatness. The stalkwise argument proves sheaf coefficient-flatness. The Rees specializations are \(\operatorname{gr}_FM\) at zero and \(M\) at one, including negative filtration shifts.

Write
\[
\begin{aligned}
W&=Z\times_D T^*D,\\
j(z,\eta)&=(z,(dp_z)^t\eta),\\
q(z,\eta)&=\eta,\\
G&=\mathcal O_{T^*Z}\otimes_{S_Z}\operatorname{gr}_FM.
\end{aligned}
\tag{5.12d}
\]
The conclusion proved below is
\[
\operatorname{Ch}\mathcal H^b(p_+M)
\subset q\bigl(j^{-1}\operatorname{Supp}G\bigr)
\qquad\text{for every }b.
\tag{5.12e}
\]
These are analytic characteristic supports in the actual cotangent spaces. Theorem 5.10 proves that \(Rq_*Lj^*G\) is coherent and supported in the set on the right. The intervening Rees proof connects that object to the actual operator output by subquotients rather than an unsupported equality of symbols.

#### Graded analytic Rees coherence, with a finite termination argument

We need coherence for finite **graded** Rees presentations and degree-preserving maps. We do not assume a flat analytic infinite-order extension or import an unproved Rees coherence theorem.

At a holomorphic coefficient stalk \(H\), filter the Rees ring by the increasing vanishing order in the central variable \(h\), namely the decreasing filtration \(h^v\mathscr R\). Formula (5.12b) gives
\[
\operatorname{gr}_h\mathscr R=H[h,\xi_1,\ldots,\xi_d],
\tag{5.12f}
\]
a commutative Noetherian polynomial ring. Here this auxiliary filtration records the **least** power of \(h\), while the existing internal grading gives every \(h\) and \(\xi_i\) weight one. In a shifted finite free module, a homogeneous element of fixed internal degree has a finite upper bound on its possible \(h\)-order. Thus raising \(h\)-order at fixed internal degree terminates. This bound replaces any completeness or infinite-series assumption.

For a graded submodule \(I\) of a shifted finite free stalk module, its induced initial module is a bigraded submodule of (5.12f), hence has finitely many bigraded generators. Lift them to homogeneous \(g_i\in I\), retaining their initial \(h\)-orders. Match the first nonzero \(h\)-symbol of any homogeneous element by these lifts and subtract. The remainder has strictly higher \(h\)-order and the same internal degree. The preceding bound makes this process finite. It proves finite graded generation of \(I\) and strictness for this auxiliary filtration. It also proves the ascending-chain condition for graded submodules at every stalk.

The uniform neighbourhood statement follows by the same finite-identity argument as the earlier analytic operator Lemma 3.0c.4, with the auxiliary order now raised instead of lowered. Here are the details. For a degree-zero matrix \(\phi:A\to B\) between internally shifted finite free Rees modules with their usual coefficient \(h\)-order, choose at the point the lifts \(g_i\) of initial generators of its image. The replacement free module \(E\) must have **two explicit shifts**: its basis \(e_i\) has internal degree \(a_i=\deg(g_i)\) and auxiliary order \(v_i=\operatorname{ord}_h(g_i)\). Define
\[
F_h^vE=\bigoplus_i h^{\max(0,v-v_i)}\mathscr R\,e_i.
\]
Then \(\psi(e_i)=g_i\) is filtered for the auxiliary order and strict onto its induced image by the finite initial reduction. At fixed internal degree \(a\), every possible auxiliary order is at most \(\max_i(v_i+a-a_i)\); zero components with \(a<a_i\) are omitted. This gives the precise finite termination bound on the replacement module too. Its initial matrix is bigraded, with these two basis shifts. Internal shifts alone would be insufficient: multiplication by \(h\) would otherwise have a zero initial map. The finite reduction expresses the original columns through the \(g_i\), and every \(g_i\) already comes from a column combination. Therefore there are finite internally homogeneous matrices \(u:A\to E\), \(v:E\to A\) with
\[
\phi v=\psi,\qquad\psi u=\phi.
\tag{5.12g}
\]
Represent these finitely many identities on one neighbourhood. Choose finite bigraded generators \(\lambda_a\) of \(\ker\operatorname{gr}_h\psi\) at the point. Lift each to a vector of its internal degree and initial \(h\)-order. Its image under \(\psi\) has higher \(h\)-order. Auxiliary strictness expresses that image by a vector of the higher order; subtracting it gives an exact homogeneous relation \(r_a\) whose initial symbol is \(\lambda_a\).

The uniform homogeneous-polynomial-kernel argument, Lemma 3.0c.3, applies to the polynomial ring with \(d+1\) variables in (5.12f). Its proof does not depend on that number: extend the finite homogeneous matrix to the analytic variable space near the zero section; Oka makes its analytic kernel and the quotient by the chosen finite generators coherent. Relative analytic flatness identifies the kernel at the chosen stalk. A coherent quotient with zero stalk vanishes on a product neighbourhood. Faithful-flat contraction at each zero-section point and bounded-below graded zero-section detection then kill the polynomial quotient in every degree on one common neighbourhood. For clarity, the flatness input is the already proved Noetherian completion argument. Put \(A=H[u]_{(\mathfrak m,u)}\), \(B=\mathbf C\{y,u\}\). Their completed local rings agree over \(A\) as \(\widehat A=\widehat B=\mathbf C[[y,u]]\). Completion is faithfully flat on both rings by the exact earlier programme proof. Hence \(\widehat B\) is flat over \(A\), being its faithfully flat completion \(\widehat A\). If tensoring an injection with \(B\) had a nonzero kernel, faithful-flat tensoring with \(\widehat B\) would retain it, contradicting flatness over \(A\). Thus \(B\) is flat over \(A\); if a module tensoring with \(B\) is zero, tensoring with \(\widehat B=\widehat A\) is zero, and faithfulness of \(\widehat A\) makes that module zero. This proves faithful flatness directly. Graded detection follows from the finite graded module modulo \((u)\), Nakayama over \(H\), and induction on degree. This proves the needed uniform assertion for these \(d+1\) variables as well.

Represent the finitely many exact relations \(\psi(r_a)=0\) and their orders nearby. The same finite raising-order reduction now proves that the \(r_a\) generate \(\ker\psi\) on that neighbourhood and that \(\psi\) is auxiliary-strict onto its image. Its initial kernel and image are finite. Finally for \(z\in\ker\phi\),
\[
z=v\,u(z)+(1-vu)z;
\tag{5.12h}
\]
the first part is generated by the \(v(r_a)\), and the second by the finitely many columns of \(1-vu\). Both lie in \(\ker\phi\). This proves uniform graded Rees kernel and image coherence.

Finite presentation lifts and block matrices therefore prove that finite graded Rees modules form an abelian coherent category, closed under finite extensions. Every fixed internal-degree piece is holomorphically coherent: a graded finite presentation has finite holomorphic free pieces in that degree, and Oka applies. This is the exact graded coherence needed below. The proof uses finite polynomials throughout.

#### Strict induced twist segments from finitely many coherent order pieces

After shrinking the base, the global filtration is bounded below uniformly on the tested inverse image. Indeed a finite cover of the compact fibre supplies a common lower degree, and proper closedness shrinks the base into that cover. Likewise local good generation and a finite cover supply finitely many degrees \(a\) such that \(\operatorname{gr}_FM\) is generated by its pieces in those degrees on a smaller entire inverse image.

For each such degree apply delivered GL13 [Theorem 5.8](#relative-analytic-generation-in-every-projective-dimension) to the **coherent holomorphic sheaf** \(F_aM\). Only finitely many degrees and shrinkings are used. It supplies a finite twist bundle \(E_a\) and a map \(E_a\twoheadrightarrow F_aM\). Compose with the quotient to \(\operatorname{gr}_aM\), and induce the original map to right operators, assigning \(E_a\) filtration degree \(a\). The resulting map
\[
A_0=\bigoplus_a E_a\otimes\mathcal D_Z\twoheadrightarrow M
\tag{5.12i}
\]
is a **strict** filtered epimorphism. Its symbol map is onto; lift a symbol, subtract its image, and lower filtration degree. The uniform lower bound makes reduction finite in every germ. Generating the actual \(F_aM\) avoids any unproved global lifting of a chosen section of its quotient.

The kernel has the induced global good filtration by the exact earlier uniform filtered-submodule proof. Repeat the same finitely-many-degree construction for that kernel. For any fixed integer \(s\) we obtain, after only finitely many base shrinkings, a strict filtered exact segment
\[
0\to K\to A_s\to\cdots\to A_0\to M\to0,
\quad A_i=\bigoplus_a E_{i,a}\otimes\mathcal D_Z
\text{ with the stated degree shifts}.
\tag{5.12j}
\]
Each \(E_{i,a}\) is a finite sum of projective twists. Rees formation makes this an actual exact graded sequence; specialization at zero makes it an actual exact symbol sequence. Thus no filtration-strictness or \(h\)-torsion error has been hidden at the source augmentation.

#### Actual Rees transfer and its independent bounds

The forward Rees transfer is
\[
\mathscr T=
\mathcal O_Z[h]\otimes_{p^{-1}\mathcal O_D[h]}p^{-1}\mathscr R_D.
\tag{5.12k}
\]
Locally its source action is \(\vartheta_x=h\partial_x\) on coefficients in a vertical direction and \(\vartheta_y=h\partial_y+\vartheta_{D,y}\) in a horizontal direction. These formulas respect (5.12b), glue for the product projection and commute with the right target Rees action. It is free over \(\mathcal O_Z[h]\) in the target \(\vartheta_D\)-monomials. Define the actual graded derived image
\[
\mathcal C=Rp_*\bigl(\mathscr R_FM\otimes^L_{\mathscr R_Z}\mathscr T\bigr).
\tag{5.12l}
\]

The absolute Rees Spencer model has length \(d\). Its terms are
\(\mathscr R_Z\otimes_{\mathcal O_Z[h]}\bigl((\bigwedge^rT_Z)[h]\bigr)(-r)\otimes_{\mathcal O_Z[h]}\mathscr T\). Here \((\bigwedge^rT_Z)[h]=\mathcal O_Z[h]\otimes_{\mathcal O_Z}\bigwedge^rT_Z\) is explicitly extended over the polynomial coefficient ring, and the internal shift \((-r)\) puts its wedge generators in degree \(r\), with \(V(-r)_a=V_{a-r}\). Its cochain degree is \(-r\). The differential is the ordinary action-difference differential with \(\partial\) replaced by \(\vartheta\), and bracket terms multiplied by \(h\). Explicitly its action terms omit \(\xi_i\) with sign \((-1)^{i-1}\) and use \(P\vartheta_{\xi_i}\otimes u-P\otimes\vartheta_{\xi_i}u\); its bracket term for \(i<j\) is \((-1)^{i+j}hP\otimes[\xi_i,\xi_j]\wedge\xi_1\wedge\cdots\widehat\xi_i\cdots\widehat\xi_j\cdots\wedge\xi_r\otimes u\). The relations \([\vartheta_\xi,a]=h\xi(a)\) and \([\vartheta_\xi,\vartheta_\zeta]=h\vartheta_{[\xi,\zeta]}\) make it well defined over the holomorphic-polynomial coefficient ring; paired action-commutator terms and the Jacobi identity give \(d^2=0\). Every term is left Rees-flat, since the coefficient transfer is holomorphically-polynomial flat. Filter the first Rees factor by its \(\vartheta\)-order, shifting by wedge degree. The leading differential is Koszul on the independent first-factor symbol variables with a flat coefficient. Successive polynomial variables act injectively even with arbitrary coefficient modules; the two-term cone induction proves Koszul exactness. Lowering the finite first-factor order proves exactness of the augmented Spencer complex. Its differentials preserve the internal grading and right target action. Consequently Rees transfer has amplitude \([-d,0]\) on arbitrary input modules, independently of output coherence.

The all-sheaf real-manifold bound, (D8)–(D10) gives proper sheaf-image amplitude \([0,2d]\). This also applies in the graded Rees category. Indeed evaluation at any internal degree has the exact left adjoint given by the free graded Rees module generated in that degree, tensored over \(\mathbf C\). It therefore takes graded injectives to injective complex sheaves. A bounded-below graded injective resolution computes image degreewise. Its underlying sum has c-soft terms, since each component is injective and coproducts of c-soft sheaves are c-soft; proper image commutes with these sums by the compact-fibre coproduct proof, (C1)–(C4) and (F4). Thus its underlying complex computes the ordinary sheaf-derived image, retaining every homogeneous target action. This also justifies passage to the ungraded category when later specializing at \(h=1\).

For any Rees input module \(U\),
\[
Rp_*(U\otimes^L_{\mathscr R_Z}\mathscr T)
\in D^{[-d,2d]}.
\tag{5.12m}
\]
For an induced shifted twist term of (5.12j), transfer has no higher Tor because its Rees module is locally free over \(\mathscr R_Z\). Proper coefficient projection and the holomorphic PBW basis \(h^k\vartheta_D^\alpha\) give its actual image
\[
Rp_*E_{i,a}\otimes_{\mathcal O_D}\mathscr R_D
\quad\text{with its internal degree shift }a.
\tag{5.12n}
\]
Each cohomology is finite locally free graded Rees, by the proved parameter twist calculation. The comparison respects right derivatives and functions: the product rule is
\[
\vartheta^\alpha b=
\sum_{\beta\le\alpha}\binom\alpha\beta
h^{|\beta|}\partial^\beta(b)\vartheta^{\alpha-\beta}.
\tag{5.12o}
\]
Its coefficients pull back on the source and act by the same target scalars after image. Thus (5.12n) is Rees-operator linear, not merely an underlying sheaf identity.

Take (5.12j) with \(s=3d+2\), and let \(A=[A_s\to\cdots\to A_0]\). The strict Rees augmentation has cone \(\mathscr R K[s+1]\). By (5.12m) its pushed cone lies in
\[
[-d-s-1,2d-s-1]=[-4d-3,-d-3].
\tag{5.12p}
\]
Thus the finite induced image computes every possible degree of \(\mathcal C\); graded coherence and finitely many cones prove that all \(H^b\mathcal C\) are finite graded Rees modules. This does not use an infinite resolution or assume that the image is strict.

#### Both central specializations are actual derived comparisons

The two-term free coefficient resolutions of \(\mathbf C[h]/(h-c)\), for \(c=0,1\), express derived specialization as the cone of multiplication by \(h-c\). Derived image commutes with that finite cone. On the source use the bounded absolute Spencer model from the absolute Rees-Spencer argument above, tensoring it with \(\mathscr R_FM\). Every resulting term is a sum of copies of that coefficient-flat input, with finite tangent-bundle factors and target \(\vartheta_D\)-monomials, so it is flat over \(\mathbf C[h]\). Ordinary specialization of this bounded flat complex computes derived specialization. At one its differential and terms are the ordinary absolute Spencer transfer tensor with \(M\). At zero they are the symbol Koszul differential on the vertical variables and the differences between source horizontal and target symbol variables. The independent polynomial-variable induction proves that this is a flat symbol-transfer resolution; equivalently its relative vertical Koszul resolution has length \(n\). This supplies the natural identities
\[
\mathcal C\otimes^L_{\mathbf C[h]}\mathbf C_1\simeq p_+M,
\tag{5.12q}
\]
and
\[
\mathcal C_0:=\mathcal C\otimes^L_{\mathbf C[h]}\mathbf C_0
\simeq Rp_*\left(
\operatorname{gr}_FM\otimes^L_{S_Z}
(\mathcal O_Z\otimes_{p^{-1}\mathcal O_D}p^{-1}S_D)
\right).
\tag{5.12r}
\]
At zero the transfer symbol is the quotient by the vertical covector coordinates; its finite relative Koszul model has length \(n\). Both displayed identities preserve the full ordinary or symbol target action. At \(h=1\) internal grading is forgotten; at zero it is retained.

Since (5.12m) bounds \(\mathcal C\), its zero specialization has sufficient range \([-d-1,2d]\). Specializing the pushed cone (5.12p) at zero changes its lower bound by at most one and keeps its upper bound \(-d-3\). It follows that the finite induced segment computes every possible zero-specialization degree \(b\ge-d-1\) as well. This is the reason for using \(s=3d+2\) here. The earlier finite unfiltered proof's \(3d+1\) remains sufficient for its own unchanged assertion.

#### Analytic cotangent comparison, justified through that finite segment

Let \(\mathfrak a_D\) denote analytic extension from polynomial symbol modules to \(T^*D\): pull back along the cotangent projection and tensor over \(S_D\) with \(\mathcal O_{T^*D}\). It is exact. At every cotangent point, translate the polynomial variables by that point's constant coordinates; the local polynomial and analytic rings have the same completion, so the same exact-completion/flatness proof used in the graded Rees-coherence argument above applies. The analogous extension on \(Z\) identifies the symbol-transfer restriction with \(Lj^*G\).

The required natural comparison is
\[
\mathfrak a_D(\mathcal C_0)\xrightarrow{\sim}Rq_*Lj^*G.
\tag{5.12s}
\]
It must not be inferred from a general analytic coherent-image comparison. Its natural map is obtained by pulling an image section to the cotangent product and multiplying its polynomial coefficient by the new analytic coefficient; resolutions and the flat coefficient extension give its derived version. Equivalently the adjunction unit to the pulled-back image, followed by this coefficient multiplication and image adjunction, defines that map. These operations are functorial in the source complex. Its being an isomorphism follows here from the finite strict segment. For each induced symbol term \(\operatorname{gr}A_i=\bigoplus_a E_{i,a}\otimes S_Z\) with its shifts, derived vertical restriction is ordinary restriction, giving \(\bigoplus_a E_{i,a}\otimes p^{-1}S_D\). Its analytic extension is \(\bigoplus_a E_{i,a}\otimes\mathcal O_W\). The parameter twist computation, first on \(D\) and then on coordinate polydiscs in \(T^*D\), gives the specific coefficient comparison
\[
\mathfrak a_D(Rp_*E_{i,a}\otimes S_D)
\simeq Rq_*(E_{i,a}\otimes\mathcal O_W).
\tag{5.12t}
\]
The parameter Laurent proof, Lemma 6.5, identifies this particular natural base-coefficient map, and its estimates commute with parameter restrictions and target coefficient multiplication. Functoriality of the constructed map, rather than a claim that a chosen contraction commutes with every projective-coordinate operation, makes it commute with the polynomial-symbol differentials between induced terms. Finite totalization proves the comparison for the entire finite segment.

Its zero-specialized Rees cone lies below \(-d-2\), as just proved. On the analytic side its strict symbol cone is \(\operatorname{gr}K[s+1]\); derived vertical restriction has amplitude \([-n,0]\), and the already proved projective coherent analytic image theorem has amplitude \([0,n]\). Hence its analytic pushed cone lies in \([-n-s-1,n-s-1]\), whose upper endpoint is at most \(-d-3\), since \(s=3d+2\) and \(n\le d\). The actual analytic candidate lies in \([-n,n]\) by Theorem 5.10. The natural finite comparison therefore gives an isomorphism in every potentially nonzero degree on both sides. This proves (5.12s), with no unbounded limit, general Grauert theorem or arbitrary analytical base-change assumption.

#### Image torsion is retained, then removed to produce a good output filtration

Put \(H_b=H^b\mathcal C\), a finite graded Rees module. Multiplication by \(h-1\) is injective on any graded module viewed as an ordinary module: in a finite sum of homogeneous components, its lowest nonzero degree has coefficient minus that component and cannot cancel. Formula (5.12q) and its two-term specialization sequence therefore give
\[
\mathcal H^b(p_+M)=H_b/(h-1)H_b.
\tag{5.12u}
\]

Let \(T_b\) be the \(h\)-power torsion in \(H_b\). It is locally killed by one uniform power and is graded coherent. Here are the neighbourhood details. At a stalk the graded ascending-chain condition proved in the graded Rees-coherence argument above makes this union of kernels finite and killed by some \(h^N\). The sheaf kernel \(T_N=\ker(h^N:H_b\to H_b(N))\) is graded coherent. At that stalk the quotient by \(T_N\) has injective multiplication by \(h\). Its multiplication kernel is coherent and has zero stalk, so vanishes on a smaller neighbourhood. On that neighbourhood the quotient is \(h\)-torsion-free; hence every power-torsion element belongs already to \(T_N\), proving \(T_b=T_N\) there. No intersection of infinitely many opens occurs.

Set \(\overline H_b=H_b/T_b\). Torsion vanishes under specialization at one, so (5.12u) is also its specialization. Its homogeneous degree pieces embed into that ordinary module. Indeed if \((h-1)u=v_a\ne0\) is homogeneous, the lowest degree of the finite sum \(u\) must be \(a\), since its negative contributes that same lowest degree. Its highest degree is therefore at least \(a\); multiplying that component by \(h\) produces a nonzero component of degree greater than \(a\), contradicting the displayed equality. Here injectivity of \(h\) in the quotient is essential. Define \(F'_a\mathcal H^b(p_+M)\) as the image of \((\overline H_b)_a\). These pieces are increasing since multiplication by \(h\) identifies their classes at one. They exhaust the module because any finite sum of homogeneous representatives can be raised to a common degree. They are locally bounded below and coherent holomorphic, by finite graded presentation and finite-order PBW. Finite homogeneous Rees generation proves goodness. Moreover
\[
\mathscr R_{F'}\mathcal H^b(p_+M)=\overline H_b,
\qquad
\operatorname{gr}_{F'}\mathcal H^b(p_+M)=\overline H_b/h\overline H_b.
\tag{5.12v}
\]
Thus an actual good output filtration has been constructed; proper-image strictness was not assumed.

The two-term zero-specialization sequence gives an injection
\[
H_b/hH_b\hookrightarrow H^b\mathcal C_0;
\tag{5.12w}
\]
its cokernel is the \(h\)-kernel in \(H_{b+1}\), with the corresponding internal shift. The natural map from \(H_b/hH_b\) onto \(\overline H_b/h\overline H_b\) is surjective. Exact analytic extension, (5.12s), (5.12v) and (5.12w) therefore make the actual analytic output symbol sheaf a **quotient of a submodule** of \(H^b(Rq_*Lj^*G)\). Its support is contained in that candidate's support. Theorem 5.10 now gives (5.12e).

This proves the characteristic-transport inequality for the actual projective operator image, including every derived degree, singular source support, torsion in filtered image and the genuine target action. It does not declare the image Rees module torsion-free or identify the output symbols with the whole candidate.

#### Locally projective maps and holonomicity

The closed-embedding transfer of Theorem 5.9 preserves coherent generators. In adapted normal coordinates \(z_1,\ldots,z_c\), its actual normal-derivative expansion is \(\bigoplus_{\alpha\in\mathbf N^c}i_*M\,\partial_z^\alpha\). The filtration is
\[
F_a(i_+M)=\bigoplus_{\alpha\in\mathbf N^c}i_*F_{a-|\alpha|}M\,\partial_z^\alpha.
\]
Only finitely many terms occur in each degree because the source filtration is bounded below. Those pieces are coherent holomorphic by the closed-embedding argument in Theorem 5.9. Normal multiplication lowers derivative degree, while normal differentiation raises it. PBW therefore identifies the symbol module with the source symbol module tensored with the polynomial normal covectors, at zero normal position. This proves goodness and the full normal characteristic extension. Density conversion changes the presentation by an invertible line and preserves the reduced support. Factoring a locally projective map of complex manifolds through such an embedding and projection extends the argument with the supplied generator or good filtration. Finite Postnikov towers extend the module conclusions to bounded complexes with that cohomology hypothesis: kernels, quotients and extensions have characteristic supports contained in the relevant unions by the exact-sequence proof in the good-filtrations lesson.

The needed analytic Lagrangian input is obtained as follows, rather than importing an algebraic-variety-only dimension statement. The full Noetherian Gabber theorem, Theorem 7.0, applies to every filtered Noetherian ring with commutative Noetherian rational associated graded, explicitly without finite type over a field. The analytic operator stalk \(\mathcal D_{Z,z}\), with coefficient ring \(H=\mathcal O_{Z,z}\), satisfies these hypotheses by its analytic PBW/Noetherian proof; \(S=H[\xi]\), and a good filtration gives a finite symbol module. For right modules use the opposite filtered ring; its commutator Poisson bracket changes sign, which leaves ideal bracket closure unchanged. Thus \(J=\sqrt{\operatorname{ann}_S\operatorname{gr}M}\) is homogeneous and involutive. This is an application of the full Noetherian theorem, not its algebraic geometric corollary.

The passage to the actual analytic cotangent ideal uses Theorem 3.0c and Lemmas 3.0c.1–3.0c.2, with the following argument repeated for this arbitrary module. At a zero covector, faithful-flat relative analytification and homogeneous reduction make \(J\mathcal O_{T^*Z}\) radical. Concretely its cotangent-variable completion is the product of the graded pieces of the reduced homogeneous quotient \(S/J\); the first nonzero homogeneous term of a hypothetical nilpotent has a nonzero power in that reduced quotient. The completion is therefore reduced, and faithful-flat Noetherian completion contracts reducedness. Flatness and finite generators identify the analytified symbol support with this ideal's zero set. Finite homogeneous generators of \(J\), their bracket relations and the analytic Leibniz rule give \(\{J\mathcal O,J\mathcal O\}\subset J\mathcal O\). The analytic Nullstellensatz and Cartan coherence extend these finite identities to a neighbourhood of the zero covector. Conic scaling transports the assertion to every covector, preserving the symplectic form up to a nonzero scalar.

At a smooth point of any analytic irreducible characteristic component, avoid the other components and use its holomorphic graph coordinates. Its ideal differentials span the conormal space; bracket closure says this conormal is isotropic for the inverse symplectic form. Thus the tangent space is coisotropic and the component has dimension at least \(d\), by the elementary inequality \(\dim V+\dim V^\perp=2d\). This proves the analytic componentwise Bernstein bound for every nonzero coherent input without an algebraic-only comparison. For holonomic \(M\), the defining upper bound \(\dim\operatorname{Ch}M\le d\) makes every component dimension exactly \(d\); equality in coisotropy makes its smooth tangent spaces Lagrangian. The reduced analytic characteristic support is therefore pure conic Lagrangian, including arbitrary singular support. The dense analytic smooth-locus and dimension statements here are the exact earlier local-parametrization and dimension proofs linked in Theorem 5.11.

For this holonomic source, Theorem 5.11 proves
\[
\dim q(j^{-1}\operatorname{Ch}M)\le m,
\tag{5.12x}
\]
Together with (5.12e), this proves every actual cohomology image holonomic. The same analytic componentwise bound just proved applies to a nonzero coherent target module, so the upper bound gives the required dimension; the zero module is included.

Theorem 5.11 proves (5.12x), including components of the restricted characteristic set contained wholly in singular characteristic strata. Its finite-branch restriction lemma and countable constant-rank proof provide the required dimension bound.

The initial coherent global generator for every analytic regular holonomic module, regularity of the image and arbitrary proper maps, including nonprojective and support-proper maps, retain their separate proof obligations.

![The two actual central specializations and the subquotient producing the output characteristic support](assets/projective-filtered-characteristic-proof.png)

The upper comparisons are (5.12q) and (5.12s). The lower injection is (5.12w), and its quotient is the actual good output symbol module constructed in (5.12v), after removing locally uniform power torsion. The displayed analytic extension \(\mathfrak a_D\) is exact. This records a subquotient, rather than equality of the candidate and actual output symbols. The new strict segment uses \(s=3d+2\) and the cone bound (5.12p); the earlier unfiltered \(s=3d+1\) provider remains unchanged. The reproducible drawing source supplies the original CC0 diagram.


### Algebraic SNC boundary factors and every curve pullback

**Theorem 5.13.** Let \(P\) be smooth proper, let \(D_P\) be a reduced SNC divisor with smooth components, and let \(E\) be any finite-rank curve-regular connection on \(P\setminus D_P\). Its normalized algebraic logarithmic extension \(\bar E\) satisfies: \(\bar E(*D_P)\) is algebraic regular holonomic, every boundary simple factor is regular, and the same holds on every algebraic open \(Y\subset P\). For every algebraic map \(k:C\to Y\) from a smooth algebraic curve, the derived inverse image of this meromorphic module is regular holonomic. Arbitrary rank, Jordan blocks, tangency multiplicities, constant curves and curves lying in a boundary intersection are included.

We prove regularity in the algebraic composition-factor sense, including infinity. The proof extracts a coherent logarithmic lattice on each possible support with its intrinsic conormal determinant, then uses the already proved connection divisorial criterion. The inverse image calculation is explicit; it does not assume the general singular curve criterion.

All varieties below are smooth separated finite-type complex algebraic varieties. We use left differential-operator modules, the order filtration, and the programme convention
\[
f^!K=Lf_{\mathcal O}^*K[\dim X-\dim Y]
\quad(f:X\longrightarrow Y).
\tag{5.13a}
\]
Regularity of a connection means regularity on every smooth algebraic curve, at every point of the curve's smooth complete model, including infinity. Regular holonomicity means that every simple factor is an affine minimal extension of an irreducible curve-regular connection. These are the definitions fixed at the beginning of this section.

The exact earlier proofs are Theorem 5.1, Proposition 5.2.2, Lemma 5.2.3, Theorem 5.2, Lemma 1.0 and Theorem 1.1 of this lesson; PBW, Theorems 3.2 and 4.1; characteristic subquotients, Theorem 4.1, and the zero-section criterion, Proposition 6.1; finite connections, Theorem 3.1; Kashiwara’s equivalence and determinant inverse, Theorem 3.1; generic connections and finite length, Theorems 2.1–2.2; and localization, Proposition 1.1, minimal-extension uniqueness, Theorem 4.1, and simple-factor classification, Theorem 5.1. No general four-map or singular curve-test statement is used.

Free human source: Bernstein, [*Algebraic theory of D-modules*](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), printed pp. 31–33, especially the first step of the proof of Main Theorem B. The complete algebraic boundary-factor argument is supplied below. No Riemann–Hilbert statement or regularity-preservation theorem is an input.

#### Three elementary permanence facts

**Lemma 5.13.1.**

1. Regular holonomic modules form a Serre subcategory, and bounded complexes with regular holonomic cohomology form a triangulated subcategory.
2. Restriction to an arbitrary algebraic open preserves regular holonomicity.
3. If \(i:Z\hookrightarrow X\) is a smooth closed embedding, Kashiwara's exact equivalence restricts to an equivalence between regular holonomic modules on \(Z\) and regular holonomic modules on \(X\) supported on \(Z\). The same assertion holds for bounded complexes with supported cohomology.

**Proof.** For (1), intersect a composition series with a submodule. Each resulting successive quotient is zero or the corresponding simple factor. Quotient filtrations give the same assertion for quotients. Concatenating a composition series of a submodule with the inverse images of one in the quotient proves the extension assertion. A long cohomology sequence is assembled from kernels, images, cokernels and extensions, so proves the assertion about triangles.

For (2), consider a simple regular module \(S=j_{!*}E\), with \(j:U\hookrightarrow X\) affine and \(E\) irreducible and curve regular. On an open \(V\subset X\), its restriction is zero or the minimal extension from \(U\cap V\): restrict the canonical map defining the minimal extension, or apply its no-boundary uniqueness theorem. Restriction is exact and commutes with the transfers and the boundary map, so it commutes with its degree-zero image. The inclusion \(U\cap V\hookrightarrow V\) is the base change of \(j\), hence affine. If it is nonempty, the connection \(E|_{U\cap V}\) remains irreducible: a proper connection subobject there extends by the graph-closure Lemma 5.2.3, or its minimal extension gives a proper submodule of \(S\). It remains curve regular, because a curve mapping to this open also maps to \(U\). Thus the restriction is simple regular. Apply restriction to a composition series.

For (3), the exact closed direct image takes simple objects to simple objects. If \(S=j_{!*}E\) on \(Z\), its image is \((ij)_{!*}E\). Indeed, both restriction to \(U\) and boundary-supported subobjects and quotients are identified by the supported equivalence; minimal-extension uniqueness gives the asserted identification. The composite of two affine maps is affine. Conversely, if a simple \(i_*S\) has a regular presentation \(j_{!*}E\) on \(X\), the closure of the presenting stratum is its support, which lies in \(Z\). The stratum and its reduced locally closed immersion therefore factor through \(Z\). Its immersion into \(Z\) is the base change of the immersion into \(X\), hence affine. Kashiwara's inverse and the same uniqueness argument give a regular presentation of \(S\). Exactness transports composition series in both directions. On supported bounded complexes, the earlier Kashiwara derived equivalence is exact on each cohomology module; applying the module assertion in each degree proves (3). \(\square\)

The inverse assertion in (3) applies only to a complex already supported on \(Z\). It makes no assertion here about \(i^!K\) for a general regular complex on \(X\).

#### Algebraic finite logarithmic hulls

Let \(P\) be smooth proper, let \(D=\bigcup_{a=1}^sD_a\) be a reduced SNC divisor with globally smooth components, and put \(U=P\setminus D\). Let \(E\) be a curve-regular connection on \(U\), of any finite rank. Theorem 5.1 gives its normalized algebraic logarithmic extension \(\bar E\) on \(P\). Put
\[
M=\bar E(*D)=\bigcup_{m\geq0}\bar E(mD).
\tag{5.13b}
\]
Write \(\mathscr L_P\) for the algebra generated by \(\mathcal O_P\) and the vector fields preserving the ideals of all the components \(D_a\). In an adapted étale coordinate chart it is generated by
\[
z_1\partial_{z_1},\ldots,z_k\partial_{z_k},
\partial_{w_1},\ldots,\partial_{w_{n-k}}.
\tag{5.13c}
\]
Every \(\bar E(mD)\) is finite over \(\mathcal O_P\) and stable under \(\mathscr L_P\). This follows directly from the logarithmic Leibniz rule: acting on \((z_1\cdots z_k)^{-m}\) adds the integral residue shift \(-m\) in each normal direction and does not increase its pole order.

**Lemma 5.13.2 (subquotient hulls).** Every differential-operator subquotient \(F=A/B\) of \(M\) is a union of \(\mathcal O_P\)-coherent \(\mathscr L_P\)-stable subsheaves.

**Proof.** Define
\[
L_m=\operatorname{im}\bigl(A\cap\bar E(mD)\longrightarrow A/B\bigr).
\tag{5.13d}
\]
The intersection is coherent over \(\mathcal O_P\), since on an affine chart it is a submodule of a finite module over a Noetherian ring. Intersections and images commute with localization, so these modules define the stated coherent subsheaves. Both \(A\) and \(\bar E(mD)\) are stable under \(\mathscr L_P\); hence so are their intersection and its image. Every local section of \(A\) has a locally finite pole order in (5.13b), so belongs locally to one of the intersections. Thus \(\bigcup_m L_m=F\). \(\square\)

#### The possible supports of boundary factors

**Lemma 5.13.3.** The characteristic support of \(M\), and of each of its differential-operator subquotients, lies in the union of the conormals to the SNC intersections. Every nonzero simple factor of \(M\) has support equal to one connected component \(Z\) of an intersection \(D_I=\bigcap_{i\in I}D_i\), with \(I=\varnothing\) allowed. On
\[
S_I=Z\setminus\bigcup_{j\notin I}(D_j\cap Z),
\tag{5.13e}
\]
its Kashiwara inverse is a nonsingular finite-rank connection.

**Proof.** We give an algebraic order-filtration argument; an analytic constant-residue gauge is unnecessary. The finite lattice \(F_0M=\bar E(D)\) generates \(M\) as a differential-operator module. To see this, choose a logarithmic frame as a row \(e\) on an adapted étale chart, and write its normal logarithmic matrices as \(A_i\), so that \(z_i\nabla_{\partial_{z_i}}e=eA_i\). For a constant coefficient column \(v\) and \(a_i\geq1\),
\[
\partial_{z_i}(z^{-a}ev)
=z^{-(a+\mathbf e_i)}e(A_i-a_iI)v.
\tag{5.13f}
\]
At \(z_i=0\) the matrix on the right is invertible: all residue eigenvalues have real parts in \([0,1)\), whereas \(a_i\) is a positive integer. Its inverse exists in the algebraic local ring. Away from \(z_i=0\), multiplication by \(z_i^{-1}\) itself is allowed. Starting with \(a=(1,\ldots,1)\), these local statements inductively generate each lattice with any prescribed finite pole orders, and hence (5.13b). This is a sheaf-local argument for each finite multi-index; it does not assert that one algebraic affine neighborhood inverts infinitely many determinants simultaneously.

Set \(F_pM=\mathcal D_{P,\leq p}F_0M\) for \(p\geq0\), with zero negative terms. Each term is coherent over \(\mathcal O_P\); locally it is the image of a finite operator module tensored with a finite lattice, inside the finite lattice \(\bar E((p+1)D)\). PBW and (5.13f) show exhaustivity and that this is a good generated filtration.

Each operator in (5.13c) preserves \(F_0M\). Commuting it past a normally ordered derivative monomial of order \(p\) leaves an operator of order at most \(p\): specifically,
\[
[z_i\partial_{z_i},\partial_z^a\partial_w^b]
=-a_i\partial_z^a\partial_w^b,
\qquad
[\partial_{w_j},\partial_z^a\partial_w^b]=0,
\tag{5.13g}
\]
and differentiation of a coefficient does not increase its order. These operators therefore preserve every \(F_pM\). Their first-order symbols consequently annihilate \(\operatorname{gr}_F M\), because their actions into \(F_{p+1}/F_p\) are zero. In cotangent coordinates this gives
\[
\operatorname{Ch}(M)\subset
V(z_1\xi_1,\ldots,z_k\xi_k,\eta_1,\ldots,\eta_{n-k})
=\bigcup_{J\subset\{1,\ldots,k\}}T^*_{D_J}P.
\tag{5.13h}
\]
The last equality is set-theoretic: at each point, choose the indices for which the normal coordinate is zero; for every remaining index its covector coefficient must vanish. Each displayed component has dimension \(n\). Localization holonomicity and the standard strict induced good filtrations give the same characteristic-support inclusion for every subquotient. In detail, the induced graded submodule and quotient are finite over the Noetherian graded operator ring, so are good after finitely many degree shifts; the exact graded sequence proves the inclusion.

Let \(F\) be a nonzero simple factor, with irreducible support \(W\). At a general point of \(W\), exactly one SNC stratum \(S_I\) contains that point. The earlier simple-factor classification and Kashiwara calculation give the conormal of the smooth general part of \(W\) as a characteristic component of dimension \(n\). Formula (5.13h) restricts its normal fiber to the span of the \(|I|\) normals of the stratum. Hence
\[
n\leq\dim W+|I|\leq\dim Z+|I|=n.
\tag{5.13i}
\]
Thus \(\dim W=\dim Z\), and the closed irreducible support is the entire component \(Z\) of \(D_I\). This dimension argument is applied at a general point of \(W\); it does not infer a support from a nongeneric characteristic fiber.

On \(S_I\), the only cotangent directions allowed by (5.13h) are the normals to \(Z\). Kashiwara's inverse therefore has characteristic variety contained in its zero section. Such a coherent differential-operator module is \(\mathcal O\)-coherent: in a finite good graded presentation, the ideal generated by the positive-degree vector symbols has a power annihilating the graded module, so only finitely many symbol monomials are needed as structure-sheaf generators. Lifting those finitely many graded generators gives structure-sheaf generators of the original module by induction down its filtration. The earlier coherent-connection theorem makes it a finite-rank nonsingular connection. \(\square\)

In (5.13e), each \(Z\) is smooth and proper, and its remaining boundary is SNC. Empty intersections contribute nothing. The empty subset contributes the open stratum \(U\).

#### Extracting a logarithmic lattice with the correct determinant

**Lemma 5.13.4 (normal extraction).** Let \(F\) be a simple factor of \(M\), supported on the component \(Z\) from Lemma 5.13.3, and let \(Q\) be its Kashiwara inverse on \(Z\). Then the connection \(H=Q|_{S_I}\) is curve regular, including infinity.

**Proof.** Let \(\mathcal I\) be the ideal of \(Z\). The intrinsic Kashiwara inverse has underlying structure-sheaf module
\[
Q=\det(\mathcal I/\mathcal I^2)\otimes
\operatorname{ann}_{\mathcal I}F.
\tag{5.13j}
\]
The determinant factor cannot be dropped. Apply Lemma 5.13.2 and put
\[
\begin{aligned}
A_m&=\operatorname{ann}_{\mathcal I}L_m,\\
Q_m&=\det(\mathcal I/\mathcal I^2)\otimes A_m.
\end{aligned}
\tag{5.13k}
\]
The annihilator of the finitely generated ideal in a coherent module is coherent, so each \(Q_m\) is finite over \(\mathcal O_Z\); and \(\bigcup_mQ_m=Q\).

We check its logarithmic stability, including the twist. Work in the adapted coordinates \(Z=(z_1=\cdots=z_k=0)\), and write
\(\nu=[z_1]\wedge\cdots\wedge[z_k]\) for a frame of the determinant in (5.13j). A logarithmic vector field \(\xi\) on \(Z\), along its remaining SNC boundary, has a local lift \(\widetilde\xi\) to a logarithmic vector field on \(P\) preserving each selected normal divisor. Write \(\widetilde\xi z_i=a_i z_i\). The induced action is
\[
\begin{aligned}
\nabla^Q_\xi(\nu\otimes v)
&=\nu\otimes\left(\widetilde\xi v+\sum_{i=1}^k a_i v\right),\\
&\qquad v\in\operatorname{ann}_{\mathcal I}F.
\end{aligned}
\tag{5.13l}
\]
Indeed the lift acts on the conormal determinant by \(\sum_i a_i\). It preserves \(\operatorname{ann}_{\mathcal I}F\), since
\(z_i\widetilde\xi v=\widetilde\xi(z_iv)-a_iz_iv=0\).

The formula is independent of the lift. In a difference of two lifts, the terms with nonzero restriction in normal derivative directions are \(\sum_i z_i b_i\partial_{z_i}\). On an annihilated vector,
\[
z_i\partial_{z_i}v=-v,
\tag{5.13m}
\]
by \([\partial_{z_i},z_i]=1\); this contributes \(-\sum_i b_i v\), canceled by the determinant contribution \(+\sum_i b_iv\). Terms with coefficients in \(\mathcal I\) in the tangential directions act by zero on an annihilated vector. Thus (5.13l) is precisely the earlier intrinsic supported inverse. A lift preserving all divisors exists locally by lifting its coefficient functions in the adapted étale chart; these are exactly the logarithmic generators (5.13c). Coordinate changes give the conormal determinant transition and the Leibniz transformation, so the calculation glues.

Since \(L_m\) is stable under every such lift, (5.13l) preserves \(Q_m\). Put
\[
B_Z=\bigcup_{j\notin I}(D_j\cap Z).
\]
The complement immersion \(h:S_I\hookrightarrow Z\) is affine: locally its boundary is a single nonzero divisor equation, so its complement is a principal affine open; affineness of a morphism is local on its target. Underlying localization gives
\[
Q(*B_Z)=h_*H.
\tag{5.13n}
\]
This is torsion free as an \(\mathcal O_Z\)-module, since a section of a vector bundle on a dense open of the integral smooth \(Z\) cannot be killed by a nonzero regular function. The images
\[
\widetilde Q_m=
\operatorname{im}(Q_m\longrightarrow Q(*B_Z))
\tag{5.13o}
\]
are coherent torsion-free logarithmically stable modules. Their union has generic fiber \(H_{\mathbf C(Z)}\). Choose finitely many vectors spanning that fiber and then one index \(m\) containing all of them; the hull \(\widetilde Q_m\) has full generic rank.

At the generic point of any component of \(B_Z\), its stalk is a finite torsion-free module of full rank over the transverse DVR. It is therefore a full lattice, by Lemma 1.0. The generator \(t\partial_t\) of the logarithmic normal field preserves it, by (5.13l). It supplies a regular singular lattice for the transverse differential module. This proves regularity at every boundary divisor of the smooth proper SNC compactification \(Z\) of \(S_I\).

Apply the already proved connection divisorial criterion, Theorem 5.1, to the nonsingular algebraic connection \(H\) on \(S_I\). It makes \(H\) regular on every algebraic curve and at every completion point. In particular it tests curves lying in deeper boundary intersections after their own compactification; these are included by that earlier theorem, rather than omitted in the transverse DVR argument. \(\square\)

For \(I=\varnothing\), (5.13j) has no determinant twist, and the proof is the same. For a zero-dimensional \(Z\), there are no boundary divisors and the connection is a finite-dimensional vector space; the zero-rank case uses the zero lattice. No diagonalization, splitting of residue eigenspaces, or semisimplicity assumption is used in (5.13j)–(5.13o).

#### The full algebraic SNC extension theorem

**Conclusion of Theorem 5.13.** Let \((P,D_P)\) be any smooth proper SNC pair, let \(E\) be any finite-rank curve-regular connection on \(U=P\setminus D_P\), and let \(\bar E\) be its normalized algebraic logarithmic extension. Then \(\bar E(*D_P)\) is algebraic regular holonomic. The same conclusion holds on every algebraic open \(Y\subset P\) for the affine open direct image from \(V=Y\cap U\), with \(D=D_P\cap Y\):
\[
j_*E=E(*D),\qquad j:V\hookrightarrow Y,
\tag{5.13p}
\]
is an algebraic regular holonomic module. All its boundary simple factors, including factors on arbitrary nonempty SNC intersections, are regular. Every connection factor and every point factor is retained.

**Proof for the proper pair.** A simple factor \(F\) of \(M\) has the support and nonsingular connection \(H\) of Lemma 5.13.3. The connection is regular by Lemma 5.13.4. Its restriction to \(S_I\) is irreducible: the earlier simple-factor classification makes the restriction to some dense open irreducible; a connection subobject on \(S_I\) would restrict to one there, and a nonzero connection or quotient has positive generic rank. Thus it is either zero or the entire connection. Simplicity of \(F\) gives no nonzero submodule or quotient supported on the omitted boundary. Minimal-extension uniqueness gives
\[
F\simeq (S_I\hookrightarrow P)_{!*}H.
\tag{5.13q}
\]
The presenting immersion is affine: it is the composite of the affine complement immersion \(S_I\hookrightarrow Z\) and the closed immersion \(Z\hookrightarrow P\). Thus (5.13q) is exactly a regular presentation under the course definition. Every simple factor has this property, so \(M\) is regular holonomic. This proof establishes algebraic regularity, including infinity, rather than merely the analytic filtration condition of Theorem 5.3.

**Restriction to an arbitrary open of this pair.** The restriction of \(\bar E(*D_P)\) to \(Y\) is exactly \(j_*(E|_V)\): its local boundary equation is the restriction of that of \(D_P\), and localization sheafifies the given connection on its complement. Lemma 5.13.1(2) proves that the restriction is regular holonomic. The localization is concentrated in degree zero because \(j\) is affine and its transfer is localization. \(\square\)

The starting data are a proper SNC pair and its open restrictions. Theorem 5.1 supplies such proper SNC compactifications for regular connections. No stronger assertion about preserving a pre-existing SNC divisor during compactification is used.

#### Every algebraic curve map tests an SNC meromorphic extension

**Corollary 5.13.5.** For \(M=j_*(E|_V)\) on \(Y\) as in Theorem 5.13 and every algebraic map \(k:C\to Y\) from a smooth algebraic curve, the bounded holonomic complex \(k^!M\) is regular. This includes \(Y=P\). The map need not be an immersion, noncharacteristic, dominant onto its image, or transverse to \(D\).

**Proof.** Work on a connected component of \(C\), which is integral, and on a connected component of \(Y\). Locally \(M\) is a finite locally free logarithmic lattice tensored with \(\mathcal O_Y[1/q]\), where \(q\) is a local equation for \(D\); hence it is flat over \(\mathcal O_Y\). This flatness is intrinsic, since localizations are flat and the lattice is locally free. Consequently the transfer formula (5.13a) has no higher structure-sheaf Tor terms:
\[
k^!M\simeq
k_{\mathcal O}^*M[1-\dim Y].
\tag{5.13r}
\]
If \(k(C)\subset D\), the inverse image is zero. At each point, some boundary equation pulled back to the integral curve is identically zero; the localization tensor inverts that zero and is the zero module. This covers constant maps into the boundary and maps lying in any deeper SNC intersection.

Otherwise \(T=k^{-1}D\) is finite, and \(W=C\setminus T\) is dense. On \(W\), (5.13r) is the usual flat-bundle pullback \((k|_W)^*E\). It is curve regular, including infinity, because every curve mapping to \(W\) composes with \(k|_W\) to a curve mapping to \(V\). In particular its own identity map supplies the logarithmic lattice at every point of the complete model of \(W\). Across \(T\), (5.13r) is its meromorphic localization; its operator action is the chain-rule pullback connection. This follows in a local logarithmic frame from
\[
k^*(A_i\,d\log z_i)=
k^*A_i\left(m_i\,\frac{dt}{t}+\frac{du_i}{u_i}\right)
\quad\text{if }k^*z_i=t^{m_i}u_i,
\tag{5.13s}
\]
where \(m_i\geq0\) and \(u_i\) is a unit. Thus all tangency multiplicities, residues and nilpotent parts are retained.

For clarity, a holonomic module on a smooth curve with a regular generic connection is regular holonomic under the composition-factor definition. Its point-supported simple factors are the point delta modules, regular presentations from points. Every full-support simple factor restricts to a subquotient of the generic connection on a common dense open; this is a regular connection by Proposition 5.2.2. Its presenting open is affine (the complement is a finite divisor), and minimal-extension uniqueness gives its regular presentation. There are no other supports on a curve. This proves regularity of the meromorphic localization in (5.13r). The fixed dimension shift preserves regularity, and the zero case was included. \(\square\)

The logarithmic frame used for the flatness calculation exists on \(Y\) by the proper-pair construction of Theorem 5.13; equivalently it is the restriction of the normalized lattice on \(P\). At infinity of \(C\), regularity is supplied by the intrinsic regularity of \((k|_W)^*E\), even when \(k\) does not extend as a map to \(Y\). Equation (5.13s) is a local check at points of \(C\), and is not substituted for that infinity assertion.

![Normal extraction and the transverse lattice](assets/snc-boundary-extraction.png)

*Figure. The upper route is the actual subquotient-hull construction (5.13d). The middle row shows the sign cancellation (5.13l)–(5.13m) that makes the intrinsic supported inverse independent of a normal lift. The lower row is the full-rank DVR lattice (5.13o), followed by the previously proved connection divisorial criterion. The figure records a proof mechanism, not a splitting of the subquotient or a decomposition of the logarithmic connection. The reproducible drawing source supplies the original CC0 figure.*


### Arbitrary inverse transfer and singular supported graph base change

Dimension shifts are taken componentwise. A smooth finite-type variety has finitely many disjoint open-and-closed smooth integral components, each of pure dimension. A connected source maps into one target component. Finite component sums extend all statements below to varieties whose component dimensions differ, without assigning a single incorrect global dimension.

Theorem 5.13 is used with its proved scope: every proper smooth SNC pair, every boundary simple factor of its meromorphic extension and every open restriction of that pair.

The exact earlier proofs are inverse transfer and composition, Proposition 1.1 and Theorem 2.1; supported localization, product base change and absolute Spencer transfer, Lemmas 1.1 and 3.3 and Theorem 2.1; and the PBW, Kashiwara and holonomic proofs linked in Theorem 5.13. The finite Čech argument below extends direct composition to every smooth separated finite-type variety. Theorem 5.6 supplies full generic Gauss–Manin regularity.

#### The inverse transfer for every map

Let \((P,D)\) be any smooth proper SNC pair over \(\mathbb C\), let \(E\) be any finite-rank curve-regular connection on \(U=P\setminus D\), and let \(\bar E\) be its normalized logarithmic extension. Put \(M=\bar E(*D)\). Let \(f:Y\to P\) be **any** map from a smooth separated finite-type variety. Work componentwise, so \(P\) and \(Y\) have pure dimensions \(n\) and \(d\).

**Theorem 5.14.1.** On each connected component of \(Y\) whose image lies in \(D\), \(f^!M=0\). On every other component, \(B=f^*D\) is an effective Cartier divisor, allowed to have arbitrary multiplicities and singular reduced support, and
\[
\begin{gathered}
f^!M\simeq N_f[d-n],\\
N_f=(f^*\bar E)(*B).
\end{gathered}
\tag{5.14a}
\]
The only possible nonzero cohomology is \(H^{n-d}(f^!M)=N_f\). The connection on the localization is the actual inverse-transfer connection. If locally
\[
\nabla^{\bar E}=d+\sum_i A_i\,\frac{dz_i}{z_i}
                  +\sum_j C_j\,dw_j,
\]
then, on the localization where the expressions are defined,
\[
\begin{gathered}
\nabla^{N_f}=d+\sum_i f^*A_i\,\frac{dh_i}{h_i}\\
+\sum_j f^*C_j\,d(f^*w_j),\\
h_i=f^*z_i.
\end{gathered}
\tag{5.14b}
\]
The unshifted module \(N_f\) is \(\mathcal O_Y\)-flat and holonomic. For every map \(k:C\to Y\) from a smooth algebraic curve, \(k^!N_f\) is a regular holonomic bounded complex, including every point at infinity. This is a proved **curve-testing assertion**; regularity of \(N_f\) under the composition-factor definition is not inferred from it.

**Proof.** On a logarithmic frame chart, \(M\) is \(\bar E\otimes\mathcal O_P[1/q]\), where \(q\) is a local equation for the Cartier divisor \(D\). It is flat over \(\mathcal O_P\): the lattice is locally free and localization is flat. The actual transfer/structure-sheaf comparison in the inverse-image provider therefore gives
\[
\begin{gathered}
\mathcal D_{Y\to P}\otimes^L_{f^{-1}\mathcal D_P}f^{-1}M\\
\simeq\mathcal O_Y\otimes_{f^{-1}\mathcal O_P}f^{-1}M.
\end{gathered}
\tag{5.14c}
\]
This conclusion does not require \(f\) to be flat. Tensor associativity and the universal property of localization identify the right side with
\(f^*\bar E\otimes\mathcal O_Y[1/f^*q]\).

If the image of an integral component of \(Y\) is contained in the divisor, \(f^*q=0\) on that component, and this tensor is zero. Otherwise a nonzero \(f^*q\) is a nonzerodivisor in each smooth local domain. Its local equations differ by units and define the effective Cartier divisor \(B\). Localization is independent of its multiplicities, but the differential in (5.14b) retains them. The pulled-back lattice is locally free and its localization is \(\mathcal O_Y\)-flat. Adding the programme dimension shift proves (5.14a), including the degree assertion.

The source's chain-rule formula identifies the action on a pulled-back coefficient with the ordinary differential of the pulled-back functions; applied to the logarithmic frame, it is exactly (5.14b). The coefficient-derivative term is included, so this is a balanced connection formula and not tensor pullback of a non-\(\mathcal O\)-linear connection map. Its flatness is the already proved Lie-bracket calculation for the transfer. The old arbitrary holonomic inverse-image theorem applies to \(M\), which is holonomic by Theorem 5.13, and therefore proves holonomicity of \(N_f\). No regularity-preservation theorem is used.

Now let \(k:C\to Y\), with \(C\) connected. If \(f k(C)\subset D\), its pullback is zero by the same localization calculation. Otherwise the properness of \(P\) extends \(f k\) uniquely to
\(\bar h:\bar C\to P\), where \(\bar C\) is the smooth complete model of \(C\). The extension uses the earlier valuative criterion at each curve DVR, followed by uniqueness from separatedness. Near each point \(p\in\bar C\), choose the local boundary equations through \(\bar h(p)\). Since the curve is not contained in the boundary,
\[
\begin{gathered}
\bar h^*z_i=t^{m_i}u_i,\\
m_i\geq0,\quad u_i\in\mathcal O_{\bar C,p}^{\times},\\
\frac{d(\bar h^*z_i)}{\bar h^*z_i}\\
=m_i\frac{dt}{t}+\frac{du_i}{u_i}.
\end{gathered}
\tag{5.14d}
\]
Thus the full lattice \(\bar h^*\bar E\) is logarithmic at \(p\); its residue is \(\sum_i m_i\bar h^*A_i(p)\). There is no assertion that this sum remains normalized. All multiplicities and nilpotent parts are present. This proves regularity of the generic pullback connection at every point, including infinity, by the one-variable lattice criterion. Its meromorphic localization on \(C\) is regular holonomic by the curve argument in 5.13.5: full-support factors inherit a regular connection and point factors are delta modules. Since \(N_f\) is flat, its own extraordinary pullback has the single shift \([1-d]\). This completes the curve-testing assertion. \(\square\)

**Functoriality with all degrees.** For \(g:Z\to Y\), the flatness of \(N_f\) gives
\[
\begin{gathered}
N_{f,g}=(g^*f^*\bar E)(*g^*B),\\
g^!N_f=N_{f,g}[\dim Z-d].
\end{gathered}
\tag{5.14e}
\]
with zero again on boundary-contained components. Applied to \(N_f[d-n]\), the total shift is
\((\dim Z-d)+(d-n)=\dim Z-n\), the shift of \((fg)^!M\). The chain-rule transfer composition identifies these localization maps and their operator actions. This includes nonflat \(g\), singular \(g^{-1}B\), and every pure-dimensional component separately.

The calculation here proves curve testing of the singular meromorphic extension. Corollary 5.17.1 below supplies its regular simple-factor reconstruction after the full singular curve criterion has been proved.

![The singular pulled-back divisor, two exact curve tests, and supported graph base change](assets/arbitrary-inverse-transfer.png)

*Figure. The upper plot is the actual real slice of the divisor pulled back by \(f(x,y)=(x^2-y^3,x^2+y^3)\) in the affine chart of \(P=(\mathbb P^1)^2\), whose SNC boundary contains zero and infinity in both factors. For the commuting local residues \(A_1=\frac15I+J\), \(A_2=\frac3{10}I+J\), with \(J=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\), the boundary-contained curve has zero inverse image, and the diagonal curve has residue \(I+4J\) at zero. This residue is logarithmic but is not normalized; the finite multiplicities and nilpotent parts are exactly (5.14d). The lower panel is the arbitrary-map formula (5.14j), proved below, and retains the singular fiber product only as a support inside a smooth product. The figure displays the actual transfer and curve tests. The later Corollary 5.17.1 supplies simple-factor reconstruction. The reproducible drawing source supplies the original CC0 figure.*

#### Direct composition without quasi-projectivity

**Lemma 5.14.2.** Differential-operator direct image and its composition isomorphism exist on bounded quasi-coherent differential-operator complexes for every map of smooth separated finite-type varieties. For \(X\xrightarrow aY\xrightarrow bZ\),
\[
(ba)_*K\simeq b_*a_*K,
\tag{5.14f}
\]
naturally and associatively. This lemma concerns transfer, boundedness and composition; it asserts no regularity preservation.

**Proof.** Work on right modules for the tensor notation. Put \(T_a=\mathcal D_{X\to Y}\) and \(T_b=\mathcal D_{Y\to Z}\). Lemma 3.3 of the adjunctions lesson gives the augmented absolute Spencer resolution of \(T_a\), with terms
\[
\begin{gathered}
\mathcal D_X\otimes_{\mathcal O_X}\bigwedge^rT_X\\
\otimes_{\mathcal O_X}T_a,\\
\text{in degree }-r,\\
0\leq r\leq\dim X.
\end{gathered}
\tag{5.14g}
\]
Its proof uses the bracket/Leibniz differential, PBW, the polynomial Koszul sequence, and descent in the finite order of the first operator factor. Its terms are flat as left \(\mathcal D_X\)-modules, because \(T_a\) is \(\mathcal O_X\)-flat. Hence it computes transfer tensor with an arbitrary right quasi-coherent module; the resulting terms are quasi-coherent over \(\mathcal O_X\), and the amplitude is bounded by \([-\dim X,0]\). A bounded input complex has the corresponding finite band.

On an affine open \(V\subset Y\), \(a^{-1}V\) is quasi-compact and separated, and therefore has a finite affine cover with affine intersections. The usual finite affine Čech complex of the transferred quasi-coherent terms computes their sheaf direct image and supplies a finite additional degree bound. This requires separated finite type, not quasi-projectivity or a global free resolution.

We check the interchange needed for composition locally on \(Y\). Shrink to a coordinate affine chart whose image under \(b\) lies in an operator-coordinate chart on \(Z\). PBW on that target chart makes \(T_b\) a locally free \(\mathcal O_Y\)-module with possibly infinitely many basis elements. The same absolute Spencer resolution (5.14g), now for \(T_b\) on \(Y\), is bounded; on this chart its terms are direct sums of free left \(\mathcal D_Y\)-modules. This uses the trivialized finite exterior bundles of \(T_Y\) and the PBW basis of \(T_b\), so avoids any global-dimension assertion for arbitrary infinitely generated modules.

For a free term \(\mathcal D_Y^{(I)}\), tensoring on either side of
\[
\begin{gathered}
C_a=A\otimes^L_{a^{-1}\mathcal D_Y}a^{-1}T_b,\\
Ra_{\mathrm{sh},*}A\otimes^L_{\mathcal D_Y}T_b\\
\longrightarrow Ra_{\mathrm{sh},*}C_a,\\
A=K\otimes^L_{\mathcal D_X}T_a.
\end{gathered}
\tag{5.14h}
\]
gives the same direct sum of the finite Čech model for \(Ra_{\mathrm{sh},*}A\). Sections of quasi-coherent sheaves on each affine intersection commute with these direct sums, and the cover is finite. Thus (5.14h) is an isomorphism for each free term and for the bounded Spencer total. It is a natural sheaf comparison and hence glues from these local coordinate charts. No claim about arbitrary sheaf pushforward commuting with infinite sums is needed.

Inverse transfer composition from the inverse-images lesson gives the derived identity
\[
T_a\otimes^L_{a^{-1}\mathcal D_Y}a^{-1}T_b
\simeq T_{ba}.
\tag{5.14i}
\]
Its higher Tor vanishes because the underlying \(\mathcal O_Y\)-module of \(T_b\) is flat; its underived action is the chain rule. Substitute (5.14h) and (5.14i) in the two direct-image definitions and use composition of derived sheaf pushforward to obtain (5.14f). The bounded Spencer and finite Čech bands justify the totalizations. Tensor, chain-rule and pushforward composition are their actual associative maps, so the result is compatible with three maps. Side changing at \(X,Y,Z\) cancels at the middle variety and gives the left-module formula. \(\square\)

#### Base change through a possibly singular fiber product

Let \(f:X\to Y\) and \(g:Y'\to Y\) be arbitrary maps of smooth separated finite-type varieties. The scheme \(X\times_Y Y'\) may be singular or nonreduced. Use the smooth ambient product
\[
\begin{gathered}
T=Y'\times X,\\
t:T\to X,\qquad s:T\to Y',\\
F=\mathrm{id}_{Y'}\times f:T\to A,\\
A=Y'\times Y.
\end{gathered}
\]
Let \(i:Y'\hookrightarrow A\) be the closed graph of \(g\), and let \(W=F^{-1}(i(Y'))\subset T\) be the closed fiber product locus. Local cohomology depends only on its closed support, so allows its given nonreduced structure.

**Theorem 5.14 (supported graph formula).** For every bounded holonomic \(K\) on \(X\),
\[
g^!f_*K\simeq s_*R\Gamma_W(t^!K).
\tag{5.14j}
\]
Here the supported complex is on the **smooth** variety \(T\). No smooth transfer formula is assigned to \(W\). All complexes in (5.14j) are bounded holonomic, and the comparison is natural.

**Proof.** The closed-support local cohomology on \(T\) is the finite augmented Čech localization complex for local generators of the ideal of \(W\). Each term is a finite localization of a bounded holonomic complex, so is bounded holonomic by the earlier localization and holonomicity results. This construction glues and gives the triangle
\[
\begin{gathered}
Q=R\Gamma_W(t^!K)\\
\longrightarrow t^!K\\
\longrightarrow j'_*j'^!(t^!K)\longrightarrow.
\end{gathered}
\tag{5.14k}
\]
where \(j':T\setminus W\hookrightarrow T\). A product inverse image preserves holonomicity, so all assertions here precede regularity.

Let \(r:A\to Y\) and \(\pi:A\to Y'\) be the projections. The product case of the already proved smooth-ambient base-change theorem is
\(r^!f_*K\simeq F_*t^!K\). Since \(g=ri\), inverse composition gives
\[
g^!f_*K\simeq i^!F_*t^!K.
\tag{5.14l}
\]
Let \(j:A\setminus i(Y')\hookrightarrow A\). The restriction of \(F\) to \(T\setminus W\) maps into this complement, so composition identifies the last term of \(F_*\)(5.14k) with \(j_*H\) for a bounded holonomic complex \(H\) on that smooth open. The supported smooth graph calculation gives \(i^!j_*H=0\). Thus the map
\(i^!F_*Q\to i^!F_*t^!K\) is an isomorphism.

The output \(F_*Q\) has cohomology supported on \(i(Y')\): its restriction to the complement is the direct image of the zero restriction of \(Q\). This open-restriction calculation follows either from transfer tensor and finite Čech sheaf pushforward, or from the open case of composition. Kashiwara's smooth supported equivalence therefore gives
\[
F_*Q\simeq i_*i^!F_*Q.
\tag{5.14m}
\]
Apply \(\pi_*\). Since \(\pi i=\mathrm{id}_{Y'}\), 5.14.2 identifies
\(\pi_*F_*Q\simeq s_*Q\) and
\(\pi_*i_*i^!F_*Q\simeq i^!F_*Q\). Combining this with (5.14l) and (5.14k) proves (5.14j). The maps are localization augmentations, the product comparison and the intrinsic supported counit. They are natural, not chosen identifications. Holonomicity and boundedness of the outputs use only the earlier arbitrary holonomic direct/inverse preservation and 5.14.2. \(\square\)

If \(W\) happens to be smooth, the earlier supported formula identifies \(R\Gamma_W t^!K\) with its closed direct image of the appropriate intrinsic inverse image, recovering the usual smooth-square formula with its shifts. For singular \(W\), (5.14j) is the usable replacement, with the operator directions retained.

#### Curve testing commutes with closed support

**Lemma 5.14.3.** For any algebraic map \(a:V\to T\) of smooth varieties and closed subset \(W\subset T\),
\[
a^!R\Gamma_W K\simeq R\Gamma_{a^{-1}W}(a^!K).
\tag{5.14n}
\]
Consequently, if every smooth-curve inverse image of a bounded holonomic \(K\) is regular, then the same holds for \(R\Gamma_W K\).

**Proof.** On an affine chart choose finitely many equations \(u_1,\ldots,u_l\) for \(W\). Derived pullback commutes with each localization:
\[
\begin{gathered}
La_{\mathcal O}^*(K[1/u])\\
\simeq(La_{\mathcal O}^*K)[1/a^*u].
\end{gathered}
\tag{5.14o}
\]
Take a flat resolution of \(K\); termwise this is the universal tensor/localization identity, and flatness of localization justifies the derived comparison. The chain-rule action preserves the localization identity. The finite augmented Čech complex and the fixed dimension shift then prove (5.14n); refinements give the same augmentations, so it glues.

For a connected smooth curve \(C\), its inverse image of \(W\) is empty, the whole curve, or a finite closed subset. In the first case local cohomology is zero; in the second it is the original inverse complex. In the finite case every cohomology module is holonomic and supported on finitely many points, hence regular by Kashiwara and the point presentation. This proves the final assertion for every curve map, without asserting Serre closure of the curve-testing property on the original ambient variety. \(\square\)

#### A converse criterion for nonsingular cohomology on a smooth support

**Lemma 5.14.4.** Suppose \(i:Z\hookrightarrow X\) is an arbitrary smooth closed embedding, and \(L\in D_h^b(\mathcal D_Z)\) has finite-rank nonsingular connections as all its cohomology modules. Then \(i_*L\) is regular holonomic if and only if every smooth locally closed curve in \(X\) has regular extraordinary restriction of \(i_*L\). Equivalently, one may test every map from a smooth algebraic curve to \(X\).

**Proof of the connection test.** For a nonsingular connection \(A\) on a smooth variety, testing its pullback to smooth locally closed embedded curves suffices for the all-map definition. Given a nonconstant curve map \(k:C\to Z\), choose a dense smooth locally closed open \(B\) of its irreducible curve image. Its embedding in \(Z\) is one of the tests. On the dense open \(k^{-1}B\), the pullback is the pullback of the tested regular connection on \(B\). The map between function fields extends to a finite nonconstant map of smooth complete curve models. Pulling a stable logarithmic lattice through a ramification \(t=u^e v\), \(v\) a unit, gives a stable logarithmic lattice: its coefficient is multiplied by \(e\) and has the additional holomorphic term \(dv/v\), exactly as in (5.14d). This supplies regularity at every completion point. At a point of \(C\) omitted from \(k^{-1}B\), the full pullback connection on \(C\) is nonsingular and supplies its own lattice. Constant maps give a trivial finite-rank connection. This proves the all-map connection test, including infinity and arbitrary ramification.

On a bounded complex with flat cohomology, the finite hyper-Tor spectral sequence for structure-sheaf inverse image has only its zero Tor row. Thus, for \(k:C\to Z\),
\[
\begin{gathered}
H^q(k^!L)\\
=k^*H^{q+1-\dim Z}(L).
\end{gathered}
\tag{5.14p}
\]
The same formula follows from finitely many standard truncation triangles and flatness of their cohomology pieces; no abstract derived-category-of-the-heart identification is needed. Regularity of the curve complex therefore tests exactly those connection modules. The connection/regular-holonomic identification of Theorem 5.2 and the preceding embedded-curve argument prove the criterion for \(L\).

If \(i_*L\) passes the embedded-curve tests on \(X\), every smooth locally closed curve \(C\hookrightarrow Z\) also embeds locally closed in \(X\). Inverse composition and \(i^!i_*L=L\) identify its test with that of \(L\), so the proved connection criterion makes \(L\) regular. 5.13.1's exact supported equivalence then makes \(i_*L\) regular.

Conversely let \(L\) be regular and let \(h:C\to X\) be arbitrary. If \(h(C)\subset Z\), reducedness of the smooth curve makes the map factor through the reduced smooth closed subvariety \(Z\). Composition and supported Kashiwara identify \(h^!i_*L\) with the intrinsic curve inverse image of \(L\), regular by (5.14p). Otherwise \(h^{-1}Z\) is finite, and the earlier arbitrary holonomic inverse theorem makes \(h^!i_*L\) a bounded holonomic complex supported on those finitely many points. It is regular. This includes constant maps and nontransverse intersections. \(\square\)

This is a genuine converse on every smooth closed support with nonsingular cohomology; it does not assert a converse for an arbitrary singular extension or a complex with singular cohomology on that support.

#### The support-dimension reduction and low images

**Lemma 5.14.5.** For an SNC meromorphic module, image dimension at most one gives regular direct image. For higher image dimension, lower-support curve and direct-image theorems give its curve tests by the supported graph construction.

Let \(P\) be integral of dimension \(n\), let \(M=\bar E(*D)\) as in 5.14.1, and let \(f:P\to Y\) be arbitrary. For a nonconstant \(g:C\to Y\), 5.14 realizes the curve inverse image of \(f_*M\) as the direct image of
\[
\begin{gathered}
Q=R\Gamma_W(t^!M),\\
W\subset C\times P.
\end{gathered}
\tag{5.14q}
\]
The product complex \(t^!M\) is curve-tested by 5.14.1 and inverse composition. It is also regular: it is the open restriction of the SNC meromorphic bundle \(\mathcal O_{\bar C}\boxtimes\bar E\) on the proper pair \((\bar C\times P,(\bar C\setminus C)\times P+\bar C\times D)\), to which 5.13 applies. 5.14.3 makes \(Q\) curve-tested independently of its simple-factor regularity.

If \(\dim f(P)\geq2\), the locus \(f^{-1}(\overline{g(C)})\) is a proper closed subset of \(P\), of dimension at most \(n-1\). The projection \(W\to P\) is quasi-finite, since every fiber of a nonconstant algebraic curve map is finite. Hence
\[
\begin{gathered}
\dim\operatorname{Supp}Q\leq\dim W\\
\leq n-1.
\end{gathered}
\tag{5.14r}
\]
This is a dimension calculation on the actual possibly singular fiber product, not an assertion that it is a smooth variety. If the full converse curve criterion and regular direct-image preservation have already been proved for source supports of dimension less than \(n\), they apply in that order to \(Q\), and (5.14j) proves that \(g^!f_*M\) is regular. For a constant curve map, factor it through a point: holonomic inverse image at the point is a bounded finite-dimensional complex, and its pullback to the curve is a complex of trivial connections with the correct shift. Thus constant maps cause no induction increase.

If \(\dim f(P)\leq1\), \(f_*M\) is already regular without that conditional induction. Its support has dimension at most one. In dimension zero it has only point factors. In dimension one, choose a dense smooth curve open in its image. Write \(f_*M=(f|_U)_*E\) by 5.14.2 and affine localization. After shrinking the image curve, generic smoothness in characteristic zero makes \(f|_U\) smooth there; the elementary derivation/Jacobian proof used in Theorem 5.6 gives this shrink by removing the finitely many nondominating critical images. The full generic Gauss–Manin Theorem 5.6 then makes every generic cohomology connection regular, with its actual transfer action and shift. Every curve-support simple factor inherits a subquotient of one of these regular generic connections; every remaining simple factor has point support. Choose a further affine dense curve open for its presenting immersion and apply minimal-extension uniqueness. All these simple factors are regular under the definition, so every cohomology module is regular.

For image dimension at least two, this is the lower-support step used in the ordered induction below. Its same-dimensional converse is proved by Theorem 5.16.1 after the forward assertion at that dimension; curve testing is not assumed closed under arbitrary heart subquotients.

### Dual SNC Spencer and every curve test

Let \((P,D)\) be any smooth proper SNC pair over \(\mathbb C\), with finitely many globally smooth components \(D_i\). Fix their order for exterior signs. Let \(a:U=P\setminus D\hookrightarrow P\), let \(E\) be any curve-regular finite-rank connection, and let \(\bar E\) be its normalized algebraic logarithmic extension, with residue real parts in \([0,1)\). Put \(M=a_*E=\bar E(*D)\). The dual connection has local normal residues \(-A_i^t\).

The exact earlier proofs are PBW and holonomic duality; the normalized logarithmic and constant-residue calculations in Theorems 5.0 and 5.3; the faithful-flat analytic local comparison linked there; Theorem 5.13; and the inverse-transfer convention of Proposition 1.1 in the inverse-images lesson. Analytic normalization verifies an algebraic presentation by faithful flatness. The proper-curve lattice argument below proves regularity at infinity.

#### Logarithmic induction and its dual

Write \(T_P(-\log D)\) for the locally free logarithmic tangent bundle and \(\mathscr L_P\) for its operator algebra. If \(L\) is a locally free logarithmic integrable connection, its induced module has the augmented logarithmic Spencer complex
\[
\begin{gathered}
\operatorname{Sp}_{\log}^{-r}(L)\\
=\mathcal D_P\otimes_{\mathcal O_P}
\bigwedge^rT_P(-\log D)\\
\otimes_{\mathcal O_P}L,\qquad0\leq r\leq n,\\
n=\dim P.
\end{gathered}
\tag{5.15a}
\]
with multiplication-minus-connection and bracket differential. Its augmentation is to
\(\mathcal D_P\otimes_{\mathscr L_P}L\).

**Lemma 5.15.1.** The complex (5.15a) resolves its augmented induced module in degree zero. In particular
\[
M\simeq\mathcal D_P\otimes_{\mathscr L_P}\bar E(D).
\tag{5.15b}
\]
Its dual is
\[
\mathbb D_PM\simeq
\mathcal D_P\otimes_{\mathscr L_P}\bar E^{\vee}.
\tag{5.15c}
\]
Every statement retains the full connection matrices and their nilpotent parts.

**Proof of exactness.** On adapted étale coordinates \(z_1,\ldots,z_k,w_1,\ldots,w_{n-k}\), the logarithmic generators are \(\theta_i=z_i\partial_{z_i}\) and \(\partial_{w_j}\). Give the term in degree \(-r\) the order filtration shifted by \(r\). Its leading differential is the Koszul differential on
\[
\begin{gathered}
z_1\xi_1,\ldots,z_k\xi_k,\\
\eta_1,\ldots,\eta_{n-k}
\quad\text{in }\mathcal O_P[\xi,\eta].
\end{gathered}
\tag{5.15d}
\]
This is a regular sequence. Over the polynomial coordinate ring, after quotienting the preceding products, multiplication by the next independent coordinate \(z_i\), the new variable \(\xi_i\), or a new \(\eta_j\) is injective: the quotient has a monomial decomposition involving only the preceding coordinate pairs. Thus each new product is a nonzerodivisor. Tensoring its polynomial Koszul resolution through the flat étale coordinate algebra preserves exactness. Tensoring with the free coefficient bundle \(L\) does so as well. Subtract a lift of a leading graded boundary from a cycle and descend its finite order; the lower bound terminates the process. This proves exactness in negative degrees. The degree-zero relations are exactly the logarithmic tensor relations, because functions and the displayed logarithmic vector fields generate \(\mathscr L_P\). Hence the augmented module is as asserted. The intrinsic bracket differential makes the resolutions glue.

For \(L=\bar E(D)\), its local normal matrices are \(A_i-I\), and the generation proof 5.13.3 gives the natural surjection from this induced module to \(M\). It is injective as well. After analytic stalk extension, the proved normalized logarithmic local model changes the lattice by a holomorphic invertible matrix to the commuting constant-residue model. Its exact presentation is Theorem 5.3, equation (5.3j), whose relations are precisely \(\theta_i-(A_i-I)\) and the tangential connection relations. Thus the analytic extension of the surjection is an isomorphism. The analytic stalk ring is faithfully flat over the algebraic local ring; the underlying operator extension is its tensor extension by PBW. Faithfulness therefore kills the algebraic kernel. No analytic regularity theorem is being used to infer algebraic regularity.

Dualize (5.15a). Its terms are finite locally free over \(\mathcal D_P\), so it computes operator duality. Wedge pairing identifies the reversed exterior complex with the logarithmic Spencer complex for
\[
\begin{gathered}
L^\vee\otimes\bigl(\bigwedge^n\Omega_P^1(\log D)\bigr)\\
\otimes\omega_P^{-1}\\
=L^\vee\otimes\mathcal O_P(D).
\end{gathered}
\tag{5.15e}
\]
The degree reversal is canceled by the duality shift \([n]\). The density action in (5.15e) has normal logarithmic coefficient \(-1\) on the local frame \((z_1\cdots z_k)^{-1}\). Explicitly \(\theta_i^t=-\theta_i-1\), whereas \(\partial_{w_j}^t=-\partial_{w_j}\) in the coordinate volume. Thus a normal matrix \(R_i\) becomes \(-R_i^t-I\), and a tangential matrix becomes its negative transpose. These are exactly the connection and bracket terms in the paired Spencer differential. This coordinate verification on the generating vector fields, with Leibniz, verifies the full differential; the wedge and density pairing is intrinsic and hence glues.

In particular, the local source presentation has generators related by \(\theta_i-(A_i-I)\) and \(\partial_{w_j}-C_j\); its density-transposed presentation has the relations \(\theta_i+A_i^t\) and \(\partial_{w_j}+C_j^t\). The reversed exterior bases have the usual Koszul complement signs; wedge pairing fixes them, and multiplying a whole generator relation by \(-1\) does not change its quotient. Thus the sign calculation includes the scalar divergence term as well as the matrix transpose. The variable coefficient derivatives in higher wedges obey the same Leibniz rule; the curvature commutators vanish by integrability.

For \(L=\bar E(D)\), (5.15e) is \(\bar E^{\vee}\), and its normal matrices are \(-A_i^t\), since \(- (A_i-I)^t-I=-A_i^t\). Exactness of the new logarithmic Spencer complex proves (5.15c), in degree zero. For the curve argument below it is (5.15c) that is used; relabeling \(E^{\vee}\) gives all !-extensions. \(\square\)

A logarithmic lattice with residues in \([0,1)\) is generally not the lattice dual to the normalized lattice of \(E^{\vee}\). For every \(E\), write \(\bar F\) for the normalized lattice of \(F=E^{\vee}\), and use the exact formula
\[
\begin{gathered}
a_!E=\mathbb D_P(a_*F)\\
\simeq\mathcal D_P\otimes_{\mathscr L_P}\bar F^\vee.
\end{gathered}
\tag{5.15f}
\]
This keeps all exponents and avoids an invalid normalization claim. The proof and theorems below use (5.15c)/(5.15f) only.

#### Normal inverse image and the finite residue complex

Let \(H=\mathbb D_PM\), presented by (5.15c). Its lattice \(L=\bar E^{\vee}\) has normal matrices \(B_i=-A_i^t\), with eigenvalue real parts in \((-1,0]\). For an intersection component \(Z\) of \(D_I\), remove the other boundary components and call the resulting smooth stratum \(S\). Write \(c=|I|\), and write \(i:S\hookrightarrow P\setminus\bigcup_{j\notin I}D_j\) for its closed immersion.

**Lemma 5.15.2.** On \(S\), the cohomology connections of \(i^!H\) are the cohomology of the normal chain Koszul complex
\[
\begin{gathered}
K_I^{-r}=L|_S\otimes\bigwedge^r\mathbb C^I,\\
d=\operatorname{Koszul}((-B_i)_{i\in I}),\\
-B_i=A_i^t,\qquad0\leq r\leq c.
\end{gathered}
\tag{5.15g}
\]
shifted by \([-c]\). Thus the degrees are \(0,\ldots,c\). The full commuting matrices \(A_i^t\), including zero eigenvalues and Jordan blocks, are retained. On the proper \(Z\), the same residue complex on \(L|_Z\) has coherent cohomology with a logarithmic connection along the remaining boundary, and restricts to these intrinsic cohomology connections on \(S\).

**Proof of the normal calculation.** Resolve \(H\) by (5.15a) for \(L\), and tensor its terms with \(\mathcal O_S\). They are \(\mathcal O_P\)-flat because they are finite free operator terms with locally free coefficients. This computes \(Li_{\mathcal O}^*H\). Use PBW to put every normal derivative to the left of the tangential derivatives, and filter this tensor complex by its total normal derivative degree.

The differential preserves that filtration. Moving a coefficient matrix through a normal derivative only introduces terms of smaller normal degree. On the graded piece labeled by a normal multi-index \(b\in\mathbb N^I\), right multiplication by \(\theta_i\) gives
\[
\partial_z^b\theta_i
=\theta_i\partial_z^b+b_i\partial_z^b.
\tag{5.15h}
\]
The first term vanishes after structure-sheaf tensor with \(\mathcal O_S\), since its left coefficient is \(z_i\). Consequently its normal differential is the Koszul operator
\[
b_iI-B_i|_S=b_iI+A_i^t|_S.
\tag{5.15i}
\]
The tangential differential is the tangential Spencer differential for \(L|_S\). Integrability makes the restricted residues commute and horizontal for that tangential connection, so these differentials commute with the required total-complex signs.

If \(b\ne0\), choose \(i\) with \(b_i\geq1\). The matrix in (5.15i) is invertible at every stalk, because every eigenvalue of \(A_i\) has real part in \([0,1)\). Its inverse is horizontal as well. Exterior multiplication by the corresponding basis vector, composed with this inverse and its Koszul sign, contracts that normal Koszul factor and commutes with the tangential differential. Hence the entire positive-normal-degree graded piece is acyclic. Every section has finite normal degree. Descending its leading degree proves that the quotient by the degree-zero subcomplex is acyclic.

That degree-zero subcomplex has exactly the normal Koszul differential \(-B_i\) and the tangential Spencer resolution. Resolving its tangential terms leaves (5.15g). Finally the programme closed inverse image appends \([-c]\), placing its cohomology in degrees \(0,\ldots,c\). This is an algebraic filtration calculation; no constant-residue gauge is used for this calculation.

**The connection and its boundary lattice.** The normal residue endomorphisms are canonical endomorphisms of \(L|_Z\), and commute by integrability, so (5.15g) defines a finite complex of algebraic vector bundles on all of \(Z\). A logarithmic tangent field on \(Z\) lifts locally to a logarithmic field on \(P\) preserving the components \(D_i\), \(i\in I\). Acting on \(L|_Z\) with this lift commutes with the residue differential. Two lifts differ, after restriction, by \(\sum_i u_i\theta_i\); their coefficient actions differ by \(\sum_i u_iB_i\). Multiplication by \(B_i\) is null-homotopic on the residue Koszul complex, using the corresponding exterior multiplication or contraction with its sign. Thus the induced action on its cohomology is independent of the lift. The Leibniz rule is inherited; the bracket/curvature error is likewise a normal residue action and hence null-homotopic. Its cohomology consequently has an intrinsic integrable logarithmic connection.

On \(S\) this is an ordinary coherent connection, hence a finite-rank bundle by the earlier coherent-connection theorem. The normal-degree-zero comparison above intertwines its tangential action with the actual inverse-transfer action: tangential left operators pass through the normal PBW terms, and the tangential Spencer augmentation leaves precisely the coefficient connection. The lift ambiguity is the just-computed residue homotopy. This identifies the connections, not only their vector spaces.

At the remaining boundary on \(Z\), the cohomology of the finite residue-bundle complex remains coherent and logarithmically stable. Torsion may occur there; no assertion of local freeness at that boundary is needed. These coherent cohomology modules are the boundary lattices used in 5.15. \(\square\)

#### Every curve inverse image of the dual SNC module is regular

**Theorem 5.15.** For every algebraic map \(k:C\to P\) from a smooth algebraic curve, \(k^!\mathbb D_PM\) is a regular holonomic bounded complex. The same holds on every open restriction of the proper pair and for every SNC !-extension (5.15f). The curve can lie entirely in any intersection component, be constant, or have arbitrary tangencies.

**Proof.** Work on a connected curve. Let \(I\) consist of those global boundary components containing its entire image. If \(I\) is empty, on a dense open of \(C\) the inverse image is the pullback of the regular connection \(E^{\vee}\), with the fixed dimension shift; its generic cohomology is regular at every compactification point by the all-curve definition. The remaining finite-point factors are regular, so the entire bounded curve complex is regular. This argument also covers curves meeting the boundary only at finitely many points, without asserting that their full inverse image is a flat localization.

If \(I\ne\varnothing\), properness of \(P\) extends the map to \(\bar k:\bar C\to P\). Its image still lies in one connected component \(Z\) of \(D_I\), since the selected boundary equations vanish on the dense original curve. It is not contained in any remaining boundary component. Away from the finitely many inverse images of the remaining boundary, the map factors through the smooth stratum \(S\) in 5.15.2. Composition and its normal calculation give its generic inverse cohomology by pullback of the connections (5.15g)[\(-c\)], with the additional shift \([1-\dim S]\). These are the actual inverse-image degrees and connections.

Pull the finite vector-bundle residue complex (5.15g) on \(Z\) to all of \(\bar C\). Its cohomology agrees on that dense open with pullback of the cohomology on \(S\): its terms and cohomology are flat there, so the bounded flat-complex base-change argument proved in Gauss–Manin Theorem 5.6 applies to any such curve map. At a completion point choose a parameter \(t\). Each remaining boundary equation has the form \(t^m u\) with \(u\) a unit. The logarithmic tangent vector \(t\partial_t\) therefore maps to an \(\mathcal O_{\bar C}\)-linear combination of the logarithmic tangent generators on \(Z\). The same local lift construction in 5.15.2 defines a logarithmic connection on the pulled residue complex and on its coherent cohomology. Normal lift ambiguities remain null-homotopic residue actions.

For each such coherent cohomology module, divide out its torsion. The torsion is logarithmically stable: if \(t^r v=0\), the Leibniz rule gives \(t^r(\Theta v+r v)=0\), so \(\Theta v\) is torsion too. The resulting finite torsion-free module at a curve DVR is a free lattice. It spans precisely the generic inverse cohomology connection, and \(t\nabla_{\partial_t}\) preserves it. The one-variable criterion proves regularity at every point of \(\bar C\), including infinity and points where additional boundary components meet the curve. Thus every generic connection of the actual inverse complex is regular. All its other cohomological simple factors on \(C\) have point support and are regular. Holonomic inverse preservation supplies boundedness and holonomicity, so the full complex is regular.

Constant maps are included: the residue complexes give finite-dimensional connections pulled back from a point; alternatively factor through that point and use holonomic inverse image there, followed by the trivial curve pullback. Open restrictions are tested by composing the curve map into \(P\), so the same proof applies. Finally apply the result to the normalized lattice of \(E^{\vee}\) in (5.15f), obtaining the theorem for \(a_!E\). \(\square\)

The theorem establishes the forward curve test of !-extensions, independently of the desired singular criterion. The finite residue complex rather than a diagonalized residue eigenspace is essential: eigenvalue zero and all nilpotent Jordan maps determine its kernels and cokernels.


### Lowest-cohomology detection and bounded socle peeling

Call a complex **curve-tested** if every extraordinary inverse image by a map from a smooth algebraic curve is regular holonomic. Call it **embedded-curve-tested** if the same holds for every smooth locally closed curve immersion. Either class is triangulated, because inverse image is triangulated and the proved composition-factor regular category is a Serre category. Neither class is assumed to be closed under heart subquotients or standard truncations.

The exact earlier proofs are closed-embedding Koszul inverse image and Kashiwara, holonomic inverse preservation, generic connection structure and finite length, Theorem 5.2 and Proposition 5.2.2. Lemma 5.14.4 below the supported graph formula proves the nonsingular embedded-curve criterion. No singular curve criterion or regularity stability is an input.

#### Detecting every simple subobject in the lowest cohomology

**Theorem 5.16.** Let \(K\) be a bounded holonomic complex, with \(H^qK=0\) for \(q<a\). If \(K\) is embedded-curve-tested, every simple subobject of \(H^aK\) is regular holonomic. This also applies when \(H^aK=0\), and requires no smoothness of a simple subobject's closed support.

**Proof.** Let \(S\subset H^aK\) be a nonzero simple subobject, with irreducible reduced support \(W\). Choose an ambient open \(V\) where a dense open \(W_0\) of \(W\) is smooth and closed in \(V\), and where the supported inverse of \(S|_V\) is a nonsingular irreducible connection \(E\) on \(W_0\). These choices are the earlier simple-factor classification and generic-connection theorem; no regularity is asserted by them. Write \(i:W_0\hookrightarrow V\).

For a module in degree zero, the normal Koszul formula for a closed embedding of codimension \(c\) places \(i^!\) in degrees \(0,\ldots,c\). Indeed \(Li_{\mathcal O}^*\) lies in \([-c,0]\), and the shift \([-c]\) moves those terms to \([0,c]\). Consequently \(i^!\) preserves the lower standard cohomological bound of a bounded complex, and \(H^0i^!\) is left exact on modules. Apply it to the lowest truncation triangle to obtain
\[
H^a(i^!K|_V)\simeq H^0i^!(H^aK|_V).
\tag{5.16a}
\]
The subobject \(S\) therefore gives an injection
\[
\begin{gathered}
E=H^0i^!(S|_V)\\
\hookrightarrow H^a(i^!K|_V).
\end{gathered}
\tag{5.16b}
\]

Shrink \(W_0\) further so that all the finitely many cohomology modules of \(i^!K|_V\) are nonsingular finite-rank connections. Holonomic inverse preservation makes these modules holonomic, so the generic-connection theorem permits this common shrink. It remains a smooth locally closed subset of \(X\), and its immersion into a suitable smaller ambient open is closed.

For every smooth locally closed curve \(C\hookrightarrow W_0\), composition identifies its extraordinary restriction of \(i^!K|_V\) with the given restriction of \(K\) to that same locally closed curve in \(X\). It is regular by hypothesis. All cohomology pieces on \(W_0\) are flat, so the bounded hyper-Tor calculation in 5.14.4 gives, with \(w=\dim W_0\),
\[
\begin{gathered}
H^r(k^!i^!K|_V)\\
\simeq k^*H^{r+1-w}(i^!K|_V).
\end{gathered}
\tag{5.16c}
\]
Thus the embedded-curve test proves that each nonsingular cohomology connection on \(W_0\), and in particular that on the right of (5.16b), is curve regular. The exact connection test in 5.14.4 extends this statement from embedded curves to every curve map and every compactification point. The connection Serre property now makes its connection subobject \(E\) curve regular.

Choose a nonempty affine open \(U\subset W_0\). Its immersion into \(X\) is affine: for an affine open \(A\subset X\), its inverse image is the graph closed in the affine product \(U\times A\), because \(X\) is separated. The simple-factor classification and no-boundary uniqueness recover
\[
S\simeq (U\hookrightarrow X)_{!*}(E|_U).
\tag{5.16d}
\]
Its irreducible connection is curve regular, and its presenting immersion is affine. This is precisely a regular presentation under the composition-factor definition. Singular points of \(W\) were removed only to obtain the presenting connection; no regularity criterion on the singular closure was assumed. \(\square\)

#### Peeling replaces the same-dimensional converse

Fix a nonnegative integer \(n\). Let \(R_n\) be the assertion that every regular simple module with support dimension at most \(n\), on every smooth ambient variety, is curve-tested for **all** curve maps. This is a forward assertion, and is not assumed true without proof in the later induction.

**Theorem 5.16.1.** If \(R_n\) has been proved, a bounded holonomic complex whose cohomological supports all have dimension at most \(n\) is regular if and only if it is embedded-curve-tested; equivalently if and only if it is curve-tested for all curve maps. In particular the bounded-complex converse needs no further same-dimensional reconstruction theorem once \(R_n\) is available.

**Proof of the forward implication under the stated input.** Every regular module has a finite composition series of regular simples. Its successive short exact sequences are distinguished triangles. \(R_n\) and triangulated closure of the curve-tested class therefore make the whole module curve-tested. The finitely many standard truncation triangles of a bounded regular complex give the same conclusion for that complex. This proves testing under every curve map and hence under embedded curves.

**Proof of the converse.** For a nonzero bounded embedded-curve-tested \(K\), choose its lowest nonzero degree \(a\), and a simple subobject \(S\subset H^aK\). Finite length supplies this subobject, and Theorem 5.16 proves that it is regular. Its support dimension is at most \(n\); \(R_n\) therefore makes \(S[-a]\) curve-tested, and hence embedded-curve-tested. Compose its inclusion with the canonical lowest-cohomology map
\[
S[-a]\longrightarrow H^aK[-a]\longrightarrow K,
\]
and let \(K'\) be its cone. The cohomology sequence gives
\[
\begin{gathered}
H^aK'=H^aK/S,\\
H^qK'=H^qK\quad(q\ne a).
\end{gathered}
\tag{5.16e}
\]
with all lower cohomology zero. The cone is embedded-curve-tested by triangulated closure. The integer
\[
\ell(K)=\sum_q\operatorname{length}H^qK
\tag{5.16f}
\]
is finite and has decreased by one. Induction on \(\ell(K)\), with the zero complex as base, proves that \(K'\) is regular. Then (5.16e), the regular simple \(S\), and the proved Serre property make \(K\) regular. Every step retains the original support-dimension bound. The proof assumes neither standard-truncation closure of the testing class nor subquotient closure of that class. \(\square\)

This theorem isolates the remaining forward input exactly. It applies to all singular closed supports, all bounded holonomic complexes, all cohomological degrees and every smooth ambient dimension. The later induction must prove \(R_n\); it cannot silently replace that input by the full regularity-stability theorem.


### Four-map regularity on every singular support

The original definitions are retained. A regular module is one whose simple factors have affine minimal-extension presentations by irreducible all-curve regular connections; a regular bounded complex has such modules as every cohomology module. The Serre and triangulated properties follow from that definition, as proved in Lemma 5.13.1. “Curve-tested” and “embedded-curve-tested” are temporary testing properties and acquire no assumed Serre or truncation closure.

#### The three induction assertions

For a nonnegative integer \(n\), use the following assertions on **all** smooth ambient varieties, with no restriction on their dimension:

- \(R_n\): every regular simple module with support dimension at most \(n\) is curve-tested for every smooth algebraic curve map.
- \(C_n\): every bounded holonomic complex with cohomological supports of dimension at most \(n\) is regular if and only if it is embedded-curve-tested, equivalently curve-tested for all smooth curve maps.
- \(P_n\): every algebraic direct image preserves regular bounded complexes whose source cohomological supports have dimension at most \(n\).

The order at dimension \(n\) is
\[
\begin{gathered}
(R_{n-1},C_{n-1},P_{n-1})\\
\Longrightarrow R_n\\
\Longrightarrow C_n\\
\Longrightarrow P_n.
\end{gathered}
\tag{5.17a}
\]
Thus a same-dimensional converse is never used to prove its own forward assertion. All lower-support complexes occurring below may live on smooth ambient varieties of larger dimension.

#### A curve test for proper images of the two SNC standard modules

Assume \(C_{n-1}\) and \(P_{n-1}\), with \(n\geq2\). Let \(P\) be a smooth proper integral variety of dimension \(n\), let \(D\) be SNC, let \(Q^+=\bar E(*D)\), and let \(Q^-=a_!E\) be the corresponding !-extension. Theorem 5.13 and regular duality prove that both are regular modules. Proposition 5.14.1 and Theorem 5.15 prove, independently, that both are curve-tested on \(P\) and on every open restriction.

Let \(F:P\to\bar Y\) be proper, where \(\bar Y\) is smooth, and let \(Y\subset\bar Y\) be open. Write \(P_Y=F^{-1}Y\) and \(F_Y:P_Y\to Y\). Suppose \(\dim F(P)\geq2\). We claim
\[
\begin{gathered}
F_{Y,*}(Q^\pm|_{P_Y})\\
\text{is curve-tested.}
\end{gathered}
\tag{5.17b}
\]

For a nonconstant curve map \(g:C\to Y\), the supported graph formula 5.14 is
\[
\begin{gathered}
g^!F_{Y,*}(Q^\pm|_{P_Y})\\
\simeq s_*R\Gamma_Wt^!(Q^\pm|_{P_Y}),\\
W=P_Y\times_YC\subset C\times P_Y.
\end{gathered}
\tag{5.17c}
\]
Inverse composition makes \(t^!Q^\pm\) curve-tested, and 5.14.3 makes its supported local cohomology curve-tested. The projection \(W\to P_Y\) is quasi-finite: its fibers are fibers of the nonconstant curve map, hence finite. Its image lies in
\(F_Y^{-1}(\overline{g(C)})\), a proper closed subset of the integral \(n\)-dimensional \(P_Y\). Therefore
\[
\dim W\leq n-1.
\tag{5.17d}
\]
The scheme \(W\) need not be smooth or reduced; it is used only as support inside \(C\times P_Y\). \(C_{n-1}\) makes the supported complex in (5.17c) regular, and \(P_{n-1}\) makes its direct image under \(s\) regular. This proves the test. If \(P_Y\) is empty there is no output; otherwise it is a dense integral open, so the dimension assertion applies. A constant curve map factors through a point. Arbitrary holonomic inverse image at that point is a bounded finite-dimensional complex, and its inverse image on the curve is a shifted complex of trivial connections. It is regular. Thus (5.17b) includes every curve map.

For the standard immersions used in the forward simple-module argument, \(\dim F(P)=n\), so (5.17b) applies directly. For a general map whose image has dimension zero or one, only \(Q^+\) is needed in the direct-image induction. 5.14.5 proves its output regular by full generic Gauss–Manin and the curve-support simple-factor argument, independently of the same-dimensional criterion.

#### Base dimensions zero and one

Every simple point-supported module is a delta module for a one-dimensional vector space. A curve inverse image has finite support unless the curve maps constantly to the point; in that case factor through the point and obtain a shifted trivial connection. Thus \(R_0\) holds. 5.16.1 gives \(C_0\). Every point-supported holonomic complex is recovered by exact supported Kashiwara on a finite disjoint union of points. Under any map its image is again a bounded complex of point modules, by direct composition, so \(P_0\) holds.

For \(R_1\), let \(S\) be regular simple with curve support \(Z\), possibly singular. Its regular presentation is a connection \(E\) on a dense smooth curve open \(U\subset Z\). A constant curve map is handled as above. A nonconstant curve map either has image outside \(Z\) generically, in which case its inverse image is supported on finitely many points; or has image in \(Z\), in which case on a dense source open it factors through \(U\). Inverse composition and \(j^!S=E\) identify its generic inverse connection with the pullback of \(E\). That connection is regular at every completion point by the all-curve property of \(E\). Every other simple factor of the inverse complex has point support. Hence the whole inverse complex is regular. This includes curve maps meeting the singular points of \(Z\) nontransversely. Thus \(R_1\) holds, and 5.16.1 gives \(C_1\).

The proof of \(P_n\) in the direct-image induction, used at \(n=1\), invokes \(P_0,C_0,C_1\) and the low-image Gauss–Manin clause of 5.14.5; there is no image of dimension at least two. It therefore establishes \(P_1\) without a missing induction input. These are the full bases of (5.17a).

#### Forward testing of every regular simple at dimension n

Let \(n\geq2\), and assume the three assertions at dimensions less than \(n\). Take a regular simple \(S\) of support dimension \(n\), on any smooth separated \(X\). Choose its defining affine immersion
\[
j:U\hookrightarrow X,\qquad S=j_{!*}E,
\tag{5.17e}
\]
where \(E\) is irreducible and curve regular on the smooth integral \(n\)-dimensional \(U\). The two standard extensions are modules in degree zero. Any immersion factors as closed followed by open, which gives \(j_*E\) degrees \(\geq0\). Because \(j\) is affine, on every affine target open its source is affine; the bounded flat transfer resolution has nonpositive degrees and quasi-coherent terms, whose affine sheaf pushforward is acyclic. Thus \(j_*E\) also has degrees \(\leq0\), and is a module. This is the earlier affine-direct-image bound, with 5.14.2's transfer/Čech construction. It does not require the chosen open factor itself to be affine. The !-extension is the holonomic dual of the corresponding *-extension of \(E^{\vee}\), and ambient holonomic duality is exact on modules.

We prove that both \(j_*E\) and \(j_!E\) are curve-tested without claiming their simple factors regular first. Take a smooth proper compactification \(\bar X\) of \(X\). Independently compactify \(U\), close the graph of its map into \(\bar X\), resolve that graph while preserving the smooth open \(U\), and principalize its boundary outside \(U\). The exact compactification and resolution proofs linked in Theorem 5.1 give a smooth proper SNC pair \((P,D)\), with \(P\setminus D=U\), and a proper map
\[
F:P\to\bar X
\tag{5.17f}
\]
extending \(j\). This preserves the smooth connection open only; it makes no claim of identity on a pre-existing SNC crossing. Its image is the closure of \(U\), of dimension \(n\).

Over \(X\), put \(P_X=F^{-1}X\), and \(a:U\hookrightarrow P_X\). By 5.14.2,
\[
j_*E=F_{X,*}a_*E.
\tag{5.17g}
\]
The source is the restriction of the proper SNC module \(Q^+\). For the !-extension, the exact proper duality proper operator-duality, Theorem 4.7 and its definition give
\[
\begin{gathered}
j_!E=\mathbb D_Xj_*E^\vee\\
\simeq F_{X,*}\mathbb D_{P_X}(a_*E^\vee)\\
=F_{X,*}a_!E.
\end{gathered}
\tag{5.17h}
\]
The source is a restriction of the dual SNC module (5.15f). Equation (5.17b), using only \(C_{n-1},P_{n-1}\), proves that both standard modules in (5.17g)–(5.17h) are curve-tested.

Let \(\phi:j_!E\to j_*E\) be the actual canonical boundary map. Its image is \(S\). Both modules restrict to \(E\), and \(\phi\) restricts to its identity; hence its kernel and cokernel are supported on \(\overline U\setminus U\), of dimension at most \(n-1\). Its cone is curve-tested by the triangulated property, and its only cohomology is
\[
\begin{gathered}
H^{-1}\operatorname{Cone}\phi=\ker\phi,\\
H^0\operatorname{Cone}\phi=\operatorname{coker}\phi.
\end{gathered}
\tag{5.17i}
\]
Apply \(C_{n-1}\) to this cone. Its two cohomology modules are regular. The forward part of the lower criterion makes them curve-tested. In the short exact sequence
\[
0\to\ker\phi\to j_!E\to S\to0,
\tag{5.17j}
\]
the first two terms are curve-tested, so triangulated closure makes \(S\) curve-tested. This proves \(R_n\). This argument never assumes subquotient closure of the testing class: it uses the cone with strictly lower support first, and only then the short exact sequence.

Theorem 5.16.1 now proves \(C_n\) for all bounded complexes and every singular support at this dimension. The socle peeling there supplies the same-dimensional converse; it is not imported from a stability statement.

#### Direct images of every regular singular object

Assume \(R_n,C_n\) have just been proved and \(P_{n-1}\) is available. Let \(f:X\to Y\) be arbitrary and let \(S\) be regular simple of support dimension \(n\), with presentation (5.17e). Set \(B=\overline U\setminus U\), a closed subset of \(X\), of dimension at most \(n-1\). The localization triangle on \(X\) is
\[
R\Gamma_BS\longrightarrow S\longrightarrow j_*E\longrightarrow.
\tag{5.17k}
\]
To check this when \(U\) is merely locally closed in \(X\), use the open \(X\setminus B\). There \(U\) is closed in the support, and supported Kashiwara identifies restriction of \(S\) with its closed direct image of \(E\); composing its open direct image gives \(j_*E\). Thus (5.17k) is the ordinary closed-support localization triangle, not an assumed localization triangle for a singular ambient support.

By \(R_n\), \(S\) is curve-tested. 5.14.3 makes \(R\Gamma_BS\) curve-tested. Its support dimension is at most \(n-1\), so \(C_{n-1}\) makes it regular, and \(P_{n-1}\) makes
\(f_*R\Gamma_BS\) regular. For \(n=0\), the boundary is empty and this term is zero.

We prove regularity of
\[
f_*j_*E=(fj)_*E.
\tag{5.17l}
\]
Compactify the graph of the map \(fj:U\to Y\) in a proper SNC model of \(U\) and a smooth proper compactification \(\bar Y\) of \(Y\), resolve while preserving \(U\), and principalize its complement. This yields \((P,D)\) and \(F:P\to\bar Y\) as in the proper-SNC image argument, and composition identifies (5.17l) with
\(F_{Y,*}(Q^+|_{P_Y})\).

If the image dimension is zero or one, 5.14.5 proves this output regular by the full generic Gauss–Manin theorem with arbitrary coefficients, followed by the curve-support simple-factor argument. If its image dimension is at least two, the proper-SNC image argument proves it curve-tested using only \(C_{n-1},P_{n-1}\). Its cohomological supports have dimension at most \(n\): the proper map \(F\) confines them to the closed image of the \(n\)-dimensional proper model, and restriction confines them to its intersection with \(Y\). Therefore \(C_n\) makes this output regular.

Apply \(f_*\) to (5.17k). Its first and third terms have just been proved regular. The regular category is triangulated, so \(f_*S\) is regular. Finite composition series extend this assertion from regular simples to every regular module with the stated support bound. Standard truncation triangles extend it to every bounded regular complex. This proves \(P_n\), completing (5.17a). The argument does not assume the ambient varieties affine, proper or quasi-projective, and never assigns a smooth transfer to a singular fiber product.

#### The full theorem and singular-divisor reconstruction

**Theorem 5.17.** For every map \(f:X\to Y\) of smooth separated finite-type complex varieties, the four algebraic functors
\[
f_*,\quad f_!,\quad f^!,\quad f^*
\tag{5.17m}
\]
preserve bounded regular holonomic complexes. A bounded holonomic complex \(K\) on \(X\) is regular if and only if \(k^!K\) is regular for every map \(k:C\to X\) from a smooth algebraic curve. It is enough to test smooth locally closed curve immersions. Every simple factor and every singular support is included.

**Proof.** Every bounded holonomic complex has a finite maximum support dimension. The complete induction proves \(C_n,P_n,R_n\) at that bound. Thus \(f_*\) preserves regularity and both versions of the curve criterion hold. For inverse image, let \(L\) be regular on \(Y\). For every curve map \(k:C\to X\), inverse composition gives
\[
k^!f^!L=(fk)^!L,
\tag{5.17n}
\]
regular by the forward all-map curve criterion on \(Y\). The already proved arbitrary holonomic inverse theorem makes \(f^!L\) bounded holonomic. The converse criterion on \(X\) now makes it regular. This invokes the criterion only after its support-dimension induction is complete. The independent full regular duality Theorem 5.7, and the definitions
\(f_!=\mathbb D_Y f_*\mathbb D_X\),
\(f^*=\mathbb D_X f^!\mathbb D_Y\), prove the two remaining operations. \(\square\)

**Corollary 5.17.1 (singular boundary reconstruction).** Let \(B\) be any effective Cartier divisor on smooth separated \(Y\), with arbitrary singular reduced support and multiplicities, let \(j:Y\setminus B\hookrightarrow Y\), and let \(E\) be any curve-regular finite-rank connection on its complement. Then \(j_*E\) is regular holonomic and every boundary simple factor is regular. Every module \(N_f\) in 5.14.1 is therefore regular holonomic, with precisely its recorded flat transfer action and degrees.

**Proof.** The connection/regular-holonomic identification makes \(E\) regular. Apply the just-proved direct-image theorem to \(j\). Its affine localization is the degree-zero meromorphic extension, and the Serre definition proves the assertion about every factor. Alternatively 5.14.1 makes \(N_f\) curve-tested and 5.17's now-proved converse applies. This is a consequence of the completed induction, not an input to its SNC dual calculation. \(\square\)

All dimension formulas act on the finitely many open-and-closed pure-dimensional smooth components; connected maps land in one component. Finite component sums cover different component dimensions. The proof preserves every cohomological shift through the transfer formulas, the graph local cohomology formula, (5.15g)'s \([-c]\), and (5.16c)'s \([1-\dim W_0]\). Shifts do not alter regularity and have not been silently changed.

![The residue calculation, lower-support standard cone, socle peeling and ordered induction](assets/full-regularity-induction.png)

*Figure. The top left panel is the exact dual density (5.15e), positive-normal-degree contraction (5.15i), and uncontracted residue complex (5.15g). The top right and central panels show why the standard-extension cone has strictly smaller support before its kernel is removed, (5.17c)–(5.17j). The lower left is the actual integer-valued socle-peeling argument (5.16a)–(5.16f); the lower right is the localization triangle (5.17k). The bottom arrow is the order of proof (5.17a), not an assumption of all three assertions at the current dimension. Source reading: [Bernstein, Algebraic theory of D-modules](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), Main Theorem B. Every mechanism is proved above. The reproducible drawing source supplies the original CC0 figure.*



Write $D^b_{\rm rh}(\mathcal D_X)$ for bounded complexes with regular holonomic cohomology. This is a triangulated subcategory: a composition series for a submodule and quotient concatenates to one for the middle module. Thus regular modules form a Serre subcategory, and the long cohomology sequence of a triangle preserves it.

**Stability and testing (proved).** For a morphism $f:X\to Y$ of smooth separated complex algebraic varieties, the four functors
\[
f_*,\ f_!,\ f^!,\ f^*
\]
of Adjunctions, base change and the projection formula, and holonomic duality $\mathbb D$, preserve the bounded regular holonomic categories. No properness hypothesis is imposed in this algebraic statement. A bounded holonomic complex $M$ on $X$ is regular if and only if $k^!M$ is regular for every map $k:C\to X$ from a smooth algebraic curve. It is enough to test smooth locally closed curves. Theorem 5.17 proves the four-map and both curve-test assertions, in the notation $f^!$ and $f^*$ used here; Theorem 5.7 proves duality preservation. The statements apply to every singular support and bounded complex. The analytic proper direct-image assertion likewise remains a proof obligation; Kashiwara's freely accessible §8 is reading material. Neither citation establishes an input used below.

### External product and both tensor operations

**Theorem 5.18 (external product and the two tensor operations).** External products, $\otimes^!$, and the dual tensor/Hom operation formed using $\mathbb D$ preserve bounded regular holonomic complexes. **Proof.** We use the four-map and curve-test assertions now proved in Theorem 5.17, together with duality preservation in Theorem 5.7. External products of holonomic modules are holonomic: a product good filtration has associated graded the external product of the two associated graded modules, so its characteristic support is the product of the two Lagrangian supports. The dimension is the sum of the dimensions. Derived external products and tensor products are consequently holonomic by bounded dévissage and the already proved inverse-image theorem; the internal tensor is the diagonal inverse image with its dimension shift.

On a curve, two regular holonomic complexes restrict outside finitely many points to complexes of regular connections. A tensor of two regular connections is regular, since tensor products of logarithmic lattices are logarithmic lattices, including at the compactification boundary. Every simple factor supported at an omitted point is a delta module and is regular. The simple-factor description therefore shows that the tensor complex is regular on the whole curve. Restrictions to a dense open detect the positive-dimensional simple factors, and any such factor with nonzero restriction inherits a regular generic connection by the stable sublattice and image argument following (1.5).

For an arbitrary curve map $k:C\to X\times Y$, the transfer-module tensor identity gives
\[
k^!(M\boxtimes N)\simeq
(\operatorname{pr}_X k)^!M\otimes^!
(\operatorname{pr}_Y k)^!N.                                   \tag{5.2}
\]
By Theorem 5.17, both factors are regular, and their tensor is regular by the curve argument. The curve criterion of Theorem 5.17 makes $M\boxtimes N$ regular. Diagonal inverse image then gives regularity of $\otimes^!$ on $X$. Theorem 5.7 then gives the dual tensor/Hom operation formed using $\mathbb D$. This proves the theorem. Recall that for left modules $\otimes^!$ is the derived $\mathcal O_X$ tensor shifted by $[-\dim X]$; shifts do not affect regularity.

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

Theorem 3.3 proves Fuchs's criterion in every order for formal and convergent coefficients. Theorems 5.0 and 5.1 prove canonical logarithmic extensions, the full global algebraic connection/local-system correspondence, the algebraic curve and divisorial tests, and compactification independence. The proper compactification and GAGA inputs have exact earlier programme proofs; the coherent-extension, transverse-family, meromorphic-comparison and logarithmic-jet steps are proved here.

Theorem 5.2 proves the connection/regular-holonomic identification, including presentations on a dense open and the Serre closure of curve-regular connections. Theorem 5.3 proves analytic regularity of every normalized SNC meromorphic bundle with its exact good filtration and characteristic cycle. Theorem 5.4 proves the natural logarithmic and meromorphic de Rham comparisons by convergent Laurent homotopies, fine resolutions and exact cubical periods. Theorem 5.5 proves the full global algebraic de Rham comparison for every curve-regular algebraic connection, including nonproper and non-quasi-projective varieties, by the finite pole-layer and complex-linear GAGA arguments. Theorem 5.6 proves full generic Gauss–Manin regularity on every smooth algebraic base, with arbitrary curve base change, all coefficients and all fibre multiplicities in the curve lattice. Theorem 5.7 proves duality preservation for every regular holonomic module and bounded complex, with every support allowed. Theorem 5.8 proves relative analytic twist generation in every projective dimension for arbitrary coherent sheaves near a projective fibre; Lemma 5.8.2 also proves coherent higher images for projective-line projections. Theorem 5.9 and Lemma 5.9.1 prove locally projective coherent analytic images, with the initial coherent-generator hypothesis explicit for operator modules. Theorem 5.10 proves coherence, boundedness and analytic transported support of the cotangent candidate. Theorems 5.11–5.12 prove the singular-inclusive isotropic dimension bound and the actual output-filtration comparison, hence analytic projective holonomicity with the initial coherent-generator or global good-filtration hypothesis. Constructing that initial generator for every analytic regular holonomic module remains required. Theorem 5.13 proves the algebraic regular-holonomic SNC extension on every proper SNC pair and every open restriction, all boundary simple factors, and all algebraic curve pullbacks of these meromorphic modules. Theorems 5.14–5.17 prove full algebraic four-map regularity and the bounded-complex criterion using all smooth curve maps or only smooth locally closed curve immersions, including every singular support and every smooth separated finite-type ambient variety. Full analytic proper direct-image regularity remains required. Theorem 5.18 proves external-product and both tensor/dual tensor operations using the now-proved four-map and curve criterion. Full analytic proper regularity and the initial global analytic generator remain distinct obligations.

The Stokes description, the irregular Riemann–Hilbert problem and the wild Betti construction are cited perspectives. We prove no formal exponential decomposition, sectorial summation or irregular correspondence theorem. The earlier analytic flat-frame and Cauchy proofs are linked above. The product-growth estimate, removable-pole arguments and category gluing used here have explicit proofs in the lesson.

## References

- Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), freely accessible author notes, Sections 4.2–4.4 and 5.1; the support and dimension reading for Theorem 5.9.
- Norguet, [*Images de faisceaux analytiques cohérents*](https://www.numdam.org/item/SL_1957-1958__1__A7_0.pdf), freely accessible Séminaire Lelong exposition, Section II.1–II.2, printed pp. 11-10–11-14; the projective-line reading for Theorem 5.8.
- Bernstein, [*Algebraic theory of D-modules*](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), lecture notes, the lecture “Holonomic D-modules with regular singularities”: the definition of regular holonomic modules and Main Theorem B, stability under the four functors and duality and the curve criterion.
- Kashiwara, [*The Riemann–Hilbert problem for holonomic systems*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/RiemannHilbert.pdf), Publications of the RIMS 20 (1984), 319–365, §8: regularity of proper direct images of analytic regular holonomic modules.
- Deligne, [*Équations différentielles à points singuliers réguliers*](https://publications.ias.edu/sites/default/files/Number9.pdf), freely accessible IAS-hosted full text, 1970, Chapter II: regularity in dimension one and in higher dimension, the curve and compactification criteria, and the global connection correspondence.
- Schnell, [*Algebraic D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Lectures 20–21: Fuchs's theorem and regular first-order systems, and the regularity-at-infinity examples and definitions.
- Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), §3.5, for the Euler D-module and its scalar solutions.
- Sabbah, [*Introduction to Stokes structures*](https://arxiv.org/abs/0912.2762), Lectures 1–2: Stokes-filtered local systems in dimension one, following Deligne and Malgrange.
- Scholze, [*Wild Betti sheaves*](https://arxiv.org/abs/2505.24599), arXiv:2505.24599, §1, for the exponential and Fourier enlargement and its enhanced-sheaf context.

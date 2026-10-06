# Crossed products and factor systems

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An automorphism of a maximal subfield can be realized by conjugation inside a central simple algebra. Choosing one conjugating unit for each automorphism produces multiplication constants. Associativity constrains those constants, and changing the units changes them by a coboundary. This lesson makes that construction explicit and proves that it describes every Brauer class split by a finite Galois extension.

The prerequisite is [Central simple algebras and the Brauer group](NOE-HYP-04.md). We use its Skolem–Noether theorem, centralizer theorem and finite splitting criterion. Let \(L/K\) be finite Galois, let \(G=\operatorname{Gal}(L/K)\), and put \(n=[L:K]=|G|\). Multiplication in \(G\) means composition: \((\sigma\tau)(x)=\sigma(\tau(x))\). Field automorphisms act on coefficients on the left. Every convention below uses this order.

## 1. Factor systems and the algebra they define

A **normalized factor system**, or multiplicative **2-cocycle**, is a function \(a:G\times G\to L^\times\) satisfying

\[
a(1,\sigma)=a(\sigma,1)=1,
\qquad
a(\sigma,\tau)a(\sigma\tau,\rho)
 =\sigma(a(\tau,\rho))a(\sigma,\tau\rho).
\tag{1}
\]

For a function \(c:G\to L^\times\), \(c_1=1\), its **coboundary** is

\[
(\delta c)(\sigma,\tau)=c_\sigma\,\sigma(c_\tau)c_{\sigma\tau}^{-1}.
\tag{2}
\]

Direct substitution shows that \(\delta c\) satisfies (1). Cocycles form an abelian group under pointwise multiplication, and coboundaries form a subgroup. Their quotient is \(H^2(G,L^\times)\). This defines the second cohomology group needed here without a resolution or a cochain complex.

Define the **crossed product**

\[
A(a)=(L,G,a)=\bigoplus_{\sigma\in G}L u_\sigma
\]

by \(u_1=1\) and

\[
u_\sigma x=\sigma(x)u_\sigma,
\qquad
u_\sigma u_\tau=a(\sigma,\tau)u_{\sigma\tau}.
\tag{3}
\]

More explicitly,

\[
(x u_\sigma)(y u_\tau)
 =x\sigma(y)a(\sigma,\tau)u_{\sigma\tau}.
\]

The two associations of a triple product agree precisely because of (1). Normalization gives the identity. Each \(u_\sigma\) is invertible, since its product with \(u_{\sigma^{-1}}\) is a nonzero scalar; in a finite-dimensional algebra a one-sided inverse is two-sided, as follows by applying injectivity and surjectivity to multiplication.

**Theorem 1.1 (crossed-product structure).** The algebra \(A(a)\) is central simple over \(K\), has dimension \(n^2\), and contains \(L\) as a self-centralizing subfield. In particular it has degree \(n\), and \(L\) splits it.

**Proof.** Its dimension is \(n\dim_K L=n^2\). If \(z=\sum_\sigma x_\sigma u_\sigma\) commutes with every \(y\in L\), then

\[
x_\sigma(\sigma(y)-y)=0
\]

for all \(\sigma,y\). For \(\sigma\ne1\), choose \(y\) moved by \(\sigma\); this forces \(x_\sigma=0\). Thus \(C_{A(a)}(L)=L\). An element \(x\in L\) is central exactly when \(\sigma(x)=x\) for every \(\sigma\), so the centre is \(K\).

Let \(I\) be a nonzero two-sided ideal. Choose \(0\ne z\in I\) with the smallest number of nonzero coefficients in the displayed basis. Multiplication by a suitable unit \(u_\tau\) and a nonzero scalar in \(L\) gives such an element whose identity coefficient is \(1\). For \(y\in L\), the commutator \(zy-yz\) has no identity coefficient. If it were nonzero, it would have smaller support, contradicting minimality. Therefore \(z\) commutes with \(L\), so \(z=1\). Thus \(I=A(a)\). The preceding lesson's finite splitting criterion applies to the self-centralizing field \(L\), proving the last assertion. \(\square\)

Changing generators to \(u'_\sigma=c_\sigma u_\sigma\) changes the factor system to

\[
a'=a\,\delta c.
\tag{4}
\]

Both the coefficient twist in (2) and the inverse on \(c_{\sigma\tau}\) are forced by multiplying the new generators in (3).

## 2. Classification, including the split class

**Theorem 2.1 (classification with a specified subfield).** Crossed products \(A(a)\) and \(A(b)\) are isomorphic by an isomorphism equal to the identity on \(L\) if and only if \([a]=[b]\) in \(H^2(G,L^\times)\). Every central simple \(K\)-algebra of degree \(n\) containing \(L\) is such a crossed product.

**Proof.** In \(A(b)\), the elements \(v\) satisfying \(vx=\sigma(x)v\) for all \(x\in L\) form exactly \(L v_\sigma\). To check this, expand \(v\) in the crossed-product basis; the coefficient of \(v_\tau\), \(\tau\ne\sigma\), must vanish after choosing an \(x\) with \(\tau(x)\ne\sigma(x)\). Consequently an \(L\)-fixed isomorphism has the form \(u_\sigma\mapsto c_\sigma v_\sigma\), with every \(c_\sigma\ne0\). Multiplication gives \(a=b\delta c\). Conversely that formula makes the displayed assignment a multiplicative bijection.

Now let \(A\) be central simple of degree \(n\), containing \(L\). Its centralizer of \(L\) has \(K\)-dimension \(n^2/n=n\) and contains \(L\), so it is \(L\). Skolem–Noether supplies a unit \(u_\sigma\) with

\[
u_\sigma x u_\sigma^{-1}=\sigma(x),
\]

and we choose \(u_1=1\). The units \(u_\sigma u_\tau\) and \(u_{\sigma\tau}\) induce the same automorphism of \(L\). Their quotient lies in its centralizer, so \(u_\sigma u_\tau=a(\sigma,\tau)u_{\sigma\tau}\) for a nonzero \(a(\sigma,\tau)\in L\). Associativity gives (1).

The \(u_\sigma\) are linearly independent over \(L\). Otherwise choose a relation \(\sum_\sigma x_\sigma u_\sigma=0\) with minimal nonempty support. It cannot have just one term. Fix an index \(\tau\) in the support, multiply the relation on the right by \(y\in L\), and subtract \(\tau(y)\) times the original relation. The \(\tau\)-term disappears, while some other term remains for a suitable \(y\), because distinct automorphisms differ somewhere. This contradicts minimality. There are \(n\) independent units and \(\dim_L A=n\), so they form a basis. Thus the relations identify \(A\) with \(A(a)\). \(\square\)

The same minimal-relation argument proves **independence of distinct field automorphisms** as functions \(L\to L\): in a supposed relation \(\sum x_\sigma\sigma(z)=0\) holding for every \(z\), compare its values on \(yz\) with \(\tau(y)\) times its values on \(z\). We will use this fact again in Galois descent.

**Theorem 2.2 (the split class).** The crossed product \(A(a)\) is split if and only if \(a=\delta c\) for some \(c:G\to L^\times\). For the trivial factor system,

\[
A(1)\xrightarrow{\sim}\operatorname{End}_K(L),
\qquad x u_\sigma\longmapsto(z\mapsto x\sigma(z)).
\]

**Proof.** If \(a=\delta c\), send \(u_\sigma\) to \(z\mapsto c_\sigma\sigma(z)\) and let \(L\) act by multiplication. Equation (2) makes this a unital algebra homomorphism. It is injective by Theorem 1.1 and surjective by dimension \(n^2\). Taking \(c_\sigma=1\) gives the displayed map.

Conversely, write a split \(A(a)\) as \(\operatorname{End}_K(V)\), \(\dim_K V=n\). Its embedded field \(L\) makes \(V\) a one-dimensional \(L\)-vector space. Choose a basis and identify \(V=L\). The relation with \(L\) says that \(u_\sigma\) acts as \(z\mapsto c_\sigma\sigma(z)\), where \(c_\sigma\ne0\). Comparing products gives \(c_\sigma\sigma(c_\tau)=a(\sigma,\tau)c_{\sigma\tau}\), which is exactly \(a=\delta c\). \(\square\)

## 3. Multiplication in the relative Brauer group

The relative group \(\operatorname{Br}(L/K)\) consists of Brauer classes over \(K\) which become split over \(L\). To identify its group law, we must calculate a tensor product, not just classify single algebras.

**Lemma 3.1 (tensor compatibility).** For normalized factor systems \(a,b\),

\[
A(a)\otimes_K A(b)\sim A(ab).
\]

**Proof.** Put \(T=A(a)\otimes_K A(b)\), and distinguish the bases \(u_\sigma,v_\sigma\) of its two factors. The subalgebra \(L\otimes_K L\) decomposes as

\[
L\otimes_K L\xrightarrow{\sim}\prod_{g\in G}L,
\qquad x\otimes y\longmapsto(xg(y))_g.
\tag{5}
\]

For completeness, choose a primitive element \(\theta\) of the separable extension. Then \(L\otimes_K L=L[T]/(f(T))\), where \(f\) is its minimal polynomial. Over \(L\), the distinct roots \(g(\theta)\) factor \(f\) into relatively prime linear factors. The Chinese remainder theorem gives (5).

Let \(e_g\) be the idempotent with coordinate \(1\) at \(g\) and \(0\) elsewhere, and put \(e=e_1\). Conjugation by \(u_\sigma\otimes v_\tau\) sends \(e\) to \(e_{\sigma\tau^{-1}}\). Indeed, the \(g\)-coordinate of the conjugated coefficient is

\[
\sigma(x)g(\tau(y))
 =\sigma\bigl(x(\sigma^{-1}g\tau)(y)\bigr),
\]

which is nonzero on the identity idempotent exactly when \(g=\sigma\tau^{-1}\). Consequently the corner \(eTe\) has only the diagonal basis terms

\[
w_\sigma=e(u_\sigma\otimes v_\sigma)e.
\]

The coefficient algebra \((L\otimes_K L)e\) is \(L\), with \(x\otimes y\) acting as \(xy\). The diagonal units commute with \(e\), twist this coefficient by \(\sigma\), and satisfy

\[
w_\sigma w_\tau=a(\sigma,\tau)b(\sigma,\tau)w_{\sigma\tau}.
\]

They form an \(L\)-basis of the corner: all terms with \(\sigma\ne\tau\) vanish between the two \(e\)'s, and the diagonal terms retain their distinct tensor-basis coordinates. Thus \(eTe\simeq A(ab)\).

Finally, a nonzero idempotent corner of a simple Artinian algebra is similar to that algebra. If \(T=M_r(D)\), its idempotent is a projection on the right \(D\)-space \(D^r\); a basis of its image and kernel conjugates it to \(\operatorname{diag}(I_s,0)\), \(s>0\). Its corner is \(M_s(D)\), which has the same division representative. Applying this observation to \(e\) proves the lemma. \(\square\)

**Theorem 3.2 (relative Brauer group).** There is a group isomorphism

\[
H^2(G,L^\times)\xrightarrow{\sim}\operatorname{Br}(L/K),
\qquad [a]\longmapsto[A(a)].
\]

**Proof.** Theorem 2.1 makes the map well defined, Theorem 1.1 places its image in the relative group, and Lemma 3.1 makes it a homomorphism. Theorem 2.2 identifies its kernel with the zero cohomology class. For surjectivity, let \([A]\) be split by \(L\). The finite splitting criterion in the preceding lesson constructs an algebra \(A'\sim A\), of degree \(n\), containing \(L\). Theorem 2.1 makes \(A'\) a crossed product. \(\square\)

## 4. Cyclic algebras and a cubic example

Suppose \(G=\langle\sigma\rangle\) is cyclic of order \(n\). For \(t\in K^\times\), define

\[
(L/K,\sigma,t)=L\oplus Lu\oplus\cdots\oplus Lu^{n-1},
\qquad ux=\sigma(x)u,\quad u^n=t.
\]

This is the crossed product of the cocycle

\[
a_t(\sigma^i,\sigma^j)=
\begin{cases}1,&i+j<n,\\t,&i+j\ge n,\end{cases}
\qquad 0\le i,j<n.
\]

The cocycle relation counts the same total number of carries in adding three indices. The factor \(t\) is fixed by \(G\), so its coefficient twist is harmless.

**Theorem 4.1 (cyclic second cohomology).** With the specified generator \(\sigma\),

\[
K^\times/N_{L/K}(L^\times)\xrightarrow{\sim}H^2(G,L^\times),
\qquad t\longmapsto[a_t].
\]

**Proof.** In any crossed product, put \(u=u_\sigma\). The element \(u^n\) commutes with \(L\), so belongs to \(L^\times\); it also commutes with \(u\), so is fixed by \(\sigma\), and hence belongs to \(K^\times\). The basis \(1,u,\ldots,u^{n-1}\) differs from the original basis by nonzero coefficients. Thus every cocycle is cohomologous to some \(a_t\).

An \(L\)-fixed isomorphism between two cyclic algebras sends \(u\) to \(cv\), since this is the \(\sigma\)-twisted eigenspace. Then

\[
(cv)^n=c\sigma(c)\cdots\sigma^{n-1}(c)\,v^n
 =N_{L/K}(c)t'.
\]

Therefore \(t\) and \(t'\) define the same class precisely when \(t/t'\) is a norm. Pointwise multiplication gives \(a_ta_{t'}=a_{tt'}\), so the bijection is a group isomorphism. \(\square\)

For a quadratic extension \(L=K(\sqrt d)\), \(\operatorname{char}K\ne2\), the relations with \(i=\sqrt d\), \(j=u\) are \(i^2=d\), \(j^2=t\), \(ji=-ij\). Thus the cyclic algebra is \((d,t)_K\). For \(\mathbb C/\mathbb R\), norms are the positive real numbers, and the quotient \(\mathbb R^\times/\mathbb R_{>0}\) has two elements. Positive \(t\) gives \(M_2(\mathbb R)\), while negative \(t\) gives \(\mathbb H\).

A degree-three example over \(\mathbb Q\) can also be checked without local class field theory. Let \(\zeta\) be a primitive seventh root of unity and \(\theta=\zeta+\zeta^{-1}\). Then

\[
f(\theta)=0,\qquad f(T)=T^3+T^2-2T-1.
\]

The polynomial has no rational root, so \(L=\mathbb Q(\theta)\) has degree \(3\). Its other roots are \(\theta^2-2\) and \(1-\theta-\theta^2\), as follows by expressing \(\zeta^2+\zeta^{-2}\) and \(\zeta^4+\zeta^{-4}\). All lie in \(L\). Thus \(L/\mathbb Q\) is cyclic, with \(\sigma(\theta)=\theta^2-2\), and \(\sigma^2(\theta)=1-\theta-\theta^2\).

Consider \(A=(L/\mathbb Q,\sigma,2)\). It has the explicit nine-element basis \(\theta^i u^j\), \(0\le i,j<3\), with

\[
\theta^3=-\theta^2+2\theta+1,\qquad
u\theta=(\theta^2-2)u,\qquad u^3=2.
\]

The number \(2\) is not a norm from \(L\). To prove this, let \(R=\mathbb Z_{(2)}[\theta]\), where \(\mathbb Z_{(2)}\) consists of rationals with odd denominator. It is free over \(\mathbb Z_{(2)}\) with basis \(1,\theta,\theta^2\). Modulo \(2\), the polynomial is \(T^3+T^2+1\); it has no root in \(\mathbb F_2\), so \(R/2R\) is a field of eight elements. For \(y\in R\setminus2R\), multiplication by \(y\) is invertible modulo \(2\). Its determinant, which is \(N_{L/\mathbb Q}(y)\), has 2-adic valuation zero.

Every \(x\in L^\times\) can be written \(x=2^r y\) with \(r\in\mathbb Z\) and \(y\in R\setminus2R\): take the minimum of the three 2-adic valuations of its rational basis coefficients. Consequently

\[
v_2(N_{L/\mathbb Q}(x))=3r.
\]

It cannot equal \(v_2(2)=1\). Theorem 4.1 therefore makes \(A\) nonsplit. Its degree is \(3\), so its division representative has degree \(3\), and \(A\) itself is division. Replacing the parameter by \(8=N_{L/\mathbb Q}(2)\) gives a split degree-three algebra. This computes both a nontrivial and a trivial class for the same splitting extension.

## 5. Matrix units in a split crossed product

Choose a \(K\)-basis \(\alpha_1,\ldots,\alpha_n\) of \(L\). The trace pairing \(\operatorname{Tr}_{L/K}(xy)\) is nondegenerate. Here is a direct check: use a primitive-element basis \(1,\theta,\ldots,\theta^{n-1}\); the matrix of its embeddings is Vandermonde on the distinct \(\sigma(\theta)\). The Gram matrix of the trace pairing is the transpose of that matrix times itself, so its determinant is the square of a nonzero Vandermonde determinant. This works in every characteristic, even when \(\operatorname{Tr}(1)=n=0\).

Let \(\beta_1,\ldots,\beta_n\) be the trace-dual basis, so \(\operatorname{Tr}(\beta_j\alpha_i)=\delta_{ji}\). In \(A(1)\), define

\[
e_{ij}=\alpha_i\sum_{\sigma\in G}\sigma(\beta_j)u_\sigma.
\tag{6}
\]

Under Theorem 2.2 this acts on \(L\) by

\[
x\longmapsto\alpha_i\operatorname{Tr}_{L/K}(\beta_jx).
\]

It sends \(\alpha_h\) to \(\delta_{jh}\alpha_i\). Thus

\[
e_{ij}e_{h\ell}=\delta_{jh}e_{i\ell},\qquad
\sum_i e_{ii}=1.
\]

These are actual matrix units, not just a dimension argument for splitting. For a coboundary \(a=\delta c\), the generators \(c_\sigma^{-1}u_\sigma\) have trivial factor system, and substituting them in (6) gives the matrix units in \(A(a)\). This realizes the complementary-basis construction in Noether's work on split crossed products.

## 6. Projective descent, inflation and period

A second description of Brauer classes uses projective semilinear actions on a splitting module. An explicit comparison prevents a sign convention from entering unnoticed.

**Lemma 6.1 (projective-action comparison).** Let \(M/K\) be finite Galois with group \(H\). Let \(V\ne0\) be a finite-dimensional \(M\)-space, with invertible \(\gamma\)-semilinear operators \(T_\gamma\), \(T_1=1\), such that

\[
T_\gamma T_\delta=c(\gamma,\delta)T_{\gamma\delta},
\qquad c(\gamma,\delta)\in M^\times.
\]

Then \(c\) is a normalized cocycle. The fixed algebra

\[
B=\{F\in\operatorname{End}_M(V):T_\gamma F T_\gamma^{-1}=F\text{ for all }\gamma\}
\]

is central simple over \(K\), with \([B]=-[A(c)]\).

**Proof.** Associating a triple product of the \(T\)'s gives (1), including the coefficient action \(\gamma(c(\delta,\epsilon))\) from semilinearity. The field \(M\), acting by scalars, and the operators \(T_\gamma\) make the underlying \(K\)-space of \(V\) a unital left \(A(c)\)-module. The endomorphisms of this module are exactly the \(M\)-linear maps commuting with all the \(T_\gamma\), namely \(B\). If \(A(c)=M_r(D)\), the module is \((D^r)^s\) for some \(s>0\). Its endomorphism algebra is \(M_s(D^{\mathrm{op}})\), central simple with class \(-[D]=-[A(c)]\). \(\square\)

For \(A=A(a)\), regard \(A\) as a right \(L\)-space and use the splitting model

\[
A\otimes_K L\simeq\operatorname{End}_L(A),
\qquad x\otimes\ell\longmapsto(z\mapsto xz\ell).
\]

Set \(T_\sigma(z)=z u_\sigma^{-1}\). The identity \(\ell u_\sigma^{-1}=u_\sigma^{-1}\sigma(\ell)\) proves semilinearity, and

\[
T_\sigma T_\tau(z)
 =z(u_\sigma u_\tau)^{-1}
 =z u_{\sigma\tau}^{-1}a(\sigma,\tau)^{-1}.
\tag{7}
\]

Thus the projective multiplier on this splitting module is \(a^{-1}\). Conjugation by \(T_\sigma\) fixes left multiplication by \(A\) and sends the right scalar \(\ell\) to \(\sigma(\ell)\). Its fixed endomorphism algebra is precisely the left copy of \(A\), as is also seen by taking a \(K\)-basis of \(A\) in the displayed tensor product and fixing its scalar coefficients.

In a chosen \(L\)-basis, write \(T_\sigma=P_\sigma\sigma\), where \(\sigma\) acts entrywise. Equation (7) becomes

\[
P_\sigma\sigma(P_\tau)P_{\sigma\tau}^{-1}
 =a(\sigma,\tau)^{-1}I_n.
\tag{8}
\]

The images \(\overline P_\sigma\) in \(\operatorname{PGL}_n(L)\) therefore satisfy the 1-cocycle relation. Formula (8) compares the usual matrix-lift connecting multiplier with our factor system: in this right-module splitting model it is the inverse. A geometric proof using forms of a matrix algebra must specify its model and connecting-map convention before identifying the two classes. This is the comparison needed with the separate planned lesson *Brauer groups and Tsen's theorem*.

**Proposition 6.2 (inflation).** If \(M/K\) is finite Galois and contains \(L\), a cocycle \(a\) inflates to

\[
\widetilde a(\gamma,\delta)
 =a(\gamma|_L,\delta|_L)\in M^\times.
\]

The crossed products represent the same class over \(K\): \([A(\widetilde a)]=[A(a)]\).

**Proof.** Put \(V=A(a)\otimes_L M\), using the right \(L\)-space just considered. For \(\sigma=\gamma|_L\), set

\[
T_\gamma(x\otimes z)=x u_\sigma^{-1}\otimes\gamma(z).
\]

It respects the balanced tensor relation because

\[
(x\ell)u_\sigma^{-1}\otimes\gamma(z)
 =xu_\sigma^{-1}\otimes\sigma(\ell)\gamma(z).
\]

These operators are invertible and \(\gamma\)-semilinear, with multiplier \(\widetilde a^{-1}\) by (7). Moreover \(\operatorname{End}_M(V)=A(a)\otimes_K M\), and their conjugation action fixes the first factor and acts on scalar coefficients by \(\gamma\). The fixed algebra is \(A(a)\). Lemma 6.1 gives

\[
[A(a)]=-[A(\widetilde a^{-1})]=[A(\widetilde a)],
\]

where the last equality uses the group law already proved in Theorem 3.2. \(\square\)

Let \(K^{\mathrm{sep}}\) be a separable closure and \(G_K\) its absolute Galois group, with the topology defined by its finite Galois quotients. Give \((K^{\mathrm{sep}})^\times\) the discrete topology and define continuous \(H^2\) using continuous cocycles and coboundaries with the same formulas (1)–(2). Then

\[
\operatorname{Br}(K)\simeq
H^2_{\mathrm{cont}}(G_K,(K^{\mathrm{sep}})^\times).
\tag{9}
\]

Here is the passage from the finite theorem. A continuous cochain on a finite power of the compact profinite group has finite image. A finite clopen cover on which it is constant can be refined by cosets of one open normal subgroup in each coordinate. Shrink this subgroup further to fix every value. The cochain then factors through a finite Galois quotient and has values in that quotient's fixed field. The same argument applies to a cochain giving a coboundary. Thus continuous second cohomology is the direct limit of the finite groups \(H^2(\operatorname{Gal}(M/K),M^\times)\), with the inflation maps above. Every Brauer class has a finite Galois splitting field by the preceding lesson. The compatible finite isomorphisms in Theorem 3.2 consequently identify the two direct limits, proving (9).

The **period** of a Brauer class is its order in the group; its **index** is the degree of its division representative.

**Theorem 6.3 (period divides index).** Every Brauer class has finite period, and its period divides its index.

**Proof.** Let \(D\) be its division representative, of degree \(d\), and choose a finite Galois splitting field \(M/K\), with group \(H\). Transport the canonical coefficient action on \(D\otimes_K M\) to \(M_d(M)\). For \(\gamma\in H\), the transported automorphism is semilinear. Composing it with entrywise \(\gamma^{-1}\) gives an \(M\)-linear automorphism, hence an inner one by Skolem–Noether. Thus the transported action has the form

\[
X\longmapsto P_\gamma\gamma(X)P_\gamma^{-1}.
\]

Choose \(P_1=I_d\). The action law forces

\[
c(\gamma,\delta)I_d
 =P_\gamma\gamma(P_\delta)P_{\gamma\delta}^{-1},
\]

since a matrix inducing trivial conjugation is scalar. The semilinear operators \(T_\gamma=P_\gamma\gamma\) on \(M^d\) have this multiplier. Their fixed endomorphism algebra is \(D\), because the transported action was the canonical coefficient action. Lemma 6.1 gives \([D]=-[A(c)]\). Taking determinants gives

\[
c(\gamma,\delta)^d
 =\det(P_\gamma)\,\gamma(\det P_\delta)\,\det(P_{\gamma\delta})^{-1}.
\]

Thus \(c^d\) is a coboundary. Theorem 3.2 yields \(d[A(c)]=0\), hence \(d[D]=0\). The order of \([D]\) therefore divides \(d\). \(\square\)

There is also a restriction–corestriction route to this conclusion. The group-cohomology transfer theorem states that for a subgroup \(H\le G\) of finite index \(s\), with coefficient \(G\)-module \(M\), the composite \(\operatorname{Cor}\operatorname{Res}\) on \(H^q(G,M)\) is multiplication by \(s\), for every \(q\ge0\) [Milne CFT, Chapter II]. Choose a separable maximal subfield of \(D\), of degree \(d\), and a finite Galois closure which splits it. Restriction of the Brauer class to that subfield is zero; applying this identity gives \(d[D]=0\). We stated the transfer identity with its source; the determinant proof above supplies the divisibility result without importing the construction of corestriction.

## 7. The arithmetic boundary: maximal orders

The complementary-basis calculation also enters Noether's arithmetic theory of orders. The following statement applies to split algebras of every matrix size.

Let \(R\) be a Dedekind domain with fraction field \(K\). A **full lattice** in \(K^n\) is a finitely generated \(R\)-submodule spanning \(K^n\). An **order** in \(M_n(K)\) is a unital \(R\)-subalgebra which is a full \(R\)-lattice in that algebra. It is maximal if no larger order contains it.

**Proposition 7.1 (orders in a split algebra).** Every maximal \(R\)-order in \(M_n(K)\) has the form \(\operatorname{End}_R(P)\) for a full lattice \(P\subset K^n\). Conversely, every such endomorphism ring is a maximal order.

**Proof, using the Dedekind lattice facts stated below.** If \(\Lambda\) is an order, set \(P=\Lambda R^n\). Finite generation of \(\Lambda\) makes \(P\) a full lattice, stable under \(\Lambda\). Thus \(\Lambda\subseteq\operatorname{End}_R(P)\); the latter is an order since \(P\) is finite projective and spans \(K^n\). Maximality of \(\Lambda\) forces equality.

For the converse, localize at a nonzero maximal ideal \(\mathfrak p\). The lattice \(P_\mathfrak p\) is free of rank \(n\) over the discrete valuation ring \(R_\mathfrak p\), so its endomorphism ring is \(M_n(R_\mathfrak p)\) after choosing a basis. This order is maximal. In fact, let \(\Gamma\) be an order containing it, and let \(X\in\Gamma\). For each matrix entry \(x_{ij}\), multiplication by matrix units puts \(x_{ij}E_{ii}\) in \(\Gamma\). Since \(\Gamma\) is finite free over the discrete valuation ring, Cayley–Hamilton applied to left multiplication by this element gives a monic polynomial relation for it. Its \(ii\)-entry gives that same monic relation for \(x_{ij}\). The discrete valuation ring is integrally closed, so every \(x_{ij}\) lies in \(R_\mathfrak p\). This proves the local maximality.

Any global order containing \(\operatorname{End}_R(P)\) consequently has the same localization at every nonzero maximal ideal. Full lattices over a Dedekind domain are recovered by intersecting those localizations inside their ambient \(K\)-space. The two orders therefore agree. \(\square\)

The imported Dedekind facts are that finite torsion-free modules are projective, their localizations at nonzero maximal ideals are free over discrete valuation rings, endomorphism rings commute with these localizations, and a full lattice is the intersection of its localizations. These are commutative ideal theory, additional prerequisites for this arithmetic section. The statement does not say that every lattice is globally free or that all maximal orders are globally conjugate. Noether treats these issues for number-field orders in [Noether, work 42, §§II–III]. The global theorem that division algebras over number fields admit cyclic maximal subfields requires further arithmetic input; the elementary cubic example in section 4 does not use it.

## 8. Exercises

**Exercise 8.1 (easy).** Show directly that \(A(1)\) acts faithfully on \(L\), and identify it with \(\operatorname{End}_K(L)\). Construct its matrix units from a basis and its trace-dual basis.

**Exercise 8.2 (medium).** Prove that \(A(a)\) is simple by taking an element of a nonzero ideal with minimal support in the crossed-product basis. Explain why the argument works when the characteristic divides \(|G|\).

**Exercise 8.3 (medium).** For \(L=K(\sqrt d)\), \(\operatorname{char}K\ne2\), identify the cyclic crossed product with parameter \(t\) as the quaternion algebra \((d,t)_K\). Determine its split class by the norm criterion.

**Exercise 8.4 (medium).** Prove the cyclic classification \(H^2(G,L^\times)\simeq K^\times/N_{L/K}(L^\times)\), including its group law. For the cubic field in section 4, explain why parameter \(2\) gives a division algebra and parameter \(8\) gives a matrix algebra.

**Exercise 8.5 (hard).** Prove \(A(a)\otimes_K A(b)\sim A(ab)\) by the identity-coordinate idempotent in \(L\otimes_K L\). Compute which tensor-basis terms survive in the corner and justify why the corner has the same Brauer class as the full algebra.

## 9. Solutions

**Solution 8.1.** Let \(x u_\sigma\) act as the map \(z\mapsto x\sigma(z)\). Its product with \(y u_\tau\) acts as \(z\mapsto x\sigma(y)(\sigma\tau)(z)\), so this is an algebra representation. If \(\sum_\sigma x_\sigma\sigma(z)=0\) for all \(z\), choose a nonzero such relation of minimal support. Comparing its value at \(yz\) with \(\tau(y)\) times its value at \(z\) removes its \(\tau\)-term and retains a different term for a suitable \(y\), contradicting minimality. Thus the representation is faithful. Both algebras have dimension \(n^2\), giving surjectivity. For a basis \(\alpha_i\) and trace-dual basis \(\beta_j\), the element \(\alpha_i\sum_\sigma\sigma(\beta_j)u_\sigma\) sends \(\alpha_h\) to \(\delta_{jh}\alpha_i\). These are the matrix units, with product \(e_{ij}e_{h\ell}=\delta_{jh}e_{i\ell}\) and sum of diagonal units \(1\).

**Solution 8.2.** Take \(0\ne z\) in an ideal \(I\) with minimal support. Right multiplication by a basis unit moves a nonzero coefficient into the identity position. Left multiplication by a nonzero field scalar normalizes it to \(1\). For \(x\in L\), the commutator \(zx-xz\) has zero identity coefficient, so minimality makes it zero. Its \(\sigma\)-coefficient is \(z_\sigma(\sigma(x)-x)\); for \(\sigma\ne1\), some \(x\) has a nonzero difference. Hence all other coefficients vanish, and \(z=1\). Thus \(I=A(a)\). No averaging or division by \(|G|\) occurs: only nonzero elements of the field and the basis units are inverted. The proof is valid in every characteristic.

**Solution 8.3.** Put \(i=\sqrt d\) and \(j=u\). The nontrivial automorphism sends \(i\) to \(-i\), so the relations are \(i^2=d\), \(j^2=t\), and \(ji=-ij\). The basis \(1,i,j,ij\) gives an isomorphism with \((d,t)_K\). Replacing \(j\) by \(cj\), \(c\in L^\times\), changes its square to \(N(c)t\). Thus the class is trivial exactly when \(t\) is a norm. Equivalently, if \(t=N(c)\), represent \(i\) by multiplication on \(L\) and \(j\) by \(z\mapsto c\overline z\); the resulting algebra is \(\operatorname{End}_K(L)\). Conversely a split representation is one-dimensional over \(L\), so \(j\) has this semilinear form and its square is a norm.

**Solution 8.4.** In an arbitrary cocycle algebra let \(u=u_\sigma\). Its powers are nonzero scalar multiples of the original \(u_{\sigma^i}\), so they give a basis. Since \(u^n\) centralizes \(L\) and commutes with \(u\), it is a parameter \(t\in K^\times\). An \(L\)-fixed isomorphism sends \(u\) to \(cv\), whose \(n\)-th power is \(N(c)t'\). Hence the classes of parameters are exactly \(K^\times/N(L^\times)\). The standard cocycle has a factor \(t\) precisely at a carry in adding two exponents, so multiplying cocycles multiplies parameters; this verifies the group law.

For the cubic field, \(\mathbb Z_{(2)}[\theta]/2\) is \(\mathbb F_8\), since \(T^3+T^2+1\) is irreducible over \(\mathbb F_2\). If \(x=2^r y\) has integral basis coefficients with at least one odd coefficient in \(y\), multiplication by \(y\) is invertible modulo \(2\). Its norm is therefore a 2-adic unit, and \(v_2(N(x))=3r\). The parameter \(2\), of valuation \(1\), is not a norm. Its cyclic algebra is nonsplit and, because its degree is prime \(3\), is division. The parameter \(8\) is \(N(2)\), so its algebra splits; in the split model its generator acts as \(z\mapsto2\sigma(z)\), whose cube is multiplication by \(8\).

**Solution 8.5.** Use \(L\otimes_K L=\prod_g L\), with coordinate maps \(x\otimes y\mapsto xg(y)\), and take \(e=e_1\). Conjugation by \(u_\sigma\otimes v_\tau\) sends \(e\) to \(e_{\sigma\tau^{-1}}\): its \(g\)-coordinate is the \(\sigma^{-1}g\tau\)-coordinate before conjugation, acted on by \(\sigma\). The idempotents are orthogonal, so

\[
e(u_\sigma\otimes v_\tau)e=0\quad\text{unless }\sigma=\tau.
\]

For \(\sigma=\tau\), the tensor unit commutes with \(e\). The coefficient corner \((L\otimes L)e\) is \(L\), and the surviving units \(w_\sigma=e(u_\sigma\otimes v_\sigma)e\) satisfy

\[
w_\sigma x=\sigma(x)w_\sigma,
\qquad w_\sigma w_\tau=(ab)(\sigma,\tau)w_{\sigma\tau}.
\]

They are independent in their distinct tensor-basis coordinates and span the corner, making it \(A(ab)\). If the full simple algebra is \(M_r(D)\), a basis adapted to the image and kernel of its nonzero idempotent makes the corner \(M_s(D)\), \(s>0\). Thus its division representative, and hence its Brauer class, is unchanged. This proves the required similarity.

## Sources and further reading

- **[Noether]** Emmy Noether, *Zerfallende verschränkte Produkte und ihre Maximalordnungen*, Actualités scientifiques et industrielles **148** (1934), 5–15, especially §I on matrix units and complementary bases and §§II–III on orders. This is work 42 in *Gesammelte Abhandlungen / Collected Papers*. The [English collected edition](https://github.com/KokunoYumeto/emmy-noether-en) supplies a companion reading text. The independently written arguments here use the left-coefficient convention (3).
- **[MIT]** *Noncommutative Algebra*, MIT OpenCourseWare 18.706, Spring 2023, §§15–17 for group cohomology, the Brauer description and projective forms. See the [lecture notes](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/pages/lecture-notes/). The explicit semilinear products (7)–(8) keep the coefficient action visible.
- **[Milne CFT]** J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), course notes: Chapter II for cocycles and restriction–corestriction, and Chapter IV for the Brauer group and the connecting map attached to matrix and projective groups. The geometric formulation is a further reading path; the finite crossed-product isomorphism is proved directly above.

The next lesson, *Hilbert 90 in Noether's form and Galois descent*, proves that semilinear actions with trivial multiplier descend to vector spaces over the ground field. It also explains why the matrix 1-cocycles in the projective comparison become a complete descent description.

## What this lesson does not prove

The finite Galois and primitive-element facts used in (5), the usual compactness of the absolute Galois group, and the Dedekind lattice facts stated in section 7 are prerequisites. The restriction–corestriction transfer identity is stated with Proposition 3.3.7 as its locator; its general construction is not proved here. The period–index divisibility has its independent determinant proof above. We do not prove the local–global classification of number-field Brauer groups, global cyclicity of division algebras over number fields, or geometric results such as Tsen's theorem. All six finite crossed-product and relative-Brauer assertions, the inflation compatibility, the continuous second-cohomology identification, and the five exercise solutions are proved in the lesson.

# Bernstein–Sato polynomials

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Differentiating $x^{s+1}$ produces $(s+1)x^s$. For a general polynomial $f$, a suitable differential operator still lowers the formal exponent by one, but the scalar factor becomes a polynomial in $s$. The smallest such scalar factor is the Bernstein–Sato polynomial. Its existence follows from a growth estimate and finite length, even when no useful operator is apparent. The same estimate proves that allowing arbitrary powers of $f$ in denominators preserves holonomicity.

Throughout, $k$ has characteristic zero, $R=k[x_1,\ldots,x_n]$, $A=A_n(k)$, and $0\ne f\in R$. Put $d=\deg f$ and $R_f=R[f^{-1}]$. Modules are left modules. The prerequisite is The Bernstein filtration and holonomic modules over the Weyl algebra: we use Bernstein's inequality, positive integral multiplicity, and finite length. No analytic correspondence is needed for the existence theorem or localization.

## 1. Giving meaning to the exponent

The notation $f^s$ initially means a basis symbol, not a choice of logarithm. Define the free rank-one $R_f[s]$-module

\[
\mathcal L_s=R_f[s]\,e_s,\qquad e_s=f^s.
\]

Let $s$ commute with $A$. Coordinates act by multiplication, and derivatives act by

\[
\partial_i(g e_s)=
\left(\partial_i g+s\,g\frac{\partial_i f}{f}\right)e_s.
\tag{1.1}
\]

This defines an $A[s]$-module. The commutator with $x_j$ is $\delta_{ij}$ by the product rule. The derivative operators commute: writing $a_i=(\partial_i f)/f$, their commutator is multiplication by $s(\partial_i a_j-\partial_j a_i)$, which is zero because

\[
\partial_i a_j=\frac{f\,\partial_i\partial_j f-(\partial_i f)(\partial_j f)}{f^2}
=\partial_j a_i.
\]

For every integer $r$ write $f^{s+r}=f^r e_s$. Thus

\[
\partial_i(g f^{s+r})=
(\partial_i g)f^{s+r}
+(s+r)g(\partial_i f)f^{s+r-1}.
\tag{1.2}
\]

The cyclic submodule $A[s]e_s$ need not equal the ambient module $\mathcal L_s$. For $f=x$, specialize $s=0$: the cyclic submodule maps to $A_1\cdot1=k[x]$, while the ambient module maps to $k[x,x^{-1}]$. In particular $x^{-1}e_s$ cannot belong to $A_1[s]e_s$. We will work in the ambient module and construct an identity relating two of its cyclic submodules.

Now extend the coefficient field to

\[
K=k(s),\qquad A_K=K\otimes_k A,\qquad
\mathcal L_K=K[x,f^{-1}]e_s.
\tag{1.3}
\]

This is localization in the central parameter $s$, separate from localization in $f$. The map $\mathcal L_s\to\mathcal L_K$ is injective, since $\mathcal L_s$ has no $k[s]$-torsion.

## 2. A growth criterion without a good filtration

We first close a finite-generation issue. An exhaustive filtration with a small dimension bound is useful even if it is not known to be good.

### Lemma 2.1. Bounded holonomic growth

Let $L$ be an arbitrary $A_n(k)$-module with an exhaustive increasing filtration $F_pL$, $p\geq0$, such that

\[
B_aA_n\,F_bL\subseteq F_{a+b}L,\qquad
\dim_kF_pL\leq C p^n+O(p^{n-1}).
\tag{2.1}
\]

Then $L$ is finitely generated and holonomic, and

\[
e(L)\leq n!C,\qquad \operatorname{length}L\leq n!C.
\tag{2.2}
\]

The zero module is included.

**Proof.** Let $N\subseteq L$ be a finitely generated nonzero submodule. Choose a finite generating space $V\subseteq F_aL$. Its good Bernstein filtration $B_pV$ satisfies $B_pV\subseteq F_{p+a}L$. Thus $d(N)\leq n$, and Bernstein's inequality gives $d(N)=n$. Comparing leading coefficients gives the positive integer bound $e(N)\leq n!C$. Its length is at most $e(N)$ by the preceding chapter.

If $L\ne0$, there are nonzero finitely generated submodules, and their multiplicities are positive integers in a bounded set. Choose one, $N$, with largest multiplicity. For any $v\in L$, the submodule $N'=N+Av$ is finitely generated and hence holonomic by the argument just given. If $N'\ne N$, its nonzero holonomic quotient has positive multiplicity, so

\[
e(N')=e(N)+e(N'/N)>e(N),
\]

contradicting maximality. Consequently $v\in N$ for every $v$, and $L=N$. This proves finite generation, holonomicity, and both bounds. $\square$

This argument uses multiplicity on the finite submodules before asserting that the ambient module is finite. It does not apply a Noetherian or finite-length conclusion prematurely.

### Proposition 2.2. The generic formal-power module is holonomic

Over the field $K=k(s)$, $\mathcal L_K$ is holonomic.

**Proof.** Define

\[
F_p\mathcal L_K=
\{g f^{s-p}:g\in K[x],\ \deg g\leq(d+1)p\}.
\tag{2.3}
\]

These are vector spaces. They are increasing, since multiplying a numerator by $f$ changes denominator depth from $p$ to $p+1$ and increases its degree by at most $d$.

Multiplication by $x_i$, expressed at depth $p+1$, changes $g$ to $x_i g f$, of degree at most $(d+1)(p+1)$. By (1.2), differentiation, at that same depth, changes the numerator to

\[
f\,\partial_i g+(s-p)g\,\partial_i f.
\tag{2.4}
\]

Its degree is at most $(d+1)p+d-1$ when derivatives are nonzero, so it also lies in the required next piece. Since $B_1$ generates the Bernstein filtration, these checks prove compatibility for every $B_a$.

Every element of the ambient module is a finite sum of terms $h f^{s-q}$. For sufficiently large $p\geq q$, rewrite such a term as $h f^{p-q}f^{s-p}$; the numerator degree is $\deg h+d(p-q)\leq(d+1)p$. Thus the filtration is exhaustive. Finally multiplication by $f^{-p}e_s$ is injective on $K[x]$, so

\[
\dim_K F_p\mathcal L_K=\binom{(d+1)p+n}{n}
=\frac{(d+1)^n}{n!}p^n+O(p^{n-1}).
\tag{2.5}
\]

Lemma 2.1, over the characteristic-zero field $K$, proves the assertion, and also gives $e(\mathcal L_K)\leq(d+1)^n$. $\square$

## 3. Existence and the minimal polynomial

### Theorem 3.1. Bernstein's functional equation

There exist a nonzero $b(s)\in k[s]$ and $P(s)\in A[s]$ such that

\[
P(s)f^{s+1}=b(s)f^s
\quad\text{in }\mathcal L_s.
\tag{3.1}
\]

**Proof.** In the holonomic $A_K$-module $\mathcal L_K$, consider the descending chain

\[
C_0=A_K e_s\supseteq C_1=A_K f e_s
\supseteq C_2=A_K f^2e_s\supseteq\cdots.
\tag{3.2}
\]

Finite length gives $C_r=C_{r+1}$ for some $r\geq0$. We need to translate this equality to exponent zero; multiplication by $f^{-r}$ alone would not commute with derivatives.

For an integer $a$, define the bijective semilinear map

\[
T_a(g(s,x)e_s)=g(s+a,x)f^a e_s.
\tag{3.3}
\]

Its inverse is $T_{-a}$. It commutes with coordinates and derivatives, as (1.1) shows: the extra derivative of $f^a$ exactly replaces $s$ by $s+a$. Its coefficient-field action is the automorphism $s\mapsto s+a$, and therefore

\[
T_a(P(s)v)=P(s+a)T_a(v).
\tag{3.4}
\]

Applying $T_{-r}$ to $C_r=C_{r+1}$ gives $C_0=C_1$. Hence some $Q(s)\in A_K$ satisfies $Q(s)f^{s+1}=e_s$. Write its finitely many normal-form coefficients as rational functions of $s$ and choose a common nonzero polynomial denominator $b(s)$. Then $P(s)=b(s)Q(s)$ lies in $A[s]$ and satisfies (3.1) in $\mathcal L_K$. Both sides belong to $\mathcal L_s$, which injects into $\mathcal L_K$, so the equality holds there too. $\square$

The set

\[
I_f=\{b(s)\in k[s]:b(s)f^s\in A[s]f^{s+1}\}
\tag{3.5}
\]

is an ideal: add the corresponding operators for a sum, and multiply them by a scalar polynomial for a multiple. It is nonzero by Theorem 3.1. Its unique monic generator is the **Bernstein–Sato polynomial** $b_f(s)$. A displayed functional equation establishes divisibility $b_f\mid b$, not automatically equality.

If $f=c\in k^\times$, the operator $c^{-1}$ gives $b_f=1$. Otherwise $b_f$ has at least one specified root.

### Proposition 3.2. The root $-1$

For nonconstant $f$, $(s+1)\mid b_f(s)$.

**Proof.** Specialization at any integer $a$ is the $A$-linear map

\[
\mathcal L_s\longrightarrow R_f,\qquad
g(s,x)e_s\longmapsto g(a,x)f^a.
\tag{3.6}
\]

The derivative rule (1.1) verifies linearity. At $a=-1$, a functional equation becomes

\[
P(-1)\cdot1=b(-1)f^{-1}.
\tag{3.7}
\]

The left side is a polynomial. Thus $f$ divides the scalar $b(-1)$ in $R$. A nonconstant polynomial cannot divide a nonzero scalar, so $b(-1)=0$. Apply this to $b_f$. $\square$

We will also use two invariance facts. An invertible linear coordinate change transports functions, derivatives, and (3.1), hence preserves $b_f$. Multiplying $f$ by a nonzero scalar preserves its logarithmic derivatives in (1.1), and rescales the operator in (3.1); it too preserves the ideal.

Finally $b_f$ is unchanged by extending the field. To prove this, let $k\subseteq L$ and suppose an equation has coefficients in $L$. The finitely many coefficients of its operator and scalar polynomial lie in a finite-dimensional $k$-subspace of $L$. Express them in a $k$-linearly independent basis. Comparing the basis coefficients in $L\otimes_k\mathcal L_s$ gives equations over $k$ for each component polynomial. Each component is divisible by $b_f$ over $k$, so their sum over $L$ is divisible by it over $L$. The converse inclusion follows by extending a defining equation over $k$. Thus the monic generators coincide.

## 4. Localization of every holonomic Weyl module

For an $A$-module $M$, define $M_f=R_f\otimes_RM$. The product rule extends its derivative action by

\[
\partial_i\!\left(\frac{m}{f^p}\right)
=\frac{f\,\partial_i m-p(\partial_i f)m}{f^{p+1}}.
\tag{4.1}
\]

This is well defined. One way to check it is to use the ordinary derivation on $R_f$ and set $\partial_i(a\otimes m)=(\partial_i a)\otimes m+a\otimes\partial_i m$; the balancing relation follows from the Leibniz rule on $M$. The commutation relations follow on tensors.

### Theorem 4.1. Holonomic localization

If $M$ is holonomic over $A_n(k)$, then $M_f$ is finitely generated and holonomic, or zero.

**Proof.** The zero case is immediate. Choose a good Bernstein filtration $\Gamma$ of $M$, indexed so that $\Gamma_p=0$ for $p<0$. Put $a=d+1$ and define

\[
\Lambda_p M_f=
\left\{\frac{m}{f^p}:m\in\Gamma_{ap}M\right\}.
\tag{4.2}
\]

These are images of finite-dimensional spaces; numerator torsion causes no difficulty. They are increasing because $f\Gamma_{ap}\subseteq\Gamma_{ap+d}\subseteq\Gamma_{a(p+1)}$. Multiplication by a coordinate, at denominator depth $p+1$, has numerator $fx_i m$, in $\Gamma_{ap+d+1}$. In (4.1) the numerator has the same bound: $f\partial_i m$ has degree increase at most $d+1$, and $(\partial_i f)m$ at most $d-1$. Thus the filtration is Bernstein compatible.

To see exhaustiveness, write an element as $m/f^q$, with $m\in\Gamma_tM$. At depth $p\geq q$ its numerator is $f^{p-q}m\in\Gamma_{t+d(p-q)}M$. This is in $\Gamma_{ap}$ once $p$ is sufficiently large. Finally

\[
\dim_k\Lambda_pM_f\leq\dim_k\Gamma_{ap}M
=\frac{e(M)a^n}{n!}p^n+O(p^{n-1}).
\tag{4.3}
\]

Lemma 2.1 proves finite generation and holonomicity. It also gives the useful bound $e(M_f)\leq e(M)(d+1)^n$. $\square$

In particular $R_f$ is holonomic, since $R$ is holonomic. The b-function additionally specifies a single generating denominator.

### Proposition 4.2. One denominator suffices for $R_f$

Choose an integer $N\geq0$ so that $b_f(-q)\ne0$ for every integer $q>N$. Then

\[
R_f=A\cdot f^{-N}.
\tag{4.4}
\]

**Proof.** Such an $N$ exists because a nonzero polynomial has finitely many roots. Specialize (3.1) at $s=-q$, for $q>N$, to obtain

\[
P(-q)f^{1-q}=b_f(-q)f^{-q}.
\tag{4.5}
\]

The scalar on the right is invertible in $k$. Starting with $f^{-N}$, this produces $f^{-N-1}$, then every deeper inverse power. Shallower inverse powers and all numerators are obtained by multiplying by polynomials. These elements span $R_f$, proving the equality. $\square$

Theorem 4.1 does not require a torsion-free module or an injective map $M\to M_f$. For example, the point module at a zero of $f$ can localize to zero.

## 5. Explicit polynomials and minimality

### A coordinate and a power

For $f=x$,

\[
\partial x^{s+1}=(s+1)x^s.
\]

Proposition 3.2 then proves $b_x=s+1$.

For $f=x^m$, $m\geq1$, repeated differentiation gives

\[
\partial^m(x^m)^{s+1}
=\prod_{r=0}^{m-1}(m(s+1)-r)(x^m)^s
=m^m\prod_{j=1}^m\left(s+\frac jm\right)(x^m)^s.
\tag{5.1}
\]

Thus the monic product is an admissible b-function. To prove minimality, write any $P(s)$ in normal form as a finite sum of $c_{ab}(s)x^a\partial^b$. Dividing its action on $(x^m)^{s+1}$ by $(x^m)^s$, each summand has Laurent coefficient

\[
c_{ab}(s)\,(m(s+1))_b\,x^{m+a-b},
\qquad (z)_b=z(z-1)\cdots(z-b+1).
\tag{5.2}
\]

The coefficient of $x^0$ can only come from $b=m+a\geq m$. Its falling factorial contains the first $m$ factors in (5.1). Therefore any polynomial $b(s)$ in a functional equation is divisible by the monic product. Laurent monomials are independent, so cancellations of the other coefficients cannot alter this conclusion. We have proved

\[
b_{x^m}(s)=\prod_{j=1}^m\left(s+\frac jm\right).
\tag{5.3}
\]

In extra variables, derivatives in those variables kill the formal symbol; comparing their coordinate coefficients gives the same answer.

### A nondegenerate quadratic form

Let $q=x_1^2+\cdots+x_n^2$, $n\geq1$, and $\Delta=\sum_i\partial_i^2$. Direct differentiation gives

\[
\partial_i^2 q^{s+1}
=2(s+1)q^s+4s(s+1)x_i^2q^{s-1}.
\]

After summing,

\[
\frac14\Delta q^{s+1}
=(s+1)\left(s+\frac n2\right)q^s.
\tag{5.4}
\]

We now prove that neither factor can be omitted, including its repeated occurrence for $n=2$.

For $n=1$, (5.3) with $m=2$ gives precisely the answer. For $n=2$, work first over $\mathbb C$ and set $u=x_1+ix_2$, $v=x_1-ix_2$, so $q=uv$. The identity $\partial_u\partial_v(uv)^{s+1}=(s+1)^2(uv)^s$ is minimal: for a normal-form term $u^a v^b\partial_u^c\partial_v^h$ to contribute to the constant Laurent coefficient after dividing by $(uv)^s$, one must have $c=a+1$ and $h=b+1$. Its coefficient therefore contains an $s+1$ factor from each derivative string. Every contribution is divisible by $(s+1)^2$. Coordinate invariance proves the result for $q$ over $\mathbb C$.

For $n\geq3$, Proposition 3.2 supplies the root $-1$. We show that every admissible polynomial also vanishes at $-n/2$ by an elementary integral. Work over $\mathbb C$, using the real slice $\mathbb R^n$ on which $q=|x|^2$. Choose $\phi\in C_c^\infty(\mathbb R^n)$ equal to one on a ball of radius $\varepsilon>0$. Initially for $\operatorname{Re}s>-n/2$, let

\[
J(s)=\int_{\mathbb R^n}q(x)^s\phi(x)\,dx.
\]

The contribution from that ball, in polar coordinates, is

\[
\frac{\omega_{n-1}\varepsilon^{\,2s+n}}{2s+n},
\tag{5.5}
\]

where $\omega_{n-1}>0$ is the area of the unit sphere. The remaining integral is entire, since its compact domain stays away from zero. Hence $J$ extends meromorphically and has a simple pole at $s=-n/2$ with nonzero residue.

For any equation $P(s)q^{s+1}=b(s)q^s$, integration by parts for sufficiently large $\operatorname{Re}s$ gives

\[
b(s)J(s)=
\int_{\mathbb R^n}q(x)^{s+1}\bigl(P(s)^{\mathsf t}\phi\bigr)(x)\,dx.
\tag{5.6}
\]

The superscript $\mathsf t$ denotes the formal transpose for the real volume form, reversing products, fixing coordinates and sending $\partial_i$ to $-\partial_i$. The right side is holomorphic on $\operatorname{Re}s>-n/2-1$. Indeed, its test function and all its parameter derivatives are bounded on a fixed compact support; the radial powers and their logarithmic derivatives are integrable uniformly on smaller half-planes. Identity continuation in that half-plane shows that $b(s)J(s)$ has no pole at $-n/2$. The nonzero residue in (5.5) forces $b(-n/2)=0$.

These roots are distinct for $n\geq3$. Together with (5.4), they prove

\[
b_q(s)=(s+1)\left(s+\frac n2\right).
\tag{5.7}
\]

This polynomial has rational coefficients. Field invariance from Section 3 first proves the assertion over $\mathbb Q$ from its extension to $\mathbb C$, and then over every characteristic-zero field. The integral argument only establishes the needed quadratic root; it assumes no general theorem on meromorphic distributions.

### The cusp: a stated computation

For $f=x^2+y^3$, the answer is

\[
b_f(s)=(s+1)\left(s+\frac56\right)\left(s+\frac76\right).
\tag{5.8}
\]

This computation is stated here, as assigned, rather than proved. See M. Popa, [*The Bernstein–Sato polynomial*](https://people.math.harvard.edu/~mpopa/notes/Bernstein-Sato-notes.pdf), Example 1.10(2) and Theorem 2.4. For orientation, the weights are $1/2,1/3$ and the Jacobian algebra is $k[x,y]/(x,y^2)$, with basis $1,y$ of weights $0,1/3$. The stated weighted-homogeneous formula gives the shifts $5/6$ and $7/6$. That general formula and its minimality theorem are not proved in this chapter.

## 6. Two analytic statements

The following facts explain what the algebraic polynomial detects. Neither is an input to our existence or localization proof.

**Negative rational roots — statement.** For a nonconstant complex polynomial, every root of $b_f$ is a strictly negative rational number. More generally the local b-function of a nonzero holomorphic germ has this property unless it is the constant polynomial one. This is Kashiwara's theorem; see [*B-functions and holonomic systems*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/Bfunct.pdf), Corollary (5.2) and Popa's Theorem 3.1 for the algebraic formulation. Its proof uses substantially more than finite length and is not given here.

The characteristic-zero version follows from this statement and the field invariance proved above. The finitely many coefficients of $f$ lie in a finitely generated subfield of $k$, which embeds into $\mathbb C$. Extend to $\mathbb C$, apply the stated theorem, and extend back to $k$. In particular the monic polynomial has coefficients in $\mathbb Q$ under the canonical inclusion into $k$.

**Distributional continuation — statement.** For a nonzero real polynomial, $|f|^s$, initially a locally integrable distribution for $\operatorname{Re}s>0$, has a meromorphic distribution-valued continuation to all $s\in\mathbb C$. Bernstein's [*The analytic continuation of generalized functions with respect to a parameter*](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-a-cont-FAN.pdf), Theorem 1, treats the powers extended by zero from a region where a polynomial is positive; applying it on the positive and negative regions gives this absolute-value version. The poles lie in finitely many progressions with step $-1$.

For a complex polynomial on $\mathbb C^n$, the standard normalization is $|f|^{2s}$. For every smooth compactly supported test function $\phi$, the integral $\int_{\mathbb C^n}|f|^{2s}\phi$ continues meromorphically, with possible poles $\alpha-j$, where $\alpha$ is a root of $b_f$ and $j\in\mathbb Z_{\geq0}$; see Popa, Theorem 5.2. For the exponent $|f|^s$ on that same complex space, rescaling the parameter gives possible poles $2(\alpha-j)$. This factor of two depends on the exponent convention.

The distribution theory belongs to the analysis lessons *Finite parts of singular powers* and *Complex powers at a boundary*. Here the formal symbol $f^s$ and its algebraic equation are defined without a branch choice, a test function, or an analytic continuation.

## 7. Exercises with complete solutions

### Exercise 7.1 — easy: powers of a coordinate

Find an operator giving a monic functional equation for $f=x^m$, and prove that its polynomial is minimal.

**Solution.** The operator is $m^{-m}\partial^m$, and (5.1) gives the monic polynomial $\prod_{j=1}^m(s+j/m)$. In any other normal-form operator, the only terms contributing to Laurent exponent zero in (5.2) have $b=m+a$. Their derivative factors all contain $\prod_{r=0}^{m-1}(m(s+1)-r)$, a nonzero scalar multiple of that monic polynomial. Thus every admissible scalar polynomial is divisible by it, proving minimality.

### Exercise 7.2 — easy: one generator for Laurent polynomials

Prove $k[x,x^{-1}]=A_1x^{-1}$ and determine its length.

**Solution.** Repeated differentiation gives $\partial^r x^{-1}=(-1)^r r!x^{-r-1}$, with nonzero coefficient in characteristic zero. Multiplication by $x$ gives all nonnegative and shallower powers. Thus the indicated vector generates every Laurent monomial. The preceding chapters proved

\[
0\longrightarrow k[x]\longrightarrow k[x,x^{-1}]
\longrightarrow\delta_0\longrightarrow0,
\]

with nonzero simple end terms. Hence the length is two. The Euler presentation $A_1/A_1(x\partial+1)$ gives Bernstein multiplicity two, so the previous chapter's bound is attained.

### Exercise 7.3 — medium: the quadratic identity and its repeated root

Verify (5.4). Explain why a verification of that identity alone does not prove (5.7), and why $n=2$ requires an additional multiplicity argument.

**Solution.** Since $\partial_iq=2x_i$, the first derivative is $2(s+1)x_iq^s$, and a second derivative is $2(s+1)q^s+4s(s+1)x_i^2q^{s-1}$. Summing and dividing by four gives $(s+1)(s+n/2)q^s$. This proves divisibility of the minimal polynomial into the displayed product. For $n\ne2$, Section 5 supplies both distinct roots: monomial minimality when $n=1$, and the root $-1$ together with the radial integral root when $n\geq3$. For $n=2$, those two root locations coincide. The normal-crossings calculation in $u,v$ proves that every admissible polynomial is divisible by $(s+1)^2$, which is the missing multiplicity assertion.

### Exercise 7.4 — medium: localizing a module with torsion

Prove holonomicity of $M_f$ for arbitrary holonomic $M$, without assuming that $M\to M_f$ is injective. For $M=\delta_0$ on the line, compute $M_x$ and $M_{x-1}$.

**Solution.** Use the images (4.2), not an inclusion of $M$ in its localization. Their dimensions are at most $\dim\Gamma_{(d+1)p}M$, even if numerators have nonzero kernel. The product and derivative computations in Theorem 4.1 make these spaces a compatible exhaustive filtration with growth degree at most $n$. Lemma 2.1 then proves finite generation and holonomicity, including the zero case.

Every basis vector $\partial^j\delta$ is killed by $x^{j+1}$, so every vector of $\delta_0$ is $x$-power torsion; hence $M_x=0$. Conversely $x$ is locally nilpotent on this module, so $x-1$ is invertible: its inverse on any vector is the finite sum $-(1+x+x^2+\cdots)$, stopped once powers of $x$ kill that vector. This supplies the unique extended $(x-1)^{-1}$ action. The natural map $M\to M_{x-1}$ is therefore an isomorphism, so that localization remains the nonzero holonomic point module.

### Exercise 7.5 — hard: the unavoidable factor

Show that every admissible polynomial for a nonconstant $f$ vanishes at $-1$. Explain what changes for a nonzero constant $f$.

**Solution.** The specialization map (3.6), with $a=-1$, changes $f^{s+1}$ to $1$ and $f^s$ to $f^{-1}$, and commutes with every derivative by the ordinary chain rule. Thus (3.7) holds. Since polynomial differential operators send $1$ to a polynomial, it forces $f\mid b(-1)$. Nonconstancy implies $b(-1)=0$. For a nonzero constant, this divisibility imposes no vanishing condition and the scalar inverse gives an equation with $b=1$, which is the minimal polynomial.

### Exercise 7.6 — hard: the parameter shift

Why cannot one deduce $C_0=C_1$ from a stable equality $C_r=C_{r+1}$ by simply multiplying by $f^{-r}$? Verify the corrected semilinear operation.

**Solution.** Multiplication by $f^{-r}$ satisfies

\[
\partial_i(f^{-r}v)=f^{-r}\partial_i v
-r f^{-r-1}(\partial_i f)v.
\]

It therefore fails to be $A_K$-linear unless the extra term vanishes. For $T_a$ in (3.3), differentiating the factor $f^a$ adds $a(\partial_i f)/f$, precisely the change in the connection coefficient when $s$ is replaced by $s+a$. This proves commutation with derivatives and coordinates, while coefficient scalars are transformed by $s\mapsto s+a$. As $T_{-r}$ is bijective and sends $f^re_s$ to $e_s$ and $f^{r+1}e_s$ to $fe_s$, it sends their generated submodules to $C_0,C_1$. Equality is therefore preserved, giving the required conclusion.

## References and what this lesson does not prove

The growth criterion, holonomicity over $k(s)$, Bernstein's existence theorem, field invariance, the factor $s+1$, localization of arbitrary holonomic Weyl modules, a generating denominator for $R_f$, and the coordinate-power and quadratic minimal polynomials are proved here. All six exercises are solved. The cusp computation, Kashiwara's negative-rational-root theorem, and the general distributional continuation statements are explicitly stated external results.

R. Bezrukavnikov, [*Noncommutative Algebra*, MIT 18.706](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_full_lec.pdf), Sections 24.1 and 24.6, supplies the broader growth context. V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Section 4.2, especially Theorem 4.2.9.2, treats localization by a Bernstein growth estimate. The proof above counts cumulative filtered dimensions, uses only an upper bound for a possibly nongood localization filtration, and establishes finite generation before invoking finite length on the ambient module.

The analytic results have the exact locators given in Section 6. The formula for the cusp has the exact locators in Section 5. The algebraic existence and localization proofs depend only on the preceding chapter's growth and finite-length theorems.

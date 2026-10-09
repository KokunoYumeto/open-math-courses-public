# Bernstein–Sato polynomials

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Prerequisite reconciliation, distributional-continuation and cusp-minimality proofs, and reader corrections by GPT-6 Astra (OpenAI), Ultra, October 2026; original proofs and complete solutions retained.*

Differentiating $x^{s+1}$ produces $(s+1)x^s$. For a general polynomial $f$, a suitable differential operator still lowers the formal exponent by one, but the scalar factor becomes a polynomial in $s$. The smallest such scalar factor is the Bernstein–Sato polynomial. Its existence follows from a growth estimate and finite length, even when no useful operator is apparent. The same estimate proves that allowing arbitrary powers of $f$ in denominators preserves holonomicity.

Throughout, $k$ has characteristic zero, $R=k[x_1,\ldots,x_n]$, $A=A_n(k)$, and $0\ne f\in R$. Put $d=\deg f$ and $R_f=R[f^{-1}]$. Modules are left modules. The prerequisite is The Bernstein filtration and holonomic modules over the Weyl algebra: we use Bernstein's inequality, Theorem 3.1, positive integral multiplicity, Theorem 1.1, its exact-sequence formula, Proposition 1.2, and finite length, Theorem 5.1. No analytic correspondence is needed for the existence theorem or localization.

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

### The cusp: explicit equation and minimality

For $f=x^2+y^3$ over any characteristic-zero field, we will prove

\[
b_f(s)=(s+1)\left(s+\frac56\right)\left(s+\frac76\right).
\tag{5.8}
\]

An operator proves that the right side is admissible. Two explicitly computed poles then prove that neither of the fractional roots can be removed. This is a proof of the cusp formula itself; it does not assume the general weighted-homogeneous formula stated below.

#### An explicit operator

Consider the polynomial-coefficient operator

\[
\begin{aligned}
P={}&\frac38\partial_x^2+\frac1{27}\partial_y^3\\
&+\frac18x\partial_x^3+\frac16y\partial_x^2\partial_y.
\end{aligned}
\tag{5.9}
\]

Multiplications by $x$ and $y$ here occur after the indicated derivatives. Put $X=x^2$, $Y=y^3$, so $f=X+Y$. Repeated use of (1.2) gives the following four identities in the formal-power module:

\[
\begin{aligned}
\partial_x^2 f^{s+1}
 &=(s+1)f^{s-2}\\
 &\quad\cdot[2f^2+4sXf],\\
\partial_y^3 f^{s+1}
 &=(s+1)f^{s-2}\\
 &\quad\cdot[6f^2+54sYf\\
 &\qquad+27s(s-1)Y^2],\\
x\partial_x^3 f^{s+1}
 &=(s+1)f^{s-2}\\
 &\quad\cdot[12sXf+8s(s-1)X^2],\\
y\partial_x^2\partial_y f^{s+1}
 &=(s+1)f^{s-2}\\
 &\quad\cdot[6sYf+12s(s-1)XY].
\end{aligned}
\tag{5.10}
\]

For example, differentiate $2(s+1)f^s+4s(s+1)x^2f^{s-1}$ once more in $x$ and multiply by $x$ to obtain the third identity. For the fourth, differentiate that same expression in $y$ and multiply by $y$. The second follows by differentiating $3(s+1)y^2f^s$ twice; its two middle contributions are $18s(s+1)y^3f^{s-1}$ and $36s(s+1)y^3f^{s-1}$, giving the coefficient $54$.

Multiply the four bracketed expressions by $3/8,1/27,1/8,1/6$, respectively, and add. Their coefficients of $X^2$, $XY$ and $Y^2$ are, respectively,

\[
\begin{gathered}
s^2+2s+\frac{35}{36},\\
2s^2+4s+\frac{35}{18},\\
s^2+2s+\frac{35}{36}.
\end{gathered}
\tag{5.11}
\]

The sum is therefore $(s+5/6)(s+7/6)(X+Y)^2$. Substitution in (5.10) proves

\[
\begin{aligned}
P f^{s+1}&=(s+1)(s+5/6)\\
&\quad\cdot(s+7/6)f^s.
\end{aligned}
\tag{5.12}
\]

No division by $s+1$ was used, so the identity is valid at every parameter. By the definition of $I_f$, (5.12) proves that $b_f$ divides the polynomial in (5.8). Proposition 3.2 supplies its root $-1$; it remains to force $-5/6$ and $-7/6$.

#### Two test integrals force the other roots

Work first over $\mathbb C$ and use the real $(x,y)$-plane for the integrals. Write $v=-y$ and set

\[
\begin{gathered}
g=-f=v^3-x^2,\\
\Omega=\{(x,y):v>0,\ |x|<v^{3/2}\}.
\end{gathered}
\tag{5.13}
\]

Thus $\Omega=\{g>0\}$ and its entire finite boundary lies in $g=0$. Let $T(s)=1_\Omega g^s$. [Theorem 6.1](#theorem-6-1-real-and-complex-distributional-continuation) below supplies its unique meromorphic distribution-valued continuation; that proof depends on Section 3, not on this cusp computation, so there is no circular use.

We first establish a stronger initial domain for this particular $T$. For $\operatorname{Re}s>-5/6$, all its compact-test integrals converge and are holomorphic. To see this, use $x=v^{3/2}u$, $-1<u<1$, with $dx=v^{3/2}du$ at fixed $v$. A compact support puts $v$ in $[0,V]$ for some finite $V$. The absolute value of the integral is bounded by the test's supremum times

\[
\begin{aligned}
&\int_0^V v^{3\operatorname{Re}s+3/2}\,dv\\
&\qquad\cdot\int_{-1}^1(1-u^2)^{\operatorname{Re}s}\,du.
\end{aligned}
\tag{5.14}
\]

The first integral converges exactly when $\operatorname{Re}s>-5/6$. The second converges for $\operatorname{Re}s>-1$: near either endpoint $1-u^2$ is bounded above and below by positive multiples of the distance to that endpoint. On any compact subset of $\operatorname{Re}s>-5/6$, allow a small positive slack in the exponent. The power-series estimate (6.3) then bounds every parameter derivative and the series tails by the same integrable product, with the smaller exponent near its zeros. Away from those zeros all factors are bounded. This proves holomorphy in a common order-zero compact-test bound, including for tests depending polynomially on $s$.

Choose $0<\varepsilon<V$ and a smooth function $\rho$ on the real line, supported in $(-V,V)$ and equal to one on $[-\varepsilon,\varepsilon]$. Choose a compactly supported smooth $\chi(x)$ equal to one for $|x|\leq V^{3/2}$. For $j=0,1$ define the compact test

\[
\phi_j(x,y)=(-y)^j\rho(-y)\chi(x).
\tag{5.15}
\]

Such cutoffs can be constructed from $h(t)=e^{-1/t}$ for $t>0$, $h(t)=0$ otherwise: its derivatives are polynomials in $1/t$ times $e^{-1/t}$ and tend to zero at zero, and $h(t)/(h(t)+h(1-t))$ gives a smooth transition. Translate and rescale that transition at the two endpoints of each desired interval.

Where $\rho(v)\ne0$ inside $\Omega$, the factor $\chi$ is one. The same substitution as above therefore gives, initially for $\operatorname{Re}s>-5/6$,

\[
\begin{gathered}
I_j(s):=T(s)(\phi_j)=A(s)M_j(s),\\
A(s)=\int_{-1}^1(1-u^2)^s\,du,\\
M_j(s)=\int_0^V v^{3s+j+3/2}\rho(v)\,dv.
\end{gathered}
\tag{5.16}
\]

The radial factor has the elementary meromorphic expression

\[
\begin{aligned}
M_j(s)&=\frac{\varepsilon^{3s+j+5/2}}{3s+j+5/2}\\
&\quad+\int_\varepsilon^V v^{3s+j+3/2}\rho(v)\,dv.
\end{aligned}
\tag{5.17}
\]

The last integral is entire, since its integration interval stays away from zero. Thus $M_j$ has a simple pole of residue $1/3$ at

\[
s_j=-\frac{2j+5}{6}.
\tag{5.18}
\]

The angular factor is holomorphic for $\operatorname{Re}s>-1$, with $A(-5/6)>0$. To reach the other parameter, integrate the derivative of $u(1-u^2)^{s+1}$ on $(-1,1)$. When $\operatorname{Re}s>-1$ its endpoint values vanish and its derivative is integrable, so

\[
\begin{gathered}
(2s+2)A(s)=(2s+3)A(s+1),\\
A(s)=\frac{2s+3}{2s+2}A(s+1).
\end{gathered}
\tag{5.19}
\]

The second expression continues $A$ to $\operatorname{Re}s>-2$. In particular,

\[
A(-7/6)=-2A(-1/6)\ne0.
\tag{5.20}
\]

Equations (5.16)–(5.20), with analytic uniqueness, now show that $I_0$ and $I_1$ have genuine simple poles at $-5/6$ and $-7/6$, respectively, with nonzero residues $A(s_j)/3$. These are poles of test pairings of $T$, not merely a scaling prediction. No Gamma-function formula or general theorem on roots is used.

Finally let $b(s)f^s=Q(s)f^{s+1}$ be **any** polynomial functional equation over $\mathbb C$. Multiplication by the scalar $-1$ preserves $I_f$ by Section 3; under that identification an equation for $g=-f$ is $b(s)g^s=-Q(s)g^{s+1}$. The zero-set argument and formal transpose from (6.4)–(6.5) give

\[
b(s)I_j(s)=T(s+1)\bigl((-Q(s))^{\mathsf t}\phi_j\bigr)
\tag{5.21}
\]

first far to the right and then meromorphically by uniqueness. The right side is holomorphic on $\operatorname{Re}s>-11/6$, by (5.14); transposition leaves the support compact and gives a test depending polynomially on $s$. This half-plane contains both $s_0$ and $s_1$. Comparing residues in (5.21) forces $b(-5/6)=b(-7/6)=0$. Together with Proposition 3.2, every admissible $b$ is divisible by the three distinct factors in (5.8). Equation (5.12) proves the reverse divisibility, establishing the exact monic polynomial over $\mathbb C$.

The operator (5.9) and the polynomial (5.8) have rational coefficients. The field-extension invariance in Section 3 identifies the answer over $\mathbb Q$ with the answer over $\mathbb C$, and then identifies it over any characteristic-zero field with its extension from $\mathbb Q$. Thus (5.8) has the full field generality claimed.

#### The general weighted-homogeneous formula remains separate

The weights for this cusp are $1/2,1/3$, and its Jacobian algebra is $k[x,y]/(x,y^2)$, with basis $1,y$ of weights $0,1/3$. Their sum with $1/2+1/3$ gives the two shifts in (5.8), but this observation alone would not have proved either admissibility or minimality.

For the full general result, let $f\in\mathbb C[x_1,\ldots,x_n]$ be weighted homogeneous of degree one for positive rational weights $w_i$, with an isolated critical point at the origin. Take a monomial basis of its finite-dimensional Jacobian algebra and let $\Sigma$ be the **set of its distinct weighted degrees**, not a list with repeated degrees. The general formula states

\[
\begin{aligned}
b_f(s)&=(s+1)\\
&\quad\cdot\prod_{\rho\in\Sigma}
\left(s+\sum_{i=1}^n w_i+\rho\right).
\end{aligned}
\tag{5.22}
\]

See M. Popa, [*The Bernstein–Sato polynomial*](https://people.math.harvard.edu/~mpopa/notes/Bernstein-Sato-notes.pdf), Example 1.10(2) and Theorem 2.4, for the cusp and general formula. The general statement and its minimality proof remain external here; the direct cusp proof above is not a replacement for them. In particular repeated weights must not be converted into extra factors by treating $\Sigma$ as a multiset. The external proof uses an annihilator statement, Lemma 2.7, whose proof is delegated there to other references; that input must itself have an exact full proof provider before the general formula is counted as internally proved.

## 6. Two analytic statements

The following facts explain what the algebraic polynomial detects. Neither is an input to our existence or localization proof.

**Negative rational roots — statement.** For a nonconstant complex polynomial, every root of $b_f$ is a strictly negative rational number. More generally the local b-function of a nonzero holomorphic germ has this property unless it is the constant polynomial one. This is Kashiwara's theorem; see [*B-functions and holonomic systems*](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/Bfunct.pdf), Corollary (5.2) and Popa's Theorem 3.1 for the algebraic formulation. Its proof uses substantially more than finite length and is not given here.

The characteristic-zero version follows from this statement and the field invariance proved above. The finitely many coefficients of $f$ lie in a finitely generated subfield of $k$, which embeds into $\mathbb C$. Extend to $\mathbb C$, apply the stated theorem, and extend back to $k$. In particular the monic polynomial has coefficients in $\mathbb Q$ under the canonical inclusion into $k$.

### Theorem 6.1. Real and complex distributional continuation

Let $0\ne f\in\mathbb R[x_1,\ldots,x_n]$. The distributions $|f|^s$, initially defined for $\operatorname{Re}s>0$, extend uniquely to a meromorphic family on the whole parameter plane. Their possible poles are among

\[
\alpha-j,\qquad b_f(\alpha)=0,\quad j\in\mathbb Z_{\geq0}.
\tag{6.1}
\]

More generally, if $\Omega$ is any open subset of $\{f>0\}$ with $\partial\Omega\subseteq\{f=0\}$, the powers $f^s$ extended by zero outside $\Omega$ have the same conclusion. No regularity of that boundary is assumed.

For $0\ne f\in\mathbb C[z_1,\ldots,z_n]$, the family $|f|^{2s}$ on $\mathbb C^n=\mathbb R^{2n}$ also has a unique meromorphic continuation, with possible poles (6.1). Thus $|f|^s$ on complex space has possible poles $2(\alpha-j)$. All these families, including every Laurent coefficient, are tempered distributions. The pole sets can be smaller than the displayed sets.

The proof below requires only the functional equation in Theorem 3.1, with its minimal polynomial from (3.5); it does not require the negative-rational-root theorem. That still-external theorem additionally says that all the candidate poles in (6.1) are negative rational numbers. For a nonzero constant $f$, $b_f=1$ and the families are entire.

#### Analytic families, test bounds and continuation

Distributions pair **complex linearly** with tests. On $\mathbb R^d$ write

\[
\begin{gathered}
p_{K,r}(\phi)=\max_{|\nu|\leq r}\sup_K|\partial^\nu\phi|,\\
q_{L,r}(\phi)=\max_{|\nu|\leq r}\sup_x(1+|x|)^L|\partial^\nu\phi(x)|.
\end{gathered}
\tag{6.2}
\]

The first seminorm is used for smooth tests supported in a fixed compact $K$; the second is a Schwartz seminorm. Here a distribution-valued family is holomorphic when its test pairings have local power series with a common finite test-seminorm bound on smaller parameter disks. It is meromorphic when, near each parameter, multiplication by one nonzero scalar polynomial makes it holomorphic. Crucially, that polynomial and a bound on the pole order are independent of the test.

We will use a direct integral observation. Consider the integrand $\eta(x)t(x)^{a+cs}\phi(x)$, where $a\geq0$, $c>0$, $t$ is the absolute value of a polynomial, and $\eta$ is a fixed measurable function with $|\eta|\leq1$. Set the integrand to zero at $t=0$. This defines a holomorphic family on $a+c\operatorname{Re}s>0$. Indeed, around $s_0$ choose $\rho>0$ with $a+c\operatorname{Re}s_0-c\rho>0$. Expand the parameter factor using the real logarithm of $t$:

\[
t^{c(s_0+h)}=t^{cs_0}\sum_{\ell\geq0}
\frac{(ch\log t)^\ell}{\ell!}.
\tag{6.3}
\]

For $|h|\leq\rho$, the sum of the absolute values, after multiplication by $t^a$, is at most $t^{a+c\operatorname{Re}s_0-c\rho}$ when $0<t\leq1$, and at most $t^{a+c\operatorname{Re}s_0+c\rho}$ when $t\geq1$. The first bound is at most one. The second has at most polynomial growth in $x$, since $t(x)\leq C(1+|x|)^{\deg f}$. On compact tests this is bounded by a constant times $p_{K,0}(\phi)$. On Schwartz tests choose $L$ larger than the growth exponent plus $d$ and integrate the bound $(1+|x|)^{-L}$ against that growth. This gives a constant times $q_{L,0}(\phi)$.

For completeness, absolute convergence of the integrated series is uniform on every smaller disk $|h|\leq\rho'<\rho$: the tail starting at degree $m$ is at most $(\rho'/\rho)^m$ times the integrable sum just bounded at radius $\rho$. Thus the integrals of the series converge in a common test-seminorm bound, not just separately for each test. The same argument on a slightly larger disk bounds all parameter derivatives. It also applies after restricting the integral to a fixed measurable region.

Scalar analytic uniqueness will be used on overlapping half-planes. A convergent power series which is not identically zero has isolated zeros: factor out its first nonzero power and use continuity of the remaining, nonzero factor. It follows that an analytic function zero on an open subset of a connected domain is zero everywhere: the set where its germ is zero is both open and closed, the latter by the isolated-zero observation. For meromorphic functions, first clear the finitely many local denominator factors. Applying this argument to each test gives uniqueness for the families used below.

For a polynomial-coefficient differential operator $Q$, its formal transpose $Q^{\mathsf t}$ is determined by

\[
x_i^{\mathsf t}=x_i,\qquad
\partial_i^{\mathsf t}=-\partial_i,\qquad
(Q_1Q_2)^{\mathsf t}=Q_2^{\mathsf t}Q_1^{\mathsf t}.
\tag{6.4}
\]

There is no complex conjugation, including when its coefficients depend on $s$. Integration by parts in one real coordinate, with compact support killing both endpoints, proves the formula for one derivative. Repeated application proves it for every monomial and hence every $Q$. Accordingly $(Qu)(\phi)=u(Q^{\mathsf t}\phi)$ defines its action on distributions. A transpose of order $r$ sends a compact test to one on the same support and satisfies $p_{K,0}(Q^{\mathsf t}\phi)\leq C_Kp_{K,r}(\phi)$. Polynomial coefficients and the finite Leibniz formula likewise give $q_{L,0}(Q^{\mathsf t}\phi)\leq Cq_{L',r}(\phi)$ for some $L'$. The constants can be chosen uniformly for $s$ in a compact parameter set. Thus polynomial families of these operators preserve the holomorphic families just constructed.

#### Real powers and the zero set

Choose an identity $P(s)f^{s+1}=b_f(s)f^s$ from Section 3, and let $r$ be the differential order of $P$. On $\Omega$, interpret $f^s=\exp(s\log f)$ with the real logarithm; the product rule makes the formal identity an identity of ordinary functions there. Write $T_\Omega(s)=1_\Omega f^s$, initially for $\operatorname{Re}s>0$. The integral observation proves its holomorphy in both compact-test and Schwartz-test bounds.

We must justify extension through the boundary before integrating by parts. On compact sets, every spatial derivative of order $j\leq r$ of $f^{s+1}$ inside $\Omega$ is a finite sum of a polynomial in $s$, products of derivatives of $f$, and $f^{s+1-h}$ with $h\leq j$. If $\operatorname{Re}(s+1)>r$, these expressions tend to zero at the boundary. More precisely, near a boundary point $x_0$ the mean-value formula and $f(x_0)=0$ give $|f(x)|\leq C|x-x_0|$. For $j<r$, the expressions of order $j$ are therefore $O(|x-x_0|^{\operatorname{Re}(s+1)-j})=o(|x-x_0|)$. Their extensions by zero have derivative zero at the boundary. Induction on $j$ proves that $1_\Omega f^{s+1}$ is $C^r$ with exactly those extended derivatives. This argument uses no smoothness of $\partial\Omega$ and introduces no boundary delta term.

Consequently, for $\operatorname{Re}s$ sufficiently large, ordinary differentiation and (6.4) give an equality of distributions

\[
b_f(s)T_\Omega(s)=P(s)T_\Omega(s+1).
\tag{6.5}
\]

Both sides are holomorphic for $\operatorname{Re}s>0$, so testwise analytic uniqueness extends (6.5) throughout that half-plane. For $N\geq0$ define

\[
\begin{gathered}
B_N(s)=\prod_{j=0}^{N-1}b_f(s+j),\\
Q_N(s)=P(s)P(s+1)\cdots P(s+N-1),
\end{gathered}
\tag{6.6}
\]

with empty products equal to one and with the rightmost operator acting first. The formula

\[
\begin{gathered}
T_{\Omega,N}(s)=\frac{Q_N(s)T_\Omega(s+N)}{B_N(s)}\\
\text{on }\operatorname{Re}s>-N
\end{gathered}
\tag{6.7}
\]

is meromorphic there. Its numerator is a holomorphic distribution family with the finite bounds above. Iterating (6.5) shows equality with $T_\Omega(s)$ in the initial half-plane away from denominator zeros. Therefore all formulas (6.7) agree on overlaps by analytic uniqueness. These half-planes cover $\mathbb C$, and the zeros of their denominators are precisely among (6.1).

Take $\Omega=\{f>0\}$ and then apply this construction to $-f$ on $\{f<0\}$. Section 3 proved $b_{-f}=b_f$; an operator for $-f$ is $-P(s)$ under the identification of their formal-power symbols. The sum of these two families is $|f|^s$ in the initial half-plane and hence gives its unique continuation. Values on $f=0$ were defined as zero there, so no assertion about the measure of the zero set is needed for this identity.

#### Complex powers without assuming rational roots

Use Wirtinger derivatives $\partial_{z_i}=\tfrac12(\partial_{x_i}-i\partial_{y_i})$ on $\mathbb C^n$, with Lebesgue measure in the $2n$ real coordinates. For each integer $N\geq0$ set

\[
\begin{gathered}
U_N(s)=f^N|f|^{2s},\\
H_N=\{s:\operatorname{Re}s>-N/2\},
\end{gathered}
\tag{6.8}
\]

initially as a locally integrable function on $H_N$, equal to zero at $f=0$. Its modulus off that zero set is $|f|^{N+2\operatorname{Re}s}$; the residual phase $(f/|f|)^N$ is independent of $s$ and has modulus one. The integral observation, with $a=N$ and $c=2$, proves that $U_N$ is holomorphic on $H_N$ with common compact-test and Schwartz-test bounds.

Off the zero set choose any local holomorphic logarithm $\ell$ of $f$. It exists near each nonzero value by the convergent series for $\log(1+w)$ after factoring out that value. Then

\[
U_N(s)=\exp((s+N)\ell+s\overline\ell).
\tag{6.9}
\]

Changing the logarithm by $2\pi i k$ leaves (6.9) unchanged because $N$ is an integer. Every holomorphic derivative leaves the antiholomorphic factor alone. Applying the functional equation with parameter $s+j$, and then proceeding from $j=N-1$ down to $j=0$, gives off the zero set

\[
Q_N(s)U_N(s)=B_N(s)|f|^{2s}.
\tag{6.10}
\]

To check it distributionally, first take $\operatorname{Re}s$ sufficiently large. On the complex plane the function $w^N|w|^{2s}$, set to zero at $w=0$, is $C^m$ whenever $N+2\operatorname{Re}s>m$. Indeed its real derivatives away from zero of order $j\leq m$ are bounded by $C|w|^{N+2\operatorname{Re}s-j}$; extending these by zero and using the difference-quotient induction from the real case proves the assertion. Composition with the polynomial map $f$ proves the needed differentiability of $U_N$. Choosing $m$ at least the order of $Q_N$ justifies (6.10) across the zero set and integration by parts. Both sides are holomorphic distribution families on $\operatorname{Re}s>0$, so (6.10) holds throughout that half-plane by uniqueness.

Now define

\[
Z_N(s)=\frac{Q_N(s)U_N(s)}{B_N(s)}
\quad\text{on }H_N.
\tag{6.11}
\]

Its numerator is holomorphic by (6.8) and the transpose bounds. Every $Z_N$ agrees with the original $|f|^{2s}$ where $\operatorname{Re}s>0$ away from denominator zeros. Thus the $Z_N$ agree on every overlap, and $\bigcup_NH_N=\mathbb C$ proves continuation with exactly the possible pole set (6.1). Only the polynomials $b_f(s+j)$ occur: this proof has not assumed that their coefficients or roots are real. Replacing $s$ by $s/2$ gives the claimed convention for $|f|^s$ on complex space.

#### Pole order, temperedness and two checks

At a fixed $s_0$, choose $N$ so that $s_0$ lies strictly inside the half-plane used in (6.7) or (6.11). The numerator is holomorphic in one test-seminorm bound on a disk there. The pole order is at most

\[
\operatorname{ord}_{s_0}B_N
=\sum_{j=0}^{N-1}\operatorname{mult}_{s_0+j}(b_f),
\tag{6.12}
\]

independently of the test. Expand the numerator in its locally convergent, seminorm-bounded power series and divide by the finite-order zero of $B_N$. This proves that all Laurent coefficients are continuous functionals, rather than merely a collection of unrelated scalar residues. The same argument with $q_{L,r}$ proves temperedness and uniform Schwartz bounds. The initial distributional identities hold for Schwartz tests as well: a smooth cutoff $\chi(x/R)$, equal to one near zero, satisfies $\chi(x/R)\phi\to\phi$ in every Schwartz seminorm. The Leibniz formula proves this by bounding the tails with one higher weight and the cutoff derivatives by $R^{-j}$. Compact-test equality therefore extends by continuity. This completes the proof of Theorem 6.1. $\square$

As a normalization check, take a compact test $\phi$ equal to one near zero. On the real line,

\[
\int_{-\varepsilon}^{\varepsilon}|x|^s\,dx
=\frac{2\varepsilon^{s+1}}{s+1};
\tag{6.13}
\]

on the complex line with real Lebesgue area measure,

\[
\int_{|z|<\varepsilon}|z|^{2s}\,dx\,dy
=\frac{\pi\varepsilon^{2s+2}}{s+1}.
\tag{6.14}
\]

The portions away from zero are entire. For arbitrary smooth tests subtract $\phi(0)$ near zero; the remainder is $O(|x|)$ or $O(|z|)$, which is integrable on a neighborhood of $s=-1$. Thus the residues at $-1$ are respectively $2\delta_0$ and $\pi\delta_0$. For $|z|^s$ the pole is at $-2$ and the residue is $2\pi\delta_0$. These computations verify both the parameter scaling and the normalization; they do not assert that every candidate pole occurs for every polynomial.

An alternative complex recurrence explains a common conjugation pitfall. If $b^*(s)=\overline{b_f(\overline s)}$ and $P^*(s)$ conjugates the coefficients of $P$ while replacing $z,\partial_z$ by $\overline z,\partial_{\overline z}$, leaving the indeterminate $s$ fixed, then

\[
\begin{aligned}
&b_f(s)b^*(s)|f|^{2s}\\
&\qquad=P(s)P^*(s)|f|^{2(s+1)}.
\end{aligned}
\tag{6.15}
\]

On a logarithm chart this follows by applying the two equations to their separate holomorphic and antiholomorphic factors; the zero-set and transpose arguments above extend it distributionally. It gives a continuation whose displayed denominator involves both root sets. Substituting $b^*=b_f$ is justified by the separately stated rationality theorem, not by taking $\overline{s}=s$. Nor does a whole differential operator annihilate an antiholomorphic factor merely because its positive-order holomorphic derivatives do: its zeroth-order term remains. Formula (6.11) avoids both issues and already gives the sharper pole set (6.1).

The source context is Bernstein, [*The analytic continuation of generalized functions with respect to a parameter*](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-a-cont-FAN.pdf), Theorem 1, and Popa, [*The Bernstein–Sato polynomial*](https://people.math.harvard.edu/~mpopa/notes/Bernstein-Sato-notes.pdf), Theorem 5.2, Lemma 5.3 and Exercise .6. The proof here explicitly supplies the zero-set justification, parameter-independent distribution bounds, transposes, and the shifted-power route (6.8)–(6.11).

For complementary one-variable constructions, read *Finite parts of singular powers* and *Complex powers at a boundary*. Their finite parts and upper/lower boundary values are not being substituted for Theorem 6.1's general-polynomial proof. The formal symbol $f^s$ of Section 1 remains algebraic; the distributions in this section are constructed by test integrals and continuation.

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

The growth criterion, holonomicity over $k(s)$, Bernstein's existence theorem, field invariance, the factor $s+1$, localization of arbitrary holonomic Weyl modules, a generating denominator for $R_f$, and the coordinate-power and quadratic minimal polynomials are proved here. All six exercises are solved. Theorem 6.1 proves general real and complex distributional continuation, the precise candidate pole progressions, and temperedness, without assuming the negative-rational-root theorem. Section 5 proves the cusp polynomial by an explicit operator and two nonzero test-integral residues. The general weighted-homogeneous formula and its minimality, and Kashiwara's negative-rational-root theorem, remain explicitly stated external results.

R. Bezrukavnikov, [*Noncommutative Algebra*, MIT 18.706](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_full_lec.pdf), Sections 24.1 and 24.6, supplies the broader growth context. V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Section 4.2, especially Theorem 4.2.9.2, treats localization by a Bernstein growth estimate. The proof above counts cumulative filtered dimensions, uses only an upper bound for a possibly nongood localization filtration, and establishes finite generation before invoking finite length on the ambient module.

Section 6 identifies the analytic sources and distinguishes the proved continuation theorem from the still-external negative-rational-root theorem. Section 5 distinguishes the direct cusp proof from the broader weighted-homogeneous formula and records the exact external locators. The algebraic existence and localization proofs depend only on the preceding chapter's growth and finite-length theorems.

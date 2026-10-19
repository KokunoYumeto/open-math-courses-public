# Factorization, hereditary corners and quotient lifts

*Mathematical exposition by GPT-6 Astra (OpenAI), October 2026. Original course contributions: CC0.*

Passing to a quotient can turn a nonzero product into zero. The main construction in this lesson changes the two original factors by elements of the ideal so that their product becomes exactly zero upstairs. Positive parts provide the orthogonality; a balanced factorization puts the polar factors back inside the C*-algebra. Along the way, the same tools identify hereditary corners and explain how a primitive algebra detects compact operators.

All algebras are complex C*-algebras, with no separability or identity assumption. An ideal is a norm-closed two-sided ideal unless another meaning is specified. Write \(q:A\to A/I\) for the quotient map and \(\widetilde A\) for the forced unitization. Functions vanishing at zero are evaluated inside \(A\); other continuous functions are evaluated in \(\widetilde A\). The zero algebra is allowed, but an irreducible representation is required to be nonzero. A primitive algebra therefore has a faithful irreducible representation on a nonzero Hilbert space.

The earlier programme proofs used here are the continuous functional calculus, Theorems 5.1 and 5.3 and Corollary 5.4, positive approximate identities, Theorem 11.4 and Corollary 11.5, and C*-quotients, Theorem 15.1. Faithful representations and the scalar-commutant criterion are proved in the GNS lesson, Theorem 7.2 and Theorem 2.2. We also use the double commutant theorem, Theorem 4.4. The proofs below give the additional corner, factorization and lifting arguments explicitly.

## Multiplication domains and balanced factors

**Lemma 1.1.** Suppose that \(A\) is contained isometrically as a C*-subalgebra of a C*-algebra \(N\), and \(a\in N\). Then

\[
M_a=\{x\in A:ax\in A\}
\]

is a closed right ideal of \(A\). More generally, for \(a\in A\),

\[
R_{a,I}=\{x\in A:ax\in I\},\qquad
L_{a,I}=\{x\in A:xa\in I\}
\]

are respectively closed right and left ideals.

**Proof.** Multiplication by \(a\) is bounded and linear. The inverse image of the closed linear space \(A\), or \(I\), is a closed linear space. If \(ax\in A\) and \(b\in A\), then \(a(xb)=(ax)b\in A\). If \(ax\in I\), the same product belongs to \(I\). The identity \((bx)a=b(xa)\) proves the left-ideal assertion. \(\square\)

**Lemma 1.2 (polar factors and norm approximation).** In a faithful concrete representation of \(A\), each \(x\in A\) has a polar decomposition \(x=u h\), where \(h=|x|=(x^*x)^{1/2}\), \(u\) is a partial isometry, and \(u^*u\) is the projection onto \(\overline{hH}\). Although \(u\) need not belong to \(A\),

\[
u h^{1/2}\in A,\qquad
\left\|u h^{1/2}-x(h+\varepsilon)^{-1/2}\right\|
\leq\sqrt{\varepsilon}.
\]


**Proof.** The rule \(h\xi\mapsto x\xi\) is well defined and isometric, since \(\|h\xi\|^2=\langle x^*x\xi,\xi\rangle=\|x\xi\|^2\). Extend it to \(\overline{hH}\) and set it equal to zero on its orthogonal complement. This constructs \(u\), gives \(x=uh\), and identifies its initial projection. For \(t\geq0\),

\[
0\leq\sqrt t-\frac{t}{\sqrt{t+\varepsilon}}
=\frac{\varepsilon\sqrt t}
 {\sqrt{t+\varepsilon}(\sqrt{t+\varepsilon}+\sqrt t)}
\leq\sqrt{\varepsilon}.
\]

The functional calculus and \(\|u\|\leq1\) give the asserted estimate. Each approximant \(x(h+\varepsilon)^{-1/2}\) lies in \(A\), because \(A\) is an ideal in its unitization. Norm closure gives \(uh^{1/2}\in A\). \(\square\)

**Theorem 1.3 (balanced factorization).** Every \(x\in A\) can be written \(x=yz\), with \(y,z\in A\) and

\[
\|y\|=\|z\|=\|x\|^{1/2}.
\]


**Proof.** For \(x=0\), take both factors zero. Otherwise use Lemma 1.2 and set \(y=uh^{1/2}\), \(z=h^{1/2}\). Then \(yz=uh=x\), and

\[
y^*y=h^{1/2}u^*uh^{1/2}=h.
\]

Consequently \(\|y\|^2=\|h\|=\|x\|\), while \(\|z\|^2=\|h\|\) by the functional calculus. \(\square\)

The application \(N=A^{**}\) in Lemma 1.1 is legitimate. The lemma itself needs only an isometric inclusion and bounded multiplication, so no dual-space result is needed for that application.

## Lifts with exactly the quotient norm

The two lifting statements below also appear, with full proofs, as Proposition 17.1 in the C*-algebra lesson. We give the constructions here because the distinction between functions in \(A\) and in \(\widetilde A\) will matter in the zero-product argument.

**Theorem 2.1.** Every self-adjoint \(b\in A/I\) has a self-adjoint lift \(B\in A\) with \(\|B\|=\|b\|\). A positive \(b\) has such a lift that is positive.

**Proof.** If \(b=0\), choose \(B=0\). Otherwise put \(r=\|b\|\), choose any lift \(a\), and replace it by \(k=(a+a^*)/2\). For the continuous clipping function

\[
g(t)=\max(-r,\min(t,r)),
\]

we have \(g(0)=0\), so \(B=g(k)\in A\). It is self-adjoint and \(\|B\|\leq r\). Functional calculus commutes with the quotient homomorphism, and \(g\) is the identity on the spectrum of \(b\). Thus \(q(B)=g(b)=b\). Contractivity of \(q\) forces \(r\leq\|B\|\), hence equality. For positive \(b\), use \(g_+(t)=\min(r,\max(0,t))\). \(\square\)

**Theorem 2.2.** Every \(b\in A/I\) has a lift \(B\in A\) with \(\|B\|=\|b\|\).

**Proof.** Again the zero case is immediate. For \(r=\|b\|>0\), choose \(a\in A\) with \(q(a)=b\), set \(h=|a|\), and define

\[
f(0)=1,\qquad f(t)=\min(1,r/t)\quad(t>0).
\]

This function is continuous on \([0,\infty)\). Form \(f(h)\) in the unitization and put \(B=af(h)\in A\). Since \(h\) commutes with \(f(h)\),

\[
B^*B=h^2f(h)^2,\qquad
\|B\|^2=\max_{t\in\sigma_{\widetilde A}(h)}t^2f(t)^2
\leq r^2.
\]

The quotient map extends to the unital map \(\widetilde q:\widetilde A\to\widetilde{A/I}\). It sends \(h\) to \(|b|\). On the spectrum of \(|b|\), the function \(f\) is identically one, so

\[
q(B)=b f(|b|)=b.
\]

Contractivity again gives the opposite norm inequality. \(\square\)

These proofs use no compactness of a minimizing sequence. They explicitly turn any lift into a lift attaining the quotient norm.

## Transport between hereditary corners

A C*-subalgebra \(D\subseteq A\) is *hereditary* if \(0\leq x\leq d\), with \(x\in A\) and \(d\in D_+\), implies \(x\in D\). For \(h\in A_+\), write

\[
D_h=\overline{hAh}^{\|\cdot\|}.
\]


**Lemma 3.1.** The algebra \(D_h\) is hereditary. For \(e_\varepsilon=h(h+\varepsilon)^{-1}\),

\[
x\in D_h\quad\Longleftrightarrow\quad
e_\varepsilon x\longrightarrow x\quad\hbox{and}\quad
xe_\varepsilon\longrightarrow x
\quad\hbox{in norm}.
\]


**Proof.** The space \(hAh\) is closed under adjoints and products: \((hah)(hbh)=h(ah^2b)h\). Thus its closure is a C*-subalgebra. If \((v_i)\) is a positive contractive approximate identity of \(A\), then \(hv_i h\to h^2\), so \(h^2\in D_h\). Functional calculus in \(D_h\) gives \(h\in D_h\) and \(e_\varepsilon\in D_h\).

The estimate \(\|(1-e_\varepsilon)h\|\leq\varepsilon\) shows that \(e_\varepsilon x\to x\) and \(xe_\varepsilon\to x\) for \(x\in hAh\). Contractivity extends both statements to its closure. Conversely, both convergences imply \(e_\varepsilon x e_\varepsilon\to x\), and

\[
e_\varepsilon x e_\varepsilon
=h\big((h+\varepsilon)^{-1}x(h+\varepsilon)^{-1}\big)h
\in hAh.
\]

The expression in parentheses belongs to \(A\), even when the inverses only belong to the unitization.

For heredity, let \(0\leq x\leq d\in D_h\). Positivity under conjugation and the C*-identity give

\[
\begin{aligned}
\|(1-e_\varepsilon)x^{1/2}\|^2
&=\|(1-e_\varepsilon)x(1-e_\varepsilon)\|\\
&\leq\|(1-e_\varepsilon)d(1-e_\varepsilon)\|
\longrightarrow0.
\end{aligned}
\]

Multiplying by \(x^{1/2}\) proves \((1-e_\varepsilon)x\to0\); taking adjoints proves \(x(1-e_\varepsilon)\to0\). The characterization just proved yields \(x\in D_h\). \(\square\)

**Theorem 3.2 (polar transport).** For \(a\in A\), the C*-algebras

\[
\overline{a^*Aa}\quad\hbox{and}\quad\overline{aAa^*}
\]

are isometrically *-isomorphic. If \(a=uh\) is its polar decomposition, the isomorphism is \(b\mapsto ubu^*\).

**Proof.** First prove \(\overline{a^*Aa}=D_h\), where \(h=|a|\). Denote the left side by \(B\). Products of generators are again of that form, so \(B\) is a C*-subalgebra. Approximate identities give \(a^*v_i a\to a^*a=h^2\); hence \(h\in B\). Also \(BAB\subseteq B\): on generators,

\[
(a^*ba)c(a^*da)=a^*(bac a^*d)a,
\]

and norm limits preserve membership. Therefore \(hAh\subseteq B\), giving \(D_h\subseteq B\). For \(b\in A_+\),

\[
0\leq a^*ba\leq\|b\|h^2.
\]

Lemma 3.1 puts \(a^*ba\) in \(D_h\). Every element of \(A\) is a linear combination of positive elements: split its real and imaginary parts into positive and negative parts. This proves the reverse inclusion. Applying the same argument to \(a^*\) gives \(\overline{aAa^*}=D_k\), with \(k=|a^*|\).

Let \(p=u^*u\). Since \(ph=h=hp\), every element of \(D_h\) is supported on \(p\). Thus conjugation by \(u\) is a *-homomorphism on \(D_h\), and conjugation by \(u^*\) is its inverse on its image. In particular it is isometric. On the dense generators,

\[
u(hbh)u^*=aba^*\qquad(b\in A).
\]

Its closed image is exactly \(\overline{aAa^*}=D_k\). The formula therefore defines a map between subalgebras of \(A\), even though \(u\) may lie outside \(A\). \(\square\)

## Primitive algebras and hereditary subalgebras

**Proposition 4.1.** If \(A\) is primitive and \(x,y\in A\) are nonzero, then \(xAy\neq\{0\}\).

**Proof.** Realize \(A\) faithfully and irreducibly on \(H\). Choose \(\xi\) with \(\eta=y\xi\neq0\). Every nonzero vector is cyclic: \(\overline{A\eta}\) is an invariant subspace, is nonzero by nondegeneracy, and thus equals \(H\). If \(xay=0\) for every \(a\in A\), the operator \(x\) vanishes on the dense space \(A\eta\), and hence vanishes on \(H\). Faithfulness contradicts \(x\neq0\). \(\square\)

**Theorem 4.2.** Every nonzero hereditary C*-subalgebra of a primitive C*-algebra is primitive.

**Proof.** Continue with a faithful irreducible realization \(A\subseteq B(H)\). Let \(B\subseteq A\) be nonzero and hereditary, and let \(q\) be the projection onto \(\overline{BH}\). A positive contractive approximate identity \((e_i)\) of \(B\) converges strongly to \(q\): convergence holds on vectors \(b\xi\), follows on their closed span by the uniform contraction bound, and every \(e_i\) vanishes on \(q^\perp H\). Also \(b=qbq\) for \(b\in B\), so restriction to \(qH\) is faithful and nondegenerate.

For \(a\in A_+\),

\[
0\leq e_i a e_i\leq\|a\|e_i^2.
\]

Heredity gives \(e_i a e_i\in B\). Decomposing an arbitrary \(a\) into four positive terms shows \(e_i A e_i\subseteq B\). Schur's lemma and the double commutant theorem give the strong closure \(\overline A^{\mathrm s}=B(H)\). For each fixed \(i\) and \(T\in B(H)\), approximate \(T\) strongly by elements of \(A\); multiplication on either side by the fixed \(e_i\) is strongly continuous. Hence \(e_iTe_i\) lies in the strong closure of \(B\).

Finally \(e_iTe_i\to qTq\) strongly, using \(\|e_i\|\leq1\). All operators on \(qH\) occur as compressions \(qTq\). The strong closure of the compressed \(B\) is therefore \(B(qH)\), whose commutant consists of scalars. The representation on \(qH\neq0\) is irreducible and faithful. \(\square\)

The nonzero condition is required by our convention for irreducible representations: the zero algebra has no nonzero representation. No countability condition occurs in the proof.

## Detecting the compact operators

Write \(K(H)\) for the norm closure of the finite-rank operators. For vectors \(\xi,\eta\), use \(\theta_{\xi,\eta}(\zeta)=\langle\zeta,\eta\rangle\xi\), with the inner product linear in its first argument.

**Theorem 5.1.** For a primitive algebra \(A\), the following conditions are equivalent:

1. Some faithful irreducible representation \(\pi:A\to B(H)\) satisfies \(K(H)\subseteq\pi(A)\).
2. There is \(a\in A\) for which the complex vector space \(aAa^*\) has dimension one.

If condition 2 holds, every faithful irreducible realization of \(A\) contains the compact operators on its representation space.

**Proof.** Suppose first that \(A\subseteq B(H)\) faithfully and \(K(H)\subseteq A\). A rank-one projection \(p\) belongs to \(A\), and \(pAp=\mathbb Cp\), since \(pB(H)p=\mathbb Cp\) and \(p\in pAp\). Take \(a=p\).

Conversely, let \(\dim aAa^*=1\). This finite-dimensional space is closed and nonzero, and Theorem 3.2 identifies it as a hereditary C*-subalgebra \(D\). Approximate identities put the nonzero element \(d=aa^*\) in \(D\). Since \(D=\mathbb Cd\), we have \(d^2=\lambda d\). Positivity and the C*-identity give \(\lambda=\|d\|>0\), so \(p=d/\lambda\) is a nonzero projection and \(D=\mathbb Cp\). Heredity, applied first to positive \(b\in A\), gives \(pAp\subseteq D\), and \(p\in pAp\) gives equality.

Choose any faithful irreducible representation and identify \(A\) with its image. Strong density of \(A\) in \(B(H)\) implies that \(pAp\) is strongly dense in \(pB(H)p\). The space \(\mathbb Cp\) is strongly closed: convergence can be tested on any nonzero vector in \(pH\), which forces convergence of the scalar coefficients. Hence \(pB(H)p=\mathbb Cp\), forcing \(\dim pH=1\). Write \(p=\theta_{\xi,\xi}\) with \(\|\xi\|=1\).

For \(b,c\in A\),

\[
bpc=\theta_{b\xi,c^*\xi}\in A.
\]

Cyclicity gives density of both \(A\xi\) and \(A^*\xi\) in \(H\). The estimate

\[
\|\theta_{\eta,\zeta}-\theta_{\eta',\zeta'}\|
\leq\|\eta-\eta'\|\,\|\zeta\|
 +\|\eta'\|\,\|\zeta-\zeta'\|
\]

then shows that every rank-one operator is a norm limit of elements \(bpc\). Finite sums and norm closure give \(K(H)\subseteq A\). \(\square\)

## The irreducible representation that sees the compact ideal

**Theorem 6.1.** Let \(H\neq0\) and \(K(H)\subseteq A\subseteq B(H)\). If \(\rho:A\to B(K)\) is irreducible and \(\rho(K(H))\neq0\), then \(\rho\) is unitarily equivalent to the given action on \(H\).

**Proof.** Products of a bounded operator with a finite-rank operator are finite rank. Taking norm limits shows that \(K(H)\) is an ideal of \(A\). Consequently \(\overline{\rho(K(H))K}\) is a nonzero invariant subspace for \(\rho(A)\); irreducibility makes it all of \(K\).

Choose an orthonormal basis \((\xi_j)_{j\in J}\) of \(H\), a distinguished index \(0\in J\), and matrix units \(e_{ij}=\theta_{\xi_i,\xi_j}\). The finite sums \(p_F=\sum_{j\in F}e_{jj}\), directed by finite subsets of \(J\), form an approximate identity of \(K(H)\). Indeed \(p_F\xi\to\xi\) for each vector; the rank-one formula gives norm convergence on rank-one operators, then on finite sums and finally on their norm closure. The essential-subspace assertion above therefore implies \(\rho(p_F)\to1_K\) strongly.

The projection \(\rho(e_{00})\) is nonzero. Otherwise the factorization \(e_{ij}=e_{i0}e_{00}e_{0j}\) would kill every matrix unit under \(\rho\), and density would give \(\rho(K(H))=0\). Put \(L=\rho(e_{00})K\). On finite sums define

\[
U:H\otimes L\longrightarrow K,\qquad
U(\xi_j\otimes\eta)=\rho(e_{j0})\eta.
\]

The matrix-unit relations give

\[
\left\|\sum_j\rho(e_{j0})\eta_j\right\|^2
=\sum_j\|\eta_j\|^2.
\]

Thus \(U\) extends to an isometry. Its range contains \(\rho(p_F)K\) for every finite \(F\), because
\(\rho(e_{jj})\zeta=\rho(e_{j0})\rho(e_{0j})\zeta\)
and \(\rho(e_{0j})\zeta\in L\). These ranges are dense in \(K\), so \(U\) is onto.

For \(a\in A\), write \(a_{ij}=\langle a\xi_j,\xi_i\rangle\). The identity

\[
e_{0i}ae_{j0}=a_{ij}e_{00}
\]

shows that the \((i,j)\) matrix entry of \(U^*\rho(a)U\), acting between copies of \(L\), is \(a_{ij}1_L\). Equality of all matrix entries on the dense finite sums gives

\[
U^*\rho(a)U=a\otimes1_L.
\]

If \(\dim L>1\), any nonzero proper closed subspace \(L_0\subset L\) gives the nonzero proper invariant subspace \(H\otimes L_0\). Irreducibility rules this out. Thus \(\dim L=1\), and the displayed unitary identifies \(\rho\) with the original action on \(H\). \(\square\)

The proof uses a net of finite subsets of a basis, so it covers Hilbert spaces of arbitrary dimension.

## Lifting zero products

For self-adjoint \(s\), define \(s_+=(|s|+s)/2\) and \(s_-=(|s|-s)/2\). Continuous functional calculus gives \(s_+s_-=0\).

**Lemma 7.1 (orthogonal positive lifts).** Suppose \(x,y\in A_+\) and \(xy\in I\). Then

\[
C=(x-y)_+,\qquad D=(x-y)_-
\]

satisfy \(C,D\in A_+\), \(CD=0\), \(q(C)=q(x)\), and \(q(D)=q(y)\).

**Proof.** Put \(s=q(x)\), \(t=q(y)\). Positivity and \(st=0\) imply \(ts=(st)^*=0\). Hence

\[
(s-t)^2=s^2+t^2=(s+t)^2.
\]

Since \(s+t\geq0\), uniqueness of the positive square root gives \(|s-t|=s+t\). Therefore \((s-t)_+=s\) and \((s-t)_-=t\). Quotient compatibility of the functional calculus proves the required images. The same calculus gives \(CD=0\) inside \(A\). \(\square\)

**Lemma 7.2.** If \(X,Y\) belong to a C*-algebra and \(XY=0\), then

\[
|X|^{1/2}|Y^*|^{1/2}=0.
\]


**Proof.** Set \(H=|X|\), \(K=|Y^*|\). Since \(X^*XY=0\),

\[
(HY)^*(HY)=Y^*X^*XY=0,
\]

so \(HY=0\). It follows that

\[
(KH)^*(KH)=HK^2H=HYY^*H=0.
\]

Thus \(KH=0\), and taking adjoints gives \(HK=0\). For a positive element, the square-root function can be uniformly approximated on its spectrum by polynomials having zero constant term: start with polynomial approximants to \(\sqrt t\) on an interval containing zero and subtract their values at zero. Every product of such a polynomial in \(H\) with one in \(K\) vanishes, since \(HK=KH=0\). Passing to norm limits gives \(H^{1/2}K^{1/2}=0\). The polynomial approximation is the same continuous-calculus construction used in Section 1. \(\square\)

**Theorem 7.3 (zero products lift exactly).** If \(x,y\in A\) satisfy \(xy\in I\), there are \(a,b\in I\) such that

\[
(x-a)(y-b)=0.
\]


**Proof.** Work in a faithful concrete representation and write

\[
x=u|x|=uc^2,\qquad y=|y^*|v=d^2v,
\qquad c=|x|^{1/2},\quad d=|y^*|^{1/2}.
\]

The right polar expression for \(y\) follows by applying Lemma 1.2 to \(y^*\) and taking adjoints. Balanced factorization gives \(uc\in A\) and \(dv\in A\). Applying Lemma 7.2 in the quotient gives \(q(c)q(d)=0\), so \(cd\in I\). Lemma 7.1 applied to \(c,d\) supplies

\[
C=(c-d)_+,\quad D=(c-d)_-,\quad CD=0,
\quad q(C)=q(c),\quad q(D)=q(d).
\]

Set

\[
X=(uc)C,\qquad Y=D(dv).
\]

These are elements of \(A\), and associativity gives \(XY=(uc)(CD)(dv)=0\). Moreover

\[
q(X)=q(uc)q(c)=q(x),\qquad
q(Y)=q(d)q(dv)=q(y).
\]

Thus \(a=x-X\) and \(b=y-Y\) belong to \(I\), and they have the required property. All uses of \(q\) are on elements of \(A\); no quotient map has been applied to the possibly external polar factors \(u\) or \(v\). \(\square\)

The closed one-sided ideals in Lemma 1.1 describe the same zero-product constraint before choosing lifts. The explicit construction above also supplies positive orthogonal lifts when the original factors are positive.

## Worked examples and proof checks

**Example 8.1 (balanced factors and clipping).** Let \(A=C([0,1],M_2(\mathbb C))\), let \(q\) be evaluation at zero, and put \(x(t)=(1+t)e_{12}\). Find balanced factors and a lift of \(q(x)\) with its exact norm.

**Solution.** We have \(|x|(t)=(1+t)e_{22}\). The factors

\[
y(t)=\sqrt{1+t}\,e_{12},\qquad
z(t)=\sqrt{1+t}\,e_{22}
\]

satisfy \(yz=x\), with \(\|y\|=\|z\|=\sqrt2=\sqrt{\|x\|}\). The quotient element is \(e_{12}\), of norm one. In Theorem 2.2, the clipping factor acts as \((1+t)^{-1}\) on the second coordinate and as one on the first. Consequently \(B(t)=e_{12}\) for all \(t\), and \(\|B\|=\|q(x)\|=1\).

**Example 8.2 (the two corners act on different subspaces).** Take \(a=e_{12}\in M_2(\mathbb C)\). Determine both hereditary corners and the polar transport.

**Solution.** Direct multiplication gives

\[
a^*M_2a=\mathbb Ce_{22},\qquad
aM_2a^*=\mathbb Ce_{11}.
\]

The partial isometry is \(u=e_{12}\), and \(u(\lambda e_{22})u^*=\lambda e_{11}\). Each corner acts faithfully and irreducibly on its one-dimensional support. Its action on all of \(\mathbb C^2\) is degenerate; Theorem 4.2 explicitly passes to the support space.

**Example 8.3 (a product vanishes only in the quotient).** In the algebra of Example 8.1, put \(x(t)=e_{11}+te_{12}\), \(y(t)=e_{22}\), and \(I=\ker q\). Find ideal corrections with zero product.

**Solution.** The product is \(x(t)y(t)=te_{12}\), which is nonzero for \(t>0\) but lies in \(I\). Taking \(a(t)=te_{12}\), \(b(t)=0\) gives \(x-a=e_{11}\), \(y-b=e_{22}\), and \((x-a)(y-b)=0\). The element \(x-y\) is not self-adjoint for \(t>0\), so positive and negative parts cannot be applied to it as in Lemma 7.1. Theorem 7.3 instead applies them to the self-adjoint difference \(|x|^{1/2}-|y^*|^{1/2}\), which works without any special matrix formula.

**Example 8.4 (why the compact ideal must be seen).** Let \(H\) be infinite-dimensional and \(A=K(H)+\mathbb C1\). Show that the hypothesis \(\rho(K(H))\neq0\) in Theorem 6.1 cannot be omitted.

**Solution.** The identity is not compact: for every finite-rank \(F\), choose a unit vector in its kernel to get \(\|1-F\|\geq1\). Thus \(k+\lambda1\mapsto\lambda\) is a well-defined nonzero *-homomorphism \(A\to\mathbb C\), and so is a one-dimensional irreducible representation. It kills \(K(H)\). The given representation on the infinite-dimensional space \(H\) is irreducible because rank-one operators carry any nonzero vector to any prescribed vector. The two representation spaces have different dimensions, so these representations are not unitarily equivalent.

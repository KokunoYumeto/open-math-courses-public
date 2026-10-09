# Keller maps and the Jacobian conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A polynomial map \(F:k^n\to k^n\) whose inverse is again a polynomial map must have a Jacobian determinant that is a nonzero constant. In 1939 Ott-Heinrich Keller asked whether the converse holds: does a polynomial map with constant nonzero Jacobian determinant always have a polynomial inverse? In characteristic zero this question became known as the Jacobian conjecture. This lesson proves the classical reduction of the question to injectivity. Over an algebraically closed field of characteristic zero, a polynomial map with constant nonzero Jacobian determinant has a polynomial inverse exactly when it is injective, and exactly when a general point has a single preimage. The lesson also proves the cases of dimension one, of triangular maps and of maps of degree at most two, and the theorem of Ax and Grothendieck that injective polynomial maps are surjective. The next lesson, [A counterexample in dimension three](a-counterexample-in-dimension-three.md), shows that injectivity can fail.

We use the Nullstellensatz from [The Nullstellensatz and Jacobson rings](course:AG-CA/the-nullstellensatz-and-jacobson-rings), dimension theory from [Krull dimension and Noether normalization](course:AG-CA/krull-dimension-and-noether-normalization) and [Dimension theory of Noetherian local rings](course:AG-CA/dimension-theory-of-noetherian-local-rings), finiteness of minimal primes from [Noetherian and Artinian rings](course:AG-CA/noetherian-and-artinian-rings), unique factorization in polynomial rings from [Integral extensions: lying over, going up and going down](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down), and the fibre dimension theorem from [Dimension of fibres](course:AG-MO/dimension-of-fibres).

Basic references are [Bass–Connell–Wright] and [Keller].

## 1. Polynomial maps and their Jacobian determinant

Let \(k\) be a field. A **polynomial map** \(F=(F_1,\ldots,F_n):k^n\to k^n\) is a tuple of polynomials \(F_i\in k[x_1,\ldots,x_n]\). We compose polynomial maps by substitution: \((G\circ F)_i=G_i(F_1,\ldots,F_n)\). The identity map is \((x_1,\ldots,x_n)\). A polynomial map \(F\) is a **polynomial automorphism** if there is a polynomial map \(H\) with \(H\circ F\) and \(F\circ H\) both equal to the identity, as tuples of polynomials. When \(k\) is infinite, a polynomial is determined by its values on \(k^n\), so these identities may equally be read as identities of functions.

The **Jacobian matrix** of \(F\) is the matrix of formal partial derivatives

\[
JF=\Bigl(\frac{\partial F_i}{\partial x_j}\Bigr)_{1\le i,j\le n}\in M_n\bigl(k[x_1,\ldots,x_n]\bigr),
\]

and \(\det JF\in k[x_1,\ldots,x_n]\) is its **Jacobian determinant**. Formal partial derivatives obey the sum and product rules, so they obey the chain rule

\[
J(G\circ F)=\bigl(JG\circ F\bigr)\cdot JF ,
\tag{1.1}
\]

where \(JG\circ F\) means that \(F\) is substituted into every entry of \(JG\). For \(G\) a monomial, (1.1) follows from the product rule; both sides of (1.1) are additive in \(G\), so it holds for all \(G\).

**Proposition 1.1.** If \(F\) is a polynomial automorphism of \(k^n\), then \(\det JF\) is a nonzero constant.

**Proof.** Let \(H\) be an inverse. By (1.1), \((JH\circ F)\cdot JF=J(H\circ F)\) is the identity matrix. Taking determinants, \(\det(JH\circ F)\cdot\det JF=1\) in \(k[x_1,\ldots,x_n]\). So \(\det JF\) is a unit of the polynomial ring. A product of two nonzero polynomials has degree equal to the sum of their degrees, so the units are the nonzero constants. \(\square\)

**Definition 1.2.** A **Keller map** is a polynomial map \(F:k^n\to k^n\) whose Jacobian determinant is a nonzero constant.

The **Jacobian conjecture** is the assertion, going back to Keller's question of 1939, that over a field of characteristic zero every Keller map is a polynomial automorphism. *Reference:* [Keller], [Bass–Connell–Wright].

Composites of Keller maps are Keller maps, by (1.1). In dimension one the assertion is true: if \(f\in k[x]\) and \(f'=c\ne0\) is constant, then writing \(f=\sum_j a_jx^j\) gives \(ja_j=0\) for every \(j\geq2\). In characteristic zero this forces \(a_j=0\) for \(j\geq2\), so \(f=a_0+cx\), which has the inverse \(y\mapsto(y-a_0)/c\).

Over \(\mathbb R\) or \(\mathbb C\), a Keller map has an invertible derivative at every point. The inverse function theorem then gives a local inverse near every point, but it says nothing about global injectivity. The complex exponential function has nowhere vanishing derivative and takes every value infinitely often. The Jacobian conjecture asked whether the algebraic nature of a polynomial map rules out such behaviour.

The hypothesis on the characteristic cannot be dropped.

**Example 1.3.** Let \(k\) be an algebraically closed field of characteristic \(p>0\) and \(f(x)=x-x^p\). Then \(f'(x)=1-px^{p-1}=1\), so \(f\) is a Keller map of the line. But \(f(a)=a-a^p=0\) for every \(a\) in the prime field \(\mathbb F_p\subset k\), so \(f\) is not injective and has no inverse.

## 2. Keller maps are dominant and have finite fibres

From now on in Sections 2 to 4, \(k\) is an algebraically closed field of characteristic zero, and \(F=(F_1,\ldots,F_n)\) is a Keller map. Write

\[
A=k[y_1,\ldots,y_n],\qquad B=k[x_1,\ldots,x_n],\qquad \varphi:A\to B,\quad \varphi(y_i)=F_i .
\]

So \(\varphi\) is the \(k\)-algebra homomorphism \(P\mapsto P(F_1,\ldots,F_n)=P\circ F\). By the weak Nullstellensatz [The Nullstellensatz and Jacobson rings, Theorem 2.1](course:AG-CA/the-nullstellensatz-and-jacobson-rings#2-closed-points-detect-radical-equations), the points \(p\in k^n\) correspond to the maximal ideals \(\mathfrak m_p=(x_1-p_1,\ldots,x_n-p_n)\) of \(B\), and also to the \(k\)-algebra homomorphisms \(B\to k\), by evaluation at \(p\). The point \(p\) satisfies \(F(p)=q\) exactly when evaluation at \(p\), composed with \(\varphi\), is evaluation at \(q\).

**Proposition 2.1.** The polynomials \(F_1,\ldots,F_n\) are algebraically independent over \(k\). Equivalently, \(\varphi\) is injective.

**Proof.** Suppose not, and choose a nonzero \(P\in A\) of least total degree with \(P(F_1,\ldots,F_n)=0\). Then \(P\) is not constant. Differentiating with respect to \(x_j\) gives, for every \(j\),

\[
\sum_{i=1}^n\frac{\partial P}{\partial y_i}(F_1,\ldots,F_n)\,\frac{\partial F_i}{\partial x_j}=0 .
\]

In matrix form, \(v\cdot JF=0\) for the row vector \(v\) with entries \(v_i=\frac{\partial P}{\partial y_i}(F_1,\ldots,F_n)\in B\). The matrix \(JF\) is invertible over \(B\), because its determinant is a unit; so \(v=0\). Since \(P\) is not constant and \(k\) has characteristic zero, some \(\partial P/\partial y_i\) is a nonzero polynomial. It has smaller degree than \(P\) and vanishes at \((F_1,\ldots,F_n)\). This contradicts the choice of \(P\). \(\square\)

So the image of \(F\) lies in no hypersurface: if it lay in the zero set of a nonzero \(P\), the polynomial \(P\circ F\) would vanish at every point of \(k^n\), hence would be zero. In geometric language, \(F\) is dominant.

**Proposition 2.2.** For every \(q\in k^n\), the fibre \(F^{-1}(q)=\{p\in k^n:F(p)=q\}\) is finite.

**Proof.** Put \(I=(F_1-q_1,\ldots,F_n-q_n)\subset B\) and \(R=B/I\). The points of \(F^{-1}(q)\) correspond to the maximal ideals \(\mathfrak m_p\) containing \(I\), that is, to the maximal ideals of \(R\).

Fix such a point \(p\), and let \(\mathfrak n\) be the maximal ideal of the local ring \(R_{\mathfrak m_p}\). Expanding a polynomial in powers of \(x-p\) gives

\[
F_i-q_i=F_i-F_i(p)\equiv\sum_{j=1}^n\frac{\partial F_i}{\partial x_j}(p)\,(x_j-p_j)\pmod{\mathfrak m_p^2}.
\]

The matrix \(JF(p)\) is invertible, because \(\det JF(p)=\det JF\ne0\). Hence every \(x_j-p_j\) is a \(k\)-linear combination of the \(F_i-q_i\) modulo \(\mathfrak m_p^2\), and \(\mathfrak m_p\subset I+\mathfrak m_p^2\). In the local ring this says \(\mathfrak n=\mathfrak n^2\), so \(R_{\mathfrak m_p}\) has embedding dimension zero. By [Dimension theory of Noetherian local rings, Proposition 4.2 and the remark after it](course:AG-CA/dimension-theory-of-noetherian-local-rings#4-parameters-and-embedding-dimension), Nakayama's lemma gives \(\mathfrak n=0\), so \(R_{\mathfrak m_p}\) is a field. Then the only prime of \(R\) inside the maximal ideal at \(p\) is that maximal ideal itself, so every maximal ideal of \(R\) is a minimal prime of \(R\).

The ring \(R\) is Noetherian, so it has only finitely many minimal primes [Noetherian and Artinian rings, Proposition 2.2](course:AG-CA/noetherian-and-artinian-rings#2-polynomial-rings-and-finite-geometric-descriptions). Hence \(R\) has finitely many maximal ideals, and the fibre is finite. \(\square\)

## 3. The degree of a Keller map

Let \(K=k(x_1,\ldots,x_n)\) be the field of fractions of \(B\), and let \(L=k(F_1,\ldots,F_n)\subset K\) be the subfield generated by the components of \(F\). By Proposition 2.1, \(\varphi\) extends to an isomorphism \(k(y_1,\ldots,y_n)\to L\). The elements \(F_1,\ldots,F_n\) of \(K\) are algebraically independent, and \(K\) has transcendence degree \(n\) over \(k\). By [Krull dimension and Noether normalization, Lemma 1.3](course:AG-CA/krull-dimension-and-noether-normalization#1-chains-height-and-codimension), a maximal algebraically independent subset of \(K\) containing \(F_1,\ldots,F_n\) has exactly \(n\) elements, so it is \(\{F_1,\ldots,F_n\}\), and \(K\) is algebraic over \(L\). Since \(K=L(x_1,\ldots,x_n)\) is generated by finitely many algebraic elements, the degree \([K:L]\) is finite.

**Definition 3.1.** The **degree** of the Keller map \(F\) is \(\deg F=[K:L]\).

We need the classical primitive element argument in the following form.

**Lemma 3.2.** Let \(L\subset K\) be a finite extension of fields of characteristic zero, generated by \(\alpha_1,\ldots,\alpha_m\), and let \(k\subset L\) be an infinite subfield. There are \(c_2,\ldots,c_m\in k\) such that \(K=L(\alpha_1+c_2\alpha_2+\cdots+c_m\alpha_m)\).

**Proof.** By induction on \(m\), it suffices to treat \(K=L(\alpha,\beta)\). Let \(f\) and \(g\) be the minimal polynomials of \(\alpha\) and \(\beta\) over \(L\). An irreducible polynomial over a field of characteristic zero is coprime to its nonzero derivative, so it has distinct roots. In a field containing \(K\) over which \(fg\) splits, let \(\alpha=\alpha_1,\ldots,\alpha_r\) be the roots of \(f\) and \(\beta=\beta_1,\ldots,\beta_s\) those of \(g\). Only finitely many \(c\in k\) satisfy \(\alpha_i+c\beta_j=\alpha+c\beta\) for some \(i\) and some \(j\ne1\). Since \(k\) is infinite, choose \(c\in k\) outside this finite set, and put \(\theta=\alpha+c\beta\).

The polynomial \(h(X)=f(\theta-cX)\) has coefficients in \(L(\theta)\), and \(h(\beta)=f(\alpha)=0\). If \(h(\beta_j)=0\), then \(\theta-c\beta_j=\alpha_i\) for some \(i\), so \(j=1\) by the choice of \(c\). Hence \(\beta\) is the only common root of \(g\) and \(h\). Since \(g\) has distinct roots, the greatest common divisor of \(g\) and \(h\) is \(X-\beta\). The Euclidean algorithm computes this greatest common divisor inside \(L(\theta)[X]\), so \(\beta\in L(\theta)\) and \(\alpha=\theta-c\beta\in L(\theta)\). \(\square\)

**Theorem 3.3.** Let \(d=\deg F\). There is a nonzero \(D\in k[y_1,\ldots,y_n]\) such that every \(q\in k^n\) with \(D(q)\ne0\) has exactly \(d\) preimages under \(F\).

**Proof.** By Lemma 3.2 there are \(c_2,\ldots,c_n\in k\) with \(K=L(\theta)\) for \(\theta=x_1+c_2x_2+\cdots+c_nx_n\in B\). Let

\[
m(T)=T^d+a_{d-1}T^{d-1}+\cdots+a_0\in L[T]
\]

be the minimal polynomial of \(\theta\) over \(L\). Each \(x_i\) lies in \(L(\theta)=L[\theta]\), so \(x_i=\sum_{j<d}b_{ij}\theta^j\) with \(b_{ij}\in L\). Identify \(L\) with \(k(y_1,\ldots,y_n)\) through \(\varphi\), and choose a nonzero \(h\in A\) such that all \(a_j\) and all \(b_{ij}\) lie in \(A_h=A[1/h]\). The discriminant \(\delta\) of \(m\) is a polynomial in its coefficients, so \(\delta\in A_h\). It is nonzero, because \(m\) is irreducible over a field of characteristic zero and so has distinct roots. Write \(\delta=e/h^N\) with \(0\ne e\in A\), and put \(D=he\).

Write \(B_h\) for \(B[1/\varphi(h)]\). It contains \(A_h\) through \(\varphi\), and it contains \(\theta\) and every \(x_i\in A_h[\theta]\), so \(B_h=A_h[\theta]\). The \(A_h\)-algebra homomorphism

\[
A_h[T]/(m)\longrightarrow B_h,\qquad T\longmapsto\theta,
\]

is therefore surjective. It is also injective: if \(r(\theta)=0\) for some \(r\in A_h[T]\), division by the monic polynomial \(m\) gives \(r=sm+r_0\) with \(\deg r_0<d\) and \(r_0(\theta)=0\). Since \(1,\theta,\ldots,\theta^{d-1}\) are linearly independent over \(L\), \(r_0=0\).

Now let \(q\in k^n\) with \(D(q)\ne0\). The preimages \(p\) of \(q\) correspond to the \(k\)-algebra homomorphisms \(\psi:B\to k\) with \(\psi\circ\varphi\) equal to evaluation at \(q\). For such \(\psi\), \(\psi(\varphi(h))=h(q)\ne0\), so \(\psi\) extends uniquely to \(B_h\). Hence the preimages correspond to the \(k\)-algebra homomorphisms \(A_h[T]/(m)\to k\) that restrict to evaluation at \(q\) on \(A_h\). These are given by the roots in \(k\) of the polynomial

\[
m_q(T)=T^d+a_{d-1}(q)T^{d-1}+\cdots+a_0(q).
\]

Its discriminant is \(\delta(q)=e(q)/h(q)^N\ne0\). As \(k\) is algebraically closed, \(m_q\) has exactly \(d\) distinct roots in \(k\). \(\square\)

In particular, the image of \(F\) contains the nonempty open set \(\{D\ne0\}\), since \(d\geq1\).

## 4. Injectivity is everything

**Theorem 4.1.** Let \(k\) be algebraically closed of characteristic zero, and let \(F:k^n\to k^n\) be a Keller map. The following are equivalent:

1. \(F\) is a polynomial automorphism;
2. \(F\) is injective;
3. \(\deg F=1\), that is, \(k(F_1,\ldots,F_n)=k(x_1,\ldots,x_n)\).

**Proof.** (1) implies (2) because an inverse map exists.

(2) implies (3). A nonzero polynomial over an infinite field does not vanish at every point of \(k^n\): by induction on \(n\), write it as a polynomial in \(x_n\) with coefficients in \(k[x_1,\ldots,x_{n-1}]\), choose a point where a nonzero coefficient does not vanish, and use that a nonzero polynomial in one variable has finitely many roots. So there is \(q\) with \(D(q)\ne0\), for the \(D\) of Theorem 3.3. That point has exactly \(\deg F\) preimages. Injectivity gives \(\deg F\leq1\), so \(\deg F=1\).

(3) implies (1). Fix \(i\). Since \(K=L\), and \(L\) is the fraction field of \(\varphi(A)\), there are \(a,b\in A\) with \(b\ne0\) and \(x_i\,\varphi(b)=\varphi(a)\) in \(B\). The ring \(A\) is a unique factorization domain [Integral extensions: lying over, going up and going down, Proposition 2.3 and its proof](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#2-integral-closure-survives-localization), so we may take \(a\) and \(b\) without common irreducible factor. We show that \(b\) is a nonzero constant.

Suppose not, and let \(g\) be an irreducible factor of \(b\). Put \(G=\varphi(g)\in B\).

*Case 1: \(G\) is a constant \(\gamma\in k\).* Then \(\varphi(g-\gamma)=0\), and Proposition 2.1 gives \(g=\gamma\). This is impossible, because an irreducible polynomial is not constant.

*Case 2: \(G\) is not constant.* Then \(G\) is not a unit of \(B\), so the ideal \(GB\) lies in some maximal ideal \(\mathfrak m_p\), and the zero set \(Z(G)\subset k^n\) is nonempty. Let \(Z_0\) be an irreducible component of \(Z(G)\). Its ideal is a prime \(\mathfrak P\) minimal over \(GB\). By Krull's height theorem [Dimension theory of Noetherian local rings, Theorem 3.1](course:AG-CA/dimension-theory-of-noetherian-local-rings#3-how-much-can-one-equation-cut), \(\operatorname{ht}\mathfrak P\le1\), and \(\mathfrak P\ne0\) because \(G\ne0\). The height formula [Krull dimension and Noether normalization, Theorem 4.3](course:AG-CA/krull-dimension-and-noether-normalization#4-parameters-measure-dimension-and-height) gives

\[
\dim Z_0=\dim B/\mathfrak P=n-1 .
\]

For \(p\in Z_0\) we have \(g(F(p))=G(p)=0\). Moreover \(b=g\,b'\) for some \(b'\in A\), so

\[
a(F(p))=\varphi(a)(p)=p_i\,\varphi(b')(p)\,G(p)=0 .
\]

Hence \(F(Z_0)\subset W=Z(g)\cap Z(a)\subset k^n\). Let \(Y_0\) be the closure of \(F(Z_0)\). It is irreducible, as the closure of the image of an irreducible set under a continuous map, so its ideal is a prime \(\mathfrak Q\) of \(A\) containing \(g\) and \(a\). The ideal \((g)\) is prime, because \(A\) is factorial, and it has height one by Krull's height theorem. It does not contain \(a\), because \(g\) does not divide \(a\). So \(0\subsetneq(g)\subsetneq\mathfrak Q\), hence \(\operatorname{ht}\mathfrak Q\ge2\), and the height formula gives \(\dim Y_0=n-\operatorname{ht}\mathfrak Q\le n-2\).

The restriction of \(F\) is a dominant morphism \(Z_0\to Y_0\) of irreducible affine varieties over \(k\). By [Dimension of fibres, Theorem 4.1](course:AG-MO/dimension-of-fibres#4-dominant-families-of-varieties), every irreducible component of every nonempty fibre of \(Z_0\to Y_0\) has dimension at least

\[
\dim Z_0-\dim Y_0\ \ge\ (n-1)-(n-2)=1 .
\]

Take \(p\in Z_0\) and \(s=F(p)\). The fibre over \(s\) is a scheme of finite type over \(k\). Its closed points are the points \(p'\in Z_0\) with \(F(p')=s\), and there are finitely many of them by Proposition 2.2. A scheme of finite type over \(k\) is Jacobson [The Nullstellensatz and Jacobson rings, Theorem 4.2](course:AG-CA/the-nullstellensatz-and-jacobson-rings#4-finite-type-over-a-jacobson-base): every closed irreducible subset is the closure of its closed points. So each irreducible component of this nonempty fibre is a single closed point, of dimension zero. This contradicts the bound just obtained.

So \(b\) is a nonzero constant, and \(x_i=\varphi(a/b)=H_i(F_1,\ldots,F_n)\) for the polynomial \(H_i=a/b\in A\). Doing this for every \(i\) gives a polynomial map \(H=(H_1,\ldots,H_n)\) with \(H\circ F\) equal to the identity.

It remains to see that \(F\circ H\) is the identity too. The homomorphism \(\varphi\) is injective by Proposition 2.1. It is surjective, because its image contains every \(x_i=\varphi(H_i)\). So \(\varphi\) is an isomorphism. Let \(\eta:B\to A\) be the \(k\)-algebra homomorphism with \(\eta(x_i)=H_i\). Then \(\varphi(\eta(x_i))=\varphi(H_i)=x_i\), so \(\varphi\circ\eta\) is the identity of \(B\), and \(\eta=\varphi^{-1}\). Therefore \(\eta\circ\varphi\) is the identity of \(A\):

\[
y_j=\eta(\varphi(y_j))=\eta(F_j)=F_j(H_1,\ldots,H_n),
\]

which says that \(F\circ H\) is the identity. \(\square\)

The proof shows a little more: any polynomial map with algebraically independent components, all fibres finite and \(\deg F=1\) is an automorphism. For a Keller map, the first two conditions are automatic.

**Remark 4.2 (fields that are not algebraically closed).** Let \(k_0\) be a field of characteristic zero with algebraic closure \(k\), and let \(F\) be a Keller map with coefficients in \(k_0\). If \(F\) has a polynomial inverse \(H\) with coefficients in \(k\), then \(H\) has coefficients in \(k_0\). Indeed, Proposition 2.1 shows that \(H_i\) is the only polynomial with \(H_i(F_1,\ldots,F_n)=x_i\). Fix a bound \(N\) for the degrees of the \(H_i\). The coefficients of the \(H_i\) are then the unique solution of a system of linear equations with coefficients in \(k_0\). Gaussian elimination solves such a system inside \(k_0\). So the Jacobian conjecture over \(k_0\) is equivalent to the Jacobian conjecture over its algebraic closure, and Theorem 4.1 decides both.

## 5. Two classical cases

**Proposition 5.1 (triangular maps).** Let \(k\) be any field, let \(c_1,\ldots,c_n\in k\) be nonzero, and let \(f_i\in k[x_1,\ldots,x_{i-1}]\). The map

\[
F=\bigl(c_1x_1+f_1,\ c_2x_2+f_2(x_1),\ \ldots,\ c_nx_n+f_n(x_1,\ldots,x_{n-1})\bigr),
\]

with \(f_1\in k\) a constant, is a polynomial automorphism with \(\det JF=c_1\cdots c_n\).

**Proof.** The Jacobian matrix is lower triangular with diagonal \(c_1,\ldots,c_n\). Define \(H\) recursively by \(H_1=(y_1-f_1)/c_1\) and

\[
H_i=\bigl(y_i-f_i(H_1,\ldots,H_{i-1})\bigr)/c_i .
\]

Substituting shows \(F_i(H_1,\ldots,H_n)=y_i\) for every \(i\), so \(F\circ H\) is the identity. The same recursion, solved for \(x_i\), shows \(H\circ F\) is the identity: if \(y=F(x)\), then \(H_1(y)=x_1\), and inductively \(H_i(y)=(y_i-f_i(x_1,\ldots,x_{i-1}))/c_i=x_i\). \(\square\)

**Theorem 5.2 (Wang).** Let \(k\) be a field of characteristic zero. A Keller map \(F:k^n\to k^n\) whose components have degree at most two is a polynomial automorphism.

**Proof.** By Remark 4.2 we may assume \(k\) algebraically closed. By Theorem 4.1 it suffices to prove that \(F\) is injective. Write \(F(x)=c+Lx+Q(x)\), with \(c\in k^n\), \(L\) a linear map and \(Q\) a tuple of quadratic forms. Let \(\beta\) be the symmetric bilinear map with \(\beta(u,u)=Q(u)\), namely \(\beta(u,v)=\tfrac12\bigl(Q(u+v)-Q(u)-Q(v)\bigr)\). Then \(JF(x)\,v=Lv+2\beta(x,v)\). For \(a,b\in k^n\) with midpoint \(m=\tfrac12(a+b)\),

\[
F(b)-F(a)=L(b-a)+\beta(b+a,\,b-a)=JF(m)\,(b-a),
\]

using bilinearity and symmetry: \(\beta(b+a,b-a)=Q(b)-Q(a)\). If \(F(a)=F(b)\), then \(JF(m)(b-a)=0\), and the invertibility of \(JF(m)\) gives \(a=b\). \(\square\)

*Reference:* [Wang].

The proof divides by two, and Exercise 7.5 shows that this is essential.

## 6. Injective polynomial maps are surjective

The equivalence in Theorem 4.1 shows that a Keller map is an automorphism as soon as it is injective. Without any hypothesis on the Jacobian, injectivity already forces surjectivity.

**Theorem 6.1 (Ax, Grothendieck).** Let \(k\) be an algebraically closed field. Every injective polynomial map \(F:k^n\to k^n\) is surjective.

**Proof.** *Step 1: finite fields.* An injective map from a finite set to itself is surjective. So for every finite field \(\mathbb F\), an injective map \(\mathbb F^n\to\mathbb F^n\) is surjective.

*Step 2: algebraic closures of finite fields.* Let \(k=\overline{\mathbb F}_p\), and let \(F\) be injective. Given \(c\in k^n\), let \(\mathbb F\) be a finite subfield of \(k\) containing the coefficients of \(F\) and the coordinates of \(c\); one exists, since \(k\) is the union of its finite subfields. Then \(F\) maps \(\mathbb F^n\) injectively to itself, so \(c=F(a)\) for some \(a\in\mathbb F^n\) by Step 1.

*Step 3: the general case.* Suppose \(F\) is injective but some \(c\in k^n\) is not a value of \(F\). The polynomials \(F_j-c_j\) have no common zero, so by the weak Nullstellensatz they generate the unit ideal of \(k[x]\):

\[
1=\sum_{j=1}^nu_j\,(F_j-c_j),\qquad u_j\in k[x].
\tag{6.1}
\]

In the polynomial ring \(k[x,x']\) in \(2n\) variables, the polynomials \(F_j(x)-F_j(x')\) have common zeros only on the diagonal \(x=x'\), because \(F\) is injective. So each \(x_i-x'_i\) vanishes on their common zeros, and the strong Nullstellensatz [The Nullstellensatz and Jacobson rings, Theorem 2.2](course:AG-CA/the-nullstellensatz-and-jacobson-rings#2-closed-points-detect-radical-equations) gives some \(N\ge1\) with

\[
(x_i-x'_i)^N=\sum_{j=1}^nv_{ij}\,\bigl(F_j(x)-F_j(x')\bigr),\qquad v_{ij}\in k[x,x'] .
\tag{6.2}
\]

Let \(R\subset k\) be the subring generated by the coefficients of all the polynomials \(F_j,u_j,v_{ij}\) and by the \(c_j\). It is a nonzero finitely generated \(\mathbb Z\)-algebra. Choose a maximal ideal \(\mathfrak M\) of \(R\). The ring \(\mathbb Z\) is Jacobson [The Nullstellensatz and Jacobson rings, Proposition 3.2](course:AG-CA/the-nullstellensatz-and-jacobson-rings#3-the-jacobson-property), so by Theorem 4.2 of that lesson \(\mathfrak M\) contracts to a maximal ideal \((p)\) of \(\mathbb Z\), and \(R/\mathfrak M\) is a finite extension of \(\mathbb F_p\). Embed the finite field \(R/\mathfrak M\) in an algebraic closure \(\overline{\mathbb F}_p\), and reduce all coefficients modulo \(\mathfrak M\). The identities (6.1) and (6.2) stay true for the reduced polynomials \(\bar F,\bar c,\bar u,\bar v\). By (6.1), \(\bar c\) is not a value of \(\bar F\) on \(\overline{\mathbb F}_p^{\,n}\). By (6.2), if \(\bar F(a)=\bar F(a')\) then \((a_i-a'_i)^N=0\) for every \(i\), so \(a=a'\): the map \(\bar F\) is injective on \(\overline{\mathbb F}_p^{\,n}\). This contradicts Step 2. \(\square\)

*Reference:* [EGA IV, Proposition 10.4.11].

## 7. Exercises

**Exercise 7.1 (easy).** Show that the composite of two Keller maps is a Keller map, and that the polynomial automorphisms of \(k^n\) form a group under composition.

**Exercise 7.2 (easy).** Show that \(F(x,y,z)=(x,\ y+x^2,\ z+xy+x^3)\) is a Keller map, and compute its inverse.

**Exercise 7.3 (medium).** Let \(m<n\). Show that if every Keller map of \(k^n\) is a polynomial automorphism, then so is every Keller map of \(k^m\). (Use \(F\times\mathrm{id}\).)

**Exercise 7.4 (medium).** Check that the proof of Theorem 3.3 uses only that \(F_1,\ldots,F_n\) are algebraically independent. For the map \(F(x,y)=(x^2,y)\), which is not a Keller map, compute \(\deg F=[k(x,y):k(x^2,y)]\) and a polynomial \(D\) as in Theorem 3.3, and compare with the fibre over a point \((0,y_0)\).

**Exercise 7.5 (medium).** Let \(k\) be an algebraically closed field of characteristic \(2\). Find a polynomial map \(k^2\to k^2\) of degree two with Jacobian determinant \(1\) that is not injective. Where does the proof of Theorem 5.2 fail?

## 8. Solutions

**7.1.** By (1.1), \(\det J(G\circ F)=(\det JG\circ F)\cdot\det JF\). If both determinants are nonzero constants, so is the product. The composite of automorphisms is an automorphism with inverse \(F^{-1}\circ G^{-1}\); the identity is an automorphism; composition of polynomial maps is associative.

**7.2.** The Jacobian matrix is lower triangular with ones on the diagonal, so \(\det JF=1\). The map is triangular as in Proposition 5.1. Its inverse is \(H(u,v,w)=(u,\ v-u^2,\ w-uv)\). Indeed \(F(H(u,v,w))=\bigl(u,\ (v-u^2)+u^2,\ (w-uv)+u(v-u^2)+u^3\bigr)=(u,v,w)\).

**7.3.** Let \(F\) be a Keller map of \(k^m\), and let \(G=F\times\mathrm{id}\), that is, \(G(x,z)=(F(x),z)\) with \(z\in k^{n-m}\). Its Jacobian matrix is block diagonal with blocks \(JF\) and the identity, so \(\det JG=\det JF\), and \(G\) is a Keller map. By hypothesis \(G\) has an inverse \(H=(H',H'')\), with \(H'\) the first \(m\) components. From \(G\circ H=\mathrm{id}\) we get \(F(H'(y,z))=y\) and \(H''(y,z)=z\). From \(H\circ G=\mathrm{id}\) we get \(H'(F(x),z)=x\). Put \(E(y)=H'(y,0)\). Then \(F\circ E=\mathrm{id}\) and \(E\circ F=\mathrm{id}\), so \(F\) is an automorphism.

**7.4.** The proof uses the identification of \(L\) with a rational function field, which is Proposition 2.1, and nothing else about \(JF\). For \(F=(x^2,y)\), the field \(k(x,y)\) is generated over \(k(x^2,y)\) by \(x\), whose minimal polynomial is \(T^2-x^2\). So \(\deg F=2\), with \(\theta=x\) and \(m(T)=T^2-y_1\). Its discriminant is \(4y_1\), so \(D=y_1\) will do. A point \((y_1,y_2)\) with \(y_1\ne0\) has the two preimages \((\pm\sqrt{y_1},y_2)\). The point \((0,y_0)\) has only one, because \(m_q\) has a double root there.

**7.5.** Take \(F(x,y)=(x+x^2,\ y)\). Its Jacobian determinant is \(1+2x=1\). But \(F(0,0)=F(1,0)=(0,0)\). The proof of Theorem 5.2 defines \(\beta\) by dividing by \(2\) and uses the midpoint \(\tfrac12(a+b)\). Both are unavailable in characteristic two. This is Example 1.3 for \(p=2\).

## References

- [Bass–Connell–Wright] H. Bass, E. H. Connell, D. Wright, The Jacobian conjecture: reduction of degree and formal expansion of the inverse, Bull. Amer. Math. Soc. (N.S.) 7 (1982), 287–330. https://doi.org/10.1090/S0273-0979-1982-15032-7
- [EGA IV] A. Grothendieck, Éléments de géométrie algébrique IV, troisième partie, Publ. Math. IHÉS 28 (1966). http://www.numdam.org/item/PMIHES_1966__28__5_0/
- [Wang] S. S.-S. Wang, A Jacobian criterion for separability, J. Algebra 65 (1980), 453–494. https://doi.org/10.1016/0021-8693(80)90233-1
- [Keller] O.-H. Keller, Ganze Cremona-Transformationen, Monatsh. Math. Phys. 47 (1939), 299–306. https://doi.org/10.1007/BF01695502

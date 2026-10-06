# The Bost–Connes Hecke algebra

A subgroup can be close enough to normal to admit convolution, yet fail to be normal in a measurable way. The Bost–Connes algebra turns that failure into time evolution. Its translation operators remember roots of unity. Its dilation operators remember positive integers. These two kinds of operators interact through averaging over roots, which will make the Riemann zeta function appear in equilibrium states.

We first construct the algebra from finite coset counts. We then obtain its generators and both its time and arithmetic symmetries. The presentation also lets us prove that every bounded *-representation is controlled by the regular representation. The proof uses averaging over a compact group of phases.

The prerequisites are discrete groups and cosets, bounded operators on Hilbert space, C*-algebras and states, finite Fourier analysis, inverse limits of finite sets, and integration against product probability measures on countable products of circles. Sections 7–8 also use the normalized valuation on \(\mathbb Q_p\), its valuation ring \(\mathbb Z_p\), and the restricted-product topology, as specified in [Milne ANT]. We prove the particular lattice and tree facts used here. Section 10 derives the general local-field modulus and compact valuation ring from the topological-field hypotheses, using the exact Haar and Radon results named there and the fundamental theorem of algebra. For the KMS step we use [Analytic elements and strip arguments](https://kokunoyumeto.github.io/open-math-courses-public/courses/analytic-elements-strips-and-kms/analytic-elements-and-strip-arguments.html), Theorem 10.3, with the sign and scale specified below. Basic references are [Bost–Connes] and [Connes–Marcolli].

*Written by GPT-6.1 Sol (OpenAI), September 2026, with Ultra reasoning effort. Self-checked by the writing AI. Public domain (CC0).*

## 1. Counting before completing

Let \(G\) be a discrete group and \(H\subset G\) a subgroup. Call \((G,H)\) a **Hecke pair** if every orbit of \(H\) on \(G/H\) is finite. For \(g\in G\), put

\[
L(g)=[H:H\cap gHg^{-1}],\qquad
R(g)=[H:H\cap g^{-1}Hg].
\]

Thus \(HgH\) is a union of \(L(g)\) right cosets and \(R(g)\) left cosets. Here a right coset means \(gH\), and a left coset means \(Hg\). The names \(L,R\) record the left and right actions, rather than the names of the cosets. Inversion interchanges the two counts.

Let \(\mathcal H(G,H)\) be the vector space of complex, \(H\)-bi-invariant functions on \(G\) supported on finitely many double cosets. Define

\[
(f*k)(x)=\sum_{Hy\in H\backslash G}f(xy^{-1})k(y),\qquad
f^*(x)=\overline{f(x^{-1})}.
\tag{1.1}
\]

Changing the representative \(y\) to \(hy\) changes the first argument to \(xy^{-1}h^{-1}\), and leaves both factors unchanged. The sum is finite because the support of \(k\) contains finitely many left cosets. The product is bi-invariant. Its support is contained in the product of the supports of \(f,k\), which is a finite union of double cosets: decompose the first support into finitely many right cosets and the second into finitely many left cosets.

**Theorem 1.1 (Regular convolution).** On \(\ell^2(H\backslash G)\), the formula

\[
(\lambda(f)\xi)(Hx)=\sum_{Hy}f(xy^{-1})\xi(Hy)
\tag{1.2}
\]

defines a faithful *-representation of the unital algebra (1.1). If

\[
A_L(f)=\sum_{HgH}|f(g)|L(g),\qquad
A_R(f)=\sum_{HgH}|f(g)|R(g),
\]

then \(\|\lambda(f)\|\le\sqrt{A_L(f)A_R(f)}\).

**Proof.** In a fixed row of the matrix (1.2), substitute \(z=xy^{-1}\). Left cosets \(Hy\) correspond to right cosets \(zH\), so the absolute row sum is \(A_L(f)\). In a fixed column, \(Hx\mapsto Hxy^{-1}\) is a bijection of left coset spaces, so the absolute column sum is \(A_R(f)\). For a finitely supported vector, weighted Cauchy–Schwarz gives

\[
\sum_x\left|\sum_y f(xy^{-1})\xi_y\right|^2
\le A_L(f)\sum_{x,y}|f(xy^{-1})||\xi_y|^2
\le A_L(f)A_R(f)\|\xi\|^2.
\]

The operator therefore extends uniquely to the Hilbert space. Reversing the matrix indices proves the adjoint formula. Multiplying the two matrices and substituting \(Hz\mapsto Hzy^{-1}\) proves \(\lambda(f)\lambda(k)=\lambda(f*k)\). All sums in this calculation are finite for fixed indices. Also \(\lambda(f)\delta_H\) has value \(f(x)\) at \(Hx\), so the representation is injective. Operator associativity now proves associativity of (1.1). The identity is \(1_H\). \(\square\)

The **reduced Hecke C*-algebra** \(A_r(G,H)\) is the norm closure of this representation.

## 2. The imbalance is multiplicative

Neither \(L\) nor \(R\) need be multiplicative. Their ratio is.

**Lemma 2.1.** The function \(d(g)=R(g)/L(g)\) is a homomorphism \(G\to\mathbb Q_{>0}^{\times}\), trivial on \(H\).

**Proof.** Two subgroups \(K_1,K_2\) are commensurable if their intersection has finite index in both. Set

\[
j(K_1,K_2)=\frac{[K_1:K_1\cap K_2]}{[K_2:K_1\cap K_2]}.
\]

For three pairwise commensurable subgroups their common intersection \(J\) has finite index in each, and \(j(K_1,K_2)=[K_1:J]/[K_2:J]\). Hence \(j(K_1,K_3)=j(K_1,K_2)j(K_2,K_3)\). Conjugation preserves this ratio. Apply the identity to \(H,gHg^{-1},ghHh^{-1}g^{-1}\). Since \(j(H,gHg^{-1})=L(g)/R(g)\), taking reciprocals gives \(d(gh)=d(g)d(h)\). For \(g\in H\), both counts are one. \(\square\)

**Theorem 2.2 (Time from cosets).** There is a unique norm-continuous-on-each-orbit group of automorphisms of \(A_r(G,H)\) satisfying

\[
\alpha_t(f)(g)=d(g)^{it}f(g).
\tag{2.1}
\]

**Proof.** On \(\ell^2(H\backslash G)\), let \(V_t\delta_{Hx}=d(x)^{it}\delta_{Hx}\). This is well-defined and unitary. Directly from the matrix entries,

\[
V_t\lambda(f)V_t^*=\lambda(\alpha_t(f)).
\]

It follows that (2.1) preserves the algebra, its norm and its involution. Each finite double-coset sum has a norm-continuous orbit. Approximation and isometry extend that assertion to its norm closure. Uniqueness follows from density. \(\square\)

The vector state

\[
\phi(a)=\langle a\delta_H,\delta_H\rangle
\tag{2.2}
\]

has \(\phi(\lambda(f))=f(1)\). Inner products are linear in the first variable.

Our **physical KMS convention** at \(\beta>0\) is

\[
F_{a,b}(t)=\omega(a\alpha_t(b)),\qquad
F_{a,b}(t+i\beta)=\omega(\alpha_t(b)a),
\tag{2.3}
\]

with \(F\) bounded and continuous on the closed strip and holomorphic inside. The analytic criterion we use is

\[
\omega(ab)=\omega(b\alpha_{i\beta}(a))
\tag{2.4}
\]

on a norm-dense invariant algebra of entire elements, with \(b\) arbitrary. It follows from Theorem 10.3 of *Analytic elements and strip arguments*: apply that theorem to the group \(s\mapsto\alpha_{-\beta s}\). Its analytic identity becomes \(\omega(\alpha_{-i\beta}(x)y)=\omega(yx)\); substitute \(x=\alpha_{i\beta}(a)\). Rescaling and reversing the strip converts its boundary condition into (2.3). This convention makes a Hamiltonian flow \(\alpha_t=\operatorname{Ad}e^{itK}\) have density proportional to \(e^{-\beta K}\).

**Proposition 2.3 (The canonical equilibrium state).** The state (2.2) is KMS at inverse temperature one for (2.1).

**Proof.** Write \(c_X=1_{HgH}\). Formula (1.1) at the identity gives, for every \(k\in\mathcal H(G,H)\),

\[
\phi(c_X*k)=L(g)k(g^{-1}),\qquad
\phi(k*c_X)=R(g)k(g^{-1}).
\]

As \(\alpha_i(c_X)=d(g)^{-1}c_X\), these are precisely (2.4). Linearity proves the identity on the Hecke algebra; norm continuity in \(k\) extends it to arbitrary \(b\in A_r(G,H)\). Each \(c_X\) is an entire eigenvector and their span is dense and invariant. The analytic criterion proves (2.3). \(\square\)

If \(H\) is normal, \(L=R=1\), the evolution is trivial and this state is a trace. A nonnormal subgroup can therefore carry a canonical equilibrium state without an arbitrarily chosen Hamiltonian.

## 3. Viewing the same algebra from the other coset space

There is a useful second realization. On \(\ell^2(G/H)\), let \(U_g\delta_{xH}=\delta_{gxH}\). Inversion defines a linear unitary

\[
I:\ell^2(H\backslash G)\longrightarrow\ell^2(G/H),\qquad
I\delta_{Hx}=\delta_{x^{-1}H}.
\]

**Proposition 3.1 (Coefficients in the commutant).** A bounded operator \(T\) commuting with all \(U_g\) is determined by

\[
f_T(g)=\langle T\delta_H,\delta_{g^{-1}H}\rangle.
\]

This function is bi-invariant and satisfies

\[
\sum_{Hg\in H\backslash G}|f_T(g)|^2=\|T\delta_H\|^2,
\quad f_{T^*}(g)=\overline{f_T(g^{-1})},
\]

\[
f_{ST}(g)=\sum_{zH\in G/H}f_S(gz)f_T(z^{-1}).
\tag{3.1}
\]

The last series is absolutely convergent. For finite double-coset support \(f\), the operator \(r(f)=I\lambda(f)I^*\) lies in this commutant and has coefficient \(f\). Moreover,

\[
\overline{r(\mathcal H(G,H))\delta_H}
=\{\xi:U_h\xi=\xi\text{ for every }h\in H\}.
\tag{3.2}
\]

**Proof.** Commutation implies \(T\delta_{yH}=U_yT\delta_H\). Thus \(T\delta_H\) determines every column. Its \(H\)-invariance proves the two-sided invariance of \(f_T\), and the matrix entry in row \(xH\), column \(yH\), is \(f_T(x^{-1}y)\). Parseval proves the norm identity. Taking adjoints gives the displayed involution. Matrix multiplication at \(x=g^{-1},y=1\) gives (3.1); the row of \(S\) and column of \(T\) belong to \(\ell^2\), so Cauchy–Schwarz proves absolute convergence.

Conjugating (1.2) by \(I\) gives exactly the kernel \(f(x^{-1}y)\). It is unchanged under simultaneous left translation of \(x,y\), hence commutes with \(U_g\). This also proves that \(r\) is an isometric *-isomorphism onto the C*-algebra generated by these kernels. It does not assert that this C*-algebra is the entire commutant.

Finally an \(H\)-invariant vector is constant on each \(H\)-orbit in \(G/H\). All these orbits are finite. Their normalized indicators form an orthonormal basis of the invariant subspace. Each indicator is \(r(c_X)\delta_H\) for the inverse double coset \(X\). Conversely each \(r(f)\delta_H\) is \(H\)-invariant. Taking closed spans proves (3.2). \(\square\)

## 4. Rational dilations and translations

Use the matrices

\[
g(b,q)=\begin{pmatrix}1&b\\0&q\end{pmatrix},\qquad
b\in\mathbb Q,\quad q\in\mathbb Q_{>0}.
\]

Their multiplication is

\[
g(b,q)g(c,r)=g(c+br,qr).
\tag{4.1}
\]

Let \(G\) be this group and \(H=\{g(k,1):k\in\mathbb Z\}\). This convention identifies the matrix with the affine map \(x\mapsto(x+b)/q\); choosing the alternative matrix for \(x\mapsto qx+b\) reciprocates the dilation parameter.

**Lemma 4.1 (Exact orbit sizes).** If \(q=m/n\) in lowest terms with \(m,n>0\), then

\[
Hg(b,q)H=\{g(b+k/n,q):k\in\mathbb Z\},\qquad
L(g)=n,\quad R(g)=m,\quad d(g)=q.
\tag{4.2}
\]

In particular \((G,H)\) is a Hecke pair.

**Proof.** Multiplying on the two sides by integral translations changes \(b\) by an element of \(\mathbb Z+q\mathbb Z=(1/n)\mathbb Z\). Right cosets identify \(b\) modulo \(\mathbb Z\), giving \(n\) possibilities. Left cosets identify \(b\) modulo \(q\mathbb Z=(m/n)\mathbb Z\), giving \(m\) possibilities. \(\square\)

Define \(e(r)=1_{Hg(r,1)H}\) for \(r\in\mathbb Q/\mathbb Z\), and

\[
\mu_n=n^{-1/2}1_{Hg(0,n)H}\quad(n\ge1).
\tag{4.3}
\]

Then \(\alpha_t(e(r))=e(r)\) and \(\alpha_t(\mu_n)=n^{it}\mu_n\).

**Theorem 4.2 (Generators and relations).** The algebra \(\mathcal H(G,H)\) is generated by \(e(r),\mu_n\), with the following presentation:

\[
\begin{gathered}
e(0)=1,\quad e(r)e(s)=e(r+s),\quad e(r)^*=e(-r),\\
\mu_1=1,\quad\mu_n^*\mu_n=1,\quad\mu_n\mu_m=\mu_{nm},\\
\mu_n\mu_m^*=\mu_m^*\mu_n\quad\text{if }\gcd(n,m)=1,\\
e(r)\mu_n=\mu_ne(nr),\qquad
\mu_ne(r)\mu_n^*=\frac1n\sum_{ns=r}e(s).
\end{gathered}
\tag{4.4}
\]

For coprime \(n,m\), the elements

\[
\mu_ne(r)\mu_m^*
=(nm)^{-1/2}1_{Hg(r/m,n/m)H},\qquad r\in\mathbb Q/\mathbb Z,
\tag{4.5}
\]

form a vector-space basis as \(n,m,r\) vary.

*Reference:* [Bost–Connes, Section 4, equation (7)] displays the translation parameter \(r\). With the generators in (4.3), multiplication gives \(r/m\), as in (4.5).

**Proof.** An equivalent form of (1.1), obtained by \(z=xy^{-1}\), is

\[
(f*k)(x)=\sum_{zH\in G/H}f(z)k(z^{-1}x).
\tag{4.6}
\]

The supports of \(e(r)\) and \(1_{Hg(0,n)H}\) each consist of one right coset. Consequently convolution on the left by either function substitutes respectively \(g(-r,1)x\) or \(g(0,n^{-1})x\), with the latter carrying the scalar \(n^{-1/2}\). These substitutions prove the group law for \(e\), the semigroup law for \(\mu\), and the covariance with \(e(r)\).

The inverse dilation class consists of the \(n\) right cosets represented by \(g(j/n,1/n)\), \(0\le j<n\). Therefore

\[
(\mu_n^**f)(x)=n^{-1/2}\sum_{j=0}^{n-1}f(g(-j,n)x).
\tag{4.7}
\]

Applying (4.7) to \(\mu_n\) gives one at \(x\in H\) and zero elsewhere: all \(n\) terms contribute \(1/n\) at \(H\). Thus \(\mu_n^*\mu_n=1\). In \(\mu_m^*\mu_n\), the possible translation residues are \(nj/m\) modulo \(\mathbb Z\). When \(n,m\) are coprime, these run once through the \(m\) residues \(j/m\). Comparing with \(\mu_n\mu_m^*\) proves the commutation relation.

For \(\mu_ne(r)\mu_n^*\), the support has dilation one and translation residues \((r+j)/n\), \(0\le j<n\), each with coefficient \(1/n\). They are precisely the solutions of \(ns=r\), which proves the last relation.

To show the relations are complete, consider the abstract *-algebra they define. Let \(t_{n,m,r}=\mu_ne(r)\mu_m^*\). Adjoints interchange \(n,m\) and negate \(r\). If \(q=\gcd(n,m)\), the last relation reduces \(t_{n,m,r}\) to

\[
\frac1q\sum_{qs=r}t_{n/q,m/q,s}.
\tag{4.8}
\]

For \(q=\gcd(m_1,n_2)\), cancellation of \(\mu_q^*\mu_q\), coprime commutation and covariance give

\[
t_{n_1,m_1,r_1}t_{n_2,m_2,r_2}
=t_{n_1n_2/q,\,m_1m_2/q,\,(n_2/q)r_1+(m_1/q)r_2}.
\tag{4.9}
\]

Equation (4.8) then reduces this product to coprime terms. Their span is therefore a unital *-algebra containing every generator.

In the concrete algebra, use the single right coset of \(\mu_n\) and of \(e(r)\) in (4.6), followed by the support of \(\mu_m^*\). This gives (4.5). For a fixed ratio \(n/m\) in lowest terms, (4.2) identifies the translation parameter modulo \((1/m)\mathbb Z\), so \(r/m\), with \(r\in\mathbb Q/\mathbb Z\), labels the double cosets without repetition. Thus the abstract spanning family maps bijectively to the double-coset basis, and there are no additional relations. \(\square\)

For example,

\[
\mu_3e(1/2)\mu_3^*
=\tfrac13\bigl(e(1/6)+e(1/2)+e(5/6)\bigr).
\]

The division by three is essential: the operator is an average, rather than a sum of three unitaries.

## 5. Why the regular norm is already universal

Let \(D\subset A_r(G,H)\) be the C*-algebra generated by the \(e(r)\). Every finite collection of rational residues lies in a finite cyclic subgroup. The corresponding unitaries have precisely the norm supplied by its finite Fourier transform. Indeed the subspace indexed by the cosets \(Hg(b,1)\), \(b\in\mathbb Q/\mathbb Z\), is invariant under \(D\), and on it the \(e(r)\) act by the regular translations. A representation of a cyclic group of order \(N\) decomposes into the eigenspaces of its generator, so its norm is at most the maximum of the same Fourier values. The regular representation attains all of them.

It follows, by taking the union over \(N\), that

\[
D=C^*(\mathbb Q/\mathbb Z)=C(\widehat{\mathbb Z}).
\tag{5.1}
\]

Here \(\widehat{\mathbb Z}=\varprojlim_N\mathbb Z/N\mathbb Z\), and \(e(a/N)\) is the function \(z\mapsto\exp(2\pi i a(z\bmod N)/N)\). Cylinder functions are dense in this continuous-function algebra: uniform continuity on the compact inverse limit gives a finite quotient on whose fibres a given continuous function oscillates by less than any prescribed positive tolerance.

**Theorem 5.1 (All representations extend).** Every unital *-representation of (4.4) by bounded operators extends uniquely to \(A_r(G,H)\).

**Proof.** Every \(t_{n,m,r}\) is represented by a contraction. Therefore the supremum over representations of the norm of any finite linear combination is finite. Complete the algebra for this supremum to obtain its universal C*-algebra \(A_u\). The regular representation gives a surjection \(\pi:A_u\to A_r\). The finite Fourier argument above shows that \(\pi\) is injective on its diagonal \(D_u\), and identifies \(D_u\) with (5.1).

Let \(K=\prod_p\mathbb T\), with \(p\) ranging over primes. A point \(z\in K\) defines \(z(n)=\prod_p z_p^{v_p(n)}\), extended to positive rationals by \(z(n/m)=z(n)/z(m)\). The assignments

\[
\gamma_z(\mu_n)=z(n)\mu_n,\qquad\gamma_z(e(r))=e(r)
\]

preserve (4.4), hence define automorphisms of \(A_u\). The action is continuous on polynomials and thus on the completion. Integrating against the product of the normalized circle measures gives a positive contractive map

\[
E_u(a)=\int_K\gamma_z(a)\,dz.
\]

The integral can first be formed on continuous finite-coordinate functions and then by uniform approximation; this also defines it for the continuous Banach-valued orbit. On \(t_{n,m,r}\), the integral vanishes unless \(n=m\), by prime factorization. If \(n=m\), (4.4) puts the term in \(D_u\). Density shows that \(E_u\) maps into \(D_u\) and is the identity there.

This expectation is faithful. If \(a\ge0\) and \(E_u(a)=0\), every state \(\rho\) gives a continuous nonnegative function \(z\mapsto\rho(\gamma_z(a))\) with zero integral. Product circle measure gives positive measure to every nonempty open set, so that function is zero everywhere. Its value at the identity is \(\rho(a)=0\). States detect positive elements, hence \(a=0\).

The same action exists on \(A_r\). One can see its isometry directly on the Hecke representation: multiply the coset vector indexed by \(Hx\) by \(z(d(x))\). It implements the prescribed action. Thus \(\pi E_u=E_r\pi\). If \(\pi(a)=0\), then \(\pi(E_u(a^*a))=0\). Injectivity on \(D_u\) gives \(E_u(a^*a)=0\), faithfulness gives \(a^*a=0\), and \(a=0\). Therefore \(\pi\) is an isomorphism. Uniqueness of an extension follows from density. \(\square\)

A representation with \(\pi(1)\ne1\) has all its generators supported on the projection \(\pi(1)\). Restricting to its range and adjoining the zero representation on its orthogonal complement gives the same extension assertion.

**Proposition 5.2 (The time-fixed algebra and centralizer).** The fixed algebra \(A_r^\alpha\) is \(D\). It also equals

\[
\{a\in A_r:\phi(ab)=\phi(ba)\text{ for all }b\in A_r\}.
\tag{5.2}
\]

**Proof.** Average \(\alpha_t\) over \([-T,T]\). On \(t_{n,m,r}\) this multiplies by

\[
\frac1{2T}\int_{-T}^T(n/m)^{it}\,dt,
\]

which tends to zero if \(n\ne m\) and is one otherwise. On polynomials the average therefore converges to \(E_r\); its norm is at most one, so approximation extends convergence to every \(a\in A_r\). A fixed element equals its average and hence lies in \(D\). Conversely every \(e(r)\) is fixed.

For \(d\in D\), approximate by translation polynomials. Each translation class has \(L=R=1\), so the calculation in Proposition 2.3 gives \(\phi(db)=\phi(bd)\).

For the converse, use the realization \(r\) in Section 3 and regard \(a\) as an operator on \(\ell^2(G/H)\). By norm approximation, the same calculation gives, for every double coset \(X=HgH\),

\[
\phi(c_Xa)=L(g)f_a(g^{-1}),\qquad
\phi(ac_X)=R(g)f_a(g^{-1}).
\]

If \(a\) satisfies (5.2), these coefficients vanish whenever \(L(g)\ne R(g)\), equivalently \(d(g)\ne1\). Time evolution multiplies the coefficient at \(g\) by \(d(g)^{it}\), as follows either from its diagonal implementer or from norm approximation. Hence \(\alpha_t(a)\) and \(a\) have identical coefficient functions. Proposition 3.1 says they are equal. The fixed-algebra assertion now finishes the proof. \(\square\)

## 6. Arithmetic symmetries

Let \(W=\widehat{\mathbb Z}^{\times}\), the inverse limit of the groups \((\mathbb Z/N\mathbb Z)^{\times}\). It acts on \(\mathbb Q/\mathbb Z\): if \(r=a/N\), multiply \(a\) by the residue of \(u\) modulo \(N\).

**Theorem 6.1.** The assignments

\[
\theta_u(e(r))=e(ur),\qquad\theta_u(\mu_n)=\mu_n
\tag{6.1}
\]

define a pointwise norm-continuous action of \(W\) on \(A_r\). It commutes with \(\alpha\), preserves \(\phi\), and satisfies

\[
A_r^W=C^*(\mu_n:n\ge1).
\tag{6.2}
\]

On \(D=C(\widehat{\mathbb Z})\), it is \(\theta_u(f)(z)=f(uz)\).

**Proof.** Multiplication by \(u\) is an automorphism of \(\mathbb Q/\mathbb Z\) and permutes the solutions of \(ns=r\). Thus it preserves every relation (4.4); Theorem 5.1 gives the automorphism and its inverse. Each translation generator has a locally constant orbit depending on a finite quotient of \(W\). The dilation generators are fixed. Approximation proves continuity. The generator formulas also prove commutation with time, and the character formula in (5.1) proves the action on \(D\).

The canonical state on a normal monomial is

\[
\phi(\mu_ne(r)\mu_m^*)=
\begin{cases}1/n,&n=m\text{ and }r=0,\\0,&\text{otherwise.}\end{cases}
\tag{6.3}
\]

For \(n\ne m\), its dilation support misses the identity. For \(n=m\), the last relation in (4.4) has a zero residue precisely when \(r=0\). Formula (6.3) is unchanged by \(r\mapsto ur\), proving state invariance.

It remains to compute the fixed algebra. Under (5.1),

\[
P_n=\mu_n\mu_n^*=1_{n\widehat{\mathbb Z}}.
\tag{6.4}
\]

This follows by summing the \(n\) characters \(e(j/n)\): their average is one exactly on the residues divisible by \(n\).

On \(\mathbb Z/N\mathbb Z\), two residues are in the same orbit of its unit group exactly when they have the same greatest common divisor with \(N\). To see the nontrivial direction, work modulo each prime power dividing \(N\). Equal valuations allow multiplication by a unit to carry one residue to the other; choose these units simultaneously by the Chinese remainder theorem. The indicators \(1_{d\mid z}\), \(d\mid N\), span the invariant functions: the indicator of the orbit with greatest common divisor \(d\) is

\[
\sum_{k\mid N/d}\mu(k)1_{dk\mid z},
\]

where \(\mu(k)\) is the Möbius function. Thus the invariant cylinder functions belong to the algebra generated by the \(P_n\). Averaging a uniformly close cylinder approximation to an invariant continuous function proves that \(D^W\) is exactly that algebra.

Averaging (6.1) over \(W\) sends \(t_{n,m,r}\) to \(\mu_n E_W(e(r))\mu_m^*\), which belongs to \(C^*(\mu_n)\). The averaging is contractive, and polynomials are dense, so its range is contained in this algebra. Every invariant element equals its average. The reverse inclusion follows because every \(\mu_n\) is fixed. This proves (6.2). \(\square\)

The symmetry group is compact, but it acts nontrivially on the equilibrium states at low temperature. The distinction between fixing the time evolution and fixing each individual equilibrium state will matter in Phase transition in the Bost–Connes system.

## 7. The adelic realization of the symmetry

The compact group in Section 6 is also the finite idele class group. We now identify its action on the regular Hecke representation. Keeping the matrices explicit determines which action is indexed by a unit and which by its inverse.

Let

\[
\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p),\qquad
R=\prod_p\mathbb Z_p=\widehat{\mathbb Z},\qquad
\mathbb A_f^\times=\prod_p'(\mathbb Q_p^\times,\mathbb Z_p^\times).
\tag{7.1}
\]

The first restricted product is the finite adele ring; \(R\) is its compact open subring. The second carries the restricted-product **idele topology**, with \(\prod_p\mathbb Z_p^\times\) open. We use the usual inverse-limit construction of \(\mathbb Z_p\), its field of fractions \(\mathbb Q_p\), valuations and the Chinese remainder theorem.

**Lemma 7.1 (Rational representatives and the idele split).** The diagonal rational embedding satisfies

\[
\overline{\mathbb Q}=\mathbb A_f,\qquad
\mathbb Q\cap R=\mathbb Z,\qquad
\mathbb A_f/R\simeq\mathbb Q/\mathbb Z.
\tag{7.2}
\]

Every finite idele has a unique factorization

\[
a=q u,\quad q\in\mathbb Q_{>0},\quad
u\in W=\prod_p\mathbb Z_p^\times,\qquad
q=\prod_p p^{v_p(a_p)}.
\tag{7.3}
\]

This is a topological product decomposition
\(\mathbb A_f^\times\simeq\mathbb Q_{>0}^{\mathrm{discrete}}\times W\).
In particular its quotient by \(\mathbb Q_{>0}\) is \(W\).

**Proof.** A basic adele neighborhood prescribes finitely many congruences
\(x_p-a_p\in p^{k_p}\mathbb Z_p\), for \(p\) in a finite set \(S\), and integrality outside \(S\). Enlarge \(S\) to contain every nonintegral coordinate of \(a\). Choose
\(D=\prod_{p\in S}p^{d_p}\)
so that \(Da_p\in\mathbb Z_p\) and \(k_p+d_p\ge0\). The Chinese remainder theorem gives an integer \(b\) with
\(b\equiv Da_p\pmod{p^{k_p+d_p}}\)
at every prescribed prime. Then \(b/D\) lies in the neighborhood, and is integral at every other prime. This proves density.

A rational number integral at every prime has no denominator prime, hence is an integer. Applying the same approximation to the open coset \(a+R\) gives a rational representative. Its ambiguity is exactly \(\mathbb Z\), proving the last assertion of (7.2).

Only finitely many valuations of an idele are nonzero, so the product in (7.3) is a positive rational. Its \(p\)-valuation is \(v_p(a_p)\); therefore \(a/q\) is a unit at every prime. A positive rational with all valuations zero is one, proving uniqueness. On each restricted-product neighborhood all but finitely many valuations are fixed at zero, and each remaining valuation is locally constant. Thus the map to \(q\), with its discrete topology, is continuous. Its kernel is \(W\); multiplication and the inverse factorization are continuous, proving the topological assertion. \(\square\)

Define the locally compact affine group and its compact open subgroup by

\[
P=\{g(b,a):b\in\mathbb A_f,\ a\in\mathbb A_f^\times\},
\qquad
K=\{g(b,u):b\in R,\ u\in W\},
\tag{7.4}
\]

using exactly the matrix \(g\) and multiplication (4.1). The rational group \(G\) of Section 4 sits inside \(P\).

**Proposition 7.2 (The coset space and the commutant action).** There is a bijection

\[
P/K=G/H=\Delta,
\tag{7.5}
\]

and

\[
\overline G=\{g(b,q):b\in\mathbb A_f,\
q\in\mathbb Q_{>0}\}\ \triangleleft P,\qquad
P/\overline G\simeq W.
\tag{7.6}
\]

Left translation gives a strongly continuous unitary representation \(L\) of \(P\) on \(\ell^2(\Delta)\). It induces a strongly continuous action on \(L(G)'\) by

\[
\Theta_u(X)=L(g(0,u))X L(g(0,u))^*.
\tag{7.7}
\]

This depends only on the class in \(P/\overline G\).

**Proof.** Write \(a=q u\) as in (7.3). Right multiplication of \(g(b,a)\) by \(g(c,u^{-1})\in K\) gives \(g(c+b/u,q)\). By (7.2), choose \(c\in R\) so that \(c+b/u\) is rational. Thus every \(P/K\)-coset has a representative in \(G\). Its stabilizer is \(G\cap K=H\), since a rational integral translation is an integer and a positive rational unit is one. This proves (7.5).

The positive rational multiplicative factor is closed and discrete in (7.3). Density of the rational translations gives the closure in (7.6). The map from \(P\) to \(W\) taking its multiplicative coordinate to \(u\) is a homomorphism with this kernel: translations do not affect it, and the multiplicative group is abelian. Hence the closure is normal and the quotient is \(W\).

The stabilizer of every coset is an open conjugate of \(K\). Orbit maps of basis vectors are therefore locally constant. Approximation by finitely supported vectors proves strong continuity of \(L\). Strong density gives \(L(G)'=L(\overline G)'\). Normality of \(\overline G\) shows that conjugation by \(L(P)\) preserves this commutant. Changing a representative by \(\overline G\) has no effect on its elements. The continuous unit representative \(g(0,u)\) then proves the stated continuity of the quotient action. \(\square\)

We identify \(A_r\) with its faithful commutant realization \(r(A_r)\) from Section 3.

**Theorem 7.3 (Exact conjugation formula).** On this realization,

\[
\Theta_u(r(\mu_n))=r(\mu_n),\qquad
\Theta_u(r(e(\gamma)))=r(e(u^{-1}\gamma)).
\tag{7.8}
\]

Consequently

\[
\Theta_u|_{r(A_r)}=r\theta_{u^{-1}}r^{-1},
\qquad
\Theta_u(f)(z)=f(u^{-1}z)\quad(f\in C(R)).
\tag{7.9}
\]

Thus \(\Theta\) preserves the regular Hecke C*-algebra, is pointwise norm continuous there, commutes with time evolution, preserves the canonical state, and has fixed algebra \(r(C^*(\mu_n:n\ge1))\).

**Proof.** There is a direct coset proof that each dilation commutes with all of \(P\), requiring no tree model. Put \(g_n=g(0,n)\). The map

\[
F_n:\Delta\to\Delta,\qquad F_n(xK)=xg_nK
\tag{7.10}
\]

is well defined: \(g_n^{-1}Kg_n\subset K\), because conjugation multiplies a translation in \(R\) by \(n\). It is \(P\)-equivariant. Every fiber has
\([g_n K g_n^{-1}:K]=[n^{-1}R:R]=n\)
points; the last index is \(|R/nR|=n\), by the finite Chinese remainder decomposition.

The operator \(S_n\delta_{xK}=\delta_{F_n(xK)}\) has norm \(\sqrt n\). Indeed, each output coefficient is the sum of the \(n\) input coefficients in its fiber, so Cauchy–Schwarz gives that bound, with equality on a normalized constant fiber vector. Also \(S_nS_n^*=n1\), and \(S_n\) commutes with \(L(P)\).

The coefficient kernel of Section 3 gives

\[
r(\mu_n^*)\delta_K=n^{-1/2}\delta_{g_nK}.
\]

Both \(r(\mu_n^*)\) and \(n^{-1/2}S_n\) commute with \(L(G)\) and have this value on \(\delta_K\). That vector is cyclic for \(L(G)\), by (7.5), so the two operators coincide. This proves dilation invariance in (7.8).

The same coefficient kernel gives
\(r(e(\gamma))\delta_K=\delta_{g(-\gamma,1)K}\).
The unit \(g(0,u)\in K\) fixes \(\delta_K\). Its conjugation of a translation is

\[
g(0,u)g(b,1)g(0,u^{-1})=g(b/u,1).
\tag{7.11}
\]

Therefore \(\Theta_u(r(e(\gamma)))\delta_K=
\delta_{g(-u^{-1}\gamma,1)K}\).
The inverse multiplication on \(\gamma\) is well defined through (7.2), even when \(u\) is not rational. Both operators in the second equality of (7.8) belong to \(L(G)'\); the cyclic-vector argument again proves equality.

The first equality of (7.9) now follows on the generators, and hence on the C*-algebra. For the second, Section 5's Fourier identification is

\[
e(a/N)(z)=\exp(2\pi i a z_N/N).
\tag{7.12}
\]

Replacing \(a/N\) by \(u^{-1}a/N\) in that character is exactly precomposition by \(z\mapsto u^{-1}z\). Density of the characters proves the formula for every \(f\in C(R)\).

All remaining assertions follow from Theorem 6.1, since inversion is a continuous automorphism of the abelian compact group \(W\). State preservation also follows directly from (7.7), because its unit representatives fix the canonical vector \(\delta_K\). \(\square\)

Equations (6.1) and (7.7) use reciprocal indices: the abstract action \(\theta_u\) is adelic conjugation by \(g(0,u^{-1})\). This convention changes neither the fixed algebra nor the symmetry group, but it matters when evaluating a character or labeling an equilibrium state.

## 8. Local trees and the restricted product

The coset space in Section 7 has a geometry at each prime. The following construction identifies that geometry without assuming a tree theorem. It also specifies the simplicial structure on the product: several prime coordinates can move at once, so the global space has higher dimensional simplices.

Fix a prime \(p\), write \(F=\mathbb Q_p\) and \(O=\mathbb Z_p\), and normalize \(v_p(p)=1\), with \(v_p(0)=+\infty\). Put

\[
P_p=\{g(b,a):b\in F,\ a\in F^\times\},
\qquad K_p=\{g(b,u):b\in O,\ u\in O^\times\}.
\]

For \(x\in F\) and \(k\in\mathbb Z\), denote the ball \(x+p^kO\) by \(B(x,k)\). Its exponent \(k\) is uniquely determined, and its center is determined modulo \(p^kO\).

**Theorem 8.1 (The local coset tree).** There is a canonical identification of \(P_p/K_p\) with the balls \(B(x,k)\). Join each ball to its parent \(B(x,k-1)\). This is a tree of degree \(p+1\), with distance

\[
d(B(x,k),B(y,l))=k+l-2h,
\qquad h=\min\{k,l,v_p(x-y)\}.
\tag{8.1}
\]

It is also the lattice tree of \(\mathrm{SL}_2(F)\): its vertices are homothety classes of full lattices in \(F^2\), and adjacent classes admit representatives \(L,L'\) with \(pL\subset L'\subset L\) and \([L:L']=p\). The \(P_p\)-action is by isometries and preserves the end obtained by repeatedly taking parents.

**Proof.** With the matrix convention (4.1), \(g(b,a)\) acts on \(F\) by

\[
\varphi_g(t)=\frac{t+b}{a}.
\tag{8.2}
\]

Indeed, \(\varphi_{g(b,a)}\varphi_{g(c,r)}=\varphi_{g(c+br,ar)}\). The stabilizer of the ball \(O\) consists exactly of \(a\in O^\times,b\in O\): the image ball is \(b/a+a^{-1}O\), whose radius agrees with that of \(O\) precisely when \(v_p(a)=0\), and whose center must then lie in \(O\). Conversely, \(B(x,k)\) is the image of \(O\) under \(g(p^{-k}x,p^{-k})\). Thus orbit and stabilizer give the claimed coset bijection.

The children of \(B(x,k)\) are exactly

\[
B(x+c p^k,k+1),\qquad c=0,\ldots,p-1.
\tag{8.3}
\]

These are its distinct cosets modulo \(p^{k+1}O\); the ball has a unique parent and these \(p\) children. Two balls have the first common ancestor \(B(x,h)=B(y,h)\), where \(h\) is as in (8.1). Their parent paths therefore connect them, with length \(k+l-2h\). There can be no finite simple cycle: a vertex in a cycle with maximal exponent would have both its neighbors as parents, whereas its parent is unique. Hence the graph is a tree and the connected path just described is its unique simple path. This proves the distance formula.

We next prove the lattice identification explicitly. Associate to a ball the lattice

\[
L(x,k)=O(p^k,0)+O(x,1).
\tag{8.4}
\]

Changing \(x\) modulo \(p^kO\) leaves the lattice unchanged. Every full, finitely generated \(O\)-submodule \(L\subset F^2\) lies between \(p^NO^2\) and \(p^{-N}O^2\) for some \(N\). For the upper inclusion, bound the coordinates of its finitely many generators. For the lower inclusion, choose two independent vectors of \(L\); the inverse of their coordinate matrix has bounded denominators.

The second-coordinate image of \(L\) is a nonzero, finitely generated fractional ideal of \(O\). Taking the smallest valuation of its generators shows that it equals \(p^sO\). Rescale \(L\) by \(p^{-s}\) to make that image \(O\). Its first-coordinate kernel is now a nonzero \(O\)-submodule of \(F\), with valuations bounded below by the preceding inclusions. An element with minimum valuation generates it, so the kernel is \(p^kO\) for some integer \(k\). Choose \((x,1)\) in the lattice. Subtracting a multiple of this vector from any lattice vector proves (8.4).

If two such normalized lattices are homothetic, their homothety scalar has valuation zero, since both second-coordinate images are \(O\). Multiplication by a unit leaves any \(O\)-module unchanged. Thus their \(k\)'s agree and their centers agree modulo \(p^kO\). We have proved a bijection between balls and lattice classes.

The intermediate lattices \(pL\subset L'\subset L\) of index \(p\) correspond to the lines of \(L/pL\simeq\mathbb F_p^2\). In the basis \((p^k,0),(x,1)\), the \(p\) lines generated by \((c,1)\) give precisely the child lattices in (8.3). The remaining line, generated by \((1,0)\), gives

\[
O(p^k,0)+O(px,p)=pL(x,k-1),
\]

the class of the parent. These exhaust the \(p+1\) lines. Thus the lattice adjacency relation is exactly the ball adjacency relation.

For clarity, it also gives the usual lattice distance, with no factor of two. Transform the first ball to \(O\); write the second as \(B(y,l)\) and now put \(h=\min\{0,l,v_p(y)\}\). The representative

\[
p^{-h}L(y,l)
=O(p^{\,l-h},0)+O(p^{-h}y,p^{-h})
\tag{8.5}
\]

is contained in \(O^2\), and contains a primitive vector, because at least one of \(l-h,v_p(y)-h,-h\) is zero. It is therefore not contained in \(pO^2\). Its index is \(p^{l-2h}\), from the determinant of the displayed basis. A primitive vector can be completed to an \(O\)-basis of \(O^2\), since one of its coordinates is a unit. In this basis the quotient by (8.5) is \(O/p^{l-2h}O\). Consequently its cyclic quotient exponent is exactly the graph distance in (8.1). Any homothetic representative that is contained in \(O^2\) and not in \(pO^2\) must have this same scaling valuation, proving the normalization used by that distance.

An invertible linear map preserves homothety, intermediate-lattice inclusions and their indices, and therefore acts by tree isometries. The action of our upper triangular matrix on (8.4), rescaled by \(a^{-1}\), is

\[
a^{-1}g(b,a)L(x,k)
=O(p^k/a,0)+O((x+b)/a,1).
\tag{8.6}
\]

It is exactly the ball action (8.2). Affine maps preserve inclusion and the index between a ball and its parent. All parent rays eventually merge, because every two balls have a common ancestor. They therefore define a single end, fixed by \(P_p\). In the lattice model the parent ray based at \(O^2\) can be represented by \(O(1,0)+p^rO(0,1)\), \(r\ge0\); its limiting direction is the line \(F(1,0)\), fixed by the upper triangular group. This completes the identification with the tree and its distinguished end. \(\square\)

Let \(T_p\) be this tree with base vertex \(o_p=O\). Its restricted product of vertex sets is

\[
\prod_p'(T_p,o_p)
=\{(v_p)_p:v_p=o_p\text{ for all but finitely many }p\}.
\tag{8.7}
\]

**Theorem 8.2 (The global geometry and the parent operators).** The adelic coset space and its permutation Hilbert space have canonical identifications

\[
\Delta=P/K\simeq\prod_p'(T_p,o_p),
\qquad
\ell^2(\Delta)\simeq
\bigotimes_p'(\ell^2(T_p),\delta_{o_p}).
\tag{8.8}
\]

The \(P\)-action is simplicial for the triangulation defined below. The rational affine subgroup acts transitively, with stabilizer \(H\), as in (7.5). If \(S_p\delta_B=\delta_{\operatorname{parent}(B)}\) on \(\ell^2(T_p)\), then, in (8.8),

\[
r(\mu_p^*)=p^{-1/2}
\bigl(1\otimes\cdots\otimes S_p\otimes\cdots\bigr).
\tag{8.9}
\]

In particular each normalized local adjoint \(p^{-1/2}S_p^*\) is an isometry.

**Proof.** The group \(P\) is the restricted product of \(P_p\) with respect to \(K_p\), and \(K=\prod_pK_p\). Sending an adelic coset to its local cosets produces (8.7). Every tuple there has a representative with finitely many nonidentity components; if two representatives give the same tuple, their relative element lies in \(K_p\) at every prime and hence in \(K\). This proves the first bijection in (8.8), and it intertwines the coordinatewise action. A restricted-product group element sends a restricted tuple to another such tuple, since its \(K_p\)-components fix \(o_p\) at all but finitely many primes.

Here is an explicit invariant simplicial structure. First form finite dimensional cubes by selecting an edge in each of finitely many prime coordinates and fixing all other coordinates at vertices. Orient every selected edge from its child to its parent. A cube with \(d\) selected coordinates has vertices labeled by subsets of those coordinates: a coordinate belongs to the subset when it has moved to its parent. Triangulate that cube by declaring each strictly increasing chain of subsets to be a simplex. This is the usual triangulation of \([0,1]^d\) by orderings of its coordinates: a point lies in a simplex by sorting its coordinate values. The triangulations agree on faces, because fixing a coordinate at zero or one restricts the same subset order. Thus they give a simplicial complex with exactly the vertex set (8.7).

Each \(P_p\)-action preserves parent orientation by Theorem 8.1. The coordinatewise \(P\)-action therefore sends cubes to cubes and increasing chains to increasing chains. It is simplicial. The restricted product need not itself be a tree: two different prime edges form a square, with two triangles in this structure. Rational transitivity and the base stabilizer are the already proved Proposition 7.2.

For the Hilbert-space assertion, send the basis vector of \((v_p)_p\) to \(\bigotimes_p\delta_{v_p}\). The tensors differ from the reference tensors at only finitely many primes. Their inner products agree with those of the coset basis, and their span is dense in the restricted tensor product by its definition. This gives the second unitary in (8.8), intertwining the permutation actions.

Finally consider \(F_p(xK)=xg(0,p)K\) from (7.10). At any prime \(q\ne p\), \(g(0,p)\in K_q\), so that coordinate is unchanged. At \(p\), \(g(0,p)K_p\) corresponds to the parent ball \(p^{-1}O\). Since the local action preserves parents, the \(p\)-coordinate of \(F_p(xK)\) is the parent of the \(p\)-coordinate of \(xK\). Thus the global \(S_p\) of Section 7 is exactly the single-coordinate parent operator in (8.9). Each parent has \(p\) children, so \(S_pS_p^*=p1\). Equation (8.9) follows from the already proved relation \(r(\mu_p^*)=p^{-1/2}S_p\). \(\square\)

This geometry explains why the arithmetic dilation of a prime is independent of the local translation and unit coordinates: every affine transformation preserves the same parent relation. The direct coset argument of Section 7 and the local tree argument here give the same normalized operator.

## 9. The adelic group corner

The full affine group averages both integral translations and local units. Its compact-subgroup corner consequently retains the prime shifts, with no independent cyclotomic observables. We prove this for the full group C*-algebra, and also prove faithfulness of its regular corner. This avoids needing a general amenability theorem for this particular identification.

First record the precise universal property of the shift algebra \(\mathcal T=C^*(\mu_n:n\ge1)\), whose faithful integer representation was proved in Phase transition in the Bost–Connes system, Proposition 11.2.

**Lemma 9.1 (The prime-shift universal property).** A family of isometries \(s_p\), one for each prime, satisfying

\[
s_ps_q=s_qs_p,\qquad
s_p^*s_q=s_qs_p^*\quad(p\ne q)
\tag{9.1}
\]

defines a unique unital *-homomorphism from \(\mathcal T\) sending \(\mu_p\) to \(s_p\).

**Proof.** Form the universal C*-algebra \(\mathcal U\) for (9.1). It exists by taking the supremum of representation norms on polynomials: every word is a contraction, so each finite linear combination has a finite supremum norm. The concrete prime shifts provide a representation and a quotient map \(\pi:\mathcal U\to\mathcal T\).

Write \(s_n=\prod_ps_p^{v_p(n)}\). Every word reduces, using (9.1) and \(s_p^*s_p=1\), to \(s_ns_m^*\). Thus the compact gauge group \(\prod_p\mathbb T\), acting by \(s_p\mapsto z_ps_p\), has fixed algebra

\[
\mathcal D_{\mathcal U}=C^*(P_n:n\ge1),
\qquad P_n=s_ns_n^*.
\tag{9.2}
\]

Indeed, averaging a monomial kills it unless \(n=m\). The average is faithful by the full-support argument in Theorem 5.1.

The map \(\pi\) is injective on this diagonal. To check it, take finitely many primes and maximal exponents \(M_p\). The projections \(P_{p^j}\), \(0\le j\le M_p\), form decreasing chains, and different prime chains commute. The atoms of their finite dimensional algebra are products of

\[
P_{p^j}-P_{p^{j+1}}\quad(0\le j<M_p),
\qquad P_{p^{M_p}}.
\tag{9.3}
\]

They are orthogonal projections with sum one. In the integer shift representation every atom is nonzero: choose an integer with exactly the specified valuations for the differences, and valuation at least \(M_p\) for a last projection. A linear combination of atoms has norm the largest absolute coefficient, both before and after \(\pi\). Taking the increasing union proves diagonal injectivity.

The concrete gauge action is implemented by \(\delta_k\mapsto z(k)\delta_k\), so \(\pi\) intertwines the faithful averages. If \(\pi(x)=0\), diagonal injectivity applied to the average of \(x^*x\) gives \(x=0\). Thus \(\pi\) is an isomorphism, proving the universal property. \(\square\)

Let \(dg=db\,d^\times a\) be left Haar measure on \(P\), normalized by \(dg(K)=1\). Additive Haar measure gives \(R\) measure one, and multiplicative Haar measure gives \(W\) measure one. With our matrix convention, left multiplication translates \(b\) at fixed \(a\) and multiplies the idele coordinate. Right multiplication by \(g(c,r)\) multiplies the additive coordinate by \(r\). Consequently

\[
d(xg)=\delta(g)\,dx,\qquad
\delta(g(b,a))=|a|_f:=\prod_p|a_p|_p.
\tag{9.4}
\]

Here \(\delta\) is specified by this change-of-variables convention. On the full group C*-algebra \(B=C^*(P)\), write \(U_g\) for the canonical multiplier unitaries. The group algebra uses left convolution and involution
\(f^*(g)=\overline{f(g^{-1})}\delta(g^{-1})\).
Put \(e=1_K=\int_KU_k\,dk\). Its image in any unitary representation is the orthogonal projection onto the \(K\)-fixed vectors.

**Theorem 9.2 (Corner and dynamics).** There is a canonical isomorphism

\[
\mathcal T\longrightarrow eBe,\qquad
\mu_n\longmapsto V_n:=U_{g(0,n)}e.
\tag{9.5}
\]

The regular representation of \(P\) is faithful on this corner, so the same identification holds with \(eC_r^*(P)e\). The modular-character dynamics

\[
\sigma_t(U_g)=\delta(g)^{-it}U_g
\tag{9.6}
\]

fixes \(e\) and restricts to \(\sigma_t(V_n)=n^{it}V_n\), exactly the prime-shift evolution.

**Proof.** Haar probability on the compact subgroup gives \(e=e^*=e^2\). Since \(K\) is open, its characteristic function lies in \(C_c(P)\), so this projection belongs to \(B\), rather than merely its multiplier algebra.

For \(g_n=g(0,n)\), the inclusion \(g_n^{-1}Kg_n\subset K\) was proved in Section 7. A smaller compact subgroup has a larger fixed-vector projection. Hence

\[
U_{g_n}^{*}eU_{g_n}\ge e,\qquad
eU_{g_n}e=U_{g_n}e.
\]

Thus \(V_n\in eBe\), \(V_n^*V_n=e\), and \(V_nV_m=V_{nm}\).

For a prime \(p\), replace the rational idele \(p\) in \(g_p\) by the idele whose \(p\)-component is \(p\) and whose other components are one. Their quotient lies in \(W\), so multiplying \(e\) makes no change to \(V_p\). Averaging \(K=\prod_qK_q\) factors into its compact subgroup averages. Operators and averages belonging to distinct prime coordinates commute. This gives \(V_p^*V_q=V_qV_p^*\) for \(p\ne q\). Lemma 9.1 therefore gives a homomorphism \(\mathcal T\to eBe\).

We prove its surjectivity by explicit compact functions. Multiplication of the three factors \(U_{g_n}eU_{g_m}^{*}\), with the right-translation Haar change in (9.4), gives

\[
(V_nV_m^*)(g(b,a))
=\frac1m\,1_{\{\,a\in(n/m)W,\ b\in m^{-1}R\,\}}.
\tag{9.7}
\]

This is an equality of compactly supported \(L^1\) functions representing the indicated group-algebra elements. At one prime, the factor for exponents \(i=v_p(n),j=v_p(m)\) is

\[
F_{i,j}(b,a)
=p^{-j}1_{\{v_p(a)=i-j,\ b\in p^{-j}O\}}.
\tag{9.8}
\]

To see that these factors span every local double-coset function, use the ball chart of Section 8. At fixed ball exponent \(k=j-i\), the \(K_p\)-orbits are classified by

\[
h=\min\{0,k,v_p(x)\},\qquad B=B(x,k).
\tag{9.9}
\]

For \(h=\min\{0,k\}\), this is one orbit: when \(k\ge0\), integral translations are transitive on the balls inside \(O\); when \(k<0\), the ball is the single ancestor \(p^kO\). For \(h<\min\{0,k\}\), its centers have valuation \(h\); multiplying by a unit carries any such center to any other. Conversely integral translation and unit multiplication preserve the displayed minimum. This proves the orbit classification.

The support of \(F_{i,j}\) in the ball chart is \(v_p(x)\ge-i\), because \(x=b/a\). For
\(i_0=\max\{0,-k\}\), \(j_0=i_0+k\),
the function \(F_{i_0,j_0}\) is a nonzero constant on the first orbit in (9.9). For each \(i>i_0\), with \(j=i+k\),

\[
F_{i,j}-p^{-1}F_{i-1,j-1}
\tag{9.10}
\]

is a nonzero constant exactly on the orbit \(h=-i\). Therefore the local orbit indicators are in their linear span.

A global double coset is a product of such local double cosets, equal to \(K_p\) outside finitely many primes. Taking products of (9.8) and (9.10) shows that all its characteristic functions lie in the span of \(V_nV_m^*\). For \(f\in C_c(P)\), the compact function \(efe\) is \(K\)-bi-invariant and constant on finitely many double cosets: those cosets are open, and its compact support meets only finitely many in the discrete quotient. Thus \(eC_c(P)e\) is contained in this span. Since \(C_c(P)\) is dense in the group C*-algebra, the homomorphism is surjective.

We next prove injectivity, including the regular assertion. The quasi-regular action \(L\) on \(\ell^2(\Delta)\) from Section 7 is a subrepresentation of the left regular action on \(L^2(P,dg)\): send \(\delta_{gK}\) to \(1_{gK}\). These functions are orthonormal because each left coset has Haar measure one. This map intertwines the actions. On the \(K\)-fixed subspace let \(v_p=L(g_p)e\).

For the base vector \(\delta_K\), averaging the \(p^j\) descendants of \(O\), and then translating them by \(g_p^j\), gives

\[
\langle v_p^jv_p^{*j}\delta_K,\delta_K\rangle=p^{-j}.
\tag{9.11}
\]

Explicitly, \(v_p^{*j}\delta_K\) is \(p^{-j}\) times the sum of the \(p^j\) balls of exponent \(j\) inside \(O\), and \(v_p^j\) takes them to the balls of exponent zero with centers in \(p^{-j}O/O\). The base center occurs once. The restricted tensor description (8.8) makes expectations for distinct primes multiply. Thus the expectation of every finite diagonal atom (9.3) is a product of strictly positive numbers \(p^{-j}-p^{-j-1}\) and \(p^{-M_p}\). Its image is nonzero, so the represented map is injective on the diagonal by the same atom-norm argument as Lemma 9.1.

The diagonal unitaries

\[
Z_z\delta_{g(b,a)K}
=\left(\prod_pz_p^{v_p(a_p)}\right)\delta_{g(b,a)K}
\tag{9.12}
\]

are well defined, since changing a coset representative changes \(a\) only by a unit idele. They commute with the \(K\)-average and satisfy \(Z_zv_pZ_z^*=z_pv_p\). The representation therefore intertwines the gauge averages. Their faithfulness and diagonal injectivity imply its injectivity on all of \(\mathcal T\). Since this representation factors through the left regular group representation, both the full corner map and its regular version are injective.

Finally, \(\delta(g)^{-it}\) is a continuous unitary character. Twisting any unitary representation by it gives (9.6) as an isometric automorphism of \(B\). Dominated convergence on \(L^1(P)\), then density, proves norm continuity in \(t\). The character is one on \(K\), so \(e\) is fixed. Since \(|n|_f=1/n\), equation (9.6) gives \(\sigma_t(V_n)=n^{it}V_n\). \(\square\)

The word *corner* in (9.5) refers to the projection \(e\), whether one starts with the full or the reduced group algebra. Formula (9.7) also specifies the normalization of the compact functions used in subsequent lattice-module computations.

## 10. Recovering a local field from its Haar modulus

The rational prime constructions use \(\mathbb Q_p\), but the compact-ring statement behind them has a wider scope. Here \(K\) is any **nondiscrete commutative Hausdorff locally compact topological field**: its addition, multiplication and inversion on \(K^\times\) are continuous. An absolute value is not assumed in the hypotheses.

We use Haar measure on locally compact groups, Theorem 2.2 for Radon representation and its compact-set regularity formula, Proposition 7.1(5) for quotients by closed subgroups, Proposition 7.3 for uniform continuity on compact supports, and Theorems 8.3 and 9.2 for existence and uniqueness of Haar measure. The following argument is the classical one for local fields; see [Milne ANT], Chapter 7. Its characteristic-independent compact-ring steps are proved explicitly.

Let \(\mu\) be additive Haar measure. Multiplication by \(a\ne0\) is an additive automorphism, so uniqueness defines
\[
\mu(aE)=m(a)\mu(E),\qquad m(a)>0;\qquad m(0)=0.
\tag{10.1}
\]
The choice of scalar normalization of \(\mu\) cancels. Composition gives \(m(ab)=m(a)m(b)\), and \(m(-1)=1\).

**Lemma 10.1 (Proper modulus and the original topology).** The map \(m:K\to[0,\infty)\) is continuous and proper. The sets \(\{x:m(x)<\varepsilon\}\), \(\varepsilon>0\), are a neighborhood basis at zero for the given topology.

**Proof.** An additive Haar point mass is zero. Otherwise an infinite compact neighborhood, containing arbitrarily many different points, would have arbitrarily large measure. A finite neighborhood would make the additive group discrete, contrary to the hypothesis.

Choose a compact neighborhood \(V\) of zero. It has positive finite measure. Given \(a\in K\) and \(\eta>0\), outer regularity gives an open \(U\supset aV\) with \(\mu(U)<\mu(aV)+\eta\). For \(a=0\) use \(\mu(\{0\})=0\). Continuity of multiplication and compactness of \(V\) give a neighborhood \(W\) of \(a\) such that \(WV\subset U\). Thus for \(x\in W\),
\[
m(x)\le m(a)+\eta/\mu(V).
\tag{10.2}
\]
This proves continuity at zero and upper semicontinuity everywhere. On \(K^\times\), the identity \(m(x)=m(x^{-1})^{-1}\) supplies lower semicontinuity, so \(m\) is continuous.

Compactness also supplies a neighborhood \(U_0\) of zero with \(U_0V\subset\operatorname{int}V\). By nondiscreteness and continuity of \(m\) at zero, choose \(c\in U_0\cap V\), \(c\ne0\), with \(m(c)<1\). Then \(cV\subset\operatorname{int}V\) and all positive powers of \(c\) lie in \(V\). Every cluster point of those powers has modulus zero, hence is zero. Compactness forces \(c^n\to0\): an infinite subsequence outside a neighborhood of zero would have a cluster point outside it. In particular \(c^nx\to0\) for every \(x\in K\), and the sets \(c^{-n}V\) increase and cover \(K\).

Set \(Q=\overline{V\setminus cV}\). This is compact and excludes zero, since \(cV\) is a neighborhood of zero. If \(x\notin V\), let \(n\ge1\) be the first integer with \(c^nx\in V\). Then \(c^nx\in V\setminus cV\), so
\[
0<\min_Qm\le m(c)^n m(x).
\tag{10.3}
\]
For \(m(x)\le r\), this bounds \(n\) by a constant depending only on \(r\). Hence the closed set \(B_r=\{m\le r\}\) lies in one compact set \(c^{-N}V\) and is compact. This proves properness.

Finally let \(V_1\) be a compact neighborhood of zero within any prescribed neighborhood. Choose \(r>0\) with \(V_1\subset B_r\). The compact set \(B_r\setminus\operatorname{int}V_1\) excludes zero, so its modulus has a positive minimum if it is nonempty. A modulus ball of radius less than both that minimum and \(r\) lies in \(V_1\). If the compact difference is empty, any radius at most \(r\) suffices. Continuity already makes the strict modulus balls open. This proves the asserted equality of topologies. \(\square\)

We next justify why the nonarchimedean case covers all fields here except the real and complex fields. This step cannot be replaced by a theorem which starts with an already specified valuation.

**Lemma 10.2 (The archimedean alternative).** Either
\[
m(x+y)\le\max\{m(x),m(y)\}\quad(x,y\in K),
\tag{10.4}
\]
or \(K\) is topologically isomorphic to \(\mathbb R\) or \(\mathbb C\).

**Proof.** Properness makes
\[
C=\max_{m(x)\le1}m(1+x)\ge1
\]
finite. Dividing the smaller-modulus summand by the larger shows that
\[
m(x+y)\le C\max\{m(x),m(y)\}.
\tag{10.5}
\]
Iterating this inequality in a balanced binary sum gives, for \(N\ge1\),
\[
m\left(\sum_{i=1}^Nz_i\right)
\le C^{\lceil\log_2N\rceil}\max_i m(z_i).
\tag{10.6}
\]
Padding by zeros to the next power of two proves this bound without a linear loss in \(N\).

Suppose first that the moduli of the nonnegative integers, interpreted in \(K\), are bounded by \(B\). For \(m(x)\le1\), expand \((1+x)^n\) by the binomial theorem and use (10.6):
\[
m(1+x)^n\le C^{\lceil\log_2(n+1)\rceil}B.
\tag{10.7}
\]
Taking \(n\)-th roots gives \(m(1+x)\le1\), hence \(C=1\) and (10.4). This includes every positive-characteristic field, since its prime subfield is finite.

If \(C>1\), the integer moduli are therefore unbounded, and \(K\) has characteristic zero. Pick an integer \(b\ge2\) with \(m(b)>1\). For each integer \(a\ge2\), expand \(a^n\) in base \(b\). There are \(L=\lfloor n\log_ba\rfloor+1\) digits, and their moduli are bounded by the fixed maximum \(B_b\) over \(0,\ldots,b-1\). Consequently
\[
m(a)^n\le C^{\lceil\log_2L\rceil}B_b\,m(b)^{L-1}.
\]
Taking roots gives \(m(a)\le m(b)^{\log_ba}\). If \(m(a)\le1\), expanding \(b^n\) in base \(a\) would instead bound its modulus by a polynomial in \(n\), contradicting \(m(b)>1\). Thus \(m(a)>1\). Interchanging \(a,b\) in the first bound proves
\[
m(a)=a^s,\qquad
m(r)=|r|^s\quad(r\in\mathbb Q),\qquad
s=\frac{\log m(b)}{\log b}>0.
\tag{10.8}
\]
The rational assertion follows from multiplicativity and \(m(-1)=1\).

Every additive Cauchy sequence in a locally compact group converges: after subtracting one term its tail lies in a compact neighborhood; it has a cluster point, and the Cauchy condition makes the entire tail converge to that point. Formula (10.8) and Lemma 10.1 therefore extend the inclusion of \(\mathbb Q\) to a topological field embedding of \(\mathbb R\) into \(K\), by taking limits of rational Cauchy sequences. The result is independent of the approximations; continuity of field operations preserves sums, products and inverses. It is injective because its extended modulus is \(|r|^s\). This equality also proves continuity in both directions on the image. Hence \(K\) is a locally compact real topological vector space.

We give the finite-dimensional step, including its measure normalization. In a real topological vector space, every neighborhood of zero contains a balanced neighborhood \(U\), meaning \([-1,1]U\subset U\). To construct one, compactness of \([-1,1]\) gives \(U_1\) with \([-1,1]U_1\) inside the prescribed neighborhood; take \(U=\bigcup_{|t|\le1}tU_1\).

For a finite-dimensional subspace \(W\subset K\) with a chosen algebraic basis, the linear map \(F:\mathbb R^d\to W\) is continuous. The image of the Euclidean unit sphere is compact and excludes zero. Choose a balanced neighborhood \(U\) disjoint from this image. If \(F(\lambda)\in U\) and \(\|\lambda\|\ge1\), balance would put \(F(\lambda/\|\lambda\|)\) in \(U\), a contradiction. Scaling \(U\) proves continuity of \(F^{-1}\) at zero. Thus \(W\) has its Euclidean topology and is closed in \(K\): a convergent net in \(K\) with terms in \(W\) has a Cauchy coordinate net, whose Euclidean limit lies in \(W\).

The quotient \(Q=K/W\) is locally compact and Hausdorff and is again a real topological vector space. Choose additive Haar measures on \(W\) and \(Q\). The integral
\[
I(f)=\int_Q\left(\int_W f(x+w)\,d\mu_W(w)\right)d\mu_Q(x+W),
\qquad f\in C_c(K),
\tag{10.9}
\]
is well defined independently of representatives. The inner integral is continuous: for \(x\) in a fixed compact neighborhood of \(x_0\), the relevant \(w\)'s lie in the intersection of \(W\) with a fixed compact set, and uniform continuity of \(f\) bounds the difference of the integrals. Its support on \(Q\) is contained in the compact image of \(\operatorname{supp}f\). Therefore (10.9) is a nonzero positive translation-invariant functional; Radon representation and Haar uniqueness identify it, after one scalar normalization, with additive Haar integration on \(K\).

For real \(r\ne0\), let \(m_Q(r)\) be the quotient Haar modulus of scalar multiplication. Changing variables in both integrals of (10.9) gives
\[
m(r)=|r|^d m_Q(r).
\tag{10.10}
\]
If \(Q=0\), its modulus is one. If \(Q\ne0\), it is nondiscrete: for nonzero \(v\in Q\), the distinct vectors \(rv\) approach zero as \(r\to0\). Its Haar point masses vanish. The compact-neighborhood argument of (10.2), now for the continuous scalar action on \(Q\), gives \(m_Q(r)\to0\) as \(r\to0\). Since \(m_Q(2^{-n})=m_Q(1/2)^n\), this implies \(m_Q(1/2)<1\). In either case (10.8) and (10.10) yield
\[
2^{-s}=2^{-d}m_Q(1/2)\le2^{-d},\qquad d\le s.
\]
All finite-dimensional subspaces of \(K\) have this fixed dimension bound, so \(K\) is finite dimensional over \(\mathbb R\).

Finally a finite field extension of \(\mathbb R\) is \(\mathbb R\) or \(\mathbb C\). Indeed the fundamental theorem of algebra makes every irreducible real polynomial have degree one or two. An element outside \(\mathbb R\) thus generates a copy of \(\mathbb C\), over which no further algebraic extension is possible. The finite-dimensional topology just proved makes the resulting field isomorphism a homeomorphism. This proves the alternative. \(\square\)

**Theorem 10.3 (The compact valuation ring).** Suppose \(K\) is not topologically isomorphic to \(\mathbb R\) or \(\mathbb C\). Define
\[
R_K=\{x:m(x)\le1\},\quad
R_K^\times=\{x:m(x)=1\},\quad
J_K=\{x:m(x)<1\}.
\tag{10.11}
\]
Then \(R_K\) is the unique maximal compact subring of \(K\), \(R_K^\times\) is its unit group, and \(J_K\) is its unique maximal ideal. There is \(\pi\in J_K\setminus\{0\}\) such that \(J_K=\pi R_K=R_K\pi\). The residue field \(k=R_K/J_K\) is finite, of some characteristic prime \(p\), and, for \(q=|k|\),
\[
m(\pi)=q^{-1},\qquad m(K^\times)=q^{\mathbb Z}.
\tag{10.12}
\]
The image in \(K\) of the integer \(p\) has modulus less than one. The metric \(d(x,y)=m(x-y)\) is an ultrametric giving the original topology, with \(\pi^nR_K\) a neighborhood basis at zero.

**Proof.** Lemma 10.2 gives the ultrametric inequality for \(m\). Thus \(R_K\) is a subring, compact by Lemma 10.1; \(J_K\) is an ideal. An element of \(R_K\) is invertible there exactly when its modulus is one. Every proper ideal excludes these units and so lies in \(J_K\); since \(R_K/J_K\) is a field, \(J_K\) is the unique maximal ideal.

For \(m(y)<1\), the ultrametric inequality in both directions, using \(1=(1+y)-y\), gives \(m(1+y)=1\). Hence the unit set is open: around a unit \(u\), the neighborhood \(u+uJ_K\) consists of units. The set \(J_K\) is open by continuity, and its complement in \(R_K\) is open too. Therefore \(J_K\) is compact as well as open. It contains a nonzero element, by continuity at zero and nondiscreteness. The positive maximum
\[
\lambda=\max_{x\in J_K}m(x)<1
\]
is attained. Choose \(\pi\) attaining it. For \(x\in J_K\), \(m(x/\pi)\le1\), and conversely every element of \(\pi R_K\) has modulus at most \(\lambda<1\). Thus \(J_K=\pi R_K\), without assuming a discrete value group in advance.

There is no modulus value strictly between \(\lambda\) and one. For any \(x\ne0\), choose the integer \(n\) such that
\(\lambda^{n+1}<m(x)\le\lambda^n\).
Then \(\lambda<m(\pi^{-n}x)\le1\), so this last value is one, and \(m(x)=\lambda^n\). This proves \(m(K^\times)=\lambda^{\mathbb Z}\).

The quotient \(k\) is discrete because \(J_K\) is open, and compact because \(R_K\) is compact. It is therefore a finite field. Its characteristic is a prime \(p\), and its cardinality \(q=p^f\) is a prime power, by viewing it as a finite vector space over its prime subfield. If \(K\) has positive characteristic, the quotient map preserves the prime subfield, so that characteristic is also \(p\). The image of \(p\) in \(K\) lies in \(J_K\). In characteristic \(p\) it is zero, so its modulus is zero; in characteristic zero it is nonzero of modulus less than one.

The \(q\) disjoint additive cosets of \(\pi R_K\) in \(R_K\) have equal Haar measure. Consequently
\[
\mu(R_K)=q\,\mu(\pi R_K)
=q\,m(\pi)\mu(R_K),
\]
proving (10.12). Each nonzero \(x\) now has a unique integer \(v(x)\) with \(m(x)=q^{-v(x)}\); set \(v(0)=+\infty\). The ultrametric inequality and Lemma 10.1 give the claimed metric and topology. In particular
\(\pi^nR_K=\{m\le q^{-n}\}\),
and these open additive ideals form the stated neighborhood basis. They are open because the value group has a gap above each \(q^{-n}\).

If \(B\) is any compact subring, \(m\) is bounded on \(B\). For \(x\in B\) with \(m(x)>1\), all powers \(x^n\) would lie in \(B\) and have unbounded modulus, a contradiction. Thus every compact subring is contained in \(R_K\), proving its unique maximality. \(\square\)

The integer prime and the uniformizer have different roles. In characteristic zero write \(p=u\pi^e\), with \(u\in R_K^\times\) and \(e=v(p)\ge1\). Then \(m(p)=q^{-e}\). In positive characteristic \(p=0\) in \(K\), so this expression with a finite \(e\) is not asserted. A unit \(u\) need not be a rational integer.

The same modulus is the affine-group module used in the course. In our matrix coordinates \(g(b,a)=\begin{pmatrix}1&b\\0&a\end{pmatrix}\), let \(db\) be additive Haar measure and
\(d^\times a=da/m(a)\)
be multiplicative Haar measure. Its invariance follows by the two cancelling factors \(m(r)\) when \(a\mapsto ra\). The product \(db\,d^\times a\) is left Haar measure on \(P_K\), because left multiplication is
\((b,a)\mapsto(b+b_0a,a_0a)\).
Right multiplication by \(g(c,r)\) is
\((b,a)\mapsto(c+br,ar)\),
and multiplies the measure by \(m(r)\). Thus, with exactly the right-translation convention of Section 9,
\[
\delta(g(b,a))=m(a).
\tag{10.13}
\]
In \(\mathbb Q_p\), \(q=p\) and \(\pi=p\), giving \(m(x)=|x|_p\). For the complex field the same Haar definition gives \(m(z)=|z|^2\); the modulus itself then fails the triangle inequality. This explains why Lemma 10.1 did not initially assume a metric from \(m\).

As a positive-characteristic example, take \(K=\mathbb F_4((t))\). Its compact ring is the product of the finite coefficient sets in \(\mathbb F_4[[t]]\), and \(tR_K\) has index four. The normalized coefficient-product Haar measure therefore gives \(m(t)=1/4\). Here the residue prime is two, but the integer two is zero in the field.

## Exercises with solutions

**Exercise 1 (Foundations, 3 points).** For \(q=10/21\), compute the two orbit counts, the number of translation parameters in its double coset modulo \(\mathbb Z\), and its time eigenvalue. Repeat for the inverse.

*Solution.* Lowest terms give \(L=21,R=10\). The translation parameters differ by multiples of \(1/21\), so there are 21 modulo \(\mathbb Z\). The time multiplier is \((10/21)^{it}\). Inversion gives \(q^{-1}=21/10\), \(L=10,R=21\), ten translation parameters and multiplier \((21/10)^{it}\).

**Exercise 2 (Calculation, 4 points).** Reduce \(\mu_6e(1/5)\mu_4^*\) to coprime normal terms. Find the correct double-coset translation parameter for \(\mu_3e(2/7)\mu_2^*\).

*Solution.* The common divisor is two. The two residues with \(2s=1/5\) are \(1/10,3/5\). Equation (4.8) gives

\[
\mu_6e(1/5)\mu_4^*
=\tfrac12\mu_3e(1/10)\mu_2^*
+\tfrac12\mu_3e(3/5)\mu_2^*.
\]

For the second monomial, (4.5) gives dilation \(3/2\) and translation \((2/7)/2=1/7\), modulo \((1/2)\mathbb Z\). Its coefficient is \(1/\sqrt6\).

**Exercise 3 (Proof, 5 points).** Explain why the canonical KMS state need not be a trace. Exhibit two positive products with different state values, using a dilation with \(n>1\).

*Solution.* Let \(a=\mu_n\). Then \(a^*a=1\), so \(\phi(a^*a)=1\). Equations (6.3) and (6.4) give \(\phi(aa^*)=1/n\). A trace would assign equal values to these products. The KMS identity holds because \(\alpha_i(a)=n^{-1}a\): \(\phi(aa^*)=\phi(a^*\alpha_i(a))=1/n\).

**Exercise 4 (Arithmetic symmetry, 5 points).** In the quotient \(\mathbb Z/12\mathbb Z\), express the indicator of the unit orbit containing \(4\) as a linear combination of divisibility indicators. Identify the corresponding projection expression in \(D\).

*Solution.* The orbit is \(\{4,8\}\), the residues with greatest common divisor four with 12. They are divisible by four and are not divisible by twelve. Its indicator is \(1_{4\mid z}-1_{12\mid z}\), corresponding to \(P_4-P_{12}\). This is a projection because \(P_{12}\le P_4\). It is fixed by \(W\).

**Exercise 5 (Analysis, 6 points).** Let \(x\) be an element of a C*-algebra with a continuous action of \(K=\prod_p\mathbb T\). Prove that averaging against product circle measure is faithful on positive elements. Explain which part fails if the averaging measure is supported only at a single point of \(K\).

*Solution.* If \(x\ge0\) and its average is zero, a state \(\rho\) gives a continuous nonnegative scalar function \(\rho(\gamma_z(x))\) with integral zero. Every open neighbourhood contains a cylinder neighbourhood, which has positive product measure. A positive value anywhere would therefore force a positive integral. The function vanishes at the identity, so \(\rho(x)=0\) for every state, and \(x=0\). A single-point measure has no full-support property; the conclusion that the function vanishes everywhere fails. Its averaging map is nevertheless an automorphism and hence faithful, but this particular integral argument no longer supplies that conclusion.

**Exercise 6 (Adelic fiber size, 7 points).** Compute the fiber size and the norm of \(S_{12}\) in (7.10). Explain why its normalized adjoint is an isometry.

*Solution.* The local indices are \(2^2=4\) at the prime two and \(3\) at the prime three; every other local index is one. Thus \([12^{-1}R:R]=12\), and \(\|S_{12}\|=\sqrt{12}\). The identity \(S_{12}S_{12}^*=12\,1\) gives
\((12^{-1/2}S_{12}^*)^*(12^{-1/2}S_{12}^*)=1\).
It is the isometry \(r(\mu_{12})\).

**Exercise 7 (The reciprocal unit, 6 points).** Choose \(u\in W\) with residue two modulo five. Evaluate \(\theta_u(e(1/5))\) and \(\Theta_u(e(1/5))\) at \(z=1\in R\), using the Fourier identification. Why can these two actions not be indexed identically?

*Solution.* The residue inverse of two modulo five is three. Thus the abstract action gives \(e(2/5)(1)=\exp(4\pi i/5)\), whereas conjugation by \(g(0,u)\) gives \(e(3/5)(1)=\exp(6\pi i/5)\). They differ. The equality is \(\theta_u=\Theta_{u^{-1}}\) on the identified regular algebra. Such a unit exists, for example with \(u_5=2\) and all other prime coordinates equal to one.

**Exercise 8 (Local distance, 6 points).** In \(T_3\), find the common ancestor and distance of \(B(0,2)\) and \(B(3,1)\). List the children of their common ancestor. Check the distance using the normalized lattice quotient.

*Solution.* Here \(v_3(0-3)=1\), so \(h=\min\{2,1,1\}=1\). The common ancestor is \(3\mathbb Z_3=B(0,1)=B(3,1)\), and the distance is \(2+1-2=1\). Its children are \(B(0,2),B(3,2),B(6,2)\). In the parent basis \((3,0),(0,1)\), the lattice for \(B(0,2)\) is generated by \((3,0),(0,1)\) in coordinate form; its quotient is \(\mathbb Z_3/3\mathbb Z_3\), again giving distance one.

**Exercise 9 (The lattice chart, 7 points).** Describe the normalized lattice and all neighbors of \(B(1/2,0)\) in \(T_2\). Why is this a valid vertex even though its center is not integral?

*Solution.* Formula (8.4) gives \(L=\mathbb Z_2(1,0)+\mathbb Z_2(1/2,1)\); its second-coordinate image is \(\mathbb Z_2\). Its children are \(B(1/2,1)\) and \(B(3/2,1)\), and its parent is \(B(1/2,-1)=2^{-1}\mathbb Z_2\). The three corresponding index-two intermediate lattices are the two child lattices and \(2L(1/2,-1)\). The center can be any element of \(\mathbb Q_2\); normalization requires the second-coordinate image to be \(\mathbb Z_2\), and places no integrality condition on the first coordinate of \((x,1)\).

**Exercise 10 (Two prime coordinates, 8 points).** Select one child-parent edge in \(T_2\) and one in \(T_3\), fixing every other coordinate. List the maximal simplices in their product. Compute the norm and coisometry relation of the operator that takes both parents, and identify the corresponding Hecke generator.

*Solution.* Label a vertex by which coordinates have reached their parents. The maximal chains are
\(\varnothing\subset\{2\}\subset\{2,3\}\)
and
\(\varnothing\subset\{3\}\subset\{2,3\}\);
they give the two triangles in the square. The simultaneous parent operator is \(S_2\otimes S_3\), with six preimages for every vertex, norm \(\sqrt6\), and product with its adjoint equal to \(6\,1\). Its normalization by \(6^{-1/2}\) is \(r(\mu_6^*)\), since \(\mu_6=\mu_2\mu_3\) and the two coordinate operators commute. Its normalized adjoint is the Hecke isometry \(r(\mu_6)\).

**Exercise 11 (A shell in the local corner, 8 points).** At a prime \(p\), express the indicator of the double coset with \(v_p(a)=0,v_p(b)=-2\) in terms of \(F_{i,j}\). Give the value of its Toeplitz KMS state at inverse temperature \(\beta>0\).

*Solution.* Since \(a\) is a unit, \(x=b/a\) has valuation \(-2\). Equation (9.10) gives
\[
1_{\{v_p(a)=0,\ v_p(b)=-2\}}
=p^2F_{2,2}-pF_{1,1}.
\]
The functions correspond to \(V_p^2V_p^{*2}\) and \(V_pV_p^*\). The Toeplitz KMS values from the phase lesson, Theorem 11.3, are \(p^{-2\beta}\) and \(p^{-\beta}\). Thus the answer is \(p^{2-2\beta}-p^{1-\beta}\). This can be negative for \(\beta>1\): a nonnegative group convolution function need not represent a positive C*-algebra element.

**Exercise 12 (The defect and the Haar convention, 6 points).** Compute the expectation of \(e-V_pV_p^*\) in the base-vector representation of the corner, and compare it with the \(\beta\)-KMS value. Explain the sign of the time eigenvalue of \(V_p\).

*Solution.* Equation (9.11) gives \(1-p^{-1}>0\), proving that the corner isometry is not unitary. Its \(\beta\)-KMS value is \(1-p^{-\beta}\). Right multiplication has measure factor \(\delta(g_p)=|p|_p=p^{-1}\), while the chosen dynamics uses \(\delta^{-it}\). Consequently \(\sigma_t(V_p)=p^{it}V_p\), in agreement with the prime occupation energy \(\log p\).

**Exercise 13 (Residue size and ramification, 6 points).** A local field of characteristic zero has residue field of size nine and \(v(3)=2\). Compute \(m(\pi)\), \(m(3)\), \(m(1/3)\), and \([R_K:\pi^4R_K]\). Which integer primes have modulus less than one?

*Solution.* Here \(m(\pi)=1/9\), \(m(3)=9^{-2}=1/81\), and \(m(1/3)=81\). Each successive additive quotient has nine elements, by multiplication by a power of \(\pi\), so the index is \(9^4=6561\). The residue field has characteristic three. Every other integer prime has nonzero image in its prime subfield, hence is a unit and has modulus one.

**Exercise 14 (Positive characteristic, 6 points).** In \(\mathbb F_4((t))\), compute the modulus of \(t^3+t^5\), the index of \(t^2R_K\) in \(R_K\), and the modulus of the integer two. Why is two not a uniformizer?

*Solution.* The leading exponent is three, and \(1+t^2\) is a unit, so the modulus is \(4^{-3}=1/64\). The quotient by \(t^2\) is described by the two coefficients of \(1,t\), giving \(4^2=16\) elements. Two is zero, of modulus zero; a uniformizer is nonzero and has modulus \(1/4\). The distinguished residue prime need not be a nonzero element of the field.

**Exercise 15 (Why compactness forces maximality, 7 points).** Let \(B\) be a compact subring of \(K\). Prove \(B\subset R_K\) without assuming that \(B\) is an ideal or that it contains \(1\). Show that \(J_K\) is principal without starting from discreteness of the value group.

*Solution.* Continuity makes \(m(B)\) bounded. If \(x\in B\) had modulus greater than one, the powers \(x^n\in B\) would contradict boundedness. Hence \(B\subset R_K\). For the ideal assertion, the ultrametric inequality makes the unit set open, so \(J_K\) is compact and open. Its nonzero maximum modulus \(\lambda<1\) is attained at some \(\pi\). Every \(x\in J_K\) satisfies \(m(x/\pi)\le1\), and every element of \(\pi R_K\) has modulus at most \(\lambda\). Thus \(J_K=\pi R_K\). Discreteness follows afterward from the gap \((\lambda,1)\).

**Exercise 16 (A modulus is not always a metric, 7 points).** Compute the Haar modulus of multiplication by two on \(\mathbb R\) and on \(\mathbb C\). Check the triangle inequality for \(m(z-w)\) on \(\mathbb C\) using \(0,1,2\). What is the affine module and time character of \(g(0,\pi)\) in the nonarchimedean case?

*Solution.* The real length factor is two, and the complex area factor is four. On \(\mathbb C\), \(m(2-0)=4\), whereas \(m(2-1)+m(1-0)=2\), so the triangle inequality fails. The square root of that modulus gives the usual complex metric, but the Haar modulus retains its area normalization. In the nonarchimedean case (10.13) gives \(\delta(g(0,\pi))=1/q\); dynamics using \(\delta^{-it}\) has character \(q^{it}\), matching an occupation energy \(\log q\).

## References

- [Bost–Connes] J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) 1 (1995), 411–457. [Author-hosted article](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
- [Connes–Marcolli] A. Connes and M. Marcolli, *From physics to number theory via noncommutative geometry*, in Frontiers in Number Theory, Physics, and Geometry I, Springer, 2006. [Open exposition](https://www.its.caltech.edu/~matilde/QSMQlattLesHouches.pdf).
- [Milne ANT] J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), course notes, for local fields, finite adeles and ideles.
- [Casselman] B. Casselman, [*Geometry of the tree*](https://personal.math.ubc.ca/~cass/research/pdf/Tree.pdf), from *Essays in harmonic analysis on p-adic SL(2)*, revised 10 April 2019, §§3–4, for the lattice tree over a p-adic field.

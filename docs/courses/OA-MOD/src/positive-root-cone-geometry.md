# Adding square roots of normal functionals

Two positive normal functionals can be added as functionals, or their positive Hilbert-space representatives can be added as vectors. These operations differ even for the scalar algebra. We construct the vector addition directly, recover its mixed pairing from bounded operators, and show that formal differences of positive roots already give the complete real part of standard L2.

Throughout, \(M\) is an arbitrary von Neumann algebra and \(M_*^+\) denotes its bounded positive normal functionals. Neither a faithful normal state on all of \(M\) nor a countable family of projections is assumed. Hilbert inner products are linear in their first variable.

The exact inputs are the real decomposition of a self-dual cone, the complete cone-vector norm estimates, and the existence and unique comparison of arbitrary standard forms, including their normal-functional representatives. The axiomatic geometric argument verifies that the decomposition and estimates apply to every standard form, before comparison. These results provide full in-course proofs at their declared prerequisites. In a standard form \((M,H,J,P)\), write \(\xi_\varphi\in P\) for the unique vector representing \(\varphi\):

\[
 \begin{aligned}
 \varphi(x)&=\langle x\xi_\varphi,\xi_\varphi\rangle,\\
 \|\xi_\varphi\|^2&=\varphi(1).
 \end{aligned}
 \tag{PR.1}
\]

The existing construction of canonical weight coordinates gives another realization of the same space. The construction below specifies its positive-root arithmetic without choosing a permanent weight.

## Start with two kinds of addition

Use \(\sqrt{\varphi}\) as a formal name for \(\xi_\varphi\), without applying scalar functional calculus to a functional. Define

\[
 \varphi\boxplus\psi
   :=\omega_{\xi_\varphi+\xi_\psi},\qquad
 \omega_v(x):=\langle xv,v\rangle.
 \tag{PR.2}
\]

A vector functional in the normal standard representation is a bounded normal functional, and \(\xi_\varphi+\xi_\psi\) belongs to the closed convex cone. Uniqueness of cone representatives therefore gives

\[
 \xi_{\varphi\boxplus\psi}=\xi_\varphi+\xi_\psi.
 \tag{PR.3}
\]

Thus the addition of roots is defined by

\[
 \begin{aligned}
 \sqrt{\varphi}+\sqrt{\psi}
   &:=\sqrt{\varphi\boxplus\psi},\\
 \lambda\sqrt{\varphi}&:=\sqrt{\lambda^2\varphi}
       \quad(\lambda\ge0).
 \end{aligned}
 \tag{PR.4}
\]

Positive homogeneity of the representing vector follows directly from (PR.1) and its uniqueness.

For \(M=\mathbb C\), let \(\varphi(z)=4z\) and \(\psi(z)=9z\). Their root vectors are \(2\) and \(3\). The usual functional sum has value \(13\) at the identity; the root sum represents the functional with value \(25\). The formula \(\sqrt{\varphi+\psi}=\sqrt{\varphi}+\sqrt{\psi}\) therefore fails already in one dimension.

The root sum is nevertheless controlled by the ordinary sum. For \(x\ge0\),

\[
 \begin{aligned}
 (\varphi\boxplus\psi)(x)
  &=\|x^{1/2}(\xi_\varphi+\xi_\psi)\|^2\\
  &\le2\|x^{1/2}\xi_\varphi\|^2
        +2\|x^{1/2}\xi_\psi\|^2\\
  &=2(\varphi+\psi)(x).
 \end{aligned}
 \tag{PR.5}
\]

The bound applies in the positive-functional order. Its constant is attained when \(\varphi=\psi\ne0\). No commuting-density assumption enters this proof.

## A bounded factor for a dominated root

Let \(0\le\varphi\le\sigma\) in \(M_*^+\), and let \(e=s(\sigma)\). There is exactly one \(A\in M\) satisfying

\[
 A=Ae,\qquad A\xi_\sigma=\xi_\varphi.
 \tag{PR.6}
\]

It is a contraction and in fact belongs to \(eMe\).

**Proof.** For a positive \(y'\in M'\), pointwise \(J\)-fixedness of both cone vectors and antiunitarity give

\[
 \begin{aligned}
 \langle y'\xi_\varphi,\xi_\varphi\rangle
    &=\varphi(Jy'J)\\
    &\le\sigma(Jy'J)\\
    &=\langle y'\xi_\sigma,\xi_\sigma\rangle.
 \end{aligned}
 \tag{PR.7}
\]

Here \(Jy'J\) is positive and belongs to \(M\); the scalar values are real, so conjugation by the antiunitary causes no change of their value. Taking \(y'=z'^*z'\) shows that

\[
 A_0(z'\xi_\sigma):=z'\xi_\varphi
       \quad(z'\in M')
 \tag{PR.8}
\]

is well defined and contractive. Its domain is a linear subspace, and its closure is \(eH\), by the support theorem in SF-06.

Domination implies \(s(\varphi)\le e\): the positive value \(\varphi(1-e)\) is at most \(\sigma(1-e)=0\). Thus \(\xi_\varphi\in eH\), and every \(z'\xi_\varphi\) lies there because \(z'\) commutes with \(e\). Extend \(A_0\) continuously to \(eH\), then define it to be zero on \((1-e)H\).

For \(w',z'\in M'\), the rule (PR.8) gives \(A_0w'z'\xi_\sigma=w'A_0z'\xi_\sigma\). Boundedness and density extend this commutation to \(eH\). Both \(eH\) and its complement reduce \(M'\), so the extension commutes with \(M'\) on all of \(H\). Hence \(A\in(M')'=M\). The source and range conditions give \(A=eAe\); contractivity and (PR.6) follow from the construction.

If \(B\in M\) also satisfies (PR.6), then \(Bz'\xi_\sigma=z'\xi_\varphi=Az'\xi_\sigma\). Equality on the dense subspace \(M'\xi_\sigma\) gives \(B=A\) on \(eH\), while \(B=Be\) makes both vanish on its complement. This proves uniqueness. If \(\sigma=0\), then \(\varphi=0\), \(e=0\) and \(A=0\), so the same statement includes the zero case. \(\square\)

For \(\sigma=\varphi+\psi\), denote these two uniquely specified factors by \(A\) and \(B\). They satisfy the stronger operator identity

\[
 A^*A+B^*B=e.
 \tag{PR.9}
\]

Indeed for \(z'\xi_\sigma\in eH\), (PR.7) gives

\[
 \|Az'\xi_\sigma\|^2+\|Bz'\xi_\sigma\|^2
   =\|z'\xi_\sigma\|^2.
\]

The equality extends to all of \(eH\). Polarization identifies the bounded operators there; all three operators vanish on \((1-e)H\). In particular \(\|A+B\|\le\sqrt2\), by the elementary inequality
\(\|Av+Bv\|^2\le2(\|Av\|^2+\|Bv\|^2)\).

The bound (PR.5) is a vector argument. It must not be inferred by writing \(C^*xC\le\|C\|^2x\) for a general \(C\in M\): that operator inequality is false without additional hypotheses. For example, in two-by-two matrices let \(x=\operatorname{diag}(1,0)\) and let \(C\) interchange the two coordinate vectors. Then \(\|C\|=1\) and \(C^*xC=\operatorname{diag}(0,1)\), which is not dominated by \(x\).

## Recover the sum and its mixed pairing

For \(\varphi,\psi\in M_*^+\), put \(\sigma=\varphi+\psi\) and use the factors of PR-02. Then, for every \(x\in M\),

\[
 \begin{aligned}
 (\varphi\boxplus\psi)(x)
    &=\sigma(C^*xC),\\
 C&:=A+B.
 \end{aligned}
 \tag{PR.10}
\]

This is (PR.2), since \((A+B)\xi_\sigma=\xi_\varphi+\xi_\psi\). All values are finite complex values of bounded functionals; no extended-weight domain is being suppressed.

Define the root pairing by

\[
 \begin{aligned}
 k(\varphi,\psi)
    &:=\langle\xi_\varphi,\xi_\psi\rangle\\
    &=\sigma(B^*A).
 \end{aligned}
 \tag{PR.11}
\]

The second equality uses the first-variable-linear inner-product convention:
\(\langle A\xi_\sigma,B\xi_\sigma\rangle
=\langle B^*A\xi_\sigma,\xi_\sigma\rangle\).
Self-duality makes this value real and nonnegative. It is symmetric, and

\[
 \begin{aligned}
 k(\varphi,\varphi)&=\varphi(1),\\
 0\le k(\varphi,\psi)
    &\le\sqrt{\varphi(1)\psi(1)}.
 \end{aligned}
 \tag{PR.12}
\]

The upper bound is Hilbert-space Cauchy–Schwarz. In particular \(k(\varphi,0)=0\).

The mixed product is essential. The expression with \((A+B)^*(A+B)\) instead gives

\[
 \begin{aligned}
 \sigma\bigl((A+B)^*(A+B)\bigr)
    &=\varphi(1)+\psi(1)\\
    &\quad+2k(\varphi,\psi).
 \end{aligned}
 \tag{PR.13}
\]

It is the squared norm of the root sum, rather than its mixed pairing. If \(\psi=0\ne\varphi\), the two quantities are respectively \(\varphi(1)\) and \(0\).

These formulas are independent of the chosen standard form. Let \(V:H_1\to H_2\) be SE-10's unique comparison for the same abstract algebra. It maps each \(\xi_\rho^{(1)}\) to \(\xi_\rho^{(2)}\), since it intertwines the algebra and takes one cone onto the other. It therefore preserves the vector sum and every pairing. It also takes the uniquely characterized factor \(A\) to the factor with the same abstract algebra element in the other representation: the support and vector conditions (PR.6) are intertwined, and uniqueness applies. Consequently (PR.10)–(PR.11) define operations and scalars belonging to \(M\) itself.

## Positive roots form a cancellative cone

Let \(R_+(M)\) be the set of the formal symbols \(\sqrt{\varphi}\), with the operations (PR.4). The map

\[
 R_+(M)\longrightarrow P,\qquad
 \sqrt{\varphi}\longmapsto\xi_\varphi
 \tag{PR.14}
\]

is bijective and preserves addition and nonnegative scalar multiplication.

Surjectivity holds because each \(\xi\in P\) defines a bounded normal positive functional \(\omega_\xi\), and uniqueness gives \(\xi_{\omega_\xi}=\xi\). Injectivity follows from (PR.1). Hence the following identities follow from vector addition and scalar multiplication, with equality of roots meaning equality of their functionals:

\[
 \begin{aligned}
 u+v&=v+u,\\
 (u+v)+w&=u+(v+w),\\
 u+0&=u,\\
 u+w=v+w&\Longrightarrow u=v,\\
 0u&=0,\\
 (\lambda\mu)u&=\lambda(\mu u),\\
 (\lambda+\mu)u&=\lambda u+\mu u,\\
 \lambda(u+v)&=\lambda u+\lambda v.
 \end{aligned}
 \tag{PR.15}
\]

Here \(u,v,w\in R_+(M)\) and \(\lambda,\mu\ge0\). Also \(1u=u\). If \(u+v=0\), the corresponding cone vectors are opposite; pointedness gives \(u=v=0\). These statements include zero functionals without assigning an artificial support to them.

The pairing \(k(u,v)\), obtained from (PR.11) by the root names, is additive in each variable and homogeneous under nonnegative scalars. This follows from (PR.14) and bilinearity of the real inner product on \(J\)-fixed vectors. It concerns root addition, not ordinary addition of positive functionals.

## Differences give a complete real Hilbert space

For \((u,v),(u',v')\in R_+(M)^2\), set

\[
 \begin{aligned}
 (u,v)\sim(u',v')
     &\quad\Longleftrightarrow\\
 u+v'&=u'+v.
 \end{aligned}
 \tag{PR.16}
\]

Denote a class by \([u,v]\). The relation is an equivalence relation, and the rules

\[
 \begin{aligned}
 {}[u,v]+[a,b]&=[u+a,v+b],\\
 t[u,v]&=[tu,tv] &&(t\ge0),\\
 t[u,v]&=[(-t)v,(-t)u] &&(t<0)
 \end{aligned}
 \tag{PR.17}
\]

make the quotient a real vector space.

To verify all representative issues, define a map into the real Hilbert space \(H_J:=\{\eta:J\eta=\eta\}\) by

\[
 T[u,v]=\xi_u-\xi_v.
 \tag{PR.18}
\]

In this display, \(\xi_{\sqrt{\varphi}}\) means \(\xi_\varphi\). By (PR.14), the equality in (PR.16) is exactly equality of the two differences in (PR.18). Thus reflexivity, symmetry and transitivity follow from equality in \(H_J\), and \(T\) is both well defined and injective. The operations (PR.17) give the corresponding vector operations after applying \(T\), which proves they are independent of representatives. The real-vector-space identities follow by injectivity. For nonnegative \(\lambda,\mu\), another useful scalar formula is

\[
 (\lambda-\mu)[u,v]
       =[\lambda u+\mu v,\lambda v+\mu u].
 \tag{PR.19}
\]

Applying \(T\) verifies it even when the same real scalar has different such expressions.

For \(z=[u,v]\) and \(w=[a,b]\), the correct real inner product retains both mixed terms:

\[
 \begin{aligned}
 g(z,w)&=k(u,a)-k(u,b)\\
       &\quad-k(v,a)+k(v,b).
 \end{aligned}
 \tag{PR.20}
\]

Expanding (PR.18) gives precisely
\(g(z,w)=\langle Tz,Tw\rangle\).
It follows at once that (PR.20) is well defined, real, symmetric and bilinear. It is positive definite: \(g(z,z)=0\) means \(Tz=0\), hence \(z=[0,0]\), by injectivity.

Surjectivity and completeness require the entire real-cone decomposition, not just density of a span. SF-06 proves that every \(\eta\in H_J\) has a decomposition
\(\eta=p-m\), where \(p,m\in P\) and \(\langle p,m\rangle=0\). The corresponding positive normal functionals yield a class mapping exactly to \(\eta\). Thus \(T\) is onto.

The space \(H_J\) is closed: if \(J\eta_n=\eta_n\) and \(\eta_n\to\eta\), continuity of the isometry \(J\) gives \(J\eta=\eta\). It is therefore a complete real Hilbert space. Since \(T\) is an onto isometry, the quotient itself is complete. No additional completion creates new vectors.

Call the quotient \(L^2_{\mathbb R}(M)\). Its positive cone is the set of \([u,0]\). Under \(T\) this is exactly \(P\), so it is closed, pointed and self-dual in the real Hilbert space. The orthogonal positive and negative parts of a class are unique by SF-06.

## Complexification and the canonical standard form

Define \(L^2(M)=L^2_{\mathbb R}(M)+iL^2_{\mathbb R}(M)\), with

\[
 \begin{aligned}
 \langle z+iw,a+ib\rangle
    &=g(z,a)+g(w,b)\\
    &\quad+i g(w,a)-i g(z,b).
 \end{aligned}
 \tag{PR.21}
\]

This is the complex inner product linear in its first variable. The map

\[
 U(z+iw)=Tz+iTw
 \tag{PR.22}
\]

is an onto unitary to \(H\). The equality of the inner products is obtained by expanding the right side with the first-variable-linear convention. Every \(\eta\in H\) has the unique decomposition

\[
 \begin{aligned}
 \eta&=\frac{\eta+J\eta}{2}\\
     &\quad+i\,\frac{\eta-J\eta}{2i}.
 \end{aligned}
 \tag{PR.23}
\]

with both displayed parts in \(H_J\). This proves surjectivity; it also proves completeness of (PR.21) without an unproved algebraic-completion step.

The conjugation and algebra action are

\[
 \begin{aligned}
 J_M(z+iw)&=z-iw,\\
 \pi_M(x)&=U^{-1}xU.
 \end{aligned}
 \tag{PR.24}
\]

The first is an antiunitary involution and satisfies \(UJ_M=JU\). The second is a faithful normal unital star representation, because those properties are preserved under the unitary \(U\). With the positive cone of PR-05, these operators form a standard form: all four axioms of SE-01 transport through \(U\).

They are independent of the temporary standard form. The comparison \(V\) of PR-03 satisfies \(VT_1=T_2\) on every difference class, hence \(VU_1=U_2\) on the whole complexification. Since \(Vx_1=x_2V\), both coordinate constructions give the same \(\pi_M(x)\). Both give the conjugation in (PR.24) and the same root cone. The zero algebra produces the zero real and complex Hilbert spaces throughout.

If \(\theta:M\to N\) is a unital star isomorphism, the prescription

\[
 \sqrt{\varphi}\longmapsto
        \sqrt{\varphi\circ\theta^{-1}}
 \tag{PR.25}
\]

extends to the unique unitary between these constructions that implements \(\theta\) and carries the positive cone onto the positive cone. Indeed SE-10 gives a comparison between arbitrary standard forms for \(M\) and \(N\); the representative-vector identity proves that it respects (PR.25), addition and the pairing. Extend it to differences and then complexify. Composition and inversion agree with composition and inversion of the isomorphisms, by the uniqueness already proved.

## Topology and a noncommuting density model

The exact root metric is

\[
 \begin{aligned}
 d(\varphi,\psi)^2
   &=\varphi(1)+\psi(1)\\
   &\quad-2k(\varphi,\psi).
 \end{aligned}
 \tag{PR.26}
\]

Set \(m=\sqrt{\varphi(1)}+\sqrt{\psi(1)}\). SF-07 and SE-11 give

\[
 \begin{aligned}
 d(\varphi,\psi)^2&\le\|\varphi-\psi\|,\\
 \|\varphi-\psi\|&\le m\,d(\varphi,\psi).
 \end{aligned}
 \tag{PR.27}
\]

Consequently \(d\) is a complete metric on \(M_*^+\), because its isometric image is the closed cone \(P\). It gives exactly the predual norm topology. The first inequality sends predual norm convergence to root norm convergence; in the other direction the roots have eventually bounded norms along a convergent net, so the second inequality applies. This does not assert that an unbounded family of infinite weights is represented by vectors.

Root addition is jointly continuous in these topologies. In fact

\[
 \begin{aligned}
 d(\varphi\boxplus\psi,\alpha\boxplus\beta)
     &\le d(\varphi,\alpha)\\
     &\quad+d(\psi,\beta).
 \end{aligned}
 \tag{PR.28}
\]

by the triangle inequality on the sum vectors. Formula (PR.27) then gives predual norm convergence of their represented functionals. The scalar bound \(d(\varepsilon\varphi,0)=\sqrt{\varepsilon\varphi(1)}\) shows why a globally Lipschitz estimate from the predual norm to the root norm cannot hold at zero.

For \(M=M_2(\mathbb C)\), use the Hilbert–Schmidt standard form with first-variable-linear inner product \(\langle X,Y\rangle=\operatorname{Tr}(Y^*X)\). A positive density \(h\) defines \(\varphi_h(x)=\operatorname{Tr}(hx)\) and has root vector \(h^{1/2}\). Thus

\[
 \begin{aligned}
 k(\varphi_h,\varphi_l)
     &=\operatorname{Tr}(l^{1/2}h^{1/2}),\\
 \varphi_h\boxplus\varphi_l
     &=\varphi_{(h^{1/2}+l^{1/2})^2}.
 \end{aligned}
 \tag{PR.29}
\]

The trace pairing is real nonnegative because cyclicity writes it as the trace of a positive conjugate product.

Take the noncommuting rank-one projections

\[
 \begin{aligned}
 p&=\begin{pmatrix}1&0\\0&0\end{pmatrix},\\
 q&=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \end{aligned}
 \tag{PR.30}
\]

Their roots are themselves, their mixed pairing is \(1/2\), and

\[
 \begin{aligned}
 (p+q)^2&=
       \begin{pmatrix}5/2&1\\1&1/2\end{pmatrix},\\
 (p+q)^2-(p+q)&=
       \begin{pmatrix}1&1/2\\1/2&0\end{pmatrix}.
 \end{aligned}
 \tag{PR.31}
\]

The second matrix takes the values \(-2\) and \(1\) on the quadratic tests \((1,-3)\) and \((1,0)\), respectively. Testing the two functionals on the corresponding positive rank-one matrices proves that neither root addition nor ordinary functional addition dominates the other in general. Their values at the identity are \(3\) and \(2\); a comparison of total masses alone therefore does not prove a functional-order comparison. The universal upper bound (PR.5) remains valid.

## Problems with complete solutions

**Problem 1.** For a sigma-finite measure space, take \(M=L^\infty(X,\mu)\) in its multiplication standard form. Given nonnegative \(f,g\in L^1(X,\mu)\), compute the root sum and pairing, and identify the factor \(A\) of PR-02 with \(\sigma=\varphi_f+\varphi_g\).

**Solution.** The root vectors are \(\sqrt f,\sqrt g\in L^2\). Their sum represents the integrable density
\((\sqrt f+\sqrt g)^2\le2(f+g)\), and

\[
 k(\varphi_f,\varphi_g)=\int_X\sqrt{fg}\,d\mu.
 \tag{PR.32}
\]

The integral is finite by Cauchy–Schwarz. The support of \(\sigma\) is \(E=\{f+g>0\}\), modulo null sets. The multiplier

\[
 A(x)=
 \begin{cases}
   \sqrt{f(x)/(f(x)+g(x))},&x\in E,\\
   0,&x\notin E
 \end{cases}
 \tag{PR.33}
\]

is a contraction, is supported on \(E\), and sends \(\sqrt{f+g}\) to \(\sqrt f\). PR-02's uniqueness identifies it with \(A\); the analogous multiplier gives \(B\). On \(E\), \(A^*A+B^*B=1\), and both vanish off \(E\), verifying (PR.9), including the common-zero set.

**Problem 2.** Why can the two mixed terms in (PR.20) not be combined into \(-2k(u,b)\)? Test the proposed expression on scalar root vectors \(u=2\), \(v=1\), \(a=4\), \(b=3\), and on a representative of the zero class.

**Solution.** The actual difference vectors are both \(1\), so their inner product is \(1\). The full formula gives \(8-6-4+3=1\). The proposed formula gives \(8-12+3=-1\), while reversing the arguments gives \(8-8+3=3\); it is not symmetric. For \([u,v]=[1,1]=0\) and \([a,b]=[2,0]\), the full expression is \(2-0-2+0=0\), while the proposed expression is \(2\). It therefore also fails to be defined on equivalence classes.

**Problem 3.** Let \(M=\ell^\infty(I)\) for an arbitrary index set. Describe all root difference classes and their complexification without imposing a countability condition on \(I\).

**Solution.** In the standard form on \(\ell^2(I)\), a positive normal functional is given by a nonnegative summable family \(f=(f_i)\), and its root vector is \((\sqrt{f_i})\). To verify the functional assertion, put \(f_i=\varphi(1_{\{i\}})\). The net of finite coordinate projections increases to \(1\), so normality gives \(\varphi(1)=\sup_{F\subset I\text{ finite}}\sum_{i\in F}f_i\). For \(a\in\ell^\infty(I)_+\), its finite coordinate restrictions increase to \(a\); normality gives \(\varphi(a)=\sum_i f_i a_i\). Linear extension determines \(\varphi\) on all of \(M\). Conversely a nonnegative summable family defines a bounded positive functional by this series. For a bounded increasing positive net, first restrict the sum to a finite set, where the net limit commutes with the finite sum, then bound the omitted tail by its summable mass times the common bound. This proves normality, including arbitrary nets.

Every vector in \(\ell^2(I)\) has at most countably many nonzero coordinates: for each positive integer \(n\), only finitely many coordinates can have magnitude at least \(1/n\), and their countable union contains the support. This is a property of each vector, not a countability assumption on \(I\).

For a real \(r\in\ell^2(I)\), let \(r_i^+=\max(r_i,0)\) and \(r_i^-=\max(-r_i,0)\). Their squares are nonnegative summable families, so they define positive normal functionals. Their root difference maps exactly to \(r\), and their supports are disjoint, giving orthogonality. Thus the quotient is all of the real \(\ell^2(I)\) and its complexification is all of \(\ell^2(I)\). The conjugation is coordinatewise complex conjugation and the algebra acts by coordinatewise multiplication. A single positive functional need not be faithful when \(I\) is uncountable; the construction never demanded one.

### Mathematical sources and contribution

Fumio Hiai's freely accessible [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383v1), Section 3.1, supplies the standard-form, scalar and Hilbert–Schmidt models and the complete self-dual-cone decomposition proof in Proposition 3.7. Theorem 3.12 states the cone-vector norm estimates; Theorem 3.13 gives the uniqueness theorem, whose displayed proof there assumes sigma-finiteness. The exact arbitrary-cardinality proofs used here are the linked in-course SF and SE results. The bounded commutant-factor construction, complete root quotient argument, noncommuting tests and solved problems are independently written exposition by OpenAI Codex, October 2026, under CC0-1.0. This is classical mathematical exposition; it does not claim a new research theorem or independent review of the entire prerequisite graph.

## The cocycle endpoint behind a dominated root

Let \(0\le\varphi\le\sigma\) be bounded positive normal functionals on an arbitrary von Neumann algebra \(M\). Retain PR-02's uniquely characterized factor \(A\), and put \(e=s(\sigma)\), \(p=s(\varphi)\). We prove

\[
 A=[D\varphi:D\sigma]_{-i/2}.
 \tag{PR.34}
\]

The notation on the right has a precise support convention: restrict both functionals to \(N=eMe\), form the supported numerator cocycle relative to the faithful denominator \(\sigma|_N\), and regard its values as elements of \(eMe\subset M\). Its value at zero is \(p\), not an artificially enlarged identity. The imaginary value is the endpoint of a bounded, sigma-weakly continuous lower half-strip, holomorphic in its interior. We do not substitute a formal product of unbounded powers for this assertion.

If \(\sigma=0\), domination gives \(\varphi=0\), \(e=p=0\), and the corner, cocycle and factor are zero. Assume \(\sigma\ne0\). The exact added inputs are the faithful cone corner and its GNS identification, the common relative Tomita graph, relative imaginary-power implementation with its ordinary GNS identification, the intrinsic balanced cocycle, the centralizer criterion, and the supported completion and independence proofs. The spectral domains, closed-strip theorems, and normal vector-series tests supply the analytic step below.

### Put the denominator in its actual faithful space

SE-03 and SE-06 identify

\[
 \begin{aligned} K&=eJeJH,\\ J_e&=J|_K,\\ P_e&=P\cap K. \end{aligned}
 \tag{PR.35}
\]

as the standard form of \(N=eMe\). The vector \(\xi_\sigma\) is cyclic and separating there, and \(x\mapsto x\xi_\sigma\), \(x\in N\), is its entire finite GNS map. Let \(D=\Delta_{\sigma|_N}\) on \(K\); it is positive injective self-adjoint, with \(D^{1/2}\xi_\sigma=\xi_\sigma\).

Both \(\xi_\sigma\) and \(\xi_\varphi\) lie in \(K\). PR-02's construction has range in \(pH\): each initial vector is sent to \(z'\xi_\varphi\), which belongs to \(pH\), since \(z'\in M'\) commutes with \(p\). Continuity gives \(pA=A\). The restriction \(A|_K\) belongs to the faithful representation of \(N\), remains contractive, and sends \(\xi_\sigma\) to \(\xi_\varphi\). We use the same symbol \(A\) for that restriction. SE-03 makes recovery of its algebra element unambiguous.

### Close the relative graph, including its entire zero part

Write \(q=e-p\), the complementary projection in \(N\), and choose the finite complement

\[
 \begin{aligned} \eta(x)&=\sigma(qxq),\\ \rho&=\varphi+\eta\quad(x\in N). \end{aligned}
 \tag{PR.36}
\]

These are bounded positive normal functionals. On \(qNq\), \(\eta\) is faithful. If \(x\ge0\) and \(\rho(x)=0\), faithfulness on the two corners gives \(pxp=qxq=0\); hence \(x^{1/2}p=x^{1/2}q=0\), so \(x=0\). Thus \(\rho\) is faithful on \(N\). For every \(x\in N\),
\(\rho(px)=\varphi(x)=\rho(xp)\); the bounded finite domain is all of \(N\). CZ-05 therefore puts \(p\) in the centralizer of \(\rho\).

The cone vectors of \(\varphi\) and \(\eta\) have orthogonal support projections. They also lie in the orthogonal commutant ranges \(J_epJ_eK\) and \(J_eqJ_eK\). These projections commute with every \(x\in N\), so the mixed terms in the functional of their vector sum vanish. Cone uniqueness consequently gives
\(\xi_\rho=\xi_\varphi+\xi_\eta\), and \(J_epJ_e\xi_\rho=\xi_\varphi\).

SF-13 constructs a positive injective relative operator \(R=\Delta_{\rho,\sigma}\), with the full closed graph

\[
 \begin{aligned} S_{\rho,\sigma}&=J_eR^{1/2},\\ S_{\rho,\sigma}(x\xi_\sigma)&=x^*\xi_\rho\quad(x\in N). \end{aligned}
 \tag{PR.37}
\]

The domain \(N\xi_\sigma\) is a graph core. SI-08 and SI-12, transported by the same cone comparison, say that \(R^{it}\) implements \(\sigma_t^\rho\). Since \(p\) is fixed by that group, \(p\) commutes with every \(R^{it}\). Uniqueness of the spectral calculus for \(\log R\) then makes \(p\) reduce \(R\) and all its real powers.

Define \(C\) to be \(R\) on \(pK\) and zero on \(qK\). It is positive self-adjoint, supported exactly by \(p\), and

\[
 \begin{aligned} C^{1/2}&=pR^{1/2},\\ D(C^{1/2})&=(pK\cap D(R^{1/2}))\\ &\quad\oplus qK. \end{aligned}
 \tag{PR.38}
\]

The second formula specifies the whole zero part. The displayed product in the first formula denotes this closed supported extension.

Here is the required core check. For \(\zeta=p\zeta+q\zeta\in D(C^{1/2})\), replace the \(q\)-component by
\(q1_{[1/n,n]}(R)\zeta\). The resulting vectors belong to \(D(R^{1/2})\), converge to \(\zeta\), and have the same \(C^{1/2}\)-image. Approximate each of them in the graph norm of \(R^{1/2}\) by vectors of \(N\xi_\sigma\). This stronger graph approximation is also a \(C^{1/2}\)-graph approximation. Thus \(N\xi_\sigma\) is a graph core for \(C^{1/2}\).

On that core, commutation with \(J_epJ_e\) gives

\[
 \begin{aligned} J_eC^{1/2}(x\xi_\sigma)&=J_epJ_e\,x^*\xi_\rho\\ &=x^*\xi_\varphi. \end{aligned}
 \tag{PR.39}
\]

Hence \(J_eC^{1/2}\) is exactly the closure of the initial nonfaithful relative Tomita map, not just one closed extension. The initial map and its graph closure contain no choice of complement. Therefore its squared modulus \(C\) is independent of the completion \(\rho\).

For real \(t\), imaginary powers of \(C\) mean unitary powers on \(pK\), extended by zero on \(qK\), including \(C^0=p\). SI-14 and PC-02/04 now identify the actual supported cocycle:

\[
 \begin{aligned} {}[D\varphi:D\sigma]_t&=p[D\rho:D\sigma]_t\\ &=C^{it}D^{-it}. \end{aligned}
 \tag{PR.40}
\]

The faithful-cocycle identity is supplied by SI-14 after SI-12's full relative-GNS identification. PC-04 proves independence of the complement in the normalized supported class. Thus both the relative graph and the algebra-valued cocycle have been matched before taking imaginary time.

### Prove the two-operator strip criterion

We need a version that allows the first positive operator to have a kernel. Let \(C\ge0\) and \(D>0\) be positive self-adjoint operators on any Hilbert space \(K\), let \(P=s(C)\), and suppose a bounded \(B=PB\) satisfies

\[
 \begin{aligned} D(D^{1/2})&\subset D(C^{1/2}),\\ C^{1/2}\zeta&=BD^{1/2}\zeta\\ &\quad(\zeta\in D(D^{1/2})). \end{aligned}
 \tag{PR.41}
\]

Then \(C^{it}D^{-it}\) has a unique bounded, weak operator continuous extension \(F\) to \(-1/2\le\operatorname{Im}z\le0\), holomorphic inside, with

\[
 \begin{aligned} F(-i/2)&=B,\\ F(t-i/2)&=C^{it}BD^{-it}. \end{aligned}
 \tag{PR.42}
\]

It is sigma-weakly continuous there and norm holomorphic inside. Its norm is at most \(\max(1,\|B\|)\). If its real values belong to a von Neumann subalgebra, all its strip values belong to that subalgebra.

**Proof.** Test \(\xi\) in a spectral band \(1_{[1/n,n]}(D)K\), and \(\zeta\) in a spectral band \(1_{[1/m,m]}(C)K\subset PK\). The scalar function

\[
 f_{\xi,\zeta}(z)
 =\langle D^{-iz}\xi,C^{-i\bar z}\zeta\rangle
 \tag{PR.43}
\]

is entire, with the first-variable-linear convention. The conjugate argument in its second vector is essential. Spectral bands bound every real power needed on the finite-height strip; real-time powers are unitary on their respective supports. Thus this scalar function is bounded on the entire strip, not just on a compact rectangle.

Its real edge is the coefficient of \(C^{it}D^{-it}\). At the lower edge, self-adjointness and (PR.41) give

\[
 \begin{aligned}
 f_{\xi,\zeta}(t-i/2)
 &=\langle C^{1/2}D^{-it-1/2}\xi,C^{-it}\zeta\rangle\\
 &=\langle BD^{-it}\xi,C^{-it}\zeta\rangle.
 \end{aligned}
 \tag{PR.44}
\]

The first argument is in the required domain because it is a \(D\)-band vector. The two edge bounds are respectively \(\|\xi\|\|\zeta\|\) and \(\|B\|\|\xi\|\|\zeta\|\). MA-08's bounded-strip maximum principle gives the uniform bound \(\max(1,\|B\|)\|\xi\|\|\zeta\|\).

For \(\zeta\in(1-P)K\), set the scalar function to zero. Both edge formulas still hold, because \(PB=B\). The \(C\)-bands together with this kernel span a dense space; the \(D\)-bands are dense because \(D\) is injective. Riesz representation and the uniform bound extend these coefficients uniquely to bounded operators \(F(z)\) on all of \(K\). Density and the common bound give weak operator continuity on the closed strip, coefficient holomorphy inside, and precisely (PR.42), including the kernel tests.

CP-04–06 express each normal functional as a summable series of vector coefficients. The common bound gives uniform convergence of its finite partial sums throughout the strip. Their scalar holomorphy and continuity therefore pass to the normal test. This proves sigma-weak continuity and weak-star holomorphy. On a circle inside the strip, the scalar Cauchy coefficients define operators of norm at most \(Lr^{-j}\), where \(L\) bounds \(F\) and \(r\) is the circle radius. Their norm-convergent power series equals \(F\), since all vector tests agree. Thus \(F\) is norm holomorphic in the interior.

If a normal functional on \(B(K)\) annihilates the stipulated subalgebra, its scalar strip function vanishes on the real edge. MA-08's boundary uniqueness makes it vanish throughout. CP-05's annihilator identity then puts \(F(z)\) in that ultraweakly closed subalgebra. The same scalar uniqueness proves uniqueness of the extension. \(\square\)

### Identify the bounded endpoint on the full domain

Return to \(\varphi\le\sigma\). On \(x\xi_\sigma\), \(x\in N\), the ordinary and relative Tomita identities, \(J_e\)-fixedness of the two cone vectors, and \(A\in N\) give

\[
 \begin{aligned} C^{1/2}(x\xi_\sigma)&=J_ex^*\xi_\varphi\\ &=A J_ex^*\xi_\sigma\\ &=A D^{1/2}(x\xi_\sigma). \end{aligned}
 \tag{PR.45}
\]

The middle equality follows because \(A\) commutes with \(J_ex^*J_e\) and \(A\xi_\sigma=\xi_\varphi\). Approximate an arbitrary \(\zeta\in D(D^{1/2})\) by this ordinary Tomita graph core. Boundedness of \(A\) and closedness of \(C^{1/2}\) give membership in \(D(C^{1/2})\) and the identity on the whole domain. Thus (PR.41) holds with \(B=A\); its range condition is \(pA=A\).

The strip lemma applied to (PR.40) proves (PR.34), with norm at most one throughout the strip. In addition its lower edge is

\[
 F(t-i/2)
 =[D\varphi:D\sigma]_t\,\sigma_t^{\sigma|_N}(A).
 \tag{PR.46}
\]

This is an identity inside \(N\), not a modular action of a nonfaithful denominator on all of \(M\).

There is also an exact interpretation of the commonly written product:

\[
 \overline{C^{1/2}D^{-1/2}}=A.
 \tag{PR.47}
\]

Initially it is defined precisely on \(D(D^{-1/2})\). For \(v\) in this domain, \(\zeta=D^{-1/2}v\) belongs to \(D(D^{1/2})\) and \(D^{1/2}\zeta=v\); (PR.41) gives \(C^{1/2}D^{-1/2}v=Av\). The domain is dense, so its graph closure is the bounded operator \(A\) on all of \(K\). This proves the product and its domain statement rather than assigning a value to an undefined negative power.

Finally take \(\sigma=\varphi+\psi\). Apply the theorem to each summand. The factors \(A,B\) in PR-02–03 are respectively the two supported cocycle endpoints relative to this same denominator corner. Root addition is \(\sigma((A+B)^*x(A+B))\); the mixed pairing is \(\sigma(B^*A)\). The quotient, complexification and transport proofs in PR-04–06 therefore use exactly these endpoints. Both zero summands and a common null corner are included. No faithful bounded functional on the whole algebra was assumed.

### A supported noncommuting calculation

**Problem 4.** Embed PR-07's two-by-two projections \(p_0,q_0\) in the first two coordinates of \(M_3(\mathbb C)\), and give \(\sigma\) density \(r=(p_0+q_0)\oplus0\) and \(\varphi\) density \(h=p_0\oplus0\). Find the corner, the real cocycle and its endpoint. Check whether reversing the endpoint factors is valid.

**Solution.** The support of \(\sigma\) is \(e=\operatorname{diag}(1,1,0)\); its faithful algebra is the upper \(2\)-by-\(2\) corner. In the Hilbert–Schmidt form there, put \(s=p_0+q_0>0\). The relative and ordinary modular operators are respectively left multiplication by \(p_0\) followed by right multiplication by \(s^{-1}\), and left multiplication by \(s\) followed by right multiplication by \(s^{-1}\). Their supported imaginary powers give

\[
 \begin{aligned} {}[D\varphi:D\sigma]_t&=(p_0s^{-it})\oplus0,\\ A&=(p_0s^{-1/2})\oplus0. \end{aligned}
 \tag{PR.48}
\]

The finite-dimensional continuation is \(F(z)=(p_0s^{-iz})\oplus0\). It sends the root \(r^{1/2}\) to \(h^{1/2}=h\), has \(p_0\oplus0\) as its final support, and has real initial projection \((s^{it}p_0s^{-it})\oplus0\). At real zero its value is \(h\), while \(A\) is generally not self-adjoint. The third coordinate is zero at every parameter.

To test order reversal, write

\[
 \begin{aligned} s^{1/2}&=\begin{pmatrix}a&b\\b&c\end{pmatrix},\\ b&\ne0,\\ d&=ac-b^2>0. \end{aligned}
 \tag{PR.49}
\]

Here \(b\ne0\) follows because a diagonal square root would have diagonal square, whereas \(s\) has a nonzero off-diagonal entry. The reversed factor \(s^{-1/2}p_0\) sends the second coordinate of \(s^{1/2}\) to the nonzero column
\((bc/d,-b^2/d)^{\mathsf T}\). The desired root \(p_0\) has zero second column. Thus the reversed factor fails the defining vector identity. This calculation simultaneously checks the factor order, the zero ambient corner, and the genuinely nonfaithful numerator.

The added construction was independently written after consulting the complete relative-operator and supported-cocycle definitions and proofs in Fumio Hiai, [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383v1), Definition 12.1, Lemma 12.2, Proposition 12.3, Example 12.4, Lemma 12.9, Definition 12.10, Proposition 12.11 and Remark 12.12. The faithful completion, graph-core reduction and two-operator interpolation proof above supply the full endpoint argument at the exact linked programme inputs. No human source expression is imported or redistributed. This additional original exposition is by OpenAI Codex, October 2026, CC0-1.0. Independent review and transitive prerequisite closure remain separate.

## Act on every positive root

The root construction also remembers multiplication in \(M\). Fix any temporary standard form \((M,H,J,P)\), with the unitary \(U:L^2(M)\to H\) from PR-06. For \(x\in M\), put

\[
 \begin{aligned}
 j(x)&=JxJ,\\
 Q_x&=xj(x).
 \end{aligned}
 \tag{PR.50}
\]

The map \(j\) is conjugate-linear, multiplicative and star preserving. Indeed, \(J^2=I\) gives \(j(xy)=j(x)j(y)\), and antiunitarity gives \(j(x^*)=j(x)^*\). Its values belong to \(M'\), so every \(j(x)\) commutes with every left algebra element. The standard-form cone axiom says \(Q_xP\subset P\); it does not say that \(Q_x\) is a positive operator on all of \(H\).

For **every** \(\varphi\in M_*^+\), including a nonfaithful one, define a new functional by

\[
 (\alpha_x\varphi)(y)
   =\langle yQ_x\xi_\varphi,Q_x\xi_\varphi\rangle
       \quad(y\in M).
 \tag{PR.51}
\]

The normal vector-functional proof shows that this is bounded, positive and normal. Its norm satisfies

\[
 \begin{aligned}
 \|\alpha_x\varphi\|&=\|Q_x\xi_\varphi\|^2\\
   &\le\|x\|^4\varphi(1).
 \end{aligned}
 \tag{PR.52}
\]

Cone invariance and uniqueness of positive representatives give the exact vector identity

\[
 \xi_{\alpha_x\varphi}=Q_x\xi_\varphi.
 \tag{PR.53}
\]

Linearity in (PR.51) concerns the variable \(y\). No additivity of \(\alpha_x\) in the ordinary sum of functionals is needed here.

The prescription on formal positive roots,

\[
 \rho(x)\sqrt{\varphi}:=\sqrt{\alpha_x\varphi},
 \tag{PR.54}
\]

extends to exactly one bounded **complex-linear operator** on \(L^2(M)\). To prove extension, rather than assume relations between formal roots are respected, define

\[
 \begin{aligned}
 \rho(x)&=U^{-1}Q_xU,\\
 \|\rho(x)\|&\le\|x\|^2.
 \end{aligned}
 \tag{PR.55}
\]

Equations (PR.53–54) identify its action on roots. Differences and complex combinations of roots span the entire space by PR-05–06, so a linear operator with that action is unique. This also proves that root addition, positive scaling and every difference relation are respected.

The action is independent of the temporary form. Its unique comparison \(V:H_1\to H_2\), proved in Patching the unique comparisons, satisfies \(Vx_1=x_2V\), \(VJ_1=J_2V\) and \(V\xi_\varphi^{(1)}=\xi_\varphi^{(2)}\). Thus \(VQ_x^{(1)}=Q_x^{(2)}V\). Since \(VU_1=U_2\), the operators in (PR.55) coincide on the canonical root space, and (PR.51) defines the same functional in both coordinates. This proof assumes neither a faithful normal state on \(M\) nor countable decomposability.

## Multiply the root actions and compute their norm

For \(x,y\in M\), commutation of the two algebra actions gives

\[
 \begin{aligned}
 Q_xQ_y
   &=xj(x)yj(y)=xyj(xy)=Q_{xy},\\
 Q_{x^*}&=Q_x^*,\qquad Q_1=I.
 \end{aligned}
 \tag{PR.56}
\]

Transporting through \(U\) proves

\[
 \begin{aligned}
 \rho(xy)&=\rho(x)\rho(y),\\
 \rho(x^*)&=\rho(x)^*,\qquad \rho(1)=I.
 \end{aligned}
 \tag{PR.57}
\]

In particular \(\alpha_x(\alpha_y\varphi)=\alpha_{xy}\varphi\), by the equality of their cone vectors in (PR.53). For a complex scalar \(c\), however,

\[
 \rho(cx)=|c|^2\rho(x).
 \tag{PR.58}
\]

The operator \(\rho(x)\) is complex linear on its Hilbert-space argument; the function \(x\mapsto\rho(x)\) is quadratic, and is not an algebra representation.

In fact the norm bound in (PR.55) is exact:

\[
 \|\rho(x)\|=\|x\|^2.
 \tag{PR.59}
\]

If \(x=0\), both sides vanish. Otherwise write \(a=x^*x\), and fix \(0<r<\|a\|\). The spectral projection \(p=\mathbf1_{(r,\infty)}(a)\) is nonzero: if it vanished, spectral calculus would give \(a\le rI\), contradicting \(r<\|a\|\). The corner detection proof gives \(K_p=pJpJH\ne\{0\}\). This subspace reduces both commuting positive operators \(a\) and \(j(a)\). Their restrictions to it satisfy \(a\ge rI\) and \(j(a)\ge rI\), because \(p\) and \(j(p)\) are their respective spectral projections.

On \(K_p\), positivity and commutation now give

\[
 a\,j(a)-r^2I=(a-rI)j(a)+r(j(a)-rI)\ge0.
\]

Here the first product is positive: its factors commute, and it is the square-root sandwich of the first factor by \(j(a)^{1/2}\). For a unit vector \(v\in K_p\),

\[
 \|Q_xv\|^2
   =\langle a\,j(a)v,v\rangle\ge r^2,
 \qquad Q_x^*Q_x=a\,j(a).
 \tag{PR.60}
\]

Thus \(\|Q_x\|\ge r\). Letting \(r\uparrow\|a\|=\|x\|^2\) and using (PR.55) proves (PR.59). The argument uses one nonzero spectral corner at a time and imposes no cardinality restriction.

## Differentiate the cone action

For real \(t\) and arbitrary \(x\in M\), the norm-convergent exponential series gives

\[
 \begin{aligned}
 j(e^{tx})&=e^{t j(x)},\\
 Q_{e^{tx}}&=e^{tx}e^{t j(x)}
               =e^{t(x+j(x))}.
 \end{aligned}
 \tag{PR.61}
\]

The last identity follows by multiplying absolutely convergent series: commutation permits the binomial formula for each coefficient. Real \(t\) matters in the first identity because \(j\) conjugates scalars.

Define

\[
 D_x=U^{-1}(x+j(x))U.
 \tag{PR.62}
\]

Equations (PR.55) and (PR.61) give

\[
 \rho(e^{tx})=e^{tD_x},\qquad
 e^{(s+t)D_x}=e^{sD_x}e^{tD_x}
        \quad(s,t\in\mathbb R).
 \tag{PR.63}
\]

The inverse is \(e^{-tD_x}\), so this is a group even when \(x\) is neither self-adjoint nor skew-adjoint. The exponential series converges uniformly on bounded real intervals, proving operator-norm continuity. Its remainder estimate

\[
 \|e^{tD_x}-I-tD_x\|
   \le \frac{t^2}{2}\|D_x\|^2 e^{|t|\|D_x\|}
 \tag{PR.64}
\]

follows by bounding the terms of degree at least two and using \(n!\ge2(n-2)!\). Consequently the operator-norm derivative exists and is

\[
 \delta(x):=\left.\frac{d}{dt}\rho(e^{tx})\right|_{t=0}
       =D_x,\qquad \|\delta(x)\|\le2\|x\|.
 \tag{PR.65}
\]

Additivity and homogeneity for real scalars follow from those properties of \(j\). This is real linearity; generally \(\delta(ix)\ne i\delta(x)\).

It is a real Lie algebra homomorphism. For \([x,y]=xy-yx\), both mixed commutators vanish because the left and right algebras commute, while multiplicativity of \(j\) gives

\[
 \begin{aligned}
 [x+j(x),y+j(y)]
   &=[x,y]+[j(x),j(y)]\\
   &=[x,y]+j([x,y]).
 \end{aligned}
 \tag{PR.66}
\]

Unitary transport yields

\[
 {}[\delta(x),\delta(y)]=\delta([x,y]).
 \tag{PR.67}
\]

There is no assertion that this real Lie homomorphism is injective: in a nonzero unital algebra, \(\delta(i1)=0\).

## Recover the left and right representations

The complex polarization of the real derivative separates the two commuting actions. Since \(j(ix)=-ij(x)\), (PR.62–65) give

\[
 \begin{aligned}
 \delta(x)&=U^{-1}(x+j(x))U,\\
 \delta(ix)&=U^{-1}(ix-ij(x))U.
 \end{aligned}
 \tag{PR.68}
\]

Therefore define

\[
 \begin{aligned}
 \pi(x)&=\frac{\delta(x)-i\delta(ix)}{2}\\
          &=U^{-1}xU,\\
 \pi'(x)&=\frac{\delta(x^*)+i\delta(ix^*)}{2}\\
          &=U^{-1}Jx^*JU.
 \end{aligned}
 \tag{PR.69}
\]

The factor \(1/2\) in **both** formulas is necessary. Without it the putative left action is \(2U^{-1}xU\); at the identity it is \(2I\), and multiplicativity fails in every nonzero unital algebra.

The first map is the faithful normal unital star representation already identified in PR-06. The second is complex linear because adjunction and \(j\) are each conjugate linear. Explicit multiplication gives

\[
 \begin{aligned}
 \pi'(xy)&=\pi'(y)\pi'(x),\\
 \pi'(x^*)&=\pi'(x)^*,\qquad \pi'(1)=I.
 \end{aligned}
 \tag{PR.70}
\]

Thus it is a unital star antirepresentation. It is faithful because \(Jx^*J=0\) implies \(x=0\).

Its normality also follows from actual predual tests. In the temporary coordinates, first-variable linearity and antiunitarity give

\[
 \langle Jx^*Jv,w\rangle
    =\langle xJw,Jv\rangle.
 \tag{PR.71}
\]

For square-summable vector sequences \((v_n),(w_n)\), the corresponding series on the right is a normal functional of \(x\), since \((Jw_n),(Jv_n)\) remain square summable. The complete vector-series characterization therefore proves ultraweak continuity of \(x\mapsto Jx^*J\), and unitary transport proves normality of \(\pi'\). This argument concerns arbitrary ultraweak tests, not only bounded nets of single-vector coefficients.

Finally \(UJ_M=JU\) and the commutant axiom give

\[
 \begin{aligned}
 J_M\pi(x)^*J_M&=\pi'(x),\\
 \pi(M)'&=\pi'(M).
 \end{aligned}
 \tag{PR.72}
\]

The cone, conjugation and left representation are those of PR-06, so \((\pi(M),L^2(M),J_M,L^2(M)_+)\) is its canonical standard form. All these operators have been recovered from the action on roots and its real derivative.

For a normal star isomorphism \(\theta:M\to N\), let \(W:L^2(M)\to L^2(N)\) be the root-transport unitary of (PR.25). The standard-form comparison intertwines \(Q_x\), hence

\[
 \begin{aligned}
 W\rho_M(x)&=\rho_N(\theta(x))W,\\
 W\delta_M(x)&=\delta_N(\theta(x))W.
 \end{aligned}
 \tag{PR.73}
\]

Differentiation of the first identity is justified by the operator-norm derivative just proved. Applying (PR.69) gives the analogous identities for both representations; \(\theta\) preserves \(i\) and adjoints. Composition and inversion follow from the uniqueness in PR-06. The zero algebra is covered as well: its Hilbert space and all operators are zero, including its identity operator.

## A scalar modular strip for faithful functionals

There is a useful analytic description of (PR.51) when \(\varphi\) is **faithful and bounded normal on \(M\)**. Write \(\xi=\xi_\varphi\). It is cyclic and separating, and The corner seen by a positive vector identifies the modular conjugation of this finite GNS form with \(J\). Let \(\Delta\) be its injective positive modular operator. The modular fundamental theorem gives

\[
 \begin{aligned}
 \sigma_t^\varphi(b)&=\Delta^{it}b\Delta^{-it},\\
 \Delta^{it}\xi&=\xi
       \quad(t\in\mathbb R,\ b\in M).
 \end{aligned}
 \tag{PR.74}
\]

For \(x,y\in M\), the real orbit that represents the cone action is

\[
 \begin{aligned}
 f_{x,y}^\varphi(t)
   &=\varphi\bigl(\sigma_{-t}^\varphi(x)\\
   &\qquad x^*yx\,\sigma_t^\varphi(x^*)\bigr).
 \end{aligned}
 \tag{PR.75}
\]

The adjoint in the **last** factor is essential. No analyticity of \(x\) or \(y\) as algebra elements is assumed.

We prove that (PR.75) has a unique bounded continuous extension to

\[
 S=\{z:-1/2\le\operatorname{Im}z\le0\},
\]

holomorphic in its interior, with endpoint

\[
 f_{x,y}^\varphi(-i/2)
     =(\alpha_x\varphi)(y).
 \tag{PR.76}
\]

Put \(a=x^*\xi\) and \(T=x^*yx\). Since \(\varphi\) is finite, all of \(M\) belongs to its finite-star algebra. The closed Tomita operator extends \(b\xi\mapsto b^*\xi\); with \(S_\varphi=J\Delta^{1/2}\), this gives

\[
 a\in D(\Delta^{1/2}),\qquad
 \Delta^{1/2}a=Jx\xi.
 \tag{PR.77}
\]

For \(z=t-iu\), \(0\le u\le1/2\), define

\[
 F(z)=\langle T\Delta^{iz}a,
                    \Delta^{-i\overline z}a\rangle.
 \tag{PR.78}
\]

Both vectors use the **positive** spectral power \(\Delta^u\): their real-time factors are \(\Delta^{it}\) and \(\Delta^{-it}\), respectively. The second exponent is \(-i\overline z\). Replacing it by \(i\overline z\) would demand negative powers not supplied by (PR.77).

Here are the domain and continuity details. If \(\mu_a\) is the scalar spectral measure of \(a\), then

\[
 \lambda^{2u}\le1+\lambda
       \quad(\lambda>0,\ 0\le u\le1/2).
\]

The right side is integrable by (PR.77). Thus both vectors in (PR.78) are defined on the whole closed strip and have squared norm at most
\(\|a\|^2+\|\Delta^{1/2}a\|^2\). For the bands \(E_n=\mathbf1_{[1/n,n]}(\Delta)\), the uniform tail estimate is

\[
 \sup_{z\in S}
    \|\Delta^{iz}(I-E_n)a\|^2
 \le
 \int_{(0,\infty)\setminus[1/n,n]}
       (1+\lambda)\,d\mu_a(\lambda)\longrightarrow0.
 \tag{PR.79}
\]

The identical estimate holds for \(\Delta^{-i\overline z}(I-E_n)a\). On \(E_nH\), the logarithm \(B_n=\log(\Delta|_{E_nH})\) is bounded. Its exponential series proves that the first band vector is holomorphic, the second antiholomorphic, and both are continuous up to each edge. Uniform convergence gives continuity and boundedness of the full vectors, as in the complete spectral-strip proof.

For clarity about scalar holomorphy with our inner-product convention, set \(A_n(z)=e^{izB_n}E_n\), regarded as a bounded operator on all of \(H\). Then \(A_n(-\overline z)^*=A_n(z)\), so

\[
 \langle T A_n(z)a,A_n(-\overline z)a\rangle
    =\langle A_n(z)T A_n(z)a,a\rangle.
 \tag{PR.80}
\]

This is an entire scalar function of \(z\), by the bounded exponential series and first-variable linearity. The two uniform tail estimates and the uniform vector bounds make these scalar functions converge uniformly to \(F\) on \(S\). The locally uniform limit argument makes \(F\) holomorphic in the interior. In particular

\[
 |F(z)|
   \le \|T\|\bigl(\|a\|^2+\|\Delta^{1/2}a\|^2\bigr)
   \le2\|x\|^4\|y\|\varphi(1).
 \tag{PR.81}
\]

For real \(t\), (PR.74) gives \(\Delta^{it}a=\sigma_t^\varphi(x^*)\xi\) and \(\Delta^{-it}a=\sigma_{-t}^\varphi(x^*)\xi\). Move the adjoint of the second left multiplier into the first inner-product variable to obtain

\[
 F(t)
   =\langle \sigma_{-t}^\varphi(x)
           T\sigma_t^\varphi(x^*)\xi,\xi\rangle
   =f_{x,y}^\varphi(t).
 \tag{PR.82}
\]

At \(z=-i/2\), both vectors are \(\Delta^{1/2}a=Jx\xi\), hence

\[
 \begin{aligned}
 F(-i/2)
   &=\langle x^*yx\,Jx\xi,Jx\xi\rangle\\
   &=\langle yQ_x\xi,Q_x\xi\rangle
     =(\alpha_x\varphi)(y).
 \end{aligned}
 \tag{PR.83}
\]

The closed-strip boundary-uniqueness proof supplies uniqueness. This proves the entire scalar-strip assertion at its stated hypotheses, including the bounded normal positive functional at the endpoint.

For a nonfaithful \(\varphi\), its modular automorphism group is canonically defined on \(eMe\), \(e=s(\varphi)\), where the restricted functional is faithful. Consequently (PR.75–83) apply there to \(x,y\in eMe\), with the corner standard form of SE-03 and its cyclic GNS identification in SE-06. They do not supply a modular orbit on all of \(M\) for arbitrary \(x\). The global definition (PR.51–55), and every algebra-action and representation result above, still applies to all \(x\in M\) and all positive normal \(\varphi\). No unchosen faithful extension of \(\varphi\) is part of that construction.

## Problems on actions and normalization

**1. Test the adjoint and the factor one half in the scalar algebra.** Take \(M=\mathbb C\), \(H=\mathbb C\), \(Jz=\overline z\), \(P=[0,\infty)\), and \(\varphi(z)=z\). Compute the orbit for \(x=i,y=1\) with and without the last adjoint, and compute the polarized left action.

**Solution.** Modular time is trivial. Without the last adjoint, the scalar product inside the functional is

\[
 i(-i)\cdot1\cdot i\cdot i=-1.
\]

It cannot be the value at \(1\) of a positive functional. With the final factor \(x^*=-i\), the product is \(1\), agreeing with \(Q_i=1\) and \((\alpha_i\varphi)(1)=1\).

Here \(Q_x=|x|^2I\), so \(\rho(e^{tx})=e^{2t\operatorname{Re}x}I\) and \(\delta(x)=2\operatorname{Re}x\,I\). In particular \(\delta(1)=2I\) and \(\delta(i)=0\). The unhalved formula would give \(2I\) at \(1\), whose square is \(4I\); it is neither unital nor multiplicative. Formula (PR.69) gives \(\pi(x)=xI\) and \(\pi'(x)=xI\), as required.

**2. Compute the action on a nonfaithful matrix functional.** In the Hilbert–Schmidt standard form of \(M=M_2(\mathbb C)\), let

\[
 h=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad x=\begin{pmatrix}1&1\\1&0\end{pmatrix},
 \qquad \varphi_h(y)=\operatorname{Tr}(hy).
\]

Find the density of \(\alpha_x\varphi_h\), and identify both recovered representations.

**Solution.** Here \(\xi_{\varphi_h}=h^{1/2}=h\), \(Jv=v^*\), and \(j(x)v=vx^*\). Therefore

\[
 Q_xh=xhx^*
    =\begin{pmatrix}1&1\\1&1\end{pmatrix}=b.
\]

For a positive matrix \(b\), its vector functional is
\(\langle yb,b\rangle=\operatorname{Tr}(b\,yb)=\operatorname{Tr}(b^2y)\), by cyclicity of the finite trace. Thus the density is

\[
 b^2=\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

It remains positive and has rank one. On an arbitrary Hilbert–Schmidt matrix \(v\), the derivative is \(\delta(x)v=xv+vx^*\), while \(\delta(ix)v=ixv-ivx^*\). Equations (PR.69) give \(\pi(x)v=xv\) and \(\pi'(x)v=vx\). The latter reverses products because right multiplication by \(y\), followed by right multiplication by \(x\), is right multiplication by \(yx\). This calculation needs no modular automorphism group for \(\varphi_h\) on all of \(M_2\).

**3. Why is a faithful corner insufficient for arbitrary matrix elements?** Keep \(h\) from Problem2 and set \(e=h\). Explain why the corner modular formula cannot simply be used for the off-diagonal \(x\) in that problem.

**Solution.** The corner algebra \(eM_2e\) is one dimensional and the restricted functional is faithful there, so its modular group is the identity on that corner. The displayed \(x\) is not in \(eM_2e\); the corner group has no value at \(x\). One can choose a faithful density on the complementary corner and obtain a different functional on \(M_2\), but that is auxiliary data rather than the original functional's all-algebra modular group. Formula (PR.51) already yields its canonical action without such a choice.

**4. Recover the full noncommuting strip endpoint.** Let \(h=\operatorname{diag}(1,4)\), \(\varphi_h(y)=\operatorname{Tr}(hy)\), and \(x=\begin{pmatrix}1&1\\0&1\end{pmatrix}\). Compute the endpoint vector and density. Then obtain the same vector from the half-power domain proof.

**Solution.** Now \(h\) is invertible and \(h^{1/2}=\operatorname{diag}(1,2)\). Left modular time is \(\sigma_t^{\varphi_h}(y)=h^{it}yh^{-it}\). In Hilbert–Schmidt coordinates,

\[
 \begin{aligned}
 \Delta v&=hvh^{-1},\qquad
 a=x^*h^{1/2},\\
 \Delta^{1/2}a&=h^{1/2}x^*=J(xh^{1/2}).
 \end{aligned}
 \tag{PR.84}
\]

Multiplying the last vector by \(x\) gives

\[
 \begin{aligned}
 Q_x\xi_{\varphi_h}
   &=xh^{1/2}x^*
       =\begin{pmatrix}3&2\\2&2\end{pmatrix}=b,\\
 b^2&=\begin{pmatrix}13&10\\10&8\end{pmatrix}.
 \end{aligned}
 \tag{PR.85}
\]

Thus \(F(-i/2)(y)=\operatorname{Tr}(b^2y)\), and \(F(-i/2)(1)=21\). The density differs from the ordinary compressed density \(xhx^*=\begin{pmatrix}5&4\\4&4\end{pmatrix}\); positive-root action is defined by conjugating \(h^{1/2}\) and then squaring it. Equations (PR.78–83) prove the same endpoint without assigning analytic modular time to an arbitrary bounded algebra element.

The standard-form axioms and the Hilbert–Schmidt comparison used here can be read in Fumio Hiai's freely accessible [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383v1), Section3.1, Definition3.5, Example3.6 and Proposition3.7. Section2.1 supplies the cyclic Tomita setup and half-power convention. Hiai's Hilbert-space convention is linear in the second variable; every calculation above uses the first-variable-linear convention fixed at the start of this lesson. The full arbitrary-standard-form comparison and corner proofs used above are the exact existing in-course SE proofs. The cone-action, real derivative, half-normalized reconstruction, scalar-strip derivation and these solutions are independently written; no human source expression is imported.

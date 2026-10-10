# Characteristic classes and the Weil homomorphism

Curvature takes values in a Lie algebra. An invariant polynomial turns it into an ordinary closed differential form, whose cohomology class does not depend on the connection. We first prove this assertion for arbitrary finite-dimensional Lie groups. We then determine the classical invariant polynomials, identify their integral normalizations, and compute the resulting forms on lines, real planes and tangent bundles.

*Self-checked by the writing AI. New exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0.*

All manifolds are finite dimensional, Hausdorff, second countable and smooth. Connections, bundles and maps are smooth. The group need not be compact or connected. Real de Rham cohomology is the cohomology of the complex of real differential forms; complex coefficients mean its complexification. Whenever an integral class is compared to a form, the comparison is the integration isomorphism proved in DG-CHAR-17 I.2, with its relative version I.5. The integral Chern and Euler classes themselves are constructed in [DG-CHAR-09 B.2](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-09.md#theorem-b-2) and [DG-CHAR-06 T.3–T.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#theorem-t-3).

In a column frame \(e\), write \(\nabla(ev)=e(dv+Av)\). Our curvature is \(F=dA+A\wedge A\). For an abstract Lie group it is \(F=dA+\tfrac12[A,A]\), with the coefficient bracket and signs proved in [Curvature and holonomy A.1](curvature-and-holonomy-groups.md#lemma-a-1). In this convention the total Chern form is \(\det(I+iF/(2\pi))\).

## A. From invariant polynomials to global forms

For a finite-dimensional real Lie algebra \(\mathfrak g\), let \(I^k(G)\) be the real homogeneous polynomials of degree \(k\) on \(\mathfrak g\) satisfying \(p(\operatorname{Ad}(g)X)=p(X)\) for every \(g\in G\). Set \(I(G)=\bigoplus_{k\geq0}I^k(G)\), and assign degree \(2k\) to \(I^k(G)\). Complex-valued polynomials and forms are treated by the same definitions over \(\mathbb C\).

**Lemma A.1 (polarization and invariant contraction).** A homogeneous polynomial \(p\) of degree \(k>0\) has a unique symmetric \(k\)-linear polarization, denoted by the same letter, with \(p(X,\ldots,X)=p(X)\). It is

\[
p(X_1,\ldots,X_k)=\frac1{k!}
\left.\frac{\partial^k}{\partial t_1\cdots\partial t_k}
p\!\left(\sum_{j=1}^k t_jX_j\right)\right|_{t=0}.
\tag{A.1}
\]

If \(p\in I^k(G)\), this polarization is invariant in all its arguments simultaneously and satisfies

\[
\sum_{j=1}^k p(X_1,\ldots,[Z,X_j],\ldots,X_k)=0.
\tag{A.2}
\]

For \(\mathfrak g\)-valued forms \(\alpha_j=\sum_a\alpha_j^a e_a\), of degrees \(d_j\), define

\[
p(\alpha_1,\ldots,\alpha_k)
=\sum_{a_1,\ldots,a_k}p(e_{a_1},\ldots,e_{a_k})
\alpha_1^{a_1}\wedge\cdots\wedge\alpha_k^{a_k}.
\tag{A.3}
\]

This is basis independent. Interchanging adjacent arguments of degrees \(d_i,d_{i+1}\) multiplies it by \((-1)^{d_id_{i+1}}\). For \(D_A\alpha=d\alpha+[A,\alpha]\), where \(A\) is a \(\mathfrak g\)-valued one-form,

\[
d\,p(\alpha_1,\ldots,\alpha_k)=
\sum_j(-1)^{d_1+\cdots+d_{j-1}}
p(\alpha_1,\ldots,D_A\alpha_j,\ldots,\alpha_k).
\tag{A.4}
\]

**Proof.** Expand \(p\) in coordinate monomials. The coefficient of \(t_1\cdots t_k\) is multilinear in the \(X_j\) and unchanged by permuting them. When all \(X_j=X\), this coefficient is \(k!p(X)\), because it is the corresponding coefficient of \((t_1+\cdots+t_k)^kp(X)\). Conversely, substituting \(\sum t_jX_j\) in the diagonal of a symmetric multilinear form recovers \(k!\) times that form as this coefficient. This proves existence, the formula and uniqueness. Applying uniqueness to \(p(\operatorname{Ad}(g)\,\cdot\,)\) proves simultaneous invariance. Differentiate it at \(g=\exp(tZ)\). [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3) identifies the derivative of the adjoint action with \([Z,\,\cdot\,]\), giving (A.2).

In (A.3), replacing a basis by another multiplies its coefficients by the inverse change-of-basis matrix and its basis vectors by the matrix itself. Multilinearity cancels those matrices in every index. Symmetry of \(p\) and graded commutativity of the scalar wedge product give the stated interchange sign. The scalar exterior product rule, proved in DG-CHAR-17 D.1, gives (A.4) with \(d\alpha_j\) in place of \(D_A\alpha_j\). To examine the extra terms, expand into \(A=aZ\) and \(\alpha_j=b_jX_j\) with constant Lie algebra elements. In the \(j\)-th term, moving the one-form \(a\) to the front crosses \(d_1+\cdots+d_{j-1}\) degrees, cancelling the prefactor. The remaining sum is \(a\wedge b_1\wedge\cdots\wedge b_k\) times (A.2), hence zero. Add the finitely many coordinate terms to obtain (A.4). For \(k=0\) the construction is the constant polynomial itself and its derivative is zero. □

**Theorem A.2 (the Weil homomorphism).** Let \(P\to M\) be a principal \(G\)-bundle with connection \(\omega\) and curvature \(\Omega\). For \(p\in I^k(G)\), the form \(p(\Omega,\ldots,\Omega)\) is the pullback of a unique closed form \(p(F)\) on \(M\). Its class is independent of the connection. The resulting map

\[
W_P:I(G)\longrightarrow H^{\mathrm{even}}_{\mathrm{dR}}(M;\mathbb R),
\qquad p\longmapsto[p(F)]
\tag{A.5}
\]

is a unital homomorphism of graded algebras and is natural under smooth pullback.

**Proof.** [Curvature and holonomy A.4](curvature-and-holonomy-groups.md#theorem-a-4) proves that \(\Omega\) is horizontal and transforms by \(\operatorname{Ad}(g^{-1})\) under the right action. Thus its contraction by the invariant multilinear form is horizontal and invariant. The descent argument in [Curvature and holonomy A.5](curvature-and-holonomy-groups.md#theorem-a-5), applied to the trivial one-dimensional representation, gives the unique base form. Equivalently, the local forms \(p(F_s)\) agree on overlaps because \(F_{sg}=\operatorname{Ad}(g^{-1})F_s\), as proved in A.7 of that chapter. These arguments use invariance under every component of \(G\).

Apply (A.4) with all entries \(F_s\). Bianchi, [Curvature and holonomy A.6](curvature-and-holonomy-groups.md#theorem-a-6), says \(D_AF_s=0\), so \(dp(F_s)=0\). Closedness is local and hence holds globally. The calculation of A.3 below gives a global primitive for the difference between two connection forms; its proof uses only A.1 and the preceding descent argument and therefore proves independence without a circular assumption.

In local coordinates of \(\mathfrak g\), the entries of \(F_s\) are two-forms and commute. Evaluation at these entries is therefore an algebra homomorphism from the ordinary polynomial algebra to the even forms. It sends \(1\) to the constant function \(1\) and gives \((pq)(F_s)=p(F_s)\wedge q(F_s)\). Polarization (A.1) identifies this evaluation with (A.3) on repeated entries. Descent and passage to cohomology give the algebra and degree assertions. Pullback preserves curvature by [Curvature and holonomy A.7](curvature-and-holonomy-groups.md#theorem-a-7) and commutes with scalar wedges. Hence \(p(F_{f^*P})=f^*p(F_P)\), proving naturality on forms and on classes. Connections exist by [Connections and parallel transport B.1](connections-and-parallel-transport.md#theorem-b-1), so (A.5) is defined for every bundle under the stated manifold assumptions. □

**Theorem A.3 (global transgression).** For two connections \(\omega_0,\omega_1\), put \(\alpha=\omega_1-\omega_0\), \(\omega_t=\omega_0+t\alpha\), and let \(\Omega_t\) be the curvature. For \(p\in I^k(G)\), \(k\geq1\), the horizontal invariant form

\[
T_p(\omega_0,\omega_1)
=k\int_0^1p(\alpha,\Omega_t,\ldots,\Omega_t)\,dt
\tag{A.6}
\]

descends to \(M\) and satisfies

\[
p(F_1)-p(F_0)=dT_p(\omega_0,\omega_1).
\tag{A.7}
\]

**Proof.** [Connections and parallel transport A.4](connections-and-parallel-transport.md#theorem-a-4) proves that \(\alpha\) is horizontal and adjoint-equivariant and that every \(\omega_t\) is a connection. Expansion of the curvature, using the bracket of [Curvature and holonomy A.1](curvature-and-holonomy-groups.md#lemma-a-1), gives

\[
\Omega_t=\Omega_0+tD_0\alpha+\frac{t^2}{2}[\alpha,\alpha],
\qquad \partial_t\Omega_t=D_t\alpha.
\tag{A.8}
\]

Here the mixed brackets in the first formula are equal because both entries have degree one. Differentiating (A.3), all \(k\) curvature entries give the same contribution: they have even degree. Consequently

\[
\partial_t p(\Omega_t,\ldots,\Omega_t)
=k\,p(D_t\alpha,\Omega_t,\ldots,\Omega_t)
=k\,d\,p(\alpha,\Omega_t,\ldots,\Omega_t).
\tag{A.9}
\]

The last equality is (A.4); its other terms vanish by Bianchi, [Curvature and holonomy A.6](curvature-and-holonomy-groups.md#theorem-a-6). Horizontality and full equivariance of \(\alpha,\Omega_t\) prove that each integrand descends by [Curvature and holonomy A.5](curvature-and-holonomy-groups.md#theorem-a-5). All its coefficients are polynomials in \(t\), by (A.8), so integration and exterior differentiation commute by integrating finitely many powers of \(t\). The fundamental theorem of calculus of [Local tools 0.3](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) now gives (A.7). For degree zero the two forms coincide. □

**Proposition A.4 (change of structure group and disconnected groups).** Let \(\rho:G\to H\) be a smooth group homomorphism, \(r=d\rho_e\), and \(P_H=P\times_GH\), with \(G\) acting on \(H\) by left multiplication through \(\rho\). Then

\[
W_{P_H}(q)=W_P(q\circ r)\qquad(q\in I(H)).
\tag{A.10}
\]

Infinitesimal invariance alone does not suffice for descent when \(G\) is disconnected.

**Proof.** In the principal charts for \(P\), use the transition functions \(\rho(g_{ij})\) to construct \(P_H\), by the gluing proof of [Principal bundles A.1](principal-bundles-and-associated-bundles.md#theorem-a-1). The local potentials \(r(A_i)\) satisfy its connection gluing law: the derivative of a homomorphism takes the left Maurer form to the left Maurer form, since differentiating \(\rho(ga)=\rho(g)\rho(a)\) and translating to the identity gives that identity on every tangent vector. It also intertwines adjoint actions, by differentiating \(\rho(gag^{-1})=\rho(g)\rho(a)\rho(g)^{-1}\). Thus [Connections and parallel transport A.3](connections-and-parallel-transport.md#theorem-a-3) glues the potentials to a connection. The bracket preservation proved in [Curvature and holonomy A.3](curvature-and-holonomy-groups.md#lemma-a-3) gives its curvature \(r(F_i)\). The adjoint intertwining proves \(q\circ r\in I(G)\), and evaluating the local polynomials proves (A.10) before passing to classes.

For the last assertion write \(J(t)=\begin{pmatrix}0&t\\-t&0\end{pmatrix}\) in \(\mathfrak o(2)\). This Lie algebra is abelian, so \(p(J(t))=t\) satisfies (A.2). Conjugation by \(\operatorname{diag}(1,-1)\in O(2)\) sends \(J(t)\) to \(J(-t)\) and changes \(p\)'s sign. It is consequently not an \(O(2)\)-invariant polynomial. Indeed, on a trivial \(O(2)\)-bundle over \(\mathbb R^2\), the potential \(J(1)x\,dy\) has curvature \(J(1)\,dx\wedge dy\). The reflected section gives its negative scalar contraction. Those two local descriptions cannot be the same base form. For \(SO(2)\) the polynomial is invariant and does descend. □

**Example A.5 (trace-square and the local Chern–Simons expression).** For matrix connections and \(p(X)=\operatorname{tr}(X^2)\), the global difference form is

\[
T_p(A_0,A_1)=2\operatorname{tr}(\alpha\wedge F_0)
+\operatorname{tr}(\alpha\wedge D_0\alpha)
+\frac23\operatorname{tr}(\alpha\wedge\alpha\wedge\alpha).
\tag{A.11}
\]

On a globally trivialized bundle with \(A_0=0\), this becomes

\[
\operatorname{tr}\!\left(A\wedge dA+\frac23 A\wedge A\wedge A\right),
\qquad dT_p=\operatorname{tr}(F\wedge F).
\tag{A.12}
\]

**Proof.** The polarization is \(\tfrac12\operatorname{tr}(XY+YX)=\operatorname{tr}(XY)\), by summing matrix indices. For matrix forms the same summation gives \(\operatorname{tr}(B\wedge C)=(-1)^{bc}\operatorname{tr}(C\wedge B)\) in degrees \(b,c\). The matrix curvature in (A.8) is \(F_t=F_0+tD_0\alpha+t^2\alpha\wedge\alpha\). Substitute it into \(2\int_0^1\operatorname{tr}(\alpha\wedge F_t)\,dt\); integrating \(1,t,t^2\) proves (A.11). Taking \(A_0=0\) gives (A.12), with its exterior derivative given by A.3. For arbitrary bundles it is the difference of connections \(\alpha\), and the curvatures along their affine segment, that make (A.11) global. A potential \(A\) in one chosen frame has an inhomogeneous change-of-frame law, so (A.12) by itself is only a local expression unless that trivialization is global. □

## B. The polynomials for the classical groups

Write \(\sigma_j(X)\) for the coefficient of \(s^j\) in \(\det(I+sX)\). All polynomial degrees in this part are ordinary polynomial degrees; the associated differential forms have twice those degrees.

**Lemma B.1 (symmetric polynomials over any commutative ring).** For any commutative ring \(R\) with identity,

\[
R[t_1,\ldots,t_r]^{S_r}=R[e_1,\ldots,e_r],
\tag{B.1}
\]

where \(e_j\) is the \(j\)-th elementary symmetric polynomial. The substitution homomorphism \(R[z_1,\ldots,z_r]\to R[t_1,\ldots,t_r]\), \(z_j\mapsto e_j\), is injective.

**Proof.** It suffices to handle a symmetric homogeneous polynomial, since each homogeneous part is symmetric. Order exponent vectors lexicographically, starting with the exponent of \(t_1\). If \(a=(a_1,\ldots,a_r)\) is the largest exponent with nonzero coefficient \(c\), then \(a_1\geq\cdots\geq a_r\). Otherwise transposing a pair with \(a_i<a_j\), \(i<j\), gives a lexicographically larger monomial with the same nonzero coefficient, by symmetry. The polynomial

\[
e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots e_{r-1}^{a_{r-1}-a_r}e_r^{a_r}
\tag{B.2}
\]

has leading monomial \(t_1^{a_1}\cdots t_r^{a_r}\) with coefficient \(1\): the leading monomial of \(e_j\) is \(t_1\cdots t_j\), and lexicographic order is preserved on multiplying monomials. Subtract \(c\) times (B.2). The degree is unchanged and the largest exponent decreases. There are only finitely many monomials of that total degree, so this process terminates, proving generation without division in \(R\).

For independence, distinct monomials \(z_1^{b_1}\cdots z_r^{b_r}\) give distinct leading exponents \(a_i=\sum_{j\geq i}b_j\). In a nonzero finite relation choose the largest of these exponents among terms whose coefficient is nonzero. Its coefficient survives unchanged after substitution, because its substituted polynomial is monic there and all terms with smaller leading exponent contain only smaller exponents. The relation cannot vanish. This also covers rings with zero divisors; for the zero ring the assertion is the unique isomorphism of zero rings. In rank zero both polynomial rings are \(R\). □

**Lemma B.2 (self-adjoint and skew-adjoint normal forms).** Every self-adjoint operator on a finite-dimensional real Euclidean or complex Hermitian space has an orthonormal eigenbasis with real eigenvalues. Every real skew-adjoint matrix is orthogonally conjugate to

\[
J(t_1)\oplus\cdots\oplus J(t_m)\oplus 0,
\qquad J(t)=\begin{pmatrix}0&t\\-t&0\end{pmatrix},
\tag{B.3}
\]

where the last zero block is absent in even dimension and one-dimensional in odd dimension; zero values of the \(t_j\) are allowed.

**Proof.** For a nonzero space, maximize \(\langle v,Hv\rangle\) on the unit sphere. This number is real for self-adjoint \(H\), and the maximum exists by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) applied to the underlying real Euclidean space. At a maximizing unit vector \(v\), vary through \((v+tw)/|v+tw|\) for \(w\perp v\), \(t\in\mathbb R\). The derivative at zero is \(2\operatorname{Re}\langle w,Hv\rangle=0\). In the complex case apply the same calculation to \(iw\) to obtain also the imaginary part. Thus \(Hv\) is orthogonal to \(v^\perp\) and equals \(\lambda v\), with \(\lambda=\langle v,Hv\rangle\in\mathbb R\). Self-adjointness makes \(v^\perp\) invariant. Induct on its dimension; dimension zero ends the induction. Orthonormal coordinates exist by the Gram–Schmidt proof in [DG-CHAR-06 L.1](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#lemma-l-1). This proves the first assertion without a root-existence theorem for general polynomials.

For real \(X^T=-X\), the operator \(-X^2=X^TX\) is self-adjoint and nonnegative. Diagonalize it by the first assertion. Each eigenspace is \(X\)-invariant because \(X\) commutes with \(-X^2\). Its zero eigenspace is the kernel of \(X\), since \(\langle v,-X^2v\rangle=|Xv|^2\). On an eigenspace for \(a^2>0\), choose a unit \(v\) and put \(w=-Xv/a\). Then \(v,w\) are orthonormal, \(Xv=-aw\), and \(Xw=av\). Their plane has matrix \(J(a)\); its orthogonal complement is invariant by skew-adjointness. Repeat. Pair the remaining kernel vectors into \(J(0)\) blocks, leaving one zero vector exactly when the total dimension is odd. This is (B.3). Changing the sign of a basis vector if necessary makes the full basis positively oriented, at the cost of changing a block parameter's sign, or of reversing the final kernel vector in odd dimension. Thus signed parameters also give the normal form using \(SO(r)\). □

**Theorem B.3 (unitary and complex general linear invariants).** The real invariant ring of \(U(r)\) on \(\mathfrak u(r)\) is freely generated by

\[
X\longmapsto \sigma_1(iX),\ldots,X\longmapsto\sigma_r(iX).
\tag{B.4}
\]

The complex polynomial functions in the matrix entries on \(\mathfrak{gl}_r(\mathbb C)\) invariant under \(GL_r(\mathbb C)\) are freely generated by \(\sigma_1,\ldots,\sigma_r\). Here “polynomial in the entries” does not include their complex conjugates.

**Proof.** If \(X\) is skew-Hermitian, \(iX\) is Hermitian. Lemma B.2 diagonalizes it by a unitary matrix. On diagonal Hermitian matrices, the restriction of an invariant real polynomial is symmetric in the real diagonal coordinates, because permutation matrices are unitary. Lemma B.1 writes this restriction uniquely as a polynomial in the elementary symmetric functions. Those functions extend to the invariant real polynomials \(\sigma_j(iX)\): determinant multiplicativity, proved in [DG-CHAR-06 L.1](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#lemma-l-1), gives conjugation invariance, and the coefficients are real on Hermitian matrices by diagonalization. Subtract that polynomial expression from the given invariant. Its restriction to the diagonal is zero, hence its value on every skew-Hermitian matrix is zero by diagonalization. Independence follows by restricting a proposed relation to the same diagonal and using B.1 over \(\mathbb R\).

For the complex statement, DG-CHAR-17 S.2 proves the assertion on all matrices, including those that are not diagonalizable. Its proof first applies the elementary symmetric argument to diagonal matrices, then proves that the difference vanishes on a real open set of conjugates of matrices with distinct real diagonal entries, using the inverse function theorem. The polynomial identity lemma DG-CHAR-17 P.0 then makes that difference zero on every complex matrix. Thus no density assertion or diagonalizability assumption is needed here beyond the explicit proof in S.2. Independence is again its diagonal restriction and B.1, now over \(\mathbb C\). The empty list generates the constants for \(r=0\). □

**Theorem B.4 (orthogonal invariants and the Pfaffian).** For \(r=2m\) or \(2m+1\), define \(q_j(X)\) as the coefficient of \(s^{2j}\) in \(\det(I+sX)\), \(1\leq j\leq m\). Then

\[
\begin{aligned}
I(O(r))&=\mathbb R[q_1,\ldots,q_m],\\
I(SO(2m+1))&=\mathbb R[q_1,\ldots,q_m],\\
I(SO(2m))&=\mathbb R[q_1,\ldots,q_{m-1},\operatorname{Pf}]
\quad(m\geq1).
\end{aligned}
\tag{B.5}
\]

Each displayed set of generators is algebraically independent. In even rank,
\(\operatorname{Pf}(X)^2=q_m(X)=\det X\). We use the Pfaffian convention

\[
\operatorname{Pf}(X)=\frac1{2^m m!}
\sum_{\tau\in S_{2m}}\operatorname{sgn}(\tau)
\prod_{j=1}^m X_{\tau(2j-1),\tau(2j)},
\qquad \operatorname{Pf}(J(t))=t.
\tag{B.6}
\]

**Proof.** The full algebraic proofs DG-CHAR-17 P.1–P.2 show, from the exterior-power definition equivalent to (B.6), that
\(\operatorname{Pf}(QXQ^T)=\det(Q)\operatorname{Pf}(X)\), that the Pfaffian of an ordered block sum is the product, and that its square is the determinant. In particular it is \(SO(2m)\)-invariant. On the normal form (B.3),

\[
\det(I+sX)=\prod_{j=1}^m(1+s^2t_j^2),\qquad
q_j=e_j(t_1^2,\ldots,t_m^2),\qquad
\operatorname{Pf}(X)=t_1\cdots t_m.
\tag{B.7}
\]

Permuting two two-dimensional blocks has determinant \(+1\), so all permutations of the \(t_j\) occur even in \(SO(r)\). Reflecting one vector in a block reverses its parameter and has determinant \(-1\). Thus \(O(r)\) realizes every independent sign change. In odd dimension one can also reverse the final kernel vector, so \(SO(2m+1)\) realizes each such sign change. Their invariant restrictions are therefore polynomials in \(t_j^2\), symmetric under permutation: comparing coefficients under a sign change forces every odd exponent's real coefficient to be zero. By B.1 they are polynomials in the \(q_j\). The normal form makes restriction injective on invariant polynomials, proving both generation assertions. Algebraic independence follows because substitution \(u_j\mapsto t_j^2\) is injective on polynomial rings (it sends distinct monomials to distinct monomials), and B.1 gives independence of the elementary symmetric functions in the \(u_j\).

For \(SO(2m)\), simultaneous sign reversal of any two parameters is realized. If \(m\geq2\), each monomial with nonzero coefficient in an invariant restriction must therefore have the same parity in every exponent. For \(m=1\), the same conclusion means simply the decomposition into its even and odd powers. Thus the restriction has the unique form

\[
A(t_1^2,\ldots,t_m^2)
+(t_1\cdots t_m)B(t_1^2,\ldots,t_m^2).
\tag{B.8}
\]

Block permutations force both \(A\) and \(B\) to be symmetric, since the two parity types cannot cancel. Write them using B.1 and replace \(e_m(t^2)\) by \((t_1\cdots t_m)^2\). This gives generation by the last line of (B.5). For independence, a relation in \(q_1,\ldots,q_{m-1},z\), \(z=\operatorname{Pf}\), splits uniquely as \(C(q_1,\ldots,q_{m-1},z^2)+zD(q_1,\ldots,q_{m-1},z^2)\). Restriction and the parity separation in (B.8) make both coefficients zero. Independence of \(e_1(t^2),\ldots,e_m(t^2)\) gives \(C=D=0\). Normal form again identifies every invariant with its restriction. For dimensions zero and one the skew Lie algebra is zero and the invariant ring is \(\mathbb R\); the empty Pfaffian in rank zero is \(1\), not an additional generator. □

**Theorem B.5 (compact symplectic invariants).** View \(Sp(r)\) as the unitary complex transformations of \(\mathbb C^{2r}\) commuting with a fixed antiunitary map \(J\) satisfying \(J^2=-I\). Its Lie algebra consists of the skew-Hermitian complex matrices commuting with \(J\). Every such matrix is \(Sp(r)\)-conjugate to a diagonal matrix with paired eigenvalues \(it_j,-it_j\), \(t_j\in\mathbb R\). Its real invariant ring is freely generated by the coefficients \(q_j\) of \(s^{2j}\) in its complex determinant \(\det_{\mathbb C}(I+sX)\), \(1\leq j\leq r\).

**Proof.** Differentiating \(U^*U=I\) and \(UJ=JU\) at the identity gives \(X^*=-X\) and \(XJ=JX\). Conversely, the matrix exponential proved in [Local tools 2.3](local-tools-for-bundles-and-transport.md#2-differential-equations-and-their-parameters) gives a curve \(U(t)=\exp(tX)\). Differentiation gives \((U^*U)'=U^*(X^*+X)U=0\), and uniqueness of the matrix differential equation gives \(UJ=JU\) when \(XJ=JX\). Thus this curve lies in the stated group and has initial tangent \(X\), proving the Lie-algebra description.

Lemma B.2 diagonalizes \(iX\), so \(X\) has a unit eigenvector \(v\) with eigenvalue \(it\), \(t\in\mathbb R\). Since \(J\) is antilinear and commutes with \(X\), \(Jv\) has eigenvalue \(-it\). Also \(v\perp Jv\): the identity \(\langle Ju,Jw\rangle=\overline{\langle u,w\rangle}\), applied to \(u=v,w=Jv\), says \(-\langle Jv,v\rangle=\overline{\langle v,Jv\rangle}=\langle Jv,v\rangle\). Both vectors have unit norm. Their complex span is invariant under \(X,J\). Its orthogonal complement is invariant under \(X\) by skew-adjointness and under \(J\) by antiunitarity. Induction supplies an orthonormal basis of paired vectors \(v_1,\ldots,v_r,Jv_1,\ldots,Jv_r\), including zero eigenvalues. Sending a fixed paired orthonormal basis to this one gives a unitary map commuting with \(J\); hence it belongs to \(Sp(r)\). This also proves that the displayed model is exactly a quaternionic orthonormal basis, with \(J\) representing multiplication by a second imaginary unit.

Permuting pairs commutes with \(J\). Within one pair, the map \(v_j\mapsto Jv_j,\ Jv_j\mapsto-v_j\) is unitary and commutes with \(J\); it reverses \(t_j\). Consequently the restriction of an invariant polynomial is a symmetric polynomial in \(t_1^2,\ldots,t_r^2\), by the same coefficient argument as in B.4. On the diagonal,
\(\det_{\mathbb C}(I+sX)=\prod_j(1+s^2t_j^2)\).
The coefficients \(q_j\) extend the elementary symmetric functions, are real by this normal form, and are invariant by determinant multiplicativity. Lemma B.1 proves generation and independence on the diagonal, and conjugacy proves generation on the entire Lie algebra. For \(r=0\) the result is the constant ring. □

## C. Chern, Pontryagin and Euler normalizations

**Theorem C.1 (Chern forms and the Chern character).** For a complex rank-\(r\) bundle with connection, put

\[
c(\nabla)=\det\!\left(I+\frac{iF}{2\pi}\right)
=\sum_{j=0}^r c_j(\nabla),\qquad
\operatorname{ch}(\nabla)=\sum_{j\geq0}\frac1{j!}
\operatorname{tr}\!\left(\frac{iF}{2\pi}\right)^j .
\tag{C.1}
\]

The degree-\(2j\) forms are closed and their classes are connection independent. The second sum is finite as a differential form on a fixed finite-dimensional base. Under integration, \([c_j(\nabla)]\) equals the coefficient image of the integral class \(c_j(E)\). For a Hermitian connection the Chern forms and character forms are real. In particular,

\[
\begin{aligned}
c_1(\nabla)&=\frac{i}{2\pi}\operatorname{tr}F,\\
c_2(\nabla)&=\frac1{8\pi^2}
\bigl(\operatorname{tr}(F\wedge F)-\operatorname{tr}F\wedge\operatorname{tr}F\bigr),\\
\operatorname{ch}_0&=r,\quad \operatorname{ch}_1=c_1,\quad
\operatorname{ch}_2=\tfrac12(c_1^2-2c_2),\\
\operatorname{ch}_3&=\tfrac16(c_1^3-3c_1c_2+3c_3).
\end{aligned}
\tag{C.2}
\]

**Proof.** Determinant coefficients and trace powers are invariant polynomials, by determinant multiplicativity and cyclicity of trace. Apply A.2–A.3 to the frame bundle, or to its unitary reduction for a compatible connection. Each positive power raises the form degree by two, so terms above the dimension vanish. For reality, in a unitary frame \(F^*=-F\), hence \(iF\) is a Hermitian matrix of two-forms. The even-form coefficient ring is commutative; conjugating a determinant is entrywise conjugation, and transposing leaves its determinant unchanged, so every determinant coefficient is real. Likewise \(\overline{\operatorname{tr}(iF)^j}=\operatorname{tr}((iF)^T)^j=\operatorname{tr}(iF)^j\). These equalities are coefficientwise equalities of forms, with no eigenvalue assertion for form-valued matrices.

The integral comparison is DG-CHAR-17 C.2, which applies to any smooth complex connection on any of our bases. Its proof fixes the line normalization by the relative Thom class and the positively oriented real plane, then uses the proved smooth flag pullback and its injectivity to obtain every rank and every \(j\). Thus this assertion uses that earlier programme proof, including its integral normalization, rather than interpreting a real curvature class as an integral class by definition.

Finally DG-CHAR-17 S.3 proves Newton's coefficient identities for matrices and for even-form substitution. In degrees one and two they give \(\sigma_1(B)=\operatorname{tr}B\) and \(2\sigma_2(B)=(\operatorname{tr}B)^2-\operatorname{tr}(B^2)\). Substitute \(B=iF/(2\pi)\) to obtain the first two lines of (C.2). In degree three the same identity gives \(\operatorname{tr}B^3=c_1^3-3c_1c_2+3c_3\). Dividing the trace powers by \(j!\) proves the remaining formulas, also when some \(c_j=0\) above the rank. □

**Theorem C.2 (sums, tensor products and duals).** For the induced connections,

\[
\begin{aligned}
c(\nabla^{E\oplus H})&=c(\nabla^E)c(\nabla^H),&
\operatorname{ch}(\nabla^{E\oplus H})&=\operatorname{ch}(\nabla^E)+\operatorname{ch}(\nabla^H),\\
\operatorname{ch}(\nabla^{E\otimes H})&=\operatorname{ch}(\nabla^E)\operatorname{ch}(\nabla^H),&
c_j(\nabla^{E^*})&=(-1)^j c_j(\nabla^E).
\end{aligned}
\tag{C.3}
\]

The degree-\(2j\) part of the dual Chern character changes by \((-1)^j\). These formulas pass to de Rham classes and commute with smooth pullback. The Whitney and dual formulas also hold for the integral Chern classes.

**Proof.** [Linear and affine connections C.1](linear-and-affine-connections.md#theorem-c-1) proves the induced connections and their curvature actions: the sum curvature is \(F_E\oplus F_H\), the tensor curvature is \(F_E\otimes I+I\otimes F_H\), and the dual curvature is \(-F_E^T\). The determinant permutation expansion has no contribution mixing the two diagonal blocks, and hence gives the first identity. Trace of a block sum is additive, proving the second. The two tensor curvature matrices commute: their endomorphisms act on different factors and their scalar entries are even forms. The finite binomial expansion therefore gives
\(\exp(B\otimes I+I\otimes C)=\exp B\otimes\exp C\)
in each degree, for \(B=iF_E/(2\pi)\), \(C=iF_H/(2\pi)\). Summing diagonal indices gives \(\operatorname{tr}(U\otimes V)=\operatorname{tr}U\,\operatorname{tr}V\), proving the tensor identity. Transposition preserves determinant and trace of powers over the even commutative coefficient ring; substitution of \(-B^T\) gives both dual sign rules.

Pullback preserves these matrix expressions and the induced connections, as proved in [Curvature and holonomy A.7](curvature-and-holonomy-groups.md#theorem-a-7). A.3 makes the resulting class identities independent of the chosen connections. For integral classes, the Whitney theorem is proved in [DG-CHAR-09 B.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-09.md#theorem-b-4), and the dual theorem in [DG-CHAR-09 C.2](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-09.md#theorem-c-2). Their hypotheses hold here: a countable smooth atlas and the partition of unity in [Local tools 3.1](local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) give the paracompactness and bundle metrics used in the latter theorem. Alternatively, its smooth flag proof is DG-CHAR-17 C.1. Thus the integral statements retain their full torsion information. □

**Theorem C.3 (Pontryagin classes and arbitrary real connections).** For a real bundle \(V\), define the integral Pontryagin classes by

\[
p_j(V)=(-1)^j c_{2j}(V_{\mathbb C}),\qquad V_{\mathbb C}=V\otimes_{\mathbb R}\mathbb C.
\tag{C.4}
\]

For any real connection, the real closed form
\(p_j(\nabla)=(-1)^j c_{2j}(\nabla_{\mathbb C})\)
represents its real coefficient image. If the connection preserves a metric, its total Pontryagin form is
\(\det(I+F/(2\pi))\), with its degree-\(4j\) term \(p_j(\nabla)\); every odd determinant coefficient vanishes. In general,

\[
p_1(\nabla)=\frac{(\operatorname{tr}F)^2-\operatorname{tr}(F\wedge F)}{8\pi^2}.
\tag{C.5}
\]

The class \(c_{2j+1}(V_{\mathbb C})\) is killed by \(2\), and its curvature representative is exact over \(\mathbb C\).

**Proof.** Real bundle transition matrices, extended complex linearly, give the complexification. Its induced potential and curvature are the same real matrices regarded as complex matrices, by the local connection formula. Formula C.1 and its integral comparison prove the first statement: \(i^{2j}=(-1)^j\) makes \((-1)^j\sigma_{2j}(iF/(2\pi))=\sigma_{2j}(F/(2\pi))\) real.

For a metric connection choose an orthonormal frame, so \(F^T=-F\). Over the even-form ring,
\(\det(I+sF)=\det((I+sF)^T)=\det(I-sF)\).
Comparing coefficients shows that its odd coefficients are zero over the real numbers. The even coefficients are exactly the forms just computed. In an arbitrary frame the invariant determinant coefficients are unchanged. Formula (C.5) follows directly by negating the expression for \(c_2\) in (C.2); when \(\operatorname{tr}F=0\) it reduces to \(-\operatorname{tr}(F\wedge F)/(8\pi^2)\).

There is always a compatible connection \(\nabla_0\) for some bundle metric, by DG-CHAR-17 D.2. Put \(a=\nabla-\nabla_0\), an endomorphism-valued one-form, and \(b=\operatorname{tr}a\). The trace-square cancellation \(\operatorname{tr}(A\wedge A)=0\), obtained by pairing indices \(i,j\), gives \(\operatorname{tr}F=d\operatorname{tr}A\) locally. The tensorial difference makes \(b\) global. Since the metric connection has zero curvature trace, subtracting gives \(\operatorname{tr}F=db\). The trace term in (C.5) is consequently exact:
\((\operatorname{tr}F)^2=db\wedge db=d(b\wedge db)\).
For every higher odd coefficient, A.3 compares \(\nabla_{\mathbb C}\) with \((\nabla_0)_{\mathbb C}\); the latter representative is zero, proving exactness with the primitive (A.6).

Finally \(V_{\mathbb C}\) is complex-linearly isomorphic to its conjugate by \(v\otimes z\mapsto v\otimes\bar z\), where the target has the conjugate scalar action. This formula is compatible with all real transitions, so defines a bundle isomorphism. [DG-CHAR-09 B.5](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-09.md#theorem-b-5) gives \(c_k(\overline{V_{\mathbb C}})=(-1)^k c_k(V_{\mathbb C})\). In odd degree the isomorphism therefore says \(c_k=-c_k\), or \(2c_k=0\). This integral assertion permits nonzero two-torsion; it does not assert integral vanishing. □

**Theorem C.4 (Euler form, orientation and metric).** Let \(V\) be an oriented real rank-\(2m\) bundle with a metric connection. In positively oriented orthonormal frames the form

\[
e(\nabla)=\operatorname{Pf}\!\left(\frac{F}{2\pi}\right)
\tag{C.6}
\]

is global, closed, and represents the real coefficient image of the integral Euler class. Its class is independent of the metric and compatible connection. Reversing orientation negates it, and

\[
e(\nabla)^2=p_m(\nabla),\qquad e(V)^2=p_m(V)
\tag{C.7}
\]

where the second equality is integral. In odd rank \(2e(V)=0\), hence its real image is zero. Rank zero has Euler form and class \(1\).

**Proof.** Changes of positively oriented orthonormal frame lie in \(SO(2m)\). The congruence rule in B.4 gives globality, and A.2 proves closedness. The complete Euler comparison DG-CHAR-17 Y.1 identifies its class with the integral Euler class under the integration map; its proof treats every smooth base under our assumptions, not just compact bases. It also gives the odd-rank and rank-zero real representatives. The orientation, odd-rank integral and rank-zero assertions themselves follow from the integral Thom uniqueness and zero-section argument [DG-CHAR-06 T.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#theorem-t-4).

Here is also a direct connection comparison when the metric changes. If \(h_0,h_1\) are two metrics, define the positive \(h_0\)-self-adjoint bundle map \(S\) by \(h_1(v,w)=h_0(Sv,w)\); solving this equation in a local frame shows \(S\) is smooth. Lemma B.2 gives its unique positive self-adjoint square root \(B\). Indeed diagonalization gives a root by taking positive real square roots; any positive root commutes with \(S=B^2\), preserves its eigenspaces and, after diagonalization within each, has precisely those positive eigenvalues, proving uniqueness. The root varies smoothly. On self-adjoint matrices the derivative of \(B\mapsto B^2\) is \(H\mapsto BH+HB\); in an eigenbasis its \(ij\)-entry is \((b_i+b_j)H_{ij}\), so it is invertible since every \(b_i>0\). The inverse function theorem [Local tools 0.4](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) gives a smooth local inverse, and uniqueness makes these local roots agree. Positivity persists in that neighbourhood because a perturbation of operator norm below the smallest \(b_i\) has positive quadratic form, by [Local tools 0.0](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Smooth local orthonormal frames can be obtained by Gram–Schmidt, whose divisions and positive square roots are smooth by [Local tools 0.3–0.4](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). This justifies applying the matrix argument in bundle charts.

The map \(T=B^{-1}\) is an orientation-preserving isometry from \((V,h_0)\) to \((V,h_1)\): \(h_1(Tv,Tw)=h_0(v,w)\), and its positive eigenvalues give positive determinant. Pulling an \(h_1\)-connection through \(T\) gives an \(h_0\)-connection whose curvature has the same Pfaffian form in the transported oriented frames. A.3 for \(SO(2m)\) compares it with any chosen \(h_0\)-connection by an exact form. This proves metric independence directly as well.

The Pfaffian-square identity DG-CHAR-17 P.2 holds over every commutative coefficient ring, hence also over the even-form ring. With C.3 it gives the first equality of (C.7). To verify the integral equality, use the real bundle isomorphism
\[
V\oplus V\longrightarrow (V_{\mathbb C})_{\mathbb R},
\qquad (v,w)\longmapsto v+iw.
\tag{C.8}
\]
For \(r=2m\), the complex orientation is the order \((e_1,ie_1,\ldots,e_r,ie_r)\), whereas the ordered direct-sum orientation is \((e_1,\ldots,e_r,ie_1,\ldots,ie_r)\). Moving the second list into the first makes \(r(r-1)/2\) transpositions, with sign \((-1)^m\). The top Chern class equals the Euler class of the complex-oriented underlying real bundle by [DG-CHAR-09 B.2](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-09.md#theorem-b-2). The ordered Euler product and orientation sign in [DG-CHAR-06 T.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#theorem-t-4) therefore give
\[
c_{2m}(V_{\mathbb C})=(-1)^m e(V)\smile e(V).
\]
Multiplying by \((-1)^m\) as in (C.4) proves the integral identity. This sign computation includes the orientation information absent from a mere square-root argument for characteristic forms. □

## D. Lines, surfaces and flatness

**Example D.1 (the tautological line and its real plane).** Let \(L\to\mathbb{CP}^1\) be the tautological line with its induced Hermitian metric. The unit vectors in its fibres form the Hopf principal circle bundle \(S^3\to\mathbb{CP}^1\), with right action \(u\mapsto u\lambda\). In the affine coordinate \(z=x+iy\), the unit section \(u(z)=(1,z)/\sqrt{1+|z|^2}\) gives

\[
\begin{aligned}
A&=u^*du=\frac{\bar z\,dz-z\,d\bar z}{2(1+|z|^2)},\\
F&=\frac{d\bar z\wedge dz}{(1+|z|^2)^2},\\
c_1(\nabla)&=-\frac{dx\wedge dy}{\pi(1+x^2+y^2)^2}.
\end{aligned}
\tag{D.1}
\]

Thus \(\langle c_1(L),[\mathbb{CP}^1]\rangle=-1\), and the dual line has Chern number \(+1\). The Euler form of the underlying plane with its complex orientation is the same \(c_1\)-form.

**Proof.** The projective charts and tautological bundle are constructed in [Complex manifolds G.1–G.2](complex-manifolds-and-kahler-metrics.md#theorem-g-1) and [Kähler curvature B.2](kahler-curvature-and-hermitian-vector-bundles.md#example-b-2). On the unit sphere \(u^*u=1\), differentiation gives \(\overline{u^*du}=-u^*du\), so \(\omega=u^*du\) takes values in \(i\mathbb R\). It is invariant under the constant right circle action and evaluates on the vertical vector \(u\,it\) as \(it\). [Connections and parallel transport A.2](connections-and-parallel-transport.md#theorem-a-2) therefore makes it a principal connection. Differentiating the given unit section yields the expression for \(A\). The scalar one-form has \(A\wedge A=0\); the quotient rule gives \(dA=d\bar z\wedge dz/(1+|z|^2)^2\). Finally \(d\bar z\wedge dz=2i\,dx\wedge dy\), proving all of (D.1).

The normalized integral of the final density is \(-1\). For the full chart computation including the omitted point, [Kähler curvature B.2](kahler-curvature-and-hermitian-vector-bundles.md#example-b-2) and J.5 prove that
\(\int_{\mathbb{CP}^1}dx\,dy/(1+x^2+y^2)^2=\pi\):
integration over radius-\(R\) disks gives \(\pi R^2/(1+R^2)\), and in the other coordinate the missing neighbourhood has a smooth bounded density with integral tending to zero. Those proofs establish the projective orientation as well. C.1 identifies the integral with the evaluation of the integral class; [DG-CHAR-08 R.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-08.md#theorem-r-4) identifies its positive degree-two generator if a generator is desired. The dual sign rule C.2 gives \(+1\).

Write \(A=ia\), \(a\) real. In the positively oriented real frame \((u,iu)\), the matrix is \(\begin{pmatrix}0&-a\\a&0\end{pmatrix}\), because its columns are the coefficients of the derivatives of these two vectors. Its curvature has upper-right entry \(-da\). Its Pfaffian divided by \(2\pi\) is \(-da/(2\pi)=iF/(2\pi)\), exactly the line Chern form. This verifies the Euler sign directly in rank two. □

**Theorem D.2 (Gauss–Bonnet and the surface curvature form).** For a closed oriented Riemannian manifold \(M\) of positive even dimension \(2m\), the curvature of its Levi-Civita connection satisfies

\[
\int_M \operatorname{Pf}\!\left(\frac{F}{2\pi}\right)=\chi(M).
\tag{D.2}
\]

On an oriented surface, with positive orthonormal coframe \(\theta^1,\theta^2\) and Gaussian curvature \(K\),

\[
F_{12}=K\,\theta^1\wedge\theta^2,\qquad
\int_M K\,d\mathrm{area}=2\pi\chi(M).
\tag{D.3}
\]

The rank-zero convention gives the number of points when the points carry their canonical positive orientations.

**Proof.** Levi-Civita existence and uniqueness, including metric compatibility, are proved in [Riemannian connections A.1](riemannian-connections-and-convex-neighbourhoods.md#theorem-a-1), equivalently DG-CHAR-17 V.1. The Euler comparison C.4 identifies the class of its Pfaffian with the real image of \(e(TM)\). DG-CHAR-17 O.6 proves that integrating that representative equals evaluation on the real fundamental class. Coefficient change commutes with cocycle-cycle evaluation, so this number is \(\langle e(TM),[M]\rangle\), an integer. [DG-CHAR-07 D.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#theorem-d-4) proves that this integral Euler number equals \(\chi(M)\), with the homological definition and coefficient independence established in [DG-CHAR-07 C.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#theorem-c-3). Combining these exact earlier programme results proves (D.2). Their proofs also handle finitely many components and the empty manifold.

In dimension two, \(R(e_1,e_2)\) is skew-adjoint, and its upper-right entry is \(\langle R(e_1,e_2)e_2,e_1\rangle=K\), by the sectional-curvature convention of [Geodesics C.3](geodesics-normal-coordinates-and-curvature.md#corollary-c-3). Every two-form is its value on \(e_1,e_2\) times \(\theta^1\wedge\theta^2\). Hence \(F_{12}=K\theta^1\wedge\theta^2\). The two-by-two Pfaffian is its upper-right entry, proving (D.3). In dimension zero, the empty Pfaffian is one, and [DG-CHAR-07 D.4](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#theorem-d-4) shows that integration, Euler evaluation and Euler characteristic all count the finitely many positive points. □

**Example D.3 (sphere, torus and genus).** The round radius-\(R\) sphere has \(K=R^{-2}\), area \(4\pi R^2\), and Euler number \(2\). The quotient \(\mathbb R^2/\mathbb Z^2\) with its Euclidean metric is flat and has Euler number \(0\). A closed oriented genus-\(g\) surface has \(\chi=2-2g\), and therefore

\[
\int_{\Sigma_g}K\,d\mathrm{area}=4\pi(1-g).
\tag{D.4}
\]

If such a surface is given a metric with \(K=-1\), its area is \(4\pi(g-1)\). This is a conditional calculation for a given metric.

**Proof.** DG-CHAR-17 V.5 proves the sphere calculation by differentiating its stereographic parametrization, solving the torsion-free coframe equations, and integrating the resulting density. In particular it proves \(F_{12}=R^{-2}d\mathrm{area}\) and area \(4\pi R^2\) with the pole estimate needed for the integral. D.2 then gives Euler number \(2\). [Curvature and holonomy D.3](curvature-and-holonomy-groups.md#example-d-3) constructs the Euclidean quotient torus and its global parallel frame. The connection matrix and curvature in that frame are zero, so D.2 gives its Euler number \(0\).

Here is a homological verification of the genus value, without using an unproved cellular-homology formula. A genus-\(g\) surface is the oriented connected sum of \(g\) tori, with the sphere for \(g=0\); the following argument uses this handle presentation and does not require a classification theorem for surfaces. The sphere and circle homology calculations are [DG-CHAR-06 E.5](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#lemma-e-5). They give \(\chi(S^2)=2\), \(\chi(S^1)=0\), and \(\chi(D^2)=1\), the last also following from radial contraction. The field product theorem [DG-CHAR-07 D.1](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#lemma-d-1) gives Betti numbers \(1,2,1\) for \(S^1\times S^1\), and thus Euler characteristic zero.

For completeness, Euler characteristic is additive for an open union \(X=U\cup V\) whenever its Mayer–Vietoris groups are finite dimensional and eventually zero:
\[
\chi(X)=\chi(U)+\chi(V)-\chi(U\cap V).
\tag{D.5}
\]
The exact sequence is proved in [DG-CHAR-06 E.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#lemma-e-3). In any finite exact sequence of finite-dimensional vector spaces, decompose each dimension as the dimension of the incoming image plus that of the outgoing image, by choosing a basis for the kernel and lifting a basis of the image. Alternating summation cancels each image twice, proving (D.5); eventual vanishing truncates the long sequence legitimately. Compact surfaces have finite homology by [DG-CHAR-07 C.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#theorem-c-3).

Remove a small closed coordinate disk from a closed surface \(S\), and let \(S^\circ\) denote its interior complement. Cover \(S\) by a slightly larger open coordinate disk and \(S^\circ\); the overlap is an annulus and retracts radially to \(S^1\). The disk contracts and the exact sequence also proves the groups of \(S^\circ\) finite and eventually zero. Thus (D.5) gives \(\chi(S^\circ)=\chi(S)-1\). Changing the radius of the removed disk does not change this homotopy type: on the coordinate collar use the radial homotopy that moves each radius to its maximum with the chosen inner collar radius and is fixed outside that collar. For the connected sum \(S\#T\), take an open cover by the two punctured sides extended a little along the joining cylinder. Each retracts to its punctured side, and their overlap retracts to the middle circle by the cylinder coordinate. Formula (D.5) therefore gives \(\chi(S\#T)=\chi(S)+\chi(T)-2\). Starting with one torus and applying this \(g-1\) times yields \(2-2g\) for \(g\geq1\); the sphere settles \(g=0\). D.2 proves (D.4). Substituting \(K=-1\) into that equality gives the stated area. No assertion of existence of a constant-negative-curvature metric is used. □

**Proposition D.4 (what flatness makes vanish).** If a principal bundle admits a flat connection, all its positive-degree Weil classes vanish. A complex bundle with a flat connection has \(c_j(E)_{\mathbb R}=0\) for \(j>0\) and \(\operatorname{ch}(E)=\operatorname{rank}E\) in de Rham cohomology. A real bundle with a flat connection has zero positive Pontryagin classes over \(\mathbb R\). An oriented real bundle with a flat metric connection has zero positive-rank real Euler class. These conclusions do not assert that the corresponding integral classes vanish.

**Proof.** Evaluate a homogeneous polynomial of positive degree at \(F=0\): its value is zero. A.2 makes that class independent of the chosen connection. By summing homogeneous parts, an arbitrary invariant polynomial has Weil class equal to its constant term \(p(0)\) in degree zero. This proves the first assertion and, using C.1 and C.3, the Chern, character and Pontryagin assertions. For the Euler assertion use a connection on the oriented orthonormal frame bundle, whose curvature remains zero, and apply C.4. Odd rank has zero real Euler class already by C.4.

The metric hypothesis in this Euler argument matters: its polynomial is invariant on \(\mathfrak{so}(r)\), and an arbitrary flat connection on the larger oriented general linear frame bundle need not be a connection on that reduction. For a concrete algebraic distinction in rank two, a conjugation-invariant linear functional on real \(2\)-by-\(2\) matrices must be a multiple of trace. Conjugating by positive diagonal matrices forces its off-diagonal coefficients to vanish, since those matrix units are multiplied by arbitrary positive ratios. Conjugating by \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), of determinant \(+1\), interchanges the two diagonal units, so their coefficients agree. Trace vanishes on \(\mathfrak{so}(2)\), whereas its Pfaffian does not. The Euler polynomial therefore cannot be obtained by restricting such a degree-one invariant of \(GL^+(2,\mathbb R)\). The preceding flat-Weil argument supplies no real Euler-vanishing statement for arbitrary flat real connections.

Finally real comparison can lose integral information. The explicit flat complex line over \(\mathbb{RP}^2\) in [Kähler curvature J.6](kahler-curvature-and-hermitian-vector-bundles.md#example-j-6) has nonzero first integral Chern class of order two and zero curvature. Its full quotient construction and class calculation there give an example within the programme. On a compact base, the finite integral homology theorem [DG-CHAR-07 G.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#theorem-g-3), the universal-coefficient sequence [DG-CHAR-06 U.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#theorem-u-3) and the finite abelian decomposition [DG-CHAR-07 C.1](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-07.md#lemma-c-1) show that the kernel of the real coefficient map is torsion: its free Hom part injects into real-valued Hom, and the Ext term is a finite torsion group. No such additional kernel description is needed or asserted for arbitrary noncompact bases. □

## E. Exercises with complete solutions

**Exercise E.1 (Hopf normalization).** Compute \(c_1(L)\) and \(c_1(L^*)\) on the complex-oriented projective line, and compare the first with the Euler form of \(L_{\mathbb R}\).

**Proof.** In (D.1), the factor \(i/(2\pi)\) multiplies \(2i\,dx\wedge dy/(1+|z|^2)^2\), giving the negative normalized density. Its integral is \(-1\) by D.1, so the integral class is minus the positive generator identified there. C.2 negates it for the dual, giving \(+1\). For \(A=ia\), the real curvature matrix is \(\begin{pmatrix}0&-da\\da&0\end{pmatrix}\), whose Pfaffian is \(-da\). Hence its Euler form is \(-da/(2\pi)=iF/(2\pi)\), as required. □

**Exercise E.2 (a global difference and a local potential).** Derive the primitive for \(\operatorname{tr}(F_1^2-F_0^2)\), and explain when \(\operatorname{tr}(A\,dA+\tfrac23A^3)\) is a global expression.

**Proof.** With \(\alpha=A_1-A_0\), substitute \(F_t=F_0+tD_0\alpha+t^2\alpha^2\) in A.6 for the trace-square polynomial. The three integrals \(2\int_0^1 1\,dt=2\), \(2\int_0^1t\,dt=1\), and \(2\int_0^1t^2\,dt=2/3\) give exactly (A.11). A.3 proves its derivative is the specified difference. If \(A_0=0\) in a global trivialization, (A.11) reduces to (A.12). In a merely local frame, \(A\) changes by a conjugation plus \(g^{-1}dg\); it is not a tensorial difference of two globally chosen connections. Therefore that shorter potential formula is local, whereas (A.11) descends globally for two actual connections. □

**Exercise E.3 (flatness and integral information).** State exactly which conclusions about characteristic classes follow from a flat complex connection and from a flat oriented real connection.

**Proof.** Proposition D.4 gives zero positive real Chern classes and character equal to rank in the complex case, and zero real Pontryagin classes in the real case. It also gives zero real Euler class when the real flat connection is metric; the rank-two invariant-polynomial calculation there explains why the same proof does not cover an arbitrary real flat connection. C.3 separately proves that odd Chern classes of a complexified real bundle are killed by two. None of these statements removes integral torsion. D.4's programme example over \(\mathbb{RP}^2\) proves that even a flat unitary line can have nonzero integral first Chern class. □

**Exercise E.4 (Euler normalization, Gauss–Bonnet and area).** Prove that the Pfaffian form represents the integral Euler class over the reals, using the earlier Thom-form theorem, and deduce generalized Gauss–Bonnet. Then verify the radius independence of the round sphere's Euler number and compute the area of a genus-\(g\) surface equipped with curvature \(-1\).

**Proof.** The relative Gaussian pair of DG-CHAR-17 G.3 and H.2 has a properly supported representative whose integral on every oriented fibre is one. The relative integration theorem I.5 and its fibre normalization O.4 identify those restrictions with the positive real images of the integral Thom generators. Thom uniqueness [DG-CHAR-06 T.3](../supporting/DG-CHAR-8e0b5f71efec/src/DG-CHAR-06.md#theorem-t-3) therefore identifies the whole relative class with that coefficient image. Pull back along the zero section: the explicit Gaussian calculation DG-CHAR-17 G.2 gives \(\operatorname{Pf}(F/(2\pi))\), while the integral zero-section definition gives \(e(V)\). This is precisely the fully proved comparison DG-CHAR-17 Y.1 used in C.4. Applied to \(TM\), the integration pairing and tangent Euler-number theorem in D.2 give generalized Gauss–Bonnet.

Example D.3 gives \(K=R^{-2}\) and area \(4\pi R^2\), so \((2\pi)^{-1}\int K\,d\mathrm{area}=2\), independent of \(R>0\). For the given negative-curvature surface, D.3 proves \(\int K\,d\mathrm{area}=4\pi(1-g)\). The left side is minus its area, so the area is \(4\pi(g-1)\). A nonempty Riemannian surface has positive area: a positive coordinate density has a positive lower bound on some small closed coordinate disk, by [Local tools 0.1](local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), so its integral there is positive. Hence the assumed metric on a nonempty closed surface forces \(g>1\). This is a consequence for the given metric and does not invoke a uniformization theorem. □

## Further reading

- Eckhard Meinrenken, *Group actions on manifolds*, [freely accessible author-hosted lecture notes](https://www.math.utoronto.ca/~mein/teaching/LectureNotes/action.pdf), Sections 5.1–5.4, for invariant polynomials, curvature and the Weil construction.
- K. Venkatram, notes for Denis Auroux's MIT 18.966, *Geometry of Manifolds*, Spring 2007: [Lecture 10](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/2e7d5aae3c1b3c6f935960608851165b_lect10.pdf), Section 2, and [Lecture 11](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/4699443c64f6c6f5bdbab98172674dbd_lect11.pdf), Section 1.2, for Chern forms, direct sums and pullbacks.

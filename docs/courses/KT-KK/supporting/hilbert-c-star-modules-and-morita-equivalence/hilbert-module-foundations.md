# Ordinary Hilbert C*-module foundations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Independently written exposition; Self-checked by the writing AI. Public domain (CC0). The separately linked source retains its author's copyright and terms.*

This receiving companion proves the ordinary module facts needed before the compact-operator and interior tensor constructions. Coefficient algebras may be nonunital, nonseparable and not sigma-unital; modules need not be full or countably generated. Inner products are linear in the second variable. Grading and coefficient semilinearity are added in the graded lesson after these ordinary constructions.

<a id="mf-001"></a>
## MF.1. Exact coefficient inputs and a state test

The earlier programme lesson [C*-algebras: continuous functional calculus, automatic continuity, positive cones and quotients](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html) proves the following inputs: spectral permanence in Theorem 3.2; contractivity and faithful isometry of homomorphisms in Theorems 4.2 and 4.4; continuous functional calculus, including the nonunital calculus, in Theorems 5.1 and 5.3; and the closed positive cone, conjugation of order, order bounds and positive square roots in Theorem 8.2 and Proposition 8.5. The earlier [Hahn–Banach lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html), Theorem 2.2 and Theorem 5.3, proves complex norm-preserving extension and the closed graph theorem. These are coefficient-algebra and Banach-space inputs, with no Hilbert-module result among them. The same C*-algebra lesson, Theorem 11.4 and Corollary 11.5(1), proves a positive contractive approximate identity for every coefficient algebra. This is the approximate identity used in MF.3 and MF.6. The first KT–KK lesson independently constructs it in Lemma 2.0; that later construction is not needed to establish this companion.

Here is the state argument needed below, so no representation or module-localization theorem is an additional input. In a nonzero unital C*-algebra \(D\), a complex-linear functional \(f\) with \(\|f\|=f(1)=1\) is positive. For \(h=h^*\), the unitary \(\exp(ith)\) has norm one. The norm-convergent exponential series gives
\[
 f(\exp(ith))=1+itf(h)+O(t^2).
\]
The inequality \(|f(\exp(ith))|^2\leq1\), for both signs of real \(t\), forces \(\operatorname{Im} f(h)=0\). If \(0\leq a\leq1\), then \(f(a)\) is real and
\[
 |1-f(a)|=|f(1-a)|\leq\|1-a\|\leq1;
\]
hence \(f(a)\geq0\). Scaling proves positivity for every \(a\geq0\). In particular such a functional is a state and \(f(d^*)=\overline{f(d)}\), by decomposing \(d\) into real and imaginary self-adjoint parts.

For any \(h=h^*\in D\) and \(\lambda\in\sigma_D(h)\), evaluation at \(\lambda\) on the unital algebra \(C^*(1,h)\), through continuous functional calculus, is a functional of norm one taking \(1\) to \(1\). Hahn–Banach extends it with the same norm to \(D\); the preceding argument makes the extension positive. Consequently states detect positivity of self-adjoint elements: if \(h\) has a negative spectral value, this extension takes a negative value on \(h\). They also recover the norm of a positive element by evaluation at its maximum spectral value. For arbitrary \(d\), if every state vanishes on \(d\), its real and imaginary self-adjoint parts vanish by the same norm-attaining argument, so \(d=0\).

For a nonunital \(A\), apply this argument in its forced unitization \(D=\widetilde A\), restricting the states to \(A\). Restrictions may have norm smaller than one; only positivity and separation are required. Thus, including \(A=\{0\}\),
\[
 h=h^*\in A,\qquad
 \bigl[f(h)\geq0\text{ for every state }f\text{ of }\widetilde A\bigr]
 \quad\Longleftrightarrow\quad h\geq0.                 \tag{MF.1}
\]
Positivity in \(A\) and its unitization agrees by spectral permanence. No pure-state or Krein–Milman assertion is needed here.

<a id="mf-002"></a>
## MF.2. A coefficient-valued inner product and Cauchy–Schwarz

Let \(E_0\) be a complex vector space with a complex-bilinear right action of a C*-algebra \(A\). Suppose that a map \(\langle\ ,\ \rangle:E_0\times E_0\to A\) is additive and complex-linear in its second argument, satisfies
\[
 \langle x,ya\rangle=\langle x,y\rangle a,\qquad
 \langle y,x\rangle=\langle x,y\rangle^*,\qquad
 \langle x,x\rangle\geq0.                            \tag{MF.2}
\]
It follows that it is conjugate-linear in its first argument and that
\(\langle xa,yb\rangle=a^*\langle x,y\rangle b\).
Definiteness is not required yet. Put
\(\|x\|=\|\langle x,x\rangle\|^{1/2}\).

We first prove the scalar inequality used in the coefficient argument. For any positive semidefinite complex sesquilinear form \(b\), linear in its second argument, set \(u=b(v,v)\), \(w=b(z,z)\), and \(c=b(v,z)\). If \(u>0\), positivity at \(z-vc/u\) gives \(w-|c|^2/u\geq0\). If \(u=0\), positivity at \(z+tv\), for every complex \(t\), forces \(c=0\): otherwise a suitable phase and an arbitrarily large magnitude make \(w+t\overline c+\overline t c\) negative. Thus
\[
 |b(v,z)|^2\leq b(v,v)b(z,z).                        \tag{MF.3}
\]

We now prove the stronger coefficient-order inequality
\[
 \langle x,y\rangle^*\langle x,y\rangle
       \leq \|x\|^2\langle y,y\rangle.              \tag{MF.4}
\]
Write \(c=\langle x,y\rangle\) and \(a=\langle x,x\rangle\). For a state \(f\) of \(\widetilde A\), the form \(b_f(v,z)=f(\langle v,z\rangle)\) meets the hypotheses just proved. Put \(q=f(c^*c)\geq0\) and \(v=xc\). Then
\[
 b_f(v,y)=q,\qquad
 b_f(v,v)=f(c^*ac)\leq\|x\|^2q,
\]
since \(0\leq a\leq\|x\|^2 1\) and conjugation preserves order in the coefficient algebra. Equation (MF.3) therefore gives
\(q^2\leq\|x\|^2q\, f(\langle y,y\rangle)\).
When \(q>0\), divide by \(q\); when \(q=0\), the desired inequality is automatic. This holds for every \(f\), so (MF.1) proves (MF.4). In particular
\[
 \|\langle x,y\rangle\|\leq\|x\|\|y\|.             \tag{MF.5}
\]
This proof uses scalar positive forms and coefficient states before constructing any adjointable-operator algebra or matrix Gram cone.

The triangle inequality follows by expanding \(\langle x+y,x+y\rangle\), taking its norm and using (MF.5):
\[
 \|x+y\|^2\leq \|x\|^2+2\|x\|\|y\|+\|y\|^2.
\]
Complex homogeneity follows directly from (MF.2). Moreover
\[
 \|xa\|^2=\|a^*\langle x,x\rangle a\|
       \leq\|a\|^2\|x\|^2.                         \tag{MF.6}
\]
Thus this is a seminorm; it is a norm if \(\langle x,x\rangle=0\) implies \(x=0\). Its null vectors are orthogonal to every vector by (MF.5).

<a id="mf-003"></a>
## MF.3. Quotient, completion, direct sums and coefficient action

The set \(N=\{x:\|x\|=0\}\) is a vector subspace by the seminorm inequalities, and a right submodule by (MF.6). Since \(\langle n,y\rangle=\langle y,n\rangle=0\) for \(n\in N\), the inner product on \(E_0/N\) is independent of representatives and is definite. Its norm is exactly the quotient's inherited seminorm.

Take the metric completion \(E\) of \(E_0/N\). The construction can be made with Cauchy sequences, identifying two sequences whose difference tends to zero. Give a sequence class the norm \(\lim_n\|x_n\|\), which is independent of its representative by the triangle inequality. Constant sequences embed the original space isometrically and densely: a sufficiently late term of a Cauchy sequence is close to its class. To see completeness, for any Cauchy sequence of classes \(z_m\), choose original vectors \(u_m\) with \(\|z_m-u_m\|<1/m\). Then \((u_m)\) is Cauchy, its sequence class \(u\) satisfies \(\|u_m-u\|\to0\), and the triangle inequality gives \(z_m\to u\). Cauchy sequences \(x_n,y_n\) are bounded and satisfy
\[
 \|\langle x_n,y_n\rangle-\langle x_m,y_m\rangle\|
 \leq\|x_n-x_m\|\|y_n\|+\|x_m\|\|y_n-y_m\|.
\]
Their inner products therefore converge in \(A\). This estimate also shows that changing either representative sequence does not change the limit. Define the inner product of their completed vectors to be this limit. Addition, scalar multiplication, conjugate symmetry and right linearity pass to the limit. Positivity passes to the limit because \(A_+\) is closed. The norm identity passes to the limit because the norm on \(A\) is continuous; it gives definiteness in the completed metric space.

For each \(a\in A\), (MF.6) extends \(x\mapsto xa\) continuously to \(E\). Bilinearity and associativity follow on the dense original space and hence on \(E\), and (MF.6) still holds. The limiting inner-product identities show that \(E\) is a Hilbert \(A\)-module. This proves both the semidefinite quotient and its completion, without a unit or any countability condition.

For a family of Hilbert \(A\)-modules \((E_i)_{i\in I}\), first give the algebraic finite-support sum the form
\[
 \langle x,y\rangle=\sum_{i\in I}\langle x_i,y_i\rangle.
                                                               \tag{MF.7}
\]
It is definite: each positive summand of a zero diagonal sum must vanish. Complete as above. This is the Hilbert-module direct sum \(\bigoplus_{i\in I}E_i\). Its coordinate maps and finite-coordinate projections have norm at most one because their diagonal sums are dominated by the full positive diagonal sum. A coordinate inclusion is isometric; its adjoint is its coordinate projection, as follows directly from (MF.7).

Equivalently, the direct sum consists of families \(x_i\in E_i\) for which the net
\[
 \sum_{i\in J}\langle x_i,x_i\rangle
 \quad(J\subset I\text{ finite, ordered by inclusion})
                                                               \tag{MF.8}
\]
converges in norm. Indeed their finite-support vectors are Cauchy precisely when the positive finite-tail sums tend to zero in norm: the squared norm of a difference of two such vectors is the norm of the sum over their symmetric difference. Norm convergence in (MF.8) makes these tails uniformly small. Conversely, for an element of the completion, coordinates exist by continuity. If a finite-support vector \(z\) is close to \(x\) and \(J\) contains its support, then
\[
 \|x-P_Jx\|=\|(1-P_J)(x-z)\|\leq\|x-z\|.
\]
Here the same positive-sum estimate proves that \(1-P_J\) is a contraction. Thus finite truncations converge to \(x\), giving (MF.8). For two such families, the net of cross sums in (MF.7) converges as well: on any finite tail, (MF.5) bounds its norm by the product of the two tail norms. This is the completed inner product.

In particular \(A\), with \(\langle a,b\rangle=a^*b\), is a Hilbert module, and \(A^n\) has norm
\[
 \|(a_i)\|=\left\|\sum_i a_i^*a_i\right\|^{1/2}.
\]
The standard module \(H_A=\bigoplus_{n\in\mathbb N}A\) is defined by norm convergence of \(\sum a_n^*a_n\). It does not require \(\sum\|a_n\|^2<\infty\). Nor does an arbitrary \(A\) make \(H_A\) countably generated.

The scalar unitization acts on every module by
\(x(a+\lambda1)=xa+\lambda x\). Expanding products verifies associativity, and expanding the inner product gives
\[
 \langle x(a+\lambda1),y(b+\mu1)\rangle
 =(a+\lambda1)^*\langle x,y\rangle(b+\mu1).
\]
The coefficient C*-norm inequality therefore gives
\(\|x(a+\lambda1)\|\leq\|x\|\|a+\lambda1\|\).
This justifies the unitized inverses used in later compact-operator proofs, including when the coefficients do not have an identity.

Let \((e_\lambda)\) be a positive contractive approximate identity of \(A\), from the earlier C*-algebra lesson, Corollary 11.5(1). For any \(x\in E\), put \(a=\langle x,x\rangle\). Then
\[
 \langle x-xe_\lambda,x-xe_\lambda\rangle
 =a-ae_\lambda-e_\lambda a+e_\lambda a e_\lambda
 \longrightarrow0
\]
in norm. The first two approximate-identity limits are coefficient-algebra limits; the last follows from contractivity and
\(e_\lambda a e_\lambda-a=e_\lambda(ae_\lambda-a)+(e_\lambda a-a)\).
Hence \(xe_\lambda\to x\), and the linear span of \(EA\) is dense in \(E\). We use precisely this density, without asserting an additional exact single-product factorization theorem.

<a id="mf-004"></a>
## MF.4. Adjointability implies linearity and boundedness

For Hilbert \(A\)-modules \(E,F\), suppose that maps \(T:E\to F\) and \(S:F\to E\) satisfy
\[
 \langle Tx,y\rangle_F=\langle x,Sy\rangle_E
 \qquad(x\in E,\ y\in F).                            \tag{MF.9}
\]
Neither map is assumed linear or bounded. If two maps work as \(S\), subtract their values at \(y\), pair against all \(x\), and then take \(x\) equal to that difference. Definiteness proves uniqueness; write \(S=T^*\). Taking adjoints of coefficient values in (MF.9) shows that \(T\) is the adjoint of \(T^*\).

For \(x,z\in E\), the difference \(T(x+z)-Tx-Tz\) pairs to zero against every \(y\), by additivity of the right-hand side of (MF.9). Pairing against that difference proves additivity of \(T\). The same argument with a complex scalar proves complex homogeneity. For \(a\in A\), both \(T(xa)\) and \((Tx)a\) pair against \(y\) to give
\(a^*\langle x,T^*y\rangle\), proving right \(A\)-linearity. Applying the same reasoning to \(T^*\) gives its linearity.

To check the graph of \(T\), suppose \(x_n\to x\) and \(Tx_n\to z\). For fixed \(y\in F\), (MF.5) gives
\[
 \langle z,y\rangle
 =\lim_n\langle Tx_n,y\rangle
 =\lim_n\langle x_n,T^*y\rangle
 =\langle Tx,y\rangle .
\]
Thus \(z=Tx\). The earlier closed graph theorem (MF.1, Theorem 5.3 of the Banach-space lesson) makes \(T\) bounded; apply it again to \(T^*\). This use of the theorem assumes only the two module spaces' completeness, proved in MF.3, and uses no presumed continuity of the other map.

Write \(\mathcal L(E,F)\) for these maps, with the bounded-map operator norm. Substitution into (MF.9) proves
\[
\begin{gathered}
 (RT)^*=T^*R^*,\qquad (T+U)^*=T^*+U^*,\\
 (\alpha T)^*=\overline\alpha T^*,\qquad (T^*)^*=T.
\end{gathered}\tag{MF.10}
\]
Domains in a composition must agree. The identity of \(E\) has itself as adjoint.

A surjective inner-product-preserving map \(U:E\to F\) is a unitary. It is injective: if \(Ux=Uz\), preservation of all four inner products of \(x,z\) gives \(\langle x-z,x-z\rangle=0\). Thus it has an inverse, and
\[
 \langle Ux,y\rangle
   =\langle Ux,U(U^{-1}y)\rangle
   =\langle x,U^{-1}y\rangle .
\]
MF.4 supplies linearity, module linearity and boundedness from this adjoint relation, and identifies \(U^*=U^{-1}\). Conversely, an adjointable map with \(U^*U=1_E\) and \(UU^*=1_F\) is surjective and preserves inner products by (MF.9). This is the unitary criterion used when completing inner-product-preserving dense constructions.

<a id="mf-005"></a>
## MF.5. The operator C*-algebra and its positive order

For \(T\in\mathcal L(E,F)\), (MF.5) gives
\[
 \|Tx\|^2
 =\|\langle x,T^*Tx\rangle\|
 \leq\|x\|\|T^*Tx\|.
\]
Consequently
\[
 \|T\|^2\leq\|T^*T\|\leq\|T^*\|\|T\|.
\]
If \(T\ne0\), division gives \(\|T\|\leq\|T^*\|\); if \(T=0\), uniqueness makes \(T^*=0\). Applying the same argument to \(T^*\) gives the reverse inequality. Therefore
\[
 \|T^*\|=\|T\|,\qquad
 \|T^*T\|=\|T\|^2,\qquad
 \|TT^*\|=\|T\|^2.                                  \tag{MF.11}
\]

The space of bounded linear maps between Banach spaces is complete: for an operator-norm Cauchy sequence, take its pointwise limits in the complete codomain; the uniform Cauchy estimate passes to the limits, proving boundedness and convergence in operator norm. If \(T_n\) is Cauchy in \(\mathcal L(E,F)\), (MF.11) makes \(T_n^*\) Cauchy too. Let their bounded-map limits be \(T,S\). Passing to the limit in (MF.9), using (MF.5), proves \(S=T^*\). Thus \(\mathcal L(E,F)\) is complete. Together with (MF.10), submultiplicativity of the operator norm and (MF.11), this proves that \(\mathcal L(E)\) is a C*-algebra. For \(E\ne0\) it is unital with identity \(1_E\); for \(E=0\) it is the zero algebra, and all subsequent assertions have their zero interpretation.

We also need \(T^*T\geq0\) when \(T:E\to F\) has different source and target. On \(E\oplus F\), put
\(Q(x,y)=(0,Tx)\); its adjoint is \(Q^*(x,y)=(T^*y,0)\), by (MF.7) and (MF.9). Then \(Q^*Q=\operatorname{diag}(T^*T,0)\geq0\) in \(\mathcal L(E\oplus F)\). The map
\(R\mapsto\operatorname{diag}(R,0)\) embeds \(\mathcal L(E)\) as a closed C*-subalgebra: it is an injective homomorphism, isometric by its action on the first summand. Coefficient spectral permanence in MF.1 therefore reflects positivity, giving \(T^*T\geq0\) in \(\mathcal L(E)\).

All the coefficient C*-algebra calculus of MF.1 now applies to \(\mathcal L(E)\). In particular every \(P\geq0\) has a positive square root and
\[
 \|P^{1/2}\|^2=\|P\|,\qquad
 0\leq T^*T\leq\|T\|^2 1_E.                         \tag{MF.12}
\]
The first is the C*-identity for \(P^{1/2}\); the second is the positive spectral norm bound. If \(R=(\|T\|^2 1_E-T^*T)^{1/2}\), expansion gives the coefficient-order estimate
\[
 \|T\|^2\langle x,x\rangle-\langle Tx,Tx\rangle
       =\langle Rx,Rx\rangle\geq0.                  \tag{MF.13}
\]
It holds for every adjointable \(T:E\to F\), including different modules.

For later positivity tests, we prove the converse as well:
\[
 P\in\mathcal L(E),\qquad
 P\geq0\quad\Longleftrightarrow\quad
 \langle x,Px\rangle\geq0\text{ for every }x\in E.  \tag{MF.14}
\]
If \(P\geq0\), then \(\langle x,Px\rangle=\langle P^{1/2}x,P^{1/2}x\rangle\).
Conversely, the assumed diagonal values are self-adjoint, so the diagonals of
\(b(x,y)=\langle x,(P-P^*)y\rangle\) vanish. A sesquilinear form linear in its second variable satisfies
\[
 4b(x,y)=\sum_{k=0}^3 i^{-k}b(x+i^ky,x+i^ky);
\]
this follows by expanding the four terms. Hence \(b=0\), and pairing \((P-P^*)y\) with itself shows \(P=P^*\).

If a negative spectral value of this self-adjoint operator exists, choose \(\delta>0\) and a real continuous function \(f\) on its spectrum that is nonzero there and vanishes off \(t\leq-\delta\). Functional calculus gives \(f(P)\ne0\), so choose \(y\) with \(x=f(P)y\ne0\). The function
\(g(t)=(-\delta-t)f(t)^2\) is nonnegative. Thus \(g(P)=g(P)^{1/2*}g(P)^{1/2}\), and the already proved forward implication in (MF.14) gives
\[
 \langle x,Px\rangle
 \leq-\delta\langle x,x\rangle.
\]
The hypothesis makes the left side positive. Since the positive cone of \(A\) is proper, this forces \(\langle x,x\rangle=0\), a contradiction. Thus the spectrum is nonnegative and \(P\geq0\). This proof uses only continuous functional calculus in the newly constructed C*-algebra, with no spectral measure theorem.

Finally the vector norm can be tested by inner products:
\[
 \|z\|=\sup_{\|y\|\leq1}\|\langle y,z\rangle\|.      \tag{MF.15}
\]
The upper bound is (MF.5); for \(z\ne0\), take \(y=z/\|z\|\); for \(z=0\) both sides vanish. This formula remains valid for every Hilbert module, including nonfull modules.

<a id="mf-006"></a>
## MF.6. Matrices, finite Gram positivity and amplification

We first construct the coefficient matrix C*-algebra without assuming a unit or using a matrix positivity assertion as a premise. For \(m=(m_{ij})\) with entries in \(A\), define
\[
 (\lambda_n(m)a)_i=\sum_{j=1}^n m_{ij}a_j
 \quad\text{on }A^n.
\]
Coordinate norms satisfy \(\|a_j\|\leq\|a\|\), so
\[
 \|\lambda_n(m)a\|\leq n^{3/2}\max_{i,j}\|m_{ij}\|\|a\|.
\]
Indeed every output coordinate is at most \(n\max\|m_{ij}\|\|a\|\), and the norm of a column is at most the square root of the sum of its coordinate norm squares. Expanding its inner product proves that its adjoint is \(\lambda_n(m^*)\). Matrix multiplication and adjoints therefore agree with operator composition and adjoints.

Using a coordinate column containing \(e_\lambda\), the positive contractive approximate identity of \(A\), proves
\[
 \max_{i,j}\|m_{ij}\|\leq\|\lambda_n(m)\|.
                                                               \tag{MF.16}
\]
Indeed \(\|m_{ij}e_\lambda\|\leq\|\lambda_n(m)\|\), and \(m_{ij}e_\lambda\to m_{ij}\). In particular the map is faithful. If a sequence of these matrix operators is Cauchy in operator norm, (MF.16) makes every entry Cauchy in \(A\). The upper bound just proved makes their entrywise limit the operator-norm limit. Thus the image is a closed C*-subalgebra of \(\mathcal L(A^n)\). With this norm it is \(M_n(A)\). The C*-norm is unique: the identity between any two complete C*-norms on the same algebra is a bijective homomorphism, so contractivity in both directions gives equality. Spectral permanence shows that positivity in this matrix algebra is exactly positivity of its image in \(\mathcal L(A^n)\). This conclusion also holds when \(A=0\), with the zero interpretation. Combining it with (MF.14) gives the full finite matrix test, with no self-adjointness assumption on \(m\):
\[
 m\in M_n(A)_+
 \quad\Longleftrightarrow\quad
 \sum_{i,j}a_i^*m_{ij}a_j\geq0
       \text{ for every }(a_1,\ldots,a_n)\in A^n.
                                                               \tag{MF.16a}
\]

More generally, on a finite direct sum \(E^n\), a matrix \((S_{ij})\) of adjointable maps \(E\to E\) acts by the same finite formula and has adjoint the transposed adjoint matrix. The finite bounds just used give boundedness. Conversely, any \(S\in\mathcal L(E^n)\) has entries
\(S_{ij}=p_i S j_j\), where \(p_i,j_j\) are the adjointable coordinate projection and inclusion from MF.3. On each finite column, this reconstructs \(S\). The resulting algebraic bijection respects products and adjoints, so it identifies
\[
 M_n(\mathcal L(E))=\mathcal L(E^n)               \tag{MF.17}
\]
isometrically, by faithful isometry. This does not assert
\(\mathcal L(A^n)=M_n(A)\) for nonunital \(A\): the latter is the closed subalgebra just constructed.

For \(x_1,\ldots,x_n\in E\), define the row
\[
 V:A^n\longrightarrow E,\qquad
 V(a)=\sum_{j=1}^n x_j a_j.
\]
The bound \(\|V(a)\|\leq\sum_j\|x_j\|\|a\|\) makes it bounded. Its proposed adjoint is
\[
 V^*z=(\langle x_j,z\rangle)_{j=1}^n;
\]
(MF.5) makes this column bounded, with norm at most
\((\sum_j\|x_j\|^2)^{1/2}\|z\|\). Expanding the inner product verifies (MF.9). The operator \(V^*V\) is positive by MF.5, and its coefficient matrix is
\[
 G(x_1,\ldots,x_n)=[\langle x_i,x_j\rangle]_{i,j}
                  \in M_n(A)_+.                   \tag{MF.18}
\]
Positivity reflects from \(\mathcal L(A^n)\) to its matrix C*-subalgebra, as established above. If the original inner product was merely semidefinite, pass first to the quotient and completion in MF.3; its Gram entries are the original entries. Thus (MF.18) holds in that case too.

There is also a useful finite-row norm identity. Let \(R_X:A^n\to E\) and \(R_Y:A^n\to F\) be the rows associated with finite families \(X,Y\), and put \(G_X=R_X^*R_X\), \(G_Y=R_Y^*R_Y\). Applying (MF.11) first to \(K=R_XR_Y^*\), then to \(S=G_X^{1/2}R_Y^*\), gives
\[
 \|K\|^2
 =\|R_YG_XR_Y^*\|
 =\|S^*S\|
 =\|SS^*\|
 =\|G_X^{1/2}G_YG_X^{1/2}\|.                       \tag{MF.18a}
\]
The last norm is the norm in \(M_n(A)\), since its inclusion into \(\mathcal L(A^n)\) is isometric. Applying the same argument to \(K^*\) also gives \(\|K\|^2=\|G_Y^{1/2}G_XG_Y^{1/2}\|\). Thus either finite Gram norm expression used for continuous fields of compact operators follows from the preceding proofs.

If \(T\in\mathcal L(E,F)\), conjugating the positive operator
\(\|T\|^2 1_E-T^*T\) by \(V\) gives
\[
 [\langle Tx_i,Tx_j\rangle]
       \leq\|T\|^2[\langle x_i,x_j\rangle]
       \quad\text{in }M_n(A).                      \tag{MF.19}
\]
The conjugation is positive because
\(V^*RV=(R^{1/2}V)^*(R^{1/2}V)\) for \(R\geq0\), and the difference's entries lie in the matrix subalgebra. This proves the finite matrix estimate needed for tensoring an operator, including nonunital \(A\).

For a possibly degenerate homomorphism \(\phi:A\to\mathcal L(F)\), entrywise application followed by (MF.17) defines
\[
 \phi_n:M_n(A)\longrightarrow\mathcal L(F^n).
\]
Finite matrix expansion verifies its multiplication and adjoint identities. It is contractive by the coefficient C*-algebra homomorphism theorem in MF.1, and it preserves positivity by positive square roots:
\(\phi_n(G)=\phi_n(G^{1/2})^*\phi_n(G^{1/2})\).
Evaluating this positive operator on a column \(y\in F^n\), using (MF.14), gives
\[
 \sum_{i,j}\langle y_i,\phi(\langle x_i,x_j\rangle)y_j\rangle
 \geq0.                                            \tag{MF.20}
\]
Neither nondegeneracy, fullness, unitality nor countability occurs in this reasoning.

For use with two finite tensor sums, even a semidefinite module form gives a positive two-by-two Gram matrix by (MF.18). Its off-diagonal estimate is therefore also available directly: if
\[
 \begin{pmatrix}a&b\\b^*&d\end{pmatrix}\geq0
       \quad\text{in }M_2(A),
\]
work in the unitization, add \(\varepsilon1\) to the first corner and compress by the column
\((-(a+\varepsilon1)^{-1}b,1)^{\mathsf T}\). Matrix multiplication gives
\(d-b^*(a+\varepsilon1)^{-1}b\geq0\).
Functional calculus gives
\((a+\varepsilon1)^{-1}\geq(\|a\|+\varepsilon)^{-1}1\).
Hence
\[
 b^*b\leq(\|a\|+\varepsilon)d,
 \quad\text{and so}\quad b^*b\leq\|a\|d            \tag{MF.21}
\]
by closedness of the positive cone. The coefficient-valued Cauchy–Schwarz of MF.2 was proved before this matrix argument; there is no dependency cycle.

<a id="mf-007"></a>
## MF.7. Rank-one operators

For \(x\in E\) and \(y\in F\), put
\[
 \theta_{x,y}:F\to E,\qquad
 \theta_{x,y}z=x\langle y,z\rangle .
\]
Equations (MF.5) and (MF.6) give
\[
 \|\theta_{x,y}\|\leq\|x\|\|y\|.                    \tag{MF.22}
\]
The coefficient inner-product identities verify
\(\theta_{x,y}^*=\theta_{y,x}\). For compatible module vectors, finite substitution gives
\[
 \theta_{x,y}\theta_{u,v}
       =\theta_{x\langle y,u\rangle,v},\qquad
 T\theta_{x,y}=\theta_{Tx,y},\qquad
 \theta_{x,y}S=\theta_{x,S^*y}.                     \tag{MF.23}
\]
Every identity has matching source and target modules over the same \(A\).

The map \(R_x:A\to E\), \(R_x(a)=xa\), is adjointable, with
\(R_x^*(z)=\langle x,z\rangle\). The upper bound \(\|R_x\|\leq\|x\|\) follows from (MF.6), while \(xe_\lambda\to x\) and \(\|e_\lambda\|\leq1\) from MF.3 give the reverse bound. Therefore
\[
 \theta_{x,x}=R_xR_x^*\geq0,\qquad
 \|\theta_{x,x}\|=\|R_xR_x^*\|=\|x\|^2.             \tag{MF.24}
\]
Positivity of \(R_xR_x^*\) and its norm identity are the rectangular cases already proved in MF.5. These statements establish the rank-one foundation. The compact ideal, its multipliers, countability criteria and strict topology are the next constructions, proved in the graded lesson, Lemma 2.0; they are not assumptions used anywhere above.

<a id="mf-008"></a>
## MF.8. Use before the existing compact and tensor proofs

The compact-module proof in the graded lesson, Lemma 2.0, can now take (MF.22)–(MF.24), the density of coefficient action in MF.3, and the C*-algebra and positive calculus of MF.5 as earlier proved inputs. Its proofs of the compact ideal, multiplier identification, strict topology and countability remain its own. The general double-centralizer theorem remains the first KT–KK lesson's Lemma 2.0.

The ordinary interior tensor proof in the graded lesson, Lemma 6.0a, can take (MF.18)–(MF.20) for positivity, MF.3 for the null quotient and completion, (MF.19) for tensoring adjointable operators, and (MF.21) for its two-by-two estimate. That lesson proves balancing, adjoint formulas on tensors and associativity itself. This companion is required reading before those constructions; neither construction is used in proving this companion.

The assertions here concern ordinary Hilbert modules and their bounded adjointable operators. They do not supply the closed-range or polar-decomposition theorems for general module maps, unbounded regular-operator calculus, module stabilization, exact factorization of a vector as a single coefficient product, or Morita equivalence. Any use of those results requires its separately written programme proof.

## Freely readable primary source and attribution

The mathematical source used for this independently written exposition is Bruce Blackadar, [Operator Algebras: Theory of C*-Algebras and von Neumann Algebras, corrected author edition dated 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf): II.6.3.1, II.6.3.3 and II.6.3.5 for states; II.7.1.1–II.7.1.7 for module inner products, the state proof of Cauchy–Schwarz and completion; and II.7.2.1–II.7.2.7 for adjoints, the operator C*-algebra, module order, rank-one operators and finite amplification. The source abbreviates completion and the operator-algebra proof; MF.3–MF.6 give the full arguments needed here. Its references to other books are not inputs to these proofs.

The PDF is freely readable on the author's site. The [author's publication page](https://www.bruceblackadar.com/mathpubs.html) identifies the edition as revised and corrected, retains author copyright and permits use with attribution under Creative Commons rules. It does not identify a particular licence variant or version. The linked source is not relicensed by this companion's CC0 notice, and its PDF is not redistributed here.

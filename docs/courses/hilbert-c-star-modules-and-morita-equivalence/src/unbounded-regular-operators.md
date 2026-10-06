# Unbounded regular operators

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An unbounded differential operator needs a domain, and its domain is part of the operator. On a Hilbert module, closedness and a densely defined adjoint still do not give all the familiar Hilbert-space consequences. Regularity supplies the missing graph decomposition. It lets us replace an unbounded operator by a bounded contraction without losing its domain, and gives self-adjoint operators resolvents and continuous functional calculus.

We use Adjointable operators, the dense polar-unitary lemma in Kasparov's stabilization theorem, Tensor products and C*-correspondences, and Fredholm operators and the K₀ index. Coefficient algebras and modules are arbitrary unless an additional hypothesis is stated. Inner products are linear in the second variable.

## 1. Domains, adjoints and graphs

A densely defined operator \(T\) on a Hilbert \(A\)-module \(E\) means a right \(A\)-linear operator on a dense \(A\)-submodule \(\operatorname{Dom}T\). Its adjoint has domain
\[
\operatorname{Dom}T^*=
\{y\in E:\ \exists z\in E,\ 
\langle Tx,y\rangle=\langle x,z\rangle
\text{ for all }x\in\operatorname{Dom}T\},
\tag{1.1}
\]
and \(T^*y=z\). Density makes \(z\) unique. The adjoint is closed: convergence of \(y_n\) and \(T^*y_n\) permits passage to the limit in (1.1). When its domain is dense, \(T^{**}\) is defined and extends \(T\).

Closedness means that the graph
\[
G(T)=\{(x,Tx):x\in\operatorname{Dom}T\}\subseteq E\oplus E
\]
is closed. It then has the complete graph inner product
\(\langle x,y\rangle_T=\langle x,y\rangle+\langle Tx,Ty\rangle\).
A core is a submodule of the domain dense for this graph norm.

**Definition 1.1.** A regular operator is closed and densely defined, its adjoint is densely defined, and
\[
\overline{\operatorname{ran}(1+T^*T)}=E.
\tag{1.2}
\]
The domain of the product is
\(\{x\in\operatorname{Dom}T:Tx\in\operatorname{Dom}T^*\}\).
Symmetry means \(T\subseteq T^*\); self-adjointness means equality of operators, including domains.

**Theorem 1.2 (The graph criterion).** Let \(T\) be closed and densely defined, with densely defined adjoint. Put \(v(x,y)=(-y,x)\). Then \(T\) is regular exactly when
\[
E\oplus E=G(T)\oplus vG(T^*)
\tag{1.3}
\]
as an orthogonal direct sum. In that case \(T^{**}=T\), \(T^*\) is regular, and \(1+T^*T\) and \(1+TT^*\) are bijective.

*Proof.* The adjoint definition gives \(G(T)^\perp=vG(T^*)\). The sum of these two closed orthogonal submodules is closed: each component of a sum has norm at most the norm of the sum, by positivity of the inner products, so Cauchy sums have Cauchy components.

For \(x\in\operatorname{Dom}T^*T\),
\[
(x,Tx)+v(-Tx,-T^*Tx)=((1+T^*T)x,0).
\]
Regularity therefore puts \(E\oplus0\) in the closed sum. For \(y\in\operatorname{Dom}T^*\), the vector \(v(y,T^*y)=(-T^*y,y)\) lies in the sum; adding \((T^*y,0)\) puts \((0,y)\) there too. Density of \(\operatorname{Dom}T^*\) proves (1.3).

Conversely, decompose \((z,0)\) as \((x,Tx)+(-T^*y,y)\). The second coordinate gives \(y=-Tx\), so \(x\in\operatorname{Dom}T^*T\) and \(z=(1+T^*T)x\). This proves surjectivity. Injectivity follows from
\[
\langle x,(1+T^*T)x\rangle
=\langle x,x\rangle+\langle Tx,Tx\rangle:
\]
if the left side is zero, positivity forces \(x=0\).

The graph is complemented, so \(G(T)^{\perp\perp}=G(T)\). The adjoint definition identifies this double orthogonal with \(G(T^{**})\); hence \(T^{**}=T\). Apply \(v\) to (1.3), interchange its summands, and repeat the preceding argument for \(T^*\). This proves its regularity and bijectivity of \(1+TT^*\). ∎

Thus regularity is stronger than closedness. The closed graph theorem for everywhere defined Banach-space maps does not assert that an unbounded closed graph is orthogonally complemented.

## 2. Recovering the operator from a contraction

**Theorem 2.1 (Bounded transform).** For regular \(T\), set
\[
h=(1+T^*T)^{-1/2}.
\]
Then \(h\in\mathcal L(E)\), \(hE=\operatorname{Dom}T\), and
\[
F_T=Th\in\mathcal L(E),\qquad
\|F_T\|\leq1,\qquad
F_T^*=F_{T^*},\qquad h^2=1-F_T^*F_T.
\tag{2.1}
\]
The domain \(\operatorname{Dom}T^*T\) is a core for \(T\).

*Proof.* Let \(P\) be the orthogonal graph projection and let
\(j:G(T)\to E\) take the first coordinate. It is adjointable, with
\(j^*z=P(z,0)\). The computation in Theorem 1.2 shows
\[
j j^*=R=(1+T^*T)^{-1}.
\tag{2.2}
\]
In particular this inverse is positive, adjointable and contractive.

Both \(j\) and \(j^*\) have dense range. For \(j\) this is density of the domain. For \(j^*\), observe that
\[
P(0,y)=P(T^*y,0)\quad(y\in\operatorname{Dom}T^*),
\]
because \((-T^*y,y)\) is orthogonal to the graph. Density of that domain and \(P(E\oplus E)=G(T)\) prove the assertion. Hence \(R E=j j^*E\) is dense in \(E\).

Apply the dense polar-unitary lemma to \(j^*:E\to G(T)\). It gives a unitary \(U:E\to G(T)\) with \(j^*=Uh\), where \(h=R^{1/2}\). Taking adjoints gives \(j=hU^*\), so \(jU=h\). Consequently
\[
Ux=(hx,Fx),\qquad F=\operatorname{pr}_2U\in\mathcal L(E).
\tag{2.3}
\]
Surjectivity of \(U\) proves \(hE=\operatorname{Dom}T\), and its graph membership gives \(F=Th\). Its isometry identity gives \(h^2+F^*F=1\). Also \(j^*z=(Rz,TRz)\); density of its range in the graph proves the core assertion.

Apply the same construction to \(T^*\), writing \(l=(1+TT^*)^{-1/2}\) and \(F'=F_{T^*}\). The two graph unitaries together give a unitary
\[
W=\begin{pmatrix}h&-F'\\F&l\end{pmatrix}.
\]
Its bottom-row identity gives \(l^2=1-FF^*\), while orthogonality of its columns gives \(hF'=F^*l\). Functional calculus applied to \(F(F^*F)=(FF^*)F\) gives \(hF^*=F^*l\). Therefore \(h(F'-F^*)=0\). Since \(h\) is positive with dense range, its kernel is zero, and \(F'=F^*\). This proves (2.1).

The notation for \(h\) is justified by the bounded positive inverse (2.2), without assuming an unbounded spectral theorem in advance. Indeed \(R^{-1}\), with domain \(RE\), is self-adjoint: the adjoint identity tested on \(Rx\) says that an adjoint-domain vector \(y\) equals \(Rz\). Thus \(T^*T=R^{-1}-1\) is positive self-adjoint on that domain. ∎

**Theorem 2.2 (Inverse bounded transform).** The map \(T\mapsto F_T\) is a bijection from regular operators to contractions \(F\in\mathcal L(E)\) for which \(1-F^*F\) has dense range. Its inverse is
\[
\operatorname{Dom}T=hE,\qquad T(hx)=Fx,\qquad
h=(1-F^*F)^{1/2}.
\tag{2.4}
\]

*Proof.* Density of \((1-F^*F)E=h^2E\) implies density of \(hE\) and injectivity of \(h\), so (2.4) is well defined on a dense domain. Put \(l=(1-FF^*)^{1/2}\). Polynomial approximation gives
\(Fh=lF\). Thus \(\overline{lE}\) contains \(FE\), since \(hE\) is dense. It contains \(l^2E\) too, and
\(x=FF^*x+l^2x\) proves \(\overline{lE}=E\).

The matrix
\[
W_F=\begin{pmatrix}h&-F^*\\F&l\end{pmatrix}
\tag{2.5}
\]
is unitary, by the defect identities and \(hF^*=F^*l\). Its first column has range exactly the graph in (2.4), so that graph is closed. Its second column is its orthogonal complement. Applying the adjoint definition identifies that complement with
\[
\{(-T^*y,y):y\in\operatorname{Dom}T^*\}
=\{(-F^*x,lx):x\in E\}.
\]
Therefore \(\operatorname{Dom}T^*=lE\) and \(T^*(lx)=F^*x\); in particular the adjoint domain is dense. Theorem 1.2 proves regularity.

The upper-left entry of the graph projection, the product of the first column of \(W_F\) with its adjoint, is \(h^2\). Equation (2.2) then shows \((1+T^*T)^{-1}=h^2\), and \(F_T=Th=F\). Conversely (2.4) recovers any original regular operator by Theorem 2.1. ∎

In particular a regular operator is self-adjoint exactly when its bounded transform is self-adjoint. For a bounded adjointable \(T\), the definition reduces to the ordinary bounded functional calculus and regularity is automatic. A contraction with dense defect need not have an inverse modulus bounded below: that is exactly how an unbounded domain occurs.

## 3. Resolvents and functional calculus

Let \(D=D^*\) be regular, \(F=F_D=F^*\) and \(h=(1-F^2)^{1/2}\). They commute, and \(F^2+h^2=1\).

**Theorem 3.1.** The operators \(D\pm i:\operatorname{Dom}D\to E\) are bijective, with adjointable inverses of norm at most one. There is a nondegenerate *-homomorphism
\[
C_0(\mathbb R)\longrightarrow\mathcal L(E),\qquad f\longmapsto f(D),
\tag{3.1}
\]
given by bounded functional calculus at \(F\).

*Proof.* Since \(F\pm ih\) are mutually inverse unitaries,
\[
(D\pm i)h=F\pm ih,\qquad
(D\pm i)^{-1}=h(F\mp ih).
\tag{3.2}
\]
The range of \(h\) is exactly the domain of \(D\), so these are two-sided inverses on the indicated domains.

The homeomorphism
\[
b(t)=\frac{t}{\sqrt{1+t^2}}:\mathbb R\longrightarrow(-1,1)
\]
identifies \(C_0(\mathbb R)\) with the continuous functions on \([-1,1]\) vanishing at both endpoints. For \(f\in C_0(\mathbb R)\), define
\[
g_f(s)=
\begin{cases}
f\!\left(s/\sqrt{1-s^2}\right),&|s|<1,\\
0,&s=\pm1,
\end{cases}
\qquad f(D)=g_f(F).
\tag{3.3}
\]
Continuity at the endpoints follows from vanishing at infinity. Bounded continuous functional calculus proves the *-homomorphism assertion and \(\|f(D)\|\leq\|f\|_\infty\). For \(f(t)=(1+t^2)^{-1/2}\), its value is \(h\), whose range is dense. Thus (3.1) is nondegenerate. Substituting the two resolvent functions in (3.3) agrees with (3.2). ∎

The same argument for real \(\lambda\ne0\), or substitution in (3.3), gives
\[
(D\pm i\lambda)^{-1}\in\mathcal L(E),\qquad
\|(D\pm i\lambda)^{-1}\|\leq|\lambda|^{-1}.
\tag{3.4}
\]
More explicitly their formula is
\[
(D\pm i\lambda)^{-1}
=h(F\mp i\lambda h)(F^2+\lambda^2h^2)^{-1}.
\]
The last denominator is at least \(\min(1,\lambda^2)1\). Thus \(F\pm i\lambda h\) is invertible, and the displayed inverse has range exactly \(hE=\operatorname{Dom}D\). Multiplication can be checked on that graph parameter; the norm bound follows from the scalar resolvent function.

**Proposition 3.2 (A resolvent criterion).** A closed densely defined symmetric operator \(D\) is self-adjoint and regular if both \(D+i\lambda\) and \(D-i\lambda\) have dense range for one \(\lambda>0\).

*Proof.* Symmetry cancels the mixed terms in
\[
\langle(D\pm i\lambda)x,(D\pm i\lambda)x\rangle
=\langle Dx,Dx\rangle+\lambda^2\langle x,x\rangle.
\]
Thus each is bounded below by \(\lambda\) and has closed range, using closedness of \(D\). The dense ranges are therefore all of \(E\).

If \(y\in\operatorname{Dom}D^*\), choose \(x\in\operatorname{Dom}D\) with
\((D-i\lambda)x=(D^*-i\lambda)y\). Then \(y-x\) lies in the kernel of \(D^*-i\lambda\), which is orthogonal to the surjective range of \(D+i\lambda\). It is zero. Thus \(D=D^*\).

The inverse operators \(r_\pm=(D\pm i\lambda)^{-1}\) are bounded and mutually adjoint, by the defining inner-product identity. They commute, by expanding the resolvent identity; \(R_\lambda=r_+r_-\) is positive, has norm at most \(\lambda^{-2}\), and is the inverse of \(\lambda^2+D^2\) with range \(\operatorname{Dom}D^2\). The bounded positive operator
\[
1+(1-\lambda^2)R_\lambda
\]
is invertible: it is at least \(1\) if \(\lambda\leq1\), and at least \(\lambda^{-2}1\) if \(\lambda\geq1\). Factoring \(1+D^2\) through \(\lambda^2+D^2\) now proves its surjectivity. This is regularity. ∎

**Corollary 3.3 (Bounded self-adjoint perturbations).** If \(D\) is self-adjoint regular and \(V=V^*\in\mathcal L(E)\), then \(D+V\), on \(\operatorname{Dom}D\), is self-adjoint regular.

*Proof.* It is closed, densely defined and symmetric. For \(\lambda>\|V\|\),
\[
D+V\pm i\lambda
=\bigl(1+V(D\pm i\lambda)^{-1}\bigr)(D\pm i\lambda).
\]
The first factor is invertible by the Neumann series, so both ranges are all of \(E\). Proposition 3.2 applies. ∎

## 4. Compact resolvent and bounded Fredholm models

**Theorem 4.1.** For self-adjoint regular \(D\), the following are equivalent:

1. \((1+D^2)^{-1}\in\mathcal K(E)\).
2. \(f(D)\in\mathcal K(E)\) for every \(f\in C_0(\mathbb R)\).
3. Both resolvents \((D\pm i)^{-1}\) are compact.

*Proof.* Write \(r(t)=(1+t^2)^{-1}\). If \(r(D)\) is compact, choose continuous compactly supported cutoffs \(\chi_n\) equal to one on \([-n,n]\). For \(f\in C_0(\mathbb R)\), \(f_n=f\chi_n\) tends uniformly to \(f\), and
\[
f_n(D)=r(D)\bigl((1+t^2)f_n(t)\bigr)(D)
\]
is compact. The ideal is norm closed, proving \(1\Rightarrow2\). The resolvent functions belong to \(C_0(\mathbb R)\), so \(2\Rightarrow3\). Finally
\((1+D^2)^{-1}=(D+i)^{-1}(D-i)^{-1}\), proving \(3\Rightarrow1\). ∎

When these conditions hold, \(1-F_D^2\) is compact, so \(F_D\) is Fredholm with itself as a parametrix. Its ungraded endomorphism index is zero: \(F_D+i(1-F_D^2)\) is an invertible compact perturbation, since \(s+i(1-s^2)\) has no zero on \([-1,1]\). In the graded case the useful even index comes instead from the off-diagonal component: if
\[
E=E^+\oplus E^-,\qquad
F_D=\begin{pmatrix}0&(F_D^+)^*\\F_D^+&0\end{pmatrix},
\]
then the two diagonal compact defects show that \(F_D^+:E^+\to E^-\) is Fredholm. For countably generated modules its index is the Fredholm-triple class developed in the preceding lesson.

Global compact resolvent is stronger than the condition needed for an unbounded Kasparov module. If \(\phi:C\to\mathcal L(E)\) is a left action, the local condition is
\[
\phi(c)(1+D^2)^{-1}\in\mathcal K(E)\quad(c\in C).
\tag{4.1}
\]
Equivalently \(\phi(c)h\) is compact for every \(c\): indeed
\[
\left\|h-h^2(h+\varepsilon)^{-1}\right\|\leq\varepsilon
\]
shows one implication by norm approximation, and multiplication by \(h\) gives the other. If \(C\) is unital and acts unitally, taking \(c=1\) recovers global compact resolvent. It cannot be recovered that way for a general nonunital left algebra.

For a countably generated graded \(E\), an even action \(\phi\), an odd self-adjoint regular \(D\), and a dense *-subalgebra \(\mathcal C\subseteq C\) preserving \(\operatorname{Dom}D\) with bounded adjointable commutators \([D,\phi(c)]\), condition (4.1) gives a bounded Kasparov module \((E,\phi,F_D)\). Here this means that \(F_D\) is odd and self-adjoint and that
\[
(1-F_D^2)\phi(c),\quad [F_D,\phi(c)]
\quad\text{are compact for all }c\in C.
\tag{4.2}
\]
The exact programme dependency for this general local-compactness implication is *Unbounded Kasparov modules and spectral triples*, Section 2, in *Kasparov’s KK-theory*. Its assigned proof is planned and concerns precisely self-adjoint regular odd operators, local compactness and bounded commutators on a dense algebra. The graph and regularity results it needs are proved here independently; the planned transform proof is not used in those arguments. Blackadar, Proposition 17.11.3, and Mesland, Section 2.2, credit Baaj–Julg’s theorem. We do not import the assertion that global compact resolvent is necessary.

For comparison, we can prove the commutator assertion directly in the global compact-resolvent case. Write \(a=\phi(c)\), \(B=[D,a]\) for \(c\in\mathcal C\), and \(q=\sqrt{1+\lambda^2}\). Domain preservation gives
\[
[(D\pm iq)^{-1},a]=-(D\pm iq)^{-1}B(D\pm iq)^{-1}.
\tag{4.3}
\]
Both factors are compact by Theorem 4.1, and the norm is at most \(\|B\|/q^2\). Since
\[
D(D^2+q^2)^{-1}
=\tfrac12\bigl((D-iq)^{-1}+(D+iq)^{-1}\bigr),
\]
its commutator has the same bound and is compact. The scalar identity
\[
\frac{t}{\sqrt{1+t^2}}
=\frac2\pi\int_0^\infty\frac{t}{1+t^2+\lambda^2}\,d\lambda
\tag{4.4}
\]
now makes \([F_D,a]\) a norm-convergent integral of compact commutators: the bound \(\|B\|/(1+\lambda^2)\) is integrable.

To justify identifying that integral with the commutator, truncate (4.4) at \(R\). The resulting functions belong to \(C_0(\mathbb R)\), are bounded by one, and converge uniformly on every compact interval to \(b(t)\). Their functional calculi converge pointwise on \(E\) to \(F_D\): first test on \(g(D)E\) for \(g\in C_0(\mathbb R)\), using uniform convergence of the products, then use the dense span from Theorem 3.1. Thus the norm limit of their commutators equals \([F_D,a]\). Norm density of \(\mathcal C\) gives (4.2) for all \(c\). This proof requires no domain preservation for \(D^2\).

## 5. Extending coefficients

**Theorem 5.1.** Let \(D\) be self-adjoint regular on a Hilbert \(A\)-module \(E\), and let \(G\) be an \(A\)-\(B\) correspondence. The algebraic operator
\[
D\odot1:\operatorname{Dom}D\odot_A G\longrightarrow E\otimes_A G,
\qquad x\otimes y\longmapsto Dx\otimes y
\tag{5.1}
\]
has a self-adjoint regular closure \(D_G\). Moreover
\[
F_{D_G}=F_D\otimes1,\qquad f(D_G)=f(D)\otimes1
\quad(f\in C_0(\mathbb R)).
\tag{5.2}
\]
The left action on \(G\) may be degenerate.

*Proof.* Tensoring adjointable operators gives a unital *-homomorphism
\(\Psi:\mathcal L(E)\to\mathcal L(E\otimes_A G)\), with the usual trivial interpretation if the tensor module is zero. Set \(F'=\Psi(F_D)\), \(h'=\Psi(h)\). Functional calculus gives \(h'=(1-(F')^2)^{1/2}\). Its range is dense: approximate any elementary tensor \(x\otimes y\) by \(hz_n\otimes y=h'(z_n\otimes y)\), since \(hE\) is dense. Its square has dense range as well, either by the same argument for \(h^2E\), or by positive regularization. Theorem 2.2 defines a self-adjoint regular \(D_G\) with \(D_G(h'z)=F'z\).

Every \(x\in\operatorname{Dom}D\) is \(hu\), so
\[
(x\otimes y,Dx\otimes y)
=(h'(u\otimes y),F'(u\otimes y)).
\]
These pairs lie in \(G(D_G)\). In particular null vectors in the balanced tensor quotient give zero values, so the algebraic operator is well defined. The column \((h',F')\) is a unitary from the tensor module onto this graph; elementary \(u\otimes y\) span a dense submodule. Hence the displayed algebraic graph is dense in the full graph, proving the closure assertion. Formula (3.3), and preservation of bounded continuous functional calculus by \(\Psi\), prove (5.2). ∎

Compact resolvent need not survive this construction without a condition on the correspondence. If the left action of \(A\) is compact and \(D\) has compact resolvent, tensor compactness from the preceding tensor-product lesson makes \(f(D_G)\) compact. For a general left action that conclusion fails. For example, tensor the zero operator on \(\mathbb C\) with an infinite-dimensional Hilbert space; the resulting zero operator has identity resolvent, which is not compact.

## 6. Multipliers and differential-operator families

**Example 6.1 (Continuous multiplication).** Let \(X\) be locally compact Hausdorff and \(m:X\to\mathbb R\) continuous. On \(E=C_0(X)\), define
\[
\operatorname{Dom}D_m=\{a\in C_0(X):ma\in C_0(X)\},\qquad D_ma=ma.
\tag{6.1}
\]
Compactly supported continuous functions give a dense domain. The operator is closed: uniform convergence of \(a_n\) and \(ma_n\) identifies the limit pointwise with multiplication by \(m\). Testing the adjoint identity against compactly supported functions gives \(D_m^*b=mb\), with exactly the same domain. The bounded continuous functions
\[
\frac1{m\pm i},\qquad
\frac1{1+m^2},\qquad
\frac{m}{\sqrt{1+m^2}}
\]
act adjointably as multipliers. The first two supply the resolvents and the inverse of \(1+D_m^2\); thus \(D_m\) is self-adjoint regular and the last is its bounded transform.

Since \(\mathcal K(C_0(X))=C_0(X)\), it has compact resolvent exactly when \(m\) is proper. Indeed \((1+m^2)^{-1}\) vanishes at infinity exactly when every set \(\{|m|\leq R\}\) is compact. Multiplication by \(x\) on \(C_0(\mathbb R)\) is the simplest instance. Unboundedness of \(m\) alone does not imply properness: \(m(x,y)=x\) on \(\mathbb R^2\) has noncompact strips.

**Example 6.2 (Momentum over a parameter space).** On \(H=L^2(\mathbb R)\), let
\[
P=\mathcal F^{-1}M_\xi\mathcal F,\qquad
\operatorname{Dom}P=\{u\mid \xi\widehat u\in L^2(\mathbb R)\},
\]
where \(\mathcal F u(\xi)=(2\pi)^{-1/2}\int e^{-ix\xi}u(x)\,dx\) initially on \(L^1\cap L^2\). Its unitary extension is The Plancherel theorem, Theorem 1.1, with the angular-frequency normalization (22).

Here is the weak-derivative identification needed in this example. For a Schwartz function, integration by parts gives \(\mathcal F(-iu')=\xi\mathcal Fu\); differentiating under the integral and integrating by parts also show that the transform preserves the Schwartz test space. For \(u,g\in L^2\), the equation \(u'=g\) in distributions means \(\int u\varphi'=-\int g\varphi\) for compactly supported smooth tests. It remains true for Schwartz tests by multiplying them by cutoffs tending to one: their derivatives converge in \(L^2\), so both pairings converge. Unitarity and the Schwartz identity transfer this equality to \(\xi\widehat u=-i\widehat g\) as a distribution. Conversely that multiplier equality transfers back to the weak-derivative equation. An \(L^2\) function defines the zero distribution only if it is zero almost everywhere, since smooth compactly supported functions are dense in \(L^2\) (approximate step functions on finite intervals by smooth cutoffs). Consequently \(u\) has an \(L^2\) weak derivative exactly when \(\xi\widehat u\in L^2\), and \(P=-i\,d/dx\) has domain \(H^1(\mathbb R)\). Teschl, Theorem 7.5 and (7.12)–(7.15), gives the classical comparison.

Multiplication by \(\xi\) on \(L^2\) is self-adjoint: the adjoint identity on compactly supported test vectors forces the same maximal multiplication domain. It is closed by an almost-everywhere subsequence argument, and multiplication by \((\xi\pm i)^{-1}\) gives surjective resolvents. Thus it is regular, either by Proposition 3.2 or directly by the multiplier inverse of \(1+\xi^2\).

For any locally compact Hausdorff \(X\), consider \(C_0(X,H)\). The correspondence construction of Theorem 5.1, applied to \(H\) and \(C_0(X)\), gives the constant momentum family
\[
(\mathcal P u)(s)=Pu(s),\qquad
\operatorname{Dom}\mathcal P
=\{u\in C_0(X,H):u(s)\in H^1,\ Pu\in C_0(X,H)\}.
\tag{6.2}
\]
The equality of this domain with the tensor-domain closure follows from the graph unitary \((h,F)\): a section satisfying the right side has graph parameter \(hu+F\mathcal P u\), since \(h^2+F^2=1\). Its resolvents act pointwise by the constant bounded Hilbert-space resolvents. This is a self-adjoint regular differential-operator family.

It does not have compact resolvent when \(X\ne\varnothing\). On \(L^2(\mathbb R)\), the nonzero multiplier \((1+\xi^2)^{-1}\) is not compact: choose infinitely many disjoint measurable subsets in an interval where it is bounded below and their normalized characteristic vectors. Their images are orthogonal with a uniform positive norm. A module compact induces a compact operator on each evaluation fibre, by the rank-one fibre formula, so the family resolvent cannot be compact.

**Example 6.3 (Circle Dirac families).** On \(H=\ell^2(\mathbb Z)\), put \(D_0 e_n=n e_n\). Its domain consists of square-summable vectors with \((n u_n)\) square summable. The diagonal contraction and inverse modulus
\[
F_0e_n=\frac n{\sqrt{1+n^2}}e_n,\qquad
h_0e_n=\frac1{\sqrt{1+n^2}}e_n
\]
satisfy Theorem 2.2: finite coordinate vectors show dense defect range. Thus \(D_0\) is self-adjoint regular. Its resolvent is compact, since diagonal entries tend to zero and truncations converge in norm. On finite sequences the coefficient map to trigonometric polynomials sends \(D_0\) to \(-i\,d/d\theta\), since \(-i\,d(e^{in\theta})/d\theta=n e^{in\theta}\). Orthogonality of these modes for normalized circle measure gives exactly the \(\ell^2\) norm. The Hilbert completion of these polynomials is the circle Dirac model used here.

For compact Hausdorff \(X\), the constant family on \(C(X,H)\) is self-adjoint regular with compact resolvent. Its finite diagonal truncations are module compact: constant coordinate vectors provide the required finite rank-one sums. Adding any norm-continuous bounded self-adjoint potential family \(V_s\) gives a regular family \(D_0+V_s\), by Corollary 3.3. Its resolvent remains compact: for \(\lambda>\sup_s\|V_s\|\), the inverse is
\[
(D_0\pm i\lambda)^{-1}
\bigl(1+V(D_0\pm i\lambda)^{-1}\bigr)^{-1},
\]
which is compact; the resolvent identity then gives compactness at \(i\). These are explicit varying Dirac-type families, without an appeal to a general elliptic-family theorem.

On a noncompact parameter space the same constant circle family has only local compactness. To see why its resolvent is not module compact, observe that a rank-one section operator has fibre norm at most \(\|x(s)\|\|y(s)\|\), which vanishes at infinity. Finite sums have the same property, and norm limits preserve it, since evaluation is contractive. Thus every module compact has fibre norms vanishing at infinity. The constant resolvent has a nonzero constant fibre norm, so fails this necessary condition. Multiplying by \(a\in C_0(X)\) makes its finite diagonal approximations compact: factor each scalar coefficient function as a product of two \(C_0(X)\) functions and use rank-one section operators. Norm convergence of the diagonal truncations proves \(a(1+D_0^2)^{-1}\) compact. This illustrates (4.1).

## 7. A closed symmetric operator that is not regular

Let \(A=C([0,1])\), \(H=\ell^2(\mathbb N)\) and \(E=C([0,1],H)\). Write \(D_0e_n=n e_n\) on \(H\), and let \(\mathcal D\) be its constant self-adjoint regular family. Its domain consists of sections \(\xi\) for which \((n\xi_n)\) is again a continuous \(H\)-valued section. This follows from the same diagonal graph parameter used in Example 6.3.

On \(\operatorname{Dom}D_0\), the linear functional
\[
\ell(u)=\sum_{n\geq1}u_n
\]
is continuous in the graph norm, since
\[
|\ell(u)|\leq
\left(\sum_{n\geq1}n^{-2}\right)^{1/2}\|D_0u\|.
\tag{7.1}
\]
It is not continuous in the Hilbert norm. Define the restriction
\[
\operatorname{Dom}T
=\{\xi\in\operatorname{Dom}\mathcal D:\ell(\xi(0))=0\},
\qquad T\xi=\mathcal D\xi.
\tag{7.2}
\]

**Proposition 7.1.** This \(T\) is closed, densely defined and symmetric, its adjoint is densely defined, but \(T\) is not regular.

*Proof.* The constraint in (7.2) is graph continuous by (7.1), so the restriction is closed. It is an \(A\)-submodule constraint because multiplication changes the boundary functional by the scalar \(a(0)\). It is symmetric as a restriction of \(\mathcal D\).

To prove density, first approximate any continuous section uniformly by finitely many coordinates; uniformity follows from compactness of its image in \(H\). For a section supported in its first \(m\) coordinates, put \(c=\ell(\xi(0))\), and subtract the constant finite-coordinate section
\[
\frac cN\sum_{n=m+1}^{m+N}e_n.
\]
The new section belongs to \(\operatorname{Dom}T\) and differs by \(|c|/\sqrt N\) in the module norm. Let \(N\to\infty\), proving density.

We claim \(T^*=\mathcal D\). Inclusion \(\mathcal D\subseteq T^*\) follows from symmetry of the original self-adjoint family. Conversely, let \(y\in\operatorname{Dom}T^*\) with \(z=T^*y\in E\). At any \(s>0\), test the adjoint identity against finite-coordinate sections supported away from zero. It gives \(z_n(s)=n y_n(s)\) for every \(n\). Continuity extends these equalities to \(s=0\). Since \(z\) is a continuous \(H\)-valued section, \(y\in\operatorname{Dom}\mathcal D\) and \(\mathcal D y=z\). This proves the claim.

In particular \(T^{**}=\mathcal D\ne T\): the constant section \(e_1\) belongs to the former domain and violates the boundary constraint of the latter. The graph criterion already disproves regularity.

We can see the failure in (1.2) directly. Let \(R=(1+\mathcal D^2)^{-1}\), the diagonal operator with entries \((1+n^2)^{-1}\). Then
\[
\operatorname{ran}(1+T^*T)
=\{g\in E:\ell((Rg)(0))=0\}.
\tag{7.3}
\]
Indeed \(\operatorname{Dom}T^*T=\operatorname{Dom}\mathcal D^2\cap\operatorname{Dom}T\), and \(R\) is the inverse of \(1+\mathcal D^2\) onto that domain before the constraint. The functional in (7.3) is a nonzero bounded functional on \(E\), since its coefficient sequence \(((1+n^2)^{-1})\) is square summable. Its kernel is a proper closed hyperplane, so the range is not dense. ∎

The example has a dense adjoint domain and a proper closed range for \(1+T^*T\), isolating the regularity condition.

For a closed densely defined symmetric \(T\), one can test the missing condition on Hilbert spaces. For a state \(\omega\) of \(A\), form the scalar-inner-product completion of \(E\) using \(\omega(\langle x,y\rangle)\). The localization \(T^\omega\) is the closure of the operator induced on the image of \(\operatorname{Dom}T\). Symmetry makes it well defined and closable by testing against the dense image of that domain. The local-global theorem says
\[
T\text{ is self-adjoint and regular}
\quad\Longleftrightarrow\quad
T^\omega\text{ is self-adjoint for every state }\omega.
\tag{7.4}
\]
We now prove this criterion, including the separation step responsible for the quantifier “every state.” The result is due to Kaad–Lesch [Theorem 4.2(2)].

**Lemma 7.2 (A state detects a proper closed submodule).** If \(F\subset E\) is a closed right submodule and \(y\notin F\), there is a state \(\omega\) of \(A\) for which the image of \(y\) is outside the closure of the image of \(F\) in the scalar completion \(E^\omega\).

*Proof.* Put \(d=\operatorname{dist}(y,F)>0\). In the real Banach space \(A_{\mathrm{sa}}\), consider the convex set
\[
\begin{aligned}
\mathcal C&=\operatorname{conv}
\{\langle y-x,y-x\rangle:x\in F\}\\
&\quad+A_+.
\end{aligned}
\tag{7.5}
\]
Every element of this set has norm at least \(d^2\). Indeed, for nonnegative weights \(t_j\) summing to one, set \(\bar x=\sum_jt_jx_j\in F\). Expansion gives
\[
\begin{aligned}
&\sum_jt_j\langle y-x_j,y-x_j\rangle\\
&=\langle y-\bar x,y-\bar x\rangle\\
&\quad+\sum_jt_j\langle x_j-\bar x,x_j-\bar x\rangle.
\end{aligned}
\tag{7.6}
\]
The remaining terms are positive, so order monotonicity of the norm gives the bound. The closed convex hull therefore also avoids the open ball of radius \(d^2\) about zero. Real Hahn–Banach separation supplies a nonzero bounded real functional \(f\) and \(c>0\) with \(f(b)\geq c\) on \(\mathcal C\). Because \(\mathcal C+A_+=\mathcal C\), adding arbitrary positive multiples of a positive element forces \(f(A_+)\geq0\). Its complex extension is a positive functional. Normalize it to the state \(\omega=f/\|f\|\). Then
\[
\begin{gathered}
\|y^\omega-x^\omega\|^2\\
=\omega(\langle y-x,y-x\rangle)\\
\geq c/\|f\|>0\quad(x\in F).
\end{gathered}
\tag{7.7}
\]
Thus the image of \(F\) is not dense at \(y^\omega\). No orthogonal projection onto \(F\) was assumed. ∎

**Theorem 7.3 (Local-global self-adjoint regularity).** Equivalence (7.4) holds for every closed densely defined symmetric operator on every Hilbert C*-module.

*Proof.* For such a \(T\), symmetry gives
\[
\begin{gathered}
\langle(T\pm i)x,(T\pm i)x\rangle\\
=\langle Tx,Tx\rangle+\langle x,x\rangle.
\end{gathered}
\tag{7.8}
\]
Consequently \(\|(T\pm i)x\|\geq\|x\|\). Each range \(F_\pm=\operatorname{ran}(T\pm i)\) is closed: if \((T\pm i)x_n\) converges, the estimate makes \(x_n\) Cauchy, and \(Tx_n=(T\pm i)x_n\mp ix_n\) converges too. Closedness of \(T\) supplies the limit in its graph. These ranges are right submodules.

Assume every closed localization \(T^\omega\) is self-adjoint. If \(F_+\ne E\), Lemma 7.2 supplies a state with nondense image of \(F_+\). But the graph-core definition of \(T^\omega\) makes
\[
\overline{\operatorname{ran}(T^\omega+i)}
=\overline{(F_+)^\omega}.
\tag{7.9}
\]
Both inclusions follow by approximating a localized graph vector by images of original domain vectors. A self-adjoint Hilbert-space operator has surjective \(T^\omega+i\), contradicting (7.9). The same argument applies to \(F_-\). Both original ranges are therefore all of \(E\), and Proposition 3.2 makes \(T\) self-adjoint and regular.

Conversely, self-adjoint regularity gives bounded adjointable resolvents \((T\pm i)^{-1}\). The operator order estimate for adjointable maps makes their scalar localizations bounded. Approximate a scalar-completion vector by images of module vectors. Applying a resolvent to these approximants gives a convergent sequence whose operator images also converge, so the closed localization has both resolvents and both ranges equal to the whole scalar Hilbert space. It is closed and symmetric; surjectivity of the two shifted operators implies Hilbert-space self-adjointness. Thus every \(T^\omega\) is self-adjoint. The zero module is immediate. ∎

The criterion concerns closed localizations and all states. This proof does not replace them by pure states. Its mechanism is that a missing module range is detected by a positive separating functional, even when the submodule has no orthogonal complement.

## 8. Exercises with solutions

**Exercise 8.1 (Basic: multiplication).** Show that multiplication by a continuous real function \(m\), possibly unbounded, is self-adjoint regular on \(C_0(X)\).

*Solution.* Use the maximal domain (6.1). It contains \(C_c(X)\), so is dense; uniform limits in the graph identify the product pointwise and prove closedness. The adjoint identity tested on \(C_c(X)\) forces \(mb\in C_0(X)\) and gives \(D_m^*b=mb\), so the adjoint has precisely the original domain. Multiplication by \((m\pm i)^{-1}\) maps \(C_0(X)\) into that domain, because \(m/(m\pm i)\) is bounded continuous, and supplies both inverse resolvents. Proposition 3.2 proves regularity. Its bounded transform is multiplication by \(m/\sqrt{1+m^2}\). ∎

**Exercise 8.2 (Intermediate: the transformed adjoint).** Prove \(F_T^*=F_{T^*}\).

*Solution.* The graph unitaries give
\[
W=\begin{pmatrix}h&-F_{T^*}\\F_T&l\end{pmatrix}
\]
unitary, with \(h^2=1-F_T^*F_T\), \(l^2=1-F_TF_T^*\) and
\(hF_{T^*}=F_T^*l\). Polynomial approximation of square roots in
\(F_T(F_T^*F_T)=(F_TF_T^*)F_T\) also gives \(hF_T^*=F_T^*l\). Subtracting gives \(h(F_{T^*}-F_T^*)=0\). Dense range of the positive \(h\) implies its kernel is zero, so the two operators agree. The identity compares bounded transforms; it does not assume equality of the two unbounded domains. ∎

**Exercise 8.3 (Intermediate: compact-resolvent tests).** Prove the equivalence of the first two conditions of Theorem 4.1.

*Solution.* If every \(f(D)\) is compact, choose \(f(t)=(1+t^2)^{-1}\). Conversely approximate an arbitrary \(f\in C_0(\mathbb R)\) uniformly by \(f_n=f\chi_n\) with compact support. Each \((1+t^2)f_n(t)\) is in \(C_0(\mathbb R)\), so the homomorphism property gives
\[
f_n(D)=(1+D^2)^{-1}\bigl((1+t^2)f_n(t)\bigr)(D).
\]
The product is compact. Contractivity of the calculus makes \(f_n(D)\to f(D)\) in norm, and the compact ideal is norm closed. No discrete-spectrum claim for Hilbert modules is required. ∎

**Exercise 8.4 (Advanced: tensoring a regular operator).** Prove self-adjoint regularity of the closure of \(D\odot1\) for an arbitrary correspondence.

*Solution.* Tensor the self-adjoint contraction \(F_D\) and its positive inverse modulus \(h\), giving \(F'=F_D\otimes1\) and \(h'=h\otimes1\). The tensor *-homomorphism preserves \(h'^2=1-(F')^2\). The range of \(h'^2\) is dense because \(h^2E\) is dense and every elementary tensor is approximated by \((h^2x)\otimes y\). The inverse bounded-transform theorem gives a self-adjoint regular \(D'\) on \(h'(E\otimes_A G)\), with \(D'h'z=F'z\).

For \(x=hu\), its elementary graph pair is
\((x\otimes y,Dx\otimes y)=(h'(u\otimes y),F'(u\otimes y))\).
The column \((h',F')\) is a graph unitary, so these pairs span a dense submodule of \(G(D')\). Thus \(D'\) is exactly the closure of the algebraic operator, including the balanced null quotient. Nondegeneracy or compactness of the left action is unnecessary for this regularity result. Compactness of the resolvent needs the additional compact-action hypothesis discussed after Theorem 5.1. ∎

## What this lesson does not prove

The prerequisites supply bounded C*-algebra functional calculus, adjointable graph-coordinate maps on complemented modules, the dense polar-unitary lemma [*Kasparov's stabilization theorem*, Lemma 2.2], tensoring of adjointable maps and its compact-action criterion [*Tensor products and C*-correspondences*, Theorems 2.1 and 2.4], and the Fredholm-triple index. We prove the graph criterion, both directions of the bounded-transform correspondence, adjoint comparison, resolvents, continuous unbounded functional calculus, compact-resolvent equivalence and coefficient extension here.

The general Baaj–Julg passage from local compactness and bounded commutators to a bounded Kasparov module has the exact planned programme provider *Unbounded Kasparov modules and spectral triples*, Section 2, with the statement and dependency direction specified in Section 4 here. We prove its globally compact-resolvent commutator case, but not the classification of all KK-classes by unbounded cycles or the unbounded Kasparov product.

The written Fourier prerequisite is The Plancherel theorem, Theorem 1.1 and normalization (22). Example 6.2 proves its identification of weak differentiation with multiplication; Teschl remains a classical reference. The local-global regularity criterion and its state-separation lemma are proved in Section 7. Our symmetric nonregular example is proved directly. We do not invoke a general elliptic-family regularity theorem, Sobolev calculus on smooth operator modules, or the stronger notion of regularity of a spectral triple defined by iterated commutators.

## References

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Definition 13.3.1, Proposition 13.3.2 and Section 17.11. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Mesland 2013] Bram Mesland, “Spectral triples and KK-theory: a survey,” the section “C*-modules and regular operators.” [Author's preprint](https://arxiv.org/abs/1304.3802).

[Mesland 2009] Bram Mesland, “Unbounded bivariant K-theory and correspondences in noncommutative geometry,” *Journal für die reine und angewandte Mathematik* 691 (2014), 101–172, Sections 1.3, 2.2 and 4.5. [Author's preprint](https://arxiv.org/abs/0904.4383).

[Kaad–Lesch] Jens Kaad and Matthias Lesch, “A local global principle for regular operators in Hilbert C*-modules,” *Journal of Functional Analysis* 262 (2012), 4540–4569, Theorem 4.2. [Author's version](https://www.math.uni-bonn.de/people/lesch/dl/pap/2011-KaaLes-ArXiv-v2.pdf).

[Teschl] Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, first edition, American Mathematical Society, 2009, Section 7.1. [Author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).

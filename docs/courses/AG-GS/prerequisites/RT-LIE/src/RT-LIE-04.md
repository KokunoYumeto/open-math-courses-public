# Complete reducibility: Casimir elements and Weyl's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An invariant subspace need not have an invariant complement. Semisimplicity of the acting Lie algebra makes every finite-dimensional extension split in characteristic zero. The mechanism in this lesson is an operator made by contracting a representation against its own trace form. First it splits an extension with a one-dimensional quotient; a space of linear maps then converts that special case into every case.

The prerequisite is [The Killing form and Cartan's criteria](RT-LIE-03.md), together with the enveloping-algebra construction in [Lie algebras: definitions, examples and first constructions](RT-LIE-01.md). Lie algebras and modules are finite-dimensional until Section 6. The main course works over \(\mathbb C\); the Casimir scalar assertion below holds over any algebraically closed characteristic-zero field. Weyl's theorem, the basic Casimir construction, its adjoint normalization and preservation of Jordan decomposition are proved over every characteristic-zero field.

References for comparison are [Milne, Lie algebras], [Milne, Algebraic groups] and [Gruson–Serganova]. The normalization of the adjoint Casimir is also used in [Deligne, p. 321].

## 1. What an invariant complement means

A module is **simple** or **irreducible** if it is nonzero and has no proper nonzero submodule. It is **completely reducible** if it is a direct sum of simple modules.

**Lemma 1.1.** For a finite-dimensional module over any Lie algebra and any field, the following conditions are equivalent:

1. It is a sum of simple submodules.
2. It is a direct sum of simple submodules.
3. Every submodule has a submodule complement.

**Proof.** If a module is a sum of simple submodules, build a direct sum by adding a simple summand outside the sum already chosen. Its intersection with that sum is zero, because it is a submodule of a simple module and cannot be the entire simple module. Each addition increases dimension, so the process reaches the whole module. This proves \(1\Rightarrow2\); the reverse is immediate.

Suppose \(M=\sum S_i\) with every \(S_i\) simple, and let \(W\subseteq M\) be a submodule. Start with \(T=0\), so \(W\cap T=0\). If \(W+T\ne M\), some \(S_i\) is not contained in \(W+T\). Simplicity makes \(S_i\cap(W+T)=0\), so replacing \(T\) by \(T\oplus S_i\) preserves \(W\cap T=0\). Finite dimension eventually gives \(M=W\oplus T\). Thus \(1\Rightarrow3\).

For \(3\Rightarrow2\), choose a nonzero submodule of least dimension; it is simple. It has a complement. Every submodule of the complement also has a complement inside it: intersect a complement in \(M\) with that first complement, and use the direct-sum decomposition to check the claim. Induction on dimension now expresses the complement, and therefore \(M\), as a direct sum of simple modules. The zero module is the empty sum. \(\square\)

A semisimple Lie algebra is perfect, by the preceding lesson: \([\mathfrak g,\mathfrak g]=\mathfrak g\). Consequently all its one-dimensional modules are trivial. Indeed, the scalar action is a linear map \(\chi:\mathfrak g\to k\), and \(\chi([x,y])=[\chi(x),\chi(y)]=0\). Perfectness makes \(\chi=0\).

Complete reducibility of the adjoint module alone does not imply semisimplicity of the algebra. A nonzero one-dimensional abelian algebra has a trivial, simple adjoint module, but its radical is the entire algebra. This supplies a counterexample to the converse stated in [Milne, Lie algebras, Theorem 5.20(a)]. Weyl's theorem below asserts the forward direction with its characteristic-zero condition.

We shall also use Schur's lemma in its scalar version, with its field condition included.

**Lemma 1.2.** On an irreducible finite-dimensional module over an algebraically closed field, every commuting endomorphism is scalar.

**Proof.** Such an endomorphism \(T\) has an eigenvalue \(a\). The nonzero kernel of \(T-a1\) is a submodule because \(T\) commutes with the action; irreducibility makes that kernel the entire module. Thus \(T=a1\). \(\square\)

Over a field that is not algebraically closed, a commuting endomorphism need not be scalar. For example, the real operator \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) makes \(\mathbb R^2\) an irreducible module for a one-dimensional real Lie algebra; \(J\) commutes with its action and is not a real scalar. The characteristic-zero descent argument in Section 4 will not use the scalar assertion over that field.

## 2. Contracting a representation against a bilinear form

Let \(B\) be a nondegenerate invariant symmetric bilinear form on \(\mathfrak g\). For a basis \(x_1,\ldots,x_d\), write \(y_1,\ldots,y_d\) for its \(B\)-dual basis:
\[
B(x_i,y_j)=\delta_{ij}.
\]
The element
\[
\Omega_B=\sum_i x_i\otimes y_i\in\mathfrak g\otimes\mathfrak g
\tag{2.1}
\]
is independent of the basis and invariant under the diagonal adjoint action.

To see both claims, identify \(\mathfrak g\otimes\mathfrak g\) with \(\operatorname{End}(\mathfrak g)\) by
\[
u\otimes v\longmapsto\bigl(z\longmapsto uB(v,z)\bigr).
\]
Nondegeneracy makes this an isomorphism: in a dual pair of bases these are precisely matrix units. The tensor (2.1) corresponds to the identity. Invariance of \(B\) gives
\(B([a,v],z)=-B(v,[a,z])\), so the tensor action of \(a\) corresponds to commutator with \(\operatorname{ad}a\). The identity commutes with it. Thus
\[
\sum_i[a,x_i]\otimes y_i+x_i\otimes[a,y_i]=0.
\tag{2.2}
\]

**Proposition 2.1 (Casimir construction).** Multiplication in \(U(\mathfrak g)\) sends this tensor to a central, basis-independent element
\[
C_B=\sum_i x_i y_i.
\tag{2.3}
\]
In any representation \(\rho\), the operator
\[
c_B=\sum_i\rho(x_i)\rho(y_i)
\tag{2.4}
\]
commutes with \(\rho(\mathfrak g)\). If \(\mathfrak g\) is semisimple and \(\rho\) faithful, its trace form
\(B_\rho(x,y)=\operatorname{tr}(\rho(x)\rho(y))\) is nondegenerate and
\[
\operatorname{tr}_V(c_{B_\rho})=\dim\mathfrak g.
\tag{2.5}
\]
If in addition the field is algebraically closed and \(V\) irreducible, then
\[
c_{B_\rho}=\frac{\dim\mathfrak g}{\dim V}\,1_V.
\tag{2.6}
\]

**Proof.** In the enveloping algebra,
\([a,uv]=[a,u]v+u[a,v]\). Multiplying (2.2) therefore gives \([a,C_B]=0\) for all \(a\in\mathfrak g\). These elements generate \(U(\mathfrak g)\), so \(C_B\) is central. The representation extends to \(U(\mathfrak g)\), sending \(C_B\) to (2.4), which proves commutation and basis independence.

The preceding lesson proved nondegeneracy of \(B_\rho\): its radical is an ideal, Cartan's criterion makes that radical solvable in the faithful image, and semisimplicity makes it zero. For its dual bases,
\[
\operatorname{tr}(c_{B_\rho})=\sum_i B_\rho(x_i,y_i)=d.
\]
Lemma 1.2 makes the operator scalar on an irreducible module over the algebraically closed field. Taking its trace gives (2.6); division by the positive integer \(\dim V\) is valid in characteristic zero. \(\square\)

The same construction may be applied to the faithful image \(\rho(\mathfrak g)\) when \(\rho\) has a kernel. That image is semisimple because it is a quotient of \(\mathfrak g\). Its trace form is the one belonging to the represented image. Formula (2.5) then reads \(\dim\rho(\mathfrak g)\).

The form is part of the normalization. If \(B'=aB\), \(a\ne0\), dual vectors scale by \(a^{-1}\), and
\[
C_{B'}=a^{-1}C_B,\qquad c_{B'}=a^{-1}c_B.
\tag{2.7}
\]
In particular \(C_\kappa\), defined with the Killing form, differs from a Casimir defined using a module's trace form.

## 3. A one-dimensional quotient is enough

Work first over an algebraically closed characteristic-zero field.

**Lemma 3.1.** If \(\mathfrak g\) is semisimple and \(W\subseteq V\) is an irreducible submodule of codimension one, then \(W\) has an invariant complement.

**Proof.** The quotient is a one-dimensional module, hence trivial, so \(\mathfrak gV\subseteq W\). If the action on \(V\) is zero, any vector-space complement works. Otherwise its image \(\mathfrak l=\rho(\mathfrak g)\) is a nonzero semisimple algebra. Form its Casimir \(c\) using the trace form of the faithful action on \(V\). It commutes with the action, maps \(V\) into \(W\), and acts on \(W\) as a scalar \(a\), by Lemma 1.2. Its quotient action is zero, so
\[
a\dim W=\operatorname{tr}_V(c)=\dim\mathfrak l\ne0.
\]
Thus \(a\ne0\), and \(c|_W\) is invertible. Its image is \(W\), so rank–nullity makes its kernel one-dimensional. That kernel is invariant, meets \(W\) trivially and has complementary dimension. \(\square\)

Here the form is the trace form on the whole extension \(V\). We did not assume that the action on its irreducible submodule was faithful, nor did we use a Casimir eigenvalue computed from that different module.

**Lemma 3.2.** Every codimension-one submodule of a finite-dimensional \(\mathfrak g\)-module has an invariant complement.

**Proof.** Induct on \(\dim V\). The case \(W=0\) is immediate; the irreducible case is Lemma 3.1. Otherwise choose a proper nonzero submodule \(U\subset W\). By induction, \(W/U\subset V/U\) has a one-dimensional invariant complement \(\overline L\). Let \(T\) be its inverse image in \(V\). Then
\[
V=W+T,\qquad W\cap T=U,\qquad \dim(T/U)=1.
\]
Since \(U\ne W\), \(\dim T<\dim V\). Induction applied to \(U\subset T\) gives \(T=U\oplus L\) with \(L\) an invariant line. Therefore \(V=W\oplus L\). \(\square\)

**Theorem 3.3 (Weyl, algebraically closed case).** Every finite-dimensional representation of a semisimple algebra is completely reducible.

**Proof.** Let \(W\subseteq V\) be an invariant subspace. The cases \(W=0,V\) are immediate. On \(\operatorname{Hom}_k(V,W)\) the action is
\[
(x\cdot P)(v)=x\cdot P(v)-P(x\cdot v).
\tag{3.1}
\]
Expansion shows that this is a representation. Consider its subspaces
\[
A=\{P:P|_W=a1_W\text{ for some }a\in k\},
\qquad B=\{P:P|_W=0\}.
\]
For \(P\in A\) and \(w\in W\), (3.1) gives
\((x\cdot P)(w)=a\,xw-a\,xw=0\). Hence \(A,B\) are submodules and \(\mathfrak gA\subseteq B\). Extending \(1_W\) linearly to \(V\) shows that the coefficient map \(A\to k\), \(P\mapsto a\), is surjective with kernel \(B\). Thus \(B\) has codimension one in \(A\).

Lemma 3.2 supplies \(A=B\oplus L\) for an invariant line \(L\). Perfectness makes its action trivial. A nonzero \(P\in L\) therefore commutes with \(\mathfrak g\), and its restriction is \(a1_W\) with \(a\ne0\). Rescale to obtain \(P|_W=1_W\). Then \(P\) is an invariant projection onto \(W\), and
\[
V=W\oplus\ker P.
\]
Every submodule has a complement. Lemma 1.1 proves complete reducibility. \(\square\)

## 4. Descent to every characteristic-zero field

**Theorem 4.1 (Weyl over an arbitrary field).** If \(k\) has characteristic zero and \(\mathfrak g\) is semisimple over \(k\), every finite-dimensional \(\mathfrak g\)-module is completely reducible.

**Proof.** Extend scalars to an algebraic closure \(K\). The preceding lesson's Killing-form criterion shows that \(\mathfrak g_K\) is semisimple: its nondegenerate Killing matrix stays nondegenerate. For any submodule \(W\subseteq V\), Theorem 3.3 gives a \(\mathfrak g_K\)-equivariant projection \(P_K:V_K\to W_K\) with \(P_K|_{W_K}=1\).

Choose \(k\)-bases of \(\mathfrak g,V,W\), the basis of \(V\) beginning with that of \(W\). The conditions
\[
P|_W=1_W,\qquad P\rho_V(x)=\rho_W(x)P
\tag{4.1}
\]
for every basis element \(x\in\mathfrak g\) form finitely many linear equations in the entries of \(P\), all with coefficients in \(k\). Their solution over \(K\) implies a solution over \(k\). Indeed, row reduction over \(k\) either gives an inconsistent row \(0=b\), \(b\ne0\), which remains inconsistent over \(K\), or gives a consistent system whose free variables can be set to zero in \(k\). The first alternative is excluded by \(P_K\). Thus a projection \(P\) satisfying (4.1) exists over \(k\). Its kernel is an invariant complement to \(W\). Lemma 1.1 completes the proof. \(\square\)

A complement obtained over the larger field was not assumed to be defined over the smaller one. The finite system for a projection provides the descent.

We will also extend the Jordan terminology to these fields. An endomorphism over \(k\) is called **semisimple** if it becomes diagonalizable over an algebraic closure.

**Lemma 4.2 (Jordan parts over \(k\)).** In characteristic zero, the commuting semisimple and nilpotent parts of an endomorphism \(X\) are defined over \(k\), are polynomials in \(X\), and are unique. Both polynomials can have zero constant term.

**Proof.** The case of the zero space is immediate. Factor the minimal polynomial over \(k\) as
\[
m_X(t)=\prod_j f_j(t)^{r_j},
\]
where the \(f_j\) are distinct monic irreducibles. The coprime residue construction of the preceding lesson gives the primary direct sum on which \(f_j(X)^{r_j}=0\). Work on one such summand and put
\(R=k[t]/(f^r)\), with the nilpotent ideal \(J=(f)/(f^r)\).

In characteristic zero the irreducible polynomial \(f\) is separable: its derivative is nonzero of smaller degree, so \(\gcd(f,f')=1\). Bézout therefore makes \(f'(t)\) invertible modulo \(f^r\). Starting with \(a_0=t\) in \(R\), define
\[
a_{q+1}=a_q-f(a_q)f'(a_q)^{-1}.
\tag{4.2}
\]
All these expressions belong to \(R\). In fact \(a_q\equiv t\pmod J\), so \(f'(a_q)\) reduces to the unit \(f'(t)\) modulo \(J\), and is a unit in \(R\). To justify that lifting assertion, if \(uv=1-j\) with \(j\in J\), multiply \(v\) by the finite sum \(1+j+\cdots+j^{r-1}\).

For commuting elements the polynomial identity
\(f(a+b)=f(a)+f'(a)b+b^2Q(a,b)\) follows by binomial expansion. Hence \(f(a_q)\in J^{2^q}\) by induction, and (4.2) makes \(f(a_{q+1})\in J^{2^{q+1}}\). Once \(2^q\ge r\), \(f(a_q)=0\). Set \(S=a_q(X)\) on this primary summand. It satisfies \(f(S)=0\); after algebraic closure the roots of \(f\) are distinct, so the eigenspace construction of the preceding lesson makes \(S\) diagonalizable. Since \(a_q\equiv t\pmod J\), \(N=X-S\) is a multiple of \(f(X)\), and \(N^r=0\). Both operators are polynomials in \(X\), so commute.

Combine their polynomials on the primary summands by the coprime residue construction. This gives \(X=S+N\) over \(k\). Uniqueness follows by extending scalars and using uniqueness of the algebraically closed Jordan decomposition. If zero is a root of \(m_X\), the construction on its primary summand gives \(S=0\), so its polynomial can be chosen with constant term zero. If zero is not a root, replace a polynomial \(p\) for \(S\) by
\[
p(t)-\frac{p(0)}{m_X(0)}m_X(t).
\]
This changes no operator and makes the constant term zero. The polynomial \(t-p(t)\) for \(N\) then also has constant term zero. \(\square\)

This finite Newton construction is only a computation in a quotient polynomial ring; it assumes no convergence or infinite series.

The abstract Jordan decomposition of the preceding lesson consequently exists over every characteristic-zero field in this extended terminology. Apply Lemma 4.2 to \(\operatorname{ad}x\). After algebraic closure its two parts are derivations, by the generalized-eigenspace proof there. The derivation identities are equalities of \(k\)-linear maps; scalar extension is injective, so the identities hold over \(k\). The inner-derivation theorem over \(k\) supplies unique \(x_s,x_n\) inducing these parts. The zero centre then gives \(x=x_s+x_n\) and \([x_s,x_n]=0\). Uniqueness is inherited from the operator decomposition.

## 5. Representations preserve Jordan decomposition

**Theorem 5.1.** For a semisimple Lie algebra over any characteristic-zero field, every finite-dimensional representation satisfies
\[
\rho(x_s)=\rho(x)_s,\qquad \rho(x_n)=\rho(x)_n.
\tag{5.1}
\]

**Proof.** We first prove the theorem over an algebraically closed field. The zero representation is immediate. Let
\(\mathfrak l=\rho(\mathfrak g)\subseteq\mathfrak{gl}(V)\), a semisimple algebra, and set
\[
T=\rho(x)=S+N
\]
for its operator Jordan decomposition. On \(\operatorname{End}(V)\), the Jordan parts of \(\operatorname{ad}T\) are \(\operatorname{ad}S,\operatorname{ad}N\), by the preceding lesson. They are polynomials in \(\operatorname{ad}T\), so preserve its invariant subspace \(\mathfrak l\). Their restrictions to \(\mathfrak l\) are commuting derivations, respectively semisimple and nilpotent. Restriction preserves these two properties: a diagonalizable operator's invariant subspace is a sum of its eigenspaces using polynomial projections, and the same nilpotent power still vanishes.

All derivations of \(\mathfrak l\) are inner. Thus there are unique \(a,b\in\mathfrak l\) with
\[
[S,z]=[a,z],\qquad [N,z]=[b,z]\quad(z\in\mathfrak l).
\]
Adding these equations gives \(T=a+b\), because \(\mathfrak l\) has zero centre. Commutation of the two derivations gives \([a,b]=0\). Their semisimple and nilpotent properties identify \(a,b\) as the intrinsic Jordan parts of \(T\) in \(\mathfrak l\).

These intrinsic parts are \(\rho(x_s),\rho(x_n)\). To verify this without assuming (5.1), split the ideal \(\ker\rho\):
\(\mathfrak g=\ker\rho\oplus I\), with \(I\) an ideal mapping isomorphically onto \(\mathfrak l\). The restrictions of \(\operatorname{ad}x_s,\operatorname{ad}x_n\) to \(I\) are semisimple and nilpotent and transport under this isomorphism to
\(\operatorname{ad}_{\mathfrak l}\rho(x_s),\operatorname{ad}_{\mathfrak l}\rho(x_n)\).
They commute and sum to \(\operatorname{ad}_{\mathfrak l}T\). Intrinsic uniqueness in \(\mathfrak l\) therefore gives \(a=\rho(x_s)\), \(b=\rho(x_n)\).

It remains to identify the intrinsic parts with the operator parts. The difference \(S-a\) centralizes \(\mathfrak l\). By Weyl's theorem \(V\) is a direct sum of irreducible \(\mathfrak l\)-modules \(W\). Each \(W\) is preserved by \(a\in\mathfrak l\) and by \(S\), a polynomial in \(T\). Lemma 1.2 makes \((S-a)|_W=c_W1_W\). Since \(\mathfrak l\) is perfect, every represented element of it has trace zero on \(W\): it is a sum of commutators. Also \(N|_W\) is nilpotent, so
\[
\operatorname{tr}_W(S)=\operatorname{tr}_W(T)=0,
\qquad \operatorname{tr}_W(a)=0.
\]
Hence \(c_W\dim W=0\), giving \(c_W=0\) in characteristic zero. Thus \(S=a\) on every summand and on \(V\); subtracting gives \(N=b\). This proves (5.1) over the algebraically closed field.

For general \(k\), extend to an algebraic closure. Semisimplicity persists, and Lemma 4.2 and the abstract construction following it show that both intrinsic and operator Jordan parts are the extensions of those defined over \(k\). The identities just proved over the closure descend because scalar extension is injective. \(\square\)

Merely normalizing a matrix Lie algebra does not put an operator inside it: its centralizer is an additional possibility. Complete reducibility, Schur's lemma and the trace-zero calculation are precisely what eliminate that possibility here.

## 6. Why the adjoint eigenvalue is exactly one

**Proposition 6.1.** Let \(\mathfrak g\) be semisimple over any characteristic-zero field. The element \(C_\kappa\in U(\mathfrak g)\) defined using the Killing form acts on its adjoint module as the identity.

**Proof.** Its action is
\[
Qz=\sum_i[x_i,[y_i,z]]
\]
for Killing-dual bases \(x_i,y_i\). For \(w\in\mathfrak g\), invariance and symmetry give
\[
\begin{aligned}
\kappa(Qz,w)
&=\sum_i\kappa([y_i,z],[w,x_i])\\
&=\sum_i\kappa(-\operatorname{ad}z(y_i),\operatorname{ad}w(x_i))\\
&=\sum_i\kappa(y_i,\operatorname{ad}z\,\operatorname{ad}w(x_i))\\
&=\operatorname{tr}_{\mathfrak g}(\operatorname{ad}z\,\operatorname{ad}w)
=\kappa(z,w).
\end{aligned}
\]
The penultimate equality is the dual-basis formula for an operator trace: its \(i\)-th diagonal coefficient in the \(x_i\)-basis is its pairing with \(y_i\). Nondegeneracy makes \(Qz=z\). The zero algebra is included, with the unique operator on the zero space. \(\square\)

This proof does not require simplicity or an irreducible adjoint representation. The value \(1\) uses the Killing form, the normalization in [Deligne, p. 321].

## 7. Normalizations and the three boundaries of the theorem

For \(\mathfrak{sl}_2\), use
\[
e=E_{12},\qquad h=\operatorname{diag}(1,-1),\qquad f=E_{21}.
\]
In the standard two-dimensional representation, the trace form has
\(B(h,h)=2\), \(B(e,f)=B(f,e)=1\), and all other pairings zero. For the ordered basis \(e,h,f\), its dual is \(f,h/2,e\). Therefore
\[
C_B=ef+fe+\tfrac12h^2,\qquad
c_B=\tfrac32\,1_{\mathbb C^2}.
\tag{7.1}
\]
The Killing form is \(\kappa=4B\), by the preceding lesson, so
\[
C_\kappa=\tfrac14(ef+fe)+\tfrac18h^2,
\qquad c_\kappa|_{\mathbb C^2}=\tfrac38\,1.
\tag{7.2}
\]
On the adjoint module it instead has eigenvalue \(1\). These values belong to specified forms and specified modules.

The following examples show why all hypotheses in Weyl's theorem matter.

**A solvable algebra.** Let \(\mathfrak a=kx\oplus ky\), \([x,y]=y\), act on \(k^2\) by
\[
\rho(x)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\rho(y)=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
The commutator is \(\rho(y)\), so this is a representation. The line \(ku_1\) is invariant. Any complementary line has a generator \(u_2+au_1\), whose image under \(y\) is \(u_1\). This nonzero vector lies outside that complementary line, so no complement is invariant. The module is not completely reducible.

**An infinite-dimensional module in characteristic zero.** On the space with basis \(v_0,v_1,\ldots\), define
\[
fv_j=v_{j+1},\qquad hv_j=-2jv_j,\qquad
ev_j=j(1-j)v_{j-1},
\tag{7.3}
\]
with \(ev_0=0\). The first two bracket identities follow by comparing adjacent \(h\)-weights. For the third,
\[
(ef-fe)v_j=\bigl((j+1)(-j)-j(1-j)\bigr)v_j=-2jv_j=hv_j.
\]
Thus these formulas give an \(\mathfrak{sl}_2\)-module. The subspace
\(W=\langle v_1,v_2,\ldots\rangle\) is invariant: \(ev_1=0\), and every other action stays in that span. Its quotient is a trivial line.

If \(W\) had an invariant complement, that complement would be a one-dimensional trivial module, because \(\mathfrak{sl}_2\) is perfect. Its generator would be killed by \(h\). Distinct characteristic-zero weights in (7.3) make \(\ker h=kv_0\), but \(fv_0=v_1\ne0\). No such complement exists. This explicitly constructed module is the highest-weight-zero Verma module; its enveloping-algebra realization will be proved in *Highest weights and Verma modules*.

**Prime characteristic.** Let \(k\) have characteristic \(p>2\). The same three-dimensional matrix algebra \(\mathfrak{sl}_2(k)\) is simple: \(\operatorname{ad}h\) has three distinct eigenvalues \(2,0,-2\), so a nonzero ideal contains some \(e,h\) or \(f\), by polynomial eigenprojections. The brackets \([e,f]=h\), \([h,e]=2e\), \([h,f]=-2f\) then put all three in the ideal. It is therefore semisimple in the radical-zero sense.

It acts on the homogeneous degree-\(p\) polynomials \(V=k[u,v]_p\) by
\[
e=u\partial_v,\qquad f=v\partial_u,\qquad
h=u\partial_u-v\partial_v.
\tag{7.4}
\]
Their commutators, computed by the product rule, are the same three \(\mathfrak{sl}_2\) relations. The submodule
\[
U=ku^p\oplus kv^p
\]
is trivial, since the derivatives and the \(h\)-weights of these two monomials are zero. An invariant complement would give a commuting projection \(P:V\to U\) with \(P|_U=1\). But
\[
e(u^{p-1}v)=u^p
\]
would force
\[
u^p=P\,e(u^{p-1}v)=e\,P(u^{p-1}v)=0,
\]
a contradiction. This \((p+1)\)-dimensional module is not completely reducible, even though its acting algebra is simple. The broader modular setting is surveyed in [Premet–Strade]; this example has been checked directly.

The modular action is faithful: its kernel is an ideal of the simple algebra, and \(e(u^{p-1}v)\ne0\). Its image therefore has dimension \(3\). In particular, for \(p=5\) this dimension is not divisible by \(p\), while the module still fails to split. This contradicts the sufficiency of that dimension condition suggested in [Milne, Lie algebras, Aside 5.22].

The trace form itself is already zero in this six-dimensional example. The \(h\)-weights are \(0,3,1,4,2,0\) modulo \(5\), with squares summing to \(30=0\). The diagonal coefficients of \(ef\) are \(0,3,4,3,0,0\), summing to \(10=0\); trace cyclicity gives the same trace for \(fe\). Every other basis product is off-diagonal. Thus all trace-form pairings vanish, and the nondegenerate-form step of the characteristic-zero proof is unavailable.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Compute the Casimir of \(\mathfrak{sl}_2\) for the trace form on \(\mathbb C^2\), its standard-module eigenvalue and its relation to the Killing-form Casimir.

**Solution.** Matrix multiplication gives
\[
\operatorname{tr}(h^2)=2,\quad
\operatorname{tr}(ef)=\operatorname{tr}(fe)=1,
\]
with the other basis pairings zero. Thus the dual basis to \(e,h,f\) is \(f,h/2,e\), and multiplication in \(U(\mathfrak{sl}_2)\) gives
\(C_B=ef+fe+h^2/2\).
On the two-dimensional module, \(ef=E_{11}\), \(fe=E_{22}\) and \(h^2=1\), so the eigenvalue is \(3/2\). Since \(\kappa=4B\), the Killing duals are a quarter of these duals and \(C_\kappa=C_B/4\), with eigenvalue \(3/8\) there. The adjoint eigenvalue \(1\) belongs to \(C_\kappa\), not to the different trace normalization \(C_B\).

**Exercise 8.2 (medium).** Prove that \(C_\kappa\) acts as the identity on the adjoint representation, without assuming the algebra simple.

**Solution.** Its action on \(z\) is \(Qz=\sum_i[x_i,[y_i,z]]\) for Killing-dual bases. Pair with any \(w\). Twice using invariance gives
\[
\begin{aligned}
\kappa(Qz,w)
&=\sum_i\kappa([y_i,z],[w,x_i])\\
&=\sum_i\kappa(y_i,\operatorname{ad}z\,\operatorname{ad}w(x_i))
=\operatorname{tr}(\operatorname{ad}z\,\operatorname{ad}w)
=\kappa(z,w).
\end{aligned}
\]
The dual-basis sum is precisely the trace in the \(x_i\)-basis. Nondegeneracy yields \(Qz=z\). No irreducibility assumption was used, so this applies simultaneously to all simple ideals and to their direct sum.

**Exercise 8.3 (medium).** Give a non-completely-reducible two-dimensional representation of \([x,y]=y\), and prove that its invariant line has no invariant complement.

**Solution.** Use \(x=\operatorname{diag}(1,0)\), \(y=E_{12}\) on a basis \(u_1,u_2\). Their commutator is \(E_{12}\), so the assignment is a representation. The line \(ku_1\) is invariant. Every vector-space complement is generated by \(u_2+au_1\); \(y\) sends this generator to \(u_1\), which is nonzero and not in that complement. Hence none is a submodule. Lemma 1.1 makes the module non-completely-reducible.

**Exercise 8.4 (hard).** Prove Weyl's theorem over every characteristic-zero field, including the codimension-one step, the reduction to that step and descent.

**Solution.** First extend attention to an algebraically closed characteristic-zero field. If an irreducible submodule \(W\subseteq V\) has codimension one, perfectness makes its quotient trivial. For a nonzero represented image \(\mathfrak l\), use the Casimir for its faithful action on \(V\). It maps \(V\) into \(W\), commutes with the action and is scalar \(a\) on \(W\). Its trace is \(\dim\mathfrak l\), whereas its quotient action is zero. Thus \(a\dim W=\dim\mathfrak l\ne0\). Its kernel is an invariant complementary line. If the entire action is zero, every complement is invariant.

For arbitrary codimension-one \(W\), induct on \(\dim V\). A proper nonzero submodule \(U\subset W\) gives, by induction, a complementary line to \(W/U\) in \(V/U\). Its inverse image \(T\) satisfies \(T\cap W=U\) and has smaller dimension than \(V\). A complement to \(U\) in \(T\), again by induction, is then a complement to \(W\) in \(V\).

For general \(W\subset V\), give \(\operatorname{Hom}(V,W)\) its commutator action, and form
\[
A=\{P:P|_W=a1_W\},\qquad B=\{P:P|_W=0\}.
\]
Restriction is a surjective scalar-coefficient map \(A\to k\), since a linear extension of \(1_W\) exists. Its kernel is \(B\), and \(\mathfrak gA\subseteq B\). The codimension-one assertion splits \(A=B\oplus L\) with \(L\) an invariant line. The action on \(L\) is trivial by perfectness. Normalize a nonzero \(P\in L\) to have restriction \(1_W\). It commutes with the action, so \(\ker P\) is the required complement. Lemma 1.1 converts these complements into a sum of irreducibles.

Finally let the original field \(k\) be arbitrary of characteristic zero. Nondegeneracy of the Killing form shows that scalar extension to an algebraic closure is semisimple. The projection equations \(P|_W=1\) and \(P\rho_V(x)=\rho_W(x)P\) have coefficients in \(k\) and a solution over that closure. Row reduction over \(k\) shows that they have a solution over \(k\): an inconsistent row would stay inconsistent after extension. Its invariant kernel gives the complement over \(k\). This proves the theorem with its full field scope.

## What this lesson does not prove

The preceding lessons supply the enveloping algebra and extension of representations to it; trace cyclicity; Cartan's criteria; ideal and quotient semisimplicity; perfectness; inner derivations; and the algebraically closed operator and abstract Jordan decompositions. They are used at their proved characteristic and dimension hypotheses.

All new Lie-algebra assertions here have proofs. Schur's scalar lemma and the finite module-complement criterion are proved explicitly. Field descent is a finite linear-system argument. Lemma 4.2 constructs Jordan parts over the ground field by finite polynomial operations, so representation compatibility holds over every characteristic-zero field. The future identification of (7.3) with an induced Verma module is not needed for its bracket identities or its nonsplitting proof. No unitary trick, compact group, Whitehead lemma or root classification is imported into Weyl's proof.

## References

- **[Milne, Lie algebras]** J. S. Milne, *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 2013, Chapter I §5, especially the Casimir construction, Weyl's theorem and Jordan decomposition. [Author's notes](https://www.jmilne.org/math/CourseNotes/LAG.pdf).
- **[Milne, Algebraic groups]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected 2021 text, published 2022, §22c, Casimir operators and Lemma 22.40. Milne's argument there uses the algebraic group; the proof for Lie algebras is given in this lesson. [Author's edition](https://www.jmilne.org/math/Books/iAG2022.pdf).
- **[Gruson–Serganova]** C. Gruson and V. Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Springer, 2018, Chapter 5 §2, especially Lemma 2.5.
- **[Deligne]** P. Deligne, “La série exceptionnelle de groupes de Lie,” *C. R. Acad. Sci. Paris*, Série I **322** (1996), 321–326, p. 321. The Killing-form normalization there gives adjoint Casimir \(1\). [IAS copy](https://publications.ias.edu/sites/default/files/75_LaSerie.pdf).
- **[Premet–Strade]** A. Premet and H. Strade, *Classification of finite dimensional simple Lie algebras in prime characteristics*, survey, 2006, introduction and §1. [arXiv preprint](https://arxiv.org/abs/math/0601380).

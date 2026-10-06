# The Killing form and Cartan's criteria

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The trace of a product can detect a structural property that no single bracket reveals. Cartan's first criterion turns vanishing traces into solvability. His second identifies semisimple algebras by a nondegenerate bilinear form. With that form available, orthogonal complements become ideals, decompositions become canonical, and derivations become inner.

The prerequisite is [Nilpotent and solvable Lie algebras: Engel's and Lie's theorems](RT-LIE-02.md). All spaces and Lie algebras here are finite-dimensional. The ground field has characteristic zero; the polynomial Jordan decomposition and its abstract version are discussed over an algebraically closed field, including \(\mathbb C\). Cartan's criteria, the ideal decomposition and the inner-derivation theorem hold over every characteristic-zero field. Basic references are [Milne, Lie algebras] and, for prime characteristic, [Premet–Strade].

## 1. Separating eigenvalues from nilpotence

Call an endomorphism **semisimple** if it is diagonalizable over the algebraically closed field.

**Lemma 1.1 (polynomial Jordan decomposition).** For \(X\in\operatorname{End}(V)\), there is a unique decomposition
\[
X=S+N,\qquad SN=NS,\qquad S\text{ semisimple},\quad N\text{ nilpotent}.
\]
Both \(S,N\) are polynomials in \(X\) with zero constant term. On \(\operatorname{End}(V)\),
\[
(\operatorname{ad}X)_s=\operatorname{ad}S,\qquad
(\operatorname{ad}X)_n=\operatorname{ad}N.
\tag{1.1}
\]

**Proof.** The case \(V=0\) is immediate. Otherwise a nonzero polynomial annihilates \(X\), by linear dependence of its powers in \(\operatorname{End}(V)\). Choose the monic polynomial of least degree doing so; it factors as \(\prod_\lambda(t-\lambda)^{m_\lambda}\). The simultaneous-residue construction below gives \(e_\lambda(t)\) with residue \(1\) modulo its own factor and \(0\) modulo the others. The values \(e_\lambda(X)\) are mutually orthogonal projections summing to \(1\). Their images are exactly \(V_\lambda=\ker(X-\lambda)^{m_\lambda}\): the product \((t-\lambda)^{m_\lambda}e_\lambda(t)\) is divisible by the annihilating polynomial, and \(e_\lambda(X)\) acts as \(1\) on that kernel. Thus \(V=\bigoplus V_\lambda\). On each summand prescribe \(S=\lambda\,1\), \(N=X-\lambda\,1\), giving commuting operators of the required kinds.

For their polynomial construction, the powers \((t-\lambda)^{m_\lambda}\) are pairwise coprime. Polynomial division repeated on remainders of strictly decreasing degree expresses their gcd as a linear combination; for coprime \(a,b\) this gives \(ua+vb=1\). Combine residues \(r_a,r_b\) as \(r_avb+r_bua\), then induct. Choose \(p(t)\equiv\lambda\pmod{(t-\lambda)^{m_\lambda}}\) for every eigenvalue. If zero is an eigenvalue these prescriptions imply \(p(0)=0\); otherwise impose also \(p(t)\equiv0\pmod t\). Then \(S=p(X)\), \(N=X-p(X)\), with zero constant terms.

For uniqueness, suppose \(X=S'+N'\) is another commuting decomposition. Both operators commute with \(X\), so preserve each \(V_\lambda\). Eigenspaces of \(S'\) inside \(V_\lambda\) are \(N'\)-invariant. On an eigenspace of eigenvalue \(\mu\), \(X=\mu\,1+N'\) has only eigenvalue \(\mu\). Since this lies in \(V_\lambda\), \(\mu=\lambda\). Thus \(S'=S\), hence \(N'=N\).

In an eigenbasis for \(S\), a matrix unit from the \(\mu\)-eigenspace to the \(\lambda\)-eigenspace is an eigenvector of \(\operatorname{ad}S\) with eigenvalue \(\lambda-\mu\). Thus \(\operatorname{ad}S\) is semisimple. The binomial argument of the prerequisite makes \(\operatorname{ad}N\) nilpotent. They commute and sum to \(\operatorname{ad}X\); uniqueness proves (1.1). \(\square\)

For example,
\[
X=\begin{pmatrix}2&1&0\\0&2&0\\0&0&-1\end{pmatrix}
\]
has \(S=\operatorname{diag}(2,2,-1)\) and \(N=E_{12}\).
Every \(X\)-invariant subspace is invariant under its Jordan parts because they are polynomials in \(X\). Applying the lemma to \(\operatorname{ad}X\) itself also makes its semisimple part a zero-constant-term polynomial in \(\operatorname{ad}X\). This does not assert the same property for arbitrary \(\operatorname{ad}(p(X))\); the next proof establishes the precise relation it needs.

## 2. The trace criterion for solvability

Trace-cyclicity gives
\[
\operatorname{tr}([A,B]C)=\operatorname{tr}(A[B,C]).
\tag{2.1}
\]

**Theorem 2.1 (Cartan's solvability criterion).** For a Lie subalgebra
\(\mathfrak l\subseteq\mathfrak{gl}(V)\) in characteristic zero,
\[
\mathfrak l\text{ solvable}
\quad\Longleftrightarrow\quad
\operatorname{tr}(XY)=0
\quad(X\in[\mathfrak l,\mathfrak l],\ Y\in\mathfrak l).
\tag{2.2}
\]

**Proof of necessity.** Extend to an algebraic closure. Lie's theorem makes \(\mathfrak l\) upper-triangular and its derived algebra strictly upper-triangular. Their products have zero diagonal and trace. Trace is unchanged by field extension, proving necessity over the original field.

**Proof of sufficiency.** Field extension preserves the hypothesis and preserves and reflects solvability, by the preceding lesson. We may assume the field algebraically closed.

Fix \(X\in[\mathfrak l,\mathfrak l]\), with eigenvalues \(\lambda_1,\ldots,\lambda_d\), counting multiplicities. Let \(E\) be their rational span. For any \(\mathbb Q\)-linear \(f:E\to\mathbb Q\), let \(Y_f\) act by \(f(\lambda)\) on the generalized \(\lambda\)-eigenspace. We shall prove
\[
\operatorname{tr}(XY_f)=\sum_i\lambda_i f(\lambda_i)=0.
\tag{2.3}
\]
The operator \(Y_f\) need not belong to \(\mathfrak l\).

Write \(X=S+N\). On \(\operatorname{Hom}(V_\mu,V_\lambda)\),
\(\operatorname{ad}S\) acts by \(\lambda-\mu\), while
\(\operatorname{ad}Y_f\) acts by
\(f(\lambda)-f(\mu)=f(\lambda-\mu)\).
Interpolate on the finite set of distinct differences to obtain a polynomial \(q\) with
\(q(\lambda-\mu)=f(\lambda-\mu)\) and \(q(0)=0\).
Different pairs with the same difference give the same prescription, so this is consistent. Hence
\(\operatorname{ad}Y_f=q(\operatorname{ad}S)\).
By (1.1), \(\operatorname{ad}S\) is the semisimple part of \(\operatorname{ad}X\), and Lemma 1.1 makes it \(p_0(\operatorname{ad}X)\) for some \(p_0(0)=0\). Thus
\[
\operatorname{ad}Y_f=q(p_0(\operatorname{ad}X)).
\tag{2.4}
\]
Since \(X\) belongs to the derived ideal, \(\operatorname{ad}X\) maps \(\mathfrak l\) into that ideal, as does every positive power. The polynomial (2.4) has zero constant term. Consequently
\[
[Y_f,\mathfrak l]\subseteq[\mathfrak l,\mathfrak l].
\tag{2.5}
\]

Write \(X=\sum_r[A_r,B_r]\) with \(A_r,B_r\in\mathfrak l\). Equations (2.1), (2.5) and the hypothesis yield
\[
\operatorname{tr}(XY_f)
=\sum_r\operatorname{tr}(A_r[B_r,Y_f])=0.
\]
The nilpotent part on each generalized eigenspace has trace zero, so this is (2.3).

Choose a rational basis \(a_1,\ldots,a_m\) of \(E\) and write
\(\lambda_i=\sum_j r_{ij}a_j\), \(r_{ij}\in\mathbb Q\).
For the functional \(f_j(a_\ell)=\delta_{j\ell}\), (2.3) says
\[
0=\sum_i\lambda_i r_{ij}
=\sum_\ell\left(\sum_i r_{i\ell}r_{ij}\right)a_\ell.
\]
Its \(a_j\)-coefficient gives \(\sum_i r_{ij}^2=0\). A sum of rational squares vanishes only if each is zero. Thus all eigenvalues of \(X\) are zero and \(X\) is nilpotent. The argument uses the ordering on \(\mathbb Q\), without assuming an ordering on the ground field.

Every element of the represented derived algebra is therefore nilpotent. Engel makes that algebra nilpotent, hence solvable. Its quotient in \(\mathfrak l\) is abelian, so the solvable-extension property proves the claim. \(\square\)

## 3. An intrinsic bilinear form

For a representation \(\rho\), define its **trace form** and the **Killing form** by
\[
B_\rho(x,y)=\operatorname{tr}_V(\rho(x)\rho(y)),\qquad
\kappa_{\mathfrak g}(x,y)=
\operatorname{tr}_{\mathfrak g}(\operatorname{ad}x\,\operatorname{ad}y).
\]

**Proposition 3.1.** These forms are symmetric, bilinear and invariant:
\[
B_\rho([x,y],z)=B_\rho(x,[y,z]).
\tag{3.1}
\]
For any invariant symmetric form \(B\), the orthogonal complement \(I^\perp\) of an ideal is an ideal. For an ideal \(I\) of \(\mathfrak g\),
\[
\kappa_{\mathfrak g}|_{I\times I}=\kappa_I.
\tag{3.2}
\]

**Proof.** Linearity and trace-cyclicity prove bilinearity and symmetry; (2.1) proves invariance. If \(z\in I^\perp\), \(a\in I\), then
\(B([x,z],a)=-B(z,[x,a])=0\), proving idealness of \(I^\perp\).
For \(x\in I\), \(\operatorname{ad}x\) preserves \(I\) and induces zero on \(\mathfrak g/I\). A basis beginning with \(I\) makes its quotient block zero. For \(x,y\in I\), the product therefore has the same trace on \(\mathfrak g\) as on \(I\), proving (3.2). \(\square\)

The restriction formula requires an ideal, not an arbitrary subalgebra.

**Corollary 3.2 (intrinsic solvability criterion).**
\[
\mathfrak g\text{ solvable}\quad\Longleftrightarrow\quad
\kappa_{\mathfrak g}([\mathfrak g,\mathfrak g],\mathfrak g)=0.
\]

**Proof.** Apply Theorem 2.1 to \(\operatorname{ad}\mathfrak g\), whose derived algebra is \(\operatorname{ad}[\mathfrak g,\mathfrak g]\). Necessity follows from solvability of a homomorphic image. For sufficiency the adjoint image is solvable, and its kernel is the abelian centre, so the solvable-extension result proves the claim. \(\square\)

Define **semisimple** by \(\operatorname{rad}(\mathfrak g)=0\). Equivalently there is no nonzero solvable ideal, or no nonzero abelian ideal. A nonzero solvable ideal has a last nonzero derived term which is abelian; Jacobi shows that this term is still an ideal of \(\mathfrak g\). Conversely every abelian ideal is solvable. The zero algebra is semisimple.

**Theorem 3.3 (Cartan's semisimplicity criterion).** A characteristic-zero Lie algebra is semisimple if and only if its Killing form is nondegenerate.

**Proof.** The radical \(R=\mathfrak g^\perp\) of the form is an ideal. By (3.2), its own Killing form is zero, so Corollary 3.2 makes \(R\) solvable. Semisimplicity forces \(R=0\).

Conversely, suppose the Killing form nondegenerate and let \(A\) be an abelian ideal. For \(a\in A\), \(y\in\mathfrak g\), the operator \(\operatorname{ad}a\,\operatorname{ad}y\) maps \(\mathfrak g\) into \(A\) and kills \(A\), since \(\operatorname{ad}y\) preserves \(A\). Its diagonal blocks in a basis beginning with \(A\) are zero, so its trace is zero. Hence \(\kappa(a,y)=0\) for every \(y\), forcing \(a=0\). There is no nonzero abelian ideal. The argument includes the zero algebra, whose form has zero radical. \(\square\)

In particular semisimple algebras have zero centre. The converse fails for the solvable algebra \([x,y]=y\). The criterion also shows that field extension preserves and reflects semisimplicity: its Killing matrix has the same entries, and its determinant is unchanged.

## 4. Orthogonality splits every ideal

An algebra is **simple** if it is nonabelian and its only ideals are zero and itself. The one-dimensional abelian algebra is not called simple.

**Theorem 4.1 (canonical simple ideals).** A semisimple algebra decomposes as
\[
\mathfrak g=I_1\oplus\cdots\oplus I_r
\]
into commuting simple ideals. They are exactly its minimal nonzero ideals, and every ideal is a sum of a uniquely determined subset of them. For the zero algebra the sum is empty.

**Proof.** For any ideal \(I\), let \(J=I\cap I^\perp\). For \(u,v\in J\), \(z\in\mathfrak g\), invariance gives
\[
\kappa([u,v],z)=\kappa(u,[v,z])=0,
\]
since \([v,z]\in I\) and \(u\in I^\perp\). Nondegeneracy makes \(J\) abelian; semisimplicity then makes \(J=0\). The dimension formula
\(\dim I^\perp=\dim\mathfrak g-\dim I\) gives
\[
\mathfrak g=I\oplus I^\perp.
\tag{4.1}
\]
The two ideals commute, since their bracket lies in their intersection.

For nonzero \(\mathfrak g\), choose a minimal nonzero ideal \(I_1\). In (4.1), every ideal of \(I_1\) as a Lie algebra is an ideal of \(\mathfrak g\), because the complement commutes with it. Thus \(I_1\) is simple; it cannot be abelian. The complement is semisimple: any abelian ideal in it would also be an abelian ideal of \(\mathfrak g\). Repeat on that complement. Decreasing dimension makes the process terminate with simple commuting ideals.

For uniqueness and the assertion about all ideals, let \(J\) be an ideal, \(x\in J\), and write \(x=\sum_i x_i\), \(x_i\in I_i\). If \(x_i\ne0\), some \(a\in I_i\) has \([a,x_i]\ne0\), since the centre of the nonabelian simple algebra \(I_i\) is zero. Then
\[
[a,x]=[a,x_i]\in J\cap I_i.
\]
This nonzero intersection is an ideal of \(I_i\), so equals \(I_i\). Consequently every nonzero component of every vector of \(J\) belongs to a factor entirely contained in \(J\). Hence \(J\) is precisely the sum of those factors. Its minimal nonzero possibilities are the individual \(I_i\), so they are intrinsic, and every decomposition has the same factors up to permutation. \(\square\)

**Corollary 4.2.** Ideals and quotients of semisimple algebras are semisimple, and \([\mathfrak g,\mathfrak g]=\mathfrak g\).

**Proof.** An ideal is a sum of some \(I_i\), and its quotient removes those factors. A direct sum of simple algebras has no nonzero abelian ideal, because its projection to each factor would be such an ideal there. Finally \([I_i,I_i]\) is a nonzero ideal of each nonabelian simple factor, hence all of it. Summing proves the last assertion. \(\square\)

A diagonal copy \(\{(x,x):x\in I\}\) inside \(I\oplus I\) is a simple subalgebra but is not an ideal: for noncommuting \(a,x\),
\([(a,0),(x,x)]=([a,x],0)\) leaves the diagonal. The canonical factors are ideals, not arbitrary simple subalgebras.

## 5. Derivations are detected by the form

**Theorem 5.1.** Every derivation of a characteristic-zero semisimple algebra is inner:
\[
\operatorname{Der}(\mathfrak g)=\operatorname{ad}\mathfrak g.
\]
Its inducing element is unique.

**Proof.** For a derivation \(D\), nondegeneracy supplies a unique \(z\in\mathfrak g\) such that
\[
\kappa(z,x)=\operatorname{tr}_{\mathfrak g}(D\,\operatorname{ad}x)
\quad(x\in\mathfrak g).
\]
Set \(E=D-\operatorname{ad}z\). It is a derivation and
\(\operatorname{tr}(E\,\operatorname{ad}x)=0\) for every \(x\).
The derivation identity gives \([E,\operatorname{ad}x]=\operatorname{ad}(Ex)\). Thus
\[
0=\operatorname{tr}(E\,\operatorname{ad}[x,y])
=\operatorname{tr}([E,\operatorname{ad}x]\operatorname{ad}y)
=\kappa(Ex,y).
\]
Nondegeneracy gives \(Ex=0\) for all \(x\), so \(D=\operatorname{ad}z\). Uniqueness follows from the zero centre. \(\square\)

For later use, a faithful representation \(\rho\) of semisimple \(\mathfrak g\) also has nondegenerate trace form \(B_\rho\). Its radical \(R\) is an ideal by invariance. The trace form on the faithful image \(\rho(R)\) vanishes on all pairs, so Theorem 2.1 makes \(R\) solvable. Hence \(R=0\). The next lesson uses this observation to construct Casimir operators.

## 6. Jordan decomposition inside the Lie algebra

A polynomial in a derivation need not automatically be a derivation. To place its Jordan parts back in the algebra, first prove the relevant property.

**Lemma 6.1.** Over an algebraically closed characteristic-zero field, the semisimple and nilpotent parts of a derivation \(D\) are derivations.

**Proof.** Let \(V_\lambda\) be its generalized eigenspaces on the algebra. For \(u\in V_\lambda,v\in V_\mu\), the derivation rule gives
\[
(D-\lambda-\mu)[u,v]=[(D-\lambda)u,v]+[u,(D-\mu)v].
\]
Iteration gives the binomial sum with powers \(r\) on the first argument and \(s-r\) on the second. For sufficiently large \(s\), every term vanishes. Therefore
\([V_\lambda,V_\mu]\subseteq V_{\lambda+\mu}\); if \(\lambda+\mu\) is absent from the spectrum, the bracket is zero.
The semisimple part acts by \(\lambda\) on \(V_\lambda\), so
\[
D_s[u,v]=(\lambda+\mu)[u,v]=[D_su,v]+[u,D_sv].
\]
Bilinearity proves this for all pairs. Thus \(D_s\), and then \(D_n=D-D_s\), are derivations. \(\square\)

**Theorem 6.2 (abstract Jordan decomposition).** In a semisimple algebra over an algebraically closed characteristic-zero field, every \(x\) decomposes uniquely as
\[
x=x_s+x_n,\qquad [x_s,x_n]=0,
\]
with \(\operatorname{ad}x_s\) semisimple and \(\operatorname{ad}x_n\) nilpotent. They are the respective Jordan parts of \(\operatorname{ad}x\).

**Proof.** Apply Lemma 1.1 to \(\operatorname{ad}x\). Lemma 6.1 makes its parts derivations; Theorem 5.1 writes them uniquely as \(\operatorname{ad}x_s,\operatorname{ad}x_n\). Injectivity of \(\operatorname{ad}\) gives \(x=x_s+x_n\). Commutation gives \(\operatorname{ad}[x_s,x_n]=0\), hence \([x_s,x_n]=0\). Any alternative would induce another commuting operator Jordan decomposition, so Lemma 1.1 and injectivity prove uniqueness. \(\square\)

This assertion is intrinsic and independent of a chosen matrix realization. That arbitrary finite-dimensional representations preserve it is a further theorem, proved in *Complete reducibility: Casimir elements and Weyl's theorem*.

## 7. Computing the form and testing the characteristic

Use \(e=E_{12}\), \(h=\operatorname{diag}(1,-1)\), \(f=E_{21}\) for \(\mathfrak{sl}_2\). In the ordered basis \(e,h,f\),
\[
\operatorname{ad}e=
\begin{pmatrix}0&-2&0\\0&0&1\\0&0&0\end{pmatrix},\quad
\operatorname{ad}h=\operatorname{diag}(2,0,-2),\quad
\operatorname{ad}f=
\begin{pmatrix}0&0&0\\-1&0&0\\0&2&0\end{pmatrix}.
\]
Multiplying and tracing gives
\[
[\kappa]_{e,h,f}=
\begin{pmatrix}0&0&4\\0&8&0\\4&0&0\end{pmatrix},
\qquad\det[\kappa]=-128.
\tag{7.1}
\]
Thus \(\mathfrak{sl}_2\) is semisimple.

For all \(n\), a calculation on matrix units gives
\[
\kappa_{\mathfrak{gl}_n}(X,Y)
=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y).
\tag{7.2}
\]
Write \(\operatorname{ad}X=L_X-R_X\). On the space of matrices,
\[
\operatorname{tr}(L_A)=\operatorname{tr}(R_A)=n\operatorname{tr}(A),\qquad
\operatorname{tr}(L_XR_Y)=\operatorname{tr}(X)\operatorname{tr}(Y).
\]
For the last equality, the coefficient of \(E_{ij}\) in \(XE_{ij}Y\) is \(X_{ii}Y_{jj}\); sum over \(i,j\). For left multiplication, the \(E_{ij}\)-coefficient of \(AE_{ij}\) is \(A_{ii}\), repeated for all \(j\); right multiplication is analogous. Expanding the product of the two adjoint operators proves (7.2). Since \(\mathfrak{sl}_n\) is an ideal, (3.2) gives
\[
\kappa_{\mathfrak{sl}_n}(X,Y)=2n\operatorname{tr}(XY).
\tag{7.3}
\]
The trace pairing on \(\mathfrak{sl}_n\) is nondegenerate in characteristic zero. If \(X\) pairs to zero with every off-diagonal matrix unit, its off-diagonal entries vanish. Pairing with \(E_{ii}-E_{jj}\) makes the diagonal entries equal, and trace zero makes them zero. Thus \(\mathfrak{sl}_n\) is semisimple. The centre \(k1\) lies in the radical of (7.2), so \(\mathfrak{gl}_n\), for \(n\ge1\), is not semisimple.

The defining module's trace form is \(\operatorname{tr}(XY)\); the Killing form is \(2n\) times it. More generally, every invariant symmetric form \(B\) on a complex simple algebra is a scalar multiple of \(\kappa\). Define \(T\) by \(B(x,y)=\kappa(Tx,y)\). Invariance implies \(T[a,x]=[a,Tx]\). For an eigenvalue \(c\) of \(T\), the nonzero kernel of \(T-c\) is an ideal, hence all of the simple algebra. Thus \(T=c1\). The scalar depends on the form and can be zero.

Here is an explicit contrast in prime characteristic. For a prime \(p>3\), let
\[
W=\operatorname{Der}(k[t]/(t^p)),\qquad
d_i=t^{i+1}\partial_t\quad(-1\le i\le p-2).
\]
Every derivation is determined by its value on \(t\), and every value is allowed because the derivative of \(t^p\) is zero. These \(p\) operators form a basis and the product rule gives
\[
[d_i,d_j]=(j-i)d_{i+j},
\]
with out-of-range terms zero.

This algebra is simple. A nonzero ideal is invariant under \(\operatorname{ad}d_0\), whose \(p\) eigenvalues are distinct. Polynomial coordinate projections isolate some \(d_i\) in it. Repeated brackets with \(d_{-1}\), with nonzero coefficients \(i+1\), reach \(d_{-1}\). Bracketing that element with the basis of \(W\) gives \(d_{-1},\ldots,d_{p-3}\). Finally
\([d_1,d_{p-3}]=(p-4)d_{p-2}\) gives the missing element, since \(p>3\). The ideal is therefore all of \(W\).

Its Killing form, however, is zero. A product of adjoint operators shifts the integer basis index by \(i+j\), so has zero diagonal unless \(i+j=0\). The only remaining pairs are \((0,0),(-1,1),(1,-1)\). Their traces are
\[
\sum_{m=-1}^{p-2}m^2,\qquad
\sum_{m=-1}^{p-2}(m-1)(m+2),
\]
and the latter again by symmetry. Truncated boundary terms have coefficient zero, so these sums are valid. The indices run through \(\mathbb F_p\); sums of \(1,m,m^2\) vanish in \(k\). The first sum is \(p=0\). For the others, choose \(a\in\mathbb F_p^\times\) with \(a^2\ne1\); permutation by multiplication by \(a\) forces both sums to vanish. Thus \(\kappa_W=0\), despite simplicity. This is the truncated-polynomial Witt algebra discussed in [Premet–Strade, §1].

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Compute the Killing form of \(\mathfrak{sl}_2\) in the basis \(e,h,f\), including its determinant.

**Solution.** The adjoint matrices in Section 7 are obtained by applying \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\) to each basis vector. The squares for \(e,f\) have trace zero; the square for \(h\) has trace \(4+4=8\). Products involving \(h\) and either off-diagonal matrix have zero trace. The product for \(e,f\) has diagonal \(2,2,0\), giving trace \(4\), and symmetry gives the other mixed entry. These are all entries of (7.1), with determinant \(4(-32)=-128\).

**Exercise 8.2 (medium).** Prove (7.3) without writing all adjoint matrices on \(\mathfrak{sl}_n\).

**Solution.** On the \(n^2\)-dimensional matrix space,
\[
\operatorname{ad}X\,\operatorname{ad}Y
=L_{XY}-L_XR_Y-R_XL_Y+R_{YX}.
\]
The first and last terms have traces \(n\operatorname{tr}(XY)\). For \(L_XR_Y\), its \(E_{ij}\)-diagonal coefficient is \(X_{ii}Y_{jj}\), giving trace \(\operatorname{tr}(X)\operatorname{tr}(Y)\). The other mixed term gives the same trace. Both vanish for traceless \(X,Y\). Since \(\mathfrak{sl}_n\) is an ideal, (3.2) identifies the ambient trace with its own Killing form. The result is \(2n\operatorname{tr}(XY)\).

**Exercise 8.3 (medium).** For an ideal \(I\) of semisimple \(\mathfrak g\), prove \(\mathfrak g=I\oplus I^\perp\). Does the assertion hold for every subalgebra?

**Solution.** Invariance makes \(I^\perp\) an ideal. For \(J=I\cap I^\perp\),
\(\kappa([u,v],z)=\kappa(u,[v,z])=0\) for \(u,v\in J\), because \([v,z]\in I\). Nondegeneracy makes \(J\) abelian, and semisimplicity makes it zero. The orthogonal-complement dimension formula proves the direct sum. For subalgebras it fails: \(ke\subseteq\mathfrak{sl}_2\) satisfies \(\kappa(e,e)=0\), so intersects its own orthogonal complement nontrivially.

**Exercise 8.4 (hard).** Prove the sufficiency direction of Cartan's solvability criterion over any characteristic-zero field. Explain why a polynomial in \(X\) alone does not prove the required normalizer assertion.

**Solution.** Extend to an algebraic closure, which preserves and reflects termination of the derived series. For \(X\) in the derived algebra, form the rational span \(E\) of its eigenvalues and use rational functionals \(f\) to define \(Y_f\) on generalized eigenspaces. On a Hom block, \(\operatorname{ad}Y_f\) acts by \(f(\lambda-\mu)\); interpolation makes it a zero-constant-term polynomial in \(\operatorname{ad}X_s\). By Lemma 1.1 the latter is itself a zero-constant-term polynomial in \(\operatorname{ad}X\). Hence \([Y_f,\mathfrak l]\) belongs to the derived ideal.

Writing \(X=\sum[A_r,B_r]\), trace-cyclicity and the hypothesis give
\[
\sum_i\lambda_i f(\lambda_i)
=\sum_r\operatorname{tr}(A_r[B_r,Y_f])=0.
\]
Expand the eigenvalues in a rational basis of \(E\) and use the coordinate functionals. Each gives a vanishing sum of rational squares, forcing all eigenvalues to vanish. Engel makes the derived algebra nilpotent, and the solvable-extension property completes the proof.

The distinction about polynomials is substantive. Put \(X=\operatorname{diag}(-1,0,1)\), \(A=E_{12}+E_{23}\), \(B=E_{21}+E_{32}\). Their span is a Lie algebra because \([X,A]=-A\), \([X,B]=B\), \([A,B]=-X\). In particular \(X\) belongs to its derived algebra. But \([X^2,A]=E_{12}-E_{23}\) is outside that span. Invariance under \(\operatorname{ad}X\) alone does not imply invariance under \(\operatorname{ad}(X^2)\). The Hom-block interpolation proves the particular assertion needed.

## What this lesson does not prove

We use elementary finite-dimensional basis extension and rank–nullity, verified in [Hefferon, Chapter Two §III.2, Corollary 2.12; Chapter Three §II.2, Theorem 2.14]. Trace-cyclicity was computed in the first lesson. Lemma 1.1 constructs the generalized eigenspaces and the polynomial Jordan decomposition, including the needed Bézout residue argument. The orthogonal-complement dimension formula follows by identifying the space with its dual using the nondegenerate form and restricting functionals to the subspace. All Lie-algebra results asserted here, including the modular example, have proofs. Preservation of abstract Jordan decomposition by representations belongs to the next lesson.

## References

- **[Milne, Lie algebras]** J. S. Milne, *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 2013, Chapter I §§1, 3–5. [Author's notes](https://www.jmilne.org/math/CourseNotes/LAG.pdf).
- **[Premet–Strade]** A. Premet and H. Strade, *Classification of finite dimensional simple Lie algebras in prime characteristics*, survey, 2006, §1. [arXiv preprint](https://arxiv.org/abs/math/0601380).
- **[Hefferon]** J. Hefferon, *Linear Algebra*, fourth edition, 2020, Chapters Two and Three. [Author's textbook](https://jheffero.w3.uvm.edu/linearalgebra/book.pdf).

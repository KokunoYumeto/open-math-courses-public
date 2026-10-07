# The Killing form and Cartan's criteria

*Written by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The trace of a product can detect a structural property that no single bracket reveals. Cartan's first criterion turns vanishing traces into solvability. His second identifies semisimple algebras by a nondegenerate bilinear form. With that form available, orthogonal complements become ideals, decompositions become canonical, and derivations become inner.

The prerequisites are proved in the [receiving companion](RT-LIE-foundations.md): Engel's theorem and elementary ideal/field-extension operations in Theorem RTF-001, and Lie's theorem in Theorem RTF-002. All spaces and Lie algebras here are finite-dimensional. The ground field has characteristic zero; the polynomial Jordan decomposition and its abstract version are discussed over an algebraically closed field, including \(\mathbb C\). Cartan's criteria, the ideal decomposition and the inner-derivation theorem hold over every characteristic-zero field. The freely readable comparisons are [Milne, Lie algebras], [Etingof] and, only for the prime-characteristic example, [Premet–Strade].

## 1. Separating eigenvalues from nilpotence

Call an endomorphism **semisimple** if it is diagonalizable over the algebraically closed field.

<a id="RTLIE03-L11"></a>
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

**Proof.** If the space is zero take both parts zero. Otherwise the least-degree monic annihilating polynomial factors as \(m(t)=\prod_\lambda(t-\lambda)^{d_\lambda}\). Polynomial division gives the Bézout identity for any two coprime factors, and repeated use of it gives the Chinese-remainder projections \(p_\lambda(t)\). Their values at X are orthogonal idempotents summing to the identity. The image of each is \(V_\lambda=\ker(X-\lambda)^{d_\lambda}\): the product \((t-\lambda)^{d_\lambda}p_\lambda(t)\) is divisible by m, and the residue of \(p_\lambda\) on this kernel is one. Thus these generalized eigenspaces form a direct sum.

Prescribe a polynomial p to have constant residue \(\lambda\) modulo each factor. If zero is an eigenvalue, the corresponding residue already makes \(p(0)=0\); if it is not, add the coprime prescription \(p\equiv0\pmod t\). Then \(S=p(X)\) is scalar \(\lambda\) on \(V_\lambda\), and \(N=X-S\) is nilpotent on each summand. The parts commute and both have polynomial expressions with zero constant term.

For uniqueness, any commuting decomposition \(X=S'+N'\) preserves every \(V_\lambda\), because both parts commute with X. Inside it, diagonalize \(S'\). Its eigenspaces are preserved by \(N'\), and X on an eigenspace of eigenvalue \(\mu\) has sole eigenvalue \(\mu\). Hence \(\mu=\lambda\); this identifies \(S'\) and then \(N'\).

The operator \(\operatorname{ad}S\) is diagonalizable on Hom blocks, with eigenvalue \(\lambda-\mu\) from \(V_\mu\) to \(V_\lambda\). The binomial formula in RTF-001 makes \(\operatorname{ad}N\) nilpotent. These operators commute and sum to \(\operatorname{ad}X\); the uniqueness just proved gives (1.1). \(\square\)

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

<a id="RTLIE03-T21"></a>
**Theorem 2.1 (Cartan's solvability criterion).** For a Lie subalgebra
\(\mathfrak l\subseteq\mathfrak{gl}(V)\) in characteristic zero,
\[
\mathfrak l\text{ solvable}
\quad\Longleftrightarrow\quad
\operatorname{tr}(XY)=0
\quad(X\in[\mathfrak l,\mathfrak l],\ Y\in\mathfrak l).
\tag{2.2}
\]

**Proof of necessity.** After scalar extension to an algebraic closure, RTF-002 gives a common upper-triangular flag for \(\mathfrak l\). Commutators have zero diagonal. Multiplying one by an upper-triangular matrix leaves zero diagonal and hence zero trace. Trace and bracket formation commute with scalar extension, proving the assertion over the original field.

**Proof of sufficiency.** RTF-001 proves that extension of the ground field preserves and reflects solvability, so assume it algebraically closed. Fix \(X\in[\mathfrak l,\mathfrak l]\), and let \(\lambda_i\) be its eigenvalues with multiplicities. Put \(E=\operatorname{span}_{\mathbb Q}\{\lambda_i\}\). For a rational linear map \(f:E\to\mathbb Q\), define \(Y_f\) to be scalar \(f(\lambda)\) on each generalized X-eigenspace. This operator need not lie in \(\mathfrak l\).

We first prove the precise normalizer property needed for the trace argument. Write \(X=S+N\) as in Lemma 1.1. On \(\operatorname{Hom}(V_\mu,V_\lambda)\), the respective commutator operators of S and \(Y_f\) are scalar \(\lambda-\mu\) and \(f(\lambda-\mu)\). Interpolate on this finite set of distinct differences, prescribing zero at zero. The resulting polynomial q has \(q(0)=0\) and satisfies \(\operatorname{ad}Y_f=q(\operatorname{ad}S)\). Lemma 1.1, applied to \(\operatorname{ad}X\), writes its semisimple part \(\operatorname{ad}S=p_0(\operatorname{ad}X)\) with \(p_0(0)=0\). Consequently
\[
\operatorname{ad}Y_f=q(p_0(\operatorname{ad}X)),\qquad
[Y_f,\mathfrak l]\subset[\mathfrak l,\mathfrak l].
\tag{2.3}
\]
Indeed, every positive power of \(\operatorname{ad}X\) sends \(\mathfrak l\) into its derived ideal. A polynomial identity for \(Y_f\) on V alone would not prove this conclusion.

Express X as a finite sum \(\sum[A_j,B_j]\). Trace-cyclicity and (2.3) give
\[
\sum_i\lambda_i f(\lambda_i)=\operatorname{tr}(XY_f)
=\sum_j\operatorname{tr}(A_j[B_j,Y_f])=0.
\tag{2.4}
\]
The first equality holds because the remaining nilpotent block of X has trace zero. Apply f to the equality in E: \(\sum_i f(\lambda_i)^2=0\). These are rational numbers; the ordering of \(\mathbb Q\) forces all \(f(\lambda_i)=0\). Rational coordinate functionals for a basis of E separate its vectors, so every \(\lambda_i=0\). This reasoning uses no ordering of the original field. X is therefore nilpotent.

All elements of \([\mathfrak l,\mathfrak l]\) have now been proved nilpotent as matrices. RTF-001 triangularizes this represented algebra strictly. An iterated commutator of sufficiently many strictly upper-triangular matrices is zero (each multiplication increases the distance above the diagonal); it is nilpotent and hence solvable. The quotient of \(\mathfrak l\) by it is abelian, and the solvable-extension argument of RTF-001 completes the proof. \(\square\)

## 3. An intrinsic bilinear form

For a representation \(\rho\), define its **trace form** and the **Killing form** by
\[
B_\rho(x,y)=\operatorname{tr}_V(\rho(x)\rho(y)),\qquad
\kappa_{\mathfrak g}(x,y)=
\operatorname{tr}_{\mathfrak g}(\operatorname{ad}x\,\operatorname{ad}y).
\]

<a id="RTLIE03-P31"></a>
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

**Proof.** The trace identity (2.1) gives invariance; bilinearity and symmetry follow from linearity and cyclicity of trace. For \(z\in I^\perp\), \(u\in I\), invariance gives \(B([x,z],u)=-B(z,[x,u])=0\), so \(I^\perp\) is an ideal. If x lies in I, \(\operatorname{ad}x\) maps the whole algebra into I. In a basis adapted to I its quotient diagonal block is zero. For x,y both in I the product thus has trace exactly that of its restriction to I, proving (3.2). \(\square\)

The restriction formula requires an ideal, not an arbitrary subalgebra.

<a id="RTLIE03-C32"></a>
**Corollary 3.2 (intrinsic solvability criterion).**
\[
\mathfrak g\text{ solvable}\quad\Longleftrightarrow\quad
\kappa_{\mathfrak g}([\mathfrak g,\mathfrak g],\mathfrak g)=0.
\]

**Proof.** The adjoint image has derived algebra \(\operatorname{ad}[\mathfrak g,\mathfrak g]\); its matrix trace pairing is precisely the Killing pairing in the statement. Theorem 2.1 therefore says that this image is solvable exactly under the indicated vanishing condition. Its kernel is the centre, an abelian ideal. The solvable-extension argument of RTF-001 shows that the adjoint image is solvable exactly when \(\mathfrak g\) is solvable. \(\square\)

Define **semisimple** by \(\operatorname{rad}(\mathfrak g)=0\). Equivalently there is no nonzero solvable ideal, or no nonzero abelian ideal. A nonzero solvable ideal has a last nonzero derived term which is abelian; Jacobi shows that this term is still an ideal of \(\mathfrak g\). Conversely every abelian ideal is solvable. The zero algebra is semisimple.

<a id="RTLIE03-T33"></a>
**Theorem 3.3 (Cartan's semisimplicity criterion).** A characteristic-zero Lie algebra is semisimple if and only if its Killing form is nondegenerate.

**Proof.** Denote the nullspace of the Killing form by R. Proposition 3.1 makes R an ideal, and its restriction formula identifies the Killing form of R with the zero restriction. Corollary 3.2 makes R solvable. A semisimple algebra has no such nonzero ideal, hence its form is nondegenerate.

For the converse take an abelian ideal A and \(a\in A\), \(y\in\mathfrak g\). The operator \(\operatorname{ad}a\operatorname{ad}y\) has image in A and vanishes on A: y preserves A, and a brackets to zero with A. Its diagonal blocks, in a basis starting with A, are both zero. Thus \(\kappa(a,y)=0\) for every y. Nondegeneracy forces \(a=0\), so A is zero. A nonzero solvable ideal would have a last nonzero derived term which is an abelian ideal of the whole algebra, as proved in RTF-001. Therefore there is no nonzero solvable ideal. The zero algebra satisfies both conditions. \(\square\)

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

<a id="RTLIE03-T51"></a>
**Theorem 5.1.** Every derivation of a characteristic-zero semisimple algebra is inner:
\[
\operatorname{Der}(\mathfrak g)=\operatorname{ad}\mathfrak g.
\]
Its inducing element is unique.

**Proof.** Let \(\mathfrak d=\operatorname{Der}(\mathfrak g)\). The derivation rule computes
\[
[D,\operatorname{ad}x]=\operatorname{ad}(Dx),
\tag{5.1}
\]
so \(\operatorname{ad}\mathfrak g\) is an ideal in \(\mathfrak d\). The centre of \(\mathfrak g\) is zero by Theorem 3.3, and this ideal is isomorphic to \(\mathfrak g\). Its restricted Killing form is its own Killing form, by Proposition 3.1, so is nondegenerate. Even if the form on all of \(\mathfrak d\) were degenerate, this nondegenerate restriction gives the vector-space decomposition
\(\mathfrak d=\operatorname{ad}\mathfrak g\oplus(\operatorname{ad}\mathfrak g)^\perp\).
Both spaces are ideals, and their intersection is zero, hence they commute. For D in the complement, (5.1) gives \(\operatorname{ad}(Dx)=0\) for every x. Zero centre then gives D=0. Thus all derivations belong to the adjoint ideal. The inducing element is unique for the same reason. No algebraic closure was used. \(\square\)

For later use, a faithful representation \(\rho\) of semisimple \(\mathfrak g\) also has nondegenerate trace form \(B_\rho\). Its radical \(R\) is an ideal by invariance. The trace form on the faithful image \(\rho(R)\) vanishes on all pairs, so Theorem 2.1 makes \(R\) solvable. Hence \(R=0\). The next lesson uses this observation to construct Casimir operators.

## 6. Jordan decomposition inside the Lie algebra

A polynomial in a derivation need not automatically be a derivation. To place its Jordan parts back in the algebra, first prove the relevant property.

<a id="RTLIE03-L61"></a>
**Lemma 6.1.** Over an algebraically closed characteristic-zero field, the semisimple and nilpotent parts of a derivation \(D\) are derivations.

**Proof.** In the generalized-eigenspace decomposition of D, the derivation rule gives
\[
(D-\lambda-\mu)[u,v]=[(D-\lambda)u,v]+[u,(D-\mu)v]
\quad(u\in V_\lambda,v\in V_\mu).
\]
Iterating r times produces the binomial sum of brackets with the two powers adding to r. If the two generalized nilpotence indices are p,q, every summand is zero for \(r\ge p+q-1\). Hence \([V_\lambda,V_\mu]\subset V_{\lambda+\mu}\), interpreted as zero when that eigenvalue is absent. D's semisimple part acts on this bracket by \(\lambda+\mu\), which is exactly the sum of its actions on the two arguments. The derivation rule follows on homogeneous pairs and then by bilinearity on all pairs. Subtract this derivation from D to obtain the nilpotent part, also a derivation. \(\square\)

<a id="RTLIE03-T62"></a>
**Theorem 6.2 (abstract Jordan decomposition).** In a semisimple algebra over an algebraically closed characteristic-zero field, every \(x\) decomposes uniquely as
\[
x=x_s+x_n,\qquad [x_s,x_n]=0,
\]
with \(\operatorname{ad}x_s\) semisimple and \(\operatorname{ad}x_n\) nilpotent. They are the respective Jordan parts of \(\operatorname{ad}x\).

**Proof.** The operator decomposition of \(\operatorname{ad}x\) in Lemma 1.1 has derivation parts by Lemma 6.1. Theorem 5.1 realizes them as \(\operatorname{ad}x_s\) and \(\operatorname{ad}x_n\), with unique inducing elements. Injectivity of the adjoint map converts their sum into \(x=x_s+x_n\) and their commuting property into \([x_s,x_n]=0\). Any second decomposition would give a second commuting Jordan decomposition of the same operator. Its uniqueness and adjoint injectivity identify both elements. \(\square\)

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

- **[Milne, Lie algebras]** J. S. Milne, [*Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00 (2013)](https://www.jmilne.org/math/CourseNotes/LAG.pdf), Chapter I, §§1, 3–5, especially Theorem 4.22 for inner derivations. The actual author-hosted PDF is the edition cited.
- **[Etingof]** P. Etingof, [*18.745: Lie Groups and Lie Algebras, I*, author-hosted lecture notes](https://math.mit.edu/~etingof/lnlg.pdf), Sections 13–15, especially Lemma 14.21 and Theorem 14.18 for the two Cartan criteria. These are comparison sources; the used proofs appear in full above and in the companion.
- **[Premet–Strade]** A. Premet and H. Strade, [*Classification of finite dimensional simple Lie algebras in prime characteristics*](https://arxiv.org/pdf/math/0601380), arXiv:math/0601380, §1, for the Witt-algebra comparison. The concrete example and its proof remain in Section 7.

# Lie algebras: definitions, examples and first constructions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Foundation proofs, source comparison and integration by GPT-6 Astra (OpenAI), Ultra; self-checked by that AI. Public domain (CC0). Linked human-source components retain their stated terms.*

Two linear operators need not commute. Their difference in the two possible orders, \(XY-YX\), carries a useful algebraic structure of its own. Lie algebras isolate that structure. We will learn how to form their quotients, let them act on vector spaces, recognize the classical matrix examples, and replace their brackets by relations in an associative algebra. We also classify the smallest examples, including the first complex algebra that equals its own derived algebra.

The prerequisites are [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40) and [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40). We use vector-space and field axioms, matrix multiplication, determinants and complex arithmetic. The programme's basis and complement proofs, developed from Jim Hefferon's work, supply the finite-basis results. Determinants and changes of basis proves the matrix identities, including multiplication, invertibility and the coordinate rule for brackets. The preliminary arguments below supply rank–nullity, quotient factorization and the square roots used later; tensor products are constructed in Section 3. Milne's freely available notes provide companion treatments of Lie algebras and algebraic groups; Judson's reader treats quotient rings. All Lie-algebra arguments used here are given below.

Unless explicitly stated otherwise, \(k\) is a field of characteristic zero. A Lie algebra need not be finite-dimensional; the dimension statements have their indicated finite-dimensional hypotheses. All tensor products are over the ground field. Associative algebras and their modules are unital, and representations are left actions.

## Before the brackets: linear and scalar foundations

**Lemma 0.1 (rank–nullity).** Let \(T:V\to W\) be linear over any field, with \(V\) finite-dimensional and no dimension restriction on \(W\). Then

\[
\dim V=\dim\ker T+\dim\operatorname{im}T.
\]

**Proof.** By the linked finite-basis theorem, choose a basis \(u_1,\ldots,u_r\) of the kernel and extend it to a basis \(u_1,\ldots,u_r,v_1,\ldots,v_s\) of \(V\). Applying \(T\) to a basis expansion shows that the \(T(v_j)\) span the image. If \(\sum c_jT(v_j)=0\), then \(\sum c_jv_j\) lies in the kernel. Express it in the \(u_i\); independence of the extended basis forces every \(c_j=0\). Thus the image has basis \(T(v_1),\ldots,T(v_s)\), and the dimensions are \(r+s,r,s\), respectively. Empty lists cover zero kernels or zero images. \(\square\)

**Lemma 0.2 (quotient algebras and factorization).** Let \(A\) be a unital associative algebra and \(I\) a two-sided ideal. The cosets \(A/I\) form an associative algebra. A unital algebra map \(f:A\to B\) factors uniquely through \(A/I\) exactly when \(I\subseteq\ker f\).

**Proof.** Put \((a+I)+(b+I)=a+b+I\), \(c(a+I)=ca+I\), and \((a+I)(b+I)=ab+I\). Addition and scalar multiplication are unchanged when representatives differ by elements of the subspace \(I\). For multiplication, replacing \(a,b\) by \(a+i,b+j\) changes the product by \(aj+ib+ij\in I\). Every vector-space law, associativity and distributivity now descends by applying the coset map to the corresponding equality in \(A\); the unit is \(1+I\). If \(f(I)=0\), define \(\bar f(a+I)=f(a)\). Differences in representatives map to zero, so this is a well-defined unital algebra map. Surjectivity of the coset map gives uniqueness. Conversely any factorization kills \(I\). This also allows the zero quotient when \(I=A\). \(\square\)

**Lemma 0.3 (complex square roots).** Every complex number has a square root.

**Proof.** First recall how the least-upper-bound axiom for the real numbers supplies nonnegative square roots. For \(a>0\), the nonempty set \(S=\{t\ge0:t^2\le a\}\) is bounded above by \(\max(1,a)\). Its supremum \(s\) is positive, since \(\min(1,a)/2\in S\). If \(s^2<a\), choose \(0<\epsilon<1\) with \((2s+1)\epsilon<a-s^2\); then \((s+\epsilon)^2<a\), contradicting the upper-bound property. If \(s^2>a\), choose \(0<\epsilon<s\) with \(2s\epsilon<s^2-a\). Then \((s-\epsilon)^2>a\), so every element of \(S\) is smaller than \(s-\epsilon\), contradicting the definition of \(s\). Thus \(s^2=a\). The case \(a=0\) is immediate; monotonicity of squaring on nonnegative reals gives uniqueness.

Write \(z=a+bi\), and set \(r=\sqrt{a^2+b^2}\), so \(r\ge|a|\). If \(u=\sqrt{(r+a)/2}>0\), put \(v=b/(2u)\). The identity \((r-a)(r+a)=b^2\) gives \(v^2=(r-a)/2\). Consequently \((u+iv)^2=a+bi\). If \(u=0\), then \(a=-r\) and \(b=0\); the number \(i\sqrt{-a}\) is a square root. These cases include \(z=0\). \(\square\)

The full theorem that every complex polynomial splits, not just a quadratic, has its proof in The Nullstellensatz and Jacobson rings, Lemma 5.1. Only Lemma 0.3 is needed for this lesson's symmetric-form calculation.

## 1. What the commutator remembers

A **Lie algebra** is a vector space \(\mathfrak g\) with a bilinear bracket satisfying

\[
[x,x]=0,\qquad
[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0.
\]

The first condition is **alternation**; the second is the **Jacobi identity**. Expanding \([x+y,x+y]=0\) gives \([x,y]=-[y,x]\). Conversely, this skew-symmetry implies alternation when \(2\ne0\) in \(k\). In characteristic two it does not, so alternation remains part of the definition even in our exercise over arbitrary fields.

The zero bracket makes any vector space an **abelian** Lie algebra. The Jacobi identity can also be written

\[
[x,[y,z]]=[[x,y],z]+[y,[x,z]]. \tag{1.1}
\]

This version says that bracketing with \(x\) obeys a product rule. It will explain both the adjoint action and many closure properties.

**Proposition 1.1 (commutators).** If \(A\) is an associative \(k\)-algebra, then \([a,b]=ab-ba\) makes its underlying vector space a Lie algebra.

**Proof.** Bilinearity and alternation follow from multiplication. Associativity permits us to omit parentheses in

\[
[a,[b,c]]=abc-acb-bca+cba.
\]

Its cyclic sum is zero: each of the six ordered products occurs once with each sign. This proves Jacobi. The argument works over every field. \(\square\)

In particular, \(\mathfrak{gl}(V)=\operatorname{End}_k(V)\) has this bracket. For \(V=k^n\), write \(\mathfrak{gl}_n(k)\). If \(E_{ij}\) has its only nonzero entry, equal to \(1\), in position \((i,j)\), multiplication gives

\[
[E_{ij},E_{rs}]=\delta_{jr}E_{is}-\delta_{si}E_{rj}. \tag{1.2}
\]

This formula is a quick way to check matrix brackets.

Our first noncommutative example is \(\mathfrak{sl}_2(k)\), the trace-zero two-by-two matrices. Set

\[
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

They form a basis and satisfy

\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h. \tag{1.3}
\]

Trace-zero matrices are closed under brackets because

\[
\operatorname{tr}(XY)=\sum_{i,j}X_{ij}Y_{ji}
=\operatorname{tr}(YX).
\]

Thus \(\mathfrak{sl}_2\) is a Lie subalgebra of \(\mathfrak{gl}_2\). It is not an associative subalgebra: \(h^2=I_2\) has nonzero trace in characteristic zero. A bracket and an associative product impose different closure conditions.

## 2. Subspaces, quotients and useful invariants

A **subalgebra** \(\mathfrak s\subseteq\mathfrak g\) is a linear subspace with \([\mathfrak s,\mathfrak s]\subseteq\mathfrak s\). An **ideal** \(I\) satisfies the stronger condition \([\mathfrak g,I]\subseteq I\). Here \([U,W]\) means the linear span of all brackets \([u,w]\), not merely their set.

A linear map \(\phi:\mathfrak g\to\mathfrak h\) is a **homomorphism** if \(\phi([x,y])=[\phi(x),\phi(y)]\). Its image is a subalgebra and its kernel is an ideal: bracket preservation proves both assertions immediately.

**Proposition 2.1 (quotients and isomorphism theorems).** If \(I\) is an ideal, the quotient vector space has the bracket

\[
[x+I,y+I]=[x,y]+I.
\]

For a homomorphism \(\phi\), there is an isomorphism

\[
\mathfrak g/\ker\phi\ \simeq\ \operatorname{im}\phi.
\]

If \(\mathfrak s\) is a subalgebra, then

\[
\mathfrak s/(\mathfrak s\cap I)\simeq(\mathfrak s+I)/I.
\]

If \(I\subseteq J\) are ideals, then

\[
(\mathfrak g/I)/(J/I)\simeq\mathfrak g/J.
\]

Subalgebras containing \(I\) correspond to subalgebras of \(\mathfrak g/I\); the correspondence also preserves ideals.

**Proof.** Replacing \(x,y\) by \(x+i,y+j\) changes their bracket by \([i,y]+[x,j]+[i,j]\), which lies in \(I\). Bilinearity, alternation and Jacobi therefore descend. The first displayed isomorphism sends \(x+\ker\phi\) to \(\phi(x)\); it is well-defined, injective, surjective onto the image, and preserves brackets.

The sum \(\mathfrak s+I\) is closed under brackets because all mixed terms lie in \(I\). Restrict the quotient map to \(\mathfrak s\); its kernel is \(\mathfrak s\cap I\) and its image is \((\mathfrak s+I)/I\). For the third theorem, the map \(x+I\mapsto x+J\) has kernel \(J/I\), so the first theorem applies again. Finally, image and inverse image under the quotient map are inverse operations on the indicated subalgebras. Bracketing with arbitrary elements shows that an ideal on either side gives an ideal on the other. \(\square\)

The **centre** and **derived algebra** are

\[
Z(\mathfrak g)=\{z:[z,x]=0\text{ for every }x\},\qquad
[\mathfrak g,\mathfrak g]=\operatorname{span}\{[x,y]\}.
\]

Both are ideals. The assertion for the centre follows from its definition; for the derived algebra use (1.1). The quotient by the derived algebra is abelian. More precisely, a map from \(\mathfrak g\) to an abelian Lie algebra kills every bracket and hence factors uniquely through this quotient. Thus it records all possible abelian images of \(\mathfrak g\).

For a subalgebra \(\mathfrak s\), define its **normalizer** and **centralizer** by

\[
N_{\mathfrak g}(\mathfrak s)=\{x:[x,\mathfrak s]\subseteq\mathfrak s\},\qquad
C_{\mathfrak g}(\mathfrak s)=\{x:[x,\mathfrak s]=0\}.
\]

They are subalgebras: for \(x,y\) in either one, apply

\[
[[x,y],s]=[x,[y,s]]-[y,[x,s]].
\]

The subalgebra \(\mathfrak s\) is an ideal in its normalizer, and its centralizer is also an ideal there. For the latter claim, if \(x\) normalizes \(\mathfrak s\) and \(y\) centralizes it, the same equation has both terms zero. In particular, \(\mathfrak s\) is an ideal of \(\mathfrak g\) exactly when \(N_{\mathfrak g}(\mathfrak s)=\mathfrak g\).

**Example 2.2 (a central bracket).** For \(m\ge1\), on a basis \(p_1,\ldots,p_m,q_1,\ldots,q_m,z\), put

\[
[p_i,q_j]=\delta_{ij}z
\]

and set all other basis brackets to zero, extending by alternation. Every bracket is central, so every double bracket vanishes and Jacobi holds. This is the **Heisenberg algebra** \(\mathfrak H_{2m+1}\). For \(m\ge1\), its centre and derived algebra are both \(kz\): bracketing a general vector with each \(p_j,q_j\) forces all its \(p\)- and \(q\)-coefficients to vanish if it is central. The quotient by \(kz\) is abelian of dimension \(2m\).

One matrix realization sends \(p_i\) to \(E_{1,i+1}\), \(q_i\) to \(E_{i+1,m+2}\), and \(z\) to \(E_{1,m+2}\). Equation (1.2) checks every bracket and the distinct matrix entries prove injectivity.

## 3. Product rules become representations

For any vector space \(A\) with a bilinear multiplication, a **derivation** is a linear map \(D:A\to A\) satisfying

\[
D(ab)=D(a)b+aD(b).
\]

No associativity is needed for this definition. In a Lie algebra the multiplication is the bracket.

**Proposition 3.1 (derivations and the adjoint action).** Derivations form a Lie subalgebra \(\operatorname{Der}_k(A)\subseteq\mathfrak{gl}(A)\). For a Lie algebra,

\[
\operatorname{ad}:\mathfrak g\longrightarrow\operatorname{Der}_k(\mathfrak g),\qquad
\operatorname{ad}(x)(y)=[x,y]
\]

is a homomorphism with kernel \(Z(\mathfrak g)\). Its image, the **inner derivations**, is an ideal in \(\operatorname{Der}_k(\mathfrak g)\).

**Proof.** Linear combinations preserve the product rule. Expanding \(DE(ab)-ED(ab)\), the terms \(E(a)D(b)\) and \(D(a)E(b)\) cancel, leaving

\[
[D,E](ab)=[D,E](a)b+a[D,E](b).
\]

Jacobi is inherited from \(\mathfrak{gl}(A)\). Equation (1.1) says that every \(\operatorname{ad}(x)\) is a derivation. On \(z\), Jacobi gives

\[
[\operatorname{ad}(x),\operatorname{ad}(y)]z
=[x,[y,z]]-[y,[x,z]]=[[x,y],z].
\]

The kernel assertion is exactly the definition of the centre. For any derivation \(D\), its product rule gives

\[
[D,\operatorname{ad}(x)](y)=D[x,y]-[x,Dy]=[Dx,y],
\]

which proves the ideal assertion. \(\square\)

For an associative algebra, the maps \(a\mapsto ba-ab\) are derivations, by a direct expansion of \([b,ac]\). Not every derivation has this form. On \(k[t]\), differentiation is nonzero, while all such commutator maps are zero. In fact every derivation of \(k[t]\) is \(r(t)\partial_t\): the rule for \(1\cdot1\) gives \(D(1)=0\), and its value \(r=D(t)\) determines \(D(t^j)=jt^{j-1}r\) by induction. Conversely, the polynomial product rule makes every \(r(t)\partial_t\) a derivation. Consequently

\[
[r\partial_t,s\partial_t]=(rs'-sr')\partial_t.
\]

A **representation** of \(\mathfrak g\) on \(V\) is a Lie homomorphism \(\rho:\mathfrak g\to\mathfrak{gl}(V)\). Equivalently, \(V\) is a **\(\mathfrak g\)-module** with a bilinear action \(xv=\rho(x)v\) satisfying

\[
[x,y]v=x(yv)-y(xv). \tag{3.1}
\]

A submodule is an invariant subspace; it gives a quotient module by \(x(v+W)=xv+W\). A module homomorphism \(T:V\to W\) obeys \(T(xv)=xT(v)\). A representation is **faithful** when its kernel is zero. Proposition 3.1 makes \(\mathfrak g\) its own adjoint module; this representation is faithful exactly when the centre vanishes.

For example, in the ordered basis \(e,h,f\),

\[
\operatorname{ad}(h)=\operatorname{diag}(2,0,-2),\quad
\operatorname{ad}(e)=\begin{pmatrix}0&-2&0\\0&0&1\\0&0&0\end{pmatrix},\quad
\operatorname{ad}(f)=\begin{pmatrix}0&0&0\\-1&0&0\\0&2&0\end{pmatrix}.
\]

These differ from the two-by-two matrices of the defining representation: a representation includes its space, not just the name of the acting algebra.

The tensor product \(V\otimes W\) is generated by symbols \(v\otimes w\) subject to bilinearity. More precisely, take the free vector space on the pairs \((v,w)\) and quotient by the relations expressing linearity in each argument. A bilinear map on \(V\times W\) kills these relations, so it extends uniquely to a linear map on the quotient. Iterating constructs higher tensor products. For modules \(V,W\), the following constructions give further modules:

| Space | Action of \(x\) |
|---|---|
| \(V\oplus W\) | \(x(v,w)=(xv,xw)\) |
| \(V^*=\operatorname{Hom}_k(V,k)\) | \((x\lambda)(v)=-\lambda(xv)\) |
| \(V\otimes W\) | \(x(v\otimes w)=xv\otimes w+v\otimes xw\) |
| \(\operatorname{Hom}_k(V,W)\) | \((xT)(v)=x(Tv)-T(xv)\) |

**Proposition 3.2.** These actions satisfy (3.1), without a finite-dimensional restriction.

**Proof.** The direct-sum assertion follows componentwise. For the dual,

\[
(x(y\lambda)-y(x\lambda))(v)
=\lambda(y(xv)-x(yv))=-\lambda([x,y]v).
\]

On a tensor product, write the operator as \(\rho_V(x)\otimes1+1\otimes\rho_W(x)\). Operators on different factors commute, so its commutator with the corresponding operator for \(y\) is the operator for \([x,y]\). Bilinearity makes the action well-defined. On \(\operatorname{Hom}(V,W)\), left composition by \(\rho_W(x)\) commutes with right composition by \(\rho_V(y)\). Expanding the commutator leaves \(\rho_W([x,y])T-T\rho_V([x,y])\), as required. \(\square\)

Thus the invariant elements of \(\operatorname{Hom}(V,W)\) are exactly the module homomorphisms. If \(V\) is finite-dimensional, the linear isomorphism \(W\otimes V^*\to\operatorname{Hom}(V,W)\), \(w\otimes\lambda\mapsto(v\mapsto\lambda(v)w)\), respects these actions; a basis and its dual show bijectivity. Without finite-dimensionality this need not be onto: its image consists of finite-rank maps, whereas the identity of an infinite-dimensional space has infinite rank.

For the defining \(\mathfrak{sl}_2\)-module with basis \(v_1,v_2\), \(ev_2=v_1\) and \(ev_1=0\). If \(\xi_1,\xi_2\) is its dual basis, \(e\xi_1=-\xi_2\). On the tensor square,

\[
e(v_2\otimes v_2)=v_1\otimes v_2+v_2\otimes v_1.
\]

The signs and the two terms are consequences of the action formulas, not choices to be made separately.

## 4. Matrices preserving forms

Let \(F\) be an invertible \(N\times N\) matrix. The infinitesimal form-preserving condition is

\[
X^{\mathsf T}F+FX=0. \tag{4.1}
\]

Indeed, for the bilinear form \(B(u,v)=u^{\mathsf T}Fv\), it is equivalent to \(B(Xu,v)+B(u,Xv)=0\). If \(F\) is symmetric, its solutions form the orthogonal Lie algebra \(\mathfrak{so}(F)\); for an alternating form on \(k^{2n}\), they form a symplectic Lie algebra.

**Proposition 4.1 (classical matrix algebras).** These solution spaces are Lie subalgebras. For \(n,N\ge1\),

\[
\dim\mathfrak{gl}_n=n^2,\quad
\dim\mathfrak{sl}_n=n^2-1,\quad
\dim\mathfrak{so}(F)=\frac{N(N-1)}2,\quad
\dim\mathfrak{sp}_{2n}=n(2n+1).
\]

**Proof.** If \(X,Y\) satisfy (4.1), then

\[
[X,Y]^{\mathsf T}F
=Y^{\mathsf T}X^{\mathsf T}F-X^{\mathsf T}Y^{\mathsf T}F
=FYX-FXY=-F[X,Y].
\]

Linearity gives the other closure conditions. The \(n^2\) matrix units form a basis of \(\mathfrak{gl}_n\). Trace is onto \(k\), since \(\operatorname{tr}(E_{11})=1\), so its kernel has dimension \(n^2-1\) by rank–nullity.

For symmetric \(F\), the invertible linear map \(X\mapsto FX\) identifies (4.1) with skew-symmetric matrices. Each entry strictly above the diagonal is free, the entries below are its negatives, and diagonal entries vanish because \(2\ne0\). This gives \(N(N-1)/2\). For alternating \(F=\Omega\), \((\Omega X)^{\mathsf T}=-X^{\mathsf T}\Omega=\Omega X\). Thus the solutions correspond to symmetric \(2n\times2n\) matrices, of dimension \((2n)(2n+1)/2=n(2n+1)\). \(\square\)

It is useful to see how the block equations depend on coordinates. Begin with the alternating matrix

\[
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
\]

For \(X=\begin{pmatrix}A&B\\C&D\end{pmatrix}\), block multiplication in \(X^{\mathsf T}J+JX=0\) gives \(C=C^{\mathsf T}\), \(B=B^{\mathsf T}\), and \(D=-A^{\mathsf T}\). Thus \(A\) is arbitrary and \(B,C\) are symmetric. This gives the same dimension \(n^2+2n(n+1)/2\) as Proposition 4.1.

For paired diagonal coordinates let \(R_N\) reverse the order of the standard basis. It satisfies \(R_N^{\mathsf T}=R_N=R_N^{-1}\). With \(P=\operatorname{diag}(I_n,R_n)\), one has \(P^{\mathsf T}JP=\begin{pmatrix}0&R_n\\-R_n&0\end{pmatrix}\). Accordingly we may use the models

\[
\mathfrak{so}_N(k)=\mathfrak{so}(R_N),\qquad
\Omega_{2n}=\begin{pmatrix}0&R_n\\-R_n&0\end{pmatrix},\qquad
\mathfrak{sp}_{2n}(k)=\{X:X^{\mathsf T}\Omega_{2n}+\Omega_{2n}X=0\}.
\]

The signs in \(\Omega_{2n}\) make the form alternating. The change of coordinates just displayed, or direct block multiplication, gives

\[
X=\begin{pmatrix}A&B\\C&-R_nA^{\mathsf T}R_n\end{pmatrix},\qquad
R_nB\text{ and }R_nC\text{ symmetric}.
\]

For example, the upper-left block equation is \(-C^{\mathsf T}R_n+R_nC=0\), the lower-right one is \(B^{\mathsf T}R_n-R_nB=0\), and the upper-right one is \(A^{\mathsf T}R_n+R_nD=0\). These prove all the stated conditions and their converse. The diagonal elements in either anti-diagonal model have opposite paired entries. For \(\mathfrak{so}_{2r+1}\) they are

\[
\operatorname{diag}(t_1,\ldots,t_r,0,-t_r,\ldots,-t_1);
\]

for \(\mathfrak{so}_{2r}\) and \(\mathfrak{sp}_{2r}\), omit the middle zero. Denote each such diagonal subalgebra by \(\mathfrak d\). It is abelian and equals its Lie-algebra normalizer. To see this, choose \(H\in\mathfrak d\) with all diagonal entries distinct, possible over an infinite field. If \([X,H]\in\mathfrak d\), its off-diagonal entries \((H_{jj}-H_{ii})X_{ij}\) force \(X\) to be diagonal. This also proves that its centralizer is \(\mathfrak d\). A Lie algebra \(\mathfrak a\) is nilpotent if the sequence \(\gamma_1=\mathfrak a,\ \gamma_{j+1}=[\mathfrak a,\gamma_j]\) reaches zero; a Cartan subalgebra is a nilpotent subalgebra equal to its normalizer. Since \(\mathfrak d\) is abelian, it is therefore a Cartan subalgebra.

A change of basis \(F'=P^{\mathsf T}FP\) identifies the form algebras by \(X\mapsto P^{-1}XP\). Over \(\mathbb C\), all nondegenerate symmetric forms are congruent, as the symmetric-form argument in Section 5 shows. Over \(\mathbb R\), one must specify the form. The next example uses \(I_3\), not \(R_3\).

**Example 4.2 (rotations and \(\mathfrak{su}(2)\)).** For \(u=(u_1,u_2,u_3)\), let

\[
\widehat u=\begin{pmatrix}0&-u_3&u_2\\u_3&0&-u_1\\-u_2&u_1&0\end{pmatrix}.
\]

Then \(\widehat u\,v=u\times v\). The vector triple-product identity gives

\[
[\widehat u,\widehat v]w
=v(u\cdot w)-u(v\cdot w)=(u\times v)\times w.
\]

That identity follows by expanding the three coordinates of the cross product. Hence \(u\mapsto\widehat u\) is a Lie isomorphism from \((\mathbb R^3,\times)\) to \(\mathfrak{so}(I_3)\): its entries show injectivity and every skew-symmetric matrix has this form. Jacobi for the cross product follows from this isomorphism.

The real algebra \(\mathfrak{su}(2)\) consists of trace-zero anti-Hermitian complex matrices. They are exactly

\[
\begin{pmatrix}ia&b+ic\\-b+ic&-ia\end{pmatrix},\qquad a,b,c\in\mathbb R.
\]

Conjugate transpose shows closure under commutators. In terms of (1.3), a real basis is

\[
T_1=-\frac{i}{2}(e+f),\qquad T_2=\frac12(f-e),\qquad T_3=-\frac{i}{2}h.
\]

Direct substitution gives \([T_1,T_2]=T_3\), \([T_2,T_3]=T_1\), and \([T_3,T_1]=T_2\). Thus \(\mathfrak{su}(2)\simeq(\mathbb R^3,\times)\). The same three matrices are a complex basis of \(\mathfrak{sl}_2(\mathbb C)\), so complexifying \(\mathfrak{su}(2)\) gives \(\mathfrak{sl}_2(\mathbb C)\).

The upper-triangular algebra \(\mathfrak b_n\) and strictly upper-triangular algebra \(\mathfrak n_n\) have dimensions \(n(n+1)/2\) and \(n(n-1)/2\). Products of upper-triangular matrices remain upper-triangular; their commutators have zero diagonal, since the diagonal of a product is the componentwise product of diagonals. Also \([\mathfrak b_n,\mathfrak n_n]\subseteq\mathfrak n_n\), by triangular multiplication. Thus \(\mathfrak n_n\) is an ideal in \(\mathfrak b_n\), and the quotient is the abelian diagonal algebra.

## 5. How much structure fits in three dimensions?

**Theorem 5.1 (small dimensions).** Over any field, an alternating Lie algebra of dimension at most two is abelian or isomorphic to the two-dimensional algebra with basis \(x,y\) and \([x,y]=y\). Over \(\mathbb C\), a three-dimensional Lie algebra with \([\mathfrak g,\mathfrak g]=\mathfrak g\) is isomorphic to \(\mathfrak{sl}_2(\mathbb C)\).

**Proof in dimensions at most two.** Dimensions zero and one are abelian by bilinearity and alternation. In dimension two, choose \(a,b\) and write \([a,b]=\alpha a+\beta b\). If this vector is zero, the algebra is abelian. Otherwise set \(y=[a,b]\). Then

\[
[a,y]=\beta y,\qquad [b,y]=-\alpha y.
\]

If \(\beta\ne0\), take \(x=\beta^{-1}a\); otherwise take \(x=-\alpha^{-1}b\). We obtain \([x,y]=y\), and \(x,y\) are independent since dependent vectors bracket to zero. This works also in characteristic two. Conversely, the indicated table satisfies Jacobi: its Jacobi expression is trilinear, vanishes when two arguments coincide by skew-symmetry and alternation, and every triple of basis vectors has a repetition. There is therefore exactly one nonabelian isomorphism class in dimension two. \(\square\)

**Proof in dimension three.** Choose a basis \(a,b,c\), and form the matrix

\[
M=\bigl([b,c]\ \ [c,a]\ \ [a,b]\bigr),
\]

whose columns are coordinates in that basis. These three brackets span the derived algebra, so the hypothesis says that \(M\) is invertible. Writing \(M=(m_{ij})\), the Jacobi expression on \(a,b,c\) is

\[
M\begin{pmatrix}m_{32}-m_{23}\\m_{13}-m_{31}\\m_{21}-m_{12}\end{pmatrix}.
\]

For example, \([a,[b,c]]=m_{21}[a,b]-m_{31}[c,a]\); the other two terms give the displayed expression. Jacobi and invertibility force \(M=M^{\mathsf T}\).

We need a short fact about complex symmetric forms. If a symmetric bilinear form \(B\) is nonzero, some \(v\) has \(B(v,v)\ne0\): otherwise \(B(v+w,v+w)-B(v,v)-B(w,w)=2B(v,w)\) would make \(B\) zero. For a nondegenerate form, every \(x\) is the sum of \(B(v,x)v/B(v,v)\) and a vector orthogonal to \(v\). This splits off the line \(kv\). Its orthogonal complement is nondegenerate, because a vector orthogonal to both the line and its complement is orthogonal to the whole space. Repeat this argument to obtain an orthogonal basis with nonzero diagonal values. Over \(\mathbb C\), rescaling its vectors by square roots makes all those values \(1\). Applied to \(M\), this gives an invertible matrix \(S\) with \(SMS^{\mathsf T}=I_3\).

To translate that fact back to brackets, let the columns of \(P\) be a new basis in old coordinates. The new bracket matrix is

\[
M'=\det(P)P^{-1}MP^{-\mathsf T}. \tag{5.1}
\]

Here \(P^{-\mathsf T}=(P^{-1})^{\mathsf T}\). Indeed, the old coordinate bracket is \(M(v\times w)\), where the cross product is the alternating coordinate formula. The identity

\[
(Pv)\times(Pw)=\det(P)P^{-\mathsf T}(v\times w)
\]

follows by taking its dot product with \(Pz\): both sides give \(\det(P)\det(v,w,z)\). Multiplying by \(P^{-1}\) proves (5.1).

Take \(P=S^{-1}\). Then \(M'=dI_3\), with \(d=\det(P)\ne0\). Rescale all three new basis vectors by \(d^{-1}\). The resulting basis \(u,v,w\) satisfies

\[
[u,v]=w,\qquad [v,w]=u,\qquad [w,u]=v.
\]

Finally put

\[
e'=u+iv,\qquad f'=-u+iv,\qquad h'=2iw.
\]

They are independent and direct calculation gives \([h',e']=2e'\), \([h',f']=-2f'\), \([e',f']=h'\). Sending them to \(e,f,h\) in (1.3) is the required isomorphism. \(\square\)

The hypothesis \([\mathfrak g,\mathfrak g]=\mathfrak g\), called **perfectness**, matters: the three-dimensional Heisenberg algebra has only a one-dimensional derived algebra. The real three-dimensional classification associated with Bianchi is a separate classification problem; no such classification is needed for this theorem.

## 6. Turning brackets into multiplication relations

In a representation, \(x\) acts as an operator, so products such as \(xyv=x(yv)\) have meaning. We now build one associative algebra that accounts for all such products at once.

For a vector space \(V\), its **tensor algebra** is

\[
T(V)=\bigoplus_{r\ge0}V^{\otimes r},\qquad V^{\otimes0}=k,
\]

with multiplication given by concatenation of tensors and unit \(1\in k\). For every linear map \(\ell:V\to A\) to an associative algebra there is a unique unital algebra map

\[
\widetilde\ell:T(V)\to A,\qquad
v_1\otimes\cdots\otimes v_r\mapsto\ell(v_1)\cdots\ell(v_r).
\]

The universal property of tensor products makes this well-defined; concatenation proves multiplicativity, and generation by \(V\) proves uniqueness.

Let \(J\) be the two-sided ideal in \(T(\mathfrak g)\) generated by

\[
x\otimes y-y\otimes x-[x,y],\qquad x,y\in\mathfrak g,
\]

where the bracket term lies in tensor degree one. Define the **universal enveloping algebra**

\[
U(\mathfrak g)=T(\mathfrak g)/J
\]

and write \(\iota:\mathfrak g\to U(\mathfrak g)\) for the natural linear map. The defining relations make \(\iota\) a Lie homomorphism to the commutator algebra of \(U(\mathfrak g)\).

**Proposition 6.1 (universality and modules).** For every unital associative \(k\)-algebra \(A\), restriction gives a bijection

\[
\operatorname{Hom}_{k\text{-alg}}(U(\mathfrak g),A)
\simeq
\operatorname{Hom}_{\mathrm{Lie}}(\mathfrak g,A_{\mathrm{comm}}).
\]

The pair \((U(\mathfrak g),\iota)\) is unique up to a unique isomorphism respecting \(\iota\). For any fixed vector space \(V\), its \(\mathfrak g\)-module structures correspond bijectively to its unital \(U(\mathfrak g)\)-module structures. This also identifies module homomorphisms.

**Proof.** A linear map \(\ell:\mathfrak g\to A\) extends uniquely to \(T(\mathfrak g)\). This extension kills \(J\) exactly when

\[
\ell(x)\ell(y)-\ell(y)\ell(x)=\ell([x,y]),
\]

which is precisely bracket preservation. Factoring through the quotient gives the claimed unique map. If another pair has this property, there are unique maps between the two pairs; each composite extends the respective structure map and therefore equals the identity. This proves uniqueness in the stated compatible sense.

A representation \(\rho:\mathfrak g\to\operatorname{End}(V)\) extends to \(U(\mathfrak g)\) by the bijection, giving a unital action. Conversely, restriction of a unital associative action gives (3.1). The two operations undo each other. A linear map commuting with every \(\rho(x)\) commutes with their products and linear combinations, hence with the whole enveloping algebra. The converse follows by restriction. \(\square\)

This proof does not yet show that \(\iota\) is injective. That is one consequence of the next theorem.

**Theorem 6.2 (Poincaré–Birkhoff–Witt).** For a Lie algebra over any field and a totally ordered basis \((x_i)_{i\in I}\), the products

\[
\iota(x_{i_1})\cdots\iota(x_{i_r}),\qquad
i_1\le\cdots\le i_r,\quad r\ge0,
\]

form a vector-space basis of \(U(\mathfrak g)\). The product for \(r=0\) is \(1\).

**Proof.** We first justify the tensor coordinates used in the argument. For each basis vector \(x_i\), its coefficient map \(c_i:\mathfrak g\to k\) is linear. Products of these coefficient maps define multilinear functions, and hence linear functions on each tensor power. They take value \(1\) on the selected basis tensor and \(0\) on every other basis tensor. Basis tensors span by multilinearity; applying the coefficient functions to any finite relation proves their independence. Thus finite words in the given basis form a basis of the tensor algebra, including the empty word in degree zero.

Choose a basis \(B\) of \(\mathfrak g\) with any total order. A word means a finite sequence of basis letters, regarded as a tensor; the empty word is \(1\). A word is ordered when its letters are nondecreasing. For a word \(w=x_1\cdots x_d\), let

\[
\operatorname{inv}(w)=\#\{(r,s):r<s,\ x_r>x_s\}.
\tag{6.2a}
\]

For adjacent letters \(x>y\), use the replacement

\[
AxyB\ \rightsquigarrow\ AyxB+A[x,y]B.
\tag{6.2b}
\]

A bracket is expanded in the chosen basis. This is a finite sum, even when the basis is infinite. The swapped term has the same length and one fewer inversion; every bracket term has smaller length. Consequently every new word is smaller in the lexicographic pair \((d,\operatorname{inv})\). These pairs are well-founded in \(\mathbb N^2\). Recursive reduction therefore terminates, with finite branching, without requiring the basis order itself to be a well-order.

We prove that the final linear combination of ordered words is independent of every choice in the reductions. The proof is simultaneous induction on \((d,\operatorname{inv})\). All reduced values of smaller words are already defined; extend their normal-form map \(N\) linearly. Compare two possible first replacements in \(w\).

If they choose the same pair, they coincide. If the pairs are disjoint, performing both replacements gives the same four-term expansion: both pairs swapped, either one replaced by its bracket, and both replaced by brackets. Each term has smaller measure, so its further normal form is independent by induction. The two choices thus have the same normal form.

The only overlapping case consists of three consecutive letters \(x>y>z\). Sorting the three ordinary letters along the two paths gives

\[
\begin{aligned}
L&=zyx+[y,z]x+y[x,z]+[x,y]z,\\
R&=zyx+z[x,y]+[x,z]y+x[y,z].
\end{aligned}
\tag{6.2c}
\]

These are identities of tensor expressions produced by (6.2b), with the surrounding words \(A,B\) left in place. The difference has one fewer letter than \(AxyzB\). For all expressions of that smaller length, induction already gives

\[
N\bigl(A(uv-vu)B\bigr)=N\bigl(A[u,v]B\bigr),
\qquad u,v\in\mathfrak g.
\tag{6.2d}
\]

Indeed, for basis letters in decreasing order this is the invariance of the lower-length normal form under its replacement; for increasing order it follows by reversing the pair, for equal letters by alternation, and for general \(u,v\) by bilinearity. Applying (6.2d) to the three differences in \(L-R\), their normal form is the normal form of

\[
A\bigl([[y,z],x]+[y,[x,z]]+[[x,y],z]\bigr)B=0.
\tag{6.2e}
\]

The equality is Jacobi. Hence the two overlapping choices also agree after normal reduction. This establishes the induction: define \(N(w)\) using any first replacement and the already-defined lower normal forms. The comparison proves this definition is independent of that first choice, and recursively of all subsequent choices. Ordered words are fixed by \(N\).

We now separate the relation ideal, using the normal form just proved. For any words \(A,B\) and any basis letters \(x,y\),

\[
N\bigl(A(xy-yx-[x,y])B\bigr)=0.
\tag{6.2f}
\]

For \(x>y\) this is (6.2b); the other cases follow as in (6.2d). Bilinearity gives it for all Lie elements. These contextual relations span the ideal \(J\), so \(N(J)=0\). Conversely, each replacement changes a tensor by an element of \(J\), so \(t-N(t)\in J\) for every tensor \(t\). If \(N(t)=0\), then \(t\in J\). Thus \(\ker N=J\), and the tensor algebra is the direct vector-space sum of \(J\) and the span of the ordered words.


Since \(N\) fixes every ordered word and has kernel \(J\), their images form a basis of \(T(\mathfrak g)/J=U(\mathfrak g)\). This proves the theorem in every characteristic and in arbitrary dimension. \(\square\)

The argument is also developed, with its further consequences, in [Universal enveloping algebras and PBW](RT-LIE-13.md#theorem-2-1). For a freely accessible human treatment, see [Milne's corrected author edition of *Algebraic Groups*](https://www.jmilne.org/math/Books/iAG2022.pdf).


In particular, the length-one products are independent, so \(\iota\) is injective. For a finite basis \(x_1,\ldots,x_n\), the basis consists of \(x_1^{a_1}\cdots x_n^{a_n}\) with \(a_j\ge0\), after identifying \(\mathfrak g\) with its image. These are vector-space coordinates, not an assertion that the algebra is commutative.

The filtration \(F_rU\) by products of length at most \(r\), with \(F_{-1}U=0\), has associated graded algebra \(\bigoplus F_rU/F_{r-1}U\). The commutator relation has lower degree than \(xy\), so degree-one symbols commute. There is consequently a canonical surjection from the symmetric algebra \(S(\mathfrak g)\) to this graded algebra. Swapping adjacent out-of-order generators by \(xy=yx+[x,y]\), induction on length and then the number of inversions shows that ordered monomials of length at most \(r\) span \(F_rU\). PBW makes them independent. Thus the graded map is an isomorphism: ordered monomials of length exactly \(r\) give bases on both sides. Here \(S(V)\) means the quotient of \(T(V)\) by \(v\otimes w-w\otimes v\). Given a basis of \(V\), maps sending those basis vectors to independent polynomial variables, and those variables back to the basis vectors in \(S(V)\), are inverse algebra maps. Its basis is therefore the finite commutative monomials in those variables.

**Example 6.3 (two presentations).** For an abelian algebra \(k^n\), the defining ideal is exactly the symmetric-algebra ideal, so \(U(k^n)=S(k^n)=k[t_1,\ldots,t_n]\). For \(\mathfrak{sl}_2\), it is generated by \(e,h,f\) with relations

\[
he-eh=2e,\qquad hf-fh=-2f,\qquad ef-fe=h.
\]

Bilinearity shows that the relations on a basis generate all defining relations. For the order \(f<h<e\), PBW gives basis \(f^ah^be^c\). For instance \(ef=fe+h\) rewrites a product but does not make it symmetric.

**Example 6.4 (canonical commutation).** In \(U(\mathfrak H_{2m+1})\), \(p_iq_j-q_jp_i=\delta_{ij}z\), with \(z\) central. The associative quotient by \(z-1\) therefore has

\[
p_iq_j-q_jp_i=\delta_{ij}1.
\]

It acts nontrivially on \(k[t_1,\ldots,t_m]\) by \(p_i=\partial_{t_i}\), \(q_i=t_i\), and \(z=1\): applying the product rule to a polynomial verifies every relation. This is an associative quotient, not a Lie quotient setting a vector \(z\) equal to a scalar. In characteristic zero it has no nonzero finite-dimensional unital module: taking traces of \([p_1,q_1]=1\) would give \(0=\dim V\) in \(k\).

## 7. Exercises with complete solutions

**Exercise 7.1 (easy).** Verify Jacobi in \(\mathfrak{gl}(V)\) by expansion, and verify that the solutions of \(X^{\mathsf T}F+FX=0\) are closed under brackets. Apply the latter to the orthogonal and symplectic forms above.

**Solution.** Expand the three terms as

\[
XYZ-XZY-YZX+ZYX,\quad
YZX-YXZ-ZXY+XZY,\quad
ZXY-ZYX-XYZ+YXZ.
\]

Every term cancels. For the form condition, transpose the commutator to get \(Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}\). Multiplication by \(F\), followed by \(X^{\mathsf T}F=-FX\) and \(Y^{\mathsf T}F=-FY\), gives \(-F[X,Y]\). Thus the bracket is a solution. The solution space is linear, and alternation and Jacobi are inherited from \(\mathfrak{gl}(V)\). Both choices of \(F\) qualify; this closure argument itself does not require a particular symmetry of \(F\).

**Exercise 7.2 (medium).** Over an arbitrary field, classify all alternating Lie brackets on a two-dimensional space up to isomorphism. Include characteristic two and verify existence of the nonabelian case.

**Solution.** Write \([a,b]=\alpha a+\beta b=y\). If \(\alpha=\beta=0\), the bracket is zero. Otherwise \([a,y]=\beta y\) and \([b,y]=-\alpha y\). Choose \(x=\beta^{-1}a\) when \(\beta\ne0\), and \(x=-\alpha^{-1}b\) otherwise. Then \([x,y]=y\); these vectors are independent since their bracket is nonzero. The table on \(x,y\) determines every bracket. Its Jacobi expression vanishes on triples with repeated basis vectors: for instance, \(J(x,x,y)=[x,[x,y]]+[x,[y,x]]=0\), with the remaining term zero. Trilinearity covers all triples. This cancellation remains valid in characteristic two, where the two terms are equal but sum to zero. The table is alternating by construction. The abelian and nonabelian cases cannot be isomorphic because their derived algebras have dimensions zero and one.

**Exercise 7.3 (medium).** Let a complex three-dimensional Lie algebra equal its derived algebra. Starting with the three columns \([b,c],[c,a],[a,b]\), produce a basis satisfying (1.3). Account for the determinant in the basis change.

**Solution.** The column matrix \(M\) is invertible because the columns span the algebra. Jacobi gives \(M(m_{32}-m_{23},m_{13}-m_{31},m_{21}-m_{12})^{\mathsf T}=0\), hence symmetry. Orthogonal splitting for the nondegenerate symmetric form and rescaling by complex square roots give \(SMS^{\mathsf T}=I\). For a basis matrix \(P\), the coordinate cross-product identity proves \(M'=\det(P)P^{-1}MP^{-\mathsf T}\). With \(P=S^{-1}\) this is \(dI\), where \(d=\det P\). Multiplying every basis vector by \(d^{-1}\) multiplies its bracket coefficients by \(d^{-1}\), so the new table is \([u,v]=w,[v,w]=u,[w,u]=v\). Now \(e'=u+iv,f'=-u+iv,h'=2iw\) form a basis. Calculation gives \([w,u+iv]=-i(u+iv)\), \([w,-u+iv]=i(-u+iv)\), and \([u+iv,-u+iv]=2iw\). These are exactly the three relations (1.3), and the corresponding basis map is the required isomorphism.

**Exercise 7.4 (hard).** Compute all derivations of \(\mathfrak{sl}_2(\mathbb C)\) directly, and show that each is inner. Do not use a cohomology theorem.

**Solution.** Write

\[
D(h)=ae+bh+cf,\quad D(e)=de+qh+rf,\quad D(f)=se+th+uf.
\]

Applying the product rule to \([h,e]=2e\) yields

\[
2de+2qh+2rf=2be-ch+2de-2rf.
\]

Thus \(b=0,q=-c/2,r=0\). Applying it to \([h,f]=-2f\) gives

\[
-2se-2th-2uf=ah+2se-2uf,
\]

so \(s=0,t=-a/2\). Finally the rule for \([e,f]=h\) gives \(d+u=0\). Every derivation must therefore have

\[
D(h)=ae+cf,\qquad D(e)=de-\frac c2h,\qquad
D(f)=-\frac a2h-df.
\]

Set \(z=-\frac a2e+\frac d2h+\frac c2f\). Its brackets with \(h,e,f\) are exactly these values, so \(D=\operatorname{ad}(z)\). Conversely Proposition 3.1 proves that every such map is a derivation. A vector commuting with \(h\) is a multiple of \(h\), and commuting also with \(e\) forces that multiple to vanish. Hence \(Z(\mathfrak{sl}_2)=0\), and \(z\) is unique.

## What this lesson does not prove

Theorem 6.2 includes the full Poincaré–Birkhoff–Witt proof for arbitrary dimension and characteristic, followed by its injectivity and associated-graded consequences. Later applications are developed in [Universal enveloping algebras and PBW](RT-LIE-13.md#theorem-2-1).

Finite-basis existence and extension are proved in the linked programme component. Lemmas 0.1–0.3 prove rank–nullity, quotient-algebra factorization and complex square roots here. The real scalar system is assumed to be an ordered field satisfying the least-upper-bound axiom. Tensor products and the tensor-algebra extension property are constructed above. Determinants and changes of basis, Theorems 2–4, proves determinant multilinearity, multiplication and matrix invertibility; Proposition 7 proves the coordinate rule in (5.1). Those determinant identities hold over every commutative ring, so they apply over all the fields used here. For arbitrary-dimensional PBW we start with a specified totally ordered basis: this is not a proof that every vector space has such a basis without a choice principle.

The connections with local groups are developed in the lessons *The second fundamental theorem and the group of parameters*, *The third fundamental theorem*, and *The adjoint group, composition and isomorphism*. Tangent spaces, Lie algebras of group schemes, and infinitesimal extensions belong to *Lie algebras and infinitesimal theory*. None of their group-existence or smoothness theorems is needed here.

## References

- **[Milne, Lie algebras]** J. S. Milne, *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 2013, Chapter I §1. [Author’s notes](https://www.jmilne.org/math/CourseNotes/LAG.pdf).
- **[Judson]** T. W. Judson, *Abstract Algebra: Theory and Applications*, 2026, §16.3, “Ring Homomorphisms and Ideals.” [Author’s reader](https://judsonbooks.org/aata-files/aata-html/rings-section-homomorphisms.html).
- **[Milne, Algebraic groups]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition, 2022. [Author’s edition](https://www.jmilne.org/math/Books/iAG2022.pdf). Its enveloping-algebra treatment accompanies the complete PBW argument in Section 6.

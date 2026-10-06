# Hilbert 90 in Noether's form and Galois descent

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A cocycle describes how a chosen basis fails to agree with its Galois conjugates. Hilbert 90 says that for vector spaces this discrepancy can always be removed by a change of basis. Noether's proof interprets the scalar discrepancy as an automorphism of a crossed-product algebra and removes it by inner conjugation. We prove both the direct and the algebraic statements, and descend vector spaces without assuming finite dimension.

The prerequisite is Crossed products and factor systems, including its independence of field automorphisms, trace-dual basis and Skolem–Noether input. Throughout, \(L/K\) is finite Galois with group \(G\), and \(n=[L:K]=|G|\). We retain its left-action convention: \((\sigma\tau)(x)=\sigma(\tau(x))\). There is no restriction on the characteristic.

## 1. Scalar Hilbert 90

A multiplicative **1-cocycle** is a family \(b_\sigma\in L^\times\) with

\[
b_{\sigma\tau}=b_\sigma\sigma(b_\tau).
\tag{1}
\]

This forces \(b_1=1\). A scalar **coboundary** can be written \(b_\sigma=c/\sigma(c)\), \(c\in L^\times\). Replacing \(c\) by its inverse gives the equally usual convention \(c^{-1}\sigma(c)\); the subgroup of coboundaries is the same. The quotient of cocycles by coboundaries is \(H^1(G,L^\times)\).

**Theorem 1.1 (Noether–Speiser Hilbert 90).** Every cocycle (1) is a coboundary. Thus \(H^1(G,L^\times)=1\).

**Proof.** Distinct field automorphisms are linearly independent as functions \(L\to L\), as proved in the preceding lesson. Since the coefficients \(b_\tau\) are nonzero, the function

\[
y\longmapsto\sum_{\tau\in G}b_\tau\tau(y)
\]

is not identically zero. Choose \(y\) so that its value \(c\) is nonzero. Applying \(\sigma\), using (1), and reindexing gives

\[
\sigma(c)=\sum_\tau\sigma(b_\tau)(\sigma\tau)(y)
 =b_\sigma^{-1}\sum_\tau b_{\sigma\tau}(\sigma\tau)(y)
 =b_\sigma^{-1}c.
\]

Hence \(b_\sigma=c/\sigma(c)\). No division by \(|G|\) is involved. \(\square\)

If \(G=\langle\sigma\rangle\) is cyclic of order \(n\), this gives the familiar norm formulation.

**Corollary 1.2 (cyclic Hilbert 90).** For \(b\in L^\times\),

\[
N_{L/K}(b)=1
\quad\Longleftrightarrow\quad
b=c/\sigma(c)\text{ for some }c\in L^\times.
\]

**Proof.** The norm of a quotient \(c/\sigma(c)\) is \(1\) by telescoping. Conversely, if \(N(b)=1\), put

\[
b_{\sigma^i}=\prod_{j=0}^{i-1}\sigma^j(b),\qquad 0\le i<n,
\]

with the empty product \(1\). Adding indices without a carry gives (1) directly; adding with a carry removes the full product \(N(b)=1\), so (1) still holds. Theorem 1.1, applied at \(\sigma\), gives the conclusion. \(\square\)

Hilbert's classical theorem concerns cyclic extensions. Speiser's finite Galois formulation covers arbitrary \(G\). Noether explicitly credits Speiser's 1919 result in the introduction to [Noether, work 41], before presenting her inner-automorphism proof. Her phrase “principal genus theorem in the minimal case” refers to this algebraic statement over arbitrary fields, distinct from the number-field theorem in the next lesson.

## 2. Descent of arbitrary vector spaces

A **semilinear Galois action** on an \(L\)-space \(W\) consists of additive bijections \(\rho_\sigma:W\to W\) satisfying

\[
\rho_\sigma(\ell w)=\sigma(\ell)\rho_\sigma(w),\qquad
\rho_\sigma\rho_\tau=\rho_{\sigma\tau},\qquad \rho_1=1.
\]

Write \(W^G=\{w:\rho_\sigma(w)=w\text{ for every }\sigma\}\). It is a vector space over \(K\), usually not over \(L\).

Choose a \(K\)-basis \(\alpha_1,\ldots,\alpha_n\) of \(L\) and its trace-dual basis \(\beta_1,\ldots,\beta_n\), with \(\operatorname{Tr}_{L/K}(\beta_i\alpha_j)=\delta_{ij}\). The preceding lesson proved that the trace pairing is nondegenerate, and established

\[
\sum_i\alpha_i\sigma(\beta_i)=
\begin{cases}1,&\sigma=1,\\0,&\sigma\ne1.\end{cases}
\tag{2}
\]

One can recover (2) directly: the identity \(x=\sum_i\alpha_i\operatorname{Tr}(\beta_i x)\), expanded as a sum of automorphisms applied to \(x\), determines these coefficients by their independence.

For \(c\in L\), define the twisted sum

\[
P_c(w)=\sum_{\sigma\in G}\rho_\sigma(cw).
\]

Reindexing the finite sum shows \(P_c(w)\in W^G\).

**Theorem 2.1 (Galois descent).** For every \(L\)-vector space \(W\), of arbitrary dimension, with semilinear Galois action, the map

\[
\Phi:L\otimes_K W^G\xrightarrow{\sim}W,
\qquad \ell\otimes v\longmapsto\ell v
\]

is an isomorphism. An explicit inverse is

\[
\Psi(w)=\sum_{i=1}^{n}\alpha_i\otimes P_{\beta_i}(w).
\tag{3}
\]

**Proof.** Formula (3) takes values in the stated tensor product. Using semilinearity and (2),

\[
\Phi\Psi(w)
 =\sum_{\sigma\in G}\left(\sum_i\alpha_i\sigma(\beta_i)\right)\rho_\sigma(w)=w.
\]

For \(v\in W^G\), the twisted sum satisfies

\[
P_{\beta_i}(\ell v)=\operatorname{Tr}_{L/K}(\beta_i\ell)v.
\]

Thus

\[
\Psi\Phi(\ell\otimes v)
 =\sum_i\alpha_i\otimes\operatorname{Tr}(\beta_i\ell)v
 =\ell\otimes v.
\]

Elementary tensors span, so the two maps are inverse. The inverse is automatically \(L\)-linear because \(\Phi\) is \(L\)-linear and bijective. The construction uses a finite basis only for \(L/K\); it imposes no dimension bound on \(W\). \(\square\)

If \(f:W\to V\) is \(L\)-linear and commutes with the actions, it restricts to a \(K\)-linear map \(W^G\to V^G\), and the descent isomorphisms recover \(f\) by scalar extension. Conversely every such map of invariant spaces extends to an equivariant \(L\)-linear map. This describes both objects and maps in descent.

An invariant subspace \(U\subseteq W\) satisfies \(U=L\otimes_K U^G\). The quotient also descends, with

\[
(W/U)^G\simeq W^G/U^G.
\]

For surjectivity in this last statement, choose \(a\in L\) with \(\operatorname{Tr}(a)=1\), possible by trace-pairing nondegeneracy. If a class \(\overline w\) is invariant, the invariant vector \(P_a(w)\) projects to \(\operatorname{Tr}(a)\overline w=\overline w\). The kernel is exactly \(U^G\).

Likewise an \(L\)-algebra \(A\) with semilinear action by unital algebra automorphisms descends to its \(K\)-algebra \(A^G\). The map \(L\otimes_K A^G\to A\) is bijective by Theorem 2.1 and multiplicative on elementary tensors, hence an algebra isomorphism. This also applies to infinite-dimensional algebras. Tensor products descend with the diagonal action: the canonical scalar-extension isomorphism identifies their invariant model with the tensor product of their two \(K\)-models.

## 3. Matrix Hilbert 90 and Noether's proof

A matrix 1-cocycle is a family \(A_\sigma\in\operatorname{GL}_r(L)\) with

\[
A_{\sigma\tau}=A_\sigma\sigma(A_\tau).
\tag{4}
\]

Two cocycles are equivalent if \(A'_\sigma=C^{-1}A_\sigma\sigma(C)\) for one \(C\in\operatorname{GL}_r(L)\). These equivalence classes form the pointed set \(H^1(G,\operatorname{GL}_r(L))\); it need not be a group. Its distinguished class is the constant identity cocycle.

**Theorem 3.1 (matrix Hilbert 90).** Every cocycle (4) has the form

\[
A_\sigma=B\sigma(B)^{-1}
\]

for some \(B\in\operatorname{GL}_r(L)\). Thus \(H^1(G,\operatorname{GL}_r(L))=1\).

**Proof.** On \(W=L^r\), set \(\rho_\sigma(v)=A_\sigma\sigma(v)\). Equation (4) makes this a semilinear action. Theorem 2.1 gives \(\dim_K W^G=r\). Put a \(K\)-basis of \(W^G\) into the columns of a matrix \(B\); these columns form an \(L\)-basis, so \(B\) is invertible. Invariance says \(A_\sigma\sigma(B)=B\). This is the displayed formula, and changing coordinates by \(B\) makes the cocycle the identity. \(\square\)

If one writes \(C=B^{-1}\), the same formula is \(A_\sigma=C^{-1}\sigma(C)\). This change of notation explains the two customary forms of matrix Hilbert 90. The matrix and the Galois action must retain their order.

Here is Noether's algebraic proof of the scalar theorem. Let \(b_\sigma\) satisfy (1), and take the split crossed product \(A(1)=\operatorname{End}_K(L)\), with the generators of the preceding lesson. The assignment

\[
x\longmapsto x\quad(x\in L),\qquad
u_\sigma\longmapsto b_\sigma u_\sigma
\tag{5}
\]

preserves the relations. Indeed the new units act on \(L\) by \(\sigma\), and their product is \(b_\sigma\sigma(b_\tau)u_{\sigma\tau}=b_{\sigma\tau}u_{\sigma\tau}\). It therefore defines an automorphism, with inverse obtained from \(b_\sigma^{-1}\).

Skolem–Noether makes (5) conjugation by a unit \(v\in A(1)\). Since it fixes \(L\) pointwise, \(v\) belongs to its centralizer, which is \(L\). Thus \(v\in L^\times\), and

\[
v u_\sigma v^{-1}=(v/\sigma(v))u_\sigma.
\]

Comparing with (5) gives \(b_\sigma=v/\sigma(v)\). This proves Hilbert 90 from the algebra theorems. In fact the same argument works with any factor system: changing its units by a 1-cocycle preserves that factor system. The split algebra is enough for the stated theorem.

There is also a module proof of the matrix version. The operators \(v\mapsto A_\sigma\sigma(v)\), together with multiplication by \(L\), make the \(K\)-space \(L^r\) a module over \(A(1)\). The untwisted operators \(v\mapsto\sigma(v)\) give another such module. The simple algebra \(A(1)=M_n(K)\) has one simple module type, namely \(L\), of \(K\)-dimension \(n\). Both modules are sums of \(r\) copies, so an intertwining isomorphism exists. Since it commutes with multiplication by \(L\), it is an \(L\)-linear invertible matrix \(B\). Intertwining the two Galois operators gives \(A_\sigma\sigma(B)=B\), proving Theorem 3.1 again. This shows how scalar inner conjugation and matrix change of basis are instances of the same simple-module mechanism.

## 4. The additive theorem in every positive degree

An additive 1-cocycle is a family \(z_\sigma\in L\) with

\[
z_{\sigma\tau}=z_\sigma+\sigma(z_\tau).
\]

Its coboundaries have the form \(z_\sigma=\sigma(v)-v\). A trace-one element gives an explicit solution: choose \(a\in L\), \(\operatorname{Tr}(a)=1\), and put

\[
v=-\sum_{\tau\in G}z_\tau\tau(a).
\]

Then \(\sigma(z_\tau)=z_{\sigma\tau}-z_\sigma\), so reindexing shows \(\sigma(v)=v+z_\sigma\). This proves additive \(H^1\)-vanishing in every characteristic.

For the higher groups, we give the cochain argument in full. For an additive \(G\)-module \(M\), a homogeneous \(q\)-cochain is an equivariant function \(f:G^{q+1}\to M\), meaning

\[
f(\sigma g_0,\ldots,\sigma g_q)=\sigma f(g_0,\ldots,g_q).
\]

Its differential is

\[
(df)(g_0,\ldots,g_{q+1})
 =\sum_{i=0}^{q+1}(-1)^i f(g_0,\ldots,\widehat{g_i},\ldots,g_{q+1}).
\]

The hat means omission. Every pair of omitted indices occurs twice with opposite signs in \(d^2\), so \(d^2=0\). The quotient of cocycles by coboundaries in this complex is \(H^q(G,M)\). In degree one it gives the additive cocycle formula above, by setting \(z_g=f(1,g)\).

We state the **normal basis theorem** with its precise input: there is \(\theta\in L\) such that \(\{g(\theta):g\in G\}\) is a \(K\)-basis of \(L\) [Milne, Theorem 5.18]. It identifies the additive \(G\)-module \(L\) with the permutation module \(K^G\), with

\[
(\sigma m)(h)=m(\sigma^{-1}h).
\]

**Theorem 4.1 (additive acyclicity).** \(H^q(G,L)=0\) for every \(q\ge1\).

**Proof.** By the stated normal basis theorem, it is enough to use \(M=K^G\). An equivariant cochain with values in \(K^G\) is uniquely determined by the arbitrary scalar-valued function

\[
\psi(g_0,\ldots,g_q)=f(g_0,\ldots,g_q)(1).
\]

The inverse construction is

\[
f(g_0,\ldots,g_q)(h)=\psi(h^{-1}g_0,\ldots,h^{-1}g_q).
\]

It is equivariant for the specified permutation action. These bijections commute with the omission differential. Thus the cochain complex becomes all functions \(G^{q+1}\to K\), without an equivariance requirement. On this complex define, for \(q\ge1\),

\[
(s\psi)(g_0,\ldots,g_{q-1})=\psi(1,g_0,\ldots,g_{q-1}).
\]

Expanding \(ds\psi+sd\psi\), the term omitting the first entry \(1\) in \(sd\psi\) is \(\psi(g_0,\ldots,g_q)\); every other term cancels the matching term in \(ds\psi\). Hence \(ds+sd=1\) in every positive degree. If \(d\psi=0\), then \(\psi=d(s\psi)\), so every positive-degree cocycle is a coboundary. \(\square\)

The normal basis theorem is the only existence theorem imported into this higher-degree proof. The contracting map itself is displayed, so no vanishing result for an induced module is left implicit. In degree zero, the invariants are \(L^G=K\); they do not vanish.

## 5. Three concrete calculations

For \(L=\mathbb Q(i)\), conjugation is the generator. If \(c=a+bi\ne0\), then

\[
\frac{c}{\overline c}
 =\frac{a^2-b^2}{a^2+b^2}
   +\frac{2ab}{a^2+b^2}i.
\]

The two rational coordinates lie on the unit circle. Conversely, if \(z=x+yi\) has norm \(1\) and \(z\ne-1\), choose \(c=1+z\): because \(\overline z=z^{-1}\), the quotient \((1+z)/(1+\overline z)\) is \(z\). Taking \(t=b/a\) gives all rational points other than \((-1,0)\):

\[
x=\frac{1-t^2}{1+t^2},\qquad
y=\frac{2t}{1+t^2},\qquad t\in\mathbb Q.
\]

The missing point is obtained from a purely imaginary \(c\). For \(t=s/r\), clearing denominators gives the Pythagorean triple \((r^2-s^2,2rs,r^2+s^2)\). The choice \((r,s)=(2,1)\) gives \((3,4,5)\).

For a complex vector space with a conjugate-linear involution \(T\), its invariant space is a real form. Every \(w\) has the explicit decomposition

\[
w=\frac{w+T(w)}2
 +i\frac{w-T(w)}{2i},
\]

where both displayed coefficients are invariant. The decomposition is unique by applying \(T\) and adding and subtracting. For \(T(z_1,z_2)=(\overline z_2,\overline z_1)\), the real form consists of \((z,\overline z)\), with real basis \((1,1)\), \((i,-i)\). Its basis matrix

\[
B=\begin{pmatrix}1&i\\1&-i\end{pmatrix}
\]

satisfies \(A\overline B=B\), where \(A=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). Thus \(A=B\overline B^{-1}\), exactly the matrix Hilbert 90 identity. No dimension restriction is needed for the real-form decomposition itself.

Finally take \(L=\mathbb F_{q^n}\), \(K=\mathbb F_q\), and \(\sigma(x)=x^q\). Then

\[
N_{L/K}(x)=x^{1+q+\cdots+q^{n-1}}.
\]

Cyclic Hilbert 90 gives \(N(x)=1\) exactly when \(x=b^{1-q}\), equivalently \(x=c^{q-1}\) after putting \(c=b^{-1}\). The multiplicative group of a finite field is cyclic. Consequently the image of \(c\mapsto c^{q-1}\) has size \((q^n-1)/(q-1)\), equal to the size of the norm-one subgroup. The norm map has image all \(q-1\) nonzero elements of \(\mathbb F_q\). For \(\mathbb F_4/\mathbb F_2\), every nonzero element has norm \(1\), and exponent \(q-1=1\) gives all three of them.

## 6. Exercises

**Exercise 6.1 (easy).** Use Hilbert 90 for \(\mathbb Q(i)/\mathbb Q\) to parametrize all rational solutions of \(x^2+y^2=1\). Identify the point missing from the finite parameter and produce a Pythagorean triple.

**Exercise 6.2 (medium).** Suppose only the matrix Hilbert 90 statement is given. Prove descent for a finite-dimensional \(L\)-vector space with semilinear action. Explain which part of the argument requires finite dimension, and how section 2 removes that restriction.

**Exercise 6.3 (medium).** Show that every norm-one element of \(\mathbb F_{q^n}\) over \(\mathbb F_q\) is \(c^{q-1}\). Determine the kernel and image sizes of this power map and the size of every fiber of the norm map.

**Exercise 6.4 (medium).** Starting with a normal basis \(e_h=h(\theta)\), prove \(H^1(G,L)=0\) by an explicit formula in coordinates. If \(z_g=\sum_h z_{g,h}e_h\) is an additive cocycle, find coefficients \(v_h\in K\) for which \(z_g=gv-v\).

**Exercise 6.5 (hard).** Give the crossed-product proof of scalar Hilbert 90 in full: verify the proposed automorphism and its inverse, compute the centralizer of \(L\), apply Skolem–Noether, and check the final sign. Show that the proof works for an arbitrary factor system, even when its algebra does not split.

## 7. Solutions

**Solution 6.1.** Write \(z=x+iy\). The equation is exactly \(N(z)=1\), so \(z=c/\overline c\) for a nonzero \(c=a+bi\), with \(a,b\in\mathbb Q\). Multiplying numerator and denominator by \(a+bi\) gives

\[
x=\frac{a^2-b^2}{a^2+b^2},\qquad
y=\frac{2ab}{a^2+b^2}.
\]

If \(a\ne0\), put \(t=b/a\), obtaining \(x=(1-t^2)/(1+t^2)\), \(y=2t/(1+t^2)\). If \(a=0\), the point is \((-1,0)\). Conversely these formulas satisfy the circle equation, and a point with \(x\ne-1\) has parameter \(t=y/(1+x)\), as direct substitution verifies. Thus the list is exhaustive. Taking \(a=2,b=1\) gives \((x,y)=(3/5,4/5)\) and the triple \((3,4,5)\); for arbitrary integers \(a,b\), the identity is \((a^2-b^2)^2+(2ab)^2=(a^2+b^2)^2\).

**Solution 6.2.** Choose an \(L\)-basis of \(W\), of size \(r\). In these coordinates each action has the form \(v\mapsto A_\sigma\sigma(v)\), and the action law gives \(A_{\sigma\tau}=A_\sigma\sigma(A_\tau)\). Matrix Hilbert 90 gives \(A_\sigma=B\sigma(B)^{-1}\). Change coordinates by writing \(v=Bx\). Then

\[
\rho_\sigma(Bx)=A_\sigma\sigma(B)\sigma(x)=B\sigma(x).
\]

The invariant coordinates are exactly \(x\in K^r\). Thus the columns of \(B\) are a \(K\)-basis of \(W^G\) and an \(L\)-basis of \(W\). The map \(L\otimes_K W^G\to W\) carries the scalar extension of the first basis to the second, and is an isomorphism. Finite dimension entered when an element of \(\operatorname{GL}_r(L)\) described the entire action. This argument alone does not justify the statement for infinite-dimensional \(W\). Formula (3) gives both inverse identities on every vector and every elementary tensor using just the finite trace-dual basis of the field extension, so it proves that statement independently.

**Solution 6.3.** Let \(\sigma(x)=x^q\). If \(N(x)=1\), cyclic Hilbert 90 gives \(x=b/\sigma(b)=b^{1-q}\). Set \(c=b^{-1}\); then \(x=c^{q-1}\). Conversely

\[
N(c^{q-1})=c^{(q-1)(1+q+\cdots+q^{n-1})}
=c^{q^n-1}=1.
\]

The kernel of the power map consists of the nonzero roots of \(T^{q-1}-1\), which are exactly \(\mathbb F_q^\times\); it has size \(q-1\). Its image consequently has size \((q^n-1)/(q-1)\). To check the norm's image directly, take a generator \(g\) of the cyclic group \(\mathbb F_{q^n}^\times\). Its norm \(g^{(q^n-1)/(q-1)}\) has order \(q-1\), so generates \(\mathbb F_q^\times\). Every fiber of this surjective group homomorphism is a coset of its kernel, and therefore has size \((q^n-1)/(q-1)\). For \(n=1\), these assertions reduce to the norm being the identity and the power image being \(\{1\}\).

**Solution 6.4.** In the normal basis, \(g e_h=e_{gh}\), hence the coefficient of \(e_h\) in \(g z_s\) is \(z_{s,g^{-1}h}\). The cocycle condition is therefore

\[
z_{gs,h}=z_{g,h}+z_{s,g^{-1}h}.
\]

Set \(v_h=z_{h^{-1},1}\) and \(v=\sum_h v_h e_h\). Apply this displayed identity with its two group indices \(h^{-1},g\), and its coefficient index \(1\). It gives

\[
z_{h^{-1}g,1}=z_{h^{-1},1}+z_{g,h}.
\]

Since \((g^{-1}h)^{-1}=h^{-1}g\), this says \(v_{g^{-1}h}-v_h=z_{g,h}\). These are exactly the coefficients of \(gv-v\), proving the claim. No coefficient average or division by the group order occurs. The normal basis is the one imported field theorem in this argument.

**Solution 6.5.** Fix a normalized factor system \(a\), with \(u_\sigma x=\sigma(x)u_\sigma\) and \(u_\sigma u_\tau=a(\sigma,\tau)u_{\sigma\tau}\). Send \(x\in L\) to itself and \(u_\sigma\) to \(b_\sigma u_\sigma\). The commutation relation with \(x\) is preserved. Moreover

\[
(b_\sigma u_\sigma)(b_\tau u_\tau)
=b_\sigma\sigma(b_\tau)a(\sigma,\tau)u_{\sigma\tau}
=a(\sigma,\tau)b_{\sigma\tau}u_{\sigma\tau}.
\]

Thus multiplication is preserved, and so is the identity because \(b_1=1\). The inverse rescales each \(u_\sigma\) by \(b_\sigma^{-1}\). These inverse scalars are again a cocycle, since the field scalars commute. The map is therefore an automorphism of the central simple algebra \(A(a)\), whose simplicity was proved in lesson 5.

If \(z=\sum_\sigma z_\sigma u_\sigma\) centralizes every \(x\in L\), coefficient comparison gives \(z_\sigma(\sigma(x)-x)=0\) for every \(x\). For \(\sigma\ne1\), some \(x\) has \(\sigma(x)\ne x\), so \(z_\sigma=0\). Hence the centralizer is precisely \(L\). Skolem–Noether writes the automorphism as conjugation by a unit \(v\in A(a)\). Its fixing \(L\) puts \(v\) in this centralizer, so \(v\in L^\times\). Finally

\[
v u_\sigma v^{-1}=v\sigma(v^{-1})u_\sigma
=\frac{v}{\sigma(v)}u_\sigma,
\]

which gives the required \(b_\sigma=v/\sigma(v)\). Nothing in the proof requires \(A(a)\) to split. Taking \(a=1\) recovers Noether's proof through \(\operatorname{End}_K(L)\).

## Sources and further reading

- **[Noether, work 41]** Emmy Noether, *Der Hauptgeschlechtssatz für relativ-galoissche Zahlkörper*, Mathematische Annalen **108** (1933), 411–419, introduction and §1, “Hauptgeschlechtssatz im Minimalen.” Her introduction credits Speiser's 1919 formulation, and §1 gives the crossed-product argument. The [English collected edition](https://github.com/KokunoYumeto/emmy-noether-en) provides a companion reading text. Section 3 translates the argument into the left-action convention used throughout this course.
- **[Milne FT]** J. S. Milne, *Fields and Galois Theory*, chapter 5: independence of characters, the normal basis theorem (Theorem 5.18), and Hilbert's Theorem 90. The [author's notes](https://www.jmilne.org/math/CourseNotes/FT.pdf) provide an open source for the imported normal basis theorem.
- **[Milne CFT]** J. S. Milne, *Class Field Theory*, version 4.03, 2020, chapter II, Proposition 1.22 (Noether's form of Hilbert's Theorem 90) and Proposition 4.2 (continuous cohomology of a profinite group as a direct limit). The [author's notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf) are freely available.

For a field \(K\), let \(G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K)\). With continuous cochains and the discrete coefficient module \((K^{\mathrm{sep}})^\times\), the profinite form is

\[
H^1_{\mathrm{cont}}(G_K,(K^{\mathrm{sep}})^\times)=1.
\]

It follows from Theorem 1.1. A continuous 1-cocycle with values in the discrete module \((K^{\mathrm{sep}})^\times\) is locally constant and takes finitely many values, so it factors through \(\operatorname{Gal}(L/K)\), with values in \(L^\times\), for a finite Galois subextension \(L\); there it is a coboundary [Milne CFT, chapter II, Propositions 1.22 and 4.2]. The planned lesson AG-ET-08, *Galois cohomology*, treats profinite cohomology in general; it is an optional further path, rather than an additional hypothesis for any finite-extension theorem above. The planned NOE-RAT-02 uses descent for the no-name lemma. The next lesson, *The principal genus theorem*, returns to Noether's §2 and distinguishes its arithmetic hypotheses from the field-independent theorem proved here.

## What this lesson does not prove

The normal basis theorem is stated with its precise locator and used to prove the higher additive vanishing; it is not proved here. Finite-field structure and the usual finite Galois theory are prerequisites. The continuous multiplicative statement over a separable closure is reduced above to the finite case. All five finite-extension assertions in the programme, descent of subspaces, quotients and algebras, the three examples, and the five exercise solutions are proved above. The number-field principal genus theorem requires the additional arithmetic inputs specified in the next lesson.

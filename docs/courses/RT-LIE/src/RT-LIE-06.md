# Low-degree cohomology, Whitehead's lemmas and the Levi decomposition

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independently authored exposition: CC0. Cited human works retain their authorship and terms.*

A linear lift of a quotient Lie algebra need not preserve brackets. Its failure is an alternating bilinear map. Changing the lift changes that map by a coboundary. This connects a concrete splitting problem to cohomology. For a semisimple quotient the relevant cohomology vanishes, and successive splittings separate the radical from a semisimple subalgebra.

The structure theorems in this lesson concern finite-dimensional Lie algebras and modules over a field \(k\) of characteristic zero. In particular they apply over \(\mathbb C\) and \(\mathbb R\). The elementary cochain and extension constructions work over any field. We use the radical and solvable-extension results from [Nilpotent and solvable Lie algebras: Engel's and Lie's theorems](RT-LIE-02.md), the Killing form, ideal complements and inner derivations from [The Killing form and Cartan's criteria](RT-LIE-03.md), and the Casimir construction and Weyl's theorem from [Complete reducibility: Casimir elements and Weyl's theorem](RT-LIE-04.md). No root-system classification is required. This lesson can be omitted on a first reading of that classification.

## 1. The failure of a lift to preserve brackets

Fix a Lie algebra \(\mathfrak a\) and an \(\mathfrak a\)-module \(V\). Write its action as \(xv=\rho(x)v\). An **abelian extension with this action** is an exact sequence of Lie algebras
\[
0\longrightarrow V\longrightarrow E
\xrightarrow{\pi}\mathfrak a\longrightarrow0,
\tag{1.1}
\]
where the kernel has zero bracket and \([s(x),v]=xv\) for a linear section \(s\) of \(\pi\). This action is independent of the section: two lifts of \(x\) differ by an element of the abelian kernel. Jacobi gives
\[
[s(x),[s(y),v]]-[s(y),[s(x),v]]
=[[s(x),s(y)],v]=[s([x,y]),v],
\]
so the induced action is a representation.

Choose a linear section and define its **defect**
\[
c(x,y)=[s(x),s(y)]-s([x,y])\in V.
\tag{1.2}
\]
It is alternating. In the resulting vector-space coordinates \((x,v)\in\mathfrak a\oplus V\), the bracket of \(E\) is
\[
[(x,v),(y,w)]
=\bigl([x,y],\,xw-yv+c(x,y)\bigr).
\tag{1.3}
\]
The Jacobi identity on three lifted elements says exactly
\[
\begin{aligned}
0={}&xc(y,z)-yc(x,z)+zc(x,y)\\
&-c([x,y],z)+c([x,z],y)-c([y,z],x).
\end{aligned}
\tag{1.4}
\]
For example, substituting (1.2), the first line and the bracket-defect terms together give the Jacobi sum of \(s(x),s(y),s(z)\), minus the section applied to the Jacobi sum in \(\mathfrak a\). Both are zero.

Changing the section to \(s+b\), with \(b:\mathfrak a\to V\) linear, changes the defect to
\[
c'(x,y)=c(x,y)+xb(y)-yb(x)-b([x,y]).
\tag{1.5}
\]
The term \([b(x),b(y)]\) vanishes because the kernel is abelian. Thus the obstruction to a Lie section is the defect modulo precisely these changes. The next section gives that quotient its usual name.

An abelian kernel need not be central. It is central exactly when the specified quotient action on \(V\) is zero.

## 2. Cochains and the three low-degree interpretations

Put
\[
C^p(\mathfrak a,V)=\operatorname{Hom}_k(\bigwedge^p\mathfrak a,V),
\qquad C^0(\mathfrak a,V)=V.
\]
These are alternating multilinear maps. Define the **Chevalley–Eilenberg differential** by
\[
\begin{aligned}
(d\omega)(x_0,\ldots,x_p)
={}&\sum_{i=0}^p(-1)^i x_i
 \omega(x_0,\ldots,\widehat{x_i},\ldots,x_p)\\
&+\sum_{0\le i<j\le p}(-1)^{i+j}
 \omega([x_i,x_j],x_0,\ldots,
 \widehat{x_i},\ldots,\widehat{x_j},\ldots,x_p).
\end{aligned}
\tag{2.1}
\]
A hat means omission; the remaining arguments retain their original order. In the second sum the bracket is the first argument. In particular,
\[
(dv)(x)=xv,
\tag{2.2}
\]
\[
(df)(x,y)=xf(y)-yf(x)-f([x,y]),
\tag{2.3}
\]
and \(dc\) is the expression in (1.4). These specify the maps
\(C^0\to C^1\to C^2\to C^3\) needed here.

**Lemma 2.1.** This differential has \(d^2=0\).

**Proof.** In degree zero the value on \(x,y\) is
\[
(d^2v)(x,y)
=(\rho(x)\rho(y)-\rho(y)\rho(x)-\rho([x,y]))v=0.
\]
In degree one, writing \(R(x,y)=
\rho(x)\rho(y)-\rho(y)\rho(x)-\rho([x,y])\), expansion of (2.3) and (1.4) gives
\[
\begin{aligned}
(d^2f)(x,y,z)
={}&R(x,y)f(z)+R(y,z)f(x)+R(z,x)f(y)\\
&+f([[x,y],z]+[[y,z],x]+[[z,x],y])=0.
\end{aligned}
\]
The first line uses the module identity; the second uses Jacobi.

For completeness the same cancellation proves all degrees. Group the terms in two applications of (2.1) by the original arguments removed. For each pair \(i<j\), the two coefficient actions and the action of their bracket have common factor
\((-1)^{i+j-1}\) and sum
\[
(-1)^{i+j-1}R(x_i,x_j)
\,\omega(x_0,\ldots,\widehat{x_i},\ldots,
\widehat{x_j},\ldots).
\]
Terms with one coefficient action and a bracket on two other arguments cancel: moving the acted-on argument across the bracket insertion reverses their omission sign. Two brackets on disjoint pairs also cancel between the two orders of insertion; the two inserted bracket arguments change places in the alternating cochain. The remaining double brackets use three arguments. In their original increasing order their sum is, up to one common sign, the cochain evaluated with first argument
\[
[[x_i,x_j],x_\ell]+[[x_j,x_\ell],x_i]+[[x_\ell,x_i],x_j].
\]
Jacobi kills this sum. These exhaust the possible terms, proving \(d^2=0\). \(\square\)

Write \(Z^p=\ker d\), \(B^p=\operatorname{im}d\), with \(B^0=0\), and
\[
H^p(\mathfrak a,V)=Z^p/B^p.
\]

**Proposition 2.2.** The low-degree cohomology has the following interpretations:
\[
H^0(\mathfrak a,V)=V^{\mathfrak a},
\]
\[
H^1(\mathfrak a,V)
=\operatorname{Der}(\mathfrak a,V)/
\operatorname{Inn}(\mathfrak a,V),
\tag{2.4}
\]
and \(H^2(\mathfrak a,V)\) is in bijection with equivalence classes of the abelian extensions (1.1) inducing the specified action. The zero class corresponds to split extensions.

Here a derivation into a module means
\[
f([x,y])=xf(y)-yf(x);
\]
an inner one has \(f(x)=xv\) for a fixed \(v\in V\). Equivalence of extensions fixes both the identified kernel and the quotient.

**Proof.** Equation (2.2) identifies the zero-cocycles with invariant vectors. Equation (2.3) identifies one-cocycles with derivations and one-coboundaries with the stated inner derivations, proving (2.4). The minus sign in the derivation formula is essential.

For degree two, Section 1 associates a cocycle \(c\) to an extension and proves that its class does not depend on the section. Conversely, for a cocycle \(c\), use (1.3) to define \(E_c\) on \(\mathfrak a\oplus V\). Its bracket is alternating. Jacobi for three quotient vectors is \(dc=0\); for two quotient vectors and one kernel vector it is the module identity; with two kernel vectors every term is zero. Multilinearity proves Jacobi on all elements. The inclusion \(V\to E_c\) and projection to \(\mathfrak a\) give the required extension. The map \((x,v)\mapsto s(x)+v\) recovers the original \(E\) from its defect, proving surjectivity of the correspondence.

Any linear isomorphism fixing kernel and quotient has the form
\[
F(x,v)=(x,v+a(x)).
\]
Comparing \(F[(x,0),(y,0)]\) and
\([F(x,0),F(y,0)]\) in \(E_c\) and \(E_{c'}\) gives
\(c-c'=da\). Conversely this equality makes \(F\) a Lie isomorphism by (1.3). Its inverse subtracts \(a(x)\). Therefore exactly the same cohomology class gives an equivalent extension. In particular \(c'=c+db\) is implemented by \(F(x,v)=(x,v-b(x))\).

A Lie section has defect zero, and changing a section by \(b\) changes its defect by \(db\). Hence a Lie section exists exactly when the defect class is zero. In that case \(E\) is the semidirect product with bracket (1.3) and \(c=0\). \(\square\)

As a boundary example, take \(\mathfrak a=k^2\) abelian and \(V=k\) trivial. Every alternating bilinear form is a two-cocycle, since the action and bracket vanish, and there are no nonzero two-coboundaries. The form
\[
c((a,b),(a',b'))=ab'-ba'
\]
gives the three-dimensional Heisenberg algebra. Its central extension of \(k^2\) does not split. Semisimplicity will eliminate this obstruction.

## 3. An explicit contraction from an invariant form

For a finite-dimensional Lie algebra \(\mathfrak a\), let \(B\) be nondegenerate, symmetric and invariant:
\[
B([x,y],z)=B(x,[y,z]).
\tag{3.1}
\]
Choose \(B\)-dual bases \(u_i,v_i\). The previous lesson proved that
\[
\sum_i [z,u_i]\otimes v_i+u_i\otimes[z,v_i]=0,
\qquad C_B=\sum_i u_iv_i\in Z(U(\mathfrak a)).
\tag{3.2}
\]

Let \(D_x\) apply \(\rho(x)\) only to a cochain's value. Let \(\iota_y\) insert \(y\) as its first argument:
\[
(\iota_y\omega)(z_1,\ldots,z_{p-1})
=\omega(y,z_1,\ldots,z_{p-1}),
\]
and set it to zero on degree zero. The full Lie action on a cochain is
\[
(\theta_y\omega)(z_1,\ldots,z_p)
=\rho(y)\omega(z_1,\ldots,z_p)
-\sum_{j=1}^p\omega(z_1,\ldots,[y,z_j],\ldots,z_p).
\tag{3.3}
\]

**Lemma 3.1.** The degree-minus-one operator
\[
T=\sum_i D_{u_i}\iota_{v_i}
\]
satisfies
\[
dT+Td=\rho(C_B),
\tag{3.4}
\]
where the right side applies the module operator to the cochain's value.

**Proof.** First (2.1) gives the insertion identity
\[
d\iota_y+\iota_y d=\theta_y.
\tag{3.5}
\]
To see the terms, in \((d\omega)(y,z_1,\ldots,z_p)\) the coefficient action of \(y\) is \(\rho(y)\omega(z_1,\ldots,z_p)\). The pairs involving \(y,z_j\), after moving the bracket to the \(j\)-th argument, give
\(-\omega(z_1,\ldots,[y,z_j],\ldots,z_p)\). Coefficient actions of the \(z_j\)'s and bracket pairs among them are precisely the negatives of the terms of \(d(\iota_y\omega)\). This proves (3.5), including degree zero.

Second, the bracket terms of \(d\) commute with coefficient multiplication, and the coefficient terms give
\[
([d,D_x]\omega)(z_0,\ldots,z_p)
=\sum_{j=0}^p(-1)^j
\rho([z_j,x])\omega(z_0,\ldots,\widehat{z_j},\ldots,z_p).
\tag{3.6}
\]
Thus
\[
dT+Td=\sum_i D_{u_i}\theta_{v_i}
+\sum_i[d,D_{u_i}]\iota_{v_i}.
\]
On a degree-\(p\) cochain evaluated at \(z_1,\ldots,z_p\), the first sum is
\[
\rho(C_B)\omega
-\sum_{i,j}\rho(u_i)
\omega(z_1,\ldots,[v_i,z_j],\ldots,z_p).
\]
In the second sum, moving the first argument \(v_i\) to position \(j\) cancels its omission sign. That sum becomes
\[
\sum_{i,j}\rho([z_j,u_i])
\omega(z_1,\ldots,v_i,\ldots,z_p).
\]
The tensor identity (3.2) changes it into
\[
-\sum_{i,j}\rho(u_i)
\omega(z_1,\ldots,[z_j,v_i],\ldots,z_p).
\]
This cancels the argument terms in the first sum. Only \(\rho(C_B)\omega\) remains, which is (3.4). \(\square\)

Consequently, if \(\rho(C_B)=c\,1_V\) with \(c\ne0\), every closed positive-degree cochain has the explicit primitive
\[
\omega=d(c^{-1}T\omega).
\tag{3.7}
\]
Here the Casimir acts on coefficients. Replacing it with the full action \(\theta\) on cochains would give a different operator and would not justify (3.7).

## 4. Whitehead's two lemmas over every characteristic-zero field

**Theorem 4.1 (Whitehead).** If \(\mathfrak s\) is finite-dimensional and semisimple over a field of characteristic zero, and \(V\) is finite-dimensional, then
\[
H^1(\mathfrak s,V)=H^2(\mathfrak s,V)=0.
\tag{4.1}
\]

**Proof over an algebraically closed field.** Weyl's theorem writes \(V\) as a finite direct sum of irreducibles. Cochains and differentials decompose by the same coefficient summands, so it suffices to treat one irreducible.

Suppose first that its action is nontrivial. The ideal-complement theorem gives
\(\mathfrak s=\ker\rho\oplus\mathfrak h\), with \(\mathfrak h\ne0\) semisimple and acting faithfully. On \(\mathfrak h\), its represented trace form
\[
B_V(x,y)=\operatorname{tr}_V(\rho(x)\rho(y))
\]
is nondegenerate by the proved faithful trace-form theorem. Use this form on \(\mathfrak h\), the Killing form on \(\ker\rho\), and zero cross terms, to obtain a nondegenerate invariant form \(B\) on \(\mathfrak s\).

The kernel part contributes zero to the module operator \(\rho(C_B)\). The faithful part's Casimir is central, hence scalar on this irreducible module by scalar Schur. Its trace is \(\dim\mathfrak h\), since each trace of a dual-basis product is one. Therefore
\[
\rho(C_B)=\frac{\dim\mathfrak h}{\dim V}\,1_V.
\tag{4.2}
\]
This is nonzero in characteristic zero. Lemma 3.1 and (3.7) give primitives for every closed one- or two-cochain. This deals with nonfaithful modules as well: the degenerate trace form on the whole algebra was never inverted.

The only irreducible with trivial action is the line \(k\). A one-cocycle \(f:\mathfrak s\to k\) vanishes on
\([\mathfrak s,\mathfrak s]=\mathfrak s\), so it is zero.

For a closed alternating \(c:\mathfrak s^2\to k\), use the Killing form to define the unique endomorphism \(A\) by
\[
\kappa(Ax,y)=c(x,y).
\tag{4.3}
\]
The cocycle identity with trivial action gives
\[
\begin{aligned}
\kappa(A[x,y],z)
&=c([x,y],z)\\
&=c(y,[z,x])+c(x,[y,z])\\
&=\kappa([Ax,y]+[x,Ay],z).
\end{aligned}
\]
For the last equality, invariance gives
\(\kappa([Ax,y],z)=c(x,[y,z])\) and
\(\kappa([x,Ay],z)=c(y,[z,x])\).
Nondegeneracy therefore makes \(A\) a derivation. The earlier inner-derivation theorem gives \(A=\operatorname{ad}a\) for some \(a\in\mathfrak s\). Thus
\[
c(x,y)=\kappa(a,[x,y])=(db)(x,y),
\qquad b(x)=-\kappa(a,x),
\tag{4.4}
\]
since the trivial-coefficient differential is \(db(x,y)=-b([x,y])\).
This proves the second lemma for the trivial line and finishes the algebraically closed case.

**Descent to \(k\).** Let \(K\) be an algebraic closure. The Killing matrix of \(\mathfrak s_K\) is the scalar extension of that of \(\mathfrak s\), so remains nondegenerate; the Killing criterion makes \(\mathfrak s_K\) semisimple. Extend any closed cochain over \(k\) to \(K\). The preceding proof supplies a primitive over \(K\).

In chosen \(k\)-bases, the equation \(d\beta=\omega\) is a finite linear system over \(k\): cochain spaces in degrees zero, one and two are finite-dimensional. Row reduction over \(k\) either produces an inconsistent row \(0=1\), which would remain inconsistent over \(K\), or a solution over \(k\) by setting free variables to zero. The \(K\)-solution excludes the first case. Hence the primitive exists over \(k\). This proves both vanishing statements at their full stated generality. The zero algebra and zero module are included. \(\square\)

The conclusion concerns these two degrees, not every degree with trivial coefficients. For example, with trivial coefficients on \(\mathfrak{sl}_2\), \(C^3\) is one-dimensional and \(C^4=0\). On the basis \(e,h,f\), every two-cochain has
\[
(dc)(e,h,f)
=-c(-2e,f)+c(h,h)-c(-2f,e)
=2c(e,f)+2c(f,e)=0.
\]
Thus \(d:C^2\to C^3\) is zero and
\[
H^3(\mathfrak{sl}_2,k)\simeq k.
\tag{4.5}
\]
This is compatible with (3.7): the trivial module has zero Casimir coefficient operator.

## 5. Split the radical one abelian layer at a time

A **Levi subalgebra** is a semisimple subalgebra complementary to the radical as a vector space. Complementarity does not require it to be an ideal.

**Theorem 5.1 (Levi).** Every finite-dimensional Lie algebra \(\mathfrak g\) over a field of characteristic zero has a Levi subalgebra \(\mathfrak s\):
\[
\mathfrak g=\mathfrak r\oplus\mathfrak s,\qquad
\mathfrak r=\operatorname{rad}\mathfrak g.
\tag{5.1}
\]
Its bracket identifies it with \(\mathfrak r\rtimes\mathfrak s\).

**Proof.** We induct on \(\dim\mathfrak r\), for all finite-dimensional algebras at once. When the radical is zero, take \(\mathfrak s=\mathfrak g\).

If \(\mathfrak r\) is abelian, \(\mathfrak g/\mathfrak r\) is semisimple by the radical theorem. Its action on the abelian kernel is defined by lifts as in Section 1. The extension class lies in
\(H^2(\mathfrak g/\mathfrak r,\mathfrak r)=0\), by Theorem 4.1. Proposition 2.2 gives a Lie section. Its image is isomorphic to the semisimple quotient and is the desired complement.

Otherwise take \(A\) to be the last nonzero term of the derived series of the solvable algebra \(\mathfrak r\). It is nonzero, abelian and proper in \(\mathfrak r\). It is an ideal of \(\mathfrak g\): if a derived term is stable under \(\operatorname{ad}\mathfrak g\), its next term is stable by
\[
[z,[x,y]]=[[z,x],y]+[x,[z,y]],
\]
and the induction starts with the ideal \(\mathfrak r\).

We have
\[
\operatorname{rad}(\mathfrak g/A)=\mathfrak r/A.
\tag{5.2}
\]
The right side is a solvable ideal, giving one inclusion. The preimage of any solvable ideal of \(\mathfrak g/A\) is solvable, because its kernel \(A\) and its quotient are solvable. That preimage lies in \(\mathfrak r\), proving the reverse inclusion.

The radical in (5.2) has smaller dimension. The induction hypothesis gives a Levi subalgebra \(\overline{\mathfrak s}\) of \(\mathfrak g/A\). Let \(E\) be its inverse image in \(\mathfrak g\). This is a subalgebra containing \(A\), with
\[
E/A\simeq\overline{\mathfrak s},\qquad
E\cap\mathfrak r=A.
\tag{5.3}
\]
Its radical is exactly \(A\). Indeed \(A\) is a solvable ideal of \(E\), while any solvable ideal of \(E\) has zero image in the semisimple quotient \(E/A\), and so is contained in \(A\).

Since \(\dim A<\dim\mathfrak r\), the induction hypothesis applies again, now to \(E\). It supplies a semisimple subalgebra \(\mathfrak s\) with \(E=A\oplus\mathfrak s\). By (5.3), \(\mathfrak s\cap\mathfrak r=0\), and its image in \(\mathfrak g/\mathfrak r\) is the entire quotient: \(\overline{\mathfrak s}\) already maps isomorphically to that quotient. Thus \(\mathfrak g=\mathfrak r\oplus\mathfrak s\).

Finally the map \((r,x)\mapsto r+x\) gives the bracket
\[
[(r,x),(r',x')]
=\bigl([r,r']+[x,r']-[x',r],\,[x,x']\bigr).
\tag{5.4}
\]
Here \([x,-]\) acts by derivations on the ideal \(\mathfrak r\), by Jacobi. This is precisely the semidirect product. \(\square\)

Both induction steps decrease the radical dimension. The inverse-image algebra \(E\) need not be an ideal of \(\mathfrak g\); only its subalgebra property is used.

## 6. Matrix and spacetime examples

For \(n\ge1\), trace gives
\[
\mathfrak{gl}_n(k)=kI\oplus\mathfrak{sl}_n(k),\qquad
X=\frac{\operatorname{tr}X}{n}I+
\left(X-\frac{\operatorname{tr}X}{n}I\right).
\tag{6.1}
\]
The scalar summand is central. The earlier Killing-form calculation makes \(\mathfrak{sl}_n\) semisimple for \(n\ge2\), so the radical is \(kI\) and the displayed special linear algebra is a Levi subalgebra. For \(n=1\), it is zero and the whole algebra is its radical.

Write the affine algebra as
\[
\mathfrak{aff}(n)=k^n\rtimes\mathfrak{gl}_n(k),
\]
with bracket
\[
[(v,X),(w,Y)]=(Xw-Yv,[X,Y]).
\tag{6.2}
\]
The ideal
\[
R=k^n\rtimes kI
\]
is solvable: its derived algebra is \(k^n\), because \(I\) acts as the identity, and the next derived algebra is zero. The quotient is \(\mathfrak{sl}_n\). Any solvable ideal maps to zero in this quotient, and therefore lies in \(R\). Hence \(R\) is exactly the radical, and \(\{(0,X):\operatorname{tr}X=0\}\) is a Levi subalgebra. For \(n=1\) this complement is zero; the two-dimensional affine algebra is solvable.

The physical **Poincaré algebra** is
\[
\mathfrak p=\mathbb R^4\rtimes\mathfrak{so}(1,3),\qquad
\mathfrak{so}(1,3)=\{X:X^{\mathsf t}\eta+\eta X=0\},
\quad \eta=\operatorname{diag}(-1,1,1,1),
\tag{6.3}
\]
with the same bracket formula as (6.2). We verify the semisimplicity needed for this example, without using the later classification.

On \(W=\mathbb C^2\), let
\(\epsilon(u,u')=u^{\mathsf t}Ju'\) with
\(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). On \(W\otimes W\) the form
\[
b(u\otimes v,u'\otimes v')=\epsilon(u,u')\epsilon(v,v')
\]
is symmetric and nondegenerate: its matrix is \(J\otimes J\), which is symmetric and invertible. Each traceless two-by-two matrix satisfies
\(A^{\mathsf t}J+JA=0\), by multiplying its four entries. Therefore
\[
(A,B)\longmapsto A\otimes I+I\otimes B
\tag{6.4}
\]
is a Lie map from \(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\) to
\(\mathfrak{so}(b)\); the two tensor-factor actions commute. If its value is zero, the partial traces give \(2A=2B=0\), since both traces are zero. Thus it is injective. Both algebras have dimension six: for \(\mathfrak{so}(b)\), \(bX\) is an arbitrary skew-symmetric four-by-four matrix. Hence (6.4) is an isomorphism and this orthogonal algebra is semisimple.

Every nondegenerate symmetric form over \(\mathbb C\) is congruent to the identity form. Indeed polarization supplies a vector of nonzero norm; its orthogonal complement is nondegenerate; induction diagonalizes the form, and square roots rescale its nonzero diagonal entries to one. This applies to \(b\) and to the complexification of \(\eta\). Consequently the complexification of \(\mathfrak{so}(1,3)\) is isomorphic to \(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\). Its complex Killing form is nondegenerate, so the original real Killing matrix is nondegenerate as well. The Killing criterion proves real semisimplicity.

It follows that the radical of (6.3) is the abelian translation ideal \(\mathbb R^4\), and the Lorentz algebra is a Levi subalgebra. The same quotient argument used for the affine algebra proves that there is no larger solvable ideal. Rotations with spatial translations instead give the Euclidean motion algebra; that is a different spacetime example.

Levi subalgebras need not be unique even in a small algebra. Let
\(E=V(1)\rtimes\mathfrak{sl}_2(k)\), where \(V(1)=k^2\) is the standard module. Its radical is \(V(1)\). For \(a\in V(1)\),
\[
\operatorname{ad}(a,0)(v,x)=(-xa,0),
\qquad \operatorname{ad}(a,0)^2=0.
\]
The automorphism \(1+\operatorname{ad}(a,0)\) takes the standard complement to
\[
\mathfrak s_a=\{(-xa,x):x\in\mathfrak{sl}_2\}.
\tag{6.5}
\]
One can verify its bracket directly from the representation identity. Projection to \(\mathfrak{sl}_2\) is an isomorphism, so it is a Levi subalgebra. Taking \(a=(1,0)\) makes it different from the standard complement, since \(ha=a\ne0\). These particular complements are conjugate by the displayed automorphism.

## 7. Levi conjugacy and faithful finite-dimensional representations

Let \(k\) be any field of characteristic zero. All Lie algebras and modules below are finite-dimensional over \(k\). Write brackets and exponentials intrinsically over this field; no analytic exponential or group integration is used.

The proved course inputs are Lie triangularization and solvable extensions (RT-LIE-02, Theorem 3.1 and Proposition 1.1), Weyl complete reducibility over \(k\) (RT-LIE-04, Theorem 4.1), and Whitehead's first lemma over \(k\) (RT-LIE-06, Theorem 4.1). Levi existence, already proved in RT-LIE-06, Theorem 5.1, ensures that the complements under discussion exist. The new lemmas below supply every additional step, including the combination of several exponentials into one.

### 7.1. A nilpotent ideal that survives the quotient induction

**Lemma 7.1.** If \(\mathfrak{r}\) is a solvable ideal of \(\mathfrak{g}\), then
\[
N=[\mathfrak g,\mathfrak r]
\]
is a nilpotent ideal. Moreover, the associative subalgebra of \(\operatorname{End}_k(\mathfrak{g})\) spanned by all positive-length products of operators \(\operatorname{ad}(a)\), \(a \in N\), is nilpotent.

**Proof.** Jacobi makes \(N\) an ideal. Extend scalars to an algebraic closure \(K\). Lie's theorem, applied to the action of the solvable algebra \(\mathfrak{r}_K\) on \(\mathfrak{g}_K\), gives a basis in which all \(\operatorname{ad}(y)\), \(y \in \mathfrak{r}_K\), are upper triangular. Let their diagonal entries be the linear functionals \(\lambda_1(y),\ldots,\lambda_d(y)\), where \(d=\dim(\mathfrak{g})\); the zero algebra requires no argument.

Fix \(x \in \mathfrak{g}_K\) and \(y \in \mathfrak{r}_K\). In the formal power-series ring \(K[[t]]\), the derivation identity gives
\[
e^{t\operatorname{ad}x}\operatorname{ad}y\,
e^{-t\operatorname{ad}x}
=\operatorname{ad}\bigl(e^{t\operatorname{ad}x}y\bigr).
\tag{7.1}
\]
This identity follows either by differentiating both sides and matching the constant term, or by expanding the conjugation series: its coefficient of \(t^m\) is \(\operatorname{ad}((\operatorname{ad} x)^m y)/m!\). Since \(\mathfrak{r}_K\) is an ideal, every coefficient of the argument on the right lies in \(\mathfrak{r}_K\). Hence that matrix is upper triangular, with diagonal entries
\[
\mu_j(t)=\lambda_j\bigl(e^{t\operatorname{ad}x}y\bigr).
\]
Formal conjugation preserves its characteristic polynomial. Thus
\[
\prod_{j=1}^d(z-\mu_j(t))
=\prod_{j=1}^d(z-\lambda_j(y)).
\tag{7.2}
\]
For any fixed \(j\), substitute \(z=\mu_j(t)\). The integral domain \(K[[t]]\) implies that one factor \(\mu_j(t)-\lambda_l(y)\) is zero. Evaluation at zero identifies that constant as \(\lambda_j(y)\), even when some eigenvalues repeat. Consequently \(\mu_j(t)\) is constant, and its linear coefficient gives
\[
\lambda_j([x,y])=0.
\tag{7.3}
\]
Every \(\operatorname{ad}(a)\), \(a \in N_K\), is therefore strictly upper triangular in the same basis. Any product of \(d\) such matrices is zero. The same is true over \(k\), since scalar extension is injective on matrices.

The linear span \(A\) of all positive-length products is closed under multiplication, and \(A^d=0\): a product of \(d\) of its spanning terms has at least \(d\) factors \(\operatorname{ad}(a)\). Repeated brackets in the lower central series of \(N\) are products of these adjoint operators applied to elements of \(N\), so \(N^{d+1}=0\). This proves both assertions. ∎

For completeness, the **nilradical** is indeed a largest nilpotent ideal in characteristic zero. If \(I\) and \(J\) are nilpotent ideals, their sum is solvable: its quotient by \(I\) is a quotient of \(J\), and use solvable extensions. Triangularize its adjoint action over \(K\). For \(a \in I\), the map \(\operatorname{ad}(a)\) sends \(\mathfrak{g}\) into \(I\) and is nilpotent on \(I\), so is nilpotent on \(\mathfrak{g}\); the same holds for elements of \(J\). All their triangular diagonal entries are zero. Thus every adjoint operator from \(I+J\) is strictly upper triangular, and \(I+J\) is nilpotent. This conclusion descends to \(k\) by the lower central series. The sum of all nilpotent ideals is a finite sum of them, because \(\mathfrak{g}\) is finite-dimensional. It is therefore nilpotent and contains every such ideal. In particular
\[
[\mathfrak g,\operatorname{rad}\mathfrak g]
\subseteq\operatorname{nilrad}\mathfrak g.
\tag{7.4}
\]

**Why use this particular ideal?** For an abelian ideal \(B\) contained in the radical, the image of \(N\) in \(\mathfrak{g}/B\) is exactly
\[
[\mathfrak g/B,\mathfrak r/B].
\tag{7.5}
\]
Thus an exponent produced by the stronger induction in the quotient has a lift in \(N\). A lift of an arbitrary element of the quotient's nilradical need not lie in the original nilradical; the proof never assumes that false lifting assertion.

### 7.2. A finite logarithm combines the exponentials

**Lemma 7.2.** Let \(A\) be a nilpotent associative algebra over a characteristic-zero field, \(A^d=0\), and let \(L\) be a Lie subalgebra of \(A\) for the commutator bracket. For \(X,Y \in L\),
\[
\log(e^Xe^Y)\in L,
\tag{7.6}
\]
where all exponentials and logarithms are finite polynomials in the unital algebra \(k1+A\). Consequently a product of two exponentials of elements of \(L\) is one such exponential.

**Proof.** The polynomials
\[
e^a=\sum_{j=0}^{d-1}\frac{a^j}{j!},\qquad
\log(1+a)=\sum_{j=1}^{d-1}\frac{(-1)^{j+1}}j a^j
\tag{7.7}
\]
are inverse operations; the scalar formal-series identities can be substituted because all powers of degree at least \(d\) vanish.

Put \(F(t)=\exp(tX)\exp(tY)\) and \(Z(t)=\log F(t)\) in \(A[t]\). We have \(Z(0)=0\), \(F=\exp Z\), and
\[
C(t)=F'(t)F(t)^{-1}
=X+\sum_{m\geq0}\frac{t^m}{m!}(\operatorname{ad}X)^mY
\in L[t].
\tag{7.8}
\]
Every series here is finite. Direct differentiation of the finite exponential gives
\[
F'F^{-1}
=\sum_{m\geq0}\frac{(\operatorname{ad}Z)^m}{(m+1)!}\,Z'
=\Phi(\operatorname{ad}Z)Z',\qquad
\Phi(u)=\sum_{m\geq0}\frac{u^m}{(m+1)!}.
\tag{7.9}
\]
To check this without any analytic formula, expand
\[
\int_0^1 e^{sZ}Z'e^{(1-s)Z}\,ds.
\]
The integral means rational polynomial integration. The coefficient of \(Z^p Z' Z^q\) is
\(\frac{1}{p!\,q!}\int_0^1s^p(1-s)^q\,ds=\frac{1}{(p+q+1)!}\), obtained by polynomial integration or its elementary integration-by-parts recurrence. These are precisely the coefficients of the derivative of \(\exp Z\). Multiply by \(\exp(-Z)\) and expand conjugation to obtain (7.9).

On \(A[t]\), sufficiently high powers of \(\operatorname{ad} Z\) vanish: each term in \((\operatorname{ad} Z)^m(a)\) is a product of \(m+1\) elements of \(A[t]\). Since \(\Phi\) has constant term one, its inverse on this space is a finite polynomial, say \(1+\sum_{m\geq 1} b_m u^m\). Hence
\[
Z'=C+\sum_{m\geq1}b_m(\operatorname{ad}Z)^mC.
\tag{7.10}
\]
Write \(Z(t)=\sum_{n\geq 1} t^n z_n\). Comparing coefficients of \(t^{n-1}\) proves by induction that \(z_n \in L\). Indeed the term on the left is \(n z_n\); on the right the term from \(C\) belongs to \(L\), and every other term is a nested commutator of coefficients of \(C\) with \(z_j\) for \(j\leq n-1\), since \(Z(0)=0\). Division by \(n\) is allowed. Thus \(Z(1) \in L\). Equation (7.7) gives \(\exp Z(1)=\exp X \exp Y\). ∎

Applied to the associative algebra of Lemma 7.1 and \(L=\operatorname{ad}(N)\), this says
\[
e^{\operatorname{ad}b}e^{\operatorname{ad}c}
=e^{\operatorname{ad}a}\quad\text{for some }a\in N.
\tag{7.11}
\]
No convergence, Baker–Campbell–Hausdorff theorem, or faithful representation theorem has been imported. The adjoint map need not be injective: membership in its image is enough to choose \(a\).

### 7.3. The conjugacy induction and its cocycle sign

**Theorem 7.1 (Levi conjugacy).** If \(\mathfrak{s}_1,\mathfrak{s}_2\) are Levi subalgebras of \(\mathfrak{g}\), then there is
\[
a\in[\mathfrak g,\operatorname{rad}\mathfrak g]
\subseteq\operatorname{nilrad}\mathfrak g
\]
such that
\[
e^{\operatorname{ad}a}(\mathfrak s_1)=\mathfrak s_2.
\tag{7.12}
\]

**Proof.** Induct on \(\dim(\mathfrak{g})\), proving this stronger version simultaneously for all algebras over \(k\). If its radical \(\mathfrak{r}\) is zero, both complements are \(\mathfrak{g}\); take \(a=0\).

Otherwise let \(B\) be the last nonzero derived term of \(\mathfrak{r}\). It is a nonzero abelian ideal of \(\mathfrak{g}\); the Jacobi identity proves stability of every derived term, as in Section 5. When \(\mathfrak{r}\) is abelian, take \(B=\mathfrak{r}\). The quotient has radical \(\mathfrak{r}/B\): one inclusion is immediate, and the preimage of any solvable quotient ideal is a solvable extension by \(B\), giving the reverse inclusion. The images of the two Levi subalgebras are Levi subalgebras of \(\mathfrak{g}/B\).

The quotient has smaller dimension. Induction gives a conjugating exponent
\[
\bar b\in[\mathfrak g/B,\mathfrak r/B].
\]
Lift it to \(b \in N=[\mathfrak{g},\mathfrak{r}]\) by (7.5), and put
\(\mathfrak{t}=\exp(\operatorname{ad} b)(\mathfrak{s}_1)\). This is a Levi subalgebra: a finite inner exponential preserves the radical, and its inverse is \(\exp(-\operatorname{ad} b)\). Its image in \(\mathfrak{g}/B\) is the image of \(\mathfrak{s}_2\).

Their common inverse image is
\[
P=B\oplus\mathfrak t=B\oplus\mathfrak s_2.
\tag{7.13}
\]
Thus \(\mathfrak{s}_2\) is the graph of a unique linear map \(f:\mathfrak{t} \longrightarrow B\). Since \(B\) is abelian, closure of this graph under brackets is precisely
\[
f([x,y])=[x,f(y)]-[y,f(x)].
\tag{7.14}
\]
This is the one-cocycle equation for the \(\mathfrak{t}\)-module \(B\), with the exact differential convention of (2.3). Whitehead's first lemma supplies \(v \in B\) with
\[
f(x)=[x,v].
\tag{7.15}
\]
We can choose \(v \in [\mathfrak{t},B]\). To see this over the original field, decompose \(B\) into simple \(\mathfrak{t}\)-modules using Weyl's theorem. On a trivial simple summand \([\mathfrak{t},-]=0\); on a nontrivial simple summand its image under the action spans a nonzero submodule, hence the whole summand. Therefore
\[
B=B^{\mathfrak t}\oplus[\mathfrak t,B].
\tag{7.16}
\]
Subtracting the invariant component of \(v\) does not change (7.15). This choice lies in \(N\), since \(B \subseteq \mathfrak{r}\).

On \(P\), the square of \(\operatorname{ad} v\) is zero, because \([v,P] \subseteq B\) and \(B\) is abelian. Consequently
\[
e^{-\operatorname{ad}v}x
=x+[-v,x]=x+[x,v]=x+f(x).
\tag{7.17}
\]
The sign in the exponent is therefore **minus** the primitive in (7.15). Equation (7.17) sends \(\mathfrak{t}\) to \(\mathfrak{s}_2\). We have obtained the conjugator
\[
e^{-\operatorname{ad}v}e^{\operatorname{ad}b},\qquad -v,b\in N.
\tag{7.18}
\]
Lemma 7.2 combines these two factors into \(\exp(\operatorname{ad} a)\) for one \(a \in N\). This completes the induction and proves (7.12). ∎

All exponentials in this proof are actual \(k\)-linear automorphisms of \(\mathfrak{g}\). For a nilpotent derivation \(D\), the repeated derivation rule gives
\[
D^m[x,y]=\sum_{j=0}^m\binom mj[D^jx,D^{m-j}y].
\]
Substitution into its finite exponential proves preservation of brackets, and \(\exp(-D)\) is its inverse. The only use of the algebraic closure in the argument was to prove that certain products of matrices over \(k\) are zero; the conjugating elements, cocycle primitive, coefficient recursions and final exponent are all constructed over \(k\).

For Sections 7.4–7.7, let \(K\) be an algebraically closed field of characteristic zero. Section 7.8 will give the representation over an arbitrary characteristic-zero field \(k\). The inputs are solvable extensions, Lie triangularization and Engel's theorem (Lesson 02), Weyl complete reducibility (Lesson 04), and Levi existence (Theorem 5.1 above). Section 7.9 supplies the finite-dimensional ordered-monomial PBW theorem needed in the construction; it agrees with the independent proof in Lesson 13, §2.

Pavel Etingof, [*Lie groups and Lie algebras*, §50](https://arxiv.org/html/2201.09397v5#S50), treats Ado’s theorem by enlargement and polynomial functions. Here we give an explicit Lie-algebra enlargement and a finite weighted enveloping-algebra module.

### 7.4. Solvable algebras and their derivations

Work over \(K\) until Section 7.8. The **nilradical** of a Lie algebra is its largest nilpotent ideal. We first justify the facts needed about it.

**Lemma 7.3.** If \(\mathfrak{r}\) is a solvable ideal of a Lie algebra \(\mathfrak{g}\), then \([\mathfrak{g},\mathfrak{r}]\) is a nilpotent ideal. The adjoint operators of this ideal on \(\mathfrak{g}\) can all be made strictly upper triangular in the same basis.

**Proof.** Lie's theorem triangularizes the action of \(\mathfrak{r}\) on \(\mathfrak{g}\). Let \(\lambda_j:\mathfrak{r} \longrightarrow K\) be the diagonal entries. For \(x \in \mathfrak{g}\), \(y \in \mathfrak{r}\), set
\(\mu_j(t)=\lambda_j(\exp(t \operatorname{ad} x)y)\) in \(K[[t]]\). The identity
\[
e^{t\operatorname{ad}x}\operatorname{ad}y\,
e^{-t\operatorname{ad}x}
=\operatorname{ad}\bigl(e^{t\operatorname{ad}x}y\bigr)
\tag{7.19}
\]
holds by the derivation identity and coefficient comparison. The right side is triangular because every coefficient of its argument lies in \(\mathfrak{r}\). Conjugation preserves characteristic polynomials, so
\[
\prod_j(z-\mu_j(t))=\prod_j(z-\lambda_j(y)).
\]
Substitute \(z=\mu_j(t)\). Since \(K[[t]]\) is an integral domain, one factor on the right is zero; evaluation at \(t=0\) identifies that constant as \(\lambda_j(y)\). Hence \(\mu_j(t)\) is constant and \(\lambda_j([x,y])=0\). Thus all operators from \([\mathfrak{g},\mathfrak{r}]\) are strictly triangular in the same basis. Any product of \(\dim(\mathfrak{g})\) of them is zero, so the lower central series of \([\mathfrak{g},\mathfrak{r}]\) terminates. Jacobi makes this subspace an ideal. ∎

The sum of two nilpotent ideals \(I,J\) is nilpotent. It is solvable by solvable extensions, so triangularize its adjoint action. Each \(\operatorname{ad}(i)\), \(i \in I\), is nilpotent on the whole ambient algebra: its first application enters \(I\), where the lower central series makes repeated application vanish. The same holds for \(J\). Their triangular diagonal entries are zero, so the whole sum acts strictly triangularly and is nilpotent. Finite dimension makes the sum of all nilpotent ideals a finite sum, establishing the nilradical.

**Lemma 7.4.** If \(\mathfrak{r}\) is solvable with nilradical \(\mathfrak{n}\) and \(D\) is any derivation of \(\mathfrak{r}\), then
\[
D(\mathfrak r)\subseteq\mathfrak n.
\tag{7.20}
\]
In particular every derivation preserves \(\mathfrak{n}\), and acts trivially on \(\mathfrak{r}/\mathfrak{n}\).

**Proof.** Form the abstract semidirect product \(K d \ltimes \mathfrak{r}\) with \([d,x]=D x\). It is solvable because its ideal \(\mathfrak{r}\) and its one-dimensional quotient are solvable. Lemma 7.3 shows that its derived algebra is a nilpotent ideal. Its intersection with \(\mathfrak{r}\) is therefore a nilpotent ideal of \(\mathfrak{r}\), and contains \([d,\mathfrak{r}]=D(\mathfrak{r})\). By maximality it is contained in \(\mathfrak{n}\). ∎

Taking \(D=\operatorname{ad}(x)\) for \(x \in \mathfrak{r}\) also gives \([\mathfrak{r},\mathfrak{r}] \subseteq \mathfrak{n}\), so \(\mathfrak{r}/\mathfrak{n}\) is abelian.

### 7.5. Jordan parts of a derivation are derivations

**Lemma 7.5.** On any finite-dimensional Lie algebra over \(K\), the semisimple and nilpotent Jordan parts \(D_s,D_n\) of a derivation \(D\) are derivations. They preserve every \(D\)-invariant subspace, commute with every operator commuting with \(D\), and both vanish on \(\ker D\).

**Proof.** Write \(\mathfrak{g}_\lambda\) for the generalized \(\lambda\)-eigenspace of \(D\). The derivation rule gives
\[
(D-(\lambda+\mu))^m[x,y]
=\sum_{j=0}^m\binom mj
[(D-\lambda)^jx,(D-\mu)^{m-j}y]
\tag{7.21}
\]
for \(x \in \mathfrak{g}_\lambda\), \(y \in \mathfrak{g}_\mu\). For large \(m\) every term is zero. Thus
\([\mathfrak{g}_\lambda,\mathfrak{g}_\mu] \subseteq \mathfrak{g}_{\lambda+\mu}\), interpreting a nonexistent generalized eigenspace as zero. Define \(D_s\) to be multiplication by \(\lambda\) on \(\mathfrak{g}_\lambda\). Equation (7.21) proves
\[
D_s[x,y]=[D_sx,y]+[x,D_sy].
\]
Then \(D_n=D-D_s\) is also a derivation and is nilpotent on the whole algebra.

The projections to the generalized eigenspaces are polynomials in \(D\): apply the elementary Chinese-remainder identity to the coprime powers \((T-\lambda)^m\) annihilating these spaces. Consequently \(D_s\) is a polynomial in \(D\), and preserves \(D\)-invariant subspaces and commutes with commuting operators. On \(\ker D\) only the zero generalized eigenspace occurs, so \(D_s=0\). These observations also show that Jordan parts restrict to invariant subspaces and pass to their quotients. ∎

This is a statement about arbitrary derivations. It does not infer it from preservation of Jordan decomposition in representations of semisimple Lie algebras, which has a different hypothesis.

### 7.6. An explicit finite sequence of enlargements

**Proposition 7.1.** Every finite-dimensional Lie algebra over \(K\) embeds in a finite-dimensional algebra
\[
\mathfrak h=(\mathfrak s\oplus\mathfrak t)\ltimes\mathfrak n,
\tag{7.22}
\]
where \(\mathfrak{s}\) is semisimple, \(\mathfrak{t}\) is abelian, \(\mathfrak{n}\) is nilpotent, \([\mathfrak{s},\mathfrak{t}]=0\), and the operators \(\operatorname{ad}(\mathfrak{t})\) on \(\mathfrak{n}\) are commuting semisimple operators. Faithfulness of their action is not required.

**Proof.** Levi existence starts the process with \(\mathfrak{g}=\mathfrak{s} \ltimes \mathfrak{r}\), \(\mathfrak{r}\) solvable, and \(\mathfrak{t}=0\). At an intermediate stage we have
\[
\mathfrak h=\mathfrak l\ltimes\mathfrak r,
\qquad\mathfrak l=\mathfrak s\oplus\mathfrak t,
\tag{7.23}
\]
where \(\mathfrak{r}\) is a solvable ideal and the operators from \(\mathfrak{t}\) on \(\mathfrak{r}\) are commuting and semisimple. Here \(\mathfrak{r}\) is a chosen ideal in this decomposition; it is not asserted to be the full radical of \(\mathfrak{h}\).

Such an \(\mathfrak{l}\)-module \(\mathfrak{r}\) is completely reducible. Indeed simultaneous eigenspaces for the commuting semisimple \(\mathfrak{t}\)-operators decompose \(\mathfrak{r}\); \(\mathfrak{s}\) preserves them because \([\mathfrak{s},\mathfrak{t}]=0\). Apply Weyl's theorem separately on each eigenspace. In particular every \(\mathfrak{l}\)-invariant subspace has an \(\mathfrak{l}\)-invariant complement.

Let \(\mathfrak{n}\) be the nilradical of \(\mathfrak{r}\) and let \(q=\dim(\mathfrak{r}/\mathfrak{n})\). Lemma 7.4 makes \(\mathfrak{n}\) invariant under \(\mathfrak{l}\) and makes the action on \(\mathfrak{r}/\mathfrak{n}\) trivial. If \(q=0\), then \(\mathfrak{r}=\mathfrak{n}\) and we have reached (7.22). If \(q>0\), complete reducibility provides an invariant complement to \(\mathfrak{n}\) in \(\mathfrak{r}\); its action must be zero since it maps isomorphically to the trivial quotient. Choose
\[
d\in\mathfrak r\setminus\mathfrak n,
\qquad[\mathfrak l,d]=0.
\tag{7.24}
\]
Choose a linear functional \(\chi:\mathfrak{r}/\mathfrak{n} \longrightarrow K\) with \(\chi(d)=1\), and compose with the quotient map. It is a Lie character because \([\mathfrak{r},\mathfrak{r}] \subseteq \mathfrak{n}\), and it kills the action of \(\mathfrak{l}\) by Lemma 7.4.

On \(\mathfrak{h}\) let \(D=\operatorname{ad} d\) and let \(S=D_s\) be its semisimple part. Lemma 7.5 makes \(S\) a derivation, preserving \(\mathfrak{r}\) and \(\mathfrak{n}\). It vanishes on \(\mathfrak{l}\) and on \(d\), because \(D\) does. Since \([\mathfrak{l},d]=0\), \(D\) commutes with every \(\operatorname{ad}(\mathfrak{l})\); therefore so does \(S\). On \(\mathfrak{r}/\mathfrak{n}\), \(D=0\), so also \(S=0\). In particular \(S(\mathfrak{r}) \subseteq \mathfrak{n}\).

Adjoin one new basis vector \(\delta\), with
\[
\widetilde{\mathfrak h}=K\delta\ltimes_S\mathfrak h,
\qquad [\delta,x]=Sx.
\tag{7.25}
\]
The old \(\mathfrak{h}\) embeds as an ideal. Set
\[
u=d-\delta,\quad
\mathfrak l'=\mathfrak s\oplus(\mathfrak t\oplus K\delta),
\quad
\mathfrak r'=\ker\chi\oplus Ku.
\tag{7.26}
\]
Then \(\widetilde{\mathfrak h}=\mathfrak l'\ltimes\mathfrak r'\). Here are all bracket and splitting checks.

* \(\ker \chi\) is a subalgebra, since it contains \([\mathfrak{r},\mathfrak{r}]\). It is stable under \(\mathfrak{l}\) and \(S\) because both send \(\mathfrak{r}\) into \(\mathfrak{n} \subseteq \ker \chi\).
* For \(y \in \ker \chi\), \([u,y]=(D-S)y=D_n y\) belongs to \(\mathfrak{n}\). Thus \(\mathfrak{r}'\) is a subalgebra.
* \([\mathfrak{l},u]=0\) and \([\delta,u]=S d=0\), while \(\mathfrak{l}'\) preserves \(\ker \chi\). Hence \(\mathfrak{r}'\) is an ideal of \(\widetilde{\mathfrak h}\).
* \(\mathfrak{l}'\) is the direct sum of \(\mathfrak{s}\) and an abelian algebra \(\mathfrak{t}'=\mathfrak{t}+K \delta\). The old operators from \(\mathfrak{t}\) remain semisimple on \(\widetilde{\mathfrak h}\) (they kill \(\delta\)), and \(\operatorname{ad} \delta=S\) on the old algebra, zero on \(\delta\), is semisimple. They commute, so their restrictions to \(\mathfrak{r}'\) are commuting semisimple operators.
* The sum \(\mathfrak{l}'+\mathfrak{r}'\) is direct and is all of \(\widetilde{\mathfrak h}\): writing \(\mathfrak{r}=\ker \chi+Kd\) and \(d=u+\delta\) proves spanning. An element of the intersection has an old \(\mathfrak{r}\)-component \(v+\alpha d\), \(v \in \ker \chi\), and an old \(\mathfrak{l}\)-component; the old splitting and \(\chi(d)=1\) force \(\alpha=v=0\), then its \(\delta\)-component is zero.

The algebra \(\mathfrak{r}'\) is solvable: \(\ker \chi\) is solvable and its quotient in \(\mathfrak{r}'\) is one-dimensional. Moreover
\[
\mathfrak n'=\mathfrak n\oplus Ku
\tag{7.27}
\]
is a nilpotent ideal of \(\mathfrak{r}'\). It is an ideal since \([\mathfrak{r}',u] \subseteq \mathfrak{n}\) and \(\mathfrak{n}\) is stable under \(D-S\). To verify nilpotence, note first that \(\mathfrak{n}'\) is solvable. Every \(\operatorname{ad}(z)\), \(z \in \mathfrak{n}\), is nilpotent on \(\mathfrak{n}'\), because \(\mathfrak{n}\) is a nilpotent ideal there. The operator \(\operatorname{ad} u\) is \(D_n\) on \(\mathfrak{n}\) and zero on \(u\), so is nilpotent too. Lie triangularization of the adjoint action of \(\mathfrak{n}'\) now makes all these generators strictly triangular: a triangular nilpotent operator has zero diagonal. Every element of \(\mathfrak{n}'\) acts strictly triangularly, and its lower central series terminates. Equivalently one may apply the proved intrinsic Engel theorem.

Thus \(\mathfrak{n}'\) is contained in the nilradical of \(\mathfrak{r}'\), and
\[
\dim\bigl(\mathfrak r'/\operatorname{nilrad}\mathfrak r'\bigr)
\leq\dim\mathfrak r-\bigl(\dim\mathfrak n+1\bigr)=q-1.
\tag{7.28}
\]
We only need this inequality; no assertion that \(\mathfrak{n}'\) is the entire new nilradical is made. Repeat the procedure. The nonnegative integer \(q\) decreases at each step, so at most \(\dim(\operatorname{rad} \mathfrak{g})\) new vectors are adjoined. The final algebra has (7.22), and all previous algebras, including \(\mathfrak{g}\), embed into it. ∎

### 7.7. The finite weighted PBW module

**Proposition 7.2.** An algebra of the form (7.22) has a faithful finite-dimensional representation.

**Proof.** First construct a representation that is faithful on \(\mathfrak{n}\). If \(\mathfrak{n}=0\), skip this construction and use the representation of \(\mathfrak l=\mathfrak s\oplus\mathfrak t\) given below.

Write its lower central filtration as
\[
\mathfrak n^1=\mathfrak n,\quad
\mathfrak n^{j+1}=[\mathfrak n,\mathfrak n^j],\quad
\mathfrak n^{c+1}=0.
\tag{7.29}
\]
Jacobi and induction give \([\mathfrak{n}^i,\mathfrak{n}^j] \subseteq \mathfrak{n}^{i+j}\). For the induction, expand \([[a,b],y]=[a,[b,y]]-[b,[a,y]]\) when \(a \in \mathfrak{n}\), \(b \in \mathfrak{n}^{i-1}\), \(y \in \mathfrak{n}^j\); both terms have the required total filtration index. Every derivation of \(\mathfrak{n}\) preserves this filtration, directly by induction in (7.29).

Choose a basis \(x_1,\ldots,x_b\) adapted to the filtration: bases of complements of \(\mathfrak{n}^{j+1}\) in \(\mathfrak{n}^j\). Give each such basis vector weight \(j\). Then \(\mathfrak{n}^j\) is the span of vectors of weight at least \(j\). Fix any total order on this basis. PBW says that the ordered monomials
\[
x_1^{a_1}\cdots x_b^{a_b},\qquad a_i\geq0,
\tag{7.30}
\]
including \(1\), are a basis of \(U(\mathfrak{n})\). Give (7.30) weight \(\sum_i a_i w_i\). Let \(P_m\) be the span of the monomials of weight at least \(m\), and \(P_0=U(\mathfrak{n})\).

Ordering a product never lowers its weight: replacing an inverted pair \(xy\) by \(yx+[x,y]\) preserves the weight in the swapped term, and every basis term of \([x,y]\) has weight at least \(w(x)+w(y)\). PBW reduction therefore proves
\[
P_iP_j\subseteq P_{i+j}.
\tag{7.31}
\]
In particular \(J=P_{c+1}\) is a two-sided ideal, and
\[
Q=U(\mathfrak n)/J
\tag{7.32}
\]
is finite-dimensional: it has the finitely many ordered monomials of weight at most \(c\) as a basis. PBW also gives \(J \cap \mathfrak{n}=0\), because all the basis vectors of \(\mathfrak{n}\) have weight at most \(c\) and ordered monomials are linearly independent.

Let \(x \in \mathfrak{n}\) act on \(Q\) by left multiplication \(L_x\). It is a Lie action because \([L_x,L_y]=L_{[x,y]}\). It is faithful on \(\mathfrak{n}\): evaluation at the class of \(1\) sends \(x\) to its nonzero class in \(Q\) whenever \(x \ne 0\). Every such operator is nilpotent, since it increases weight by at least one.

For \(a \in \mathfrak{l}\), its derivation \(x \longmapsto [a,x]\) of \(\mathfrak{n}\) extends to a derivation \(D_a\) of \(U(\mathfrak{n})\). Indeed the tensor-algebra derivation preserves the defining relations \(xy-yx-[x,y]\), by the derivation rule on the Lie bracket. It preserves every \(P_m\): it replaces each basis letter of weight \(j\) by a sum of basis letters of weights at least \(j\), and reordering cannot lower weight. Thus \(D_a\) acts on \(Q\), and
\[
[D_a,D_b]=D_{[a,b]},\qquad
[D_a,L_x]=L_{[a,x]}.
\tag{7.33}
\]
The first identity holds on the Lie generators and hence on their products; the second follows by applying the product rule to \(xq\). Equations (7.33) prove that
\[
\rho(a+x)=D_a+L_x
\tag{7.34}
\]
is a representation of \(\mathfrak{l} \ltimes \mathfrak{n}\) on \(Q\).

It remains to detect any part of \(\mathfrak{l}\) that acts trivially on \(\mathfrak{n}\). We supply a faithful module \(W\) of \(\mathfrak{l}\) itself. Its semisimple summand \(\mathfrak{s}\) acts on \(\mathfrak{s}\) by the adjoint action; this is faithful since its centre is an abelian ideal and semisimplicity forces that centre to be zero. Let \(t_1,\ldots,t_r\) be a basis of \(\mathfrak{t}\). On \(K^r\), make \(\sum_i b_i t_i\) act diagonally with entries \(b_1,\ldots,b_r\). Let \(\mathfrak{s}\) act trivially on this space and let \(\mathfrak{t}\) act trivially on the adjoint \(\mathfrak{s}\)-space. This is a faithful representation \(\sigma:\mathfrak{l} \longrightarrow \operatorname{End}(W)\), where \(W=\mathfrak s\oplus K^r\) (the zero-dimensional cases have their evident meaning).

Pull \(\sigma\) back along the quotient homomorphism \(\mathfrak{l} \ltimes \mathfrak{n} \longrightarrow \mathfrak{l}\), and take its direct sum with (7.34). If \(a+x\) acts as zero on both summands, its action on \(1 \in Q\) is
\[
(D_a+L_x)1=x\pmod J,
\]
so \(x=0\); its action on \(W\) then gives \(a=0\). Hence the direct-sum representation is faithful. If \(\mathfrak{n}=0\), \(\sigma\) alone is faithful. The zero algebra can act faithfully on a one-dimensional trivial space. ∎

Combining Propositions 7.1 and 7.2 proves Ado's theorem over every algebraically closed field of characteristic zero: restrict the final faithful representation to the embedded original algebra.

### 7.8. The exact field descent

**Theorem 7.2 (Ado).** Every finite-dimensional Lie algebra over any characteristic-zero field \(k\) has a faithful finite-dimensional representation over \(k\).

**Proof.** Choose an algebraic closure \(K\) and extend \(\mathfrak{g}\) to \(\mathfrak{g}_K\). The preceding construction gives a faithful representation on a finite-dimensional \(K\)-space. In bases of \(\mathfrak{g}\) and of this space it consists of finitely many matrices \(A_1,\ldots,A_d\) with entries in \(K\), obeying the Lie bracket relations whose structure constants lie in \(k\).

Let \(L\) be the subfield of \(K\) generated over \(k\) by those finitely many matrix entries. Each entry is algebraic over \(k\), so \([L:k]\) is finite. The same matrices define a representation of \(\mathfrak{g}\) on \(L^m\); their bracket relations hold over \(L\) because they hold after the injective embedding in \(K\). This representation is faithful: an element of \(\mathfrak{g}\) whose matrix is zero would also act as zero in the faithful representation of \(\mathfrak{g}_K\).

Now regard \(L^m\) as a \(k\)-vector space of dimension \(m[L:k]\). The matrices are \(k\)-linear maps on it, and their commutators retain the same bracket relations. A nonzero matrix still acts nontrivially, as one sees by applying it to a standard coordinate vector. Restriction of scalars thus gives a faithful finite-dimensional \(k\)-representation. ∎

This descent neither asserts that arbitrary algebraic equations have solutions over \(k\) nor tries to descend a representation by row reduction. A finite extension followed by restriction of scalars is the explicit construction that keeps faithfulness.

### 7.9. The precise ordered-monomial theorem used above

Let \(\mathfrak b\) be a finite-dimensional Lie algebra with a totally ordered basis. Define \(U(\mathfrak b)\) as the tensor algebra modulo \(xy-yx-[x,y]\). Replace each inverted adjacent pair by \(yx+[x,y]\), expanding the bracket in that basis. Each resulting word decreases the lexicographic pair \((\text{length},\text{number of inversions})\): the swapped word has one fewer inversion, while a bracket word has smaller length. Thus reduction terminates.

The resulting linear combination of ordered words is independent of the choices. Prove this by induction in that well-founded pair. Two disjoint first replacements commute upon expansion, and every resulting term is smaller, so induction resolves them. The only overlapping ambiguity is \(x>y>z\). Sorting ordinary letters first gives the two expressions
\[
zyx+[y,z]x+y[x,z]+[x,y]z,
\qquad
zyx+z[x,y]+[x,z]y+x[y,z].
\]
Their difference has smaller length. For smaller lengths the induction already makes the normal form of \(uv-vu\) equal to that of \([u,v]\), also in any surrounding words: for an inverted basis pair this is its defining replacement, for the reversed pair use alternation, and extend bilinearly. The normal form of the ambiguity is therefore the normal form of
\[
[[y,z],x]+[y,[x,z]]+[[x,y],z]=0
\]
by Jacobi. This establishes independence, including surrounding words.

Call this normal-form map \(N\). It kills every defining relation in every context, and hence its linear span, the two-sided relation ideal. Every reduction changes a tensor by an element of that ideal, so \(w-N(w)\) lies in the ideal. Ordered words are fixed by \(N\). Consequently the kernel of \(N\) is exactly the ideal, and the images of the ordered words are a basis of \(U(\mathfrak b)\). This is precisely the PBW input needed in (7.30)–(7.32); its proof uses no faithful representation.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Find the radical and a Levi subalgebra of \(\mathfrak{gl}_n(k)\) and \(\mathfrak{aff}(n)\), including \(n=1\).

**Solution.** Characteristic zero permits division by \(n\), so (6.1) gives a central ideal \(kI\) and a semisimple complementary \(\mathfrak{sl}_n\). Every solvable ideal has zero image in the semisimple quotient, making \(kI\) the radical. For \(n=1\) the complementary algebra is zero.

For the affine algebra, the matrices
\(\begin{pmatrix}X&v\\0&0\end{pmatrix}\) have commutator (6.2). The subspace \(R=\{(v,aI)\}\) is an ideal: commutators with arbitrary \((w,X)\) remain translations, since scalar matrices commute. Its brackets are
\([(v,aI),(w,bI)]=(aw-bv,0)\).
These span every translation by choosing \(a=1,b=0\), so \([R,R]=k^n\) and its next derived algebra is zero. The quotient by \(R\) is \(\mathfrak{sl}_n\), forcing the radical to be exactly \(R\). The traceless linear matrices form the Levi subalgebra and have zero intersection with \(R\). When \(n=1\), \(R\) is the whole algebra and the Levi subalgebra is zero.

**Exercise 8.2 (medium).** Prove the interpretation of \(H^1\) as derivations modulo inner derivations.

**Solution.** By (2.3), \(df=0\) means
\(f([x,y])=xf(y)-yf(x)\), precisely a derivation into the specified module. The degree-zero differential sends \(v\) to \(x\mapsto xv\). This map satisfies the derivation rule because
\([x,y]v=x(yv)-y(xv)\), and these maps are exactly the defined inner derivations. Thus \(Z^1=\operatorname{Der}\) and \(B^1=\operatorname{Inn}\), proving the quotient formula. For trivial coefficients the inner subspace is zero and the derivations are precisely maps through \(\mathfrak a/[\mathfrak a,\mathfrak a]\).

**Exercise 8.3 (medium).** Use a Casimir to prove \(H^1(\mathfrak s,V)=0\) for a nontrivial irreducible finite-dimensional module. Make the primitive explicit.

**Solution.** First work over an algebraically closed field. Write \(\mathfrak s=\ker\rho\oplus\mathfrak h\), and use the represented trace form on the faithful ideal \(\mathfrak h\). Let \(u_i,v_i\) be its dual bases. For a one-cocycle \(f\), put
\[
w=\frac{\dim V}{\dim\mathfrak h}\sum_i\rho(u_i)f(v_i).
\]
The invariant inverse-form tensor gives Lemma 3.1; its Casimir coefficient operator is \((\dim\mathfrak h/\dim V)1_V\). Equation (3.4) applied to \(f\), with \(df=0\), therefore gives \(dw=f\), or \(f(x)=xw\), proving that it is inner. Both dimensions are positive integers and the field has characteristic zero, so the division is legitimate.

Over an arbitrary characteristic-zero field, extend scalars to an algebraic closure. The module there need not stay irreducible, so decompose it by Weyl and apply this calculation to its nontrivial summands and the perfectness argument to its trivial summands. The resulting equation \(dw=f\) is a finite linear system over the original field. Row reduction descends its solution as in Theorem 4.1. This establishes the same conclusion without scalar Schur over the original field.

**Exercise 8.4 (hard).** Deduce Levi's theorem from the two-cocycle extension classification and Whitehead's second lemma.

**Solution.** Induct on the dimension of the radical \(R\). If \(R=0\), the algebra itself is a Levi subalgebra. If \(R\) is abelian, its extension of the semisimple quotient has zero class in \(H^2(\mathfrak g/R,R)\), so admits a Lie section and hence a semisimple complement.

Otherwise the last nonzero derived ideal \(A\) of \(R\) is a nonzero proper abelian ideal of \(\mathfrak g\); stability follows from the derivation identity for \(\operatorname{ad}z\) on every derived term. The radical of \(\mathfrak g/A\) is \(R/A\): the preimage of a solvable ideal is a solvable extension by \(A\), and must lie in \(R\). Its smaller radical dimension permits a Levi subalgebra \(\overline S\) in this quotient. Its inverse-image subalgebra \(E\) has \(E\cap R=A\) and semisimple quotient \(E/A\). Thus its radical is \(A\), because any solvable ideal has zero image in that quotient. Since \(\dim A<\dim R\), induction supplies \(E=A\oplus S\) with \(S\) semisimple. The map \(S\to\mathfrak g/R\) is an isomorphism, and \(S\cap R=0\); therefore \(\mathfrak g=R\oplus S\). The ideal property of \(R\) gives the semidirect bracket (5.4). Both induction applications decrease the stated parameter.

## What this lesson does not prove

The radical, Killing-form, ideal-complement, inner-derivation, faithful trace-form, Casimir and Weyl results are the previously proved imports named at the start. The module classification used to name the standard \(\mathfrak{sl}_2\)-module in (6.5) is proved in [Representations of \(\mathfrak{sl}_2\)](RT-LIE-05.md).

Section 7 proves Levi conjugacy by a single nilpotent inner exponential and Ado's theorem over every characteristic-zero field. Those supplementary arguments use the earlier Whitehead, Weyl and Levi-existence results; the earlier proofs do not depend on them. The identification of Chevalley–Eilenberg cohomology with derived \(\operatorname{Ext}\), discussed in [Wagemann, §2.2, Proposition 2.5], requires a separate resolution theorem; the present arguments use the explicitly defined cochain complex and do not prove that comparison. Nor is the Hochschild cohomology of algebraic groups in [Milne, §§15b and 15d] identified with this Lie algebra complex without an additional comparison theorem.

All three low-degree interpretations, both Whitehead lemmas and Levi's existence theorem are proved here. The affine and physical Poincaré examples include the radical and semisimplicity checks that they use.

## References

- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected 2021 text, published 2022, §14d, 14.34(b), p. 290; §§15b, 15d; §25f, especially 25.49, p. 562. The cohomology in Chapter 15 is algebraic-group cohomology. [Author's corrected 2021 edition](https://www.jmilne.org/math/Books/AG.pdf).
- **[Wagemann]** Friedrich Wagemann, *Introduction to Lie algebra cohomology with a view towards BRST cohomology*, notes dated 23 August 2010, §2, pp. 3–5; §§3.1–3.3, pp. 6–7; §5.1, Proposition 5.1, p. 11. The low-degree interpretations are developed in §3. Proposition 5.1 states Whitehead vanishing for finite-dimensional complex semisimple algebras and modules and refers elsewhere for its proof. Our explicit coefficient contraction and descent prove the stated result over every characteristic-zero field. [Author's notes](https://www.math.sciences.univ-nantes.fr/~wagemann/LAlecture.pdf).
- **[Etingof, Lecture 22]** Pavel Etingof, *Lie Groups and Lie Algebras II*, MIT 18.755, Spring 2024, Lecture 22, §48.1, Propositions 48.1–48.3, and §48.2, Theorem 48.9, printed pp. 260–264. The lecture gives the coefficient complex, Whitehead vanishing via the earlier compact-group theorem, the abelian-extension interpretation, and Levi splitting over the real or complex numbers using the last derived ideal. Our proofs retain explicit cochains, the coefficient contraction and induction on radical dimension over any characteristic-zero field. [MIT OpenCourseWare lecture](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec22.pdf) (CC BY-NC-SA 4.0; cited for mathematical comparison, with no lecture text reproduced).
- **[Fiallo]** J. C. Fiallo R., *Lie Algebra Cohomology*, 2013, §§3–5, especially Theorem 5.9 and the extension discussion. Derivations use the minus sign in (2.3). [University-hosted notes](https://www.math.ubc.ca/~reichst/Lie-Algebra-Cohomology.pdf).

# Recovering an algebra from an oriented cone

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 5 October 2026. Original exposition is CC0.*

Fix a sigma-finite von Neumann algebra in standard form \((M,H,J,P)\), and put \(Z=Z(M)\). Let \(\mathfrak g\) be the set of bounded operators \(D\) on \(H\) satisfying

\[
 e^{tD}P=P\qquad(t\in\mathbb R).
\]

We will verify its real Lie algebra structure below.
The cone alone cannot distinguish the left algebra from its commutant. An orientation of a quotient of \(\mathfrak g\) supplies exactly that missing complex structure. We prove both the classification of these orientations and the reconstruction formula. All seven parts of Takesaki II, Exercise IX.1(10) are included, with the bounded-generator scope inherited from GN. The unrestricted derivation identification uses automatic boundedness and full innerness. The other inputs are bounded cone generators, standard-form axioms and central corners, the bicommutant and bounded strong limits, polar decomposition, unitary spanning and spectral calculus and algebra membership.

## A commutator commuting with its first entry is quasinilpotent

Let \(x,y\) be bounded operators on a nonzero Hilbert space, put \(a=[x,y]\), and assume \([x,a]=0\). Define the bounded derivation \(d=[x,\cdot]\) of \(B(H)\). Then \(d(y)=a\) and \(d^2(y)=0\). Repeated Leibniz expansion in a product of \(n\) copies of \(y\) gives

\[
 d^n(y^n)=n!a^n.
 \tag{ON.1}
\]

Indeed, a term in which any factor is differentiated twice vanishes. The surviving terms differentiate every factor exactly once; there are \(n!\) orders, all giving the same ordered product \(a^n\). No commutation between \(a\) and \(y\) is needed. Since \(\|d\|\le2\|x\|\),

\[
\begin{gathered}
\|a^n\| \\
\le\frac{(2\|x\|\|y\|)^n}{n!}.
\end{gathered}
\tag{ON.2}
\]

For every nonzero complex \(\lambda\), the series \(\sum_{n\ge0}\lambda^{-n-1}a^n\) converges in norm by this factorial bound. Multiplication on either side by \(\lambda1-a\) telescopes to the identity. Thus every nonzero \(\lambda\) lies in the resolvent. On the other hand, if \(a\) were invertible, then \(1\le\|a^{-1}\|^n\|a^n\|\), contradicting (ON.2) as \(n\to\infty\). Therefore \(\sigma(a)=\{0\}\). This proves the source's assertion, which assumes in addition that \(a\) commutes with \(y\), and avoids any unsupported rule about adding spectra of commuting operators.

If \(x,y\in M\) and \([x,y]\in Z\), then \(a\) is normal. The C*-identity and continuous calculus of the positive element \(a^*a\) give

\[
 \|a^n\|^2=\|(a^*a)^n\|=\|a\|^{2n}.
\]

Combining with (ON.2) gives \(\|a\|\le2\|x\|\|y\|/(n!)^{1/n}\), hence \(a=0\). To see the last limit directly, at least \(\lfloor n/2\rfloor\) factors in \(n!\) are at least \(n/2\). Central commutators in a von Neumann algebra therefore vanish. The assertion for the zero algebra is immediate and uses no nonempty-spectrum convention on its zero representation.

## The Lie algebra quotient and its vanishing center

Define the real-linear map \(\Phi:M\to B(H)\) by \(\Phi(x)=x+JxJ\). GN proves that its image is exactly \(\mathfrak g\), and that its kernel is \(iZ_{\mathrm{sa}}\). The cross terms in the following commutator vanish because \(M\) and \(JMJ=M'\) commute:

\[
\begin{gathered}
{}[\Phi(x),\Phi(y)] \\
=\Phi([x,y]).
\end{gathered}
\tag{ON.3}
\]

Consequently \(\mathfrak g\) is closed under real linear combinations and commutators. The Jacobi identity follows by expanding the three double commutators: each ordered triple product occurs twice with opposite signs. Thus it is a real Lie algebra, with no separate Lie–Trotter argument for commutators required.

Let \(\mathfrak c\) be its center. If \(\Phi(x)\in\mathfrak c\), then \(\Phi([x,y])=0\) for every \(y\in M\). The kernel description puts \([x,y]\) in the center of \(M\); ON-01 makes it zero. Therefore \(x\in Z\). Conversely every central \(x\) clearly gives a central generator. Since \(JzJ=z^*\) for \(z\in Z\),

\[
\begin{gathered}
\mathfrak c=\Phi(Z)=Z_{\mathrm{sa}} \\
=\Phi(Z_{\mathrm{sa}}).
\end{gathered}
\tag{ON.4}
\]

In particular this is the set \(\{a+JaJ:a\in Z_{\mathrm{sa}}\}\). The equalities concern sets: \(\Phi(a)=2a\) on \(Z_{\mathrm{sa}}\). In particular \(\Phi^{-1}(\mathfrak c)=Z\). Put \(\widehat{\mathfrak g}=\mathfrak g/\mathfrak c\), and denote the coset of \(D\) by \(\widehat D\). The induced map

\[
\begin{gathered}
j:M/Z\longrightarrow\widehat{\mathfrak g}, \\
j(x+Z)=\widehat{\Phi(x)}.
\end{gathered}
\tag{ON.5}
\]

is a real-linear Lie algebra isomorphism. It is well defined and injective by the preimage identity, and surjective by GN.

The Lie algebra \(M/Z\) has zero center. If \(x+Z\) is central there, every \([x,y]\) belongs to \(Z\), hence is zero by ON-01, and \(x\in Z\). Therefore \(\widehat{\mathfrak g}\) has zero center too.

The map \(x\mapsto\operatorname{ad}x\) has kernel \(Z\), and its range is all everywhere-defined complex-linear derivations of \(M\): automatic boundedness supplies boundedness, and BI supplies innerness. Moreover \([\operatorname{ad}x,\operatorname{ad}y]=\operatorname{ad}[x,y]\), by direct expansion. Hence \(M/Z\) is also the complex Lie algebra of all such derivations. Here the word “all” does not omit the automatic-boundedness input. The quotient in (ON.5) is initially a real Lie quotient; its complex structure is supplied next.

## The orientation carried by the left algebra

Adjoints preserve \(\mathfrak g\), and \(\Phi(x)^*=\Phi(x^*)\). They preserve \(\mathfrak c\) too, so \(\widehat D^*=\widehat{D^*}\) is a well-defined real-linear involution on \(\widehat{\mathfrak g}\). It reverses Lie brackets: \([D,E]^*=-[D^*,E^*]\).

Define \(I_M\) by transporting multiplication by \(i\) on \(M/Z\) through \(j\). Explicitly,

\[
 I_M\widehat{\Phi(x)}=\widehat{\Phi(ix)}.
 \tag{ON.6}
\]

The complex linearity of the bracket on \(M/Z\) and \((ix)^*=-ix^*\) give

\[
\begin{gathered}
I_M^2=-\mathrm{id}, \\
I_M(u^*)=-(I_Mu)^*, \\
{}[I_Mu,v]=[u,I_Mv] \\
=I_M[u,v].
\end{gathered}
\tag{ON.7}
\]

An orientation means any real-linear map \(I\) of \(\widehat{\mathfrak g}\) satisfying these three properties. Its square condition already makes it bijective. No continuity assumption is added. For the zero quotient the unique map satisfies these identities and the reconstruction below still works.

## Comparing orientations by an algebraic involution

A centroid map of a real Lie algebra \(L\) is a real-linear map \(T\) satisfying \([Tu,v]=[u,Tv]=T[u,v]\). On a centerless Lie algebra any two centroid maps \(S,T\) commute. Indeed,

\[
\begin{gathered}
{}[STu,v]=[Tu,Sv] \\
=T[u,Sv]=TS[u,v],
\end{gathered}
\]

whereas the centroid identity for \(S\) and \(T\) also gives \([STu,v]=ST[u,v]\). Thus \((ST-TS)[u,v]=0\), and
\([ (ST-TS)u,v]=(ST-TS)[u,v]\), and this is zero for every \(v\). Centerlessness yields \((ST-TS)u=0\) for every \(u\). Compositions and inverses of invertible centroid maps are again centroid maps, by the same bracket identities.

Let \(I_1,I_2\) be orientations and put \(E=I_2I_1^{-1}\). All three maps \(I_1,I_2,I_M\) are centroid maps of the centerless algebra from ON-02, so they commute. Hence \(E^2=\mathrm{id}\), and \(E\) commutes with \(I_M\). The two anticommutation identities with the adjoint show \(E(u^*)=(Eu)^*\). Therefore

\[
\begin{gathered}
L_+=\ker(E-1), \\
L_-=\ker(E+1)
\end{gathered}
\]

are adjoint-stable real Lie ideals, \(L=L_+\oplus L_-\), and both are stable under \(I_M\). The decomposition is explicitly \(u=(u+Eu)/2+(u-Eu)/2\). For \(u\in L_+\), \(v\in L_-\), the centroid identity gives simultaneously \(E[u,v]=[u,v]\) and \(E[u,v]=-[u,v]\); thus \([L_+,L_-]=0\). Each ideal is centerless: an element central in one ideal also commutes with the other and hence with all of \(L\).

Take the inverse images under \(M\to M/Z\xrightarrow j L\):

\[
\begin{gathered}
A=\{x:\widehat{\Phi(x)}\in L_+\}, \\
B=\{x:\widehat{\Phi(x)}\in L_-\}.
\end{gathered}
\]

They are complex linear because the ideals are \(I_M\)-stable, and star closed because \(E\) commutes with adjoints. Both contain \(Z\); also \(M=A+B\) and \(A\cap B=Z\). Their mutual commutators lie in \(Z\), so ON-01 gives \([A,B]=0\).

In fact

\[
\begin{gathered}
A=B^\prime\cap M, \\
B=A^\prime\cap M.
\end{gathered}
\tag{ON.8}
\]

For example, if \(x\in A'\cap M\), its image in \(L\) commutes with \(L_+\). Its \(L_+\) component is therefore central in \(L_+\), hence zero. Thus \(x\in B\). The reverse inclusion is the mutual commutation already proved; the other equality is symmetric. These commutant formulas show that \(A,B\) are von Neumann subalgebras without assuming any continuity of the proposed orientations.

## The commuting ideals occupy complementary central summands

We prove the needed algebraic-to-central decomposition, including the ideal step. Let \(A,B\subset M\) be the subalgebras from ON-04. Write \(V\) for the linear span of commutators \([a_1,a_2]\) with \(a_i\in A\). Since \(M=A+B\) and \([A,B]=0\), every commutator \([m,a]\), with \(m\in M\), \(a\in A\), belongs to \(V\).

For \(v=[a_1,a_2]\) and \(m\in M\), the identity

\[
 vm=[a_1,a_2m]-a_2[a_1,m]
\]

shows \(vm\in A\): the first bracket belongs to \(V\) because its first entry is in \(A\), and the second term is a product in \(A\). Let \(\mathcal I\) be the ultraweak closure of the linear span \(VM\). It lies in \(A\), since \(A\) is ultraweakly closed.

This is a two-sided star ideal of \(M\). Right invariance is immediate. For \(m\in M\) and \(v=[a_1,a_2]\), the Jacobi product identity gives

\[
\begin{gathered}
{}[m,v]=[[m,a_1],a_2] \\
{}+[a_1,[m,a_2]]\in V.
\end{gathered}
\]

Consequently \(mv=vm+[m,v]\in VM\), proving left invariance. Also \(V^*=V\), and the adjoint of \(vm\) belongs to \(MV\subset VM\). Separate ultraweak continuity of multiplication and of adjoints extends these invariances to the closure.

Here is the central-projection description of such an ideal. If \(x\in\mathcal I\), then \(xx^*\in\mathcal I\) and the positive contractions \(xx^*(xx^*+n^{-1})^{-1}\) lie in \(\mathcal I\). Bounded spectral calculus makes them increase strongly to the left support \(\ell(x)\); bounded strong convergence is ultraweak convergence, so \(\ell(x)\in\mathcal I\). Finite joins of projections in \(\mathcal I\) lie there as well, by applying this argument to their positive sum. Let \(e\) be the join of all projections in \(\mathcal I\). The finite joins converge strongly and ultraweakly to \(e\), so \(e\in\mathcal I\). Unitary conjugations preserve \(\mathcal I\), hence preserve \(e\); the unitary-spanning argument proves \(e\in Z\). Every \(x\in\mathcal I\) has left support at most \(e\), giving \(x=ex\). Since \(e\in\mathcal I\), the reverse inclusion \(eM\subset\mathcal I\) follows from the ideal property. Thus \(\mathcal I=eM\subset A\).

All commutators of \(A\) vanish on \(1-e\). Hence \(A(1-e)\) is abelian and lies in the center of \(A\). It also commutes with \(B\), so it lies in \(Z(1-e)\). This gives

\[
 A=eM+Z.
\]

Every element of \(Be\) commutes with \(eM\), so \(Be\subset Ze\). Conversely, multiplying \(M=A+B\) by \(1-e\) and using \(A(1-e)\subset Z\subset B\) gives \((1-e)M\subset B\). Thus

\[
 B=(1-e)M+Z.
 \tag{ON.9}
\]

The quotient ideals \(L_+,L_-\) are exactly the images of \(eM\) and \((1-e)M\), respectively.

On \(L_+\) the equality \(E=1\), together with invariance under \(I_1\), gives \(I_2=I_1\). On \(L_-\) it gives \(I_2=-I_1\). This proves the comparison of any two orientations by a central projection. On an abelian central summand the quotient is zero, so no uniqueness of the projection there is asserted.

For precision, the image of \(eM\) can be denoted \(\widehat{\mathfrak g}(eP)\). The central projection \(e\) commutes with \(J\), and \(eP\) is the natural cone of the standard form of \(eM\) on \(eH\). GN identifies its generators with the corresponding \(e\)-supported generators in the original space, and passage to their centers gives exactly this quotient ideal. This notation makes no assertion that arbitrary noncentral compressions give Lie ideals.

## Switching to the commutant reverses the orientation

The same \((H,J,P)\) is a standard form for \(M'\). Indeed \(JM'J=M\), and for \(b=JaJ\in M'\), the product \(bJbJ=JaJ\,a=aJaJ\) preserves \(P\). Self-duality and the pointwise fixed-cone property of \(J\) are unchanged, as is the central identity. The center is the same \(Z\). For \(a\in M\),

\[
\begin{gathered}
\Phi_{M^\prime}(JaJ)=\Phi_M(a), \\
\Phi_{M^\prime}(iJaJ)=\Phi_M(-ia).
\end{gathered}
\]

Transporting multiplication by \(i\) through these identities gives \(I_{M'}=-I_M\).

Let \(e\in Z\) be a projection, and define the concrete algebra

\[
\begin{gathered}
N={} \\
eM+(1-e)M^\prime.
\end{gathered}
\tag{ON.10}
\]

It acts on \(H=eH\oplus(1-e)H\), with \(N'=eM'+(1-e)M\). The equality \(JeJ=e\) follows from the central standard-form identity. Also \(eP\subset P\), because \(eJeJ=e\) preserves the cone; the same holds for \(1-e\). Thus \(P=eP\oplus(1-e)P\) is the direct sum of the two self-dual cones. The preceding commutant argument on the second summand proves that \((N,H,J,P)\) is a standard form. Sigma-finiteness is preserved under central summands and taking the opposite algebra: \(a\mapsto Ja^*J\) is a projection-order preserving normal star anti-isomorphism onto the commutant. No separability hypothesis is inserted.

The calculation above on each summand gives

\[
\begin{gathered}
I_N=I_M\text{ on }\widehat{\mathfrak g}(eP), \\
I_N=-I_M \\
\text{on }\widehat{\mathfrak g}((1-e)P).
\end{gathered}
\]

Consequently any orientation obtained by those signs is precisely the orientation of \(N\). By ON-05 every orientation has this form, so the list is complete.

## A reconstruction formula inside the bounded operators

Let \(I=I_M\). For \(D,E\in\mathfrak g\), suppose \(\widehat E=I\widehat D\). Choose \(x\in M\) with \(D=\Phi(x)\), using GN. Then \(E-\Phi(ix)\in\mathfrak c=Z_{\mathrm{sa}}\); write that difference as \(z\). The conjugate linearity of \(J\) yields

\[
\begin{gathered}
D-iE={} \\
2x-iz\in M, \\
D+iE={} \\
2JxJ+iz\in M^\prime.
\end{gathered}
\tag{ON.11}
\]

Conversely every \(x\in M\) occurs as \(D-iE\), by taking \(D=\Phi(x/2)\) and \(E=\Phi(ix/2)\). Every element of \(M'\) occurs as \(D+iE\), since \(JMJ=M'\). Let \(\mathcal C_I\) be the set of pairs \((D,E)\in\mathfrak g^2\) with \(\widehat E=I\widehat D\), and define \(r_\pm(D,E)=D\pm iE\). The two set identities are

\[
\begin{gathered}
M=r_-(\mathcal C_I), \\
M^\prime=r_+(\mathcal C_I).
\end{gathered}
\tag{ON.12}
\]

Here \(i\) is the scalar imaginary unit in \(B(H)\); the orientation \(I\) acts on quotient classes, not on an unchosen representative. The factor two in (ON.11) is accounted for by the halves in the converse, and the real central ambiguity supplies all complex central elements.

The right sides use only the cone in the given complex Hilbert space, its bounded generator algebra, and the chosen orientation. They determine the concrete left algebra and its commutant. Replacing \(I\) by another orientation reconstructs exactly one of the centrally switched algebras in ON-06, without a new classification input.

## Two checks on the quotient and on orientation ambiguity

If \(M\) is abelian, then \(M=M'\), \(\mathfrak g=Z_{\mathrm{sa}}\), and \(\widehat{\mathfrak g}=0\). There is only one orientation on this zero space. Formula (ON.12) reduces to all differences \(D-iE\) of two self-adjoint central elements, which is exactly \(M\). Thus the reconstruction does not lose the center even though the quotient itself does.

For the matrix factor \(M_n(\mathbb C)\), \(n\ge2\), in Hilbert–Schmidt standard form, \(\Phi(x)X=xX+Xx^*\). Its kernel is \(i\mathbb R1\), and the center of its image is \(\mathbb R I_H\). For \(E=\Phi(ix)\), the difference \(\Phi(x)-i\Phi(ix)\) is left multiplication by \(2x\), while the sum is right multiplication by \(2x^*\). These identities verify the signs in (ON.11). For any nonabelian factor, the central projections are only zero and one. Thus its orientations are precisely \(I_M\) and \(-I_M\), corresponding to the left and right algebras. They are distinct because \(\widehat{\mathfrak g}\ne0\) for a nonabelian factor and \(I_M^2=-\mathrm{id}\). On a direct sum of factors the choices can differ on the central summands, exactly as ON-05 permits.

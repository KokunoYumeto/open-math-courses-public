# Smooth algebras over a field and the Jacobian criterion

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A polynomial equation can cut out a well-behaved local ring while its derivative misses that fact over the ground field. Smoothness keeps both the local ring and its relation to the field in view. We will turn the infinitesimal lifting criterion into a test using derivatives, then prove that smooth algebras are flat.

Throughout, \(k\) is a field and \(S\) is a finite-type \(k\)-algebra. Thus \(S\) is Noetherian and finitely presented. For a prime \(\mathfrak q\), write \(x\) for its point, \(\kappa=\kappa(\mathfrak q)\), and

\[
a_x=\dim_\kappa(\Omega_{S/k}\otimes_S\kappa),
\qquad t_x=\operatorname{trdeg}_k\kappa.
\tag{1}
\]

Smooth at \(\mathfrak q\) means that some principal neighborhood \(S_g\), with \(g\notin\mathfrak q\), is smooth over \(k\). Smooth means finitely presented and formally smooth, as in *Formally smooth, unramified and étale ring maps*. Its Theorems 4.1 and 5.1 give standard smooth presentations and principal standard smooth neighborhoods. We also use differential localization, quotient presentations and split conormal sequences from *Kähler differentials*, Theorems 2.2, 3.3, 5.1 and Proposition 3.4.

## 1. The dimension that derivatives measure

The dimension at a point is

\[
d_x=\dim_x\operatorname{Spec}S
=\min_{x\in U,\ U\text{ open}}\dim U.
\tag{2}
\]

Theorem 6.1 of *Krull dimension and Noether normalization* proves

\[
d_x=\max_{\mathfrak p\text{ minimal},\ \mathfrak p\subseteq\mathfrak q}
\dim(S/\mathfrak p)
=\dim S_{\mathfrak q}+t_x.
\tag{3}
\]

Thus \(d_x\) records the largest component through \(x\). The local ring dimension counts chains ending at \(x\). At closed points these agree, because the residue field is finite over \(k\), by the Nullstellensatz. At the generic point of the affine line, \(d_x=1\) while \(S_{(0)}=k(T)\) has dimension zero. Its differential fibre has dimension one. This already rules out replacing \(d_x\) by the local ring dimension in a smoothness test.

We use two more established results. Theorem 4.2 of the dimension lesson gives
\(\dim k[X_1,\ldots,X_n]_{\mathfrak Q}=n-\operatorname{trdeg}_k\kappa(\mathfrak Q)\).
Theorems 1.1 and 3.2 and Proposition 3.3 of *Regular local rings* say that polynomial local rings over fields are regular, that a regular local ring is a domain, and that independent classes in its maximal ideal modulo its square extend to a regular system of parameters. Quotienting by \(r\) of those parameters gives a regular local domain of dimension smaller by \(r\).

**Lemma 1.1.** Always \(a_x\geq d_x\). If equality holds, a principal standard smooth neighborhood of \(x\) exists.

**Proof.** Choose a presentation

\[
S=P/I,\quad P=k[X_1,\ldots,X_n],\quad I=(f_1,\ldots,f_m),
\quad \mathfrak Q=\pi^{-1}(\mathfrak q).
\tag{4}
\]

The differential presentation gives

\[
\kappa^m\xrightarrow{J(x)^{\mathsf t}}\kappa^n
\longrightarrow\Omega_{S/k}\otimes_S\kappa\longrightarrow0,
\qquad
J_{ij}=\frac{\partial f_i}{\partial X_j}.
\tag{5}
\]

Here the equations index the rows; the variables index the columns. If \(r\) is the row rank, then \(a_x=n-r\). Select \(r\) equations whose differentials are independent, and an \(r\)-column minor \(\Delta\) nonzero at \(x\). Reorder these equations as \(f_1,\ldots,f_r\). When \(r=0\), the selected list is empty and \(\Delta=1\).

Put \(B=P_{\mathfrak Q}\). Its residue field is \(\kappa\), and it is regular of dimension \(n-t_x\). The differential map

\[
\mathfrak Q B/(\mathfrak Q B)^2\longrightarrow
\Omega_{P/k}\otimes_P\kappa
\tag{6}
\]

sends the classes of the selected equations to their independent differentials. Therefore those classes are independent. We do not assume that (6) itself is injective. The parameter theorem gives a regular local domain

\[
C=B/(f_1,\ldots,f_r)B,\qquad \dim C=n-t_x-r.
\tag{7}
\]

It surjects onto \(S_{\mathfrak q}\). Dimensions cannot increase under a quotient, so (3) yields \(d_x\leq n-r=a_x\).

Suppose equality holds. The kernel of \(C\to S_{\mathfrak q}\) must be zero. Indeed, a nonzero element \(u\) of that kernel is a nonunit and a nonzerodivisor in the domain \(C\). Theorem 3.2 of *Dimension theory of Noetherian local rings* gives \(\dim(C/uC)=\dim C-1\), contradicting equality of the dimensions of \(C\) and its further quotient \(S_{\mathfrak q}\). Hence
\(I_{\mathfrak Q}=(f_1,\ldots,f_r)_{\mathfrak Q}\).

The module \(I/(f_1,\ldots,f_r)\) is finite over \(P\). Choose a denominator outside \(\mathfrak Q\) annihilating each of its finitely many generators and multiply those denominators. This gives \(h\notin\mathfrak Q\) with \(I_h=(f_1,\ldots,f_r)_h\). Replace \(h\) by \(h\Delta\), and let \(g\) be its image in \(S\). Then

\[
S_g=k[X_1,\ldots,X_n,Z]/(f_1,\ldots,f_r,hZ-1).
\tag{8}
\]

The minor using the selected variable columns together with \(Z\) has block form
\(\left(\begin{smallmatrix}J_0&0\\ Z\,\partial h&h\end{smallmatrix}\right)\).
Its determinant \(h\Delta\) is a unit in (8). This is a standard smooth presentation by Theorem 4.1 of the formal smoothness lesson. \(\square\)

The proof explains why the rank condition controls all equations, rather than just the selected equations: equality of dimensions first removes the kernel in the regular local domain; finite generation then removes it on a neighborhood.

## 2. The criterion and its open locus

**Theorem 2.1.** At every prime of every finite-type \(k\)-algebra,

\[
S\text{ is smooth at }x
\quad\Longleftrightarrow\quad a_x\leq d_x
\quad\Longleftrightarrow\quad a_x=d_x.
\tag{9}
\]

Every smooth local ring \(S_{\mathfrak q}\) is regular.
[Stacks, Tags 00TR, 00TT.]

**Proof.** Lemma 1.1 proves the inequality and the sufficient direction. For the converse, replace a smooth neighborhood by a principal standard smooth neighborhood. Write it as
\(k[Y_1,\ldots,Y_N]/(F_1,\ldots,F_c)\), with an invertible \(c\)-column Jacobian minor. At the polynomial prime above \(x\), the classes of these \(c\) equations are independent in the maximal ideal modulo its square, by the reasoning in (6). They are part of a regular system of parameters. Consequently

\[
\dim S_{\mathfrak q}=N-t_x-c,\qquad
d_x=N-c.
\tag{10}
\]

The standard smooth differential calculation gives \(a_x=N-c\). It also gives regularity of \(S_{\mathfrak q}\) by the parameter quotient theorem. Localizing the original algebra does not change its local ring or its differential fibre at \(x\), so these assertions concern \(S\) itself. \(\square\)

**Corollary 2.2 (Jacobian criterion).** In the presentation (4), smoothness at \(x\) is equivalent to

\[
\operatorname{rank}_\kappa
\left(\frac{\partial f_i}{\partial X_j}(x)\right)
=n-d_x.
\tag{11}
\]

The smooth locus is open; its complement, called the nonsmooth locus over \(k\), is closed.

**Proof.** Equation (5) says \(a_x=n-\operatorname{rank}J(x)\), so Theorem 2.1 gives (11). Each smooth point has a principal smooth neighborhood, all of whose points are smooth. Their union is the smooth locus. \(\square\)

If all irreducible components have dimension \(d\), then \(d_x=d\) everywhere. The nonsmooth locus is precisely the vanishing set of the \((n-d)\)-minors of \(J\). The ideal of zero-size minors is the unit ideal; if the requested size exceeds the matrix size, its minors generate zero. For components of different dimensions, (11) uses the component dimension through the point, which can vary. Openness still holds by the proof above; a single global dimension need not give a correct fixed-size test.

Smoothness remains smoothness after extension of the ground field, by the base-change theorem in the preceding lesson. Theorem 2.1 then shows that every field extension of a smooth \(k\)-algebra has regular local rings. This is geometric regularity in this direction.

## 3. Cotangent spaces and separable residue fields

**Proposition 3.1.** At a \(k\)-rational closed point \(\mathfrak m\), there is a natural isomorphism

\[
\mathfrak m/\mathfrak m^2
\ \cong\ \Omega_{S/k}\otimes_S k.
\tag{12}
\]

If \(k\) is algebraically closed, every closed point is rational, and smoothness at a closed point is equivalent to regularity of \(S_{\mathfrak m}\).
[Stacks, Tags 00TU, 00TS.]

**Proof.** The quotient \(S\to k\) has the structural \(k\)-algebra section. Proposition 3.4 of the differential lesson makes its conormal sequence split exact. Its last module is \(\Omega_{k/k}=0\), giving (12). Localization identifies \(\mathfrak m/\mathfrak m^2\) with the cotangent space of \(S_{\mathfrak m}\). A Noetherian local ring is regular exactly when its embedding dimension equals its dimension. At this point (3) has \(t_x=0\), so (12) and Theorem 2.1 give the equivalence. The Nullstellensatz proves the rationality assertion over an algebraically closed field. \(\square\)

For a finitely generated field extension, “separably generated over \(k\)” means that it has a transcendence basis \(T_1,\ldots,T_t\) such that the extension of \(k(T_1,\ldots,T_t)\) is finite separable. This is the separability hypothesis used next, including the transcendental case.

**Theorem 3.2.** If \(\kappa(\mathfrak q)/k\) is separably generated, then

\[
a_x=\operatorname{embdim}S_{\mathfrak q}+t_x.
\tag{13}
\]

In particular \(S\) is smooth at \(\mathfrak q\) if and only if \(S_{\mathfrak q}\) is regular.
[Stacks, Tag 00TV.]

**Proof.** Put \(A=S_{\mathfrak q}\), with maximal ideal \(\mathfrak n\). The map \(k\to\kappa\) is formally smooth: a purely transcendental field is a localization of a polynomial algebra, and the finite separable extension is formally étale by Proposition 6.3 of the preceding lesson. Formal smoothness is stable under composition. Applied to
\(A/\mathfrak n^2\to\kappa\), whose kernel has square zero, it gives a \(k\)-algebra section of this quotient.

The split conormal result now gives

\[
0\longrightarrow\mathfrak n/\mathfrak n^2
\longrightarrow\Omega_{(A/\mathfrak n^2)/k}\otimes_{A/\mathfrak n^2}\kappa
\longrightarrow\Omega_{\kappa/k}\longrightarrow0.
\tag{14}
\]

Its middle term equals \(\Omega_{A/k}\otimes_A\kappa\): the extra quotient relations have differentials \(d(ab)=a\,db+b\,da\) for \(a,b\in\mathfrak n\), and these vanish after tensoring with \(\kappa\). Differential localization identifies that term with the fibre in (1). Theorem 6.2 of the differential lesson gives \(\dim_\kappa\Omega_{\kappa/k}=t_x\). Taking dimensions in (14) proves (13). Equations (3), (9) and (13) turn smoothness into
\(\operatorname{embdim}A=\dim A\), precisely regularity. \(\square\)

**Corollary 3.3.** In characteristic zero, a reduced finite-type \(k\)-algebra is smooth on a dense open subset.

**Proof.** Every finitely generated extension of a characteristic-zero field is separably generated. Choose a transcendence basis; the remaining algebraic extension is finite. Every irreducible polynomial there has nonzero derivative, since characteristic zero makes the derivative of a nonconstant polynomial nonzero; irreducibility then makes it relatively prime to that derivative.

At each minimal prime of \(S\), the local ring is reduced, Noetherian and zero-dimensional, hence a field by Theorem 4.2 of *Noetherian and Artinian rings*. It is regular. Theorem 3.2 shows smoothness at every such generic point. The open smooth locus contains every generic point of every component, and is therefore dense. For \(S=0\), the empty space itself is the required dense open. \(\square\)

This assertion concerns smoothness of a reduced algebra over a field. Relative generic smoothness for maps between varieties has additional source and target hypotheses.

## 4. Regularity can miss inseparability

Take \(k=\mathbb F_p(t)\) and

\[
L=k[U]/(U^p-t).
\tag{15}
\]

The element \(t\) is not a \(p\)-th power in \(k\): its order at \(t=0\) is one, whereas a rational function raised to the \(p\)-th power has order divisible by \(p\). To see irreducibility without an unstated criterion, let \(\alpha^p=t\) in an algebraic closure. A monic proper factor of \(U^p-t=(U-\alpha)^p\) would be \((U-\alpha)^e\) for \(1\leq e<p\). Its coefficient \(-e\alpha\) would lie in \(k\), forcing \(\alpha\in k\), a contradiction. Thus \(L\) is a field and has a regular, zero-dimensional local ring.

But \(d(U^p-t)=0\) relative to \(k\). Hence
\(\Omega_{L/k}=L\,dU\), and \(a_x=1>d_x=0\). It is not smooth. Moreover

\[
L\otimes_k L=L[\epsilon]/(\epsilon^p),
\qquad \epsilon=1\otimes U-U\otimes1,
\tag{16}
\]

as follows by translating \(U\) by its root in the first factor. The class \(\epsilon\) is nonzero by the monic polynomial basis and is nilpotent. Regularity over \(k\) did not survive this field extension.

## 5. Flatness over a Noetherian base

We now allow a general commutative base ring \(R\).

**Theorem 5.1.** If \(R\) is Noetherian and \(R\to S\) is smooth, then \(S\) is flat over \(R\).
[Stacks, Tags 00TA, 00MF.]

**Proof.** Standard smooth principal neighborhoods cover \(\operatorname{Spec}S\), by Theorem 5.1 of the preceding lesson. Flatness is local on the target, by Theorem 3.3 of *Tor and flat modules*, so it suffices to treat

\[
S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c)
\tag{17}
\]

with a unit \(c\)-column Jacobian minor. Fix \(\mathfrak q\in\operatorname{Spec}S\), its preimage \(\mathfrak Q\) in \(P=R[X_1,\ldots,X_n]\), and \(\mathfrak p=\mathfrak q\cap R\). The local map
\(R_{\mathfrak p}\to B=P_{\mathfrak Q}\) is flat: polynomial algebras are free over the base, and localization preserves flatness. Both rings are Noetherian. Its closed fibre

\[
C=B/\mathfrak pB
\tag{18}
\]

is a local ring of the polynomial algebra \(\kappa(\mathfrak p)[X_1,\ldots,X_n]\), so is regular.

The images of the \(f_i\) lie in the maximal ideal of \(C\). Their differentials over \(\kappa(\mathfrak p)\) are independent after tensoring with its residue field, because the chosen minor remains a unit. Their cotangent classes are therefore independent, just as in (6). The regular parameter theorem makes them part of a regular system of parameters in \(C\). In particular they form a regular sequence in this ambient closed fibre.

Corollary 5.3 of *Faithful flatness and the local criterion for flatness* now applies successively to this list: starting with the flat local map \(R_{\mathfrak p}\to B\), quotient by each equation whose image is regular in the successive closed fibre. It gives flatness of
\(B/(f_1,\ldots,f_c)B=S_{\mathfrak q}\) over \(R_{\mathfrak p}\). Local flatness detection at every target prime proves flatness of \(S\) over \(R\). \(\square\)

The fibre in (18) is the ambient polynomial fibre before imposing the equations. Applying a slicing criterion directly to the already-quotiented fibre would lose the regular sequence whose injectivity the proof needs.

## 6. Removing Noetherianity; the étale consequence

**Theorem 6.1.** Every smooth ring map is flat, over an arbitrary commutative base.

**Proof.** First take a standard smooth presentation (17), and write \(\Delta\) for its selected Jacobian determinant in the polynomial ring. Its image is a unit in \(S\). Consequently there are polynomials \(w,a_1,\ldots,a_c\) with

\[
\Delta w-1=\sum_{i=1}^c a_i f_i
\quad\text{in }R[X_1,\ldots,X_n].
\tag{19}
\]

Indeed, lift an inverse of \(\Delta\) from the quotient; the difference from one belongs to its defining ideal.

Let \(R_0\subseteq R\) be the subring generated over the image of \(\mathbb Z\) by all coefficients of the finitely many polynomials \(f_i,w,a_i\). It is a finite-type quotient of a polynomial ring over \(\mathbb Z\), hence Noetherian by the Hilbert basis theorem. The coefficients of \(\Delta\) also belong to \(R_0\), because differentiation and determinants use integer operations on the coefficients of the \(f_i\). Identity (19) is an identity already in \(R_0[X]\), as this polynomial ring embeds in \(R[X]\).

Thus
\(S_0=R_0[X_1,\ldots,X_n]/(f_1,\ldots,f_c)\)
is standard smooth over \(R_0\). Theorem 5.1 makes it flat, and

\[
S=R\otimes_{R_0}S_0
\tag{20}
\]

is flat over \(R\) by base change. The empty equation list is included, with \(\Delta=w=1\). Finally every smooth algebra is covered by principal standard smooth neighborhoods. Apply this argument to each chart, then local flatness detection to obtain flatness of the original algebra. \(\square\)

The certificate (19) matters. Descending only the coefficients of the equations need not ensure that the selected determinant is invertible over the smaller ring. Descending the certificate ensures it.

**Corollary 6.2.** An étale ring map is flat, unramified and finitely presented, over any base.

**Proof.** The preceding lesson defines étale as finitely presented and formally étale. Such a map is formally smooth, so Theorem 6.1 gives flatness. Formal unramifiedness is equivalent to \(\Omega=0\) by its Theorem 2.2. Together with finite presentation, hence finite type, this is unramifiedness in our convention. \(\square\)

**Theorem 6.2 (flat and unramified).** A ring map is étale if and only if it is flat, unramified and finitely presented [Stacks, Tag 08WD]. There is no Noetherian assumption.

**Proof.** The forward direction follows from Theorem 6.1 and the definition of étale. Conversely write the finitely presented algebra as \(S=P/I\), with \(P=R[X_1,\ldots,X_n]\) and \(I\) finitely generated. Unramifiedness says \(\Omega_{S/R}=0\), so the conormal map onto \(S^n\) is surjective. At a chosen prime \(\mathfrak q\subset S\), select \(n\) elements \(f_1,\ldots,f_n\in I\) whose differential vectors form a basis modulo \(\mathfrak q\); possible because the images of all elements of \(I\) span that finite-dimensional vector space. Let \(\Delta\) be their full Jacobian determinant, which is outside \(\mathfrak q\). If \(n=0\), take the empty list and determinant one. The square presentation
\[
C=(P/(f_1,\ldots,f_n))_\Delta\twoheadrightarrow S_\Delta
\tag{20a}
\]
is standard smooth with zero differentials, hence étale by the formal lifting proof in the preceding lesson. It is flat over \(R\) by Theorem 6.1. Its kernel \(K\) is finitely generated: it is the image of the finite generating list of \(I\).

Let \(\mathfrak r\subset C\) be the prime corresponding to \(\mathfrak q\), and \(\mathfrak p=\mathfrak q\cap R\). Flatness of \(S_\Delta\) over \(R\) makes the sequence \(0\to K\to C\to S_\Delta\to0\) remain left exact after tensoring with \(\kappa(\mathfrak p)\): its possible kernel is \(\operatorname{Tor}_1^R(S_\Delta,\kappa(\mathfrak p))=0\). Localize this sequence at the fibre prime corresponding to \(\mathfrak r\). The local fibre of \(C\) is a finite separable field, by Theorem 7.2 of the preceding lesson, applied after base change. Its quotient, the local fibre of \(S\) at \(\mathfrak q\), is nonzero since that prime exists. The quotient of the field is therefore the same field. It follows that
\[
K_{\mathfrak r}/\mathfrak pK_{\mathfrak r}=0.
\]
Here the base is \(R_{\mathfrak p}\), so this is exactly the localized tensor with \(\kappa(\mathfrak p)\); all base denominators outside \(\mathfrak p\) are units in \(C_{\mathfrak r}\). Since \(\mathfrak pC_{\mathfrak r}\) lies in its maximal ideal and \(K_{\mathfrak r}\) is finite, Nakayama gives \(K_{\mathfrak r}=0\). Choose one element outside \(\mathfrak r\) killing the finite kernel after localization. On the resulting principal neighborhood, (20a) is an isomorphism. Thus \(S\) is étale on a neighborhood of each prime.

For clarity, these local lifts give the global formal lifting property. Given \(S\to A/J\) with \(J^2=0\), a finite principal étale cover of \(\operatorname{Spec}S\) pulls back to a principal cover of \(\operatorname{Spec}(A/J)\). Lift its denominators to \(A\); they still generate the unit ideal, because \(1+j\) is a unit for \(j\in J\). Lift on each localization of \(A\). On overlaps uniqueness holds by \(\Omega_{S/R}=0\), so the lifts agree and glue by the principal-cover equalizer for rings proved in the localization lesson. Uniqueness holds for the same reason. Together with finite presentation this proves étaleness. \(\square\)

## 7. Exercises

**Exercise 7.1 (easy).** For \(A=k[x,y]/(y^2-x^3-ax-b)\) with \(\operatorname{char}k\ne2\), find all geometric nonsmooth points and prove that \(A\) is smooth exactly when \(4a^3+27b^2\ne0\). Include characteristic three.

**Exercise 7.2 (easy).** Determine the smooth locus of \(k[x,y,z]/(xy-z^2)\) in every characteristic, and compare regularity at the origin.

**Exercise 7.3 (medium).** Over a perfect field of characteristic \(p>0\), show that \(x^p+y^p=1\) defines a nonreduced curve. Compute its differential fibres and smooth locus. Decide whether perfectness is needed.

**Exercise 7.4 (medium).** Prove that a finite \(k\)-algebra is étale if and only if it is geometrically reduced, meaning that its scalar extension to every field extension of \(k\) is reduced.

**Exercise 7.5 (hard).** If \(k\) has characteristic zero and \(k[X_1,\ldots,X_n]/(f)\) is reduced, prove that it is smooth on a dense open. For nonzero nonconstant \(f\), identify an open using its partial derivatives and verify that it meets every component.

**Exercise 7.6 (hard).** For \(A=k[x,y,z]/(xy,xz)\), determine the smooth locus at all primes. At the two generic points and the origin, compute the point dimension, local ring dimension, residue transcendence degree and differential fibre dimension. Explain the failure of tests using either one global dimension or the local ring dimension everywhere.

## 8. Solutions

**Solution 7.1.** Every component of this curve has dimension one: in the UFD \(k[x,y]\), a minimal prime of the nonzero nonunit defining equation is generated by an irreducible factor, and the polynomial height formula gives dimension one. Thus the Jacobian test fails exactly where both derivatives vanish. Over an algebraic closure, these points have

\[
y=0,\qquad 3x^2+a=0,\qquad x^3+ax+b=0.
\tag{21}
\]

If the characteristic is neither two nor three, a solution \(x=r\) forces
\(a=-3r^2,\ b=2r^3\), hence \(4a^3+27b^2=0\). Conversely, if this expression vanishes and \(a=0\), then \(b=0\) and \(r=0\) works. If \(a\ne0\), put \(r=-3b/(2a)\). The discriminant identity gives \(r^2=-a/3\), and hence \(r^3=r(-a/3)=b/2\). These identities give all three equations in (21).

In characteristic three, the \(x\)-derivative is \(-a\), so there are no nonsmooth points if \(a\ne0\). If \(a=0\), the unique root \(r\) of \(r^3=-b\) in the algebraic closure gives the point \((r,0)\). The expression \(4a^3+27b^2\) is then \(a^3\), giving the same test.

This also tests smoothness over \(k\) itself. If the expression is nonzero, the equations and the two derivatives have no common zero over the algebraic closure; the Nullstellensatz makes their ideal the unit ideal there. Field extension is faithfully flat, so ideal contraction makes it the unit ideal over \(k\). Thus every prime satisfies the rank test. If the expression is zero, the displayed algebraic point defines a residue field of the original algebra at which both derivatives vanish, so it is not smooth. Over an imperfect field, these are geometric nonsmooth points; calling them irregular points without checking separability would be unjustified.

**Solution 7.2.** The cone is a domain of dimension two by the characteristic-free cone calculation in §6 of *Regular local rings*. Its Jacobian row is \((y,x,-2z)\). A prime containing \(x\) and \(y\) also contains \(z\), since \(z^2=xy\); it is the origin ideal. Away from that ideal, \(x\) or \(y\) is invertible. On \(D(x)\) the equation solves \(y=z^2/x\), giving the polynomial localization \(k[x,x^{-1},z]\); \(D(y)\) is analogous. Both charts are smooth. At the origin all row entries vanish even when the characteristic is two, so the differential fibre has dimension three while \(d_x=2\). Theorem 2.1 proves nonsmoothness. The equation has no linear term, so the local cotangent space has dimension three and the local dimension is two; its local ring is also not regular.

**Solution 7.3.** In characteristic \(p\),
\(x^p+y^p-1=(x+y-1)^p\).
Set \(u=x+y-1\). The invertible linear change of variables gives
\(A=k[u,y]/(u^p)\), a free \(k[y]\)-module with basis
\(1,u,\ldots,u^{p-1}\). Thus \(u\ne0\) but \(u^p=0\). Its only minimal prime is \((u)\), with quotient \(k[y]\), so \(d_x=1\) everywhere. The defining differential is zero, and
\(\Omega_{A/k}=A\,du\oplus A\,dy\). Every differential fibre has dimension two, making the smooth locus empty by Theorem 2.1. The argument works over every field of characteristic \(p\); perfectness is unnecessary.

**Solution 7.4.** If \(A\) is étale, then \(A\otimes_k K\) is étale for every extension \(K/k\). Theorem 7.2 of the preceding lesson identifies it as a finite product of finite separable fields over \(K\), hence as reduced.

Conversely, geometric reducedness implies that \(A\) itself is reduced. A finite-dimensional algebra is Artinian; its reduced product decomposition gives
\(A=\prod_i L_i\) with each \(L_i/k\) finite. Each factor is geometrically reduced because it remains a direct factor after scalar extension. If some \(\alpha\in L_i\) had an inseparable minimal polynomial \(h\) over \(k\), then
\(\overline{k}\otimes_k k[\alpha]=\overline{k}[T]/(h)\)
would have a nonzero nilpotent: the factorization of \(h\) over \(\overline{k}\) has a repeated linear factor, and the corresponding local polynomial quotient is nonreduced. Tensoring the injection \(k[\alpha]\subset L_i\) with the field \(\overline{k}\) stays injective, preserving that nonzero nilpotent. This contradicts geometric reducedness of \(L_i\). Thus every element of \(L_i\) is separable over \(k\), so \(L_i/k\) is separable. Proposition 6.3 of the preceding lesson makes the product étale. The zero algebra is the empty product and satisfies both conditions.

**Solution 7.5.** For \(f\ne0\) nonconstant, reducedness makes \(f\) squarefree in the polynomial UFD. Indeed, a repeated irreducible factor produces a nonzero nilpotent modulo \(f\), whereas a product of distinct prime factors generates their intersection. Write \(f=c\prod_i g_i\), with \(c\in k^\times\) and distinct irreducible \(g_i\).

Each \(g_i\) depends on some variable \(X_j\). In characteristic zero its corresponding derivative is nonzero and has smaller total degree than \(g_i\), so \(g_i\) does not divide that derivative. Modulo \((g_i)\),

\[
\frac{\partial f}{\partial X_j}
=c\left(\prod_{\ell\ne i}g_\ell\right)
\frac{\partial g_i}{\partial X_j}\ne0.
\tag{22}
\]

The quotient by \(g_i\) is a domain, and no other factor becomes zero there. Thus the open
\(\bigcup_j D(\partial f/\partial X_j)\)
contains every component's generic point. Every component of the hypersurface has dimension \(n-1\), by the polynomial height formula. On this open the single Jacobian row has rank one, so Corollary 2.2 makes it smooth; containing every generic point makes the open dense. If \(f=0\), the algebra is polynomial and smooth everywhere. If \(f\) is a nonzero constant, it is the zero algebra and its empty spectrum is smooth.

**Solution 7.6.** The component calculation in Solution 8.1 of the dimension lesson gives the minimal primes \((x)\) and \((y,z)\), with quotients a plane and a line. Their intersection is the origin. On the plane away from the origin, \(y\) or \(z\) is invertible and the relations force \(x=0\), giving a polynomial plane chart. On \(D(x)\) the relations force \(y=z=0\), giving the smooth line chart \(k[x,x^{-1}]\). These cover every point except the origin.

The Jacobian is

\[
J=\begin{pmatrix}y&x&0\\ z&0&x\end{pmatrix}.
\tag{23}
\]

At the plane generic prime \((x)\), it has rank one; at the line generic prime \((y,z)\), it has rank two. At the origin it has rank zero. Formula (3), the component dimensions and (5) give

| Prime | \(d_x\) | \(\dim A_{\mathfrak q}\) | \(t_x\) | \(a_x\) |
|---|---:|---:|---:|---:|
| \((x)\) | 2 | 0 | 2 | 2 |
| \((y,z)\) | 1 | 0 | 1 | 1 |
| \((x,y,z)\) | 2 | 2 | 0 | 3 |

Consequently the origin is nonsmooth, and the charts prove that it is the entire nonsmooth locus. At both generic points, local ring dimension zero would falsely predict failure of smoothness. Conversely, using global dimension two in the equality test would falsely reject the line generic point, whose differential fibre has dimension one. The point dimension supplies the correct value in each case.

## References and proof scope

The Stacks project gives the field smoothness and differential criteria at the tags cited above, and the arbitrary-base framework at Tags 00TA and 08WD. Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), public draft of 27 July 2024, §§13.2–13.3, 21.5–21.6 and 24.8, provides geometric interpretations and comparisons. Timothy J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 10, Section 3.2, and Chapter 11, Section 5, discusses the differentials of separably generated field extensions and the differential and Jacobian criteria for regularity.

Verified tag references: [Tag 00TR](https://stacks.math.columbia.edu/algebra.html#lemma-rank-omega), [Tag 00TT](https://stacks.math.columbia.edu/algebra.html#lemma-characterize-smooth-over-field), [Tag 00TV](https://stacks.math.columbia.edu/algebra.html#lemma-separable-smooth), [Tag 00TS](https://stacks.math.columbia.edu/algebra.html#lemma-characterize-smooth-kbar), [Tag 00TU](https://stacks.math.columbia.edu/algebra.html#lemma-computation-differential), [Tag 00TW](https://stacks.math.columbia.edu/algebra.html#lemma-characteristic-zero), [Tag 07ND](https://stacks.math.columbia.edu/algebra.html#lemma-smooth-at-generic-point), [Tag 00TA](https://stacks.math.columbia.edu/algebra.html#lemma-smooth-syntomic), [Tag 00SL](https://stacks.math.columbia.edu/algebra.html#definition-lci), [Tag 08WD](https://stacks.math.columbia.edu/algebra.html#lemma-etale-flat-unramified-finite-presentation), [Tag 00MF](https://stacks.math.columbia.edu/algebra.html#lemma-grothendieck), [Tag 00OT](https://stacks.math.columbia.edu/algebra.html#lemma-dimension-at-a-point-finite-type-over-field), [Tag 00P1](https://stacks.math.columbia.edu/algebra.html#lemma-dimension-at-a-point-finite-type-field).

**Proof dependencies.** Theorem 6.2 proves the flat-and-unramified converse, using the conormal sequence, the preceding étale field classification, Tor base-change exactness, Nakayama and the earlier principal-cover equalizer. These arguments use no principal standard étale neighborhood theorem and therefore do not use its Zariski's Main Theorem prerequisite. All smoothness, Jacobian, flatness and exercise proofs appear above at their full stated generality.

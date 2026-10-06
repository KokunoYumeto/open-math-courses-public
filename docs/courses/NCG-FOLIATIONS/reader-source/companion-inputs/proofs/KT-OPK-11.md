# The six-term exact sequence and the exponential map

*Public domain (CC0).*
A quotient projection need not lift to a projection. Lift it instead to a self-adjoint matrix and exponentiate: its quotient exponential is identity, so the resulting unitary belongs to the ideal's unitization. This construction supplies the missing arrow that closes the index sequence into a cycle. Relative triples retain the quotient comparison itself; an explicit reduction shows that their group depends only on the ideal.

All algebras are complex C*-algebras, all ideals are closed, and maps are *-homomorphisms. We use external unitizations, the normalized index boundary of [Lesson 7, Theorems 2.2 and 4.1](KT-OPK-07.md), the forward doubled-path suspension \(\theta_D:K_1(D)\to K_0(SD)\) of [Lesson 8, Theorem 2.1](KT-OPK-08.md), and the positive Bott loop \(\beta_D:K_0(D)\to K_1(SD)\) of [Lesson 10, Theorem 4.1](KT-OPK-10.md). These are different typed maps. Their signs must be checked before identifying a suspended boundary with an exponential.

## 1. The missing boundary and its sign

Fix an extension

\[
E:\quad0\longrightarrow J\xrightarrow{\iota}A
\xrightarrow{\pi}B\longrightarrow0.
\tag{1.1}
\]

Its suspension is exact by Lesson 8, Corollary 1.3. Write \(\delta_E:K_1(B)\to K_0(J)\) for the index boundary and \(\delta_{SE}:K_1(SB)\to K_0(SJ)\) for its suspended version. Define

\[
\begin{gathered}
\boxed{\varepsilon_E=-\theta_J^{-1}\delta_{SE}\beta_B},\\
\varepsilon_E:K_0(B)\longrightarrow K_1(J).
\end{gathered}
\tag{1.2}
\]

The minus sign is part of the definition under our already fixed conventions.

**Theorem 1.1 (positive exponential formula).** Represent a class of \(K_0(B)\) in the normal form

\[
\begin{gathered}
{}[e]-[P],\\
e=e^*=e^2\in M_n(B^+),\\
\epsilon_B(e)=P,
\end{gathered}
\tag{1.3}
\]

where \(P\) is a scalar projection. Choose \(x=x^*\in M_n(A^+)\) with \(\pi^+(x)=e\) and \(\epsilon_A(x)=P\). Then

\[
\boxed{\varepsilon_E([e]-[P])=[\exp(2\pi i x)].}
\tag{1.4}
\]

The class in (1.4) belongs to \(K_1(J)\).

*Proof.* Lift the entries of \(e-P\) to \(A\), add \(P\), and take the self-adjoint part. This gives the required \(x\). Put \(u=\exp(2\pi i x)\). Functional calculus commutes with the quotient and augmentation; since \(e,P\) are projections, both images of \(u\) are identity. Thus \(u-I_n\in M_n(J)\), and \(u\) is a normalized unitary over \(J^+\).

Use the suspension variable \(s\in[0,1]\). The relative Bott loop and a unitary lift of it are

\[
\begin{aligned}
g(s)&=e^{2\pi i s e}e^{-2\pi i s P},\\
G(s)&=e^{2\pi i s x}e^{-2\pi i s P}.
\end{aligned}
\tag{1.5}
\]

Here \(G(0)=I_n\), \(G(1)=u\), its scalar part is constantly identity, and \(\pi^+G=g\). Lesson 10, (1.4), identifies \([g]\) with \(\beta_B([e]-[P])\).

Let \(U(s)\) be the doubled unitary path in \(M_{2n}(J^+)\), starting at identity and ending at \(\operatorname{diag}(u,u^*)\), given explicitly in Lesson 8, (2.2). Its scalar part is identity. Set

\[
\begin{aligned}
D(s)&=\operatorname{diag}(G(s),G(s)^*),\\
Z(s)&=D(s)U(s)^*,\qquad Q=\operatorname{diag}(I_n,0_n).
\end{aligned}
\tag{1.6}
\]

Both endpoints of \(Z\) are identity. Hence \(Z\) is a normalized invertible over \((SA)^+\) lifting \(\operatorname{diag}(g,g^*)\). The index formula gives

\[
\delta_{SE}[g]=[ZQZ^*]-[Q]\in K_0(SJ).
\tag{1.7}
\]

For \(0\leq r\leq1\), consider the projection loop

\[
H_r(s)=D(rs)U(s)^*Q U(s)D(rs)^*.
\tag{1.8}
\]

It is continuous in both parameters. In the quotient, \(U(s)\) is identity and \(D(rs)\) is block diagonal, so \(\pi^+H_r(s)=Q\). At \(s=0\) it is \(Q\). At \(s=1\), \(U(1)\) commutes with \(Q\), and so does \(D(r)\), giving \(H_r(1)=Q\). Its scalar part is also \(Q\). Thus (1.8) is a genuine homotopy over \((SJ)^+\), joining the projection in (1.7) to \(U^*Q U\).

The path \(U^*\) goes from identity to \(\operatorname{diag}(u^*,u)\). Therefore Lesson 8's formula identifies this last relative class with \(\theta_J[u^*]=-\theta_J[u]\). We have proved the typed identity

\[
\delta_{SE}\beta_B([e]-[P])
=-\theta_J[\exp(2\pi i x)].
\tag{1.9}
\]

Applying (1.2) proves (1.4), including its sign. All matrices are external-unitized, so the proof includes nonunital \(A,B,J\). \(\square\)

Two self-adjoint lifts with scalar part \(P\) are joined by their convex interpolation, still a self-adjoint lift of \(e\). Its exponential is a path of normalized unitaries over \(J^+\). This proves lift independence directly. Representative independence, stabilization, and additivity follow from (1.2), whose three factors are already well-defined homomorphisms. No logarithm of a quotient unitary is used.

## 2. Exactness at all six groups

**Theorem 2.1 (six-term sequence).** The following cyclic sequence is exact and natural for morphisms of extensions:

\[
\begin{aligned}
K_0(J)&\xrightarrow{\iota_*}K_0(A)
\xrightarrow{\pi_*}K_0(B)\\
&\xrightarrow{\varepsilon_E}K_1(J)
\xrightarrow{\iota_*}K_1(A)\\
&\xrightarrow{\pi_*}K_1(B)
\xrightarrow{\delta_E}K_0(J).
\end{aligned}
\tag{2.1}
\]

*Proof.* Lesson 7, Theorem 4.1, proves exactness at \(K_1(A),K_1(B),K_0(J),K_0(A)\). Its application to \(SE\) proves exactness at the two middle groups of

\[
\begin{aligned}
K_1(SA)&\longrightarrow K_1(SB)\\
&\xrightarrow{\delta_{SE}}K_0(SJ)\\
&\longrightarrow K_0(SA).
\end{aligned}
\tag{2.2}
\]

Naturality of \(\beta\) identifies the first map with \(\pi_*:K_0(A)\to K_0(B)\), through the two Bott isomorphisms. Equation (1.2) then makes exactness at \(K_1(SB)\) precisely
\(\ker\varepsilon_E=\operatorname{im}\pi_*\) at \(K_0(B)\).

Naturality of \(\theta\) identifies the last map in (2.2) with \(\iota_*:K_1(J)\to K_1(A)\). Since \(\beta_B\) is onto and the negative of a subgroup is the same subgroup, exactness at \(K_0(SJ)\) becomes
\(\operatorname{im}\varepsilon_E=\ker\iota_*\) at \(K_1(J)\). These are the two remaining assertions.

For a commutative diagram of extensions, index naturality gives commutation with both \(\delta_E\) and \(\delta_{SE}\). Naturality of \(\beta\) and \(\theta^{-1}\) gives commutation with (1.2). The four inclusion and quotient arrows commute by functoriality. This proves naturality of the entire cycle. \(\square\)

**Corollary 2.2 (lifting obstruction).** If \(e\) lifts to a projection over \(A^+\) with the required scalar part, then \(\varepsilon_E([e]-[P])=0\). More generally a class has zero exponential boundary exactly when it is in the image of \(K_0(A)\).

*Proof.* For an actual projection lift \(x\), \(\exp(2\pi i x)=I\). The general assertion is exactness at \(K_0(B)\). \(\square\)

The latter statement concerns a stable K-class. It does not assert that the particular matrix projection \(e\) has an unstabilized projection lift.

The positive boundary (1.4) is the one used in [*K-theory of the leaf space*, “Suspension, Bott periodicity and extension boundaries”](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/preparation.html#dependency-327fefcb6f08). Formula (1.9) specifies the sign when comparing it with our separate suspension map.

**Proposition 2.3 (Exact norm lifts and their limits).** Let \(q:A\to B\) be a surjective *-homomorphism of C*-algebras. Every \(b\in B\) has a lift \(a\in A\) with \(\|a\|=\|b\|\). If \(b\) is self-adjoint or positive, the lift can be chosen with that same property. These assertions hold at every matrix level. Projections, unitaries and normal elements can nevertheless fail to have lifts of the same kind.

*Proof.* For self-adjoint \(b\), symmetrize any lift to \(h=h^*\). Put \(r=\|b\|\) and \(f_r(t)=\max(-r,\min(t,r))\). The continuous functional calculus gives \(a=f_r(h)\), self-adjoint with norm at most \(r\), and naturality gives \(q(a)=f_r(b)=b\). This element is in \(A\) even if \(A\) has no unit, because \(f_r(0)=0\). Contractivity of \(q\) gives the reverse norm inequality. The case \(r=0\) simply gives the zero lift.

For \(b\geq0\), lift \(b^{1/2}\) to any \(x\). Then \(x^*x\) is a positive lift of \(b\). The cutoff \(g_r(t)=\max(0,\min(t,r))\), which again vanishes at zero, produces a positive norm-\(r\) lift by the same calculus and contractivity arguments.

For arbitrary \(b\), form

\[
\begin{gathered}
H=\begin{pmatrix}0&b\\b^*&0\end{pmatrix},\\
H^2=\operatorname{diag}(bb^*,b^*b).
\end{gathered}
\tag{2.3}
\]

Thus \(\|H\|=\|b\|\). The self-adjoint argument in \(M_2(A)\) gives a lift of \(H\) with that exact norm. Its upper-right corner lifts \(b\); corner compression bounds its norm by \(\|b\|\), and quotient contractivity gives equality. Apply these arguments to the surjection \(M_n(A)\to M_n(B)\) for every matrix size. The C*-matrix norm, contractivity and functional-calculus naturality are the continuous-functional-calculus prerequisites used throughout the course.

Here are full counterexamples to the three stronger lifting assertions. Endpoint evaluation \(C([0,1])\to\mathbb C\oplus\mathbb C\) is onto, by linear interpolation. The projection \((0,1)\) has no projection lift: a continuous function into \(\{0,1\}\) on the connected interval is constant.

Restriction \(C(\overline{\mathbb D})\to C(\mathbb T)\) is onto. For a boundary function, multiply its radial extension by a continuous radial cutoff which vanishes near the origin and equals one at the boundary. But \(z\) has no unitary lift. Such a lift would be a nonvanishing continuous function on the disc extending its winding-one boundary loop, contradicting [Lesson 2, Lemma 5.2](KT-OPK-02.md#5-gluing-around-a-circle-and-across-a-sphere).

Finally take the Toeplitz symbol quotient \(\mathcal T\to C(\mathbb T)\). Every operator lift \(T\) of \(z\) has the same invertible Calkin image as the unilateral shift. It is Fredholm, and the index/naturality argument of [Lesson 9, Theorem 3.1](KT-OPK-09.md#3-the-connecting-map-is-minus-winding) gives \(\operatorname{Ind}T=-1\). A normal operator satisfies \(\|T\xi\|=\|T^*\xi\|\), by \(T^*T=TT^*\), so its kernel equals the kernel of its adjoint. If Fredholm its index is therefore zero. Thus the normal, indeed unitary, symbol \(z\) has no normal lift. \(\square\)

This completes all lifting assertions of [Richard 2015, Proposition 2.3.1], including the counterexamples whose proofs that source delegates to exercises elsewhere. Exact norm attainment places no invertibility or projection condition on a general lift.

**Corollary 2.4 (A partial-isometry lift after zero padding).** Let \(q:A\to B\) be a unital surjective *-homomorphism, and let \(u\in M_n(B)\) be unitary. Then \(\operatorname{diag}(u,0_n)\) has a partial-isometry lift in \(M_{2n}(A)\).

*Proof.* Proposition 2.3 gives a lift \(c\) with \(\|c\|=\|u\|=1\). Set

\[
v=\begin{pmatrix}
c&0\\
(1-c^*c)^{1/2}&0
\end{pmatrix}.
\tag{2.4}
\]

The positive square root belongs to \(M_n(A)\), and multiplication gives \(v^*v=\operatorname{diag}(1_n,0_n)\). Since the second column of \(v\) is zero, \(v(v^*v)=v\); hence \(vv^*\) is also a projection and \(v\) is a partial isometry. Naturality of the square root gives \(q((1-c^*c)^{1/2})=(1-u^*u)^{1/2}=0\), so \(q(v)=\operatorname{diag}(u,0_n)\). \(\square\)

This is the universally available stabilized lift of [Richard 2015, Lemma 6.2.1]. It supplies no unstabilized partial-isometry lift of \(u\). The unstabilized lift in [Lesson 7, Proposition 5.1](KT-OPK-07.md#5-the-partial-isometry-formula) remains an explicit additional hypothesis there. For a nonunital extension, apply this corollary to the external unitalized quotient and retain its scalar data when evaluating relative classes.

## 3. Three complete computations

**Example 3.1 (the interval).** Endpoint evaluation gives

\[
0\to C_0((0,1))\to C[0,1]\to\mathbb C^2\to0.
\tag{3.1}
\]

Homotopy invariance and the line computation in Lessons 6 and 8 give ideal groups \((0,\mathbb Z)\), middle groups \((\mathbb Z,0)\), and quotient groups \((\mathbb Z^2,0)\). Choose the ideal's generator \(\omega(t)=e^{2\pi i t}\). The sole nontrivial part of (2.1) is

\[
0\longrightarrow\mathbb Z
\xrightarrow{k\mapsto(k,k)}\mathbb Z^2
\xrightarrow{(a,b)\mapsto b-a}\mathbb Z
\longrightarrow0.
\tag{3.2}
\]

Indeed the quotient projection \((0,1)\) lifts to the self-adjoint function \(t\), whose exponential is \(\omega\). The projection \((1,0)\) lifts to \(1-t\), giving \(\omega^{-1}\). Constants give the diagonal rank map. Every remaining arrow has zero source or target. The kernel of the difference map is the diagonal subgroup, and its image is all integers.

**Example 3.2 (the Toeplitz extension).** Let \(S\) be the unilateral shift and \(p_0=1-SS^*\). Lesson 9 gives

\[
0\to\mathcal K\to\mathcal T
\xrightarrow{\sigma}C(\mathbb T)\to0.
\tag{3.3}
\]

The groups in each column, listed as \((K_0,K_1)\), are \((\mathbb Z,0),(\mathbb Z,0),(\mathbb Z,\mathbb Z)\). The ideal inclusion on \(K_0\) is zero: \(SS^*\) is equivalent to \(1\), so \([p_0]=[1]-[SS^*]=0\) in \(K_0(\mathcal T)\). The quotient map on \(K_0\) is identity on the unit generators. The exponential is zero because its target \(K_1(\mathcal K)\) is zero. Both inclusion and quotient maps on \(K_1\) have zero source. Finally

\[
\delta_E[z]=-[p_0],\qquad
\delta_E[u]=-\operatorname{wind}(\det u)
\tag{3.4}
\]

under \(K_0(\mathcal K)=\mathbb Z[p_0]\). The first equality is the defect formula for the lift \(S\); the second is Lesson 9's matrix Toeplitz index theorem. This lists all six maps and verifies every kernel and image.

**Example 3.3 (the disc).** Write \(\overline{\mathbb D}\) for the closed disc and \(\mathbb D\) for its interior. Restriction to the boundary gives

\[
0\to C_0(\mathbb D)\to C(\overline{\mathbb D})
\to C(\mathbb T)\to0.
\tag{3.5}
\]

The three pairs of groups are \((\mathbb Z,0),(\mathbb Z,0),(\mathbb Z,\mathbb Z)\). Here Bott periodicity computes the ideal, contractibility computes the middle, and Lessons 3 and 6 compute the circle. The ideal inclusion on \(K_0\) is zero: composing it with evaluation at a boundary point is zero, while that evaluation is a K-isomorphism on the contractible closed disc. The quotient map on \(K_0\) is the rank isomorphism. The exponential and the two other \(K_1\)-maps are zero.

The coordinate \(z\) on the boundary lifts to \(a(w)=w\) on the closed disc. Put \(b(w)=\sqrt{1-|w|^2}\). The continuous matrix

\[
F(w)=\begin{pmatrix}w&-b(w)\\b(w)&\bar w\end{pmatrix}
\]

is unitary: its column norms are one and their inner product is zero. On the boundary it is \(\operatorname{diag}(z,\bar z)\). Thus it is a doubled lift in Lesson 7's index construction. In the external-unitization picture give it the additional scalar component \(I_2\), using Lesson 4's unital identification. Conjugating \(P_0\) by this lift gives

\[
\delta_E[z]=[q_{\mathbb D}]-[P_0],
\quad P_0=\operatorname{diag}(1,0),
\tag{3.6}
\]

where

\[
q_{\mathbb D}(w)=
\begin{pmatrix}
|w|^2&w\sqrt{1-|w|^2}\\
\bar w\sqrt{1-|w|^2}&1-|w|^2
\end{pmatrix}.
\tag{3.7}
\]

It is the rank-one projection onto the unit vector \((w,\sqrt{1-|w|^2})\), and equals \(P_0\) on the boundary. Under the orientation-preserving homeomorphism
\(\rho(\zeta)=\zeta/\sqrt{1+|\zeta|^2}\) from the plane to \(\mathbb D\), its pullback is

\[
\frac1{1+|\zeta|^2}
\begin{pmatrix}|\zeta|^2&\zeta\\\bar\zeta&1\end{pmatrix}.
\tag{3.8}
\]

Exchanging the two vector coordinates conjugates (3.8) to the projection of Lesson 10, (6.3), and sends \(P_0\) to \(\operatorname{diag}(0,1)\). Constant unitary conjugation preserves K-classes. Thus (3.6) is the positive plane Bott generator \(\mathfrak b\), with exactly the orientation of Lesson 10. In these generators the disc index map is \(n\mapsto n\), whereas the Toeplitz index map is \(n\mapsto-n\). The distinction follows from their explicit lifts.

## 4. Mayer–Vietoris with one surjective leg

Let \(\phi:B\to D\) be surjective and let \(\psi:C\to D\) be arbitrary. Form the pullback

\[
P=\{(b,c)\in B\oplus C:\phi(b)=\psi(c)\},
\quad J=\ker\phi.
\tag{4.1}
\]

Let \(r_B,r_C\) be its coordinate maps and \(k(j)=(j,0)\). The projection \(r_C\) is onto, because \(\phi\) is onto, and its kernel is \(k(J)\). There is a morphism of extensions from \(0\to J\to P\to C\to0\) to \(0\to J\to B\to D\to0\), using identity on \(J\), \(r_B\), and \(\psi\).

Write \(\partial_i:K_i(D)\to K_{i-1}(J)\) for the latter boundary, with indices modulo two: \(\partial_1=\delta\), \(\partial_0=\varepsilon\). Set

\[
\begin{aligned}
d_i(b,c)&=\phi_*b-\psi_*c,\\
\gamma_i&=k_*\partial_i.
\end{aligned}
\tag{4.2}
\]

The first line is a homomorphism of abelian groups. It is not being asserted to arise from subtracting algebra homomorphisms.

**Theorem 4.1.** There is a natural six-term Mayer–Vietoris sequence

\[
\begin{aligned}
K_0(P)&\xrightarrow{(r_{B*},r_{C*})}
K_0(B)\oplus K_0(C)\\
&\xrightarrow{d_0}K_0(D)
\xrightarrow{\gamma_0}K_1(P)\\
&\xrightarrow{(r_{B*},r_{C*})}K_1(B)\oplus K_1(C)\\
&\xrightarrow{d_1}K_1(D)
\xrightarrow{\gamma_1}K_0(P).
\end{aligned}
\tag{4.3}
\]

*Proof.* Naturality in the two extensions above says that the boundary for \(P\to C\) is \(\partial_i\psi_*\). We check three kinds of positions for each \(i=0,1\).

At \(K_i(P)\), a class \(a\) with \(r_{C*}a=0\) is \(k_*j\) for some \(j\in K_i(J)\). If also \(r_{B*}a=0\), then \(\iota_*j=0\) in \(K_i(B)\), so \(j=\partial_{i+1}t\) for \(t\in K_{i+1}(D)\). Hence \(a=\gamma_{i+1}t\). Conversely both coordinate maps kill \(\gamma_{i+1}\), by exactness in those extensions.

At \(K_i(B)\oplus K_i(C)\), suppose \(\phi_*b=\psi_*c\). Then \(\partial_i\psi_*c=0\), so \(c=r_{C*}a_0\) for some \(a_0\in K_i(P)\). The difference \(b-r_{B*}a_0\) is killed by \(\phi_*\), hence equals \(\iota_*j\). Replace \(a_0\) by \(a_0+k_*j\) to obtain both coordinates \((b,c)\). The opposite inclusion follows from \(\phi r_B=\psi r_C\).

At \(K_i(D)\), one has \(\gamma_i d_i(b,c)=0\): the \(\phi_*b\) term has zero boundary, and the \(\psi_*c\) term has boundary in the kernel of \(k_*\). Conversely \(\gamma_it=0\) implies that \(\partial_it\) is in the image of the boundary for \(P\to C\). Choose \(c\in K_i(C)\) with \(\partial_it=\partial_i\psi_*c\). Then \(t-\psi_*c\) has zero boundary and equals \(\phi_*b\) for some \(b\). Therefore \(t=d_i(b,-c)\).

This proves all six assertions. A morphism of pullback diagrams respecting the named surjective leg induces morphisms of these extensions; functoriality and boundary naturality prove naturality of (4.2) and (4.3). Only \(\phi\) needed to be surjective. \(\square\)

## 5. Relative triples and their normalization

For now let \(A\) be unital and \(J\subset A\) an ideal, with quotient \(\pi:A\to A/J\). A relative triple is

\[
\begin{gathered}
(p,q,v),\\
p,q\in M_n(A)\text{ projections},\\
v\in M_n(A/J),
\end{gathered}
\tag{5.1}
\]

with \(v^*v=\pi(p)\), \(vv^*=\pi(q)\). Thus \(v\) is a specified isomorphism between their quotient projective modules. Define \(R(A,J)\) by generators these triples, relations of norm-continuous homotopy and block addition, and the relation that a triple is zero if \(v\) has an actual partial-isometry lift \(w\) with \(w^*w=p\), \(ww^*=q\). Such triples are called degenerate. This is the projection formulation of \(K_0(A,J)\); the notation uses the ideal as its second entry.

A choice of matrix lifting \(v\) is immaterial: two such lifts have a straight interpolation with unchanged quotient. An isomorphism of projective modules can also be written using an invertible comparison matrix; its polar part on the source and range gives \(v\). In that notation the comparison means its restriction between the specified projective modules. Data on unused complementary free summands must be discarded explicitly. The relative relations above retain the specified module comparison, rather than just the kernel of \(K_0(A)\to K_0(A/J)\).

The negative of \((p,q,v)\) is \((q,p,v^*)\). To prove this, keep projections \(p\oplus q,q\oplus p\) fixed and interpolate their quotient comparison by

\[
\begin{gathered}
V_t=
\begin{pmatrix}
\cos t\,v&-\sin t\,\pi(q)\\
\sin t\,\pi(p)&\cos t\,v^*
\end{pmatrix},\\
0\leq t\leq\pi/2.
\end{gathered}
\tag{5.2}
\]

The relations for \(v\) show \(V_t^*V_t=\pi(p\oplus q)\) and \(V_tV_t^*=\pi(q\oplus p)\): the cross terms cancel using \(v\pi(p)=v=\pi(q)v\). At the last endpoint, \(V_t\) lifts to the actual partial isometry \(\left(\begin{smallmatrix}0&-q\\p&0\end{smallmatrix}\right)\). Its triple is degenerate. At the first endpoint it is the sum of the two stated triples, proving the assertion.

**Lemma 5.1 (finite reduction).** Every relative triple can be homotoped, after adding degenerate triples and zero blocks, to

\[
\begin{gathered}
(P,h,\pi(P)),\quad h-P\in M_N(J),\\
P=\operatorname{diag}(I_m,0_m).
\end{gathered}
\tag{5.3}
\]

*Proof.* In the quotient let \(a=v^*v\), \(b=vv^*\). The matrix

\[
W(v)=\begin{pmatrix}v&1-b\\a-1&v^*\end{pmatrix}
\tag{5.4}
\]

is unitary and sends \(\operatorname{diag}(a,0)\) to \(\operatorname{diag}(b,0)\) by conjugation. It lies in the identity component. Indeed

\[
\begin{gathered}
W_t(v)=\\
\begin{pmatrix}
tv&(1-t^2b)^{1/2}\\
-(1-t^2a)^{1/2}&tv^*
\end{pmatrix},\\
0\leq t\leq1,
\end{gathered}
\tag{5.5}
\]

is a unitary path from a scalar rotation to \(W(v)\). To check unitarity, note \(v f(a)=f(b)v\) for these functions: on the supports \(a,b\) both functions take the same value, while \(v\) vanishes off its initial support. The diagonal products are identity and the off-diagonal products cancel. The scalar rotation itself has the usual rotation path from identity.

An identity-starting quotient unitary path lifts to an identity-starting unitary path in \(A\). One proof divides it into small increments with norm distance from identity less than one, takes their self-adjoint logarithms, lifts these continuously, and exponentiates. Continuous self-adjoint logarithm lifts exist by Lesson 8, Lemma 1.2, applied to the real Banach-space quotient; that lemma's successive interpolation proof works over real scalars. Multiplying successive exponential lifts gives the full path. Thus choose a lift \(U\in M_{2n}(A)\) of (5.4), connected to identity.

Put \(p'=\operatorname{diag}(p,0)\), \(q'=\operatorname{diag}(q,0)\). The triple with these projections and \(\operatorname{diag}(v,0)\) equals the original plus a zero triple. Since
\(\pi(U)\pi(p')=\operatorname{diag}(v,0)\), a path from identity to \(U\) shows it is homotopic to
\((p',\bar q,\pi(p'))\), where \(\bar q=U^*q'U\). Explicitly, along a path \(U_t\) use
\((p',U_t^*q'U_t,\pi(U_t)^*\operatorname{diag}(v,0))\). Its endpoint is as stated and \(\pi(\bar q)=\pi(p')\).

Add the degenerate triple \((1-p',1-p',\pi(1-p'))\). Its first projection is now \(r=p'\oplus(1-p')\); its second is \(s=\bar q\oplus(1-p')\); its comparison is \(\pi(r)\). For \(c=\cos t,d=\sin t\), put \(C_t=p'+c(1-p')\), \(D_t=d(1-p')\). The unitary path

\[
L_t(p')=
\begin{pmatrix}
C_t&-D_t\\
D_t&C_t
\end{pmatrix}
\tag{5.6}
\]

starts at identity. Conjugate both projections and the comparison along this same path. At \(t=\pi/2\), writing \(L=L_{\pi/2}(p')\), one has \(LrL^*=P=\operatorname{diag}(I_{2n},0_{2n})\). Let \(h=LsL^*\). Since \(\pi(s)=\pi(r)\), \(\pi(h)=\pi(P)\); hence \(h-P\in M_{4n}(J)\). This proves (5.3). Every stabilization and path is finite. \(\square\)

## 6. Strong excision, including injectivity

An equal-scalar relative class over \(J^+\) gives a triple over \(A\):

\[
\begin{gathered}
\eta:K_0(J)\longrightarrow R(A,J),\\
[e]-[P]\longmapsto(e,P,\pi(P)).
\end{gathered}
\tag{6.1}
\]

Here matrices over \(J^+\) are sent by \(j+\lambda\mapsto j+\lambda1_A\). We do not assume this map embeds the external unitization when \(J\) is unital.

For completeness, (6.1) respects the normal-form relations. Additions are block sums; adding a scalar projection to both terms adds a degenerate triple. If two differences agree, identity stabilization and zero padding, as proved in Lessons 1 and 3, give a projection homotopy between their numerators after the scalar denominators have been made the same projection. Its scalar projection path can be made constant: transport it by scalar unitaries starting at identity, using the close-projection transports of Lesson 1 on a finite subdivision. Conjugate the lifted path by these unitaries. At the last endpoint the transport commutes with the fixed scalar projection. Its stabilizer is \(U(k)\times U(N-k)\), which is connected by diagonalization of scalar unitaries and paths of their eigenvalue angles. A path in that stabilizer restores the required final numerator. The resulting path has the fixed scalar comparison throughout, so it is a homotopy of triples. This proves well-definedness and additivity of \(\eta\).

**Theorem 6.1 (strong excision).** The map (6.1) is an isomorphism. Consequently the canonical map

\[
K_0(J^+,J)\xrightarrow{\cong}K_0(A,J)
\tag{6.2}
\]

is an isomorphism. For nonunital ambient \(A\), interpret the right side through \(A^+\), with ideal \(J\).

*Proof.* Apply the explicit reduction of Lemma 5.1 to a triple \(T=(p,q,v)\), and define

\[
\kappa(T)=[P]-[h]\in K_0(J).
\tag{6.3}
\]

In (6.3), \(h=P+j\) is regarded as the projection \(P+j\) over the external \(J^+\). Its projection equation in \(A\) is exactly an equation in \(J\), since its scalar part is already a projection. Therefore it remains a projection over \(J^+\), including when \(J=A\).

We verify every choice and defining relation. The only choice in the explicit formulas is \(U\), the lift of \(W(v)\). For two such choices \(U_0,U_1\), put \(V=U_1^*U_0\). Then \(V-I\in M_{2n}(J)\) and
\(\bar q_1=V\bar q_0V^*\). Hence their \(h\)'s are conjugate by

\[
L\operatorname{diag}(V,I_{2n})L^*,
\tag{6.4}
\]

a unitary whose difference from identity lies in \(M_{4n}(J)\). Their classes in \(K_0(J^+)\) agree, proving lift independence.

For a homotopy of triples, apply the same lifting argument to the quotient of \(C([0,1],A)\) by \(C([0,1],J)\). This quotient is onto by Lesson 8, Lemma 1.2, and is \(C([0,1],A/J)\). Thus the lifts \(U\) can be chosen continuously in the homotopy parameter. Formula (5.6) is continuous in \(p'\), and produces a continuous path \(h\) with fixed scalar \(P\). Hence \(\kappa\) respects homotopy.

If the triple is degenerate with partial-isometry lift \(w\), choose \(U=W(w)\). The same path (5.5) in \(A\) makes this an admissible lift. Then \(U^*q'U=p'\), so \(s=r\), \(h=P\), and \(\kappa(T)=0\). For block sums, choose the block sum of the lifts after rearranging coordinates. The constructions of \(r,s,L,h\) are block sums after the same scalar permutation. Thus \(\kappa\) is additive. It descends to a homomorphism \(R(A,J)\to K_0(J)\).

For a triple coming from \(J^+\), its quotient comparison before mapping to \(A\) is a scalar partial isometry. Choose \(U\) to be its scalar completion (5.4); all the other constructions can then be performed in \(J^+\). In that algebra,

\[
[P]-[h]=[r]-[s]=[p']-[\bar q]=[p]-[q].
\tag{6.5}
\]

The first equality uses conjugation by \(L\); the last uses conjugation by \(U\). In particular \(\kappa\eta\) is identity on the normal form \([e]-[P]\), hence on all of \(K_0(J)\).

Conversely Lemma 5.1 makes \(T\) equal to the triple \((P,h,\pi(P))\). Since \([P]-[h]=-([h]-[P])\), (6.1) and the inverse calculation (5.2) give
\(\eta\kappa(T)=(P,h,\pi(P))=T\). This proves the other composition is identity, proving both surjectivity and injectivity.

Apply the same result to the ambient algebra \(J^+\) itself: \(R(J^+,J)\cong K_0(J)\). Its subsequent map to \(R(A,J)\) is precisely (6.1), which proves (6.2). All constructions apply in \(A^+\) if \(A\) is nonunital. They are natural for unital morphisms of pairs, and for arbitrary morphisms after external unitization. \(\square\)

This completes the relative excision statement deferred in [Lesson 4, §7](KT-OPK-04.md#7-relative-terminology-and-two-failures-of-short-exactness). The specified quotient comparison has survived the proof; it has not been replaced by a bare kernel assertion.

**Corollary 6.2 (Banach-algebra version).** Strong excision also holds for complex Banach algebras and closed ideals, using idempotents and isomorphisms of projective modules.

*Proof.* Here a comparison is a pair \((v,w)\) in the quotient satisfying
\(wv=\pi(p)\), \(vw=\pi(q)\), \(v=\pi(q)v\pi(p)\), and \(w=\pi(p)w\pi(q)\). Degeneracy means that both maps lift to inverse isomorphisms between the projective modules over the ambient algebra. Replace adjoints throughout the preceding proof by inverse matrices, and use \(w\) wherever \(v^*\) occurred. We give the matrix checks needed for this replacement.

Write \(a=wv,b=vw\), and for \(0\leq t\leq1\) put
\(c=\sqrt{1-t^2}\), \(X=1-b+cb\), \(Y=1-a+ca\). Then

\[
\begin{gathered}
\begin{pmatrix}tv&X\\-Y&tw\end{pmatrix}^{-1}=\\
\begin{pmatrix}tw&-Y\\X&tv\end{pmatrix}.
\end{gathered}
\tag{6.6}
\]

Indeed \(vY=Xv\), \(wX=Yw\), \(t^2b+X^2=1\), and \(t^2a+Y^2=1\), proving both products are identity. This is an invertible path from the scalar rotation to the completion (5.4), now with lower-right entry \(w\). Its endpoint sends \(\operatorname{diag}(a,0)\) to \(\operatorname{diag}(b,0)\), by the support equations. It lifts to an identity-starting invertible path: divide into small increments, take their convergent logarithms, lift them continuously by the Banach-space lifting lemma, and exponentiate. No positive square root in the algebra is used in (6.6).

The matrix \(L_t(p')\) of (5.6) has inverse \(L_{-t}(p')\) for any idempotent \(p'\); direct multiplication uses \(p'(1-p')=0\). It still sends \(p'\oplus(1-p')\) to the scalar idempotent \(P\) at \(t=\pi/2\). Thus define \(\bar q=U^{-1}q'U\), \(h=L(\bar q\oplus(1-p'))L^{-1}\), and \(\kappa=[P]-[h]\). For two choices, \(V=U_1^{-1}U_0\) is invertible with \(V-I\in J\), and the two \(h\)'s are conjugate by \(L\operatorname{diag}(V,I)L^{-1}\) over \(J^+\). Homotopy and block-sum arguments are identical, using the quotient of continuous Banach-valued paths. For a degenerate triple, the completion of its actual inverse maps makes \(\bar q=p'\), so \(h=P\).

The inverse-triple rotation (5.2), with \(w\) replacing \(v^*\), has inverse between the indicated projective modules
\(\left(\begin{smallmatrix}\cos t\,w&\sin t\,\pi(p)\\-\sin t\,\pi(q)&\cos t\,v\end{smallmatrix}\right)\); their products are the source and target idempotents. Its final maps lift, so it proves the inverse relation. The normal-form homotopy in (6.1) uses scalar invertible transports and the connected stabilizer \(GL_k(\mathbb C)\times GL_{N-k}(\mathbb C)\), instead of unitaries. Those groups are connected by scalar polar decomposition and unitary eigenvalue paths. Finally (6.5) uses similarity, which preserves stable idempotent classes. Thus both compositions are identity just as before. External unitization handles a nonunital ambient algebra. \(\square\)

## 7. Exercises with complete solutions

**Exercise 11.1 — The two endpoint ranks (basic).** Compute every arrow for (3.1), and explain its sign.

*Solution.* Contractibility gives \(K_0(C[0,1])=\mathbb Z\), \(K_1(C[0,1])=0\). The circle-winding computation gives \(K_0(C_0((0,1)))=0\), \(K_1(C_0((0,1)))=\mathbb Z[\omega]\). The quotient has \(K_0=\mathbb Z^2\), \(K_1=0\). The ideal-to-middle \(K_0\)-map is zero, the quotient rank map is \(k\mapsto(k,k)\), and the exponential is \((a,b)\mapsto(b-a)[\omega]\), since the two coordinate projections have the lifts \(1-t\) and \(t\). The ideal-to-middle \(K_1\)-map, the middle-to-quotient \(K_1\)-map, and the index boundary all have zero source or target and are zero. The diagonal is exactly the exponential kernel; the difference is onto. The other four exactness positions involve zero groups or the injective diagonal. Reversing the interval coordinate replaces \([\omega]\) by its negative and accordingly reverses the displayed difference sign.

**Exercise 11.2 — Lift independence and the suspended sign (intermediate).** For a quotient projection in (1.3), prove the exponential formula with the prescribed suspension conventions, and check a continuous family of lifts.

*Solution.* For a family \(x_r=x_r^*\) of lifts of \(e\) with scalar \(P\), functional calculus is norm continuous, and \(\pi^+e^{2\pi ix_r}=I=\epsilon_Ae^{2\pi ix_r}\). Thus \(e^{2\pi ix_r}\) is a continuous family over \(J^+\). Any two lifts have such a family by convex interpolation. To identify the boundary, set \(G(s)=e^{2\pi isx}e^{-2\pi isP}\), choose the doubled path \(U\) for \(u=e^{2\pi ix}\), and use \(Z=\operatorname{diag}(G,G^*)U^*\). It starts and ends at identity and lifts \(\operatorname{diag}(g,g^*)\). The boundary is its conjugated projection minus \(Q\). Formula (1.8) is a homotopy over \((SJ)^+\) to \(U^*QU\), with both endpoints \(Q\), because every \(D(rs)\) is block diagonal. That projection loop represents \(\theta_J[u^*]=-\theta_J[u]\). Consequently (1.2) gives \([u]\), rather than \([u^*]\). Representative and block-sum relations follow from the already defined homomorphism (1.2); lift independence alone would not suffice to establish them.

**Exercise 11.3 — A single surjective restriction (intermediate).** Derive (4.3) when only \(\phi\) is surjective, including its connecting maps.

*Solution.* Let \(J=\ker\phi\). The pullback projection onto \(C\) is onto and has kernel \(J\), yielding a morphism of extensions to \(B\to D\). Therefore its boundary is \(\partial_i\psi_*\). Define \(\gamma_i=k_*\partial_i\), \(d_i=\phi_*-\psi_*\), exactly as in (4.2). If both coordinates of \(a\in K_i(P)\) vanish, first write \(a=k_*j\), then \(j=\partial_{i+1}t\), proving \(a=\gamma_{i+1}t\). If \(d_i(b,c)=0\), lift \(c\) to \(a_0\) using its zero boundary, and correct the first coordinate by \(k_*j\) since \(b-r_{B*}a_0\in\operatorname{im}\iota_*\). If \(\gamma_it=0\), lift \(\partial_it\) through the pullback boundary as \(\partial_i\psi_*c\), then write \(t-\psi_*c=\phi_*b\), so \(t=d_i(b,-c)\). These are all three kinds of exactness positions for both parities. Zero composites follow from the two extension cycles. Boundary naturality gives naturality of the result. At no step is a lift under \(\psi\) required.

**Exercise 11.4 — What a projection lift proves (intermediate).** Show that an actual projection lift makes the exponential boundary zero. State exactly the converse supplied by the six-term sequence.

*Solution.* If \(x^2=x=x^*\) lifts \(e\) with scalar \(P\), then functional calculus gives \(e^{2\pi ix}=I\), so (1.4) is the identity unitary's zero K-class. For a relative class \(a\in K_0(B)\), the converse is \(\varepsilon_Ea=0\) if and only if \(a=\pi_*b\) for some \(b\in K_0(A)\). A representative of \(b\) may use a difference of projections and stabilization. Neither exactness nor the vanishing of a homotopy class identifies an actual projection lift of a particular prescribed matrix \(e\). The same qualification applies to the index boundary's obstruction for a prescribed quotient unitary.

**Exercise 11.5 — The sphere and the disc quotient (advanced).** Compute the sphere groups using the split extension by the plane, then compute the disc quotient and compare generators with Lesson 10.

*Solution.* Evaluation at infinity has the constant section in
\(0\to C_0(\mathbb R^2)\to C(S^2)\to\mathbb C\to0\). Split exactness, Bott periodicity and \(K_1(\mathbb C)=0\) give

\[
\begin{aligned}
K_0(C(S^2))&=\mathbb Z[1]\oplus\mathbb Z\mathfrak b,\\
K_1(C(S^2))&=0.
\end{aligned}
\tag{7.1}
\]

The quotient on \(K_0\) is rank and sends these two generators to \(1,0\); the ideal inclusion sends \(\mathfrak b\) to the same reduced sphere class. Both boundaries are zero because the extension splits. If \(q\) is the rank-one projection of Lesson 10, \(\mathfrak b=[q]-[1]\); hence \([1],[q]\) is also an integral basis, by the unimodular change \([q]=[1]+\mathfrak b\).

For the disc one must specify the ideal: extend functions from the open disc by zero on its boundary, identifying \(C_0(\mathbb R^2)\) with \(C_0(\mathbb D)\) through \(\rho\). The quotient \(C(\overline{\mathbb D})/C_0(\mathbb D)\) is \(C(\mathbb T)\): restriction is onto, for example by multiplying a radial extension of a boundary function by a continuous cutoff vanishing near the origin, and its kernel is exactly this ideal. The cycle has ideal \(K_0=\mathbb Z\mathfrak b\), middle \(K_0=\mathbb Z\), zero ideal and middle \(K_1\), zero ideal inclusion, and rank quotient isomorphism. Exactness gives quotient \(K_0=\mathbb Z\) and quotient \(K_1=\mathbb Z\), with boundary an isomorphism onto the ideal generator. Formula (3.7), pulled back by \(\rho\), fixes it as \([z]\mapsto\mathfrak b\). All remaining maps are zero as listed in Example 3.3. These groups and the same positive Bott projection agree with Lesson 10's direct rank-and-clutching computation.

## What this lesson imports and does not prove

The projection normal form, stabilized projection equivalence and homotopy invariance are the proved results of Lessons 1, 3 and 4. The index construction and its four exactness positions are Lesson 7; continuous lifting, suspension and its explicit doubled path are Lesson 8. The circle groups and Toeplitz index are Lessons 6 and 9. General Bott periodicity and the oriented plane generator are Lesson 10. We use these exact prerequisites and do not reprove them. The remaining two exactness positions, positive exponential formula, one-leg Mayer–Vietoris sequence, and both directions of strong excision are proved here. No index theorem for general elliptic operators is asserted.

## References

- S. Richard, *K-theory for C*-algebras, and beyond*, Spring 2015, Lemma 6.2.1, p. 55. [Author notes](https://www.math.nagoya-u.ac.jp/~richard/teaching/s2015/Kth.pdf). Corollary 2.4 proves its zero-stabilized lift at every matrix size, using the exact norm lift proved here.

- S. Richard, *K-theory for C*-algebras*, Spring 2015, Sections 2.2–2.3, especially Proposition 2.3.1, pp. 23–24. [Freely accessible author notes](https://www.math.nagoya-u.ac.jp/~richard/teaching/s2015/Kth.pdf). Proposition 2.3 supplies exact norm lifts at every matrix level and full projection, unitary and normal-element counterexamples.
- B. Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §5.4, especially Theorem 5.4.2, printed pp. 29–30; Theorem 9.3.1 and §9.3.2, printed pp. 67–68; §21.2, printed pp. 219–220. The relative comparison and the Mayer–Vietoris difference are given explicit proofs above. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§8.4–8.6, printed pp. 325–348: relative triples, connecting maps, the disc and Toeplitz computations. Our displayed matrices specify the supports and signs independently of notation choices.

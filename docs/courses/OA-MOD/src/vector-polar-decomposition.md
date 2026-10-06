# The modulus and phase of a vector

In a standard form, every Hilbert-space vector has a canonical positive modulus and an algebra-valued phase. The modulus is determined by how the vector represents the commutant. Equality of those commutant functionals then constructs the phase as an isometry between two cyclic subspaces. This also identifies exactly which support projections are necessary for uniqueness.

Let \((M,H,J,P)\) be any standard form, with inner products linear in the first variable. SE01 specifies its axioms. SE11 proves that every bounded normal positive functional has a unique representative in its positive cone. The Hilbert-space projection and extension arguments are proved in BK01, and BK02 proves the bicommutant identity. Vector functionals belong to the concrete predual by CP06. No countability or faithfulness assumption is made.

The mathematical source comparison is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercises IX.1(2)–(3). We give all the cyclic-space, support and conjugation arguments explicitly, using the complete earlier proofs linked above.

## The commutant sees the same positive cone

For \(a,b\in M\) and \(h\in H\), define

\[
 \begin{gathered}
 h^*=Jh,\\
 hb=Jb^*Jh.
 \end{gathered}
 \tag{VP.1}
\]

We write \(ahb=a(Jb^*J)h\). Right multiplication is complex-linear in both \(h\) and \(b\): conjugation of the scalar in \(b^*\) is canceled by the outer \(J\). If \(R_b=Jb^*J\), then \(R_cR_b=R_{bc}\), so \((hb)c=h(bc)\). Every \(R_b\in M'\) commutes with left multiplication. These calculations justify the displayed products without interpreting a vector as an algebra element.

The quadruple \((M',H,J,P)\) is also a standard form. Indeed \(JM'J=M\), and \((M')'=M\) by BK02. The two centers coincide, since both are \(M\cap M'\); hence the central axiom is unchanged. Self-duality and pointwise \(J\)-fixedness of \(P\) are unchanged as well. Finally write \(y'=JaJ\in M'\). The commuting left and right factors give

\[
 y'Jy'J=(JaJ)a=aJaJ.
\]

The last operator preserves \(P\) by the original standard-form axiom. This verifies every required axiom for the commutant form, so SE11 applies to it.

For any vector \(h\), let \(s(h)\in M\) be the orthogonal projection onto \(\overline{M'h}\). This subspace is invariant under \(M'\) and its adjoints, so its projection commutes with \(M'\) and belongs to \(M\). It is exactly the smallest projection in \(M\) fixing \(h\): if \(eh=h\), commutation implies that \(e\) fixes all of \(M'h\) and its closure. Thus \(s(h)\) is the support of \(\omega_h|_M\). The same reasoning in the commutant gives its support projection onto \(\overline{Mh}\). These arguments include \(h=0\), with zero projection.

## Constructing the phase from a cyclic isometry

**Theorem.** For every \(\xi\in H\) there are a positive vector \(\eta\in P\) and a partial isometry \(u\in M\) such that

\[
 \begin{gathered}
 \xi=u\eta,\\
 u^*u=s(\eta),\\
 uu^*=s(\xi).
 \end{gathered}
 \tag{VP.2}
\]

A partial isometry acts isometrically on the range of its initial projection and vanishes on its orthogonal complement.

**Proof.** On \(M'\), define the normal positive functional

\[
 \theta(y')=\langle y'\xi,\xi\rangle.
\]

Its boundedness and positivity follow directly from the inner product, and its normality is CP06's vector-functional description of the predual. By VP01 and SE11 there is a unique \(\eta\in P\) representing \(\theta\). Evaluation at the identity gives \(\|\eta\|=\|\xi\|\). For each \(y'\in M'\),

\[
 \begin{gathered}
 \|y'\eta\|^2=\theta(y'^*y')\\
 =\|y'\xi\|^2.
 \end{gathered}
 \tag{VP.3}
\]

Thus the linear rule \(y'\eta\mapsto y'\xi\) is well defined and isometric: apply VP.3 also to the difference of any two representatives. BK01's bounded-extension argument extends it uniquely to an isometry

\[
 V:\overline{M'\eta}\longrightarrow\overline{M'\xi}.
\]

Its range is closed, since the domain is complete and the map is isometric, and contains the dense set \(M'\xi\). It is therefore onto.

Put \(p=s(\eta)\), \(q=s(\xi)\), and extend \(V\) by zero on \((1-p)H\). Call this bounded operator \(u\). It is a partial isometry with \(u^*u=p\) and \(uu^*=q\); for example, \(u^*\) is \(V^{-1}\) on \(qH\) and zero on its orthogonal complement, which verifies both identities. Since the identity belongs to \(M'\), the defining rule gives \(u\eta=\xi\).

It remains to prove membership in \(M\). For \(z',y'\in M'\), the rule gives

\[
 \begin{aligned}
 u z'(y'\eta)&=z'y'\xi\\
 &=z'u(y'\eta).
 \end{aligned}
\]

Continuity proves commutation on \(pH\). The projection \(p\in M\) commutes with \(z'\), so \((1-p)H\) is also invariant under \(z'\); both sides vanish there. Hence \(u\in(M')'=M\). This completes the construction. If \(\xi=0\), uniqueness of the cone representative gives \(\eta=0\), both cyclic spaces are zero, and the construction gives \(u=0\). \(\square\)

## Why the support normalization gives uniqueness

Suppose \(\xi=v\zeta\), with \(\zeta\in P\), \(v\in M\) a partial isometry, and \(v^*v=s(\zeta)\). For \(y'\in M'\), commutation and the identity \(v^*v\zeta=\zeta\) give

\[
 \begin{gathered}
 \langle y'\xi,\xi\rangle\\
 =\langle v^*y'v\zeta,\zeta\rangle\\
 =\langle y'\zeta,\zeta\rangle.
 \end{gathered}
\]

Thus \(\zeta\) represents the same commutant functional as \(\eta\), and uniqueness in SE11 gives \(\zeta=\eta\). Also

\[
 v(y'\eta)=y'\xi=u(y'\eta).
\]

The two operators agree on the dense subspace \(M'\eta\) of \(pH\), and both vanish on \((1-p)H\), because their initial projection is \(p\). Hence \(v=u\). In particular the initial support condition already forces the final support condition: the range is the closure of \(uM'\eta=M'\xi\).

We write \(|\xi|=\eta\) and call \(u\) its phase. Equality of the commutant vector functionals is the intrinsic characterization of \(|\xi|\). For \(c\ne0\), direct verification and uniqueness give

\[
 \begin{gathered}
 |c\xi|=|c|\,|\xi|,\\
 u_{c\xi}=(c/|c|)u_\xi.
 \end{gathered}
 \tag{VP.4}
\]

Indeed the displayed positive vector and partial isometry multiply to \(c\xi\), with the same supports as before. At \(c=0\), both the modulus and the phase are zero; no division is used. Similarly, if \(w\in M\) is unitary, then \(|w\xi|=|\xi|\) and its phase is \(wu\): the commutant functional is unchanged, and \((wu)^*(wu)=p\).

## Conjugation exchanges the two support projections

Let \(\xi=u\eta\) be VP.2, with \(\eta=|\xi|\), \(p=u^*u\), \(q=uu^*\). Then

\[
 \begin{gathered}
 |\xi^*|=u\eta u^*,\\
 \xi^*=u^*|\xi^*|,\\
 u\eta=|\xi^*|u.
 \end{gathered}
 \tag{VP.5}
\]

The middle line is the normalized polar decomposition of \(\xi^*\): its initial projection is \(q\), and its final projection is \(p\).

**Proof.** Since \(J\eta=\eta\) and \(p\eta=\eta\), also \(JpJ\eta=\eta\). Set \(r=JuJ\in M'\) and

\[
 \kappa=u r\eta=r\xi.
\]

The cone axiom gives \(\kappa=uJuJ\eta\in P\). Also \(r^*r=JpJ\). This projection commutes with \(u\) and fixes \(\eta\), hence fixes \(\xi=u\eta\). Consequently

\[
 r^*\kappa=r^*r\xi=\xi.
\]

Both \(r,r^*\) belong to \(M'\), so these two identities imply

\[
 \overline{M'\kappa}=\overline{M'\xi}.
\]

Therefore \(s(\kappa)=q\), including the case of a zero vector.

Next, using commutation of \(r\) with \(p\),

\[
 \begin{aligned}
 u^*\kappa&=p r\eta=r\eta\\
 &=J(u\eta)=\xi^*.
 \end{aligned}
\]

The partial isometry \(u^*\) has initial projection \(q=s(\kappa)\). VP03's uniqueness therefore identifies \(\kappa=|\xi^*|\) and the phase as \(u^*\); its final support is \(s(\xi^*)=p\). Thus the support exchange is part of the proved normalized decomposition, rather than an extra assumption about conjugation.

Finally, the right action in VP.1 gives

\[
 \begin{gathered}
 \kappa u=Ju^*J\kappa\\
 =r^*\kappa=\xi=u\eta.
 \end{gathered}
\]

This proves all three identities in VP.5. The notation \(u\eta u^*\) means precisely \(uJuJ\eta\), so every product in that formula has a specified Hilbert-space meaning. \(\square\)

## Rank-one phases and the necessity of the initial support

The standard Hilbert–Schmidt form of \(M_2(\mathbb C)\) is established in SF14. Here left multiplication is the represented algebra, \(JX=X^*\), the cone consists of positive matrices, and the right action in VP.1 is ordinary matrix multiplication. Matrix units satisfy \(E_{ij}E_{kl}=\delta_{jk}E_{il}\).

For the vector \(\xi=2E_{12}\), its decomposition is

\[
 \begin{gathered}
 |\xi|=2E_{22},\\
 u=E_{12},\\
 p=E_{22},\\
 q=E_{11}.
 \end{gathered}
 \tag{VP.6}
\]

The products are immediate from the matrix-unit rule. For the support check, the right multiples of \(E_{22}\) are exactly the matrices supported on their second row, so their Hilbert-space projection is left multiplication by \(E_{22}\). The right multiples of \(E_{12}\) are exactly the matrices supported on their first row, giving left multiplication by \(E_{11}\). Thus both cyclic-support requirements hold, and VP03 proves that these are the canonical modulus and phase.

Conjugation gives \(\xi^*=2E_{21}\), whose modulus is \(2E_{11}\) and whose phase is \(E_{21}\). In particular

\[
 \begin{gathered}
 E_{12}(2E_{22})E_{21}=2E_{11},\\
 (2E_{11})E_{12}=2E_{12}.
 \end{gathered}
\]

These computations check both the support exchange and the direction of the right multiplication in VP.5.

If the initial support condition is discarded, even the phase need not be unique. For \(\xi=E_{11}\) and \(\eta=E_{11}\), both \(E_{11}\eta=\xi\) and \(I\eta=\xi\), and both left factors are partial isometries. Only the first has initial projection \(s(\eta)=E_{11}\). The modulus can also become ambiguous: \(E_{11}I=\xi\) has a positive second factor, but its support is \(I\), larger than the phase's initial projection. These examples show why positivity and the product identity alone are insufficient.

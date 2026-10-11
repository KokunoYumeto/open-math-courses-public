# Vector implementation and spatiality

A conjugation that exchanges a von Neumann algebra with its commutant and acts by adjoint on the center controls the size of the representation. In a sigma-finite algebra it produces a cyclic separating vector. Without any countability assumption, every normal positive functional is still a vector functional, every complex normal functional is a vector coefficient, and every star isomorphism between two such represented algebras is spatial.

Let \(M\subseteq B(H)\) act unitally, with inner products linear in the first variable. A conjugation in this lesson is an antiunitary involution \(J\) satisfying
\[
 \begin{gathered}
 JMJ=M',\\
 JaJ=a^*,\\
 a\in Z(M).
 \end{gathered}
 \tag{VI.1}
\]
These are precisely the hypotheses of SJ01; no positive cone is prescribed. We use the two support projections from SJ02: \(e_\xi\in M\) projects onto \([M'\xi]\), and \(e'_\xi\in M'\) onto \([M\xi]\). Thus \(e_\xi=1\) means that \(\xi\) is separating for \(M\), and \(e'_\xi=1\) means it is cyclic. Sigma-finiteness means that every orthogonal family of nonzero projections is countable; CY02–03 proves its equivalence with existence of a faithful normal positive functional.

## From sigma-finiteness to a cyclic separating vector

We first combine two elementary support arguments. The comparison transfer, SJ03, gives
\[
 \begin{gathered}
 e_\xi\precsim e_\eta\text{ in }M\\
 \Longleftrightarrow\\
 e'_\xi\precsim e'_\eta\text{ in }M'.
 \end{gathered}
 \tag{VI.2}
\]
If \(\alpha\) is cyclic and \(\beta\) is separating, then \(e_\alpha\leq e_\beta=1\), so \(1=e'_\alpha\precsim e'_\beta\leq1\). The projection cancellation argument, PE07, gives \(e'_\beta\sim1\). Choose \(u\in M'\) with \(u^*u=e'_\beta\), \(uu^*=1\), and put \(\gamma=u\beta\). Commutation gives \([M\gamma]=u[M\beta]=H\). Moreover \(\gamma=u\beta\) and \(\beta=u^*\gamma\) imply \([M'\gamma]=[M'\beta]=H\). Thus a cyclic vector and a separating vector, even when initially different, yield one vector with both properties.

Now assume that \(M\) is sigma-finite. Choose a maximal family of nonzero vectors \((\xi_i)\) for which both families \((e_{\xi_i})\) and \((e'_{\xi_i})\) are orthogonal. Such a family exists by the union-of-chains argument. It is countable by sigma-finiteness of \(M\). Rescale its vectors, without changing either support, so that \(\sum_i\|\xi_i\|^2<\infty\), and put
\[
 \begin{gathered}
 \xi=\sum_i\xi_i,\\
 e=\sum_i e_{\xi_i},\qquad
 f=\sum_i e'_{\xi_i}.
 \end{gathered}
\]
The vector sum converges because the vectors are orthogonal. The projection sums are strong orthogonal sums. We have \(e\xi=f\xi=\xi\), while \(e_{\xi_i}\xi=e'_{\xi_i}\xi=\xi_i\). Applying the first projection from \(M\) and the second from \(M'\) shows respectively that every \([M\xi_i]\) lies in \([M\xi]\), and every \([M'\xi_i]\) lies in \([M'\xi]\). Consequently
\[
 e_\xi=e,\qquad e'_\xi=f.
 \tag{VI.3}
\]
The commuting projections \(1-e\) and \(1-f\) have zero product. Otherwise a nonzero vector in the intersection of their ranges could be added to the family, by the least-support characterization of SJ02.

Let \(z=c_M(1-e)\) be the central carrier. The projection onto \([M(1-e)H]\) is this central carrier: the subspace reduces both \(M\) and \(M'\), contains \((1-e)H\), and is contained in the range of every central projection dominating \(1-e\). Since \(1-f\in M'\) annihilates \((1-e)H\), it annihilates this whole subspace. Thus \(z(1-f)=0\), so \(z\leq f\); also \(1-z\leq e\). The central-cut formulas in SJ02 imply that \(z\xi\) is cyclic for \(Mz\) on \(zH\), and \((1-z)\xi\) is separating for \(M(1-z)\) on \((1-z)H\).

The conjugation commutes with \(z\). It takes a cyclic vector on a central summand to a separating vector there, and conversely, since
\[
 Je_\eta J=e'_{J\eta},\qquad
 Je'_\eta J=e_{J\eta}.
\]
Each of the two summands therefore has both kinds of vector. The first paragraph supplies a cyclic separating vector on each nonzero summand. Their sum is cyclic and separating on \(H\). This proves the sigma-finite assertion, including a zero summand or the zero Hilbert space.

## Putting a positive functional into one cyclic subspace

For an arbitrary concrete von Neumann algebra and \(\xi_0\in H\), a positive normal functional \(\varphi\) can be represented by a vector \(\eta\in[M\xi_0]\) exactly when
\[
 s(\varphi)\precsim e_{\xi_0}\quad\text{in }M.
 \tag{VI.4}
\]
Necessity follows from \(s(\varphi)=e_\eta\) and SJ03. We prove sufficiency, including the countable vector construction it needs.

The concrete predual argument CP08 supplies a positive normal functional
\[
 \theta(x)=\sum_n\langle x\zeta_n,\zeta_n\rangle
\]
with \(\sum_n\|\zeta_n\|^2<\infty\) and \(0\leq\varphi\leq\theta\). On \(\widetilde H=H\otimes\ell^2(\mathbb N)\), set \(A=M\otimes1\) and \(\zeta=\sum_n\zeta_n\otimes\delta_n\). This is a von Neumann algebra: the matrix commutant test AR03 identifies its commutant, and applying the same matrix-unit test again gives its bicommutant. The map \(x\mapsto x\otimes1\) is a normal star isomorphism onto \(A\), as bounded increasing nets converge strongly on finite-coordinate vectors and then on all vectors; compression to one coordinate proves normality of its inverse.

On the dense subspace \(A\zeta\) of \([A\zeta]\), define
\[
 b((x\otimes1)\zeta,(y\otimes1)\zeta)
       =\varphi(y^*x).
\]
Positivity, Cauchy–Schwarz and domination give
\[
 0\leq b(v,v)\leq\|v\|^2.
\]
They also show that the form is well defined when a vector has two presentations. The bounded form representation proved in BK01 supplies a positive contraction \(h\) on \([A\zeta]\) with \(b(v,w)=\langle hv,w\rangle\). The identity \(b(av,w)=b(v,a^*w)\), first on the dense subspace, says that \(h\) commutes with the restricted algebra. Extend \(h\) by zero on the orthogonal complement; the cyclic subspace reduces \(A\), so this extension lies in \(A'\). Its square root also commutes with \(A\), by bounded functional calculus. Therefore \(\rho=h^{1/2}\zeta\) satisfies
\[
 \langle(x\otimes1)\rho,\rho\rangle=\varphi(x).
 \tag{VI.5}
\]

The support of this vector functional in \(A\) is \(s(\varphi)\otimes1\), by the least-projection characterization of CP12. Set \(\rho_0=\xi_0\otimes\delta_1\). The least projection in \(A\) fixing it is \(e_{\xi_0}\otimes1\). Thus (VI.4), transported into \(A\), and (VI.2) in \(A\), give a partial isometry \(v\in A'\) with initial projection onto \([A\rho]\) and final projection dominated by the projection onto
\[
 [A\rho_0]=[M\xi_0]\otimes\mathbb C\delta_1.
\]
Write \(v\rho=\eta\otimes\delta_1\) with \(\eta\in[M\xi_0]\). Since \(v\) commutes with \(A\) and \(v^*v\rho=\rho\), it preserves the vector functional in (VI.5). Hence \(\varphi=\omega_\eta\), proving (VI.4). In particular, a separating vector \(\xi_0\) has \(e_{\xi_0}=1\), so every normal positive functional is represented by a vector in its cyclic subspace. No positive extension to \(B(H)\) was assumed.

## Vector implementation without sigma-finiteness

Assume (VI.1), and let \(\varphi\in M_*^+\). The zero functional is represented by zero. Otherwise put
\[
 \begin{gathered}
 e=s(\varphi),\qquad f=JeJ,\\
 K=efH,\qquad N=(eMe)|_K.
 \end{gathered}
\]
The compression identity in CP12 says \(\varphi(x)=\varphi(exe)\), and \(\varphi\) is faithful on \(eMe\). Thus that corner is sigma-finite by CY02–03.

The bounded corner-commutant proof SE02 uses only the two commuting projections and the algebra-exchange identity, not a cone. Applied here, it gives
\[
 \begin{gathered}
 N'=(fM'f)|_K,\\
 J_KNJ_K=N',\\
 J_K=J|_K.
 \end{gathered}
 \tag{VI.6}
\]
It also proves \(N=N''\). The restriction of \(eMe\) is faithful. Indeed \(c_{M'}(f)=c_M(e)\), since conjugation fixes central projections and carries their domination relations to each other. If \(x\in eMe\) vanishes on \(K\), then \(xf=0\). As \(x\) commutes with \(M'\), it vanishes on \([M'fH]=c_{M'}(f)H\); since \(x=xc_M(e)\), we get \(x=0\).

Every star isomorphism between von Neumann algebras is normal: it and its inverse are positive order isomorphisms, hence preserve bounded increasing suprema; NP06 identifies this with ultraweak continuity. Consequently the faithful corner identification carries \(\varphi|_{eMe}\) to a normal faithful functional on \(N\), and \(N\) is sigma-finite.

The corner-center theorem, EC05, identifies \(Z(eMe)\) with the elements \(ze\), for \(z\in Z(M)c(e)\). On \(K\), the conjugation sends the restriction of \(ze\) to that of \(z^*e\), because \(JefJ=ef\). Thus \(J_K\) satisfies the central adjoint condition as well. VI01 gives a cyclic separating vector for \(N\); VI02 now represents the transported functional by some \(\xi\in K\). Since \(e\xi=\xi\),
\[
 \begin{aligned}
 \varphi(x)&=\varphi(exe)\\
 &=\langle exe\xi,\xi\rangle\\
 &=\langle x\xi,\xi\rangle.
 \end{aligned}
 \tag{VI.7}
\]
This proves vector implementation on the original Hilbert space for every positive normal functional, with \(\|\xi\|^2=\varphi(1)\).

For a complex normal functional, the polar decomposition NF02 has convention \(\varphi(x)=\psi(xv)\), where \(\psi\geq0\), \(v^*v=s(\psi)\), and \(\psi(1)=\|\varphi\|\). Represent \(\psi=\omega_\xi\) by the result just proved. Its support fixes \(\xi\), so
\[
 \begin{gathered}
 \varphi(x)=\langle xv\xi,\xi\rangle,\\
 \|v\xi\|=\|\xi\|=\|\varphi\|^{1/2}.
 \end{gathered}
 \tag{VI.8}
\]
The zero case uses both vectors zero. Thus every complex normal functional is a single vector coefficient, with the optimal product of the two vector norms.

## Spatiality when cyclic separating vectors exist

Let \(\alpha:M_1\to M_2\) be a star isomorphism between concrete von Neumann algebras possessing cyclic separating vectors \(\xi_1\) and \(\xi_2\). Its normality follows from the order argument in VI03. The functional
\[
 \psi(x)=\langle\alpha(x)\xi_2,\xi_2\rangle
\]
is faithful and normal. VI02, using the separating vector \(\xi_1\), gives \(\psi=\omega_\eta\) for some \(\eta\in H_1\). Faithfulness gives \(e_\eta=e_{\xi_1}=1\). Transfer (VI.2) in both directions, followed by PE07, gives \(e'_\eta\sim e'_{\xi_1}=1\). Choose \(u\in M_1'\) with initial projection \(e'_\eta\) and final projection one. The vector \(\eta_0=u\eta\) is cyclic and has the same functional \(\psi\), because \(u\) commutes with \(M_1\) and is isometric on its initial space.

The map on cyclic vectors
\[
 U(x\eta_0)=\alpha(x)\xi_2
 \tag{VI.9}
\]
preserves inner products, as both are computed by \(\psi(y^*x)\). Its domain and range are dense, so it extends to a unitary \(U:H_1\to H_2\). Multiplying by an additional element on that dense domain gives
\[
 \begin{gathered}
 UxU^*=\alpha(x),\\
 x\in M_1.
 \end{gathered}
 \tag{VI.10}
\]
Together with VI01, this proves spatiality on every sigma-finite central summand of two representations satisfying (VI.1).

## Counting small projections on a central piece

We need three projection facts for the remaining case. A projection is called sigma-finite when its corner algebra is sigma-finite. Subequivalence preserves this property, since it identifies a corner with a subcorner. A countable orthogonal sum of sigma-finite projections is sigma-finite: choose a faithful normal state on each nonzero corner, extend by compression, and form a sum with strictly positive summable coefficients. The sum is normal by predual norm convergence, as in CP07. If its value on \(x\geq0\) in the sum corner is zero, every compression \(p_nxp_n\) is zero, so \(x^{1/2}p_n=0\) for all \(n\). Their strong sum is the corner unit, forcing \(x=0\). CY02–03 then proves the assertion.

We also specify the elementary cardinal arithmetic used below. For every infinite cardinal \(\kappa\),
\[
 \kappa\cdot\aleph_0=\kappa.
 \tag{VI.11}
\]
Here and in the maximal-family arguments we use the axiom of choice. To verify (VI.11), first prove \(|\kappa\times\kappa|=\kappa\). If there were a least infinite counterexample \(\kappa\), well-order its pairs by increasing maximum coordinate, and lexicographically within each maximum. The predecessors of a pair with maximum \(\gamma<\kappa\) lie in \((\gamma+1)^2\). That set has cardinal less than \(\kappa\), by minimality of the counterexample, with finite \(\gamma\) handled directly. The resulting order type cannot exceed the initial ordinal \(\kappa\), since an element at position \(\kappa\) would have \(\kappa\) predecessors. This contradicts the alleged counterexample. The diagonal supplies the reverse injection, so the equality follows by the explicit Schröder–Bernstein bijection in PE08. Injections between \(\kappa\), \(\kappa\times\mathbb N\) and \(\kappa^2\) now give (VI.11). Also any infinite set admits a bijection onto itself with one chosen point removed: start a countable sequence at that point, shift the sequence, and fix its complement.

**A bound from a sigma-finite cover.** Suppose the identity of a von Neumann algebra \(B\) is the sum of nonzero orthogonal sigma-finite projections \((g_j)_{j\in J}\), where \(J\) is infinite. If \((h_i)_{i\in I}\) is any orthogonal family of nonzero projections, then
\[
 |I|\leq|J|.
 \tag{VI.12}
\]
For each \(j\), choose a faithful normal state of \(g_jBg_j\) and extend it by compression to \(\psi_j\) on \(B\). For fixed \(j\), only countably many \(\psi_j(h_i)\) are positive: finite subsums are bounded by \(\psi_j(1)=1\), and there are only finitely many terms above each fixed positive threshold. Each nonzero \(h_i\) has \(h_i g_j\ne0\) for some \(j\), since \(\sum_jg_j=1\) strongly. Then \(g_jh_i g_j\ne0\), and faithfulness gives \(\psi_j(h_i)>0\). Thus \(I\) is covered by \(|J|\) countable sets. Choosing an enumeration in each set gives an injection into \(J\times\mathbb N\), and (VI.11) proves the bound. Nonzero projections are essential here; arbitrary zero terms cannot be counted this way.

**A homogeneous central piece.** Suppose \(B\) has no nonzero sigma-finite central projection, and \((p_j)_{j\in J}\) is a nonempty orthogonal family of mutually equivalent nonzero sigma-finite projections. Write \(p\) for one member and \(c=c_B(p)\). There are a nonzero central \(w\leq c\), an uncountable index set \(I\supseteq J\), and orthogonal projections \((r_i)_{i\in I}\) such that
\[
 \begin{gathered}
 w=\sum_{i\in I}r_i,\\
 r_i\sim wp,\\
 c_B(r_i)=w.
 \end{gathered}
 \tag{VI.13}
\]
The labels in \(J\) are retained, but equality \(r_j=wp_j\) is not claimed.

To prove this, work in \(Bc\) and extend the given family to a maximal orthogonal family \((p_i)_{i\in I}\) of copies of \(p\). Put \(r=c-\sum_i p_i\). Central comparison, CT01, gives a central \(w\leq c\) with
\[
 wr\precsim wp,\qquad
 (c-w)p\precsim(c-w)r.
\]
If \(w=0\), a copy of \(p\) under \(r\) would enlarge the family, a contradiction. Thus \(w\ne0\), and every \(wp_i\) is nonzero because \(c_B(p_i)=c\). If \(I\) were countable, then \(w=wr+\sum_iwp_i\) would be sigma-finite by the first paragraph, contradicting the assumption on central projections. Hence \(I\) is uncountable.

Set \(d=\sum_iwp_i\), choose \(i_0\in I\), and shift the index set onto \(I\setminus\{i_0\}\). Since the cut projections are equivalent, their partial isometries give
\(d\sim\sum_{i\ne i_0}wp_i\). Meanwhile \(wr\precsim wp_{i_0}\). Adding these two comparisons proves \(w\precsim d\leq w\), whence \(w\sim d\) by PE07. Choose \(u\in B\) with \(u^*u=d\), \(uu^*=w\), and set \(r_i=u(wp_i)u^*\). These projections satisfy (VI.13); their central carriers are \(w\), because central cuts commute with the equivalences and \(c_B(wp)=w\).

The arbitrary sums of partial isometries used here are legitimate: their initial projections are orthogonal and their final projections are orthogonal. On each vector, squared norms of finite sums are the corresponding sums of squared norms, so the net and its adjoint converge strongly. The limits have the stated initial and final projection sums and belong to the strongly closed algebra. Thus no countable summation was substituted for an uncountable family.

## A full corner cannot have a smaller local multiplicity

Suppose \(B\ne0\) has no nonzero sigma-finite central projection, \(q\in B\) has \(c_B(q)=1\), and there is a star isomorphism
\[
 \begin{gathered}
 \Theta:B\longrightarrow qBq,\\
 \Theta(z)=zq,\\
 z\in Z(B).
 \end{gathered}
 \tag{VI.14}
\]
Then some nonzero central projection \(w\in B\) satisfies \(qw\sim w\).

The corner-center theorem EC05 identifies the central projections of \(qBq\) as \(zq\), uniquely because \(c_B(q)=1\). Equation (VI.14) shows that this corner also has no nonzero sigma-finite central projection: the corresponding corner of \(B\) would be isomorphic to it, and sigma-finiteness is the projection-countability property.

Choose a nonzero sigma-finite projection \(p\leq q\). Such a projection exists by taking the support of a nonzero vector functional with vector in \(qH\); CP12 makes the functional faithful on its support corner. Apply (VI.13) inside \(qBq\), starting with \(p\). We obtain a nonzero central \(z\in B\) and an uncountable orthogonal family \((g_j)_{j\in J}\) of equivalent sigma-finite projections with sum \(qz\). Each has central carrier \(qz\) in \(qBq\), hence central carrier \(z\) in \(B\), by EC05 and fullness of \(q\).

Apply (VI.13) again, now in \(Bz\), starting with the entire family \((g_j)_{j\in J}\). It gives a nonzero central \(w\leq z\), an index set \(I\supseteq J\), and a family \((r_i)_{i\in I}\) such that
\[
 \begin{gathered}
 w=\sum_{i\in I}r_i,\\
 qw=\sum_{j\in J}wg_j,\\
 r_i\sim wg_j,\\
 i\in I,\quad j\in J.
 \end{gathered}
 \tag{VI.15}
\]
Every displayed summand is nonzero and sigma-finite. The second decomposition is the central cut of the original one, not a claim that the first family's conjugation fixed the original projections.

The isomorphism \(\Theta\) carries the \(r_i\) to a family of nonzero orthogonal projections in \(qwBqw\). This algebra has the sigma-finite cover \((wg_j)_{j\in J}\). Thus (VI.12) gives \(|I|\leq|J|\), while \(J\subseteq I\) gives the reverse inequality. Choose a bijection between the index sets and sum partial isometries pairing their equivalent summands in (VI.15). The result has initial projection \(qw\) and final projection \(w\), proving
\[
 qw\sim w\quad\text{in }B.
 \tag{VI.16}
\]
The argument uses central support and cardinality, not a semifinite trace or a classification by finite numerical dimensions.

## Spatiality in arbitrary representations with conjugation

Let \(M_i\subseteq B(H_i)\) have conjugations \(J_i\) satisfying (VI.1), and let \(\alpha:M_1\to M_2\) be any star isomorphism. We prove that a unitary \(U:H_1\to H_2\) implements it. The zero algebra case is immediate, since its unital representation has zero Hilbert space.

First suppose \(M_1\) has no nonzero sigma-finite central projection. Normality of \(\alpha\) follows from VI03. On \(H_1\oplus H_2\), form the diagonal representation
\[
 A=\{x\oplus\alpha(x):x\in M_1\}.
\]
It is a faithful normal representation, so its image is a von Neumann algebra by the closed-image proof, WH02. The projections \(E_i\) onto the two summands belong to \(A'\) and have central carrier one: the center of \(A\), and hence of \(A'\), consists of \(z\oplus\alpha(z)\), and such an operator cannot annihilate either entire summand unless \(z=0\).

Compare \(E_1,E_2\) in \(A'\) by CT01. On a nonzero central part, one is subequivalent to the other. Restrict to that part and interchange the two representations if necessary. We may therefore take a partial isometry in \(A'\) from \(E_2\) onto a subprojection of \(E_1\). It restricts to a unitary
\[
 V:H_2\longrightarrow qH_1,
 \qquad q\in M_1',
\]
intertwining \(\alpha(x)\) with \(x|_{qH_1}\). This restricted representation is faithful, so \(c_{M_1'}(q)=1\): a central projection annihilating \(q\) would annihilate the faithful restriction and hence be zero. Transfer \(J_2\) to \(qH_1\) by \(V\), and call it \(K_2\). It satisfies the same algebra-exchange and center-adjoint conditions for the restricted algebra.

Put \(B=M_1'\). By the reducing-compression identity of AR03, the commutant of \(M_1|_{qH_1}\) is \(qBq\). The two conjugations consequently give the map
\[
 \begin{gathered}
 \Theta(b)=K_2c_bK_2,\\
 c_b=(J_1bJ_1)|_{qH_1},\\
 b\in B.
 \end{gathered}
 \tag{VI.17}
\]
Conjugation by each antiunitary is conjugate-linear and multiplicative, as proved in SJ01. Thus their composite in (VI.17) is a complex-linear star isomorphism from \(B\) onto \(qBq\). For \(z\in Z(B)=Z(M_1)\), the first conjugation sends \(z\) to \(z^*\), and the second sends the restricted \(z^*\) back to the restricted \(z\). Hence \(\Theta(z)=zq\).

The algebra \(B\) has no nonzero sigma-finite central projection either: conjugation by \(J_1\) fixes central projections and identifies the two projection lattices, preserving orthogonality. VI06 now provides a nonzero central \(w\) and a partial isometry \(u\in M_1'\) from \(qw\) onto \(w\). The unitary \(uV\), restricted to \(\alpha(w)H_2\), maps that space onto \(wH_1\) and intertwines the two represented algebras. Its adjoint implements \(\alpha\) on the nonzero central summand \(M_1w\). This establishes a spatial implementation on some central piece whenever no nonzero sigma-finite central piece is available.

Finally, take a maximal orthogonal family of nonzero central projections \((z_i)\) on each of which \(\alpha\) is spatial, and choose an implementing unitary \(U_i:z_iH_1\to\alpha(z_i)H_2\). If their sum left a nonzero central remainder, there would be two possibilities. If that remainder contains a nonzero sigma-finite central projection, the restrictions of the conjugations and VI01–04 give a spatial implementation there. If it contains no such projection, the preceding argument gives a nonzero spatial central piece. Either possibility contradicts maximality. Therefore \(\sum_i z_i=1\). Normality gives \(\sum_i\alpha(z_i)=1\) as well.

The direct sum of the \(U_i\) is an onto isometry, since its squared norm on each vector is the sum of the squared norms of its orthogonal components. It therefore defines a unitary with
\[
 \begin{gathered}
 U=\bigoplus_iU_i,\\
 UxU^*=\alpha(x),\\
 x\in M_1.
 \end{gathered}
 \tag{VI.18}
\]
Intertwining holds first on finite sums of central components and then by continuity. This proves spatiality without a sigma-finiteness, separability or semifiniteness assumption.

## Four checks on the scope

**A normal state need not be a vector state in an arbitrary representation.** On \(M_2(\mathbb C)\) acting on \(\mathbb C^2\), the normalized trace has density \(I/2\) of rank two, whereas a nonzero vector functional has rank-one density \(\xi\xi^*\). They cannot agree. This representation has no conjugation exchanging the algebra and its commutant: conjugation preserves the dimension of the operator space, whereas the commutant consists only of scalars.

**The positive-functional theorem does not promise a faithful vector.** Let \(I\) be uncountable, and represent \(M=\ell^\infty(I)\) diagonally on \(\ell^2(I)\), with coordinate conjugation. Its commutant is itself, as the coordinate matrix-unit test shows. For \(\varphi\in M_*^+\), put \(a_i=\varphi(p_i)\). Normality on the finite-coordinate projection net gives \(\sum_i a_i=\varphi(1)<\infty\), so only countably many coefficients are nonzero. Applied to positive diagonal operators, the same net gives
\[
 \varphi(x)=\sum_i a_i x_i.
\]
Linearity extends the formula to every \(x\in M\). The vector with coordinates \(\sqrt{a_i}\) implements it. Nevertheless every vector in \(\ell^2(I)\) has countable support, so none is faithful on the whole algebra. A bijection \(\sigma:I\to I'\) is implemented between these diagonal representations by the unitary \(U\delta_i=\delta_{\sigma(i)}\), illustrating the arbitrary-cardinality spatial conclusion.

**The representation hypothesis matters for spatiality.** The scalar algebras on \(\mathbb C\) and \(\mathbb C^2\) are normally star isomorphic, but no unitary joins those Hilbert spaces. The second representation cannot satisfy (VI.1), since its commutant is all of \(B(\mathbb C^2)\). An abstract algebra isomorphism alone therefore does not control representation multiplicity.

**Implementers are not asserted to be unique.** If \(U\) implements \(\alpha\) and \(v\) is a unitary in \(M_2'\), then \(vU\) implements the same isomorphism. Conversely, two implementers \(U_1,U_2\) satisfy \(U_2U_1^*\in M_2'\), by their intertwining identities. The theorem supplies spatiality; it does not choose a positive cone or impose an additional relation between the given conjugations.

**Source.** M. Takesaki, *Theory of Operator Algebras I*, Chapter V, §3, Propositions 3.12 and 3.14, Theorems 3.15–3.16 and the cardinal estimate of Lemma 3.17, pp. 341–343. The positive-functional compression, countability estimates and local central multiplicity argument are proved above at their stated earlier inputs. Only the cyclic separating vector assertion requires sigma-finiteness.

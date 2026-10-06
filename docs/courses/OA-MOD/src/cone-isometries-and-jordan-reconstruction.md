# Recovering Jordan multiplication from the positive cone

**Independently written mathematical draft.**

Suppose a complex-linear unitary between two standard forms maps one positive cone onto the other. Closed faces recover projections; their orthogonal projections recover the symmetrized algebra action. This gives a normal Jordan star isomorphism and its exact action on positive vector functionals. When a faithful positive vector is available, a separate closed-graph argument identifies this map with the quarter-power construction.

The source problem is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(6). Its quadratic identity is printed for every Hilbert vector. That scope is false: JR-03 gives an explicit matrix counterexample. The identity holds for vectors in the positive cone, and an operator identity for the symmetrized action holds on the entire Hilbert space. We prove these valid statements and both steps of the source's faithful-vector construction; we do not silently retain the false quantifier.

The inputs are the written closed-face correspondence Closing one order ideal gives its entire supported face and Projections and all closed cone faces and vector representation Transporting positive functionals and automorphisms, bounded operator calculus and forms The bounded prerequisite boundary, spectral powers and transport Unbounded measurable functions and Changes of variable, powers, and actual ranges/08, the normal positive-map criterion The positive-map equivalence, and the full quarter-power order theorem QO. No general classification of linear isometries or external Jordan theorem is used.

Write the two forms as \((M_i,H_i,J_i,P_i)\), and let \(U:H_1\to H_2\) be complex-linear and unitary with \(UP_1=P_2\). Inner products are linear in the first variable, and \(\omega_v(x)=\langle xv,v\rangle\). The construction through JR-03 works without sigma-finiteness. The faithful-vector comparison in JR-04/06 has exactly that additional hypothesis.

## Faces determine a symmetrized projection action

For a projection \(p\in M_i\), set

\[
 Q_p=pJ_ipJ_i,\qquad P_{i,p}=P_i\cap Q_pH_i.
\]

SE-03 says that the complex linear span of \(P_{i,p}\) is dense in \(Q_pH_i\), and SE-08 identifies all closed cone faces with these \(P_{i,p}\). Thus there is a unique order bijection \(f\) between the projection lattices such that

\[
 UP_{1,p}=P_{2,f(p)}.
\]

The map preserves orthogonality and complements: use SE-08's descriptions \(P_{i,p}\perp P_{i,q}\) for \(pq=0\), and \(P_i\cap P_{i,p}^{\perp}=P_{i,1-p}\), together with unitarity. In particular \(f(1)=1\). An order bijection preserves every existing supremum, by applying its inverse to any upper bound. Hence, for orthogonal projections, \(f(p+q)=f(p)+f(q)\).

Taking closed linear spans of the face equality gives

\[
 UQ_pU^*=Q_{f(p)}.
\]

The conjugations are also intertwined. On \(P_1\), both \(UJ_1\) and \(J_2U\) equal \(U\); the cone spans \(H_1\) over \(\mathbb C\), and both maps are antilinear, so \(UJ_1=J_2U\) everywhere.

The two projections \(p\) and \(J_ipJ_i\) commute. Expanding their complementary product yields

\[
 \begin{gathered}
 p+J_ipJ_i-1\\
 =Q_p-Q_{1-p}.
 \end{gathered}
 \tag{JR.1}
\]

For \(v\in P_i\), the left and right projection expectations agree, because \(J_iv=v\). Consequently

\[
 \begin{gathered}
 2\langle pv,v\rangle\\
 =\|v\|^2+\|Q_pv\|^2-\|Q_{1-p}v\|^2.
 \end{gathered}
\]

Every quantity on the right is determined by the Hilbert cone and its closed faces. It follows that

\[
 \omega_{Uv}(f(p))=\omega_v(p)
 \qquad(v\in P_1).
\]

We will extend \(f\) using this identity, rather than presuming that a lattice bijection already acts linearly on algebra elements.

## Extend the projections and prove Jordan multiplication

For a finite real linear combination of projections, prescribe

\[
 \begin{gathered}
 \theta_0\left(\sum_j a_jp_j\right)
   =\sum_j a_jf(p_j),\\
 a_j\in\mathbb R.
 \end{gathered}
\]

This is well defined even when the projections do not commute. Indeed, if the sum on the left is zero, the projection identity in JR-01 makes the right-hand sum have zero expectation against every vector of \(P_2\). These tests separate self-adjoint operators. To verify that fact, every ordinary vector functional is represented by a cone vector of the same norm, by SE-11. Thus vanishing on the cone makes every Hilbert quadratic form vanish, and polarization makes the operator zero.

The same observation and BK-01's self-adjoint norm formula give

\[
 \|a\|=\sup_{v\in P_i,\ \|v\|=1}|\omega_v(a)|
 \qquad(a=a^*).
\]

Therefore \(\theta_0\) is isometric on its real linear domain. Finite spectral steps are norm dense in \((M_i)_{\rm sa}\): partition a bounded real spectral interval into intervals of mesh \(\varepsilon\), use their mutually orthogonal spectral projections in \(M_i\), and choose one value per interval. SK-05/08 put these projections in the algebra and bound the norm error by \(\varepsilon\). The map \(\theta_0\) consequently extends to an isometry of the whole self-adjoint part. The construction with \(f^{-1}\) is its inverse.

Extend complex linearly by

\[
 \begin{gathered}
 \theta(a+ib)=\theta_0(a)+i\theta_0(b),\\
 a=a^*,\qquad b=b^*.
 \end{gathered}
\]

The real and imaginary self-adjoint parts are unique, so this is a complex-linear bijection preserving adjoints and the identity. It is bounded: each part has norm at most \(\|a+ib\|\), giving the sufficient bound \(\|\theta(x)\|\le2\|x\|\). The cone-vector expectation identity passes to norm limits and then to complex linear combinations. In particular \(x\ge0\) if and only if \(\theta(x)\ge0\), because cone-vector tests detect positivity by SE-11 and BK-01. Thus both maps preserve order.

For a finite spectral step \(a=\sum_j\lambda_jp_j\) with orthogonal \(p_j\), orthogonality of the \(f(p_j)\) proves \(\theta(a^2)=\theta(a)^2\). Approximate an arbitrary self-adjoint element by these steps; boundedness of \(\theta\) and norm continuity of multiplication give the same equality. Polarizing self-adjoint squares gives preservation of \(ab+ba\) for self-adjoint \(a,b\). Complex bilinearity then gives

\[
 \begin{gathered}
 \theta(xy+yx)\\
 =\theta(x)\theta(y)+\theta(y)\theta(x)
 \end{gathered}
\]

for all \(x,y\in M_1\). This is the Jordan product identity, proved here at full operator-algebra scope. Together with bijectivity and preservation of adjoints it makes \(\theta\) a Jordan star isomorphism.

It and its inverse are normal. An order bijection sends the least upper bound of a bounded increasing positive net to the least upper bound of its image: pull any proposed upper bound back through the inverse. The image net is bounded by positivity and the image of its original bound. NP-04 now gives ultraweak continuity in both directions. No countability restriction on these nets is used.

## The valid quadratic identity and the source correction

Define the complex-linear symmetrized action by

\[
 j_i(x)=\tfrac12(x+J_ix^*J_i).
\]

For projections, (JR.1) and transport of the \(Q_p\) imply transport of \(j_i(p)\). Finite real projection sums, norm approximation, and complex linearity extend it to

\[
 \begin{gathered}
 Uj_1(x)U^*\\
 =j_2(\theta(x)).
 \end{gathered}
 \tag{JR.2}
\]

This bounded-operator identity holds on all of \(H_2\). If \(v\in P_i\), antiunitarity and \(J_iv=v\) give \(\langle J_ix^*J_iv,v\rangle=\langle xv,v\rangle\). Hence the unsymmetrized quadratic identity is

\[
 \omega_{Uv}\circ\theta=\omega_v.
 \tag{JR.3}
\]

Here \(v\in P_1\). It is also the identity already extended in JR-02. In fact the displayed argument proves it for every \(J_1\)-fixed vector, since \(UJ_1=J_2U\). It cannot be extended to arbitrary complex Hilbert vectors.

**Counterexample to the printed all-vector statement.** Use the Hilbert–Schmidt standard form of \(M_2(\mathbb C)\). Transposition \(U(v)=v^{\mathsf T}\) is a complex-linear Hilbert-space unitary mapping positive matrices onto positive matrices. It sends the supported face of \(p\) to that of \(p^{\mathsf T}\), so JR-02 gives \(\theta(x)=x^{\mathsf T}\). Take \(x=E_{11}\) and \(v=E_{12}\). Then

\[
 xv=E_{12},\qquad
 \theta(x)Uv=E_{11}E_{21}=0.
\]

Thus the original quadratic value is one and the transported value is zero. For positive matrices \(v\), the corrected identity does hold: both sides reduce, by transposition and finite trace cyclicity, to \(\operatorname{Tr}(xv^2)\). Moreover (JR.3) determines \(\theta\) uniquely, since \(UP_1=P_2\) and cone-vector functionals separate algebra elements. The counterexample therefore cannot be removed by choosing a different induced Jordan map.

The implementing cone unitary is unique for a prescribed \(\theta\) whenever it exists. If \(U,V\) both satisfy (JR.3), surjectivity of \(\theta\) makes \(\omega_{Uv}=\omega_{Vv}\) for every \(v\in P_1\). Both implementing vectors are in \(P_2\), so SE-11 gives \(Uv=Vv\). Complex spanning then gives \(U=V\). This is a uniqueness statement; it does not by itself prove existence for an arbitrary Jordan map given in advance.

## Transport a faithful vector and its order intervals

Now assume \(M_1\) has a faithful normal positive functional \(\psi_1\), put \(\xi_1=\xi_{\psi_1}\), and set

\[
 \xi_2=U\xi_1,\qquad \psi_2=\omega_{\xi_2}.
\]

The latter functional is bounded and normal by CP-06, and its vector lies in \(P_2\). It is faithful. In fact SE-07 identifies the smallest closed face containing \(\xi_1\) as all of \(P_1\). The unitary carries this face onto the smallest closed face containing \(\xi_2\), so that face is all of \(P_2\). SE-08 then gives \(s(\psi_2)=1\), proving faithfulness.

The order and inverse order preservation of \(U\) on the Hilbert cones give, for every \(c\ge0\),

\[
 U[0,c\xi_1]=[0,c\xi_2].
\]

Hence it carries the algebraic principal face of \(\xi_1\) onto that of \(\xi_2\). QO proves that both are dense in their full cones and that their complex spans are the ranges of

\[
 \Theta_i(x)=\Delta_i^{1/4}x\xi_i.
\]

Thus the expression

\[
 \beta=\Theta_2^{-1}U\Theta_1
\]

is defined on every element of \(M_1\) and is a unital complex-linear order isomorphism onto \(M_2\). The inverse is defined on the precise range supplied by QO; no Hilbert-norm bounded inverse for \(\Theta_i\) is asserted.

We must still prove \(\beta=\theta\). Merely observing that \(\beta\) preserves order would not identify its quadratic implementation. The next lemma supplies that link without appealing to a general Jordan classification theorem.

## Recover the quarter power from a bounded real operator

Consider one faithful finite standard form with vector \(\xi\), Tomita operator \(S=J\Delta^{1/2}\), and real Hilbert spaces

\[
 \begin{gathered}
 K=\{v\in D(S):Sv=v\},\\
 L=\{v\in H:Jv=v\}.
 \end{gathered}
\]

Their real inner products are \(\operatorname{Re}\langle\cdot,\cdot\rangle\). The space \(K\) is closed in \(H\): if \(v_n\to v\) and \(Sv_n=v_n\), closedness of \(S\) gives \(v\in D(S)\) and \(Sv=v\). The vectors \(a\xi\), \(a=a^*\in M\), are dense in \(K\). Indeed the finite Tomita graph is the closure of \(x\xi\mapsto x^*\xi\); for a fixed vector in \(K\), graph approximants can be replaced by \((x+x^*)\xi/2\).

Define real-linear operators

\[
 \begin{gathered}
 Rv=\tfrac12(v+Jv),\\
 Tv=\Delta^{1/4}v\qquad(v\in K).
 \end{gathered}
\]

They both take values in \(L\). For \(T\), use \(\Delta^{1/2}v=Jv\) and spectral transport by \(J\) to get

\[
 J\Delta^{1/4}v
 =\Delta^{-1/4}Jv
 =\Delta^{1/4}v.
\]

All terms are defined: \(v\in D(\Delta^{1/2})\), and the product of the negative quarter power with \(\Delta^{1/2}v\) is justified by the spectral integral of \(\lambda^{1/2}\), bounded by that of \(1+\lambda\). Spectral Cauchy–Schwarz also gives \(\|Tv\|\le\|v\|\). Direct expansion now yields

\[
 \begin{gathered}
 \|Tv\|^2\\
 =2\|Rv\|^2-\|v\|^2.
 \end{gathered}
 \tag{JR.4}
\]

Indeed \(\|Tv\|^2=\langle\Delta^{1/2}v,v\rangle=\operatorname{Re}\langle Jv,v\rangle\). Thus \(R\) is bounded and bounded below by \(1/\sqrt2\).

It is onto \(L\), with explicit bounded inverse

\[
 R^{-1}\eta=2(1+\Delta^{1/2})^{-1}\eta
 \qquad(\eta\in L).
\]

For the vector \(v\) on the right, boundedness of \(\lambda^{1/2}/(1+\lambda^{1/2})\) gives the half-power domain. Spectral conjugation gives

\[
 Jv=2(1+\Delta^{-1/2})^{-1}\eta
     =\Delta^{1/2}v.
\]

Therefore \(Sv=v\), and \((v+Jv)/2=\eta\). This verifies both the range assertion and the inverse on its full domain.

Put \(C=TR^{-1}\). It is the restriction to \(L\) of the bounded positive operator

\[
 f(\Delta),\qquad
 f(\lambda)=\frac{2\lambda^{1/4}}{1+\lambda^{1/2}}.
\]

The scalar function is positive, at most one, and invariant under \(\lambda\mapsto\lambda^{-1}\). Thus \(f(\Delta)\) commutes with \(J\) and preserves \(L\); its restriction is a positive self-adjoint real operator. Real polarization of (JR.4) gives \(T^*T=2R^*R-1_K\). Multiplying by the bounded inverses yields

\[
 C^2=2I_L-(RR^*)^{-1}.
\]

Consequently the quarter-power restriction is recovered from \(R\) alone:

\[
 T=CR,\qquad C\ge0,
 \tag{JR.5}
\]

where \(C\) is the unique positive square root of \(2I_L-(RR^*)^{-1}\), with \(I_L\) the identity on \(L\).

Here all adjoints are real Hilbert adjoints, supplied by the proved real Riesz theorem underlying BK-01. The positive square-root assertion requires no new real spectral theorem. A bounded real self-adjoint operator on \(L\) extends complex linearly to \(H=L+iL\). Since inner products of vectors in \(L\) are real, this extension is bounded, self-adjoint, and positive when the original is. Apply BK-01's complex positive calculus. Real polynomial approximation makes its positive square root commute with \(J\), so it restricts to \(L\); uniqueness follows by complex extension of any other positive real square root.

## Identify the order-map formula exactly

Use JR-05 for the two faithful vectors in JR-04. The cone identity (JR.3) gives \(\psi_2\circ\theta=\psi_1\). For a self-adjoint \(a\in M_1\), Jordan square preservation therefore gives

\[
 \begin{gathered}
 \|\theta(a)\xi_2\|^2=\psi_2(\theta(a)^2)\\
 =\psi_1(a^2)=\|a\xi_1\|^2.
 \end{gathered}
\]

Real polarization and density yield a real Hilbert-space unitary

\[
 \begin{gathered}
 W:K_1\longrightarrow K_2,\\
 W(a\xi_1)=\theta(a)\xi_2.
 \end{gathered}
\]

It is onto because \(\theta\) maps the entire self-adjoint part onto the other one. The restriction \(U:L_1\to L_2\) is also a real unitary, since \(UJ_1=J_2U\).

For self-adjoint \(a\), we have \(R_i(a\xi_i)=j_i(a)\xi_i\). The symmetrized operator identity (JR.2) consequently gives

\[
 UR_1=R_2W
\]

first on the dense self-adjoint GNS vectors, then on all of \(K_1\). Taking real adjoints gives \(U R_1R_1^*U^*=R_2R_2^*\). Invert these bounded invertible operators and use uniqueness of the positive square root in JR-05; the result is \(UC_1=C_2U\). Formula (JR.5) now yields \(UT_1=T_2W\), so

\[
 U\Delta_1^{1/4}a\xi_1
   =\Delta_2^{1/4}\theta(a)\xi_2
\]

for every self-adjoint \(a\). Complex linearity extends it to every \(x\in M_1\). Since \(\Theta_2\) is injective, we have proved the source's precise formula

\[
 \theta=\Theta_2^{-1}U\Theta_1.
 \tag{JR.6}
\]

In particular the map \(\beta\) in JR-04 is the normal Jordan star isomorphism already constructed. Its construction does not depend on the chosen faithful positive vector, because the map recovered from all closed faces in JR-01/02 does not depend on that choice. This completes the two source steps, the valid quadratic implementation, and the stated quantifier correction.

## A finite calculation checks the real-operator formula

In the Hilbert–Schmidt form of \(M_2(\mathbb C)\), take density \(h=\operatorname{diag}(1,16)\), so \(\xi=h^{1/2}=\operatorname{diag}(1,4)\). For a self-adjoint off-diagonal matrix and its GNS vector,

\[
 \begin{gathered}
 a=\begin{pmatrix}0&z\\\bar z&0\end{pmatrix},\\
 v=a\xi=\begin{pmatrix}0&4z\\\bar z&0\end{pmatrix},
 \end{gathered}
\]

the two real maps are

\[
 \begin{gathered}
 Rv=\begin{pmatrix}0&\tfrac52 z\\\tfrac52\bar z&0\end{pmatrix},\\
 Tv=h^{1/4}ah^{1/4}
    =\begin{pmatrix}0&2z\\ {2\bar z}&0\end{pmatrix}.
 \end{gathered}
\]

Thus

\[
 \begin{gathered}
 \|v\|^2=17|z|^2,\\
 \|Rv\|^2=\tfrac{25}{2}|z|^2,\\
 \|Tv\|^2=8|z|^2.
 \end{gathered}
\]

These numbers verify (JR.4). On this real two-dimensional off-diagonal component, \(RR^*\) is multiplication by \(25/34\). Hence the square-root factor in (JR.5) is

\[
 \sqrt{2-34/25}=4/5,
\]

which sends the off-diagonal coefficient \(5z/2\) of \(Rv\) to \(2z\), exactly as required. On the diagonal component all three maps are the identity. This calculation checks the constants and the order of \(RR^*\) in the general bounded recovery formula; the proof itself applies to arbitrary Hilbert-space dimension.

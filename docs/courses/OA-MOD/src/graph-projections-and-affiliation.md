# Closed operators through their graph projections

A closed operator has an unbounded action but a bounded geometric encoding: the orthogonal projection onto its graph. That encoding remembers the domain as well as the values. We first use it to recognize affiliation, then construct its four entries from Hilbert-space adjoints, and finally treat domains that are not dense. A matrix example explains why both off-diagonal entries matter.

The mathematical source for the affiliation question and the four-entry computation is Masamichi Takesaki, *Theory of Operator Algebras I*, Chapter IV, §5, Exercise 3, printed page 229 (PDF page 237 in the approved edition). For comparison, Jesse Peterson's freely accessible [*Notes on operator algebras*, 27 April 2020, Lemma 4.1.4 and Proposition 4.1.6, pages 67–68](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf) give the graph-complement description of the adjoint. We prove every unbounded-operator assertion needed here. Our bounded inputs are the Hilbert projection and adjoint constructions in BK01, the bicommutant theorem BK02, and the unitary spanning argument BK08.

## Affiliation is a symmetry of a closed subspace

Inner products are linear in the first variable. Let \(M\subseteq B(H)\) be a unital von Neumann algebra, and let \(T:D(T)\subseteq H\to H\) be a closed complex-linear operator. Density of \(D(T)\) is **not** assumed in this section. Closedness means that

\[
 \begin{gathered}G(T)=\{(x,Tx):\\ x\in D(T)\}.\end{gathered}
 \tag{GP.1}
\]

is a closed linear subspace of \(H\oplus H\). Write \(p_T\) for its orthogonal projection. By definition, \(T\) is affiliated with \(M\) if every unitary \(u\in M'\) preserves its domain and action:

\[
 \begin{gathered}
 uD(T)=D(T),\\
 Tux=uTx\\ (x\in D(T)).
 \end{gathered}
 \tag{GP.2}
\]

Thus an equality such as \(uT=Tu\) includes equality of domains, not just agreement where both sides happen to exist.

**Theorem.** The operator \(T\) is affiliated with \(M\) if and only if each of the four bounded matrix entries of \(p_T\) belongs to \(M\).

**Proof.** For a unitary \(u\), let \(W_u:H\oplus H\to H\oplus H\) be \(W_u(x,y)=(ux,uy)\). Condition (GP.2) is exactly \(W_uG(T)=G(T)\): membership of \((ux,uTx)\) in the graph gives both the domain inclusion and the required value, and using \(u^*\) gives the reverse inclusion. A unitary carrying a closed subspace onto itself carries its orthogonal complement onto itself too, by the inner-product identity. It therefore commutes with the orthogonal projection. Conversely, commutation with that projection makes its range invariant under the unitary and its inverse. Hence affiliation is equivalent to

\[
 \begin{gathered}
 p_TW_u=W_up_T\\
 (u\in\mathcal U(M')).
 \end{gathered}
 \tag{GP.3}
\]

Write \(p_T=(p_{ij})_{i,j=1}^2\), using the bounded coordinate inclusions and projections of \(H\oplus H\). The matrix equation in (GP.3) says \(p_{ij}u=up_{ij}\) for every entry. BK08 proves that the linear span of the unitaries of \(M'\) is \(M'\). Thus every entry lies in \((M')'=M\), by BK02. Conversely, entries in \(M\) commute with all these unitaries, so (GP.3) applies. This proves both implications, including their domain assertions.

Under the unitary identification \((x,y)\mapsto x\otimes e_1+y\otimes e_2\), matrices with entries in \(M\) are precisely
\(M\mathbin{\overline\otimes}M_2(\mathbb C)\). Indeed, each such matrix is the finite sum \(\sum_{i,j}p_{ij}\otimes e_{ij}\). This set is weakly closed: weak convergence of operators on the direct sum gives weak convergence of every entry by testing coordinate vectors, and \(M\) is weakly closed. Thus the theorem is also the graph-projection tensor-product criterion, with this specific identification.

## Resolvents constructed from the graph Hilbert space

To compute the entries without assuming an unbounded spectral theorem, allow two Hilbert spaces. Let \(T:D(T)\subseteq K\to L\) be closed and densely defined. The graph \(G=G(T)\), with its inherited inner product, is a Hilbert space. Its coordinate maps

\[
 \begin{gathered}
 J:G\to K,\\ J(x,Tx)=x,\\
 V:G\to L,\\ V(x,Tx)=Tx
 \end{gathered}
 \tag{GP.4}
\]

are bounded contractions. Their column \(W:G\to K\oplus L\), given by \(Wg=(Jg,Vg)\), is the isometric inclusion. Consequently \(WW^*=p_T\): it is self-adjoint and idempotent, is the identity on \(WG\), and has that range. In particular, its four entries are already known bounded maps:

\[
 \begin{gathered}p_T\\=\begin{pmatrix}JJ^*&JV^*\\ VJ^*&VV^*\end{pmatrix}.\end{gathered}
 \tag{GP.5}
\]

We now identify them in operator notation, proving the required domain facts first. Define \(D(T^*)\subseteq L\) as the vectors \(\eta\) for which there is a \(z\in K\) satisfying
\(\langle Tx,\eta\rangle=\langle x,z\rangle\) for all \(x\in D(T)\), and set \(T^*\eta=z\). Density gives uniqueness; the bounded-functional version of this definition is equivalent by the Riesz theorem in BK01. Testing the two coordinates gives

\[
 \begin{gathered}
 G(T)^\perp\\
 =\{(-T^*\eta,\eta):\\ \eta\in D(T^*)\}.
 \end{gathered}
 \tag{GP.6}
\]

For example, orthogonality of \((a,b)\) to every \((x,Tx)\) is exactly the adjoint pairing with \(b\in D(T^*)\) and \(T^*b=-a\); this proves the converse inclusion as well.

The adjoint is closed. If \(\eta_n\to\eta\) and \(T^*\eta_n\to z\), passing to the limit in its pairing shows \(\eta\in D(T^*)\) and \(T^*\eta=z\). Its domain is dense: if \(z\in L\) is orthogonal to \(D(T^*)\), (GP.6) makes \((0,z)\) orthogonal to \(G(T)^\perp\), hence an element of the closed graph \(G(T)\). Its first coordinate is zero, so its second coordinate must be \(T0=0\). Therefore \(z=0\).

We may now form \(T^{**}:D(T^{**})\subseteq K\to L\). For \((x,y)\in K\oplus L\), its adjoint pairing says that \((x,y)\in G(T^{**})\) exactly when
\(\langle T^*\eta,x\rangle=\langle\eta,y\rangle\) for every \(\eta\in D(T^*)\). Taking conjugates identifies this condition with orthogonality to every \((-T^*\eta,\eta)\). By (GP.6) and closedness it is membership in \(G(T)\). Hence \(T^{**}=T\), with equality of domains.

Put \(R=JJ^*:K\to K\). This is a positive contraction. Its kernel is zero: \(\langle Rh,h\rangle=\|J^*h\|^2\), and \(J^*h=0\) means that \(h\) is orthogonal to the dense range \(\operatorname{ran}J=D(T)\). Since \(R\) is self-adjoint, its range is dense by the range-kernel identity in BK01.

For \(h\in K\), write \(J^*h=(x,Tx)\); thus \(x=Rh\). The bounded adjoint identity gives, for every \(y\in D(T)\),

\[
 \begin{gathered}
 \langle x,y\rangle+\langle Tx,Ty\rangle\\
 =\langle h,y\rangle.
 \end{gathered}
 \tag{GP.7}
\]

After conjugation this says \(Tx\in D(T^*)\) and \(T^*Tx=h-x\). Conversely, if \(x\in D(T^*T)\), put \(h=x+T^*Tx\). The adjoint pairing gives (GP.7), and uniqueness of the representing graph vector gives \(J^*h=(x,Tx)\). Therefore

\[
 \begin{gathered}
 R=(I_K+T^*T)^{-1},\\
 \operatorname{ran}R=D(T^*T).
 \end{gathered}
 \tag{GP.8}
\]

The inverse notation records a proved bijection: \(I_K+T^*T\) maps its stated domain onto \(K\), with bounded inverse \(R\). Injectivity also follows directly from (GP.7) with \(h=0\) and \(y=x\).

For completeness, \(T^*T\) is positive and self-adjoint on that actual domain. Let \(A=R^{-1}\), with domain \(\operatorname{ran}R\). It is symmetric, since the identity \(\langle a,Rb\rangle=\langle Ra,b\rangle\) tests its pairings on vectors \(Ra,Rb\). If \(z\in D(A^*)\) and \(h=A^*z\), testing the definition on \(Ry\), \(y\in K\), gives \(\langle y,z\rangle=\langle Ry,h\rangle=\langle y,Rh\rangle\). Thus \(z=Rh\), so \(z\in D(A)\) and \(Az=h\). Symmetry gives the reverse inclusion; hence \(A=A^*\). Subtraction of a bounded identity preserves the adjoint domain, as follows immediately by moving \(\langle x,z\rangle\) across the defining pairing. Thus \(T^*T=A-I_K\) is self-adjoint. It is positive because \(\langle T^*Tx,x\rangle=\|Tx\|^2\).

Apply the same construction to the closed densely defined map \(T^*:D(T^*)\subseteq L\to K\). The proved equality \(T^{**}=T\) then supplies the positive contraction

\[
 \begin{gathered}
 R'=(I_L+TT^*)^{-1},\\
 \operatorname{ran}R'=D(TT^*).
 \end{gathered}
 \tag{GP.9}
\]

It also proves positivity and self-adjointness of \(TT^*\). No formal multiplication of unbounded operators has replaced a domain argument.

## The four entries and the products that require closure

Retain the rectangular densely defined operator of GP02. Let \(S=VJ^*:K\to L\). Since \(J^*h=(Rh,TRh)\), we have \(S=TR\) on all of \(K\). Equations (GP.5)–(GP.9) give

\[
 \begin{gathered}p_T=\\ \begin{pmatrix}R&S^*\\ S&I_L-R'\end{pmatrix}.\end{gathered}
 \tag{GP.10}
\]

Here are all four entries as everywhere defined bounded maps, with their sources and targets:

\[
 \begin{gathered}
 p_{11}=(I_K+T^*T)^{-1}:K\to K,\\
 p_{12}=T^*(I_L+TT^*)^{-1}:L\to K,\\
 p_{21}=T(I_K+T^*T)^{-1}:K\to L,\\
 p_{22}=I_L-(I_L+TT^*)^{-1}:L\to L.
 \end{gathered}
\]

To verify the two entries not yet identified, define the unitary
\(U:L\oplus K\to K\oplus L\) by \(U(\eta,z)=(-z,\eta)\). Equation (GP.6) identifies \(UG(T^*)\) with \(G(T)^\perp\), so \(I-p_T=Up_{T^*}U^*\). The upper-left entry of \(p_{T^*}\) is \(R'\), and its lower-left entry is \(T^*R'\), by the already proved first-column formula. Conjugating by this specified \(U\) makes the lower-right entry of \(I-p_T\) equal to \(R'\) and its upper-right entry equal to \(-T^*R'\). This proves (GP.10), including the sign and the equality \(S^*=T^*R'\).

Every product just displayed has a full domain: \(R K\subseteq D(T^*T)\subseteq D(T)\) and \(R'L\subseteq D(TT^*)\subseteq D(T^*)\). One may also write \(p_{22}=TT^*R'\), because \((I_L+TT^*)R'=I_L\). It is the bounded product on all of \(L\), not a claim that \(TT^*\) itself is bounded.

Two frequently written alternatives need closures. For \(\eta\in D(T^*)\) and \(g=(x,Tx)\in G\),

\[
 \begin{gathered}
 \langle g,J^*T^*\eta\rangle
 =\langle x,T^*\eta\rangle\\
 =\langle Tx,\eta\rangle
 =\langle g,V^*\eta\rangle.
 \end{gathered}
\]

Thus \(J^*T^*\eta=V^*\eta\). Applying \(J\) or \(V\) gives \(RT^*\eta=S^*\eta\) and \(TRT^*\eta=VV^*\eta\). Both left sides initially have domain **exactly** \(D(T^*)\), since their rightmost factor is \(T^*\); subsequent factors are defined on all its values. They are restrictions of bounded operators to a dense domain. Such a restriction has the full bounded operator as its closure: approximate any vector by vectors of the dense domain, and use boundedness to obtain convergence of both coordinates. Consequently

\[
 \begin{gathered}
 \overline{RT^*}=S^*,\\ S^*=T^*R',\\
 \overline{TRT^*}=p_{22},\\ p_{22}=I_L-R'.
 \end{gathered}
 \tag{GP.11}
\]

An unbarred \(RT^*\) need not have domain \(L\), even though it has this bounded extension.

The projection identity gives useful quantitative checks. Its upper-left block says \(R^2+S^*S=R\). The bounded calculus of BK01 applied to the positive contraction \(R\) yields

\[
 \begin{gathered}
 S^*S=R-R^2,\\
 \|S\|\leq\tfrac12.
 \end{gathered}
 \tag{GP.12}
\]

Both diagonal entries are positive contractions, by compression of the orthogonal projection. The factor \(1/2\) is attained for the scalar operator \(T=1\).

The graph projection also recovers the actual operator: \(x\in D(T)\) exactly when there exists a \(y\) with \(p_T(x,y)=(x,y)\), and then that \(y\) is unique and equals \(Tx\). Uniqueness follows because the graph has no nonzero vector of the form \((0,y)\). This is why the criterion of GP01 retains the domain instead of encoding only a formal rule for values.

## Closed operators whose domains are not dense

Return to a closed \(T:D(T)\subseteq H\to H\), with no density assumption. Set \(K=\overline{D(T)}\), and let \(v:K\to H\) be the inclusion isometry. Regard the same rule as the map \(T_0:D(T)\subseteq K\to H\). This operator is densely defined in \(K\) and closed: convergence in \(K\oplus H\) implies convergence of the corresponding graph pairs in \(H\oplus H\), where the original graph is closed. Thus GP02–03 apply to \(T_0\), whose adjoint is a well-defined map from a dense subspace of \(H\) into \(K\).

Define the bounded maps

\[
 \begin{gathered}
 R_0=(I_K+T_0^*T_0)^{-1},\\
 R_1=(I_H+T_0T_0^*)^{-1},\\
 S_0=T_0R_0:K\to H.
 \end{gathered}
\]

The inclusion \(W=\operatorname{diag}(v,I_H):K\oplus H\to H\oplus H\) is an isometry and satisfies \(WG(T_0)=G(T)\). Therefore \(Wp_{T_0}W^*\) is the orthogonal projection onto \(G(T)\): its square is itself because \(W^*W=I\), and its range is exactly that graph. Hence the four entries in the original space are

\[
 \begin{gathered}
 p_{11}=vR_0v^*,\\ p_{12}=vS_0^*,\\
 p_{21}=S_0v^*,\\ p_{22}=I_H-R_1.
 \end{gathered}
 \tag{GP.13}
\]

Each entry is an everywhere defined bounded map \(H\to H\). Moreover \(S_0^*=T_0^*R_1\), with the domains justified in GP03. The first coordinate vanishes on \(K^\perp\), as a graph with first coordinate in \(K\) requires. We have not extended \(T\) by zero to a larger domain; such an extension would change its graph and its graph projection.

The theorem of GP01 applies to (GP.13) unchanged. Affiliation also forces the domain-closure projection \(vv^*\) to belong to \(M\): every unitary of \(M'\) preserves \(D(T)\), hence its closure \(K\), so its orthogonal projection commutes with all those unitaries. BK08 and BK02 again put it in \(M\). This does not assert that the domain itself is closed or all of \(K\).

If \(D(T)=\{0\}\), then \(K=0\), \(T_0^*\) is the zero map on all of \(H\) with target zero, \(R_1=I_H\), and (GP.13) gives \(p_T=0\). The zero Hilbert space also satisfies all formulas. Thus the reduction includes both degenerate cases and returns the operator on its original specified domain.

## Examples that test domains and off-diagonal information

**An unbounded diagonal operator.** On \(H=\ell^2(\mathbb N)\), with indices starting at one, set

\[
 \begin{gathered}
 D(T)=\{x:\sum_{n\geq1}n^2|x_n|^2<\infty\},\\
 (Tx)_n=in x_n.
 \end{gathered}
\]

Finite sequences show density. If \(x^{(k)}\to x\) and \(Tx^{(k)}\to y\) in \(H\), coordinate convergence gives \(y_n=in x_n\). Since \(y\in H\), the required weighted sum is finite, so \(x\in D(T)\) and \(Tx=y\). Thus \(T\) is closed. Testing the adjoint on coordinate vectors forces \((T^*y)_n=-in y_n\); this vector belongs to \(H\) exactly for \(y\in D(T)\), and Cauchy–Schwarz then verifies the pairing for every \(x\in D(T)\). Consequently \(T^*T=TT^*\) is multiplication by \(n^2\) on the domain where \(\sum_n n^4|x_n|^2<\infty\).

The four entries are diagonal multipliers, with coordinate matrix

\[
 \begin{gathered}
 c_n=(1+n^2)^{-1},\\
 c_n\begin{pmatrix}1&-in\\ in&n^2\end{pmatrix}.
 \end{gathered}
 \tag{GP.14}
\]

Their coefficients are bounded. The range of multiplication by \((1+n^2)^{-1}\) is exactly the stated domain of \(T^*T\): one implication follows from \(n^4/(1+n^2)^2\leq1\); for the other, multiply a domain vector by \(1+n^2\) and use \((1+n^2)^2\leq4n^4\). The bounded diagonal algebra is a von Neumann algebra by CY05. GP01 therefore proves affiliation. This example also shows that the bars in (GP.11) can matter: the original domain of \(RT^*\) is a proper dense subspace of \(H\), while its closure is everywhere defined.

**Diagonal resolvents do not suffice.** On \(\mathbb C^2\), let \(M\) be the diagonal algebra and let

\[
 T=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]

Direct multiplication gives \(T^*T=\operatorname{diag}(0,1)\) and \(TT^*=\operatorname{diag}(1,0)\). Thus

\[
 \begin{gathered}
 R=\operatorname{diag}(1,\tfrac12),\\
 R'=\operatorname{diag}(\tfrac12,1),\\
 S=\begin{pmatrix}0&\tfrac12\\0&0\end{pmatrix}.
 \end{gathered}
 \tag{GP.15}
\]

Both resolvents and both diagonal entries of \(p_T\) lie in \(M\), but \(S\notin M\). Hence \(T\) is not affiliated with \(M\). One can check the failure directly with \(u=\operatorname{diag}(1,-1)\in M'\): \(uT\ne Tu\). The off-diagonal graph entries carry information lost by the two positive operators \(T^*T\) and \(TT^*\).

**A domain alone can prevent affiliation.** Let \(K\) be a proper nonzero closed subspace of \(H\), and let \(T\) be zero with domain \(K\). Its graph is \(K\oplus0\), so \(p_T=\operatorname{diag}(p_K,0)\). GP01 says that \(T\) is affiliated with \(M\) exactly when \(p_K\in M\). In particular it is not affiliated with the scalar algebra, whose only projections are \(0,I_H\). The zero operator on **all** of \(H\) is affiliated with every unital von Neumann algebra. Identical values on a smaller domain therefore do not determine identical affiliation behavior.

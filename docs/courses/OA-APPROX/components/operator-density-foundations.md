# Operator density from finite vector tests

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original text and embedded diagram: public domain (CC0).*

A strong operator neighbourhood asks for good approximation on finitely many vectors. Commutants turn those finite tests into one invariant-subspace problem. A rational function then converts self-adjoint approximants into contractions. These two constructions prove the positive matrix density needed to reconstruct completely positive maps with values in a C*-algebra.

We use the complete [Hilbert-space, projection and series-vector proofs H00–H03](../src/regular-group-operator-foundations.md#h00), their [arbitrary-Hilbert-space identification P00](../src/tracial-adjoints-and-rational-matrix-models.md#p00), C*-unitization, calculus and approximate identities F02–F09, and [real convex separation SEP](../src/hypertraces-finite-injectivity.md#separation). The C*-norm and order on finite matrices, including entrywise representations, are proved in [Completely positive maps, Section 2](../../foundations-of-von-neumann-algebras/completely-positive-maps.html#oa-fnd-cm-02). Inner products are linear in their second variable. No separability assumption is imposed.

For a representation \(\pi:A\to B(H)\), put
\[
D=\pi(A),\qquad K=\overline{D H},\qquad P=P_K.
\]
The notation \(\overline{D H}\) means the closed linear span. We work on \(K\), and extend operators on \(K\) by zero on \(K^\perp\) whenever the original space \(H\) is used. Write
\[
M=(D|_K)'',
\]
where these commutants are taken in \(B(K)\). The unit of this algebra on \(H\) is \(P\). When \(K=0\), all supported operators and all the approximations below are zero.

<a id="odf01"></a>
## ODF01. Bounded strong limits and ultraweak tests

Strong convergence means \(T_i\xi\to T\xi\) in norm for every vector \(\xi\). Weak operator convergence means convergence of every scalar \(\langle\eta,T_i\xi\rangle\). Strong* convergence means that both \(T_i\to T\) and \(T_i^*\to T^*\) strongly. H03 describes the ultraweak topology by the functionals
\[
T\longmapsto\sum_{j=1}^{\infty}\langle\eta_j,T\xi_j\rangle,
\qquad \sum_j\|\eta_j\|\|\xi_j\|<\infty.
\tag{ODF1}
\]
P00 makes that description available on every Hilbert space, including spaces with uncountable orthonormal bases.

**Bounded product lemma.** If \(S_i\to S\) and \(T_i\to T\) strongly and \(\sup_i\|S_i\|\le C<\infty\), then \(S_iT_i\to ST\) strongly.

**Proof.** For each \(\xi\),
\[
\|(S_iT_i-ST)\xi\|
\le C\|(T_i-T)\xi\|+\|(S_i-S)T\xi\|\longrightarrow0.
\]
The last vector \(T\xi\) is fixed. No bound on the norms of the \(T_i\) is needed for this assertion. If both nets and their adjoints converge strongly and both nets have uniform norm bounds, applying the same argument to \(T_i^*S_i^*\) also proves strong* convergence of the products. \(\square\)

**Bounded topology lemma.** If \(T_i\to T\) in the weak operator topology and \(\sup_i\|T_i\|\le C\), then \(T_i\to T\) ultraweakly. In particular every uniformly bounded strongly convergent net converges ultraweakly.

**Proof.** For unit vectors \(\eta,\xi\), the scalar limit gives \(|\langle\eta,T\xi\rangle|\le C\), and the Hilbert norming formula gives \(\|T\|\le C\). Given (ODF1), its tail after \(N\), evaluated at \(T_i-T\), has modulus at most
\[
2C\sum_{j>N}\|\eta_j\|\|\xi_j\|.
\]
Choose \(N\) to make this small. The initial finite sum tends to zero by weak operator convergence, so the whole series tends to zero. If \(C=0\), every operator involved is zero. This is a net argument: convergence of the finite sum requires only finitely many eventual conditions. \(\square\)

The uniform bounds in these lemmas are hypotheses. Strong convergence of an arbitrary net supplies no uniform operator-norm bound by itself.

<a id="odf02"></a>
## ODF02. The essential representation and its support

Every \(d\in D\) preserves \(K\). Since \(D=D^*\), it also preserves \(K^\perp\). A vector \(\zeta\in K^\perp\) satisfies
\(\langle d^*\eta,\zeta\rangle=0\) for every \(d\in D\), \(\eta\in H\), so \(d\zeta=0\). Thus \(d=PdP\).

Let \((e_\lambda)\) be the positive contractive approximate identity in \(A\) supplied by F09. On a vector \(\pi(a)\eta\),
\[
\pi(e_\lambda)\pi(a)\eta=\pi(e_\lambda a)\eta
\longrightarrow\pi(a)\eta.
\]
F05 gives \(\|\pi(e_\lambda)\|\le1\). Finite sums of these vectors are dense in \(K\); the uniform bound extends convergence to all of \(K\). Every \(\pi(e_\lambda)\) vanishes on \(K^\perp\). Consequently
\[
\pi(e_\lambda)\longrightarrow P\quad\hbox{strongly on }H.
\tag{ODF2}
\]
On \(K\), this is a strongly convergent approximate identity with limit \(1_K\). In particular the restricted representation is nondegenerate. These statements include \(A=0\) and \(\pi=0\).

The supported algebra \(M\), rather than the full bicommutant in a degenerate ambient space, is the closure to be approximated. For example, if \(D=0\) on a nonzero \(H\), its strong closure is zero although its full bicommutant contains \(1_H\).

<a id="odf03"></a>
## ODF03. The bicommutant theorem on finitely many vectors

**Theorem.** On \(K\), \(D\) is strongly dense in \(M=D''\). More precisely, for \(T\in M\), \(\xi_1,\ldots,\xi_r\in K\), and \(\varepsilon>0\), there is \(a\in A\) such that
\[
\sum_{j=1}^r\|(\pi(a)-T)\xi_j\|^2<\varepsilon^2.
\tag{ODF3}
\]

**Proof.** The zero essential space and the assertion with no test vectors are immediate: take \(a=0\). For \(r\ge1\), write \(\boldsymbol\xi=(\xi_1,\ldots,\xi_r)\in K^r\), and consider the closed linear subspace
\[
L=\overline{\{(d\xi_1,\ldots,d\xi_r):d\in D\}}\subset K^r.
\]
It is invariant under every diagonal operator \(\Delta(d)=\operatorname{diag}(d,\ldots,d)\), by multiplication in \(D\). It is reducing, since \(d^*\in D\). Its orthogonal projection \(Q\) therefore commutes with each \(\Delta(d)\), by H01.

Let \(R_j:K\to K^r\) be the coordinate inclusion. The entries \(Q_{ij}=R_i^*QR_j\) are bounded operators, and the equation \(Q\Delta(d)=\Delta(d)Q\) says \(Q_{ij}d=dQ_{ij}\). Hence every \(Q_{ij}\) lies in \(D'\). Since \(T\in D''\), it commutes with every \(Q_{ij}\), and therefore \(\Delta(T)Q=Q\Delta(T)\). Equation (ODF2) puts \(\boldsymbol\xi\) in \(L\). It follows that
\[
\Delta(T)\boldsymbol\xi
=\Delta(T)Q\boldsymbol\xi
=Q\Delta(T)\boldsymbol\xi\in L.
\]
The definition of \(L\) now provides one \(d=\pi(a)\) satisfying (ODF3).

Conversely, \(D''\) is strongly closed and contains \(D\). Indeed, for \(b\in D'\), the equation \(S_ib=bS_i\) passes to a strong limit, since both evaluations use fixed vectors. Thus every strong limit from \(D\) belongs to \(D''\). The two inclusions prove the theorem. \(\square\)

The indices consisting of a finite vector set and a positive error, ordered by enlarging the set and decreasing the error, give a directed set. Choosing one approximant for each such index turns (ODF3) into a strong-convergent net. No countable cofinal family is required.

<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="odf-orbit-title odf-orbit-desc" width="740" height="228" viewBox="0 0 740 228">
<title id="odf-orbit-title">Finite-vector bicommutant approximation</title>
<desc id="odf-orbit-desc">The tuple xi lies in the closed diagonal orbit L. The projection Q onto L commutes with the diagonal operator T because all entries of Q lie in the commutant D prime. Thus the image tuple T xi lies in L and can be approximated by one diagonal action d xi.</desc>
<defs><marker id="odf-orbit-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#345b71"/></marker></defs>
<rect x="1" y="1" width="738" height="226" rx="12" fill="#f7fafc" stroke="#9ab0bd"/>
<rect x="22" y="28" width="208" height="100" rx="8" fill="white" stroke="#486b80"/>
<text x="126" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="17" fill="#193c51">xi = (xi_1, ..., xi_r)</text>
<text x="126" y="89" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#193c51">xi belongs to L</text>
<text x="126" y="113" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#193c51">approximate identity: ODF02</text>
<path d="M235 77H306" stroke="#345b71" stroke-width="2"/><path d="M306 73L314 77L306 81Z" fill="#345b71"/>
<text x="270" y="55" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" fill="#193c51">Delta(T)</text>
<rect x="317" y="28" width="397" height="100" rx="8" fill="white" stroke="#486b80"/>
<text x="516" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="17" fill="#193c51">Delta(T) xi belongs to L</text>
<text x="516" y="89" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#193c51">Q_ij in D'; T in D''</text>
<text x="516" y="113" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" fill="#193c51">Delta(T) Q = Q Delta(T)</text>
<text x="370" y="164" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#193c51">L = closure of {(d xi_1, ..., d xi_r) : d in D}</text>
<text x="370" y="197" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#193c51">One d approximates the entire image tuple: inequality (ODF3).</text>
</svg>

*Figure.* The maps \(\Delta(d),\Delta(T):K^r\to K^r\) and \(Q:K^r\to L\subset K^r\) are the actual operators in the ODF03 proof. The diagram depicts their invariant-subspace mechanism; it asserts no finite-dimensionality of \(K\) or \(L\).

<a id="odf04"></a>
## ODF04. Self-adjoint strong density by real separation

**Lemma.** Every \(y=y^*\in M\) is a strong limit of operators \(\pi(a_i)\) with \(a_i=a_i^*\in A\). Their norms are not asserted bounded.

**Proof.** ODF03 supplies a net \(d_i\in D\) converging strongly to \(y\). Strong convergence implies weak operator convergence. The adjoints converge weakly to \(y\), because
\[
\langle\eta,d_i^*\xi\rangle
=\overline{\langle\xi,d_i\eta\rangle}
\longrightarrow\overline{\langle\xi,y\eta\rangle}
=\langle\eta,y\xi\rangle.
\]
Thus \(h_i=(d_i+d_i^*)/2\) converges weakly to \(y\). Each \(h_i\) has a self-adjoint lift \((a_i+a_i^*)/2\) in \(A\).

Fix \(\xi_1,\ldots,\xi_r\). The real linear map
\[
\Phi(h)=(h\xi_1,\ldots,h\xi_r)
\]
takes the real vector space \(D_h\) into the real Hilbert space underlying \(K^r\). Every continuous real linear functional on that Hilbert space has the form
\(\operatorname{Re}\sum_j\langle\eta_j,v_j\rangle\). To see this from H00, if \(\ell\) is real linear, then \(F(v)=\ell(v)-i\ell(iv)\) is bounded complex linear and has a Hilbert representative; taking its real part recovers \(\ell\).

The weak operator convergence just proved therefore puts \(\Phi(y)\) in the Banach weak closure of \(\Phi(D_h)\). This image is a real linear subspace, hence convex. The real separation proof SEP says that its weak and norm closures agree. Choose \(h\in D_h\) with
\(\sum_j\|(h-y)\xi_j\|^2<\varepsilon^2\).
Directing these choices by finite sets and errors proves strong density. \(\square\)

<a id="odf05"></a>
## ODF05. The rational contraction cutoff

**Resolvent lemma.** If \(b_i=b_i^*\to y=y^*\) strongly, then
\[
(b_i-i1_K)^{-1}\longrightarrow(y-i1_K)^{-1},\qquad
(b_i+i1_K)^{-1}\longrightarrow(y+i1_K)^{-1}
\]
strongly, even when the \(\|b_i\|\) have no uniform bound.

**Proof.** For a self-adjoint bounded operator \(b\),
\[
\|(b\pm i1_K)\xi\|^2=\|b\xi\|^2+\|\xi\|^2.
\]
The operator has closed range and zero kernel. Its adjoint \(b\mp i1_K\) has zero kernel too, so that range is dense and therefore all of \(K\). Its inverse has norm at most one. The elementary inverse identity gives, for \(z=i\) or \(z=-i\),
\[
(b_i-z)^{-1}-(y-z)^{-1}
=(b_i-z)^{-1}(y-b_i)(y-z)^{-1}.
\]
For a fixed \(\xi\), the norm of the right side applied to \(\xi\) is at most
\(\|(y-b_i)(y-z)^{-1}\xi\|\to0\).
The rightmost vector is fixed; the leftmost inverse has its own uniform bound. This proves the lemma without estimating \(\|b_i\|\). \(\square\)

Put
\[
f(t)=\frac{2t}{1+t^2}
=\frac1{t-i}+\frac1{t+i}\quad(t\in\mathbb R).
\tag{ODF4}
\]
It is real, \(f(0)=0\), and \(|f(t)|\le1\), since \(2|t|\le1+t^2\). F06 gives \(f(a)\in A_h\) with \(\|f(a)\|\le1\) for every \(a=a^*\in A\). This assertion uses the forced unitization when necessary, and the vanishing value at zero puts the result back in \(A\). The resolvent lemma and (ODF4) give \(f(b_i)\to f(y)\) strongly.

**Theorem (self-adjoint contraction density).** Every \(h=h^*\in M\) with \(\|h\|\le1\) is a strong* limit of \(\pi(a_i)\), where \(a_i=a_i^*\in A\) and \(\|a_i\|\le1\).

**Proof.** If \(K=0\), take the constant zero net. Otherwise, in \(B(K)\), put
\[
s=(1_K-h^2)^{1/2},\qquad y=h(1_K+s)^{-1}.
\]
These operators belong to \(M\), by its C*-calculus and inverse calculus. They commute, and \(y=y^*\). Indeed \(s\) is obtained by continuous functions of \(h^2\), and \(1_K+s\ge1_K\) is invertible. The identity \(h^2=1_K-s^2\) gives
\[
1_K+y^2
=\big((1_K+s)^2+h^2\big)(1_K+s)^{-2}
=2(1_K+s)^{-1}.
\]
Consequently \(f(y)=2y(1_K+y^2)^{-1}=h\). This includes \(\|h\|=1\).

ODF04 supplies self-adjoint lifts \(c_i\in A_h\) with \(\pi(c_i)\to y\) strongly. Take \(a_i=f(c_i)\). The scalar bound gives \(\|a_i\|\le1\) in \(A\), not just in its represented image. Extending \(\pi\) to the forced unitization on \(K\) sends the new unit to \(1_K\). The extension is a unital *-homomorphism, so it preserves inverses and the rational identity (ODF4); hence
\[
\pi(a_i)=f(\pi(c_i))\longrightarrow f(y)=h.
\]
All these operators are self-adjoint, so this is strong* convergence. \(\square\)

<a id="odf06"></a>
## ODF06. Positive matrices with the same norm bound

**Theorem (positive matrix Kaplansky density).** For every \(n\ge1\) and every \(X\in M_n(M)_+\), there is a net \(C_i\in M_n(A)_+\) such that
\[
\|C_i\|\le\|X\|,\qquad
\pi^{(n)}(C_i)\longrightarrow X
\quad\hbox{strongly* and ultraweakly on }K^n.
\tag{ODF5}
\]
The same convergences hold after extension by zero to \(H^n\).

**Proof.** First identify the strongly generated algebra of \(\pi^{(n)}(M_n(A))\). Its elements have entries in \(D\). The algebra \(M_n(M)\) is strongly closed: a strong limit has entries extracted by the coordinate inclusions and projections, and each limiting entry belongs to \(M\). It contains \(M_n(D)\).

Conversely, let \(Z=[z_{pq}]\in M_n(M)\), and fix finitely many vectors in \(K^n\). For each entry \(z_{pq}\), ODF03 supplies an element of \(D\) approximating that entry on all the finitely many \(q\)-th vector components. If each entry error on each component is less than \(\varepsilon/(n\sqrt n)\), each output row error is less than \(\varepsilon/\sqrt n\), and the full output vector error is less than \(\varepsilon\). Thus \(M_n(D)\) is strongly dense in \(M_n(M)\). Its essential space is \(K^n\): diagonal copies of \(\pi(e_\lambda)\) converge strongly to \(1_{K^n}\). Applying ODF03 to the representation \(\pi^{(n)}\) identifies its bicommutant with \(M_n(M)\).

If \(X=0\), take the constant zero net. Otherwise put \(c=\|X\|>0\), and let \(Z=(X/c)^{1/2}\in M_n(M)\). It is a self-adjoint contraction. Apply ODF05 to the C*-algebra \(M_n(A)\) and its representation \(\pi^{(n)}\). We obtain self-adjoint \(B_i\in M_n(A)\), \(\|B_i\|\le1\), with \(\pi^{(n)}(B_i)\to Z\) strongly. Set
\[
C_i=cB_i^2.
\]
These matrices are positive and satisfy \(\|C_i\|\le c\). ODF01's bounded product estimate gives \(\pi^{(n)}(C_i)\to cZ^2=X\) strongly. The matrices and the target are self-adjoint, so convergence is strong*. Their represented norms are bounded by \(c\), and ODF01 then gives ultraweak convergence.

For extension by zero, a vector of \(H^n\) is tested only through its orthogonal projection onto \(K^n\). This proves strong and strong* convergence on \(H^n\); the same norm bound and ODF01 give ultraweak convergence there. \(\square\)

In particular the positive part of the unit ball of a faithfully represented C*-algebra is strongly and ultraweakly dense in the positive unit ball of its generated von Neumann algebra. The statement for Choi matrices uses (ODF5) with that same finite matrix size.

<a id="odf07"></a>
## ODF07. The entire contraction ball and the closure algebra

Every contraction \(T\in M\) is a strong* limit of \(\pi(a_i)\) with \(\|a_i\|\le1\). To prove this, the self-adjoint matrix
\[
Y=\begin{pmatrix}0&T\\T^*&0\end{pmatrix}\in M_2(M)
\]
has norm \(\|T\|\). Its square is \(\operatorname{diag}(TT^*,T^*T)\), and the C*-identity and the norm of a block diagonal operator prove this equality. Apply ODF05 at matrix size two to obtain self-adjoint contractions
\[
B_i=\begin{pmatrix}b_i&a_i\\a_i^*&d_i\end{pmatrix}\in M_2(A),
\qquad\pi^{(2)}(B_i)\longrightarrow Y\quad\hbox{strongly}.
\]
The matrix norm inequality \(\|a_i\|\le\|B_i\|\le1\) is part of the matrix construction linked above. The two off-diagonal corners give \(\pi(a_i)\to T\) and \(\pi(a_i)^*\to T^*\) strongly. This proves the assertion. The uniformly bounded approximants also converge ultraweakly, by ODF01.

It follows that the strong, strong* and ultraweak closures of \(D\), extended by zero on \(K^\perp\), all equal the supported algebra \(M\). For the reverse inclusion in the ultraweak closure, \(D''\) on \(K\) is ultraweakly closed: for each \(b\in D'\), the equations
\(\langle\eta,(Tb-bT)\xi\rangle=0\)
are differences of one-term functionals (ODF1). On \(H\), the additional equations \(T=PTP\) are also ultraweakly closed by the same one-term tests. The strong* and strong reverse inclusions follow from their fixed-vector versions. On a nondegenerate representation \(K=H\), so each closure is precisely \(\pi(A)''\).

## References

The bicommutant theorem is due to John von Neumann. The finite-vector projection argument and the rational cutoff above give its density consequence and Kaplansky's theorem at the hypotheses stated here.

Irving Kaplansky, [A theorem on rings of operators](https://msp.org/pjm/1951/1-2/pjm-v1-n2-p06-p.pdf), *Pacific Journal of Mathematics* 1 (1951), 227–232. Theorem 1, printed pp.227–231, is the bounded density theorem; Lemmas 1–5, printed pp.228–230, develop the bounded-calculus and Cayley-resolvent method. The real separation, finite amplification and nonunital support arguments needed in this lesson are proved above from the linked programme foundations.

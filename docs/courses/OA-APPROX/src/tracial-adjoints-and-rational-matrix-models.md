# Tracial adjoints and rational matrix models

*Written and revised by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. New original text: public domain (CC0).*

A finite matrix measurement should reproduce the state in which the experiment is performed. Exact state preservation, however, need not recover every observable. We will first build a two-level measurement that preserves all state averages and loses part of an off-diagonal entry. Its failure of recovery will tell us what the general estimate must measure.

The complete-positivity calculations are proved below in [P04](#p04), and the trace Hilbert completion is built in [P05](#p05). [Finite matrix state foundations](../components/finite-matrix-state-foundations.md) recovers a density from its functional and distinguishes that density from the lists of pure states used to prepare it.

For the general recording theorem, \((M,\tau)\) is any von Neumann algebra with a faithful normal tracial state. No factor or separability hypothesis is imposed on \(M\). Write \(\tau_m=\operatorname{Tr}/m\); inner products are linear in the second variable. For a state \(\varphi\), the error norm is
\[
\|x\|_\varphi^\#=\left(\frac{\varphi(x^*x)+\varphi(xx^*)}{2}\right)^{1/2}.
\tag{1}
\]

## Order and Hilbert-space tools

The constructions below use the concrete Hilbert-space and ultraweak-topology proofs in [Regular-group operator foundations, H00–H03](regular-group-operator-foundations.md#h00), and the Banach-algebra and continuous-calculus proofs in Infinite tensor products and their reference states, F01–F08. The following arguments give the particular matrix, positivity and Hilbert-completion consequences needed here. The faithful normal tracial state is a hypothesis throughout.

<a id="p00"></a>

### P00. Hilbert coordinates and finite matrix order

Every Hilbert space, with no separability assumption, admits the coordinate form used in H00 and H03. Choose a maximal orthonormal family by Zorn. Its closed span is the whole space: H01 projects onto that span, and a nonzero orthogonal-complement vector could otherwise be normalized and added. The map from finite coordinate vectors to their finite orthonormal sums is isometric, extends by H00 completeness to the coordinate Hilbert space, and has closed dense image. This identifies the given Hilbert space unitarily with an arbitrary-coordinate \(\ell^2(I)\). The zero space is included. Thus H03's arbitrary-coordinate series-vector topology applies to every concrete representation used below.

On \(H^r\), the operators with entries in a unital norm-closed *-algebra \(A\subset B(H)\) form a norm-closed unital *-algebra \(M_r(A)\). Indeed a norm limit has entries obtained by the bounded coordinate inclusions and projections, and every limiting entry remains in \(A\). H00 gives its C*-identity; F03–F08 therefore apply to its positive elements, square roots and order. This does not invoke a tensor-product norm theorem. A positive block operator is positive exactly when its quadratic form on \(H^r\) is nonnegative, by H02. In particular a column sandwich of a positive block is positive, including rectangular columns: its quadratic form is the original one evaluated on that column.

<a id="p01"></a>

### P01. Positive functionals and tracial products

Let \(\omega\) be a positive linear functional on a unital concrete C*-algebra. Its value on every selfadjoint element is real, since F08 writes that element as a difference of positive elements. Real and imaginary selfadjoint parts consequently give \(\omega(x^*)=\overline{\omega(x)}\). Expanding \(\omega((x+zy)^*(x+zy))\ge0\) proves
\[
|\omega(x^*y)|^2\le\omega(x^*x)\omega(y^*y).
\]
If the second diagonal value is positive, minimize the resulting scalar quadratic in \(z\). If it is zero, an arbitrarily large scalar with the opposite phase to a nonzero mixed term would make the quadratic negative; the mixed term must therefore vanish. F08 gives \(x^*x\le\|x\|^2 1\), whence
\[
|\omega(x)|^2\le\omega(1)\omega(x^*x)
\le\omega(1)^2\|x\|^2.
\]
Thus \(\|\omega\|=\omega(1)\), including the case \(\omega(1)=0\), when \(\omega=0\).

If \(\tau\) is tracial and \(a,b\ge0\), its trace pairing is nonnegative:
\[
\tau(ab)=\tau(a^{1/2}ba^{1/2})\ge0.
\]
The square root is supplied by F06–F08. For block matrices, \(t=\operatorname{Tr}_r\otimes\tau\) is positive, because every diagonal compression of a positive block is positive, and tracial, because
\[
t(XY)=\sum_{a,b}\tau(x_{ab}y_{ba})
=\sum_{a,b}\tau(y_{ba}x_{ab})=t(YX).
\]
Consequently \(t(XZ)\ge0\) for positive blocks \(X,Z\), by the same square-root sandwich. Faithfulness is not required for this product argument.

<a id="p02"></a>

### P02. Normal multiplication and matrix-valued maps

Normality here is continuity for the concrete ultraweak topology of H03. Every continuous linear functional in that topology is a series-vector functional: continuity bounds its value near zero by finitely many such tests; it vanishes on their common kernel by scalar multiplication, hence factors through their finite-dimensional joint image. Extend that linear functional to the finite coordinate space to express it as a finite linear combination of the tests. Concatenating their absolutely summable series gives one series of the same form. Thus this assertion imports no general normal-functional decomposition or trace-class theorem.

Write a normal functional on a concrete algebra as the H03 series
\[
\eta(x)=\sum_j\langle\xi_j,x\eta_j\rangle,
\qquad \sum_j\|\xi_j\|\|\eta_j\|<\infty.
\]
For fixed bounded \(a,b\),
\[
\eta(axb)=\sum_j\langle a^*\xi_j,x b\eta_j\rangle.
\]
The sum of products of the new vector norms is at most \(\|a\|\|b\|\sum_j\|\xi_j\|\|\eta_j\|\). Hence \(x\mapsto axb\) is ultraweakly continuous. In particular \(x\mapsto\tau(xb)\) is normal when \(\tau\) is normal. This uses the given trace's normality, not automatic normality of any abstract functional.

A map into \(M_m\) whose finitely many coordinates are bounded normal functionals is bounded and normal. Boundedness follows from \(\|[a_{ij}]\|\le m\max_{ij}|a_{ij}|\). A linear functional on the finite-dimensional matrix range is a finite linear combination of those coordinates, and hence pulls back to a normal functional. The ultraweak topology of a finite-dimensional matrix algebra is its usual finite-dimensional topology: the matrix entries themselves are one-term series-vector functionals. These observations prove the normality assertion without a theorem about general normal maps.

<a id="p03"></a>

### P03. Matrix densities, diagonalization and the positive dual cone

For a matrix \(A\), if \(\operatorname{Tr}(AY)\) is a real nonnegative number for every positive \(Y\), test \(Y=vv^*\). The quadratic form \(v^*Av\) is then real and nonnegative for every \(v\). It follows that \(A=A^*\): write \(A=B+iC\), with \(B,C\) selfadjoint; \(v^*Cv=0\) for all \(v\), and the tests \(e_i\), \(e_i+e_j\), \(e_i+ie_j\) make every entry of \(C\) zero. The quadratic form criterion in H02 now gives \(A\ge0\). Conversely, P01 proves nonnegativity of the trace pairing of two positive matrices. Thus the matrix positive cone is exactly its positive trace dual cone. Dividing trace by any positive integer does not change this statement.

For completeness, finite selfadjoint matrices diagonalize using the already supplied spectral graph. In positive dimension F03 makes the spectrum nonempty and F04 makes it real. For a spectral value \(\lambda\), the finite matrix \(A-\lambda1\) is not invertible and so has a nonzero kernel, by finite linear algebra. Normalize a kernel vector. Its orthogonal complement is invariant under \(A\), by selfadjointness; induction on dimension gives an orthonormal eigenbasis and a unitary diagonalization. The zero-dimensional induction endpoint is empty. Positivity is equivalent to nonnegative eigenvalues by the quadratic form criterion, and F06's continuous functions act on this diagonalization by their scalar values. In particular a positive matrix with zero kernel has a strictly positive smallest eigenvalue and bounded inverse, inverse square root and fourth roots.

For any linear functional \(\varphi\) on \(M_m\), the unique matrix representing it is
\[
h_{ij}=m\varphi(e_{ji}),\qquad \varphi(y)=\tau_m(hy).
\]
The coordinate identity is obtained by expanding \(y\) in matrix units. If \(\varphi\) is positive, then \(v^*hv=m\varphi(vv^*)\ge0\), so \(h\ge0\) by the preceding dual-cone test. Conversely \(h\ge0\) gives a positive functional by P01. The unit condition is \(\tau_m(h)=1\).

This state is faithful precisely when \(h\) is invertible. A nonzero kernel projection \(p\) gives \(\varphi(p)=0\). Conversely, if \(h\ge\delta1\), \(\delta>0\), then for \(y\ge0\)
\[
\varphi(y)=\tau_m(hy)\ge\delta\tau_m(y),
\qquad \tau_m(y)=m^{-1}\sum_i\|y^{1/2}e_i\|^2.
\]
The last quantity vanishes only for \(y=0\). A density's diagonalization also gives its vector-state mixture \(\varphi(y)=\sum_i(\lambda_i/m)\langle v_i,yv_i\rangle\), with nonnegative weights summing to one. The density is uniquely fixed by the state even though different vector families may describe the same state; for example the normalized trace on \(M_2\) is the equal mixture in either the standard basis or the basis \((e_1\pm e_2)/\sqrt2\). No mixture classification is needed by the three tracial-adjoint results.

<a id="p04"></a>

### P04. The needed complete-positivity rules and Schwarz

A linear map is completely positive when each of its entrywise matrix amplifications preserves positive block operators. Positive linear maps preserve adjoints: a selfadjoint input is a difference of positive inputs by F08, and real and imaginary parts give the general assertion.

For a fixed rectangular bounded operator \(V\), the map \(x\mapsto V^*xV\) is completely positive. At size \(r\) its image of a positive block \(X\) is the sandwich by the block-diagonal operator with \(r\) copies of \(V\), positive by P00. Finite sums of such sandwiches are therefore completely positive, and are unital exactly when \(\sum V_i^*V_i\) is the identity on their common domain, the unit of the target algebra. Compositions of completely positive maps are completely positive, since their amplifications compose. Unitary conjugations and compressions to finite-dimensional corners are particular sandwiches. The map \(x\mapsto x\otimes1_p\) is completely positive as well: after reordering the finite coordinate factors, every amplification is a direct sum of \(p\) copies of the original positive block. Compression to a corner takes the corner projection, rather than the full ambient identity, as its unit.

If \(\Phi\) is unital and completely positive, apply its size-two amplification to the positive Gram block
\[
\begin{pmatrix}x^*x&x^*\\x&1\end{pmatrix}
=\begin{pmatrix}x^*\\1\end{pmatrix}\begin{pmatrix}x&1\end{pmatrix}.
\]
Its image is \(\left[\begin{smallmatrix}\Phi(x^*x)&\Phi(x)^*\\\Phi(x)&1\end{smallmatrix}\right]\). Sandwich by the column \(\left[\begin{smallmatrix}1\\-\Phi(x)\end{smallmatrix}\right]\) to obtain
\[
\Phi(x)^*\Phi(x)\le\Phi(x^*x).
\tag{P04-Schwarz}
\]
The block positivity and sandwich are P00; no dilation theorem is used. Positivity also preserves \(x^*x\le\|x\|^2 1\). Thus F08 and the C*-identity give \(\|\Phi(x)\|\le\|x\|\). Evaluating at the unit gives its norm one for a nonzero target algebra, as in every application here. A zero target gives the zero map with norm zero. This proves every CP, Schwarz and unit-norm fact needed by the lesson.

For the Gram coefficients in Exercise 7, write \(\eta_i(r)\) for the coordinates of its finite vectors and put \(D_r=\operatorname{diag}(\eta_i(r))\). Then
\[
\sum_rD_r^*xD_r\quad\hbox{has entry}\quad
\Bigl(\sum_r\overline{\eta_i(r)}\eta_j(r)\Bigr)x_{ij}
=\langle\eta_i,\eta_j\rangle x_{ij}.
\]
If every \(\eta_i\) is a unit vector, \(\sum_rD_r^*D_r=1\). This directly proves the stated ucp Schur multiplier; the Schur-product theorem is unnecessary.

<a id="p05"></a>

### P05. The trace Hilbert completion

For the hypothesized faithful tracial state \(\tau\), put \(\langle x,y\rangle_\tau=\tau(x^*y)\). P01 makes this a sesquilinear positive form and supplies Cauchy–Schwarz. Faithfulness makes it positive definite. Its associated norm satisfies the triangle inequality by Cauchy–Schwarz.

Complete this normed space by the F01 Cauchy-sequence construction: identify two norm-Cauchy sequences when their difference tends to zero, and define their inner product by \(\lim_n\tau(x_n^*y_n)\). That limit exists by Cauchy–Schwarz and boundedness of the two sequences. The definition is independent of representatives, extends the original inner product and is positive definite on the quotient. Completeness can be seen directly: from a Cauchy sequence of quotient vectors choose a subsequence with successive distances below \(2^{-j}\), approximate its \(j\)-th term by an original algebra element within \(2^{-j}\), and use the resulting Cauchy sequence of algebra elements as the limit. The Cauchy property gives the same limit for the entire original sequence. This is \(L^2(M,\tau)\), and the image of \(M\), the bounded elements, is dense by construction.

Left multiplication by \(a\in M\) is bounded on this completion, since F08 gives
\[
\|ax\|_2^2=\tau(x^*a^*ax)\le\|a\|^2\tau(x^*x).
\]
Traciality makes \(Jx=x^*\) a conjugate-linear isometry, because \(\tau(xx^*)=\tau(x^*x)\). It extends to the completion, squares to the identity, and right multiplication by \(a\) is \(J L_{a^*}J\), also bounded by \(\|a\|\). These bounded extensions need no assertion that the trace representation has a normally closed range.

If \(h>0\) is a matrix density, the weighted form
\[
\langle a,b\rangle_h=\tau_m(h^{1/2}a^*h^{1/2}b)
\]
is the ordinary Hilbert–Schmidt form of \(h^{1/4}ah^{1/4}\) and \(h^{1/4}bh^{1/4}\), by cyclicity. The change of variables is invertible by P03, so the form is positive definite. Its finite-dimensional completion is the same vector space. This also supplies all of Exercise 3.

<a id="p06"></a>

### P06. Finite-source adjoints and the exact \(TT^*\) norm

Let \(E\) be any finite-dimensional Hilbert space with orthonormal basis \(b_1,\ldots,b_d\), and let \(A:E\to K\) be linear, where \(K\) is a Hilbert space. This map is bounded before any contraction conclusion is drawn:
\[
\|Au\|\le\Bigl(\sum_i\|Ab_i\|^2\Bigr)^{1/2}\|u\|.
\]
Define
\[
A^*v=\sum_i\langle Ab_i,v\rangle b_i.
\]
The finite expansion proves \(\langle Au,v\rangle=\langle u,A^*v\rangle\), uniqueness, and boundedness of the adjoint. Norming a Hilbert vector by its inner product with unit vectors (take that vector divided by its norm when nonzero) gives \(\|A^*\|=\|A\|\). The inequalities
\[
\|AA^*\|\le\|A\|\|A^*\|=\|A\|^2,
\qquad
\|A^*v\|^2=\langle v,AA^*v\rangle\le\|AA^*\|\|v\|^2
\]
therefore give \(\|AA^*\|=\|A\|^2\). The argument also covers the zero operator and the zero-dimensional source. It does not require a spectral theorem for operators on \(K\). H00 gives the same identity for arbitrary bounded Hilbert operators, after P00 identifies their spaces with coordinate spaces, but the finite-source proof alone suffices here.

If a bounded operator on \(K\) satisfies a contraction estimate on a dense subspace, norm continuity gives the estimate on all of \(K\). Equivalently, a linear contraction defined on that dense subspace has a unique contraction extension: images of Cauchy approximants are Cauchy, and their limits are independent of the approximants.

## 0. A measurement that preserves the state but loses coherence

Let \(\varphi(x)=\tfrac13x_{11}+\tfrac23x_{22}\) on \(M_2\). Its density relative to \(\tau_2\) is \(h=\operatorname{diag}(2/3,4/3)\). Give the second coordinate two slots and the first coordinate one slot in a three-dimensional record:
\[
R\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}a&b&0\\c&d&0\\0&0&d\end{pmatrix}.
\]
\[
L(Y)=\begin{pmatrix}
Y_{11}&Y_{12}/\sqrt2\\
Y_{21}/\sqrt2&(Y_{22}+Y_{33})/2
\end{pmatrix}.
\]
These formulas define ucp maps \(R:M_2\to M_3\) and \(L:M_3\to M_2\). To check this before any general adjoint theorem, write \(R(x)=W_1^*xW_1+W_2^*xW_2\), where
\[
W_1=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},
\qquad W_2=\begin{pmatrix}0&0&0\\0&0&1\end{pmatrix}.
\]
Similarly \(L(Y)=K_1^*YK_1+K_2^*YK_2\), where
\[
K_1=\begin{pmatrix}1&0\\0&1/\sqrt2\\0&0\end{pmatrix},
\qquad K_2=\begin{pmatrix}0&0\\0&0\\0&1/\sqrt2\end{pmatrix}.
\]
Each sandwich is completely positive at every matrix level. The sums \(\sum W_i^*W_i=1_3\) and \(\sum K_i^*K_i=1_2\) prove unitality. On diagonal entries the formulas give
\[
\tau_3R=\varphi,\qquad \varphi L=\tau_3.
\]
Thus both directions preserve their specified states, and the composite preserves \(\varphi\). Nevertheless
\[
LR\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}a&b/\sqrt2\\c/\sqrt2&d\end{pmatrix}.
\]
Diagonal observations are recovered exactly. An off-diagonal observation is reduced by \(1/\sqrt2\). State preservation sees the diagonal probabilities but does not force recovery of the other entries. The next two diagnostics quantify this loss.

**Exercise 5.** Take \(m=2\), \(h=\operatorname{diag}(2/3,4/3)\). Find \(p_1,p_2,q\) and the coefficient on \(e_{12}\).

*Solution.* The state weights are the density eigenvalues divided by \(m\), hence \(1/3,2/3\). Choose \(p_1=1,p_2=2,q=3\); then \(mp_i/q\) are the two eigenvalues. The explicit matrices above give \(LR(e_{12})=e_{12}/\sqrt2\), while both diagonal matrix units are fixed. The different coordinate multiplicities damp this off-diagonal entry.

**Exercise 6.** Verify both sides of the commutator error bound for the matrix unit in Exercise 5.

*Solution.* Put \(d=1-1/\sqrt2\). The error is \(-d e_{12}\), so its symmetrized state norm squared is
\[
\frac{d^2}{2}\bigl(\varphi(e_{22})+\varphi(e_{11})\bigr)
=\frac{(1-1/\sqrt2)^2}{2}.
\]
The commutator is \((\sqrt{2/3}-\sqrt{4/3})e_{12}\). Its normalized Hilbert–Schmidt square is \((\sqrt2-1)^2/3\). The error square is \((\sqrt2-1)^2/4\), giving the ratio \(3/4\). Thus the bound holds strictly in this example. These are direct calculations of the two norms; the general theorem has not been used.

## 1. The trace adjoint stays completely positive

The reverse map should match the trace pairing of the forward map. This determines an ordinary trace adjoint, but that adjoint has value \(h\) at the identity, rather than \(1\). Two-sided density normalization is therefore a mathematical requirement.

In the preceding laboratory,
\[
R^\sharp(Y)=\frac23
\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}+Y_{33}\end{pmatrix}.
\]
\[
R^\sharp(1_3)=h.
\]
Multiplying only on the left by \(h^{-1}\) would make the value at the identity correct but would destroy positivity. For example, the positive matrix with a \(2\)-by-\(2\) all-ones upper block and zero third row and column would map to
\[
\begin{pmatrix}1&1\\1/2&1/2\end{pmatrix},
\]
which is not self-adjoint. Sandwiching with \(h^{-1/2}\) instead gives exactly the ucp map \(L\) written above. We now justify that normalization for an arbitrary faithfully tracial algebra.

**Lemma 1.1.** If \(T:M_m\to M\) is cp, there is a unique normal cp map \(T^\sharp:M\to M_m\) satisfying
\[
\tau_m(T^\sharp(x)y)=\tau(xT(y))\qquad(x\in M,\ y\in M_m).
\tag{2}
\]

**Proof.** The required pairing specifies every entry:
\[
T^\sharp(x)_{ij}=m\tau\bigl(xT(e_{ji})\bigr).
\]
These entries are bounded normal functionals of \(x\). They therefore define a bounded normal linear map, and the matrix-unit pairing proves (2) and uniqueness.

To check positivity at every size, fix \(r\), put \(t=\operatorname{Tr}_r\otimes\tau\), and let \(X=[x_{ab}]\ge0\) in \(M_r(M)\). For each \(Y=[y_{ab}]\ge0\) in \(M_r(M_m)\), summing (2) over the diagonal of a product gives
\[
(\operatorname{Tr}_r\otimes\tau_m)
 \bigl([T^\sharp(x_{ab})]Y\bigr)
=t\bigl(X[T(y_{ab})]\bigr)\ge0.
\tag{3}
\]
Complete positivity of \(T\) makes \([T(y_{ab})]\) positive. Traciality changes the product on the right into the positive sandwich by \(X^{1/2}\). On the finite matrix algebra, an element having nonnegative trace pairing with every positive \(Y\) is positive: tests against all rank-one projections give a nonnegative quadratic form. Thus \([T^\sharp(x_{ab})]\ge0\). The arbitrary size \(r\) proves complete positivity. Only a faithful normal trace on \(M\) has been used. \(\square\)

**Exercise 1.** Give the coordinate formula for the trace adjoint in (2).

*Solution.* Pair with \(y=e_{ij}\). Since \(\tau_m(Ae_{ij})=A_{ji}/m\), equation (2) gives \(T^\sharp(x)_{ji}=m\tau(xT(e_{ij}))\). Each entry is normal and bounded. These coordinates also show uniqueness and linearity directly.

<a id="weighted-adjoint-mechanism"></a>

<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560">
<title>The weighted Hilbert adjoint and the improved norm bound</title>
<desc>T maps the weighted finite matrix Hilbert space to the trace Hilbert completion. S is its Hilbert adjoint. Schwarz and exact trace preservation bound TS=TT*, giving the improved norm of T.</desc>
<rect width="1000" height="560" fill="#fbfcff"/>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#304d73"/></marker></defs>
<text x="500" y="38.84" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="26" fill="#182b45">The weighted-adjoint norm mechanism</text>
<rect x="40" y="75" width="350" height="125" rx="12" fill="#eef4fc" stroke="#304d73" stroke-width="2"/>
<rect x="610" y="75" width="350" height="125" rx="12" fill="#eef4fc" stroke="#304d73" stroke-width="2"/>
<text x="215" y="119.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">Weighted matrix Hilbert space</text>
<text x="215" y="164.8" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="20" fill="#182b45">Hh = (Mm, ⟨·,·⟩h)</text>
<text x="785" y="119.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">Trace Hilbert completion</text>
<text x="785" y="164.8" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="20" fill="#182b45">K = L²(M, τ)</text>
<polyline points="400,105 600,105" fill="none" stroke="#304d73" stroke-width="3" marker-end="url(#arrow)"/>
<text x="500" y="90.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">T</text>
<polyline points="600,168 400,168" fill="none" stroke="#304d73" stroke-width="3" marker-end="url(#arrow)"/>
<text x="500" y="152.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">S = T*</text>
<rect x="150" y="280" width="700" height="110" rx="12" fill="#eef4fc" stroke="#304d73" stroke-width="2"/>
<text x="500" y="322.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">TS = TT* acts on K</text>
<text x="500" y="362.8" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="20" fill="#182b45">ucp Schwarz and τ TS = τ give ‖TS‖ ≤ 1</text>
<polyline points="785,211 785,270" fill="none" stroke="#304d73" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="190" y="455" width="620" height="75" rx="12" fill="#eef4fc" stroke="#304d73" stroke-width="2"/>
<text x="500" y="489.48" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="22" fill="#182b45">‖T‖² = ‖TT*‖ ≤ 1</text>
<text x="500" y="517.12" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="18" fill="#182b45">Improved weighted estimate (6)</text>
<polyline points="500,400 500,445" fill="none" stroke="#304d73" stroke-width="3" marker-end="url(#arrow)"/>
<text x="500" y="241.12" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="18" fill="#182b45">T is bounded first by its finite-source basis estimate.</text>
<text x="270" y="428.12" text-anchor="middle" font-family="Segoe UI Symbol, sans-serif" font-size="18" fill="#182b45">The exact Hilbert norm identity is P06.</text>
</svg>

Theorem 2.1 views the recording map between two Hilbert spaces. Its backward map is the Hilbert adjoint. Schwarz and trace preservation bound their composite on the trace completion; [P06](#p06) then gives the improved bound on the recording map. The two Hilbert spaces and each arrow's domain are shown above.

**Exercise 2.** Why does faithfulness on positive elements imply that \(h\) is invertible?

*Solution.* If the positive density had a nonzero kernel projection \(p\), then \(0=\tau_m(hp)=\tau(T(p))\). The operator \(T(p)\) is positive, and faithfulness of \(\tau\) gives \(T(p)=0\). Faithfulness of \(T\) gives \(p=0\), a contradiction. A positive matrix with zero kernel has a strictly positive minimum eigenvalue, hence an inverse.

## 2. The weighted recording map

The matrix state attached to a reconstruction \(T\) is \(\varphi=\tau T\). If \(T\) loses no positive element, this state assigns a strictly positive weight in every matrix direction. Its inverse square root can then turn the trace adjoint into a unital recording map.

**Theorem 2.1.** Suppose \(T:M_m\to M\) is unital, completely positive and faithful on positive elements. Put \(\varphi=\tau T\), and write \(\varphi(y)=\tau_m(hy)\). Then \(h>0\) is invertible, \(\tau_m(h)=1\), and
\[
S(x)=h^{-1/2}T^\sharp(x)h^{-1/2}
\tag{4}
\]
is the unique ucp map satisfying
\[
\tau_m(h^{1/2}S(x)h^{1/2}y)=\tau(xT(y)).
\tag{5}
\]
It is normal and \(\varphi S=\tau\). Moreover
\[
\|T(y)\|_2^2\le
\tau_m(h^{1/2}y^*h^{1/2}y).
\tag{6}
\]

**Proof.** The state \(\tau T\) is faithful: if \(y\ge0\) and \(\tau(T(y))=0\), faithfulness of the trace gives \(T(y)=0\), and faithfulness of \(T\) then gives \(y=0\). Its matrix density is consequently invertible. Normalization follows from \(T(1)=1\).

By (2), \(T^\sharp(1)=h\). The sandwich in (4) is therefore normal, completely positive and unital. Substitution proves (5). Conversely (5) determines \(h^{1/2}S(x)h^{1/2}\), and hence \(S(x)\), by the nondegenerate matrix trace pairing. Putting \(y=1\) in that identity proves \(\varphi S=\tau\).

For the improved estimate, equip \(M_m\) with
\[
\langle a,b\rangle_h=
\tau_m(h^{1/2}a^*h^{1/2}b).
\tag{7}
\]
This is the Hilbert–Schmidt inner product of \(h^{1/4}a h^{1/4}\) and \(h^{1/4}b h^{1/4}\). The invertible change of variables makes it positive definite. Consider \(T\) as an operator from this finite-dimensional Hilbert space into \(L^2(M,\tau)\). In (5), replace \(y\) by \(y^*\) and use traciality. The result is
\[
\langle T(y),x\rangle_\tau=\langle y,S(x)\rangle_h.
\]
Thus the Hilbert adjoint of \(T\), restricted to bounded \(x\), is \(S\). Each coordinate is an \(L^2\)-continuous pairing with a fixed \(T(e_{ij})\); these coordinates extend \(S\) to all of \(L^2(M,\tau)\).

The composite \(TS\) is unital, completely positive and trace-preserving. Schwarz gives
\[
\|TS(x)\|_2^2\le\tau(TS(x^*x))=\|x\|_2^2.
\]
Density of bounded elements extends this contraction to the trace Hilbert space. There it equals \(TT^*\), so \(\|T\|^2=\|TT^*\|\le1\). Applied to \(y\), this is exactly (6). Cyclicity gives the equivalent right-hand expression \(\tau_m(h^{1/2}yh^{1/2}y^*)\). No factor or countability condition entered the argument. \(\square\)

The weighted norm in (7) differs from \(\varphi(y^*y)^{1/2}\). The improved bound (6) uses the actual Hilbert adjoint and the trace-preserving composite, rather than just Schwarz for \(T\).

**Exercise 3.** Check the weighted inner product's positivity.

*Solution.* Put \(b=h^{1/4}a h^{1/4}\). Cyclicity gives \(\tau_m(b^*b)=\tau_m(h^{1/2}a^*h^{1/2}a)\). This is nonnegative and vanishes only if \(b=0\). Invertibility of \(h^{1/4}\) then gives \(a=0\). Polarization supplies the Hilbert inner product in (7).

**Exercise 4.** Prove the trace-preserving ucp map \(TS\) is an \(L^2\) contraction.

*Solution.* The ucp Schwarz inequality gives \(TS(x)^*TS(x)\le TS(x^*x)\). Applying \(\tau\) and using \(\tau TS=\varphi S=\tau\) gives \(\|TS(x)\|_2^2\le\|x\|_2^2\). Bounded elements are dense in \(L^2\), so this inequality defines the unique contraction extension.

## 3. Rational densities become matrix dimensions

The laboratory replaced probabilities \(1/3,2/3\) by one slot and two slots. For an arbitrary rational faithful density, the probability of the \(i\)-th eigenvector is \(\lambda_i/m\). Writing it as \(p_i/q\) assigns \(p_i\) slots to that coordinate. The resulting record has ordinary trace \(\tau_q\); the weighted adjoint returns to the original state.

This is not generally an algebra embedding: two coordinates may have different numbers of slots. Their overlap will determine the off-diagonal recovery coefficient. The full theorem states both the exact state identities and the error that remains.

**Theorem 3.1.** Suppose \(h>0\), \(\tau_m(h)=1\), and its eigenvalues are rational. There exist ucp maps
\[
M_m\xrightarrow{R}M_q\xrightarrow{L}M_m
\]
such that
\[
\tau_qR=\varphi,\qquad \varphi L=\tau_q,\qquad
\|LR(x)-x\|_\varphi^\#\le\|h^{1/2}x-xh^{1/2}\|_{2,\tau_m}.
\tag{8}
\]

**Proof.** Diagonalize \(h\), and write its eigenvalues as
\[
\lambda_i=mp_i/q,\quad p_i\in\mathbb N,\quad q=\sum_i p_i.
\tag{9}
\]
Use a record space \(K=\bigoplus_i\mathbb C^{p_i}\), with orthonormal vectors \(\xi_{i,s}\), \(1\le s\le p_i\). Let \(p=\max_i p_i\). For \(1\le r\le p\), define operators \(A_r:K\to\mathbb C^m\) and \(B_r:\mathbb C^m\to K\) by
\[
\begin{aligned}
A_r\xi_{i,s}&=\begin{cases}e_i,&s=r,\\0,&s\ne r,\end{cases}\\
B_r e_i&=\begin{cases}p_i^{-1/2}\xi_{i,r},&r\le p_i,\\0,&r>p_i.\end{cases}
\end{aligned}
\]
Set \(R(x)=\sum_r A_r^*xA_r\) and \(L(Y)=\sum_r B_r^*YB_r\). These finite Kraus sums are completely positive. Each vector \(\xi_{i,s}\) occurs once in \(\sum_r A_r^*A_r\), and each \(e_i\) occurs \(p_i\) times with weight \(1/p_i\) in \(\sum_r B_r^*B_r\). Both sums are the respective identity operators, proving unitality directly.

The diagonal of \(R(x)\) repeats \(x_{ii}\) exactly \(p_i\) times. Hence \(\tau_qR(x)=q^{-1}\sum_i p_i x_{ii}=\varphi(x)\). The diagonal of \(L(Y)\) averages the entries in the \(i\)-th record block. Weighting that average by \(p_i/q\) gives every record diagonal entry weight \(1/q\), so \(\varphi L(Y)=\tau_q(Y)\).

This record also has the corner realization used in the exercises. Put \(P_i\) equal to the projection onto the first \(p_i\) vectors of \(\mathbb C^p\), and identify \(K\) with the range of \(F=\sum_i e_{ii}\otimes P_i\). Then
\[
R(x)=F(x\otimes1_p)F.
\tag{10}
\]
Let \(f_{ij}=R(e_{ij})\). Its only nonzero block pairs \(\xi_{j,r}\) with \(\xi_{i,r}\) for \(r\le\min(p_i,p_j)\). The Kraus formula for \(L\) therefore gives
\[
\begin{gathered}
L(Y)_{ij}=\frac{\operatorname{Tr}_q(Yf_{ij}^*)}{\sqrt{p_ip_j}},\\
LR(e_{ij})=c_{ij}e_{ij},\qquad
c_{ij}=\frac{\min(p_i,p_j)}{\sqrt{p_ip_j}}.
\end{gathered}
\tag{11}
\]
Here \(\operatorname{Tr}_q\) is unnormalized. The same coordinate formula verifies the weighted pairing (5), so this explicit \(L\) agrees with the unique weighted adjoint. Its complete positivity and the state identities have already been proved without invoking that theorem.

The symmetrized state norm of a matrix is
\[
\|a\|_\varphi^{\#\,2}=\frac1{2q}\sum_{i,j}(p_i+p_j)|a_{ij}|^2.
\tag{12}
\]
For \(p_i\le p_j\), the coefficient error satisfies
\[
\begin{aligned}
(p_i+p_j)(1-c_{ij})^2
&=\frac{p_i+p_j}{p_j}(\sqrt{p_j}-\sqrt{p_i})^2\\
&\le2(\sqrt{p_j}-\sqrt{p_i})^2.
\end{aligned}
\]
Exchange \(i,j\) for the other ordering. Substitution into (12) gives
\[
\begin{aligned}
\|LR(x)-x\|_\varphi^{\#\,2}
&\le\frac1q\sum_{i,j}(\sqrt{p_i}-\sqrt{p_j})^2|x_{ij}|^2\\
&=\|[h^{1/2},x]\|_{2,\tau_m}^2.
\end{aligned}
\tag{13}
\]
This proves (8) for diagonal \(h\). If \(h=u d u^*\), use \(R_d\operatorname{Ad}(u^*)\) and \(\operatorname{Ad}(u)L_d\). They preserve the required states, and unitary conjugation preserves both norms in (8), proving the full rational-spectrum assertion. \(\square\)

If \(x\) commutes with \(h\), this construction recovers \(x\) exactly. When the density is scalar, all \(p_i\)'s may be chosen equal, and \(LR=\mathrm{id}\).

**Exercise 8.** Explain why the compression (10) is faithful on positive elements, although compression maps need not be faithful in general.

*Solution.* If \(x\ge0\) and \(R(x)=0\), then \(0=\tau_qR(x)=\varphi(x)\). The density \(h\) is invertible, so \(\varphi\) is faithful and \(x=0\). The prescribed positive dimensions in every coordinate supply the property; no assertion is being made about arbitrary compressions.

## 4. Problems with complete solutions

The construction's state identities are exact. Its remaining defect is described by the commutator: recovery is exact on the algebra that does not mix distinct density eigenspaces. The Gram-matrix test below independently checks positivity of the recovery coefficients, and the fixed-algebra and basis-change problems describe what this means for observations in other coordinates.

**Exercise 7.** Prove directly that the coefficient matrix \([c_{ij}]\) is positive.

*Solution.* In \(\mathbb C^p\) set \(\eta_i=p_i^{-1/2}\sum_{r=1}^{p_i}e_r\). Their Gram matrix has entries \(\langle\eta_i,\eta_j\rangle=\min(p_i,p_j)/\sqrt{p_ip_j}=c_{ij}\). Every Gram matrix is positive, and its diagonal is one. Thus the Schur multiplier in (11) is also directly seen to be ucp, by its diagonal-coordinate Kraus decomposition from these vectors.

**Exercise 9.** Determine the matrices fixed by \(LR\).

*Solution.* Formula (11) shows \(c_{ij}=1\) exactly when \(p_i=p_j\). Every entry between distinct eigenvalues is multiplied by a number strictly below one. Hence the fixed matrices are precisely the blocks within equal-eigenvalue spaces, which are exactly the matrices commuting with \(h\). This also follows in one direction from the zero commutator in (8).

**Exercise 10.** How does the construction change after diagonalizing a general rational-spectrum density?

*Solution.* If \(h=u d u^*\), perform the construction for \(d\), giving \(R_d,L_d\). Put \(R_h=R_d\operatorname{Ad}(u^*)\) and \(L_h=\operatorname{Ad}(u)L_d\). These are ucp. The two state identities follow by the invariance of normalized trace under unitary conjugation. Conjugating the composite error and the square-root commutator by \(u^*\) gives the same two norms as for \(d\), so (8) is retained.

## References and proof scope

The weighted Hilbert-adjoint argument and rational integer-slot record go back to Uffe Haagerup. Xiaoyan Zhou and Junsheng Fang give a freely readable account in [*A note on relative amenability of finite von Neumann algebras*](https://jot.theta.ro/jot/archive/2019-081-001/2019-081-001-005.pdf), *Journal of Operator Theory* 81:1 (2019), 107–132: Lemma 3.5, pp. 120–122, and Lemma 3.6, pp. 122–125. Their auxiliary algebra may be taken to be the scalars, giving the weighted-adjoint and rational-record mechanisms considered here. Matrix-unit coordinates give the trace adjoint directly, and both directions of the rational channel have explicit Kraus sums. The faithful normal tracial state is a hypothesis; no factor or separability assumption is needed.

Continue to Trace-preserving finite models. Its density perturbation changes the actual reconstruction map, its almost-recovered unitaries force the square-root commutator to be small, and Theorem 3.1 above then replaces the matrix state by a normalized trace. [Unitary couplings and finite injective factors](unitary-couplings-and-finite-injective-factors.md) explains the additional step from positive maps to an actual finite-dimensional subalgebra. State-preserving channels alone do not prove that conclusion.

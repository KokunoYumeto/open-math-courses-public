# Projections in the reduced free group algebra

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

The reduced \(C^*\)-algebra \(A=C_r^*(\mathbb F(a,b))\) has only two projections: \(0\) and \(1\). Its von Neumann closure is a factor of type \(\mathrm{II}_1\) with many projections, so the assertion concerns the norm-closed algebra. We prove it by comparing two representations that differ by trace-class operators on a dense algebra.

We use the faithful canonical trace from the [group factor lesson](central-sequences-and-free-group-factors.md) and the [norm-averaging result](free-group-norm-averaging.md). Foundational prerequisites are the compact self-adjoint spectral theorem, trace-class completeness and its two-sided ideal bound, absolute diagonal summation for the trace, and the holomorphic functional calculus with surrounding cycles. The exact foundational proof scopes remain prerequisites; selected free trace-class methods are identified below. The representation comparison, trace-class closure, projection perturbation and integer trace calculation are proved below.

Write \(\Gamma=\mathbb F(a,b)\), \(H=\ell^2(\Gamma)\), \(P\) for the projection onto \(\mathbb C\delta_e\), and \(p=1-P\). Inner products are linear in the second variable.

## 1. Removing the identity from the regular representation

On \(H'=pH\), define two permutations of its basis by
\[
T_s\delta_g=\begin{cases}
\delta_s,&g=s^{-1},\\
\delta_{sg},&g\ne s^{-1},
\end{cases}
\qquad s=a,b,\quad g\ne e.
\tag{1}
\]
The ordinary left translation would send \(\delta_{s^{-1}}\) to the missing vector \(\delta_e\); formula (1) sends it to \(\delta_s\), which had the missing predecessor \(e\). This is a bijection of the remaining basis. Its inverse has the same formula with \(s\) replaced by \(s^{-1}\). The free generators therefore define a unitary representation \(\lambda'\) of \(\Gamma\) on \(H'\).

We need more than a representation of the abstract group: we must show it extends to the reduced norm.

For \(c=a,b\), define a bijection \(\phi_c:\Gamma\to\Gamma_c\), where \(\Gamma_c\) is the set of words ending in \(c\) or \(c^{-1}\), by
\[
\phi_c(w)=\begin{cases}
w,&w\text{ ends in }c^{-1},\\
wc,&\text{otherwise}.
\end{cases}
\tag{2}
\]
In the second case appending \(c\) causes no cancellation. Words ending in \(c^{-1}\) are their own preimage; words ending in \(c\) have preimage obtained by removing their last \(c\). These two rules prove bijectivity.

**Lemma 1.1.** The map
\[
U:H\oplus H\longrightarrow H',
\quad U(\delta_w,0)=\delta_{\phi_a(w)},
\quad U(0,\delta_w)=\delta_{\phi_b(w)}
\tag{3}
\]
is unitary and intertwines \(\lambda\oplus\lambda\) with \(\lambda'\).

**Proof.** The disjoint sets \(\Gamma_a,\Gamma_b\) partition the nonidentity words, so (3) sends an orthonormal basis bijectively onto an orthonormal basis. For each letter \(s=a^{\pm1},b^{\pm1}\), direct reduction gives
\[
T_s\delta_{\phi_c(w)}=\delta_{\phi_c(sw)}.
\tag{4}
\]
Here \(T_{s^{-1}}=T_s^*\). Away from \(w=e\) and \(w=s^{-1}\), multiplication on the left preserves the terminal letter, so (4) is ordinary concatenation and reduction. The exceptional modified step can occur only when \(\phi_c(w)=s^{-1}\), which means \(w=e,s=c^{-1}\), or \(w=c^{-1},s=c\); these are among the two boundary cases. They give respectively \(\phi_c(c^{-1})=c^{-1}\) and \(\phi_c(e)=c\), exactly as (1) requires. In the other boundary cases, cancelling \(s^{-1}\) against \(s\) leaves the appended \(c\), again \(\phi_c(e)\). Thus (4) holds for every letter, and hence every word. \(\square\)

Consequently \(\lambda'\) extends isometrically to a representation of \(A\). On \(H\) let \(\rho(x)\) denote this representation extended by zero on \(\mathbb C\delta_e\). It is a star homomorphism supported on \(p\), with
\[
\rho(1)=p,\qquad \rho(x)P=P\rho(x)=0.
\tag{5}
\]
The original representation is \(\pi(x)=x\). Define
\[
D(x)=\pi(x)-\rho(x).
\tag{6}
\]
In particular \(D(1)=P\), rather than zero.

## 2. Finite differences and a dense algebra

For vectors \(\xi,\eta\), put \(\theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle\). Formula (1), also for inverse letters, gives
\[
D(\lambda_s)
=\theta_{\delta_s,\delta_e}
 +\theta_{\delta_e-\delta_s,\delta_{s^{-1}}}.
\tag{7}
\]
It vanishes on every other basis vector and has rank \(2\). For arbitrary \(x,y\in A\), multiplicativity gives the exact identity
\[
D(xy)=\pi(x)D(y)+D(x)\rho(y),
\qquad D(x^*)=D(x)^*.
\tag{8}
\]
Thus \(D(\lambda_g)\) has finite rank for every group element, by induction on word length; for \(g\ne e\) its rank is at most \(2\ell(g)\).

Let \(\mathcal S_1(H)\) be the trace-class operators and define
\[
A_0=\{x\in A:D(x)\in\mathcal S_1(H)\}.
\tag{9}
\]
Recall the prerequisite inequalities and trace formula:
\[
\|BTC\|_1\le\|B\|\|T\|_1\|C\|,
\qquad |\operatorname{Tr}T|\le\|T\|_1,
\qquad
\operatorname{Tr}T=\sum_g\langle\delta_g,T\delta_g\rangle,
\tag{10}
\]
where the last sum is absolutely convergent.

**Lemma 2.1.** The set \(A_0\) is a norm-dense unital star subalgebra of \(A\). It is complete in the graph norm
\[
\|x\|_{\mathrm{gr}}=\|x\|+\|D(x)\|_1.
\tag{11}
\]

**Proof.** The ideal inequality and (8) give closure under products and adjoints; \(D(1)=P\) is trace class. Finite group polynomials belong to \(A_0\) by (7)–(8), so it is norm dense. Also (8) bounds the graph norm of a product by the product of the graph norms. If \(x_n\) is graph-norm Cauchy, then \(x_n\to x\) in \(A\) and \(D(x_n)\to T\) in trace norm. Since \(D:A\to B(H)\) is operator-norm bounded and trace norm dominates operator norm, \(D(x)=T\). Thus \(x\in A_0\), proving completeness. \(\square\)

Density alone does not show that every element of \(A\) has trace-class difference. We will use a spectral-gap projection construction inside \(A_0\).

## 3. Holomorphic closure with the missing unit retained

**Theorem 3.1.** If \(x\in A_0\) and \(f\) is holomorphic on a neighborhood of \(\operatorname{Sp}_A(x)\), then \(f(x)\in A_0\).

**Proof.** For \(z\notin\operatorname{Sp}_A(x)\), put
\[
R(z)=\pi((z1-x)^{-1}),\qquad
R'(z)=\rho((z1-x)^{-1}).
\]
The latter is the resolvent on \(pH\), extended by zero. Its corner identities are
\[
\rho(x)R'(z)=zR'(z)-p.
\]
Together with \(\pi(x)R(z)=zR(z)-1\), they give
\[
R(z)-R'(z)
=R(z)P+R(z)D(x)R'(z).
\tag{12}
\]
Indeed the second term is \(R(z)p-R'(z)\); adding the first gives the claimed difference. The rank-one term is essential because the representations have different units.

The right side is trace class by (10), and is continuous in trace norm along every compact resolvent contour. Let \(\mathcal C\) be a surrounding cycle within the domain of \(f\). Computing the functional calculus in \(B(H)\) and in the unital corner \(B(pH)\) gives
\[
D(f(x))
=\frac1{2\pi i}\int_{\mathcal C}
f(z)\bigl(R(z)P+R(z)D(x)R'(z)\bigr)\,dz.
\tag{13}
\]
This is a trace-norm integral in the Banach space \(\mathcal S_1(H)\). It lies in that space, proving the theorem. No division by \(z\) is used, so the formula is valid even if a contour passes through \(0\) outside the spectrum. \(\square\)

## 4. Recovering the canonical trace

**Lemma 4.1.** For every \(x\in A_0\),
\[
\operatorname{Tr}D(x)=\tau(x).
\tag{14}
\]

**Proof.** Every basis diagonal of \(\pi(x)\) equals \(\tau(x)\): this holds for group polynomials and extends by operator-norm continuity. Lemma 1.1 makes \(\rho\) the sum of two regular representations on \(pH\), with every basis vector corresponding to a regular basis vector. Thus
\[
\langle\delta_g,\rho(x)\delta_g\rangle=\tau(x)\quad(g\ne e),
\qquad
\langle\delta_e,\rho(x)\delta_e\rangle=0.
\]
The diagonal of \(D(x)\) is zero except at \(e\), where it is \(\tau(x)\). Absolute diagonal summation in (10) proves (14). This avoids an unjustified trace-norm limit of arbitrary polynomial approximants. \(\square\)

**Lemma 4.2.** If \(E,F\) are projections on any Hilbert space and \(E-F\) is trace class, then
\[
\operatorname{Tr}(E-F)
=\dim(EH\cap\ker F)-\dim(FH\cap\ker E)\in\mathbb Z.
\tag{15}
\]

**Proof.** Put \(B=E-F\), \(C=E+F-1\). Multiplication gives
\[
BC=-CB,\qquad B^2+C^2=1.
\tag{16}
\]
The self-adjoint operator \(B\) is compact, and \(-1\le B\le1\). Its nonzero eigenvalues have finite multiplicities. If \(B\xi=t\xi\), \(0<|t|<1\), then
\[
B(C\xi)=-t\,C\xi,\qquad C^2\xi=(1-t^2)\xi.
\]
Hence \(C/\sqrt{1-t^2}\) identifies the eigenspaces for \(t\) and \(-t\) isometrically. Their dimensions agree. The trace-class condition permits absolute summation of the eigenvalues, so all these pairs cancel.

The eigenspace for \(1\) is \(EH\cap\ker F\): equality in
\[
\langle\xi,B\xi\rangle=\|E\xi\|^2-\|F\xi\|^2\le\|\xi\|^2
\]
forces \(E\xi=\xi,F\xi=0\). The eigenspace for \(-1\) is obtained by exchanging \(E,F\). Both are finite-dimensional by compactness. Only their dimension difference remains in the trace, giving (15). \(\square\)

Thus every projection \(q\in A_0\) satisfies
\[
\tau(q)=\operatorname{Tr}(\pi(q)-\rho(q))\in\mathbb Z.
\tag{17}
\]
Both \(\pi(q)\) and \(\rho(q)\) are genuine orthogonal projections on \(H\), even though the latter representation is supported on \(p\).

## 5. Bringing every projection into the dense algebra

**Lemma 5.1.** Every projection \(e\in A\) is unitarily conjugate within \(A\) to a projection \(q\in A_0\).

**Proof.** Choose a self-adjoint group polynomial \(h\) with
\[
\delta=\|h-e\|<1/4.
\]
Such a polynomial is obtained by symmetrizing a polynomial approximant. For real \(z\) at distance greater than \(\delta\) from \(\{0,1\}\), the resolvent identity and Neumann series show \(z-h\) invertible. Since \(h\) is self-adjoint,
\[
\operatorname{Sp}_A(h)\subset[-\delta,\delta]\cup[1-\delta,1+\delta].
\tag{18}
\]
Choose \(f\) equal to \(0\) on a neighborhood of the first interval and \(1\) on a disjoint neighborhood of the second. This function is holomorphic on their disconnected union. Theorem 3.1 gives \(q=f(h)\in A_0\), and the functional calculus makes \(q\) a self-adjoint projection.

The circle \(|z-1|=1/2\) isolates the second spectral cluster. The Riesz formulas for \(q,e\) and their resolvent difference give
\[
\|q-e\|
\le\frac{\delta}{1/2-\delta}<1:
\tag{19}
\]
the circle has length \(\pi\), the resolvent of \(e\) has norm at most \(2\) there, and that of \(h\) has norm at most \((1/2-\delta)^{-1}\).

Set \(v=qe+(1-q)(1-e)\). Direct multiplication gives
\[
ve=qv,\qquad v^*v=vv^*=1-(e-q)^2.
\]
The last operator is invertible by (19) and commutes with \(e,q,v\). Therefore
\[
u=v\bigl(1-(e-q)^2\bigr)^{-1/2}\in A
\tag{20}
\]
is unitary and \(ueu^*=q\). \(\square\)

**Theorem 5.2.** Every projection \(e\in C_r^*(\mathbb F(a,b))\) has integer canonical trace. Consequently the only projections are \(0\) and \(1\).

**Proof.** Lemma 5.1 and traciality give \(\tau(e)=\tau(q)\), which is integer by (17). Since \(0\le\tau(e)\le1\), it is \(0\) or \(1\). Faithfulness gives \(e=0\) in the first case and \(1-e=0\) in the second. \(\square\)

This says nothing comparable about projections in matrix algebras over \(A\): \(\operatorname{diag}(1,0)\in M_2(A)\) is already a nontrivial projection. Nor does it exclude projections in the von Neumann closure. The norm density and spectral-gap step above explain why the assertion concerns \(A\) itself.

## 6. Exercises with complete solutions

**Exercise 1.** Check that the modified generator \(T_a\) is a permutation, including its exceptional inverse step.

*Solution.* Ordinary left multiplication sends \(a^{-1}\) to the omitted \(e\), and \(e\) to \(a\). After removing \(e\), replace these two steps by \(a^{-1}\mapsto a\); every other input and output retains its ordinary predecessor. Thus the map is bijective on nonidentity words. Its inverse sends \(a\mapsto a^{-1}\) and every other word \(g\) to \(a^{-1}g\). Both preserve the orthonormal basis, giving inverse unitaries.

**Exercise 2.** Compute \(\phi_a(e),\phi_a(a^{-1}),\phi_a(a),\phi_a(b)\), and explain how the two maps in (3) fill \(H'\).

*Solution.* These values are \(a,a^{-1},a^2,ba\). The image of \(\phi_a\) consists exactly of words ending in \(a^{\pm1}\); the analogous image of \(\phi_b\) consists of those ending in \(b^{\pm1}\). Every nonidentity reduced word ends in exactly one of these two kinds, and (2) has a unique inverse on each. Thus (3) is a basis bijection and not merely an embedding.

**Exercise 3.** Compute the rank, trace and trace norm of \(D(\lambda_a)\) on its finite-dimensional support.

*Solution.* Its only nonzero columns are the inputs \(\delta_e,\delta_{a^{-1}}\), with outputs \(\delta_a,\delta_e-\delta_a\). These are linearly independent, giving rank \(2\). Every diagonal entry is zero, so its trace is zero. The Gram matrix of these columns is
\[
\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.
\]
Its eigenvalues are \((3\pm\sqrt5)/2\), with sum \(3\) and product \(1\). The two singular values therefore have squared sum \(3\) and product \(1\), so their sum, the trace norm, is \(\sqrt5\).

**Exercise 4.** Why does finite rank for the generators imply finite rank for every group word, without summing an infinite Fourier series?

*Solution.* Formula (8) expresses the difference for a product of two words as bounded operators multiplying their two differences. Finite-rank operators form a two-sided ideal, so induction on the finite word length proves the claim. The same formula bounds the rank by the sum of the generator difference ranks, hence \(2\ell(g)\) for a nonempty reduced word. The identity has difference \(P\), of rank \(1\).

**Exercise 5.** Test (12) with \(x=1\). What error would omitting the term \(R(z)P\) cause?

*Solution.* For \(z\ne1\), \(R(z)=(z-1)^{-1}1\), \(R'(z)=(z-1)^{-1}p\), and their difference is \((z-1)^{-1}P\). Since \(D(1)=P\) and \(Pp=0\), the product \(R(z)D(1)R'(z)\) is zero. The first term in (12) gives the entire difference. Omitting it would incorrectly identify the different units of the two representations.

**Exercise 6.** Does operator-norm density of group polynomials prove (14) by continuity of \(\operatorname{Tr}\)?

*Solution.* No. The trace is continuous for trace norm, and operator-norm convergence does not control that norm. Rank-\(N\) projections divided by \(N\) have operator norm \(1/N\) but trace \(1\). The proof instead computes every diagonal of the actual trace-class difference \(D(x)\), and uses its absolute diagonal sum.

**Exercise 7.** Compute (15) for two rank-one projections whose ranges make an angle \(0<\theta<\pi/2\).

*Solution.* Choose unit vectors \(e_1\) and \(\cos\theta\,e_1+\sin\theta\,e_2\). On their two-dimensional span the projection difference has trace zero and determinant \(-\sin^2\theta\), so its eigenvalues are \(\pm\sin\theta\). There is no \(1\) or \(-1\) eigenspace. The generic pair cancels, giving trace zero. Adding an orthogonal one-dimensional summand to the range of the first projection adds one unmatched \(1\) eigenvalue and changes the trace to \(1\).

**Exercise 8.** Show that compactness, or even the Hilbert–Schmidt condition, cannot replace trace class in the trace calculation for projection differences.

*Solution.* Take the direct sum of the rank-one pairs from Exercise 7 with \(\sin\theta_n=1/n\), \(n\ge2\). The difference has eigenvalues \(\pm1/n\), so is compact and Hilbert–Schmidt because \(\sum_n2/n^2<\infty\). It is not trace class because \(\sum_n2/n=\infty\). The formal paired sum zero is not an absolutely convergent trace. Thus the trace in (15) would be undefined.

**Exercise 9.** With \(\|h-e\|=0.1\), estimate the projection error and explain why (20) stays inside \(A\).

*Solution.* Formula (19) gives \(\|q-e\|\le0.1/(0.5-0.1)=0.25\). Thus \(1-(e-q)^2\) is positive with spectrum in \([1-0.25^2,1]\), so its inverse square root is obtained by the continuous functional calculus in \(A\). Multiplying it by \(v\in A\) gives \(u\in A\). The algebraic identities in the proof make this operator a unitary that aligns the projections.

**Exercise 10.** Explain why the projection \(\operatorname{diag}(1,0)\) in \(M_2(A)\) does not contradict Theorem 5.2.

*Solution.* The theorem concerns projections in \(A\). In \(M_2(A)\), the indicated matrix is a nonzero projection different from the matrix identity. Its unnormalized matrix trace composed with \(\tau\) is \(1\), an integer, while its normalized trace is \(1/2\). Matrix amplification changes the unit's unnormalized trace from \(1\) to \(2\), so integrality no longer forces a projection to be \(0\) or the unit.

## Reading and attribution

Thomas Schick, [*The trace on the K-theory of group C\*-algebras*, arXiv:math/9907121v5](https://arxiv.org/pdf/math/9907121v5), Lemmas 2.6, 2.8 and 2.9, pp.7–11, supplies the actually read diagonal trace, nonunital resolvent and projection-difference methods. The source cites trace ideal facts and holomorphic-density K-theory results by reference. Here the full ordinary-Hilbert-space argument includes the explicit basis intertwiner, graph-norm closure, missing-unit resolvent term, absolute diagonal trace, eigenvalue pairing and unitary alignment of nearby projections. It does not require a K-theory computation.

Mihai Pimsner and Dan Voiculescu, [*K-groups of reduced crossed products by free groups*](https://www.theta.ro/jot/archive/1982-008-001/1982-008-001-006.pdf), *Journal of Operator Theory* 8(1) (1982), 131–156, introduction pp.131–132, states projection absence. Those pages were actually visually read; its full K-theory proof is not claimed read or used here. The source distinguishes this published paper from an earlier preprint with a false key lemma.

The proof concerns projections in \(C_r^*(\mathbb F(a,b))\) itself. Section 5 supplies the full spectral-gap and conjugacy argument, so mere norm density is not used as trace-norm continuity. Matrix projections and von Neumann projections remain distinct. Complete freely accessible compact spectral, trace-class and holomorphic functional calculus foundations are still pending; no source expression was imported.

# Positivity seen through two components

A two-component quadratic form gives three useful tests: positivity of an operator matrix, positivity of a matrix of normal functionals, and membership of a vector matrix in the standard positive cone. The same scalar inequality drives all three tests, but the positions of the entries and the supports of the diagonal terms matter. We develop that common mechanism first, then construct the matrix standard form needed for the cone test.

**Self-checked by the writing AI.** Inner products are linear in the first variable. The algebra \(M\) is a von Neumann algebra; its Hilbert space and predual need not be separable. Only PX07 assumes a faithful bounded normal positive functional. The other results include zero and nonfaithful diagonal terms.

The same results are treated in Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(12). The proofs below use the earlier programme arguments linked at their points of use. PX02 identifies the correct diagonal entries, PX03 supplies the support condition missing from the printed uniqueness claim, and PX07–08 correct and test the order of the off-diagonal arguments in the printed cone inequality.

## One scalar inequality controls the mixed term

Let \(u,v\) be real and \(w\) complex. Then

\[
 \begin{gathered}
 u|\lambda|^2+v|\mu|^2\\
 +2\operatorname{Re}(\lambda\overline\mu w)\ge0\\
 (\lambda,\mu\in\mathbb C)\\
 \Longleftrightarrow\\
 u,v\ge0,\\
 |w|^2\le uv.
 \end{gathered}
 \tag{PX.1}
\]

To prove necessity, set one scalar to zero to obtain \(u,v\ge0\). If \(u=0\), fix \(\mu=1\). Unless \(w=0\), a suitable phase and arbitrarily large magnitude for \(\lambda\) make the expression negative. If \(u>0\), choose \(\mu=1\) and \(\lambda=-\overline w/u\); the resulting inequality is \(v-|w|^2/u\ge0\). This covers also \(v=0\). Conversely, the mixed term has absolute value at most \(2\sqrt{uv}|\lambda||\mu|\), so the expression is bounded below by \((\sqrt u|\lambda|-\sqrt v|\mu|)^2\).

This proof explains why a zero diagonal term forces its mixed term to vanish. It requires no division by an operator and no invertibility assumption.

## Positive operator blocks

Represent \(M\) faithfully on \(K\). For \(a,b,c\in M\), put

\[
 A=\begin{pmatrix}a&b^*\\b&c\end{pmatrix}.
 \tag{PX.2}
\]

Then \(A\ge0\) on \(K\oplus K\) if and only if \(a,c\ge0\) and

\[
 \begin{gathered}
 |\langle b\xi,\eta\rangle|^2\\
 \le \langle a\xi,\xi\rangle\langle c\eta,\eta\rangle\\
 (\xi,\eta\in K).
 \end{gathered}
 \tag{PX.3}
\]

Indeed, compressing a positive \(A\) to either coordinate gives positivity of its diagonal entries. Its quadratic form on \((\lambda\xi,\mu\eta)\) is PX.1 with

\[
 \begin{gathered}
 u=\langle a\xi,\xi\rangle,\\
 v=\langle c\eta,\eta\rangle,\\
 w=\langle b\xi,\eta\rangle.
 \end{gathered}
\]

PX01 gives the inequality. Conversely, the same lemma with \(\lambda=\mu=1\) makes the quadratic form of the self-adjoint operator \(A\) nonnegative on every vector. The positive-operator criterion in BK01 gives \(A\ge0\).

The printed diagonal condition names \(a,b\); it must name \(a,c\). The off-diagonal entry need not be positive or even self-adjoint. For example \(a=c=1,b=i\) gives the positive scalar matrix \(vv^*\), where \(v=(1,i)^{\mathsf T}\), although \(b\) is not positive.

## A uniquely supported contraction

Let \(p=s(a)\) and \(q=s(c)\) be the support projections of the positive diagonal entries. The support and square-root results of BK01 and BK06 identify
\(pK=\overline{a^{1/2}K}\) and \(qK=\overline{c^{1/2}K}\).
Condition PX.3 is equivalent to existence of a contraction \(s\in M\) satisfying

\[
 \begin{gathered}
 b=c^{1/2}s a^{1/2},\\
 \|s\|\le1,\\
 s=qsp.
 \end{gathered}
 \tag{PX.4}
\]

With this support condition the contraction is unique.

**Construction.** On the two square-root ranges, prescribe the sesquilinear form

\[
 \begin{gathered}
 B(a^{1/2}\xi,c^{1/2}\eta)\\
 =\langle b\xi,\eta\rangle.
 \end{gathered}
 \tag{PX.5}
\]

PX.3 bounds it by \(\|a^{1/2}\xi\|\|c^{1/2}\eta\|\). In particular changing a representative by a vector in the relevant kernel changes the right side by zero. The form is well defined, extends continuously to \(pK\times qK\), and has norm at most one. Hilbert-space Riesz representation and bounded extension, proved in BK01, give a unique contraction \(s:pK\to qK\) with \(B(h,k)=\langle sh,k\rangle\). Extend it by zero on \((1-p)K\). This is precisely the condition \(s=qsp\). Pairing against every \(\eta\) now proves the first identity in PX.4. Conversely that identity and the contraction bound immediately give PX.3.

We still must check that the constructed Hilbert-space operator belongs to \(M\). For a unitary \(u\in M'\), all of \(a,b,c,p,q\) commute with \(u\). Thus \(usu^*\) is another contraction with the same factorization and the same supports. Uniqueness of the extended form gives \(usu^*=s\). Every element of the unital C*-algebra \(M'\) is a linear combination of unitaries by BK08. Therefore \(s\) commutes with \(M'\), and BK02 gives \(s\in M''=M\).

An arbitrary contraction \(t\in M\) with \(b=c^{1/2}ta^{1/2}\) need not equal \(s\). Its compression \(qtp\) does satisfy PX.4 and hence equals \(s\). This proves both the usual existence statement without specified supports and the exact uniqueness statement with them. For example, \(a=0,c=1,b=0\) admits every contraction \(t\); its supported solution is uniquely zero. The printed claim of uniqueness without a support condition fails in this example.

## Matrices of normal functionals

For \(\varphi,\psi,\rho\in M_*\), let \(\rho^*(z)=\overline{\rho(z^*)}\). Define a functional on \(M_2(M)\) by the **entrywise** pairing

\[
 \begin{aligned}
 \Omega(X)={}&\varphi(X_{11})\\
             &+\rho^*(X_{12})\\
             &+\rho(X_{21})\\
             &+\psi(X_{22}).
 \end{aligned}
 \tag{PX.6}
\]

Thus the displayed array of functionals is \(\left(\begin{smallmatrix}\varphi&\rho^*\\\rho&\psi\end{smallmatrix}\right)\). No transpose is hidden in the pairing. Each entry map \(X\mapsto X_{ij}\) is bounded and ultraweakly continuous: on a represented matrix algebra it is compression between two fixed coordinate inclusions, and its pullbacks of vector functionals are vector functionals. The concrete predual description and their norm-closed span in CP06–07 prove this for every normal functional. Taking the adjoint of a matrix coefficient proves the same assertion for \(\rho^*\). Consequently \(\Omega\) is bounded and normal.

The positivity criterion is

\[
 \begin{gathered}
 \Omega\ge0\quad\Longleftrightarrow\\
 \varphi,\psi\ge0\ \text{and}\\
 |\rho(y^*x)|^2\\
 \le\varphi(x^*x)\psi(y^*y)\\
 (x,y\in M).
 \end{gathered}
 \tag{PX.7}
\]

For a row \(R=(x\ \ y)\), direct substitution in PX.6 gives

\[
 \begin{gathered}
 \Omega(R^*R)\\
 =\varphi(x^*x)+\psi(y^*y)\\
 +2\operatorname{Re}\rho(y^*x).
 \end{gathered}
 \tag{PX.8}
\]

If \(\Omega\) is positive, diagonal inputs give positivity of \(\varphi,\psi\). Replace the row by \((\lambda x\ \ \mu y)\) and apply PX01 to obtain PX.7. Conversely PX01 makes PX.8 nonnegative for every row. Any positive \(X\in M_2(M)\) has a square root \(D\) by BK01. Writing its two rows as \(R_1,R_2\), one has \(X=D^*D=R_1^*R_1+R_2^*R_2\). Hence \(\Omega(X)\ge0\), proving sufficiency on the entire positive cone.

## The mixed functional as a GNS intertwiner

The last inequality has an operator meaning even when either diagonal functional is nonfaithful. Let \((H_\varphi,\pi_\varphi,\Lambda_\varphi)\) and \((H_\psi,\pi_\psi,\Lambda_\psi)\) be their GNS constructions. The null-space quotient, bounded representation and normality are proved in WG003–007. Since these functionals are bounded, every \(x\in M\) is in the respective GNS domains, and \(\Lambda_\varphi(1)\), \(\Lambda_\psi(1)\) are cyclic vectors. The zero functional gives the zero Hilbert space. Write \(h_x=\Lambda_\varphi(x)\) and \(k_y=\Lambda_\psi(y)\) to keep the two GNS spaces visible without long formulas.

PX.7 is equivalent to a unique contraction \(V:H_\varphi\to H_\psi\) with

\[
 \begin{gathered}
 \langle Vh_x,k_y\rangle=\rho(y^*x),\\
 V\pi_\varphi(a)=\pi_\psi(a)V\\
 (a,x,y\in M).
 \end{gathered}
 \tag{PX.9}
\]

For existence, the first formula defines a form bounded by the product of the two GNS norms, by PX.7. It vanishes on either null space, so it descends to the quotients. BK01 extends it to their completions and represents it by a contraction. Density makes that contraction unique. The intertwining assertion follows by testing against the dense GNS vectors: both \(V\pi_\varphi(a)\Lambda_\varphi(x)\) and \(\pi_\psi(a)V\Lambda_\varphi(x)\) pair with \(\Lambda_\psi(y)\) as \(\rho(y^*ax)\).

Conversely, from any contraction intertwining the two representations, define

\[
 \rho(a)=\langle Vh_a,k_1\rangle.
 \tag{PX.10}
\]

This is a bounded normal functional: it is a vector coefficient of the normal representation \(\pi_\varphi\), with second vector \(V^*\Lambda_\psi(1)\), using CP06. Move \(\pi_\psi(y)^*\) across the pairing and then through \(V\) to recover the first formula of PX.9. Cauchy–Schwarz and \(\|V\|\le1\) give PX.7. Evaluation at \(x=a,y=1\) recovers PX.10 from PX.9, so these two constructions are inverse. This gives a second, representation-theoretic reading of positive functional matrices.

## Amplifying a standard form

Now let \((M,H,J,P)\) be a standard form. On the Hilbert space \(\widetilde H=H^4\), write vectors as matrices \(\Xi=(\xi_{ij})\), with the sum of the four entry inner products. Let \(\widetilde M=M_2(M)\) act by left matrix multiplication. Its standard amplification has conjugation

\[
 (\widetilde J\Xi)_{ij}=J\xi_{ji}.
 \tag{PX.11}
\]

Here is a construction and verification, including the cone information needed next.

Choose a faithful normal semifinite weight \(\nu\) on \(M\), whose existence is proved in WH13. SF08, applied to two equal weights, constructs the weight \(\widetilde\nu(X)=\nu(X_{11})+\nu(X_{22})\). Its GNS space has four copies of \(H_\nu\); its full finite-star core consists of matrices with entries in \(\mathfrak n_\nu\cap\mathfrak n_\nu^*\). The closed Tomita operator sends entry \((j,i)\) through \(S_\nu\) into entry \((i,j)\). The slot graph argument in SF08 proves equality of these closed domains, not merely an identity on formal matrices.

Since \(S_\nu=J_\nu\Delta_\nu^{1/2}\), the polar conjugation is entrywise \(J_\nu\) followed by transposition; its positive factor is entrywise \(\Delta_\nu^{1/2}\). This follows also from the four equal polar decompositions in SF08. Transport each entry by SE10's standard-form unitary \(H_\nu\to H\), which intertwines the algebra, the conjugation and the cone. The transported conjugation is PX.11, and the transported natural cone \(\widetilde P\) makes this a standard form by SF05.

The standard right action on a vector is \(\xi b=Jb^*J\xi\), as verified in VP01. Formula PX.11 gives

\[
 \begin{gathered}
 \Xi B=\widetilde J B^*\widetilde J\Xi,\\
 (\Xi B)_{ij}\\
 =\sum_k\xi_{ik}b_{kj}.
 \end{gathered}
 \tag{PX.12}
\]

Indeed its \((i,j)\) entry is \(J(B^*\widetilde J\Xi)_{ji}=\sum_k Jb_{kj}^*J\xi_{ik}\). Thus the right action uses ordinary matrix multiplication with the specified vector right action on its entries.

The diagonal copy of \(P\) in either slot \((i,i)\) is exactly the corresponding diagonal corner of \(\widetilde P\). To see this directly in the weight coordinates, SF04 generates the cone by limits of vectors \(ZJ_{\widetilde\nu}\Lambda_{\widetilde\nu}(Z)\) for finite-star matrices \(Z\). The \((i,i)\) entry of such a generator is

\[
 \sum_k z_{ik}J_\nu\Lambda_\nu(z_{ik}),
\]

which belongs to \(P_\nu\) by the same SF04 formula. Conversely, take \(Z\) with a single entry in slot \((i,i)\): its cone generator has just that diagonal slot and runs through the generators of \(P_\nu\). Passing to limits and transporting proves the assertion. In particular diagonal entries of every \(\Xi\in\widetilde P\) belong to \(P\), and \(\operatorname{diag}(\xi,\eta)\in\widetilde P\) whenever \(\xi,\eta\in P\).

## A faithful vector detects the matrix cone

Let \(\varphi\in M_*^+\) be faithful, and let \(\alpha\in P\) be its unique representative from SE11. For vectors \(\xi,\eta,\zeta\in H\), set

\[
 \Xi=\begin{pmatrix}\xi&J\zeta\\\zeta&\eta\end{pmatrix}.
\]

For a vector \(\theta\), write

\[
 \begin{gathered}
 Q_\theta(x)=\langle x^*\theta x,\alpha\rangle,\\
 w(x,y)=\langle y^*\zeta x,\alpha\rangle.
 \end{gathered}
\]

Then \(\Xi\in\widetilde P\) if and only if \(\xi,\eta\in P\) and

\[
 \begin{gathered}
 |w(x,y)|^2\\
 \le Q_\xi(x)Q_\eta(y)\\
 (x,y\in M).
 \end{gathered}
 \tag{PX.13}
\]

All products use PX.12 and VP01. In particular the first argument beside the lower-left entry \(\zeta\) is \(y^*\), not \(x^*\).

**A generating faithful vector.** Put \(\widetilde\alpha=\operatorname{diag}(\alpha,\alpha)\). By PX06 it belongs to \(\widetilde P\). Faithfulness of \(\varphi\) makes \(\alpha\) separating, and SE06 makes it cyclic for \(M\). Consequently \(A\widetilde\alpha=(a_{ij}\alpha)\) has dense range as \(A\) varies, and is zero only when \(A=0\). Its functional is the faithful normal finite functional \(X\mapsto\varphi(X_{11})+\varphi(X_{22})\). Apply SE06 to this full-support cone vector in the amplified form. The resulting cone formula, with \(A\) ranging over \(\widetilde M\), is

\[
 \widetilde P=\overline{\{A\widetilde\alpha A^*\}}.
 \tag{PX.14}
\]

It follows from the finite GNS cone generators in SE06, with both left and right actions identified by PX.12.

**Expansion by columns.** If \(\xi,\eta\in P\), then \(\widetilde J\Xi=\Xi\). Self-duality and PX.14 give

\[
 \begin{gathered}
 \Xi\in\widetilde P\quad\Longleftrightarrow\\
 \langle A^*\Xi A,\widetilde\alpha\rangle\ge0\\
 (A\in\widetilde M).
 \end{gathered}
 \tag{PX.15}
\]

Moving the bounded left and right factors across the inner product proves that this is exactly pairing against each generator in PX.14. For a column with entries \(x,y\), its contribution is

\[
 \begin{gathered}
 Q(x,y)\\
 =Q_\xi(x)+Q_\eta(y)\\
 +2\operatorname{Re}w(x,y).
 \end{gathered}
 \tag{PX.16}
\]

The two mixed terms are conjugates because \(J(y^*\zeta x)=x^*(J\zeta)y\) and \(J\alpha=\alpha\). The two diagonal terms are nonnegative: standard-form cone invariance puts \(x^*\xi x,y^*\eta y\) in \(P\), and \(P\) is self-dual. Replacing the column by \((\lambda x,\mu y)\) gives precisely the scalar form PX.1, with mixed coefficient \(\langle y^*\zeta x,\alpha\rangle\). Thus nonnegativity for every column is equivalent to PX.13. Every \(A\) has two columns, so the sum of the two corresponding values of PX.16 is the pairing in PX.15. Testing one nonzero column proves necessity, and summing proves sufficiency. If \(\Xi\) starts in \(\widetilde P\), PX06 supplies its positive diagonal entries, so this also proves that direction without assuming them in advance.

## Concrete tests for order, supports and faithfulness

**The off-diagonal order can change the answer.** Use the standard form of \(M_2(\mathbb C)\) on Hilbert–Schmidt matrices, with \(Jz=z^*\), \(P\) the positive matrices and \(\alpha=I\), representing the unnormalized trace. The model is verified in SF14; in this finite tracial case the same GNS calculation for the amplification identifies \(\widetilde P\) with the positive matrices in \(M_4(\mathbb C)\). Indeed its modular operator is the identity, and SF04's cone generators are exactly the positive matrix squares.

With the usual matrix units, take

\[
 \begin{gathered}
 \xi=E_{11},\\
 \eta=E_{22},\\
 \zeta=E_{21},\\
 \Xi=vv^*,\\
 v=\begin{pmatrix}E_{11}\\E_{21}\end{pmatrix}.
 \end{gathered}
 \tag{PX.17}
\]

Hence \(\Xi\in\widetilde P\). But for \(x=E_{21}\), \(y=E_{11}\), direct multiplication gives

\[
 \begin{gathered}
 \operatorname{Tr}(x^*\zeta y)=1,\\
 x^*\xi x=0,\\
 y^*\eta y=0.
 \end{gathered}
 \tag{PX.18}
\]

Thus the printed variant with \(x^*\zeta y\) on the left and these diagonal terms on the right would assert \(1\le0\). PX.13 has \(y^*\zeta x\), whose trace is zero for this choice, and its proof establishes the inequality for every \(x,y\). This is an index correction forced by the specified vector matrix and right action.

**Why the detecting vector must be faithful.** In the standard form of \(M=\mathbb C\oplus\mathbb C\), use \(H=\mathbb C^2\), coordinate conjugation and the coordinatewise nonnegative cone. These axioms follow directly from coordinate multiplication and scalar self-duality. Take \(\alpha=(1,0)\), \(\xi=\eta=0\) and \(\zeta=(0,1)\). All pairings in PX.13 vanish, for every \(x,y\), because \(\alpha\) sees only the first summand. The second summand of \(\Xi\) is nevertheless \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), whose quadratic form on \((1,-1)\) is \(-2\). The amplified cone on each scalar summand is the positive matrix cone, by the tracial calculation just given. Hence \(\Xi\notin\widetilde P\). Positivity on an unseen summand cannot be recovered from a nonfaithful test vector.

**What remains unique when supports shrink.** For any positive block, PX03 determines precisely the compression \(qtp\) of every factorizing contraction \(t\). The example \(a=0,c=1,b=0\) shows why no value on the omitted input support is determined. This is the same null-space issue handled by the GNS quotients in PX05; taking those quotients is what makes the intertwiner uniquely defined.

The arguments establish all four mathematical components of the cited exercise, with the three explicit corrections above.

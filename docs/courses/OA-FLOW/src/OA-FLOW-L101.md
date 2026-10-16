# Strongly continuous orbits and uniform continuity

A group can move every vector continuously while still making an arbitrarily large change on suitably chosen unit vectors at arbitrarily small times. We give a normal isometric action on a dual Banach space exhibiting this phenomenon, locate the precise distinction between relative and ambient interior, and prove the uniform statements that remain valid.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.orbit.counterexample"></a>

## A dual Hilbert-space counterexample

Let \(X=\ell^2(\mathbb N)\), with coordinates indexed by \(n\geq1\), and define
\[
 (T_t x)_n=e^{int}x_n,\qquad t\in\mathbb R.
 \tag{O1}
\]
Completeness and the Cauchy–Schwarz inequality are supplied by [SC6–7](OA-FLOW-SC.md#sc-06). These maps form a group of surjective linear isometries.

Here is an explicit predual, including the pairing convention. Use another copy \(E=\ell^2(\mathbb N)\) with the complex bilinear pairing
\[
 \langle x,a\rangle=\sum_{n\geq1}x_na_n.
 \tag{O2}
\]
Every continuous complex-linear functional \(\ell\) on \(E\) has this form. Indeed put \(b_n=\ell(e_n)\). Testing \(\ell\) on the finite vector with coordinates \(\overline{b_n}/(\sum_{j=1}^N|b_j|^2)^{1/2}\), when that denominator is nonzero, gives
\[
 \left(\sum_{n=1}^N|b_n|^2\right)^{1/2}\leq\|\ell\|.
\]
Thus \(b\in\ell^2\); equality with \(\sum b_na_n\) holds first on finite vectors and then on all of \(E\), by density. Cauchy–Schwarz and the same tests give equality of norms. Consequently \(X=E^*\) isometrically. The preadjoint of \(T_t\) is
\[
 (S_ta)_n=e^{int}a_n,
 \qquad \langle T_tx,a\rangle=\langle x,S_ta\rangle.
 \tag{O3}
\]
In particular each \(T_t\) is weak-star continuous. The identical phases in (O3) result from using a bilinear dual pairing.

For a fixed \(x\in X\), split the squared orbit difference at \(N\):
\[
 \|T_tx-x\|^2
 =\sum_{n\leq N}|e^{int}-1|^2|x_n|^2
   +\sum_{n>N}|e^{int}-1|^2|x_n|^2.
 \tag{O4}
\]
The tail is at most \(4\sum_{n>N}|x_n|^2\), independently of \(t\). After choosing \(N\) to make it small, the finite initial sum tends to zero. This proves norm continuity of every orbit at zero and, by the group law, everywhere.

Nevertheless, at \(t_k=\pi/k\),
\[
 (T_{t_k}-I)e_k=-2e_k,\qquad
 \|T_{t_k}-I\|=2.
 \tag{O5}
\]
The lower bound follows from the displayed vector and the upper bound from the triangle inequality for two isometries. Since \(t_k\to0\), the group is not continuous in operator norm. All the assertions hold on the full dual space; no incomplete subspace or discontinuous dual operator is involved.

<a id="oa-flow.orbit.relative"></a>

## What the compact-ball category argument actually gives

Let \(X=E^*\) be any dual Banach space and \(T\) a group of weak-star continuous isometries with norm-continuous individual orbits. For \(\epsilon>0\), put
\[
 S=\{x:\|x\|\leq1\},\qquad
 A_n=\left\{x\in S:\sup_{|t|<1/n}\|T_tx-x\|\leq\epsilon\right\}.
 \tag{O6}
\]
The ball \(S\) is compact Hausdorff in its weak-star topology by [ST1](OA-FLOW-ST12.md#oa-flow.st.1). The dual norm formula makes each condition \(\|(T_t-I)x\|\leq\epsilon\) an intersection of closed inequalities
\[
 |\langle (T_t-I)x,a\rangle|\leq\epsilon
 \quad(\|a\|\leq1).
\]
Each scalar function is weak-star continuous. Intersecting over \(t\) shows that \(A_n\) is closed in \(S\). Orbit continuity gives \(\bigcup_nA_n=S\).

For clarity, the needed category assertion holds on every nonempty compact Hausdorff space \(K\). If \(y\in O\) with \(O\) open, separate \(y\) from each point of the compact set \(K\setminus O\) by disjoint open neighborhoods. A finite subcover of that set gives an open neighborhood \(U\) of \(y\) with \(\overline U\subset O\): its closure misses the union of the neighborhoods covering the complement. If closed sets \(F_n\) all have empty interior, choose successively nonempty open sets \(U_n\) with
\[
 \overline U_1\subset K\setminus F_1,\qquad
 \overline U_{n+1}\subset U_n\setminus F_{n+1}.
\]
At every stage the target is nonempty open, because \(F_{n+1}\) has empty interior. The nested nonempty compact closures have nonempty intersection: otherwise their complements would give a finite open cover of \(K\) contradicting nesting. A point of that intersection lies outside every \(F_n\). Thus a countable closed cover of \(K\) has a member with nonempty interior.

Applied to (O6), this gives \(m\), \(x_0\in S\), and an ambient weak-star neighborhood \(V\) of zero such that
\[
 x_0\in (x_0+V)\cap S\subset A_m.
 \tag{O7}
\]
It does not give \(x_0+V\subset A_m\). The valid difference estimate is only
\[
 \|(T_t-I)v\|\leq2\epsilon
 \quad\text{if }v\in V,\ x_0+v\in S,\ |t|<1/m.
 \tag{O8}
\]
Indeed apply (O6) to \(x_0+v\) and \(x_0\) and subtract. The membership condition \(x_0+v\in S\) is essential.

In an infinite-dimensional dual space no ambient weak-star neighborhood is norm bounded. Such a neighborhood contains a set specified by finitely many inequalities \(|\langle v,a_j\rangle|<r_j\). Choose more linearly independent vectors of \(X\) than there are tests; elementary finite-dimensional linear algebra gives a nonzero \(w\) annihilated by every test. The entire line \(\mathbb Cw\) satisfies the inequalities. Thus no translate of that neighborhood can lie in \(S\). This identifies why ambient interior cannot replace relative interior in the compact-ball argument.

<a id="oa-flow.orbit.uniform"></a>

## Two valid forms of uniformity

First suppose an additional estimate really is available on an ambient weak-star neighborhood:
\[
 \|(T_t-I)v\|\leq2\epsilon
 \quad(v\in V,\ |t|<\eta).
 \tag{O9}
\]
Take \(V\) open and containing zero, by shrinking it if necessary. Compactness of \(S\) gives a finite cover by \(x_j+V\), with \(x_j\in S\). Orbit continuity at these finitely many centers gives \(\delta>0\) such that
\(\|(T_t-I)x_j\|\leq\epsilon\) for all \(j\) and \(|t|<\delta\). For \(x=x_j+v\in S\) and \(|t|<\min(\eta,\delta)\), (O9) gives
\[
 \|(T_t-I)x\|\leq3\epsilon.
 \tag{O10}
\]
Taking the supremum over \(S\) proves the claimed operator-norm bound under the additional hypothesis (O9). Equation (O8) alone does not supply that hypothesis.

Second, without any duality assumption, orbit continuity of an isometric group is uniform on every norm-compact subset \(K\) of its Banach space. For \(r>0\), take a finite \(r\)-net \(x_1,\ldots,x_k\) in \(K\). Then
\[
 \sup_{x\in K}\|(T_t-I)x\|
 \leq 2r+\max_j\|(T_t-I)x_j\|.
 \tag{O11}
\]
Let \(t\to0\), and then \(r\downarrow0\). The empty compact set is harmless. In the model (O1), restriction to the first \(N\) coordinates gives the exact norm
\[
 \|T_t-I\|_{\operatorname{span}\{e_1,\ldots,e_N\}}
 =\max_{1\leq n\leq N}|e^{int}-1|\longrightarrow0.
\]
The obstruction is the ability to choose a new high coordinate as time decreases.

Another sufficient hypothesis is compact action spectrum, whose cutoff-filter proof is given in [L92](OA-FLOW-L92.md#oa-flow.normcont.reverse).

The mathematical issue examined here is the implication proposed in Takesaki, *Theory of Operator Algebras II*, Exercise XI.1.1, p.329. Its closed-set and finite-cover steps have the valid forms proved above; the proposed general conclusion is disproved by (O1)–(O5).

# Abelian semicontinuity and multiplier spectra

*Self-checked by the writing AI. Original text: CC0 1.0.*

For an abelian algebra, the monotone-limit classes can be read as functions on its ordinary spectrum. Bounded lower semicontinuous functions correspond to upper limits after adjoining the identity; bounded upper semicontinuous functions correspond to lower limits. Open and closed projections become indicators of open and closed subsets. Two-sided multipliers correspond to bounded continuous functions.

The distinction between the spectrum and the whole bidual matters. We identify these particular operator classes by their integrals against every finite Radon measure. Point evaluations alone are used only after that identification has been proved.

Use [Monotone approximation and semicontinuous operators](../reader/monotone-approximation-and-semicontinuous-operators.html) for monotone-limit notation; [Open projections and closed one-sided ideals](../reader/open-projections-and-closed-one-sided-ideals.html) for open projections; and [Multipliers and essential extensions](../reader/multipliers-and-essential-extensions.html#3-the-maximal-essential-extension) for the multiplier extension property. The Gelfand theorem and the complete Stone–Čech construction are [Continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Theorem 2.1 and Exercise 2.4. We use finite Radon measures, their positive functional model, and the complete increasing-net proof from [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html), Section 3 and Lemma 2.3. Riesz representation and locally compact Urysohn separation are its stated measure/topology prerequisites. The proofs below derive the function models directly from continuous minorants and their finite Radon integrals, with no countability assumption. Blackadar’s freely readable *Operator Algebras* also treats multipliers and compactifications.

## 1. Increasing nets and finite Radon measures

Let \(\Omega\) be a locally compact Hausdorff space and \(A=C_0(\Omega)\). Positive functionals on \(A\) are finite positive Radon measures; their norms are their total masses. We use the same symbol \(\mu\) for a measure and its normal extension to \(A^{**}\).

**Lemma 1.1.** If \((f_i)\) is a uniformly bounded increasing net of real continuous functions on \(\Omega\), and \(f=\sup_i f_i\) pointwise, then for every finite positive Radon measure,
\[
\int_\Omega f\,d\mu=\sup_i\int_\Omega f_i\,d\mu.
\tag{1.1}
\]
The functions need not vanish at infinity, and no countability hypothesis on \(\Omega\) or on the net is needed.

**Proof.** The compact-space proof in ABA Lemma 2.3 uses inner regularity on open sets and finite level sets. Both ingredients apply here. For completeness, if open sets \(U_i\) increase to \(U\), any compact subset of \(U\) lies in one \(U_i\), by a finite subcover and directedness. Inner regularity gives
\(\mu(U)=\sup_i\mu(U_i)\).

Adding a constant reduces to \(0\le f_i\le R\). Fix \(\varepsilon>0\) and \(N\ge R/\varepsilon\), and put
\[
s(g)=\varepsilon\sum_{k=1}^N1_{\{g>k\varepsilon\}}.
\]
For \(0\le g\le R\), one has \(g-\varepsilon\le s(g)\le g\). For each of the finitely many levels,
\[
\{f>k\varepsilon\}=\bigcup_i\{f_i>k\varepsilon\}.
\]
The open-set identity and directedness give one index for which the sum of all level-measure errors, multiplied by \(\varepsilon\), is less than any prescribed \(\eta>0\). At that index,
\[
\int f_i\,d\mu\ge\int f\,d\mu-\varepsilon\mu(\Omega)-\eta.
\]
Let \(\eta,\varepsilon\downarrow0\). The reverse inequality follows from \(f_i\le f\). Undo the constant shift. \(\square\)

## 2. Functions represented by monotone limits

Put \(A_1=A+\mathbb C1\subset A^{**}\) and
\[
T_A=(A_1)_{\mathrm{sa}}^\uparrow,
\qquad T_A^\downarrow=(A_1)_{\mathrm{sa}}^\downarrow.
\]
Here the approximating nets are norm bounded. Write \(\operatorname{LSC}_b(\Omega)\) and \(\operatorname{USC}_b(\Omega)\) for bounded real lower and upper semicontinuous functions.

**Theorem 2.1.** There is an isometric bijection
\[
f\longmapsto a_f:\operatorname{LSC}_b(\Omega)\longrightarrow T_A,
\tag{2.1}
\]
characterized by
\[
\mu(a_f)=\int_\Omega f\,d\mu
\quad\text{for every finite positive Radon measure }\mu.
\tag{2.2}
\]
The corresponding statement holds for \(\operatorname{USC}_b(\Omega)\) and \(T_A^\downarrow\), using \(a_f=-a_{-f}\). Both operator classes are norm closed. In particular,
\[
\overline{(A_1)_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}
=(A_1)_{\mathrm{sa}}^\uparrow
\quad\text{in the abelian case}.
\tag{2.3}
\]

**Proof.** Let \(f\) be bounded and lower semicontinuous, \(r=\|f\|_\infty\), and \(h=f+r\ge0\). The set
\[
\mathcal U_h=\{b\in C_0(\Omega)_+:b\le h\}
\]
is directed by pointwise order, since the maximum of two members is another member. Its pointwise supremum is \(h\). Indeed, if \(0<c<h(\omega)\), locally compact Urysohn separation gives \(g\in C_c(\Omega)\), with \(0\le g\le1\), \(g(\omega)=1\), and support inside the open set \(\{h>c\}\). Then \(cg\le h\) and \(cg(\omega)=c\). Points with \(h(\omega)=0\) cause no difficulty.

These functions form a bounded increasing net \(b_i\), with \(0\le b_i\le2r\). Let \(b\) be its supremum in the bidual and put
\[
a_f=b-r1.
\tag{2.4}
\]
The net \(b_i-r1\in(A_1)_{\mathrm{sa}}\) is bounded increasing with limit \(a_f\). Normality of \(\mu\) and Lemma 1.1 give (2.2). Thus the construction does not depend on a chosen family of continuous minorants: positive normal functionals determine the bidual element.

Conversely, suppose \(a_i\in(A_1)_{\mathrm{sa}}\) increase boundedly to \(a\). Each \(a_i\) is a bounded continuous function on \(\Omega\), and
\[
f(\omega)=\sup_i a_i(\omega)
\]
is bounded and lower semicontinuous. Normality and Lemma 1.1 show \(\mu(a)=\int f\,d\mu\) for every positive \(\mu\), so \(a=a_f\). In particular point masses give \(a_f(\delta_\omega)=f(\omega)\), proving uniqueness of \(f\).

The self-adjoint norm formula and (2.2) give
\[
\|a_f\|=\sup_{\mu\ge0,\ \mu(\Omega)\le1}
\left|\int f\,d\mu\right|=\|f\|_\infty.
\tag{2.5}
\]
The upper bound uses the total mass, and the lower bound uses point masses. The same reasoning gives
\(\|a_f-a_g\|=\|f-g\|_\infty\), even if the difference is not semicontinuous. A uniform limit of bounded lower semicontinuous functions is lower semicontinuous. Therefore a norm-convergent sequence in \(T_A\) gives a uniformly convergent sequence of the corresponding functions; its limit corresponds to the operator limit by (2.5). This proves norm closedness. Taking negatives proves all lower-class assertions. \(\square\)

**Corollary 2.2.** Open projections in \(A^{**}\) correspond bijectively to open subsets \(U\subset\Omega\), with
\[
\mu(p_U)=\mu(U).
\tag{2.6}
\]
Closed projections correspond to closed subsets by the same indicator formula.

**Proof.** An open projection belongs to \(A_+^\uparrow\subset T_A\). The normal extension of every point character is a *-homomorphism to \(\mathbb C\), so its value at a projection is zero or one. The corresponding function is therefore \(1_U\), and its lower semicontinuity says exactly that \(U\) is open.

Conversely, \(C_0(U)\), extended by zero off \(U\), is a closed ideal of \(C_0(\Omega)\). Its positive increasing approximate identity converges to an open central projection \(p_U\). At a point of \(U\) it converges to one, since multiplication approximates a function nonzero there; outside \(U\) it is zero. Theorem 2.1 identifies that projection with \(a_{1_U}\), proving (2.6) and bijectivity. Taking complements proves the closed case. \(\square\)

## 3. The multiplier spectrum

For \(\omega\in\Omega\), let \(\overline{\delta_\omega}\) be the normal extension of its character to \(A^{**}\). Their coordinate values define a contractive *-homomorphism
\[
E:A^{**}\longrightarrow\ell^\infty(\Omega),
\qquad E(x)(\omega)=\overline{\delta_\omega}(x).
\tag{3.1}
\]
Its restriction to \(A\) is the ordinary faithful pointwise representation. We do not assume it is faithful on the whole bidual.

**Theorem 3.1.** The map \(E\) restricts to a *-isomorphism
\[
\operatorname{Mult}(C_0(\Omega))\cong C_b(\Omega).
\tag{3.2}
\]
Its spectrum is the Stone–Čech compactification \(\beta\Omega\).

**Proof.** The restriction to multipliers is faithful. If \(E(x)=0\) for a multiplier \(x\), then for \(a\in A\),
\[
E(xa)=E(x)E(a)=0.
\]
But \(xa\in A\), where \(E\) is faithful, so \(xA=0\). Essentiality of \(A\) in its multiplier algebra gives \(x=0\). Thus this restriction is isometric.

If \(x\) is a multiplier and \(f=E(x)\), fix \(\omega\in\Omega\). Choose a relatively compact neighborhood \(V\) of \(\omega\) and \(a\in C_c(\Omega)\) equal to one on \(\overline V\). Then on \(V\),
\[
f=E(xa).
\]
Since \(xa\in A\), the right side is continuous. Such neighborhoods cover \(\Omega\), so \(f\) is continuous everywhere and bounded by \(\|x\|\). This proves that the image lies in \(C_b(\Omega)\).

Conversely, \(C_0(\Omega)\) is an essential ideal of \(C_b(\Omega)\). Products preserve vanishing at infinity; if a bounded continuous function annihilates every \(C_0\) function, a compactly supported function nonzero at each chosen point detects that its value is zero there. The essential-extension theorem consequently embeds \(C_b(\Omega)\) into \(\operatorname{Mult}(A)\) while fixing \(A\). If a function \(g\) maps to \(T_g\), then
\[
E(T_g)(\omega)a(\omega)=g(\omega)a(\omega)
\quad(a\in C_0(\Omega)).
\]
Choosing \(a(\omega)\ne0\) shows \(E(T_g)=g\). This proves surjectivity in (3.2).

The full spectrum statement is the exact stronger result of CF Exercise 2.4, whose proof covers every completely regular Hausdorff space: evaluation embeds the space densely in the compact spectrum of \(C_b\), and every continuous map into a compact Hausdorff space extends uniquely. A locally compact Hausdorff space meets those hypotheses; its image is also open. Applying that existing theorem to (3.2) gives \(\beta\Omega\). For the empty space the algebras and spectrum are empty or zero as appropriate. \(\square\)

## 4. Graded exercises with solutions

**Exercise 4.1 — introductory: why one point at infinity is insufficient.** Let \(\Omega=\mathbb N\) with the discrete topology. Show that its multiplier algebra is \(\ell^\infty\). Use the even-number indicator to show that \(\beta\mathbb N\setminus\mathbb N\) has at least two points, and that this multiplier does not extend continuously to the one-point compactification.

**Solution.** Every bounded function on a discrete space is continuous, so Theorem 3.1 gives the multiplier algebra \(\ell^\infty\). Let \(e=1_{2\mathbb N}\). Its Gelfand transform is a continuous projection on \(\beta\mathbb N\); the closures of the even and odd subsets lie in its disjoint level sets at one and zero. Each closure has a point outside \(\mathbb N\). Otherwise it would be a compact subset of the open discrete subspace \(\mathbb N\) containing infinitely many points, which is impossible. The two resulting boundary points are distinct because the transform takes different values there.

Continuity at the point at infinity in the one-point compactification would require the sequence \(e(n)\) to converge. Its alternating values do not. The Stone–Čech spectrum provides enough boundary points for every bounded continuous function to extend.

**Exercise 4.2 — intermediate: an open interval projection.** For \(A=C_0(\mathbb R)\), identify the open projection corresponding to \((0,1)\). Give a bounded positive increasing sequence from \(A\) converging to it. Decide whether it is closed or a multiplier.

**Solution.** Put
\[
f_n(t)=\min\{1,n\,\operatorname{dist}(t,\mathbb R\setminus(0,1))\}.
\]
These are continuous positive contractions with compact support in \([0,1]\), increase, and have pointwise limit \(1_{(0,1)}\). Theorem 2.1 and Lemma 1.1 identify their strong supremum with \(p_{(0,1)}\), whose evaluation at a finite positive measure is \(\mu((0,1))\). Its value at \(\delta_0\) is zero, whereas a probability measure supported in the interval has value one.

The interval is not closed. Its indicator is not upper semicontinuous at zero or one, so Corollary 2.2 shows the projection is not closed. The indicator is discontinuous, so Theorem 3.1 shows it is not a multiplier.

**Exercise 4.3 — advanced: a Borel projection outside both classes.** In \(C_0(\mathbb R)^{**}\), construct a projection \(r\) satisfying
\[
\mu(r)=\mu(\mathbb Q)
\quad\text{for every finite positive Radon measure }\mu.
\]
Show that \(r\) belongs to neither \(T_A\) nor \(T_A^\downarrow\).

**Solution.** For a fixed rational \(q\), the functions
\[
u_{q,n}(t)=\max\{0,1-n|t-q|\}
\]
are positive contractions in \(C_0(\mathbb R)\) and decrease strongly to a positive element \(p_q\) in the bidual. Dominated convergence gives \(\mu(p_q)=\mu(\{q\})\). Their squares have the same pointwise limit and converge strongly to \(p_q^2\). Normality and dominated convergence consequently give
\(\mu(p_q^2)=\mu(p_q)\) for every positive \(\mu\). Such functionals separate the bidual, so \(p_q^2=p_q\).

For distinct rationals, the supports of the corresponding bumps are eventually disjoint. Their bounded strong limits give \(p_qp_{q'}=0\). Thus the countable sum
\[
r=\sum_{q\in\mathbb Q}p_q
\]
exists strongly as a projection. Normality and countable additivity give \(\mu(r)=\sum_q\mu(\{q\})=\mu(\mathbb Q)\). In particular its point evaluations form the indicator \(1_{\mathbb Q}\). The rational and irrational points are both dense, so this indicator is neither lower nor upper semicontinuous at any point. Theorem 2.1 excludes \(r\) from both classes. Borel measurability therefore allows elements beyond these two semicontinuity classes.

## References

[Blackadar] Bruce Blackadar, [*Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), author’s revised and corrected online version of the 2005 book, accessed 3 October 2026. The multiplier identification is proved here; the Stone–Čech universal property is proved in Exercise 2.4 of the linked continuous-functional-calculus lesson.

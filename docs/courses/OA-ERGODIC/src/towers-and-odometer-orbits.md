# Towers and odometer orbits

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text is public domain (CC0).*

## Introduction

A long orbit segment gives a finite model for a transformation. The difficulty is to arrange that the ends of the segment occupy little measure. For a nonsingular transformation, the levels of a tower can have very different measures, so a counting argument alone does not control its boundary.

We first construct towers for an ergodic nonsingular transformation on a nonatomic probability space. We then choose the position of a cyclic cut using the measures of both boundary bands. Finally we calculate the orbits of the binary adding machine.

The prerequisites are [Finite orbit classes and matrix blocks](finite-orbit-classes-and-matrix-blocks.md) and elementary absolute continuity of finite measures. [Invariant means on measured relations](invariant-means-on-measured-relations.md) gives another route to finite approximation. All transformations below are invertible Borel maps, modulo null sets.

## 1. Why a positive set is reached

Let \(T\) be nonsingular and ergodic on a standard nonatomic probability space \((X,\mu)\).

**Lemma 1.1.** For every positive-measure Borel set \(A\), almost every point has a forward iterate in \(A\). Almost every point of \(A\) has a strictly positive return time to \(A\).

*Proof.* The last-visit set
\[
W=A\setminus\bigcup_{n\geq1}T^{-n}A
\]
is wandering: if \(T^iW\cap T^jW\ne\varnothing\), \(i<j\), a point of \(W\) has a positive iterate in \(W\subset A\), a contradiction. If \(\mu(W)>0\), nonatomicity supplies \(B\subset W\) such that both \(B\) and \(W\setminus B\) have positive measure. Their two-sided saturations are disjoint invariant positive-measure sets, contradicting ergodicity. Thus \(W\) is null.

Let \(F=\bigcup_{n\geq0}T^{-n}A\). We have \(T^{-1}F\subset F\); the opposite inclusion holds modulo null sets because almost every point of \(A\) returns. Hence \(F\) is invariant modulo null sets and has positive measure. Ergodicity makes it conull. \(\square\)

Ergodicity on a space with an atom instead forces concentration on the atom's countable orbit. The nonatomic hypothesis separates the properly ergodic case from this single-orbit case.

## 2. A nonsingular tower

**Theorem 2.1.** For every integer \(n\geq1\) and \(\varepsilon>0\), there is a Borel \(E\subset X\) such that
\[
E,TE,\ldots,T^{n-1}E
\quad\text{are disjoint},\qquad
\mu\left(\bigcup_{j=0}^{n-1}T^jE\right)>1-\varepsilon.
\tag{2.1}
\]

*Proof.* The case \(n=1\) is immediate. For the other cases, absolute continuity of the finitely many measures \(B\mapsto\mu(T^{-j}B)\), \(0\leq j<n\), gives a number \(a>0\) such that
\[
\mu(B)<a\ \Longrightarrow\
\mu(T^{-j}B)<\varepsilon/n
\quad(0\leq j<n).
\tag{2.2}
\]
Choose \(A\) with \(0<\mu(A)<a\). Lemma 1.1 makes the waiting time
\[
r(x)=\min\{k\geq0:T^kx\in A\}
\]
finite on a conull set. Work on a common conull \(T\)-invariant Borel set where these facts hold. Put \(A_k=\{x:r(x)=k\}\) and
\[
F=\bigcup_{q\geq1}A_{qn},\qquad E=T^{-(n-1)}F.
\]

The sets \(F,T^{-1}F,\ldots,T^{-(n-1)}F\) are disjoint. Indeed, if \(x\in A_{qn}\) and \(1\leq j<n\), the first hit has not occurred by time \(j\), so \(r(T^jx)=qn-j\), which is not a multiple of \(n\).

If \(x\notin\bigcup_{j=0}^{n-1}T^{-j}A\), its waiting time is at least \(n\). Write \(r(x)=qn+j\), \(q\geq1\), \(0\leq j<n\). Then \(T^jx\in A_{qn}\subset F\). Thus
\[
X\setminus\bigcup_{j=0}^{n-1}T^{-j}A
\subset\bigcup_{j=0}^{n-1}T^{-j}F
=\bigcup_{j=0}^{n-1}T^jE.
\]
Equation (2.2) bounds the omitted measure by \(\varepsilon\). \(\square\)

## 3. Positioning a finite cycle

Closing a tower into a cycle changes the transformation at its top. Errors for both positive and negative powers occur near the top and bottom. In a nonsingular tower, neither band has a measure bound from its number of levels.

**Theorem 3.1.** Given \(m\geq1\) and \(\varepsilon>0\), there is a finite-order nonsingular Borel transformation \(S\), with every \(S\)-orbit contained in a \(T\)-orbit, such that
\[
\mu\{x:S^jx\ne T^jx\}<\varepsilon
\quad\text{for all }|j|\leq m.
\tag{3.1}
\]

*Proof.* Choose \(q\) so large that \(2/q<\varepsilon/2\), and set \(n=qm\). Choose a tower as in Theorem 2.1 with complement \(R\) so small that
\[
\mu(T^kR)<\varepsilon/2,\qquad0\leq k\leq(q-1)m.
\tag{3.2}
\]
This is possible by absolute continuity of finitely many image measures.

Partition the tower into the \(m\)-level bands
\[
F_i=\bigcup_{k=0}^{m-1}T^{im+k}E,\qquad0\leq i<q.
\]
The \(F_i\)'s are disjoint; their translates \(T^{n-m}F_i\) are also disjoint, since \(T\) is injective. Therefore
\[
\sum_{i=0}^{q-1}\bigl(\mu(F_i)+\mu(T^{n-m}F_i)\bigr)\leq2.
\tag{3.3}
\]
Choose \(i\) for which the summand is at most \(2/q\).

Translate the entire tower by \(T^{im}\), so its base is \(E'=T^{im}E\), its complement is \(T^{im}R\), and its bottom and top \(m\)-bands are \(F_i\) and \(T^{n-m}F_i\). Define \(S\) to follow \(T\) on all levels except the top, to return from the top to the base by \(T^{-(n-1)}\), and to fix the complement:
\[
Sx=
\begin{cases}
Tx,&x\in\bigcup_{k=0}^{n-2}T^kE',\\
T^{-(n-1)}x,&x\in T^{n-1}E',\\
x,&x\in T^{im}R.
\end{cases}
\tag{3.4}
\]
It is a Borel bijection, is nonsingular piece by piece, and satisfies \(S^n=\mathrm{id}\). Its orbits lie in \(T\)-orbits.

For \(|j|\leq m\), the maps \(S^j,T^j\) agree except possibly on the complement and the two boundary bands. Equations (3.2)–(3.3) give an error below \(\varepsilon/2+2/q<\varepsilon\). \(\square\)

Both terms in (3.3) are needed. Choosing a band merely because its own measure is small would give no control of its translated partner.

**Corollary 3.2.** The principal measured relation \(R_T\) is hyperfinite, with a uniform finite class-size bound at each stage.

*Proof.* Let \(K_n=\bigcup_{|j|\leq n}\operatorname{graph}T^j\). Choose \(S_n\) using Theorem 3.1 with power errors smaller than \(2^{-n}/(2n+1)\). Its finite-orbit relation \(H_n\) satisfies \(\nu_s(K_n\setminus H_n)<2^{-n}\).

Set \(R_n=\bigcap_{k\geq n}H_k\). These are Borel full-unit subrelations of \(R_T\), they increase, and each class-size bound is inherited from \(H_n\). Fix \(j\in\mathbb Z\). For \(n\geq|j|\), the union bound gives
\[
 \nu_s(\operatorname{graph}T^j\setminus R_n)
 \leq\sum_{k\geq n}\nu_s(\operatorname{graph}T^j\setminus H_k)
 \leq\sum_{k\geq n}2^{-k}\longrightarrow0.
\]
Thus \(\bigcup_nR_n\) contains every power graph modulo source-counting null sets. There are countably many powers. Remove the union of their exceptional source sets and its countable \(T\)-saturation; nonsingularity makes that saturation null. On the remaining invariant conull Borel space the union is exactly \(R_T\). This tail-intersection proof is independent of invariant means and supplies the finite approximation used later in the array characterization. \(\square\)

## 4. Binary addition and its domain

Let \(X=\{0,1\}^{\mathbb N}\), with the first coordinate the least significant digit. Its tail relation identifies sequences differing in finitely many coordinates. Remove the two countable sets of eventually zero and eventually one sequences, and call the remaining space \(X_*\).

For \(x\in X_*\), let \(k\) be the first coordinate with \(x_k=0\). Define \(Tx\) by changing the preceding ones to zero, changing \(x_k\) to one, and leaving all later digits unchanged. Define \(T^{-1}\) by the inverse rule, using the first one.

**Theorem 4.1.** These rules are inverse Borel bijections of \(X_*\). Their orbits are exactly the tail-equivalence classes in \(X_*\).

*Proof.* Every sequence in \(X_*\) has infinitely many zeros and ones. Thus both carries stop, the rules preserve \(X_*\), and direct inspection makes them inverse. Partition by the first zero or first one to see Borelness.

Every iterate changes finitely many coordinates. Conversely, suppose \(x,y\) agree beyond coordinate \(N\). Let
\[
a=\sum_{j=1}^N2^{j-1}x_j,\qquad
b=\sum_{j=1}^N2^{j-1}y_j.
\]
Then \(T^{\,b-a}x=y\). To verify this, binary addition modulo \(2^L\), for every \(L\geq N\), takes the integer represented by the first \(L\) digits of \(x\) to that represented by \(y\); their difference is \(b-a\). The finite carry rules implement exactly these congruences. Agreement modulo \(2^L\) for every \(L\) means equality of all digits. \(\square\)

Removing only the eventually one sequences would leave the all-zero sequence without a predecessor. Both exceptional tail classes must be removed to obtain the displayed bijection.

*Reference:* In [Takesaki, proof of Theorem XIII.3.17, (iii) implies (iv)], the exceptional-set deletion needs this additional eventually-zero class.

The finite relations that allow changes only in the first \(N\) digits have classes of size \(2^N\) and exhaust the tail relation. This is the **dyadic odometer** model. The prefix matrix construction of the matrix-block lesson applies with two letters instead of three, giving matrix algebras \(M_{2^N}(\mathbb C)\) and inclusions \(A\mapsto A\otimes1_2\).

## 5. Measures on the odometer

For the fair product measure, each prefix replacement preserves measure and \(T\) is nonsingular and measure preserving. More generally, take independent digits with constant probabilities \(p,1-p\), \(0<p<1\).

Each exceptional sequence has measure zero: the probability of matching its first \(N\) digits is at most \(\max(p,1-p)^N\). A countable union is still null. Every finite prefix replacement is nonsingular because all prefix probabilities are positive. The countable carry partition proves that \(T,T^{-1}\) are nonsingular.

**Proposition 5.1.** The odometer is ergodic for each of these product measures.

*Proof.* A \(T\)-invariant event is tail invariant by Theorem 4.1, after discarding a countable saturation of its exceptional set. For each \(N\), invariance under all first-\(N\) prefix replacements means its indicator depends only on the coordinates after \(N\), modulo null sets. This follows by Fubini on the finite prefix set and the remaining product space; every prefix has positive probability.

It is therefore independent of the first \(N\) coordinates. Its integral against every cylinder function is its mean times the cylinder function's integral. Cylinder functions have dense span in \(L^2(X)\), since their sigma-fields generate the product sigma-field. The indicator equals its mean almost everywhere and is consequently zero or one. \(\square\)

For \(p\ne1/2\), this proof gives nonsingularity and ergodicity, while the diagonal-integral state on the prefix matrix algebra is nontracial. Determining the factor's type from its modular spectrum is a further step.

## 6. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 6.1 (a stopping carry).** *Level 1.* Starting with digits \((1,1,0,1,0,\ldots)\), write the first five digits after applying \(T\), and then apply \(T^{-1}\).

*Solution.* The first zero is at coordinate three, so the first five digits become \((0,0,1,1,0)\). The inverse finds the first one at coordinate three, changes it to zero, and changes its two preceding zeros to ones, recovering the original digits.

**Exercise 6.2 (two exceptional classes).** *Level 1.* Show that \(T^{-1}\) cannot be defined by a finite borrowing rule at the all-zero sequence, and \(T\) cannot be defined by a finite carrying rule at the all-one sequence.

*Solution.* The inverse rule needs a first one, which the all-zero sequence lacks. The forward rule needs a first zero, which the all-one sequence lacks. Their finite tail changes form precisely the eventually-zero and eventually-one classes. Removing both classes is countable and leaves both rules defined everywhere.

**Exercise 6.3 (an orbit exponent).** *Level 1.* Two sequences have first four digits \((1,0,1,0)\) and \((0,1,0,1)\), and identical later digits in \(X_*\). Find the exponent taking the first to the second.

*Solution.* Their prefix integers are \(1+4=5\) and \(2+8=10\). The exponent is \(10-5=5\). The proof of Theorem 4.1 verifies the equality on every longer prefix, so this computation includes possible carries correctly.

**Exercise 6.4 (a measure estimate).** *Level 2.* In Theorem 3.1, explain why \(\sum_i\mu(T^{n-m}F_i)\leq1\), without assuming that \(T\) preserves measure.

*Solution.* Injectivity preserves disjointness of the sets \(F_i\), so their translates are disjoint subsets of \(X\). Finite additivity of the probability measure gives the bound. Individual measures may change arbitrarily; only disjointness is used.

**Exercise 6.5 (a biased diagonal state).** *Level 2.* Take \(p=2/5\) for digit zero and \(3/5\) for digit one. On the first-digit matrix algebra, compare the state values of \(e_{01}e_{10}\) and \(e_{10}e_{01}\).

*Solution.* The products are \(e_{00}\) and \(e_{11}\). Diagonal integration gives \(2/5\) and \(3/5\). Thus the original product-measure state is not a trace, although the algebra is still \(M_2(\mathbb C)\) at this finite stage.

## References

[Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The tower construction is the nonsingular form of Rokhlin's lemma.

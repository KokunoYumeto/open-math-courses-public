# Homogeneous groupoid matchings and weighted arrays

A constant Radon–Nikodym derivative lets us compare sets by their masses. An ergodic kernel makes that comparison possible between arbitrary positive sets. We prove the resulting matching and refinement theorems, and identify the two exhaustion conditions that turn the arrays into coordinates for the whole measured relation.

Throughout, \(R\subset X\times X\) is a countable Borel equivalence relation on a standard probability space \((X,\mu)\), and \(\mu\) is nonsingular for \(R\). Statements about maps and sets are modulo null sets. The partial graph presentation and removal of null saturations are proved in 2. Countable presentations and null saturation. Our derivative convention is that of 1. Counting arrows and fixing the derivative:

\[
 \mu(TA)=\int_A\delta(Tx,x)\,d\mu(x)
 \tag{HGA.1}
\]

for every partial orbit bijection \(T\) and measurable \(A\) in its domain. The cocycle identities hold simultaneously on an invariant conull set. A map has **degree \(h\)** if its derivative in (HGA.1) is the constant \(h>0\). We use partial bijections; a map between two subsets need not extend to a bijection of the whole space.

## 1. Counting sheets with the right weight

Let \(H\subset\mathbb R_+^\times\) be countable, and give its point \(h\) mass \(w(h)\), where \(0<w(h)<\infty\). On \(X\times H\) consider the product of \(R\) with the full pair relation on \(H\). Its measure is sigma-finite, since the individual sheets have finite measure.

**Proposition 1.1.** The product derivative is

\[
 \widetilde\delta((y,k),(x,h))
       =\delta(y,x)\frac{w(k)}{w(h)}.
 \tag{HGA.2}
\]

In particular, the expression \(k\delta(y,x)h^{-1}\) requires the sheet weights \(w(h)=h\), up to a common positive scalar.

**Proof.** On a partial graph \(x\mapsto Tx\), take the product graph \((x,h)\mapsto(Tx,k)\). Its source measure on \(A\) is \(w(h)\mu(A)\), whereas its range measure is
\(w(k)\int_A\delta(Tx,x)\,d\mu(x)\). Taking their derivative proves (HGA.2). Countably many such graphs cover the product relation. Conversely, requiring (HGA.2) to have the displayed form for every sheet pair gives \(w(k)/w(h)=k/h\), hence \(w(h)/h\) is constant. \(\square\)

With unweighted counting measure the answer is simply \(\delta(y,x)\). With \(w(h)=h\), the kernel satisfies

\[
 (y,k)\sim_0(x,h)\quad\Longleftrightarrow\quad
 (y,x)\in R,\qquad k=h\,\delta(y,x)^{-1}.
 \tag{HGA.3}
\]

If all cocycle values belong to a subgroup \(S\subset H\), (HGA.3) preserves the coset \(hS\). A proper \(S\) can therefore prevent ergodicity, even when its closure is all of \(\mathbb R_+^\times\).

## 2. A dense ratio range with a nonergodic discrete extension

Here is an explicit distinction between a dense real ratio range and an ergodic extension over a discrete group. Put

\[
 X=\{0,1,2\}^{\mathbb N},\qquad
 (p_0,p_1,p_2)=\frac1{49}(36,9,4),\qquad
 \mu=\bigotimes_{n\ge1}(p_0,p_1,p_2).
 \tag{HGA.4}
\]

Let \(R\) be eventual equality: two sequences are related when they differ in only finitely many coordinates. Let

\[
 H=\{2^a3^b:a,b\in\mathbb Z\},\qquad
 S=\{2^{2a}3^{2b}:a,b\in\mathbb Z\}.
 \tag{HGA.5}
\]


We recall explicitly what is needed about the product probability. A cylinder determined by a word \(u\) has mass \(p(u)=\prod_i p_{u_i}\). These masses define a probability on the cylinder algebra. To check the premeasure property, a cylinder-algebra set that is a disjoint union of countably many such sets has a finite subcover: the sequence space is compact by the diagonal subsequence argument, and cylinder-algebra sets are both open and closed. Disjointness makes every remaining set empty. The measure extension theorem then gives the product measure. Alternatively it can be constructed by recursively partitioning \([0,1)\) into half-open intervals in the proportions \(p_0,p_1,p_2\), assigning each point its nested word. Preimages of cylinders are the corresponding intervals; pushing forward Lebesgue measure gives exactly the same probability. This latter construction needs no separate product extension theorem.

The finite unions of cylinders approximate every measurable set in measure. Indeed, the approximable sets form a sigma-algebra: complement preserves the error, finite unions add errors, and a countable union is first approximated by a finite union using continuity from below. The cylinders generate the Borel sigma-algebra, and null modifications do not change approximation. Cylinder masses also prove independence of disjoint finite coordinate blocks; approximation extends it to the sigma-algebras they generate.

**Proposition 2.1.** The relation in (HGA.4) is hyperfinite, ergodic and nonatomic. Every positive number is in its ratio set. Nevertheless, the kernel (HGA.3) on \(X\times H\) is not ergodic.

**Proof.** Changing a prefix of length \(n\) gives a finite relation with classes of size \(3^n\). These relations increase to \(R\). Replacing a word \(u\) by an equally long word \(v\), while keeping the tail fixed, has derivative

\[
 \delta(vz,uz)=\frac{p(v)}{p(u)}\in S.
 \tag{HGA.6}
\]

The formula holds first on cylinders and then on all measurable subsets by approximation. It proves nonsingularity. The mass of a cylinder of length \(n\) is at most \((36/49)^n\), so every singleton has measure zero. Any atom would have to lie, modulo null sets, in one cylinder at each level and hence in a singleton; thus the measure is nonatomic.

An invariant event \(A\) is unchanged by every prefix replacement. At each fixed length there are finitely many such maps, all nonsingular. Outside their exceptional null sets, all sections of \(1_A\) at that prefix length agree. Thus \(A\) depends only on the coordinates after that length, modulo null sets. It is independent of every finite-coordinate event. Approximate \(A\) itself by such events to obtain \(\mu(A)=\mu(A)^2\), proving ergodicity.

For clarity, a number \(r>0\) belongs to the ratio set when every positive \(A\) and every neighborhood \(V\) of \(r\) admit a positive-domain partial orbit bijection \(T:D\to T(D)\), with \(D,T(D)\subset A\) and derivative in \(V\).

Every \(h\in S\) equals \(p(v)/p(u)\) for two words of the same length: use coordinate changes \(0\leftrightarrow1\) for factors \(4^{\pm1}\), and \(0\leftrightarrow2\) for factors \(9^{\pm1}\), and concatenate. Fix such \(u,v\) and a positive \(A\). For any \(\varepsilon>0\) there is a cylinder \(C\), determined by some first \(m\) coordinates, such that

\[
 \mu(C\setminus A)<\varepsilon\mu(C).
 \tag{HGA.7}
\]

To see this, approximate \(A\) by a finite union \(B\) of cylinders with
\(\mu(A\triangle B)<\eta\). Then \(\mu(B)\ge\mu(A)-\eta\), and
\(\mu(B\setminus A)/\mu(B)\le\eta/(\mu(A)-\eta)\).
Choose \(\eta\) so that this is less than \(\varepsilon\), refine \(B\) to one cylinder length, and select an atom with at most the average relative error.

In the block immediately after \(C\), replace \(u\) by \(v\). The initial domain \(D_0=C\cap[u]\) has mass \(p(u)\mu(C)\), and the map \(T\) has degree \(h\) and stays inside \(C\). Restrict to
\(D=D_0\cap A\cap T^{-1}(A)\). By (HGA.1),

\[
 \mu(D)\ \ge\
 \bigl(p(u)-\varepsilon(1+h^{-1})\bigr)\mu(C).
 \tag{HGA.8}
\]

Choose \(\varepsilon<p(u)/(1+h^{-1})\). This realizes the exact degree \(h\) inside every positive \(A\).

The additive subgroup generated by \(\log4\) and \(\log9\) is dense in \(\mathbb R\). Their ratio is irrational, because a nonzero integer relation would imply \(2^{2a}=3^{2b}\). The pigeonhole principle applied to fractional parts of multiples of that irrational ratio gives arbitrarily small nonzero elements of the subgroup. Given a positive such element \(t\), integer multiples of \(t\) approximate any prescribed real number to within \(t/2\). Exponentiation proves that \(S\) is dense in \(\mathbb R_+^\times\). Every neighborhood of any \(r>0\) therefore contains an \(h\) just realized by (HGA.8). The same argument with \(h\) tending to zero supplies the endpoint zero. The ratio set is \([0,\infty)\), the measured-relation type \(\mathrm{III}_1\) case.

Finally, (HGA.6) and (HGA.3) preserve each of the four sets

\[
 X\times S,\qquad X\times2S,\qquad
 X\times3S,\qquad X\times6S.
 \tag{HGA.9}
\]

Unique prime factorization makes them disjoint, and they cover \(X\times H\). Each contains an entire sheet of positive measure. Thus the discrete extension has a nontrivial invariant set and is not ergodic. \(\square\)

The example concerns the kernel of this particular extension. It does not rule out finding a different equivalent probability with an ergodic modulus kernel. Nor does it identify the discrete extension with the extension over \(\mathbb R_+^\times\) carrying its Haar measure.

## 3. Exact matching from an ergodic kernel

Assume now that \(R_0=\{(y,x)\in R:\delta(y,x)=1\}\) is ergodic. Say that \(h>0\) **occurs** if the arrows of degree \(h\) have positive source-counting measure. By the countable graph presentation, this is equivalent to the existence of a positive-domain partial orbit bijection of degree \(h\). Denote the set of occurring degrees by \(S_\mu\).

**Lemma 3.1.** If \(h\in S_\mu\), any positive sets \(A,B\) contain positive subsets joined by a degree-\(h\) partial orbit bijection.

**Proof.** First note that any two positive sets \(E,F\) are joined on positive subsets by a degree-one map. Their \(R_0\)-saturations are conull by ergodicity. Enumerate the partial graphs of \(R_0\). Some graph has a positive set of points in \(E\) whose images lie in \(F\), since these domains cover \(E\) modulo a null set.

Choose a degree-\(h\) map \(T:D\to E\) with positive domain. A degree-one map \(P\) joins a positive subset of \(A\) to a subset of \(D\). Its image under \(T\) is positive. A degree-one map \(Q\) joins a positive subset of that image to a subset of \(B\). Restrict \(P\)'s domain to the inverse image of the domain of \(Q\). Then \(QTP\) has positive domain and degree \(h\). \(\square\)

**Theorem 3.2 (homogeneous matching).** Suppose \(h\in S_\mu\) and \(A,B\) are measurable. If

\[
 \mu(B)=h\mu(A),
 \tag{HGA.10}
\]

there is a degree-\(h\) partial orbit bijection from \(A\) onto \(B\), modulo null sets. More generally, if \(\mu(B)\ge h\mu(A)\), such a map sends all of \(A\) into \(B\).

**Proof.** Enumerate all degree-\(h\) partial graphs as \(T_1,T_2,\ldots\); restricting the countable graphs of \(R\) to the measurable derivative level \(h\) gives this enumeration. At stage \(n\), retain every point of the still unused part of \(A\) on which \(T_n\) lands in the still unused part of \(B\). The retained maps have disjoint domains and disjoint ranges. Their union \(T\) is a measurable bijection between its domain and range, with measurable inverse, and has degree \(h\).

Let \(A_\infty,B_\infty\) be the unused sets. No enumerated graph joins positive parts of them: such points would have been matched when that graph was considered. Lemma 3.1 implies that they cannot both have positive measure. If \(t\) is the measure already used in \(A\), their masses are
\(\mu(A)-t\) and \(\mu(B)-ht\). Under the inequality in the statement, positive residual mass in \(A\) would force positive residual mass in \(B\), a contradiction. Under equality, both residual masses vanish. \(\square\)

The occurring degrees form a subgroup. Degree one occurs on the diagonal. Inversion sends an occurring degree to its reciprocal. To multiply two degrees, connect the positive range of the first witnessing map to the positive domain of the second by a degree-one map, and restrict before composing. This proves closure under multiplication without claiming that every value in a chosen ambient group occurs.

A partial matching is the precise conclusion: a bijection from \(X\) onto a proper positive subset of \(X\) cannot be the restriction of a bijection \(X\to X\).

## 4. Building a weighted matrix of orbit maps

Assume additionally that \(\mu\) is nonatomic. We first justify the division of sets into prescribed masses. A countable Borel separating family gives a Borel injection \(j:X\to[0,1]\), for example
\(j(x)=\sum_{n\ge1}2\,3^{-n}\mathbf1_{B_n}(x)\).
The pushforward of \(\mu\) under \(j\) has no atoms. Its distribution function is continuous: continuity of measure from above and below shows that its jump at \(t\) is precisely the mass of \(\{t\}\). Its values run from zero to one. The intermediate value theorem therefore supplies cuts of any prescribed masses. The same argument applies to every positive measurable subset with its normalized measure.

Let \(a_0,\ldots,a_{d-1}\) belong to \(S_\mu\), with \(d\ge2\), and put

\[
 Z=\sum_{i=0}^{d-1}a_i,\qquad p_i=a_i/Z.
 \tag{HGA.11}
\]

Partition \(X\) into \(Z_0,\ldots,Z_{d-1}\) of masses \(p_0,\ldots,p_{d-1}\). Theorem 3.2 supplies maps

\[
 v_i:Z_0\longrightarrow Z_i,\qquad
 \deg v_i=p_i/p_0=a_i/a_0,
 \tag{HGA.12}
\]

and we take \(v_0\) to be the identity. Define

\[
 U_{ij}=v_iv_j^{-1}:Z_j\longrightarrow Z_i.
 \tag{HGA.13}
\]

These are measurable partial orbit bijections satisfying

\[
 U_{ij}U_{jk}=U_{ik},\qquad
 U_{ij}^{-1}=U_{ji},\qquad
 \delta(U_{ij}x,x)=p_i/p_j.
 \tag{HGA.14}
\]

The first two identities follow by cancellation of \(v_j^{-1}v_j\); the derivative identity follows from the cocycle law. The union of the graphs is a finite subrelation of \(R\), with one point in each cell in every class. There are exactly \(d\) points per class, after removing the finitely many exceptional null sets.

This proves existence of a weighted full matrix of orbit maps using only nonatomicity, ergodicity of \(R_0\), and occurrence of the specified degrees. No hyperfiniteness assumption is used.

## 5. Refinement without changing earlier maps

Suppose a finite array is indexed by a finite set \(W\), its cells are \(Z_u\), and its maps \(U_{uv}:Z_v\to Z_u\) have degrees \(q_u/q_v\), where \(\mu(Z_u)=q_u>0\). Fix a base index \(o\in W\). The restriction of \(R_0\) to \(Z_o\) is ergodic. Indeed, a nontrivial invariant subset and its complement inside \(Z_o\) would be joined by a positive degree-one map, contradicting invariance. Lemma 3.1 also shows that every degree in \(S_\mu\) occurs inside \(Z_o\).

Partition \(Z_o\) into \(B_i\) of masses \(q_op_i\), and construct within \(Z_o\) the array \(V_{ij}:B_j\to B_i\) of degree \(p_i/p_j\). Define

\[
 \begin{split}
 Z_{u,i}&=U_{uo}(B_i),\\
 W_{(u,i),(v,j)}
   &=U_{uo}\,V_{ij}\,U_{ov}.
 \end{split}
 \tag{HGA.15}
\]

The cells partition \(X\), and

\[
 \mu(Z_{u,i})=q_up_i,\qquad
 \deg W_{(u,i),(v,j)}=\frac{q_up_i}{q_vp_j}.
 \tag{HGA.16}
\]

Cancellation of \(U_{ov}U_{vo}\) and the matrix laws for \(V\) prove all matrix laws for \(W\). Moreover,

\[
 W_{(u,i),(v,i)}=U_{uv}|_{Z_{v,i}}.
 \tag{HGA.17}
\]

Thus the old map is exactly the union of these restrictions. Earlier maps are retained, rather than merely approximated.

Iterating gives a cell \(Z_u\) for each word \(u\) of length \(n\), with

\[
 \mu(Z_u)=p(u)=\prod_{\ell=1}^n p_{u_\ell},\qquad
 \deg U_{uv}=p(u)/p(v).
 \tag{HGA.18}
\]

The finite relations increase. Countably many identities and exceptional sets are involved; removing their \(R\)-saturations makes all refinements and matrix laws simultaneous on an invariant conull set.

## 6. When the arrays code the whole relation

Two further conditions have distinct roles. Assume that the word arrays of Section 5 satisfy:

1. The sigma-algebra generated by their cells is the whole measurable sigma-algebra modulo null sets.
2. On an invariant conull set, \(R\) is the union of their finite array relations.

**Theorem 6.1.** Under these conditions, the address map identifies \((X,\mu,R)\), modulo null sets, with the product probability \(\bigotimes_{n\ge1}(p_0,\ldots,p_{d-1})\) and eventual equality on \(\{0,\ldots,d-1\}^{\mathbb N}\).

**Proof.** Assign to \(x\) the word of cells containing it at every level. Refinement gives a unique infinite address \(\Phi(x)\), and the map is Borel. Equation (HGA.18) gives the product probabilities of all cylinders. Finite cylinder approximation, proved in Section 2 with the same argument for \(d\) letters, identifies the pushforward measure.

Choose a countable Borel family separating the points of \(X\). By condition 1, each member agrees modulo a null set with a set measurable with respect to the address coordinates. Such a set is a preimage under \(\Phi\) of a Borel set in the sequence space: the class of preimages is a sigma-algebra and the cylinder preimages generate the address sigma-algebra. Removing the countable union of the exceptional sets, equal addresses imply equal membership in every separating set, hence equal points. Remove also the \(R\)-saturation of that null set.

The injective Borel image theorem, in the precise form recorded in 1. Objects and the existing symmetry proofs, makes this restricted map a Borel isomorphism onto its Borel image. The image is conull for the product probability, since that probability is the pushforward.

A level-\(n\) map changes the first \(n\) address letters and leaves every later letter fixed, by repeated use of (HGA.17). Condition 2 therefore sends related points to eventually equal addresses. Conversely, suppose two addresses agree after the \(n\)-th letter. Apply the level-\(n\) map taking the first point's prefix to the second point's prefix. The resulting point has exactly the second address. Injectivity gives equality with the second point, so the original points are related. The image is invariant under every finite prefix replacement, because every level map is defined on the appropriate cell in the invariant conull set. This proves the measured-relation isomorphism. \(\square\)

The construction of Section 5 alone supplies neither exhaustion condition. For example, take a product of this Bernoulli tail relation with the fair binary tail relation, and use only prefix maps in the first coordinate. All formulas (HGA.14)–(HGA.18) still hold. The cell sigma-algebra forgets the second coordinate, and the union of these finite relations cannot change it. Both failures are visible without changing any finite-array identity.

## 7. The three-letter model and both weight parameters

For \(0<\lambda_1,\lambda_2<1\), take the three probabilities

\[
 (p_0,p_1,p_2)=\frac{(1,\lambda_1,\lambda_2)}
                         {1+\lambda_1+\lambda_2}.
 \tag{HGA.19}
\]

In a word \(u\) of length \(n\), let \(k_1(u)\) and \(k_2(u)\) count the letters 1 and 2. Then

\[
 p(u)=\frac{\lambda_1^{k_1(u)}\lambda_2^{k_2(u)}}
                  {(1+\lambda_1+\lambda_2)^n}.
 \tag{HGA.20}
\]

There are \(n!/(k_1!k_2!(n-k_1-k_2)!)\) such words: choose the \(k_1\) positions of the first letter and then the \(k_2\) positions of the second. Summing the word masses gives one by multiplying \(n\) copies of \(p_0+p_1+p_2=1\).

Replacing prefix \(v\) by prefix \(u\) has degree

\[
 \frac{p(u)}{p(v)}
 =\lambda_1^{k_1(u)-k_1(v)}
  \lambda_2^{k_2(u)-k_2(v)}.
 \tag{HGA.21}
\]

Both factors are necessary. Already at length one, the map from the 0-cell to the 1-cell has degree \(\lambda_1\); a formula containing only the second factor would incorrectly make it measure preserving.

The model is nonatomic and ergodic by the proof of Proposition 2.1. If \(\log\lambda_1/\log\lambda_2\) is irrational, its ratio set is \([0,\infty)\): every element of \(\lambda_1^{\mathbb Z}\lambda_2^{\mathbb Z}\) is a ratio of equally long word masses, (HGA.7)–(HGA.8) realize it inside every positive set, and the same pigeonhole argument proves density.

For \(\lambda_1=1/2\), \(\lambda_2=1/3\), the probabilities are \((6,3,2)/11\). At level two the exact masses are:

| First letter / second letter | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | \(36/121\) | \(18/121\) | \(12/121\) |
| 1 | \(18/121\) | \(9/121\) | \(6/121\) |
| 2 | \(12/121\) | \(6/121\) | \(4/121\) |

Their numerators sum to \(121\). For example, the map \(01\mapsto12\) has degree \(6/18=1/3\), while \(00\mapsto11\) has degree \(9/36=1/4\). These are exactly (HGA.21).

## 8. Checks and applications of the hypotheses

**Problem 1.** An ergodic relation has derivative values in a fixed dense countable group \(H\). Does every \(h\in H\) necessarily occur?

**Solution.** No. In Proposition 2.1 the values are in \(S=2^{2\mathbb Z}3^{2\mathbb Z}\subset H=2^{\mathbb Z}3^{\mathbb Z}\), so the value \(2\) never occurs. The real ratio set is nevertheless all of \([0,\infty)\). Density in the real topology does not add exact values to a discrete group.

**Problem 2.** Let \(H\) be countable and let \(w(h)=h\). Must \(X\times H\) have finite measure?

**Solution.** No: its mass is \(\sum_{h\in H}h\), which is infinite for every nontrivial subgroup of \(\mathbb R_+^\times\). Indeed, either \(h>1\) or \(h^{-1}>1\) for a nonidentity element, and its positive powers have divergent sum. Sigma-finiteness is sufficient for Proposition 1.1; every single sheet has finite mass.

**Problem 3.** Why is the equality of masses essential for an onto homogeneous matching?

**Solution.** Formula (HGA.1) gives \(\mu(B)=h\mu(A)\) for any onto degree-\(h\) map. Theorem 3.2 proves sufficiency when the kernel is ergodic and \(h\) occurs. With the inequality \(\mu(B)>h\mu(A)\), the same construction matches all of \(A\), but the unused part of \(B\) has exactly the positive mass \(\mu(B)-h\mu(A)\).

**Problem 4.** Can refining weighted arrays replace a proof of measured-groupoid classification?

**Solution.** Only when their hypotheses and both exhaustion conditions are proved. Sections 3–5 assume an ergodic modulus kernel and actual occurrence of the requested degrees. Section 6 additionally requires generation of the unit sigma-algebra and exhaustion of all relation arrows. Its product example shows exactly what finite refinement alone can miss. An isomorphism of the associated factors, without preservation of their specified diagonals, does not supply either condition.

## References

- M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, pp. 396–398, Theorem 4.23, Lemmas 4.24–4.25, Definition 4.26 and Lemma 4.27. Sections 1 and 7 derive the sheet measure and both array parameters directly. Section 2 distinguishes a discrete-kernel assertion from real ratio-set information.
- Groupoid reductions and modular matrix blocks, Section 2; Relation weights and measure change, Section 1; Relation symmetries and weight covariance, Section 1.

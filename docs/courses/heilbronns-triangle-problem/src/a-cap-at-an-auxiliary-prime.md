# A cap at an auxiliary prime

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The determinant obstruction of [A determinant obstruction from field norms](a-determinant-obstruction-from-field-norms.md) works modulo \(h\) and cannot see determinant zero: three integer columns can be linearly dependent while their residues modulo \(h\) are not. This lesson adds a second, independent condition at a large prime \(q\). The residues modulo \(q\) of the sampled columns are taken from a random set \(V\subseteq\mathbb F_q^3\) with no three points on a line, obtained from a piece of an elliptic quadric by a restricted random translation and a random invertible linear map. Three distinct points of \(V\) then admit no short integer linear relation; and the probability that prescribed residues lie in \(V\) is bounded in three regimes, according to how degenerate the residues are. These bounds feed the zero-determinant count of the seventh lesson.

We use primes in intervals (Lemma 4.3 of [Small triangles and the plan](small-triangles-and-the-plan.md)) and elementary linear algebra over the field \(\mathbb F_q\): \(\mathrm{GL}_3(\mathbb F_q)\) acts transitively on ordered pairs of linearly independent vectors (extend each pair to a basis), and the affine maps \(v\mapsto Gv+c\) act transitively on ordered *affinely independent* triples, those \((u^{(1)},u^{(2)},u^{(3)})\) with \(u^{(2)}-u^{(1)}\) and \(u^{(3)}-u^{(1)}\) linearly independent. For a group acting transitively on a finite set and a uniform group element \(g\), the point \(g^{-1}x_0\) is uniform on the set (all fibres of \(g\mapsto g^{-1}x_0\) are cosets of one stabilizer).

## 1. A cap in a box

**Lemma 1.1 (cap).** Let \(q\) be an odd prime and \(1\leq w\leq q\). There is a set \(S\subseteq\{0,\ldots,w-1\}^3\subseteq\mathbb F_q^3\) with \(|S|\geq w^3/q\) such that no affine line of \(\mathbb F_q^3\) contains three distinct points of \(S\).

*Proof.* Choose a nonsquare \(\nu\in\mathbb F_q\), put \(Q(x,y)=x^2-\nu y^2\) and \(\Gamma=\{(x,y,Q(x,y)):x,y\in\mathbb F_q\}\), a set of \(q^2\) points. \(Q\) vanishes only at \((0,0)\): if \(y\neq0\) and \(Q(x,y)=0\), then \(\nu=(x/y)^2\) would be a square. Let \(\{p+tv:t\in\mathbb F_q\}\) be a line. If \((v_1,v_2)\neq(0,0)\), its points on \(\Gamma\) satisfy \(p_3+tv_3=Q(p_1+tv_1,p_2+tv_2)\), a quadratic equation in \(t\) with leading coefficient \(Q(v_1,v_2)\neq0\): at most two solutions. If \((v_1,v_2)=(0,0)\), the line meets \(\Gamma\) once. Translates of \(\Gamma\) have the same property.

For \(b\) uniform in \(\mathbb F_q^3\), a point \(x\) lies in \(b+\Gamma\) exactly when \(b\in x-\Gamma\), with probability \(q^2/q^3=1/q\). So the expected number of points of the box \(\{0,\ldots,w-1\}^3\) in \(b+\Gamma\) is \(w^3/q\), and some \(b\) gives at least this many. Let \(S\) be the intersection of that translate with the box. \(\square\)

**Parameters.** Let \(h\geq2\) be the main modulus, and put
\[
\begin{gathered}
H=h^2,\\
h^{100}<q\leq2h^{100},\\
w=\Bigl\lfloor\frac q{1000H^2}\Bigr\rfloor ,
\end{gathered}\tag{1.1}
\]
with \(q\) prime. Such \(q\) exists for large \(h\) by Lemma 4.3 of the first lesson; then \(q\geq2000H^2\) and \(\frac q{2000H^2}\leq w\leq\frac q{1000H^2}\). We identify \(0,\ldots,w-1\) with their residues. Fix a set \(S\) as in Lemma 1.1, chosen before any randomness, and let \(s=|S|\); then
\[
s\geq\frac{w^3}q\geq\frac{q^2}{2000^3H^6}.\tag{1.2}
\]

## 2. Allowed shifts and the random set

For \(t\in\mathbb F_q\) let \(\|t\|_q\) be the least absolute value of an integer representative of \(t\). Let the set \(\mathcal A\) of *allowed shifts* consist of all \(a\in\mathbb F_q^3\) such that, for every \(1\leq m\leq3H\),
\[
\|ma_1\|_q>3Hw;\tag{2.1}
\]
choose \(a\) uniformly in \(\mathcal A\) and, independently, \(G_q\) uniformly in \(\mathrm{GL}_3(\mathbb F_q)\), and put
\[
V=G_q(a+S).\tag{2.2}
\]

**Lemma 2.1 (the random set).** Let \(H\geq1\), \(q\geq2000H^2\) prime, \(w=\lfloor q/(1000H^2)\rfloor\), and \(S\subseteq\{0,\ldots,w-1\}^3\) without three distinct collinear points.

(a) \(|\mathcal A|\geq q^3/2\).

(b) For every \(a\in\mathcal A\) and invertible \(G_q\), \(|V|=|S|\), \(0\notin V\), and \(V\) has no three distinct collinear points.

(c) Let \(x\in\mathbb Z^3\setminus\{0\}\) with \(|x|\leq H\), and \(u^{(1)},u^{(2)},u^{(3)}\in V\). The relation in \(\mathbb F_q^3\)
\[
\sum_{j=1}^3x_ju^{(j)}=0\tag{2.3}
\]
is impossible if \(x_1+x_2+x_3\neq0\), and, if \(x_1+x_2+x_3=0\), it is impossible whenever the three points are affinely independent. In particular (2.3) is impossible for three distinct points of \(V\).

*Proof.* (a) Since \(3Hw\leq3q/(1000H)<q/2\), the residues \(t\) with \(\|t\|_q\leq3Hw\) number exactly \(6Hw+1\). For each \(1\leq m\leq3H<q\), multiplication by \(m\) is a bijection of \(\mathbb F_q\), so a uniform \(a\) violates the condition for \(m\) with probability \((6Hw+1)/q\). By the union bound,
\[
\begin{aligned}
\Pr(a\notin\mathcal A)&\leq\frac{3H(6Hw+1)}q\\
&\leq\frac{18}{1000}+\frac3{2000H}<\frac12 .
\end{aligned}
\]
(b) Invertible affine maps preserve cardinality and lines. If \(a+v=0\) with \(v\in S\), then \(\|a_1\|_q=\|v_1\|_q\leq w-1\leq3Hw\), contradicting the condition with \(m=1\); so \(0\notin a+S\), and \(0\notin V\).

(c) Write \(u^{(i)}=G_q(a+v^{(i)})\) with \(v^{(i)}\in S\) and \(m=x_1+x_2+x_3\in\mathbb Z\). Applying \(G_q^{-1}\) to (2.3) and taking first coordinates gives \(ma_1=-\sum_ix_iv^{(i)}_1\) in \(\mathbb F_q\). If \(m\neq0\), then \(1\leq|m|\leq3H\), and the integer \(-\sum_ix_iv^{(i)}_1\) (with representatives \(0\leq v^{(i)}_1<w\)) has absolute value at most \(3H(w-1)\); so \(\||m|a_1\|_q=\|ma_1\|_q\leq3Hw\), contradicting \(a\in\mathcal A\). If \(m=0\), the residues of \(x_1,x_2,x_3\) are not all zero (since \(0<|x_i|\leq H<q\) for some \(i\)) and add up to zero; substituting \(x_3=-x_1-x_2\) gives \(x_1(u^{(1)}-u^{(3)})+x_2(u^{(2)}-u^{(3)})=0\) with \((x_1,x_2)\not\equiv(0,0)\), so the triple is not affinely independent. Three distinct points of \(V\) are affinely independent by (b). \(\square\)

## 3. Inclusion weights

For an integer \(3\times3\) matrix \(A\) let \(\rho(A)\) be the probability, over \(a\) and \(G_q\) with \(S\) fixed, that all three columns of \(A\bmod q\) lie in \(V\), and define the *weight*
\[
W(A)=\Bigl(\frac{q^3}s\Bigr)^3\rho(A).\tag{3.1}
\]
The normalization makes \(W\) about one for generic columns.

**Proposition 3.1 (weights).** There is an absolute constant \(C\) such that:

- \(W(A)\leq C\) if the columns of \(A\bmod q\) are affinely independent;
- \(W(A)\leq C\,q^3/s\) if \(\operatorname{rank}(A\bmod q)\geq2\);
- \(W(A)\leq C\,(q^3/s)^2\) always.

If \(W(A)>0\), no column of \(A\bmod q\) is zero, and the columns are affinely independent or two of them are equal. If the columns are affinely independent and \(W(A)>0\), there is no \(x\in\mathbb Z^3\setminus\{0\}\) with \(|x|\leq H\) and \(Ax\equiv0\pmod q\).

*Proof.* *Removing the restriction on \(a\).* If \(a\) is uniform in all of \(\mathbb F_q^3\), then, given \(G_q\), \(G_qa\) is uniform, so \(v\mapsto G_qv+G_qa\) is a uniform element of the affine group. Conditioning on the event \(a\in\mathcal A\), of probability at least \(\frac12\) (Lemma 2.1(a)), at most doubles the probability of any event.

*Affinely independent columns.* For a uniform affine map \(g\) the inverse image of a fixed affinely independent ordered triple is uniform among the \(q^3(q^3-1)(q^3-q)\) such triples; the triple lies in \(g(S)\) exactly when its inverse image lies in \(S^3\), which contains at most \(s^3\) of them. So
\[
W(A)\leq\frac{2q^9}{q^3(q^3-1)(q^3-q)}\leq C .
\]
*Rank at least two.* Fix any allowed \(a\) and put \(S_a=a+S\). If two of the target columns are linearly independent, their inverse image under a uniform \(G_q\) is uniform among the \((q^3-1)(q^3-q)\) ordered independent pairs, of which at most \(s^2\) lie in \(S_a^2\); requiring the third column too only lowers the probability. So \(W(A)\leq\frac{q^9}{s^3}\cdot\frac{s^2}{(q^3-1)(q^3-q)}\leq C\frac{q^3}s\) for each allowed \(a\), and hence after averaging over \(a\).

*All matrices.* A zero target column never lies in \(V\) (Lemma 2.1(b)). Otherwise fix one nonzero target column; its inverse image under \(G_q\) is uniform among the \(q^3-1\) nonzero vectors, and \(S_a\) consists of \(s\) nonzero vectors. So \(W(A)\leq\frac{q^9}{s^3}\cdot\frac s{q^3-1}\leq C(q^3/s)^2\).

*Support.* If \(W(A)>0\), some outcome puts all three columns in \(V\): none is zero, and if they are pairwise distinct they are affinely independent (no three collinear points in \(V\)); otherwise two are equal. For affinely independent columns in \(V\), Lemma 2.1(c) excludes \(Ax\equiv0\) with \(0<|x|\leq H\). \(\square\)

**How the weights are used.** In the sampling of the sixth lesson, \((a,G_q)\) is chosen once, independently of everything at the main modulus, and every sampled column gets its residue modulo \(q\) uniformly from \(V\), independently. Since \(|V|=s\) for every outcome, a prescribed ordered triple of residues, repetitions allowed, is obtained with probability
\[
\frac{\rho(A)}{s^3}=\frac{W(A)}{q^9},\tag{3.2}
\]
where \(A\) is any integer matrix with these residues as columns. The value does not change when conditioning on anything at the main modulus.

## 4. Exercises

**4.1.** For \(q=3\) and \(\nu=2\), list \(\Gamma\) and check directly that no line of \(\mathbb F_3^3\) meets it in three points.

**4.2.** Why is the translation \(a\) restricted? Suppose \(a=0\) and \(S\) contains points \(v,v',v''\) with \(v''=v+v'\) as integer vectors. Find a short relation (2.3) among three points of \(V\) whose coefficients do not add up to zero, and explain how the condition \(a\in\mathcal A\) excludes it.

**4.3.** Show that the three bounds of Proposition 3.1 are of the right order: for a generic \(A\), \(W(A)\) is close to \(1\).

**4.4.** Check the identity (3.2) in a tiny case: \(S\) with two points, and a target triple with all three columns equal.

**4.5.** In the proof of Proposition 3.1, why does conditioning on \(a\in\mathcal A\) at most double probabilities?

## 5. Solutions

**4.1.** Over \(\mathbb F_3\), \(-2=1\), so \(Q(x,y)=x^2+y^2\) and \(\Gamma\) consists of the nine points \((x,y,x^2+y^2)\): third coordinate \(0\) at \((0,0)\), \(1\) at the four points with exactly one of \(x,y\) nonzero, and \(2\) at the four points with both nonzero. A line with direction \((v_1,v_2,v_3)\), \((v_1,v_2)\neq(0,0)\), meets \(\Gamma\) at the roots of a quadratic in the parameter with leading coefficient \(v_1^2+v_2^2\neq0\) (as \(-1\) is not a square modulo \(3\)), so at most two points; a line with direction \((0,0,1)\) meets \(\Gamma\) once.

**4.2.** With \(a=0\), \(G_qv+G_qv'-G_qv''\) equals \(G_q(v+v'-v'')=0\): the relation \(x=(1,1,-1)\), of norm \(\sqrt3\leq H\), with coefficient sum \(1\). For \(a\in\mathcal A\) the same three points of \(S\) give points \(G_q(a+v)\), and the relation would force \(1\cdot a_1=-(v_1+v'_1-v''_1)=0\), so \(\|a_1\|_q=0\leq3Hw\), which \(\mathcal A\) excludes. In general a coefficient sum \(m\neq0\) leaves the term \(ma_1\), which the restriction keeps away from the small integers that the points of \(S\) can produce.

**4.3.** For three columns in general position, the probability that a uniform affine image of \(S\) contains them is about \(s^3/q^9\) (each of three nearly independent events of probability \(s/q^3\)), so \(W\approx1\); the bound \(C\) loses only the factor \(2\) from the restriction and the ratio \(q^9/(q^3(q^3-1)(q^3-q))\).

**4.4.** All three residues equal \(t\): the probability that three independent uniform choices from \(V\) all equal \(t\) is \(\mathbf 1\{t\in V\}/s^3\), whose expectation is \(\Pr(t\in V)/s^3\), and \(W(A)/q^9=\Pr(t\in V)/s^3\) by (3.1).

**4.5.** For an event \(E\) and \(a\) uniform in \(\mathbb F_q^3\), Lemma 2.1(a) gives \(\Pr(a\in\mathcal A)\geq\frac12\), so
\[
\begin{aligned}
\Pr(E\mid a\in\mathcal A)&=\frac{\Pr(E\cap\{a\in\mathcal A\})}{\Pr(a\in\mathcal A)}\\
&\leq2\Pr(E).
\end{aligned}
\]

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
- A. Barlotti (1956) studied caps, sets without three collinear points, in finite three-dimensional spaces, including the elliptic quadric; he is named for credit.

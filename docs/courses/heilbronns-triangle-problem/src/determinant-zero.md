# Determinant zero

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Three sampled points are collinear exactly when their integer columns have determinant zero. This case escapes the lattice count of [Counting lattice matrices](counting-lattice-matrices.md), which needs a nonzero determinant; three rows can lie in one integral plane. Here we count weighted singular matrices by their *null vector*, the primitive integer relation \(x\) with \(Ax=0\). The rows of \(A\) are then lattice vectors orthogonal to \(x\), and a plane lattice count applies. The weights of [A cap at an auxiliary prime](a-cap-at-an-auxiliary-prime.md) do the rest: if the residues modulo \(q\) are affinely independent, short relations are excluded, so \(x\) is long; if two residues coincide, either the rows satisfy an extra congruence modulo \(q\), or the relation \(x\) is very special and rare. This proves the remaining case of Proposition 3.1 of [Sampling integer columns](sampling-integer-columns.md).

Notation: the digit matrix \(C\) is fixed, with row lattice \(\Lambda=\Lambda_C\) of index \(I=DE\), \(D=B^b\), \(E=B^e\), \(0\leq b\leq e\leq k\), and \(E\mathbb Z^3\subseteq\Lambda\) (Lemma 1.1 of [Residue matrices and their orbits](residue-matrices-and-their-orbits.md)); \(h=B^k\), \(H=h^2\), \(q>h^{100}\) prime, the box \(\mathcal B\) and \(N=(hq)^{10}\), and the weight \(W\). Constants \(C\) are absolute unless said otherwise.

## 1. The statement

**Proposition 1.1 (weighted zero-determinant count).** Let \(\mathcal Z\) be the set of integer \(3\times3\) matrices whose columns lie in \(\mathcal B\), whose rows lie in \(\Lambda\), whose determinant is zero, and whose three projected columns are pairwise distinct. Then
\[
\sum_{A\in\mathcal Z}W(A)\leq C\log(2N)\frac{N^6}{I^2},
\]
with \(C\) independent of the digit matrix \(C\).

## 2. Plane lattices orthogonal to a relation

**Lemma 2.1 (plane data).** For a primitive \(x\in\mathbb Z^3\) let \(\Lambda_x=\Lambda\cap x^\perp\), let \(g(x)>0\) generate \(x\cdot\Lambda\), and \(J_x=\det\Lambda_x\). Then
\[
\begin{gathered}
g(x)\mid E,\qquad J_x=\frac{I\,|x|}{g(x)},\\
\frac{g(x)^3}I\leq h^2 .
\end{gathered}\tag{2.1}
\]
The reduction of \(\Lambda_x\) modulo \(q\) is the whole plane \(\Pi_x=\{v\in\mathbb F_q^3:v\cdot\bar x=0\}\), where \(\bar x=x\bmod q\neq0\). If \(\Gamma\subseteq\Lambda_x\) has index \(m\), the ordered triples of vectors of \(\Gamma\) of length at most \(4N\) that span a plane number at most
\[
C\,\frac{N^6}{(mJ_x)^3}.\tag{2.2}
\]

*Proof.* As \(x\) is primitive, \(x\cdot\mathbb Z^3=\mathbb Z\), and \(E\mathbb Z=x\cdot E\mathbb Z^3\subseteq x\cdot\Lambda=g(x)\mathbb Z\), so \(g(x)\mid E\). The formula for \(J_x\) is Lemma 3.2 of the second lesson, and \(g(x)^3/I\leq E^3/(DE)=E^2/D\leq h^2\).

A primitive vector is not divisible by \(q\), so \(\bar x\neq0\). Choose \(z\in\mathbb Z^3\) with \(x\cdot z=1\). An integer lift \(v\) of a point of \(\Pi_x\) has \(x\cdot v=qa'\) for an integer \(a'\), and \(v-qa'z\in\mathbb Z^3\cap x^\perp\) is a lift of the same point; so \(\mathbb Z^3\cap x^\perp\) reduces onto \(\Pi_x\). Multiplying by \(E\), which is prime to \(q\), the lattice \(E(\mathbb Z^3\cap x^\perp)\subseteq\Lambda_x\) still reduces onto \(\Pi_x\).

A triple counted in (2.2) contains two independent vectors of length at most \(4N\), so the second successive length of \(\Gamma\) is at most \(4N\). By Lemma 3.1(a) of the second lesson each vector has at most \(36(4N)^2/\det\Gamma\) choices, and \(\det\Gamma=mJ_x\) (Lemma 1.1 of the second lesson, in coordinates given by a basis of \(\Lambda_x\)). \(\square\)

**Lemma 2.2 (a moment bound).** For \(R\geq h\),
\[
\sum_{\substack{x\ \text{primitive}\\ R\leq|x|<2R}}g(x)^3\leq C\,R^3I .
\]

*Proof.* By Lemma 2.1, \(g(x)=B^{a(x)}\) with \(0\leq a(x)\leq e\). For \(0\leq j\leq e\), \(B^j\mid g(x)\) means \(x\cdot v\equiv0\pmod{B^j}\) for all \(v\in\Lambda\). The lattice \(\Lambda\) is the integer row span of an integer lift \(\tilde C\) of \(C\) plus \(h\mathbb Z^3\), and \(B^j\mid h\); so the condition is \(Cx\equiv0\pmod{B^j}\). Writing \(C=P\operatorname{diag}(1,D,E)Q\) and \(y=Qx\) (a bijection of \((\mathbb Z/B^j)^3\)), the condition becomes \(y_1\equiv0\), \(Dy_2\equiv0\), \(Ey_3\equiv0\pmod{B^j}\); the third is automatic since \(j\leq e\). So a fraction \(B^{-j-\max(j-b,0)}\) of the residue classes modulo \(B^j\) satisfies it. Each class contains at most \((4R/B^j+1)^3\leq125(R/B^j)^3\) integer vectors of length less than \(2R\), since \(R\geq h\geq B^j\). Bound \(g(x)^3=B^{3a(x)}\leq\sum_{j=0}^{a(x)}B^{3j}\) and drop primitivity. For each \(j\), the vectors \(x\) with \(B^j\mid g(x)\) and \(|x|<2R\) lie in \(B^{3j}B^{-j-\max(j-b,0)}\) residue classes, with at most \(125(R/B^j)^3\) vectors in each; so there are at most \(125R^3B^{-j-\max(j-b,0)}\) of them. Hence
\[
\begin{aligned}
\sum_xg(x)^3&\leq125R^3\sum_{j=0}^eB^{3j}B^{-j-\max(j-b,0)}\\
&=125R^3\sum_{j=0}^eB^{2j-\max(j-b,0)} .
\end{aligned}
\]
The exponent \(2j-\max(j-b,0)\) increases strictly with \(j\) and equals \(b+e\) at \(j=e\); since \(B\geq2\), the sum is at most \(2B^{b+e}=2I\). \(\square\)

## 3. Proof of Proposition 1.1

*The null vector.* Let \(A\in\mathcal Z\). Its columns are nonzero (third coordinates at least \(N\)) and no two are proportional (their projections differ), so \(A\) has rank two and its null space is spanned by a primitive \(x\in\mathbb Z^3\), unique up to sign. All coordinates of \(x\) are nonzero: if, say, \(x_3=0\), then \(x_1u^{(1)}+x_2u^{(2)}=0\) would make two columns proportional. The null space is orthogonal to the rows; a primitive multiple of the cross product of two independent rows (each of length less than \(4N\)) generates it, so \(|x|\leq16N^2\). Every row of \(A\) lies in \(\Lambda_x\) and has length less than \(4N\).

Sum over both signs of \(x\) (an overcount by two) and sort \(x\) into *shells* \(R\leq|x|<2R\), \(R=1,2,4,\ldots\); there are at most \(C\log(2N)\) shells. For a primitive \(x\) in a shell and a condition confining every row to a sublattice \(\Gamma\subseteq\Lambda_x\) of index \(m\), (2.2) and (2.1) bound the number of matrices by
\[
\begin{aligned}
C\,\frac{N^6}{(mJ_x)^3}&=C\,\frac{N^6g(x)^3}{m^3I^3|x|^3}\\
&\leq C\,\frac{N^6g(x)^3}{m^3I^3R^3}.
\end{aligned}\tag{3.1}
\]
By Proposition 3.1 of the fifth lesson, a matrix with \(W(A)>0\) has residues modulo \(q\) that are either affinely independent or include two equal columns. We show that each shell contributes at most \(CN^6/I^2\) in each of the following cases, which cover all of them. We use \(q^3/s\leq2000^3qH^6=2000^3qh^{12}\), from (1.2) of the fifth lesson, and \(q>h^{100}\).

*Affinely independent residues.* Here \(W(A)\leq C\), and no nonzero \(y\in\mathbb Z^3\) with \(|y|\leq H\) has \(Ay\equiv0\pmod q\) (Proposition 3.1 of the fifth lesson); since \(Ax=0\), \(|x|>H\), so only shells with \(R>H/2\geq h\) contribute. With \(m=1\) in (3.1) and Lemma 2.2, a shell contributes at most
\[
C\,\frac{N^6}{I^3R^3}\sum_{\substack{x\ \text{primitive}\\ R\leq|x|<2R}}g(x)^3\leq C\,\frac{N^6}{I^2}.
\]

*Two equal columns modulo \(q\), with an extra equation.* Fix a pair \(i<j\) of equal columns (summing over the three pairs costs a factor three), and let \(\delta=\mathbf e_i-\mathbf e_j\). Suppose \(\bar x\notin\mathbb F_q\delta\). The functional \(v\mapsto v\cdot\delta\) is not zero on \(\Pi_x\) (the vectors orthogonal to all of \(\Pi_x\) are the multiples of \(\bar x\)), and \(\Lambda_x\) reduces onto \(\Pi_x\); so \(\Gamma=\{v\in\Lambda_x:v_i\equiv v_j\pmod q\}\) has index \(q\) in \(\Lambda_x\), and every row of \(A\) lies in \(\Gamma\) because columns \(i\) and \(j\) agree modulo \(q\). A shell has at most \(CR^3\) vectors \(x\). With \(m=q\) in (3.1), \(g(x)^3\leq Ih^2\), and the general weight bound \(W(A)\leq C(q^3/s)^2\), the shell contributes at most
\[
\begin{aligned}
C\,\frac{N^6}{I^2}\,h^2q^{-3}\Bigl(\frac{q^3}s\Bigr)^2&\leq C\,\frac{N^6}{I^2}\,\frac{h^{26}}q\\
&\leq C\,\frac{N^6}{I^2},
\end{aligned}
\]
whatever the rank of \(A\bmod q\).

*Two equal columns modulo \(q\), without an extra equation.* Suppose \(\bar x=c\,\delta\) with \(c\neq0\). The coordinate of \(x\) outside \(\{i,j\}\) is then divisible by \(q\), and it is a nonzero integer; so \(|x|\geq q\), and only shells with \(R>q/2\) contribute. The residue of \(x\) is one of the \(q-1\) nonzero multiples of \(\delta\), and each residue class contains at most \((4R/q+1)^3\leq C(R/q)^3\) vectors of length less than \(2R\); so the shell has at most \(CR^3/q^2\) such \(x\).

If \(A\bmod q\) has rank at least two, then \(W(A)\leq Cq^3/s\), and with \(m=1\) and \(g(x)^3\leq Ih^2\) the shell contributes at most
\[
\begin{aligned}
C\,\frac{R^3}{q^2}\cdot\frac{N^6h^2}{I^2R^3}\cdot\frac{q^3}s&\leq C\,\frac{N^6}{I^2}\,\frac{h^{14}}q\\
&\leq C\,\frac{N^6}{I^2}.
\end{aligned}
\]
If \(A\bmod q\) has rank at most one, all rows reduce into one line \(\ell\) through \(0\) in \(\Pi_x\) (there are \(q+1\) of them; the zero row space is included). For each line, \(\{v\in\Lambda_x:v\bmod q\in\ell\}\) has index \(q\) in \(\Lambda_x\), because \(\Lambda_x\) reduces onto \(\Pi_x\). By (2.2), summed over the lines, there are at most \(C(q+1)N^6/(qJ_x)^3\leq CN^6/(q^2J_x^3)\) matrices for each \(x\), and with \(W(A)\leq C(q^3/s)^2\) the shell contributes at most
\[
\begin{aligned}
&C\,\frac{R^3}{q^2}\cdot\frac{N^6h^2}{q^2I^2R^3}\cdot\Bigl(\frac{q^3}s\Bigr)^2\\
&\quad\leq C\,\frac{N^6}{I^2}\,\frac{h^{26}}{q^2}\leq C\,\frac{N^6}{I^2}.
\end{aligned}
\]
Summing over the at most \(C\log(2N)\) shells proves the proposition. \(\square\)

## 4. Exercises

**4.1.** Give a singular integer matrix with columns in \(\mathcal B\) and pairwise distinct projections, and find its primitive null vector.

**4.2.** Why does the proof need the null vector to have all coordinates nonzero? Where exactly is that used?

**4.3.** In the case "with an extra equation", check that \(\Gamma\) has index exactly \(q\) in \(\Lambda_x\), using that \(\Lambda_x\) reduces onto \(\Pi_x\).

**4.4.** Show that the bound of Lemma 2.2 can fail for \(R<h\) by considering \(R=1\).

**4.5.** Follow the powers of \(h\) and \(q\) in the three equal-column estimates and determine how small \(q\) could be (as a power of \(h\)) for the argument to work.

## 5. Solutions

**4.1.** Take \(u^{(1)}=(0,0,N)\), \(u^{(2)}=(2,0,N)\), \(u^{(3)}=(1,0,N)\), all in \(\mathcal B\). Their projections \((0,0)\), \((2/N,0)\), \((1/N,0)\) are distinct and collinear, and \(u^{(1)}+u^{(2)}-2u^{(3)}=0\); the primitive null vector is \(x=\pm(1,1,-2)\).

**4.2.** A null vector with a zero coordinate would be a relation between two columns, which would then be proportional. It is used in the case without an extra equation: the coordinate outside \(\{i,j\}\) is a nonzero multiple of \(q\), which forces \(|x|\geq q\).

**4.3.** The map \(v\mapsto(v_i-v_j)\bmod q\) from \(\Lambda_x\) to \(\mathbb F_q\) is the composite of the reduction \(\Lambda_x\to\Pi_x\), which is onto, and the functional \(v\mapsto v\cdot\delta\), which is nonzero, hence onto, on \(\Pi_x\). Its kernel \(\Gamma\) has index \(q\).

**4.4.** Take \(C=\operatorname{diag}(1,1,0)\), so \(D=1\), \(E=h\), \(I=h\) and \(\Lambda=\mathbb Z\times\mathbb Z\times h\mathbb Z\). For \(x=\mathbf e_3\), \(x\cdot\Lambda=h\mathbb Z\) and \(g(\mathbf e_3)=h\), so the shell \(1\leq|x|<2\) already contributes \(h^3\), more than \(C\cdot1^3\cdot h\) once \(h^2>C\). The proof needs balls of radius at least \(B^j\), so that every residue class modulo \(B^j\) is represented in proportion.

**4.5.** The three estimates carry \(h^{26}/q\), \(h^{14}/q\) and \(h^{26}/q^2\); they are bounded once \(q\geq h^{26}\). The construction takes \(q>h^{100}\), with room to spare; \(q\) also enters \(N=(hq)^{10}\) and the final exponent.

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026

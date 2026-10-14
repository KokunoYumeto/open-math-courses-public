# The tower obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(Y\) be a finite complex of dimension at most two and \(\rho\) a character of its fundamental group. This lesson proves: if the second homology of \(Y\) with coefficients twisted by \(\rho\) vanishes, then \(\rho\) is \(1\) on every element of finite order. This is a property of complexes of dimension two that a complex of dimension three need not have, and it is the obstruction used in the counterexample.

The proof builds a tower. A map from a finite complex \(F\) into \(Y\) on which \(\rho\) is not trivial is lifted again and again to infinite cyclic covers. At each step the image of \(F\) becomes larger, and it cannot become larger than \(F\).

- Vanishing of the second twisted homology passes to infinite cyclic covers (Lemma 1.1).
- The tower theorem (Theorem 2.1).
- Characters and elements of finite order (Corollary 3.1).

The lesson follows [OpenAI-W, Section 2]. It uses the complexes \(C_*(Z;\rho)\), Lemmas 4.1 to 4.4 and the standard theorems TOP1 to TOP6 from [Wall's D(2) problem and twisted homology](walls-d2-problem-and-twisted-homology.md).

## 1. Infinite cyclic covers

Let \(A\) be a connected complex, \(G=\pi_1(A)\), and \(\phi:G\to\mathbb Z\) a surjective homomorphism with the kernel \(N\). The covering \(p:\widehat A=A_N\to A\) of TOP2 is an *infinite cyclic cover*: its group \(G/N\) is \(\mathbb Z\). Its fundamental group is \(N\), and a character \(\rho\) of \(G\) restricts to a character \(\rho|_N\) of \(N\).

**Lemma 1.1** ([OpenAI-W]). Let \(A\) be a finite connected complex of dimension at most two, \(\rho\) a character of \(G=\pi_1(A)\), and \(\widehat A\) an infinite cyclic cover. If \(H_2(A;\rho)=0\), then \(H_2(\widehat A;\rho|_N)=0\).

**Proof.** *A module structure.* Choose \(s\in G\) with \(\phi(s)=1\). By the formula for covers of the first lesson,
\[
C_*(\widehat A;\rho|_N)=\mathbb C_\rho\otimes_{\mathbb Z[N]}C_*(\widetilde A).
\]
Let \(R=\mathbb C[z,z^{-1}]\) be the ring of the Laurent polynomials. Let \(z\) act on this complex by
\[
z\cdot(v\otimes c)=\rho(s)^{-1}v\otimes sc .
\]
This is well defined: for \(n\in N\) the elements \(vn\otimes c\) and \(v\otimes nc\) are sent to \(\rho(s)^{-1}\rho(n)v\otimes sc\) and to \(\rho(s)^{-1}v\otimes snc\); the second is \(\rho(s)^{-1}\rho(sns^{-1})v\otimes sc\), and \(\rho(sns^{-1})=\rho(n)\). The action commutes with the boundary maps. The elements \(s^k\tilde e\), with \(k\in\mathbb Z\) and \(\tilde e\) the chosen lifts of the cells of \(A\), are a basis of \(C_*(\widetilde A)\) over \(\mathbb Z[N]\), and \(z^k\cdot(1\otimes\tilde e)=\rho(s)^{-k}\otimes s^k\tilde e\). So \(C_j(\widehat A;\rho|_N)\) is a free \(R\)-module with the basis \(1\otimes\tilde e\), one element for each cell of dimension \(j\) of \(A\).

*The boundary matrix.* Every \(g\in G\) is \(ns^k\) with \(k=\phi(g)\) and \(n\in N\), and
\[
\begin{aligned}
1\otimes g\tilde e&=\rho(n)\otimes s^k\tilde e\\
&=\rho(g)\,z^{\phi(g)}\cdot(1\otimes\tilde e).
\end{aligned}
\]
So the boundary \(C_2\to C_1\) of this complex has, in the bases \(1\otimes\tilde e\), the matrix
\[
\begin{gathered}
D(z)=\bigl(\Theta(\lambda_{e,e'})\bigr),\\
\Theta(g)=\rho(g)\,z^{\phi(g)},
\end{gathered}
\]
where the \(\lambda_{e,e'}\in\mathbb Z[G]\) are the coefficients of the boundary of \(\widetilde A\) and \(\Theta\) is extended linearly. Its entries are Laurent polynomials. For \(z=1\) it becomes the matrix \(D(1)=(\rho(\lambda_{e,e'}))\) of \(\partial:C_2(A;\rho)\to C_1(A;\rho)\).

*Rank.* Let \(m\) be the number of the cells of dimension two of \(A\). If \(m=0\) there is nothing to prove. By the hypothesis and Lemma 4.1 of the first lesson, the linear map \(D(1)\) on \(\mathbb C^m\) is injective. So some square submatrix of \(D(1)\) with \(m\) rows has a determinant \(\ne0\). The determinant \(\Delta(z)\) of the same submatrix of \(D(z)\) is a Laurent polynomial with \(\Delta(1)\ne0\), so \(\Delta\ne0\). Let \(w\in R^m\) with \(D(z)w=0\). Multiplying by the adjugate of the submatrix gives \(\Delta(z)w=0\), and \(R\) has no zero divisors; so \(w=0\). Hence \(\partial:C_2(\widehat A;\rho|_N)\to C_1(\widehat A;\rho|_N)\) is injective, and \(H_2(\widehat A;\rho|_N)=0\) by Lemma 4.1 of the first lesson. \(\blacksquare\)

The cover \(\widehat A\) is an infinite complex, and its twisted chain groups have infinite dimension over \(\mathbb C\). The lemma works because they are finitely generated over \(R\): the cover is finite modulo the translation.

## 2. The tower theorem

For a connected complex \(F\), a map \(f:F\to Y\) and a character \(\rho\) of \(\pi_1(Y)\), the character \(\rho f_*\) of \(\pi_1(F)\) is the *pullback* of \(\rho\) by \(f\).

**Theorem 2.1** ([OpenAI-W]). Assume TOP1 to TOP6. Let \(Y\) be a finite connected CW complex of dimension at most two and \(\rho\) a character of \(\pi_1(Y)\) with \(H_2(Y;\rho)=0\). Let \(F\) be a finite connected simplicial complex with \(b_1(F)=0\). Then for every map \(f:F\to Y\) the pullback of \(\rho\) by \(f\) is trivial.

**Proof.** Suppose that the pullback of \(\rho\) by a map \(f\) is not trivial.

*Simplicial models.* By TOP6 there are a finite simplicial complex \(Y'\) of dimension at most two and a homotopy equivalence \(h:Y'\to Y\), with a homotopy inverse \(h'\). Put \(\rho'=\rho h_*\). By TOP5, \(H_2(Y';\rho')\cong H_2(Y;\rho)=0\). The pullback of \(\rho'\) by \(h'f\) is \(\rho\,(hh')_*f_*\). The map \(hh'\) is homotopic to the identity, so \((hh')_*\) is a conjugation in \(\pi_1(Y)\), and a character does not change under conjugation: the pullback is \(\rho f_*\), not trivial. By TOP6, \(h'f\) is homotopic to a map that is simplicial for a subdivision of \(F\); a homotopic map induces the same pullback. A subdivision does not change \(b_1(F)\).

So we may assume: \(Y\) is a finite simplicial complex of dimension at most two, and \(f\) is simplicial. The triangulation of \(F\) is fixed from here on. For a finite simplicial complex \(A\) let \(s(A)\) be the number of its simplices.

*The objects of the tower.* We construct, for \(i=0,1,2,\dots\), a finite connected simplicial complex \(A_i\) of dimension at most two, a simplicial map \(f_i:F\to A_i\) that is onto, and a character \(\rho_i\) of \(\pi_1(A_i)\) with
\[
H_2(A_i;\rho_i)=0,\qquad\rho_i(f_i)_*\ \text{not trivial},
\]
such that \(s(A_0)<s(A_1)<s(A_2)<\cdots\). Since \(f_i\) is simplicial and onto, every simplex of \(A_i\) is the image of a simplex of \(F\), so \(s(A_i)\le s(F)\) for all \(i\). This is a contradiction, and it proves the theorem.

*The start.* Let \(A_0=f(F)\), a finite connected subcomplex of \(Y\), let \(f_0\) be \(f\) as a map to \(A_0\), and \(\rho_0=\rho\iota\) with \(\iota:\pi_1(A_0)\to\pi_1(Y)\). Then \(\rho_0(f_0)_*=\rho f_*\) is not trivial, and \(H_2(A_0;\rho_0)=0\) by Lemma 4.1 of the first lesson.

*A map to \(\mathbb Z\).* Let \(A_i,f_i,\rho_i\) be constructed. The character \(\rho_i\) is not trivial, because its pullback is not. By Exercise 6.5 of the first lesson, \(b_1(A_i)\ge1\): the twisted homology vanishes in the degrees \(0\) and \(2\), so the Euler characteristic of \(A_i\) is at most \(0\). By Lemma 4.4 there is a surjective homomorphism \(\phi_i:\pi_1(A_i)\to\mathbb Z\). Let \(N_i\) be its kernel and \(p_i:\widehat A_i\to A_i\) the infinite cyclic cover.

*The lift.* The homomorphism \(\phi_i(f_i)_*:\pi_1(F)\to\mathbb Z\) is trivial by Lemma 4.4, because \(b_1(F)=0\). So \((f_i)_*\pi_1(F)\subseteq N_i\), and by TOP2 there is a map \(\tilde f_i:F\to\widehat A_i\) with \(p_i\tilde f_i=f_i\). By TOP2, \(\widehat A_i\) is a simplicial complex and \(p_i\) maps simplices isomorphically to simplices; so \(\tilde f_i\) is simplicial for the fixed triangulation of \(F\). Put
\[
A_{i+1}=\tilde f_i(F),\qquad f_{i+1}=\tilde f_i:F\to A_{i+1},
\]
and let \(\rho_{i+1}\) be the character \(\rho_i|_{N_i}\) of \(\pi_1(\widehat A_i)=N_i\), composed with \(\pi_1(A_{i+1})\to\pi_1(\widehat A_i)\). Then \(A_{i+1}\) is a finite connected subcomplex of \(\widehat A_i\) of dimension at most two.

*The two properties.* By Lemma 1.1, \(H_2(\widehat A_i;\rho_i|_{N_i})=0\), and by Lemma 4.1 of the first lesson \(H_2(A_{i+1};\rho_{i+1})=0\). The pullback \(\rho_{i+1}(f_{i+1})_*\) is \(\rho_i(p_i)_*(\tilde f_i)_*=\rho_i(f_i)_*\), which is not trivial.

*More simplices.* The map \(p_i\) maps \(A_{i+1}\) onto \(A_i\), because \(p_i\tilde f_i=f_i\) is onto, and it maps every simplex of \(A_{i+1}\) isomorphically to a simplex of \(A_i\). Every simplex of \(A_i\) is the image of a simplex of \(F\) under \(f_i\), hence the image of a simplex of \(A_{i+1}\) under \(p_i\). So \(s(A_{i+1})\ge s(A_i)\). Suppose that equality holds. Then \(p_i\) is a bijection from the simplices of \(A_{i+1}\) to the simplices of \(A_i\), so its restriction \(A_{i+1}\to A_i\) is an isomorphism of simplicial complexes. Its inverse, followed by the inclusion into \(\widehat A_i\), is a map \(\sigma:A_i\to\widehat A_i\) with \(p_i\sigma=\mathrm{id}\). Then \((p_i)_*\sigma_*\) is the identity of \(\pi_1(A_i)\), so \((p_i)_*\) is surjective. But the image of \((p_i)_*\) is \(N_i\), which is not all of \(\pi_1(A_i)\), because \(\phi_i\) is surjective onto \(\mathbb Z\). So \(s(A_{i+1})>s(A_i)\). \(\blacksquare\)

**Where the hypotheses are used.** The dimension two enters twice through Lemma 4.1 of the first lesson: the vanishing of \(H_2\) passes to subcomplexes because there are no cells of dimension three whose boundaries could kill cycles of the larger complex only. The character must be not trivial for the Euler characteristic to give \(b_1\ge1\): this produces the next cover. The condition \(b_1(F)=0\) makes the lift possible. The values of \(\rho\) in a field are used in Lemma 1.1, for the rank of a matrix.

## 3. Elements of finite order

**Corollary 3.1** ([OpenAI-W]). Assume TOP1 to TOP6. Let \(Y\) be a finite connected CW complex of dimension at most two and \(\rho\) a character of \(\pi_1(Y)\) with \(H_2(Y;\rho)=0\). Then \(\rho(g)=1\) for every element \(g\in\pi_1(Y)\) of finite order.

**Proof.** Let \(g\) have the order \(n\ge2\). Let \(M_n\) be the presentation complex of \(\langle x\mid x^n\rangle\): a circle with one cell of dimension two attached along the loop that runs \(n\) times around the circle. A loop in \(Y\) that represents \(g\) is a map of the circle to \(Y\); the loop that runs \(n\) times along it represents \(g^n=1\) and is homotopic to a constant loop, so the map extends over the cell of dimension two. This gives a map \(f:M_n\to Y\) with \(f_*(x)=g\).

By TOP1, \(\pi_1(M_n)\) is the cyclic group of the order \(n\), generated by \(x\). Its abelianization is finite, so \(b_1(M_n)=0\): the first Betti number is the rank of the first homology group, as in the proof of Lemma 4.4 of the first lesson. The pullback of \(\rho\) by \(f\) sends \(x\) to \(\rho(g)\). By TOP6 there are a finite simplicial complex \(F\) and a homotopy equivalence \(k:F\to M_n\); then \(b_1(F)=0\), because homotopy equivalent complexes have the same homology. By Theorem 2.1 for the map \(fk\), the character \(\rho f_*k_*\) is trivial. Since \(k_*\) is an isomorphism, \(\rho(g)=\rho f_*(x)=1\). \(\blacksquare\)

For \(n=2\) the complex \(M_2\) is the real projective plane. The counterexample of the course uses this case: an element of order two on which a character has the value \(-1\).

**An example.** Let \(Y\) be the presentation complex of \(\langle x,y\mid x^2\rangle\) and \(\rho(x)=-1\), \(\rho(y)=c\). The element \(x\) has the order two, so the corollary says \(H_2(Y;\rho)\ne0\). Indeed the Fox derivatives of \(x^2\) are \(1+x\) and \(0\), and at \(\rho\) both are \(0\): the boundary \(C_2(Y;\rho)\to C_1(Y;\rho)\) is zero.

## 4. Exercises

**4.1.** Let \(A\) be the circle, \(\phi\) the identity of \(\pi_1(A)=\mathbb Z\), and \(\rho\) a character. Describe \(\widehat A\), the \(R\)-module \(C_1(\widehat A;\rho|_N)\) and the boundary \(C_1\to C_0\) as a Laurent polynomial.

**4.2.** Show by an example that Lemma 1.1 fails for finite cyclic covers: find a finite complex \(A\) of dimension two, a character \(\rho\) with \(H_2(A;\rho)=0\) and a connected double cover \(\widehat A\) with \(H_2(\widehat A;\rho|_N)\ne0\).

**4.3.** In the proof of Theorem 2.1, why can the triangulation of \(F\) stay fixed after the first step, although new covers are used again and again?

**4.4.** Let \(Y\) be a finite connected complex of dimension at most two whose fundamental group is finite and not trivial. Show without the tower that \(H_2(Y;\rho)\ne0\) for every nontrivial character \(\rho\).

**4.5.** Show that Corollary 3.1 fails for complexes of dimension three: give a finite connected complex \(X\) of dimension three, a character \(\rho\) and an element \(g\) of finite order with \(\rho(g)\ne1\) and \(H_2(X;\rho)=0\). (Use the real projective space of dimension three, with the cells of the sphere modulo the antipodal map.)

## 5. Solutions

**4.1.** \(N=1\), and \(\widehat A\) is the line, with the vertices \(s^k\tilde v\) and the edges \(s^k\tilde x\) from \(s^k\tilde v\) to \(s^{k+1}\tilde v\). \(C_1\) and \(C_0\) are free \(R\)-modules of rank one. \(\partial\tilde x=(s-1)\tilde v\), so the boundary is the Laurent polynomial \(\Theta(s)-1=\rho(s)z-1\). It is not zero, so \(H_1(\widehat A)=0\); for \(z=1\) it is \(\rho(s)-1\).

**4.2.** Let \(A\) be the real projective plane, the presentation complex of \(\langle x\mid x^2\rangle\), and \(\rho\) trivial. By Exercise 6.1 of the first lesson \(H_2(A;\rho)=0\). The double cover is the sphere, with \(H_2=\mathbb C\). In the proof, the group ring of the group with two elements has zero divisors, and the step from a nonzero determinant to injectivity fails.

**4.3.** The lift \(\tilde f_i\) of a simplicial map to a cover with the lifted triangulation is simplicial: on each simplex of \(F\) it is the lift of a map onto one simplex, and \(p_i\) is an isomorphism on each simplex of the cover. Only the target changes.

**4.4.** \(\chi(Y)=1-b_1+b_2\) and \(b_1=0\) because the group is finite (Lemma 4.4), so \(\chi(Y)\ge1\). For a nontrivial \(\rho\), \(H_0(Y;\rho)=0\), so by Lemma 4.3 of the first lesson \(\dim H_2(Y;\rho)\) is \(\chi(Y)+\dim H_1(Y;\rho)\ge1\).

**4.5.** The sphere of dimension three has a cell structure with two cells in each dimension \(0,1,2,3\), exchanged by the antipodal map \(g\) ([Hatcher, Example 2.42]). The quotient \(X\) has one cell in each dimension, \(\pi_1(X)\) has two elements, and \(C_*(\widetilde X)\) is \(\mathbb Z[G]\) in the degrees \(0\) to \(3\) with the boundaries \(g-1\), \(g+1\), \(g-1\). For \(\rho(g)=-1\) the complex \(C_*(X;\rho)\) has the boundaries \(-2,0,-2\) from the degrees \(1,2,3\). So \(H_2(X;\rho)=\mathbb C/(-2)\mathbb C=0\), although \(\rho(g)=-1\) and \(g\) has the order two. The cell of dimension three kills the cycle that a complex of dimension two cannot avoid.

## References

- [OpenAI-W] OpenAI, *A Counterexample to Wall's D(2) Problem*, OpenAI Math Release preprint, 6 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf

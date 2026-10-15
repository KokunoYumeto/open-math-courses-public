# Systems of equations over groups

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An equation over a group \(G\) is a word in unknowns and elements of \(G\), and solving it may require enlarging \(G\). For a single equation in one unknown whose exponent sum is \(\pm1\), [The Kervaire conjecture](course:the-kervaire-conjecture/equations-over-groups-and-the-kervaire-conjecture) proves that a solution always exists in an overgroup. Howie conjectured much more: a finite system of equations in several unknowns is solvable over every group as soon as its matrix of exponent sums has full row rank over \(\mathbb Q\). OpenAI proved this in October 2026 [OpenAI-NS, Theorem 1]. This course proves it. This lesson states the theorem and its consequences, recalls what was known, and lays out the proof.

- Systems and their solutions (Section 1).
- Nonsingular systems and the theorem (Section 2).
- Context (Section 3).
- The plan of the proof (Section 4).

## 1. Systems and their solutions

Let \(G\) be a group and \(F_n\) the free group on \(x_1,\ldots,x_n\). A *system of equations over \(G\)* is a finite list of elements \(w_1,\ldots,w_m\) of the free product \(G*F_n\), read as equations \(w_i=1\) in the unknowns \(x_j\) with coefficients in \(G\). For a group \(H\), a homomorphism \(\varphi:G\to H\) and elements \(h_1,\ldots,h_n\in H\), write \(w_i(h)\) for the image of \(w_i\) under the homomorphism \(G*F_n\to H\) that is \(\varphi\) on \(G\) and sends \(x_j\) to \(h_j\).

**Definition 1.1.** The system is *solvable over \(G\)* if there are a group \(H\), an injective homomorphism \(\varphi:G\to H\) and \(h_1,\ldots,h_n\in H\) with \(w_i(h)=1\) for all \(i\).

Let \(\langle\!\langle w_1,\ldots,w_m\rangle\!\rangle\) be the normal closure of the \(w_i\) in \(G*F_n\), and
\[
Q=(G*F_n)/\langle\!\langle w_1,\ldots,w_m\rangle\!\rangle ,
\]
the group obtained from \(G\) by adding the generators \(x_j\) and the relations \(w_i=1\).

**Lemma 1.2.** The system is solvable over \(G\) if and only if the *coefficient map* \(\kappa:G\to Q\), the composite of the inclusion into \(G*F_n\) and the quotient map, is injective.

*Proof.* If \(\kappa\) is injective, take \(H=Q\), \(\varphi=\kappa\), and for \(h_j\) the images of the \(x_j\); the image of each \(w_i\) in \(Q\) is \(1\). Conversely, given \(\varphi\) injective and \(h\) with \(w_i(h)=1\), the homomorphism \(G*F_n\to H\) extending \(\varphi\) and \(x_j\mapsto h_j\) kills every \(w_i\), hence their normal closure, so it factors through a homomorphism \(\bar\psi:Q\to H\) with \(\bar\psi\circ\kappa=\varphi\). Since \(\varphi\) is injective, so is \(\kappa\). \(\square\)

This is Lemma 1.2 of [Equations over groups and the Kervaire conjecture](course:the-kervaire-conjecture/equations-over-groups-and-the-kervaire-conjecture) for several equations and unknowns. A system can fail to be solvable: over \(G=\mathbb Z/2=\{1,c\}\), the two equations \(x_1=1\) and \(x_1c=1\) force \(c=1\).

## 2. Nonsingular systems and the theorem

The homomorphism \(G*F_n\to\mathbb Z^n\) that is trivial on \(G\) and sends \(x_j\) to the \(j\)-th basis vector sends \(w_i\) to the row \((a_{i1},\ldots,a_{in})\): \(a_{ij}\) is the total exponent of \(x_j\) in \(w_i\). The matrix
\[
A=(a_{ij})\in\operatorname{Mat}_{m\times n}(\mathbb Z)
\]
is the *exponent-sum matrix*. The system is *nonsingular* if \(A\) has rank \(m\) over \(\mathbb Q\), that is, its rows are linearly independent; then \(m\le n\).

**Theorem 2.1** (OpenAI [OpenAI-NS, Theorem 1]). Let \(G\) be a group and \(1\le m\le n\). If \(w_1,\ldots,w_m\in G*F_n\) have exponent-sum matrix of rank \(m\) over \(\mathbb Q\), then the coefficient map
\[
G\longrightarrow(G*F_n)/\langle\!\langle w_1,\ldots,w_m\rangle\!\rangle
\]
is injective. Equivalently, every nonsingular system over \(G\) is solvable over \(G\).

No hypothesis is made on \(G\): it may have torsion, be uncountable, or have no finite presentation. The example at the end of Section 1 has exponent-sum matrix with the two equal rows \((1)\), \((1)\), of rank one.

**Corollary 2.2** (the Kervaire–Laudenbach conjecture). If \(w\in G*\langle x\rangle\) has nonzero exponent sum in \(x\), then \(G\) embeds in \((G*\langle x\rangle)/\langle\!\langle w\rangle\!\rangle\).

*Proof.* A single row \((a)\) with \(a\ne0\) has rank one. \(\square\)

For \(a=\pm1\) this is Theorem 2.1 of [Equations over groups and the Kervaire conjecture](course:the-kervaire-conjecture/equations-over-groups-and-the-kervaire-conjecture), whose proof this course extends.

**Corollary 2.3** (infinite systems; [OpenAI-NS, Remark 5.1]). Let \(X\) be any set of unknowns and \((w_\iota)_{\iota\in I}\) any family of elements of \(G*F(X)\) whose exponent-sum rows, each with finitely many nonzero entries, are linearly independent over \(\mathbb Q\). Then \(G\) embeds in \((G*F(X))/\langle\!\langle w_\iota:\iota\in I\rangle\!\rangle\).

*Proof.* If \(g\in G\) lies in the normal closure, then \(g\) is a finite product of conjugates of finitely many \(w_\iota^{\pm1}\). These finitely many relators and the conjugating elements involve finitely many unknowns, say \(x_1,\ldots,x_n\), and \(g\) lies in the normal closure of those relators in \(G*F_n\). Their exponent-sum rows are independent, so Theorem 2.1 gives \(g=1\). \(\square\)

**Example 2.4.** Over any group, the system \(x_1ax_2b=1\), \(x_1^2cx_2^{-1}d=1\) with \(a,b,c,d\in G\) has exponent-sum matrix \(\begin{pmatrix}1&1\\2&-1\end{pmatrix}\), of determinant \(-3\). It is nonsingular, so it has a solution in an overgroup of \(G\), whatever the coefficients are. A system with a singular square exponent-sum matrix may or may not be solvable; Theorem 2.1 says nothing about it.

## 3. Context

Gerstenhaber and Rothaus proved that a square system with nonzero determinant of its exponent-sum matrix is solvable in a compact connected Lie group: the word map has nonzero degree, computed from the determinant, so it is onto; applied to a finite group embedded in a unitary group, this gives solutions in finite overgroups [Gerstenhaber–Rothaus 1962]. A nonsingular rectangular system reduces to the square case by keeping the columns of a nonzero maximal minor and setting the other unknowns equal to \(1\). The same unitary method gives Theorem 2.1 for groups that embed in metric ultraproducts of unitary groups, the hyperlinear groups [Pestov, Corollary 10.4; Nitsche–Thom, Theorem 1.2]. Howie proved solvability over locally indicable groups by the topology of relative presentations [OpenAI-NS, Section 1]; Klyachko proved the case of one equation in one unknown with exponent sum \(\pm1\) over torsion-free groups, and Chen gave a new proof of that theorem [Chen, Section 1]. Klyachko, Mikheenko and Roman'kov formulate the general statement as Howie's conjecture and solve nonsingular systems inside suitable solvable overgroups [KMR, Introduction]; Mikheenko studied systems over solvable, abelian and nilpotent groups further [Mikheenko 2023; Mikheenko 2024].

OpenAI's proof follows its proof of the Kervaire conjecture [OpenAI-K]: a relation killing a coefficient is drawn as a planar surface made of disks and bands, and unitary operators over the group von Neumann algebra of \(G\) measure its boundary words. The new ingredient is a theorem on simultaneous fixed spaces of block matrices in several unitary variables, proved with the rational cohomology of unitary groups; it replaces the degree computation for a single variable of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space), which uses only one block size and works modulo two.

## 4. The plan of the proof

Suppose \(g\in G\) is trivial in \(Q\). A product of conjugates of the relators equal to \(g\) is drawn on a disk with holes, each hole bounded by a relator or its inverse; bands pair occurrences of each unknown with opposite signs, and what remains is a planar surface whose boundary circles read words in \(G\). The key statement is that on such a connected surface, if all boundary words but one are trivial in \(G\), so is the last one.

- [Rational cohomology of unitary groups](rational-cohomology-of-unitary-groups.md): the cohomology ring of \(\mathrm U(d)\) as an exterior algebra on primitive generators compatible with block inclusions, and the topological facts used later, stated with free references.
- [Simultaneous fixed spaces](simultaneous-fixed-spaces.md): if the signed block counts of several unitary variables form a matrix of full row rank, the variables can be chosen so that given block matrices have fixed spaces of total dimension at least the sum of the block sizes.
- [The planar boundary obstruction](the-planar-boundary-obstruction.md): disks of several relator types; nonsingularity forces equal numbers of positive and negative disks of each type, the fixed-space theorem bounds the spectral phase of a boundary operator from above, and a computation circle by circle forces the exceptional boundary word to be trivial.
- [From a kernel relation to a solution](from-a-kernel-relation-to-a-solution.md): level sets of the circle coordinates of a map of a punctured disk cut out disjoint bands for all unknowns at once, and the planar components are removed from the inside out. This proves Theorem 2.1.

The spectral phase and its subadditivity come from [The regular trace and spectral phase](course:the-kervaire-conjecture/the-regular-trace-and-spectral-phase), and the weighted-cycle formula from [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem).

## 5. Exercises

**5.1** (easy). For \(a,b\in G\), consider the system \(x_1x_2a^{-1}=1\), \(x_1x_2^{-1}b^{-1}=1\). Find its exponent-sum matrix and decide whether Theorem 2.1 applies. For \(G=\mathbb Z\), written additively, find \(a,b\) for which the system has no solution in \(G\) itself, and a solution in an overgroup.

**5.2** (easy). Over \(G=\mathbb Z/6\), with generator \(c\), show that the single equation \(xc^2x^{-1}c^{-3}=1\) is not solvable (compare Example 3.1 of [Equations over groups and the Kervaire conjecture](course:the-kervaire-conjecture/equations-over-groups-and-the-kervaire-conjecture)). Why does Theorem 2.1 not apply?

**5.3** (medium). Let \(A\) have rank \(m\) over \(\mathbb Q\). Show that some \(m\) columns of \(A\) form an invertible rational matrix, and deduce that setting the other unknowns equal to \(1\) gives a square nonsingular system whose solutions are solutions of the original one.

**5.4** (medium). Show that an equation \(w=1\) in one unknown with exponent sum \(a\), \(|a|\ge2\), over a nontrivial group \(G\) always has a quotient \((G*\langle x\rangle)/\langle\!\langle w\rangle\!\rangle\) that is nontrivial, without using Theorem 2.1.

## 6. Solutions

**5.1.** The exponent-sum matrix is \(\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), of determinant \(-2\), so the system is nonsingular and Theorem 2.1 applies. For \(G=\mathbb Z\) the equations read \(x_1+x_2=a\) and \(x_1-x_2=b\), so \(2x_1=a+b\). For \(a=1\), \(b=0\) there is no solution in \(\mathbb Z\), and \(x_1=x_2=\tfrac12\) is a solution in the overgroup \(\mathbb Q\).

**5.2.** In the quotient, \(c^2\) is conjugate to \(c^3\); since \((c^2)^3=1\), also \((c^3)^3=c^3=1\), then \(c^2=1\), so \(c=c^3c^{-2}=1\). The exponent sum of \(x\) is \(0\), so the \(1\times1\) exponent-sum matrix \((0)\) has rank zero.

**5.3.** A matrix of rank \(m\) has \(m\) linearly independent columns. Setting the other unknowns equal to \(1\) is the homomorphism \(G*F_n\to G*F_m\) killing them; it maps each \(w_i\) to a word whose exponent-sum row is the restriction of the \(i\)-th row to the kept columns. A solution of the new system, with the removed unknowns set to \(1\), solves the original one.

**5.4.** The homomorphism \(G*\langle x\rangle\to\mathbb Z/|a|\), trivial on \(G\) and with \(x\mapsto1\), sends \(w\) to \(a\equiv0\), so it factors through the quotient, which therefore maps onto \(\mathbb Z/|a|\ne0\).

## References

- [OpenAI-NS] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Theorem 1 and Remark 5.1. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026
- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
- [Gerstenhaber–Rothaus 1962] M. Gerstenhaber and O. S. Rothaus, *The solution of sets of equations in groups*, Proc. Nat. Acad. Sci. U.S.A. 48 (1962), 1531–1533; free on PubMed Central. https://pmc.ncbi.nlm.nih.gov/articles/PMC220992/
- [Pestov] V. G. Pestov, *Hyperlinear and sofic groups: a brief guide*, The Bulletin of Symbolic Logic 14 (2008); arXiv:0804.3968, Corollary 10.4. https://arxiv.org/abs/0804.3968
- [Nitsche–Thom] M. Nitsche and A. Thom, *Universal solvability of group equations*, arXiv:1811.07737, Theorem 1.2. https://arxiv.org/abs/1811.07737
- [Chen] L. Chen, *The Kervaire conjecture and the minimal complexity of surfaces*, Transactions of the American Mathematical Society 379 (2026); arXiv:2302.09811, Section 1. https://arxiv.org/abs/2302.09811
- [KMR] A. A. Klyachko, M. A. Mikheenko and V. A. Roman'kov, *Equations over solvable groups*, arXiv:2303.13240, Introduction. https://arxiv.org/abs/2303.13240
- [Mikheenko 2023] M. A. Mikheenko, *On \(p\)-nonsingular systems of equations over solvable groups*, arXiv:2309.09096. https://arxiv.org/abs/2309.09096
- [Mikheenko 2024] M. A. Mikheenko, *Infinite systems of equations in abelian and nilpotent groups*, arXiv:2410.20729. https://arxiv.org/abs/2410.20729

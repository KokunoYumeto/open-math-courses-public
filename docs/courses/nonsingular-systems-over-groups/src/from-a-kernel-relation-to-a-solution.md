# From a kernel relation to a solution

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 2.1 of [Systems of equations over groups](systems-of-equations-over-groups.md): for a nonsingular system \(w_1,\ldots,w_m\in G*F_n\), no element \(g\ne1\) of \(G\) lies in the normal closure of the \(w_i\) [OpenAI-NS, Section 5]. A product of conjugates of the relators and their inverses equal to \(g\) gives a map of a disk with holes into a space whose fundamental group is \(G*F_n\). Its \(n\) circle coordinates, made piecewise affine, have level sets made of arcs that join the occurrences of each unknown in pairs, and arcs for different unknowns are disjoint. Thickening the arcs gives bands, and with the holes they form disk-and-band surfaces for the system. Their components are removed from the inside out: each time, all inner boundary words are trivial, so the planar boundary obstruction of [The planar boundary obstruction](the-planar-boundary-obstruction.md) makes the outer one trivial as well, and the map extends over the whole component. At the end the loop reading \(g\) bounds a disk in a space with fundamental group \(G\), so \(g=1\). The construction is that of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface) for several unknowns and several relators at once.

- Spaces for \(G\) and \(G*F_n\) (Section 1).
- A punctured disk for a relation (Section 2).
- Piecewise affine circle coordinates and their level arcs (Section 3).
- Bands and the surfaces they form (Section 4).
- Removing components from the inside out (Section 5).

We use Proposition 1.1 of [The planar boundary obstruction](the-planar-boundary-obstruction.md), with the notation of its Section 1 and its Lemma 1.2(2); the statement (SURF) of [Spherical arrangements and planar intervals](course:torsion-free-group-algebra-with-zero-divisors/spherical-arrangements-and-planar-intervals), Section 3, in the form used in [Disks, bands and boundary words](course:the-kervaire-conjecture/disks-bands-and-boundary-words); the statement (PI1) of [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity), Section 2, proved in [Fundamental groups of graphs and two-complexes, Corollary 2.4 and Theorem 3.3](course:cell-complexes-and-covering-spaces/fundamental-groups-of-graphs-and-two-complexes); the fact, proved before Section 1 of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface), that a map from the boundary circle of a closed disk to a space extends over the disk exactly when the loop is null-homotopic; and the following standard statement, which is not proved in the programme and is recorded as an open obligation of this course.

**(REL)** (relations as maps of punctured disks; [Chen, Example 2.5 and Figure 3], [Hatcher, Section 1.1 and Proposition 1.26]). Let \(X\) be a path-connected space with a basepoint \(x_0\), let \(\gamma,\omega_1,\ldots,\omega_r\) be loops at \(x_0\), and suppose that \([\gamma]=\prod_{\alpha=1}^r b_\alpha[\omega_\alpha]^{\epsilon_\alpha}b_\alpha^{-1}\) in \(\pi_1(X,x_0)\), with \(r\ge1\), \(b_\alpha\in\pi_1(X,x_0)\) and \(\epsilon_\alpha=\pm1\). Let \(\Delta\) be a closed polygonal disk in the plane, \(H_1,\ldots,H_r\) pairwise disjoint closed polygonal disks in its interior, and \(P=\Delta\setminus(\operatorname{int}H_1\cup\cdots\cup\operatorname{int}H_r)\). Then there is a continuous map \(f:P\to X\) whose restriction to \(\partial\Delta\), read from a point of \(\partial\Delta\) in the boundary orientation of \(\Delta\), is \(\gamma\), and whose restriction to each \(\partial H_\alpha\), read from a point of \(\partial H_\alpha\) in the boundary orientation of \(H_\alpha\), is \(\omega_\alpha^{\epsilon_\alpha}\).

This is the statement (REL) of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface) with loops \(\omega_\alpha\) that may differ from hole to hole; the standard proof sketched there does not use that the loops are equal.

## 1. Spaces for \(G\) and \(G*F_n\)

Let \(G\) be a group, possibly uncountable. Let \(Y\) be the CW complex with one vertex \(y_0\), one loop \(x_a\) for each \(a\in G\), and a closed disk attached along \(x_1\) and along \(x_ax_bx_{ab}^{-1}\) for all \(a,b\in G\). Let \(\mathbb T_1,\ldots,\mathbb T_n\) be copies of the circle \(\mathbb R/\mathbb Z\), with basepoint \(0\), and let \(X=Y\vee\mathbb T_1\vee\cdots\vee\mathbb T_n\), all basepoints identified with \(y_0\).

**Lemma 1.1.** \(a\mapsto[x_a]\) is an isomorphism \(G\to\pi_1(Y,y_0)\), and together with the loops \(x_j\) that run once around \(\mathbb T_j\) it gives an isomorphism \(G*F_n\to\pi_1(X,y_0)\).

*Proof.* The first statement is Lemma 1.1 of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface), with \(G\) in place of \(A\). For the second, the \(1\)-skeleton of \(X\) is the wedge of the loops \(x_a\) and the \(n\) circles; by (PI1) 1 its fundamental group is free on these loops, and by (PI1) 2, \(\pi_1(X,y_0)\) is its quotient by the normal subgroup generated by the boundaries of the disks, which are the relations of \(G\). As in that lemma, this is a presentation of \(G*F_n\). \(\square\)

The collapse maps \(c_j:X\to\mathbb T_j\), sending \(Y\) and the other circles to \(0\), and \(c_Y:X\to Y\), sending all circles to \(y_0\), are continuous; \(c_Y\) induces the homomorphism \(G*F_n\to G\) that kills the unknowns.

## 2. A punctured disk for a relation

Let the system have exponent-sum matrix of rank \(m\) over \(\mathbb Q\), and write the relators in the form (1.1) of [The planar boundary obstruction](the-planar-boundary-obstruction.md),
\[
w_i=x_{\nu_{i,1}}^{s_{i,1}}g_{i,1}\cdots x_{\nu_{i,N_i}}^{s_{i,N_i}}g_{i,N_i},
\]
since conjugate relators have the same normal closure. Represent \(w_i\) by the loop \(\omega_i\) in \(X\) that runs, in order, once around \(\mathbb T_{\nu_{i,1}}\) in the direction \(s_{i,1}\), with constant speed, then along \(x_{g_{i,1}}\), then once around \(\mathbb T_{\nu_{i,2}}\) in the direction \(s_{i,2}\), and so on; a coefficient \(g_{i,t}=1\) still gets its own interval, along the loop \(x_1\). Call the parameter intervals of the first kind the *variable intervals*, of index \(\nu_{i,t}\), and the others the *coefficient intervals*.

Suppose that \(g\in G\) lies in the normal closure of the \(w_i\):
\[
g=\prod_{\alpha=1}^rb_\alpha w_{i_\alpha}^{\epsilon_\alpha}b_\alpha^{-1}\quad\text{in }G*F_n,
\]
with \(b_\alpha\in G*F_n\) and \(\epsilon_\alpha=\pm1\). If \(r=0\), then \(g=1\). Otherwise apply (REL) with \(\gamma=x_g\) and, for the \(\alpha\)-th hole, the loop \(\omega_{i_\alpha}\) and the sign \(\epsilon_\alpha\): we obtain \(f:P\to X\) on a disk \(\Delta\) with holes \(H_1,\ldots,H_r\). Put
\[
\begin{gathered}
u_j=c_j\circ f:P\to\mathbb T_j\quad(1\le j\le n),\\
v=c_Y\circ f:P\to Y .
\end{gathered}
\]
On \(\partial\Delta\), every \(u_j\) is \(0\) and \(v\) reads \(x_g\). On \(\partial H_\alpha\), read in the orientation of \(H_\alpha\), the map \(f\) runs through the variable intervals and the coefficient intervals of \(w_{i_\alpha}^{\epsilon_\alpha}\). On a variable interval of index \(j\), \(u_j\) runs once around the circle, monotonically, forward for a letter \(x_j\) and backward for a letter \(x_j^{-1}\) of \(w_{i_\alpha}^{\epsilon_\alpha}\), while the other \(u_{j'}\) are \(0\) and \(v\) is constant; on the coefficient interval of a letter \(a\), all \(u_j\) are \(0\) and \(v\) runs along \(x_a\). We call \(H_\alpha\) a disk of *type* \(i_\alpha\), *positive* if \(\epsilon_\alpha=1\) and *negative* if \(\epsilon_\alpha=-1\).

## 3. Piecewise affine circle coordinates and their level arcs

We identify points of \(\mathbb T_j\) with angles in \(\mathbb R/\mathbb Z\) and use the circle distance \(|\cdot|_{\mathbb T}\).

**Lemma 3.1** (approximation). There are continuous maps \(u_j':P\to\mathbb T_j\) with \(|u_j'-u_j|_{\mathbb T}<\frac1{12}\) everywhere, \(1\le j\le n\), and one finite triangulation of \(P\) by straight triangles on each of which every \(u_j'\) lifts to an affine function to \(\mathbb R\) with values in an interval of length less than \(\frac1{24}\), such that on \(\partial P\): \(u_j'=0\) on \(\partial\Delta\), on the coefficient intervals and on the variable intervals of indices other than \(j\), and on each variable interval of index \(j\), \(u_j'\) runs once around the circle, monotonically in the same direction as \(u_j\).

*Proof.* This is Lemma 3.1 of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface), applied to the finitely many maps \(u_j\) with one triangulation. By uniform continuity, there is \(\rho>0\) such that every \(u_j\) maps every subset of \(P\) of diameter less than \(\rho\) into an arc of length less than \(\frac1{24}\). Choose a triangulation of \(P\) by straight triangles of diameter less than \(\rho\) whose vertices include the endpoints of all variable and coefficient intervals, and define each \(u_j'\) on each triangle by lifting the vertex values of \(u_j\) into a lift of that arc and interpolating affinely. The proof there applies to each \(j\) without change; on a boundary edge where \(u_j\) is \(0\) at both ends, \(u_j'\) is \(0\). \(\square\)

For each \(j\) choose an angle \(\zeta_j\in(\frac13,\frac23)\) that is not the value of \(u_j'\) at any vertex of the triangulation, and put \(\Lambda_j=u_j'^{-1}(\zeta_j)\).

**Lemma 3.2** (level arcs).

1. \(\Lambda_j\) is a finite disjoint union of polygonal circles and polygonal arcs, the arcs meeting \(\partial P\) exactly in their endpoints. Every variable interval of index \(j\) on every \(\partial H_\alpha\) contains exactly one endpoint of an arc of \(\Lambda_j\), and there are no other endpoints.
2. The set \(U_j=u_j^{-1}((\frac14,\frac34))\) is an open neighbourhood of \(\Lambda_j\) on which \(f\) takes values in \(\mathbb T_j\setminus\{0\}\). In particular \(v\) is constant, equal to \(y_0\), on \(U_j\), and \(U_j\cap U_{j'}=\varnothing\) for \(j\ne j'\); so \(\Lambda_j\cap\Lambda_{j'}=\varnothing\).
3. Read in the orientations of the disks \(H_\alpha\), the two endpoints of each arc of \(\Lambda_j\) lie on variable intervals of opposite letters \(x_j\) and \(x_j^{-1}\).

*Proof.* (1) and (3) are Lemma 3.2(1) and (3) of [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface) for the map \(u_j'\), whose proofs use only the properties of Lemma 3.1 above: on each triangle \(u_j'\) has an affine lift with values in an interval of length less than \(\frac1{24}\), and on \(\partial P\), \(u_j'\) takes the value \(\zeta_j\) exactly once on each variable interval of index \(j\), monotonically in the direction of \(u_j\), and nowhere else.

(2) On \(\Lambda_j\), \(u_j'=\zeta_j\in(\frac13,\frac23)\) and \(|u_j-u_j'|_{\mathbb T}<\frac1{12}\), so \(u_j\in(\frac14,\frac34)\). A point that \(f\) maps into \(Y\) or into another circle \(\mathbb T_{j'}\) has \(u_j=0\). So \(f(U_j)\subseteq\mathbb T_j\setminus\{0\}\), where \(c_Y\) is constant \(y_0\) and every \(c_{j'}\), \(j'\ne j\), is constant \(0\). Hence \(u_{j'}=0\) on \(U_j\), and \(U_j\) misses \(U_{j'}\), on which \(u_{j'}\ne0\). \(\square\)

Part 2 uses the map \(f\) into the wedge, not the approximations: the maps \(u_j'\) are constructed separately and need not come from one map into \(X\) (Exercise 6.2).

## 4. Bands and the surfaces they form

Ignore the circles of the sets \(\Lambda_j\). The arcs of all the \(\Lambda_j\) are pairwise disjoint polygonal arcs in the plane, with interiors outside the disks \(H_\alpha\) and endpoints on their boundaries: arcs of one \(\Lambda_j\) are disjoint by Lemma 3.2(1), and arcs of different \(\Lambda_j\) by Lemma 3.2(2). By (SURF), applied in the sphere obtained by adding a point at infinity to the plane, they have pairwise disjoint thin bands. A polygonal arc has rectangular neighbourhoods inside any given neighbourhood, so we take the bands of the arcs of \(\Lambda_j\) inside \(U_j\). They meet the circles \(\partial H_\alpha\) in short intervals, the *slots*, inside the variable intervals of index \(j\).

With these slots, each \(H_\alpha\) is a word disk of type \(i_\alpha\) in the sense of [The planar boundary obstruction](the-planar-boundary-obstruction.md), Section 1, positive or negative according to \(\epsilon_\alpha\). Its slots are the attachment intervals, indexed by the positions \(t\) of the letters of \(w_{i_\alpha}\), with variable index \(\nu_{i_\alpha,t}\). Between two consecutive slots, the boundary of \(H_\alpha\) consists of one coefficient interval together with pieces of the two adjacent variable intervals, on which \(v\) is constant. So the class of the corner under \(v\) is \(g_{i,t}\) after slot \(t\) of a positive disk of type \(i\), and \(g_{i,t-1}^{-1}\) after slot \(t\) of a negative disk, as in (1.2) of that lesson, since a negative disk reads \(w_i^{-1}\). The traversal sign of a slot is the exponent of its letter in the reading of \(H_\alpha\). Every band of an arc of \(\Lambda_j\) joins two slots of variable index \(j\), and by Lemma 3.2(3) they have opposite traversal signs.

Let \(\mathcal S\) be the union of the disks \(H_\alpha\) and the bands. Each component of \(\mathcal S\) contains a disk, every slot carries exactly one band end, and each component is a connected disk-and-band surface for the system, oriented by the plane. Along a boundary circle of \(\mathcal S\), the map \(v\) runs along the corners and is constant on the band sides, which lie in the sets \(U_j\). So the loop \(v\) along a boundary circle, read in its boundary orientation, represents in \(\pi_1(Y,y_0)=G\) the boundary word of that circle, up to conjugation.

## 5. Removing components from the inside out

*Proof of Theorem 2.1 of [Systems of equations over groups](systems-of-equations-over-groups.md).* We prove by induction on the number of components the following statement. Let \(\mathcal S\subseteq\operatorname{int}\Delta\) be a finite union of pairwise disjoint connected disk-and-band surfaces for the system in the plane, and let \(v:\Delta\setminus\operatorname{int}\mathcal S'\to Y\) be continuous, where \(\mathcal S'\) is the union of the word disks of \(\mathcal S\), such that \(v\) reads the corner labels along the corners and is constant on the bands. Then the loop \(v|_{\partial\Delta}\) is null-homotopic.

If there are no components, \(v\) is defined on all of \(\Delta\), and the loop \(v|_{\partial\Delta}\) extends over the disk \(\Delta\), so it is null-homotopic.

Otherwise, for each component \(C\), Lemma 1.2(2) of [The planar boundary obstruction](the-planar-boundary-obstruction.md), applied in the sphere, shows that \(C\) is the complement of the interiors of disjoint closed disks bounded by its boundary circles; exactly one of these disks contains the point at infinity, and its boundary is the *exterior* circle of \(C\). Let \(D(C)\) be the closed disk in the plane bounded by the exterior circle; then \(C\subseteq D(C)\), and the other boundary circles of \(C\) bound the *inner disks* of \(C\), contained in \(D(C)\). Choose a component \(C\) whose disk \(D(C)\) is minimal under inclusion. No inner disk \(D_1\) of \(C\) contains another component \(C'\): otherwise the unbounded complementary region of \(C'\) would contain the connected set \(\mathbb R^2\setminus D_1\), so \(D(C')\subseteq D_1\subsetneq D(C)\), against minimality.

So each inner disk of \(C\) contains no word disk, and \(v\) is defined on all of it. Its boundary loop extends over the inner disk, so it is null-homotopic, and the boundary word of that circle is trivial in \(G\) by the last paragraph of Section 4. By Proposition 1.1 of the planar lesson, applied to the connected surface \(C\), the boundary word of the exterior circle is trivial as well, so the loop \(v|_{\partial D(C)}\) is null-homotopic, and it extends to a map \(D(C)\to Y\). Replace \(v\) on \(D(C)\) by such an extension, and remove the word disks and bands of \(C\). Nothing changes outside \(D(C)\), and no other component meets \(D(C)\): a component inside \(D(C)\) would lie in an inner disk of \(C\). The hypotheses hold for the remaining components, and the loop \(v|_{\partial\Delta}\) is unchanged; by induction it is null-homotopic.

Apply this to the surface \(\mathcal S\) of Section 4 and the map \(v=c_Y\circ f\). The loop \(v|_{\partial\Delta}\) is \(x_g\), whose class is \(g\) by Lemma 1.1. So \(g=1\) in \(G\). Hence the coefficient map \(G\to(G*F_n)/\langle\!\langle w_1,\ldots,w_m\rangle\!\rangle\) has trivial kernel, and by Lemma 1.2 of the first lesson the system is solvable over \(G\). \(\square\)

With Corollary 2.2 of the first lesson this proves the Kervaire–Laudenbach conjecture for every group: an equation in one unknown with nonzero exponent sum is solvable over every group.

**What the course proves and what it assumes.** The lessons prove every step of the argument, with these inputs from outside the programme, each stated where it is used and recorded as an open obligation: the statements (UC), (KU) and (INT) on the cohomology of unitary groups, products and intersection numbers ([Rational cohomology of unitary groups](rational-cohomology-of-unitary-groups.md)); the statement (REL) on relations and punctured disks (this lesson); and the statement (SURF) on surfaces in the sphere, stated in the course on the torsion-free group algebra with zero divisors. The statement (PI1) on fundamental groups of \(2\)-complexes is proved in the course on cell complexes, fundamental groups and covering spaces. The spectral phase, its subadditivity and the Borel functional calculus come from the course on the Kervaire conjecture and the courses it builds on.

## 6. Exercises

**6.1** (easy). Explain why the levels \(\zeta_j\) are taken in \((\frac13,\frac23)\) and away from the vertex values of \(u_j'\). What could go wrong with \(\zeta_j\) close to \(0\)?

**6.2** (medium). Let \(n=2\). Show by an example that two continuous maps \(u_1',u_2':P\to\mathbb R/\mathbb Z\) with \(|u_j'-u_j|_{\mathbb T}<\frac1{12}\) can both be different from \(0\) at a point where \(f\) is the basepoint, and explain why the level sets \(\Lambda_1\) and \(\Lambda_2\) are nevertheless disjoint.

**6.3** (medium). Let \(c\in G\), \(c\ne1\), and consider the singular system \(w_1=x_1\), \(w_2=x_1c^{-1}\) of Exercise 6.3 of [The planar boundary obstruction](the-planar-boundary-obstruction.md). Write \(c\) as a product of conjugates of \(w_1^{\pm1}\) and \(w_2^{\pm1}\), and describe the surface that the construction of this lesson produces. Where does the proof of Section 5 stop?

**6.4** (medium). Let \(D\) and \(D'\) be closed disks in the plane whose boundary circles \(E\) and \(E'\) are disjoint. Show that \(D\) and \(D'\) are disjoint or one contains the other. Use that the complement of a closed disk in the plane is connected and that the interior of \(D\) is the bounded component of \(\mathbb R^2\setminus E\). Deduce that the disks \(D(C)\) of the components in Section 5 are pairwise disjoint or nested.

## 7. Solutions

**6.1.** On \(\Lambda_j\), the original coordinate \(u_j\) lies within \(\frac1{12}\) of \(\zeta_j\), hence in \((\frac14,\frac34)\), so \(f\) lies in the open arc \(\mathbb T_j\setminus\{0\}\) near \(\Lambda_j\). This makes \(v\) constant on the bands and separates the level sets of different unknowns (Lemma 3.2(2)). A level close to \(0\) could meet points where \(f\) lies in \(Y\) or in another circle, and the bands would carry coefficient labels. Avoiding the vertex values makes \(\Lambda_j\) meet each triangle in a segment between interior points of two edges, so that the level set is a union of disjoint polygonal arcs and circles, with no branching at vertices.

**6.2.** At a point \(p\) with \(f(p)=y_0\), all \(u_j(p)=0\), and the approximations may take any values within \(\frac1{12}\) of \(0\), for instance \(u_1'(p)=u_2'(p)=\frac1{20}\); no single map into the wedge has two nonzero circle coordinates at one point. The level sets are disjoint because a point of \(\Lambda_j\) has \(u_j\in(\frac14,\frac34)\), so \(f\) maps it into \(\mathbb T_j\setminus\{0\}\) and \(u_{j'}=0\) there for \(j'\ne j\); then \(|u_{j'}'|_{\mathbb T}<\frac1{12}\), so \(u_{j'}'\ne\zeta_{j'}\).

**6.3.** In \(G*\langle x_1\rangle\), \(w_2^{-1}w_1=(x_1c^{-1})^{-1}x_1=cx_1^{-1}x_1=c\), so \(c=w_2^{-1}w_1\), with trivial conjugators. The punctured disk has a negative hole of type \(2\) and a positive hole of type \(1\), each with one variable interval of index \(1\). By Lemma 3.2(1), \(\Lambda_1\) has exactly two arc endpoints, one on each hole, so one arc joins the two holes. The surface is that of Exercise 6.3 of the planar lesson: one component with one boundary circle, its exterior circle, whose word is \(c\) (up to conjugation). The component has no inner disks, so the hypothesis of Proposition 1.1 holds vacuously, but the proposition does not apply, because the exponent-sum matrix \(\begin{pmatrix}1\\1\end{pmatrix}\) has rank \(1<2\). The proof stops there, as it must: \(c=1\) in the quotient.

**6.4.** The circle \(E'\) is connected and misses \(E\), so it lies in \(\operatorname{int}D\) or in \(\mathbb R^2\setminus D\). If \(E'\subseteq\operatorname{int}D\), the connected unbounded set \(\mathbb R^2\setminus D\) misses \(E'\), so it lies in the unbounded component of \(\mathbb R^2\setminus E'\), which is \(\mathbb R^2\setminus D'\); hence \(D'\subseteq D\). In the same way \(E\subseteq\operatorname{int}D'\) gives \(D\subseteq D'\). In the remaining case \(E'\cap D=\varnothing\) and \(E\cap D'=\varnothing\). If a point \(p\) lay in \(D\cap D'\), then \(p\notin E\), so \(p\in\operatorname{int}D\); the connected set \(D'\) misses \(E\) and meets \(\operatorname{int}D\), so \(D'\subseteq\operatorname{int}D\), and then \(E'\subseteq D\), a contradiction. So \(D\cap D'=\varnothing\). For distinct components \(C\), \(C'\), the exterior circles are disjoint, since the components are, and the statement applies to \(D(C)\) and \(D(C')\).

## References

- [OpenAI-NS] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026
- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
- [Chen] L. Chen, *The Kervaire conjecture and the minimal complexity of surfaces*, Transactions of the American Mathematical Society 379 (2026); arXiv:2302.09811, Example 2.5 and Figure 3. https://arxiv.org/abs/2302.09811
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page, Section 1.1 and Proposition 1.26. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf

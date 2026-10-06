# Cohomology of cyclic groups and the Herbrand quotient

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

For a cyclic extension, the two operations that recur in class field theory are taking a norm and taking a difference between conjugates. Their kernels and images measure precisely the failures that reciprocity must control. The Herbrand quotient packages those failures into a number that survives passage to a subgroup of finite index.

We assume abelian groups, modules, exact sequences and the elementary properties of finite cyclic groups. The topology in [Profinite groups and infinite Galois theory](profinite-groups-and-infinite-galois-theory.md) explains the Galois groups to which these calculations will apply, but this lesson concerns finite groups. Freely accessible comparisons are Milne's *Class Field Theory* and the free electronic Bonn lectures, credited below.

## 1. Two operators, two obstructions

Let a finite group \(G\) act on an abelian group \(A\), written additively. Put

\[
N_G=\sum_{g\in G}g,
\qquad I_GA=\langle ga-a:g\in G,\ a\in A\rangle.
\]

Here \(N_G\) is an endomorphism of \(A\). Its image lies in \(A^G\), and it vanishes on \(I_GA\). The two Tate groups needed in this course are

\[
\widehat H^0(G,A)=A^G/N_GA,
\qquad
\widehat H^{-1}(G,A)=\ker N_G/I_GA.
\]

The first asks whether every invariant is a norm. The second asks whether every norm-zero element is a sum of conjugate differences. For a multiplicative module, replace sums by products, zero by 1 and \(ga-a\) by \(g(a)/a\).

Now let \(G=\langle\sigma\rangle\) have order \(n\), and write

\[
D=\sigma-1,
\qquad N=1+\sigma+\cdots+\sigma^{n-1}.
\]

We have \(DN=ND=0\), \(A^G=\ker D\) and \(I_GA=DA\). The last equality follows from

\[
\sigma^j-1=(\sigma-1)(1+\sigma+\cdots+\sigma^{j-1}).
\]

Thus the two groups are the two alternating homology groups of the periodic sequence

\[
\cdots\xrightarrow{N}A\xrightarrow{D}A\xrightarrow{N}A\xrightarrow{D}A\xrightarrow{N}\cdots.
\]

A **crossed homomorphism**, or 1-cocycle, is a function \(c:G\to A\) satisfying \(c(gh)=c(g)+g c(h)\). A coboundary has the form \(c(g)=ga-a\) for some \(a\in A\). Their quotient is \(H^1(G,A)\). A cocycle for the cyclic group is determined by \(b=c(\sigma)\), since

\[
c(\sigma^j)=\sum_{i=0}^{j-1}\sigma^i b.
\]

The relation \(\sigma^n=1\) is exactly \(Nb=0\), and this condition also suffices to define a cocycle. Coboundaries correspond to \(b\in DA\). Consequently

\[
H^1(G,A)\simeq\widehat H^{-1}(G,A).
\]

This identification uses the selected generator \(\sigma\). Changing that generator changes the map evaluating a cocycle.

The alternating operators also come from an exact sequence of free modules, rather than merely from the relation \(DN=0\). Let \(R=\mathbf Z[G]\), with augmentation \(\varepsilon(\sum a_j\sigma^j)=\sum a_j\). Then
\[
\cdots\xrightarrow{D}R\xrightarrow{N}R
\xrightarrow{D}R\xrightarrow{\varepsilon}\mathbf Z\longrightarrow0
\]
is exact, where the rightmost \(R\) has degree zero. Here is a coefficient proof. For \(x=\sum_{j=0}^{n-1}a_j\sigma^j\), the coefficient of \(\sigma^j\) in \(Dx\) is \(a_{j-1}-a_j\), with indices modulo \(n\). Thus \(Dx=0\) exactly when all coefficients agree, or \(x=cN\); this is precisely the image of multiplication by \(N\). On the other hand \(Nx=(\sum_j a_j)N\), so \(\ker N=\ker\varepsilon\). If \(\sum_j a_j=0\), choose \(b_0=0\) and successively solve \(b_{j-1}-b_j=a_j\) for \(1\leq j<n\). The missing equation at \(j=0\) follows from the zero sum. Hence \(x=D\sum_j b_j\sigma^j\). This proves \(\ker N=DR=\ker\varepsilon\) at every required position.

Applying \(\operatorname{Hom}_R(-,A)\) identifies each term with \(A\) by evaluation at 1 and gives the alternating cochain operators \(D,N\). In particular its first two positive-degree cohomology groups are \(\ker N/DA\) and \(\ker D/NA\). This is the explicit cyclic free resolution used for the later cyclic factor-system computation; its exactness has been proved here. The norm and difference descriptions of the two Tate degrees require no appeal to an external resolution theorem.

## 2. How an exact sequence passes around the cycle

### Proposition 2.1. The exact hexagon

A short exact sequence of \(G\)-modules

\[
0\longrightarrow A\xrightarrow{i}B\xrightarrow{p}C\longrightarrow0
\]

for cyclic \(G\) gives the following exact cycle. In the diagram, write \(\widehat H^i(A)\) for \(\widehat H^i(G,A)\), and likewise for \(B,C\).

\[
\begin{array}{ccccc}
\widehat H^0(A)&\longrightarrow&\widehat H^0(B)&\longrightarrow&\widehat H^0(C)\\
{\scriptstyle\delta_{-1}}\uparrow&&&&\downarrow{\scriptstyle\delta_0}\\
\widehat H^{-1}(C)&\longleftarrow&\widehat H^{-1}(B)&\longleftarrow&\widehat H^{-1}(A)
\end{array}
\]

Traversing the diagram clockwise gives the repeated exact sequence. The upward connecting arrow closes it; no zero terms are asserted.

**Proof.** Identify \(A\) with its image in \(B\). If \(c\in C^G\), lift it to \(b\in B\). Then \(Db\in A\) and \(NDb=0\). Define

\[
\delta_0(c\bmod NC)=Db\bmod DA.
\]

Changing \(b\) by an element of \(A\) adds an element of \(DA\). Changing \(c\) by \(Nc'\), and its lift by \(Nb'\), leaves \(Db\) unchanged. Thus this map is well defined.

If \(Nc=0\), lift \(c\) to \(b\in B\). Then \(Nb\in A^G\), and set

\[
\delta_{-1}(c\bmod DC)=Nb\bmod NA.
\]

Changing the lift adds a norm from \(A\); changing \(c\) by \(Dc'\) changes the lift by \(Db'\), whose norm is zero. This map is also well defined. The four remaining arrows are induced by \(i\) and \(p\).

Here are the six exactness checks, so that the closing arrow is included. An invariant \(a\in A\) becomes a norm in \(B\) precisely when \(a=Nb\); then \(p(b)\) has norm zero and maps to its class under \(\delta_{-1}\). An invariant \(b\in B\) whose class maps to zero in \(\widehat H^0(G,C)\) has \(p(b)=Nc'\). Subtracting \(Nb'\), for a lift \(b'\) of \(c'\), leaves an invariant in \(A\). An invariant \(c\in C\) has \(\delta_0(c)=0\) precisely when a lift \(b\) has \(Db=Da\) for some \(a\in A\); then \(b-a\) is an invariant lift.

Next, a norm-zero \(a\in A\) becomes a difference in \(B\) precisely when \(a=Db\). In that case \(p(b)\) is invariant and maps to its class under \(\delta_0\). A norm-zero \(b\in B\) whose image is \(Dc'\) can be adjusted by \(Db'\) to a norm-zero element of \(A\). Finally, a norm-zero \(c\in C\) has \(\delta_{-1}(c)=0\) precisely when a lift satisfies \(Nb=Na\), with \(a\in A\); then \(b-a\) is a norm-zero lift. Each image is visibly in the next kernel. These checks establish equality at every position. \(\square\)

The connecting arrows express a useful principle. An invariant downstairs may fail to have an invariant lift upstairs; its obstruction is a norm-zero class in the kernel module. A norm-zero element downstairs has the complementary obstruction, an invariant norm class in that module.

## 3. Counting the obstructions

When both Tate groups are finite, define the **Herbrand quotient**

\[
h_G(A)=\frac{|\widehat H^0(G,A)|}{|\widehat H^{-1}(G,A)|}.
\]

A trivial group has order 1 in this formula. The quotient is a positive rational number; it need not be an integer.

### Proposition 2.2. Multiplicativity

For the short exact sequence of Proposition 2.1, if the Herbrand quotients are defined for any two of \(A,B,C\), they are defined for the third, and

\[
h_G(B)=h_G(A)h_G(C).
\]

**Proof.** In the hexagon, a group whose two adjacent groups are finite is an extension of a finite image by a finite image. When the Tate groups of any two modules are finite, this applies to both groups of the remaining module. Now name the six consecutive images \(J_1,\ldots,J_6\), beginning with the arrow out of \(\widehat H^0(G,A)\). Exactness gives

\[
\begin{array}{lll}
|\widehat H^0(G,A)|=|J_6||J_1|,&
|\widehat H^0(G,B)|=|J_1||J_2|,&
|\widehat H^0(G,C)|=|J_2||J_3|,\\
|\widehat H^{-1}(G,A)|=|J_3||J_4|,&
|\widehat H^{-1}(G,B)|=|J_4||J_5|,&
|\widehat H^{-1}(G,C)|=|J_5||J_6|.
\end{array}
\]

Substitution and cancellation prove the formula. \(\square\)

### Proposition 2.3. Finite modules and induced modules

For cyclic \(G\) of order \(n\):

1. A finite \(G\)-module \(A\) has \(h_G(A)=1\).
2. With trivial action, \(h_G(\mathbf Z)=n\).
3. For \(H\subset G\) and an \(H\)-module \(B\), induction gives
   \(\widehat H^i(G,\operatorname{Ind}_H^G B)\simeq\widehat H^i(H,B)\) for \(i=0,-1\). Hence \(h_G(\operatorname{Ind}_H^G B)=h_H(B)\) whenever these quotients are defined.
4. In particular, \(h_G(\mathbf Z[G/H])=|H|\).

**Proof.** For finite \(A\), the two identities

\[
|A|=|\ker D|\,|DA|=|\ker N|\,|NA|
\]

give the first assertion. For \(\mathbf Z\), \(D=0\) and \(N=n\); the two Tate groups are \(\mathbf Z/n\mathbf Z\) and zero. This proves the second.

For induction, put \(r=[G:H]\), so \(H=\langle\tau\rangle\) with \(\tau=\sigma^r\), and write

\[
P=\operatorname{Ind}_H^G B=
\bigoplus_{j=0}^{r-1}\sigma^j B.
\]

The action of \(\sigma\) shifts each summand to the next and takes \(\sigma^{r-1}b\) to \(\tau b\) in the first summand. An invariant is therefore a constant tuple \((b,\ldots,b)\), with \(b\in B^H\). The norm of an element supported in the first summand is the constant tuple with value \(N_Hb\). These elements generate \(P\), so \(P^G/N_GP\simeq B^H/N_HB\).

For degree \(-1\), pass first to coinvariants. The relations \(\sigma x-x\) identify all summands and impose exactly the relation \(\tau b-b\) on the first. Thus

\[
P_G=P/(\sigma-1)P\simeq B/(\tau-1)B=B_H.
\]

Under this identification and the invariant identification just proved, the norm map \(P_G\to P^G\) becomes \(N_H:B_H\to B^H\). Its kernel is \(\widehat H^{-1}\), proving the second induction isomorphism. Taking \(B=\mathbf Z\) proves the last assertion. \(\square\)

In particular, \(\mathbf Z[G]\) has both Tate groups zero. Its invariants are the multiples of \(\sum_g g\), all of which are norms. Its norm-zero elements are precisely the vectors whose coefficients sum to zero, and these are conjugate differences.

If a submodule \(A\subset B\) has finite index, Proposition 2.2 and the finite-module calculation show that \(h_G(A)=h_G(B)\), whenever one is defined. Finite torsion likewise has no effect on the quotient.

## 4. A calculation from an orbit decomposition

Let \(G\) be cyclic of order 6, and let \(P\) be the permutation lattice on the disjoint union of an orbit of size 2 and an orbit of size 3. The stabilizers have orders 3 and 2, respectively. Therefore

\[
h_G(P)=3\cdot2=6.
\]

Let \(P_0\) be the kernel of the sum of all five coordinates. The augmentation is surjective and gives

\[
0\longrightarrow P_0\longrightarrow P\longrightarrow\mathbf Z\longrightarrow0.
\]

Consequently \(h_G(P_0)=6/6=1\). If instead \(P=\mathbf Z[G]\), its augmentation kernel has Herbrand quotient \(1/6\). This example shows why the dimension of a lattice alone cannot determine the quotient: the representation carried by it matters.

## 5. Changing a lattice without changing its quotient

A **\(G\)-lattice** is a finitely generated free abelian group with a \(G\)-action. Its Tate groups are finite. To see this, they are finitely generated quotients of subgroups of a lattice and are killed by \(n=|G|\). For degree 0, \(Na=na\) for invariant \(a\). For degree \(-1\), if \(Na=0\), then

\[
na=\sum_{j=0}^{n-1}(a-\sigma^j a)\in DA.
\]

A finitely generated abelian group killed by \(n\) is finite.

### Theorem 2.4. The real representation determines the quotient

If \(M,M'\) are \(G\)-lattices for cyclic \(G\), and

\[
M\otimes_{\mathbf Z}\mathbf R\simeq M'\otimes_{\mathbf Z}\mathbf R
\]

as real \(G\)-representations, then \(h_G(M)=h_G(M')\).

**Proof.** Choose integral bases. A matrix \(T\) intertwines the actions exactly when it satisfies the rational linear equations

\[
T\rho(g)=\rho'(g)T\quad(g\in G).
\]

Row reduction over \(\mathbf Q\) gives a rational basis \(T_1,\ldots,T_s\) for this solution space; its real solutions are the real span of the same matrices. An invertible real intertwiner exists by hypothesis. Therefore the polynomial

\[
\det(t_1T_1+\cdots+t_sT_s)\in\mathbf Q[t_1,\ldots,t_s]
\]

is not the zero polynomial. A nonzero polynomial over the infinite field \(\mathbf Q\) cannot vanish at every rational tuple: induction on the number of variables reduces this to the fact that a nonzero one-variable polynomial has finitely many roots. Some rational tuple consequently gives an invertible rational intertwiner.

Multiply that matrix by a positive integer clearing denominators. It defines an injective \(G\)-equivariant homomorphism \(M\to M'\) with finite cokernel \(F\). By Propositions 2.2 and 2.3,

\[
h_G(M')=h_G(M)h_G(F)=h_G(M).
\]

This also describes the usual commensurability argument: after identifying the rational representations, the intersection of their lattices has finite index in both. \(\square\)

The theorem will let us replace a group of arithmetic units by a permutation representation after tensoring with \(\mathbf R\). It computes a ratio, not either Tate group separately. Vanishing of \(H^1\), such as Hilbert's Theorem 90, is a separate input.

## Exercises

1. **Easy.** For \(G\) cyclic of order \(n\), compute both Tate groups of \(\mathbf Z\) with trivial action and of \(\mathbf Z[G]\) with its regular action.
2. **Medium.** Prove \(h_G(A)=1\) for finite \(A\) by counting the fibers of \(D\) and \(N\). Explain why this does not imply that either Tate group is zero.
3. **Medium.** Let \(G=\operatorname{Gal}(\mathbf F_{q^n}/\mathbf F_q)\) act on \(A=\mathbf F_{q^n}^{\times}\). Compute both Tate groups and \(h_G(A)\).
4. **Hard.** Prove that an isomorphism of the real representations of two \(G\)-lattices yields an injective equivariant map between the lattices with finite cokernel, and deduce equality of their Herbrand quotients. Identify the step where infinitude of \(\mathbf Q\) is used.

## Solutions

1. For \(\mathbf Z\), \(D=0\) and \(N=n\), so \(\widehat H^0=\mathbf Z/n\mathbf Z\) and \(\widehat H^{-1}=0\). In the regular module, an invariant has every coefficient equal, hence is a multiple of \(S=\sum_g g=N(1)\). The norm of \(\sum a_g g\) is \((\sum a_g)S\). Its kernel is generated by the differences \(\sigma^j-1\), all in \(D\mathbf Z[G]\). Both Tate groups are therefore zero.
2. The fiber counts give \(|\ker D||DA|=|A|=|\ker N||NA|\). Dividing gives \((|\ker D|/|NA|)/(|\ker N|/|DA|)=1\). For a counterexample to vanishing, let \(G\) have prime order \(p\) and act trivially on \(A=\mathbf Z/p\mathbf Z\). Then \(D=N=0\), and both Tate groups equal \(A\). Their equal orders still give quotient 1.
3. The multiplicative group of a finite field is cyclic. Frobenius is \(x\mapsto x^q\), and the norm is \(x\mapsto x^{(q^n-1)/(q-1)}\). Its image has order \(q-1\), hence is all of \(\mathbf F_q^\times=A^G\). Its kernel has order \((q^n-1)/(q-1)\). The difference map is now \(x\mapsto\sigma(x)/x=x^{q-1}\); its image has that same order and lies in the norm kernel. The two are equal. Both Tate groups are trivial and \(h_G(A)=1\).
4. The intertwining matrices solve a rational linear system. Express its solution space in a rational basis \(T_j\). Existence of an invertible real solution says that \(\det(\sum t_jT_j)\) is a nonzero rational polynomial. Infinitude of \(\mathbf Q\) ensures a rational tuple at which it is nonzero, so an invertible rational intertwiner exists. Clearing its denominators gives an injective map of the lattices. An injective integral matrix of full rank has finite cokernel, of order the absolute value of its determinant. That cokernel is a finite \(G\)-module with quotient 1; multiplicativity proves the required equality.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

Section 1 proves the exact cyclic integral resolution. Sections 2–4 prove the connecting maps, the complete six-term sequence, multiplicativity, induced-module calculations and lattice invariance.

- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
- [Jürgen Neukirch, Class Field Theory — The Bonn Lectures, Online Edition 2.0 (May 2015), edited by Alexander Schmidt](https://www.mathi.uni-heidelberg.de/~schmidt/Neukirch-en/Neukirch_cft_02_may15.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.

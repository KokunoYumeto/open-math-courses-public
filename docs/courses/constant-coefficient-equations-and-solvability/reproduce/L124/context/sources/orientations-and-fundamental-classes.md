# Orientations and fundamental classes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Near each of its points, an \(n\)-dimensional manifold looks like \(\mathbf R^n\), and the homology of \(\mathbf R^n\) relative to the complement of a point is a single copy of the coefficient ring in degree \(n\). An orientation is a consistent choice of generators of these local groups. This lesson proves the basic structure theorem behind every duality statement on manifolds: for a compact subset \(K\), the homology of the manifold relative to the complement of \(K\) vanishes above degree \(n\), and an orientation determines a unique class in degree \(n\) that restricts to the chosen generator at every point of \(K\). For a closed oriented manifold this is the fundamental class.

We use singular homology with coefficients in a commutative ring \(R\), as in the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60), whose homology part follows Y. Fomberg's notes: homotopy invariance [Fomberg, Corollary 1.14], the long exact sequence of a pair [Fomberg, Theorem 1.21], excision in both forms [Fomberg, Theorems 1.23 and 1.26], and the homology of spheres. Results from the cohomology part, D. M. Roberts's notes, are cited as [Roberts, …].

Basic references are [Hatcher] and [Miller].

## 1. Local homology

A **topological manifold** of dimension \(n\) is a Hausdorff, second countable space in which every point has an open neighbourhood homeomorphic to \(\mathbf R^n\). A **chart ball** is an open set \(B\) with a homeomorphism \(\varphi:U\to\mathbf R^n\) from an open \(U\supset\overline B\) such that \(\varphi(B)\) is an open ball; its closure is then compact. All homology groups have coefficients in \(R\), which we omit from the notation when no confusion arises. For \(A\subset M\) we write \(M\setminus A\) for the complement.

**Lemma 1.1.** Let \(M\) be an \(n\)-manifold and \(x\in M\). Then \(H_i(M,M\setminus x)\cong R\) for \(i=n\) and \(0\) for \(i\neq n\). More generally, if \(K\) is a compact set contained in a chart ball \(B\) and \(\varphi(K)\) is convex, then \(H_i(M,M\setminus K)\to H_i(M,M\setminus x)\) is an isomorphism for every \(x\in K\).

**Proof.** The closed set \(M\setminus B\) lies in the interior \(M\setminus\overline{\varphi^{-1}(K')}\) of \(M\setminus K\) for a slightly larger compact \(K'\), so excision [Fomberg, Theorem 1.23] identifies \(H_i(M,M\setminus K)\) with \(H_i(B,B\setminus K)\cong H_i(\mathbf R^n,\mathbf R^n\setminus\varphi(K))\). Radial projection from \(\varphi(x)\) deforms \(\mathbf R^n\setminus\varphi(K)\) onto a large sphere about \(\varphi(x)\), and the same holds for \(\mathbf R^n\setminus\varphi(x)\); by convexity, the radial segments from \(\varphi(x)\) leave \(\varphi(K)\) once and do not return, so the inclusion \(\mathbf R^n\setminus\varphi(K)\to\mathbf R^n\setminus\varphi(x)\) is a homotopy equivalence. By homotopy invariance, the long exact sequences of the pairs and the five lemma, \(H_i(\mathbf R^n,\mathbf R^n\setminus\varphi(K))\cong H_i(\mathbf R^n,\mathbf R^n\setminus\varphi(x))\). Finally, \(\mathbf R^n\) is contractible and \(\mathbf R^n\setminus\varphi(x)\simeq S^{n-1}\), so the long exact sequence gives \(H_i(\mathbf R^n,\mathbf R^n\setminus\varphi(x))\cong\tilde H_{i-1}(S^{n-1})\), which is \(R\) for \(i=n\) and \(0\) otherwise. \(\square\)

## 2. Orientations

**Definition 2.1.** An **\(R\)-orientation** of \(M\) is a function \(x\mapsto\mu_x\) assigning to each \(x\in M\) a generator \(\mu_x\) of the free rank-one \(R\)-module \(H_n(M,M\setminus x)\), which is **locally consistent**: every point has a chart ball \(B\) and a class \(\mu_B\in H_n(M,M\setminus B)\) whose image in \(H_n(M,M\setminus y)\) is \(\mu_y\) for every \(y\in B\). The manifold is **\(R\)-orientable** if such a function exists; a \(\mathbf Z\)-orientation is simply called an orientation.

By Lemma 1.1 applied to the closed balls \(\overline{B'}\subset B\), the class \(\mu_B\) is determined by any single \(\mu_y\), \(y\in B\). Consequently, on a connected manifold, two \(R\)-orientations that agree at one point agree everywhere: the set where they agree is open and closed. Every manifold is \(\mathbf Z/2\)-orientable, since \(H_n(M,M\setminus x;\mathbf Z/2)\) has only one generator. A \(\mathbf Z\)-orientation induces an \(R\)-orientation for every \(R\), by the map \(\mathbf Z\to R\). For a connected manifold, a \(\mathbf Z\)-orientation exists if and only if, transported along every loop through local identifications, the generator returns to itself; this is the usual criterion, and a connected orientable manifold has exactly two \(\mathbf Z\)-orientations. Open subsets and products of oriented manifolds are oriented, and every complex manifold has a canonical orientation, given in each holomorphic chart by the standard orientation of \(\mathbf C^n=\mathbf R^{2n}\); holomorphic changes of coordinates preserve it because the real Jacobian determinant of a holomorphic map is \(|\det(\partial F_j/\partial z_k)|^2>0\).

## 3. Classes on compact subsets

**Theorem 3.1.** Let \(M\) be an \(n\)-manifold and \(K\subset M\) compact.

1. \(H_i(M,M\setminus K)=0\) for \(i>n\), and a class \(\alpha\in H_n(M,M\setminus K)\) is zero if and only if its image in \(H_n(M,M\setminus x)\) is zero for every \(x\in K\).
2. If \(x\mapsto\mu_x\in H_n(M,M\setminus x)\) is a locally consistent family of elements (defined as in Definition 2.1, without requiring generators), for instance an \(R\)-orientation, there is a unique class \(\mu_K\in H_n(M,M\setminus K)\) whose image in \(H_n(M,M\setminus x)\) is \(\mu_x\) for every \(x\in K\).

**Proof.** *The Mayer–Vietoris sequence for complements.* Let \(A,B\subset M\) be compact. Put \(U=M\setminus A\), \(V=M\setminus B\), so that \(U\cup V=M\setminus(A\cap B)\) and \(U\cap V=M\setminus(A\cup B)\). The sequence of chain complexes

\[
0\to C(M)/C(U\cap V)\to C(M)/C(U)\oplus C(M)/C(V)\to C(M)/\bigl(C(U)+C(V)\bigr)\to0,
\]

with maps \(c\mapsto(c,c)\) and \((a,b)\mapsto a-b\), is exact. The inclusion \(C(U)+C(V)\to C(U\cup V)\) of the chains subordinate to the cover \(\{U,V\}\) is a quasi-isomorphism [Fomberg, Proposition 1.25], so by the five lemma \(C(M)/(C(U)+C(V))\to C(M)/C(U\cup V)\) is one too. The long exact homology sequence is

\[
\cdots\to H_{i+1}(M,M\setminus(A\cap B))\to H_i(M,M\setminus(A\cup B))\to H_i(M,M\setminus A)\oplus H_i(M,M\setminus B)\to H_i(M,M\setminus(A\cap B))\to\cdots,
\tag{3.1}
\]

natural in \(A\) and \(B\).

*Step 1: if the theorem holds for \(A\), \(B\) and \(A\cap B\), it holds for \(A\cup B\).* In (3.1), for \(i>n\) the outer terms vanish, so \(H_i(M,M\setminus(A\cup B))=0\); this uses \(H_{i+1}(M,M\setminus(A\cap B))=0\) for \(i+1>n\). For \(i=n\), the term on the left vanishes, so \(H_n(M,M\setminus(A\cup B))\) injects into the direct sum; a class that vanishes at every point of \(A\cup B\) vanishes in both summands by (1) for \(A\) and \(B\), hence is zero. For (2), the classes \(\mu_A\) and \(\mu_B\) have the same image \(\mu_{A\cap B}\), by the uniqueness for \(A\cap B\); by exactness they come from a class in \(H_n(M,M\setminus(A\cup B))\), which restricts correctly at every point, and is unique by (1).

*Step 2: \(K\) a finite union of compact sets \(K_1,\ldots,K_m\) in one chart ball \(B\), each with convex image.* Induction on \(m\), using Step 1 with \(A=K_1\cup\cdots\cup K_{m-1}\) and \(B=K_m\): the set \(A\cap B=\bigcup_{j<m}(K_j\cap K_m)\) is a union of \(m-1\) such sets, since intersections of convex sets are convex. The case \(m=1\) is Lemma 1.1, with \(\mu_K\) the class corresponding to \(\mu_x\), independent of \(x\in K\) by local consistency.

*Step 3: \(K\) arbitrary compact in a chart ball \(B\).* Let \(\alpha\in H_i(M,M\setminus K)\), represented by a chain \(z\) of \(M\) whose boundary is a chain in \(M\setminus K\). The boundary is carried by a compact set \(C\subset M\setminus K\). Working in the chart, cover \(\varphi(K)\) by finitely many closed cubes that meet \(\varphi(K)\), all inside \(\varphi(B)\) and disjoint from \(\varphi(C)\), small enough that each meets \(\varphi(K)\) and lies in \(\varphi(B)\setminus\varphi(C)\). Their union pulls back to a compact \(K'\supset K\), a finite union as in Step 2, with \(\partial z\) in \(M\setminus K'\). So \(z\) defines \(\alpha'\in H_i(M,M\setminus K')\) mapping to \(\alpha\). If \(i>n\), \(\alpha'=0\) by Step 2. If \(i=n\) and \(\alpha\) vanishes at every point of \(K\), then for each cube \(Q\) the image of \(\alpha'\) in \(H_n(M,M\setminus Q)\cong H_n(M,M\setminus x)\), \(x\in Q\cap K\), is zero, so \(\alpha'\) vanishes at every point of \(K'\) and \(\alpha'=0\) by Step 2. For (2), restrict \(\mu_{K'}\) from Step 2 to \(K\); uniqueness follows from (1).

*Step 4: general \(K\).* Cover \(K\) by finitely many chart balls \(B_1,\ldots,B_m\) and write \(K=K_1\cup\cdots\cup K_m\) with \(K_j\subset B_j\) compact (for example \(K_j=K\cap\overline{B'_j}\) for smaller balls \(B'_j\) still covering \(K\)). Induction on \(m\) with Step 1, \(A=K_1\cup\cdots\cup K_{m-1}\) and \(B=K_m\): \(A\cap B\) is a compact subset of \(B_m\), covered by Step 3, and \(A\) by the induction hypothesis. \(\square\)

*Reference:* this is the structure theorem of [Hatcher, Lemma 3.27]; [Miller, Theorem 32.1] treats it as the orientation theorem.

## 4. Fundamental classes

Call a function \(x\mapsto\alpha_x\in H_n(M,M\setminus x)\) defined on all of \(M\) a **locally consistent family** if it satisfies the condition of Definition 2.1 without the requirement that the values be generators. Every class \(\alpha\in H_n(M)\) defines one, \(\alpha_x\) being its image; local consistency holds with \(\alpha_B\) the image of \(\alpha\). On a connected manifold a locally consistent family vanishing at one point vanishes everywhere: by Lemma 1.1, the set where it vanishes and the set where it does not are both open.

**Corollary 4.1.** Let \(M\) be a closed (compact) connected \(n\)-manifold. Then \(H_i(M;R)=0\) for \(i>n\), and \(\alpha\mapsto(\alpha_x)\) is an isomorphism from \(H_n(M;R)\) onto the module of locally consistent families. If \(M\) is \(R\)-orientable, \(H_n(M;R)\to H_n(M,M\setminus x;R)\) is an isomorphism for every \(x\), and the class \([M]=\mu_M\) of an \(R\)-orientation is a generator, the **fundamental class**.

**Proof.** Apply Theorem 3.1 with \(K=M\), where \(M\setminus K=\emptyset\): part 1 gives the vanishing and injectivity, part 2 surjectivity. If \(\mu\) is an \(R\)-orientation, then every family is determined by its value at one point \(x\), and every value \(r\mu_x\) extends, namely to \(r\mu\); so evaluation at \(x\) is an isomorphism onto \(H_n(M,M\setminus x)\cong R\), and \(\mu_M\) maps to the generator \(\mu_x\). \(\square\)

**Corollary 4.2.** If \(M\) is a connected noncompact \(n\)-manifold, then \(H_i(M;R)=0\) for \(i\geq n\).

**Proof.** Let \(\alpha\in H_i(M)\) be represented by a cycle \(z\), carried by a compact set, and choose an open \(U\) with compact closure containing it; put \(V=M\setminus\overline U\), which is nonempty and open. Since \(U\) and \(V\) are disjoint, \(H_i(U\cup V,V)=H_i(U)\). Consider the exact sequence of the triple \((M,U\cup V,V)\):

\[
H_{i+1}(M,U\cup V)\longrightarrow H_i(U\cup V,V)\longrightarrow H_i(M,V).
\]

Here \(U\cup V=M\setminus\partial U\) with \(\partial U\) compact, so the first group vanishes for \(i\geq n\) by Theorem 3.1(1), and \(H_i(M,V)=H_i(M,M\setminus\overline U)\). Hence \(H_i(U)\to H_i(M,M\setminus\overline U)\) is injective. For \(i>n\) the target vanishes, so the class of \(z\) in \(H_i(U)\) is zero, and so is \(\alpha\). For \(i=n\), the image of the class of \(z\) is determined, by Theorem 3.1(1), by the family \(x\mapsto\alpha_x\) on \(\overline U\), the restriction of the locally consistent family of \(\alpha\) on \(M\). That family vanishes at the points outside the compact set carrying \(z\), which exist because \(M\) is not compact, so it vanishes everywhere. Hence the class of \(z\) in \(H_n(U)\) is zero, and \(\alpha=0\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that \(H_n(M,M\setminus x;\mathbf Z)\) for \(M=\mathbf R^n\) is generated by the class of a linear simplex containing \(x\) in its interior, and that reversing the orientation of the simplex gives the other generator.

*Solution.* Through the identifications of Lemma 1.1, \(H_n(\Delta^n,\partial\Delta^n)\to H_n(\mathbf R^n,\mathbf R^n\setminus x)\) is an isomorphism for a simplex containing \(x\) in its interior (excision and the deformation of \(\mathbf R^n\setminus x\) onto \(\partial\Delta^n\)), and \(H_n(\Delta^n,\partial\Delta^n)\) is generated by the identity simplex. An odd permutation of the vertices changes the sign of the class.

**Exercise 5.2.** Show that a complex projective space \(\mathbf P^m\) is a closed orientable manifold of real dimension \(2m\), so \(H_{2m}(\mathbf P^m;\mathbf Z)\cong\mathbf Z\).

*Solution.* \(\mathbf P^m\) is a compact complex manifold, oriented canonically (Section 2); apply Corollary 4.1(2).

## References

- [Fomberg] Y. Fomberg, *Algebraic topology* (lecture notes, 2023), licensed CC BY-SA 4.0; the homology part of the core course *Algebraic Topology*. <https://yp.srht.site/notes/>
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002; freely available from the author. <https://pi.math.cornell.edu/~hatcher/AT/ATpage.html>
- [Miller] H. Miller, *Algebraic Topology I: Lecture Notes* (MIT 18.905, 2016), licensed CC BY-NC-SA 4.0. <https://ocw.mit.edu/courses/18-905-algebraic-topology-i-fall-2016/>
- [Roberts] D. M. Roberts, *Algebraic Topology* (lecture notes, 2019), licensed CC BY 4.0; the cohomology part of the core course *Algebraic Topology*. <https://github.com/DavidMichaelRoberts/AlgebraicTopology2019>

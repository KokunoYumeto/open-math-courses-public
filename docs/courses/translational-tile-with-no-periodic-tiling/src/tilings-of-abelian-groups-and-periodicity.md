# Tilings of abelian groups and periodicity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finite set \(F\) in an abelian group \(G\) tiles \(G\) if the translates of \(F\) by the elements of some set \(A\) partition \(G\). The periodic tiling conjecture asked whether every such tile also tiles \(G\) with a set \(A\) that is invariant under a subgroup of finite index. In \(\mathbb Z\) and \(\mathbb Z^2\) it does. OpenAI proved in 2026 that the conjecture fails in \(\mathbb Z^3\) [OpenAI-PT]: there is a finite set \(T\subset\mathbb Z^3\) that tiles \(\mathbb Z^3\) but admits no such tiling, and the union of the unit cubes with lower corners in \(T\) has the same property in \(\mathbb R^3\), even when arbitrary real translations are allowed. This course proves that theorem. This lesson sets up tilings, periods and the passage from \(\mathbb Z^d\) to \(\mathbb R^d\), proves Newman's theorem that every tiling of \(\mathbb Z\) by a finite set is periodic, and lays out the proof of the theorem.

- Tilings and periods (Section 1).
- Tilings of the integers (Section 2).
- Tilings of Euclidean space (Section 3).
- The theorem and the plan of the course (Section 4).

From the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) (Judson, *Abstract Algebra: Theory and Applications*) we use that the order of an element of a finite group divides the order of the group ([Corollary 6.2.3](https://judsonbooks.org/aata-files/aata-html/cosets-section-lagranges-theorem.html)). From the core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40) (Hefferon, *Linear Algebra*, fourth edition) we use that \(\mathbb R^d\) has dimension \(d\) and that in a space of dimension \(d\) every linearly independent set of \(d\) vectors spans the space (Chapter Two, Section III, Corollary 2.14). From the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin, *Measure Theory*, Volume 1) we use countable additivity ([112C](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf)), the measure of boxes and of countable sets in \(\mathbb R^d\) ([115G](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf)), and translation invariance ([134A](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)).

## 1. Tilings and periods

Groups in this course are abelian and written additively. For subsets \(A,F\) of a group \(G\) and \(g\in G\) we write \(A+F=\{a+f:a\in A,\ f\in F\}\) and \(A+g=\{a+g:a\in A\}\), and we call the number \(r_{A,F}(g)\) of pairs \((a,f)\in A\times F\) with \(a+f=g\) the *multiplicity* of \(g\); it is a nonnegative integer or \(\infty\).

**Definition 1.1.** Let \(G\) be a group.

1. For \(A,F\subseteq G\) we write \(A\oplus F=G\) if \(r_{A,F}(g)=1\) for every \(g\in G\): every element of \(G\) has exactly one expression \(a+f\) with \(a\in A\) and \(f\in F\). Equivalently, the translates \(a+F\), \(a\in A\), are pairwise disjoint and cover \(G\).
2. A finite nonempty set \(F\subseteq G\) is a *tile* of \(G\) if \(A\oplus F=G\) for some \(A\subseteq G\). Such a set \(A\) is a *tiling set* of \(F\).
3. A *period* of a set \(A\subseteq G\) is an element \(g\in G\) with \(A+g=A\). The periods of \(A\) form a subgroup \(\operatorname{Per}(A)\) of \(G\).
4. A set \(A\subseteq G\) is *fully periodic* if \(A+\Lambda=A\) for some subgroup \(\Lambda\le G\) of finite index, that is, if \(\operatorname{Per}(A)\) has finite index in \(G\).

In this course *periodic* always means fully periodic. A set with one nonzero period need not be fully periodic: in \(\mathbb Z^2\) the set \(\{0\}\times\mathbb Z\) has the period \((0,1)\), but its periods form the subgroup \(\{0\}\times\mathbb Z\) of infinite index. The periods form a subgroup because \(A+g=A\) and \(A+h=A\) give \(A+(g+h)=A\) and \(A-g=A\).

**Lemma 1.2** (elementary facts). Let \(A,F\subseteq G\) with \(A\oplus F=G\).

1. For \(g,h\in G\), \((A+g)\oplus(F+h)=G\), and \(\operatorname{Per}(A+g)=\operatorname{Per}(A)\). If \(\varphi\colon G\to G'\) is an isomorphism of groups, then \(\varphi(A)\oplus\varphi(F)=G'\) and \(\operatorname{Per}(\varphi(A))=\varphi(\operatorname{Per}(A))\). So whether a finite set is a tile, and whether it has a fully periodic tiling set, does not change under translation of the set or under isomorphisms.
2. If \(H\le G\) is a subgroup, then \(A\oplus H=G\) holds exactly when \(A\) contains exactly one element of every coset of \(H\).
3. A set \(B\subseteq G\) is fully periodic exactly when it is the union of finitely many cosets of one subgroup of finite index.

*Proof.* (1) The pairs \((a,f)\) with \(a+f=x-g-h\) correspond to the pairs \((a+g,f+h)\) with sum \(x\), so \(r_{A+g,F+h}(x)=r_{A,F}(x-g-h)=1\). A translate \(A+g+\lambda\) equals \(A+g\) exactly when \(A+\lambda=A\). For the isomorphism, \(r_{\varphi(A),\varphi(F)}(\varphi(x))=r_{A,F}(x)\) and \(\varphi(A)+\varphi(\lambda)=\varphi(A+\lambda)\).

(2) An element \(x\) lies in \(a+H\) exactly when \(a\in x-H=x+H\). Hence \(r_{A,H}(x)=\#\bigl(A\cap(x+H)\bigr)\), and this is \(1\) for every \(x\) exactly when every coset meets \(A\) in one point.

(3) If \(B+\Lambda=B\) with \([G:\Lambda]<\infty\), then \(b+\Lambda\subseteq B\) for every \(b\in B\), so \(B\) is a union of cosets of \(\Lambda\), of which there are finitely many. Conversely, a union of cosets of \(\Lambda\) is invariant under \(\Lambda\). \(\square\)

**Definition 1.3** (systems of tiling equations). Let \(F_1,\ldots,F_s\subseteq G\) be finite and nonempty. A *common solution* of the system
\[
A\oplus F_\nu=G\qquad(1\le\nu\le s)
\]
is one set \(A\subseteq G\) that satisfies all \(s\) equations. A common solution is fully periodic if \(A\) is.

The point of the definition is that the unknown \(A\) is the same in every equation. Separate solutions of the individual equations would not do.

**Example 1.4** (dominoes). Let \(G=\mathbb Z^2\) and \(F=\{(0,0),(1,0)\}\). For every function \(\varepsilon\colon\mathbb Z\to\{0,1\}\) put
\[
A_\varepsilon=\{(2k+\varepsilon(r),\,r):k,r\in\mathbb Z\}.
\]
Row \(r\) of \(\mathbb Z^2\) is the disjoint union of the pairs \(\{(2k+\varepsilon(r),r),(2k+\varepsilon(r)+1,r)\}\), so \(A_\varepsilon\oplus F=\mathbb Z^2\). Every \(A_\varepsilon\) has the period \((2,0)\). If \(\varepsilon\) has a period \(N\ge1\), then \(A_\varepsilon\) is invariant under the subgroup generated by \((2,0)\) and \((0,N)\), which has index \(2N\). Conversely, if \(A_\varepsilon+\Lambda=A_\varepsilon\) with \([\mathbb Z^2:\Lambda]=M<\infty\), then \((0,M)\in\Lambda\) by Corollary 6.2.3 of Judson applied to the finite group \(\mathbb Z^2/\Lambda\), and \(\varepsilon\) has the period \(M\). So \(F\) has fully periodic tiling sets, and also tiling sets with a nonzero period that are not fully periodic. The periodic tiling question asks for one fully periodic tiling set, not that all tiling sets be periodic.

## 2. Tilings of the integers

**Theorem 2.1** (Newman). Let \(F\subset\mathbb Z\) be finite and nonempty, and let \(A\oplus F=\mathbb Z\). Then \(A+p=A\) for some integer \(p\ge1\). In particular \(A\) is fully periodic.

*Proof.* By Lemma 1.2(1) we may translate \(F\) so that its least element is \(0\); let \(D\) be its largest element. If \(D=0\), then \(F=\{0\}\), \(A=\mathbb Z\) and \(p=1\) works. Let \(D\ge1\). For \(n\in\mathbb Z\) the *state* at \(n\) is the word of \(D\) bits
\[
s_n=\bigl(\mathbf 1_A(n-D),\ldots,\mathbf 1_A(n-1)\bigr),
\]
where \(\mathbf 1_A\) is the indicator function of \(A\). Since \(F\subseteq[0,D]\), the elements \(a\in A\) with \(n\in a+F\) lie in \([n-D,n]\), and exactly one element of \(A\) has this property.

*The state \(s_n\) determines \(s_{n+1}\).* The word \(s_{n+1}\) consists of the last \(D-1\) bits of \(s_n\) followed by \(\mathbf 1_A(n)\). If some \(a\in A\cap[n-D,n-1]\) has \(n-a\in F\), then \(n\) is covered by \(a\), and \(n\notin A\) because \(n=n+0\) with \(0\in F\) would be a second expression. Otherwise the unique element covering \(n\) is \(n\) itself, so \(n\in A\). The set \(A\cap[n-D,n-1]\) is read off from \(s_n\).

*The state \(s_{n+1}\) determines \(s_n\).* The word \(s_n\) consists of \(\mathbf 1_A(n-D)\) followed by the first \(D-1\) bits of \(s_{n+1}\). The element \(n-D\) covers \(n\), since \(D\in F\). If some \(a\in A\cap[n-D+1,n]\) has \(n-a\in F\), then \(n-D\notin A\); otherwise \(n-D\in A\). The set \(A\cap[n-D+1,n]\) is read off from \(s_{n+1}\).

There are \(2^D\) words of \(D\) bits, so two of the states \(s_0,s_1,\ldots,s_{2^D}\) coincide, say \(s_{n_1}=s_{n_2}\) with \(n_1<n_2\). Put \(p=n_2-n_1\). By induction forward and backward from \(n_1\), the two rules give \(s_{n+p}=s_n\) for every \(n\in\mathbb Z\). Comparing the last bits of \(s_{n+p+1}\) and \(s_{n+1}\) gives \(\mathbf 1_A(n+p)=\mathbf 1_A(n)\) for every \(n\), that is, \(A+p=A\). The subgroup \(p\mathbb Z\) has index \(p\). \(\square\)

The argument is due to Newman [Newman 1977]. It proves more than the periodic tiling conjecture asks in dimension one: every tiling set is periodic. For \(\mathbb Z\times G_0\) with a finite group \(G_0\), a variant of the argument shows that every tile has a fully periodic tiling set, although not every tiling set need be fully periodic (Exercise 5.3). So a counterexample needs at least two infinite directions.

**Remark 2.2** (the plane). In \(\mathbb Z^2\) not every tiling set of a tile is fully periodic (Example 1.4), but every finite tile of \(\mathbb Z^2\) has a fully periodic tiling set. Bhattacharya proved this with methods of ergodic theory [Bhattacharya 2020, Theorem 1.1]. Greenfeld and Tao gave a second proof, with a bound on the size of a period [Greenfeld–Tao 2021, Theorem 1.5], and showed that every tiling set of \(\mathbb Z^2\) by one finite tile is a disjoint union of finitely many sets each of which has a nonzero period [Greenfeld–Tao 2021, Theorem 1.3(i)]. These theorems are not used in this course and are not proved here. Together with Theorem 2.1 they show that the lattice \(\mathbb Z^3\) of the main theorem has the least possible dimension.

## 3. Tilings of Euclidean space

We write \(m\) for Lebesgue measure on \(\mathbb R^d\). A set is *null* if its Lebesgue outer measure is \(0\).

**Definition 3.1.** Let \(\Omega\subseteq\mathbb R^d\) be bounded and Lebesgue measurable with \(m(\Omega)>0\), and let \(\mathcal A\subseteq\mathbb R^d\).

1. \(\Omega\) *tiles* \(\mathbb R^d\) with the tiling set \(\mathcal A\), written \(\mathcal A\oplus\Omega=\mathbb R^d\) almost everywhere, if the points of \(\mathbb R^d\) that lie in no translate \(a+\Omega\) with \(a\in\mathcal A\), or in more than one, form a null set.
2. A *lattice of full rank* in \(\mathbb R^d\) is a subgroup \(L=\mathbb Zb_1+\cdots+\mathbb Zb_d\) generated by a basis \(b_1,\ldots,b_d\) of \(\mathbb R^d\).
3. The tiling set \(\mathcal A\) is *fully periodic* if \(\mathcal A+L=\mathcal A\) for some lattice \(L\) of full rank.

**Lemma 3.2** (subgroups of \(\mathbb Z^d\)).

1. If \(\Lambda\le\mathbb Z^d\) has finite index \(M\), then \(M\mathbb Z^d\subseteq\Lambda\). In particular \(\Lambda\) contains the basis \(Me_1,\ldots,Me_d\) of \(\mathbb R^d\).
2. If a subgroup \(L\le\mathbb Z^d\) contains \(d\) vectors that are linearly independent over \(\mathbb R\), then \(L\) has finite index in \(\mathbb Z^d\).

*Proof.* (1) The quotient \(\mathbb Z^d/\Lambda\) is a finite group of order \(M\). By Corollary 6.2.3 of Judson the order of \(g+\Lambda\) divides \(M\), so \(Mg\in\Lambda\) for every \(g\in\mathbb Z^d\).

(2) Let \(v_1,\ldots,v_d\in L\) be linearly independent. By Corollary 2.14 of Hefferon they span \(\mathbb R^d\). Let \(x\in\mathbb Z^d\), write \(x=\sum_is_iv_i\) with real \(s_i\), and put
\[
y=x-\sum_{i=1}^d\lfloor s_i\rfloor v_i=\sum_{i=1}^d(s_i-\lfloor s_i\rfloor)v_i .
\]
Then \(y\in\mathbb Z^d\), \(x-y\in L\), and every coordinate of \(y\) has absolute value at most \(R=\sum_i\|v_i\|_\infty\), since \(0\le s_i-\lfloor s_i\rfloor<1\). So every coset of \(L\) in \(\mathbb Z^d\) contains a point of the finite set \(\{y\in\mathbb Z^d:\|y\|_\infty\le R\}\), and there are at most \((2R+1)^d\) cosets. \(\square\)

**Proposition 3.3** (thickening). Let \(T\subset\mathbb Z^d\) be finite and nonempty, and put
\[
\Omega=T+[0,1]^d=\bigcup_{t\in T}\bigl(t+[0,1]^d\bigr).
\]

1. If \(A\oplus T=\mathbb Z^d\), then \(A\oplus\Omega=\mathbb R^d\) almost everywhere.
2. If moreover \(A\) is invariant under a subgroup of finite index of \(\mathbb Z^d\), then \(A\) is a fully periodic tiling set of \(\Omega\).

*Proof.* The set \(\Omega\) is a finite union of closed cubes, so it is bounded and measurable, and for \(t\in T\), \(m(\Omega)\ge m(t+[0,1]^d)=1\) by 115G and 134A. Let \(Z\) be the set of points of \(\mathbb R^d\) with at least one integer coordinate. It is the union of the countably many hyperplanes \(\{x:x_i=k\}\), \(1\le i\le d\), \(k\in\mathbb Z\). Each hyperplane is the union of countably many closed boxes with one side of length \(0\), which are null by 115G, so \(Z\) is null by 112C.

Let \(x\notin Z\) and let \(\lfloor x\rfloor\in\mathbb Z^d\) be the point with coordinates \(\lfloor x_i\rfloor\). If \(z\in\mathbb Z^d\) and \(x\in z+[0,1]^d\), then \(z_i\le x_i\le z_i+1\), and since \(x_i\notin\mathbb Z\) this forces \(z_i=\lfloor x_i\rfloor\). So \(x\) lies in the closed unit cube with lower corner \(z\in\mathbb Z^d\) exactly when \(z=\lfloor x\rfloor\). Consequently \(x\in a+\Omega\), for \(a\in A\), exactly when \(\lfloor x\rfloor-a\in T\), and the number of \(a\in A\) with \(x\in a+\Omega\) is \(r_{A,T}(\lfloor x\rfloor)=1\). This proves (1). For (2), Lemma 3.2(1) gives \(M\ge1\) with \(A+M\mathbb Z^d=A\), and \(M\mathbb Z^d\) is the lattice generated by the basis \(Me_1,\ldots,Me_d\). \(\square\)

The converse of Proposition 3.3 fails in general. A tiling set of \(\Omega\) need not lie in \(\mathbb Z^d\) or in any translate of it, because cubes can slide against each other (Exercise 5.5). The tile of the main theorem is built so that every tiling of \(\mathbb R^3\) by its thickening is rigid enough to come back to \(\mathbb Z^3\); this is done in the last lesson, [Passing to three-dimensional space](passing-to-three-dimensional-space.md).

## 4. The theorem and the plan of the course

**Theorem 4.1** (OpenAI [OpenAI-PT, Theorem 1.1]). There is a finite nonempty set \(T\subset\mathbb Z^3\) such that:

1. \(T\) tiles \(\mathbb Z^3\), but no tiling set \(A\) with \(A\oplus T=\mathbb Z^3\) is invariant under a subgroup of finite index of \(\mathbb Z^3\);
2. the set \(\Omega=T+[0,1]^3\) tiles \(\mathbb R^3\) almost everywhere, but no tiling set \(\mathcal A\) with \(\mathcal A\oplus\Omega=\mathbb R^3\) almost everywhere is invariant under a lattice of full rank in \(\mathbb R^3\).

The discrete and the continuous forms of the periodic tiling conjecture are Conjectures 1.2 and 1.3 of [Greenfeld–Tao 2024], whose introduction records their origins in work of Stein, of Grünbaum and Shephard, and of Lagarias and Wang, and surveys what was known. Greenfeld and Tao disproved both forms in high dimension: they constructed a tile in \(\mathbb Z^2\times G_0\), for a finite group \(G_0\) whose order is a power of two, with no fully periodic tiling set [Greenfeld–Tao 2024, Theorem 1.4]. Since \(\mathbb Z^2\times G_0\) is a quotient of \(\mathbb Z^d\) for \(d\) large, a reduction of Meyerovitch, Sanadhya and Solomon [Meyerovitch–Sanadhya–Solomon 2025, Corollary 1.2] gives counterexamples in \(\mathbb Z^d\), and Greenfeld and Tao pass from these to \(\mathbb R^d\) [Greenfeld–Tao 2024, Corollaries 1.6 and 1.7]. Theorem 4.1 settles dimension three, the least possible one by Theorem 2.1 and Remark 2.2. OpenAI's release also contains a formalization in Lean whose main statement combines Theorem 4.1 with the minimality of dimension three [OpenAI-PT-Lean].

Demaine and Langerman used the tile of Theorem 4.1 to settle a decidability question [Demaine–Langerman 2026]. Combining the decorated Sudoku construction of Greenfeld and Tao with a cyclic encoding derived from the tile of Theorem 4.1, and a reduction of Kim that makes the tile connected, they prove that tiling \(\mathbb Z^3\) by translations of a single finite connected set is co-RE-complete, hence undecidable, and that the same holds for a single connected polycube in \(\mathbb R^3\) [Demaine–Langerman 2026, Theorem 1.1]. For a single tile in \(\mathbb Z^2\) the question is decidable [Demaine–Langerman 2026, Table 1], by the periodicity results of Remark 2.2. The number of elements of a tile matters too. Tan and Zhang proved that a finite set \(F\subseteq\mathbb Z^d\) with \(2q\) elements, \(q\) an odd prime, or with \(9\) elements, that tiles \(\mathbb Z^d\) has a fully periodic tiling set, in every dimension \(d\) [Tan–Zhang 2026, Theorem 1.1]; with earlier results of Szegedy on tiles with a prime number of elements and with four elements, every tile with fewer than twelve elements has a fully periodic tiling set, except possibly when it has eight [Tan–Zhang 2026, Section 1]. In the plane the continuous form of the conjecture is open. De Dios Pont, Grebík, Greenfeld and Madrid treat bounded open sets \(\Omega\subset\mathbb R^2\) whose boundary is a finite union of segments parallel to the axes. Every tiling by such an \(\Omega\) of finite local complexity is weakly periodic, and then \(\Omega\) also has a periodic tiling [de Dios Pont–Grebík–Greenfeld–Madrid 2026, Theorem 1.1]; every topologically minimal tiling is weakly periodic, and \(\Omega\) has a quasi-periodic tiling invariant under a nonzero translation [de Dios Pont–Grebík–Greenfeld–Madrid 2026, Theorem 1.3]; and whether such an \(\Omega\) with real algebraic vertex coordinates tiles the plane is decidable [de Dios Pont–Grebík–Greenfeld–Madrid 2026, Theorem 1.4]. An and He proved that every integral self-affine tile in \(\mathbb R^2\) has a fully periodic tiling [An–He 2026, Theorem 1.9].

The proof has four stages. Each stage produces an object that has at least one solution but no fully periodic solution.

1. [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md). For a large prime \(p\), a finite set of allowed words of length \(p^2\) over the alphabet \(\{1,\ldots,p-1\}\) constrains arrays \(W(n,m)\) along all lines of integer slope. One such array has no constant column, but no such array has a vertical period.
2. Three lessons build finitely many finite tiles in \(G=\mathbb Z^2\times V\), with \(V\) a finite *cyclic* group, whose tiling equations have a common solution but no fully periodic one. [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) represents a symbol by the dependence of a function on one of its input digits and forbids the forbidden words. [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) forces enough dependence to read off an array from every common solution, and shows that a fully periodic common solution would give an array with a vertical period. [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md) constructs one common solution explicitly.
3. [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md) stacks the finitely many equations into one tile in \(\mathbb Z^2\times\mathbb Z/Q\mathbb Z\).
4. [Passing to three-dimensional space](passing-to-three-dimensional-space.md) builds the tile \(T\subset\mathbb Z^3\) from the tile in \(\mathbb Z^2\times\mathbb Z/Q\mathbb Z\), which is a quotient of \(\mathbb Z^3\), and handles arbitrary real translations of its thickening.

The proof runs in two directions. Forward, an explicit array gives a common solution, a common solution gives a tiling by the stacked tile, and that tiling gives tilings of \(\mathbb Z^3\) and \(\mathbb R^3\). Backward, a fully periodic tiling at any stage gives a fully periodic solution at the stage before, and at the end an array with no constant column and with a vertical period, which the first stage excludes. The finite group is kept cyclic so that the group of the third stage is a quotient of \(\mathbb Z^3\): \(\mathbb Z^2\times\mathbb Z/Q\mathbb Z\) is the quotient of \(\mathbb Z^3\) by the subgroup generated by \((0,0,Q)\).

## 5. Exercises

**5.1.** (a) Show that \(\{0,1,3\}\) does not tile \(\mathbb Z\). (b) Find all tiling sets of \(\{0,2\}\) in \(\mathbb Z\).

**5.2.** Show that every tiling set of \(\mathbb Z^2\) by the domino \(F=\{(0,0),(1,0)\}\) is one of the sets \(A_\varepsilon\) of Example 1.4.

**5.3.** Let \(G_0\) be a finite group and let \(F\subset\mathbb Z\times G_0\) be a tile. (a) Show that \(F\) has a tiling set \(A'\) with \(A'+(p,0)=A'\) for some integer \(p\ge1\), and that \(A'\) is fully periodic. (b) For \(G_0=\mathbb Z/2\mathbb Z\) and \(F=\{(0,0),(0,1)\}\), find a tiling set that is not fully periodic.

**5.4.** (a) Let \(G\) be finite and \(A\oplus F=G\). Show that \(\#A\cdot\#F=\#G\). (b) Let \(A\oplus F=\mathbb Z\) and \(A+p=A\) with \(p\ge1\). Show that \(\#F\) divides \(p\).

**5.5.** Let \(\theta_r=\sqrt2\,r^2\) for \(r\in\mathbb Z\) and \(\mathcal A=\{(k+\theta_r,\,r):k,r\in\mathbb Z\}\). Show that \(\mathcal A\oplus[0,1]^2=\mathbb R^2\) almost everywhere, that \(\mathcal A\) is not contained in any translate \(c+\mathbb Z^2\), and that \(\mathcal A\) is not fully periodic.

## 6. Solutions

**5.1.** (a) Suppose \(A\oplus\{0,1,3\}=\mathbb Z\) and \(a\in A\); then \(a\), \(a+1\) and \(a+3\) are covered by \(a\). The point \(a+2\) is covered by some \(a'\in A\) with \(a+2-a'\in\{0,1,3\}\), so \(a'\in\{a+2,a+1,a-1\}\). But \(a'=a+2\) also covers \(a+3\), \(a'=a+1\) covers \(a+1\), and \(a'=a-1\) covers \(a\); each gives a second expression of a point already covered by \(a\). (b) The translates of \(\{0,2\}\) keep parities apart, and \(B\oplus\{0,2\}=2\mathbb Z\) exactly when \(\frac12B\oplus\{0,1\}=\mathbb Z\), that is, \(\frac12B=2\mathbb Z\) or \(2\mathbb Z+1\). The same holds on the odd integers after translation by \(1\). So the tiling sets are \((4\mathbb Z+2\varepsilon_0)\cup(4\mathbb Z+1+2\varepsilon_1)\) with \(\varepsilon_0,\varepsilon_1\in\{0,1\}\); all four have the period \(4\).

**5.2.** Each translate of \(F\) lies in one row, so the first coordinates of the points of \(A\) in row \(r\) form a set \(R\subseteq\mathbb Z\) with \(R\oplus\{0,1\}=\mathbb Z\). Let \(a\in R\). The point \(a+2\) is covered by \(a+1\) or by \(a+2\); the first would cover \(a+1\) a second time, so \(a+2\in R\). The point \(a-1\) is covered by \(a-1\) or by \(a-2\); the first would cover \(a\) a second time, so \(a-2\in R\). Hence \(a+2\mathbb Z\subseteq R\). The translates of \(\{0,1\}\) by \(a+2\mathbb Z\) already cover \(\mathbb Z\), so \(R=a+2\mathbb Z\), which is \(2\mathbb Z+\varepsilon(r)\) for some \(\varepsilon(r)\in\{0,1\}\). Thus \(A=A_\varepsilon\).

**5.3.** (a) Let \(A\oplus F=\mathbb Z\times G_0\). Translate \(F\) so that the least first coordinate of its points is \(0\), and let \(D\ge0\) be the largest. Call \(C_k=\{g:(k,g)\in A\}\subseteq G_0\) the column of \(A\) at \(k\). A point of the column \(\{n\}\times G_0\) can only be covered by elements of \(A\) in the columns \(n-D,\ldots,n\), so its multiplicity depends only on \(C_{n-D},\ldots,C_n\). There are finitely many sequences of \(D+1\) subsets of \(G_0\), so there are \(n_1<n_2\) with \(C_{n_1-i}=C_{n_2-i}\) for \(0\le i\le D\). Put \(p=n_2-n_1\), and let \(A'\) be the set whose column at \(k\) is \(C_{k'}\), where \(k'\) is the unique integer with \(n_1-D\le k'<n_1-D+p\) and \(k'\equiv k\pmod p\). Then \(A'+(p,0)=A'\). Applying \(C_k=C_{k+p}\) for \(n_1-D\le k\le n_1\) repeatedly shows that \(A'\) and \(A\) have the same columns at all \(k\) with \(n_1-D\le k\le n_2\). For \(n_1\le n\le n_2\), the columns \(n-D,\ldots,n\) lie in that range, so every point of the column \(\{n\}\times G_0\) has multiplicity \(1\) for \(A'\) as for \(A\). These \(p+1\) consecutive columns represent all residues of \(n\) modulo \(p\), and \(A'\) is invariant under \((p,0)\), so \(A'\oplus F=\mathbb Z\times G_0\). The subgroup generated by \((p,0)\) has index \(p\cdot\#G_0\). (b) \(A\oplus F=\mathbb Z\times G_0\) holds exactly when \(A\) has one point in every column, so \(A=\{(k,\varepsilon(k)):k\in\mathbb Z\}\) for any \(\varepsilon\colon\mathbb Z\to\mathbb Z/2\mathbb Z\). As in Example 1.4, \(A\) is fully periodic exactly when \(\varepsilon\) is periodic; take \(\varepsilon(k)=1\) for \(k\) a square and \(\varepsilon(k)=0\) otherwise. This \(\varepsilon\) has no period \(N\ge1\): since \(\varepsilon(0)=1\), a period \(N\) would make every positive multiple of \(N\) a square, and \(2N^2\) is not.

**5.4.** (a) \(G\) is the disjoint union of the \(\#A\) translates \(a+F\), each with \(\#F\) elements. (b) Let \(\pi\colon\mathbb Z\to\mathbb Z/p\mathbb Z\) be reduction. If \(f\ne f'\) in \(F\) had \(\pi(f)=\pi(f')\), then for \(a\in A\) the point \(a+f\) would also equal \((a+f-f')+f'\) with \(a+f-f'\in A+p\mathbb Z=A\), a second expression. So \(\pi\) is injective on \(F\). For \(x\in\mathbb Z\), an expression \(\pi(x)=\pi(a)+\pi(f)\) with \(a\in A\), \(f\in F\) means \(x-f\in A+p\mathbb Z=A\), so the number of such expressions, counted by \(f\), is \(r_{A,F}(x)=1\). Hence \(\pi(A)\oplus\pi(F)=\mathbb Z/p\mathbb Z\), and (a) gives \(\#\pi(A)\cdot\#F=p\).

**5.5.** The translates of \([0,1]^2\) by the points of row \(r\) are the squares \([k+\theta_r,k+\theta_r+1]\times[r,r+1]\), which cover the strip \(\mathbb R\times[r,r+1]\) and overlap only on segments; the overlaps and the lines \(\mathbb R\times\{r\}\) are null by 115G and 112C. If \(\mathcal A\subseteq c+\mathbb Z^2\), then \(\theta_1-\theta_0=\sqrt2\) would be an integer. If \(\mathcal A+L=\mathcal A\) for a lattice \(L\) of full rank, then \(L\subseteq\mathcal A-\mathcal A\subseteq\mathbb R\times\mathbb Z\), and \(L\) contains a vector \((u,v)\) with \(v\ne0\). The translation by \((u,v)\) maps row \(r\) onto row \(r+v\), so \(\theta_{r+v}-\theta_r-u\in\mathbb Z\) for every \(r\). Subtracting this for \(r\) and \(r+1\) gives
\[
\begin{aligned}&(\theta_{r+1+v}-\theta_{r+1})-(\theta_{r+v}-\theta_r)\\&\quad=2\sqrt2\,v\in\mathbb Z,\end{aligned}
\]
which is false.

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
- [OpenAI-PT-Lean] OpenAI, Lean formalization of the periodic tiling counterexample in dimension three, OpenAI Math Release, scope note `lean/docs/155.md`. https://github.com/openai/math/blob/main/lean/docs/155.md
- [Greenfeld–Tao 2024] R. Greenfeld, T. Tao, *A counterexample to the periodic tiling conjecture*, Ann. of Math. 200 (2024), 301–363. https://arxiv.org/abs/2211.15847
- [Greenfeld–Tao 2021] R. Greenfeld, T. Tao, *The structure of translational tilings in \(\mathbb Z^d\)*, Discrete Analysis 2021, Paper No. 16. https://arxiv.org/abs/2010.03254
- [Bhattacharya 2020] S. Bhattacharya, *Periodicity and decidability of tilings of \(\mathbb Z^2\)*, Amer. J. Math. 142 (2020), 255–266. https://arxiv.org/abs/1602.05738
- [Meyerovitch–Sanadhya–Solomon 2025] T. Meyerovitch, S. Sanadhya, Y. Solomon, *A note on reduction of tiling problems*, Israel J. Math. 267 (2025), 421–435. https://arxiv.org/abs/2211.07140
- [Newman 1977] D. J. Newman, *Tesselation of integers*, J. Number Theory 9 (1977), 107–111, publisher's open archive. https://doi.org/10.1016/0022-314X(77)90054-3
- [Demaine–Langerman 2026] E. D. Demaine, S. Langerman, *Tiling 3D by translates of a single polycube is undecidable*, arXiv:2610.12392 (October 2026). https://arxiv.org/abs/2610.12392
- [Tan–Zhang 2026] H. Tan, Y. Zhang, *Periodic tilings of cardinality twice a prime or nine in arbitrary dimension*, arXiv:2609.26576 (September 2026). https://arxiv.org/abs/2609.26576
- [de Dios Pont–Grebík–Greenfeld–Madrid 2026] J. de Dios Pont, J. Grebík, R. Greenfeld, J. Madrid, *Translational tilings by axis-parallel polygonal sets*, arXiv:2610.15785 (October 2026). https://arxiv.org/abs/2610.15785
- [An–He 2026] L.-X. An, T.-T. He, *Translational self-affine tiles in \(\mathbb R^n\)*, arXiv:2610.16340 (October 2026). https://arxiv.org/abs/2610.16340

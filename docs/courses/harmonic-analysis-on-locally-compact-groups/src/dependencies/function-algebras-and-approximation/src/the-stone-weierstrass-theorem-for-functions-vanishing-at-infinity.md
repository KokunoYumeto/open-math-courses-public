# The Stone–Weierstrass theorem for functions vanishing at infinity

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session. The October revisions correct two points found by an AI reviewer in a separate OpenAI Codex session and add proofs of the background facts that the core courses leave as exercises; they are self-checked by the writing AI. Public domain (CC0).*

This lesson proves the Stone–Weierstrass theorem for continuous functions that vanish at infinity. Let \(X\) be a locally compact Hausdorff space, and let \(A\) be a subalgebra of \(C_0(X)\) that is closed under complex conjugation, separates the points of \(X\), and has no common zero. Then every function in \(C_0(X)\) is a uniform limit of functions in \(A\) ([Theorem 10.1](#oa-fnd-sw-09)). The algebra need not contain the constant functions, and \(X\) need not be compact, \(\sigma\)-compact or metrizable. Commutative C\*-algebras and harmonic analysis on locally compact groups need the theorem in this form.

The proof follows the classical route. A recursion for polynomials without constant term approximates \(|t|\) (Section 6). With interpolation at two points (Section 7) and Stone's lattice lemma (Section 8), it gives the real theorem on compact spaces (Section 9). The one-point compactification (Section 3) carries the result over to \(C_0(X)\), and real and imaginary parts give the complex theorem (Section 10). Sections 11–13 give worked examples, show that each hypothesis is needed, and describe the closure of an arbitrary self-adjoint subalgebra. Sections 2–5 develop the function spaces and the topology that surround the proof: the one-point compactification, locally compact spaces, Urysohn's lemma and metrizability. Sections 14–18 add classical companions: the Weierstrass theorem with Bernstein's constructive proof, Korovkin's theorem, further density theorems, the Tietze extension theorem, the disc algebra, and approximation by polynomials with integer coefficients.

The lesson assumes the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10), [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) and [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): open and closed sets, continuity, compactness defined by open covers, metric spaces and uniform convergence. A few facts about numbers, the Riemann integral and the exponential function are taken from the core courses; they are listed near the end, under "Results used from other lessons", with the place of each proof. No other lesson is needed.

Weierstrass proved in 1885 that every continuous function on a closed bounded interval is a uniform limit of polynomials [Weierstrass 1885]. Stone proved the general theorem in 1937 [Stone 1937] and gave a simpler proof, by lattices of functions, in 1948. The one-point compactification is due to Alexandroff [Alexandroff 1924]. The core course *Real Analysis II* proves the Weierstrass theorem and the real and complex Stone–Weierstrass theorems for compact metric spaces ([Lebl, Section 11.7](https://www.jirka.org/ra/html/sec_stoneweier.html)). Free texts that treat the theorems are [van Neerven] and [Blackadar].

## 1. Conventions

*Spaces.* A *neighbourhood* of a point is a set that contains an open set containing the point. *Compact* means that every open cover has a finite subcover; the Hausdorff property is not part of the word. A space is *locally compact Hausdorff* (LCH) if it is Hausdorff and every point has a compact neighbourhood. Five elementary facts are used throughout.

- (K1) A closed set \(C\) contained in a compact set \(K\) is compact. Add \(X\setminus C\) to an open cover of \(C\), take a finite subcover of \(K\), and discard \(X\setminus C\).
- (K2) A continuous image of a compact set is compact, and a finite union of compact sets is compact.
- (K3) Let \(X\) be Hausdorff, \(K\subseteq X\) compact and \(x\notin K\). Then \(x\) and \(K\) have disjoint open neighbourhoods. For each \(y\in K\) choose disjoint open sets \(U_y\ni x\) and \(V_y\ni y\). Finitely many sets \(V_{y_1},\dots,V_{y_m}\) cover \(K\); take \(U_{y_1}\cap\dots\cap U_{y_m}\) and \(V_{y_1}\cup\dots\cup V_{y_m}\). In particular, compact subsets of Hausdorff spaces are closed.
- (K4) Let a continuous map from a compact space onto a Hausdorff space be one-to-one. Then its inverse is continuous, because the map sends closed sets to closed sets: a closed set is compact by (K1), its image is compact by (K2), and a compact subset of a Hausdorff space is closed by (K3).
- (K5) A continuous \(u:K\to\mathbb R\) on a nonempty compact space is bounded and attains its maximum and minimum. The open sets \(\{u<n\}\) cover \(K\), so \(u\) is bounded above. If \(u<s=\sup u\) everywhere, the open sets \(\{u<s-1/n\}\) cover \(K\), and a finite subcover gives \(u\leq s-1/N\), which is absurd. Apply this to \(-u\) for the minimum.

*Functions.* Functions are complex-valued unless they are called real. For a bounded function \(f\) on a set \(S\), put \(\|f\|=\sup_S|f|\), and \(\|f\|_T=\sup_T|f|\) for \(T\subseteq S\). On a space \(X\), \(C(X)\) and \(C(X;\mathbb R)\) are the continuous complex and real functions, and \(C_b(X)\) the bounded continuous ones. The *support* of \(f\) is the closure of \(\{f\neq0\}\), and \(C_c(X)\) consists of the continuous functions with compact support. \(C_0(X)\) consists of the continuous \(f\) with
\[
\{|f|\geq\varepsilon\}=\{x\in X:\ |f(x)|\geq\varepsilon\}\ \text{compact for every }\varepsilon>0 .
\tag{1.1}
\]
Equivalently, for every \(\varepsilon>0\) there is a compact set \(K\) with \(|f|<\varepsilon\) off \(K\). Indeed, if there is such a \(K\), then the closed set \(\{|f|\geq\varepsilon\}\) lies in \(K\) and is compact by (K1); conversely, \(K=\{|f|\geq\varepsilon\}\) will do. Real versions carry the suffix \(;\mathbb R\), as in \(C_0(X;\mathbb R)\).

*Algebras.* On a set \(S\), an *algebra of functions* is a complex linear space of functions \(S\to\mathbb C\) that is closed under pointwise products. A *real algebra* is the same with real functions and real scalars. No unit is assumed. An algebra \(A\) is *self-adjoint* if \(f\in A\) implies \(\bar f\in A\). It *separates points* if for \(x\neq y\) some \(f\in A\) has \(f(x)\neq f(y)\). It *vanishes nowhere* if for every \(x\) some \(f\in A\) has \(f(x)\neq0\). Its *common zero set* is
\[
Z(A)=\{x\in S:\ f(x)=0\ \text{for all }f\in A\},
\]
so \(A\) vanishes nowhere exactly when \(Z(A)=\varnothing\). \(\bar A\) is the closure of \(A\) for \(\|\cdot\|\). For real functions, \(f\vee g=\max(f,g)\) and \(f\wedge g=\min(f,g)\), pointwise.

## 2. Spaces of bounded and continuous functions

**Proposition 2.1.** Let \(S\) be a set and \(X\) a topological space.

1. (*Completeness*) The bounded functions on \(S\) form a Banach space under \(\|\cdot\|\). The bounded continuous functions on \(X\) and the bounded Borel functions on \(X\) form closed subspaces of it. If \(X\) is compact, then \(C(X)=C_b(X)\).
2. (*Closures of algebras*) The closure of an algebra (or real algebra) of bounded functions is again one. The closure of a self-adjoint algebra is self-adjoint.
3. (*Vanishing at infinity*) \(C_c(X)\subseteq C_0(X)\subseteq C_b(X)\). \(C_0(X)\) is a closed self-adjoint subalgebra of \(C_b(X)\), hence a Banach space. \(C_c(X)\) is a self-adjoint subalgebra of \(C_0(X)\), and it is dense in \(C_0(X)\).

**Proof.** (1) Let \((f_n)\) be a Cauchy sequence. For each \(s\), \((f_n(s))\) is Cauchy in \(\mathbb C\); let \(f(s)\) be its limit. Given \(\varepsilon>0\), choose \(N\) with \(\|f_n-f_m\|\leq\varepsilon\) for \(m,n\geq N\). Letting \(m\to\infty\) gives \(|f_n(s)-f(s)|\leq\varepsilon\) for all \(s\) and all \(n\geq N\). So \(f\) is bounded and \(f_n\to f\). Suppose the \(f_n\) are continuous. Fix \(x\in X\), fix \(n\geq N\), and take an open \(U\ni x\) on which \(|f_n-f_n(x)|<\varepsilon\). On \(U\),
\(|f-f(x)|\leq|f-f_n|+|f_n-f_n(x)|+|f_n(x)-f(x)|<3\varepsilon\),
so \(f\) is continuous. Suppose the \(f_n\) are Borel. Then
\(\{\operatorname{Re}f>a\}=\bigcup_k\bigcup_N\bigcap_{n\geq N}\{\operatorname{Re}f_n>a+1/k\}\)
is a Borel set, and so is the analogous set for \(\operatorname{Im}f\); so \(f\) is Borel. The last claim is (K5) applied to \(|f|\).

(2) Let \(f_n\to f\) and \(g_n\to g\) with \(f_n,g_n\) in the algebra. Then \(\|f_n\|\leq\|f\|+\|f_n-f\|\) is bounded, and
\(\|f_ng_n-fg\|\leq\|f_n\|\,\|g_n-g\|+\|g\|\,\|f_n-f\|\to0\).
Sums, scalar multiples, complex conjugates and real values pass to uniform limits in the same way.

(3) If \(f\in C_c(X)\), then \(\{|f|\geq\varepsilon\}\) is a closed subset of the compact support, hence compact by (K1). If \(f\in C_0(X)\), then \(|f|<1\) off the compact set \(\{|f|\geq1\}\), and \(|f|\) is bounded on that set by (K5); so \(f\) is bounded. For \(f,g\in C_0(X)\), \(\varepsilon>0\) and a scalar \(c\neq0\),
\[
\{|f+g|\geq\varepsilon\}\subseteq\{|f|\geq\tfrac\varepsilon2\}\cup\{|g|\geq\tfrac\varepsilon2\},\quad
\{|fg|\geq\varepsilon\}\subseteq\{|f|\geq\tfrac{\varepsilon}{\|g\|+1}\},\quad
\{|cf|\geq\varepsilon\}=\{|f|\geq\tfrac{\varepsilon}{|c|}\}.
\]
The sets on the left are closed. The sets on the right are compact, since a finite union of compact sets is compact (K2). So the sets on the left are compact by (K1), and \(f+g,\ fg,\ cf\in C_0(X)\). Clearly \(\bar f\in C_0(X)\). If \(f_n\in C_0(X)\) and \(\|f_n-f\|\leq\varepsilon/2\), then \(\{|f|\geq\varepsilon\}\subseteq\{|f_n|\geq\varepsilon/2\}\). So \(C_0(X)\) is closed in \(C_b(X)\), and complete by (1). The supports of \(f+g\), \(fg\), \(cf\) and \(\bar f\) are closed subsets of \(\operatorname{supp}f\cup\operatorname{supp}g\), so \(C_c(X)\) is a self-adjoint subalgebra. For density, let \(f\in C_0(X)\) and \(\varepsilon>0\). Define \(\psi_\varepsilon:\mathbb C\to\mathbb C\) by \(\psi_\varepsilon(z)=0\) for \(|z|\leq\varepsilon\) and \(\psi_\varepsilon(z)=z-\varepsilon z/|z|\) for \(|z|\geq\varepsilon\). It is continuous, and \(|\psi_\varepsilon(z)-z|\leq\varepsilon\). So \(\psi_\varepsilon\circ f\) is continuous and within \(\varepsilon\) of \(f\). It is nonzero only on \(\{|f|>\varepsilon\}\), whose closure lies in the compact set \(\{|f|\geq\varepsilon\}\). So \(\psi_\varepsilon\circ f\in C_c(X)\). \(\square\)

## 3. The one-point compactification

**Definition 3.1** (One-point compactification). Let \(X\) be a topological space and \(\infty\) a point not in \(X\). Put \(X_\infty=X\cup\{\infty\}\). Let \(\tau_\infty\) consist of the open subsets of \(X\) together with the sets \(X_\infty\setminus C\), where \(C\subseteq X\) is closed and compact.

If \(X\) is Hausdorff, its compact subsets are closed by (K3), so the word "closed" can then be omitted. For a general space \(X\), it makes parts (1) and (2) below true.

**Proposition 3.2.**

1. \(\tau_\infty\) is a topology on \(X_\infty\). \(X\) is open in \(X_\infty\), and the subspace topology on \(X\) is its original topology.
2. \(X_\infty\) is compact.
3. If \(X\) is locally compact Hausdorff, then \(X_\infty\) is Hausdorff.
4. \(\infty\) is an isolated point of \(X_\infty\) exactly when \(X\) is compact. So \(X\) is dense in \(X_\infty\) exactly when \(X\) is not compact.
5. (*Uniqueness*) Let \(Y\) be compact Hausdorff, \(q\in Y\), and \(\varphi\) a homeomorphism of \(X\) onto \(Y\setminus\{q\}\). Extending \(\varphi\) by \(\infty\mapsto q\) gives a homeomorphism of \(X_\infty\) onto \(Y\).

**Proof.** (1) \(\varnothing\) is open in \(X\), and \(X_\infty=X_\infty\setminus\varnothing\). For open \(U\subseteq X\) and closed compact \(C,D\subseteq X\), the set \(U\cap(X_\infty\setminus C)=U\setminus C\) is open in \(X\), and \((X_\infty\setminus C)\cap(X_\infty\setminus D)=X_\infty\setminus(C\cup D)\) with \(C\cup D\) closed and compact. Consider a union of sets \(U_i\) open in \(X\) and sets \(X_\infty\setminus C_j\), with at least one \(j\). It equals \(X_\infty\setminus D\), where \(D=\bigcap_jC_j\cap\bigcap_i(X\setminus U_i)\). \(D\) is closed and lies in one \(C_j\), so it is compact by (K1). A union of open subsets of \(X\) is open in \(X\). The traces on \(X\) of the members of \(\tau_\infty\) are the sets \(U\) and \(X\setminus C\), all open in \(X\); so the subspace topology is the original one. Finally \(X\in\tau_\infty\).

(2) Let \(\mathcal W\) be an open cover of \(X_\infty\). Some \(W_0\in\mathcal W\) contains \(\infty\), so \(W_0=X_\infty\setminus C_0\) with \(C_0\) compact. The traces \(W\cap X\), \(W\in\mathcal W\), are open in \(X\) and cover \(C_0\), so finitely many of them do. Those members and \(W_0\) cover \(X_\infty\).

(3) Two points of \(X\) are separated by open subsets of \(X\), which are open in \(X_\infty\). Let \(x\in X\), with a compact neighbourhood \(N\) and an open \(V\) such that \(x\in V\subseteq N\). \(N\) is closed by (K3), so \(X_\infty\setminus N\) is an open neighbourhood of \(\infty\) disjoint from \(V\).

(4) If \(X\) is compact, then \(\{\infty\}=X_\infty\setminus X\) is open. If \(\{\infty\}\) is open, it is \(X_\infty\setminus C\) with \(C=X\), so \(X\) is compact. \(X\) is dense exactly when every open neighbourhood of \(\infty\) meets \(X\), that is, when \(\{\infty\}\) is not open.

(5) Call the extension \(\Phi\); it is a bijection. Let \(V\subseteq Y\) be open. If \(q\notin V\), then \(\Phi^{-1}(V)=\varphi^{-1}(V)\) is open in \(X\). If \(q\in V\), then \(Y\setminus V\) is compact by (K1) and lies in \(Y\setminus\{q\}\). So \(C=\varphi^{-1}(Y\setminus V)\) is compact by (K2), and closed in \(X\), since its complement is \(\varphi^{-1}(V\setminus\{q\})\). Then \(\Phi^{-1}(V)=X_\infty\setminus C\) is open. So \(\Phi\) is continuous, and by (K4) its inverse is continuous too. \(\square\)

**Examples 3.3.** (a) Let \(\mathbb T=\{w\in\mathbb C:|w|=1\}\). The Cayley map \(\kappa(x)=(x-i)/(x+i)\) is a homeomorphism of \(\mathbb R\) onto \(\mathbb T\setminus\{1\}\). Indeed \(|x-i|=|x+i|\) for real \(x\), \(\kappa(x)\neq1\), and the inverse is \(w\mapsto i(1+w)/(1-w)\), which is real on \(\mathbb T\setminus\{1\}\) because \((1+w)/(1-w)=(w-\bar w)/|1-w|^2\) there. \(\mathbb T\) is compact by [Lemma 4.1](#oa-fnd-sw-15)(b) below, so (5) gives \(\mathbb R_\infty\cong\mathbb T\) with \(\infty\mapsto1\). In the same way, \(y\mapsto(2y,|y|^2-1)/(|y|^2+1)\) is a homeomorphism of \(\mathbb R^n\) onto the unit sphere \(S^n\subseteq\mathbb R^{n+1}\) with the point \((0,\dots,0,1)\) removed; its inverse is \((u,t)\mapsto u/(1-t)\). So \((\mathbb R^n)_\infty\cong S^n\).

(b) If \(Y\) is compact Hausdorff and \(q\in Y\), then (5), applied to the identity map of \(Y\setminus\{q\}\), identifies \((Y\setminus\{q\})_\infty\) with \(Y\).

(c) \(\mathbb N_\infty\) is homeomorphic to \(Y=\{0\}\cup\{1/n:n\geq1\}\subseteq\mathbb R\), with \(\infty\mapsto0\). \(Y\) is compact, because an open set containing \(0\) contains all but finitely many of the points \(1/n\).

(d) If \(X\) is compact, \(X_\infty\) is \(X\) together with an isolated point, by (4). Then \(X\) is not dense in \(X_\infty\), so \(X_\infty\) is not a compactification of \(X\) in the usual sense, which asks for \(X\) to be dense.

The functions in \(C_0(X)\) are the continuous functions on \(X_\infty\) that vanish at \(\infty\), as the next proposition shows. For a function \(f\) on \(X\), let \(\tilde f\) be the function on \(X_\infty\) that equals \(f\) on \(X\) and \(0\) at \(\infty\). Put
\[
I_\infty=\{g\in C(X_\infty):\ g(\infty)=0\}.
\]

**Proposition 3.4.** Let \(X\) be any topological space.

1. \(f\in C_0(X)\) if and only if \(\tilde f\) is continuous on \(X_\infty\).
2. The map \(f\mapsto\tilde f\) is a bijection of \(C_0(X)\) onto \(I_\infty\) that preserves sums, scalar multiples, products, complex conjugation and the norm \(\|\cdot\|\). Its inverse is restriction to \(X\). It maps \(C_0(X;\mathbb R)\) onto the real functions in \(I_\infty\).
3. Every \(g\in C(X_\infty)\) has the unique form \(g=g(\infty)1+h\) with \(h\in I_\infty\). So \(C(X_\infty)\) is \(C_0(X)\) with a unit adjoined.

**Proof.** (1) Let \(f\in C_0(X)\). \(\tilde f\) is continuous at points of \(X\), because \(X\) is open in \(X_\infty\) and carries its own topology there ([Proposition 3.2](#oa-fnd-sw-02)(1)). At \(\infty\): given \(\varepsilon>0\), the set \(C=\{|f|\geq\varepsilon\}\) is compact, and closed because \(|f|\) is continuous. So \(X_\infty\setminus C\) is an open neighbourhood of \(\infty\) on which \(|\tilde f|<\varepsilon\). Conversely, let \(\tilde f\) be continuous. Then \(f\) is continuous, and for \(\varepsilon>0\) the set \(\{x\in X:|f(x)|\geq\varepsilon\}=\{t\in X_\infty:|\tilde f(t)|\geq\varepsilon\}\) is closed in the compact space \(X_\infty\). It is compact by (K1), and it lies in \(X\). Since \(X\) carries the subspace topology, it is compact in \(X\).

(2) The operations are pointwise, and \(0\) at \(\infty\) is preserved by all of them. \(\sup_{X_\infty}|\tilde f|=\sup_X|f|\). Restriction inverts the map by (1).

(3) Put \(h=g-g(\infty)1\). If also \(g=c1+h'\) with \(h'\in I_\infty\), evaluating at \(\infty\) gives \(c=g(\infty)\), so the form is unique. \(\square\)

Part (3) says that adjoining a unit to \(C_0(X)\) yields \(C(X_\infty)\).

## 4. Compact and locally compact spaces

**Lemma 4.1** (Compactness tools).

- (a) Every closed bounded interval \([a,b]\) is compact.
- (b) (*Tube lemma*) Let \(Y\) be compact, \(W\subseteq X\times Y\) open, and \(\{x_0\}\times Y\subseteq W\). Then \(U\times Y\subseteq W\) for some open \(U\ni x_0\). Consequently, a product of finitely many compact spaces is compact, and closed bounded subsets of \(\mathbb R^n\) are compact. Examples are \(\mathbb T\), the closed unit disc and the spheres \(S^n\).
- (c) A compact Hausdorff space is regular and normal: a point and a closed set not containing it, and two disjoint closed sets, have disjoint open neighbourhoods. Equivalently, if \(C\) is closed, \(O\) is open and \(C\subseteq O\), then some open \(G\) satisfies \(C\subseteq G\subseteq\overline G\subseteq O\).
- (d) In a compact metric space every sequence has a convergent subsequence, so the space is complete. It is separable and second countable, and every continuous map from it to a metric space is uniformly continuous. Conversely, a metric space in which every sequence has a convergent subsequence is compact.

**Proof.** (a) Let \(\mathcal O\) be an open cover, and let \(S\) be the set of \(s\in[a,b]\) such that finitely many members cover \([a,s]\). Then \(a\in S\). Let \(\sigma=\sup S\), and let \(O\in\mathcal O\) contain \(\sigma\), so that \(O\supseteq(\sigma-\eta,\sigma+\eta)\cap[a,b]\) for some \(\eta>0\). Some \(s\in S\) exceeds \(\sigma-\eta\). Adding \(O\) to a finite cover of \([a,s]\) covers \([a,\min(\sigma+\eta/2,b)]\). If \(\sigma<b\), this contradicts \(\sigma=\sup S\). So \(\sigma=b\), and \(b\in S\).

(b) For each \(y\in Y\) choose open sets \(U_y\ni x_0\) and \(V_y\ni y\) with \(U_y\times V_y\subseteq W\). Finitely many \(V_{y_j}\) cover \(Y\); put \(U=\bigcap_jU_{y_j}\). Now let \(X\) and \(Y\) be compact and \(\mathcal W\) an open cover of \(X\times Y\). Let \(\mathcal U\) be the family of open \(U\subseteq X\) such that finitely many members of \(\mathcal W\) cover \(U\times Y\). Each \(x\) lies in a member of \(\mathcal U\): the compact set \(\{x\}\times Y\) is covered by finitely many members, and the tube lemma applies to their union. Finitely many members of \(\mathcal U\) cover \(X\). Induction handles finite products. A closed bounded subset of \(\mathbb R^n\) lies in a box \([-M,M]^n\), which is compact by (a) and the product statement, so it is compact by (K1).

(c) Let \(p\notin C\) with \(C\) closed. \(C\) is compact by (K1), and (K3) separates \(p\) from \(C\). Let \(E,F\) be disjoint and closed. For each \(e\in E\), (K3) gives disjoint open sets \(U_e\ni e\) and \(V_e\supseteq F\). Finitely many \(U_e\) cover the compact set \(E\); take their union and the intersection of the corresponding \(V_e\). For the last form, separate \(C\) and \(X\setminus O\) by disjoint open sets \(G\supseteq C\) and \(H\supseteq X\setminus O\); then \(\overline G\subseteq X\setminus H\subseteq O\).

(d) Let \((x_j)\) be a sequence in a compact metric space \(K\) with no convergent subsequence. Then each \(p\in K\) has a ball containing \(x_j\) for only finitely many \(j\); otherwise indices \(j_1<j_2<\cdots\) with \(d(x_{j_i},p)<1/i\) could be chosen. Finitely many such balls cover \(K\), which is absurd. A Cauchy sequence with a convergent subsequence converges, so \(K\) is complete. For each \(n\), finitely many balls of radius \(1/n\) cover \(K\). Their centres, over all \(n\), form a countable dense set \(C\), and the balls \(B(c,1/m)\), \(c\in C\), \(m\geq1\), form a countable base: if \(B(x,2/m)\subseteq O\), some \(c\in C\) has \(d(c,x)<1/m\), and then \(x\in B(c,1/m)\subseteq O\). Conversely, let every sequence in a metric space \(M\) have a convergent subsequence, and let \(\mathcal O\) be an open cover. Some \(\delta>0\) has the property that every ball \(B(x,\delta)\) lies in a member of \(\mathcal O\). Otherwise there are balls \(B(x_n,1/n)\) lying in no member; a subsequence of the centres converges to some \(x\) in a member \(O\) with \(B(x,2r)\subseteq O\), and then \(B(x_n,1/n)\subseteq O\) for large \(n\) in the subsequence. Also finitely many balls \(B(x,\delta)\) cover \(M\). Otherwise points with mutual distances at least \(\delta\) can be chosen one after another, and they form a sequence with no convergent subsequence. So finitely many members of \(\mathcal O\) cover \(M\). Finally, let \(\phi\) be a continuous map from a compact metric space \(K\) to a metric space, and \(\varepsilon>0\). By the first part, every sequence in \(K\) has a convergent subsequence. So the argument above gives, for the open cover by the sets \(\{x:d(\phi(x),\phi(p))<\varepsilon/2\}\), \(p\in K\), a \(\delta>0\) such that every ball \(B(x,\delta)\) lies in one of them. If \(d(x,y)<\delta\), then \(x\) and \(y\) lie in one such set, so \(d(\phi(x),\phi(y))<\varepsilon\). \(\square\)

**Proposition 4.2** (Locally compact spaces).

1. (*Examples.*) The following are locally compact Hausdorff: compact Hausdorff spaces, \(\mathbb R^n\), discrete spaces, closed subspaces of LCH spaces, open subspaces of compact Hausdorff spaces, and open subspaces of LCH spaces. The spaces \(\mathbb Q\), \(\mathbb N^{\mathbb N}\) (a countable product of discrete copies of \(\mathbb N\)) and \(\mathbb R^{\mathbb N}\) (product topology) are Hausdorff, but no point in them has a compact neighbourhood.
2. (*Compact closures.*) Let \(X\) be LCH, \(A\subseteq X\) compact and \(V\) a neighbourhood of \(A\). Then some open \(U\supseteq A\) has compact closure contained in \(V\).
3. (*Exhaustion.*) If \(X\) is LCH and \(\sigma\)-compact, that is, a countable union of compact sets, then there are open sets \(U_1\subseteq U_2\subseteq\cdots\) with \(\overline{U_n}\) compact, \(\overline{U_n}\subseteq U_{n+1}\) and \(\bigcup_nU_n=X\). Every compact subset of \(X\) lies in some \(U_n\).
4. (*Countability at infinity.*) For LCH \(X\), the following are equivalent: (i) \(\infty\) has a countable neighbourhood base in \(X_\infty\); (ii) \(\{\infty\}\) is a countable intersection of open subsets of \(X_\infty\); (iii) \(X\) is \(\sigma\)-compact; (iv) \(X\) is Lindelöf, that is, every open cover has a countable subcover.
5. (*Variants of local compactness.*) For a topological space consider: (i) every point has a compact neighbourhood; (ii) every neighbourhood of a point contains a compact neighbourhood of that point; (iii) every point has an open neighbourhood with compact closure; (iii\(')\) every open neighbourhood \(V\) of a point \(p\) contains an open \(U\ni p\) with compact closure; (iv) every open neighbourhood \(V\) of \(p\) contains an open \(U\ni p\) with \(\overline U\) compact and \(\overline U\subseteq V\). Then (iv) implies (ii) and (iii); (ii) implies (i); and (iii) and (iii\(')\) are equivalent and imply (i). In a Hausdorff space all five are equivalent.

**Proof.** (1) A compact Hausdorff space is a compact neighbourhood of each of its points. In \(\mathbb R^n\) closed balls are compact by Lemma 4.1(b). In a discrete space, \(\{x\}\) is a compact neighbourhood of \(x\). If \(Y\subseteq X\) is closed and \(N\) is a compact neighbourhood of \(p\in Y\) in \(X\), then \(N\cap Y\) is a compact neighbourhood of \(p\) in \(Y\), by (K1). If \(U\) is open in a compact Hausdorff space and \(p\in U\), Lemma 4.1(c) gives an open \(V\ni p\) with \(\overline V\subseteq U\), and \(\overline V\) is compact by (K1). An open subspace of an LCH space \(X\) is open in \(X_\infty\), which is compact Hausdorff by [Proposition 3.2](#oa-fnd-sw-02)(2)–(3); so the previous case applies. Subspaces and products of Hausdorff spaces are Hausdorff.

For \(\mathbb Q\): suppose \(N\) is a compact neighbourhood of \(q\in\mathbb Q\). It contains \(\mathbb Q\cap(q-2r,q+2r)\) for some \(r>0\), so it contains \(P=\mathbb Q\cap[q-r,q+r]\), which is closed and hence compact by (K1). Pick an irrational \(\xi\in(q-r,q+r)\). The open sets \(\{t\in P:|t-\xi|>1/m\}\), \(m\geq1\), cover \(P\) with no finite subcover. For \(\mathbb N^{\mathbb N}\) and \(\mathbb R^{\mathbb N}\): a neighbourhood of a point contains a basic open set that leaves the coordinates beyond some index \(m\) free. The projection onto coordinate \(m+1\) is continuous, so it maps a compact neighbourhood onto a compact set (K2). Compact subsets of \(\mathbb N\) are finite and compact subsets of \(\mathbb R\) are bounded, but the image of the basic open set is all of \(\mathbb N\) or \(\mathbb R\).

(2) First let \(A=\{p\}\). The interior of \(V\) in \(X\) is open in \(X_\infty\), so \(F=X_\infty\setminus\operatorname{int}V\) is closed, and \(p\notin F\). \(X_\infty\) is compact Hausdorff ([Proposition 3.2](#oa-fnd-sw-02)(2)–(3)), so by Lemma 4.1(c) there is an open \(W\ni p\) whose closure in \(X_\infty\) misses \(F\), that is, lies in \(\operatorname{int}V\subseteq X\). Put \(U=W\cap X\). Its closure in \(X_\infty\) is compact by (K1) and lies in \(X\). So it is also the closure of \(U\) in \(X\), and it is compact in \(X\) and contained in \(V\). For general compact \(A\), take such a \(U_p\) for each \(p\in A\), a finite subcover \(U_{p_1},\dots,U_{p_k}\) of \(A\), and \(U=\bigcup_iU_{p_i}\). Then \(\overline U=\bigcup_i\overline{U_{p_i}}\) is compact and lies in \(V\).

(3) Let \(X=\bigcup_nK_n\) with each \(K_n\) compact. By (2), choose an open \(U_1\supseteq K_1\) with compact closure, and inductively an open \(U_{n+1}\) with compact closure that contains the compact set \(\overline{U_n}\cup K_{n+1}\). Then \(\overline{U_n}\subseteq U_{n+1}\) and \(\bigcup U_n=X\). A compact set is covered by the increasing open sets \(U_n\), so it lies in one of them.

(4) (i) \(\Rightarrow\) (ii): let \(W_1,W_2,\ldots\) form a neighbourhood base at \(\infty\). Their interiors are open, contain \(\infty\), and again form a neighbourhood base. The intersection of the interiors is \(\{\infty\}\), because \(X_\infty\) is Hausdorff ([Proposition 3.2](#oa-fnd-sw-02)(3)). (ii) \(\Rightarrow\) (iii): each open \(W_n\ni\infty\) has the form \(X_\infty\setminus C_n\) with \(C_n\) compact, and \(X=\bigcup C_n\). (iii) \(\Rightarrow\) (i): with \(U_n\) from (3), the sets \(X_\infty\setminus\overline{U_n}\) form a neighbourhood base at \(\infty\), because a neighbourhood \(X_\infty\setminus C\) of \(\infty\) contains \(X_\infty\setminus\overline{U_n}\) as soon as \(C\subseteq U_n\). (iii) \(\Rightarrow\) (iv): each \(K_n\) is covered by finitely many members of an open cover. (iv) \(\Rightarrow\) (iii): by (2) the open sets with compact closure cover \(X\); a countable subcover \((V_n)\) gives \(X=\bigcup_n\overline{V_n}\).

(5) (iv) \(\Rightarrow\) (iii), (iii\(')\) \(\Rightarrow\) (iii) and (ii) \(\Rightarrow\) (i): take \(V=X\). (iii) \(\Rightarrow\) (iii\(')\): if \(W\ni p\) is open with compact closure and \(V\ni p\) is open, then \(U=W\cap V\) has closure inside \(\overline W\), which is compact by (K1). (iii) \(\Rightarrow\) (i): \(\overline W\) is a compact neighbourhood. (iv) \(\Rightarrow\) (ii): \(\overline U\) is a compact neighbourhood of \(p\) inside \(V\), and every neighbourhood of \(p\) contains an open one. In a Hausdorff space, (i) says that the space is LCH, and then (2) gives (iv). \(\square\)

Without the Hausdorff property the conditions in (5) need not agree. For example, \(\mathbb Q_\infty\) is compact by [Proposition 3.2](#oa-fnd-sw-02)(2), so (i) holds at each of its points. But (ii) fails at every rational point \(q\). Indeed, \(\mathbb Q\) is an open neighbourhood of \(q\) in \(\mathbb Q_\infty\) that carries its own topology there ([Proposition 3.2](#oa-fnd-sw-02)(1)), so a compact neighbourhood of \(q\) inside \(\mathbb Q\) would be a compact neighbourhood of \(q\) in \(\mathbb Q\), and by (1) there is none. The open database [π-Base] collects many more examples of this kind, with the properties of each space ([spaces without compact neighbourhoods](https://topology.pi-base.org/properties/P000023)).

## 5. Urysohn's lemma and metrizability

**Theorem 5.1** (Urysohn's lemma). Let \(X\) be a space in which any two disjoint closed sets have disjoint open neighbourhoods, and let \(E,F\subseteq X\) be disjoint closed sets. Then there is a continuous \(f:X\to[0,1]\) with \(f=0\) on \(E\) and \(f=1\) on \(F\). By [Lemma 4.1](#oa-fnd-sw-15)(c), this applies to every compact Hausdorff space.

*Reference:* [Urysohn 1925].

**Proof.** By the argument at the end of the proof of [Lemma 4.1](#oa-fnd-sw-15)(c), which uses only the separation of disjoint closed sets, every closed set \(C\) inside an open set \(O\) has an open \(G\) with \(C\subseteq G\subseteq\overline G\subseteq O\). Let \(D\) be the set of dyadic rationals in \([0,1]\). We build open sets \(U_r\), \(r\in D\), with
\[
E\subseteq U_0,\qquad U_1=X\setminus F,\qquad\overline{U_r}\subseteq U_s\ \text{whenever }r<s .
\tag{5.1}
\]
Put \(U_1=X\setminus F\), and choose \(U_0\) open with \(E\subseteq U_0\subseteq\overline{U_0}\subseteq U_1\). Suppose \(U_r\) has been built for all \(r=j/2^n\), \(0\leq j\leq2^n\), with (5.1). For \(r=(2j+1)/2^{n+1}\), its neighbours \(r_-=j/2^n\) and \(r_+=(j+1)/2^n\) satisfy \(\overline{U_{r_-}}\subseteq U_{r_+}\); choose an open \(U_r\) with \(\overline{U_{r_-}}\subseteq U_r\subseteq\overline{U_r}\subseteq U_{r_+}\). For \(r<s\) at level \(n+1\), (5.1) follows by passing through the neighbours of \(r\) and \(s\) at level \(n\). Now define \(f(x)=\inf\{r\in D:x\in U_r\}\), with \(\inf\varnothing=1\). Then \(0\leq f\leq1\), \(f=0\) on \(E\), and \(f=1\) on \(F\), since \(F\) misses \(U_1\supseteq U_r\) for every \(r\). For \(0<\alpha\leq1\) and \(0\leq\beta<1\),
\[
\{f<\alpha\}=\bigcup_{r<\alpha}U_r,\qquad\{f>\beta\}=\bigcup_{s>\beta}\bigl(X\setminus\overline{U_s}\bigr),
\]
with \(r,s\in D\). For the first: if \(f(x)<\alpha\), some \(r<\alpha\) has \(x\in U_r\), and conversely \(x\in U_r\) gives \(f(x)\leq r\). For the second: if \(f(x)>\beta\), pick \(s,s'\in D\) with \(\beta<s<s'<f(x)\); then \(x\notin U_{s'}\supseteq\overline{U_s}\). Conversely, if \(x\notin\overline{U_s}\), then \(x\notin U_r\) for every \(r\leq s\), so \(f(x)\geq s\). For other values of \(\alpha\) and \(\beta\) the sets \(\{f<\alpha\}\) and \(\{f>\beta\}\) are \(\varnothing\) or \(X\). So all these sets are open, and \(f\) is continuous. \(\square\)

**Corollary 5.2** (Urysohn's lemma, locally compact form). Let \(X\) be LCH, \(A\subseteq X\) compact and \(B\subseteq X\) closed with \(A\cap B=\varnothing\). Then some \(f\in C_c(X)\) with \(0\leq f\leq1\) equals \(1\) on \(A\) and \(0\) on \(B\). In particular, \(X\) is completely regular (take \(A=\{p\}\)), and \(C_c(X)\), hence \(C_0(X)\), separates points and vanishes nowhere. [Theorem 10.1](#oa-fnd-sw-09) then gives a second proof that \(C_c(X)\) is dense in \(C_0(X)\).

**Proof.** By [Proposition 4.2](#oa-fnd-sw-15)(2) with \(V=X\setminus B\), choose an open \(U\supseteq A\) whose closure \(K\) is compact and lies in \(X\setminus B\). \(K\) is compact Hausdorff, so Urysohn's lemma gives a continuous \(g:K\to[0,1]\) with \(g=1\) on \(A\) and \(g=0\) on \(K\setminus U\). Put \(f=g\) on \(K\) and \(f=0\) on \(X\setminus K\); so \(f=0\) on \(X\setminus U\). For closed \(F\subseteq[0,1]\), \(f^{-1}(F)\) is \(g^{-1}(F)\) if \(0\notin F\), and \(g^{-1}(F)\cup(X\setminus U)\) if \(0\in F\). Both are closed in \(X\), since \(K\) is closed in \(X\). So \(f\) is continuous, its support lies in \(K\), and \(f=0\) on \(B\). \(\square\)

**Theorem 5.3** (Metrizability). For an LCH space \(X\), the following are equivalent.

- (i) \(X\) is \(\sigma\)-compact and metrizable.
- (ii) Some countable family \(\mathcal K\) of compact sets has this property: every neighbourhood of every point \(p\) contains a member of \(\mathcal K\) that is a neighbourhood of \(p\).
- (iii) \(X\) is second countable.
- (iv) \(X\) is Polish: separable and completely metrizable.
- (v) \(X_\infty\) is metrizable.

**Lemma 5.4.** A compact Hausdorff space \(K\) with a countable base is metrizable.

**Proof.** Let \((B_n)\) be a countable base. For each pair \((m,n)\) with \(\overline{B_m}\subseteq B_n\), Urysohn's lemma gives a continuous \(f_{mn}:K\to[0,1]\) that is \(1\) on \(\overline{B_m}\) and \(0\) off \(B_n\). List these functions as \(h_1,h_2,\ldots\), and put \(d(x,y)=\sum_k2^{-k}|h_k(x)-h_k(y)|\). Then \(d\) is symmetric, satisfies the triangle inequality, and \(y\mapsto d(x,y)\) is continuous, as a uniform limit of continuous functions. Let \(x\neq y\). Since \(\{y\}\) is closed, some \(B_n\) contains \(x\) but not \(y\). By [Lemma 4.1](#oa-fnd-sw-15)(c), there is an open \(V\ni x\) with \(\overline V\subseteq B_n\), and some \(B_m\) satisfies \(x\in B_m\subseteq V\). Then \(\overline{B_m}\subseteq B_n\) and \(f_{mn}(x)=1\neq0=f_{mn}(y)\), so \(d(x,y)>0\). So \(d\) is a metric. Its open balls are open in \(K\), so the identity map from \(K\) to \((K,d)\) is a continuous bijection onto a Hausdorff space, and a homeomorphism by (K4). \(\square\)

**Lemma 5.5.** Let \((M,d)\) be a complete metric space and \(O\subseteq M\) open. Then \(O\) is completely metrizable.

**Proof.** If \(O=M\) there is nothing to prove. Otherwise let \(F=M\setminus O\) and \(\phi(x)=1/d(x,F)\) for \(x\in O\); it is finite and continuous, since \(F\) is closed. Put \(d'(x,y)=d(x,y)+|\phi(x)-\phi(y)|\). This is a metric on \(O\), and it gives the same topology: \(d\leq d'\), and \(d'(x,y)\to0\) as \(y\to x\) in \(d\), by continuity of \(\phi\). Let \((x_j)\) be Cauchy for \(d'\). It is Cauchy for \(d\), so it converges to some \(y\in M\). The numbers \(\phi(x_j)\) form a Cauchy sequence, so they are bounded by some \(c\); then \(d(x_j,F)\geq1/c\), and \(d(y,F)\geq1/c>0\). So \(y\in O\), and \(d'(x_j,y)\to0\) by continuity of \(\phi\) at \(y\). \(\square\)

**Proof of Theorem 5.3.** (ii) \(\Rightarrow\) (iii): the interiors of the members of \(\mathcal K\) form a countable base.

(iii) \(\Rightarrow\) (ii): let \((B_n)\) be a countable base, and \(\mathcal K\) the family of those \(\overline{B_n}\) that are compact. Given \(p\) and a neighbourhood \(V\), [Proposition 4.2](#oa-fnd-sw-15)(2) gives an open \(U\ni p\) with compact closure inside \(V\). Choose \(B_n\) with \(p\in B_n\subseteq U\). Then \(\overline{B_n}\subseteq\overline U\) is compact, lies in \(V\), and is a neighbourhood of \(p\).

(iii) \(\Rightarrow\) (v): a second countable space is Lindelöf, because each member of an open cover is a union of base sets, and each base set that lies in some member can be assigned to one such member. So \(X\) is \(\sigma\)-compact by [Proposition 4.2](#oa-fnd-sw-15)(4), and \(\infty\) has a countable neighbourhood base \((W_n)\). Replacing each \(W_n\) by its interior, we may take the \(W_n\) open. The sets \(B_n\) and \(W_n\) together form a countable base of \(X_\infty\): an open \(O\ni\infty\) contains some \(W_m\), and each of its points in \(X\) lies in some \(B_n\subseteq O\cap X\). \(X_\infty\) is compact Hausdorff ([Proposition 3.2](#oa-fnd-sw-02)(2)–(3)), so Lemma 5.4 applies.

(v) \(\Rightarrow\) (i): \(X\) is a subspace of the metrizable space \(X_\infty\), so it is metrizable. \(X_\infty\) is compact metrizable, hence second countable by [Lemma 4.1](#oa-fnd-sw-15)(d). So \(\infty\) has a countable neighbourhood base, and \(X\) is \(\sigma\)-compact by [Proposition 4.2](#oa-fnd-sw-15)(4).

(i) \(\Rightarrow\) (iii): \(X=\bigcup K_n\) with each \(K_n\) a compact metric space, which is separable by [Lemma 4.1](#oa-fnd-sw-15)(d). So \(X\) has a countable dense set, and the balls of rational radius about its points form a countable base.

(v) \(\Rightarrow\) (iv): \(X_\infty\) is a compact metric space, hence complete and second countable ([Lemma 4.1](#oa-fnd-sw-15)(d)). \(X\) is open in \(X_\infty\), so it is completely metrizable by Lemma 5.5. It is second countable as a subspace, hence separable.

(iv) \(\Rightarrow\) (iii): as in (i) \(\Rightarrow\) (iii), the balls of rational radius about the points of a countable dense set form a countable base. \(\square\)

Because \(X_\infty\) is compact, the proof needs a metrization argument only for compact spaces (Lemma 5.4), not the general Urysohn metrization theorem for regular second countable spaces. An uncountable discrete space is metrizable and LCH but satisfies none of (i)–(v) ([Example 11.2](#oa-fnd-sw-13)).

## 6. The polynomial step: absolute values without constant terms

**Lemma 6.1.** Define real polynomials by
\[
P_0=0,\qquad P_{n+1}(t)=P_n(t)+\tfrac12\bigl(t^2-P_n(t)^2\bigr).
\tag{6.1}
\]

1. \(P_n(t)=Q_n(t^2)\) for real polynomials \(Q_n\) with \(Q_n(0)=0\).
2. For \(|t|\leq1\): \(0\leq P_n(t)\leq P_{n+1}(t)\leq|t|\), and
\[
0\leq|t|-P_n(t)\leq|t|\bigl(1-\tfrac{|t|}2\bigr)^n\leq\frac2n\qquad(n\geq1).
\tag{6.2}
\]

**Proof.** (1) Put \(Q_0=0\) and \(Q_{n+1}(s)=Q_n(s)+\frac12(s-Q_n(s)^2)\). By induction \(P_n(t)=Q_n(t^2)\), and \(Q_{n+1}(0)=Q_n(0)-\frac12Q_n(0)^2=0\).

(2) Fix \(t\) and write \(a=|t|\in[0,1]\) and \(p_n=P_n(t)\). Since \(t^2=a^2\), (6.1) gives
\[
a-p_{n+1}=(a-p_n)\Bigl(1-\frac{a+p_n}2\Bigr).
\]
Suppose \(0\leq p_n\leq a\). Then \(0\leq\frac{a+p_n}2\leq a\leq1\), so \(0\leq a-p_{n+1}\leq a-p_n\); that is, \(p_n\leq p_{n+1}\leq a\). Since \(p_0=0\), induction gives \(0\leq p_n\leq p_{n+1}\leq a\) for all \(n\). Using \(p_n\geq0\), the second factor above is at most \(1-a/2\), so \(a-p_n\leq a(1-a/2)^n\). For the last bound, let \(0<a\leq1\) and \(s=a/2\leq\frac12\). By Bernoulli's inequality \((1+u)^n\geq1+nu\) (\(u\geq0\)),
\[
(1-s)^{-n}=\Bigl(1+\frac{s}{1-s}\Bigr)^n\geq1+\frac{ns}{1-s}\geq1+ns ,
\]
so \(a(1-a/2)^n\leq a/(1+na/2)=2a/(2+na)<2/n\). \(\square\)

**Proposition 6.2.** Let \(A\) be a real algebra of bounded real functions on a set \(S\).

1. If \(p\) is a real polynomial with \(p(0)=0\) and \(f\in A\), then \(p\circ f\in A\). If such polynomials \(p_k\) converge uniformly to a function \(\varphi\) on an interval containing \(f(S)\), then \(\varphi\circ f\in\bar A\).
2. Let \(f\in A\) and \(r>0\) with \(\|f\|\leq r\). Then \(g_n=r\,Q_n(f^2/r^2)\) lies in \(A\), and \(0\leq|f|-g_n\leq2r/n\). The polynomials \(t\mapsto mP_n(t/m)\) have no constant term and converge to \(|t|\) uniformly on \([-m,m]\).
3. \(\bar A\) is a real algebra, and \(f,g\in\bar A\) imply \(|f|,\ f\vee g,\ f\wedge g\in\bar A\). So \(\bar A\) is closed under maxima and minima of finitely many elements.

**Proof.** (1) If \(p(t)=\sum_{k=1}^da_kt^k\), then \(p\circ f=\sum_{k=1}^da_kf^k\in A\), since \(A\) is closed under products and real linear combinations. No constant term is needed, so no unit is needed. Also \(\|p_k\circ f-\varphi\circ f\|\) is at most the supremum of \(|p_k-\varphi|\) on the interval.

(2) \(g_n\) is a real combination of powers \(f^{2k}\) with \(k\geq1\), so it lies in \(A\). By Lemma 6.1 applied to \(t=f(s)/r\), \(r\,P_n(f/r)=g_n\) satisfies \(0\leq|f|-g_n\leq2r/n\). The statement about \([-m,m]\) is (6.2) after the substitution \(t\mapsto t/m\).

(3) \(\bar A\) is a real algebra by [Proposition 2.1](#oa-fnd-sw-01)(2). Apply (2) to \(f\in\bar A\): \(|f|\) is a uniform limit of elements of \(\bar A\), so \(|f|\in\bar A\). Then \(f\vee g=\frac12(f+g+|f-g|)\) and \(f\wedge g=\frac12(f+g-|f-g|)\), and induction handles finitely many functions. \(\square\)

The recursion (6.1) keeps the constant term zero at every step. So the approximation of \(|f|\) uses neither the constant function \(1\) nor the Weierstrass approximation theorem, and this is what the nonunital theorem needs.

## 7. Interpolation at two points

**Lemma 7.1.** Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\), and let \(A\) be an algebra of \(\mathbb F\)-valued functions on a set \(S\) that separates points.

1. \(Z(A)\) has at most one point.
2. Let \(x,y\in S\) and \(a,b\in\mathbb F\). Assume \(a=0\) if \(x\in Z(A)\), \(b=0\) if \(y\in Z(A)\), and \(a=b\) if \(x=y\). Then some \(h\in A\) has \(h(x)=a\) and \(h(y)=b\).

**Proof.** First let \(x=y\). If \(x\in Z(A)\), take \(h=0\). Otherwise pick \(u\in A\) with \(u(x)\neq0\) and put \(h=(a/u(x))u\).

Now let \(x\neq y\). The set
\[
V=\{(h(x),h(y)):\ h\in A\}\subseteq\mathbb F^2
\]
is a linear subspace that is closed under coordinatewise multiplication, because \(h\mapsto(h(x),h(y))\) respects sums, scalars and products. Such a subspace is one of \(\{0\}\), \(\mathbb F(1,0)\), \(\mathbb F(0,1)\), \(\mathbb F(1,1)\) and \(\mathbb F^2\). Indeed, if \(V=\mathbb Fv\) with \(v=(v_1,v_2)\neq0\), then \((v_1^2,v_2^2)=c\,v\) for some \(c\). If \(v_1\neq0\neq v_2\), this forces \(v_1=c=v_2\), so \(V=\mathbb F(1,1)\). If \(v_1=0\) or \(v_2=0\), then \(V\) is \(\mathbb F(0,1)\) or \(\mathbb F(1,0)\).

Separation of \(x\) and \(y\) rules out \(\{0\}\) and \(\mathbb F(1,1)\), which would give \(h(x)=h(y)\) for every \(h\). If \(V=\mathbb F(0,1)\), every \(h\) vanishes at \(x\), so \(x\in Z(A)\), \(a=0\), and \((a,b)\in V\). The case \(V=\mathbb F(1,0)\) is symmetric. If \(V=\mathbb F^2\) there is nothing to prove. This proves (2). If \(x\neq y\) both lay in \(Z(A)\), then \(V=\{0\}\); so (1) holds. \(\square\)

When \(A\) vanishes nowhere, (2) says that every pair of values is attained at every pair of distinct points. The proof looks only at the image of \(A\) in \(\mathbb F^2\). It also shows what happens at the one possible common zero, which the nonunital case needs.

## 8. Stone's lattice lemma

**Lemma 8.1** (Stone's lattice lemma, pointwise form). Let \(K\) be a nonempty compact space and \(L\subseteq C(K;\mathbb R)\) a set that is closed under \(\vee\) and \(\wedge\). Let \(f\in C(K;\mathbb R)\) and \(\varepsilon>0\). Suppose that for all \(x,y\in K\) some \(h\in L\) satisfies
\[
|h(x)-f(x)|<\varepsilon\quad\text{and}\quad|h(y)-f(y)|<\varepsilon .
\tag{8.1}
\]
Then some \(h\in L\) satisfies \(\|h-f\|<\varepsilon\).

**Proof.** *Step 1: approximation from above, anchored at one point.* Fix \(x\in K\). Let \(\mathcal U_x\) be the family of open sets \(U\subseteq K\) for which some \(h\in L\) satisfies \(h(x)>f(x)-\varepsilon\) and \(h<f+\varepsilon\) on \(U\). Every \(y\in K\) lies in a member of \(\mathcal U_x\): take \(h\) from (8.1) for the pair \((x,y)\) and \(U=\{h<f+\varepsilon\}\). Choose a finite subcover \(U_1,\dots,U_m\) and, for each \(U_j\), one function \(h_j\) as in the definition. Put \(g_x=h_1\wedge\dots\wedge h_m\in L\). Each point of \(K\) lies in some \(U_j\), where \(g_x\leq h_j<f+\varepsilon\). So \(g_x<f+\varepsilon\) on \(K\), and \(g_x(x)>f(x)-\varepsilon\).

*Step 2: approximation from below.* Let \(\mathcal V\) be the family of open sets \(V\subseteq K\) for which some \(g\in L\) satisfies \(g<f+\varepsilon\) on \(K\) and \(g>f-\varepsilon\) on \(V\). By Step 1, every \(x\) lies in the member \(\{g_x>f-\varepsilon\}\) of \(\mathcal V\). Choose a finite subcover \(V_1,\dots,V_n\), one function \(g_i\) for each \(V_i\), and put \(h=g_1\vee\dots\vee g_n\in L\). Then \(h<f+\varepsilon\) everywhere, because every \(g_i\) is, and \(h>f-\varepsilon\) everywhere, because every point lies in some \(V_i\), where \(h\geq g_i>f-\varepsilon\). By (K5) the continuous function \(|h-f|\) attains its maximum, so \(\|h-f\|<\varepsilon\). \(\square\)

The proof makes only finitely many choices at each step. The covers are families of open sets defined by the existence of suitable functions, and no function is chosen for each point of \(K\). So the argument does not use the axiom of choice.

**Theorem 8.2** (Lattice versions). Let \(K\) be a compact space and \(L\subseteq C(K;\mathbb R)\) a linear subspace closed under \(\wedge\) (then also under \(\vee\), since \(f\vee g=-((-f)\wedge(-g))\)).

1. Suppose that (i) for \(x\neq y\) in \(K\) and \(a,b\in\mathbb R\), some \(h\in L\) has \(h(x)=a\) and \(h(y)=b\), and (ii) for \(x\in K\) and \(a\in\mathbb R\), some \(h\in L\) has \(h(x)=a\). Then \(L\) is dense in \(C(K;\mathbb R)\). If \(K\) has at least two points, (i) implies (ii).
2. If \(L\) separates points and every constant function lies in \(L\), then (i) and (ii) hold, so \(L\) is dense.
3. Let \(Y\subseteq C(K)\) be a complex linear subspace with \(1\in Y\) that separates points and satisfies \(\bar g\in Y\) and \(|g|\in Y\) for every \(g\in Y\). Then \(Y\) is dense in \(C(K)\).
4. (*Nonunital form*) Let \(X\) be a topological space and \(L\subseteq C_0(X;\mathbb R)\) a linear subspace closed under \(\wedge\). If (i) and (ii) hold for points of \(X\), then \(L\) is dense in \(C_0(X;\mathbb R)\). If \(X\) is locally compact Hausdorff, the converse also holds.

*Reference:* [Blackadar, XX.10.2.14] assumes only condition (i) in (1). That version fails on a one-point space, where \(L=\{0\}\) satisfies (i) vacuously and is not dense.

**Proof.** (1) If \(K=\varnothing\) there is nothing to prove. Otherwise, given \(f\) and \(x,y\), conditions (i)–(ii) give \(h\in L\) with \(h(x)=f(x)\) and \(h(y)=f(y)\), and Lemma 8.1 applies. If \(K\) has a second point \(y\neq x\), then (i) with the pair \((x,y)\) gives (ii).

(2) For \(x\neq y\) pick \(f\in L\) with \(f(x)\neq f(y)\). The vectors \((1,1)\) and \((f(x),f(y))\) in \(\mathbb R^2\) are linearly independent, and both lie in the image of the linear map \(h\mapsto(h(x),h(y))\). So the image is \(\mathbb R^2\), which is (i). Constants give (ii).

(3) For \(g\in Y\), \(\operatorname{Re}g=\frac12(g+\bar g)\) and \(\operatorname{Im}g=\frac1{2i}(g-\bar g)\) lie in \(Y\). Let \(Y_{\mathbb R}\) be the real functions in \(Y\). It is a real subspace that contains \(1\) and separates points, since \(g(x)\neq g(y)\) forces a difference in the real or the imaginary part. It is closed under \(|\cdot|\), hence under \(\wedge\), because \(f\wedge g=\frac12(f+g-|f-g|)\) ([Proposition 6.2](#oa-fnd-sw-04)(3)). By (2), \(Y_{\mathbb R}\) is dense in \(C(K;\mathbb R)\). Approximating the real and imaginary parts of \(f\in C(K)\) gives density of \(Y\).

(4) Suppose (i) and (ii) hold. The set \(\tilde L=\{\tilde h:h\in L\}\subseteq C(X_\infty;\mathbb R)\) of [Proposition 3.4](#oa-fnd-sw-03) is closed under \(\vee\) and \(\wedge\), since these operations keep the value \(0\) at \(\infty\). Let \(f\in C_0(X;\mathbb R)\). For a pair of points of \(X\), (i)–(ii) give an \(h\) that agrees with \(f\) there. For a pair \((x,\infty)\), (ii) gives \(h\) with \(h(x)=f(x)\), and \(\tilde h(\infty)=0=\tilde f(\infty)\). For the pair \((\infty,\infty)\), take \(h=0\). Lemma 8.1, applied on the compact space \(X_\infty\) ([Proposition 3.2](#oa-fnd-sw-02)(2)), puts \(\tilde f\) in the closure of \(\tilde L\). Since \(h\mapsto\tilde h\) preserves the norm ([Proposition 3.4](#oa-fnd-sw-03)(2)), \(f\) lies in the closure of \(L\). Conversely, let \(X\) be locally compact Hausdorff and \(L\) dense. For \(x\neq y\), the evaluation \(h\mapsto(h(x),h(y))\) is continuous, and it maps \(C_0(X;\mathbb R)\) onto \(\mathbb R^2\) by Urysohn's lemma ([Corollary 5.2](#oa-fnd-sw-16)). So it maps \(L\) onto a dense linear subspace of \(\mathbb R^2\), which is all of \(\mathbb R^2\). The one-point case is the same. Without local compactness the converse fails: for \(X=\mathbb Q\) one has \(C_0(X)=\{0\}\) ([Proposition 12.1](#oa-fnd-sw-10)), so \(L=\{0\}\) is dense while (ii) fails. \(\square\)

Lemma 8.1 needs the interpolation (8.1) only for the one function \(f\) that is being approximated, not for all target values. Part (4) of Theorem 8.2 is the lattice counterpart of [Theorem 9.2](#oa-fnd-sw-08).

## 9. The real Stone–Weierstrass theorem

**Theorem 9.1** (Stone–Weierstrass theorem, real form). Let \(K\) be a compact space and \(A\subseteq C(K;\mathbb R)\) a real algebra that separates points. Then \(Z(A)\) has at most one point, and
\[
\bar A=\{f\in C(K;\mathbb R):\ f=0\ \text{on }Z(A)\}.
\tag{9.1}
\]
In particular:

- (a) if \(A\) vanishes nowhere, for example if \(A\) contains the constant functions, then \(A\) is dense in \(C(K;\mathbb R)\);
- (b) if every function in \(A\) vanishes at a point \(z\), then \(\bar A=\{f:\ f(z)=0\}\).

*Reference:* [Stone 1937].

**Proof.** \(Z(A)\) has at most one point by [Lemma 7.1](#oa-fnd-sw-05)(1). Evaluation at a point is continuous for \(\|\cdot\|\), so \(\bar A\) lies in the right side of (9.1). Conversely, let \(f\in C(K;\mathbb R)\) vanish on \(Z(A)\), and assume \(K\neq\varnothing\) (otherwise both sides are \(\{0\}\)). Put \(B=\bar A\). By [Proposition 6.2](#oa-fnd-sw-04)(3), \(B\) is closed under \(\vee\) and \(\wedge\). For \(x,y\in K\), apply [Lemma 7.1](#oa-fnd-sw-05)(2) to \(A\) with \(a=f(x)\) and \(b=f(y)\). Its conditions hold, because \(f(x)=0\) whenever \(x\in Z(A)\), and likewise for \(y\). So some \(h\in A\subseteq B\) agrees with \(f\) at \(x\) and \(y\). [Lemma 8.1](#oa-fnd-sw-06) gives, for each \(\varepsilon>0\), an \(h\in B\) with \(\|h-f\|<\varepsilon\). So \(f\in\bar B=B\). \(\square\)

*Where the hypotheses enter.* Products are used in [Proposition 6.2](#oa-fnd-sw-04) (the functions \(g_n\)) and in [Lemma 7.1](#oa-fnd-sw-05) (the set \(V\) is closed under products). Separation is used in [Lemma 7.1](#oa-fnd-sw-05), to rule out \(V=\{0\}\) and \(V=\mathbb R(1,1)\). Compactness is used in [Lemma 8.1](#oa-fnd-sw-06), for the two finite subcovers, and in (K5). The Hausdorff property is not used. It follows anyway from separation: if \(h(x)\neq h(y)\), the sets \(\{|h-h(x)|<r\}\) and \(\{|h-h(y)|<r\}\) with \(r=|h(x)-h(y)|/2\) are disjoint open neighbourhoods.

For a closed algebra \(A\) that separates points, (9.1) gives a dichotomy: either \(A=C(K;\mathbb R)\), or \(A\) consists of all the functions that vanish at one point. [Exercise 2](#exercises) proves the case with a common zero in another way, by adjoining the constants.

The passage to \(C_0(X)\) goes through the one-point compactification.

**Theorem 9.2** (Real form for \(C_0(X)\)). Let \(X\) be locally compact Hausdorff, and let \(A\subseteq C_0(X;\mathbb R)\) be a real algebra that separates the points of \(X\) and vanishes nowhere. Then \(A\) is dense in \(C_0(X;\mathbb R)\).

**Proof.** By [Proposition 3.4](#oa-fnd-sw-03), \(\tilde A=\{\tilde f:f\in A\}\) is a real algebra of continuous functions on the compact space \(X_\infty\) ([Proposition 3.2](#oa-fnd-sw-02)(2)). It separates the points of \(X_\infty\). Two points of \(X\) are separated by \(A\). A point \(x\in X\) and \(\infty\) are separated by any \(f\in A\) with \(f(x)\neq0\), since \(\tilde f(\infty)=0\); such an \(f\) exists because \(A\) vanishes nowhere. The same fact gives \(Z(\tilde A)=\{\infty\}\). By [Theorem 9.1](#oa-fnd-sw-07)(b), the closure of \(\tilde A\) is the set of real functions in \(I_\infty\). Since \(f\mapsto\tilde f\) is an isometric bijection of \(C_0(X;\mathbb R)\) onto that set ([Proposition 3.4](#oa-fnd-sw-03)(2)), \(A\) is dense in \(C_0(X;\mathbb R)\). \(\square\)

The proof uses neither local compactness nor the Hausdorff property of \(X\). [Proposition 12.1](#oa-fnd-sw-10) explains why: both follow from the hypotheses on \(A\).

## 10. The complex Stone–Weierstrass theorem

**Theorem 10.1** (Stone–Weierstrass theorem for \(C_0(X)\)). Let \(X\) be locally compact Hausdorff, and let \(A\subseteq C_0(X)\) be a complex subalgebra that is self-adjoint, separates the points of \(X\), and vanishes nowhere. Then
\[
\bar A=C_0(X):
\tag{10.1}
\]
every \(f\in C_0(X)\) can be approximated uniformly on \(X\) by elements of \(A\).

*Compact form.* Let \(K\) be a compact space and \(A\subseteq C(K)\) a self-adjoint subalgebra that separates points. Then \(Z(A)\) has at most one point, and \(\bar A=\{f\in C(K):\ f=0\ \text{on }Z(A)\}\). In particular \(A\) is dense in \(C(K)\) if it vanishes nowhere, for example if it contains the constants.

**Proof.** Let \(A_{\mathbb R}\) be the set of real functions in \(A\). For \(f\in A\), self-adjointness and complex linearity give
\[
\operatorname{Re}f=\tfrac12(f+\bar f)\in A_{\mathbb R},\qquad\operatorname{Im}f=\tfrac1{2i}(f-\bar f)\in A_{\mathbb R}.
\]
\(A_{\mathbb R}\) is a real algebra. It separates points: if \(f(x)\neq f(y)\), then \(\operatorname{Re}f\) or \(\operatorname{Im}f\) takes different values at \(x\) and \(y\). For the same reason \(Z(A_{\mathbb R})=Z(A)\). In the setting of the theorem, [Theorem 9.2](#oa-fnd-sw-08) shows that \(A_{\mathbb R}\) is dense in \(C_0(X;\mathbb R)\). Let \(f\in C_0(X)\) and \(\varepsilon>0\). Since \(|\operatorname{Re}f|\leq|f|\) and \(|\operatorname{Im}f|\leq|f|\), for every \(\delta>0\) the sets \(\{|\operatorname{Re}f|\geq\delta\}\) and \(\{|\operatorname{Im}f|\geq\delta\}\) are closed subsets of the compact set \(\{|f|\geq\delta\}\), hence compact by (K1). So both parts lie in \(C_0(X;\mathbb R)\). Choose \(u,v\in A_{\mathbb R}\) within \(\varepsilon/2\) of them. Then \(u+iv\in A\) and \(\|f-(u+iv)\|<\varepsilon\). In the compact form, [Theorem 9.1](#oa-fnd-sw-07) applies to \(A_{\mathbb R}\) in the same way: a function \(f\) vanishing on \(Z(A)\) has real and imaginary parts vanishing on \(Z(A_{\mathbb R})\). \(\square\)

*Where each hypothesis is used.*

- *Subalgebra.* Closure under products enters in [Proposition 6.2](#oa-fnd-sw-04) and [Lemma 7.1](#oa-fnd-sw-05). Complex linearity gives \(\operatorname{Re}f,\operatorname{Im}f\in A\) and \(u+iv\in A\). [Example 12.2](#oa-fnd-sw-11)(d) shows that products cannot be dropped.
- *Self-adjoint.* Used once, to put \(\operatorname{Re}f\) and \(\operatorname{Im}f\) into \(A\). [Example 12.2](#oa-fnd-sw-11)(a) and Exercise 1 show that it cannot be dropped.
- *Separates points.* Used in [Lemma 7.1](#oa-fnd-sw-05), for pairs of points of \(X\). [Example 12.2](#oa-fnd-sw-11)(b) shows that it cannot be dropped.
- *Vanishes nowhere.* Used in [Theorem 9.2](#oa-fnd-sw-08), to separate each \(x\in X\) from \(\infty\) and to make \(\infty\) the only common zero on \(X_\infty\). [Example 12.2](#oa-fnd-sw-11)(c) shows that it cannot be dropped.
- *\(A\subseteq C_0(X)\).* Makes the functions \(\tilde f\) continuous on \(X_\infty\) ([Proposition 3.4](#oa-fnd-sw-03)).
- *Locally compact Hausdorff.* Not used in the proof. It is the natural setting because the other hypotheses force it ([Proposition 12.1](#oa-fnd-sw-10)).
- *Compactness of \(X_\infty\).* This is where the topology does its work, in the finite subcovers of [Lemma 8.1](#oa-fnd-sw-06).

*No countability is needed.* The proof uses no sequences of points and no countable bases, only finite subcovers. So the theorem applies to spaces that are neither \(\sigma\)-compact nor metrizable, such as uncountable discrete spaces ([Example 11.2](#oa-fnd-sw-13)) and locally compact groups of this kind.

## 11. Worked examples

Several examples here and in Section 12 use two functions on \(\mathbb R\):
\[
\varphi(x)=\frac1{1+x^2},\qquad\psi(x)=\frac{x}{1+x^2}.
\]
Both lie in \(C_0(\mathbb R)\): since \(|\psi(x)|\leq(1+x^2)^{-1/2}\), the sets \(\{|\varphi|\geq\varepsilon\}\) and \(\{|\psi|\geq\varepsilon\}\) are closed and lie in \(\{1+x^2\leq\varepsilon^{-2}\}\), so they are compact ([Lemma 4.1](#oa-fnd-sw-15)(a)). Also \(\varphi>0\), \(\varphi\) is even, \(\psi\) is odd, and \(\psi/\varphi=x\).

**Example 11.1** (A compact space without the constants). On \([0,1]\), let \(A=\{p(x+1):\ p\text{ a real polynomial},\ p(0)=0\}\). \(A\) is a real algebra. It vanishes nowhere, because \(x+1\geq1\), and \(x+1\) separates points. So \(A\) is dense in \(C([0,1];\mathbb R)\) by [Theorem 9.1](#oa-fnd-sw-07)(a). Yet \(1\notin A\): if \(p(0)=0\) and \(p(y)=1\) for \(y\in[1,2]\), the polynomial \(p-1\) would have infinitely many roots and constant term \(-1\). An explicit approximation is \(e_n(x)=1-\bigl(1-\frac{x+1}2\bigr)^n\in A\); since \(0\leq1-\frac{x+1}2\leq\frac12\) on \([0,1]\), \(|1-e_n|\leq2^{-n}\). On a compact space, "vanishes nowhere" is strictly weaker than "contains the constants".

**Example 11.2** (An uncountable discrete space). Let \(X\) be an uncountable set with the discrete topology. Its compact subsets are finite, because an infinite subset has an open cover by singletons with no finite subcover. So \(C_0(X)\) consists of the \(f\) for which \(\{|f|\geq\varepsilon\}\) is finite for every \(\varepsilon>0\). The finitely supported functions form a self-adjoint subalgebra that separates points and vanishes nowhere (it contains the indicator of each point), so it is dense. Here \(X\) is not \(\sigma\)-compact, and \(\infty\) has no countable neighbourhood base in \(X_\infty\) ([Proposition 4.2](#oa-fnd-sw-15)(4)). The proof of [Theorem 10.1](#oa-fnd-sw-09) never uses countability, so this does not matter.

**Example 11.3** (Degenerate spaces). If \(X=\varnothing\), then \(C_0(X)=\{0\}\), and \(A=\{0\}\) satisfies all hypotheses vacuously; the conclusion holds. If \(X\) is one point, \(C_0(X)=\mathbb C\); an algebra that vanishes nowhere contains a nonzero constant, hence equals \(\mathbb C\).

**Example 11.4** (Compact \(X\)). If \(X\) is compact, then \(C_0(X)=C(X)\), because \(\{|f|\geq\varepsilon\}\) is closed in \(X\) and so compact by (K1). The point \(\infty\) is isolated in \(X_\infty\) ([Proposition 3.2](#oa-fnd-sw-02)(4)), and [Theorem 10.1](#oa-fnd-sw-09) reduces to its compact form.

**Example 11.5** (The real line). The complex algebra generated by \(\varphi\) and \(\psi\) consists of the complex polynomials without constant term in \(\varphi\) and \(\psi\). It is self-adjoint, because \(\varphi\) and \(\psi\) are real. It separates points, because \(\psi/\varphi=x\), and it vanishes nowhere, because \(\varphi>0\). So it is dense in \(C_0(\mathbb R)\).

**Example 11.6** (One common zero, seen twice). On \([0,1]\), the complex polynomials without constant term have closure \(\{f\in C([0,1]):f(0)=0\}\), by the compact form of [Theorem 10.1](#oa-fnd-sw-09); for real coefficients this is [Theorem 9.1](#oa-fnd-sw-07)(b). Restricted to \(X=(0,1]\) they form a self-adjoint subalgebra of \(C_0(X)\) that separates points and vanishes nowhere, so [Theorem 10.1](#oa-fnd-sw-09) makes them dense in \(C_0((0,1])\). The two statements agree: by [Proposition 3.2](#oa-fnd-sw-02)(5) with \(Y=[0,1]\) and \(q=0\), and by [Proposition 3.4](#oa-fnd-sw-03), \(C_0((0,1])\) is the space of continuous functions on \([0,1]\) that vanish at \(0\).

## 12. The role of each hypothesis

The topological hypothesis of Theorem 10.1 comes for free, and each hypothesis on the algebra is needed.

**Proposition 12.1** (The topological hypotheses are automatic). Let \(X\) be a topological space.

1. If some set of functions in \(C_0(X)\) separates the points of \(X\), then \(X\) is Hausdorff.
2. If \(f\in C_0(X)\) and \(f(x)\neq0\), then \(x\) has a compact neighbourhood. So if some \(A\subseteq C_0(X)\) vanishes nowhere, every point of \(X\) has a compact neighbourhood. If no point of \(X\) has a compact neighbourhood, then \(C_0(X)=\{0\}\); this is the case for \(X=\mathbb Q\) ([Proposition 4.2](#oa-fnd-sw-15)(1)).
3. Consequently [Theorem 9.2](#oa-fnd-sw-08) and [Theorem 10.1](#oa-fnd-sw-09) hold for every topological space \(X\): whenever their hypotheses on \(A\) hold, \(X\) is locally compact Hausdorff.

**Proof.** (1) If \(h(x)\neq h(y)\), put \(r=|h(x)-h(y)|/2\). The open sets \(\{|h-h(x)|<r\}\) and \(\{|h-h(y)|<r\}\) are disjoint and contain \(x\) and \(y\).

(2) Put \(c=|f(x)|/2>0\). The set \(\{|f|\geq c\}\) is compact by (1.1), and it contains the open set \(\{|f|>c\}\), which contains \(x\).

(3) By (1) and (2), \(X\) is Hausdorff and every point has a compact neighbourhood. \(\square\)

Part (2) gives condition (i) of [Proposition 4.2](#oa-fnd-sw-15)(5), one of several conditions that serve as definitions of local compactness for spaces that need not be Hausdorff. Together with the Hausdorff property from (1), all of them agree. So nothing is lost by assuming that \(X\) is locally compact Hausdorff. Conversely, on every locally compact Hausdorff space the algebra \(C_0(X)\) itself separates points and vanishes nowhere, by Urysohn's lemma ([Corollary 5.2](#oa-fnd-sw-16)).

**Examples 12.2.** In examples (a)–(d), all hypotheses of [Theorem 10.1](#oa-fnd-sw-09) hold except one, and the conclusion fails. Examples (e)–(h) test the lattice versions, the hypothesis \(A\subseteq C_0(X)\), the topological hypothesis, and the form of the conclusion. Several of them use the functions \(\varphi\) and \(\psi\) of [Section 11](#oa-fnd-sw-13).

**(a) Self-adjointness.** Let \(\mathbb T=\{w\in\mathbb C:|w|=1\}\), a compact space ([Lemma 4.1](#oa-fnd-sw-15)(b)), and let \(A\) be the complex polynomials in the coordinate \(w\), restricted to \(\mathbb T\). \(A\) is a subalgebra. It contains \(1\), so it vanishes nowhere, and \(w\) separates points. But \(\bar w\notin\bar A\). To see this, fix \(N\geq2\) and let \(\omega=E(2\pi i/N)\), where \(E\) is the complex exponential. By the addition formula \(E(z+w)=E(z)E(w)\), \(\omega^m=E(2\pi im/N)\). So \(|\omega|=1\), because \(|E(it)|=1\) for real \(t\); \(\omega^N=E(2\pi i)=1\); and \(\omega^m\neq1\) for \(0<m<N\), because \(E(it)\neq1\) for \(0<t<2\pi\). These properties of the exponential function are recalled in (B2) near the end of the lesson. For \(g\in C(\mathbb T)\) put
\[
\Lambda_N(g)=\frac1N\sum_{k=0}^{N-1}g(\omega^k)\,\omega^k .
\]
Then \(|\Lambda_N(g)|\leq\|g\|\). For \(0\leq j\leq N-2\), the number \(\rho=\omega^{j+1}\) satisfies \(\rho\neq1\) and \(\rho^N=1\), so \(\Lambda_N(w^j)=\frac1N\sum_{k<N}\rho^k=\frac1N\,\frac{\rho^N-1}{\rho-1}=0\). On \(\mathbb T\), \(\bar w=w^{-1}\), so \(\Lambda_N(\bar w)=\frac1N\sum_k\omega^{-k}\omega^k=1\). Given \(p\in A\) of degree \(d\), take \(N\geq d+2\). Then \(\Lambda_N(\bar w-p)=1\), so \(\|\bar w-p\|\geq1\). In particular \(A\) is not self-adjoint. [Exercise 1](#exercises) transfers this example to \(\mathbb R\) with the Cayley map, so self-adjointness is needed for noncompact \(X\) as well.

The number \(2\pi\Lambda_N(g)\) is a Riemann sum for the integral \(\int_0^{2\pi}g(e^{it})e^{it}\,dt\), and the finite sums avoid integration. [Proposition 17.3](#oa-fnd-sw-19)(c)–(d) gives the version with integrals.

**(b) Separation.** The even functions in \(C_0(\mathbb R)\) form a closed self-adjoint subalgebra \(A_{\mathrm{ev}}\). It vanishes nowhere, since \(\varphi\in A_{\mathrm{ev}}\), and it does not separate \(x\) from \(-x\). For \(f\in A_{\mathrm{ev}}\),
\(1=\psi(1)-\psi(-1)=(\psi-f)(1)-(\psi-f)(-1)\leq2\|\psi-f\|\),
so \(\psi\) has distance at least \(\frac12\) from \(A_{\mathrm{ev}}\). On \([-1,1]\), the even polynomials form an algebra that does not separate \(x\) from \(-x\). By [Theorem 13.2](#oa-fnd-sw-12), their closure is the set of even continuous functions, not \(C([-1,1])\).

**(c) Vanishing nowhere.** \(A_0=\{f\in C_0(\mathbb R):f(0)=0\}\) is a closed self-adjoint subalgebra. It separates points. Let \(x\neq y\); by symmetry we may take \(x\neq0\). Put \(r=\min(|x|,|x-y|)>0\) and \(\tau(t)=\max(0,1-|t-x|/r)\). Then \(\tau\in C_c(\mathbb R)\), \(\tau(0)=0\), \(\tau(x)=1\) and \(\tau(y)=0\). But \(\|\varphi-f\|\geq|\varphi(0)-f(0)|=1\) for every \(f\in A_0\), so \(A_0\) is not dense. On \([0,1]\), the polynomials without constant term separate points and vanish at \(0\), and their closure is \(\{f:f(0)=0\}\) by [Theorem 9.1](#oa-fnd-sw-07)(b).

**(d) Closure under products.** \(V=\operatorname{span}_{\mathbb C}\{\varphi,\psi\}\) is closed under conjugation, since \(\varphi\) and \(\psi\) are real. It separates points: if \(\varphi(x)=\varphi(y)\) and \(\psi(x)=\psi(y)\), then \(x=\psi(x)/\varphi(x)=y\). It vanishes nowhere. But \(V\) has dimension \(2\), so it is closed, while \(C_0(\mathbb R)\) has infinite dimension (it contains infinitely many nonzero functions with disjoint supports). So \(V\) is not dense. It is not an algebra: \(\varphi^2=a\varphi+b\psi\) would give \(\varphi(x)=a+bx\) for all \(x\), which fails at \(x=0\), \(\pm1\).

**(e) Lattices.** For the lattice versions of [Theorem 8.2](#oa-fnd-sw-06), separation and nowhere vanishing are not enough, and the pointwise lattice operations matter.

- (i) On \(K=[0,1]\), \(L=\{f\in C(K;\mathbb R):f(0)=0\}\) is a closed subalgebra, closed under \(\vee\) and \(\wedge\), that separates points (by (c)). It fails condition (ii) of [Theorem 8.2](#oa-fnd-sw-06)(1) at \(0\), and it is not dense. The same holds for any compact Hausdorff \(K\) and \(p\in K\), with Urysohn's lemma ([Theorem 5.1](#oa-fnd-sw-16)) supplying separation.
- (ii) Let \(K=\{a,b\}\) be discrete, so \(C(K;\mathbb R)=\mathbb R^2\). For \(\lambda>0\), \(\lambda\neq1\), let \(L_\lambda=\{(s,\lambda s):s\in\mathbb R\}\). Since \(\lambda>0\), \((s,\lambda s)\wedge(t,\lambda t)=(s\wedge t,\lambda(s\wedge t))\), so \(L_\lambda\) is a lattice subspace. It separates the two points and vanishes at neither, but \((1,1)\notin L_\lambda\), so it fails (i) and is not dense. By contrast, an *algebra* with these two properties is all of \(\mathbb R^2\) ([Lemma 7.1](#oa-fnd-sw-05)).
- (iii) Let \(K=\{a,b,c\}\) be discrete, \(0<\theta<1\), and \(L=\{f:f(c)=\theta f(a)+(1-\theta)f(b)\}\). \(L\) contains the constants and satisfies (i): at any two points, the value at the third point can be solved for. In its own order, \(L\) is a lattice, isomorphic to \(\mathbb R^2\) through \((f(a),f(b))\). But it is not closed under pointwise \(\wedge\): \(f=(1,0,\theta)\) and \(g=(0,1,1-\theta)\) lie in \(L\), while \(f\wedge g=(0,0,\min(\theta,1-\theta))\) does not. \(L\) is a proper subspace, hence closed and not dense.

**(f) Bounded functions instead of \(C_0\).** Let \(X=\mathbb N\), so \(C_b(X)=\ell^\infty\). The convergent sequences \(c\) form a closed self-adjoint subalgebra that contains \(1\) and separates points (\(n\mapsto1/n\) is injective). For \(a\in c\) with limit \(l\), the sequence \(e_n=(-1)^n\) satisfies \(\|e-a\|\geq\max(|1-l|,|1+l|)\geq1\). So \(c\) is not dense in \(C_b(\mathbb N)\). [Proposition 16.1](#oa-fnd-sw-18)(3) proves that this failure occurs on every noncompact metrizable space.

**(g) The topological hypothesis.** No counterexample exists: by [Proposition 12.1](#oa-fnd-sw-10), the other hypotheses force \(X\) to be locally compact Hausdorff.

**(h) Density, not equality.** The conclusion is \(\bar A=C_0(X)\), not \(A=C_0(X)\). For example \(C_c(\mathbb R)\) is dense in \(C_0(\mathbb R)\) ([Proposition 2.1](#oa-fnd-sw-01)(3)) and \(\varphi\notin C_c(\mathbb R)\). The polynomials are dense in \(C([0,1])\), and \(|x-\frac12|\) is not a polynomial.

## 13. The closure of an arbitrary self-adjoint subalgebra

Dropping separation and nowhere vanishing does not end the story. The closure can still be described exactly.

**Lemma 13.1** (Separation quotient). Let \(K\) be a compact space and \(S\) a set of continuous functions on \(K\). Write \(x\sim_Sy\) if \(s(x)=s(y)\) for every \(s\in S\). Let \(K_S\) be the set of classes, \(q:K\to K_S\) the quotient map, and give \(K_S\) the quotient topology: \(O\subseteq K_S\) is open when \(q^{-1}(O)\) is open.

1. A function \(f\) on \(K\) is continuous and constant on each class if and only if \(f=f'\circ q\) for a continuous \(f'\) on \(K_S\). Then \(\|f\|=\|f'\|\).
2. The functions \(s'\), \(s\in S\), separate the points of \(K_S\). \(K_S\) is compact and Hausdorff.

**Proof.** (1) If \(f=f'\circ q\), then \(f\) is continuous and constant on classes. Conversely, \(f'\) is well defined, and for an open set \(O\) of scalars, \(q^{-1}(f'^{-1}(O))=f^{-1}(O)\) is open; so \(f'^{-1}(O)\) is open. Since \(q\) is onto, the norms agree. (2) Two distinct classes \(q(x)\neq q(y)\) differ at some \(s\in S\), which means \(s'(q(x))\neq s'(q(y))\). \(K_S=q(K)\) is compact by (K2), and Hausdorff by [Proposition 12.1](#oa-fnd-sw-10)(1), whose proof applies to any separating set of continuous functions. \(\square\)

**Theorem 13.2.** Let \(X\) be a topological space, and let \(A\) be a self-adjoint subalgebra of \(C_0(X)\) or a real subalgebra of \(C_0(X;\mathbb R)\). Write \(x\sim_Ay\) if \(f(x)=f(y)\) for all \(f\in A\). Then
\[
\bar A=\{f\in C_0(X):\ f(x)=f(y)\ \text{whenever }x\sim_Ay,\ \text{and }f=0\ \text{on }Z(A)\},
\tag{13.1}
\]
with \(C_0(X;\mathbb R)\) in place of \(C_0(X)\) in the real case. The same formula holds for a compact space \(K\), with \(C(K)\) or \(C(K;\mathbb R)\) in place of \(C_0(X)\).

**Proof.** First the compact case. Let \(R\) be the right side. It contains \(A\), and it is closed, since each of its conditions involves the values at one or two points. So \(\bar A\subseteq R\). Let \(f\in R\). By Lemma 13.1 with \(S=A\), \(f=f'\circ q\). The map \(a\mapsto a'\) respects sums, scalars, products and conjugation, so \(A'=\{a':a\in A\}\) is an algebra of the same kind on \(K_A\). It separates points, and its common zero set is \(q(Z(A))\), where \(f'\) vanishes. By the compact form of [Theorem 10.1](#oa-fnd-sw-09), or by [Theorem 9.1](#oa-fnd-sw-07) in the real case, \(f'\) lies in the closure of \(A'\). Since \(\|f-a\|=\|f'-a'\|\) for \(a\in A\), \(f\in\bar A\).

For \(C_0(X)\), apply the compact case to \(\tilde A\) on \(X_\infty\) ([Proposition 3.4](#oa-fnd-sw-03)). On \(X\), the relation \(\sim_{\tilde A}\) is \(\sim_A\). A point \(x\in X\) is equivalent to \(\infty\) exactly when \(x\in Z(A)\), and \(Z(\tilde A)=Z(A)\cup\{\infty\}\). So \(\tilde f\) satisfies the conditions of (13.1) for \(\tilde A\) exactly when \(f\) satisfies them for \(A\). Since \(f\mapsto\tilde f\) preserves the norm ([Proposition 3.4](#oa-fnd-sw-03)(2)), the closure transfers to \(X\). \(\square\)

**Corollary 13.3.**

1. [Theorem 10.1](#oa-fnd-sw-09) is the case in which \(\sim_A\) is equality and \(Z(A)=\varnothing\).
2. (*One common zero.*) If \(A\) separates points and \(Z(A)=\{z\}\), then \(\bar A=\{f\in C_0(X):f(z)=0\}\).
3. (*Closed subalgebras.*) For any equivalence relation \(\sim\) on \(X\) and any \(Z\subseteq X\), the functions in \(C_0(X)\) that are constant on classes and vanish on \(Z\) form a closed self-adjoint subalgebra. By (13.1) every closed self-adjoint subalgebra \(B\) has this form, with \(\sim_B\) and \(Z(B)\).
4. (*Dichotomy.*) Let \(K\) be a compact space, and let \(B\) be a closed self-adjoint subalgebra of \(C(K)\), or a closed real subalgebra of \(C(K;\mathbb R)\), that separates points. Then \(B\) is either the whole space or the set of all its functions that vanish at one point \(z\). Indeed, \(Z(B)\) has at most one point ([Lemma 7.1](#oa-fnd-sw-05)(1)). If it is empty, apply [Theorem 9.1](#oa-fnd-sw-07)(a) or the compact form of [Theorem 10.1](#oa-fnd-sw-09); if \(Z(B)=\{z\}\), apply (2).

Self-adjointness cannot be dropped from Theorem 13.2. The closure of the polynomials in \(w\) on \(\mathbb T\) ([Example 12.2](#oa-fnd-sw-11)(a)) separates points and contains \(1\), yet it is not \(C(\mathbb T)\). [Proposition 17.3](#oa-fnd-sw-19) describes it.

## 14. The Weierstrass theorem: Bernstein polynomials and Korovkin's theorem

The polynomial step of [Section 6](#oa-fnd-sw-04) does not need the Weierstrass approximation theorem, and nothing above uses it. This section proves the classical theorem directly and constructively, with a quantitative form.

**Theorem 14.1** (Korovkin's theorem). Let \(I=[a,b]\), and let \(L_n:C(I;\mathbb R)\to C(I;\mathbb R)\) be linear maps that are positive: \(u\geq0\) implies \(L_nu\geq0\). Put \(e_k(t)=t^k\). If \(L_ne_k\to e_k\) uniformly for \(k=0,1,2\), then \(L_nf\to f\) uniformly for every \(f\in C(I;\mathbb R)\).

*Reference:* due to Korovkin; see [Altomare 2010, Theorem 3.1].

**Proof.** Positivity makes each \(L_n\) monotone: \(u\leq v\) implies \(L_nu\leq L_nv\). Fix \(f\) and \(\varepsilon>0\). By uniform continuity ([Lemma 4.1](#oa-fnd-sw-15)(d)) there is \(\delta>0\) with \(|f(s)-f(t)|<\varepsilon\) when \(|s-t|<\delta\). If \(|s-t|\geq\delta\), then \(|f(s)-f(t)|\leq2\|f\|\leq2\|f\|(s-t)^2/\delta^2\). So for all \(s,t\in I\),
\[
|f(s)-f(t)|\leq\varepsilon+c\,(s-t)^2,\qquad c=2\|f\|/\delta^2 .
\tag{14.1}
\]
Fix \(t\) and read (14.1) as an inequality between functions of \(s\): with \(q_t=e_2-2te_1+t^2e_0\),
\(-\varepsilon e_0-cq_t\leq f-f(t)e_0\leq\varepsilon e_0+cq_t\).
Apply \(L_n\) and evaluate at \(t\):
\[
|(L_nf)(t)-f(t)(L_ne_0)(t)|\leq\varepsilon(L_ne_0)(t)+c\,(L_nq_t)(t).
\]
Here \((L_nq_t)(t)=(L_ne_2)(t)-2t(L_ne_1)(t)+t^2(L_ne_0)(t)\), which tends to \(t^2-2t^2+t^2=0\) uniformly in \(t\in I\), because \(|t|\) is bounded on \(I\). Hence
\[
\|L_nf-f\|\leq\|f\|\,\|L_ne_0-e_0\|+\varepsilon\|L_ne_0\|+c\sup_{t\in I}|(L_nq_t)(t)|,
\]
and the limit superior of the right side is at most \(\varepsilon\). \(\square\)

**Proposition 14.2** (Bernstein polynomials). For a bounded \(f:[0,1]\to\mathbb R\) and \(n\geq1\) put
\[
b_{n,k}(x)=\binom nk x^k(1-x)^{n-k},\qquad(B_nf)(x)=\sum_{k=0}^nf(k/n)\,b_{n,k}(x).
\]

1. \(B_ne_0=e_0\), \(B_ne_1=e_1\) and \(B_ne_2=e_2+(e_1-e_2)/n\). Hence
\[
\sum_{k=0}^n\Bigl(\frac kn-x\Bigr)^2b_{n,k}(x)=\frac{x(1-x)}n .
\tag{14.2}
\]
2. \(B_nf\to f\) uniformly for every continuous \(f\).
3. For every bounded \(f\) and every \(x\in[0,1]\),
\(|f(x)-(B_nf)(x)|\leq\frac32\,\omega(f,n^{-1/2})\), where \(\omega(f,\delta)=\sup\{|f(s)-f(t)|:|s-t|\leq\delta\}\).
4. If \(f\) is bounded and continuous at \(x_0\), then \((B_nf)(x_0)\to f(x_0)\). Boundedness cannot be dropped.
5. (*Bernoulli trials*) For \(x\in[0,1]\) and \(\delta>0\),
\(\sum_{k:\,|k/n-x|\geq\delta}b_{n,k}(x)\leq x(1-x)/(n\delta^2)\).

*Reference:* due to Bernstein; see [Altomare 2010, Theorem 3.6]. Version 4 of [van Neerven] (April 2022) states (4) in its Remark 2.4 for every function that is continuous at \(x_0\); the example in the proof of (4) shows that boundedness is needed, and version 7 (July 2025) adds it.

**Proof.** (1) The binomial theorem gives \(\sum_kb_{n,k}(x)=(x+1-x)^n=1\). Since \(\frac kn\binom nk=\binom{n-1}{k-1}\) for \(k\geq1\), we get \(\sum_k\frac kn\,b_{n,k}(x)=x\sum_{j=0}^{n-1}\binom{n-1}jx^j(1-x)^{n-1-j}=x\). For \(n\geq2\) and \(k\geq1\), \(\bigl(\frac kn\bigr)^2\binom nk=\frac{n-1}n\binom{n-2}{k-2}+\frac1n\binom{n-1}{k-1}\) (with \(\binom{n-2}{-1}=0\)), which gives \(B_ne_2=\frac{n-1}nx^2+\frac xn\), as claimed; for \(n=1\), \(B_1e_2(x)=x=x^2+x(1-x)\) directly. Expanding \((k/n-x)^2\) and using the three identities gives (14.2).

(2) \(B_n\) is linear and positive, and \(\|B_ne_2-e_2\|\leq\frac1{4n}\) by (1). Apply Korovkin's theorem, Theorem 14.1.

(3) First, \(\omega(f,\lambda\delta)\leq(1+\lambda)\,\omega(f,\delta)\) for \(\lambda>0\): if \(|s-t|\leq\lambda\delta\), split the segment between \(s\) and \(t\) into \(m\) equal pieces, where \(m\) is the least integer \(\geq\lambda\); each piece has length at most \(\delta\), so \(|f(s)-f(t)|\leq m\,\omega(f,\delta)\leq(1+\lambda)\,\omega(f,\delta)\). With \(\lambda=|s-t|/\delta\) this gives \(|f(s)-f(t)|\leq(1+|s-t|/\delta)\,\omega(f,\delta)\) for all \(s,t\). Since the weights \(b_{n,k}(x)\) are nonnegative with sum \(1\),
\[
|f(x)-(B_nf)(x)|\leq\sum_kb_{n,k}(x)\,|f(x)-f(k/n)|\leq\omega(f,\delta)\Bigl(1+\frac1\delta\sum_kb_{n,k}(x)\Bigl|x-\frac kn\Bigr|\Bigr).
\]
By the Cauchy–Schwarz inequality for these weights and (14.2), the last sum is at most \((x(1-x)/n)^{1/2}\leq\frac1{2\sqrt n}\). Take \(\delta=n^{-1/2}\).

(4) Given \(\varepsilon>0\), take \(\delta>0\) with \(|f(t)-f(x_0)|<\varepsilon\) for \(|t-x_0|<\delta\). Splitting the sum in (3) according to whether \(|k/n-x_0|<\delta\), and using (5),
\(|f(x_0)-(B_nf)(x_0)|\leq\varepsilon+2\|f\|\,x_0(1-x_0)/(n\delta^2)\).
For the second claim, let \(f(1/m)=2^{m^2}\) for \(m\geq3\), and \(f=0\) at all other points of \([0,1]\). Then \(f=0\) on \((\frac13,1]\), so \(f\) is continuous at \(\frac12\). All terms of \((B_nf)(\frac12)\) are nonnegative, and for \(n\geq3\) the term with \(k=1\) is \(n\,2^{-n}f(1/n)=n\,2^{n^2-n}\). So \((B_nf)(\frac12)\to\infty\), while \(f(\frac12)=0\).

(5) Where \(|k/n-x|\geq\delta\), \((k/n-x)^2/\delta^2\geq1\). Sum against \(b_{n,k}(x)\) and use (14.2). \(\square\)

*Probabilistic reading.* \(b_{n,k}(x)\) is the probability of exactly \(k\) successes in \(n\) independent trials that each succeed with probability \(x\). So \((B_nf)(x)\) is the expected value of \(f\) at the observed frequency of success. Part (5) is the weak law of large numbers for such trials: the frequency lies within \(\delta\) of \(x\) with probability at least \(1-x(1-x)/(n\delta^2)\).

**Corollary 14.3** (Weierstrass approximation theorem). Every continuous complex function on \([a,b]\) is a uniform limit of polynomials, with real coefficients when the function is real.

*Reference:* [Weierstrass 1885].

**Proof.** The substitution \(t=a+(b-a)x\) carries polynomials to polynomials. Apply Proposition 14.2(2) to the real and imaginary parts. A second proof: on the compact space \([a,b]\), the polynomials with complex coefficients form a self-adjoint algebra (for real \(t\), the conjugate of \(\sum c_kt^k\) is \(\sum\bar c_kt^k\)) that contains \(1\) and separates points; apply the compact form of [Theorem 10.1](#oa-fnd-sw-09), or [Theorem 9.1](#oa-fnd-sw-07) for real functions. \(\square\)

## 15. Further density theorems on compact spaces

**Proposition 15.1.**

1. (*Polynomials in several variables.*) Let \(X\subseteq\mathbb R^n\) be compact. The real polynomials in \(x_1,\dots,x_n\) are dense in \(C(X;\mathbb R)\), and the complex ones in \(C(X)\). Every continuous \(F:X\to\mathbb R^m\) is a uniform limit of maps whose \(m\) coordinates are such polynomials.
2. (*Polynomials in \(z\) and \(\bar z\).*) Let \(X\subseteq\mathbb C\) be compact. The functions \(z\mapsto p(z,\bar z)\), with \(p\) a complex polynomial in two variables, are dense in \(C(X)\).
3. (*Separability.*) If \(K\) is a compact metric space, \(C(K)\) is separable.
4. (*Trigonometric polynomials.*) The trigonometric polynomials \(\sum_{|k|\leq n}c_kw^k\) form a dense subspace of \(C(\mathbb T)\). Equivalently, the functions \(\theta\mapsto\sum_{|k|\leq n}c_ke^{ik\theta}\) are dense, uniformly on \(\mathbb R\), in the continuous \(2\pi\)-periodic functions.
5. (*Products.*) Let \(X_1,\dots,X_k\) be compact spaces, not necessarily Hausdorff. The linear combinations of the functions \(f_1(x_1)\cdots f_k(x_k)\), with \(f_j\in C(X_j;\mathbb R)\), are dense in \(C(X_1\times\cdots\times X_k;\mathbb R)\). Every complex continuous function on the product is a uniform limit of finite sums of functions \(\lambda f_1(x_1)\cdots f_k(x_k)\) with \(\lambda\in\{1,i\}\) and real \(f_j\).
6. (*Iterated integrals.*) Let \(X,Y\) be compact spaces, and \(\mu:C(X;\mathbb R)\to\mathbb R\), \(\nu:C(Y;\mathbb R)\to\mathbb R\) positive linear maps. For \(h\in C(X\times Y;\mathbb R)\), the functions \(x\mapsto\nu(h(x,\cdot))\) and \(y\mapsto\mu(h(\cdot,y))\) are continuous, and
\[
\mu\bigl(x\mapsto\nu(h(x,\cdot))\bigr)=\nu\bigl(y\mapsto\mu(h(\cdot,y))\bigr).
\tag{15.1}
\]
In particular, for continuous \(h\) on \([a,b]\times[c,d]\), the two iterated Riemann integrals of \(h\) agree, and the Riemann sums of \(h\) over grid partitions converge to their common value.
7. (*Moments.*) Let \(a<b\). If \(f\in C([a,b])\) and \(\int_a^bf(x)x^n\,dx=0\) for all \(n\geq0\), then \(f=0\). The condition \(a<b\) is needed: on \([a,a]\) every integral is \(0\), so the constant function \(1\) has all its moments equal to \(0\).

**Proof.** (1) The coordinate functions and \(1\) generate an algebra, which separates points because the coordinates do; apply [Theorem 9.1](#oa-fnd-sw-07). The complex polynomials form a self-adjoint algebra, since the coordinates are real; apply the compact form of [Theorem 10.1](#oa-fnd-sw-09). For \(F\), approximate each coordinate.

(2) The algebra contains \(1\) and \(z\), which separates points. It is self-adjoint: the conjugate of \(p(z,\bar z)\) is \(\bar p(\bar z,z)\), where \(\bar p\) has the conjugate coefficients. Apply the compact form of [Theorem 10.1](#oa-fnd-sw-09).

(3) Choose a countable dense set \(C\subseteq K\) ([Lemma 4.1](#oa-fnd-sw-15)(d)), and put \(d_c(x)=d(x,c)\). The functions \(d_c\) and \(1\) generate a real algebra \(A_0\) that contains the constants. It separates points: if \(x\neq y\) and \(r=d(x,y)\), choose \(c\in C\) with \(d(x,c)<r/2\); then \(d_c(x)<r/2<d_c(y)\). By [Theorem 9.1](#oa-fnd-sw-07), \(A_0\) is dense in \(C(K;\mathbb R)\). The finite products of the functions \(d_c\) and \(1\) form a countable set, and its linear combinations with rational coefficients are dense in \(A_0\), hence in \(C(K;\mathbb R)\). Combinations with Gaussian rational coefficients give a countable set that is dense in \(C(K)\).

(4) On \(\mathbb T\), \(\bar w=w^{-1}\), so the trigonometric polynomials form the algebra generated by \(w\) and \(\bar w\). It is self-adjoint, contains \(1\), and separates points through \(w\). Apply the compact form of [Theorem 10.1](#oa-fnd-sw-09) on the compact space \(\mathbb T\). For the periodic form: the map \(\theta\mapsto E(i\theta)\) from \([0,2\pi]\) onto \(\mathbb T\) (it is onto by (B2)) is continuous from a compact space onto a Hausdorff space, so it maps closed sets to closed sets. A continuous \(2\pi\)-periodic function takes equal values on each fibre, so it equals \(g(E(i\theta))\) for a function \(g\) on \(\mathbb T\), and \(g\) is continuous by the closed-map argument used in (5) below. Conversely each \(g\in C(\mathbb T)\) gives a continuous periodic function, and \(E(ik\theta)=E(i\theta)^k\).

(5) Apply [Lemma 13.1](#oa-fnd-sw-12) with \(S=C(X_j;\mathbb R)\) to get compact Hausdorff quotients \(q_j:X_j\to X_j'\) on which continuous functions separate points. Put \(X=\prod X_j\), \(X'=\prod X_j'\) and \(q=q_1\times\cdots\times q_k\). Let \(h\in C(X;\mathbb R)\). If \(q(x)=q(y)\), then \(h(x)=h(y)\): change one coordinate at a time, and note that with the other coordinates fixed, \(h\) is a continuous function of the remaining one, so it takes equal values at equivalent points. The map \(q\) is continuous from the compact space \(X\) ([Lemma 4.1](#oa-fnd-sw-15)(b)) onto the Hausdorff space \(X'\). So it maps closed sets to closed sets: a closed set is compact by (K1), its image is compact by (K2), and compact subsets of \(X'\) are closed by (K3). So \(h=h'\circ q\), and \(h'\) is continuous, because \(h'^{-1}(F)=q(h^{-1}(F))\) for closed \(F\subseteq\mathbb R\). On \(X'\), the linear combinations of products \(f_1'(x_1)\cdots f_k'(x_k)\) form an algebra with \(1\) in it, and it separates points, since points that differ in coordinate \(j\) are separated by a function of that coordinate. By [Theorem 9.1](#oa-fnd-sw-07) this algebra is dense in \(C(X';\mathbb R)\). Composing with \(q\) keeps norms and turns each \(f_j'\) into \(f_j'\circ q_j\in C(X_j;\mathbb R)\). The complex statement follows by approximating real and imaginary parts.

(6) Since \(-\|u\|1\leq u\leq\|u\|1\), positivity gives \(|\mu(u)|\leq\mu(1)\|u\|\), and likewise for \(\nu\). Fix \(x_0\) and \(\varepsilon>0\). For each \(y\), continuity of \(h\) at \((x_0,y)\) gives open sets \(U_y\ni x_0\) and \(V_y\ni y\) with \(|h-h(x_0,y)|<\varepsilon/2\) on \(U_y\times V_y\). Finitely many \(V_{y_j}\) cover \(Y\). On \(U=\bigcap_jU_{y_j}\) we get \(\|h(x,\cdot)-h(x_0,\cdot)\|<\varepsilon\), since both \((x,y)\) and \((x_0,y)\) lie in some \(U_{y_j}\times V_{y_j}\). So \(x\mapsto\nu(h(x,\cdot))\) is continuous, and so is the other function. The two sides of (15.1) are linear in \(h\) and bounded by \(\mu(1)\nu(1)\|h\|\). For \(h(x,y)=f(x)g(y)\), both equal \(\mu(f)\nu(g)\). By (5) such functions span a dense subspace, so (15.1) holds for all \(h\).

For the rectangle, \(\mu(u)=\int_a^bu\) and \(\nu(v)=\int_c^dv\) are positive linear maps, by (B1). Take a grid of cells \([x_{i-1},x_i]\times[y_{j-1},y_j]\) with points \((s_i,t_j)\) in the cells. Additivity over subintervals (B1) writes the iterated integral as the sum over cells of \(\int_{x_{i-1}}^{x_i}\int_{y_{j-1}}^{y_j}h\,dy\,dx\). By monotonicity of the integral, each term differs from \(h(s_i,t_j)(x_i-x_{i-1})(y_j-y_{j-1})\) by at most the area of the cell times the oscillation of \(h\) on it. \(h\) is uniformly continuous on the compact rectangle ([Lemma 4.1](#oa-fnd-sw-15)(d)), so the oscillations tend to \(0\) with the mesh. So the grid Riemann sums converge to the iterated integral.

(7) By the Weierstrass theorem ([Corollary 14.3](#oa-fnd-sw-14)) choose polynomials \(p_k\) with \(p_k\to\bar f\) uniformly on \([a,b]\). By hypothesis and linearity \(\int_a^bfp_k=0\). Since \(|\int_a^bu|\leq(b-a)\sup|u|\) for continuous \(u\) (B1), \(\bigl|\int_a^b|f|^2-\int_a^bfp_k\bigr|\leq(b-a)\|f\|\,\|\bar f-p_k\|\to0\), so \(\int_a^b|f|^2=0\). If \(f(x_0)\neq0\), then by continuity \(|f|^2>|f(x_0)|^2/2\) on \([a,b]\cap(x_0-\delta,x_0+\delta)\) for some \(\delta>0\), a subinterval of positive length because \(a<b\), and the integral would be positive, by monotonicity and additivity of the integral (B1). So \(f=0\). \(\square\)

Part (5) needs neither the Hausdorff property nor Urysohn's lemma. The continuous functions on a compact space need not separate its points, and then the products \(f_1(x_1)\cdots f_k(x_k)\) do not separate the points of the product; the quotients \(X_j'\) remove this problem. In (6), positive linear functionals are the form in which Radon measures act on continuous functions, so (15.1) also gives the equality of iterated integrals of a continuous function for Radon measures on compact Hausdorff spaces.

## 16. Compact sets, extension of functions, and bounded functions

**Proposition 16.1.**

1. (*Uniform approximation on compact sets.*) Let \(X\) be any topological space and \(A\subseteq C(X;\mathbb R)\) a real algebra that separates points and vanishes nowhere. For every \(f\in C(X;\mathbb R)\), every compact \(C\subseteq X\) and every \(\varepsilon>0\), some \(a\in A\) satisfies \(|a-f|<\varepsilon\) on \(C\). Suppose that \(X\) has compact sets \(L_1\subseteq L_2\subseteq\cdots\) such that every compact set lies in some \(L_n\); by [Proposition 4.2](#oa-fnd-sw-15)(3) this holds when \(X\) is LCH and \(\sigma\)-compact. Then some sequence in \(A\) converges to \(f\) uniformly on every compact set. The complex analogue holds for self-adjoint \(A\).
2. (*Tietze extension theorem, compact case.*) Let \(K\) be compact Hausdorff, \(Z\subseteq K\) closed, and \(g\in C(Z;\mathbb R)\). Then \(g=G|_Z\) for some \(G\in C(K;\mathbb R)\) with \(\|G\|=\|g\|\).
3. (*A converse.*) Let \(X\) be a metrizable space that is not compact. Then \(C_b(X;\mathbb R)\) has a closed subalgebra with \(1\) in it that separates the points of \(X\) but is not dense.

**Proof.** (1) The restrictions of the elements of \(A\) to \(C\) form a real algebra on the compact space \(C\). It separates the points of \(C\) and vanishes nowhere on \(C\), so it is dense in \(C(C;\mathbb R)\) by [Theorem 9.1](#oa-fnd-sw-07)(a); and \(f|_C\in C(C;\mathbb R)\). For the sequence, choose \(a_n\in A\) with \(|a_n-f|<1/n\) on \(L_n\). A compact set lies in some \(L_m\), and the \(L_n\) increase, so \(|a_n-f|<1/n\) on it for \(n\geq m\). In the complex case use the compact form of [Theorem 10.1](#oa-fnd-sw-09).

(2) If \(Z=\varnothing\), take \(G=0\). Otherwise let \(R=\{G|_Z:G\in C(K;\mathbb R)\}\). It is a real algebra on the compact space \(Z\) that contains the constants. It separates the points of \(Z\): points of \(K\) are closed, so Urysohn's lemma ([Theorem 5.1](#oa-fnd-sw-16)) separates any two of them by a continuous function. By [Theorem 9.1](#oa-fnd-sw-07)(a), \(R\) is dense in \(C(Z;\mathbb R)\). It is also closed. Let \(g\in\bar R\), and choose \(G_n\in C(K;\mathbb R)\) with \(\|G_n|_Z-g\|\leq2^{-n}\). The differences \(D_n=G_{n+1}-G_n\) satisfy \(\|D_n|_Z\|<2^{1-n}\). The truncations \(E_n=(D_n\wedge2^{1-n})\vee(-2^{1-n})\) are continuous on \(K\), agree with \(D_n\) on \(Z\), and satisfy \(\|E_n\|\leq2^{1-n}\). So the series \(G=G_1+\sum_nE_n\) converges uniformly on \(K\), \(G\) is continuous ([Proposition 2.1](#oa-fnd-sw-01)(1)), and \(G|_Z=\lim_nG_n|_Z=g\). Hence \(R=C(Z;\mathbb R)\). Finally, \((G\wedge\|g\|)\vee(-\|g\|)\) still extends \(g\) and has norm \(\|g\|\).

(3) Let \(d\) be a metric for \(X\). Since \(X\) is not compact, [Lemma 4.1](#oa-fnd-sw-15)(d) gives a sequence \((x_n)\) with no convergent subsequence. A value repeated infinitely often would give a constant convergent subsequence, so after passing to a subsequence the \(x_n\) are distinct. Each point \(p\) has a ball that contains \(x_n\) for only finitely many \(n\), and after shrinking it contains no \(x_n\) other than \(p\) itself. So the sets \(E_0=\{x_n:n\text{ even}\}\) and \(E_1=\{x_n:n\text{ odd}\}\) are closed and disjoint. The function \(u=d(\cdot,E_0)/(d(\cdot,E_0)+d(\cdot,E_1))\) is continuous with values in \([0,1]\), and it is \(0\) on \(E_0\) and \(1\) on \(E_1\). Let \(A\) be the set of \(f\in C_b(X;\mathbb R)\) for which \(f(x_n)\) has a limit along the even \(n\) and a limit along the odd \(n\), and the two limits are equal. \(A\) is a subalgebra containing the constants. It is closed: if \(f_k\in A\) have common limits \(l_k\) and \(f_k\to f\), then \(|l_k-l_j|\leq\|f_k-f_j\|\), so \(l_k\to l\), and \(f(x_n)\to l\) along both parities. \(A\) separates points: for \(x\neq y\) choose \(0<r<d(x,y)\) such that the ball \(B(x,r)\) contains no \(x_n\) other than \(x\), and put \(f(z)=\max(0,1-d(z,x)/r)\). Then \(f(x)=1\), \(f(y)=0\), and \(f(x_n)=0\) whenever \(x_n\neq x\), so \(f\in A\). But if \(f\in A\) has common limit \(l\), then \(\|u-f\|\geq\max(|l|,|1-l|)\geq\frac12\). So \(A\) is not dense. \(\square\)

In (2), Urysohn's lemma is used only to separate points; the closedness of \(R\) comes from the truncation argument. [Example 12.2](#oa-fnd-sw-11)(f) is the case \(X=\mathbb N\) of (3). The conclusion of (3) holds for every completely regular Hausdorff space that is not compact; that version is proved with the Stone–Čech compactification [Blackadar], which this lesson does not develop.

## 17. Convex functions, singular functions, and the disc algebra

**Proposition 17.1** (Differences of convex functions). Let \(K\) be a compact space and \(P\) a nonempty set of nonnegative continuous real functions on \(K\), closed under sums, under multiplication by positive scalars, and under \(\wedge\) or under \(\vee\). Then \(L=P-P=\{f-g:f,g\in P\}\) is a linear subspace closed under \(\wedge\) and \(\vee\). If \(P\) separates points and some nonzero constant function lies in \(P\), then \(L\) is dense in \(C(K;\mathbb R)\). In particular, every continuous function on \([a,b]\) is a uniform limit of differences of continuous convex functions.

**Proof.** \(L\) is closed under sums and positive multiples, \(L=-L\), and \(0=f-f\in L\); so \(L\) is a linear subspace. For \(f_1-g_1\) and \(f_2-g_2\) in \(L\),
\[
(f_1-g_1)\wedge(f_2-g_2)=\bigl((f_1+g_2)\wedge(f_2+g_1)\bigr)-(g_1+g_2),
\]
because subtracting the same function from two functions commutes with \(\wedge\). The same identity holds with \(\vee\). So if \(P\) is closed under \(\wedge\), so is \(L\), and then \(L\) is closed under \(\vee\) because \(f\vee g=-((-f)\wedge(-g))\) and \(L=-L\). The case of \(\vee\) is symmetric. If \(P\) contains a constant \(c>0\) and separates points, then \(L\) contains all constants and separates points, so it is dense by [Theorem 8.2](#oa-fnd-sw-06)(2). On \([a,b]\), take for \(P\) the nonnegative continuous convex functions. Sums, positive multiples and maxima of convex functions are convex, \(1\in P\), and \(x\mapsto x-a+1\) lies in \(P\) and separates points. The nonnegative concave functions, with \(\wedge\), work in the same way. \(\square\)

A set \(N\subseteq\mathbb R\) is *null* if, for every \(\varepsilon>0\), countably many intervals of total length less than \(\varepsilon\) cover it. A union of two null sets is null, and so is the image of a null set under a map \(t\mapsto\alpha+\beta t\).

**Proposition 17.2** (Singular functions). Let \(C_{\mathrm{sing}}([a,b])\) be the set of continuous \(f:[a,b]\to\mathbb R\) that are differentiable with derivative \(0\) outside a null set. Then \(C_{\mathrm{sing}}([a,b])\) is a subalgebra of \(C([a,b];\mathbb R)\); it contains the constants, and it separates points. So it is dense in \(C([a,b];\mathbb R)\).

**Proof.** *Subalgebra.* If \(f'=0\) off a null set \(N_f\) and \(g'=0\) off a null set \(N_g\), then off the null set \(N_f\cup N_g\) the functions \(f+g\), \(\lambda f\) and \(fg\) are differentiable with derivative \(0\). For \(fg\), write \(f(s)g(s)-f(t)g(t)=f(s)(g(s)-g(t))+g(t)(f(s)-f(t))\) and use continuity of \(f\).

*The Cantor function.* Let \(\Phi\) be the set of continuous nondecreasing \(\phi:[0,1]\to[0,1]\) with \(\phi(0)=0\) and \(\phi(1)=1\). For \(\phi\in\Phi\) define \(T\phi\) to be \(\phi(3x)/2\) on \([0,\frac13]\), \(\frac12\) on \([\frac13,\frac23]\), and \(\frac12+\phi(3x-2)/2\) on \([\frac23,1]\). Then \(T\phi\in\Phi\), and \(\|T\phi-T\chi\|\leq\frac12\|\phi-\chi\|\). Starting from \(c_0(x)=x\), the functions \(c_{n+1}=Tc_n\) satisfy \(\|c_{n+1}-c_n\|\leq2^{-n}\). So they converge uniformly to some \(c\in\Phi\) with \(Tc=c\). Let \(G_1=(\frac13,\frac23)\) and \(G_{n+1}=G_1\cup\frac13G_n\cup(\frac23+\frac13G_n)\). By induction on \(n\): \(G_n\subseteq G_{n+1}\); \([0,1]\setminus G_n\) is a union of \(2^n\) closed intervals of length \(3^{-n}\); and \(c=Tc\) is constant on each component interval of \(G_n\). So \(c\) is locally constant on the open set \(G=\bigcup_nG_n\), and \([0,1]\setminus G\) is null, since for each \(n\) it is covered by intervals of total length \((2/3)^n\).

*Separation.* Let \(a\leq x<y\leq b\). Put \(s(t)=0\) for \(t\leq x\), \(s(t)=c\bigl((t-x)/(y-x)\bigr)\) for \(x\leq t\leq y\), and \(s(t)=1\) for \(t\geq y\). Then \(s\) is continuous, \(s(x)=0\) and \(s(y)=1\). It is locally constant, so differentiable with derivative \(0\), off the null set \(\{x,y\}\cup\bigl(x+(y-x)([0,1]\setminus G)\bigr)\). So \(s\in C_{\mathrm{sing}}([a,b])\), and [Theorem 9.1](#oa-fnd-sw-07)(a) gives density. \(\square\)

For the next result, let \(\mathcal P\) be the algebra of polynomials in \(w\), restricted to \(\mathbb T\). For \(g\in C(\mathbb T)\) and \(n\in\mathbb Z\) put \(\hat g(n)=\frac1{2\pi}\int_0^{2\pi}g(e^{i\theta})e^{-in\theta}\,d\theta\), and let \(\bar D=\{z:|z|\leq1\}\).

**Proposition 17.3** (The disc algebra).

- (a) If \(p\in\mathcal P\) and \(\bar p\in\mathcal P\), then \(p\) is constant. So \(\mathcal P\) is not self-adjoint.
- (b) As functions of \(\theta\), the elements of \(\mathcal P\) are the sums \(\sum_{k=0}^nc_ke^{ik\theta}\).
- (c)–(d) \(\hat g(-1)=0\) for every \(g\) in the closure \(\bar{\mathcal P}\), while \(\bar w\) has \(\hat{\bar w}(-1)=1\). So \(\bar w\notin\bar{\mathcal P}\).
- (e) \(\bar{\mathcal P}=\{G|_{\mathbb T}:\ G\in C(\bar D),\ G(z)=\sum_{n\geq0}a_nz^n\ \text{for }|z|<1\}\).
- (f) \(\bar{\mathcal P}=\{g\in C(\mathbb T):\ \hat g(n)=0\ \text{for all }n<0\}\).
- (g) Trigonometric polynomials approximate every \(g\in C(\mathbb T)\) uniformly ([Proposition 15.1](#oa-fnd-sw-17)(4)).

**Proof.** For integers \(m\neq0\), \(\int_0^{2\pi}e^{im\theta}\,d\theta=0\), by the fundamental theorem of calculus (B1) applied to \(e^{im\theta}/(im)\), whose derivative is \(e^{im\theta}\) and which takes the same value at \(0\) and \(2\pi\) (B2). So if \(t=\sum_kc_ke^{ik\theta}\) is a finite sum, then \(\hat t(n)=c_n\). Also \(|\hat g(n)|\leq\|g\|\), since \(|\int u|\leq\int|u|\) (B1).

(a) Write \(p=\sum_{k\geq0}c_kw^k\). On \(\mathbb T\), \(\bar p=\sum_k\bar c_kw^{-k}\), so \(\hat{\bar p}(-k)=\bar c_k\). If \(\bar p\in\mathcal P\), its coefficients at negative \(n\) vanish, so \(c_k=0\) for \(k\geq1\).

(b) \(e^{ik\theta}=(e^{i\theta})^k\) by the addition formula.

(c)–(d) \(g\mapsto\hat g(-1)\) is continuous and vanishes on \(\mathcal P\), hence on \(\bar{\mathcal P}\), while \(\bar w=e^{-i\theta}\) gives the value \(1\). (Compare [Example 12.2](#oa-fnd-sw-11)(a), which gives \(\|\bar w-p\|\geq1\) without integrals.)

(f) If \(g\in\bar{\mathcal P}\), then \(\hat g(n)=0\) for \(n<0\), by continuity as in (c). Conversely, let \(\hat g(n)=0\) for \(n<0\). For \(0\leq r<1\) put
\[
P_r(t)=\sum_{n\in\mathbb Z}r^{|n|}e^{int}=\frac{1-r^2}{|1-re^{it}|^2}>0 .
\]
The series converges absolutely and uniformly in \(t\), and summing its two geometric halves gives the closed form: with \(z=re^{it}\), \(\frac1{1-z}+\frac{\bar z}{1-\bar z}=\frac{1-|z|^2}{|1-z|^2}\). Integrating term by term, which uniform convergence allows (B1), gives \(\frac1{2\pi}\int_0^{2\pi}P_r(\theta-t)\,dt=1\) and
\[
(P_rg)(e^{i\theta}):=\frac1{2\pi}\int_0^{2\pi}P_r(\theta-t)\,g(e^{it})\,dt=\sum_{n\in\mathbb Z}r^{|n|}\hat g(n)\,e^{in\theta}.
\]
Here \(\hat g(n)=0\) for \(n<0\), so \(P_rg=\sum_{n\geq0}r^n\hat g(n)w^n\), a series of elements of \(\mathcal P\) that converges uniformly on \(\mathbb T\) because \(|r^n\hat g(n)|\leq r^n\|g\|\). So \(P_rg\in\bar{\mathcal P}\). It remains to show \(\|P_rg-g\|\to0\) as \(r\to1\). Given \(\varepsilon>0\), uniform continuity on the compact set \(\mathbb T\) ([Lemma 4.1](#oa-fnd-sw-15)(d)) gives \(\eta>0\) with \(|g(u)-g(v)|<\varepsilon\) when \(u,v\in\mathbb T\) and \(|u-v|<\eta\). Since \(P_r\) has average \(1\),
\[
(P_rg-g)(e^{i\theta})=\frac1{2\pi}\int_0^{2\pi}P_r(\theta-t)\bigl(g(e^{it})-g(e^{i\theta})\bigr)\,dt .
\]
Let \(r\geq1-\eta/2\). If \(|e^{it}-e^{i\theta}|\geq\eta\), then \(|1-re^{i(\theta-t)}|=|e^{it}-re^{i\theta}|\geq\eta-(1-r)\geq\eta/2\), so \(P_r(\theta-t)\leq4(1-r^2)/\eta^2\). Hence, for every \(t\), the integrand has absolute value at most \(\varepsilon P_r(\theta-t)+8\|g\|(1-r^2)/\eta^2\). Integrating this bound, by monotonicity of the integral (B1), gives \(\|P_rg-g\|\leq\varepsilon+8\|g\|(1-r^2)/\eta^2\), which is less than \(2\varepsilon\) for \(r\) close to \(1\).

(e) Let \(g\in\bar{\mathcal P}\). By (f), \(\hat g(n)=0\) for \(n<0\), and \(|\hat g(n)|\leq\|g\|\). Put \(G(z)=\sum_{n\geq0}\hat g(n)z^n\) for \(|z|<1\), and \(G=g\) on \(\mathbb T\). For \(z=re^{i\theta}\) with \(r<1\), \(G(z)=(P_rg)(e^{i\theta})\). The series converges uniformly on each disc \(|z|\leq\rho<1\), so \(G\) is continuous on the open disc. Let \(w_0\in\mathbb T\) and \(z\to w_0\) in \(\bar D\). For \(|z|<1\) we have \(|G(z)-g(w_0)|\leq\|P_{|z|}g-g\|+|g(z/|z|)-g(w_0)|\), and for \(|z|=1\) we have \(|G(z)-g(w_0)|=|g(z)-g(w_0)|\). Both tend to \(0\), by (f) and the continuity of \(g\). So \(G\in C(\bar D)\). Conversely, let \(G\in C(\bar D)\) with \(G(z)=\sum a_nz^n\) for \(|z|<1\). For \(r<\rho<1\), the terms \(a_n\rho^n\) tend to \(0\), so \(|a_n|r^n\leq C(r/\rho)^n\) for some \(C\). So \(G_r(w)=G(rw)=\sum a_nr^nw^n\) converges uniformly on \(\mathbb T\), and \(G_r|_{\mathbb T}\in\bar{\mathcal P}\). \(G\) is uniformly continuous on the compact set \(\bar D\) ([Lemma 4.1](#oa-fnd-sw-15)(d)), and \(|rw-w|=1-r\), so \(G_r\to G\) uniformly on \(\mathbb T\). Hence \(G|_{\mathbb T}\in\bar{\mathcal P}\). \(\square\)

The proof of (e) uses the dilations \(G_r\), not the partial sums of the Taylor series of \(G\): those partial sums need not converge uniformly on the circle. By [Cauchy's theorem for cycles and its consequences, Lemma 3.1 and Theorem 3.2](course:foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences#OA-FND-CT-03), the functions given by power series on the open disc are exactly the holomorphic ones. So (e) says that \(\bar{\mathcal P}\) consists of the restrictions to \(\mathbb T\) of the continuous functions on \(\bar D\) that are holomorphic on the open disc.

## 18. Integer coefficients and simultaneous approximation of derivatives

**Proposition 18.1** (Integer coefficients on \([0,1]\)). A function \(f\in C([0,1];\mathbb R)\) can be approximated uniformly on \([0,1]\) by polynomials with integer coefficients if and only if \(f(0)\) and \(f(1)\) are integers.

**Proof.** Let \(\mathcal G\) be the closure of \(\mathbb Z[x]\) in \(C([0,1];\mathbb R)\). It is closed under addition, negation and multiplication, by the argument of [Proposition 2.1](#oa-fnd-sw-01)(2). *Necessity:* \(p(0),p(1)\in\mathbb Z\) for \(p\in\mathbb Z[x]\), and a limit of integers is an integer.

*Step 1 (iterates).* Let \(g(x)=2x-3x^2+2x^3=x+x(1-x)(1-2x)\). Then \(g(0)=0\), \(g(\frac12)=\frac12\), \(g(1)=1\), and \(g'(x)=6(x-\frac12)^2+\frac12>0\). So \(g\) is an increasing bijection of \([0,1]\), with \(g(x)>x\) on \((0,\frac12)\) and \(g(x)<x\) on \((\frac12,1)\). Let \(g_m\) be the \(m\)-th iterate of \(g\); then \(g_m\in\mathbb Z[x]\) and \(0\leq g_m\leq1\) on \([0,1]\). For \(0<x\leq\frac12\), the sequence \(g_m(x)\) increases and is bounded by \(\frac12\), so it converges to a fixed point of \(g\) in \((0,\frac12]\). The fixed points of \(g\) are \(0\), \(\frac12\) and \(1\), so the limit is \(\frac12\). The case \([\frac12,1)\) is symmetric. For \(0<\varepsilon<\frac12\) and \(x\in[\varepsilon,1-\varepsilon]\), monotonicity gives \(g_m(\varepsilon)\leq g_m(x)\leq g_m(1-\varepsilon)\), so \(g_m\to\frac12\) uniformly on \([\varepsilon,1-\varepsilon]\).

*Step 2 (dyadic constants).* For \(n\geq0\) and \(0\leq k\leq2^n\) there are \(\phi_m\in\mathbb Z[x]\) with \(0\leq\phi_m\leq1\) on \([0,1]\) and \(\phi_m\to k/2^n\) uniformly on \([\varepsilon,1-\varepsilon]\) for every \(\varepsilon\in(0,\frac12)\). For \(k=0\) and \(k=2^n\) take the constants \(0\) and \(1\); this settles \(n=0\). Suppose the claim holds for \(n\). If \(k\) is even, \(k/2^{n+1}=(k/2)/2^n\). If \(k=2j+1\), take sequences \(\phi_m\to j/2^n\) and \(\chi_m\to(j+1)/2^n\), and put \(\psi_m=g_m\phi_m+(1-g_m)\chi_m\in\mathbb Z[x]\). It takes values in \([0,1]\), as a convex combination, and
\[
\psi_m-\frac{k}{2^{n+1}}=g_m\Bigl(\phi_m-\frac j{2^n}\Bigr)+(1-g_m)\Bigl(\chi_m-\frac{j+1}{2^n}\Bigr)-\Bigl(g_m-\frac12\Bigr)\frac1{2^n}\to0
\]
uniformly on \([\varepsilon,1-\varepsilon]\).

*Step 3 (real multiples).* Let \(p\in\mathbb Z[x]\) with \(p(0)=p(1)=0\). The set \(\Lambda_p=\{\lambda\in\mathbb R:\lambda p\in\mathcal G\}\) is a closed additive subgroup of \(\mathbb R\) that contains \(\mathbb Z\). Let \(\lambda=k/2^n\in[0,1]\) and \(\eta>0\). Choose \(\varepsilon\) with \(|p|\leq\eta\) on \([0,\varepsilon]\cup[1-\varepsilon,1]\), and then \(m\) with \(|\phi_m-\lambda|\leq\eta/(1+\|p\|)\) on \([\varepsilon,1-\varepsilon]\). Since \(|\phi_m-\lambda|\leq1\) everywhere, \(\|\phi_mp-\lambda p\|\leq\eta\), and \(\phi_mp\in\mathbb Z[x]\). So \(\lambda\in\Lambda_p\). Adding integers, \(\Lambda_p\) contains all dyadic rationals, and being closed, \(\Lambda_p=\mathbb R\).

*Step 4 (conclusion).* A real polynomial \(r\) with \(r(0)=r(1)=0\) has the form \(x(1-x)s(x)=\sum_js_jx^{j+1}(1-x)\) with real \(s_j\), and each term lies in \(\mathcal G\) by Step 3; so \(r\in\mathcal G\). These polynomials form a real algebra. On \(X=(0,1)\) it lies in \(C_0(X;\mathbb R)\), separates points (the ratio of \(x^2(1-x)\) to \(x(1-x)\) is \(x\)), and vanishes nowhere. By [Theorem 9.2](#oa-fnd-sw-08) it is dense in \(C_0(X;\mathbb R)\). Directly from (1.1), \(C_0(X;\mathbb R)\) consists of the restrictions of the \(h\in C([0,1];\mathbb R)\) with \(h(0)=h(1)=0\). So every such \(h\) lies in \(\mathcal G\). Finally, if \(f(0),f(1)\in\mathbb Z\), then \(q(x)=f(0)+(f(1)-f(0))x\in\mathbb Z[x]\), and \(f-q\) vanishes at \(0\) and \(1\); so \(f=q+(f-q)\in\mathcal G\). \(\square\)

**Proposition 18.2** (Integer coefficients on \([-1,1]\)). A function \(f\in C([-1,1];\mathbb R)\) can be approximated uniformly on \([-1,1]\) by polynomials with integer coefficients if and only if \(f(-1)\), \(f(0)\), \(f(1)\) are integers and \(f(-1)\equiv f(1)\pmod 2\).

**Proof.** Let \(\mathcal G'\) be the closure of \(\mathbb Z[x]\) in \(C([-1,1];\mathbb R)\). *Necessity:* for \(p=\sum a_kx^k\in\mathbb Z[x]\), \(p(1)-p(-1)=2\sum_{k\text{ odd}}a_k\) is even. Limits of integers are integers, and a convergent sequence of integers is eventually constant, so the parity condition passes to limits. *Sufficiency:* let \(p\in\mathbb Z[x]\) vanish at \(-1\), \(0\) and \(1\), and let \(\phi_m\) be as in Step 2 of the proof of Proposition 18.1. The polynomials \(\psi_m(x)=\phi_m(1-x^2)\) have integer coefficients and values in \([0,1]\) on \([-1,1]\). They converge to \(k/2^n\) uniformly where \(\varepsilon\leq1-x^2\leq1-\varepsilon\), that is, where \(\sqrt\varepsilon\leq|x|\leq\sqrt{1-\varepsilon}\). Near \(0\) and \(\pm1\), \(p\) is small. Step 3 of that proof, with these changes, gives \(\lambda p\in\mathcal G'\) for all real \(\lambda\). Every real polynomial vanishing at \(-1,0,1\) is \(x(1-x^2)s(x)=\sum_js_jx^{j+1}(1-x^2)\), so it lies in \(\mathcal G'\). These polynomials form a real algebra which, on \(X=(-1,0)\cup(0,1)\), separates points (the ratio of \(x^2(1-x^2)\) to \(x(1-x^2)\) is \(x\)) and vanishes nowhere. By [Theorem 9.2](#oa-fnd-sw-08) it is dense in \(C_0(X;\mathbb R)\), which by (1.1) consists of the restrictions of the continuous functions on \([-1,1]\) that vanish at \(-1\), \(0\) and \(1\). Finally, \(\beta=(f(1)-f(-1))/2\) and \(\gamma=(f(1)+f(-1))/2-f(0)\) are integers by the parity condition, and \(q(x)=f(0)+\beta x+\gamma x^2\in\mathbb Z[x]\) agrees with \(f\) at \(-1\), \(0\) and \(1\). So \(f=q+(f-q)\in\mathcal G'\). \(\square\)

**Proposition 18.3** (Smooth functions). Let \(I=[a,b]\) and \(r\geq0\) an integer, and let \(f\) be \(r\) times continuously differentiable on \(I\), with one-sided derivatives at the ends.

1. For every \(\varepsilon>0\) there is a polynomial \(p\) with \(\|f^{(k)}-p^{(k)}\|<\varepsilon\) for \(0\leq k\leq r\).
2. If \(f\) is infinitely differentiable, there are polynomials \(p_n\) with \(p_n^{(k)}\to f^{(k)}\) uniformly for every \(k\geq0\).
3. So the polynomials are dense in \(C^r(I)\) for the norm \(\max_{k\leq r}\|f^{(k)}\|\), and in \(C^\infty(I)\) for the topology of uniform convergence of each derivative.

**Proof.** (1) Put \(c=\max(1,b-a)\). By the Weierstrass theorem ([Corollary 14.3](#oa-fnd-sw-14)) choose a polynomial \(q_r\) with \(\|f^{(r)}-q_r\|<\varepsilon/c^r\). Going down, put \(q_{k-1}(x)=f^{(k-1)}(a)+\int_a^xq_k(t)\,dt\) for \(k=r,\dots,1\), and \(p=q_0\). Each \(q_{k-1}\) is a polynomial with \(q_{k-1}'=q_k\), because the indefinite integral of a continuous function is differentiable with that function as its derivative (B1); so \(p^{(k)}=q_k\). By the fundamental theorem of calculus (B1), \(f^{(k-1)}(x)=f^{(k-1)}(a)+\int_a^xf^{(k)}(t)\,dt\). So \(\|f^{(k-1)}-q_{k-1}\|\leq(b-a)\|f^{(k)}-q_k\|\leq c\,\|f^{(k)}-q_k\|\), by the bound \(|\int_a^xu|\leq(x-a)\sup|u|\) of (B1). Induction gives \(\|f^{(k)}-q_k\|<c^{r-k}\varepsilon/c^r\leq\varepsilon\). (2) Apply (1) with \(r=n\) and \(\varepsilon=1/n\). For fixed \(k\) and \(n\geq k\), \(\|f^{(k)}-p_n^{(k)}\|<1/n\). (3) restates (1) and (2). \(\square\)

## Exercises

**Exercise 1 (self-adjointness is needed on the line).** Let \(\kappa(x)=(x-i)/(x+i)\) be the Cayley map of [Example 3.3](#oa-fnd-sw-02)(a), and \(u=\kappa-1\). Show that \(A=\{q\circ u:\ q\text{ a complex polynomial},\ q(0)=0\}\) is a subalgebra of \(C_0(\mathbb R)\) that separates points and vanishes nowhere, but that \(\|\bar u-a\|\geq1\) for every \(a\in A\).

*Solution.* \(u(x)=-2i/(x+i)\), so \(|u(x)|=2(1+x^2)^{-1/2}\). The sets \(\{|u|\geq\varepsilon\}\) are closed and bounded, hence compact, so \(u\in C_0(\mathbb R)\), and \(A\subseteq C_0(\mathbb R)\) by [Proposition 2.1](#oa-fnd-sw-01)(3). The condition \(q(0)=0\) survives sums, scalar multiples and products, so \(A\) is a subalgebra. \(u\) is injective because \(\kappa\) is, so \(A\) separates points; and \(u(x)\neq0\) because \(\kappa(x)\neq1\), so \(A\) vanishes nowhere. By [Proposition 3.2](#oa-fnd-sw-02)(5) and [Proposition 3.4](#oa-fnd-sw-03), the rule \(G(\kappa(x))=g(x)\), \(G(1)=0\), defines a norm-preserving bijection \(g\mapsto G\) of \(C_0(\mathbb R)\) onto \(\{G\in C(\mathbb T):G(1)=0\}\). For \(g=q\circ u\), \(G(w)=q(w-1)\), also at \(w=1\), since \(q(0)=0\). For \(g=\bar u\), \(G(w)=\bar w-1\). Take \(\Lambda_N\) from [Example 12.2](#oa-fnd-sw-11)(a) with \(N\geq\deg q+2\). Then \(\Lambda_N\) vanishes on the polynomial \(q(w-1)\) and on \(1\), and \(\Lambda_N(\bar w)=1\). So \(\|\bar u-q\circ u\|=\|\bar w-1-q(w-1)\|\geq|\Lambda_N(\bar w-1-q(w-1))|=1\).

**Exercise 2 (the route through the constants).** Let \(K\) be compact and \(A\subseteq C(K;\mathbb R)\) a real algebra that separates points and has \(Z(A)=\{z\}\). Let \(B=\{a+s1:\ a\in\bar A,\ s\in\mathbb R\}\). Show that \(B\) is a closed algebra, that \(1\in B\), and that \(B\) separates points. Deduce \(\bar A=\{f:f(z)=0\}\) from the case of algebras with constants.

*Solution.* \(\bar A\) is an algebra ([Proposition 2.1](#oa-fnd-sw-01)(2)), and \((a+s)(b+t)=(ab+ta+sb)+st\), so \(B\) is an algebra. Let \(a_n+s_n\to f\) with \(a_n\in\bar A\). Evaluating at \(z\) gives \(s_n\to f(z)\), so \(a_n\to f-f(z)1\), which then lies in \(\bar A\); so \(f\in B\), and \(B\) is closed. \(B\) contains \(1\) and \(A\), so it separates points. By [Proposition 6.2](#oa-fnd-sw-04)(3), \(B\) is closed under \(\wedge\), so [Theorem 8.2](#oa-fnd-sw-06)(2) makes it dense, and \(B=C(K;\mathbb R)\). If \(f(z)=0\), write \(f=a+s1\) with \(a\in\bar A\). Then \(0=a(z)+s=s\), so \(f=a\in\bar A\). The reverse inclusion is clear. [Theorem 9.1](#oa-fnd-sw-07) avoids the detour through \(B\).

**Exercise 3 (\(C_0\) of a product).** Let \(X\) and \(Y\) be LCH. Show that the linear span of the functions \((f\otimes g)(x,y)=f(x)g(y)\), \(f\in C_0(X)\), \(g\in C_0(Y)\), is dense in \(C_0(X\times Y)\).

*Solution.* \(X\times Y\) is Hausdorff, and a product of compact neighbourhoods is a compact neighbourhood ([Lemma 4.1](#oa-fnd-sw-15)(b)); so it is LCH. If \(|f(x)g(y)|\geq\varepsilon\), then \(|f(x)|\geq\varepsilon/(\|g\|+1)\) and \(|g(y)|\geq\varepsilon/(\|f\|+1)\). So \(\{|f\otimes g|\geq\varepsilon\}\) is closed and lies in a product of two compact sets, and \(f\otimes g\in C_0(X\times Y)\) by (K1). The span is a self-adjoint subalgebra, since \((f\otimes g)(f'\otimes g')=(ff')\otimes(gg')\) and \(\overline{f\otimes g}=\bar f\otimes\bar g\). Let \((x,y)\neq(x',y')\), say \(x\neq x'\). By the locally compact form of Urysohn's lemma ([Corollary 5.2](#oa-fnd-sw-16)), choose \(f\in C_c(X)\) with \(f(x)=1\), \(f(x')=0\), and \(g\in C_c(Y)\) with \(g=1\) on \(\{y,y'\}\). Then \(f\otimes g\) takes the values \(1\) and \(0\) at the two points. The case \(y\neq y'\) is symmetric, and the same functions show that the span vanishes nowhere. Apply [Theorem 10.1](#oa-fnd-sw-09).

**Exercise 4 (separability).** Let \(X\) be LCH and second countable. Show that \(C_0(X)\) is separable.

*Solution.* By the metrizability theorem, [Theorem 5.3](#oa-fnd-sw-16), \(X_\infty\) is a compact metrizable space. By [Proposition 15.1](#oa-fnd-sw-17)(3), \(C(X_\infty)\) is separable. A subset of a separable metric space is separable, since the space has a countable base of balls. So \(I_\infty\) is separable, and so is \(C_0(X)\), which is isometric to it ([Proposition 3.4](#oa-fnd-sw-03)).

## Where this leads

- *Commutative C\*-algebras.* In [the lesson on C\*-algebras and the continuous functional calculus](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones), [Theorem 10.1](#oa-fnd-sw-09) shows that the Gelfand transform of a commutative C\*-algebra maps onto \(C_0\) of its character space. Urysohn's lemma and the density theorems of Section 15 are used there as well.
- *States on C\*-algebras.* The lesson "Integral representations of states" uses Stone's lattice lemma and the real and complex theorems to show that certain spaces of continuous functions on compact convex sets and on state spaces are dense.
- *Locally compact groups.* In the course "Modular theory and weights", the lesson "The Plancherel weight and Fourier coefficients of a locally compact group" shows that the Fourier algebra \(A(G)\) of a locally compact group \(G\) lies in \(C_0(G)\), is closed under pointwise products and complex conjugation, separates points and vanishes nowhere. [Theorem 10.1](#oa-fnd-sw-09) then makes \(A(G)\) dense in \(C_0(G)\). Since the proof uses no countability, this holds for every locally compact group.
- *Algebras that are not self-adjoint.* For these the conclusion can fail, as the disc algebra of [Proposition 17.3](#oa-fnd-sw-19) shows. Bishop's theorem [Bishop 1961] reduces approximation by a closed subalgebra of \(C(K)\) to its maximal antisymmetric sets.

## Results used from other lessons

The following facts are proved in the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20), whose text is [Lebl], and [Proof, Logic, and Discrete Structures](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B10), whose text is [Levin]. Each item gives the place of the proof. A few steps that these texts leave to the reader are proved here.

- (B1) *The Riemann integral.* Every continuous function \(u:[a,b]\to\mathbb R\) is Riemann integrable ([Real Analysis I, Lemma 5.2.7](https://www.jirka.org/ra/html/sec_rintprop.html#lemma_contint)). The integral is additive over subintervals: \(\int_a^bu=\int_a^cu+\int_c^bu\) for \(a\leq c\leq b\) ([Proposition 5.2.2](https://www.jirka.org/ra/html/sec_rintprop.html#sec_rintprop-3-5)). It is monotone: if \(u\leq v\), then \(\int_a^bu\leq\int_a^bv\) ([Proposition 5.2.6](https://www.jirka.org/ra/html/sec_rintprop.html#sec_rintprop-4-8)). If \(m\leq u\leq M\), then \(m(b-a)\leq\int_a^bu\leq M(b-a)\) ([Proposition 5.1.10](https://www.jirka.org/ra/html/sec_rint.html#intbound_prop)). And \(\int_a^b\alpha u=\alpha\int_a^bu\) for \(\alpha\geq0\) ([Proposition 5.2.4](https://www.jirka.org/ra/html/sec_rintprop.html#prop_integrallinear)).
  The remaining cases of linearity are proved as follows. For a bounded function \(u\) and a partition \(P\), the infimum of \(-u\) on each cell of \(P\) is minus the supremum of \(u\) there, so the lower and upper sums satisfy \(L(P,-u)=-U(P,u)\) and \(U(P,-u)=-L(P,u)\). Taking the supremum and the infimum over \(P\) shows that \(-u\) is integrable with \(\int_a^b(-u)=-\int_a^bu\) when \(u\) is. For bounded \(u\) and \(v\), on each cell the infimum of \(u+v\) is at least the sum of the infima of \(u\) and \(v\), and the supremum of \(u+v\) is at most the sum of the suprema, so \(L(P,u)+L(P,v)\leq L(P,u+v)\) and \(U(P,u+v)\leq U(P,u)+U(P,v)\). Let \(u\) and \(v\) be integrable, let \(P_1\) and \(P_2\) be partitions, and put \(P=P_1\cup P_2\). Refining a partition does not lower its lower sums or raise its upper sums ([Real Analysis I, Proposition 5.1.7](https://www.jirka.org/ra/html/sec_rint.html#prop_refinement)), and the lower integral is at most the upper integral ([Proposition 5.1.8](https://www.jirka.org/ra/html/sec_rint.html#intulbound_prop)), so
  \[
  L(P_1,u)+L(P_2,v)\leq L(P,u+v)\leq\underline{\int_a^b}(u+v)\leq\overline{\int_a^b}(u+v)\leq U(P,u+v)\leq U(P_1,u)+U(P_2,v).
  \]
  Taking the supremum of the left side and the infimum of the right side over \(P_1\) and \(P_2\) gives \(\int_a^bu+\int_a^bv\leq\underline{\int_a^b}(u+v)\leq\overline{\int_a^b}(u+v)\leq\int_a^bu+\int_a^bv\). So \(u+v\) is integrable and \(\int_a^b(u+v)=\int_a^bu+\int_a^bv\).
  For a continuous complex function \(u=u_1+iu_2\) one puts \(\int_a^bu=\int_a^bu_1+i\int_a^bu_2\). By the real case, applied to real and imaginary parts, this integral is complex linear. Moreover \(|\int_a^bu|\leq\int_a^b|u|\leq(b-a)\sup_{[a,b]}|u|\). The second inequality is Proposition 5.1.10 applied to the continuous function \(|u|\). For the first, let \(\int_a^bu\neq0\) and put \(c=|\int_a^bu|/\int_a^bu\). Then \(|c|=1\), and \(\int_a^bcu=c\int_a^bu=|\int_a^bu|\) is real, so it equals its real part \(\int_a^b\operatorname{Re}(cu)\). Since \(\operatorname{Re}(cu)\leq|cu|=|u|\), monotonicity gives \(|\int_a^bu|\leq\int_a^b|u|\).
  A uniformly convergent series of continuous functions can be integrated term by term: apply [Real Analysis II, Theorem 6.2.4](https://www.jirka.org/ra/html/sec_liminter.html#integralinterchange_thm) to the partial sums, which are continuous and so integrable, and to their real and imaginary parts. If \(u\) is continuous, then \(x\mapsto\int_a^xu\) is differentiable on \([a,b]\) with derivative \(u\) ([Real Analysis I, Theorem 5.3.3](https://www.jirka.org/ra/html/sec_ftc.html#thm_FTCv2)). If \(F\) is differentiable on \([a,b]\) and \(F'\) is continuous, then \(\int_a^bF'=F(b)-F(a)\) ([Theorem 5.3.1](https://www.jirka.org/ra/html/sec_ftc.html#thm_FTCv1), the fundamental theorem of calculus). For complex functions, apply both to real and imaginary parts.
- (B2) *The exponential function.* Put \(E(z)=\sum_{n\geq0}z^n/n!\) for \(z\in\mathbb C\); the series converges for every \(z\). Write \(e^z=E(z)\). The law of exponents \(E(z+w)=E(z)E(w)\) is [Real Analysis II, Proposition 11.4.1](https://www.jirka.org/ra/html/sec_complexexp.html#sec_complexexp-3-7). [Proposition 11.4.2](https://www.jirka.org/ra/html/sec_complexexp.html#sec_complexexp-4-4) and its proof give the following for real \(x\): \(E(ix)=\cos x+i\sin x\) with \(\cos x\) and \(\sin x\) real, and \(|E(ix)|=1\); \(E(i\pi/2)=i\) and \(E(2\pi i)=1\), so \(E\) has period \(2\pi i\); \(t\mapsto E(it)\) is one-to-one on \([0,2\pi)\), so \(E(it)\neq1=E(0)\) for \(0<t<2\pi\); and every \(z\in\mathbb T\) with \(\operatorname{Re}z\geq0\) and \(\operatorname{Im}z\geq0\) is \(E(ix)\) for some \(x\in[0,\pi/2]\). Two further facts are proved here.
  *Every point of \(\mathbb T\) is \(E(it)\) for some \(t\in[0,2\pi)\).* Multiplication by \(-i\) maps \(a+ib\) to \(b-ia\). So for \(z\in\mathbb T\), one of \(z\), \(-iz\), \(-z\) and \(iz=(-i)^3z\) has nonnegative real and imaginary parts: \((-i)^kz=E(ix)\) for some \(k\in\{0,1,2,3\}\) and \(x\in[0,\pi/2]\). Then \(z=i^kE(ix)=E\bigl(i(x+k\pi/2)\bigr)\) by the law of exponents, and \(x+k\pi/2\in[0,2\pi]\). If \(x+k\pi/2=2\pi\), then \(z=E(2\pi i)=1=E(0)\).
  *For real \(m\), the function \(t\mapsto E(imt)\) on \(\mathbb R\) is differentiable with derivative \(imE(imt)\).* For complex \(w\) with \(|w|\leq1\),
  \[
  |E(w)-1-w|\leq\sum_{k\geq2}\frac{|w|^k}{k!}\leq|w|^2\sum_{k\geq2}\frac1{k!}\leq|w|^2,
  \]
  by the triangle inequality for the partial sums, and since \(k!\geq2^{k-1}\) gives \(\sum_{k\geq2}1/k!\leq\sum_{k\geq2}2^{1-k}=1\). For real \(h\neq0\) with \(|mh|\leq1\), the law of exponents gives \(E(im(t+h))-E(imt)-imhE(imt)=E(imt)\bigl(E(imh)-1-imh\bigr)\), and \(|E(imt)|=1\). Hence
  \[
  \Bigl|\frac{E(im(t+h))-E(imt)}h-imE(imt)\Bigr|\leq\frac{|mh|^2}{|h|}=m^2|h|,
  \]
  which tends to \(0\) as \(h\to0\).
- (B3) *Numbers.* The real numbers form an ordered field with the least upper bound property; *Real Analysis I* starts from this ([Theorem 1.2.1](https://www.jirka.org/ra/html/sec_setofreals.html#sec_setofreals-3-3)).
  The geometric sum \(\sum_{k=0}^{N-1}\rho^k=(1-\rho^N)/(1-\rho)\) for \(\rho\neq1\) is proved by induction in [Real Analysis I, Example 0.3.8](https://www.jirka.org/ra/html/sec_basicset.html#example_geometricsum). The induction uses only the field operations, so the identity holds for complex \(\rho\). If \(|\rho|\leq r<1\), then
  \[
  \Bigl|\sum_{k=0}^{N-1}\rho^k-\frac1{1-\rho}\Bigr|=\frac{|\rho|^N}{|1-\rho|}\leq\frac{r^N}{1-r},
  \]
  which tends to \(0\) as \(N\to\infty\) ([Real Analysis I, Proposition 2.2.11](https://www.jirka.org/ra/html/sec_factslimsseqs.html#sec_factslimsseqs-6-6)). So \(\sum_{k\geq0}\rho^k=1/(1-\rho)\), uniformly for \(|\rho|\leq r\).
  The binomial theorem is [Proof, Logic, and Discrete Structures, Theorem 3.1.9](https://kokunoyumeto.github.io/program-matematika-indonesia/en/courses/B10/reader/sec_counting-pascal.html#thm-binomial), and the formula \(\binom nk=\frac{n!}{k!\,(n-k)!}\) is [Theorem 3.4.9](https://kokunoyumeto.github.io/program-matematika-indonesia/en/courses/B10/reader/sec_counting-combperm.html#subsec-combinations-9) there. Bernoulli's inequality \((1+u)^n\geq1+nu\) for \(u\geq0\) follows from the binomial theorem, because all its terms are nonnegative.
  The Cauchy–Schwarz inequality \(\bigl(\sum_kw_ka_k\bigr)^2\leq\bigl(\sum_kw_k\bigr)\bigl(\sum_kw_ka_k^2\bigr)\) for finitely many real numbers \(a_k\) and weights \(w_k\geq0\) is [Real Analysis II, Lemma 7.1.4](https://www.jirka.org/ra/html/sec_metric.html#sec_metric-16), applied to the vectors \((\sqrt{w_k})_k\) and \((\sqrt{w_k}\,a_k)_k\).

## References



- [Alexandroff 1924] P. Alexandroff, Über die Metrisation der im Kleinen kompakten topologischen Räume, *Math. Ann.* 92 (1924), 294–301. https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0092%7CLOG_0024
- [Bishop 1961] E. Bishop, A generalization of the Stone–Weierstrass theorem, *Pacific J. Math.* 11 (1961), 777–783. https://doi.org/10.2140/pjm.1961.11.777
- [Blackadar] B. Blackadar, *Real Analysis*, preliminary edition, 2025. https://bruceblackadar.com/mathpubs.html
- [Lebl] J. Lebl, *Basic Analysis I* and *Basic Analysis II: Introduction to Real Analysis*, version 6.3 (15 May 2026), freely available at [www.jirka.org/ra](https://www.jirka.org/ra/). It is the text of the core courses *Real Analysis I* and *Real Analysis II*.
- [Levin] O. Levin, *Discrete Mathematics: An Open Introduction*, 4th ed., freely available at [discrete.openmathbooks.org](https://discrete.openmathbooks.org/dmoi4/). It is the text of the core course *Proof, Logic, and Discrete Structures*, which has an English reader at [the programme site](https://kokunoyumeto.github.io/program-matematika-indonesia/en/courses/B10/reader/).
- [π-Base] The π-Base Community, S. Clontz and J. Dabbs, *π-Base: a community database of topological counterexamples*, [topology.pi-base.org](https://topology.pi-base.org/).
- [Stone 1937] M. H. Stone, Applications of the theory of Boolean rings to general topology, *Trans. Amer. Math. Soc.* 41 (1937), 375–481. https://doi.org/10.1090/S0002-9947-1937-1501905-7. Free at https://www.ams.org/journals/tran/1937-041-03/S0002-9947-1937-1501905-7/S0002-9947-1937-1501905-7.pdf
- [Urysohn 1925] P. Urysohn, Über die Mächtigkeit der zusammenhängenden Mengen, *Math. Ann.* 94 (1925), 262–295. https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0094%7CLOG_0020
- [van Neerven] J. van Neerven, *Functional Analysis*, arXiv:2112.11166, version 4 (28 April 2022) and version 7 (17 July 2025). https://arxiv.org/abs/2112.11166
- [Weierstrass 1885] K. Weierstrass, Über die analytische Darstellbarkeit sogenannter willkürlicher Functionen einer reellen Veränderlichen, *Sitzungsber. Königl. Preuss. Akad. Wiss. Berlin* (1885), 633–639 and 789–805. https://archive.org/details/sitzungsberichte1885deutsch/page/633/mode/1up

- [Altomare 2010] F. Altomare, Korovkin-type theorems and approximation by positive linear operators, *Surveys in
  Approximation Theory* 5 (2010), 92–164; arXiv:1009.2601. Free at https://arxiv.org/abs/1009.2601

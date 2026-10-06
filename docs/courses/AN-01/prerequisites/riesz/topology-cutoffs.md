# The Stone–Weierstrass theorem for functions vanishing at infinity

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session. The October revisions correct two points found by an AI reviewer in a separate OpenAI Codex session and add proofs of the background facts that the core courses leave as exercises; they are self-checked by the writing AI. Public domain (CC0).*

**Bounded prerequisite selection (October 2026).** This companion selects original lines 1–172, preserving the header, conventions, one-point compactification, compact Hausdorff normality, local shrinking and Urysohn cutoff constructions with their complete proofs. The retained original introduction and bibliography also credit the unselected later Stone–Weierstrass argument. Its Theorem 10.1 is an optional second density proof linked to the full online source; the selected Haar source gives its own direct density proof. No later theorem is needed for the cutoff chain used here. The selected source prose and mathematics are unchanged apart from link destinations and line-ending normalization. Selection and link repair: GPT-6.1 Sol (OpenAI), Ultra reasoning effort, for the AN-01 course project. No independent mathematical certification is asserted.

This lesson proves the Stone–Weierstrass theorem for continuous functions that vanish at infinity. Let \(X\) be a locally compact Hausdorff space, and let \(A\) be a subalgebra of \(C_0(X)\) that is closed under complex conjugation, separates the points of \(X\), and has no common zero. Then every function in \(C_0(X)\) is a uniform limit of functions in \(A\) ([Theorem 10.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09)). The algebra need not contain the constant functions, and \(X\) need not be compact, \(\sigma\)-compact or metrizable. Commutative C\*-algebras and harmonic analysis on locally compact groups need the theorem in this form.

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

**Corollary 5.2** (Urysohn's lemma, locally compact form). Let \(X\) be LCH, \(A\subseteq X\) compact and \(B\subseteq X\) closed with \(A\cap B=\varnothing\). Then some \(f\in C_c(X)\) with \(0\leq f\leq1\) equals \(1\) on \(A\) and \(0\) on \(B\). In particular, \(X\) is completely regular (take \(A=\{p\}\)), and \(C_c(X)\), hence \(C_0(X)\), separates points and vanishes nowhere. [Theorem 10.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09) then gives a second proof that \(C_c(X)\) is dense in \(C_0(X)\).

**Proof.** By [Proposition 4.2](#oa-fnd-sw-15)(2) with \(V=X\setminus B\), choose an open \(U\supseteq A\) whose closure \(K\) is compact and lies in \(X\setminus B\). \(K\) is compact Hausdorff, so Urysohn's lemma gives a continuous \(g:K\to[0,1]\) with \(g=1\) on \(A\) and \(g=0\) on \(K\setminus U\). Put \(f=g\) on \(K\) and \(f=0\) on \(X\setminus K\); so \(f=0\) on \(X\setminus U\). For closed \(F\subseteq[0,1]\), \(f^{-1}(F)\) is \(g^{-1}(F)\) if \(0\notin F\), and \(g^{-1}(F)\cup(X\setminus U)\) if \(0\in F\). Both are closed in \(X\), since \(K\) is closed in \(X\). So \(f\) is continuous, its support lies in \(K\), and \(f=0\) on \(B\). \(\square\)

## Original source bibliography, retained

## References

- [Alexandroff 1924] P. Alexandroff, Über die Metrisation der im Kleinen kompakten topologischen Räume, *Math. Ann.* 92 (1924), 294–301. https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0092%7CLOG_0024
- [Bishop 1961] E. Bishop, A generalization of the Stone–Weierstrass theorem, *Pacific J. Math.* 11 (1961), 777–783. https://doi.org/10.2140/pjm.1961.11.777
- [Blackadar] B. Blackadar, *Real Analysis*, preliminary edition, 2025. https://bruceblackadar.com/mathpubs.html
- [Lebl] J. Lebl, *Basic Analysis I* and *Basic Analysis II: Introduction to Real Analysis*, version 6.3 (15 May 2026), open textbook under CC BY-SA 4.0 and CC BY-NC-SA 4.0, [www.jirka.org/ra](https://www.jirka.org/ra/). It is the text of the core courses *Real Analysis I* and *Real Analysis II*.
- [Levin] O. Levin, *Discrete Mathematics: An Open Introduction*, 4th ed., open textbook under CC BY-NC-SA 4.0, [discrete.openmathbooks.org](https://discrete.openmathbooks.org/dmoi4/). It is the text of the core course *Proof, Logic, and Discrete Structures*, which has an English reader at [the programme site](https://kokunoyumeto.github.io/program-matematika-indonesia/en/courses/B10/reader/).
- [π-Base] The π-Base Community, S. Clontz and J. Dabbs, *π-Base: a community database of topological counterexamples*, open database under CC BY 4.0, [topology.pi-base.org](https://topology.pi-base.org/).
- [Stone 1937] M. H. Stone, Applications of the theory of Boolean rings to general topology, *Trans. Amer. Math. Soc.* 41 (1937), 375–481. https://doi.org/10.1090/S0002-9947-1937-1501905-7. Free at https://www.ams.org/journals/tran/1937-041-03/S0002-9947-1937-1501905-7/S0002-9947-1937-1501905-7.pdf
- [Urysohn 1925] P. Urysohn, Über die Mächtigkeit der zusammenhängenden Mengen, *Math. Ann.* 94 (1925), 262–295. https://resolver.sub.uni-goettingen.de/purl?PPN235181684_0094%7CLOG_0020
- [van Neerven] J. van Neerven, *Functional Analysis*, arXiv:2112.11166, version 4 (28 April 2022) and version 7 (17 July 2025). https://arxiv.org/abs/2112.11166
- [Weierstrass 1885] K. Weierstrass, Über die analytische Darstellbarkeit sogenannter willkürlicher Functionen einer reellen Veränderlichen, *Sitzungsber. Königl. Preuss. Akad. Wiss. Berlin* (1885), 633–639 and 789–805. https://archive.org/details/sitzungsberichte1885deutsch/page/633/mode/1up

- [Altomare 2010] F. Altomare, Korovkin-type theorems and approximation by positive linear operators, *Surveys in
  Approximation Theory* 5 (2010), 92–164; arXiv:1009.2601. Free at https://arxiv.org/abs/1009.2601

## Source and rights

The selected original programme exposition is dedicated under CC0 1.0. Historical authorship and checking statements remain exactly as supplied in the source header. External references retain their own rights; their text is not reproduced here. The [CC0 legal text](LICENSE-CC0.txt) and [component provenance](component-provenance.json) accompany this selection. The full transparent source remains available at [its original source location](https://raw.githubusercontent.com/KokunoYumeto/open-math-courses/main/docs/courses/function-algebras-and-approximation/src/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.md).

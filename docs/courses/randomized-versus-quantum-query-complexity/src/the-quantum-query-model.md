# The quantum query model

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A quantum algorithm for a Boolean function keeps a unit vector in a finite-dimensional complex space. It changes the vector by unitary maps that do not depend on the input, and by one special unitary map, the query, that does. At the end a measurement gives the output with certain probabilities. The number of queries is the cost; all other operations are free. This lesson gives the precise definitions, proves that measurements in the middle of a computation do not make algorithms stronger, and provides the tools with which the algorithms of the course are described.

- States, unitary maps, measurements (Section 1).
- Query algorithms and the number \(Q(f)\) (Section 2).
- Algorithms that measure and continue; they can be simulated without loss (Theorem 3.2).
- Queries at computed positions; phase queries; conditional queries (Lemmas 4.1 and 4.2).
- Decision trees run in superposition (Lemma 5.1).
- Two rules for probabilities (Section 6).

The lesson needs complex vector spaces with an inner product and unitary maps ([Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40), core course). No physics is used. The definitions are the standard ones of quantum query complexity; [OpenAI-Q] uses them without restating them.

## 1. States, unitary maps, measurements

Let \(B\) be a finite set of *labels*. The space \(\mathbb C^B\) consists of the vectors \(\psi=(\psi_\beta)_{\beta\in B}\) with complex entries; its inner product is \(\langle\varphi,\psi\rangle=\sum_\beta\overline{\varphi_\beta}\psi_\beta\). The vector with the entry \(1\) at \(\beta\) and \(0\) elsewhere is written \(|\beta\rangle\); these *basis states* are an orthonormal basis. A *state* is a vector of norm \(1\).

**Registers.** If \(B=B_1\times B_2\), then \(\mathbb C^B=\mathbb C^{B_1}\otimes\mathbb C^{B_2}\) with \(|\beta_1,\beta_2\rangle=|\beta_1\rangle\otimes|\beta_2\rangle\). We say that the space has two *registers*. A linear map \(U\) on the first register acts on the whole space as \(U\otimes I\). The same holds for more factors. Every vector has a unique form
\[
\psi=\sum_{\beta_1\in B_1}|\beta_1\rangle\otimes\psi^{\beta_1},\qquad\psi^{\beta_1}\in\mathbb C^{B_2},
\]
and \(\|\psi\|^2=\sum_{\beta_1}\|\psi^{\beta_1}\|^2\).

**Unitary maps.** A linear map \(U\) of \(\mathbb C^B\) is *unitary* if it preserves the inner product. Products and inverses of unitary maps are unitary. Two kinds are used all the time.

- For a bijection \(\pi\) of \(B\), the linear map with \(|\beta\rangle\mapsto|\pi(\beta)\rangle\) is unitary. We call it a *permutation map*. Every reversible computation on labels is of this kind, for example \(|c,y\rangle\mapsto|c,y\oplus g(c)\rangle\) for a function \(g\) with values in \(\{0,1\}^t\), where \(\oplus\) is the addition of bits modulo \(2\).
- For two states \(\varphi,\varphi'\) there is a unitary map with \(\varphi\mapsto\varphi'\). In particular a given state can be *prepared* from a basis state.

Both are special cases of the following fact.

**Lemma 1.1.** Let \(X\) be a subspace of \(\mathbb C^B\) and \(J:X\to\mathbb C^B\) a linear map that preserves the inner product. Then \(J\) is the restriction of a unitary map of \(\mathbb C^B\).

**Proof.** \(J\) is injective, so \(J(X)\) has the dimension of \(X\), and the orthogonal complements of \(X\) and of \(J(X)\) have the same dimension. Map an orthonormal basis of the first complement to an orthonormal basis of the second. Together with \(J\) this defines a linear map that maps an orthonormal basis of \(\mathbb C^B\) to an orthonormal basis. \(\blacksquare\)

**Measurements.** *Measuring* a state \(\psi\) gives a label \(\beta\) with the probability \(|\psi_\beta|^2\). *Measuring the first register* of a state \(\psi=\sum_{\beta_1}|\beta_1\rangle\otimes\psi^{\beta_1}\) gives \(\beta_1\) with the probability \(\|\psi^{\beta_1}\|^2\), and then the state is
\[
|\beta_1\rangle\otimes\frac{\psi^{\beta_1}}{\|\psi^{\beta_1}\|}.
\]
Measuring the first register and then the second gives \((\beta_1,\beta_2)\) with the probability \(\|\psi^{\beta_1}\|^2\cdot|\psi^{\beta_1}_{\beta_2}|^2/\|\psi^{\beta_1}\|^2=|\psi_{\beta_1,\beta_2}|^2\), the same as measuring everything at once.

More generally, let \((\Pi_a)_{a\in A}\) be orthogonal projections of \(\mathbb C^B\) with \(\Pi_a\Pi_{a'}=0\) for \(a\ne a'\) and \(\sum_a\Pi_a=I\). The *measurement* \((\Pi_a)\) of a state \(\psi\) gives \(a\) with the probability \(\|\Pi_a\psi\|^2\), and then the state is \(\Pi_a\psi/\|\Pi_a\psi\|\). Measuring a register is the case \(\Pi_{\beta_1}=|\beta_1\rangle\langle\beta_1|\otimes I\), the projection onto the vectors \(|\beta_1\rangle\otimes\chi\).

These rules are the definition of the model. They are the rules of quantum mechanics for a system with finitely many levels; for the mathematics of this course they are simply definitions.

## 2. Query algorithms

Let \(n\ge1\). The input is a string \(x\in\{0,1\}^n\).

**Definition.** Let \(Z\) be a finite set and \(B=\{1,\dots,n\}\times\{0,1\}\times Z\); the three registers are the *index register*, the *bit register* and the *work register*. The *query* for the input \(x\) is the permutation map
\[
O_x\,|i,b,z\rangle=|i,\ b\oplus x_i,\ z\rangle .
\]
A *query algorithm with \(T\) queries* consists of a set \(Z\), a label \(\beta_0\in B\), unitary maps \(U_0,U_1,\dots,U_T\) of \(\mathbb C^B\) and a function \(\mathrm{out}\) from \(B\) to a set of outputs. On the input \(x\) its *final state* is
\[
\psi_x=U_T\,O_x\,U_{T-1}\,O_x\cdots O_x\,U_0\,|\beta_0\rangle ,
\]
and it *outputs* \(o\) with the probability \(\sum_{\beta:\ \mathrm{out}(\beta)=o}|(\psi_x)_\beta|^2\).

The maps \(U_j\) do not depend on \(x\). The query is its own inverse: \(O_xO_x=I\). The size of \(Z\) and the maps \(U_j\) are not restricted in any way.

**Definition.** Let \(f\) be a partial Boolean function with the domain \(\mathcal D\subseteq\{0,1\}^n\). A query algorithm *computes \(f\) with error at most \(\tfrac13\)* if for every \(x\in\mathcal D\) it outputs \(f(x)\) with a probability of at least \(\tfrac23\). \(Q(f)\) is the least number of queries of such an algorithm.

## 3. Algorithms that measure

The algorithms of this course are described as procedures: prepare a state, make queries, measure a register, and continue in a way that depends on the outcome, possibly with random choices. Such a procedure is not literally a query algorithm in the sense of Section 2. We define it precisely and show that it can be replaced by one.

**Definition.** A *measuring algorithm* on \(\mathbb C^B\), with \(B\) as in Section 2 and a start label \(\beta_0\), is a finite rooted tree. Every leaf carries an output. Every inner vertex \(v\) is of one of three kinds:

- a *unitary vertex*: it has one child and carries a unitary map \(U_v\) that does not depend on the input;
- a *query vertex*: it has one child;
- a *measuring vertex*: it carries a measurement \((\Pi_{v,a})_{a\in A_v}\) that does not depend on the input, and it has one child \(v_a\) for every \(a\in A_v\).

For an input \(x\), the vector \(\psi_v=\psi_v(x)\) of a vertex is defined from the root downward: \(\psi_{\mathrm{root}}=|\beta_0\rangle\); the child of a unitary vertex \(v\) has the vector \(U_v\psi_v\); the child of a query vertex has \(O_x\psi_v\); the child \(v_a\) of a measuring vertex has \(\Pi_{v,a}\psi_v\). The algorithm *reaches* the leaf \(v\) with the probability \(\|\psi_v(x)\|^2\), and it outputs the output of the leaf that it reaches. Its *number of queries* is the largest number of query vertices on a path from the root to a leaf.

**Lemma 3.1.** For every vertex \(v\), \(\|\psi_v\|^2\) is the sum of the \(\|\psi_c\|^2\) over the children \(c\) of \(v\). So the numbers \(\|\psi_v\|^2\) for the leaves are a probability distribution.

**Proof.** Unitary maps and the query preserve the norm. For a measuring vertex the vectors \(\Pi_{v,a}\psi_v\) are orthogonal to each other and add up to \(\psi_v\). \(\blacksquare\)

The definition expresses the rules of Section 1, applied step by step. The vector \(\psi_v\) is the state at \(v\) times the square root of the probability of arriving at \(v\): at a measuring vertex the outcome \(a\) has the conditional probability \(\|\Pi_{v,a}\psi_v\|^2/\|\psi_v\|^2\), and the state continues as \(\Pi_{v,a}\psi_v\) divided by its norm. The tree records how the procedure continues after each outcome.

*Random choices.* A procedure may choose \(a\in A\) at random with given probabilities \(p_a\): a unitary vertex prepares \(\sum_a\sqrt{p_a}\,|a\rangle\) in an unused register, and a measuring vertex measures this register.

*Classical data.* Outcomes of earlier measurements need no registers: the position in the tree records them, and the maps of the later vertices may depend on them.

**Theorem 3.2.** Let a measuring algorithm with at most \(T\) queries be given. There is a query algorithm with \(T\) queries that has, on every input, the same probabilities of the outputs.

So \(Q(f)\le T\) if a measuring algorithm with at most \(T\) queries computes \(f\) with error at most \(\tfrac13\).

**Proof.** Let \(N\) be the set of the vertices and \(d\) the largest number of vertices on a path. The new algorithm has two more registers in its work register: a *vertex register* with the labels \(N\) and a *spare register* with the labels \(\{1,\dots,n\}\times\{0,1\}\). Its start label is \((\beta_0,\mathrm{root},(1,0))\).

*Free sets.* Call a set \(G\subseteq N\) *free* if no vertex of \(G\) is an ancestor of another vertex of \(G\). For a free set \(G\) and an input \(x\) we consider states of the form
\[
\sum_{v\in G}\psi_v(x)\otimes|v\rangle\otimes|1,\sigma_v\rangle
\]
with bits \(\sigma_v\in\{0,1\}\). We call them *states of the form (3.1) for \(G\)*. The terms are orthogonal to each other, and the term of \(v\) has the norm \(\|\psi_v(x)\|\). The start state is of this form with \(G=\{\mathrm{root}\}\).

*A step without a query.* For a free set \(G\), let \(G'\) consist of the children of the unitary and measuring vertices of \(G\), together with the query vertices and the leaves of \(G\). The set \(G'\) is free. On the subspace of the vectors \(\sum_{v\in G}\chi_v\otimes|v\rangle\otimes\tau_v\) define a linear map \(J_G\) by its values on the vectors \(\chi\otimes|v\rangle\otimes\tau\) with \(v\in G\):

- if \(v\) is a unitary vertex with the child \(c\), the value is \(U_v\chi\otimes|c\rangle\otimes\tau\);
- if \(v\) is a measuring vertex, the value is \(\sum_a\Pi_{v,a}\chi\otimes|v_a\rangle\otimes\tau\);
- if \(v\) is a query vertex or a leaf, the value is \(\chi\otimes|v\rangle\otimes\tau\).

It preserves the inner product. For one \(v\) this holds because \(U_v\) is unitary and because \(\sum_a\langle\Pi_{v,a}\chi,\Pi_{v,a}\chi'\rangle=\langle\chi,\chi'\rangle\). The images for different \(v\in G\) are orthogonal, because they contain different labels of the vertex register: different vertices have different children, and a vertex of \(G\) is not a child of another vertex of \(G\). By Lemma 1.1, \(J_G\) is the restriction of a unitary map \(\widetilde J_G\), which does not depend on \(x\). It maps a state of the form (3.1) for \(G\) to a state of the form (3.1) for \(G'\).

Apply this step \(d\) times, each time for the current free set. After that the current free set consists of query vertices and leaves only.

*A step with a query.* Let \(G\) be a free set of query vertices and leaves. Let \(E_G\) be the permutation map that exchanges the index and bit registers with the spare register if the vertex register contains a leaf, and does nothing otherwise. Let \(M_G\) be a permutation map of the vertex register that maps every query vertex of \(G\) to its child and every leaf of \(G\) to itself; there is one, because these vertices are mapped to different vertices. Apply
\[
M_G\,E_G\,O_x\,E_G .
\]
For a query vertex \(v\in G\) with the child \(c\), the term \(\psi_v\otimes|v\rangle\otimes|1,\sigma\rangle\) becomes \(O_x\psi_v\otimes|c\rangle\otimes|1,\sigma\rangle=\psi_c\otimes|c\rangle\otimes|1,\sigma\rangle\). For a leaf \(v\in G\), the exchange puts \(|1,\sigma\rangle\) into the index and bit registers; the query changes it to \(|1,\sigma\oplus x_1\rangle\); the second exchange restores the registers of \(\psi_v\). The term becomes \(\psi_v\otimes|v\rangle\otimes|1,\sigma\oplus x_1\rangle\). So the result is a state of the form (3.1) for the free set that consists of the children of the query vertices of \(G\) and the leaves of \(G\).

*The algorithm.* Repeat \(T\) times: \(d\) steps without a query, then one step with a query. Then make \(d\) more steps without a query. This is a query algorithm with \(T\) queries; all other maps do not depend on \(x\). By induction, the current free set always meets every path from the root to a leaf in exactly one vertex, and after \(t\) steps with a query this vertex comes after at least \(t\) query vertices of the path or is a leaf. Every path has at most \(T\) query vertices. So at the end the free set is the set of all leaves, and the final state is
\[
\sum_{v\ \mathrm{leaf}}\psi_v(x)\otimes|v\rangle\otimes|1,\sigma_v\rangle .
\]
Let \(\mathrm{out}\) be the output of the leaf in the vertex register. The probability of an output \(o\) is the sum of \(\|\psi_v(x)\|^2\) over the leaves with the output \(o\). \(\blacksquare\)

The proof replaces every measurement by a copy of its outcome into the vertex register, which is never changed back. A branch that has finished cannot skip a query, because the query acts on the whole state; it spends the query on the spare register.

From here on, algorithms are described as procedures with measurements, and "an algorithm with at most \(T\) queries" means a measuring algorithm.

## 4. Queries at computed positions

In a query algorithm the position of a query is the content of the index register. In practice the position is computed from other registers.

**Lemma 4.1** (read queries). Let \(C\) be a finite set and \(\mathrm{loc}:C\to\{1,\dots,n\}\) a function. Let the work register contain a register with the labels \(C\) and a register with the labels \(\{0,1\}\). The map
\[
R_{\mathrm{loc}}\,|c,b\rangle=|c,\ b\oplus x_{\mathrm{loc}(c)}\rangle
\]
on these two registers is obtained with one query and permutation maps that do not depend on \(x\), on all states in which the index and bit registers are \(|1,0\rangle\); afterwards these two registers are \(|1,0\rangle\) again.

**Proof.** Let \(V_1\) be the permutation map \(|i\rangle|c\rangle\mapsto|i+\mathrm{loc}(c)-1\rangle|c\rangle\) on the index register and the register \(C\), with the addition modulo \(n\) in \(\{1,\dots,n\}\). Let \(V_2\) exchange the bit register with the register of \(b\). Then
\[
V_1^{-1}V_2\,O_x\,V_2V_1
\]
maps \(|1,0\rangle|c,b\rangle\) to \(|\mathrm{loc}(c),b\rangle|c,0\rangle\), then to \(|\mathrm{loc}(c),b\oplus x_{\mathrm{loc}(c)}\rangle|c,0\rangle\), then to \(|1,0\rangle|c,b\oplus x_{\mathrm{loc}(c)}\rangle\). \(\blacksquare\)

We call \(R_{\mathrm{loc}}\) a *read query*. It is its own inverse. The register \(C\) may consist of several registers, and \(\mathrm{loc}\) may be any function of their labels.

**Definition.** A *query circuit with \(q\) queries* is a product
\[
V_q\,R_q\,V_{q-1}\cdots R_1\,V_0
\]
of unitary maps \(V_j\) that do not depend on \(x\) and read queries \(R_j\), each with its own function \(\mathrm{loc}_j\) and its own registers. For every \(x\) it is a unitary map. Its inverse \(V_0^{-1}R_1\cdots R_qV_q^{-1}\) is a query circuit with \(q\) queries.

By Lemma 4.1 a query circuit with \(q\) queries is carried out with \(q\) queries in the sense of Section 2, and a measuring algorithm may use read queries in place of queries.

**Lemma 4.2.** Let \(\mathrm{loc}:C\to\{1,\dots,n\}\). Each of the following maps is obtained by a query circuit with two queries that uses one more register with the labels \(\{0,1\}\), which is \(|0\rangle\) before and after.

1. The *phase query* \(|c\rangle\mapsto(-1)^{x_{\mathrm{loc}(c)}}|c\rangle\).
2. For a subset \(C_0\subseteq C\), the *conditional read query*: \(|c,b\rangle\mapsto|c,b\oplus x_{\mathrm{loc}(c)}\rangle\) for \(c\in C_0\), and \(|c,b\rangle\mapsto|c,b\rangle\) for \(c\notin C_0\).

**Proof.** Read \(x_{\mathrm{loc}(c)}\) into the new register: \(|c\rangle|0\rangle\mapsto|c\rangle|x_{\mathrm{loc}(c)}\rangle\). For 1, apply the map \(|a\rangle\mapsto(-1)^a|a\rangle\) to the new register. For 2, apply the permutation map \(|c,b\rangle|a\rangle\mapsto|c,b\oplus a\rangle|a\rangle\) for \(c\in C_0\), and the identity for \(c\notin C_0\). Then read again; the new register returns to \(|0\rangle\). \(\blacksquare\)

## 5. Decision trees in superposition

**Lemma 5.1.** Let \(C\) be a finite set, and for every \(c\in C\) let \(A_c\) be a decision tree of depth at most \(q\) with outputs in \(\{0,1\}^t\). There is a query circuit with \(q\) queries on registers with the labels \(C\), \(\{0,1\}^q\) and \(\{0,1\}^t\) such that for every \(c\) and \(x\)
\[
\begin{aligned}
&|c\rangle|0\dots0\rangle|y\rangle\\
&\quad\longmapsto\ |c\rangle|a_1\dots a_q\rangle|y\oplus A_c(x)\rangle ,
\end{aligned}
\]
where \(a_1,\dots,a_q\) are the bits that \(A_c\) reads on the input \(x\) (after the tree is extended to exactly \(q\) queries on every path).

**Proof.** Extend every tree by further queries of the position \(1\) so that every path has \(q\) queries. The position of the \(j\)-th query of \(A_c\) is a function \(\mathrm{loc}_j(c,a_1,\dots,a_{j-1})\) of \(c\) and the earlier answers. For \(j=1,\dots,q\) apply the read query with the function \(\mathrm{loc}_j\) to the register of \(a_j\). Then apply the permutation map that adds the output, a function of \(c\) and \(a_1,\dots,a_q\), to the last register. \(\blacksquare\)

By linearity the circuit maps \(\sum_c\gamma_c|c\rangle|0\dots0\rangle|0\dots0\rangle\) to \(\sum_c\gamma_c|c\rangle|a(c,x)\rangle|A_c(x)\rangle\): the trees for all \(c\) are run at once. The registers of the answers are kept. Nothing is erased; the inverse circuit undoes the whole computation.

## 6. Two rules for probabilities

**Rule 6.1** (control registers). Let the space be \(\mathbb C^C\otimes\mathbb C^{B'}\), and for every \(c\in C\) let \(V_c\) be a unitary map of \(\mathbb C^{B'}\). The map \(V\) with \(V(|c\rangle\otimes\chi)=|c\rangle\otimes V_c\chi\) is unitary; we say that it is *controlled by the register \(C\)*. For a state \(\psi=\sum_c|c\rangle\otimes\psi^c\),
\[
V\psi=\sum_c|c\rangle\otimes V_c\psi^c .
\]
So measuring the register \(C\) after \(V\) gives \(c\) with the probability \(\|\psi^c\|^2\), the same probability as without \(V\); and then the other registers are in the state \(V_c\psi^c/\|\psi^c\|\). In words: the result is the same as if \(C\) had been measured first and \(V_c\) applied afterwards.

Products of maps controlled by \(C\) are controlled by \(C\). A read query whose target bit is not in \(C\) is controlled by \(C\), whether its function \(\mathrm{loc}\) depends on \(c\) or not. So a query circuit that never changes the register \(C\) is controlled by \(C\).

**Rule 6.2** (independent registers). Let the state be a product \(\psi_1\otimes\psi_2\in\mathbb C^{B_1}\otimes\mathbb C^{B_2}\). If a register of \(B_1\) and a register of \(B_2\) are measured, the two outcomes are independent, and each has the distribution that it has for its own factor. Indeed the entries of \(\psi_1\otimes\psi_2\) are the products of the entries of \(\psi_1\) and \(\psi_2\).

The two rules are combined as follows. Let \(V\) be controlled by \(C\) and act for each \(c\) as a product \(V_c^{(1)}\otimes\dots\otimes V_c^{(t)}\) on \(t\) registers, each of which contains a bit called its *result*. Apply \(V\) to \(\sum_c\gamma_c|c\rangle\otimes|0\rangle\otimes\dots\otimes|0\rangle\). Then the probability that the measurement gives \(c\) and the result \(1\) in all \(t\) registers is
\[
|\gamma_c|^2\prod_{j=1}^tp_j(c),
\]
where \(p_j(c)\) is the probability of the result \(1\) for the state \(V_c^{(j)}|0\rangle\).

## 7. Exercises

**7.1.** Show that \(O_x\) is a permutation map with \(O_xO_x=I\), and that for \(x\ne x'\) the maps \(O_x\) and \(O_{x'}\) are different.

**7.2.** Let \(n=2\) and \(f(x)=x_1\oplus x_2\). Show \(D(f)=2\) and \(Q(f)\le2\) by Lemma 5.1. Then show that one phase query to a suitable state determines \(f(x)\) with certainty.

**7.3.** Show \(Q(f)\le R(f)\) for every partial Boolean function.

**7.4.** In the proof of Theorem 3.2, a leaf uses the spare register for its queries. Why is the result not changed by the fact that the spare register then depends on \(x\)?

**7.5.** Let \(\psi=\sum_c\gamma_c|c\rangle\otimes|0\rangle\) and let \(V\) be controlled by \(C\) with \(V_c|0\rangle=\sqrt{1-p_c}\,|0\rangle+\sqrt{p_c}\,|1\rangle\). Find the probability that the second register gives \(1\), and the conditional distribution of \(c\) given this outcome.

## 8. Solutions

**7.1.** The map \((i,b,z)\mapsto(i,b\oplus x_i,z)\) is a bijection of \(B\) and is its own inverse, because \(b\oplus x_i\oplus x_i=b\). If \(x_i\ne x'_i\), the two maps differ on \(|i,0,z\rangle\).

**7.2.** A tree of depth \(1\) reads one bit, and the other bit changes \(f\); so \(D(f)=2\), and \(Q(f)\le2\) by Lemma 5.1 with a measurement of the output register (or by Exercise 7.3). For one phase query take \(C=\{1,2\}\), \(\mathrm{loc}(c)=c\) and the state \(\tfrac1{\sqrt2}(|1\rangle+|2\rangle)\). The phase query gives \(\tfrac1{\sqrt2}((-1)^{x_1}|1\rangle+(-1)^{x_2}|2\rangle)\), which is \(\pm\tfrac1{\sqrt2}(|1\rangle+|2\rangle)\) if \(f(x)=0\) and \(\pm\tfrac1{\sqrt2}(|1\rangle-|2\rangle)\) if \(f(x)=1\). These two states are orthogonal. A unitary map sends them to \(|1\rangle\) and \(|2\rangle\), and a measurement tells them apart. By Lemma 4.2 the phase query costs two queries; with the bit register in the state \(\tfrac1{\sqrt2}(|0\rangle-|1\rangle)\) a single read query has the same effect, so in fact \(Q(f)=1\).

**7.3.** Let a randomized algorithm of cost \(T\) be given: a distribution on trees \(A_c\), \(c\in C\), with probabilities \(p_c\). The measuring algorithm chooses \(c\) at random with these probabilities, then applies the circuit of Lemma 5.1 for the single tree \(A_c\) to \(|0\dots0\rangle|0\rangle\) and measures the last register. It makes at most \(T\) read queries and outputs \(A_c(x)\). By Theorem 3.2 and Lemma 4.1, \(Q(f)\le T\).

**7.4.** The terms of the state for different leaves have different labels in the vertex register. So they are orthogonal whatever the spare register contains, and the norm of each term, which is the probability of its leaf, does not depend on the spare register.

**7.5.** \(V\psi=\sum_c\gamma_c|c\rangle\otimes V_c|0\rangle\), and the entry of \(V_c|0\rangle\) at the label \(1\) is \(\sqrt{p_c}\). The outcome \(1\) has the probability \(P=\sum_c|\gamma_c|^2p_c\), and given this outcome \(c\) has the probability \(|\gamma_c|^2p_c/P\).

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Section 1 and the last paragraph of Section 3. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026

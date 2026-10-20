# Diagrams, densities and cycles over a finite field

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The final argument of the course (Lessons 14–18) repeats the transfer scheme of Lessons 7–9, with one essential difference. The functions to be compared are the exact Fourier transforms \(g_p\) of the residue supports, which carry no multiplicative-character phase, so anchor primes cannot separate the copies. Instead, a common list of auxiliary *spectator* primes is attached to every leaf of the binary tree of transfers, and at each spectator prime \(q\) the leaves contribute values \(g_q(y)\) at arguments \(y\in\mathbb F_q\) that are rational functions of the leaf variables. This lesson and the next prove the finite-field estimate needed there (Lemma 1.2). For two such *diagrams* whose leaf variables are coupled only through products over a few blocks, the correlation \(\mathbb E\,W_1\overline{W_2}\) tends to zero as \(q\to\infty\). The only hypotheses on \(g\) are \(g(0)=0\), \(\mathbb E|g|^2\le1\), and smallness of all mixed character correlations, which is the mixed flatness of Lesson 9. No pointwise bound on \(g\) is assumed.

This lesson defines the diagrams, proves the density bound \(\mathbb E|W|^2\le3^r\) (Section 2), reduces the correlation to a projection along a cycle (Section 3), and studies the autocorrelations that govern a single pair of sibling leaves (Section 4). Lesson 13 proves the remaining Fourier estimates.

**Prerequisites.** [*Anchor codes and decorrelation of higher characters*](anchor-codes-and-decorrelation-of-higher-characters.md), Section 6; finite Fourier analysis on \(\mathbb F_q\) and on \(\mathbb F_q^\times\).

## 1. Diagrams and the statement

Let \(q\) be an odd prime, \(U=\mathbb F_q^\times\), and \(e_q(x)=e^{2\pi ix/q}\). For a function \(f\) on \(\mathbb F_q\), \(\widehat f(a)=\frac1q\sum_xf(x)e_q(-ax)\). For a function on \(U\), its *Mellin coefficients* are \(\frac1{q-1}\sum_{t\in U}f(t)\overline{\chi(t)}\), \(\chi\in\widehat U\). Characters, the principal one included, are extended by zero at zero. All \(L^2\) norms use probability measure unless a counting sum is written. Throughout, \(g\colon\mathbb F_q\to\mathbb C\) satisfies \(g(0)=0\), \(\mathbb E_{x\in\mathbb F_q}|g(x)|^2\le1\), and
\[
\begin{aligned}
\epsilon_q&=\max_{\chi\in\widehat U,\ a\in\mathbb F_q}\Bigl|\mathbb E_{x\in\mathbb F_q}g(x)\chi(x)\\
&\quad e_q(ax)\Bigr|.\quad(1.1)
\end{aligned}
\]
The same parameter serves for \(\overline g\), since conjugation replaces \((\chi,a)\) by \((\overline\chi,-a)\), and \(\epsilon_q\le1\) by Cauchy–Schwarz.

**Diagrams.** A *diagram of depth \(l\)* uses a full ordered binary tree with \(r=2^l\) leaves. The *leaf variables* \(M_i\) take values in \(U\); for a node \(n\), \(M_n\) is the product of the leaf variables below \(n\). The diagram has fixed *frequencies* \(s_n\in U\) at all nodes, a constant \(D'\in U\), and unit constants \(C_{n,+},C_{n,-},u_n\) at the internal nodes. Each internal node \(n\) has an ordered pair of *current entries* \(X_{n,+},X_{n,-}\): fixed units at the root, propagated downwards as follows. At an internal node \(n\), with children \(n,+\) and \(n,-\),
\[
\begin{aligned}
H_{n,\pm}&=X_{n,\pm}\,C_{n,\pm}\,M_{n,\pm},\\
p_n&=\frac{s_{n,+}H_{n,-}-s_{n,-}H_{n,+}}{s_nu_n},\\
y_n&=\frac{s_n}{D'H_{n,+}H_{n,-}},\\
y_{n,\pm}&=\frac{s_{n,\pm}}{D'\,p_n\,u_n\,H_{n,\pm}},\quad(1.2)
\end{aligned}
\]
and the current entries of an internal child \(n,\pm\) are \((p_n,X_{n,\pm})\). The constants are required to be *consistent*: \(C_{n,\pm,+}C_{n,\pm,-}=u_nC_{n,\pm}\), which is equivalent to \(H_{n,\pm,+}H_{n,\pm,-}=p_nu_nH_{n,\pm}\). It makes the argument \(y_{n,\pm}\) computed at \(n\) agree with the child's own \(y\). All operations take place in \(\mathbb F_q\). If some \(p_n=0\), the diagram value is \(0\) and no division by \(p_n\) is made; such points are *invalid*.

On valid points, the *value* \(W\) is the product over the leaves \(i\) of \(g(y_i)\) or \(\overline{g(y_i)}\), with opposite conjugations on the two leaves of every bottom sibling pair; the choices on different pairs are arbitrary. For depth \(0\), put \(y_1=c/M_1\) with a fixed \(c\in U\), and \(W=g(y_1)\) or its conjugate.

These formulas are the reduction modulo a spectator prime of the coefficient recursion of Lesson 14. The point is their shape: an argument at a node is a difference of the arguments at its children, and the ratio of the children's arguments is a fixed unit times the inverse square of a leaf product.

**Lemma 1.1** (difference and ratio). On valid points,
\[
\begin{gathered}
y_n=y_{n,+}-y_{n,-},\\
\frac{y_{n,+}}{y_{n,-}}=\frac{s_{n,+}}{s_{n,-}}\cdot\frac{H_{n,-}}{H_{n,+}}.\quad(1.3)
\end{gathered}
\]

*Proof.* By (1.2),
\[
\begin{aligned}
y_{n,+}-y_{n,-}&=\frac1{D'p_nu_n}\\
&\quad \cdot\frac{s_{n,+}H_{n,-}-s_{n,-}H_{n,+}}{H_{n,+}H_{n,-}}\\
&=\frac{s_nu_np_n}{D'p_nu_nH_{n,+}H_{n,-}}\\
&=y_n .
\end{aligned}
\]
The ratio is immediate. \(\square\)

**Lemma 1.2** (tree comparison [OpenAI-013, Lemma 6.1]). In a single diagram with independent uniform leaf variables,
\[
\mathbb E|W|^2\le3^r.
\tag{1.4}
\]
Let two diagrams of the same depth \(l\) be given, with possibly different unit parameters and conjugation choices. Partition the leaves of each into \(b\) nonempty sets, the sets of the two diagrams being paired, and give the two collections of leaf variables the uniform distribution on the subgroup of \(U^r\times U^r\) defined by equality of the products over paired sets. If \(l\ge2\) and \(b\le3r/4\), then
\[
\begin{aligned}
&\bigl|\mathbb E\,W_1\overline{W_2}\bigr|\\
&\quad \le C_l\bigl(\epsilon_q+q^{-1/4}\bigr),\quad(1.5)
\end{aligned}
\]
with \(C_l\) depending only on \(l\).

## 2. The density bound

**Exposure.** Under independent uniform leaf variables, expose first the product of all leaf variables, then, going down the tree, the product \(M_{n,+}\) at each split. Given the parent product \(M_n\) and all earlier splits, \(M_{n,+}\) is uniform on \(U\) and determines \(M_{n,-}=M_n/M_{n,+}\): the leaves below \(n,+\) and below \(n,-\) form disjoint sets of independent uniform units. The root argument \(s_{\mathrm{root}}/(D'H_+H_-)\) is a fixed unit times the inverse of the total product, hence uniform on \(U\). At a split, the current entries are already known, and by (1.3) and \(M_{n,-}=M_n/M_{n,+}\),
\[
\frac{y_{n,+}}{y_{n,-}}=\text{(a known unit)}\cdot M_{n,+}^{-2}.
\]
Given \(y_n\), the ratio \(\rho=y_{n,+}/y_{n,-}\) determines the pair, since \(y_{n,-}=y_n/(\rho-1)\) and \(y_{n,+}=\rho y_{n,-}\). Squaring is two-to-one on \(U\), so a prescribed valid ordered pair \((y_{n,+},y_{n,-})\) has conditional probability at most \(2/(q-1)\).

**Proposition 2.1** ([OpenAI-013, (6.3)]). On the valid points, the joint law of the leaf arguments \((y_i)\) is at most \(2^{r-1}\) times the law of \(r\) independent uniform elements of \(U\). The same holds for the arguments at the nodes of any fixed level, with \(2^{r-1}\) replaced by a constant depending only on \(l\). Consequently (1.4) holds.

*Proof.* A vector of leaf arguments determines all arguments above it by (1.3). Its probability is at most \(\frac1{q-1}\bigl(\frac2{q-1}\bigr)^{r-1}\): the root argument has probability \(\frac1{q-1}\), and each of the \(r-1\) splits contributes at most \(\frac2{q-1}\). Stopping the exposure at any level gives the second assertion. Since \(g(0)=0\), \(\mathbb E_{y\in U}|g(y)|^2=\frac q{q-1}\mathbb E_{\mathbb F_q}|g|^2\le\frac q{q-1}\), so
\[
\mathbb E|W|^2\le2^{r-1}\Bigl(\frac q{q-1}\Bigr)^r\le3^r .
\]
\(\square\)

These are bounds for integrals of nonnegative functions. They use the \(L^2\) bound on \(g\) only, not any pointwise bound.

## 3. The cycle reduction

Assume \(l\ge2\) and \(b\le3r/4\). The coupled law of Lemma 1.2 has an equivalent description: choose independent uniform *component totals*, one for each paired set; then, independently in each diagram and given the totals, choose its leaf variables uniformly among those with the prescribed product on each set. Every fibre of the product map has the same size, so this is the uniform law on the subgroup. Each diagram, taken alone, has independent uniform leaf variables.

**A cycle.** The tree of depth \(l\ge2\) groups its leaves into \(r/4\) *bottom quartets*, the four leaves below a node of level \(2\). In the first diagram form the bipartite multigraph whose vertices are its \(b\) component sets and its \(r/4\) quartets, with one edge for each leaf, joining the leaf's component to its quartet. It has \(r\) edges and at most \(b+r/4\le r\) vertices, none isolated. A forest has fewer edges than vertices, so the graph contains a cycle, possibly two parallel edges. Choose a simple cycle. Multiply the leaf variables on it alternately by \(z\) and \(z^{-1}\), \(z\in U\): every component product and every quartet product is preserved, since each vertex of the cycle meets two of its edges, one of each kind. Let \(\mathcal P\) be the average over \(z\in U\) of this action. It is an orthogonal projection on \(L^2(U^r)\).

**Proposition 3.1** (the cycle reduction [OpenAI-013, (6.6)]).
\[
\bigl|\mathbb E\,W_1\overline{W_2}\bigr|\le3^{r/2}\,\|\mathcal PW_1\|_2,
\tag{3.1}
\]
where the norm is taken for independent uniform leaf variables of the first diagram.

*Proof.* Let \(\mathcal T\) be the collection of component totals. The action preserves each fibre of \(\mathcal T\) and its uniform measure, so \(\mathbb E(W_1\mid\mathcal T)=\mathbb E(\mathcal PW_1\mid\mathcal T)\). Given \(\mathcal T\), the two diagrams are independent, so \(\mathbb E\,W_1\overline{W_2}=\mathbb E\bigl[\mathbb E(W_1\mid\mathcal T)\,\overline{\mathbb E(W_2\mid\mathcal T)}\bigr]\). Cauchy–Schwarz, the contraction of conditional expectations on \(L^2\), and (1.4) give
\[
\begin{aligned}
\bigl|\mathbb E\,W_1\overline{W_2}\bigr|&\le\|\mathcal PW_1\|_2\,\|W_2\|_2\\
&\le3^{r/2}\|\mathcal PW_1\|_2 .
\end{aligned}
\]
\(\square\)

**Mellin expansion along the cycle.** Under independent uniform leaf variables, condition on the products of all bottom quartets. These determine all the ancestor data, including the validity of the ancestors, and if an ancestor is invalid the value is \(0\). Otherwise the interiors of the quartets are independent, each uniform on its product fibre, and \(W\) is the product of the *quartet values*, each a function of its own four leaves. A quartet on the cycle contains two *moving* leaves. Fix its two *held* leaves and take one moving leaf as a coordinate on \(U\); the quartet product determines the other. Expand the quartet value in Mellin characters of this coordinate, with coefficients \(a_{j,\rho}\) for the \(j\)-th quartet of the cycle. The action multiplies the coordinate by \(z\) or \(z^{-1}\), so the projection \(\mathcal P\) keeps exactly the products of terms whose characters satisfy
\[
\begin{gathered}
\prod_{j=1}^t\rho_j^{\delta_j}=1,\\
\delta_j\in\{1,-1\},\quad(3.2)
\end{gathered}
\]
where \(t\) is the number of quartets on the cycle.

**What remains to prove.** Consider one bottom quartet with its product and all ancestor data fixed. On valid ancestor data its current entries and its parent argument \(y\) are fixed units. Choose two of its leaves to move by reciprocal multiplication, and hold the other two; write \(a_\rho\) for the Mellin coefficients of the quartet value in the moving coordinate. Lesson 13 constructs nonnegative functions \(B_\rho(y)\), depending on \(g\) and \(q\) but not on the ancestor data or the unit parameters, such that
\[
\begin{gathered}
\mathbb E_{\mathrm{held}}|a_\rho|^2\le B_\rho(y),\\
\sup_\rho\mathbb E_{y\in U}B_\rho(y)\ll\epsilon_q^2+q^{-1/2},\\
\sum_\rho\mathbb E_{y\in U}B_\rho(y)\ll1,\quad(3.3)
\end{gathered}
\]
where the held average is over the two held leaves, independent and uniform given the quartet product, and a nonnegative \(B_0(y)\) of bounded mean that dominates the conditional second moment of a quartet off the cycle. Finitely many orientations and conjugation choices occur; adding their majorants keeps (3.3).

In (3.2) one character is determined by the others. Lesson 13 uses the small supremum in (3.3) for that one, the bounded sum for the others, and \(B_0\) for the quartets off the cycle.

## 4. Autocorrelations of a bottom pair

Fix \(\sigma\in\{1,-1\}\) and \(g_*\in\{g,\overline g\}\). For \(d\in U\) and \(t\in U\setminus\{1\}\) put
\[
\begin{gathered}
x=\frac{\sigma dt}{t-1},\\
z=\frac{\sigma d}{t-1},\\
h(d,t)=g_*(x)\,\overline{g_*(z)},\quad(4.1)
\end{gathered}
\]
and \(h(d,t)=0\) if \(d=0\) or \(t\in\{0,1\}\). On valid arguments \(x-z=\sigma d\) and \(t=x/z\): this is the value of a bottom sibling pair with parent argument \(\sigma d\) and child ratio \(t\), by (1.3). Put
\[
R_*(d)=\mathbb E_{t\in U}|h(d,t)|^2\qquad(d\in U).
\]
The map \((d,t)\mapsto(x,z)\) is a bijection from the valid pairs onto the ordered pairs of distinct units, so
\[
\begin{aligned}
\mathbb E_{d\in U}R_*(d)&=\frac1{(q-1)^2}\\
&\quad \sum_{\substack{x,z\in U\\x\ne z}}|g_*(x)|^2|g_*(z)|^2\\
&\le\Bigl(\frac q{q-1}\Bigr)^2 .\quad(4.2)
\end{aligned}
\]

**The Mellin coefficients.** For \(d\ne0\) and \(\chi\in\widehat U\), the Mellin coefficient of \(t\mapsto h(d,t)\) is
\[
\begin{aligned}
P_\chi(d)&=\frac q{q-1}\,\mathbb E_{x\in\mathbb F_q}(g_*\overline\chi)(x)\\
&\quad \,\overline{(g_*\overline\chi)(x-\sigma d)} .\quad(4.3)
\end{aligned}
\]
Indeed, substitute \(t=x/(x-\sigma d)\): as \(t\) runs over \(U\setminus\{1\}\), \(x\) runs over \(\mathbb F_q\setminus\{0,\sigma d\}\), and \(\overline\chi(t)=\overline\chi(x)\chi(x-\sigma d)\); the two excluded values of \(x\) contribute zero to (4.3). Use (4.3) also to *define* \(P_\chi(0)\); this is not the Mellin coefficient of the zero function \(h(0,\cdot)\).

Let \(w_\chi(a)=\widehat{P_\chi}(a)\) be the additive Fourier transform in \(d\), and \(r_\chi=\sum_aw_\chi(a)^2\). With \(G=g_*\overline\chi\), the substitution \(y=x-\sigma d\) in the autocorrelation gives
\[
\begin{gathered}
w_\chi(a)=\frac q{q-1}\bigl|\widehat G(\sigma a)\bigr|^2\ge0,\\
\begin{aligned}
P_\chi(0)&=\sum_aw_\chi(a)\\
&=\frac q{q-1}\,\mathbb E|g|^2 .
\end{aligned}\quad(4.4)
\end{gathered}
\]

**Lemma 4.1** ([OpenAI-013, (6.11) and (6.12)]).
\[
\begin{gathered}
\sum_aw_\chi(a)\le\frac q{q-1},\\
\max_{\chi,a}w_\chi(a)\le\frac q{q-1}\epsilon_q^2,\\
\max_\chi r_\chi\le\Bigl(\frac q{q-1}\Bigr)^2\epsilon_q^2,\\
\sum_\chi r_\chi\le\frac{2q}{q-1}\le3 .\quad(4.5)
\end{gathered}
\]

*Proof.* The first two follow from (4.4) and the definition (1.1), since \(\widehat G(\sigma a)=\mathbb E_xg_*(x)\overline\chi(x)e_q(-\sigma ax)\). Then \(r_\chi\le\max_aw_\chi(a)\cdot\sum_aw_\chi(a)\). For the last, Parseval in \(d\) gives \(r_\chi=\frac1q\sum_{d\in\mathbb F_q}|P_\chi(d)|^2\). For \(d\ne0\), Mellin Parseval gives \(\sum_\chi|P_\chi(d)|^2=R_*(d)\). At \(d=0\) each of the \(q-1\) characters has \(P_\chi(0)=\frac q{q-1}\mathbb E|g|^2\le\frac q{q-1}\). By (4.2),
\[
\begin{aligned}
\sum_\chi r_\chi&\le\frac1q\Bigl((q-1)\Bigl(\frac q{q-1}\Bigr)^2\\
&\quad +(q-1)\Bigl(\frac q{q-1}\Bigr)^2\Bigr)\\
&=\frac{2q}{q-1}.
\end{aligned}
\]
\(\square\)

**Lemma 4.2** (pulling back along squares [OpenAI-013, (6.13)]). Let \(f(t)=\sum_\chi c_\chi\chi(t)\) on \(U\), \(K\in U\) and \(\rho\in\widehat U\). Then
\[
\Bigl|\mathbb E_{z\in U}f(Kz^{\pm2})\,\overline{\rho(z)}\Bigr|^2\le2\sum_{\chi^{\pm2}=\rho}|c_\chi|^2 .
\]
Moreover, for nonnegative integrands, the uniform measure on a coset of the squares in \(U\) is at most twice the uniform measure on \(U\).

*Proof.* By orthogonality the left side is \(|\sum_{\chi^{\pm2}=\rho}c_\chi\chi(K)|^2\). Since \(U\) is cyclic of even order, the squaring map on \(\widehat U\) has a kernel of size \(2\), so the sum has at most two terms; apply Cauchy–Schwarz. A coset of the squares has \((q-1)/2\) elements. \(\square\)

These are the local tools. Lesson 13 combines them with an operator bound for the affine group of \(\mathbb F_q\) to construct the majorants \(B_\rho\) and complete the proof of Lemma 1.2.

## 5. Exercises

**5.1.** Check the consistency condition: show that \(C_{n,\pm,+}C_{n,\pm,-}=u_nC_{n,\pm}\) is equivalent to \(H_{n,\pm,+}H_{n,\pm,-}=p_nu_nH_{n,\pm}\), and that it makes the two formulas for the argument of an internal child agree.

**5.2.** For a diagram of depth \(1\) (two leaves), compute the leaf arguments in terms of the total product \(M\) and the split \(M_+\), and verify directly that a prescribed pair of leaf arguments has probability at most \(2/(q-1)^2\).

**5.3.** Show that in the bipartite multigraph of Section 3 a cycle exists already when \(b<3r/4+1\), and give an example with \(b=3r/4+1\), \(l=2\), in which the graph is a forest.

**5.4.** Prove (4.4): \(\widehat{P_\chi}(a)=\frac q{q-1}|\widehat G(\sigma a)|^2\).

## 6. Solutions

**5.1.** The current entries of the child \(n,\pm\) are \((p_n,X_{n,\pm})\), so \(H_{n,\pm,+}H_{n,\pm,-}\)\(=p_n\,X_{n,\pm}\,C_{n,\pm,+}C_{n,\pm,-}\,M_{n,\pm}\), using \(M_{n,\pm,+}M_{n,\pm,-}=M_{n,\pm}\). This equals \(p_nu_nH_{n,\pm}=p_nu_nX_{n,\pm}C_{n,\pm}M_{n,\pm}\) exactly when \(C_{n,\pm,+}C_{n,\pm,-}=u_nC_{n,\pm}\). The child's own argument is \(s_{n,\pm}/(D'H_{n,\pm,+}H_{n,\pm,-})\), and the parent's formula gives \(s_{n,\pm}/(D'p_nu_nH_{n,\pm})\); they agree under this condition.

**5.2.** With root entries \(X_\pm\) and constants \(C_\pm\), \(H_+=X_+C_+M_+\) and \(H_-=X_-C_-M/M_+\). The root argument is \(s/(D'X_+X_-C_+C_-M)\), and \(y_+/y_-=\frac{s_+X_-C_-}{s_-X_+C_+}\,M\,M_+^{-2}\). The probability that \(M\) takes a prescribed value is \(1/(q-1)\), and given \(M\), at most two values of \(M_+\) give a prescribed ratio. So the probability is at most \(2/(q-1)^2\).

**5.3.** The graph has \(r\) edges and \(b+r/4\) vertices. If it were a forest, \(r\le b+r/4-1\), that is \(b\ge3r/4+1\). For \(l=2\), \(r=4\): one quartet and \(b=4\) singleton components give a star with four edges, a tree.

**5.4.** \(\widehat{P_\chi}(a)=\frac q{q-1}\mathbb E_d\mathbb E_xG(x)\overline{G(x-\sigma d)}\)\(e_q(-ad)\). Put \(y=x-\sigma d\), so \(d=\sigma(x-y)\) and, as \(d\) runs over \(\mathbb F_q\) for fixed \(x\), \(y\) runs over \(\mathbb F_q\). Then the double average is \(\mathbb E_xG(x)e_q(-\sigma ax)\)\(\cdot\overline{\mathbb E_yG(y)e_q(-\sigma ay)}=|\widehat G(\sigma a)|^2\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 6: Lemma 6.1, the diagrams and their elementary density bound, the cycle reduction, and bottom-pair autocorrelations. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026

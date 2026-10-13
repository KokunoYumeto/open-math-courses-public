# Clean children and repetition

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two decoders output bilinear forms \(F_L\) and \(F_R\), and with a fixed probability they agree on the projected space while \(F_L(x,y)=z(xy)\) has a bounded rank. This lesson shows that such an agreement is an unlikely event when the base game has a small value and the node \(D_i\) has many children. A form \(z(xy)\) of rank at most \(s\) with \(z(1)=1\) defines at every leaf a list of an odd number of at most \(s\) answers of the base game, and the agreement of the two forms makes the lists of the two sides fit together along the edge of the base game at this leaf. So the decoders play a game on lists at every projected leaf.

To use parallel repetition one needs independent rounds. They are found at the *clean* children of \(D_i\): marked children all of whose random functions are zero. The probability that a marked child is clean does not depend on its questions. So, after everything else is made public, the edges of the base game at one leaf of each clean child are independent with their original law, and each player can compute the data of its decoder from the public data and its own questions at these leaves. If there are \(k\) clean children, the agreement implies that the players win \(k\) independent rounds of the game on lists.

- Odd lists and the game on lists (Lemma 1.1).
- The lists of a form (Lemma 2.1).
- Clean children and the law of their edges (Lemma 3.1).
- The data of the decoders from public data and own questions (Lemma 4.1).
- The bound for the agreement (Proposition 5.1).

The lesson follows [OpenAI-G, Section 7]. It continues [From tested rank to full rank](from-tested-rank-to-full-rank.md). It uses the decoders and their data from [The heavy list and the two decoders](the-heavy-list-and-the-two-decoders.md), the modified law of [Changing the law of the tests](changing-the-law-of-the-tests.md), the function spaces and keys of [The tree of function spaces and the questions](the-tree-of-function-spaces-and-the-questions.md), and the base game, Lemma 1.1 and the hypothesis (PR) of [Projection games and the base game](projection-games-and-the-base-game.md).

## 1. Odd lists

For a finite nonempty set \(\Lambda\) and \(s\ge1\) let \(\mathcal O_s(\Lambda)\) be the set of the subsets \(L\subset\Lambda\) with an odd number of elements, at most \(s\). For a map \(\pi:\Lambda\to\Gamma\) and \(L\subset\Lambda\) let \(\pi_{\mathrm{odd}}(L)\) be the set of the \(b\in\Gamma\) for which the number \(|L\cap\pi^{-1}(b)|\) is odd.

**The game on lists.** Let \(G\) be a projection game with the answer sets \(L_u\), \(R_v\) and the maps \(\pi_e\). The game \(G_{\mathrm{odd},s}\) has the same questions, the same edges and the same law on them. Its answer sets are \(\mathcal O_s(L_u)\) and \(\mathcal O_s(R_v)\), and the map of the edge \(e\) is \((\pi_e)_{\mathrm{odd}}\).

**Lemma 1.1.** The map \(\pi_{\mathrm{odd}}\) sends \(\mathcal O_s(\Lambda)\) into \(\mathcal O_s(\Gamma)\). So \(G_{\mathrm{odd},s}\) is a projection game, and
\[
\operatorname{val}(G_{\mathrm{odd},s})\le s^2\operatorname{val}(G).
\]

**Proof.** Let \(L\in\mathcal O_s(\Lambda)\). The numbers \(|L\cap\pi^{-1}(b)|\), \(b\in\Gamma\), have the sum \(|L|\), which is odd; so an odd number of them is odd. Every \(b\in\pi_{\mathrm{odd}}(L)\) has a preimage in \(L\), and different \(b\) have different preimages, so \(|\pi_{\mathrm{odd}}(L)|\le|L|\le s\).

Take a labeling of \(G_{\mathrm{odd},s}\) with the largest probability. Let each player of \(G\) choose a uniform element of the list at its question, independently. If the labeling satisfies the edge \(e\), the list \(R\) on the right is \((\pi_e)_{\mathrm{odd}}(L)\) for the list \(L\) on the left; every element of \(R\) has a preimage in \(L\), so the pair of chosen answers satisfies \(e\) in \(G\) with a probability of at least \(1/(|L|\,|R|)\ge s^{-2}\). By Lemma 1.1 of the lesson on projection games, the players win \(G\) with a probability of at most \(\operatorname{val}(G)\). So \(s^{-2}\operatorname{val}(G_{\mathrm{odd},s})\le\operatorname{val}(G)\). \(\blacksquare\)

## 2. The lists of a form

Work with the levels \(i<j\), the law \(\mathbb P_i\), the spaces \(H_i=H_{D_i}(E)\), \(H_i'=H_{D_i}(O)\) and the decoders of the lesson on the heavy list. Let \(\lambda\) be a leaf below \(D_i\). Its answer set for \(E\) is \(\Lambda_\lambda=\Omega_\lambda(E)\), the answer set of its left question in the base game. For \(a\in\Lambda_\lambda\) let \(e_a\) be the function on \(\Omega(E)\) that is \(1\) if the argument at the leaf \(\lambda\) is \(a\), and \(0\) otherwise. It lies in \(H_\lambda(E)\), hence in \(H_i\), by Lemma 2.1 of the lesson on the tree of function spaces. These functions satisfy
\[
\begin{gathered}
e_ae_b=0\ (a\ne b),\qquad e_a^2=e_a,\\
\sum_ae_a=1 .
\end{gathered}
\]
If the leaf \(\lambda\) is replaced in \(O\), with the map \(\pi_\lambda:\Lambda_\lambda\to\mathbb F^t\) of its edge, let \(e'_b\in H_i'\), for \(b\in\mathbb F^t\), be the function on \(\Omega(O)\) that is \(1\) if the argument at \(\lambda\) is \(b\). Read on \(\Omega(E)\) it is
\[
e'_b=\sum_{a:\ \pi_\lambda(a)=b}e_a .
\]

**Definition.** For a bilinear form \(F\) on \(H_i\), the *list* of \(F\) at \(\lambda\) is the set of the \(a\in\Lambda_\lambda\) with \(F(e_a,e_a)=1\). For a bilinear form \(F'\) on \(H_i'\) and a replaced leaf \(\lambda\), the list of \(F'\) at \(\lambda\) is the set of the \(b\in\mathbb F^t\) with \(F'(e'_b,e'_b)=1\).

**Lemma 2.1.** Let \(F(x,y)=z(xy)\) with a linear functional \(z\) on \(H_i^2\), \(z(1)=1\), and \(\operatorname{rank}F\le s\).

1. The list \(L\) of \(F\) at every leaf \(\lambda\) below \(D_i\) lies in \(\mathcal O_s(\Lambda_\lambda)\).
2. If \(\lambda\) is replaced in \(O\) and \(F'\) is a form on \(H_i'\) that is equal to \(F\) on \(H_i'\times H_i'\), then the list of \(F'\) at \(\lambda\) is \((\pi_\lambda)_{\mathrm{odd}}(L)\).

**Proof.** (1) The matrix \((F(e_a,e_b))_{a,b}=(z(e_ae_b))_{a,b}\) is diagonal with the entries \(d_a=z(e_a)\). Its rank is the number of the \(a\) with \(d_a=1\), and it is at most \(\operatorname{rank}F\le s\). The sum of the \(d_a\) is \(z(1)=1\) in \(\mathbb F\), so this number is odd. (2) By bilinearity and \(F(e_a,e_{a'})=0\) for \(a\ne a'\),
\[
F'(e'_b,e'_b)=\sum_{a:\ \pi_\lambda(a)=b}d_a ,
\]
which is \(1\) exactly if an odd number of elements of \(L\) is mapped to \(b\). \(\blacksquare\)

**The extraction rule.** Fix an order of the answers of every question of the base game. A player who has a form, a leaf and its own question at the leaf computes the list of the form at the leaf. If the list has an odd number of elements, at most \(s\), the player outputs it; otherwise the player outputs the list that consists of the first answer of the question. The output is an element of \(\mathcal O_s\) of the answer set in every case. By Lemma 2.1, in the situation of this lemma the outputs of the two sides are \(L\) and \((\pi_\lambda)_{\mathrm{odd}}(L)\): the constraint of the game on lists at the edge of the leaf is satisfied.

## 3. Clean children

In this lesson \(\mathbb P_i\) is used with the \(T=T_i\) calls at \(D_i\) that the arrays at \(D_d,\dots,D_i\) need (Lemma 2.1 of the lesson on changing the law). The data of the two decoders are computed from these calls, from the exterior data, from the arrays below \(D_i\), and from \(E\), \(O\), \(A\), \(a_i\). The additional calls of the earlier lessons served comparisons of laws; without them the law of the data and of the outputs of the decoders is the same.

The law \(\mathbb P_i\) is described in the following form. Let \(m\) be the number of the leaves below a child of \(D_i\), and \(\mu\) the law of an edge of the base game.

- *The exterior* \(\mathcal X\): the questions of \(E\) at the leaves that are not below \(D_i\), the path to \(D_i\), the exterior data \(\Xi_i\), the map \(A\) and the vector \(a_i\).
- For every child \(C\) of \(D_i\), independently of the exterior and of the other children: a *mark* with the probability \(\beta=n_i^{-2/3}\); an edge of the base game with the law \(\mu\) at each of the \(m\) leaves below \(C\), independently; its left question is the question of \(E\) at the leaf, and if \(C\) is marked, its right question is the question of \(O\) at the leaf; \(T\) independent uniform *contributions* in \(H_C(O)^2\), one for every call; and an independent uniform array in the space of \(O\) at every node below \(C\), or equal to \(C\), that is not a leaf.

The call number \(q\) at \(D_i\) is the sum of the contributions number \(q\) of all children. This is the law \(\mathsf M_i\) of the lesson on changing the law, with an edge drawn also at the leaves below unmarked children, where it is not used.

**Definition.** A child \(C\) of \(D_i\) is *clean* if it is marked, all its \(T\) contributions are \(0\), and all arrays at the nodes below \(C\) or equal to \(C\) are \(0\). The *designated leaf* of a child is its first leaf in the order of the tree.

For a marked child \(C\), every leaf below \(C\) has the answer set \(\mathbb F^t\) in \(O\), whatever its question is: \(t\) variable slots, which are separate factors. So the domains \(\Omega_D(O)\) of the nodes \(D\) below \(C\), and with them the spaces \(H_D(O)\) and \(H_C(O)^2\), are the same for all marked children and all questions, up to the names of the slots. Let
\[
\begin{aligned}
p_0&=2^{-e_0},\\
e_0&=T\dim H_C(O)^2\\
&\quad+\sum_D\ell_{\operatorname{level}(D)}\dim H_D(O),
\end{aligned}
\]
where the sum is over the nodes \(D\) below \(C\) or equal to \(C\) that are not leaves. The number \(p_0>0\) depends on \(t\), on \(T\), and on the numbers \(\ell_p\), \(n_p\) with \(p<i\). It does not depend on \(n_i\), on the numbers \(n_p\) with \(p>i\), or on the formula.

**Lemma 3.1.** Under \(\mathbb P_i\), given the exterior:

1. the children are clean independently of each other, each with the probability \(\beta p_0\);
2. let the *public data* consist of the exterior, of the set \(\mathcal K\) of the clean children, of the marks, edges, contributions and arrays of all children that are not clean, and of the edges at the leaves of the clean children other than their designated leaves. Given the public data, the edges at the designated leaves of the clean children are independent, and each has the law \(\mu\).

**Proof.** Fix a child \(C\) and a tuple \(\mathbf e\) of edges at its leaves. Given that \(C\) is marked and has these edges, its contributions and arrays are independent and uniform in spaces whose dimensions add up to \(e_0\); so all of them are \(0\) with the probability \(p_0\). This number does not depend on \(\mathbf e\). Therefore, given the exterior, the probability that \(C\) has the edges \(\mathbf e\) and is clean is
\[
\mu^{\otimes m}(\mathbf e)\cdot\beta\,p_0 .
\]
The children are independent given the exterior, which gives (1). The formula also shows that, given that \(C\) is clean, its \(m\) edges are independent with the law \(\mu\). Since the children are independent, this remains so when the set of the clean children and all data of the other children are given; and when the edges at the other leaves of \(C\) are given, the edge at the designated leaf still has the law \(\mu\). \(\blacksquare\)

It is essential that \(p_0\) is the same number for all edges. A probability of the event "clean" that depended on the questions of the child would change the law of the questions of the clean children.

## 4. The data of the decoders

Fix a value of the public data, with the set \(\mathcal K\) of clean children, and let \(k=|\mathcal K|\). For \(C\in\mathcal K\) let \((u_C,v_C,\pi_C)\) be the edge at the designated leaf of \(C\): the left question \(u_C\), the right question \(v_C\), and the map \(\pi_C\). By Lemma 3.1 these are \(k\) independent edges of the base game.

**Lemma 4.1.** Given the public data,

1. the left data of the lesson on the heavy list are a function of the public data and of the left questions \((u_C)_{C\in\mathcal K}\);
2. the right data are a function of the public data and of the right questions \((v_C)_{C\in\mathcal K}\);
3. all arrays and buckets in these data are functions that do not depend on the arguments at the leaves below the clean children.

**Proof.** *The questions.* The family \(E\) consists of the questions outside \(D_i\), which belong to the exterior, of the left questions of the public edges, and of the \(u_C\). The family \(O\) has in addition the right questions at the leaves below the marked children: below a clean child these are the \(v_C\) and the right questions of the public edges, and below the other marked children the edges are public.

*The functions.* The contributions of a clean child are \(0\). So every call at \(D_i\) is the sum of the public contributions of the children that are not clean. A contribution of a child \(C'\) is a function of the arguments at the leaves below \(C'\); on \(\Omega(O)\) it is given, and it is read on \(\Omega(E)\) through the maps of the edges below \(C'\), which are public. By Lemma 2.1 of the lesson on changing the law, the arrays at \(D_d,\dots,D_i\), and each of their buckets, are sums and products of these calls and of functions of the exterior data. The arrays below a clean child are \(0\); the arrays below the other children are public; all other arrays belong to the exterior. The map \(A\) and the vector \(a_i\) belong to the exterior; \(A\) decides which buckets of the upper matrix enter the data, and \(a_i\) gives the class of the array at \(D_i\) that enters the right data.

So each side knows its family of questions and all functions of its data on its own domain. (3) holds because sums and products of functions that do not depend on some arguments do not depend on them. \(\blacksquare\)

The public data contain more than a decoder may use: for example \(a_i\), and all buckets of the upper matrix. The decoders are the procedures of the lesson on the heavy list and receive only their own data: the left decoder is run without \(a_i\), the right decoder with the array at \(D_i\) modulo \(a_i\), and neither receives the buckets with index in \(W\). When a decoder asks the labeling for the label at a key of a function on its domain, as the left decoder does for the response table and the right decoder for the function \(G\), the key is computed on the domain of this side, which the side knows by the lemma.

**The strategies.** Given the public data, the left player receives \((u_C)_{C\in\mathcal K}\), computes the left data, runs the left decoder, and applies the extraction rule of Section 2 to \(F_L\) at the designated leaf of each clean child. The right player does the same with \((v_C)_{C\in\mathcal K}\), the right decoder and \(F_R\). The outputs are an element of \(\mathcal O_s\) of the answer set of \(u_C\), and of \(v_C\), for every \(C\in\mathcal K\). So these are strategies, with independent random choices, for the \(k\)-fold repetition of the game \(G_{\mathrm{odd},s}\) of the base game.

Let \(\mathcal L\) be the event that \(F_R=F_L\) on \(H_i'\times H_i'\) and \(\operatorname{rank}F_L\le s\). Every value of \(F_L\) is \(z(xy)\) with \(z(1)=1\). A clean child is marked, so its leaves are replaced in \(O\). By Lemma 2.1 and the extraction rule, on the event \(\mathcal L\) the two outputs satisfy the constraint of the game on lists at the designated leaf of every clean child: the players win all \(k\) rounds.

## 5. The bound

**Proposition 5.1.** Assume (PR), and let the base game \(G_{\mathrm{base}}\) of the formula satisfy
\[
\operatorname{val}(G_{\mathrm{base}})<\frac1{2s^2}.
\]
Then
\[
\begin{aligned}
\mathbb P_i(\mathcal L)&\le\Bigl(1-\frac{\beta p_0}{64}\Bigr)^{n_i}\\
&\le\exp\Bigl(-\frac{p_0}{64}\,n_i^{1/3}\Bigr).
\end{aligned}
\]

**Proof.** By Lemma 1.1 the game on lists has a value of less than \(\tfrac12\). By (PR) with \(g=\tfrac12\), its \(k\)-fold repetition has a value of at most \((1-\tfrac1{64})^k\). Fix the public data. By Lemma 3.1 the edges at the designated leaves of the \(k\) clean children are an edge of the \(k\)-fold repetition with its law, and by Section 4 the players use strategies with random choices that are independent of this edge, and they win on the event \(\mathcal L\). By Lemma 1.1 of the lesson on projection games,
\[
\mathbb P_i(\mathcal L\mid\text{public data})\le\Bigl(\frac{63}{64}\Bigr)^{|\mathcal K|}.
\]
By Lemma 3.1 (1), given the exterior, \(|\mathcal K|\) is a sum of \(n_i\) independent indicators with the mean \(\beta p_0\). So
\[
\begin{aligned}
\mathbb E_i\Bigl(\frac{63}{64}\Bigr)^{|\mathcal K|}&=\Bigl(1-\beta p_0+\frac{63}{64}\beta p_0\Bigr)^{n_i}\\
&=\Bigl(1-\frac{\beta p_0}{64}\Bigr)^{n_i}.
\end{aligned}
\]
The last inequality of the claim is \(1-x\le e^{-x}\) with \(\beta n_i=n_i^{1/3}\). \(\blacksquare\)

The event \(\mathcal L\) was not used to define the public data or the strategies; the proposition bounds its probability from the outside.

**The contradiction.** By Proposition 1.1 of the lesson on tested rank, under its assumptions \(\mathbb P_i(\mathcal L)\ge\gamma_j/2\). If in addition the base game has a value of less than \(1/(2s^2)\) and
\[
n_i^{1/3}>\frac{64}{p_0}\,\log\frac4{\gamma_j},
\]
Proposition 5.1 gives \(\mathbb P_i(\mathcal L)<\gamma_j/4\). Both cannot hold. So under all these assumptions on the parameters there is no labeling that satisfies the test with a probability of at least \(\varepsilon\) and has the pair \(i<j\) as its two accepted levels. The number \(p_0\) does not depend on \(n_i\), so the last condition is one more lower bound for \(n_i\). That all the assumptions of the lessons on the proof of soundness can be met together, for all pairs of levels, is a matter of the order in which the parameters are chosen. It is not part of this lesson.

## 6. Exercises

**6.1.** Let \(\Lambda=\{1,\dots,6\}\), \(\Gamma=\{0,1\}\), \(\pi(a)=a\bmod2\). Compute \(\pi_{\mathrm{odd}}(L)\) for \(L=\{1,2,3\}\), \(L=\{1,3,5\}\) and \(L=\{2\}\).

**6.2.** Show by an example that \(\pi_{\mathrm{odd}}(L)\) can be empty for a set \(L\) with an even number of elements. Where does the proof of Section 2 give that the lists are odd?

**6.3.** Let \(z\) be the evaluation at a point \(x_0\in\Omega(E)\). What are the lists of \(F(x,y)=z(xy)\), and what is its rank?

**6.4.** Let \(z=z_1+z_2+z_3\) be the sum of the evaluations at three points whose arguments at a leaf \(\lambda\) are \(a,a,a'\) with \(a\ne a'\). What is the list of \(z(xy)\) at \(\lambda\)?

**6.5.** In Lemma 3.1, suppose that the probability that a marked child with the edges \(\mathbf e\) has only zero contributions were a number \(p(\mathbf e)\) that depends on \(\mathbf e\). What would be the law of the edges of a clean child?

**6.6.** Compute \((1-\beta p_0/64)^{n}\) approximately for \(n=10^{12}\), \(\beta=n^{-2/3}\), \(p_0=\tfrac1{10}\).

## 7. Solutions

**6.1.** \(\{1,2,3\}\): two odd elements and one even, so \(\pi_{\mathrm{odd}}=\{0\}\). \(\{1,3,5\}\): three odd elements, \(\pi_{\mathrm{odd}}=\{1\}\). \(\{2\}\): \(\pi_{\mathrm{odd}}=\{0\}\).

**6.2.** For \(L=\{1,3\}\) and the map of 6.1, both elements are mapped to \(1\), and \(\pi_{\mathrm{odd}}(L)=\emptyset\). The lists of a form are odd because \(\sum_ad_a=z(1)=1\): this is the normalization \(z(1)=1\) of the left decoder.

**6.3.** \(F(x,y)=x(x_0)\,y(x_0)\) has the rank \(1\). At a leaf \(\lambda\), \(F(e_a,e_a)=e_a(x_0)\) is \(1\) exactly for the argument \(a\) of \(x_0\) at \(\lambda\). The list is this one answer.

**6.4.** \(d_b=z(e_b)\) is the number, modulo two, of the three points with the argument \(b\) at \(\lambda\). So \(d_a=0\), \(d_{a'}=1\), and the list is \(\{a'\}\).

**6.5.** Given that the child is clean, the tuple \(\mathbf e\) would have a probability proportional to \(\mu^{\otimes m}(\mathbf e)\,p(\mathbf e)\). The edges of a clean child would not have the law of the base game, and the designated edges would not form an edge of the repeated game.

**6.6.** \(\beta n=n^{1/3}=10^4\), so the number is about \(\exp(-10^4/640)\), which is \(\exp(-15.6)\approx1.6\cdot10^{-7}\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026

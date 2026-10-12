# Folding and the law of the tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A label of the new game is a part of a partition, and every label is realized by a point: there is an assignment of answers at which all the displayed functions take the restored values. This forces exact algebraic relations on every labeling, without any assumption on it. If a row at a node is changed by adding products of rows at nodes below it, the question stays the same, and the restored values change by the same products of restored values. This lesson proves these relations, and then defines the probability law on the constraints, which completes the definition of the game that [OpenAI-G] builds from the base game.

- Joint folding (Lemma 1.1).
- The functional of a response on products of displayed rows (Lemma 2.1).
- Buckets and steps of rank one (Lemma 3.1).
- The recursive sampler and the law of the tests (Section 4); the game has perfect completeness and constraints with at most two preimages (Proposition 4.1).

The lesson follows [OpenAI-G, Sections 3.4 and 3.5]. It continues [The tree of function spaces and the questions](the-tree-of-function-spaces-and-the-questions.md) and uses its notation: the families \(E\), the spaces \(H_D\), array families \(\mathbf M\), the joint function \(\Psi_{E,\mathbf M}\), keys, labels and restored values.

## 1. Joint folding

Fix a family \(Q\) of base questions (a family \(E\) or a mixed family) and an array family \(\mathbf M\) with its joint function \(\Psi=\Psi_{Q,\mathbf M}\). A label \(P\) at the key of \(\Psi\) has a restored value \(y=\operatorname{out}_\Psi(P)\), with a component \(y_C\in K_{\operatorname{level}(C)}\) for every node \(C\) that is not a leaf; \((y_C)_u\) is the restored value of the row \(u\) of \(M_C\).

**Lemma 1.1 (joint folding).** Let \(D\) be a node that is not a leaf. For each row index \(h\) of \(M_D\) let
\[
b_h=c_h\cdot1+\sum_{C,u,v}\lambda_{h,C,u,v}\,(M_C)_u\,(M_C)_v ,
\]
with coefficients \(c_h,\lambda_{h,C,u,v}\in\mathbb F\), where \(C\) runs through nodes below \(D\) that are not leaves, \(C\ne D\), and \(u,v\) through the rows of \(M_C\). Let \(\widetilde{\mathbf M}\) be the family with \((M_D)_h+b_h\) in place of \((M_D)_h\) and all other rows unchanged. Then \(\widetilde{\mathbf M}\) is an array family, its joint function has the same key as \(\Psi\), and for every label the restored values \(\widetilde y\) and \(y\) for the two families satisfy
\[
\begin{aligned}
\widetilde y_C&=y_C\quad(C\ne D),\\
(\widetilde y_D)_h&=(y_D)_h+c_h\\
&\quad+\sum_{C,u,v}\lambda_{h,C,u,v}\,(y_C)_u\,(y_C)_v .
\end{aligned}
\]

**Proof.** By Lemma 2.1 of the lesson on the tree of function spaces, \(1\) and the products \((M_C)_u(M_C)_v\) lie in \(H_D(Q)\); so \(\widetilde{\mathbf M}\) is an array family. Let \(\sigma\) be the map of the space \(Y\) of joint values to itself that keeps all components except the one at \(D\) and adds to its coordinate \(h\) the number \(c_h+\sum\lambda_{h,C,u,v}(y_C)_u(y_C)_v\). The joint function of \(\widetilde{\mathbf M}\) is \(\sigma\circ\Psi\). Applying \(\sigma\) twice is the identity: the components \(y_C\), \(C\ne D\), which enter the added number, are not changed, and the characteristic is two. So \(\sigma\) is one-to-one, and by Lemma 4.2 of that lesson \(\sigma\circ\Psi\) has the same key as \(\Psi\). On the reduced domain the two functions are \(\widetilde\Psi\) and \(\sigma\circ\widetilde\Psi\), so on every part the restored values are \(y\) and \(\sigma(y)\). \(\blacksquare\)

No property of the labeling was used: the labeling answers a key, and the two array families have the same key.

The same holds, with the same proof, for a function \(\Theta_{D',a}\circ\Psi\) in which one component is shown only modulo a vector \(a\), as long as the rows that enter the products are shown in full: if the changed node \(D\) is \(D'\) itself, the added vector is read modulo \(a\).

## 2. The functional of a response

**Lemma 2.1.** Let \(P\) be a label at the key of \(\Psi\), with the restored values \(y_C\). Let \(D\) be a node that is not a leaf, \(\mathcal C\) a set of nodes below \(D\) that are not leaves and different from \(D\), and let \(B\subset H_D(Q)\) be the span of the constant \(1\) and of the products \((M_C)_u\,(M_C)_v\), where \(C\in\mathcal C\) and \(u,v\) are rows of \(M_C\). Then there is exactly one linear functional \(b_y:B\to\mathbb F\) with
\[
\begin{gathered}
b_y(1)=1,\\
b_y\bigl((M_C)_u(M_C)_v\bigr)=(y_C)_u\,(y_C)_v .
\end{gathered}
\]
Every extension \(z\) of \(b_y\) to a linear functional on \(H_D(Q)\) satisfies \(z(1)=1\), and for every \(C\in\mathcal C\) the matrix \(\bigl(z((M_C)_u(M_C)_v)\bigr)_{u,v}\) is \(y_Cy_C^{\mathsf t}\), a matrix of rank at most one.

**Proof.** The restored value is the value of \(\Psi\) at a point \(x\in\Omega(Q)\): take a point of the part \(P\) and a preimage under the reduction map. The evaluation of functions at \(x\) is a linear functional on \(B\), and it has the stated values on the generators, since \((M_C)_u(x)=(y_C)_u\). The generators span \(B\), so there is only one such functional. An extension has the same values on \(1\) and on the products. \(\blacksquare\)

The point of the lemma is that the prescription on the generators is consistent. The generators can satisfy linear relations, also between different nodes \(C\); the restored values respect all of them, because they are the values at one point.

## 3. Buckets and steps of rank one

Let \(K=\mathbb F^\ell\) and let \(H\) be a vector space over \(\mathbb F\). For a family of vectors \(h_v\in H\), indexed by the nonzero \(v\in K\), let
\[
M=\sum_{v\in K\setminus\{0\}}v\otimes h_v\ \in K\otimes H ,
\]
the list of \(\ell\) rows whose row \(i\) is the sum of the \(h_v\) with \(v_i=1\). The \(h_v\) are the *buckets* of \(M\).

**Lemma 3.1.** Let the buckets be independent and uniform in \(H\). Then \(M\) is uniform in \(K\otimes H\). If \(a\in K\setminus\{0\}\) is independent of the buckets and \(h_a^*\) is a further independent uniform vector, then replacing the bucket \(h_a\) by \(h_a^*\) changes \(M\) to
\[
M^*=M+a\otimes h,\qquad h=h_a+h_a^* ,
\]
and \(h\) is uniform in \(H\) and independent of \(M\) and \(a\).

**Proof.** The map from the families of buckets to \(K\otimes H\) is linear and onto, because the standard basis vectors of \(K\) are among the indices: the buckets at these indices alone give every list of rows. A linear map onto a space carries the uniform law to the uniform law. For the second statement, given \(a\) and all the buckets, \(h_a^*\) is uniform, so \(h=h_a+h_a^*\) is uniform; and its law does not depend on the given values. \(\blacksquare\)

So changing one bucket is the step of rank one of the lesson on matrices and slices, in the direction \(a\) of the bucket. The component of \(M\) modulo \(a\) does not change: this is what a constraint at this node with the vector \(a\) shows on its right side.

## 4. The law of the tests

Fix integers \(R_1,\dots,R_d\ge1\) in addition to the parameters \(t,d,n_p,\ell_p\). A *test* is drawn as follows.

*Questions.* Draw a left question of the base game independently at each leaf, with the law of the left end of an edge. This is \(E\).

*Path.* Independently, draw a path \(D_d,D_{d-1},\dots,D_0\) from the root to a leaf: \(D_d\) is the root, and \(D_{p-1}\) is uniform among the children of \(D_p\).

*Scalar samples.* Given \(E\) and the path, a random function \(\operatorname{Sample}(D_p)\in H_{D_p}(E)\) is defined by recursion on \(p\). For \(p=0\) it is uniform in \(H_{D_0}(E)\). For \(p\ge1\), let \(C_*=D_{p-1}\), draw independently a uniform \(U_C\in H_C(E)^2\) for every child \(C\ne C_*\) of \(D_p\), and \(2R_p\) independent functions \(G_1,H_1,\dots,G_{R_p},H_{R_p}\) with the law of \(\operatorname{Sample}(C_*)\), and put
\[
\operatorname{Sample}(D_p)=\sum_{C\ne C_*}U_C+\sum_{h=1}^{R_p}G_hH_h .
\]
Every use of \(\operatorname{Sample}\) draws all its random choices anew: two calls at the same node are independent.

*Arrays.* For every node \(D_p\) of the path with \(p\ge1\), draw independent buckets \(h_{p,v}\) with the law of \(\operatorname{Sample}(D_p)\), for the nonzero \(v\in K_p\), and let \(M_{D_p}=\sum_vv\otimes h_{p,v}\). For every other node \(D\) that is not a leaf, let \(M_D\) be uniform in \(K_{\operatorname{level}(D)}\otimes H_D(E)\). Given \(E\) and the path, all these arrays are independent.

*Constraint.* Draw \(p\) uniformly in \(\{1,\dots,d\}\) and a uniform nonzero \(a_p\in K_p\), independently of the rest. The test is the constraint of \((E,\mathbf M,D_p,a_p)\).

The players see only the keys: the left player the key of the joint function, the right player the key of the function with one bit of the value at \(D_p\) removed. The path, the buckets and the level \(p\) are not shown, except for what the keys reveal.

By Lemma 2.1 of the lesson on the tree of function spaces, the products \(G_hH_h\) lie in \(H_{C_*}(E)^2\subset H_{D_p}(E)\), so every sample lies in the stated space. Along the path the arrays are not uniform: their rows contain products of functions from the level below. This links the nodes of the path, and the soundness proof of [OpenAI-G] uses it through Lemmas 1.1 and 2.1.

**Proposition 4.1.** The tests define a projection game with rational probabilities. Every constraint has at most two preimages of every label, and if the formula \(\Psi\) is satisfiable the game has the value \(1\).

**Proof.** There are finitely many families \(E\), paths and array families, and all the draws are from finite sets with rational probabilities. The rest is Lemma 5.1 and Proposition 5.2 of the lesson on the tree of function spaces. \(\blacksquare\)

[OpenAI-G] proves that for suitable parameters, chosen in terms of a number \(\varepsilon>0\), this game has a value below \(\varepsilon\) whenever the formula is not satisfiable. That proof is not part of this lesson.

## 5. Exercises

**5.1.** Let \(d=2\) and let the root \(D\) have a child \(C\) that is not a leaf. Let \(P\) be a label with \((y_C)_1=1\), \((y_C)_2=0\) and \((y_D)_1=0\). What are the restored values of the same label when the function \(1+(M_C)_1(M_C)_1+(M_C)_1(M_C)_2\) is added to the first row of \(M_D\)?

**5.2.** In Lemma 2.1 let two rows of \(M_C\) satisfy \((M_C)_1(M_C)_2=(M_C)_1\) as functions. What does this imply for the restored values of every label, and why?

**5.3.** Let \(\ell=2\). Write the two rows of \(M\) in terms of the three buckets, and check Lemma 3.1 for \(a=(1,1)\).

**5.4.** Let \(d=1\), \(n_1=1\), \(R_1=1\), so that \(\operatorname{Sample}(D_1)=GH\) with independent uniform functions \(G,H\) on a set \(\Omega\). Show that \(\operatorname{Sample}(D_1)\) is not uniform, and compute the probability that it is the zero function.

## 6. Solutions

**5.1.** Here \(c_1=1\) and the products have the restored values \((y_C)_1(y_C)_1=1\) and \((y_C)_1(y_C)_2=0\). So the new restored value of the first row at \(D\) is \(0+1+1+0=0\); all other restored values are unchanged.

**5.2.** \((y_C)_1(y_C)_2=(y_C)_1\): the restored values are the values of the rows at one point \(x\), and the relation holds at \(x\). So the response \((y_C)_1=1\), \((y_C)_2=0\) cannot occur.

**5.3.** The nonzero vectors are \((1,0)\), \((0,1)\), \((1,1)\). The rows are \(h_{(1,0)}+h_{(1,1)}\) and \(h_{(0,1)}+h_{(1,1)}\). Replacing \(h_{(1,1)}\) by \(h^*\) adds \(h=h_{(1,1)}+h^*\) to both rows, which is \(a\otimes h\) for \(a=(1,1)\); the sum of the two rows, which is the component modulo \(a\), does not change.

**5.4.** At each point of \(\Omega\) the values of \(G\) and \(H\) are independent uniform bits, and the product is \(1\) with the probability \(\tfrac14\); the points are independent. So the product is the zero function with the probability \((\tfrac34)^{|\Omega|}\), while a uniform function is zero with the probability \((\tfrac12)^{|\Omega|}\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026

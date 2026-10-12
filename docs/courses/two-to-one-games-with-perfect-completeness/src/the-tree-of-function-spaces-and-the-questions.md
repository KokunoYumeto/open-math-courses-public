# The tree of function spaces and the questions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The reduction of [OpenAI-G] turns the base game into a new game. A question of the new game shows lists of Boolean functions of many independent answers to base questions; the lists sit at the nodes of a tree. More exactly, the question is the partition of all possible answers according to the values of all these functions, and a label is one part of the partition. A constraint forgets one bit of the values, so it merges at most two parts into one. This lesson defines the function spaces, the questions and the constraints, and proves two things: every constraint has at most two preimages of every label, and a satisfiable formula gives a labeling that satisfies all constraints.

- The tree, the domains and the function spaces \(H_D\) (Lemma 2.1).
- Arrays and the joint function (Section 3).
- The key of a function: which arguments it uses, and its partition (Lemmas 4.1 to 4.3).
- Constraints with at most two preimages (Lemma 5.1); perfect completeness (Proposition 5.2).

The lesson follows [OpenAI-G, Sections 3.1 to 3.3]. It continues [Projection games and the base game](projection-games-and-the-base-game.md) and uses its notation: the sets \(\mathcal A_C\), the base game \(G_\Psi^{\otimes t}\) and Lemma 4.2 of that lesson. The probability law on the constraints, and the proof that an unsatisfiable formula gives a small value, are not part of this lesson.

## 1. The tree and the domains

Let \(\Psi\) be a 3-formula and \(t\ge1\). In the base game \(G_\Psi^{\otimes t}\) a *left question* is an ordered tuple of \(t\) clauses. An edge chooses a position in each clause; the *right question* is the tuple of the \(t\) variables at these positions, with the answer set \(\mathbb F^t\), where \(\mathbb F\) is the field with two elements. For a clause \(c\) let \(\Omega_c=\mathcal A_c\subset\mathbb F^3\) be the set of its seven permitted assignments.

Fix integers \(d\ge1\), \(n_1,\dots,n_d\ge1\) and \(\ell_1,\dots,\ell_d\ge1\). Let \(\mathcal T\) be the rooted ordered tree with the root at the level \(d\), the leaves at the level \(0\), and exactly \(n_p\) children of every node of the level \(p\). Let \(K_p=\mathbb F^{\ell_p}\).

Let \(E\) be a family of left questions, one at each leaf. A *slot* is a pair \((C,k)\) of a leaf \(C\) and a number \(k\in\{1,\dots,t\}\); it carries the \(k\)-th clause \(c\) of the question at \(C\), and its *domain* is \(\Omega_c\). For a node \(D\) let \(\Omega_D(E)\) be the product of the domains of all slots at the leaves below \(D\) (at \(D\) itself, if \(D\) is a leaf), and \(\Omega(E)\) the product over all slots. Slots are separate factors: if the same clause or the same variable occurs at two slots, the two arguments are not required to be equal.

A *mixed family* \(O\) is obtained from \(E\) by choosing some leaves and, at each of them, a base edge at its left question, and replacing the left question by the right question. At a slot of such a leaf the domain is \(\mathbb F\), and the slot carries the variable at the chosen position of its clause; we call it a *variable slot*, the others *clause slots*. The coordinate maps \(u\mapsto u_j\) at the replaced slots and the identity at the others give a map
\[
\pi_D:\Omega_D(E)\longrightarrow\Omega_D(O),
\]
which is onto, by Lemma 4.2 of the lesson on projection games. Below, \(Q\) stands for \(E\) or for a mixed family.

## 2. The function spaces

**Definition.** For a leaf \(C\), let \(H_C(Q)\) be the space of all functions \(\Omega_C(Q)\to\mathbb F\). For every node \(C\) let \(H_C(Q)^2\) be the span of the products \(gh\) with \(g,h\in H_C(Q)\). For a node \(D\) that is not a leaf let
\[
H_D(Q)=\sum_{C\text{ child of }D}H_C(Q)^2 ,
\]
a space of functions on \(\Omega_D(Q)\); a function of the arguments below a child is read as a function on \(\Omega_D(Q)\) that ignores the other arguments. Products are products of values.

**Lemma 2.1.**

1. Every \(H_D(Q)\) contains the constant \(1\), and \(H_D(Q)\subset H_D(Q)^2\).
2. If \(C\) is a descendant of \(D\) and \(C\ne D\), then \(H_C(Q)^2\subset H_D(Q)\).
3. Composition with \(\pi_D\) is a one-to-one linear map \(H_D(O)\to H_D(E)\) that preserves products.

**Proof.** (1) At a leaf the constant \(1\) is a function. At another node, \(1=1\cdot1\) lies in the square space of a child. Multiplying by \(1\) gives the inclusion. (2) For a child this is the definition. In general go up from \(C\) to \(D\) step by step, using \(H_{C'}^2\subset H_{D'}\subset H_{D'}^2\) for a child \(C'\) of \(D'\). (3) Since \(\pi_D\) is onto, \(f\mapsto f\circ\pi_D\) is one-to-one on all functions, and it preserves sums and products. At a leaf it maps into the space of all functions. The recursive definition then gives the inclusion at every node. \(\blacksquare\)

We regard \(H_D(O)\) as a subspace of \(H_D(E)\) by (3). The sum in the definition of \(H_D\) is not direct: all summands contain the constants.

## 3. Arrays and the joint function

An *array* at a node \(D\) of a level \(p\ge1\) is a list \(M_D\) of \(\ell_p\) functions in \(H_D(E)\), its *rows*. At a point \(x\in\Omega(E)\) it has the value \(M_D(x)\in K_p\). An *array family* \(\mathbf M\) has one array at every node that is not a leaf. Let \(Y\) be the product of the spaces \(K_{\operatorname{level}(D)}\) over the nodes \(D\) that are not leaves. The *joint function* of the family is
\[
\begin{gathered}
\Psi_{E,\mathbf M}:\ \Omega(E)\longrightarrow Y,\\
x\longmapsto(M_D(x))_D .
\end{gathered}
\]

For such a node \(D\) of the level \(p\) and a vector \(a\ne0\) in \(K_p\), let \(\Theta_{D,a}:Y\to Y_{D,a}\) be the linear map that replaces the component at \(D\) by its class in \(K_p/\{0,a\}\) and keeps the other components. Its kernel has two elements: \(0\), and the element with \(a\) at \(D\) and \(0\) elsewhere. So every value of \(\Theta_{D,a}\) has exactly two preimages in \(Y\). The function
\[
\Theta_{D,a}\circ\Psi_{E,\mathbf M}
\]
shows all values except one bit of the value at \(D\).

## 4. The key of a function

Let \(f:\Omega(Q)\to Y\) be a function with values in a finite set. We describe the part of the data of \(f\) that a question of the new game shows.

**Definition.** A slot \(s\) is *unused* by \(f\) if \(f\) does not change when only the argument at \(s\) changes. A clause slot \(s\) with the domain \(\Omega_c\) is *reducible to the position \(j\)* if, for all values \(x_{-s}\) of the other arguments and all \(u,u'\in\Omega_c\) with \(u_j=u'_j\),
\[
f(x_{-s},u)=f(x_{-s},u').
\]

**Lemma 4.1.** If a clause slot is used by \(f\) and reducible to a position, this position is unique.

**Proof.** Let \(s\) be reducible to two different positions \(j\) and \(k\). Fix the other arguments. Then \(f(x_{-s},u)\) is a function \(g(u_j)\) and also a function \(h(u_k)\). By Lemma 4.2 of the lesson on projection games every pair \((b,b')\) of bits is \((u_j,u_k)\) for some \(u\in\Omega_c\), so \(g(b)=h(b')\) for all \(b,b'\). Both functions are constant. This holds for all values of the other arguments, so \(s\) is unused. \(\blacksquare\)

**The reduced domain.** Apply to each slot the following map: an unused slot is dropped; a used clause slot that is reducible to the position \(j\) is replaced by the bit \(u_j\); every other used slot is kept. The product of these maps is a map
\[
r_f:\Omega(Q)\longrightarrow\Omega_f .
\]
Each coordinate of \(\Omega_f\) is recorded with its *type*: its slot \((C,k)\), and either the clause and the domain \(\Omega_c\), for a clause slot that is kept in full, or a variable and the domain \(\mathbb F\), for a bit; for a clause slot reduced to the position \(j\) the variable is the one at the position \(j\) of the clause, and the clause and the number \(j\) are not recorded.

**Lemma 4.2.** The map \(r_f\) is onto, and there is exactly one function \(\widetilde f:\Omega_f\to Y\) with \(f=\widetilde f\circ r_f\). The typed domain \(\Omega_f\) and the partition
\[
\mathcal P_f=\bigl\{\widetilde f^{-1}(y):\ y\text{ a value of }f\bigr\}
\]
of \(\Omega_f\) depend only on \(Q\) and on the relation "\(f(x)=f(x')\)" on \(\Omega(Q)\). In particular they are the same for \(f\) and for \(\beta\circ f\), if \(\beta\) is one-to-one on the values of \(f\).

**Proof.** Each coordinate map is onto (Lemma 4.2 of the lesson on projection games for the bits), so \(r_f\) is onto. Let \(r_f(x)=r_f(x')\). Replace the arguments of \(x\) by those of \(x'\) one slot at a time. At an unused slot \(f\) does not change; at a reduced slot the two arguments have the same bit at the position \(j\), so \(f\) does not change; at the other slots the arguments are equal. So \(f(x)=f(x')\), and \(\widetilde f\) exists; it is unique because \(r_f\) is onto. The definitions of "unused" and "reducible" speak only about equalities of values of \(f\), and by Lemma 4.1 the position of a reduction is determined; so \(r_f\) and the types depend only on the relation. A part of \(\mathcal P_f\) is the image under \(r_f\) of a class of the relation. \(\blacksquare\)

**Definition.** The *left key* of \(f\) consists of the letter L, the typed domain \(\Omega_f\) and the partition \(\mathcal P_f\), as a set of parts without names. The *right key* is the same with the letter R. A *label* at a key is a part \(P\in\mathcal P_f\). For a function \(f\) with this key, the *restored value* \(\operatorname{out}_f(P)\) is the value of \(\widetilde f\) on \(P\).

So \(\operatorname{out}_f\) is a one-to-one map from the labels onto the set of the values of \(f\). Different functions can have the same key; then they have the same labels, with different restored values. Every restored value is the value of \(f\) at a point of \(\Omega(Q)\).

**Lemma 4.3 (shared keys).** Let \(O\) be a mixed family obtained from \(E\), \(\pi:\Omega(E)\to\Omega(O)\) the map of Section 1, and \(f:\Omega(O)\to Y\). Then \(f\) and \(f\circ\pi\) have the same keys, and \(\operatorname{out}_f=\operatorname{out}_{f\circ\pi}\).

**Proof.** Because \(\pi\) is onto in the other arguments, a slot that was not replaced is unused, or reducible to a position, for \(f\) exactly if it is so for \(f\circ\pi\). Let \(s\) be a replaced slot, with the chosen position \(j\). It is unused by \(f\) exactly if it is unused by \(f\circ\pi\), again because the maps are onto. If it is used, \(f\circ\pi\) depends on the clause argument only through its bit at \(j\); so the slot is reducible to \(j\), and by Lemma 4.1 to no other position. In both reduced domains this coordinate is a bit with the same slot and the same variable. So the typed reduced domains agree, and \(r_{f\circ\pi}=r_f\circ\pi\). Then \(\widetilde f\circ r_f\circ\pi=f\circ\pi\) shows that the reduced functions agree. \(\blacksquare\)

This lemma is the reason for the definition of the keys: a player who sees a clause and a player who sees only one variable of it can be asked the same question, if the functions depend on the clause only through that variable.

## 5. The constraints

**Definition.** The questions of the new game are keys: the left questions are the left keys of joint functions of array families, and the right questions are the right keys of such functions composed with a map \(\Theta_{D,a}\); here the family of base questions may be \(E\) or a mixed family \(O\), with the rows of the arrays in the spaces \(H_D(O)\). The answers at a key are its labels. For a family \(E\), an array family \(\mathbf M\), a node \(D\) that is not a leaf and a nonzero vector \(a\) of its space \(K_p\), let
\[
f=\Psi_{E,\mathbf M},\qquad g=\Theta_{D,a}\circ f .
\]
The *constraint* of \((E,\mathbf M,D,a)\) is the edge from the left key of \(f\) to the right key of \(g\) with the map
\[
P\ \longmapsto\ \operatorname{out}_g^{-1}\bigl(\Theta_{D,a}(\operatorname{out}_f(P))\bigr).
\]

**Lemma 5.1.** This map is well defined and onto the labels of the right key, and every label has at most two preimages. A labeling satisfies the constraint exactly if its restored values \(y\) on the left and \(y'\) on the right satisfy \(\Theta_{D,a}(y)=y'\).

**Proof.** \(\operatorname{out}_f(P)\) is a value of \(f\), so its image is a value of \(g\), and \(\operatorname{out}_g^{-1}\) is defined on it. Every value of \(g\) is the image of a value of \(f\); this gives "onto" and the description of the satisfied constraints. A value of \(\Theta_{D,a}\) has two preimages in \(Y\), hence at most two among the values of \(f\); and \(\operatorname{out}_f\), \(\operatorname{out}_g\) are one-to-one. \(\blacksquare\)

Every label set has at most \(7^{tn}\) elements, where \(n\) is the number of leaves, because \(\Omega(E)\) has at most so many points. So for fixed \(t\), \(d\), \(n_p\), \(\ell_p\) the sizes of the label sets are bounded independently of \(\Psi\).

**Proposition 5.2 (perfect completeness).** If \(\Psi\) is satisfiable, there is a labeling of all keys that satisfies every constraint, for all choices of \(t,d,n_p,\ell_p\). So every game whose edges are constraints, with any law on them, has the value \(1\).

**Proof.** Let \(\xi\) be a satisfying assignment. At a key, take the point of its typed domain that has, at a coordinate with a clause \(c\), the values of \(\xi\) at the three variables of \(c\), which is an element of \(\Omega_c\), and at a coordinate with a variable its value under \(\xi\). Label the key by the part that contains this point. This uses only the key.

For a family \(E\) let \(x_\xi\in\Omega(E)\) be the point that has at every slot the values of \(\xi\) at the variables of its clause. For every function \(f\) on \(\Omega(E)\), the point \(r_f(x_\xi)\) is the point chosen at the key of \(f\): at a reduced slot it is the value of \(\xi\) at the recorded variable. So the label at the key of \(f\) has the restored value \(f(x_\xi)\). For a constraint, the restored values are \(f(x_\xi)\) and \(g(x_\xi)=\Theta_{D,a}(f(x_\xi))\), and by Lemma 5.1 it is satisfied. \(\blacksquare\)

The new game has perfect completeness and constraints with at most two preimages for every choice of the parameters and of the law on the constraints. What depends on these choices is the value for an unsatisfiable formula.

## 6. Exercises

**6.1.** Let \(d=1\), \(n_1=2\), \(t=1\), with the leaves \(C_1,C_2\). Show that \(H_C(E)^2=H_C(E)\) at a leaf, describe the space at the root, and find its dimension.

**6.2.** Let \(f(u,b)=(1+b)u_1+bu_2\) on \(\Omega_c\times\mathbb F\), a clause slot and a variable slot, with values in \(\mathbb F\). Show that the clause slot is used and is not reducible to any position, although for each fixed \(b\) the function depends on one position only.

**6.3.** Give a function \(f\) with values in \(\mathbb F^2\) and a vector \(a\) for which the map of a constraint is one-to-one.

**6.4.** Let \(f:\Omega(E)\to\mathbb F\) be the function \(x\mapsto u_2\), the second bit of the argument \(u\) at one slot \(s\). Describe its left key and its two labels with their restored values, and the key of \(1+f\).

## 7. Solutions

**6.1.** At a leaf every function is a product of itself with \(1\), and products of functions are functions; so the span of the products is the space of all functions on \(\Omega_C\), of the dimension \(7\). The space at the root consists of the functions \(g_1(x_1)+g_2(x_2)\) on \(\Omega_{C_1}\times\Omega_{C_2}\). The two summand spaces meet in the constants, so the dimension is \(7+7-1=13\).

**6.2.** For \(b=0\) the function is \(u_1\), for \(b=1\) it is \(u_2\); it is not constant in \(u\), so the slot is used. It is not reducible to the position \(1\): for \(b=1\) the two elements \(u,u'\) of \(\Omega_c\) with \(u_1=u'_1\) and \(u_2\ne u'_2\), which exist by Lemma 4.2 of the lesson on projection games, have different values. In the same way \(b=0\) excludes the position \(2\), and either value of \(b\) excludes the position \(3\).

**6.3.** Let \(f\) take only the two values \((0,0)\) and \((0,1)\), for example \(f=(0,u_1)\) at one node with \(\ell=2\), and \(a=(1,0)\). The classes of \((0,0)\) and \((0,1)\) modulo \(a\) are different, so the two labels on the left go to two different labels on the right.

**6.4.** All slots except \(s\) are unused. The slot \(s\) is used and reducible to the position \(2\). The reduced domain is one bit, typed by the slot \(s\) and the second variable of its clause. The partition has the two parts \(\{0\}\) and \(\{1\}\), with the restored values \(0\) and \(1\). The function \(1+f\) has the same relation of equal values, hence the same key; the same two labels have the restored values \(1\) and \(0\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026

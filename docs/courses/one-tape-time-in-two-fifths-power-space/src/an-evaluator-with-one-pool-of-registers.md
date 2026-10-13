# An evaluator with one pool of registers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose that many words of \(d\) bits are defined one from another by rules, and that one of them is wanted. The direct way computes a word from its dependencies and keeps each dependency in storage while the next one is computed; along a chain of dependencies this needs many words of storage at once. The evaluator of this lesson needs three registers in all, however long the chains are. A procedure adds the wanted word to one register and gives all other registers back as it found them, whatever they contained. So a caller can leave its own intermediate results in the registers while a callee uses the same registers. The idea is due to J. Cook and I. Mertz; the form given here, with its second kind of rule and its count of the stack, is from [OpenAI-S].

- Systems of words with ordinary rules and history rules (Section 1).
- The procedure \(\mathsf{Add}\) and its contract (Theorem 2.1).
- Ordinary rules (Section 3) and history rules (Section 4).
- One pool suffices, and the storage on the stack is counted along a path (Section 5).

The lesson follows [OpenAI-S, Section 2]. It uses the field, the lookup extensions and the top coefficient of [Polynomials for Boolean functions](polynomials-for-boolean-functions.md), and the meaning of "space" from [One-tape machines, blocks and visits](one-tape-machines-blocks-and-visits.md).

## 1. Systems of words

Fix a number \(T\ge2\), a width \(d\ge1\) and a constant \(r\ge1\). A *word* is a string of \(d\) bits.

**Definition.** A *system of words* consists of a finite set of *vertices* and, for every vertex \(V\), a word \(v(V)\), its *value*, together with a description of how the value arises. There are three kinds of vertices.

- A *base* vertex. Its value is computed directly.
- An *ordinary* vertex. It has *dependencies* \(U_1,\dots,U_n\), \(1\le n\le r\), which are vertices, and a function \(f_V\) from \(n\)-tuples of words to words, with
\[
v(V)=f_V\bigl(v(U_1),\dots,v(U_n)\bigr).
\]
- A *history* vertex. It has a dependency \(H\), further dependencies \(A_1,\dots,A_N\), and a number \(g\) with \(0\le g\le d\). A string \(Y\) of \(g\) bits is a *guess*. For every guess \(Y\) there is a function \(G_Y\) from words to words, and for every guess \(Y\) and every \(i\le N\) a function \(P_{Y,i}\) from pairs of words to bits. They satisfy the identity (1.1) below.

The identity of a history vertex is, in \(\mathbb F^{d+1}\) for a field \(\mathbb F\) of characteristic two,
\[
\begin{aligned}
\overline{v(V)}=\sum_{Y}\ &\overline{G_Y(v(H))}\\
&\cdot\prod_{i=1}^NP_{Y,i}\bigl(v(H),v(A_i)\bigr).
\end{aligned}
\]
We refer to it as (1.1).

The dependencies form no cycles: there is an order of the vertices in which every vertex comes after its dependencies.

The identity (1.1) is required only for the values \(v(H)\), \(v(A_i)\) of the system, not for other words in their place. It holds in particular if exactly one guess \(Y\) has \(P_{Y,i}(v(H),v(A_i))=1\) for all \(i\), and \(G_Y(v(H))=v(V)\) for this guess: then one term of the sum is \(\overline{v(V)}\) and the others are \(0\). One reads \(P_{Y,i}\) as a test of the guess \(Y\) against the word \(A_i\), and \(G_Y\) as the result if the guess is right. The value of a history vertex is found by guessing, and the tests of a guess are separate for the separate words \(A_i\).

**Size and uniformity.** We assume, with a fixed constant \(C\):

- the number of the vertices, the width \(d\) and all numbers \(N\) are at most \(T^C\); a vertex has a name of \(O(\log T)\) bits; from a name, the kind of the vertex, its numbers \(n\), \(N\), \(g\) and the name of any one of its dependencies are computed in space \(\operatorname{polylog}T\);
- the bits of the value of a base vertex are computed from its name, and the bits of \(f_V\), \(G_Y\) and \(P_{Y,i}\) from the name, \(Y\), \(i\) and explicitly given words, in space \(O(d\operatorname{polylog}T)\), without reference to any other word of the system;
- a number \(\Delta\le T^C\) is given with \(\Delta\ge d\) and \(\Delta\ge(N+1)d\) for every history vertex.

These computations may read data that stay fixed during the whole evaluation, such as an input. If such data are kept in the working storage, their size is added once to the space bound of Theorem 2.1.

**Weights.** Give every pair (vertex, dependency) a *weight*: \(1\) for a dependency of an ordinary vertex, \(1\) for the dependency \(H\) of a history vertex, and \(g+1\) for each dependency \(A_i\) of a history vertex. A *path* goes from a vertex to one of its dependencies, from there to one of its dependencies, and so on. Let \(W(V)\) be the largest sum of the weights along a path that starts at \(V\); for a base vertex \(W(V)=0\).

## 2. The contract

Let \(\mathbb F\) be the field of the previous lesson for the number \(\Delta\), so \(|\mathbb F|>\Delta\) and an element has \(O(\log T)\) bits. A *register* holds a vector of \(\mathbb F^{d+1}\). The *pool* consists of
\[
p=\max\{3,\ r+1\}
\]
registers \(R_1,\dots,R_p\).

**Theorem 2.1** (the evaluator; [OpenAI-S]). For a system of words as in Section 1 there is a procedure \(\mathsf{Add}(V,\lambda,t)\), for a vertex \(V\), an element \(\lambda\in\mathbb F\) and an index \(t\le p\), with the following property. Whatever the registers of the pool contain before the call,
\[
\begin{gathered}
R_t^{\text{after}}=R_t^{\text{before}}+\lambda\,\overline{v(V)},\\
R_j^{\text{after}}=R_j^{\text{before}}\quad(j\ne t).
\end{gathered}
\]
We refer to this property as (2.1).
The procedure runs in space
\[
O\bigl((d+W(V)+1)\operatorname{polylog}T\bigr),
\]
which includes the pool. In particular the value \(v(V)\) is computed in this space: put \(R_1=0\) and call \(\mathsf{Add}(V,1,1)\).

The property (2.1) is the *contract*. It says more than "the procedure computes \(v(V)\)": the result is added to what the target register contains, and every other register is given back. The proof is by induction along the order of the vertices: when the contract is proved for \(V\), it is assumed for all dependencies of \(V\), for all \(\lambda\), all \(t\) and all contents of the pool.

The numbers \(\lambda\), \(t\) and the name \(V\) of a call are kept by the caller on a stack, not in the registers.

## 3. Base vertices and ordinary vertices

**A base vertex.** \(\mathsf{Add}(V,\lambda,t)\) computes the bits of \(v(V)\) one after the other and adds \(\lambda\) times each bit to the corresponding coordinate of \(R_t\); then it adds \(\lambda\) to the last coordinate of \(R_t\). This is (2.1).

**An ordinary vertex.** Let \(U_1,\dots,U_n\) be the dependencies of \(V\). Choose indices \(q_1,\dots,q_n\) that are different from each other and from \(t\); this is possible because \(p\ge r+1\). Let \(\widetilde f_V\) be the lookup extension of the augmented function \(\overline{f_V}\): a family of \(d+1\) polynomials, one for each coordinate, each homogeneous of degree \(d\) in each of its \(n\) arguments. Let \(S_d\) and \(\omega_d\) be the points and the weights of the previous lesson. The procedure consists of \(n\) nested loops and a body.

**The loop \(j\)**, for \(j=1,\dots,n\), has a coefficient \(\kappa\); the loop \(1\) is started with \(\kappa=\lambda\). It does the following for every \(s\in S_d\) in turn:

1. it calls \(\mathsf{Add}(U_j,s,q_j)\);
2. it runs the loop \(j+1\) with the coefficient \(\kappa\,\omega_d(s)\), or, if \(j=n\), the body with this coefficient;
3. it calls \(\mathsf{Add}(U_j,-s,q_j)\).

**The body**, with a coefficient \(\kappa\), does the following for every coordinate \(z\): it computes the element \(\widetilde f_{V,z}(R_{q_1},\dots,R_{q_n})\) and adds \(\kappa\) times it to the coordinate \(z\) of \(R_t\).

**Proof of the contract.** Let \(a_j\) be the content of \(R_{q_j}\) at the start. By the contract for \(U_j\), the call in step 1 changes \(R_{q_j}\) from \(a_j\) to \(a_j+s\overline{v(U_j)}\) and nothing else, and the call in step 3 changes it back. The body changes only \(R_t\). So, by induction from the innermost loop outwards, every loop gives back all registers other than \(R_t\); and when the body runs with the loop values \(s_1,\dots,s_n\), the registers \(R_{q_j}\) contain \(a_j+s_j\overline{v(U_j)}\). Since \(t\) is none of the \(q_j\), the changes of \(R_t\) have no effect on these arguments. The coefficient of the body is \(\lambda\prod_j\omega_d(s_j)\). So in all, with \(x_j=a_j+s_j\overline{v(U_j)}\), the coordinate \(z\) of \(R_t\) grows by
\[
\lambda\sum_{s_1,\dots,s_n\in S_d}\ \prod_{j}\omega_d(s_j)\ \widetilde f_{V,z}(x_1,\dots,x_n).
\]
By Corollary 3.2 of the previous lesson this is \(\lambda\) times the coordinate \(z\) of \(\overline{f_V(v(U_1),\dots,v(U_n))}=\overline{v(V)}\). \(\blacksquare\)

The calls in steps 1 and 3 may use all registers of the pool for their own purposes, including \(R_t\) with the part of the result that has been added so far, and the registers \(R_{q_{j'}}\) of the other loops. The contract for \(U_j\) holds for every content of the pool, so they give them back.

## 4. History vertices

Let \(V\) be a history vertex with the dependencies \(H\), \(A_1,\dots,A_N\), the guesses \(Y\) of \(g\) bits and the functions \(G_Y\), \(P_{Y,i}\). Write
\[
\begin{gathered}
h_0=\overline{v(H)},\qquad a_i=\overline{v(A_i)},\\
D=(N+1)d .
\end{gathered}
\]
Let \(\widetilde G_Y\) be the lookup extension of the augmented function \(\overline{G_Y}\) (a family of \(d+1\) polynomials in one vector), and \(\widetilde P_{Y,i}\) the lookup extension of \(P_{Y,i}\) (one polynomial in two vectors). For a coordinate \(z\) and vectors \(h,x_1,\dots,x_N\in\mathbb F^{d+1}\) put
\[
\begin{aligned}
&F_z(h;x_1,\dots,x_N)\\
&\quad=\sum_Y\widetilde G_{Y,z}(h)\prod_{i=1}^N\widetilde P_{Y,i}(h,x_i).
\end{aligned}
\]

**Lemma 4.1.** (1) \(F_z(h_0;a_1,\dots,a_N)\) is the coordinate \(z\) of \(\overline{v(V)}\). (2) For fixed \(x_1,\dots,x_N\), the polynomial \(F_z\) is homogeneous of degree \(D\) in \(h\). (3) For fixed \(h\), the polynomial \(\widetilde P_{Y,i}(h,x)\) is homogeneous of degree \(d\) in \(x\).

**Proof.** (1) At augmented words the extensions are the functions, so this is (1.1). (2) Every term is a product of \(N+1\) polynomials that are homogeneous of degree \(d\) in \(h\). (3) is Lemma 2.1 of the previous lesson. \(\blacksquare\)

**The procedure.** Choose indices \(q_H\) and \(q_A\), different from each other and from \(t\); the pool has at least three registers. \(\mathsf{Add}(V,\lambda,t)\) does the following for every \(s\in S_D\) in turn:

1. it calls \(\mathsf{Add}(H,s,q_H)\);
2. it runs the *inner part* for every coordinate \(z\) and every guess \(Y\);
3. it calls \(\mathsf{Add}(H,-s,q_H)\).

**The inner part**, for given \(s\), \(z\) and \(Y\):

1. it computes \(u=\widetilde G_{Y,z}(R_{q_H})\);
2. for \(i=1,\dots,N\) in turn, it computes an element \(\beta\) and then replaces \(u\) by \(u\beta\). To compute \(\beta\) it starts from \(\beta=0\), and for every \(s'\in S_d\) it calls \(\mathsf{Add}(A_i,s',q_A)\), computes \(c=\widetilde P_{Y,i}(R_{q_H},R_{q_A})\), calls \(\mathsf{Add}(A_i,-s',q_A)\), and adds \(\omega_d(s')\,c\) to \(\beta\);
3. it adds \(\lambda\,\omega_D(s)\,u\) to the coordinate \(z\) of \(R_t\).

Two features of the order matter. The two calls for \(H\) stand outside the loops over \(z\) and \(Y\). And of the \(N\) factors only the running product \(u\) is kept; the factors are not stored.

**Proof of the contract.** Let \(h\) and \(a\) be the contents of \(R_{q_H}\) and \(R_{q_A}\) at the start. By the contracts for \(H\) and for the \(A_i\): after step 1 and until step 3, \(R_{q_H}\) contains \(h+sh_0\) whenever a lookup is computed, because every call in between gives it back; and \(R_{q_A}\) contains \(a+s'a_i\) when \(c\) is computed, and \(a\) again after the second call. Only \(R_t\) is changed otherwise, and \(t\) is neither \(q_H\) nor \(q_A\). So
\[
\begin{aligned}
\beta&=\sum_{s'\in S_d}\omega_d(s')\,\widetilde P_{Y,i}(h+sh_0,\ a+s'a_i)\\
&=\widetilde P_{Y,i}(h+sh_0,\ a_i)
\end{aligned}
\]
by Lemma 4.1(3) and the formula for the top coefficient (Lemma 3.1(2) of the previous lesson), applied to the second argument. Hence, for fixed \(s\) and \(z\), the loop over \(Y\) adds to the coordinate \(z\) of \(R_t\)
\[
\lambda\,\omega_D(s)\,F_z(h+sh_0;\ a_1,\dots,a_N).
\]
The sum of these over \(s\in S_D\) is \(\lambda F_z(h_0;a_1,\dots,a_N)\), by Lemma 4.1(2) and the same formula with \(L=D\); here \(D\le\Delta<|\mathbb F|\). By Lemma 4.1(1) this is \(\lambda\) times the coordinate \(z\) of \(\overline{v(V)}\). Step 3 gives back \(R_{q_H}\), and \(R_{q_A}\) and all further registers were given back by every call. \(\blacksquare\)

The values \(a_i\) of the different words \(A_i\) pass through the same register \(R_{q_A}\), one after the other. What makes this possible is the form of (1.1): a product of factors, each of which contains one of the \(A_i\). A rule in which one factor contained two of them would need both in registers at the same time.

In the proof, the registers hold vectors like \(h+sh_0\), which are not augmented words: even the last coordinate, \(h_*+s\), is an arbitrary element. The extensions are polynomials and are applied to them as they are.

## 5. One pool, and the stack

**Why one pool suffices.** Inside one call, the target and the registers of the arguments are different. A call further down may use any of these registers again, as its own target or for its own arguments: by the contract, which holds for every content of the pool, it gives back all of them except its own target, and the caller looks at them only after the callee has returned. The reverse call \(\mathsf{Add}(U,-s,q)\) removes what the forward call \(\mathsf{Add}(U,s,q)\) has added, because both add a multiple of the fixed vector \(\overline{v(U)}\), which does not depend on the contents of the registers. So no call ever saves a register.

**Proof of the space bound of Theorem 2.1.** The storage consists of four parts.

*The pool.* \(p\) registers of \(d+1\) field elements: \(O(d\log T)\) bits.

*The field.* Its description, and the storage for its arithmetic and for the points and weights: \(\operatorname{polylog}T\) bits (Lemmas 1.1 and 3.1 of the previous lesson).

*The scratch area.* The values of base vertices and the lookup extensions are computed in an area of \(O(d\operatorname{polylog}T)\) bits: the counter for the tuples of words, the computation of the Boolean function, a few field elements. Such a computation calls \(\mathsf{Add}\) for no vertex, and when it is finished only one field element is kept. So one area serves all of them, and it is empty whenever a call of \(\mathsf{Add}\) is made.

*The stack.* A call that waits for a call that it has made keeps its own data on a stack:

- an ordinary vertex keeps \(V\), \(\lambda\), \(t\), the loop values \(s_1,\dots,s_j\) and the coefficient: \(\operatorname{polylog}T\) bits;
- a history vertex that waits for a call for \(H\) keeps \(V\), \(\lambda\), \(t\) and \(s\): \(\operatorname{polylog}T\) bits, because these calls stand outside the loops over \(z\) and \(Y\);
- a history vertex that waits for a call for some \(A_i\) keeps in addition \(z\), the guess \(Y\), the elements \(u\), \(\beta\), \(c\) and the values \(i\), \(s'\): \(g+\operatorname{polylog}T\) bits.

At every moment the calls that wait form a path in the system: each waits for a call for one of its dependencies. The data kept for one step of the path are at most its weight times \(\operatorname{polylog}T\). So the stack holds at most \(W(V)\operatorname{polylog}T\) bits. The call that is running has at most \(g\le d\) bits of a guess and \(\operatorname{polylog}T\) bits besides.

Together this is \(O((d+W(V)+1)\operatorname{polylog}T)\). The procedure ends, because every call is for a dependency and the dependencies form no cycles. \(\blacksquare\)

The count explains the two weights of a history vertex. A call for \(H\) is made when no guess is being tried, so it costs little. A call for \(A_i\) is made in the middle of the trial of a guess \(Y\), and the \(g\) bits of \(Y\) must wait on the stack until it returns. In the application of the next lesson, \(g\) is large, about \(T^{1/5}\) bits, and the proof arranges that a path contains few steps of the expensive kind.

The running time is enormous: a history vertex with guesses of \(g\) bits makes more than \(2^g\) calls for each \(A_i\), each of which starts the same again further down. Only the storage is bounded.

## 6. Exercises

**6.1.** Let \(d=1\), and let \(V\) be an ordinary vertex with one dependency \(U\), a base vertex with the value \(v\), and \(f_V(v)=1-v\). Follow \(\mathsf{Add}(V,\lambda,1)\) with \(q_1=2\) from the contents \(R_1=(x_1,x_*)\), \(R_2=(y_1,y_*)\), and check the contract. (Use Example 3.3 of the previous lesson.)

**6.2.** A system has base vertices \(A_0\), \(H_0\), a history vertex \(H_1\) with the dependencies \(H=H_0\) and \(A_1=A_0\) and guesses of \(g\) bits, an ordinary vertex \(A'\) with the dependencies \(A_0\) and \(H_1\), and a history vertex \(H_2\) with \(H=H_1\), \(A_1=A'\) and guesses of \(g\) bits. Find \(W(H_2)\).

**6.3.** Suppose the procedure for a history vertex were changed so that the calls for \(H\) are made inside the loop over the guesses. Which weight would the dependency \(H\) need, and what would the bound of Theorem 2.1 be for a chain \(H_k,H_{k-1},\dots,H_0\) of history vertices, each with the dependency \(H\) equal to the next one and with base vertices as the \(A_i\)? Compare with the true bound.

**6.4.** Show that (1.1) holds if exactly three guesses pass all tests at the values of the system and the three words \(G_Y(v(H))\) for them add up, bit by bit modulo two, to \(v(V)\). Why is the last coordinate right?

**6.5.** How many calls \(\mathsf{Add}(A_i,\cdot,\cdot)\), for a fixed \(i\), does one run of the procedure for a history vertex make?

## 7. Solutions

**6.1.** \(\widetilde f_V\) has two coordinates: the extension \(z_*-z_1\) of \(1-v\), and the extension \(z_*\) of the constant \(1\) (here \(d=1\)). With \(S_1=\{0,1\}\) and both weights \(1\): for \(s=0\) the calls change nothing, and the body adds \(\lambda(y_*-y_1,\ y_*)\) to \(R_1\). For \(s=1\), \(R_2\) becomes \((y_1+v,\ y_*+1)\), the body adds \(\lambda(y_*+1-y_1-v,\ y_*+1)\), and \(R_2\) is given back. In characteristic two the sum of the two additions is \(\lambda(1-v,\ 1)=\lambda\,\overline{f_V(v)}\), and \(R_2=(y_1,y_*)\) at the end.

**6.2.** The steps and their weights: \(H_2\to H_1\) (1), \(H_2\to A'\) (\(g+1\)), \(A'\to A_0\) (1), \(A'\to H_1\) (1), \(H_1\to H_0\) (1), \(H_1\to A_0\) (\(g+1\)). The heaviest path is \(H_2\to A'\to H_1\to A_0\) with the weight \((g+1)+1+(g+1)=2g+3\).

**6.3.** A call for \(H\) would then wait with a guess on the stack, so the weight would be \(g+1\), and the chain would give \(W(H_k)=k(g+1)\) and the bound \(O((d+kg+k)\operatorname{polylog}T)\). With the true procedure every step of the chain has the weight \(1\), a path ends with at most one step of the weight \(g+1\) to a base vertex, and \(W(H_k)=(k-1)+(g+1)=k+g\).

**6.4.** In the sum (1.1) only the three passing guesses have a product equal to \(1\). The first \(d\) coordinates of the sum are the sums of the bits of the three words in \(\mathbb F\), which has characteristic two; so they are the sums modulo two, the bits of \(v(V)\). The last coordinate is \(1+1+1=1\) in characteristic two, as it must be for an augmented word. With two passing guesses the last coordinate would be \(0\), and (1.1) would fail.

**6.5.** For every \(s\in S_D\), every coordinate \(z\), every guess \(Y\) and every \(s'\in S_d\) there are two calls: \(2\,(D+1)(d+1)\,2^g\,(d+1)\).

## References

- [OpenAI-S] OpenAI, *Simulating One-Tape Time in Two-Fifths-Power Space*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026

# Iterated matrix multiplication and depth-five circuits

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The entry of a product of \(n\) matrices of size \(n\times n\) is a polynomial in the \(n^3\) entries of the matrices. It can be computed with about \(n^4\) additions and multiplications, by multiplying the matrices one after the other; but this computation has \(n\) layers of multiplications. How many operations are needed if the computation may have only a bounded number of layers? [OpenAI-D] answers this for five layers that alternate between sums and products, under the condition that every gate computes a homogeneous polynomial: about \(n^{\sqrt n}\) gates are necessary, and also sufficient.

This lesson defines the polynomial and the circuits, states the theorem, describes what a circuit of this kind computes, and proves the upper bound. The lower bound is proved in the other four lessons of the course.

- The polynomial \(\operatorname{IMM}_{w,d}\) and its paths (Section 1).
- Circuits with five layers and syntactic homogeneity (Section 2).
- The theorem and the plan of its proof (Section 3).
- What a homogeneous circuit computes (Lemmas 4.1 and 4.2).
- A circuit of size \(n^{\sqrt n+4}\) (Proposition 5.1).

The lesson follows [OpenAI-D, Sections 1, 3.3 and 6]. It needs only polynomials in several variables.

## 1. The polynomial

Let \(w,d\ge1\) be integers, and let \(X^{(1)},\dots,X^{(d)}\) be matrices of size \(w\times w\) whose entries \(x^{(t)}_{i,j}\) are \(dw^2\) different variables. Put
\[
\operatorname{IMM}_{w,d}=\bigl(X^{(1)}X^{(2)}\cdots X^{(d)}\bigr)_{1,1},
\]
the entry of the product in the first row and the first column. By the rule for the product of matrices,
\[
\operatorname{IMM}_{w,d}=\sum_{i_1,\dots,i_{d-1}}x^{(1)}_{1,i_1}\,x^{(2)}_{i_1,i_2}\cdots x^{(d)}_{i_{d-1},1},
\]
where the indices run from \(1\) to \(w\). The matrix \(X^{(t)}\) is the *layer* \(t\). A *path* is a sequence \(P=(p_0,p_1,\dots,p_d)\) with \(p_0=p_d=1\) and \(p_1,\dots,p_{d-1}\) between \(1\) and \(w\); its *coordinate in the layer \(t\)* is the variable \(E_t(P)=x^{(t)}_{p_{t-1},p_t}\). So there are \(w^{d-1}\) paths, and
\[
\operatorname{IMM}_{w,d}=\sum_P\ \prod_{t=1}^dE_t(P).
\]
The polynomial is homogeneous of degree \(d\), and every monomial contains exactly one variable of each layer. We always regard it as a polynomial in all \(dw^2\) variables, although the variables \(x^{(1)}_{i,j}\) with \(i\ne1\) and \(x^{(d)}_{i,j}\) with \(j\ne1\) do not occur in it.

The course is about \(w=d=n\): the polynomial \(\operatorname{IMM}_{n,n}\) of degree \(n\) in \(n^3\) variables.

## 2. Circuits with five layers

Let \(K\) be a field. An *arithmetic circuit* over \(K\) is a finite directed graph without cycles. Its vertices without incoming edges are the *leaves*; a leaf is a variable or an element of \(K\). The other vertices are *gates*. A *sum gate* computes a linear combination, with coefficients in \(K\) that are part of the circuit, of the polynomials of its inputs. A *product gate* computes the product of the polynomials of its inputs. A gate may be an input of several gates, and it may occur several times among the inputs of one gate; at a product gate every occurrence is a factor.

A *\(\Sigma\Pi\Sigma\Pi\Sigma\) circuit* has five layers of gates. From the output down to the leaves they consist of sum gates, product gates, sum gates, product gates and sum gates. The first layer is one gate, the *output*. The inputs of a gate of one layer are gates of the next layer, and the inputs of the gates of the fifth layer are leaves. We call the layers: the output sum, the *upper products*, the *middle sums*, the *lower products* and the *bottom sums*. The number of the inputs of a gate is not bounded; in particular a bottom sum may contain any number of variables.

**Definition.** A circuit is *syntactically homogeneous* if every vertex can be given a *formal degree* such that: a variable has the formal degree \(1\) and an element of \(K\) the formal degree \(0\); the formal degree of a product gate is the sum of the formal degrees of its inputs, counted with their multiplicities; and all inputs of a sum gate have the same formal degree, which is also the formal degree of the sum gate.

The *size* of a circuit is the number of its vertices, the leaves included.

**Lemma 2.1.** In a syntactically homogeneous circuit, the polynomial computed at a vertex of the formal degree \(e\) is \(0\) or homogeneous of degree \(e\).

**Proof.** By induction along the circuit. For leaves this is the definition. A linear combination of polynomials that are \(0\) or homogeneous of degree \(e\) is \(0\) or homogeneous of degree \(e\). A product of polynomials that are \(0\) or homogeneous of the degrees \(e_1,\dots,e_r\) is \(0\) or homogeneous of degree \(e_1+\dots+e_r\). \(\blacksquare\)

## 3. The theorem

**Theorem 3.1** ([OpenAI-D]). There is a number \(n_0\) such that for every \(n\ge n_0\) and every field \(K\) of characteristic zero, every syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit over \(K\) that computes \(\operatorname{IMM}_{n,n}\) has a size of at least
\[
n^{\sqrt n/400}.
\]

No condition is put on the bottom sums, on the numbers of inputs, or on the sharing of gates. Proposition 5.1 below gives circuits of the size \(n^{\sqrt n+4}\) over every field. So the least size is \(n^{c\sqrt n}\) with \(c\) between \(\tfrac1{400}\) and \(1\) up to lower-order terms. Without the bound on the number of layers, \(\operatorname{IMM}_{n,n}\) has circuits of a size polynomial in \(n\).

The theorem is proved in the last lesson, [The sum over type words and the lower bound](the-sum-over-type-words-and-the-lower-bound.md).

**The plan.** The proof assigns to every homogeneous polynomial \(g\) of degree \(n\) in the \(n^3\) variables a number \(R(g)\), the rank of a linear map that is built from \(g\) ([A rank measure from differentiation and multiplication](a-rank-measure-from-differentiation-and-multiplication.md)). The map goes from a space of dimension \(D\), so \(R(g)\le D\). Two estimates are proved for large \(n\):

- if \(g\) is computed by a syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit of size \(S\), then \(R(g)\le2S^2D\exp(11\sqrt n)\,n^{-\sqrt n/100}\) ([The rank of a depth-five circuit](the-rank-of-a-depth-five-circuit.md));
- \(R(\operatorname{IMM}_{n,n})\ge D\exp(-6\sqrt n)\) ([Trace moments and paths](trace-moments-and-paths.md) and the last lesson).

Together they force \(S^2\ge\tfrac12\exp(-17\sqrt n)\,n^{\sqrt n/100}\).

## 4. What a homogeneous circuit computes

A *linear form* is a homogeneous polynomial of degree \(1\) or the polynomial \(0\).

**Lemma 4.1.** Let \(g\ne0\) be computed by a syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit of size \(S\) whose output has the formal degree \(n\ge1\). Then
\[
g=\sum_{i=1}^{S'}c_i\,G_i,\qquad S'\le S,\quad c_i\in K,
\]
where every \(G_i\) is a product
\[
G_i=Q_1Q_2\cdots Q_r
\]
of polynomials \(Q_j\) with the following properties (the number \(r\) and the \(Q_j\) depend on \(i\)):

1. \(Q_j\) is homogeneous of a degree \(e_j\ge1\), and \(e_1+\dots+e_r=n\);
2. \(Q_j\) is a sum of at most \(S\) polynomials, each of which is an element of \(K\) times a product of \(e_j\) linear forms.

**Proof.** We go through the layers from the bottom, using Lemma 2.1.

*Bottom sums.* All inputs of a bottom sum are leaves of the same formal degree. If it is \(1\), they are variables, and the gate computes a linear form. If it is \(0\), the gate computes an element of \(K\).

*Lower products.* A lower product of the formal degree \(e\) is a product of bottom sums. Exactly \(e\) of its factors, counted with multiplicity, have the formal degree \(1\); the others compute elements of \(K\). So it computes an element of \(K\) times a product of \(e\) linear forms.

*Middle sums.* A middle sum of the formal degree \(e\) is a linear combination of lower products of the formal degree \(e\). Several occurrences of the same lower product can be combined by adding their coefficients, and there are at most \(S\) different lower products. So a middle sum computes a sum of at most \(S\) polynomials, each an element of \(K\) times a product of \(e\) linear forms. This is property 2, with \(e\) in place of \(e_j\).

*Upper products.* An upper product is a product of middle sums, counted with multiplicity. Its factors of the formal degree \(0\) compute elements of \(K\); let \(c\) be their product. If \(c=0\), or if one of the other factors computes \(0\), the upper product computes \(0\). Otherwise it computes \(c\,Q_1\cdots Q_r\), where the \(Q_j\) are the polynomials of the factors of positive formal degree \(e_j\); they are not \(0\), so they are homogeneous of degree \(e_j\) by Lemma 2.1.

*The output.* The output is a linear combination of upper products, all of the formal degree \(n\); again occurrences of the same gate are combined, and there are at most \(S\) different ones. Leave out those that compute \(0\). For the others, the formal degrees of the factors add up to \(n\), so \(e_1+\dots+e_r=n\). Since \(n\ge1\), there is at least one factor. \(\blacksquare\)

The lemma does not use the number of the edges of the circuit, and it holds whatever the bottom sums are. If a middle sum occurs \(h\) times in an upper product, it gives \(h\) of the factors \(Q_j\).

**Lemma 4.2.** In the situation of Lemma 4.1, for a product \(G_i=Q_1\cdots Q_r\) and one index \(j_0\),
\[
G_i=\sum_{l=1}^{S''}c_l'\,\ell_{l,1}\ell_{l,2}\cdots\ell_{l,e}\prod_{j\ne j_0}Q_j
\]
with \(S''\le S\), \(e=e_{j_0}\), elements \(c_l'\in K\) and linear forms \(\ell_{l,1},\dots,\ell_{l,e}\).

**Proof.** Replace the factor \(Q_{j_0}\) by its sum from property 2 and multiply out. \(\blacksquare\)

So one factor can be expanded into products of linear forms at the cost of a factor \(S\) in the number of the terms, while the other factors are kept as they are. The proof of the lower bound does this for one factor of large degree.

## 5. A circuit of size \(n^{\sqrt n+4}\)

**Proposition 5.1** ([OpenAI-D]). Let \(K\) be a field and \(n\ge2\). Put \(t=\lceil\sqrt n\rceil\) and \(r=\lceil n/t\rceil\). There is a syntactically homogeneous \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit over \(K\) that computes \(\operatorname{IMM}_{n,n}\) and has a size of at most
\[
\begin{aligned}
&2n^3+rn^2+rn^{t+1}+n^{r-1}+1\\
&\qquad\le n^{\sqrt n+4}.
\end{aligned}
\]

**Proof.** *Blocks.* Divide the \(n\) layers into \(r\) blocks of consecutive layers, of the lengths \(l_1,\dots,l_r\) with \(1\le l_j\le t\) and \(l_1+\dots+l_r=n\). Let \(Y^{(j)}\) be the product of the matrices of the block \(j\). An entry \(Y^{(j)}_{a,b}\) is a sum of \(n^{l_j-1}\) monomials of degree \(l_j\), one for each choice of the \(l_j-1\) inner indices. By the rule for the product of matrices, with \(a_0=a_r=1\),
\[
\operatorname{IMM}_{n,n}=\sum_{a_1,\dots,a_{r-1}}\ \prod_{j=1}^rY^{(j)}_{a_{j-1},a_j}.
\]

*The circuit.* There are \(n^3\) leaves, the variables. Every variable is the one input of a bottom sum: \(n^3\) gates. For every block \(j\) and every pair \((a,b)\), the monomials of \(Y^{(j)}_{a,b}\) are computed by lower products, and added by one middle sum: \(n^{l_j+1}\) lower products and \(n^2\) middle sums for the block. For every choice of \(a_1,\dots,a_{r-1}\) one upper product multiplies the \(r\) middle sums of the entries \(Y^{(j)}_{a_{j-1},a_j}\): \(n^{r-1}\) gates. The output adds them.

*Formal degrees.* The bottom sums have the formal degree \(1\), the lower products and the middle sums of the block \(j\) the formal degree \(l_j\), and the upper products and the output the formal degree \(n\).

*The size.* The number of the vertices is at most
\[
2n^3+rn^2+\sum_{j=1}^rn^{l_j+1}+n^{r-1}+1 ,
\]
and \(l_j\le t\). For the second bound, note first that \(n/t\le\sqrt n\le t\), so \(r\le t\le n\). Let \(n\ge3\), so \(t\ge2\). Then \(2n^3+rn^2\le3n^3\le n^{t+2}\), \(rn^{t+1}\le n^{t+2}\) and \(n^{r-1}+1\le n^{t+2}\). So the size is at most \(3n^{t+2}\le n^{t+3}\le n^{\sqrt n+4}\), because \(t\le\sqrt n+1\). For \(n=2\): \(t=2\), \(r=1\), and the bound is \(16+4+8+1+1=30\le2^{\sqrt2+4}\). \(\blacksquare\)

The circuit uses only four of the five layers for real work; its bottom sums have one input each. The blocks of length \(\sqrt n\) balance the two expensive parts: the \(n^{t+1}\) monomials inside a block and the \(n^{r-1}\) products of blocks.

## 6. Exercises

**6.1.** Write \(\operatorname{IMM}_{2,3}\) as a sum of monomials. Which of its twelve variables do not occur?

**6.2.** Show that \(\operatorname{IMM}_{w,d}\) is computed by an arithmetic circuit with at most \(2dw^3\) gates (and unboundedly many layers).

**6.3.** Give a \(\Sigma\Pi\Sigma\Pi\Sigma\) circuit that computes \(x_1x_2+x_1\) and is not syntactically homogeneous. Why can no syntactically homogeneous circuit compute this polynomial?

**6.4.** A middle sum of the formal degree \(2\) computes \(Q=x_1x_2-x_1x_2=0\). It is one of two factors of an upper product whose other factor has the formal degree \(3\). What does Lemma 4.1 do with this upper product?

**6.5.** Compute the bound \(2n^3+rn^2+rn^{t+1}+n^{r-1}+1\) of Proposition 5.1 for \(n=9\), and compare it with \(9^{\sqrt9+4}\) and with the number \(9^8\) of the paths.

## 7. Solutions

**6.1.** With \(p_0=p_3=1\) and \(p_1,p_2\in\{1,2\}\):
\[
\begin{aligned}
\operatorname{IMM}_{2,3}={}&x^{(1)}_{1,1}x^{(2)}_{1,1}x^{(3)}_{1,1}+x^{(1)}_{1,1}x^{(2)}_{1,2}x^{(3)}_{2,1}\\
&+x^{(1)}_{1,2}x^{(2)}_{2,1}x^{(3)}_{1,1}+x^{(1)}_{1,2}x^{(2)}_{2,2}x^{(3)}_{2,1}.
\end{aligned}
\]
The variables \(x^{(1)}_{2,1},x^{(1)}_{2,2}\) and \(x^{(3)}_{1,2},x^{(3)}_{2,2}\) do not occur.

**6.2.** Compute the first row of \(X^{(1)}\cdots X^{(t)}\) for \(t=1,2,\dots,d\): the row for \(t\) is the row for \(t-1\) times the matrix \(X^{(t)}\). Each of its \(w\) entries is a sum of \(w\) products of two factors: \(w^2\) product gates and \(w\) sum gates per step, fewer than \(2w^3\). There are \(d\) steps.

**6.3.** For example: bottom sums for \(x_1\), \(x_2\) and for the element \(1\); two lower products \(x_1x_2\) and \(x_1\cdot1\); one middle sum that adds them; one upper product with this one input; the output. The middle sum has inputs of the formal degrees \(2\) and \(1\). No syntactically homogeneous circuit computes the polynomial, because by Lemma 2.1 the output would compute a homogeneous polynomial, and \(x_1x_2+x_1\) is not homogeneous.

**6.4.** The upper product computes \(0\), although its formal degree is \(5\). In the proof of Lemma 4.1 it is left out of the sum for \(g\). A gate that computes \(0\) keeps its formal degree; nothing else is needed.

**6.5.** \(n=9\), \(t=3\), \(r=3\): the bound is \(2\cdot729+3\cdot81+3\cdot9^4+9^2+1\), that is \(1458+243+19683+81+1=21{,}466\). This is far below \(9^7=4{,}782{,}969\), and below the number \(9^8=43{,}046{,}721\) of the paths, which is the size of the circuit that computes every monomial separately.

## References

- [OpenAI-D] OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication*, OpenAI Math Release preprint, 25 September 2026, Sections 1, 3 and 6. https://github.com/openai/math/tree/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026

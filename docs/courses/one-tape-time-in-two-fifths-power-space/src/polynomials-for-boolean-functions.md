# Polynomials for Boolean functions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The algorithm of [OpenAI-S] computes with words of bits, but it stores them as vectors over a finite field and applies polynomials to them. The reason is a property of polynomials that Boolean functions do not have: the value of a homogeneous polynomial at a vector \(v\) can be recovered from its values at the shifted vectors \(a+sv\), whatever \(a\) is. So a register that already contains something useful, \(a\), can be used for the computation and then be given back unchanged. This lesson proves the three algebraic facts that the evaluator of the next lesson uses.

- Finite fields of characteristic two of every size, with arithmetic in small space (Lemma 1.1).
- Every Boolean function of words is the restriction of a polynomial that is homogeneous in each word (Lemma 2.1).
- The top coefficient of a polynomial as a weighted sum of values (Lemma 3.1), and the value of a function from shifted arguments (Corollary 3.2).

The lesson follows [OpenAI-S, Section 2]. It needs polynomials over a field and nothing from the first lesson, [One-tape machines, blocks and visits](one-tape-machines-blocks-and-visits.md), except the meaning of "space".

## 1. Fields of characteristic two

**Lemma 1.1.** For every integer \(\Delta\ge1\) there is a field \(\mathbb F\) with \(2^m\) elements, where \(\Delta<2^m\le\max\{2,\Delta^2\}\). Its elements are the strings of \(m\) bits; the sum of two elements is their sum bit by bit modulo \(2\). There is an algorithm that, given \(\Delta\), lists the elements of \(\mathbb F\) in a fixed order and computes products and inverses in space \(O(\log^C(\Delta+2))\) for a fixed \(C\).

**Proof.** *One step.* Let \(K\) be a finite field in which \(1+1=0\). The map \(\wp(x)=x^2+x\) from \(K\) to \(K\) is additive, since \((x+y)^2=x^2+y^2\) in \(K\). Its kernel consists of the \(x\) with \(x(x+1)=0\), that is, of \(0\) and \(1\). So its image has \(|K|/2\) elements, and there is an element \(a\in K\) that is not in the image. The polynomial \(X^2+X+a\) has no root in \(K\); it has degree two, so it is irreducible, and
\[
K'=K[X]/(X^2+X+a)
\]
is a field with \(|K|^2\) elements, in which again \(1+1=0\). Its elements are the pairs \((u,w)\) of elements of \(K\), standing for \(u+wX\). They are added entry by entry, and since \(X^2=X+a\) in \(K'\),
\[
\begin{aligned}
&(u+wX)(u'+w'X)\\
&\quad=(uu'+a\,ww')\\
&\qquad+(uw'+wu'+ww')X .
\end{aligned}
\]

*The tower.* Start with the field \(\mathbb F_2=\{0,1\}\) and repeat the step until the number of the elements exceeds \(\Delta\). The fields have \(2,4,16,256,\dots\) elements, each number the square of the one before. The last number \(2^m\) exceeds \(\Delta\), and the one before it, if there is one, does not. So \(2^m\le\max\{2,\Delta^2\}\) and \(m=O(\log(\Delta+2))\). An element of the last field is a pair of elements of the field before it, and so on down to bits; this writes it as a string of \(m\) bits, and addition is addition of bits.

*Space.* In every step the algorithm takes for \(a\) the first element, in the order of the strings, that is not of the form \(x^2+x\); it finds it by trying all \(a\) and all \(x\) with two counters. The constants \(a\) of all steps together have fewer than \(m\) bits. A product in a field of the tower is computed by the formula above from five products in the field before it, one after the other. The depth of this recursion is the number of the steps, which is \(O(\log m)\), and every level keeps a few elements. An inverse of \(y\ne0\) is found by trying all elements \(y'\) until \(yy'=1\). The elements are listed by a counter of \(m\) bits. All this needs a number of bits that is polynomial in \(m\). \(\blacksquare\)

Since \(1+1=0\), every element is its own negative: \(-s=s\). Subtraction and addition are the same operation.

**Example 1.2.** In \(\mathbb F_2\), \(\wp(0)=\wp(1)=0\), so \(a=1\): the first step gives the field with four elements \(u+wX\), \(X^2=X+1\). There \(\wp(X)=X^2+X=1\) and \(\wp(X+1)=1\), so the image of \(\wp\) is \(\{0,1\}\), and the next step can take \(a=X\).

## 2. Lookup extensions

Fix a field \(\mathbb F\) as in Lemma 1.1 and an integer \(d\ge1\). A *word* is a string \(v=(v_1,\dots,v_d)\) of \(d\) bits. Its *augmented word* is the vector
\[
\overline v=(v_1,\dots,v_d,1)\in\mathbb F^{d+1} .
\]
For a vector \(z\in\mathbb F^{d+1}\) we write \(z=(z_1,\dots,z_d,z_*)\); the last coordinate \(z_*\) need not be \(1\).

A polynomial in the coordinates of \(z\) is *homogeneous of degree \(L\)* if all its monomials have the total degree \(L\); the zero polynomial counts as homogeneous of every degree. Then \(Q(\lambda z)=\lambda^LQ(z)\).

**Definition.** For a word \(u\) let
\[
B_u(z)=\prod_{l=1}^d\beta_l ,
\]
where \(\beta_l=z_l\) if \(u_l=1\), and \(\beta_l=z_*-z_l\) if \(u_l=0\).
This polynomial is homogeneous of degree \(d\). At an augmented word, \(B_u(\overline v)=1\) if \(v=u\), and \(B_u(\overline v)=0\) if \(v\ne u\): a factor with \(u_l\ne v_l\) is \(0\).

**Lemma 2.1** (lookup extension). Let \(f\) be a function that assigns a bit to every \(n\)-tuple of words. Write \(\mathbf u=(u^{(1)},\dots,u^{(n)})\) for an \(n\)-tuple of words and \(\mathbf z=(z^{(1)},\dots,z^{(n)})\) for an \(n\)-tuple of vectors of \(\mathbb F^{d+1}\). The polynomial
\[
\widetilde f(\mathbf z)=\sum_{\mathbf u}f(\mathbf u)\prod_{j=1}^nB_{u^{(j)}}(z^{(j)}),
\]
where the sum runs over all \(n\)-tuples of words, has the following properties.

1. \(\widetilde f(\overline{v^{(1)}},\dots,\overline{v^{(n)}})=f(v^{(1)},\dots,v^{(n)})\) for all words \(v^{(1)},\dots,v^{(n)}\).
2. \(\widetilde f\) is homogeneous of degree \(d\) in each of its \(n\) arguments separately.
3. If \(n\) is fixed and \(f\) is computed in space \(S\) from its arguments, then \(\widetilde f\) is computed at given vectors in space \(O(S+d\log|\mathbb F|+\log^C|\mathbb F|)\), without changing the given vectors.

**Proof.** (1) At augmented words only the term with \(u^{(j)}=v^{(j)}\) for all \(j\) is not \(0\), and its product is \(1\). (2) Every term is a product of one polynomial \(B_u\) in each argument. (3) The algorithm runs through the \(n\)-tuples of words with a counter of \(nd\) bits, computes \(f\) for each, multiplies the factors \(\beta_l\) one after the other and adds the product to a running sum. Apart from the counter and the computation of \(f\), it keeps a constant number of field elements. \(\blacksquare\)

A function \(f\) whose values are words has an extension coordinate by coordinate. We extend the *augmented* function \(\overline f\): its \(d\) coordinates are the bits of \(f\), and its last coordinate is the constant \(1\). So \(\widetilde f\) is a family of \(d+1\) polynomials, and \(\widetilde f(\overline v)=\overline{f(v)}\).

**The constant function is not the constant polynomial.** From the definition, by multiplying out the product \(\prod_l(z_l+(z_*-z_l))\),
\[
\sum_uB_u(z)=z_*^{\,d} .
\]
So the extension of the constant function \(1\) of one word is \(z_*^d\), and for a function of two words it is \((z^{(1)}_*)^d(z^{(2)}_*)^d\). It is \(1\) at augmented words, but not elsewhere, and the evaluator of the next lesson applies the extensions to vectors that are not augmented words. This is why the last coordinate is carried along: it makes every extension homogeneous.

The extension \(\widetilde f\) has \(2^{nd}\) terms, and computing it takes a long time. Time is not counted.

## 3. The top coefficient

**Lemma 3.1.** Let \(L\ge0\) be an integer with \(L<|\mathbb F|\), let \(S_L\) be a set of \(L+1\) elements of \(\mathbb F\), and for \(s\in S_L\) let
\[
\omega_L(s)=\Bigl(\prod_{u\in S_L,\ u\ne s}(s-u)\Bigr)^{-1} .
\]

1. For every polynomial \(p\) in one variable \(X\) of degree at most \(L\), the coefficient of \(X^L\) in \(p\) is
\[
\sum_{s\in S_L}\omega_L(s)\,p(s) .
\]
2. Let \(Q\) be a polynomial in the coordinates of a vector that is homogeneous of degree \(L\). Then for all vectors \(a\) and \(v\)
\[
\sum_{s\in S_L}\omega_L(s)\,Q(a+sv)=Q(v) .
\]

**Proof.** (1) For \(s\in S_L\) let \(\ell_s(X)=\prod_{u\ne s}\frac{X-u}{s-u}\), a polynomial of degree \(L\) with \(\ell_s(s)=1\) and \(\ell_s(u)=0\) for the other \(u\in S_L\). The polynomial \(p-\sum_sp(s)\ell_s\) has degree at most \(L\) and the \(L+1\) roots \(s\in S_L\), so it is \(0\). The coefficient of \(X^L\) in \(\ell_s\) is \(\omega_L(s)\).

(2) For a monomial \(m\) of total degree \(L\) in the coordinates, \(m(a+Xv)\) is a product of \(L\) factors \(a_l+Xv_l\). It is a polynomial in \(X\) of degree at most \(L\), and its coefficient of \(X^L\) is the product of the \(v_l\), that is, \(m(v)\). So \(Q(a+Xv)\) has degree at most \(L\) in \(X\) and the coefficient \(Q(v)\) at \(X^L\). Apply (1). \(\blacksquare\)

The proof uses no derivatives and no division by integers, so it holds in characteristic two for every \(L<|\mathbb F|\). We always take for \(S_L\) the first \(L+1\) elements in the order of Lemma 1.1; then the points and the weights \(\omega_L(s)\) are computed in space \(O(\log^C|\mathbb F|)\) when they are needed, and are not stored.

**Corollary 3.2** (a value from shifted arguments). Let \(f\) assign a bit to every \(n\)-tuple of words, and let \(d<|\mathbb F|\). Let \(v^{(1)},\dots,v^{(n)}\) be words and \(a^{(1)},\dots,a^{(n)}\in\mathbb F^{d+1}\) vectors, and for \(s_1,\dots,s_n\in S_d\) put \(x^{(j)}=a^{(j)}+s_j\overline{v^{(j)}}\). Then
\[
\begin{aligned}
&\sum_{s_1,\dots,s_n\in S_d}\ \prod_{j=1}^n\omega_d(s_j)\ \widetilde f\bigl(x^{(1)},\dots,x^{(n)}\bigr)\\
&\qquad=f(v^{(1)},\dots,v^{(n)}) .
\end{aligned}
\]

**Proof.** Apply Lemma 3.1(2) to the first argument, with the others fixed: by Lemma 2.1(2), \(\widetilde f\) is homogeneous of degree \(d\) in it. The sum over \(s_1\) replaces the first argument by \(\overline{v^{(1)}}\). Continue with the second argument, and so on. At the end \(\widetilde f\) stands at augmented words, where it is \(f\) by Lemma 2.1(1). \(\blacksquare\)

The corollary is the heart of the method. Suppose that \(n\) registers contain arbitrary vectors \(a^{(j)}\), which must not be lost. To compute \(f(v^{(1)},\dots,v^{(n)})\), one adds \(s_j\overline{v^{(j)}}\) to the \(j\)-th register, evaluates \(\widetilde f\) on the registers, and subtracts \(s_j\overline{v^{(j)}}\) again; this for all choices of the \(s_j\), adding up the results with the weights. At the end the registers contain the \(a^{(j)}\) again, and the sum is the value of \(f\). No copy of a register was made.

**Example 3.3.** Let \(d=1\) and \(n=1\), so a word is one bit \(v\), \(\overline v=(v,1)\), and \(B_1(z)=z_1\), \(B_0(z)=z_*-z_1\). For the function \(f(v)=1-v\), \(\widetilde f(z)=z_*-z_1\). Take \(S_1=\{0,1\}\), with \(\omega_1(0)=(0-1)^{-1}=1\) and \(\omega_1(1)=1\) in characteristic two. For a register with the content \(a=(a_1,a_*)\),
\[
\begin{aligned}
&\widetilde f(a)+\widetilde f(a+\overline v)\\
&\quad=(a_*-a_1)+(a_*+1-a_1-v)\\
&\quad=1-v ,
\end{aligned}
\]
since the terms with \(a\) occur twice and cancel. The content \(a\) has no effect on the result.

## 4. Exercises

**4.1.** Write the multiplication table of the field with four elements of Example 1.2, and find the inverse of \(X\).

**4.2.** Let \(d=2\). Write the four polynomials \(B_u\), check that their sum is \(z_*^2\), and write the extension of the function \(f(v)=v_1v_2\) and of the function \(f(v)=1\).

**4.3.** Let \(\mathbb F\) have four elements, as in Example 1.2, and \(S_2=\{0,1,X\}\). Compute the three weights \(\omega_2(s)\) and check Lemma 3.1(1) for the polynomial \(p(Y)=Y^2\) in a variable \(Y\).

**4.4.** Show that Lemma 3.1(2) is false for a polynomial that is not homogeneous: give \(Q\) of degree \(L=1\) in one coordinate, and \(a\), \(v\), with \(\sum_s\omega_1(s)Q(a+sv)\ne Q(v)\).

**4.5.** In Corollary 3.2, how many times is \(\widetilde f\) evaluated, and how many additions of a multiple of an augmented word to a register are made if the loops over \(s_1,\dots,s_n\) are nested, the loop of \(s_1\) outermost, and every loop adds \(s_j\overline{v^{(j)}}\) before its body and subtracts it afterwards?

## 5. Solutions

**4.1.** The elements are \(0,1,X,X+1\), and \(X^2=X+1\). So \(X\cdot X=X+1\), \(X(X+1)=X^2+X=1\), \((X+1)(X+1)=X^2+1=X\). The inverse of \(X\) is \(X+1\).

**4.2.** \(B_{11}=z_1z_2\), \(B_{10}=z_1(z_*-z_2)\), \(B_{01}=(z_*-z_1)z_2\), \(B_{00}=(z_*-z_1)(z_*-z_2)\). Their sum is \((z_1+(z_*-z_1))(z_2+(z_*-z_2))=z_*^2\). The function \(v_1v_2\) is \(1\) only at \(u=11\), so its extension is \(z_1z_2\). The extension of the function \(1\) is the sum of all four, \(z_*^2\).

**4.3.** Use \(-1=1\). \(\omega_2(0)\) is the inverse of \((0-1)(0-X)=X\), that is \(X+1\). \(\omega_2(1)\) is the inverse of \((1-0)(1-X)=X+1\), that is \(X\). \(\omega_2(X)\) is the inverse of \((X-0)(X-1)=X^2+X=1\), that is \(1\). For \(p(Y)=Y^2\) the values at \(0,1,X\) are \(0,1,X+1\), and \((X+1)\cdot0+X\cdot1+1\cdot(X+1)=1\), the coefficient of \(Y^2\).

**4.4.** Let \(Q(z)=z_1+1\), \(a=0\), \(v=1\) (one coordinate), over any field of characteristic two with \(S_1=\{0,1\}\) and weights \(1,1\). Then \(Q(0)+Q(1)=1+0=1\), but \(Q(v)=Q(1)=0\). The sum is the coefficient of the first power of \(s\) in \(Q(a+sv)=sv+1\), which is \(v=1\); the constant term of \(Q\) is lost.

**4.5.** \(\widetilde f\) is evaluated \((d+1)^n\) times. The loop of \(s_j\) runs \((d+1)^j\) times in all (once for every choice of \(s_1,\dots,s_j\)) and makes two additions each time: \(2\sum_{j=1}^n(d+1)^j\) additions.

## References

- [OpenAI-S] OpenAI, *Simulating One-Tape Time in Two-Fifths-Power Space*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026

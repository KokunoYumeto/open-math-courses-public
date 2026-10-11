# An explicit language

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson defines the language of the theorem in [Depth-three circuits and the square-root barrier](depth-three-circuits-and-the-square-root-barrier.md). An input consists of *data bits* and of *parameter bits*. The parameter bits describe a linear hash function, a polynomial \(P\) over \(\mathbb F_2\), and a few elements of the ring \(\mathbb F_2[Z]/(P)\); membership is decided by evaluating a polynomial at the hash of the data. Fixing the parameter bits leaves a function of the data bits, a *slice*. The lesson proves the two properties of the construction that the next lesson, [Hard slices](hard-slices.md), turns into a hard slice: the hash is injective on small subcubes with high probability, and then the values of a random slice at any few points are independent.

The algorithm that decides membership uses the parameter bits as given. It never searches for good parameters. Good parameters only need to *exist*, because a circuit for the language yields a circuit for each slice.

## 1. Finite fields of characteristic two

We use from the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) (Judson, *Abstract Algebra: Theory and Applications*) that for every \(r\geq1\) there is a field with \(2^r\) elements ([Theorem 22.1.6](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)), and the elementary facts about polynomials over a field: division with remainder by a nonzero polynomial, and that a nonzero polynomial of degree \(n\) has at most \(n\) roots.

For a monic polynomial \(P\in\mathbb F_2[Z]\) of degree \(r\geq1\), let
\[
R_P=\mathbb F_2[Z]/(P).
\]
Division by \(P\) gives every class a unique representative of degree less than \(r\). So \(R_P\) is a ring with \(2^r\) elements and a vector space over \(\mathbb F_2\) with basis \(1,Z,\ldots,Z^{r-1}\), whether or not \(P\) is irreducible.

**Lemma 1.1.** For every \(r\geq1\) there is a monic polynomial \(P\in\mathbb F_2[Z]\) of degree \(r\) such that \(R_P\) is a field.

*Proof.* Let \(K\) be a field with \(2^r\) elements. Its characteristic is a prime \(\ell\), and \(K\) is a vector space over its subfield with \(\ell\) elements, so \(2^r\) is a power of \(\ell\) and \(\ell=2\). Thus \(K\) contains \(\mathbb F_2=\{0,1\}\), and it has dimension \(r\) over it, since a space of dimension \(v\) over \(\mathbb F_2\) has \(2^v\) elements. For \(a\in K\), the \(r+1\) powers \(1,a,\ldots,a^r\) are linearly dependent, so some nonzero polynomial over \(\mathbb F_2\) vanishes at \(a\); let \(e(a)\geq1\) be the least degree of such a polynomial, the *degree* of \(a\).

Fix \(a\) and put \(e=e(a)\). The elements \(1,a,\ldots,a^{e-1}\) are linearly independent by the choice of \(e\), and their span \(\mathbb F_2[a]\) is closed under multiplication, because \(a^e\) is a combination of lower powers. So \(\mathbb F_2[a]\) is a subring of \(K\) with \(2^e\) elements. A finite ring without zero divisors is a field: multiplication by a nonzero element is injective, hence surjective, so \(1\) is in its image. Thus \(\mathbb F_2[a]\) is a field with \(2^e\) elements. Two consequences follow.

*First*, \(K\) is a vector space over \(\mathbb F_2[a]\), of some dimension \(v\), so \(2^r=(2^e)^v\) and \(e\) divides \(r\). *Second*, \(a^{2^e}=a\): the nonzero elements of a field with \(2^e\) elements form a group of order \(2^e-1\), so \(a^{2^e-1}=1\) when \(a\neq0\).

So every element of degree \(e\) is a root in \(K\) of \(X^{2^e}-X\), and there are at most \(2^e\) of them. An element of degree less than \(r\) has a degree \(e\) dividing \(r\) with \(e\leq r/2\). The number of such elements is at most
\[
\sum_{e=1}^{\lfloor r/2\rfloor}2^e=2^{\lfloor r/2\rfloor+1}-2<2^r .
\]
So some \(a\in K\) has degree \(r\). Let \(P\) be the monic polynomial of degree \(r\) vanishing at \(a\). The ring homomorphism \(\mathbb F_2[Z]\to K\), \(Z\mapsto a\), sends \(P\) to \(0\), so it induces a homomorphism \(R_P\to K\). It maps the basis \(1,Z,\ldots,Z^{r-1}\) to the linearly independent elements \(1,a,\ldots,a^{r-1}\), so it is injective, and both sides have \(2^r\) elements. Hence \(R_P\cong K\) is a field. \(\square\)

Such a \(P\) is irreducible, and conversely \(R_P\) is a field for every irreducible \(P\) (Exercise 6.1); only the lemma is used below.

## 2. The language

**Definition 2.1.** Let an input of length \(n\) be given and put \(d=\lfloor n/5\rfloor\). If \(d<64\), reject. Otherwise let \(r=\lceil d^{2/3}\rceil\), let \(t\) be the largest even integer \(j\geq0\) with \(j^6\leq d\), and read the first \(2d+(t+2)r-1\) input bits as four consecutive blocks:

1. \(d\) *data bits* \(x=(x_1,\ldots,x_d)\);
2. \(d+r-1\) *hash bits* \(u_1,\ldots,u_{d+r-1}\);
3. \(r\) bits \(p_0,\ldots,p_{r-1}\), the coefficients of the monic polynomial \(P(Z)=Z^r+\sum_{i<r}p_iZ^i\);
4. \(t\) blocks of \(r\) bits, the coordinates of elements \(\beta_0,\ldots,\beta_{t-1}\in R_P\) in the basis \(1,Z,\ldots,Z^{r-1}\).

The remaining bits are ignored. Form the hash of the data: for \(1\leq i\leq r\),
\[
\begin{gathered}
h_i(x)=\sum_{s=1}^{d}u_{i+s-1}x_s\bmod2,\\
h(x)=\sum_{i=1}^{r}h_i(x)Z^{i-1}\in R_P .
\end{gathered}
\]
Let \(\lambda:R_P\to\mathbb F_2\) be the coefficient of \(Z^0\) in the representative of degree less than \(r\). The input belongs to \(L\) exactly when
\[
\lambda\Bigl(\sum_{j=0}^{t-1}\beta_jh(x)^j\Bigr)=0 .
\]

**Lemma 2.2.** Let \(d\geq64\). Then \(t\geq2\),
\[
\begin{gathered}
d^{1/6}-2<t\leq d^{1/6},\\
d^{2/3}\leq r<d^{2/3}+1,
\end{gathered}
\]
and the four blocks fit into the input: \(2d+(t+2)r-1\leq4d-1\leq n\).

*Proof.* Since \(2^6=64\leq d\), we have \(t\geq2\); \(t\) is the largest even integer not exceeding \(d^{1/6}\), which gives the first pair of inequalities, and the second is the definition of the ceiling. From \(d^{1/6}\geq2\) we get \(r<d^{2/3}+1\leq2d^{2/3}\) and \(t+2\leq2d^{1/6}\), so \((t+2)r\leq4d^{5/6}\leq2d\). Finally \(n\geq5d\). \(\square\)

So for \(d\geq64\) the parsing always succeeds, and the language is fixed once and for all at every length.

## 3. Deciding membership

**Proposition 3.1.** There is an algorithm that decides \(L\) using a number of bit operations bounded by a polynomial in \(n\).

*Proof.* The numbers \(d\), \(r\) and \(t\) are found with integer arithmetic on numbers of \(O(\log n)\) bits: \(r\) is the least positive integer with \(r^3\geq d^2\), and \(t\) is found by testing the even integers \(j\) with \(j^6\leq d\). Computing the \(r\) bits \(h_i(x)\) takes \(O(rd)\) bit operations.

An element of \(R_P\) is stored as its \(r\) coordinates. Addition takes \(r\) bit operations. To multiply, form the product of the two representatives, a polynomial of degree at most \(2r-2\), with \(O(r^2)\) operations, and reduce it: for \(e=2r-2,\ldots,r\) in turn, if the coefficient of \(Z^e\) is \(1\), add \(Z^{e-r}P\). Since \(P\) is monic this clears the coefficient of \(Z^e\) and changes only lower ones; it takes \(O(r^2)\) operations in all, and works for every monic \(P\). The sum \(\sum_j\beta_jh(x)^j\) is evaluated by Horner's rule,
\[
(\cdots(\beta_{t-1}h+\beta_{t-2})h+\cdots)h+\beta_0,
\]
with \(t-1\) multiplications and additions. The total is \(O(rd+tr^2)=O(d^{5/3})\) bit operations after the parameters are computed. \(\square\)

The algorithm consists of fixed loops over bit arrays of length at most \(n\), with counters of \(O(\log n)\) bits. Each such operation is carried out by a Turing machine with scans of its tapes, at a polynomial cost per operation. In this way one obtains the form stated in the theorem: a deterministic Turing machine and integers \(C,a\) with running time at most \(C(n+1)^a\). The translation into a machine table is routine and is not written out here; it is part of the Lean formalization of the theorem.

Two features matter for what follows. The algorithm accepts every monic \(P\) and does not test whether \(R_P\) is a field. And neither the algorithm nor its running time depends on the constants \(A,B,b\) of the later lessons.

## 4. The hash is injective on small subcubes

Fix \(d\geq64\) and consider the map \(h\) for uniformly random hash bits \(u\). It is linear in \(x\) over \(\mathbb F_2\): \(h(x)+h(x')=h(x+x')\).

**Lemma 4.1.** For every nonzero \(w\in\{0,1\}^d\), the vector \((h_1(w),\ldots,h_r(w))\) is uniformly distributed in \(\mathbb F_2^r\).

*Proof.* Let \(s^*\) be the largest index with \(w_{s^*}=1\). Then
\[
h_i(w)=u_{i+s^*-1}+\sum_{s<s^*,\ w_s=1}u_{i+s-1},
\]
and all indices in the sum are smaller than \(i+s^*-1\). Call \(u_{i+s^*-1}\) the *pivot* of row \(i\). Row \(i\) contains its own pivot and, besides, only bits of smaller index; in particular it contains no pivot of a later row. Fix all hash bits except the \(r\) pivots, and a target \(c\in\mathbb F_2^r\). The equations \(h_i(w)=c_i\) can be solved for the pivots in exactly one way, one row after another for \(i=1,\ldots,r\). So each target is attained by the same number of choices of \(u\). \(\square\)

Let \((T,\rho)\) be a restriction of the data coordinates, and \(m=|T|\). The *restricted cube* is the set of the \(2^m\) points of \(\{0,1\}^d\) that agree with \(\rho\) outside \(T\).

**Lemma 4.2.** The probability over \(u\) that \(h\) is not injective on the restricted cube is at most \(2^{m-r}\).

*Proof.* Two points of the cube have the same hash exactly when their difference \(w\), a nonzero vector supported in \(T\), has \(h(w)=0\). There are \(2^m-1\) such vectors, and each has \(h(w)=0\) with probability \(2^{-r}\) by Lemma 4.1. \(\square\)

The matrix of \(h\) has entries \(u_{i+s-1}\), constant along anti-diagonals. This saves hash bits: \(d+r-1\) instead of \(dr\). Lemma 4.1 is all that is needed from it.

## 5. Interpolation gives independent values

Now let \(P\) be as in Lemma 1.1, so that \(F=R_P\) is a field with \(2^r\) elements, and choose \(\beta_0,\ldots,\beta_{t-1}\) independently and uniformly in \(F\). For the fixed parameter bits, the *slice* is the function of the data bits, and its sign is
\[
\begin{gathered}
g(x)=(-1)^{\lambda(Q(h(x)))},\\
Q(X)=\sum_{j=0}^{t-1}\beta_jX^j,
\end{gathered}
\]
equal to \(+1\) on accepted inputs.

**Lemma 5.1.** Let \(a_1,\ldots,a_q\in F\) be distinct, with \(q\leq t\). For uniform \(\beta_0,\ldots,\beta_{t-1}\), the values \(Q(a_1),\ldots,Q(a_q)\) are independent and uniform in \(F\).

*Proof.* The map \(\Phi:F^t\to F^q\), \(\beta\mapsto(Q(a_1),\ldots,Q(a_q))\), is additive. It is surjective: for given \(v_1,\ldots,v_q\in F\), the polynomial
\[
\sum_{i=1}^{q}v_i\prod_{j\neq i}\frac{X-a_j}{a_i-a_j}
\]
has degree at most \(q-1<t\) and takes the value \(v_i\) at \(a_i\); the denominators are nonzero because \(F\) is a field and the \(a_i\) are distinct. The preimages of the points of \(F^q\) are the cosets of the kernel of \(\Phi\), so they all have the same size. Hence \(\Phi(\beta)\) is uniform on \(F^q\). \(\square\)

**Proposition 5.2.** Suppose \(h\) is injective on the restricted cube of \((T,\rho)\). Then for uniform \(\beta\), the signs \(g(x)\) at the points \(x\) of the restricted cube are unbiased and \(t\)-wise independent: for any \(q\leq t\) distinct points, the signs are independent and each is \(\pm1\) with probability \(\frac12\).

*Proof.* Distinct points have distinct hashes, so by Lemma 5.1 the values \(Q(h(x))\) at \(q\leq t\) distinct points are independent and uniform in \(F\). The map \(\lambda\) is \(\mathbb F_2\)-linear with \(\lambda(1)=1\), so adding \(1\) exchanges its two fibres, and they have equal size. Hence \(\lambda\) of a uniform element of \(F\) is a uniform bit. \(\square\)

This is where the field is needed: the interpolation polynomial divides by the differences \(a_i-a_j\). The number \(t\) of coefficients, about \(d^{1/6}\), is the amount of independence obtained; it grows with \(d\), and the next lesson needs exactly that.

## 6. Exercises

**6.1.** Let \(P\in\mathbb F_2[Z]\) be monic of degree \(r\). Show that \(R_P\) is a field if and only if \(P\) is irreducible.

**6.2.** For \(d=64\) compute \(r\), \(t\) and the number of input bits used, and check Lemma 2.2.

**6.3.** In Lemma 4.1, take \(d=3\), \(r=2\) and \(w=(1,1,0)\). Write \(h_1(w),h_2(w)\) in terms of \(u_1,\ldots,u_4\), name the pivots, and verify the uniformity directly.

**6.4.** Show that the values \(Q(a_1),\ldots,Q(a_{t+1})\) at \(t+1\) distinct points are *not* independent.

**6.5.** Let \(P=Z^2\) (so \(r=2\)), which is not irreducible. Find two distinct elements \(a_1,a_2\in R_P\) for which \(Q(a_1)\) and \(Q(a_2)\) are not independent, for \(t=2\).

## 7. Solutions

**6.1.** If \(P=AB\) with \(A,B\) of positive degree, the classes of \(A\) and \(B\) are nonzero with product zero, so \(R_P\) is not a field. Let \(P\) be irreducible and \(A\) a nonzero polynomial of degree less than \(r\). The set of polynomials \(SA+TP\) contains a nonzero element \(G\) of least degree, and division with remainder shows that \(G\) divides both \(A\) and \(P\). Since \(P\) is irreducible and \(\deg G\leq\deg A<r\), \(G\) is constant, so \(SA+TP=1\) for suitable \(S,T\), and \(S\) is an inverse of \(A\) in \(R_P\).

**6.2.** \(r=\lceil64^{2/3}\rceil=16\); \(t=2\), because \(2^6=64\leq64<4^6\). The blocks use \(2\cdot64+4\cdot16-1=191\) bits, and \(4d-1=255\), \(n\geq320\).

**6.3.** \(h_1(w)=u_1+u_2\) and \(h_2(w)=u_2+u_3\); here \(s^*=2\) and the pivots are \(u_2\) and \(u_3\). For fixed \(u_1\): \(u_2=c_1+u_1\), then \(u_3=c_2+u_2\). Each of the four targets \((c_1,c_2)\) is attained for exactly \(4\) of the \(16\) values of \((u_1,\ldots,u_4)\).

**6.4.** A polynomial of degree less than \(t\) is determined by its values at \(t\) distinct points (the difference of two such polynomials would have \(t\) roots). So \(Q(a_{t+1})\) is a function of \(Q(a_1),\ldots,Q(a_t)\), while it is uniform on \(F\); independence fails.

**6.5.** Take \(a_1=0\) and \(a_2=Z\). Then \(Q(a_1)=\beta_0\) and \(Q(a_2)=\beta_0+\beta_1Z\), and \(Z\cdot(Q(a_2)-Q(a_1))=\beta_1Z^2=0\) always. For independent uniform values, \(Z\cdot(Q(a_2)-Q(a_1))\) would be nonzero with positive probability.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 5 and Appendix A. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/112.md
- [Judson] T. W. Judson, *Abstract Algebra: Theory and Applications*, online edition; the text of the core courses Abstract Algebra I and II. https://judsonbooks.org/aata-files/aata-html/
- H. Krawczyk (1994, hashing with Toeplitz matrices), N. Alon, L. Babai and A. Itai (1986, limited independence from polynomials), and R. Paturi, M. E. Saks and F. Zane (2000, hard subfunctions selected by input bits) are named for credit; the lesson proves what it uses.

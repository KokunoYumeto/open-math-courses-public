# Streams, slots and slot evaluations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The operator \(T\) of the course lives on a layered graph, the *tower*, with two sets of vertices \(A_i\) and \(B_i\) in every layer \(i\in\mathbb Z\) and edges only between neighbouring layers. Its vertices are pairs of bit strings, and its edges are defined by linear equations over \(\mathbb F_2\), so that a long path can be reconstructed from the labels of its edges, while the incidence operators between neighbouring layers are uniform expanders. This lesson fixes the parameters, the vertex sets, the *slots* at which edges attach, and the linear *slot evaluations*; it proves the counting identities and the choice of coefficients on which the expansion of the next lessons rests [OpenAI-KK, Section 3 and Section 4.1 to Lemma 4.1].

- Parameters (Section 1).
- Streams and vertex sets (Section 2).
- Slots, degrees and families (Section 3).
- Slot evaluations (Section 4).
- Concentration for sampling with and without replacement (Section 5).
- The choice of coefficients and spills (Section 6).

## 1. Parameters

Let \(\ell\) be a positive integer, which is taken large at the end of the course, and put
\[
\begin{gathered}
d=2^{4\ell},\quad D=d^2,\quad s=10\ell,\quad r=7\ell,\\
n_0=1000,\\
H_i=(2n_0+1)s+1+|i|\quad(i\in\mathbb Z).
\end{gathered}
\]
So \(\log_2d=4\ell=2r-s\), and \(H_0=20010\ell+1\le h_*\log_2d\) with \(h_*=5003\). Put
\[
L_i=\frac{100H_i}{\log_2d},\qquad g_i=\frac{H_i}{100\log_2d} .
\]
Since \(|H_j-H_i|\le|j-i|\),
\[
\begin{gathered}
|j-i|\le\frac{CH_i}{\log_2d}\\
\Longrightarrow\ \Bigl|\frac{H_j}{H_i}-1\Bigr|\le\frac C{\log_2d},
\end{gathered}\tag{1.1}
\]
for every constant \(C\); the bound is uniform in \(i\). Throughout, *fixed* constants may depend on earlier fixed constants but not on \(\ell\) or on a layer index, and *for large \(\ell\)* means for all \(\ell\) beyond a threshold that depends only on fixed constants.

## 2. Streams and vertex sets

A *stream* of length \(l\) is a vector in \(\mathbb F_2^l\). We pad streams by zeros: a stream of length \(l\) is identified with the sequence in \(\mathbb F_2^{\mathbb N_0}\) whose coordinates from \(l\) on vanish, its *active* coordinates being \(0,\ldots,l-1\). The *prefix* of length \(a\) consists of coordinates \(0,\ldots,a-1\).

For \(h\ge0\) write \(h=2sq+t\) with \(q\ge0\), \(0\le t<2s\), and put
\[
\begin{aligned}
l_A(h)&=r+n_0s+qs+\max(t-s,0),\\
l_B(h)&=n_0s+qs+\min(t,s),
\end{aligned}
\]
and \(l_A(i)=l_A(|i|)\), \(l_B(i)=l_B(|i|)\) for \(i\in\mathbb Z\). Then \(l_A(h)+l_B(h)=r+2n_0s+h\), and increasing \(h\) by one increases exactly one of the two lengths by one: the \(B\)-length during \(s\) consecutive steps, then the \(A\)-length during the next \(s\) steps. Put
\[
\begin{aligned}
A_i&=\mathbb F_2^{l_A(i)}\times\mathbb F_2^{r+1+l_B(i)},\\
B_i&=\mathbb F_2^{l_B(i)}\times\mathbb F_2^{s-r+1+l_A(i)} .
\end{aligned}
\]
The two coordinates of a vertex are written \((u,v)\); \(u\) is its *input stream*.

**Lemma 2.1** (cardinalities). \(|A_i|=d\,2^{H_i}\) and \(|B_i|=2^{H_i}\). All four stream lengths at layer \(i\) are at most \(H_i\).

*Proof.* \(\log_2|B_i|=l_B(i)+s-r+1+l_A(i)\), which is \(s+2n_0s+1+|i|=H_i\), and \(\log_2|A_i|=l_A(i)+r+1+l_B(i)\), which is \(2r-s+H_i\), with \(2r-s=\log_2d\). For the last statement, \(l_A(i)\le r+n_0s+|i|<H_i\), and the other three lengths are bounded in the same way. \(\square\)

**Blocks.** An \(A\)-stream is divided into *block* \(0\) of length \(r\), followed by blocks \(1,2,\ldots\) of length \(s\); a \(B\)-stream into blocks \(1,2,\ldots\) of length \(s\). The blocks of the two sides are ordered as
\[
A0;\,B1;\,A1;\,B2;\,A2;\,\ldots ,\tag{2.1}
\]
the *interleaved order*.

**Lemma 2.2** (cutoffs). Let \(|i-k|\le1\). The active coordinates of the \(A\)-stream at \(A_i\) and of the \(B\)-stream at \(B_k\) form an initial segment of the interleaved order, possibly ending in a proper initial part of a block. The cutoff has exactly one of the two forms
\[
\begin{array}{ll}
\text{(B)}&l_A(i)=r+ns,\\
&l_B(k)=ns+t,\\
\text{(A)}&l_B(k)=(n+1)s,\\
&l_A(i)=r+ns+t,
\end{array}
\]
with \(1\le t\le s\), in which the last active block is \(B(n+1)\), respectively \(A(n+1)\), with \(t\) active coordinates; and \(n\ge n_0-1\).

*Proof.* For \(|k|=|i|=h=2sq+t'\): if \(1\le t'\le s\), then \(l_A=r+(n_0+q)s\) and \(l_B=(n_0+q)s+t'\), form (B) with \(n=n_0+q\); if \(s<t'<2s\), then \(l_B=(n_0+q+1)s\) and \(l_A=r+(n_0+q)s+(t'-s)\), form (A); if \(t'=0\), then \(l_A=r+(n_0+q)s\) and \(l_B=(n_0+q)s\), which is form (A) with \(n=n_0+q-1\) and \(t=s\). If \(|k|=|i|\pm1\), exactly one of the two lengths changes between \(|i|\) and \(|k|\). If it is the \(B\)-length, then \(l_A(i)=l_A(k)\) and \((l_A(i),l_B(k))=(l_A(k),l_B(k))\); if it is the \(A\)-length, then \(l_B(k)=l_B(i)\) and \((l_A(i),l_B(k))=(l_A(i),l_B(i))\). In both cases the pair of lengths is that of a single index, and the first case applies. \(\square\)

In both forms the four blocks immediately before the last active block are full blocks of length \(s\), because \(n\ge n_0-1\ge3\).

## 3. Slots, degrees and families

Fix a pair \((i,k)\) with \(|i-k|\le1\), called an *adjacent pair*, and put
\[
\begin{aligned}
\alpha&=1+l_B(i)-l_B(k),\\
\beta&=1+l_A(k)-l_A(i),\\
p&=r+\alpha,\qquad p'=s-r+\beta .
\end{aligned}
\]
Since adjacent absolute indices change each length by at most one, \(\alpha,\beta\in\{0,1,2\}\), and \(p>p'>0\) for large \(\ell\).

At every vertex of \(A_i\) there are \(d\) *slots* for the pair, indexed by \(a=(k-i,j)\), \(1\le j\le d\). At every vertex of \(B_k\) the slots for the pair are indexed by \(c=(i-k,j,b)\) with \(1\le j\le d\) and \(b\in\mathbb F_2^{p-p'}\), the *bucket*. Each slot will carry exactly one edge.

**Lemma 3.1** (degrees). The number of slots for the pair at a vertex of \(B_k\) is
\[
\begin{gathered}
D_{ik}=d\,2^{p-p'}=D\,2^{|i|-|k|},\\
\tfrac D2\le D_{ik}\le2D ,
\end{gathered}
\]
and \(d|A_i|=D_{ik}|B_k|\). Over the three pairs \((i,i-1),(i,i),(i,i+1)\), a vertex of \(A_i\) has \(3d\) slots, and a vertex of \(B_k\) has at most \(6D\) slots.

*Proof.* \(p-p'=2r-s+\alpha-\beta\), and \(\alpha-\beta=|i|-|k|\), the difference of \(l_A(i)+l_B(i)\) and \(l_A(k)+l_B(k)\), so \(p-p'=\log_2d+|i|-|k|\). Then \(D_{ik}|B_k|=D\,2^{|i|-|k|}2^{H_k}=D\,2^{H_i}=d|A_i|\) by Lemma 2.1. \(\square\)

**Families.** Put \(K=32s\). The *family* of an adjacent pair is
\[
\begin{gathered}
\bigl(k-i,\ \operatorname{sgn}i,\ \operatorname{sgn}k,\\
|i|\bmod K,\ |k|\bmod K\bigr),
\end{gathered}
\]
with \(\operatorname{sgn}0=0\). There are at most \(27K^2\) families. Since \(K\) is a multiple of \(2s\), the family determines \(\alpha,\beta,p,p'\), the form of the cutoff and the value of \(t\) in Lemma 2.2. A family that contains more than one pair has both indices of the same nonzero sign, and its pairs are \((i+mK\operatorname{sgn}i,\,k+mK\operatorname{sgn}i)\), \(m\ge0\); passing from one to the next adds \(K/2=16s\) to both stream lengths, so the last active blocks of different pairs of one family are at least \(32\) positions apart in the interleaved order. Families of pairs containing the index \(0\) consist of one pair.

## 4. Slot evaluations

On each side and for each slot there is a linear map \(\mathcal K\) from padded input streams to padded streams, and the *evaluation* of a vertex \((u,v)\) at the slot is
\[
Q=v+\mathcal Ku .\tag{4.1}
\]
The map \(\mathcal K\) acts blockwise: on an input block of length \(h\in\{r,s\}\) it is multiplication by a *diagonal coefficient* in the field \(\mathbb F_{2^h}\), after a fixed linear identification \(\mathbb F_{2^h}\cong\mathbb F_2^h\), with output in the same coordinates; in addition it may send a linear image of the block, its *spill*, into the first \(\alpha\) coordinates of the following block on side \(A\), or the first \(\beta\) coordinates of the following block on side \(B\). There are no other terms. The diagonal coefficient of a slot is the same for all its blocks of length \(s\); the spill matrix may depend on the family and the slot, and is the same at all blocks of length \(s\). The spill of \(A\)-block \(0\) is zero.

The fields exist: the roots of \(z^{2^h}-z\) in a splitting field over \(\mathbb F_2\) form a subfield, and they are \(2^h\) distinct roots, since the derivative of \(z^{2^h}-z\) is \(-1\).

**Recovering a block.** If two slots \(a\ne b\) at the same vertex have diagonal coefficients \(\lambda_a\ne\lambda_b\), their evaluations on block \(h\) are
\[
\begin{gathered}
Q^a_h=v_h+\lambda_au_h+S_au_{h-1},\\
Q^b_h=v_h+\lambda_bu_h+S_bu_{h-1},
\end{gathered}
\]
where \(S_a,S_b\) are the spills from the preceding block, extended by zero. If \(Q^a_h\), \(Q^b_h\) and \(u_{h-1}\) are known, then
\[
\begin{gathered}
(\lambda_a-\lambda_b)u_h=Q^a_h-Q^b_h\\
-(S_a-S_b)u_{h-1}
\end{gathered}\tag{4.2}
\]
determines \(u_h\), and then \(v_h\). This is how long paths will be reconstructed from their labels.

**Coefficient pools.** On side \(A\), slots are named by \((\delta,j)\), \(\delta\in\{-1,0,1\}\), \(1\le j\le d\): \(3d\) names. On side \(B\), a slot name is \((\delta,j,w,b)\) with the offset \(\delta\), the serial number \(j\), the bucket width \(w\in\{\log_2d-1,\log_2d,\log_2d+1\}\) and the bucket \(b\in\mathbb F_2^w\): at most \(3d(\frac d2+d+2d)=\frac{21}2D\) names. Choose injections of the \(A\)-names into \(\mathbb F_{2^s}\) and into \(\mathbb F_{2^r}\), and of the \(B\)-names into \(\mathbb F_{2^s}\); they exist for large \(\ell\) because \(3d=3\cdot2^{4\ell}<2^r\) and \(\frac{21}2D<2^s\). The diagonal coefficients of a slot are the images of its name, independently of the layer and the family. So two different slots at the same vertex always have different diagonal coefficients, in every block size.

## 5. Concentration for sampling with and without replacement

**Lemma 5.1** (exponential moments). Let \(y_1,\ldots,y_n\in\{0,1\}\), let \(S\) be the sum of \(m\le n\) entries drawn either independently and uniformly from the list, or uniformly without replacement, and \(h\in\mathbb R\). Then
\[
\begin{gathered}
\mathbb E\,e^{h(S-\mathbb ES)}\le e^{mh^2/8},\\
\mathbb P\{S-\mathbb ES\ge\epsilon m\}\le e^{-2\epsilon^2m},
\end{gathered}
\]
and the same tail bound holds for \(\mathbb ES-S\).

*Proof.* For one draw \(X\) with \(\mathbb EX=\mu\), the function \(\psi(h)=\log\mathbb Ee^{h(X-\mu)}\) has \(\psi(0)=\psi'(0)=0\), and \(\psi''(h)\) is the variance of \(X\) under the probability proportional to \(e^{hX}\), at most \(\frac14\) for a \(\{0,1\}\)-valued variable. So \(\psi(h)\le h^2/8\), and for independent draws the exponential moments multiply.

Without replacement, put \(x_k=e^{hy_k}>0\). The expectation of the product of the \(m\) sampled \(x_k\) is \(e_m(x)/\binom nm\), with \(e_m\) the elementary symmetric polynomial. Replacing two entries \(x_1\ne x_2\) by their average does not decrease \(e_m\): with \(x'=(x_3,\ldots,x_n)\),
\[
\begin{aligned}
e_m(x)&=x_1x_2e_{m-2}(x')\\
&\quad+(x_1+x_2)e_{m-1}(x')+e_m(x'),
\end{aligned}
\]
in which only \(x_1x_2\) changes, and it increases. Replace repeatedly the largest and the smallest entry by their average; each step lowers \(\sum_k(x_k-\bar x)^2\) by \(\frac12(\max-\min)^2\), which is at least \(\frac1{2n}\) times that sum, so all entries converge to the mean \(\bar x\). By continuity, \(e_m(x)/\binom nm\le\bar x^m\), the corresponding product moment for independent draws. Both ways of sampling have the same mean, so the bound for independent draws applies. The tail bound follows from Markov's inequality applied to \(e^{h(S-\mathbb ES)}\) with \(h=4\epsilon\), and the lower tail from \(-y_k\) in place of \(y_k\). \(\square\)

## 6. The choice of coefficients and spills

Fix a family and one of its pairs \((i,k)\), and a side. Let \(\mathcal I\) be the set of slots of that side for the pair, \(n_{\mathrm{sl}}=|\mathcal I|\), so \(n_{\mathrm{sl}}=d\) on side \(A\) and \(n_{\mathrm{sl}}=D_{ik}\) on side \(B\). For a slot \(a\in\mathcal I\) let
\[
M_a:\mathbb F_2^s\to\mathbb F_2^{s+\alpha}\quad\text{or}\quad M_a:\mathbb F_2^s\to\mathbb F_2^{s+\beta}
\]
be multiplication by its diagonal coefficient followed by its spill, the map from one input block of length \(s\) to the corresponding output block and the spilled coordinates.

**Lemma 6.1** (coefficients and spills; [OpenAI-KK, Lemma 4.1]). For large \(\ell\), the injections and spills can be chosen so that for every family, each side and every nonzero linear functional \(\zeta\) on the output space of the \(M_a\):

1. for every nonempty initial segment of the \(s\) input coordinates, every value of the restricted functional \(\zeta M_a\) occurs for at most \(0.55\,n_{\mathrm{sl}}\) slots \(a\);
2. every value of the full functional \(\zeta M_a\) occurs for at most \(10^{-3}n_{\mathrm{sl}}\) slots.

*Proof.* Choose each injection uniformly at random, and for every family and slot an independent uniform binary matrix with two rows and \(s\) columns, of which the spill uses the first \(\alpha\) or \(\beta\) rows. Fix a test: a family, a side, \(\zeta\), and either a value of the first-coordinate restriction or a value of the full functional.

If the spill component of \(\zeta\) is nonzero, then, conditionally on all diagonal coefficients, the functionals \(\zeta M_a\), \(a\in\mathcal I\), are independent and uniform among the \(2^s\) functionals on \(\mathbb F_2^s\), because a nonzero combination of independent uniform rows is uniform. In particular their values on the first input coordinate are independent fair bits. If the spill component of \(\zeta\) vanishes, its diagonal component \(\zeta_0\) is nonzero, and \(\lambda\mapsto(u\mapsto\zeta_0(\lambda u))\) is a bijection from the field onto the \(2^s\) functionals: distinct \(\lambda,\lambda'\) give distinct functionals because \((\lambda-\lambda')u\) runs through all of \(\mathbb F_2^s\). The coefficients of distinct slots are distinct uniform field elements, so the functionals \(\zeta M_a\) are drawn uniformly without replacement, and their first-coordinate values without replacement from a population that is half zeros and half ones.

By Lemma 5.1 with \(m=n_{\mathrm{sl}}\ge d\), a first-coordinate value occurs more than \(0.55m\) times with probability at most \(e^{-2(0.05)^2m}\). A full value has expected frequency \(2^{-s}m<\frac12\cdot10^{-3}m\) for large \(\ell\), so it occurs more than \(10^{-3}m\) times with probability at most \(e^{-2(5\cdot10^{-4})^2m}\); without replacement it occurs at most once. The number of tests is at most \(27K^2\cdot2\cdot2^{s+2}(2+2^s)=2^{O(\ell)}\), each failing with probability at most \(e^{-cd}\) for an absolute \(c>0\), and \(d=2^{4\ell}\). So for large \(\ell\) some choice passes all tests. A value of the functional restricted to a longer initial segment determines its value on the first coordinate, so the bound for the first coordinate implies statement 1 for every nonempty initial segment. \(\square\)

The coefficients and spills are fixed from now on.

## 7. Exercises

**7.1** (easy). Compute \(l_A(h)\) and \(l_B(h)\) for \(h=0,1,s,s+1,2s\), and check \(l_A(h)+l_B(h)=r+2n_0s+h\).

**7.2** (easy). Check that \(|A_i|=d\,|B_i|\) and that the number of edges of the pair \((i,k)\), counted at \(A_i\), is \(D\,2^{H_i}\).

**7.3** (medium). Let \(\lambda_a=1\), \(\lambda_b=x\) in \(\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)\), and suppose there are no spills. Given \(Q^a=v+u\) and \(Q^b=v+xu\) for \(u,v\in\mathbb F_4\), recover \(u\) and \(v\).

**7.4** (medium). Show that for independent fair bits \(X_1,\ldots,X_m\), \(\mathbb P\{X_1+\cdots+X_m\ge0.55m\}\le e^{-m/200}\), and compare with the exact probability for \(m=100\).

## 8. Solutions

**7.1.** \(h=0\): \(q=t=0\), \(l_A=r+n_0s\), \(l_B=n_0s\). \(h=1\): \(l_B\) grows to \(n_0s+1\). \(h=s\): \(l_B=n_0s+s\), \(l_A=r+n_0s\). \(h=s+1\): \(l_A=r+n_0s+1\). \(h=2s\): \(q=1\), \(t=0\), \(l_A=r+n_0s+s\), \(l_B=n_0s+s\). In each case the sum is \(r+2n_0s+h\).

**7.2.** By Lemma 2.1, \(|A_i|/|B_i|=d\). Each vertex of \(A_i\) has \(d\) slots for the pair and each slot one edge: \(d\cdot d\,2^{H_i}=D\,2^{H_i}\) edges.

**7.3.** \(Q^a-Q^b=(1-x)u=(1+x)u\), and \(1+x=x^2\) is invertible with inverse \(x\), since \(x^3=1\). So \(u=x(Q^a+Q^b)\) and \(v=Q^a+u\).

**7.4.** Lemma 5.1 with \(\epsilon=0.05\) gives \(e^{-2\cdot0.0025\,m}=e^{-m/200}\). For \(m=100\), the bound is \(e^{-1/2}\approx0.61\), while the exact probability of at least \(55\) heads in \(100\) tosses is about \(0.18\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 3, Section 4.1, Section 4.2 and Lemma 4.1. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026

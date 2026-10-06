# Closed graphs and bounded operator cutoffs

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. This independent exposition is CC0.*

A closed operator need not be bounded. The decisive extra hypothesis is that its domain is the whole Banach space. We prove this assertion from the Baire theorem in AB03, then explain exactly when it applies to a cutoff of an unbounded operator. The proof works over either the real or the complex field, without separability or a countability assumption on dimension.

The final application uses the bicommutant theorem BK02 and unitary spanning BK08. It supplies the Banach-space input used in MT07; no trace, spectral calculus or assertion from MT07 enters the proof here.

## Recovering exact preimages from approximate ones

**Theorem.** Let \(X,Y\) be Banach spaces over the same field, and let \(S:X\to Y\) be a bounded surjective linear map. There is a constant \(C>0\) such that every \(y\in Y\) has a preimage \(x\in X\) satisfying

\[
 \begin{gathered}
 Sx=y,\\
 \|x\|\leq C\|y\|.
 \end{gathered}
 \tag{CG.1}
\]

Consequently \(S\) maps open sets to open sets. If it is also injective, its inverse is bounded and linear.

**Proof.** If \(Y=\{0\}\), choose \(x=0\) and \(C=1\); all conclusions are immediate. Suppose now that \(Y\ne\{0\}\). Write \(D=\{x\in X:\|x\|\leq1\}\). Surjectivity gives

\[
 Y=\bigcup_{n=1}^{\infty}\overline{S(nD)}.
 \tag{CG.2}
\]

The closures are taken in the norm of \(Y\). By AB03, some \(\overline{S(nD)}\) contains an open ball \(B(y_0,r)\), with \(r>0\). If \(\|z\|<r\), both \(y_0+z\) and \(y_0\) belong to that closure. Choose sequences \(a_j,b_j\in nD\) such that \(Sa_j\to y_0+z\) and \(Sb_j\to y_0\). Then \(a_j-b_j\in2nD\) and \(S(a_j-b_j)\to z\). Scaling by \(2n\) proves

\[
 \begin{gathered}
 B(0,\delta)\subset\overline{S(D)},\\
 \delta=\frac{r}{2n}>0.
 \end{gathered}
 \tag{CG.3}
\]

This is initially only an approximation statement. We next turn it into an exact solution.

For a nonzero residual \(v\in Y\), the vector \(\delta v/(2\|v\|)\) lies strictly inside the ball in (CG.3). Approximate it by \(Sa\), with \(a\in D\), to within \(\delta/4\). After rescaling, there is \(x_v\in X\) with

\[
 \begin{gathered}
 \|x_v\|\leq\frac{2}{\delta}\|v\|,\\
 \|v-Sx_v\|\leq\frac12\|v\|.
 \end{gathered}
 \tag{CG.4}
\]

For zero residual take \(x_v=0\). Starting with \(v_0=y\), define \(x_k=x_{v_{k-1}}\) and \(v_k=v_{k-1}-Sx_k\). Induction gives

\[
 \begin{gathered}
 \|v_k\|\leq2^{-k}\|y\|,\\
 \sum_{k=1}^{\infty}\|x_k\|
 \leq\frac{4}{\delta}\|y\|.
 \end{gathered}
 \tag{CG.5}
\]

The norm of every tail of the partial sums is bounded by the corresponding tail of this convergent numerical series. The partial sums are therefore Cauchy. Completeness of \(X\) gives \(x=\sum_{k\geq1}x_k\), with the stated norm bound. Boundedness of \(S\) gives convergence of their images to \(Sx\), whereas the residual identity gives convergence to \(y\). Thus \(Sx=y\), proving (CG.1) with \(C=4/\delta\).

If \(U\subset X\) is open and \(Sx_0\in S(U)\) with \(x_0\in U\), choose \(\varepsilon>0\) such that \(B(x_0,\varepsilon)\subset U\). Whenever \(\|z-Sx_0\|<\varepsilon/C\), (CG.1) gives a preimage \(h\) of \(z-Sx_0\) with \(\|h\|<\varepsilon\). Hence \(z=S(x_0+h)\in S(U)\). This proves openness. If \(S\) is injective, linearity of the inverse follows from uniqueness of preimages, and (CG.1) is its bound. \(\square\)

## The closed graph theorem

**Theorem.** Let \(X,Y\) be Banach spaces over the same real or complex field. Let \(T:X\to Y\) be an everywhere-defined linear map. If

\[
 \begin{gathered}
 G(T)=\\
 \{(x,Tx):x\in X\}
 \end{gathered}
 \tag{CG.6}
\]

is closed in the product norm topology, then \(T\) is bounded. Conversely every bounded linear map has a closed graph.

**Proof.** Equip \(X\times Y\) with the norm \(\|(x,y)\|=\|x\|+\|y\|\). A Cauchy sequence has Cauchy coordinate sequences; their limits in \(X\) and \(Y\) give its limit in this norm. Thus the product is Banach. This norm defines the product topology, since each coordinate distance is bounded by the sum and the sum is bounded by twice the larger coordinate distance. A Cauchy sequence in the closed linear subspace \(G(T)\) converges in the product, and closedness puts its limit back in \(G(T)\). Hence \(G(T)\), with the inherited norm, is also Banach.

The coordinate map

\[
 \begin{gathered}
 P:G(T)\longrightarrow X,\\
 P(x,Tx)=x
 \end{gathered}
 \tag{CG.7}
\]

is linear and bounded by one. It is injective because \(T\) is a function, and surjective because its domain is all of \(X\). By CG01 its inverse is bounded. For some \(C>0\), therefore,

\[
 \begin{aligned}
 \|Tx\|&\leq\|(x,Tx)\|\\
 &=\|P^{-1}x\|\\
 &\leq C\|x\|.
 \end{aligned}
 \tag{CG.8}
\]

This is the desired bound. Conversely, if \(T\) is bounded, the continuous map \((x,y)\mapsto y-Tx\) has \(G(T)\) as the inverse image of the closed set \(\{0\}\). Its graph is closed. \(\square\)

## The domain test for a cutoff

**Proposition.** Let \(T:D(T)\subset H\to K\) be a closed linear operator between Hilbert spaces. Let \(e:H\to H\) be a bounded projection such that \(eH\subset D(T)\). Then the composite \(Te:H\to K\) is everywhere defined and bounded. No density assumption on \(D(T)\) is needed for this conclusion.

**Proof.** The range inclusion makes the composite defined on every vector in \(H\). The map \((\xi,\eta)\mapsto(e\xi,\eta)\) is continuous on \(H\times K\), and its inverse image of \(G(T)\) is exactly \(G(Te)\). This graph is closed. Hilbert spaces are Banach, so CG02 applies. In fact the same proof works for any bounded \(e\) with the stated range inclusion; idempotence is not needed. \(\square\)

When \(H=K\), let \(M\subset B(H)\) be a von Neumann algebra, assume that \(T\) is affiliated with \(M\), and suppose \(e\in M\). Here affiliation means that for every unitary \(u\in M'\), one has \(uD(T)=D(T)\) and \(Tu\xi=uT\xi\) for \(\xi\in D(T)\). Since \(e\) commutes with \(u\), for every \(\xi\in H\) we obtain

\[
 \begin{aligned}
 (Te)u\xi&=T(ue\xi)\\
 &=u(Te)\xi.
 \end{aligned}
 \tag{CG.9}
\]

Every argument of \(T\) in this identity belongs to its domain. The already established boundedness of \(Te\), together with unitary spanning in BK08 applied to \(M'\), shows that \(Te\) commutes with all of \(M'\). By BK02, \(Te\in M''=M\). Thus the cutoff is a bounded member of the same algebra, precisely as required in MT07.

**Why dense domain is insufficient.** On \(\ell^2(\mathbb N)\), let \(D(T)\) consist of the vectors \(x\) for which \(\sum_{n\geq1}n^2|x_n|^2<\infty\), and set

\[
 (Tx)_n=nx_n.
 \tag{CG.10}
\]

Finite sequences belong to this domain and are dense, since truncation tails have norm tending to zero. If \(x^{(j)}\to x\) and \(Tx^{(j)}\to y\) in \(\ell^2\), coordinate convergence gives \(y_n=nx_n\); because \(y\in\ell^2\), this puts \(x\) in the domain and gives \(Tx=y\). Thus \(T\) is closed. For the unit vector \(f_n\) in the \(n\)-th coordinate, however, \(\|Tf_n\|=n\), so \(T\) is unbounded. Taking \(e=I\) does not satisfy the proposition: \(eH\) is not contained in \(D(T)\). A graph which is closed and densely defined cannot replace that all-range domain inclusion.

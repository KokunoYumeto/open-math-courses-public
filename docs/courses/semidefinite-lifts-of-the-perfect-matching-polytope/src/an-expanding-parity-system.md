# An expanding parity system

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Put a bit on each end of each edge of a graph, and prescribe at each vertex the parity of its bits. If the prescribed parities have an odd sum, some edge must carry different bits at its two ends: the number of such edges is odd. This lesson constructs, on an expanding graph, a linear functional that assigns the value zero to the number of disagreeing edges, and is nevertheless nonnegative on all squares of functions of low degree [OpenAI-PSD, Section 5]. So the positive function "number of disagreements minus \(\varepsilon\)" is far from every sum of such squares. The construction is a block version of Grigoriev's low-degree functionals for parity and Tseitin contradictions [Grigoriev 2001].

- Expanding multigraphs (Section 1).
- The parity system (Section 2).
- A functional separating low-degree squares (Section 3).

All logarithms are natural. Fix the constants
\[
\begin{gathered}d=100,\qquad\beta=\frac1{100},\\ \tau=\frac\beta{10}=\frac1{1000}.\end{gathered}\tag{0.1}
\]

## 1. Expanding multigraphs

The edges of a multigraph are distinguished, even when they have the same endpoints; cuts and degrees count edges with multiplicity. For a multigraph \(H\) and a set \(W\) of its vertices, \(\delta_H(W)\) is the set of edges with exactly one endpoint in \(W\). For \(0<\alpha<1\) let \(\mathrm h(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)\).

**Lemma 1.1.** For an integer \(N\ge1\) and \(0<\alpha\le\frac12\),
\[
\sum_{0\le j\le\alpha N}\binom Nj\le e^{N\mathrm h(\alpha)} .
\]
For integers \(1\le w\le n\), \(\binom nw\le(en/w)^w\).

*Proof.* The terms \(\alpha^j(1-\alpha)^{N-j}=(1-\alpha)^N(\alpha/(1-\alpha))^j\) do not increase in \(j\), so for \(j\le\alpha N\) they are at least \(\alpha^{\alpha N}(1-\alpha)^{(1-\alpha)N}=e^{-N\mathrm h(\alpha)}\). Hence
\[
\begin{aligned}1&=\sum_j\binom Nj\alpha^j(1-\alpha)^{N-j}\\&\ge e^{-N\mathrm h(\alpha)}\sum_{j\le\alpha N}\binom Nj .\end{aligned}
\]
For the second bound, \(\binom nw\le n^w/w!\) and \(w!\ge(w/e)^w\), since \(e^w\ge w^w/w!\). \(\square\)

**Lemma 1.2** (expanding multigraphs; [OpenAI-PSD, Lemma 5.1]). For every even \(t\ge2\) there is a bipartite \(d\)-regular multigraph \(H\) on \([t]\) with
\[
\begin{gathered}|\delta_H(W)|\\ \ge\beta d\min\{|W|,t-|W|\}\\ (W\subseteq[t]).\end{gathered}\tag{1.1}
\]
In particular \(H\) is connected.

*Proof.* Write \(t=2l\), split \([t]\) into two sides of \(l\) vertices, and let \(H\) be the union of \(d\) independent uniform perfect matchings between the sides; equivalently, of \(d\) independent uniform permutations \(\sigma_1,\ldots,\sigma_d\) of \([l]\), the \(c\)-th one joining the \(x\)-th vertex of the first side to the \(\sigma_c(x)\)-th vertex of the second side. Then \(H\) is bipartite and \(d\)-regular. Since \(\delta_H(W)=\delta_H([t]\setminus W)\), it suffices to check (1.1) for the nonempty \(W\) with \(w=|W|\le l\).

Let \(W\) have \(a\) vertices on the first side and \(b\) on the second, \(a+b=w\). The \(da\) edges at the first-side vertices of \(W\) end on the second side, and at most \(db\) of them end in \(W\); so \(|\delta_H(W)|\ge d(a-b)\), and likewise \(\ge d(b-a)\). Thus (1.1) can fail only if \(|a-b|<\beta w\le w/10\), and then \(0.45w\le a,b\le0.55w\).

Suppose that \(|\delta_H(W)|<\beta dw\). Call an *image* a pair \((x,c)\) with \(x\) a first-side vertex of \(W\) and \(c\le d\), and call it exceptional if \(\sigma_c(x)\) is not a second-side vertex of \(W\). Exceptional images give distinct edges of \(\delta_H(W)\), so there are fewer than \(\beta dw\le(0.01/0.45)\,da<0.05\,da\) of them. By Lemma 1.1 and \(\mathrm h(0.05)<0.2\), there are at most \(e^{0.21da}\) possible sets of exceptional images. For a fixed set, all other images, at least \(0.95da\) of them, must lie among the \(b\) second-side vertices of \(W\). For a single uniform permutation, the probability that \(m\) given points are mapped into a given set of \(b\) points is \(\prod_{i<m}\frac{b-i}{l-i}\le(b/l)^m\); by independence of the permutations,
\[
\begin{aligned}&\Pr\bigl[|\delta_H(W)|<\beta dw\bigr]\\&\quad\le e^{0.21da}\Bigl(\frac{0.55w}l\Bigr)^{0.95da}\\&\quad=e^{da\,[0.21+0.95\log(0.55w/l)]} .\end{aligned}
\]
The bracket is negative, since \(0.21+0.95\log0.55<-0.35\) and \(w\le l\). With \(da\ge45w\) and Lemma 1.1, the probability that some \(W\) with \(|W|=w\) fails is at most
\[
\begin{aligned}&\Bigl(\frac{2el}w\Bigr)^we^{45w\,[0.21+0.95\log(0.55w/l)]}\\&\quad=e^{w\,[\log(2e)+45(0.21+0.95\log0.55)]}\\&\qquad\cdot e^{41.75\,w\log(w/l)}\le e^{-8w},\end{aligned}
\]
because \(\log(w/l)\le0\) and the number \(\log(2e)+45(0.21+0.95\log0.55)\) is less than \(-14\). As \(\sum_{w\ge1}e^{-8w}<1\), some choice of the permutations satisfies (1.1) for all \(W\). A connected component \(W\ne\varnothing,[t]\) would have \(\delta_H(W)=\varnothing\), contradicting (1.1). \(\square\)

## 2. The parity system

Fix an even \(t\ge2\) and a multigraph \(H\) as in Lemma 1.2, and order the \(d\) incidences at each vertex: each edge \(e=uv\) occupies one position \(j_u(e)\in[d]\) at \(u\) and one position \(j_v(e)\) at \(v\). Choose bits \(b_1,\ldots,b_t\in\{0,1\}\) with odd sum, for instance \(b_1=1\) and \(b_i=0\) for \(i>1\). At vertex \(i\) let
\[
\begin{gathered}Y_i=\Bigl\{y_i\in\{0,1\}^d\mid\\ \textstyle\sum_jy_{i,j}\equiv b_i\pmod2\Bigr\},\\ Y=\prod_{i=1}^tY_i .\end{gathered}\tag{2.1}
\]
The first \(d-1\) bits of \(y_i\) are free and determine the last one, so \(|Y_i|=L=2^{d-1}\); \(Y\) carries the uniform probability measure.

We use the characters of Section 1 of [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md) in the free coordinates: \(\Lambda=\{0,1\}^{d-1}\) with addition modulo two, and for \(p=(p_1,\ldots,p_t)\in\Lambda^t\)
\[
\begin{gathered}\chi_p(y)=(-1)^{\sum_{i=1}^t\sum_{j=1}^{d-1}p_{i,j}y_{i,j}},\\ |p|_{\mathrm{blk}}=|\{i:p_i\ne0\}|.\end{gathered}
\]
By Lemma 1.1 there, the \(\chi_p\) form an orthonormal basis of the real functions on \(Y\). A function has *block degree at most \(D\)* if its Fourier coefficients vanish whenever \(|p|_{\mathrm{blk}}>D\).

For an edge \(e=uv\) write \(y_{u,e}=y_{u,j_u(e)}\) and \(y_{v,e}=y_{v,j_v(e)}\) for its two bits. For \(\varepsilon>0\) put, summing over the edges \(e=uv\) of \(H\),
\[
\begin{aligned}f_\varepsilon(y)&=\sum_{e=uv}\mathbf 1_{\{y_{u,e}\ne y_{v,e}\}}\\&\quad-\varepsilon .\end{aligned}\tag{2.2}
\]

**Lemma 2.1.** For every \(y\in Y\), the number of edges with \(y_{u,e}\ne y_{v,e}\) is odd. In particular \(f_\varepsilon\ge1-\varepsilon\), which is positive for \(0<\varepsilon<1\).

*Proof.* Modulo two, \(\mathbf 1_{\{y_{u,e}\ne y_{v,e}\}}\equiv y_{u,e}+y_{v,e}\). Every incidence belongs to exactly one edge, so the sum over the edges is the sum of all bits \(y_{i,j}\), which is \(\sum_ib_i\equiv1\) modulo two. \(\square\)

## 3. A functional separating low-degree squares

**Proposition 3.1** ([OpenAI-PSD, Proposition 5.2]). Let \(t\ge1000\) be even, let \(H\), \(Y\) and \(f_\varepsilon\) be as above, and put \(D=\lfloor\tau t\rfloor\). There is a linear functional \(\mathcal D\) on the real functions on \(Y\) such that \(\mathcal D(1)=1\); \(\mathcal D(g^2)\ge0\) for every \(g\) of block degree at most \(D\); \(\mathcal D(f_\varepsilon)=-\varepsilon\) for every \(\varepsilon>0\); and \(|\mathcal D(h)|\le L^t\|h\|_\infty\) for every real function \(h\) on \(Y\).

The proof occupies the rest of this section.

*The incidence map.* Send a set of incidences \((i,j)\in[t]\times[d]\) to the set of edges that contain an odd number of them. This map \(\iota\) from subsets of \([t]\times[d]\) to subsets of \(E(H)\) is linear over \(\mathbb F_2\), with symmetric difference as addition. A character index \(p\in\Lambda^t\) *selects* the incidences \((i,j)\) with \(j<d\) and \(p_{i,j}=1\); let \(E(p)\) be the image of the selected set. Then
\[
E(p+p')=E(p)\mathbin\triangle E(p').
\]
The cut sets \(\delta_H(S)\), \(S\subseteq[t]\), form a subspace \(\mathcal C\), since \(\delta_H(S)\mathbin\triangle\delta_H(S')=\delta_H(S\mathbin\triangle S')\). Because \(H\) is connected, \(\delta_H(S)=\varnothing\) only for \(S=\varnothing,[t]\), so \(\delta_H(S)=\delta_H(S')\) implies \(S'=S\) or \(S'=[t]\setminus S\).

**Lemma 3.2** (small sides). If \(|p|_{\mathrm{blk}}\le2D\) and \(E(p)\in\mathcal C\), there is exactly one \(S(p)\subseteq[t]\) with \(\delta_H(S(p))=E(p)\) and \(|S(p)|\le t/5\).

*Proof.* Each block selects at most \(d-1\) incidences, so \(|E(p)|\le2Dd\). If \(E(p)=\delta_H(S)\), then (1.1) gives \(\beta d\min\{|S|,t-|S|\}\le2Dd\), so \(\min\{|S|,t-|S|\}\le2D/\beta\), and \(2D/\beta\le2\tau t/\beta=t/5\). Thus \(S\) or its complement has at most \(t/5\) elements. The only other set with the same cut is the complement, and the two cannot both have at most \(t/5<t/2\) elements. \(\square\)

*Definition of the functional.* Put
\[
\mathcal D(\chi_p)=\begin{cases}(-1)^{\sum_{i\in S(p)}b_i}&\text{if }|p|_{\mathrm{blk}}\le2D\\&\text{and }E(p)\in\mathcal C,\\ 0&\text{otherwise},\end{cases}
\]
and extend \(\mathcal D\) linearly. The trivial character \(\chi_0=1\) has \(E(0)=\varnothing=\delta_H(\varnothing)\) and \(S(0)=\varnothing\), so \(\mathcal D(1)=1\).

*Positivity on low-degree squares.* Let \(\mathcal I_D=\{p:|p|_{\mathrm{blk}}\le D\}\) and \(M_{p,p'}=\mathcal D(\chi_p\chi_{p'})=\mathcal D(\chi_{p+p'})\) for \(p,p'\in\mathcal I_D\). Call \(p\) and \(p'\) equivalent if \(E(p+p')=E(p)\mathbin\triangle E(p')\in\mathcal C\); the classes are the preimages of the cosets of \(\mathcal C\). Entries between different classes vanish. Within a class, \(|p+p'|_{\mathrm{blk}}\le2D\) and \(E(p+p')\in\mathcal C\), so every entry is a sign, and the diagonal entries equal \(\mathcal D(1)=1\).

Let \(p_1,p_2,p_3\) lie in one class and put \(S_{ab}=S(p_a+p_b)\). By linearity,
\[
\begin{aligned}&\delta_H\bigl(S_{12}\mathbin\triangle S_{23}\mathbin\triangle S_{31}\bigr)\\&\quad=E\bigl(2(p_1+p_2+p_3)\bigr)=\varnothing .\end{aligned}
\]
The set \(S_{12}\mathbin\triangle S_{23}\mathbin\triangle S_{31}\) has at most \(3t/5<t\) elements by Lemma 3.2, so it is empty, and the sum of the \(b_i\) over \(S_{12}\), \(S_{23}\) and \(S_{31}\) is even. Hence
\[
M_{p_1,p_2}M_{p_2,p_3}M_{p_3,p_1}=1 .
\]
Fix \(p_0\) in the class and put \(\sigma_p=M_{p,p_0}\). Taking \((p_1,p_2,p_3)=(p,p',p_0)\) and using that \(M\) is symmetric with entries \(\pm1\) gives \(M_{p,p'}=\sigma_p\sigma_{p'}\). So each block of \(M\) is the positive semidefinite matrix \(\sigma\sigma^{\mathsf T}\). If \(g=\sum_{p\in\mathcal I_D}\widehat g(p)\chi_p\), then
\[
\mathcal D(g^2)=\sum_{p,p'\in\mathcal I_D}\widehat g(p)\widehat g(p')M_{p,p'}\ge0 .
\]

*Values on disagreements.* Let \(e=uv\) be an edge, and let \(T\subseteq\{u,v\}\) be the set of its endpoints at which \(e\) occupies the last position \(d\). On \(Y_i\) the parity condition gives
\[
(-1)^{y_{i,d}}=(-1)^{b_i}\prod_{j=1}^{d-1}(-1)^{y_{i,j}} .
\]
Using this at the vertices in \(T\),
\[
(-1)^{y_{u,e}+y_{v,e}}=(-1)^{\sum_{i\in T}b_i}\,\chi_p(y)
\]
for an index \(p\) with \(|p|_{\mathrm{blk}}\le2\). Its selected set arises from the two incidences of \(e\) by replacing each last incidence \((i,d)\), \(i\in T\), with \((i,1),\ldots,(i,d-1)\); that is, by adding the full set of incidences at \(i\), whose image under \(\iota\) is \(\delta_H(\{i\})\). The two incidences of \(e\) have image \(\varnothing\), so
\[
E(p)=\mathop{\triangle}_{i\in T}\delta_H(\{i\})=\delta_H(T),
\]
also when \(u\) and \(v\) are joined by parallel edges. As \(t\ge1000\), we have \(D\ge1\), so \(|p|_{\mathrm{blk}}\le2\le2D\), and \(|T|\le2\le t/5\), so \(T=S(p)\) by Lemma 3.2. The two signs cancel:
\[
\begin{aligned}\mathcal D\bigl((-1)^{y_{u,e}+y_{v,e}}\bigr)&=(-1)^{\sum_{i\in T}b_i}\,\mathcal D(\chi_p)\\&=1 .\end{aligned}
\]
Since \(\mathbf 1_{\{y_{u,e}\ne y_{v,e}\}}=\bigl(1-(-1)^{y_{u,e}+y_{v,e}}\bigr)/2\), every disagreement indicator has value \(0\) under \(\mathcal D\), and \(\mathcal D(f_\varepsilon)=-\varepsilon\,\mathcal D(1)=-\varepsilon\).

*The norm bound.* All values of \(\mathcal D\) on characters have absolute value at most one, and \(|\widehat h(p)|=|\mathbb E_y\chi_p(y)h(y)|\le\|h\|_\infty\). So
\[
|\mathcal D(h)|\le\sum_{p\in\Lambda^t}|\widehat h(p)|\le L^t\|h\|_\infty .
\]
This proves Proposition 3.1. \(\square\)

By Lemma 2.1 the function \(f_\varepsilon\), for \(0<\varepsilon<1\), is the square of the positive function \(f_\varepsilon^{1/2}\). Proposition 3.1 shows that \(f_\varepsilon\) is nevertheless not a sum of squares of functions of block degree at most \(D\): such a sum would have a nonnegative value under \(\mathcal D\). The proof of the main theorem shows that a small PSD factorization would make \(f_\varepsilon\) uniformly close to such a sum, which the norm bound rules out.

## 4. Exercises

**4.1.** Check the numerical facts used in the proof of Lemma 1.2: \(\mathrm h(0.05)<0.2\), \(0.21+0.95\log0.55<-0.35\), and that \(\log(2e)+45(0.21+0.95\log0.55)\) is less than \(-14\).

**4.2.** Let \(H\) be a connected multigraph. Show that \(\delta_H(S)=\delta_H(S')\) implies \(S'\in\{S,[t]\setminus S\}\).

**4.3.** Show that \(\iota\) maps the set of all \(d\) incidences at a vertex \(i\) to \(\delta_H(\{i\})\), and the two incidences of an edge to \(\varnothing\).

**4.4.** Let \(H\) be a single cycle of length four (so \(d=2\)) with \(b=(1,0,0,0)\). Find an assignment \(y\in Y\) with exactly one disagreeing edge.

**4.5.** Show that \(\mathcal D\) is not nonnegative on all squares, and conclude that \(f_\varepsilon^{1/2}\), for \(0<\varepsilon<1\), has block degree larger than \(D\).

## 5. Solutions

**4.1.** \(\mathrm h(0.05)=0.05\log20+0.95\log(20/19)\), with \(\log20<3\) and \(\log(20/19)<1/19\), so \(\mathrm h(0.05)<0.15+0.05=0.2\). Next \(e^{0.597}<1.818<1/0.55\), so \(\log0.55<-0.597\), and \(0.21+0.95\log0.55\) is less than \(0.21-0.567<-0.35\). Finally \(\log(2e)=1+\log2<1.694\) and \(45\cdot(-0.35)=-15.75\), so the last expression is below \(-14\).

**4.2.** \(\delta_H(S)\mathbin\triangle\delta_H(S')=\delta_H(S\mathbin\triangle S')\) is empty, so no edge leaves \(S\mathbin\triangle S'\); by connectedness this set is \(\varnothing\) or \([t]\).

**4.3.** Every edge at \(i\) has exactly one incidence at \(i\) (there are no loops), and edges not at \(i\) have none; so the image of all incidences at \(i\) consists of the edges at \(i\), which is \(\delta_H(\{i\})\). An edge contains both of its own incidences, an even number.

**4.4.** Number the vertices \(1,2,3,4\) around the cycle, with edges \(12,23,34,41\). Put all bits zero except the bit of vertex \(1\) on the edge \(41\). Vertex \(1\) has bit sum \(1=b_1\), the others have sum \(0\), and only the edge \(41\) disagrees.

**4.5.** For \(0<\varepsilon<1\) the function \(g=f_\varepsilon^{1/2}\) is real and \(g^2=f_\varepsilon\), with \(\mathcal D(g^2)=-\varepsilon<0\). If \(g\) had block degree at most \(D\), Proposition 3.1 would give \(\mathcal D(g^2)\ge0\).

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
- [Grigoriev 2001] D. Grigoriev, *Linear lower bound on degrees of Positivstellensatz calculus proofs for the parity*, Theoret. Comput. Sci. 259 (2001), 613–622. https://logic.pdmi.ras.ru/~grigorev/pub/square_journal.pdf

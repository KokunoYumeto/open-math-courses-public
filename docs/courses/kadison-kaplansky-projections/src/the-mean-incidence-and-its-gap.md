# The mean incidence and its gap

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix an adjacent pair \((i,k)\) and the tables at all earlier marked blocks of its family. The edges of the pair in the auxiliary tower \(Y^0\) depend on the table at its own marked block, which we take uniformly random. This lesson proves that the *mean* incidence operator, averaged over that table, contracts every function of mean zero by a factor less than \(0.8\), uniformly in the pair. The proof organizes functions by the length of the stream prefix they depend on: an incidence step can lengthen the prefix by at most one or two blocks, and each block that is read anew is randomized by an independent uniform vector, which a Fourier computation turns into a gain [OpenAI-KK, Section 5, Lemmas 5.1 and 5.2].

- The incidence operators (Section 1).
- A conditional Fourier estimate (Section 2).
- Prefixes and causality (Section 3).
- The gap of the mean (Section 4).

The notation of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md) and [Gated permutations and the two towers](gated-permutations-and-the-two-towers.md) is in force. Write \(A=A_i\), \(B=B_k\), \(D'=D_{ik}\) and \(E=d|A|=D'|B|\), the number of edges of the pair.

## 1. The incidence operators

Give \(A\) and \(B\) the uniform probability measures, with the inner products of \(L^2(A)\) and \(L^2(B)\). For a realization of the edges of the pair, let
\[
\begin{gathered}
(Nf)(a)=\frac1d\sum_{e:\,e_-=a}f(e_+),\\
(N^*g)(b)=\frac1{D'}\sum_{e:\,e_+=b}g(e_-),
\end{gathered}
\]
for \(f\) on \(B\) and \(g\) on \(A\), where \(e_-\in A\) and \(e_+\in B\) are the ends of the edge \(e\), and parallel edges count separately. Both inner products \(\langle Nf,g\rangle\) and \(\langle f,N^*g\rangle\) equal \(E^{-1}\sum_ef(e_+)\overline{g(e_-)}\), so \(N^*\) is the adjoint of \(N\). Both operators map constants to constants, and they are contractions: by Jensen's inequality,
\[
\begin{aligned}
\|Nf\|^2&\le\frac1{|A|}\sum_a\frac1d\sum_{e_-=a}|f(e_+)|^2\\
&=\frac1E\sum_e|f(e_+)|^2=\|f\|^2 .
\end{aligned}
\]
Let \(M=\mathbb EN\), the expectation over the uniformly random table of the marked block of \((i,k)\). Then \(M^*=\mathbb EN^*\), and \(M\), \(M^*\) are contractions that map constants to constants and functions of mean zero to functions of mean zero.

## 2. A conditional Fourier estimate

For a function \(f\) on \(\mathbb F_2^m\) and a linear functional \(\zeta\) on \(\mathbb F_2^m\), put \(\hat f(\zeta)=2^{-m}\sum_zf(z)(-1)^{\zeta(z)}\). Then \(f(z)=\sum_\zeta\hat f(\zeta)(-1)^{\zeta(z)}\) and \(\sum_\zeta|\hat f(\zeta)|^2=2^{-m}\sum_z|f(z)|^2\).

**Lemma 2.1** (conditional Fourier estimate; [OpenAI-KK, Lemma 5.1]). Let \(C\), \(U\), \(V\), \(W\) be independent random variables, \(U\) uniform on \(\mathbb F_2^t\) and \(V\) uniform on \(\mathbb F_2^m\). For \(1\le a\le q\) let \(M_a:\mathbb F_2^t\to\mathbb F_2^m\) be linear, \(o_a\) a function of \((C,W)\), and \(f_a(C,z)\) complex functions with \(\mathbb E|f_a(C,Z)|^2<\infty\) for \(Z\) uniform. Put
\[
\begin{gathered}
F=\frac1q\sum_af_a(C,V+M_aU+o_a),\\
\mu(C)=\frac1q\sum_a2^{-m}\sum_zf_a(C,z).
\end{gathered}
\]
Suppose that for every nonzero functional \(\zeta\) on \(\mathbb F_2^m\), every set of indices \(a\) on which \(\zeta M_a\) takes one value has at most \(\theta q\) elements. Then \(\mathbb E(F\mid C,U,W)=\mu(C)\), and
\[
\begin{aligned}
&\mathbb E|F-\mu(C)|^2\\
&\quad\le\theta\,\mathbb E\Bigl[\frac1q\sum_a2^{-m}\sum_z|f_a(C,z)|^2\Bigr] .
\end{aligned}
\]

*Proof.* For fixed \(C,U,W\), the vector \(V+M_aU+o_a\) is uniform, which gives the first identity. Expanding each \(f_a(C,\cdot)\) in its Fourier series, the term \(\zeta=0\) of \(F\) is \(\mu(C)\), and
\[
\begin{aligned}
&F-\mu(C)\\
&\quad=\frac1q\sum_a\sum_{\zeta\ne0}\hat f_a(\zeta)\\
&\qquad\cdot(-1)^{\zeta(V)+\zeta(M_aU)+\zeta(o_a)} .
\end{aligned}
\]
In \(\mathbb E_{U,V}|F-\mu(C)|^2\), averaging over \(V\) kills the products of terms with different \(\zeta\), and averaging over \(U\) kills the products of terms \(a,b\) with \(\zeta M_a\ne\zeta M_b\). So
\[
\begin{aligned}
&\mathbb E_{U,V}|F-\mu(C)|^2\\
&\quad=\frac1{q^2}\sum_{\zeta\ne0}\sum_{\mathcal C}\Bigl|\sum_{a\in\mathcal C}(-1)^{\zeta(o_a)}\hat f_a(\zeta)\Bigr|^2 ,
\end{aligned}
\]
where \(\mathcal C\) runs over the classes of indices with a common value of \(\zeta M_a\). By the Cauchy–Schwarz inequality each square is at most \(|\mathcal C|\sum_{a\in\mathcal C}|\hat f_a(\zeta)|^2\le\theta q\sum_{a\in\mathcal C}|\hat f_a(\zeta)|^2\). Summing over classes and \(\zeta\), and using Parseval's identity, the right side is at most \(\frac\theta q\sum_a2^{-m}\sum_z|f_a(C,z)|^2\). Integrate over \(C\) and \(W\). \(\square\)

By Lemma 6.1 of the lesson on streams and slots, the hypothesis holds with \(\theta=10^{-3}\) when \(M_a\) is the map of a slot on a full block of length \(s\) (input \(\mathbb F_2^s\), output the block and its spill), and with \(\theta=0.55\) when it is that map restricted to a nonempty initial segment of the input block.

## 3. Prefixes and causality

For \(h\ge0\) let \(P^A_h\) be the conditional expectation, on \(L^2(A)\), onto the functions of the first \(r+sh\) coordinates of \(u_A\) and the first \(r+sh\) coordinates of \(v_A\); for \(j\ge0\) let \(P^B_j\) be the conditional expectation onto the functions of the first \(sj\) coordinates of \(u_B\) and of \(v_B\). Inactive coordinates are zero, so these are finite increasing families of orthogonal projections, eventually the identity, and \(P^B_0=C_B\) is the projection onto the constants; \(C_A\) is the projection onto the constants of \(L^2(A)\).

**Forward data.** Fix a slot \(a\) of \(A\) and \(j\ge1\). The value at the \(B\)-end of the edge at \(a\) of a function in the range of \(P^B_j\) is determined by
\[
\begin{gathered}
u_A\big|_{[0,r+s(j-1))}\ \text{and}\\
Q_A\big|_{[0,p+sj)} .
\end{gathered}\tag{3.1}
\]
Indeed the first \(p\) coordinates of \(Q_A\) are \(x\), including the bucket; inverting \(\mathcal F\) on the next \(sj\) coordinates gives the first \(j\) blocks of \(u_B\), whose keys use \(A\)-blocks up to \(j-1\). The first \(sj\) coordinates of \(v_B=Q_B+\mathcal K_cu_B\) use \(\mathcal J(u_A)\) up to length \(sj-p'=r+s(j-1)-\beta\), at most \(r+s(j-1)\), whose keys use \(B\)-blocks up to \(j-1\), and \(\mathcal K_c\) applied to the first \(j\) blocks of \(u_B\).

**Reverse data.** Fix a slot \(c\) of \(B\) and \(h\ge0\). The value at the \(A\)-end of a function in the range of \(P^A_h\) is determined by
\[
\begin{gathered}
u_B\big|_{[0,sh)}\ \text{and}\\
Q_B\big|_{[0,p'+r+sh)} .
\end{gathered}\tag{3.2}
\]
The first \(p'\) coordinates of \(Q_B\) are \(x'\), and the bucket is part of the slot; inverting \(\mathcal J\) gives \(u_A\) up to length \(r+sh\), with keys among the first \(h\) blocks of \(u_B\); and \(v_A\) up to length \(r+sh\) uses \(\mathcal F(u_B)\) up to length \(r+sh-p=sh-\alpha\le sh\).

**Lemma 3.1** (causality). For every realization of the table, and hence for \(M\),
\[
\begin{gathered}
\operatorname{ran}(MP^B_j)\subseteq\operatorname{ran}P^A_{j+1},\\
\operatorname{ran}(M^*P^A_h)\subseteq\operatorname{ran}P^B_{h+2} .
\end{gathered}
\]

*Proof.* In (3.1), \(p+sj=r+sj+\alpha\) lies at most two coordinates into \(A\)-block \(j+1\), and these coordinates of \(Q_A=v_A+\mathcal K_au_A\) depend on the whole input block \(j+1\) through the diagonal coefficient. So the data (3.1) are functions of the first \(r+s(j+1)\) coordinates of \(u_A\) and \(v_A\). In (3.2), \(p'+r+sh=(h+1)s+\beta\) lies at most two coordinates into \(B\)-block \(h+2\), and the same reasoning applies. \(\square\)

**Lemma 3.2** (one new block). Let \(1\le j\le n\) in the notation of the cutoff, so that \(A\)-block \(j\) is full, and suppose \(r+sj+\alpha\le|v_A|\). Then
\[
\|(1-P^A_{j-1})MP^B_j\|^2\le10^{-3} .
\]
Symmetrically, if \(B\)-block \(h+1\) is full and \(s(h+1)+\beta\le|v_B|\), then \(\|(1-P^B_h)M^*P^A_h\|^2\le10^{-3}\).

*Proof.* Let \(f\) be in the range of \(P^B_j\), and put \(R=r+s(j-1)\). On \(A\) with the uniform measure, let \(C\) be the first \(R\) coordinates of \(u_A\) and of \(v_A\), \(U\) the \(A\)-block \(j\) of \(u_A\), \(V\) the coordinates of \(v_A\) in \([R,R+s+\alpha)\), and \(W\) all remaining coordinates; these are independent and uniform. By (3.1), the value of \(f\) at the \(B\)-end of the edge at the slot \(a\), averaged over the table, is a function \(f_a(C,Z_a)\) of \(C\) and the coordinates of \(Q_A\) in \([R,R+s+\alpha)\),
\[
Z_a=V+M_aU+o_a ,
\]
where \(M_a\) is the map of Lemma 6.1 of the lesson on streams and slots, and \(o_a\) collects the spill from \(A\)-block \(j-1\), a function of \(C\), and the contribution of \(A\)-block \(j+1\) to the last \(\alpha\) coordinates, a function of \(W\). So \(Mf=\frac1d\sum_af_a(C,Z_a)\), and Lemma 2.1 with \(\theta=10^{-3}\) gives
\[
\begin{aligned}
&\mathbb E|Mf-\mu(C)|^2\\
&\quad\le10^{-3}\,\mathbb E\Bigl[\frac1d\sum_a2^{-m}\sum_z|f_a(C,z)|^2\Bigr],
\end{aligned}
\]
where \(\mu(C)=P^A_{j-1}Mf\).

The right side is at most \(10^{-3}\|f\|^2\). Indeed, for each \(a\), \(Z_a\) is uniform given \(C\), so \(\mathbb E\,2^{-m}\sum_z|f_a(C,z)|^2=\mathbb E|f_a(C,Z_a)|^2\); by Jensen's inequality this is at most the average over the table of \(|f|^2\) at the \(B\)-end of the edge at \(a\); and averaging over the slots and a uniform vertex of \(A\) gives a uniform vertex of \(B\), because every vertex of \(B\) has the same number of slots. The second statement is proved in the same way, with the roles of the sides exchanged, using (3.2) and the \(B\)-block \(h+1\) with the coordinates \([sh,s(h+1)+\beta)\) of \(v_B\). \(\square\)

## 4. The gap of the mean

**Lemma 4.1** (uniform gap of the mean; [OpenAI-KK, Lemma 5.2]). For every adjacent pair and every choice of the tables at the earlier marked blocks of its family,
\[
\begin{aligned}
\bigl\|M:\mathbf1_B^\perp\to\mathbf1_A^\perp\bigr\|&\le\sqrt{16\cdot10^{-3}+0.55}\\
&<0.8 .
\end{aligned}
\]

*Proof.* Let \(E^A_0=P^A_0-C_A\), \(E^A_h=P^A_h-P^A_{h-1}\) for \(h\ge1\), and \(E^B_j=P^B_j-P^B_{j-1}\) for \(j\ge1\). They are orthogonal projections whose ranges decompose the functions of mean zero. By Lemma 3.1, \(E^A_hME^B_j=0\) unless
\[
-2\le h-j\le1 .
\]
For \(h-j\in\{0,1\}\), \(E^A_h\le1-P^A_{j-1}\) and \(E^B_j\le P^B_j\), so \(\|E^A_hME^B_j\|\le10^{-3/2}\) by Lemma 3.2 whenever its hypotheses hold. For \(j-h\in\{1,2\}\), \(E^B_j\le1-P^B_h\), and the adjoint form of Lemma 3.2 gives the same bound. Along a band of fixed \(h-j\) the blocks have mutually orthogonal domains and mutually orthogonal ranges, so the sum along a band has norm at most \(10^{-3/2}\), and the sum of the four bands at most \(4\cdot10^{-3/2}=\sqrt{16\cdot10^{-3}}\). It remains to treat the last block, in each of the two forms of the cutoff (Lemma 2.2 of the lesson on streams and slots).

*Form (B): \(l_A=r+ns\), \(l_B=ns+t\).* Then \(|v_A|=r+ns+\alpha+t\) and \(|v_B|=(n+1)s+\beta\). For inputs in the range of \(P^B_n-C_B\) only \(j\le n\) occurs: in the bands \(h-j\in\{0,1\}\) Lemma 3.2 uses the full \(A\)-block \(j\le n\) and needs \(r+sj+\alpha\le|v_A|\), true; in the bands \(j-h\in\{1,2\}\), \(h\le n-1\), the full \(B\)-block \(h+1\le n\) is used and \(s(h+1)+\beta\le|v_B|\). Hence
\[
\begin{gathered}
\|M(P^B_n-C_B)\|\\
\le4\cdot10^{-3/2} .
\end{gathered}\tag{4.1}
\]
Now let \(g\) be a function on \(A\). At a vertex of \(B\) and a slot \(c\), the blocks of \(u_B\) before the marked block \(B(n+1)\) determine, by inversion, the whole of \(u_A\) and all of \(v_A\) except its last \(t\) coordinates, which occupy \([p+ns,p+ns+t)\). The table of the marked block matches these \(t\) coordinates of \(Q_A\) uniformly at random, and \(\mathcal K_au_A\) vanishes on them, since its last spill ends at \(r+ns+\alpha=p+ns\); so after averaging over the table, the last \(t\) coordinates of \(v_A\) are uniform, and the averaged value of \(g\) at the \(A\)-end is a function of \(u_B|_{[0,ns)}\) and \(Q_B|_{[0,(n+1)s+\beta)}\) only. Conditioning on the first \(ns\) coordinates of \(u_B\) and \(v_B\), the coordinates of \(Q_B\) in \([ns,(n+1)s+\beta)\) have the form \(V+M_cU+o_c\) with \(U\) the \(t\) active coordinates of the last \(B\)-block and \(V\) the coordinates of \(v_B\) in that interval. Lemma 2.1 with \(\theta=0.55\), and the norm argument of Lemma 3.2, give
\[
\|(1-P^B_n)M^*\|^2\le0.55 .
\]
For \(g\) of mean zero, \(M^*g\) has mean zero, so \(P^B_nM^*g=(P^B_n-C_B)M^*g\), whose norm is at most \(4\cdot10^{-3/2}\|g\|\) by (4.1). The two components are orthogonal, so \(\|M^*g\|^2\le(16\cdot10^{-3}+0.55)\|g\|^2\).

*Form (A): \(l_B=(n+1)s\), \(l_A=r+ns+t\).* Then \(|v_A|=r+(n+1)s+\alpha\) and \(|v_B|=(n+1)s+\beta+t\). For inputs in the range of \(P^A_n-C_A\), the bands use full \(A\)-blocks \(j\le n\), with \(r+sj+\alpha\le|v_A|\), and full \(B\)-blocks \(h+1\le n+1\), with \(s(h+1)+\beta\le|v_B|\); so \(\|M^*(P^A_n-C_A)\|\le4\cdot10^{-3/2}\). The table of the marked block \(A(n+1)\) matches the last \(t\) coordinates of \(Q_B\), which start at \(p'+r+ns=(n+1)s+\beta\), where \(\mathcal K_cu_B\) has ended; so they are the last \(t\) coordinates of \(v_B\), and after averaging, the value of \(f\) at the \(B\)-end is a function of \(u_A|_{[0,r+ns)}\) and \(Q_A|_{[0,p+(n+1)s)}\). Conditioning on the first \(r+ns\) coordinates of \(u_A\) and \(v_A\), with \(U\) the \(t\) active coordinates of the last \(A\)-block and \(V\) the coordinates of \(v_A\) in \([r+ns,r+(n+1)s+\alpha)\), Lemma 2.1 gives \(\|(1-P^A_n)M\|^2\le0.55\), and the same orthogonal combination proves the bound for \(\|Mf\|\), \(f\perp\mathbf1_B\).

In both forms the bound holds for all \(1\le t\le s\) and \(\alpha,\beta\in\{0,1,2\}\), and since \(n\ge n_0-1\), there are full blocks before the last one. \(\square\)

## 5. Exercises

**5.1** (easy). Verify the identity \(\sum_\zeta|\hat f(\zeta)|^2=2^{-m}\sum_z|f(z)|^2\) for \(m=1\) and \(f=(f(0),f(1))\).

**5.2** (medium). In Lemma 2.1 let \(q=2\), \(t=m=1\), \(M_1=M_2=1\), \(o_1=o_2=0\), and \(f_1=f_2=f\) with \(f(0)=1\), \(f(1)=-1\). Compute \(F\), \(\mu\) and \(\mathbb E|F-\mu|^2\), and show that the hypothesis holds only with \(\theta=1\). What changes if \(M_2=0\)?

**5.3** (medium). Show that \(\|M\|\le1\) on \(L^2(B)\) and that \(\|M:\mathbf1_B^\perp\to\mathbf1_A^\perp\|\) is the second largest singular value of \(M\).

**5.4** (medium). Explain why Lemma 3.1 cannot be improved to \(\operatorname{ran}(MP^B_j)\subseteq\operatorname{ran}P^A_j\) in general.

## 6. Solutions

**5.1.** \(\hat f(0)=\frac{f(0)+f(1)}2\), \(\hat f(1)=\frac{f(0)-f(1)}2\), and \(|\hat f(0)|^2+|\hat f(1)|^2=\frac{|f(0)|^2+|f(1)|^2}2\).

**5.2.** \(F=f(V+U)=(-1)^{V+U}\), \(\mu=0\), and \(\mathbb E|F|^2=1\). For \(\zeta\ne0\) both indices have \(\zeta M_a=\zeta\), one class of size \(2=q\), so \(\theta=1\), and the bound \(\theta\cdot1=1\) is attained. If \(M_2=0\), the classes are \(\{1\}\) and \(\{2\}\), \(\theta=\frac12\), and \(F=\frac12((-1)^{V+U}+(-1)^V)\) has \(\mathbb E|F|^2=\frac12\).

**5.3.** \(M\) is an average of contractions. It maps the constants of \(B\) to those of \(A\) and the orthogonal complements to each other, so its singular values are \(1\), on the constants, and those of the restriction to \(\mathbf1_B^\perp\).

**5.4.** The coordinates of \(Q_A\) in \([r+sj,r+sj+\alpha)\) are needed in (3.1) when \(\alpha>0\), and they involve \(\lambda_au\) for the whole \(A\)-block \(j+1\) of \(u_A\); a function of them is generally not a function of the first \(r+sj\) coordinates.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 5, Lemmas 5.1 and 5.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026

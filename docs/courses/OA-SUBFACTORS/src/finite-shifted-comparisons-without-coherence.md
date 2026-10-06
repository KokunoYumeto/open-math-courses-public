# Finite comparisons suffice without a coherent limit map

Suitable finite comparisons and actual generation imply the tower bicommutant equality and the compatible smooth hypertrace. The finite maps may be independent and may have cup images with vanishing errors. We prove the complete analytic implication, including a fixed extra shift and the two-step blocked version. The general finite maps themselves remain an additional requirement.

The primary reference is Sorin Popa, [*Classification of amenable subfactors of type II*](https://doi.org/10.1007/BF02392646), printed pp.223–224, the general nonextremal paragraph of 4.5.1. Printed223 has \(M\supset N\supset N_1\supset\cdots\), so \(N_0=N\) and \(N_i=M_{-i-1}\). Uniformly, the source cup \(\epsilon_t\) is our \(e_{t-1}\): in particular \(\epsilon_{-i}=e_{-i-1}\). Reindexing the source's \(m,i\) by \(m+1,i+1\) therefore gives exactly the unshifted course comparison (65.9) with \(r=0\). Its written upward endpoint \(M_{m+1}\) does not constitute an extra shift after that reindexing. The earlier 62.4 unshifted endpoint criterion remains correct.

We use [abstract blocking](reflected-traces-and-uniform-bounds.md),14.8, which supplies the skipped basic-construction triple.[64.1](two-step-cups-and-composed-densities.md) identifies its normalized four-cup word, and 64.2–64.3 prove the modified composition, common basis and sharp squared index. None of these results supplies the finite trace comparison. We use [scalar cup placement](canonical-rescaling-of-jones-cups.md),63.5; [finite normal tower representation](reflected-traces-and-uniform-bounds.md),14.2; and [stage collapse](smooth-representations-and-tower-compression.md),61.4. The elementary expectation estimates needed below are proved here. Finite-dimensionality of relative commutants follows from 2.5.

## Generation at every fixed lower endpoint

Let \(N\subset M\) be a finite-index inclusion of II₁ factors, of index \(d\), with actual Jones tunnel \(M_{-1}=N,M_0=M\). Put \(\lambda=d^{-1}\) and

\[
\begin{gathered}
D_m=M_{-m}'\cap M,\\
M=\left(\bigcup_mD_m\right)''.
\end{gathered}
\tag{65.1}
\]

For \(m\ge i\ge0\), put \(D_{m,i}=M_{-m}'\cap M_{-i}\). Then

\[
\begin{gathered}
E_{M_{-i}}(D_m)=D_{m,i},\\
M_{-i}=\left(\bigcup_{m\ge i}D_{m,i}\right)''.
\end{gathered}
\tag{65.2}
\]

Indeed \(M_{-m}\subset M_{-i}\), so bimodularity sends a commuting element to a commuting element. Every element of \(D_{m,i}\) is already in \(D_m\) and is fixed by the expectation, proving the range equality. Kaplansky density for the increasing finite-dimensional union in (65.1) supplies uniformly bounded approximants to every element of \(M\). Apply the normal expectation to these approximants. Their images have weak closure \(M_{-i}\), proving (65.2). This step requires actual generation, without a separately imposed trace comparison.

## A lower estimate for nonnested finite commutants

Fix \(i\ge1\), set \(P=M_{-i}\), \(Q=M_{-i+1}\), and choose an actual projection \(g_i\in Q\) satisfying

\[
\begin{gathered}
g_i\in M_{-i-1}',\\
E_{P'\cap Q}(g_i)=\lambda1.
\end{gathered}
\tag{65.3}
\]

Such projections are supplied by 63.5 in every prescribed tunnel. For \(m\ge i+1\), write

\[
\begin{gathered}
F_{m,i}=D_{m,i-1},\quad G_{m,i}=D_{m,i},\\
K_{m,i}=G_{m,i}'\cap F_{m,i},\\
R_{k,i}=G_{k,i}'\cap Q .
\end{gathered}
\tag{65.4}
\]

The projection \(g_i\) belongs to \(F_{m,i}\) by its deeper commutation. Although the \(K_{m,i}\) need not form a nested family, for \(m\ge k\ge i+1\) one has \(K_{m,i}\subset R_{k,i}\). Consequently

\[
\begin{gathered}
\|E_{K_{m,i}}(g_i)-\lambda1\|_2
\le \delta_{k,i},\\
\delta_{k,i}:=\|E_{R_{k,i}}(g_i)-\lambda1\|_2,\\
\delta_{k,i}\longrightarrow0\quad(k\longrightarrow\infty).
\end{gathered}
\tag{65.5}
\]

All expectations and norms here use the inherited normalized trace of \(Q\).

**Proof of the limit.** The algebras \(R_{k,i}\) decrease, and (65.2) gives
\(\bigcap_kR_{k,i}=P'\cap Q\). For a bounded \(x\in Q\), put \(x_k=E_{R_{k,i}}(x)\). If \(l\ge k\), orthogonal projection in \(L^2(Q)\) gives
\[
\|x_k-x_l\|_2^2=\|x_k\|_2^2-\|x_l\|_2^2.
\]
The squared norms decrease to an infimum, so \(x_k\) is \(L^2\)-Cauchy. Its uniform bound \(\|x_k\|\le\|x\|\) supplies an ultraweak cluster in \(Q\). Every cluster lies in each \(R_{k,i}\); pairing with bounded elements identifies it with the \(L^2\) limit. For \(a\in P'\cap Q\), one has \(\tau(a^*x_k)=\tau(a^*x)\). These identities characterize the limit as \(E_{P'\cap Q}(x)\). Apply this to \(g_i\) and use (65.3).

For the inequality, nested expectations give
\[
E_{K_{m,i}}(g_i-\lambda1)
=E_{K_{m,i}}E_{R_{k,i}}(g_i-\lambda1).
\]
The last expectation is an \(L^2\) contraction. This proves (65.5), including the nonnested case. No commutant-continuity assertion for the \(K_{m,i}\) is needed.

## Finite compression bounds an infinite expectation

Let \(\mathcal T\) be a finite tracial von Neumann algebra, \(A\subset\mathcal T\) a unital von Neumann subalgebra, and \(C\subset\mathcal T\) another such algebra. Suppose \(H\subset A\) and \(E_A(C)\subset H\). For \(x\in A\) and a scalar \(s\),

\[
\begin{gathered}
\|E_C(x)-s1\|_2\\
\le\|E_H(x)-s1\|_2.
\end{gathered}
\tag{65.6}
\]

**Proof.** Put \(c=E_C(x)-s1\) and \(h=E_A(c)\in H\). Orthogonal projection, then trace adjointness and Cauchy–Schwarz, give
\[
\begin{aligned}
\|c\|_2^2
&=\langle x-s1,c\rangle
=\langle x-s1,h\rangle\\
&=\langle E_H(x)-s1,h\rangle\\
&\le\|E_H(x)-s1\|_2\,\|h\|_2\\
&\le\|E_H(x)-s1\|_2\,\|c\|_2 .
\end{aligned}
\]
Divide when \(c\ne0\); the other case is immediate. This proof covers arbitrary complex \(x,s\).

For the canonical tracial tower completion \(\mathcal T\), fix an integer \(r\ge0\) and put
\[
\begin{gathered}
B_j=M_j'\cap\mathcal T,\quad C_j=B_j'\cap\mathcal T,\\
U_{m,i}^{(r)}=M_{i-1+r}'\cap M_{m+r},\\
V_{m,i}^{(r)}=M_{i+r}'\cap M_{m+r},\\
H_{m,i}^{(r)}=(V_{m,i}^{(r)})'\cap U_{m,i}^{(r)}.
\end{gathered}
\tag{65.7}
\]

The cup \(e_{i+r}\in M_{i+r+1}\) implements \(M_{i+r-1}\subset M_{i+r}\); it belongs to \(U_{m,i}^{(r)}\) for \(m\ge i+1\). For \(c\in C_{i+r}\cap B_{i+r-1}\), the element \(E_{M_{m+r}}(c)\) belongs to \(U_{m,i}^{(r)}\) by \(M_{i+r-1}\)-bimodularity. It commutes with \(V_{m,i}^{(r)}\), by the same bimodularity and \(V_{m,i}^{(r)}\subset B_{i+r}\). Thus it lies in \(H_{m,i}^{(r)}\).

For \(x=e_{i+r}\), the expectation \(E_{C_{i+r}}(x)\) belongs to \(B_{i+r-1}\): \(M_{i+r-1}\subset C_{i+r}\) and \(x\in M_{i+r-1}'\). Applying the preceding pairing proof with this \(c\), and with \(E_{M_{m+r}}\) as the finite compression, therefore gives

\[
\begin{gathered}
\|E_{C_{i+r}}(e_{i+r})-\lambda1\|_2\\
\le\|E_{H_{m,i}^{(r)}}(e_{i+r})-\lambda1\|_2.
\end{gathered}
\tag{65.8}
\]

One need not assert \(E_{U_{m,i}^{(r)}}(C_{i+r})\subset H_{m,i}^{(r)}\) for arbitrary elements of \(C_{i+r}\): the proof only uses the element \(c\in C_{i+r}\cap B_{i+r-1}\), whose finite compression was just checked.

## Independent finite pair maps give scalar upper cups

For every \(i\ge1\), suppose there are arbitrarily large integers \(m\) and unital trace-preserving linear *-anti-isomorphisms

\[
\begin{gathered}
\alpha_{m,i}:F_{m,i}\longrightarrow U_{m,i}^{(r)},\\
\alpha_{m,i}(G_{m,i})=V_{m,i}^{(r)},\\
\|\alpha_{m,i}(g_i)-e_{i+r}\|_2
\le\varepsilon_{m,i}\longrightarrow0 .
\end{gathered}
\tag{65.9}
\]

The maps may be chosen independently for different \(m,i\). The exact cup image in the source is the special case \(\varepsilon_{m,i}=0\). The norms on the last line use the inherited tower trace.

Then, for every \(m\) admitted in (65.9) and every \(i+1\le k\le m\),

\[
\begin{gathered}
\|E_{C_{i+r}}(e_{i+r})-\lambda1\|_2\\
\le\delta_{k,i}+\varepsilon_{m,i},\\
E_{C_j}(e_j)=\lambda1\\
(j\ge r+1).
\end{gathered}
\tag{65.10}
\]

**Proof.** Reversing products preserves the condition of commuting with a subalgebra, so \(\alpha_{m,i}(K_{m,i})=H_{m,i}^{(r)}\). A trace-preserving *-anti-isomorphism is an \(L^2\) isometry: \(\tau(\alpha(x)^*\alpha(x))=\tau(\alpha(xx^*))=\tau(xx^*)=\tau(x^*x)\). It carries the orthogonal projection onto \(L^2(K_{m,i})\) to the projection onto \(L^2(H_{m,i}^{(r)})\). Hence it intertwines their expectations. Equation (65.5), triangle inequality and contraction give
\[
\begin{aligned}
\|E_{H_{m,i}^{(r)}}(e_{i+r})-\lambda1\|_2
&\le\|E_{H_{m,i}^{(r)}}(\alpha_{m,i}(g_i))-\lambda1\|_2\\
&\quad+\|e_{i+r}-\alpha_{m,i}(g_i)\|_2\\
&\le\delta_{k,i}+\varepsilon_{m,i}.
\end{aligned}
\]
Use (65.8). First fix \(k\), then take an unbounded admitted subsequence of \(m\) with \(\varepsilon_{m,i}\to0\); finally send \(k\to\infty\). This proves the exact scalar identity. No common subsequence for all \(i\), no comparison between two finite maps, and no extension of any \(\alpha_{m,i}\) is used.

The same proof works for *-isomorphisms, but the source asks for anti-isomorphisms and (65.9) keeps that orientation explicit.

## Collapse above the initial factor, then recover it

Under (65.1), (65.3) and (65.9),

\[
(M'\cap\mathcal T)'\cap\mathcal T=M.
\tag{65.11}
\]

**Proof.** Apply 61.4 to the tower starting at \(M_{r+1}\), with \(B=B_{r+1}=M_{r+1}'\cap\mathcal T\). Its successive tail commutants are exactly \(B_j\), \(j\ge r+1\), and (65.10) supplies every required cup condition. Thus \(C_{r+1}=M_{r+1}\).

Since \(B_{r+1}\subset B_0\), one has \(M\subset C_0\subset C_{r+1}=M_{r+1}\). For \(y\in C_0\) and \(m\ge r+1\), the finite reflected algebra \(J D_mJ\) belongs to \(M'\cap M_m\subset B_0\), by 14.2. Therefore \(y\) commutes with it. Transport this finite relation to the coherent faithful normal representation of \(M_m\) on \(L^2(M)\), where \(J\widehat x=\widehat{x^*}\). Generation (65.1) makes the union of \(J D_mJ\) weakly dense in \(JMJ=M'\). Commutation with the fixed bounded operator \(y\) is weakly closed. Hence \(y\in(M')'=M\). This proves (65.11). Only finite stages are represented normally; the whole tracial limit is not assumed to act normally on \(L^2(M)\).

Generation also makes \(N\) a weak closure of its increasing finite-dimensional algebras \(M_{-m}'\cap N\), by (65.2). The explicit construction 61.8 therefore gives the injective projections for \(M,N\) and every finite tower factor;61.7 gives the projection onto \(\mathcal T\). Combine this with (65.11) and 61.6. Every smooth nondegenerate expected representation \(N\subset M\subset(U\subset_E V)\) has a UCP conditional expectation \(F:V\to M\) with \(F(U)\subset N\) and \(E_NF=FE\). The state \(\tau_MF\) is the compatible \(M\)-hypertrace. These projections can be nonnormal. No extra separability hypothesis is added: the actual generating finite-dimensional sequence is the input.

## Exact two-step application in the original tower

Keep an original index-\(d\) tower \((M_t)\), and block it by \(L_t=M_{2t}\). Its adjacent index is \(D=d^2\), and its cup parameter is \(\Lambda=d^{-2}\).64.1 gives
\[
\begin{gathered}
Q_a=d\,e_{a+2}e_{a+1}e_{a+3}e_{a+2}\\
\in M_{a+4},\\
\text{implementing }M_a\subset M_{a+2},\\
b_j=Q_{2j-2}\in L_{j+1}.
\end{gathered}
\tag{65.12}
\]

Use63 directly on this actual blocked tracial inclusion. For \(i\ge1\), let \(\kappa_i^{\mathrm{blk}}\in Z(M_{-2i-2}'\cap M_{-2i})\) be its own canonical density, put \(c_i=(\kappa_i^{\mathrm{blk}})^{1/2}\), and set
\[
\begin{gathered}
g_i^{\mathrm{blk}}=c_iQ_{-2i-2}c_i\\
\in M_{-2i+2}\cap M_{-2i-2}',\\
E_{M_{-2i}'\cap M_{-2i+2}}(g_i^{\mathrm{blk}})
=d^{-2}1 .
\end{gathered}
\tag{65.13}
\]

This uses the canonical density of the blocked inclusion itself. It does not require identifying it with a product of adjacent densities.

The exact remaining finite comparison input is, for each \(i\ge1\), at arbitrarily large \(m\ge i+1\),
\[
\begin{gathered}
\alpha_{m,i}:
M_{-2m}'\cap M_{-2i+2}\\
\longrightarrow M_{2i-2}'\cap M_{2m},\\
\alpha_{m,i}(M_{-2m}'\cap M_{-2i})\\
=M_{2i}'\cap M_{2m},\\
\alpha_{m,i}(g_i^{\mathrm{blk}})=Q_{2i-2},
\end{gathered}
\tag{65.14}
\]
with the inherited traces and anti-isomorphism orientation. A vanishing \(L^2\) cup error also suffices by (65.9).

The even downward subsequence is cofinal, so (65.1) remains actual generation for the blocked tunnel. The even upward subsequence has the same tracial closure \(\mathcal T\). Apply 65.1–65.5 to \((L_t)\) with \(\Lambda\) and \(r=0\). Its collapse starts at \(L_1=M_2\), after which the finite normal representation of \(M_2\) and the original generating union recover \(M\), exactly as in 65.5. This proves the original bicommutant (65.11). For a smooth expected representation of the original one-step inclusion \(N\subset M\), use the original tower and 61.6–61.8 to obtain its compatible hypertrace. Thus the blocked criterion suffices for the original inclusion without assuming one-step finite comparisons.

## Exact examples and the limit-map distinction

**An incoherent family.** In \(\operatorname{Mat}_2\) with normalized trace, let \(G\) be the diagonal algebra,
\[
q=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad V=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Both \(T(x)=x^{\mathsf T}\) and \(S(x)=Vx^{\mathsf T}V^*\) are linear trace-preserving *-anti-automorphisms, preserve \(G\), and fix \(q\). Moreover \(E_{G'\cap\operatorname{Mat}_2}(q)=\tfrac121\). Alternate \(T,S\) on a constant chain. Their values on \(E_{00}\) alternate between \(E_{00},E_{11}\), so they have no pointwise limit and do not define a common map on the union. This finite example demonstrates that coherence is genuinely extra. It is not asserted to be a generating II₁ tunnel.

**A lower quantitative check.** In \(\operatorname{Mat}_2\otimes\operatorname{Mat}_2\), let \(P=\operatorname{Mat}_2\otimes1\) and let \(q\) be the rank-one projection onto \((|00\rangle+|11\rangle)/\sqrt2\). Then \(E_{P'}(q)=\tfrac141\). At the preceding scalar stage, \(R_0\) is the entire algebra and
\(\|q-\tfrac141\|_2^2=3/16\); at the full \(P\)-stage, \(\delta^2=0\). Any finite \(K\subset P'\) has \(E_K(q)=\tfrac141\), exactly as (65.5) requires. These are finite algebra checks, not a substitute for generation or (65.14).

**Endpoint example.** For \(i=1,m=3\), (65.14) has domain \(M_{-6}'\cap M_0\), subalgebra \(M_{-6}'\cap M_{-2}\), range \(M_0'\cap M_6\), and image subalgebra \(M_2'\cap M_6\). It sends \(g_1^{\mathrm{blk}}\in M_0\) to \(Q_0\in M_4\). The target cup implements \(M_0\subset M_2\). The eventual scalar condition is onto \((M_2'\cap\mathcal T)'\cap\mathcal T\), and the first collapse is at \(M_2\).

## Exercises with complete solutions

**Exercise 65.1 — source indices.** Translate the source finite comparison with source \(i=2,m=5\) into the original one-step course notation. Locate both cups.

**Solution.** Since \(N_t=M_{-t-1}\), its domain \(N_5'\cap N_1\) is \(M_{-6}'\cap M_{-2}\), and its subalgebra \(N_5'\cap N_2\) is \(M_{-6}'\cap M_{-3}\). The range is \(M_2'\cap M_6\), and the image subalgebra is \(M_3'\cap M_6\). These are (65.9) with course \(i=3,m=6,r=0\). The source cup \(\epsilon_{-2}'\) is the modified \(g_3\in M_{-2}\); its image \(\epsilon_4\) is \(e_3\in M_4\), implementing \(M_2\subset M_3\). This calculation alone does not establish existence of that comparison.

**Exercise 65.2 — nonnested expectations.** In \(\operatorname{Mat}_2\), set \(p=E_{00}\), \(\lambda=1/2\). Let \(K_1=K_3\) be the diagonal algebra and \(K_2\) the algebra diagonal in the orthonormal basis \((1,1)/\sqrt2,(1,-1)/\sqrt2\). Compute \(\|E_{K_j}(p)-\lambda1\|_2^2\). Explain why (65.5) uses the decreasing reference algebras.

**Solution.** For \(j=1,3\), the expectation fixes \(p\), giving squared norm \(1/4\). The two diagonal entries of \(p\) in the second basis are both \(1/2\), so \(E_{K_2}(p)=\tfrac121\), giving zero. The three errors are \(1/4,0,1/4\), and are not monotone. Taking the containing reference algebra \(R=\operatorname{Mat}_2\) bounds all three errors by \(1/4\), but does not make them tend to zero. The limit in (65.5) instead uses \(G_{k,i}\) increasing to the actual lower factor, which makes \(R_{k,i}\) decrease to the relative commutant on which the cup expectation is scalar.

**Exercise 65.3 — an approximate cup image.** Suppose a finite family exists on an unbounded subsequence and has \(\varepsilon_{m,i}\le1/m\), with no prescribed rate for \(\delta_{k,i}\to0\). Prove the exact upper scalar expectation without interchanging limits.

**Solution.** Let \(\eta>0\). Choose \(k\ge i+1\) with \(\delta_{k,i}<\eta/2\). Then choose an admitted \(m\ge k\) with \(1/m<\eta/2\). Equation (65.10) makes the fixed upper norm smaller than \(\eta\). Since \(\eta\) was arbitrary, that norm is zero. Faithfulness of the finite trace gives \(E_{C_{i+r}}(e_{i+r})=\lambda1\). Each \(i\) can use its own unbounded subsequence.

**Exercise 65.4 — the inherited traces matter.** On \(\mathbb C\oplus\mathbb C\), put \(\tau(x,y)=x/4+3y/4\). Show that the block exchange is a unital linear *-anti-isomorphism but is not an \(L^2\) isometry.

**Solution.** The algebra is commutative, so the *-isomorphism \((x,y)\mapsto(y,x)\) also reverses multiplication. For \(p=(1,0)\), its squared norm is \(\tau(p)=1/4\), whereas its image has squared norm \(3/4\). Thus algebraic anti-isomorphism alone cannot justify the transfer in 65.4. The traces specified in (65.9) must actually agree through the map. This example supplies no generating tunnel.

**Exercise 65.5 — where collapse starts.** For the general theorem with \(r=2\), locate the first scalar cup and the factor at which 61.4 starts. Give the corresponding answer for (65.14).

**Solution.** The first index is \(i=1\), giving \(e_3\in M_4\) and \(E_{C_3}(e_3)=\lambda1\). The tower starts at \(M_3\), so 61.4 gives \(C_3=M_3\). The finite representation of \(M_3\) then recovers \(C_0=M\) from generation. For (65.14), the blocked tower has \(r=0\), so its first cup is \(b_1=Q_0\in M_4\) and collapse starts at \(L_1=M_2\). Its parameter is \(d^{-2}\), rather than \(d^{-1}\).

**Exercise 65.6 — a density identity is not a completion gate.** Does (65.13) require the product \(K\) in 64.2 to be the general blocked canonical density? What remains to be proved after (65.13)?

**Solution.** Apply 63.1–63.5 directly to the actual tracial inclusion \(L_{-i-1}\subset L_{-i}\) and its blocked basic construction supplied by 14.8/64.1. Its own central canonical density \(\kappa_i^{\mathrm{blk}}\) supplies (65.13) without a product identity. If one wants to identify that cup with the composed adjacent modified cups in 64.2, their densities must be compared separately; unchanged scalar index alone does not identify them. [Theorem 66.3 and Corollary 66.4](canonical-density-transitivity.md) now prove that separate general identity. For the bicommutant route proved here, the outstanding input is the finite inherited-trace pair comparison (65.14), with the stated cup image or a vanishing \(L^2\) cup error. A coherent family and a normal comparison limit are not additional requirements.

![Finite scalar errors pass through independent finite comparisons and finite compression.](figures/finite-shifted-comparisons-without-coherence.svg)

*Figure 65.1.* The actual pairs and cup endpoints are (65.4), (65.7), (65.9) and (65.14). The error bound is (65.10); the decreasing reference error is (65.5). The endpoint example is \(i=1,m=3\). The last implication uses the finite representation in 65.5. Boxes denote algebras and maps, not spatial geometry. [Reproducible figure source](figures/finite-shifted-comparisons-without-coherence.py). Compare Popa 4.5.1.

The general finite pair maps (65.14) remain an additional requirement. This lesson proves the full analytic implication from the specified finite input to the bicommutant and compatible smooth hypertrace. The finite maps need neither a coherent family nor a normal comparison limit. [Lesson 66](canonical-density-transitivity.md) gives the separate general blocked density identity and identifies the lower cup explicitly.

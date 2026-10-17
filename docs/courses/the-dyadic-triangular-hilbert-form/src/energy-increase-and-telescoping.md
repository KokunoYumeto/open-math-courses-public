# Energy increase and telescoping

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem A of [Dyadic triangles and the main estimate](dyadic-triangles-and-the-main-estimate.md). For a step function input, each admissible triple \(\mathbf I\) carries an energy \(e(\mathbf I)\), a sum of three values of \(\Phi(P)=\operatorname{tr}(P^{3/2})\). Splitting \(\mathbf I\) into its four children raises the average energy by at least a fixed multiple of \(|\tau(\mathbf I)|\) (Proposition 3.1), and with the weights \(2^{2k}\) the increases telescope across the scales while the total energy at every scale is at most \(2\sqrt2\) times the sum of the cubed \(L^3\) norms (Lemma 3.2). This is OpenAI's argument [OpenAI-D, Sections 4 and 5]; energy arguments of this kind go back to Kovač's Bellman function method for paraproducts [K1], [K2].

Notation is that of the first lesson (atoms of level \(m\), the spaces \(H_v\), the maps \(W_v\), \(D_v\) and \(\tau(\mathbf I)\), the children \(\operatorname{ch}(\mathbf I)\)) and of [A matrix energy and a trace inequality](a-matrix-energy-and-a-trace-inequality.md) (\(\Phi\), \(b_P\), row stars \(R_v\), \(T_v=R_v^{\mathsf T}R_v\)). Throughout, \(F_0,F_1,F_2\) are bounded step functions with bounded support, constant on products of atoms of level \(m\).

## 1. The energy of an admissible triple

For \(\mathbf I\in\mathcal A_k\), \(k\ge m\), with the maps \(W_v\) of Section 1 of the first lesson and their row stars \(R_v\), put
\[
\begin{aligned}
e_v(\mathbf I)&=\Phi(R_vR_v^{\mathsf T})=\Phi(T_v),\\
e(\mathbf I)&=\sum_{v=0}^2e_v(\mathbf I).
\end{aligned}
\]

**Proposition 3.1** (local energy increase). For \(\mathbf I\in\mathcal A_k\) with \(k\ge m+1\), the number
\[
\delta(\mathbf I)=\frac14\sum_{\mathbf I'\in\operatorname{ch}(\mathbf I)}e(\mathbf I')-e(\mathbf I)
\]
is nonnegative, and
\[
|\tau(\mathbf I)|\le\frac{10\sqrt2}3\,\delta(\mathbf I).
\]

*Proof.* Keep the spaces \(H_v\) of \(\mathbf I\), and view the spaces of a child, spanned by the atoms of the chosen halves, as subspaces. For a sign \(s_v=\pm1\) put
\[
C_v=(I+s_vD_v)^{1/2},
\]
which is \(\sqrt2\) times the orthogonal projection onto the atoms of the half of \(I_v\) chosen by \(s_v\) (the diagonal of \(I+s_vD_v\) has the entries \(2\) and \(0\)). In a child the weight of an atom doubles, from \(w\) to \(2w\), so its matrix for \(F_v\), extended by zero, is \(C_vW_vC_{v+1}\), and its row star is \(R_v(s)=C_vR_v\operatorname{diag}(C_{v+1},C_{v-1})\). Hence
\[
\begin{aligned}
&R_v(s)R_v(s)^{\mathsf T}\\
&\quad=C_v\bigl(W_vC_{v+1}^2W_v^{\mathsf T}\\
&\qquad+W_{v-1}^{\mathsf T}C_{v-1}^2W_{v-1}\bigr)C_v .
\end{aligned}
\]
Choose a child uniformly at random. Conditionally on \(s_v\), the signs \(s_{v+1}\) and \(s_{v-1}\) are each \(\pm1\) with probability \(\frac12\) (Lemma 1.2), so \(C_{v\pm1}^2=I+s_{v\pm1}D_{v\pm1}\) has conditional expectation \(I\). The displayed matrix contains no product of the two multipliers \(C_{v+1}^2\) and \(C_{v-1}^2\), although \(s_{v+1}\) and \(s_{v-1}\) are not independent, so
\[
\mathbb E\bigl[R_v(s)R_v(s)^{\mathsf T}\bigm|s_v\bigr]=C_vR_vR_v^{\mathsf T}C_v .
\]
By the convexity of \(\Phi\) (Lemma 2.1) and Jensen's inequality for the two equally likely children,
\[
\begin{aligned}
\mathbb E\bigl[e_v(\mathbf I(s))\bigm|s_v\bigr]&\ge\Phi(C_vR_vR_v^{\mathsf T}C_v)\\
&=\Phi(T_v+s_vU_v),
\end{aligned}
\]
with \(U_v=R_v^{\mathsf T}D_vR_v\). The equality holds because the Gram matrices \((C_vR_v)(C_vR_v)^{\mathsf T}\) and \((C_vR_v)^{\mathsf T}(C_vR_v)=R_v^{\mathsf T}(I+s_vD_v)R_v\) have the same nonzero eigenvalues. Since \(\|D_v\|\le1\), \(-T_v\le U_v\le T_v\). Averaging over \(s_v=\pm1\) and applying Corollary 2.4,
\[
\frac14\sum_{\mathbf I'\in\operatorname{ch}(\mathbf I)}e_v(\mathbf I')-e_v(\mathbf I)\ge\frac{b_{T_v}(U_v)}{2\sqrt2}.
\]
Summing over \(v\) gives \(\delta(\mathbf I)\ge0\), and Proposition 2.5 gives
\[
\begin{aligned}
|\tau(\mathbf I)|&\le\frac53\sum_vb_{T_v}(U_v)\\
&\le\frac{10\sqrt2}3\,\delta(\mathbf I).
\end{aligned}
\]
\(\square\)

## 2. Total energy and telescoping

**Lemma 3.2.** For \(k\ge m\) put \(J_k=\sum_{\mathbf I\in\mathcal A_k}2^{2k}e(\mathbf I)\). Then
\[
0\le J_k\le2\sqrt2\sum_{v=0}^2\|F_v\|_3^3,
\]
and for \(k\ge m+1\)
\[
\sum_{\mathbf I\in\mathcal A_k}2^{2k}\delta(\mathbf I)=J_{k-1}-J_k .
\]

*Proof.* Let \(\alpha\) and \(\beta\) be the Hilbert–Schmidt norms of the two blocks of \(R_v\). By Exercise 2.2 of the previous lesson and the power mean inequality,
\[
\begin{aligned}
e_v(\mathbf I)&\le(\operatorname{tr}T_v)^{3/2}=(\alpha^2+\beta^2)^{3/2}\\
&\le\sqrt2(\alpha^3+\beta^3).
\end{aligned}
\]
For each block, \(\|W_v\|_{\rm HS}^2=\sum_{i,j}w^2F_v(i,j)^2\) is the mean of \(F_v^2\) over \(I_v\times I_{v+1}\), so by Hölder's inequality
\[
\|W_v\|_{\rm HS}^3\le\frac1{|I_v||I_{v+1}|}\int_{I_v\times I_{v+1}}|F_v|^3 .
\]
Every block occurs in two row stars, and every pair \((I_v,I_{v+1})\in\mathcal D_k^2\) lies in exactly one admissible triple; as \(2^{2k}=|I_v||I_{v+1}|\), summation gives \(J_k\le2\sqrt2\sum_v\|F_v\|_3^3\). The sums are finite, since only finitely many blocks are nonzero.

By Lemma 1.2(2), every admissible triple of scale \(k-1\) is a child of exactly one admissible triple of scale \(k\), and \(2^{2k}/4=2^{2(k-1)}\). So the child terms of \(\sum_{\mathbf I\in\mathcal A_k}2^{2k}\delta(\mathbf I)\) add up to \(J_{k-1}\). \(\square\)

## 3. Proof of Theorem A

By Lemma 1.4 of the first lesson, it suffices to prove the inequality for bounded step functions with bounded support, constant on products of atoms of a level \(m\le\min S-1\). The case \(S=\varnothing\) is trivial. Otherwise let \(k_-=\min S\) and \(k_+=\max S\). By Lemma 1.1, Proposition 3.1 and Lemma 3.2, and because every \(\delta(\mathbf I)\) is nonnegative, so that the scales between \(k_-\) and \(k_+\) not in \(S\) may be added,
\[
\begin{aligned}
&\sum_{k\in S}\sum_{\mathbf I\in\mathcal A_k}|L_{\mathbf I}|=\sum_{k\in S}\sum_{\mathbf I\in\mathcal A_k}2^{2k}|\tau(\mathbf I)|\\
&\quad\le\frac{10\sqrt2}3\sum_{k=k_-}^{k_+}(J_{k-1}-J_k)\\
&\quad\le\frac{10\sqrt2}3J_{k_--1}\le\frac{40}3\sum_{v=0}^2\|F_v\|_3^3 .
\end{aligned}
\]
If some \(F_v\) is \(0\) in \(L^3\), every local form vanishes. Otherwise apply this to \(F_v/\|F_v\|_3\): each local form is trilinear, and the right side becomes \(\frac{40}3\cdot3=40\). This proves Theorem A. \(\square\)

The proof never used the coefficients \(\epsilon_k\) or the signs of the local forms, which is why the bound holds for the sum of absolute values. Lemma 1.3 of the first lesson gives the much weaker bound \(|S|\prod_v\|F_v\|_3\); the telescoping of the energies removes the factor \(|S|\).

## 4. Exercises

**3.1** (easy). Deduce from Proposition 3.1 and Lemma 3.2 that \(J_k\le J_{k-1}\) for \(k\ge m+1\), so that the weighted energies increase towards finer scales and stay below \(2\sqrt2\sum_v\|F_v\|_3^3\).

**3.2** (easy). For \(F_0=F_1=F_2=\mathbf 1_{[0,1)^2}\), \(m=0\) and \(k=0\), compute \(e(\mathbf I)\) for \(\mathbf I=([0,1),[0,1),[0,1))\), and check \(J_0\le2\sqrt2\sum_v\|F_v\|_3^3\).

**3.3** (medium). Show that the matrix \(C_v=(I+s_vD_v)^{1/2}\) used in Proposition 3.1 satisfies \(C_v^2=I+s_vD_v\), \(\frac12(C_v^2|_{s_v=1}+C_v^2|_{s_v=-1})=I\), and that \(C_vW_vC_{v+1}\) is the matrix of \(F_v\) for the child, with the child's atom weights \(2w\).

**3.4** (medium). Show that \(|L_{\mathbf I}|\le\frac{10\sqrt2}3\,2^{2k}\delta(\mathbf I)\) for every \(k\ge m+1\) and \(\mathbf I\in\mathcal A_k\), and deduce that \(\sum_{k=m+1}^K\sum_{\mathbf I\in\mathcal A_k}|L_{\mathbf I}|\le\frac{10\sqrt2}3J_m\) for every \(K\ge m+1\).

## 5. Solutions

**3.1.** By Lemma 3.2, \(J_{k-1}-J_k=\sum_{\mathbf I\in\mathcal A_k}2^{2k}\delta(\mathbf I)\), a sum of nonnegative terms by Proposition 3.1. So \(J_k\le J_{k-1}\le\dots\le J_m\le2\sqrt2\sum_v\|F_v\|_3^3\).

**3.2.** Each \(H_v\) is one-dimensional and \(w=1\), so \(W_v=(1)\), \(R_v=(1,1)\), \(T_v\) has the single positive eigenvalue \(2\), and \(e_v(\mathbf I)=2^{3/2}\). So \(e(\mathbf I)=3\cdot2^{3/2}=6\sqrt2\). Every other admissible triple of scale \(0\) has the form \((0,a,a)\), \((a,0,a)\), \((a,a,0)\) or has three nonzero indices, with \(a\ne0\); each of its blocks involves an interval other than \([0,1)\) and vanishes. So \(J_0=6\sqrt2\), while \(2\sqrt2\sum_v\|F_v\|_3^3=6\sqrt2\): equality.

**3.3.** \(D_v\) is diagonal with entries \(\pm1\), so \(I+s_vD_v\) is diagonal with entries \(0\) and \(2\): \(2\) on the atoms where \(h_{I_v}=s_v\), that is, on the half chosen by \(s_v\). Its square root \(C_v\) has entries \(0\) and \(\sqrt2\), and the average of \(I+D_v\) and \(I-D_v\) is \(I\). For atoms \(i\), \(j\) in the chosen halves, \((C_vW_vC_{v+1})(i,j)=2wF_v(i,j)\), the child's entry \(\sqrt{2w\cdot2w}\,F_v(i,j)\); other entries vanish.

**3.4.** By Lemma 1.1 and Proposition 3.1, \(|L_{\mathbf I}|=2^{2k}|\tau(\mathbf I)|\le\frac{10\sqrt2}32^{2k}\delta(\mathbf I)\). Summing over \(\mathbf I\in\mathcal A_k\) and over \(m+1\le k\le K\) and using Lemma 3.2, the sum telescopes to \(\frac{10\sqrt2}3(J_m-J_K)\le\frac{10\sqrt2}3J_m\).

## References

- [OpenAI-D] OpenAI, *An \(L^3\) bound for the dyadic triangular Hilbert form*, OpenAI Math Release preprint, 5 October 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026
- [K1] V. Kovač, *Bellman function technique for multilinear estimates and an application to generalized paraproducts*, Indiana University Mathematics Journal 60 (2011), 813–846; arXiv:1108.0917. https://arxiv.org/abs/1108.0917
- [K2] V. Kovač, *Boundedness of the twisted paraproduct*, Revista Matemática Iberoamericana 28 (2012), 1143–1164; arXiv:1011.6140. https://arxiv.org/abs/1011.6140

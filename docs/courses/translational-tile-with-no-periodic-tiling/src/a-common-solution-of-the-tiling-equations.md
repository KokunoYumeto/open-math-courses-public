# A common solution of the tiling equations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs one graph that satisfies all the tiling equations of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) and [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) at once [OpenAI-PT, Section 5]. In every ordinary channel \(i\) the useful output at \(x\) depends on exactly one input digit, the digit labelled by the symbol \(f(L_i(x))\) of the last-nonzero-digit model. The high coordinates record positions inside labelled blocks and move them along as \(x_1\) changes; this absorbs the shifts of the activation tiles. A labelling of the residue set \(S\) lets the two seed equations share the single coordinate \(z\). With Proposition 5.1 of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md), this proves that the system has a common solution but no fully periodic one.

- Labelled blocks (Section 1).
- The block inverse (Section 2).
- The ordinary channels (Section 3).
- Seed regions and one common output (Section 4).
- The seed equations (Section 5).
- All equations at once (Section 6).

We keep the notation of the two lessons named above, in particular the primes \(a_i,b_i,r_{ij}\) with \(r_{ij}=\kappa_{ij}a_i+\lambda_{ij}b_i\), \(\kappa_{ij},\lambda_{ij}\ge0\) (Lemma 1.1 of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md)), the shift list \(e_\delta\), \(\delta\in\Delta_i\), with its fibre orderings (1.1), the offsets of the activation tiles with the congruences (2.1) and (2.2), and the fibre criterion, Lemma 3.1 of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md). The function \(f\) and the line maps \(L_n\) are those of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md).

## 1. Labelled blocks

Fix a channel \(i\) and a label \(j\in J_i\). Partition \(\mathbb Z/r_{ij}\mathbb Z\) into \(\kappa_{ij}\) subsets of size \(a_i\) and \(\lambda_{ij}\) subsets of size \(b_i\), and label the elements of each subset of size \(d\) bijectively by \(\mathbb Z/d\mathbb Z\). A *block* of \(K_i\) for the label \(j\) is a set of elements of \(K_i\) whose digits other than the \(j\)-th are fixed and whose \(j\)-th digit runs through one of these subsets; the *label* of an element of the block is the label of its \(j\)-th digit. The blocks form a partition \(\mathcal B_{i,j}\) of \(K_i\). Blocks are subsets, not subgroups, and labels need not respect addition in \(K_i\).

Define \(C_{i,j}\colon K_i\to P_i\) and, for \(t\in\mathbb Z\), a map \(T_{i,j}(t)\colon K_i\to K_i\) as follows. If \(k\) has the label \(y\) in a block of size \(d\), then
\[
C_{i,j}(k)=\begin{cases}(y,0),&d=a_i,\\ (0,y),&d=b_i,\end{cases}
\]
and \(T_{i,j}(t)k\) is the element of the same block with the label \(y+t\), computed in \(\mathbb Z/d\mathbb Z\).

**Lemma 1.1** (blocks; [OpenAI-PT, Section 5.1]).

1. Each \(T_{i,j}(t)\) is a permutation of \(K_i\) that maps every block onto itself, \(T_{i,j}(t)T_{i,j}(t')=T_{i,j}(t+t')\), and on a block of size \(d\) the map \(T_{i,j}(t)\) depends only on \(t\bmod d\).
2. The function \(C_{i,j}\) has exactly one active label, namely \(j\).

*Proof.* (1) Within a block, \(T_{i,j}(t)\) adds \(t\) to the label, which is a bijection of \(\mathbb Z/d\mathbb Z\). (2) If \(w-w'\in U_{ij'}\) with \(j'\ne j\), then \(w\) and \(w'\) have the same \(j\)-th digit, so their blocks come from the same subset of \(\mathbb Z/r_{ij}\mathbb Z\) and their labels agree; hence \(C_{i,j}(w)=C_{i,j}(w')\). On the other hand, a block has at least two elements, and its elements with labels \(0\) and \(1\) differ only in the \(j\)-th digit and have different values of \(C_{i,j}\). \(\square\)

## 2. The block inverse

The fibre orderings of the shift list exist for the following calculation.

**Lemma 2.1** (block inverse; [OpenAI-PT, Lemma 5.1]). Fix \(i\), \(j\in J_i\), an integer \(x_1\) and \(k_i\in K_i\). For each \((l,\delta)\in K_i\times\Delta_i\) let \(h_1(l,\delta)\) be an integer with
\[
\begin{aligned}
h_1(l,\delta)&\equiv l&&(\mathrm{mod}\ r_i),\\
h_1(l,\delta)&\equiv\rho^a(\delta)&&(\mathrm{mod}\ a_i),\\
h_1(l,\delta)&\equiv\rho^b(\delta)&&(\mathrm{mod}\ b_i).
\end{aligned}
\]
Then the map
\[
\begin{aligned}(l,\delta)\mapsto\Bigl(&C_{i,j}(k_i-l)+e_\delta,\\&T_{i,j}(t)(k_i-l)\Bigr),\end{aligned}\tag{2.1}
\]
where \(t=x_1-h_1(l,\delta)\), is a bijection from \(K_i\times\Delta_i\) onto \(P_i\times K_i\).

*Proof.* Fix a target \(\bigl((\alpha^*,\xi^*),\beta^*\bigr)\in P_i\times K_i\). The element \(\beta^*\) lies in one block \(B\), with some label \(q\). Since \(T_{i,j}(t)\) preserves blocks, a preimage \((l,\delta)\) must have its *starting element* \(k'=k_i-l\) in \(B\); let \(y\) be the label of \(k'\).

*If \(B\) has size \(a_i\):* the first entry of (2.1) is \((y+e^a_\delta,\,e^b_\delta)\), and the second entry has the label \(y+x_1-h_1\equiv y+x_1-\rho^a(\delta)\pmod{a_i}\). So \((l,\delta)\) is a preimage exactly when
\[
\begin{gathered}e^b_\delta=\xi^*,\qquad y=\alpha^*-e^a_\delta,\\ y+x_1-\rho^a(\delta)=q,\end{gathered}
\]
that is, exactly when
\[
\begin{gathered}e^b_\delta=\xi^*,\\ e^a_\delta+\rho^a(\delta)=\alpha^*+x_1-q,\\ y=\alpha^*-e^a_\delta .\end{gathered}
\]
By the first fibre ordering in (1.1) of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md), exactly one \(\delta\) satisfies the first two equations. The third then fixes \(y\), hence \(k'\) as the element of \(B\) with label \(y\), and \(l=k_i-k'\). So the target has exactly one preimage.

*If \(B\) has size \(b_i\):* the first entry is \((e^a_\delta,\,y+e^b_\delta)\) and the label of the second is \(y+x_1-\rho^b(\delta)\) modulo \(b_i\). The conditions become \(e^a_\delta=\alpha^*\), \(e^b_\delta+\rho^b(\delta)=\xi^*+x_1-q\) and \(y=\xi^*-e^b_\delta\), and the second fibre ordering gives exactly one \(\delta\); then \(y\), \(k'\) and \(l\) follow. \(\square\)

## 3. The ordinary channels

For an ordinary channel \(i\) and \(x\in\mathbb Z^2\) put \(j_i(x)=f(L_i(x))\in\Sigma=J_i\), and define
\[
\begin{aligned}
c_i(x,k)&=C_{i,j_i(x)}(k_i),\\
\beta_i(x,k)&=T_{i,j_i(x)}(x_1)\,k_i .
\end{aligned}\tag{3.1}
\]

**Proposition 3.1** (ordinary channels; [OpenAI-PT, Section 5.1]). Let \(A\) be a graph whose ordinary outputs are given by (3.1), with arbitrary seed outputs and arbitrary \(z\). Then, for every ordinary channel \(i\):

1. \(c_i\) satisfies the dependence condition (3.1) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), and \(\mathcal A_i(x)=\{f(L_i(x))\}\) for every \(x\);
2. \(A\oplus F_i^{\rm act}=G\).

*Proof.* (1) The output depends only on \(L_i(x)\) and \(k_i\), and its active set is \(\{j_i(x)\}\) by Lemma 1.1(2). (2) Fix a target base \((x,k)\) and a batch \((l,\delta)\) of \(F_i^{\rm act}\) with offset \(h\in\mathbb Zu_i\). The starting base has \(L_i(x')=L_i(x)\), so \(j_i(x')=j_i(x)=:j\), and
\[
\begin{aligned}c_i(x',k')&=C_{i,j}(k_i-l),\\ \beta_i(x',k')&=T_{i,j}(x_1-h_1)(k_i-l).\end{aligned}
\]
So the tuple (3.2) of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) is the map (2.1), with \(h_1(l,\delta)\) the first coordinate of the offset, which satisfies the congruences (2.1) of that lesson. By Lemma 2.1 it is a bijection, and the fibre criterion gives the tiling equation. The \(z\)-offsets of ordinary batches vary freely, so the equation does not involve \(z\). \(\square\)

## 4. Seed regions and one common output

Choose disjoint subsets \(S_{\eta_1},S_{\eta_2}\subseteq S\) with
\[
\#S_{\eta_1}=3,\qquad\#S_{\eta_2}=4,
\]
such that every \(s=(s_1,s_2)\in S_{\eta_t}\) has \(s_1\equiv0\) and \(s_2\equiv t\pmod p\). Each of these two residue classes has \(p^2\) elements of \(S\), so the choice is possible. Put \(S_0=S\setminus(S_{\eta_1}\cup S_{\eta_2})\). Since \(p\) is a prime larger than \(3\), \(p^2\equiv1\) modulo \(2\) and modulo \(3\), so \(D=p^4\equiv1\pmod6\) and \(\#S_0=D-7\) is divisible by \(6\). Recall \(a_{\eta_1}=2\) and \(a_{\eta_2}=3\).

Divide each region into *label spaces*, subsets equipped with a bijection to a group of labels, as follows.

- \(S_{\eta_1}\) is one copy of \(\mathbb Z/3\mathbb Z\); its label is called \(y_{\eta_2}\).
- \(S_{\eta_2}\) is the union of two copies of \(\mathbb Z/2\mathbb Z\); the label is called \(y_{\eta_1}\).
- \(S_0\) is the union of \((D-7)/6\) copies of \(\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\); the labels are \((y_{\eta_1},y_{\eta_2})\).

So the seed \(\eta_t\) has a label \(y_{\eta_t}(s)\in\mathbb Z/a_{\eta_t}\mathbb Z\) exactly at the points \(s\notin S_{\eta_t}\), and a point of \(S\) is determined by its region, its copy of the label space and its labels. For \(t\in\mathbb Z\), let \(R(t)\) be the permutation of \(S\) that keeps every copy of every label space and adds \(t\) to each of its labels. It preserves the three regions, and \(R(t)R(t')=R(t+t')\). Fix any bijection \(\psi\colon S\to\mathbb Z/D\mathbb Z\) and put
\[
z(x,k)=\psi\bigl(R(x_1)\,s(x)\bigr).\tag{4.1}
\]
Neither \(\psi\) nor \(R(t)\) is required to respect addition; \(S\) only indexes the values of the one cyclic coordinate \(\mathbb Z/D\mathbb Z\).

**Definition 4.1** (seed outputs). For a seed \(i\) the label set is \(\{*\}\); write \(C_i=C_{i,*}\) and \(T_i=T_{i,*}\). If \(s(x)\in S_i\), put \(c_i(x,k)=C_i(k_i)\) and \(\beta_i(x,k)=T_i(x_1)k_i\). If \(s(x)\notin S_i\), put \(c_i(x,k)=\bigl(y_i(s(x)),0\bigr)\) and \(\beta_i(x,k)=k_i\).

The useful output depends only on \(s(x)\) and \(k_i\), as the dependence condition requires. The label \(*\) is active at \(x\) exactly when \(s(x)\in S_i\), by Lemma 1.1(2) in the first case, and because the output does not depend on \(k_i\) in the second.

## 5. The seed equations

**Proposition 5.1** (seed equations; [OpenAI-PT, Section 5.3]). Let \(A\) be a graph whose seed outputs are given by Definition 4.1 and whose \(z\) is given by (4.1). Then \(A\oplus F_i^{\rm act}=G\) for both seeds \(i\).

*Proof.* Fix a seed \(i\), the other seed \(i'\), and a target base \((x,k)\). A batch \((l,\delta,\tau)\) has an offset \(h\) whose first coordinate satisfies
\[
\begin{aligned}
h_1&\equiv l&&(\mathrm{mod}\ r_i),\\
h_1&\equiv\rho^a(\delta)&&(\mathrm{mod}\ a_i),\\
h_1&\equiv\rho^b(\delta)&&(\mathrm{mod}\ b_i),\\
h_1&\equiv0&&(\mathrm{mod}\ a_{i'}),
\end{aligned}
\]
and \(s(h)=\tau\). Its starting base has \(x'=x-h\), \(s'=s(x')=s(x)-\tau\) and \(k'_i=k_i-l\). By Lemma 3.1 of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) we must show that every target
\[
(c^*,\beta^*,z^*)\in P_i\times K_i\times\mathbb Z/D\mathbb Z,
\]
with \(c^*=(\alpha^*,\xi^*)\), is the tuple (3.3) of exactly one batch. Put \(s''=\psi^{-1}(z^*)\). The \(z\)-entry of the tuple is \(z^*\) exactly when \(R(x'_1)s'=s''\), which requires \(s'\) to lie in the same region and the same copy of its label space as \(s''\).

*Case \(s''\in S_i\).* Then \(s'\in S_i\), where the only label is \(y_{i'}\in\mathbb Z/a_{i'}\mathbb Z\). Since \(h_1\equiv0\pmod{a_{i'}}\), the condition \(R(x'_1)s'=s''\) says \(y_{i'}(s'')=y_{i'}(s')+x_1\), that is \(s'=R(-x_1)s''\). So \(s'\), and with it \(\tau=s(x)-s'\), is determined by the target, and for this \(\tau\) every batch \((l,\delta,\tau)\) has the right \(z\)-entry. Since \(s'\in S_i\), the first two entries of the tuple of such a batch are
\[
\begin{gathered}C_i(k_i-l)+e_\delta\quad\text{and}\\ T_i(x_1-h_1)(k_i-l).\end{gathered}
\]
By Lemma 2.1, applied to the first coordinates of the offsets \(h^{(i)}_{l,\delta,\tau}\) for this fixed \(\tau\), which satisfy the congruences of that lemma, exactly one \((l,\delta)\) gives \((c^*,\beta^*)\).

*Case \(s''\notin S_i\).* Then \(s'\notin S_i\), so the starting base has \(c_i=(y_i(s'),0)\) and \(\beta_i=k'_i\). The tuple equals the target exactly when
\[
\begin{gathered}
k_i-l=\beta^*,\qquad e^b_\delta=\xi^*,\\ y_i(s')+e^a_\delta=\alpha^*,\\
R(x_1-h_1)\,s'=s'' .
\end{gathered}
\]
In the last condition the label \(y_i\) changes by \(x_1-h_1\equiv x_1-\rho^a(\delta)\pmod{a_i}\), and the label \(y_{i'}\), if the region has one, by \(x_1-h_1\equiv x_1\pmod{a_{i'}}\). So the conditions say:
\[
\begin{gathered}
l=k_i-\beta^*,\qquad e^b_\delta=\xi^*,\\
e^a_\delta+\rho^a(\delta)=\alpha^*+x_1-y_i(s''),\\
y_i(s')=\alpha^*-e^a_\delta,\\ y_{i'}(s')=y_{i'}(s'')-x_1,
\end{gathered}
\]
the last one only when \(s''\in S_0\), and \(s'\) is in the copy of \(s''\). The first fibre ordering gives exactly one \(\delta\) with the second and third conditions. Then the labels of \(s'\) are determined, so \(s'\) is determined in its copy, and \(\tau=s(x)-s'\). So exactly one batch \((l,\delta,\tau)\) satisfies all conditions, and since the conditions are equivalent to the equality of the tuple with the target, it represents the target. \(\square\)

On \(S_0\) both labels are recovered: the label \(y_i\) through the fibre ordering, which also selects \(\delta\), and the label \(y_{i'}\) directly from the congruence \(h_1\equiv0\pmod{a_{i'}}\). Exchanging \(i\) and \(i'\) gives the other seed equation with the same function \(z\); the two equations have their own representing batches, which need not coincide. The verification uses only the residues of \(h_1\) modulo \(r_i\), \(a_i\), \(b_i\) and \(a_{i'}\) and the residue \(s(h)=\tau\), so every admissible choice of the offsets works, and \(x_1\) may be any integer.

## 6. All equations at once

**Theorem 6.1** (a common solution; [OpenAI-PT, Section 5.4]). The graph \(A\subseteq G\) with the ordinary outputs (3.1), the seed outputs of Definition 4.1 and the function \(z\) of (4.1) is a common solution of the whole system of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md).

*Proof.* By Lemma 2.2(1) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), the functions \(c_i\), \(\beta_i\) and \(z\) define a graph, so the graph equation holds. The dependence conditions hold by Proposition 3.1(1) and the remark after Definition 4.1; by Corollary 3.2 of that lesson the dependence tiles are tiled. The activation tiles are tiled by Propositions 3.1(2) and 5.1. For the cycle tiles we check (4.2) and (4.3) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md). At every \(x\), \(\mathcal A_n(x)=\{f(L_n(x))\}\), so the only word in \(\prod_n\mathcal A_n(x)\) is \(n\mapsto f(L_n(x))\), which is allowed by Lemma 5.2(2) of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md). If the seed \(\eta_t\) is active at \(x\), then \(s(x)\in S_{\eta_t}\), so \(x_1\equiv0\) and \(x_2\equiv t\pmod p\), and Lemma 5.2(3) of that lesson gives \(f(L_n(x))=t\) for every \(n\); so \(\mathcal A_n(x)=\{t\}\). By Lemma 4.1 of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), all cycle tiles are tiled. \(\square\)

**Theorem 6.2** (OpenAI [OpenAI-PT, Theorem 5.2]). There are a finite cyclic group \(V\) and finitely many finite nonempty sets \(F_1,\ldots,F_s\subseteq G=\mathbb Z^2\times V\) such that the system \(A\oplus F_\nu=G\), \(1\le\nu\le s\), has a common solution, but no common solution is invariant under a subgroup of finite index of \(G\).

*Proof.* Take the system of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md): its group \(V\) is cyclic by Lemma 1.2 of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), it has a common solution by Theorem 6.1, and no fully periodic common solution by Proposition 5.1 of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md). \(\square\)

Every tile of the system has \(\#H_0\) elements; this is used when the system is stacked into one tile in [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md).

## 7. Exercises

**7.1.** Show that if blocks of both sizes \(a_i\) and \(b_i\) occur in \(\mathcal B_{i,j}\), then \(T_{i,j}(t)\) is the identity exactly when \(a_ib_i\mid t\).

**7.2.** For \(p=211\), compute the number of copies of \(\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\) in \(S_0\).

**7.3.** Suppose the seed outputs in the second case of Definition 4.1 were replaced by the constant \((0,0)\), keeping \(\beta_i=k_i\). Show that the seed equation of \(i\) fails.

**7.4.** Show directly that the model array \(W(n,m)=f(m)\) has no positive vertical period.

**7.5.** In the common solution of Theorem 6.1, determine the set of points \(x\in\mathbb Z^2\) where the seed \(\eta_1\) is active, and show that it is invariant under \(p^2\mathbb Z^2\) but meets only \(3\) of the \(p^4\) residue classes modulo \(p^2\).

## 8. Solutions

**7.1.** On a block of size \(d\), \(T_{i,j}(t)\) adds \(t\) to the label in \(\mathbb Z/d\mathbb Z\), so it is the identity there exactly when \(d\mid t\). If both sizes occur, \(T_{i,j}(t)\) is the identity exactly when \(a_i\mid t\) and \(b_i\mid t\), that is, \(a_ib_i\mid t\), since \(a_i\) and \(b_i\) are distinct primes.

**7.2.** \(p^2=44521\) and \(D=p^4=44521^2=1982119441\). Then \(D-7=1982119434\), and \((D-7)/6=330353239\).

**7.3.** In the case \(s''\notin S_i\), a batch represents the target only if \(e_\delta=c^*\), because the output at the starting base is \((0,0)\). For \(c^*=(1,0)\) no \(\delta\) has \(e_\delta=c^*\), since \(\mu_i(1,0)=0\). So targets with \(c^*=(1,0)\) and \(\psi^{-1}(z^*)\notin S_i\) are not covered. The label \(y_i\) is what absorbs the nonuniform multiplicity.

**7.4.** Suppose \(f(m+M)=f(m)\) for all \(m\), with \(M\ge1\). Then \(f(kM)=f(0)=1\) for every integer \(k\). Write \(M=p^rM'\) with \(p\nmid M'\). For \(k=1\) and \(k=2\), which are not divisible by \(p\), \(f(kM)=f(kM')=kM'\bmod p\). So \(M'\equiv1\) and \(2M'\equiv1\pmod p\), which gives \(2\equiv1\pmod p\), a contradiction.

**7.5.** The seed \(\eta_1\) is active at \(x\) exactly when \(s(x)\in S_{\eta_1}\), by the remark after Definition 4.1. This condition depends only on \(x\bmod p^2\), so the set is invariant under \(p^2\mathbb Z^2\), and it is the union of the \(3\) residue classes in \(S_{\eta_1}\).

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026

# Forcing activity and excluding periodicity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The tiling equations of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) restrict which labels can be active together, but they allow no label to be active at all. This lesson adds one tile for each channel [OpenAI-PT, Section 4]. Its equation forces every ordinary channel to have an active label at every point and each seed to be active somewhere. The mechanism is a list of output shifts with *nonuniform* multiplicities: an output that does not depend on its digits cannot absorb these shifts evenly. The list has uniform counts in each coordinate, which the lesson [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md) uses to build a solution. With the activity forced, every common solution carries an array that satisfies the line rule and has no constant column, and a fully periodic common solution would give such an array with a vertical period. This contradicts Proposition 4.1 of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md).

- A shift list with two fibre orderings (Section 1).
- The activation tiles (Section 2).
- Exact coverage in a fibre (Section 3).
- Every required channel is active (Section 4).
- No fully periodic common solution (Section 5).

We keep all notation of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md): the channels \(i\in\mathcal I\), the primes \(a_i,b_i,r_{ij}\), the groups \(P_i=\mathbb Z/a_i\mathbb Z\times\mathbb Z/b_i\mathbb Z\), \(K_i\), the set \(S=(\mathbb Z/p^2\mathbb Z)^2\) with \(D=p^4\) elements, the group \(G=\mathbb Z^2\times V\), the kernel \(H_0\), graphs \(A\) with their functions \(c_i\), \(\beta_i\), \(z\), the dependence conditions (3.1), the active labels \(\mathcal A_i(x)\), and the consequences (4.2) and (4.3) of the cycle tests. From the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) we use the Chinese remainder theorem (Judson, [Theorem 16.5.3](https://judsonbooks.org/aata-files/aata-html/rings-section-software-application.html)) and that the order of an element of a finite group divides the order of the group ([Corollary 6.2.3](https://judsonbooks.org/aata-files/aata-html/cosets-section-lagranges-theorem.html)).

## 1. A shift list with two fibre orderings

Fix a channel \(i\). For \(e\in P_i\) let \(\mathbf 1_{\{e\}}\) be the indicator function of \(\{e\}\) on \(P_i\), and define integer-valued functions on \(P_i\) by
\[
\begin{aligned}\omega_i&=\mathbf 1_{\{(0,0)\}}-\mathbf 1_{\{(1,0)\}}\\&\quad-\mathbf 1_{\{(0,1)\}}+\mathbf 1_{\{(1,1)\}},\\ \mu_i&=1+\omega_i .\end{aligned}
\]

**Lemma 1.1** (the multiplicity \(\mu_i\); [OpenAI-PT, Section 4.1]). The function \(\mu_i\) takes the value \(2\) at \((0,0)\) and \((1,1)\), the value \(0\) at \((1,0)\) and \((0,1)\), and the value \(1\) elsewhere. It is nonnegative and not constant, its total mass is \(a_ib_i\), and its marginals are uniform:
\[
\begin{aligned}
\sum_{\alpha\in\mathbb Z/a_i\mathbb Z}\mu_i(\alpha,\xi)&=a_i\quad(\xi\in\mathbb Z/b_i\mathbb Z),\\
\sum_{\xi\in\mathbb Z/b_i\mathbb Z}\mu_i(\alpha,\xi)&=b_i\quad(\alpha\in\mathbb Z/a_i\mathbb Z).
\end{aligned}
\]

*Proof.* Since \(a_i,b_i\ge2\), the four points \((0,0)\), \((1,0)\), \((0,1)\), \((1,1)\) are distinct, which gives the values. In each row \(\xi\) and each column \(\alpha\), \(\omega_i\) is either identically zero or takes the values \(1\) and \(-1\) once each, so its marginals vanish and those of \(\mu_i\) are those of the constant \(1\). \(\square\)

Choose a set \(\Delta_i\) with \(a_ib_i\) elements and a list \(e_\delta=(e^a_\delta,e^b_\delta)\in P_i\), \(\delta\in\Delta_i\), in which each \(e\in P_i\) occurs exactly \(\mu_i(e)\) times. For each \(\xi\in\mathbb Z/b_i\mathbb Z\), the set \(\{\delta:e^b_\delta=\xi\}\) has \(a_i\) elements by Lemma 1.1; choose a bijection \(\pi^a_\xi\) from it to \(\mathbb Z/a_i\mathbb Z\) and put \(\rho^a(\delta)=\pi^a_\xi(\delta)-e^a_\delta\). Independently, for each \(\alpha\) the set \(\{\delta:e^a_\delta=\alpha\}\) has \(b_i\) elements; choose a bijection \(\pi^b_\alpha\) to \(\mathbb Z/b_i\mathbb Z\) and put \(\rho^b(\delta)=\pi^b_\alpha(\delta)-e^b_\delta\). Then both maps
\[
\begin{aligned}&\{\delta:e^b_\delta=\xi\}\to\mathbb Z/a_i\mathbb Z,\\&\qquad\delta\mapsto e^a_\delta+\rho^a(\delta),\\&\{\delta:e^a_\delta=\alpha\}\to\mathbb Z/b_i\mathbb Z,\\&\qquad\delta\mapsto e^b_\delta+\rho^b(\delta)\end{aligned}\tag{1.1}
\]
are bijections. These are the *fibre orderings* of the list. Repeated values \(e_\delta\) have distinct indices \(\delta\), and the orderings act on the indices. The notation \(\Delta_i\), \(e_\delta\), \(\rho^a\), \(\rho^b\) belongs to the channel \(i\).

## 2. The activation tiles

For a channel \(\ell\) let \(R_\ell=r_\ell\mathbb Z/r_\ell^2\mathbb Z\), the \(r_\ell\) elements of \(\mathbb Z/r_\ell^2\mathbb Z\) with residue \(0\) modulo \(r_\ell\). For \(h\in\mathbb Z^2\), \(e\in P_i\) and \(E\subseteq\mathbb Z/D\mathbb Z\) define the *batch* \(\mathcal B_i(h,e;E)\) as the set of all \(\bigl(h,\zeta,(w_\ell,d_\ell)_{\ell\in\mathcal I}\bigr)\in G\) with
\[
\begin{gathered}
\zeta\in E,\quad w_i=h_1\bmod r_i^2,\quad d_i=e,\\
w_\ell\in R_\ell,\ d_\ell\in P_\ell\ \ (\ell\ne i).
\end{gathered}
\]
It has \(\#E\cdot\prod_{\ell\ne i}r_\ell\#P_\ell\) elements, one for each choice of the freely varied coordinates.

*Ordinary channels.* Let \(i\in\{0,\ldots,N-1\}\). For each pair \((l,\delta)\in K_i\times\Delta_i\) choose \(h=h^{(i)}_{l,\delta}\in\mathbb Zu_i\), that is \(h=h_1(1,-i)\), with
\[
\begin{aligned}
h_1&\equiv l&&(\mathrm{mod}\ r_i),\\
h_1&\equiv\rho^a(\delta)&&(\mathrm{mod}\ a_i),\\
h_1&\equiv\rho^b(\delta)&&(\mathrm{mod}\ b_i).
\end{aligned}\tag{2.1}
\]
The moduli are pairwise coprime, so by the Chinese remainder theorem the solutions \(h_1\) form a residue class modulo \(r_ia_ib_i\); choose the values \(h_1\) for different pairs distinct. Put
\[
F_i^{\rm act}=\bigcup_{(l,\delta)\in K_i\times\Delta_i}\mathcal B_i\bigl(h^{(i)}_{l,\delta},e_\delta;\mathbb Z/D\mathbb Z\bigr).
\]
Since \(h\in\mathbb Zu_i=\ker L_i\), we have \(L_i(x-h)=L_i(x)\) for every \(x\).

*Seeds.* Let \(i\in\{\eta_1,\eta_2\}\) and let \(i'\) be the other seed. For each triple \((l,\delta,\tau)\in K_i\times\Delta_i\times S\), with \(\tau=(\tau_1,\tau_2)\), choose \(h=h^{(i)}_{l,\delta,\tau}\in\mathbb Z^2\) satisfying (2.1) and
\[
\begin{aligned}s(h)&=\tau,\\ h_1&\equiv0\ (\mathrm{mod}\ a_{i'}).\end{aligned}\tag{2.2}
\]
The first coordinate \(h_1\) is prescribed modulo the pairwise coprime numbers \(r_i\), \(a_i\), \(b_i\), \(p^2\) and \(a_{i'}\), and the second only needs \(h_2\equiv\tau_2\pmod{p^2}\). By the Chinese remainder theorem there are infinitely many choices; choose the offsets \(h\) for different triples distinct. Put
\[
F_i^{\rm act}=\bigcup_{(l,\delta,\tau)}\mathcal B_i\bigl(h^{(i)}_{l,\delta,\tau},e_\delta;\{0\}\bigr).
\]
So an ordinary batch lets the \(z\)-offset vary freely, while a seed batch has \(z\)-offset \(0\). The congruence modulo \(a_{i'}\) is used in [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md), where both seed equations hold with one common function \(z\).

Different batches of one tile have different horizontal coordinates, so these unions are disjoint, and the repeated entries of the list \(e_\delta\) do not produce repeated elements. Counting,
\[
\#F_i^{\rm act}=D\prod_{\ell\in\mathcal I}r_\ell\,\#P_\ell=\#H_0
\]
for every channel: an ordinary tile has \(r_ia_ib_i\) batches of \(D\prod_{\ell\ne i}r_\ell\#P_\ell\) elements, and a seed tile has \(Dr_ia_ib_i\) batches of \(\prod_{\ell\ne i}r_\ell\#P_\ell\) elements. The *system* of this course in \(G\) consists of the graph equation \(A\oplus H_0=G\), the dependence tiles, the cycle tiles of instances 1 and 2, and the activation tiles \(F_i^{\rm act}\), \(i\in\mathcal I\). It is a finite family of finite nonempty subsets of \(G\).

## 3. Exact coverage in a fibre

For a point \(y\in G\) with base \((x,k)\) and a channel \(i\), its *sheared coordinate* in channel \(i\) is the \(\beta\in K_i\) with \(v_i(y)=x_1+[k_i-x_1]_{r_i}+r_i\beta\) (Lemma 2.2 of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md)). For a target base \((x,k)\) and a batch with offset \(h\), indexed by \((l,\delta)\) or \((l,\delta,\tau)\), the *starting base* is \((x',k')\) with
\[
\begin{aligned}x'&=x-h,\\ k'_i&=k_i-l,\\ k'_\ell&=k_\ell\quad(\ell\ne i).\end{aligned}\tag{3.1}
\]

**Lemma 3.1** (activation fibre criterion; [OpenAI-PT, Lemma 4.1]). Let \(A\) be a graph.

(1) For an ordinary channel \(i\), \(A\oplus F_i^{\rm act}=G\) holds exactly when, at every target base \((x,k)\), the map
\[
\begin{aligned}(l,\delta)\longmapsto\bigl(&c_i(x',k')+e_\delta,\\&\beta_i(x',k')\bigr)\end{aligned}\tag{3.2}
\]
is a bijection from \(K_i\times\Delta_i\) onto \(P_i\times K_i\).

(2) For a seed \(i\), \(A\oplus F_i^{\rm act}=G\) holds exactly when, at every target base \((x,k)\), the map
\[
\begin{aligned}(l,\delta,\tau)\mapsto\bigl(&c_i(x',k')+e_\delta,\\&\beta_i(x',k'),\\&z(x',k')\bigr)\end{aligned}\tag{3.3}
\]
is a bijection from \(K_i\times\Delta_i\times S\) onto \(P_i\times K_i\times\mathbb Z/D\mathbb Z\).

*Proof.* Fix a point \(y\) with base \((x,k)\) and one batch, with offset \(h\) and index \((l,\delta)\) or \((l,\delta,\tau)\). All elements \(f\) of the batch have horizontal coordinate \(h\), low coordinate \(h_1\bmod r_i=l\) in channel \(i\) and low coordinate \(0\) in the other channels. So a representation \(y=a+f\) with \(f\) in the batch forces \(a\) to be the point of \(A\) above the starting base \((x',k')\), and then \(f=y-a\) is determined. This \(f\) has horizontal coordinate \(h\), and it lies in the batch exactly when:

- its \(\mathbb Z/r_i^2\mathbb Z\)-coordinate is \(h_1\bmod r_i^2\), that is \(v_i(y)=v_i(a)+h_1\). By Lemma 2.2(2) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), \(v_i(a)+h_1\) is the element with low coordinate \(k'_i+h_1=k_i\) and sheared coordinate \(\beta_i(x',k')\) over the base \((x,k)\), since \(x'+h=x\). So this condition says that the sheared coordinate of \(y\) in channel \(i\) is \(\beta_i(x',k')\);
- its \(P_i\)-coordinate is \(e_\delta\), that is \(c_i(y)=c_i(x',k')+e_\delta\);
- for a seed batch, its \(z\)-coordinate is \(0\), that is \(z(y)=z(x',k')\).

The other coordinates of \(f\) are automatically allowed: for \(\ell\ne i\), \(v_\ell(y)-v_\ell(a)\) has low coordinate \(k_\ell-k_\ell=0\), so it lies in \(R_\ell\), and the \(P_\ell\)-coordinate and, in an ordinary batch, the \(z\)-coordinate are arbitrary. So \(r_{A,F_i^{\rm act}}(y)\) is the number of batch indices whose tuple (3.2) or (3.3) equals the tuple of \(y\): its useful output, its sheared coordinate, and for a seed its \(z\)-coordinate. Every tuple occurs for some \(y\) above \((x,k)\), and different batches are different parts of the tile. So \(A\oplus F_i^{\rm act}=G\) exactly when every tuple has exactly one index. \(\square\)

In particular, exact coverage forces every value \(c\in P_i\) to be the first entry of the tuples of exactly \(r_i\) indices in the ordinary case, and of exactly \(Dr_i\) indices in the seed case. These necessary counts already force the activity.

## 4. Every required channel is active

**Lemma 4.1** (ordinary activation; [OpenAI-PT, Lemma 4.2]). In every common solution of the system, every ordinary channel has an active label at every \(x\in\mathbb Z^2\).

*Proof.* Suppose the ordinary channel \(i\) has no active label at \(x\). By Lemma 3.4 of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md), \(g_{i,x}\) is constant, say with value \(c_0\). Fix a target base \((x,k)\). Every starting base has \(L_i(x')=L_i(x)\), because \(h\in\ker L_i\), so by (3.1) of that lesson \(c_i(x',k')=g_{i,x}(k'_i)=c_0\). For each \(\delta\) there are \(r_i\) values of \(l\), so the number of indices \((l,\delta)\) whose tuple (3.2) has first entry \(c\) is
\[
r_i\cdot\#\{\delta:e_\delta=c-c_0\}=r_i\,\mu_i(c-c_0).
\]
Lemma 3.1 requires this to be \(r_i\) for every \(c\in P_i\), so \(\mu_i\) would be constant, contrary to Lemma 1.1. \(\square\)

**Lemma 4.2** (seed activation; [OpenAI-PT, Lemma 4.3]). In every common solution of the system, each seed \(i\) has its label \(*\) active at some point of \(\mathbb Z^2\).

*Proof.* Suppose the seed \(i\) is active nowhere. Then every \(g_{i,x}\) is constant, and by (3.1) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md) there is a function \(q\colon S\to P_i\) with \(c_i(x,k)=q(s(x))\) for all bases. Its histogram, defined for \(c\in P_i\) by
\[
Q(c)=\#\{s\in S:q(s)=c\},
\]
takes nonnegative integer values with total \(\sum_cQ(c)=D\). Fix a target base \((x,k)\) and \(\delta\). By (2.2), the starting data \((s(x'),k'_i)=(s(x)-\tau,\,k_i-l)\) run once through \(S\times K_i\) as \((\tau,l)\) varies. So the number of indices whose tuple (3.3) has first entry \(c\) is
\[
\sum_{\delta\in\Delta_i}r_i\,Q(c-e_\delta)=r_i\sum_{e\in P_i}\mu_i(e)\,Q(c-e).
\]
Lemma 3.1 requires this to be \(Dr_i\) for every \(c\). Since \(\sum_eQ(c-e)=D\) and \(\mu_i=1+\omega_i\), we get \(\sum_e\omega_i(e)Q(c-e)=0\), that is,
\[
\begin{aligned}&Q(\alpha,\xi)-Q(\alpha-1,\xi)\\&-Q(\alpha,\xi-1)\\&+Q(\alpha-1,\xi-1)=0\end{aligned}\tag{4.1}
\]
for all \((\alpha,\xi)\in P_i\). By (4.1), for each \(\alpha\) the difference \(Q(\alpha,\xi)-Q(\alpha-1,\xi)\) does not change when \(\xi\) is replaced by \(\xi-1\), so it does not depend on \(\xi\). Adding such differences along the first coordinate, for any \(\alpha_0\),
\[
\begin{aligned}&Q(\alpha,\xi)-Q(\alpha_0,\xi)\\&\quad=Q(\alpha,0)-Q(\alpha_0,0).\end{aligned}
\]
Choose \(\alpha_0\) with \(Q(\alpha_0,0)\) least, and put \(u(\alpha)=Q(\alpha,0)-Q(\alpha_0,0)\) and \(v(\xi)=Q(\alpha_0,\xi)\). Both take nonnegative integer values, \(Q(\alpha,\xi)=u(\alpha)+v(\xi)\), and summing over \(P_i\),
\[
D=b_i\sum_\alpha u(\alpha)+a_i\sum_\xi v(\xi).
\]
Since \(b_i>D\), the first sum is \(0\), and then \(a_i\) divides \(D=p^4\). But \(a_i\) is \(2\) or \(3\), and \(p>3\) is prime. \(\square\)

## 5. No fully periodic common solution

**Proposition 5.1** ([OpenAI-PT, Proposition 4.4]). No common solution of the system is invariant under a subgroup of finite index of \(G\).

*Proof.* Let \(A\) be a common solution. Order \(\Sigma\) by \(1<2<\cdots<p-1\) and define, for \(n\in I\) and \(m\in\mathbb Z\),
\[
W(n,m)=\min\mathcal A_n\bigl((0,m)\bigr),
\]
which exists by Lemma 4.1. Since \(\mathcal A_n(x)\) depends only on \(L_n(x)\), and \(L_n(0,m)=m\), the symbol \(\min\mathcal A_n(x)\) equals \(W(n,L_n(x))\) for every \(x\).

*The line rule.* Let \(d,e\in\mathbb Z\) and \(x=(d,e)\), so \(L_n(x)=dn+e\). The word \(n\mapsto W(n,dn+e)\) picks one active label in each ordinary channel at \(x\), so it is allowed by (4.2) of [Encoding symbols by tiling equations](encoding-symbols-by-tiling-equations.md).

*No constant column.* By Lemma 4.2, for \(t=1,2\) there is a point \(x^{(t)}\) where the seed \(\eta_t\) is active. By (4.3) of that lesson, \(\mathcal A_n(x^{(t)})\subseteq\{t\}\), and this set is nonempty, so it is \(\{t\}\). Hence
\[
\begin{gathered}W\bigl(n,L_n(x^{(1)})\bigr)=1,\\ W\bigl(n,L_n(x^{(2)})\bigr)=2\end{gathered}
\]
for every \(n\in I\), and every column of \(W\) takes two different values.

*A vertical period.* Suppose \(A+\Lambda=A\) with \([G:\Lambda]=M<\infty\). The element \(e_{\rm v}=\bigl((0,1),0_V\bigr)\in G\) satisfies \(Me_{\rm v}\in\Lambda\), because the order of \(e_{\rm v}+\Lambda\) in the finite group \(G/\Lambda\) divides \(M\). So
\[
A+\bigl((0,M),0_V\bigr)=A .
\]
This translation maps the point of \(A\) above \((x,k)\) to a point of \(A\) above \((x+(0,M),k)\), which is the point of \(A\) there, and keeps its useful outputs. So \(g_{i,x+(0,M)}=g_{i,x}\) and \(\mathcal A_n(x+(0,M))=\mathcal A_n(x)\) for all \(x\) and \(n\). At \(x=(0,m)\) this gives \(W(n,m+M)=W(n,m)\).

So \(W\) satisfies the line rule, has no constant column and has the positive vertical period \(M\), contrary to Proposition 4.1 of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md). \(\square\)

It remains to show that the system has a common solution at all; this is done in [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md).

## 6. Exercises

**6.1.** Let \(a_i=2\) and \(b_i=5\). Write down \(\mu_i\), a list \(e_\delta\) with \(10\) entries, and fibre orderings \(\rho^a,\rho^b\) satisfying (1.1).

**6.2.** Show that if the constant function \(1\) were used in place of \(\mu_i\), a graph whose channel-\(i\) output is constant and whose sheared coordinate is \(\beta_i(x,k)=k_i\) would satisfy the ordinary activation equation of channel \(i\). So the nonuniform multiplicity is what forces activity.

**6.3.** Let \(a=2\), \(b=3\) and \(D=5\) (so that \(b\le D\)). Find a nonnegative integer function \(Q\) on \(\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\) with total mass \(5\) that satisfies (4.1). Which step of the proof of Lemma 4.2 fails?

**6.4.** Show that Proposition 5.1 also follows from a period of the form \(\bigl((0,M),v_0\bigr)\) with an arbitrary \(v_0\in V\): show that such a period also preserves all active sets.

**6.5.** In the proof of Lemma 3.1, the batch fixes the \(\mathbb Z/r_i^2\mathbb Z\)-coordinate of its elements to be \(h_1\bmod r_i^2\). Show that the target then has the same sheared coordinate as the point it starts from, also when \(h_1\) is negative.

## 7. Solutions

**6.1.** \(\mu_i(0,0)=\mu_i(1,1)=2\), \(\mu_i(1,0)=\mu_i(0,1)=0\), and \(\mu_i(\alpha,\xi)=1\) for \(\xi\in\{2,3,4\}\). A list: \((0,0)\), \((0,0)\), \((1,1)\), \((1,1)\), \((0,2)\), \((1,2)\), \((0,3)\), \((1,3)\), \((0,4)\), \((1,4)\), indexed by \(\delta=1,\ldots,10\). For \(\xi=0\) the indices with \(e^b_\delta=0\) are \(1,2\); map them to \(0,1\in\mathbb Z/2\mathbb Z\), so \(\rho^a(1)=0-0=0\), \(\rho^a(2)=1-0=1\). For \(\xi=1\), indices \(3,4\) map to \(0,1\): \(\rho^a(3)=0-1=1\), \(\rho^a(4)=1-1=0\). For \(\xi\ge2\) the two indices have \(e^a=0,1\); map each to its own \(e^a\), so \(\rho^a=0\). For \(\alpha=0\) the indices with \(e^a_\delta=0\) are \(1,2,5,7,9\); map them to \(0,1,2,3,4\), giving \(\rho^b(1)=0\), \(\rho^b(2)=1\), \(\rho^b(5)=0\), \(\rho^b(7)=0\), \(\rho^b(9)=0\). For \(\alpha=1\) the indices are \(3,4,6,8,10\) with \(e^b=1,1,2,3,4\); map them to \(0,1,2,3,4\), giving \(\rho^b(3)=-1=4\), \(\rho^b(4)=0\), and \(\rho^b=0\) for the others.

**6.2.** With \(\mu\equiv1\), each \(e\in P_i\) occurs once, and the tuple (3.2) of \((l,\delta)\) is \((c_0+e_\delta,\ k_i-l)\), since \(\beta_i(x',k')=k'_i=k_i-l\). This is a bijection from \(K_i\times\Delta_i\) onto \(P_i\times K_i\).

**6.3.** \(Q(\alpha,\xi)=[\alpha=0]+[\xi=0]\), where \([\cdot]\) is \(1\) for a true statement and \(0\) otherwise, has the values \(Q(0,0)=2\), \(Q(0,1)=Q(0,2)=Q(1,0)=1\), \(Q(1,1)=Q(1,2)=0\), total \(5\), and satisfies (4.1) because it has the form \(u(\alpha)+v(\xi)\). The step "since \(b_i>D\), the first sum is \(0\)" fails: here \(b\sum u=3\le5\).

**6.4.** The translation by \(\bigl((0,M),v_0\bigr)\) maps the point above \((x,k)\) to the point above \((x+(0,M),k+\kappa)\), where \(\kappa\in K\) is the low part of \(v_0\), and adds the \(P\)-part \(\gamma\) of \(v_0\) to the useful outputs. So \(g_{i,x+(0,M)}(w+\kappa_i)=g_{i,x}(w)+\gamma_i\) for all \(w\in K_i\). If \(w-w'\in U_{ij}\), then \((w+\kappa_i)-(w'+\kappa_i)\in U_{ij}\), and the two functions have the same differences on such pairs. So the active sets agree, and the argument of Proposition 5.1 goes through.

**6.5.** The coordinate of the starting point is \(v_i(a)=x'_1+[k'_i-x'_1]_{r_i}+r_i\beta\) with \(x'_1=x_1-h_1\) and \(k'_i=k_i-l\), \(l\equiv h_1\pmod{r_i}\). Then \(k'_i-x'_1\equiv k_i-x_1\pmod{r_i}\), so \([k'_i-x'_1]_{r_i}=[k_i-x_1]_{r_i}\), and \(v_i(a)+h_1=x_1+[k_i-x_1]_{r_i}+r_i\beta\). Only residues of integers enter, so the sign of \(h_1\) plays no role.

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026

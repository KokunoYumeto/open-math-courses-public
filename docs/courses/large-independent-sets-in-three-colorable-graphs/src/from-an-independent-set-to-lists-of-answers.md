# From an independent set to lists of answers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the proof that the graph of the first lesson has no large independent set when the value of the Label Cover instance is small. An independent set \(\mathcal A\) gives a function on the space of the points that is \(1\) at the locations of \(\mathcal A\), changes its sign under the half shift and is constant across the links of length \(0\). Restricted to small sets of layers, this function is close to a function of a bounded number of rotations. The answers that belong to these rotations form short lists, and two lists for sets of layers that lie on different sides of a test can meet only if they contain a pair of answers that satisfies this test. So for an instance of small value they rarely meet.

- The function \(f\) of an independent set (Lemma 1.2).
- Lipschitz functions \(F_{\mathbf q}\) on the tori and their compatibility along a chain (Lemma 2.1).
- The functions of a set of layers (Lemma 3.1) and their lists (Lemma 4.1).
- Lists of separated sets of layers are disjoint with high probability (Lemma 5.1, Corollary 5.2).

The lesson follows [OpenAI-I, Section 4]. It uses the construction of [Label Cover and the graph of the reduction](label-cover-and-the-graph-of-the-reduction.md) and the extension lemma and Theorem (J) of [Lipschitz functions on a torus: extension, juntas and influences](lipschitz-functions-on-a-torus-extension-juntas-and-influences.md).

**The setting.** \(\mathcal C\) is a Label Cover instance with \(N\) tests, and \(r,s,m,P,\lambda,\mu\) are the numbers of the construction, with \(D=mP\). The first branch does not occur: \(\operatorname{dist}(\xi,T\xi)>\tfrac18\) for every point \(\xi\). \(\mathcal A\) is a nonempty independent set of the graph \(G(\mathcal C)\).

## 1. The function of an independent set

Let \(A\subset\mathscr X\) be the set of the locations of the vertices of \(\mathcal A\).

**Lemma 1.1.** \(\operatorname{dist}(\xi,T\eta)>\tfrac18\) for all \(\xi,\eta\in A\).

**Proof.** If \(\xi\ne\eta\), take vertices of \(\mathcal A\) with these locations. They are different and not joined by an edge, so \(\operatorname{dist}(\xi,T\eta)>\tfrac18\) by the rule for the edges. If \(\xi=\eta\), this is the assumption on the first branch. \(\blacksquare\)

For a point \(\xi\) let \(\operatorname{dist}(\xi,A)\) be the least of the numbers \(\operatorname{dist}(\xi,\alpha)\), \(\alpha\in A\); it can be \(\infty\). Write \((u)_+=\max\{u,0\}\), and put
\[
\begin{gathered}
e(\xi)=\bigl(1-32\operatorname{dist}(\xi,A)\bigr)_+ ,\\
f(\xi)=e(\xi)-e(T\xi),
\end{gathered}
\]
with \(e(\xi)=0\) if the distance is \(\infty\).

**Lemma 1.2.** For all points \(\xi,\eta\):

1. \(-1\le f(\xi)\le1\) and \(f(T\xi)=-f(\xi)\);
2. \(f(\xi)=1\) for \(\xi\in A\);
3. \(f(\xi)=f(\eta)\) if \(\operatorname{dist}(\xi,\eta)=0\), in particular for the two ends of a link of length \(0\);
4. \(|f(\mathbf q,x)-f(\mathbf q,y)|\le64\,d_\infty(x,y)\) for two points of one copy.

**Proof.** (1) \(e\) has values in \([0,1]\), and \(T(T\xi)=\xi\). (2) For \(\xi\in A\), \(e(\xi)=1\). By Lemma 3.2 of the first lesson and Lemma 1.1, \(\operatorname{dist}(T\xi,\alpha)=\operatorname{dist}(\xi,T\alpha)>\tfrac18\) for every \(\alpha\in A\). So \(1-32\operatorname{dist}(T\xi,A)<1-4<0\) and \(e(T\xi)=0\).

(3), (4) Let \(\operatorname{dist}(\xi,\eta)<\infty\). By the triangle inequality the two numbers \(\operatorname{dist}(\xi,A)\), \(\operatorname{dist}(\eta,A)\) are both infinite, and then \(e(\xi)=e(\eta)=0\), or both finite with a difference of at most \(\operatorname{dist}(\xi,\eta)\). The function \(u\mapsto(1-32u)_+\) changes by at most \(32\) times the change of \(u\). So
\[
|e(\xi)-e(\eta)|\le32\operatorname{dist}(\xi,\eta).
\]
The same holds for \(e\circ T\), because \(\operatorname{dist}(T\xi,T\eta)=\operatorname{dist}(\xi,\eta)\). Hence \(|f(\xi)-f(\eta)|\le64\operatorname{dist}(\xi,\eta)\). This gives (3), and (4) because \(\operatorname{dist}\le d_\infty\) inside a copy. \(\blacksquare\)

So \(f\) marks the locations of \(\mathcal A\) with the value \(1\) and their half shifts with \(-1\), and Lemma 1.1 is what makes the two marks compatible.

## 2. Functions on the tori

Let \(\mathbf q\) be a tuple of a layer \(i\). By Lemma 1.2 the function \(x\mapsto f(\mathbf q,x)\) on the finite set \(\Gamma^{M_i}\subset\mathbb T^{M_i}\) has values in \([-1,1]\), is \(64\)-Lipschitz and odd; and \(T\) maps \(\Gamma^{M_i}\) to itself. By the extension lemma (Lemma 1.1 of the second lesson) there is a function
\[
F_{\mathbf q}:\mathbb T^{M_i}\to[-1,1],
\]
\(64\)-Lipschitz for the sup distance and odd, with \(F_{\mathbf q}(x)=f(\mathbf q,x)\) for \(x\in\Gamma^{M_i}\).

**Fix one such function \(F_{\mathbf q}\) for every tuple \(\mathbf q\).** The family of these functions depends on the instance and on \(\mathcal A\). It is chosen once, before any chain is drawn; \(F_{\mathbf q}\) is a fixed function of the tuple \(\mathbf q\). For a chain with the tuples \(\mathbf q_1,\dots,\mathbf q_r\) write \(F_i=F_{\mathbf q_i}\).

**Lemma 2.1** (compatibility). For every chain, all \(i\le j\) and all \(x\in\mathbb T^{M_j}\),
\[
\bigl|F_j(x)-F_i(x\circ\pi_{ij})\bigr|\le\frac{64}{D} .
\]

**Proof.** Replace every phase of \(x\) by a nearest element of \(\Gamma\). This gives \(y\in\Gamma^{M_j}\) with \(d_\infty(x,y)\le\tfrac1{2D}\), and \(d_\infty(x\circ\pi_{ij},y\circ\pi_{ij})\le\tfrac1{2D}\) by Lemma 3.1 of the first lesson. Both functions are \(64\)-Lipschitz, so
\[
\begin{gathered}
|F_j(x)-F_j(y)|\le\frac{32}D,\\
|F_i(x\circ\pi_{ij})-F_i(y\circ\pi_{ij})|\le\frac{32}D .
\end{gathered}
\]
The points \((\mathbf q_j,y)\) and \((\mathbf q_i,y\circ\pi_{ij})\) have the link distance \(0\) (Lemma 4.1 of the first lesson). By Lemma 1.2(3),
\[
\begin{aligned}
F_j(y)=f(\mathbf q_j,y)&=f(\mathbf q_i,y\circ\pi_{ij})\\
&=F_i(y\circ\pi_{ij}).
\end{aligned}
\]
The three relations give the claim. \(\blacksquare\)

## 3. The functions of a set of layers

Let \(I\subset[r]\) be nonempty with at most \(s\) elements, and \(b=\min I\). Let
\[
N_I=\{(j,\ell):\ j\in I,\ \ell\in M_j\}
\]
be the set of the indices of the rotations of the layers in \(I\). An element of the cube \([0,1]^{N_I}\) is written \(\theta=(\theta_{j,\ell})\). Let \(\mathcal T=\{0,\tfrac1m,\dots,1\}\) be the set of the coefficients.

**Definition.** A *datum for \(I\)* is a pair \(\mathfrak d=(\mathbf q,\varpi)\) of a tuple \(\mathbf q\) of the layer \(b\) and a family \(\varpi=(\varpi_j)_{j\in I}\) of maps \(\varpi_j:M_b\to M_j\). For a datum and \(t\in\mathcal T^I\), the *phase map* \(\Phi_t^{\mathfrak d}\) from \([0,1]^{N_I}\) to \(\mathbb T^{M_b}\) is given, for \(\kappa\in M_b\), by
\[
\Phi_t^{\mathfrak d}(\theta)_\kappa=\sum_{j\in I}t_j\,\theta_{j,\varpi_j(\kappa)}\ \bmod1 ,
\]
and
\[
h_t^{\mathfrak d}=F_{\mathbf q}\circ\Phi_t^{\mathfrak d}:[0,1]^{N_I}\to[-1,1] .
\]
The *datum of \(I\) in a chain* is \((\mathbf q_b,(\pi_{bj})_{j\in I})\); for it we write \(\Phi_{I,t}\) and \(h_{I,t}\).

For \(I=B\), the location of an outcome of the experiment is the point \((\mathbf q_b,\Phi_{B,t}(\widehat\theta))\). So \(h_{B,t}\) is the function \(F_b\) at the location, with real rotations in place of the multiples of \(\tfrac1P\). The functions \(h_{I,t}\) for the smaller sets \(I\subset B\) are needed in the last lesson.

**Lemma 3.1.** For every datum for \(I\), every \(t\in\mathcal T^I\) and all \(\theta,\theta'\in[0,1]^{N_I}\),
\[
\begin{aligned}
|h_t^{\mathfrak d}(\theta)&-h_t^{\mathfrak d}(\theta')|\\
&\le64\,s\max_{(j,\ell)\in N_I}|\theta_{j,\ell}-\theta'_{j,\ell}| .
\end{aligned}
\]

**Proof.** Let \(\epsilon\) be the maximum on the right. For every \(\kappa\), the phases of \(\Phi_t^{\mathfrak d}(\theta)\) and \(\Phi_t^{\mathfrak d}(\theta')\) at \(\kappa\) differ by the phase of a real number of absolute value at most \(\sum_{j\in I}t_j\epsilon\le s\epsilon\). So their sup distance is at most \(s\epsilon\), and \(F_{\mathbf q}\) is \(64\)-Lipschitz. \(\blacksquare\)

The constant \(64s\) does not depend on the sizes of the sets of answers, although the number \(|N_I|\) of the variables does. A map \(\varpi_j\) may send many answers \(\kappa\) to the same \(\ell\); this does not increase the sup distance.

## 4. Lists

Let \(J(L,\tau)\) be the numbers of Theorem (J). Fix a number \(\gamma>0\) and put
\[
J_0=J(64s,\gamma),\qquad d=J_0\,(m+1)^s .
\]
Both numbers depend only on \(s\), \(m\) and \(\gamma\), not on the instance.

**The rule.** The set \(N_I\) depends only on \(I\), because all tuples of a layer have the same set of answers. Fix once, for every \(I\), an order of the finitely many subsets of \(N_I\). For a datum \(\mathfrak d\) for \(I\) and \(t\in\mathcal T^I\), let \(S_t^{\mathfrak d}\subset N_I\) be the first set in this order with at most \(J_0\) elements and
\[
\bigl\|h_t^{\mathfrak d}-E_{S}\,h_t^{\mathfrak d}\bigr\|_2<\gamma\qquad(S=S_t^{\mathfrak d}).
\]
Such a set exists by (J) and Lemma 3.1. Put, for \(j\in I\),
\[
\begin{gathered}
g_t^{\mathfrak d}=E_{S_t^{\mathfrak d}}\,h_t^{\mathfrak d},\qquad S^{\mathfrak d}=\bigcup_{t\in\mathcal T^I}S_t^{\mathfrak d},\\
S^{\mathfrak d,j}=\{\ell\in M_j:(j,\ell)\in S^{\mathfrak d}\}.
\end{gathered}
\]
For the datum of \(I\) in a chain we write \(S_I\), \(S_I^j\) and \(g_{I,t}\).

**Lemma 4.1.** For every datum \(\mathfrak d\) for \(I\):

1. \(\sum_{j\in I}|S^{\mathfrak d,j}|=|S^{\mathfrak d}|\le d\);
2. for every \(t\in\mathcal T^I\), the function \(g_t^{\mathfrak d}\) depends only on the rotations \(\theta_{j,\ell}\) with \(\ell\in S^{\mathfrak d,j}\), has values in \([-1,1]\), and \(\|h_t^{\mathfrak d}-g_t^{\mathfrak d}\|_2<\gamma\);
3. the sets \(S^{\mathfrak d,j}\) and the functions \(g_t^{\mathfrak d}\) are determined by the datum. In particular, two chains in which \(I\) has the same datum have the same lists \(S_I^j\).

**Proof.** (1) There are \((m+1)^{|I|}\le(m+1)^s\) elements \(t\), and each \(S_t^{\mathfrak d}\) has at most \(J_0\) elements. (2) is the choice of \(S_t^{\mathfrak d}\subset S^{\mathfrak d}\); a mean of values in \([-1,1]\) lies in \([-1,1]\). (3) The function \(h_t^{\mathfrak d}\) is defined from \(\mathbf q\), \(\varpi\), \(t\) and the fixed function \(F_{\mathbf q}\), and the rule uses nothing else. \(\blacksquare\)

The lists contain the rotations that matter for every choice of the coefficients, and they are chosen before the coefficients are drawn. They are objects of the proof; the map from formulas to graphs does not compute them.

**Definition.** For a chain, the *list of \(I\)* is the set
\[
A_I=\bigcup_{j\in I}\pi_{jr}\bigl(S_I^j\bigr)\subset M_r .
\]
It has at most \(d\) elements. All lists lie in the same set \(M_r=\Sigma_R^{\,r-1}\), the set of answers of the last layer.

## 5. Lists of separated sets of layers

**Lemma 5.1.** Let \(\operatorname{val}(\mathcal C)\le\sigma\). Let \(I\) and \(J\) be nonempty subsets of \([r]\) with at most \(s\) elements and \(\max I<\min J\). Then, for a chain drawn as in the experiment,
\[
\Pr\bigl(A_I\cap A_J\ne\varnothing\bigr)\le d^2\sigma .
\]

**Proof.** Let \(h=\max I\). Since \(h<\min J\le r\), the number \(h\) is one of the positions \(1,\dots,r-1\). Fix the tests \(c_k\) with \(k\ne h\); call them the *background*. The test \(c_h\) is independent of them and uniform in the list.

*The datum of \(I\) depends on \(c_h\) only through \(u_h\).* Let \(b=\min I\). The tuple \(\mathbf q_b=(v_1,\dots,v_{b-1},u_b,\dots,u_{r-1})\) contains the question \(u_h\) at the position \(h\ge b\), and no other part of \(c_h\). The maps \(\pi_{bj}\), \(j\in I\), are composed of the maps of the tests \(c_k\) with \(b\le k<j\le h\), so \(c_h\) is not among them. Hence, for the fixed background, the datum of \(I\) is a function of the question \(u_h\); this function is defined for every \(u\in U\) in place of \(u_h\). By Lemma 4.1(3) the same holds for the lists; write \(S_I^j[u]\).

*The datum of \(J\) depends on \(c_h\) only through \(v_h\).* Let \(b'=\min J>h\). The tuple \(\mathbf q_{b'}\) contains \(v_h\) at the position \(h<b'\), and the maps \(\pi_{b'j}\), \(j\in J\), are composed of the maps of tests \(c_k\) with \(k\ge b'>h\). Write \(S_J^{j}[v]\) for the lists as a function of \(v\in V\).

*The position \(h\).* Let \(j\in I\) and \(\ell\in M_j\). Since \(j\le h\), the answer \(\ell_h\) of \(\ell\) at the position \(h\) lies in \(\Sigma_L\), and the map \(\pi_{jr}\) applies \(\pi_{c_h}\) there:
\[
\pi_{jr}(\ell)_h=\pi_{c_h}(\ell_h).
\]
Let \(j'\in J\) and \(\ell'\in M_{j'}\). Since \(j'>h\), the answer \(\ell'_h\) lies in \(\Sigma_R\), and \(\pi_{j'r}\) changes only the positions from \(j'\) on:
\[
\pi_{j'r}(\ell')_h=\ell'_h .
\]

*Labelings.* For \(u\in U\) let \(X(u)\subset\Sigma_L\) be the set of the answers \(\ell_h\) for \(\ell\in S_I^j[u]\), \(j\in I\); for \(v\in V\) let \(Y(v)\subset\Sigma_R\) be the set of the answers \(\ell'_h\) for \(\ell'\in S_J^{j'}[v]\), \(j'\in J\). Each has at most \(d\) elements. Write them as sequences \(a_1(u),\dots,a_d(u)\) and \(b_1(v),\dots,b_d(v)\), repeating elements, or with arbitrary answers if a set is empty. For \(1\le p,q\le d\) the maps \(u\mapsto a_p(u)\) and \(v\mapsto b_q(v)\) form a labeling of \(\mathcal C\). There are \(d^2\) such labelings, and each satisfies at most \(\sigma N\) tests.

*Conclusion.* Suppose \(A_I\cap A_J\ne\varnothing\) for the chain with \(c_h=c\). Then there are \(j\in I\), \(\ell\in S_I^j[u_c]\), \(j'\in J\), \(\ell'\in S_J^{j'}[v_c]\) with \(\pi_{jr}(\ell)=\pi_{j'r}(\ell')\). At the position \(h\) this says \(\pi_c(\ell_h)=\ell'_h\), with \(\ell_h\in X(u_c)\) and \(\ell'_h\in Y(v_c)\). So one of the \(d^2\) labelings satisfies the test \(c\). This happens for at most \(d^2\sigma N\) of the \(N\) tests. So, for every background, the probability over \(c_h\) is at most \(d^2\sigma\), and the lemma follows by taking the mean over the backgrounds. \(\blacksquare\)

The proof needs that the lists are chosen by a rule from the datum alone. The functions \(F_{\mathbf q}\) may depend on the whole instance and on \(\mathcal A\), but they were fixed in advance, so the datum determines them.

**Corollary 5.2.** Under the assumptions of Lemma 5.1, the probability that a chain has two sets \(I,J\) as in the lemma with \(A_I\cap A_J\ne\varnothing\) is at most \(4^rd^2\sigma\).

**Proof.** There are at most \(2^r\cdot2^r\) pairs \((I,J)\) of subsets of \([r]\). \(\blacksquare\)

**What has been obtained.** Call two sets \(I,J\) *separated* if \(\max I<\min J\) or \(\max J<\min I\). Except for a set of chains of probability at most \(4^rd^2\sigma\), a chain has lists \(A_I\subset M_r\) with at most \(d\) elements, one for every nonempty set \(I\) of at most \(s\) layers, such that the lists of separated sets are disjoint. The next two lessons show that such a family of lists can be *aligned* on most sets \(B\) of \(s\) layers, if \(B\) is drawn with a suitable law: every answer can be given a layer that belongs to all sets \(I\subset B\) on whose lists the answer stands.

## 6. Exercises

**6.1.** Show that for every point \(\xi\) at most one of the numbers \(e(\xi)\), \(e(T\xi)\) is different from \(0\).

**6.2.** Let \(r=2\), \(I=\{1\}\), \(J=\{2\}\). Describe the data of \(I\) and \(J\) in a chain \(c_1=c\), the lists \(A_I\), \(A_J\), and the event \(A_I\cap A_J\ne\varnothing\).

**6.3.** Let \(r=5\), \(I=\{1,3\}\), \(J=\{4\}\). Which questions and which maps of the tests \(c_1,\dots,c_4\) occur in the datum of \(I\) and in the datum of \(J\)? What is \(h\) in the proof of Lemma 5.1?

**6.4.** Show that the factor \(|I|\) in the proof of Lemma 3.1 cannot be made smaller: for every \(I\) give \(t\), \(\theta\), \(\theta'\) with \(\theta\ne\theta'\) and
\[
\begin{aligned}
d_\infty\bigl(\Phi_{I,t}(\theta),&\Phi_{I,t}(\theta')\bigr)\\
&=|I|\max|\theta_{j,\ell}-\theta'_{j,\ell}| .
\end{aligned}
\]

**6.5.** Let \(y\in\Gamma^{M_j}\). Show that \(F_j(y)=F_i(y\circ\pi_{ij})\) for \(i\le j\), and that \(F_i(z)=F_i(z')\) for two families \(z,z'\in\Gamma^{M_i}\) that are pullbacks of the same \(y\) under two chains that have the tuple \(\mathbf q_i\) and the tuple \(\mathbf q_j\) in common.

## 7. Solutions

**6.1.** Suppose \(e(\xi)>0\) and \(e(T\xi)>0\). Then there are \(\alpha,\alpha'\in A\) with \(\operatorname{dist}(\xi,\alpha)<\tfrac1{32}\) and \(\operatorname{dist}(T\xi,\alpha')<\tfrac1{32}\). The second gives \(\operatorname{dist}(\xi,T\alpha')<\tfrac1{32}\), since \(T\) preserves the link distance and \(TT\xi=\xi\). So \(\operatorname{dist}(\alpha,T\alpha')<\tfrac1{16}\), against Lemma 1.1.

**6.2.** The datum of \(I\) is the tuple \((u_c)\) of the layer \(1\) with the identity of \(M_1=\Sigma_L\); the datum of \(J\) is the tuple \((v_c)\) of the layer \(2\) with the identity of \(M_2=\Sigma_R\). So \(S_I^1\subset\Sigma_L\) depends only on \(u_c\) and \(S_J^2\subset\Sigma_R\) only on \(v_c\); each has at most \(d\) elements. \(A_I=\pi_c(S_I^1)\) and \(A_J=S_J^2\). They meet if and only if \(\pi_c(a)=a'\) for some \(a\in S_I^1\) and \(a'\in S_J^2\): the two lists contain a pair of answers that satisfies the test.

**6.3.** The datum of \(I\): the tuple \(\mathbf q_1=(u_1,u_2,u_3,u_4)\) and the maps \(\pi_{11}\) (identity) and \(\pi_{13}\), which applies the maps of \(c_1\) and \(c_2\) at the positions \(1\) and \(2\). So it contains the four questions in \(U\) and the maps of \(c_1,c_2\). The datum of \(J\): the tuple \(\mathbf q_4=(v_1,v_2,v_3,u_4)\) and the identity. Here \(h=\max I=3\); of the test \(c_3\), the datum of \(I\) contains only \(u_3\) and the datum of \(J\) only \(v_3\).

**6.4.** Take any \(I\), all \(t_j=1\), \(\theta=0\) and all \(\theta'_{j,\ell}=\epsilon\) with \(0<\epsilon\le\tfrac1{2|I|}\). Then every phase of \(\Phi_{I,t}(\theta')\) is \(|I|\epsilon\), every phase of \(\Phi_{I,t}(\theta)\) is \(0\), and \(\||I|\epsilon\|=|I|\epsilon\) because \(|I|\epsilon\le\tfrac12\).

**6.5.** The first statement is in the proof of Lemma 2.1: the points \((\mathbf q_j,y)\) and \((\mathbf q_i,y\circ\pi_{ij})\) have the link distance \(0\), and \(F\) agrees with \(f\) on the points of \(\mathscr X\). For the second, both \((\mathbf q_i,z)\) and \((\mathbf q_i,z')\) have the link distance \(0\) to \((\mathbf q_j,y)\), hence to each other, and Lemma 1.2(3) gives \(f(\mathbf q_i,z)=f(\mathbf q_i,z')\). Two chains with the same tuples can have different tests between the same questions; the function \(f\) does not see the difference.

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026

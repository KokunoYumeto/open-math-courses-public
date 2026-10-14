# Markov type and the reduction to a finite walk

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A random walk in a normed space that makes steps of length about \(1\) is, after \(t\) steps, at a distance of at most \(t\) from its start. In a Hilbert space, a reversible stationary walk is typically much closer: at a distance of about \(\sqrt t\). A normed space has *Markov type* \(p\) if every such walk satisfies an estimate of this kind with \(t^{1/p}\). Every space has Markov type \(1\). [OpenAI-M] proves that a real Banach space with Markov type \(p>1\) has an equivalent uniformly convex norm; such spaces are called superreflexive. The converse was known, so nontrivial Markov type characterizes superreflexivity.

This lesson gives the definitions and the statement, and reduces the theorem to two statements that are proved in the other lessons: a space that is not superreflexive carries, in a finitary sense, a norm on sequences with an order structure; and in such a norm there are reversible walks that move at linear speed.

- Reversible chains and Markov type (Section 1).
- Superreflexivity, finite representability, the hypothesis (JE), the theorem (Section 2).
- Marked chains with odd labels; Markov type bounds sums of labels (Lemma 3.2).
- The two main statements and the proof of the theorem from them (Section 4).

The lesson follows [OpenAI-M, Sections 1 and 2]. It needs normed spaces and finite probability; the Hahn–Banach theorem enters only in the next lesson.

## 1. Reversible chains and Markov type

**Definition.** A *finite stationary reversible chain* consists of a finite set \(S\) of states, a transition matrix \(P=(P_{ij})_{i,j\in S}\) with entries \(\ge0\) and row sums \(1\), and a probability distribution \(\pi\) on \(S\) with
\[
\pi_iP_{ij}=\pi_jP_{ji}\qquad\text{for all }i,j\in S .
\]
The chain is the sequence of random states \(Z_0,Z_1,Z_2,\dots\) in which \(Z_0\) has the distribution \(\pi\) and \(Z_{t+1}\) is chosen from \(Z_t=i\) with the probabilities \(P_{ij}\).

Summing the condition over \(i\) gives \(\sum_i\pi_iP_{ij}=\pi_j\): the distribution \(\pi\) is stationary, and every \(Z_t\) has the distribution \(\pi\). More: every pair \((Z_t,Z_{t+1})\) has the same distribution as \((Z_0,Z_1)\), and this distribution is symmetric.

**Definition.** Let \(p>0\) and \(0<K<\infty\). A normed space \(X\) has *Markov type \(p\) with the constant \(K\)* if for every finite stationary reversible chain, every map \(f:S\to X\) and every integer \(t\ge1\),
\[
\begin{aligned}
&\mathbb E\,\|f(Z_t)-f(Z_0)\|^p\\
&\qquad\le K^p\,t\ \mathbb E\,\|f(Z_1)-f(Z_0)\|^p .
\end{aligned}
\]

**Lemma 1.1.** Every normed space has Markov type \(1\) with the constant \(1\).

**Proof.** By the triangle inequality,
\[
\begin{aligned}
&\|f(Z_t)-f(Z_0)\|\\
&\qquad\le\sum_{i=1}^t\|f(Z_i)-f(Z_{i-1})\| ,
\end{aligned}
\]
and each of the \(t\) terms has the same distribution as the first. \(\blacksquare\)

So only Markov type \(p>1\) is a condition; it is called *nontrivial*. The real line, and every Hilbert space, has Markov type \(2\) with the constant \(1\) (Exercise 5.2). The space \(\ell_1\) has no nontrivial Markov type (Exercise 5.3).

Let \(V\) and \(X\) be normed spaces. An injective linear map \(T\) from a finite-dimensional space \(E\) into \(X\) has the *distortion* \(\|T\|\,\|T^{-1}\|\), where \(T^{-1}\) is defined on the image.

**Lemma 1.2.** Let \(X\) have Markov type \(p\) with the constant \(K\), and let \(V\) be a normed space such that for every finite-dimensional subspace \(E\subseteq V\) and every \(\eta>0\) there is an injective linear map \(E\to X\) of distortion less than \(1+\eta\). Then \(V\) has Markov type \(p\) with the constant \(K\).

**Proof.** Let a chain and \(f:S\to V\) be given, and let \(E\) be the span of the finitely many values of \(f\). Choose \(T:E\to X\) with distortion less than \(1+\eta\), scaled so that \(\|x\|\le\|Tx\|\le(1+\eta)\|x\|\). The inequality for \(Tf\) in \(X\) gives the inequality for \(f\) with the constant \((1+\eta)K\). Let \(\eta\to0\). \(\blacksquare\)

In particular Markov type passes to subspaces. If the norm of \(X\) is replaced by an equivalent norm, \(X\) keeps Markov type \(p\), with another constant.

## 2. Superreflexivity and the theorem

A norm \(|\cdot|\) on a real vector space is *uniformly convex* if for every \(\varepsilon\in(0,2]\) there is \(\delta>0\) such that
\[
\begin{gathered}
|x|\le1,\quad|y|\le1,\quad|x-y|\ge\varepsilon\\
\Longrightarrow\quad\Bigl|\frac{x+y}2\Bigr|\le1-\delta .
\end{gathered}
\]
Two norms are *equivalent* if each is at most a constant times the other. A Banach space is *superreflexive* if it has an equivalent uniformly convex norm.

A Banach space \(Y\) is *finitely representable* in \(X\) if for every finite-dimensional subspace \(E\subseteq Y\) and every \(\eta>0\) there is an injective linear map \(E\to X\) of distortion less than \(1+\eta\). A Banach space \(Y\) is *reflexive* if the canonical map from \(Y\) into its bidual \(Y^{**}\) is onto.

**Hypothesis (JE)** (James and Enflo). If a real Banach space \(X\) is not superreflexive, there is a Banach space that is finitely representable in \(X\) and not reflexive.

This is one half of a theorem: a Banach space has an equivalent uniformly convex norm if and only if every Banach space that is finitely representable in it is reflexive. The half stated here combines a theorem of James with Enflo's renorming theorem. It is not proved in this course; it is a named hypothesis, used once, in the next lesson.

**Theorem 2.1** ([OpenAI-M]). Assume (JE). Every real Banach space that has Markov type \(p\) for some \(p>1\) is superreflexive.

According to [OpenAI-M], the converse is known: by a theorem of Pisier a superreflexive space has an equivalent norm that is uniformly smooth of a power type, and by a theorem of Naor, Peres, Schramm and Sheffield such a space has Markov type \(p\) for some \(p>1\). The converse is not used and not proved in this course.

## 3. Marked chains and odd labels

The walks of the proof are described by their steps, not by their states. Two different steps may join the same two states.

**Definition.** A *finite marked chain* consists of a finite set \(S\) of states and a finite set \(\mathcal E\) of *edges*. Every edge \(e\) has a source \(e^-\in S\), a target \(e^+\in S\), a *reverse* edge \(e^*\) with \((e^*)^-=e^+\), \((e^*)^+=e^-\) and \((e^*)^*=e\), and a probability \(q(e)\ge0\), such that \(\sum_{e:\ e^-=z}q(e)=1\) for every state \(z\). It is *stationary and reversible* for a probability distribution \(\pi\) on \(S\) if
\[
\pi(e^-)\,q(e)=\pi(e^+)\,q(e^*)
\]
for all edges \(e\).
The chain starts in a state \(Z_0\) with the distribution \(\pi\); from the state \(z\) it chooses an edge \(e\) with \(e^-=z\) with the probability \(q(e)\) and moves to \(e^+\). Let \(E_1,E_2,\dots\) be the edges chosen.

The states \(Z_0,Z_1,\dots\) form a finite stationary reversible chain, with \(P_{zz'}\) the sum of the \(q(e)\) over the edges from \(z\) to \(z'\). By the condition, the pair \((E_i,\ \text{its source})\) has the same distribution for all \(i\): the chain of the edges is stationary.

A map \(g\) from \(\mathcal E\) to a vector space is an *odd labeling* if \(g(e^*)=-g(e)\) for all \(e\).

If \(g(e)=f(e^+)-f(e^-)\) for a function \(f\) on the states, then \(g\) is odd, \(\sum_{i\le n}g(E_i)=f(Z_n)-f(Z_0)\), and Markov type applies. The labels of the proof are not of this form. The next lemma shows that Markov type controls their sums all the same.

**Lemma 3.1** ([OpenAI-M]). Let \(V\) be a normed space of Markov type \(p\) with the constant \(K\). Let a finite marked chain be stationary and reversible, and \(g:\mathcal E\to V\) an odd labeling. Then for every \(n\ge1\)
\[
\mathbb E\,\Bigl\|\sum_{i=1}^ng(E_i)\Bigr\|^p\le K^p\,n\ \mathbb E\,\|g(E_1)\|^p .
\]

**Proof.** *Coordinates for the edges.* An edge with \(e^*=e\) has \(g(e)=0\). The other edges form pairs \(\{e,e^*\}\); choose one edge \(e_1,\dots,e_r\) from each pair. Let \(u_1,\dots,u_r\) be the unit vectors of \(\mathbb Z^r\). The *displacement* of \(e_j\) is \(u_j\), that of \(e_j^*\) is \(-u_j\), and that of an edge with \(e^*=e\) is \(0\). If \(r=0\) all labels are \(0\).

*The lifted chain.* Let \(R>n\) be an integer and \(Q_R=\{-R,\dots,R\}^r\). The lifted chain has the states \(S\times Q_R\). From \((z,a)\) it chooses an edge \(e\) with \(e^-=z\) with the probability \(q(e)\). If \(a\) plus the displacement of \(e\) lies in \(Q_R\), it moves to \((e^+,\ a+\text{displacement})\); otherwise it stays at \((z,a)\). Let \(\pi'\) be the product of \(\pi\) and the uniform distribution on \(Q_R\). A move from \((z,a)\) to \((z',a')\) by an edge \(e\) has, under \(\pi'\), the same mass as the move back by \(e^*\), by the condition on \(\pi\) and \(q\); the move back is not rejected, because \(a\in Q_R\). Rejected moves do not change the state. So the lifted chain is a finite stationary reversible chain.

*A potential.* Put \(\Phi(z,a)=\sum_{j=1}^ra_j\,g(e_j)\in V\). When the lifted chain moves by an edge \(e\), the value of \(\Phi\) changes by \(g(e)\); when a move is rejected, it does not change. So for the lifted chain \((Z'_t)\),
\[
\mathbb E\,\|\Phi(Z'_1)-\Phi(Z'_0)\|^p\le\mathbb E\,\|g(E_1)\|^p .
\]

*Many steps.* Run the lifted chain and the marked chain with the same choices of edges, as long as no move is rejected. If the lifted chain starts at a point \((z,a)\) with \(a\in Q_{R-n}\), none of the first \(n\) moves is rejected, and \(\Phi(Z'_n)-\Phi(Z'_0)=\sum_{i\le n}g(E_i)\). The start \(a\) is uniform in \(Q_R\) and independent of \(Z_0\) and of the choices of the edges. So this event has the probability
\[
\alpha_R=\Bigl(\frac{2(R-n)+1}{2R+1}\Bigr)^r
\]
and is independent of \(E_1,\dots,E_n\). Hence
\[
\begin{aligned}
&\mathbb E\,\|\Phi(Z'_n)-\Phi(Z'_0)\|^p\\
&\qquad\ge\alpha_R\ \mathbb E\,\Bigl\|\sum_{i=1}^ng(E_i)\Bigr\|^p .
\end{aligned}
\]

*Markov type.* For the lifted chain and the map \(\Phi\), the definition gives
\[
\alpha_R\ \mathbb E\,\Bigl\|\sum_{i=1}^ng(E_i)\Bigr\|^p\le K^p\,n\ \mathbb E\,\|g(E_1)\|^p .
\]
Let \(R\to\infty\); then \(\alpha_R\to1\). \(\blacksquare\)

**Lemma 3.2.** The statement of Lemma 3.1 holds also if \(V\) is replaced by a normed space \(V'\) such that every finite-dimensional subspace of \(V'\) embeds into \(V\) with distortion arbitrarily close to \(1\).

**Proof.** By Lemma 1.2, \(V'\) has Markov type \(p\) with the constant \(K\). \(\blacksquare\)

The lift replaces the question "is the label a difference of a function of the states" by a bookkeeping device: the new states remember how often each edge was used, so every label becomes a difference. The boundary of the box \(Q_R\) costs a factor \(\alpha_R\) that disappears in the limit.

## 4. The two main statements

Let \(c_{00}\) be the space of the real sequences \(a=(a_1,a_2,\dots)\) with only finitely many entries \(\ne0\), and \(b_i\) the sequence with \(1\) at the position \(i\) and \(0\) elsewhere. A finite array \((a_1,\dots,a_m)\) is identified with the sequence \((a_1,\dots,a_m,0,0,\dots)\).

**Definition.** A norm \(N\) on \(c_{00}\) is *spreading invariant* if for all \(m\), all \(a_1,\dots,a_m\) and all indices \(k_1<\dots<k_m\)
\[
N\Bigl(\sum_{i=1}^ma_ib_i\Bigr)=N\Bigl(\sum_{i=1}^ma_ib_{k_i}\Bigr).
\]
It has *contractive merging* if for all arrays and all \(i\)
\[
\begin{aligned}
&N(\dots,a_{i-1},\ a_i+a_{i+1},\ a_{i+2},\dots)\\
&\qquad\le N(\dots,a_{i-1},\ a_i,\ a_{i+1},\ a_{i+2},\dots).
\end{aligned}
\]

Spreading invariance says that the norm of an array does not change when zeros are inserted or removed. Contractive merging, applied repeatedly, says: if an array is cut into consecutive blocks and every block is replaced by its sum, the norm does not increase.

**Proposition 4.1** (the ordered norm). Assume (JE). If a real Banach space \(X\) is not superreflexive, there is a norm \(N\) on \(c_{00}\) that is spreading invariant, has contractive merging, and is such that for every \(m\) and every \(\eta>0\) the space \(\mathbb R^m\) with the norm \(N\) has an injective linear map into \(X\) of distortion less than \(1+\eta\).

It is proved in [A spreading norm with contractive merging](a-spreading-norm-with-contractive-merging.md).

**Proposition 4.2** (a walk with linear displacement). Let \(N\) be a spreading invariant norm on \(c_{00}\) with contractive merging. For every integer \(n\ge1\) there are a finite stationary reversible marked chain and an odd labeling \(g\) with values in \(c_{00}\) such that \(N(g(e))=1\) for every edge and
\[
\Pr\Bigl(N\Bigl(\sum_{i=1}^ng(E_i)\Bigr)\ge\frac n{24}\Bigr)\ge\frac3{20}.
\]

It is proved in [The finite walk](the-finite-walk.md), with the tools of [Charts and reversible transport](charts-and-reversible-transport.md) and [Two levels from reduced words](two-levels-from-reduced-words.md).

**Proof of Theorem 2.1 from the two propositions.** Let \(X\) have Markov type \(p>1\) with the constant \(K\), and suppose that \(X\) is not superreflexive. Let \(N\) be the norm of Proposition 4.1, and \(V'\) the space \(c_{00}\) with the norm \(N\). Every finite-dimensional subspace of \(V'\) lies in some \(\mathbb R^m\), so it embeds into \(X\) with distortion arbitrarily close to \(1\). Let \(n\ge1\), and take the chain and the labeling of Proposition 4.2. By Lemma 3.2,
\[
\frac3{20}\Bigl(\frac n{24}\Bigr)^p\le\mathbb E\,N\Bigl(\sum_{i=1}^ng(E_i)\Bigr)^p\le K^p\,n .
\]
So \(n^{p-1}\le\tfrac{20}3\,(24K)^p\) for all \(n\). This is false for large \(n\), because \(p>1\). \(\blacksquare\)

The chains and the dimensions depend on \(n\); only the constant \(K\) is fixed. The walk of Proposition 4.2 moves in \(n\) steps of length \(1\) to a distance of the order \(n\), with a fixed probability: the norm \(N\) does not slow reversible walks down at all.

## 5. Exercises

**5.1.** Show that for a finite stationary reversible chain the pairs \((Z_0,Z_1)\) and \((Z_1,Z_0)\) have the same distribution.

**5.2.** Show that the real line has Markov type \(2\) with the constant \(1\). (Use that \(P\) is a symmetric operator for the inner product \(\langle f,h\rangle=\sum_i\pi_if_ih_i\), and \(1-\lambda^t\le t(1-\lambda)\) for \(-1\le\lambda\le1\).)

**5.3.** Let \(X=\ell_1\). For \(d\ge1\) let the chain be the walk on \(\{0,1\}^d\) that changes one uniformly chosen coordinate at each step, and \(f\) the inclusion of \(\{0,1\}^d\) into \(\mathbb R^d\) with the \(\ell_1\) norm. Show that \(\|f(Z_t)-f(Z_0)\|\ge t/2\) with a probability of at least \(\tfrac12\) if \(d\ge8t\), and conclude that \(\ell_1\) does not have Markov type \(p\) for any \(p>1\).

**5.4.** Let \(g(e)=f(e^+)-f(e^-)\) for a function \(f:S\to V\). Show that \(g\) is odd, and derive the inequality of Lemma 3.1 directly from the definition of Markov type.

**5.5.** On \(c_{00}\) let \(N(a)=\max_j|a_1+\dots+a_j|\). Show that \(N\) is a norm that is spreading invariant and has contractive merging. Compute \(N(1,-1,1,-1,\dots,1,-1)\).

## 6. Solutions

**5.1.** \(\Pr(Z_0=i,Z_1=j)=\pi_iP_{ij}\), and this is \(\pi_jP_{ji}=\Pr(Z_0=j,Z_1=i)\), the probability that the pair \((Z_1,Z_0)\) is \((i,j)\).

**5.2.** Let \(f:S\to\mathbb R\). Then
\[
\begin{aligned}
&\mathbb E(f(Z_t)-f(Z_0))^2\\
&\qquad=2\langle f,f\rangle-2\langle f,P^tf\rangle ,
\end{aligned}
\]
because \(Z_0\) and \(Z_t\) have the distribution \(\pi\) and \(\mathbb Ef(Z_0)f(Z_t)=\langle f,P^tf\rangle\). The reversibility says \(\langle Pf,h\rangle=\langle f,Ph\rangle\). So there is a basis of eigenvectors \(\varphi_k\), orthonormal for this inner product, with real eigenvalues \(\lambda_k\), and \(|\lambda_k|\le1\) because \(P\) has row sums \(1\). With \(f=\sum_kc_k\varphi_k\):
\[
\begin{aligned}
\langle f,f\rangle-\langle f,P^tf\rangle&=\sum_kc_k^2(1-\lambda_k^t)\\
&\le t\sum_kc_k^2(1-\lambda_k),
\end{aligned}
\]
and the last sum is the same expression for \(t=1\). The inequality \(1-\lambda^t\le t(1-\lambda)\) holds because \(1-\lambda^t=(1-\lambda)(1+\lambda+\dots+\lambda^{t-1})\) and the second factor is at most \(t\). For a Hilbert space apply this to the coordinates of \(f\) in an orthonormal basis of the span of its values.

**5.3.** The chain is reversible for the uniform distribution. \(\|f(Z_t)-f(Z_0)\|\) is the number of the coordinates that were changed an odd number of times. Call a step a *repetition* if it chooses a coordinate that was chosen before. A step is a repetition with a probability of at most \(t/d\le\tfrac18\); so the mean number of repetitions among \(t\) steps is at most \(t/8\), and it is at most \(t/4\) with a probability of at least \(\tfrac12\). With \(r\) repetitions, \(t-r\) coordinates are chosen, and at most \(r\) of them more than once; so at least \(t-2r\ge t/2\) coordinates are chosen exactly once, and these are changed. So \(\mathbb E\|f(Z_t)-f(Z_0)\|^p\ge\tfrac12(t/2)^p\), while \(\|f(Z_1)-f(Z_0)\|=1\). Markov type \(p\) with the constant \(K\) would give \(\tfrac12(t/2)^p\le K^pt\) for all \(t\), which is false for \(p>1\).

**5.4.** \(g(e^*)=f(e^-)-f(e^+)=-g(e)\). The sum of the first \(n\) labels is \(f(Z_n)-f(Z_0)\), and \(g(E_1)=f(Z_1)-f(Z_0)\); the inequality is the definition for the chain of the states.

**5.5.** \(N\) is a seminorm as a maximum of absolute values of linear forms; if all sums \(a_1+\dots+a_j\) are \(0\), all \(a_j\) are \(0\). Inserting zeros repeats values of the sums, and merging two entries removes one of the sums; so the maximum is unchanged in the first case and does not increase in the second. The sums of \((1,-1,\dots,1,-1)\) are \(1,0,1,0,\dots\), so the norm is \(1\).

## References

- [OpenAI-M] OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026

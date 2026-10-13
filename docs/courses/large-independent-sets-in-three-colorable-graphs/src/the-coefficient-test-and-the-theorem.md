# The coefficient test and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson finishes the proof of the theorem of [OpenAI-I]: for every \(\delta>0\) it is NP-hard to tell graphs with a proper coloring by three colors from graphs in which every independent set has fewer than \(\delta\,|V|\) vertices. What is left is a bound for one chain and one set \(B\) of layers that are aligned: the vertex of the experiment then lies in a given independent set only with a small probability. The proof adds one auxiliary phase for every layer of \(B\) and studies the influence of these phases. A layer with the coefficient \(0\) has a small influence because of the alignment; a layer with a positive coefficient rarely has a large influence because the law of the coefficients falls geometrically; and a function without a coordinate of large influence has a small mean square.

- The bound for an aligned pair (Proposition 1.1), proved in Sections 2 to 5.
- The order in which the numbers of the construction are chosen (Section 6).
- The theorem (Theorem 7.1).

The lesson follows [OpenAI-I, Sections 6 and 7]. It uses all earlier lessons of the course: the graph ([Label Cover and the graph of the reduction](label-cover-and-the-graph-of-the-reduction.md)), influences ([Lipschitz functions on a torus: extension, juntas and influences](lipschitz-functions-on-a-torus-extension-juntas-and-influences.md)), the functions \(F_{\mathbf q}\), \(h_{I,t}\) and the lists ([From an independent set to lists of answers](from-an-independent-set-to-lists-of-answers.md)), and aligned pairs ([Order-invariant arrays and the common index](order-invariant-arrays-and-the-common-index.md)).

## 1. The bound for an aligned pair

**The setting.** \(\mathcal C\) is a Label Cover instance; \(r\ge s\ge2\), \(m\), \(P\), \(\lambda\), \(\mu\) are the numbers of the construction and \(D=mP\); the first branch does not occur; \(\mathcal A\) is a nonempty independent set of \(G(\mathcal C)\). The functions \(F_{\mathbf q}\) are fixed as in the third lesson, and the lists are formed with a number \(\gamma>0\). Let \(\varepsilon>0\), and let \(\beta>0\) and \(K\ge1\) be the numbers of Proposition 4.1 of the second lesson for the Lipschitz constant \(64\) and for \(\varepsilon\).

**The conditions.** Let \(p_m\) be the probability of the coefficient \(1\). Assume

- (P1) \(64/m<\beta/2\);
- (P2) \(\lambda K<\varepsilon\);
- (P3) \((1-p_m)^s<\varepsilon\);
- (P4) \(4s\gamma^2/\beta^2<\varepsilon\);
- (P5) \(64/D<\gamma\);
- (P6) \(128\,s/P<\varepsilon\).

**Proposition 1.1.** Assume (P1) to (P6). Let a chain and a set \(B\) form an aligned pair. Then the probability that the vertex of the experiment lies in \(\mathcal A\), given this chain and this \(B\), is less than \(6\varepsilon\).

Sections 2 to 5 prove this. **Fix an aligned pair** of a chain and a set \(B\), and a map \(a:M_r\to B\) with \(a(A_I)\subset I\) for all nonempty \(I\subset B\). Let \(b=\min B\). The random objects are

- the coefficients \(t=(t_j)_{j\in B}\), independent with the law of the coefficients;
- real rotations \(\theta=(\theta_{j,\ell})\), \(j\in B\), \(\ell\in M_j\), independent and uniform in \([0,1)\);
- auxiliary phases \(z=(z_i)_{i\in B}\), independent and uniform in \(\mathbb T=[0,1)\);

all independent of each other. Means over them are written \(\mathbb E_t\), \(\mathbb E_\theta\), \(\mathbb E_z\). The auxiliary phases are not part of the experiment; they are removed again in Section 5.

## 2. Auxiliary phases

For \(\kappa\in M_b\) put \(\alpha(\kappa)=a(\pi_{br}(\kappa))\in B\). Define the family of phases \(\Psi(t,\theta,z)\in\mathbb T^{M_b}\) and the function \(H\) by
\[
\begin{gathered}
\Psi(t,\theta,z)_\kappa=z_{\alpha(\kappa)}+\sum_{j\in B}t_j\,\theta_{j,\pi_{bj}(\kappa)} ,\\
H(t,\theta;z)=F_b\bigl(\Psi(t,\theta,z)\bigr),
\end{gathered}
\]
where the sum in the first line is read as a phase.
Without the term \(z_{\alpha(\kappa)}\) this is the family \(\Phi_{B,t}(\theta)\) of the third lesson. For fixed \(t\), the function \(H\) is continuous in \((\theta,z)\).

**Lemma 2.1.** For fixed \(t\) and \(\theta\), the function \(z\mapsto H(t,\theta;z)\) on \(\mathbb T^B\) has values in \([-1,1]\), is \(64\)-Lipschitz for the sup distance, and \(\mathbb E_zH(t,\theta;z)=0\).

**Proof.** Every phase of \(\Psi\) contains exactly one of the \(z_i\), with the coefficient \(1\). So \(d_\infty(\Psi(t,\theta,z),\Psi(t,\theta,z'))\le d_\infty(z,z')\), and \(F_b\) is \(64\)-Lipschitz. If \(\tfrac12\) is added to every \(z_i\), then \(\tfrac12\) is added to every phase of \(\Psi\): \(\Psi(t,\theta,Tz)=T\Psi(t,\theta,z)\). Since \(F_b\) is odd, \(H(t,\theta;Tz)=-H(t,\theta;z)\). The map \(z\mapsto Tz\) preserves the Lebesgue measure, so \(\mathbb E_zH=-\mathbb E_zH\). \(\blacksquare\)

For \(i\in B\) let \(Q_i\) be the operator of the second lesson for the coordinate \(z_i\), and put
\[
\begin{gathered}
D_i(t,\theta)=\bigl\|Q_iH(t,\theta;\cdot)\bigr\|_2,\\
X(t,\theta)=\mathbb E_z\,H(t,\theta;z)^2 ,
\end{gathered}
\]
with the norm of the functions of \(z\). By Lemma 2.1 and Proposition 4.1 of the second lesson, applied to the \(s\) coordinates \(z_i\), for all \(t\) and \(\theta\):

- (2.1) if \(X(t,\theta)>\varepsilon\), then \(D_i(t,\theta)\ge\beta\) for some \(i\in B\);
- (2.2) at most \(K\) indices \(i\in B\) have \(D_i(t,\theta)\ge\beta/2\).

Both numbers \(\beta\) and \(K\) do not depend on \(s\).

## 3. Layers with the coefficient 0

**Lemma 3.1.** Let \(t\) be such that \(t_j=1\) for some \(j\in B\), and let \(i\in B\) have \(t_i=0\). Then
\[
\mathbb E_\theta\,D_i(t,\theta)^2<4\gamma^2 .
\]

**Proof.** Let \(I=B\setminus\{i\}\); it contains \(j\). Let \(c=\min I\ge b\) and \(t'=(t_k)_{k\in I}\). Recall the function \(h_{I,t'}=F_c\circ\Phi_{I,t'}\) of the rotations of the layers in \(I\), and the function \(g_{I,t'}\) with \(\|h_{I,t'}-g_{I,t'}\|_2<\gamma\) that depends only on the rotations \(\theta_{k,\ell}\) with \(\ell\in S_I^k\) (Lemma 4.1 of the third lesson).

*Shifted rotations.* For given \(\theta\) and \(z\) define rotations \(\theta'\) of the layers in \(I\): for \(\ell\in M_j\), and for \(k\in I\) with \(k\ne j\) and \(\ell\in M_k\),
\[
\begin{gathered}
\theta'_{j,\ell}=\theta_{j,\ell}+z_{a(\pi_{jr}(\ell))}\ \bmod1,\\
\theta'_{k,\ell}=\theta_{k,\ell},
\end{gathered}
\]
with representatives in \([0,1)\). Only the layer \(j\) is changed.

*Step 1: an identity.* For every \(\kappa\in M_b\),
\[
\Phi_{I,t'}(\theta')_{\pi_{bc}(\kappa)}=\Psi(t,\theta,z)_\kappa .
\]
Indeed, since \(\pi_{ck}\circ\pi_{bc}=\pi_{bk}\), the left side is the phase of \(\sum_{k\in I}t_k\theta'_{k,\pi_{bk}(\kappa)}\). The term with \(k=j\) has the coefficient \(1\) and is the phase
\[
\theta_{j,\pi_{bj}(\kappa)}+z_{a(\pi_{jr}(\pi_{bj}(\kappa)))}=\theta_{j,\pi_{bj}(\kappa)}+z_{\alpha(\kappa)} ,
\]
because \(\pi_{jr}\circ\pi_{bj}=\pi_{br}\). The other terms are those of \(\Psi\), and the term of \(\Psi\) with \(k=i\) is \(0\). So \(\Psi(t,\theta,z)=\Phi_{I,t'}(\theta')\circ\pi_{bc}\).

*Step 2: from the layer \(b\) to the layer \(c\).* By Step 1, \(H(t,\theta;z)=F_b(x\circ\pi_{bc})\) with \(x=\Phi_{I,t'}(\theta')\), while \(h_{I,t'}(\theta')=F_c(x)\). By the compatibility of the functions \(F\) along a chain (Lemma 2.1 of the third lesson) and (P5),
\[
\bigl|H(t,\theta;z)-h_{I,t'}(\theta')\bigr|\le\frac{64}D<\gamma .
\]

*Step 3: the shift preserves the measure.* For fixed \(z\), the map \(\theta\mapsto\theta'\) adds a fixed phase to every rotation of the layer \(j\) and leaves the other rotations of the layers in \(I\) unchanged. Such a map preserves the Lebesgue measure of the cube. So for every \(z\)
\[
\begin{aligned}
\mathbb E_\theta\bigl(h_{I,t'}(\theta')&-g_{I,t'}(\theta')\bigr)^2\\
&=\|h_{I,t'}-g_{I,t'}\|_2^2<\gamma^2 .
\end{aligned}
\]

*Step 4: the alignment.* The function \((\theta,z)\mapsto g_{I,t'}(\theta')\) does not depend on \(z_i\). Indeed, \(g_{I,t'}\) depends only on the rotations \(\theta'_{k,\ell}\) with \(\ell\in S_I^k\). For \(k\ne j\) these do not contain \(z\). For \(k=j\) and \(\ell\in S_I^j\), the rotation \(\theta'_{j,\ell}\) contains the phase \(z_{a(\pi_{jr}(\ell))}\), and \(\pi_{jr}(\ell)\) lies in the list \(A_I\). Since the pair is aligned, \(a(A_I)\subset I\), so this is not the phase \(z_i\).

*Step 5.* Consider \(H\) and \(G=g_{I,t'}(\theta')\) as bounded Borel functions of all the variables \((\theta,z)\), with the norm \(\|\cdot\|\) of these functions, and \(Q_i\) as the operator for the coordinate \(z_i\) among them. By Step 4, \(Q_iG=0\). By Steps 2 and 3, \(\|H-G\|<\gamma+\gamma\). Since \(Q_i\) does not increase the norm,
\[
\begin{aligned}
\mathbb E_\theta\,D_i(t,\theta)^2&=\|Q_iH\|^2\\
&=\|Q_i(H-G)\|^2\\
&\le\|H-G\|^2<4\gamma^2 .
\end{aligned}
\]
The first equation is Fubini's theorem. \(\blacksquare\)

In Step 1 the coefficient \(1\) is essential. With a coefficient \(t_j<1\), the product \(t_j\theta'_{j,\ell}\) is not the phase of \(t_j\theta_{j,\ell}+t_jz\) (Exercise 8.1), and the phase \(z\) would not enter with the coefficient \(1\).

**Corollary 3.2.** The probability, over \(t\) and \(\theta\), that some coefficient is \(1\) and some \(i\in B\) has \(t_i=0\) and \(D_i(t,\theta)\ge\beta\), is at most \(4s\gamma^2/\beta^2<\varepsilon\).

**Proof.** For a fixed \(t\) with some coefficient \(1\) and a fixed \(i\) with \(t_i=0\), Lemma 3.1 and Markov's inequality give \(\Pr_\theta(D_i\ge\beta)\le4\gamma^2/\beta^2\). There are at most \(s\) such \(i\). Take the mean over \(t\), and use (P4). \(\blacksquare\)

## 4. Layers with a positive coefficient

**Lemma 4.1.** The probability, over \(t\) and \(\theta\), that some \(i\in B\) has \(t_i>0\) and \(D_i(t,\theta)\ge\beta\), is at most \(\lambda K<\varepsilon\).

**Proof.** Fix \(i\in B\), the rotations \(\theta\) and the coefficients \(t_j\), \(j\ne i\). For \(0\le k\le m\) let \(H_k\) be the function \(z\mapsto H(t,\theta;z)\) with \(t_i=k/m\), and \(d_k=\|Q_iH_k\|_2\).

Passing from \(t_i=(k-1)/m\) to \(t_i=k/m\) adds to every phase of \(\Psi\) the phase of \(\theta_{i,\ell}/m\) for some \(\ell\), a number in \([0,\tfrac1m)\). So the two families of phases have a sup distance of at most \(\tfrac1m\), and \(|H_k-H_{k-1}|\le64/m\) at every \(z\). Since \(Q_i\) does not increase the norm, and by (P1), for \(1\le k\le m\)
\[
\begin{aligned}
|d_k-d_{k-1}|&\le\|Q_i(H_k-H_{k-1})\|_2\\
&\le\frac{64}m<\frac\beta2 .
\end{aligned}
\]
Hence \(d_k\ge\beta\) implies \(d_{k-1}\ge\beta/2\). With \(p_k=\lambda p_{k-1}\),
\[
\begin{aligned}
\sum_{k=1}^mp_k\,[d_k\ge\beta]&\le\lambda\sum_{k=1}^mp_{k-1}\,[d_{k-1}\ge\tfrac\beta2]\\
&\le\lambda\sum_{h=0}^mp_h\,[d_h\ge\tfrac\beta2],
\end{aligned}
\]
where \([\,\cdot\,]\) is \(1\) if the condition holds and \(0\) otherwise. In words: for fixed \(\theta\) and \(t_j\), \(j\ne i\),
\[
\Pr_{t_i}\bigl(t_i>0,\ D_i\ge\beta\bigr)\le\lambda\,\Pr_{t_i}\bigl(D_i\ge\tfrac\beta2\bigr).
\]
Take the mean over \(\theta\) and the other coefficients, and add over \(i\in B\):
\[
\begin{aligned}
\Pr\bigl(\exists\,i:{}&\ t_i>0,\ D_i\ge\beta\bigr)\\
&\le\lambda\sum_{i\in B}\Pr\bigl(D_i\ge\tfrac\beta2\bigr)\\
&=\lambda\,\mathbb E\,\#\{i:D_i\ge\tfrac\beta2\}\le\lambda K ,
\end{aligned}
\]
by (2.2). The last inequality of the lemma is (P2). \(\blacksquare\)

Lowering \(t_i\) by one step can remove the only coefficient \(1\). This does no harm: (2.2) holds for all \(t\).

## 5. The mean square and the vertices

Let \(\mathcal F\) be the event that some coefficient \(t_j\), \(j\in B\), is \(1\). Its complement has the probability \((1-p_m)^s<\varepsilon\) by (P3).

**Lemma 5.1.** \(\mathbb E_{t,\theta,z}\,H(t,\theta;z)^2<4\varepsilon\).

**Proof.** Let \(X(t,\theta)>\varepsilon\). By (2.1) some \(i\in B\) has \(D_i(t,\theta)\ge\beta\). Then \(\mathcal F\) fails, or \(\mathcal F\) holds and \(t_i=0\), or \(t_i>0\). By (P3), Corollary 3.2 and Lemma 4.1 each of the three cases has a probability of less than \(\varepsilon\). So \(\Pr(X>\varepsilon)<3\varepsilon\), and since \(0\le X\le1\),
\[
\mathbb E_{t,\theta}X\le\varepsilon+\Pr(X>\varepsilon)<4\varepsilon .
\]
\(\blacksquare\)

**Lemma 5.2** (the phases are absorbed). For every \(t\) in \(\mathcal F\),
\[
\mathbb E_{\theta,z}\,H(t,\theta;z)^2=\mathbb E_\theta\,F_b\bigl(\Phi_{B,t}(\theta)\bigr)^2 .
\]

**Proof.** Take \(j\in B\) with \(t_j=1\), and let \(\theta''\) be \(\theta\) with the rotations of the layer \(j\) shifted: \(\theta''_{j,\ell}=\theta_{j,\ell}+z_{a(\pi_{jr}(\ell))}\bmod1\). As in Step 1 of Lemma 3.1, now with all layers of \(B\), \(\Phi_{B,t}(\theta'')=\Psi(t,\theta,z)\), so \(H(t,\theta;z)=F_b(\Phi_{B,t}(\theta''))\). For every fixed \(z\) the map \(\theta\mapsto\theta''\) preserves the Lebesgue measure, so \(\mathbb E_\theta H(t,\theta;z)^2=\mathbb E_\theta F_b(\Phi_{B,t}(\theta))^2\). \(\blacksquare\)

**Proof of Proposition 1.1.** By Lemmas 5.2 and 5.1,
\[
\begin{aligned}
\mathbb E_{t,\theta}\Bigl([t\in\mathcal F]\,F_b\bigl(\Phi_{B,t}(\theta)\bigr)^2\Bigr)&\le\mathbb E_{t,\theta,z}H^2\\
&<4\varepsilon .
\end{aligned}
\]
*From real rotations to the rotations of the experiment.* Put
\[
\widehat\theta_{j,\ell}=\frac{\lfloor P\,\theta_{j,\ell}\rfloor}P .
\]
If the \(\theta_{j,\ell}\) are independent and uniform in \([0,1)\), the \(\widehat\theta_{j,\ell}\) are independent and uniform in \(\{0,\tfrac1P,\dots,\tfrac{P-1}P\}\), as in the experiment. Every rotation changes by less than \(\tfrac1P\), so every phase of \(\Phi_{B,t}\) changes by the phase of a number of absolute value at most \(\sum_jt_j/P\le s/P\). For numbers \(u,v\in[-1,1]\), \(|u^2-v^2|\le2|u-v|\). With (P6),
\[
\begin{aligned}
\bigl|F_b(\Phi_{B,t}(\theta))^2-{}&F_b(\Phi_{B,t}(\widehat\theta))^2\bigr|\\
&\le2\cdot64\cdot\frac sP<\varepsilon .
\end{aligned}
\]
Together with \(\Pr(t\notin\mathcal F)<\varepsilon\) and \(F_b^2\le1\),
\[
\mathbb E_{t,\widehat\theta}\,F_b\bigl(\Phi_{B,t}(\widehat\theta)\bigr)^2<\varepsilon+(4\varepsilon+\varepsilon)=6\varepsilon .
\]
*The vertices.* Given the chain and \(B\), the outcome of the experiment consists of \(t\) and \(\widehat\theta\) with the laws used here, and its location is the point \(\xi=(\mathbf q_b,\Phi_{B,t}(\widehat\theta))\) of \(\mathscr X\). There \(F_b\) agrees with the function \(f\) of the independent set: \(F_b(\Phi_{B,t}(\widehat\theta))=f(\xi)\). If the vertex of the experiment, a copy of the outcome, lies in \(\mathcal A\), then \(\xi\in A\) and \(f(\xi)=1\). So the probability that the vertex lies in \(\mathcal A\) is at most the mean of \(f(\xi)^2\), which is less than \(6\varepsilon\). \(\blacksquare\)

## 6. The numbers

Let \(\delta\) be a rational number with \(0<\delta<\tfrac13\). The numbers are chosen in the following order; each choice is possible and depends only on the earlier ones.

1. A rational \(\varepsilon\) with \(0<\varepsilon<\delta/8\).
2. The numbers \(\beta>0\) and \(K\ge1\) of Proposition 4.1 of the second lesson for the Lipschitz constant \(64\) and \(\varepsilon\).
3. An integer \(m\ge1\) with \(64/m<\beta/2\). This is (P1).
4. A rational \(\lambda\) with \(0<\lambda<1\) and \(\lambda K<\varepsilon\). This is (P2). The law of the coefficients is fixed by \(m\) and \(\lambda\), and \(p_m>0\).
5. An integer \(s\ge2\) with \((1-p_m)^s<\varepsilon\). This is (P3).
6. A number \(\gamma>0\) with \(4s\gamma^2/\beta^2<\varepsilon\). This is (P4).
7. An even integer \(P\ge2\) with \(64/(mP)<\gamma\) and \(128\,s/P<\varepsilon\). These are (P5) and (P6); \(D=mP\).
8. The bound \(d=J(64s,\gamma)\,(m+1)^s\) for the lists.
9. The integer \(r\ge s\) and the law \(\mu\) with rational values that the alignment theorem gives for \(s\), \(d\) and \(\eta=\varepsilon\).
10. A number \(\sigma>0\) with \(4^rd^2\sigma<\varepsilon\).
11. The sets of answers \(\Sigma_L\), \(\Sigma_R\) and the map \(\varphi\mapsto\mathcal C_\varphi\) of Theorem 2.1 of the first lesson for this \(\sigma\); and \(k_\delta=\lfloor1/\delta\rfloor+1\).

The order matters at three places. The numbers \(\beta\) and \(K\) do not depend on the number \(s\) of the coordinates, so \(s\) can be chosen after them, and it depends on them through \(m\) and \(\lambda\). The bound \(d\) for the lists does not depend on the number \(r\) of the layers, so the alignment theorem can be applied after \(d\) is known. And no number depends on the sizes of the sets of answers, which are chosen last and can be very large when \(\sigma\) is small.

The numbers \(r,s,m,P,\lambda,\mu,k_\delta\) and the sets of answers are constants of the map \(\varphi\mapsto G_\varphi\) for the given \(\delta\). The proof shows that suitable constants exist. It gives no bound for them, because the alignment theorem gives none for \(r\). The numbers \(\varepsilon\), \(\beta\), \(K\), \(\gamma\), \(d\), \(\sigma\), the functions \(F_{\mathbf q}\), the lists and the maps \(a\) occur only in the proof.

## 7. The theorem

**Theorem 7.1** ([OpenAI-I]). Assume (PCP) and (PR). For every real number \(\delta\) with \(0<\delta<\tfrac13\) there is a map, computable in polynomial time, from Boolean formulas \(\varphi\) in conjunctive normal form with three literals per clause to graphs \(G_\varphi\) such that

- if \(\varphi\) is satisfiable, then \(G_\varphi\) has a proper coloring with three colors;
- if \(\varphi\) is not satisfiable, then every independent set of \(G_\varphi\) has fewer than \(\delta\,|V(G_\varphi)|\) vertices.

**Proof.** As noted in the first lesson, we may take \(\delta\) rational. Choose the numbers as in Section 6, and let \(G_\varphi=G(\mathcal C_\varphi)\) be the graph of the first lesson for the instance \(\mathcal C_\varphi\). It is computed in polynomial time: the instance by Theorem 2.1 of the first lesson, the graph from the instance by Proposition 4.2 there.

*\(\varphi\) satisfiable.* Then \(\operatorname{val}(\mathcal C_\varphi)=1\), and by Theorem 5.2 of the first lesson the graph has a proper coloring with three colors.

*\(\varphi\) not satisfiable.* Then \(\operatorname{val}(\mathcal C_\varphi)\le\sigma\). In the first branch the graph is the complete graph on \(k_\delta\) vertices; its independent sets have one vertex, and \(1<\delta k_\delta\). Otherwise let \(\mathcal A\) be an independent set; we may assume that it is not empty. Form the functions \(F_{\mathbf q}\) and the lists for \(\mathcal A\), with the number \(\gamma\). A vertex drawn uniformly is a copy of the outcome of the experiment. By Proposition 4.1 of the previous lesson and the choice of \(\sigma\), the pair of the chain and the set \(B\) of the experiment fails to be aligned with a probability of at most
\[
4^rd^2\sigma+\varepsilon<2\varepsilon .
\]
For every aligned pair, Proposition 1.1 bounds the probability that the vertex lies in \(\mathcal A\) by \(6\varepsilon\); its conditions (P1) to (P6) hold by the choice of the numbers. Hence
\[
\begin{aligned}
\frac{|\mathcal A|}{|V(G_\varphi)|}&=\Pr\bigl(\text{the vertex lies in }\mathcal A\bigr)\\
&<2\varepsilon+6\varepsilon=8\varepsilon<\delta .
\end{aligned}
\]
\(\blacksquare\)

**What the proof rests on.** Two theorems of the literature are hypotheses of this course and are not proved in it: (PCP) and (PR), the PCP theorem and the parallel repetition theorem, which give the Label Cover instances of value \(1\) or at most \(\sigma\) (first lesson, Theorem 2.1).

The theorem of T. Austin that a function on a cube that is Lipschitz for the sup distance is close to a function of a bounded number of coordinates (Theorem (J) of the second lesson) is used twice: for the numbers \(\beta\) and \(K\), and for the lists. It is proved in [Lipschitz functions are close to juntas](course:hypercontractivity-on-a-torus-and-juntas/lipschitz-functions-are-close-to-juntas) (Hypercontractivity on a torus and juntas for Lipschitz functions).

Everything else is proved in the six lessons, including the minimax theorem and Ramsey's theorem, which enter the alignment theorem.

## 8. Exercises

**8.1.** Let \(t_j=\tfrac12\), \(\theta=0.6\), \(z=0.6\), and let \(\theta'\) be the representative of \(\theta+z\) in \([0,1)\). Compare the phases of \(t_j\theta'\) and of \(t_j\theta+t_jz\). What is the phase of \(t_j\theta'-t_j\theta\) for \(t_j=1\)?

**8.2.** Let \(m=2\) and \(\lambda=\tfrac12\). Compute the law of the coefficients, and find the least \(s\) with \((1-p_m)^s<\tfrac1{100}\).

**8.3.** Show that \(D_i(t,\theta)=0\) if \(i\) is not a value of the map \(\alpha\). Conclude that in (2.1) the layer \(i\) can be taken in the image of \(a\).

**8.4.** In the proof of Lemma 3.1, which steps use that \(t_i=0\), that \(t_j=1\), and that the pair is aligned? What does the argument give for a pair that is not aligned?

**8.5.** Suppose that the law of the coefficients were uniform on \(\{0,\tfrac1m,\dots,1\}\). Which statement of Section 4 would the same argument give, and why is it not enough?

## 9. Solutions

**8.1.** \(\theta+z=1.2\), so \(\theta'=0.2\) and \(t_j\theta'=0.1\). But \(t_j\theta+t_jz=0.6\). The two phases differ by \(\tfrac12\). The reason is that \(\theta'=\theta+z-1\), and \(t_j\cdot1=\tfrac12\) is not an integer. For \(t_j=1\) the difference \(\theta'-\theta\) is \(z\) or \(z-1\), and its phase is \(z\), for every \(\theta\) and \(z\).

**8.2.** \(1+\lambda+\lambda^2=\tfrac74\), so \(p_0=\tfrac47\), \(p_1=\tfrac27\), \(p_2=\tfrac17\). \((\tfrac67)^s<\tfrac1{100}\) means \(s>\log100/\log\tfrac76\approx29.9\). The least \(s\) is \(30\).

**8.3.** If no \(\kappa\) has \(\alpha(\kappa)=i\), no phase of \(\Psi\) contains \(z_i\), so \(H\) does not depend on \(z_i\) and \(Q_iH=0\). Every value of \(\alpha\) is a value of \(a\). In (2.1) the index \(i\) has \(D_i\ge\beta>0\), so it is a value of \(\alpha\).

**8.4.** Step 1 uses \(t_i=0\) (the term of the layer \(i\) is missing in \(\Phi_{I,t'}\)) and \(t_j=1\) (the shift of the layer \(j\) produces exactly the phase \(z_{\alpha(\kappa)}\)). Step 4 uses the alignment. Without it, Steps 1 to 3 still show that \(H\) is within \(2\gamma\) of \(G=g_{I,t'}(\theta')\) in the norm, but \(G\) may depend on \(z_i\) through a rotation \(\theta'_{j,\ell}\) with \(\ell\in S_I^j\) and \(a(\pi_{jr}(\ell))=i\); then \(Q_iG\ne0\) is possible and nothing follows for \(D_i\).

**8.5.** With \(p_k=p_{k-1}\) the same steps give \(\Pr(t_i>0,\ D_i\ge\beta)\le\Pr(D_i\ge\beta/2)\) and, after adding over \(i\), the bound \(K\) for the expected number of layers with \(t_i>0\) and \(D_i\ge\beta\). This is the bound (2.2) again and says nothing about the probability, which must be small. The factor \(\lambda\) of the geometric law is what makes it small. The price is that the coefficient \(1\) has the small probability \(p_m\), and this is made up for by the number \(s\) of the layers.

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026

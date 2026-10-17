# From packing to a power saving

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md) shows that a family of step-disjoint intervals of activity at least \(b\) has at most \(C_1(N/b)^{4/3}\) members. The heart of OpenAI's proof [OpenAI-HL] is that the constant \(C_1\) can be replaced by any \(\xi>0\) once \(N/b\) is large enough. This lesson states that packing theorem, shows how a fixed small constant at one fixed scale yields a power saving, by an induction over the number of points, and reduces the packing theorem to a statement about batches. Lessons 4 to 12 prove that statement by contradiction; the last section fixes the assumptions they work under.

Throughout, configurations are generic in the sense of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md), and intervals, activity and batches are as in [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md).

## 1. The packing theorem

**Theorem 1.1** (uniform activity packing; OpenAI). For every \(\xi>0\) there is \(Q_\xi<\infty\) with the following property. For every generic configuration of \(N\) points, every rank \(k\), and every integer \(1\le b\le N\) with \(N/b\ge Q_\xi\), every family of step-disjoint intervals of activity at least \(b\) has at most \(\xi(N/b)^{4/3}\) members.

The quantifiers matter: \(Q_\xi\) depends only on \(\xi\), not on the configuration, the rank or \(b\). The proof gives no formula for \(Q_\xi\).

## 2. Restricting a block

**Lemma 2.1** (restriction). Let \(I\) be an interval of the rank-\(k\) sweep of a generic configuration \(P\), let \(A\) be its set of active points, and let \(B\) be the set of points outside \(A\) that are marked at the first state of \(I\). Put \(r=k-|B|\). Then \(A\), as a configuration, is generic, and at every state \(s\) of \(I\) the marked points of \(A\) are its \(r\) points with the smallest values of \(\varphi_s\). The number of switches of the rank-\(k\) sweep of \(P\) at steps of \(I\) is at most \(S_r(A)\).

*Proof.* Conditions (G1)–(G4) for \(A\) concern its points and segments, which are points and segments of \(P\). A point outside \(A\) does not change membership during \(I\), so at every state \(s\) of \(I\) the points of \(B\) are marked and the other points outside \(A\) are not; hence \(M_k(s)\cap A\) has \(k-|B|=r\) elements. Since \(M_k(s)\) consists of the first \(k\) points in the order of \(\varphi_s\), its intersection with \(A\) consists of the first \(r\) points of \(A\) in that order.

A switch of \(P\) at a step of \(I\) exchanges two points \(u,v\), both active, so both in \(A\), at the slope \(\sigma_{uv}\) of their segment. The set of the first \(r\) points of \(A\) is \(M_k\cap A\) on both sides of \(\sigma_{uv}\), and it changes there; so the step of the sweep of \(A\) that crosses \(\sigma_{uv}\) is a switch of rank \(r\). Different switches of \(P\) have different slopes and give different switches of \(A\). \(\square\)

## 3. The induction

**Proposition 3.1** (packing gives a power; OpenAI). Suppose that for every \(\eta>0\) there is \(Q_\eta<\infty\) such that the conclusion of Theorem 1.1 holds with \(\xi=\eta\). Then there are absolute constants \(\varepsilon>0\) and \(C\) such that \(S_k(P)\le CN^{4/3-\varepsilon}\) for every generic configuration \(P\) of \(N\ge1\) points and every rank \(k\).

*Proof.* *Choice of the scale.* Put \(\eta=(4\cdot2^{4/3})^{-1}\) and fix an integer \(q\ge\max\{4,Q_\eta\}\). Put
\[
\varepsilon=\frac{\log2}{2\log q},\qquad\beta=\frac43-\varepsilon>0 .
\]
For \(n\ge0\) let \(F(n)\) be the largest number of switches of a sweep of a generic configuration of exactly \(n\) points, over all ranks; \(F(0)=F(1)=0\), and \(F(n)\le\binom n2\) by Lemma 2.1(d) of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md). Choose \(C\ge1\) with \(F(n)\le Cn^\beta\) for \(1\le n<4q\). We show \(F(N)\le CN^\beta\) for \(N\ge4q\) by induction on \(N\).

*Blocks.* Let \(N\ge4q\) and put \(d=\lfloor N/q\rfloor\) and \(b=d-1\). Then
\[
\frac N{2q}\le\frac Nq-2\le b<\frac Nq ,
\]
since \(N\ge4q\); so \(b\ge2\), \(N/b>q\ge Q_\eta\), and \(N/b\le2q\). Divide the rank-\(k\) sweep of a configuration \(P\) of \(N\) points into consecutive intervals, its *blocks*: starting at the first state, end a block at the first state at which its activity reaches \(b\), and start the next block there; the last block may have activity less than \(b\). Every step lies in exactly one block. Just before the last step of a completed block its activity is at most \(b-1\), and a step changes the membership of at most two points, so a block has at most \(b+1=d\le N/q\) active points. The completed blocks are step-disjoint intervals of activity at least \(b\), so there are at most
\[
\eta\Bigl(\frac Nb\Bigr)^{4/3}\le\eta(2q)^{4/3}=\frac{q^{4/3}}4
\]
of them, and with the last block at most \(q^{4/3}/2\) blocks, since \(q^{4/3}\ge4\).

*Counting switches.* Let the blocks have \(t_1,t_2,\dots\) active points. By Lemma 2.1 the switches in the \(j\)th block number at most \(F(t_j)\), and \(t_j\le N/q<N\). By the induction hypothesis, and since \(F(0)=0\),
\[
\begin{aligned}
S_k(P)&\le\sum_jF(t_j)\le C\sum_jt_j^\beta\\
&\le C\,\frac{q^{4/3}}2\Bigl(\frac Nq\Bigr)^\beta=\frac C2\,q^{\varepsilon}N^\beta\\
&=\frac C{\sqrt2}N^\beta\le CN^\beta .
\end{aligned}
\]
This holds for every rank, so \(F(N)\le CN^\beta\). \(\square\)

The constant \(q\) depends on \(Q_\eta\), for which the proof of Theorem 1.1 gives no value; so \(\varepsilon\) has no explicit value either.

**Proof of Theorems A and B, given Theorem 1.1.** Theorem 1.1 provides the hypothesis of Proposition 3.1, which is Theorem B. Theorem A follows from the case \(k=N/2\), by Lemmas 1.1 and 2.2 of [Halving lines and rank sweeps](halving-lines-and-rank-sweeps.md). \(\square\)

## 4. Reduction to batches

For a generic configuration, a rank \(k\) and an integer \(a\ge1\), let \(R_k(P,a)\) be the number of batches produced by Lemma 2.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md) when \(\lceil d/2\rceil=a\); that is, the greedy batches of endpoint distance exactly \(a\), starting at the first state. The proof of Theorem 6.1 there gives
\[
R_k(P,a)\le41\Bigl(\frac Na\Bigr)^{4/3}.
\]

**Theorem 4.1** (batch packing). For every \(\xi>0\) there is \(Q<\infty\) such that \(R_k(P,a)\le\xi(N/a)^{4/3}\) for every generic configuration of \(N\) points, every rank \(k\) and every integer \(a\ge1\) with \(N/a\ge Q\).

**Lemma 4.2.** Theorem 4.1 implies Theorem 1.1.

*Proof.* Let \(\xi>0\), take \(Q\) from Theorem 4.1 for \(\xi'=\xi/(2\cdot16^{4/3})\), and put \(Q_\xi=Q\). Let \(N/b\ge Q\) and consider step-disjoint intervals of activity at least \(b\). By Lemma 1.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md) they split into at most two subfamilies of intervals with endpoint distance at least \(d\) in a sweep of some rank, where \(d=\lfloor b/4\rfloor\) if \(b\ge4\) and \(d=1\) if \(b\le3\). By Lemma 2.1 there, each subfamily has at most \(R_{k'}(P,a)\) members, with \(a=\lceil d/2\rceil\). In both cases \(b/16\le a\le\max(b/4,1)\le b\), so \(N/a\ge N/b\ge Q\), and
\[
\begin{aligned}
R_{k'}(P,a)&\le\xi'\Bigl(\frac Na\Bigr)^{4/3}\\
&\le\xi'\,16^{4/3}\Bigl(\frac Nb\Bigr)^{4/3}\\
&=\frac\xi2\Bigl(\frac Nb\Bigr)^{4/3}.
\end{aligned}
\]
Adding the two subfamilies proves Theorem 1.1. \(\square\)

## 5. The extremal sequence

Lessons 4 to 12 prove Theorem 4.1 by contradiction. Suppose it fails. Then there are \(\xi_0>0\) and, for \(n=1,2,\dots\), generic configurations \(P_n\) of \(N_n\) points, ranks \(k_n\) and integers \(a_n\ge1\) with
\[
\begin{gathered}
\frac{N_n}{a_n}\longrightarrow\infty,\\
\xi_0\Bigl(\frac{N_n}{a_n}\Bigr)^{4/3}\le R_n\le41\Bigl(\frac{N_n}{a_n}\Bigr)^{4/3},
\end{gathered}
\]
where \(R_n=R_{k_n}(P_n,a_n)\). We keep only the batches: in configuration \(n\), the \(R_n\) consecutive batches of the rank-\(k_n\) sweep, each losing \(a_n\) points and gaining \(a_n\) points, with their \(a_n^2\) exchange edges each. We write \(N,a,R\) for \(N_n,a_n,R_n\) when the index is clear, and
\[
E_*=Ra^2,\qquad M=aN ;
\]
so \(E_*\) is the number of exchange edges. Then
\[
\begin{gathered}
E_*^3=R^3a^6\asymp\Bigl(\frac Na\Bigr)^4a^6=a^2N^4,\\
\frac{E_*}M=\frac{Ra}N\asymp\Bigl(\frac Na\Bigr)^{1/3}\longrightarrow\infty ,
\end{gathered}
\]
where \(\asymp\) means bounded above and below by positive constants depending only on \(\xi_0\). In particular \(N_n\to\infty\). The contradiction will be reached in [Boundary activity](boundary-activity.md); every later choice of subsequence is a subsequence of this sequence, and constants called \(C\) may depend on \(\xi_0\) but never on \(n\).

## 6. Exercises

**6.1** (easy). In the proof of Proposition 3.1, why must the induction hypothesis cover all ranks, and not only the rank \(k\) being bounded?

**6.2** (medium). Show that the proof of Proposition 3.1 uses its hypothesis for the single value \(\eta=(4\cdot2^{4/3})^{-1}\). Deduce that a bound of the form \(C_1(N/b)^{4/3}(\log(N/b))^{-c}\), for some fixed \(c>0\), on the number of step-disjoint intervals of activity at least \(b\) would also give a power saving, and express \(\varepsilon\) in terms of \(C_1\) and \(c\).

**6.3** (easy). Check the inequality \(N/(2q)\le N/q-2\) for \(N\ge4q\), and explain why \(b\ge2\).

## 7. Solutions

**6.1.** A block is restricted to its active points \(A\) and the rank becomes \(r=k-|B|\), which depends on the block (Lemma 2.1). The bound \(F(t_j)\) must therefore hold for all ranks of configurations with \(t_j\) points.

**6.2.** The proof fixes \(\eta=(4\cdot2^{4/3})^{-1}\) and uses only that intervals with \(N/b\ge q\) number at most \(\eta(N/b)^{4/3}\). The logarithmic bound gives this as soon as \(C_1(\log q)^{-c}\le\eta\), since \(N/b\ge q\); choose the least integer \(q\ge4\) with \(\log q\ge(C_1/\eta)^{1/c}\). The induction then gives \(\varepsilon=\log2/(2\log q)\), which is about \(\tfrac12\log2\,(\eta/C_1)^{1/c}\): a power saving, small when \(c\) is small. The difficulty in the halving-line problem is to prove any bound of the form \(o((N/b)^{4/3})\) at all.

**6.3.** \(N/q-2\ge N/(2q)\) is equivalent to \(N/(2q)\ge2\), that is, \(N\ge4q\). Then \(b\ge N/(2q)\ge2\).

## References

- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Sections 2 and 8. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026

# Rank coordinates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The packing estimate is proved by contradiction, through limits of configurations. Euclidean positions are a poor tool for such limits: the configurations of the extremal sequence of [From packing to a power saving](from-packing-to-a-power-saving.md) can be distorted arbitrarily. OpenAI's idea [OpenAI-HL, Section 3] is to label each point of the plane by *ranks*: for each time window \(J\) of the sweep, a smoothed fraction \(r_J\) of a family of convex chains of the window lying below the point. These labels take values in \([0,1]\), so limits exist; two windows give a coordinate system of the plane; crossings between two windows sit on a grid of mesh \(1/M\) in the corresponding coordinates; and rank coordinates have small total variation along the edges. This lesson constructs the labels in one configuration and proves these four properties.

We work in one configuration of the extremal sequence: a generic configuration of \(N\) points, a rank, and \(R\) consecutive batches, each exchanging \(a\) lost points for \(a\) gained points through \(a^2\) exchange edges, with \(M=aN\).

## 1. Times, windows and directions

Give the \(i\)th batch the *time* \((i-\frac12)/R\). A *window* is a dyadic interval \(J=[j2^{-m},(j+1)2^{-m})\subseteq[0,1]\), closed on the right when \((j+1)2^{-m}=1\). The batches of \(J\) are those with time in \(J\); they are consecutive, and their exchange edges are the *edges of \(J\)*. For a nonempty window, its *slope span* runs from the state just before its first batch to the state just after its last batch. By Lemma 3.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md), every edge slope lies strictly inside the span of its batch, and disjoint windows have spans with disjoint interiors. Since \(R\to\infty\) along the extremal sequence, each fixed window is nonempty in all late configurations.

For \(t\in(0,1)\), the batch \(i=1+\lfloor Rt\rfloor\) has \(t\) in its time cell \([(i-1)/R,i/R)\). Let \(\varsigma(t)\) be the mean of the slopes of its two endpoint states. A *line of direction \(t\)* is a line of slope \(\varsigma(t)\). If fixed times and windows are separated by positive gaps, then in all late configurations their batches are separated by further batches, and the directions and spans have the same strict order as the times.

Let \(S_J\) be the number of distinct endpoints of edges of \(J\): the points whose membership differs between the endpoint states of at least one batch of \(J\). By Lemma 4.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md),
\[
\operatorname{cr}(J)\le2a^2S_J^2 ,
\]
where \(\operatorname{cr}(J)\) is the number of crossing pairs of edges of \(J\); the edges of \(J\) are partitioned into at most \(aS_J\) convex chains; and all edges of the configuration are partitioned into at most \(aN=M\) convex chains and into at most \(M\) concave chains.

## 2. Smoothed ranks

Fix a nonempty window \(J\) and a convex chain partition of its edges into at most \(aS_J\le M\) chains. Extend each chain to a convex piecewise affine function on \(\mathbb R\): on the left by a ray whose slope lies strictly between the left end of the span of \(J\) and the slope of the first edge, and on the right by a ray whose slope lies strictly between the slope of the last edge and the right end of the span. Add affine functions with slopes inside the span until there are exactly \(M\) functions \(g_{J,1},\dots,g_{J,M}\). All their slopes lie in a closed interval \([\ell_J,u_J]\) inside the open span of \(J\).

Consider the finitely many points where an edge of \(J\) crosses an edge not in \(J\). Such a point lies on the graph of the chain containing its \(J\)-edge, and on no other edge of \(J\), by (G4). Choosing the slopes of the rays and the translates of the added affine functions to avoid these finitely many points, we arrange that through each of them passes exactly one of the \(M\) graphs.

Let \(\Phi(u)=1/(1+e^{-u})\), a continuous, strictly increasing function from \(\mathbb R\) onto \((0,1)\). For \(\epsilon_J>0\) put
\[
r_J(x,y)=\frac1M\sum_{i=1}^M\Phi\Bigl(\frac{y-g_{J,i}(x)}{\epsilon_J}\Bigr).
\]
As \(\epsilon_J\to0\), each summand tends to the indicator of \(y>g_{J,i}(x)\) at every point off the graph of \(g_{J,i}\). Choose \(\epsilon_J\) so small that at each of the finitely many crossing points above, the summands of the graphs not through the point differ from these indicators by at most \(1\) in total. For an empty window, let the \(g_{J,i}\) be any \(M\) affine functions and \(\epsilon_J=1\); statements about finitely many fixed windows are made in configurations where they are nonempty.

**Lemma 2.1** (rank slots). Let \(X\) be a point where an edge of \(J\) crosses an edge not in \(J\), and let the graph through \(X\) be the \(i\)th from below among the \(M\) graphs at the first coordinate of \(X\). Then \(|r_J(X)-i/M|\le2/M\).

*Proof.* Exactly \(i-1\) of the other graphs pass below \(X\); the graph through \(X\) contributes \(\Phi(0)\in(0,1)\); and the error of the others is at most \(1\). So \(Mr_J(X)\) lies between \(i-2\) and \(i+1\). \(\square\)

## 3. Level graphs and the coordinate homeomorphism

For fixed \(x\), the function \(y\mapsto r_J(x,y)\) is continuous and strictly increasing, with limits \(0\) and \(1\). So for \(0<v<1\) the level set \(r_J=v\) is the graph of a function \(g_{J,v}\), the *level graph*. The function \((v,x)\mapsto g_{J,v}(x)\) is continuous: if \(v_m\to v\) and \(x_m\to x\), then \(g_{J,v_m}(x_m)\) is bounded, because \(r_J(x',y)\to0\) or \(1\) as \(y\to\mp\infty\) uniformly for \(x'\) in a compact set, and every limit point \(y\) of it has \(r_J(x,y)=v\), so \(y=g_{J,v}(x)\).

**Lemma 3.1** (chord slopes). For \(x<x'\) and \(0<v<1\),
\[
\begin{aligned}
\ell_J(x'-x)&\le g_{J,v}(x')-g_{J,v}(x)\\
&\le u_J(x'-x).
\end{aligned}
\]

*Proof.* Each \(g_{J,i}\) has slopes at most \(u_J\), so \(g_{J,i}(x+h)\le g_{J,i}(x)+u_Jh\) for \(h>0\), and moving from \((x,y)\) to \((x+h,y+u_Jh)\) does not decrease any summand of \(r_J\). Applied at \((x,g_{J,v}(x))\), this gives \(r_J(x',g_{J,v}(x)+u_J(x'-x))\ge v\), hence the upper bound. The lower bound is analogous, with \(\ell_J\). \(\square\)

Say that a window \(A\) *precedes* a disjoint window \(B\) if \(A\) lies to the left of \(B\) in \([0,1]\). Then the span of \(A\) lies below that of \(B\), so \(u_A<\ell_B\).

**Proposition 3.2** (rank charts). Let \(A\) precede \(B\), both nonempty. Then
\[
(r_A,r_B):\mathbb R^2\longrightarrow(0,1)^2
\]
is a homeomorphism. Along an \(A\)-level graph, \(r_B\) decreases strictly as \(x\) increases; along a \(B\)-level graph, \(r_A\) increases strictly.

*Proof.* For \(v,w\in(0,1)\), the function \(D(x)=g_{A,v}(x)-g_{B,w}(x)\) satisfies \(D(x')-D(x)\le(u_A-\ell_B)(x'-x)\) for \(x<x'\), by Lemma 3.1. So it is continuous, strictly decreasing, and tends to \(+\infty\) and \(-\infty\) at the two ends. It has exactly one zero \(x^*\), and \((x^*,g_{A,v}(x^*))\) is the unique point with \(r_A=v\) and \(r_B=w\). So the map is a continuous bijection. Its inverse is continuous: given \(\eta>0\), \(D(x^*-\eta)>0>D(x^*+\eta)\), and by the continuity of level graphs in \(v,w\) these strict inequalities persist for nearby levels, whose zero therefore lies within \(\eta\) of \(x^*\).

Along the \(A\)-level graph, each difference \(g_{A,v}(x)-g_{B,i}(x)\) has chord slopes at most \(u_A-\ell_B<0\), so every summand of \(r_B\) decreases strictly. Along a \(B\)-level graph, each \(g_{B,w}(x)-g_{A,i}(x)\) has chord slopes at least \(\ell_B-u_A>0\). \(\square\)

**Proposition 3.3** (monotone coordinates). Let \(A\) precede \(B\), and let \(C\) be a window disjoint from both. The function \(F_C=r_C\circ(r_A,r_B)^{-1}\) on \((0,1)^2\) is continuous and strictly monotone in each coordinate, with signs, for the first and the second coordinate, \((+,-)\) if \(C\) precedes \(A\), \((+,+)\) if \(C\) lies between \(A\) and \(B\), and \((-,+)\) if \(B\) precedes \(C\).

*Proof.* Moving right along a \(B\)-level graph fixes \(r_B\) and increases \(r_A\); moving right along an \(A\)-level graph fixes \(r_A\) and decreases \(r_B\) (Proposition 3.2). Along a curve with chord slopes in \([\ell,u]\), the summand of \(r_C\) for \(g_{C,i}\) increases strictly if \(\ell>u_C\) and decreases strictly if \(u<\ell_C\). If \(C\) precedes \(A\), both level graphs have slopes above \(u_C\), so \(r_C\) increases in both moves: it increases with \(r_A\) and decreases with \(r_B\). If \(C\) lies between, \(r_C\) increases along \(B\)-level graphs and decreases along \(A\)-level graphs: it increases in both coordinates. If \(B\) precedes \(C\), both level graphs have slopes below \(\ell_C\): \(r_C\) decreases with \(r_A\) and increases with \(r_B\). \(\square\)

## 4. Crossings sit on a grid

**Proposition 4.1** (crossing grid). Let \(I\) and \(J\) be disjoint nonempty windows, and give each point where an edge of \(I\) crosses an edge of \(J\) the mass \(M^{-2}\), placed at \((r_I,r_J)\) of the point. For every continuous \(f\ge0\) on \([0,1]^2\), the total integral of \(f\) is at most
\[
\frac1{M^2}\sum_{i,j=1}^Mf\Bigl(\frac iM,\frac jM\Bigr)+\omega_f(3/M),
\]
where \(\omega_f\) is the modulus of continuity of \(f\).

*Proof.* Order the \(M\) functions of each family pointwise: let \(\bar g_{I,i}(x)\) be the \(i\)th smallest of the values \(g_{I,1}(x),\dots,g_{I,M}(x)\). Order statistics of functions with chord slopes in \([\ell_I,u_I]\) are continuous with chord slopes in \([\ell_I,u_I]\), being formed by maxima and minima. Suppose \(I\) precedes \(J\); then \(\bar g_{I,i}-\bar g_{J,j}\) is strictly decreasing, and each pair of sorted graphs meets at most once. A crossing point \(X\) lies on exactly one graph of each family, by the construction of Section 2; if this graph is the \(i\)th of \(I\) and the \(j\)th of \(J\) at the first coordinate of \(X\), then \(X\) lies on \(\bar g_{I,i}\) and on \(\bar g_{J,j}\). So different crossing points give different pairs \((i,j)\), and by Lemma 2.1 the pair \((r_I,r_J)(X)\) is within \(2/M\) in each coordinate of \((i/M,j/M)\). Replacing \(f\) at the point by its value at the grid point costs at most \(\omega_f(3/M)\) per crossing, with at most \(M^2\) crossings. \(\square\)

So every weak limit of these crossing masses, as \(M\to\infty\), is at most Lebesgue measure on the unit square: the Riemann sums converge to \(\int f\).

## 5. Small variation along the edges

For a function \(f\) and a segment \(e\), let \(\operatorname{Var}_e(f)\) be the total variation of \(f\) along \(e\).

**Proposition 5.1** (variation). For every window \(J\), summing over all exchange edges \(e\) of the configuration,
\[
\sum_e\operatorname{Var}_e(r_J)\le2M .
\]

*Proof.* Write \(\Phi(u)\) as the probability that a random variable \(\theta\) with distribution function \(\Phi\) is less than \(u\). Then \(r_J(x,y)\) is the average over \(i\) and the expectation over \(\theta\) of the indicator that \((x,y)\) lies above the translated graph \(g_{J,i}+\epsilon_J\theta\). Take a concave chain \(\Lambda\) of the partition of all edges into at most \(M\) concave chains (Section 1), the graph of a concave function \(f\). For each \(i\) and \(\theta\), the difference \(f-g_{J,i}-\epsilon_J\theta\) is concave on the domain of \(\Lambda\), so the set where it is positive is an interval, and the indicator of lying above the translated graph has variation at most \(2\) along \(\Lambda\), counting all changes of sign, including at tangencies. Averaging, \(r_J\) has variation at most \(2\) along \(\Lambda\). Variation is additive over the edges of a chain, and there are at most \(M\) chains. \(\square\)

## 6. Labels

List all windows as \(J_1,J_2,\dots\) and give the cube \(Z=[0,1]^{\mathbb N}\) the metric
\[
d(z,z')=\sum_{j\ge1}2^{-j}|z_j-z'_j| .
\]
It is a compact metric space: a sequence in \(Z\) has a subsequence converging in every coordinate, by a diagonal argument, and convergence in every coordinate is convergence in \(d\). The *label* of a point \(q\) of the plane is \(z(q)=(r_{J_j}(q))_{j\ge1}\). For a window \(J=J_j\) write \(z_J=z_j\).

For an edge \(e\), let \(\operatorname{osc}_ez\) be the diameter of \(z(e)\) in \(Z\). It is at most \(\sum_j2^{-j}\operatorname{Var}_e(r_{J_j})\), so by Proposition 5.1
\[
\sum_e\operatorname{osc}_ez\le2M .
\]
In the extremal sequence \(E_*/M\to\infty\), where \(E_*=Ra^2\) is the number of edges. Hence for every fixed \(\rho>0\), the number of edges with \(\operatorname{osc}_ez>\rho\) is at most \(2M/\rho\), a vanishing fraction of all edges. Along almost every edge, the label is almost constant.

## 7. Exercises

**7.1** (easy). Let \(M=1\) and \(g_{J,1}(x)=x\). Describe the level graphs of \(r_J\).

**7.2** (medium). Show that the \(i\)th order statistic of finitely many functions with chord slopes in \([\ell,u]\) has chord slopes in \([\ell,u]\).

**7.3** (medium). Let \(A\) precede \(B\). Show that along a line of slope \(s\) with \(u_A<s<\ell_B\), as \(x\) increases, \(r_A\) increases strictly and \(r_B\) decreases strictly. What are the two directions of change along a line of slope \(s<\ell_A\), and along a line of slope \(s>u_B\)?

## 8. Solutions

**7.1.** \(r_J(x,y)=\Phi((y-x)/\epsilon_J)\), so the level set \(r_J=v\) is the line \(y=x+\epsilon_J\Phi^{-1}(v)\): the level graphs are parallel translates of the single graph.

**7.2.** The maximum of functions with \(f(x')-f(x)\le u(x'-x)\) satisfies the same inequality, since each function does, and similarly the minimum and the lower bound. The \(i\)th smallest value equals \(\max_{|T|=i}\min_{k\in T}f_k\) over \(i\)-element sets \(T\).

**7.3.** Along the line \(y=y_0+sx\), the argument of the \(i\)th summand of \(r_A\) is \((y_0+sx-g_{A,i}(x))/\epsilon_A\), whose chord slopes are at least \((s-u_A)/\epsilon_A>0\); so each summand increases strictly. For \(r_B\) the chord slopes are at most \((s-\ell_B)/\epsilon_B<0\). For \(s<\ell_A\) both coordinates decrease strictly, and for \(s>u_B\) both increase strictly. In each case the forward displacement in the rank chart has a fixed sign in each coordinate, determined by the position of \(s\) relative to the two spans.

## References

- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026

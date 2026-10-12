# The tail and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By [Positivity on the half-gaps](positivity-on-the-half-gaps.md) the two sign conditions \(H_1\le T_k\) and \(H_2\ge0\) hold on \([0,89.5]\). This lesson proves them for all \(s\ge89.5\), by one argument for all the infinitely many remaining gaps. The normalized statement and the universal optimality of the triangular lattice follow.

- The sine product satisfies \(P(s)\ge0.68\,(s-m)^2\), where \(m\) is a zero nearest to \(s\) (Lemma 1.2).
- Beyond \(89.5\) the cardinal function \(p_i\) is the sine product times a rational function \(R_i\), formed from the entries at the nodes up to \(88\), plus a very small rest. The function \(\pm R_i\) is larger than \(0.002\) (Lemma 2.2); this uses ten computed inequalities (Proposition 2.1).
- Everything else in the slack function \(F_i\) is collected in a remainder \(Z_i\), which has a second derivative below \(0.0002\) and vanishes to second order at every node from \(91\) on (Section 3). So \(|Z_i(s)|\le0.0001\,(s-m)^2\), which is less than \(0.68\cdot0.002\,(s-m)^2\).
- Hence \(F_i\ge0\) on \([89.5,\infty)\) (Theorem 3.4), the normalized statement holds for every \(k\ge2.36\) (Theorem 4.1), and the triangular lattice is universally optimal (Theorem 4.2).

The lesson follows [OpenAI-T, Section 5, the part on the tail, and the tail inequalities of the finite certificate in Section 3].

## 1. A lower bound for the sine product

Recall \(P(s)=\prod_{a\in L}(2\sin\tfrac{\pi(s-a)}{12})^2\) with \(L=\{0,1,3,4,7,9\}\), and its set of real zeros \(\mathcal Z\), the integers congruent modulo \(12\) to an element of \(L\). Since \((2\sin x)^2=2-2\cos2x\),
\[
P(s)=\prod_{a\in L}\Bigl(2-2\cos\frac{\pi(s-a)}6\Bigr).
\]
The gaps between consecutive zeros are, modulo \(12\), the intervals \([0,1]\), \([1,3]\), \([3,4]\), \([4,7]\), \([7,9]\), \([9,12]\).

**Lemma 1.1.** Let \(c\) be the midpoint of a gap and \(\ell\) half its length. Then \(P(c)/\ell^2\) is

- \(12-8\sqrt2\) for the gaps \([0,1]\) and \([3,4]\);
- \(1\) for the gap \([1,3]\);
- \(\tfrac89(3+\sqrt2+\sqrt3+\sqrt6)\) for the gaps \([4,7]\) and \([9,12]\);
- \(9\) for the gap \([7,9]\).

All four numbers are larger than \(0.686\).

**Proof.** \(P\) has the period \(12\) and satisfies \(P(4-s)=P(s)\), because \(a\mapsto4-a\) permutes the residues of \(L\) modulo \(12\). So \(P(\tfrac72)=P(\tfrac12)\) and \(P(\tfrac{21}2)=P(-\tfrac{13}2)=P(\tfrac{11}2)\), and it is enough to compute \(P\) at \(\tfrac12\), \(2\), \(\tfrac{11}2\) and \(8\). Let
\[
\begin{gathered}
c_1=\cos\frac\pi{12}=\frac{\sqrt6+\sqrt2}4,\\
c_5=\cos\frac{5\pi}{12}=\frac{\sqrt6-\sqrt2}4 .
\end{gathered}
\]
Then \(c_1-c_5=\tfrac{\sqrt2}2\), \(c_1c_5=\tfrac14\), \(4-4c_1^2=2-\sqrt3\) and \(4-4c_5^2=2+\sqrt3\).

*At \(s=\tfrac12\).* The numbers \(s-a\) are \(\tfrac12,-\tfrac12,-\tfrac52,-\tfrac72,-\tfrac{13}2,-\tfrac{17}2\), and the cosines of \(\pi(s-a)/6\) are \(c_1,c_1,c_5,-c_5,-c_1,-c_5\). So
\[
\begin{aligned}
&P(\tfrac12)\\
&\ =(2-2c_1)^2(2-2c_5)\\
&\qquad\cdot(2+2c_5)^2(2+2c_1)\\
&\ =(2-2c_1)(2+2c_5)\\
&\qquad\cdot(4-4c_1^2)(4-4c_5^2)\\
&\ =4\,(1-c_1+c_5-c_1c_5)=3-2\sqrt2 .
\end{aligned}
\]
With \(\ell=\tfrac12\) this gives \(12-8\sqrt2\).

*At \(s=\tfrac{11}2\).* The numbers \(s-a\) are \(\tfrac{11}2,\tfrac92,\tfrac52,\tfrac32,-\tfrac32,-\tfrac72\), with the cosines \(-c_1,-\tfrac{\sqrt2}2,c_5,\tfrac{\sqrt2}2,\tfrac{\sqrt2}2,-c_5\). So
\[
\begin{aligned}
&P(\tfrac{11}2)\\
&\ =(2+2c_1)(2+\sqrt2)\\
&\qquad\cdot(2-\sqrt2)^2(4-4c_5^2)\\
&\ =2\,(2+2c_1)(2-\sqrt2)(2+\sqrt3)\\
&\ =(4+\sqrt6+\sqrt2)(2-\sqrt2)(2+\sqrt3),
\end{aligned}
\]
and multiplying out gives \(2\,(3+\sqrt2+\sqrt3+\sqrt6)\) (Exercise 6.2). With \(\ell=\tfrac32\) this gives the third value.

*At \(s=2\) and \(s=8\).* Here all cosines are \(\pm\tfrac12\) or \(\pm\tfrac{\sqrt3}2\), and \(P(2)=1\), \(P(8)=9\) (Exercise 6.1); in both cases \(\ell=1\).

Finally \(8\sqrt2<11.314\), so \(12-8\sqrt2>0.686\); the third value is larger than \(7\). \(\blacksquare\)

**Lemma 1.2.** Let \(s\) be real and \(m\in\mathcal Z\) a zero of \(P\) nearest to \(s\). Then
\[
P(s)\ge0.68\,(s-m)^2 .
\]

**Proof.** Let \(m'\) be the neighbour of \(m\) in \(\mathcal Z\) on the side of \(s\), and \(c\) the midpoint of \(m\) and \(m'\); then \(s\) lies in the closed interval \(I\) between \(m\) and \(c\). On \(I\) let
\[
\varphi(s)=\frac{P(s)}{(s-m)^2}
\]
for \(s\ne m\), and \(\varphi(m)=Q_m\), where \(Q_m>\tfrac74\) is the number with \(P(m+u)=Q_mu^2(1+O(u))\). The function \(\varphi\) is continuous and positive on \(I\). We show that \(\log\varphi\) is concave on \(I\). Then \(\varphi\ge\min(\varphi(m),\varphi(c))\) on \(I\), and by Lemma 1.1 both numbers are larger than \(0.68\).

Let \(a_0\in L\) be the residue of \(m\) modulo \(12\) and \(u=s-m\). The factor of \(P\) with index \(a_0\) is \((2\sin\tfrac{\pi u}{12})^2\), so
\[
\begin{aligned}
\log\varphi={}&\log\frac{4\sin^2(\pi u/12)}{u^2}\\
&+\sum_{a\ne a_0}\log\Bigl(2\sin\frac{\pi(s-a)}{12}\Bigr)^2 .
\end{aligned}
\]
For \(a\ne a_0\) the factor does not vanish on \(I\), and the second derivative of \(\log\sin^2\theta\) with respect to \(\theta\) is \(-2/\sin^2\theta<0\); so each term of the sum is concave. For the first term, with \(\alpha=\pi/12\) and \(u\ne0\),
\[
\begin{aligned}
&\frac{d^2}{du^2}\log\frac{\sin^2(\alpha u)}{u^2}\\
&\quad=\frac2{u^2}-\frac{2\alpha^2}{\sin^2(\alpha u)}\le0,
\end{aligned}
\]
because \(|\sin(\alpha u)|\le|\alpha u|\). The term is continuous at \(u=0\), so it is concave on \(I\). \(\blacksquare\)

## 2. The rational part

Fix \(k\ge2.36\). Let \(\ell_1,\ell_2\) be the lists of Theorem 3.1 of [Exact interpolation](exact-interpolation.md), with the entries \(C_i\), \(c_{i,n}\), \(d_{i,n}\), let \(p_i\) be their cardinal functions, \(H_1,H_2\) the functions of Corollary 3.2 there, and \(F_i=\sigma_iH_i+\delta_iT_k\) the slack functions, with \(\sigma_1=-1\), \(\sigma_2=1\), \(\delta_1=1\), \(\delta_2=0\). Let \(s_0=89.5\).

The largest element of \(\mathcal N_0\) below \(s_0\) is \(88\), and the next node is \(91\). For \(s>88\) let
\[
\begin{aligned}
R_i(s)={}&C_i+\sum_{n\le88}\frac{c_{i,n}}{(s-n)^2}\\
&+\sum_{n\le88}\frac{d_{i,n}}{s-n},
\end{aligned}
\]
the sums running over the elements \(n\) of \(\mathcal N_0\) up to \(88\),
and let \(p_i^{\mathrm{hi}}\) be the cardinal function of the list that has the entries \(c_{i,n},d_{i,n}\) of \(\ell_i\) at the nodes \(n\ge91\) and \(0\) elsewhere. By the definition of cardinal functions, for \(s>88\)
\[
p_i(s)=P(s)\,R_i(s)+p_i^{\mathrm{hi}}(s),
\]
first for \(s\) outside the nodes and then for all \(s>88\) by continuity.

The corresponding function for the reference list \(\ell_i^{\mathrm{ref}}=X_iq(k)\) is linear in \(q(k)\). Let \(\rho_{i,C}\), \(\rho_{i,(c,n)}\), \(\rho_{i,(d,n)}\) be the rows of the matrix \(\sigma_iX_i\) that belong to the entries \(C\), \(c_n\), \(d_n\); each is a row of ten numbers. For consecutive endpoints \(K<J\) and a row \(l\) let \([l]_{K,J}\) be the bracket of the lesson on positivity, and
\[
\eta(l)=\min\bigl(0,\ [l]_{K,J}\bigr).
\]

**Proposition 2.1.** For \(i=1,2\) and each of the five pairs of consecutive endpoints \(K<J\), the number
\[
\begin{aligned}
&[\rho_{i,C}]_{K,J}+\frac1{s_0}\,\eta\Bigl(\sum_{n\le88}\rho_{i,(d,n)}\Bigr)\\
&\quad+\sum_{n\le88}\frac{\eta(\rho_{i,(c,n)})}{(s_0-n)^2}\\
&\quad+\sum_{n\le88}\frac{n\,\eta(\rho_{i,(d,n)})}{s_0\,(s_0-n)}
\end{aligned}
\]
is larger than \(0.0021\). The sums run over the \(46\) elements \(n\) of \(\mathcal N_0\) up to \(88\).

**Verification.** These are ten inequalities between explicitly defined numbers. They were established by a computation in ball arithmetic, as in the lessons on the reference lists and on positivity. The values, rounded downwards, are for \(i=1\) and \(i=2\):

- \(K=2.36\): \(0.002455\) and \(0.002267\);
- \(K=2.65\): \(0.002980\) and \(0.003113\);
- \(K=3.2\): \(0.003721\) and \(0.004256\);
- \(K=4\): \(0.004432\) and \(0.005317\);
- \(K=6\): \(0.005371\) and \(0.006681\).

Section 5 prints the program. \(\blacksquare\)

**Lemma 2.2.** For \(i=1,2\) and all \(s\ge s_0\),
\[
\sigma_i\,R_i(s)>0.002 .
\]

**Proof.** Let \(R_i^{\mathrm{ref}}\) be defined like \(R_i\) with the entries of the reference list at \(C\) and at the nodes up to \(88\). Then
\[
\begin{aligned}
\sigma_iR_i^{\mathrm{ref}}(s)={}&\rho_{i,C}\,q(k)\\
&+\sum_{n\le88}\frac{\rho_{i,(c,n)}\,q(k)}{(s-n)^2}\\
&+\sum_{n\le88}\frac{\rho_{i,(d,n)}\,q(k)}{s-n}.
\end{aligned}
\]
Since
\[
\frac1{s-n}=\frac1s+\frac n{s\,(s-n)},
\]
the terms with simple poles are \(\tfrac1s\) times \((\sum_n\rho_{i,(d,n)})\,q(k)\), plus the sum of the terms \(\tfrac n{s(s-n)}\rho_{i,(d,n)}\,q(k)\). Choose consecutive endpoints with \(K\le k\le J\), or \(K=6\) and \(J=\infty\) if \(k\ge6\). By Lemma 1.1 of the lesson on positivity, \(l\,q(k)\ge[l]_{K,J}\ge\eta(l)\) for every row \(l\). The factors \(\tfrac1s\), \(\tfrac1{(s-n)^2}\) and \(\tfrac n{s(s-n)}\) are nonnegative and decrease for \(s\ge s_0\). Since \(\eta(l)\le0\), the product of \(\eta(l)\) with such a factor is at least its value at \(s_0\). So \(\sigma_iR_i^{\mathrm{ref}}(s)\) is at least the number of Proposition 2.1, hence larger than \(0.0021\).

The lists \(\ell_i\) and \(\ell_i^{\mathrm{ref}}\) have the same entry \(C\), and their other entries differ by less than \(2\cdot10^{-8}\) in total (Theorem 3.1 of the lesson on exact interpolation). For \(s\ge s_0\) and \(n\le88\) we have \(s-n\ge1.5\), so \(\tfrac1{(s-n)^2}\) and \(\tfrac1{s-n}\) are less than \(1\). Hence \(|R_i(s)-R_i^{\mathrm{ref}}(s)|<2\cdot10^{-8}\), and \(\sigma_iR_i(s)>0.0021-2\cdot10^{-8}>0.002\). \(\blacksquare\)

## 3. The remainder

Let \(j\) denote the index other than \(i\). For \(s>88\) let
\[
\begin{aligned}
Z_i(s)={}&\sigma_i\bigl(p_i^{\mathrm{hi}}(s)+K_{p_j}(s)\bigr)\\
&+\delta_i\,T_k(s).
\end{aligned}
\]
Since \(H_i=p_i+K_{p_j}\) and \(p_i=PR_i+p_i^{\mathrm{hi}}\), for \(s>88\)
\[
F_i(s)=\sigma_i\,P(s)\,R_i(s)+Z_i(s).
\]

**Lemma 3.1.** The entries of the two lists at the nodes from \(91\) on satisfy
\[
\sum_{i=1}^2\ \sum_{n\ge91}\bigl(|c_{i,n}|+|d_{i,n}|\bigr)<2.4\cdot10^{-7}.
\]

**Proof.** The interpolation system says, at every node \(n\),
\[
\begin{gathered}
(c_{1,n},d_{1,n})=(S\ell_2)_n+(\mathcal JT_k)_n,\\
(c_{2,n},d_{2,n})=(S\ell_1)_n .
\end{gathered}
\]
Let \(w\) be the sum of the absolute values of all entries \(c_{i,n},d_{i,n}\) of the two lists, and \(c=|C_1|+|C_2|\). Then \(w+c<5\) by Theorem 3.1 of the lesson on exact interpolation, and \(c<0.02\) by Corollary 4.2 of the lesson on the reference lists, because the exact lists have the same extra entries as the reference lists. By the tail bound ([The transformed function at distant nodes](the-transformed-function-at-distant-nodes.md), Theorem 3.2), applied to the two lists together, the terms with \(S\) contribute at most \(U_{91}(w,c)\le U_{91}(5,0.02)\). In
\[
\begin{aligned}
&U_{91}(5,0.02)=800\cdot5.02\,\frac{e^{-63.7}}{1-e^{-0.70}}\\
&\quad+5.3\Bigl(\frac{12.7}{91}+0.04\Bigr)\frac{e^{-17.017}}{1-e^{-0.187}}
\end{aligned}
\]
the first term is less than \(10^{-23}\). In the second, \(5.3\,(12.7/91+0.04)<0.9517\), \(e^{-17.017}<4.08\cdot10^{-8}\) and \(1-e^{-0.187}>0.1705\), so it is less than \(2.28\cdot10^{-7}\). The terms with \(\mathcal JT_k\) contribute at most \(c_*\sum_{n\ge91}e^{-2.36(n-1)}<10^{-89}\), with the bound for \(\mathcal JT_k\) and the constant \(c_*<1.327\) of the lesson on exact interpolation. \(\blacksquare\)

**Lemma 3.2.** For \(i=1,2\) and all \(s\ge s_0\),
\[
|Z_i''(s)|<0.0002 .
\]

**Proof.** The three parts of \(Z_i\) are estimated separately.

*The part \(p_i^{\mathrm{hi}}\).* Its list has \(C=0\), and the sum \(W\) of the absolute values of its entries is less than \(2.4\cdot10^{-7}\) by Lemma 3.1. By Corollary 2.3 of the lesson on cardinal functions, \(|(p_i^{\mathrm{hi}})''(s)|\le36\,\pi^2\,W\), which is less than \(8.53\cdot10^{-5}\).

*The part \(K_{p_j}\).* By Theorem 3.1 of the lesson on distant nodes with the order \(2\), and with \(w=5\), \(c=0.02\) as bounds for the list \(\ell_j\),
\[
\begin{aligned}
&|K_{p_j}''(s)|\le3\,(3\pi)^2\cdot180.5\,e^{-0.70s}\\
&\quad+1.25\,(1.32\pi)^2\Bigl(\frac{12.7}s+0.04\Bigr)e^{-0.187s}.
\end{aligned}
\]
Both terms decrease in \(s\). At \(s=s_0\) the first is less than \(10^{-22}\). In the second, \((1.32\pi)^2<17.2\), \(12.7/89.5+0.04<0.182\) and \(e^{-0.187\cdot89.5}<5.39\cdot10^{-8}\), so it is less than \(2.2\cdot10^{-7}\).

*The part \(T_k\).* \(T_k''(s)=k\,e^{-k(s-1)}\). For \(s\ge s_0\) this decreases in \(s\), and in \(k\) for \(k\ge1/(s-1)\); so it is at most \(2.36\,e^{-2.36\cdot88.5}<10^{-90}\).

The sum of the three bounds is less than \(8.6\cdot10^{-5}\). \(\blacksquare\)

**Lemma 3.3.** For every node \(m\ge91\) and \(i=1,2\), \(Z_i(m)=Z_i'(m)=0\).

**Proof.** \(F_i(m)=F_i'(m)=0\) by Corollary 3.2 of the lesson on exact interpolation. The function \(R_i\) is smooth near \(m\), because its poles are at most \(88\), and \(P\) has a double zero at \(m\). So \(PR_i\) and its derivative vanish at \(m\), and \(Z_i=F_i-\sigma_iPR_i\). \(\blacksquare\)

These zeros come from the exact interpolation at the node \(m\), not from the smallness of the entries at the high nodes. The single terms of \(Z_i\) do not vanish at \(m\).

**Theorem 3.4.** For every \(k\ge2.36\), \(i=1,2\) and all \(s\ge89.5\), \(F_i(s)\ge0\).

**Proof.** Let \(s\ge s_0\). There is a zero \(m\in\mathcal Z\) nearest to \(s\) with \(m\ge91\): for \(s=s_0\), which has the same distance from \(88\) and from \(91\), take \(m=91\), and for \(s>s_0\) every nearest zero is at least \(91\). The interval between \(s\) and \(m\) lies in \([s_0,\infty)\). By Lemma 3.3 and Lemma 1.2 of [Quotients on the half-gaps](quotients-on-the-half-gaps.md), \(Z_i(s)=(s-m)^2\,\mathcal D_mZ_i(s)\), and \(|\mathcal D_mZ_i(s)|\) is at most half the maximum of \(|Z_i''|\) between \(m\) and \(s\). With Lemma 3.2,
\[
|Z_i(s)|\le0.0001\,(s-m)^2 .
\]
By Lemma 1.2 and Lemma 2.2, and because \(P\ge0\),
\[
\sigma_i\,P(s)\,R_i(s)\ge0.68\cdot0.002\,(s-m)^2 .
\]
Since \(0.68\cdot0.002=0.00136>0.0001\), we get \(F_i(s)=\sigma_iP(s)R_i(s)+Z_i(s)\ge0\). \(\blacksquare\)

## 4. The theorem

**Theorem 4.1.** For every real \(k\ge2.36\) the normalized statement \((\mathrm N_k)\) of [Shells and Gaussian duality](shells-and-gaussian-duality.md) holds. More precisely, there are entire functions \(H_1,H_2\), real on the real axis, such that \(f(x)=e^{-\pi hs}H_1(s)\), with \(s=b|x|^2\), is an admissible radial function on \(\mathbb R^2\) with \(\widehat f(x)=e^{-\pi hs}H_2(s)\), such that \(H_1(s)\le T_k(s)\) and \(H_2(s)\ge0\) for all \(s\ge0\), and such that at every node \(n\in\mathcal N\)
\[
\begin{gathered}
H_1(n)=T_k(n),\qquad H_1'(n)=T_k'(n),\\
H_2(n)=0,\qquad H_2'(n)=0 .
\end{gathered}
\]

**Proof.** The functions are those of Corollary 3.2 of the lesson on exact interpolation. The two inequalities hold on \([0,89.5]\) by Theorem 3.2 of the lesson on positivity and on \([89.5,\infty)\) by Theorem 3.4. \(\blacksquare\)

**Theorem 4.2.** Let \(A\) be the triangular lattice of covolume one in the plane, and \(g\colon(0,\infty)\to[0,\infty)\) a completely monotone function. Then for every configuration \(\mathcal C\) of density one in the plane
\[
E_g(\mathcal C)\ge E_g(A),
\]
where \(E_g\) is the energy for the interaction \(g\) of the squared distance.

**Proof.** By Theorem 4.1 the hypothesis of Corollary 4.2 of the lesson on shells and Gaussian duality holds. \(\blacksquare\)

So the triangular lattice is universally optimal among the configurations of density one in the plane. The proof given in this course consists of the following parts.

- The linear programming bound and its sharp case ([Energy, density and the linear programming bound](energy-density-and-the-linear-programming-bound.md)), the passage from Gaussians to completely monotone interactions ([Completely monotone interactions](completely-monotone-interactions.md)), and the reduction to the normalized statement (the lesson on shells and Gaussian duality).
- The construction of the functions \(H_1,H_2\): cardinal functions, their Fourier transforms, the interpolation system and its exact solution (the lessons from the sine product to exact interpolation).
- The two sign conditions (the lessons on the quotients and on positivity, and this lesson).

Three statements in this chain are finite sets of inequalities between explicitly defined numbers and were established by computations with rigorous error bounds: Proposition 4.1 of the lesson on the reference lists, Proposition 3.1 of the lesson on positivity, and Proposition 2.1 above. Their programs are printed in the lessons. All other steps are proved in the lessons or in the lessons they name.

## 5. The program

The following lines continue the programs of [The reference lists](the-reference-lists.md), Section 5, and of the lesson on positivity, Section 4; they are to be appended to them. They compute the ten numbers of Proposition 2.1.

```
# Continuation of the two programs: a lower bound for the rational
# part of the cardinal functions of the reference lists beyond 89.5.
s0 = dec("89.5")
low = [n for n in N0 if n <= 88]
for K, J in zip(ENDS, ENDS[1:]):
    for X, sign in ((X1, -1), (X2, 1)):

        def row(r):
            return [sign * X[r, c] for c in range(10)]

        def eta(v):
            # the smaller of 0 and the lower bound for v.q(k)
            return arb(0).min(box_low(v, K, J))

        dsum = [sum((sign * X[col_d[n], c] for n in low), arb(0))
                for c in range(10)]
        v = box_low(row(COL_C), K, J) + eta(dsum) / s0
        for n in low:
            v += eta(row(col_c[n])) / (s0 - n) ** 2
            v += n * eta(row(col_d[n])) / (s0 * (s0 - n))
        assert v > dec("0.0021")
        print(K, 1 if sign < 0 else 2, round(float(v.mid()), 6))
```

The program prints, for each \(K\) and for \(i=1,2\), the value listed in Section 2.

## 6. Exercises

**6.1.** Compute \(P(2)\) and \(P(8)\) from the product with the cosines.

**6.2.** Verify
\[
\begin{aligned}
&(4+\sqrt6+\sqrt2)(2-\sqrt2)(2+\sqrt3)\\
&\quad=2\,(3+\sqrt2+\sqrt3+\sqrt6).
\end{aligned}
\]

**6.3.** Which zero of \(P\) is nearest to \(s\) for \(89.5\le s\le92\), and which for \(92\le s\le94.5\)? What is the largest distance of a real number from \(\mathcal Z\)?

**6.4.** The sign conditions on \([0,89.5]\) were proved by one computation for each half-gap. Why is this method not used beyond \(89.5\), and which properties of the functions make the argument of this lesson possible there and not near \(0\)?

## 7. Solutions

**6.1.** At \(s=2\) the numbers \(s-a\) are \(2,1,-1,-2,-5,-7\), and the cosines of \(\pi(s-a)/6\) are \(\tfrac12,\tfrac{\sqrt3}2,\tfrac{\sqrt3}2,\tfrac12,-\tfrac{\sqrt3}2,-\tfrac{\sqrt3}2\). The factors \(2-2\cos\) are \(1\), \(2-\sqrt3\), \(2-\sqrt3\), \(1\), \(2+\sqrt3\), \(2+\sqrt3\), with product \(1\). At \(s=8\) the numbers \(s-a\) are \(8,7,5,4,1,-1\), with the cosines \(-\tfrac12,-\tfrac{\sqrt3}2,-\tfrac{\sqrt3}2,-\tfrac12,\tfrac{\sqrt3}2,\tfrac{\sqrt3}2\); the factors are \(3\), \(2+\sqrt3\), \(2+\sqrt3\), \(3\), \(2-\sqrt3\), \(2-\sqrt3\), with product \(9\).

**6.2.** First
\[
\begin{aligned}
&(2-\sqrt2)(2+\sqrt3)\\
&\quad=4+2\sqrt3-2\sqrt2-\sqrt6 .
\end{aligned}
\]
Multiplying this by \(4\), by \(\sqrt6\) and by \(\sqrt2\) gives
\[
\begin{gathered}
16+8\sqrt3-8\sqrt2-4\sqrt6,\\
4\sqrt6+6\sqrt2-4\sqrt3-6,\\
4\sqrt2+2\sqrt6-4-2\sqrt3 .
\end{gathered}
\]
The sum is \(6+2\sqrt3+2\sqrt2+2\sqrt6\).

**6.3.** The zeros near \(90\) are \(88,91,93,96\). For \(89.5\le s\le92\) the nearest zero is \(91\), with a tie with \(88\) at \(89.5\) and with \(93\) at \(92\). For \(92\le s\le94.5\) it is \(93\). The longest gaps have length \(3\), so the largest distance from \(\mathcal Z\) is \(1.5\).

**6.4.** Beyond \(89.5\) there are infinitely many gaps, so a computation for each is impossible. The argument of this lesson needs that everything except the sine product times the rational part is small compared with \(0.68\cdot0.002\,(s-m)^2\). This holds far from the origin: the transformed functions and the target decay exponentially, and the entries of the lists at the high nodes are tiny. Near \(0\) the transformed function and the target are of the same size as the other terms, so there the functions have to be computed.

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 5. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026

# Stationarity alone does not control joint localization

[The general core proof in Lesson 68](core-central-transition-bounds.md) gives bounded positive central transitions and a small weighted stationarity defect. The joint-density input (68.16) concerns distance to a larger-center function. The following original construction proves that the numerical transition bounds and stationarity estimate alone do not imply that input.

This is one fixed countable commutative probability algebra. It is not asserted to be a Jones core, and its densities are not asserted to be dimensions of actual relative Følner projections. It therefore does not refute Popa's general rounding theorem. It identifies additional information that a proof of that theorem must use. The motivating human source is Sorin Popa, *Classification of amenable subfactors of type II*, [DOI 10.1007/BF02392646](https://doi.org/10.1007/BF02392646), Theorem 4.2.2, printed pp. 213–214. The model and all calculations below are authored here.

We use ordinary countable sums, positive conditional expectations on an atomic probability algebra, and the scalar triangle inequality. The Hilbert-space statement uses only the conditional-expectation pairing and the elementary formula for an adjoint; its full calculation is given below. No direct-integral or graph classification result is invoked.

## One fixed joint algebra and its two centers

Let

\[
\begin{gathered}
\mathcal E=\mathbb N_0\times\{0,1\},\\
D_0=\ell^\infty(\mathcal E),\\
\mu(j,0)=\frac{2^{-j}}3,\\
\mu(j,1)=\frac{2^{-j-1}}3,\\
\tau(t)=\sum_{j,\epsilon}\mu(j,\epsilon)t(j,\epsilon).
\end{gathered}
\tag{69.1}
\]

Here \(\mathbb N_0\) denotes the nonnegative integers. Every atom has positive weight. Since the two geometric series have sums 2 and 1, respectively, \(\mu(\mathcal E)=1\), and \(\tau\) is faithful and normal.

Give atom \((j,0)\) the smaller label \(s_j\), and atom \((j,1)\) the smaller label \(s_{j+1}\). Give both atoms the larger label \(r_j\). Let \(Z_s,Z_r\subset D_0\) be the functions of those labels. Their joint algebra is \(D_0\): intersecting the projections of the two labels isolates each atom. The label measures are

\[
\begin{gathered}
\tau(s_0)=\frac13,\\
\tau(s_k)=\frac{2^{1-k}}3\quad(k\geq1),\\
\tau(r_j)=2^{-j-1}\quad(j\geq0).
\end{gathered}
\tag{69.2}
\]

Write \(P_0=E_{Z_r}\) and \(Q_0=E_{Z_s}\). Their explicit formulas, for bounded \(t\in D_0\), are

\[
\begin{gathered}
\begin{aligned}
(P_0t)(r_j)&=\frac23t(j,0)\\
&\quad+\frac13t(j,1),
\end{aligned}\\
(Q_0t)(s_0)=t(0,0),\\
\begin{aligned}
(Q_0t)(s_k)&=\frac12t(k,0)\\
&\quad+\frac12t(k-1,1),
\end{aligned}
\\ k\geq1.
\end{gathered}
\tag{69.3}
\]

Each formula is the weighted average of its indicated fiber. Direct substitution of (69.1)–(69.2) proves preservation of \(\tau\). These maps are positive, unital and normal, and they fix their respective subalgebras and are bimodular over them. They are the faithful tracial conditional expectations. Truncation extends them to positive \(L^1\) densities.

**Proposition 69.1 — all the transition bounds hold at fixed index parameter.** Take \(d=4\), \(b_d=13\), and \(\kappa=1\). Then \(P_\kappa=P_0\), \(Q_\kappa=Q_0|_{Z_r}\), both marginals of \(\kappa\) are 1, and for every \(t\in(D_0)_+\),

\[
\begin{gathered}
\frac14\leq\kappa\leq\frac{13}4,\\
t\leq3P_0(t)\leq4P_\kappa(t)\leq13P_0(t),\\
t\leq2Q_0(t)\leq4Q_0(t).
\end{gathered}
\tag{69.4}
\]

For every finite orthogonal projection family \((x_l)\) with sum at most 1, both sums of projected support projections are at most 2, hence at most \(\lfloor d\rfloor=4\).

**Proof.** On a larger fiber the two atomic probabilities are \(2/3\) and \(1/3\), so its average is at least \(1/3\) times either nonnegative input value. On a smaller fiber the probabilities are \(1/2,1/2\), except for the single-atom endpoint, where the probability is 1. This proves (69.4) atom by atom. Every larger fiber has two atoms and every smaller fiber has at most two. At most two disjoint input projections can meet one fiber, proving the support bound. The marginal identities for \(\kappa=1\) are immediate. The two comparisons between \(P_\kappa\) and \(P_0\) in (68.9) also hold. \(\square\)

Put \(T=Q_0P_0|_{Z_s}\). For \(s\in Z_s\), (69.3) gives

\[
\begin{gathered}
\begin{aligned}
(Ts)(s_0)&=\frac23s(s_0)\\
&\quad+\frac13s(s_1),
\end{aligned}\\
\begin{aligned}
(Ts)(s_k)&=\frac12s(s_k)\\
&\quad+\frac16s(s_{k+1})\\
&\quad+\frac13s(s_{k-1}),
\end{aligned}
\\ k\geq1.
\end{gathered}
\tag{69.5}
\]

**Lemma 69.2 — the stationarity operator has additional symmetry.** The map \(T\) is positive, unital, normal and \(\tau\)-preserving. As an operator on \(L^2(Z_s,\tau)\), it is a self-adjoint positive contraction.

**Proof.** The first properties follow from those of \(P_0,Q_0\). Their \(L^2\) contraction follows on each fiber from the scalar weighted Cauchy–Schwarz inequality and then summation. For \(s\in Z_s\) and \(r\in Z_r\), direct summation or expectation adjointness gives

\[
\langle P_0s,r\rangle_\tau
=\langle s,Q_0r\rangle_\tau.
\tag{69.6}
\]

Thus \(Q_0|_{Z_r}=(P_0|_{Z_s})^*\), and \(T=P_0^*P_0\). It is self-adjoint, \(\langle s,Ts\rangle_\tau=\|P_0s\|_2^2\geq0\), and its norm is at most 1. Bounded truncations extend the pairing to \(L^2\). \(\square\)

## An escaping family is almost stationary

For each integer \(L\geq2\), define the bounded positive smaller-center function

\[
\begin{gathered}
f_L(s_k)=2^k\quad(0\leq k<L),\\
f_L(s_k)=0\quad(k\geq L),\\
c_L=\tau(f_L)=\frac{2L-1}{3},\\
\zeta_L=f_L/c_L.
\end{gathered}
\tag{69.7}
\]

The underlying algebra, measures and maps stay fixed as \(L\) varies. Only this finite-support density changes. It has \(\tau(\zeta_L)=1\).

**Proposition 69.3 — exact stationarity defect.** For every \(L\geq2\),

\[
\begin{gathered}
\|f_L-Tf_L\|_1=\frac49,\\
\|\zeta_L-T\zeta_L\|_1=\frac4{3(2L-1)},\\
\frac4{3(2L-1)}\longrightarrow0.
\end{gathered}
\tag{69.8}
\]

**Proof.** On \(s_0\), \(Tf_L=4/3\), so \(f_L-Tf_L=-1/3\). For \(1\leq k\leq L-2\), substitute \(2^k\) into (69.5): the three terms are \(2^{k-1}\), \(2^k/3\), and \(2^{k-1}/3\), whose sum is \(2^k\). This interval is empty at \(L=2\).

At the upper two labels,

\[
\begin{gathered}
(Tf_L)(s_{L-1})=\frac23\,2^{L-1},\\
(Tf_L)(s_L)=\frac13\,2^{L-1}.
\end{gathered}
\tag{69.9}
\]

All later values vanish. Multiplying the three nonzero absolute differences by the measures in (69.2) gives \(1/9,2/9,1/9\). Their sum is \(4/9\). The mass formula in (69.7) follows from endpoint mass \(1/3\) and \(L-1\) interior contributions \(2/3\). Divide by that mass to obtain (69.8). \(\square\)

The cancellation in the interior is precise: the geometric density balances both neighboring terms. Stationarity only records the remaining endpoint imbalance.

## Every larger-center approximation stays separated

**Theorem 69.4 — stationarity and all the bounds do not imply joint localization.** In the single fixed model (69.1), for every \(L\geq2\),

\[
\begin{gathered}
\Delta(f):=\inf\{\|f-b\|_{L^1(D_0,\tau)}:\\
b\in L^1(Z_r,\tau)_+\},\\
\Delta(f_L)=\frac L6,\\
\Delta(\zeta_L)=\frac L{2(2L-1)}>\frac14.
\end{gathered}
\tag{69.10}
\]

The infimum is attained. In particular, even self-adjoint positive \(T\), \(\kappa=1\), faithful normal expectations, the bounds (68.5)/(68.9), and finite partition overlap at most 2 do not yield a joint-distance bound tending to zero with the stationarity defect.

**Proof.** On larger label \(r_j\), the two smaller values are \(x=f_L(s_j)\) and \(y=f_L(s_{j+1})\). Put \(w=2^{-j}/3\), so the two atomic weights are \(w,w/2\). For any \(b_j\geq0\), the triangle inequality gives

\[
\begin{aligned}
C_j(b_j)&=w|x-b_j|\\
&\quad+\frac w2|y-b_j|,\\
C_j(b_j)&\geq\frac w2|x-b_j|\\
&\quad+\frac w2|y-b_j|,\\
C_j(b_j)&\geq\frac w2|x-y|.
\end{aligned}
\tag{69.11}
\]

The choice \(b_j=x\) attains equality. Thus the minimum on a larger fiber is \((w/2)|x-y|\).

For \(0\leq j\leq L-2\), the difference is \(2^j\), so this minimum is \(1/6\). At \(j=L-1\), the two values are \(2^{L-1},0\), giving the same minimum \(1/6\). All later costs are zero. Summing the nonnegative terms proves the global lower bound \(L/6\), for every positive \(L^1\) function \(b\).

It is attained by the finite-support larger-center function \(b_L(r_j)=f_L(s_j)\). This function is bounded and integrable, since \(\tau(b_L)=L/2\). Scaling \(b_L\) by \(c_L\), and using the same lower bound for all scaled candidates, proves the second line of (69.10). Finally \(L/[2(2L-1)]>1/4\), whereas (69.8) tends to zero. All hypotheses in the last assertion were checked in 69.1–69.2. \(\square\)

**Corollary 69.5 — no uniform modulus follows from these data.** There is no function \(\omega:[0,\infty)\to[0,\infty)\), with \(\omega(a)\to0\) as \(a\downarrow0\), such that all positive mass-one densities in this fixed model satisfy

\[
\Delta(\zeta)\leq\omega(\|\zeta-T\zeta\|_1).
\tag{69.12}
\]

**Proof.** Substitute \(\zeta_L\). The right side tends to zero by (69.8); the left side is greater than \(1/4\) by (69.10), a contradiction. \(\square\)

For comparison, the ordinary larger conditional density is

\[
\begin{gathered}
\beta_L=P_0f_L,\\
0\leq j\leq L-2:\\
\beta_L(r_j)=\frac43\,2^j,\\
\beta_L(r_{L-1})=\frac23\,2^{L-1},\\
\beta_L(r_j)=0\quad(j\geq L),\\
J_L:=\|f_L-P_0f_L\|_{L^1(D_0,\tau)},\\
\frac{J_L}{c_L}=\frac{2L}{3(2L-1)}>\frac13.
\end{gathered}
\tag{69.13}
\]

The last equality follows by summing \(2/9\) on every one of the \(L\) active larger fibers. The conditional density preserves mass, but it is not the positive \(L^1\) minimizer in 69.4.

![A fixed two-center atomic path: interior cancellation hides persistent joint distance.](figures/stationarity-and-joint-localization.svg)

*Figure 69.1. Each solid edge is one joint atom; its exact weight appears beside it. All fibers contain at most two atoms. The upper drawing shows the first part of the infinite fixed model, rather than a finite cyclic replacement. The lower panels give exact values at \(L=2,4,8,16\) and the limits in (69.8)/(69.10). The stationarity defect tends to zero while the best larger-center distance tends to \(1/4\). Layout is schematic; there is no claim of a Jones-core realization. [Editable figure source](figures/stationarity-and-joint-localization.py). Source problem: Popa4.2.2, pp.213–214.*

## Examples and exercises with complete solutions

**Example 69.1 — two active smaller labels.** At \(L=2\), \(f_2=(1,2,0,\ldots)\) has mass 1. Its stationarity defect is \(4/9\), its best joint distance to the larger center is \(1/3\), and its distance to \(P_0f_2\) is \(4/9\). The stationarity and conditional-distance equality at this single parameter is incidental.

**Example 69.2 — eight active smaller labels.** At \(L=8\), \(c_8=5\). The mass-one density has stationarity defect \(4/45\), best joint distance \(4/15\), and conditional joint distance \(16/45\). Increasing \(L\) improves stationarity but preserves the separation in 69.4.

### Exercise 69.1 — introductory

Check that the smaller label measures in (69.2) sum to 1.

**Solution.** The endpoint has measure \(1/3\); the remaining geometric sum is \((2/3)\sum_{k\geq1}2^{-k}=2/3\). Their sum is 1. The larger measures sum to \((1/2)\sum_{j\geq0}2^{-j}=1\).

### Exercise 69.2 — introductory

Derive the two probabilities on a larger fiber and the two probabilities at smaller label \(s_3\).

**Solution.** On \(r_j\), divide \(2^{-j}/3\) and \(2^{-j-1}/3\) by their sum to obtain \(2/3,1/3\). At \(s_3\), the incident atoms are \((3,0)\) and \((2,1)\); both have measure \(2^{-3}/3\), giving probabilities \(1/2,1/2\).

### Exercise 69.3 — intermediate

For \(L=4\), compute the mass and all three relative quantities in (69.8), (69.10), and (69.13).

**Solution.** The mass is \(c_4=7/3\). The relative stationarity defect is \(4/21\), the optimal relative joint distance is \(2/7\), and the relative distance to \(P_0f_4\) is \(8/21\). The unnormalized optimal distance is \(4/6=2/3\).

### Exercise 69.4 — intermediate

Verify detailed balance between adjacent smaller labels and deduce that \(T\) preserves mass.

**Solution.** For \(k\geq1\), the transition coefficients in the function formula (69.5) are \(1/6\) forward and \(1/3\) backward. Their measure-weighted values are \((2^{1-k}/3)(1/6)=2^{-k}/9\) and \((2^{-k}/3)(1/3)=2^{-k}/9\). At \(k=0\), they are \((1/3)(1/3)=1/9\) and \((1/3)(1/3)=1/9\). The diagonal terms preserve their own weight, and each row sum is 1; summing the balanced columns gives \(\tau(Ts)=\tau(s)\) for bounded \(s\).

### Exercise 69.5 — advanced

Why does the minimizing larger density \(b_L\) have mass \(L/2\), whereas \(P_0f_L\) has mass \((2L-1)/3\)? Does this affect 69.4?

**Solution.** Each active larger label contributes \(2^{-j-1}2^j=1/2\) to \(\tau(b_L)\), so its mass is \(L/2\). The expectation \(P_0\) preserves \(\tau\), giving the other mass. 69.4 minimizes over all positive integrable larger densities, without imposing a mass constraint. Its lower bound therefore also holds on any smaller class that imposes mass preservation; allowing every positive density makes the separation stronger.

### Exercise 69.6 — advanced

Explain the precise consequence for the open general-core localization argument. Which assertion about actual cores has been proved false here?

**Solution.** No assertion about actual Jones cores or actual projection dimensions has been refuted. The model proves that a deduction of (68.16) from only the transition inequalities, finite support overlap, and the scalar size of the stationarity defect is invalid. A complete general-core proof must use further information from the actual projections or construct a different sufficient localization input. Larger-factor rounding58 and all universal core transition proofs68 remain unchanged.

---

Authored by GPT-6.1 Sol (OpenAI), Ultra reasoning, October 2026. Original exposition CC0 1.0. Author self-check. The course remains in development.

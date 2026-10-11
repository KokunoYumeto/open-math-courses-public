# Iterated pullbacks and the cost of descent

*Written by GPT-6 Astra (OpenAI), Ultra mode in Codex, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Repeated application of a deterministic map changes both the set of admissible inputs and the size of its complement. This lesson studies that change quantitatively. It also shows how an absorbing small-input region affects iteration: once the map becomes the identity there, it contributes no further movement and no further time.

The Collatz application combines three pieces of mathematics. Finite fibres transport an arbitrary exceptional target back to the source. A recursion retains the exact power of the exceptional count, together with its logarithmic cost. Bounds on the same stopped trajectories then turn the amount of descent into a graded time estimate. The result reaches the target \(n^\alpha\), including the closed exponent \(\alpha\), with one exceptional count and simultaneous clock and height bounds.

Prerequisites are the [reverse product and integer fibre arguments](NT-COLLATZ-34.md#a-landing-and-a-time-force-one-odd-count), the [full-entropy envelope estimate](NT-COLLATZ-35.md#retaining-the-prefactor-uniformly-as-the-tolerance-shrinks), and [exceptional sets and stopped orbit chains](NT-COLLATZ-36.md). A basic reference is Idris Ali Shaik's *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, with its accompanying stopped-map and graded-clock construction. The arguments below preserve that construction while retaining the individual time costs, logarithmic factors and exact behaviour below the startup threshold.

## A total map with an absorbing small-input region

Use the shortcut map \(T\) and the constants
\[
 \lambda=\log_2 3,\quad a_0=\lambda/2,\quad
 g=1-a_0,\quad \rho=2^{-g},\quad \ell=\log2.
\]
As before,
\(I_M=[2^M,2^{M+1})\cap\mathbb N\), and \(W_\eta\) consists of positive integers \(n\) satisfying
\[
 \rho^k n^{1-\eta}\le T^k(n)\le \rho^k n^{1+\eta}
 \quad(0\le k\le\lfloor\log_2n\rfloor).
 \tag{1}
\]
Fix \(a_0<r<1\) and \(0<\eta<r-a_0\). Choose \(M_0\ge2\) so that at every integer \(M\ge M_0\), with \(Y_M=2^{\lfloor rM\rfloor}\),
\[
 1<Y_M<2^M,\qquad M\le Y_M,\qquad
 \rho^M(2^{M+1})^{1+\eta}\le Y_M.
 \tag{2}
\]
These are explicit requirements on fixed parameters, not assumptions about unknown orbits. For example, it suffices to choose \(M_0\ge2\) with
\[
 rM_0\ge2,\qquad
 (r-a_0-\eta)M_0\ge2+\eta,\qquad
 2^{rM_0-1}\ge M_0.
 \tag{3}
\]
The last inequality persists at larger integers: the ratio of consecutive values of \(2^{rM-1}/M\) is \(2^r M/(M+1)>\sqrt3(2/3)>1\). Such an \(M_0\) exists because exponential growth dominates linear growth; the same ratio is bounded below by a constant greater than one for \(M\ge2\). The other two conditions plainly persist.

Put \(K=2^{M_0}\). For \(n<K\), define \(l(n)=0\). For \(n\ge K\), let \(m=\lfloor\log_2 n\rfloor\) and define \(l(n)\) to be the least \(k\le m\) with \(T^k(n)\le Y_m\), if one exists; otherwise set \(l(n)=0\). Define
\[
 F(n)=T^{l(n)}(n),\qquad
 W^*=W_\eta\cup[1,K),\qquad
 P(S)=W^*\cap F^{-1}(S).
 \tag{4}
\]
All sets in this lesson are subsets of the positive integers. The zero time in the nonexistence branch makes \(F\) a total function; it does not assert that a passage has occurred.

For \(n\in W^*\) with \(n\ge K\), (1) and (2) prove that passage exists by time \(m\). Hence the nonexistence branch is not used on these retained inputs. Moreover,
\[
 1\le l(n)\le m,\qquad F(n)\le Y_m\le n^r<n.
 \tag{5}
\]
For \(n<K\), instead, \(F(n)=n\) and \(l(n)=0\). The interval \([1,K)\) is therefore an absorbing region for this stopped map.

Define the repeated retained sets by
\[
 S_0=W^*,\qquad S_{R+1}=P(S_R).
 \tag{6}
\]
Induction gives the exact description
\[
 n\in S_R
 \quad\Longleftrightarrow\quad
 F^i(n)\in W^*\ \text{for every }0\le i\le R.
 \tag{7}
\]
In particular \(S_{R+1}\subseteq S_R\), and every \(S_R\) contains \([1,K)\). The recursion requires admissibility at each checkpoint, without treating different checkpoints as independent samples.

## Summing the time fibres before taking a common bound

The following finite estimate applies to arbitrary first passages, not only to inputs in \(W_\eta\).

**Proposition 1.** Let \(M\ge2\), let \(Y=2^q<2^M\) with \(q\ge1\), and assume \(M\le Y\). Let \(B\subseteq[1,Y]\cap\mathbb N\). The number of starts in \(I_M\) whose first passage to \(Y\) occurs by time \(M\) and lands in \(B\) is at most
\[
 |B|\sum_{h=1}^M
 \left(1+\left\lfloor
 \frac{(h-1)(2^{M+1}-1)}{3Y+4}
 \right\rfloor\right).
 \tag{8}
\]
Consequently it is at most
\[
 \frac{2^M|B|}{Y}
 \left(\frac{MY}{2^M}+\frac{YM(M-1)}{3Y+4}\right)
 \le \frac5{12}M^2\frac{2^M}{Y}|B|.
 \tag{9}
\]
Every bound remains valid on any restricted subset of the source shell.

**Proof.** The final crossing is even, since an odd shortcut step increases its positive input. At time \(h\), there have been at most \(h-1\) odd inputs. Each such input before passage is an odd integer greater than the even threshold \(Y\), hence at least \(Y+1\).

The [reverse-product bound](NT-COLLATZ-34.md#reversing-a-finite-path) therefore bounds the product defect by
\(\epsilon_h=(h-1)/(3Y+4)\).
Since \(h\le M\le Y\), it lies in \([0,1/3)\). The integer fibre theorem in that lesson bounds the number of sources for a fixed time and landing by
\(1+\lfloor\epsilon_h(2^{M+1}-1)\rfloor\).
Only landings in \((Y/2,Y]\) are possible; replacing \(B\) by its intersection with that band can only reduce its size. Distinct first-passage tags have disjoint fibres, proving (8).

Drop the floors and use \(\sum_{h=1}^M(h-1)=M(M-1)/2\). The coefficient of \(|B|\) is at most
\[
 M+\frac{(2^{M+1}-1)M(M-1)}{2(3Y+4)}
 \le M+\frac{2^M M(M-1)}{3Y+4}.
\]
Factoring \(2^M/Y\) gives the first expression in (9). Since \(Y\) and \(2^M\) are powers of two and \(Y<2^M\), \(Y/2^M\le1/2\). Thus the parenthesis is at most
\[
 M/2+M(M-1)/3=M^2/3+M/6\le5M^2/12,
\]
where the last step uses \(M\ge2\). Restricting the source never enlarges a fibre. ∎

![For M equal to six and threshold Y equal to sixteen, the separate integer fibre bounds at times one through six are one, three, five, eight, ten and thirteen. Their sum is forty; using the largest bound at all six times gives seventy-eight. These are upper bounds, not observed fibre sizes.](../figures/time-fibres.svg)

*Figure 1. The time-dependent bounds in (8), for one prescribed landing. Their sum retains information lost by using a single longest-horizon bound. Actual arithmetic and first-passage constraints may make the fibres smaller or empty.*

Shaik's arbitrary-target transport estimate has the coefficient \(5/2\) in the last expression of (9). His stage assumptions include \(M/(2Y)\le1/3\), which implies the hypothesis \(M\le Y\) used here. Thus (9) applies to the same stopped maps. The refinement changes a finite constant, not the density exponent by itself. Equation (8) retains the more precise integer information before a uniform coefficient is used.

## One pullback with its logarithmic cost

For \(S\subseteq\mathbb N_{>0}\), write
\(B_S(X)=|[1,X]\cap\mathbb N\setminus S|\), for integers \(X\ge1\).
The envelope estimate from the preceding lessons is
\[
 |I_M\setminus W_\eta|
 \le C^*2^M(M+1)^{-1/2}e^{-bM},\qquad
 b=I(\eta/\lambda),\quad D=b/\ell\in(0,1),
 \tag{10}
\]
where \(C^*=C_\eta^*\) is the explicit fixed-tolerance constant in
[Maximal parity deviations and orbit envelopes](NT-COLLATZ-35.md#retaining-the-prefactor-uniformly-as-the-tolerance-shrinks).
Put
\[
 v=\ell r/2,\qquad Z(p)=v^{\min(p,0)},\qquad \kappa=5/12.
\]

**Theorem 2.** Suppose \(C>0\), \(0<d\le D\), \(p\ge-1/2\), and
\[
 B_S(X)\le CX^{1-d}(1+\log X)^p\quad(X\ge1).
\]
Then
\[
 B_{P(S)}(X)
 \le \Pi(C,d,p)X^{1-rd}(1+\log X)^{p+2},
 \tag{11}
\]
where
\[
 \Pi(C,d,p)=
 \frac{\ell^{-(p+2)}
   \{2^{rdM_0}+C^*+\kappa\,2^dZ(p)C\}}
      {1-2^{rd-1}}.
 \tag{12}
\]
If \(S\) contains \([1,K)\), the term \(2^{rdM_0}\) may be deleted.

**Proof.** In a shell \(I_M\) with \(M\ge M_0\), failure of membership in \(P(S)\) means either failure of \(W^*\), or an actual first passage landing outside \(S\). The initial failure is bounded by (10). Proposition 1 bounds the latter number by
\[
 \kappa M^2\frac{2^M}{Y_M}B_S(Y_M)
 \le\kappa C M^2 2^M Y_M^{-d}(1+\log Y_M)^p .
\]
The floor gives \(Y_M^{-d}\le2^d e^{-rd\ell M}\).

For the logarithmic factor, \(rM\ge1\) implies
\(\lfloor rM\rfloor\ge rM/2\). Hence
\[
 v(1+M)\le1+\log Y_M\le1+M.
 \tag{13}
\]
For \(p\ge0\), use the upper inequality; for \(p<0\), use the lower one and reverse the inequality when taking the negative power. In both cases,
\((1+\log Y_M)^p\le Z(p)(1+M)^p\).
Thus the transported failure is bounded by
\(\kappa 2^d Z(p)C\,2^{(1-rd)M}(1+M)^{p+2}\).
Since \(rd\le D\) and \(p+2\ge3/2\), (10) bounds the initial failure by
\(C^*2^{(1-rd)M}(1+M)^{p+2}\).

For \(M<M_0\), the trivial count \(2^M\) is at most
\(2^{rdM_0}2^{(1-rd)M}(1+M)^{p+2}\).
If \(S\) contains \([1,K)\), these small shells are already in \(P(S)\): both the window condition and the identity branch hold, so their failure count is zero.

Let \(J=\lfloor\log_2 X\rfloor\). Because \(1-rd>0\) and \(p+2\ge0\),
\[
 \sum_{M=0}^J2^{(1-rd)M}(1+M)^{p+2}
 \le\frac{2^{(1-rd)J}(1+J)^{p+2}}{1-2^{rd-1}}.
\]
This follows by writing \(M=J-j\), bounding the polynomial factor by its value at \(J\), and summing a geometric series. Now \(2^J\le X\) and \(1+J\le(1+\log X)/\ell\). Summing the shell bounds proves (11)–(12), including the stated startup saving. ∎

The loss of two logarithmic powers has a transparent origin: the available times and the sizes of their fibres together contribute a quadratic factor in the source rank. Shaik's pure-power formulation pays such a polynomial factor from a strict exponent margin \(\chi<r\). Keeping it explicitly instead retains the endpoint exponent \(rd\).

## Iteration with an explicit dependence on depth

The initial global count retains the negative half-power in (10).

**Lemma 3.** The extended set \(W^*\) satisfies
\[
 B_{W^*}(X)\le A_0X^{1-D}(1+\log X)^{-1/2},\qquad
 A_0=\frac{C^*\sqrt{1+\ell}}{(1-e^b/2)^2}.
 \tag{14}
\]

**Proof.** Adding the startup interval only decreases the complement. Put \(J=\lfloor\log_2 X\rfloor\) and \(z=e^b/2<1\). Summation of (10), with \(j=J-M\), gives
\[
 \sum_{M=0}^J\frac{2^M e^{-bM}}{\sqrt{M+1}}
 \le \frac{2^J e^{-bJ}}{\sqrt{J+1}}
       \sum_{j=0}^J(j+1)z^j
 \le \frac{2^J e^{-bJ}}{\sqrt{J+1}(1-z)^2}.
\]
Indeed \((J+1)/(J-j+1)\le j+1\), and
\(\sqrt{j+1}\le j+1\).
Finally \(2^Je^{-bJ}\le X^{1-D}\) and
\(1+\log X\le(1+\ell)(J+1)\). ∎

For \(R\ge0\), set
\[
 d_R=Dr^R,\qquad p_R=2R-\tfrac12,\qquad
 A_{R+1}=
 \frac{\ell^{-(p_R+2)}
       \{C^*+\kappa\,2^{d_R}Z(p_R)A_R\}}
      {1-2^{rd_R-1}}.
 \tag{15}
\]

**Theorem 4.** The original sets from (6) satisfy
\[
 B_{S_R}(X)\le
 A_RX^{1-Dr^R}(1+\log X)^{2R-1/2}
 \quad(R\ge0,\ X\ge1).
 \tag{16}
\]
Every fixed \(S_R\) has natural density one. Moreover, if
\[
 Q=(1-2^{rD-1})^{-1},\qquad
 F_0=\kappa\,2^D v^{-1/2},\qquad
 L_*=1+Q(C^*+F_0),
\]
then
\[
 A_R+1\le(A_0+1)L_*^R\ell^{-(R^2+R/2)}.
 \tag{17}
\]

**Proof.** The case \(R=0\) is Lemma 3. Every \(S_R\) contains \([1,K)\), so the startup-saving version of Theorem 2 applies. It sends \(d_R\) to \(rd_R=d_{R+1}\) and \(p_R\) to \(p_R+2=p_{R+1}\), with exactly (15). This proves (16) by induction.

For (17), \(d_R\le D\), \(Z(p_R)\le v^{-1/2}\), and
\((1-2^{rd_R-1})^{-1}\le Q\). Hence
\[
 A_{j+1}+1
 \le L_*\ell^{-(2j+3/2)}(A_j+1).
\]
Multiply from \(j=0\) through \(R-1\), using
\(\sum_{j=0}^{R-1}(2j+3/2)=R^2+R/2\).

For fixed \(R\), \(Dr^R>0\). Dividing (16) by \(X\) tends to zero. To see the elementary domination explicitly, put \(u=\log X\) and choose an integer \(k> \max(p_R,0)\). The exponential series gives \(e^{d_Ru}\ge(d_Ru)^k/k!\), so a fixed power of \(1+u\) times \(e^{-d_Ru}\) tends to zero. ∎

The quantifier “fixed” matters. When \(R\) varies with \(X\), both the shrinking exponent and the increasing constant in (17) must be retained. A density-one assertion for each fixed depth cannot simply be substituted at a depth that grows with the initial input.

## Absorbing startup without multiplying its cost at every stage

Let \(n\in S_R\). Define
\[
 z_i=F^i(n),\qquad
 h_R=\sum_{i=0}^{R-1}l(z_i),\qquad
 G_R=\sum_{i=0}^{R-1}r^i=\frac{1-r^R}{1-r}.
\]
Set \(G_0=0\). Let \(\nu\) be the first index \(i<R\) with \(z_i<K\), or \(R\) if there is none.

**Proposition 5.** These checkpoints lie on one actual trajectory, and
\[
 z_R=T^{h_R}(n)\le\max\{K,n^{r^R}\},\qquad
 h_R\le G_\nu\log_2 n\le G_R\log_2 n.
 \tag{18}
\]
The shortcut height through \(h_R\) is at most \(n^{1+\eta}\).

**Proof.** Concatenating the actual iterates in (4) gives \(z_R=T^{h_R}(n)\). Before startup, (5) gives \(z_i\le n^{r^i}\) by induction. If startup is never reached, the same induction gives \(z_R\le n^{r^R}\). If it is reached, every subsequent checkpoint is the same integer below \(K\), proving the maximum in (18).

Only the stages \(i<\nu\) have positive lengths. They satisfy
\(l(z_i)\le\log_2z_i\le r^i\log_2n\). Summing proves the clock bound. The checkpoint values never increase, and the envelope on each executed block bounds its height by \(z_i^{1+\eta}\le n^{1+\eta}\). Zero-length blocks contribute no further states. ∎

The coarse inequality \(F(n)\le K n^r\) is also valid, but iterating it would repeatedly pay for a region in which the map has already stopped. Keeping the two actual branches proves the sharper maximum in (18). This argument applies to any map that contracts by a power above a threshold and is the identity below it.

## Shortened horizons for the original stopping times

A time bound is not a replacement for the stopping time itself. The next proposition produces an earlier guaranteed horizon but continues to use the original first passage \(l(n)\).

**Proposition 6.** For \(z\in W^*\), \(z\ge K\), let \(m=\lfloor\log_2 z\rfloor\), \(q=\lfloor rm\rfloor\), and
\[
 H(z)=\left\lceil\frac{(1+\eta)\log_2z-q}{g}\right\rceil .
\]
Then \(1\le l(z)\le H(z)\le m\), and
\[
 l(z)\le\min\{\log_2z,\ a\log_2z+c_r\},
 \qquad a=\frac{1+\eta-r}{g},\quad c_r=\frac{1+r}{g}+1.
 \tag{19}
\]
For the original \(R\)-stage path,
\[
 h_R\le
 \min\{G_\nu\log_2n,\ aG_\nu\log_2n+\nu c_r\}.
 \tag{20}
\]

**Proof.** The numerator defining \(H(z)\) is positive because \(z>2^q\). Condition (2) gives
\(2^{-gm}z^{1+\eta}\le2^q\), so its ceiling is at most the integer \(m\). The envelope is therefore valid at \(H(z)\), and
\(T^{H(z)}(z)\le2^{-gH(z)}z^{1+\eta}\le2^q\).
Minimality of the original first passage gives \(l(z)\le H(z)\).

Put \(u=\log_2z-m\in[0,1)\) and \(w=rm-q\in[0,1)\). Exactly,
\[
 (1+\eta)\log_2z-q
 =(1+\eta-r)\log_2z+ru+w.
\]
Use \(ru+w<r+1\) and \(\lceil t\rceil<t+1\) to obtain (19). The other bound in (19) is (5). Before startup, \(\log_2z_i\le r^i\log_2n\); after startup the lengths vanish. Sum the two valid bounds on those same lengths to get (20). ∎

Concatenating the longer \(H(z_i)\)-prefixes instead would generally change the next checkpoint. The proof does not do that: the map \(F\), the retained sets \(S_R\) and the actual path remain unchanged.

## Odd counts and three clocks on one path

Let \(s_R\) be the number of odd shortcut inputs among the first \(h_R\) transitions. The [exact affine formula](NT-COLLATZ-34.md#affine-coordinates-and-exact-composition) has a nonnegative additive term. On each positive-length block,
\[
 \frac{3^{s_i}z_i}{2^{l_i}}
 \le T^{l_i}(z_i)
 \le 2^{-gl_i}z_i^{1+\eta}.
\]
Taking logarithms and using \((1-g)\ell=\log3/2\) gives
\(s_i\le l_i/2+\eta\log z_i/\log3\).
Summing, and also using the reverse-product identity for the whole path, proves
\[
 s_R\le
 \min\left\{\frac{h_R}{2}+\frac{\eta G_\nu\log n}{\log3},\quad
 \frac{h_R+\log_2z_R-\log_2n}{\lambda}\right\}.
 \tag{21}
\]
These are two bounds on the same integer, so their minimum is available.

The ordinary Collatz time to \(z_R\) is exactly \(h_R+s_R\). Each inserted state is twice a shortcut output, so the ordinary height is at most \(2n^{1+\eta}\). If \(n\) is odd, complete the final even tail to the odd part of \(z_R\). The odd-return clock is \(s_R\); completing that tail adds no odd input. Its ordinary time would additionally include the length of the final even tail. These statements keep the endpoints and clocks distinct.

For \(R\ge1\), put \(\alpha=r^R\) and define
\[
 C_T=\frac{aG_R}{\ell},\qquad
 C_S=\frac{C_T}{2}+\frac{\eta G_R}{\log3},\qquad
 C_C=\frac{3C_T}{2}+\frac{\eta G_R}{\log3}.
 \tag{22}
\]
Whenever \(n\in S_R\) and \(n^\alpha\ge K\), (18), (20) and (21) give
\[
 z_R\le n^\alpha,\quad
 h_R\le C_T\log n+Rc_r,\quad
 s_R\le C_S\log n+\tfrac12Rc_r,\quad
 h_R+s_R\le C_C\log n+\tfrac32Rc_r .
 \tag{23}
\]
In particular the target exponent is exactly \(r^R\), not a larger exponent introduced to absorb a repeatedly charged startup constant.

## Choosing parameters for a prescribed descent

The coefficients in (22) separate into an amount-of-descent term and a positive tolerance cost. Write \(L_0=\log(4/3)=2g\ell\). Since \((1-r)G_R=1-\alpha\),
\[
\begin{aligned}
 C_T&=\frac{2(1-\alpha)}{L_0}+\frac{2\eta G_R}{L_0},\\
 C_S&=\frac{1-\alpha}{L_0}
       +\eta G_R\left(\frac1{L_0}+\frac1{\log3}\right),\\
 C_C&=\frac{3(1-\alpha)}{L_0}
       +\eta G_R\left(\frac3{L_0}+\frac1{\log3}\right).
\end{aligned}
\tag{24}
\]
These are identities at positive \(\eta\), not permission to set \(\eta=0\) in the exceptional-set estimate.

**Theorem 7.** Given \(0<\alpha<1\), \(\varepsilon>0\) and \(\beta>0\), there are fixed parameters \(R,r,\eta,M_0\), an explicit cutoff \(N\), and a set \(Q\) such that every \(n\in Q\) has one shortcut path to an integer at most \(n^\alpha\), with ordinary height at most \(n^{1+\beta}\), and
\[
\begin{aligned}
 h&<\left(\frac{2(1-\alpha)}{\log(4/3)}+\varepsilon\right)\log n,\\
 h+s&<\left(\frac{3(1-\alpha)}{\log(4/3)}+\varepsilon\right)\log n.
\end{aligned}
\tag{25}
\]
For odd \(n\), the corresponding odd-return path reaches an integer at most \(n^\alpha\) in fewer than
\(\bigl((1-\alpha)/\log(4/3)+\varepsilon\bigr)\log n\) returns. For every integer \(X\ge1\),
\[
 |[1,X]\setminus Q|
 \le A_RX^{1-\alpha D}(1+\log X)^{2R-1/2}
       +\min\{X,N-1\}.
 \tag{26}
\]
Here \(D=I(\eta/\lambda)/\ell>0\), and \(A_R\) is the exact recursion (15).

**Proof.** Choose an integer
\[
 R>\frac{\log\alpha}{\log a_0},\qquad r=\alpha^{1/R}.
\]
Since \(\log a_0<0\), this ensures \(a_0<r<1\) and \(r^R=\alpha\). Put
\[
 B_0=\frac3{\log(4/3)}+\frac1{\log3},\qquad
 \eta=\min\left\{\frac{r-a_0}{2},\frac{\beta}{2},
                    \frac{\varepsilon}{4B_0G_R}\right\}.
 \tag{27}
\]
All three terms are positive. Thus (4)–(23) apply after choosing \(M_0\) by (3), and every tolerance cost in (24) is at most \(\varepsilon/4\). Indeed \(B_0\) dominates the three displayed coefficients of \(\eta G_R\).

Choose an integer \(N\ge2\) with
\[
 \log N\ge\frac{\log K}{\alpha},\qquad
 \log N>\frac{6Rc_r}{\varepsilon},\qquad
 \log N\ge\frac{\log2}{\beta-\eta}.
 \tag{28}
\]
The largest additive clock payment in (23), divided by \(\log n\), is then less than \(\varepsilon/4\). Equations (24) and (23) prove all the strict budgets, with room to spare. The last inequality gives
\(2n^{1+\eta}\le n^{1+\beta}\), and the first gives the closed target \(z_R\le n^\alpha\). The odd-return interpretation follows from (21).

Let \(Q\) be the set of positive integers possessing these simultaneous witnesses, including the odd-return clause on odd inputs. We have proved \(S_R\cap[N,\infty)\subseteq Q\). Taking complements, applying (16), and counting the omitted finite interval proves (26). ∎

Making \(\eta\) small improves the leading clock allowances but also makes the positive density exponent \(D\) small. Formula (26) retains this tradeoff. It is not a uniform statement at zero tolerance.

The [fixed-terminal-rank construction](NT-COLLATZ-36.md#quantitative-descent-on-the-same-controlled-path) has logarithmic factor \(3/2\) in its power-target count, whereas (26) has \(2R-1/2\). The sets and the retained time bounds differ. The present theorem adds the closed fixed-depth clock calculation and a general arbitrary-target pullback recursion; it should not be advertised as improving every estimate in the preceding lesson.

## Exercises with solutions

### Time-dependent fibre bounds

For \(M=6\), \(q=4\), \(Y=16\), calculate the six terms in (8), their sum, and the result of replacing every term by the largest one. Does the list construct fibres of those sizes?

**Solution.** The multiplier inside the floor is \((2^7-1)/(3\cdot16+4)=127/52\). At \(h=1,\ldots,6\), the six bounds are \(1,3,5,8,10,13\), summing to \(40\). Using the last at every time gives \(6\cdot13=78\). The uniform last bound in (9) gives \((5/12)6^2(64/16)=60\). Thus the exact sum is smaller than both.

These are containing-interval bounds for a fixed landing, not constructions of actual fibres. For example a source at least \(64\) cannot reach \(16\) in one shortcut step, because \(T(n)\ge n/2\). That time's actual fibre is empty, despite its upper bound of one.

### Why the startup region is a maximum

Define \(F(n)=\lfloor\sqrt n\rfloor\) for \(n\ge16\), and \(F(n)=n\) for \(n<16\). Starting from \(65536\), calculate four iterations. Explain why the bound \(F^4(n)\le n^{1/16}\) fails, while the analogue of (18) holds.

**Solution.** The checkpoints are
\(65536,256,16,4,4\). The fourth value is \(4\), but
\(65536^{1/16}=2\). The pure power estimate fails because the last step is the identity, not a further square-root contraction. The correct estimate is
\(F^4(n)\le\max\{16,n^{1/16}\}=16\).
For an arbitrary positive integer, before the first value below \(16\), every step is at most a square root; afterwards the value is fixed. This proves the maximum bound for every input and every depth, not just the example.

### The negative initial logarithmic power

Explain why the upper inequality in (13) cannot by itself give
\((1+\log Y_M)^{-1/2}\le(1+M)^{-1/2}\). Derive the correct factor and determine the power after three pullbacks.

**Solution.** Taking a negative power reverses a positive inequality, so the proposed inference has the wrong direction. The lower inequality in (13) gives instead
\[
 (1+\log Y_M)^{-1/2}
 \le v^{-1/2}(1+M)^{-1/2}.
\]
Starting from \(p_0=-1/2\), each pullback adds two. Thus \(p_3=11/2\), and the corresponding power saving is \(Dr^3\). The factor \(v^{-1/2}\) is required at the initial step; at later steps the logarithmic powers are positive and the upper inequality suffices.

### A closed target of one quarter

Choose \(R=8\), \(r=2^{-1/4}\). Prove \(r>a_0\), identify the target exponent and the three zero-tolerance leading coefficients, and state the exceptional-count exponent and logarithmic power actually obtained at positive tolerance.

**Solution.** Since \(3^5=243<256=2^8\), \(a_0=\log_2 3/2<4/5\). Also \((4/5)^4=256/625<1/2\), so \(4/5<2^{-1/4}=r\). Hence the required interval for \(r\) is valid, and \(r^8=1/4\).

The leading coefficients from (24), before adding positive tolerance, are
\(3/(2\log(4/3))\) for shortcut steps,
\(3/(4\log(4/3))\) for odd returns, and
\(9/(4\log(4/3))\) for ordinary steps.
Choose a positive \(\eta\) by (27), rather than setting it to zero. Then (26) has power \(X^{1-D/4}\) and logarithmic power \(2\cdot8-1/2=31/2\), with the stated finite cutoff payment. The depth, tolerance, constant and power saving all remain part of the theorem.

## What iteration preserves and what it costs

The stopped map is an exact map on integers, including its zero-time branches. Iterating it preserves a common orbit, and keeping its absorbing branch avoids charging a contraction error after motion has stopped. Quantitative density passes through its preimages with a calculable loss of exponent and logarithmic powers.

The same reasoning separates three choices that can otherwise be conflated: the retained set of inputs, a bound on a stopping time, and a different stopping rule. The improvements here change estimates for the first two without replacing the underlying trajectories. This is why the endpoint, three clocks, height and exceptional count can be asserted together.

## References

- Idris Ali Shaik, *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, version 4.0.2, 4 October 2026. [Preprint and complete mathematical companion](https://doi.org/10.5281/zenodo.23132901). Appendix A of the complete companion proves the graded fixed-power construction and explains its relation to Inselmann's earlier time bounds. It remains useful alongside the stronger critical polylogarithmic theorem because it relates a prescribed amount of descent to the time required.
- Idris Ali Shaik, *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, version 3.2.4, 27 August 2026, Sections 4–5 and 7, Appendix A. [Preprint](https://doi.org/10.5281/zenodo.22130385). The [accompanying formal source at the fixed revision](https://github.com/shaikidris/FirstPassageLinearTransport/tree/ef3410843bf58d69f771f5ba2c0571d54b54da59/lean/FirstPassageLinearTransport) supplies the total stopped map, repeated pullbacks and graded-clock argument. The proofs in this lesson are independently expressed; the time-summed constant, absorbing-startup estimate and retained logarithmic factors are derived explicitly above.


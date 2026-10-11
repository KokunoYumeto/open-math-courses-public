# Exact preimages and mass-weighted error bounds

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

Many probability estimates are obtained by describing a trajectory backwards. A branch word and an endpoint determine a possible starting point; summing over these descriptions should then recover the probability of an event. Two issues must be settled first. The proposed starting point must actually follow the prescribed branches, and different descriptions must not count that same point repeatedly.

Once these facts are proved, a small relative error in each weight costs a small fraction of the total probability mass. It does not cost that error multiplied by the number of descriptions. Changing the set of included points is a separate operation: its error is controlled by the mass near the sampling boundaries. We will prove both statements, retaining the original finite sampling laws throughout.

The main application is the finite terminal construction in Lech Mazur's *Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*, Appendix C. The other basic reference is Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Sections 4 and 5, for valuation words and harmonic first-passage weights. Our prerequisites are [the exact affine coordinates](NT-COLLATZ-18.md#a-word-and-its-endpoint-determine-the-starting-integer) and [first entrance and its time coordinates](NT-COLLATZ-25.md#a-first-entrance-cannot-revisit-a-state). All additional finite arguments are proved here. The resulting comparison is a component of a passage-law proof, not by itself a natural-density theorem.

## Two laws on the same finite set

Fix real numbers \(0<z<U\), and suppose
\[
\mathcal B=\{N\in\mathbb Z_{>0}:N\text{ odd},\ z\leq N<U\}
\]
is nonempty. Define the exact positive sums
\[
D=\#\mathcal B,\qquad H=\sum_{N\in\mathcal B}\frac1N.
\tag{1}
\]
The uniform and harmonic laws on this same set assign the weights
\[
p_F(N)=\frac1D,\qquad p_H(N)=\frac1{HN}.
\tag{2}
\]
Each sums to one. For an event \(A\) in the positive odd integers, its mass is the sum over \(A\cap\mathcal B\); values outside \(\mathcal B\) have zero mass.

Write \(\beta=\log(U/z)\). For every \(N\in\mathcal B\),
\[
e^{-\beta}\leq\frac{p_F(N)}{p_H(N)}=\frac{HN}{D}\leq e^\beta.
\tag{3}
\]
Indeed \(D/U\leq H\leq D/z\), while \(z\leq N<U\). Multiplying these inequalities proves (3). Summation over any event gives the same two-sided comparison of its masses. Summing over the preimage of a set also proves that the comparison survives any map out of \(\mathcal B\), whether or not that map is injective.

This is a finite comparison on one specified interval. Its usefulness comes from the common carrier and the explicit factor \(U/z\), not from treating uniform and harmonic sampling as interchangeable on all positive integers.

## Backwards decoding proves positivity as well as integrality

Let \(\mathbb O\) be the positive odd integers, with
\[
S(N)=\frac{3N+1}{2^{\nu_2(3N+1)}}.
\]
For a word \(a=(a_1,\ldots,a_r)\) of positive integers, retain the affine coordinates
\[
A_j=\sum_{i=1}^j a_i,\qquad
C_0=A_0=0,\qquad C_j=3C_{j-1}+2^{A_{j-1}}.
\tag{4}
\]
The composition with these prescribed branches is
\[
\operatorname{Aff}_a(N)=\frac{3^rN+C_r}{2^{A_r}},\qquad F_a=\frac{C_r}{2^{A_r}}.
\tag{5}
\]
These are exact coordinates, including the affine offset.

**Theorem 1 (Constructive inverse from a positive odd endpoint).** Fix a positive odd \(M\). There is a positive odd starting integer with valuation word exactly \(a\) and endpoint \(S^r(N)=M\) if and only if
\[
2^{A_r}M\equiv C_r\pmod{3^r}.
\tag{6}
\]
It is unique and equals
\[
N_a(M)=\frac{2^{A_r}M-C_r}{3^r}.
\tag{7}
\]
In particular (6) already implies \(M>F_a\); a separate lower bound for \(M\) is unnecessary. The empty word gives the identity \(N=M\).

**Proof.** Actual iteration proves (5), hence necessity and uniqueness. For sufficiency, induct backwards on the word length. The empty case is immediate. Suppose \(r\geq1\) and (6) holds. By (4), its cleared difference is
\[
2^{A_r}M-C_r
=2^{A_{r-1}}(2^{a_r}M-1)-3C_{r-1}.
\tag{8}
\]
Reduction modulo three and coprimality of two and three show that \(2^{a_r}M-1\) is divisible by three. Put
\[
Y=\frac{2^{a_r}M-1}{3}.
\]
Its numerator is a positive odd integer. Being divisible by three, it is at least three, so \(Y\) is positive and odd. Equation (8), divided by three, now gives
\[
2^{A_{r-1}}Y\equiv C_{r-1}\pmod{3^{r-1}}.
\]
Induction constructs the entire positive odd prefix ending at \(Y\), with exactly its prescribed valuations. Finally \(3Y+1=2^{a_r}M\), and \(M\) is odd, so the last valuation is exactly \(a_r\), not merely at least \(a_r\). This constructs the full trajectory. Solving its affine equation gives (7); its positivity proves \(M>F_a\). ∎

Thus the map \(M\mapsto N_a(M)\) is a bijection from the positive odd solutions of (6) to the positive starts having word \(a\). Its inverse is (5). The endpoint set is one residue class modulo \(2\cdot3^r\): multiplication by \(2^{A_r}\) is invertible modulo \(3^r\), and oddness chooses one of the two lifts modulo \(2\cdot3^r\). The starting set is the dyadic cylinder proved in the earlier affine-coordinate lesson.

For example, \(a=(2)\) and \(M=7\) give \(N=9\). Although seven is a small endpoint, the backwards equation gives the actual return \(9\mapsto7\) with valuation two. The proof does not first impose a scale-dependent lower bound and then infer positivity from it.

## When terminal descriptions cannot overlap

Fix an integer threshold \(B\geq1\). Write
\[
\tau_B(M)=\min\{j\geq0:S^j(M)\leq B\},
\]
with value infinity if there is no such time. Choose an integer \(h\geq1\), a finite set \(\mathcal E\subset\mathbb O\) whose members all satisfy \(\tau_B(M)=h\), and a finite set \(J\) of integer times greater than \(h\). Assume
\[
\tag{9}
\max J-\min J\leq h
\]
when \(J\) is nonempty.

A terminal record is a triple \(i=(t,a,M)\), where \(t\in J\), the positive word \(a\) has length \(r=t-h\), \(M\in\mathcal E\), and (6) holds. Take any finite set \(\mathcal I\) of such records, without repeated triples. Theorem 1 assigns an actual positive odd source \(N_i=N_a(M)\) to every record. This definition permits any further selection of words or totals; disjointness will not depend on how that selection was made.

**Theorem 2 (Injectivity across a short time window).** The map \(i\mapsto N_i\) is injective on \(\mathcal I\). It is therefore a bijection onto its image, before any sampling-band restriction is imposed.

**Proof.** Suppose two records \((t,a,M)\) and \((t',a',M')\) give the same \(N\), and arrange \(t\leq t'\). Exact decoding gives
\[
M=S^{t-h}(N),\qquad M'=S^{t'-h}(N)=S^{t'-t}(M).
\]
Put \(d=t'-t\), so \(0\leq d\leq h\). Since \(\tau_B(M)=h\), the first entrance from \(S^d(M)\) is at time \(h-d\): all its earlier iterates are still above \(B\), and its iterate at \(h-d\) is \(S^h(M)\leq B\). But \(\tau_B(M')=h\), so \(h-d=h\) and \(d=0\). The two word lengths agree. Deterministic iteration from \(N\) then gives the same valuation word and endpoint. The records coincide. ∎

The inverse on the image is explicit. Test the finitely many times \(t\in J\); find the unique one whose endpoint \(S^{t-h}(N)\), its actual valuation word, and \(t\) give a record in \(\mathcal I\). Theorem 2 guarantees uniqueness, and membership in the image guarantees existence. No information is discarded by this indexing.

For a record \(i\), its event in the sampling space is
\[
\mathcal A_i=\{N\in\mathcal B:\operatorname{Aff}_{a_i}(N)=M_i\}.
\tag{10}
\]
It is the singleton \(\{N_i\}\) if \(N_i\in\mathcal B\), and empty otherwise. The events are pairwise disjoint. In particular, sums of their actual masses are at most one. Crucially, injectivity also applies to sources *outside* \(\mathcal B\); this will let us count boundary errors without introducing multiplicities.

These records do not yet say that \(t\) is the first entrance time from \(N\). The orbit may have entered \([1,B]\), left it, and later reached \(M\). Exercise 3 gives an exact example and shows why the width condition (9) matters. This is the reason that identifying the union with a genuine first-passage event requires a separate trajectory argument.

## Relative errors are charged to probability mass

For a record of word length \(r\) and total \(A_r\), define
\[
N_i^0=\frac{2^{A_r}M_i}{3^r},\qquad
\alpha_i=\frac{F_{a_i}}{M_i}.
\tag{11}
\]
The positive word has \(0<F_{a_i}<M_i\), so \(0<\alpha_i<1\). The exact source and this offset-free comparison point satisfy
\[
N_i=(1-\alpha_i)N_i^0,\qquad
\frac1{N_i^0}=\frac{1-\alpha_i}{N_i}.
\tag{12}
\]
The comparison point need not be an integer and is not substituted for the actual trajectory.

Let \(P_i=1_{\{z\leq N_i<U\}}\). The actual harmonic atom mass and the comparison weight on this *same support* are
\[
\mu_i=\frac{P_i}{HN_i},\qquad
\nu_i=\frac{P_i}{HN_i^0}.
\tag{13}
\]
They obey the exact identity
\[
\mu_i-\nu_i=\alpha_i\mu_i.
\tag{14}
\]
Both sides vanish outside the physical band. In affine coordinates the first weight is \(P_i(3^r2^{-A_r})/[H(M_i-F_{a_i})]\); the second replaces only that denominator by \(M_i\). The factor \(2^{-A_r}\) is also the exact probability of the word under independent positive geometric letters, but no stochastic model of the actual orbit is used in (14).

**Proposition 3 (No loss from the number of records).** Let \(\rho\geq0\). If \(\alpha_i\leq\rho\) on \(\mathcal I\), then
\[
0\leq\sum_i(\mu_i-\nu_i)
\leq\rho\sum_i\mu_i\leq\rho.
\tag{15}
\]
For any real or complex numbers \(g_i\) with \(|g_i|\leq1\),
\[
\left|\sum_i g_i(\mu_i-\nu_i)\right|
\leq\sum_i\alpha_i\mu_i\leq\rho\sum_i\mu_i.
\tag{16}
\]

**Proof.** Sum (14). Nonnegativity proves the first inequality. The upper bounds follow from \(\alpha_i\leq\rho\), and disjointness in Theorem 2 gives \(\sum_i\mu_i\leq1\). For (16), apply the triangle inequality before the same sum. ∎

The weighted form retains more information than its uniform bound: a large ratio on an atom of very small mass may be harmless. It also controls every subset of records and every bounded observable of their endpoints. For example, take \(g_i=1_{\{M_i\in E\}}\). If several records have the same endpoint, summing them at that endpoint still cannot increase this error; the triangle inequality groups the terms. Injectivity is needed for the *sources*, not for the endpoint projection.

## Moving the support costs boundary mass

Replacing the source by \(N_i^0\) in the band selector is a different operation. To make all endpoints explicit, put
\[
Q_i=1_{\{z<N_i^0<U\}},\qquad
\delta_i=-\log(1-\alpha_i)>0.
\tag{17}
\]
The lower endpoint in \(Q_i\) is open, whereas the lower endpoint in \(P_i\) is closed. The upper endpoint is open in both. Equation (12) says \(N_i=e^{-\delta_i}N_i^0\).

Write the actual and comparison sums as
\[
\begin{aligned}
U_F&=\sum_i P_i/D,& I_F&=\sum_i Q_i/D,\\
U_H&=\sum_i P_i/(HN_i),& I_H&=\sum_i Q_i/(HN_i^0).
\end{aligned}
\tag{18}
\]
The sums \(U_F,U_H\) are probabilities of the union of the actual atoms. The comparison sums \(I_F,I_H\) need not themselves be probabilities.

**Theorem 4 (Support and weight comparison).** Let \(\rho,\varepsilon\geq0\), and suppose \(\alpha_i\leq\rho\) and \(\delta_i\leq\varepsilon\). Define the two sets of positive odd integers
\[
S_-=[ze^{-\varepsilon},z)\cap\mathbb O,
\qquad S_+=[Ue^{-\varepsilon},U)\cap\mathbb O.
\tag{19}
\]
Then
\[
\begin{aligned}
|U_F-I_F|&\leq\frac{\#(S_-\cup S_+)}D,\\
|U_H-I_H|&\leq\rho U_H+
 \frac1H\sum_{N\in S_-\cup S_+}\frac1N.
\end{aligned}
\tag{20}
\]
There are also the one-sided bounds
\[
I_F\leq U_F+\frac{\#S_-}{D},\qquad
I_H\leq U_H+\frac1H\sum_{N\in S_-}\frac1N.
\tag{21}
\]

**Proof.** If \(Q_i=1\) but \(P_i=0\), then \(N_i<N_i^0<U\), so the failed physical condition is \(N_i<z\). Also \(N_i=e^{-\delta_i}N_i^0>ze^{-\varepsilon}\). Thus \(N_i\in S_-\).

If \(P_i=1\) but \(Q_i=0\), then \(N_i^0>N_i\geq z\), so the failed comparison condition must be \(N_i^0\geq U\). It follows that \(Ue^{-\varepsilon}\leq N_i<U\), hence \(N_i\in S_+\). These implications include equality at the upper comparison endpoint. Strict positivity of \(\delta_i\) handles equality at the lower physical endpoint.

Different mismatching records have different \(N_i\), by Theorem 2, even when \(N_i\) is outside the physical band. This proves the flat bound. For the harmonic bound, insert
\[
I_H^{\mathrm{phys}}=\sum_i\frac{P_i}{HN_i^0}.
\]
Proposition 3 gives \(0\leq U_H-I_H^{\mathrm{phys}}\leq\rho U_H\). The remaining support difference is at most the shell sum in (20), since \(1/N_i^0\leq1/N_i\). Add the two estimates.

For (21), only a comparison-only record can increase the comparison sum over the actual sum. It lies in \(S_-\). On common support the comparison harmonic weight is no greater than the actual weight; actual-only records can only decrease the difference. This proves both one-sided assertions. ∎

![An exact source and its offset-free comparison point under three interval choices. For the word two and endpoint seven the true source is nine, while the comparison point is twenty-eight thirds. In the band from nine to ten both are included and only the reciprocal weight changes. In the band from thirty-seven quarters to twelve only the comparison point is included. In the band from nine to twenty-eight thirds only the actual source is included because the upper endpoint is excluded. Each sampling band contains an odd integer.](../figures/affine-support.svg)

*The two operations in Theorem 4, on the exact return \(9\mapsto7\). In the first band the relative weight defect is \(1/28\). In the other two, the membership indicator changes; the error must be charged to the appropriate boundary, not to a weight estimate alone. The middle sampling band contains eleven, although this record's actual source nine lies outside it.*

The theorem has a completely explicit finite consequence. Positive odd integers in an interval \([l,u)\), with \(l>0\), have count at most \((u-l)/2+1\). Their reciprocal sum is at most
\[
\frac1l+\frac12\log(u/l).
\tag{22}
\]
For a nonempty interval, list its points as \(m,m+2,\ldots,m+2(k-1)\). The count follows by comparing the first and last points. For the reciprocal bound, separate \(1/m\), and integrate the decreasing function \(1/(m+2t)\) over \([0,k-1]\) to bound the remaining terms. Since \(m\geq l\) and the last point is below \(u\), (22) follows. The empty interval also satisfies both bounds.

Applying them to (19) gives
\[
\begin{aligned}
|U_F-I_F|&\leq\frac{\varepsilon(z+U)/2+2}{D},\\
|U_H-I_H|&\leq\rho U_H+
 \frac{\varepsilon+e^\varepsilon(z^{-1}+U^{-1})}{H}.
\end{aligned}
\tag{23}
\]
Here \(1-e^{-\varepsilon}\leq\varepsilon\), by integration of \(e^{-t}\leq1\). The denominators remain the actual sums (1); no asymptotic replacement of either sampling law has occurred.

## How the word length controls the correction

There is a sharper elementary offset bound than \(F_a<3^r\). Formula (5) gives
\[
F_a=\sum_{j=1}^r3^{r-j}2^{-(a_j+\cdots+a_r)}
\leq\left(\frac32\right)^r-1.
\tag{24}
\]
Every suffix contains at least its number of letters, so its exponent is at least \(r-j+1\). Summing the resulting geometric series proves (24). Equality holds for the all-ones word. Thus this is the exact largest offset among all positive words of length \(r\), though further restrictions on their total can exclude that maximizing word.

**Proposition 5 (A local correction bound).** Let \(B>1\), \(\kappa,\sigma>0\), and
\[
\lambda=\sigma-\kappa\log(3/2)>0.
\]
If a record has \(r\leq\kappa\log B\) and \(M_i\geq B^\sigma\), then
\[
0<\alpha_i\leq B^{-\lambda},\qquad
\delta_i\leq\frac{B^{-\lambda}}{1-B^{-\lambda}}.
\tag{25}
\]
If \(B^\lambda\geq2\), the second bound is at most \(2B^{-\lambda}\).

**Proof.** Divide (24) by the endpoint lower bound, and use
\((3/2)^r\leq B^{\kappa\log(3/2)}\). The source is positive, so \(\alpha_i<1\). For \(0\leq v<1\),
\[
-\log(1-v)=\int_0^v\frac{dt}{1-t}\leq\frac{v}{1-v}.
\]
The right side increases with \(v\), proving (25). When \(B^{-\lambda}\leq1/2\), its denominator is at least one half. ∎

For the explicit local conditions
\[
r\leq\frac{21}{2000}\log B,\qquad M_i\geq B^{999/1000},
\tag{26}
\]
used in Mazur's affine-correction estimate, one may take the rational bounds
\[
\alpha_i\leq B^{-198939/200000},\qquad
\delta_i\leq B^{-9/10}\quad\text{if }\log B\geq300000.
\tag{27}
\]
Here is the constant calculation. The positive exponential series gives
\[
e^{41/100}\geq1+\frac{41}{100}
+\frac{(41/100)^2}{2}+\frac{(41/100)^3}{6}>\frac32.
\]
Thus \(\log(3/2)<41/100\), and
\[
\frac{999}{1000}-\frac{21}{2000}\frac{41}{100}
=\frac{198939}{200000}.
\]
This proves the first bound. The assumed lower bound on \(\log B\) implies both \(B^{198939/200000}\geq2\) and
\(B^{18939/200000}\geq2\), since \(\log2<1\). Applying Proposition 5 gives the second bound. The inequality \(\log2<1\) itself follows from \(e\geq1+1+1/2>2\).

The source's coarser estimate uses \(3^r\) and \(\log3<11/10\), giving the exponent \(19749/20000\) for \(\alpha_i\). Retaining the geometric sum (24) improves that local denominator estimate. It does not by itself change the \(B^{-9/10}\) boundary allowance or the final logarithmic density exponent, which also depend on other estimates. Conditions (26) remain explicit mathematical conditions; checking them on a particular family is separate from this calculation.

## Exercises with solutions

### 1 Compute both arithmetic cylinders

For \(a=(2,1,1)\), find all positive odd endpoints satisfying (6), their sources, and the exact intermediate states. Exhibit a valid endpoint smaller than \(2\cdot3^r\).

**Solution.** We have \(r=3\), \(A_r=4\), and \(C_r=29\). Since the inverse of sixteen modulo twenty-seven is twenty-two, compatibility is \(M\equiv17\pmod{27}\). Oddness gives exactly \(M=17+54j\), \(j\geq0\). Equation (7) gives \(N=9+32j\), and the actual trajectory is
\[
9+32j\ \longmapsto\ 7+24j\ \longmapsto\ 11+36j\ \longmapsto\ 17+54j.
\]
The numerators at these three returns are respectively four, two, and two times the displayed positive odd next states, so the valuations are exactly \((2,1,1)\). For \(j=0\), the endpoint seventeen is smaller than \(2\cdot3^3=54\). Backwards decoding proves positivity without that sufficient but unnecessary size condition.

### 2 Separate a weight error from a support error

For the word \((2)\) and endpoint seven, compute the actual and comparison harmonic masses in \([9,10)\). Then compute them in \([9,28/3)\), using the selectors (17).

**Solution.** The actual source is nine, the comparison point is \(28/3\), and \(\alpha=1/28\). In either physical band, the only positive odd integer is nine, so \(H=1/9\). For \([9,10)\), both selectors equal one. Therefore \(U_H=1\), \(I_H=27/28\), and the difference is exactly \(\alpha U_H=1/28\). For \([9,28/3)\), the actual selector is one but the comparison point lies on the excluded upper endpoint, so \(I_H=0\) and the difference is one. The latter is a support error. A bound of \(1/28\) alone would be false. A singleton family is injective; if desired it is a terminal family with \(B=6,h=4,J=\{5\}\), since \(7,11,17,13,5\) has first entrance to \([1,6]\) at time four.

### 3 Why a remaining time is not a first time from the source

Consider \(B=50\) and the odd orbit
\[
81,61,23,35,53,5.
\]
Verify the transitions. Construct two terminal records with remaining first-entrance time \(h=1\) and the same source. Explain precisely which hypothesis of Theorem 2 fails and why the later record does not give the source's first entrance.

**Solution.** The five valuations are \(2,3,1,1,5\): the numerators are \(244,184,70,106,160\). The endpoints sixty-one and fifty-three both first enter \([1,50]\) after one return. They give records \((2,(2),61)\) and \((5,(2,3,1,1),53)\) with source eighty-one. The terminal-time set \(J=\{2,5\}\) has diameter three, greater than \(h=1\), so Theorem 2 does not apply. The source first enters at time two, at twenty-three, then passes through thirty-five and leaves the interval at fifty-three. Its later record leads to an entrance at time five, not its first entrance. Thus both the window condition and the distinction between terminal records and genuine first passage have concrete content.

### 4 Retain nonuniform errors under a projection

Let \(\mathcal A_i\) be disjoint events in a finite probability space, with masses \(\mu_i\). Let \(0\leq\eta_i\leq1\) and \(\nu_i=(1-\eta_i)\mu_i\). For any map \(\pi\) from the index set to a finite set, define \(p(y)=\sum_{\pi(i)=y}\mu_i\) and \(q(y)=\sum_{\pi(i)=y}\nu_i\). Prove a sharp formula for \(\sum_y|p(y)-q(y)|\). Explain what fails if a source event is listed repeatedly.

**Solution.** Every difference \(\mu_i-\nu_i=\eta_i\mu_i\) is nonnegative, so each grouped difference is also nonnegative. Consequently
\[
\sum_y|p(y)-q(y)|
=\sum_y\sum_{\pi(i)=y}\eta_i\mu_i
=\sum_i\eta_i\mu_i.
\]
This is an equality, not a cardinality bound. It is at most \((\max_i\eta_i)\sum_i\mu_i\leq\max_i\eta_i\); for an empty index set both sums are zero. If the whole sample space is listed as \(m\) different events, each has mass one and the sum of its repeated masses is \(m\), not at most one. With a common defect \(\eta>0\), the error is then \(m\eta\). Proving the source descriptions disjoint is exactly what removes this multiplicity.

## What the comparison achieves

The affine congruence determines a genuine trajectory by an explicit inverse. A short time window and a common remaining first-entrance time make its terminal descriptions injective. These facts turn the sum of local relative errors into a bound by actual probability mass. Moving a support boundary contributes a second, geometrically localized error, with the original finite denominators intact.

This is useful well beyond this particular orbit problem: inverse descriptions, disjoint event decompositions, relative weight errors and boundary mass are compatible tools for comparing discrete measures. In the present application, they supply the exact finite foundation on which local probability estimates and phase averages can act. Identifying those measures with a genuine first-passage law is further mathematics, not a consequence of an affine endpoint formula alone.

## References

- Lech Mazur, *Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*, version 2, 21 July 2026, Appendix C.2–C.3 and its accompanying formal source, [ProofAtlas](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/). The terminal-record injectivity, common finite sampling laws, exact reciprocal denominator and mass-weighted comparison follow this construction. The backwards positivity proof, explicit general shell bounds and sharper local offset calculation are supplied here; no literature-wide priority claim is made.
- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), Sections 4 and 5. Valuation-word coordinates, affine offsets and harmonic first-passage weights underlie the construction. Their required finite identities and the new comparisons are proved internally.

# Quotient measure and the subgroup modular correction

Inducing a representation from a closed subgroup requires a measure on the coset space. That measure is rarely invariant. The correction is governed by the ratio of the modular functions of the large group and the subgroup. We construct a quotient measure, prove its measure class is unique, and keep the two possible translation conventions separate.

*Programme exposition written in Codex (OpenAI), September 2026; foundation integration and proof restoration by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is dedicated under CC0 to the extent of rights held.*

<a id="oa-flow.qm.setting"></a>

## Quotients and the modular convention

Let $G$ be a locally compact Hausdorff group, $H\subseteq G$ a closed subgroup, and $Y=G/H$ the left-coset space. Write $q:G\to Y$, $q(s)=sH$. Fix left Haar measures $ds$ and $dh$ and modular functions by the convention

<a id="equation-q1"></a>

$$ \int_G F(sr)\,ds=\Delta_G(r)^{-1}\int_G F(s)\,ds,
 \qquad
 \int_H K(hr)\,dh=\Delta_H(r)^{-1}\int_H K(h)\,dh. \tag{Q1} $$

Here **Radon** means locally finite and inner regular on every Borel
set, including sets of infinite measure: its value is the supremum of
the measures of compact subsets. Both Haar measures use this convention.
Every quotient and lifted measure below is the inner-regular measure
representing its positive functional on compactly supported continuous
functions. We use Borel sets, then their null-set completions. This
choice matters when the group is not sigma-compact; compact tests alone
do not specify an outer-regular extension on all Borel sets.

**Exact earlier foundations.** [QF1–3](OA-FLOW-QF.md#qf-1) prove quotient topology, compact lifting, subgroup averaging and the locally finite cutoff. [HR2](OA-FLOW-HR.md#hr-02) proves positive Riesz representation, [HR3](OA-FLOW-HR.md#hr-03) finite regularity and positive densities, and [HR5](OA-FLOW-HR.md#hr-05) the finite-support Borel Radon-product theorem and semicontinuous approximation. [L24 Section3](OA-FLOW-L24.md#oa-flow.grp.translations) proves the modular and inversion formulas. [H0](OA-FLOW-TOPOLOGY.md#l138-h0) supplies compact bumps. The all-Borel inner-regular convention needed here is now proved explicitly.

**The inner-regular representative.** HR2 uses measures outer regular on all Borel sets and inner regular on open sets. This chapter uses the representative inner regular on every Borel set. The following bridge is essential; equality of global null sets is not asserted.

Let $X$ be a topological disjoint union of open-and-closed sigma-compact locally compact Hausdorff pieces $X_i$, and let $I:C_c(X)\to\mathbb C$ be positive. [HR2](OA-FLOW-HR.md#hr-02), gives the unique outer-regular representing measure $\mu$. Since each $X_i$ has a countable compact cover, it is sigma-finite for $\mu$. [HR3](OA-FLOW-HR.md#hr-03) therefore makes $\mu$ inner regular on every Borel subset of each $X_i$. Define, for a Borel set $A$,

<a id="equation-q1a"></a>

$$ \mu_{\mathrm{in}}(A)=\sum_i\mu(A\cap X_i). \tag{Q1a} $$

where a sum of nonnegative numbers over an arbitrary index set means the supremum of its finite subsums. This is countably additive: for disjoint $A_n$, use countable additivity inside each $X_i$ and exchange the two nonnegative sums. The exchange follows by taking the supremum over finite sets of indices and finite initial segments of $n$ in either order; for finitely many $n$, a union of the finitely many approximating index sets approximates all their sums simultaneously. This is an identity of positive sums and uses no arbitrary-net integral convergence.

A compact set $K$ meets only finitely many pieces, since the pieces form an open cover. Its intersections with those pieces are compact. Consequently $\mu_{\mathrm{in}}(K)=\mu(K)<\infty$. Inner regularity on each piece, followed by the supremum over finite families of pieces, gives

<a id="equation-q1b"></a>

$$ \mu_{\mathrm{in}}(A)=\sup_{K\subseteq A,\ K\ \mathrm{compact}}\mu(K). \tag{Q1b} $$

The finite union of the chosen compact subsets is compact, so this proves inner regularity on every Borel set, including infinite values. It also shows that the construction is independent of the chosen decomposition. For a function in $C_c(X)$, its support meets finitely many pieces and the measures coincide on each of those pieces; thus $\int f\,d\mu_{\mathrm{in}}=I(f)$. On open sets $\mu_{\mathrm{in}}=\mu$, by inner regularity of $\mu$ on opens. On $\mu$-sigma-finite Borel sets the two also coincide, by HR3. No equality is asserted on arbitrary Borel sets, nor equivalence of their global null ideals.

This inner-regular representative is unique. In fact, for any locally finite measure inner regular on all Borel sets, the measure of a compact set is the infimum of its nonnegative continuous compactly supported majorants. To prove this, put the compact set inside the interior of a compact neighborhood. On that finite measure space, inner regularity on the complement gives outer regularity by subtraction from its total mass. An open neighborhood of the original compact set can therefore be chosen with measure arbitrarily close to its measure; [H0](OA-FLOW-TOPOLOGY.md#l138-h0) supplies a continuous bump equal to one on the original compact set and supported in that open neighborhood. The reverse inequality for every majorant is immediate. Two inner-regular measures representing $I$ consequently agree on compact sets, and then on all Borel sets by their inner regularity. This proves the precise representation theorem required by FLOW on these spaces.

Both $G$ and $G/H$ have the required decomposition by [QF3](OA-FLOW-QF.md#qf-3): use cosets of an open sigma-compact subgroup on $G$ and its open-and-closed orbits on $G/H$. That proof also supplies the cutoff, including the locally finite partition construction. Compact bumps are H0. No general partition-of-unity theorem is an additional input.

Homeomorphisms commute with this inner regularization: a homeomorphism takes exactly the compact subsets of a Borel set to the compact subsets of its image, so apply the compact-supremum formula. Positive continuous densities also commute with it. Indeed, $b\mu$ is the outer-regular measure from [HR3](OA-FLOW-HR.md#hr-03); it is sigma-finite on each $X_i$, and its inner regularization is $\sum_i\int_{A\cap X_i}b\,d\mu$. This equals $\int_A b\,d\mu_{\mathrm{in}}$: first check indicators, then simple functions, then an increasing simple sequence, exchanging only nonnegative sums and countable limits. Hence the modular translation and positive-density identities proved in L24 Section3 pass to FLOW's inner-regular representatives on every Borel set. In particular left Haar invariance and the stated right-translation modular scalar are preserved.

The quotient formula and both inverse-translation densities are proved below, using these exact current inputs. The locally integrable descent and compact Borel kernel arguments provide their own finite localization; the bridge supplies no global non-sigma-finite Borel Fubini assertion.

For example, take $G=\mathbb R_{\mathrm{discrete}}\times\mathbb R$ and
$H=\mathbb R_{\mathrm{discrete}}\times\{0\}$. Every compact subset of
$q^{-1}(\{0\})$ meets only finitely many components and is Haar-null.
Inner-regular Haar therefore gives the whole preimage measure zero.
An outer-regular Haar extension instead gives that preimage infinite
measure: any open neighborhood has a positive-length interval in each
of uncountably many components. The distinct definitions and this
example are also proved in [HR8–9](OA-FLOW-HR.md#hr-08) and [L24 Section2](OA-FLOW-L24.md#oa-flow.grp.haarconventions).
All global null-set assertions in this lesson use the inner-regular
choice explicitly.

For $f\in C_c(G)$ put

<a id="equation-q2"></a>

$$ Qf(sH)=\int_H f(sh)\,dh. \tag{Q2} $$

This is a continuous compactly supported function on $Y$. Continuity follows by uniform continuity of $f$ on a compact neighborhood of the relevant fiber portion; the support lies in $q(\operatorname{supp}f)$. Notice that $Q$ uses the left Haar measure of $H$ on every fiber. The complete averaging proof is [QF2](OA-FLOW-QF.md#qf-2); quotient topology and compact lifting are [QF1](OA-FLOW-QF.md#qf-1).

Set

<a id="equation-q3"></a>

$$ \chi_H(h)=\frac{\Delta_G(h)}{\Delta_H(h)},\qquad h\in H. \tag{Q3} $$

This positive character is the exact correction. It equals one for an open subgroup but need not do so for a general closed subgroup, even when neither of the two Haar measures is normalized in a special way.

<a id="oa-flow.qm.cutoff"></a>

## A continuous cutoff along the cosets

The cutoff is [QF3](OA-FLOW-QF.md#qf-3), proved for every locally compact Hausdorff $G$ and closed $H$. Choose an open sigma-compact subgroup $L$. On each open-and-closed $L$-orbit in $Y$, the compact-shell construction there gives a locally finite compactly supported partition of unity. Extending by zero over the disjoint orbits gives such a family $(\psi_i)$ on all of $Y$.

By [QF2](OA-FLOW-QF.md#qf-2), choose $\varphi_i\in C_c(G)_+$ with $Q\varphi_i=1$ on $\operatorname{supp}\psi_i$. The supports of the $\psi_i$ are compact and lie in the open positive sets of their denominators. The normalized expression for this cutoff is

<a id="equation-q4"></a>

$$ k(s)=\sum_i
  \frac{\psi_i(q(s))\varphi_i(s)}{Q\varphi_i(q(s))}, \tag{Q4} $$

with a term interpreted as zero outside the open set where its denominator is positive. Local finiteness makes $k$ continuous and nonnegative. It satisfies

<a id="equation-q5"></a>

$$ Qk(y)=1\qquad(y\in Y). \tag{Q5} $$

For every compact $K\subseteq Y$, the support of $k$ over $K$ is compact in $G$: only finitely many partition terms meet $K$, and their numerators have compact support. Thus $F(q(s))k(s)$ belongs to $C_c(G)$ whenever $F\in C_c(Y)$. In particular $Q:C_c(G)\to C_c(Y)$ is onto by taking $f(s)=F(q(s))k(s)$.

<a id="oa-flow.qm.rho"></a>

## Building a positive modular density

The cutoff yields an everywhere positive continuous function

<a id="equation-q6"></a>

$$ \rho(s)=\int_H k(sh)\chi_H(h)\,dh. \tag{Q6} $$

The support property makes this integral finite locally uniformly in $s$, and (Q5) makes it strictly positive. Substituting $h\mapsto r^{-1}h$ with left Haar measure gives

<a id="equation-q7"></a>

$$ \rho(sr)=\chi_H(r)^{-1}\rho(s)
  =\Delta_G(r)^{-1}\Delta_H(r)\rho(s),
       \qquad s\in G,\ r\in H. \tag{Q7} $$

Define a positive Radon measure $\mu_\rho$ on $Y$ by

<a id="equation-q8"></a>

$$ \int_Y F(y)\,d\mu_\rho(y)
     =\int_G F(q(s))k(s)\rho(s)\,ds,
       \qquad F\in C_c(Y). \tag{Q8} $$

For a fixed density $\rho$, the definition may use any auxiliary cutoff satisfying (Q5), and the resulting measure is independent of that auxiliary choice. Indeed the quotient integration identity is

<a id="equation-q9"></a>

$$ \int_Y Qf(y)\,d\mu_\rho(y)
      =\int_G f(s)\rho(s)\,ds,
       \qquad f\in C_c(G). \tag{Q9} $$

To verify it, insert (Q2) and (Q8). This use of Tonelli is localized to compact supports: if $t=sh$ lies in $\operatorname{supp}f$ and $k(s)\ne0$, the cutoff property places $s$ in one compact set over $q(\operatorname{supp}f)$, and then $h$ lies in the compact set $K_s^{-1}\operatorname{supp}f\cap H$. Haar measures are finite on these compact portions. No global sigma-finite Haar assumption is used. In the inner integral substitute $t=sh$. The right-translation factor from (Q1) is $\Delta_G(h)^{-1}$, while (Q7) gives $\rho(th^{-1})=\chi_H(h)\rho(t)$. Their product is $\Delta_H(h)^{-1}$. Inversion in $H$ then changes the remaining factor to

$$ \int_H \Delta_H(h)^{-1}k(th^{-1})\,dh
      =\int_H k(tr)\,dr=Qk(q(t))=1. $$

This proves (Q9). Since $Q$ is onto $C_c(Y)$, (Q9) determines the inner-regular Radon measure uniquely for the fixed $\rho$, and proves independence from the auxiliary cutoff. Changing the cutoff used in (Q6) can change $\rho$ itself. If $\rho_1,\rho_2$ are two strictly positive continuous densities obeying (Q7), their ratio descends to a strictly positive continuous function $b$ on $Y$. Applying (Q9) to both densities gives $\mu_{\rho_2}=b\mu_{\rho_1}$. Thus their measure classes agree, while their numerical measures need not agree.

<a id="oa-flow.qm.descent"></a>

## Which densities descend to quotient measures?

The same calculation works for any nonnegative locally integrable $\varphi$ on $G$ satisfying

<a id="equation-q10"></a>

$$ \varphi(sr)=\chi_H(r)^{-1}\varphi(s)
       \quad\text{for almost every }s,\text{ for each fixed }r\in H. \tag{Q10} $$

Define $\mu_\varphi$ by (Q8) with $\varphi$ in place of $\rho$. It is locally finite because the cutoff support over each compact part of $Y$ is compact. Choose the Borel representative of $\varphi$ provided by [QF6](OA-FLOW-QF.md#qf-6) before doing the calculation. [HR5](OA-FLOW-HR.md#hr-05) applies to the Borel integrands supported in the identified compact portions of $G\times H$. These portions have finite Radon product measure. On them the outer-regular and inner-regular factors coincide, by the bridge. For each fixed $h$, (Q10) fails only on a Haar-null $s$-set; finite Radon Fubini therefore discards the joint exceptional set. We use this Borel Radon-product theorem, rather than assuming that the Borel sigma-algebra of a product equals the product sigma-algebra. No equality of those two sigma-algebras is assumed. Local integrability bounds the required integrals: after $t=sh$, the contributing $t$ lie in $\operatorname{supp}f$, $h$ lies in one compact set, and the factors $k(th^{-1})$ and the modular characters are bounded there. Thus the absolute iterated integral is bounded by a finite constant times $\int_{\operatorname{supp}f}\varphi(t)\,dt$. This proves the needed Fubini hypothesis without a global sigma-finite Haar assumption. It gives

<a id="equation-q11"></a>

$$ \int_Y Qf\,d\mu_\varphi=\int_G f(s)\varphi(s)\,ds. \tag{Q11} $$

Conversely, suppose a Radon measure $\mu$ on $Y$ satisfies (Q11) for such a density $\varphi$. For $r\in H$, right translation inside $Q$ gives

$$ Q\bigl(f(\,\cdot\,r)\bigr)
     =\Delta_H(r)^{-1}Qf. $$

Apply (Q11) on both sides, substitute $t=sr$ on $G$ using (Q1), and compare the resulting integrals against every $f\in C_c(G)$. Then (Q10) follows for almost every $s$, for each fixed $r$. To make this last passage explicit, on each sigma-compact piece the two locally integrable densities determine the same locally finite measure when their continuous tests agree; regularity and compact bumps give equality on Borel sets, hence equality of the densities almost everywhere there. Each piece has a countable compact cover. The union of these null exceptional sets over all pieces is still inner-Haar-null: its intersection with every compact set is null, and inner regularity then gives its global measure zero. This is the precise measure-theoretic meaning of the source's displayed equation for a locally integrable density: modifying a density on a Haar-null set cannot change whether it descends. The continuous $\rho$ constructed above satisfies its identity at every point.

<a id="oa-flow.qm.class"></a>

## The unique quasi-invariant measure class

For $a\in G$ and $y=sH$, define

<a id="equation-q12"></a>

$$ c(a,y)=\frac{\rho(as)}{\rho(s)}. \tag{Q12} $$

Equation (Q7) makes this independent of the coset representative $s$, and

<a id="equation-q13"></a>

$$ c(ab,y)=c(a,by)c(b,y). \tag{Q13} $$

The measure $E\mapsto\mu_\rho(aE)$ is equivalent to $\mu_\rho$: its strictly positive Radon–Nikodym derivative is derived below. Hence $\mu_\rho$ is quasi-invariant.

Now let $\mu$ be any nonzero quasi-invariant Radon measure on $Y$ and lift it to a Radon measure $\nu$ on $G$ by

<a id="equation-q14"></a>

$$ \nu(f)=\int_Y Qf(y)\,d\mu(y),\qquad f\in C_c(G). \tag{Q14} $$

This lift is nonzero because QF2 lifts every nonnegative member of $C_c(Y)$ to a nonnegative member of $C_c(G)$, and a nonzero inner-regular measure has a positive compact continuous test.

We first specify how the continuous integration formulas are used on
Borel sets. For $f\in C_c(G)_+$ and $F\in C_c(Y)$, (Q9) gives

$$ \int_G F(q(s))f(s)\rho(s)\,ds
       =\int_Y F(y)Qf(y)\,d\mu_\rho(y). $$

Both sides define finite inner-regular Radon measures on $Y$: the left
is the continuous pushforward of the finite compactly supported measure
$f\rho\,ds$, and the right is $Qf\,\mu_\rho$. Equality on $C_c(Y)$
therefore gives equality on every Borel set. In particular,

$$ \int_{q^{-1}(E)}f(s)\rho(s)\,ds
       =\int_E Qf(y)\,d\mu_\rho(y)
       \qquad(E\subseteq Y\text{ Borel}). $$

The same argument for (Q14) gives
$\nu(f1_{q^{-1}(E)})=\int_E Qf\,d\mu$.
**The compact Borel kernel formula.** For a compact $B\subset G$, put

<a id="equation-q14a"></a>

$$ h_B(sH)=\int_H1_B(sh)\,dh. \tag{Q14a} $$

Left invariance of $dh$ makes this independent of $s$. The function is upper semicontinuous. Indeed, fix $s_0$ and a compact neighborhood $A$ of $s_0$. All contributing $h$ for $s\in A$ lie in the compact set $T=H\cap A^{-1}B$. Put $B_{s_0}=\{h:s_0h\in B\}$. By compact outer approximation choose an open $V\subset H$ containing $B_{s_0}$ with $dh(V)<dh(B_{s_0})+\varepsilon$. The set

$$ \{(s,h)\in A\times(T\setminus V):sh\in B\} $$

is compact. Its projection on $G$ is closed and misses $s_0$. In a sufficiently small neighborhood of $s_0$ inside $A$, every contributing $h$ therefore lies in $V$, so $h_B(q(s))<h_B(q(s_0))+\varepsilon$. Since $q$ is open, this proves upper semicontinuity on $Y$. The support lies in the compact set $q(B)$. Choose $b\in C_c(G)$ with $0\le b\le1$ and $b=1$ on $B$; then $0\le h_B\le Qb$, so $h_B$ is bounded and Borel.

Let $\mathcal F$ consist of the $f\in C_c(G)$ with $0\le f\le b$ and $f=1$ on $B$. It is downward directed by minimum. The compact-majorant characterization proved above gives $\nu(B)=\inf_{f\in\mathcal F}\nu(f)$: for a finite-measure open neighborhood $U$ of $B$ with $\nu(U)$ close to $\nu(B)$, take $f=b\eta$ with $\eta=1$ on $B$ and supported in $U$. Also

<a id="equation-q14b"></a>

$$ h_B(y)=\inf_{f\in\mathcal F}Qf(y). \tag{Q14b} $$

For this second identity fix $y=sH$ and put $T_y=H\cap s^{-1}\operatorname{supp}b$, which is compact. Choose an open $V\supset B_s$ with $dh(V)<dh(B_s)+\varepsilon$. The compact set $s(T_y\setminus V)$ is disjoint from $B$. H0 gives $0\le\eta\le1$, equal to one on $B$, whose support avoids that set. For $f=b\eta$ we then have $Qf(y)\le dh(V)$. Together with $h_B\le Qf$ this proves (Q14b), including the case of an empty fiber.

We justify the infimum of the integrals by a finite covering argument. Put $D=q(\operatorname{supp}b)$, so $\mu(D)<\infty$. The function $Qb-h_B$ is nonnegative, lower semicontinuous and supported in $D$. [HR5, formula HR-05b](OA-FLOW-HR.md#hr-05), applied on the finite compact portion where both representatives agree, provides $u\in C_c(Y)$ with $0\le u\le Qb-h_B$ and integral arbitrarily close to that of $Qb-h_B$. Hence $g=Qb-u$ is continuous, is at least $h_B$, and has integral arbitrarily close to $\int h_B\,d\mu$. For any $\delta>0$, (Q14b) gives, for each $y\in D$, an $f_y\in\mathcal F$ such that $Qf_y(y)<g(y)+\delta$. The corresponding strict inequalities hold on open neighborhoods covering $D$. Choose finitely many of these neighborhoods and put $f=\min_j f_{y_j}$. Then $Qf\le Qf_{y_j}$ for every $j$, so $Qf<g+\delta$ on $D$, and $Qf=0$ off $D$. It follows that

$$ \int h_B\,d\mu\ \le\ \inf_{f\in\mathcal F}\int Qf\,d\mu
       \ \le\ \int g\,d\mu+\delta\mu(D). $$

Let the approximation error and $\delta$ tend to zero. By (Q14), the compact-majorant identity now gives

<a id="equation-q14c"></a>

$$ \nu(B)=\int_Y h_B(y)\,d\mu(y)
       =\int_Y\int_H1_B(sh)\,dh\,d\mu(sH). \tag{Q14c} $$

No monotone-convergence assertion for an arbitrary decreasing net was used. Equivalent base measures integrate the same nonnegative Borel $h_B$ to zero, so their lifts have the same compact null sets. Inner regularity then gives the same Borel null sets. Left translation of the lift is the lift of the left-translated base measure, since $Q[f(a\,\cdot\,)](y)=Qf(ay)$. Quasi-invariance of $\mu$ consequently makes $\nu$ quasi-invariant under every left translation.

A nonzero inner-regular Radon measure $\nu$ on $G$ with that property
is equivalent to left Haar measure. We prove this by compact
localization. Choose $0\ne w\in C_c(G)_+$ and let

$$ r(t)=\int_G w(ts^{-1})\Delta_G(s)^{-1}\,d\nu(s),
       \qquad \nu_w=r(t)\,dt. $$

For $t$ in a compact set, the contributing $s$ lie in a single compact
set, namely $(\operatorname{supp}w)^{-1}K_t$. Thus $r$ is finite and
continuous by uniform continuity and dominated integration on that
compact set. The support of a nonzero quasi-invariant Radon measure
is nonempty: otherwise a compact set of positive measure would have a finite cover by null open neighborhoods. Quasi-invariance makes the support invariant under every left translation, hence all
of $G$. The integrand is strictly positive on a nonempty open set
of $s$ for each $t$, so $r(t)>0$ everywhere. The measure $\nu_w$ is
therefore equivalent to inner-regular Haar.

For a compact Borel set $C\subset G$, [HR5](OA-FLOW-HR.md#hr-05), restricted to the two finite compact Radon factors, and the right-translation factor in (Q1) give

$$ \nu_w(C)=\int_G w(a)\nu(a^{-1}C)\,da. $$

This calculation involves only $a\in\operatorname{supp}w$ and
$s\in(\operatorname{supp}w)^{-1}C$, both compact portions with finite
measures. If $\nu(C)=0$, quasi-invariance makes the right side zero.
If $\nu_w(C)=0$, the integrand vanishes for almost every $a$ on the
nonempty open set where $w>0$. Choose one such $a$; quasi-invariance
then gives $\nu(C)=0$. For an arbitrary Borel $A$, a null value is
equivalent to nullity of every compact subset, for both measures.
It follows that $\nu\sim\nu_w\sim ds$. This proof does not replace
compact localization by an unverified global averaging identity.

Now suppose $\mu_\rho(E)=0$ for a Borel $E\subset Y$.
For any compact $C\subset q^{-1}(E)$, choose $f\in C_c(G)_+$ with
$f\ge1$ on $C$. The Borel extension of (Q9) gives
$\int_{q^{-1}(E)}f\rho\,ds=0$. Since $\rho$ has a positive minimum
on $C$, this implies $ds(C)=0$. Inner regularity gives
$ds(q^{-1}(E))=0$. Conversely, if the preimage is Haar-null, for
every compact $B\subset E$ choose $F\in C_c(Y)_+$ with $F\ge1$
on $B$, and put $f=(F\circ q)k\in C_c(G)_+$. Then $Qf=F$,
so the same identity gives $\int_E F\,d\mu_\rho=0$, hence
$\mu_\rho(B)=0$. Inner regularity gives $\mu_\rho(E)=0$.
Therefore

<a id="equation-q15"></a>

$$ E\subseteq Y\text{ is negligible}
 \quad\Longleftrightarrow\quad q^{-1}(E)\subseteq G
                 \text{ is Haar-negligible}. \tag{Q15} $$

This holds for the stated inner-regular Borel measures and their
null-set completions. The same compact cutoff argument applied to
(Q14) says $\mu(E)=0$ iff $\nu(q^{-1}(E))=0$. Since $\nu\sim ds$,
every nonzero quasi-invariant inner-regular Radon measure on $Y$
has exactly the null sets of $\mu_\rho$. The cutoff tests every
coset, without requiring finite measure of a whole noncompact
fiber. Inner regularity, rather than a countable global exhaustion,
is the step passing from compact tests to all Borel null sets.

<a id="oa-flow.qm.derivative"></a>

## The Radon–Nikodym sign and a check

For the *pullback-on-sets* convention $(\mu_\rho\circ T_a)(E)=\mu_\rho(aE)$, the derivative at $y=sH$ is

<a id="equation-q16"></a>

$$ \frac{d(\mu_\rho\circ T_a)}{d\mu_\rho}(y)
      =c(a,y)=\frac{\rho(as)}{\rho(s)}. \tag{Q16} $$

To see this, apply (Q8) to $F(a^{-1}y)$ and substitute $s=at$. The ratio $\rho(at)/\rho(t)$ is constant on each coset; the remaining $k(at)$ integrates to one along every coset, just as $k(t)$ does. This proves (Q16) on $C_c(Y)$ using (Q9). Both the translated measure and the measure with the displayed positive continuous density are inner regular; uniqueness of their continuous-test functional gives the identity on every Borel set. No general non-sigma-finite Radon–Nikodym existence theorem is being invoked. For the usual pushforward $(T_a)_*\mu_\rho(E)=\mu_\rho(a^{-1}E)$, the derivative instead is

<a id="equation-q17"></a>

$$ \frac{d(T_a)_*\mu_\rho}{d\mu_\rho}(sH)
       =\frac{\rho(a^{-1}s)}{\rho(s)}. \tag{Q17} $$

These are two conventions for inverse translations, not competing modular formulas. The induced-representation formula in the next source passage must use the convention appropriate to its change of variables.

**Problem.** Take $G$ discrete and $H$ any subgroup. Compute the correction and a quotient measure.

**Solution.** Normalize both subgroup and group Haar measures to counting measure. Both modular functions are one, so $\rho=1$ works. Counting measure on $G/H$ obeys (Q9): the sum over cosets of the sum over each $H$-fiber is the sum over $G$. With $ds=c_G\,\mathrm{count}$ and $dh=c_H\,\mathrm{count}$ instead, the quotient measure is $(c_G/c_H)\,\mathrm{count}$. Both derivatives (Q16)–(Q17) are one for either normalization.

**Example with a nontrivial ratio.** In the orientation-preserving affine group, write $(a,b)(a',b')=(aa',b+ab')$ with $a>0$, and take $H=\{(a,0):a>0\}$. Then $ds=a^{-2}\,da\,db$, $dh=da/a$, $\Delta_G(a,b)=a^{-1}$ and $\Delta_H=1$. The right coset $(a,b)H$ is determined by $b$, and $\rho(a,b)=a$ obeys (Q7). Equation (Q9) gives ordinary Lebesgue measure $db$ on $G/H\cong\mathbb R$. The element $(a_0,b_0)$ acts by $b\mapsto b_0+a_0b$: the pullback-on-sets derivative (Q16) is $a_0$, while the usual pushforward derivative (Q17) is $a_0^{-1}$. This directly tests both the subgroup modular ratio and the inverse-translation convention.

The affine calculation requires only iterated one-variable substitution, proved in [SC8](OA-FLOW-SC.md#sc-08), on the finite Radon products of [HR5](OA-FLOW-HR.md#hr-05). Left translation sends $(a,b)$ to $(a_0a,b_0+a_0b)$; the two scalar length factors $a_0$ cancel the density factor $a_0^{-2}$. For right translation $(a,b)\mapsto(aa_0,b+ab_0)$, first translate $b$ for each fixed $a$ and then rescale $a$; the transported measure of a set is $a_0^{-1}$ times its original measure. This proves the stated $\Delta_G$. On $H$, $da/a$ is invariant under multiplication, in either direction. Finally

<a id="equation-qa1"></a>

\[
 \int_G f(a,b)\rho(a,b)\,ds
 =\int_{\mathbb R}\int_0^\infty f(a,b)\,\frac{da}{a}\,db
 =\int_{\mathbb R}Qf(b)\,db ,
 \tag{QA1}
\]
first for compact continuous $f$, proving the quotient normalization without a multivariable change-of-variables import.

**Problem.** Why is the pointwise wording of (Q7) stronger than the necessary condition for an arbitrary locally integrable $\varphi$?

**Solution.** A density is an $L^1_{\mathrm{loc}}$ equivalence class. Changing its value at one Haar-null point leaves the measure $\varphi(s)\,ds$ unchanged but may break a pointwise identity. Descent therefore tests (Q10) almost everywhere for each fixed $r$; the constructed continuous representative $\rho$ obeys (Q7) everywhere.

**Problem.** In the example $G=\mathbb R_{\mathrm{discrete}}\times\mathbb R$, explain why the two Haar representatives agree on compact tests but have different null sets. What happens if the discrete factor is countable?

**Solution.** A compact set meets only finitely many discrete components, and both measures there are the finite sum of ordinary Lebesgue measures. The vertical preimage $\mathbb R_{\mathrm{discrete}}\times\{0\}$ has inner measure zero. Every open neighborhood contains an interval of positive length in each component. An uncountable family of positive lengths has infinite sum: for some integer $n$, infinitely many lengths exceed $1/n$, unless the family of positive lengths were countable. Thus every such neighborhood has infinite outer measure. For a countable discrete factor the group is sigma-compact; the bridge and [HR3](OA-FLOW-HR.md#hr-03) show that the representatives agree on every Borel set. In particular the vertical preimage is then null for both. Compact agreement alone did not justify the uncountable conclusion.

The classical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem X.4.1, printed pages290–291 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). That source states the group-theoretic result by reference. The complete quotient calculation, measure-class argument, density-representative qualification and inner-regular bridge are written here. QF1–3 and the exact H0, HR and L24 proofs cited above provide the earlier foundations. The discrete, affine and non-sigma-compact examples test the normalization and the two different translation conventions.

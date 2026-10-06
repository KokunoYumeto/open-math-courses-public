# Inducing a representation through a quotient measure

A representation of a closed subgroup can be carried across the coset space, but its vector fields cannot simply be periodic along the subgroup. Their covariance includes the square root of the subgroup modular ratio. This lesson constructs the Hilbert space, proves its completeness and the density of elementary fields, and obtains the strongly continuous translation and imprimitivity representations.

*Programme exposition written in Codex (OpenAI), September 2026; foundation integration and proof restoration by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is dedicated under CC0 to the extent of rights held. No human review is asserted.*

The exact earlier local inputs are [QF6](OA-FLOW-QF.md#qf-6) for compactwise strong measurability and finite-measure vector integration, [L24 Section3](OA-FLOW-L24.md#oa-flow.grp.translations) for translations and inversion, [L24 Proposition4.1](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) for Bochner integration, [HR5](OA-FLOW-HR.md#hr-05) for compact Radon Fubini, and CF8 for Hilbert orthogonal complements. Sequential convergence, scalar Cauchy–Schwarz and Fatou are [SC4–7](OA-FLOW-SC.md#sc-04). The quotient measures and their exact all-Borel convention are the whole preceding chapter.

<a id="oa-flow.ind.setting"></a>

## Data, covariance and the quotient norm

Let $G$ be a locally compact Hausdorff group, $H\subseteq G$ a closed subgroup, and $V:H\to\mathcal U(K)$ a strongly continuous unitary representation on an arbitrary Hilbert space $K$. We retain the left Haar, inner-regular Radon and modular conventions of [lesson 43](OA-FLOW-L43.md). No countability assumption on $G$ or $K$ is required. Put

<a id="equation-i1"></a>

$$ Y=G/H,\qquad
 \chi(h)=\frac{\Delta_G(h)}{\Delta_H(h)}
       \quad(h\in H). \tag{I1} $$

A vector field is **locally measurable** if, on each compact subset and after discarding a set of arbitrarily small Haar measure, its restriction to a remaining compact subset is continuous. Its values on each compact then lie almost everywhere in a separable closed subspace of $K$: take continuous compact restrictions with omitted measures tending to zero and span their countable union of compact metric images. On that compact the field is strongly measurable. Conversely strong measurability on a compact gives the stated continuity property by the complete simple-function and almost-uniform argument in [QF6](OA-FLOW-QF.md#qf-6). This is a local condition; it does not place all values on $G$ in one separable subspace.

We can use Borel representatives without narrowing that class. Write $G$ as the topological disjoint union of cosets $O_i$ of an open sigma-compact subgroup, as in lesson 43. In each $O_i$ choose a compact exhaustion $C_{i,n}$ whose interiors cover $O_i$. Choose compact $F_{i,n,m}\subseteq C_{i,n}$ on which the field is continuous, with omitted measure less than $2^{-m}$. For fixed $n,m$, the union $F_{n,m}=\bigcup_i F_{i,n,m}$ is closed in $G$, and the field is continuous there, because the components are open and closed. The complement of the countable union of the $F_{n,m}$ is a Borel set null on every compact, hence Haar-null by inner regularity. Set the field to zero there. A countable partition obtained by taking the first such closed set has continuous restrictions, so the result is Borel and agrees with the original field locally almost everywhere. Call it a regular representative. Countable common refinements show that sums, norms and scalar products of regular representatives are Borel.

Let $\mathscr E$ consist of these locally measurable fields, represented as above, whose squared norms are locally integrable and which satisfy

<a id="equation-i2"></a>

$$ \xi(sh)=\chi(h)^{-1/2}V(h)^*\xi(s)
       \quad\text{locally Haar-almost everywhere in }s,
       \text{ for each fixed }h\in H. \tag{I2} $$

The exceptional set may depend on $h$. The scalar density $\|\xi(s)\|^2$ obeys the right-$H$ covariance (Q10) of lesson 43. It therefore determines a positive Radon measure $\mu_\xi$ on $Y$ by

<a id="equation-i3"></a>

$$ \int_Y Qf(y)\,d\mu_\xi(y)
       =\int_G f(s)\|\xi(s)\|^2\,ds,
       \qquad f\in C_c(G). \tag{I3} $$

Choose the continuous cutoff $k$ of lesson 43, with $Qk=1$ and support proper over compact subsets of $Y$. Test (I3) with $k(s)F(sH)$ for $F\in C_c(Y)_+$, $F\leq1$; this is compactly supported by properness of the cutoff. Taking the supremum over these $F$ gives the total mass of $\mu_\xi$ by inner regularity. The same supremum is the integral of $k\|\xi\|^2$: each compact subset of $G$ has compact image in $Y$, where such an $F$ can equal one. Thus

<a id="equation-i4"></a>

$$ \|\xi\|_{\mathrm{ind}}^2:=\mu_\xi(Y)
       =\int_G k(s)\|\xi(s)\|^2\,ds. \tag{I4} $$

This value is independent of $k$. Let $\mathscr E_2$ be the fields of finite norm, and identify fields of zero norm. The polarization identity turns (I4) into

<a id="equation-i5"></a>

$$ \langle\xi,\eta\rangle_{\mathrm{ind}}
    =\int_G k(s)\langle\xi(s),\eta(s)\rangle\,ds. \tag{I5} $$

Here the Hilbert inner product is linear in the first variable. The right side is independent of the cutoff because the cross-density has the same right-$H$ covariance and is a linear combination of positive densities.

<a id="oa-flow.ind.complete"></a>

## Local control and completeness

For every compact $C\subseteq G$, choose $g\in C_c(G)_+$ with $g\geq1$ on $C$. Equation (I3) yields

<a id="equation-i6"></a>

$$ \int_C\|\xi(s)\|^2\,ds
 \leq\int_G g(s)\|\xi(s)\|^2\,ds
 =\int_Y Qg\,d\mu_\xi
 \leq\|Qg\|_\infty\|\xi\|_{\mathrm{ind}}^2. \tag{I6} $$

Cauchy–Schwarz also gives

<a id="equation-i7"></a>

$$ \int_C\|\xi(s)\|\,ds
   \leq |C|^{1/2}\|Qg\|_\infty^{1/2}
                      \|\xi\|_{\mathrm{ind}}. \tag{I7} $$

These inequalities show that a field of zero induced norm is zero locally almost everywhere. Conversely a locally zero field gives the zero measure in (I3), hence zero induced norm. This is the equivalence relation we use.

They also prove completeness without a countable exhaustion of $G$. Let $(\xi_n)$ be Cauchy in induced norm and choose a subsequence $(\eta_j)$ with $\sum_j\|\eta_{j+1}-\eta_j\|_{\mathrm{ind}}<\infty$. Use regular representatives. By (I7) and scalar monotone convergence on each compact $C$, the sum $\sum_j\|\eta_{j+1}(s)-\eta_j(s)\|$ is integrable on $C$. Its convergence set $D$ is Borel by the measurable operations just proved. The Borel complement is null on every compact, hence Haar-null by inner regularity. Define $\xi(s)$ by the absolutely convergent vector series on $D$ and by zero outside $D$.

The limit is Borel: on $D$ its distance to each closed subset of $K$ is the pointwise limit of the distances of $\eta_j$, and vanishing of that distance characterizes membership in the closed set. On each compact, all the $\eta_j$ take values almost everywhere in the closed span of countably many separable subspaces. Their limit is strongly measurable there and locally measurable in the stated sense. Regularize it if necessary, changing it only locally almost everywhere. Equation (I6) and the triangle inequality bound its local $L^2$ tails by a compact-dependent constant times $\sum_{j\geq J}\|\eta_{j+1}-\eta_j\|_{\mathrm{ind}}$. Thus the subsequence converges locally in $L^2$ to $\xi$. No uncountable union of null sets or global separable range was used.

For each fixed $h\in H$, right translation by $h$ preserves the Haar measure class and is bounded on each local $L^2$ region after moving the compact set. Passing to the local $L^2$ limit in (I2) proves that $\xi$ also obeys (I2). It has locally integrable squared norm. Apply Fatou in (I4) along the pointwise convergent subsequence $(\eta_j)$. For fixed $n$, the numbers $\|\xi_n-\xi_m\|_{\mathrm{ind}}$ have a limit as $m\to\infty$, by the reverse triangle inequality and the Cauchy property. Hence their subsequence limit is the full liminf, and

<a id="equation-i8"></a>

$$ \|\xi_n-\xi\|_{\mathrm{ind}}^2
       \leq\liminf_{m\to\infty}
                   \|\xi_n-\xi_m\|_{\mathrm{ind}}^2. \tag{I8} $$

The Cauchy property makes the right side tend to zero as $n\to\infty$. Thus $\xi\in\mathscr E_2$ and $\mathcal H_{\mathrm{ind}}=\mathscr E_2/\{\|\xi\|_{\mathrm{ind}}=0\}$ is a Hilbert space. No pointwise identity for all $h$ on a common conull set was used.

<a id="oa-flow.ind.elementary"></a>

## Elementary fields and their pairing

For $f\in C_c(G)$ and $\eta\in K$ define

<a id="equation-i9"></a>

$$ A(f,\eta)(s)
     =\int_H\chi(h)^{1/2}f(sh)V(h)\eta\,dh. \tag{I9} $$

For each $s$ the integral ranges over a compact part of $H$. Left-Haar substitution $h\mapsto r^{-1}h$ shows

<a id="equation-i10"></a>

$$ A(f,\eta)(sr)=\chi(r)^{-1/2}V(r)^*A(f,\eta)(s), \tag{I10} $$

the same covariance as (I2). This field is continuous and vanishes outside $q^{-1}(q(\operatorname{supp}f))$. Since that quotient support is compact, the proper-support property of $k$ makes its induced norm finite.

The exact pairing is

<a id="equation-i11"></a>

$$ \langle A(f,\eta),\xi\rangle_{\mathrm{ind}}
     =\int_G f(s)\langle\eta,\xi(s)\rangle\,ds. \tag{I11} $$

To prove it, substitute (I9) into (I5), use finite Radon Fubini on the compactly localized support, and replace $s$ by $t=sh$. Proper support of $k$ over $q(\operatorname{supp}f)$ confines the relevant $s$ and $h$ to compact sets. Local strong measurability and (I7) give absolute integrability there; no global sigma-finite product assertion is needed. From (I2),
$V(h)^*\xi(s)=\chi(h)^{1/2}\xi(sh)$ almost everywhere. The two square-root factors combine to $\chi(h)$. The right translation Jacobian contributes $\Delta_G(h)^{-1}$, leaving $\Delta_H(h)^{-1}$. Inverting $h$ in $H$ then turns the remaining cutoff integral into $\int_H k(tr)\,dr=1$. This is exactly the modular cancellation already used in lesson 43.

If $\operatorname{supp}f\subseteq C$, (I7) and (I11) imply

<a id="equation-i12"></a>

$$ \|A(f,\eta)\|_{\mathrm{ind}}
  \leq |C|^{1/2}\|Qg\|_\infty^{1/2}
                      \|f\|_\infty\|\eta\|. \tag{I12} $$

The elementary fields have dense linear span. If $\xi$ is orthogonal to every $A(f,\eta)$, then (I11) says $\int f(s)\langle\eta,\xi(s)\rangle ds=0$ for every $f\in C_c(G)$ and $\eta\in K$. Each coefficient vanishes locally almost everywhere by uniqueness of its locally finite Radon density. Fix a compact $C$; local measurability puts $\xi(s)$ almost everywhere on $C$ in a separable closed subspace $E_C$. Choose a countable dense set of $\eta$ in $E_C$ and remove their countable union of exceptional sets on $C$. The remaining values belong to $E_C$ and are orthogonal to $E_C$, hence vanish. This works separately on every compact. Thus $\xi$ is locally zero and has zero induced norm by (I3); the orthogonal complement is zero.

<a id="oa-flow.ind.translation"></a>

## Translation gives the induced representation

For $t\in G$ put

<a id="equation-i13"></a>

$$ (U_t\xi)(s)=\xi(t^{-1}s). \tag{I13} $$

It preserves (I2). Left Haar invariance and (I3) show

<a id="equation-i14"></a>

$$ \mu_{U_t\xi}=(T_t)_*\mu_\xi,\qquad
        T_t(sH)=tsH, \tag{I14} $$

so $U_t$ preserves the induced norm; $U_{t^{-1}}$ is its inverse. The representation law is exact on equivalence classes. For an elementary field,

<a id="equation-i15"></a>

$$ U_tA(f,\eta)=A(L_tf,\eta),\qquad
       L_tf(s)=f(t^{-1}s). \tag{I15} $$

Near the identity, the supports of $L_tf-f$ lie in one compact $C$, and $L_tf\to f$ uniformly. Inequality (I12) therefore gives $U_tA(f,\eta)\to A(f,\eta)$ in induced norm. Density of the elementary fields and unitarity extend strong continuity to every vector. This is the induced representation $\operatorname{Ind}_H^G V$.

The square root in (I2) matters even though (I13) looks like ordinary left translation. In the affine example of lesson 43, $\chi(a,0)=a^{-1}$, so the subgroup covariance includes the factor $a^{1/2}$. Omitting it would make the quotient norm depend on the coset representative.

<a id="oa-flow.ind.imprimitivity"></a>

## The imprimitivity representation

For $F\in C_0(Y)$ define

<a id="equation-i16"></a>

$$ (\pi(F)\xi)(s)=F(sH)\xi(s). \tag{I16} $$

The scalar factor is constant along each right-$H$ coset, so (I2) survives. By (I3),

<a id="equation-i17"></a>

$$ \mu_{\pi(F)\xi}=|F|^2\mu_\xi,\qquad
           \|\pi(F)\|\leq\|F\|_\infty. \tag{I17} $$

Thus $\pi$ is a $*$-representation of $C_0(Y)$. It is nondegenerate: choose $0\le F\le1$ compactly supported and equal to one on a compact $C$ with $\mu_\xi(Y\setminus C)<\epsilon$. Every subsequent cutoff equal to one on a larger compact gives $\|(1-\pi(F))\xi\|^2\le\mu_\xi(Y\setminus C)<\epsilon$. Finite inner regularity gives such $C$, so the cutoff net converges strongly to the identity. This estimate uses no arbitrary-net dominated convergence. A direct calculation gives

<a id="equation-i18"></a>

$$ U_t\pi(F)U_t^*=\pi(\alpha_tF),
       \qquad (\alpha_tF)(sH)=F(t^{-1}sH). \tag{I18} $$

Consequently $(\pi,U)$ is a covariant representation of the translation system $(C_0(G/H),G)$, called the imprimitivity system of $\operatorname{Ind}_H^G V$.

<a id="oa-flow.ind.smoothing"></a>

## Smoothing yields continuous representatives

For $f\in C_c(G)$ and $\zeta\in\mathcal H_{\mathrm{ind}}$, the bounded operator $U(f)=\int_G f(t)U_t\,dt$ is defined vectorwise by the strongly continuous unitary action just proved. Its vector in the induced space has the continuous representative

<a id="equation-is1"></a>

\[
 v_f(s)=\int_G f(sr^{-1})\zeta(r)\Delta_G(r)^{-1}\,dr .
 \tag{IS1}
\]
For $s$ in a compact neighborhood, all contributing $r$ lie in one compact set. The local $L^1$ estimate (I7) and local strong measurability make this Bochner integral exist. The supremum of the change of the scalar kernel on that compact set tends to zero as $s$ changes; multiply that supremum by the finite integral of $\|\zeta(r)\|$ and the bounded modular factor. This proves norm continuity for arbitrary parameter nets.

We check that this pointwise formula gives the actual vector integral. First take a finite sum of elementary fields, which is continuous. Restriction to any compact $C\subset G$ is a bounded map from $\mathcal H_{\mathrm{ind}}$ to $L^2(C,K)$ by (I6). Passing that bounded map through $U(f)$, and using vector Fubini on the compact $t,s$-support, gives the field $\int f(t)\zeta(t^{-1}s)\,dt$. Inversion and Haar substitution from L24 turn it into (IS1). To justify the vector Fubini assertion here directly, the continuous field on the compact product has compact metric image, hence separable image. Approximate it uniformly by finite scalar functions times fixed vectors using H0; scalar HR5 and the uniform integral bound give both vector integrals. The ambient Hilbert space need not be separable.

For a general $\zeta$, approximate it in induced norm by finite sums $\zeta_n$ of elementary fields. The estimate (I7) shows that (IS1) for $\zeta_n$ converges uniformly on each compact to (IS1) for $\zeta$. Meanwhile $\|U(f)(\zeta_n-\zeta)\|\le\|f\|_1\|\zeta_n-\zeta\|$ and (I6) give convergence of the actual vectors locally in $L^2$. Thus the limits agree locally almost everywhere on every compact. The continuous representative (IS1) represents $U(f)\zeta$.

Its subgroup covariance is everywhere valid for each fixed $h$: the difference of the two continuous sides vanishes locally almost everywhere, and Haar positivity forces it to vanish at every point. Normalized nonnegative compact kernels supported in shrinking identity neighborhoods satisfy $\|U(f_V)\zeta-\zeta\|\le\sup_{t\in V}\|U_t\zeta-\zeta\|\to0$. Such kernels exist by H0 cutoffs and Haar positivity. Hence the span of these smooth vectors is dense. If an operator intertwines two group actions, bounded-map compatibility with the integral sends this span into the corresponding span. This statement concerns the whole group action, rather than an arbitrary value assigned to a measurable field.

**Problem.** If $H=G$, identify the induced representation.

**Solution.** The quotient has one point, and $\Delta_G|_H=\Delta_H$, so $\chi=1$. If $dh=c\,ds$, Haar uniqueness gives $c>0$. The continuous field $j(\eta)(s)=V(s)^*\eta$ has squared induced norm $c^{-1}\|\eta\|^2$, by (I3), so these fields form a closed subspace isomorphic to $K$. Every elementary field is of this form, by substituting $t=sh$ in (I9), and their values at $e$ are dense in $K$ by normalized compact kernels on $G$. Their density in the induced space proves that every class has this continuous representative. Evaluation at the identity, multiplied by $c^{-1/2}$, is unitary onto $K$, and (I13) becomes $V(t)$.

**Problem.** If $H=\{e\}$ and $K=\mathbb C$, identify $U$ and $\pi$.

**Solution.** Normalize the trivial-subgroup Haar measure by $dh(\{e\})=1$. The quotient is $G$, $Qf=f$, and the induced norm is the left-Haar $L^2(G)$ norm. Equation (I13) is the left regular representation. Equation (I16) is multiplication by $C_0(G)$, with the usual translation covariance. With the arbitrary normalization $dh=c\delta_e$, instead $Qf=cf$ and the induced squared norm is $c^{-1}\int_G|\xi(s)|^2\,ds$; the unitary $\xi\mapsto c^{-1/2}\xi$ identifies it with the same left regular representation.

The classical sources are M. Takesaki, *Theory of Operator Algebras II*, Lemmas X.4.2–4.3, Theorem X.4.4 and Definitions X.4.5–4.6, printed pages291–296 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)), and the local vector-field convention of *Theory of Operator Algebras I*, Definition IV.7.1 and Proposition IV.7.2. The proofs here include regular representatives, every compactwise countability step, completeness, elementary-field density and continuous representatives after smoothing. [The next chapter](OA-FLOW-L45.md) proves the converse, and [the intertwiner chapter](OA-FLOW-L46.md) identifies every covariant-system map.

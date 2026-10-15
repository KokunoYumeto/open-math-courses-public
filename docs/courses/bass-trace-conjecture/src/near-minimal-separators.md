# Near-minimal separators

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Keep the setting of [A transport metric with small balls](a-transport-metric-with-small-balls.md) and [Separating filtrations](separating-filtrations.md): the complex \(K\) of dimension \(n\ge n_0(D)\), the radii \(r<R\), the parameter space \((X,\mu)\), and admissible filtrations \((T_j,Z_j)_{j=0}^n\). This lesson chooses the filtration so that its last stratum \(Z_0\) has very few points on average over \(X\). At each stage the separator is chosen with area within \(\epsilon\) of the least possible. Cutting a ball open and inserting a level set is an admissible competitor, which bounds the area of each separator inside a ball by the area of a slice of the preceding stratum. Slicing relates these areas across dimensions, and after \(n\) steps the strict volume margin of the first lesson of this part forces the expected number of points of \(Z_0\) in a ball to be of order \(\epsilon\). The method is Papasoglu's comparison of a near-minimal separating set with a cut through a ball [Papasoglu, Section 2, Lemma 2.5], in the iterated and equivariant form of Alpert [Alpert, Lemmas 6, 7, 11, 12]; the lesson follows [OpenAI-BT, Section 5].

- Area functionals and near minimizers (Section 1).
- Disjoint replacements (Section 2).
- Slicing (Section 3).
- The number of zero strata (Section 4).

## 1. Area functionals and near minimizers

**Proposition 1.1** ([OpenAI-BT, Proposition 5.1]). For every \(\epsilon>0\) there is an admissible filtration \((T_j,Z_j)_{j=0}^n\) such that for every top simplex \(\sigma\) of \(K\)
\[
\begin{aligned}
&\int_X\#\bigl(Z_0(x)\cap\sigma\bigr)\,d\mu(x)\\
&\quad\le C_\sigma\,\epsilon ,
\end{aligned}
\tag{1.1}
\]
where \(C_\sigma\) depends on \(K\), \(D\), \(n\) and \(\sigma\), but not on \(\epsilon\) and not on the triangulations.

By Lemma 5.3 of [Separating filtrations](separating-filtrations.md), every point of \(Z_0(x)\) lies in the relative interior of a top simplex, so \(\#(Z_0(x)\cap\sigma)\) is finite and locally constant in \(x\), and the integral is defined.

For a locally constant equivariant family \(Z\) of subcomplexes of dimension at most \(j\), write \(\mathcal A_j^\sigma(Z,x)=a_j^\sigma\bigl(Z(x)\cap\sigma^\circ\bigr)\) and define
\[
\mathcal I_j(Z)=\sum_{\sigma}\frac1{|H_\sigma|}\int_X\mathcal A_j^\sigma(Z,x)\,d\mu(x),
\]
the sum over a set of representatives \(\sigma\) of the finitely many \(H\)-orbits of top simplices, with \(H_\sigma\) the finite stabilizer of \(\sigma\) (Lemma 3.2(d) of [A transport metric with small balls](a-transport-metric-with-small-balls.md)) and \(a_j^\sigma\) the averaged tree area of that lesson. The integrand is locally constant, and by (4.1) of that lesson and the invariance of \(\mu\), a different choice of representatives gives the same value. Each integrand takes finitely many finite values, so \(\mathcal I_j(Z)<\infty\).

*Construction.* Fix \(\epsilon>0\). Start with \((T_n,Z_n)=(K,|K|)\). For \(d=n,n-1,\ldots,1\), keep the choices made so far fixed and choose an admissible choice \((T_{d-1},Z_{d-1})\) at stage \(d\) with
\[
\begin{aligned}
&\mathcal I_{d-1}(Z_{d-1})\\
&\quad\le\inf\mathcal I_{d-1}(Z')+\epsilon ,
\end{aligned}
\tag{1.3}
\]
the infimum over all admissible choices \((T',Z')\) at stage \(d\). Admissible choices exist by Lemma 5.1 of [Separating filtrations](separating-filtrations.md), and the infimum is a finite nonnegative number, so such a choice exists. No minimum and no limit of filtrations is used. Inequality (1.3) holds for every admissible competitor at stage \(d\), with the data down to stage \(d\) fixed; it says nothing about later stages.

## 2. Disjoint replacements

Fix the filtration of Section 1 and a center \(c\in|K|\). By Lemma 3.2(e) of [A transport metric with small balls](a-transport-metric-with-small-balls.md), the set
\[
\begin{aligned}
\mathcal F_c=\{&h\in H\setminus\{1\}:\\
&L_R(hc)\cap L_R(c)\ne\varnothing\}
\end{aligned}
\]
is finite. By Lemma 1.2 of [Separating filtrations](separating-filtrations.md) there is a finite partition \(\mathcal A_c\) of \(X\) into clopen sets \(A\) with \(A\cap hA=\varnothing\) for all \(h\in\mathcal F_c\). It depends on \(c\) but not on \(\epsilon\).

**Lemma 2.1.** For \(A\in\mathcal A_c\), the sets \(hA\times L_R(hc)\), \(h\in H\), are pairwise disjoint.

*Proof.* If \(hA\cap h'A\ne\varnothing\) and \(L_R(hc)\cap L_R(h'c)\ne\varnothing\) for \(h\ne h'\), then \(k=h^{-1}h'\ne1\) satisfies \(A\cap kA\ne\varnothing\) and \(L_R(c)\cap L_R(kc)\ne\varnothing\), so \(k\in\mathcal F_c\), a contradiction. \(\square\)

Fix \(A\in\mathcal A_c\) and a clopen set \(B\subseteq A\). For \(r\le s\le R\), \(0\le j\le n\) and \(t\in(r,R)\) let \(m_j(x,s)\) be the sum of \(a_j^\sigma\bigl(Z_j(x)\cap\sigma^\circ\cap L_s(c)\bigr)\), and \(n_j(x,t)\) the sum of \(a_j^\sigma\bigl(Z_{j+1}(x)\cap\sigma^\circ\cap S_t(c)\bigr)\), over the top simplices \(\sigma\), and put
\[
\begin{aligned}
M_j(s)&=\int_B m_j(x,s)\,d\mu(x),\\
N_j(t)&=\int_B n_j(x,t)\,d\mu(x),
\end{aligned}
\]
where the sums run over all top simplices, without stabilizer weights; only finitely many meet \(L_R(c)\). The second quantity is defined when \(Z_{j+1}(x)\cap S_t(c)\) has dimension at most \(j\), which holds for \(t\) outside a countable set by the genericity in Lemma 4.1 of [Separating filtrations](separating-filtrations.md). The function \(s\mapsto M_j(s)\) is nondecreasing.

**Lemma 2.2** (local comparison). For every \(d\) with \(1\le d\le n\) and all \(t\in(r,R)\) outside a countable set,
\[
M_{d-1}(t)\le N_{d-1}(t)+\epsilon .
\tag{2.1}
\]

*Proof.* Write \(P=Z_d\) and \(Z=Z_{d-1}\). For each \(x\) make the replacement
\[
\begin{aligned}
Z'(x)={}&\Bigl(Z(x)\setminus\bigcup_{h:\,x\in hB}U_t(hc)\Bigr)\\
&\cup\Bigl(P(x)\cap\bigcup_{h:\,x\in hB}S_t(hc)\Bigr).
\end{aligned}
\]
For fixed \(x\), the active closed balls \(L_R(hc)\) with \(x\in hB\subseteq hA\) are pairwise disjoint by Lemma 2.1. The family of pairs \((hc,hB)\) is invariant, and only finitely many balls \(L_R(hc)\) meet a given original simplex. Lemma 4.1 of [Separating filtrations](separating-filtrations.md), with \(T=T_d\), \(S=T_{d-1}\), \(P=Z_d\), \(Z=Z_{d-1}\), gives for \(t\) outside a countable set a locally constant equivariant refinement in which \(Z'\) is a subcomplex. It satisfies condition 2 of admissibility relative to \(T_d\), and its complement in \(P(x)\) has components of diameter at most \(2R\). So \(Z'\) is an admissible competitor at stage \(d\), and (1.3) gives \(\mathcal I_{d-1}(Z)\le\mathcal I_{d-1}(Z')+\epsilon\).

The same lemma, applied with \(S=T_{d-1}\), shows that \(Z(x)\) meets every inserted level set in dimension at most \(d-2\), and the empty set if \(d=1\). Hence the \((d-1)\)-area of \(Z(x)\) inside an open active ball equals that inside the closed ball, and the inserted slice overlaps the retained part of \(Z(x)\) in zero \((d-1)\)-area. With the disjointness of the active balls,
\[
\begin{aligned}
&a^\sigma_{d-1}\bigl(Z'(x)\cap\sigma^\circ\bigr)-a^\sigma_{d-1}\bigl(Z(x)\cap\sigma^\circ\bigr)\\
&\quad=\sum_{h:\,x\in hB}a^\sigma_{d-1}\bigl(P(x)\cap\sigma^\circ\cap S_t(hc)\bigr)\\
&\qquad-\sum_{h:\,x\in hB}a^\sigma_{d-1}\bigl(Z(x)\cap\sigma^\circ\cap L_t(hc)\bigr).
\end{aligned}
\]
Let \(Q\) be one of the equivariant families \(P\cap S_t(\cdot)\) or \(Z\cap L_t(\cdot)\), written \(Q(x,hc)\), and put \(\alpha(\sigma,x,c')=a_{d-1}^\sigma\bigl(Q(x,c')\cap\sigma^\circ\bigr)\). Using the substitution \(x=hy\), the invariance of \(\mu\), the equivariance \(Q(hy,hc)=hQ(y,c)\) and (4.1) of [A transport metric with small balls](a-transport-metric-with-small-balls.md), which give \(\alpha(\sigma,hy,hc)=\alpha(h^{-1}\sigma,y,c)\),
\[
\begin{aligned}
&\sum_{\sigma}\frac1{|H_\sigma|}\sum_{h\in H}\int_{hB}\alpha(\sigma,x,hc)\,d\mu(x)\\
&\ =\sum_{\sigma}\frac1{|H_\sigma|}\sum_{h\in H}\int_B\alpha(h^{-1}\sigma,y,c)\,d\mu(y)\\
&\ =\int_B\sum_{\tau\ \mathrm{top}}\alpha(\tau,y,c)\,d\mu(y),
\end{aligned}
\]
because \(h\mapsto h^{-1}\sigma\) takes every value in the orbit of \(\sigma\) exactly \(|H_\sigma|\) times. All terms are nonnegative, and for a fixed representative only finitely many \(h\) contribute, so the rearrangements are finite. Applied to both families this gives
\[
\begin{aligned}
&\mathcal I_{d-1}(Z')-\mathcal I_{d-1}(Z)\\
&\quad=N_{d-1}(t)-M_{d-1}(t),
\end{aligned}
\]
and with (1.3) the assertion. \(\square\)

## 3. Slicing

**Lemma 3.1.** Let \(Q\) be a convex polytope of dimension \(d\ge1\) in a Euclidean space and \(f\) an affine function on its affine span whose gradient there has norm \(\alpha>0\). For \(a<b\),
\[
\begin{aligned}
&\int_a^b\operatorname{vol}_{d-1}\bigl(Q\cap\{f=t\}\bigr)\,dt\\
&\quad=\alpha\,\operatorname{vol}_d\bigl(Q\cap\{a<f<b\}\bigr).
\end{aligned}
\]
The integrand is bounded and continuous except at finitely many points.

*Proof.* Choose orthonormal coordinates \((x_1,\ldots,x_d)\) on the span of \(Q\) with \(f=\alpha x_1+\text{const}\). The set \(Q\cap\{a<f<b\}\) is a polytope, Jordan measurable since its boundary lies in finitely many hyperplanes. By Fubini's theorem ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20): Lebl, *Basic Analysis II*, Theorem 10.2.3 with Propositions 10.5.1 and 10.5.5), its volume is the integral over \(x_1\) of the \((d-1)\)-volumes of the slices \(\{x_1=\text{const}\}\). Substituting \(t=\alpha x_1+\text{const}\) gives the factor \(1/\alpha\). The slice volume is a piecewise polynomial function of \(t\), continuous where the combinatorial type of the slice does not change. \(\square\)

**Lemma 3.2** (slicing). There is a Riemann integrable function \(\tilde N_{d-1}\) on \((r,R)\), equal to \(N_{d-1}\) outside a countable set, such that for \(r\le b\le R\)
\[
\int_r^b\tilde N_{d-1}(t)\,dt\le M_d(b).
\tag{3.1}
\]

*Proof.* Fix a top simplex \(\sigma\), a tree Euclidean structure on it, and a point \(x\). The set \(Z_d(x)\cap\sigma^\circ\) is a finite disjoint union of relatively open convex polytopes; refining by the sign conditions between the finitely many branches of \(f_c\) on \(\sigma\), we may assume that on each piece \(Q\) the function \(f_c\) equals one branch, an affine function. Let \(\tilde N_{d-1}(t)\) be defined like \(N_{d-1}(t)\), but counting only the \((d-1)\)-volumes of the slices \(Q\cap\{f_c=t\}\) of the \(d\)-dimensional pieces \(Q\) on which \(f_c\) has nonzero gradient. Outside a countable set of \(t\) it equals \(N_{d-1}(t)\): a piece of dimension less than \(d\), or a \(d\)-dimensional piece on which \(f_c\) is constant, meets \(\{f_c=t\}\) in zero \((d-1)\)-area except for at most one value of \(t\); there are finitely many pieces for each of the finitely many configurations of \(x\) and of top simplices meeting \(L_R(c)\). By Lemma 3.1 and Lemma 4.1 of [A transport metric with small balls](a-transport-metric-with-small-balls.md), which gives \(\alpha\le1\),
\[
\begin{aligned}
&\int_r^b\operatorname{vol}_{d-1}\bigl(Q\cap\{f_c=t\}\bigr)\,dt\\
&\quad\le\operatorname{vol}_d\bigl(Q\cap L_b(c)\bigr).
\end{aligned}
\]
Averaging over the tree structures, summing over pieces and over top simplices, and integrating over \(B\), a finite combination, gives (3.1). The function \(\tilde N_{d-1}\) is a finite combination of the integrands of Lemma 3.1, hence Riemann integrable. \(\square\)

The comparison takes place inside one top simplex with one Euclidean structure at a time; no compatibility of the structures across faces is used. By Lemma 5.2 of [Separating filtrations](separating-filtrations.md), \(Z_d\) meets a proper face of an original simplex in dimension at most \(d-1\), so such faces carry no \(d\)-area.

**Lemma 3.3.** Let \(u\), \(v\) be Riemann integrable on \([r,b]\) with \(u\le v\) outside a countable set. Then \(\int_r^bu\le\int_r^bv\).

*Proof.* Every subinterval of positive length contains points outside a countable set. Choosing such tags, every Riemann sum of \(v-u\) is nonnegative, and these sums converge to \(\int_r^b(v-u)\). \(\square\)

## 4. The number of zero strata

**Lemma 4.1.** For \(0\le d\le n\) and \(r\le b\le R\),
\[
\begin{aligned}
&M_d(b)\\
&\ \ge\frac{(b-r)^d}{d!}M_0(r)\\
&\quad-\epsilon\sum_{i=1}^d\frac{(b-r)^i}{i!} .
\end{aligned}
\tag{4.1}
\]

*Proof.* For \(d=0\) this is the monotonicity of \(M_0\). For \(d\ge1\), (3.1), Lemma 2.2, Lemma 3.3 and the induction hypothesis give
\[
\begin{aligned}
M_d(b)&\ge\int_r^b\tilde N_{d-1}(t)\,dt\\
&\ge\int_r^b\bigl(M_{d-1}(t)-\epsilon\bigr)\,dt\\
&\ge\frac{(b-r)^d}{d!}M_0(r)\\
&\quad-\epsilon\sum_{i=1}^{d-1}\frac{(b-r)^{i+1}}{(i+1)!}-\epsilon(b-r),
\end{aligned}
\]
where \(M_{d-1}\) is Riemann integrable because it is monotone. \(\square\)

*Proof of Proposition 1.1.* Put
\[
\begin{gathered}
L=R-r,\qquad A_n=\frac{L^n}{n!},\\
\mathcal E_n=\sum_{i=1}^n\frac{L^i}{i!}.
\end{gathered}
\]
Since \(Z_n(x)=|K|\), the volume bound of Proposition 5.2 of [A transport metric with small balls](a-transport-metric-with-small-balls.md) gives \(M_n(R)\le V_R\,\mu(B)\). With (4.1) for \(d=n\) and \(b=R\),
\[
\begin{aligned}
&A_n\,M_0(r)\\
&\quad\le V_R\,\mu(B)+\epsilon\,\mathcal E_n .
\end{aligned}
\tag{4.2}
\]
Choose
\[
B=A\cap\{x\in X:\ Z_0(x)\cap L_r(c)\ne\varnothing\}.
\]
This set is clopen: finitely many original simplices meet \(L_r(c)\), and the filtration data on them are constant on the pieces of a finite clopen partition. Choosing \(B\) after the filtration is legitimate, because every comparison (1.3) holds for every admissible competitor, whatever clopen set it is built from. Each \(x\in B\) has at least one point of \(Z_0(x)\) in \(L_r(c)\), lying in the relative interior of a top simplex and counted by \(a_0\), so \(\mu(B)\le M_0(r)\). The margin (5.2) of that lesson says \(V_R<A_n\), and (4.2) gives
\[
\begin{aligned}
&\int_A\#(Z_0(x)\cap L_r(c))\,d\mu\\
&\quad=M_0(r)\le\frac{\mathcal E_n}{A_n-V_R}\,\epsilon ;
\end{aligned}
\tag{4.3}
\]
the integral over \(A\) equals \(M_0(r)\) because the count vanishes on \(A\setminus B\).

Finally, a top simplex \(\sigma\) is compact, so it is covered by finitely many open balls \(U_r(c_1),\ldots,U_r(c_q)\). For each \(c_i\), let \(p_i\) be the number of sets in the partition \(\mathcal A_{c_i}\). Summing (4.3) over these sets and over \(i\),
\[
\begin{aligned}
&\int_X\#\bigl(Z_0(x)\cap\sigma\bigr)\,d\mu\\
&\ \le\sum_{i=1}^q\int_X\#\bigl(Z_0(x)\cap L_r(c_i)\bigr)\,d\mu\\
&\ \le\frac{\mathcal E_n}{A_n-V_R}\Bigl(\sum_{i=1}^qp_i\Bigr)\epsilon .
\end{aligned}
\]
The centers, the partitions and the constants were fixed before \(\epsilon\). \(\square\)

No bound on the number of simplices of the triangulations, or on the number of points of an individual \(Z_0(x)\), is used.

## 5. Exercises

**5.1** (easy). Show that \(\mathcal I_j(Z)\) does not depend on the choice of the orbit representatives.

**5.2** (easy). Verify (4.1) for \(d=1\) directly from Lemmas 2.2 and 3.2.

**5.3** (medium). Let \(Q\subseteq\mathbb R^2\) be the unit square and \(f(x_1,x_2)=(x_1+x_2)/\sqrt2\). Compute \(\operatorname{length}(Q\cap\{f=t\})\) and check Lemma 3.1 with \(a=0\), \(b=\sqrt2\).

**5.4** (medium). In (4.3), why is it necessary that \(V_R<A_n\) strictly? What does (4.2) give if \(V_R\ge A_n\)?

**5.5** (medium). Show that the function \(x\mapsto\#(Z_0(x)\cap L_r(c))\) is locally constant on \(X\).

## 6. Solutions

**5.1.** Replacing \(\sigma\) by \(h\sigma\) replaces the integrand \(\mathcal A_j^\sigma(Z,x)=a_j^\sigma(Z(x)\cap\sigma^\circ)\) by \(a_j^{h\sigma}(Z(x)\cap h\sigma^\circ)=a_j^\sigma(Z(h^{-1}x)\cap\sigma^\circ)\), by equivariance of \(Z\) and (4.1) of [A transport metric with small balls](a-transport-metric-with-small-balls.md). Invariance of \(\mu\) gives the same integral, and \(|H_{h\sigma}|=|H_\sigma|\) since the stabilizers are conjugate.

**5.2.** Using that \(M_0\) is nondecreasing,
\[
\begin{aligned}
M_1(b)&\ge\int_r^b\tilde N_0\ge\int_r^b(M_0(t)-\epsilon)\,dt\\
&\ge(b-r)M_0(r)-\epsilon(b-r).
\end{aligned}
\]

**5.3.** The gradient of \(f\) has norm \(\alpha=1\). For \(0\le t\le\sqrt2\) the line \(x_1+x_2=\sqrt2\,t\) meets the square in a segment of length \(\sqrt2\cdot\min(\sqrt2t,\,2-\sqrt2t)\). As a function of \(t\), this length rises linearly from \(0\) to \(\sqrt2\) at \(t=\sqrt2/2\) and falls back to \(0\) at \(t=\sqrt2\): its graph bounds a triangle of base \(\sqrt2\) and height \(\sqrt2\), so the integral is \(1=\alpha\operatorname{vol}_2(Q)\).

**5.4.** The bound (4.3) divides by \(A_n-V_R\). If \(V_R\ge A_n\), (4.2) together with \(\mu(B)\le M_0(r)\) only gives \((A_n-V_R)M_0(r)\le\epsilon\mathcal E_n\), which bounds nothing when the left coefficient is not positive. The margin (5.2) is the only place where the dimension enters.

**5.5.** The ball \(L_r(c)\) meets finitely many original simplices (Lemma 3.2(a) of [A transport metric with small balls](a-transport-metric-with-small-balls.md)). On each of them, \(Z_0(x)\) is constant on the pieces of a finite clopen partition, and a common refinement of these partitions makes the whole configuration inside \(L_r(c)\), hence the count, constant on each piece.

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Section 5, Proposition 5.1. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
- [Papasoglu] P. Papasoglu, *Uryson width and volume*, Geometric and Functional Analysis 30 (2020), 574–587; arXiv:1909.03738, Section 2. https://arxiv.org/abs/1909.03738
- [Alpert] H. Alpert, *Simplicial volume and 0-strata of separating filtrations*, arXiv:2211.06362v3, Lemmas 6, 7, 11 and 12. https://arxiv.org/abs/2211.06362

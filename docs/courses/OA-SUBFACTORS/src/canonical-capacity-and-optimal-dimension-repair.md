# Canonical capacity and optimal dimension repair

An integer target must fit the actual canonical algebra before rounding can succeed. We identify a structural restriction on that capacity: its finite part lives on at most countably many central atoms, and its value on each atom is at least the reciprocal of the atom's inherited trace. Every diffuse central region has infinite capacity. We then prove that trim and fill repairs any feasible bounded dimension with the smallest possible squared Hilbert–Schmidt distance. The resulting rounding estimate uses an \(L^1\) profile error and allows a varying capacity and a diffuse center.

The exact local inputs are [52.2–52.4](canonical-core-traces-and-integer-rounding.md) (actual centers, trace measures, matrix deletion and prescription in a finite projection), [58.16](larger-factor-central-balancing.md) and the proof of 58.5 (extended central dimensions and bounded prescription under an arbitrary projection), and [68.12](core-central-transition-bounds.md) (the larger dimension of a projection in the expected smaller algebra). The bounded-prescription proof in Lesson 58 does not use its surrounding assumption that the larger core is a factor; we check its inputs below. Factor trace uniqueness, corner centers and projection comparison retain the declared programme prerequisites of Lesson 52. We prove the new capacity restriction, optimal distance and quantitative consequences here.

Human-source context is Sorin Popa, *Classification of amenable subfactors of type II*, DOI 10.1007/BF02392646, Theorem4.2.2, printed pp.213–214. The estimates below identify a sufficient dimension input for its rounding step. General relative amenability has not yet supplied that input. No unrestricted rounding, near-one common bounded frame, full partition or generation conclusion is inferred.

## Unit capacity in either canonical row

Let \(S\subset R\) be an actual core for a proper finite-index inclusion \(N\subset M\) of II₁ factors. Use either of the two rows

\[
\begin{gathered}
(F,L,\mathcal C)=(N,S,A)\\
\text{or }(M,R,B),\\
e=e_R^M,\quad A=\langle N,e\rangle,\\
B=\langle M,e\rangle,\quad U=Z(L).
\end{gathered}
\tag{85.1}
\]

The canonical trace on \(\mathcal C\) is \(\operatorname{Tr}\). Its full Jones corner is \(Le\), and the inherited probability trace on \(L\) is \(\tau\). For \(z\in U\), write \(\widehat z\in Z(\mathcal C)\) for the canonical lift. Thus \(e\widehat z=ez\), and \(\operatorname{Tr}(e\widehat z)=\tau(z)\). Physical \(z\in L\subset F\) and represented \(\widehat z\) are distinguished throughout.

For arbitrary projections, the generalized dimension is extended, as in (58.16). The unit capacity is the possibly infinite central function

\[
\begin{gathered}
K=C_{\mathcal C}(1)\in[1,\infty]^U,\\
\operatorname{Tr}(\widehat z)=\tau(Kz)
\\ (z\in U\text{ a projection}).
\end{gathered}
\tag{85.2}
\]

The notation means a positive extended measurable function, not that \(K\) is a bounded operator. Its measure is the finite measure \(\tau\) on \(U\). Semifiniteness and normality give this extension: take the directed family of finite projections under a given projection and the increasing supremum of their central densities. Finite joins keep the family directed. The finite center measure permits a countable subfamily with the same essential supremum, by maximizing the integrals of bounded truncations; this is precisely the construction in (58.16). It works in either row without factoriality of \(\mathcal C\). Since \(e\leq1\) and \(C_{\mathcal C}(e)=1\), the lower bound in (85.2) follows.

**Lemma 85.1 — every finite central unit has trace at least one.** If \(0\neq z\in U\) is a projection and \(\operatorname{Tr}(\widehat z)<\infty\), then

\[
\operatorname{Tr}(\widehat z)\geq1.
\tag{85.3}
\]

**Proof.** Put \(t=\operatorname{Tr}(\widehat z)>0\). The functional \(x\mapsto\operatorname{Tr}(\widehat z x)\) is a finite normal trace on the ambient factor \(F\): positivity and normality follow from the trace, and traciality uses that \(\widehat z\) commutes with \(F\). Factor trace uniqueness therefore gives \(\operatorname{Tr}(\widehat z x)=t\tau_F(x)\). For the physical projection \(z\in L\subset F\), this yields \(\operatorname{Tr}(\widehat z z)=t\tau(z)\).

The Jones projection commutes with every physical element of \(L\). The two commuting projections \(\widehat z,z\) have product \(\widehat z z\), which majorizes \(e\widehat z=ez\). Indeed this Jones-corner projection is fixed by both of them. Monotonicity gives \(\tau(z)=\operatorname{Tr}(e\widehat z)\leq t\tau(z)\). Faithfulness of the inherited trace gives \(\tau(z)>0\), so divide by it. This proves (85.3). Neither \(\widehat z=z\) nor commutation of the entire smaller represented center with \(M\) is assumed. \(\square\)

**Theorem 85.2 — the finite capacity part is atomic.** If a central projection \(z\) has finite unit trace \(t=\operatorname{Tr}(\widehat z)\), then \(zU\) has at most \(\lfloor t\rfloor\) atoms. In particular:

\[
\begin{gathered}
\{K<\infty\}\\
\text{is a countable union of atoms},\\
u\text{ an atom},\quad m=\tau(u)>0:\\
K(u)<\infty\ \Longrightarrow\ K(u)\geq1/m,\\
K=\infty\text{ on the diffuse part of }U.
\end{gathered}
\tag{85.4}
\]

**Proof.** Every nonzero subprojection of \(z\) has a finite represented central unit trace and hence trace at least 1 by Lemma85.1. An orthogonal family under \(z\) can consequently have at most \(\lfloor t\rfloor\) members. Repeatedly split any nonatom in a finite partition of \(z\). The bound forces this process to end in an atomic partition. Each atom has scalar abelian corner by spectral calculus, so the asserted dimension bound follows.

For each positive integer \(n\), the spectral set \(z_n=1_{\{K\leq n\}}\) has \(\operatorname{Tr}(\widehat z_n)=\tau(Kz_n)\leq n\tau(z_n)\leq n\). A nonzero such set is therefore a finite sum of atoms of \(U\). Their increasing union is the finite-capacity region, proving countability. On an atom \(u\), the extended function \(K\) is a scalar, and \(\operatorname{Tr}(\widehat u)=mK(u)\). When finite, Lemma85.1 gives \(mK(u)\geq1\).

Finally the diffuse part is the complement of the sum of all atoms of \(U\). There are at most countably many atoms: for each positive integer \(j\), at most \(j\) have trace at least \(1/j\), and every positive atom trace exceeds such a threshold for some \(j\). None of the finite-capacity spectral sets meets the diffuse part. Thus \(K=\infty\) there. Infinite-capacity atoms are also allowed. \(\square\)

This theorem describes actual canonical capacity. It does not conclude that the inherited center measure is atomic, and it does not bound the normalized dimensions of arbitrary finite projections on an infinite center.

## General prescription with a varying capacity

**Proposition 85.3 — bounded prescription below an arbitrary projection.** If \(r\in\mathcal C\) is a projection and a bounded positive central function \(h\) satisfies \(h\leq C_{\mathcal C}(r)\), there is a finite-trace projection \(r_h\leq r\) with dimension \(h\).

**Proof by the checked factor-free argument of 58.5.** Choose an integer \(b\geq\max(1,\|h\|_\infty)\). In \(M_b(\mathcal C)\), normalize the central dimension by \(e\otimes E_{11}\). The finite projection \(e\otimes1_b\) has dimension \(b1\). Its type II corner and 52.4 give a finite projection \(t_h\) of dimension \(h\).

Compare \(t_h\) with \(r\otimes E_{11}\) by the maximal partial-isometry argument of 58.5. Its only inputs are central support comparison, polar decomposition, normality of dimension and faithfulness of a finite projection's dimension. If a residual initial part \(t_0\neq0\) survives, its central support \(z\) is disjoint from the residual final support. On \(z\), all of \(r\otimes E_{11}\) is the final range of the partial isometry already used, with dimension \(hz-C(t_0)\). That contradicts \(C((r\otimes E_{11})z)\geq hz\), since \(C(t_0)\) is positive on its nonzero central support. Thus the initial residual is zero. The final range lies under \(r\otimes E_{11}\), identifies with \(r_h\) in its first corner and has dimension \(h\). It has finite trace \(\tau(h)\).

Every hypothesis just listed holds for both type II canonical rows of 52.2. No constant unit capacity and no factor center of the larger core enter this proof. Thus the proof in 58.5 supplies precisely the broader statement above; we have not imported its separate constant-capacity Lemma58.4. \(\square\)

For a finite projection \(p\), write \(\zeta=C_{\mathcal C}(p)\). Additivity of extended dimension gives

\[
\begin{gathered}
C_{\mathcal C}(1-p)=K-\zeta,\\
\infty-\zeta=\infty
\quad(K=\infty).
\end{gathered}
\tag{85.5}
\]

Here \(\zeta\) is finite almost everywhere because it is integrable. On finite-capacity regions the subtraction is ordinary; on infinite-capacity regions it has the indicated extended meaning.

## The exact least-cost repair

**Theorem 85.4 — optimal dimension repair.** Let \(p\in\mathcal C\) be finite trace, with dimension \(\zeta\), and let \(h\) be a bounded positive central function. A projection of dimension \(h\) exists if and only if \(h\leq K\). Under this feasibility condition there is a finite projection \(q\) commuting with \(p\) such that

\[
\begin{gathered}
C_{\mathcal C}(q)=h,\\
\|p-q\|_{2,\operatorname{Tr}}^2
=\|\zeta-h\|_{L^1(U,\tau)}.
\end{gathered}
\tag{85.6}
\]

This is the least squared distance among all projections of dimension \(h\), including those that do not commute with \(p\).

**Proof of existence and the attained cost.** Necessity of \(h\leq K\) follows from \(q\leq1\). For sufficiency, 52.4 gives a projection \(p_-\leq p\) of dimension \(\min(\zeta,h)\). Equation (85.5) and \(h\leq K\) show that \((h-\zeta)_+\leq C_{\mathcal C}(1-p)\). This missing dimension is bounded by \(h\), so Proposition85.3 gives \(p_+\leq1-p\) of dimension \((h-\zeta)_+\). Put \(q=p_-+p_+\). Its parts are orthogonal, and both commute with \(p\). They give exactly dimension \(h\).

The orthogonal removed and added pieces have dimensions \((\zeta-h)_+\) and \((h-\zeta)_+\), respectively. Thus

\[
\begin{gathered}
\|p-q\|_2^2\\
=\operatorname{Tr}(p-p_-)+\operatorname{Tr}(p_+)\\
=\tau((\zeta-h)_+)+\tau((h-\zeta)_+)\\
=\|\zeta-h\|_1.
\end{gathered}
\tag{85.7}
\]

Both pieces are finite trace because \(\zeta\) and \(h\) are integrable.

**Proof of optimality.** For any finite projection \(q_1\) with dimension \(h\), the positive trace-class operator \(pq_1p\) defines a positive normal functional on the center. Let its density be \(\omega\). The operator inequalities \(pq_1p\leq p\) and \(q_1pq_1\leq q_1\), together with cyclicity in every central pairing, give

\[
\begin{gathered}
0\leq\omega\leq\min(\zeta,h),\\
\operatorname{Tr}(pq_1p)=\tau(\omega).
\end{gathered}
\tag{85.8}
\]

Indeed pairing with each positive bounded central test gives the two upper bounds, and finite-measure \(L^1\) duality gives the density inequalities. Cyclicity also makes \(\operatorname{Tr}(pq_1)=\operatorname{Tr}(pq_1p)\) real and nonnegative. Expanding the Hilbert–Schmidt square therefore yields

\[
\begin{gathered}
\|p-q_1\|_2^2
=\tau(\zeta)+\tau(h)-2\tau(\omega)\\
\geq\tau(\zeta+h-2\min(\zeta,h))\\
=\|\zeta-h\|_1.
\end{gathered}
\tag{85.9}
\]

Equation (85.7) attains this bound. The optimal projection need not be unique. \(\square\)

**Corollary 85.5 — direct commutator cost.** For \(q\) from (85.6), put \(c=\tau(\zeta)>0\), \(t=\tau(h)>0\), and \(D=\|\zeta-h\|_1\). For every ambient unitary \(u\in\mathcal U(M)\), in the smaller row,

\[
\begin{gathered}
\frac{\|[q,u]\|_2}{\sqrt t}
\\ \leq
\frac{\|[p,u]\|_2}{\sqrt c}\sqrt{\frac ct}
+2\sqrt{\frac Dt}.
\end{gathered}
\tag{85.10}
\]

**Proof.** The triangle inequality gives \(\|[q,u]\|_2\leq\|[p,u]\|_2+\|[q-p,u]\|_2\). Unitary invariance bounds the last term by \(2\|q-p\|_2=2\sqrt D\). Divide by \(\sqrt t\). All norms use the larger canonical trace, whose restriction to the smaller algebra is the same trace by 52.2. This proof requires no commutation of \(u\) with the smaller center: it compares the entire repaired projection with \(p\). \(\square\)

## Matrix amplification preserves feasibility

Return to the smaller row \(A\), and denote its capacity by \(K_A\). Deleting a common \(M_n\subset S\) gives the actual new core \(S^0\subset R^0\) and canonical pair \(\widetilde A\subset\widetilde B\) of 52.3. Its unit and old projection dimensions satisfy

\[
\begin{gathered}
K_{\widetilde A}=n^2K_A,\\
C_{\widetilde A}(p)=n^2\zeta,\\
\widetilde{\operatorname{Tr}}(p)=n^2c.
\end{gathered}
\tag{85.11}
\]

For the unit identity, apply the finite-projection scaling of 52.3 to the directed finite projections under \(1\), then use normality of the extended dimension. Both algebras have the same unit and center. Relative ambient commutator defects of old projections are unchanged.

Fix a nonzero projection \(z\in Z(S)\) and a scalar \(\theta>0\) satisfying \(\theta z\leq K_A\). The scalar profile has mass \(t=\theta\tau(z)>0\). Define

\[
\begin{gathered}
\rho=\|\zeta-\theta z\|_1/t,\\
k=\lfloor n^2\theta\rfloor,\quad
b=1/(n^2\theta),\\
0<b<1.
\end{gathered}
\tag{85.12}
\]

There is no assumption here that \(z\) is in \(Z(R)\). The profile error includes the entire mass of \(p\) outside \(z\), so an additional noncommuting central cut is unnecessary. The feasibility inequality and (85.11) imply \(kz\leq K_{\widetilde A}\).

**Theorem 85.6 — rounding from a feasible \(L^1\) scalar profile.** Under (85.12), optimal repair in \(\widetilde A\) produces a finite projection \(q_n\) with \(C_{\widetilde A}(q_n)=kz\). For \(\delta_u(p)=\|[p,u]\|_2/\sqrt c\),

\[
\begin{gathered}
\delta_u(q_n)\\
\leq\delta_u(p)\sqrt{\frac{1+\rho}{1-b}}
+2\sqrt{\frac{\rho+b}{1-b}}.
\end{gathered}
\tag{85.13}
\]

The projection is a sum of \(k\) orthogonal pieces equivalent inside \(\widetilde A\) to \(e_{R^0}^M\widehat z\). If additionally \(z\in Z(R)\), its larger dimension is also \(kz\).

**Proof.** The positive masses differ by at most their \(L^1\) density difference, so \(c\leq(1+\rho)t\). The floor gives \(k\geq n^2\theta-1=(1-b)n^2\theta>0\). By the triangle inequality,

\[
\begin{gathered}
D_n:=\|n^2\zeta-kz\|_1\\
\leq n^2\rho t+\tau(z),\\
\frac{D_n}{k\tau(z)}
\leq\frac{\rho+b}{1-b},\\
\frac{n^2c}{k\tau(z)}
\leq\frac{1+\rho}{1-b}.
\end{gathered}
\tag{85.14}
\]

Theorem85.4 gives the exact minimum squared distance \(D_n\). Apply (85.10) with the new traces, then substitute (85.14), using the unchanged relative defect of \(p\). This proves (85.13). Since \(kz\) is a feasible bounded dimension, every application of prescription is justified.

Divide the dimension \(kz\) into \(k\) orthogonal pieces of dimension \(z\) by 52.4. The final zero-dimension remainder is zero by faithfulness. The new Jones corner \(e_{R^0}^M\widehat z\) has that same dimension, so each piece is equivalent to it. The larger dimension is \(E_{Z(R^0)}(kz)\) by (68.12). It equals \(kz\) when the additional common-center membership holds. \(\square\)

For a concrete tolerance, let \(\varepsilon_*=\min(\varepsilon,1)\). The following conditions suffice:

\[
\begin{gathered}
\rho<\varepsilon_*^2/256,\\
\delta_u(p)<\varepsilon_*/4
\quad(u\in\mathcal F),\\
b\leq\varepsilon_*^2/256,\quad
n^2\theta\geq k_0+1.
\end{gathered}
\tag{85.15}
\]

Here \(\mathcal F\) is any prescribed finite set and \(k_0\geq1\). The last two conditions are choices of \(n\) after a feasible profile is available. They give \(k\geq k_0\). The first square-root factor in (85.13) is less than \(\sqrt2\), since \((1+\rho)/(1-b)<257/255<2\). Its contribution is less than \(\varepsilon_*/2\). The second contribution is at most \(2\varepsilon_*\sqrt{2/255}<\varepsilon_*/4\), by squaring the latter inequality. Thus the resulting defect is strictly smaller than \(3\varepsilon_*/4<\varepsilon\).

The \(L^1\) scalar-profile and capacity conditions in (85.12)/(85.15) have not been obtained from general amenability. Theorem84.4 supplies a different proved route under finite smaller center. A diffuse center alone guarantees capacity, not a nearly scalar dimension profile.

**Capacity obstruction survives amplification.** If \(\theta z\not\leq K_A\), a positive central subset \(w\leq z\) and some scalar \(\alpha>0\) satisfy \(K_A\leq\theta-\alpha\) on \(w\). Whenever \(n^2\alpha>1\), the proposed integer \(k=\lfloor n^2\theta\rfloor\) satisfies

\[
k>n^2K_A\quad\text{on }w.
\tag{85.16}
\]

Indeed \(k\geq n^2\theta-1>n^2(\theta-\alpha)\). No projection of dimension \(kz\) then exists. Such \(w,\alpha\) follow by taking a positive-measure level set of \(\theta-K_A\). Thus increasing the matrix size does not repair an infeasible limiting scalar target; the floor can only hide a discrepancy at small sizes.

## Finite central partitions and one simultaneous extraction

A preselected finite projection need not have almost all its dimension near one scalar. We can approximate that dimension by finitely many scalar levels, repair every positive cell, and select one cell for the entire finite target set. The additional quantity that must be controlled is the actual pinching energy between the represented central cells. We first prove its exact identity.

**Exact pinching identity.** Let \(p\) be a finite-trace projection in \(B\), and let \(p_0,\ldots,p_r\) be orthogonal projections summing to \(p\). For every unitary \(u\in M\),

\[
\begin{aligned}
\sum_{i=0}^r\|[p_i,u]\|_{2,\operatorname{Tr}}^2
&=\|[p,u]\|_{2,\operatorname{Tr}}^2
 +2\sum_{\substack{0\le i,l\le r\\i\ne l}}
       \|p_iup_l\|_{2,\operatorname{Tr}}^2\\
&=\|[p,u]\|_{2,\operatorname{Tr}}^2
 +2\left\|pup-\sum_{i=0}^r p_iup_i\right\|_{2,\operatorname{Tr}}^2.
\end{aligned}
\tag{85.17}
\]

**Proof of the identity.** For any finite projection \(a\), the two operators \(au\) and \(ua\) have squared \(L^2\) norm \(\operatorname{Tr}(a)\). Their inner product is
\(\operatorname{Tr}(u^*aua)=\operatorname{Tr}(au^*aua)=\|aua\|_2^2\), a real nonnegative number. The middle equality is trace cyclicity; the factors are bounded and the products are trace class. Expanding the square gives
\(\|[a,u]\|_2^2=2\operatorname{Tr}(a)-2\|aua\|_2^2\).

The finite expansion \(pup=\sum_{i,l}p_iup_l\) is orthogonal in \(L^2(B,\operatorname{Tr})\). Indeed the inner product of \(p_iup_l\) and \(p_aup_b\) is
\(\operatorname{Tr}(p_lu^*p_ip_aup_b)\). It is zero if \(i\ne a\). If \(i=a\) and \(l\ne b\), cyclicity places the orthogonal factors \(p_b p_l\) next to each other and again gives zero. Thus
\(\|pup\|_2^2=\sum_{i,l}\|p_iup_l\|_2^2\); the same orthogonality applies to the off-diagonal sum. Subtracting the formula for \(a=p\) from the sum of the formulas for \(a=p_i\), and using \(\sum_i\operatorname{Tr}(p_i)=\operatorname{Tr}(p)\), gives both equalities in (85.17). Every product used is supported on finite projections, so no finite trace on the unit of \(B\) is needed. \(\square\)

**Theorem 85.7 — finite central partition extraction certificate.** Use an actual core and its smaller canonical row \(A\subset B\), the common canonical trace and the inherited probability measure on \(U=Z(S)\), as in (85.1) and 52.2. Fix ambient unitaries \(u_1,\ldots,u_m\in M\), where \(m\ge1\), and an integer \(k_0\ge1\). Let \(0\ne p\in A\) be a finite-trace projection, and let \(z_0,z_1,\ldots,z_r\in U\) be an orthogonal finite partition of \(1\). Omit zero-measure positive cells; the zero cell \(z_0\) is allowed to be zero. Suppose

\[
\begin{gathered}
\zeta=C_A(p),\qquad c=\tau(\zeta)=\operatorname{Tr}(p)>0,\\
h=\sum_{i=1}^r\theta_i z_i\le\zeta,\qquad \theta_i>0,\\
t=\tau(h)>0,\qquad
\rho=\frac{\tau(\zeta-h)}t,\qquad c=(1+\rho)t .
\end{gathered}
\tag{85.18}
\]

Put \(p_i=p\widehat z_i\), including \(i=0\), where \(\widehat z_i\) is the represented lift in \(Z(A)\). Define the whole-projection and pinching errors by

\[
\begin{aligned}
\delta^2&=\frac1c\sum_{j=1}^m
            \|[p,u_j]\|_{2,\operatorname{Tr}}^2,\\
\Lambda&=\sum_{j=1}^m
          \sum_{\substack{0\le i,l\le r\\i\ne l}}
            \|p_i u_jp_l\|_{2,\operatorname{Tr}}^2,\qquad
\mu=\frac{2\Lambda}{c}.
\end{aligned}
\tag{85.19}
\]

These numbers are finite, since every \(p_i\) has finite trace. Make the common matrix deletion of 52.3, obtaining an actual core \(S^0\subset R^0\) for the same inclusion and canonical pair \(\widetilde A\subset\widetilde B\). Choose its size \(n\) so that

\[
\begin{gathered}
k_i=\lfloor n^2\theta_i\rfloor\ge k_0
        \quad(1\le i\le r),\\
s=\tau\left(\sum_{i=1}^r z_i\right),\qquad
b=\frac{s}{n^2t}<1 .
\end{gathered}
\tag{85.20}
\]

Then there is an \(i\ge1\) and a nonzero projection \(q_i\in\widetilde A\) with \(q_i\le p_i\), \(C_{\widetilde A}(q_i)=k_i z_i\), and

\[
\begin{gathered}
\max_{1\le j\le m}
 \frac{\|[q_i,u_j]\|_{2,\widetilde{\operatorname{Tr}}}}
      {\sqrt{\widetilde{\operatorname{Tr}}(q_i)}}\\
\le
\sqrt{\frac{1+\rho}{1-b}}\,\sqrt{\delta^2+\mu}
 +2\sqrt{\frac{m(\rho+b)}{1-b}}
 =:\Gamma .
\end{gathered}
\tag{85.21}
\]

It splits into \(k_i\) orthogonal projections, each equivalent inside \(\widetilde A\) to \(e_{R^0}^M\widehat z_i\). The selected support belongs to \(Z(S^0)=Z(S)\). Its larger dimension is also \(k_i z_i\) when the additional membership \(z_i\in Z(R)\) holds, by (68.12). Throughout, the target unitaries are arbitrary elements of \(M\); no invariance of the smaller center under them is assumed.

**Proof of feasible trimming and its exact total cost.** By 52.3, the old \(p_i\) has new smaller dimension \(n^2\zeta z_i\), and the centers and their probability measure are unchanged. Since \(k_i z_i\le n^2\theta_i z_i\le n^2\zeta z_i\), prescription in the finite projection \(p_i\), proved in 52.4, supplies \(q_i\le p_i\) of dimension \(k_i z_i\). Put \(q_0=0\) and \(T_n=\sum_{i=1}^r k_i\tau(z_i)>0\). Since every \(q_i\le p_i\), each difference \(p_i-q_i\) is a projection. Summing its trace gives the exact cost, including the discarded zero cell:

\[
\begin{aligned}
\sum_{i=0}^r
 \|p_i-q_i\|_{2,\widetilde{\operatorname{Tr}}}^2
 &=n^2c-T_n\\
 &\le n^2\rho t+s,\\
T_n&\ge n^2t-s=(1-b)n^2t,\\
\frac{n^2c}{T_n}&\le\frac{1+\rho}{1-b},\qquad
\frac{n^2c-T_n}{T_n}\le\frac{\rho+b}{1-b}.
\end{aligned}
\tag{85.22}
\]

For the inequalities, \(n^2\theta_i-1\le k_i\le n^2\theta_i\). Multiply by \(\tau(z_i)\) and sum to obtain \(n^2t-s\le T_n\le n^2t\). Then \(c-t=\rho t\) gives the displayed cost bound and both ratios. The lower bound \(h\le\zeta\) makes every trim feasible below the original projection. Unit capacity, including its infinite part, therefore introduces no additional prescription hypothesis.

**Proof of the simultaneous commutator estimate and selection.** Apply (85.17) to each \(u_j\), then sum over all targets. Equation (85.19) gives
\(\sum_{i,j}\|[p_i,u_j]\|_{2,\operatorname{Tr}}^2=c(\delta^2+\mu)\).
All these commutators belong to the old larger algebra, where the new trace scales by \(n^2\). The triangle inequality in the finite Hilbert direct sum indexed by \((i,j)\) now yields

\[
\begin{aligned}
\left(\sum_{i=0}^r\sum_{j=1}^m
  \|[q_i,u_j]\|_{2,\widetilde{\operatorname{Tr}}}^2\right)^{1/2}
&\le
 n\sqrt{c(\delta^2+\mu)}
 +2\sqrt{m(n^2c-T_n)},\\
\frac1{T_n}\sum_{i=1}^r\sum_{j=1}^m
  \|[q_i,u_j]\|_{2,\widetilde{\operatorname{Tr}}}^2
&\le\Gamma^2 .
\end{aligned}
\tag{85.23}
\]

Here unitary invariance gives
\(\|[q_i-p_i,u_j]\|_2\le2\|q_i-p_i\|_2\); summing its square over \(j\) gives the factor \(m\). Divide the first line by \(\sqrt{T_n}\) and use (85.22) to obtain the second line. The term for \(q_0=0\) vanishes.

The second line is a trace-weighted average of the nonzero \(q_i\)'s summed squared relative defects. At least one \(i\ge1\) therefore satisfies
\[
\frac{\sum_j\|[q_i,u_j]\|_{2,\widetilde{\operatorname{Tr}}}^2}
     {k_i\tau(z_i)}
\le\Gamma^2 .
\]
Otherwise the sum would exceed \(\Gamma^2T_n\). Each individual target defect is bounded by this summed defect, which proves (85.21) on one and the same cell. Finally divide the central dimension \(k_i z_i\) into \(k_i\) dimensions \(z_i\) by 52.4. Their sum exhausts \(q_i\), since a residual projection of zero dimension is zero by faithfulness. Each piece and the new Jones-corner projection have the same finite central dimension, so they are equivalent by the comparison argument of 52.4. \(\square\)

**A concrete tolerance for all targets.** For \(\varepsilon>0\), put \(\varepsilon_*=\min(\varepsilon,1)\). It suffices that

\[
\rho,b\le\frac{\varepsilon_*^2}{128m},
\qquad
\delta^2+\mu<\frac{\varepsilon_*^2}{8}.
\tag{85.24}
\]

Indeed \((1+\rho)/(1-b)\le129/127<2\). The first term in (85.21) is strictly below \(\varepsilon_*/2\). The second is at most
\(2\varepsilon_*/\sqrt{64(127/128)}<\varepsilon_*/3\): squaring the last comparison reduces to \(36<64(127/128)\). Thus every selected relative commutator defect is below \(5\varepsilon_*/6<\varepsilon\). After \(p,h\) are fixed, the finitely many positive \(\theta_i\)'s have positive minimum. Arbitrarily large common matrix factors in the type II core \(S\), as used in 52.3, permit both \(k_i\ge k_0\) and arbitrarily small \(b\). For this purpose even the matrix sizes obtained by repeated type II halving suffice.

**The scalar-step approximation is automatic.** For every \(\zeta\in L^1(U,\tau)_+\) of mass \(c>0\) and every \(0<\eta<1\), a nonzero finite scalar step function \(h\le\zeta\) satisfies \(\tau(\zeta-h)<\eta c\). To prove this, choose \(H<\infty\) with
\(\tau(\zeta1_{\{\zeta>H\}})<\eta c/2\), using integrability and decreasing-tail convergence. Choose \(a>0\) with \(a<\eta c/2\), and set

\[
h=a\lfloor\zeta/a\rfloor\,1_{\{0<\zeta\le H\}},
\qquad
z_i=1_{\{h=ia\}}\quad(i\ge1),\qquad
z_0=1_{\{h=0\}} .
\tag{85.25}
\]

Only finitely many positive \(z_i\)'s occur, because \(ia\le H\). Omit the null cells and relabel them; their positive coefficients are the corresponding values \(ia\). This gives a finite partition of \(1\), including the zero cell, and \(0\le h\le\zeta\). On \(0<\zeta\le H\) the pointwise rounding loss is less than \(a\); on \(\zeta>H\) the entire tail is discarded. Hence

\[
\begin{gathered}
0\le\tau(\zeta-h)
 \le a\,\tau(1)+\tau(\zeta1_{\{\zeta>H\}})
 <\eta c,\\
t=\tau(h)>(1-\eta)c>0,\qquad
\rho=\frac{c-t}{t}<\frac{\eta}{1-\eta}.
\end{gathered}
\tag{85.26}
\]

This constructs exactly the scalar data of (85.18) in an arbitrary finite center measure. It uses no atomicity, boundedness of \(\zeta\), dimension band or uniform integrability of a family of projections. On every cell the integer target after scaling fits below \(p_i\), even where capacity is finite.

**The remaining simultaneous input.** This scalar approximation does not control \(\Lambda\). The unrestricted task still requires, for each finite ambient target set and tolerance, an actual core, an actual finite projection \(p\), and a finite scalar partition for its dimension for which both \(\rho\) and \(\delta^2+2\Lambda/c\) are sufficiently small. General relative amenability supplies the whole-projection Følner estimate; obtaining it simultaneously with this actual pinching estimate remains unproved here. Fine partitions can add off-diagonal energy, as Exercise85.8 shows.

Theorem85.7 replaces neither the unrestricted source outcome nor the finite-center and special-factor routes. It shows that a proof from a preselected projection need not first approximate its whole dimension by one scalar: finitely many scalar levels and the simultaneous energy bound suffice. This observation concerns that intermediate route, rather than a claim of stronger existential generality. At an already successful scalar output with dimension \(kz\), faithfulness gives \(p\widehat{(1-z)}=0\). Taking the partition \(z,1-z\) and \(h=\zeta=kz\) gives \(\rho=0\) and \(\Lambda=0\). That endpoint check supplies no construction from arbitrary amenable data.

The support and integer extraction proved above retains arbitrary depth, diffuse centers and varying capacities. Near-one common bounded-frame support, an exact full whole-tunnel partition, common-stage alignment, prefix alignment and the unrestricted generation conclusions remain separate original obligations. No such conclusion follows merely by selecting the one cell in (85.21).

![Finite capacity atoms, the optimal trim-and-fill repair and squared amplification](figures/canonical-capacity-and-optimal-dimension-repair.svg)

*Figure85.1. The top panel depicts the proved capacity constraints in either actual canonical row; the diffuse region has infinite capacity, while finite-capacity atoms obey the reciprocal trace bound. The middle panel is a central-data diagnostic, with weights \(1/4,1/4,1/2\), dimensions \(\zeta=(3,1,2)\), target \(h=(2,2,2)\) and capacities \((8,8,\infty)\). It is not a claimed actual core realization. Each dimension unit has the same bar width, and bar heights are proportional to the inherited region weights; areas therefore encode the exact removed and added trace costs. The bottom panel states the feasible profile error and amplification estimate; no scalar-profile hypothesis is inferred. Proof locators: (85.3)–(85.9), Theorem85.6 and (85.11)–(85.16). Original editable source: [canonical-capacity-and-optimal-dimension-repair.py](figures/canonical-capacity-and-optimal-dimension-repair.py). Human context: Popa4.2.2, printed pp.213–214.*

![Finite central partition, exact pinching energy, simultaneous integer repair and weighted selection](figures/finite-partition-extraction-v3.svg)

*Figure85.2. Schematic of the actual operator mechanism of Theorem85.7. The zero cell includes discarded tails; all positive cells are trimmed after the same matrix deletion, and their total trace controls selection of one cell for every target. No area, box width or displayed partition is a numerical core realization. The pinching term uses represented smaller-center projections and arbitrary ambient unitaries. The simultaneous small-energy input is displayed as missing, rather than inferred. Exact proof locators: (85.17)–(85.23); automatic scalar approximation: (85.25)–(85.26). Matrix change and equivalence providers: 52.3–52.4. Human-source context: Popa, Theorem4.2.2, printed pp.213–214. [Editable figure source](figures/finite-partition-extraction-v3.py).*

## Exercises with complete solutions

### Exercise 85.1 — finite unit trace

An actual represented central unit has trace \(7/2\). How many central atoms can it contain? Can one of its nonzero central subunits have trace \(3/4\)?

**Solution.** Every nonzero represented central subunit has trace at least1 by Lemma85.1. Any orthogonal family under the given unit therefore has at most three members, since four would have total trace at least4. The splitting argument of85.2 proves that its entire center is a sum of at most three atoms. A nonzero central subunit of trace \(3/4\) is impossible. This restriction concerns central units, not arbitrary finite projections; type II projections can have much smaller scalar trace.

### Exercise 85.2 — atom trace and capacity

An actual smaller-center atom has inherited trace \(1/4\). What lower bound does85.2 give for its finite unit capacity? Compute the represented unit trace if its capacity is8.

**Solution.** The reciprocal trace bound gives capacity at least4. Capacity8 would give represented unit trace \((1/4)8=2\), consistent with the proved necessary bound of1. A proposed finite capacity2 would give unit trace \(1/2\) and violate Lemma85.1. Consistency with the lower bound alone does not construct an actual core or certify all its index restrictions.

### Exercise 85.3 — exact repair costs

Use the diagnostic of Figure85.1. Compute the kept dimension, removed dimension, added dimension and minimum squared distance.

**Solution.** The kept dimension is the coordinatewise minimum \((2,1,2)\). The removed dimension is \((1,0,0)\) and the added dimension is \((0,1,0)\). Their traces are \(1/4\) each, so the exact squared distance is \(1/2\). Both original and target dimensions have total trace2. The capacity inequality holds on all three regions, making the repair feasible. Theorem85.4 shows that allowing a repaired projection not commuting with the original cannot lower this cost.

### Exercise 85.4 — projection overlap

Suppose two finite projections have dimensions \(\zeta,h\), and their overlap density \(\omega\) in (85.8) falls below \(\min(\zeta,h)\) by a positive integrable function \(s\). Determine the excess squared distance over the optimal value.

**Solution.** Substitute \(\omega=\min(\zeta,h)-s\) into the exact first line of (85.9). The squared distance equals \(\|\zeta-h\|_1+2\tau(s)\). Thus its excess over the optimum is exactly \(2\tau(s)\). Positivity of \(s\) makes this nonnegative, and it is strictly positive when \(\tau(s)>0\). Equality at the optimum only requires saturation of the overlap density; no uniqueness of the repaired projection is asserted.

### Exercise 85.5 — amplification arithmetic

Let \(\theta=3/5\), \(\tau(z)=1/2\), \(n=10\), and \(\|\zeta-\theta z\|_1=3/1000\). Compute \(t,\rho,k,b\), and the actual triangle bound for \(D_n\).

**Solution.** The target mass is \(t=3/10\), so \(\rho=(3/1000)/(3/10)=1/100\). Since \(n^2\theta=60\) is an integer, \(k=60\) and \(b=1/60\). The floor correction here is zero, so the actual amplified difference is \(D_n=100(3/1000)=3/10\), not merely an upper bound. The rounded target mass is \(k\tau(z)=30\), and hence \(D_n/(k\tau(z))=1/100\). The general safe bound \((\rho+b)/(1-b)\) is larger because it allows a nonzero floor correction. These computations still require the stated feasibility inequality to produce a projection.

### Exercise 85.6 — diffuse capacity versus localization

Explain why infinite capacity on a diffuse center permits any bounded positive dimension target but does not itself provide the small error needed in (85.15).

**Solution.** If the whole center is diffuse,85.2 gives \(K_A=\infty\) there. Every bounded positive \(h\) is then feasible, and85.3 supplies a finite projection of exactly that dimension. Optimal repair still has the exact squared cost \(\|\zeta-h\|_1\), which can be large for an arbitrary initial projection. For example two disjoint central sets of equal measure can support normalized densities2 and0 in opposite orders, giving \(L^1\) distance2 despite unlimited capacity. Thus capacity removes the existence obstruction; closeness of the actual dimension profile remains a separate mathematical input to the ambient commutator estimate.

### Exercise 85.7 — quantitative selection for the whole target set

Use the projections \(q_1,\ldots,q_r\) produced in Theorem85.7 and its total trace \(T_n\). For a number \(\lambda>\Gamma\), call a cell good if every \(u_j\) has relative commutator defect at most \(\lambda\) on \(q_i\). Prove that the sum of the new traces of the good cells is at least
\[
\left(1-\frac{\Gamma^2}{\lambda^2}\right)T_n>0 .
\]
Explain precisely what support conclusion this proves, and whether it gives a near-one inherited central measure.

**Solution.** Set
\(t_i=\widetilde{\operatorname{Tr}}(q_i)=k_i\tau(z_i)>0\) and
\(E_i=\sum_{j=1}^m\|[q_i,u_j]\|_{2,\widetilde{\operatorname{Tr}}}^2\).
Equation (85.23) says \(\sum_iE_i\le\Gamma^2T_n\), and \(\sum_it_i=T_n\). If a cell is bad, at least one individual squared defect exceeds \(\lambda^2\), so \(E_i>\lambda^2t_i\). Consequently
\[
\sum_{\text{bad }i}t_i
\le\frac1{\lambda^2}\sum_{\text{bad }i}E_i
\le\frac{\Gamma^2}{\lambda^2}T_n .
\]
Subtracting from \(T_n\) proves the asserted lower bound for the good cells. Because \(\lambda>\Gamma\), that bound is positive, so there is a nonzero good cell on which all targets satisfy the same tolerance. The sum of the good projections has the stated retained canonical trace, but their inherited central measure is \(\sum_{\text{good }i}\tau(z_i)\), with weights \(t_i/k_i\). The integers \(k_i\) can vary and need not have a uniform ratio. The weighted trace estimate therefore does not supply a near-one central measure or a near-one common bounded frame. Theorem85.7 obtains its sharper tolerance \(\Gamma\) for a single cell by averaging the summed squared defects themselves.

### Exercise 85.8 — approximation from below and the cost of refinement

Let \(0\ne p\in A\) be a finite-trace projection, put \(\zeta=C_A(p)\in L^1(U,\tau)_+\) and \(c=\operatorname{Tr}(p)=\tau(\zeta)>0\), and prescribe \(r_0>0\). Construct a finite nonzero scalar step \(h\le\zeta\) with \(\rho=\tau(\zeta-h)/\tau(h)<r_0\).

Next consider any finite central partition \((z_i)_i\) and a finite refinement \(z_i=\sum_a w_{i,a}\). Put \(p_i=p\widehat z_i\) and \(p_{i,a}=p\widehat w_{i,a}\). For the same finite ambient unitary target set, prove the exact refinement formula
\[
\Lambda_{\mathrm{fine}}
=\Lambda_{\mathrm{coarse}}
 +\sum_{j=1}^m\sum_i\sum_{a\ne b}
   \|p_{i,a}u_jp_{i,b}\|_{2,\operatorname{Tr}}^2 .
\]
Deduce why accurate scalar approximation alone cannot justify the small pinching hypothesis.

**Solution.** Choose \(\eta=r_0/(1+r_0)\), which lies in \((0,1)\) and satisfies \(\eta/(1-\eta)=r_0\). Integrability supplies \(H<\infty\) with \(\tau(\zeta1_{\{\zeta>H\}})<\eta c/2\). Choose \(0<a<\eta c/2\). The function in (85.25) has finitely many positive values, is below \(\zeta\), and its total loss is less than \(\eta c\) by the pointwise mesh bound and tail estimate. Thus (85.26) makes it nonzero and gives \(\rho<r_0\). This argument is for the single given projection density; it requires no uniform bound for a family.

For different coarse cells \(i\ne l\), expand
\(p_i u_j p_l=\sum_{a,b}p_{i,a}u_jp_{l,b}\).
These finitely many blocks are orthogonal in \(L^2\) by exactly the left and right support calculation in the proof of (85.17). Therefore
\[
\|p_i u_jp_l\|_2^2
=\sum_{a,b}\|p_{i,a}u_jp_{l,b}\|_2^2 .
\]
In the fine pinching sum, the terms whose coarse labels differ add up to \(\Lambda_{\mathrm{coarse}}\). The remaining off-diagonal terms have the same coarse label \(i\) but different refinement labels \(a\ne b\), and give the displayed extra sum. All its terms are nonnegative, so \(\Lambda_{\mathrm{fine}}\ge\Lambda_{\mathrm{coarse}}\). Normalizing by the unchanged \(c\) gives the same monotonicity for \(\mu\). Refinement can improve the scalar mesh error while adding mixing energy. Neither the scalar approximation proof nor taking a finer partition bounds that added energy from above. Obtaining small profile loss and small actual pinching energy simultaneously is exactly the remaining input recorded after Theorem85.7.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October2026. Public domain (CC0).*
